# WINDOWED SOURCE-SIDE KREIN GRAM

```text
STATUS: candidate-T / candidate-D inside NON-CANONICAL incubation
ISSUE:  #355
PUBLIC STATUS CHANGE: none
```

This file sharpens the surviving target from scalar signed norms to the full Suzuki screw kernel. No zeta zeros and no RH assumption enter the factorization.

## 1. Half-argument alignment

Use Suzuki's spectral convention

```text
s = 1/2 - i xi,
w = s/2 = 1/4 - i xi/2.
```

For every prime power `n` define the complex amplitude atom

```text
alpha_n(xi) = sqrt(Lambda(n)) n^(-w).
```

Then exactly

```text
|alpha_n(xi)|^2 = Lambda(n)/sqrt(n),
alpha_n(xi) / |alpha_n(xi)| = exp(i xi log(n)/2).
```

Thus the quarter-power magnitude and half-phase are not independent patterns. They are the modulus and phase of the same square-root Dirichlet atom `sqrt(Lambda(n)) n^(-s/2)`.

At the archimedean place the completed zeta already contains `Gamma(s/2)=Gamma(w)`. Therefore, at the level of the completed logarithmic derivative used by Suzuki, the finite-place square-root atoms and the archimedean Gamma argument naturally meet at the same half-argument `w=s/2`. On the critical spectral axis `Re(s)=1/2`, this means `Re(w)=1/4`.

This is an exact alignment statement. It is not an RH proof and does not assert a square root of the complete xi-function.

In particular, `sqrt(Lambda(n))` is not multiplicative. These atoms do not
define an Euler product, and no Dirichlet series is claimed whose square is
`zeta`, `xi`, or `-zeta'/zeta`. The alignment is kinematic at the level of
the displayed factorization, not a multiplicative square-root construction.

## 2. Pole kernel is rank-(1,1) Pythagoras

Suzuki's pole piece is

```text
g_0(t) = -4(e^(t/2)+e^(-t/2)-2)
       = -8(cosh(t/2)-1).
```

Its screw kernel is

```text
G_0(t,u)=g_0(t-u)-g_0(t)-g_0(-u)+g_0(0)
        = 8[sinh(t/2)sinh(u/2)
            -(cosh(t/2)-1)(cosh(u/2)-1)].
```

Hence with scalar features

```text
x_0(t)=sqrt(8) sinh(t/2),
y_0(t)=sqrt(8) (cosh(t/2)-1),
```

we have

```text
G_0(t,u)=x_0(t)x_0(u)-y_0(t)y_0(u).
```

The scalar perfect square `[4 sinh(t/4)]^2` is the diagonal shadow of this rank-(1,1) kernel factorization.

## 3. Prime kernel is half-angle Krein Pythagoras

For one delayed leg `h_L(t)=(|t|-L)_+`, `HALFANGLE-PRIME-KERNEL.md` proves

```text
G_(h_L)(t,u)=<S_L(t),S_L(u)>-<C_L(t),C_L(u)>,
```

where

```text
phi_t(xi)=(exp(i xi t)-1)/xi,
S_L(t)(xi)=pi^(-1/2) sin(L xi/2) phi_t(xi),
C_L(t)(xi)=pi^(-1/2) cos(L xi/2) phi_t(xi).
```

For `L=log n`, multiplication by `sqrt(Lambda(n)) n^(-1/4)` gives the exact prime-power amplitude. The sine/cosine quadratures are exactly the imaginary/real quadratures of the half-phase `exp(i xi log(n)/2)` from the atom `alpha_n(xi)` above.

### Windowing is essential

A global direct sum of the positive and negative half-angle pieces over all prime powers is not asserted: for `L>|t|`, the two Hilbert norms need not vanish separately even though their Krein difference does.

Fix `a>0` and restrict `t,u in [-a,a]`. In the original unsplit delayed kernel, every leg with `L>2a` vanishes identically because `|t|`, `|u|`, and `|t-u|` are all `<L`. Therefore one first truncates the **original** prime kernel to the finite set

```text
log n <= 2a,
```

and only then applies the half-angle split. The resulting windowed positive/negative prime feature spaces are finite direct sums of `L2(R)` and are honest Hilbert spaces.

This order of operations avoids an illegal infinity-minus-infinity separation.

## 4. Gamma/Hurwitz kernel is OU increments minus Brownian

Let

```text
a_m=m+1/4,
kappa=log(pi)-psi(1/4)>0.
```

Suzuki's archimedean Gamma piece is

```text
g_inf(t)
 = (kappa/2)|t|
   + sum_(m>=0) [e^(-2a_m|t|)-1]/(4a_m^2).
```

Define the Brownian increment kernel

```text
K_B(t,u)=(|t|+|u|-|t-u|)/2.
```

Then the linear term contributes

```text
G_linear(t,u)=-kappa K_B(t,u).
```

For each `m`, the stationary Ornstein-Uhlenbeck kernel

```text
k_m(t,u)=e^(-2a_m|t-u|)
```

is positive definite. Its increment kernel relative to zero is

```text
K_m^inc(t,u)
 = e^(-2a_m|t-u|)-e^(-2a_m|t|)-e^(-2a_m|u|)+1,
```

also positive definite. Therefore

```text
G_inf(t,u)
 = sum_(m>=0) K_m^inc(t,u)/(4a_m^2)
   - kappa K_B(t,u).
```

The positive series converges absolutely and locally uniformly because the coefficients are `O(a_m^-2)` and each increment kernel is bounded on a fixed window.

An explicit OU feature may be taken in `L2(R,dr)` as

```text
eta_m(t)(r)=sqrt(4a_m) e^(-2a_m(t-r)) 1_(r<=t),
```

for which `<eta_m(t),eta_m(u)>=e^(-2a_m|t-u|)`. Thus

```text
q_m(t)=(eta_m(t)-eta_m(0))/(2a_m)
```

has Gram kernel `K_m^inc/(4a_m^2)`. A standard oriented interval indicator is an explicit Brownian feature for `K_B`.

## 5. Full windowed source-side Krein factorization

For every fixed `a>0`, assemble

```text
X_(+,a)(t):
  pole positive feature x_0(t),
  prime sine half-angle features for log n<=2a,
  all Gamma OU increment features q_m(t),

X_(-,a)(t):
  pole negative feature y_0(t),
  prime cosine half-angle features for log n<=2a,
  Brownian counterterm sqrt(kappa) beta_t,
```

where `beta_t` is the oriented interval feature with Gram `K_B`.

Then for every `t,u in [-a,a]`, exactly

```text
G_g(t,u)
 = <X_(+,a)(t),X_(+,a)(u)>
   - <X_(-,a)(t),X_(-,a)(u)>.
```

This is a source-side Krein-Gram factorization of Suzuki's full screw kernel using only the pole, prime-power, and Gamma/Hurwitz data already present in equation (1.1) and its exact decomposition. It contains no zero ordinate.

## 6. Gram-domination lemma: the real next target

Let `X_+:T->H_+` and `X_-:T->H_-` be any two feature maps. The kernel

```text
K(t,u)=<X_+(t),X_+(u)>-<X_-(t),X_-(u)>
```

is positive semidefinite on `T` **iff** there exists a contraction

```text
T0 : closure(span X_+(T)) -> closure(span X_-(T))
```

such that

```text
T0 X_+(t)=X_-(t)   for every t in T.
```

### Proof

If `K` is positive, then for every finite coefficient family

```text
||sum c_j X_-(t_j)||^2 <= ||sum c_j X_+(t_j)||^2.
```

Therefore any linear relation among the `X_+` vectors is also a relation among the `X_-` vectors. The prescription

```text
sum c_j X_+(t_j) -> sum c_j X_-(t_j)
```

is well-defined and contractive on the algebraic span, hence extends uniquely to its closure. The converse follows immediately from contractivity.

### Source boundary for the downstream RH reading

The frozen `PREREG.md` imported Suzuki Theorem 1.7 only, which is the
pointwise criterion `RH iff Psi(t)>=0`. That theorem controls the diagonal
`G_g(t,t)=2Psi(t)` but does not by itself imply positivity of all mixed
finite Gram matrices.

The source-side factorization above and the abstract Gram-domination lemma
do not need any further RH criterion. The downstream equivalence in the next
paragraph additionally imports Suzuki Theorem 1.2, which states that RH is
equivalent to `g` being a screw function, hence to positivity of `G_g` on
every finite window. Suzuki Theorem 1.3 is a separate localized
hermitian-form criterion on its stated zero-mean test class. It is not a
direct substitute for Theorem 1.2 in the pointwise-kernel statement unless
the required kernel-to-form bridge, domains, and normalizations are supplied.

This is a post-freeze source disclosure. It does not rewrite the preregistered
input. Any promoted public lock must name the theorem appropriate to its
kernel or form scope explicitly.

### Consequence for this incubation

By imported Suzuki Theorem 1.2, RH is equivalent to positivity of `G_g` on
every finite window. Combined with the explicit factorization above:

```text
RH
iff for every a>0 there exists a contraction T_a
    with T_a X_(+,a)(t)=X_(-,a)(t) for all |t|<=a.
```

This equivalence is a reformulation, not a proof.

The new non-circular construction problem is now precise:

```text
construct T_a directly from the explicit source-side channels,
prove ||T_a||<=1 without RH or zero data,
and control compatibility as a increases.
```

A contraction obtained only after assuming positivity is circular and earns nothing.

## 7. Structural conclusion

The local breaker and the exact two-point prime-sector witness in
`NO-LOCAL-CONTRACTION.md` have a sharper meaning. Each delayed prime leg is
indefinite, and the whole prime sector remains indefinite even after arbitrary
mixing among prime powers. Any successful `T_a` must use **cross-place
mixing** between finite-prime quadratures and the pole/Gamma boundary
channels for these explicit carriers.

This is exactly the sense in which a proof, if it exists in this representation, must be a global Pythagorean theorem rather than a sum of locally positive prime energies.

The half-angle is forced at the prime-kernel level. A fixed `zeta_8` is not. Its legitimate appearance is only as the special value of the universal half-phase when a local full phase is `i`, or under an independently justified balanced-quadrature selector.
