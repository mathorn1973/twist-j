# Referee report, lane D (F-watch), lens: evidence and code

```text
STATUS      NON-CANONICAL. Adversarial referee report on lane D of the
            2026-09-15 attack session. Status R. Gates nothing.
DATE        2026-09-15
BASIS       Public Canon v86, tag canon-v86,
            content commit 56068ba4423a2ca38ce5760f1e34e82e2597f99f,
            CANON.md sha256 cfec639d2f952bc8d38f565b5ffc01851e53b39e764e10e95cfb6a1581b11b61
RH          unchanged: open program-level obligation, no status motion
REVIEWS     F-WATCH-2026-09-15.md, verify_f_watch.py, verify_f_watch.stdout
BUILDS ON   ZETA-RH-STATUS-2026-09-08.md sections 1 and 5;
            RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md sections 3 and 7
FILES       REFEREE-LANE-D-EVIDENCE-CODE-2026-09-15.md, rerun.stdout.txt
```

## Falsifiers first

| finding | what kills it |
|---|---|
| R1 rerun identical, exit 0 | a clean-shell rerun of `verify_f_watch.py` whose stdout differs from `verify_f_watch.stdout` or exits nonzero |
| R2 check 5 does not test its label | a reading of lines 83-86 of the verifier under which `n_claim >= 1` distinguishes STOP from `F` |
| R3 CLAIM-ONLY filing contradicts step 4 | a passage in the report making proof-direction claims STOP rather than NONE |
| R4 Fayed "misdate" correction is itself unverified and likely wrong | a reading of the arXiv version history of 2209.01890 showing v4 (2022-11-13) as the last version |
| R5 unreachable-host counts inconsistent | a count of distinct unreachable hosts in the verifier table other than 10 (3 arXiv, 7 other) across 11 attempts |
| R6 verifier certifies a typed table, not the scan | any raw search or fetch record in the lane directory that the verifier reads |

## 1. Verdict table

| claim | lane status | referee verdict | one line |
|---|---|---|---|
| D1-watch-state | R | WEAKENED | the headline (no reachable record of an off-critical zero on 2026-09-15) is consistent with everything I could verify, but the verifier certifies only a hand-typed table, the Fayed date "correction" is unsupported and probably wrong, host counts disagree in three places, and 4 of the 5 CLAIM-ONLY rows are filed STOP against the lane's own step 4 |
| D2 procedure (in the report's falsifier table, absent from the submitted claim list) | R | UNVERIFIED | no check exists for it; completeness relative to the patch falsifier text is a reading, not a test |

Status R is the right label for both; nothing here is overclaimed upward.

## 2. Rerun and code audit (what is CONFIRMED)

- Rerun from a clean shell (`env -i PATH=/usr/bin:/bin LC_ALL=C
  PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_f_watch.py`):
  exit 0, wall time 0.016 s, Python 3.11.15. `cmp` against
  `verify_f_watch.stdout`: identical (sha256 `e4d36b50...cd18` both sides).
  Second run with `PYTHONHASHSEED=12345`: identical.
- Imports: `import sys` only (line 13). No floating point anywhere; no
  `random`; no `Fraction` needed (counts only). The one set, `ALLOWED`
  (line 53), is used for membership only, never iterated into output. The
  printed order is the list order of `SOURCES`. Deterministic.
- Header block present (lines 4-9: STATUS NON-CANONICAL, DATE, BASIS v86,
  RH unchanged). "Falsifiers first" (line 24), verdict table (line 33),
  "What this does not do" (line 204) present.
- Forbidden-string scan: no absolute scratch path, no machine nickname, no
  secret. Every hit on "promot" or "evidence for" is a negation (lines 31,
  38, 91, 126, 214). The only bare `T` is inside the disclaimer sentence
  (line 212).
- Gate: header commit and CANON.md sha256 match `STATUS.md` at v86. The
  lane says it did not rerun the SHA sums (line 22); I did:
  `sha256sum -c canon/SHA256SUMS` OK 5 of 5.
- Network: `curl` to `export.arxiv.org` and `arxiv.org` today answers
  `CONNECT tunnel failed, response 403`; proxy status shows
  `connect_rejected` for both hosts. The block is real. The Cornell export
  mirrors are blocked the same way.
- The three GitHub READMEs, fetched raw today: `vstaln/riemann` carries
  "Record RETIRED (2026-08-24) after external audit" and "No proof of RH
  exists here or is claimed"; `GoldenPhysicsProject/GPPVerify` names
  `rh_of_weil_pairedForm_nonneg` as its flagship conditional statement and
  documents `True := trivial` stubs; `dbsanfte/RiemannGaussian` says "The
  proof is not complete". The lane's characterisations at lines 38, 75-86
  are verbatim-correct.
- Not a duplicate of record: no earlier F-watch or external-claim scan page
  exists in either repository.

## 3. Findings (what is REFUTED or WEAKENED)

F1. `verify_f_watch.py:83-86`. Check 5 is labelled "claims present are
CLAIM-ONLY (STOP, not F)" but its predicate is `n_claim >= 1`. It cannot
distinguish STOP from `F` (that is check 4, line 80-81) and it FAILS on a
clean watch that surfaces no claim at all, which is the desirable state.
The label does not describe the code. The claim-list field
"5 CLAIM-ONLY filed STOP" inherits the mislabel: nothing in the verifier
tests "filed STOP".

F2. `verify_f_watch.py:21-22` versus `F-WATCH-2026-09-15.md:181-185`. The
verifier's vocabulary makes any claim, "proof or disproof", CLAIM-ONLY with
action STOP. Step 4 of the lane's own procedure says an unconfirmed proof
"is not even STOP; it is NONE for the watch". Four of the five CLAIM-ONLY
rows (verifier lines 31, 33, 36, 48) are proof-direction items; only line 32
(Liu disproof) is a disproof claim. Under the lane's step 4 the count should
be 1, not 5, and the four rows should read NONE. The procedure and the
verifier disagree on the closed vocabulary they both claim to fix.

F3. `F-WATCH-2026-09-15.md:40, 115-117` and the claim list. The lane records
a "misdate caught": Fayed 2209.01890 dated 2026-09-09 by one summary,
"corrected" to 2022-09-05 (v1) and 2022-11-13 (v4) by a second summary, and
instructs that the 2026 date "is not repeated". Two searches today return
indexed html and pdf versions of 2209.01890 up to at least v39, with a
summary placing v33 in April 2025 and later revisions in October 2025. So
v4 is not the terminal version, the paper is under continuous revision, and
a 2026-09-09 revision is entirely plausible. The arXiv abstract page is
blocked, so neither the lane nor I can settle the date. The lane's
correction is summary-only, is presented as a fact, and would suppress a
possibly true datum at the next watch. Classification (CLAIM-ONLY) is
unaffected; the recorded "error" is the unverified item.

F4. Host counts. Line 28: "arXiv and nine other hosts were unreachable".
Line 47: "every arXiv host and for eight other publisher or database
hosts". Claim list: six other hosts named (mathlumen omitted). The verifier
table has 11 unreachable attempts on 10 distinct hosts: 3 arXiv hosts and
7 others (export.arxiv.org appears at lines 38 and 50). Check 3's
`total=23` counts attempts, not sources; line 195 calls them "23 sources".

F5. `F-WATCH-2026-09-15.md:49-50`. "The reviewing session of 2026-09-10
recorded 'arxiv.org blocked'" cites no file. The source is `README.md` of
the RH binary-routing review bundle (line 36), which says the session "had
no access to arxiv.org"; it does not record a proxy 403. Uncited and
slightly overread.

F6. `verify_f_watch.py:35`. The query text pins 2609.02882 to "Alpoge
Furman"; the report (lines 40, 113) and today's search agree the author is
Lamzouri. Query strings are data, so no finding flips, but the Alpoge-Furman
result itself is never given an identifier anywhere in the lane files
(line 72), so the T-DIRECTION row for it points at nothing citable.

F7. Evidence gap. The claim's evidence field lists "WebSearch/WebFetch
results and proxy status log recorded in this session". None of these are
in the lane directory. `SOURCES` (verifier lines 27-51) is typed by hand;
all six checks are consistency checks on that typed table. The lane says so
itself (lines 198-201), so this is not an overclaim, but the claim-list
mapping "claim -> verifier_checks" is real only in the bookkeeping sense:
the verifier cannot fail because a scan was wrong.

F8. `F-WATCH-2026-09-15.md:187-189`. Step 5 requires "If arXiv is still
blocked, say so in the first line of the verdict". The verdict table's first
row (line 37) does not; the block appears in row (d) (line 40). The page
does not follow its own procedure on this point.

F9. `F-WATCH-2026-09-15.md:39, 100`. "Gourdon 10^13 (2004)" and the query
"up to height 10^13" conflate a count with a height. From the referee's
recollection (not verifiable today, arXiv blocked): Gourdon's 2004 run
covers the first 10^13 zeros, height about 2.4*10^12, which is below the
Platt-Trudgian height 3*10^12 (about 1.24*10^13 zeros). The lane's
conclusion (not a record) stands, but the item was never a candidate
extension of the record, so "is not a record in the sense of section 3" is
the wrong reason.

F10. Claim mapping. The submitted claim list carries only D1; the report's
falsifier table (lines 28-29) carries D1 and D2; the verdict table (lines
35-41) uses labels (a)-(d) and "watch state" and never mentions D1 or D2.

## 4. Derivations

None. Nothing in the lane or in this report is candidate-T or candidate-C;
no proof is supplied or required. All arithmetic in this report is
counting of table rows, done by inspection and by the rerun.

## 5. What this does not do

- It does not verify, enclose, or compute any zero of `zeta(s)`.
- It does not read arXiv; the version history of 2209.01890 above is from
  search indices and summaries, which are data, not records. F3 says the
  lane's correction is unsupported, not that the 2026 date is right.
- It does not move any row and does not change the lane's status R; it
  weakens the certainty of four sub-statements of D1 and leaves the
  headline (no reachable record found) standing as an R.
- It does not treat the three GitHub READMEs as records of anything beyond
  their own text.
- It does not decide any owner decision of the patch proposal.
