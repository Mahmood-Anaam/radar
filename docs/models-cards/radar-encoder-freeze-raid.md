---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: radar-encoder-freeze-raid
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# radar-encoder-freeze-raid

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1972
- Roc-auc: 0.974
- Brier: 0.941
- C@1: 0.92
- F1: 0.918
- F05u: 0.935
- Mean: 0.938

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
| 0.2243        | 1.0776 | 500  | 0.3152          | 0.946   | 0.898 | 0.85  | 0.83  | 0.912 | 0.887 |
| 0.2362        | 2.1552 | 1000 | 0.2601          | 0.958   | 0.919 | 0.887 | 0.881 | 0.923 | 0.914 |
| 0.1790        | 3.2328 | 1500 | 0.2396          | 0.963   | 0.926 | 0.9   | 0.895 | 0.929 | 0.923 |
| 0.2652        | 4.3103 | 2000 | 0.2677          | 0.965   | 0.916 | 0.885 | 0.875 | 0.934 | 0.915 |
| 0.1927        | 5.3879 | 2500 | 0.2230          | 0.968   | 0.932 | 0.906 | 0.908 | 0.908 | 0.925 |
| 0.1476        | 6.4655 | 3000 | 0.2172          | 0.971   | 0.933 | 0.908 | 0.905 | 0.936 | 0.931 |
| 0.2706        | 7.5431 | 3500 | 0.2093          | 0.971   | 0.936 | 0.913 | 0.913 | 0.928 | 0.932 |
| 0.1720        | 8.6207 | 4000 | 0.2072          | 0.972   | 0.937 | 0.914 | 0.913 | 0.929 | 0.933 |
| 0.1574        | 9.6983 | 4500 | 0.2077          | 0.972   | 0.937 | 0.914 | 0.913 | 0.931 | 0.933 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
