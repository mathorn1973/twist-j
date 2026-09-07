# TRC1 composition and finite-ensemble identifiability

**NON-CANONICAL / CONDITIONAL MATHEMATICS / L1 ONLY / PROOF-FIRST.**

This argument composes the specified mathematical profile and classifies what
its chosen calibration can identify. It supplies no physical realization,
occurrence selection, Canon promotion or historical novelty claim. Finite
verifier audits do not replace the quantifiers below. Execution and acceptance
status belong to the separate run/result record; this proof is not a run.

The public basis is main `876726287c96d6c25a64029a339a99039bcfdd67`, Public
Canon v80. The definitions are [TRC1](../../notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md)
and [RRP1](../../notes/DECODER-RESERVOIR-PHYSICAL-PROFILE-1.md). The inherited
proofs are [transport](../P-DECODER-RETARDED-ENERGY-TRANSPORT-1/PROOF.md),
[coupling](../P-DECODER-RESERVOIR-COUPLING-1/PROOF.md) and
[quadratic partition](../P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/PROOF.md).
Their exact executable dependencies and the finite audit domain are frozen
separately in PREREG.md. No inherited source or conclusion is amended here.

## 1. Fixed source and complete conditional transition

A head is `h=(n0,x0) in N_0 x F_5^6`; its actual checkpoint at cut t is
`U^t(h)`. Read its first four coordinates once with the balanced lift
`(0,1,2,-2,-1)` to obtain `z in Z={-2,-1,0,1,2}^4`. The head, marking and
lift are choices. Later checkpoints label the history; they do not inject
another source. At arbitrary n0, the TRC1 quadratic comparison is its
declared anchored direct write, not a reset of the actual native counter.

Fix `c=(Gamma,q,N)`, where Gamma is a finite nonnegative rational field on
`D3={x in Z^3:sum x_i is even}`, positive on its support R, `q>0` is rational
and `N>=0` is an integer. Empty R is allowed. Context equality retains N.
These parameters select a reading; they are not additional inputs to U.

For `s=sum z_i`, inject at the five sites
`y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0))`:

```text
S(z)=sum_(j<5) ((z,0)_j-s/5) delta_(y_j),
G=I_4-ee^T/5, e=(1,1,1,1)^T,
m(z)=z^T G z=||S(z)||^2, P_0=(0,S(z)).
```

G is positive definite: its eigenvalues are 1/5 on span(e) and 1 on
e-perpendicular. This norm-exposed injection is inherited, not newly
derived from physical source preparation. Initialize heat and tape to zero.

The finite stencil D contains all signed coordinate permutations of
`(1,1,0),(2,0,0),(2,2,0),(3,1,0),(4,0,0)`, with shell weights
`(6,1,15,1,1)/324`. Write `c_d` for the resulting coefficients, so
`sum_D c_d=8/9`, and `L v(x)=sum_D c_d[v(x)-v(x+d)]`.
On a finite-support rational pair P=(u,v), the cold transition is

```text
w_x=[2v_x-(Lv)_x-(1-Gamma_x/2)u_x]/(1+Gamma_x/2),
b_x=-(w_x-u_x)/2   (x in R),     D_x=Gamma_x b_x^2,
P'=(v,w),         H'=H+D,        tape'=tape appended with b.
```

Every denominator is positive. With B={0} union D, successor support lies
inside `supp(u) union (supp(v)+B)`. Thus each finite cut has finite rational
state, without a periodic boundary substitution. For example, the support
after t steps is contained in the initial five sites plus t stencil steps.
Computing the inherited local energy/current also retains its stated halo.

The coupling proof, sections 1-3, gives the positive energy and cold balance

```text
E(u,v)=||v-u||^2/2+<u,Lv>/2 >=0,
E(P')+sum_R D_x=E(P).
```

Consequently induction proves `E(P_t)+sum_R H_x(t)=m(z)/2` and
`H_x(t)=sum_(j<t) Gamma_x (b_x^j)^2`. Tape and heat describe the same
stored energy; storing both does not add their energies twice. Each step
uses a fresh zero incoming slot and retains the old outgoing slots. The
inherited full-port inverse reconstructs earlier states from the signed
tape, not from heat alone. Finite cold capacity remains a chosen resource.

Put `C_x(t)=floor(H_x(t)/q)` and `r_x(t)=H_x(t)-q C_x(t)`.
Nonnegative deposits give nondecreasing integer counts and `0<=r_x(t)<q`.
For each step emit every ordinal from `C_x(t)+1` through `C_x(t+1)`,
ordered first by site and then ordinal. One accounting event is emitted per
coupled transition, including zero-crossing and multiple-crossing batches.

The complete transition record retains both pair snapshots, both apparatus
snapshots, signed b, deposits, heat/counts before and after, remainder,
crossings, h, c and the actual beginning/completed native checkpoints.
The apparatus contains `(h,c,t,tape,H)`, not the record itself. Thus these
value snapshots have no circular record reference. Model persistence checks
the old snapshot and returns the new one; append requires the next matching
source, context, cut and pair/apparatus values. Arbitrary incompatible
history/record pairs are outside this compatibility domain.

The executable event wrapper admits only generated MODEL events: its before
checkpoint, pair and apparatus must equal the boundary obtained by replaying
the declared source to that cut, and its after-values must equal the cold
step. A locally consistent transition from an unrelated pair is insufficient.
The broader class of arbitrary coherent cold states is not the wrapper's
event-admission domain. This restriction makes standalone persist/read
operations retain the same source ownership as the generated history.

**Composition.** At t=0 the unique prepared state satisfies every displayed
invariant. Given a coherent generated state with t<N, the local formula
uniquely gives w,b,D; the count rule uniquely gives the complete batch;
snapshot construction and compatible append uniquely give the next history.
Energy, tape equality, ordering, continuity and checkpoint labels are
preserved. Induction therefore defines one complete history through N for
every admitted head and context. At N, administrative END retains the
completed state and emits no further accounting event or crossing.

For z=0, all fields and deposits remain zero and there are exactly N
zero-crossing accounting events. N=0 gives the empty history. Empty R gives
empty port vectors and no threshold crossings. No case is discarded or
renormalized. Rereading an existing model record is the identity on that
record; it does not append another source interaction. RESET_REQUEST is
disabled with unchanged state. This is not the reset codomain required by
physical contract #539 and proves no physical nondisturbance or erasure law.

Prefix consistency first means truncation inside one fixed context. If a
longer horizon is selected, the wave/tape/heat/crossing prefix agrees, but
literal full records contain the changed N in their context. Comparing those
records requires explicit transport of context references, not false literal
equality. One update per U label is a clock convention, not an intertwining
theorem or a physical time calibration.

## 2. Visible histories and the imported ensemble

The selected visible packet retains the fixed context, relative cut,
NO/SINGLE/MULTIPLE_CROSSING category, site multiplicities and ordinal ranges.
It discards head/checkpoint identity, signed fields, tape and snapshots.
In particular, its no-crossing category does not identify zero source.
These observations are MODEL packets; no FOREIGN_NIST or other detector
record becomes a model packet by changing its tag.

For fixed c and relative cuts, the visible history depends only on z.
Linearity of preparation and the cold recurrence gives
`P_t(-z)=-P_t(z)` and `b_t(-z)=-b_t(z)` by induction. Deposits, heat,
counts, remainders and crossings are therefore identical for z and -z.
On Z there are 625 points, exactly one fixed point of this involution and
312 nonzero pairs. Hence at most 313 distinct complete visible histories
occur for any fixed context/horizon. This is an upper bound, not an exact
count or a dimension claim. It does not identify signed tapes, full records,
native checkpoints or arbitrary other readings. It also does not follow that
every distinct antipodal class is separated by this visible projection.

Fix a nonempty finite list of heads `h_1,...,h_M` and a rational probability
vector p. Zero weights can be omitted from the TRC1 positive-weight encoding.
Draw one initial head by this stipulated ensemble and then evolve its whole
complete state deterministically. If `v_i^(k)` is its visible k-prefix, then

```text
Pr(prefix=y)=sum_i p_i 1[v_i^(k)=y],   0<=k<=N.
```

This finite pushforward is nonnegative, normalized and prefix-consistent:
every head has exactly one prefix and one next packet. Conditional next
probabilities use the surviving weights after an observed prefix; a zero
denominator is IMPOSSIBLE_UNDER_FIXED_MODEL. Resampling the original p every
tick changes the joint law. No independence between repeated preparations,
empirical convergence, source probability from U or Born law follows from
this elementary conditional construction.

The fair mixture of zero and 2e0, with origin conductance 1, q=1/16 and
N=2, gives a concrete product-marginal control. Section 4 proves a positive
first crossing for 2e0. For its second step, write `H_op=2I-L`. Its diagonal
coefficient is 10/9 and its nonnegative off-diagonal coefficients are at
most 5/108. Initially `v_0(0)=8/5` and `v_0(x)<=0` off the origin; hence
`w_0(0)=1421/1215` and `w_0(x)<=2/27` off the origin. Consequently
`(H_op w_0)(0)<=14930/10935`, and the second outgoing amplitude satisfies
`b_1=[2v_0(0)-(H_op w_0)(0)]/3>=20062/32805>1/4`.
Its deposit exceeds q, so the second step also has a new crossing. Both
time marginals thus separate zero from 2e0. The joint law assigns mass 1/2
to each of two complete words; their marginal product assigns mass 1/4
also to the two mixed words, which the once-selected source never emits.
This product samples hypothetical readings of separate precomputed
trajectories. It is not a physical protocol replacing the source while
retaining the apparatus, nor an asserted model of physical resampling.

## 3. Exact classification of calibration sufficiency

Let `A in Q^(r x M)` list any finitely many prescribed calibration readings
on the same heads, and let `B in Q^(s x M)` list prescribed validation
readings. Rows can be rational scalar readings or indicators of complete
visible outcomes. For a mixture p their expectations/laws are Ap and Bp.
Set `C=[1^T;A]`, including the normalization row even if redundant.

**Theorem.** The following conditions are equivalent:

1. For every two rational probability vectors p,q, `Ap=Aq` implies `Bp=Bq`.
2. `ker C subset ker B` over Q.
3. Every row of B lies in the rational row space of C.
4. There is a rational matrix K with `B=KC`.

These conditions are also equivalent to condition 1 for real probability
vectors. They concern all mixtures over this frozen finite head list, not
all physical preparations or all decoder families.

**Proof.** Conditions 3 and 4 are the definition of row span. Gaussian
elimination identifies the annihilator of ker C with row(C), proving 2 iff
3. If 4 holds, `Bp=K(1,Ap)^T`, proving condition 1 over either field.

Conversely, suppose 2 fails. A rational nullspace basis supplies a rational
vector d with `Cd=0` and `Bd!=0`. In particular `sum_i d_i=0`.
Start at the interior vector `p0_i=1/M`. Choose a positive rational
epsilon with `epsilon max_i |d_i|<1/M`; for example
`epsilon=1/[2M(1+max_i |d_i|)]` works. Then `p+=p0+epsilon d` and
`p-=p0-epsilon d` are strictly positive rational probability vectors.
They have equal A calibration but their B readings differ by
`2 epsilon Bd!=0`. This contradicts condition 1 even on interior rational
mixtures, and proves the remaining directions. For M=1 the kernel is zero
and the conclusion holds as well. No fitted numerical tolerance is used.

When the criterion passes, `K(1,Ap)^T` is the identified affine prediction
on the attainable calibration image. K need not be unique or nonnegative
on arbitrary inputs outside that image. This does not certify arbitrary
calibration numbers as attainable or provide stability under measurement
error. For one fixed calibration y, the sharper condition is simply that
B is constant on `{p>=0:Cp=(1,y)^T}`. Global failure does not imply ambiguity
on every boundary fibre; infeasible y instead rejects this finite model.

For outcome-indicator B, its columns are the deterministic output vertices
and achievable laws form their convex hull. Choosing p after observing a
validation law inside this hull is fitting. It is not an independent
prediction, even when every arithmetic step of the pipeline is exact.

## 4. Exact end-to-end negative and positive examples

Use heads at n0=0 with the displayed first four coordinates and last two
coordinates zero. Let `e0=(1,0,0,0)` and `e1=(0,1,0,0)`. They are balanced
heads in the actual source domain. The inherited algebraic scalar targets are

```text
L_QDD=ee^T/20, H_QDD=I_4-ee^T/4, L_QDD+H_QDD=G.
```

Both sources have total m=4/5, LOW weight 1/20 and HIGH weight 3/4, hence
normalized weights `(1/16,15/16)`. The calibration here contains these
scalar weights, NOT the full QDD density: their density records differ.
Repeating or normalizing these scalar rows does not distinguish the heads.

Fix the single origin port with conductance g=1, N=1 and q=1/16. For the
first step put `H_op=2I-L`. The inherited partition proof, section 4, gives

```text
(H_op S(z))_0=k z, k=(1421,-349,-349,-349)/1620,
b_0=-k z/(2+g),        D_0=g(k z)^2/(2+g)^2.
```

Thus the two deposits are `1421^2/4860^2` and `349^2/4860^2`.
Writing `a=1421^2=2019241`, `b=349^2=121801` and
`d=4860^2=23619600`, exact integer comparisons give
`d<=16a<2d` and `0<=16b<d`. The threshold counts are therefore 1 and 0.
The corresponding visible one-step categories differ along the whole chain.

With columns ordered (e0,e1), C has rank 1 and kernel span(1,-1).
Take B as the two indicators COUNT=0 and COUNT=1. Its columns are distinct
unit vectors and it has rank 2. The two interior mixtures
`p=(1/3,2/3)` and `q=(2/3,1/3)` have identical scalar calibration but
`Pr(COUNT=1)=1/3` and `2/3`. This is an analytic fixture, not a fitted or
experimentally measured discrepancy. It does not contradict contextual
readings: the selected apparatus reads more than the selected calibration.

An additional scaling example uses heads e0 and 2e0, g=1, N=1, q=1/8.
Their normalized LOW/HIGH weights agree, but their totals are 4/5 and 16/5
and their absolute branch weights differ. Calibration in this example
therefore omits those absolute quantities. The deposits are a/d and 4a/d.
The inequalities `0<=8a<d` and `2d<=32a<3d` give counts 0 and 2.
For the same mixtures p,q, `Pr(COUNT=2)=2/3` and `1/3` respectively.
This exhibits why normalization alone can hide a threshold-relevant scale.

There is also a positive, explicitly selected control. On either two-head
family, append calibration row `(1,0)`. Together with normalization it has
rank 2, so its kernel is zero and it determines every B on those heads.
For the first family it directly supplies the mixture mass of e0. This is
a sufficient mathematical calibration, not a physically obtained source
indicator, a derivation of its accessibility, or a new selector from U.

## 5. Inherited obstruction to sharp energy postprocessing

This composition retains the earlier uniform obstruction; averaging must
not conceal it. On any fixed context with active origin and N>=1, write
the fine deposit forms `M_(t,x)` and actual residual-energy form `R_N` in
the normalization twice-energy, so

```text
M_(t,x)>=0, R_N>=0, sum_(t<N,x in R) M_(t,x)+R_N=G.
```

Positivity follows from the inherited energy proof, not a sampled fit.
Admit exactly state-independent complete nonnegative two-output processing:
one real coefficient `a_j in [0,1]` per fine form and residual, with
`A_LOW=sum_j a_j M_j`, `A_HIGH=sum_j(1-a_j)M_j`.
The first origin form is `2g/(2+g)^2 k^T k`, nonzero and positive
semidefinite for g>0.
It is strictly positive both on `z_H=(1,-1,0,0)` and `z_L=(1,1,1,1)`:
`k z_H=1770/1620!=0` and `k z_L=374/1620!=0`.
But the LOW target vanishes on z_H and HIGH target vanishes on z_L.

If both targets were reproduced on this source class, positivity at z_H
would force the first slot's LOW coefficient to be 0. Positivity at z_L
would force its HIGH coefficient to be 0, hence the LOW coefficient to be
1. This contradiction proves impossibility for the entire stated processing
class, at every positive finite horizon and positive origin conductance.
Both witness sources belong to the balanced head domain. No enumeration of
coefficient samples or cancellation by other positive slots repairs it.

This theorem is inherited rather than newly discovered. It does not cover
all physical apparatuses, altered couplings, coherent amplitude transforms,
nonlinear/source-dependent processing or discarded-output renormalization.
The cases N=0 or inactive origin are outside this proof, not established
positive realizations. The new finite-ensemble criterion neither strengthens
this negative claim to all physics nor evades it with averaged frequencies.

## 6. What an independent physical prediction would require

An executable conditional composition can establish its exact formulas and
identifiability boundaries. It cannot issue physical encodings, instruments,
ready states, source opportunities, retained records or occurrence laws.
In particular, native provenance labels are not physical time calibration;
fresh cold slots and passive queries remain mathematical assumptions.

TRC1 already gives an example of a separate prospective response test. For
a prepared zero pair and an independently calibrated warm pulse A!=0 at
one port, the general coupling predicts `r=b/A=(2-g)/(2+g)`, so
`g=2(1-r)/(1+r)`. A different cold source e0 then predicts
`b=-1421/[1620(2+g)]` and its corresponding deposit and threshold crossings.
Using the first domain for calibration and the second for held-out
validation would have predictive content only with independently fixed
physical source/port/clock/observable maps, threshold, uncertainties and
selection rules. Energy-only calibration has the inherited g versus 4/g
ambiguity; choosing a branch from the desired output is not calibration.

No such physical realization or measurement is asserted here. A measured
response outside a preregistered joint prediction/error set could reject the
specified admitted profile; absence of the physical dictionary is STOP.
The finite matrix theorem likewise concerns an exact known calibration,
not an uncertainty model for estimated frequencies. Physical sampling,
L1-to-L5/L6 gates, terminal-event semantics, complete apparatus-family scope
and #539 reset conformance remain unresolved. Neither Mark2024 nor NIST
records supply these identities merely by sharing a packet interface.
