# P-QDD-AFFINE-PURE-RECORD-BRIDGE-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the pull-request workflow, which reruns the pinned verifier on x86_64 and
aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: 0c1da26db3b6aca5c5adbf6660196a08ee2be7d1
verifier_sha256: 385aa57dd1968f36ec1f2338c2aae9bb9fcb81da1709db13d791ae69fc814d74
command: python3 probes/P-QDD-AFFINE-PURE-RECORD-BRIDGE-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: b0b81ae919db9f9a30d17f0476f5b05e2b20ef5757f78eb84809c3da60cf3d21
stdout_bytes: 854
stdout_lines: 26
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 2a5601a9ec5cd5c8e24e80f3da78ca6838608fb4

PREREG.md
  sha256: 8417eef90dec350b55b18b01701f7766a04198de553a869bb16ebce8ce9faacb
  bytes:  12348
  lines:  535
  blob:   8b6c3f57a4f3fa9c365db3cc1f43fb962fa8b261

verify.py
  sha256: 385aa57dd1968f36ec1f2338c2aae9bb9fcb81da1709db13d791ae69fc814d74
  bytes:  11355
  lines:  363
  blob:   1958fd45727ad8649ca953d0ca5b020ff0157543

public_pin_comment: issue 497 comment 5371984656
parallel_lane: issue 495 not imported and not used as evidence
```

Both accepted files were read back from the exact public pin before execution.
Their Git object IDs, SHA-256 values, byte counts, ASCII/LF encoding, zero CR
bytes, and final LF matched the accepted bytes. Static AST parsing and syntax
compilation passed before the pin.

The verifier was executed exactly once from a clean repository-shaped
directory under

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
timeout_seconds=120
```

The process started at `2026-08-21T15:37:21Z` and ended at
`2026-08-21T15:37:24Z`.

The verifier process itself returned zero and wrote no stderr. After the
capture files and explicit exit record had completed, the surrounding
execution service emitted `TERM environment variable not set` and a terminal
clear sequence to the tool console. Those service bytes are outside the
verifier process, are absent from captured stdout and stderr, and are not part
of `EXPECTED.txt`. The verifier was not rerun.

## Accepted result

```text
checks: 18/18 PASS
decision: PURE-RECORD-BRIDGE-BOUNDARY
scalar: one exact rank-two blind internal commutator
pure_record: exact reconstruction and 313 finite fibres
global_helper: R_cyc o iota_B0 projectively faithful on Q^4
public_boundary: finite D_matter domain does not own full W
bridge_gate: GATE-L4-L1-QDD-PURE-RECORD unadopted
O2: unchanged
O1: untouched
SAMPLING NOT PROVIDED
```
