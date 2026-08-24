# P-J-LI-CARRIER-NOGO-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 5d84bc937e744af2f094ad86e4cb56898cdb63ac
verifier_sha256: 762bcaf2aa077c7e86e04fe96b7a2d7125f0469de889388b8a1b75487b307697
command: python3 probes/P-J-LI-CARRIER-NOGO-1/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: x86_64
python: CPython 3.11.15
exit_code: 0
stdout_sha256: 83eb6d677863ba57dae0f4da440ff20d8d5c85724051ba64a3da63389d070fe3
stdout_bytes: 1185
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 159d6ccdcd8e589ddee29c85d99f77bc20487241bf368c8016c040779ce5e039
PREREG bytes:  6273
PREREG blob:   3329f0f4fc778ab4cd2b1a73fa8f3fad3a57f754
verify bytes:  5895
verify blob:   8a6b76ba6de9352b61c21203d64bd34584f1a880
public pin comment: issue #447, comment 5353332762
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
decision: finite mechanism audits pass; the carrier exclusion is carried
          by the written proof with imports labeled
```
