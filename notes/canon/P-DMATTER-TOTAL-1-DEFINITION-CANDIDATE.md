# P-DMATTER-TOTAL-1 Gram-spectral definition candidate (NON-CANONICAL)

Status: `DRAFT / STOP-DEFINITION`

This note refines the ruling in
`P-DMATTER-TOTAL-1-PREDEFINITION.md`. It freezes one exact algebraic
subcandidate and records the remaining definition debt. It is not a public
definition, probe, preregistration, verifier, run, or status proposal. It
changes no Canon object and authorizes no promotion.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          QUADRATIC-DECODER-DATA [O]
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
normative layer:    MULTI
future probe:       P-DMATTER-TOTAL-1
candidate:          QDD-GRAM-SPECTRAL-CANDIDATE-1
```

Public `main` is the authority surface. A private development head is not an
additional currency gate after the public cutover.

## Audit ruling

The proposed Gram-spectral algebra is exact, but it does not yet define a
complete `D_matter` candidate. In particular:

1. the Canon quadratic map is an ordered pair, not a right-Gram density;
2. coefficient dagger, transpose, and Gram adjoint are distinct typed
   operations even when dagger and transpose agree over `Q`;
3. a direct readout constructed from the same quadratic formulas would make
   the target factorization true by definition;
4. the physical measure dictionary, layer gate, completion-contract
   dependency, and several identifier-valued manifest slots are unresolved.

The lane therefore remains `STOP`. The definitions below reduce algebraic
debt without manufacturing a positive route.

## 1. Anchored carrier and balanced section

Let

```text
X  = F_5^6
K0 = { kappa_x = (U^n(0,x))_(n>=0) : x in X }
```

with equality in `K0` given by equality of the complete pointed forward
sequences. The only permitted read in this subcandidate is the pre-update
checkpoint at `n=0`.

Define the set-theoretic section

```text
ell(0)=0, ell(1)=1, ell(2)=2, ell(3)=-2, ell(4)=-1.
```

This is not a ring homomorphism. Put

```text
Veff = ell(F_5)^4 subset Q^4

beta(kappa_x)
  = (ell(p_1), ell(p_4), ell(p'_1), ell(p'_4))^T.
```

The checkpoint coordinates `q` and `r`, every later checkpoint, environment,
time, randomness, network input, and dynamic evaluation are forbidden inputs.

Proposed identifiers:

```text
CAND-READ-CHECKPOINT-N0-PRE
CAND-EQ-POINTED-FORWARD-SEQUENCE
CAND-REGION-PISTON4-N0
CAND-COARSE-IDENTITY-N0
CAND-CARRIER-BALANCED-PISTON4
CAND-BETA-BALANCED-PISTON-N0
```

These are proposal-local names. They do not satisfy the public-identifier
requirement of the completion contract until a later normative definition
fold adopts them.

## 2. Raw Gram, normalized Gram, and adjoints

Let `1` denote the all-ones column in `Q^4`. Freeze both scales explicitly:

```text
G0 = 5 I_4 - 1 1^T
G  = G0 / 5 = I_4 - (1/5) 1 1^T.
```

Thus `G0` has spectrum `(1,5,5,5)` and `G` has spectrum
`(1/5,1,1,1)`. The normalized object is used below; no equality of
unnormalized weights across these two scales is asserted.

Over the coefficient ring `Q`, the coefficient involution is trivial. For a
column vector `v` and a matrix `A`:

```text
v^dagger = v^T
transpose(A) = A^T
sharp_G(A) = G^(-1) A^T G.
```

The equality `v^dagger=v^T` does not identify `sharp_G` with ordinary
transpose.

Proposed identifiers:

```text
CAND-RING-Q-TRIVIAL-INVOLUTION
CAND-GRAM-GALOIS-Q4-RAW
CAND-GRAM-GALOIS-Q4-NORMALIZED
CAND-DAGGER-Q
CAND-TRANSPOSE-Q
CAND-G-ADJOINT-Q4
```

## 3. Canon-typed quadratic map

For `v in Veff`, let `A(v)=v v^T`. The candidate preserves the registered
ordered-pair type:

```text
Qcan(v) = (v v^dagger, v v^T) = (A(v), A(v)).
```

Define

```text
QCarrier = image(Qcan | Veff) subset M_4(Q) x M_4(Q)
```

with componentwise rational equality. It is not the set of all rational
rank-at-most-one matrices. The exact finite image has 313 elements: one zero
element and 312 nonzero sign-pair elements.

On the 15,625 anchored checkpoints, the zero fiber has size 25 and every
nonzero fiber has size 50. Consequently, a complete future fiber test must
cover both `q,r` blindness and the sign pair `v <-> -v`; varying only `q,r`
is insufficient.

The right-Gram numerator is a derived map, not `Qcan`:

```text
N_G(A) = A G.
```

Proposed identifiers:

```text
CAND-Q-ORDERED-PAIR-Q4
CAND-QCARRIER-EXACT-FINITE-IMAGE
CAND-QCARRIER-EQ-COMPONENTWISE-Q
CAND-RIGHT-GRAM-NUMERATOR
```

## 4. Algebraic spectral effects and weights

Define the two spectral idempotents of `G`:

```text
E_low  = (1/4) 1 1^T
E_high = I_4 - E_low.
```

They satisfy

```text
E_j^2 = E_j
sharp_G(E_j) = E_j
E_low + E_high = I_4.
```

For `(A,A) in QCarrier`, define

```text
m(A)      = Tr(A G)
w_j(A)    = Tr(E_j A G)
w_low(A) + w_high(A) = m(A).
```

For `v in Veff`, these reduce to

```text
m        = v^T G v
w_low    = (sum_i v_i)^2 / 20
w_high   = sum_i v_i^2 - (sum_i v_i)^2 / 4.
```

These are exact nonnegative rational weights. This note does not call them
physical probabilities: `MEASURE-BORN-VERB` does not by itself authorize a
generic Gram-spectral measurement dictionary.

No coupling dilation, Kraus family, Lueder instrument, or post-state update
is part of this candidate. In particular, no object named `U_QDD` is
introduced.

Proposed identifiers:

```text
CAND-EFFECT-GRAM-LOW
CAND-EFFECT-GRAM-HIGH
CAND-GRAM-TOTAL-WEIGHT
CAND-GRAM-SPECTRAL-WEIGHTS
```

## 5. Total algebraic codomain and factor map

Use a total tagged union; do not divide at the zero vector and do not emit a
bare null:

```text
CandidateQuadraticData =
  ZERO {
    support_state            = ZERO,
    total_weight             = 0,
    branch_weights           = (0,0),
    density_state            = ZERO_DENOMINATOR,
    normalized_weight_state  = ZERO_DENOMINATOR
  }
| NONZERO {
    support_state            = NONZERO,
    total_weight             = m(A),
    branch_weights           = (w_low(A),w_high(A)),
    density_state            = DENSITY(A G / m(A)),
    normalized_weight_state  = NORMALIZED((w_low(A),w_high(A))/m(A))
  }.
```

This gives one exact proposal-local factor map

```text
F_Gram : QCarrier -> CandidateQuadraticData.
```

The companion note
`P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` proves, in the standard
cyclotomic power basis, that this same factor has an exact trace-pairing
realization. It also supplies the explicit representation equality
`[T_w]_B0=A G` and matching total `ZERO`/`NONZERO` tags. This removes a
coordinate-typing ambiguity, but it does not supply an independently
published `D_direct`: the cyclotomic record is another realization of this
same Gram factor.

The classification amendment
`P-DMATTER-TOTAL-1-BRANCH-CLASSIFICATION.md` bounds the current frame
ambiguity without treating moving-basis matrices as equal. In its frozen
five-window class the scalar subrecord has one numerical class, the complete
fixed-basis record has five classes, and invariance of the branch projector
under the full group `Gal(Q(zeta_5)/Q)` leaves one split. That optional
filter is not adopted, and none of these proposal-local facts supplies an
independently published `D_direct`.

It does not yet give the required direct map

```text
D_direct : K0 -> MatterData_quadratic.
```

`D_direct` must come from an independently published reading rule. It may not
be defined through `Qcan`, `N_G`, `F_Gram`, or a shared factorization helper.
Inventing new `MatterData` fields from the formulas above and then showing
that those fields factor through `Qcan` would be outcome leakage, not closure
of `QUADRATIC-DECODER-DATA`.

## 6. Exact checks retained for a later definition package

The following checks are frozen as requirements, not claimed results of a
formal probe:

1. enumerate all 15,625 anchored inputs;
2. construct the exact ordered-pair `Qcan` key;
3. group and compare every complete `Qcan` fiber;
4. cover the zero fiber and all nonzero sign fibers;
5. check the tagged normalization predicates exactly over `Q`;
6. close the hidden-input allowlist transitively across imports, files,
   environment, clock, randomness, network, and dynamic evaluation;
7. verify the complete declared dependency DAG and its acyclicity;
8. keep direct and factor implementations structurally independent once a
   legitimate `D_direct` exists.

A valid implementation negative control is

```text
WRONG-FACTOR-OMIT-G:
    replace m(A)=Tr(A G) by m_wrong(A)=Tr(A), and
    replace Tr(E_j A G) by Tr(E_j A).
```

For `v=e_1`, the correct normalized low weight is `1/16`, whereas the wrong
factor gives `1/4`. Calling `v v^T` an "Euclidean Q" is not a valid fiber
negative control: over `Q`, `v v^T` is precisely each component of the
registered `Qcan`, and right multiplication by invertible `G` does not change
its fibers.

## 7. Residual definition ledger

| Contract surface | Exact state after this note | Required next decision |
| --- | --- | --- |
| anchored carrier and balanced section | algebraic proposal frozen | adopt public IDs and exact layer typing |
| Gram scale | raw and normalized forms distinguished | adopt one normative use per map |
| dagger / transpose / Gram adjoint | types separated | adopt public IDs |
| Canon-typed `Q` and equality | exact finite-image proposal frozen | adopt public IDs |
| algebraic effects and factor map | proposal frozen | decide physical reading and measure dictionary |
| `D_direct` | `UNRESOLVED`; the companion realizes `F_Gram`, while the bounded `C5` classification supplies no `D_direct` | separately adopt a complete scoped dictionary/write rule (`B0`, or a consistently re-frozen `c_1` after an optional `Adm_GalSplit` ruling) or retain the genuinely prior-readout requirement |
| complete `MatterData_quadratic` ownership | `UNRESOLVED` | freeze actual fields, roles, stage and leg |
| physics and measure identifiers | `UNRESOLVED` | no illegal `NOT_APPLICABLE` in identifier slots |
| bridge layer endpoints and gate | `UNRESOLVED` | add or identify a public gate before `READY` |
| completion-contract dependency | `UNRESOLVED` | decide a public dependency edge |
| closure manifest | partial only | `feeds_U=FALSE` is stage-local; `terminal_output_ids=[]` requires a public basis |

The v14 contract permits `NOT_APPLICABLE` only in its explicit state/leg
cases and only with a resolvable basis item. It cannot be inserted into
`source_id`, `current_id`, `propagator_id`, `metrology_id`, `scheme_id`, or
other identifier-valued slots. Those slots remain `UNRESOLVED` unless a
later definition-only contract fold introduces an explicit typed optional-ID
constructor.

## 8. Routing

```text
CURRENT:
    STOP-DEFINITION

OWNER ROUTING AFTER V15-OWNER-FOLD-107-109:
    the five-window root-injection search is CLOSED PROPOSAL-LOCALLY;
    the branch-projector Galois filter remains NOT ADOPTED;
    an optional filter-adoption fold is DEFERRED and requires a complete
    scoped dictionary/write package;
    search outside C5 is UNSCHEDULED until a genuinely prior typed readout
    candidate is supplied;
    D_direct remains UNRESOLVED and no classification result supplies it;

NEXT DEFINITION-ONLY PASS:
    complete MatterData_quadratic ownership;
    physical measure/dictionary ruling;
    exact L1--L6 bridge endpoints and gate
    completion-contract dependency ruling
    legal completion of every identifier-valued manifest slot

FORMAL PROBE:
    forbidden until every required public identifier resolves and both
    positive and negative outcomes remain reachable
```

This subcandidate is useful because it removes ambiguity in the algebraic
half of the factor map. It does not reduce the public frontier count and does
not move the scheduler from `STOP`.
