# Formal records and the next actual-history interface

**PUBLIC, NON-CANONICAL. Specification annex to PREREG.md, not an
actual-outcome mechanism or an earned theorem.** Original work,
Apache-2.0. Owner: A. M. Thorn. Prepared 2 October 2026 for issue #1333.
Coordinator-authored with disclosed control_ownership contract assistance;
neither contribution is the fresh independent review.

The receiving references are exact C at
`024936502544c2ec45acc8890a052c7b3aca26be` and approximate preparation P at
`1f88665ce8646cdf134cb4366958db0ca2d302d7`. All positive statements below
are conditional on the internal-controller claims in this candidate's
PREREG being proved. No new scientific execution is authorized by this
annex. The public source freeze and review procedure are the same as for
the main specification.

## State description and available record object

This candidate uses category 2: the complete vector/density on its declared
complex extension, evolved by its fixed unitary F. The carrier retains the
source, packet geometry, pointers, archive flags, every fresh/spent bath,
program, descriptor, mobile head, counters, scratch, operand buses and
invocation/context metadata. An arbitrary finite reference is retained.
The density is not identified with a native integer configuration or with
one selected component of a coherent record state.

For a supported initialized classical program, the controller supplies a
chronology during its first forward execution and declared read window.
The stored metadata and controller phase identify the invocation, context,
archive slot and completed-round boundary in that interval. The finite
epoch/cursor fields are not an absolute unbounded history counter. After
the inverse tail, reused labels do not denote newly prepared independent
sources or permanent old records.

Four objects remain distinct:

| Object | Meaning and limit |
|---|---|
| Funded WRITE predicate | The inherited local receiver condition before G. Its occurrence at the specified command is proved only on the supported clean transport domain. |
| Archive flag | A retained bit acted on by append. A flag can change without a supported WRITE in raw evolution. |
| Formal parity read | The complete projector-valued partition of the retained archive and its resulting CP branch maps. All branches and their cross terms before reading remain accounted for. |
| Realized outcome | A particular local LOW/HIGH result with its invocation/context in an actual-state model. This candidate supplies no such selection map. |

The available formal payload at a completed prefix of j rounds is the
**whole instrument**, not a selected word. Write its maps as
F_dev[Pi,w], for every word w in {LOW,HIGH}^j, including zero maps.
They are obtained by the specified complete internal evolution followed
by the declared archive projectors, with controller, environments and
reference retained. Their traces are formal weights. No bath is discarded
and then reinterpreted as a chosen event. A normalized conditional state
is supplied only if that branch trace is positive.

## A total typed report, not a readiness detector

The report takes a declared descriptor, a specified classical controller
chronology, the relevant completed boundary, and an explicit statement of
which preparation hypotheses are assumed or established. It is an external
mathematical interface; it neither chooses the next operation nor changes
F. It does not purport to infer unknown purity, phase, support or coherence
by observing a quantum input.

Every report retains these fields:

```text
status; applicability; raw_resource_diagnostic; completed_round_count;
invocation/context/epoch/slot metadata;
complete raw joint state;
formal prefix instrument when its contract applies;
realized_record = NOT_DERIVED.
```

Applicability is separately one of CONDITIONAL_ON_DECLARED_PROMISE,
NOT_ESTABLISHED, or KNOWN_VIOLATED. These labels are admission information,
not outcomes of a newly introduced measurement. In particular,
NOT_ESTABLISHED never becomes a claim that the unknown state is ready.

The status cases have the following ordered meaning:

| Status | Definition |
|---|---|
| INVALID_PROMISE(reason) | The positive interface is not applicable. Reasons distinguish a missing admission statement, a contradicted hypothesis, an unsupported descriptor, no single specified classical chronology, or a boundary outside the forward/read retention interval. This does not assert that every unverified input is physically bad. |
| NO_COMPLETED_ROUND | The admitted forward/read chronology has not reached a completed round. Its empty formal prefix has weight one. This is not a statement that no microscopic interaction occurred. |
| FORMAL_RECORD_AVAILABLE(j) | j>=1 supported rounds have completed and their archive remains inside the declared retention interval. Return all formal prefix maps of length j. |

Evaluate the rows in that order on the typed reporting inputs. The result
is a total report on those inputs, not a total realized-outcome transducer.
For K>=1, ordinary completion with all K slots used is
FORMAL_RECORD_AVAILABLE(K); K=0 instead has NO_COMPLETED_ROUND.
The useful compiled program never needs an extra append.

Resource diagnosis is a separate field, evaluated from the specified
classical command/cursor chronology even when the whole program fails the
positive interface. For a forward COLLIDE or APPEND, inspect the retained
cursor at the command entry; inverse commands are resource recovery, not
fresh forward requests. Do not infer a chronology from a dirty counter
value alone.

| raw_resource_diagnostic | Definition |
|---|---|
| NO_REQUEST | No additional forward bath/archive request is under consideration. Normal completion, including h=K, has this value. |
| WITHIN_CAPACITY | The specified forward request has b<B or a<K, respectively. This asserts an address is available, not that its unknown contents are pure or ready. |
| CAPACITY_EXHAUSTED | The additional forward request has b=B or a=K. Retain its actual reversible failure-counter and cursor update. It produces no valid new preparation collision or archive append. |
| NO_CLASSICAL_CHRONOLOGY | No single classical command/cursor chronology has been supplied; retain the raw coherent state. |

Thus an unsupported extra-append tape may receive INVALID_PROMISE together
with CAPACITY_EXHAUSTED. The raw resource fact does not admit that tape to
the positive theorem. Earlier supported prefix reports remain available
as reports of their earlier boundary; arbitrary later raw commands are
not promised to preserve their archive. The failure counters have exactly
the finite-range/modular meaning in PREREG. They count failed requests
as nonnegative integers only on the stated forward-polarity prefix from
zero; inverse or mixed programs retain modular values. They are not an absorbing halt
or permanent overflow flag.

Off-domain data always retain their specified unitary evolution. Coherent
superpositions of program or controller phases do not silently receive one
classical chronology or scalar operational status. Without a separately
specified status measurement they remain a raw joint quantum state and
receive the corresponding interface reason above. No bad or unknown input
is projected into the positive domain, normalized as a successful trial,
or omitted from the raw carrier.

## Three laws and their separate comparisons

For one admitted program Pi, initial state, finite horizon and declared
read boundary, keep the following objects separate:

| Law | Definition or missing input |
|---|---|
| P_actual,Pi | The pushforward of an independently specified actual preparation measure by an independently specified actual record map; presently undefined. |
| P_dev,Pi | Formal traces of the finite internally implemented device, with its approximate preparation and full retained controller. |
| P_ideal C,Pi | The exact ready-bank Stage-C reference under the same supplied source/context program. |

P_dev is not P_ideal C merely because the compiler is exact. Finite pointer
loading remains approximate. The comparison state uses P_E to the m-th
tensor power times the **actual output remainder marginal**, including all
spent baths and any source/bus/reference correlations. Preparation is
charged once for the bank. Bath feedback, unregistered source replacement
or extra approximate gates require a new comparison contract.

If the complete command-map equivalence in PREREG is proved, the controller
error is exactly zero, with its stated initialized-controller domain and
output identification. This conclusion must follow from the operator
proof, not a finite simulation. The new controller-extension proof must
also show that subsequent microsteps leave preparation baths untouched
and do not retain fine source labels in classical metadata.

For a possible approximate successor define epsilon_control by a uniform
complete-output trace-distance bound, including arbitrary admitted finite
references, between its internal implementation and the corresponding
external finite preparation/measurement program with a fixed complete
output identification. Define epsilon_occurrence separately by a proved
total-variation bound between P_actual and P_dev on one common complete
history space. Only after these definitions and proofs could the triangle
inequality give

```text
TV(P_actual[Pi], P_ideal_C[Pi])
  <= min(1, epsilon_occurrence + epsilon_control + epsilon_prep).
```

This is a prospective conditional composition rule. Here the occurrence
law and epsilon_occurrence are undefined, not zero. Extra source/context
approximations need their own terms or inclusion in the uniform control
bound. All admitted histories, including newly positive ideal-zero
histories and declared status leaves, must remain in a comparison; no
conditioning away unwanted histories is permitted.

Even a history-law bound does not by itself compare actual conditional
post-states with quantum conditional states. Rare-prefix continuation
requires its own proved relation and positive lower-weight conditions.
For the presently formal device/ideal comparison, the inherited
min(1,2 epsilon_prep/min(p_w,q_w)) bound is used only when both p_w and
q_w are positive. An ideal-zero branch has no normalized ideal state.

## What an actual-state proposal must add

A successor must specify one complete actual-state space with equality
and measurable structure, its total update, preparation domain and
relation to the complete complex representation. It must give a total
chronological record-prefix map, including no completed event, invalid
input and capacity exhaustion, and prove prefix extension over its claimed
retention interval. The source, controller and settings and all their
allowed correlations must belong to that same model.

The initial measure or a frequency construction must have an independent
basis and falsifier. Defining it from the target trace table, supplying a
Born-distributed seed or loading an outcome tape does not derive it.
Any added selection law must be labelled as an additional law. Relevant
L1-to-L5 and L5-to-L6 physical crossings require their named gates; this
annex establishes neither crossing and changes no existing owner.

The conditional controller can order a supported interaction and preserve
its formal record. Single-outcome selection, source renewal and the initial
occurrence law remain separate obligations. Their absence here is not a
general impossibility theorem for deterministic measurement models.
