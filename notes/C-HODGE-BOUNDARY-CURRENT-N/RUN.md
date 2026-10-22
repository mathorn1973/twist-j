# Accepted execution custody and first-run records

**NON-CANONICAL. L1. State: BOTH FIRST EXECUTIONS PASS.**

The accepted execution pin is
`4fc3b693b2ae55274153dc6219f8ccd61c042ce1`, with parent
`e6240e2689bb22aab5f02bad90b75d3692bb96d9` and tree
`5da3b0f4171c91b0104eace873d91a9b1f842dcc`. Its Git timestamp is
2026-10-22 23:06:10 UTC. It was assigned to the public branch
`notes/c-hodge-boundary-current-n`. Before either program ran, all 11
package files were fetched at that exact commit and
matched byte for byte, including their Git blob IDs. Author and committer
matched the explicitly authorized attribution below.

The local checkout then fetched that branch, checked out the exact accepted
commit, confirmed a clean worktree, and verified all ten manifest entries.
Each scientific program was executed exactly once. Its first stdout,
stderr and exit were preserved before any result metadata was updated.
No program import or scientific execution occurred before the public pin.

## Frozen local preparation

The contract and first two proofs were committed locally at
`e765ae999f2fc60a0ed30096e835386b0f025660`, before either program was completed.
The supplemental full-label proof and exact source manifest followed at
`271bc3d88fe417ad780fb7a31af96bc306b852b2`, still before any execution.
Both local commits have author and committer
`A. M. Thorn <thorn@twistj.com>`.

Before any accepted public pin or execution, one redundant final blank line
in PROOF_CURRENT.md was removed after the full base-diff whitespace check.
No mathematical text, contract or program changed. Its original bytes remain
in the first local commit; the table records the accepted normalized file.

Frozen source bytes at the accepted execution pin, unchanged after execution:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 10621 | `302319f0a75e485e50d443e796bda0b0da3344c561950c6b6b09ee8629f90abb` |
| PROOF_CURRENT.md | 20089 | `20aea3a68f1751f31963ab111029efe2e46ed44ace8c4c477302591f79fe0c90` |
| PROOF_METRIC.md | 13978 | `5d2edf21b84be9b056ad853176586a8f78f019964d8e03a94260f573a8f13b82` |
| PROOF_LABELS.md | 9207 | `6686d8fbe6032ea71a9c4fb413bafe0c5d36b7606c2e2307d8c359296e5feb65` |
| SOURCES.md | 6548 | `960cc501262871662c34d4c05b3e726b2b92a48e9fd0f2cb5e4b9fdae865892c` |
| verify.py | 18736 | `567a47c87d82a28795e275b038062a37860b47ff380f183e7bc55480dc82e05b` |
| break.py | 28276 | `ca25c2200fd1ba9e7c93479a5c8c52712885f49acc465162cab274df43a3e512` |

The main implementation uses Q(sqrt(5)) and two quadratic extensions,
Gaussian elimination and Newton identities. The independently written
breaker uses an explicit four-coefficient quotient field, a separate CM
pair representation, and principal-minor permutation determinants. The
breaker author did not inspect the first implementation. Both completed
programs were statically reviewed before execution; their inputs and expected
analytical outcomes were exposed. This is same-session code-blind
corroboration, not an external blind study.

## Publication attribution before execution

The GitHub connector successfully uploaded the then-current seven blobs, before the
cosmetic EOF normalization just recorded, and a
prospective tree `2145e8f5cb8f1add06a9771985347a279062b69d`, then created the
unreferenced commit `ecdaa90ecc6bfd0974349e5237a485ce519b37be`.

Before any ref update, readback showed that the connector assigns the
connected account's noreply email to both author and committer. The name is
A. M. Thorn, but the email differs from the repository's required
`thorn@twistj.com`. The connector exposes no author/committer override.
Therefore this object was **not** assigned to a branch and is **not** accepted
as the execution pin. No draft pull request was opened from it.

The local clone has no usable Git write credential, and the separate
authenticated transport checks did not respond. No remote scientific
program, shared checkout mutation or remote Git configuration was attempted.
Publication was paused for an explicit author exception. The author then
authorized use of `A. M. Thorn
<221838986+mathorn1973@users.noreply.github.com>` for the new draft. This
exception resolves attribution only. The old unreferenced object remains
unaccepted and was never executed. The fresh complete package named above
included the normalized proof and prospective records, and was committed,
assigned to the new branch, and read back before execution.

The public base and predecessor were rechecked after this authorization.
Public main and peeled canon-v104 remain
`e6240e2689bb22aab5f02bad90b75d3692bb96d9`; source PR #1713 remains at
`31aad8fd834ca17a98d853081a8891a029b32fd5`. The reserved issue #1714 is open
and the proposed remote branch was absent before publication.

## First scientific executions

Both commands were run from the root of the clean accepted checkout:

~~~sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-HODGE-BOUNDARY-CURRENT-N/verify.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-HODGE-BOUNDARY-CURRENT-N/break.py
~~~

Neutral environment: **Linux; x86_64; Python 3.12.14**. No second architecture
has executed these programs. The processes ran sequentially and neither
changed a repository file. The first outputs were captured as bytes; the two
published EXPECTED files are copies of those unchanged first stdout streams.

| Record | verify.py | break.py |
| --- | --- | --- |
| Start, UTC, 2026-10-22 | 23:07:03.005638 | 23:07:03.986037 |
| End, UTC, 2026-10-22 | 23:07:03.972848 | 23:07:04.651884 |
| Exit | 0 | 0 |
| Stdout file | EXPECTED.txt | BREAKER_EXPECTED.txt |
| Stdout bytes | 700 | 607 |
| Stderr bytes | 0 | 0 |
| Executions | 1 | 1 |

Stdout SHA-256:

- EXPECTED.txt:
  `4864fd6d13f97855a8a508ff4f361c15e91a8f0e7d63be99bb552f0d935e7a7d`.
- BREAKER_EXPECTED.txt:
  `9a1bf94b4bf3eac5d905b933883ba4b0b57656427312186be1517ae0afefc6cd`.
- Each empty stderr stream:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Both executions passed every frozen audit family and all five rejecting
negative controls. No scientific code, proof, source manifest, contract or
threshold was changed after pinning. There was no scientific rerun, amendment
or discarded execution. Their distinct stdout formats do not need to agree
with one another; any future replay must match its own retained output byte
for byte.

The full-label theorem and the corrected CM dual-number/saturated-lattice
comparison retain their analytical basis. The latter is explicitly printed
as ANALYTIC_ONLY by the breaker. These finite audits do not claim to establish
universal real-parameter theorems by enumeration.

## Repository checks

These required checks passed both during preparation and after the first
scientific executions:

- `check_policy.py`: PASS.
- `unittest discover -s tools -p 'test_*.py'`: all 210 tests PASS.
- `check_canon.py`: PASS, v104, 576 claims.
- `check_ledger.py`: PASS.
- `check_gate_contract.py`: PASS.
- Changed-path verifier and reproduction checks against public v104:
  NOT APPLICABLE, because this is a notes-only change.
- Diff whitespace and named-file public-safety review: PASS.

The first unit-test attempt encountered 26 missing historical-object errors
in a partial clone. Fetching the complete public objects resolved the
environment defect; the repeated required suite passed all 210 tests.
No scientific program was part of either unit-test invocation.

These infrastructure checks are not mathematical output, scientific
reproduction, or a two-architecture scientific gate.
