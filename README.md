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

### MahmoodAnaam/radar-encoder-freeze

<img width="1600" height="386" alt="image" src="https://github.com/user-attachments/assets/f32a7c4a-fd9d-444f-8df2-230e9661b230" />


### MahmoodAnaam/RADAR

<img width="1600" height="445" alt="image" src="https://github.com/user-attachments/assets/32bd8889-a774-4c88-932b-a48d30fa687a" />


### MahmoodAnaam/radar-encoder-freeze-pan26

<img width="1600" height="447" alt="image" src="https://github.com/user-attachments/assets/8336836f-c079-4d57-a200-8179afb6cd07" />


### MahmoodAnaam/radar-encoder-freeze-raid

<img width="1600" height="390" alt="image" src="https://github.com/user-attachments/assets/af357deb-d6ce-4d21-88e2-0762abfc6c0c" />






