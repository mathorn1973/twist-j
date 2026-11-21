# Execution and custody record

Candidate: C-PRIME-TWO-BODY-CHANNELS-N
Date: 2026-10-30
Status: NON-CANONICAL / L1 / exact finite audit.

## Prospective public pin

    c708a68d6407d750aabf61e9595e7b16ba9d21d1

The pin contains the five scientific/reference files and FROZEN.sha256.
It was publicly pushed and fetched back before either program executed.
Every source SHA-256 was checked immediately before each execution.
The x86_64 authoring environment had a read-only deploy key; the exact
properly authored Git bundle was transported to an authenticated publisher.
The bundle and commit were verified byte-for-byte. No source was rewritten
and no public pin was backdated. This transport changed no scientific input.

Author and committer: A. M. Thorn <thorn@twistj.com>.
Base main: a193e389fb1ddb0bdc89165b015c95a17eb1e425, Canon v106.

## Exact commands and environment

From this directory, on the unchanged pin, with 120 s process limit per run:

    python3 -I verify.py
    python3 -I crosscheck.py

Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Python standard library only, no floating point.
Each of the two programs ran once on each of the following architectures:

| Architecture | Operating system | Python | verify.py | crosscheck.py |
|---|---|---|---|---|
| x86_64 | Debian GNU/Linux 13 (trixie) | 3.13.5 | exit 0, stderr 0 bytes | exit 0, stderr 0 bytes |
| aarch64 | Debian GNU/Linux 12 (bookworm) | 3.11.2 | exit 0, stderr 0 bytes | exit 0, stderr 0 bytes |

verify.py stdout: 516 bytes, SHA-256
`75ecc00695ea85e75c6c46fdabb3ccd3c63c10e30c6528b1ba7706468c11c55b`.
crosscheck.py stdout: 466 bytes, SHA-256
`38ca7c08dabb2a58f83911fdd99237ce7162d9e8e7a62ea3fd4ca6ba98779184`.
Each program's stdout is byte-identical across the two architectures.
The full channel-ledger hash agrees between BOTH implementations:
`354b9ded4cc7aa8af1094b3904c2ad0ac50b911fe94bd328e27c481268e04d85`.

## Scope of this agreement

These are genuine two-architecture reproductions of a notes-only audit,
NOT a formal public probe run or a promotion to a registered theorem.
Neither architecture run is an independent mathematical confirmation.
The second implementation was authored by the same session, using trace
coordinates rather than coefficient coordinates; no blind-agent claim.
Its frozen stdout sentence "not independent review or second architecture"
describes the implementation distinction itself. This run record separately
records the actual aarch64 replay without altering that frozen script.
Repository CI does not run scientific scripts under notes/ and must not be
counted as an additional scientific execution.

## Frozen inputs

FROZEN.sha256 remains unchanged from the public pin. No failure, rerun,
threshold change, range change or source correction occurred after the pin.
The later SHA256SUMS covers the completed note package, excluding itself.
