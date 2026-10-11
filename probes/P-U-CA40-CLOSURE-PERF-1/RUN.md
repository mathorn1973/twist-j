# First exact supporting run

PUBLIC NON-CANONICAL. L1 computational supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

```text
pin_commit: a7f88f96b7e1d8c20ad78f4079264055120ff87a
command: python3 probes/P-U-CA40-CLOSURE-PERF-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
prereg_sha256: fb9c7d7dfba8b3617d24b9d636115ed1d337c3eefb86be54e59eabc54af800b0
verifier_sha256: 87c8ecc39178d11df9de6c71d3cdf35121bda63d068958783d2f248330014014
public_source_readback_utc: 2026-10-11T13:02:58.390843+00:00
started_utc: 2026-10-11T13:04:12.949226+00:00
ended_utc: 2026-10-11T13:04:13.965754+00:00
wall_seconds: 1.0165355056524277
exit_code: 0
stdout_bytes: 521
stdout_lines: 1
stdout_sha256: 7a7f49cf9df0e482f116f0b5c70d1f6079535a9d18c27f49b1955786ae54db79
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

All fourteen source files were publicly compared byte for byte before this
first execution. EXPECTED.txt contains its actual ASCII/LF stdout.
Environment overrides were PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
LC_ALL=C, LANG=C and TZ=UTC.

The finite rational support, layout, ownership and Horner fixtures passed.
This small standard-library run does not execute C++, prove IEEE trace
equivalence, measure speed or certify a trajectory. Actual prefix outcomes
and their separate custody account belong to PERFORMANCE.md. Cross-
architecture CI replays this exact verifier, not the numerical panel.
