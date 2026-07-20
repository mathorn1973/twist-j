# P-SQRT-PHI-DIGIT-1 formal run record

pin_commit: 25821b83bf9763b07802526a3a3e3036a7a4cbb0
base_commit: 3d8c6307f20d01ad50fc90ae1c5777926b884881
prereg_sha256: b8f3e7769490da70b686f5de21769ccb29b79fca4304256dd477aff198eaeada
verifier_sha256: ad94fdff5cf0b7c8674d36b675f058f347287702c90428c19aa6b76e8e4a1cab
command: python3 probes/P-SQRT-PHI-DIGIT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 9a82917b6736026c3b4e0af9d401400be78be920582f6f8acdbffd87c2e4ddde
stdout_bytes: 606
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
public_lock: issue 87

The formal run used a clean detached checkout of the exact public pin commit.
The checkout and the separate raw stdout and stderr files are retained for
audit. The machine is recorded only by neutral platform and architecture
descriptors.
