# Preserved first v110 integration attempt

NON-CANONICAL. This disposition concerns the structural integration audit,
not a failed mathematical identity or a changed scientific criterion.

The first complete content candidate was publicly frozen and read back at
`da638c51131d8b5518a72ac10cacda1c9543e115` on branch
`codex/canon-v110`. That commit and branch are preserved without amendment,
rebase or force-push. All twenty changed files were checked by byte count,
SHA-256 and Git blob in a fresh public Git checkout before execution.

Its first direct status-separation execution started at
`2026-11-08T17:22:39.370258+00:00` on Linux x86_64, Python 3.12.3.
It exited 1 with empty stderr, no timeout and 35898 stdout bytes, SHA-256
`5460f7ddc19cf2c941a3e81b0df286d0289e29e6e71e0ebb25f5cdbb88f9c062`.
All 216 historical checks passed. The eight new checks returned FAIL,
with final result 216/224. The expected output has 35902 bytes and SHA-256
`50478798472d2c147af4c820e121f6c1046a1880c3e4fb50e67432dbe8d84630`.
Exact stdout, empty stderr and the process receipt are retained outside the
public repository. The S3 wrapper was not executed in this attempt because
the direct-run sequence stopped at this failure.

Static diagnosis by the adapter author and coordinator agreed:
`V110_SOURCE_FILES` correctly binds all four existing forward-filter files,
but `V110_SOURCE_INVENTORIES` lacks the key
`reproduce/C-FORWARD-ONLY-CAPTURE-FILTER-N`. The new inventory predicate
indexes that key unconditionally. Its KeyError is caught by the generic
failure handler, which returns all eight new checks as false. The historical
byte reconstruction succeeded; no missing source byte or mathematical
counterexample was observed.

The successor candidate on `codex/canon-v110-2` starts from the same public
main base `e6dfc3de9659139d654000954733c084b8a6b86b`, independently retains
the complete fold, adds the missing explicit four-file directory inventory,
and binds this disposition and the updated audit documentation. All Canon
bytes, scientific source programs, supplementary S3 wrapper, expected output,
224 criteria, existing functions and operational limits remain unchanged.
There is no acceptance-threshold movement or expected-output repair.

The new complete content is committed, published and read back before its
first execution. Its later release-form commit changes only STATUS.md,
README.md and CITATION.cff. The failed branch remains a public witness and
is not part of the two-commit release branch. A successful successor is a
successful corrected candidate, never a first-attempt PASS.
