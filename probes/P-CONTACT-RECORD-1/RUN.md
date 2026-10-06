# P-CONTACT-RECORD-1 — first formal local run

```text
pin_commit: 3fe0d2d39e42965d8aab58b27212211f3445e729
verifier_sha256: 99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134
command: python3 probes/P-CONTACT-RECORD-1/verify.py
platform: Ubuntu 22.04.5 LTS (Linux-compatible WSL)
architecture: x86_64
python: 3.12.15
exit_code: 0
stdout_sha256: a003c89fa6776a4679e0c81e3ffeed0b65cc96186480b6b7d7ddb104cae234d4
stdout_bytes: 815
stdout_lines: 6
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Date: 2026-10-06. One first formal run after public pin and complete byte readback.
Working directory: repository root. Environment: LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0. Limit: 600 seconds.
Elapsed seconds: 0.3997886089782696 (metadata, not a scientific threshold).
Interpreter build: main, Oct  3 2026 01:03:07.

stdout was captured as raw bytes and copied without newline or whitespace normalization.
stderr was empty. No verifier or scientific function was imported or run before pinning.

## Complete package custody

All files below were read back through the public GitHub file API at the immutable
pin and compared byte for byte with both the accepted local package and pinned Git blobs.
Their hashes were checked again immediately before execution.

| File | Bytes | SHA-256 |
|---|---:|---|
| PROOF.md | 13626 | `805137842d66894b36cc5cef17b45bf1c67b81570bf9eb8a4c77c9394d40abf5` |
| PREREG.md | 7910 | `24a24ee5b055fec4b6a1cd6ebb5b4a3ffcec2e0e078b5f5937111e8a253ba4cd` |
| README.md | 3443 | `c9006df8528dae2655bb8a7378b504d2855283f5d8a5a37eed8f81de4b7174f0` |
| SOURCES.json | 4795 | `9943a1d831cc3ccbea1dc520071f8ff1b3a1d88bd4edf27e2cc47ea344fc6929` |
| verify.py | 17430 | `99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134` |
| ACCEPTANCE.md | 2710 | `390286e58c69245123ff26e501e33cf198d1873025bba42f587f412238c3c7f8` |
| PROOF-REVIEW.md | 13220 | `0bf0d40e7351da7a3657a8c0960ca5715ed487be52d378718eb7c5b785b30812` |
| PACKAGE.json | 2278 | `b74afa05ffd792c8a77b3af9db8dc81bc868d16ac135785d0aed0dc606409f46` |

## Evidence boundary

This local x86_64 result is the pinned limited audit only. Public two-architecture
acceptance requires both x86_64 and aarch64 jobs and aggregate check on one PR head.
The workflow compares the same committed EXPECTED.txt against both executions.
Written-proof adoption is recorded separately in ACCEPTANCE.md and PROOF-REVIEW.md.
No Canon or owner status is changed by this run record.

The launcher preflight encountered a local Git alternate-object path warning at the
Windows/Linux boundary. It occurred outside the candidate process; candidate exit
was zero and its captured stderr was empty. The local checkout was subsequently
made self-contained without modifying any pinned content or rerunning the candidate.
