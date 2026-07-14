# Theorem and dictionary separation audit

This release audit checks a structural boundary in the current Public Canon.
It establishes no new mathematical or physical claim. It verifies that the
named algebraic, finite-group, chain, and recurrence rows remain at `T`, while
their physical projection, place/CPT, force-curvature, color, Maxwell, Born,
and cosmology readings are carried by explicit `D` rows. Its count check is
updated by each completed Canon fold; the theorem/dictionary boundary checks stay
structural.

The audit reads only `canon/REGISTRY.tsv`, uses the Python standard library,
and emits deterministic text. Its eight checks cover the current registry
partition,
the axiom and plenum, the two arithmetic places, the finite Weyl commutator,
the Maxwell chain, the Born finite algebra, the color ladder, and the
cosmology identities. Selected theorem scopes are also checked for the
interpretive phrases moved to dictionary rows.

Run from the repository root:

```text
python3 reproduce/status-separation/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 8/8 ALL PASS`,
exit 0, and empty stderr.
