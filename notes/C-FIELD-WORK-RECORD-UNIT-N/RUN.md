# Actual post-public-pin audit

PUBLIC / NON-CANONICAL / candidate-T / L1. Authority remains v95.
Reservation #1315; [draft PR #1316](https://github.com/mathorn1973/twist-j/pull/1316).
Date: 2026-10-01. No merge or promotion.

## Source pin and provenance

The immutable scientific source is
[`d01ff9a4bd0ba6cef62b7fc932a0e8ce8a0c054a`](https://github.com/mathorn1973/twist-j/commit/d01ff9a4bd0ba6cef62b7fc932a0e8ce8a0c054a),
parent 04fa72ca2506398bf47a64fe33aa024625bd4f9b (#1312). It adds 12 text files.
All 12 new files and 6 inherited source/proof inputs were fetched as actual
GitHub Contents API bytes at that pin and matched local bytes. The public
branch ref matched the pin. All 18 readbacks completed before the first new
scientific import/execution and before opening the draft PR. Eleven manifest
entries and eleven bridge source hashes bind the declared inputs.

The known C5 proof was supplied by the user, reviewed and separately
implemented. Expected counts/output were prepared from its frozen audit
scope before execution. This is audit of known mathematics, not blind
prediction. Both new adapters reuse exposed #1310 local arithmetic; a
separate unchanged #1312 adapter checks the entire old-state projection.
No original ZIP source was used to author or execute this new audit.

The user supplied the original ZIP after this source pin and first new run.
The frozen statements about its unavailability describe that earlier point.
They remain unchanged as provenance. ZIP_REVIEW.md records the subsequent
static custody/source review. Original archived run claims remain distinct
from the actual executions below; the original verifier was not replayed.

| Frozen file | SHA-256 |
| --- | --- |
| PREREG.md | 3b50502c27330588bc71bd176f1217a68855dde78c559ff01d0e8d2574cd5731 |
| PROOF.md | 91675857b1b99862772858bef50dd6ba9e56c2f001bcc1ea42f25dd6f192c511 |
| primary.py | 11009d50a61a6e158aeffd9f1fde5bd867ccfb286b38029f985774d9155eb705 |
| challenger.py | 5067aa1f50b433d6c1ddd50c00f40151164982226b665e51728a211e184c072c |
| audit.py | 2293c9354f3109351dc6ea652d68230b48714b69ce829a2ef27b3e727a1bc0b6 |
| verify.py | b1b231508fca99a3d26474c46a75918774924cc9263a6688e38db5d185da57f9 |
| EXPECTED.txt | ead14e75ea593819e24be8e9bdb178a7733b01ba6df87dfe853b453095208b80 |

EXPECTED.txt is 591 ASCII bytes in 8 LF-terminated lines. The unchanged runner
requires scientific exit 0, empty stderr and exact byte equality within 120 s.
Its PASS receipt executes both full-state adapters and the projection audit;
it is not merely a source-hash assertion or an earlier candidate's result.

## First clean local execution

An ordinary clean clone at the exact public-verified pin was used with Linux
Git metadata. HEAD and empty git status were checked before execution; all
manifest hashes were verified before and after. Command:

```text
python3 -B tools/check_reproduce.py --base 04fa72ca2506398bf47a64fe33aa024625bd4f9b
```

| Item | Actual value |
| --- | --- |
| Platform | Ubuntu 22.04, WSL2 |
| Architecture | x86_64 |
| Python | CPython 3.10.12 |
| Duration | 2.299 seconds |
| Exit | 0 |
| stderr | 0 bytes |
| Runner stdout | 170 bytes,LF |
| Runner stdout SHA-256 | bb4baa8ee5702012f0c1cd14a54f149dc2e28ea9d9918eebcfe12ec1404c871c |
| Frozen source hashes | unchanged before/after |

Exact runner stdout:

```text
REPRODUCE PASS field-work-record-unit-n b1b231508fca99a3d26474c46a75918774924cc9263a6688e38db5d185da57f9 ead14e75ea593819e24be8e9bdb178a7733b01ba6df87dfe853b453095208b80
```

This first new audit passed without changing the source pin. No failed
scientific run preceded it in this new audit. This assertion describes this
work's execution, not the unobserved history of the supplied original ZIP.

## Actual public architecture receipts

[Workflow 36854724602](https://github.com/mathorn1973/twist-j/actions/runs/36854724602)
ran source head d01ff9a4bd0ba6cef62b7fc932a0e8ce8a0c054a successfully.

| Job | Result | Python | Evidence |
| --- | --- | --- | --- |
| [architecture-x86_64](https://github.com/mathorn1973/twist-j/actions/runs/36854724602/job/110344385477) | success | CPython 3.12.14 | identical receipt above |
| [architecture-aarch64](https://github.com/mathorn1973/twist-j/actions/runs/36854724602/job/110344385800) | success | CPython 3.12.14 | identical receipt above |
| [check](https://github.com/mathorn1973/twist-j/actions/runs/36854724602/job/110344551151) | success | not applicable | both architectures pass |

Actual completed logs were read for both architecture jobs. Each contains
this reproduction name with identical bridge and EXPECTED hashes, plus 172
passing repository tests and policy/Canon/ledger/gate-contract passes.
Publication was correctly skipped for a draft. The runner/workflow are
unchanged. This satisfies the public two-architecture computation gate for
this new frozen audit. It is not a reproduction of the original ZIP verifier.

## Scope and disposition

The new audit checked 20 unit-energy seeds, 1440 positive full boundaries,
27 cuts / 518 boundaries, 72 offimage boundaries, 1960 local cases and 2160 generic
state/cut cases. The full projection, all layer accounts and both inverse
identities pass. The local accepted pair has the exact ten-cycle, correctly
rejecting involutivity of the extended reaction. Universal all-length and
all-time conclusions remain proof-based. No frozen falsifier fired.

The pinned source is preserved. Later changes add only RUN.md, RESULT.md
and ZIP_REVIEW.md; final-head checks must also pass before handoff. The
mathematical unit is closed at its declared conditional candidate scope.
The physical contract remains open and supplies no laboratory evidence,
registered physical lift, J-derived law or measured cost of the pointer.
No merge, promotion, Canon/registry change, tag or release is performed.
