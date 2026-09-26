# Preregistered signed-slice and insertion audit

PUBLIC, NON-CANONICAL; notes item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Basis: Public Canon v91, main 6f181bb96b9b0692c03195dbc12233b14ed2b476.

This is a finite candidate-C audit of the written candidate-T derivation in
SIGNED-SLICES.md. It is not a formal P-probe or a P1 certificate. No scientific
execution of this continuation precedes its public pin.

## Inputs and execution order

Commit and publicly read back this file, SIGNED-SLICES.md and the complete
verify_signed_slices.py before its first execution. Record the immutable
commit and SHA-256 values. The unchanged imported helper is
verify_connected_current.py from #1156, SHA-256
`ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403`.
Its top-level audit must not run on import. All four files must be present
and hash-checked at the same public commit. Static syntax checks are allowed
before pinning; scientific execution is not.

On Linux x86_64 with Python 3 and only standard-library exact integer and
Fraction arithmetic, run from this note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_signed_slices.py
```

Budget: 60 seconds. Require exit zero, empty stderr, and the final line
`RESULT PASS; no uniform upper-chi estimate or positive P1 gap`.
Preserve exact stdout, environment, timing, hashes and byte counts in
SIGNED-RUN-20260924.md. No random sampling or floating-point evaluation is
part of this audit.

## Frozen mathematical targets

1. For D=3,4,8,16,32 and L=2D+4, construct the aligned bridge in the written
   proof. Check ternary coefficients, 4D+40 faces, 2D+10 faces of orientation
   01, eight degree-five and 8D+60 degree-two edges. The current consists of
   two disjoint, equally oriented elementary loops. The signed constraint
   graph is connected and consistent, hence has exactly two signings.
2. Check the complete signed axial slice vector, not a floating form factor:
   A(0)=A(D+1)=-5 and all other A(r)=0. Check its boundary relation with the
   slice current, its exact minimum absolute-deviation quotient ell=2, and
   the raw counting comparison ell <= m01/5. This establishes the stated
   Laurent-polynomial form factor for each audited fixture. The all-D
   statement and nonvanishing trigonometric limit require the written proof.
3. Check integer-closed cube fixtures have constant longitudinal slice
   vector and ell=0. Check subtraction of a constant leaves every nonzero
   discrete Fourier coefficient unchanged through the exact polynomial
   quotient, not an approximate transform. No uniform ensemble moment is
   inferred from these fixtures.
4. On L=8 and L=12, construct each central 01 and central 02 four-cup
   insertion. Check 21 faces, four degree-five and 32 degree-two edges,
   one consistent paired component and the exact boundary -5 partial p.
   Construct the whole edge-sharing face neighborhood B and check |B|<=153.
   For the longitudinal insertion check A01=-5 delta_0; for the transverse
   insertion check A02=-3 delta_0-delta_1-delta_(-1). These verify the
   geometric inputs to the full-measure insertion proof. They do not
   enumerate the full partition function or replace its analytical proof.
5. Check the exact rational constant rho=2^-173 and b_floor=25 rho, and
   record that this floor equals 25 times the proved lower bound on chi.
   It therefore cannot exceed 25 times any valid upper bound on chi.

The targets and thresholds are derived before execution. Every failure,
nonzero exit, unexpected stderr, timeout or input hash mismatch is retained
against the unchanged pin. Do not repair a frozen file or rerun a changed
target silently. A repair needs a new public pin and explicit disposition
of the failed attempt.

## Scope and review

The finite audit is candidate-C on one architecture. The analytical statements
are candidate-T only, with separate agent review using shared sources, not
blind external acceptance. Ordinary repository CI checks both architectures
but does not execute this notes audit and is not its scientific gate.

The signed-slice moment has no evaluated volume-uniform upper constant.
The evaluated positive b floor is supplied by bounded charged components,
which contribute equally to 25 chi in the infrared. The original numerical
comparison and P1 remain open, as do P2 and the later spectral obligations.
No Canon, Registry, formal probe or phase claim changes.
