# Result

Status: `ABANDONED`.

```text
probe            P-QDD-FRESH-RECORD-NOFEEDBACK-1
public lock      issue #470
formal gate      executed once, never completed
formal result    none
recorded         2026-08-24, Public Canon v62
```

## Why the gate never completed

The sole formal execution of the accepted verifier exited nonzero on a
fixture defect: the old-record control changed the label on only one entry of
a multi-entry sparse state and then required every entry to carry that label.

A nonzero exit yields no exact stdout to pin and no scientific conclusion, so
this probe has no `EXPECTED.txt` and no `RUN.md` to commit. No mathematical
disagreement was established, and nothing here is evidence for or against the
frozen proposition.

The defect was in the fixture, not in the mathematics. That is why this is an
abandonment and not a fired falsifier: no falsifier fired, because no gate
completed.

## The identifier is consumed

`P-QDD-FRESH-RECORD-NOFEEDBACK-1` is spent. It must not be reused, renamed,
repaired, rerun or resumed, and no part of its lane may be cited as evidence.
The pin and the accepted verifier stay exactly as they were frozen; this
record is the only file added.

The successor `P-QDD-FRESH-RECORD-NOFEEDBACK-2` carries the mandatory
predecessor STOP disclosure in its own preregistration, before its own pin,
and is already public on `main`. It repairs nothing here and imports no
predecessor code, helper, transcript or result.

## Canon effect

None. No claim is registered, promoted, lowered or retired; no registry,
frontier, gate, dependency or Canon text changes; the live `H` and `O` count
is unchanged.
