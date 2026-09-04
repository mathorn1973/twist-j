# Retarded energy transport formal run

```text
pin_commit: 30ab237b4dcb339115517f67b883ca4cc3e00c32
source_commit: 30ab237b4dcb339115517f67b883ca4cc3e00c32
pin_tree: b04f0fc4b81e5c82a906b7828d95f95d3ad82f5c
base_commit: 2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97
public_lock: https://github.com/mathorn1973/twist-j/issues/822
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/822#issuecomment-5547732894
command: python3 probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-04T23:45:53.774832+00:00
finish_utc: 2026-09-04T23:46:01.179381+00:00
formal_execution_count: 1
exit_code: 0
stdout_sha256: 615c95d924b8e496bbf713c63707d3257818b34517eddad6874e3f3f2ed77c1b
stdout_bytes: 494
stdout_lines: 16
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only, final LF present
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: ff8ed5cce4e12a78ed74248a4343461985b9e14e50aaff33ae51f26e2a32a568
verifier_bytes: 7831
verifier_blob: 5709d08b0bf4b80b08f1737d58d2fed6eefb3dc2
prereg_sha256: a6e37f7aefbb5fa7fd52d0ac23554f58ce340319eb6f1499653f42c6c86c294d
prereg_bytes: 10259
prereg_blob: f1eca717257dc65c4935dc4d72ef49ed6b32a961
public_readback: PASS before formal execution
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
result: CONFIRMED
architecture_gate: PENDING independent GitHub replay
post_result_security_review: PENDING
```

## Complete immutable source inventory

All seven files matched the public commit before execution and retained
the same SHA-256 values before and after the clean Linux run. The verifier
additionally enforces the four runtime dependency/proof/contract hashes.

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/CONTRACT.md` | `89909f2a6b83d751092d1d233b634db523e80e44264932a9bbbd28c05b02527c` | 11843 | `3b735d3d6f91f62ba48f8b383de60aac7501ced4` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/PREREG.md` | `a6e37f7aefbb5fa7fd52d0ac23554f58ce340319eb6f1499653f42c6c86c294d` | 10259 | `f1eca717257dc65c4935dc4d72ef49ed6b32a961` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/PROOF.md` | `8115805719a468bf2ecef2add97640d100b74660ecdbc6e5ee9acc046219143b` | 15062 | `1240971b9c663f7120a30f2173cbb48753ac883e` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/README.md` | `2b781355df08236cddb1b1c99bfa1823cca1ac3c4955cfa8d7bb21b7b0b24005` | 4388 | `657fa73d168fd8bbb72bd7bbac2e40672a4ca415` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/audit_transport.py` | `6d9740ac000f014d6cecb7963fc27d3d0ab4454d6eeed49470ffd075237514cb` | 12664 | `fa82f8d45330c97b040bec379074a3af5d5a92c1` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py` | `983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60` | 11353 | `9af43a4fb9ac812d81bd04c3a047cf9ce720c4ab` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/verify.py` | `ff8ed5cce4e12a78ed74248a4343461985b9e14e50aaff33ae51f26e2a32a568` | 7831 | `5709d08b0bf4b80b08f1737d58d2fed6eefb3dc2` |

## Execution boundary

The exact public pin was checked out in a clean Linux clone. The command ran
from the repository root with LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1 and PYTHONNOUSERSITE=1. No scientific import or
execution preceded the public pin and byte readback. EXPECTED.txt is the
captured stdout byte for byte, with checked digest, byte count, line count,
empty stderr and final LF. This is the sole initial local formal run.

Frozen source documents retain their pre-execution labels. RUN.md and
RESULT.md record later evidence without rewriting those source documents.
Independent architecture evidence is recorded separately when available.
Public claims remain unregistered; Canon v76 and physical gates are unchanged.
