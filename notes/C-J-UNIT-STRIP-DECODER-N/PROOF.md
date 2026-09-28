# C-J-UNIT-STRIP-DECODER-N proof

```text
STATUS:             NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:  candidate-T proof layer; candidate-C finite count
ACTION LAYER:       L1 only
PUBLIC LOCK:        issue #1269
BASE:               b648e2dfb8ea8f1519e8e0a6e139c0bb49676ade
CANON/REGISTRY:     UNCHANGED
```

The general native reader classification is already public as
`U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]`. This note adds no competing
classification. It specializes that theorem to one chosen integral scalar
carrier and proves the arithmetic needed for the specialization.

## 1. J-strip normal form

Let `K=Q(zeta)`, `O_K=Z[zeta]`, `zeta^5=1`, `zeta!=1`,
`phi=-zeta^2-zeta^3`, and `J=1+zeta^2=zeta/phi`.
For the labeled embeddings `sigma_a(zeta)=zeta^a`, put for nonzero alpha

```text
c(alpha) = (log|sigma_2(alpha)|-log|sigma_1(alpha)|)/(2 log phi).
```

The two relevant absolute values of J are `phi^-1` and `phi`, hence c is
additive and `c(J)=1`. Let

```text
B = { beta in O_K\{0} : 0 <= c(beta) < 1 }.
```

For every nonzero alpha define `n=floor(c(alpha))` and
`beta=J^(-n) alpha`. Since `J^-1=-zeta-zeta^2` is integral, beta is integral,
and `0<=c(beta)<1`. If `J^n beta=J^m gamma` with beta,gamma in B, then
`n-m=c(gamma)-c(beta)` is an integer in (-1,1), hence zero. Therefore

```text
O_K\{0}  <->  Z x B,      alpha <-> (n,beta),
```

and multiplication by `J^k` adds k to n and leaves beta unchanged.

## 2. Integer reduction test

Write the relative norm

```text
alpha*bar(alpha) = u + v phi,      u,v in Z.
```

For `alpha=a+b zeta+c zeta^2+d zeta^3`, direct reduction by
`1+zeta+zeta^2+zeta^3+zeta^4=0` gives

```text
u = a^2-ab+b^2-bc+c^2-cd+d^2,
v = ab-ac-ad+bc-bd+cd.
```

The two real embeddings are

```text
A  = u+v phi        = |sigma_1(alpha)|^2,
A' = u+v-v phi      = |sigma_2(alpha)|^2,
```

and the absolute norm is

```text
N(alpha)=u^2+uv-v^2.
```

Now `0<=c(alpha)<1` is equivalent to `A<=A'<phi^4 A`. Exact subtraction gives

```text
A'-A          = -v sqrt(5),
phi^4 A - A'  = (u+2v)(1+3phi).
```

Both fixed factors are positive. Thus

```text
alpha in B  iff  v<=0 and u+2v>0.
```

This yields an exact integer algorithm. If `(u_m,v_m)` are the coefficients of
`phi^(2m)(u+v phi)`, then `v_m<=0` iff `m<=c(alpha)`. Exponential bracketing
and binary search therefore recover `floor(c(alpha))` without logarithms or
floating point.

## 3. Binary carry

For beta,gamma in B,

```text
e(beta,gamma)=floor(c(beta)+c(gamma)) in {0,1},
beta star gamma = J^(-e) beta gamma in B.
```

Hence

```text
(n,beta)(m,gamma)=(n+m+e, beta star gamma).
```

The carry satisfies

```text
e(beta,gamma)+e(beta star gamma,delta)
 = e(gamma,delta)+e(beta,gamma star delta),
```

because both sides equal `floor(c(beta)+c(gamma)+c(delta))`.

For the ramified generator `pi=1-zeta`, direct ring arithmetic gives

```text
pi*bar(pi)=3-phi,      N(pi)=5,      c(pi)=1/2,
(1-zeta)^2 = -sqrt(5) J,
(1-zeta)^4 = 5 J^2.
```

Thus two reduced copies of pi produce exactly one J-carry.

## 4. Finite strip and exact orbit count

For beta in B put `t=c(beta)`. Then

```text
|sigma_1(beta)| = N(beta)^(1/4) phi^(-t),
|sigma_2(beta)| = N(beta)^(1/4) phi^t.
```

So `B_X={beta in B:N(beta)<=X}` is finite.

For beta=`sum_(j=0)^3 a_j zeta^j`, set `a_4=0`. Five-point Fourier inversion
applied to `a_j-a_4` gives

```text
a_j = (1/5) sum_(k=1)^4 sigma_k(beta)
                    (zeta^(-kj)-zeta^(-4k)).
```

Therefore

```text
|a_j| <= (4/5)(r_1+r_2)
       < (4/sqrt(5)) X^(1/4),
```

because on the half-open strip
`r_1+r_2=N^(1/4)(phi^t+phi^-t)<sqrt(5)X^(1/4)`.
Thus the complete search box has radius

```text
B_coeff = floor((256X/25)^(1/4)).
```

The public rows `J-HARMONIC-SEAM [T]` and
`CYCLOTOMIC-CLASS-NUMBER-ONE [T]` give

```text
O_K^x = mu_10 x <phi> = mu_10 x <J>,      h_K=1.
```

Every nonzero integral ideal is therefore principal, and its generators modulo
powers of J form exactly ten classes. Since the strip is a fundamental domain
for those J-orbits,

```text
|B_X| = 10 A_K(X)
```

for every X>=1, where `A_K(X)` counts nonzero integral ideals by norm.

Independently of lattice enumeration, prime splitting in `Q(zeta_5)` gives the
local ideal factors, with `t=p^-s`,

```text
p=5:       (1-t)^-1,
p=1 mod 5: (1-t)^-4,
p=4 mod 5: (1-t^2)^-2,
p=2,3 mod5:(1-t^4)^-1.
```

The exact finite audit expands these factors and compares every norm 1..1000
with the complete lattice box. The frozen cumulative targets are

```text
|B_940|=3110,   |B_941|=3150,   |B_1000|=3410.
```

These finite values are candidate-C until a formal public computation gate is
run. The formulas surrounding them are proof statements.

## 5. Selected native scalar code

Import the public theorem `U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]`. On the
origin-zero reachable domain D it supplies conserved onto labels
`ell_n in F_5^5` and proves that for every stipulated target bijection L,
all exact readers have the form

```text
R(n,x)=L^n G(ell_n(x)).
```

For n>=3 each ell_n is a bijection of the synchronized sheet with `F_5^5`.
Choose `L(alpha)=J alpha`. Sort B_941 by `(N(beta), coefficient tuple)` and map
the base-five index of each label to the corresponding first 3125 entries.
Call this injection b. Define

```text
R_J(n,x)=J^n b(ell_n(x)).
```

Then the imported conservation law gives `R_J(U omega)=J R_J(omega)`.
Norm J=1 gives `N(R_J)<=941`. Since every codeword b(label) is reduced, the
strip decoder returns exactly `(n,b(label))`. Thus R_J is injective on the
union of all reachable sheets with n>=3 and has an explicit inverse.

This is a chosen coordinate dictionary. Neither J as target nor b as codebook
is selected by the native theorem.

## 6. Sharp capacity threshold in the frozen class

Consider nonzero integral scalar readers which

1. satisfy exact U-to-J equivariance,
2. are globally injective across all reachable sheets n>=3, and
3. obey one uniform bound `N(R)<=X`.

By the imported classification, `R(n,x)=J^n G(ell_n(x))`. If two distinct
labels i,j have `G(i)=J^m G(j)`, choose n so both n and n+m are at least three.
Then

```text
R(n,ell_n^-1(i)) = R(n+m,ell_(n+m)^-1(j)),
```

contradicting global injectivity. Therefore the 3125 labels require 3125
distinct J-orbits. A norm bound X supplies exactly `|B_X|` such orbits.
The finite audit gives `|B_940|=3110<3125` and `|B_941|=3150>=3125`.
The construction in section 5 attains 941. Hence, conditional only on those
exact finite counts,

```text
X_min = 941.
```

This is not a bound for fixed-time injectivity, where cross-time collisions are
allowed. It is not a physical constant.

## 7. Scope boundary

Imported public claims are used without strengthening:
`J-UNIT`, `J-GOLDEN-BRIDGE`, `J-PROJECTIONS`, `J-HARMONIC-SEAM`,
`CYCLOTOMIC-CLASS-NUMBER-ONE`, `REGULATOR-TWO-LOG-PHI`,
`QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS`,
`U-NATIVE-CHART-AND-QDD-READBACK`, and
`U-COUNTER-REACHABLE-AMPLITUDE-CLASS`.

No Canon or Registry move follows. No physical clock, preferred codebook,
Hodge amplitude, Born law, apparatus, event, measure, SI scale or L2-L6 bridge
is claimed. The regulator `2 log phi`, this scalar J exponent, and the
`4 log phi` coaxial rapidity spacing of PR #683 remain distinct.
