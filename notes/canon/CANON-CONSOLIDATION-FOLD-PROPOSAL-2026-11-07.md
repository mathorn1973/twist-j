# Proposal: an editorial consolidation fold for the Public Canon

**NON-CANONICAL.** Canon patch proposal under `notes/canon/`. It changes no
Canon file and creates no claim, status, scope, evidence or version. A later
sealed public fold, with the release procedure of POLICY.md section 5 and
AGENTS.md section 6 item 9, is the only way any of it reaches `canon/`.

Basis: `main` `d4d3637`, Public Canon v109, `canon/CANON.md` 1,464,066 bytes,
32,933 lines, SHA-256 `035408ec...6383`. All five checkers pass at the basis.
Measurements were made by scripts during the 2026-11-07 consolidation; values
marked *estimate* are judgements.

## 1. Finding

The Canon has grown 27.6 times in bytes while its claim count grew 3.8 times:

| Release | Date | CANON.md bytes | Claims | Bytes per claim |
|---|---|---:|---:|---:|
| v1 | 2026-07-13 | 53,118 | 161 | 330 |
| v27 | 2026-07-30 | 150,959 | 214 | 705 |
| v50 | 2026-08-17 | 240,724 | 249 | 967 |
| v81 | 2026-09-08 | 568,924 | 406 | 1,401 |
| v100 | 2026-10-06 | 980,212 | 510 | 1,922 |
| v109 | 2026-11-03 | 1,464,066 | 609 | 2,404 |

`CORE.md`, the "short stable core", grew from 14,020 bytes at v81 to 51,239 at
v109.

The growth is **not verbatim duplication**. Exact duplicate paragraphs total
1,043 bytes, exact duplicate sentences of 40 or more characters 1,018 bytes,
and near-duplicate paragraphs (word 5-shingle Jaccard at least 0.8) 70 bytes.
Only 1.0 percent of prose tokens sit inside an 8-word run that recurs
anywhere. 382 of the 609 claim IDs are mentioned exactly once.

The growth is **append-order structure**. Within each top-level section the
line position of a claim tracks the release that first declared it (Spearman
+0.86 in section 2, +0.49 to +1.00 in eleven other sections). Section 2,
"Time, space, and the decoder", is 708.6 KB (48.4 percent of the file) and is
in practice a stack of fold blocks for v76 to v109, most opened by a claimless
scope intro. A reader meets the decoder and apparatus program in release
order, not in logical order.

## 2. Structural defects worth fixing

| ID | Where | Bytes | Defect |
|---|---|---:|---|
| D1 | section 18, lines 32448-32787 | 15,817 | per-release ledger chronology "The vN ledger change is signed term by term" for v22 to v36, with stale counts. POLICY section 5 excludes version chronology and fold narratives from the Canon. No claim ID or NORMATIVE anchor occurs only here. |
| D2 | section 18, lines 32788-32909 | 7,077 | a hand-maintained frontier board that repeats the generated `FRONTIER.md` and is **stale**: 12 of its 33 registry IDs are closed claims and 5 live claims are missing (LAMBDA-COCYCLE-ANGLES, PHOTON-CONE-CONVERGENCE, PHOTON-MASSLESS-PHASE, QUADRATIC-MEMORY-NATIVE-CONTACT, TRACEKERNEL-CURVATURE-FORCING). It is the only mention of GENERATIONS-L3, so one sentence naming it must stay. |
| D3 | preamble, lines 16-49 | 2,068 | four bold release-news paragraphs that paraphrase the v108 and v109 CHANGELOG entries and the CORE narrative |
| D4 | section 2 at 1003, 3296, 3676, 5144, 6507, 11031, 13523 | 4,281 | claimless fold-scope intros, each repeating a generic L1 scope for its own fold |
| D9 | lines 136, 171, 16393, 22130, 32929 | under 1 KB | stale identifiers ("Public Canon v104 contains no such theorem", Genesis-procedure wording "before the synthesis pull request opens") |
| D10 | `CORE.md` narrative | 28,417 | recent-fold news ("now closes", "now restores") instead of orientation; a third paraphrase of the same release news |

The companion files do not copy Canon text: the verbatim Canon share of
`CHANGELOG.md`, `CORE.md` and `FRONTIER.md` is 1.0, 6.4 and 4.6 percent.
`CHANGELOG.md` is the correct home for chronology and needs no change.

## 3. Proposed fold, in three independent phases

### Phase 1: editorial consolidation (one fold, move and delete only)

1. Keep all 19 numbered top-level headings and their exact titles. They are
   referenced by every `canon_section` value, by 311 `NORMATIVE.tsv`
   anchors, by `tools/architecture_map_report.py` (`WALL_SECTION`) and by a CI
   unit test.
2. Reorganize section 2 internally into themed parts, demoting the current
   `###` fold blocks to `####` and merging the D4 intros into one intro per
   part:

   | Part | Theme | KB |
   |---|---|---:|
   | 2.A | autonomous state, clock, selector, decoder interface | 4.3 |
   | 2.B | geometry reading: curvature class, trace subrecord, Hodge home | 17.9 |
   | 2.C | native readers and clock or history readout | 79.6 |
   | 2.D | QDD matter reading: algebra, dictionary, passive family, incidence, ports, stabilizer | 153.8 |
   | 2.E | J-register simplex arithmetic | 12.1 |
   | 2.F | decoder dynamics, reservoirs, calibration | 26.8 |
   | 2.G | records, occurrence and selection criteria | 15.3 |
   | 2.H | archived external observation records | 9.1 |
   | 2.I | ion and Hodge readout, controlled native writers | 47.3 |
   | 2.J | integer field automata, packet instrument, work-record chains | 124.2 |
   | 2.K | quadratic memory and residual contact architecture | 52.3 |
   | 2.L | J x M resultant seam and pair sources | 19.6 |
   | 2.M | contact accounts, role contacts, funded receivers | 57.1 |
   | 2.N | integral relative contact: minima, rhythms, apparatus, workbank | 74.9 |
   | 2.O | carry pairing and carry circuits | 14.2 |

   The line-range-to-part mapping is in the appendix. The headings "QDD Route A dictionary" (49 NORMATIVE
   anchors) and "Passive QDD observable family" (5 anchors) stay verbatim.
3. Delete D1 and D3. Replace D2 by one pointer to `FRONTIER.md` and one
   sentence that keeps GENERATIONS-L3. Fix D9.
4. Move every claim statement and proof as whole, byte-identical paragraphs.
5. Ship a mechanical proof that the fold only moves and deletes: the v110
   paragraph multiset equals the v109 multiset minus an explicit deletion
   list, and all 609 IDs, all 739 bracketed labels with their sentences, all
   323 NORMATIVE anchors and the exact strings read by
   `probes/P-QDD-EVENT-CARRY-BANK-1/verify.py` are preserved.

*Estimate:* about 25 KB smaller. The value of phase 1 is readability and
order, not size.

### Phase 2: scope and evidence compression (separate fold, reviewed claim by claim)

State one global scope convention for section 2 and section 15 apparatus
material ("unless a registered D, H or O row says otherwise, these statements
are L1 mathematics on the declared carrier and assert no physical realization,
interface, selection or derivation from J"). Then remove only the generic
disclaimers it covers (657 disclaimer sentences, 78 KB, carry no claim ID,
formula, label or evidence reference) and shorten evidence sentences that
repeat `REGISTRY.tsv` and `EVIDENCE.tsv` locations, keeping every ID and label
in its sentence. Normalize mathematics to one notation (today ASCII, 1,785
LaTeX lines and 338 Unicode-glyph lines coexist). Every removed sentence must
be checked for a hidden scope boundary, because removing a specific boundary
would rescope a claim. *Estimate:* 40 to 60 KB.

### Phase 3: optional moves between sections

Candidates: 2.B to section 5, 2.G to section 8, 2.H to section 15, 2.L and 2.O
to section 4, and the contact and apparatus theorems of section 15 into
section 2. Each move changes `canon_section` for the moved claims (hash
neutral) and needs the v110 status-separation layer to allow it explicitly.

### CORE.md

Trim the hand-written narrative to orientation: the axiom, the architecture
and decoder boxes, the one-paragraph statement of each established theme, and
a pointer to `FRONTIER.md`. Keep the generated claim block and the two anchor
lines required by `tools/generate_canon_views.py`. *Estimate:* 8 to 15 KB
smaller.

## 4. Constraints and the main risk

- `tools/check_canon.py`: first line `# TWIST-J Public Canon vN`; every claim
  ID must occur in CANON.md as an exact token; every `canon_section` value must
  be a substring of CANON.md; the five hashed files may not contain the words
  `sealed`, `internal`, `private`, `hidden`, `unpublished`; CANON.md may not
  contain `carried forward`.
- `tools/check_status_labels.py`: every bracketed status label must share a
  sentence with a registry ID of that status. Merging or splitting sentences
  can break this.
- `tools/check_ledger_core.py`: `NORMATIVE.tsv` anchors are raw substrings of
  CANON.md, including line breaks, so re-flowing a paragraph can break them.
- `reproduce/status-separation/verify.py` (1,598,248 bytes) reconstructs each
  earlier release from current bytes by reverse line patches. Past folds were
  nearly append-only, so each patch embeds at most about 6 KB of Canon text.
  A reorder expressed as a line patch would embed about 1.4 MB and push the
  file towards the 5 MiB policy limit, and the v109 proof blocks are pinned by
  byte span and SHA-256 (`V109_PROOF_CONTRACTS`). **Mitigation:** express the
  v110 layer as a paragraph permutation plus a deletion list. That restore is
  small and doubles as the move-and-delete proof of phase 1, item 5.
- Any change under `canon/` replays every probe and reproduction on both
  architectures in CI.

## 5. What this proposal deliberately does not do

- It does not shorten the Canon by moving proofs out. 528 KB (36 percent) of
  the Canon sits in subsections whose claims also carry probe or reproduction
  evidence, but only about 47 KB of Canon text is verbatim in `probes/`. For
  many T claims the Canon proof is what earns the T. Relocating proofs is a
  policy decision for the owner, not consolidation.
- It does not touch the registry, the companion ledgers, any status or any
  scope.

## Appendix: section 2 line ranges at v109 and their proposed parts

Line numbers refer to `canon/CANON.md` at v109. Byte counts were measured;
the assignment of a block to a part is a judgement for review. "Could move"
marks phase 3 candidates.

| Current lines | KB | Proposed | Notes |
|---|---:|---|---|
| 481-591 | 4.3 | 2.A | keep as §2 opening; the anchor "2. Time, space, and the decoder" stays |
| 592-1002 | 17.9 | 2.B | could move to §5 "The force is the curvature" (needs canon_section and anchor edits) |
| 1003-1416 | 20.7 | 2.C | v79; fold *intro* 1003 merges into the 2.C intro; the "### 1." to "### 5." numbering is dropped |
| 1417-1822 | 17.7 | 2.D | v79/v80 incidence and finite audit ("### 6.", "### 7.") |
| 1823-2301 | 15.9 | 2.D | factor-canonicity overlay |
| 2302-2959 | 39.1 | 2.D | **keep "QDD Route A dictionary" verbatim as a heading (49 NORMATIVE anchors)**; the 26-claim block is the primary statement of those claims (13 are mentioned only there) |
| 2960-3128 | 6.9 | 2.D | piston reshape and wedge |
| 3129-3509 | 19.1 | 2.D | v86 Galois code; v89 ports (*intro* 3296) |
| 3510-4082 | 26.3 | 2.D | **keep "Passive QDD observable family" verbatim (5 anchors)**; *intro* 3676 |
| 4083-4382 | 12.1 | 2.E | could move to §1 or §4 |
| 4383-4740 | 17.5 | 2.F | v77 decoder and reservoir |
| 4741-4975 | 11.0 | 2.D | v78 L4 stabilizer |
| 4976-5143 | 9.1 | 2.H | could move to §15 metrology |
| 5144-5525 | 17.1 | 2.C | v101 (*intro* 5144) |
| 5526-5999 | 17.8 | 2.D | v80 |
| 6000-6232 | 12.2 | 2.G | could move to §8 measure and Born |
| 6233-6287 | 2.8 | 2.C | v81 finite reader independence |
| 6288-6338 | 3.1 | 2.G | v81 occurrence address |
| 6339-6506 | 9.3 | 2.F | v81 loader, registration, TRC1 |
| 6507-6655 | 7.3 | 2.C | v90 (*intro* 6507) |
| 6656-7230 | 26.0 | 2.I | v91 |
| 7231-7429 | 9.1 | 2.C | v95 one-shot transfer |
| 7430-8792 | 69.3 | 2.J | v95-v97 |
| 8793-9247 | 21.3 | 2.I | v98 |
| 9248-10255 | 52.3 | 2.K | v99/v100 |
| 10256-10411 | 6.1 | 2.C | v102 |
| 10412-10745 | 12.7 | 2.J | v102 |
| 10746-11042 | 12.9 | 2.C | v102 (*intro* 10746, scope 11031) |
| 11043-11667 | 28.5 | 2.J | v103 |
| 11668-12117 | 19.6 | 2.L | could move to §4 "two places" (M = 1+m+m^2 with m = zeta_8 is the prime-2 object in the Notation block) |
| 12118-12448 | 13.8 | 2.J | v104 |
| 12449-13522 | 57.1 | 2.M | v104 |
| 13523-15167 | 74.9 | 2.N | v107-v109 (*intro* 13523); the v109 proof blocks are hash-pinned (§6.6) |
| 15168-15248 | 3.5 | 2.C | v109 first-tick transfer |
| 15249-15562 | 14.2 | 2.O | could move to §4 (carry lifts) |
