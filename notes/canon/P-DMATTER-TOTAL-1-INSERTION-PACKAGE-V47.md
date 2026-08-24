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
                           its D-promotion package is withdrawn), the first
                           conservative candidate PR #385 (closed unmerged;
                           four defects listed in section 0) and the second
                           conservative candidate PR #386 (closed unmerged;
                           the transitive firewall blocker in section 0)
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

Second audit, 2026-08-15, PR #385. The owner stopped the first conservative
candidate over four defects; all four are fixed in this package by
construction.

Defect 1, stale manifest pins. The contract manifest carried the withdrawn
package's integrity values. It now pins the renamed verifier
(`fbd1da8b9945033ad03794c9960341a457640d636929c9b3a030e0898b0fb464`) and the
conservative bundle
(`897f18e27e822a96ece61048cb17d4a5488b267d014f2bb10787f1a56edc8c6a`); no
`5214ebdb` or `0511f528` value remains anywhere in the package.

Defect 2, stale finalizer text. The finalizer's status-separation README
sentence described the withdrawn variant (246 claims, 11 gates, an L6
DICTIONARY_LIFT gate). It now describes the conservative fold with counts
computed from the folded tree at run time, states that the CENTRAL, CM-2I
and J-SEAM checks are unchanged and keep reading QUADRATIC-DECODER-DATA as
an open obligation, and requires the absence of any Born-readout row,
effect-selection bridge or L1-L6 gate.

Defect 3, `git add -A`. Both release commits now stage explicitly named
paths: the fold commit stages only files on a fixed allowlist and aborts on
any unexpected modified path, and the release-form commit requires the
changed set to equal exactly STATUS.md, README.md and CITATION.cff.
`git add -A` does not occur in the package.

Defect 4, fail-open checks. Every decisive step now aborts with a nonzero
exit on failure: the delta runs the witness, the view generator,
check_ledger and check_status_labels fail-closed; the finalizer runs
check_policy, unittest, check_canon, check_ledger and check_status_labels
fail-closed BEFORE the fold commit, verifies the regenerated v48 counts
block, and runs check_activation --full after the release-form commit,
aborting with DO NOT PUSH on failure.

Third audit, 2026-08-15, PR #386. The owner found a forbidden transitive
path in the future ledger, DEF-QDD-DIRECT-WRITE -> DEF-QDD-MATTER-RECORD ->
DEF-QDD-BRANCH-WEIGHT-PAIRING -> DEF-QDD-PROJECTOR-LOW/HIGH, all REQUIRES,
against section 6 of the DICTIONARY-DIRECT owner amendment (the direct
branch may use MatterData_QDD as a pure schema only; its definitional
closure must not continue into BornPair_QDD, Q_QDD, the projectors or a
helper unfolding through them). The manifest sourced total_weight,
branch_weights and normalized_weight_state from
DEF-QDD-BRANCH-WEIGHT-PAIRING and density_state from DEF-QDD-QPAIR while
naming DEF-QDD-DIRECT-WRITE as the write map, the uncorrected point 2 of
AUDIT-QDD-BINDING-PACKAGE-V27, and the falsifier of
QDD-ALGEBRAIC-FACTORIZATION would have fired on the fold itself. All fixed
by construction in this package:

1. DEF-QDD-MATTER-RECORD is a pure type schema (types, tags, branch order,
   ZERO branch; no computation rule); its only ledger edge is a typing edge
   to DEF-QDD-COEFFICIENT-Q.
2. The cyclotomic formulas moved out of DEF-QDD-BRANCH-WEIGHT-PAIRING into
   DEF-QDD-DIRECT-WRITE, so all five direct-branch fields are sourced
   through R_cyc alone; the manifest now carries every field on
   DEF-QDD-AMPLITUDE-B0 with source and write map DEF-QDD-DIRECT-WRITE. The
   verifier already computed this way (R_cyc uses field arithmetic, the
   trace pairing, lambda_B and MATRIX_B0 only; G and the projectors appear
   only in F_QDD), so verify.py, EXPECTED.txt and the bundle hash are
   unchanged.
3. DEF-QDD-BRANCH-WEIGHT-PAIRING keeps only the factor-route Born pairing
   and is marked a factor-branch helper; DEF-QDD-GRAM likewise.
4. The transitive closure of DEF-QDD-DIRECT-WRITE is enforced twice: a
   fail-closed step in the insertion delta aborts before the dependency
   table is written if the closure differs from exactly {domain, balanced piston,
   amplitude, coefficient data, trace pairing, LOW LINE, record schema} or
   touches a factor-side object, and the new thirty-fourth
   status-separation check QDD-DIRECT-FIREWALL enforces the same set
   permanently on the public ledger.
5. Ledger counts recomputed on the folded tree (claims 245, items 280,
   dependencies 425, gates 10); this pull request is a new clean candidate
   pin with new two-architecture RUNS and new public CI.

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
