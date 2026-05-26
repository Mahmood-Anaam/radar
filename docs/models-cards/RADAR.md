---
library_name: transformers
base_model: MahmoodAnaam/radar-encoder-freeze
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: RADAR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# RADAR

This model is a fine-tuned version of [MahmoodAnaam/radar-encoder-freeze](https://huggingface.co/MahmoodAnaam/radar-encoder-freeze) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1610
- Roc-auc: 0.99
- Brier: 0.967
- C@1: 0.964
- F1: 0.964
- F05u: 0.974
- Mean: 0.972

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

| Training Loss | Epoch  | Step  | Validation Loss | Roc-auc | Brier | C@1   | F1    | F05u  | Mean  |
|:-------------:|:------:|:-----:|:---------------:|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0.2103        | 0.4153 | 500   | 0.1814          | 0.982   | 0.928 | 0.904 | 0.902 | 0.952 | 0.934 |
| 0.2102        | 0.8306 | 1000  | 0.1866          | 0.977   | 0.93  | 0.909 | 0.91  | 0.945 | 0.934 |
| 0.0821        | 1.2458 | 1500  | 0.2049          | 0.989   | 0.94  | 0.921 | 0.93  | 0.905 | 0.937 |
| 0.0476        | 1.6611 | 2000  | 0.0868          | 0.993   | 0.969 | 0.961 | 0.962 | 0.979 | 0.973 |
| 0.0551        | 2.0764 | 2500  | 0.0932          | 0.994   | 0.972 | 0.966 | 0.968 | 0.971 | 0.974 |
| 0.0306        | 2.4917 | 3000  | 0.1181          | 0.995   | 0.969 | 0.963 | 0.966 | 0.959 | 0.97  |
| 0.0295        | 2.9070 | 3500  | 0.0943          | 0.994   | 0.973 | 0.969 | 0.971 | 0.975 | 0.976 |
| 0.0345        | 3.3223 | 4000  | 0.1363          | 0.989   | 0.962 | 0.955 | 0.957 | 0.972 | 0.967 |
| 0.0555        | 3.7375 | 4500  | 0.1326          | 0.991   | 0.964 | 0.958 | 0.96  | 0.976 | 0.97  |
| 0.0493        | 4.1528 | 5000  | 0.1600          | 0.991   | 0.96  | 0.954 | 0.957 | 0.963 | 0.965 |
| 0.0113        | 4.5681 | 5500  | 0.1321          | 0.992   | 0.966 | 0.96  | 0.962 | 0.97  | 0.97  |
| 0.0074        | 4.9834 | 6000  | 0.1529          | 0.99    | 0.962 | 0.956 | 0.958 | 0.971 | 0.968 |
| 0.0515        | 5.3987 | 6500  | 0.1594          | 0.99    | 0.963 | 0.958 | 0.96  | 0.973 | 0.969 |
| 0.0059        | 5.8140 | 7000  | 0.1533          | 0.991   | 0.964 | 0.959 | 0.961 | 0.973 | 0.97  |
| 0.0174        | 6.2292 | 7500  | 0.1489          | 0.991   | 0.963 | 0.958 | 0.96  | 0.976 | 0.97  |
| 0.0230        | 6.6445 | 8000  | 0.1465          | 0.991   | 0.966 | 0.961 | 0.963 | 0.973 | 0.971 |
| 0.0128        | 7.0598 | 8500  | 0.1461          | 0.991   | 0.967 | 0.962 | 0.964 | 0.974 | 0.972 |
| 0.0408        | 7.4751 | 9000  | 0.1477          | 0.991   | 0.966 | 0.961 | 0.963 | 0.974 | 0.971 |
| 0.0057        | 7.8904 | 9500  | 0.1483          | 0.991   | 0.967 | 0.962 | 0.964 | 0.974 | 0.972 |
| 0.0262        | 8.3056 | 10000 | 0.1502          | 0.991   | 0.968 | 0.965 | 0.966 | 0.975 | 0.973 |
| 0.0198        | 8.7209 | 10500 | 0.1382          | 0.992   | 0.972 | 0.97  | 0.971 | 0.98  | 0.977 |
| 0.0111        | 9.1362 | 11000 | 0.1351          | 0.992   | 0.973 | 0.971 | 0.973 | 0.981 | 0.978 |
| 0.0016        | 9.5515 | 11500 | 0.1350          | 0.992   | 0.973 | 0.971 | 0.973 | 0.982 | 0.978 |
| 0.0029        | 9.9668 | 12000 | 0.1352          | 0.992   | 0.973 | 0.971 | 0.973 | 0.982 | 0.978 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
