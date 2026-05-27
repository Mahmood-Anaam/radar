# RADAR — Submission Guide

**Task:** PAN 2026 Voight-Kampff Generative AI Authorship Verification  
**TIRA task ID:** `generative-ai-authorship-verification-panclef-2026`  
**HuggingFace model:** `******/RADAR`

---

## What Gets Submitted

When you run `tira-cli code-submission` (see below), TIRA packages **the entire
repository directory** into a Docker image and evaluates it by running the installed
`radar-predict` command.  Nothing is sent to the internet at evaluation time; the
model weights are mounted directly from the HuggingFace Hub snapshot via the
`--mount-hf-model` flag.

What TIRA uses from this repo:

| File / Directory | Purpose |
|---|---|
| `pyproject.toml` | Package metadata and `radar-predict` entry-point declaration |
| `radar/predict.py` | Prediction entry-point (CLI, preprocessing, inference) |
| `radar/modeling/` | `RADARModel` and `RADARConfig` (custom HF model classes) |
| `radar/features/` | `StylemetricFeatureExtractor` (38 stylometric features) |
| `pan26_genai_baselines/` | Evaluator utilities (local dependency) |
| `pan26_genai_evaluator/` | PAN 2026 evaluator (local dependency) |

---

## Input / Output Format

**Input** (`$inputDataset/dataset.jsonl`): newline-delimited JSON, one record per line:

```jsonl
{"id": "abc123", "text": "The quick brown fox ..."}
```

**Output** (`$outputDir/predictions.jsonl`): newline-delimited JSON, one record per line:

```jsonl
{"id": "abc123", "label": 0.97}
```

`label` is a float in **[0, 1]** where `0.0` = human-authored and `1.0` = AI-generated.
A value of exactly `0.5` means *undecidable* (the model abstains).

---

## Local Testing (Before Submitting)

### 1 — Install the package

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2 — Download the smoke-test dataset

```bash
pip install tira
tira-cli verify-installation
```

Then fetch the smoke-test data:

```bash
tira-cli dataset-submission \
  --path pan26-generative-ai-detection-smoke-test \
  --task generative-ai-authorship-verification-panclef-2026 \
  --split train \
  --dry-run
```

Or download the JSONL directly from the PAN GitHub repository:
[pan26-generative-ai-detection-smoke-test](https://github.com/pan-webis-de/pan-code/tree/master/clef26/generative-authorship-verification/pan26-generative-ai-detection-smoke-test)

### 3 — Run the predictor locally

```bash
mkdir -p /tmp/radar-out

radar-predict \
  pan26-generative-ai-detection-smoke-test/dataset.jsonl \
  /tmp/radar-out
```

The predictions are written to `/tmp/radar-out/predictions.jsonl`.

### 4 — Evaluate locally (optional)

```bash
pan26-evaluator \
  /tmp/radar-out/predictions.jsonl \
  pan26-generative-ai-detection-smoke-test/test-truth.jsonl \
  /tmp/radar-eval
```

---

## Submitting to TIRA

### Prerequisites

```bash
pip install tira
tira-cli verify-installation
```

### Step 1 — Smoke-test on the training split (dry run)

```bash
tira-cli code-submission \
  --dry-run \
  --path . \
  --task generative-ai-authorship-verification-panclef-2026 \
  --dataset pan26-generative-ai-detection-smoke-test-20260330-training \
  --mount-hf-model ******/RADAR \
  --command 'radar-predict $inputDataset/dataset.jsonl $outputDir'
```

Remove `--dry-run` once the output looks correct:

```bash
tira-cli code-submission \
  --path . \
  --task generative-ai-authorship-verification-panclef-2026 \
  --dataset pan26-generative-ai-detection-smoke-test-20260330-training \
  --mount-hf-model ******/RADAR \
  --command 'radar-predict $inputDataset/dataset.jsonl $outputDir'
```

### Step 2 — Submit to the official test set

```bash
tira-cli code-submission \
  --path . \
  --task generative-ai-authorship-verification-panclef-2026 \
  --dataset pan26-generative-ai-detection-20260330-test \
  --mount-hf-model ******/RADAR \
  --command 'radar-predict $inputDataset/dataset.jsonl $outputDir'
```

> **Note on internet access:** TIRA evaluation containers have **no outbound internet
> access**.  The `--mount-hf-model ******/RADAR` flag pre-fetches the model weights
> and makes them available inside the container via the standard HuggingFace Hub
> cache.  The `radar-predict` script loads the model with
> `RADARModel.from_pretrained("******/RADAR")`, which will resolve from the local
> cache without requiring a network connection.

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `RADAR_MODEL` | `******/RADAR` | HuggingFace model repository (name or local path) |
| `RADAR_BATCH_SIZE` | `16` | Number of samples processed per forward pass |

Example — run with a local model checkpoint:

```bash
RADAR_MODEL=/path/to/local/checkpoint \
  radar-predict dataset.jsonl /tmp/out
```

---

## Preprocessing Pipeline

The preprocessing applied at inference time is **identical** to the pipeline used
during training:

1. **PII removal** — e-mail addresses → `[EMAIL]`, `@username` mentions → `[USER]`,
   phone numbers → `[PHONE]`.
2. **Lowercase** — all text is converted to lower case.
3. **Strip** — leading and trailing whitespace is removed.

Short texts (< 50 characters after preprocessing) were excluded during training;
the inference script processes them normally but confidence is expected to be low.

---

## Architecture Summary

RADAR is a hybrid binary classifier with four modules:

1. **ARSE** — ModernBERT-large encoder producing a CLS semantic embedding.
2. **SLPE** — Stylometric feature extractor computing 38 linguistic features
   (vocabulary richness, syntactic complexity, discourse coherence, style
   fingerprinting, perplexity signals).
3. **Cross-Attention Fusion** — Multi-head cross-attention lets the semantic
   representation attend to the projected stylometric features, then both are
   concatenated and passed through a fusion MLP.
4. **UACC** — A single linear classifier with sigmoid activation producing a
   calibrated confidence score in [0, 1].
