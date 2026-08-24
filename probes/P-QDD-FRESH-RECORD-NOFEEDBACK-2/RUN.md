# P-QDD-FRESH-RECORD-NOFEEDBACK-2 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 219fb7ce95a3c842fe3c2dfcc2fd142b918f9c4b
verifier_sha256: 45132e5dd30910023a27e46f361cd2acf70600ecae7b920dc2a34139aee1b439
command: python3 probes/P-QDD-FRESH-RECORD-NOFEEDBACK-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 1939173794601f5b8db8bfe86e1c80936737c4460f2f451df65854743cd2faf4
stdout_bytes: 783
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent commit: 4ef54f0c34f80897af0121a2d93b710e70a8377c
PREREG sha256: ec4a7d67f9b3c1538bfce99c93d72a707be3d7b4b6d0e4a72ec9d7fa38ff3bf4
PREREG bytes: 9320
PREREG blob: a67a36ff791e04d6d778f0a3ddce33aa57dd3593
verify bytes: 9395
verify blob: 54d4f60923a6c7d1ebfe2f14f64bee8110ee091a
public pin comment: issue #472, comment 5360186841
predecessor STOP: issue #470, no scientific conclusion and no reused evidence
```

The verifier was executed once, formally, from a clean local directory with
the two accepted pinned files under the declared repository path. Before
execution, both SHA-256 values matched the public pin comment, and both remote
Git blob IDs matched independent local Git-object hashes.

The accepted process began at `2026-08-20T18:40:51Z` and finished at
`2026-08-20T18:40:54Z`. It used exact standard-library `Fraction` arithmetic
and no external data. The environment was:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw process stdout, with LF endings and final
LF. The process wrote zero stderr bytes. The surrounding execution service
emitted a terminal-cleanup warning only after the verifier process, capture
files, and explicit exit record had completed. That warning is outside the
verifier process and is not part of `EXPECTED.txt` or captured stderr.

## Accepted run

```text
checks: 14/14 PASS
decision: NONIMPLICATION
negative route: fresh append-only no-feedback repeatability does not imply projective idempotence
witness: target-independent J-native T_star = R - C
positive boundary: record sufficiency is the extra terminality premise
boundary: global O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
