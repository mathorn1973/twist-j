# P-DMATTER-TOTAL-1 QDD Public Requirements Audit (NON-CANONICAL)

```text
STATUS:                    PUBLIC-SOURCE INVENTORY / V27 DAG REFRESH
AUTHORITY:                 NOT CANON
PUBLIC MAIN BASE:          b0a53eb65e3a3511af28f5876b9d1bb882bda160
PUBLIC CANON:              Public Canon v27 / canon-v27
PUBLIC CONTENT COMMIT:     116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256:      c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
PUBLIC CANON BYTES:        150959
CLAIM ISSUE / COMMENT:     107 / 5093431422
SCOPE:                     EXACT 14-ITEM QUADRATIC-DECODER-DATA STOP INVENTORY
INVENTORY RULE:            PUBLIC ONLY WITH AN EXACT RESOLVABLE TYPED PUBLIC ID
OWNER DECISION:            BINDING-PACKAGE / 2026-07-30
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

`canon/GATES.tsv` contains eleven gates and no QDD or `D_matter` binding gate.
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

## 4. The binding DAG

The fourteen missing bindings are not fourteen independent owner choices.
They form five typed blocks. The arrows below are dependency arrows, not
state-update arrows:

```text
B1 SOURCE
   public headed-orbit carrier/equality
       -> common total D_matter domain
       -> orbit-to-amplitude bridge

B2 QUADRATIC ALGEBRA
   coefficient ring
       -> effective amplitude carrier
       -> Gram + dagger + transpose
       -> QCarrier equality + Q

B1 + B2
       -> B3 PHYSICAL READ
          effects + Born pairing

B1 + B2 + B3
       -> B4 OUTPUT
          complete MatterData schema
              -> exact D_matter write map

B1 + B2 + B3 + B4
       -> B5 CLOSURE
          complete dependency graph
              -> exact acyclicity certificate
              -> layer endpoints and a scope-valid binding gate
```

The five blocks cover the registered inventory exactly:

| block | inventory items | current public state |
|---|---|---|
| B1 SOURCE | common total domain, orbit-to-amplitude bridge | `MISSING` |
| B2 QUADRATIC ALGEBRA | coefficient ring, effective carrier, Gram, dagger, transpose, QCarrier equality, `Q` | `MISSING` |
| B3 PHYSICAL READ | effects, Born pairing | `MISSING` |
| B4 OUTPUT | MatterData schema, exact write map | `MISSING` |
| B5 CLOSURE | complete dependency graph, including its layer/gate binding | `MISSING` |

This decomposition prevents two invalid shortcuts.

First, publishing B2 alone cannot close QDD: the exact proposal-local Gram
and finite `Q` calculations do not select a physical read, own a MatterData
field, or bind a decoder domain. Second, publishing B1 and B4 without B3
would make the write rule a relabeling of algebraic output rather than the
registered quadratic/Born `D_matter` action.

The proposal-local owner signature

```text
OMEGA_0 with [K0] = [Krange_0]
```

is the nearest B1 candidate. It is not public `K`, is not
`dom(D_matter)`, and does not supply physical occurrence. The Route A
rational Gram package is the nearest B2 candidate. The Q2 apparatus and
preparation freezes are candidate inputs to B3, but retain unresolved
source-selected image, physical outcome, Born, occurrence, layer, and gate
fields. The five-field tagged record is the nearest B4 candidate. No
proposal-local package supplies B5.

The next admissible owner action must therefore choose one of:

```text
BINDING-PACKAGE
    freeze B1 through B5 together as one prospective public definition,
    with every identifier, equality, map, dependency, layer endpoint, and
    gate explicit while both positive and registered negative outcomes
    remain reachable;

SOURCE-ONLY
    freeze only B1 as a separately scoped public definition and leave QDD
    O / STOP, with no claim that B2 through B5 follow;

RETAIN-STOP
    decline a public source/domain binding and keep all five blocks open.
```

`BINDING-PACKAGE` is the only listed route that would resolve every
registered STOP input. `SOURCE-ONLY` is a valid preparatory action but cannot
move QDD from `O / STOP`. Neither option is itself authorization to create a
preregistration or run a verifier.

The owner selected `BINDING-PACKAGE` on 2026-07-30. Its prospective typed
content is recorded in
`P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md`. The selection changes no
public result in this inventory until a later normative fold adopts it.

## 5. Boundary exposed by this inventory

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
