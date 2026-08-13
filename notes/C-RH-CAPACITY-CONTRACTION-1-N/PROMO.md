# CORRECTED PROMO C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS: NON-CANONICAL REVIEW PACKAGE
AUTHORITY: none
ISSUE: #357
PR: #359
PROMOTION: not executed
```

`CORRECTION.md` is part of this package. It withdraws every conclusion that
used the wrong positive factorization of the pole term.

## 1. Exact results that survive

### A. Finite prime powers form an exact signed pair

**candidate-T.** On `D_a=C_c^infty(-a,a)`,

```text
q_P,a=||V_a^-||^2-||V_a^+||^2.
```

Each isolated delayed block has both signs. The cutoff restriction law also
survives: a newly admitted disjoint delay adds exactly `w_n||v||^2` to each
side.

### B. The gamma term is a jump energy minus mass

**candidate-T.** Directly from Suzuki's displayed Weil functional,

```text
q_gamma(v)
 = integral_0^infinity K(t)||E_av-U_tE_av||^2 dt
   -kappa||v||^2,

K(t)=e^(-t/2)/(1-e^(-2t)),
kappa=log(pi)-psi_dig(1/4).
```

The separate pole term is **not** positive. It is

```text
2 Re[M_+conj(M_-)]
 =(1/2)|M_++M_-|^2-(1/2)|M_+-M_-|^2.
```

Thus the corrected `q_A,a` is an explicit signed coercivity problem, not a
positive Dirichlet energy minus one scalar mass.

### C. Translation and strict-shell lemmas

**candidate-T.** The path-chain estimate gives

```text
||v-U_Lv||^2
 >=2[1-cos(pi/(ceil(2a/L)+1))]||v||^2.
```

For `a<L<2a`, the right side is `||v||^2`. Together with unconditional
Chebyshev bounds, the strict shell `x<n<x^2`, `x=e^a>=41`, contributes at
least

```text
[(9/20)x-3/5-(log x)/x]||v||^2
```

to `q_A,a`. The earlier large-cutoff theorem does not follow because the pole
term can be negative. G3 remains `UNDECIDED` for all `a>0`.

### D. Euler-normalized balanced stabilization

**candidate-T for the equality; working choice for the geometry.** For an
included prime `p`, adding all powers beyond the support cutoff adds equal
norm to the two signed channels and leaves `Q_W` unchanged. This is a natural
Euler-normalized balanced stabilization. It is not forced uniquely by the
signed form and it changes `q_A`, both auxiliary norms, and graph geometry.

At the scalar Fourier-symbol level, with `r=p^(-1/2)`,

```text
A_p(theta)=c_p|1-b_r(e^(i theta))|^2,
B_p(theta)=c_p|1+b_r(e^(i theta))|^2+d_p,

b_r(z)=(z-r)/(1-rz),
c_p=(log p)r/[2(1-r^2)],
d_p=2(log p)r^2/(1-r^2).
```

The exact identity `|1-b_r|^2+|1+b_r|^2=4` holds on the circle. These norm
symbols do not yet supply a linear tower-to-state intertwiner.

### E. Local Weil symbols are scattering-phase derivatives

**candidate-T.** On the critical line,

```text
rho_p(s)=gamma_p(s)/gamma_p(1-s)=z/b_r(z),
d/dxi arg rho_p=(log p)[1-P_r(xi log p)],
```

and

```text
d/dxi arg rho_inf
 =Re psi_dig(1/4+i xi/2)-log pi.
```

The finite and infinite non-pole symbols are local pieces of one
scattering-phase derivative. The bare factor `z` contributes `log p`; it is
part of the equality.

### F. The compensating Blaschke factor has a lossless realization

**candidate-T.** The real orthogonal `2x2` colligation with one-dimensional
state

```text
U_r=[[r,sqrt(1-r^2)],
     [sqrt(1-r^2),-r]]
```

has transfer function `b_r`. It does **not** directly realize `rho_p=z/b_r`,
which has a pole at `z=r` in this orientation. Passing to the semilocal
scattering multiplier still requires inversion, the bare phase, and a frozen
Hardy orientation.

### G. The two-sheeted square-root identities are exact locally

**candidate-T.** With `q=p^(-1/4)`, `z=w^2`, and `s=2u`,

```text
b_(q^2)(w^2)=b_q(w)b_(-q)(w),
1-p^(-2u)=[1-p^(-u)][1+p^(-u)],
Gamma_R(2u)=2^(u-1)Gamma_R(u)Gamma_R(u+1).
```

The critical line becomes `Re(u)=1/4`. The two Blaschke factors are exchanged
by the deck involution, up to sign; they are not separately even and odd
functions. The gamma scattering ratio also carries the pure boundary phase
`2^(2u-1/2)`, whose phase derivative contributes `log 2`.

These are local or finite-semilocal identities. They do not define convergent
global Euler products of both half factors on `Re(u)=1/4`.

## 2. Corrected fully signed carrier

The source-side form retains the exact factorization

```text
Q_W^a(v)=||R_+(v)||^2-||R_-(v)||^2,
```

provided the pole components are

```text
R_+^pole(v)=[M_+(v)+M_-(v)]/sqrt(2),
R_-^pole(v)=[M_+(v)-M_-(v)]/sqrt(2).
```

Together with the continuous jump, mass, and prime delayed channels, these
give exact Hilbert feature maps. Their contractive coherent graph map is not
proved.

## 3. Falsifications and live boundaries

1. **F positive pole shortcut:** the pole form is indefinite.
2. **F supplied large-cutoff proof:** the valid prime shell cannot discard the
   negative pole term; `a>=log 41` is not closed by that proof.
3. **F local positivity:** one prime leg and the complete finite-prime sector
   are indefinite in the frozen source-side splitting.
4. **F pure-archimedean positive Schur shortcut:** a positive lower Schur
   block contributes a negative semidefinite correction.
5. **F automatic Hardy shortcut:** Toeplitz contractivity of a unimodular
   multiplier does not imply the signed relative-projection inequality.
6. **Boundary Hardy orientation:** for
   `W=Tr(M_f[P-u*Pu])`, positivity needs the corresponding co-inner order;
   an ordinary inner orientation gives the opposite order. Trace-class
   hypotheses must be frozen.
7. **Boundary Sonin system:** Connes--Consani's comparison maps for adding
   places are multiplier maps, not plain inclusions. Their quasi-inner result
   supplies a candidate comparison category, not the missing intertwiner.
8. **Boundary zeta_8:** a coordinate `w^2=i` has two sheets. The normalized
   Euler half-variable has the inverse orientation and yields a square root of
   `-i`; neither choice is privileged by RH.

## 4. Ordered next step

The proposed exact comparison with the semilocal Hardy/Sonin projection pair
is a useful falsification target. Under the frozen breaker order in
`PREREG.md`, however, G6 opens only after G3-G5 survive. The immediate #357
task is therefore a corrected joint coercivity analysis for G3.

An intertwiner study may proceed earlier only under an explicit separate lock
that calls it an independent carrier-comparison/no-go test and does not claim
G6 or consume positivity.

## 5. Promotion recommendation

Do not promote any RH or G3 claim. A later public theorem probe may separate
the exact algebraic identities from the open capacity and intertwining
problems, after independent audit and a fresh claim lock.
