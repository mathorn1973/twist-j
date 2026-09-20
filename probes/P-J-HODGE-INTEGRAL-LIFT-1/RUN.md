# RUN: P-J-HODGE-INTEGRAL-LIFT-1

pin_commit: 56f1d28bd7c4a180f68d5a6f7fce59f5cd7447cf
verifier_sha256: 23316c905b944762a56c4804e172aac860e17289187554de197f50f4b7fe7bf8
command: python3 probes/P-J-HODGE-INTEGRAL-LIFT-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: c8580491eda301ebdc698f112f0a4e8c5fb46cc1aa88d90eec698b8237d953a8
stdout_bytes: 364
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 7e023460c0d02ba6858d422c7308bdffad392e1af6f22d9fa974822131fdae5a
proof_sha256: d475f2b5504cb85a50209c00d2c1b0cf83f15fa63efafe153870d87d583fa5ff

The first scientific execution followed public readback of the atomic three-file
pin. The pinned verifier Git blob a74687e02d05f3f3954dfe27e6508a5604302f42
was reconstructed byte-for-byte before execution; its computed SHA-256 is the
recorded verifier_sha256.

The repository-relative command was run with LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. EXPECTED.txt contains
the actual stdout. This is one x86_64 local lane only. Required clean GitHub
x86_64/aarch64 replay and aggregate check remain the public computation gate.
