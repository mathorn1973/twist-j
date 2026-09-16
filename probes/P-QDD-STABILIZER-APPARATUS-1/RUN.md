# P-QDD-STABILIZER-APPARATUS-1 formal run record

Date: 2026-09-06.

Status: one completed local formal run after public pin/readback.
The independent public two-architecture replay is performed by the PR workflow.

```text
pin_commit: 515bdf33f04bd43cbe5e48e0522d844fd6135f37
verifier_sha256: 54ce2c4b6ab16d45800987ba9aeaf444a569c86e9fd842317ec7ea95a2c2bdee
command: python3 probes/P-QDD-STABILIZER-APPARATUS-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 1803b09225dc11f21f618be83db78025e83943e5fae90b6fbb31c9ed96aacc84
stdout_bytes: 292
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The local leg used Ubuntu under WSL2. It ran from the repository root with
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1.
The verifier ran once, took approximately 20.91 seconds, and returned all
eight gates PASS. Its child-process stdout and stderr were captured as raw
bytes; EXPECTED is those exact 292 stdout bytes, without wrapper metadata
or shell newline conversion. No scientific program was executed before pin.

## Complete pin custody

Public reservation: [issue 854](https://github.com/mathorn1973/twist-j/issues/854).
Public pin/readback: [comment 5557409419](https://github.com/mathorn1973/twist-j/issues/854#issuecomment-5557409419).
All seven files were fetched from the public GitHub contents API at the pin,
compared with committed blobs and the clean local tree, and hashed again
before and after execution. No pinned source changed.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 9821 | `f94f7b487b39f6a2a682346ddd3db1417c72a533d8dbc10302811db1a84f21b9` |
| PROOF.md | 17723 | `7aed4f0d3181724376097397d0a033e2c6a0b653b3b04fe91eb97c833b8d5062` |
| apparatus.py | 4832 | `f5643442653a82a591e2e4ea6e6ef44f54f13f0c604fcaa62bd8d2cf64df8524` |
| verify.py | 15983 | `54ce2c4b6ab16d45800987ba9aeaf444a569c86e9fd842317ec7ea95a2c2bdee` |
| RECORD-CONTRACT.md | 8632 | `51db9e55c90e751c539cf758ebd6ff3f747b3a31d88cb6dfb8e8611df5dc12f4` |
| record.py | 8437 | `6e3b89b25ea027be6f6ea267b85029a97d350e12b4a63f830e7c28cbf01ae3ee` |
| record_audit.py | 7931 | `6b33c1315c39d3dfa0db756c992903d6c1c8ea4b224824d163cdc83fb42aabe8` |

## Scope

This is an exact audit of the frozen conditional L4 mathematical model.
The general mixer-class and lattice proofs are frozen in PROOF.md; finite
PASS output does not substitute for their universal arguments. No physical
apparatus, event law, Born occurrence, Canon promotion or parent-O closure
is asserted by this run record.
