# P-C20-TEICHMULLER-SPLIT-2 formal run record

pin_commit: 338a90c6b82a8934a0f7f28090dee51bce6c791c
base_commit: 633940a0187f7bdac83eae5639844622ad955d9f
prereg_sha256: b5054f27c7c018f0f8b305b9d26c8f64e34f528e8729eb48d1b8ebfade28733c
prereg_bytes: 12386
prereg_git_blob: 970a999e84a704dc2ea1c0b2258c5fe4809c28d0
verifier_sha256: 5ba3680f2cca840ab458e72e8a2f0febb99c732fcacaeadd68c71c020baacd41
verifier_bytes: 9079
verifier_git_blob: fa1ad3436dbadcc181c9351a5fb9da64b994c002
command: python3 probes/P-C20-TEICHMULLER-SPLIT-2/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_at: 2026-07-23T05:27:59Z
run_finished_at: 2026-07-23T05:33:23Z
pre_run_clean: yes
post_run_clean: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 4cbf934b2220c5a5c3de8169a448baac1396236ebc37c286536c3886bb8d86e8
stdout_bytes: 724
stdout_lines: 7
stdout_cr_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
public_lock: issue 126
public_run_return: issue comment 5054847202

The formal run used a fresh fetch and a clean detached checkout of the exact
public pin commit. The public branch tip, both frozen file hashes, byte counts,
and Git blobs matched the pin before execution. Raw stdout and stderr were
captured separately outside the worktree. The machine is recorded only by
neutral platform and architecture descriptors.
