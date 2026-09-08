# RRP1 two-exposure reset: software implementation

**NON-CANONICAL / NOT YET EXECUTED / NO PHYSICAL CONFORMANCE RESULT.**

This is the bounded software implementation of
[the two-exposure definition](../V81-RRP1-FINITE-RESET-ADAPTER-1.md), on Public
Canon v81 basis `82d536a71025032d6dd4093db61ecb9f31990250`. It prepares exactly
two predeclared nonzero signed heads in order, using two reserved carriers and
one fixed `ContextKey`. Reset preserves the first carrier and hands its complete
custody into the second preparation. No refill, third preparation, source
selection from observations or statistical independence is implemented.

Files: [adapter.py](adapter.py), [test_adapter.py](test_adapter.py). These are
implementation regression checks under `notes/`, not a formal scientific
probe, empirical test, complete #539 verifier or owner-closing result. The
scientific owner `QDD-INSTRUMENT-APPARATUS` remains open. A successful test run
would establish only the listed finite software behavior.

## Dependency and execution boundary

The adapter dynamically imports the unchanged sealed
[`chain.py`](../../probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/chain.py), bound to
SHA-256 `d6f23db8a6f28ee6b90e2544a71608e2f320770046ecdeea94418d0f64468a99`.
That engine verifies its own native, reservoir and transport source hashes.
An occupied import name or unexpected source identity/origin stops import.
Use one fresh Python process for these checks; no other TRC1 engine should
already occupy its module names. No sealed source is edited or copied.

Only source inspection and compilation/AST parsing are allowed during this
preparation. The complete implementation, tests and this scope are to be
reviewed, publicly committed, pushed and read back before first execution.
The intended ordinary software-test command, from the repository root, is:

```text
python -B -m unittest discover -s notes/RRP1-TWO-EXPOSURE-RESET-1 -p test_adapter.py -v
```

Use Python 3.12 and its standard library. Running this command
imports and executes the sealed engine and the new adapter. It accesses no
experimental data or network and writes no scientific `EXPECTED`/`RUN` record.
There is currently no execution result. The actual software check outcome
will be recorded after the reviewed public pin; this README asserts no PASS.

## Carriers, exact domains and history admission

All implementation carriers are frozen dataclasses containing only tuples,
other frozen carriers, exact integers/Fractions, strings and the declared
optional `None`. Field preflight rejects missing declared dataclass fields,
mutable children, cyclic input graphs and malformed Fractions before calling
sealed validators. Normal generated immutable sharing is retained. A narrow
missing-field check produces an input error; arbitrary internal
`AttributeError` exceptions are not swallowed. This is a finite value API,
not a security boundary against reflective mutation of Python objects.

`ApparatusState` owns the plan, complete context, phase/index and both banks.
Prepared banks are complete sealed-core states, including their residual wave
pair, native checkpoint, signed tape, heat and all core events. Unprepared
banks have an explicit indexed `Unprepared` tag. `SupportCarrier` is the
ordered tagged wave projection of that same joint state, with literal
compatibility at `step`. It is not another energy store.

`ReadyState` separates schedule-only `Selection` from complete READY custody.
`prepare` checks both and initializes only the designated unprepared bank.
`reset` is defined only at COMPLETE bank 0 with bank 1 still unprepared, and
returns `(ReadyState, ApparatusState)` with identical retained custody. All
other reset positions, including incomplete, READY and exhausted states, are
domain errors rather than successful reset outputs. A valid zero-amplitude
plan has the distinct `REJECTED` request disposition; malformed requests are
`INVALID_REQUEST`. These exclusions do not alter TRC1's own zero-source case.

The public mathematical write carrier is exactly `HistoryState = EventRecord*`.
`append(history,event)` validates carrier membership and returns
`history + (event,)`. It accepts every finite typed sequence, including valid
duplicates, discontinuities, cross-session events and lengths exceeding run
capacity. It does not enforce reachability. Malformed records are outside the
carrier. An `EventRecord` retains the complete step delta: bank index, full
core event, and before/after session apparatus snapshots. No session event is
stored back inside its apparatus; only sealed core histories live in banks.

`ProtocolPosition = (apparatus, journal)` is a separate frozen carrier;
`ProtocolState` is its exact alias for the shared-contract spelling. Its journal
is a tuple of `JournalEntry(kind,before,after)`, where kind is PREPARE, RESET or
STEP. Validation starts at the unique initial state for its plan/context and
checks every exact action image and continuity. Administrative entries are
not EventRecords. The derived action index ranges from 0 through `2*N+3`.
When `N=0`, indices 0, 1, 2 and 3 respectively mean before preparation 0,
after preparation 0, after reset and after preparation 1; every event history
is still empty.

The three-argument predicates
`admissible_append(position,history,event)` and
`admissible_extension(protocol,history,event)` are the same Boolean function.
The supplied position is **before the proposed STEP**. It must contain a
coherent journal ending at a RUNNING apparatus; the supplied history must
equal all prior STEP entries projected to their complete session events; the
new event's exact before-snapshot must equal that apparatus. Event validation
already checks its complete next-step image. The predicate returns false for
failed input/compatibility checks. Admitted appends are followed by
`journal_append(journal,"STEP",before,after)`; total `append` itself does not
change the protocol. Preparations and reset use the corresponding journal
entries. A passive `reread` changes neither history nor action index.

The journal detects duplicate token use at a claimed protocol position. A
copyable mathematical ready value may still be replayed in another value-level
calculation; no physical single-use token, global allocation ledger or erasure
mechanism is claimed.

## Two independent implementation obligations

**Retention:** reset changes only phase/index. Preparation replaces only the
new bank, while the complete old core state remains in Ready custody, the
returned joint apparatus, later support projections and later session-event
snapshots. Residual energy and the signed outgoing tape are retained together.
Heat/count/remainder accounts describe the same modeled energy. Reset adds or
removes none; each separate preparation contributes its declared source kick.

**New-bank core noninterference:** actual generation is confined to
`_prepare_bank(head,context)` and `_step_bank(active_bank)`. The first receives
only the scheduled head and fixed context; the second receives only the active
bank. `_selection(plan,context,index)` has no custody argument. Inactive-bank
data enter compatibility validation, exact copying and accounting, but never
these core-generation inputs. Sealed `validate_state` may replay earlier
histories to check coherence; that is validation, not a new physical exposure
or a source-selection input. Full session records deliberately differ when
retained custody differs, even while their new-bank core events agree.

The dependency boundary supplies the structural argument. The test's AST
guard checks the narrow generator inputs and allowed core calls, and a finite
comparison changes the first head while fixing the second head/context. This
does not claim independent physical trials or quantify over a complete
physical apparatus family. Freezing inactive banks remains an additional
isolation/local-clock convention of this adapter.

## Bounded regression coverage

The concrete fixtures use two-step origin coupling with heads `e0,2e0`,
one-step empty support, one-step subthreshold behavior and zero horizon.
The additional noninterference comparison uses first heads `e0,e1,-e0` with
the same second head and context. Tests cover:

- exact agreement of each generated bank with the unchanged core;
- old nonzero residual, signed tape and complete core-record survival through
  reset and preparation 1, including custody in full later session events;
- the two-kick joint energy account and bounded fresh-slot consumption;
- zero/multiple crossings, empty port support and all four `N=0` positions;
- total concatenation versus skipped, repeated, discontinuous or exhausted
  protocol admission, including administrative journal continuity;
- incomplete/exhausted reset, mismatched contexts/support/tokens, malformed
  heads and missing local/nested-core fields;
- rejected record forgeries, passive rereads and nested immutable carriers;
- new-bank generation noninterference, distinct full session provenance and
  the structural field-dependency guard.

No cross-architecture scientific gate, physical retention/capacity/reset
certificate, zero reset work, U-to-clock dictionary, Born law, occurrence law
or NIST identification is earned by these software checks.
