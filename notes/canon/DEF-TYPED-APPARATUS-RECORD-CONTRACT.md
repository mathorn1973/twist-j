# DEF-TYPED-APPARATUS-RECORD-CONTRACT

Status: **NON-CANONICAL / STOP-DEFINITION / NO SCIENTIFIC AUTHORITY**.
Owner lane: issue #539.
Basis: Public Canon v61, public `main` at `25440d1dd872e1e91f6a4e01d85bad45a4062eb8`.
Content commit: `76b405033b41397cd62217bf3998ac9c26111964`.
Canon SHA-256: `e9ee0781e489e1c3951b978be567a19c5c7370708095631f966561efe03b6cb5`.
Canon bytes: 334100.

This note proposes one reusable typed manifest contract at the L4 support to
L5 stream boundary. It creates no apparatus, event, decoder, observation,
measure, gate, claim or status. It is a specification surface against which
later profile candidates can be preregistered and falsified.

The motivating public obligations remain separate:

```text
QUADRATIC-DECODER-DATA [O]
QDD-INSTRUMENT-APPARATUS [O]
MINIMAL-READ-DERIVATION [O]
O-LINEAR-READING-APPARATUS-LIFT [proposed only]
```

One conforming manifest does not close another profile. Shared syntax creates
no shared scientific edge.

## 1. Layer boundary

A profile conforming to this contract has exactly three declared layer roles:

```text
source_layer   the layer on which admitted source data are defined;
support_layer  L4, the effective support carrier acted on by the apparatus;
stream_layer   L5, the ordered event/history carrier emitted by the apparatus.
```

For the current public read-only decoder architecture:

```text
feeds_U = false.
```

No output of `prepare`, `step`, `emit`, `append`, `persist` or `reset` may alter
`Omega`, `U`, a kernel generator, the selector or the public counter. A profile
with `feeds_U=true` is a different architecture and requires its own public
architecture definition before this contract can type it.

An L4 to L5 scientific statement requires a separately registered gate. This
contract records the proposed gate identifier and endpoints but cannot create,
run or pass the gate.

L6 is outside this contract. Counts, frequencies and normalized rational
fields remain L5 records. Calling them probability or measure requires a
separate L5 to L6 gate and dictionary.

## 2. Manifest identity

A profile manifest has the immutable administrative fields

```text
contract_version
profile_id
profile_version
owner_issue
basis_commit
status
source_layer
support_layer
stream_layer
feeds_U
gate_id
```

Allowed definition states are

```text
STOP-DEFINITION
READY-DEFINITION
```

Neither is a scientific status. `READY-DEFINITION` says only that every type,
equality, map, dependency and decision procedure is published without an
unresolved slot.

## 3. Carrier registry

Every carrier entry has

```text
carrier_id
layer
scope
construction
nonempty_decision
finite_decision
source_ids
equality_id
```

The following carrier roles are mandatory and distinct:

```text
Source
SupportedSource
ContextKey
ReadyState
ApparatusState
SupportCarrier
Outcome
RecordDelta
EventRecord
HistoryState
```

`SupportedSource` is either a published subtype of `Source` or the image of a
published support predicate. It cannot be inferred from a denominator used
later in a formula.

Each `equality_id` names a separately published exact equivalence relation and
a decision procedure where equality is decidable. These equalities may not be
silently identified:

```text
SourceEq
ContextEq
ReadyEq
ApparatusEq
SupportEq
OutcomeEq
RecordDeltaEq
EventRecordEq
HistoryEq
```

In particular, projective sign, phase relabeling, equality of effects,
equality of occurrence weights, equality of post-state rays and equality of
complete apparatus laws are different relations unless an exact theorem and
explicit adapter identify them.

## 4. Map registry

Every map or relation entry has

```text
map_id
map_kind            FUNCTION or RELATION
source_product
codomain
graph_predicate
domain_predicate
totality_decision
functionality_decision
surjectivity_decision
injectivity_decision
consumed_ids
emitted_field_ids
```

For `map_kind=RELATION`, existence and uniqueness are unresolved until the
named exact decision procedures classify them. A bare existential dilation or
coupling does not define an apparatus law.

The required maps are:

```text
context_of : Source -> ContextKey

support_map : Source -> tagged union
              UNSUPPORTED + SupportedSource

ready_select : SupportedSource x ContextKey -> ReadyState

prepare : SupportedSource x ContextKey x ReadyState
          -> SupportCarrier x ApparatusState

step : SupportCarrier x ApparatusState x ContextKey
       -> Outcome x SupportCarrier x ApparatusState x RecordDelta

emit : Outcome x SupportCarrier x ApparatusState x RecordDelta
       -> EventRecord

append : HistoryState x EventRecord -> HistoryState

persist : ApparatusState x Outcome x EventRecord -> ApparatusState

reset : ApparatusState x ContextKey -> ReadyState x ApparatusState

terminal : EventRecord -> {0,1}

zero_support : Source -> ZeroDisposition
```

`ZeroDisposition` is a published tagged carrier containing exactly the profile
choices admitted from

```text
NO_EVENT
ZERO_EVENT(EventRecord)
REJECTED(reason_id)
```

A profile may admit one or more tags only when the source partition and the
subsequent history semantics for each tag are complete. Division by zero is
never a disposition.

## 5. Step semantics

A functional `step` owns one complete transition law. For input

```text
(s,a,c) in SupportCarrier x ApparatusState x ContextKey
```

it returns exactly one tuple

```text
(o,s',a',delta).
```

If an outcome is intended to remain nonselected, `step` must be declared a
relation and the profile remains `STOP-DEFINITION` until a selector or a
complete negative classification is published. An unordered family of branch
maps is not a realized-event transducer.

`persist` and the apparatus component returned by `step` must agree under the
profile's exact coherence equation. `reset` is a distinct operation. A fresh
preparation cannot be substituted silently for persistent continuation.

The context key and ready state are selected before the output target is
known. Any rule that reads desired effects, target frequencies, a chosen
outcome or a later event record to select `ContextKey` or `ReadyState` is
classified `CIRCULAR`.

## 6. Record ownership

Every `EventRecord` field has

```text
field_id
field_type
field_equality_id
source_map_id
totality_decision
zero_branch_rule
```

A field has one owner map. A value appearing in two algebraically equal
presentations does not give it two independent sources.

The complete `EventRecordEq` is frozen before any selector, terminality or
apparatus comparison. A profile must state whether record equality includes or
excludes context, ready phase, apparatus state, support before/after, outcome,
record delta and terminal tag.

`emit` may compress the transition only after it proves that every retained
field is constant on the declared compression fibres. Two transitions
separated by the intended apparatus action but equal under `EventRecordEq`
fire the profile's record-faithfulness falsifier unless the loss was explicitly
excluded from scope before comparison.

## 7. Ordered history

`HistoryState` is an ordered L5 carrier. The `append` map must be total and must
publish:

```text
empty_history
length
head/tail or equivalent order access
append_associativity convention
passive_reread rule
fresh_interaction rule
history equality
```

Passive rereading emits no new event unless the profile explicitly defines a
new read event. Fresh interaction invokes `step` and appends exactly one
completed event or one explicit zero disposition.

Any idempotent, terminal or saturation quotient of histories is a separate
named map with its own equality. It cannot replace the append-only history in
the definition of a realized-event stream.

## 8. Required law registry

Every profile must provide one exact decision procedure for each law ID:

```text
LAW-TYPE-CLOSURE
LAW-DOMAIN-TOTALITY
LAW-ZERO-DISPOSITION
LAW-CONTEXT-PRESELECTION
LAW-READY-PRESELECTION
LAW-STEP-FUNCTIONALITY
LAW-PERSIST-COHERENCE
LAW-RESET-SEPARATION
LAW-RECORD-FIELD-OWNERSHIP
LAW-RECORD-FAITHFULNESS
LAW-APPEND-TOTALITY
LAW-ORDER-PRESERVATION
LAW-REREAD-FRESH-SEPARATION
LAW-NO-FEEDBACK
LAW-NO-HIDDEN-INPUT
LAW-DEPENDENCY-ACYCLICITY
LAW-L4-L5-GATE-DECLARATION
LAW-L6-EXCLUSION
LAW-DECISION-ROUTING
```

A decision procedure may return `PASS`, `FAIL`, `EMPTY` or `STOP` only under
conditions published in the profile. No threshold or admitted class may move
after preregistration.

## 9. Dependency graph

Every consumed object appears in `dependency_ids`. The manifest defines a
finite directed graph whose vertices include carriers, equalities, maps,
fields, laws, external definitions and proposed gate endpoints.

The graph must be acyclic after removing only the explicit historical
`BOUNDED_BY` reporting edges. These cycles are prohibited:

```text
target effect -> context/ready selection -> apparatus -> same target effect;
output record -> source preparation -> same output record;
normalized occurrence target -> transition rule -> same normalized target;
terminal predicate -> record equality -> same terminal predicate;
future history -> current step -> same future history.
```

An unlisted clock, environment, seed, phase, accumulator, target, oracle or
normalization input fires `LAW-NO-HIDDEN-INPUT`.

## 10. Decision routing

A scientific profile built on this definition must preregister four disjoint
routes:

```text
POSITIVE
  every declared type and law passes and the profile-specific scientific
  statement passes its separately registered gate;

NEGATIVE
  the complete frozen admissible class is nonempty and an exact counterexample
  fires a named scientific condition;

EMPTY
  the complete frozen admissible class is proved empty;

STOP
  the definition, class, equality, dependency graph, evidence, gate or exact
  decision is incomplete.
```

Failure of one favored construction is `STOP` unless the frozen complete class
has been classified.

## 11. Profile adapters

### 11.1 QDD decoder-data adapter

Candidate source assignments may name the public

```text
K_QDD
QCarrier_QDD
MatterData_QDD
D_QDD_direct
```

and their exact equalities. The NON-CANONICAL promotion package
`PROMO-C-QDD-DIRECT-RECORD-QUOTIENT-1` is review material only until a formal
child probe earns public evidence.

This adapter still requires decoder ownership of every emitted field, a
complete profile graph and conformance to the active decoder completion
contract. It does not remove the existing dependencies of
`QUADRATIC-DECODER-DATA`, adopt the Born measure dictionary, or close that O
row.

### 11.2 QDD apparatus adapter

This profile must supply, rather than merely cite:

```text
physical ContextKey;
selected ReadyState/phase;
complete ApparatusEq on whole laws;
functional step or exact complete negative classification;
persist/reset semantics;
ZERO_SUPPORT disposition;
ordered EventRecord and HistoryState;
L4 to L5 gate identifier and endpoints.
```

Existing effect fibres, rational dilations, carry banks, finite-memory
families and U-induced classifications remain inputs or boundaries. None is a
selected realized-event transducer by itself.

### 11.3 Minimal-read adapter

This profile freezes the exact L5 fields consumed by the proposed L1 coin
selector, together with the accumulator, redundancy rule, protocol class and
history equality. It may not use `MINIMAL-READ`, `w=1` or `beta_1` as a
construction premise.

### 11.4 Linear-reading adapter

This profile may consume a registered L1 invariant or character-covariant
reading only as source data. It must independently publish the L4 support
carrier, apparatus law, EventRecord codomain, HistoryState and L4 to L5 gate.
A nonzero covariant polynomial is not itself an observation.

## 12. Definition status

The proposed definition is `READY-DEFINITION` only when a reviewed version of
this contract and its machine-readable manifest schema contain no undefined
identifier, implicit equality or unresolved validator requirement.

The template file beside this note is intentionally `STOP-DEFINITION`. It is
not a candidate profile and cannot be cited as one.

A later Canon fold may add this contract only as a definition without a claim
status. Each adapter remains a separate scientific lane with its own owner,
preregistration, evidence, gate and falsifier.
