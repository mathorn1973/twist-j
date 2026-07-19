# P-METAL-TRACE-1 formal run record

pin_commit: 908a9b72cd72edd74209e5987a7abae8f0583668
prereg_sha256: 5d5dd5c7853c3ebd3c3ed09ceefcfae0cc1891a53713a595289e6d47559d2982
verifier_sha256: 57501a2975ff71a43a1e5f98e7f976e35d27dd6252143fb5d20ce715375fff2a
command: python3 probes/P-METAL-TRACE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04 LTS
architecture: x86_64
python: 3.11.15
exit_code: 0
stdout_sha256: 8f1567fd0d9f2ac766d8242821ec8bff6277a3c40fcd467a284662dd9de54d12
stdout_bytes: 1101
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: ALL OK, 19 checks
wall_seconds: 0.1
base_commit: 72a04e1e2dae8df66f170b169328611b75a8a1af
second_architecture: aarch64 local leg pending (appended to RESULT.md when
run, without changing any pinned file); the GitHub CI check reruns the
pinned verifier on x86_64, which is a same-architecture reproduction
cross_session: stdout sha256 equals the candidate session's pinned expected
output byte for byte (candidate leg was Python 3.12.3, this leg 3.11.15)
