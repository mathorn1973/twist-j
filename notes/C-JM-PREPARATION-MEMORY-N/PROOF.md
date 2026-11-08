# Preparation memory: identical marginals, distinguishable blocks

**NON-CANONICAL, L1. Candidate C-JM-PREPARATION-MEMORY-N.**
Analytical results: candidate-T. Finite exact audits: candidate-C.
Owner: A. M. Thorn, session jm-preparation-memory-2026-10-20, issue #1677.

## Result and boundary

A preparation source that redraws its entire label independently at every
emission is not equivalent to a source that holds one label while preparing
several distinct output systems. The previously exhibited opposite-seam
mixtures remain indistinguishable at every block length under REDRAW. Under
HOLD, their two-copy states differ exactly. More generally, on every complete
bounded source family B_Q there is an explicit finite, positive one-sided
measurement: an affirmative result is impossible for all on-seam sources
and has positive probability for every off-seam source. This remains true
for arbitrary mixtures whose label is held within each supplied block.

The minimum block length for this EXACT one-sided contract grows as
Theta(sqrt(Q)); a universal bound-free finite block is impossible. This is
not a sample-efficiency improvement over approximate two-sided discrimination.
The success probability can be very small. A physical repeatable source and
its retained preparation memory have not been derived.

## 1. Fixed source and adopted comparison model

Public authority was checked at main
75a7d64f29e37d740ba4895135d7a7b9bcaf162e, Public Canon v103. The normative
content/hash tuple is in PREREG.md. The resultant-seam note is merged; the
oriented-quadratic report and readout-cost proof are unpromoted conversation
references, not additional authority. Their source hashes are recorded in
PREREG.md. Their needed model definitions are restated here, so no missing
publication is treated as a theorem dependency or an available physical device.

Use integral cyclotomic coordinates z=(a0,a1,a2,a3,b0,b1,b2,b3). The source is
S=O5 x Z[M], not the whole maximal product, with exact membership

    z in S iff b1-b2-b3=0 mod3.

The additional seam is

    ell=(1,10,18,16,-1,-27,-32,-3),
    z in R iff ell z=0 mod41.

Choose G=diag(5I4-ones4,4I4) and q(z)=z^T G z. Both are comparison inputs;
q is not identified with physical energy. For integer Q>=8 freeze the ENTIRE
finite set B_Q={z in S:0<q(z)<=Q}. Supply a reference and positive metric

    y_z=(1,z), Ghat=diag(1,G), A_z=1+q(z),
    rho_z=y_z y_z^T Ghat/A_z.

These are rank-one Ghat-positive trace-one projectors. Distinct z have distinct
rays because their reference coordinate is fixed to one. This supply of a
reference is not free or derived from native U. The formula for probabilities
is the adopted Born comparison rule tr(rho E). All results stay in the same
L1 mathematical model; no L1-to-L6 occurrence gate is asserted.

When tensor powers below denote several output systems, ordinary state-space
tensor composition and conditional product preparation are ADDITIONAL model
premises. They are distinct from the earlier outer-record module
R tensor_Z conjugate(R). No new field or physical spatial dimension is inferred.
Rational operator formulas are sufficient throughout. An orthonormal real
chart is occasionally used for proofs, not as an arithmetic field extension.

## 2. Two complete preparation contracts

For any distribution pi on B_Q write bar rho_pi=sum pi_z rho_z. Define

    REDRAW_k(pi)=(bar rho_pi) tensor-power k,
    HOLD_k(pi)=sum pi_z (rho_z tensor-power k).

REDRAW independently redraws the entire label at each emission. HOLD chooses
one complete z per block and supplies k fresh systems in the corresponding
conditional product state. The reader does not receive z, q(z), or a seam bit.
HOLD does not mean measuring the same specimen k times. After a measurement,
the next output must be freshly prepared from the retained source setting.

Both expressions have the same one-system marginal. They are generally not
the same multi-system density. HOLD mixtures are separable across the outputs;
no entanglement is required to carry the source-memory correlations.

If pi and nu have bar rho_pi=bar rho_nu, then REDRAW_k(pi)=REDRAW_k(nu) for all
k by substitution. Every measurement on the available k-system state has the
same probabilities. A common state-only quantum channel, identical auxiliary
state, or fixed measurement protocol cannot turn this equality into inequality.
Conversely HOLD supplies additional correlations at the source; it is not a
postprocessing that recovers information from the already averaged density.

These statements are about complete preparation contracts, not an assertion
that a density operator has a uniquely correct hidden pure-state decomposition.
The latent z here is an independently specified source setting in the model.

## 3. Exact two-copy separation of the known collision

Let v=(1,0,0,0,-1,0,0,0), q(v)=8, and use the two-dimensional source span with
coordinates (reference,v) and metric G2=diag(1,8). Let

    p_t=1/(1+8t^2), sigma_t=(rho_(tv)+rho_(-tv))/2,
    lambda=354161/735212, 1-lambda=381051/735212.

The known one-copy identity is

    sigma_41=lambda sigma_40+(1-lambda)sigma_42.

The left source uses only +/-41v in R; the right uses only +/-40v,+/-42v
outside R. All have q<=14112. REDRAW therefore erases the distinction for
all block lengths. It does not erase it under the supplied HOLD contract.

For the effect P0 onto the reference, the probability of a click on each of
two held outputs is p_t^2, independent of sign. The right-minus-left gap is

    V=lambda p40^2+(1-lambda)p42^2-p41^2
     =lambda(1-lambda)(p40-p42)^2
     =(p40-p41)(p41-p42)
     =15936/1210262180216419 > 0.

This is the variance of a conditional response, not a difference of the
one-copy responses. Two supplied outputs already give nonzero statistical
separation. The sign may even be redrawn for this specific reference-only
test if the magnitude is held; the following full-state formula instead
uses the declared complete-label HOLD contract.

For its exact trace distance, use a proof-only orthonormal chart. Fair signs
held over the two copies give, in the order 00,01,10,11,

    Gamma_t = [[p^2,0,0,p(1-p)],
               [0,p(1-p),p(1-p),0],
               [0,p(1-p),p(1-p),0],
               [p(1-p),0,0,(1-p)^2]], p=p_t.

Equality of the first moment leaves a difference

    Delta=Gamma_off-Gamma_on
         =V [[1,0,0,-1],[0,-1,-1,0],[0,-1,-1,0],[-1,0,0,1]].

Its eigenvalues are 2V,-2V,0,0, hence half its trace norm is 2V. The projector
onto (|00>-|11>)/sqrt(2) attains this maximal event-probability gap. It has a
rational description in the original metric: project onto

    w=(8,0,0,-1), G2 tensor G2=diag(1,8,8,64), norm(w)=128.

Consequently the exact distance and optimal binary-effect gap are

    31872/1210262180216419.

This is small, not a practical high-contrast detector. One copy is exactly
insufficient and two give nonzero distinguishability for this pair; two do
not give a certain answer in a single block. In particular the on/off pure
rays have nonzero overlap, whose positive powers remain nonzero for every
finite number of copies. Perfect finite-copy discrimination is not inferred.

## 4. A universal finite one-sided detector under HOLD

The preceding two-copy result concerns one pair of mixtures. The next result
covers every distribution supported inside B_Q, without receiving its labels.

Compute from the fixed inverse metric

    C=ell G^-1 ell^T
     =(1^2+10^2+18^2+16^2+45^2)/5
       +(1^2+27^2+32^2+3^2)/4
     =19639/20.

Cauchy gives |ell z|^2<=C q(z)<=CQ. Put

    m(Q)=floor(sqrt(CQ)/41), d(Q)=2m(Q)+1.

For each integer j=-m,...,m independently define

    L_j=(-41j,ell), u_j=Ghat^-1 L_j^T,
    c_j=u_j^T Ghat u_j=C+1681j^2,
    E_j=u_j u_j^T Ghat/c_j.

All E_j are explicitly rational rank-one orthogonal projectors in Ghat.
They and I-E_j are positive. Their setting depends only on the frozen seam,
metric and Q, not on a successful measurement, unknown label, or source norm.
The coefficients are rational formulas of size polynomial in the setting
index; a Q-dependent exponentially precise lookup table is not hidden in them.
Their physical implementation and calibration are nevertheless unprovided.

On a fresh output conditionally prepared from z, the yes probability is

    p_j(z)=(ell z-41j)^2/[(C+1681j^2)(1+q(z))], 0<=p_j(z)<=1.

Use d distinct outputs from the SAME held preparation. On output j measure
the binary context (E_j,I-E_j). The declared affirmative event is that every
measurement returned yes. Every other full block is recorded as inconclusive;
no silent loss or discarded failure is introduced. The product effect is
positive, bounded by I, and requires no entangled measurement. Conditional
product preparation gives

    h_Q(z)=product_(j=-m)^m p_j(z).

If z is on-seam, ell z=41j for one j in the complete allowed interval, so
that factor is zero. If z is off-seam, every numerator is a nonzero integer
square and all denominators are positive. Thus exactly

    h_Q(z)=0 iff z in R, for z in B_Q.

This realizes a one-sided operational predicate in the ADOPTED comparison
model, unlike the earlier mere arithmetic reconstruction of an integral
record. It is not a perfect two-outcome classifier: an off-seam state may
produce an inconclusive block.

For every off-seam z, integrality and q(z)<=Q give the explicit conservative
bound

    h_Q(z)>=beta_Q
      =1/[(Q+1)^d product_(j=-m)^m(C+1681j^2)]>0.

For an arbitrary HOLD mixture with off-seam weight w_off,

    beta_Q w_off <= Pr(affirmative) <= w_off.

In particular every all-on mixture is dark, and every all-off mixture is
bright by at least beta_Q. Thus the two finite-support mixture classes no
longer have intersecting output density sets at this block length. This is
a theorem for supplied HOLD outputs, not a contradiction of the REDRAW
one-copy mixture obstruction.

## 5. Event cost, tolerances, and renewed blocks

The block length is not the total experimental cost. beta_Q is a very loose
bound and can be extraordinarily small. At Q=14112 this construction uses
181 outputs; the reduced Fraction for beta_Q has a 783-bit numerator and a
7055-bit denominator. This is only a certificate of positivity, not a usable
sample budget or an optimized apparatus proposal.

If independent fresh blocks are additionally supplied by an all-off source,
N blocks have probability of no affirmative event at most

    (1-beta_Q)^N <= exp(-N beta_Q).

Hence N>=ceil(log(1/eta)/beta_Q) is sufficient for error at most eta when
classifying the promised all-on versus all-off source. All-on remains dark
in the exact model. Independence across blocks is another explicit renewal
premise, not a consequence of held labels within a block.

The exact-zero property must not be mistaken for finite-error robustness.
If each actual conditional single-effect probability differs from the
specified p_j(z) by at most epsilon, and conditional product preparation
still holds, telescoping products bounds the affirmative-probability error
by d epsilon. More sharply, every on-seam z has a designated zero factor,
so its actual affirmative probability is at most epsilon. An all-off source
has probability at least beta_Q-d epsilon. These intervals are separated
when (d+1)epsilon<beta_Q. The bound must include source drift and reference
errors to the extent they affect those conditional responses. Arbitrary
correlated errors or loss of the held-label contract are outside this bound.
No nonzero device tolerance or attainable calibration precision is selected.

This discussion is a conditional error calculation, not a new empirical
claim or a replacement of the exactly frozen scientific tests.

## 6. Sharp order of the required exact-darkness block length

Let k_min(Q) be the least k for which some positive effect E on k supplied
identical anchored pure copies has zero response on EVERY on-seam z in B_Q
and strictly positive response on EVERY off-seam z. The class permits all
positive effects, including collective ones; it is not limited to the
product construction. The upper bound is k_min(Q)<=d(Q).

For Q>=16 consider the affine source line

    z_t=(1+t,0,0,0,1-t,0,0,0), t in Z,
    q(z_t)=8+8t^2, ell z_t=2t.

These points always satisfy the S congruence and are never zero. The on-seam
parameters within B_Q include t=41j with |j|<=n, where

    n=floor(sqrt((Q-8)/(8*41^2))).

There are 2n+1 such distinct parameters. The off-seam point t=1 is supported
for Q>=16. Strip off the positive normalization of each k-copy vector. Its
remaining vector Y_t=y_(z_t) tensor-power k is a vector polynomial in t of
degree at most k. Positivity implies

    <Y_t,E Y_t>=0 iff E^(1/2)Y_t=0.

Every coordinate of E^(1/2)Y_t is still a polynomial of degree at most k,
regardless of whether E's coefficients are rational. If k<2n+1, the 2n+1
on-seam roots force each coordinate polynomial to vanish identically. The
effect is then also dark at t=1, contrary to its stipulated off-seam response.
Therefore

    2 floor(sqrt((Q-8)/(8*41^2)))+1
        <= k_min(Q)
        <= 2 floor(sqrt((19639/20)Q)/41)+1.

Both bounds have order sqrt(Q). Thus k_min(Q)=Theta(sqrt(Q)) as Q grows,
for THIS exact one-sided class. The constants are not sharp. At Q=14112,

    3 <= k_min(14112) <= 181.

The lower bound can be seen without matrix square roots for k=2: the vector
Y_1 is the exact linear combination of Y_-41,Y_0,Y_41 with coefficients
(-20,1680,21)/1681. A positive effect annihilating those three on-seam vectors
also annihilates Y_1. This is consistent with section3: distinguishing one
specified pair of mixtures at k=2 is weaker than a universal exactly-dark
classifier for the full preparation family.

For unbounded Q there are infinitely many on-seam t values, so the same
polynomial argument rules out every fixed finite k for the exact one-sided
unbounded-source contract. It does not rule out approximate two-sided tests
on a finite class, variable-length procedures with another complete contract,
extra source records or differently typed apparatuses.

The earlier Q^2 worst-case sample scale concerned approximate pure-state
classification at fixed error. Our Theta(sqrt(Q)) concerns the length needed
for a NONZERO, possibly tiny one-sided detection probability. It does not
improve that earlier total sampling cost.

## 7. Why the memory premise cannot be omitted

Even a source using ONLY on-seam labels can trigger the section4 test under
REDRAW. At Q=14112 take equal weights on

    z0=(1,0,0,0,1,0,0,0), ell z0=0, q=8,
    z1=(41,0,0,0,-41,0,0,0), ell z1=82, q=13448.

Both are in R. Under HOLD each has its own zero factor, j=0 or j=2, so the
complete affirmative probability is zero. Under REDRAW every single-effect
mean (p_j(z0)+p_j(z1))/2 is strictly positive, since the two labels never
have a zero at the same setting. Their product is strictly positive.

The mathematics of the detector is unchanged. Its source-memory premise
has changed. Thus a verified source contract is not administrative metadata;
it is necessary to interpret its output. Same one-system marginals do not
certify retained labels, repeated preparation, or an entire joint law.

## 8. What a source must provide, and the copying boundary

A source specification sufficient for HOLD can be written as an extended
classical-quantum preparation:

    sum_z pi_z |z><z|_memory tensor rho_z tensor-power k.

Tracing out the memory yields HOLD_k. A classical register, fixed control
and fresh ready systems supply such a mathematical model. This is not an
implementation from J or U, nor a proof that the memory, reference, ready
systems, energy, clock, occupied archive and reset are physically available.
Its transition is a supplied preparation channel, not a closed reversible
physical dynamics. Completing that full account is the next separate problem.

A universal device that takes only the averaged one-system density cannot
construct both source-dependent HOLD states from section3: the input density
is the same, so linear state-only operations must give the same output.

Nor may one silently replace a retained preparation source by cloning an
unknown specimen. For a pure-state copier, inner-product preservation would
force c=c^2 (or, with additional output memory, |c|<=|c|^2) for two inputs
with overlap 0<|c|<1, which is impossible. This is the standard no-cloning
boundary; see Wootters and Zurek, Nature 299,802-803 (1982), DOI
10.1038/299802a0. It constrains the supplied quantum comparison model, not
every deterministic integer state-copying operation.

There is a sharp small resource lemma for one deliberately narrow source
class. Suppose an isometry exactly appends a fresh pure output while returning
the same pure preparation program:

    W(|p_z> tensor |blank>)=|p_z> tensor |psi_z>.

For two labels, inner-product preservation implies

    <p_z|p_w>=<p_z|p_w><psi_z|psi_w>.

Distinct output rays have overlap magnitude strictly below one, so their
program states must be orthogonal. A finite catalogue of M distinct emitted
rays therefore needs at least M mutually orthogonal program states in this
exact unchanged-program class. The bound concerns reusable pure programs;
it is not a universal lower bound for all destructive, approximate, mixed,
stochastic, changing-memory or native preparation mechanisms. A readable
program register is also a different receiver-access contract from an
unreadable but persistent source register.

## 9. Verification and disposition

The first preregistration and verifier were published before execution at
9c984ee82b8779ef2997355bc5985a00e261b35c. The second implementation and its
own pre-execution record were published at
749ef40745bbc794184aae519c8b89869131c288. The second audit knew the claimed
results and was written in this same session, with no import of verify.py;
it is not blind independent-agent confirmation.

Both were executed on one Linux x86_64 environment, Python3.13.5, using only
the standard library, exact integers and Fraction. Both exited0 with empty
stderr. ACTUAL.txt and SECOND-ACTUAL.txt contain the actual deterministic
outputs; RUN.md binds the scripts, pins and byte hashes. The finite checks
include 7873 possible integer seam coordinates across three complete Cauchy
intervals,181 rational projector identities,2162 admitted ternary controls,
the two-copy exact matrix identity, and a second scalar/polynomial audit of
all cut bounds for8<=Q<=20000. These do not enumerate every B_Q. Universal
conclusions are proved above; no theorem status is earned from sample size.

No predecessor pin, falsifier or claim has been altered. No Canon, registry,
frontier, gate or workflow changes. Ordinary notes-only CI checks repository
integrity and does not execute the scientific audits. The result is a new
conditional mathematical preparation contract and its exact boundaries,
not a native apparatus, Born derivation, measurement result, conserved energy
or physical occurrence law.
