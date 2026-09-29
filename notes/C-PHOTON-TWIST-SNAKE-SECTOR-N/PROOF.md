# Class-restricted ladders and the sector sum rule for the twisted ratio

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-TWIST-SNAKE-SECTOR-N
- Author: A. M. Thorn
- Basis: Public Canon v92; public main
  `fe64af20c9aae768de8a25576e3316ba0b5bd352`, the merge of #1260
- Scope: exact finite-volume identities for the partially twisted link
  measures of `notes/C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N/PROOF.md` (#1259,
  cited as (S.n)) restricted to two integer sector classes, and the sum
  rule that recombines the classes.
- Primary thermodynamic lower bound: **NOT PROVED**.

The measure, seam, endpoint measures, signed contrast, partially twisted
chain, naive and conditional estimators, control identities and slice
sector bookkeeping are those of (S.1)-(S.16) and of the #1249 proof cited
there. Nothing there is modified or promoted. This note adds the
identities needed to estimate the chain normaliser ratios within a class
of link fields whose definition moves with the twist count, and to
recombine the classes. It supplies no sign theorem, mixing-time estimate,
irreducibility proof or thermodynamic bound.

## 1. Objects

Let L be even, L>=4, k in {1,2}, and h_n, Q_n, nu_n, r_n = Q_{n+1}/Q_n,
rho_n = h_{n+1}/h_n for 0<=n<=L^2 as in (S.2)-(S.4): the source k acts on
the first n seam plaquettes q_0,...,q_{n-1} ordered by j = x_2 + L x_3, and
Q_0 = Z_0, Q_{L^2} = Z_k, R_k = prod_n r_n. For a link field alpha and a
slice j let s_j(alpha, n) be the sum over the L^2 01-plaquettes of slice j
of the representative in {-2,...,2} of the effective flux in ensemble n,
c_j(n) the representative of the source of the seam plaquette q_j in
ensemble n (k if j<n, else 0), and

\[
w_j(\alpha,n)=\frac{s_j(\alpha,n)-c_j(n)}{5}\in\mathbb Z,\qquad
W_n(\alpha)=\sum_{j<n}w_j(\alpha,n),
\tag{1}
\]

the integer of (S.6) and its sum over the twisted slices. Only w_n differs
between ensembles n and n+1, since only the source of q_n changes; hence

\[
W_{n+1}(\alpha)=W_n(\alpha)+w_n(\alpha,n+1).
\tag{2}
\]

## 2. Classes, restricted measures, restricted kernel

For 0<=n<=L^2 define

\[
C_0(n)=\{\alpha:\ 2W_n(\alpha)\ge -n\},\qquad
C_-(n)=\{\alpha:\ 2W_n(\alpha)< -n\},
\tag{3}
\]

a partition of F_5^E for every n, with C_-(0) empty. For c in {0,-} let

\[
Q_n^{(c)}=\sum_{\alpha\in C_c(n)}h_n(\alpha),\qquad
\nu_n^{(c)}=\frac{h_n\,1_{C_c(n)}}{Q_n^{(c)}},\qquad
Q_n=Q_n^{(0)}+Q_n^{(-)}.
\tag{4}
\]

nu_n^{(c)} is a probability measure whenever Q_n^{(c)}>0; Q_n^{(0)}>0
always (the all-zero field has W_n=0) and Q_n^{(-)}>0 for n>=1 (the field
with alpha_0=2 on the 0-link at x_0=x_1=0 of every slice has w_j=-1 on
every twisted slice, so W_n=-n).

*Restricted single-link kernel.* Fix n and c and a link e. The conditional
law of alpha_e given alpha_{-e} under nu_n^{(c)} is proportional to
h_n(a,alpha_{-e}) 1_{C_c(n)}(a,alpha_{-e}) over a in F_5. Since a single
link change alters s_j of its own slice by 0 or +-5 (S.6) and no other
slice, this is the ordinary heat-bath law of (S.7) with the candidates
that leave C_c(n) given weight zero and the rest renormalised; the current
value is always allowed, so the normaliser is positive. Replacing alpha_e
by a draw from this law is a Gibbs update of nu_n^{(c)}: it leaves
nu_n^{(c)} invariant and satisfies detailed balance with respect to it.
Only 0- and 1-links of twisted slices can change W_n; for every other link
the restricted law equals the unrestricted one. Irreducibility of the
sequential sweep of these updates on C_c(n) is **not proved** here; it is
the assumption under which the time averages of section 3 estimate
expectations under nu_n^{(c)}, and the diagnostic probes it only
empirically (chains started in the cold class layout and chains that
reached the endpoint through the ladder).

*Class-preserving twist step.* Let alpha in C_c(n). After the source is
added to q_n, (2) gives W_{n+1} = W_n + w_n(alpha,n+1). If alpha is not in
C_c(n+1), replace the 0- and 1-links of slice n by the all-zero layout
(then w_n(alpha,n+1)=0) for c=0, or by alpha_0=2 on the 0-link at x_0=x_1=0
and zero on the other 0- and 1-links of the slice (then s_n = rep(k+2) +
rep(-2) = -3 for k=2 and -4 for k=1, so w_n(alpha,n+1) = -1 for both k) for
c=-. This touches no 01-plaquette of another slice, so W_n is unchanged
and, for every W_n with 2W_n >= -n, 2(W_n+0) >= -(n+1); for every W_n with
2W_n < -n, 2(W_n-1) < -(n+1)-1 < -(n+1). Hence the reset field lies in
C_c(n+1). It is a starting point for discarded sweeps, not a sample.

## 3. Four exact restricted step estimators

Fix n with 0<=n<L^2 and c with Q_n^{(c)}>0, Q_{n+1}^{(c)}>0. Let
I = C_c(n) ∩ C_c(n+1) and

\[
A=\sum_{\alpha\in I}h_{n+1}(\alpha),\qquad B=\sum_{\alpha\in I}h_n(\alpha).
\tag{5}
\]

Then, directly from (4) and rho_n = h_{n+1}/h_n,

\[
\begin{aligned}
F_n^{(c)}&:=E_{\nu_n^{(c)}}\bigl[\rho_n\,1_{C_c(n+1)}\bigr]=\frac{A}{Q_n^{(c)}},&
P^B_n{}^{(c)}&:=E_{\nu_{n+1}^{(c)}}\bigl[1_{C_c(n)}\bigr]=\frac{A}{Q_{n+1}^{(c)}},\\
P^F_n{}^{(c)}&:=E_{\nu_n^{(c)}}\bigl[1_{C_c(n+1)}\bigr]=\frac{B}{Q_n^{(c)}},&
B^w_n{}^{(c)}&:=E_{\nu_{n+1}^{(c)}}\bigl[\rho_n^{-1}\,1_{C_c(n)}\bigr]=\frac{B}{Q_{n+1}^{(c)}},
\end{aligned}
\tag{6}
\]

so that, with r_n^{(c)} = Q_{n+1}^{(c)}/Q_n^{(c)},

\[
r_n^{(c)}=\frac{F_n^{(c)}}{P^B_n{}^{(c)}}=\frac{P^F_n{}^{(c)}}{B^w_n{}^{(c)}}
\qquad\text{(pairings A and B)}.
\tag{7}
\]

The pairing F/B^w is not exact: it equals (A/B) r_n^{(c)}. The classes
move with n, so neither C_c(n+1) ⊆ C_c(n) nor the converse holds in
general; the four quantities are bounded (F and B^w lie in [0, max rho_n]
with the maximum of (S.6), since the indicator can vanish; P^F and P^B in
[0,1]), and when the restriction is dropped (indicators identically one)
F and B^w are the estimators (S.4), (S.5) and P^F = P^B = 1.

*Conditional forms.* Let e be a boundary link of q_n; e is a 0- or 1-link
of slice n. Under nu_n^{(c)} the conditional law of alpha_e given
alpha_{-e} carries no indicator, because at twist n slice n is untwisted
and W_n does not depend on alpha_e; it is the law of (S.7). Under
nu_{n+1}^{(c)} it carries 1_{C_c(n+1)}(a), which depends on a through
w_n(·,n+1), while 1_{C_c(n)} does not depend on a. Writing Pi_m(a) for
prod_{p∋e} W((d alpha^{e<-a})_p + k S_m(p)) and J(a) for
1_{C_c(n+1)}(a,alpha_{-e}), the tower property gives, exactly as in (S.8),

\[
\lambda_F(e)=\frac{\sum_a\Pi_{n+1}(a)J(a)}{\sum_a\Pi_n(a)},\quad
\lambda_{P^F}(e)=\frac{\sum_a\Pi_n(a)J(a)}{\sum_a\Pi_n(a)},\quad
\lambda_{B^w}(e)=1_{C_c(n)}\,\frac{\sum_a\Pi_n(a)J(a)}{\sum_a\Pi_{n+1}(a)J(a)},
\tag{8}
\]

with E_{nu_n^{(c)}} lambda_F = F_n^{(c)}, E_{nu_n^{(c)}} lambda_{P^F} =
P^F_n{}^{(c)}, E_{nu_{n+1}^{(c)}} lambda_{B^w} = B^w_n{}^{(c)}, for each of
the four boundary links and for their arithmetic mean. The denominator of
lambda_{B^w} is positive because the current value of alpha_e is allowed.
P^B is an indicator of W_n, which no boundary link of q_n can change, so
its conditional form is itself. Each lambda is a convex combination of
the values of the corresponding integrand and lies in the same interval
[0, max rho_n] or [0,1]; the single-sample variance inequality (S.10)
holds for each. Nothing is claimed about time correlations.

## 4. Sum rule and class weights

With Q_0 = Z_0 and C_-(0) empty, r_0 = Q_1/Q_0 is the unrestricted step of
(S.3)-(S.5). Define pi_1(c) = Q_1^{(c)}/Q_1, the class weights of the
one-twisted-slice unrestricted measure nu_1, and l_c = sum_{n=1}^{L^2-1}
log r_n^{(c)}. Telescoping (7) within each class from n=1 to L^2 and
summing the classes,

\[
Z_k=Q_{L^2}=\sum_cQ_{L^2}^{(c)}=\sum_cQ_1^{(c)}e^{l_c}
=Z_0\,r_0\sum_c\pi_1(c)\,e^{l_c},
\qquad
\log R_k=\log r_0+\log\Bigl[\pi_1(0)e^{l_0}+\pi_1(-)e^{l_-}\Bigr].
\tag{9}
\]

Likewise pi_k = nu_{L^2} = sum_c P_c nu_{L^2}^{(c)} with the endpoint class
weights and, for the seam observable Y_k of (S.1),

\[
P_c=\frac{\pi_1(c)e^{l_c}}{\sum_{c'}\pi_1(c')e^{l_{c'}}},\qquad
E_{\pi_k}Y_k=\sum_cP_c\,E_{\nu_{L^2}^{(c)}}Y_k.
\tag{10}
\]

These are finite identities of the stationary measures. The unrestricted
ladder (S.3) estimates the same log R_k; agreement of the two routes is an
exact identity that the diagnostic tests, not a hypothesis.

## 5. Sector observables of the control endpoints

The control chain of (S.12)-(S.13) carries a uniform whole-seam source at
both endpoints (2k at n=0, 3k at n=L^2), so every slice is equivalent
there and the twisted-slice sum W_n is uninformative at n=0. The per-slice
integers w_j(alpha,n) of (1) with the source-inclusive representative are
nevertheless defined for every slice at both endpoints; the diagnostic
records the numbers of slices with w_j = -1 and w_j = +1 over all L^2
slices and uses their agreement across chains, together with the mean of
Y, as the condition under which the exact identities (S.12), (S.13) and
E_{2k}Y = -E_{3k}Y are read. No statement is made about the weight of
any w value under either endpoint measure.

## 6. What this note does not control

(9) and (10) are exact if the restricted chains sample nu_n^{(c)} and the
step-zero and one-twisted-slice groups sample nu_0 and nu_1. Irreducibility
of the restricted kernel on C_c(n), the relaxation time after a
class-preserving reset, the correlation time of the samples and the
coverage of empirical intervals are not controlled here. The class weights
P_c are finite-volume quantities of the measure pi_k; no thermodynamic
statement about them is made or implied.

## 7. Disposition

The identities of this note are elementary consequences of positivity of
W, the definition of conditional expectation in a finite product space,
the integrality of the slice sums (S.6) and the telescoping of (S.3)
within a fixed class; they hold at every finite even L>=4 and are
candidate-T pending separate review. They give no positive lower bound on
R_k, on |E_{pi_k}Y_k|, on the sector polarization H_L or on its
thermodynamic limit. The separately preregistered floating-point run that
uses them is an engineering diagnostic with **ZERO scientific evidential
weight**; it cannot close P1, establish PHOTON-MASSLESS-PHASE, or promote
any Canon claim. Public Canon v92 is unchanged.
