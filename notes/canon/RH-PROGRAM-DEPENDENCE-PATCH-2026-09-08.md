# Canon patch proposal: RH as a declared program dependency

```text
STATUS      NON-CANONICAL. Canon patch proposal. No status motion.
BASIS       Public Canon v81, tag canon-v81, main f198220abf3b764dba680f76b97f226d212ce85f
CONTENT     72863e7014a770eb19d5f54fee0fbf253a6a2cc9
CANON.md    sha256 940e1d192f729c16fcb74b6e6ac1b8f02d1050326b6164affb276684c8696fbf, 568924 bytes
GATE        STATUS.md ACTIVE; tag and content commit ancestors of main; SHA256SUMS 5 of 5 OK
LAYER       NOT_APPLICABLE (program dependency, not a layer claim)
DATE        2026-09-08
```

This note proposes one registry row, one program-table row and one
paragraph of frontier prose. It creates no theorem, no estimate, no
zero-location statement and no dependency edge that is not written below.
Only a later sealed fold changes the Canon.

## 1. Source

Owner declaration of 2026-09-08, verbatim:

„RH je vyžadováno pro TWIST-J. Padne RH a padá TWIST-J.“

English: RH is required for TWIST-J. If RH falls, TWIST-J falls.

The declaration states a program-level dependency. It is not derived from the
axiom `J = 1 + zeta_5^2` and this note does not attempt to derive it; the
program's rule that the axiom is posited and its consequences are proved
(`notes/AXIOM-NOT-DERIVED-2026-08-26.md`) applies to a standing hypothesis in
the same way. A hypothesis is admitted with its falsifier or not at all.

## 2. Finding at v81

- `canon/CORE.md` contains no statement about the Riemann hypothesis, its
  zeros, or GRH.
- The registry has no row named `RH`, at v81 or at any earlier public tag.
- RH is mentioned by exactly two live rows, both labelled `ENRICHMENT` in
  `canon/FRONTIER_PROGRAMS.tsv`:
  `LAMBDA-COCYCLE-ANGLES [H]`, whose falsifier fires if RH is disproved or
  on one exact off-grid zero, and `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`,
  whose positive closure is at RH strength.
- `SUZUKI-LOCAL-CAPACITY-NOGO [T]` and the Li and lambda no-go rows state
  explicitly that they make no statement about RH.

So the registry files RH as enrichment and the owner files it as a
requirement. A summary that follows the Canon currently understates the
program's exposure. The fold below removes that understatement without
adding any positive claim.

## 3. Proposed registry row

Schema `claim_id  status  scope  canon_section  evidence  falsifier`, one
tab-separated line. Written here as fields for readability; the fold copies
them into `canon/REGISTRY.tsv` as one line.

```text
claim_id      RH-PROGRAM-DEPENDENCE
status        H
scope         the declared program-level dependency of 2026-09-08: TWIST-J
              requires the Riemann hypothesis, every nontrivial zero of
              zeta(s) has Re(s) = 1/2; adopted as a standing hypothesis of
              the program and not derived from the axiom; the exact required
              statement, RH for zeta(s), or GRH for zeta_F with F = Q(sqrt5),
              or GRH for the Hecke character tower over Q(sqrt5), and the
              rows that consume it are recorded as open owner decisions in
              notes/canon/RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md; every
              candidate statement contains RH for zeta(s), so the falsifier
              below is the same under each; no theorem, estimate,
              zero-location or prime-distribution result is asserted
canon_section 18. The frontier
evidence      inline
falsifier     fires, and by the owner declaration falsifies the program, if a
              nontrivial zero of zeta(s) with Re(s) != 1/2 is rigorously
              established in an independent public record by exact enclosure
              or machine-checked proof; a claim without such a record is
              STOP, not F; an external proof of RH does not promote this row,
              it retires the row to the changelog with the citation, turns
              the RH-strength target of TRIVIAL-RAPIDITY-EVALUATION-BRIDGE
              into a corollary, and leaves LAMBDA-COCYCLE-ANGLES unchanged,
              which is strictly stronger than RH
```

The `evidence` field is the word `inline` because the row is a declaration
with a falsifier, not a computed or derived result. The fold must not attach
a probe to it, and no probe can promote it above `H`.

## 4. Proposed program-table row

`canon/FRONTIER_PROGRAMS.tsv`, schema
`claim_id  program_id  queue_role  work_state  work_mode`:

```text
RH-PROGRAM-DEPENDENCE   <PROGRAM>   ROOT   BLOCKED   FORMAL
```

`<PROGRAM>` is owner decision 2 below. `BLOCKED` is the honest work state: the
row is decided from outside the program, and inside it only by the closure
of the bridge row. Whether `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE` moves out of
`ENRICHMENT` in the same fold is part of the same decision.
`LAMBDA-COCYCLE-ANGLES` stays under `ENRICHMENT` in every variant of this
proposal, because it asserts RH plus a grid condition and the owner has
already ruled that route not decidable by finite means.

## 5. Proposed frontier prose

One paragraph in `canon/CANON.md`, section 18, next to the two existing rows.
The fold owner writes the final wording; the content is fixed here. The
wording below has been checked against the forbidden word list of
`tools/check_canon.py` by eye only; the fold runs the tool.

> RH-PROGRAM-DEPENDENCE [H]. TWIST-J requires the Riemann hypothesis. The
> requirement is declared, not derived: it is a standing hypothesis adopted
> with its falsifier. A rigorously established nontrivial zero of zeta(s) off
> the critical line falsifies the row and, by the same declaration, the
> program. No row in this Canon proves, estimates or approaches RH; the
> bridge row TRIVIAL-RAPIDITY-EVALUATION-BRIDGE names the estimate that would
> close the arithmetic side at RH strength, and LAMBDA-COCYCLE-ANGLES names a
> strictly stronger route. An external proof of RH retires this row and adds
> nothing to the Canon's own results.

## 6. Owner decisions the fold needs

1. The exact required statement: RH for `zeta(s)`, GRH for `zeta_F`, or GRH
   for the Hecke tower over `Q(sqrt5)`. Since `zeta_F = zeta L(s, chi_5)`
   and every character in the tower has `zeta` in its product, each choice
   contains RH for `zeta(s)`; the choice fixes what would suffice, not what
   would falsify. Recommendation: file the weakest statement that the
   consuming rows actually need, once decision 3 is made; until then the row
   text above names RH for `zeta(s)` as the floor.
2. The program id. Options: a new program id for the arithmetic base, or an
   existing core program. Not a fold's choice.
3. The consuming rows. Which CORE rows use RH, and through which edge. The
   two consumers known from the working record are not public rows: the
   prime-order reading, in which fairness of the plenum stream is GRH for the
   character tower, and the O5 lane target `GRH(zeta_F)` through `O_5`.
   Edges must be derived and written, never assumed. Until they exist the
   row stands alone and the program-level reading rests on the declaration.

## 7. What the fold must not do

- Not promote `RH-PROGRAM-DEPENDENCE` above `H` on any evidence, including an
  external proof of RH; a proof from outside retires the row.
- Not fold an `F` on a claimed disproof without the independent public record
  named in the falsifier.
- Not attach the O5 candidate-T probes, the 2026-09-05 notes, or draft PR #856
  to this row; they belong to the bridge row and its future definitional lane.
- Not write a second RH statement anywhere in CORE; one row owns the
  dependency.

## 8. Cross-references

- `notes/RH-ONE-WALL-CROSSREF_2026-08-17.md`: counting rule for the one
  obstruction met at four levels; applies to any future summary of this row.
- `notes/AXIOM-NOT-DERIVED-2026-08-26.md`: the discipline for posited
  statements, extended here to a standing hypothesis.
- `notes/C-GRH-QSQRT5-SPLIT-ORIENTATION-1`: the only written record of the
  target mismatch `GRH(zeta_F)` versus `M(N)`; decision 1 should resolve it.
- Handoff status page `ZETA-RH-STATUS-2026-09-08.md` in
  `mathorn1973/twistj-handoff`: where the RH line stands at v81, section 4
  the wall, section 6 the next steps.
