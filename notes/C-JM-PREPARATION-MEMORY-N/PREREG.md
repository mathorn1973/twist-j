# C-JM-PREPARATION-MEMORY-N: frozen scope and finite audit

Status: NON-CANONICAL incubation, L1. No authority or status promotion.
Owner: A. M. Thorn, session jm-preparation-memory-2026-10-20; issue #1677.
Public basis: main 75a7d64f29e37d740ba4895135d7a7b9bcaf162e, Public Canon v103.
Content 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66; Canon SHA256
 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. Normative hashes, ancestry and required checks passed.

This is a new candidate, not reopening a sealed probe. The proposed statements
are analytical predictions developed before this pin, not blind discoveries.
The finite verifier is to be frozen with this file before execution. Only exact
integers and Fraction are allowed in decision paths. One local x86_64 audit
is planned, not a second-architecture or independent-agent confirmation.

## Inputs, types and equality

The merged resultant-41 note supplies S=O5 x Z[M], its suborder R of index41,
and the comparison fields. Unpromoted conversation inputs are the oriented
quadratic report and the readout-cost proof. They are references, not authority:
source ZIP SHA256 c9987855b3cb4c1bc7470dfa826be62213fc13f6d7231f52e382d1d561283553
and adfa7f3ed69ae6547a4938d720631288b3180f60b6b286f6525ac2c79b3b9a39.
No successful publication of those two packets is assumed.

All necessary model data are restated here. In integral cyclotomic coordinates
z=(a0,a1,a2,a3,b0,b1,b2,b3), S is b1-b2-b3=0 mod3, and

 ell=(1,10,18,16,-1,-27,-32,-3),  z in R iff ell z=0 mod41,
 G=diag(5I4-ones4,4I4), q(z)=z^T G z,
 B_Q={z in S:0<q(z)<=Q}, Q an integer >=8.

Supply reference y_z=(1,z), Ghat=diag(1,G), A_z=1+q(z), and
rho_z=y_z y_z^T Ghat/A_z. Literal equality of the complete matrices and of
integral source labels is used. The reference, positive trace metric, tensor
composition of distinct emitted systems, effects, Born probabilities and
conditional independence within a prepared block are declared comparison
premises. No native U source, physical energy, random seed, apparatus, event
law, reset or cross-layer gate is derived.

## The two preparation contracts

For a probability distribution pi on a finite subset of B_Q define

 REDRAW_k(pi)=(sum_z pi_z rho_z) tensor-power k,
 HOLD_k(pi)=sum_z pi_z (rho_z tensor-power k).

REDRAW redraws the entire label independently for each emitted system. HOLD
selects the whole label once per k-system block and supplies k fresh pure
preparations conditional on it. Neither contract is a sequence of repeated
measurements on one undisturbed specimen. Repetition across blocks requires
an additional independent renewal premise. No map from an unknown single
specimen to arbitrary identical copies is allowed.

## Frozen claims and falsifiers

A. The known one-copy collision survives every REDRAW block and every
state-only measurement, but the following HOLD two-copy states differ.
Let v=(1,0,0,0,-1,0,0,0), q(v)=8; on labels +/-41v with weights1/2;
off labels +/-40v with total weight lambda=354161/735212 and +/-42v with
remaining weight, signs fair. In the rational two-coordinate basis (reference,v),
G2=diag(1,8). Put p_t=1/(1+8t^2) and
V=lambda(1-lambda)(p40-p42)^2. The two-reference-click gap is V>0. With the
full sign also held, their trace distance is 2V; the fixed rank-one effect
onto w=(8,0,0,-1) in G2 tensor G2 attains mean gap 2V. One copy is insufficient
and two suffice for nonzero statistical distinguishability of this pair,
not certain one-block classification. Exact fractions will be computed only
by the pinned audit. Falsifier: a failed identity, nonpositive V, or wrong
claimed two-copy polynomial/effect identity.

B. A complete one-sided detector exists for every B_Q with sufficiently long
HOLD blocks. Let C=ell G^-1 ell^T (predicted 19639/20),
m=floor(sqrt(C Q)/41), d=2m+1. For every integer j=-m,...,m put
L_j=(-41j,ell), u_j=Ghat^-1 L_j^T, E_j=u_j u_j^T Ghat/(u_j^T Ghat u_j).
The event YES means one click of E_j on each of d distinct supplied copies.
Its conditional probability is

 h_Q(z)= product_j (ell z-41j)^2 / [(C+1681j^2)(1+q(z))].

It is zero exactly on R within B_Q and strictly positive on every off-seam
label. It thus remains zero for every all-on HOLD mixture and positive for
every all-off HOLD mixture. A conservative uniform lower bound on the latter is

 beta_Q=1/[(1+Q)^d product_j(C+1681j^2)]>0.

A YES certifies off-seam only in this ideal model; NO is inconclusive. Blocks
redrawn independently from an all-off distribution have probability of no YES
at most (1-beta_Q)^N after N blocks. Effect precision, source errors and
reset must not be silently assumed: these are exact comparison effects.
Falsifier: wrong coefficient C, nonprojector, wrong positivity/complement,
failed seam-zero equivalence, or failure of the lower bound on any admitted z.

C. The exact-darkness block-length order is sharp, not the success probability
or number of blocks. For Q>=16, z_t=(1+t,0,0,0,1-t,0,0,0) has q=8+8t^2,
and belongs to R iff41 divides t. Any positive effect on k HOLD copies that
has zero probability for every on-seam source but positive probability for
every off-seam source must have

 k>=2 floor(sqrt((Q-8)/(8*41^2)))+1.

Reason to prove: applying its positive square root to y_t tensor-power k gives
a vector polynomial of degree at most k; more distinct zeros force it to vanish
identically on that entire line. Together with B, the minimal k in this exact
one-sided class is Theta(sqrt(Q)). At Q=14112, the predicted bounds are 3<=k<=181.
For the unbounded source no finite k can satisfy the same exact one-sided
contract. This does NOT rule out finite-error classification of a specified
pair, adaptive protocols with another complete contract, or other resources.
Falsifier: a counterexample in precisely the stated positive-effect class or
a defect in the polynomial-root argument.

D. An all-on REDRAW source can trigger the detector from B. Check the equal
mixture of z=(1,0,0,0,1,0,0,0) and z=41v, within Q=14112. Each held label has
one zero factor, but every REDRAW single-effect mean is strictly positive.
This is a change of preparation contract, not a false positive inside HOLD.

E. Supplying HOLD is a resource. No state-only quantum channel on the common
one-copy mixture can produce both different HOLD outputs. For exact reusable
pure programming with an isometry W(p_z tensor blank)=p_z tensor psi_z and
unchanged pure program, distinct emitted pure rays force orthogonal programs
by inner-product preservation. This is a scoped memory bound, not a theorem
about every possible physical preparation. A retained classical label with
controlled fresh preparation is a mathematical sufficient model, not native U.

## Finite audit plan

Use Fraction matrices for the known 2D/4D collision, projector identities,
the trace-distance polynomial certificate and the full eight-coordinate
Gram/inverse. Check all possible integer seam coordinates in the Cauchy
interval for Q in {8,16,14112}, by exact products, not a sample of sources.
Check source/projector controls on named seam/off-seam pairs and ternary
sources, and check the lower-bound polynomial interpolation at t=-41,0,41.
All universal conclusions must also have written proofs. No finite check is
presented as enumeration of every B_Q or every distribution.

Output must be deterministic, exit zero with empty stderr; retain the exact
output, script/prereg hashes, environment and command. Do not alter thresholds
or hide a mathematical failure. Packaging failures are distinct from an exact
counterexample. No measurement dataset is consumed. License: new original
work under the repository Apache-2.0 terms; external standard no-cloning
context is cited, not imported as code. No third-party source is vendored.
