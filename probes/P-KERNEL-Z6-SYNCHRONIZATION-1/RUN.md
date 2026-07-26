# P-KERNEL-Z6-SYNCHRONIZATION-1 formal run record

pin_commit: c23ea20f9a4903acd4ca341ec857b29a635ae7ca
base_commit: 4ac41b4fac3a3794a6e9d5be1e2027d324edb806
branch: probe/P-KERNEL-Z6-SYNCHRONIZATION-1
prereg_sha256: e783a3a16891804f0c97b5b80744b0bb4ec5dcee1f8b2ae4f479283e2b48703a
prereg_bytes: 17085
prereg_git_blob: 1806259b009c2fc6ff12632c2197576758846872
verifier_sha256: a9c696dfa59562d29f3422ebe30979678c053d307229b7deecb8beb64b7c2e02
verifier_bytes: 35503
verifier_git_blob: 82ad39a4424c2732c54740eb7370afe0bd1ef00f
command: python3 probes/P-KERNEL-Z6-SYNCHRONIZATION-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Linux
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-07-26T11:40:16.949720999Z
run_finished_utc: 2026-07-26T11:40:20.606981579Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: b86fd3889abb668ebc235e045aeed928e791cd02ca14e4b92910b81c65959077
stdout_bytes: 1000
stdout_lines: 21
stdout_lf: 21
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
result: PROOF-SURVIVES
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
public_lock: issue 160
public_pin_comment: 5083156464
public_run_authorization: 5083158699
public_run_return: 5083313218

The single authorized formal execution used a fresh clean detached checkout
of the exact immutable pin on native Linux/aarch64. The public commit,
preregistration, and verifier were read back by SHA-256, byte count, Git blob
identity, and LF metadata before process start. `EXPECTED.txt` is the exact
1000-byte stdout stream from this execution. Stderr is the empty byte string.

The exact raw stdout and neutral run metadata were returned publicly on issue
#160 before these post-run records were created. No rerun occurred.

The required GitHub-hosted Linux/x86_64 reproduction of the byte-identical
pinned verifier remains pending.
