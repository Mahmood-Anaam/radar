---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: radar-encoder-freeze-pan26
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# radar-encoder-freeze-pan26

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7864
- Roc-auc: 0.716
- Brier: 0.731
- C@1: 0.65
- F1: 0.659
- F05u: 0.649
- Mean: 0.681

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.03
- num_epochs: 10

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Roc-auc | Brier | C@1   | F1    | F05u  | Mean  |
|:-------------:|:------:|:----:|:---------------:|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0.1171        | 0.6748 | 500  | 0.1264          | 0.984   | 0.956 | 0.942 | 0.955 | 0.955 | 0.958 |
| 0.0899        | 1.3495 | 1000 | 0.0864          | 0.992   | 0.97  | 0.963 | 0.971 | 0.971 | 0.973 |
| 0.0498        | 2.0243 | 1500 | 0.0732          | 0.994   | 0.976 | 0.968 | 0.975 | 0.971 | 0.977 |
| 0.0716        | 2.6991 | 2000 | 0.0638          | 0.995   | 0.979 | 0.972 | 0.979 | 0.977 | 0.98  |
| 0.0672        | 3.3738 | 2500 | 0.0583          | 0.996   | 0.98  | 0.972 | 0.979 | 0.98  | 0.981 |
| 0.0453        | 4.0486 | 3000 | 0.0618          | 0.996   | 0.98  | 0.974 | 0.98  | 0.977 | 0.981 |
| 0.0785        | 4.7233 | 3500 | 0.0555          | 0.997   | 0.979 | 0.97  | 0.977 | 0.983 | 0.981 |
| 0.0467        | 5.3981 | 4000 | 0.0522          | 0.997   | 0.982 | 0.977 | 0.982 | 0.981 | 0.984 |
| 0.0672        | 6.0729 | 4500 | 0.0534          | 0.997   | 0.983 | 0.978 | 0.983 | 0.981 | 0.984 |
| 0.0249        | 6.7476 | 5000 | 0.0694          | 0.997   | 0.979 | 0.973 | 0.98  | 0.972 | 0.98  |
| 0.0227        | 7.4224 | 5500 | 0.0488          | 0.997   | 0.983 | 0.977 | 0.982 | 0.983 | 0.984 |
| 0.0261        | 8.0972 | 6000 | 0.0507          | 0.997   | 0.983 | 0.979 | 0.984 | 0.982 | 0.985 |
| 0.0654        | 8.7719 | 6500 | 0.0478          | 0.997   | 0.983 | 0.978 | 0.983 | 0.984 | 0.985 |
| 0.0291        | 9.4467 | 7000 | 0.0494          | 0.997   | 0.984 | 0.978 | 0.983 | 0.982 | 0.985 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
