# First formal local run

pin_commit: 01781f62472969cd08428e5368f93b8761c20faa
prereg_sha256: fb12b0848286f9e4de6b54d4f8bcc1fc91f82e7d39aaa86dc988d7a850a9736c
verifier_sha256: 02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9
command: python3 probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 3b73db632d37eb54c4fee2053eea87072addcfe2e2972905457851fc814aecea
stdout_bytes: 288
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The pinned verifier bytes were reconstructed from the public GitHub readback
and independently hashed before execution; their SHA-256 equals the public
record above. The local x86_64 run is one lane only. Required clean GitHub
x86_64 and aarch64 jobs must replay the unchanged verifier against the same
EXPECTED.txt before computation-grade acceptance.
