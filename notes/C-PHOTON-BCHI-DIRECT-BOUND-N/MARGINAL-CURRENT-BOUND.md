# Partial-current probabilities in the full measure

**Working item:** C-PHOTON-BCHI-DIRECT-BOUND-N; owner
[#1143](https://github.com/mathorn1973/twist-j/issues/1143).
**Author:** A. M. Thorn. **Date:** 24 September 2026.

**PUBLIC, NON-CANONICAL; candidate-T written derivation.** No Canon or phase
promotion. Basis: Public Canon v91; continuation of [CURRENT-BOUND.md](CURRENT-BOUND.md)
as merged in `1e967f5bb30e17094ef6c4fe18d7fbd91cb390ae`. This note extends its
pointwise Fourier estimate to partial-current marginals, including their
normalization. It proves no decay with distance and does not close P1.

The same agent wrote and checked this derivation with access to the source
proof. No independent or blind review is claimed. The finite audit in
[MARGINAL-PREREG-20260924.md](MARGINAL-PREREG-20260924.md) is a separate,
at-most-candidate-C check; it cannot establish the universal argument below.

## 1. Measure and partial marginals

Let E and P be the positively oriented edges and plaquettes of an even
periodic four-dimensional cubic lattice of side L>=4. Write

\[
 w(n)=2^{-|\operatorname{supp}n|},\qquad
 \Omega=\{n\in\{-1,0,1\}^{P}:\partial n\equiv0\pmod5\},
 \qquad j(n)=\partial n/5.
\]

Each edge meets six plaquettes, so j_e is in {-1,0,1}. The measure is
mu(n)=w(n)/Z on Omega, with Z=sum_Omega w(n). Let S,T be disjoint subsets
of E and a in {-1,0,1}^S. Define

\[
 Q_T^S(a)=\sum_{n\in\Omega}w(n)
       {\bf1}_{j|_S=a}{\bf1}_{j|_T=0},\qquad
 Z_T=\sum_{n\in\Omega}w(n){\bf1}_{j|_T=0}.
\]

Every unspecified current is summed. In particular, neither Q_T^S(a) nor
Q_T^S(0) denotes a complete fixed-current sector. The conditional measure
mu_T=mu(. | j|_T=0) exists because n=0 contributes, and
mu_T(j|_S=a)=Q_T^S(a)/Z_T. Taking T empty gives the original measure.

## 2. Mixed Haar and Z5 representation

For edge angles A, put W_p(A)=2+exp(i(dA)_p)+exp(-i(dA)_p). On S union T
integrate each angle against normalized U(1) Haar measure. On all remaining
edges average over A_e=2*pi*m/5, m=0,...,4. Denote this product measure by
d nu_(S union T)(A). Then

\[
 \boxed{Q_T^S(a)=2^{-|P|}\int
   e^{-5i\langle a,A_S\rangle}\prod_{p\in P}W_p(A)
   \,d\nu_{S\cup T}(A).}                                      \tag{1}
\]

To prove (1), expand each W_p as the three terms with plaquette charge
n_p=0,+1,-1 and coefficients 2,1,1. The common factor 2^(-|P|) gives
exactly w(n). Haar orthogonality enforces (partial n)_e=5a_e on S and
(partial n)_e=0 on T. The discrete average enforces divisibility by 5 on
every other edge. These are precisely the conditions in Q_T^S(a).
All products and sums are finite, so changing the integration order is valid.

The distinction from a naive sum of fixed-sector bounds is essential:
W_p(A)=2+2*cos((dA)_p)>=0 pointwise, including when exterior angles are
restricted to Z5. In (1) the only nonzero Fourier source is on S. There is
therefore a nonnegative exterior factor after integrating S. No oscillatory
character from an unspecified nonzero exterior current needs to be summed
or discarded.

## 3. A block bound for the partial marginal

For a plaquette p, let S_p be its four boundary edges and N_p the 21
plaquettes incident on at least one of these edges. Call p_1,...,p_k
compatible when their N_p are pairwise disjoint. Set S=union_i S_(p_i).
No plaquette then contains selected edges from two blocks. Allow any T
disjoint from S, with the zero-current condition already specified above.

For any exterior angles, orient the four variables of one block along
partial p. The block integrand is

\[
 H(z)=\prod_{i=1}^4|P_i(z_i)|^2
       (2+u z_1z_2z_3z_4+\bar u(z_1z_2z_3z_4)^{-1}),
 \quad P_i(z)=\prod_{r=1}^5(1+u_{ir}z),\quad |u_{ir}|=|u|=1.
\]

Here u=1 in the actual boundary coordinates. Sections 3-5 of
[CURRENT-BOUND.md](CURRENT-BOUND.md) prove pointwise

\[
 |\widehat H(5s_1,5s_2,5s_3,5s_4)|\le\widehat H(0)/16
       \quad(s_i\in\{-1,1\}).                                \tag{2}
\]

The proof uses the exact polynomial sum-of-squares identity, followed by
two applications of Holder's inequality. For mixed signs the shifted
degree-six coefficients vanish; the same bound applies. It permits all
exterior U(1) phases, so it also permits the mixed exterior domain in (1).

Integrate all selected variables first. The k block integrations factor
pointwise in the exterior variables. Apply (2) in each factor and then
integrate against the remaining nonnegative factor. The resulting zero
coefficients give exactly (1) with a=0. Since the original sum is
nonnegative, for every a whose selected entries are all nonzero,

\[
 \boxed{0\le Q_T^S(a)\le16^{-k}Q_T^S(0).}                    \tag{3}
\]

Equation (3) is uniform in the volume, compatible block positions and
the disjoint set T. It does not assume independence under mu or mu_T.
The condition on T must be zero current. This proof does not establish the
same conditional result for prescribed nonzero exterior currents or for
arbitrary fixed exterior plaquette values. The separate fixed-complete-
sector estimate in CURRENT-BOUND.md retains its own stated scope.

## 4. Normalized local circulation bounds

Orient every S_p along partial p and define Y_p to be +1 if all four
oriented edge currents are +1, -1 if they are all -1, and 0 otherwise.
Other currents may touch the block. Y_p is a local pattern indicator,
not an assertion that the complete current is an isolated elementary loop.

For compatible p_1,...,p_k, each circulation sign vector sigma in
{-1,1}^k specifies one a(sigma) covered by (3). Write

\[
 q_0=\mu_T(j|_S=0),\qquad
 q_\sigma=\mu_T(Y_{p_i}=\sigma_i\text{ for all }i),\qquad
 c=16^{-k}.
\]

These events are disjoint, q_sigma<=c q_0, and q_0+sum_sigma q_sigma<=1.
Let F=sum_sigma q_sigma. Then F<=2^k c q_0<=2^k c(1-F), hence

\[
 \boxed{\mu_T(|Y_{p_i}|=1\text{ for all }i)\le\frac1{1+8^k}.} \tag{4}
\]

For the signed moment, let A and B be the sums of q_sigma over sign vectors
with product +1 and -1 respectively. Each group has 2^(k-1) elements.
With D=|A-B| and a_k=2^(k-1)c, one has
D<=max(A,B)<=a_k q_0 and q_0+D<=q_0+A+B<=1. Thus
D<=a_k/(1+a_k). Global reversal n->-n preserves mu_T and changes each Y
to -Y, so odd products have expectation zero. For even k,

\[
 \boxed{\left|\mathbb E_{\mu_T}\prod_{i=1}^kY_{p_i}\right|
       \le\frac1{1+2\,8^k}.}                                \tag{5}
\]

In particular, in the full original measure as well as under a permitted
zero-current condition,

\[
 \mu_T(|Y_p|=1)\le\frac19,\qquad
 \mu_T(|Y_p|=|Y_q|=1)\le\frac1{65},\qquad
 |\operatorname{Cov}_{\mu_T}(Y_p,Y_q)|\le\frac1{129},         \tag{6}
\]

where the last two bounds require compatible blocks. Each individual mean
vanishes by reversal, so the covariance in (6) is the signed second moment.
The constants are optimal for the relaxed mass inequalities used here;
attainability in the lattice measure W is not established.

## 5. The remaining connected quantity

The pair covariance has the exact identity

\[
 \operatorname{Cov}_{\mu_T}(Y_p,Y_q)
 =2\{\mu_T(Y_p=1,Y_q=1)-\mu_T(Y_p=1,Y_q=-1)\}.             \tag{7}
\]

The estimates above control the two nonnegative probabilities individually.
They give no improvement in their difference as the blocks separate.
For example, the abstract unnormalized masses
q_00=256, q_++=q_--=1, q_+-=q_-+=0 obey all two-block inequalities,
respect global reversal and give covariance 1/129 after normalization.
There is no distance variable in these constraints. This is a limitation of
the mass inequalities alone, not a realizable counterexample to decay in W.

Consequently (6) cannot supply a volume-uniform summable covariance tail.
Moreover Y_p is not j_e. Configurations without any complete elementary
circulation can still carry nonzero currents. A bound on these selected
patterns cannot be substituted for a bound on the full edge-current
covariance C_j(e,f) or chi_*.

The next analytical target is distance-dependent cancellation in (7), with
an additional argument covering non-elementary current configurations
before transfer to C_j. Equivalently, a direct uniform tail estimate for the
full current covariance would bypass these pattern indicators. The required
thermodynamic-first, infrared-second control and the positive P1 gap
underline(b)-25*overline(chi)>0 remain open at Public Canon v91.
