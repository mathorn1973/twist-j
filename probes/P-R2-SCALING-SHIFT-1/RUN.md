# P-R2-SCALING-SHIFT-1 formal run record

pin_commit: 3c5d2e6e778aab8e2c3d29f09df4e2c7532de12a
prereg_sha256: 3196030ef2deace237d081f4174a206ff3f18102aa4b2c4124f49d33c5d8c7df
verifier_sha256: e8519402773cc0d94425eb9d4afa6d7f260c3c770c5d142bfbb5c13e44ff3894
command: python3 probes/P-R2-SCALING-SHIFT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
architecture_gate: local aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 3
deterministic_stdout: byte-identical
exit_code: 0
stdout_sha256: 4f50c87d24d0705d843dfe431d43fa472ba46ecf7f28ad7471711f62a113180f
stdout_bytes: 1832
stdout_lines: 22
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: ALL PASS (13 gates)
public_lock: issue 59
