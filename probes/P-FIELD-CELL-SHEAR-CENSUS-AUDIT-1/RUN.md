# First formal run

PUBLIC / NON-CANONICAL. Captured before author-result exposure.

pin_commit: 105d22bfc457f5e3f29dfa7b3ca75694b21670fd
verifier_sha256: aa2ea1cdd4e3a8d409cad4d75a0f0d0d390d7d78d5b15177f4820541a1e080e6
prereg_sha256: 56494c692a1759ee43cc0855f83f98c4881e800651d4b39968f1224ec23e4d9b
command: python3 probes/P-FIELD-CELL-SHEAR-CENSUS-AUDIT-1/verify.py
platform: Debian GNU/Linux 12 (bookworm)
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 8d9826f1ffd8437c283123571941af32194fe411d2f56ddfc19e20322d3b8542
stdout_bytes: 523
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-16T22:05:13.747119+00:00
ended_utc: 2026-10-16T22:05:13.939442+00:00

The exact pin was fetched into a separate clean Linux checkout and its
verifier hash checked before execution. LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1; PYTHONOPTIMIZE unset.
Timeout was 600 seconds. stdout and stderr were captured separately outside
the checkout; the stdout bytes were transferred without text normalization,
then checked against the captured byte count and SHA-256 before committing
EXPECTED.txt. There was no previous scientific run, import or dry run.

All five cases, 248 orientations and the preregistered negative controls
passed. The first output is preserved verbatim. Formal GitHub replay and
author comparison have not yet occurred at this record's first commit.
