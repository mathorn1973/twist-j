# First execution record

PUBLIC / NON-CANONICAL / L1. Claim #1559, lane RA.

pin_commit: a19a2f38517863a480476abb35fa45bfa4dfdfeb
verifier_sha256: f9cb88e38afdd4b8279adb1d55bbbcfa90076dd9254713de971c60a663ac4890
command: python3 probes/P-U-AFRAME-GATE-AUDIT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 5fae6e8c596460e3b1d2a71a6460c0d3d7ddaf4ad10fc9e33e3db576158e1477
stdout_bytes: 1044
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-16T21:31:52.735827+00:00
completed_utc: 2026-10-16T21:31:54.240138+00:00
elapsed_seconds: 1.503325
timeout_seconds: 600
timeout: false

## Custody and environment

This was the first scientific execution or import of the frozen verifier.
The repository was clean at the full pin. The branch had been pushed, and
all five initial files were read back byte-identically through GitHub at
that pin before execution. The public pre-execution receipt is
https://github.com/mathorn1973/twist-j/issues/1559#issuecomment-6225089549 .

The process ran from the repository root with `LC_ALL=C`, `LANG=C`,
`TZ=UTC`, `PYTHONHASHSEED=0`, and `PYTHONDONTWRITEBYTECODE=1`. Standard
output was captured as bytes without normalization and copied exactly to
`EXPECTED.txt`. Standard error was empty. No timeout, repair, retry,
threshold change or source change occurred.

All nine frozen falsifiers printed PASS and the final line was
`RESULT PASS`. This is an actual completed computation. It is not a
second architecture result or a claim that finite regression proves
unbounded time. The frozen `PROOF.md` supplies the algebraic derivation
and induction. The author comparison had not begun when this record was
written; the author proof, implementation and results remained unopened.

## Subsequent reproduction

Repository replay and GitHub architecture results are to be recorded
after this first-run record is committed. A replay will not replace or
reinterpret this first result.
