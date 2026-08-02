# PREREG C-CENTRAL-LIFT-PHASE-1

NON-CANONICAL. Incubation-lane preregistration, not a public probe.
Recorded before the recorded run leg of this bundle.

```text
CANDIDATE  C-CENTRAL-LIFT-PHASE-1
DATE       2026-08-02
OWNER      claude incubation session 2026-08-02
TARGET     the audit's central-phase and correction claims as exact
           gates: branch pinning, projective fifth power, cone theorem,
           square-root-free one tick, Sym central phase, mu_5 vs mu_10,
           tick-ladder integrality, split-unit projectors, rigidity
BASIS      Public Canon v30, STATE ACTIVE, AUTHORITY mathorn1973/twist-j
           main, TAG canon-v30, CONTENT_COMMIT
           857223fcd5e7bc8c8e68f1df768d6e8222b24ee0, CANON_SHA256
           2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
           CANON_BYTES 157167, SHA256SUMS 5 of 5 OK, verified this session
```

## Code

```text
verify_central_lift_phase.py
  sha256 e31b2ad0aa608c00db4fb863cd664f9731df57e3dbfb1ad1c1b0121eec8d9b58
  12863 bytes, 16 gates
```

Python 3 stdlib, exact arithmetic (Z[zeta5], Q(sqrt5), rational
complex, integer grids), deterministic, no randomness, no tolerance.

## Systematics

Grid proofs are frozen at the sizes stated in the gate names (3^4 for
the char-poly identity, 5^3 for (n.sigma)^2, 5^4 for the rigidity
lever); the unit sweep is +-zeta5^a phi^b with a = 0..4, |b| <= 2. The
residue facts cite the glue criterion of C-COMMON-CARRIER-ICOSIAN-1
(gate T3) for their integral interpretation.

## Failure thresholds

Any FAIL line fires F-CLP-1; both named structural falsifiers F-CLP-2,
F-CLP-3 are stated in the claim doc. Exit 0, empty stderr required.

## Action layer

L1/L4 algebraic identities only; the tick-counter reading is [D]; no
L5/L6 content, no dictionary claim, no registry row touched.
