# First local formal run

pin_commit: b3de2d7886a00bc7d6b2f5fe470516424be8b046
command: python3 probes/P-INTEGER-SOURCE-HOLONOMY-1/verify.py
verifier_sha256: 113b137043b15843e6d8c6d5f3a10c5bc40218d89f8d6cf7da219ae5346f2eda
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: c053b1840bf40ede47a7d03525d84ce3cd4a3a010190572a8f492bb2f3b3aaef
stdout_bytes: 930
stdout_lines: 16
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 75660464a3a8d437ab7a84f602da5b8bced2e2b1516e4567a4b7c451c57776de
breaker_sha256: 129e29f021f7b7e6733bbb131526ced9dd3dfb36f0d364d7a72e0636e5028e8c
frozen_manifest_sha256: 423ddd1eca3e51ab8801f62d9ec360c8d46219cb433075935d348387452e40ab

## Execution custody

This was the first scientific execution of either pinned implementation.
Before execution, the complete pin was public, every file was read back
and matched, the local checkout was clean at the exact pin, and all five
frozen file hashes passed. The entry point ran the independent breaker in
a separate Python process and required complete certificate equality.

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. The independent subprocess additionally uses
Python isolated mode. No scientific source or input was altered after pin.

EXPECTED.txt is the exact first completed stdout. No stderr artifact is
needed because stderr was empty. RESULT.md states the mathematical scope
and separates a passed audit from unearned native or physical claims.

## Required architecture evidence

The unchanged PR workflow must run this same verifier and independent
breaker on x86_64 and aarch64 and compare with this one EXPECTED.txt.
The public PR checks and the PR body carry the actual job/run identifiers
and exact stdout readback once available. This local record does not
assert that an unobserved remote run has already passed.
