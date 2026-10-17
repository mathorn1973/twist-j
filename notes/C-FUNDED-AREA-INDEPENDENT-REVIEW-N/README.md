# Independent Review R2: Funded Integer Contact and Action-Area Record (`C-FUNDED-AREA-INDEPENDENT-REVIEW-N`)

**Status:** PUBLIC / NON-CANONICAL / L1
**Issue:** [#1588](https://github.com/mathorn1973/twist-j/issues/1588) (parent [#1586](https://github.com/mathorn1973/twist-j/issues/1586))
**Target:** [PR #1585](https://github.com/mathorn1973/twist-j/pull/1585) (`probe/P-FUNDED-AREA-PHASE-RECORD-1`, head `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`, formal source pin `a4ec92176c9f8ace9f884254e05d57a5466b84e0`), reservation [#1584](https://github.com/mathorn1973/twist-j/issues/1584).
**Reviewer session:** `Antigravity-R2-20261017-8f0b47e9`
**Author:** A. M. Thorn `<thorn@twistj.com>`
**SPDX-License-Identifier:** Apache-2.0

## Purpose

This directory contains the method-blind independent mathematical proof, adversarial breaker (`break.py`), run record, and post-break comparison review for R2 (#1588) auditing `probes/P-FUNDED-AREA-PHASE-RECORD-1/` (PR #1585).

## Pre-execution frozen files

- `PREREG.md` — Six-field preregistration of the independent review and breaker protocol, frozen before the first execution of `break.py`.
- `PROOF.md` — Self-contained independent mathematical proofs and adversarial scope classifications for all six mandatory attacks of #1588.
- `break.py` — Dependency-free Python 3 standard-library exact-integer breaker and exhaustive finite-inventory audit script, written from the frozen specification before inspecting the target `verify.py` or `PROOF.md`.
- `EXPOSURE.md` — Exact pre-break and post-break exposure disclosure and method-blind classification.
- `SOURCES.tsv` — Exact commit, blob, byte-count, and SHA-256 manifest of normative Public Canon v103 and target inputs.
- `README.md` — Directory overview and scope guard.

## Post-execution files (added after `PINNED_R2` and first run)

- `EXPECTED.txt` — Exact stdout captured from the first frozen execution of `break.py`.
- `RUN.md` — Execution metadata, environment, hashes, and pin verification for the first run of `break.py`.
- `REVIEW.md` — Post-run audit comparing our independent proof and breaker results against the author's `PROOF.md`, `verify.py`, `EXPECTED.txt`, `RUN.md`, and `RESULT.md` at `a4ec92176c9f8ace9f884254e05d57a5466b84e0` and `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`.
- `RESULT.md` — Final scoped review disposition (`CONFIRMED_IN_SCOPE` / `STOP_INCOMPLETE` / `COUNTEREXAMPLE`) and boundary ledger.

## Explicit physical and canonical guards

All results in this directory are strictly conditional L1 statements about a selected integer automaton on $\mathbb{Z}^4 \times \mathbb{N}_0 \times \{+1,-1\}^2 \times C_4$ and a chosen five-state monomial Weyl representation. They establish no physical action scale, no $\hbar$, no SI bridge, no native $U$ or $J$ compilation, no physical phase measurement, and no closure of `METRO-EDGE-SCALE` or `QDD-INSTRUMENT-APPARATUS`.
