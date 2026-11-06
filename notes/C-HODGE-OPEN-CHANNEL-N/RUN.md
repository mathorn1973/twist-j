# Original first-execution record

**NON-CANONICAL. L1. C-HODGE-OPEN-CHANNEL-N.**

Accepted public pre-execution commit: [668f28977a9adcfd2c41a044ffa15997c7d94d16](https://github.com/mathorn1973/twist-j/commit/668f28977a9adcfd2c41a044ffa15997c7d94d16).
Accepted tree: `e39eddb91300d02e1bbe4ed1a14a2a3737935bb3`.

All eight accepted files were published before any scientific execution or import, fetched back from this immutable commit and checked byte for byte. The local worktree was fetched and checked out at exactly this pin, with empty git status. Each file hash and byte count was rechecked before the first run.

Each accepted program was executed once, sequentially. These are the original outputs; no scientific repair, rerun, changed threshold or substituted expected output occurred. The accepted worktree remained clean after both runs. The result files are additions; none of the eight accepted files changes.

## Neutral environment

- Platform: Ubuntu 24.04.3 LTS.
- Architecture: `x86_64`.
- Python: `3.12.14`.
- Environment: `LC_ALL=C.UTF-8`, `TZ=UTC`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`.
- Working directory: repository root.

## Original execution streams

| Program | Started UTC | Completed UTC | Exit | stdout bytes | stderr bytes |
|---|---|---|---:|---:|---:|
| `verify.py` | 2026-10-23T09:37:40.029791+00:00 | 2026-10-23T09:37:59.773065+00:00 | 0 | 581 | 0 |
| `break_certificate.py` | 2026-10-23T09:37:59.773623+00:00 | 2026-10-23T09:37:59.821028+00:00 | 0 | 415 | 0 |

| Output | SHA-256 |
|---|---|
| [EXPECTED.txt](EXPECTED.txt) | `4cb540b52f09584b71f16568a9797fadbbff3739adc787bb6c75ff271d809934` |
| [BREAK_EXPECTED.txt](BREAK_EXPECTED.txt) | `421b82fb4e2b797caec648c5d4268a0e397c9273384034336be0e30d163a371a` |

Both empty stderr streams have SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Counts and digests include the original terminal newlines.

## Accepted scientific contract

| File | Bytes | SHA-256 |
|---|---:|---|
| [PREREG.md](PREREG.md) | 10793 | `66916a78143ef49e0511fd4a53467dac6e48b8f5e3735ba46e78bec66e2b3fa1` |
| [PROOF_CURRENT.md](PROOF_CURRENT.md) | 18741 | `fd9ef380f700ba03295c158db8d9bff37dab1fa87204b7fac49af20471db03d3` |
| [PROOF_PORT.md](PROOF_PORT.md) | 18535 | `9f7428ebca237586012c4c04bd06b1b02451214db0fa0631fe4f6ea0354485db` |
| [PROOF_REDUCTION.md](PROOF_REDUCTION.md) | 8295 | `f170abec693e645eaecc2d04888b3514e36c42b1d07b0655c736b8a22b872ffb` |
| [README.md](README.md) | 8810 | `5d5dbc05cd7c768264f0b0126372337fbf789ba3c84c8f318ff2bb8d1f21404e` |
| [SOURCES.md](SOURCES.md) | 6480 | `63837957ecd1c149e6a7cb0904dba9e5073fe0f978f3f8d2078e2f4d8a37997e` |
| [break_certificate.py](break_certificate.py) | 12829 | `828bbb7b3e522849378f551204260256c9bdd50c276d0bb49cb4074fc1f8dda0` |
| [verify.py](verify.py) | 15525 | `be6851d2f3fcaff01617e5b02b5ec1ea93a6631bea3ba6f6578847dd3f51599a` |

## Reproduction commands

```sh
LC_ALL=C.UTF-8 TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python notes/C-HODGE-OPEN-CHANNEL-N/verify.py
LC_ALL=C.UTF-8 TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python notes/C-HODGE-OPEN-CHANNEL-N/break_certificate.py
```

Require exit 0, empty stderr and stdout byte identical to the corresponding committed output. The programs use only the Python standard library and read no external scientific code or data.

This record is one x86_64 scientific execution. The repository workflow does not execute these programs under notes; its x86_64 and aarch64 jobs are not a two-architecture scientific gate. Universal statements rest on the explicit analytical proofs, with finite audit scope recorded separately.

## Repository validation

The local repository policy check, all 210 unit tests, the Canon v104
check, the evidence/dependency ledger check and the explicit gate-contract
check passed. The changed-public-probe and changed-minimal-reproduction
selectors both reported not applicable for this notes-only change.
These repository validations are separate from the two scientific
executions above; no accepted scientific program was rerun by them.
