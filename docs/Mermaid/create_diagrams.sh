#!/usr/bin/env bash
# ============================================================
# Mermaid diagram scripts for the RADAR paper
# These define the diagrams in Mermaid syntax.
# Rendering is done via Python/matplotlib (see generate_figures.py)
# because a headless browser may not be available in the CI
# environment.
# ============================================================

# ── Diagram 1: RADAR Model Architecture ─────────────────────
cat > radar_architecture.mmd << 'EOF'
flowchart TB
    A[Input Text] --> B[Preprocessing]
    B --> C[Tokenizer]
    B --> D[Stylometric Extractor\n38 features]

    C --> E[ARSE\nModernBERT-large Encoder]
    D --> F[SLPE\nStylometric Projection Layer]

    E -->|CLS Token h_semantic| G[Cross-Attention Fusion]
    F -->|h_style_proj| G

    G --> H[UACC Classification Head]
    H --> I[AI Detection Score 0–1]
EOF

# ── Diagram 2: Training Pipeline ────────────────────────────
cat > training_pipeline.mmd << 'EOF'
flowchart LR
    A[PAN-2026\nTrain 23,682] --> C[Combined\nTraining Set\n38,503]
    B[RAID External\nDev Sample 30,000] --> C

    C --> D[Stage 1\nEncoder Frozen\n1.2% params trained]
    D --> E[Stage 2\nFull Fine-tuning\n100% params trained]

    E --> F[RADAR\nFinal Model]

    G[PAN-2026\nValidation 3,589] --> H[Evaluation\nROC-AUC · F1 · C@1]
    I[RAID Test\n10,000] --> H
    F --> H
EOF

echo "Mermaid scripts written. Run generate_figures.py to produce PNG images."
