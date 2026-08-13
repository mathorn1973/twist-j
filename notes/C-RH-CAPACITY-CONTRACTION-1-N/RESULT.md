# RESULT C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS: NON-CANONICAL INCUBATION RESULT
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## R0. Current decision state

```text
G1  DELAYED-KREIN-FACTOR          candidate-T, closed algebraically
G2  PURE-ARCHIMEDEAN-SCHUR-NOGO  candidate-T, closed abstractly
G3  CAPACITY-POSITIVITY           OPEN, sharply reduced
G4  CAPACITY-CLOSURE              BLOCKED on G3
G5  CUTOFF-COHERENCE              candidate-T restriction law obtained
G6  NESTED-CONTRACTION            BLOCKED on G3-G5
```

No RH or Weil-positivity conclusion is claimed.

## R1. Exact finite-place signed factor

For `v in D_a=C_c^infty(-a,a)`, write `f=E_a v` and

```text
C_L(v) = <U_L f,f>,
w_n    = Lambda(n)/sqrt(n),
L_n    = log n.
```

Since `supp(f)` has diameter `<2a`, `C_L(v)=0` for `L>=2a`. The prime part of
Suzuki's Weil functional is

```text
q_P,a(v)=-2 sum_(L_n<2a) w_n Re C_(L_n)(v).
```

With

```text
(V_a^-v)_n=sqrt(w_n/2)(f-U_(L_n)f),
(V_a^+v)_n=sqrt(w_n/2)(f+U_(L_n)f),
```

translation invariance of the full `L2(R)` norm gives exactly

```text
q_P,a(v)=||V_a^-v||^2-||V_a^+v||^2.
```

For one delayed block the Hermitian bilinear matrix has both signs. Hence no
invertible change of basis can make an isolated prime leg positive (Sylvester
inertia law). The exact finite breaker records a normalized determinant `-1`.

**Status:** candidate-T.

## R2. Exact archimedean Dirichlet decomposition

Start directly from Suzuki's displayed Weil functional on PDF page 1. For
`f=v*tilde(v)`, one has

```text
f(0)=||v||^2,
f(t)+f(-t)=2 Re <U_t E_a v,E_a v>.
```

Define

```text
M_+(v)=integral_R v(x)e^(x/2) dx,
M_-(v)=integral_R v(x)e^(-x/2) dx,
K(t)=e^(-t/2)/(1-e^(-2t)),
kappa=log(pi)-psi(1/4)
     =log(pi)+EulerGamma+pi/2+3 log 2 >0.
```

The polar term factors as

```text
integral f(t)(e^(t/2)+e^(-t/2))dt
  = |M_+(v)|^2+|M_-(v)|^2.
```

For the gamma/infinite-place term, use

```text
||f-U_t f||^2 = 2||f||^2-2 Re <U_t f,f>
```

on the zero-extended carrier together with the integral representation of the
digamma function. The exact result is

```text
q_gamma(v)
 = integral_0^infinity K(t)||E_a v-U_t E_a v||^2 dt
   - kappa ||v||^2.
```

Equivalently, in Fourier variables its multiplier is

```text
Re psi(1/4+i xi/2)-log pi
 = -kappa
   + 2 integral_0^infinity K(t)(1-cos(xi t))dt.
```

This is the direct archimedean counterpart of the finite-place delayed
Pythagorean factors. No zeta zero enters.

**Status:** candidate-T.

## R3. Capacity form reduced to one spectral-gap inequality

Combining R1 and R2 gives the frozen capacity candidate in the explicit form

```text
q_A,a(v)
 = |M_+(v)|^2+|M_-(v)|^2
 + integral_0^infinity K(t)||E_a v-U_t E_a v||^2 dt
 + (1/2) sum_(L_n<2a) w_n ||E_a v-U_(L_n)E_a v||^2
 - kappa ||v||^2.
```

Thus every term except the single scalar `-kappa||v||^2` is manifestly
nonnegative. G3 is exactly the coercivity question

```text
E_a(v) >= kappa ||v||^2,
```

where `E_a` is the sum of the two polar squares, the continuous
archimedean jump energy, and the discrete prime-power jump energy displayed
above.

This is strictly sharper than writing `q_A=Q_W+||V^+||^2`: it gives a direct
source-side object which can be attacked without RH.

### Diagnostic only

A non-formal Galerkin search using Dirichlet sine bases (dimensions up to 20,
cutoffs sampled through `a=4`) found no negative direction of `q_A,a`. The
smallest values occur below the first prime threshold and approach zero near
`a=(log 2)/2`; after the first prime channel enters the diagnostic gap jumps
upward. This is **not evidence for G3** and carries no candidate-C status until
packaged under a frozen numerical protocol.

## R4. Exact translation-chain lower bound

Let `I` be an interval of length `T=2a` and let `0<L`. Compression of
translation by `L` to `I` decomposes, after writing points by residue modulo
`L`, into finite path chains. If

```text
m(L)=ceil(T/L)
```

(the a.e. maximal chain length), the Hermitian part of the path shift has
largest eigenvalue

```text
cos(pi/(m(L)+1)).
```

Therefore for every `v` supported in `I`,

```text
||v-U_L v||^2
 >= 2[1-cos(pi/(m(L)+1))] ||v||^2.
```

For `a<L<2a`, `m(L)=2`, yielding the simple exact bound

```text
||v-U_L v||^2 >= ||v||^2.
```

Consequently G3 has the unconditional sufficient lower bound

```text
q_A,a(v)/||v||^2
 >= G_gamma(a)+G_prime(a)-kappa,
```

where

```text
G_gamma(a)
 = 2 integral_0^infinity K(L)
       [1-cos(pi/(ceil(2a/L)+1))] dL,

G_prime(a)
 = sum_(L_n<2a) w_n
       [1-cos(pi/(ceil(2a/L_n)+1))].
```

No pole contribution was used in this lower bound, so it is deliberately
conservative.

A still simpler shell corollary is

```text
q_A,a(v)/||v||^2
 >= integral_a^(2a) K(L)dL
    +2 integral_(2a)^infinity K(L)dL
    +(1/2) sum_(a<L_n<2a) w_n
    -kappa.
```

This reduces large-cutoff positivity to an elementary lower bound for the
Chebyshev-weighted prime-power shell. A complete all-`a` proof has not yet
been supplied.

**Status:** candidate-T for the translation-chain and lower-bound lemmas;
G3 remains OPEN.

## R5. Exact cutoff restriction law

Let `0<a<b` and view `v in D_a` also as an element of `D_b`. For every newly
admitted prime-power delay

```text
2a <= L_n < 2b,
```

the supports of `E_a v` and `U_(L_n)E_a v` are disjoint. Translation preserves
norm, hence exactly

```text
||(V_b^-v)_n||^2 = w_n ||v||^2,
||(V_b^+v)_n||^2 = w_n ||v||^2.
```

Therefore

```text
q_A,b(v)
 = q_A,a(v)
   + [sum_(2a<=L_n<2b) w_n] ||v||^2,
```

while the Weil difference is unchanged because capacity and target acquire
exactly the same scalar increment.

This is the first genuine nested structure: old vectors become strictly safer
in the capacity norm as the cutoff grows, and every new prime channel enters as
a matched plus/minus diagonal pair before it begins to overlap at larger
support.

**Status:** candidate-T.

## R6. The more canonical fully signed factorization

R3 also exposes a structural choice which must not be hidden. The negative
archimedean mass `-kappa||v||^2` can be kept inside `q_A` (the frozen G3
question), or it can be placed on the negative side of the signed Pythagorean
pair, exactly as the scalar predecessor #355 did.

Define feature maps

```text
R_+(v) = (
  M_+(v), M_-(v),
  sqrt(K(t)) [E_a v-U_tE_a v]_(t>0),
  [sqrt(w_n/2)(E_a v-U_(L_n)E_a v)]_(L_n<2a)
),

R_-(v) = (
  sqrt(kappa) E_a v,
  [sqrt(w_n/2)(E_a v+U_(L_n)E_a v)]_(L_n<2a)
).
```

Then, directly from the source functional,

```text
Q_W^a(v)=||R_+(v)||^2-||R_-(v)||^2.
```

The positive side `||R_+||^2` is manifestly a Hilbert norm without any G3
assumption. This does **not** solve RH: Weil positivity is exactly the stronger
contraction inequality

```text
||R_-(v)|| <= ||R_+(v)||  for every a,v.
```

The canonical algebraic graph map

```text
T_a^0 : R_+(D_a) -> R_-(D_a),
T_a^0(R_+v)=R_-v
```

is independently defined once injectivity is checked. The real problem is no
longer existence of a formal `T_a`, but proving that this canonical graph map
extends contractively and coherently without importing Weil positivity.

This fully signed factorization is a **follow-up structural observation**. It
does not change the frozen G3 decision on `q_A` and is not used to claim G3.

## R7. Current verdict

```text
SURVIVES, sharpened.
```

The attack has not proved RH and has not closed G3. It has reduced the problem
to two concrete non-circular tasks:

1. decide the spectral gap of the explicit nonlocal Dirichlet capacity `q_A`;
2. analyze the canonical graph map from the fully positive feature carrier
   `R_+` to the signed target carrier `R_-`, seeking an intrinsic scattering /
   colligation factorization whose contractivity is not assumed.

The exact cutoff law in R5 is the required nesting datum for either route.
