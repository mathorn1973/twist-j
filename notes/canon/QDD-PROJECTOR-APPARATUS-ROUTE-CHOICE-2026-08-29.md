# QDD Projector/Apparatus Route Choice (NON-CANONICAL)

```text
STATUS:                  OWNER-ADOPTED ARCHITECTURAL ROUTE CHOICE /
                         OWNER-GUIDANCE-ONLY / NOT CANON
AUTHORITY:               NO NORMATIVE AUTHORITY
DECISION DATE:           2026-08-29
CLAIM ISSUE:             107
PUBLIC BASE:             569fbf409c77e3bd83111dfb3c88d2748043d7e2
PUBLIC CANON:            Public Canon v69 / canon-v69
PUBLIC CONTENT COMMIT:   f15c228683f706e9b411125db75764bca4745465
PUBLIC CANON SHA-256:    0a97c67ce29e7545016471884a169822eec9bed4a0f33e7ff4ca232407333737
PUBLIC CANON BYTES:      361884
TIMING:                  POST-RESULT / RESULT-EXPOSED
SCIENTIFIC CREDIT:       NONE
DERIVATION STATUS:       NOT FORCED
UNIQUENESS STATUS:       NOT CLAIMED
CANONICITY STATUS:       NOT CLAIMED
ALTERNATIVE ROUTE:       UNADOPTED / NOT FALSIFIED /
                         NOT SHOWN COMPLETE
FORMAL RUN:              NONE
PROBE / PREREGISTRATION: NONE
CANON / TABLE CHANGE:    NONE
GATE / FRONTIER CHANGE:  NONE
QDD STATUS:              O / STOP, unchanged
```

This note records an owner choice of architecture. It changes no public
definition, claim, status, scope, dependency, gate, frontier row, count, hash,
tag, or release. It authorizes no probe and supplies no evidence for a
scientific claim. A later normative change, if any, must enter in the content
commit of a new Public Canon and pass the complete release procedure.

Upon reviewed merge and byte-for-byte public-main readback, this note freezes
owner guidance only.

## 1. Exact owner choice

The owner adopts `ALGEBRAIC-DMATTER` as the target contract architecture for
the QDD quadratic leg.

In that architecture, the existing `D_matter` slot is to be bound, on the
exact displayed scope only, by

```text
D_matter|_(K_QDD,D_quadratic)
    := D_QDD_direct
     : K_QDD -> MatterData_QDD.
```

Separately, the existing theorem-grade algebraic identity is

```text
D_QDD_direct = F_QDD o Q_QDD o beta_QDD.
```

The binding adopts the direct writer. The factorization theorem verifies an
equality of two expressions; it is not the definition source of the direct
writer and does not select this architecture.

The codomain is exactly the existing five-field `DEF-QDD-MATTER-RECORD`:

```text
support_state
total_weight
branch_weights
density_state
normalized_weight_state
```

All five fields are exact algebraic record data at L1 on this scope. In
particular, `normalized_weight_state` is an ordered normalized rational pair
with its zero marker. It is not, by this choice alone, an occurrence
probability, sampling law, random variable, physical event stream, or L6
measure.

The target quadratic manifest carries an ordered pair of algebraic projector
identifiers and an algebraic branch-weight pairing identifier:

```text
quadratic_manifest.projector_ids = (
    DEF-QDD-PROJECTOR-LOW,
    DEF-QDD-PROJECTOR-HIGH
)

quadratic_manifest.branch_weight_pairing_id =
    DEF-QDD-BRANCH-WEIGHT-PAIRING
```

This is a prospective architecture specification for a later normative fold.
This non-canonical note does not amend the current v69 manifest schema.

The current and selected-future surfaces are therefore distinct:

```text
v69 current:
    quadratic_manifest.effect_ids
    quadratic_manifest.born_pairing_id
    both topology and ownership remain exactly as published;
    effect_ids remains unresolved.

selected successor:
    quadratic_manifest.projector_ids
    quadratic_manifest.branch_weight_pairing_id
    physical effect_ids transferred to a newly defined apparatus_manifest.
```

The transfer has not occurred in v69. Under the selected successor
architecture, physical effect identifiers are not fields of the algebraic
`D_matter` contract. They, their instrument identifiers, apparatus carrier,
ready state, coupling, pointer, reduction, realized outcomes, post-state
instruments, occurrence law, and physical realization certificates are owned
solely by a newly named machine-readable `apparatus_manifest` under
`QDD-INSTRUMENT-APPARATUS [O] / STOP`.

`DEF-QDD-BRANCH-WEIGHT-PAIRING` remains the prospective pairing value. Any
legacy use of the word "Born" in its name or provenance is, on this scoped
algebraic writer, only a historical label for the exact branch-weight pairing.
It supplies no physical effect, occurrence law, or L6 meaning.

The public apparatus obligation remains open.

## 2. Choice, not determinedness

**This is an owner selection of the contract boundary for the present
architecture. It is not a theorem of mathematical determinedness.**

No result in Public Canon v69 proves that `J`, `U`, `Q_QDD`, the Gram form,
the 313-fibre census, `QDD-ALGEBRAIC-FACTORIZATION`, the projector theorem, or
the public dependency graph uniquely forces this ownership split. No route is
called canonical, and no zero-discrete-choice or uniqueness-from-`J` claim is
made.

The exact factorization

```text
D_QDD_direct = F_QDD o Q_QDD o beta_QDD
```

is a theorem-grade identity inside the already adopted algebraic definitions.
It does not select the owner of physical effects and does not turn this owner
choice into a theorem.

Likewise, any relative uniqueness of the ordered projector pair inside its
stated algebraic class is only uniqueness **within that selected class**. It
does not prove that the class, the `D_matter` boundary, or the separation from
apparatus is uniquely forced.

The counterroute `PHYSICAL-DMATTER`, in which a differently defined
`D_matter` contract would contain physically selected `effect_ids`, is named
but not adopted. Current public results do not falsify or exclude it. This
note also does not claim that a complete typed instance of that counterroute
has been constructed. The two routes are mutually exclusive definitions of
one active contract boundary, not contradictory mathematical propositions.
A later owner amendment could select a separately named physical route
without retroactively falsifying the algebraic equalities or proving that the
present choice had been forced.

This note has no public status. Any later registered dictionary based solely
on this choice has status ceiling `D`, never `T`. The existing algebraic `T`
rows retain their independent meanings.

## 3. Projector/effect type wall

The selected successor architecture assigns the following distinct roles:

```text
projector_id    exact algebraic L1 readout operator
effect_id       physically realized effect owned by an apparatus
instrument_id   physical post-state operation or instrument component
```

Consequently:

```text
projector_id  != effect_id
projector_id  != instrument_id
effect_id     != instrument_id
```

as typed identifiers. Entrywise equality of two rational matrices does not
alias their identifiers, types, owners, or evidentiary obligations.

The existing matrices denoted `E_low` and `E_high` remain the ordered
algebraic projectors `DEF-QDD-PROJECTOR-LOW/HIGH`. This note does not promote
them to physical effects. A later apparatus may target the same matrix values
only through a separately defined realization or target-comparison bridge.
Any selected physical certificate tying a chosen instrument component and
effect identifier to one of these target projectors must keep identity and
value comparison separate, for example:

```text
value(effect_id_a) = K_a^sharp K_a = value(projector_id_a)
realizes(effect_id_a, projector_id_a)
```

The exact target-comparison relation, its domain, and the complete physical
class remain unresolved under
`QDD-INSTRUMENT-APPARATUS`.

This preserves the substance of Ruling 2 in
`QDD-OWNER-RULINGS-2026-07-30.md`: algebraic projectors do not fill physical
`effect_ids`. The selected architecture changes the future ownership topology;
it does not evade the effect prohibition by renaming a physical object.

## 4. Required later normative transaction

This owner choice does not itself move `QUADRATIC-DECODER-DATA`. That row
remains `O / STOP` in Public Canon v69.

A later Public Canon may implement the choice only as one atomic content
transaction. At minimum it must change together:

1. `DEF-DECODER-MATTER`, with the exact scoped binding to
   `D_QDD_direct` and no extension beyond `K_QDD` or `D_quadratic`;
2. `DEF-DECODER-COMPLETION-CONTRACT`, removing the current unresolved physical
   `effect_ids` requirement from the selected algebraic route, transferring
   that duty to the physical apparatus owner, and applying both exact schema
   changes:

   ```text
   effect_ids       -> ordered projector_ids
   born_pairing_id  -> branch_weight_pairing_id
   ```
3. every active `READING-SPLIT` and QDD scope sentence that currently imports
   physical Born/effect semantics into the quadratic algebraic writer;
4. `QUADRATIC-DECODER-DATA`, restricted to the exact L1 algebraic record
   writer and explicitly excluding physical `effect_ids`, physical-effect
   semantics, apparatus, realized events, occurrence, sampling, randomness,
   post-state content, and L6 measure;
5. `QDD-INSTRUMENT-APPARATUS`, with a newly named machine-readable
   `apparatus_manifest` carrying at least `effect_ids`, `instrument_ids`,
   apparatus carrier, ready state, coupling, pointer, reduction, realization
   or target-comparison fields, realized-event semantics, occurrence law, and
   post-state duties; these fields begin `UNRESOLVED` and the apparatus owner
   remains `O / STOP`;
6. the dependency graph, removing physical `MEASURE-BORN-VERB` lineage from
   the algebraic QDD writer, adding `QDD-ALGEBRAIC-FACTORIZATION`, and changing
   projector-edge bases from physical "effect pair" language to an ordered
   algebraic projector pair;
7. the successor algebraic ledger item, typed `DICTIONARY / D / L1` only
   after complete conformance, with empty `gate_ids` and no L1-to-L1
   `bridge_manifest` row; for a same-identifier retype this is the explicit
   transition `OBLIGATION / O / MULTI -> DICTIONARY / D / L1`;
8. `FRONTIER_PROGRAMS.tsv`, removing the old QDD composite row only when it is
   retired or validly retyped, while the apparatus program remains `O / STOP`;
9. a successor manifest with a new format identifier; the hashed v47
   manifests and every older artifact remain unchanged;
10. history, technical `INLINE_CANON` evidence hashes, frontier surfaces,
   generated views, status-separation checks, and every current-status
   sentence.

The old physical `effect_ids` debt must be recorded as **transferred, not
satisfied**. Old hashed manifests, notes, probes, and result bundles remain
historical and are not silently migrated.

This note deliberately does not choose the later ledger identity operation.
The safest available form is to retire or supersede the old composite
`QUADRATIC-DECODER-DATA [O]` as split, without a fired falsifier and without
positive closure; declare a separately named algebraic QDD `D_matter`
dictionary with status ceiling `D`; and strengthen the already-open apparatus
row with every transferred physical duty.

If a later release instead retains the same `QUADRATIC-DECODER-DATA`
identifier, it must expose the governance retype separately from any status
change:

```text
SCOPE_CHANGE   O -> O
    owner-selected effects/projectors ownership split;
    post-result; not forced; alternative not falsified;
    old physical condition transferred, not met;
    not positive closure of the old composite obligation.

STATUS_CHANGE  O -> D
    only after a successor algebraic manifest, exact scoped binding,
    dependency graph, and all checkers conform to the owner-selected scope;
    governance retype, not scientific frontier closure.
```

The two events must not be collapsed. Review may require them to occur in
separate release steps. The first records **we chose the contract**. The
second, if independently authorized, may record only **the successor package
conforms to that chosen contract**. Neither may be reported as a theorem that
algebra determined the contract. If any atomic surface or conformance check
fails, no status event occurs and the old row remains `O / STOP`.

No new cross-layer gate is expected only if the successor scoped item is
normatively typed as an L1-to-L1 dictionary action. Otherwise it returns for
layer and gate adjudication. This says nothing about the still-open physical
lifts under the apparatus obligation.

## 5. Anti-inheritance firewall

This choice does not assert, imply, or discharge any of the following:

```text
K_QDD = K
dom(D_matter) = K
totality of D_matter outside the exact scoped leg
completion of the whole decoder
closure of D_linear, D_binary, D_geom, or D_clock
derivation of projectors or branch-weight pairing from J
physical effect selection or apparatus completeness
realized LOW/HIGH detector events
post-state instrument uniqueness
occurrence, frequency, sampling, randomness, or independence
an L6 measure
physical canonicity or uniqueness of the route
any CM, Psi, primary-carrier, seam, or writeback consequence
```

Common numeric values do not cross the type wall. Projector completeness does
not imply apparatus completeness. Algebraic normalization does not imply a
physical occurrence law. The factorization theorem does not imply route
selection.

## 6. Invalid owner transaction conditions

Any later purported adoption is invalid and must stop under one of these
conditions:

`PARTIAL-ADOPTION`
: Only `effect_ids` is renamed while physical Born wording, dependencies, or
  ownership remain in the algebraic writer.

`PHYSICAL-INPUT-LEAK`
: A `MatterData_QDD` field consumes apparatus, realized-event, occurrence, or
  physical-measure data.

`TYPE-ALIAS`
: One public identifier fills projector and physical-effect roles, or matrix
  equality is used as identifier equality.

`CHOICE-AS-THEOREM`
: The owner choice is assigned `T`, theorem-grade or scientific evidence,
  scientific credit, forcedness, canonicity, or uniqueness wording. A
  technical `INLINE_CANON / registry-scope-sha256-v1` entry for a later public
  dictionary is allowed and is not scientific evidence that the route was
  forced.

`ALTERNATIVE-ERASURE`
: Non-adoption of `PHYSICAL-DMATTER` is reported as its falsification or as a
  proof of its impossibility.

`DEBT-ERASURE`
: The old physical effect duty is described as satisfied instead of
  transferred to the still-open apparatus owner.

`STATUS-LEAK`
: This note alone is used to move a public status, gate, frontier, or claim.

## 7. Immediate disposition

After this owner note is reviewed, merged, and read back from public `main`:

```text
owner route guidance                 ALGEBRAIC-DMATTER, pinned only;
                                      no normative authority
mathematical determinedness          NOT CLAIMED
PHYSICAL-DMATTER counterroute        UNADOPTED / NOT FALSIFIED /
                                      NOT SHOWN COMPLETE
QUADRATIC-DECODER-DATA               O / STOP, unchanged
QDD-ALGEBRAIC-FACTORIZATION          T, unchanged
QDD-INSTRUMENT-APPARATUS             O / STOP, unchanged
formal executions authorized or
performed by this owner note          0
public Canon/table/status change      NONE
```

The owner-guidance next proposed action is a separately reviewed
successor-manifest and Public Canon content transaction. It may test
conformance to the chosen architecture. It may not redescribe this post-result
choice as mathematical determination.
