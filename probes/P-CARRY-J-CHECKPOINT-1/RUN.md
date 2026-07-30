# P-CARRY-J-CHECKPOINT-1 formal run record

pin_commit: 55f678d721a13f3168f0a5175be65b9f8101a64f
base_commit: 3d8c6307f20d01ad50fc90ae1c5777926b884881
prereg_sha256: b946d9808ced64f3ecae68fe0bea5df03a07ea1956bd850b68d5dd105c416163
verifier_sha256: 406004360a511512f3c3c44351f25df64df115aa6f35dbd1c0ac16f4587b20c2
command: python3 probes/P-CARRY-J-CHECKPOINT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 87584b6afc5b77a3d8b1cc7957197431227fbdd77cf447da3ea92289fa1e668a
stdout_bytes: 394
stdout_lines: 6
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 5/5 ALL PASS
public_lock: issue 81

The formal run used a clean detached checkout of the exact public pin commit.
The checkout and the separate raw stdout and stderr files are retained for
audit. The machine is recorded only by neutral platform and architecture
descriptors.
