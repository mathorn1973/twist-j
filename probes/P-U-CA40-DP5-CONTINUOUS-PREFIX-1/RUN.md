# First exact supporting run

PUBLIC NON-CANONICAL. L1 computational supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.

```text
pin_commit: 4c3a29e3ce4db210b754cd18e5340b805f8c5df7
command: python3 probes/P-U-CA40-DP5-CONTINUOUS-PREFIX-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
prereg_sha256: c7312af7654a0abc2038bd8f8f20b705346968c5862e527c54a37ca19c3097e0
verifier_sha256: bc95d66be0f53529831c6c4d114d97960a2caf91b783215334a2599b3e5cadec
public_source_readback_utc: 2026-10-12T07:43:35.175509+00:00
started_utc: 2026-10-12T07:45:34.017631+00:00
ended_utc: 2026-10-12T07:45:34.232912+00:00
wall_seconds: 0.21528926119208336
exit_code: 0
stdout_bytes: 1536
stdout_lines: 1
stdout_sha256: 8853daa287401d818bcff8c8d347d0aa32c3c0c9f64d65e914a0ab4bbc96c6e2
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

All fifteen sources plus SOURCE_SHA256SUMS were publicly compared byte for
byte before this first execution. EXPECTED.txt contains its actual ASCII/LF
stdout. Environment overrides were PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, LC_ALL=C, LANG=C and TZ=UTC.

The exact rational-tableau, order, composition, reconstruction, continuous-prefix geometry and cumulative
chain support checks passed. This standard-library gate does not run
the numerical kernel, emulate binary64 arithmetic, measure performance or
certify a complete trajectory. COMPARISON.md records the separate numerical
first outcome. CI replays the exact supporting verifier only.
