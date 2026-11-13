# Result: exact wave read and store comparison are necessary; typed compilation open

**NON-CANONICAL / L1.** Analytical status: Theorems 1-2
**candidate-T**; the Q0 audit, the §5 typing analysis and the
initialized algebraic recipe are checked records, not compiled-word
theorems. `AUTHORED_PROOF`, `SELF_REVIEWED`,
`NOT_INDEPENDENTLY_REVIEWED` (round R1 responds to the A4 review;
A4 re-review of this revision has not yet occurred). Scientific
verifier: **NOT_RUN** (none authorized). Canon v101 unchanged.

## Erratum R1 (replaces every contrary statement below from round 0)

Following the binding A4 review of head `53c71462`:

1. **(A1-R1) Compilation claim withdrawn.** The former "Theorem 3"
   five-step calculation is retained only as an *initialized
   algebraic recipe* from `(d,beta)=(0,0)` with ancillas restored
   along that execution. It is not a compiled word in globally
   admitted primitives: `CONTRACT.md` §4 requires each primitive to
   be a permutation of the whole extended carrier, but the store is
   bounded (`b in Q cap [0,B]`) while `d in Q` is arbitrary, so
   `K_reg` on `b` — a typing defect already inside frozen `Gamma+`,
   recorded here without editing the frozen contract — and the
   proposed `K_guard` instance `b -> b-d` at `beta=1` are not
   self-maps of the carrier (witness `B=2/5, b=0, d=1, beta=1`).
   Refusing invalid subtractions is also non-injective
   (`B=1, d=1/2`: `b=1/2` and `b=0` both give `b'=0`). INITIALIZED
   final equality does not waive the separate global-permutation
   requirement on the primitives themselves.
2. **(A1-R2) Q3 unresolved, no minimality.** The frozen question
   concerns `Gamma+`; the recipe needs an added guarded ingredient
   in a future separately typed extension. Neither a `Gamma+`
   no-go, nor necessity of the guard, nor any minimal extension is
   proved. Native admission remains `STOP`, not completed.
3. **(A1-R3) Export fixed.** `H_B` and the displayed recipe fix
   `(n,x)`; arbitrary words in the comparison grammars may apply
   `x -> g_i(x)` and need not fix `x`. Contact-stage words fix `n`.
4. **(A1-R4) Retained.** Q0 and Theorems 1-2, including costs
   `2/5, 2, -6/5` and the `b=2/5` vs `b=0` pair, are unchanged and
   scoped to the specified grammars — not to every possible native
   contact. `PROOF.md`, `RESULT.md` and `PROMO` are synchronized
   accordingly; `CONTRACT/PREREG/SOURCES/README` are unchanged.

## Conservative verdict

```text
CLASS_NO_GO_WITH_SCOPE
  no COMPLETE contact-stage compilation of H_B exists in Gamma_wb,
  in Gamma_sb, or hence in Gamma_fc (CONTRACT §4), already at B=2/5.
NATIVE_ADMISSION_UNSUPPLIED/STOP
  both permission kinds shown necessary are UNSUPPLIED by Canon,
  and no globally typed compilation of H_B is established in any
  class here (Q3 unresolved, Erratum R1). H_native(B) of #1496
  remains open; QUADRATIC-MEMORY-NATIVE-CONTACT remains O.
```

## What is proved here (new)

1. **Q0 audit.** The five Canon/#1489 generator formulas agree
   literally on `F_5^6`; `g_i^2=I` and the `z_6` table are verified
   symbolically; `g_2,g_3,g_4` are genuinely affine. No inverse of
   the selector-defined `U` follows. (`PROOF.md` §1)
2. **Wave-blind no-go (Theorem 1).** If coupling control and payments
   never read the exact occupied `(u,v)` wave and tapes — with
   arbitrary finite control, arbitrary word length, and exact
   `(w,b)` reads allowed — no word equals `H_B` on the complete
   carrier. Witnesses at `(q,r)=(0,1)`, `B=2/5`: accepted empty wave
   `S_0` versus rejected occupied `S_2` (shortage) and `S_{-2}`
   (overflow). This covers `Gamma_fc` as a corollary. It is new for
   the order-two target `H_B`, to which the inherited infinite-order
   obstruction against the unlimited `C` does not apply.
3. **Store-blind no-go (Theorem 2).** If control and payments never
   read `b` — with exact wave reads allowed — no word equals `H_B`.
   Witness: `S_0` with `b=2/5` (accepted) versus `b=0` (rejected).
   Hence exact wave read and exact store comparison are two
   separately necessary permission kinds in these frozen forms.
4. **Initialized algebraic recipe only (former "Theorem 3",
   corrected in Erratum R1).** From `(d,beta)=(0,0)` the five-step
   algebra outputs `H_B` for all `B`, both directions, all occupied
   states, with ancillas restored along that execution
   (`PROOF.md` §5.2). It is **not** a compilation in globally typed
   primitives (§5.1): guarded payment is only a proposed sufficient
   ingredient for a future separately frozen, completely typed
   reversible extension, outside this revision. No necessity,
   minimality or `Gamma+` no-go is proved.

## What is conditional, excluded, or still missing

- **Q3 is unresolved, with an exact typing obligation first.** No
  compilation in frozen `Gamma+` is shown and no `Gamma+` no-go is
  claimed. Outstanding, in order: (i) repair the frozen typing of
  additions into bounded `b` in a separately frozen successor whose
  every generator is a permutation of its whole carrier;
  (ii) compile at a declared scope or prove a class no-go in that
  completely typed class; (iii) prove guard necessity/minimality
  separately if ever claimed. Whether comparison/receiver channels
  could simulate guarded payment is part of (ii), not decided here.
- The §5.2 recipe is **not** a globally typed or COMPLETE equality
  and **not** a native compilation. All exact-arithmetic kinds,
  and both necessary kinds, are comparison permissions with no Canon
  warrant found in the audited Canon text (`PROOF.md` §6).
- Unresolved premises for any future positive claim: the separately
  frozen completely typed reversible grammar of (i)-(ii) above; an
  independently warranted admission of the exact-read kinds at
  complete occupied scope; the inherited external schedule/clock,
  addressing and reset obligations; finite precision of the rational
  store (not claimed here); physical realization (`NOT_READY`,
  untouched).
- Excluded by design and not reopened: funding/budgets 2/5 and 8/5,
  5/25 cardinalities, rank-2 span, the `R_fin` obstruction for `C`,
  `q`-only/`r`-only bounds, every finite audit, the two-use device
  of lane A2, and any sibling A2/A3 result (none read or used).

## Checks actually run (administrative, separated from science)

Executed repository checks and the exact CI record for each result
commit are reported in the lane-issue submission/revision receipts. No
scientific code, enumeration, solver or verifier was executed for
this note; `PROOF.md` contains only hand symbolic derivations over
`F_5` and `Q`. Passing notes CI would be policy evidence only, not
a scientific reproduction of any inherited audit.
