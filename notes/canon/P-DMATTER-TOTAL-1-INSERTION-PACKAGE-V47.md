# P-DMATTER-TOTAL-1 Insertion Package v47, conservative (NON-CANONICAL until fold)

```text
STATUS:                    CONSERVATIVE INSERTION PACKAGE / OWNER-DIRECTED / NOT CANON
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               Public Canon v47, tag canon-v47
PUBLIC CONTENT COMMIT:     95219e2ba51bdedce76b2040bb0cfcb97937edfa
PUBLIC CANON SHA-256:      5e4c454e53381e13df2bc2e894bd6e7328af9329c4b13df03106c902c7caf400
PUBLIC CANON BYTES:        225589
CLAIM ISSUE:               107
OWNER DECISIONS:           2026-08-15 SPLIT / ACCEPT T1 / SLOT RULING,
                           2026-08-15 AUDIT: conservative variant
CARRIES:                   QDD-OWNER-RULINGS-2026-07-30 (both rulings),
                           P-DMATTER-TOTAL-1-EFFECT-SHADOW-MINIMAL-OWNER-FREEZE.md,
                           the ten corrections of AUDIT-QDD-BINDING-PACKAGE-V27.md
SUPERSEDES:                the four-commit branch and PR #384 (closed unmerged;
                           its D-promotion package is withdrawn)
FORMAL RUN:                NONE (public two-architecture jobs are the evidence)
CANON / TABLE CHANGE:      NONE by this note; the delta is a fold candidate
QDD STATUS:                O / STOP, NOT changed by this package
```

## 0. Audit findings carried into this package

The owner audit of 2026-08-15 stopped the previous release with two binding
blockers. Both are fixed here by construction.

Blocker 1, release form. `AGENTS.md` item 9: after v1 activation one reviewed
release branch may carry exactly two frozen commits, the complete content fold
and the release-form commit changing exactly `STATUS.md`, `README.md` and
`CITATION.cff`; merge without squash or rebase. The previous branch carried
four commits. This package therefore splits the flow: the candidate bundle
and its RUNS records reach `main` first through their own pull request (the
v47 pattern), and only then is the release branch cut with exactly the two
frozen commits.

Blocker 2, effect_ids. Ruling 2 of `QDD-OWNER-RULINGS-2026-07-30` and the
`EFFECT_SHADOW_MINIMAL` owner freeze ("creates no public identifier and fills
no completion-contract field by itself") bind: `quadratic_manifest.effect_ids`
is `UNRESOLVED`, the `effects` requirement of the completion contract stays
open, the contract is not submitted, and `QUADRATIC-DECODER-DATA` stays
`[O] / STOP`, untouched in registry, normative table, frontier program table
and Canon prose. Promotion to `[D]` would require a new explicit owner
amendment superseding Ruling 2; no such amendment exists, so it is not
attempted.

## 1. Composition (conservative)

```text
FOLD IN
    17 definitions DEF-QDD-* (statement source canon/CANON.md, Ruling 1);
        DEF-QDD-PROJECTOR-LOW / DEF-QDD-PROJECTOR-HIGH carry ALGEBRAIC_READOUT
        and cite the EFFECT_SHADOW_MINIMAL freeze (Ruling 2)
    QDD-ALGEBRAIC-FACTORIZATION      [T, L1]   exact record factorization,
        with the DIRECT-WRITE independence firewall in scope and falsifier
    QDD-PROJECTOR-PAIR-TR4           [T, L1]   unique G-self-adjoint idempotent
        with kernel ker Tr_4; closed forms; no uniqueness-from-J
    QDD-QCARRIER-DIAGONAL-BOUNDARY   [T, L1]   A_dagger = A_T = v v^T on V_eff;
        both slots stay typed; no central phase
    QDD-INSTRUMENT-APPARATUS         [O, MULTI] physical instrument family,
        separate row, fills no completion-contract field

FOLD OUT (withdrawn from the previous package)
    QDD-BORN-READOUT-MEASURE [D]     no L6 row
    DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION   no physical LOW/HIGH assignment
    GATE-L1-L6-QDD-BORN-READOUT      no gate
    every change to QUADRATIC-DECODER-DATA (registry, normative, frontier,
        prose, dependencies): the row keeps its scope, status O, ROOT/STOP
        program entry, and acquires no edge
```

The record tag of the fifth field is `NORMALIZED`, matching section 6 of the
freeze; the word measure does not occur in the frozen record.

## 2. Files of the package

```text
notes/canon/P-DMATTER-TOTAL-1-INSERTION-PACKAGE-V47.md        this note
notes/canon/P-DMATTER-TOTAL-1-INSERTION-MANIFEST-V47.json     contract manifest, effect_ids UNRESOLVED, contract NOT submitted
notes/canon/CANON-BLOCK-QDD-ROUTE-A.md                        the Canon text block (verbatim fold content)
notes/canon/apply_qdd_insertion_delta.py                      the ledger delta plus checker run
notes/canon/update_status_separation_witness.py               the release-audit update (counts, check 33), called by the delta
notes/canon/finalize_fold_v48.py                              version bump, CHANGELOG, SHA256SUMS, the two release commits, checks
reproduce/qdd-route-a/verify.py, EXPECTED.txt, README.md      the public reproduction bundle (15 checks)
```

## 3. Falsification first

```text
F1  D_QDD_direct and F_QDD o Q_QDD o beta_QDD differ on one of the 15625 checkpoints
F2  a G-self-adjoint idempotent other than E_low has kernel ker Tr_4
F3  the two public reproduction jobs are not byte identical to EXPECTED.txt
F4  tools/check_ledger.py fails on the folded tree
F5  any DEF-QDD-* identifier is stated outside canon/CANON.md (Ruling 1)
F6  effect_ids is filled, the effects requirement is closed, or the contract
    is submitted without a new owner amendment superseding Ruling 2
F7  the value 1/6 enters as input, threshold, normalization or confirmation
F8  a Herm-only claim or a new Sym-slot field appears
F9  the release branch carries more or fewer than two frozen commits, or the
    release-form commit changes anything besides STATUS.md, README.md,
    CITATION.cff
F10 QUADRATIC-DECODER-DATA is modified in any table or prose
```

None of F1 to F10 holds in this package.

## 4. Evidence and re-audit on v47

`reproduce/qdd-route-a/verify.py`, fifteen checks, RESULT 15/15 ALL PASS,
recomputed from scratch on the v47 tree: x86_64 (Ubuntu 24.04, CPython 3.12.3)
and aarch64 (Ubuntu 24.04, CPython 3.12.3), byte-identical stdout. The RUNS
records of the public staged runs and the two public CI jobs on the candidate
commit are the architecture gate; local hashes are audit input only. Checker
lines on the assembled tree are recorded in the pull requests.

## 5. Fold instructions (owner and agent)

```text
1  candidate PR to main: reproduce/qdd-route-a + notes/canon package,
   followed by the two staged RUNS record commits on the same branch
   (candidate_commit = the bundle commit); owner merges without squash
   or rebase
2  release branch from updated main, exactly two frozen commits:
     python3 notes/canon/apply_qdd_insertion_delta.py <checkout>
     python3 notes/canon/finalize_fold_v48.py <checkout>
   (the first rewrites the tree, the second bumps the version, writes the
   CHANGELOG entry and SHA256SUMS, commits the content fold, then writes the
   three activation files and commits the release form)
3  activation PR; owner reviews byte for byte, merges without squash or
   rebase, verifies public readback, tags the merge canon-v48, publishes the
   release assets after tag readback
```

## 6. Scope firewall

```text
CANON CHANGE BY THIS NOTE       NONE
REGISTRY CHANGE BY THIS NOTE    NONE
PROBE / FORMAL RUN              NONE
QUADRATIC-DECODER-DATA          O / STOP, untouched
EFFECT SELECTION                open; effect_ids UNRESOLVED
COMPLETION CONTRACT             not submitted
HYBRID EXTENSION                excluded, no row
SYM SLOT FIELD                  none; QDD-QCARRIER-DIAGONAL-BOUNDARY only
```
