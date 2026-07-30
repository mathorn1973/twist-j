# P-DMATTER-TOTAL-1 OD1 to OD4 Owner Ruling (NON-CANONICAL)

```text
STATUS:              OWNER-ADOPTED DEFINITION RULING
AUTHORITY:           NOT CANON
PUBLIC BASE:         Public Canon v23
PUBLIC CANON TAG:    canon-v23
ACTIVATION COMMIT:   4ac41b4fac3a3794a6e9d5be1e2027d324edb806
CONTENT COMMIT:      7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:       f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:         116017
PUBLIC MAIN BASE:    de32e7786599870db5b09144e68717023810b4e8
RESOLUTION MAP HASH: 2480f917178b4fdb3c7ff0faeff31521c45042572dcec1b77e2b7d07bbb578cc
QDD STATUS:          O / STOP, unchanged
FORMAL RUN:          NONE
REGISTRY CHANGE:     NONE
GATE CHANGE:         NONE
```

This ruling records the owner's adoption of OD1 to OD4 from
`P-DMATTER-TOTAL-1-A01-A15-RESOLUTION-MAP.md`. It fixes four definition
choices and nothing stronger. It does not fill a public identifier slot,
change the Canon, open a probe, or move `QUADRATIC-DECODER-DATA`.

The companion
`P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json` transcribes this ruling
against every slot of `DEF-DECODER-COMPLETION-CONTRACT`. The JSON file is a
non-canonical skeleton, not a submitted public completion.

## 0. Falsification first

This ruling is violated if a later candidate does any of the following
without a new owner ruling made before evaluation:

1. drops, adds, reassigns, or marks as `AUXILIARY` any of the five adopted
   record fields;
2. calls `D_scoped` a stream or infers a layer or gate from its stage and leg;
3. inserts a hybrid label without the missing source object, module, equality,
   total map, endpoints, and gate;
4. reconstructs `K_a` from `E_a` or fills physical effect or instrument
   slots with the algebraic effect candidates;
5. infers terminality from `READOUT`, an emit rule, or `feeds_U=FALSE`;
6. treats an `UNRESOLVED` identifier as resolved;
7. moves the parent QDD row from `O / STOP`.

These are definition failures and route `STOP`. They are not negative
scientific results. For a decoder classification, `NONUNIQUE` or `EMPTY`
becomes meaningful only after the complete decoder universe and its decoder
equivalence are frozen. For the separate physical-instrument classification,
the admissible instrument universe and both its `K`-level and `E`-level
equivalences must be frozen.

Changing any adopted role, record semantics, hybrid boundary, or `K/E`
distinction after an audit or classification has opened returns
`FIRE-POSTHOC`.

## 1. OD1 adopted: exact field ownership

For the scoped `CandidateQuadraticData` record, exactly these five fields are
adopted:

```text
support_state
total_weight
branch_weights
density_state
normalized_weight_state
```

Every field has:

```text
record owner  = CandidateQuadraticData
role          = READOUT
stage owner   = D_matter
reading leg   = D_quadratic.
```

No field is `AUXILIARY`, no field uses `NOT_APPLICABLE`, and no additional
scoped field is created by this ruling.

This fixes semantic ownership only. It does not create the required public
`record_id`, `field_id`, `field_type_id`, carrier, normalization, equality,
source, write-map, or emit-rule identifiers. Therefore A08 and A09 remain
`PARTIAL`. The A10 semantic choice is fixed, but its strict manifest rows
remain `UNRESOLVED` until every required public identifier and typed stage
and leg row exists.

`READOUT`, `D_matter`, and `D_quadratic` are three contract assignments. They
do not imply an L1 to L6 layer, a physical measure, or terminality.

## 2. OD2 adopted: anchored record, not stream

Freeze

```text
D_scoped : K0 -> CandidateQuadraticData
```

as one total tagged record for each `kappa_x`, read from the frozen pre-update
checkpoint at `n=0`.

`D_scoped` is not an L5 stream. It has no output index, shift law, stream
equality, or stream emit rule. No time-indexed extension is inherited merely
because its domain elements are forward orbits.

A future stream requires a separate total definition:

```text
S_scoped : K0 -> CandidateQuadraticData^(N_0)
```

including its exact term, read convention, shift law, equality, emit rule,
layer endpoints, dependencies, and public gate.

Until that object exists:

```text
S_scoped                UNRESOLVED
cross-layer assignments UNRESOLVED
core public gate        UNRESOLVED
A13                     OPEN / STOP.
```

No existing log-projection or Born-reading gate is inherited automatically.

## 3. OD3 adopted: the hybrid is a separate open extension

The hybrid construction remains a separate unresolved extension:

```text
QDD-HYBRID-CARRIER-BRIDGE  O / STOP.
```

The exact base core may be transcribed without inserting a hybrid label. This
does not make A02 or the parent QDD manifest complete.

The following remain unresolved:

```text
GyronObject
L_label and its equality
ell_gyron and its totality domain
C_hyb and G_hyb
j_hyb
source and target layers
public transport gate
physical-carrier identification.
```

`GYRON-DENSITY` does not define any of these objects. No unpublished carrier
or physical bridge may be imported.

## 4. OD4 adopted: the K/E firewall

`E_low`, `E_high`, their exact weights, and

```text
w_low + w_high = m
```

remain algebraic content only.

No physical instrument, physical effect selection, outcome semantics,
post-event rule, or physical Born-pairing identifier is adopted. In
particular:

```text
K_a must not be inferred from E_a.
Equal effects do not imply equal instruments.
K_a := E_a is not adopted by this ruling.
```

A later predefinition may include `K_a=E_a` as an explicit pre-result
candidate. It may not recover that equality after inspecting effects or
outputs, and the equality alone would not supply apparatus, outcome, or
post-event semantics.

Before any enumeration, the separate physical-effect predefinition must
freeze:

```text
the admissible instrument universe
every exact K_a
every E_a = K_a^sharp K_a certificate
K-level and E-level equivalence
outcome semantics
post-event semantics
coarse-graining
Born pairing
normalization and completeness
the MatterData fields that read each outcome
PASS, NONUNIQUE, EMPTY, and STOP semantics.
```

Therefore A11 remains `PARTIAL`, and
`QDD-PHYSICAL-EFFECT-SELECTION` remains `O / STOP`.

## 5. Exact consequences for A08 to A14

```text
A08
    Exactly five semantic fields and their ownership are fixed.
    Public field rows and IDs remain incomplete.

A09
    D_scoped remains the exact write map at the value level.
    Public write-map and record-owner IDs remain UNRESOLVED.

A10
    The five role, stage, and leg assignments are fixed.
    The public stage_manifest and leg_manifest remain incomplete.

A11
    Algebraic effects are exact.
    Physical instruments, effects, outcomes, and Born IDs remain UNRESOLVED.

A13
    D_scoped is one anchored record.
    L-layer assignments, stream semantics, and gates remain UNRESOLVED.

A14
    The semantic write-target set is exactly the five fields.
    feeds_U = FALSE remains exact.
    Public write_target_ids, terminal_output_ids, and
    terminality_basis_id remain UNRESOLVED.
```

`feeds_U=FALSE` is stage-local. It does not establish completion-wide
terminality and does not close `OBSERVER-WRITE-PORT`.

## 6. Manifest-skeleton rules

The companion JSON follows these rules:

1. `contract_manifest` contains every slot named by
   `DEF-DECODER-COMPLETION-CONTRACT`.
2. Its row inventory is scoped to the adopted QDD Route A core. The separate
   hybrid extension and non-QDD stages and legs are not inserted as core
   contract rows.
3. Every missing contract identifier is the literal string `UNRESOLVED`, or
   a one-element `["UNRESOLVED"]` array for a plural ID slot.
4. There is no `null` and no `NOT_APPLICABLE`.
5. Keys beginning `_` are skeleton metadata and are not contract slots.
6. `proposal_local_catalog` records exact values and local row handles without
   promoting them to public identifiers.
7. Repeated `UNRESOLVED` values do not satisfy uniqueness. Uniqueness is
   tested only after distinct public field identifiers exist.
8. `presence_state=RESOLVED` records the adopted presence of each field. It
   does not resolve that row's identifier-valued slots.
9. All A01 to A15 `value_state` entries remain `UNRESOLVED` in the strict
   contract ledger.

The skeleton is therefore exact about both what is known and what is not.

## 7. Status readback

```text
OD1 field ownership               ADOPTED
OD2 anchored-record semantics     ADOPTED
OD3 hybrid separation             ADOPTED AS OPEN BOUNDARY
OD4 K/E firewall                  ADOPTED

A08                               PARTIAL
A09                               PARTIAL
A10 semantic choice               FIXED
A10 strict manifest               UNRESOLVED
A11                               PARTIAL / O-STOP
A13                               OPEN / STOP
A14                               PARTIAL

QDD scoped dictionary             owner-adopted proposal
QDD hybrid bridge                 O / STOP
QDD physical effect selection     O / STOP
QDD independent factorization     O / STOP
QUADRATIC-DECODER-DATA            O / STOP.
```

The controlling sentence is:

> `READOUT` does not determine a layer, an anchored record is not a stream,
> an algebraic effect is not an instrument, and `feeds_U=FALSE` is not a
> terminality proof.

## 8. Next allowed actions

1. Audit the companion JSON for complete schema coverage and literal
   unresolvedness.
2. Assign proposal-local IDs only in a separate definition package, with no
   claim that they are public identifiers.
3. Decide the remaining A02 hybrid objects or keep the parent QDD row at
   `STOP`.
4. Prepare the separate physical-instrument predefinition required by OD4.
5. Define `S_scoped` only if a time-indexed stream is actually intended.
6. Propose a normative fold only after every required public identifier,
   dependency, endpoint, and gate is exact.

No formal scientific run is authorized by this ruling.
