# P-DMATTER-TOTAL-1 predefinition ruling (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION`

This note is a definition package proposal. It is not a public probe, does
not authorize a verifier or run, changes no Canon status, and creates no new
claim. The public lock is issue #107.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          QUADRATIC-DECODER-DATA [O]
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
normative layer:    MULTI
future probe:       P-DMATTER-TOTAL-1
```

The v14 `DEF-DECODER-COMPLETION-CONTRACT` is the controlling schema. It
authorizes no probe and proves no existence, totality, factorization,
physical bridge, completeness, or terminality statement.

## One exact target

The future candidate concerns only fields owned by the registered
`D_quadratic` reading leg at stage `D_matter`. The predefinition package must
freeze candidate objects with the typed shape

```text
beta        : K_phys -> C
Q           : C -> QCarrier
F_candidate : im(Q) -> MatterData_quadratic
D_candidate : K_phys -> MatterData_quadratic

target test:
D_candidate ?= F_candidate o Q o beta.
```

Here `K_phys`, `C`, `QCarrier`, `MatterData_quadratic`, all equalities, and
all four maps are names for objects that must be published before the lane
can become `READY`. The equality and normalization are targets of the later
pinned probe, not predefinition assumptions.

The linear `CODEC-TR4` leg, the binary Thue-Morse/census leg, cross-leg or
state reconstruction, and post-state instrument selection are excluded.

## Required manifest freeze

Every required identifier-valued slot in the controlling contract must hold
a resolvable public identifier or `UNRESOLVED`. `NOT_APPLICABLE` is permitted
only in the explicit state or leg cases allowed by v14 and then requires a
resolvable basis item. A bare null, prose placeholder, private input, or
choice made from later output is forbidden.

The table is a QDD delta overlay, not a shortened replacement for the v14
contract. The submitted candidate must contain the complete public contract,
including every exact slot in:

```text
carrier_manifest[]
record_field_manifest[]
stage_manifest[]
leg_manifest[]
bridge_manifest[]
quadratic_manifest
physics_manifest
measure_manifest
closure_manifest
obligation_manifest[]
```

| Block | QDD-specific freeze | Current ruling |
| --- | --- | --- |
| identity | `candidate_id`, `public_pin_id`, `read_convention_id`, `history_equivalence_id`, `region_id`, `coarse_graining_id` | `UNRESOLVED` |
| carrier | `carrier_id`, parent carrier, inclusion or quotient map, equality, coefficient object, `K_phys`, and effective carrier `C` | `UNRESOLVED` |
| bridge | orbit-to-amplitude `beta`, source, target, domain, codomain, map, dependencies, layer endpoints and gate IDs | `UNRESOLVED` |
| quadratic | coefficient ring, Gram, dagger, transpose, `QCarrier`, `QCarrier` equality, exact `Q`, effects, Born pairing, and candidate factor map | `UNRESOLVED` |
| record | complete owned-field rows, including `record_id`, `field_id`, field type, role, carrier, domain, normalization, equality, source item, write map, presence state, absence basis, emit rule, stage and leg | `UNRESOLVED` |
| stage and leg | `D_matter` and `D_quadratic` domain, codomain, map, totality domain, dependencies and complete owned-field list | `UNRESOLVED` |
| physics and measure | every contract slot, with public scope ownership; no physical source, current, propagation, detector, measure, metrology, or scheme is inferred from syntax | `UNRESOLVED` |
| dependencies | every item read by every map, including the public floor below, plus a declared DAG and exact acyclicity test | `UNRESOLVED` |
| closure and obligations | write targets, `feeds_U`, terminal outputs and basis, plus every requirement owner, value state and basis item | `UNRESOLVED` |

The currently registered dependency floor is:

```text
QUADRATIC-DECODER-DATA -> DEF-ARCHITECTURE
QUADRATIC-DECODER-DATA -> DEF-DECODER-MATTER
QUADRATIC-DECODER-DATA -> READING-SPLIT
QUADRATIC-DECODER-DATA -> COUPLINGS-DETERMINE
QUADRATIC-DECODER-DATA -> MEASURE-BORN-VERB
```

These edges are inherited bounds, not a declaration that the future graph is
complete. The ruling must also decide publicly whether use of
`DEF-DECODER-COMPLETION-CONTRACT` requires a new declared dependency; v14 has
no such edge for `QUADRATIC-DECODER-DATA`. Any actual cross-layer map must
identify its endpoints and an existing public gate. If no such gate exists,
the package remains `STOP` until a separate definition-only fold creates it.

## Acceptance test before a formal probe exists

The ruling may be accepted as `READY` only if a reviewer can establish all
of the following without deciding the scientific target:

1. every included identifier resolves publicly at the pinned commit;
2. each output field has exactly one record owner, one stage owner, and one
   permitted reading-leg assignment;
3. every candidate domain, codomain, equality and map is explicit and the
   proposed verifier can decide all required equalities exactly;
4. the factorization equation, Q-fiber constancy predicate, normalization
   predicate and hidden-input predicate are frozen as tests, without assuming
   that they pass;
5. the complete dependency list and an exact DAG/acyclicity checker are
   frozen, without assuming the resulting graph passes;
6. every real layer lift has its own public gate;
7. all excluded legs and instrument claims remain absent;
8. both positive and negative scientific outcomes remain reachable under
   the frozen routing.

If a definition or decision procedure is missing, the only valid state is
`STOP`. A well-typed candidate that later fails factorization or normalization
is a valid negative scientific result, not a predefinition failure.
Syntactic conformance to the manifest is not scientific evidence.

## Future formal lane, still forbidden

Only after this definition package is reviewed, merged, and read back from
public `main` may a separate commit create:

```text
branch: probe/P-DMATTER-TOTAL-1
path:   probes/P-DMATTER-TOTAL-1/
```

That future probe must freeze the six policy fields and an accepted exact
verifier before execution. Its positive route requires every frozen field to
factor through `Q` with exact normalization and a complete acyclic dependency
graph. Its negative route requires a typed fiber witness, normalization
failure, ill-typed action, or unregistered input. Missing definitions remain
`STOP`, not a negative scientific result.

## Debt firewall

This note neither closes `QUADRATIC-DECODER-DATA` nor creates a replacement
umbrella row. It does not touch `OBSERVER-WRITE-PORT`, geometry, clock,
metrology, state update, or decoder completeness. Its only purpose is to turn
one existing `STOP` owner row into a finite, reviewable definition task.
