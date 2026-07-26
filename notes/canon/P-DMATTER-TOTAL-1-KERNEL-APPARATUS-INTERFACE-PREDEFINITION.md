# P-DMATTER-TOTAL-1 Kernel-Apparatus Interface Predefinition (NON-CANONICAL)

```text
STATUS:                 DRAFT / PREDEFINITION / CONDITIONAL BRANCH SURFACE
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / DEFINITION-ONLY
OWNER INPUT REQUIRED:   YES
PHYSICAL BRANCH ADOPTED: NONE
PUBLIC BASE:            Public Canon v23
PUBLIC CANON TAG:       canon-v23
ACTIVATION COMMIT:      4ac41b4fac3a3794a6e9d5be1e2027d324edb806
CONTENT COMMIT:         7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:            116017
PUBLIC MAIN BASE:       93f214d358ea50ea4ca8eb045fc9d4ec24542d5b
ROUTE A OWNER DECISION: 8ce44e09a3967f3c160ba5db632f8e36a9ee71fbb6d62c5d7aad16e1380b2cde
OD1-OD4 OWNER RULING:   0cb5d0e46d2a76d5170ac399b15626b558256984cf2d01c4029441ca0d248ca5
PROPOSAL-ID PACKAGE:    d9e10e605e937971ea56974fb1afaecf36bfc1ebad3e1ff7ed304914f208b266
INSTRUMENT PREDEFINITION:
                        1cfde364a3ad7f64730433ed142fd7cb04df6064779087f7144ffa6991918ee6
CLAIM ISSUE:            107
A11 STATUS:             PARTIAL / O-STOP, unchanged
QDD STATUS:             O / STOP, unchanged
FORMAL RUN:             NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
GATE CHANGE:            NONE
```

This note performs one schema-first action after the merged physical-
instrument predefinition. It freezes the fields and kill tests required of a
future kernel-apparatus submission. It also records an exact conditional
calculation showing why ordinary nondemolition does not select the Luders
instrument.

It does not adopt an apparatus carrier, a ready-state convention, a tensor
product as physical, a coupling law, a nondemolition principle, reduced
centrality, full joint central control, the full commutant, a physical effect,
a physical outcome, a layer, a gate, or feedback. The calculations below are
decision inputs, not physical outputs.

## 0. Falsification first

A submitted interface candidate is rejected if it does any of the following:

1. supplies `K_a` as an independent input instead of deriving it by the
   frozen coupling-to-pointer reduction;
2. uses a partial, multivalued, or equality-dependent reduction;
3. fails an exact certificate

   ```text
   E_a = K_a^sharp K_a,
   E_low + E_high = I_4,
   p_a(rho) = Tr(E_a rho);
   ```

4. uses a pointer event whose map to the fixed Route A labels `low` and
   `high` is partial, ambiguous, nonexhaustive, or changed after opening;
5. reads an unregistered kernel state, apparatus value, clock, random choice,
   measured value, history entry, network value, or later output;
6. infers a public ID, layer, gate, physical Born pairing, feedback channel,
   or terminality claim from an algebraic formula;
7. calls a candidate universe complete while omitting a typed object admitted
   by its own frozen predicate;
8. calls an amplitude-level isometry a full physical apparatus evolution
   without a separately exact extension, equality, and completeness proof;
9. reports physical `PASS`, `NONUNIQUE`, `EMPTY`, or Canon `F` from either
   conditional algebraic branch below;
10. moves A11 or `QUADRATIC-DECODER-DATA` from `O / STOP`.

The conditional predefinition is inconsistent if any of these statements is
false:

```text
AMPLITUDE-DILATION
    V_K^natural V_K = I_4 for every admitted algebraic instrument.

POINTER-REDUCTION
    the labeled pointer component of V_K is exactly K_a.

COMMUTANT-BRANCH
    both the Luders family and the exact P_12 family survive, and the
    operational quotient has cardinality aleph_0.

READY-CENTRAL-BRANCH
    every admitted reduced K_a is plus or minus E_a and all sign choices
    define one operational instrument class.
```

A failed displayed identity or conditional branch calculation returns
`PREDEFINITION-INCONSISTENT`. A submitted object that violates a type,
certificate, hidden-input, hidden-owner-choice, pointer, completeness, or
routing rule returns `CANDIDATE-REJECTED / STOP`. Neither output is Canon or
registry `F`.

After a classification opens, changing any carrier, equality, ready state,
joint composition, coupling class, preservation law, pointer event, label
map, reduction, admissibility predicate, candidate-universe equality,
completeness proof or method, physical identifier, Born pairing, dependency,
layer, gate, history or feedback rule, output meaning, or branch choice
returns `FIRE-POSTHOC`.

## 1. Fixed input boundary

The merged instrument predefinition supplies only the proposal-local
amplitude surface

```text
H_Q = (Q^4, <x,y>_G = x^T G y),

G       = I_4 - (1/5) 1 1^T,
G^(-1)  = I_4 + 1 1^T,
A^sharp = G^(-1) A^T G,

E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low,

Instr_alg(E_low,E_high)
  = { (K_low,K_high) in M_4(Q)^2 :
      K_a^sharp K_a = E_a for a in {low,high} }.
```

It also freezes `Eq_K_matrix`, operational `Eq_instrument`, `Eq_effect`,
the event operation, tagged zero-probability semantics, and outcome
forgetting. None of these objects is a public physical identifier.

The public kernel state remains

```text
Omega = N_0 x F_5^6
```

with the autonomous update `U`. The Route A map `beta` reads one anchored
pre-update record into the amplitude candidate. No public action of `U` on
`H_Q`, no post-event stream, and no kernel-to-apparatus bridge exists.
Therefore `H_Q` must not be renamed a kernel dynamical carrier.

The public QDD row expressly excludes post-state instrument uniqueness.
This note does not expand that row. Its interface fields prepare the separate
`QDD-PHYSICAL-EFFECT-SELECTION` boundary from the Route A owner decision.

## 2. Required kernel-apparatus interface schema

A later submitted candidate must publish a finite manifest with every field
below. The block names are proposal-local schema names, not public contract
extensions.

```text
kernel_source_manifest:
    kernel_source_id
    kernel_state_carrier_id
    kernel_state_equality_id
    kernel_totality_domain_id
    kernel_to_amplitude_bridge_id
    bridge_domain_id
    bridge_codomain_id
    bridge_equality_id

apparatus_manifest:
    apparatus_carrier_id
    apparatus_coefficient_object_id
    apparatus_membership_id
    apparatus_equality_id
    apparatus_pairing_id

ready_manifest:
    ready_state_carrier_id
    ready_state_id
    ready_state_value_id
    ready_state_equality_id
    ready_domain_id
    ready_to_pointer_relation_id

joint_manifest:
    joint_carrier_id
    joint_composition_id
    joint_equality_id
    system_embedding_id
    apparatus_embedding_id
    coupling_class_id
    coupling_map_id
    coupling_domain_id
    coupling_codomain_id
    coupling_totality_domain_id
    coupling_preservation_law_id

pointer_manifest:
    pointer_carrier_id
    pointer_equality_id
    pointer_map_id
    pointer_map_domain_id
    pointer_map_codomain_id
    pointer_map_totality_domain_id
    pointer_map_totality_certificate_id
    pointer_map_equality_compatibility_id
    pointer_event_ids
    pointer_event_equality_id
    physical_outcome_ids
    outcome_equality_id
    pointer_to_outcome_map_id
    pointer_to_outcome_domain_id
    pointer_to_outcome_codomain_id
    pointer_to_outcome_totality_certificate_id
    pointer_to_outcome_equality_compatibility_id
    outcome_to_route_label_map_id
    outcome_to_route_label_domain_id
    outcome_to_route_label_codomain_id
    outcome_to_route_label_totality_certificate_id
    outcome_to_route_label_equality_compatibility_id
    pointer_exhaustivity_certificate_id

reduction_manifest:
    reduction_map_id
    reduction_domain_id
    reduction_codomain_id
    reduction_equality_id
    derived_instrument_ids
    derived_effect_ids
    K_matrix_equality_id
    instrument_operation_equality_id
    effect_equality_id
    event_operation_id
    post_event_semantics_id
    outcome_coarse_graining_id
    reduction_to_K_certificate_ids
    effect_certificate_ids
    normalization_completeness_certificate_id
    born_pairing_id
    born_identity_certificate_id
    MatterData_outcome_field_ids
    MatterData_outcome_read_map_ids
    MatterData_outcome_write_map_ids

admissibility_manifest:
    apparatus_realization_id
    apparatus_realization_equality_id
    candidate_universe_id
    candidate_universe_equality_id
    physical_admissibility_predicate_id
    physical_admissibility_domain_id
    physical_admissibility_codomain_id
    physical_admissibility_totality_domain_id
    physical_admissibility_decision_procedure_id
    candidate_universe_membership_test_id
    instrument_classification_equality_id
    completeness_statement_id
    completeness_proof_id
    completeness_method_id

layer_assignment_manifest[]:
    object_id
    layer

gate_binding_manifest[]:
    map_id
    from_layer
    to_layer
    gate_id

sampling_manifest:
    state = DEFINED | NONE | UNRESOLVED

    DEFINED:
        sampling_mode_id
        sampling_rule_id
        sampling_map_id
        sampling_domain_id
        sampling_codomain_id
        sampling_totality_domain_id
        sampling_totality_certificate_id
        sampling_equality_compatibility_id
        sampling_input_source_id

    NONE:
        no_sampling_basis_id

history_update_manifest:
    state = DEFINED | NONE | UNRESOLVED

    DEFINED:
        history_carrier_id
        history_equality_id
        history_update_id
        history_update_domain_id
        history_update_codomain_id
        history_update_totality_domain_id
        history_update_totality_certificate_id
        history_update_equality_compatibility_id

    NONE:
        no_history_update_basis_id

writeback_manifest:
    state = DEFINED | NONE | UNRESOLVED

    DEFINED:
        feedback_mode_id
        feeds_U
        writeback_bridge_id
        writeback_map_id
        writeback_domain_id
        writeback_codomain_id
        writeback_totality_domain_id
        writeback_totality_certificate_id
        writeback_equality_compatibility_id
        writeback_gate_id
        write_source_id
        write_source_layer
        write_target_id
        write_target_layer
        autonomous_state_codomain_id

    NONE:
        feeds_U = FALSE
        no_writeback_basis_id

dependency_closure_manifest:
    dependency_item_ids
    dependency_graph_id
    acyclicity_certificate_id
    hidden_input_allowlist_id
    hidden_input_denylist_id

completion_contract_binding_manifest:
    quadratic_manifest_effect_ids_binding
    quadratic_manifest_born_pairing_binding
    record_field_manifest_outcome_row_ids
    closure_manifest_write_target_ids
    closure_manifest_terminal_output_ids
    closure_manifest_terminality_basis_id

output_manifest:
    predefinition_output_id
    candidate_rejection_output_id
    classification_output_id
    candidate_relation_id
    fire_posthoc_id.
```

Every identifier-valued field contains a resolvable public identifier or the
literal `UNRESOLVED`. `NOT_APPLICABLE` is forbidden. There is no bare null.

Each tagged manifest selects exactly one variant. `DEFINED` requires every
field displayed under that variant. `NONE` requires its exact resolvable
absence-basis ID and forbids invented dummy maps. `UNRESOLVED` supplies no
substitute value and routes `STOP`. Mixing fields from two variants is a
schema error. In a defined writeback variant, `feeds_U` is exactly `TRUE` or
`FALSE`; in the `NONE` variant it is exactly `FALSE`; in the `UNRESOLVED`
variant its effective state is `UNRESOLVED`.

At the current single-operator Route A scope, the pointer-to-label boundary
must publish exactly two nonempty, disjoint, exhaustive physical outcome IDs
and a total bijection

```text
physical outcome IDs  ->  {low,high}.
```

The physical outcome IDs are not the strings `low` and `high`. Those strings
are algebraic sector labels already fixed by the effects. A micro-outcome or
multi-Kraus extension is outside this single-operator schema and requires a
new owner ruling before it can be classified.

Proposal-local schema names:

```text
CAND-QDD-KERNEL-APPARATUS-INTERFACE-SCHEMA
CAND-QDD-APPARATUS-REALIZATION-SCHEMA
CAND-QDD-EQ-APPARATUS-REALIZATION-SCHEMA
CAND-QDD-COUPLING-TO-K-REDUCTION-SCHEMA
CAND-QDD-POINTER-TO-ROUTE-LABEL-SCHEMA
CAND-QDD-PHYSICAL-ADMISSIBILITY-SCHEMA
CAND-QDD-APPARATUS-COMPLETENESS-OBLIGATION
CAND-QDD-HISTORY-FEEDBACK-SCHEMA
CAND-QDD-APPARATUS-DEPENDENCY-CLOSURE-SCHEMA
CAND-QDD-APPARATUS-COMPLETION-BINDING-SCHEMA.
```

They identify definitions in this note only. They fill no public manifest
slot.

## 3. Coupling-to-instrument reduction and contract binding

The future reduction is a deterministic typed function. Schematically,

```text
Reduce_a :
    KernelSource
    x ApparatusReady
    x AdmissibleCoupling
    x PointerEvent_a
    -> End_Q(H_Q),

Reduce_a(source,ready,coupling,event_a) = K_a.
```

The tuple on the left is the input. `K_a` is the output. A candidate that
lists an independently chosen `K_a` and merely checks it afterward violates
the coupling-first rule.

The reduction must prove, in exact arithmetic and on its complete named
domain,

```text
K_a in End_Q(H_Q),
K_a^sharp K_a = E_a,
sum_a K_a^sharp K_a = I_4,
p_a(rho) = Tr(K_a rho K_a^sharp) = Tr(E_a rho).
```

The apparatus-realization equality, `Eq_K_matrix`, `Eq_instrument`, and
`Eq_effect` are four distinct relations. Two apparatus realizations may
differ while reducing to the same operational instrument class. Equality of
effects does not make two reduced event maps equal.

The future completeness proof must quantify over the exact apparatus and
coupling predicate, not over a hand-selected list of `K_a` matrices. The
complete dependency graph must include every source read by the kernel
bridge, coupling, pointer, reduction, record write, sampling, history, and
feedback maps, and the hidden-input allowlist must close transitively.

The completion-contract bindings are literal obligations:

```text
derived physical effect IDs
    -> quadratic_manifest.effect_ids

derived physical Born pairing ID
    -> quadratic_manifest.born_pairing_id

MatterData outcome field and map IDs
    -> record_field_manifest outcome rows

write target, terminal output, and terminality basis IDs
    -> closure_manifest.
```

None of these bindings may be filled by a proposal-local `CAND-*` name.

## 4. Conditional amplitude dilation

This section defines a mathematical witness only. It does not fill the
apparatus schema.

Let

```text
A_out = Q^2,
f_low  = (1,0)^T,
f_high = (0,1)^T,
F_a    = f_a f_a^T.
```

For every `(K_low,K_high)` in `Instr_alg`, define

```text
V_K : H_Q -> H_Q tensor_Q A_out,

V_K x
  = K_low x tensor f_low
  + K_high x tensor f_high.
```

The codomain pairing is `G tensor I_2`. With `natural` denoting the adjoint
between the two paired spaces,

```text
V_K^natural V_K
  = K_low^sharp K_low + K_high^sharp K_high
  = E_low + E_high
  = I_4.
```

Thus `V_K` is an exact rational isometry. The pointer component maps

```text
R_a = I_4 tensor f_a^T
```

obey

```text
R_a V_K = K_a.
```

Conversely, decomposing any labeled `V` into its two pointer components
recovers `(K_low,K_high)`, and `V^natural V=I_4` is exactly the completeness
equation for those components.

Therefore the existence of this amplitude dilation does not narrow
`Instr_alg` at all. It is a repackaging of the instrument family, not a
physical selection principle.

Proposal-local candidate names:

```text
CAND-QDD-AMPLITUDE-POINTER-Q2
CAND-QDD-AMPLITUDE-DILATION-VK
CAND-QDD-POINTER-COMPONENT-REDUCTION
CAND-QDD-AMPLITUDE-ISOMETRY-CERTIFICATE.
```

The choice `A_out=Q^2` is not adopted as the physical apparatus carrier. It
only supplies the smallest output-label carrier for the conditional
calculation.

## 5. Exact reversible QND counterexample

This section adds a ready state only to construct two exact counterposed
candidates. The convention is not adopted physically.

Freeze the proposal-local conditional proposition

```text
Q2-WEAK-QND-LUDERS-SUFFICIENCY:
    On H_Q tensor Q^2 with eta=f_low, G_tot=G tensor I_2, the fixed pointer
    projectors F_low,F_high, rational G_tot-unitarity, natural
    self-adjointness, involutivity, exact pointer correlation, and both
    ready-domain QND intertwining laws, every coupling reduces to the
    operational Luders class.
```

Let

```text
A_Q    = Q^2,
eta    = f_low,
X      = [0 1
          1 0],
G_tot  = G tensor I_2,
J_eta(x) = x tensor eta,
Pi_a   = I_4 tensor F_a.
```

For an endomorphism `Z` of `H_Q tensor A_Q`, define

```text
Z^natural = G_tot^(-1) Z^T G_tot.
```

The central candidate

```text
U_L = E_low tensor I_2 + E_high tensor X
```

satisfies exactly

```text
U_L^natural = U_L,
U_L^2 = I_8,
U_L^natural U_L = I_8,

U_L J_eta(x)
  = E_low x tensor f_low
  + E_high x tensor f_high.
```

Its pointer reduction gives

```text
K_low  = E_low,
K_high = E_high.
```

Let `P_12` exchange the first two system coordinates. The merged instrument
predefinition proves

```text
P_12^sharp P_12 = I_4,
P_12 E_a = E_a P_12.
```

The noncentral candidate

```text
U_P
  = E_low tensor I_2
  + (P_12 E_high) tensor X
```

also satisfies exactly

```text
U_P^natural = U_P,
U_P^2 = I_8,
U_P^natural U_P = I_8.
```

Both candidates obey the same ready-domain laws

```text
Pi_a U J_eta = U J_eta E_a,
(E_a tensor I_2) U J_eta = U J_eta E_a.
```

They use the same rational coefficient field, apparatus dimension, ready
state, pointer projectors, reversible law, involution law, perfect pointer
correlation, branch repeatability, and effects. Their reduced high event maps
are operationally different.

Therefore `U_P` is an exact proposal-local counterexample to
`Q2-WEAK-QND-LUDERS-SUFFICIENCY`. This is not registry or Canon `F`, and it
does not classify a physical apparatus universe.

Proposal-local candidate names:

```text
CAND-QDD-Q2-WEAK-QND-LUDERS-SUFFICIENCY
CAND-QDD-Q2-COUPLING-LUDERS
CAND-QDD-Q2-COUPLING-P12
CAND-QDD-Q2-QND-TIE-WITNESS.
```

Neither coupling is a physical apparatus selection.

## 6. Conditional branch classification

Let

```text
C = Comm(E_low,E_high)
  = {T in M_4(Q) : T E_a = E_a T for a in {low,high}}.
```

Since `E_low` and `E_high` are complementary rank-one and rank-three
projectors,

```text
C = E_low M_4(Q) E_low direct-sum E_high M_4(Q) E_high
  isomorphic to M_1(Q) direct-sum M_3(Q),

Z(C)
  = Q E_low direct-sum Q E_high
  = Alg_Q(E_low,E_high).
```

### 6.1 Full-commutant reduced candidate

Define the conditional algebraic branch

```text
Adm_comm
  = { (K_low,K_high) in Instr_alg :
      K_a in C for each label a }.
```

Every member has

```text
K_low  = V_low E_low,
K_high = V_high E_high,

V_low  in O(im(E_low),G),
V_high in O(im(E_high),G).
```

Signs from the one-dimensional low factor disappear under `Eq_instrument`.
The operational quotient retains the projective rational orthogonal group of
the three-dimensional high sector.

The quotient has exactly cardinality `aleph_0`. It is at most countable
because every matrix entry is rational. It is infinite by the following
exact family. For integer `t >= 2`, let

```text
u_t = (1,-1,t,-t)^T,

R_t = I_4 - 2 u_t u_t^T / (u_t^T u_t)
    = I_4 - u_t u_t^T / (1+t^2).
```

Then

```text
1^T u_t = 0,
R_t^T = R_t,
R_t^2 = I_4,
R_t 1 = 1,
R_t^sharp R_t = I_4,
R_t E_a = E_a R_t.
```

The instruments

```text
K_low^(t)  = E_low,
K_high^(t) = R_t E_high
```

all lie in `Adm_comm`. Their high event maps are pairwise operationally
inequivalent. Equality of two single-operator event maps on all rational
rank-one states forces the two nonzero operators to differ by a global
rational sign. The reflections `R_t` are pairwise distinct, and their
high-sector trace is `1`, so no `R_t` is the negative of another on the
three-dimensional high sector.

Every displayed member has a full reversible involutive candidate dilation

```text
U_t
  = E_low tensor I_2
  + (R_t E_high) tensor X.
```

Thus the conditional exact output is

```text
COMMUTANT-ALEPH0-ALGEBRAIC.
```

It is not physical `NONUNIQUE(aleph_0)` because `Adm_comm` is not adopted as
the physical universe and no kernel-to-apparatus completeness proof exists.

### 6.2 Ready-reduced centrality candidate

Define the stronger conditional reduced branch

```text
Adm_ready_center
  = { (K_low,K_high) in Instr_alg :
      K_a in Z(C) for each label a }.
```

Write

```text
K_a = alpha_a E_low + beta_a E_high.
```

The exact equations `K_a^sharp K_a=E_a` force

```text
K_low  = epsilon_low E_low,
K_high = epsilon_high E_high,
epsilon_low, epsilon_high in {+1,-1}.
```

All four sign pairs define the same operational event maps. Therefore the
conditional exact output is

```text
READY-CENTRAL-ALGEBRAIC-SINGLETON / LUDERS-MATCH.
```

It is not physical `PASS`. The reduced condition is the new principle

```text
READY-REDUCED-NO-INTRASECTOR-BACKACTION:
    every ready-state pointer reduction K_a lies in Z(C).
```

This condition constrains only the reduced ready-domain event maps. It does
not imply that the full joint coupling is central on apparatus states
orthogonal to the ready state. A full-joint central-control condition would
be a separate, strictly stronger owner input with its own coupling-level
definition and falsifier.

Ready-reduced centrality is not implied by minimum apparatus dimension,
rationality, reversibility, involutivity, pointer correlation, repeatability,
projector conservation, the two weak-QND laws, or Public Canon v23.

Its exact falsifier is:

```text
an admitted physical coupling reduces to some K_a in C but not in Z(C).
```

`P_12 E_high` is an exact algebraic witness that such a reduction is
possible. It is not yet a derived physical counterexample.

Proposal-local branch names:

```text
CAND-QDD-ADM-COMMUTANT
CAND-QDD-ADM-READY-REDUCED-CENTRALITY
CAND-QDD-FALSIFIER-NONCENTRAL-REDUCTION.
```

No branch is adopted by this note.

## 7. Irreducible owner decisions and writeback routing

Before a physical apparatus universe can be frozen, an owner ruling must
choose or reject each independent axis:

```text
APPARATUS READY SEMANTICS
    READY-IN-ONE-OUTCOME
    NEUTRAL-READY-DISTINCT-FROM-OUTCOMES
    NEITHER / REDEFINE

COUPLING TYPE
    READY-DOMAIN ISOMETRY
    FULL REVERSIBLE JOINT EVOLUTION
    IRREVERSIBLE TYPED COUPLING
    NEITHER / REDEFINE

SYSTEM-SIDE ADMISSIBILITY
    FULL-COMMUTANT READY REDUCTION
    READY-REDUCED CENTRALITY
    FULL-JOINT CENTRAL CONTROL, after a separate exact definition
    KERNEL-DERIVED DIFFERENT PREDICATE
    NEITHER / REDEFINE

PHYSICAL SOURCE
    exact kernel source and domain
    exact bridge into the amplitude carrier
    source and target layers
    one gate row for every cross-layer map

HISTORY AND FEEDBACK
    no sampling
    sampled terminal history only
    typed writeback
    NEITHER / REDEFINE.
```

The writeback routing is frozen:

```text
feeds_U = TRUE
    A nontrivial L5-output to L1 autonomous-state channel must name
    GATE-L5-L1-OBSERVER-WRITEBACK and fires OBSERVER-WRITE-PORT.

    A write channel with any other endpoint pair requires its own separately
    named gate and owner. It may not reuse the L5-to-L1 gate.

feeds_U = FALSE
    No writeback into U is declared at this interface. This does not prove
    completion-wide terminality, and another typed target must still name
    its own owner and gate when a write channel exists.

feeds_U = UNRESOLVED
    STOP.
```

Every defined sampling candidate must record its rule, map, domain, codomain,
totality domain and certificate, equality compatibility, and exact input or
randomness source. Every defined history update must record its carrier,
equality, update map, domain, codomain, totality domain and certificate, and
equality compatibility. Every defined writeback must record the bridge and
map, source and target carriers and layers, autonomous-state codomain, exact
write target, domain, codomain, totality domain and certificate, equality
compatibility, gate, and dependency closure.

Every owner choice must occur before classification. Choosing reduced
centrality after seeing `COMMUTANT-ALEPH0-ALGEBRAIC` is post-result selection
unless it is independently owner-adopted first.

## 8. Frozen output semantics

```text
PREDEFINITION-CONSISTENT
    The interface schema is exhaustive at its declared scope and all
    conditional algebraic calculations pass. This is not physical PASS.

PREDEFINITION-INCONSISTENT
    A displayed conditional identity or branch classification is false.
    This is not Canon or registry F.

CANDIDATE-REJECTED
    A submitted candidate violates a frozen type, certificate, hidden-input,
    hidden-owner-choice, pointer, completeness, dependency, or routing rule.
    The physical classification does not open and the result remains STOP.

OWNER-INPUT-REQUIRED
    At least one apparatus, coupling, admissibility, source, layer, gate,
    history, or feedback axis remains unchosen. This is the current output.

READY-FOR-CLASSIFICATION
    Every schema field has a legal frozen value, the physical candidate
    universe and its equality are exact, and a completeness proof and method
    are pinned. This still is not PASS.

PASS
    After READY-FOR-CLASSIFICATION, exactly one Eq_instrument class survives,
    with mandatory LUDERS-MATCH or LUDERS-MISMATCH.

NONUNIQUE(k)
    After READY-FOR-CLASSIFICATION, exactly k finite or infinite
    Eq_instrument classes survive, with exact cardinal k >= 2.

EMPTY
    After READY-FOR-CLASSIFICATION, no physical instrument survives.

STOP
    Any required schema value, type, equality, map, certificate, public ID,
    physical predicate, completeness proof, dependency closure, layer, gate,
    or history and feedback rule is missing or inexact.

FIRE-POSTHOC
    Any frozen input or output meaning changes after classification opens.
```

The current physical output is

```text
OWNER-INPUT-REQUIRED / STOP.
```

## 9. Exact status consequence

```text
kernel-apparatus schema                   DEFINED, proposal-local
coupling-to-K direction                   DEFINED, schema-level
completion-contract bindings              DEFINED, schema-level
dependency and hidden-input closure       DEFINED, schema-level
amplitude dilation V_K                    DEFINED, conditional algebra
Luders reversible dilation                DEFINED, conditional candidate
P_12 reversible dilation                  DEFINED, conditional control
Q2-WEAK-QND-LUDERS-SUFFICIENCY            EXACT COUNTEREXAMPLE,
                                          proposal-local conditional algebra;
                                          not registry or Canon F
full-commutant reduced quotient            aleph_0, conditional algebra
ready-reduced central quotient             one Luders class,
                                          conditional algebra

physical apparatus carrier                UNRESOLVED
physical ready state                       UNRESOLVED
kernel-to-apparatus coupling               UNRESOLVED
physical pointer and outcome IDs           UNRESOLVED
physical admissibility predicate           UNRESOLVED
physical completeness proof                UNRESOLVED
physical instrument/effect/Born IDs        UNRESOLVED
layers and public gate                     UNRESOLVED
history and feedback                       UNRESOLVED

A11                                        PARTIAL / O-STOP
QDD-PHYSICAL-EFFECT-SELECTION              O / STOP
QUADRATIC-DECODER-DATA                     O / STOP, unchanged.
```

No formal scientific run, physical branch adoption, or normative fold is
authorized by this predefinition.
