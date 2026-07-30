# C-ENTROPY-MACKEY-OBSTRUCTION-4-N primary run

```text
STATUS:       NON-CANONICAL PRIMARY RUN
AUTHORITY:    none
PUBLIC BASIS: Public Canon v28
CANDIDATE:    C-ENTROPY-MACKEY-OBSTRUCTION-4-N
DECISION:     PRIMARY ROUTE SURVIVES; INDEPENDENT BREAKER REQUIRED
```

## Frozen inputs

```text
recon merge:        39d9a88f3249310ed33df3f2a1172ef169456ead
status note:        a19b86131df447a189d54599f4a8d2a2e0f0c805
prereg commit:      2314e92ee0571cfe9c38e2bd11733ce4a1ba3cc8
primary code commit:309840a6eb33b4970c5bf22de55d0e1a44d36974
primary blob:       917dab1825c8e4ba74cd061fd91b054195b6c156
primary SHA-256:    fb82b7af4cb199c07b5c671c5a955b2ea1ef251af89e6459ca802bbfe5dd2c4a
primary bytes:      23494
primary lines:      719
breaker file:       absent
```

The primary file was committed and read back from GitHub before execution.
`mackey4_break.py` did not exist and was not authored or read in this session.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 notes/entropy_selection/mackey4_verify.py
```

The connected execution environment used the byte-identical pinned content at
`/tmp/mackey4_verify.py`; its Git blob identity matched the public blob above.

## Environment and streams

```text
platform:           Linux 6.12.13
architecture:       x86_64
python:             Python 3.13.5
executions:         1
exit_code:          0
stdout_sha256:      22a81fb7361f8694904c05ce0bdbfd1aa068578983ecbfd13669d5cd2487adfa
stdout_bytes:       1794
stdout_lines:       21
stdout_cr:          0
stdout_final_byte:  10
stderr_sha256:      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:       0
gates:              13 of 13 PASS
```

`mackey4_primary.stdout.txt` is the exact raw program stdout. A later terminal
clear attempted by the surrounding execution wrapper after stream capture is
not part of the program stdout or stderr and changed no file or decision.

## Scope boundary

This is one x86_64 primary run in an incubation lane. It is not independent
confirmation, not a two-architecture gate, not public evidence, and not a
candidate-C conclusion by itself. The preregistration requires a separately
authored frozen breaker that does not read or import the primary verifier.
