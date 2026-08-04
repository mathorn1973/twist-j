# P-PHOTON-KAPPA-LEMMA-1 formal run record

Status: `FORMAL LOCAL EXECUTION PASS / BELOW-THRESHOLD / GITHUB
X86_64+AARCH64 REPRODUCTION PENDING`

Exactly one formal execution was performed after immutable public pin
readback and explicit owner authorization. This record contains neutral public
descriptors only. It contains no machine nickname, hostname, username,
private path, credential, or elapsed-time telemetry.

## Authority and authorization

```text
STATE:                 ACTIVE
Public Canon:          v35
tag:                   canon-v35
activation commit:     7c5e1560d56ddf801bf55079674a90682c4b58ee
content commit:        c94fc18ed3b5be1706397e4cc8666b6123858918
initial public base:   ac264113fd1596ab09d8d31daff93d7a7c7aab19

branch:                probe/P-PHOTON-KAPPA-LEMMA-1
pin commit:            b24f60fa5e44d891a4da43fa0f4747c01c836e68
pin parent:            ac264113fd1596ab09d8d31daff93d7a7c7aab19
public lock:           issue #200
definition freeze:     issue comment 5175681684
verifier/pin approval: issue comment 5175862160
run authorization:     issue comment 5175948529
formal return:         issue comment 5175976102
```

Before execution, `git ls-remote`, a fresh fetch, the local detached commit,
and the remote-tracking ref all resolved to the full pin commit. The local and
fetched remote three-file trees had an empty byte diff.

## Immutable pin inventory at execution

```text
PREREG.md
  bytes:      16670
  SHA-256:    15486b5e0a1846d9b60cea776f654ccd636adb890d31eb50d2cec635b719adc5
  Git blob:   2e30642c712bcc9f69ae5c878c26035931f44469
  LF/CR/NUL:  467 / 0 / 0
  final byte: 10 (LF)

verify.py
  bytes:      29777
  SHA-256:    7a3c8e1e3a1658f8b2538a2aa069f1ea678d358a66f56c158a09bc96161ca976
  Git blob:   30a80c821cef2b786e98bbcd20b00e08d77ed71c
  LF/CR/NUL:  970 / 0 / 0
  final byte: 10 (LF)

witness_6_3_6_6.json
  bytes:      280106
  SHA-256:    9b664f16830d2b562949933e40b4f1460d9da5645a88beff7bca347b70320313
  Git blob:   c39cd1dd3e0cae3974fff4f67bde89d131efa249
  LF/CR/NUL:  0 / 0 / 0
  final byte: 125 (`}`)
```

## Environment and command

```text
platform:             Ubuntu 24.04.3 LTS
kernel family:        Linux
architecture:         x86_64
Python:               3.12.3
UTC start:            2026-08-04T07:34:47Z
UTC finish:           2026-08-04T07:34:49Z
checkout before:      clean, detached at exact pin
checkout after:       clean, detached at exact pin
formal executions:    1
```

Environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Command from repository root:

```text
python3 -B probes/P-PHOTON-KAPPA-LEMMA-1/verify.py
```

## Exact process result

```text
exit code:             0
stdout bytes:          911
stderr bytes:          0
stdout SHA-256:        546c1cc2ec839588041a0bdd420bd9b976cf68ca379b6d3441cb0b00a10e0f12
stdout LF/CR/NUL:      16 / 0 / 0
stdout final byte:     10 (LF)
EXPECTED.txt bytes:    911
EXPECTED.txt SHA-256:  546c1cc2ec839588041a0bdd420bd9b976cf68ca379b6d3441cb0b00a10e0f12
```

`EXPECTED.txt` is the raw captured stdout copied byte-for-byte. No newline,
encoding, whitespace, or content normalization was applied. The captured
stderr file was empty. The detached checkout remained clean and contained no
cache or generated file after execution.

## Reproduction disposition

The local exact result is complete. Cross-process public reproduction is
pending the required pull-request jobs:

```text
GitHub ubuntu-latest x86_64:       PENDING
GitHub ubuntu-24.04-arm aarch64:   PENDING
aggregate required check:          PENDING
```

Both jobs must use the unchanged verifier SHA-256 above, exit zero with empty
stderr, and produce stdout byte-identical to the one committed
`EXPECTED.txt`. Until they pass, the two-architecture computation gate is not
recorded here as complete and no Canon status is earned.
