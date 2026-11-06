# C-PHOTON-DISCRETE-DEFECT-CONTRAST-N preregistration

**PUBLIC, NON-CANONICAL. No Canon authority.**

- Owner: A. M. Thorn / photon-discrete-defect-contrast-20260927
- Issue: #1220
- Basis: Public Canon v92, public main 2294a75656ea10eeef2e11e04ac31f5d57ffdd8d
- Date: 27 September 2026
- Status ceiling: candidate-T for the written exact proof, candidate-C for one-architecture audit
- Layers: L4 for unnormalised discrete-source partition identities; L6 only for the normalized finite-measure response obtained from the same fixed partition sum. No new physical cross-layer dictionary.
- No claim: no positive thermodynamic floor, no P1 closure, no P2, S7, massless-phase closure, continuum, apparatus or physical photon.

## Frozen model

Let zeta be a primitive fifth root of unity, theta = 2*pi/5, and

\[
W(f)=2+\zeta^f+\zeta^{-f},\qquad f\in\mathbb F_5.
\]

For the same even four-torus \(K_L\) and fixed model used by the current photon notes, define for every discrete plaquette source \(b\)

\[
Z_L[b]=\sum_{a\in C^1(K_L;\mathbb F_5)}
       \prod_p W((da)_p+b_p).
\]

Let \(\Sigma\) be one 01 seam with \(L^2\) plaquettes and \(p\in\Sigma\).

## Frozen claims

### A. Exact local finite difference

For \(r=1,2\), at every fifth-root argument,

\[
w'(u)=
\frac{w(u+r\theta)-w(u-r\theta)}{2\sin(r\theta)},
\qquad w(u)=2+2\cos u.
\]

With \(C_{L,k}=\Phi'_k(0)\), seam translation symmetry then gives

\[
C_{L,k}
=
i\,\frac{L^2}{2\sin(r\theta)}
\frac{Z_L[k\Sigma-r\delta_p]-Z_L[k\Sigma+r\delta_p]}{Z_L[0]},
\]

using \((k,r)=(1,1)\) and \((2,2)\).

### B. Binary-pair Gram identity

For

\[
\mathcal B_\beta
=
\{S\in\{0,1\}^{P(K_L)}:\partial S=\beta\pmod5\},
\qquad
A_\beta(b)=\sum_{S\in\mathcal B_\beta}\zeta^{\langle S,b\rangle},
\]

prove

\[
Z_L[b]
=
5^{|E(K_L)|}\sum_\beta |A_\beta(b)|^2.
\]

### C. Galois covariance

For \(\sigma_r(\zeta)=\zeta^r\),

\[
\sigma_r(Z_L[b])=Z_L[rb].
\]

Define

\[
N_L=5^{-|E|}Z_L[0]\in\mathbb Z_{>0},
\]

and

\[
5^{-|E|}
\bigl(Z_L[\Sigma-\delta_p]-Z_L[\Sigma+\delta_p]\bigr)
=A_L+B_L\varphi.
\]

The coefficients \(A_L,B_L\) must be integers, and the \(k=2,r=2\) defect is the real Galois conjugate \(A_L+B_L(1-\varphi)\).

### D. Two-mode integer collapse

Prove exactly

\[
|C_{L,1}|^2+|C_{L,2}|^2
=
L^4\frac{A_L^2+B_L^2}{N_L^2}.
\]

At the unchanged candidate scope of #1213 and #1216 this yields only the conditional corollary

\[
\Delta_L(q)
\ge
H_L
\ge
\frac45 L^4\frac{A_L^2+B_L^2}{N_L^2}.
\]

The missing fixed-model theorem is still

\[
\liminf_{L\to\infty,\ L\ {\rm even}}
L^4\frac{A_L^2+B_L^2}{N_L^2}>0.
\]

## Frozen audit

The audit is algebraic only. It will:

1. implement exact \(\mathbb Z[\zeta_5]\) arithmetic with \(\Phi_5(\zeta)=0\);
2. check the local finite-difference identity for all five residues and \(r=1,2\);
3. freeze the toy incidence matrix
   \[
   D=\begin{pmatrix}1&0\\0&1\\1&-1\end{pmatrix}
   \quad\text{over }\mathbb F_5,
   \]
   enumerate all \(5^2\) link fields, all \(2^3\) binary plaquette chains and all \(5^3\) discrete sources, and compare the primal partition sum with the binary-pair Gram formula exactly;
4. check Galois covariance for \(r=1,2,3,4\) on every toy source;
5. check exact extraction into \(\mathbb Z[\varphi]\);
6. check the two-mode denominator identity and sum-of-two-squares collapse on an exact integer control grid.

No floating point, random input, Monte Carlo, extrapolation or phase inference is allowed. Hard execution timeout: 45 seconds. The first execution is preserved including failure. Any exception, nonzero exit, nonempty stderr, timeout or failed assertion consumes this audit attempt. A successful local run is candidate-C only and is not a two-architecture gate.

## Falsifiers

The item fails if the exact audit or written proof finds a sign or factor error in A, a boundary-matching or \(5^{|E|}\) error in B, a covariance failure in C, a failure of \(\mathbb Z[\varphi]\) integrality, or any defect of the final identity D.

No scientific execution occurred before this preregistration was committed.
