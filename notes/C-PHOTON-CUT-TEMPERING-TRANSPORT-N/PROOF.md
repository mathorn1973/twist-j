# Cut tempering and coherent sheet updates preserve the full pair law

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-CUT-TEMPERING-TRANSPORT-N.
- Author: A. M. Thorn.
- Scope: exact finite-volume stationary laws, kernel identities and reversal
  controls. No mixing-time or thermodynamic lower bound is proved.
- Sources within the repository:
  `notes/C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N/PROOF.md`, especially its
  positive twisted representation and endpoint-pair identity;
  `notes/C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N/PROOF.md`, especially its
  reversal identities and integer slice-sector bookkeeping.

The predecessor's consumed trajectory in
`notes/C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N/RESULT.md` motivates the additional
updates. It is not an assumption of any identity proved here. In
particular, this note does not interpret a failed trajectory as a failure
of the stationary identities.

## 1. Fixed carrier and an extended pair measure

Let L be even and at least four, and let the carrier be the positively
oriented periodic cubical four-torus. Links have values alpha_e in F_5.
Write theta=2 pi/5 and

\[
W(f)=2+2\cos(\theta f),\qquad f\in\mathbb F_5.
\]

All five weights are strictly positive: W(0)=4,
W(+-1)=phi^2 and W(+-2)=phi^{-2}. For a positive mu-nu plaquette,

\[
(d\alpha)_{\mu\nu}(x)=\alpha_\mu(x)
+\alpha_\nu(x+e_\mu)-\alpha_\mu(x+e_\nu)-\alpha_\nu(x).
\tag{1}
\]

Let Sigma contain the positive 01 plaquettes at x_0=x_1=0. Define the
larger cut

\[
\mathcal D=\{p:\ p\text{ is a positive }01\text{ plaquette at }x_0=0\}.
\tag{2}
\]

Thus Sigma is contained in D, |Sigma|=L^2 and |D|=L^3. The background
index b is either 0 (main pair) or 2 (reversal-control pair), k is either
1 or 2, and s is an endpoint bit. Put

\[
f_p(s,\alpha)=(d\alpha)_p+k(b+s)\Sigma_p\pmod5,
\]
\[
S_{\rm bulk}(\alpha)=\sum_{p\notin\mathcal D}\log W((d\alpha)_p),
\qquad S_{\mathcal D}(s,\alpha)=\sum_{p\in\mathcal D}\log W(f_p(s,\alpha)),
\]
\[
h_\lambda(s,\alpha)=
\exp\{S_{\rm bulk}(\alpha)+\lambda S_{\mathcal D}(s,\alpha)\},
\qquad 0\le\lambda\le1.
\tag{3}
\]

The associated probability law is h_lambda divided by its sum over both
s and all link fields. There is no separate normalization of either
endpoint before the pair is formed. At lambda=1 this is exactly the
native pair of full plaquette weights. At lambda=0 the cut factors have
been removed, s is an independent fair bit, and the remaining bulk
measure is generally not a uniform link measure. Removing the factors
does not remove the links or the periodic curl constraint.

The replica system has fixed values
0=lambda_0<...<lambda_M=1 and stationary product density

\[
\mathcal H((s_i,\alpha_i)_{i=0}^M)
\ \propto\ \prod_{i=0}^M h_{\lambda_i}(s_i,\alpha_i).
\tag{4}
\]

The extra replicas change the sampling procedure. The marginal at the
fixed slot lambda_M=1 remains the full native pair law (3), not a
sector-restricted or occupancy-balanced substitute.

## 2. Coherent sheet orbit and its exact heat bath

For j in Z/LZ define a link cochain eta_j by

\[
(\eta_j)_0(x)=\mathbf1_{\{x_0=0,\ x_1=j\}},\qquad
(\eta_j)_\mu(x)=0\quad(\mu\ne0).
\tag{5}
\]

Its nonzero links extend over every (x_2,x_3). Formula (1) gives

\[
(d\eta_j)_{01}(x)=
\mathbf1_{\{x_0=0,\ x_1=j\}}-
\mathbf1_{\{x_0=0,\ x_1=j-1\}},
\qquad (d\eta_j)_{\mu\nu}=0\quad(\mu\nu\ne01).
\tag{6}
\]

For 02 and 03 plaquettes the two possible eta_0 terms cancel because
eta_0 is constant in x_2 and x_3. The other three orientations contain
no nonzero component. Hence the update alpha -> alpha+a eta_j changes
only two L^2 sheets, both inside D, and has no bulk action cost.

At fixed s and lambda, form the five-element orbit
O_j(alpha)={alpha+a eta_j:a in F_5}. Draw its new member with

\[
\Pr(a\mid s,\alpha)=
\frac{\exp\{\lambda S_{\mathcal D}(s,\alpha+a\eta_j)\}}
{\sum_{c\in\mathbb F_5}
 \exp\{\lambda S_{\mathcal D}(s,\alpha+c\eta_j)\}}.
\tag{7}
\]

All action terms outside the two affected sheets cancel in this ratio.
The five link fields are distinct. Replacing alpha by any member of the
orbit only relabels its five members, so the denominator is the same
for every starting point in the orbit. Consequently, for alpha and
alpha' in the same orbit,

\[
h_\lambda(s,\alpha)K_j(\alpha,\alpha')
=\frac{h_\lambda(s,\alpha)h_\lambda(s,\alpha')}
{\sum_{\gamma\in O_j(\alpha)}h_\lambda(s,\gamma)}
=h_\lambda(s,\alpha')K_j(\alpha',\alpha).
\tag{8}
\]

The move is an exact finite-orbit heat bath. It requires neither a
normalizing partition sum nor a proposal fitted to observed sectors.
At lambda=0 all five orbit choices have probability 1/5.

This move acts on the integer branch that the predecessor recorded. For
example, take the full source k Sigma with b=0, s=1 and all links zero.
For every 01 slice the representative sum is k, hence w=0. Apply
alpha -> alpha+2 eta_0. For k=2 the seam representative becomes -1 and
the neighboring sheet representative becomes -2, so the sum is -3 and
w=(-3-2)/5=-1. For k=1 both representatives become -2, and again
w=(-4-1)/5=-1. This is an example of a legal branch-changing move, not
a statement that it equilibrates the branch distribution at lambda=1.
At lambda=0 it is one of the five equally weighted choices.

## 3. Other updates and replica exchanges

For one link e, condition on s and all other links. Its exact conditional
probability for value a is proportional to

\[
\prod_{p\ni e}W(f_p(s,\alpha^{e\leftarrow a}))^{t_p},
\qquad
t_p=\begin{cases}\lambda,&p\in\mathcal D,\\1,&p\notin\mathcal D.
\end{cases}
\tag{9}
\]

There are six incident plaquettes. Every conditional probability is
strictly positive, including at lambda=0. The usual finite conditional
probability identity proves detailed balance for each such heat bath.

An endpoint flip proposes s' = 1-s at the same alpha. A symmetric
proposal coin and Metropolis acceptance

\[
\min\{1,\exp[\lambda(S_{\mathcal D}(1-s,\alpha)
-S_{\mathcal D}(s,\alpha))]\}
\tag{10}
\]

preserve h_lambda. The bulk action is independent of s because all of
Sigma is in D. At lambda=0 a proposed flip is accepted with probability
one. A proposal coin strictly between zero and one also gives positive
probability to leave s unchanged.

For adjacent replica slots i and j, exchange their complete states
(s_i,alpha_i) and (s_j,alpha_j). Let Q_i=S_D(s_i,alpha_i) and similarly
Q_j. The ratio of the new to the old product density is

\[
\exp\{(\lambda_i-\lambda_j)(Q_j-Q_i)\}.
\tag{11}
\]

Both bulk terms cancel in the exchange. Accepting with the minimum of
one and (11) satisfies detailed balance for the product law (4).
Traveling labels, if recorded for transport diagnostics, are carried
with the complete state and do not enter the weight.

Each individual kernel preserves its declared law. A fixed composition
of single-link, sheet-orbit and endpoint kernels, followed by an
alternating schedule of adjacent exchanges, therefore preserves (4).
The composition itself need not be reversible. The observable is
measured at the fixed lambda=1 slot, including every declared target
observation; visits to other slots or to selected sectors do not replace
those observations.

For a finite carrier, full-link heat baths have positive probability to
set any prescribed link field in one sweep. Each sheet heat bath can
leave its state unchanged, each endpoint can be chosen either way using
the lazy flip (10), and every attempted exchange has positive acceptance
probability. Thus a complete sweep can reach any prescribed physical
replica state with positive probability: choose all exchanges to be
accepted, and choose the pre-exchange fields and bits to be the inverse
permutation of the desired final states. The same argument gives a
positive probability to return to the initial physical state. This
establishes finite-state irreducibility and aperiodicity under this
schedule. It gives no useful lower bound on a transition probability
uniform in L, no equilibration time and no error bound for a finite run.

## 4. The native signed estimator uses one common denominator

Write Z_t for the full partition sum with source t Sigma, and pi_t for
its normalized full link measure. The main pair b=0 at lambda=1 has
normalizer Z_0+Z_k. Define

\[
Y(s,\alpha)=L^{-2}\sum_{p\parallel01}
\tan\!\left(\frac{\theta f_p(s,\alpha)}2\right),\quad
I_0=\mathbf1_{\{s=0\}},\quad I_1=\mathbf1_{\{s=1\}}.
\tag{12}
\]

The tangent is well-defined on F_5: changing the integer representative
by five changes its argument by pi. Let c_k=-i C_k be the real signed
contrast of the endpoint proof. That proof gives
c_k=(Z_k/Z_0) E_{pi_k}Y. Directly under the target pair law,

\[
E I_0=\frac{Z_0}{Z_0+Z_k},\qquad
E(I_1Y)=\frac{Z_k}{Z_0+Z_k}E_{\pi_k}Y,
\]
\[
\boxed{c_k=\frac{E(I_1Y)}{E I_0}.}
\tag{13}
\]

These are equilibrium expectations, not a claim of unbiasedness for a
finite ratio of time averages. In particular, if Y^+=max(Y,0) and
Y^-=max(-Y,0), then

\[
c_k=c_k^+-c_k^-,\qquad
c_k^\pm=\frac{E(I_1Y^\pm)}{E I_0}.
\tag{14}
\]

The same full-pair denominator appears in both nonnegative terms. Their
relative weights are supplied by the full measure. Averaging separately
normalized positive and negative sectors, assigning equal weights to
initial branches, or replacing the signed numerator by its absolute
value would compute a different quantity. Positive variance does not
bound the difference in (14) away from zero.

For b=2 the analogous endpoint ratio would instead use Z_{3k}/Z_{2k}
and E_{pi_{3k}}Y. It is not c_k, and no main-pair contact-moment bound is
asserted for that control ratio. Its role here is solely the exact
reversal test proved next.

## 5. Reversal controls, including non-pure slice sectors

For b=2 consider the involution

\[
\mathcal R(s,\alpha)=(1-s,-\alpha).
\tag{15}
\]

Its effective flux is minus the original flux modulo five because

\[
-(d\alpha)+k(3-s)\Sigma
\equiv-[(d\alpha)+k(2+s)\Sigma]\pmod5.
\tag{16}
\]

Evenness of W shows that (15) preserves h_lambda at every lambda,
including the partially removed cut. It exchanges the two endpoints.
Oddness of the tangent shows Y o R = -Y. Therefore the exact controls are

\[
\boxed{E I_0=E I_1=\tfrac12,\qquad E Y=0,\qquad
E[Y\mid s=1]=-E[Y\mid s=0].}
\tag{17}
\]

Here E Y is the unconditional pair mean of the effective-source
observable (12), not E(I_1Y); the latter need not vanish.

Let rep take F_5 to {-2,-1,0,1,2}, and set
c_s=rep(k(b+s)). For a 01 slice indexed by z=(x_2,x_3), define

\[
w_z(s,\alpha)=\frac{
\sum_{x_0,x_1}\operatorname{rep}(f_{01}(x_0,x_1,z))-c_s}{5}.
\tag{18}
\]

The sum of a periodic integer curl over the slice is zero before
reduction, so the numerator is divisible by five. The number w_z is
always an integer. It is neither an added restriction on the measure
nor a conservation law of the local heat bath. For b=2 the endpoint
representatives obey c_{1-s}=-c_s, and rep(-f)=-rep(f). Consequently,

\[
w_z\circ\mathcal R=-w_z.
\tag{19}
\]

Thus the full conditional slice distributions obey
Pr(w_z=t | s=1)=Pr(w_z=-t | s=0), and in particular the endpoint means
of the slice average bar w=L^{-2} sum_z w_z are opposite. These
identities apply also when no sampled state has all slices in one
common branch. They do not depend on a pure-layout classification.

For the main pair b=0, reversal preserves the conditional untwisted
endpoint s=0 and makes Y and every w_z odd. Hence their conditional
means at that endpoint vanish. There is no corresponding fixed-twist
symmetry forcing the signed mean at s=1 to vanish or to be positive.

## 6. Why symmetry alone does not supply the missing mixing statement

In a fixed nonzero twisted endpoint, charge conjugation alpha -> -alpha
sends its effective flux to -f+2k Sigma. It is not the weight-preserving
map f -> -f at that same source. No periodic link cochain can compensate
by d eta=-2k Sigma, because Sigma has nonzero flux through a 01 torus
whereas every exact cochain has zero flux modulo five. A joint reversal
of source and links instead relates the distinct k and -k measures, as
used in (15)-(17).

Relocating a source by b_source -> b_source+d chi together with
alpha -> alpha-chi leaves the effective flux exactly unchanged. Such a
source-representation change does not change Y or the integer slice
branches (18). Combining an orientation reflection with charge
conjugation can preserve a fixed-source ensemble, but its two sign
changes also cancel on the corresponding 01 observable. These symmetries
cannot be used to impose equal weights on opposite signs of the target
observable.

The sheet move (7) is different: it changes the effective flux inside
the same finite-field cohomology class. The cut supplies a replica where
that move is uniform. Whether that replica communicates sufficiently
with the target slot during the declared budget is an empirical
transport question, not a consequence of the balance calculation.

## 7. Exact diagnostic for the old whole-volume temperature spacing

This paragraph concerns the old whole-volume density exp(beta S),
S=sum_p log W(f_p), not the new cut density (3). At beta=0 all links
and the endpoint bit are uniform and independent. Distinct plaquette
boundary rows over F_5 have different supports for L>=4 and hence are
nonproportional. Their two curls are therefore independent uniform
F_5 variables. Adding fixed source residues preserves this fact, and
the conditional first and second moments do not depend on the endpoint.

Writing a=log 2 and d=log phi, the five possible log weights are
2a,2d,-2d,-2d,2d. Thus

\[
E\log W=2a/5,\qquad
v:=\operatorname{Var}(\log W)=16a^2/25+16d^2/5,
\]
\[
\operatorname{Var}_{\beta=0}S=6L^4v.
\tag{20}
\]

The old spacing Delta beta=1/(2L) consequently has
Delta beta times sd(S) = L sqrt(6v)/2. Its dimensionless score
fluctuation scale grows with L. Spacing of order L^-2 would keep
that particular quantity bounded at beta=0. This is an exact local
scale calculation, not an acceptance estimate, proof of the old
failure, or protection against a bottleneck elsewhere on a ladder.
In particular, beta=0 uniform-link independence must not be applied
to the bulk-weighted lambda=0 cut law of this note.

## 8. Disposition and limits

Equations (3)-(19) are finite-volume identities for exactly specified
positive measures and kernels. They retain the complete signed
competition in (14). They do not give a positive lower bound for that
difference, for sector polarization H_L, or for any thermodynamic
liminf. Irreducibility at each finite L cannot replace a mixing-time
estimate or demonstrate sampling from stationarity within a budget.

The separately preregistered L=4 execution is a floating-point
engineering qualification with ZERO scientific evidential weight.
Observed replica transport, branch changes or agreement with exact
controls can qualify or reject that finite schedule under its frozen
rules; they cannot prove equilibrium, a thermodynamic lower bound, P1
or PHOTON-MASSLESS-PHASE. The primary lower bound remains open and
Public Canon v92 is unchanged.
