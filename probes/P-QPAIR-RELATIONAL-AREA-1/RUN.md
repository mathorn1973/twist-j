# P-QPAIR-RELATIONAL-AREA-1 formal run record

pin_commit: a7564e7f47ee4d7ff39b952554f5af3bf673bf22
base_commit: 91e11e4f4db01d1badeabfea0a361972a6d4f2ea
branch: probe/P-QPAIR-RELATIONAL-AREA-1
prereg_sha256: ca2c2ac707b900ace4b1b9e06d44a7fa2e760eeab720c04445ea1c0f8a04cfea
prereg_bytes: 25543
prereg_git_blob: 59e83787d421db50384c6fc5e4c9374e09f0de75
verifier_sha256: 2b26d98781cd8e49118981ba6a1046ebc7c37e818f886adcd72a69a2abb340b2
verifier_bytes: 24364
verifier_git_blob: 90dafe3486a3608e2da86460b210897be7cd0475
command: python3 probes/P-QPAIR-RELATIONAL-AREA-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Linux
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-08-19T05:18:32Z
run_finished_utc: 2026-08-19T05:18:32Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: cf07f330d7f39d2487171f59dd260b5dcbf8934d92f67f9858d2b1d06040f7fa
stdout_bytes: 4526
stdout_lines: 72
stdout_lf: 72
stdout_cr_bytes: 0
stdout_nul_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
stderr_lf: 0
stderr_cr_bytes: 0
stderr_nul_bytes: 0
stderr_final_byte: EMPTY
run_integrity: PASS
result: PASS
architecture_gate: PASS
public_lock: issue 424
public_pin_comment: 5337851333
public_run_return: 5337865246
public_pull_request: 426
x86_public_return: 32219985004
x86_workflow_run: 32219985004
x86_workflow_job: 95968516655
x86_tested_merge_commit: c2ec4c00754fdbdd237b1c51f3e40acdf8a40a0b
x86_head_commit: e555ec56a4032b57135e84f1ca099bfae8c8689c
x86_base_commit: 91e11e4f4db01d1badeabfea0a361972a6d4f2ea
x86_platform: Ubuntu 24.04.4 LTS
x86_runner_image: ubuntu-24.04 20260810.271.1
x86_runner: 2.336.0
x86_python: CPython 3.12.13
x86_architecture: x86_64
x86_exit_code: 0
x86_stderr_bytes: 0
x86_verifier_sha256: 2b26d98781cd8e49118981ba6a1046ebc7c37e818f886adcd72a69a2abb340b2
x86_stdout_sha256: cf07f330d7f39d2487171f59dd260b5dcbf8934d92f67f9858d2b1d06040f7fa
x86_byte_identity: PASS
aarch64_replay_workflow_job: 95968516518
aarch64_replay_runner_image: ubuntu-24.04-arm 20260810.90.1
aarch64_replay_python: CPython 3.12.13
aarch64_replay_byte_identity: PASS
aggregate_check_job: 95968564806

The single authorized formal execution used a fresh clean checkout of the
exact immutable pin on native Linux/aarch64, from the repository root, after
the public commit, preregistration, and verifier had been read back by
SHA-256, byte count, and Git blob identity. The verifier exited zero, wrote
no stderr, and produced the exact 4526-byte stdout stream recorded in
`EXPECTED.txt`. The raw stdout and neutral run metadata were returned
publicly on issue #424 before these post-run records were created. No rerun
occurred. `EXPECTED.txt` was assembled from that public return and its
SHA-256, byte count, and line count agree with the returned values.

The first clean GitHub Linux/x86_64 pull-request replay (pull request
#426) used the identical pinned verifier at tested merge commit
c2ec4c00754fdbdd237b1c51f3e40acdf8a40a0b. Workflow run 32219985004, job
95968516655, exited zero with empty stderr and reproduced `EXPECTED.txt`
byte for byte (`VERIFY PASS` with the pinned verifier SHA-256 and the
recorded stdout SHA-256). The parallel GitHub Linux/aarch64 job 95968516518
also replayed byte for byte, and the aggregate check job 95968564806
passed. Together with the sole formal aarch64 execution, the required
two-architecture computation gate is PASS.
