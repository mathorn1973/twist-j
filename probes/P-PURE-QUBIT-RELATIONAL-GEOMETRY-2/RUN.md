# P-PURE-QUBIT-RELATIONAL-GEOMETRY-2 formal run record

pin_commit: d6d373a095a6f6d8053f35046ef9a1c45a63ce8a
base_commit: e1fc4677d72eaef5851b103d1fbcbf95cf4dd38f
branch: probe/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2
prereg_sha256: 82b7f7d940ab3b95683f9148086afed7ccfc7f591de34a98206b1ba587129dbf
prereg_bytes: 17775
prereg_git_blob: 8b7df8674091ac349c9c76c34d59af8499d170a7
verifier_sha256: 2405a218512813fa041334562be83e655d95a9cc1622892027686bb965c94a77
verifier_bytes: 10239
verifier_git_blob: 500650bf73695c139f0b516f54687bc625302785
command: python3 probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04
architecture: x86_64
python: CPython 3.12.13
run_started_utc: 2026-08-19T07:13:01Z
run_finished_utc: 2026-08-19T07:13:07Z
remote_readback: PASS
deterministic_executions: 1
exit_code: 0
stdout_sha256: 1c1c60dbca25469e55081841f7c73b636516df1888602344515c7e21b8936676
stdout_bytes: 1539
stdout_lines: 25
stdout_lf: 25
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
public_lock: issue 430
public_pin_comment: 5338770133
public_run_return: 5338770284
public_pull_request: 431
github_workflow_run: 32226965301
github_workflow_job: 95988501590
github_tested_merge_commit: 0d85c8b8bb67e9b9a276d42d74c5d0d72e994f8d
github_head_commit: 7494576c78ae9424e5980b36b8b4d378303856bf
github_base_commit: e1fc4677d72eaef5851b103d1fbcbf95cf4dd38f
github_platform: Ubuntu 24.04.4 LTS
github_runner_image: ubuntu-24.04-arm 20260810.90.1
github_runner: 2.336.0
github_python: CPython 3.12.13
github_architecture: aarch64
github_exit_code: 0
github_stderr_bytes: 0
github_verifier_sha256: 2405a218512813fa041334562be83e655d95a9cc1622892027686bb965c94a77
github_stdout_sha256: 1c1c60dbca25469e55081841f7c73b636516df1888602344515c7e21b8936676
github_byte_identity: PASS
x86_replay_workflow_job: 95988501973
x86_replay_runner_image: ubuntu-24.04 20260816.277.1
x86_replay_python: CPython 3.12.14
x86_replay_byte_identity: PASS
aggregate_check_job: 95988607069

The single authorized formal execution used the exact verifier whose public
remote bytes, SHA-256, byte count and Git blob identity were read back at the
immutable pin before execution. The verifier exited zero, wrote no stderr and
produced the exact 1,539-byte stream in `EXPECTED.txt`. All 17 gates passed.
No rerun occurred.

The written proofs in `PREREG.md` carry the universal statements. The exact
finite audit covered 2,401 Gaussian-rational `2 x 2` matrices and 69,888
Gaussian-rational two-row matrices for `n=2,3,4`.

The first clean pull-request replay at tested merge commit
`0d85c8b8bb67e9b9a276d42d74c5d0d72e994f8d` reproduced the exact pinned
verifier and expected stdout on native Linux/aarch64, workflow run
`32226965301`, job `95988501590`. The parallel Linux/x86_64 job
`95988501973` reproduced the same bytes, and aggregate job `95988607069`
passed. The local x86_64 formal leg and required aarch64 GitHub leg differ in
architecture and are byte-identical; the workflow independently passed both
required architectures. The two-architecture gate is PASS.
