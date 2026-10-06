# Supplemental scalar Hermitian norm audit

This exact L1 reproduction supports the inline proofs of
SCALAR-HERMITIAN-NORM-IMAGE, RAMIFIED-HERMITIAN-NORM-OBSTRUCTION, and
J-TWO-TRACE-SCALAR-NORM-IMAGE. The carrier is O_K=Z[zeta_5], with real
subfield O_F=Z[phi], relative norm H(alpha)=alpha*bar(alpha), and the
stipulated pure-J reading J=1+zeta_5^2. It does not assert a physical
metric, dimension, time, measurement, Hodge-memory identification, native
contact, occurrence law, or perfect-cuboid result.

Run from the repository root:

```sh
python reproduce/scalar-hermitian-norm/verify.py
```

Successful stdout must equal EXPECTED.txt and the exit code must be zero.
The verifier uses only the Python standard library, integer arithmetic,
and coefficient multiplication in Z[X]/Phi_5(X). It performs no writes
and has no network or optional-package dependency.

It checks the displayed scalar witnesses, the mod19 factorization and
quadratic nonsquares, primality of 5779, the two-trace and Gram identities,
the exact residue patterns, and all 14641 points of the proved norm-19
coefficient box. It also compares the analytical norm-image criterion
against the complete scalar trace<=40 image of 155 pairs; the trace-Gram
inequality places every such scalar in the same box. The sequence check
covers the stated examples and residues for n=0,...,12, not all odd n.

The analytical classification relies on the inline ideal-theoretic proof
and registered class-number/unit premises, not on extrapolating the finite
census. This is a supplemental proof audit consolidated from disclosed
exploratory work, not a retrospectively preregistered experiment or a
standalone formal probe. A local rerun does not by itself constitute an
independent-author or cross-architecture claim. No transient run log is
part of this reproduction.
