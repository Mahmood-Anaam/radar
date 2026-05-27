#!/usr/bin/env python3
"""
RADAR — PAN 2026 Generative AI Authorship Verification
Submission script for the TIRA evaluation platform.

Usage:
    radar-predict INPUT_FILE OUTPUT_DIRECTORY

Arguments:
    INPUT_FILE        Path to the input JSONL file (each line: {"id": ..., "text": ...}).
    OUTPUT_DIRECTORY  Directory where predictions.jsonl will be written.

The model weights are loaded from the HuggingFace Hub repository
``MahmoodAnaam/RADAR``.  When running on the TIRA platform the model is
pre-mounted via ``--mount-hf-model MahmoodAnaam/RADAR``; no internet
connection is required at evaluation time.
"""

import json
import os
import sys
from pathlib import Path

import click
import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoTokenizer

# Register RADAR config / model with Hugging Face Auto-classes before loading.
from radar.modeling import RADARModel, registers

registers()

from radar.features import StylemetricFeatureExtractor, extract_features_batch  # noqa: E402
from radar.preprocessing import preprocess  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

MODEL_NAME = os.environ.get("RADAR_MODEL", "MahmoodAnaam/RADAR")
OUTPUT_FILE = "predictions.jsonl"
MAX_LENGTH = 512
BATCH_SIZE = int(os.environ.get("RADAR_BATCH_SIZE", "16"))
# Scores within this margin of 0.5 are snapped to 0.5 (abstain) to improve the
# c@1 metric, which rewards abstention when confidence is low rather than
# penalising an incorrect hard decision.  Value matches the PAN baselines.
C_AT_1_THRESHOLD = 0.01


# ---------------------------------------------------------------------------
# Prediction
# ---------------------------------------------------------------------------


@click.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.argument("output_directory", type=click.Path(file_okay=False, writable=True))
def main(input_file: str, output_directory: str) -> None:
    """
    Run RADAR on INPUT_FILE and write JSONL predictions to OUTPUT_DIRECTORY.

    Each output line has the form: {\"id\": \"<id>\", \"label\": <float in [0,1]>}
    where 0.0 = human-authored and 1.0 = AI-generated.
    """
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # ---- Device ----
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[RADAR] device: {device}", file=sys.stderr)

    # ---- Load model and tokenizer ----
    print(f"[RADAR] loading model from '{MODEL_NAME}' ...", file=sys.stderr)
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = RADARModel.from_pretrained(MODEL_NAME)
    except Exception as exc:
        print(
            f"[RADAR] ERROR: failed to load model/tokenizer from '{MODEL_NAME}': {exc}\n"
            "Ensure the model is pre-mounted with --mount-hf-model on TIRA, "
            "or set the RADAR_MODEL env var to a local path.",
            file=sys.stderr,
        )
        sys.exit(1)
    model.eval()
    model.to(device)
    print("[RADAR] model loaded.", file=sys.stderr)

    # ---- Stylometric extractor ----
    extractor = StylemetricFeatureExtractor()

    # ---- Read input ----
    records = []
    with open(input_file, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    print(f"[RADAR] {len(records):,} samples to predict.", file=sys.stderr)

    # ---- Predict ----
    output_path = Path(output_directory) / OUTPUT_FILE
    with open(output_path, "w", encoding="utf-8") as out:
        for batch_start in tqdm(
            range(0, len(records), BATCH_SIZE),
            desc="Predicting",
            unit="batch",
            file=sys.stderr,
        ):
            batch = records[batch_start : batch_start + BATCH_SIZE]
            ids = [r["id"] for r in batch]
            texts = [preprocess(r["text"]) for r in batch]

            # Tokenise
            encoding = tokenizer(
                texts,
                padding=True,
                truncation=True,
                max_length=MAX_LENGTH,
                return_tensors="pt",
            )
            input_ids = encoding["input_ids"].to(device)
            attention_mask = encoding["attention_mask"].to(device)

            # Extract stylometric features
            style_array = extract_features_batch(texts, extractor)  # (B, 38)
            style_features = torch.tensor(style_array, dtype=torch.float32, device=device)

            # Forward pass
            with torch.no_grad():
                outputs = model(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    style_features=style_features,
                )
                scores = torch.sigmoid(outputs.logits).cpu().numpy()  # (B,)

            for sample_id, score in zip(ids, scores):
                score = float(score)
                # Optimise c@1: abstain when confidence is near the decision boundary
                if abs(score - 0.5) < C_AT_1_THRESHOLD:
                    score = 0.5
                json.dump({"id": sample_id, "label": score}, out)
                out.write("\n")
        out.flush()

    print(f"[RADAR] predictions written to '{output_path}'.", file=sys.stderr)


if __name__ == "__main__":
    main()
