# Telescoping local estimators for the twisted partition ratio

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N
- Author: A. M. Thorn
- Basis: Public Canon v92; public main
  `213fad32b3cc3070685d226403d5aec93a37c9f5`, the merge of #1258
- Scope: exact finite-volume identities for a chain of strictly positive
  partially twisted link measures and their bounded local ratio estimators.
- Primary thermodynamic lower bound: **NOT PROVED**.

The measure, seam, endpoint measures and signed contrast are those of
`notes/C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N/PROOF.md` (#1249), whose
equations are cited below as (E.n). Nothing there is modified or promoted.
This note adds the identities needed to estimate the partition ratio
R_k=Z_k/Z_0 through L^2 local steps instead of one global endpoint flip.
It supplies no sign theorem, mixing-time estimate or thermodynamic bound.

## 1. Fixed finite-volume objects

Let L be even, L>=4, K_L=(Z/LZ)^4 the periodic cubical complex with
positively oriented links E and plaquettes P, theta=2 pi/5 and

\[
W(f)=2+2\cos(\theta f),\qquad f\in\mathbb F_5,
\]

so W(0)=4, W(+-1)=phi^2, W(+-2)=phi^{-2} with phi the golden ratio. All
five values are strictly positive. For a link field alpha in F_5^E the
oriented coboundary (d alpha)_p is the display preceding (E.1). Let Sigma
be the 01 seam
at x_0=x_1=0: the L^2 positive 01 plaquettes with one plaquette for every
(x_2,x_3). Fix k in {1,2} and, as in (E.4),

\[
Z_k=\sum_\alpha\prod_pW\bigl((d\alpha)_p+k\Sigma_p\bigr),\qquad
R_k=Z_k/Z_0\in(0,1],\qquad
\pi_k(\alpha)=Z_k^{-1}\prod_pW\bigl((d\alpha)_p+k\Sigma_p\bigr).
\]

With Y_k=L^{-2} sum_{p parallel 01} tan(theta((d alpha)_p+k Sigma_p)/2) as
in (E.6), the finite identities (E.7), (E.12) and (E.13) give

\[
-iC_k=R_k\,E_{\pi_k}Y_k,\qquad
E_{\pi_0}Y_0=0,\qquad E_{\pi_0}Y_0^2\le1,\qquad
\operatorname{Var}_{\pi_k}(R_kY_k)\le R_k(R_k+1)\le2.
\tag{1}
\]

The vanishing of E_{pi_0}Y_0 is the reversal symmetry alpha -> -alpha of
the untwisted measure together with oddness of the tangent; it is exact at
every finite L.

## 2. The partially twisted chain

Order the seam plaquettes q_0,...,q_{L^2-1} by j=x_2+Lx_3. For
0<=n<=L^2 let S_n be the indicator of {q_0,...,q_{n-1}} and define

\[
h_n(\alpha)=\prod_pW\bigl((d\alpha)_p+kS_n(p)\bigr),\qquad
Q_n=\sum_\alpha h_n(\alpha),\qquad
\nu_n=h_n/Q_n.
\tag{2}
\]

Every factor is one of the five positive values of W, so every h_n is
strictly positive and every nu_n is a strictly positive probability
measure on all link fields. S_0=0 and S_{L^2}=Sigma, hence Q_0=Z_0,
Q_{L^2}=Z_k, nu_0=pi_0, nu_{L^2}=pi_k, and

\[
R_k=\prod_{n=0}^{L^2-1}r_n,\qquad r_n=\frac{Q_{n+1}}{Q_n}.
\tag{3}
\]

The chain normalisers Q_n are written with a different letter because
Z_1 and Z_2 already denote the fully twisted endpoints. For 0<n<L^2 the
intermediate S_n is not a cocycle; no cohomological meaning
is attached to nu_n. It is only a positive interpolating weight in which
the source k acts on n seam plaquettes.

## 3. Naive ratio estimators

Write F_p=(d alpha)_p+kS_n(p) mod 5 for the effective flux in ensemble
n. Since h_{n+1}/h_n depends only on the plaquette q_n,

\[
\rho_n(\alpha)=\frac{h_{n+1}(\alpha)}{h_n(\alpha)}
=\frac{W(F_{q_n}+k)}{W(F_{q_n})},\qquad
E_{\nu_n}\rho_n=\frac{1}{Q_n}\sum_\alpha h_{n+1}(\alpha)=r_n.
\tag{4}
\]

Likewise, in ensemble n+1 where the effective flux of q_n includes the
source,

\[
\rho_n^{-1}(\alpha)=\frac{W(F_{q_n}-k)}{W(F_{q_n})},\qquad
E_{\nu_{n+1}}\rho_n^{-1}=\frac{1}{r_n}.
\tag{5}
\]

Both estimators are bounded. Their values lie in the finite set
{W(f+k)/W(f): f in F_5}, which is {phi^{-4},phi^4,1,phi^2/4,4/phi^2} for
k=1 and {phi^{-4},phi^4,1,phi^{-2}/4,4phi^2} for k=2. Hence

\[
\phi^{-4}\le\rho_n\le\phi^4\ (k=1),\qquad
\tfrac14\phi^{-2}\le\rho_n\le4\phi^2\ (k=2),
\tag{6}
\]

numerically [0.1459,6.854] and [0.09549,10.47]. The same bounds hold for
rho_n^{-1}. Every finite empirical mean of either estimator lies in the
same interval.

## 4. Local conditional (Rao-Blackwellised) estimators

Let e be any link on the boundary of q_n and alpha_{-e} the remaining
links. Under nu_n the conditional law of alpha_e given alpha_{-e} is

\[
\nu_n(\alpha_e=a\mid\alpha_{-e})
=\frac{h_n(a,\alpha_{-e})}{\sum_{b\in\mathbb F_5}h_n(b,\alpha_{-e})}.
\]

Only the six plaquettes containing e depend on alpha_e; define the
heat-bath normaliser of e in ensemble m by

\[
\Lambda_m(e;\alpha_{-e})=\sum_{a\in\mathbb F_5}\prod_{p\ni e}
W\bigl((d\alpha^{e\leftarrow a})_p+kS_m(p)\bigr).
\tag{7}
\]

The factors of plaquettes not containing e are common to h_n and h_{n+1}
and cancel, so

\[
E_{\nu_n}\bigl[\rho_n\mid\alpha_{-e}\bigr]
=\frac{\sum_ah_{n+1}(a,\alpha_{-e})}{\sum_ah_n(a,\alpha_{-e})}
=\frac{\Lambda_{n+1}(e;\alpha_{-e})}{\Lambda_n(e;\alpha_{-e})}
=:\lambda_n(e;\alpha).
\tag{8}
\]

By the tower property E_{nu_n}lambda_n(e)=E_{nu_n}rho_n=r_n, exactly, for
each of the four boundary links e of q_n, and therefore also for their
arithmetic mean

\[
\bar\lambda_n=\tfrac14\sum_{e\in\partial q_n}\lambda_n(e),\qquad
E_{\nu_n}\bar\lambda_n=r_n.
\tag{9}
\]

Each lambda_n(e) is a convex combination of the five values of rho_n
obtained by varying alpha_e, with the conditional probabilities as
weights, so it obeys the bounds (6), and it does not depend on the value
of alpha_e itself. By the conditional-variance identity,

\[
\operatorname{Var}_{\nu_n}\lambda_n(e)\le\operatorname{Var}_{\nu_n}\rho_n,
\qquad
\operatorname{Var}_{\nu_n}\bar\lambda_n\le\operatorname{Var}_{\nu_n}\rho_n.
\tag{10}
\]

The second inequality follows from the first and the convexity of the
variance under averaging. These are stationary (single-sample) variances
under nu_n. No claim is made about the asymptotic variance of a time
average along a correlated Markov chain, which conditioning need not
reduce; that quantity is only compared empirically by the diagnostic.
The reverse version in ensemble n+1,

\[
\bar\lambda_n^{\mathrm{rev}}
=\tfrac14\sum_{e\in\partial q_n}
\frac{\Lambda_n(e;\alpha_{-e})}{\Lambda_{n+1}(e;\alpha_{-e})},\qquad
E_{\nu_{n+1}}\bar\lambda_n^{\mathrm{rev}}=\frac1{r_n},
\tag{11}
\]

is obtained in the same way from (5). No independence of plaquettes is
assumed anywhere; (8) is the definition of a conditional expectation in a
finite product space.

## 5. Exact control identities and the residue law

Reversal alpha -> -alpha together with evenness of W gives Z(c) = Z(-c) for
every integer seam-coefficient field c. For the whole-seam multiple 2k plus
the extra source k on the first n seam plaquettes,

\[
Z\bigl(2k+kS_n\bigr)=Z\bigl(-2k-kS_n\bigr)=Z\bigl(3k-kS_n\bigr)
=Z\bigl(2k+k(1-S_n)\bigr),
\tag{12}
\]

since 3k-k=2k on the twisted plaquettes and 3k=2k+k elsewhere modulo 5.
At n=L^2 this is Z(3k)=Z(2k), so the telescoping sum of log ratios of the
chain from 2k to 3k vanishes exactly. When n=mL is a whole number of rows
x_3<m, the complement 1-S_n is the set of rows x_3>=m, which the
translation x_3 -> x_3-m maps onto the rows x_3<L-m. Translation
invariance of the periodic weight gives

\[
C_m:=\log\frac{Z(2k+kS_{mL})}{Z(2k)}=C_{L-m},\qquad m=0,\ldots,L,
\tag{13}
\]

so the partial sums of the control chain at row boundaries are symmetric
and the sum over the middle block of steps mL<=n<(L-m)L vanishes exactly.
Reversal also gives E_{2k}Y = -E_{3k}Y for the seam observable: under
the joint reversal of the links and of the source, Y changes sign, since
tan(theta f/2) is odd and 5-periodic in f and -2k = 3k modulo 5. These
identities hold for the full ensembles at every finite even L.

With R_0=1 and R_k=E_mu cos(k theta A) from (E.5), the law p_a of the seam
residue A inverts by finite Fourier analysis:

\[
p_0=\frac{1+2R_1+2R_2}{5},\qquad
p_{\pm1}=\frac{1+R_1/\phi-\phi R_2}{5},\qquad
p_{\pm2}=\frac{1-\phi R_1+R_2/\phi}{5},
\tag{14}
\]

using cos(2 pi/5)=1/(2 phi) and cos(4 pi/5)=-phi/2. Nonnegativity of the
p_a is equivalent to

\[
R_1\le\phi^{-1}+\phi^{-2}R_2,\qquad R_2\le\phi^{-1}+\phi^{-2}R_1,
\tag{15}
\]

numerically R_1 <= 0.618+0.382 R_2 and R_2 <= 0.618+0.382 R_1; the first
is p_{+-2}>=0 and the second p_{+-1}>=0, while p_0>=0 follows from R_k>0.
Any pair of estimated ratios must satisfy (15); the p_a are descriptive
quantities of the untwisted measure.

## 6. Slice sector bookkeeping

For a slice (x_2,x_3) let s be the sum over its L^2 01-plaquettes of the
representative in {-2,...,2} of the effective flux, and let c be the
representative of the slice's seam source. Since the integer sum of the
curl over a closed 01-torus vanishes, s is congruent to the source modulo
five and w=(s-c)/5 is an integer. The value of w is a property of the
sampled configuration; it is not conserved by the single-link heat bath,
which changes s by 0 or +-5 whenever a representative wraps. The
diagnostic records the numbers of twisted slices with w=0, w=-1, w=+1 and
other, the number of untwisted slices with w!=0, and whether all twisted
slices share one of the values 0, -1, +1 while every untwisted slice has
w=0, which it calls a pure layout. No statement is made here about the relative
weight of these classes under nu_n; that weight is what the diagnostic
observes, and it is exactly the quantity that a chain trapped in one class
cannot estimate.

## 7. Combined estimate and what it does not control

With finite empirical means bar F_n of bar lambda_n under samples of nu_n
and bar B_n of bar lambda_n^rev under samples of nu_{n+1}, the analyzer
forms

\[
\widehat{\log r_n}=\tfrac12\bigl(\log\bar F_n-\log\bar B_n\bigr),\qquad
\widehat{\log R_k}=\sum_{n=0}^{L^2-1}\widehat{\log r_n},
\tag{16}
\]

and multiplies the resulting interval for R_k with the interval for the
sample mean of Y_k under nu_{L^2}=pi_k to bound the signed contrast (1).
The preregistered analysis weights the two logs by inverse variance
instead of equally; the equal-weight form is kept as a secondary value.
Equation (16) is a finite-sample construction: log of a sample mean is not
an unbiased estimator of log r_n, the paired deficit
log bar F_n + log bar B_n has population value zero only in equilibrium,
and no coverage statement is made for the empirical intervals. The
identities (3), (4), (5), (8), (9) and (11) are exact statements about the
stationary measures; they bound neither the time to reach them under the
single-link heat bath nor the time correlations of the samples.

## 8. Disposition

The identities of this note are elementary consequences of (E.1)-(E.7),
reversal, translation invariance and positivity of W; they hold at every
finite even L>=4 and are candidate-T pending separate review. They give no positive lower bound on
R_k, on |E_{pi_k}Y_k|, on the sector polarization H_L or on its
thermodynamic limit. The separately preregistered floating-point run that
uses them is an engineering diagnostic with **ZERO scientific evidential
weight**; it cannot close P1, establish PHOTON-MASSLESS-PHASE, or promote
any Canon claim. Public Canon v92 is unchanged.
