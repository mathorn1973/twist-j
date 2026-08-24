# CLEANUP-RECORD 2026-07-27

```text
ACTION      project doc removal pass, incubation lane
AUTHORITY   none. Housekeeping. No canon, registry, frontier or probe was touched.
BASIS       Public Canon v24, mathorn1973/twist-j main, tag canon-v24
            CONTENT_COMMIT bee0f1bfe421d6dbd599b6625e077ef08f03fb4c
            CANON_SHA256   2511e68c949d471b00d26bb94f23fab9056c2cbb3cc2b9d976c77d276ba02742
            canon/SHA256SUMS 5 of 5 OK, verified by clone
BEFORE      278 docs, 1600313 bytes of knowledge
AFTER       103 docs, 543454 bytes. 66 percent reduction.
REMOVED     175, all with a verdict and a reason
BACKUP      TWIST-J_project_archive_2026-07-27.zip, delivered to the owner.
            172 of 175 archived byte-faithfully with MANIFEST.tsv
            (path, verdict, bytes, sha256, reason). 3 recorded, not archived.
```

## Method

Every one of the 278 docs was read and matched against the public repository
head by claim id, by probe path, by registry row text, and by SHA-256 where a
pin was recorded. Each doc received exactly one verdict. Naming drift between
the two lines was resolved by hand: project `C-FOO-BAR-1` lands as registry
claim `FOO-BAR`, project `PREREG-C-FOO-1.md` lands as `probes/P-FOO-1/PREREG.md`,
project `OWNER_VERDICT_<topic>_<date>.md` lands as `notes/verdicts/OWNER_VERDICT_<n>_<date>.md`.
Matching by id alone would have misjudged several.

```text
IN_REPO     101  substance confirmed present in mathorn1973/twist-j
SUPERSEDED   35  a later revision of the same artifact exists
OBSOLETE     39  session seed, status snapshot or fold runbook for work
                 that has since completed; pinned to a state long past
--------------------
removed     175

LIVE         74  unfolded work not in the repo, kept
UNIQUE       24  narrative, essays, audits with no repo counterpart, kept
HELD          5  matched a removal class, held anyway on inspection
--------------------
kept        103
```

No fired falsifier was removed for having failed. Failure is first-class
evidence in this program and every doc was judged only on redundancy and
currency. `F-CENSUS-ERGODIC-BIJECTION-313.md` stands.

Two docs created by a concurrent session during the pass
(`AUDIT-EXTERNAL-PHOTON-FERMAT-NOTE_2026-07-27.md`, `break_photon_fermat.py`)
were outside the inventory and were not touched.

## The five HELD docs

Docs that matched a removal class and were kept anyway because inspection
found sole-copy content in them.

```text
C-CENSUS-ORIENTED-ERGODIC-625-1-RESULT-AND-PROMO.md
  the only copy of the proposed registry row texts for the live 625 lane
  (CENSUS-CONTEXT-DECOMPOSITION, CENSUS-MIRROR-QUOTIENT,
  CENSUS-COARSE-RETURN-MONODROMY, CENSUS-SEED-MASS-UNIFORM). The -2 and -3
  docs are titled RESULT only and do not carry them.
PROMO-C-CENSUS-RETURN-COCYCLE-1.md
  its row 4 (313) is falsified, but rows 1 and 2
  (MACHINE-INVARIANT-MEASURE-FINITENESS, CENSUS-HULL-ATTRACTOR) were never
  falsified, are not in the repo, and are not carried forward by the 625 promo
ZAPORNY_SVET_NADHLED_2026-07-19.md
  its successor carries an explicit instruction that it is not to be deleted:
  it stands as the archive of two fired falsifiers
PRINCIP-DEKODERU-VAHOVY-ZEBRIK_2026-07-24.md
  marked archive, do not edit; byte b19d33de was independently audited
verify_wall_li2_rung.py
  the claim folded with evidence inline, but the rational-interval enclosure
  witness (Machin pi, Newton sqrt, ln(phi) series, Fibonacci-majorant tail
  bounds, width below 1e-15, no floats) exists nowhere in the repository
```

## The three docs recorded but not archived

Three base64-wrapped git bundles could not be transcribed faithfully.
Maximum-entropy base64 does not survive a language-model copy: two attempts
produced silent corruption inside the first fifteen payload lines, and a
corrupted bundle is worthless rather than degraded, so nothing was written
rather than something that looks complete and is not. Removal was confirmed by
the owner on that basis.

```text
incubation-c-li-cocycle-1.bundle.base64.md
incubation-consolidation-li-lane.bundle.base64.md
incubation-consolidation-li-lane-2.bundle.base64.md
```

Their payload files are all on repo main under `notes/C-LI-COCYCLE-1/`,
`notes/C-PENTAGON-WEIL-1/` and `notes/C-WEIL-REALIZATION-1/` at equal or later
revision. Only the git history wrapper is gone, and repo
`notes/C-LI-COCYCLE-1/C-LI-COCYCLE-1.md` section 12 records that the local
commit `aee7a376` and its parentage were not preserved, by design.

## Defects found during the pass, not fixed here

These are findings, not actions. Each needs an owner decision.

```text
1  INSTRUCTIONS STALE. The project instructions name Public Canon v10. The
   head is v24. Step 0, the currency gate, literally orders a session to
   "Confirm STATUS.md reads CANON Public Canon v10", which no longer holds.
   Every new session runs that gate first. This was already flagged in
   NADHLED-V20-PROGRAM-STATE_2026-07-24.md and is still open.
   Recommended: drop the version integer from the contract and pin only
   "mathorn1973/twist-j main, whatever STATUS.md reads".

2  INSTRUCTIONS, MATH. The carried-files list states
   "SS98_polylogarithm_bridge.md  the polylogarithm bridge, Li_2(J) = pi^2/100".
   That is false as a complex equality; Im Li_2(J) is not zero. The public
   registry row is correctly fenced to Re. The contract line is not.

3  INSTRUCTIONS, FILENAME. The manifest is stored as
   "TWISTJ_Verejny_manifest_v2_CZ (1).md", a duplicate-upload name. The
   instructions reference the clean name. There is no clean-named sibling,
   so this single copy is authoritative despite the suffix.

4  DEAD NUMBER IN A LIVE EXPOSITION. CO_TWIST_DOOPRAVDY_JE_SYNTEZA2 section 3
   asserts Tr(C^2) = -21/8. The registry records CURVATURE-TRACE-VALUE [F]:
   that exact value is falsified, the true value is -881/8 with dim V = 818
   (CURVATURE-HISTORICAL-TRACE [T]). This is the head of the Czech exposition
   lane and the doc a reader reaches for. It needs a correction, which is why
   it was kept rather than removed.

5  PINS THAT NO LONGER RESOLVE IN-PROJECT. Several kept PROMO docs pin
   verifier files by SHA-256 that were removed as IN_REPO or SUPERSEDED. The
   pins remain valid as records and every file is in the archive with its
   hash in MANIFEST.tsv, but the bytes are no longer one project doc away.

6  PRE-AXIOM DOC ON THE REFERENCE SURFACE. Thue_Morse_Phi_Computation_Guide.md
   is on the carried-files list so it was kept, but it predates the axiom,
   never mentions J = 1 + zeta_5^2, cites the retired program name, is
   float-first against current canon style, is stored as UTF-8 mojibake, and
   is the only carried doc that puts the real-name link and a contact line in
   the body. Keep, correct, or drop from the contract.

7  LANES OPEN WITH NO PUBLIC MOVEMENT. Worth an owner ruling on each: fold,
   retire with an F, or re-target.
     C-ENTROPY-RESIDUE-1        6 proposed rows, targeted Canon v2, zero hits
                                anywhere in the repo at v24
     PROMO-J-LI-*  (4 docs)     all target a v6 to v7 fold that never happened;
                                their three verifiers exist nowhere in the repo
                                (82 repo .py files hashed, no match)
     C-C8-BILINEAR-SHADOW-1     both probes are in the repo, -2 passing 6 of 6,
                                but no registry row exists at v24
     C-COLOR-MEASURE-DIM-1      targets Canon v5; v22 retyped the parent to a
                                much stricter STOP surface. Needs rebasing
                                before folding, not folding as written.
     C-KERNEL-SUBSET-LANDSCAPE-1  proposed rider row KERNEL-CONNECT-MINIMAL-SET
                                appears in no repo file; carries a first-class
                                fired falsifier (5^(k(6-dim U_S)) lower bound,
                                25 claimed, 2 measured by exhaustive union-find)
```

## Falsifier for this record

This record is wrong if any doc listed as removed is found in the project, if
any doc listed as kept is absent, or if any archived file's SHA-256 differs
from its MANIFEST.tsv row. The post-pass state was verified by set difference
against the plan: zero docs survived that should have been removed, zero were
removed that should have been kept.
