# Result: H_B needs exact wave read, exact store comparison, guarded payment

**NON-CANONICAL / L1.** Analytical status of the new statements:
**candidate-T**, `AUTHORED_PROOF`, `SELF_REVIEWED`,
`NOT_INDEPENDENTLY_REVIEWED`. Scientific verifier: **NOT_RUN**
(none authorized in this round). Canon v101 unchanged.

## Conservative verdict

```text
CLASS_NO_GO_WITH_SCOPE
  no COMPLETE contact-stage compilation of H_B exists in Gamma_wb,
  in Gamma_sb, or hence in Gamma_fc (CONTRACT §4), already at B=2/5.
NATIVE_ADMISSION_UNSUPPLIED/STOP
  every permission kind shown necessary, and the kind shown
  sufficient at INITIALIZED scope in the extended comparison
  grammar Gamma++, is UNSUPPLIED by Canon. H_native(B) of #1496
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
4. **Guarded-payment sufficiency, scoped (Theorem 3).** Frozen
   `Gamma+` payments are unconditional; the natural pay word fails
   on `S_2`. Adding the single declared kind `K_guard` (guarded
   register addition) gives an explicit five-step word equal to
   `H_B` for all `B`, both directions, all occupied states, at
   **INITIALIZED** ancilla scope `(d,beta)=(0,0)`, ancillas restored.
   This is in `Gamma++`, outside frozen `Gamma+`.

## What is conditional, excluded, or still missing

- **Q3 inside frozen `Gamma+` is unresolved.** No compilation in
  `Gamma+` is shown, and no `Gamma+` no-go is claimed: whether its
  comparison/receiver channels can simulate guarded payment — at
  COMPLETE or INITIALIZED scope — is the exact remaining sub-question.
- Theorem 3 is **not** a COMPLETE equality for occupied ancillas and
  **not** a native compilation. All of its exact-arithmetic kinds,
  and both necessary kinds, are comparison permissions with no Canon
  warrant found in the audited Canon text (`PROOF.md` §6).
- Unresolved premises for any future positive claim: an independently
  warranted admission, at complete occupied scope, of exact wave
  read, exact store comparison and guarded exact payment (or a
  simulation theorem in an independently admitted class); the
  inherited external schedule/clock, addressing and reset
  obligations; finite precision of the rational store (not claimed
  here); physical realization (`NOT_READY`, untouched).
- Excluded by design and not reopened: funding/budgets 2/5 and 8/5,
  5/25 cardinalities, rank-2 span, the `R_fin` obstruction for `C`,
  `q`-only/`r`-only bounds, every finite audit, the two-use device
  of lane A2, and any sibling A2/A3 result (none read or used).

## Checks actually run (administrative, separated from science)

Executed repository checks and the exact CI record for the result
commit are reported in the lane-issue submission receipt. No
scientific code, enumeration, solver or verifier was executed for
this note; `PROOF.md` contains only hand symbolic derivations over
`F_5` and `Q`. Passing notes CI would be policy evidence only, not
a scientific reproduction of any inherited audit.
