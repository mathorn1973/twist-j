# RUN: P-U-COUNTER-AMPLITUDE-CLASS-1

pin_commit: e38ee8049797a9ae60935753eb2c68e5a53f2492
verifier_sha256: d811afdd74cc11891282d93bf4575e7fc087a2ee209d74729e4ba1e3feb0e703
command: python3 probes/P-U-COUNTER-AMPLITUDE-CLASS-1/verify.py
exit_code: 0
stdout_sha256: f6495cdbf148175e762ab7d0fb628b303d93ecda3130c06c3f94bd3df0a8b2cb
stdout_bytes: 1155
stdout_lines: 18
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14

prereg_sha256: d69d98c58d417ca3f760394ab639096076863a3be1b3335d515539b570297de3
proof_sha256: e2e2e42dcb66d007d2f7eeb52178cff50eb4000c3a350e0368b54759bec32725

The first execution followed byte-identical public readback of all four
pinned files. The repository-relative command ran with LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

This record describes the local x86_64 execution. Later public verifier
acceptance is recorded separately in ACCEPTANCE.md, with exact tested
head and job URLs; this local record is not rewritten as a CI run.
