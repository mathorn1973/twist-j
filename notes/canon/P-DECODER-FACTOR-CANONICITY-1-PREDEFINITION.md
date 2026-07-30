# P-DECODER-FACTOR-CANONICITY-1 predefinition (NON-CANONICAL)

```text
STATUS:                 DRAFT / DEFINITION-ONLY / STOP-PREDEFINITION
AUTHORITY:              NOT CANON
PUBLIC BASE:            Public Canon v23
PUBLIC CANON TAG:       canon-v23
CONTENT COMMIT:         7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:            116017
POSSIBLE TARGET:        Public Canon v24, definition-only disposition
PUBLIC CLAIM CREATED:   NONE
PUBLIC STATUS CHANGE:   NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
GATE CHANGE:            NONE
FORMAL PROBE:           NONE
FORMAL RUN:             NONE
```

This note defines a result-independent audit surface for a future claim that
a decoder reading is canonical only as a factor or equivalence class. It does
not assert that any such factor exists, is unique, is physically admissible,
is maximal, is stable under scale change, or carries a closed macrodynamics.
It authorizes no verifier, probe, run, registry row, or Canon status.

The target principle is deliberately narrower than a decoder-universality
hypothesis:

> A decoder factor is canonical at a declared scope only after its typed
> domain, admissible candidate class, invisible transformations, covariant
> transports, output equality, nonconstancy test, and completeness proof
> have been frozen independently of the classification result.

The existence of a set-theoretic quotient is not scientific content by
itself. The scientific content would lie in the independently justified
input surface, the nontriviality of the surviving factor, and a complete
classification.

## 0. Falsification and STOP first

This predefinition is inconsistent if it permits any of the following:

1. choosing a gauge, scale map, apparatus reduction, candidate class, or
   output equality because it produces a desired value;
2. treating scale covariance as strict invariance without exact
   identification of source and target domains, decoder components, output
   carriers, and identity output transport;
3. treating equality of effects as equality of instruments or post-event
   operations;
4. calling the project's required factor nontrivial without an exact
   nonconstancy witness;
5. calling a factor a maximal invariant without a complete independently
   frozen invariant class and a universal factorization proof;
6. asserting totality without naming the exact totality domain;
7. transferring a factorization, invariance law, status, evidence, or closure
   between reading legs or decoder stages;
8. deriving exact macrodynamics from gauge invariance, scale covariance, or
   apparatus reduction coherence without a separate `U`-congruence proof;
9. inferring a layer, cross-layer gate, normalization, physical measure,
   instrument, writeback channel, or terminality result from a commuting
   diagram;
10. repairing a fired or nonunique predecessor by enlarging an equivalence
    after classification;
11. using this schema either to undo or to import into Canon issue #107's
    owner-adopted Route A / `c_0` definition-only proposal, or to adopt
    `Adm_GalSplit`, `D_direct`, an apparatus source, or a physical
    admissibility predicate.

A submitted instance routes `STOP` while any applicable carrier, domain,
totality domain, equality, map, output transport, candidate class,
nonconstancy test, completeness statement, completeness proof, layer, gate,
dependency, or output meaning is missing or inexact. If an action, category,
or indexed family is claimed, its applicable identity, composition, closure,
and compatibility laws are also mandatory.

An exact counterexample to a frozen future scientific predicate may support
that predicate's registered negative route. Missing definitions, a broken
schema, or a post-result input change are not Canon `F`.

## 1. Public boundary inherited from v23

Public Canon v23 defines a typed partial decoder:

```text
D_matter : dom(D_matter) subset K -> MatterData
D_geom   : dom(D_geom) subset K x MatterData -> GeometryData
D_clock  : dom(D_clock) subset K x MatterData x GeometryData
           -> ObservableHistory.
```

The stages

```text
D_matter, D_geom, D_clock
```

and the reading legs

```text
D_linear, D_binary, D_quadratic
```

are independent axes. `DEF-DECODER-COMPLETION-CONTRACT` is a schema only.
It proves no existence, totality, factorization, canonicity, completeness,
physical measure, instrument, or terminality statement.

This predefinition is an optional overlay on that contract. It does not
replace any existing manifest and does not fill any existing
`UNRESOLVED` field.

## 2. One typed factor-canonicity datum

For one fixed `stage_id`, one fixed `leg_id`, and one declared scope, freeze
before classification a datum

```text
C_factor = (
    source_carriers,
    output_carriers,
    declared_domains,
    source_equalities,
    output_equalities,
    candidate_class,
    candidate_equivalence,
    factor_maps,
    gauge_comparisons,
    scale_comparisons,
    apparatus_reductions,
    optional_categorical_coherence,
    optional_U_congruence,
    nonconstancy_test,
    completeness_statement,
    completeness_method
).
```

Every object and map is typed. A candidate at scale `ell` has the form

```text
D_ell : Dom_ell -> Y_ell,
Dom_ell subset X_ell.
```

`D_ell` is total only relative to the named set `Dom_ell`. Totality on
`Dom_ell` implies neither totality on `X_ell` nor completion-wide decoder
totality. Every equation below is required only on the intersection of its
declared exact domains.

A factor candidate has the typed shape

```text
q       : Dom -> QCarrier,
im(q)   subset QCarrier,
q_bar   : Dom -> im(q),       q_bar(x) = q(x),
i_q     : im(q) -> QCarrier,  the image inclusion,
q       = i_q o q_bar,
F       : im(q) -> Y,
D       : Dom -> Y,

factor equation:
D = F o q_bar  on Dom.
```

Here `q_bar` is the corestriction of `q` and is surjective by definition.
With the two equalities frozen, fiber constancy is exactly the equivalence

```text
[for all x,x' in Dom, q(x) = q(x') implies D(x) = D(x')]

if and only if

[there exists a unique F : im(q) -> Y with D = F o q_bar].
```

The reverse direction uses the factor equation. The forward direction
defines `F(q_bar(x)) := D(x)`; fiber constancy gives well-definedness and
surjectivity of `q_bar` gives uniqueness. The equality on `QCarrier` and the
equality on `Y` are separate frozen inputs.

The surviving factor must be nonconstant on its declared domain. A valid
certificate names exact witnesses

```text
x_0, x_1 in Dom,
D(x_0) != D(x_1),
```

or an equivalent exact image-cardinality proof with `|im(D)| >= 2`.
Syntactic dependence on an input field is not a nonconstancy certificate.

## 3. Four different per-map coherence tests

The base schema freezes individual typed commuting squares. It does not by
itself assert a monoid action, group action, source category, output functor,
or natural transformation. For each admitted map it freezes

```text
r     : Dom_s -> Dom_t,
D_s   : Dom_s -> Y_s,
D_t   : Dom_t -> Y_t,
T_r   : Y_s -> Y_t,

D_t o r = T_r o D_s.
```

Strict invariance is the special case only when all of

```text
Dom_s = Dom_t = Dom,
D_s = D_t = D,
Y_s = Y_t = Y,
T_r = id_Y
```

are identified at the declared scope. Equality of only the source or output
carrier is insufficient. The following per-map tests are independent. No
test is inherited from another merely because the same candidate appears in
both.

A stronger categorical reading is optional. It may be claimed only after a
separate manifest freezes objects, arrow membership, identity arrows,
composition, closure, associativity, left and right unit laws, source-map
identity and composition laws, output-transport identity and composition
laws, and the decoder-family commuting square for every admitted arrow. A
monoid-action claim additionally freezes the action identity and composition
laws. A group-action claim additionally freezes inverse assignment, inverse
closure, and both inverse laws.

### 3.1 Gauge invariance

An admitted gauge comparison is a frozen per-map square

```text
g       : Dom_s -> Dom_t,
Gamma_g : Y_s -> Y_t,

D_t o g = Gamma_g o D_s.
```

It is strict gauge invariance only under the full identifications above,
including

```text
Gamma_g = id_Y,
D o g = D.
```

The admitted-map class, its membership test, and any completeness proof must
be independent of decoder outputs. Calling that class a monoid action
additionally requires frozen identity, composition, closure, and action laws.
Calling it a group action additionally requires frozen inverse assignment,
inverse closure, and left and right inverse laws.

A comparison action, change of reading orientation, or dynamical
precomposition is not gauge merely because it connects two candidates.

### 3.2 Scale covariance

A scale comparison is one typed per-map square between possibly different
carriers:

```text
R_(b,ell) : Dom_ell -> Dom_(b ell),
Z_(b,ell) : Y_ell -> Y_(b ell).
```

Scale covariance means

```text
D_(b ell) o R_(b,ell) = Z_(b,ell) o D_ell.
```

The source map `R_(b,ell)` and output transport `Z_(b,ell)` are both frozen
before classification. Scale covariance becomes strict invariance only in a
separately declared fixed-point scope with

```text
Dom_(b ell) = Dom_ell,
D_(b ell) = D_ell,
Y_(b ell) = Y_ell,
Z_(b,ell) = identity.
```

A forward substitution, an information-losing block map, and an inverse
desubstitution are different typed operations. One may not be renamed as
another. Blocking origin, window convention, phase policy, normalization,
and pre-update versus post-update reading remain explicit inputs.

### 3.3 Apparatus reduction coherence

Let `P` and `P'` be typed apparatus or protocol objects and let an admitted
reduction carry exact transports

```text
r_X   : Dom_P -> Dom_(P'),
tau_r : Y_P -> Y_(P').
```

The per-reduction commuting square is

```text
D_(P') o r_X = tau_r o D_P.
```

Admission of `r` requires its exact precondition, source and target
equalities, transport laws, and pointwise intertwining certificate. A
generated reduction equivalence may be used only after the admitted-arrow
class and its finite-zig-zag completeness have been proved.

Forgetting an outcome is an operation on event maps. It is not automatically
the same as replacing the effects by their sum. Equality of Born weights or
effects does not identify distinct post-event operations.

### 3.4 Optional `U`-congruence

This clause is optional and separately typed. Let `Dom_U subset Dom` be a
named domain and freeze the restrictions and corestriction

```text
U_U     := U|Dom_U : Dom_U -> Dom_U,
D_U     := D|Dom_U : Dom_U -> Y,
Y_U     := D(Dom_U) subset Y,
D_bar_U : Dom_U -> Y_U,       D_bar_U(x) = D_U(x),
i_U     : Y_U -> Y,           the image inclusion,
D_U     = i_U o D_bar_U.
```

The requirement `U(Dom_U) subset Dom_U` is part of the typing of `U_U`.
Define

```text
x ~_D x'  iff  D_U(x) = D_U(x').
```

The kernel relation of `D_U` is a `U_U`-congruence exactly when

```text
D_U(x) = D_U(x')  implies  D_U(U_U x) = D_U(U_U x')
```

for every `x,x'` in `Dom_U`. Only then is

```text
U_bar : Y_U -> Y_U,
U_bar(D_bar_U(x)) := D_bar_U(U_U x)
```

well defined, and only then does the typed corestricted square

```text
D_bar_U o U_U = U_bar o D_bar_U
```

hold on `Dom_U`. The unqualified expression `U_bar o D` is not used because
its domain need not be all of `Y` or all of `Dom`.

`U`-congruence asserts no attractor, feedback, purpose, write channel, or
terminality result. In particular, it neither fires nor closes
`OBSERVER-WRITE-PORT`.

## 4. Candidate equivalence and classification

Two candidates are equivalent only under a frozen typed output isomorphism

```text
h : Y_1 -> Y_2
```

that preserves every owned record field, equality, normalization, effect,
outcome label, orientation datum, and declared transport, and obeys

```text
h o D_1 = D_2
```

on the common declared domain. A bijection invented after seeing the output
does not define an admissible equivalence.

Before candidate-equivalence classes may be counted, the admitted
isomorphism relation must be proved to be an equivalence relation on the
complete candidate class. The frozen certificate includes

```text
reflexivity:   every candidate has an admitted identity isomorphism;
symmetry:      every admitted h has an admitted inverse h^(-1);
transitivity: admitted h_12 and h_23 have admitted composite h_23 o h_12;
closure:       identities, inverses, and composites remain in the admitted
               isomorphism class and preserve every owned field.
```

Without these laws there is only a comparison graph, not a quotient into
candidate-equivalence classes.

A future complete classification has the following disjoint scientific
outcomes:

```text
UNIQUE
    exactly one candidate-equivalence class survives and it is nonconstant;

NONUNIQUE(kappa)
    exactly kappa inequivalent candidate-equivalence classes survive, for an
    arbitrary cardinal kappa >= 2, and at least one survivor is nonconstant;

EMPTY
    no candidate survives;

CONSTANT-ONLY
    at least one candidate survives and every survivor is constant.
```

`UNIQUE`, an exact `NONUNIQUE(kappa)`, `EMPTY`, and `CONSTANT-ONLY` each
assert exhaustion and therefore require a complete classification. Two
exhibited exact inequivalent survivors immediately falsify uniqueness,
without any completeness claim, but do not determine the exact cardinal
`kappa`.

The separate process routes are:

```text
STOP
    the input surface or completeness proof is incomplete or inexact;

FIRE-POSTHOC
    a frozen input or output meaning changes after classification opens.
```

These are definition-level outcome and route names. They are not public
statuses and this note reaches none of them except `STOP`.

## 5. Maximal invariant is a completeness theorem, not a definition shortcut

For one frozen scope with one common source domain, let
`Inv_adm(C_factor)` be an independently defined complete class of admissible
readouts that are strictly invariant under the independently frozen
invisible-transformation class. Its readouts are typed as

```text
D       : Dom -> Y_D,
D_bar   : Dom -> im(D),       D_bar(x) = D(x),
i_D     : im(D) -> Y_D,
D       = i_D o D_bar,
A       : Dom -> Y_A.
```

A candidate `D` may be called a maximal invariant only if all of the
following are proved:

1. `D` belongs to `Inv_adm(C_factor)` and is strictly invariant under every
   declared invisible transformation at that scope;
2. every `A` in `Inv_adm(C_factor)` has the same declared source `Dom` as
   `D`, and there exists a unique typed mediator

   ```text
   A_bar : im(D) -> Y_A
   ```

   with

   ```text
   A = A_bar o D_bar;
   ```

3. the invisible-transformation class, invariant class, candidate class, and
   candidate equivalence are each complete at the declared scope;
4. all dependencies and hidden inputs are closed.

A non-strict gauge comparison, scale-covariant square, or apparatus
reduction square may be an additional coherence obligation, but it does not
discharge strict invariance under an invisible transformation. A universal
factorization theorem for a merely covariant family is a maximal covariant
readout theorem, not a maximal-invariant theorem.

For an indexed family, the statement must be componentwise typed. For every
index `i` it freezes

```text
D_i       : Dom_i -> Y_i,
D_bar_i   : Dom_i -> im(D_i),
A_i       : Dom_i -> Z_i,
A_bar_i   : im(D_i) -> Z_i,
A_i       = A_bar_i o D_bar_i.
```

For every frozen source map `r : Dom_i -> Dom_j`, it also freezes decoder and
readout transports satisfying

```text
D_j o r = T_D(r) o D_i,
A_j o r = T_A(r) o A_i.
```

The first square induces the corestricted map

```text
T_D_bar(r) : im(D_i) -> im(D_j).
```

The component mediators are compatible only when

```text
T_A(r) o A_bar_i = A_bar_j o T_D_bar(r)
```

for every admitted `r`. Componentwise factorization without these frozen
compatibility equations is not indexed maximality.

Nonconstancy is separate from this universal property. A `nontrivial maximal
invariant` is a maximal invariant together with an exact certificate

```text
x_0, x_1 in Dom,
D(x_0) != D(x_1),
```

or an equivalent proof that `|im(D)| >= 2`. The project scientific criterion
requires a nontrivial maximal invariant; the term `maximal invariant` alone
does not encode nonconstancy.

Constructing a coequalizer of a fully declared action, or of a declared
family of parallel maps, proves only a universal property relative to that
declared surface. It does not prove that the surface is physically complete,
that the quotient is nonconstant, that it has a local or measurable
realization, or that one stable decoder class survives.

The terms `nontrivial maximal invariant`, `universal quotient`,
`universality class`, and `canonical factor` remain forbidden outputs while
any applicable maximality, compatibility, completeness, or nontriviality
item above is unresolved.

## 6. Proposed completion-contract overlay

A later definition fold may add an optional block with the following shape:

```text
factor_canonicity_manifest:
  owner_item_id
  stage_id
  leg_id
  source_carrier_id
  output_carrier_id
  domain_id
  totality_domain_id
  source_equality_id
  output_equality_id
  qcarrier_id
  q_equality_id
  q_map_id
  q_image_id
  q_corestriction_id
  q_image_inclusion_id
  factor_map_id
  factor_equation_id
  fiber_constancy_test_id
  fiber_factor_equivalence_statement_id
  fiber_factor_equivalence_proof_id
  nonconstancy_test_id
  candidate_class_id
  candidate_membership_test_id
  candidate_equivalence_id
  candidate_equivalence_reflexivity_proof_id
  candidate_equivalence_symmetry_proof_id
  candidate_equivalence_transitivity_proof_id
  candidate_isomorphism_closure_proof_id
  candidate_completeness_statement_id
  candidate_completeness_proof_id
  hidden_input_closure_id

gauge_square_manifest[]:
  comparison_id
  source_domain_id
  target_domain_id
  source_decoder_component_id
  target_decoder_component_id
  source_output_carrier_id
  target_output_carrier_id
  source_map_id
  output_transport_id
  membership_test_id
  commuting_square_id
  completeness_statement_id
  completeness_proof_id
  pre_output_freeze_basis_id

  strict_invariance_manifest:
    state = NOT_CLAIMED | DEFINED | UNRESOLVED

    DEFINED:
      common_domain_identification_id
      decoder_component_identification_id
      output_carrier_identification_id
      identity_output_transport_id
      strict_invariance_proof_id

    NOT_CLAIMED:
      nonstrict_square_basis_id

scale_manifest[]:
  source_scale_id
  target_scale_id
  source_domain_id
  target_domain_id
  source_decoder_component_id
  target_decoder_component_id
  source_output_carrier_id
  target_output_carrier_id
  source_map_id
  output_transport_id
  commuting_square_id
  blocking_origin_id
  phase_policy_id
  normalization_id
  pre_post_convention_id
  completeness_statement_id
  completeness_proof_id
  pre_output_freeze_basis_id

  strict_invariance_manifest:
    state = NOT_CLAIMED | DEFINED | UNRESOLVED

    DEFINED:
      common_domain_identification_id
      decoder_component_identification_id
      output_carrier_identification_id
      identity_output_transport_id
      strict_invariance_proof_id

    NOT_CLAIMED:
      nonstrict_square_basis_id

apparatus_reduction_manifest[]:
  source_protocol_id
  target_protocol_id
  source_domain_id
  target_domain_id
  source_decoder_component_id
  target_decoder_component_id
  source_output_carrier_id
  target_output_carrier_id
  reduction_precondition_id
  source_transport_id
  output_transport_id
  commuting_square_id
  reduction_equality_id
  membership_test_id
  completeness_statement_id
  completeness_proof_id
  pre_output_freeze_basis_id

U_congruence_manifest:
  state = DEFINED | NONE | UNRESOLVED

  DEFINED:
    U_id
    U_stable_domain_id
    U_restriction_id
    decoder_restriction_id
    decoder_image_id
    decoder_corestriction_id
    decoder_image_inclusion_id
    decoder_kernel_equality_id
    congruence_test_id
    induced_map_id
    induced_map_equality_id
    corestricted_factor_dynamics_equation_id

  NONE:
    no_U_congruence_claim_basis_id

categorical_coherence_manifest:
  state = NONE | DEFINED | UNRESOLVED

  DEFINED:
    object_class_id
    arrow_class_id
    identity_arrow_id
    composition_id
    arrow_closure_proof_id
    composition_associativity_proof_id
    left_unit_law_proof_id
    right_unit_law_proof_id
    source_identity_law_id
    source_composition_law_id
    output_identity_law_id
    output_composition_law_id
    decoder_family_naturality_id

    group_action_manifest:
      state = NOT_CLAIMED | DEFINED | UNRESOLVED

      DEFINED:
        inverse_assignment_id
        inverse_closure_proof_id
        left_inverse_law_proof_id
        right_inverse_law_proof_id

      NOT_CLAIMED:
        no_group_action_claim_basis_id

  NONE:
    no_categorical_coherence_claim_basis_id

maximality_manifest:
  state = NOT_CLAIMED | DEFINED | UNRESOLVED

  DEFINED:
    common_domain_id
    decoder_corestriction_id
    invisible_transformation_class_id
    strict_invariance_statement_id
    strict_invariance_proof_id
    admissible_invariant_class_id
    invariant_membership_test_id
    invariant_completeness_statement_id
    invariant_completeness_proof_id
    universal_factorization_statement_id
    universal_factorization_proof_id

    indexed_family_manifest:
      state = NONE | DEFINED | UNRESOLVED

      DEFINED:
        component_domain_manifest_id
        component_mediator_manifest_id
        component_mediator_compatibility_id

      NONE:
        single_scope_basis_id

nontriviality_manifest:
  state = NOT_CLAIMED | DEFINED | UNRESOLVED

  DEFINED:
    nonconstancy_certificate_id
```

Every identifier-valued field is a resolvable public identifier or
`UNRESOLVED`. There is no bare null. `DEFINED` does not mean proved. A
scientific owner and its evidence must decide the corresponding property.

`NONE` is the normal categorical-coherence state for the base per-map schema.
Categorical `DEFINED` requires every identity, composition, closure,
associativity, unit, source, output, and decoder-family field above. A group
claim additionally requires every inverse field. A componentwise indexed
claim requires its mediator compatibility field; otherwise its state is
`UNRESOLVED`.

`NOT_CLAIMED` is the normal strict-invariance state for a legitimate
non-strict commuting square. It supplies the named non-strict basis and does
not turn that square into an invisible transformation.

Maximality and nontriviality have independent states. `maximality =
NOT_CLAIMED` is required when the submission proves only factorization
through a named `q` and no universal invariant property. `nontriviality =
NOT_CLAIMED` is required when no exact nonconstancy claim is made. A defined
maximality claim may therefore coexist with `nontriviality = NOT_CLAIMED`.

## 7. Cross-leg and cross-stage firewall

The following inheritance is forbidden:

```text
D_quadratic factorization  -/->  D_binary or D_linear factorization
D_binary coherence         -/->  D_quadratic instrument selection
one D_matter field         -/->  every MatterData field
D_matter closure           -/->  D_geom or D_clock closure
L5 reduction equivalence   -/->  L6 normalization
effect equality            -/->  instrument equality
common numeric value       -/->  typed bridge
comparison action          -/->  adopted gauge
```

A relation between legs requires an explicit `bridge_manifest[]` row with
source, target, domain, codomain, equality, map, dependencies, layer
endpoints, and every required public gate. A common decoder stage does not
supply that bridge.

## 8. Three separate existing instances

### 8.1 Thue-Morse selector and measure surface

`TM-SYM2-PROJECTIVE-FOURFOLD [T]` proves at its frozen scope that 48 exact
selectors form four projective-gauge orbits of 12 and have one common
mathematical pushforward and operator. It does not select a representative,
adopt a larger gauge, or prove a physical probability.

`TM-SYM2-PHYSICAL-MEASURE [O]` is the separate existing owner of any future
physical L5-to-L6 coherence statement. It must retain
`epsilon_read = chi_Q chi_F` as typed L5 data, consume all 48 selectors,
avoid enlarging the fired projective gauge, and prove the registered Born
and normalization bridge. This predefinition neither supplies that source
schema nor changes its `STOP` state.

`GYRON-DENSITY [T]` owns the stationary sliding-pair density `1/6`.
The equal number in the six-line cardinal average is not a typed bridge.
No factor-canonicity instance may identify the two without an exact source
map, marginal or event map, domain, equality, normalization, and layer gate.

The fired `TM-SYM2-MEASURE [F]` boundary remains terminal at its frozen
selector gate. Factor language may not reopen or repair it.

### 8.2 Quadratic decoder data

`QUADRATIC-DECODER-DATA [O]` is the existing owner of the statement that
every frozen `D_quadratic` field at stage `D_matter` factors through

```text
Q(psi) = (psi psi^dagger, psi psi^T)
```

on one published common totality domain. At that scope the relevant future
test is fiber constancy. Factorization through `Q` would not prove that `Q`
is maximal, that the whole decoder is canonical, or that a post-state
instrument is unique.

The current issue #107 owner decision is noncanonical and definition-only. It
adopts Route A / `c_0` as the scoped `D_quadratic` write dictionary proposal,
not as a Canon claim, independent `Q`-factor theorem, physical source, or
canonicity theorem. The remaining apparatus and instrument documents stay at
their exact noncanonical scopes. Their source-free Q2 apparatus algebra,
effect candidates, instrument equalities, and conditional classifications do
not supply a kernel source, source-selected physical image, public physical
identifiers, layers, gates, sampling, history, writeback, or physical
completeness. Nothing in this note imports them into the public QDD manifest.

### 8.3 Metrology reduction

`METRO-REDUCTION-CALCULUS [O]` owns the typed `U_RF` protocol objects,
admitted L5 reduction arrows, exact output transport `tau_R`, and generated
finite-zig-zag equivalence `approx_red`. It owns no normalization or
cross-layer gate.

The Metro reduction class does not automatically act on TM selectors, QDD
amplitudes, QDD instruments, or decoder records. Such use requires a
separately frozen bridge from the instance carrier into `U_RF`, exact
transport of every owned output field, and a declared owner. This
predefinition creates no such bridge.

## 9. Issue #107 debt firewall

The controlling current disposition in
`P-DMATTER-TOTAL-1-ROUTE-A-OWNER-DECISION.md` is:

```text
ROUTE A / c_0:          OWNER-ADOPTED PROPOSAL / DEFINITION-ONLY / NOT CANON
ROUTE B DEFAULT:        SUPERSEDED ONLY FOR ISSUE #107 ROUTING
D_scoped:               ADOPTED SCOPED WRITE-DICTIONARY PROPOSAL
Adm_GalSplit:           NOT ADOPTED
D_direct:               UNRESOLVED
QUADRATIC-DECODER-DATA: O / STOP
FORMAL PROBE:           FORBIDDEN
```

The adopted definition keeps the visible choice

```text
c_0 = (0, B0, iota_0, L_0, H_0, Pi_0),
D_scoped := R_cyc o iota_B0 o beta,
D_scoped = F_Gram o Qcan o beta.
```

The second equality is a derived identity of the adopted definitions. It is
not `QDD-INDEPENDENT-Q-FACTOR`, a blind scientific target, or a theorem that
`c_0` is canonical. The choice of `c_0` remains visible.

Accordingly this schema neither imports that decision into Canon nor undoes,
reopens, or reroutes it. In particular it:

1. does not restore Route B as the issue #107 default;
2. does not restart the closed `C5` search;
3. does not use invariance or maximality language to adopt `Adm_GalSplit`;
4. does not manufacture `D_direct` or reclassify the displayed derived
   identity as an independent `Q`-factorization;
5. does not treat the scoped write dictionary, an apparatus singleton, or an
   algebraic `aleph_0` quotient as a physical classification;
6. does not create a replacement QDD owner or umbrella decoder owner;
7. does not move `QUADRATIC-DECODER-DATA` from `O / STOP` or authorize its
   forbidden formal probe.

The still-open scientific obligations remain separately owned:

```text
QDD-SCOPED-WRITE-DICTIONARY       definition-only adopted proposal scope
QDD-INDEPENDENT-Q-FACTOR          O / STOP
QDD-PHYSICAL-EFFECT-SELECTION     O / STOP
QDD-HYBRID-CARRIER-BRIDGE         O / STOP
```

This factor-canonicity schema supplies no precedent for resolving any of
those scientific obligations.

## 10. Future scientific kill tests

After a separately owned instance has reached an exact pre-output freeze and
its classification has formally opened, the following are legitimate
scientific kill tests at that instance's scope:

Immediate falsification of uniqueness is weaker than an exact
`NONUNIQUE(kappa)` classification.

```text
FACTOR-FAILURE
    q(x)=q(x') but D(x)!=D(x') for exact admitted x,x';

GAUGE-SQUARE-FAILURE
    D_t(gx)!=Gamma_g(D_s(x)) for an exact admitted gauge comparison g;

SCALE-FAILURE
    D_(b ell)(R_(b,ell)x)!=Z_(b,ell)(D_ell(x));

APPARATUS-FAILURE
    an admitted reduction violates its frozen commuting square;

U-CONGRUENCE-FAILURE
    D(x)=D(x') but D(Ux)!=D(Ux') on the frozen U-stable domain,
    only when U-congruence was claimed;

UNIQUENESS-FALSIFIED
    two exact inequivalent candidates survive; this conclusion is immediate
    and requires no exhaustion claim;

NONUNIQUE(kappa)
    a complete exact classification proves that the survivor quotient has
    the exact cardinal kappa >= 2 and at least one survivor is nonconstant;

CONSTANT-ONLY
    a complete exact classification leaves at least one candidate and every
    survivor is constant;

EMPTY
    a complete exact classification leaves no candidate.
```

Each result belongs to its separately registered owner and decision
condition. This note owns none of those outcomes.

## 11. Possible v24 disposition

A possible Public Canon v24 may use this note only for a definition-only
extension of `DEF-DECODER-COMPLETION-CONTRACT`. That disposition would:

1. add no `DECODER-UNIVERSALITY`, `H-DECODER-UNIVERSALITY`, or other umbrella
   registry row;
2. add no public claim, status, evidence item, frontier count, dependency,
   gate, probe, verifier, run, or scientific result;
3. preserve `GYRON-DENSITY [T]`,
   `TM-SYM2-PROJECTIVE-FOURFOLD [T]`,
   `TM-SYM2-PHYSICAL-MEASURE [O]`,
   `QUADRATIC-DECODER-DATA [O]`,
   `METRO-REDUCTION-CALCULUS [O]`, and
   `OBSERVER-WRITE-PORT [H]` at their exact current scopes and statuses;
4. state that gauge comparison, scale covariance, apparatus reduction, and
   optional `U`-congruence are four different typed per-map obligations;
5. reserve `nontrivial maximal invariant` and universality language for a
   later complete maximality proof plus a separate exact nonconstancy
   certificate, all with independently frozen inputs.

Any wider v24 use requires a separate owner decision. Until such a reviewed
fold exists, this file remains a noncanonical definition proposal and its
only current routing is

```text
DEFINITION-DRAFT-COMPLETE / SCIENTIFIC-CLASSIFICATION-STOP.
```
