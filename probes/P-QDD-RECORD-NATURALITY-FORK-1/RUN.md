# P-QDD-RECORD-NATURALITY-FORK-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 17668ff8bf1eca3c1866a71bbacda92f2c811da6
verifier_sha256: 25087c9a22c2c0aa4ecd2a4aa6bd8e78283c2ba8feba63152422b47f69f5f5a3
command: python3 probes/P-QDD-RECORD-NATURALITY-FORK-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 93e4a72975bbc074a8fcacaa882f9de2d8c4dc3c326e34cedeffaa46d9c68bb7
stdout_bytes: 901
stdout_lines: 24
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: e6845b96fc19a47c473761ad49d4f8a7812c2f58
prereg_sha256: 812a93353a3f05f122ecf51cd7dd9d9baf9866fbf0940e18a650af6600be9ba9
prereg_bytes: 15904
prereg_lines: 580
prereg_blob: dcaade408f9b19a3dd45377bee30d96c229a7960
verify_bytes: 16135
verify_lines: 518
verify_blob: 78a545aa70e70a4abbfcfbdf423e1c1db9b6766f
public_pin_comment: issue 476 comment 5360977200
```

Both accepted files were fetched from the public remote at the exact pin before
execution. Their SHA-256 values, byte counts, line endings, final LF, and Git
blob IDs matched the independently prepared local bytes.

The accepted verifier was executed exactly once from a clean
repository-shaped directory. It began at `2026-08-20T19:56:57Z` and finished
at `2026-08-20T19:57:01Z`. The environment was:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and final LF. The
process wrote zero stderr bytes. The verifier was not rerun.

## Accepted run

```text
checks: 10/10 PASS
decision: NATURALITY-FORK
strict_route: strict law naturality gives one Lueder sign class
weak_route: uniform quotient covariance gives 48 algebraic members and 24 sign classes
transposition_control: same effects and record, weakly covariant, nonterminal
comparison_equality: extended +-S4 gauge quotient gives one newly identified class
public_derivation: strict naturality and enlarged equality are not derived
global_scope: O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
