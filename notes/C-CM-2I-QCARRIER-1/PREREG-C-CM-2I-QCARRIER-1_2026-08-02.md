# PREREG C-CM-2I-QCARRIER-1

NON-CANONICAL. Incubation-lane preregistration, not a public probe.
Recorded before the recorded run leg of this bundle.

```text
CANDIDATE  C-CM-2I-QCARRIER-1
DATE       2026-08-02
OWNER      claude incubation session 2026-08-02
TARGET     descent of the arithmetic Galois C4 to the registered
           integral 2I lift <S, T> over Z[zeta5]; the invariant Gram
           and its uniqueness; frozen equivalence: GL2(K)-conjugacy
BASIS      Public Canon v30, STATE ACTIVE, AUTHORITY mathorn1973/twist-j
           main, TAG canon-v30, CONTENT_COMMIT
           857223fcd5e7bc8c8e68f1df768d6e8222b24ee0, CANON_SHA256
           2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
           CANON_BYTES 157167, SHA256SUMS 5 of 5 OK, verified this session
```

## Code

```text
verify_cm_2i_qcarrier.py
  sha256 ee632df2af7e6e210770af6505b9bdb10991726f59ba13ca88dede8cdcfe53b2
  11693 bytes, 10 gates
```

Python 3 stdlib, exact Z[zeta5] arithmetic, deterministic, no
randomness, no tolerance.

## Systematics

The lift is regenerated from the registered generators S, T by closure;
Galois twists are entrywise gal(., a) for a in {1, 2, 3, 4}; the
invariance system for Hermitian forms is the exact 32 x 8 rational
linear system over the parametrization a + b sqrt5 (diagonals) and
zeta-coefficients (off-diagonal). The frozen equivalence for descent
statements is GL2(K)-conjugacy with markings (trace-preserving on
labeled elements).

## Failure thresholds

Any FAIL line fires F-QC-1; structural falsifiers F-QC-2 and F-QC-3
are stated in the claim doc. Exit 0, empty stderr required.

## Action layer

L4 support-level structure only; no L5/L6 content; no registry row
closed, moved, or re-scoped.
