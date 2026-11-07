# TWIST-J unmerged-work ledger, 2026-11-07

NON-CANONICAL. Read-only audit input for the owner's cleanup. Nothing was pushed, closed, merged, labelled or deleted.

```text
base            origin/main d4d36372 (Public Canon v109; last merge PR #1923)
remote heads    364 after the second fetch (363 at the first fetch + ccr-674ed817-vstfzn, PR #1952)
ledger tool     tools/build_branch_ledger.py (full clone, not shallow)
states          BASE=1 DIVERGENT=343 MERGED=19 ORPHAN=1
open PRs        216 (215 listed + #1952 opened during this audit); all 216 heads are DIVERGENT
note            #1952 (this consolidation) kept moving during the audit (1bdaa2d2 -> 0456ca92); its row is indicative only
files           PR-LEDGER.tsv (one row per PR), BRANCH-LEDGER.tsv (tool output), this file
```

## How recommendations were assigned

- **MERGE-CANDIDATE** when at least one holds. **M1**: it closes an obligation (ABANDONED pin, completed FAIL, completed INCONCLUSIVE run, failed-audit or STOP disposition). **M2**: merged work on main, or `canon/CANON.md` itself, already relies on this PR's exact head as a source or premise (vendored bytes, SOURCES/PREREG entries, commit-pinned links). **M3**: a complete result with an acceptance review on record (V104 release review M/E, V106 ACCEPT, or an independent review PR with PASS).
- **SUPERSEDED**: the content is on main (byte-identical files, or main explicitly records it as consolidated or folded inline) or is strictly contained in a newer PR. The successor is named.
- **DUPLICATE**: not used. No two open PRs touch the same probe or note directory. The only overlap is the stacked field-L5 chain, recorded as SUPERSEDED.
- **STALE-HARVEST**: complete but unreviewed, untouched for more than 7 days, no dependency on main. Sealed probe records in this class (column `obligation` = `sealed completed probe record`) should eventually be merged as records rather than closed, because their identifiers are spent.
- **KEEP-ACTIVE**: touched since 2026-10-31 by real work, or part of a live chain.
- Closing a PR never licenses deleting its branch: every PR head is DIVERGENT and AGENTS.md section 5a forbids deleting it.

## Counts

| recommendation | PRs |
|---|---|
| MERGE-CANDIDATE | 78 |
| SUPERSEDED | 15 |
| DUPLICATE | 0 |
| STALE-HARVEST | 103 |
| KEEP-ACTIVE | 20 |
| total | 216 |

Obligation column: sealed completed probe record: 44; ABANDONED pin disposition (merge to close obligation): 6; notes-level failed-audit disposition: 5; completed INCONCLUSIVE sealed record: 2; completed FAIL / fired falsifier (merge, never relabel): 2; notes-level STOP disposition: 2; notes-level INCONCLUSIVE record: 1.

Other facts: 166 drafts; 2 conflict with main (#1276, #1828), all other 214 merge cleanly with `git merge-tree`; 95 are more than 500 commits behind main and 29 are within 50; 103 are cited from main (by PR number or by a commit unique to the PR), 71 of them by merged work or Canon rather than only by release-review notes, and 4 (#1746, #1761, #1764, #1766) by commit inside canon/CANON.md itself. Every MERGE-CANDIDATE was test-merged into d4d36372 in a temporary local worktree: all 78 merge cleanly and every merged tree passes tools/check_policy.py; the first 11 tested also pass check_canon.py and check_ledger.py (column check_policy_after_merge). Note that #1639, #1644, #1658, #1596, #1608 and #1791 still need the review errata or corrections named in the evidence column.

| lane | PRs | MERGE | SUPERSEDED | HARVEST | ACTIVE | lines added |
|---|---|---|---|---|---|---|
| L01 contact-work-clock | 9 | 1 | 0 | 0 | 8 | 18421 |
| L02 pole-height | 8 | 2 | 0 | 0 | 6 | 10215 |
| L03 collatz-relative-contact | 9 | 5 | 0 | 0 | 4 | 13322 |
| L04 dirac-contact-scattering | 10 | 0 | 0 | 10 | 0 | 9280 |
| L05 bound-pair-capture | 4 | 0 | 0 | 4 | 0 | 17109 |
| L06 native-memory-clock | 4 | 1 | 0 | 3 | 0 | 6511 |
| L07 j-carry | 2 | 2 | 0 | 0 | 0 | 5526 |
| L08 source-energy | 6 | 3 | 0 | 3 | 0 | 9081 |
| L09 thermal-clock-preparation | 15 | 9 | 0 | 6 | 0 | 24930 |
| L10 hodge | 7 | 0 | 3 | 4 | 0 | 14445 |
| L11 j-reading | 5 | 0 | 0 | 5 | 0 | 7284 |
| L12 integer-gravity | 14 | 14 | 0 | 0 | 0 | 37926 |
| L13 v104-phase-contact-intake | 15 | 14 | 0 | 1 | 0 | 20520 |
| L14 hb-two-use | 7 | 7 | 0 | 0 | 0 | 10056 |
| L15 v100-matter-photon-endpoint | 17 | 5 | 0 | 12 | 0 | 24845 |
| L16 v100-review-drafts | 3 | 0 | 3 | 0 | 0 | 6792 |
| L17 photon | 22 | 8 | 0 | 14 | 0 | 24618 |
| L18 ion-ls | 8 | 1 | 0 | 7 | 0 | 11725 |
| L19 field-l5-work-record | 10 | 1 | 5 | 4 | 0 | 47872 |
| L20 j-memory-ramified | 5 | 3 | 0 | 2 | 0 | 3689 |
| L21 rh | 12 | 0 | 0 | 12 | 0 | 19241 |
| L22 misc-older | 14 | 1 | 0 | 13 | 0 | 15408 |
| L23 infra-docs | 10 | 1 | 4 | 3 | 2 | 3230 |

## Most important findings

1. **Open obligations sitting in open PRs.** All 8 ABANDONED/FAIL formal-probe records are in the integer-gravity lane and unmerged: ABANDONED #1636, #1637, #1638, #1656, #1672, #1673; FAIL #1643, #1657. Policy says these close only when merged. Also unmerged: completed INCONCLUSIVE probes #1787 and #1789; notes-level failed audits #1166, #1174, #1175, #1180 and #1302; STOP dispositions #1596 and #1629; INCONCLUSIVE diagnostic #1211.
2. **Open obligations with no PR at all** (DIVERGENT branches): pinned and never run, `probe/P-INTEGER-LOCAL-PARENT-CLOSURE-1` (#1659, pin 10a4c4d8) and `probe/P-U-J-HODGE-SEPARABLE-COUNTER-READ-1` (lock #1069, pin 51672be0). An ABANDONED record written but never merged: `probe/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1`. Negative audit records: `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` (PARTIAL/STOP) and `-AUDIT-2` (SCIENTIFIC_FAIL). Possibly also `probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2` (pin commit, no result; the owner must confirm whether the pin was public).
3. **Main depends on unmerged heads.** Canon v106 text links #1746/#1761/#1764/#1766 by commit. Merged v104/v108/v109 probes cite or vendor #1639, #1644, #1646, #1648, #1658, #1857, #1819 and #1821. Merged #1923 builds on #1908, #1912 and #1915. Merging these restores custody inside main.
4. **Largest overlap clusters** (none are true duplicates): the field-L5 stack #1310-#1319 (v96 folded it inline; up to 46 shared blobs); integer-gravity retry chains (K1 bridge 1-4, second-order 1-3, reciprocal 1-2, Maurer-Cartan 1-2 with -3 merged); photon N/N2 retries (#1166->#1167, #1180->#1181, #1174->#1175 then N3 on main); the thermal preparation chain #1756->#1766; Hodge #1721/#1723/#1726, which main explicitly consolidated; the three v100 review drafts #1388-#1390, now byte-carried by merged probes.
5. **Live work**: L01 contact-work-clock and L02 pole-height (17 PRs, all from 2026-11-03..07) plus the Collatz notes. Merging #1908, #1912 and #1915 is urgent because #1923 already relies on them.

## Lane syntheses

Status words are quoted as the PRs state them. "candidate-T/C" are the PRs' own
non-canonical labels, not registry statuses. Nothing here promotes anything.

### L01 contact-work-clock (9 PRs: #1892 #1894 #1910 #1915 #1917 #1919 #1930 #1942 #1950)
- Live lane, all touched 2026-11-03..07. #1915 proves the native paired phase (+e_k/-e_k set by the parity of v_2(k)) and a sharp bounded-work obstruction; merged #1923 (C-COMMON-COUNTER-PATH-PHASE-N) already builds on it.
- #1910 gives a conditional common contact action, work bank and returning clock with a stated "remaining selection debt"; #1917 composes two overlapping contacts under one Hamiltonian (candidate-T, finite audit PASS, 2-arch gate pending).
- #1892 PASS_IN_FROZEN_SCOPE (latched receiver) and #1894 C (modal action, no falsifier) on the neutral ring; #1950 COMPLETE piston-Gram non-descent with sharp 16/8 completion.
- #1930 loaded-current compatibility (55,950 assertions, aarch64 byte-identical) has an independent review #1942: no error, but every scope needs corrections before Canon wording.
- No duplicates. #1919 explicitly defers to #1908/#1912 instead of re-proving them.
- Next step: merge #1915 now; run the 2-arch workflow on #1910/#1917/#1950; write one #1923-style consolidation folding #1910+#1917+#1930 (with #1942 corrections)+#1950.

### L02 pole-height / 322-contact loader (8 sealed probes: #1896..#1912)
- Chain: #1896 SEARCH_NOT_FOUND (bounded non-finding) -> #1898 odd inputs cannot reach the target in the six-slot contract -> #1900 catalytic neutral-stock witness plus orientation obstruction -> #1902 common odd-input word, 124 exclusions, five-input word not found -> #1904/#1906 complete zero orbit (1556 states), INCONCLUSIVE -> #1908 PASS fixed 322-contact five-input loader -> #1912 COMPLETE: succeeds exactly for t in {-2..2}.
- #1908 and #1912 are already relied on by merged #1923 (WORD.txt byte-identical).
- No duplicates (#1904/#1906 share one helper blob; #1908/#1912 share WORD.txt by design). No ABANDONED pins; every probe completed.
- Risk of misreading: #1898's no-go is scoped to its own contract; #1908's witness is in a later, different contract.
- Next step: merge #1908 and #1912 first (main depends), then the six search records in order, one PR each with merge commits; add a one-page index mapping each probe to its contract.

### L03 Collatz / relative-contact source renewal (9 PRs: #1857 #1859 #1862 #1864 #1865 #1867 #1869 #1880 #1889)
- #1857 PASS (ten-input variable-arrival apparatus) is the byte source of WORD535.txt in merged P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1 (v108).
- #1862 (contact Collatz step, two depth records) and #1865 (affine numerator cascade) each have an independent blind review PASS WITH NOTES (#1880, #1889); their heads are cited by merged probes.
- #1859 (blocks, carries, inverse memory), #1864 (odd-head return map), #1867 (four-chart renewal bounds), #1869 (funded two-pass renewal): candidate-T plus candidate-C replays, unreviewed.
- Duplicates: none; reviews pair with their targets.
- Next step: merge #1857 and the two reviewed pairs; fold #1859/#1864/#1867/#1869 into one Collatz-contact synthesis with a single review.

### L04 Dirac contact and scattering (10 PRs, 2026-10-26..30, all STALE-HARVEST)
- Positive constructions: finite rotor clock (#1795), triad bound states plus resonance (#1799), exact four-channel point-contact S matrix and pole sheets (#1800), pair emission with a gap-2 and a gapless quadratic channel, "not a Weyl particle" (#1801), finite coherent Dirac source (#1804), unwrapped kinematic reference (#1835), prime two-body channel selection (#1837), W P=0 scattering with transparent fifth-root phase (#1841).
- Fired routes: Dirac chart obstruction for the prime elastic contact (#1839); nominated normalized Dirac W total REJECTED (#1843).
- V106 marked #1795/#1804 FOLLOWUP and #1799/#1800/#1801 OUTSIDE_CORE. No independent review in the lane.
- Next step: one consolidated Dirac-contact note recording the eight constructions and two rejections, reviewed once; then the standalone drafts can be closed (branches kept).

### L05 bound-pair capture (4 PRs: #1813 #1815 #1817 #1823)
- #1813 C, both architectures (relative capture profile enclosed); #1815 CERTIFIED absolute capture bound; #1817 CERTIFIED 130-condition resolvent audit; #1823 four manuscripts for the finite-time bound, acceptance pending.
- Three sealed probe records and one manuscript note, no review, no main dependency.
- Next step: one independent review of #1815/#1817 (and the #1823 manuscripts), then merge the three probe records.

### L06 native memory and finite clock (4 PRs: #1825 #1827 #1829 #1831)
- #1831: unchanged native U implements one-shot q-controlled swap/hold on all 50 preparations, audits PASS on two architectures; it is a declared source of merged C-J-INTEGRAL-RELATIVE-CONTACT-N.
- #1825: a permanent one-shot record and a memory-changing preparation both exist, but their conjunction in one reusable receiver does NOT follow. #1827 finite source/clock/archive (review PASS). #1829 relational model with a 561-level reference clock.
- Next step: merge #1831; harvest the other three into one relational-clock note.

### L07 J carry arithmetic (2 PRs: #1819 #1821)
- Reversible all-N J multiplier (#1819) and carry moments (#1821), both candidate-C plus proof.
- Both are declared sources of merged v109 P-NATIVE-RECEIVER-CARRY-MIRROR-1; its review (E5) flags that the sources sit on unmerged PRs. The compiler is vendored byte-identically.
- Next step: merge both.

### L08 original-source energy (6 PRs: #1781 #1783 #1785 #1787 #1789 #1791)
- Analytical: finite occupation energy bridge (#1781), refined bound with cut mass <= 512*eta (#1783), nearest-neighbour energy action ruled out (#1785). All V106 OUTSIDE_CORE.
- Probes: #1787 INCONCLUSIVE and #1789 INCONCLUSIVE (V106 PRESERVED_PREDECESSOR), then #1791 CERTIFIED_OBSTRUCTION at diameter two with six review-synopsis corrections pending.
- Next step: merge #1787 and #1789 as completed records; correct #1791's synopsis (additive file) and merge; fold the analytical three into one source-energy note.

### L09 thermal / clock preparation and capture apparatus (15 PRs, 2026-10-24..27, all drafts)
- A sequential chain replaces supplied resources by finite thermal preparation: #1756 local clock source -> #1758 thermal environment -> #1761 registers -> #1764 work store and master clock -> #1766 one common temperature plus one fuel qubit. Side constructions: #1748/#1751 forward filter and local Hamiltonian, #1752/#1754 batteries, #1762 launch capacity, #1772 scale and energy logarithm, #1774 finite prefixes and archive decoder.
- canon/CANON.md (v106) cites #1746, #1761, #1764 and #1766 by commit; #1772/#1774 are bases of merged notes. V106 accepted #1743 (three restricted native-controller obstructions) and #1744 (record retention) at scope.
- No exact duplicates; successive "prior" refinements.
- Next step: merge the nine dependency/accepted PRs (Canon custody); fold the remaining six into one apparatus-preparation synthesis.

### L10 Hodge (7 PRs: #1711 #1713 #1716 #1719 #1721 #1723 #1726)
- #1721/#1723/#1726 are SUPERSEDED: merged C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N (v105) records them at their exact heads as "Consolidated at exact scope; do not merge standalone draft".
- Remaining results: #1711 first-order bridge gives a marked similarity, not an isometry under sqrt(5); #1713 pulse vs Hodge readings; #1716 boundary-current obstruction plus arithmetic Hodge map; #1719 actual capture gives no fixed Hodge packet step (obstruction).
- Next step: close the three superseded drafts (keep branches); harvest #1716/#1719 obstructions into a short Hodge-boundary note.

### L11 J readers (5 PRs: #1708 #1727 #1729 #1730 #1733)
- #1708 quadratic reading forced by one mixing; #1727 eventual read capacity m <= L_(2|k|)-1; #1729 complete binary reader classification; #1730 the arrow sits in the modulus, not the phase; #1733 PASS 26/26 with two-arch gate (digon/triangle J modes).
- Next step: one "J readers" synthesis of #1708/#1727/#1729; review and merge #1733 as a sealed record.

### L12 integer gravity: K1 / Noether / Maurer-Cartan (14 PRs: #1636..#1673)
- ABANDONED x6 (#1636 #1637 #1638 K1 bridge 1-3; #1656 second-order 1; #1672 #1673 Maurer-Cartan 1-2). FAIL x2 (#1643 at INITIAL_DATA; #1657 at BREAKER_BYTES). PASS x6 (#1639 K1 bridge 4; #1644 reciprocal action 2; #1646 joint variation; #1648 positive kinetic; #1654 cubic Noether; #1658 second-order 3).
- Merged successors (#1641 #1650 #1652 #1662 #1664 #1674) cite these by exact head; P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3 names #1672/#1673 as ABANDONED predecessors. V104 categorized all: R for the eight obligation records, M for #1646/#1648/#1654, E (errata) for #1639/#1644/#1658.
- This lane holds all 8 ABANDONED/FAIL probe records that sit unmerged in open PRs.
- Next step: merge all 14 (one probe per PR, merge commits), obligation records first; carry the V104 errata as additive ERRATA files, never edits to sealed files. Separately, P-INTEGER-LOCAL-PARENT-CLOSURE-1 (#1659) is pinned with no result and no PR.

### L13 v104 phase/contact source intake, remainder (15 PRs: #1577..#1634)
- V104 reviewed every one; the release merged their siblings (#1581 #1583 #1594 #1595 #1601 #1604 #1612 #1613 #1615 #1623 #1625 #1627 #1675) and left these open.
- Content: #1577 PHASE-DISTINCTION NOT_TRANSMITTED and #1579 AUDIT PASS (predecessors of merged #1581, V104 M); #1585 funded area AUDIT PASS with partial review #1606 (R); #1592 CLASS_NO_GO_WITH_SCOPE (M) and #1596 STOP_UNTYPED (E), both accepted by review #1608 (E); #1605 phase-energy gap located (N); #1607 PARTIAL/CHANGES_REQUIRED review (R, replaced by merged #1675); #1617 paid-record proposal rejected (N); #1619/#1621 native receiver and exchange boundaries (N); #1629 STOP_ADMISSION_UNSUPPLIED (N); #1631 SURVIVES (N); #1634 five-tick corollary.
- 12 of 15 are cited by merged work beyond the release review itself (not #1617, #1629, #1634).
- Next step: merge as records (M/N/R/E, errata as additive files); fold #1634 into #1631's lane.

### L14 H_B two-use and refresh memory (7 PRs: #1501 #1502 #1503 #1505 #1510 #1527 #1570)
- The five incubations are declared sources of merged C-FUNDED-TWO-USE-EXECUTABLE(-2)-N and P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-1/2. #1503 DELIVERED_CANDIDATE; #1510 contact factor is not a wave state.
- #1527 (sharp memory and exact refresh boundary) is accepted by independent audit #1570 (VERDICT PASS); merged C-TWO-USE-RESULTS-SYNTHESIS-N cites it.
- The failed audits AUDIT-1 (PARTIAL/STOP) and AUDIT-2 (SCIENTIFIC_FAIL) sit on branches with no PR.
- Next step: merge #1527 with #1570 and the five sources; open PRs for the AUDIT-1/-2 records.

### L15 v100 matter / photon / endpoint incubations (17 PRs: #1399..#1434)
- Positive: #1420 integer relative phase controls reciprocal trace-energy exchange (POSITIVE); #1411 exact flux-string translation; #1405 Z[phi] wave step with stable reading; #1407 reciprocal charge/field law; #1432 two unit writes into one receiver.
- Fired or negative: #1409 no robust free particle (robustness fails); #1403 integer-step obstruction; #1417 unchanged U loses the initial distinction; #1428 the one-tick decomposition fails in all four cases; #1422 complete Gauss obstruction.
- Open boundaries: #1413/#1415 native Hamiltonian selection open; #1399 admission forms; #1401 NS-TILT remains H; #1434 chi=3 for the unit-distance graph.
- Next step: merge the five dependency PRs (#1399 #1420 #1424 #1428 #1430); one "v100 matter-field outcomes" synthesis for the other twelve.

### L16 v100 review drafts (3 PRs: #1388 #1389 #1390)
- SUPERSEDED: merged probes P-CONTACT-RECORD-1, P-ALG-CONTACT-REALIZATION-1 and P-RESIDUAL-RECORD-COMPOSITION-1 carry byte-identical files and describe themselves as continuations of these PRs. Close candidates; branches kept.

### L17 photon: polymer, signed Xi, transfer (22 PRs: #1104..#1717)
- Signed-Xi bounds (candidate-T): simple cycles (#1177), sign-sensitive extension (#1181), ribbons (#1185), square tubes (#1187), planar bundles (#1189), prism bundles (#1191); source optimum rho=1/12 (#1183).
- No-go routes: sibling-only tree majorant supercritical at x=1/16 (#1169); uncle-memory family has no certificate (#1171); universal replica thinning q*<1 FALSE (#1167).
- Failure records: #1166, #1174, #1175, #1180 FAILED FIRST AUDIT; #1211 INCONCLUSIVE. Retry clusters: #1166->#1167, #1180->#1181, #1174->#1175-> merged N3.
- Dependencies: #1104 (merged SLOW-MODE-SECTOR-MAZUR-N), #1218/#1222 (merged BINARY-FIBER-SECTOR-CAP-N). #1326 leaves rooted-current boundedness unresolved; #1717 U(1)-Z7 bridge.
- Next step: merge the five failure/inconclusive records and the three dependency sources; one signed-Xi family synthesis (six class bounds, three no-gos), then close the standalone drafts.

### L18 ion light-shift (8 PRs: #1359..#1375)
- Pre-v98 inputs; v98 accepted six ion theorems inline (ION-LS-CONNECTED-RESPONSE, U-ION-HODGE-*).
- #1371 PASS (64 phase blocks realize all 25 sums) is the pinned source model of the merged ion notes. #1365 and #1369 PASS (linked from merged CA40 notes), #1361 restricted-model exclusion, #1359 resource gate HOLD, #1363/#1367 interface audits, #1375 state/observation/geometry separation.
- Next step: merge #1371; merge the three sealed probes as records or fold the lane into a v98-ion appendix.

### L19 field L5 / work record (10 PRs: #1302..#1319)
- v96 accepted FIELD-CONSERVATIVE-CHAIN-LAW, FIELD-CHAIN-FIRST-WORK and FIELD-LOCAL-WORK-RECORD with inline proofs.
- Stacked chain: #1310 is inside #1312, which is inside #1314 and #1316, inside #1318, inside #1319 (up to 46 shared blobs). #1302 failed its primary audit and #1304 is the PASS successor; #1306/#1308 are reviewed PASS with two-arch gates.
- Next step: close #1310/#1312/#1314/#1316/#1318 as superseded (keep branches); merge #1302 as the failure record; re-cut #1319's engineering prototypes (cartridge, controller, custody, reserve) as one fresh notes PR off main if wanted.

### L20 J memory and ramified locality (5 PRs, v94 era, all ready: #1289 #1291 #1293 #1295 #1297)
- #1297 RAMIFIED-TREE-TRANSPORT-BOUNDARY: five theorem-grade proofs passed separate review, audit PASS. #1291 and #1295 are cited by merged work. #1289/#1293 are classifications with three-reviewer PASS.
- Next step: merge #1297, #1291 and #1295; harvest #1289/#1293.

### L21 RH (12 PRs, all notes: #856 #933 #966 #979 #1008 #1014 #1020 #1021 #1022 #1031 #1194 #1235)
- #1235 maps 35 RH-adjacent registry rows (26 T, 3 C, 4 F, 1 H, 1 O) and at least ten reformulations; #979 consolidates the Mobius mean-channel frontier; #856 finds actual prime-frequency families far too large for the moment target; #933 finds the binary routing real, the RH transfer not closed and the first-layer finite transfer refuted; #1020 lists lane F-routes ("never a falsification of RH"); #1031 polynomial growth ladder, review HOLDS.
- #1021 (declare ordinary RH as a program dependency) is a refresh of the no-PR branch notes/rh-program-dependence-2026-09-08 and was never adopted in Canon.
- Next step: one RH lane synthesis built on #1235 + #979, with the F-route list from #1020/#933/#856; owner decision on #1021.

### L22 miscellaneous older (14 PRs)
- #910 lapse/shift identities are cited by exact head in merged V81-K1-LINEAR-METRIC-DECODER-1 (merge). #696 PROOF-SURVIVES, #783 and #1381 two-arch PASS: sealed probe records. #1345 counterexample to the global phi/5 pentit conjecture; #650 exploratory unit claim FALSIFIED; #980 W2K family fails joint gluability ("do not reopen"); #693/#695 STOP-predefinitions waiting for the owner.
- Next step: merge #910; merge #696/#783/#1381 as records (#696 keeps its priority caveat); harvest the notes.

### L23 infra, docs, maps (10 PRs)
- #1276 (v93 prep) and #1828 (v106 recovery CI) conflict and are superseded; main's V107 release plan says not to merge #1828. #787/#788 are superseded v75 planning. #995 (full clone needed for check_activation.py) is still accurate; it touches CLAUDE.md, so the owner decides. #786 needs the legacy/ security-review route. #907/#1234 are snapshots. #1874 is active. #1952 is this consolidation.


## MERGED branches that may be pruned (19)

Per AGENTS.md section 5a these are ancestors of main, so deleting the ref deletes nothing. None is an open-PR head, and `main` is not among them. Regenerate the ledger and apply the guarded procedure in notes/BRANCH-LEDGER-2026-08-24/README.md (`grep -qx main` stop and `--`) before deleting. Do not prune from this snapshot alone.

```text
codex/canon-v80-r3
codex/v102-consolidation-custody
codex/v107-publication-recovery-20261101
codex/v96-content-transport-review
codex/v96-field-j-review
codex/v96-internal-control-review
codex/v96-local-instrument-review
codex/v96-preparation-review
codex/v96-tuple-reader-review
notes/c-u-coaxial-herm2-lift-contract-n
notes/mirrored-contact-three-port-1920
prep/P-O5-FIRST-MISSING-SHELL-1-blobs
prep/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1-blobs
prep/P-O5-WALSH-LINK-HOMOLOGY-1-blobs
probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
probe/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1
probe/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
probe/P-SO3-FINITE-ANISOTROPY-DEPTH-1-copy
thorn/tabule-j-2026-10-16
```

`ccr-674ed817-vstfzn` was BASE at the first fetch. It is now DIVERGENT because PR #1952 pushed to it, so it is not prunable.

## DIVERGENT branches with no open PR (127) and ORPHAN (1)

**Never delete any of these** (AGENTS.md section 5a). The category says what each needs. Only OBLIGATION-OPEN, SEALED-RECORD, HARVEST and PRIOR-LEDGER-FOLD need action; the rest are retained history. `probe/` and `probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2` point to the same commit.

| category | n | meaning |
|---|---|---|
| OBLIGATION-OPEN | 5 | needs a PR: an unmerged ABANDONED or negative record, or a pin with no disposition |
| OBLIGATION-OPEN? | 2 | pin commit without result; the owner must confirm the pin was public |
| SEALED-RECORD | 4 | completed probe record never merged; a successor exists on main or the 2026-08-24 ledger dispositioned it |
| HARVEST | 6 | finished or draft content with no PR; owner review |
| PRIOR-LEDGER-FOLD | 27 | the 2026-08-24 ledger said FOLD (finished work that should land); still unlanded |
| CARRIED-BY-OPEN-PR | 3 | its content is inside an open PR |
| RETARGETED-ON-MAIN | 2 | content re-pinned under a new identifier on main, which cites this commit |
| SUPERSEDED-BY-MAIN | 2 | main holds the same probe with a later status, explained on main |
| TERMINAL-RECORD-ON-MAIN | 5 | identifier closed by notes/V63-TERMINAL-RECORDS |
| RELEASE-STAGING | 38 | release-form staging; that Canon is active on main |
| PRIOR-LEDGER-ARCHIVE | 32 | the 2026-08-24 ledger said ARCHIVE (historical, no obligation) |
| PRIOR-LEDGER | 1 | 2026-08-24 ledger disposition |
| ORPHAN | 1 | no merge base with main |

### OBLIGATION-OPEN (5)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `probe/P-U-J-HODGE-SEPARABLE-COUNTER-READ-1` | 2026-09-20 | 1 | 3 | 1/0 | pinned 51672be0 (lock #1069) with PREREG/PROOF/verify.py, no RESULT since 2026-09-20; main notes defer to its owner -> needs run or ABANDONED record PR / commit cited by main: notes/C-U-SELECTOR-READING-STRUCTURE-N,notes/canon,probes/P-U-COUNTER-AMPLITUDE-CLASS-1 |
| `probe/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` | 2026-10-15 | 2 | 8 | 1/1 | Status: ABANDONED record exists on the branch (d9a20f7b) and is cited by merged notes/C-U-NONLINEAR-AUDIT-CUSTODY-RECOVERY-N, but was never merged -> open a PR to merge the ABANDONED record / commit cited by main: notes/C-U-NONLINEAR-AUDIT-CUSTODY-RECOVERY-N.md,probes/P-U-NONLINEAR-AUDIT-ERRATA-1,probes/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2 |
| `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` | 2026-10-17 | 2 | 11 | 1/1 | completed first run, PARTIAL/STOP (audit-fixture typo; stages 5-6 NOT_RUN) with EXPECTED/RUN; successor AUDIT-3 is open PR #1570 -> merge this negative record (never relabel) |
| `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-2` | 2026-10-17 | 3 | 11 | 1/1 | completed, VERDICT SCIENTIFIC_FAIL, superseded by AUDIT-3 (#1570) -> fired result must be merged, not closed |
| `probe/P-INTEGER-LOCAL-PARENT-CLOSURE-1` | 2026-10-20 | 1 | 6 | 1/0 | pinned 10a4c4d8 (issue #1659), six frozen files, no RESULT since 2026-10-20; merged probes record "a pin but no completed execution" -> needs an ABANDONED record PR (or the run) / commit cited by main: probes/P-INTEGER-LOCAL-AUXILIARY-NOETHER-1,probes/P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1,probes/P-INTEGER-SCALAR-LAPSE-RIGIDITY-1 |

### OBLIGATION-OPEN? (2)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `probe-attempts/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2` | 2026-09-01 | 1 | 14 | 1/0 | same commit b36d285b as probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2 (twin ref); one disposition covers both / commit cited by main: probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2 |
| `probe/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2` | 2026-09-01 | 1 | 14 | 1/0 | commit "pin fresh dual Ward crosscheck 2" (2026-09-01), PREREG+engine, no RESULT; identical commit b36d285b to probe-attempts/ twin; main probes say issue #756 must decide before any CROSSCHECK-2 reservation -> owner to confirm whether the pin is public; if so it needs an ABANDONED record / commit cited by main: probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2 |

### SEALED-RECORD (4)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `probe/P-C20-TEICHMULLER-SPLIT-1` | 2026-07-22 | 2 | 5 | 1/1 | completed formal aarch64 leg (theorem candidate T, 6/6 PASS); successor P-C20-TEICHMULLER-SPLIT-2 on main calls it a quarantined predecessor; 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-C20-TEICHMULLER-SPLIT-2 |
| `probe/P-CARRY-ARITY-CIRCUIT-1` | 2026-08-09 | 6 | 5 | 1/1 | TRUE PROOF-FIRST LEMMA, two-arch audit PASS, promotion STOP; 2026-08-24 ledger FOLD (never landed) |
| `probe/P-CARRY-QUADRATIC-SYMMETRY-1` | 2026-08-21 | 3 | 5 | 1/1 | CARRY-QUADRATIC-SYMMETRY-CONFIRMED; successor -2 on main cites its pin; 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-CARRY-QUADRATIC-SYMMETRY-2 |
| `probe/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-1` | 2026-09-01 | 2 | 10 | 1/1 | WARD_ENGINE_QUALIFICATION_PASS (engineering only); successor -2 on main cites it / commit cited by main: probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2 |

### HARVEST (6)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `maintenance/reading-family-discipline` | 2026-08-29 | 5 | 2 | 0/0 | AGENTS/POLICY edits (134+/136-); main POLICY section 4 already has reading-family discipline -> likely superseded; owner check |
| `notes/c-j-norm-one-trace-kernel-seam-1-n` | 2026-08-29 | 5 | 5 | 1/1 | incubation result with PROMO; no PR |
| `notes/c-c40-reciprocal-ramified-seam-n` | 2026-09-01 | 3 | 10 | 1/1 | completed notes candidate with RESULT/EXPECTED/RUN and PROMO; no PR, no registry row |
| `cdx/qs-ab-diagnostic` | 2026-10-13 | 1 | 2 | 0/0 | QS variant A/B diagnostic note (1448 lines) in notes/canon; no PR |
| `notes/TOPDOWN-AUTOMATON-SYNTHESIS-2026-10-16` | 2026-10-16 | 1 | 2 | 0/0 | top-down integer automaton synthesis + U-to-chain gate bridge note; no PR |
| `probe/P-PHOTON-AXIS-POS-PRIMAL-1` | 2026-10-16 | 9 | 9 | 1/0 | pre-pin draft (commit subject says pre-pin); no obligation; owner decision |

### PRIOR-LEDGER-FOLD (27)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `notes/j-li-ra0-frobenius-square` | 2026-07-18 | 2 | 4 | 0/0 | 2026-08-24 ledger FOLD |
| `agent/incubation-contract` | 2026-08-01 | 8 | 2 | 0/0 | 2026-08-24 ledger FOLD: rewrites AGENTS.md; conflicts with this cleanup |
| `notes/c-split-unit-1` | 2026-08-01 | 2 | 12 | 1/1 | 2026-08-24 ledger FOLD |
| `codex/lean-public-audit-policy` | 2026-08-02 | 2 | 9 | 0/0 | 2026-08-24 ledger FOLD: touches AGENTS.md, POLICY.md, tools/check_policy.py and adds root audits/; conflicts with this cleanup and needs a POLICY layout change |
| `notes/lean-twistj-algebraic-seed-4` | 2026-08-02 | 1 | 10 | 0/0 | 2026-08-24 ledger FOLD |
| `notes/lean-twistj-layer-typing-3` | 2026-08-03 | 3 | 24 | 0/0 | 2026-08-24 ledger FOLD |
| `notes/census-v2-and-photon-lane` | 2026-08-05 | 4 | 21 | 1/0 | 2026-08-24 ledger FOLD / commit cited by main: notes/incubation-import-2026-08-21 |
| `notes/c-mass-read-n` | 2026-08-07 | 1 | 1 | 0/0 | 2026-08-24 ledger FOLD / commit cited by main: probes/P-RELATIONAL-MASS-CLOSED-RECOIL-1,probes/P-RELATIONAL-MASS-METRIC-RESPONSE-1 |
| `notes/c-golden-ame-galois-descent-1-n` | 2026-08-13 | 3 | 15 | 1/1 | 2026-08-24 ledger FOLD |
| `agent/review-lambda-cocycle-conductor-capacity-2026-08-14` | 2026-08-14 | 1 | 7 | 0/0 | 2026-08-24 ledger FOLD |
| `notes/c-golden-ame-a5-lu-covariants-1-n` | 2026-08-14 | 2 | 17 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-golden-ame-a5-lu-covariants-2-n` | 2026-08-14 | 2 | 31 | 1/2 | 2026-08-24 ledger FOLD |
| `notes/c-golden-ame-j-rigidity-1-n` | 2026-08-14 | 2 | 40 | 2/3 | 2026-08-24 ledger FOLD |
| `notes/c-golden-ame-twoplace-1-n` | 2026-08-14 | 4 | 18 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-golden-ame-vs-gg-artisanal-f8-1-n` | 2026-08-14 | 2 | 46 | 2/5 | 2026-08-24 ledger FOLD |
| `notes/c-rh-hadamard-horizontal-source-1-n` | 2026-08-14 | 3 | 3 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-rh-hadamard-weil-cayley-1-n` | 2026-08-14 | 5 | 5 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-tm-sym2-hadamard-character-1-n` | 2026-08-14 | 5 | 5 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-tm-sym2-nchar-born-carrier-1-n` | 2026-08-14 | 4 | 4 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-qdd-u-induced-null-anatomy-1-n` | 2026-08-17 | 3 | 6 | 1/0 | 2026-08-24 ledger FOLD / commit cited by main: probes/P-U-PREPARATION-EVENT-RECORD-1 |
| `handoff/audit-euler-widder-depth-20260820` | 2026-08-20 | 2 | 20 | 4/0 | 2026-08-24 ledger FOLD |
| `handoff/audits-lambda-grid-qdd-terminality-20260820` | 2026-08-20 | 1 | 20 | 3/0 | 2026-08-24 ledger FOLD |
| `notes/c-j-artin-mazur-zeta-1-n` | 2026-08-20 | 1 | 2 | 0/0 | 2026-08-24 ledger FOLD / commit cited by main: probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1 |
| `notes/c-rh-ray-finite-window-certificate-1-n` | 2026-08-20 | 7 | 7 | 1/0 | 2026-08-24 ledger FOLD |
| `notes/c-rh-ray-finite-window-certificate-3-n` | 2026-08-20 | 9 | 10 | 1/1 | 2026-08-24 ledger FOLD / commit cited by main: notes/BRANCH-LEDGER-2026-08-24,notes/V63-CLEANUP-SCOPE.md,notes/V63-TERMINAL-RECORDS |
| `notes/c-rh-stieltjes-widder-euler-1-n` | 2026-08-20 | 9 | 9 | 1/1 | 2026-08-24 ledger FOLD |
| `notes/c-jacobi-phase-cross-1-canonical-h-review` | 2026-08-23 | 3 | 12 | 1/0 | 2026-08-24 ledger FOLD |

### CARRIED-BY-OPEN-PR (3)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `claude/decoder-physical-reading-00xa91` | 2026-08-30 | 3 | 3 | 1/0 | drafts of TM-CORR-ZEROS prereg (run in #696), GENERATIONS-L3 and QS-COUPLING (#693/#695) / commit cited by main: notes/canon |
| `notes/rh-program-dependence-2026-09-08` | 2026-09-08 | 1 | 1 | 0/0 | original RH program-dependence proposal; refreshed by open PR #1021 |
| `codex/v96-photon-rooted-review` | 2026-10-01 | 2 | 3 | 1/0 | its 3 files are byte-identical to notes/C-PHOTON-ROOTED-CURRENT-REVIEW-N in open PR #1326 |

### RETARGETED-ON-MAIN (2)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `notes/C-J-SINGER-MAHLER-LIFT-1-N` | 2026-08-25 | 2 | 13 | 1/1 | completed notes candidate (RESULT/EXPECTED/RUN); content retargeted into merged probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1 which cites this commit / commit cited by main: probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1 |
| `notes/c-u-native-memory-event-n` | 2026-09-06 | 3 | 11 | 1/1 | incubation candidate-T (issue #861); retargeted into merged probes/P-U-NATIVE-MEMORY-EVENT-1 which cites this commit / commit cited by main: probes/P-U-NATIVE-MEMORY-EVENT-1 |

### SUPERSEDED-BY-MAIN (2)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `probe/P-A4-RAMIFIED-HODGE-TRACEKERNEL-1` | 2026-09-19 | 5 | 5 | 1/1 | branch holds an interim STOP RESULT; main holds the same probe with Status PASS (A4-RAMIFIED-HODGE-TRACEKERNEL T) |
| `probe/P-J-HODGE-PREDICTIVE-CLOSURE-1` | 2026-09-19 | 3 | 3 | 1/1 | branch says ABANDONED, main says PASS: explained on main (notes/canon/C-J-HODGE-NATIVE-FOLD-READINESS-N): PR #1054 was a later duplicate from an old base, closed without merge; accepted pin 8766a31c |

### TERMINAL-RECORD-ON-MAIN (5)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `notes/C-EM-UNIT-CARRIER-1` | 2026-07-28 | 1 | 3 | 1/0 | abandoned/retargeted identifier closed by notes/V63-TERMINAL-RECORDS on main (2026-08-24 ledger ABANDON/RETARGET) / commit cited by main: notes/V63-TERMINAL-RECORDS |
| `notes/entropy-selection-recon-breaker-m2` | 2026-07-30 | 35 | 65 | 3/3 | abandoned/retargeted identifier closed by notes/V63-TERMINAL-RECORDS on main (2026-08-24 ledger ABANDON/RETARGET) / commit cited by main: notes/V63-TERMINAL-RECORDS |
| `notes/c-rh-ray-finite-window-certificate-2-n` | 2026-08-20 | 5 | 5 | 1/0 | abandoned/retargeted identifier closed by notes/V63-TERMINAL-RECORDS on main (2026-08-24 ledger ABANDON/RETARGET) / commit cited by main: notes/V63-TERMINAL-RECORDS |
| `notes/c-rh-weil-norm-junction-1-n` | 2026-08-20 | 3 | 3 | 1/0 | abandoned/retargeted identifier closed by notes/V63-TERMINAL-RECORDS on main (2026-08-24 ledger ABANDON/RETARGET) / commit cited by main: notes/RH-EULER-HAUSDORFF-SOURCE-TAIL-2026-09-05.md,notes/V63-TERMINAL-RECORDS |
| `notes/c-rh-widder-angle-sweep-correction-1-n` | 2026-08-20 | 6 | 6 | 1/0 | abandoned/retargeted identifier closed by notes/V63-TERMINAL-RECORDS on main (2026-08-24 ledger ABANDON/RETARGET) / commit cited by main: notes/V63-TERMINAL-RECORDS |

### RELEASE-STAGING (38)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `fold/ramified-tm-lift-v11` | 2026-07-19 | 2 | 16 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `fold/canon-v22` | 2026-07-25 | 2 | 20 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `fold/canon-v26-c8-bilinear-shadow` | 2026-07-27 | 2 | 17 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `fold/canon-v26-c8-metro-reduction-arrows` | 2026-07-28 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `agent/canon-v27-tm-sym2-retire-disposition` | 2026-07-29 | 1 | 1 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `ci/v27-activation-preflight-209` | 2026-07-29 | 1 | 1 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `fold/canon-v27-minimal-read` | 2026-07-29 | 2 | 20 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v28` | 2026-07-30 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v29` | 2026-07-31 | 2 | 14 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `prep/v39-pretag-review-fix` | 2026-08-07 | 1 | 1 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v53` | 2026-08-19 | 2 | 19 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v56` | 2026-08-20 | 2 | 17 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `prep/canon-v61-build-export` | 2026-08-23 | 3 | 2 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `prep/canon-v61-evidence-hashes` | 2026-08-23 | 1 | 1 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `prep/canon-v62-build-export` | 2026-08-24 | 5 | 3 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v72` | 2026-08-30 | 2 | 17 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `codex/canon-v77` | 2026-09-05 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `codex/canon-v80` | 2026-09-06 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/canon-v80-r2` | 2026-09-06 | 2 | 19 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `fold/canon-v84-tt-source` | 2026-09-11 | 2 | 16 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `fold/canon-v84-tt-source-r2` | 2026-09-11 | 2 | 19 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/canon-v87-qdd-passive-family` | 2026-09-15 | 2 | 16 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v91` | 2026-09-21 | 2 | 21 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v93` | 2026-09-28 | 1 | 14 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v93-consolidated` | 2026-09-29 | 2 | 19 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v94` | 2026-09-29 | 2 | 14 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/canon-v95-native-record-energy` | 2026-09-30 | 2 | 17 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/v96-mathematical-fold` | 2026-10-01 | 2 | 19 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/C-V96-MEASUREMENT-CLOSURE-N |
| `codex/canon-v97-release` | 2026-10-02 | 2 | 22 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `codex/canon-v98-ion-hodge` | 2026-10-05 | 2 | 31 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/canon-v98-ion-hodge-release` | 2026-10-05 | 2 | 31 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/v102-consolidation` | 2026-10-16 | 2 | 21 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `release/canon-v104` | 2026-10-21 | 2 | 17 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `release/canon-v104-audit` | 2026-10-21 | 2 | 23 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `codex/v105-connected-asymptotic-20261024` | 2026-10-24 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |
| `codex/v105-connected-asymptotic-r2-20261024` | 2026-10-24 | 2 | 21 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `release/canon-v106` | 2026-10-27 | 2 | 18 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit |
| `codex/v108-release-20261103` | 2026-11-03 | 2 | 21 | 0/0 | release-form/staging branch; the corresponding Canon was activated on main by a separate commit / commit cited by main: notes/canon |

### PRIOR-LEDGER-ARCHIVE (32)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `agent/b-c-lane-2026-07-17` | 2026-07-17 | 1 | 7 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/p-curvature-operator-canonical-1-aut-reduction` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/p-curvature-operator-canonical-1-parent-surface-2` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/canon |
| `notes/p-dmatter-total-1-direct-readout` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/incubation-import-2026-08-21 |
| `notes/p-dmatter-total-1-owner-decision-input` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/canon |
| `notes/p-metro-class-1-fork-witness` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/p-metro-class-1-ruling-amendment-1-draft` | 2026-07-21 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/canon |
| `agent/two-architecture-workflow` | 2026-07-27 | 9 | 6 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/entropy-selection-recon` | 2026-07-30 | 31 | 58 | 1/1 | 2026-08-24 ledger ARCHIVE |
| `agent/incubation-checker` | 2026-07-31 | 13 | 4 | 0/0 | 2026-08-24 ledger ARCHIVE: touches tools/check_policy.py and .github/workflows/policy.yml; conflicts with this cleanup |
| `claude/science-status-v31-plan-ds4adk` | 2026-08-02 | 2 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `codex/cm-2i-qcarrier-hardening` | 2026-08-02 | 1 | 5 | 1/0 | 2026-08-24 ledger ARCHIVE |
| `codex/entropy-mackey-consolidation` | 2026-08-02 | 1 | 8 | 2/0 | 2026-08-24 ledger ARCHIVE |
| `notes/lean-twistj-foundations-1` | 2026-08-02 | 1 | 14 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/lean-twistj-observation-2` | 2026-08-03 | 2 | 20 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `claude/coin-minimal-read-type-1c194b` | 2026-08-04 | 2 | 17 | 0/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/canon,notes/kappa-witness-2026-08-03 |
| `notes/c-photon-point-group-1` | 2026-08-04 | 1 | 7 | 1/1 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/incubation-import-2026-08-21,probes/P-A3-FCC-POINT-GROUP-1 |
| `notes/canon-v39-lambda-cocycle` | 2026-08-06 | 1 | 1 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/c-suzuki-local-capacity-nogo-1` | 2026-08-13 | 2 | 4 | 1/1 | 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1 |
| `notes/rh-suzuki-consolidation-20260813` | 2026-08-13 | 6 | 19 | 2/2 | 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1 |
| `notes/c-tm-sym2-orientation-source-1-n` | 2026-08-14 | 3 | 3 | 1/1 | 2026-08-24 ledger ARCHIVE |
| `notes/c-tm-sym2-oriented-born-junction-1-n` | 2026-08-14 | 5 | 5 | 1/1 | 2026-08-24 ledger ARCHIVE |
| `notes/c-qdd-instrument-dilation-1-n` | 2026-08-16 | 6 | 2 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/c-tt-vector-moment-underdetermination-1` | 2026-08-17 | 2 | 21 | 2/2 | 2026-08-24 ledger ARCHIVE / commit cited by main: notes/V81-TT-NORMALIZATION-CLOSURE-INPUT-1.md,probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 |
| `notes/c-entanglement-local-relation-pythagoras-1-n` | 2026-08-18 | 4 | 4 | 1/1 | 2026-08-24 ledger ARCHIVE |
| `notes/c-entanglement-relational-wedge-1-n` | 2026-08-18 | 5 | 4 | 1/1 | 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-RELATIONAL-MASS-METRIC-RESPONSE-1 |
| `fix/policy-architecture-timeout-15` | 2026-08-21 | 1 | 3 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `notes/C-TRACEKERNEL-EXTERIOR-CLOSURE-1-N` | 2026-08-21 | 1 | 2 | 1/0 | 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1 |
| `notes/PROMO-C-TRACEKERNEL-EXTERIOR-CLOSURE-1` | 2026-08-21 | 3 | 8 | 1/1 | 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1 |
| `notes/record-crt-idempotent-and-v60-manifest-draft` | 2026-08-22 | 2 | 12 | 0/0 | 2026-08-24 ledger ARCHIVE |
| `agent/c-jacobi-phase-cross-1` | 2026-08-23 | 2 | 8 | 1/0 | 2026-08-24 ledger ARCHIVE: strict ancestor of notes/c-jacobi-phase-cross-1-canonical-h-review; fold the descendant only, or the same eight blobs land twice |
| `notes/C-AFFINE-READING-CHARACTER-CENSUS-1` | 2026-08-23 | 2 | 11 | 1/1 | 2026-08-24 ledger ARCHIVE |

### PRIOR-LEDGER (1)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `probe/P-QDD-INSTRUMENT-U-INDUCED-2` | 2026-08-17 | 1 | 1 | 1/0 | PREREG_DRAFT only, no verifier; 2026-08-24 ledger ARCHIVE / commit cited by main: probes/P-U-PREPARATION-EVENT-RECORD-1 |

### ORPHAN (1)

| branch | last commit | ahead | files | prereg/result | note |
|---|---|---|---|---|---|
| `ops/board` | 2026-07-31 | 3 | 8 | 0/0 | unrelated history, 8-file ops board, no pin; 2026-08-24 ledger ARCHIVE |

