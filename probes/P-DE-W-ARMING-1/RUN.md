# P-DE-W-ARMING-1 formal run record

Date: 2026-08-19

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 516538cd73b35e3e2877acd5382e0e188638a706
verifier_sha256: 0321d6e6c123bdec4f8847b7513c340fdd58392ac41297433d8879def7e66290
command: python3 probes/P-DE-W-ARMING-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: cb55279b43f82504fddb0ca35a0ec28e35b0cb5bdf6514b96c061f84966b66f1
stdout_bytes: 2061
stdout_lines: 27
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 241a0222f8a651a47092a3b7486f5aa9f2fa8422383193947c20a9e42522c101
PREREG bytes:  9169
PREREG blob:   c3a7ef02694ba27987fc779a92a5de58aa011fbf
verify bytes:  7431
verify blob:   5a11cf9f12bb45f49bea5ae8ee3770d76ce431b2
public pin comment: issue #442, comment 5352429691
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
quoted-summary table frozen inside the pinned verifier. Wall time under one
second, within the 120 second budget declared in `PREREG.md`. As disclosed
in `PREREG.md`, the probe is result-exposed and the candidate file was
smoke-executed once before the pin, outside the repository; that smoke run
is not evidence and is not this record.

## Accepted run

```text
checks:   10/10 PASS
decision: DE-W-CONSTANT ARMED, HOLDS
```
