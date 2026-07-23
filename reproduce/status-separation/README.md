# Theorem and dictionary separation audit

This release audit checks a structural boundary in the current Public Canon.
It establishes no new mathematical or physical claim. It verifies that the
named algebraic, finite-group, chain, and recurrence rows remain at `T`, while
their physical projection, place/CPT, force-curvature, color, Maxwell, Born,
and cosmology readings are carried by explicit `D` rows and unresolved
computation or obligation boundaries remain explicit `C` or `O` rows. Its count check is
updated by each completed Canon fold; the theorem/dictionary boundary checks stay
structural.

The audit reads `canon/REGISTRY.tsv`, `canon/NORMATIVE.tsv`,
`canon/DEPENDENCIES.tsv`, and `canon/EVIDENCE.tsv`, uses the Python standard
library, and emits deterministic text. Its eleven checks cover the current
registry partition, the axiom and plenum, the two arithmetic places, the carry
lifts and checkpoint no-go, the finite Weyl commutator, the Maxwell chain, the
Born finite algebra, the color ladder, the cosmology identities, the Schwinger
target arithmetic/physical firewall, and the C20 theorem's separation from
the finite-depth time tower and decoder readings. Selected theorem scopes are
also checked for the interpretive phrases moved to dictionary rows.

Run from the repository root:

```text
python3 reproduce/status-separation/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 11/11 ALL PASS`,
exit 0, and empty stderr.
