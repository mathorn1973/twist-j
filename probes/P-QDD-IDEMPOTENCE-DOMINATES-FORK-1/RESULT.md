# Result

Status: `ABANDONED`.

```text
probe            P-QDD-IDEMPOTENCE-DOMINATES-FORK-1
public lock      issue #479
formal gate      stopped at mandatory readback
formal result    none
recorded         2026-08-24, Public Canon v62
```

## Why the gate never ran

Mandatory public readback found that the pinned `PREREG.md` blob differed
from the independently accepted bytes. The transport mismatch stopped the
lane before execution. Formal verifier executions remained zero, so there is
no exact stdout to pin, no `EXPECTED.txt`, no `RUN.md`, no fired falsifier
and no scientific result.

This reason is disclosed by the successor
`P-QDD-IDEMPOTENCE-DOMINATES-FORK-2` in its public preregistration on `main`
as `STOP / PUBLIC PIN TRANSPORT MISMATCH / NO SCIENTIFIC CONCLUSION`. The
successor repairs nothing here and imports no evidence from this lane.

## The identifier is consumed

`P-QDD-IDEMPOTENCE-DOMINATES-FORK-1` is spent. It must not be reused,
renamed, repaired, rerun or resumed, and no part of this lane may be cited as
evidence. The pin, accepted verifier and helper modules stay exactly as
frozen; this record is the only file added.

## Canon effect

None. No claim is registered, promoted, lowered or retired; no registry,
frontier, gate, dependency or Canon text changes; the live `H` and `O` count
is unchanged.
