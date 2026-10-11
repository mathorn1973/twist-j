# First exact supporting run

PUBLIC NON-CANONICAL. L1 computational supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

```text
pin_commit: 09dde450cfcb9386262afbd0b790250bd3c1bb4a
command: python3 probes/P-U-CA40-DP5-COMPARISON-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
prereg_sha256: 56dae6218278be2a878765fd784f64a112ae29e6c27d876d93a81b4626bd1560
verifier_sha256: d581503a14357c1d27a2fd3b62fb775960e2400c5542a7b3a4cbee59e4254e81
public_source_readback_utc: 2026-10-11T17:15:19.565240+00:00
started_utc: 2026-10-11T17:16:44.843142+00:00
ended_utc: 2026-10-11T17:16:45.058401+00:00
wall_seconds: 0.21526585705578327
exit_code: 0
stdout_bytes: 963
stdout_lines: 1
stdout_sha256: 621c571e28fcba8f228f8deaf0755407cd9fe7825e128ac5a97a20211226cee7
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
