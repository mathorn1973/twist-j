# First exact supporting run

PUBLIC NON-CANONICAL. L1 computational supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.

```text
pin_commit: 99625cf6039a4a17334664b00630857bdfa772c3
command: python3 probes/P-U-CA40-DP5-384-COMPARISON-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
prereg_sha256: 992462d2ab993d09f8ae04123ad70d3c7446ec7d9ebac65f6b16c88299a7990a
verifier_sha256: 1ef14a28f92624edb71e7c77b9c81ca6cbff3d3a86c46e6264cfa78b4e1ce7e8
public_source_readback_utc: 2026-10-12T07:07:46.644910+00:00
started_utc: 2026-10-12T07:09:19.841748+00:00
ended_utc: 2026-10-12T07:09:20.056743+00:00
wall_seconds: 0.21500125899910927
exit_code: 0
stdout_bytes: 1219
stdout_lines: 1
stdout_sha256: dad43eb4277ebc1941f300ca94e923acfa61ef501da0ec095fc2e16c483a7a18
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

All fifteen sources plus SOURCE_SHA256SUMS were publicly compared byte for
byte before this first execution. EXPECTED.txt contains its actual ASCII/LF
stdout. Environment overrides were PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC.

The exact rational-tableau, order, composition, reconstruction and local
comparison support checks passed. This standard-library gate does not run
the numerical kernel, emulate binary64 arithmetic, measure performance or
certify a complete trajectory. COMPARISON.md records the separate numerical
first outcome. CI replays the exact supporting verifier only.
