# Independent exact review — C-GOLDEN-AME-J-RIGIDITY-1-N

Public lock: issue #369; preregistration commit
`bc06e77c86c74dfe1b7b988614a33b5130b877f7`.

This lane did not import the post-lock solver or `golden_symbolic.py`.
`independent_sympy.py` reparses the pinned `AME46_ORIGINAL.m` byte stream,
reconstructs the tensor and all three row-Gram systems, and works over exact
`QQ`.  `independent_stdlib_verify.py` repeats the parse and Gram construction
and checks the sealed artifacts with `fractions.Fraction` only.

## 1. Six-coordinate core and the complete complex ideal

In frozen raw-record order the following six literal coordinates generate the
same ideal as all 3,889 records:

```text
01:00:00
01:02:02
02:08:05
02:12:13
02:13:22
unit_phase
```

Their raw monomial lists, in source variable order `(alpha,beta,gamma,x,y)`,
are:

```text
01:00:00  = -1 + 2 gamma^2
01:02:02  = -1 + 2 beta^2 x^3 y^3 + 2 alpha^2 x^18 y^18
02:08:05  = beta gamma x^10 + alpha beta x^2 y^3
              + alpha beta x^19 y^18
02:12:13  = alpha beta x y^4 + alpha beta x^10 y^3
02:13:22  = beta gamma x^19 y^14 + beta^2 x^4 y^10
              + alpha^2 x^3 y^5
unit_phase = xy - 1
```

The reduced exact lexicographic basis for
`alpha > beta > gamma > y > x` is

```text
g0 = alpha + gamma*x^7/5 - 2*gamma*x^5/5
           + 3*gamma*x^3/5 - 4*gamma*x/5
g1 = beta + 3*gamma*x^7/5 - gamma*x^5/5
          - gamma*x^3/5 - 2*gamma*x/5
g2 = gamma^2 - 1/2
g3 = y + x^7 - x^5 + x^3 - x
g4 = x^8 - x^6 + x^4 - x^2 + 1
```

The independent SymPy run obtains this basis both from all 362 distinct
nonzero raw polynomials and from the six literal coordinates.  The stdlib
checker verifies Buchberger's criterion, reducedness, and zero normal form for
all 383 active raw records.  Thus no unused raw equation cuts the variety
further.

The raw ideal is already saturated.  In its quotient,

```text
D = alpha*beta*gamma*x*y
h = -8*gamma*x^6 + 8*gamma*x^4 + 4*gamma
D*h = 1.
```

Consequently `I_raw = I^circ`.  The frozen saturation basis for
`t > alpha > beta > gamma > y > x` is simply

```text
t + 8*gamma*x^6 - 8*gamma*x^4 - 4*gamma,
g0, g1, g2, g3, g4.
```

Canonical JSON hashes emitted by the independent serializer are:

```text
complex reduced basis   65693339a44018108bd147ec364d09ff20733da05040fe66b5ce98d39cd81935
saturation basis        5ff059e4ae7ecb73e769cddeb9b202d8e467fbac2a698cc05c771acc8b080fdf
```

This is a zero-dimensional degree-16 radical ideal.  It is in fact prime:
after eliminating the three linear variables its quotient is

```text
Q[x,gamma]/(Phi_20(x), gamma^2-1/2).
```

`Phi_20` is irreducible.  The quadratic subfields of `Q(zeta_20)` are
`Q(i)`, `Q(sqrt(5))`, and `Q(sqrt(-5))`; `Q(sqrt(2))` (conductor 8) is not
one of them.  Hence adjoining `gamma` doubles degree 8 to 16 and the quotient
is a field.  There are no extra complex components, embedded components, or
nilpotents, either before or after the prescribed saturation.

## 2. Exact real locus

After `x=u+i v`, `y=u-i v`, splitting over `Q`, adding `u^2+v^2-1`, and
using lex order `alpha > beta > gamma > v > u`, the reduced basis is

```text
h0 = alpha + (8/5)*gamma*u^3 - 2*gamma*u
h1 = beta - (16/5)*gamma*u^3 + 2*gamma*u
h2 = gamma^2 - 1/2
h3 = v^2 + u^2 - 1
h4 = u^4 - (5/4)*u^2 + 5/16.
```

Canonical JSON SHA-256:

```text
56cffa396293f2b309538b663d411627cbb3b264fc12604fe7553e3268498d6f
```

Put `p(u)=2u^2-3/2`.  Modulo `h4`,

```text
p(u)^2 = 1-u^2,
p(u)^(-1) = 8u^2-4.
```

Therefore the real ideal is the intersection of two comaximal reduced
components obtained by `v=p(u)` and `v=-p(u)`.  Its 16 real points are
parameterized by

```text
u^2 = (5 +/- sqrt(5))/8,
u = either square-root sign,
gamma = either sign of 1/sqrt(2),
v = either sign of sqrt(1-u^2),
alpha = (2/5)*gamma*u*(5-4u^2),
beta  = (2/5)*gamma*u*(8u^2-5).
```

The inequalities select exactly two points.  Positivity of `gamma` selects
`+1/sqrt(2)`.  Since `5-4u^2>0` for both roots, positivity of `alpha` then
selects `u>0`.  Finally `8u^2-5` is `+sqrt(5)` on the plus root and
`-sqrt(5)` on the minus root, so positivity of `beta` selects

```text
u^2 = (5+sqrt(5))/8.
```

The two surviving points are

```text
gamma = 1/sqrt(2),
alpha^2 = (5-sqrt(5))/20,
beta^2  = (5+sqrt(5))/20,
u = sqrt((5+sqrt(5))/8),
v = +/-(sqrt(5)-1)/4.
```

They are reduced and are exchanged by `v -> -v`, with identical positive
amplitudes.  There is no positive deformation and no finite positive
counterbranch.

## 3. Frozen targets and field readback

All six ordered target relations have zero normal form under the complex
basis.  Hence

```text
complex radical mask   111111
positive universal mask 111111
```

The phase polynomial is `Phi_20(x)` and divides `x^20-1`.  On the positive
points `x=u+iv` is `zeta_20` or its conjugate.  The two frozen entries give

```text
Uhat[0,1] = gamma,
Uhat[1,2] = gamma*x^17,
(17*13) mod 20 = 1,
```

so the nonzero entries recover both `gamma` and `x`.  Conversely the two seam
relations express `alpha,beta` in `Q(x,gamma)`, so every entry lies there.
Thus

```text
Q(nonzero entries) = Q(x,gamma) = Q(zeta_20,sqrt(2)).
```

Since `i=x^5` up to sign and `(1+i)/sqrt(2)` supplies `zeta_8`, the compositum
is `Q(zeta_20,zeta_8)=Q(zeta_40)`.  Complex conjugation is the only surviving
orientation ambiguity.

The independent verdict is therefore

```text
EXACT_J_RIGID_UP_TO_CONJUGATION
```

strictly within the preregistered tied printed-gauge family.

## 4. Reproduction hashes

Environment: CPython 3.12, SymPy 1.14.0, exact `QQ` only.

```text
independent_sympy.py
db628246afa7a58c5b8c4ab7ea65ca0617825330647b457e0705468fc63c0cc7

independent_stdlib_verify.py
af07bbeed1dd8469d3917cf0a45cd73587be656fbe8fbf647cca90b220cdfaf0

independent_sympy.py stdout
5cb4c9c756e25c69bcbb7effe88fde744dbac15e79bd1d7244a5acdcb8405e60

independent_stdlib_verify.py stdout
e840cf4eb52d0ec236d25f3666c9b0965235c01e54ad592123eeddb0ba92c043

INDEPENDENT_REP_CERT.md
dc1e1692377253babb797ef16e482a33064d8032ed537b3abc6dc1d0a7c25fb4

expanded six-coordinate representation (regenerated in memory; 233819 bytes)
541295971b4ebf3f221fd65e4435a9801b8c9e760c43191340ca17d6c281034b
```

The portable scripts write nothing, make no network calls, and reject an
optimized Python interpreter because the exact checks require active
assertions.
