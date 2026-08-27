# P-O5-DEDEKIND-GRH-READ-1 result

Status: ABANDONED.

## Disposition

The immutable public pin is consumed and must not be reused, renamed, resumed,
or rerun.

```text
probe:          P-O5-DEDEKIND-GRH-READ-1
issue:          #587
pin commit:     0717455c537449f70180029057406af324b8c12e
basis main:     7dd25c7c21202c560d8a31774971c7c6200fca76
verifier sha256: 621adb2c286d3a9d6f3cfe91abf8cc4d6a9599d475f51e2ee2a837abec9c33de
```

## Why the formal gate did not complete

After the public pin and readback, the accepted command was invoked once on a
Linux x86_64 host under the frozen deterministic environment.

The verifier body reached its diagnostic end and produced the nine expected
PASS-shaped lines, but the Python host injected a spreadsheet-runtime warmup
failure into stderr during interpreter startup, before the verifier source
ran.

```text
exit_code:       0
diagnostic stdout sha256:
  8535184664a8e8fa54c5ae4a780e78ab4a9bea2cff017b39c1f38996a4a72752
diagnostic stdout bytes: 549
diagnostic stdout lines: 9
stderr sha256:
  3eb8b21bb3e6e859ea8c74765f381bf327eb9f0b62d7c10637128f85ca723e4c
stderr bytes:    754
technical source:
  host-injected artifact_tool spreadsheet warmup during Python startup
```

The preregistered threshold requires exit zero, exact stdout, and empty
stderr. Empty stderr failed. Therefore there is no accepted formal run, no
`EXPECTED.txt`, no `RUN.md`, no protocol verdict, and no scientific
conclusion from this probe. The diagnostic stdout is not evidence and is not
committed as an expected result.

This is a technical execution failure, not a counterexample to the written
mathematics and not a scientific falsifier.

## Successor boundary

Any renewed attack must use a fresh identifier, fresh issue, fresh branch,
fresh preregistration, fresh verifier pin, and one new formal run. Its
preregistration must name this abandoned predecessor and must freeze a clean
interpreter-startup control before the scientific command.

Public Canon v67, its Registry, Frontier, dependencies, gates, evidence, and
all existing probes remain unchanged.
