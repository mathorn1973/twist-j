# P-QDD-J-CENTRALIZER-TERMINALITY-1 formal run record

Date: 2026-08-20

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: e1cf7394279d07318571f99d1c81762919a761f9
verifier_sha256: 992f1bcc6b9651a3bf349b5b03c460622b56f8a09790e0b4551cf5180881d2ac
command: python3 probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: fc40a4568cd30ca107d3d48589a070e9896f1f61a5606b995cd9d345fbbe44e4
stdout_bytes: 848
stdout_lines: 23
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent commit: 2fbee86973a5372bf0c96ddbd39b1610fecf72e2
PREREG sha256: 3274806fc70df8793040ab881b6d2ebf256ff485cae794d326b7fb7b941907fd
PREREG bytes: 17331
PREREG blob: 582a8383358a79ef932e0ffe7925cf35e1caaf2b
helper sha256: 12b87e67a4c523428230f2a1acfd88e82697b710456e7c5e69e3f43ba5da8525
helper bytes: 4216
helper blob: 245372ba895758bb7c4990e06629619287efb088
verify bytes: 12450
verify blob: 50a54fae6296b97737e43f2100decfc3de85d0bc
public pin comment: issue #459, comment 5358722036
```

The verifier was executed once, formally, from a fresh local directory
containing exactly the three accepted pinned files under the declared
repository path. Before execution, every SHA-256 matched the public pin
comment, and every remote Git blob matched the independent local Git-object
hash of the bytes.

The accepted process began at `2026-08-20T16:24:17Z` and finished at
`2026-08-20T16:24:32Z`. It used exact standard-library `Fraction` arithmetic
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
files, and explicit exit record had completed. That service warning is outside
the verifier process and is not part of `EXPECTED.txt` or captured stderr.

## Accepted run

```text
checks: 14/14 PASS
decision: BIFURCATION-PASS
negative route: infinitely many post-state classes
positive route: ray terminality selects one Lueder physical class
strict route: branch idempotence selects the positive Q representative
boundary: global O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
