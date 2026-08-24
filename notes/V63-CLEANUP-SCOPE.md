# v63 cleanup scope: owner rulings

Status: **NON-CANONICAL. RECORD OF OWNER DECISIONS.**

```text
recorded    2026-08-24
authority   Public Canon v62, tag canon-v62, CONTENT_COMMIT
            72d7fdaf131f999763bb0904e50e8841245027ff
            mathorn1973/twist-j main ec810acad66ab73631fdfa7e582043e7363eb435
```

v63 is a cleanup fold. It is not a new scientific basis, and the current
authority remains Public Canon v62 until v63 is declared. Two open questions
raised during the cleanup have been decided by the owner and are recorded here
so the decisions survive the session that produced them.

## 1. Issue #374, C-RH-WEIL-NORM-JUNCTION-1-N

**Ruling: content RETARGET, original identifier ABANDONED, no retroactive J7
verdict.**

Two things are separated deliberately.

The *content* is retargeted, because the branch holds work worth keeping: the
Cauchy `K_ray`, the involution model, the determinant chain, the projection
form `S2 - lambda_1`, and several exact no-go results. This is not waste.

The *identifier* is spent. `C-RH-WEIL-NORM-JUNCTION-1-N` froze gates J1 to J8
by reference to issue #374 and never reached its decision bar J7. No `SOURCE`,
`PARTIAL`, `F`, or `STOP` verdict was earned. The branch's own addendum records
the position honestly: "Nothing here proves any one of the resulting
inequalities from the Euler side. That remains the source wall." The branch
still holds three unique files and its basis is Public Canon v46, far behind
current `main`, so resuming it under the same pin is not available either —
`POLICY.md` section 3 forbids reusing, renaming or resuming a sealed probe.

```text
disposition       RETARGET
old identifier    consumed; terminal record Status: ABANDONED
the record must   preserve the candidate results actually achieved
the record must NOT
                  manufacture a J7 verdict after the fact, in any direction
sequencing        write the record only after the abandoned-pin rule of this
                  cleanup has merged, so the record can cite the policy it
                  follows
issue #374        stays OPEN until that accounting closure is merged; close
                  it after, not before
continuation      if the RH direction continues, it starts under a NEW
                  identifier after v63, on the narrower real problem:
                  Euler and prime-side global Stieltjes or Pick positivity.
                  Retargeting does not release the old identifier.
```

`notes/BRANCH-LEDGER-2026-08-24/DISPOSITIONS.tsv` already carries this branch
as `RETARGET` with `abandoned_pin=1`, which is exactly this combination.

## 2. WP5, the three incubation promotion packages

**Ruling: NOT APPLICABLE, dropped from v63. The missing packages are not to be
reconstructed.**

The cleanup audit looked for three packages named in the v63 plan:

```text
PROMO-C-RAPIDITY-GAP-REPULSION-1
PROMO-C-CLASS-BALANCE-SQRT-LADDER-1
PROMO-C-TM-SPLIT-CLASS-CROSS-1
```

None exists. No path matching any of those names has ever been added in any
commit, on any of the 203 refs, anywhere in the full history of this
repository. The claims they would have promoted are real and the rapidity lane
is registered, but the packages themselves are absent.

That is a negative audit result, and it is the finding. It is not an
instruction to build the packages now. Constructing them at this point would
not be folding existing evidence; it would be reconstructing provenance after
the fact and presenting the reconstruction as history. A cleanup fold is the
worst possible place to do that.

```text
WP5 status    NOT APPLICABLE / DROPPED FROM v63
kept          this record, that the expected historical packages were
              searched for and not found
if the origin of those claims is ever genuinely needed, it is a separate
audit or a legacy/ step under its own review, never a promotion package
authored to fill the gap
```

## 3. The closed scope of v63

**Ruling: v63 is hygiene. It is exactly three things and it ends after the
third.**

```text
1  phase A          errata, branch ledger and generator, retention rule,
                    abandoned-pin rule, the disposition table
2  the prune        the 107 MERGED refs, once the ledger is in main to
                    serve as the receipt for what was deleted
3  fifteen records  the abandonment and retarget closures: fourteen
                    branch-level pins plus PREREG-BREAKER-MACKEY4-2
```

Nothing follows point 3. v63 adds no claim, no carrier, no dictionary and no
layer lift; the live `H` and `O` count stays at **30**, and a cleanup fold that
opened new obligations would not be a cleanup.

### The 28 folds are not v63

The disposition table marks 28 refs `FOLD`. None of them lands here. Each goes
**one at a time**, into v64 or later, under ordinary probe discipline: its own
issue, its own pin, its own gate, its own pull request. Folding is how science
enters the Canon, and it does not get to ride in on a hygiene release just
because the accounting happened to touch the same branches.

The 51 `ARCHIVE` refs need no action at all beyond their recorded row.

### What this changes about the records

One consequence is worth stating, because the earlier sequencing assumed
otherwise. The record for `C-RH-RAY-FINITE-WINDOW-CERTIFICATE-2-N` was going
to quote `-3-N` after folding it. `-3-N` is a fold, so it stays unmerged, and
the record instead **cites** it: branch
`notes/c-rh-ray-finite-window-certificate-3-n`, path
`notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N/RESULT.md` section 5, commit
`ce3c7b5cb41f79d0686a600f40534ec411764f6f`, and states the fact directly, that
the pinned wrapper failed on import before the engine ran and was not
repaired. A citation to an unmerged branch is honest; inventing a merge to
make the quotation available would not be.
