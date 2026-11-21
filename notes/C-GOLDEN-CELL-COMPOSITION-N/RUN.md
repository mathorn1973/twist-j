# Exact audit execution record

Candidate: C-GOLDEN-CELL-COMPOSITION-N. Date: 2026-10-30.
Owner: A. M. Thorn / ChatGPT-golden-composition-20261030, issue #1842.
Status: NON-CANONICAL / L1 / supplementary exact audit.

## Prospective pin and source custody

Public pre-execution commit:
`cf79477d95d1dae72f48dd99305a7787ef179db1`.

All six pin files were committed and pushed, fetched back, and the
FROZEN.sha256 file was additionally read through the GitHub connector
before any scientific execution. The fixed inputs were checked immediately
before each run. Their bytes have not changed. Source assertions and the
negative witnesses were analytically exposed, not blind predictions.

Author and committer: A. M. Thorn <thorn@twistj.com>.
Base: a193e389fb1ddb0bdc89165b015c95a17eb1e425, Public Canon v106.

## Actual first executions

Command from the note directory: `python3 -I verify.py`.
Environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1. Per-process timeout:120 seconds.
Python standard library, integers and Fraction, no floating point.

| Architecture | Operating system | Python | Exit | Stderr |
|---|---|---|---|---|
| aarch64 | Debian GNU/Linux 12 (bookworm) | 3.11.2 | 0 | 0 bytes |
| x86_64 | Debian GNU/Linux 13 (trixie) | 3.13.5 | 0 | 0 bytes |

One run on each architecture. Both actual stdouts are879 bytes, SHA-256:
`766f8df36e89316de216f6ae99e60a585cdb86f50c0e9da455f554cfd13676df`.
The normal-form ledger hash is
`78b5403b6aff161f26fcf702e87132f9bd28fa3b72a81a6fcff6a800b32f1ac4`.
EXPECTED.txt contains the actual aarch64 stdout; readback against the
original x86_64 output is part of publication validation.

## Interpretation

Every frozen exact check passed on its first execution. No scientific
source, input range, threshold or hypothesis was changed after the pin.
PASS reproduces the stated positive identities AND negative obstructions.
It does not mean that the rejected normalized total-momentum map exists.

These are genuine two-architecture reproductions of one notes-only program,
not independent mathematical review, a formal P-probe gate, or promotion
to a Public Canon T row. The different coefficient and trace recurrences
were authored in the same session. Repository CI does not run scientific
scripts in notes/ and is not counted as another scientific replay.
Universal statements are the written proofs, not these finite ranges.
