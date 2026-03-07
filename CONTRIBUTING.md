# Contributing to The Cosmic Pattern

Thank you for your interest. This document explains how to engage with, verify, and extend this work.

---

## First: Run the Code

Before reading any documentation, run the audit script:

```bash
python3 scripts/cosmic_pattern_ground_truth_v41.py
```

Everything printed is derived from `D = 3` alone. The script writes a CSV you can open in any spreadsheet. Verify the numbers independently before forming an opinion.

---

## What Is Sealed vs. Open

The **scaffold** is sealed. The topology `T²(13,3)`, the lens identity `L = 1/cosh`, and the adjacency map from `D=3` to all sealed observables are not subject to revision — they would need to be falsified, not modified.

A result is **falsifiable** if any of these occur:
- A genuine unitarity violation in CKM or PMNS is confirmed (would falsify the topological closure of `T²(13,3)`)
- A physical constant is measured outside the CA = 2.7% resolution window (would falsify the interface-pixel bound)
- A fermion mass is measured that cannot be assigned an optical-depth address in the `{R, r, D, K, A, Φ₂, Φ₆, 2}` semigroup

**Open threads** (CT-3 through CT-5) are derivations *within* the sealed framework. Contributions here are welcome.

---

## How to Contribute

### 1. Verification (most needed)
Run `cosmic_pattern_ground_truth_v41.py` on your own machine, in your own environment, and report your results as a GitHub Issue. Include:
- Python version and OS
- Any discrepancy from the expected CSV output
- SHA-256 of your output CSV

### 2. CT-3: Fermion Mass Grammar
The top quark is sealed at `w = 0`. The 5 remaining quarks need optical-depth addresses in the grammar. Candidate approach: assign `w` values from the `Z₁₃×Z₃` sector walk and verify mass ratios.

**Gate requirement:** Any proposed `w` assignment must reproduce the top at `w = 0` as a fixed point, not as a fit.

### 3. CT-4: Cabibbo Fresnel Precision
The Fresnel series for `sin(θ_C)` is derived but needs the second term evaluated. Current gap: ~0.12°. The series is:
```
sin(θ_C) = (r/R) · (1 − CA/2 + CA²/8 − ...)
```

### 4. CT-5: PMNS Neutrino Mixing
The sign of δ_PMNS is confirmed (outward/neutrino chart gives negative holonomy). The magnitude needs a second-order holonomy correction. Chart direction rule: always declare inward/outward, apply L↔β flip for outward.

### 5. Documentation
Plain-language translations, visual diagrams of the adjacency map, or worked examples of the methodology gates are welcome.

---

## What Not to Propose

- **New scaffold constants** — the grammar is frozen: `{R, r, D, K, A, Φ₂, Φ₆, 2}`. Denominators outside this semigroup require strong justification and pass through the Grammar Freeze gate.
- **Free parameters** — every new quantity must be derived from the scaffold, not fitted to data.
- **Speculation disconnected from the adjacency map** — if a result cannot be traced back to `D=3` through the adjacency map, it is not part of this framework.

---

## Issue / PR Labels

| Label | Meaning |
|-------|---------|
| `verification` | Running the audit and reporting results |
| `CT-3` through `CT-5` | Work on open computation targets |
| `documentation` | Improving explainers, diagrams, translations |
| `falsification` | A result that appears to contradict a sealed prediction |
| `question` | Genuine questions about methodology or derivations |

---

## Code of Conduct

Engage with the mathematics, not with the person. Every claim in this repository is falsifiable. If you believe something is wrong, show the derivation that contradicts it.
