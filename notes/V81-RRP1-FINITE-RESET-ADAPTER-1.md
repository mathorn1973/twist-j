# RRP1: a finite reset adapter for two declared exposures

**NON-CANONICAL / PROPOSED DEFINITION / NOT IMPLEMENTED / NO FORMAL RUN.**
Physical use and full #539 conformance remain **STOP-DEFINITION**.

Basis: Public Canon v81, public commit
`82d536a71025032d6dd4093db61ecb9f31990250`, tag `canon-v81`.
Scientific owner: `QDD-INSTRUMENT-APPARATUS [O]`. The shared definition
surface is [#539](https://github.com/mathorn1973/twist-j/issues/539).

This work supplies a concrete candidate for the missing reset codomain,
including the information that must survive into the next preparation.
It reuses the existing TRC1 exposure law. It does not identify an external
apparatus, select an occurrence law, or classify the physical apparatus family.

## 1. The actual incompatibility

[RRP1 section 4](DECODER-RESERVOIR-PHYSICAL-PROFILE-1.md) and
[TRC1 section 3](TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md) return
`REJECTED_RESET_DISABLED`, retaining the old apparatus. The
[#539 map registry](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md) requires

```text
reset   : ApparatusState x ContextKey -> ReadyState x ApparatusState
prepare : SupportedSource x ContextKey x ReadyState
          -> SupportCarrier x ApparatusState.
```

There are two separate missing inputs. Reset cannot obtain a residual wave
pair from its arguments if that pair exists only in SupportCarrier. Prepare
cannot retain an old apparatus archive unless ReadyState carries it: prepare
has no ApparatusState argument. Changing the return tag alone fixes neither.

The proposal below gives both values explicit ownership. It also exposes a
third issue: #539 section 5 prohibits a later record selecting ReadyState.
Preserving an old record in a ready token needs an explicit separation of
custody from selection; the current wording does not automatically grant it.

## 2. One finite session, fixed before its first record

Use exactly two exposures, indexed `j=0,1`, of the unchanged TRC1 model with
one fixed context `c=(Gamma,q,N)`. The session source is an ordered plan
`H=(h_0,h_1)` of two explicitly supplied pointed U heads. These are two
preparations, not a reset or modification of U. No relation between their
heads, a source ensemble or independence is inferred.

The generated state domain is finite for each frozen `H,c` instance. The
family over arbitrary heads, rational contexts and horizons is not asserted
to be finite, and this construction supplies no uniform storage bound.

For this narrow adapter, both signed heads must be nonzero. A valid zero
head in either slot has disposition `REJECTED(ZERO_AMPLITUDE_SESSION_PLAN)`;
malformed input has a distinct `INVALID_REQUEST`. This is exclusion from
this proposed supported-source class, not a physical no-event claim or a
change to TRC1's existing zero-source branch. `N=0` and empty port support
remain admitted. Zero outgoing amplitudes and zero-crossing batches on an
admitted exposure remain ordinary complete TRC1 records.

The initial source plan, context, bank order and capacity are literal inputs
selected before either exposure. Comparing alternative values is a different
predeclared session. Neither bank order nor the next head depends on counts,
signs, outcomes, desired QDD weights or validation data.

Each bank owns a wave pair, its unused incoming slots, signed outgoing tape
and complete underlying TRC1 history. Its initial tag `UNPREPARED` is distinct
from a prepared zero pair, an empty event history or a record with no crossings.
There is no bank replacement, replenishment or erasure during this session.

## 3. Complete joint state and exact equalities

Define the finite session value

```text
A = (H, c, phase, j, bank_0, bank_1)
phase in {READY, RUNNING, COMPLETE}
bank_i = UNPREPARED | CoreHistory_i.
```

`CoreHistory_i` is the complete generated TRC1 history for `h_i,c`, including
its current residual Pair and core ApparatusState, full signed tape, heat and
underlying core EventRecords. No new session EventRecord occurs inside A.
Only the active prepared bank changes during an exposure. Earlier completed
banks retain their complete values; later banks remain UNPREPARED.

ApparatusState is A. SupportCarrier is its tagged ordered pair of bank-wave
projections. The external support argument to step must equal that projection
literally. It is a second description of the same joint state, never an extra
energetic copy. In particular, reset can retain the residual Pair because A
already owns it.

SourceEq compares the ordered full heads; ContextEq compares every component
of c and the fixed two-bank protocol identity; ApparatusEq compares all A
fields; SupportEq compares the tagged bank-wave projections. These are distinct
named comparisons, not energy, phase or sign quotients.

ReadyState is a record

```text
Ready = (selection=(H,c,j,COLD_FRESH_BANK_j), custody=A_ready).
```

ReadyEq compares both fields exactly. The selection projection names the
already reserved fresh bank. Custody retains the full old state and is not
erased or quotiented. A contains no Ready value, so this construction is not
recursive. A saved snapshot alone is not a physical storage certificate.

## 4. Proposed maps and their exact domains

| Map | Domain and assigned value |
|---|---|
| `ready_select(H,c)` | Valid supported plan and fixed c. Construct `A_0=(H,c,READY,0,UNPREPARED,UNPREPARED)` and return its Ready record. No result is read. |
| `prepare(H,c,Ready)` | Literal matching H,c; custody is a reachable READY state; `Ready.selection=(custody.H,custody.c,custody.j,COLD_FRESH_BANK_custody.j)`; designated bank is UNPREPARED and every earlier bank is complete. Initialize only bank j using TRC1's unchanged one-kick preparation. Retain all other banks; return the support projection and A with phase RUNNING, or COMPLETE immediately when N=0. |
| `step(S,A,c)` | Matching c and `S=support(A)`; phase RUNNING; active core cut `t<N`. Apply exactly one unchanged TRC1 core step and compatible core append. Update only bank j; set phase COMPLETE iff its new cut is N. Produce delta with j, the full core event, and complete old/new A snapshots. Return `(core_outcome,support(A_after),A_after,delta)`. |
| `emit` | Exact image of the session step. Package the entire delta as one session event, including zero-crossing batches. Event equality retains j and all delta fields. |
| `persist(A,o,event)` | Exact matching step image. Return event.A_after. It must equal the apparatus returned by step. |
| `reread(event)` | Return the same event. No step, bank advance, source kick or new event occurs. |
| `reset(A,c)` | Matching c; phase COMPLETE; j=0; bank 0 is a full N-step generated history and bank 1 is UNPREPARED. Assign `A_next=(H,c,READY,1,bank_0,UNPREPARED)` and return `(Ready(selection for bank 1,custody=A_next), A_next)`. |

Reset does not call prepare, emit an interaction, add a source kick, change a
core record, zero a tape or remove a residual Pair. Its two outputs carry the
same A_next value. The next prepare consumes this Ready value, so old custody
does not disappear at the signature boundary. Source 1 is used only by that
next, separately named preparation.

The complement of `D_reset` consists of every other input: incomplete exposure,
already READY, exhausted second bank, mismatched context or malformed state.
There is no third exposure. A public API can report a domain error while
leaving the input unchanged, but that error is not a value of the mathematical
reset codomain. A COMPLETE second bank terminates the finite session.

Thus `D_reset` is a proper subset of `ApparatusState x ContextKey`.
Whether #539 admits that restricted domain under its displayed product
signature is a separate **OPEN domain ruling**. Listing exact domain
metadata does not itself settle that ruling or make the reset total.

Admitted action histories preserve the order
`prepare_0, N core steps, reset, prepare_1, N core steps`.
Passive reads may occur between these actions. N=0 has two preparations and
one reset, but no interaction events. Administrative preparation/reset entries
belong to an action journal and are never counted as detection events.
One Ready value is used at its corresponding preparation position in this
history; this is a protocol rule, not a claim that a copyable token enforces
physical single use. Starting a new session requires a new explicitly owned
resource allocation.

HistoryState is the ordered sequence of full session EventRecords, including
`j`, the core event and complete `A_before/A_after` snapshots. The ordered
tagged core-event sequence is only a named projection of HistoryState, not
its replacement. A session APPEND requires the next compatible action
position and full step image; it never stores a session event back inside A.
Core histories inside A contain only the unmodified core snapshot type.
This avoids a cycle of session events containing their own apparatus_after
snapshots.

## 5. What the resource account actually consumes

There are two distinct wave carriers and at most `2*N*|R|` fresh cold port
slots, plus the signed outgoing tapes and complete record/custody storage.
The heat, counts and remainder summarize each tape's same energy; they are
not additional energy reservoirs. Immutable sharing does not establish a
physical memory capacity or a bound in bits for exact rational states.

For a prepared bank i retain the inherited account

```text
E(P_i) + sum_x heat_i(x) = m(z_i)/2.
```

The proposed joint bookkeeping sums this expression over prepared banks.
Each prepare adds its own source kick `m(z_i)/2`; each core step preserves
the inherited account; reset merely advances the bank descriptor and adds
or discards no modeled energy. At session completion both residual Pairs
remain in custody. Hiding the old residual or counting only outgoing heat
would fail this account.

Keeping the inactive old bank unchanged is an **additional isolation/local
clock convention** of this session wrapper. It is not an inherited physical
TRC1 law. A realizable apparatus must independently explain retention or
continued evolution of that residual, the two wave carriers, cold supply,
storage, two preparation kicks and reset duration/work. No zero physical
reset cost, passive storage law or physical time assignment is claimed.

## 6. Exact proposed #539 ruling, not an adopted amendment

The following is proposed review text for LAW-READY-PRESELECTION, alongside
the existing ban on output-selected preparations:

> A ready carrier may contain separately typed selection and immutable
> custody fields. Full ReadyEq retains both. Selection of the next source,
> context, bank, coupling, clock, threshold and outcome interpretation must
> factor through the predeclared source/context/resource schedule and the
> declared completion position. Replacing a retained history by any other
> admissible history at that same position must leave those selections
> unchanged. Custody may preserve the old complete state, but may neither
> choose those selections nor alter the next bank's law. The finite resource
> and exact map domains must be explicit. This exception does not license
> adaptive measurement or a source law derived from observed outcomes.

The selection functions must structurally consume only frozen `H,c,j` and
the protocol descriptor. Retained event, tape and amplitude fields cannot
control selection, new preparation, exposure law or new-cycle core outputs.
Custody may be read for compatibility checks, exact copying, passive reads
and resource accounting. Compatible custody changes can affect retained
fields and prior provenance, but not the new bank's generated core outputs.
This field-dependency obligation is necessary because the counterfactual
history comparison alone can be vacuous for deterministic TRC1 at fixed
`H,c` and cut.

This is an observable independence obligation for a later implementation
review, not permission to ignore full record equality. Ready's custody does
depend on old records. Consequently the existing literal #539 prohibition
does not by itself certify this proposal. The proposed ruling and every
other #539 law still require review; this note does not mark the shared
schema complete or change its current wording.

A second, independent proposed ruling concerns the reset domain:

> A finite preallocated profile may declare
> `reset : D_reset -> ReadyState x ApparatusState`, with `D_reset` an
> explicitly published decidable subset of `ApparatusState x ContextKey`.
> The domain must include every coherent state at every reset boundary
> admitted by the frozen protocol. Among coherent states, eligibility may
> depend only on matching context, the declared completion cut and unused
> reserved capacity, never on amplitudes, outcomes or desired records.
> Reset must be functional and total on `D_reset`, and its output must
> satisfy the next preparation's published compatibility predicate.
> Every other reachable protocol position must have a predeclared
> non-reset or exhaustion disposition. Administrative errors outside
> `D_reset` are not reset outputs and cannot count as successful resets.
> Acceptance of this restricted signature establishes no total reset on
> the full Cartesian product.

Here `D_reset` is exactly the coherent matching states with phase COMPLETE,
j=0, a complete N-step bank-0 history and bank 1 UNPREPARED. This rule and
its application remain proposed and unadopted. Neither the custody proposal
nor an implementation can silently amend #539's total-signature
interpretation. Both rulings remain open.

## 7. Disposition and the next concrete work

The missing residual-state and preparation-custody inputs now have explicit
candidate carriers, and the reset returns the requested product on one
specified domain, finite for each frozen `H,c`. This is a design disposition,
with **no execution evidence and no physical closure**. The existing RRP1/TRC1 reset functions
and all completed probe files are unchanged.

The next bounded implementation is this adapter after decisions on both
the custody/selection and restricted-domain rulings. Its acceptance cases
are: complete first exposure with nonzero residual and signed tape; zero-crossing and multiple
crossing records; N=0; empty R; repeated passive reads; incomplete/exhausted
reset rejection; exact archive survival through the second prepare; and
absence of record-to-source/context/bank selection. A formal claim needs its
own public pin and accepted verifier before execution. None has been run here.

For physical use, neither the descriptor advance nor a second mathematical
bank is a detector reset certificate. In particular the NIST observation
adapter is still a separate source with no RRP1/TRC1 identification. A
complete calibrated realization and finite capacity/retention/reset evidence
remain required, along with the unchanged apparatus-family and occurrence
obligations.

## Sources at the pinned public basis

- [RRP1](DECODER-RESERVOIR-PHYSICAL-PROFILE-1.md), sections 2-4: finite cold
  capacity, full signed tape, exact reset mismatch.
- [TRC1](TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md), sections 1, 3 and 5:
  pointed sources, unchanged exposure law, reset exclusion, ensemble premise.
- [TRC1 proof](../probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/PROOF.md),
  section 1: generated complete histories and energy account; no reset claim.
- [Typed contract](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md), sections
  3-9: distinct equalities, map domains, preselection and acyclic ownership.
- [Canon](../canon/CANON.md), RECORD-LOADER-RETENTION-CLASS and
  OCCURRENCE-ADDRESS-AND-LOG-EQUALITY: fresh-space, retention and identity
  boundaries; no physical certificate follows from symbolic storage.
