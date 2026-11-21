# Audit A: first-run custody record

**PUBLIC-source, NON-CANONICAL; candidate-C local computation. No authority.**
Candidate C-PHOTON-U1-FINITE-CENTER-N, owner issue #1715.
Author: A. M. Thorn. Record date: 2026-10-23. Apache-2.0.

## Frozen inputs and execution boundary

The preregistration was publicly frozen at
`b7be3d00495330e4ac00441b865f9009e54a6299`. The complete scientific source
set was committed, pushed and publicly read back at
`9a74d03fb8f2c8086eff0f326446352f0f628082` before execution.
`SOURCE-MANIFEST.json` records the eight frozen files below. Its
`scientific_execution: NOT_RUN_AT_FREEZE` describes the time of freezing;
this record describes the subsequent first executions.

The primary program and sampler exercise share `z7_exact.py`. The breaker
was authored from the frozen contract without reading that module,
`verify.py`, their outputs or the comparison digest before its own source
was frozen. It uses separate cyclotomic arithmetic. Analytical predictions
and the sharpness-witness construction were exposed to both authors before
execution; this is implementation independence, not a blind prediction or
external acceptance. See `BREAKER_REVIEW.md`.

| Frozen file | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 10129 | `87e2f1f6265e2524b84ff3c298d166ac51f9fcdc6374b5961971392684d6d97e` |
| z7_exact.py | 15923 | `f5a61136e6f9862ac689c05e013ab3047ab15cf07e9d29fecffcec39f8581c89` |
| verify.py | 14870 | `9a85bd93b7ae230aae07ad08b5bb69a6b5339282f7537c0641e4527e146d8110` |
| break.py | 18652 | `bac3152937fa3cf2096da3f52aff18f965fd5410194007ac52292525fe7a4061` |
| exercise.py | 2636 | `bd9cdb3a0fc7b387ee2f596db6c1b449d1e33a0d0bccdb8e442877ba72ce35e0` |
| PROOF.md | 15634 | `93b6fcb57a2d72170b88497e2cd802f9984b38cad8ba9de7b47513197c4fd7f3` |
| MEASUREMENT.md | 10675 | `eb5a7abe591f3e1cce9407780b8c30991e156bd02cacae8377c44b465e41eabd` |
| BREAKER_REVIEW.md | 5929 | `01c710a82edd8cb403d1ee26b4ebe0adf7f871fe3db21d2c6e51306d69188b15` |

The source manifest itself has 1437 bytes and SHA-256
`116e8e902e6b523cdf7f87c5b23d42aac5357d73f52379a0c2c7d9546b81dc66`.
All eight source byte counts and hashes were compared with the manifest
after execution and agreed before the documentation clarification described
below. No scientific executable source was changed after these runs, and
no scientific program was rerun to prepare this record.

After Audit A, section 4 of `MEASUREMENT.md` was clarified to distinguish
the executed audit from prospective scripted-bit, direct-link-replacement
and corruption tests. That paragraph explicitly records its post-pin
documentation status. The manifest remains a custody record of the exact
source commit above, not a claim that every final documentation file still
has its pre-execution hash. The clarification changes no executed code,
frozen test, threshold or captured output.

## Commands and environment

Working directory: `notes/C-PHOTON-U1-FINITE-CENTER-N/` in the repository.
System: Linux. Architecture: x86_64. Python: 3.12.14. Standard library only.
The recorded environment was:

```text
LC_ALL=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The recorded argument vectors were:

```text
python3 -B verify.py
python3 -B break.py
python3 -B exercise.py
```

Each program had its own preregistered 180-second wall-clock budget.
Timing decimals below are engineering metadata, not scientific assertions.

| Program | First start, UTC | Seconds | Exit | stderr bytes | Recorded status |
|---|---|---:|---:|---:|---|
| verify.py | 2026-10-22T23:13:03Z | 2.325 | 0 | 0 | PASS |
| break.py | 2026-10-22T23:13:05Z | 0.516 | 0 | 0 | PASS |
| exercise.py | 2026-10-22T23:13:05Z | 2.472 | 0 | 0 | PASS_OPERATIONS_ONLY in stdout |

The UTC start date is October 22; the local Europe/Prague date was
October 23. All three first executions completed successfully. There was
no failed scientific run, timeout, scientific repair, replacement transcript
or threshold change in Audit A. The execution wrapper records the last
program as PASS, while its scientific stdout deliberately uses the narrower
`PASS_OPERATIONS_ONLY` status.

## Captured bytes

All streams are retained without rewriting under `runs/audit-a/`.

| stdout file | Bytes | SHA-256 |
|---|---:|---|
| verify.py.stdout.txt | 6465 | `37ad0dac91f3778775b9d86f13e8e0a6011f2a94524903a3adfe6b4505525303` |
| break.py.stdout.txt | 952 | `a40f3af4434b4e35557dae7b92ebc3e3782c5a150879dc573617efda8ff9bfff` |
| exercise.py.stdout.txt | 15228 | `fba1c6f0a94fd97d0366522b3855072e48095a80b48cb0050bb8664bb43aaaac` |

Each corresponding `.stderr.txt` file contains zero bytes and has SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
`runs/audit-a/RUN-METADATA.json` contains 2089 bytes and has SHA-256
`36933319689ce94f61b955516f7fcb9e0b4be44b8fa1a5de8a751608a0e89389`.
Every captured stream's byte count and digest was checked against that
metadata while preparing this record. This was artifact inspection, not
another scientific execution.

## Cross-implementation comparison

The two implementations' ordinary stdout formats intentionally differ.
Both independently generated the preregistered 6468 compact JSON lines:
924 lexicographically ordered six-staple count vectors, then seven proposed
residues each. Every line carries the three integer coefficients of the
unnormalized conditional mass in the basis `(1,x,x^2)`. The common SHA-256 is

```text
04ef99ab864b0240d3d8b0039e538eaf18d79d999aeadf89a8cb624ae84a4e5b
```

These comparison lines are hashed as generated and are not separately
stored as a table. Both programs preserve the digest in their original
stdout. Captured outputs also agree on all incidence-word alias counts,
the ten actual-torus witness supports, six wrapping sheets, 1024 local
cube boundaries, both exact two-torus partitions and Hessians, their
discrete-source controls, and the cube/disk controls. Exact values are
collected in `RESULT.md`.

## Operation-only exercise

Each start underwent exactly two sequential full sweeps. A hot start uses
the declared sampler PRNG stream to draw initial uniform link residues,
then continues that stream for exact conditional transitions. The
`random_bits` counter below counts bits requested by the categorical
updates only; it excludes initialization draws.

| L | Start | Seed | Edge updates | Actual changes | Categorical bits | Sweeps |
|---:|---|---:|---:|---:|---:|---:|
| 2 | cold | 230701 | 128 | 59 | 4096 | 2 |
| 2 | hot | 230702 | 128 | 70 | 4096 | 2 |
| 3 | cold | 230703 | 648 | 283 | 20736 | 2 |
| 3 | hot | 230704 | 648 | 385 | 20736 | 2 |
| Total | four starts | | 1552 | 797 | 49664 | 8 |

After every sweep the program checked cached curls against recomputation,
the mod-seven Bianchi identity, principal-plane divisibility and exact
reader serialization. The transcript retains state digests and individual
reader values. No sign or magnitude of these reader values is interpreted
as equilibrium response or a phase. The breaker did not reproduce the
sampler trajectory, as explicitly permitted by the preregistration.

## Status boundary

This is one local x86_64 execution lane. The finite computational evidence
is candidate-C. The independent written argument in `PROOF.md` is recorded
separately as candidate-T; the finite run does not prove its universal
quantifiers. Notes CI does not rerun these scientific audits and is not
the repository's two-architecture computation-grade T gate. No canonical
promotion, practical mixing certificate, thermodynamic conclusion or
physical-photon conclusion is supplied.
