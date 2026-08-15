# P-DMATTER-TOTAL-1 Insertion Package v47 (NON-CANONICAL until fold)

```text
STATUS:                    COMPLETE INSERTION PACKAGE / OWNER-DIRECTED / NOT CANON
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               Public Canon v47, tag canon-v47
PUBLIC CONTENT COMMIT:     95219e2ba51bdedce76b2040bb0cfcb97937edfa
PUBLIC CANON SHA-256:      5e4c454e53381e13df2bc2e894bd6e7328af9329c4b13df03106c902c7caf400
PUBLIC CANON BYTES:        225589
CLAIM ISSUE:               107
OWNER DECISIONS:           2026-08-15: SPLIT, ACCEPT T1, ACCEPT GATE, SLOT RULING
SUPERSEDES:                the eight-item "next ordered requirement" of
                           P-DMATTER-TOTAL-1-DICTIONARY-DIRECT-OWNER-AMENDMENT.md
CARRIES:                   the ten corrections of AUDIT-QDD-BINDING-PACKAGE-V27.md
                           and the two rulings of QDD-OWNER-RULINGS-2026-07-30.md
FORMAL RUN:                NONE (public two-architecture jobs are the evidence)
CANON / TABLE CHANGE:      NONE by this note; the delta is a fold candidate
QDD STATUS:                O / STOP until the fold; target D at the fold
```

This package is the complete proposal-local insertion of the owner-adopted
QDD Route A dictionary into the public ledger. It contains (i) the Canon text
block, (ii) the ledger delta, (iii) the reproduction bundle, (iv) the
completion-contract manifest, and (v) the fold instructions. It changes
nothing until the owner folds it as the content commit of a new Canon.

Files of the package:

```text
notes/canon/P-DMATTER-TOTAL-1-INSERTION-PACKAGE-V47.md        this note
notes/canon/P-DMATTER-TOTAL-1-INSERTION-MANIFEST-V47.json     completion-contract manifest
notes/canon/CANON-BLOCK-QDD-ROUTE-A.md                        the Canon text block (verbatim fold content)
notes/canon/apply_qdd_insertion_delta.py                      the ledger delta, applied to a scratch tree, plus checker run
notes/canon/update_status_separation_witness.py               the release-audit update (counts, QDD at D, check 33), called by the delta
notes/canon/finalize_fold_v48.py                              version bump, CHANGELOG entry, SHA256SUMS, fold and staging commits, checks
reproduce/qdd-route-a/verify.py, EXPECTED.txt, README.md      the public reproduction bundle
```

## 0. Falsification first

The package is rejected as a fold candidate if any of the following holds:

```text
F1  D_QDD_direct and F_QDD o Q_QDD o beta_QDD differ on one of the 15625 checkpoints
F2  a G-self-adjoint idempotent other than E_low has kernel ker Tr_4
F3  the two public reproduction jobs are not byte identical to EXPECTED.txt
F4  tools/check_ledger.py fails on the folded tree
F5  any DEF-QDD-* identifier is stated outside canon/CANON.md (Ruling 1)
F6  E_low or E_high is named an effect or fills quadratic_manifest.effect_ids
    without the bridge and the separate apparatus row (Ruling 2, decision (a))
F7  the value 1/6 enters as input, threshold, normalization or confirmation
F8  a Herm-only claim or a new Sym-slot field appears (decision (d))
```

None of F1 to F8 holds in this package. F1 and F2 are excluded by the
reproduction, F4 by the recorded checker line, F5 to F8 by construction.

## 1. Owner decisions carried into the package

```text
(a) SPLIT
    QDD-ALGEBRAIC-FACTORIZATION      T   L1   exact record factorization
    QDD-PROJECTOR-PAIR-TR4           T   L1   projector pair theorem
    QDD-QCARRIER-DIAGONAL-BOUNDARY   T   L1   slot ruling
    QDD-BORN-READOUT-MEASURE         D   L6   physical effect and Born dictionary
    QDD-INSTRUMENT-APPARATUS         O   MULTI full apparatus, outside QDD
    QUADRATIC-DECODER-DATA           O -> D at the fold, layer MULTI
    QDD owns the effect shadow, the Born evaluation and the MatterData_QDD write.
    QDD carries no unregistered blocker: the apparatus is its own row.

(b) ACCEPT T1
    uniqueness of the projector pair             T (QDD-PROJECTOR-PAIR-TR4)
    LOW/HIGH physical assignment                 D (QDD-BORN-READOUT-MEASURE)
    explicit bridge                              DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION
        Tr_4 line -> ordered LOW, ker Tr_4 -> ordered HIGH
    no "inherited from CODEC-TR4", no uniqueness-from-J

(c) ACCEPT GATE
    GATE-L1-L6-QDD-BORN-READOUT, owner QDD-BORN-READOUT-MEASURE, L1 -> L6,
    DICTIONARY_LIFT; only normalized_weight_state on the NONZERO branch is L6;
    eight PASS conditions; ZERO branch is a tag, not a measure

(d) SLOT RULING
    no new Sym-slot field; no Herm-only claim; both slots stay typed;
    QDD-QCARRIER-DIAGONAL-BOUNDARY: on V_eff, A_dagger = A_T = v v^T
```

## 2. The eight ordered items of the amendment

1. Final identifiers. Direct map `DEF-QDD-DIRECT-WRITE`; record
   `DEF-QDD-MATTER-RECORD`; fields `support_state`, `total_weight`,
   `branch_weights`, `density_state`, `normalized_weight_state`, all `READOUT`,
   stage `D_matter`, leg `D_quadratic`, owner `DEF-QDD-DIRECT-WRITE`.
2. Bindings. Carrier `DEF-QDD-DOMAIN-K0` (pointed forward orbits, head n = 0),
   `DEF-QDD-BALANCED-PISTON`, `DEF-QDD-AMPLITUDE-B0`; codomain
   `DEF-QDD-MATTER-RECORD`; equalities `DEF-QDD-COEFFICIENT-Q` (rational),
   `DEF-QDD-QCARRIER-EQUALITY` (ordered componentwise); tags `ZERO_SUPPORT`,
   `SUPPORTED`, `ZERO_DENOMINATOR`, `DENSITY`, `MEASURE`; no bare null, no
   division on the ZERO branch.
3. Theorem, not premise. `QDD-ALGEBRAIC-FACTORIZATION [T]` states
   `D_QDD_direct = F_QDD o Q_QDD o beta_QDD` on the complete domain; the
   direct write is defined without naming `Q_QDD` or `F_QDD` (firewall of the
   amendment, section 6).
4. Dependency graph. 64 new rows in `canon/DEPENDENCIES.tsv`; acyclicity is
   decided by `tools/check_ledger.py` (cycle detection over the whole ledger):
   `LEDGER PASS claims=246 items=282 dependencies=448 evidence=246
   history=763 gates=11 programs=7`; the release audit
   `reproduce/status-separation` is updated as every fold updates it (counts of
   the folded tree, QDD read as D, the apparatus row in the program table, a
   33rd check `QDD-ROUTE-A`) and returns `RESULT 33/33 ALL PASS`;
   `tools/check_reproduce.py` re-runs all 23 reproductions on the folded tree
   with `REPRODUCE PASS` for each; `tools/check_status_labels.py` passes;
   `tools/check_canon.py` passes up to the release-facing fields
   (SHA256SUMS, STATUS.md, CHANGELOG entry) that belong to the fold commit.
5. Contract slots. `P-DMATTER-TOTAL-1-INSERTION-MANIFEST-V47.json` fills every
   slot owned by stage `D_matter`, leg `D_quadratic`, the five fields, the
   quadratic manifest, the two bridges, the measure and closure manifests, and
   the fourteen obligation rows; excluded slots use the typed constructor
   `SCOPE_EXCLUDED(expected_kind_id, submitted_scope_id, owning_requirement_id,
   public_basis_item_id)` with `SCOPE-QDD-DMATTER-DQUADRATIC`, whose one
   paragraph is part of the Canon block.
6. Endpoints and gate. Every DEF-QDD-* item and the three T rows are L1; the
   D row is L6 and owns the gate; the O row is MULTI; QDD stays MULTI. No lift
   is performed by this note.
7. Routing. The gate closes positively on the eight owner conditions,
   negatively on a supported head with a value outside [0,1], a pair not
   summing to 1, or two heads with equal `Q_QDD` and different pairs, and
   STOP while the record, the ordered outcome set or the L1 theorem is
   missing. The registry falsifiers of the five rows are displayed in the
   delta and can each fire on the finite domain.
8. Re-audit on v47. Every count in this package was recomputed from scratch
   on the v47 tree by `reproduce/qdd-route-a/verify.py` (fifteen checks,
   RESULT 15/15 ALL PASS) on x86_64 (Ubuntu 24.04, CPython 3.12.3) and aarch64
   (Ubuntu 24.04, CPython 3.12.3): verifier SHA-256
   `5214ebdbc775f58117d73495617bea59895f00b4bd6186120e9b2098547c8ec8`, stdout
   SHA-256 `41870e4c3335ebdc3fbbecf57dfb4940830d928817c8ea60d0eb67109b88a230`
   on both, bundle hash `0511f52896e67fa3e073a0da72ef58188f3e07cbc12f72f71441b2f633c7a357`.
   These runs are audit input; the public evidence is the pair of public
   reproduction jobs on the fold commit.

## 3. The ten audit corrections

```text
 1  displayed formulas          DEF-QDD-TRACE-PAIRING writes <x,y> = (1/5) Tr(x sigma_4(y)) with its 1/5;
                                sigma_4 = (zeta -> zeta^4) is defined; T_w, MATRIX_B0(T_w) = v v^T G and the
                                ordered branch pair are displayed; the target was rerun on all 15625 checkpoints
 2  LOW LINE named correctly    DEF-QDD-LOW-LINE: Q lambda_B, lambda_B = -zeta^4, Tr = 1; the words
                                "rational-line and trace-kernel" do not occur; NEGLINE control 480 of 625
 3  gate can route negative     GATE-L1-L6-QDD-BORN-READOUT: eight PASS conditions, explicit negative and STOP
 4  layer field                 owner of the gate is the L6 row QDD-BORN-READOUT-MEASURE; the cross-layer edges
                                to L1 items are enforced by check_ledger; QDD stays MULTI (decision (c))
 5  ledger delta passes         LEDGER PASS recorded above; produced by apply_qdd_insertion_delta.py
 6  statement_source            every new item: canon/CANON.md::QDD Route A dictionary (Ruling 1)
 7  effect ruling cited         DEF-QDD-PROJECTOR-LOW/HIGH carry ALGEBRAIC_READOUT; the physical selection is the
                                bridge [D] and the apparatus is QDD-INSTRUMENT-APPARATUS [O] (Ruling 2)
 8  SCOPE_EXCLUDED split        constructor stated in the Canon block; used only for excluded stages, legs,
                                physics, metrology and scheme slots; never for one of the fourteen QDD data
 9  313 collision disclosed     in the Canon block, the registry scopes and the manifest; no cross-leg identity
10  probe scoped                the reproduction bundle is a conformance certificate; a prospective probe is not
                                needed for the fold and would be scoped for reproducibility only
```

## 4. Compliance with the two rulings

Ruling 1. No `DEF-QDD-*` identifier is stated in a note. The Canon block is
the statement source of all eighteen definitions and the five claims; the
version, hash and byte count move at the fold.

Ruling 2. The two matrices are projectors (`DEF-QDD-PROJECTOR-LOW`,
`DEF-QDD-PROJECTOR-HIGH`, `ALGEBRAIC_READOUT`). The word "effect" appears
only in `DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION`, which is the explicit
dictionary bridge the ruling asked for, adopted by the D row, and in
`QDD-INSTRUMENT-APPARATUS`, which is the open physical row. The forbidden
slot `quadratic_manifest.effect_ids` is filled in the manifest with the two
projector identifiers under the semantics label "effect shadow selected by
the bridge [D]; the physical instrument family is QDD-INSTRUMENT-APPARATUS [O]
and is not asserted here". If the owner prefers the slot to remain
`UNRESOLVED` until the apparatus row closes, that is a one-line change of the
manifest and of the QDD scope sentence "owns the effect shadow"; the delta is
otherwise unaffected.

## 5. What the package asserts and what it does not

Asserted: the exact identity of the adopted dictionary on the complete finite
domain; the projector-pair theorem; the diagonal boundary of the two slots on
`V_eff`; the L6 reading of the normalized branch through the named gate; the
public binding of the fourteen data; the split of the apparatus into its own
row.

Not asserted: uniqueness from J; an apparatus, instrument, realized outcome,
occurrence law, sampling, post-state or SI claim; totality, uniqueness or
completeness of `D_matter`; a Herm-only reading; a physical central phase from
`A_dagger = A_T`; any binding of the number 1/6 or of the count 313.

## 6. Fold instructions (owner only)

```text
1  apply the delta to a release branch from main at canon-v47:
     python3 notes/canon/apply_qdd_insertion_delta.py <checkout>
   (it appends the Canon block, rewrites the four prose occurrences of
   "QUADRATIC-DECODER-DATA [O]" and the section 18 list entry, adds the
   ledger rows, updates the status-separation witness, regenerates the views,
   and prints the checker lines; the whole result is also available as one
   git patch, qdd-insertion-package-v47.patch)
2  place the Canon block where section 2 ends the decoder interface (the
   anchor "QDD Route A dictionary" must stay in the heading)
3  add the CHANGELOG entry, regenerate canon/SHA256SUMS, update STATUS.md
   (version, CONTENT_COMMIT, CANON_SHA256, CANON_BYTES); check_canon.py
   passes up to exactly those release-facing fields on the scratch tree
4  let the public x86_64 and aarch64 reproduction jobs run on the same commit;
   their RUNS records are the architecture gate for reproduce/qdd-route-a
5  activation commit and tag; QUADRATIC-DECODER-DATA moves O -> D in the
   activation, not before
```

## 7. Scope firewall

```text
CANON CHANGE BY THIS NOTE       NONE
REGISTRY CHANGE BY THIS NOTE    NONE
PROBE / FORMAL RUN              NONE
QUADRATIC-DECODER-DATA          O / STOP until the fold; D at the fold
QDD-INSTRUMENT-APPARATUS        O / STOP, separate, from the fold on
HYBRID EXTENSION                excluded, no row
SYM SLOT FIELD                  none; QDD-QCARRIER-DIAGONAL-BOUNDARY only
```
