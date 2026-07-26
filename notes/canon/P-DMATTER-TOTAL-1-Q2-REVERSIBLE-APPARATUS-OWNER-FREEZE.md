# P-DMATTER-TOTAL-1 Q2 Reversible-Apparatus Owner Freeze (NON-CANONICAL)

```text
STATUS:                 OWNER-ADOPTED DEFINITION RULING /
                        APPARATUS-PACKAGE FREEZE
AUTHORITY:              NOT CANON
SCOPE:                  PROPOSAL-LOCAL / DEFINITION-ONLY / SOURCE-UNBOUND
OWNER DECISION:         Q2 / READY-IN-ONE-OUTCOME /
                        FULL REVERSIBLE JOINT EVOLUTION
SYSTEM-SIDE RULE:       FULL-COMMUTANT READY REDUCTION, inherited
KERNEL SOURCE:          UNRESOLVED
SOURCE-SELECTED IMAGE:  UNRESOLVED
PHYSICAL CLASSIFICATION: NOT OPEN
PUBLIC BASE:            Public Canon v23
PUBLIC CANON TAG:       canon-v23
ACTIVATION COMMIT:      4ac41b4fac3a3794a6e9d5be1e2027d324edb806
CONTENT COMMIT:         7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:            116017
PUBLIC MAIN BASE:       ab87e292668075ea83258cc2cc83324a735a068e
INSTRUMENT PREDEFINITION:
                        1cfde364a3ad7f64730433ed142fd7cb04df6064779087f7144ffa6991918ee6
KERNEL-APPARATUS PREDEFINITION:
                        ec412acd3b4d03d17a1296d651c7c2145535b07950575bfa1cc89f410464f23c
FULL-COMMUTANT OWNER FREEZE:
                        133c7dceef9e51148445a8f52ea71a07d84e9aae59b64ff870be47bcbe005bba
CLAIM ISSUE:            107
A11 STATUS:             PARTIAL / O-STOP, unchanged
QDD STATUS:             O / STOP, unchanged
FORMAL RUN:             NONE
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
GATE CHANGE:            NONE
```

This ruling adopts the minimal two-sector rational apparatus package exposed
by the preceding owner freeze. It fixes the apparatus carrier, ready state,
joint tensor carrier, complete source-free reversible coupling class,
algebraic pointer projectors, ready reduction, apparatus equality, and exact
apparatus-side completeness theorem.

It does not adopt a kernel source, a source-to-coupling selector, public
physical outcome identifiers, layers, gates, sampling, history update,
writeback, or completion-wide terminality. It does not open a physical
classification.

Two pre-freeze corrections are binding:

1. `K_low tensor I_2 + K_high tensor X` is a valid reversible witness for
   every admitted reduced pair. It is not generally natural-self-adjoint or
   involutive.
2. Full reversibility does not imply or adopt full-joint sector preservation
   away from the ready input. The complete coupling class is constrained by
   its derived ready reduction, not by an off-ready QND law.

## 0. Falsification and freeze firewall first

The present package is mathematically inconsistent if any of the following
is false:

```text
Q2-POINTER
    F_low and F_high are nonzero, orthogonal, rank-one, and exhaustive.

FULL-REVERSIBILITY
    U^natural U = I_8 for a square rational U implies
    U U^natural = I_8.

CONTROLLED-X-WITNESS
    every K in Adm_comm has a reversible Q2 realization reducing to K.

CROSS-ADJOINT-WITNESS
    every K in Adm_comm has a natural-self-adjoint involutive Q2
    realization reducing to K.

SCOPED-COMPLETENESS
    Red(Cpl_Q2_rev_comm) = Adm_comm.

MINIMALITY
    no apparatus of dimension less than two has two nonzero orthogonal
    exhaustive pointer sectors.
```

Failure of a displayed identity returns
`APPARATUS-PACKAGE-INCONSISTENT / STOP`. This is not Canon or registry `F`.

Before a physical classification opens, a continuation returns
`FREEZE-BREACH / STOP` if it does any of the following without a new
pre-opening owner ruling:

1. replaces `Q^2`, the ordered basis `(f_low,f_high)`, or `eta=f_low`;
2. replaces `READY-IN-ONE-OUTCOME` by a neutral ready state;
3. changes the standard rational apparatus pairing;
4. changes the tensor joint carrier or `G tensor I_2`;
5. weakens exact rational reversibility to a tolerance;
6. adds natural self-adjointness, involutivity, full-joint sector
   preservation, weak or full QND, centrality, a preferred frame, or a
   Luders-only condition to coupling-class membership;
7. supplies `K_a` independently rather than deriving it from `U`;
8. changes apparatus equality from exact `M_8(Q)` equality;
9. changes the inherited `Eq_instrument` classification equality;
10. treats the algebraic strings `low` and `high` as public physical outcome
    identifiers;
11. assumes that a kernel source realizes every coupling in the source-free
    apparatus class;
12. fills a source, public-ID, layer, gate, sampling, history, writeback,
    dependency, or terminality field by inference;
13. reports physical `PASS`, `NONUNIQUE`, `EMPTY`, or Canon `F`;
14. moves A11 or `QUADRATIC-DECODER-DATA` from `O / STOP`.

After a physical classification opens, any change to the apparatus carrier,
ready state, joint composition, coupling class, apparatus equality, pointer,
reduction, source, source-selection relation, public identifiers, physical
outcomes, layer, gate, sampling, history, writeback, dependency closure,
completeness method, classification equality, or output meaning returns
`FIRE-POSTHOC`.

## 1. Inherited system boundary

The fixed rational system carrier is

```text
H_Q = (Q^4, <x,y>_G = x^T G y),

G       = I_4 - (1/5) 1 1^T,
G^(-1)  = I_4 + 1 1^T,
A^sharp = G^(-1) A^T G,

E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low.
```

The complete algebraic single-operator universe remains

```text
Instr_alg
  = { (K_low,K_high) in M_4(Q)^2 :
      K_a^sharp K_a = E_a for a in {low,high} }.
```

The preceding owner ruling fixes

```text
C = Comm(E_low,E_high),

Adm_comm
  = { (K_low,K_high) in Instr_alg :
      K_a in C for each a in {low,high} }.
```

Operational `Eq_instrument`, exact matrix `Eq_K_matrix`, and
`Eq_effect` remain distinct. The fixed labels are ordered and are not
swapped.

This note changes none of that boundary. It supplies a complete apparatus
realization of the source-free class `Adm_comm`.

## 2. Q2 apparatus and ready state

Freeze

```text
A_Q = (Q^2, <r,s>_A = r^T s),

f_low  = (1,0)^T,
f_high = (0,1)^T,

F_low  = f_low f_low^T,
F_high = f_high f_high^T.
```

The apparatus equality is coordinate equality in `Q^2`. Endomorphism
equality is entrywise equality in `M_2(Q)`.

The pointer identities are exact:

```text
F_a^T = F_a,
F_a^2 = F_a,
F_low F_high = F_high F_low = 0,
F_low + F_high = I_2,
rank(F_low) = rank(F_high) = 1.
```

Freeze the ready convention

```text
READY-IN-ONE-OUTCOME,

eta = f_low,
ReadyDomain = {eta},

F_low eta  = eta,
F_high eta = 0.
```

The choice of `low` rather than `high` is an explicit discrete model choice.
It is not derived from `J`, apparatus minimality, or a gauge quotient.
Because the algebraic labels are ordered and are not identified by any
adopted algebraic equivalence, the choice remains visible.

The apparatus dimension is minimal at the declared scope. If two pointer
projectors are nonzero, orthogonal, and exhaustive on a finite-dimensional
carrier `A`, then

```text
dim(A) = rank(F_low) + rank(F_high) >= 2.
```

The displayed `Q^2` carrier reaches the bound. A neutral ready sector
orthogonal to both outcome sectors would require dimension at least three
and a changed pointer/exhaustivity rule. That branch is not adopted.

## 3. Joint carrier, pointer, and ready reduction

Freeze the joint carrier and pairing

```text
H_tot = H_Q tensor_Q A_Q = Q^8,

G_tot = G tensor I_2,

<Psi,Phi>_tot = Psi^T G_tot Phi,

Z^natural = G_tot^(-1) Z^T G_tot.
```

The factor-operator embeddings are

```text
i_sys(T) = T tensor I_2,
i_app(B) = I_4 tensor B.
```

They do not identify state carriers or assign a public action layer.

Define

```text
J_eta : H_Q -> H_tot,
J_eta x = x tensor eta,

R_a : H_tot -> H_Q,
R_a = I_4 tensor f_a^T,

Pi_a = R_a^natural R_a = I_4 tensor F_a.
```

Then

```text
J_eta^natural J_eta = I_4,
Pi_a^natural = Pi_a,
Pi_a Pi_b = delta_(a,b) Pi_a,
Pi_low + Pi_high = I_8.
```

Every joint vector has the unique pointer-component decomposition

```text
Psi
  = (R_low Psi) tensor f_low
  + (R_high Psi) tensor f_high.
```

The exact algebraic pointer map is

```text
Ptr_Q2 : {low,high} -> End_Q(A_Q),
Ptr_Q2(a) = F_a.
```

Its two events are exhaustive and equality-compatible. This map does not
sample or realize an event. `low` and `high` remain algebraic labels, not
public physical outcome identifiers.

For a coupling `U`, define the ready reduction

```text
K_a(U) = R_a U J_eta,

Red(U) = (K_low(U),K_high(U)).
```

`K_a` is an output of `U`. It is never an independent candidate input.

## 4. Complete source-free reversible coupling class

Freeze

```text
Cpl_Q2_rev_comm
  = { U in M_8(Q) :
      U^natural U = I_8
      and Red(U) in Adm_comm }.
```

Because `U` is a square matrix over `Q`, the first equation supplies a left
inverse and therefore

```text
U^(-1) = U^natural,
U U^natural = I_8.
```

Thus every member is a full reversible joint evolution. The second
two-sided identity is a derived certificate, not an additional filter.

Candidate membership is a finite exact decision:

```text
1. read one U in M_8(Q);
2. verify U^natural U = I_8;
3. compute K_a(U) = R_a U J_eta;
4. verify K_a(U)^sharp K_a(U) = E_a;
5. verify [K_a(U),E_b] = 0 for every a,b in {low,high}.
```

All assertions use rational matrix equality. There is no tolerance, search,
randomness, measured value, or hidden supplied `K`.

Apparatus-realization equality is

```text
U Eq_apparatus U'  iff  U = U' entrywise in M_8(Q).
```

It is not `Eq_instrument`. Many distinct joint couplings may reduce to the
same operational instrument.

No other coupling law is adopted. In particular, membership does not require

```text
U^natural = U,
U^2 = I_8,
[U,E_a tensor I_2] = 0,
full-joint QND,
full-joint central control,
ready-reduced centrality,
a preferred high-sector frame,
or a Luders-only reduction.
```

The action of `U` outside the ready subspace `Image(J_eta)` is constrained
only by reversibility and by exact matrix equality.

## 5. Exact apparatus-side completeness

The inclusion

```text
Red(Cpl_Q2_rev_comm) subset Adm_comm
```

is immediate from class membership. The reverse inclusion has two exact
constructive witnesses.

Let

```text
K = (K_low,K_high) in Adm_comm.
```

First derive the sector supports. For `a != b`,

```text
(K_a E_b)^sharp (K_a E_b)
  = E_b K_a^sharp K_a E_b
  = E_b E_a E_b
  = 0.
```

Positive definiteness of `G` gives `K_a E_b=0`. Since `K_a` commutes with the
effects,

```text
K_a = E_a K_a E_a.
```

On the one-dimensional low sector,

```text
K_low = epsilon_low E_low,
epsilon_low in {+1,-1},

K_low^sharp = K_low,
K_low^2 = E_low.
```

On the three-dimensional high sector, the restriction

```text
L = K_high | Image(E_high)
```

obeys `L^sharp L=I_3`. A square finite-dimensional map with a left inverse is
invertible, so `L^(-1)=L^sharp`. Therefore

```text
K_high K_high^sharp = E_high.
```

### 5.1 Controlled-X reversible witness

Let

```text
S = f_high f_low^T,
X = S + S^T
  = [0 1
     1 0].
```

Define

```text
U_K^X
  = K_low tensor I_2
  + K_high tensor X.
```

Low/high cross terms vanish, `X^T X=I_2`, and hence

```text
(U_K^X)^natural U_K^X
  = (K_low^sharp K_low + K_high^sharp K_high) tensor I_2
  = I_8.
```

Furthermore,

```text
U_K^X J_eta x
  = K_low x tensor f_low
  + K_high x tensor f_high,

R_a U_K^X J_eta = K_a.
```

Thus `U_K^X` lies in `Cpl_Q2_rev_comm` and reduces to `K`.

For generic `K_high`, this witness need not satisfy

```text
(U_K^X)^natural = U_K^X
or
(U_K^X)^2 = I_8.
```

It is nevertheless exactly reversible, which is the class requirement.

### 5.2 Cross-adjoint strong witness

The apparatus shift obeys

```text
S^2 = (S^T)^2 = 0,
S S^T = F_high,
S^T S = F_low.
```

Define

```text
U_K^ca
  = K_low tensor I_2
  + K_high tensor S
  + K_high^sharp tensor S^T.
```

Then

```text
(U_K^ca)^natural = U_K^ca.
```

All low/high cross terms vanish, and

```text
(U_K^ca)^2
  = E_low tensor I_2
    + (K_high K_high^sharp) tensor F_high
    + (K_high^sharp K_high) tensor F_low
  = I_8.
```

It has the same ready action:

```text
U_K^ca J_eta x
  = K_low x tensor f_low
  + K_high x tensor f_high,

R_a U_K^ca J_eta = K_a.
```

Thus every member of `Adm_comm` has both a general controlled-X reversible
witness and a stronger natural-self-adjoint involutive witness. The stronger
properties belong to the witness, not to coupling-class membership.

The exact source-free completeness result is

```text
Q2-FULL-REVERSIBLE-REDUCTION-SURJECTIVITY:

Red(Cpl_Q2_rev_comm) = Adm_comm.
```

This is a complete two-inclusion proof over the exact candidate class, not a
hand-selected list.

## 6. Off-ready firewall

Ready-domain behavior does not determine the full joint action.

For an exact witness, let `v=e_1` and define the rational `G`-orthogonal
Householder map

```text
P
  = I_4 - 2 v (v^T G) / (v^T G v).
```

It satisfies

```text
P^sharp P = I_4,
[P,E_low] != 0.
```

Let

```text
W
  = I_4 tensor F_low
    + P tensor F_high,

U_L
  = E_low tensor I_2
    + E_high tensor X,

U = U_L W.
```

Both factors are `G_tot`-unitary and `W J_eta=J_eta`. Hence

```text
Red(U) = Red(U_L) = (E_low,E_high),
U in Cpl_Q2_rev_comm.
```

But

```text
[U,E_low tensor I_2] != 0.
```

Therefore full-joint sector preservation is neither a membership condition
nor a consequence of the adopted package. Rejecting this `U` solely because
of its off-ready mixing would silently add the unadopted QND principle.

## 7. Apparatus quotient and kernel-source firewall

Because

```text
Red(Cpl_Q2_rev_comm) = Adm_comm
```

and the preceding owner freeze proves

```text
|Adm_comm / Eq_instrument| = aleph_0,
```

the exact apparatus-relative result is

```text
Q2-APPARATUS-ALEPH0-ALGEBRAIC.
```

It is not physical `NONUNIQUE(aleph_0)`.

A future physical source package must freeze an exact set

```text
PhysReal subset KernelSource x Cpl_Q2_rev_comm.
```

Its source-selected reduced image is

```text
PhysImage
  = { Red(U) :
      exists source with (source,U) in PhysReal }.
```

The physical classification is

```text
PhysImage / Eq_instrument,
```

not the quotient of the complete source-free apparatus class.

The distinction is strict. A constant source selector

```text
B(source) = U_L
```

has one coupling matrix in its image and one Luders instrument class after
reduction, even though the source-free apparatus quotient has cardinality
`aleph_0`.

Depending on a future independently frozen source relation, the physical
image may be empty, one class, a finite `k`, or countably infinitely many
classes (`aleph_0`). Merely
naming a kernel source while leaving it inert in coupling selection does not
prove physical completeness.

The existing Route A map `beta` maps an anchored orbit to an amplitude. It
does not select a member of `Cpl_Q2_rev_comm` and is not promoted to that
role by this ruling.

## 8. Proposal-local schema coverage

Every `CAND-*` identifier below is proposal-local. It fills no public
completion-contract slot.

### 8.1 Locally defined apparatus and ready fields

```text
apparatus_carrier_id:
    CAND-QDD-APPARATUS-CARRIER-AQ-Q2
apparatus_coefficient_object_id:
    CAND-COEFFICIENT-RING-Q
apparatus_membership_id:
    CAND-QDD-MEMBERSHIP-AQ-Q2
apparatus_equality_id:
    CAND-QDD-EQ-AQ-Q2-VECTOR
apparatus_pairing_id:
    CAND-QDD-PAIRING-AQ-I2

ready_state_carrier_id:
    CAND-QDD-APPARATUS-CARRIER-AQ-Q2
ready_state_id:
    CAND-QDD-READY-STATE-ETA-Q2
ready_state_value_id:
    CAND-QDD-POINTER-BASIS-VECTOR-F-LOW-Q2
ready_state_equality_id:
    CAND-QDD-EQ-AQ-Q2-VECTOR
ready_domain_id:
    CAND-QDD-READY-DOMAIN-SINGLETON-ETA-Q2
ready_to_pointer_relation_id:
    CAND-QDD-READY-TO-POINTER-RELATION-LOW-Q2
ready_certificate_id:
    CAND-QDD-CERT-READY-IN-LOW-POINTER-Q2
```

The ruling identifier is

```text
CAND-QDD-OWNER-FREEZE-Q2-REVERSIBLE-APPARATUS.
```

### 8.2 Locally defined joint and coupling fields

```text
joint_carrier_id:
    CAND-QDD-JOINT-CARRIER-HQ-TENSOR-AQ-Q2
joint_composition_id:
    CAND-QDD-JOINT-COMPOSITION-TENSOR-Q
joint_equality_id:
    CAND-QDD-EQ-JOINT-Q8-VECTOR
joint_pairing_id:
    CAND-QDD-JOINT-PAIRING-G-TENSOR-I2
joint_adjoint_id:
    CAND-QDD-JOINT-ADJOINT-G-TENSOR-I2
system_embedding_id:
    CAND-QDD-SYSTEM-OPERATOR-EMBEDDING-TENSOR-I2-Q2
apparatus_embedding_id:
    CAND-QDD-APPARATUS-OPERATOR-EMBEDDING-I4-TENSOR-Q2

coupling_class_id:
    CAND-QDD-COUPLING-CLASS-UFULL-Q2-REVERSIBLE-ADM-COMMUTANT
coupling_map_id:
    CAND-QDD-COUPLING-EVALUATION-UFULL-Q2
coupling_domain_id:
    CAND-QDD-COUPLING-EVALUATION-DOMAIN-UFULL-Q2
coupling_codomain_id:
    CAND-QDD-JOINT-CARRIER-HQ-TENSOR-AQ-Q2
coupling_totality_domain_id:
    CAND-QDD-COUPLING-EVALUATION-DOMAIN-UFULL-Q2
coupling_preservation_law_id:
    CAND-QDD-PRESERVATION-LAW-G-TENSOR-I2
coupling_equality_id:
    CAND-QDD-EQ-UFULL-Q2-MATRIX
coupling_membership_id:
    CAND-QDD-MEMBERSHIP-UFULL-Q2-ADM-COMMUTANT
```

### 8.3 Locally defined pointer-event boundary

```text
pointer_carrier_id:
    CAND-QDD-APPARATUS-CARRIER-AQ-Q2
pointer_equality_id:
    CAND-QDD-EQ-AQ-Q2-VECTOR
pointer_projector_carrier_id:
    CAND-QDD-POINTER-PROJECTOR-CARRIER-END-AQ-Q2
pointer_projector_equality_id:
    CAND-QDD-EQ-POINTER-PROJECTOR-Q2-MATRIX
pointer_map_id:
    CAND-QDD-POINTER-MAP-LABEL-TO-PROJECTOR-Q2
pointer_map_domain_id:
    CAND-QDD-ALGEBRAIC-LABEL-CARRIER-LOW-HIGH
pointer_map_codomain_id:
    CAND-QDD-POINTER-PROJECTOR-CARRIER-END-AQ-Q2
pointer_map_totality_domain_id:
    CAND-QDD-ALGEBRAIC-LABEL-CARRIER-LOW-HIGH
pointer_map_totality_certificate_id:
    CAND-QDD-CERT-POINTER-MAP-TOTAL-Q2
pointer_map_equality_compatibility_id:
    CAND-QDD-CERT-POINTER-MAP-EQUALITY-Q2

pointer_event_ids:
    CAND-QDD-POINTER-PROJECTOR-F-LOW-Q2
    CAND-QDD-POINTER-PROJECTOR-F-HIGH-Q2
pointer_event_equality_id:
    CAND-QDD-EQ-POINTER-PROJECTOR-Q2-MATRIX
pointer_exhaustivity_certificate_id:
    CAND-QDD-CERT-POINTER-EVENTS-EXHAUSTIVE-Q2

joint_pointer_event_ids:
    CAND-QDD-JOINT-POINTER-EVENT-PI-LOW-Q2
    CAND-QDD-JOINT-POINTER-EVENT-PI-HIGH-Q2
ready_embedding_id:
    CAND-QDD-READY-EMBEDDING-J-ETA-Q2
pointer_component_ids:
    CAND-QDD-POINTER-COMPONENT-R-LOW-Q2
    CAND-QDD-POINTER-COMPONENT-R-HIGH-Q2
```

The following strict pointer fields remain literal `UNRESOLVED`:

```text
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
outcome_to_route_label_equality_compatibility_id.
```

### 8.4 Locally defined source-free reduction

```text
reduction_map_id:
    CAND-QDD-REDUCTION-RED-UFULL-Q2
reduction_domain_id:
    CAND-QDD-COUPLING-CLASS-UFULL-Q2-REVERSIBLE-ADM-COMMUTANT
reduction_codomain_id:
    CAND-QDD-ADM-COMMUTANT
reduction_equality_id:
    CAND-QDD-EQ-K-MATRIX

reduction_component_ids:
    CAND-QDD-POINTER-COMPONENT-R-LOW-Q2
    CAND-QDD-POINTER-COMPONENT-R-HIGH-Q2
reduction_to_K_certificate_ids:
    CAND-QDD-CERT-REDUCTION-R-LOW-U-J-ETA-Q2
    CAND-QDD-CERT-REDUCTION-R-HIGH-U-J-ETA-Q2
    CAND-QDD-CERT-REDUCTION-TOTAL-UFULL-Q2
    CAND-QDD-CERT-REDUCTION-EQUALITY-UFULL-Q2

K_matrix_equality_id:
    CAND-QDD-EQ-K-MATRIX
instrument_operation_equality_id:
    CAND-QDD-EQ-INSTRUMENT-OPERATIONAL
effect_equality_id:
    CAND-QDD-EQ-EFFECT-MATRIX
event_operation_id:
    CAND-QDD-EVENT-OPERATION
post_event_semantics_id:
    CAND-QDD-POST-STATE-TAGGED
outcome_coarse_graining_id:
    CAND-QDD-COARSE-FORGET-OUTCOME

effect_certificate_ids:
    CAND-QDD-CERT-REDUCTION-EFFECTS-ELOW-EHIGH-Q2
normalization_completeness_certificate_id:
    CAND-QDD-CERT-REDUCTION-NORMALIZATION-Q2
born_identity_certificate_id:
    CAND-QDD-CERT-REDUCTION-BORN-TRACE-Q2

controlled_X_witness_id:
    CAND-QDD-CONTROLLED-X-REVERSIBLE-LIFT-U-K-Q2
cross_adjoint_witness_id:
    CAND-QDD-CROSS-ADJOINT-LIFT-U-K-Q2
cross_adjoint_reversibility_certificate_id:
    CAND-QDD-CERT-CROSS-ADJOINT-REVERSIBLE-Q2
cross_adjoint_reduction_certificate_id:
    CAND-QDD-CERT-CROSS-ADJOINT-REDUCES-TO-K-Q2
```

Algebraic effect candidates and the trace Born pairing may be cited for the
displayed certificates. They do not become public physical IDs.

The following physical reduction fields remain `UNRESOLVED`:

```text
derived_instrument_ids
derived_effect_ids
born_pairing_id
MatterData_outcome_field_ids
MatterData_outcome_read_map_ids
MatterData_outcome_write_map_ids.
```

### 8.5 Locally defined apparatus admissibility and scoped completeness

```text
apparatus_realization_id:
    CAND-QDD-APPARATUS-REALIZATION-Q2-UFULL
apparatus_realization_equality_id:
    CAND-QDD-EQ-UFULL-Q2-MATRIX
candidate_universe_id:
    CAND-QDD-COUPLING-CLASS-UFULL-Q2-REVERSIBLE-ADM-COMMUTANT
candidate_universe_equality_id:
    CAND-QDD-EQ-UFULL-Q2-MATRIX
candidate_universe_membership_test_id:
    CAND-QDD-MEMBERSHIP-UFULL-Q2-ADM-COMMUTANT
instrument_classification_equality_id:
    CAND-QDD-EQ-INSTRUMENT-OPERATIONAL

scoped_completeness_statement_id:
    CAND-QDD-SCOPED-COMPLETENESS-RED-UFULL-EQUALS-ADM-COMMUTANT
scoped_completeness_proof_id:
    CAND-QDD-SCOPED-COMPLETENESS-PROOF-CROSS-ADJOINT-Q2
scoped_completeness_method_id:
    CAND-QDD-SCOPED-COMPLETENESS-METHOD-CROSS-ADJOINT-Q2
```

These scoped completeness identifiers prove apparatus-side surjectivity
only. They do not fill the strict physical fields

```text
physical_admissibility_predicate_id
physical_admissibility_domain_id
physical_admissibility_codomain_id
physical_admissibility_totality_domain_id
physical_admissibility_decision_procedure_id
completeness_statement_id
completeness_proof_id
completeness_method_id.
```

Every field in that last block remains `UNRESOLVED`.

## 9. Explicit unresolved and non-adopted ledger

The entire `kernel_source_manifest` remains `UNRESOLVED`:

```text
kernel_source_id
kernel_state_carrier_id
kernel_state_equality_id
kernel_totality_domain_id
kernel_to_amplitude_bridge_id
bridge_domain_id
bridge_codomain_id
bridge_equality_id.
```

The following also remain `UNRESOLVED`:

```text
source-to-coupling selection relation
source-selected physical image and equality
public physical instrument, effect, Born, and outcome IDs
public MatterData outcome rows and maps
all layer assignments
all gate bindings
sampling_manifest
history_update_manifest
writeback_manifest
dependency_closure_manifest
completion_contract_binding_manifest
completion-wide terminality.
```

No tagged `NONE` choice is inferred. The existing stage-local
`feeds_U=FALSE` for `D_scoped` does not choose apparatus writeback and does
not close `OBSERVER-WRITE-PORT`.

Every `CAND-*` value in this note is `LOCAL-DEFINED` only. Its value in a
strict public identifier slot remains the literal `UNRESOLVED` until a later
normative action creates a resolvable public identifier.

The package also does not adopt:

```text
neutral-ready Q3 apparatus
multi-Kraus or micro-outcome extensions
sampling or collapse as an autonomous update
full-joint sector preservation
weak or full QND
natural self-adjointness or involutivity as a class filter
ready-reduced centrality
full-joint central control
preferred high-sector frame
Luders-only apparatus
kernel-source surjectivity.
```

## 10. Frozen output semantics

```text
OWNER-APPARATUS-PACKAGE-FROZEN
    Q2, eta=f_low, the joint tensor carrier, exact reversible coupling
    class, pointer PVM, ready reduction, apparatus equality, and
    apparatus-side completeness theorem are frozen.

APPARATUS-PACKAGE-INCONSISTENT
    A displayed apparatus, reversibility, witness, minimality, or
    completeness identity is false. The physical classification remains
    STOP. This is not Canon F.

Q2-FULL-REVERSIBLE-REDUCTION-SURJECTIVITY
    Red(Cpl_Q2_rev_comm)=Adm_comm exactly.

Q2-APPARATUS-ALEPH0-ALGEBRAIC
    The source-free apparatus reduction quotient has cardinality aleph_0.
    This is not physical NONUNIQUE.

SOURCE-SELECTED-IMAGE-UNRESOLVED
    No exact kernel source and source-to-coupling relation has been frozen.

OWNER-INPUT-REQUIRED
    At least one source, physical outcome, public-ID, layer, gate, sampling,
    history, writeback, dependency, terminality, or full physical
    completeness field remains unresolved.

READY-FOR-CLASSIFICATION
    Requires a complete exact source-selected physical universe and every
    strict interface field. This ruling does not reach that state.

STOP
    Any required type, map, source, identifier, layer, gate, dependency,
    or completeness proof is missing or inexact.

FIRE-POSTHOC
    Any frozen input or output meaning changes after physical
    classification opens.
```

The current combined output is

```text
OWNER-BRANCH-FROZEN
OWNER-APPARATUS-PACKAGE-FROZEN
Q2-FULL-REVERSIBLE-REDUCTION-SURJECTIVITY
Q2-APPARATUS-ALEPH0-ALGEBRAIC
SOURCE-SELECTED-IMAGE-UNRESOLVED
OWNER-INPUT-REQUIRED / STOP.
```

## 11. Exact status consequence

```text
A_Q = Q^2                              OWNER-ADOPTED, proposal-local
READY-IN-ONE-OUTCOME                   OWNER-ADOPTED
eta = f_low                            OWNER-ADOPTED discrete choice
pointer projectors F_low,F_high        FIXED, algebraic events
joint carrier H_Q tensor_Q A_Q         OWNER-ADOPTED
full reversible coupling class         OWNER-ADOPTED
apparatus equality U=U'                FIXED
ready reduction Red(U)                 FIXED
Red(Cpl_Q2_rev_comm)=Adm_comm           EXACT PROPOSAL-LOCAL THEOREM
source-free reduction quotient         aleph_0, apparatus algebra

full-joint sector preservation          NOT ADOPTED
self-adjointness class filter           NOT ADOPTED
involutivity class filter               NOT ADOPTED
ready-reduced centrality                NOT ADOPTED

kernel source and selector              UNRESOLVED
source-selected physical image          UNRESOLVED
physical outcome IDs                    UNRESOLVED
public IDs, layers, and gates            UNRESOLVED
sampling, history, and writeback         UNRESOLVED
physical completeness                   UNRESOLVED
READY-FOR-CLASSIFICATION                NO
physical NONUNIQUE(aleph_0)             NOT EARNED

A11                                     PARTIAL / O-STOP
QDD-PHYSICAL-EFFECT-SELECTION           O / STOP
QUADRATIC-DECODER-DATA                 O / STOP, unchanged
formal scientific run                  NONE.
```

No public theorem, derived dictionary, physical uniqueness, physical
nonuniqueness, Canon claim, registry row, dependency, gate, probe, verifier,
evidence, or status move is produced by this owner ruling.

## 12. Next allowed actions

1. Freeze an exact kernel source carrier and equality.
2. Freeze a source-to-coupling relation
   `PhysReal subset KernelSource x Cpl_Q2_rev_comm`.
3. Prove totality and classify the exact source-selected image without
   changing the source-free apparatus package.
4. Create public physical outcome, instrument, effect, Born, and MatterData
   identifiers only through a later normative action.
5. Assign every object and map an exact layer and every cross-layer map a
   public gate.
6. Choose and type sampling, history-update, and writeback variants.
7. Complete dependency closure and the strict completion-contract bindings
   before opening a physical classification.

No formal probe or Canon fold is authorized by this ruling.
