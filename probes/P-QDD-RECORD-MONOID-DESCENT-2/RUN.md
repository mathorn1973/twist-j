# P-QDD-RECORD-MONOID-DESCENT-2 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 7f4fe2e60983cf052813760d47e6f1a5885422d0
verifier_sha256: 82e1944d8e51b5704eedf31091ad35dfd4ceb4ee767958496efe6a8e269e6962
command: python3 probes/P-QDD-RECORD-MONOID-DESCENT-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: e2c9367ac848194ac658f1587e344522fdaea2bc1d7359ba2fd4fe20dd05573d
stdout_bytes: 1227
stdout_lines: 42
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 7820173bdf035fa8b59e40113fdad3ac3c66f12a
prereg_sha256: b0ee79e4e967f8d1c44d48c9cda3b8e3cd73343bf7f07c5b3474c9a499897c1d
prereg_bytes: 7412
prereg_lines: 275
prereg_blob: 8d52415ab61070eed5eee4ec2d688cb600588656
verify_bytes: 7427
verify_lines: 148
verify_blob: 2764071fbacb39111ba1acdab01708c457b134bc
public_pin_comment: issue 490 comment 5369990410
predecessor_stop: issue 489, no scientific conclusion and no reused evidence
```

Both accepted files were read back from the exact public pin before execution.
Their Git object IDs, SHA-256 values, byte counts, LF endings, final LF and
UTF-8 decoding matched the accepted bytes. Static parsing and syntax
compilation passed.

The accepted verifier was executed exactly once from a clean
repository-shaped directory. It began at `2026-08-21T12:48:54Z` and finished
at `2026-08-21T12:48:56Z`. The environment was:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and final LF. The
process wrote zero stderr bytes. The surrounding execution service emitted
`TERM environment variable not set` only after the verifier process, capture
files and explicit exit record had completed. That service warning is outside
the verifier process and is not part of `EXPECTED.txt` or captured stderr. The
verifier was not rerun.

## Accepted run

```text
checks: 36/36 PASS
decision: RECORD-MONOID-NONDESCENT
finite_orbit: period two under one persistent HIGH symbol
infinite_orbit: exact non-root-of-unity certificate trace 6/5
descent_boundary: saturation iff projective idempotence iff the sign class of Q
operation_boundary: same-record conditioning is not fresh apparatus reinteraction
global_scope: O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
