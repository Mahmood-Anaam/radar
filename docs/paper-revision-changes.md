# Paper Revision Documentation

**Paper:** Team RADAR at PAN 2026: Robust Adversarial-Resistant AI Text Detection  
**Submission:** EasyChair \#480  
**Revision date:** 6 July 2026  
**Reviewer role note:** Changes were made first to satisfy the mandatory editorial
requirements and reviewer recommendations, then extended through a full academic
review of the paper's content. All modifications are documented below with their
justifications.

---

## Summary of Changes

| # | Location | Type | Description |
|---|----------|------|-------------|
| 1 | `\conference` command | **Mandatory** | Updated conference footnote with full CLEF 2026 details |
| 2 | `pan25-lit.bib` | **Mandatory** | Added `bevendorff:2026b` BibTeX entry |
| 3 | `pan25-lit.bib` | **Mandatory** | Added `bevendorff:2026c` BibTeX entry |
| 4 | `pan25-lit.bib` | Bug fix | Removed broken `rangel2026pan` placeholder entry |
| 5 | Abstract | Content | Updated to reflect official challenge test results |
| 6 | Introduction (§1) | Citation fix | Replaced `\cite{rangel2026pan}` with proper citations |
| 7 | Training Protocol §4.2 | Reviewer req. | Clarified "frozen" variant terminology |
| 8 | Results §5 | Reviewer req. | Added official platform evaluation subsection |
| 9 | Conclusion §6 | Content | Updated to reflect official evaluation findings |
| 10 | Conclusion §6 | Content | Expanded future-work paragraph |
| 11 | Acknowledgments | Citation | Added new citations |

---

## Detailed Change Log

### Change 1 — Conference footnote (Mandatory)

**File:** `pan-notebook-template.tex`  
**Before:**
```latex
\conference{CLEF 2026 Working Notes, PAN Lab}
```
**After:**
```latex
\conference{CLEF 2026 Working Notes, 21--24 September 2026, Jena, Germany}
```
**Justification:** The reviewer explicitly required the addition of the full conference
venue and dates in the page-1 footnote, following the CEUR-ART template convention
for working-notes papers.

---

### Change 2 & 3 — New BibTeX entries (Mandatory)

**File:** `pan25-lit.bib`  
**Added:**
```bibtex
@InProceedings{bevendorff:2026b, ...}   % PAN 2026 condensed lab overview paper
@InProceedings{bevendorff:2026c, ...}   % Voight-Kampff task overview paper
```
**Justification:** The reviewer mandated the inclusion of both the condensed lab
overview paper (Bevendorff et al. 2026b, Springer LNCS) and the task overview paper
(Bevendorff et al. 2026c, CEUR-WS) as required citations for any PAN 2026 notebook.
The BibTeX entries were copied verbatim from the review decision email.

---

### Change 4 — Removed broken `rangel2026pan` placeholder (Bug fix)

**File:** `pan25-lit.bib`  
**Before:** A placeholder `@InProceedings{rangel2026pan, ...}` entry existed in a
half-commented state (only its first line carried a `%` prefix, which is not a
valid BibTeX comment character). The remaining fields were loose text outside any
`@type{}` block and would either silently fail to parse or produce a bibliography
warning.  
**After:** The entire placeholder block was removed and replaced with the two proper
entries (`bevendorff:2026b`, `bevendorff:2026c`).  
**Justification:** The placeholder was a forward-reference to bibliographic details
that were not yet available at initial submission. Those details are now provided
through the new mandatory entries. Retaining the broken entry would cause compilation
warnings or errors.

---

### Change 5 — Abstract updated to reflect official results

**File:** `pan-notebook-template.tex`  
**Before:** The abstract stated "the final model achieves a mean score of 0.997
across all five evaluation metrics … substantially outperforming the provided
baselines and demonstrating strong generalization."  
**After:** The abstract now states that the encoder-frozen variant (RADAR-EF)
achieves the highest mean score of 0.788 on the official challenge test set,
outperforming the end-to-end fine-tuned model, and attributes this to the
generalization benefit of preserving pre-trained encoder representations.  
**Justification:** The original abstract described internal validation results
obtained on a split drawn from the same distribution as the training data. The
official TIRA platform evaluation on the withheld test set
(`pan26-generative-ai-detection-20260507-test`) produced substantially different
rankings across variants. Publishing the internal figures without disclosing the
official test outcome would misrepresent the system's external validity. The
revised abstract accurately reports the headline finding from the public leaderboard.

---

### Change 6 — Citation fix in Introduction

**File:** `pan-notebook-template.tex`  
**Before:** `~\cite{rangel2026pan}` (using the now-removed placeholder entry)  
**After:** `~\cite{bevendorff:2026b,bevendorff:2026c}`  
**Justification:** The two new mandatory entries are the correct scholarly references
for PAN 2026 as a whole and for the Voight-Kampff task in particular. The same
replacement was also applied at the second occurrence of the PAN-2026 task citation
later in the same paragraph.

---

### Change 7 — Clarification of "frozen" variant terminology (Reviewer request)

**File:** `pan-notebook-template.tex`, §4.2 Controlled variants  
**Before:** The subsection described the PAN-only and RAID-only controlled variants
but did not explain why they are called "frozen" or how they differ from Stage 1 of
the two-stage training.  
**After:** A second paragraph was added explicitly distinguishing:
- **Stage 1 of two-stage training** — a preliminary frozen-encoder pass that
  stabilizes newly initialized layers before Stage 2 unfreezes the full model; it
  is not an independently evaluated configuration.
- **RADAR-EF / RADAR-EF-PAN26 / RADAR-EF-RAID** — models trained to convergence
  with the encoder permanently frozen; these are fully independent, evaluated, and
  submitted configurations.

The paragraph also explains that the "EF" (encoder-frozen) label in the result
tables marks any variant that remained in frozen-encoder mode throughout its entire
training, distinguishing it unambiguously from the end-to-end "RADAR" model.  
**Justification:** Reviewer 1 explicitly flagged this as unclear: "It is not quite
clear why this is called 'frozen' and what the difference is to the 'frozen' first
training pass." The added paragraph removes this ambiguity without restructuring the
section.

---

### Change 8 — Added official platform evaluation subsection (Reviewer request)

**File:** `pan-notebook-template.tex`, new §5.3 "Official Platform Evaluation"  
**Content added:**
- A table (`tab:official`) reporting the TIRA scores for all four submitted variants
  on `pan26-generative-ai-detection-20260507-test` (ROC-AUC, Brier complement, C@1,
  F1, F0.5u, and Mean).
- Three analytical paragraphs explaining why RADAR-EF (mean 0.788) outperformed
  the end-to-end RADAR model (mean 0.632) on the official test set.

The official scores used in the table were taken directly from the evaluation tables
in the repository's `README.md` file.

The three analytical points are:
1. **Generalization versus overfitting** — end-to-end fine-tuning shifts encoder
   representations toward the training distribution, reducing robustness to the
   novel generators and obfuscations present in the official test set. The frozen
   encoder retains broad pre-trained representations that generalise more reliably.
2. **Calibration under distributional shift** — RADAR's Brier complement collapses
   from 0.997 (internal validation) to 0.541 (official test), while RADAR-EF
   retains 0.805, indicating that frozen-encoder training produces better-calibrated
   confidence estimates under distribution shift.
3. **Role of the stylometric branch** — because the frozen-encoder variants train
   only the stylometric projection, fusion module, and classifier, they learn a
   compact task-relevant adapter on top of stable encoder representations, which is
   less prone to catastrophic forgetting of general language knowledge.

**Justification:** Reviewer 1 stated: "Since only the frozen model performed well in
the final leader board, a bit of analysis would be helpful as to what might be the
reasons." This subsection directly addresses that request with a concrete results
table and a multi-factor analysis grounded in the observed metric patterns.

---

### Change 9 — Conclusion updated to reflect official evaluation

**File:** `pan-notebook-template.tex`, §6 Conclusion  
**Before:** "The submitted model, RADAR, reached a mean score of 0.997 on the
official PAN-2026 validation set and 0.972 on the held-out out-of-domain test set,
significantly outperforming the provided baselines."  
**After:** The paragraph now reports the headline finding from the official test:
RADAR-EF achieved mean 0.788 on the official challenge test, outperforming the
end-to-end model (mean 0.632). The text frames encoder freezing as a practical
insight relevant to deployment scenarios where new generators emerge continuously.  
**Justification:** The original conclusion reported internal figures that no longer
represent the most important result of the submission. A conclusion that omits the
official leaderboard outcome would leave readers with an inaccurate picture of the
system's performance under real evaluation conditions.

---

### Change 10 — Expanded future-work paragraph

**File:** `pan-notebook-template.tex`, §6 Conclusion  
**Added:** A sentence proposing parameter-efficient adaptation techniques (e.g.,
LoRA) as a middle ground between fully frozen and fully fine-tuned encoder training.  
**Justification:** The official evaluation finding motivates the question of whether
partial encoder adaptation (rather than full fine-tuning) could recover some of the
in-domain accuracy lost by complete encoder freezing without sacrificing the
generalisation gains. Adding this direction makes the future-work paragraph more
directly motivated by the paper's own empirical findings.

---

### Change 11 — Acknowledgments citations updated

**File:** `pan-notebook-template.tex`, Acknowledgments  
**Before:** "The authors thank the PAN 2026 organizers …"  
**After:** "The authors thank the PAN 2026 organizers~\cite{bevendorff:2026b,bevendorff:2026c} …"  
**Justification:** The acknowledgments section should cite the organizers' overview
papers when referencing the task organizers directly. This also ensures the new
mandatory citations appear at least once in the body of the paper beyond the
abstract and introduction.

---

## Reviewer Self-Assessment

After completing the mandatory and recommended revisions, a full academic review of
the paper was conducted. The following observations were noted and acted upon where
appropriate.

**Strengths of the paper (unchanged):**
- Clear problem framing and well-motivated hybrid architecture.
- Transparent description of data processing steps with exact row counts.
- Honest caveat about the distributional similarity between training and internal
  validation data.
- All experimental configurations are described precisely enough for replication,
  and source code is publicly available.

**Issues addressed in this revision:**
- The abstract no longer overstates performance using internal-only figures.
- The "frozen" terminology is now precisely defined and disambiguated from Stage 1.
- The official evaluation result, which is the most externally valid measure of the
  system, is now reported and analysed.
- The two mandatory citations are properly integrated.

**Remaining limitations (not addressed, noted for transparency):**
- The commented-out analysis section (§5 Analysis) was left as-is in commented form.
  The key analytical points from those comments were incorporated into the new
  §5.3 text to avoid duplication, but the commented blocks were retained to preserve
  the author's original notes.
- The paper does not include an ablation that isolates the contribution of the
  stylometric features versus the encoder alone. This would strengthen the claims
  about stylometric generalisation but would require new experiments beyond the
  scope of this revision.
- The GitHub repository URL in the footnote (`github.com/yusrpro9/radar`) was not
  changed; it reflects the author's public submission repository.
