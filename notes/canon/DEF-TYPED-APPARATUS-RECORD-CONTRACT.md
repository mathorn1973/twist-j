# DEF-TYPED-APPARATUS-RECORD-CONTRACT

Status: **NON-CANONICAL / STOP-DEFINITION / NO SCIENTIFIC AUTHORITY**.
Owner lane: issue #539.
Revision: `DEF-TYPED-APPARATUS-RECORD-CONTRACT-v1`.
Basis: Public Canon v81, public `main` at `82d536a71025032d6dd4093db61ecb9f31990250`.
Content commit: `72863e7014a770eb19d5f54fee0fbf253a6a2cc9`.
Canon SHA-256: `940e1d192f729c16fcb74b6e6ac1b8f02d1050326b6164affb276684c8696fbf`.
Canon bytes: 568924.

The original v0 proposal was based on Public Canon v61 at
`25440d1dd872e1e91f6a4e01d85bad45a4062eb8`. That is historical provenance,
not this revision's authority basis. This non-canonical revision adopts the
ready-custody, restricted-reset-domain and total-history-append conventions
below following author review. Their adoption here is not a merged public
schema change, a scientific result or a completed profile conformance decision.
Existing profile manifests retain their declared contract versions and map
conventions; this revision does not silently retrofit them.

This note proposes one reusable typed manifest contract at the L4 support to
L5 stream boundary. It creates no apparatus, event, decoder, observation,
measure, gate, claim or status. It is a specification surface against which
later profile candidates can be preregistered and falsified.

The motivating obligations remain separate. Their v81 routing is:

```text
QDD-INSTRUMENT-APPARATUS [O]
MINIMAL-READ-DERIVATION [O]
O-LINEAR-READING-APPARATUS-LIFT [proposed only]
```

`QUADRATIC-DECODER-DATA` was a motivating O in the original proposal. At
v81 it is not a live registry row: the admitted algebraic reading is
`ALGEBRAIC-DMATTER [D]`, while its transferred physical debt is owned by
`QDD-INSTRUMENT-APPARATUS [O]`. This revision preserves that separation.

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

`HistoryState` is the broad carrier `EventRecord*` of all finite event-record
sequences. Reachable histories of a finite protocol are a separately
specified subset, not a substitute for this carrier. Profiles also publish
their `ProtocolState` and `ActionJournal` carriers and exact equalities for
the separate admissibility predicate. A singleton is allowed only when the
profile has no additional protocol position or administrative distinction
to retain; preparation and reset cannot be hidden by that choice.

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

reset : D_reset -> ReadyState x ApparatusState
        D_reset subset of ApparatusState x ContextKey

admissible_extension : ProtocolState x HistoryState x EventRecord -> {0,1}

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

`D_reset` is an explicit typed domain, with its membership predicate and
equality inherited from the ambient product. The accepted restricted-domain
convention in section 5.2 does not relax the full Cartesian domain of
`append`. `admissible_extension` is a separate total predicate; it cannot
turn algebraic append into a partial function.

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

The context key and ready selection are fixed before the output target is
known. Any rule that reads desired effects, target frequencies, a chosen
outcome or a later event record to select `ContextKey` or the selection
component of `ReadyState` is classified `CIRCULAR`. Section 5.1 specifies
exactly when old state may instead occur as retained custody.

### 5.1 Ready selection and retained custody

A ready carrier may contain separately typed `ReadyChoice` and immutable
`CustodyPayload`. Full `ReadyEq` compares both fields under their published
exact equalities; a profile cannot erase custody by comparing only the choice.
Every datum controlling the next source, context, bank, ready phase, incoming
slots, preparation, coupling, clock, threshold, exposure or outcome
interpretation belongs to `ReadyChoice`.

Selection functions consume only the predeclared source/context/resource
schedule and the declared protocol position. Retained event, tape and
amplitude fields cannot control those selections, the new preparation or
the next interaction law. Custody may be read for literal compatibility
checks, preservation, passive inspection and exact resource accounting.
Changing admissible custody at the same selection and protocol position may
change retained fields and explicit prior-state provenance, but cannot change
new-cycle core outputs. The profile publishes both this noninterference
condition and the structural field dependencies: comparison of alternative
histories alone may be vacuous for a deterministic source at a fixed cut.

Ready validity includes exact compatibility of the selection with its
custody and reserved capacity. If `prepare` has no separate apparatus input,
the ready value must carry all prior state that preparation must retain.
If `reset` has no support input, its apparatus argument must own every
residual support value that reset must retain, or its domain must exclude
that operation explicitly. Aliased support/state descriptions are one store;
snapshots require an acyclic ownership construction.

This convention permits retained prior records; it does not permit adaptive
selection from them. It supplies no statistical independence, source
ensemble, occurrence law, physical memory, or physical preparation certificate.

### 5.2 Restricted reset domain

A finite preallocated profile may declare the restricted reset signature in
section 4, with an explicit decidable `D_reset`. The domain must include every
coherent state at every reset boundary admitted by the frozen protocol.
Among coherent states, eligibility may depend only on matching context,
the declared completion cut and unused reserved capacity, never on amplitudes,
outcomes or desired records. Reset must be functional and total on `D_reset`; its output must
satisfy the next preparation's published compatibility predicate.

Every other reachable protocol position has a predeclared non-reset or
exhaustion disposition. An administrative error outside `D_reset` is not a
reset output or a successful reset. Exhaustion does not create a fresh bank,
erase old state or license another exposure. Acceptance of this restricted
signature establishes no total reset on the full ambient Cartesian product
and no physical reset or resource certificate.

For the two-exposure adapter, the declared domain is exactly coherent
matching states with `phase=COMPLETE`, `j=0`, a complete N-step bank-0 history
and bank 1 `UNPREPARED`. That example does not replace another profile's
domain predicate or establish its implementation conformance.

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

The history convention of this revision is exactly

```text
HistoryState = EventRecord*
empty_history = ()
append(h,e) = h concatenated with (e)
```

Append is total on every `HistoryState x EventRecord` input, including
physically or procedurally incompatible pairs. `HistoryEq` compares lengths
and corresponding records using full `EventRecordEq`. Concatenation has its
ordinary associative law and empty-sequence identity. This broad finite-word
carrier is generally infinite; it is not a claim of infinite apparatus
capacity or physically realizable arbitrary histories.

Each profile must publish:

```text
empty_history
length
head/tail or equivalent order access
append_associativity convention
passive_reread rule
fresh_interaction rule
history equality
admissible_extension predicate
reachable_history predicate and finite-domain scope
protocol state, action journal and their update/ownership rules
```

`admissible_extension(p,h,e)` decides whether the current protocol state,
history and prospective full event form the next admitted interaction. It
checks the declared action position, context, exact step/emit image and state
continuity. Rejecting this predicate does not make `append(h,e)` undefined;
the resulting word simply need not be a reachable history. A physical or
modeled execution extends its stream only by admitted events. No replacement
of a full session event by its core-event projection is implicit.

The profile retains a protocol state and action journal for preparation,
reset, exhaustion and zero dispositions separately from the event sequence.
For N=0, the event sequence is empty before and after both preparations and
reset, so it cannot determine the current action position. The journal's
typed actions, equality and ownership, together with the current apparatus
state, must distinguish these positions without an implicit global counter.
Administrative actions do not become detection events merely by being logged.
Reachability is derived from this declared initial state and protocol. Finite
reachable histories for a fixed source/context/resource plan do not make
`EventRecord*` finite.

Passive rereading emits no new event or protocol advance unless a new action
is explicitly declared; any persistent read log needs its own capacity rule.
Fresh accepted interaction invokes `step` and appends its one complete
emitted `EventRecord`. A `ZERO_EVENT(e)` disposition contributes its declared
event under the profile's separate zero-branch rule; `NO_EVENT` and `REJECTED`
are retained as administrative dispositions without adding an untyped value
to `EventRecord*`. These typing rules imply no physical no-event law or
statistical independence of successive interactions.

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
LAW-RESET-DOMAIN
LAW-RECORD-FIELD-OWNERSHIP
LAW-RECORD-FAITHFULNESS
LAW-APPEND-TOTALITY
LAW-HISTORY-ADMISSIBILITY
LAW-PROTOCOL-POSITION
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

For a finite session, graph vertices distinguish its declared action
positions and prior/new state values. Retaining an earlier record as custody
does not permit a reference cycle through the current event's own
apparatus_after snapshot or an event-to-selection dependency.

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

and their exact equalities. The historical NON-CANONICAL promotion package
`PROMO-C-QDD-DIRECT-RECORD-QUOTIENT-1` is not the authority for the current
binding: v81's `ALGEBRAIC-DMATTER` and `QDD-ALGEBRAIC-FACTORIZATION` supply
their own exact registered scope and evidence.

This adapter still requires decoder ownership of every emitted field, a
complete profile graph and conformance to the active decoder completion
contract. It does not extend the algebraic binding to a physical apparatus,
adopt an occurrence law or L6 measure, or discharge the live
`QDD-INSTRUMENT-APPARATUS` obligation.

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
an inventory template, not an executable validator or a candidate profile,
and cannot be cited as one. Adopting the three conventions in this revision
does not fill unresolved profile, gate, carrier, equality or decision slots.
No formal verifier or formal run belongs to this shared definition revision.

A later Canon fold may add this contract only as a definition without a claim
status. Each adapter remains a separate scientific lane with its own owner,
preregistration, evidence, gate and falsifier.
