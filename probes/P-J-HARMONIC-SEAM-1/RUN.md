# P-J-HARMONIC-SEAM-1 local run record

Date: 2026-08-09

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

## Pin

```text
PIN_COMMIT:      61aa12c2b0e9705c3c0d9fb91fc4cfe6c80697ff
PREREG sha256:   751807cb6a84d2e9f06dbf2995d6f9395b57d1a8ea4e285f0736dc27850565f4
PREREG bytes:    9363
verify sha256:    9aa0b47f91c8e57c421b900d4578d159537715cca773c404209c20fd1ec71a40
verify bytes:     9079
```

The verifier was executed from a local byte-identical copy of the public pinned
`verify.py`. Before execution, both its SHA-256 and its Git blob identity were
checked against the public remote.

## Environment

```text
platform:       Linux 6.18.35
architecture:   x86_64
Python:         3.13.5
LC_ALL:         C
LANG:           C
PYTHONDONTWRITEBYTECODE: 1
PYTHONHASHSEED: 0
TZ:             UTC
command form:   python3 <byte-identical-local-copy-of-pinned-verify.py>
```

No external data were opened.

## Accepted run

```text
exit code:      0
stdout bytes:   1548
stdout sha256:  8198dc9c8c7dcc188d04635ec4c365e86dcb4524e28b347f2b2d1da1c943118d
stderr bytes:   0
stderr sha256:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
checks:         38/38 PASS
decision:       SEAM-PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the same byte count and
SHA-256.

## Rejected launcher attempt

Before the accepted clean-system run, the same pinned verifier bytes were
invoked through a notebook Python launcher. That launcher injected unrelated
spreadsheet-runtime startup diagnostics on stderr before verifier execution.
The attempt was therefore rejected as an integrity STOP and contributes no
scientific evidence. No file, threshold, equation, or verifier byte changed
between the rejected launcher attempt and the accepted run.

The accepted result above is the first evidence-bearing local run. A repeated
clean-system execution produced the identical stdout hash and empty stderr;
that repetition is reproduction only, not independent confirmation.
