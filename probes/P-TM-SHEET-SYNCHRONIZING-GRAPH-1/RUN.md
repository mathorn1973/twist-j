# P-TM-SHEET-SYNCHRONIZING-GRAPH-1 formal run record

pin_commit: 4d526476d33885224424a2bc68549ea48e877b0e
base_commit: cef0a08cec219a41333b36fbfe0a0e4dc780045f
branch: probe/P-TM-SHEET-SYNCHRONIZING-GRAPH-1
prereg_sha256: a66dbc167a90e89b315122137035076386751a857e06f194e5b6ab6388d41ce3
prereg_bytes: 9356
prereg_git_blob: c287274ec3824e587901dce8ad0af85c1e856c95
verifier_sha256: 4b1cf8b9c9b2ba8adb2d0a4f87be476d6f91493da24c572e14c8e4c4d4e3aae1
verifier_bytes: 11978
verifier_git_blob: 6881f460b846d515a50dfcf7c88f53adba9dea52
command: python3 probes/P-TM-SHEET-SYNCHRONIZING-GRAPH-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Linux
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-08-18T18:27:00.079671028Z
run_finished_utc: 2026-08-18T18:27:00.424628201Z
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 7d267d7a74bdd745b68443bd63514834700580525391b42436ff988f9031bafc
stdout_bytes: 1157
stdout_lines: 19
stdout_lf: 19
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
public_lock: issue 417
public_pin_comment: 5332360634
public_run_return: 5332376736

The single authorized formal execution used a fresh clean detached checkout
of the exact immutable pin on native Linux/aarch64. The public commit,
preregistration, and verifier were read back by SHA-256, byte count, and Git
blob identity before process start. EXPECTED.txt is the exact 1157-byte
stdout stream from this execution. Stderr is the empty byte string. The raw
stdout and neutral run metadata were returned publicly on issue #417 before
these post-run records were created. No rerun occurred. The pull-request
replay supplies the second architecture leg; its fields are appended to this
record when the replay lands.
