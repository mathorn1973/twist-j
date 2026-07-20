# C-LI-Q-MOMENT-1 / N2 independent aarch64 readback

```text
STATUS:       PASS, independent notes-lane readback.
AUTHORITY:    none. NON-CANONICAL, NON-FORMAL.
DATE:         2026-07-17
```

The readback used a fresh clone of the public branch at the exact commit

```text
a002e72481b8cf74fc95e51411bf3c9ead29cda3
```

and verified before execution:

```text
platform          Ubuntu 24.04
architecture      aarch64
python            CPython 3.12.3
verifier_sha256   fc86ec75f31cd2884c6dffa36ba0068e778faebc06cf0c70aaae0ae3f6e80300
SHA256SUMS        PASS
```

The neutral environment was

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Three executions of

```text
python3 -B notes/C-LI-Q-MOMENT-1/verify_q_moment_n2.py
```

returned exit zero, empty stderr, and byte-identical output.  Every output
also matched `stdout_q_moment_n2.txt` exactly:

```text
stdout_sha256   743c0886225489f16e0fa03bb74108f8d444303739520b83f3947ccc1d807a9f
stdout_bytes    2034
stdout_lines    29
stderr_bytes    0
executions      3 byte-identical
```

The same checkout also returned

```text
POLICY PASS
38/38 tool tests PASS
CANON PASS v8 claims=178
LEDGER PASS claims=178 items=193 dependencies=224 evidence=178 history=454 gates=7
```

Together with the first Windows 11/x86_64 run recorded in
`N2_SH1P_RESULT.md`, this establishes byte-identical independent behavior on
two architectures.  Because N2 is an incubation note rather than a pinned
public probe, this is deliberately classified as a notes-lane readback, not
the policy two-architecture promotion gate.  It creates no public status and
does not change the N2 scope ceiling.
