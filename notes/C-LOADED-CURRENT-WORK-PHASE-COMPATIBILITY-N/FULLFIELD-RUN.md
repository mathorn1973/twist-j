# Full-field execution record

**NON-CANONICAL / L1. Actual finite candidate-C evidence, not independent acceptance.**

## Prospective source

- Source commit: `2caeb658493825ad0e8a5f8f840c15634aa3ca8d`.
- Verifier: `verify_fullfield.py`,23,976 bytes, SHA-256
  `bf84cbca8fe96b4dfc7e4f96d973e787d29ea922687bfbaa7dcf1b1909758023`.
- The proof, exact fixture inventory and 900-second/1-GiB limits were
  fixed before execution. FULLFIELD-SHA256SUMS binds the five new inputs.
- All six additive files, including the manifest, were retrieved from
  GitHub at the exact source commit and matched their local Git blobs
  before the first run. The earlier SOURCE-SHA256SUMS inputs also remain
  unchanged. No code repair, tolerance change or fixture substitution
  occurred after either source freeze.

Command:

    python3 -I -B notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/verify_fullfield.py

The launcher fixed PYTHONHASHSEED=0, LC_ALL=C.UTF-8 and TZ=UTC, imposed
a 900-second subprocess timeout and RLIMIT_AS=1,073,741,824 bytes, and
retained actual stdout, stderr, exit status and timing. The verifier
uses only integer/Fraction standard-library arithmetic.

## First execution

- Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12.
- Started 2026-11-07T08:21:20.289001+00:00.
- Elapsed 116.506516783 seconds.
- Exit 0, no timeout, empty stderr.
- 2,547 assertions PASS.
- Stdout 612 bytes, including its final newline.
- Stdout SHA-256:
  `3b5f60d029efcb5df47678184826f30d5e11b8164fd0f997feb6166d8e5c5419`.
- Empty stderr SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

FULLFIELD-EXPECTED.txt is the actual first successful stdout.

## Reproduction and limits

The identical public pin was cloned into a clean checkout on aarch64.
Both frozen manifests and the clean Git state were checked before execution.

- Debian GNU/Linux 12 (bookworm), aarch64, Python 3.11.2.
- Started 2026-11-07T08:22:55.946998+00:00.
- Elapsed 340.5661609920062 seconds.
- Exit 0, no timeout, empty stderr, 2,547 assertions PASS.
- Identical 612-byte stdout and SHA-256 shown above.

The connector's initial wait expired while this same process continued.
Its original completed receipt and output were retrieved afterward; no
replacement run was launched. The scientific 900-second limit was not reached.
This is cross-architecture reproduction of one authored verifier, not
independent authorship or independent scientific acceptance.

This is a new full-field reconstruction from the public equations and
signed-port contract. The unavailable original #1926/#1927 bundles were
not replayed. The finite inventory cannot establish universal claims;
those depend on FULL-FIELD-PHASE.md and its explicit premises.

Repository policy CI is separate. It checks repository policy, unit
tests, Canon, ledger, gate contract and changed public probes/minimal
reproductions. It does not execute this notes verifier and is not counted
as scientific evidence for this candidate.
