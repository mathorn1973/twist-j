# Quantitative finite approximation of the original capture packet and joint event

**PUBLIC ANALYTICAL PROPOSAL. NON-CANONICAL / L1.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Companion to [#1816](https://github.com/mathorn1973/twist-j/issues/1816).
The original-operator audit and source custody are `PROOF.md` and
`SOURCES.md` in this directory. This note's analytical bounds are
distinct from the finite polynomial gates of the companion probe.

This is a reconciliation contribution to the continuing root-owned audit of the exact packet whose absolute probability was certified in PR #1815 / `P-BOUND-PAIR-ABSOLUTE-CAPTURE-1`. It is not a new finite-interface reservation, probe, run, or closure claim. No scientific executable, import, CAS, numerical trial, or public mutation was used for this draft.

The original law, source normalization, all 26 carrier labels, the receiver at `z=100`, and arbitrary old-memory/reference input are retained. Finite filters below are supplied mathematical operations; a native autonomous implementation is not inferred.

## 0. Existing ownership and the precise additional question

The following public issue/PR records were read on 2026-10-28 and identify the adjacent lanes:

| Existing lane | What this draft must not replace or inherit without its hypotheses |
|---|---|
| [#1741](https://github.com/mathorn1973/twist-j/issues/1741), finite interface | Whole-state finite-interface and locality-cone work already has an owner. This draft supplies quantitative approximation bounds for the unchanged #1815 packet, for reconciliation with that lane. |
| [PR #1744](https://github.com/mathorn1973/twist-j/pull/1744), head `af8a4991cfbb101e7b2992fc4ac56ee5bea9d00f` | The stated all-later-time retention bound concerns its declared smooth product family. Its corrected R3 explicitly does not supply the same estimate for the actual normalized selected capture component. |
| [#1745 / PR #1746](https://github.com/mathorn1973/twist-j/pull/1746), head `01acc42b78f75095587765e9a5b91ee70dc28f37` | Its compact source and forward-only finite readout are different from the original packet and `Q_win`. Its accepted weights cannot be reassigned to this packet. Its full-history instrument/resource distinctions remain relevant. |
| [#1749 / PR #1751](https://github.com/mathorn1973/twist-j/pull/1751), head `e2a37296c6a4c6fde4c4a28e8cbcd1af48331cb9` | Its local digital simulator is an added apparatus. It does not identify the particle-coordinate native dynamics or automatically compile the new filters below under the same resource account. |

These are scope comparisons with the read-back issue/PR records, not independent acceptance of their theorems.

The useful conclusion available now is stronger than qualitative density of finite-support vectors: explicit finite source and detector degrees give explicit errors on this particular packet. The remaining quantitative scattering-time estimate is isolated in section 6.

## 1. Exact source, event, and certified target probability

Use the source notation of `PROOF_PACKET_CERTIFICATE.md` section 2 and CP-11 of `PROOF_CAPTURE_PROFILE.md`:

\[
\delta=h=\delta_K=10^{-3},\quad
I_P=[-\delta,\delta],\quad I_E=[E_*-h,E_*+h],\quad E_*=8\pi/5,
\]

\[
a_0=\delta_{R=0,r=0}\,iB,\qquad U_1=e^{-i\beta}W,
\qquad a(E)=[2h\rho_{\rm in}(E)]^{-1/2}.
\]

Let `T_R` be the unit center translation, with spectral variable `P`. The odd spectral measure is purely absolutely continuous on the required source rectangle. Consequently the original source can be written exactly as

\[
\psi=a(H_1)\mathbf1_{I_E}(H_1)\mathbf1_{I_P}(P)a_0,
\qquad \|\psi\|=1.
\tag{1}
\]

The relative-ac projection in the inherited definition is redundant on this displayed vector after the energy restriction, not on arbitrary states. Functional calculus on the contact vector retains both continuum roots and their original coherent direction.

Tensor (1) with `|y=0,t1>` and an arbitrary normalized memory/reference vector

\[
\Phi=\sum_{j=0}^{25}|d_j\rangle|\phi_j\rangle,
\qquad \sum_j\|\phi_j\|^2=1.
\]

Call this full reference input `Psi`. Put `Xi=S_rec Psi`. The exact event is the projector from section 5 of `PROOF_CURRENT_RECORD_INTERFACE.md`:

\[
Q=\mathbf1_{I_K}(K)\mathbf1_{|P|\le1/100}
\mathbf1_{I_E}(\Omega_b(P)+\beta+\varepsilon(k))
\Pi_b(P)\otimes P_+(k)\mathbf1_{\varepsilon'(k)>0}
\otimes I_{\rm carrier\ label}\otimes |d_1\rangle\langle d_1|
\otimes I_{\rm ref}.
\tag{2}
\]

Thus binding, the positive right-moving pulse, both spectral windows, and the receiver record are all part of the target. No carrier label is discarded. The receiver conjugacy transfers the entire old-memory/reference vector coherently into those labels.

The existing absolute certificate, with public input pin `173ca05aab8fac006a5e4d54d640f8a9eff35d18` and completed result at `32306016908c0097650277aa416fc0152b2f81a4`, gives

\[
L=\frac{293166031669590845829}{2^{96}}
\le\|Q\Xi\|^2\le
\frac{352434475368785347398}{2^{96}}=U.
\tag{3}
\]

In particular `L>(6/100000)^2` and `U<(7/100000)^2`. The exact integers, not a midpoint estimate, are the target of the approximation below.

## 2. Why finite support cannot preserve the sharp incoming momentum window exactly

If a nonzero state has finite support in `R`, its `P` Fourier transform is a finite Hilbert-valued Laurent polynomial. If that transform vanished on the open complement of the proper arc `I_P`, every scalar component would vanish identically by the polynomial identity theorem. The state would be zero.

Therefore a nonzero finite source cannot simultaneously retain exact sharp `P` support. The construction below controls the leakage in norm. It does not claim exact membership in `P_in` or exact zero unwanted relative-bound weight for the finite approximation.

Likewise, no uniform approximation of a sharp continuum spectral step by continuous trigonometric polynomials is asserted. The estimates below are state-specific, except for explicitly stated estimates on a spectrally gapped, momentum-restricted block.

## 3. An explicit finite source with an error bound

### 3.1 Two elementary polynomial kernels

For an integer `M>=2`, let the Fejer kernel and its convolution be

\[
F_M(\theta)=\frac1M\left|\sum_{j=0}^{M-1}e^{ij\theta}\right|^2,
\qquad \mathcal F_M f=F_M*f,
\]

where convolution uses `dtheta/(2pi)`. It is positive, normalized, and has degree `M-1`. If `f=1_I` for a circular interval, then `0<=F_M*f<=1` and

\[
\|\mathcal F_M\mathbf1_I-\mathbf1_I\|_{L^2(d\theta/2\pi)}^2\le\frac1M.
\tag{4}
\]

Indeed the nonzero Fourier coefficients of the step have absolute value at most `1/(pi |j|)`. The error from `1<=|j|<M` is at most `2/(pi^2 M)`; the tail is at most `3/(pi^2 M)`. Their sum is less than `1/M` for `M>=2`.

For `n>=1`, use the positive Jackson kernel

\[
J_n(\theta)=\frac{3}{n(2n^2+1)}
\left(\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right)^4.
\]

Its normalized integral is one and its degree is `2(n-1)`. The normalization follows by squaring the triangular Fourier coefficients of the Fejer numerator. The bounds

\[
\left|\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right|
\le\min(n,\pi/|\theta|)
\]

and splitting the first moment at `pi/n` give

\[
\int_{-\pi}^{\pi}|\theta|J_n(\theta)\frac{d\theta}{2\pi}
<\frac{3\pi}{2n}<\frac5n.
\]

Hence a circular Lipschitz function of constant `D` satisfies the pointwise estimate

\[
|J_n*f-f|\le5D/n.
\tag{5}
\]

### 3.2 Uniform constants supplied by the original density and the new full odd resolvent

The source certificate gives

\[
\rho_{\rm in}(E)>\rho_{\min}:=24/10^6\quad(E\in I_E),
\qquad 0<a(E)<5000=:A.
\tag{6}
\]

On the source rectangle, write `t=cos P-5cos omega`, `D=t+4cos(omega-g)`, and `rho=sqrt(t^2-16)/(2pi D)`. The inherited inequalities `t<51/10`, `t^2-16>4`, `|t_omega|<3`, `D>57/10`, and `|D_omega|<7` give

\[
|\partial_\omega\log\rho|
\le153/40+70/57<6.
\]

Integration in `P` preserves this logarithmic bound for `rho_in`, so

\[
|a'(E)|\le3A\quad(E\in I_E).
\tag{7}
\]

Extend `a` around the remaining circular arc by the linear segment joining its endpoint values. The resulting positive continuous periodic function `a_ext` agrees with `a` on `I_E`, is bounded by `A`, and has Lipschitz constant at most `3A`.

There is also a uniform full-`P` density bound on the larger energy interval

\[
J_E=[E_*-2h,E_*+2h].
\]

The complete odd formula from the current absolute proof is

\[
f_B=\frac{R-4i\sin(\omega-g)}{t+4\cos(\omega-g)}.
\]

On all `P` and `E in J_E`, the elementary golden-ratio bounds still give `3<t<51/10` and `t+4cos(omega-g)>21/5`. The physical square root has `0<=Re R<16/5`. There are no poles. The explicit formula and nonzero denominator give locally uniform exterior radial bounds through the square-root edges, not merely finite almost-everywhere boundary values. This excludes a singular part of the contact measure on `J_E`. Its density therefore satisfies

\[
0\le\rho(P,E-\beta)\le M_0:=\frac8{21\pi}<\frac8{63}.
\tag{8}
\]

This is a bound for the complete odd port, including all `P`, and is not a selected-density replacement in the capture denominator.

### 3.3 The finite polynomial source

Set

\[
p_M=\mathcal F_M\mathbf1_{I_P},\qquad
e_N=\mathcal F_N\mathbf1_{I_E},\qquad
a_n=J_n*a_{\rm ext},
\]

and define the unnormalized finite vector

\[
\zeta_{M,N,n}=a_n(U_1)e_N(U_1)p_M(T_R)a_0.
\tag{9}
\]

Here a trigonometric polynomial is evaluated as a finite Laurent polynomial of the corresponding unitary, with its spectral-angle convention fixed to agree with `P,E`. This is not a single-plane-wave replacement. All operators commute in the free token arrangement.

**Finite-source estimate.** For `M,N>=2` and `n>=1`,

\[
\boxed{\|\zeta_{M,N,n}-\psi\|\le
\frac{75}{\sqrt M}
+5000\sqrt{\frac{\delta}{3N}+\frac{\pi\delta}{N^2h^2}}
+\frac{1500}{n}=:\mathfrak e_{M,N,n}.}
\tag{10}
\]

Proof of the three terms:

1. Replacing the sharp momentum gate by `p_M` after the original energy gate costs at most `sqrt(M0/rho_min)/sqrt(M)<75/sqrt(M)`, by (4), (6), (8), and the constant norm-one fiber representative of `a0`.
2. The spectral measure of `p_M(T_R)a0` has total mass at most `delta/pi`. On `J_E` its density is at most `M0 delta/pi`, because Fejer convolution contracts the scalar `L2` norm. Equation (4) bounds the squared energy-filter error on `J_E` by `2M0 delta/N<delta/(3N)`. Outside `J_E`, every point of `I_E` is at circular distance at least `h`; `F_N(theta)<=pi^2/(N h^2)` gives `e_N(E)<=pi/(N h)`. This gives the remaining squared error `pi delta/(N^2 h^2)`. Multiply its square root by `A`.
3. Equations (5) and (7) give `|a_n-a_ext|<=15A/n`. Also `||p_M(T_R)a0||<=sqrt(delta/pi)<1/50`. Their product is less than `1500/n`.

If `mathfrak e<1`, normalize (9):

\[
\psi_{M,N,n}=\zeta_{M,N,n}/\|\zeta_{M,N,n}\|,
\qquad \|\psi_{M,N,n}-\psi\|\le2\mathfrak e.
\tag{11}
\]

For example, for any `0<epsilon<=1`, the explicit integer choices

\[
M\ge\left\lceil202500/\epsilon^2\right\rceil,
\quad N\ge\left\lceil4000000/\epsilon^2\right\rceil,
\quad n\ge\left\lceil9000/\epsilon\right\rceil
\tag{12}
\]

give `2 mathfrak e<=epsilon`. For the energy term, use the square-root sum inequality, `sqrt(pi delta)<3/50`, and allocate `epsilon/12` to each of its two summands.

The `U1` Laurent degree is

\[
D_E=N-1+2(n-1),
\]

and the center-translation degree is `M-1`. Since each object step changes at most one of `(R,r)` by one, (9) has support

\[
|r|\le D_E,\qquad |R|+|r|\le B_{\rm src}:=M-1+D_E.
\tag{13}
\]

In particular both physical constituent positions obey `|x_A|,|x_B|<=B_src`; the token remains exactly at zero. Tensoring this construction with the unchanged arbitrary `Phi` preserves the norm estimate without tracing out its reference.

The finite vector generally has unwanted momentum/channel components. Their squared norm is at most `epsilon^2` for any projector that annihilates the original source, by (11). This is the controlled replacement for the impossible assertion of exact sharp momentum support.

The finite polynomial coefficients are explicitly defined compact one-dimensional integrals. They have not been numerically evaluated here. If implemented coefficients differ, expand the complete two-variable Laurent polynomial in (9), and add the certified l1 sum of its coefficient errors to (10) before normalization. Each Laurent monomial is unitary, so this controls its action on the seed by the triangle inequality. Errors assigned separately to the three factors must include the corresponding amplitude/contractivity factors; their unweighted sum is not a substitute. Exact real-amplitude loading or a certified approximate loader remains an apparatus premise.

## 4. A finite filter approximating the entire original readout on its actual output state

### 4.1 The original selected bound root lies strictly inside the output momentum window

The inherited root proof applies on `|P|<=p_b=1/100`. On its pulse interval, `cos k in [-1/5,0]`; the exact identity

\[
v(k)^2=\frac{2(1-\cos k)}{3-2\cos k}
\]

therefore gives the convenient conservative bounds `4/5<v(k)<9/10`. With `L_b=165/13`,

\[
v(k)-\Omega_b'(P)\ge4/5-2L_b p_b=71/130.
\]

At `P=0`, the root equation differs from zero by at most `h+(9/10)delta_K=19/10000`. The mean-value theorem yields

\[
\boxed{|P_*(K,E)|\le\frac{247}{71000}<\frac1{250}}
\qquad(K,E\in I_K\times I_E).
\tag{14}
\]

Choose the even continuous plateau `g_P(P)` equal to one on `|P|<=1/250`, decreasing linearly to zero at `|P|=1/100`, and zero outside. Its Lipschitz constant is `500/3`. On the exact bound/positive-pulse/K/E event, replacing the sharp `|P|<=1/100` factor by this plateau has **zero** error, by (14) and the uniqueness of the inherited root. Binding and the other factors are retained.

### 4.2 Explicit polynomial bound and pulse selectors

For a unitary `Z` and `gamma=exp(-ig)`, put

\[
X_Z=\frac{|Z-\gamma I|^2}{4}
=\frac{2I-\overline\gamma Z-\gamma Z^*}{4},\quad 0\le X_Z\le I.
\]

Define the positive contraction polynomial

\[
B_\ell(X)=\sum_{j=0}^{\lfloor\ell/200\rfloor}
\binom\ell j X^j(I-X)^{\ell-j}.
\tag{15}
\]

It has Laurent degree at most `ell` in `Z`. For `x<=1/40000` it differs from one by at most `exp(-ell/31250)`; for `x>=1/100` it is at most the same quantity. One direct proof is the Bernoulli exponential-moment bound: the second derivative of a centered Bernoulli log-mgf is at most `1/4`, so the mgf is at most `exp(t^2/8)`. Markov's inequality optimized at `t=4d`, with `d=1/250`, gives `exp(-2ell d^2)`. Both spectral sets lie at least `d` from the threshold `1/200`.

For `Z=W`, on `|P|<=1/100`, the nominated eigenvalue obeys `|lambda_b(P)-gamma|<=1/100`. The remaining spectrum is at distance at least

\[
27/110-1/100=259/1100>1/5
\]

from `gamma`, using the inherited zero-momentum gap and perturbation estimate. Thus (15) approximates the nominated bound projector on this **restricted momentum block**, with error at most

\[
e_b=\exp(-\ell_b/31250).
\]

For `Z=V`, when `K in I_K` and `|P|<=1/100`, `k=K-P` lies strictly in `(-pi,0)` and

\[
|\varepsilon(k)-g|\le(9/10)(11/1000)<1/100.
\]

The plus eigenvalue is in the first spectral set of (15). The minus eigenvalue is more than one away from `gamma`, since `sin g>9/10`. Therefore (15) approximates `P_+(k)` there with error

\[
e_p=\exp(-\ell_p/31250).
\]

On this `k` block the plus branch also has strictly positive velocity. Thus the right-moving condition has not been replaced by an energy-only or memory-only herald.

### 4.3 Finite K/E and plateau filters, with actual-state errors

Let

\[
k_M=\mathcal F_M\mathbf1_{I_K},\qquad
e_N=\mathcal F_N\mathbf1_{I_E},\qquad g_m=J_m*g_P.
\]

The plateau error is at most `1000/m`. The pulse part of the actual receiver scattering output has its `K` and `E` spectral measures dominated by

\[
\frac{dK}{2\pi},\qquad \frac{\mathbf1_{I_E}(E)}{2h}\,dE,
\tag{16}
\]

respectively. For `K`, this statement is deliberately restricted to the pulse part: the pulse asymptotic receiver calibration commutes with `K`, whereas the token half-line calibration need not. The bare scattering operator preserves the original `K` marginal, and taking a pulse subprojection can only decrease it. The same domination holds after the memory projection, which commutes with both spectral variables.

Equation (4) therefore gives actual-state amplitude errors at most

\[
1/\sqrt{M_K},\qquad \sqrt{\pi/(hN_E)}.
\tag{17}
\]

No differentiability of the unknown selected scattering amplitude is used here.

Let `Pi_pulse` be the arrangement projector, `M1=|d1><d1|`, and `T_tot` the simultaneous center/carrier translation. Define the commuting finite Laurent-filter contraction

\[
\mathcal A=
\Pi_{\rm pulse}M_1\,
k_{M_K}(T_{\rm tot})\,e_{N_E}(U_0)\,g_m(T_R)\,
B_{\ell_b}(X_W)B_{\ell_p}(X_V)
\otimes I_{\rm carrier\ label}\otimes I_{\rm ref}.
\tag{18}
\]

The memory factor is exactly the original receiver-memory question, and the label factor is the identity on all 26 labels. The one-carrier safe-window premise identifies the periodic energy gate with the original additive energy interval; no many-carrier alias claim is made.

Telescope through the commuting contractions in the following order: first replace the finite K/E filters by their sharp projectors, then replace `g_m` by `g_P`, and only on this restricted block replace the bound and pulse filters by their spectral projectors. This order applies the gap estimates only where they have been proved. Using (14)–(17) gives

\[
\boxed{\|\mathcal A\Xi-Q\Xi\|\le
\frac1{\sqrt{M_K}}+\sqrt{\frac\pi{hN_E}}+
\frac{1000}{m}+e_b+e_p=:\epsilon_D.}
\tag{19}
\]

One explicit choice giving an error at most `epsilon`, for `0<epsilon<=1`, is

\[
M_K\ge\lceil25/\epsilon^2\rceil,\quad
N_E\ge\lceil80000/\epsilon^2\rceil,\quad
m\ge\lceil5000/\epsilon\rceil,
\]

\[
\ell_b=\ell_p=31250r,\qquad 2^{-r}\le\epsilon/5.
\tag{20}
\]

The simple exponential bound follows from `e>2`. The filter's physical spatial range is at most

\[
B_D=(M_K-1)+(N_E-1)+2(m-1)+\ell_b+\ell_p.
\tag{21}
\]

This is a bound on the actual joint event, not a claim that a receiver label alone diagnoses binding. It is also not a global sharp-projector operator-norm approximation.

### 4.4 Complete finite instrument and supplied-control boundary

The pass probability of (18) is `||A state||^2`; the pass map is `A`, not its effect `A* A`. All rejection must be retained.

For a state of known finite spatial support `Lambda`, choose the larger finite region `Lambda'` containing its `B_D` neighborhood. The finite matrix

\[
A_\Lambda=\mathbf1_{\Lambda'}\mathcal A\mathbf1_\Lambda
\]

acts exactly like `A` on that input and is a contraction. The finite-dimensional isometry with the two orthogonal outcomes

\[
|1\rangle A_\Lambda\psi
\ \oplus\ |0\rangle(I-A_\Lambda^*A_\Lambda)^{1/2}\psi
\]

can be extended to a finite unitary. Tensoring it with the identity retains arbitrary reference entanglement. This establishes a complete finite mathematical instrument on the specified input region. It does not assert finite range for the square root on the infinite lattice.

The Laurent construction uses adjoints of free steps and supplied coherent control/readout. It is not the forward-only instrument of #1746. Exact gate loading, controlled free steps, fresh outcome storage, local compilation and energy accounting remain apparatus premises to be reconciled with the existing finite-interface/local-execution owners.

## 5. Finite physical experiment: the exact error ledger

Let `Psi_f` be the normalized finite source from (11), with the original token and unchanged `Phi`, and write `||Psi_f-Psi||<=epsilon_S`.

For nonnegative integers `N_-` and `N_+`, prepare at time `-N_-` the finite reference vector

\[
(U'_0)^{-N_-}\Psi_f,
\qquad U'_0=U_0\otimes I_{\rm mem,ref},
\]

then evolve for `N_-+N_+` steps under the unchanged `U_rec`. Apply the finite instrument (18). Define the two **fixed-state** wave-operator errors

\[
\epsilon_-(N_-)=
\|U_{\rm rec}^{N_-}(U'_0)^{-N_-}\Psi-
\Omega_{{\rm rec},-}\Psi\|,
\]

\[
\epsilon_+(N_+)=
\|U_{\rm rec}^{N_+}\Omega_{{\rm rec},+}\Xi-
(U'_0)^{N_+}\Xi\|.
\tag{22}
\]

The inherited wave operators prove both tend to zero for the original fixed state. The receiver conjugacy gives memory/reference-uniform bounds through the fixed bare spatial packet and the calibration tail in (28); this is not uniformity over arbitrary spatial or time-translated packets. Asymptotic completeness gives `Omega_rec,+ Xi=Omega_rec,- Psi`. Since `A` is a contraction commuting with `U'_0`, unitary norm preservation and (19) give

\[
\left|\sqrt{p_{\rm finite}}-\sqrt{P_0}\right|
\le\epsilon_S+\epsilon_D+\epsilon_-(N_-)+\epsilon_+(N_+)
=:\epsilon_{\rm all}.
\tag{23}
\]

Consequently the exact useful probability bound is

\[
\boxed{
\bigl(\max(0,\sqrt L-\epsilon_{\rm all})\bigr)^2
\le p_{\rm finite}\le
\min\{1,(\sqrt U+\epsilon_{\rm all})^2\}.}
\tag{24}
\]

This amplitude estimate is much more useful at `P0` of order `10^-9` than a generic additive probability error `2epsilon`.

No finite-source ac assertion is needed in (23): any unwanted finite-source component is already included in `epsilon_S` and is propagated unitarily, not silently projected away.

### Exact locality after the two times have been supplied

The inverse free evolution of the finite source increases its object radius by at most `N_-`; the subsequent unchanged interacting evolution increases each constituent/carrier radius by at most `N_-+N_+`. A finite active region with radius

\[
\max\{100,B_{\rm src}+2N_-+N_+\}+B_D
\tag{25}
\]

therefore contains the complete causal cone through the readout. A finite implementation agreeing with the original local gates on that cone has **zero** finite-boundary error for this experiment. Nothing is truncated in the memory/reference register.

### A concrete error allocation, without a claim to a numerical scattering time

Take `epsilon_S=epsilon_D=10^-6`, using (12), (20). Their conservative spatial bounds satisfy `B_src<4.3*10^18` and `B_D<8.1*10^16`; these are deliberately loose existence bounds, not practical apparatus sizes. If one subsequently certifies integers `N_-,N_+` with

\[
\epsilon_-(N_-)+\epsilon_+(N_+)\le10^{-6},
\tag{26}
\]

then (3), (23) give `epsilon_all<=3*10^-6`. In addition to the strictly positive original-event approximation, this meets the absolute probability-error target `|p_finite-P0|<=L/4`:

\[
p_{\rm finite}\ge(57\cdot10^{-6})^2=3.249\cdot10^{-9},
\qquad
|p_{\rm finite}-P_0|
\le2\sqrt U\,\epsilon_{\rm all}+\epsilon_{\rm all}^2
<429\cdot10^{-12}<L/4.
\tag{27}
\]

The active spatial radius is then less than `max(100,4.4*10^18+2N_-+N_+)`. Formula (27), including its probability-error target, is conditional on the quantitative time certificate (26), not its substitute.

## 6. The exact outstanding quantitative time premise

The unresolved item is now concrete: certify (26), or a smaller readout-specific analogue obtained by placing the contraction `A` in front of the two differences in (22), for the **literal original packet and its fixed phase/time origin**.

The existing absolute boundary certificate computes `P0`; it does not by itself supply that rate. The trace-class theorem proves strong convergence, not a numerical modulus. The inherited no-uniform-shutoff theorem also prevents replacing this fixed-state request by a bound uniform over all time-translated packets in the energy band.

The receiver source gives an informative decomposition. Before receiver dressing, write `chi=S Psi_loc`. The outgoing error can be bounded by

\[
\epsilon_+(n)\le
\|(U^n\Omega_+-U_0^n)\chi\|
+2\delta_{\rm cal}(n),
\tag{28}
\]

where `delta_cal(n)` is the norm of the free positive-velocity pulse left of `z=100`, together with the free negative-velocity pulse right of that cut, in orthogonal spatial sides. The token calibration is exact under free evolution because tokens do not move. The bound `2` is uniform over arbitrary memory/reference inputs and keeps all labels. For the nominated positive branch the inherited statement is the sharper familiar `delta_n+tilde eta_n` wrong-memory bound.

Thus a practical proof still needs both:

* A free-tail estimate relative to the fixed receiver and time origin for the actual relevant scattering output, not merely an object-pulse relative moment.
* A quantitative interacting/free comparison for the same state, with a summable or otherwise rigorously cancellative remainder.

This is exactly the boundary that corrected R3 of PR #1744 leaves open for the actual selected component. Its smooth product-family bound cannot be substituted.

A naive absolute Cook sum is not yet that missing proof. The source's exact free contact amplitude is

\[
\langle a_0,U_1^n\psi\rangle
=\frac1{\sqrt{2h}}\int_{I_E}e^{-inE}\sqrt{\rho_{\rm in}(E)}\,dE.
\]

Integration by parts exposes nonzero sharp-endpoint terms of order `1/n`. The resulting available absolute `O(1/n)` estimate is not summable and therefore supplies no Cook-tail modulus. One must either retain the oscillatory cancellations with a proved remainder, derive an appropriate local-smoothness estimate, or introduce a quantitatively controlled smooth approximation and prove the corresponding comparison. The new source/filter errors above can pay for such an approximation; they do not assert that its scattering estimate has already been proved.

## 7. What is established by this draft and what remains with the existing owners

Equations (10)–(13) give an explicit finite-support approximation to the exact normalized source, with controlled channel/momentum leakage. Equations (14)–(21) give an explicit finite-range approximation of the complete original readout on its actual scattered pulse state, without assuming endpoint regularity of the selected amplitude. Equations (23)–(25) give the correct probability and finite-volume error ledger, uniformly retaining arbitrary old-memory/reference information.

The remaining new audit target for the #1815 packet is a quantitative fixed-state time certificate such as (26). Apparatus admission, forward-only realization, autonomous/native loading and long-term record retention remain reconciliations with the already reserved finite-interface, retention, filter and local-execution lanes. No existing claim is promoted and no competing closure is registered here.
