# P-CURVATURE-COLUMN-GOLDEN-FRAME-1 result

Status: ABANDONED

## Disposition

The immutable preregistration pin was executed once. The process exited
nonzero before the scientific computation began. Under `POLICY.md`, this is
an abandoned pin: no accepted exact stdout was produced, no scientific route
was decided, and the identifier is consumed permanently.

This probe must not be reused, renamed, resumed, repaired, or rerun.
`EXPECTED.txt` and `RUN.md` are intentionally absent. Any retargeted attack
requires a new probe identifier, a new preregistration, and a new immutable
pin.

## Immutable pin

```text
issue:          #674
branch:         probe/P-CURVATURE-COLUMN-GOLDEN-FRAME-1
pin commit:     280e01fdfcb65fb74897aafb891fb95cc63b7349
PREREG SHA-256: bacaf7e6357aeb8382f943c90cddb687122ad55c011a687907f1a7d21f5edc8d
verify SHA-256: cf00b2a4eaa6dd7dd49c3565f0f3f67419c1fff4f2a14b3c1f031fa561bc2963
dependency:     probes/P-CURVATURE-GAUSS-SPLIT-1/verify.py
dep SHA-256:   4080da59872a923b0ce4204a93184e17307f6923243d97f0f3105c771c48b8bd
```

All three local files matched these frozen hashes before execution.

## Failed formal attempt

```text
date UTC:       2026-08-30T07:14:04Z
command:        python3 probes/P-CURVATURE-COLUMN-GOLDEN-FRAME-1/verify.py
platform:       Linux
architecture:   x86_64
Python:         3.13.5
exit code:      1
stdout bytes:   88
stdout SHA-256: 1386ec9bbf101d7a9659eb1c1b5a944258b34a95eee79acbfc4554089fd3e854
stderr bytes:   0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The rejected stdout was:

```text
P-CURVATURE-COLUMN-GOLDEN-FRAME-1
DECISION STOP exception=AttributeError
RESULT INVALID
```

This output is recorded only to explain abandonment. It is not
`EXPECTED.txt`, a completed gate transcript, or scientific evidence.

## Fixture diagnosis

The frozen `load_dependency()` creates a module with
`module_from_spec(spec)` and immediately calls `spec.loader.exec_module(module)`
without first inserting that module into `sys.modules`. The frozen dependency
uses postponed annotations and applies `@dataclass` during import. Python's
`dataclasses` implementation resolves those annotations through
`sys.modules[cls.__module__]`; the missing module entry therefore raises

```text
AttributeError: 'NoneType' object has no attribute '__dict__'
```

A separate minimal loader control reproduced this exact exception without
executing or modifying the pinned verifier. The defect is in the frozen
fixture and is not a mathematical falsifier.

## Scientific result

None.

The probe did not reach construction of the historical columns, projective
ray quotient, cosine census, `c^2 = 1/5` graph, six-clique enumeration, rank
check, or projector-tightness check. Therefore it decides none of
`UNIQUE-GOLDEN6`, `MULTIPLE-GOLDEN6`, `PAIR-ONLY`, or `ABSENT`.

It does not change `CURVATURE-HISTORICAL-TRACE [T]`,
`CURVATURE-HISTORICAL-GAUSS-SPLIT [T]`,
`GOLDEN-SIX-LINE-SYM2-FRAME [T]`, or
`CURVATURE-OPERATOR-CANONICAL [O]`.
