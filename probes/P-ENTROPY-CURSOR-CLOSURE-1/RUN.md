# P-ENTROPY-CURSOR-CLOSURE-1 formal run record

pin_commit: 916eed58a37f0a4ce56ff093fc0dcb7e1d42d5ff
base_commit: a11ea993f2c120b6f5c8c896c1ce11a9d0740d44
prereg_sha256: d57fc9e12527aa98db4c270952add818a1f2e3b083c13155b5861d5c24b35f14
prereg_bytes: 14153
prereg_git_blob: b192e333ca28582a14e3cef4d88e3f50d1b70cb8
verifier_sha256: 6a41a8846a19b3e0e75cbf25a87c8825a13f369238732549a004a17687092e76
verifier_bytes: 26897
verifier_git_blob: af87636e85a20f403489661c7b9d7a2f33fdfd76
command: python3 probes/P-ENTROPY-CURSOR-CLOSURE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-25T16:25:55Z
run_finished_utc: 2026-07-25T16:26:41Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 21ca2301ffa17634eb868c154e7b683c0d2ca0bc54661962029b12a7a0e65ca7
stdout_bytes: 1474
stdout_lines: 19
stdout_cr_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: PASS / cursor axis closed through window 32
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
public_lock: issue 151
public_pin_comment: 5079250745
public_run_return: 5079260592

The formal execution used a fresh fetch and a clean detached checkout of the
exact immutable pin. The preregistration and verifier were read back by both
SHA-256 and Git blob identity before execution. `EXPECTED.txt` is the exact
stdout byte stream from this one formal aarch64 execution. The independent
GitHub-hosted x86_64 reproduction remains pending.
