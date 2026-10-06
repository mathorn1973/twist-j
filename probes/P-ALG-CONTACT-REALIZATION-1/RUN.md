# P-ALG-CONTACT-REALIZATION-1 — first formal local run

```text
pin_commit: 195befdae1abeb6cf3249d7baf2088cdd9921998
verifier_sha256: 115f6cae93934792a31178bd5b2ea630336ac7e43cf2abbeca8e2db0823222b0
command: python3 probes/P-ALG-CONTACT-REALIZATION-1/verify.py
platform: Ubuntu 22.04.5 LTS (Linux-compatible WSL)
architecture: x86_64
python: 3.12.15
exit_code: 0
stdout_sha256: 2ff8efcdaef8a54d3a8814a4109d94b991c38c05eae96c3ab358876e64b480ba
stdout_bytes: 4454
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Date: 2026-10-06. One first formal run after public pin and complete byte readback.
Working directory: repository root. Environment: LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0. Limit: 600 seconds.
Elapsed seconds: 20.689502625988098 (metadata, not a scientific threshold).
Interpreter build: main, Oct  3 2026 01:03:07.

stdout was captured as raw bytes and copied without newline or whitespace normalization.
stderr was empty. No verifier or scientific function was imported or run before pinning.

## Complete package custody

All files below were read back through the public GitHub file API at the immutable
pin and compared byte for byte with both the accepted local package and pinned Git blobs.
Their hashes were checked again immediately before execution.

| File | Bytes | SHA-256 |
|---|---:|---|
| ACCEPTANCE.md | 2583 | `aa6fc40c08f721696217b77394e7259d96a4f8c42ba8dbfab6c2db6190b420e8` |
| CHECK-MAP.md | 15164 | `acfa89f08cacd453d51c0fa0b3093735af93d72925a78800a244604b016650a2` |
| PACKAGE.json | 3472 | `b80584e6c7c40b59d0add2cde3e6cc31afe19a030d4d38530f6cc9bf573ff82d` |
| PREREG-DRAFT.md | 9809 | `fe924d5074700aeaabf427e3071844a65a407de37ed8e4335f115932a4eb587c` |
| PREREG.md | 3967 | `fed4f0bdd59e5a2854cdb1f0549260c20d180868d82f68913b6fac7985d0fd76` |
| PROOF-REVIEW.md | 19517 | `3e107db16981e844bba21c1950d2322c695a633a471f0fc141252d01a612d560` |
| README.md | 3053 | `901670f95cce8f0643ab15f1ebd575d9603adad0a1e345d8aa8bca4a65480551` |
| SOURCE_PROVENANCE.json | 1138 | `cad544df526a9fe52afd4fbc72ccdc09ee20cced054262619dcc46d9295ba442` |
| SPEC.md | 46719 | `bcf48fbece05e445a1e6d958b749dfc0ff4d0b6f05f702d699f08fb142bfa656` |
| STATIC-REVIEW.md | 2817 | `ed99f903f56b76aeceddfe4f6eb2eb9c0e39d46993cfea5cd8b10dc9e372c4fa` |
| compiler_identity_checks.py | 9777 | `54bb787eb9a222a5a7fe764863002b4490826c099ac3e599992a7d28ccbe04b7` |
| verify.py | 52887 | `115f6cae93934792a31178bd5b2ea630336ac7e43cf2abbeca8e2db0823222b0` |

## Evidence boundary

This local x86_64 result is the pinned limited audit only. Public two-architecture
acceptance requires both x86_64 and aarch64 jobs and aggregate check on one PR head.
The workflow compares the same committed EXPECTED.txt against both executions.
Written-proof adoption is recorded separately in ACCEPTANCE.md and PROOF-REVIEW.md.
No Canon or owner status is changed by this run record.
