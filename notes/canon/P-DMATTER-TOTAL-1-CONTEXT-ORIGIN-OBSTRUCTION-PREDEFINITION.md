# P-DMATTER-TOTAL-1 Context-Origin Obstruction and Adjacent-Supply Predefinition (NON-CANONICAL)

```text
STATUS:                 EXACT DEFINITION-ONLY RESULT /
                        UNADOPTED ADJACENT-SUPPLY CANDIDATE
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / L1 /
                        QDD BETA CONTEXT ORIGIN
PUBLIC CANON:           Public Canon v24
PUBLIC CANON TAG:       canon-v24
PUBLIC MAIN BASE:       f6f797739be21acfa70851be544c994ea17b7f5a
PUBLIC MAIN TREE:       cea987dd32b8717d5c0111edd933feb8be3fe4df
IMMEDIATE PREDECESSOR:  P-DMATTER-TOTAL-1-BETA-PREP-SUPPLY-
                        PAIR-INPUT-OWNER-FREEZE.md
PREDECESSOR BLOB:       7ff1f3925bf7b284bacabf22c3aa34fb4921797f
PREDECESSOR SHA-256:    30dab9c4b38505fd3b920ff628054c908b780b5b116dc9fdfdebb19b8946554b
PREDECESSOR BYTES:      38293
CLAIM ISSUE:            107
CLAIM COMMENT:          5091489547
OWNER DECISION:         NONE IN THIS NOTE
FORMAL RUN:             NONE
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
NORMATIVE CHANGE:       NONE
DEPENDENCY CHANGE:      NONE
GATE TABLE CHANGE:      NONE
STATUS CHANGE:          NONE
QDD STATUS:             O / STOP, unchanged
READY-FOR-CLASSIFICATION:
                        NO
```

This note closes one ambiguity left by the immediate predecessor. A map from
one source orbit into the two-role conditional input is mathematically easy to
write, but the frozen types do not select one. Moreover, if the evaluation
role is required to mean the actual next checkpoint, the source cannot forget
the odometer phase.

The note proves those two statements exactly and then records a full-`Omega`
one-step phase quotient and adjacent-supply candidate. The candidate is not a
physical occurrence law and is not owner-adopted here.

## 0. Firewall

The following are failures of this note:

```text
MAP-NONEXISTENCE-OVERCLAIM
    the absence of an adopted map is reported as the absence of every
    set-theoretic or typed map;

CONDITIONAL-OCCURRENCE-COLLAPSE
    the full Cartesian PairInput_beta carrier is reported as physically
    occurring, sampled, independent, uniform, or distributed;

ROLE-TAG-COLLAPSE
    PREP_SOURCE(lambda), PREPARE_BETA(PREP_SOURCE(lambda)), and
    EVAL_SOURCE(kappa) are identified;

DIAGONAL-POSTHOC-PROMOTION
    the same-source diagonal is adopted because its already known agreement
    behavior is favorable;

CHECKPOINT-SUCCESSOR-FACTORING
    an actual one-step successor is claimed to be a function of the
    checkpoint alone on the full forward carrier;

REANCHORING-TAIL-COLLAPSE
    the fresh anchored orbit kappa_(F_t(x)) is identified with the actual
    tail of a state at arbitrary counter n;

CANDIDATE-ADOPTION
    AdjacentInput_beta is called physical, canonical, unique, or occurring
    without a later explicit owner ruling;

STATUS-PROMOTION
    QUADRATIC-DECODER-DATA is moved from O / STOP, or any public table,
    dependency, gate, or completion field is filled.
```

A probability assignment on `PairInput_beta` does not supply a deterministic
map `S->PairInput_beta`. Any stochastic alternative would require its own
typed kernel, sampler, zero handling, and occurrence semantics and is outside
this note. Conversely, a typed deterministic source map does not define a
probability law.

## 1. Frozen input types

Retain the proposal-local anchored source carrier

```text
X  = F_5^6,
K0 = { kappa_x = (U^n(0,x))_(n>=0) : x in X }.
```

Pointed-sequence equality gives

```text
kappa_x Eq_K0 kappa_y iff x=y,
|K0|=|X|=5^6=15625.
```

Write the already frozen pair constructor as

```text
q(lambda,kappa)
  = (
      PREPARE_BETA(PREP_SOURCE(lambda)),
      EVAL_SOURCE(kappa)
    )
  in PairInput_beta.
```

The first component is a preparation procedure. The second is an evaluation
context. Their payloads have the same carrier `K0`, but the role-tagged types
are disjoint.

The immediate predecessor freezes

```text
|PairInput_beta|=15625^2=244140625
```

as a conditional full Cartesian carrier. It freezes no physical occurrence
support and no map from one public decoder input to this carrier.

## 2. Single-source decomposition and cardinal bound

Let `S` be any typed source carrier. Every total map

```text
C : S -> PairInput_beta
```

is uniquely equivalent to a pair of total payload maps

```text
lambda_C : S -> K0,
kappa_C  : S -> K0
```

through

```text
C(s)=q(lambda_C(s),kappa_C(s)).
```

This follows only from the tagged-product equality and the constructor
bijections already frozen. It is not a physical selection theorem.

For `S=K0`, every deterministic single-orbit supply therefore has

```text
|Image(C)| <= 15625
             = |PairInput_beta| / 15625.
```

Thus the image of any single-valued map `C:K0->PairInput_beta` contains at
most 15,625 pair inputs, namely at most `1/15625` of the conditional
Cartesian carrier. This is only an image-cardinality statement. It says
nothing about relation-valued, stochastic, or time-indexed occurrence support
and does not identify any such image as physical occurrence.

## 3. What constructor-only naturality would select

This section states a conditional criterion; it does not add that criterion
to Public Canon.

Let every permutation `pi` of `K0` induce the constructor action

```text
pi . PREPARE_BETA(PREP_SOURCE(lambda))
  = PREPARE_BETA(PREP_SOURCE(pi(lambda))),

pi . EVAL_SOURCE(kappa)
  = EVAL_SOURCE(pi(kappa)),

pi . q(lambda,kappa)=q(pi(lambda),pi(kappa)).
```

This is an action on the constructor/equality reduct only; it does not assert
covariance of the full `RunPrep_beta` semantics. Call a supply
`constructor-only natural` when

```text
C(pi(lambda)) = pi . C(lambda)
```

for every `pi` in `Sym(K0)`.

By the decomposition above, both payload self-maps commute with every
permutation of `K0`. A self-map `f:K0->K0` with that property is the identity:
the stabilizer of `lambda` fixes `f(lambda)`, while the only point fixed by
the whole stabilizer is `lambda`. Therefore

```text
lambda_C = id_K0,
kappa_C  = id_K0,
C        = C_diag,

C_diag(lambda)=q(lambda,lambda).
```

So full relabeling naturality leaves exactly the same-source diagonal.
However, the diagonal is already frozen as a mandatory negative control, not
as the physical occurrence law, and its agreement behavior was known before
this note. It can be adopted only by a new owner action with a post-hoc audit.
There is consequently no presently adopted constructor-only natural supply.

## 4. Exact nonuniqueness invisible to the successful state entry

Existing algebra already supplies a second exact binding. Define

```text
nu : K0 -> K0,
nu(kappa_x)=kappa_(-x),
```

where negation is coordinatewise in `F_5^6`, and define

```text
C0(kappa_x)=q(kappa_x,kappa_x),
C1(kappa_x)=q(nu(kappa_x),kappa_x).
```

Both maps are total, exact, parameter-free, and compatible with the tagged
zero branch. They are distinct on 15,624 of the 15,625 source points and on
all 15,600 successful source points.

The symmetric integer lift in `beta_Q` gives

```text
beta_Q(nu(kappa_x)) = -beta_Q(kappa_x).
```

Hence the zero/nonzero decision agrees, and on every successful source

```text
rho_beta(nu(kappa_x)) = rho_beta(kappa_x).
```

The already frozen successful entry therefore satisfies

```text
EnterPair_beta(C0(kappa_x))
  = EnterPair_beta(C1(kappa_x))
```

for every successful `kappa_x`, even though `PairInput_beta` and the tagged
`RunPair_beta` results retain different preparation origins.

This is an exact nonuniqueness of typed proposal-local candidate bindings
with equality at one downstream readout. It is not a classification of physical
architectures or decoder universality: physical occurrence, the complete
`MatterData` write, and the complete decoder remain open.

## 5. The checkpoint cannot carry an actual successor law

The public autonomous update uses

```text
Omega = N_0 x X,
theta_n = s_2(n) mod 2,
F_t(x) = g_((z_6(x)+2t) mod 5)(x),
U(n,x) = (n+1,F_(theta_n)(x)).
```

The public generator trace laws give

```text
z_6(F_0(x)) by input sheet z:  0 4 0 4 4,
z_6(F_1(x)) by input sheet z:  2 1 1 3 1.
```

The two output sheets differ in every column. Therefore

```text
F_0(x) != F_1(x) for every x in X.                    (1)
```

`CARRY-J-CHECKPOINT [T]` proves on the full forward carrier that, for every
genesis seed,

```text
psi_4=psi_6.
```

The registered odometer definition independently gives

```text
theta_4=1,
theta_6=0.
```

Let their common checkpoint be `x`. The next checkpoints are

```text
psi_5=F_1(x),
psi_7=F_0(x),
```

which are unequal by (1). Thus no self-map

```text
Next_X : X -> X
```

can satisfy `Next_X(psi_n)=psi_(n+1)` at every state of the declared full
forward carrier.

Consequently, a supply whose evaluation payload is defined to be the actual
one-step successor cannot factor through the checkpoint, or through the
checkpoint label `kappa_x`, alone. At least the branch information forgotten
by that projection must remain in the source.

## 6. Full-Omega one-step phase quotient and candidate

Define the proposal-local algebraic source carrier

```text
AdjSource_beta = F_2 x X
```

and the total public-state projection

```text
PhaseCheckpoint_beta : Omega -> AdjSource_beta,
PhaseCheckpoint_beta(n,x)=(theta_n,x).
```

This projection is surjective as a carrier map: `n=0` supplies phase zero and
`n=1` supplies phase one for arbitrary `x`. This is a statement about the
declared state carrier `Omega`. It does not say that the image of the
anchored full forward carrier is all of `AdjSource_beta`. A later occurrence
ruling must choose and freeze its source support.

Nor is `PhaseCheckpoint_beta` a dynamic factor. For example, counters `n=0`
and `n=5` have the same current bit but different next bits. The quotient
`AdjSource_beta` is sufficient for one displayed update `F_t(x)`; it does not
retain event identity or define an occurrence history.

Define

```text
AdjacentContext_beta(t,x)
  = (
      PREP_SOURCE(kappa_x),
      EVAL_SOURCE(kappa_(F_t(x)))
    ),

AdjacentInput_beta
  = MakePairInput_beta o AdjacentContext_beta.
```

This is a total exact map

```text
AdjacentInput_beta : AdjSource_beta -> PairInput_beta.
```

The corresponding state-indexed composite is

```text
StateAdjacentInput_beta
  = AdjacentInput_beta o PhaseCheckpoint_beta
  : Omega -> PairInput_beta.
```

To expose the still-missing one-orbit type, define only proposal-locally

```text
Khead_beta
  = { Orb(omega)=(U^m(omega))_(m>=0) : omega in Omega },

Head_beta : Khead_beta -> Omega,
Head_beta(Orb(omega))=omega,

OrbitAdjacentInput_beta
  = StateAdjacentInput_beta o Head_beta
  : Khead_beta -> PairInput_beta.
```

Equality on `Khead_beta` is pointwise equality of the displayed pointed
sequences. `Head_beta` is then total and equality-compatible because the
zeroth sequence entry is its head.

Public Canon names `K` as the set of forward `U`-orbits, but v24 does not
freeze whether its registered orbit objects are pointed sequences with a
zeroth entry, nor a completion-grade representation/equality ID,
`head:K->Omega`, orbit-position field, or `K->K0` reanchoring ID. Therefore
this note does not identify `Khead_beta` with public `K`, bind it to
`dom(D_matter)`, or fill `single_orbit_to_pair_map_id`. It exhibits the exact
candidate data those bindings would need.

The displayed algebraic map uses no new selector, fit, randomness, external
clock, file, environment value, network value, or second free context. It
deliberately reads the registered internal counter only through
`n |-> theta_n`. This proposed counter read is not owner-adopted here and
does not amend the predecessor denylist. The displayed candidate-map
endpoints are proposal-locally L1; the public `DEF-DECODER-MATTER` / QDD
binding remains `MULTI` and unresolved.

Because the first payload recovers `x` and (1) separates the two branches,
`AdjacentInput_beta` is injective. Its exact image counts are

```text
|Image(AdjacentInput_beta)| = 2*15625 = 31250,
zero-preparation inputs    = 2*25    = 50,
successful inputs          = 2*15600 = 31200.
```

This image is an externally defined graph support inside the unchanged full
Cartesian `PairInput_beta`. It adds no internal lambda-kappa constraint to
the conditional interface and supplies no frequency or distribution.

Define the head-checkpoint reanchoring candidate

```text
ReanchorHead_beta(Orb((n,x)))=kappa_x.
```

Section 5 proves that `OrbitAdjacentInput_beta` cannot descend through this
map on the full forward carrier. There is no total

```text
CheckpointAdjacentInput_beta : K0 -> PairInput_beta
```

for which

```text
OrbitAdjacentInput_beta
  = CheckpointAdjacentInput_beta o ReanchorHead_beta
```

and whose evaluation payload is the actual one-step successor at every
occurrence. This is the precise nonfactorization result: one pointed orbit is
sufficient for the candidate, while its `K0` reanchoring is not.

## 7. Semantic and reanchoring boundary

The displayed candidate packages several unadopted semantic choices:

```text
1. use the pointed-orbit head as the relevant source position;
2. assign the current checkpoint to preparation;
3. assign one forward U-step to evaluation;
4. retain the ordered current-to-next role orientation;
5. genesis-reanchor both checkpoint payloads through x |-> kappa_x.
```

Once this package is chosen, `U` fixes `F_t`; `U` does not select the package
itself. The candidate is structure-using, not structure-forced.

The same-source diagonal, reversed adjacent roles, and other explicitly
structured graphs remain distinct rivals. The public update alone does not
rank them as preparation/evaluation dictionaries.

Furthermore,

```text
kappa_(F_t(x))=(U^m(0,F_t(x)))_(m>=0)
```

is a fresh `K0` anchor whose initial checkpoint is `F_t(x)`. This note does
not identify it with the actual tail beginning at counter `n+1`. The current
beta and projected-Householder rules read the anchored source through its
initial checkpoint, but a future rule that reads later orbit entries must
revisit this reanchoring.

## 8. Single-current-Q boundary

A successful public collision gives one further exact boundary. Take

```text
psi_0=(0,0,0,1,2,0).
```

Its orbit has

```text
psi_4=psi_6=x=(0,0,0,1,0,3),
beta_Q(kappa_x)=(0,0,0,1)!=0.
```

Under the unadopted `AdjacentInput_beta` candidate, the two actual successor
checkpoints would select different projected-Householder high lines:

```text
theta_4=1:
    F_1(x)=b(x)=(0,4,0,0,0,2),
    beta_Q(kappa_(F_1(x)))=(0,-1,0,0),
    primitive high line=(1,-3,1,1);

theta_6=0:
    F_0(x)=e(x)=(2,1,3,3,2,3),
    beta_Q(kappa_(F_0(x)))=(2,1,-2,-2),
    primitive high line=(9,5,-7,-7).
```

Under that same conditional candidate, the selected instruments differ.
Applied algebraically to the same prepared current ray, their high-outcome
post-state rays are respectively proportional to

```text
(5,-3,5,-7),
(75,19,-149,55),
```

so the post-states differ as well. Nevertheless both instruments have the
same high effect `E_high`; the Born high probability of the current state is
`15/16` in both cases. The current checkpoint and its current
`Qcan(beta_Q)` datum are identical.

This does not fire `QUADRATIC-DECODER-DATA`. Its public scope explicitly
excludes post-state instrument uniqueness, and the current-Q effect/Born
read survives this witness. The exact boundary is narrower:

```text
a phase-sensitive adjacent evaluation instrument or post-state cannot be
added to the fields claimed to factor through current Q alone.
```

Such fields cannot enter the current-Q-factorized `D_quadratic` /
`MatterData` manifest. They must remain outside that manifest unless a
separately registered typed scope, domain, equality, dependency graph, and
factor datum, such as an explicit `(Q_current,Q_successor)` input, is adopted.
Otherwise the adjacent proposal routes negatively for current-Q
factorization. `AdjacentInput_beta` remains only a conditional candidate.

## 9. Dependencies, hidden inputs, layers, and gates

The exact algebraic dependencies branch as follows:

```text
DEF-CHECKPOINT
  + DEF-ODOMETER-ORBIT
  + DEF-KERNEL-GENERATORS
  + DEF-SELECTOR
  -> DEF-AUTONOMOUS-STATE / U.

DEF-ODOMETER-ORBIT
  -> theta_n
  -> PhaseCheckpoint_beta.

U
  -> F_t;

U
  -> the predecessor-adopted proposal-local K0 genesis map
     x |-> kappa_x;

U
  -> Khead_beta and Head_beta;

F_t
  + the proposal-local K0 genesis map
  + PREP_SOURCE and EVAL_SOURCE
  + MakePairInput_beta
  -> AdjacentInput_beta;

PhaseCheckpoint_beta
  + AdjacentInput_beta
  -> StateAdjacentInput_beta;

Head_beta
  + StateAdjacentInput_beta
  -> OrbitAdjacentInput_beta.
```

The checkpoint-only successor obstruction is a corollary of
`CARRY-J-CHECKPOINT [T]`, the registered odometer definition, and the branch
separation proved in section 5.

At the algebraic map level the displayed objects and maps are L1 to L1 and
introduce no cross-layer lift. The physical-occurrence role remains
unassigned, so this note does not fill a gate field or inherit a public gate
completion. A later owner action must perform a fresh gate audit for the new
source endpoint rather than inherit the earlier pair-input no-gate ruling.

The candidate allowlist proposed for a later owner ruling is:

```text
PhaseCheckpoint_beta:
    explicit (n,x) in Omega;
    registered theta_n;
    checkpoint projection.

AdjacentContext_beta:
    explicit (t,x);
    z_6, the registered generators, and F_t;
    the proposal-local genesis map x |-> kappa_x;
    PREP_SOURCE and EVAL_SOURCE constructors.

AdjacentInput_beta:
    AdjacentContext_beta;
    MakePairInput_beta;
    exact tagged and ordered-product equalities.

Head_beta:
    one explicit pointed sequence;
    its zeroth entry only.
```

This allowlist is proposed, not adopted, and does not amend the predecessor
denylist. The new maps remain forbidden to read `D_scoped`, `MatterData`,
`Post`, `Delta`, event outputs, log positions, result-dependent defaults,
randomness, external clocks, environment, files, or network. Implementation
hidden-input closure remains unresolved.

## 10. Exact next owner fork

This note prepares, but does not take, the following decision:

```text
ADOPT CONDITIONAL ADJACENT CANDIDATE
    freeze Khead_beta, its equality, Head_beta, and the explicit internal
    counter allowlist; adopt OrbitAdjacentInput_beta as the one-orbit
    conditional supply candidate; separately decide whether and how that
    source binds to public K, dom(D_matter), and physical occurrence;

REJECT ADJACENT
    retain the obstruction and choose another explicitly structured source
    and two payload maps;

RETAIN K0 DOMAIN
    freeze two total payload maps from the 15625-element K0 domain;
    their single-valued graph contains at most 15625 pair inputs;

CHANGE DOMAIN
    make a normative decoder-domain proposal before classification;

STOP
    leave every occurrence and public binding field unresolved.
```

Even after `ADOPT CONDITIONAL ADJACENT CANDIDATE`, the map would be
conditional supply, not a distribution, realized history, writeback rule, or
complete `D_matter` origin theorem.

## 11. Result boundary and timing disclosure

This note establishes exactly:

```text
one-source pair maps decompose into two payload maps;
a single-valued K0-to-PairInput_beta map has image cardinal at most
    15625 = |PairInput_beta|/15625;
under the section-3 constructor-only Sym(K0)-equivariance criterion,
    the diagonal is the unique equivariant map;
C0 and C1 are distinct typed proposal-local candidate bindings with equal
    successful EnterPair_beta output;
the actual successor does not factor through the checkpoint on the full
    forward carrier;
the phase-checkpoint pair (theta_n,x) suffices for the displayed one-step
    candidate;
the Khead_beta-domain candidate is total but does not descend through K0;
under the unadopted adjacent candidate, a successful collision separates
    conditional post-states while preserving the current-Q effect/Born read.
```

It does not establish:

```text
a physical occurrence law;
a probability or frequency law;
an owner-adopted adjacent semantics;
a public dom(D_matter)-to-PairInput_beta map;
uniqueness of a phase-retaining supply;
full physical equivalence of C0 and C1;
decoder totality, completeness, factor canonicity, or universality;
any QDD status change.
```

The decomposition, cardinal bound, sign-twisted witness, branch-separation
table, collision corollary, adjacent candidate, successful post-state
witness, and all displayed counts were derived before this note was claimed.
They are disclosed results, not a blind
formal run. No verifier is authorized or required for this definition-only
artifact.
