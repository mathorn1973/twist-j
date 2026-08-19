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
architecture_gate: PENDING
public_lock: issue 430
public_pin_comment: 5338770133
public_run_return: 5338770284

The single authorized formal execution used the exact verifier whose public
remote bytes, SHA-256, byte count and Git blob identity were read back at the
immutable pin before execution. The verifier exited zero, wrote no stderr and
produced the exact 1,539-byte stream in `EXPECTED.txt`. All 17 gates passed.
No rerun occurred.

The written proofs in `PREREG.md` carry the universal statements. The exact
finite audit covered 2,401 Gaussian-rational `2 x 2` matrices and 69,888
Gaussian-rational two-row matrices for `n=2,3,4`. Public x86_64 and aarch64
pull-request replays are pending; until both reproduce these same bytes and
the aggregate `check` passes, the architecture gate remains PENDING.
