# First exact run

pin_commit: 1949d6c5c9712fc2c3aa10f0ac296afb9ea5e928
verifier_sha256: 4f8481297febd4a5d01b47bda050a5f30216b4474ff76de761fefbd0d5c87a0c
command: python3 probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-1/verify.py
platform: Ubuntu 24.04 / Linux
architecture: aarch64
python: 3.12.3
exit_code: 0
stdout_sha256: 481062b8cbedafe06f14835e0ed1a3dee33380b48c92782a76478d616f747acf
stdout_bytes: 210
stdout_lines: 3
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The clean Linux checkout was obtained from the public Git branch and checked
out at the exact pin. All frozen file hashes passed before execution. Public
readback and the PINNED receipt preceded the first scientific import/run.
The wrapper used a 600-second subprocess timeout and the deterministic
environment `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Output was captured as bytes without filtering or normalization.

First execution began 2026-10-15T09:59:36.330310Z and ended
2026-10-15T09:59:36.394158Z. Measured wall time was 0.064 seconds
(engineering metadata, not exact scientific data).

The run completed the frozen false-target reporting path: exact geometry
assertion FAILED; remaining checks NOT_RUN. Exit zero records a completed
deterministic failure report, not scientific success. See RESULT.md.

No comparison-mode execution or cross-lane code exposure occurred before
this record. Architecture replay evidence is recorded separately after it
exists; this first run alone is aarch64 evidence only.
