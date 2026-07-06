# Camera-Ready Revision Notes for the RADAR PAN 2026 Paper

## Scope of the revision

This document records the camera-ready revisions made to `docs/pan-paper-template/pan-notebook-template.tex` after acceptance of the PAN 2026 notebook paper. The changes address the mandatory reviewer requests and add a concise interpretation of the official TIRA/leaderboard results now available in the repository README.

## Changes made

### 1. Conference metadata corrected

- Updated the CEURART `\conference{...}` field from the generic PAN Lab wording to the requested venue text: `CLEF 2026 Working Notes, 21--24 September 2026, Jena, Germany`.
- Justification: this directly satisfies the reviewer’s mandatory page-1 footnote/location requirement and aligns the manuscript with the proceedings metadata.

### 2. Required PAN 2026 citations added

- Added the condensed PAN 2026 lab overview citation (`bevendorff:2026b`) to the bibliography.
- Added the PAN/ELOQUENT 2026 Voight-Kampff task overview citation (`bevendorff:2026c`) to the bibliography.
- Cited both entries in the abstract and acknowledgments, and cited them in the introduction where the paper describes the shared task context.
- Justification: the review explicitly requested both citations. The citations are placed where they support claims about PAN 2026 as a lab and about the 2026 Voight-Kampff task specifically.

### 3. Clarified the meaning of the “frozen” variants

- Rewrote the controlled-variants subsection to define `EF` precisely as an encoder-frozen run for the entire training process.
- Distinguished the following checkpoints:
  - `RADAR-EF`: frozen ModernBERT encoder, PAN+RAID training mixture.
  - `RADAR-EF-PAN26`: frozen ModernBERT encoder, official PAN-only training.
  - `RADAR-EF-RAID`: frozen ModernBERT encoder, filtered RAID-only training.
  - `RADAR`: second-stage end-to-end model initialized from `RADAR-EF` with the encoder unfrozen.
- Justification: this addresses the reviewer’s concern that the “frozen” terminology was ambiguous, especially relative to the first pass of the two-stage training protocol.

### 4. Added official platform results and hidden-test analysis

- Added a new “Official platform results” subsection to the Results and Discussion section.
- Added a table with the official TIRA scores on `pan26-generative-ai-detection-20260507-test` for all four packaged checkpoints.
- Identified `radar-encoder-freeze` as the strongest official submission, with mean score 0.788 and 11th place on the leaderboard as reported by the project context.
- Added analysis explaining why the frozen model likely generalized better than the fully unfrozen RADAR checkpoint on the hidden test set:
  - the unfrozen model had the best ROC-AUC but much worse Brier complement and thresholded metrics;
  - full end-to-end fine-tuning likely over-specialized the ModernBERT encoder to the local training/validation distribution;
  - freezing preserved broad pretrained linguistic representations and forced adaptation into the smaller fusion/classification layers;
  - RAID-only training helped some robustness metrics but lacked enough task-specific PAN grounding.
- Justification: this directly addresses the reviewer’s request for analysis of why only the frozen model performed well on the final leaderboard.

### 5. Adjusted conclusion to reflect official-test lessons

- Extended the conclusion to note that the hidden-test evaluation favored the frozen-encoder PAN+RAID checkpoint, despite the stronger local validation scores of the fully unfrozen checkpoint.
- Justification: this prevents the paper from overstating the local validation result and records the main empirical lesson from the platform evaluation.

### 6. Reviewer-style consistency pass

- Checked that the new text distinguishes local validation results from official hidden-test results.
- Preserved the original local evaluation table because it documents the development process described in the submitted notebook.
- Added cautious wording around validation performance and calibration to avoid overclaiming.
- Kept the methodology consistent with the implementation: ModernBERT semantic branch, 38 stylometric features, cross-attention-style fusion, BCE-with-logits training, frozen and unfrozen training variants, and PAN/RAID data-source analysis.

## Publication-readiness assessment

After these revisions, the paper addresses all mandatory review items and adds the requested discussion of the official leaderboard behavior. The manuscript now more clearly separates the development-stage evaluation from the hidden-test platform evaluation, which should make the final camera-ready version more transparent and defensible.
