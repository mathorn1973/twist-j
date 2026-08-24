# P-LAMBDA-COCYCLE-ANGLES-2 formal run record

The preregistration and verifier were committed, pushed, and read back from the
public branch before execution. The local formal leg below invoked the pinned
verifier exactly once from the repository root on a clean worktree. The
pull-request architecture gate has since passed: the required GitHub Linux
x86_64 and aarch64 jobs both reproduced `EXPECTED.txt` byte for byte from the
same verifier hash, and their aggregate `check` job succeeded.

pin_commit: ac496a684d715cbfca69b199abfb19dcc8000c20
base_commit: 11a059cc1578f2d48037b523c670196a49ae8f40
prereg_sha256: 1e566e8df11645395db00c8eec556a24547c9bf6303dc8594e37bca5de918196
prereg_bytes: 17477
prereg_git_blob: 412b7734d66ca4cba20bc57ceca42bddb0e19dc1
verifier_sha256: 37347d200eba27b2aa94da3e79c3705aa1e8e4d8cc6136c6347d32cd7b6306a9
verifier_bytes: 16104
verifier_git_blob: 55624873fbbc5844e7ff34cf784c3ffa0fb6bee8
command: python3 probes/P-LAMBDA-COCYCLE-ANGLES-2/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04
architecture: x86_64
python: CPython major 3 minor 11 patch 15
compatibility_basis: standard-library CPython with a portable process environment and no system-dependent verifier operations
run_started_utc: 2026-08-06T15:29:20Z
run_finished_utc: 2026-08-06T15:29:21Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 7c5b661401dc245e9469e9cc7b6e9129f4a773b44226410ff557770d35727eeb
stdout_bytes: 2234
stdout_lines: 34
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 97f199bd4c471f13587981c641816e14b3d43928
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 33/33 ALL PASS
github_platform: Ubuntu 24.04
github_architecture: aarch64
github_python: CPython major 3 minor 12 patch 13
github_verifier_sha256: 37347d200eba27b2aa94da3e79c3705aa1e8e4d8cc6136c6347d32cd7b6306a9
github_stdout_sha256: 7c5b661401dc245e9469e9cc7b6e9129f4a773b44226410ff557770d35727eeb
github_exit_code: 0
github_stderr_bytes: 0
github_status: PASS
github_verdict: VERIFY PASS
github_byte_identity: PASS
architecture_gate: PASS
pull_request: 288
workflow_run: 31116267757
tested_head: ba474e6ce6b1bd39a59f363f2a55ee36637e926a
github_aarch64_job: 92666497935
github_x86_64_job: 92666498002
github_check_job: 92666742977
public_lock: issue 287

## Integrity notes

`EXPECTED.txt` is the exact raw standard output from the one formal local
execution. It is LF-only, contains all 34 lines, ends in LF, and has the hash
and byte count recorded above. Standard error is the exact empty byte string.

The remote readback preceding execution compared the two pinned blobs as stored
by the remote against the local worktree. Both agreed at

```text
remote pin commit = ac496a684d715cbfca69b199abfb19dcc8000c20
PREREG.md  remote sha256 1e566e8df11645395db00c8eec556a24547c9bf6303dc8594e37bca5de918196
verify.py  remote sha256 37347d200eba27b2aa94da3e79c3705aa1e8e4d8cc6136c6347d32cd7b6306a9
```

The verifier forms no floating-point value, reads no external file, and imports
only `fractions`, `math.gcd`, `itertools` and `sys`. Before the pin it was
checked to produce byte identical standard output under
`LC_ALL=C TZ=UTC PYTHONHASHSEED=0` and under
`LC_ALL=cs_CZ.UTF-8 TZ=Asia/Tokyo PYTHONHASHSEED=1`, so the recorded bytes do
not depend on locale, timezone, or hash seed. That determinism check ran on a
development copy outside the repository; the pinned file's first execution is
the formal leg recorded above.

The local leg is Linux x86_64 on CPython 3.11.15. The recorded GitHub leg is
Linux aarch64 on CPython 3.12.13. The two legs differ in architecture and in
interpreter minor version and produced byte-identical standard output from the
same verifier hash, so the two-architecture computation gate rests on byte
identity against the one committed `EXPECTED.txt` and not on any platform
declaration. No conclusion relies on a machine name or on an
operating-system-specific operation.
