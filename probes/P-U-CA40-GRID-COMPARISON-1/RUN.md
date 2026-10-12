# First exact supporting run

PUBLIC NON-CANONICAL. L1 computational supporting evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

```text
pin_commit: ea8bff874876c1b6f902409888e4e98fb7716066
command: python3 probes/P-U-CA40-GRID-COMPARISON-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
prereg_sha256: 6f0c1f772e119f5a1f47219b2308491f1c8c3177f1b73a5438c9917bbf0d9eba
verifier_sha256: 7e3edbbc566ecc1e9a7f696e64f3db860e33325775daffa22b70e18e9370db9c
public_source_readback_utc: 2026-10-11T16:05:12.942240+00:00
started_utc: 2026-10-11T16:06:22.050056+00:00
ended_utc: 2026-10-11T16:06:22.115024+00:00
wall_seconds: 0.06497555412352085
exit_code: 0
stdout_bytes: 539
stdout_lines: 1
stdout_sha256: 921c664b6b09becb84c79cc99be0c4d5680c6d59b1bb6c83dd1bbe2da2183c00
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

All fourteen source files were publicly compared byte for byte before this
first execution. EXPECTED.txt contains its actual ASCII/LF stdout.
Environment overrides were PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
LC_ALL=C, LANG=C and TZ=UTC.

The exact matching-window, triangle/enclosure, classification and bound-growth
fixtures passed. This standard-library gate does not run the numerical kernel,
emulate binary64 arithmetic, measure performance or certify a trajectory.
The numerical first outcome is reported separately in COMPARISON.md. CI
replays this exact supporting verifier, not the numerical campaign.
