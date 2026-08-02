# PREREG C-CM-2I-QCARRIER-2

NON-CANONICAL. Incubation-lane preregistration, not a public probe.
Recorded before the recorded run leg of this bundle.

```text
CANDIDATE  C-CM-2I-QCARRIER-2
DATE       2026-08-02
OWNER      claude incubation session 2026-08-02
TARGET     the explicit G-equivariant tau-semilinear quarter-turn on
           the branch pair of the registered 2I lift: intertwiner,
           cocycle, order decision, branch swap, Gram transport
BASIS      Public Canon v30, STATE ACTIVE, AUTHORITY mathorn1973/twist-j
           main, TAG canon-v30, CONTENT_COMMIT
           857223fcd5e7bc8c8e68f1df768d6e8222b24ee0, CANON_SHA256
           2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
           CANON_BYTES 157167, SHA256SUMS 5 of 5 OK, verified this session
```

## Code

```text
verify_cm_2i_qcarrier_2.py
  sha256 07bc78c68dbc98662f2bfdd065bddf8b26641028a098b755b88318ee6ab2ab4b
  12814 bytes, 11 gates
```

Python 3 stdlib, exact Z[zeta5] arithmetic, deterministic, no
randomness, no tolerance.

## Systematics

Primitive integral C from the reduced nullspace with fixed free-column
convention; d = smallest solution of N(d) = phi^2 in the frozen box
|c_i| <= 3; the same box gives the exhaustive unsolvability audit for
the plus sign (whose proof is total positivity of CM norms).

## Failure thresholds

Any FAIL line fires F-QC2-1; structural falsifiers F-QC2-2 (an
order-4 equivariant semilinear structure) and F-QC2-3 (an equivariant
semilinear map outside the Schur ansatz) are stated in the claim doc.
Exit 0, empty stderr required.

## Action layer

L4 support-level structure only; no L5/L6 content; no registry row
closed, moved, or re-scoped.
