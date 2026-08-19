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
architecture_gate: PENDING
public_lock: issue 425
public_pin_comment: 5337851425
public_run_return: 5337865387

The single authorized formal execution used a fresh clean checkout of the
exact immutable pin on native Linux/aarch64, from the repository root, after
the public commit, preregistration, and verifier had been read back by
SHA-256, byte count, and Git blob identity. The verifier exited zero, wrote
no stderr, and produced the exact 4431-byte stdout stream recorded in
`EXPECTED.txt`. The raw stdout and neutral run metadata were returned
publicly on issue #425 before these post-run records were created. No rerun
occurred. `EXPECTED.txt` was assembled from that public return and its
SHA-256, byte count, and line count agree with the returned values.

The two-architecture computation gate is pending the probe-only pull
request: its Linux/x86_64 and Linux/aarch64 jobs must rerun the identical
pinned verifier and reproduce `EXPECTED.txt` byte for byte, and the
aggregate check must pass. Their identifiers are to be appended to this
record after the replay.
