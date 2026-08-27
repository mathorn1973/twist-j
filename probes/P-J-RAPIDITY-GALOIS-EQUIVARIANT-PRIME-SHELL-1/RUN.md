# P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1 formal run record

Date: 2026-08-26

Status: local accepted formal record. The public two-architecture gate is
completed by the repository pull-request workflow, which reruns the pinned
verifier on x86_64 and aarch64 and compares stdout byte for byte against the
single committed `EXPECTED.txt`.

The flat fields below are the machine-readable record required by the public
repository checks.

```text
pin_commit: 4b590f861504edc0e0884c5140facc9177a1144a
verifier_sha256: ca82c5e87c9b41e269db7c9b7139e3f8bc431c85abbc6d3ad38c0fad9b0fcaf4
command: python3 probes/P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1/verify.py
platform: macOS 26.5.2
architecture: aarch64
python: CPython 3.9.6
exit_code: 0
stdout_sha256: 157f651499c12f967ede03136659ad7954eb57a7e15dd2828fb09c6b89e5fba5
stdout_bytes: 812
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: ed699e7190058dd8d23c2f5403141d278b447c4ad899882c74b0eb3225d089ff
PREREG bytes:  13259
PREREG blob:   bed89ac3228ad70d4a4b89eeb3b92d7de89147fe
verify bytes:  12230
verify blob:   e9bc679ac21f14dfc8b06c970aa99b9fb5a3c542
public pin comment: issue #578, comment 5432135074
```

The verifier was executed once, formally, from a fresh clone of the public
repository at the pushed pin commit. Before execution the SHA-256, byte count,
and Git blob of both pinned files were read back from that clone and matched
the public pin comment. `EXPECTED.txt` is the exact raw stdout of that execution,
with LF line endings and a final LF. The process exited zero and wrote no
stderr.

Accepted environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened. The only pre-pin action on the accepted public
verifier was static AST parsing; earlier computations belonged to the disclosed
non-canonical reconnaissance and are not evidence for this record.

## Accepted result

```text
checks: 7/7 PASS
positive result: exact L1 theorem package survives
negative controls:
  same-root eigenline/prime-ideal label FIRED-AS-EXPECTED
  unrefined scalar-correction tail FIRED-AS-EXPECTED
```

The pinned `PREREG.md` and `verify.py` were not changed after the pin.
