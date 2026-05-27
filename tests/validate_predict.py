#!/usr/bin/env python3
"""
RADAR Predict Validation Script
================================
Validates the predict pipeline using a small dataset without requiring
full model weights (GPU / HuggingFace download).

Tests covered
-------------
1. Preprocessing — email / user / phone substitution, lowercasing.
2. Stylometric feature extraction — shape, range, no NaN/Inf values.
3. Output format — valid JSONL with required fields, label in [0, 1].
4. End-to-end smoke test — runs the full predict CLI against the sample
   dataset; requires RADAR_MODEL env var pointing to a local/HF model,
   or is skipped automatically when the model is unavailable.

Usage
-----
    python tests/validate_predict.py                   # all tests
    python tests/validate_predict.py --smoke-only      # only full-pipeline test
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Make sure the package is importable from the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from radar.features import StylemetricFeatureExtractor, extract_features_batch
from radar.preprocessing import preprocess

# Path to the small sample dataset shipped alongside this script.
SAMPLE_INPUT = Path(__file__).parent / "data" / "sample_input.jsonl"

# Number of stylometric features the extractor must produce per sample.
EXPECTED_FEATURE_DIM = 38


# ---------------------------------------------------------------------------
# Test cases
# ---------------------------------------------------------------------------


class TestPreprocessing(unittest.TestCase):
    """Unit tests for the text-preprocessing step."""

    def test_email_replacement(self):
        text = "Contact us at support@example.com for help."
        result = preprocess(text)
        self.assertNotIn("support@example.com", result)
        self.assertIn("[email]", result)

    def test_user_mention_replacement(self):
        text = "Thanks @JohnDoe for the update!"
        result = preprocess(text)
        self.assertNotIn("@JohnDoe", result)
        self.assertIn("[user]", result)

    def test_phone_replacement(self):
        text = "Call me at +1 555-867-5309 anytime."
        result = preprocess(text)
        self.assertNotIn("555-867-5309", result)
        self.assertIn("[phone]", result)

    def test_lowercase(self):
        text = "Hello WORLD, This IS a Test."
        result = preprocess(text)
        self.assertEqual(result, result.lower())

    def test_strip_whitespace(self):
        text = "   hello world   "
        result = preprocess(text)
        self.assertEqual(result, result.strip())

    def test_empty_string(self):
        result = preprocess("")
        self.assertEqual(result, "")

    def test_plain_text_unchanged_structure(self):
        text = "A simple sentence with no special tokens."
        result = preprocess(text)
        self.assertEqual(result, text.lower().strip())


class TestStylemetricExtractor(unittest.TestCase):
    """Unit tests for the stylometric feature extractor."""

    @classmethod
    def setUpClass(cls):
        cls.extractor = StylemetricFeatureExtractor()

    def _sample_texts(self):
        texts = []
        with open(SAMPLE_INPUT, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    record = json.loads(line)
                    texts.append(preprocess(record["text"]))
        return texts

    def test_feature_shape(self):
        texts = self._sample_texts()
        features = extract_features_batch(texts, self.extractor)
        self.assertEqual(
            features.shape,
            (len(texts), EXPECTED_FEATURE_DIM),
            f"Expected shape ({len(texts)}, {EXPECTED_FEATURE_DIM}), got {features.shape}",
        )

    def test_no_nan_or_inf(self):
        import numpy as np

        texts = self._sample_texts()
        features = extract_features_batch(texts, self.extractor)
        self.assertFalse(
            np.any(np.isnan(features)),
            "Feature matrix contains NaN values.",
        )
        self.assertFalse(
            np.any(np.isinf(features)),
            "Feature matrix contains Inf values.",
        )

    def test_feature_range(self):
        """Most stylometric features should be bounded to a reasonable range."""
        import numpy as np

        texts = self._sample_texts()
        features = extract_features_batch(texts, self.extractor)
        # Values should not exceed a very large threshold (sanity check).
        self.assertTrue(
            np.all(np.abs(features) < 1e6),
            "Some features have unexpectedly large magnitudes.",
        )

    def test_single_text(self):
        """Extractor should handle a single-element batch without errors."""
        import numpy as np

        features = extract_features_batch(
            ["This is a single sentence."], self.extractor
        )
        self.assertEqual(features.shape, (1, EXPECTED_FEATURE_DIM))
        self.assertFalse(np.any(np.isnan(features)))

    def test_short_text(self):
        """Very short texts should produce valid (possibly zero) features."""
        import numpy as np

        features = extract_features_batch(["ok"], self.extractor)
        self.assertEqual(features.shape, (1, EXPECTED_FEATURE_DIM))
        self.assertFalse(np.any(np.isnan(features)))


class TestOutputFormat(unittest.TestCase):
    """Tests that validate the output JSONL format produced by predict."""

    def _run_predict(self, input_path: Path, output_dir: Path) -> Path:
        """Invoke radar-predict CLI and return the predictions file path."""
        import subprocess

        env = os.environ.copy()
        result = subprocess.run(
            [sys.executable, "-m", "radar.predict", str(input_path), str(output_dir)],
            capture_output=True,
            text=True,
            env=env,
            timeout=300,
        )
        return result, output_dir / "predictions.jsonl"

    def _load_input_ids(self, input_path: Path):
        ids = []
        with open(input_path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    ids.append(json.loads(line)["id"])
        return ids

    def test_predictions_file_exists(self):
        """predictions.jsonl must be created in the output directory."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            self.assertTrue(pred_path.exists(), "predictions.jsonl was not created.")

    def test_predictions_valid_jsonl(self):
        """Every line in predictions.jsonl must be valid JSON."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            with open(pred_path, encoding="utf-8") as fh:
                for i, line in enumerate(fh):
                    line = line.strip()
                    if line:
                        try:
                            json.loads(line)
                        except json.JSONDecodeError as exc:
                            self.fail(f"Line {i} is not valid JSON: {exc}")

    def test_predictions_required_fields(self):
        """Each prediction must contain 'id' and 'label'."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            with open(pred_path, encoding="utf-8") as fh:
                for i, line in enumerate(fh):
                    line = line.strip()
                    if line:
                        record = json.loads(line)
                        self.assertIn("id", record, f"Line {i} missing 'id'.")
                        self.assertIn("label", record, f"Line {i} missing 'label'.")

    def test_predictions_label_range(self):
        """Labels must be floats in [0, 1]."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            with open(pred_path, encoding="utf-8") as fh:
                for i, line in enumerate(fh):
                    line = line.strip()
                    if line:
                        record = json.loads(line)
                        label = record["label"]
                        self.assertIsInstance(label, float, f"Line {i}: label is not float.")
                        self.assertGreaterEqual(label, 0.0, f"Line {i}: label < 0.")
                        self.assertLessEqual(label, 1.0, f"Line {i}: label > 1.")

    def test_predictions_count_matches_input(self):
        """Number of predictions must equal number of input samples."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            input_ids = self._load_input_ids(SAMPLE_INPUT)
            predictions = []
            with open(pred_path, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        predictions.append(json.loads(line))
            self.assertEqual(
                len(predictions),
                len(input_ids),
                f"Expected {len(input_ids)} predictions, got {len(predictions)}.",
            )

    def test_predictions_ids_match_input(self):
        """Prediction IDs must match input IDs."""
        model = os.environ.get("RADAR_MODEL", "")
        if not model:
            self.skipTest("RADAR_MODEL not set; skipping end-to-end output format test.")
        with tempfile.TemporaryDirectory() as tmpdir:
            _, pred_path = self._run_predict(SAMPLE_INPUT, Path(tmpdir))
            input_ids = set(self._load_input_ids(SAMPLE_INPUT))
            pred_ids = set()
            with open(pred_path, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        pred_ids.add(json.loads(line)["id"])
            self.assertEqual(input_ids, pred_ids, "Prediction IDs do not match input IDs.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="RADAR predict validation")
    parser.add_argument(
        "--smoke-only",
        action="store_true",
        help="Run only the end-to-end smoke test (requires RADAR_MODEL to be set).",
    )
    args, remaining = parser.parse_known_args()

    if args.smoke_only:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestOutputFormat)
    else:
        suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
