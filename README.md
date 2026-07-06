# radar
RADAR (Robust Adversarial-Resistant Detection with Adaptive Reasoning) is a hybrid architecture for detecting AI-generated text.

## Variants Submitted to TIRA

First ensure that the models are in the HF_HOME:

```
python3 -c 'from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained("MahmoodAnaam/radar-encoder-freeze", trust_remote_code=True); AutoModel.from_pretrained("MahmoodAnaam/radar-encoder-freeze", trust_remote_code=True);'
python3 -c 'from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained("MahmoodAnaam/RADAR", trust_remote_code=True); AutoModel.from_pretrained("MahmoodAnaam/RADAR", trust_remote_code=True);'
python3 -c 'from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained("MahmoodAnaam/radar-encoder-freeze-pan26", trust_remote_code=True); AutoModel.from_pretrained("MahmoodAnaam/radar-encoder-freeze-pan26", trust_remote_code=True);'
python3 -c 'from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained("MahmoodAnaam/radar-encoder-freeze-raid", trust_remote_code=True); AutoModel.from_pretrained("MahmoodAnaam/radar-encoder-freeze-raid", trust_remote_code=True);'
```

```
tira-cli code-submission \
    --dry-run \
    --path . \
    --task generative-ai-authorship-verification-panclef-2026 \
    --dataset pan26-generative-ai-detection-smoke-test-20260330-training \
    --mount-hf-model MahmoodAnaam/radar-encoder-freeze answerdotai/ModernBERT-large \
    --command '/usr/local/bin/radar --model MahmoodAnaam/radar-encoder-freeze'


tira-cli code-submission \
    --dry-run \
    --path . \
    --task generative-ai-authorship-verification-panclef-2026 \
    --dataset pan26-generative-ai-detection-smoke-test-20260330-training \
    --mount-hf-model MahmoodAnaam/radar-encoder-freeze-pan26 answerdotai/ModernBERT-large \
    --command '/usr/local/bin/radar --model MahmoodAnaam/radar-encoder-freeze-pan26'

tira-cli code-submission \
    --dry-run \
    --path . \
    --task generative-ai-authorship-verification-panclef-2026 \
    --dataset pan26-generative-ai-detection-smoke-test-20260330-training \
    --mount-hf-model MahmoodAnaam/radar-encoder-freeze-raid answerdotai/ModernBERT-large \
    --command '/usr/local/bin/radar --model MahmoodAnaam/radar-encoder-freeze-raid'


```

## Evaluation


### radar-encoder-freeze

| Dataset                                                    | Run                 | Roc-Auc | Brier |   C@1 |    F1 |  F05U |  Mean |
| ---------------------------------------------------------- | ------------------- | ------: | ----: | ----: | ----: | ----: | ----: |
| eloquent-20260601-test                                     | 2026-06-07-07-24-03 |   0.868 | 0.756 | 0.622 | 0.749 | 0.882 | 0.775 |
| eloquent-20260523-test                                     | 2026-06-07-07-22-56 |   0.865 | 0.758 | 0.637 | 0.760 | 0.888 | 0.782 |
| pan25-generative-ai-detection-20260508-test                | 2026-06-07-07-19-43 |   0.925 | 0.889 | 0.845 | 0.882 | 0.916 | 0.891 |
| pan26-generative-ai-detection-20260507-test                | 2026-06-07-07-16-27 |   0.772 | 0.805 | 0.722 | 0.800 | 0.839 | 0.788 |
| pan26-generative-ai-detection-smoke-test-20260330-training | 2026-06-07-07-14-16 |   1.000 | 0.963 | 0.971 | 0.968 | 0.987 | 0.978 |



### RADAR

| Dataset                                                    | Run                 | Roc-Auc | Brier |   C@1 |    F1 |  F05U |  Mean |
| ---------------------------------------------------------- | ------------------- | ------: | ----: | ----: | ----: | ----: | ----: |
| eloquent-20260523-test                                     | 2026-06-06-13-17-57 |   0.760 | 0.556 | 0.539 | 0.677 | 0.834 | 0.673 |
| eloquent-20260601-test                                     | 2026-06-05-06-39-29 |   0.774 | 0.573 | 0.554 | 0.692 | 0.844 | 0.687 |
| pan25-generative-ai-detection-20260508-test                | 2026-06-05-06-32-38 |   0.984 | 0.917 | 0.914 | 0.935 | 0.971 | 0.944 |
| eloquent-20260601-test                                     | 2026-06-05-06-30-25 |   0.774 | 0.573 | 0.554 | 0.692 | 0.844 | 0.687 |
| pan26-generative-ai-detection-20260507-test                | 2026-06-05-06-29-21 |   0.790 | 0.541 | 0.530 | 0.555 | 0.741 | 0.632 |
| pan26-generative-ai-detection-smoke-test-20260330-training | 2026-06-05-06-28-25 |   1.000 | 0.971 | 0.971 | 0.968 | 0.987 | 0.979 |



### radar-encoder-freeze-pan26

| Dataset                                                    | Run                 | Roc-Auc | Brier |   C@1 |    F1 |  F05U |  Mean |
| ---------------------------------------------------------- | ------------------- | ------: | ----: | ----: | ----: | ----: | ----: |
| eloquent-20260601-test                                     | 2026-06-07-07-09-48 |   0.814 | 0.716 | 0.601 | 0.733 | 0.868 | 0.747 |
| eloquent-20260601-test                                     | 2026-06-07-07-09-42 |   0.814 | 0.716 | 0.601 | 0.733 | 0.868 | 0.747 |
| eloquent-20260523-test                                     | 2026-06-07-07-04-45 |   0.815 | 0.722 | 0.615 | 0.744 | 0.874 | 0.754 |
| pan25-generative-ai-detection-20260508-test                | 2026-06-06-07-18-48 |   0.897 | 0.858 | 0.817 | 0.856 | 0.908 | 0.867 |
| pan26-generative-ai-detection-20260507-test                | 2026-06-06-07-15-57 |   0.673 | 0.658 | 0.545 | 0.608 | 0.736 | 0.644 |
| pan26-generative-ai-detection-smoke-test-20260330-training | 2026-06-06-07-14-34 |   0.997 | 0.960 | 0.941 | 0.933 | 0.972 | 0.961 |



### radar-encoder-freeze-raid

| Dataset                                                    | Run                 | Roc-Auc | Brier |   C@1 |    F1 |  F05U |  Mean |
| ---------------------------------------------------------- | ------------------- | ------: | ----: | ----: | ----: | ----: | ----: |
| eloquent-20260601-test                                     | 2026-06-07-07-08-31 |   0.749 | 0.657 | 0.452 | 0.591 | 0.780 | 0.646 |
| eloquent-20260523-test                                     | 2026-06-07-07-05-59 |   0.749 | 0.662 | 0.470 | 0.607 | 0.792 | 0.656 |
| pan26-generative-ai-detection-smoke-test-20260330-training | 2026-06-06-07-23-27 |   0.392 | 0.692 | 0.500 | 0.000 | 0.000 | 0.317 |
| pan26-generative-ai-detection-20260507-test                | 2026-06-06-07-23-04 |   0.701 | 0.792 | 0.694 | 0.783 | 0.812 | 0.756 |
| pan25-generative-ai-detection-20260508-test                | 2026-06-06-07-21-45 |   0.639 | 0.738 | 0.559 | 0.606 | 0.710 | 0.650 |







