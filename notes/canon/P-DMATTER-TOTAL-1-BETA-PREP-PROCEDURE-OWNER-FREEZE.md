# P-DMATTER-TOTAL-1 Kernel-Beta Preparation-Procedure Owner Freeze (NON-CANONICAL)

```text
STATUS:                 OWNER-ADOPTED DEFINITION RULING /
                        PHYSICAL PREPARATION-PROCEDURE FREEZE
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / DEFINITION-ONLY /
                        KERNEL-BETA PREPARATION
OWNER DECISION:         ROLE-SEPARATED K0 PREPARATION CONTEXT /
                        TOTAL TAGGED BETA PREPARATION
PREP PROCEDURE:         PREPARE_BETA(lambda), lambda in K0
PREP ZERO BRANCH:       TAGGED / NO NORMALIZED STATE
PHYSICAL RELATION:      PhysPrep_beta, exact successful graph
PREPARED IMAGE:         272 normalized beta states, exact and proper
PHYSICAL OCCURRENCE:    UNRESOLVED
PREP DISTRIBUTION:      UNRESOLVED
SOURCE-PREP CORRELATION:
                        UNRESOLVED
STATE LAYER:            UNRESOLVED
PREP LAYERS:            UNRESOLVED
PREPARATION GATE:       UNRESOLVED
PUBLIC CANON:           Public Canon v24
PUBLIC CANON TAG:       canon-v24
ACTIVATION COMMIT:      0f768cbe50f5f391b261295e58273877b73568f2
CONTENT COMMIT:         bee0f1bfe421d6dbd599b6625e077ef08f03fb4c
RELEASE-FORM COMMIT:    382ddb915648b95c7c09714b6a6b61b63d3c22df
CANON SHA-256:          2511e68c949d471b00d26bb94f23fab9056c2cbb3cc2b9d976c77d276ba02742
CANON BYTES:            134556
CANON BLOB:             5055e0f31ad5cd25ecb57128a1faf152a3f1ba1f
REGISTRY SHA-256:       479ddb3cc4cc6065a770ebfc5159a6112f6652b20eddf009a6bfd7ca55ee1a9e
PUBLIC MAIN BASE:       190e28d943a6dac333b92d520dc5434ac9b49650
HOUSEHOLDER FREEZE:
                        a490b337f0d9388ca3706192ff9ca7e47c8bc2a3df752b61d83722441dc1b3fe
SOURCE-DOMAIN FREEZE:
                        90052839951af4a3490aef2463af11496a3f0e4eb6a5d667b24106d587398e49
SUPPLIED-STATE FREEZE:
                        5280a6ea38e91cec3254da09eaf5eb89951a77fd6798ca7e62f55105ae691e9b
CLAIM ISSUE:            107
CLAIM COMMENT:          5088494047
OWNER CONFIRMATION:     2026-07-27, current session
A11 STATUS:             PARTIAL / O-STOP, unchanged
QDD STATUS:             O / STOP, unchanged
FORMAL RUN:             NONE
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
LAYER CHANGE:           NONE
GATE CHANGE:            NONE
```

This ruling fills the proposal-local `PrepProcedure`, successful
`PhysPrep`, and physically preparable image slots left unresolved by the
supplied-state interface freeze.

It adopts one new model input:

```text
KERNEL-BETA PREPARATION
    a separately role-tagged anchored K0 context may be used as a
    deterministic preparation procedure through the already frozen
    beta_Q bridge.
```

This is not a theorem forced by `J`, Public Canon v24, `beta_Q`, or the
state validator. It is an explicit owner choice made before any formal
classification is opened.

The preparation context is named `lambda`. The instrument-selection
context remains named `kappa`. They have the same inherited payload carrier
`K0`, but they have different role tags and are not identified.

## 0. Falsification and freeze firewall first

The package is inconsistent if any of the following occurs:

```text
PREP-PROCEDURE-TYPE-FAIL
    a preparation procedure lacks a PREPARE_BETA constructor or a K0
    payload, or procedure equality differs from tagged Eq_K0 equality.

PREP-ROLE-COLLAPSE
    PREP_SOURCE(lambda) and EVAL_SOURCE(kappa) are identified merely
    because both payloads lie in K0.

PREP-ZERO-NORMALIZATION
    beta_Q(lambda)=0 is divided by, normalized, replaced, projected,
    clipped, or sent to a default supplied state.

PREP-STATE-FAIL
    one successful output lies outside SuppliedState_G(Q), or the displayed
    normalized beta matrix is not the exact output.

PREP-TAG-COLLAPSE
    PREP_ZERO_BETA and PREP_SUCCESS_BETA are identified with each other or
    with REJECT_NOT_STATE, ZERO_DENOMINATOR, IMPOSSIBLE, or POST.

PREP-TOTALITY-FAIL
    RunPrep_beta is partial on PrepProcedure_beta.

PREP-RELATION-FAIL
    PhysPrep_beta contains a zero-branch pair, omits a successful pair,
    contains a pair not returned by RunPrep_beta, or ceases to be
    right-unique.

PREP-IMAGE-FAIL
    PreparedImage_beta differs from the exact image of PhysPrep_beta.

PREP-IMAGE-COUNT-FAIL
    the exact image has a cardinal other than 272, the successful procedure
    domain has a cardinal other than 15600, or the zero branch has a
    cardinal other than 25.

PREP-FIBRE-FAIL
    the exact successful fibres are not 40 state fibres of size 100 and
    232 state fibres of size 50.

PREP-DIAGONAL-COLLAPSE
    lambda=kappa is imposed silently, or the same-source beta diagonal is
    reported as the complete preparation-occurrence law.

PREP-HIDDEN-FEEDBACK
    D_scoped, MatterData, an event, Post, Delta, history, or a decoder
    output is read back to construct the prepared input.

PREP-MIXING-INFLATION
    a convex mixture, component sampler, frequency, state distribution,
    ancilla reduction, or L6 measure is inferred from this pure-state
    preparation rule.

PREP-SURJECTIVITY-INFLATION
    the 272-state prepared image is identified with all of State_G(Q) or
    all rational pure states.

PREP-OCCURRENCE-INFLATION
    conditional execution of a procedure is reported as proof that the
    procedure occurs, how often it occurs, or how it is paired with kappa.

PREP-LAYER-GATE-INFERENCE
    a layer endpoint, public gate, public identifier, dependency, or
    completion-contract field is filled by inference from this ruling.

FIRE-POSTHOC
    the procedure carrier, role separation, zero tag, realization relation,
    prepared image, equality, or output meaning changes after a
    classification opens.
```

Failure returns

```text
BETA-PREP-PROCEDURE-PACKAGE-INCONSISTENT / STOP.
```

This is not a Canon or registry `F`.

The following actions are forbidden without a new pre-opening owner ruling:

1. drop the 25 zero-beta procedures from the total procedure carrier;
2. normalize `beta_Q(lambda)=0`;
3. identify a raw amplitude with a supplied state without the displayed
   exact normalization and role tag;
4. quotient procedure identity by equality of prepared outputs;
5. set `lambda=kappa` by convention or by shared notation;
6. infer a probability product from the role-separated Cartesian
   admissibility surface;
7. add arbitrary rational rays or mixed states to the physical image;
8. read `D_scoped.density_state` back into the event input;
9. infer preparation occurrence, sampling, frequencies, or a state law;
10. reuse an existing public gate for this preparation map;
11. move A11 or `QUADRATIC-DECODER-DATA` from `O / STOP`;
12. promote the inherited preliminary 146 or the new 272 count to a blind
    formal result.

## 1. Inherited exact scope

Retain the complete anchored source carrier

```text
K0
  = { kappa_x=(U^n(0,x))_(n>=0) : x in F_5^6 }
```

with its frozen pointed-sequence equality `Eq_K0`. The generation map from
`F_5^6` is bijective, so

```text
|K0|=5^6=15625.
```

Retain the balanced section

```text
ell(F_5)={-2,-1,0,1,2}
```

and the exact total bridge

```text
beta_Q : K0 -> Veff,

Veff=ell(F_5)^4 subset Q^4.
```

Every `v in Veff` has exactly 25 inverse images in `K0`, indexed by the
two beta-blind coordinates `(q,r) in F_5^2`.

Retain

```text
G = I_4-(1/5) 1 1^T,

H_Q=(Q^4,<u,v>_G=u^T G v),

State_G(Q)
  = { rho=sum_i q_i v_i v_i^T G, finite sum :
      q_i in Q_(>=0), v_i in Q^4, Tr(rho)=1 }.
```

The form `G` is rational, symmetric, invertible, and positive definite.
For every nonzero `v in Q^4`,

```text
n_G(v)=v^T G v>0.
```

Retain the exact supplied-state carrier and entry map

```text
SuppliedState_G(Q)
  = { SUPPLIED_STATE(rho) : rho in State_G(Q) },

Enter_HH :
    K0 x SuppliedState_G(Q) -> K0 x State_G(Q).
```

`Enter_HH` is the already frozen total bijection. It does not become a
preparation map.

Retain the source-conditioned projected-Householder rule

```text
kappa |-> K_HH(kappa)
```

and its full evaluation domain

```text
Dom_HH=K0 x State_G(Q).
```

The full product is Cartesian admissibility. It is not occurrence,
probabilistic independence, or physical preparation of every state.

The prior supplied-state freeze kept the same-source beta diagonal as an
audit-only subdomain. This ruling does not adopt that diagonal as an
occurrence law. It adopts a new role-separated preparation source.

## 2. Role-separated preparation and evaluation contexts

Define two disjoint tagged copies of `K0`:

```text
PrepContext_K0
  = { PREP_SOURCE(lambda) : lambda in K0 },

EvalContext_K0
  = { EVAL_SOURCE(kappa) : kappa in K0 }.
```

Equality within each carrier is inherited payload equality:

```text
PREP_SOURCE(lambda)=PREP_SOURCE(lambda')
iff
lambda Eq_K0 lambda',

EVAL_SOURCE(kappa)=EVAL_SOURCE(kappa')
iff
kappa Eq_K0 kappa'.
```

Cross-constructor equality is always false:

```text
PREP_SOURCE(lambda) != EVAL_SOURCE(kappa)
```

for every pair of payloads, including `lambda Eq_K0 kappa`.

Define the total payload maps

```text
UnpackPrep_K0 :
    PrepContext_K0 -> K0,

UnpackPrep_K0(PREP_SOURCE(lambda))
  = lambda,
```

and

```text
UnpackEval_K0 :
    EvalContext_K0 -> K0,

UnpackEval_K0(EVAL_SOURCE(kappa))
  = kappa.
```

Both are bijections. Their exact inverses are the corresponding role
constructors.
No inherited map typed on bare `K0` silently consumes a role-tagged
context. It receives the payload only through the corresponding unpack
map.

Define the physical preparation-procedure carrier

```text
PrepProcedure_beta
  = { PREPARE_BETA(PREP_SOURCE(lambda)) : lambda in K0 }.
```

Procedure equality is

```text
PREPARE_BETA(PREP_SOURCE(lambda))
  = PREPARE_BETA(PREP_SOURCE(lambda'))

iff

lambda Eq_K0 lambda'.
```

Thus

```text
|PrepProcedure_beta|=15625.
```

Procedure identity is not quotient by `beta_Q`, normalized state, prepared
output, `Qcan`, or Householder shadow. Distinct procedures may prepare the
same state.

The model input frozen here is:

```text
OWNER-KERNEL-BETA-PREPARATION
    PREPARE_BETA(PREP_SOURCE(lambda)) is an admissible deterministic
    physical preparation instruction at the proposal-local interface.
```

This statement is conditional on the procedure being supplied. It does not
say that a procedure occurs or that an external agent selects it.

## 3. Total tagged execution

For

```text
p=PREPARE_BETA(PREP_SOURCE(lambda)),
```

define

```text
v_lambda
  = beta_Q(UnpackPrep_K0(PREP_SOURCE(lambda)))
  = beta_Q(lambda).
```

If `v_lambda!=0`, define the exact normalized beta state

```text
rho_beta(lambda)
  = v_lambda v_lambda^T G / n_G(v_lambda),

n_G(v_lambda)
  = v_lambda^T G v_lambda.
```

All entries lie in `Q`. Moreover,

```text
rho_beta(lambda) G^-1
  = v_lambda v_lambda^T / n_G(v_lambda)
```

is rational, symmetric, positive semidefinite, and rank one, and

```text
Tr(rho_beta(lambda))
  = v_lambda^T G v_lambda / n_G(v_lambda)
  = 1.
```

Therefore

```text
rho_beta(lambda) in State_G(Q),

Validate_G(rho_beta(lambda))
  = ACCEPT_STATE(rho_beta(lambda)).
```

Define the exact successful-source carrier

```text
K0_beta^+
  = { lambda in K0 : beta_Q(lambda)!=0 }
```

with equality restricted from `Eq_K0`. Define the two total maps

```text
RhoBeta_G :
    K0_beta^+ -> State_G(Q),

RhoBeta_G(lambda)=rho_beta(lambda),
```

and

```text
SupplyBeta_G :
    K0_beta^+ -> SuppliedState_G(Q),

SupplyBeta_G(lambda)
  = AdmitSupplied_G(ACCEPT_STATE(RhoBeta_G(lambda))).
```

Both maps are total and equality-compatible on `K0_beta^+`.

Define the tagged result carrier

```text
PrepResult_beta

  = { PREP_ZERO_BETA(lambda) :
      lambda in K0 and beta_Q(lambda)=0 }

    disjoint-union

    { PREP_SUCCESS_BETA(lambda,s) :
      lambda in K0,
      beta_Q(lambda)!=0,
      s=SupplyBeta_G(lambda) }.
```

Tagged equality is literal constructor equality plus:

```text
Eq_K0 on lambda;
exact supplied-state equality on s.
```

The two constructors are never equal.

Define the execution map

```text
RunPrep_beta :
    PrepProcedure_beta -> PrepResult_beta,

RunPrep_beta(PREPARE_BETA(PREP_SOURCE(lambda)))

  = PREP_ZERO_BETA(lambda)
        if beta_Q(lambda)=0,

  = PREP_SUCCESS_BETA(lambda,SupplyBeta_G(lambda))
        if beta_Q(lambda)!=0.
```

This map is total and deterministic.

The zero branch is exact:

```text
beta_Q(lambda)=0
```

exactly when the four beta-visible piston coordinates are zero. The two
beta-blind coordinates are arbitrary, so

```text
|{ lambda in K0 : beta_Q(lambda)=0 }|
  =5^2
  =25.
```

Consequently,

```text
zero procedures:        25,
successful procedures:  15625-25=15600.
```

The zero tag means:

```text
the selected beta amplitude has no normalized state.
```

It is not:

```text
REJECT_NOT_STATE
    rejection of a supplied raw matrix;

ZERO_DENOMINATOR
    the inherited D_scoped readout tag;

IMPOSSIBLE
    a zero-weight event branch;

POST
    a normalized post-event state.
```

No zero-branch supplied state exists.

## 4. Exact physical realization relation

Define the successful procedure subcarrier

```text
PrepProcedure_beta^+

  = { PREPARE_BETA(PREP_SOURCE(lambda)) :
      lambda in K0,
      beta_Q(lambda)!=0 }.
```

Define the exact physical realization relation

```text
PhysPrep_beta

  = { (PREPARE_BETA(PREP_SOURCE(lambda)),s)
      in PrepProcedure_beta x SuppliedState_G(Q) :

      RunPrep_beta(PREPARE_BETA(PREP_SOURCE(lambda)))
        = PREP_SUCCESS_BETA(lambda,s) }.
```

Relation membership uses:

```text
constructor equality;
Eq_K0 on procedure payloads;
exact entrywise rational equality on supplied-state payloads.
```

Use the exact two-element truth carrier

```text
Truth_beta={TRUE,FALSE}
```

with literal equality. Define the total characteristic predicate

```text
InPhysPrep_beta :
    PrepProcedure_beta x SuppliedState_G(Q) -> Truth_beta,

InPhysPrep_beta(p,s)=TRUE
iff
(p,s) in PhysPrep_beta.
```

Its domain equality is product equality from procedure equality and exact
supplied-state equality. It is total and equality-compatible on the full
ambient product.

`PhysPrep_beta` is the graph of `SupplyBeta_G` on
`PrepProcedure_beta^+`. Therefore:

```text
1. it is left-total on PrepProcedure_beta^+;
2. it is right-unique;
3. its projection to PrepProcedure_beta is exactly
   PrepProcedure_beta^+;
4. it has no pair above a PREP_ZERO_BETA procedure.
```

It is not left-total on all of `PrepProcedure_beta`, because the 25 exact
zero procedures have no normalized state. Totality belongs to the tagged
map `RunPrep_beta`, not to the successful relation after its failure tag is
forgotten.

Define the physically preparable image

```text
PreparedImage_beta

  = { s in SuppliedState_G(Q) :
      exists p in PrepProcedure_beta
      with (p,s) in PhysPrep_beta }.
```

Define the total characteristic predicate

```text
InPreparedImage_beta :
    SuppliedState_G(Q) -> Truth_beta,

InPreparedImage_beta(s)=TRUE
iff
s in PreparedImage_beta.
```

It uses exact supplied-state equality, is total on all of
`SuppliedState_G(Q)`, and is equality-compatible.

By construction,

```text
PreparedImage_beta

  = { SUPPLIED_STATE(rho_beta(lambda)) :
      lambda in K0,
      beta_Q(lambda)!=0 }

  = { SUPPLIED_STATE(v v^T G/(v^T G v)) :
      v in Veff,
      v!=0 }.
```

This equality is exact and complete. No unlisted state is physically
prepared by this ruling, and every listed state has at least one successful
procedure.

## 5. Exact image classification

For nonzero rational vectors `v,w`,

```text
v v^T G/(v^T G v)
  = w w^T G/(w^T G w)
```

if and only if

```text
w=c v
```

for some `c in Q^*`.

The forward direction follows after right multiplication by `G^-1`.
Equality of the resulting nonzero rank-one symmetric matrices makes their
ranges equal, so `w=c v`; the scalar is rational because both vectors are
rational and one coordinate of `v` is nonzero. The reverse direction is
immediate because numerator and denominator both scale by `c^2`.

Thus `PreparedImage_beta` is classified by the rational projective rays
meeting

```text
Veff\{0}
  = {-2,-1,0,1,2}^4\{0}.
```

Every such ray has a unique primitive integer representative up to sign.
There are

```text
5^4-1=624
```

nonzero vectors in the box. A vector in the box is nonprimitive exactly
when all four coordinates are even. There are

```text
3^4-1=80
```

nonzero all-even vectors. Hence the number of primitive vectors is

```text
624-80=544.
```

No nonzero primitive vector equals its negative. Quotienting by sign gives

```text
|PreparedImage_beta|
  =544/2
  =272.
```

The inverse fibres also classify exactly.

There are

```text
(3^4-1)/2=40
```

projective rays with a primitive representative in
`{-1,0,1}^4\{0}`. Such a ray meets `Veff` in

```text
{v,-v,2v,-2v},
```

so it has four amplitude representatives and

```text
4*25=100
```

successful K0 procedures.

The remaining

```text
272-40=232
```

rays meet `Veff` only in `{v,-v}` and have

```text
2*25=50
```

successful procedures.

The complete fibre check is

```text
40*100+232*50
  =4000+11600
  =15600.
```

Together with the 25 zero procedures this recovers all of
`PrepProcedure_beta`.

The image is a proper finite subset of `SuppliedState_G(Q)`.

For a mixed-state witness, let

```text
rho_*=I_4/4.
```

Then

```text
rho_* G^-1=(I_4+1 1^T)/4
```

is rational positive definite and `Tr(rho_*)=1`, so
`rho_* in State_G(Q)`. It has rank four and is not in
`PreparedImage_beta`.

The image is also a proper subset of the rational pure states. For example,
the primitive direction

```text
u=(1,3,0,0)
```

does not meet `Veff`, while its normalized Gram state is a valid rational
pure state.

Therefore this ruling proves, rather than assumes:

```text
PreparedImage_beta
  proper-subset
SuppliedState_G(Q).
```

No physical surjectivity onto the full state carrier is claimed.

## 6. Relation to the full product and the old diagonal

The physical preparation context and the instrument-selection context have
different roles:

```text
lambda    selects the beta preparation procedure;
kappa     selects K_HH(kappa).
```

This ruling adopts no equation or relation

```text
lambda=kappa.
```

For every successful prepared state

```text
s=SUPPLIED_STATE(rho_beta(lambda))
```

and every role-tagged evaluation context

```text
e=EVAL_SOURCE(kappa),

kappa=UnpackEval_K0(e),
```

the already frozen full product admits

```text
(kappa,s) in K0 x SuppliedState_G(Q).
```

Define the exact proposal-local admissibility entry

```text
EnterPrepared_HH :
    EvalContext_K0 x PreparedImage_beta -> Dom_HH^sup,

EnterPrepared_HH(e,s)
  = (UnpackEval_K0(e),s).
```

With the displayed product equalities, it is equality-compatible, total,
and bijective onto the subset

```text
K0 x PreparedImage_beta
  subset Dom_HH^sup.
```

Composition with the inherited entry is

```text
Enter_HH(EnterPrepared_HH(e,s))
  = (UnpackEval_K0(e),UnpackSupplied_G(s))
  in Dom_HH.
```

This is a consequence of Cartesian admissibility. It is not a probability
factorization and does not assert that the pair occurs.

The same-source diagonal

```text
lambda=kappa,

rho=rho_beta(kappa)
```

remains the inherited mandatory negative control. On that diagonal the
projected-Householder and Luders tagged pointer-read data agree for every
nonzero beta amplitude. This ruling neither removes that fact nor promotes
the diagonal to the complete physical law.

The following three statements remain different:

```text
PAIR ADMISSIBILITY
    every typed kappa may be evaluated with every state in
    PreparedImage_beta.

PREPARATION EXECUTION
    a supplied PREPARE_BETA(lambda) deterministically returns its tagged
    preparation result.

PAIR OCCURRENCE
    a law says which lambda and kappa occur together.
```

The first two are fixed at proposal scope. The third is unresolved.

In particular, a beta-zero `kappa` remains a valid evaluation context. The
zero failure concerns `lambda` in its preparation role only.

## 7. Six beta-preparable states separate the Householder shadows

Let

```text
b_1=(1,0,0,-1),
b_2=(0,1,0,-1),
b_3=(0,0,1,-1).
```

These vectors form a rational basis of the three-dimensional high sector.
Define

```text
W_beta
  = { b_1,b_2,b_3,
      b_1+b_2,b_1+b_3,b_2+b_3 }.
```

Equality in `W_beta` is exact equality in `Q^4`. Membership is the total
six-comparison predicate

```text
InW_beta : Q^4 -> Truth_beta,

InW_beta(w)=TRUE
iff
w equals one of the six displayed vectors.
```

Thus `W_beta` is an exact finite carrier of cardinality six.

Explicitly, the last three vectors are

```text
(1,1,0,-2),
(1,0,1,-2),
(0,1,1,-2).
```

Every vector in `W_beta`:

```text
is nonzero;
has coordinate sum zero;
lies in Veff;
lies in Image(E_high);
has 25 beta_Q preimages.
```

Define the exact state-image map

```text
BetaRayState_G :
    W_beta -> PreparedImage_beta,

BetaRayState_G(w)
  = SUPPLIED_STATE(w w^T G/(w^T G w)).
```

It is total and equality-compatible. Its denominator is positive because
every `w in W_beta` is nonzero, and its codomain claim follows from the
displayed `Veff` membership and the 25 exact `beta_Q` preimages. The six
vectors occupy six distinct rational rays, so `BetaRayState_G(W_beta)`
contains six states.

This is a mathematical state-image map. It selects no preparation
procedure and asserts no occurrence or distribution.

Let `T` and `T'` be two high-sector operators selected by the inherited
projected-Householder source rule. Each is either the identity or a
three-dimensional Householder reflection.

Suppose their high event maps agree on all six normalized states. Exact
rank-one equality and high-sector isometry give signs

```text
epsilon_i, epsilon_ij in {+1,-1}
```

such that

```text
T b_i
  = epsilon_i T' b_i,

T(b_i+b_j)
  = epsilon_ij T'(b_i+b_j).
```

Because `T'` is invertible and `b_i,b_j` are independent, comparison of the
two coefficients in the pair-sum equation forces

```text
epsilon_i=epsilon_j=epsilon_ij.
```

The three basis signs are therefore equal, so

```text
T=+T'
```

or

```text
T=-T'.
```

The negative case cannot occur inside the selected family. The high-sector
identity has trace `3`, and each three-dimensional Householder reflection
has trace `1`. Negation changes the trace sign. Therefore

```text
T=T'.
```

Contrapositively, every unequal pair of selected high-sector operators is
separated by at least one beta-preparable state from `W_beta`.

Define, only on the inherited source-selected Householder family, the
restricted comparison

```text
K Eq_beta-prep K'

iff

K_a rho K_a^sharp
  = K'_a rho (K'_a)^sharp

for every SUPPLIED_STATE(rho) in PreparedImage_beta
and each a in {low,high}.
```

Define the two total comparison predicates on

```text
SourceImage_HH x SourceImage_HH.
```

First,

```text
Agree_W_beta(K,K')=TRUE
```

if and only if the two labeled event maps agree on the six normalized
states in `BetaRayState_G(W_beta)`. Second,

```text
InEqBetaPrep(K,K')=TRUE
iff
K Eq_beta-prep K'.
```

Both use product equality inherited from exact instrument equality and have
codomain `Truth_beta`. They are total and equality-compatible. The proof
above gives the exact certificate

```text
Agree_W_beta(K,K')=TRUE
iff
InEqBetaPrep(K,K')=TRUE
iff
K Eq_instrument K'
```

for every `(K,K') in SourceImage_HH x SourceImage_HH`.

The low operator is fixed, and the six-ray lemma gives

```text
Eq_beta-prep
  = Eq_instrument
```

on `SourceImage_HH`.

This closes the state-side witness-availability obstruction for that
source-selected family. Mixed-state preparation and arbitrary rational-ray
preparation are not needed to distinguish its unequal shadows.

The inherited count

```text
|SourceImage_HH/Eq_instrument|=146
```

remains preliminary exact nonformal analysis. The six-ray lemma does not
turn it into physical `NONUNIQUE(146)`, an alternative-decoder count, a
formal probe result, or a public claim. Source occurrence, formal
classification completeness, layers, gates, public identifiers, and
implementation closure remain unresolved.

## 8. Explicitly non-adopted alternatives

The following are not part of this ruling:

```text
SAME-SOURCE DIAGONAL LAW
    PREP_SOURCE(lambda) and EVAL_SOURCE(kappa) are identified and only
    lambda=kappa is admitted or said to occur.

ARBITRARY RATIONAL-RAY PREPARATION
    every ray in (Q^4\{0})/Q^* is declared physically preparable.

FINITE RATIONAL CONVEX MIXING
    rational weights over pure preparations are treated as a physical
    mixture or as a preparation probability.

MIXED-STATE SURJECTIVITY
    every member of State_G(Q) is declared physically preparable.

D_SCOPED FEEDBACK
    the `density_state` readout field is written back as the next input.

POST-EVENT PREPARATION
    a tagged Post value becomes the next input without a realized-outcome
    and history rule.

DELTA HISTORY
    Delta_HH is iterated without a frozen initial state and context stream.

Q2-OUTPUT ORIGIN
    the reversible apparatus is treated as producing an input state without
    first receiving a system state.

HIDDEN DEFAULT
    one state is supplied without a preparation procedure.

RANDOM PREPARATION
    a component or state is sampled from an untyped distribution.

GYRON PREPARATION
    the v24 Gyron `1/6` is used as a preparation probability or sampler.
```

Arbitrary rational-ray preparation would add a countably infinite unsourced
physical input carrier. Finite convex mixing would require a separately
chosen meaning for its weights:

```text
proper mixture       sampling or frequencies;
improper mixture     ancilla, coupling, and reduction;
epistemic mixture    observer or coarse-graining semantics.
```

None is needed for the six-ray separation result, and none is frozen here.

## 9. Layers and gates

Public Canon v24 declares:

```text
L1 state,
L2 manifold,
L3 boundary,
L4 support,
L5 stream,
L6 measure.
```

It does not publicly assign the new or inherited proposal-local
preparation objects to those layers.

The following remain unresolved:

```text
PrepContext_K0 layer
EvalContext_K0 layer
PrepProcedure_beta layer
PrepResult_beta layer
SuppliedState_G(Q) layer
State_G(Q) layer
UnpackPrep_K0 endpoints
UnpackEval_K0 endpoints
RhoBeta_G endpoints
SupplyBeta_G endpoints
BetaRayState_G endpoints
EnterPrepared_HH endpoints
RunPrep_beta endpoints
PhysPrep_beta endpoints
prepared-image endpoint
source-state entry endpoints
physical preparation gate
source-state entry gate.
```

In particular, no current public gate authorizes this surface:

```text
GATE-L1-L5-LOG-PROJECTION
    concerns only the derived Log stream.

GATE-L5-L6-BORN-READING
    concerns only the Born dictionary lift.

GATE-L5-L6-METRO-NORMALIZATION
    concerns only the metrology normalization obligation.

GATE-L5-L1-OBSERVER-WRITEBACK
    remains OPEN_WRITEBACK / STOP and cannot be reused as a preparation
    permission.
```

If the later frozen endpoints differ, a new public gate is required. If
they coincide, the same-layer statement still requires an explicit public
ruling. The word `state` does not assign L1 automatically.

No layer or gate ledger changes in this note.

## 10. Occurrence, sampling, history, and writeback

This ruling defines no:

```text
procedure occurrence relation;
preparation-context distribution;
evaluation-context distribution;
joint lambda-kappa distribution;
source-state frequency;
component sampler;
realized-outcome sampler;
history carrier;
history-update map;
state-transition recursion;
feedback edge;
writeback into U;
terminality theorem.
```

`RunPrep_beta` is deterministic conditional execution. It does not choose
its own input procedure.

The rational normalization denominator is a state normalization. It is not
a preparation probability, occurrence probability, L5 stream, or L6
measure.

No output of `RunPrep_beta`, `PhysPrep_beta`, `EnterPrepared_HH`, or
`Enter_HH` feeds the autonomous update `U`. This is a proposal-local
no-edge statement for the maps defined here, not a completion-wide
`feeds_U=FALSE` or terminality proof.

No public tagged `NONE` is inferred for sampling, history, or writeback.
Their values remain `UNRESOLVED`.

## 11. Semantic hidden-input closure

Freeze the free-variable allowlists for the role payload maps:

```text
UnpackPrep_K0 reads only its explicit PREP_SOURCE(lambda) argument;
UnpackEval_K0 reads only its explicit EVAL_SOURCE(kappa) argument;
each returns only the unchanged K0 payload.
```

Freeze the free-variable allowlists for `RhoBeta_G` and `SupplyBeta_G`:

```text
the explicit lambda in K0_beta^+;
beta_Q, exact G, and exact rational arithmetic;
the displayed normalized rank-one formula;
ACCEPT_STATE, AdmitSupplied_G, and SUPPLIED_STATE.
```
Freeze the free-variable allowlist for `RunPrep_beta`:

```text
the explicit PREPARE_BETA(PREP_SOURCE(lambda)) argument;
Eq_K0 and the inherited anchored K0 payload;
the inherited total beta_Q map;
the fixed exact G;
UnpackPrep_K0;
exact rational matrix arithmetic;
the exact zero test on beta_Q(lambda);
the displayed normalized rank-one formula on the nonzero branch;
Validate_G soundness and the exact ACCEPT_STATE constructor;
AdmitSupplied_G and the SUPPLIED_STATE constructor;
the PREP_ZERO_BETA and PREP_SUCCESS_BETA constructors.
```

Freeze the free-variable allowlist for `PhysPrep_beta`:

```text
the explicit procedure and supplied-state arguments;
RunPrep_beta;
constructor equality;
Eq_K0;
exact supplied-state payload equality.
```

Freeze the allowlist for `PreparedImage_beta`:

```text
PhysPrep_beta;
exact existential projection over PrepProcedure_beta;
exact relation and supplied-state equality.
```


Freeze the free-variable allowlists for `InW_beta` and
`BetaRayState_G`:

```text
the explicit w argument;
the six displayed vectors and exact Q^4 equality for InW_beta;
the exact G, rational arithmetic, and displayed rank-one state formula;
the SUPPLIED_STATE constructor;
the proved W_beta membership in Veff and its exact beta_Q preimages;
the proved codomain inclusion in PreparedImage_beta.
```

`BetaRayState_G` reads no selected `beta_Q` preimage, preparation
procedure, lambda-kappa relation, occurrence law, or distribution.

Freeze the free-variable allowlists for `Agree_W_beta` and
`InEqBetaPrep`:

```text
the explicit K and K' arguments in SourceImage_HH;
the inherited exact low/high event maps and instrument equality;
BetaRayState_G(W_beta) for Agree_W_beta;
PreparedImage_beta for InEqBetaPrep;
exact finite or universal comparison with no tolerance.
```

Freeze the allowlist for `EnterPrepared_HH`:

```text
the explicit EVAL_SOURCE(kappa) argument;
the explicit s in PreparedImage_beta;
UnpackEval_K0;
exact product construction;
the inherited Enter_HH and UnpackSupplied_G maps for the displayed
composition only.
```

It reads no preparation procedure, lambda-kappa relation, or occurrence law.

The semantic denylist for `RunPrep_beta`, `PhysPrep_beta`, and
`PreparedImage_beta` is:

```text
an EVAL_SOURCE(kappa) payload;
an equation lambda=kappa;
a later checkpoint;
the counter or current log position;
the Thue-Morse bit;
Qcan or a Householder class count;
D_scoped or MatterData;
an event, Born value, Post value, or Delta output;
a selected ensemble component;
randomness or a probability distribution;
environment variables;
files or network data;
clock or date;
dynamic evaluation;
a hidden default state;
automatic zero normalization;
floating-point arithmetic or tolerance.
```

This freezes semantic free-variable closure only.

It does not fill the Public Canon v24 field

```text
factor_canonicity_manifest.hidden_input_closure_id: UNRESOLVED.
```

Transitive implementation closure remains unresolved until code, imports,
files, environment reads, clock access, randomness, network access, and
dynamic evaluation are pinned and audited.

## 12. Proposal-local dependency graph

The new dependency graph is:

```text
PrepContext_K0
    -> PrepProcedure_beta,

PrepContext_K0
    -> UnpackPrep_K0
    -> K0
    -> beta_Q

beta_Q + G
    -> RhoBeta_G on K0_beta^+
    -> Validate_G = ACCEPT_STATE
    -> AdmitSupplied_G
    -> SupplyBeta_G

PrepProcedure_beta + UnpackPrep_K0 + beta_Q zero test + SupplyBeta_G
    -> RunPrep_beta
    -> PREP_ZERO_BETA or PREP_SUCCESS_BETA

RunPrep_beta + exact result equality
    -> InPhysPrep_beta
    -> PhysPrep_beta
    -> InPreparedImage_beta
    -> PreparedImage_beta.
```

The evaluation and entry branches are

```text
EvalContext_K0
    -> UnpackEval_K0
    -> K_HH
    -> source-conditioned event maps,

EvalContext_K0 + PreparedImage_beta
    -> EnterPrepared_HH
    -> Enter_HH.
```

The separation theorem depends on

```text
BetaRayState_G : W_beta -> PreparedImage_beta;
SourceImage_HH;
K_HH;
Eq_instrument;
the six exact high-sector event-map comparisons.
```

These dependencies produce `Agree_W_beta` and the exact agreement of the
beta-restricted comparison with `Eq_instrument` on `SourceImage_HH`.

The preparation and evaluation branches meet only through
`EnterPrepared_HH` when a caller supplies a typed pair. No occurrence law
is inferred.

There is no edge:

```text
D_scoped -> RunPrep_beta;
MatterData -> RunPrep_beta;
Post -> RunPrep_beta;
Delta -> RunPrep_beta;
PreparedImage_beta -> U;
event output -> U.
```

The proposal-local graph is acyclic. Public dependency closure is not
claimed.

## 13. Proposal-local schema

Every identifier in this section is proposal-local. It fills no public
Canon, registry, dependency, gate, evidence, completion-contract, or
factor-canonicity slot.

### 13.1 Context and procedure

```text
truth_carrier_id:
    CAND-QDD-CARRIER-TRUTH-BETA

truth_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

prep_context_carrier_id:
    CAND-QDD-CARRIER-K0-PREP-CONTEXT-BETA-N0

prep_context_constructor_id:
    CAND-QDD-CONSTRUCTOR-PREP-SOURCE-K0

prep_context_equality_id:
    CAND-QDD-EQ-PREP-SOURCE-K0-POINTED

eval_context_carrier_id:
    CAND-QDD-CARRIER-K0-EVAL-CONTEXT-HH

eval_context_constructor_id:
    CAND-QDD-CONSTRUCTOR-EVAL-SOURCE-K0

eval_context_equality_id:
    CAND-QDD-EQ-EVAL-SOURCE-K0-POINTED

role_disjointness_certificate_id:
    CAND-QDD-CERT-PREP-EVAL-K0-ROLE-DISJOINT

prep_context_unpack_map_id:
    CAND-QDD-MAP-UNPACK-PREP-SOURCE-K0

prep_context_unpack_domain_id:
    CAND-QDD-CARRIER-K0-PREP-CONTEXT-BETA-N0

prep_context_unpack_codomain_id:
    CAND-CARRIER-ANCHORED-ORBITS-K0

prep_context_unpack_domain_equality_id:
    CAND-QDD-EQ-PREP-SOURCE-K0-POINTED

prep_context_unpack_codomain_equality_id:
    CAND-EQ-POINTED-FORWARD-SEQUENCE

prep_context_unpack_totality_domain_id:
    CAND-QDD-CARRIER-K0-PREP-CONTEXT-BETA-N0

prep_context_unpack_totality_id:
    CAND-QDD-CERT-UNPACK-PREP-SOURCE-K0-TOTAL

prep_context_unpack_equality_id:
    CAND-QDD-CERT-UNPACK-PREP-SOURCE-K0-EQUALITY

prep_context_unpack_bijection_id:
    CAND-QDD-CERT-UNPACK-PREP-SOURCE-K0-BIJECTIVE

eval_context_unpack_map_id:
    CAND-QDD-MAP-UNPACK-EVAL-SOURCE-K0

eval_context_unpack_domain_id:
    CAND-QDD-CARRIER-K0-EVAL-CONTEXT-HH

eval_context_unpack_codomain_id:
    CAND-CARRIER-ANCHORED-ORBITS-K0

eval_context_unpack_domain_equality_id:
    CAND-QDD-EQ-EVAL-SOURCE-K0-POINTED

eval_context_unpack_codomain_equality_id:
    CAND-EQ-POINTED-FORWARD-SEQUENCE

eval_context_unpack_totality_domain_id:
    CAND-QDD-CARRIER-K0-EVAL-CONTEXT-HH

eval_context_unpack_totality_id:
    CAND-QDD-CERT-UNPACK-EVAL-SOURCE-K0-TOTAL

eval_context_unpack_equality_id:
    CAND-QDD-CERT-UNPACK-EVAL-SOURCE-K0-EQUALITY

eval_context_unpack_bijection_id:
    CAND-QDD-CERT-UNPACK-EVAL-SOURCE-K0-BIJECTIVE

prep_procedure_carrier_id:
    CAND-QDD-CARRIER-PREP-PROCEDURE-BETA-N0

prep_procedure_constructor_id:
    CAND-QDD-CONSTRUCTOR-PREPARE-BETA-N0

prep_procedure_equality_id:
    CAND-QDD-EQ-PREP-PROCEDURE-BY-K0-POINTED

prep_procedure_cardinality_id:
    CAND-QDD-CERT-PREP-PROCEDURE-CARD-15625
```

### 13.2 Tagged execution

```text
prep_success_source_carrier_id:
    CAND-QDD-CARRIER-K0-BETA-NONZERO

prep_success_source_equality_id:
    CAND-QDD-EQ-K0-BETA-NONZERO-POINTED

rho_beta_map_id:
    CAND-QDD-MAP-RHO-BETA-G-NONZERO

rho_beta_domain_id:
    CAND-QDD-CARRIER-K0-BETA-NONZERO

rho_beta_codomain_id:
    CAND-QDD-STATE-G-RATIONAL

rho_beta_domain_equality_id:
    CAND-QDD-EQ-K0-BETA-NONZERO-POINTED

rho_beta_codomain_equality_id:
    CAND-QDD-EQ-RATIONAL-MATRIX

rho_beta_totality_domain_id:
    CAND-QDD-CARRIER-K0-BETA-NONZERO

rho_beta_totality_id:
    CAND-QDD-CERT-RHO-BETA-G-TOTAL-NONZERO

rho_beta_equality_id:
    CAND-QDD-CERT-RHO-BETA-G-EQUALITY

supply_beta_map_id:
    CAND-QDD-MAP-SUPPLY-BETA-G-NONZERO

supply_beta_domain_id:
    CAND-QDD-CARRIER-K0-BETA-NONZERO

supply_beta_codomain_id:
    CAND-QDD-CARRIER-SUPPLIED-STATE-G-RATIONAL

supply_beta_domain_equality_id:
    CAND-QDD-EQ-K0-BETA-NONZERO-POINTED

supply_beta_codomain_equality_id:
    CAND-QDD-EQ-SUPPLIED-STATE-G-RATIONAL

supply_beta_totality_domain_id:
    CAND-QDD-CARRIER-K0-BETA-NONZERO

supply_beta_totality_id:
    CAND-QDD-CERT-SUPPLY-BETA-G-TOTAL-NONZERO

supply_beta_equality_id:
    CAND-QDD-CERT-SUPPLY-BETA-G-EQUALITY

prep_result_carrier_id:
    CAND-QDD-CARRIER-PREP-RESULT-BETA-TAGGED

prep_zero_constructor_id:
    CAND-QDD-CONSTRUCTOR-PREP-ZERO-BETA

prep_success_constructor_id:
    CAND-QDD-CONSTRUCTOR-PREP-SUCCESS-BETA

prep_result_equality_id:
    CAND-QDD-EQ-PREP-RESULT-BETA-TAGGED

prep_run_map_id:
    CAND-QDD-MAP-RUN-PREP-BETA-N0

prep_run_domain_id:
    CAND-QDD-CARRIER-PREP-PROCEDURE-BETA-N0

prep_run_codomain_id:
    CAND-QDD-CARRIER-PREP-RESULT-BETA-TAGGED

prep_run_domain_equality_id:
    CAND-QDD-EQ-PREP-PROCEDURE-BY-K0-POINTED

prep_run_codomain_equality_id:
    CAND-QDD-EQ-PREP-RESULT-BETA-TAGGED

prep_run_totality_domain_id:
    CAND-QDD-CARRIER-PREP-PROCEDURE-BETA-N0

prep_run_totality_id:
    CAND-QDD-CERT-RUN-PREP-BETA-TOTAL

prep_run_equality_id:
    CAND-QDD-CERT-RUN-PREP-BETA-EQUALITY

prep_zero_count_id:
    CAND-QDD-CERT-PREP-ZERO-BETA-25

prep_success_count_id:
    CAND-QDD-CERT-PREP-SUCCESS-BETA-15600

prep_state_soundness_id:
    CAND-QDD-CERT-PREP-BETA-STATE-G-SOUND
```

### 13.3 Physical relation, image, and entry

```text
phys_prep_relation_id:
    CAND-QDD-REL-PHYS-PREP-BETA-N0

phys_prep_ambient_domain_id:
    CAND-QDD-DOMAIN-PREP-PROCEDURE-X-SUPPLIED-STATE-G

phys_prep_ambient_domain_equality_id:
    CAND-QDD-EQ-PREP-PROCEDURE-X-SUPPLIED-STATE-G-PRODUCT

phys_prep_relation_extensional_equality_id:
    CAND-QDD-EQ-REL-PHYS-PREP-BETA-EXTENSIONAL

phys_prep_relation_membership_id:
    CAND-QDD-PRED-PHYS-PREP-BETA-N0

phys_prep_membership_map_id:
    CAND-QDD-MAP-IN-PHYS-PREP-BETA

phys_prep_membership_domain_id:
    CAND-QDD-DOMAIN-PREP-PROCEDURE-X-SUPPLIED-STATE-G

phys_prep_membership_codomain_id:
    CAND-QDD-CARRIER-TRUTH-BETA

phys_prep_membership_domain_equality_id:
    CAND-QDD-EQ-PREP-PROCEDURE-X-SUPPLIED-STATE-G-PRODUCT

phys_prep_membership_codomain_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

phys_prep_membership_totality_domain_id:
    CAND-QDD-DOMAIN-PREP-PROCEDURE-X-SUPPLIED-STATE-G

phys_prep_membership_totality_id:
    CAND-QDD-CERT-IN-PHYS-PREP-BETA-TOTAL

phys_prep_membership_equality_id:
    CAND-QDD-CERT-IN-PHYS-PREP-BETA-EQUALITY

phys_prep_success_domain_id:
    CAND-QDD-DOMAIN-PHYS-PREP-BETA-NONZERO

phys_prep_success_domain_equality_id:
    CAND-QDD-EQ-PREP-PROCEDURE-BETA-NONZERO

phys_prep_left_totality_domain_id:
    CAND-QDD-DOMAIN-PHYS-PREP-BETA-NONZERO

phys_prep_functionality_id:
    CAND-QDD-CERT-PHYS-PREP-BETA-RIGHT-UNIQUE

phys_prep_success_totality_id:
    CAND-QDD-CERT-PHYS-PREP-BETA-LEFT-TOTAL-ON-NONZERO

prepared_image_carrier_id:
    CAND-QDD-CARRIER-PREPARED-IMAGE-BETA-N0

prepared_image_equality_id:
    CAND-QDD-EQ-PREPARED-IMAGE-STATE-G-ENTRYWISE

prepared_image_membership_id:
    CAND-QDD-PRED-PREPARED-IMAGE-BETA-N0

prepared_image_membership_map_id:
    CAND-QDD-MAP-IN-PREPARED-IMAGE-BETA

prepared_image_membership_domain_id:
    CAND-QDD-CARRIER-SUPPLIED-STATE-G-RATIONAL

prepared_image_membership_codomain_id:
    CAND-QDD-CARRIER-TRUTH-BETA

prepared_image_membership_domain_equality_id:
    CAND-QDD-EQ-SUPPLIED-STATE-G-RATIONAL

prepared_image_membership_codomain_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

prepared_image_membership_totality_domain_id:
    CAND-QDD-CARRIER-SUPPLIED-STATE-G-RATIONAL

prepared_image_membership_totality_id:
    CAND-QDD-CERT-IN-PREPARED-IMAGE-BETA-TOTAL

prepared_image_membership_equality_id:
    CAND-QDD-CERT-IN-PREPARED-IMAGE-BETA-EQUALITY

prepared_image_completeness_statement_id:
    CAND-QDD-STATEMENT-PREPARED-IMAGE-BETA-EXACT

prepared_image_completeness_method_id:
    CAND-QDD-METHOD-PREPARED-IMAGE-BETA-PROJECTIVE-RAY-CLASSIFICATION

prepared_image_completeness_proof_id:
    CAND-QDD-PROOF-PREPARED-IMAGE-BETA-624-80-OVER-2

prepared_image_cardinality_id:
    CAND-QDD-CERT-PREPARED-IMAGE-BETA-272

prepared_image_fibre_id:
    CAND-QDD-CERT-PREPARED-IMAGE-BETA-FIBRES-40X100-232X50

prepared_image_properness_id:
    CAND-QDD-CERT-PREPARED-IMAGE-BETA-PROPER

prepared_entry_map_id:
    CAND-QDD-MAP-ENTER-PREPARED-HH

prepared_entry_domain_id:
    CAND-QDD-DOMAIN-EVAL-CONTEXT-X-PREPARED-IMAGE-BETA

prepared_entry_codomain_id:
    CAND-QDD-DOMAIN-K0-X-SUPPLIED-STATE-G

prepared_entry_domain_equality_id:
    CAND-QDD-EQ-EVAL-CONTEXT-X-PREPARED-IMAGE-BETA-PRODUCT

prepared_entry_codomain_equality_id:
    CAND-QDD-EQ-K0-X-SUPPLIED-STATE-G-PRODUCT

prepared_entry_totality_domain_id:
    CAND-QDD-DOMAIN-EVAL-CONTEXT-X-PREPARED-IMAGE-BETA

prepared_entry_totality_id:
    CAND-QDD-CERT-ENTER-PREPARED-HH-TOTAL

prepared_entry_equality_certificate_id:
    CAND-QDD-CERT-ENTER-PREPARED-HH-EQUALITY

prepared_entry_bijection_onto_image_id:
    CAND-QDD-CERT-ENTER-PREPARED-HH-BIJECTIVE-ONTO-K0-X-IMAGE
```

### 13.4 Separation and closure

```text
beta_six_ray_carrier_id:
    CAND-QDD-CARRIER-BETA-SIX-RAY-SEPARATOR

beta_six_ray_equality_id:
    CAND-QDD-EQ-BETA-SIX-RAY-Q4-ENTRYWISE

beta_six_ray_membership_map_id:
    CAND-QDD-MAP-IN-BETA-SIX-RAY

beta_six_ray_membership_domain_id:
    CAND-QDD-CARRIER-Q4

beta_six_ray_membership_domain_equality_id:
    CAND-QDD-EQ-Q4-ENTRYWISE

beta_six_ray_membership_codomain_id:
    CAND-QDD-CARRIER-TRUTH-BETA

beta_six_ray_membership_codomain_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

beta_six_ray_membership_totality_domain_id:
    CAND-QDD-CARRIER-Q4

beta_six_ray_membership_totality_id:
    CAND-QDD-CERT-IN-BETA-SIX-RAY-TOTAL

beta_six_ray_membership_equality_id:
    CAND-QDD-CERT-IN-BETA-SIX-RAY-EQUALITY

beta_six_ray_cardinality_id:
    CAND-QDD-CERT-BETA-SIX-RAY-CARD-6

beta_ray_state_map_id:
    CAND-QDD-MAP-BETA-RAY-TO-PREPARED-STATE-G

beta_ray_state_domain_id:
    CAND-QDD-CARRIER-BETA-SIX-RAY-SEPARATOR

beta_ray_state_codomain_id:
    CAND-QDD-CARRIER-PREPARED-IMAGE-BETA-N0

beta_ray_state_domain_equality_id:
    CAND-QDD-EQ-BETA-SIX-RAY-Q4-ENTRYWISE

beta_ray_state_codomain_equality_id:
    CAND-QDD-EQ-PREPARED-IMAGE-STATE-G-ENTRYWISE

beta_ray_state_totality_domain_id:
    CAND-QDD-CARRIER-BETA-SIX-RAY-SEPARATOR

beta_ray_state_totality_id:
    CAND-QDD-CERT-BETA-RAY-STATE-TOTAL

beta_ray_state_equality_certificate_id:
    CAND-QDD-CERT-BETA-RAY-STATE-EQUALITY

beta_ray_state_injectivity_id:
    CAND-QDD-CERT-BETA-RAY-STATE-INJECTIVE

beta_comparison_domain_id:
    CAND-QDD-DOMAIN-SOURCE-IMAGE-HH-SQUARED

beta_comparison_domain_equality_id:
    CAND-QDD-EQ-SOURCE-IMAGE-HH-SQUARED-PRODUCT

beta_six_agreement_map_id:
    CAND-QDD-MAP-AGREE-BETA-SIX-RAY

beta_six_agreement_domain_id:
    CAND-QDD-DOMAIN-SOURCE-IMAGE-HH-SQUARED

beta_six_agreement_domain_equality_id:
    CAND-QDD-EQ-SOURCE-IMAGE-HH-SQUARED-PRODUCT

beta_six_agreement_codomain_id:
    CAND-QDD-CARRIER-TRUTH-BETA

beta_six_agreement_codomain_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

beta_six_agreement_totality_domain_id:
    CAND-QDD-DOMAIN-SOURCE-IMAGE-HH-SQUARED

beta_six_agreement_totality_id:
    CAND-QDD-CERT-AGREE-BETA-SIX-RAY-TOTAL

beta_six_agreement_equality_id:
    CAND-QDD-CERT-AGREE-BETA-SIX-RAY-EQUALITY

beta_restricted_equality_id:
    CAND-QDD-EQ-HH-INSTRUMENT-ON-BETA-PREPARED-IMAGE

beta_restricted_membership_map_id:
    CAND-QDD-MAP-IN-EQ-BETA-PREP

beta_restricted_membership_domain_id:
    CAND-QDD-DOMAIN-SOURCE-IMAGE-HH-SQUARED

beta_restricted_membership_domain_equality_id:
    CAND-QDD-EQ-SOURCE-IMAGE-HH-SQUARED-PRODUCT

beta_restricted_membership_codomain_id:
    CAND-QDD-CARRIER-TRUTH-BETA

beta_restricted_membership_codomain_equality_id:
    CAND-QDD-EQ-TRUTH-BETA-LITERAL

beta_restricted_membership_totality_domain_id:
    CAND-QDD-DOMAIN-SOURCE-IMAGE-HH-SQUARED

beta_restricted_membership_totality_id:
    CAND-QDD-CERT-IN-EQ-BETA-PREP-TOTAL

beta_restricted_membership_equality_id:
    CAND-QDD-CERT-IN-EQ-BETA-PREP-EQUALITY

beta_six_ray_separation_id:
    CAND-QDD-CERT-BETA-SIX-RAY-SEPARATES-HH-SHADOWS

beta_six_ray_separation_proof_id:
    CAND-QDD-PROOF-BETA-SIX-RAY-SIGN-CONSISTENCY

beta_full_equality_agreement_id:
    CAND-QDD-CERT-EQ-BETA-PREP-EQUALS-EQ-INSTRUMENT-ON-SOURCE-IMAGE

beta_separation_dependency_ids:
    CAND-QDD-CARRIER-PREPARED-IMAGE-BETA-N0,
    CAND-QDD-CARRIER-BETA-SIX-RAY-SEPARATOR,
    CAND-QDD-MAP-BETA-RAY-TO-PREPARED-STATE-G,
    CAND-QDD-CERT-BETA-RAY-STATE-TOTAL,
    CAND-QDD-CERT-BETA-RAY-STATE-EQUALITY,
    CAND-QDD-CERT-BETA-RAY-STATE-INJECTIVE,
    CAND-QDD-SOURCE-IMAGE-K0-HH-READY-REDUCTIONS,
    CAND-QDD-MAP-K0-TO-HH-READY-INSTRUMENT,
    CAND-QDD-EQ-INSTRUMENT-OPERATIONAL

semantic_hidden_input_closure_id:
    CAND-QDD-CLOSURE-BETA-PREP-SEMANTIC-ALLOWLIST

implementation_hidden_input_closure_id:
    UNRESOLVED

prep_occurrence_relation_id:
    UNRESOLVED

prep_context_distribution_id:
    UNRESOLVED

eval_context_distribution_id:
    UNRESOLVED

prep_eval_pairing_law_id:
    UNRESOLVED
```
The schema names do not create public objects.

## 14. Public and physical fields that remain unresolved

The following remain literal `UNRESOLVED` or otherwise uncreated:

```text
public preparation-context carrier ID
public evaluation-context role ID
public PrepProcedure carrier ID
public PrepResult carrier and tag IDs
public RunPrep_beta map ID
public PhysPrep_beta relation ID
public PreparedImage_beta carrier ID
public six-ray certificate ID
all preparation, state, and entry layers
all preparation and source-state entry gates
all public dependency rows for the preparation surface
public completion-contract bindings
public factor-canonicity hidden_input_closure_id
transitive implementation hidden-input closure
physical preparation mechanism below the abstract procedure interface
procedure supply and occurrence
source-context supply and occurrence
lambda-kappa pairing law
procedure, source, state, and pair distributions
realized outcome and sampling
history update
writeback
completion-wide terminality
physical completeness
formal definition audit
formal source-image classification.
```

No existing public identifier is overloaded to fill these slots.

## 15. Timing disclosure

This owner choice was made after all of the following were visible:

```text
the preliminary exact nonformal count 146;
the same-source beta-diagonal caveat;
the full K0 x State_G(Q) product choice;
the exact supplied-state validator and role tag;
Public Canon v24 and its factor-canonicity overlay;
the derived 272-state normalized beta image;
the six beta-preparable separating rays.
```

Therefore:

```text
the beta procedure and image may define future work;
272 is not a blind scientific prediction;
the six-ray lemma is disclosed pre-probe analysis;
neither fact promotes 146;
future audits must preregister these expected values;
the preparation carrier may not be enlarged after a failed
classification.
```

No formal probe, verifier, scientific run, or data opening occurred.

## 16. Frozen output semantics

```text
OWNER-KERNEL-BETA-PREPARATION-FROZEN
    the proposal-local physical preparation instruction is exactly
    PREPARE_BETA(PREP_SOURCE(lambda)).

PREP-EVAL-ROLES-DISJOINT
    lambda and kappa inhabit disjoint role-tagged K0 copies.

PREP-EVAL-PAYLOAD-UNPACK-BIJECTIVE
    each role-tagged context enters an inherited bare-K0 map only through
    its exact total payload bijection.

PREPARED-ENTRY-TOTAL
    EvalContext_K0 x PreparedImage_beta enters the already frozen supplied
    product through one total exact map; this is not an occurrence law.

PREP-RUN-TOTAL-TAGGED
    all 15625 procedures return exactly one PREP_ZERO_BETA or
    PREP_SUCCESS_BETA result.

PREP-ZERO-25
    exactly 25 procedures have beta_Q(lambda)=0 and no normalized state.

PHYS-PREP-BETA-EXACT
    PhysPrep_beta is exactly the successful realization graph.

PREPARED-IMAGE-BETA-272
    the successful physical image contains exactly 272 supplied states.

PREPARED-IMAGE-PROPER
    the physical image is a proper finite subset of SuppliedState_G(Q).

PREP-FIBRES-EXACT
    40 prepared states have 100 successful procedure preimages and 232
    have 50.

BETA-SIX-RAY-SEPARATION
    six states in PreparedImage_beta separate every unequal pair in the
    inherited projected-Householder source image.

PREP-OCCURRENCE-UNRESOLVED
    procedure supply, occurrence, frequency, and lambda-kappa pairing are
    not inferred.

LAYER-AND-GATE-UNRESOLVED
    no physical layer placement or cross-layer permission is inferred.

IMPLEMENTATION-HIDDEN-INPUT-CLOSURE-UNRESOLVED
    no code, import, file, environment, clock, randomness, network, or
    dynamic-evaluation audit has yet been pinned.

BETA-PREP-PROCEDURE-PACKAGE-INCONSISTENT
    one displayed carrier, role, tag, map, relation, count, image,
    separation, equality, closure, or scope statement is false.

OWNER-INPUT-REQUIRED
    at least one public ID, layer, gate, dependency, implementation,
    occurrence, distribution, sampling, history, writeback, terminality, or
    physical-completeness field remains unresolved.

STOP
    a required public type, ID, layer, gate, dependency, closure,
    occurrence rule, or completeness proof is missing.

FIRE-POSTHOC
    a frozen procedure, role, tag, relation, image, equality, closure, or
    output meaning changes after classification opens.
```

The current combined output is

```text
OWNER-KERNEL-BETA-PREPARATION-FROZEN
PREP-EVAL-ROLES-DISJOINT
PREP-RUN-TOTAL-TAGGED
PREP-ZERO-25
PREP-EVAL-PAYLOAD-UNPACK-BIJECTIVE
PREPARED-ENTRY-TOTAL
PHYS-PREP-BETA-EXACT
PREPARED-IMAGE-BETA-272
PREPARED-IMAGE-PROPER
PREP-FIBRES-EXACT
BETA-SIX-RAY-SEPARATION
PREP-OCCURRENCE-UNRESOLVED
LAYER-AND-GATE-UNRESOLVED
IMPLEMENTATION-HIDDEN-INPUT-CLOSURE-UNRESOLVED
OWNER-INPUT-REQUIRED / STOP.
```

## 17. Exact status consequence

```text
preparation context payload                K0, inherited
preparation context role                   PREP_SOURCE, owner-adopted
evaluation context role                    EVAL_SOURCE, retained separately
preparation procedure                      PREPARE_BETA, owner-adopted
procedure equality                         tagged Eq_K0
role payload unpacking                      total exact bijections to K0
prepared-image admissibility entry          total, exact, not occurrence
procedure cardinal                         15625
execution map                              total and deterministic
zero branch                                25, tagged, no state
successful procedure domain                15600
physical realization relation              exact successful graph
prepared-state image                       272 exact pure states
six-ray vector-to-state map                total exact injection
prepared image surjective onto State_G     NO
prepared image fibre sizes                 40x100 and 232x50
same-source diagonal                       negative control only
arbitrary rational-ray preparation         NOT ADOPTED
finite rational convex mixing              NOT ADOPTED
mixed-state preparation                    UNRESOLVED
six-ray state-side separation              exact proposal-local theorem
inherited 146                              preliminary nonformal, not promoted
semantic free-variable closure             frozen
implementation closure                     UNRESOLVED

procedure occurrence                       UNRESOLVED
source occurrence                          UNRESOLVED
lambda-kappa pairing law                   UNRESOLVED
state and source distributions             UNRESOLVED
state and preparation layers               UNRESOLVED
physical preparation and entry gates       UNRESOLVED
public identifiers and dependencies        UNRESOLVED
sampling                                   UNRESOLVED
history update                             UNRESOLVED
writeback                                  UNRESOLVED
physical completeness                     UNRESOLVED
READY-FOR-CLASSIFICATION                   NO

A11                                        PARTIAL / O-STOP
QDD-PHYSICAL-EFFECT-SELECTION              O / STOP
QUADRATIC-DECODER-DATA                     O / STOP, unchanged
formal scientific run                      NONE.
```

No Canon theorem, registry row, dependency, public layer, public gate,
probe, verifier, evidence, occurrence law, distribution, parameter count,
physical uniqueness result, physical nonuniqueness result, or scientific
status move is produced.

## 18. Next allowed actions

1. Freeze the exact layer of `PrepContext_K0`, `PrepProcedure_beta`,
   `PrepResult_beta`, `SuppliedState_G(Q)`, and every preparation endpoint.
   Add a public gate only if the adopted map is genuinely cross-layer.
2. Freeze how a preparation procedure is supplied or occurs and whether a
   separate exact law pairs `lambda` with `kappa`. Do not infer a
   distribution.
3. Decide whether the program requires mixed-state physical preparation.
   If so, freeze its mechanism before adding mixed states to the image.
4. Create public preparation, state-input, instrument, effect, Born,
   outcome, and MatterData identifiers only through a later normative
   action.
5. If an implementation is proposed, pin its code, imports, files,
   environment, clock, randomness, network, and dynamic-evaluation closure
   before execution.
6. After the required layers, gates, public IDs, dependencies, and
   implementation closure are frozen, preregister the exact definition
   audit. Disclose expected counts 25, 15600, 272, and 146 before execution.
7. Keep the same-source beta diagonal as a mandatory negative control and
   keep the six-ray separator as a positive exact control.
8. Do not open physical `PASS`, `NONUNIQUE`, `EMPTY`, or classification
   output until the remaining public and completeness fields close.

No formal probe or Canon fold is authorized by this ruling.
