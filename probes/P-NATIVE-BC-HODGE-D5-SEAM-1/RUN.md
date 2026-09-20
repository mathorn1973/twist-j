# RUN: P-NATIVE-BC-HODGE-D5-SEAM-1

pin_commit: 594b14ba4d5a8aac54926344eb95de6b366cbadf
verifier_sha256: 2f0162073a5012ea18db9528c00996118e7215d34014264bfe8f094908fee85f
command: python3 probes/P-NATIVE-BC-HODGE-D5-SEAM-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 801b45c8b63515e27a9734952145e9d92ea583f6591c128a5f23979cbeb596b8
stdout_bytes: 639
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first scientific execution followed the atomic public pin and exact Git
blob readback. The pinned verifier Git blob is
9532ef7802b46f6807e5aabe41bf921997abb85c; its reconstructed bytes have the
recorded SHA-256. The repository-relative command was run with LC_ALL=C,
LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

EXPECTED.txt is the actual stdout. This is one local x86_64 lane. Clean
GitHub x86_64/aarch64 replay and aggregate check remain required.
