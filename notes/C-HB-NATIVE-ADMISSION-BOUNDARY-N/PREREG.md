# Preregistration: H_B native admission boundary

**NON-CANONICAL / L1 / analytical only. Frozen before the new proof.**
Candidate `C-HB-NATIVE-ADMISSION-BOUNDARY-N`, lane
[#1498](https://github.com/mathorn1973/twist-j/issues/1498), base
`8b91a935c426036e00ecb300019fd94734addeec` (Public Canon v101).

## Evidence mode

`ANALYTICAL_ONLY`. No new scientific execution is authorized in this
round: no verifier, enumeration, solver, simulation or audit script is
run, and no `EXPECTED.txt`/`RUN.md` evidence is created. All new claims
must be exact symbolic derivations over `F_5` and `Q`. Repository
policy/Canon/ledger checks are administrative and are reported
separately. A statement that would need a computation not supplied here
must be left as an explicit gap, not asserted.

## Known exposure (not new results of this note)

The following are result-exposed premises, read at the immutable commits
in `SOURCES.json`. They are never claimed as discoveries of this lane:

1. Canon v101 native conventions: carrier `F_5^6`, five generators,
   selector `U`; owner `QUADRATIC-MEMORY-NATIVE-CONTACT [O]` with its
   own finite `F_5^12 x {0,1}` target (not claimed here).
2. #1485 classical contract: Dirichlet carrier, `E_D`, `E_full`, tapes.
3. #1489: contact `C_*`, lift `eta`, classes `N0`/`NC`, `N0`
   factor-separation obstruction, prepared-image inverse limits.
4. #1492 finite census (merged, unregistered): 625 preparations, five
   encodings, 51 occupied cases. Used as context only.
5. #1496 (noncanonical premise): complete `H_B`, difference formula
   (1), involution theorem, cardinalities 5/25, rank 2, budgets 2/5
   and 8/5, unbounded occupied-wave cost, `q`-only/`r`-only fixed-word
   insufficiency, finite-relation lift obstruction for the unlimited
   `C`, direction-collision witnesses, open hypothesis `H_native(B)`,
   and its one-architecture 7,200-instance auxiliary audit.
6. #1399: finite `F_5` factor-compatible word obstruction
   (Proposition 3) and its admission table, on a different carrier.
7. `CW-ALG-1` (`P-ALG-CONTACT-REALIZATION-1` SPEC): a finite `F_5`
   compiler with declared `W` gates as premises; it grants no operation
   on the rational wave.

## Frozen questions (new obligations)

- **Q0 (compulsory audit).** Compare the five generator formulas of
  Canon v101 with the #1489 text on the same carrier; verify
  symbolically `g_i^2 = I` and the `z_6` table; separate generator
  involutions from invertibility of the selector-defined `U`.
- **Q1 (wave-blind class).** Decide complete-carrier compilation of
  `H_B` in the frozen grammar `Gamma_wb` of `CONTRACT.md`.
- **Q2 (store-blind class).** Decide complete-carrier compilation of
  `H_B` in the frozen grammar `Gamma_sb`.
- **Q3 (initialized sufficiency).** In the extended grammar `Gamma+`,
  either exhibit one explicit finite word equal to `H_B` on the
  declared initialized-ancilla subcarrier, with ancillas restored, or
  prove that the added kinds still do not suffice.
- **Q4 (warrant audit).** For every permission kind used, state its
  origin. In particular decide from the cited Canon text whether any
  cross-register exact rational read/write kind is Canon-admitted.

## Outcomes and failure witnesses

Positive compilation requires literal equality on the declared carrier
and scope in `CONTRACT.md`, including both rejection reasons and the
two-sided inverse behaviour inherited from `H_B`. A single complete
occupied state on which a candidate word differs from `H_B` refutes
that word; a class no-go must cover every word of the frozen class.
Admissible verdicts: `NATIVE_COMPILATION_SHOWN_IN_FROZEN_CLASS`,
`CLASS_NO_GO_WITH_SCOPE`, `NATIVE_ADMISSION_UNSUPPLIED/STOP`, each only
at its proved scope. Absence of a Canon permission is `UNSUPPLIED`,
never a theorem about all future physics. The broad owner rows stay
`O/STOP` unless separately closed elsewhere.

## Stop conditions

Stop and report `BLOCKED_A1` if the base or Canon moves, a pinned
source hash differs, a topical collision appears, a needed premise is
not actually in the cited source, or a proof step would require an
unauthorized computation or an unnamed layer lift.
