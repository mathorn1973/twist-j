# Run Record: `C-HOMOGENEOUS-RECORD-RETENTION-N`

**PUBLIC, NON-CANONICAL.**

## Pin

| Field | Value |
|---|---|
| Prospective pin commit | `24cc067983142017d3fd9a111acf80d6ab29db54` (pushed and read back before execution) |
| Parent | `892a0b11089d34e241e1eb76d2c03247022d18e6` (main, tag `canon-v105`) |
| `verify.py` | SHA-256 `a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7`, 33053 bytes |
| `notes/.../PROTOCOL.md` | SHA-256 `afd849bd4aa20a41588f29e2b5d22575a3754bb45a5583e7eea50bf6746a034f`, 10333 bytes |
| `notes/.../PROOF.md` | SHA-256 `d806d79ba7a647c1467c966c590c7b666de40e21bf60db6b99d60e20d5deb0b6`, 28645 bytes |
| `notes/.../INTERFACE.md` | SHA-256 `3e7657f899a83aede34823700170611f419f2e47e1e68b6082d68bbdec4b928f`, 3976 bytes |
| `notes/.../SOURCES.tsv` | SHA-256 `3e55ad8d45179c8e0f6af34ed55387c970ba205f2bb2d18c18b581537d3c1c6b`, 3267 bytes |

## Formal execution

| Field | Value |
|---|---|
| Checkout | clean detached worktree of the pin (no modified or untracked files) |
| Command | `python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py` from the repository root |
| Environment | `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` |
| platform | Ubuntu 24.04 |
| architecture | x86_64 |
| Python | 3.13.17 |
| Time (UTC) | 2026-10-24T17:38:49Z to 2026-10-24T17:38:50Z, about 1 second wall time |
| Exit code | 0 |
| Standard error | 0 bytes |
| Standard output | 1162 bytes, SHA-256 `dccec8381f051efede09b61cea2b15c6735a883a4286e2d13c131bc2ea0164d3`, saved unchanged as `EXPECTED.txt` |
| Checks | 187 (groups 1–6: 5, 21, 14, 127, 11, 9) |

## Attempt custody

One invocation preceded the formal execution at 2026-10-24T17:38:38Z. It wrapped
the same command in an external timing utility that is not installed on the
platform; the wrapper failed with exit code 127 before any Python process
started, so the verifier was not executed and produced no output. No file
changed between that invocation and the formal execution.

## Cross-architecture gate

This local run is x86_64. The pull-request workflow reruns the unchanged
verifier on GitHub-hosted x86_64 (`ubuntu-latest`) and aarch64
(`ubuntu-24.04-arm`) with Python 3.12 and compares standard output with
`EXPECTED.txt` byte for byte; the aarch64 job supplies the different
architecture.
