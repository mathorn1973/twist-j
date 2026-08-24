# P-PISTON-RELATIONAL-WEDGE-1 formal run record

pin_commit: 348c3c3ea65b0dbc79052a70482eba690e82b145
base_commit: 91e11e4f4db01d1badeabfea0a361972a6d4f2ea
branch: probe/P-PISTON-RELATIONAL-WEDGE-1
prereg_sha256: 2467e6847229ca829989e6929342d0f0200249b064245d880f8beb1ad6c28001
prereg_bytes: 29137
prereg_git_blob: 6abf543688386b21384faace275bd5c41a25804c
verifier_sha256: 74940cbf4482abb7541fafc1b1e2262410533472a81dc0e07672bfb91bae52b4
verifier_bytes: 18812
verifier_git_blob: 4689971b5d208233ee245222dda92b62eded6ede
command: python3 probes/P-PISTON-RELATIONAL-WEDGE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Linux
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-08-19T05:18:48Z
run_finished_utc: 2026-08-19T05:18:48Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: c41fe236222402f35d678316e3180b651a8c51da600135bc3dda78071e4337b0
stdout_bytes: 4431
stdout_lines: 71
stdout_lf: 71
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
public_lock: issue 425
public_pin_comment: 5337851425
public_run_return: 5337865387
public_pull_request: 427
x86_public_return: 32219987568
x86_workflow_run: 32219987568
x86_workflow_job: 95968523697
x86_tested_merge_commit: 98e26368c5325a9f8add1ad4d8f1bc8ed532d590
x86_head_commit: 2bb3e0c8bb5de9ebcfaf6ba567e20c76be5376fc
x86_base_commit: 91e11e4f4db01d1badeabfea0a361972a6d4f2ea
x86_platform: Ubuntu 24.04.4 LTS
x86_runner_image: ubuntu-24.04 20260810.271.1
x86_runner: 2.336.0
x86_python: CPython 3.12.13
x86_architecture: x86_64
x86_exit_code: 0
x86_stderr_bytes: 0
x86_verifier_sha256: 74940cbf4482abb7541fafc1b1e2262410533472a81dc0e07672bfb91bae52b4
x86_stdout_sha256: c41fe236222402f35d678316e3180b651a8c51da600135bc3dda78071e4337b0
x86_byte_identity: PASS
aarch64_replay_workflow_job: 95968523721
aarch64_replay_runner_image: ubuntu-24.04-arm 20260810.90.1
aarch64_replay_python: CPython 3.12.13
aarch64_replay_byte_identity: PASS
aggregate_check_job: 95968573327

The single authorized formal execution used a fresh clean checkout of the
exact immutable pin on native Linux/aarch64, from the repository root, after
the public commit, preregistration, and verifier had been read back by
SHA-256, byte count, and Git blob identity. The verifier exited zero, wrote
no stderr, and produced the exact 4431-byte stdout stream recorded in
`EXPECTED.txt`. The raw stdout and neutral run metadata were returned
publicly on issue #425 before these post-run records were created. No rerun
occurred. `EXPECTED.txt` was assembled from that public return and its
SHA-256, byte count, and line count agree with the returned values.

The first clean GitHub Linux/x86_64 pull-request replay (pull request
#427) used the identical pinned verifier at tested merge commit
98e26368c5325a9f8add1ad4d8f1bc8ed532d590. Workflow run 32219987568, job
95968523697, exited zero with empty stderr and reproduced `EXPECTED.txt`
byte for byte (`VERIFY PASS` with the pinned verifier SHA-256 and the
recorded stdout SHA-256). The parallel GitHub Linux/aarch64 job 95968523721
also replayed byte for byte, and the aggregate check job 95968573327
passed. Together with the sole formal aarch64 execution, the required
two-architecture computation gate is PASS.
