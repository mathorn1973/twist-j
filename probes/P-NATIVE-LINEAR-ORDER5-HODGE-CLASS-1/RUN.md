# RUN: P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1

pin_commit: 2f6a3d9bc30ab7e34b324bb82d136e011de3cfbd
verifier_sha256: b81b0236aa360a5f37d7891e314b4d4a3fdf0f6c9286c5dffe385677e770cff6
command: python3 probes/P-NATIVE-LINEAR-ORDER5-HODGE-CLASS-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 4189f62c33bbc83d82fe5db79713dc0d11c2d97382623650d5e2f3510bf7129a
stdout_bytes: 436
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first scientific execution followed the atomic public pin and exact Git
blob readback. The pinned verifier Git blob is
68da936dadd8b83451f336bf124c40ae94b49ee0 and its reconstructed bytes have
the recorded SHA-256. The repository-relative command was run with LC_ALL=C,
LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

EXPECTED.txt is the actual stdout. This is one local x86_64 lane only. Clean
GitHub x86_64/aarch64 replay and aggregate check remain required.
