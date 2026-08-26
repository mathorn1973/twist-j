# QDD STOP inventory refresh at Public Canon v65 (NON-CANONICAL)

```text
STATUS:                    PUBLIC-SOURCE INVENTORY / V65 REFRESH
AUTHORITY:                 NOT CANON
PUBLIC CANON:              Public Canon v65 / canon-v65
PUBLIC CONTENT COMMIT:     de0806dd579e303e102f9961c068852095e19f07
PUBLIC CANON SHA-256:      34a2833153a917441c3e4df7e2406f34cf0e62ecafbf366eddfa6615dc8fb6d2
PUBLIC CANON BYTES:        339260
SCOPE:                     EXACT 14-ITEM QUADRATIC-DECODER-DATA STOP INVENTORY
INVENTORY RULE:            PUBLIC ONLY WITH AN EXACT RESOLVABLE TYPED PUBLIC ID
SUPERSEDES (INVENTORY):    notes/canon/P-DMATTER-TOTAL-1-QDD-PUBLIC-REQUIREMENTS-AUDIT.md
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
BINDING GATE:              MISSING
CANON/TABLE/STATUS CHANGE: NONE
QDD STATUS:                O / STOP, unchanged
RESULT AS FOUND (v65):     PUBLIC 13 / MISSING 1
OWNER RULING:              WIRE-THE-ROW, 2026-08-26
OUTCOME:                   folded as Public Canon v66; re-runs PUBLIC 14 / MISSING 0
```

> **Outcome.** This audit was written against Public Canon v65 and found item 14
> missing. The owner selected `WIRE-THE-ROW` on 2026-08-26 and the fourteen
> `REQUIRES` edges were folded into the dependency ledger as **Public Canon
> v66**. The checker reads the live Canon version, so it now reports
> `PUBLIC 14 / MISSING 0` and check 12 passes. Sections 3, 5 and 7 below
> describe the v65 state that motivated the fold and are kept as the record of
> it; section 7 records which route was taken. The four residuals of section 6
> are untouched by the fold and remain open.

## 1. Why this file exists

`notes/canon/P-DMATTER-TOTAL-1-QDD-PUBLIC-REQUIREMENTS-AUDIT.md` recorded the
fourteen-item `QUADRATIC-DECODER-DATA` STOP inventory at **Public Canon v27**
and reported:

```text
PUBLIC   0
MISSING 14
```

That inventory is thirty-eight Canon versions old. It is still the most recent
written inventory of the row, and the decoder lane is still described as
blocked on missing typed definitions. This file re-runs the same inventory,
under the same decision rule, against the ledger at v65.

The result has almost completely inverted, and what survives is one specific,
small, mechanical gap rather than a research obstruction.

## 2. Decision rule

Unchanged from the v27 audit. The authoritative requirement is the
`QUADRATIC-DECODER-DATA [O]` falsifier in `canon/REGISTRY.tsv`. A requirement
counts as `PUBLIC` only when the public ledger resolves the exact typed object.
A displayed formula, a generic theorem, a schema slot, or a `notes/`-local
`CAND-*` identifier does not count.

The frozen STOP clause is pinned verbatim by the checker:

```text
STOP until the coefficient ring, effective carrier, common total domain,
orbit-to-amplitude bridge, Gram, dagger, transpose, QCarrier equality, Q,
effects, Born pairing, MatterData schema, write map, and complete dependency
graph are public
```

The checker splits that clause itself and asserts it names exactly fourteen
inputs, so the inventory cannot silently drift from the registry text.

## 3. Fourteen-item inventory at v65

| # | required public item | v27 | v65 | resolving public normative ID |
|---:|---|---|---|---|
| 1 | coefficient ring | `MISSING` | `PUBLIC` | `DEF-QDD-COEFFICIENT-Q` |
| 2 | effective carrier | `MISSING` | `PUBLIC` | `DEF-QDD-BALANCED-PISTON` |
| 3 | common total domain | `MISSING` | `PUBLIC` | `DEF-QDD-DOMAIN-K0` |
| 4 | orbit-to-amplitude bridge | `MISSING` | `PUBLIC` | `DEF-QDD-AMPLITUDE-B0` |
| 5 | Gram | `MISSING` | `PUBLIC` | `DEF-QDD-GRAM` |
| 6 | dagger | `MISSING` | `PUBLIC` | `DEF-QDD-DAGGER` |
| 7 | transpose | `MISSING` | `PUBLIC` | `DEF-QDD-TRANSPOSE` |
| 8 | QCarrier equality | `MISSING` | `PUBLIC` | `DEF-QDD-QCARRIER-EQUALITY` |
| 9 | `Q` | `MISSING` | `PUBLIC` | `DEF-QDD-QPAIR` |
| 10 | effects | `MISSING` | `PUBLIC` | `DEF-QDD-PROJECTOR-LOW`, `DEF-QDD-PROJECTOR-HIGH` |
| 11 | Born pairing | `MISSING` | `PUBLIC` | `DEF-QDD-BRANCH-WEIGHT-PAIRING` |
| 12 | MatterData schema | `MISSING` | `PUBLIC` | `DEF-QDD-MATTER-RECORD` |
| 13 | exact write map | `MISSING` | `PUBLIC` | `DEF-QDD-DIRECT-WRITE` |
| 14 | complete dependency graph | `MISSING` | `MISSING` | see section 5 |

```text
PUBLIC  13
MISSING  1
```

Each of items 1 to 13 is a `DEFINITION` row in `canon/NORMATIVE.tsv` at layer
`L1`, carries its definition text in the `### QDD Route A dictionary` block of
`canon/CANON.md`, and is anchored by an exact canon phrase the checker matches.
Three anchors are near-verbatim restatements of the registry wording:

- `DEF-QDD-DOMAIN-K0` reads "the common total domain of the quadratic
  `D_matter` leg", which is item 3 word for word;
- `DEF-QDD-QPAIR` reads `Q_QDD(v) = (A_dagger, A_T) = (v v^dagger, v v^T)`,
  which is the `Q(psi) = (psi psi^dagger, psi psi^T)` displayed in the open row;
- `DEF-QDD-PROJECTOR-LOW` and `DEF-QDD-PROJECTOR-HIGH` are declared as the
  first and second members of "the frozen ordered effect pair", which is item 10.

## 4. What changed between v27 and v65

The v27 audit decomposed the fourteen items into five typed blocks and recorded
every block as `MISSING`. At v65:

| block | inventory items | v27 | v65 |
|---|---|---|---|
| B1 SOURCE | common total domain, orbit-to-amplitude bridge | `MISSING` | `PUBLIC` |
| B2 QUADRATIC ALGEBRA | coefficient ring, effective carrier, Gram, dagger, transpose, QCarrier equality, `Q` | `MISSING` | `PUBLIC` |
| B3 PHYSICAL READ | effects, Born pairing | `MISSING` | `PUBLIC` (algebraic; residual 4) |
| B4 OUTPUT | MatterData schema, exact write map | `MISSING` | `PUBLIC` |
| B5 CLOSURE | complete dependency graph | `MISSING` | `PARTIAL` (section 5) |

The owner selected `BINDING-PACKAGE` on 2026-07-30, the route the v27 audit
identified as "the only listed route that would resolve every registered STOP
input". That package was folded into the Canon. The v27 audit correctly said
the selection "changes no public result in this inventory until a later
normative fold adopts it". The fold happened; the inventory was never re-run.

Two further facts show how far the lane moved:

- `QDD-ALGEBRAIC-FACTORIZATION [T]` proves
  `D_QDD_direct = F_QDD o Q_QDD o beta_QDD` field by field on all 15625
  checkpoints, with the record total, exactly normalized on the 15600 supported
  heads, constant on each of the 313 `Q_QDD`-fibres and injective on
  `QCarrier_QDD`, on `two-architecture` evidence at `reproduce/qdd-route-a`.
  That is the registry's positive-closure phrase "exact factor maps through `Q`
  produce every frozen `D_matter` field with exact normalization", discharged
  on the frozen finite domain.
- The `DEF-QDD-*` closure is 27 nodes, every node registered, and acyclic. The
  `EFFECT_SHADOW_MINIMAL` independence firewall holds structurally: the
  17-node definitional closure of `DEF-QDD-DIRECT-WRITE` contains no
  factor-side object.

## 5. The one thing still missing: item 14

Item 14 asks for a **complete dependency graph**. The graph exists and is
acyclic — but the open row is not on it.

`canon/DEPENDENCIES.tsv` gives `QUADRATIC-DECODER-DATA` exactly five
`REQUIRES` edges:

```text
QUADRATIC-DECODER-DATA -> DEF-ARCHITECTURE
QUADRATIC-DECODER-DATA -> DEF-DECODER-MATTER
QUADRATIC-DECODER-DATA -> READING-SPLIT
QUADRATIC-DECODER-DATA -> COUPLINGS-DETERMINE
QUADRATIC-DECODER-DATA -> MEASURE-BORN-VERB
```

These are the same five the v27 audit called "public lineage", and it noted
then that "none binds a completion-grade object to this QDD action". That is
still exactly true. **Zero of the seventeen `DEF-QDD-*` items appear in the
row's dependency closure.** The row names its fourteen required inputs in prose
and reaches none of them through the ledger.

The wiring is not absent from the Canon — it is routed around the parent. The
frontier debt map the checker emits makes this visible. As read at v65, before
the fold:

```text
live O/H rows                        30
shared architecture baseline          9 definitions
QDD-TERMINAL-EVENT-SEMANTICS        +18
QDD-INSTRUMENT-APPARATUS             +5
TRACEKERNEL-CURVATURE-FORCING        +2
MINIMAL-READ-DERIVATION              +1
METRO-ADMISSIBILITY-DIM              +1
LAMBDA-COCYCLE-ANGLES                +1
rows owning no definition above it   24 of 30
```

At v66 the same map reads `QUADRATIC-DECODER-DATA +14` and `23 of 30`, which is
the whole effect of the fold.

`QDD-TERMINAL-EVENT-SEMANTICS`, a *child* obligation, reaches all seventeen
`DEF-QDD-*` definitions through the theorem chain. `QUADRATIC-DECODER-DATA`,
the *parent* row that names them, reaches none and sits at `+0`, in the same
bucket as twenty-three rows that genuinely have no definitional apparatus at
all.

So item 14 is `MISSING` on a technicality — and the technicality is the whole
point of a dependency ledger. A "complete dependency graph" for the quadratic
`D_matter` action that does not connect the action to its coefficient ring,
carrier, Gram, `Q`, effects, schema and write map is not complete. The fix is
a small sealed ledger fold adding the missing `REQUIRES` edges with their
bases; it changes no status, no scope, no evidence and no gate.

## 6. Residuals outside the inventory

Four items sit outside the fourteen and none is closed by this audit:

1. **No binding gate.** `canon/GATES.tsv` carries eleven gates and none is a
   QDD or `D_matter` gate. The registry falsifier does not name a gate among
   its fourteen inputs, so this is not a STOP-clause item; but the v27 audit
   put "layer endpoints and a scope-valid binding gate" inside its B5, and the
   `status-separation` release audit records "no gate and no L6 row exist" as
   part of the current QDD boundary. Whether the row can close without one is
   an owner question, not an inventory question.
2. **Domain scope.** `DEF-QDD-DOMAIN-K0` declares `K_QDD` total *for the
   quadratic leg*, as the set of pointed forward sequences with distinguished
   head `n = 0`. `DEF-DECODER-MATTER` keeps `dom(D_matter)` a declared subset
   of `K`, the set of forward `U`-orbits, and no `K_QDD = K` identity is
   registered. `QDD-ALGEBRAIC-FACTORIZATION` states explicitly that it is "not
   a completion, totality or uniqueness claim for `D_matter`".
3. **The pair does not separate on the frozen carrier.**
   `QDD-QCARRIER-DIAGONAL-BOUNDARY [T]` proves that on `V_eff` the two typed
   slots coincide, `A_dagger = A_T = v v^T`, because the dagger of
   `DEF-QDD-DAGGER` is the transpose over `Q`. Both slots remain typed and
   declared, but the frozen domain does not test their difference. Any reading
   that leans on the *pair* structure of `Q` is, on this carrier, leaning on a
   distinction the evidence does not exercise.
4. **The Born pairing is adopted, not derived.**
   `DEF-QDD-BRANCH-WEIGHT-PAIRING` is declared "an adopted dictionary input,
   not derived from `J` or from the projector identities". The factorization is
   therefore an exact identity *between adopted definitions*, which is what
   `QDD-ALGEBRAIC-FACTORIZATION` says it is.

Residuals 2 to 4 are declared boundaries in the Canon, not defects found here.
They are listed because a reader who sees `PUBLIC 13 / MISSING 1` should see
them in the same view.

## 7. What this inventory supports

`canon/REGISTRY.tsv` says the row is STOP *until* fourteen named inputs are
public. Thirteen are public and the fourteenth fails only because the row lacks
its own ledger edges. `canon/FRONTIER_PROGRAMS.tsv` still carries:

```text
QUADRATIC-DECODER-DATA	DECODER_CORE	ROOT	STOP	FORMAL
```

That label was correct at v27, when nothing was public. It is now carried by a
single missing set of dependency rows. The admissible owner actions are:

```text
WIRE-THE-ROW
    one sealed ledger fold adds the REQUIRES edges from
    QUADRATIC-DECODER-DATA to the DEF-QDD-* block it already names in prose,
    with a basis string per edge. No status, scope, evidence or gate moves.
    After it, the fourteen-item clause is discharged and the work_state
    question becomes live on the text as written.

CLAUSE-INCOMPLETE
    the fourteen-item clause no longer expresses what is actually missing; the
    registry falsifier is amended in a sealed fold to name the binding gate,
    the domain-exhaustion obligation, or whichever residual the owner holds to
    be a genuine STOP input, and the row stays STOP against the amended clause.
```

These are not exclusive: `WIRE-THE-ROW` is a hygiene fold that should happen
regardless of how the owner rules on the clause, because a dependency ledger
that omits the edges is wrong independently of what it implies for scheduling.

**Owner ruling, 2026-08-26: `WIRE-THE-ROW`.** The fourteen edges were folded
into `canon/DEPENDENCIES.tsv` as Public Canon v66, one edge per named object,
each with a basis naming the STOP-clause item it discharges. The fold moves no
claim, status, scope, evidence pointer or gate, and releases no lifecycle
event. `CLAUSE-INCOMPLETE` was not taken and remains available: the registry
falsifier still names exactly the fourteen items, and whether the binding gate
or the domain-exhaustion obligation belongs among them is still undecided.

What is not tenable is describing the lane as blocked on missing typed
definitions. It has not been since the binding package was folded. Thirteen of
the fourteen named objects are public, normative, L1, textually anchored, and
carried by a two-architecture reproduction.

## 8. Reproduction

From the repository root:

```sh
python3 notes/QDD-STOP-INVENTORY-V65/check_qdd_stop_inventory.py
```

Exact expected stdout is `EXPECTED.txt`. The checker uses the Python standard
library only, reads `canon/REGISTRY.tsv`, `canon/NORMATIVE.tsv`,
`canon/DEPENDENCIES.tsv`, `canon/EVIDENCE.tsv`, `canon/GATES.tsv` and
`canon/CANON.md`, and emits deterministic text.

Checks 01 to 11 are audit integrity: they verify the ledger state this file
reports, and the script exits non-zero if any of them breaks, so a later fold
that moves the row, the definitions, the closure or the evidence grade will
break the audit rather than silently invalidate it. Check 12 is the finding
itself, reported as `GAP`, not as an audit failure — it will start passing on
its own once the missing edges are folded in.

## 9. Boundary

This file is `NON-CANONICAL`. It creates no definition, candidate ID, probe,
preregistration, verifier, formal run, result, evidence row, gate, dependency,
owner decision or Canon change. It does not close, promote, or falsify
`QUADRATIC-DECODER-DATA`, which remains `O` and whose scheduler label remains
whatever `canon/FRONTIER_PROGRAMS.tsv` says until a sealed fold changes it.

It reports two facts: thirteen of the fourteen public inputs the registry names
as the condition for leaving STOP are, at Public Canon v65, public; and the
fourteenth is missing because the open row carries no dependency edge into the
definitional block that discharges the other thirteen.
