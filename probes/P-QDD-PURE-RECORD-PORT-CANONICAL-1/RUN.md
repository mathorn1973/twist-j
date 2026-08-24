# P-QDD-PURE-RECORD-PORT-CANONICAL-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: 39016daa975aa9ddfc0cd861084f96284b40a9ed
verifier_sha256: df5eb038e750c22d2702bd4c3c35d06a0b554bad8bab435df7bf08da783acc23
command: python3 probes/P-QDD-PURE-RECORD-PORT-CANONICAL-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: cd97da93f5c8a4ce165f77aeb310205877d107004b679fed4bde44bb173a4d22
stdout_bytes: 669
stdout_lines: 25
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 47fa9ddd8db5e9fdbbd4440f29107ca298898350
prereg_sha256: ab2e13e3197950b7cbe18bdb9c40f1963eced337e5d0f4da1c3239b6a6d12e98
prereg_bytes: 11115
prereg_lines: 367
prereg_blob: 192e798acc1783a52613734462369a1ca7898113
verify_bytes: 5469
verify_lines: 121
verify_blob: 8ac22f24a0f6f52de3a7f8ecc8c909e1972a0f70
public_pin_comment: issue 505 comment 5373650749
```

Both accepted files were read back from the exact public pin before execution.
Their Git blob IDs matched the locally recomputed Git object IDs, which fixes
byte identity. Both files are ASCII with LF endings and a final LF. Static
syntax compilation passed before the pin; the accepted verifier was not
executed before the pin.

The accepted verifier was executed exactly once in a repository-shaped root
under

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The process returned zero and wrote empty stderr. `EXPECTED.txt` is the complete
raw stdout with LF endings and final LF. The verifier was not rerun.

## Accepted run

```text
checks: 17/17 PASS
decision: PORT-CANONICAL
ordered_source: full rational W sign quotient
direct_port_class: singleton
overlap: 84 nonzero balanced vectors, 42 sign classes
read_only: feeds_U=FALSE, no source-to-K encoding
schema_boundary: separate bridge manifest possible, public gate unregistered
global_scope: O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
