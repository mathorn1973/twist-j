# P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1 result

Status: ABANDONED.

## Disposition

The immutable public pin is consumed and must not be reused, renamed, resumed,
or executed.

```text
probe:              P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1
issue:              #594
pin commit:         4726319ddc8c4acbe5267badb39b0761554aa086
basis main:         e051ad2472e77cf2ffbc2bad965e2a99e7dfea10
public pin tree:    7c695e67890d924116f50952e114944f73616f71
```

## Why the formal gate did not start

The pin was created with exactly `PREREG.md` and `verify.py`. Before any
startup preflight or verifier execution, public readback was compared with the
locally frozen source bytes.

The verifier matched exactly:

```text
verify bytes:       12905
verify sha256:      cd5c2a3cc0ff1b4d266c309e3527bfbd4d0718500d4d59b73f94368f5c71356a
local Git blob:     6c632b89ebc627a6a164155f2ac8c7481727c406
public Git blob:    6c632b89ebc627a6a164155f2ac8c7481727c406
```

The preregistration did not:

```text
PREREG bytes:       14100 on both surfaces
local sha256:       40e7669af5b961f33729ec84dc1f951f684b4a6a8b32e8b8ec01224a0600199d
local Git blob:     45614f1dc9dca7a6bd8d3e8790581b07a47585aa
public Git blob:    65100eeef1d9855a48c3d20e02c8939e0e535422
```

Equal byte counts do not repair unequal content identities. The frozen
protocol classifies any changed pinned byte or readback mismatch as integrity
STOP. Therefore the startup preflight and scientific command were not run.

There is no `EXPECTED.txt`, no `RUN.md`, no protocol verdict, and no scientific
result from this probe. The mismatch is a transport/transcription failure, not
a counterexample to the proposed mathematics and not a fired scientific
falsifier.

## Successor boundary

Any renewed attack must use a fresh identifier, issue, branch, preregistration,
verifier pin, and formal run. It must name this abandoned predecessor and must
repeat public readback before execution.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, workflows,
Notes and all existing scientific rows remain unchanged.
