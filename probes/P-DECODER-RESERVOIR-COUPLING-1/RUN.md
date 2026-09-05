# Reservoir coupling formal run

```text
pin_commit: 550420d188a45c4929e300ca6aabcde812f4d65a
source_commit: 550420d188a45c4929e300ca6aabcde812f4d65a
pin_tree: 4f7b74980c01dfe443c102608aa9e65b58ce509e
base_commit: a353b7e2aaec3e13f458f52e68c6464b9d718e67
public_lock: https://github.com/mathorn1973/twist-j/issues/824
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/824#issuecomment-5547895682
command: python3 probes/P-DECODER-RESERVOIR-COUPLING-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-05T00:07:30.890270+00:00
finish_utc: 2026-09-05T00:07:43.927412+00:00
formal_execution_count: 1
exit_code: 0
stdout_sha256: 370ae19a621222b100dd22d6e9d7eea6fff09774746e29081edf3bab722be326
stdout_bytes: 437
stdout_lines: 14
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only, final LF present
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: 8daa2f935c005b9a09221d6ca0172582f0fda028e5b65230f98b383cf294b16d
verifier_bytes: 7939
verifier_blob: e8ae6895ad083539af2e28f83d5b0824be89a417
prereg_sha256: bd05455541232803d65868eafec04198a60829678a2f568062f3eed331cdc02b
prereg_bytes: 11963
prereg_blob: a02e472a6715a640f0dc56c05ee3dc17668aee41
public_readback: PASS before formal execution
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
result: CONFIRMED
architecture_gate: PENDING independent GitHub replay
post_result_security_review: PENDING
```

## Complete immutable source inventory

All eight dependency/source files (seven new and one inherited) matched the public commit before execution and retained
the same SHA-256 values before and after the clean Linux run. The verifier
additionally enforces the four runtime dependency/proof/contract hashes.

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `probes/P-DECODER-RESERVOIR-COUPLING-1/CONTRACT.md` | `935ccb861096328ae523145b55135541029dba4d000c14f2aa51acddd5ca36c8` | 16579 | `a61559f11664c50930f6e83ef34bcbaa45ba5755` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/PREREG.md` | `bd05455541232803d65868eafec04198a60829678a2f568062f3eed331cdc02b` | 11963 | `a02e472a6715a640f0dc56c05ee3dc17668aee41` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/PROOF.md` | `b4608f99bff54cb89ce9c5292f79f8738d8df8245a6a9e275afb48295f7731d0` | 15392 | `d98878c834cce9b266fcd010e6f14a48bca23842` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/README.md` | `b7ed67afe91dcbf1437ea7a7434d0c347967c09403bc1ed497616fc775bbb2f1` | 5297 | `7f00623b3986a65b09d9a74d19477f06502a9d60` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/audit_coupling.py` | `28cf0f018ecdc756f58f70e8dfb63f72c033750c62c59feba98df56f283a1385` | 13587 | `5d74c89d924fa41c11eb220ebd2202acda0e6d8b` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/coupling.py` | `54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403` | 7966 | `6fd369a86ec8585877377b801aa01b852789ec20` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/verify.py` | `8daa2f935c005b9a09221d6ca0172582f0fda028e5b65230f98b383cf294b16d` | 7939 | `e8ae6895ad083539af2e28f83d5b0824be89a417` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py` | `983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60` | 11353 | `9af43a4fb9ac812d81bd04c3a047cf9ce720c4ab` |

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
