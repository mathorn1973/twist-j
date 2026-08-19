# P-DQRC-ARITHMETIC-RECONSTRUCTION-1 formal run record

pin_commit: b0f7c660447b01d6dbc23ffedb80390f2b566b5d
base_commit: 278d253f2d72f5e0bce95b380792ea3912a6420a
branch: probe/P-DQRC-ARITHMETIC-RECONSTRUCTION-1
prereg_sha256: d06fcd5779a8c201fffc5d3c61bfd16892ad477130db55b160fe2bf824f4f881
prereg_bytes: 26324
prereg_git_blob: a73d47e9fc7b36ae4fb849302a6dbd48efd1662b
verifier_sha256: 2af01ac1bdc4692226e6eda913f5551c63efeee0a26229c1a059f61082a5cf53
verifier_bytes: 12804
verifier_git_blob: 24f32e3632b4e64a55771eccdf5aa419a609f3b9
command: python3 probes/P-DQRC-ARITHMETIC-RECONSTRUCTION-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.13
run_started_utc: 2026-08-19T11:35:13Z
run_finished_utc: 2026-08-19T11:35:13Z
remote_readback: PASS
deterministic_executions: 1
exit_code: 0
stdout_sha256: 7a776facd047c039b8b8f75ab627d93d75341d6da30eee7b2c76eb7cc6e4a94e
stdout_bytes: 1032
stdout_lines: 17
stdout_lf: 17
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
public_lock: issue 436
public_pin_comment: 5341552325
public_run_return: 5341562720
public_pull_request: PENDING
github_workflow_run: PENDING

The single authorized formal execution used the exact verifier whose public
remote bytes, SHA-256, byte count, and Git blob identity were read back at the
immutable pin before execution. It exited zero, wrote no stderr, and produced
the exact 1,032-byte stream in `EXPECTED.txt`. All 15 exact audit groups
passed. No rerun occurred.

The self-contained proofs in `PREREG.md` carry the universal statements. The
finite boxes are coordinate and boundary audits only. No physical apparatus,
event stream, causal law, probability ontology, or external dataset was used.
The required native aarch64 and independent workflow x86_64 replays remain
pending.
