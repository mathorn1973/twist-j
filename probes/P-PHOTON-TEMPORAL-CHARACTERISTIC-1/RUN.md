# P-PHOTON-TEMPORAL-CHARACTERISTIC-1 formal run record

Date: 2026-09-01

Status: `FORMAL EXECUTION PASS / PUBLIC X86_64+AARCH64 REPRODUCTION PASS /
AGGREGATE PASS`

The flat fields below are the machine-readable local and public aarch64 leg
record required by `tools/check_verifier.py`.

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
github_platform: Ubuntu 24.04.4 LTS
github_architecture: aarch64
github_python: CPython 3.12.14
github_verifier_sha256: 3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
github_stdout_sha256: a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645
github_exit_code: 0
github_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
github_stderr_bytes: 0
github_status: PASS
github_verdict: VERIFY PASS
github_byte_identity: PASS
github_replay: PASS
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

Pull request #735 tested result head
`442d66a1764650e49036f2eabd4e17cc427218b3` in public workflow
`33447090686`. Both clean architecture jobs used CPython 3.12.14, exited zero,
wrote empty stderr and reproduced the unchanged verifier hash and committed
stdout hash exactly.

```text
WORKFLOW = 33447090686
EVIDENCE_HEAD = 442d66a1764650e49036f2eabd4e17cc427218b3
TESTED_MERGE = 9b635c57468ba233142441c21c601e14e9673398

X86_JOB = 99668497852
X86_RESULT = success
X86_PLATFORM = Ubuntu 24.04.4 LTS
X86_ARCH = x86_64
X86_PYTHON = CPython 3.12.14
X86_VERIFIER_SHA256 = 3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
X86_STDOUT_SHA256 = a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645

ARM_JOB = 99668497583
ARM_RESULT = success
ARM_PLATFORM = Ubuntu 24.04.4 LTS
ARM_ARCH = aarch64
ARM_PYTHON = CPython 3.12.14
ARM_VERIFIER_SHA256 = 3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e
ARM_STDOUT_SHA256 = a317ee20f5060cce80aef535ebe3f55a1e74d422f4d619ece8978767bbc12645

AGGREGATE_JOB = 99668558513
AGGREGATE_RESULT = success
AGGREGATE_TERMINAL = TWO-ARCHITECTURE CHECK PASS
PUBLICATION_JOB = 99668498904
PUBLICATION_RESULT = skipped as required for a pull request
```

Each architecture also passed repository policy, all 142 unit tests, Canon,
ledger and gate-contract checks before reproducing the changed public probe.
The aggregate job depended on both successful architecture jobs. The required
public two-architecture computation gate is therefore complete.

The theorem status remains proof-first from the self-contained exact proof in
`PREREG.md`; the executable is its independent finite audit. This completed
probe still makes no public Canon edit or gate movement by itself.
