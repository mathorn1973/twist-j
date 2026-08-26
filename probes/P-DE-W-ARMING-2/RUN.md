# P-DE-W-ARMING-2 formal run record

Date: 2026-08-26

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 01f1ac3e0af34b8223460a4151168e0edea67b81
verifier_sha256: 5387eaf687aaba0c8bf2925b2772f732926d1f17a48c57700e70f6deebc56ab0
command: python3 probes/P-DE-W-ARMING-2/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: a27410b63c023c1a589ca3423522f7c11ebe0d4610bb9d20651b8aa3bda0aa0b
stdout_bytes: 1492
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 6592005e2d5985cac52687eb99bb0371facaf8f9e0ca78872da76911c5ed4069
PREREG bytes:  8548
PREREG blob:   3ea06c476500b7e05e10e74458e49197f7ce3e09
verify bytes:  5322
verify blob:   2910793676a92113b89fddd1d0f3442a6858f062
public pin comment: issue #576, comment 5428791045
```

The verifier was executed once, formally, from a fresh clone of the public
repository at the pushed pin commit, from the repository root. Before
execution the SHA-256 of both pinned files was read back from the fresh
clone and matched the values recorded at the pin and in the public pin
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

No external data were opened at run time; the record evaluated is the
quoted-summary entry frozen inside the pinned verifier, with its readback
provenance disclosed in `PREREG.md`. Wall time under one second, within the
120 second budget declared in `PREREG.md`. As disclosed in `PREREG.md`, the
probe is result-exposed; the pre-pin smoke runs (including the one that
exposed and fixed the malformed G7 guard before the pin) are not evidence
and are not this record.

## Accepted run

```text
checks:   9/9 PASS
decision: R1 FIRED; DE-W-CONSTANT [H] -> F at the next sealed fold
```
