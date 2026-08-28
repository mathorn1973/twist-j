# P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1 result

Status: ABANDONED.

The first formal gate invocation after the immutable public pin exited
nonzero at `G12 scope_nonselector_guard` and wrote a traceback to stderr.
Under `POLICY.md`, a nonzero run never completed the formal gate and produces
no exact scientific stdout to pin.

The cause is a verifier-integrity string-coupling defect, not a scientific
falsifier. The frozen `G12` requires the contiguous literal

```text
No selector, physical mechanism, or preferred embedding
```

inside `PREREG.md`. The frozen preregistration contains the same scope sentence
but wraps a newline between `preferred` and `embedding`, so the literal
substring test is false. The verifier and preregistration are immutable after
the pin and are not repaired.

The invocation printed partial `PASS` lines through `G11`, but it emitted no
decision line, exited nonzero, and wrote nonempty stderr. Those partial lines
are diagnostic only. They earn no theorem, negative theorem, evidence,
candidate status, selector result, Galois result, mounted-breaker result, or
physical conclusion.

This directory intentionally contains no `EXPECTED.txt` and no `RUN.md`.
Public Canon v68, Registry, Frontier, dependencies, gates, physical statuses,
and all existing candidate rows remain unchanged.

The identifier `P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1` is consumed and
must not be reused, renamed, resumed, amended, or treated as evidence. Any
successor must use a fresh issue, probe identifier, preregistration pin, and
verifier, and must name this abandoned predecessor and its exact G12
string-coupling defect before its own pin.
