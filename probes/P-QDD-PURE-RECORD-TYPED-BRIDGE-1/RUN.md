# P-QDD-PURE-RECORD-TYPED-BRIDGE-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the pull-request workflow, which reruns the pinned verifier on x86_64 and
aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: 78b35777cdabbfbbfc61ce2866fd8e9ce09bc711
verifier_sha256: 16adcb43261d8e2154d96ea33e47e94f4c371cff451ec82f96a1dd75bf3719b3
command: python3 probes/P-QDD-PURE-RECORD-TYPED-BRIDGE-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: b8fdbaba86684e4881b51e369cb72a0a9f93ea4fca94b215fbd7e075a9ac561c
stdout_bytes: 1048
stdout_lines: 30
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 1b288cbed5a9ccdfed5edde906df82fa1522870e
prereg_sha256: 221bb4d9e54c132b186f2e773ab82c060b8729e0e1f83cd63597cff67528ccd8
prereg_bytes: 12146
prereg_lines: 397
prereg_blob: 766f282d4b0838e02afc1c2207748e93937105b0
verify_bytes: 13024
verify_lines: 490
verify_blob: 33bc8f71465c5b416d83561bc4c182a3070138aa
public_pin_comment: issue 502 comment 5373309052
```

Both accepted files were fetched from the exact public pin before execution.
Their Git blob IDs, SHA-256 values, byte counts, LF endings, final LF, and
ASCII/UTF-8 decoding matched the accepted bytes. Static parsing and syntax
compilation passed before pinning. No accepted-verifier execution occurred
before the pin.

The accepted verifier was executed exactly once from a repository-shaped root.
It began at `2026-08-21T17:47:07Z` and ended at
`2026-08-21T17:47:09Z`. The process environment was:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and final LF. The
verifier process wrote zero stderr bytes. The surrounding execution service
printed `TERM environment variable not set` only after the process and capture
files had completed; it is not verifier stderr and is not part of the evidence.
The accepted verifier was not rerun.

## Accepted run

```text
checks: 21/21 PASS
decision: READONLY-BRIDGE-ONLY
global_record: exact and faithful on Q^4 minus zero modulo sign
finite_leg: 313 fibres, insufficient for the infinite rational source
static_encodings: two explicit disjoint exact encodings, not selected
U_congruence: frozen faithful motor-to-tail class empty
L4_restriction: one rank-two internal commutator distinguished
public_gate: GATE-L4-L1-QDD-PURE-RECORD absent on the v59 basis
global_scope: O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
