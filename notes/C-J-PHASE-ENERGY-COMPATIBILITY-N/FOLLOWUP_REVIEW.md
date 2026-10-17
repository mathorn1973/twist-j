# Review and custody of the analytical continuation

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.
Date: 2026-10-18 Europe/Prague.

## Scope and exposure

This record covers only the four new files listed below. It does not
rewrite REVIEW.md or extend the original independent audit to new claims.
The owner supplied all three evolving proposals before these analyses.
Five separate assistant contexts supplied mathematical or consistency
reviews. They saw the exposed questions and, where stated, the author's
draft. This is neither a blind study nor external peer review.

The existing notes owner declared this continuation before any new commit
in [#1603 comment6242247371](https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6242247371).
Further owner steering supplied the Lucas/transcendence proposal and the
finite-mismatch interpretation while this work was in progress. They are
included as exposed hypotheses, not retrospectively preregistered tests.

## Exact reviewed content

| File | SHA-256 |
|---|---|
| README.md | a83f2b036c2c17d58bf35817e63e71ea53385f693a68cea46ac1b72a8551ccab |
| PROPOSALS.md | e59215ed0e7882ac7bddbe4948ca627a2924b6c3cb5f5dc3236f1fa412ea7bc0 |
| CLOCKS.md | bc09e0ccff204a5da0692d34a677a256687e06918a4d302143c171eeba7c3f1a |
| ENERGY.md | b45274080765f6dbbf1ea1ff9255bc5113ee6ef4b561afc0d0b0efe9e586f245 |

The root author checked each review against the actual files and source
statements. The dispositions are scoped as follows:

- Galois/clock review: accepted all of PROPOSALS.md, CLOCKS.md sections1–2
  and ENERGY.md section7, with the exact final hashes. It located the
  already canonical Fourier obstruction and strip clock; no novelty is
  claimed for those theorems.
- Rapidity/blocking review: accepted the corrected proposal identities and
  CLOCKS.md section3, including the two nonzero Chebyshev harmonics, the
  explicit spatial discrepancy and the half-angle/dyadic distinction.
- Operator/phase-space review: accepted CLOCKS.md section4 and ENERGY.md
  sections1–3 on the exact final hashes, including the time-sign correction,
  symplectic endpoint term, signed Cayley formula and conserved alternatives.
- Transcendence/compatibility review: accepted all of ENERGY.md at its
  exact final hash. It independently checked the local derivative theorem,
  counterexample to rest-matrix-only algebraicity, the operator identities
  and the finite-mismatch/entropy boundary. It used an additional assistant
  for the transcendence argument and counterexample, not an independent run.
- Publication-consistency review: checked all four texts against the live
  Canon pins, scopes, custody and safety. It accepted after the two final
  z-versus-k notation replacements in PROPOSALS.md, which were also checked
  by the mathematical reviewers. No private-data or status leak was found.

## Corrections made before this final content

Review fixed the Laurent/wavenumber notation and coin-name collision,
restored the n>=3 and known normalized G premises of native readback,
restricted the transcendence application to algebraic derivative data,
and specified the one-sided massless slope. Crucially, the energy candidate
now uses H=-K on the exp(-i omega) band under psi_t=U^t psi_0, so energy,
the centered time difference and group drift share one phase convention.

The owner's finite mismatch is explicitly preserved as a physical
hypothesis. A continuum limit is optional, not an imposed correction.
The proof does not turn that hypothesis into per-tick dissipation or infer
thermodynamic entropy from the distinct toral expansion entropy.

## Integrity and execution record

All eleven original files are unchanged relative to
14ce73995f376b295be6c18f296ac7d8ed2c2441. In particular the old PREREG,
PROOF, audit source, historical reviewer text and first-run evidence retain
their exact bytes. Only the four listed analytical files and this review
record are added. No formal scientific program was executed or repeated.

On the staged four-file content, local repository-integrity checks passed:

    POLICY PASS
    CANON PASS v103 claims=530
    LEDGER PASS claims=530 items=594 dependencies=1105 evidence=530 history=1077 gates=26 programs=7
    GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2

These are infrastructure checks, not scientific reproduction. The public
commit/tree readback and final PR Actions outcome are recorded in the issue
and PR after publication so that this record does not claim a future run.
The original author-address approval applies to this continuation; no policy
file is changed. All new contents are authored mathematical prose and public
references, with no copied external code, private material or raw log dump.

Disposition: no blocking mathematical defect found at the stated scope.
Analytical candidate-T ceiling only; the physical mismatch, energy reading,
contact admission and entropy-cost interpretations are not promoted.
