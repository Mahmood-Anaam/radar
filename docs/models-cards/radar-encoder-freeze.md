---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: radar-encoder-freeze
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# radar-encoder-freeze

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1800
- Roc-auc: 0.97
- Brier: 0.934
- C@1: 0.913
- F1: 0.907
- F05u: 0.941
- Mean: 0.933

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
| 0.3978        | 0.4153 | 500   | 0.3255          | 0.9     | 0.873 | 0.816 | 0.806 | 0.875 | 0.854 |
| 0.3261        | 0.8306 | 1000  | 0.2694          | 0.937   | 0.897 | 0.851 | 0.844 | 0.907 | 0.887 |
| 0.1887        | 1.2458 | 1500  | 0.2409          | 0.949   | 0.911 | 0.877 | 0.877 | 0.912 | 0.905 |
| 0.1766        | 1.6611 | 2000  | 0.2422          | 0.957   | 0.904 | 0.867 | 0.862 | 0.926 | 0.903 |
| 0.2418        | 2.0764 | 2500  | 0.2167          | 0.961   | 0.917 | 0.885 | 0.883 | 0.931 | 0.915 |
| 0.2052        | 2.4917 | 3000  | 0.2028          | 0.962   | 0.927 | 0.901 | 0.904 | 0.929 | 0.924 |
| 0.1627        | 2.9070 | 3500  | 0.1999          | 0.965   | 0.929 | 0.903 | 0.906 | 0.927 | 0.926 |
| 0.1645        | 3.3223 | 4000  | 0.1948          | 0.967   | 0.932 | 0.908 | 0.913 | 0.922 | 0.928 |
| 0.1826        | 3.7375 | 4500  | 0.2087          | 0.97    | 0.917 | 0.887 | 0.884 | 0.939 | 0.919 |
| 0.0895        | 4.1528 | 5000  | 0.1864          | 0.971   | 0.929 | 0.903 | 0.902 | 0.943 | 0.93  |
| 0.0716        | 4.5681 | 5500  | 0.1904          | 0.972   | 0.927 | 0.902 | 0.901 | 0.945 | 0.929 |
| 0.0591        | 4.9834 | 6000  | 0.1982          | 0.973   | 0.923 | 0.898 | 0.896 | 0.945 | 0.927 |
| 0.0892        | 5.3987 | 6500  | 0.1719          | 0.974   | 0.936 | 0.913 | 0.914 | 0.946 | 0.936 |
| 0.0671        | 5.8140 | 7000  | 0.1727          | 0.974   | 0.936 | 0.913 | 0.914 | 0.945 | 0.936 |
| 0.0713        | 6.2292 | 7500  | 0.1767          | 0.976   | 0.933 | 0.909 | 0.909 | 0.948 | 0.935 |
| 0.0790        | 6.6445 | 8000  | 0.1641          | 0.976   | 0.94  | 0.919 | 0.922 | 0.944 | 0.94  |
| 0.0431        | 7.0598 | 8500  | 0.1692          | 0.976   | 0.936 | 0.914 | 0.915 | 0.949 | 0.938 |
| 0.0694        | 7.4751 | 9000  | 0.1685          | 0.976   | 0.937 | 0.915 | 0.916 | 0.948 | 0.939 |
| 0.0576        | 7.8904 | 9500  | 0.1633          | 0.976   | 0.94  | 0.919 | 0.921 | 0.946 | 0.941 |
| 0.0742        | 8.3056 | 10000 | 0.1653          | 0.976   | 0.939 | 0.917 | 0.919 | 0.948 | 0.94  |
| 0.0872        | 8.7209 | 10500 | 0.1638          | 0.976   | 0.94  | 0.919 | 0.921 | 0.947 | 0.941 |
| 0.0777        | 9.1362 | 11000 | 0.1636          | 0.976   | 0.94  | 0.918 | 0.92  | 0.946 | 0.94  |
| 0.0511        | 9.5515 | 11500 | 0.1639          | 0.976   | 0.939 | 0.918 | 0.92  | 0.947 | 0.94  |
| 0.0381        | 9.9668 | 12000 | 0.1634          | 0.976   | 0.94  | 0.918 | 0.92  | 0.946 | 0.94  |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
