<!-- SPDX-License-Identifier: Apache-2.0 -->

# First execution record

**NON-CANONICAL / L1 / candidate-C finite audit. One architecture.**

## Immutable source and public readback

- Base: `d4d363722f052141a4ce65e9da39f11a74b43b95`, Public Canon v109 ACTIVE.
- Original source pin: `05c09a7de1a10cd1b466a7d9b2885b7e45e3461c`.
- Published checkout: `d2846f75cb31ef3150a662b502757674797679fd`.
- Branch: `notes/c-gauss-determinant-archive-1`.
- Reservation: https://github.com/mathorn1973/twist-j/issues/1951.

The author explicitly authorized publication, both first executions and a
draft pull request. The existing two-commit history was published without
rewrite. Before either script ran, the GitHub connector returned all six
files at the published checkout; their UTF-8 bytes and Git blob identities
matched the local files exactly. PREREG.md, PROOF.md and both checkers matched
the source hashes recorded in the earlier PROMO.md. This ordering was
observed by the executing session, not independently time-attested.

The source and breaker were both frozen before their first runs. The
breaker was previously authored from PREREG.md and its public premises
without verify.py. A separate pre-publication static reviewer read all six
files and found no safety, licence or source correctness blocker; that
reviewer did not execute either script and is not a new blind breaker.

## Environment and commands

Working directory: the repository root of the clean published checkout.

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Each command ran once in a separate subprocess with a 600-second timeout.
Exact stdout and stderr were captured separately. Both commands finished
normally; neither timed out. The checkout remained clean after execution.

## verify.py

```text
command: python3 notes/C-GAUSS-DETERMINANT-ARCHIVE-1/verify.py
checkout: d2846f75cb31ef3150a662b502757674797679fd
platform: Linux
architecture: x86_64
python: 3.12.14
started_utc: 2026-11-07T22:05:41.721537+00:00
finished_utc: 2026-11-07T22:05:41.938107+00:00
exit_code: 0
source_sha256: 828afff92f64a43ff2c2c50e3f830eb8ed4c2274fb7fee61355d4b36cd4d1ca2
stdout_bytes: 2330
stdout_sha256: c37eb22a573213beae003073856cfbdaa6970c7bd3684be8b62da8ab0b288529
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## break.py

```text
command: python3 notes/C-GAUSS-DETERMINANT-ARCHIVE-1/break.py
checkout: d2846f75cb31ef3150a662b502757674797679fd
platform: Linux
architecture: x86_64
python: 3.12.14
started_utc: 2026-11-07T22:05:41.939331+00:00
finished_utc: 2026-11-07T22:05:42.377454+00:00
exit_code: 0
source_sha256: 10fa7d006c728ae0b6e9d0f559e4efd8c1e4a73b935bc16bd991c008446f6427
stdout_bytes: 1971
stdout_sha256: 8effd71b4755f41221b86f586e0280ba42551f4e93e12851a1a15961a8f4e23b
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Primary stdout is preserved verbatim as EXPECTED.txt; breaker stdout as
BREAK_EXPECTED.txt. The stderr files were both empty and are represented
by the byte counts and empty-string hashes above. No private machine
name, environment dump or failed development log is published.

## Output comparison

The schemas differ, so byte identity between these two stdout files is
neither expected nor asserted. The post-run evidence-only comparison

```text
python3 notes/C-GAUSS-DETERMINANT-ARCHIVE-1/compare_results.py
COMMON OUTPUT COMPARISON PASS comparisons=42
```

compares the common scale and receiver values, both source accounts and
counts, full edge-current vectors, field returns and diagnostic changes,
both actual matrix fingerprints and determinants, complete path sums,
and inverse lengths. It reads only the two recorded outputs and does not
run or import either frozen checker. It was added after execution as
transparent bookkeeping, not presented as a preregistered scientific probe.

A separate post-run reviewer also compared the common outputs and found
no mismatch. The primary-only G0 enumeration and primary-only intermediate
diagnostic-cut observations are not claimed as independently reproduced.

## Status and repository validation

The finite audits are candidate-C on x86_64. The conditional proofs retain
candidate-T scope without independent public acceptance. A second checker
is not a second architecture. Notes-only repository CI checks repository
integrity and does not run these scientific scripts. Required workflow
results are recorded on the associated pull request at its exact head.
The direct continuity lift remains REJECTED_FIELD_RETURN and the coupled
root-pair target remains NOT_REALIZED, as detailed in RESULT.md.
