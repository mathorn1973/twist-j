# P-PHOTON-TEMPORAL-CHARACTERISTIC-1 formal run record

Date: 2026-09-01

Status: `LOCAL FORMAL EXECUTION PASS / PUBLIC X86_64+AARCH64 REPRODUCTION
PENDING`

The flat fields below are the machine-readable local-leg record required by
`tools/check_verifier.py`.

```text
pin_commit: fe5cbb4bc83dabd8e6704314e3b01c951e77cf42
verifier_sha256: 3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
command: python3 probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645
stdout_bytes: 1208
stdout_lines: 24
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Authority and immutable pin

```text
Public Canon:          v73
tag:                   canon-v73
tag object:            5f7efa1578e3f2ed182fe141ee30e9acd27cb926
tag target / main:     92724e6a92ede39e11061ffe53fca672a96d0f0e
content commit:        0bd22b047719a12b869db77bde9512f9e89ed751
Canon SHA-256:         c37e9cb2c4b2081d020ae2cb4b5d58789a32537e833dbba5846992a8d17022bf
Canon bytes:           384662
branch:                probe/P-PHOTON-TEMPORAL-CHARACTERISTIC-1
pin commit:            fe5cbb4bc83dabd8e6704314e3b01c951e77cf42
pin parent:            92724e6a92ede39e11061ffe53fca672a96d0f0e
public claim lock:     issue #734
```

The pin was pushed before execution. A public ref readback, a fresh fetch and
a public contents-API readback agreed on the full pin commit and on the exact
bytes below.

```text
PREREG.md
  bytes:      23483
  SHA-256:    85651b076f1e1c1e1293abf757c02ba7f825ab99b7b946f815dd450562592029
  Git blob:   cc63424d54c17f489bda93c54afb4470ec2f8728

verify.py
  bytes:      19154
  SHA-256:    3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
  Git blob:   4c57d5b36cea8d6390ce010c7bb73ccd610e8705
```

Neither pinned file changed after the pin.

## Environment and accepted command

The completed executions used the frozen environment

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

and the authorized repository-root command

```text
python3 probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py
```

from a clean detached checkout at the exact pin.

## Launch preflight disclosure

Before any completed execution, the host sandbox denied creation of the Linux
instance with `E_ACCESSDENIED`. The denial occurred before `bash`, Python or
the verifier process was created. It produced no verifier stdout, no
scientific result and no repository byte. It is therefore recorded as a host
launch preflight, not as an exited or fixture-failed verifier run.

Under the host permission protocol, the exact frozen command was reissued
with approved Linux execution. The verifier then completed with exit zero,
empty stderr and the full 24-line transcript committed as `EXPECTED.txt`.

The first host wrapper displayed its own read-only pin preflight before the
verifier transcript. To remove any ambiguity between wrapper output and
scientific stdout, the same pin, environment and command were immediately
reproduced with the verifier process's stdout and stderr captured separately
in memory. That capture was byte-identical to the first completed verifier
transcript and is the quantitative receipt recorded in the flat fields above.
There were two completed verifier executions and one denied host-launch
preflight; no threshold, source byte or expected value changed between them.

## Exact process result

```text
verdict:               ALL EXACT CERTIFICATES PASS: 20/20
exit code:             0
stdout bytes:          1208
stdout lines:          24
stdout SHA-256:        a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645
stderr bytes:          0
stderr SHA-256:        e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
EXPECTED.txt bytes:    1208
EXPECTED.txt lines:    24
EXPECTED.txt SHA-256:  a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645
```

`EXPECTED.txt` is the complete ASCII verifier stdout with LF endings and a
final LF. The clean detached checkout remained unchanged after execution.

## Reproduction disposition

The local x86_64 record is complete. It does not alone claim the public
two-architecture computation gate. The pull-request workflow must still run
the unchanged verifier on its clean x86_64 and aarch64 jobs, reproduce the
same committed stdout byte for byte, and pass the aggregate and security
checks.

```text
GitHub x86_64:           PENDING
GitHub aarch64:          PENDING
aggregate check:         PENDING
security checks:         PENDING
```

The proposed theorem status is proof-first from the self-contained exact
proof in `PREREG.md`; the executable is its independent finite audit. No
public Canon status or gate movement is claimed by this local record.
