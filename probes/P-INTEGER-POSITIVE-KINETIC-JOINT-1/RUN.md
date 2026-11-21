# First local formal run

pin_commit: bd7e1dada3a4869ecfae76c0aea03c0a88c9983f
command: python3 probes/P-INTEGER-POSITIVE-KINETIC-JOINT-1/verify.py
verifier_sha256: 7fdea52ae7f106f45104bb7d7a7e9f7d13f36c8a1f9e14cc028ed5f634fbfd3b
platform: Windows-11-10.0.26300-SP0
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 5b050c5aab38db6bb8865fe00ca5b023a1a73f36b25c9ba3d37c863f3ac8ff0a
stdout_bytes: 720
stdout_lines: 25
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T14:21:50Z
completed_utc: 2026-10-19T14:21:53Z
prereg_sha256: 343340814f65850c2a745746039c9db599c4f325c0afb4aed7611e2800d532a6
proof_sha256: ccb097fa59811f0ba66026437800bd0a4b2de9cf1e80a377ed05d40d9ab3d1c8
source_sha256: c5bc54ad9500131f7cc3a82fd5623beca6b4f492e2780c23517d848e78dc10cb
breaker_sha256: 071bd62a5ef52a03f413ff6069fc0e3f468615dfde73ca09d4cdd9add2009ec9
frozen_manifest_sha256: f2aec854e2acfe227f00ed2bb58fe25840dd34aa812002da5c37ea2ec7593393

## Execution custody

This was the first scientific execution of either pinned implementation.
All six frozen files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`,
`breaker.py`, `FROZEN.sha256`) were committed and pushed to GitHub at
`bd7e1dada3a4869ecfae76c0aea03c0a88c9983f`, read back remotely via the
GitHub API with byte-for-byte agreement, and recorded in the prospective
pin receipt on ownership issue #1647 before any execution or import:
https://github.com/mathorn1973/twist-j/issues/1647#issuecomment-6269491226.

Environment: `LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONHASHSEED=0`, `TZ=UTC`. The primary (`verify.py`) launched
`breaker.py` with the same Python executable and `-I` in a separate
process. The child completed with exit code `0`, empty stderr, and
exactly the same 23-line (680-byte, SHA-256
`3accd1e0633cb07e10410bb6df112d4712b789c6bd50dc62226ae7674667d334`)
certificate bytes as the primary, including every LF. The primary
appended `BREAKER_RAW_BYTES=IDENTICAL` and `RESULT=PASS` to form the
720-byte `EXPECTED.txt`.

## Required architecture gate

This record states the observed first local run (`x86_64`) only. The
draft PR's unchanged `.github/workflows/policy.yml` workflow must replay
the exact verifier and breaker on both `x86_64` (`ubuntu-latest`) and
`aarch64` (`ubuntu-24.04-arm`) with Python 3.12 and compare to the same
720-byte `EXPECTED.txt`.
