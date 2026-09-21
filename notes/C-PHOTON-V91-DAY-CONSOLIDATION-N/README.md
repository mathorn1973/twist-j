# Photon v91 day consolidation, 2026-09-21

**Working item:** C-PHOTON-V91-DAY-CONSOLIDATION-N  
**Issue:** #1128  
**Author:** A. M. Thorn  
**Date:** 21 September 2026  
**Target:** PUBLIC, NON-CANONICAL consolidation  
**Authority:** none. Public Canon v91 remains the only public authority.

## 0. Authority and hard boundary

Public authority at the time of this consolidation is:

STATE: ACTIVE  
CANON: Public Canon v91  
TAG: canon-v91  
MAIN: 11b66d4755a697031157f0e10dc1898a7d5b6379  
CONTENT_COMMIT: b89b0c80bb5cebddade567f31a979aaf42f1d9dd  
CANON_SHA256: 6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1  
CANON_BYTES: 772678

Immutable release:

https://github.com/mathorn1973/twist-j/releases/tag/canon-v91

Nothing in this note changes Canon, Registry, Frontier, GATES, #757, #742, or any formal probe predicate.

All photon work below is NON-CANONICAL unless an older Canon claim is explicitly named. Labels such as candidate-T and candidate-C are note-level scientific ceilings, not public Registry promotions.

The main finite photon attachment remains the open maintenance PR:

- PR #1104: https://github.com/mathorn1973/twist-j/pull/1104
- branch: codex/photon-finite-s2-v91
- head: 87ccd4b80575143ba1d3418171a7171c6e7d82e4

It is not merged by this consolidation.

## 1. Executive state

The photon lane made a large mathematical reduction today, but the program is not closed.

What is now structurally understood:

1. A finite positive transfer construction and electric insertion exist at candidate level.
2. Two-cut reflection positivity and a positive spectral reconstruction route have candidate proofs.
3. The exact finite axis tensor reduces to one scalar Maxwell coefficient.
4. The character ensemble has exact hard-dual, binary-pair, switching, lift-flow, and current-sector descriptions.
5. Charge-five current sectors have an exact renormalized geometric tension on the frozen even periodic sequence:
   \[
   0\le Q_j/Q_0
   \le 2^{-\lceil |\operatorname{supp}j|/8\rceil}.
   \]
6. If the correct positive continuum Maxwell tensor is obtained, the massless shell at \(E=|\mathbf q|\) and the rank-two photon projector are consequences, not extra assumptions.

What is not proved:

1. P1: a model-specific positive infrared coefficient \(\Delta>0\) for the fixed \(W\)-measure.
2. P2 actual hypotheses: the uniform second-moment and Hessian regularity needed to force the full continuum angular tensor.
3. Ordered-limit equivalence: the lowest finite-volume mode \(q_{\min}=2\pi/L\) is not automatically the S7 infrared scaling limit.
4. Spectral S7: a Euclidean tensor modulus is not yet the required positive energy-momentum measure and pole-band control.
5. S1 full-sequence convergence: the proposed S1-B complete-limit-set profile has not been adopted.

Therefore:

\[
\boxed{\text{PHOTON-MASSLESS-PHASE remains OPEN.}}
\]

Neither photon existence nor photon absence has been established for the fixed Gibbs model.

## 2. Public object map for today's lane

### 2.1 Finite transfer and first spectral reduction

### PR #1104, finite transfer, Gauss dynamics, infinite-volume scope

https://github.com/mathorn1973/twist-j/pull/1104

NON-CANONICAL notes. Finite S2 transfer is candidate mathematics. The transfer support, electric insertion, finite winding sectors, Gauss non-invariance, and conditional infinite-volume reconstruction are recorded there.

Do not read PR #1104 as a phase proof.

### #1105, spectral tightness, general R0, proposed S1-B

https://github.com/mathorn1973/twist-j/issues/1105

[candidate-T, conditional]

Key consequences include

\[
\int \coth(E/2)\,d\sigma_{BB}
\le a/\kappa^2,
\]

\[
\int 2/\sinh(E)\,d\sigma_{EE}
\le a/\kappa^2.
\]

These give \(O(M)\) low-energy spectral mass, exclude an \(E=0\) atom, and give an upper bound on any massless residue.

The old sufficient endpoint \(R\to0\) was replaced by

\[
\kappa^2 Z=a-R_0/3.
\]

S1-B, the complete periodic-limit-set profile, was drafted only. It is not adopted.

### #1106, continuum little-group classification

https://github.com/mathorn1973/twist-j/issues/1106

[candidate-T, conditional]

Reflection-inclusive \(O(4)\) covariance forces

\[
C_0(q)=A(|q|)P_{\rm ex}(q)+B(|q|)P_{\rm co}(q)
\]

and kills the exact/coexact mixed block. \(SO(4)\) alone is insufficient because Hodge star can intertwine the two rank-three sectors.

### #1107, exact finite axis little group

https://github.com/mathorn1973/twist-j/issues/1107

[candidate-T]

At a nonzero coordinate-axis momentum, exact finite hypercubic symmetry gives scalar exact/coexact rank-three blocks and zero mixed block.

This is a finite-lattice directional theorem. It does not prove radial isotropy or \(O(4)\) emergence.

### #1108, exact axis residue triad

https://github.com/mathorn1973/twist-j/issues/1108

[candidate-T written mathematics]

Define

\[
\Delta_L=A_L-B_L.
\]

At \(q_L=(2\pi/L)e_1\),

\[
\boxed{
\Delta_L
=
\kappa^2[
\widehat C_{01,01}(q_L)
-
\widehat C_{02,02}(q_L)]
=
\widehat C_{n,02,02}(q_L)
-
\widehat C_{n,01,01}(q_L)
=
a_L-R_L(q_L)/3.
}
\]

A covariance-level countermodel proves that CONTACT, positivity, local moments and hypercubic symmetry alone do not force \(\Delta>0\).

This issue introduced the complete joint axis limit-set language, but the closure audit below later proves that the \(q_{\min}\) path is not automatically the ordered S7 limit.

### #1109, complete periodic hard duality

https://github.com/mathorn1973/twist-j/issues/1109

[candidate-T]

The exact character weight

\[
c=(2,1,0,0,1)
\]

is the finite Fourier dual of \(W\). The complete periodic duality includes all

\[
H^2(T^4;\mathbb F_5)\cong\mathbb F_5^6
\]

flux sectors.

The charge-five current becomes the hard-dual monopole current:

\[
M_{\rm hard}=*j.
\]

Duality does not remove the phase problem. It restates it as a monopole-screening and exact/coexact anisotropy problem.

### #1110, positive Maxwell coefficient forces the shell

https://github.com/mathorn1973/twist-j/issues/1110

[candidate-T, conditional analytic theorem]

Proof object: 72e8938d25e0262a995585d16ad38eab69bb2069  
RESULT: ac55f1065b26d6e17631378f7f7027c16bfc6785

If the accepted continuum covariance has

\[
C_0(p)=cI_6+ZP_{\rm ex}(p),\qquad Z>0,
\]

then after retaining the contact terms and applying the frozen electric continuation, the positive spectral measure has the simple atom

\[
E=|\mathbf q|
\]

with residue

\[
R(\mathbf q)
=
Z|\mathbf q|\Pi_\gamma(\mathbf n),
\]

\[
\Pi_\gamma(\mathbf n)
=
\frac12
\begin{pmatrix}
P(\mathbf n)&-C(\mathbf n)\\
C(\mathbf n)&P(\mathbf n)
\end{pmatrix},
\qquad
\operatorname{rank}\Pi_\gamma=2.
\]

Thus shell location and two polarizations are downstream consequences once the actual P1/P2/S7 hypotheses are proved.

## 2.2 Exact binary surface and defect combinatorics

### #1111, uniform binary surface pairs

https://github.com/mathorn1973/twist-j/issues/1111

[candidate-T exact finite combinatorics]

The fixed action admits

\[
W(f)=|1+\zeta_5^f|^2,
\]

and

\[
Z_W(L)
=
\#\{(x,y)\in\{0,1\}^P\times\{0,1\}^P:
\partial x\equiv\partial y\pmod5\}.
\]

For the common syndrome \(b\),

\[
Z_W=\sum_b N(b)^2.
\]

Conditional on \(b\), the two binary surfaces are independent and uniform in the same fibre \(X_b\).

### #1112, component switching and surface-current competition

https://github.com/mathorn1973/twist-j/issues/1112

[candidate-T written mathematics; exact one-agent audits]

Mismatch components are separately closed modulo five and can be switched independently by \(x\leftrightarrow y\).

The covariance decomposes into connected-component form factors:

\[
\widehat C_{n,II}(q)
=
V^{-1}
E\sum_\gamma |F_{\gamma,I}(q)|^2.
\]

At an axis,

\[
\boxed{
\Delta_L(q)
=
V^{-1}E\sum_\gamma |F_{\gamma,02}(q)|^2
-
\frac{25}{\lambda(q)V}
E\sum_{\gamma\in\Gamma_5}
|\widetilde j_{\gamma,0}(q)|^2.
}
\]

Integer-closed components are nonnegative for this sign test. Negative contributions are localized to charge-five defect components.

An explicit connected 21-face defect support has bracket \(-25\), so componentwise positivity is false.

Proof: 5e96b9378d29a2e68f1e03a21098b0f425a9ac80  
Audits: 4c6e7be0f01bde2770147ff11a08938d4f83234a, ff6d88024ac9b194237e2adbb6c35cb0841138b5

### #1113, lift ambiguity is an affine cycle-flow problem

https://github.com/mathorn1973/twist-j/issues/1113

[candidate-T exact finite mathematics]

Only common syndrome edges \(b_e=\pm2\) admit two integer lifts.

Every realized integer boundary has

\[
r=\bar b+5t,
\qquad
\partial t=-\partial\bar b/5.
\]

Different lifts differ by a conserved current on the extreme-syndrome graph.

If that graph is a forest, the lift is unique and \(j=0\) identically.

### #1114, elementary current filling cost 21

https://github.com/mathorn1973/twist-j/issues/1114

[candidate-C]

For finite-support ternary two-chains,

\[
n_q\in\{-1,0,1\},
\qquad
\partial n=5\partial p,
\]

the exact minimum support is

\[
\boxed{|\operatorname{supp}n|_{\min}=21.}
\]

The lower bound uses one prospectively pinned exact 625-case enumeration on one x86_64 lane.

Proof: 1fe1bc190e48ee4c2a74821e0553b433db1e4b42  
RESULT: 802cb4f0ff5d05e5b67917e2888683c2f52f3fb4  
Audit: 09e8fbbdb136e4e0fa16eebdacfd51693f25eeca

The bare \(2^{-21}\) cost is not the renormalized current-sector activity.

## 2.3 Renormalized charge-five current control

### #1115, all closed-surface dressing summed

https://github.com/mathorn1973/twist-j/issues/1115

[candidate-T]

With

\[
M(r)=\#\{x\in\{0,1\}^P:\partial x=r\},
\]

\[
2^{|P|}Q_j
=
\sum_r M(r)M(r-5j),
\]

\[
2^{|P|}Q_0
=
\sum_r M(r)^2.
\]

The shift graph is a matching for \(j\ne0\), giving

\[
\boxed{Q_j<Q_0/2.}
\]

Proof: dc997419c7ce614d5daf747525653abbb039163f  
RESULT: 1c52e5139738ddfbcc4d78050c4a683a1e762233

### #1116, reserved primal finite-size AXIS-POS test

https://github.com/mathorn1973/twist-j/issues/1116

[PUBLIC RESERVATION ONLY]

No formal probe has been pinned or executed.

This lane tests the finite-size primal estimator of \(\Delta_L(q_L)\) only. Its maximum ceiling is C-grade finite-size evidence. It cannot close the thermodynamic theorem, P2, S7, or PHOTON-MASSLESS-PHASE.

After the closure audit below, any future interpretation must also respect that \(q_{\min}\) at fixed rescaled momentum does not by itself realize the ordered S7 limit.

### #1117, first-ring fixed-exterior healing route fails

https://github.com/mathorn1973/twist-j/issues/1117

[NON-CANONICAL route-negative; one-arch exact enumeration]

On the central-plus-first-ring 21-plaquette region there are no shared complete residual signatures between target sectors differing by \(5\partial p\).

Audit: 2aaaa3b7384a9bb3dbb499d47fcdba60223498d0  
RESULT: fcbfb0ac72856ea1be779bbd377f236d8df09744

### #1118, minimal correct healing block has ratio one

https://github.com/mathorn1973/twist-j/issues/1118

[candidate-T route-negative]

On the true 21-face four-cup healing block, complementation gives an exact bijection between the two local completion classes.

Therefore

\[
\rho_*=1.
\]

No strict fixed-exterior local completion factor exists even on the smallest correct healing block.

### #1119, exact compact-U(1) charge-five representation

https://github.com/mathorn1973/twist-j/issues/1119

[candidate-T]

The renormalized sector ratio is exactly a charge-five Wilson observable in the compact \(U(1)\) model with

\[
g(\alpha)=\cos^2(\alpha/2).
\]

This continuous extension is not chosen after the result:

\[
4g(\alpha)=2+2\cos\alpha.
\]

Reflection positivity holds for this \(g\), but no external area/perimeter theorem was imported.

### #1120, renormalized current perimeter tension

https://github.com/mathorn1973/twist-j/issues/1120

[candidate-T]

A one-edge conditional charge-five Fourier estimate gives

\[
|\widehat h(5)|
\le
\widehat h(0)/2.
\]

Packing plaquette-disjoint current edges yields

\[
Q_j/Q_0
\le
2^{-\lceil|\operatorname{supp}j|/19\rceil}.
\]

Proof: 80f0bb349868ec59a10c609e17a68cc1c9b7373d  
RESULT: ba8ce7d4ad5514b4df7c48ca1e5d5795623da7b9

### #1121, exact 8-color improvement

https://github.com/mathorn1973/twist-j/issues/1121

[candidate-T, even periodic volumes]

For even \(L\), the exact edge coloring

\[
c(x,\mu)=
\left(
\mu,
\sum_{\nu\ne\mu}x_\nu\bmod2
\right)
\]

has eight plaquette-disjoint color classes.

Therefore

\[
\boxed{
0\le Q_j/Q_0
\le
2^{-\lceil|\operatorname{supp}j|/8\rceil}
\le
\exp[-(\log2)|\operatorname{supp}j|/8].
}
\]

This includes all integer-closed dressing.

Proof: d6e04af74b487fcb8dcd360d245946d5f67a5dec  
RESULT: e62d24f70f402f0780310979305cc16021802ebb

## 2.4 P1 surface/current reduction

### #1122, source Hessian and the missing cluster estimate

https://github.com/mathorn1973/twist-j/issues/1122

[candidate-T]

The current generating function is

\[
\mathcal Z_L(h)=\sum_jQ_je^{\langle h,j\rangle}
\]

and is exactly the inhomogeneous primal source extension.

Thus

\[
\partial_{h_e}\partial_{h_f}\log\mathcal Z_L|_{h=0}
=
C_j^L(e,f).
\]

The geometric perimeter bound #1121 does not imply spatial clustering: two elementary current loops can be arbitrarily far apart while their combined support remains eight edges.

The coefficient-level sufficient comparison was reduced to

\[
b_*>25\chi_*.
\]

Proof: b828f5906e1102c1bb550998f60dbca3a9f79cdc  
RESULT: 1a57a47be4e1d536d6fe75f9f69b04e9cb1ecf03

### #1123, microscopic closed surfaces cannot carry q_min stiffness

https://github.com/mathorn1973/twist-j/issues/1123

[candidate-T]

For finite-lift integer-closed components,

\[
\partial c^\gamma=n^\gamma,
\qquad
\|c^\gamma\|_1\le4D_\gamma A_\gamma.
\]

Therefore

\[
|F_{\gamma,02}(q_L)|
\le
(8\pi/L)D_\gamma A_\gamma.
\]

A uniformly microscopic gas of finite closed surfaces cannot carry nonzero \(q_{\min}\) stiffness.

Wrapped/nontrivial \(H_2\) components remain outside this contraction estimate.

Proof: d6c1e4032adce0b1fc388a08ebf1096cf6f9b8b8  
RESULT: df61777de4eaa5e37dae54f67271326bd3d889fc

### #1124, coherent macroscopic sheet gives positive first harmonic

https://github.com/mathorn1973/twist-j/issues/1124

[candidate-T]

If an integer-closed component has one-sign \(02\) layer profile inside a cyclic interval of width at most \(\alpha L\), \(\alpha<1/2\), then

\[
|F_{\gamma,02}(q_{\min})|
\ge
\cos(\pi\alpha)
\sum_s|m_\gamma(s)|.
\]

An \(O(L^2)\) coherent oriented area gives an \(O(1)\) stiffness contribution.

A uniform occurrence probability \(p>0\) yields

\[
b_*\ge
p c^2\cos^2(\pi\alpha).
\]

Ordinary wrapping is weaker and does not imply this first-harmonic coherence.

Proof: 9fb427ab6cf871bbec84d0f70dc18a6ab682d190  
RESULT: d4d9c73eeb12df2ecd6b63037b49f0288951c59c

## 2.5 P1/P2 reduction and closure correction

### #1125, program reduction

https://github.com/mathorn1973/twist-j/issues/1125

This is the synthesis owner for the two remaining theoretical obligations.

Its early P1/P2 reduction remains useful, but its latest closure-audit comment is the controlling interpretation for continuation.

### #1126, P2 hypercubic Hessian theorem

https://github.com/mathorn1973/twist-j/issues/1126

[candidate-T, conditional]

Assuming uniformly summable second moments for

\[
A=25S_j=E_1^*KE_1,
\]

\[
B=S_\rho=E_2QE_2^*,
\]

\[
M=E_1^*KE_2^*,
\]

signed hypercubic symmetry and conservation force

\[
A(q)=
\alpha(|q|^2I-qq^T)+o(q^2),
\]

\[
HB(q)H^*
=
\beta(|q|^2I-qq^T)+o(q^2),
\]

\[
M(q)=o(q^2).
\]

The exact exterior complex then gives, for a fixed infinite-volume state,

\[
Q(q)
=
\beta I+
\Delta P_{\rm ex}^{\rm lat}(q)+o(1),
\qquad
\Delta=a-\alpha-\beta.
\]

Proof: b5a5b60d0855273d792cf3ea9e124a2c603fc89f  
RESULT: 96e3c6599236ef019ecb04fc6b585bc882c7a227

Important correction: #1126 does not by itself establish the ordered S7 limit or the spectral S7 certificate.

### #1127, P1 channel-resolved coefficient theorem

https://github.com/mathorn1973/twist-j/issues/1127

[candidate-T, conditional]

Using

\[
\rho
=
\kappa(5m+\sqrt5\,h),
\qquad
m=dF/5,
\qquad
h=dH,
\]

the score-defect coefficient is

\[
\beta
=
\kappa^2
(25\mu+10\sqrt5\,\xi+5\eta).
\]

Joint covariance positivity gives

\[
|\xi|\le\sqrt{\mu\eta}.
\]

Thus a robust sufficient P1 condition is

\[
\boxed{
\alpha+
\kappa^2
(5\sqrt\mu+\sqrt5\sqrt\eta)^2
<a.
}
\]

The sharper signed criterion retains \(\xi\).

Proof: 978bebc9de8d093ba42ce58aeb484e89a5f9b804  
RESULT: 42282c88f91f99bc38951ea289d299db61251b3c

No actual second-moment bounds strong enough to prove this inequality have been established for the selected model.

## 3. Closure-limit audit, controlling correction

Recorded on #1125:

https://github.com/mathorn1973/twist-j/issues/1125#issuecomment-5765436380

**C-PHOTON-CLOSURE-LIMIT-AUDIT-N**

[candidate-T written conditional mathematics plus an inference breaker; one-agent one-architecture audit]

This correction controls how all earlier \(q_{\min}\) statements may be used.

### 3.1 Lowest-mode inference gap

The S7 order is:

local thermodynamic limit, then reconstruction, then infrared scaling on fixed nonzero rescaled annuli, then shell extraction.

A joint finite approximation requires

\[
\varepsilon L\to\infty.
\]

The path

\[
q_L=2\pi e_1/L=\varepsilon_L k
\]

at fixed rescaled \(k\) keeps \(\varepsilon_LL\) constant.

Therefore a positive sequence \(\Delta_L(q_{\min})\) does not by itself prove a positive coefficient of the ordered S7 infinite-volume scaling limit.

An exact covariance-level witness preserves CONTACT, positivity, hypercubic covariance and same-face moments, has the same local limit as a constant covariance, but keeps

\[
\Delta_L(q_{\min})=1/3
\]

for every \(L\) while the local limiting infrared coefficient is zero.

This witness is not claimed to realize the selected Gibbs model. It proves an inference gap only.

### 3.2 Exact full-block Euclidean reconstruction identity

With

\[
s=|2\sin(q/2)|^2,
\qquad
P=E_1E_1^*/s,
\]

\[
A=E_1^*KE_1,
\qquad
B=E_2QE_2^*,
\qquad
M=E_1^*KE_2^*,
\]

and

\[
U=A-\alpha E_1^*E_1,
\qquad
V=B-\beta E_2E_2^*,
\]

the exact identity is

\[
\boxed{
\|Q-\beta I-\Delta P\|_{\rm HS}^2
=
\frac{
\|U\|_{\rm HS}^2+
\|V\|_{\rm HS}^2+
2\|M\|_{\rm HS}^2
}{s^2}.
}
\]

The operator error obeys

\[
\|Q-\beta I-\Delta P\|_{\rm op}
\le
\frac{
\max(\|U\|,\|V\|)
+\|M\|
}{s}.
\]

This is a Euclidean tensor modulus. It is not the positive spectral bounded-Lipschitz and pole-band control required by S7.2-S7.3.

### 3.3 Correct P1 finite-window certificate

The usable finite-window sufficient certificate remains

\[
\boxed{
\Delta
\ge
a_{\rm lower}
+
\frac{
M_{R,L}-E_{R,L}-T_R
}{24}.
}
\]

Here \(M_{R,L}\) is the measured or exactly bounded signed finite block, \(E_{R,L}\) is a proved finite-volume error, and \(T_R\) is a proved bound on the complete omitted infinite-volume weighted tail.

A positive right-hand side closes the coefficient gap.

No values establishing positivity for the selected action were obtained today.

Unknown \(E_{R,L}\) or \(T_R\) may not be replaced by zero.

### 3.4 Closure-audit custody

Proof: e6b338d3ebb00014ba0a3d1b69f3fa54bea4f89f  
Exact audit source: fe2cca8d3534e4e185319f2d2a814b249c6d6e88  
RESULT: 80796bb15d77617e8d05888fe0a0efb775e20bcf

Local audit:

- platform: Linux
- architecture: x86_64
- Python: 3.13.5
- exact arithmetic: integer / Fraction
- exit: 0
- stderr: 0
- groups: 4/4 PASS
- stdout SHA-256: 95a0c13322f156df1dfc1a4222ecc111d2b00c9cbfabab94c5767f6f04f02e4d

This is not a formal public probe, second-architecture gate, or independent theorem confirmation.

## 4. Current true frontier

### P1, phase coefficient

**OPEN.**

The target is

\[
\Delta>0.
\]

Equivalent coefficient forms include

\[
\Delta=a-\alpha-\beta,
\]

and

\[
\Delta
=
a-\alpha
-
\kappa^2
(25\mu+10\sqrt5\,\xi+5\eta).
\]

A robust sufficient criterion is

\[
\alpha+
\kappa^2
(5\sqrt\mu+\sqrt5\sqrt\eta)^2
<a.
\]

The strongest practical finite-window route currently written is the BLOCK-TEST with explicit \(E_{R,L}\) and \(T_R\).

What is missing is not algebra. It is a model-specific quantitative tail or clustering theorem, or an independently controlled finite-window certificate.

### P2, Euclidean angular tensor

**OPEN at its hypotheses.**

For a fixed infinite-volume state, #1126 plus the closure-audit identity show that uniform second moments of \(A,B,M\) force the continuum Maxwell angular tensor.

Still missing:

1. proof of those second moments for the selected fixed action;
2. uniform tail control over the complete admitted limit profile;
3. common limiting coefficients where required;
4. a proof connecting finite approximations to the ordered limit.

### Spectral S7

**OPEN separately from P2 Euclidean angular control.**

S7.2-S7.3 require control of positive energy-momentum measures, pole-band extraction and the regular spectral remainder.

A Euclidean operator-norm estimate is not automatically a spectral bounded-Lipschitz or pole-band estimate.

### S1

The original full even-volume sequence requirement remains the active specification in PR #1104.

The alternative S1-B complete-limit-set profile is proposed only. Do not silently switch to it.

## 5. What would actually close the mathematical photon attachment

A legitimate positive closure needs all of the following:

1. A proved thermodynamic / reconstruction state at the accepted S1 scope.
2. A P1 certificate giving a common positive
   \[
   \Delta>0.
   \]
3. P2 Euclidean tensor regularity in the ordered scaling limit.
4. Spectral S7 control connecting that Euclidean scaling tensor to the positive reconstructed spectral measure.
5. Then #1110 applies and yields
   \[
   Z=\Delta/\kappa^2>0,
   \qquad
   E=|\mathbf q|,
   \]
   and
   \[
   R(\mathbf q)
   =
   Z|\mathbf q|\Pi_\gamma(\mathbf n),
   \qquad
   \operatorname{rank}\Pi_\gamma=2.
   \]

Only after these are established can the mathematical S1-S7 photon attachment be called closed.

This still does not by itself close the broader Canon owner PHOTON-CONE-CONVERGENCE or physical apparatus/detector questions.

## 6. Route dispositions, do not repeat these attacks

The following routes were resolved today and should not be retried under new names without new premises.

1. Global covariance positivity alone to \(\Delta>0\): fails as an inference.
2. Force \(R\to0\): too strong. The correct coefficient is \(\kappa^2 Z=a-R_0/3\).
3. Componentwise surface positivity: false. #1112 has a connected negative defect component.
4. Naive continuous \(L^1\) certificate for the 21-face minimum: impossible. Stokes caps that relaxation at 5.
5. First-ring fixed-exterior local healing ratio: vacuous. #1117.
6. Strict local ratio on the correct 21-face healing block: false. #1118 has exact ratio one.
7. Perimeter tension alone to spatial clustering: false as an inference. #1122.
8. Microscopic closed surfaces to positive \(q_{\min}\) stiffness: impossible under bounded size moment. #1123.
9. Ordinary wrapping probability to positive first harmonic: insufficient. #1124.
10. Positive \(q_{\min}\) sequence to ordered S7 coefficient: unjustified without a limit-equivalence theorem.
11. Euclidean P2 modulus to complete spectral S7: unjustified.

## 7. START HERE NEXT SESSION

Do not begin by inventing another photon representation.

The fixed representation has enough structure.

### First priority: one model-specific P1 tail theorem

Attack the existing BLOCK-TEST:

\[
\Delta
\ge
a_{\rm lower}
+
(M_{R,L}-E_{R,L}-T_R)/24.
\]

The useful theorem must control \(E_{R,L}\) and \(T_R\) for the actual fixed \(W\)-measure.

Equivalent channel language may be used if it produces stronger bounds on

\[
\alpha,\mu,\eta,\xi.
\]

The current perimeter theorem #1121 is useful input but not enough because it does not control separation of disconnected current components.

### Second priority: make the same theorem pay for P2

A sufficiently strong exponential or weighted-second-moment result for the derived defect kernels should also establish the actual hypotheses of #1126.

Do not separately assume \(O(4)\) if the Hessian route can prove it.

### Third priority: ordered-limit bridge

Any finite-size attack must use a scaling path compatible with

\[
\varepsilon L\to\infty.
\]

Do not use \(q_{\min}=2\pi/L\) alone as the continuum coefficient.

If #1116 is ever executed, interpret it strictly as finite-size C-grade evidence unless a separate theorem connects its path to the ordered limit.

### Fourth priority: spectral reconstruction error

After the Euclidean tensor is controlled, prove the positive-measure S7.2-S7.3 bounds.

Do not rename a Euclidean matrix estimate as spectral pole control.

### Promotion discipline

When a genuine model-specific bound is found:

1. freeze one scoped item;
2. collision-scan issues, branches, probes and registry;
3. write the theorem with its exact limit order and complete error terms;
4. if computation is essential, preregister it under the public probe protocol;
5. promote only through the normal reviewed fold.

## 8. One-line restart state

PUBLIC Canon v91 unchanged. PR #1104 remains open. Photon finite/dual/switching/current algebra is highly developed. P1 OPEN: no proved positive Delta for the fixed Gibbs model. P2 OPEN at actual second-moment and ordered-limit hypotheses. Spectral S7 OPEN. S1-B NOT ADOPTED. Do not infer the continuum coefficient from q_min alone. Next theorem: prove finite-volume plus infinite-tail control for the actual defect second moment, ideally strong enough to discharge both P1 and P2.

Original new text: Apache-2.0.
