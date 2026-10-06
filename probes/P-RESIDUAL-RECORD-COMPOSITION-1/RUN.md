# P-RESIDUAL-RECORD-COMPOSITION-1 — first formal local run

```text
pin_commit: a784b37e90caf65144258d3d637044c1e63e4a2d
verifier_sha256: bf693e33d5652141bf2367c6892e9c54d76a2f3a383aee19849747d1f17bae9f
command: python3 probes/P-RESIDUAL-RECORD-COMPOSITION-1/verify.py
platform: Ubuntu 22.04.5 LTS (Linux-compatible WSL)
architecture: x86_64
python: 3.12.15
exit_code: 0
stdout_sha256: c980b279e559aa9a4c2f538d9d4c4f0a4e33700860e37a08e9679390a3052b74
stdout_bytes: 1047
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Date: 2026-10-06. One first formal run after public pin and complete byte readback.
Working directory: repository root. Environment: LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0. Limit: 600 seconds.
Elapsed seconds: 0.256170397013193 (metadata, not a scientific threshold).
Interpreter build: main, Oct  3 2026 01:03:07.

stdout was captured as raw bytes and copied without newline or whitespace normalization.
stderr was empty. No verifier or scientific function was imported or run before pinning.

## Complete package custody

All files below were read back through the public GitHub file API at the immutable
pin and compared byte for byte with both the accepted local package and pinned Git blobs.
Their hashes were checked again immediately before execution.

| File | Bytes | SHA-256 |
|---|---:|---|
| ACCEPTANCE.md | 3095 | `eb9a89ac1d856adf1a75f44861ca3c6116532a026142fb9cda9ffc14453c9488` |
| CHECK-MAP.md | 11306 | `e2165d2158f08f8a48bfea63f30113ffb09672c4b6612fa0dec78e801bc49f55` |
| DEPENDENCIES.json | 2142 | `1cce7f893e52504995fa49bf732ec312ebea007e7bf3120f8cd4870883ed00df` |
| PACKAGE.json | 4360 | `47e6f0d32ac666737b0962f221f5c75ffe100e9794cdb81ff2f51fd4a78b0108` |
| PREREG-DRAFT.md | 3389 | `021a18883fa4c1dc0918f723aa7debc5d1c410ad42bb4c3a4f9893f8aa374515` |
| PREREG.md | 4268 | `42ee37c2b33151219b827b133bc1a7542ad5f52c678ead4b608c32c3d46f8d3d` |
| PROOF-REVIEW.md | 14810 | `c1f435f0bf7690ce3cb84e8d3f89a8da150065abd5e1546886f7f3352e473876` |
| PROOF.md | 10749 | `7736730cc186669859f0d714e2790fea8a461129c7fbaf922a024eb90149273a` |
| PUBLIC-DEPENDENCIES.json | 7594 | `4e1bd30830e54456ec2c64ac32fdcee838951ac091deaa8821c584b38470b051` |
| README.md | 5555 | `5a57a1c8d5746f52f48736b6f1aadba4e64cbafc091872d1c046c84b7920356b` |
| STATIC-REVIEW.md | 7859 | `4e2ce0bba0f027c4cccd9108c74fd72b38d690548ae2a9568393876a2828bdd3` |
| VERIFIER-PINS.json | 1555 | `97e01da313579d388958b2f60751d5e717f45182b66155afffcb3cbba8a628ba` |
| algebra_dependency.py | 52887 | `115f6cae93934792a31178bd5b2ea630336ac7e43cf2abbeca8e2db0823222b0` |
| contact_dependency.py | 17430 | `99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134` |
| verify.py | 22825 | `bf693e33d5652141bf2367c6892e9c54d76a2f3a383aee19849747d1f17bae9f` |

## Evidence boundary

This local x86_64 result is the pinned limited audit only. Public two-architecture
acceptance requires both x86_64 and aarch64 jobs and aggregate check on one PR head.
The workflow compares the same committed EXPECTED.txt against both executions.
Written-proof adoption is recorded separately in ACCEPTANCE.md and PROOF-REVIEW.md.
No Canon or owner status is changed by this run record.
