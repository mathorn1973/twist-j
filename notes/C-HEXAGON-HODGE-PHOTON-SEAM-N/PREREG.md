# PREREG - C-HEXAGON-HODGE-PHOTON-SEAM-N

**Status:** PUBLIC, NON-CANONICAL incubation. No Canon authority.  
**Owner:** A. M. Thorn / hexagon-hodge-photon-seam-20260927  
**Date:** 2026-09-27  
**Issue:** #1219  
**Action layer:** L1 exact algebra only.  
**Authority:** Public Canon v92. Normative files remain unchanged.

## Purpose

Freeze one narrow seam suggested by the six-register / four-chart discussion.
The candidate does **not** attempt to derive physical dimension or identify the
native checkpoint with an electromagnetic field. It tests whether the most
direct six-to-six linear identification is mathematically available, and
whether integer time blocking repairs it.

## Frozen inherited inputs

Only the following current public rows are used, at their registered L1 scope.

1. `J-HODGE-HERM2-LOXODROME [T]`:
   the marked fixed-J predictive carrier `E_+` has dimension four, is
   `L`-invariant, has real wedge signature `(3,1)`, and its step
   `A=L|E_+` has characteristic polynomial

   ```text
   p_E(x)=(x^2-3x+1)(x^2-phi x+1),
   phi=(1+sqrt(5))/2.
   ```

2. `J-HODGE-RATIONAL-CLOSURE [T]`:
   `W_Q=Lambda^2(A4 tensor Q)` is the minimum Q-defined containing carrier for
   the full fixed-J chart, with rank-six integral witness `Lambda^2 A4`.

3. `J-HODGE-SEMILINEAR-MEMORY [T]`:
   the exact present plus triple reconstructs the rational source through
   conjugation and the least fixed-J F-linear predictive realization has
   dimension four; its primary axial recurrence is

   ```text
   y_(n+2)=3 y_(n+1)-y_n.
   ```

4. `J-C5-HODGE-CONIC-ATLAS [T]`:
   the six accepted Hodge axes are the six Sylow-five labels and are not a
   canonically ordered planar six-cycle.

The photon rows are **context only**, not theorem premises:
`PHOTON-TEMPORAL-CHARACTERISTIC [T]`, `PHOTON-HERM2-TANGENT-GERM [T]`,
`PHOTON-CONE-CONVERGENCE [O]`, and `PHOTON-MASSLESS-PHASE [O]`.

## Frozen carriers and operators

Let

```text
F   = Q(sqrt(5)),
V   = A4 tensor Q,
W_F = (Lambda^2 V) tensor F.
```

In the marked `A4` basis `e0-e4,...,e3-e4`, let `C` be the coordinate
five-cycle and put

```text
M = I + C^2,
L = Lambda^2 M  on W_F.
```

Let `A=L|E_+` be the accepted four-dimensional fixed-J predictive step, and
put

```text
B = Lambda^2 A  on Lambda^2 E_+.
```

All equality below is literal F-linear operator equality on these fixed
carriers. No quotient, similarity up to scalar, nonlinear map, history field,
auxiliary carrier or layer lift is silently admitted.

## G1. Planar-hexagon mnemonic audit

For a display coordinate tuple `(r0,...,r5)`, freeze the conversational map

```text
x0 = r0-r3
x1 = r1-r4
x2 = r2-r5
tau = r0+r1+r2+r3+r4+r5
g1 = r0+r3-r1-r4
g2 = r0+r3+r1+r4-2r2-2r5.
```

Decision:

- compute its integer determinant exactly;
- test the antipodal-odd three-space under one vertex rotation;
- record only the algebraic conclusion.

A non-unimodular map or reducible odd triple forbids treating this picture as
six independent integer coordinates or as a symmetry-forced physical
`3+1+2` decomposition. It does not forbid the picture as a mnemonic.

## G2. Same-step six-to-six seam

Compute the exact characteristic polynomial of `L` from the marked `A4`
construction and of `B=Lambda^2 A` from the accepted `p_E`.

Freeze the complete class

```text
Hom_1 = { S in Hom_F(W_F,Lambda^2 E_+) : S L = B S }.
```

Accepted outcomes:

- `SAME-STEP-ZERO` if `Hom_1={0}`;
- `SAME-STEP-SEAM` otherwise, with exact dimension.

A proof by coprime characteristic polynomials is admitted only if both
polynomials are independently reconstructed exactly and the polynomial gcd is
exactly one over `F`.

## G3. Complete positive-integer blocking class

For every positive integers `m,n`, freeze

```text
Hom_(m,n) = { S : S L^m = B^n S }.
```

Using `zeta=zeta_10`, the accepted spectral data imply the frozen labels

```text
Spec(L^m):
  phi^(2m), phi^(-2m), zeta^m, zeta^(3m), zeta^(7m), zeta^(9m)

Spec(B^n):
  1, 1,
  phi^(2n) zeta^n, phi^(2n) zeta^(-n),
  phi^(-2n) zeta^n, phi^(-2n) zeta^(-n).
```

The primary theorem target is the all-positive-integer formula

```text
dim_F Hom_(m,n) = 0    if 10 does not divide m,
                    8    if 10 divides m and m != n,
                   12    if 10 divides m and m = n,
```

and the stronger decision that **no positive pair `(m,n)` admits an invertible
intertwiner**.

The proof must be all-integer, not a finite extrapolation. A finite exact
census is audit only.

## G4. Axial-recurrence boundary

For the accepted scalar recurrence `y'=3y-z`, `z'=y`, prove directly that

```text
I(y,z)=y^2-3yz+z^2
```

is invariant and has signature `(1,1)` over R. Record explicitly that this is
an algebraic invariant of the predictive recurrence and is not thereby the
selected photon temporal transfer law.

## G5. Photon firewall

No positive or negative outcome here:

- identifies `Lambda^2 E_+` with the selected photon carrier `T_D3`;
- changes `PHOTON-CONE-CONVERGENCE [O]`;
- changes `PHOTON-MASSLESS-PHASE [O]`;
- establishes a continuum limit, Lorentz-covariant physical field strength,
  polarization, propagator, occurrence law, apparatus or SI scale;
- closes `TRACEKERNEL-CURVATURE-FORCING [O]`.

A restricted negative leaves multichart, twisted-bundle, history-dependent,
nonlinear, counter-assisted, field-valued and conformally rescaled bridges
outside scope.

## Exact audit contract

Only after this file, `verify.py`, and `break.py` are committed, pushed and
publicly read back may the candidate audit execute.

`verify.py` is standard-library only and must check:

1. the exact marked `A4` exterior-step polynomial;
2. the exact `Lambda^2 E_+` polynomial from `p_E`;
3. gcd one for the same-step class;
4. the planar mnemonic determinant and reducibility control;
5. an exact finite census against the all-integer blocking formula;
6. the quadratic invariant of the axial recurrence.

`break.py` is a separate spectral-label attack written from this frozen
preregistration. It is not an independent-agent confirmation. It attempts to
find a blocked common spectrum, an invertible multiplicity match, or a
repair by target time reversal.

## Falsifiers

Any exact failure of G1-G4 fires the corresponding candidate clause.
Implementation, pin, public-readback or runtime failure is STOP.

## Repository boundary

Only `notes/C-HEXAGON-HODGE-PHOTON-SEAM-N/` may be added in this candidate PR.
No Canon, Registry, Frontier, gate, formal probe, workflow, tool or existing
note may be changed.
