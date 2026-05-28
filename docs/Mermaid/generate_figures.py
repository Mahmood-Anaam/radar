"""
generate_figures.py
====================
Generates the two figures used in the RADAR paper as high-resolution
PNG files and saves them to docs/pan-paper-template/images/.

Usage:
    python docs/Mermaid/generate_figures.py

The Mermaid-syntax definitions of the same diagrams can be found in
docs/Mermaid/create_diagrams.sh.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

OUT = Path(__file__).parent.parent / "pan-paper-template" / "images"
OUT.mkdir(parents=True, exist_ok=True)

BORDER = '#555555'

def box(ax, x, y, w, h, label, color, fontsize=9, bold=False):
    rect = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.08",
        linewidth=1.2, edgecolor=BORDER, facecolor=color,
    )
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center',
            fontsize=fontsize,
            fontweight='bold' if bold else 'normal',
            color='#222222')


def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=BORDER, lw=1.4))


# ── Figure 1: RADAR Model Architecture ──────────────────────────────────────

def fig_architecture():
    C_INPUT = '#D6EAF8'
    C_ENC   = '#D5E8D4'
    C_STYLE = '#FFF2CC'
    C_FUSE  = '#E1D5E7'
    C_CLS   = '#F8CECC'
    C_OUT   = '#DAE8FC'

    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9.5)
    ax.axis('off')

    box(ax, 4.5, 9.0, 3.0, 0.65, 'Input Text', C_INPUT, fontsize=10, bold=True)
    box(ax, 4.5, 8.1, 3.6, 0.65,
        'Preprocessing  (tokenize · PII masking)', C_INPUT, fontsize=8.5)
    arrow(ax, 4.5, 8.67, 4.5, 8.43)

    box(ax, 2.2, 6.9, 3.0, 0.75,
        'ARSE\nModernBERT-large Encoder', C_ENC, fontsize=8.5)
    box(ax, 6.8, 6.9, 3.0, 0.75,
        'SLPE\nStylometric Projection', C_STYLE, fontsize=8.5)
    arrow(ax, 3.5, 7.77, 2.5, 7.28)
    arrow(ax, 5.5, 7.77, 6.5, 7.28)

    box(ax, 2.2, 5.8, 2.8, 0.65,
        'CLS token  h_semantic\n(1024-dim)', C_ENC, fontsize=8)
    box(ax, 6.8, 5.8, 2.8, 0.65,
        '38 features → h_style\n(128-dim)', C_STYLE, fontsize=8)
    arrow(ax, 2.2, 6.52, 2.2, 6.13)
    arrow(ax, 6.8, 6.52, 6.8, 6.13)

    box(ax, 4.5, 4.55, 4.4, 0.85,
        'Cross-Attention Fusion\nh_semantic × h_style  →  h_fused (512-dim)',
        C_FUSE, fontsize=8.5)
    arrow(ax, 2.2, 5.47, 3.3, 4.98)
    arrow(ax, 6.8, 5.47, 5.7, 4.98)

    box(ax, 4.5, 3.30, 3.2, 0.75,
        'UACC  ·  Classification Head\nLinear(512→1) + Sigmoid',
        C_CLS, fontsize=8.5)
    arrow(ax, 4.5, 4.12, 4.5, 3.68)

    box(ax, 4.5, 2.2, 3.0, 0.65,
        'AI Detection Score  [0, 1]', C_OUT, fontsize=9, bold=True)
    arrow(ax, 4.5, 2.92, 4.5, 2.53)

    ax.text(4.5, 0.55,
            'Figure 1 — Overview of the RADAR model architecture',
            ha='center', va='center', fontsize=9, color='#444444')

    plt.tight_layout()
    fig.savefig(OUT / 'radar_architecture.png',
                dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved {OUT / 'radar_architecture.png'}")


# ── Figure 2: Training Pipeline ─────────────────────────────────────────────

def fig_pipeline():
    C_DATA  = '#D6EAF8'
    C_TRAIN = '#D5E8D4'
    C_MODEL = '#E1D5E7'
    C_EVAL  = '#FFF2CC'

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6)
    ax.axis('off')

    box(ax, 1.4, 5.0, 2.4, 0.75, 'PAN-2026\n23,682 samples', C_DATA, fontsize=8.5)
    box(ax, 4.2, 5.0, 2.4, 0.75, 'RAID (external)\n30,000 samples', C_DATA, fontsize=8.5)

    box(ax, 2.8, 3.8, 2.8, 0.75,
        'Combined Training Set\n38,503 samples', C_DATA, fontsize=8.5, bold=True)
    arrow(ax, 1.6, 4.62, 2.3, 4.18)
    arrow(ax, 4.0, 4.62, 3.3, 4.18)

    box(ax, 2.8, 2.6, 3.0, 0.80,
        'Stage 1 – Encoder Frozen\n1.2% params trained', C_TRAIN, fontsize=8.5)
    arrow(ax, 2.8, 3.42, 2.8, 3.00)

    box(ax, 2.8, 1.4, 3.0, 0.80,
        'Stage 2 – Full Fine-tuning\n100% params trained', C_TRAIN, fontsize=8.5)
    arrow(ax, 2.8, 2.20, 2.8, 1.80)

    box(ax, 2.8, 0.45, 2.6, 0.65,
        'RADAR  (final model)', C_MODEL, fontsize=9, bold=True)
    arrow(ax, 2.8, 1.00, 2.8, 0.78)

    box(ax, 8.2, 4.2, 2.4, 0.75,
        'PAN-2026 Validation\n3,589 samples', C_EVAL, fontsize=8.5)
    box(ax, 8.2, 2.9, 2.4, 0.75,
        'RAID Test Set\n10,000 samples', C_EVAL, fontsize=8.5)
    box(ax, 8.2, 1.55, 2.6, 0.90,
        'Evaluation\nROC-AUC · F1 · C@1\nBrier · F0.5u · Mean',
        C_EVAL, fontsize=8)

    arrow(ax, 8.2, 3.82, 8.2, 3.28)
    arrow(ax, 8.2, 2.52, 8.2, 2.00)
    arrow(ax, 4.1, 0.45, 7.0, 1.55)

    ax.text(5.5, 0.08,
            'Figure 2 — RADAR training pipeline and evaluation protocol',
            ha='center', va='center', fontsize=9, color='#444444')

    plt.tight_layout()
    fig.savefig(OUT / 'training_pipeline.png',
                dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved {OUT / 'training_pipeline.png'}")


if __name__ == '__main__':
    fig_architecture()
    fig_pipeline()
    print("All figures generated.")
