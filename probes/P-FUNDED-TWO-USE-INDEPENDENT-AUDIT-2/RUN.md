# First pinned Linux run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: 4947a92a5e5ca471e7acde009ef255e17a61a493
verifier_sha256: ca69ea36e59013f9867d316ddcd4ea7b35382a72f554e972df346f21a0233c47
command: python3 probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-2/verify.py
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
exit_code: 0
stdout_sha256: ced7a6aec4b4acd83e0ec35abcdd5c4c200787b71eee235417e19b73681f2075
stdout_bytes: 4722
stdout_lines: 49
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

First execution started 2026-10-15T11:21:08.415405+00:00 and ended 2026-10-15T11:21:19.843559+00:00;
elapsed 11.428140 seconds, timeout 600 seconds, no timeout.
The public pin was cloned and detached at the exact commit; its sole parent
is the declared public main. The checkout was clean before and after the run.
All frozen file hashes were checked before the scientific import. Command ran
from repository root with LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. Exact binary stdout/stderr were captured separately;
EXPECTED.txt is the unedited stdout. No scientific code changed after pin.

Public PINNED/readback receipt: #1516 comment6190834003. Neither owner nor
helper opened counterpart I2 scientific code/output/digest before this record.
This is a completed exact first-run PASS on one architecture, not the final
required dual-architecture replay or cross-implementation comparison.
