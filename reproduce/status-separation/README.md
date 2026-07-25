# Theorem and dictionary separation audit

This release audit checks a structural boundary in the current Public Canon.
It establishes no new mathematical or physical claim. It verifies that named
exact rows remain at `T`, while physical readings are carried by explicit
`D`, `C`, `H`, `O`, or `F` rows. Its count check is updated by each completed
Canon fold; the theorem/dictionary boundary checks stay structural.

The audit reads `canon/REGISTRY.tsv`, `canon/NORMATIVE.tsv`,
`canon/DEPENDENCIES.tsv`, `canon/EVIDENCE.tsv`, `canon/GATES.tsv`, and
`canon/FRONTIER_PROGRAMS.tsv`, uses the Python standard library, and emits
deterministic text. Its fifteen checks cover the current registry partition,
the axiom and plenum, the two arithmetic places, the carry lifts and
checkpoint no-go, the finite Weyl commutator, the Maxwell chain, the Born
finite algebra, the color ladder, the cosmology identities, the Schwinger
target firewall, the C20 arithmetic/time firewall, the TM-SYM2 split
between three closed action classifications, the fired frozen selector, and
the distinct open physical-measure successor, plus the separation of the
exact WALL-LI2-RUNG theorem from the still-open QUANT-SUBSTRATE coupling.
The final two checks pin the corrected midpoint and branch scope of
WALL-CIRCLE-LEMMA and keep the L5 finite-state rationality theorem separate
from the still-open METRO-ADMISSIBILITY lift.

Run from the repository root:

```text
python3 reproduce/status-separation/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 15/15 ALL PASS`,
exit 0, and empty stderr.
