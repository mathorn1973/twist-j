# Positive endpoint estimators for the signed sector contrast

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N, #1249
- Author: A. M. Thorn
- Basis: Public Canon v92; public main
  `de4576b8dba5caf4764cd743e5545ec11e664da3`
- Scope: exact finite-volume identities and stationary-measure moment bounds.
- Primary thermodynamic lower bound: **NOT PROVED**.

The source contact identity is inherited from the public photon work; its
zero-momentum form is stated in
`notes/C-PHOTON-AVERAGED-SECTOR-POLARIZATION-N/PROOF.md`, section 3.
The full ternary measure and the sector observable are those used there and
in `notes/C-PHOTON-SECTOR-ORIENTATION-CANCELLATION-N/PROOF.md`.
We derive the required identities directly, so this note does not depend
on an unmerged discrete-defect calculation or on a numerical run.
The purpose is to define an estimator of the signed full-measure contrast
with an explicit volume-independent second-moment bound. It supplies no
sign theorem, mixing-time estimate, or thermodynamic lower bound.

## 1. Fixed finite-volume measure

Let L be even and L>=4, and let K_L=(Z/LZ)^4 be the periodic cubical
complex, with positively oriented edge and plaquette sets E and P. Put

\[
\theta=2\pi/5,\qquad \zeta=e^{i\theta},\qquad
w(u)=2+2\cos u,\qquad W(f)=w(\theta f).
\]

All five values W(f), f in F_5, are strictly positive. In particular,
although the continuous function w has zeros, none is an endpoint weight
used below. For a link field alpha in F_5^E, its oriented coboundary is

\[
(d\alpha)_{\mu\nu}(x)
=\alpha_\mu(x)+\alpha_\nu(x+e_\mu)
 -\alpha_\mu(x+e_\nu)-\alpha_\nu(x)\pmod5.
\]

The sum is over all link fields, without gauge fixing. For a real
plaquette source B define the finite analytic function

\[
\mathcal Z(B)=\sum_{\alpha\in\mathbb F_5^E}
 \prod_{p\in P}w\bigl(\theta(d\alpha)_p+B_p\bigr),
\qquad Z_0=\mathcal Z(0).
\tag{1}
\]

Changing the integer representative of (d alpha)_p does not change a
factor. Expanding w(u)=2+e^{iu}+e^{-iu} and summing the link characters
gives exactly

\[
\frac{\mathcal Z(B)}{Z_0}
=E_\mu\exp\!\left(i\sum_p n_pB_p\right),
\quad
\mu(n)=\mathfrak Z^{-1}2^{-|\operatorname{supp}n|},
\quad
\Omega_L=\{n\in\{-1,0,1\}^{P}:\partial n=0\pmod5\}.
\tag{2}
\]

Indeed the link sum contributes 5^{|E|} on an admissible n, and zero
otherwise; the product of its plaquette coefficients is
2^{|P|-|supp n|}. These common factors cancel in (2). Every surface
expectation in this note is in this original full measure.

Let Sigma be the 01 seam at x_0=x_1=0, with its positive orientation,
and retain

\[
F=\langle n,\Sigma\rangle,\qquad A=F\pmod5,\qquad
G=L^{-2}\sum_{p\parallel01}n_p,\qquad
Q=L^{-4}\sum_{p\parallel01}n_p^2.
\tag{3}
\]

The seam has L^2 faces; the set of all 01 faces has L^4 faces.
The sector is the residue of F, not of the generally noninteger G.
Parallel seams have the same residue by the mod-five boundary equations.
Translations preserve both the full measure and A, so
E_mu[G zeta^{kA}]=E_mu[F zeta^{kA}]. Thus the averaged observable below
measures the same previously defined one-seam contrast.
For k in {0,1,2}, define

\[
Z_k=\mathcal Z(k\theta\Sigma),\quad
R_k=Z_k/Z_0,
\quad
\pi_k(\alpha)=Z_k^{-1}
 \prod_pW\bigl((d\alpha)_p+k\Sigma_p\bigr).
\tag{4}
\]

The endpoint link measures pi_k are strictly positive. Reversal n->-n
in (2) gives

\[
R_k=E_\mu\cos(k\theta A),\qquad 0<R_k\le1.
\tag{5}
\]

The strict lower inequality follows from Z_k>0, not from pointwise
positivity of the cosine. No volume-independent positive lower bound for
R_k is asserted.

## 2. The first derivative measures the signed contrast

At an endpoint write

\[
X_{k,p}(\alpha)
=\tan\!\left(\frac{\theta((d\alpha)_p+k\Sigma_p)}2\right),
\qquad
Y_k=L^{-2}\sum_{p\parallel01}X_{k,p},
\quad
U_k=L^{-4}\sum_{p\parallel01}X_{k,p}^2.
\tag{6}
\]

The tangent is finite and independent of the chosen integer representative.
Set

\[
B_k(t)=k\theta\Sigma+tL^{-2}1_{01},
\qquad C_k=E_\mu[G\zeta^{kA}].
\]

Differentiating (2) at zero gives
Z_0^{-1}(d/dt) mathcal Z(B_k(t))|_0=i C_k.
On the link side, w'/w=-tan(u/2), so the same derivative is
-R_k E_{pi_k}Y_k. Therefore

\[
\boxed{C_k=iR_k E_{\pi_k}Y_k,
\qquad -iC_k=R_k E_{\pi_k}Y_k.}
\tag{7}
\]

Reversal shows that C_k is purely imaginary, so the right side is the
real signed contrast. These are identities of finite sums; differentiation
requires no exchange with a thermodynamic limit. The endpoint factors
are strictly positive, so all logarithmic derivatives used here exist in
a neighborhood of t=0.

## 3. The inherited contact identity gives a uniform moment bound

For X=tan(u/2), direct differentiation gives

\[
\frac{w''(u)}{w(u)}=\frac{X^2-1}{2},\qquad
(\log w)''(u)=-\frac{1+X^2}{2}.
\tag{8}
\]

First differentiate (2) twice in the source of a single face p, at
B=k theta Sigma. This gives

\[
-E_\mu[n_p^2\zeta^{kA}]
=\frac{R_k}{2}E_{\pi_k}(X_{k,p}^2-1).
\]

Summing over the 01 faces and dividing by L^4 yields

\[
E_\mu[Q\zeta^{kA}]
=\frac{R_k}{2}(1-E_{\pi_k}U_k).
\tag{9}
\]

Second differentiate along B_k(t). The product rule and (8) give

\[
-E_\mu[G^2\zeta^{kA}]
=R_k E_{\pi_k}\left[Y_k^2-\frac{1+U_k}{2}\right].
\tag{10}
\]

Eliminate U_k using (9). Since G^2+Q is reversal-even, the imaginary part
of the surface expectation vanishes, and we obtain the endpoint form of
the contact identity:

\[
\boxed{
R_kE_{\pi_k}Y_k^2
=R_k-E_\mu[(G^2+Q)\cos(k\theta A)].}
\tag{11}
\]

At k=0 this is the inherited zero-momentum identity

\[
E_\mu(G^2+Q)+E_{\pi_0}Y_0^2=1.
\tag{12}
\]

Here E_mu G=0 by reversal, so E_mu G^2 is also its variance. In particular,
G^2+Q is nonnegative and its mean is at most one. It follows from (11)
that

\[
0\le R_kE_{\pi_k}Y_k^2\le R_k+1,
\qquad
\boxed{\operatorname{Var}_{\pi_k}(R_kY_k)
\le R_k(R_k+1)\le2.}
\tag{13}
\]

The uniform bound concerns the endpoint observable with its exact
normalizing ratio. It does not assume independent plaquettes and does
not replace R_k by a fitted value. In particular, (13) alone is not an
error bar for a correlated finite simulation.

## 4. A positive pair ensemble incorporates the ratio

For a fixed k in {1,2}, introduce s in {0,1} and the unnormalized weight

\[
h_k(s,\alpha)=\prod_p W((d\alpha)_p+s k\Sigma_p),
\qquad
\nu_k(s,\alpha)=\frac{h_k(s,\alpha)}{Z_0+Z_k}.
\tag{14}
\]

This is a positive measure on the two actual endpoints, not a measure on
fractional twists. Let

\[
D=1_{\{s=0\}},\qquad T=1_{\{s=1\}}Y_k(\alpha),\qquad
p_0=E_{\nu_k}D=\frac1{1+R_k}\ge\frac12.
\]

The conditional law at s=1 is pi_k. Hence (7) and (13) give

\[
\boxed{\frac{E_{\nu_k}T}{E_{\nu_k}D}=-iC_k,}
\qquad
\boxed{E_{\nu_k}T^2
=\frac{R_k}{1+R_k}E_{\pi_k}Y_k^2\le1.}
\tag{15}
\]

Thus both the original normalization ratio and the signed contrast are
represented by a single positive target measure. The denominator has an
exact population lower bound, while the signed numerator has a uniform
second-moment bound. The ratio of finite empirical averages is not
asserted to be unbiased, and a finite trajectory can have a small or zero
empirical denominator despite the population bound.

For clarity about the ultimate diagnostic, if
m_a=E_mu[G 1_{A=a}], then reversal gives m_0=0 and m_{-a}=-m_a.
Finite Fourier orthogonality consequently gives

\[
|C_1|^2+|C_2|^2=5(m_1^2+m_2^2).
\tag{16}
\]

Both signed means in (15) must be assessed before taking their squares.
Squaring a noisy estimate has a positive noise contribution even when its
population mean is zero. Equation (16) supplies no lower bound by itself.

## 5. Stationary target of the proposed replica sampler

The following statements specify exact transition kernels. They are not
claims of exact arithmetic for their floating-point implementation.
For the same fixed k and finite L, set

\[
\beta_j=j/(2L),\quad j=0,\ldots,2L,\qquad
\nu_{k,\beta}(s,\alpha)
=\frac{h_k(s,\alpha)^\beta}
 {\sum_{s',\alpha'}h_k(s',\alpha')^\beta}.
\tag{17}
\]

At beta=0 this is the uniform measure on all links and both endpoints;
at beta=1 it is (14). Every intermediate weight is strictly positive.
The exponent beta scales the weight, not the seam twist. The target of
the complete replica array is the product

\[
\mathcal V_k=\bigotimes_{j=0}^{2L}\nu_{k,\beta_j}.
\tag{18}
\]

For fixed s and the other links, the heat-bath probability of assigning
the value a in F_5 to a link e is proportional to

\[
\prod_{p\ni e}
W\bigl((d\alpha^{e\leftarrow a})_p+s k\Sigma_p\bigr)^\beta.
\tag{19}
\]

All five probabilities are positive. This is the exact conditional law,
so one such update preserves nu_{k,beta}; a systematic sequence of link
updates does as well. Reversibility of the whole systematic sweep is
neither needed nor asserted.

A symmetric proposal to replace s by 1-s at fixed alpha has Metropolis
acceptance probability

\[
\min\{1,[h_k(1-s,\alpha)/h_k(s,\alpha)]^\beta\}.
\tag{20}
\]

This preserves nu_{k,beta}. For adjacent replicas with states x and y
(each state includes s and all links), exchange them with acceptance

\[
\min\{1,\exp[(\beta_j-\beta_{j+1})
                 (\log h_k(y)-\log h_k(x))]\}.
\tag{21}
\]

The ratio in (21) is exactly the new product weight divided by the old
one, so this move preserves (18). Normalizing constants cancel. Any
fixed composition of the stated preserving kernels preserves (18).
At stationarity the beta=1 replica therefore has exactly the pair
ensemble needed for (15).

All states of one replica can be connected by single-link changes and
endpoint flips, and each required nontrivial move has positive probability
at every finite beta and L. This describes the graph of the elementary
updates. The endpoint proposal can be made lazy by attempting the flip
with probability 1/2 and otherwise doing nothing; this preserves the same
measure. A mandatory endpoint flip at beta=0, in isolation, alternates s
and must not be cited as an aperiodic kernel. No convergence rate or
convergence theorem for an arbitrary composition schedule is asserted.

Finite-state accessibility provides no useful upper bound on the time
needed to reach equilibrium or on time correlations at the proposed
budget. Agreement across initial states, endpoint visits, exchange rates,
and block comparisons are diagnostics; without further justification
they are not a rigorous certificate of equilibration. The moment bounds
in (13) and (15) concern the exact stationary law and do not control this
remaining sampling error.

## 6. Disposition

The written finite-volume identities and moment bounds are candidate-T.
The underlying contact identity and source expansion are inherited;
their endpoint use and the pair-ensemble ratio are made explicit here.
No positive sector mean, nonvanishing large-volume contrast, Coulomb
phase, or physical photon follows from these upper bounds.

The separately preregistered floating-point run is an engineering
diagnostic with **ZERO scientific evidential weight**. It cannot earn a
computed theorem, validate the exact identities by numerical agreement,
close P1, or promote a Canon claim. A scientific gate would require its
own prospectively frozen admissible procedure and evidence contract.
The proof above is finite and analytic and does not depend on whether
that diagnostic runs, mixes, or produces any particular trend.
