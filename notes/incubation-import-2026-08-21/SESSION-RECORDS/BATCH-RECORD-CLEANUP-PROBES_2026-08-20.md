# BATCH-RECORD: cleanup probes for the consolidation fold, 2026-08-20

NON-CANONICAL. Batch execution record, no authority. Owner order: the
background cleanup (audit plan Faze 5 folds) and the DE-W arming in ONE
sealed fold; precedent v53 (one fold, nine rows, three probe families).
Structure: one public probe per package first, then a single fold
consuming all merged probes.

## The four probes, all established today

```text
1  P-PENTAGON-ONLY-DILATIONS-1     issue #445, pin a9ef097e, PR #446
   6/6 PASS. Deficiency (1/12)(1 - 1/q^2) constant in tower height,
   best approximant (1/q) g_1, Gram re-derived by independent exact
   integration. Rows: J-LI-PENTAGON-DILATION-DEFICIENCY [T],
   PENTAGON-ONLY-DILATIONS [F]. CI: both architectures PASS.
2  P-J-LI-CARRIER-NOGO-1           issue #447, pin 5d84bc93, PR #448
   6/6 PASS. No finite-dimensional cyclic carrier for the Li ladder;
   exemplars exact in Q(zeta_10) = Q(zeta_5), remainder bound
   6 + 2 sqrt5 attained. Row: J-LI-CYCLIC-CARRIER-DIMENSION [T].
   CI: both architectures PASS.
3  P-KERNEL-SUBSET-LANDSCAPE-1     issue #449, pin 5613256f, PR #450
   7/7 PASS. Exact 32-entry dim U_S table; connectivity iff
   dim U_S = 6; connected subsets exactly acde and abcde; the lane's
   fired lower-bound clause honored and not asserted. Row:
   KERNEL-SUBSET-LANDSCAPE [T]. CI: both architectures PASS.
4  P-ENTROPY-RESIDUE-MATH-1       issue #451, pin 740dd83f, PR #452
   8/8 PASS. Toral entropy 2 log phi by exact Z[phi] factorization;
   #Fix(T^15) = 1860496 by two exact paths; TM driver entropy zero
   (p(20) = 60, stabilized); residue bracket [log(phi^2/2), 2 log phi]
   with strict floor 1/phi. Rows: J-TORAL-ENTROPY [T],
   TM-ENTROPY-ZERO [T], BINARY-READ-RELATIVE-ENTROPY [T].
   CI: was pending at record time; see the PR.
```

Every probe: fresh public files, issue claim before commit, pin before
the single formal execution (candidate files smoke-executed pre-pin,
disclosed; all probes result-exposed), formal leg from a clean checkout
at the pin (Ubuntu 24.04.4 x86_64, CPython 3.11.15, sealed environment,
exit 0, empty stderr), EXPECTED.txt byte-exact, RUN.md machine-readable,
commits as A. M. Thorn.

## Deferred from the batch

C-COLOR-MEASURE-DIM-1 stays deferred: its carrier objects (the 24
orbits and 16 observable types) are not registered at v54 (grep witness;
the parent COLOR-MEASURE-SELECTION [O] scope now speaks of the 2I-core
L4-to-L6 lift). The rebase is derivation work, not bookkeeping. The
dimension-15 nonselection content remains queued for its own probe after
a rebase onto the current carrier, per CLEANUP-RECORD_2026-08-19.md.

## The consolidation fold v(next), plan

One sealed fold consuming five merged probes:

```text
P-DE-W-ARMING-1 (merged in PR #443)   DE-W-CONSTANT [H]  (variant B
                                      falsifier, frozen in that PREREG)
PR #446                                J-LI-PENTAGON-DILATION-DEFICIENCY [T]
                                       PENTAGON-ONLY-DILATIONS [F]
PR #448                                J-LI-CYCLIC-CARRIER-DIMENSION [T]
PR #450                                KERNEL-SUBSET-LANDSCAPE [T]
PR #452                                J-TORAL-ENTROPY [T]
                                       TM-ENTROPY-ZERO [T]
                                       BINARY-READ-RELATIVE-ENTROPY [T]
```

Signed ledger delta: claims 279 + 8 = 287; T 165 + 6 = 171; H 2 + 1 = 3;
F 15 + 1 = 16; D, C, O unchanged; live 26 + 1 = 27 (DE-W-CONSTANT is the
only new live row; one new frontier entry, one program-table row, mode
EMPIRICAL). Exact row texts are frozen in the five PREREG files; canon
paragraphs per those files (sections 2, 3, 16, and the cosmology
passage).

Remaining steps: (1) owner merges PRs #446, #448, #450, #452 (no squash,
no rebase; #452 after its CI is green); (2) on the owner's go, build
release/canon-v(next) per the release procedure (exactly two frozen
commits: the content fold, then the release form changing exactly
STATUS.md, README.md, CITATION.cff), full checker suite and activation
dry run before any push; merge and tag stay with the owner.

## Falsifier for this record

Wrong if any listed pin, hash, issue, or PR number fails readback, or if
any listed proposed row text differs from the corresponding PREREG.
