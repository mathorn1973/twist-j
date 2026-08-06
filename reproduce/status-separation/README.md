# Theorem and dictionary separation audit

This release audit checks a structural boundary in the current Public Canon.
It establishes no new mathematical or physical claim. It verifies that named
exact rows remain at `T`, while physical readings are carried by explicit
`D`, `C`, `H`, `O`, or `F` rows. Its count check is updated by each completed
Canon fold; the theorem/dictionary boundary checks stay structural.

The audit reads `canon/REGISTRY.tsv`, `canon/NORMATIVE.tsv`,
`canon/DEPENDENCIES.tsv`, `canon/EVIDENCE.tsv`, `canon/GATES.tsv`,
`canon/FRONTIER_PROGRAMS.tsv`, and `canon/CORE.md`, uses the Python standard
library, and emits deterministic text. Its twenty-three checks cover the current
registry partition,
the axiom and plenum, the two arithmetic places, the carry lifts, the
checkpoint no-go, the exact KERNEL-Z6-SYNCHRONIZATION all-n theorem, the
branch-invariant C8-BILINEAR-SHADOW theorem, the exact boost drift and
conditional coin-ranking theorems separated from the MINIMAL-READ D/O rows,
the finite Weyl commutator, the Maxwell chain, the Born finite algebra, the
central Herm/Sym phase theorem kept at L4 and separate from the Herm2 cone,
decoder data, and physical readings, the full quartic cyclotomic
total-ramification census kept at L1 and separate from degree selection,
broader CM completeness, TWO-PLACE-PHYSICS, and every physical lift, the
abelian Galois CM unique-even-bit discriminant-minimum theorem kept at L1 and
separate from total ramification, physical class selection,
TWO-PLACE-PHYSICS, and every higher-layer lift, the exact alternating
trace-form pencil theorem kept at L1 with its repaired scalar-similitude
boundary, the
color ladder, the marked CM 2I semilinear-pair theorem kept at L4 and
separate from marked-lift selection, decoder QCarrier and measure obligations,
the exact Gyron discrepancy and forward pair-substitution
theorems, their corrected stationary-density boundary, and the separate
cosmology dictionary, the Schwinger target firewall, the C20 arithmetic/time
firewall, the TM-SYM2 split between four closed exact classifications, the
fired frozen selector, and the distinct open physical-measure successor, plus
the separation of the exact WALL-LI2-RUNG theorem from the still-open
QUANT-SUBSTRATE coupling. The final four checks pin the corrected midpoint
and branch scope of WALL-CIRCLE-LEMMA; keep the L5 finite-state rationality
theorem separate from the computed METRO-REDUCTION-ARROWS obligations A and C,
while the typed reduction-calculus parent remains O and STOP on obligations B,
D, and E and the dimensional child and residual remain O; and fence the
all-cursor finite-cylinder theorem from both the narrow fired cut and the
still-open Route A entropy bridge; and register the failed universal Kappa
proposition and its conjunctive photon-window parent at F while leaving the
independent roughening question unregistered.

Run from the repository root:

```text
python3 reproduce/status-separation/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 23/23 ALL PASS`,
exit 0, and empty stderr.
