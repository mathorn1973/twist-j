# P-DMATTER-TOTAL-1 QDD Public Requirements Audit (NON-CANONICAL)

```text
STATUS:                    PUBLIC-SOURCE INVENTORY
AUTHORITY:                 NOT CANON
PUBLIC MAIN BASE:          412d56fd46f3d6a919d17fdaaa39bb4c9bfc681b
PUBLIC CANON:              Public Canon v24 / canon-v24
PUBLIC CONTENT COMMIT:     bee0f1bfe421d6dbd599b6625e077ef08f03fb4c
CLAIM ISSUE / COMMENT:     107 / 5093431422
SCOPE:                     EXACT 14-ITEM QUADRATIC-DECODER-DATA STOP INVENTORY
INVENTORY RULE:            PUBLIC ONLY WITH AN EXACT RESOLVABLE TYPED PUBLIC ID
OWNER DECISION:            NONE
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
BINDING GATE:              MISSING
CANON/TABLE/STATUS CHANGE: NONE
QDD STATUS:                O / STOP, unchanged
```

## 1. Decision rule

The authoritative requirement is the `QUADRATIC-DECODER-DATA [O]` row in
`canon/REGISTRY.tsv`, reproduced in `canon/FRONTIER.md` under **Decoder
core**. A requirement counts as `PUBLIC` only when the public ledger resolves
the exact typed object and its QDD binding. A displayed formula, a generic
theorem used by QDD, a schema slot, or a `notes/`-local `CAND-*` identifier
does not count.

This rule is forced by the public boundary:

- `DEF-DECODER-MATTER` declares only a partial interface whose fields exist
  where registered.
- `DEF-DECODER-COMPLETION-CONTRACT` declares manifest shapes, explicitly not
  their values, existence, totality, factorization, or closure.
- `READING-SPLIT [D]`, `COUPLINGS-DETERMINE [T]`, and
  `MEASURE-BORN-VERB [D]` are public lineage, but none binds a completion-grade
  object to this QDD action.
- The displayed `Q(psi)=(psi psi^dagger,psi psi^T)` in the open row is not yet
  a typed total map with a resolved ring, domain, carrier, and equality.

## 2. Fourteen-item inventory

| # | required public item | result | exact residual and nearest non-canonical candidate |
|---:|---|---|---|
| 1 | coefficient ring | `MISSING` | No QDD-bound public `coefficient_ring_id`. `P-DMATTER-TOTAL-1-DEFINITION-CANDIDATE.md` Section 2 proposes rational coefficients; `P-DMATTER-TOTAL-1-ROUTE-A-PROPOSAL-ID-PACKAGE.json` proposes `CAND-COEFFICIENT-RING-Q`. |
| 2 | effective carrier | `MISSING` | No public QDD carrier/domain binding. The definition candidate Section 1 proposes `CAND-CARRIER-BALANCED-PISTON4`. |
| 3 | common total domain | `MISSING` | `dom(D_matter)` remains partial and unresolved. `P-DMATTER-TOTAL-1-K0-HOUSEHOLDER-SOURCE-RULE-OWNER-FREEZE.md` Sections 2 and 12.1 propose `CAND-QDD-TOTALITY-DOMAIN-K0-ANCHORED-N0`; the Omega0 freeze keeps `public_Dmatter_domain_id` unresolved. |
| 4 | orbit-to-amplitude bridge | `MISSING` | No public map or binding gate. The Householder freeze Sections 2 and 12.1 propose `CAND-QDD-K0-TO-HQ-BALANCED-AMPLITUDE-N0`; the older Route A package proposes `CAND-MAP-ORBIT-TO-AMPLITUDE-B0-N0`. |
| 5 | Gram | `MISSING` | Public Gram identities do not select a typed QDD Gram. The definition candidate Section 2 proposes `CAND-GRAM-GALOIS-Q4-NORMALIZED`. |
| 6 | dagger | `MISSING` | No QDD-bound public dagger. The definition candidate Section 2 proposes `CAND-DAGGER-Q`. |
| 7 | transpose | `MISSING` | No QDD-bound public transpose. The definition candidate Section 2 proposes `CAND-TRANSPOSE-Q`. |
| 8 | QCarrier equality | `MISSING` | No public equality for the unresolved QDD carrier. The definition candidate Section 3 proposes `CAND-QCARRIER-EQ-COMPONENTWISE-Q`. |
| 9 | `Q` map | `MISSING` | The open-row formula is not a resolved typed total map. The definition candidate Section 3 proposes `CAND-Q-ORDERED-PAIR-Q4`. |
| 10 | effects | `MISSING` | No physical public `effect_ids`. The definition candidate Section 4 proposes `CAND-EFFECT-GRAM-LOW/HIGH`; `P-DMATTER-TOTAL-1-PHYSICAL-INSTRUMENT-PREDEFINITION.md` forbids those algebraic effects from filling the physical slot. |
| 11 | Born pairing | `MISSING` | `MEASURE-BORN-VERB` does not supply the QDD pairing. `P-DMATTER-TOTAL-1-K0-PHYSICAL-ROLE-INPUT-DOMAIN-OWNER-FREEZE.md` Sections 4 and 12.2 propose `CAND-QDD-MAP-K0-HH-BORN-FULL-STATE`; the public `born_pairing_id` remains unresolved. |
| 12 | MatterData schema | `MISSING` | No complete public field manifest. The Route A package proposes `CAND-RECORD-CANDIDATE-QUADRATIC-DATA`, but all five rows retain `public_contract_state: UNRESOLVED`; `P-DMATTER-TOTAL-1-A01-A15-RESOLUTION-MAP.md` Section 4 records A08 as partial. |
| 13 | exact write map | `MISSING` | No public write-map ID and field ownership. The Route A package proposes `CAND-MAP-D-SCOPED`; the resolution map Section 4 records A09 as partial. |
| 14 | complete dependency graph | `MISSING` | No complete public DAG or exact public acyclicity certificate. The resolution map Section 6 records A12 as partial and its candidate core as incomplete. |

```text
PUBLIC   0
MISSING 14
```

The result is an inventory, not a claim that the candidate formulas are
wrong. It says that none of the fourteen completion-grade bindings is yet
public.

## 3. Gate, evidence, and falsifier state

`canon/GATES.tsv` contains ten gates and no QDD or `D_matter` binding gate.
The QDD normative gate slot is blank, no matching public probe directory or
`PREREG.md` exists, and `canon/EVIDENCE.tsv` records QDD as `INLINE_CANON`
evidence at `inline`, with hash mode `registry-scope-sha256-v1` and
architecture requirement `none`. Existing Born, log-projection, and
observer-writeback gates cannot substitute for the missing binding gate.

All five registered negative conditions remain `LIVE / UNEVALUATED`; none is
fired and none is cleared:

1. the action is ill typed;
2. an included field is not constant on `Q`-fibers;
3. two states distinguished by the typed `D_matter` action have equal `Q`;
4. normalization fails;
5. an unregistered input is required.

## 4. Boundary exposed by this inventory

Before a future QDD decision, all fourteen required public bindings must be
resolved collectively and a scope-valid public binding gate must exist. This
inventory does not require one package to supply them and does not open any
next action.

Any candidate-definition package, preregistration, probe, immutable pin,
formal run, result, or Canon fold requires a separate public claim and the
normal policy sequence. All are outside this file and claim comment
`5093431422`.

This audit creates no definition, candidate ID, probe, verifier, result,
evidence, gate, dependency, owner decision, or Canon change. It does not
authorize further definition-corpus growth in place of the missing typed
bindings.
