# Exact scoped result

Public lock: issue `#369`, preregistration commit
`bc06e77c86c74dfe1b7b988614a33b5130b877f7`, tree
`0f8057a815efee04a1ed47b81336765fa237e84b`.

## Verdict

```text
EXACT_J_RIGID_UP_TO_CONJUGATION
```

This verdict is restricted to the preregistered three-amplitude/one-phase,
support/label/exponent-tied printed-gauge family.  It is not a uniqueness
theorem for all AME(4,6) tensors, support-only completions, or local-unitary
orbits.

## Complex ideal

All 3,889 frozen raw records reproduce the locked 136,262-byte stream with
SHA-256
`09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762`.
There are 383 active records and 362 distinct normalized nonzero
polynomials.

In lexicographic order `alpha > beta > gamma > y > x`, the raw ideal has
reduced basis

```text
alpha + gamma*x^7/5 - 2*gamma*x^5/5
      + 3*gamma*x^3/5 - 4*gamma*x/5
beta  + 3*gamma*x^7/5 - gamma*x^5/5
      - gamma*x^3/5 - 2*gamma*x/5
gamma^2 - 1/2
y + x^7 - x^5 + x^3 - x
x^8 - x^6 + x^4 - x^2 + 1
```

The saturation divisor `D=alpha*beta*gamma*x*y` is already a unit modulo the
raw ideal, with

```text
D * (-8*gamma*x^6 + 8*gamma*x^4 + 4*gamma) = 1.
```

Thus the raw and saturated ideals coincide.  In the frozen order
`t > alpha > beta > gamma > y > x`, the saturation basis adds only

```text
t + 8*gamma*x^6 - 8*gamma*x^4 - 4*gamma.
```

The tracked 276,630-byte certificate has SHA-256
`79db9845615cea94540211a383e49471fe2a92cd02388a7caac92d20f9d76526`.
The quotient is zero-dimensional of degree 16, radical, and prime over
`Q`.  Equivalently it is

```text
Q[x,gamma]/(Phi_20(x), gamma^2-1/2),
```

a degree-16 field.

The canonical machine-readable final record is `RESULT.json` (2,434 bytes,
SHA-256
`ed58df12b9b41e892da017d7d6f24f19f5d3e6056f649059604e318ef55b4a41`).
`verify_result_json.py` cross-checks it against the immutable Groebner,
target-blind, real-positive, target-evaluation, and controls artifacts.

## Positive real locus and targets

After imposing `x=u+i*v`, `y=u-i*v` and the unit circle, the exact real
locus has 16 reduced points.  Positivity leaves exactly two:

```text
gamma = 1/sqrt(2)
u^2   = (5+sqrt(5))/8
v     = +/-(sqrt(5)-1)/4
alpha^2 = (5-sqrt(5))/20
beta^2  = (5+sqrt(5))/20.
```

They are exchanged by complex conjugation.  All six preregistered target
polynomials have zero normal form, so the complex-radical and
positive-universal masks are both `111111`.

The pinned entries recover `gamma` and `x` (the inverse of exponent 17 is 13
modulo 20), while every entry lies in `Q(x,gamma)`.  Therefore

```text
Q(nonzero entries) = Q(x,gamma)
                   = Q(zeta_20,sqrt(2))
                   = Q(zeta_40).
```

Consequently `zeta_5=x^4` and the frozen arithmetic readout
`J(x)=1+x^8` are forced within this family, with complex conjugation as the
only surviving orientation ambiguity.

## Independent replay (G7)

G7 is `PASS`.  A post-lock parser rebuilt all 3,889 records directly from
the pinned MATLAB literal.  The independent exact SymPy lane recovered the
same reduced complex basis both from all 362 distinct nonzero raw
polynomials and from only the six literal tags
`01:00:00`, `01:02:02`, `02:08:05`, `02:12:13`, `02:13:22`, and
`unit_phase`.  The standard-library lane independently reparses the source,
checks Buchberger's criterion, all 383 active raw residuals, saturation
redundancy, the real sign classification, and all frozen targets.  The
separate G3 controls lane supplies the independent construction-B fixture and
column-Gram audit.  Details and exact hashes are in `INDEPENDENT_REPORT.md`.

## Controls

NC0--NC5 pass.  In particular, the phase-free control retains an infinite
positive locus and forces none of the six targets; conjugation acts as
`v -> -v`; the two independent locked tensor constructions agree in all 112
positions; and all 3,888 independently constructed column-Gram coordinates
vanish at the exact known point.  Column redundancy follows from the
universal determinant/adjugate identity recorded in
`COLUMN_REDUNDANCY_CERTIFICATE.txt`.
