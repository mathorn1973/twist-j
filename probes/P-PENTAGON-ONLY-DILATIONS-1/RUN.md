# P-PENTAGON-ONLY-DILATIONS-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: a9ef097e40c00bcdb38492e483ed9130a5e9bd9c
verifier_sha256: 68182f3c34d15ec8f09d2d494e3783292187466d953821659b4a11ff8195a8fe
command: python3 probes/P-PENTAGON-ONLY-DILATIONS-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: 129622f859b8db60d2316a1f6d4e937c85a9380242db508b92ece50b1f98d2d8
stdout_bytes: 1161
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 8419ca616fe17067204d2023f5ae7a6279dcaaa42e6d189a7a349c95ce2d3e88
PREREG bytes:  6274
PREREG blob:   57c349fc6a220596efaff5ff4a5575a8af8d508b
verify bytes:  5382
verify blob:   872c9af2fe38e2c7c1789eb67a40510c386ac0b9
public pin comment: issue #445, comment 5353256243
```

The verifier was executed once, formally, from a clean checkout of the
public repository at the pushed pin commit, from the repository root.
Before execution the SHA-256 of both pinned files was read back from that
checkout and matched the values recorded at the pin and in the public pin
comment. `EXPECTED.txt` is the exact raw stdout of that one execution, LF
line endings, final LF. The process exited zero and wrote no stderr.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data exist in this probe. Wall time under one second, within
the 120 second budget declared in `PREREG.md`. As disclosed in `PREREG.md`,
the probe is result-exposed; the candidate file was smoke-executed once
before the pin, outside the repository, revealing nothing not declared.

## Accepted run

```text
checks:   6/6 PASS
decision: pentagon-tower dilations miss every cross-prime direction by an
          exact positive constant; the route is dead
```
