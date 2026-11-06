# RH binary routing: review bundle (2026-09-10)

Status: **NON-CANONICAL NOTE**. No registry row, no probe, no status motion,
no Canon change. RH remains an open obligation of the program.

This directory reviews the owner's working note of 2026-09-10, *RH: binární
skládání, ortogonální vrstvy a přesná racionální norma* (a Nyman–Beurling /
Báez-Duarte / Bagchi sequence-space route), re-verifies every identity in it
with exact arithmetic, records what is new relative to the note, places the
route against the existing RH lanes of the repository, and plans the Lean
follow-up.

```text
NOTE-SOURCE-CZ.md                 the reviewed note, verbatim (Czech)
REVIEW-CZ.md                      the review: verdict, corrections, new
                                  lemmas with proofs, the proof gap, links to
                                  existing lanes (Czech)
LEAN-PLAN-CZ.md                   Lean 4 / Mathlib formalization plan (Czech,
                                  identifiers in English)
verify_rh_binary_review.py        independent exact re-verification, Python
                                  standard library only (int, Fraction)
verify_rh_binary_review.stdout.txt  its stdout on the reviewing machine
verification_review.json          its machine-readable output
```

Run from this directory:

```sh
python3 verify_rh_binary_review.py verification_review.json
```

The run is deterministic (seeded `random`), takes about one minute of CPU,
and writes nothing else. One printed block is labelled as a floating-point
diagnostic; every assertion is exact.

Boundaries. The reviewing session had no access to arxiv.org or to a Lean
toolchain, so the four references of the note are cited as the note cites
them and no Lean file here was compiled. The elementary direction of the
sequence criterion (membership of the constant sequence implies RH) is
re-derived in the review; the hard direction is imported from Bagchi (2006)
exactly as the note imports it.
