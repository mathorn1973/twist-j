# Prospective execution custody

**NON-CANONICAL. L1. State: PREPARED / NOT EXECUTED.**

There has been no import or execution of either new scientific program.
There are no first-run stdout, stderr or exit records, and no EXPECTED file is
invented. Static parsing and compilation are not scientific execution.

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
in the first local commit; the table records the prospective normalized file.

Accepted source bytes prepared for the prospective package:

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
programs were statically reviewed; their inputs and expected analytical
outcomes were exposed. This is same-session code-blind corroboration, not an
external blind study.

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
exception resolves attribution only. The old unreferenced object is still
not an accepted execution pin: a fresh complete package, including the
normalized proof and these prospective records, must be committed, assigned
to the new branch, and read back before execution.

The public base and predecessor were rechecked after this authorization.
Public main and peeled canon-v104 remain
`e6240e2689bb22aab5f02bad90b75d3692bb96d9`; source PR #1713 remains at
`31aad8fd834ca17a98d853081a8891a029b32fd5`. The reserved issue #1714 is open
and the proposed remote branch was absent before publication.

## Required next execution sequence

1. Publish an accepted package with authorized attribution. Preserve the
   seven source-file hashes above.
2. Read the complete package back from its exact public commit and verify all
   file bytes, Git blobs, author and committer before execution.
3. From the repository root run each accepted program once with the following
   deterministic environment, separately preserving stdout, stderr and exit.

~~~sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-HODGE-BOUNDARY-CURRENT-N/verify.py
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 notes/C-HODGE-BOUNDARY-CURRENT-N/break.py
~~~

4. Keep the first outputs even if they disagree or fail. A genuine mismatch
   rejects the corresponding candidate. A code or custody defect must be
   recorded before any explicitly amended successor run; no silent edit or
   rerun is permitted.
5. Add neutral run metadata and the exact outputs, without changing the
   frozen contract, proofs or programs. Open the notes-only draft PR and
   report repository CI separately from scientific execution.

The current planned run lane is Linux x86_64 with Python 3.12.14. A second
architecture has not run these programs. Their distinct stdout formats need
not agree with one another; each transcript must be retained and any replay
must match its own frozen output byte for byte.

## Repository checks already completed

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
