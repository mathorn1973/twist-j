# PROMO C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS: NON-CANONICAL PROMOTION PACKAGE
AUTHORITY: none
ISSUE: #357
PROMOTION: not executed
```

## 1. Results that survived

### A. Delayed prime powers form an exact signed Pythagorean pair

**candidate-T.** On `D_a=C_c^infty(-a,a)`, with zero extension and
`w_n=Lambda(n)/sqrt(n)`, the exact prime part is

```text
q_P,a=||V_a^-||^2-||V_a^+||^2,
```

where `V^-` and `V+` are the antisymmetric and symmetric delayed channels.
Every isolated delayed block has both signs, so no local basis change can make
one prime leg positive.

### B. The archimedean remainder has an exact Dirichlet-energy form

**candidate-T.** Directly from Suzuki's Weil functional,

```text
q_gamma(v)
 = integral_0^infinity K(t)||E_av-U_tE_av||^2 dt
   - kappa||v||^2,

K(t)=e^(-t/2)/(1-e^(-2t)),
kappa=log(pi)-psi(1/4).
```

The pole term is the positive rank-two form

```text
|M_+(v)|^2+|M_-(v)|^2.
```

Hence the frozen capacity `q_A` is one explicit nonlocal Dirichlet energy
minus a single scalar mass.

### C. Large-cutoff G3 is closed unconditionally

**candidate-T, external exact Chebyshev input.** Using the translation-chain
lower bound and the unconditional explicit estimates

```text
psi(x)>=(9/10)x for x>=41,
psi(x)<=(6/5)x for x>=0,
```

one gets

```text
q_A,a(v)>0
```

for every nonzero `v` and every

```text
a>=log 41.
```

No RH, zero data, or Weil positivity is used. The strict endpoint in the
frozen cutoff is handled explicitly by subtracting at most `2 log x` before
applying the shell bound.

The unresolved G3 domain is the compact interval

```text
0<a<log 41.
```

### D. Cutoff nesting is exact

**candidate-T.** If `0<a<b` and `v in D_a`, each newly admitted prime-power
channel has disjoint translated support and adds exactly

```text
w_n||v||^2
```

to both signed sides. Thus old vectors gain a matched diagonal block as the
cutoff grows.

### E. Completing a prime through its full Euler tower is canonical

**candidate-T.** For an included prime `p`, adding all powers `p^k`, including
those beyond the support cutoff, changes neither signed Weil difference nor
any old correlation: beyond support the plus/minus norms are equal.

With `r=p^(-1/2)` the completed local positive symbol is

```text
A_p(theta)=c_p|1-b_r(e^(i theta))|^2,

b_r(z)=(z-r)/(1-rz),
c_p=(log p)r/[2(1-r^2)].
```

The symmetric symbol is

```text
B_p(theta)=c_p|1+b_r(e^(i theta))|^2+d_p,
d_p=2(log p)r^2/(1-r^2).
```

Since `|b_r|=1`, the two local quadratures obey

```text
|1-b_r|^2+|1+b_r|^2=4.
```

### F. The local phase is the standard L-factor scattering ratio

**candidate-T.** On the critical line,

```text
rho_p(s)=gamma_p(s)/gamma_p(1-s)=z/b_r(z),
z=exp(i xi log p),
```

and

```text
d/dxi arg rho_p(1/2+i xi)
```

is exactly the completed local prime Weil symbol. At infinity,

```text
d/dxi arg rho_inf(1/2+i xi)
 = Re psi(1/4+i xi/2)-log pi,
```

which is exactly the gamma multiplier. Finite and infinite places are
therefore one scattering-phase-derivative mechanism.

### G. Every finite prime place has a lossless two-state colligation

**candidate-T.** The Blaschke phase is the transfer function of

```text
U_r=[[r,sqrt(1-r^2)],
     [sqrt(1-r^2),-r]],
U_r^T U_r=I.
```

This is a genuine local contraction/unitarity input independent of RH.

### H. The square-root cover is exact at every place

**candidate-T.** With `q=p^(-1/4)` and `z=w^2`,

```text
b_(q^2)(w^2)=b_q(w)b_(-q)(w).
```

Equivalently

```text
1-p^(-s)=[1-p^(-s/2)][1+p^(-s/2)].
```

The archimedean analogue is Legendre duplication

```text
Gamma_R(2u)=2^(u-1)Gamma_R(u)Gamma_R(u+1),
s=2u.
```

Thus the same half-argument cover splits finite Euler factors into `+/-`
parity factors and the infinite factor into even/odd real gamma factors. The
critical line `Re(s)=1/2` becomes `Re(u)=1/4`.

This gives a global exact reason that quarter-power modulus and half phase
appear together. `zeta_8=sqrt(i)` is one special fiber value when the base
phase equals `i`; no fixed eighth root is globally selected.

## 2. Falsifications / boundaries

1. **F local positivity:** one prime leg is genuinely indefinite. No local
   `SU(2)` or other invertible change of basis can cure it.
2. **F pure-archimedean positive Schur shortcut:** a positive lower Schur block
   contributes only a negative semidefinite correction. The positive prime
   channel must live in the capacity or the auxiliary geometry must be
   indefinite.
3. **F automatic Hardy shortcut:** a unimodular scattering multiplier has a
   contractive Hardy compression, but the Weil functional is a signed relative
   projection / quantized-differential quantity. Automatic Toeplitz
   contractivity does not imply Weil positivity.
4. **Boundary quasi-inner vs inner:** existing Connes--Consani semilocal
   products are quasi-inner and their Sonin spaces form an inductive system.
   This supplies the right carrier category, not the missing projection order.
5. G3 remains open on `0<a<log 41`. No finite numerical scan is promoted.
6. G6 nested contraction is not closed.

## 3. Sharpened RH wall

The fully signed source-side factorization may be written

```text
Q_W^a(v)=||R_+(v)||^2-||R_-(v)||^2.
```

The canonical graph map

```text
T_a^0(R_+v)=R_-v
```

is algebraically defined once injectivity is fixed. The hard statement is its
contractive, coherent extension. That statement may be recast as an exact
relative-subspace / projection-order problem in a semilocal scattering model
only after an intertwining theorem is proved.

The best next theorem target is therefore:

```text
Construct an exact intertwiner between

  (i) the frozen delayed-amplitude feature pair R_+,R_-, and
  (ii) the semilocal Hardy/Sonin projection pair generated by
       rho_inf * product_(p in S) rho_p,

compatible with the full Euler-local towers and cutoff inclusions.
```

If the intertwiner exists, the residual RH wall becomes a precise subspace
inclusion / innerness-strengthening problem. If it does not, the present
scattering route is falsified without touching RH itself.

## 4. Promotion recommendation

Do not promote any RH claim. A later public theorem probe could reasonably
separate the exact algebraic lemmas (delayed factor, local Blaschke/Euler
completion, scattering derivative, double-cover parity factorization) from the
open positivity/contraction problem. Such promotion requires independent audit
and a fresh public claim lock.
