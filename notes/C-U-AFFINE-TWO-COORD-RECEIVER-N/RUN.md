# First execution record

NON-CANONICAL / L1 / candidate-C. Result-exposed audit, not a blind prediction.
All four input files were fetched at the public immutable pin and compared
byte for byte before the execution below. The readback receipt is on #1519.
No source was changed after the pin. EXPECTED.txt is the actual first stdout.

pin_commit: 5caff8280c195c12c8c41bf462daae8e6d4bd64b
verifier_sha256: 5966925f5cfd587c6ad6cef911ab344907c923638fae096df89cdf480f230bd2
command: python3 notes/C-U-AFFINE-TWO-COORD-RECEIVER-N/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: e23f8f3db9cf86e66700abbbefba32ccbf1ecafd8ae2b42a42cdf2b6b0263278
stdout_bytes: 731
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-15T12:02:48.672508+00:00
finished_utc: 2026-10-15T12:02:49.031240+00:00

Deterministic environment: PYTHONHASHSEED=0, PYTHONUTF8=1,
PYTHONDONTWRITEBYTECODE=1, LC_ALL=C, LANG=C, TZ=UTC.
Execution used a 90-second safety timeout; the completed output is retained
without a timeout or threshold change.

This is one x86_64 computation lane. The direct and matrix checks are by the
same author. No independent-agent review or two-architecture scientific gate
is claimed. Ordinary notes-only PR checks do not execute this verifier.
No first-run failure occurred. No older conversation run is counted.
