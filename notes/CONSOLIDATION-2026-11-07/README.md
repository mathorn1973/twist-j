# Consolidation of 2026-11-07

**NON-CANONICAL.** A one-time review of everything built for TWIST-J, aimed at
cleanup, removal of duplication and a synthesis of what is valuable. It
creates no claim, status, scope, evidence or Canon version, and it changed no
file under `canon/`, `probes/`, `reproduce/`, `tools/` or `.github/`.
Authority is declared only by `STATUS.md`.

Basis: twist-j `main` `d4d3637` (Public Canon v109), plus the satellite
repositories `twistj-handoff`, `twistjdotcom` and
`kniha-realny-pruvodce-imaginarnim-vesmirem` at their `main` heads of the same
day.

## Files

| File | What it is |
|---|---|
| [SYNTHESIS.md](SYNTHESIS.md) | the valuable content: what TWIST-J posits, what is established by theme, all 19 falsifications, where the frontier sits, an assessment |
| [UNMERGED-WORK.md](UNMERGED-WORK.md) | ledger of the 216 open pull requests by lane, with one synthesis per lane, open obligations, and the PR heads `main` depends on |
| [PR-LEDGER.tsv](PR-LEDGER.tsv) | one row per open pull request, with evidence, successor and recommendation |
| [BRANCH-LEDGER.tsv](BRANCH-LEDGER.tsv) | output of `tools/build_branch_ledger.py` on a full clone, recorded before any pruning (AGENTS.md section 5a) |
| [NOTES-INVENTORY.tsv](NOTES-INVENTORY.tsv) | one row per top-level `notes/` entry at `0456ca92`: references, landing, successor, clutter, recommendation |
| [../canon/CANON-CONSOLIDATION-FOLD-PROPOSAL-2026-11-07.md](../canon/CANON-CONSOLIDATION-FOLD-PROPOSAL-2026-11-07.md) | measured proposal for an editorial, claim-preserving Canon fold |

## What the review found

| Surface | Size | Finding |
|---|---|---|
| `canon/CANON.md` | 1.46 MB, 609 claims | 27.6 times the v1 size for 3.8 times the claims. Verbatim duplication is about 2 KB. The size comes from fold blocks appended in release order, half of it in section 2. Real defects: a stale hand-kept frontier board in section 18 (12 of 33 entries closed, 5 live claims missing), a v22 to v36 chronology, release news in the preamble. |
| `canon/CORE.md` | 51 KB | the "short stable core" grew from 14 KB at v81; its narrative is release news, a third paraphrase of the CHANGELOG |
| `notes/` | 278 entries, 2,652 files, 45.6 MB | not where the duplication lives. 140 entries are referenced by Canon, tools or sealed probes (46 of them byte-frozen by `reproduce/status-separation`), 32 feed live work. Only 21 files were referenced nowhere. 15.4 MB of run dumps inside kept notes are bound by the notes' own `SHA256SUMS`. |
| open pull requests | 216 | 78 merge candidates (all merge cleanly and pass `check_policy.py`), 15 superseded, 103 stale-harvest, 20 active, no true duplicates. Eight ABANDONED or FAIL probe records and several negative notes records sit unmerged, although policy closes those obligations only by merge. `canon/CANON.md` and merged probes already cite heads of 71 unmerged PRs. |
| remote branches | 364 | BASE 1, DIVERGENT 343, MERGED 19, ORPHAN 1. Only the 19 MERGED refs may be pruned. |
| `twistj-handoff` | 151 files | all 39 + 46 SHA-256 pins intact; the start page pointed at the v105 readiness map; 59 loose root files |
| `twistjdotcom` | 104 files | all 112 status labels match v109; only metadata dates were stale |
| book | 416 MB tree, about 1.05 GB on GitHub | book text clean; the web compendium had wrong v108 and v109 counts; CI commits about 90 MB of PDF and EPUB back to `main` on every build |

## What was done

In this pull request:

- added `SYNTHESIS.md`, the Canon fold proposal and the three ledgers;
- removed four `notes/` entries and one empty file that nothing in the
  repository references, checked twice (token index and `git grep -F` on every
  path and entry name):

  | Removed | Why |
  |---|---|
  | `notes/C-J-UNIT-STRIP-DECODER-N/` (9 files) | landed: its result is registered as J-UNIT-STRIP-NORMAL-FORM, ZETA5-DEDEKIND-RESIDUE and ZETA5-IDEAL-COUNT-LANDAU [T] through `probes/P-ZETA5-RESIDUE-STRIP-DECODER-2` |
  | `notes/FRONTIER-ATTACK-MAP-2026-08-26/` (3 files) | attack map at Public Canon v66, superseded by `canon/FRONTIER.md` |
  | `notes/QDD-STOP-INVENTORY-V65/` (4 files) | QDD STOP inventory at Public Canon v65, superseded by the registry |
  | `notes/V81-CLOSURE-WORK-PROGRAM-2026-09-08-CZ.md` | control board at Public Canon v81, superseded |
  | `notes/C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N/ENGINEERING/analysis.stderr` | empty file, not listed in that note's `SHA256SUMS` |

  Every removed byte stays reachable in history at `d9393120`.

In sibling draft pull requests:

- `twistj-handoff` #51: 150 renames into four dated `archive/` folders, bytes
  unchanged, all pins re-verified; README now points at v109 and maps old names
  to new paths;
- `kniha-realny-pruvodce-imaginarnim-vesmirem` #9: corrected the v108 and v109
  counts in `web/Konstrukce_ke_kapitolam.md` (26 live H/O rows, not 27;
  RELATIVE-CONTACT-COMMON-APPARATUS-OPEN is T since v108);
- `twistjdotcom` #18: refreshed stale `dateModified` and sitemap dates, dropped
  foreign `.gitignore` rules.

## Owner decisions, in order of value

1. **Close open obligations by merge.** ABANDONED #1636, #1637, #1638, #1656,
   #1672, #1673; FAIL #1643, #1657; INCONCLUSIVE #1787, #1789; negative notes
   records #1166, #1174, #1175, #1180, #1302, #1211; STOP #1596, #1629. Open
   pull requests for the obligations that have none:
   `probe/P-INTEGER-LOCAL-PARENT-CLOSURE-1` and
   `probe/P-U-J-HODGE-SEPARABLE-COUNTER-READ-1` (pinned, never run),
   `probe/P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-1` (ABANDONED record written),
   `probe/P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1` and `-2` (negative audits),
   and decide whether the `P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2` pin was public.
2. **Restore custody inside `main`.** Merge the PRs whose exact heads `main`
   already relies on: #1746, #1761, #1764, #1766 (cited by commit in
   `canon/CANON.md`; one cited path, `notes/C-THERMAL-REGISTER-PREPARATION-N/HAMILTONIAN.md`,
   exists only on #1761), #1908, #1912, #1915 (merged #1923 builds on them),
   and #1639, #1644, #1646, #1648, #1658, #1819, #1821, #1857. The full list is
   the `main_dependency` column of `PR-LEDGER.tsv`.
3. **Close the 15 superseded pull requests** without deleting their branches:
   #1310, #1312, #1314, #1316, #1318 (folded inline in v96), #1721, #1723,
   #1726 (consolidated in v105), #1388, #1389, #1390 (byte-carried by merged
   probes), #1276, #1828, #787, #788.
4. **Harvest the 103 stale drafts lane by lane.** One reviewed synthesis note
   per lane (Dirac contact, signed-Xi photon bounds, RH, v100 matter-field
   outcomes, thermal preparation and others in `UNMERGED-WORK.md`), then close
   the standalone drafts. Branches stay.
5. **Prune the 19 MERGED branches** listed in `UNMERGED-WORK.md`, after
   regenerating the ledger. Never delete a DIVERGENT or ORPHAN ref.
6. **Run the editorial Canon fold** of the proposal: reorganize section 2 by
   theme, delete the section 18 chronology and stale board and the preamble
   news, trim the CORE narrative, and prove move-and-delete mechanically.
7. **Public safety.** `notes/incubation-import-2026-08-21/SESSION-RECORDS` and
   nearby files contain machine nicknames, a private hostname and home-directory
   paths; a zip in `notes/C-J-RAMIFIED-DECODER-DEPTH-N` (pinned by two sealed
   probes) contains Windows home paths and private-repository context;
   `notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/VALIDATION.md` contains a personal
   e-mail address. All are covered by their notes' own checksum lists or by
   sealed probes, and all remain in public history, so redaction on `main`
   alone would not remove them. This needs an explicit owner decision.
8. **Satellites.** Tag the three handoff commits that twist-j cites but that
   live only on branches without a PR (`3eb3edb`, `6ad511d`, `fc1f182`) before
   any handoff branch cleanup. Stop committing generated PDF and EPUB from the
   book CI, since the `sazba-latest` release already carries them.
