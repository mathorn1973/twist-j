# P-J-LI-CARRIER-NOGO-1 result

Status: `PROVED AND AUDITED / CANON UNCHANGED`

## Disposition

```text
theorem:    no unitary with finite-dimensional cyclic subspace realizes
            the Li ladder. Exactly: q_n = a* n^2 + R_n with
            a* = ||P_(z=1) v||^2 and 0 <= R_n <= C; against Li
            nonnegativity (Bombieri-Lagarias) and the Lagarias asymptotic
            both branches close. Corollaries: every exact realization has
            infinite spectral support, 1 in the support, no atom at 1.
integrity:  no STOP. One formal execution, exit zero, empty stderr,
            6/6 gates PASS, stdout equal to EXPECTED.txt.
```

The audited exemplars live inside the program's own field
Q(zeta_10) = Q(zeta_5): the mu_10 rotation gives the exact 10-periodic
ladder with period maximum 6 + 2 sqrt5 = 4/|1 - zeta_10|^2, attained,
which is the proof's remainder bound realized with equality; the
eigenvalue-1 carrier gives q_n = n^2; their orthogonal sum gives the
mixed branch with the exact bracket.

## Proposed registry consequence (a later sealed fold, not this probe)

J-LI-CYCLIC-CARRIER-DIMENSION [T], exact row text frozen in PREREG.md,
canon section 16. It complements the registered carrier no-gos
(J-LI-TORAL-HAAR-NOGO, J-LI-LAMBDA-HAAR-HS-NOGO, J-LI-LAMBDA-SHIFT-NOGO):
those exclude specific carriers, this one excludes every finite one and
forces the support facts. No live row moves; RH stays O.

## Evidence boundary

Local formal leg x86_64 (Ubuntu 24.04.4 LTS, CPython 3.11.15); the
pull-request workflow supplies the x86_64 and aarch64 replays against
EXPECTED.txt, completing the repository two-architecture computation gate.
The universal statement is carried by the written proof with imports
labeled (Li / Bombieri-Lagarias, Lagarias, spectral theorem); the verifier
audits the finite mechanism only. Nothing here advances RH or any
physical row, and the cocycle-vector form of LAMBDA-COCYCLE-ANGLES [H] is
untouched.
