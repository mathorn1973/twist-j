# P-FIELD-ZERO-NONZERO-CUT-1 local run record

Date: 2026-08-18

Status: local reproduction record only. This record does not satisfy the public
two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 4c63a5ac23efb71d6c12bddbc79a7d2788937559
verifier_sha256: 1a5e539c07e4f448eacb99f81e9f9e009efa947225d71ce12d143cd2ffccc2aa
command: python3 probes/P-FIELD-ZERO-NONZERO-CUT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.13
exit_code: 0
stdout_sha256: f5dcf8c2f6115c6ece84303b736cce877e4fec67933c5ea8e37570667b90f6be
stdout_bytes: 889
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 23e307ecfc726cb9a387baefdf51b79e91273e09206c8df7b3c095ae5476a5a0
PREREG bytes:  11374
PREREG blob:   48a785b0a7cb84794837490ef58a601b1c2465f8
verify bytes:  8217
verify blob:   41919519d3cd0d79fdf9babdd7f41d8949dd1595
```

The verifier was executed from a fresh detached worktree of the public
repository at the pushed pin commit, from the repository root. Before formal
execution, both pinned files were read back from the immutable public commit
and matched the local files byte for byte. The canonical repository
reproduction command is the machine-readable `command` field above.

Environment for the accepted run:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

No external data were opened. Both recorded executions exited zero with empty
stderr and byte-identical stdout. The proof in `PREREG.md`, rather than this
finite audit, carries the theorem's quantifier over arbitrary fields.

## Accepted run

```text
field audits:     8/8 PASS
boundary control: 1/1 PASS
decision:         VERDICT PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the byte count, line count,
and SHA-256 recorded above. The repository-required GitHub x86_64 and aarch64
jobs at pull-request time rerun the same pinned verifier and compare stdout
byte for byte, completing the public two-architecture gate.
