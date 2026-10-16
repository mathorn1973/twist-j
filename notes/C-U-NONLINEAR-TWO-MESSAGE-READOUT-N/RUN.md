# First execution record

NON-CANONICAL / L1 / candidate-C. Result-exposed audit, not a blind prediction.
All five input files were read back byte for byte from the public pin before
this execution; no source was changed after the pin. Earlier conversational
throwaway runs on 2026-10-15 are disclosed in PREREG.md and are not counted.

pin_commit: d085d7ad63401619911bd26a2da09df06be5a047
verifier_sha256: 72be3d0c668932f0147462c50cd710b2c82f65bb1ab45087bda508db1bcbfa55
command: python3 notes/C-U-NONLINEAR-TWO-MESSAGE-READOUT-N/verify.py
platform: Windows 11 (10.0.26300)
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256_as_captured_crlf: 7abfa86b7853b039f08a07726afc78fef4f87639a5b9d305f1d20840132eec3c
stdout_bytes_as_captured_crlf: 141
stdout_sha256_committed_lf: e552f0a2cd306bbea07ea43e216fff3bb68cd6dfe24c83561b8d68d5cfc469e5
stdout_bytes_committed_lf: 140
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-15T19:40:37.350490+00:00
finished_utc: 2026-10-15T19:40:37.683850+00:00

Deterministic environment: PYTHONHASHSEED=0, PYTHONUTF8=1,
PYTHONDONTWRITEBYTECODE=1, TZ=UTC.

Platform note on bytes: this first lane execution ran on Windows, where the
captured stdout line ends CRLF (141 bytes, first hash above). The repository
`.gitattributes` mandates `eol=lf`, and a Linux replay of the same frozen
verifier emits LF; EXPECTED.txt therefore commits the LF form (140 bytes,
second hash above). The single output line is otherwise byte-identical.
The frozen verifier was not modified after the pin to alter its output
framing; an independent Linux replay is the clean way to remove this note.

This is one x86_64 computation lane by the owner session. No
independent-agent review and no two-architecture scientific gate is claimed.
Ordinary notes-only PR checks do not execute this verifier. No first-run
failure occurred; exit code 0 and empty stderr are recorded above.
