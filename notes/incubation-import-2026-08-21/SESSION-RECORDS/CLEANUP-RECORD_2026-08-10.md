# CLEANUP-RECORD 2026-08-10

```text
ACTION      project doc removal pass, incubation lane
AUTHORITY   none. Housekeeping. No canon, registry, frontier or probe was touched.
BASIS       Public Canon v41, mathorn1973/twist-j main, tag canon-v41
            CONTENT_COMMIT 096e97b44727830102846746f0c723af1c59a2cf
            CANON_SHA256   a15474c4204db637d7ce276ef6ea5dbe94b50af593e46389fd5e77aa16ca80e8
            CANON_BYTES    198932
            canon/SHA256SUMS 5 of 5 OK, verified by clone at HEAD 278b534
BEFORE      395 docs, 4518240 bytes of doc text, knowledge 1652203 bytes
AFTER       201 docs of the inventory, plus 2 written by a concurrent session
            during the pass, plus this record. Knowledge 932255 bytes.
            44 percent reduction in indexed knowledge, 49 percent in doc count.
REMOVED     194, all with a verdict and a reason
BACKUP      TWIST-J_project_archive_2026-08-10.zip, delivered to the owner
            before the first deletion. 194 of 194 archived byte-faithfully
            with MANIFEST.tsv (path, verdict, tier, bytes, sha256, evidence,
            reason).
```

## The premise this pass was opened on, and its falsification

The pass was opened on the reading that most project docs had already reached
the public canon and were therefore redundant. That is false and the numbers
say so. All 395 docs were matched against the clone by content, and 26 have
their substance in the public repo. The public line grew from v24 to v41 in the
same fortnight, but it grew through independently authored public probes, not
through folds of the lanes incubated here. The ballast in this project is not
duplicated publication. It is unfolded work.

That finding changed what the pass could safely do. It could not be a
redundancy sweep, because redundancy accounts for 65 docs. It became a
separation: the project keeps the ledger, the archive keeps the machinery.

## Method

Every doc was staged to disk byte-faithfully, then read and matched against
`mathorn1973/twist-j` main at v41 by eight independent classifier sessions.
Matching was on mathematics, not on filenames: a distinctive equation, rational,
count or threshold sentence pulled from the doc and grepped against the clone.
Naming drift is the norm and matching by id alone would have misjudged most of
the set. The worst case in this pass:

```text
project C-TM-MOEBIUS-1     -> registry MOBIUS-TM-PRIME2-BRIDGE
                              probes/P-MOBIUS-TM-PRIME2-1
project C-FOO-BAR-1        -> registry claim FOO-BAR
project PREREG-C-FOO-1.md  -> probes/P-FOO-1/PREREG.md
```

A shingle-containment pass (7-word windows, every doc against every repo file)
ran first as a cross-check and independently confirmed the low overlap: 12 docs
above 0.85 containment, 378 below 0.20.

Staging fidelity was tested, not assumed. `TWIST_J_Canon_v184_ALL_IN_ONE.md`
staged to exactly 230406 bytes and sha256 `cd92b8bba54658e154e8fc05eb562749f04c70b134dcc728c7236ed10378ef80`,
equal to the byte pin in the project contract. A 24-doc random sample, weighted
to code, was then re-read by an independent session that had not seen the staged
copies: 24 of 24 byte-identical.

## Verdicts over all 395 docs

```text
IN_REPO      26  substance confirmed present in the repo at v41
SUPERSEDED   12  a later revision of the same artifact exists
OBSOLETE     27  plan, status snapshot, run record or fold runbook for work
                 that has since completed
LIVE        246  unfolded work with no repo counterpart
UNIQUE       74  narrative, essay, audit, owner ruling, no repo counterpart
CARRIED      10  the top level docs named by the project contract
```

## What was removed, and under which rule

```text
tier 1, verified redundant                                       59
  IN_REPO 26, SUPERSEDED 10, OBSOLETE 23, minus six holds
tier 2, executable machinery of open lanes                      135
  every .py, .c, .stdout.txt, .diff and .patch carrying a LIVE or
  UNIQUE verdict
--------------------------------------------------------------------
removed                                                         194
  by type: py 119, md 40, stdout.txt 30, c 2, txt 1, patch 1, diff 1
```

Tier 2 is a relocation, not a judgement that the work is worthless. Every one
of those 135 files was flagged SOLE_COPY by its classifier: the repo carries no
verifier for the claim, so the file is the only executable witness its lane has.
It now lives in the archive, indexed by MANIFEST.tsv with its sha256, and the
candidate, preregistration and result docs that cite those hashes all stay in
the project. The pin still resolves; it resolves to the archive rather than to a
sibling doc. This is the same trade the 2026-07-27 pass recorded as its defect 5,
taken deliberately this time rather than as a side effect.

No fired falsifier was removed for having failed. Every doc was judged on
redundancy and currency only.

## The six holds

Docs that matched a removal class and were kept anyway.

```text
PRINCIP-DEKODERU-VAHOVY-ZEBRIK_2026-07-24.md
  classified SUPERSEDED. Held: the 2026-07-27 pass already held it once, its
  successor voids only sections 3 to 6, and sections 7 to 11 survive.
PROMO-C-CENSUS-RETURN-COCYCLE-1.md
  classified SUPERSEDED. Held: the 2026-07-27 pass held it on the ground that
  rows 1 and 2 (MACHINE-INVARIANT-MEASURE-FINITENESS, CENSUS-HULL-ATTRACTOR)
  were never falsified and are carried forward by nothing. Still true at v41.
PROMO-C-FRONTIER-WELLPOSEDNESS-1.md
  classified OBSOLETE, with the classifier flagging it as a judgement call.
  The four owner actions it licensed are done; the census row it proposes is
  not in the repo.
C-DMATTER-DIRECT-1_RUN_2026-07-21.md
  classified OBSOLETE, flagged. It carries sha pins that resolve nowhere in
  the repo and cites break_dmatter_direct_1.py, which exists in neither line.
CANON-v28-CTENARSKA-VERZE_2026-07-30.md
  classified OBSOLETE, flagged. Thirteen versions stale, and the only Czech
  full-canon exposition that exists.
kernel-fold-package-2026-07-18.zip.base64.md
  classified OBSOLETE. Held on a hard rule: it could not be archived, so it
  could not be deleted. Maximum-entropy base64 does not survive a
  language-model copy; two attempts produced silent corruption, exactly as
  the 2026-07-27 pass recorded for three sibling bundles. Its payload may
  also be the sole copy of break_invariants.py, which
  probes/P-KERNEL-CONNECT-ALL-K-1/NOTES.md states was retained privately.
```

## Two things a later session must know

```text
1  verify_wall_li2_rung.py was held by name in the 2026-07-27 pass because its
   rational-interval enclosure witness (Machin pi, Newton sqrt, ln(phi) series,
   Fibonacci-majorant tail bounds, width below 1e-15, no floats) exists nowhere
   in the repository. It is still the only copy. It was moved to the archive
   under the tier 2 rule rather than held a second time, because the owner
   chose that rule knowingly. It is in the zip; it is not in the project.
2  A concurrent session was working in this project while the pass ran. It
   created BUILD-JAM-MCP-AUDIT_2026-08-10.md and
   POSTREVIEW-ANALYTIC-STATUS-C-TM-MOEBIUS-1.md and rewrote four TM-MOEBIUS
   docs after this pass had staged its copies. Those six docs were not touched.
   The TM-MOEBIUS verifiers, breakers and transcripts were removed to the
   archive under tier 2 while that lane was live. If that session still needs
   them, every one is in the zip with its sha256 and can be restored byte
   faithfully.
```

## Findings, not actions

Surfaced by the classifiers while matching against v41. Each needs an owner
decision and none was touched by this pass.

```text
1  canon/CANON.md line 2401 and data/EXTERNAL_SOURCES.tsv still pin
   SRC-CODATA-2018-MUON while the book lane uses CODATA 2022.
2  canon/CANON.md line 3194 carries an unlabelled claim, that the Fibonacci
   category with central charge c = 14/5 is mathematical background, inside a
   hashed normative file with no backing registry row. Raised first in
   CLOSING-SLATE_2026-07-27 tier 4 item 6, still open.
3  CENSUS-HOSTING [C] and COLOR-RETURN-D5 [T] state the return group of order
   10 on the coarse symbolic quotient with no scope note. The project's
   oriented-census lane records that D_5 is the monodromy of the coarse
   quotient while C_5 is the return group of one oriented cell, and proposes
   registering the qualifier. The repo carries no such note.
4  DEPOSIT-C-TM-MOEBIUS-1.md is out of sync with PAPER-tm_moebius.tex: the
   deposit sheet still carries the pre-rebuild title and file list.
5  Contract open decision 3 confirmed still open at v41. None of the five
   packaged lanes has moved publicly.
6  Contract open decision 4 is half done. CO_TWIST_DOOPRAVDY_JE_SYNTEZA2 dated
   2026-07-30 already carries Tr(C^2) = -881/8 with -21/8 recorded as [F]. The
   2026-07-19 sibling still asserts -21/8 and is still in the project.
7  C0-PATCH_ESSAY_UNIVERSE_ELEMENTAL_2026-07-30.md is an unapplied patch. Its
   target, ESSAY_UNIVERSE_ELEMENTAL_DRAFT_2026-07-19.md, still carries both
   the byte-exact anchors and the falsified -21/8 value.
```

## Falsifier for this record

This record is wrong if any doc listed as removed is found in the project, if
any doc listed as kept is absent, if any archived file's sha256 differs from its
MANIFEST.tsv row, or if any doc removed under tier 1 has no counterpart at the
repo path or claim id its manifest row names. The post-pass state was verified
by set difference against the removal list.
