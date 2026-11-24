# Positive pair/five wiring of the full two-replica measure

**PUBLIC, NON-CANONICAL. Candidate-T written proof, pending separate review.**
Working item: C-PHOTON-BCHI-DIRECT-BOUND-N, owner issue #1143.
Author: A. M. Thorn. Date: 26 September 2026. Apache-2.0.
Basis: Public Canon v92, public main `8b1132d828d94f83e653dab34d686a7e68394939`.

This continuation gives an exact positive auxiliary representation of **all**
pairs of configurations of the original measure. Unlike the restricted
replica fibers in [REPLICA-CAPS.md](REPLICA-CAPS.md), it fixes no corridor,
replica sum, empty halo, or exterior current sector. It also retains the
unsaturated backgrounds from [FULL-MEASURE.md](FULL-MEASURE.md).

The new ingredient is a normalized local partition into opposite-sign pairs
and same-sign five-blocks for as many as twelve incidence tokens. In particular,
the difference of two allowed currents can have magnitude two. A rule using
only the one-copy neutral matchings does not handle these cases.

The generic independent-replica covariance identity and component-sign method
are not claimed as new. The result here is their explicit positive pair/five
realization, with the stated rational weights, for this full replica measure.

**Neither the original uniform Xi_L bound nor P1 is proved.** A second,
precisely normalized sufficient moment is obtained below. No ordering between
it and the original Xi_L is asserted. The declared v92 theorem and all Canon,
registry, frontier, gate, workflow and formal-probe files remain untouched.

## 1. Original measure and a facewise bijection

Let L>=4 be even, V=L^4, and use the periodic four-dimensional cubical complex,
with canonical plaquettes P, edges E, boundary operator partial and incidence
signs epsilon(e,p). The measure is exactly

    mu_L(n)=Z_L^-1 product_p w(n_p) 1{partial n=0 mod 5},
    n_p in {-1,0,1},   w(0)=1,   w(+1)=w(-1)=1/2,
    j=partial n/5.

Take two independent copies n1,n2. Put s=n1+n2, d=n1-n2, a=|d| facewise.
The following table lists every possible (s,a) and the weight omega **per
allowed sign of d**, not the sign-summed weight:

| s | a | allowed d | omega(s,a) |
|---|---|---|---|
| -2 or +2 | 0 | 0 | 1/4 |
| -1 or +1 | 1 | -1,+1 | 1/2 |
| 0 | 0 | 0 | 1 |
| 0 | 2 | -2,+2 | 1/4 |

It accounts for all nine ordered pairs of ternary coefficients. The inverse
is n1=(s+d)/2, n2=(s-d)/2. Integrality and ternarity follow from the table.
Since two is invertible modulo five, the two closure constraints are precisely

    partial s=0 mod 5,     partial d=0 mod 5.                (1)

No additional parity filter is missing: parity is already enforced facewise.

## 2. A positive exact local projector

At an edge e make a_p distinguishable tokens (p,1),...,(p,a_p) for every
incident face p. There are m=sum_(p incident e) a_p<=12 tokens. Every token of
one face has the same incidence sign epsilon(e,p) x_p, where d_p=a_p x_p.

Partition these labelled tokens into unordered blocks of sizes two and five.
A pair requires opposite incidence signs; a five-block requires all five
incidence signs to agree. Write b for the number of five-blocks. Assign the
following weight to **each individual labelled-token partition**; omitted
entries are zero:

| m | b=0 | b=1 | b=2 |
|---|---|---|---|
| 0 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 4 | 1/2 | 0 | 0 |
| 5 | 0 | 1 | 0 |
| 6 | 1/6 | 0 | 0 |
| 7 | 0 | 1/6 | 0 |
| 8 | 1/24 | 0 | 0 |
| 9 | 0 | 1/42 | 0 |
| 10 | 25/3024 | 0 | 1/126 |
| 11 | 0 | 1/336 | 0 |
| 12 | 5/3696 | 0 | 1/1386 |

Call the entries lambda_(m,b). The empty partition has weight one. There are
no partitions at m=1 or m=3.

**Local identity.** For every assignment z_t in {-1,+1} to the m labelled
incidence tokens,

    sum_(pi compatible with z) lambda_(m,b(pi))
      = 1{sum_t z_t=0 mod 5}.                              (2)

**Proof.** Every compatible pair contributes zero to the sign sum, and every
compatible five-block contributes +5 or -5. Thus the left side vanishes on an
inadmissible assignment. For the remaining assignments let p,q be the numbers
of positive and negative tokens, p+q=m.

If only balanced pairs are possible, p=q=r and there are r! bijections between
the two signs. This gives the entries at m=0,2,4,6,8. If m is odd and admissible,
then m=5,7,9,11 and, up to reversal, p=r+5,q=r with r=0,1,2,3. There are
binom(r+5,5) r! compatible partitions into one five-block and r pairs: their
counts are 1,6,42,336. The reciprocal weights give (2).

At m=10 the admissible counts are (5,5),(10,0),(0,10). In the all-equal case
there are 10!/(5!^2 2!)=126 partitions into two indistinguishable five-blocks.
In the balanced case there are 5!=120 pair matchings and one partition into
opposite-sign five-blocks. Exactly

    120*(25/3024)+1/126=1.

At m=12 the admissible counts are (6,6),(11,1),(1,11). In the (11,1) case choose
the majority token paired with the minority token in eleven ways, and partition
the remaining ten into five-blocks in 126 ways. This gives 1386 partitions.
In the balanced case there are 6!=720 pair matchings and 6*6=36 partitions with
one positive five-block, one negative five-block and one remaining pair.
Exactly

    720*(5/3696)+36/1386=1.

These are all cases because m<=12. This proves (2). The table is one positive
normalization sufficient for the construction; no general uniqueness result
for wiring rules is claimed.

Two useful conditional facts follow. Given an admissible replica pair, a
neutral edge with m=10 uses two five-blocks with probability 1/126; at m=12 it
does so with probability 2/77. All-pair probabilities are respectively 125/126
and 75/77. These probabilities concern the extra wiring, conditional on the
replicas. They are not unconditional current probabilities or independent
percolation parameters after the replicas are averaged.

## 3. Exact unsigned structure and normalization

Given n1,n2, choose a compatible partition pi_e at every edge with its weight
from (2), independently conditional on the replicas. Each local law has total
mass one. This augments mu_L tensor mu_L without changing its marginal.

Now forget the signs x and retain the structure T=(s,a,{pi_e}). The graph has
one vertex for each face with a_p>0, **not one vertex per distinguishable
token**. All tokens on a face are tied to the same sign variable. A pair joining
faces p,q imposes x_q=-epsilon(e,p)epsilon(e,q)x_p. Within a five-block the
relation is x_q=+epsilon(e,p)epsilon(e,q)x_p. A pair of tokens from the same face
therefore imposes x_p=-x_p and is inconsistent, rather than a new degree of
freedom. Repeated tokens inside a five-block are handled by the same rule.

A structure has zero weight if its sign relations are inconsistent. Otherwise,
let k(T) be the number of graph components. Each component has exactly two
signings, independently. With the face table and partial s=0 mod 5 imposed,
its unnormalized unsigned weight is

    w2(T)=2^k(T) product_p omega(s_p,a_p)
                   product_e lambda_(m_e,b(pi_e)).          (3)

**The partition sum of (3) is exactly Z_L^2.** To see this, first sum over the
2^k signings of each consistent structure. The inverse face map constructs
exactly the admissible replica pairs. At each such pair the sum of all wiring
weights is one by (2), independently at every edge. The remaining weight is
product_p w(n1_p)w(n2_p). Summing it is Z_L^2. This also proves that conditional
on T the component signs are independent uniform signs.

The statement includes every s permitted by the table and (1), not just a
fixed sum. Local sum constraints do not impose extra sign relations on d.

## 4. Integer currents and the full covariance identity

Choose a reference signing on each component K and put eta_K(p)=a_p x_p on
that component, zero elsewhere. Every pair cancels separately in its component,
and every five-block belongs entirely to one component. Hence

    J_K=partial eta_K/5

is an integer current. It is conserved because partial^2=0. Its total current
in every direction is zero on the periodic complex. If a component contains
no five-block it has J_K=0. The converse need not hold: opposite five-block
contributions can cancel. Even a neutral edge can contain two five-blocks,
and the two blocks may belong to different components.

Conditional on T,

    d=sum_K sigma_K eta_K,   j1-j2=sum_K sigma_K J_K,

with independent uniform signs sigma_K. Combining this with the ordinary
identity E[(X1-X2)(X1-X2)^T]=2 Cov(X) for independent equal-law copies gives

    Cov_mu(n) = (1/2) E_2aug sum_K eta_K tensor eta_K,
    Cov_mu(j) = (1/2) E_2aug sum_K J_K tensor J_K.           (4)

These identities hold on the whole finite torus, in the full original measure.
There is no empty-exterior, separate-patch-closure or fixed-fiber qualification.
They do not assert clustering or a numerical improvement over the one-copy
representation in [CONNECTED-CURRENT.md](CONNECTED-CURRENT.md).

## 5. Axial quotient and the exact factor one-half

The signed-slice argument of [SIGNED-SLICES.md](SIGNED-SLICES.md) extends to
eta_K in {-2,-1,0,1,2}; it uses its boundary, not ternarity. Set

    A_K(r)=sum_(x:x1=r) eta_K(p01(x)),
    B_K(r)=sum_(x:x1=r) J_K(e0(x)),   r in Z/LZ.

The transverse differences telescope, so A_K(r)-A_K(r-1)=5 B_K(r). Choose an
integer cyclic primitive H_K of B_K; it exists since sum_r B_K(r)=0. Then
A_K=5H_K+c_K. For every allowed nonzero t=2 pi k/L,

    F_etaK,01(t e1)=5 exp(-it/2) sum_r H_K(r) exp(-itr).

Define ell_K=min_(h in Z) sum_r |H_K(r)-h|. An integer median attains this
minimum. It is unchanged by the reference sign, the primitive constant and
cyclic origin. Subtracting any integer-closed filling changes A_K only by a
constant; this removes its nonzero axial response exactly. This algebraic
observation does not authorize changes to the configuration or its weight.

With the original convention lambda(t)=4 sin^2(t/2) and
chi_L(t)=S_j,00^L(t e1)/lambda(t), equation (4) yields

    chi_L(t)=(1/(2V)) E_2aug sum_K
                      |sum_r H_K(r) exp(-itr)|^2
            <= Xi_L^(2):=(1/(2V)) E_2aug sum_K ell_K^2.      (5)

Components with J_K=0 have ell_K=0, as do components whose projected B_K
vanishes. The original one-copy Xi_L and the new Xi_L^(2) are different
expectations. **Neither Xi_L^(2)<=Xi_L nor its reverse has been proved.**
No constant uniform in L is supplied for either moment.

## 6. A connection bound must count junction multiplicity

Let Jcal_e be the set of five-blocks at edge e; it has at most two elements.
For a block u let K(u) be its component. Define the nonnegative kernel

    P_L^(2)(e,f)=E_2aug sum_(u in Jcal_e, v in Jcal_f)
                                      1{K(u)=K(v)}.         (6)

This is a multiplicity-weighted expectation, not generally a probability.
Each J_K(e) is a signed sum of the five-blocks at e belonging to K. Thus (4)
and the triangle inequality give

    |Cov_mu(j_e,j_f)| <= (1/2) P_L^(2)(e,f).                (7)

Replacing the sum in (6) by a single-component event at each edge would lose
multiplicity and need not give (7).

For e=e0(0), let C_L(x)=Cov_mu(j_e,j_e0(x)). Global reversal, translations and
symmetry of covariance give an even real C_L; zero total orientation-zero
current gives sum_x C_L(x)=0. Consequently, for an allowed axis character,

    S_j,00^L(t e1)=sum_x [cos(t x1)-1] C_L(x).

Take centered integer displacement representatives on the torus. The elementary
integer inequality 1-cos(tm)<=m^2(1-cos t), followed by (7), implies

    0<=chi_L(t)<= (1/4) sum_x x1^2 P_L^(2)(e0(0),e0(x)).    (8)

All sums are finite-volume sums in the same exact measure. No infinite-volume
connection event or interchange of Fourier and volume limits has been used.
An evaluated uniform upper bound on (5) or (8) would control chi in every
already admitted ordered profile. Identifying an infinite-volume moment from
local convergence alone would still be invalid without tail control.

## 7. What this closes and what it does not

This establishes a normalized, all-volume positive two-replica wiring and its
full current-covariance formula. It closes the *representation* step: the
auxiliary formula no longer excludes the other replica sums or neutral
backgrounds. It does not close the *estimate* step. The occurrence and geometry
of the connected components in (5)--(8) have not been bounded uniformly.

In particular, the conditional edge mixtures in section 2 do not give a
subcritical branching process by themselves. Face signs are tied across edges;
the distribution of (s,a) is constrained by (1); neutral paths and cycles can
connect distant charged junctions. Applying conditional local probabilities
as independent full-measure transmission factors would repeat the gap exposed
by the earlier unsaturated-fiber obstruction.

A useful next analytic target is an exploration or switching estimate for
(6), with exact conditional completion weights, or an estimate of the signed
quotient (5) that avoids taking absolute values along whole neutral surfaces.
The present identity supplies the full law for such an estimate, not its
missing numerical constant. A separate macroscopic transverse lower contrast
is still required for b_lower>25 chi_upper. The shared local floor accepted
in v92 cannot supply that strict comparison by itself.

No existence or uniqueness of ordered profiles, rotational restoration,
spectral transfer, massless phase, physical photon or P1 closure follows.

## 8. Prospective finite audit protocol

The complete proof and `verify_replica_wiring.py` are to be committed publicly
and read back before the first scientific execution. Only static source review
and compilation have occurred while preparing this protocol. The author of
this continuation also wrote its verifier; no independent review is claimed.
This is a notes audit, not a new formal P-probe or two-architecture gate.

Run the pinned standard-library verifier once, with a 45-second execution
budget, in a Linux x86_64/Python 3.13.5 environment. Preserve first stdout,
stderr, exit status, elapsed time and input SHA-256 hashes, including a failure
or timeout. Do not silently change the frozen verifier or retry as a new first
run. Repository CI is not an independent execution of this notes verifier.

The expected checks, declared before execution, are:

1. All nine ordered single-face replica pairs and their weights/inverses.
2. Independent enumeration of all unordered labelled-token pair/five partitions
   for m=0,...,12, not merely substitution in the proof's factorial identities:
   27,237 partitions, 8,191 sign assignments, 1,719 admissible assignments.
   Every compatible-weight sum must equal the exact modulo-five indicator.
   The m=10 and m=12 conditional neutral mixtures are checked from enumeration.
3. Nine one-edge tied-face graph fixtures, including doubled tokens and
   difference-current magnitude two, plus one two-edge gluing fixture. Compare
   unsigned graph masses and every face covariance entry against direct sign
   enumeration. These are algebraic incidence fixtures, not whole four-tori.
4. A 21-face four-cup geometry: verify 32 degree-two and four degree-five edges,
   five neutral equality components of sizes 1,5,5,5,5, common generator boundary,
   and boundary squared zero. Enumerate its 53 standalone states and all 2,809
   replica pairs; compare 441 face covariance entries with the exact factor
   one-half. This is a small standalone complex, not enumeration of mu_L.

Any failed equality, unexpected census, exception, nonzero exit, nonempty
stderr or timeout fails the audit. No numerical extrapolation or fitting is
allowed. A passing audit corroborates the written finite algebra only; it is
not a test or proof of uniform Xi_L, Xi_L^(2), spatial decay or P1. The first-run
record, if obtained, will be added separately without editing these inputs.
