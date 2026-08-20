# P-QDD-J-AFFINE-APPARATUS-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 6d71e93930e1b891ac14986ea0cd44550d834262
verifier_sha256: f946497132b0f12bb781b14e269c6c37442948bca60d7247563d4271e9e08246
command: python3 probes/P-QDD-J-AFFINE-APPARATUS-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: ae944d523ffb77319907e50799812e7fabdbc9952c9bdbd93d6d854cc12de80c
stdout_bytes: 781
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: c25f3b3e1b6f5ffe37e8fedc2f0d4008194d508374117f77aa60bb6363dea25a
PREREG bytes:  10056
PREREG blob:   d8335ebf5182b37688766c666369efd6082b52bd
helper sha256: 76b30b33d3b7994dc4230941d353dd3c8c737212f556d9341043ae38b31f5dfb
helper bytes:  4214
helper blob:   2d46ed2232feca0a8273aec96dfafe89206e50f5
verify bytes:  6252
verify blob:   e45aeccd82c3e85bc892b57b5eb9f495c50c9548
public pin comment: issue #456, comment 5357998645
```

The verifier was executed once, formally, from a clean local directory
containing only the three accepted pinned files under the declared repository
path. Before execution, every SHA-256 matched the public pin comment and every
remote Git blob ID matched the independently computed local `git hash-object`
value. `EXPECTED.txt` is the exact raw stdout of that one verifier process,
with LF line endings and final LF. The verifier process exited zero and wrote
no stderr.

The surrounding execution service emitted a terminal-cleanup warning only
after the verifier process, captured stdout, captured stderr, and explicit exit
record had completed. That service warning is outside the verifier process and
is not included in `EXPECTED.txt` or stderr. The process evidence above is read
from the explicit exit-code and capture files.

No locale, hash-seed, timezone, or bytecode environment override was supplied
to the accepted local process. The verifier uses exact standard-library
`Fraction` arithmetic and no external data.

## Accepted run

```text
checks:   11/11 PASS
decision: NONUNIQUE
scope:    restricted target-independent J-affine L4 apparatus class
boundary: global O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
