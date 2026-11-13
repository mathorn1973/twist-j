# C-RH-MOBIUS-MEAN-CHANNEL-N

**Title:** RH arithmetic approximation, common signed Mobius compensation and current closure seam  
**Author:** A. M. Thorn  
**Date:** 2026-09-12  
**Status:** NON-CANONICAL public research note. No Canon authority.  
**Object lock:** #978  
**Branch:** `notes/c-rh-mobius-mean-channel-n`  
**Public baseline:** Public Canon v84. No Canon, Registry, Frontier, gate, evidence or claim status is changed.

## 0. Purpose and status

This note is the public continuation surface for the RH-directed arithmetic approximation program developed in incubation. It records the exact objects, the strongest analytic bounds reached so far, the proof routes already decided negatively, and the next mathematical target.

It is not a proof of RH. It does not claim unconditional fixed-epsilon `L^2` membership of the regularized arithmetic function. It does not claim the closure-strength `O(J)` bound for the original sharp family. It does not assume simple zeta zeros. It does not backdate a public preregistration to computations that were already executed before this note.

Status convention inside this note:

- **candidate-T:** analytic derivation exists, without independent public analytic review.
- **candidate-C:** exact or rigorous-interval computation on one x86_64 lane.
- **O:** open mathematical obligation.
- **F-route:** a precisely scoped proof route is ruled out. This is not a falsification of RH.

The adjacent digit-antiresonance and Walsh-transfer note in PR #966 is a useful neighboring seam, but it is not a premise of the results below.

## 1. Fixed arithmetic setting

For

\[
Q=2^j,\qquad j\ge1,\qquad n\ge1,
\]

set

\[
A_Q(n)=\mathbf 1_{n\equiv Q\pmod{2Q}},\qquad r_k(n)=n\bmod k,
\]

\[
E=\operatorname{span}_{\mathbf Q}\{r_k:k\ge2\},\qquad V=\overline E,
\]

with

\[
w_B(n)=4^{-\lfloor\log_2 n\rfloor},\qquad
\|x\|_B^2=\sum_{n\ge1}w_B(n)|x(n)|^2.
\]

The auxiliary norm is

\[
\|x\|_H^2=\sum_{n\ge1}\frac{|x(n)|^2}{n(n+1)},\qquad
\|x\|_H^2\le\|x\|_B^2\le4\|x\|_H^2.
\]

In code, dyadic exponents use `n.bit_length()-1`, never a floating-point logarithm.

Define

\[
t_Q=\mu*\Delta A_Q,\qquad
T_{Q,N}=\sum_{k\le N}\frac{t_Q(k)}k,\qquad
K_h=4Q2^h,
\]

\[
p_h=-\sum_{k<K_h}\frac{t_Q(k)}k r_k+T_{Q,K_h-1}r_{K_h},
\qquad e_h=A_Q-p_h,
\]

\[
S_{Q,J}=\sum_{h<J}e_h.
\]

The two channels are

\[
\mathcal Hx(n)=x(2n+1)-x(2n),\qquad
\mathcal Lx(n)=\frac{x(2n)+x(2n+1)}2,
\]

\[
D_{Q,J}=\mathcal H S_{Q,J},\qquad Y_{Q,J}=\mathcal L S_{Q,J}.
\]

The exact norm identity is

\[
\boxed{
\left\|A_Q-\frac1J\sum_{h<J}p_h\right\|_B^2
=\frac{\|Y_{Q,J}\|_B^2}{2J^2}
+\frac{\|D_{Q,J}\|_B^2}{8J^2}.
}
\tag{1}
\]

**candidate-T.** The difference channel of this original family has unconditional norm control with normalized quadratic error of order `J^-2` for fixed `Q`. The unresolved closure debt is the average channel.

On `n<Q^2`, common signed Mobius summation gives

\[
\boxed{
\left\|
\left(A_Q-\frac1J\sum_{h<J}p_h\right)\mathbf1_{n<Q^2}
\right\|_B^2
\le
\frac{4096j^4\min(J,j)^2}{Q^2J^2}.
}
\tag{2}
\]

This is a whole norm on the stated region, not a tail estimate.

## 2. Global overlaps and the balanced coefficient

Define

\[
\gamma_{Q,K}
=T_{Q,K-1}-\frac1K\sum_{k<K}t_Q(k),
\qquad
|\gamma_{Q,K}|<\frac5{4Q^2}.
\tag{3}
\]

For a source pair truncated by a cut, the correct upper endpoint is

\[
a=mQu,\qquad b=\min\{m(Qu+1),K\}.
\]

The global residue identity is

\[
\boxed{
p_{Q,K-1}(n)=
\sum_{\substack{u\text{ odd}\\mQu<K}}
\mu(m)
\left(
\left\lfloor\frac n{mQu}\right\rfloor-
\left\lfloor\frac n{\min(m(Qu+1),K)}\right\rfloor
\right)
-K\gamma_{Q,K}\left\lfloor\frac nK\right\rfloor.
}
\tag{4}
\]

The balancing coefficient is `K gamma`, not `K T`. This distinction is forced by split source pairs.

For `n=Qv+s`, `0<=s<Q`, all intervals with a common endpoint can be summed first. The global cell identity has the form

\[
\boxed{
S_{Q,J}(Qv+s)=c^\gamma_{Q,J}(v)+\sum_{t=1}^Q\Xi_{v,t}\mathbf1_{s<t}.
}
\tag{5}
\]

The exact cell mean is

\[
\boxed{
b_{Q,J}(v)=c^\gamma_{Q,J}(v)+\frac1Q\sum_{t=1}^Qt\Xi_{v,t}.}
\tag{6}
\]

The balancing term and pulse sum must remain joined until after squaring.

## 3. Whole-region bounds already obtained

### 3.1 Region beyond each cut square

Let

\[
O_{Q,J}(n)=\sum_{\substack{h<J\\K_h^2\le n}}e_h(n),
\qquad
\Theta_7(x)=\sum_{r\ge0}2^{-r}(x+r)^7.
\]

**candidate-T.** For all `Q=2^j`, `j>=1`, `J>=1`,

\[
\boxed{
\|O_{Q,J}\|_B^2
\le
\frac{128J}{Q^4}
+\frac{12}{Q}\Theta_7(j+3)
+\frac{288}{Q^2}
+\frac{80}{27Q^3}.
}
\tag{7}
\]

This is the complete infinite norm of the common sum `O`, not the sum of individual cut norms.

In the unbounded regime `J>=Theta_7(j+3)`, its cell means satisfy

\[
\boxed{
\|b^{\rm old}_{Q,J}\|_B^2\le173J,
\qquad
\|\mathcal L O_{Q,J}\|_B^2\le346J/Q.
}
\tag{8}
\]

### 3.2 A large inner part of the near region

Define

\[
U_{Q,J}(n)=
\sum_{\substack{h<J\\K_h\le n<K_h^2\le Q^2n}}e_h(n).
\]

Then

\[
\boxed{
\|U_{Q,J}\|_B^2
\le
\frac{48J}{Q^2}
+\frac{96(2j+3)}Q
+\frac{2j^2}{Q^2}
+28Q^2\Theta_7(2j+1).
}
\tag{9}
\]

The unresolved interval of one cut is reduced to

\[
\boxed{K_h\le n<K_h^2/Q^2.}
\tag{10}
\]

For `J>=Q^3 Theta_7(2j+1)`,

\[
\boxed{
\|b_U\|_B^2\le64J,
\qquad
\|\mathcal L U\|_B^2\le128J/Q.
}
\tag{11}
\]

## 4. Exact cancellation in the remaining core

Write

\[
s_Q(u)=\sum_{k\le u}t_Q(k),\qquad
T_Q(u)=\sum_{k\le u}\frac{t_Q(k)}k.
\]

Finite summation by parts gives

\[
\boxed{\gamma_{Q,K}=\sum_{u=1}^{K-1}\frac{s_Q(u)}{u(u+1)}.}
\tag{12}
\]

For one cut,

\[
\boxed{
e_K(n)=
\sum_{\ell=1}^{\lfloor n/K\rfloor}
 s_Q\!\left(\left\lfloor\frac n\ell\right\rfloor\right)
+K\left\lfloor\frac nK\right\rfloor\gamma_{Q,K}.
}
\tag{13}
\]

Let

\[
P(u)=\sum_{a=1}^uT_Q(a).
\]

The identities

\[
P(K-1)=K\gamma_{Q,K},\qquad
s_Q(m)=mT_Q(m)-P(m-1)
\]

remove the balancing term algebraically and give

\[
\boxed{
e_K(n)=\sum_{u=K}^{n}T_Q(u)[r_{u+1}(n)-r_u(n)].}
\tag{14}
\]

For any finite sequence `x_K,...,x_M`, with `P_n=sum_{u=K}^n x_u`,

\[
\boxed{
\sum_{n=K}^{M}\frac{|nx_n-P_{n-1}|^2}{n(n+1)}
=
\sum_{n=K}^{M}|x_n|^2
-\frac1{M+1}\left|\sum_{n=K}^{M}x_n\right|^2.
}
\tag{15}
\]

The negative square is a real mixed contribution. On the first quotient band it can remove at most one half of a generic `sum |T_Q|^2`, so this mechanism alone cannot yield arbitrary decay.

## 5. Exact global Hardy energy gluing

After partitioning the remaining core into dyadic blocks with fixed active cuts, exact boundary bookkeeping yields

\[
\boxed{
\|C_{Q,J}\|_H^2
=
\sum_X\sum_{X\le n<2X}|w_X(n)-\beta_X|^2
+\frac12\sum_XX|\beta_X-\alpha_X|^2.
}
\tag{16}
\]

All Mobius contributions are combined in `w_X` before the block mean is removed. New cuts enter with zero primitive boundary term. Departing cuts can contribute with either sign before the final positive form is assembled, so they cannot be discarded separately.

**F-route.** Dyadic geometry plus the available coarse pointwise envelopes does not imply the closure bound. A separate auxiliary arithmetic input can satisfy those coarse envelopes while the analogous common energy grows. The actual relation `t_Q=mu*Delta A_Q` must be used.

## 6. Unconditional Mobius decay controls a further complement

Using the external unconditional explicit Mertens bound listed below, partial summation gives for the actual sparse periodic source

\[
\boxed{
|T_Q(n)|\le
\frac{D_0}{Q(1+\lfloor\log_2(n/Q)\rfloor)^4}
}
\tag{17}
\]

with an explicit, deliberately crude `D_0`.

For every fixed integer `p>=1`, one may choose

\[
X_h^{(p)}\asymp
\max\left\{K_h,\frac{K_h^2}{Q^2(h+2)^{2p}}\right\}
\]

and obtain

\[
\boxed{
\left\|\sum_{h<J}e_h\mathbf1_{n\ge X_h^{(p)}}\right\|_B^2
\le C_{Q,p},
}
\tag{18}
\]

where `C_{Q,p}` is independent of `J`. The constants are not uniform in `p`, so `p -> infinity` is not permitted.

A separate complete-norm bound is

\[
\boxed{
\left\|\sum_{h<J}\xi_he_h\right\|_B^2
\le
\frac{N}{Q^2}\min\{800(J+1)^2,2^{96-\rho_J}\},
\quad
\rho_J=\left\lfloor\frac{\sqrt{J+1}}{160}\right\rfloor,
}
\tag{19}
\]

for arbitrary masks `|xi_h(n)|<=1`, where `N=K_{J-1}`. This is a real Mobius saving relative to the raw scale, but it is still far weaker than a closure-strength `CJ` mean-channel bound.

## 7. Walsh projection and the live high-bit seam

On a dyadic block `[L,2L)`, `L=2^b`, let `f_L(x)=R(L+x)`. If `S` denotes a Walsh bit support, exact `Q=2^j` cell averaging gives

\[
\boxed{
\left\|b_R\mathbf1_{[L/Q,2L/Q)}\right\|_B^2
=
\frac QL
\sum_{S\cap\{0,\ldots,j-1\}=\varnothing}
|\widehat f_L(S)|^2.
}
\tag{20}
\]

Thus survival depends on bit support, not only Walsh degree.

With

\[
r_b=
\max\left\{j,\left\lfloor\frac b2\right\rfloor
-6\left\lceil\log_2(b+1)\right\rceil\right\},
\]

the portion using at least one bit in `{j,...,r_b-1}` has total energy

\[
\boxed{\mathcal E_{\rm mid}\le\frac{Q}{4(j+2)}.}
\tag{21}
\]

The remaining high-bit energy `E_top` is supported only on `{r_b,...,b-1}`.

**F-route.** Even after exact odd/even Mobius pairing, replacing all source Walsh coefficients by one common absolute bound and then using absolute matrix row sums is too expensive. The matrix cost itself grows too fast. Any successful Walsh argument must preserve relations among source coefficients inside the joined quadratic form.

## 8. Strength guard for the original all-large-J family

Let

\[
U_J=\|S_{Q,J}\|_B,
\qquad
E_h=\sum_{n=K_h}^{2K_h-1}|T_Q(n)|^2.
\]

Since `e_h=S_{Q,h+1}-S_{Q,h}` and the first-band Hardy identity is exact,

\[
\boxed{\sqrt{E_h}\le\sqrt2\,(U_{h+1}+U_h).}
\tag{22}
\]

Define the paired source Dirichlet function

\[
\mathscr A_Q(s)=
\sum_{u\text{ odd}}[(Qu)^{-s}-(Qu+1)^{-s}].
\]

Then for `Re s>1`,

\[
\boxed{
\int_1^\infty T_Q(x)x^{-s}\,dx
=
\frac{\mathscr A_Q(s)}{(s-1)\zeta(s)}.
}
\tag{23}
\]

Moreover, for `sigma=Re s>=1/2`,

\[
\boxed{
Q\ge4|s+1|
\Longrightarrow
|\mathscr A_Q(s)|\ge\frac{|s|}{3Q^{\sigma+1}}>0.
}
\tag{24}
\]

**candidate-T guard.** If for an unbounded set of dyadic `Q` the original uniform sharp family converges for all sufficiently large `J`, then the Mellin quotient forces RH and also excludes multiple critical zeros. In particular, an all-large-`J` `O(J)` bound is stronger than a bare RH location statement.

This is not an assumption of simple zeros and not a proof that a multiple zero exists. It is a warning about the strength of that closure target. A diagonal schedule `J=J(Q)` sufficient for infinitely many `Q` remains logically distinct.

## 9. Symmetric damping branch and finite-certificate bridge

A comparison family is

\[
q_\varepsilon(n)=
-\sum_{a\ge2}\frac{\mu(a)}{a^{1+\varepsilon}}r_a(n),
\qquad 0<\varepsilon\le\frac14.
\]

Let

\[
h_\varepsilon(k)=
\sum_{d\mid k}\frac{\mu(d)}{d^\varepsilon}
=\prod_{p\mid k}(1-p^{-\varepsilon}),
\]

\[
H_\varepsilon(n)=\sum_{k\le n}h_\varepsilon(k),
\qquad
c_\varepsilon=\frac1{\zeta(1+\varepsilon)}.
\]

The exact arithmetic identity is

\[
\boxed{q_\varepsilon(n)=H_\varepsilon(n)-c_\varepsilon n.}
\tag{25}
\]

Hence

\[
\boxed{
\|a_1-q_\varepsilon\|_H^2
=
\sum_{n\ge1}
\frac{(1+c_\varepsilon n-H_\varepsilon(n))^2}{n(n+1)}.
}
\tag{26}
\]

Under RH, the symmetrically shifted Mellin calculation gives a joined norm of order `epsilon`, with no separate simple-zero premise. This conditional branch is retained only as structural evidence for the form of the needed cancellation.

The following transfer is unconditional. For a finite rational `q in E`, set

\[
\delta_q^2=\|a_1-q\|_H^2.
\]

For integer `U>=1`, define

\[
\widetilde p_{Q,U}[q](n)=
\sum_{r=0}^{U-1}
\left[
q\!\left(\left\lfloor\frac n{Q(2r+1)}\right\rfloor\right)
-q\!\left(\left\lfloor\frac n{Q(2r+1)+1}\right\rfloor\right)
\right].
\tag{27}
\]

Then `ptilde` is a finite rational element of `E` and

\[
\boxed{
\|A_Q-\widetilde p_{Q,U}[q]\|_B^2
\le
\frac2{Q^2U}+\frac{64U}{Q}\delta_q^2.
}
\tag{28}
\]

For the retained third-layer test,

\[
\boxed{
Q=8,\quad U=64,\quad
\delta_q^2\le\frac9{2^{23}}
\Longrightarrow
\|A_8-\widetilde p_{8,64}[q]\|_B^2\le\frac{17}{16384}.
}
\tag{29}
\]

No such finite certificate is claimed in this note.

## 10. Fixed-epsilon hyperbola seam

Use reciprocal coordinates

\[
F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor).
\]

With a dyadic hyperbola cut `D(x)`, exact finite summation gives

\[
\boxed{F_\varepsilon=Z_\varepsilon+B_\varepsilon+\mathscr Q_\varepsilon.}
\tag{30}
\]

The first two pieces have complete unconditional weighted norm bounds

\[
\boxed{\|Z_\varepsilon\|_\varepsilon^2\le\frac{32}{3},\qquad
\|B_\varepsilon\|_\varepsilon^2\le11664,}
\tag{31}
\]

where

\[
\|f\|_\varepsilon^2=\int_1^\infty x^{\varepsilon-2}|f(x)|^2dx.
\]

The remaining joined term has the exact atom expansion

\[
\boxed{
\mathscr Q_\varepsilon(x)
=
\sum_{d\ge1}\mu(d)d^{-\varepsilon}
\left\{\frac{x}{\max(d,D(x))}\right\}.
}
\tag{32}
\]

Its positive diagonal is finite for fixed positive `epsilon`, but the unrestricted sum of absolute off-diagonal pair contributions diverges even for the actual Mobius input. Signed summation is mandatory.

On a simultaneous growing `(epsilon,Y)` region, the signed off-diagonal cancels the logarithmically growing diagonal:

\[
\boxed{
\mathcal O_\varepsilon(Y)=-c_*\log Y+O(1),
\qquad
c_*=\frac{\log(2\pi)-\gamma}{\zeta(2)}.
}
\tag{33}
\]

The proved region grows without bound as `epsilon -> 0`, but remains finite for each fixed positive `epsilon`.

## 11. Fixed positive epsilon: exact obstruction and whole-domain moments

For the joined function,

\[
\boxed{
\int_1^\infty F_\varepsilon(x)x^{-s-1}dx
=
\frac{c_\varepsilon}{s-1}
-\frac{\zeta(s)}{s\zeta(s+\varepsilon)},
\qquad \Re s>1,
}
\tag{34}
\]

followed by meromorphic continuation.

**F-route.** Every finite nonconstant Taylor truncation of this regularization at `epsilon=0`, and its exact remainder, have infinite separate weighted square norms. Therefore fixed-epsilon finiteness cannot be proved by bounding finitely many Taylor pieces and the remainder separately.

This does not prove that the fully resummed joined function has infinite norm.

Set `delta=epsilon/2` and define the actual whole-domain moments

\[
m_k(\varepsilon)=
\frac{c_\varepsilon}{k+1-\delta}
-
\frac{\zeta(k+2-\delta)}{(k+2-\delta)\zeta(k+2+\delta)}.
\tag{35}
\]

All zeta arguments are real and greater than one.

Let

\[
R_n(t)=
\sum_{k=0}^n
(-1)^{n-k}\binom nk\binom{n+k+2}{k+2}t^k,
\]

and

\[
a_n(\varepsilon)=\sum_{k=0}^n b_{n,k}m_k(\varepsilon).
\]

The extended exact identity is

\[
\boxed{
\|g_\varepsilon\|_2^2
=
\frac{c_\varepsilon^2}{1+\varepsilon}
+
\sum_{n\ge0}(2n+3)|a_n(\varepsilon)|^2,
}
\tag{36}
\]

where `+infinity` is allowed. Thus fixed-epsilon finiteness is exactly equivalent to a uniform bound on the finite partial sums

\[
L_N(\varepsilon)=
\frac{c_\varepsilon^2}{1+\varepsilon}
+
\sum_{n=0}^{N}(2n+3)|a_n(\varepsilon)|^2.
\tag{37}
\]

## 12. Current endpoint: proved upper bound for every finite moment sum

Let `A=N+2`.

**candidate-T.** For every `0<epsilon<=1/4` and finite `N`,

\[
\boxed{
L_N(\varepsilon)
\le
\frac{c_\varepsilon^2}{1+\varepsilon}
+
\frac{A^{2-2\varepsilon}}{\varepsilon^2}
\min\left\{
25,
2^{16}\exp\left(-\frac{\sqrt{2\log A}}{20}\right)
\right\}.
}
\tag{38}
\]

The first branch is elementary. The second uses the declared external unconditional Mertens input.

The proof keeps the finite quadratic form joined:

\[
\boxed{
L_N-\frac{c_\varepsilon^2}{1+\varepsilon}
=
\sup_{\substack{v\in V_N\\\|v\|_2=1}}
\left|
\int_0^1g_\varepsilon(t)\overline{v(t)}dt
\right|^2,
\qquad
V_N=\operatorname{span}\{t,\ldots,t^{N+1}\}.
}
\tag{39}
\]

No individual Jacobi coefficient is replaced by the absolute sum of its binomial terms.

For fixed positive `epsilon`, however, the right side of (38) still grows with `N`. Therefore

\[
\boxed{\sup_NL_N(\varepsilon)<\infty}
\tag{40}
\]

remains open.

The precise loss is the replacement of the joined arithmetic function by a pointwise envelope inside (39). A degree-`N+1` normalized polynomial can concentrate near `t` of order `(N+2)^-2`, and the present envelope leaves a positive power of `N`.

## 13. No-go ledger

The following proof routes are decided narrowly and should not be repeated without a new ingredient.

1. **Absolute Mobius pair summation:** the unrestricted absolute Q23 off-diagonal pair series diverges for the actual Mobius input.
2. **Degree-only Walsh control:** degree does not determine survival under `Q`-cell averaging; bit support does.
3. **One common Walsh coefficient bound plus absolute row sums:** the balanced transfer matrix cost grows too quickly, even after exact odd/even pairing.
4. **Scalar Mertens envelope alone:** an auxiliary input can satisfy the same coarse envelope while its analogous quadratic energy diverges.
5. **Finite Taylor truncation in epsilon:** each nonconstant finite truncation and its exact remainder have infinite separate weighted norms.
6. **Pointwise decay alone in the moment supremum:** the current all-`N` bound retains a positive power of `N`; changing only constants or the same root-log factor cannot make it uniform.
7. **All-large-J sharp-family guard:** uniform convergence of the original sharp family for unbounded `Q` is strong enough to force simple critical zeros as well as RH. Do not silently treat it as only another RH-equivalent estimate.

None of these statements falsifies RH.

## 14. Next proof target

The primary continuation target is now explicit.

For one fixed rational

\[
0<\varepsilon\le\frac14,
\]

prove directly from the joined arithmetic moments that

\[
\boxed{
\sup_{N\ge0}\sum_{n=0}^N(2n+3)|a_n(\varepsilon)|^2<\infty.
}
\tag{41}
\]

The proof must preserve the complete sum in (39), or an equivalent Gram/Hankel form, until after the arithmetic cancellation is assembled.

Plausible genuinely new ingredients include:

- a bound on the joint Jacobi transform of the zeta-ratio moment sequence, rather than on individual moments;
- an operator estimate for the finite Hilbert/Hankel inverse quadratic form evaluated on the actual completely monotone zeta-ratio input;
- dyadic or multiplicative orthogonality acting before endpoint concentration in (39);
- a signed Walsh or carry-defect estimate transported through the exact balanced kernel instead of absolute row sums.

A secondary independent target remains the finite certificate condition (29). Such a certificate would advance the original RH approximation program without first proving convergence of the full sharp family.

If returning to the original sharp cuts, prefer a controlled diagonal schedule `J=J(Q)` sufficient for infinitely many `Q` unless a proof genuinely supports all sufficiently large `J`.

## 15. External inputs

External analytic results used in the incubation chain are not re-proved here:

1. E. S. Lee and N. Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*, arXiv:2208.06141. Used through weakened unconditional Mertens bounds.
2. A. Fiori, H. Kadiri, J. Swidinsky, *Sharper bounds for the Chebyshev function psi(x)*, arXiv:2204.02588. Used in the finite prime-window extension.
3. J.-F. Burnol, arXiv:math/0202166. Used to delimit symmetric regularization and the distinction between formal Mellin boundary values and actual `L^2` membership.
4. J. Bourgain, arXiv:1109.2784. Background for uniform Mobius-Walsh correlations; insufficient by itself for the balanced transfer matrix.
5. The Baker-Harman `3/4+epsilon` Fourier statement is GRH-conditional and is not used in any unconditional conclusion here.

## 16. Minimal reproduction of the current finite-moment endpoint

This branch adds:

- `notes/C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py`
- `notes/C-RH-MOBIUS-MEAN-CHANNEL-N_EXPECTED.txt`

Run

```bash
python notes/C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py
```

The verifier uses only Python standard-library integer arithmetic, `Fraction`, integer root enclosures, and outward rational intervals. It checks:

- exact finite signed hyperbola identities;
- exact Legendre/Jacobi polynomial identities used in the moment functional;
- exact power-model Jacobi coefficients;
- rigorous real-zeta Euler-Maclaurin enclosures at the actual moment arguments;
- actual moment partial energies through degree 32 for `epsilon=1/4` and `epsilon=1/16`;
- the proved finite-`N` upper bound against those enclosed energies.

It does not verify the external Mertens theorem, RH, zeta-zero properties, fixed-epsilon full norm finiteness, or the missing uniform-in-`N` upper bound.

Local byte-for-byte run before publication:

```text
PASS: 5566 exact/rigorous-enclosure checks; 24 groups
```

Frozen source hashes before publication:

```text
fdb8d53015a4451f3b04963933c8bb1c931154f2e081aeedce9a882468623e4c  C-RH-MOBIUS-MEAN-CHANNEL-N_VERIFY.py
07d01b3d42de2e5cc8e8db60f7a82d0777761333f6ab8a20952d48d426fbda6f  C-RH-MOBIUS-MEAN-CHANNEL-N_EXPECTED.txt
```

This is a public NON-CANONICAL reproduction aid, not a formal probe gate. No public preregistration is backdated. No independent analytic review or second architecture is claimed for the new mathematics.

## 17. Handoff

Continue from (41), not from another equivalent formulation of RH and not from another pointwise Mertens majorant. The next useful result is a uniform bound on the joined Jacobi/Hankel quadratic form, or an exact breaker showing that this fixed-epsilon regularization cannot have finite norm at the selected epsilon. Preserve signed arithmetic cancellation until after the common quadratic form is assembled.
