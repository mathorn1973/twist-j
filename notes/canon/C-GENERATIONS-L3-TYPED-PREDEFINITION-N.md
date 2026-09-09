# C-GENERATIONS-L3-TYPED-PREDEFINITION-N: typed L2-to-L3 generation-count predefinition (NON-CANONICAL)

```text
NOTE STATE:              DRAFT / NON-CANONICAL
DEFINITION DISPOSITION:  STOP-PREDEFINITION / LOCAL AUDIT ONLY
SCIENTIFIC STATUS:       UNCHANGED
SCIENTIFIC RUN:          NONE
FORMAL PROBE:            NONE
PREREGISTRATION:         NONE
COORDINATION LOCK:       issue #685
OWNER ROW:               GENERATIONS-L3 [O]
THIS NOTE ACTION LAYER:  NOT_APPLICABLE
TARGET GATE ENDPOINTS:   L2 -> L3
TARGET GATE:             GATE-L2-L3-GENERATIONS / OPEN_LIFT
CANON CHANGE:            NONE
REGISTRY CHANGE:         NONE
STATUS MOVE:             NONE
```

Public work-object lock: [issue #685](https://github.com/mathorn1973/twist-j/issues/685).

This note is a definition-only audit for the registered
`GENERATIONS-L3 [O]` frontier. It does not choose a generation carrier, run a
classification, derive a generation count, or authorize a verifier. It
turns the current prose question into an exact list of types and decisions
that must be public before a formal probe can exist.

The present local definition disposition is `STOP-PREDEFINITION`. It is
neither a Canon status nor a scientific result. Public v72 supplies a gate
and a comparison with three, but it does not supply the source, target, lift
class, generation object, or count functional to which that comparison could
be applied.

## 1. Authority, collision, and routing pin

```text
Canon:                    Public Canon v72
state:                    ACTIVE
authority:                mathorn1973/twist-j main
lock base commit:         b7d7ba5d0b9f42c3ac30eda4e70e19e1494eed23
audit/main commit:        43cfd9e4ca570a51f9aa548a8b0e61dad45f5b7f
tag:                      canon-v72
content commit:           aac8a3a4aff027beb2b08edbde1ae8e59224914c
Canon SHA-256:            39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70
Canon bytes:              374406
owner:                    GENERATIONS-L3 [O]
scheduler:                NONABELIAN_QCD / ROOT / READY / FORMAL
normative layer:          L3
gate:                     GATE-L2-L3-GENERATIONS
gate kind:                OPEN_LIFT
gate endpoints:           L2 -> L3
work-object issue:        #685
note branch:               notes/c-generations-l3-typed-predefinition-n
this file:                notes/canon/C-GENERATIONS-L3-TYPED-PREDEFINITION-N.md
post-lock collision:      RESOLVED / #687 CLOSED AS DUPLICATE
companion PR:             #688 MERGED / COMPATIBLE
reserved future probe:    NONE
formal pin/run/result:    ABSENT / NOT AUTHORIZED / ABSENT
```

Repin record. This note was first pinned against Public Canon v71 at audit
base `7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2`. On 2026-08-31 the owner
repinned it against Public Canon v72 at audit base
`43cfd9e4ca570a51f9aa548a8b0e61dad45f5b7f`. The v71-to-v72 delta is additive
and confined to the photon lane: four registry rows
(`FCC-WEIGHTED-SHELL-SYMBOL`,
`PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP`,
`PHOTON-CONE-CONVERGENCE`, `PHOTON-MASSLESS-PHASE`), their three gates, the
matching dependency and evidence rows, and the release-identity string in
`canon/CORE.md`. No registry row, gate, dependency, layer definition, or
scheduler label cited by this note changed between the two releases, so every
disposition below is restated at v72 with no change of content. The
coordination lock base of issue #685 stays at
`b7d7ba5d0b9f42c3ac30eda4e70e19e1494eed23`, which is history and is not
repinned. The definition disposition remains `STOP-PREDEFINITION`.

A rescan at the new audit base found no competing open issue, pull request,
branch, probe, Registry row, or path claiming the typed-predefinition scope.
Issue #685 remains the sole exact lock. Pull request #699, which carried an
unpinned draft of this lane under the relinquished `P-GENERATIONS-L3-1`
identifier, was closed terminally on 2026-08-31 without merge.

A fresh pre-lock scan on the stated lock base found no open issue, pull
request, branch, probe, Registry row, divergent-head file, or path with
`C-GENERATIONS-L3-TYPED-PREDEFINITION-N` or the same typed-predefinition
scope. Issue #685 claims exactly this note. It reserves no `P-*` identifier.

Issue #687 was opened 59 seconds after issue #685 and claims an overlapping
typed-predefinition scope plus the future identifier `P-GENERATIONS-L3-1`.
The owner retained the earlier exact lock #685 and issue #687 was closed as a
duplicate on 2026-08-30; its provisional `P-*` identifier was relinquished.
PR #688 subsequently merged as `7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2`.
A post-merge rescan confirms that it contains only the distinct working-map
intake and center-character census under `notes/`, no competing typed-
predefinition path, and no Canon, Registry, NORMATIVE, gate, or dependency
change. The coordination collision is therefore resolved.

`READY` in `canon/FRONTIER_PROGRAMS.tsv` permits scope or preregistration
work. By `canon/LEDGER.md`, it does not authorize a verifier. The missing
definition fields below produce the local `STOP-PREDEFINITION` disposition
despite that scheduler label.

## 2. Exact inherited public surface

The complete registered surface specific to this owner is:

```text
REGISTRY
  id:        GENERATIONS-L3
  status:    O
  scope:     the generation structure at the standard model L3 frontier
  decision:  closes positively by deriving the generation count at the L3
             boundary layer; closes negatively if the derived count differs
             from three

NORMATIVE
  item_id:   GENERATIONS-L3
  kind:      OBLIGATION
  status:    O
  layer:     L3
  gate_ids:  GATE-L2-L3-GENERATIONS

GATE
  id:        GATE-L2-L3-GENERATIONS
  owner_item_id:
             GENERATIONS-L3
  from:      L2
  to:        L3
  kind:      OPEN_LIFT

DEPENDENCY FLOOR
  GENERATIONS-L3 -> DEF-ARCHITECTURE

EVIDENCE
  INLINE_CANON only
```

Public v72 defines the layer names as `L1 state`, `L2 manifold`, `L3
boundary`, `L4 support`, `L5 stream`, and `L6 measure`. It does not thereby
define a particular object at any layer. The complete dependency closure of
`GENERATIONS-L3` contains no concrete L2 carrier. `DEF-ARCHITECTURE` supplies
the declared state architecture and typed partial decoder, not a generation
lift:

```text
Omega = N_0 x F_5^6,
U     : Omega -> Omega,
D     : a typed partial interface on registered domains.
```

The Canon explicitly does not claim totality, uniqueness, or completeness of
`D`. No unspecified decoder field may be used to fill a slot below.

## 3. Scope mismatch that must be resolved

The owner scope names `generation structure`, while the gate decision tests
only an integer `generation count`. These are not equivalent questions.
Two inequivalent L3 boundary structures can have the same count. Conversely,
one mathematical multiplicity does not by itself prove the physical reading
of those blocks as Standard-Model generations.

Before a formal probe, an owner-reviewed definition fold must choose exactly
one of the following scopes:

```text
COUNT-ONLY
  classify every admissible lift far enough to prove that its generation
  multiplicity is a well-defined integer; compare only that integer.

FULL-STRUCTURE
  classify the complete L3 generation object under a frozen output
  equivalence, including every structure field that can differ while the
  count stays fixed.
```

This note prepares the narrower `COUNT-ONLY` contract because that is the
only target described by the current gate. It does not silently narrow the
Registry scope. Until a Canon proposal resolves the mismatch, the public
owner remains open and no formal probe is authorized.

The tuple below implements `COUNT-ONLY` only. If the owner retains
`FULL-STRUCTURE`, this draft remains `STOP-PREDEFINITION` and must be replaced
or extended by a separately reviewed contract with an exact full-output
carrier, `OutputEq`, structure invariants, compatibility rules, and
structure-level outcomes. Selecting `FULL-STRUCTURE` does not activate an
unimplemented branch of this tuple.

## 4. Complete definition object

A valid owner definition must publish two dataflow-separated tuples

```text
S_classify = (
  classification_authority_pin,

  SourceUniverse, SourceClass, SourceEq,
  Cat2, X2, Eq2, G2, rho2, Struct2,
  source_transport,
  source_owner, source_context, source_nonempty,
  source_disposition, source_selection_or_adoption, source_completeness,

  TargetUniverse, TargetClass, TargetEq,
  Cat3, Y3, Eq3, G3, rho3, Boundary3,
  BoundaryOut, BoundarySigma, eq3_output_action,
  target_transport, output_transport,
  BoundaryEq, BoundaryQuotient, output_transport_coherence,
  boundary_owner, boundary_context,
  target_nonempty,
  target_disposition, target_selection_or_adoption, target_completeness,

  GenSchemaUniverse, GenSchemaClass, SchemaEq,
  GenSchemaSource, GenSchemaVersion, GenSchemaStatus,
  GenSchemaDisposition, GenSchemaSelectionOrAdoption,
  GenSchemaNonempty, GenSchemaCompleteness,
  GenSchema, GenEq, gen_transport, generation_block,

  LiftTagSet, lift_tag_nonempty,
  LiftIndex, LiftUniverse, LiftType, LiftSigma, profile_projection,
  lift_domain, lift_codomain, lift_totality, action_compatibility,
  lift_disposition, lift_selection_or_adoption,
  substantive_key_space, substantive_nonempty,
  auxiliary_key_space, auxiliary_nonempty,
  key_partition_proof, overlap_rule,

  StructuralExclusion,
  boundary_eval, SchemaCheck, residual_rule, StructuralCheck,

  Adm, A, LiftEq,
  profile_scope, profile_completeness,

  boundary_output, MultiplicityObject, GenDecomp, multiplicity,
  raw_count,
  N_gen, count_domain, count_invariance, count_uniformity,

  classification_definition_order, classification_dependency_DAG,
  deterministic_order,
  classification_mode, symbolic_proof_mode, classifier, completeness_proof,
  PhaseAArtifactSchema, PhaseAValidityCertificateSchema,
  PhaseAArtifactChecker, PhaseAArtifactCheckerTotality,

  comparison_firewall
).

S_compare = (
  gate_id,
  comparison_target,
  validity_first_routing,
  comparator, comparator_totality,
  comparison_definition_order,
  comparison_dependency_DAG,
  PhaseBComparisonCertificateSchema,
  PhaseBComparisonChecker, PhaseBComparisonCheckerTotality
).

S_gen = (S_classify, S_compare).
```

`classification_authority_pin` binds the repository, base commit, Canon tag,
Canon content hash, owner, gate identifier and endpoints, and the exact
version of every classification source. `S_classify` has a
comparison-target-free dependency closure. It contains no comparison value,
gate decision text, or comparator rule. `S_compare` alone contains the public
integer comparison target and routing. The immutable Phase A artifact binds
to the complete `S_classify` hash before `S_compare` is evaluated.

Every slot must contain an exact public value or definition, a resolvable
public identifier, or the literal value `UNRESOLVED`. A prose synonym,
private notebook, implicit convention, post-result selection, or bare null
is invalid. `NOT_APPLICABLE` is allowed only where the controlling schema
explicitly permits it and a public basis for non-applicability is supplied.

The current disposition of the tuple is:

| Block | Required content | Public v72 disposition |
| --- | --- | --- |
| authority | owner, layer endpoints, gate, dependency floor | `FROZEN` |
| L2 source | nonempty source universe and equality, complete admitted class, category, carrier, action, structure, transports, owner, context and selection, adoption, or completeness rule | `UNRESOLVED` |
| L3 target | nonempty target universe and equality, complete admitted class, category, boundary carrier, dependent output family and quotient, action, structure, transports, owner, context and selection, adoption, or completeness rule | `UNRESOLVED` |
| generation schema | exact universe, class, equality, source, version, dictionary status, selection or adoption rule, nonemptiness, one complete block per admitted schema, transports, intrinsic occurrences, multiplicity and residual rules | `UNRESOLVED` |
| lift | complete dependent lift universe, nonempty tag and key domains, exact tagged mathematical kinds, codomains, map or functor, totality and action compatibility | `UNRESOLVED` |
| admissible class | comparison-target-independent predicate, complete class, context and overlap rules | `UNRESOLVED` |
| equivalence | all and only allowed identifications of lifts and outputs | `UNRESOLVED` |
| output and count | typed per-tag boundary output, decomposition, raw multiplicity, auxiliary-key uniformity, substantive-key classification, and well-defined descent to an integer functional | `UNRESOLVED` |
| dependencies | complete separated public acyclic graphs and acyclic union, including every actual cross-layer input | `UNRESOLVED` |
| completeness | terminating classifier or symbolic theorem, certificates and exact checker | `UNRESOLVED` |
| routing | diagnostic outcomes and present gate routing | `PARTLY FROZEN` |

No block marked `UNRESOLVED` may be filled by the observed number of fermion
families or by another occurrence of the integer three.

## 5. L2 source profile

The symbol `X2` is a metavariable, not a historical object name. A submitted
profile must first freeze the universe relative to which its source claim is
complete:

```text
SourceUniverse    the exact universe of eligible L2 source objects
SourceClass       the nonempty complete comparison-target-independent or
                  owner-adopted subclass in scope
SourceEq          object-level equality or equivalence on SourceClass
source_disposition
                  GLOBAL-CLASS, FORCED-SELECTION, OWNER-ADOPTED, or
                  ANSATZ-ONLY
source_selection_or_adoption
                  an exact comparison-target-independent selection theorem
                  or a
                  reviewed pre-result Canon architecture adoption
source_completeness
                  a theorem proving that the class is exhaustive, that the
                  selected X2 is forced up to SourceEq, or that the claim is
                  exactly scoped to a reviewed owner-adopted architecture
```

For each admitted source, it must then specify all of:

```text
Cat2             one exact category, or exact indexed category Cat2(x), for
                 every x in SourceClass
X2               a total assignment x |-> X2(x) in Ob(Cat2(x)); each value
                 has one public carrier identifier
Eq2              literal equality or declared gauge equivalence on each X2(x)
G2               the exact acting group, groupoid, algebra, or monoid G2(x)
rho2             each action rho2(x) and its domain and codomain
Struct2          every preserved structure on X2(x) used by Adm or a lift
source_transport exact transport of Eq2, actions, structures, and context
                 across SourceEq-equivalent objects
source_owner     the resolvable Canon definition, NORMATIVE.item_id, or
                 registered claim_id that publicly owns X2
source_context   basis, orientation, placement, scale, boundary and labels
source_nonempty  proof that SourceClass and every admitted source domain
                 required by totality are nonempty
```

Calling a carrier an `L2 manifold` is not enough. Dimension, coefficient
ring, topology, smoothness, metric, bundle data, boundary conditions,
orientation, connectedness, labels, base points, and allowed automorphisms
must each be fixed or explicitly inapplicable.

If the source is only a restricted subcarrier, the restriction predicate
must be fixed before any count is read. The future conclusion is then
conditional on that restricted source. It cannot be promoted to the full
public architecture without a separate completeness theorem.

There are four honest source dispositions:

```text
GLOBAL-CLASS
  SourceClass equals SourceUniverse, or is one exact small skeleton or
  exhaustive representative class for SourceUniverse modulo SourceEq, and
  every represented object is covered by the later classification;

FORCED-SELECTION
  a comparison-target-independent theorem proves that one X2 is selected up
  to
  SourceEq from the complete SourceClass;

OWNER-ADOPTED
  a reviewed Canon definition adopts one X2 or one exact SourceClass as
  architecture before any output is read, and the owner scope, dependencies,
  and gate contract are explicitly restricted to that adoption;

ANSATZ-ONLY
  one X2 is proposed without a complete selection theorem; every later
  result is conditional on that ansatz and cannot close GENERATIONS-L3.
```

Publishing one well-typed source does not by itself make the program-level
class complete.

## 6. L3 boundary and one-generation profile

The symbol `Y3` is also a metavariable. The target side must first freeze:

```text
TargetUniverse    the exact universe of eligible L3 boundary objects
TargetClass       the nonempty complete comparison-target-independent or
                  owner-adopted subclass in scope
TargetEq          object-level equality or equivalence on TargetClass
target_disposition
                  GLOBAL-CLASS, FORCED-SELECTION, OWNER-ADOPTED, or
                  ANSATZ-ONLY
target_selection_or_adoption
                  an exact comparison-target-independent selection theorem
                  or a
                  reviewed pre-result Canon architecture adoption
target_completeness
                  a theorem proving that the class is exhaustive, that the
                  selected Y3 is forced up to TargetEq, or that the claim is
                  exactly scoped to a reviewed owner-adopted architecture
```

For each admitted target, a submitted profile must specify:

```text
Cat3              one exact target category, or exact indexed category
                  Cat3(y), for every y in TargetClass
Y3                a total assignment y |-> Y3(y) in Ob(Cat3(y)); each value
                  has one public L3 boundary carrier identifier
Eq3               literal equality or declared gauge equivalence on each Y3(y)
G3                the exact boundary action object G3(y)
rho3              each action rho3(y) on Y3(y)
Boundary3         each boundary construction and all orientation conventions
BoundaryOut       a total dependent assignment y |-> BoundaryOut(y) of the
                  actual set-coded L3 output objects carried by Y3(y)
BoundarySigma     the disjoint union of BoundaryOut(y) over y in TargetClass
eq3_output_action the exact induced action or equivalence of Eq3(y) on
                  BoundaryOut(y), for every y
target_transport  exact transport of Eq3, actions, structures, and context
                  across TargetEq-equivalent objects
output_transport  for every y TargetEq y', an explicitly listed equivalence
                  between
                  BoundaryOut(y) and BoundaryOut(y') preserving actions,
                  Boundary3, GenSchema data, and context; these explicitly
                  listed pre-quotient maps are generators, not maps defined
                  from BoundaryEq
BoundaryEq        the exact least equivalence on BoundarySigma generated by
                  eq3_output_action inside each fiber and the explicitly
                  listed pre-quotient output_transport maps
BoundaryQuotient  BoundarySigma / BoundaryEq, or one exact small normal-form
                  presentation of that quotient
output_transport_coherence
                  a post-BoundaryEq proof that identity, inverse, and
                  composition laws hold and that the generators descend to
                  well-defined quotient transports
boundary_owner    the resolvable Canon definition, NORMATIVE.item_id, or
                  registered claim_id that owns the target
boundary_context  coefficient ring, basis, labels, placement and scale
target_nonempty   proof that TargetClass, each required Y3(y), and every
                  target domain required by boundary_eval are nonempty
```

`TargetClass` therefore indexes target profiles; it is not itself the output
codomain of a lift. Actual outputs live in the dependent fibers
`BoundaryOut(y)`. No checker or decomposition may replace such an output by
the bare profile identifier `y`.

The generation schema is itself a target-side selection and must be frozen
before any candidate output is evaluated:

```text
GenSchemaUniverse     the exact admitted universe of one-generation schemas
GenSchemaClass        the nonempty complete comparison-target-independent or
                      owner-adopted subclass in scope
SchemaEq              the exact object-level equivalence on GenSchemaClass
GenSchemaSource(s)    a public Canon, NORMATIVE, Registry, or exact inline
                      definition source for every s in GenSchemaClass
GenSchemaVersion(s)   immutable version or content hash
GenSchemaStatus(s)    exactly one of MATHEMATICAL-SCHEMA,
                      OWNER-ADOPTED-DICTIONARY, or
                      REGISTERED-PHYSICAL-DICTIONARY
GenSchemaDisposition  GLOBAL-CLASS, FORCED-SELECTION, OWNER-ADOPTED, or
                      ANSATZ-ONLY
GenSchemaSelectionOrAdoption
                      comparison-target-independent theorem or reviewed
                      pre-result owner adoption; otherwise an exact ansatz
                      declaration
GenSchemaNonempty     proof that the universe, GenSchemaClass, and every
                      selected schema domain required by GenSchema are
                      nonempty
GenSchemaCompleteness completeness relative to the claimed Standard-Model
                      scope
GenSchema(s)          the exact one-generation definition for schema s
GenEq(s)              equality of generation blocks for schema s
gen_transport         coherence of GenSchema, GenEq, and block data under
                      SchemaEq, Eq3, BoundaryEq, TargetEq, and output
                      transports
```

The status enum applies pointwise to every admitted `s` and has a conclusion
ceiling. `MATHEMATICAL-SCHEMA` permits only a mathematical block-multiplicity
statement. `OWNER-ADOPTED-DICTIONARY`
permits an architecture-relative dictionary statement, not an independently
derived physical identification. `REGISTERED-PHYSICAL-DICTIONARY` permits
physical wording only up to the status and evidence ceiling of the exact
registered dictionary source. A mixed-status class is reported at its weakest
applicable ceiling unless results are partitioned by schema. No status is
inferred from a successful count.

`GLOBAL-CLASS` here has the same exhaustive meaning as for source and target:
`GenSchemaClass` equals `GenSchemaUniverse`, or is an exact small skeleton or
exhaustive representative class modulo `SchemaEq`. `FORCED-SELECTION` and
`OWNER-ADOPTED` may instead select one schema or one exact class before
outputs. `ANSATZ-ONLY` cannot close the public owner.

Each `GenSchema(s)` must define one generation without referring to the
number of generations. At minimum it must decide:

1. the exact representation or module content of one block;
2. chirality conventions;
3. whether antiparticles are separate fields, conjugate data, or already
   included in the block;
4. whether a right-handed neutrino is present;
5. how color multiplicity and weak-doublet components are represented;
6. which charges, gradings, orientations, and real structures are part of
   block equality;
7. whether zero modes, degeneracies, or repeated eigenvalues count as
   distinct occurrences;
8. the allowed exotic or residual sector and whether a nonzero residual
   invalidates the generation count;
9. the exact Standard-Model gauge group, including any global quotient;
10. the hypercharge normalization and charge-conjugation convention;
11. whether Higgs and gauge fields are excluded, shared across copies, or
    included in a generation block;
12. whether Yukawa and mixing data belong to block identity, output
    structure, or neither;
13. the anomaly constraints and the coefficient ring in which they are
    checked;
14. an exact checker for one block and for a complete block decomposition.

The dependent rule `generation_block(s,...)` must return intrinsically
distinct subobjects or occurrences relative to `GenSchema(s)`. Labels may
certify distinct idempotents, summands, subquotients, support components, or
other frozen intrinsic data; they may not create multiplicity merely by
duplicating names or input indices. Counting only isomorphism classes would
collapse several identical copies to one and is therefore not a multiplicity
rule. Conversely, copying the same subobject under several labels is label
inflation and must be rejected. The owner must freeze an exact decomposition
or multiplicity object that preserves genuine copies, is invariant under
`Eq3`, `BoundaryEq`, and `SchemaEq`, and is unchanged when auxiliary names are
forgotten.

For each admitted boundary output `B`, a typical allowed shape is

```text
B  Eq3  GenBlock_1 direct_sum ... direct_sum GenBlock_n direct_sum Residual,
```

but direct sum is not assumed by this note. The owner may choose a different
exact composition law only before the future classification and with a proof
that the resulting multiplicity is well defined. The definition of the
composition law may not mention the comparison value three.

As on the source side, one selected `Y3` can support a program-level result
through either a comparison-target-independent selection theorem from the
complete `TargetClass` or a reviewed pre-result `OWNER-ADOPTED` Canon
architecture whose scope and dependencies are explicit. Otherwise the result
is `ANSATZ-ONLY` and conditional.

On the target side `GLOBAL-CLASS` likewise means that `TargetClass` equals
`TargetUniverse`, or is one exact small skeleton or exhaustive representative
class for it modulo `TargetEq`; it never means merely exhaustive treatment of
an arbitrarily narrowed subclass.

## 7. Lift type and complete admissible class

The phrase `lift from L2 to L3` does not determine a mathematical type. The
owner must freeze an exact `LiftUniverse`. It may contain one mathematical
type or an explicit tagged disjoint union of several types, for example maps,
bundle morphisms, boundary functors, or representation lifts. An implicit
mixture of types is forbidden. Every tag must have its own equality,
totality, action law, and comparison rule, including rules for whether two
different tags can ever be equivalent.

`SourceClass`, `TargetClass`, `GenSchemaClass`, `BoundarySigma`, every key
class, and the lift class must be set-coded or essentially small with one
exact small skeleton. Otherwise the quotient, image, cardinality tests, and
certificates below are undefined.

For the frozen universe, define

```text
LiftIndex = {
  (x,y,s,k,tau) :
  x in SourceClass,
  y in TargetClass,
  s in GenSchemaClass,
  tau in LiftTagSet,
  k in K_sub(x,y,s,tau), the product of all frozen substantive profile-key
       domains for this source, target, schema, and tag
}.

LiftSigma = disjoint_union over (x,y,s,k,tau) in LiftIndex of
            Lift_tau(x,y,s,k).
```

A substantive key is a physical, source, target, boundary, placement, or
schema alternative that can change output. The schema identifier `s` and the
complete product `K_sub(x,y,s,tau)` are part of `LiftIndex` and therefore
remain visible in `A/LiftEq` and `C`. An auxiliary key is only a basis, gauge,
chart, certificate, or equivalent presentation over which one lift must be
uniform. This partition is frozen before outputs. A lift-dependent omission
of an inconvenient key is forbidden.

Freeze

```text
LiftIndex        the exact dependent profile index above
LiftTagSet       the exact nonempty set of admitted mathematical type tags
lift_tag_nonempty
                 a proof that LiftTagSet is nonempty; an empty scientific
                 lift result must come from empty lift fibers or Adm, not
                 from declaring no lift type
LiftUniverse     the exact tagged family Lift_tau(x,y,s,k)
LiftType         the literal type tag tau of each admitted object
LiftSigma        the exact disjoint union of all tagged lift objects
profile_projection
                 the canonical map ell |-> (x,y,s,k,tau) from LiftSigma to
                 LiftIndex
lift_domain      every mandatory source and auxiliary-key domain for each
                 tag and profile index
lift_codomain    the complete target domain for each tag and profile index
lift_totality    the exact totality predicate on every mandatory key
action_compatibility
                 the intertwining, covariance, or preservation law
lift_disposition GLOBAL-CLASS, FORCED-SELECTION, OWNER-ADOPTED, or
                 ANSATZ-ONLY
lift_selection_or_adoption
                 the comparison-target-independent theorem or reviewed
                 pre-result Canon adoption that fixes the admitted lift scope
substantive_key_space
                 the complete product K_sub promoted into LiftIndex
substantive_nonempty
                 a proof that every required K_sub is nonempty, using one
                 declared UNIT key when there is no substantive choice
auxiliary_key_space
                 the complete pre-output auxiliary-key set K_aux for each
                 profile
auxiliary_nonempty
                 a proof that every K_aux is nonempty, using one declared
                 trivial key where no presentation choice is needed
key_partition_proof
                 a proof that every mandatory key is classified exactly once
                 as substantive or auxiliary
overlap_rule     agreement required on intersecting contexts
StructuralExclusion
                 the exact set-coded tagged universe of count-free exclusion
                 reasons, with no numeric or comparison payload
boundary_eval    the total per-tag structural evaluator on every candidate
                 and mandatory auxiliary key, with a typed output or exact
                 StructuralExclusion reason
SchemaCheck      the dependent family of exact count-free maps
                 SchemaCheck_s on BoundaryQuotient for every s in
                 GenSchemaClass
residual_rule    the dependent family of exact count-free maps
                 residual_rule_s on BoundaryQuotient for every s
StructuralCheck  the total dependent family StructuralCheck_s obtained from
                 SchemaCheck_s and residual_rule_s
Adm_tau(ell)     all pre-comparison admissibility predicates for each tag;
                 these may use boundary_eval, typed boundary structure,
                 StructuralCheck, and the residual rule, but not GenDecomp,
                 multiplicity, or any count
A                { ell in LiftSigma : Adm_tau(ell) }
LiftEq            the equivalence relation on A
profile_scope     the exact admitted LiftIndex and LiftSigma scope
profile_completeness
                 a theorem that membership in A is exhaustively decided for
                 every object of LiftSigma, plus a theorem or reviewed Canon
                 adoption that fixes the scope claimed by the owner
```

`profile_completeness` does not assert that `A` is nonempty. A proved empty
`A` remains available for the later `EMPTY` route after every validity
obligation passes.

`LiftEq` must list separately every permitted basis change, gauge action,
global conjugation, source automorphism, boundary automorphism, relabeling,
orientation reversal, scale, Galois action, central quotient, and placement
change, plus every allowed schema change. An item not listed is not an
equivalence. A schema change is allowed only through `SchemaEq` and its frozen
transport; non-`SchemaEq` schemas remain distinct in `Q`. Every allowed
equivalence must preserve the predeclared source, target, output, and
generation-schema structures. `LiftEq` may use the frozen structural
equalities and transports; it may not be defined from a raw count, `N_gen`,
`C`, or the comparator.

State-dependent gauge, unrestricted lookup tables, one-orbit maps, constant
maps, zero maps, post-result basis choices, and comparison-fitted filters are
not automatically admissible. They must either be excluded by exact
predicates or included honestly and classified. Excluding a degeneracy after
seeing its count is forbidden.

One displayed lift, even one with an exact count, proves only existence in a
restricted ansatz. It cannot decide `GENERATIONS-L3` unless a symbolic proof
or complete census exhausts `A` relative to the independently frozen
admitted scope, and either a comparison-target-independent theorem or a
reviewed pre-result Canon adoption establishes that exact scope for the owner
row.
Completeness relative to a singleton `Adm` chosen only in a probe is not
program-level completeness.

## 8. Generation-count functional

For every profile index and type tag, first freeze a total structural
evaluator, selected without any count:

```text
boundary_eval_tau :
  { (ell,i) : profile_projection(ell)=(x,y,s,k,tau),
              i in K_aux(profile_projection(ell)) }
  -> BoundaryOut(y) disjoint_union StructuralExclusion.
```

`StructuralExclusion` is an exact comparison-target-independent reason
schema. It cannot encode a count, the comparison target, or failure to obtain
a desired value.
Before `Adm` is evaluated, also freeze

```text
SchemaCheck_s : BoundaryQuotient
                -> SCHEMA-VALID disjoint_union StructuralExclusion,

residual_rule_s : BoundaryQuotient
                  -> RESIDUAL-ALLOWED disjoint_union StructuralExclusion,

StructuralCheck_s([b]) = STRUCTURALLY_ADMISSIBLE
  exactly when SchemaCheck_s([b]) = SCHEMA-VALID and
               residual_rule_s([b]) = RESIDUAL-ALLOWED;
  otherwise it returns the exact tagged StructuralExclusion reason.
```

This checker uses only the one-generation schema's typing constraints and
the residual-sector rule. It may detect a forbidden residual, but it may not
decompose into a multiplicity object, count blocks, or read any later value.
All three dependent map families are total and invariant under `BoundaryEq`
and `SchemaEq` by construction or proof. `Adm_tau(ell)` at profile schema `s`
requires every mandatory evaluation at target profile `y` to land in
`BoundaryOut(y)`, all corresponding `StructuralCheck_s` values to return
`STRUCTURALLY_ADMISSIBLE`, and every other predeclared structural predicate
to hold. The restriction to `A` is the total typed output map

```text
boundary_output_tau = boundary_eval_tau restricted to
  { (ell,i) : profile_projection(ell)=(x,y,s,k,tau), ell in A,
              i in K_aux(profile_projection(ell)) },
with boundary_output_tau(ell,i) in BoundaryOut(y).
```

Every output lies in the fiber over the exact target profile named by
`profile_projection(ell)`. `output_transport` and `BoundaryEq` control
comparison across `TargetEq`-equivalent profiles; a bare target-profile
identifier is never an output. The evaluator may not be a free table. Then
freeze one exact decomposition chain

```text
MultiplicityObject(s)
            the exact set-coded multiplicity-witness type for schema s,

GenDecomp_s : dom(GenDecomp_s) subset BoundaryQuotient
              -> MultiplicityObject(s),

multiplicity_s : MultiplicityObject(s) -> N_0.
```

The dependent families `MultiplicityObject`, `GenDecomp`, and `multiplicity`
must be total on every admitted boundary-output class, coherent with
`BoundaryEq`, `Eq3`, `TargetEq`, `SchemaEq`, `GenEq`, and all transports,
independent of every allowed decomposition choice, and subject to the
intrinsic-label firewall of section 6. Each `MultiplicityObject(s)` must be
set-coded or supplied with one exact small normal-form class. The only raw
instance count is the composite

```text
m_raw(ell,i) = multiplicity_s(
  GenDecomp_s([boundary_output_tau(ell,i)]_BoundaryEq)
), where profile_projection(ell)=(x,y,s,k,tau).
```

The residual rule is evaluated by `StructuralCheck` before multiplicity. A
forbidden residual or a well-defined non-generation output gives an exact
exclusion certificate under `Adm_tau`; if every lift is excluded in a
complete valid scope, the later result may be `EMPTY`. An undefined
evaluation, ambiguous structural check or decomposition, unresolved residual
rule, or missing exclusion proof gives `STOP-PREDEFINITION`, not an empty
class or a numerical count.

For the complete nonempty pre-output auxiliary-key set, prove

```text
count_uniformity:
m_raw(ell,i) = m_raw(ell,j)
for every ell in A and every mandatory auxiliary i,j.
```

By auxiliary nonemptiness and uniformity, define `raw_count(ell)` as the
unique integer equal to `m_raw(ell,i)` for every mandatory auxiliary key
`i`. Substantive alternatives are not part of this uniformity condition:
they already label separate objects in `LiftIndex`, so distinct values remain
visible to the classification. If a key can change physical output, treating
it as auxiliary is a type error.

Next prove descent:

```text
count_invariance:
ell LiftEq ell'  implies  raw_count(ell) = raw_count(ell').
```

If `LiftEq` identifies objects with different auxiliary-key sets, it must
supply an exact transport preserving `boundary_output`, decomposition, and
every raw count. Without that proof the count does not descend.

Only after quotient existence and the descent proof, define

```text
Q = A / LiftEq,
N_gen : Q -> N_0,
N_gen([ell]) = raw_count(ell).
```

The quotient must be set-coded or represented by an exact small normal-form
class. `N_gen` must count intrinsic generation-block multiplicity, not block
names, species, colors, weak components, eigenvalue labels, or isomorphism
types. The exact `count_domain` declaration is
`dom(raw_count)=A`, `dom(N_gen)=Q`, with codomain `N_0` for both.

For every `Q`, including the empty quotient, define

```text
C = image(N_gen) = { N_gen(q) : q in Q } subset N_0.
```

Thus `C` is empty exactly when `Q` is empty. `C` is read only from the frozen
class. It is never supplied to the builder, classifier, normalizer,
equivalence reducer, or stopping rule.

## 9. Validity-first diagnostic outcomes

Outcome routing is ordered. Phase A first emits an immutable artifact
conforming to `PhaseAArtifactSchema`. The frozen `PhaseAArtifactChecker`
either rejects it or emits a new proof object conforming to
`PhaseAValidityCertificateSchema`:

```text
PhaseAValidityCertificate:
  binds the Phase A artifact hash and S_classify hash;
  every type, equality, nonemptiness, totality, invariant, dependency,
  universe, selection or adoption, profile-completeness,
  classification-completeness, exactness, termination, soundness, and
  underlying Phase A obligation has a checkable witness.
```

The validity certificate is checker output, not a field that certifies
itself. If the Phase A artifact is absent, incomplete, nonterminating, or
rejected, return `STOP-INTEGRITY` without using `Q` or `C` as a scientific
gate result. Only after the checker emits a valid certificate may the
remaining rows be evaluated. Every routed row also requires an accepted
`PhaseBComparisonCertificate`; otherwise its route is `STOP-INTEGRITY`.
This runtime diagnostic is distinct from the local definition disposition
`STOP-PREDEFINITION`.

The currently inherited comparison fields are

```text
gate_id             GATE-L2-L3-GENERATIONS
comparison_target   3
comparator(n)        PASS-COUNT when n = comparison_target;
                     FAIL-NONTHREE when n != comparison_target
comparator_totality  decidable integer equality proves termination and one
                     exact comparator output for every n in N_0
validity_first_routing
                     integrity check, then EMPTY or NONUNIQUE diagnostics,
                     then the comparator on one universally forced count
```

The diagnostic routing is proposed here but is not yet part of the public
gate. The exact conditions are:

| Outcome | Exact condition | Scientific meaning | Current gate routing |
| --- | --- | --- | --- |
| `STOP-INTEGRITY` | Phase A is absent, incomplete, nonterminating, or rejected; or Phase B fails, does not terminate, or its certificate is rejected | no certified gate result exists | gate remains open |
| `EMPTY` | validity verifies, an exact proof establishes `Q` empty, and the Phase B routing certificate verifies | no admissible lift exists in the frozen complete class | gate remains open under this proposed contract |
| `PASS-COUNT` | validity verifies, one `q in Q` witnesses nonemptiness, an exact universal proof gives `N_gen(q')=3` for every `q' in Q`, and the comparison certificate verifies | every admissible lift has count three | eligible for the present positive route |
| `FAIL-NONTHREE` | validity verifies, an exact integer `n!=3` and one nonempty witness exist, a universal proof gives `N_gen(q')=n` for every `q' in Q`, and the comparison certificate verifies | one non-three count is forced by the complete class | eligible for the present negative route |
| `NONUNIQUE-COUNT` | validity verifies, two exact witnesses in `Q` have unequal counts or an equivalent exact theorem supplies both values, and the Phase B routing certificate verifies | the frozen architecture does not determine one count | gate remains open under this proposed contract |

Under this priority rule the conditions are mutually exclusive. A raw empty
enumerator output without a validity certificate is still
`STOP-INTEGRITY`. Failure to find a lift is `STOP-INTEGRITY`. Failure of one
candidate is `STOP-INTEGRITY`, not `FAIL-NONTHREE`. A malformed or
inconsistent definition gives `STOP-INTEGRITY`, not `EMPTY`.

Several inequivalent lifts may all have count three. That is `PASS-COUNT`
for the count-only question, but it is not uniqueness of the lift or of the
full boundary structure. If the owner retains the wider `generation
structure` scope, an additional output equivalence and full-structure
classification are mandatory.

The present public gate routes one derived count positively or negatively.
It has no explicit `EMPTY`, class-level `NONUNIQUE-COUNT`, or validity-first
`STOP-INTEGRITY` clause. This note does not rewrite that gate and does not
claim that the current text forbids a separately adopted scoped architecture.
If the owner accepts this class-level contract, a separate definition-only
Canon clarification must resolve these routes before its formal probe is
created.

## 10. Comparison-target leakage firewall

`comparison_firewall` is the enforceable no-read contract formed by the
prohibitions below, the frozen dependency manifest, and the Phase A/Phase B
artifact boundary. Its checker must reject any undeclared input or dependency
edge. The integer three may enter only the final comparator for the
already-public gate. It may not choose or modify:

1. `SourceUniverse`, `SourceClass`, `SourceEq`, a source selector or adoption,
   `Cat2`,
   `X2`, its dimension, topology, cutoff, basis, orientation, subgroup,
   placement, normalization, restriction, or source-instance rule;
2. `TargetUniverse`, `TargetClass`, `TargetEq`, a target selector or adoption,
   `Cat3`, `Y3`, `BoundaryOut`, `eq3_output_action`, `BoundaryEq`,
   `output_transport`, or `output_transport_coherence`, including any rank,
   block structure, label, boundary condition, action, equivalence, or
   residual rule;
3. `GenSchemaUniverse`, `GenSchemaClass`, `SchemaEq`,
   `GenSchemaDisposition`, `GenSchemaSelectionOrAdoption`, `GenSchema`,
   `GenEq`, or any one-generation convention;
4. `LiftIndex`, `LiftUniverse`, `LiftType`, a lift selector or adoption,
   `Adm`, `A`, `LiftEq`, the profile scope, the auxiliary/substantive key
   partition, or an overlap rule;
5. the intrinsic decomposition, multiplicity rule, or `N_gen`;
6. the classifier order, search bound, pruning rule, normal form, or stopping
   criterion; or
7. a choice among completed branches after their counts are visible.

`classification_definition_order` is the exact first partial order below.
Together with the complete `classification_dependency_DAG`, it must be
acyclic:

```text
source/target/schema universes, equalities, selections or adoptions
  -> LiftIndex and LiftUniverse
  -> boundary_eval, SchemaCheck, residual_rule, and StructuralCheck
  -> Adm, A, and LiftEq
  -> boundary_output, GenDecomp, and multiplicity
  -> raw_count and N_gen
  -> C
  -> PhaseAArtifact
  -> PhaseAValidityCertificate.
```

`comparison_definition_order` is frozen independently:

```text
S_compare, including comparison_target, is frozen independently.
(PhaseAArtifact, PhaseAValidityCertificate) + S_compare
  -> PhaseBComparisonCertificate and routed outcome.
```

The derived `S_gen_definition_order` is the union of these two orders and the
displayed join edge. It too must be acyclic.

No reverse read is permitted. In particular, `eq3_output_action`,
`output_transport`, `BoundaryEq`, `output_transport_coherence`,
`boundary_eval`, `SchemaCheck`, `residual_rule`,
`StructuralCheck`, `Adm`, `LiftEq`, `GenDecomp`, `TargetEq`, `Eq3`, `GenEq`,
the key partition, and any selection or adoption rule may not read a later
node, `raw_count`, `N_gen`, `C`, or `S_compare`. `multiplicity` may read only
the frozen decomposition object, never a comparison value or routed outcome.

The future implementation must separate construction from comparison:

```text
PHASE A: CLASSIFY
  input:   S_classify only
  output:  a finite representative list or exact symbolic normal-form
           description, a PhaseAArtifact with underlying witness data and
           outcome proof input, and a finite or exact symbolic description
           of the raw set C; the checker separately emits or rejects a
           PhaseAValidityCertificate

PHASE B: COMPARE
  input:   the immutable PhaseAArtifact, its accepted validity certificate,
           and S_compare, whose
           comparison_target = 3 comes from the public gate
  output:  PASS-COUNT, FAIL-NONTHREE, NONUNIQUE-COUNT, EMPTY, or
           STOP-INTEGRITY, plus a checked PhaseBComparisonCertificate
```

The Phase A builder and classifier must not read `S_compare` or the comparison
target. Its exact dependency closure and allowed file manifest must be
audited; simply omitting one function argument is insufficient. Its output
must be written and hashed before Phase B. A later formal preregistration
must pin the two executable interfaces and the artifact boundary before any
run.

The value three is already public, so dataflow isolation cannot make a future
result historically blind or an independent prediction. The exploration log
and every result-exposed seed must be disclosed. A later result can be only a
preregistered, comparison-target-isolated conditional theorem or postdiction
relative to the frozen owner scope, never retrospective blinded evidence.

The following direct assignments are forbidden:

```text
N_gen := d where d=3 in the architecture notation
N_gen := Tr(J) because a trace equals 3
N_gen := dim(kernel(Tr)) because that dimension equals 3
N_gen := 1+2 from a color splitting
N_gen := a face degree of an icosahedron
N_gen := the number of selected codimensions in C^3
N_gen := the number of historically named charged-lepton formulas
```

Any one of these quantities may become an input witness only through a
separate typed map selected by a comparison-target-independent selection and
completeness theorem. Any proposed external consequence must itself be
preregistered, must not be tautological from the construction data, and must
be checked independently of the generation-count comparison. Merely adding
a second exact identity does not cure target leakage. Numerical coincidence,
familiar terminology, or dimension matching is not a cross-layer lift.

## 11. Public candidate and firewall inventory

The following is a non-exhaustive inventory of identified public candidates
and nearby noncanonical lanes at the pinned commit. It selects none of them
and makes no claim that an unlisted candidate does not exist.

| Candidate | Public scope | Exact obstruction to silent adoption |
| --- | --- | --- |
| `W_5` trace-kernel rows `TRACEKERNEL-RESIDUAL-FORM`, `TRACEKERNEL-HOME-DIMENSION`, and `TRACEKERNEL-F5-HODGE-BRACKET` | `[T] / L1`; related `TRACEKERNEL-CURVATURE-FORCING [O] / MULTI` is separately gated | the public scope grants no generation lift; dimension three and the conditional Hodge split are not generation multiplicity |
| `COLOR-SPLIT-12` | `[D] / NOT_APPLICABLE` | a dictionary split `3=1+2` supplies no L2 source, generation block, or owner dependency |
| `COLOR-KINEMATICAL-GL2` | `[D] / NOT_APPLICABLE` | a kinematical color reading is not a generation multiplicity |
| `HYPERCHARGE-LAW` | `[T] / NOT_APPLICABLE` | exact charge algebra is not an L2-to-L3 lift or complete lift class |
| `MASS-LADDER-FORMS`, `MU-TAU-COEFFICIENT`, and `MU-EXCHANGE-IDENTITY`, on the empirical electron-mass anchor | `[D] / NOT_APPLICABLE`, then `[T] / NOT_APPLICABLE` | named mass formulas do not define a complete generation schema or count theorem |
| `COLOR-CORE-2I`, `COLOR-GOLDEN-TABLE`, `COLOR-MCKAY-E8`, `COLOR-INTEGRAL-LIFT`, `QPAIR-SYM2-2I-IRREDUCIBLE`, `QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4`, and `COLOR-CM-2I-SEMILINEAR-PAIR` | first four `[T] / NOT_APPLICABLE`, next two `[T] / L1`, last `[T] / L4` | none has a registered dependency, concrete L2 source, and complete L3 boundary functor for this owner |
| icosian common-carrier proposals | noncanonical note scope, with no Registry or NORMATIVE item | no public authority, complete carrier selection, or registered generation dependency |
| public E8 functional-calculus rows `J-LI-E8-SHELL-MULTIPLICITY-NOGO` and `MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER` | `[T] / L6` and `[F] / L6` | a different layer and a falsified carrier route cannot be retyped as the required L2-to-L3 lift |
| `J-TORAL-ENTROPY` and `J-TORAL-PERIODIC-POINTS` on `R^4/Z^4` | `[T] / L2` and `[C] / L2` | no dependency or typed route from this torus to `GENERATIONS-L3` |
| `CURVATURE-HISTORICAL-TRACE`, `CURVATURE-HISTORICAL-GAUSS-SPLIT`, `CURVATURE-TRACE-VALUE`, and `CURVATURE-OPERATOR-CANONICAL` | historical rows `[T] / L2`, value `[F] / L2`, canonicality `[O] / L2` | no canonical physical reading, completed L3 boundary functor, or owner dependency |
| `TT-QUADRATIC-GERM` | `[D] / L2` | a bookkeeping input has no generation object, lift, or count functional |
| four classes behind `SPIN-LIFT-FORCED` | `[F] / L3` | four placement or lift classes are not generation blocks, and the row falsifies uniqueness rather than deriving a generation count |

The dependency ledger, not thematic resemblance, controls inheritance. A
future owner may propose one candidate only by publishing all missing fields
of `S_gen`, adding every required dependency, and passing the
comparison-target leakage audit before classification.

## 12. Result-exposed and historical risk ledger

Exploratory review found result-exposed algebraic, orbifold, curvature,
McKay, and historical defect constructions. Their detailed calculations and
nonpublic version labels are deliberately outside this public definition
contract. They are differently typed, have no common public comparison
relation, and are not members of a frozen complete `A`. They illustrate
specification risk only. They do not prove `NONUNIQUE-COUNT`,
underdetermination of a completed public profile, or any scientific outcome.

The following disclosures are mandatory for any later owner proposal:

1. every result-exposed seed, its output, and every carrier, restriction,
   equality, and occurrence-count choice inspected during exploration;
2. every nonauthoritative algebraic or orbifold seed as a specification-risk
   disclosure only, never as an inherited definition or blinded prediction;
3. the historical curvature/domain-wall route supplies no public canonical
   L2 source, L3 boundary carrier, or complete boundary functor;
4. historical face-degree, defect-codimension, trace-kernel, color-split,
   charged-lepton, McKay, and generation-like readings expose their target
   or remain at other layers;
5. any superseded incidence-map control or later nonpublic manuscript remains
   nonauthority and cannot be retyped as the current generation lift;
6. the complete class behind `SPIN-LIFT-FORCED [F]` has four inequivalent
   classes at its own scope, and removing one witness to leave three would be
   post-result selection; and
7. internal full-dynamical-color language cannot override public
   `COLOR-DYNAMICAL-COLOR [F]` or the limited dictionary scope of
   `COLOR-LADDER-DICTIONARY [D]`.

These records cannot later be presented as blinded evidence. They are not
public dependencies, evidence, definitions, carrier selections, or inputs
to a formal probe. A future owner must disclose any use of them, justify its
source, target, equality, and universe choices independently of the exposed
count, and pass the complete comparison-target leakage audit in section 10.

## 13. Dependency and gate contract

The accepted definition must publish two dataflow-separated directed acyclic
graphs. `classification_dependency_DAG` has one node for every universe,
class, selection or adoption rule, carrier, action, map, normalization,
decomposition rule, key rule, classifier input, Phase A artifact field, and
validity-check field; it contains no `S_compare` value and does not contain
its own graph or order manifest as a node.
`comparison_dependency_DAG` has only the immutable Phase A artifact and
validity-certificate inputs, the non-manifest `S_compare` data fields, Phase B
checker, certificate, and route. It excludes itself,
`comparison_definition_order`, and the derived union from its node set. Their
exact common graph type is

```text
DependencyDAG = (DependencyNode, DependencyEdge, reads),
DependencyEdge subset DependencyNode x DependencyNode,
(u,v) in DependencyEdge means that v reads u,
reads(e) = the exact named fields consumed across edge e,
with a public proof that DependencyEdge is acyclic and complete relative to
the executable or proof manifest.

S_gen_dependency_DAG =
  classification_dependency_DAG
  union comparison_dependency_DAG
  union the declared Phase-A-artifact/certificate join edges.
```

The node and edge sets must be set-coded and deterministically serializable.
The derived `S_gen_dependency_DAG` must also be acyclic. Each consumed node
must record

```text
item_id, item_type, status, layer, evidence_id,
relation, status_ceiling, source_commit.
```

Every edge must say exactly which data are read. At this audit pin, inherited
nodes must resolve at `43cfd9e4ca570a51f9aa548a8b0e61dad45f5b7f`.
Any later accepted `S_gen` must repin after the definition fold is merged and
read back, so newly adopted definition nodes resolve at that later public
commit.

The inherited floor

```text
GENERATIONS-L3 -> DEF-ARCHITECTURE
```

is a lower bound, not a complete graph. The definition must add actual
dependencies for the chosen L2 source, L3 boundary, generation schema, and
classification laws. An `F` or unresolved `O` item may be a blocker or
negative control, but not a positive `REQUIRES` premise above its status
ceiling. For every actual cross-layer dependency, the dependent owner must
list the matching gate in `NORMATIVE.gate_ids`; otherwise the definition
remains `STOP-PREDEFINITION` until a separate fold creates or assigns the
gate.

`GENERATIONS-L3` owns `GATE-L2-L3-GENERATIONS`, the only current registered
gate for the declared transition. A candidate may not create an unnamed
L2-to-L3 shortcut. A registered, typed upstream decoder dependency is not
forbidden merely because it is a decoder. What is forbidden is any read of
`S_compare`, a measurement, or a later output by `X2`, `A`, an equivalence,
or a selection/adoption rule, plus any decoder-output feedback into the
autonomous update `U`.

## 14. Completeness and certificate contract

A future classification is accepted only through one of these exact modes:

```text
SYMBOLIC
  a written theorem reduces every admitted lift to a finite list or an exact
  symbolic family of declared normal forms and proves that the description
  is exhaustive;

FINITE-CENSUS
  a written finiteness theorem proves exact bounds, an exact enumerator visits
  every case in a deterministic order, and a checker validates inclusion,
  exclusion, equivalence reduction, counts, and completeness;

HYBRID
  a written symbolic reduction produces one finite residual class, followed
  by the complete exact census above.
```

The remaining classification fields have these exact roles:

```text
classifier
  a mode-tagged total normal-form relation with proof terms in SYMBOLIC mode,
  a total exact enumerator plus inclusion/exclusion classifier in
  FINITE-CENSUS mode, or the declared composition of both in HYBRID mode;

deterministic_order
  one exact decidable total order on every finite enumerator domain and its
  output records, or NOT_APPLICABLE with a SYMBOLIC mode-derived basis;

completeness_proof
  one public proof object or reviewed-theorem record establishing that the
  classifier covers every object of LiftSigma, decides Adm, and covers every
  class of A/LiftEq in the exact claimed mode.
```

A bounded search without a theorem that the bound is complete gives
`STOP-INTEGRITY`; a proposal that relies on such a search remains
`STOP-PREDEFINITION`.
Floating-point clustering, numerical rank decisions, heuristic isomorphism,
random sampling, and manual representative selection cannot certify a
formal result.

`classification_mode` is tagged `SYMBOLIC`, `FINITE-CENSUS`, or `HYBRID`.
For `SYMBOLIC` or the symbolic part of `HYBRID`, `symbolic_proof_mode` is
exactly `PROOF-TERM` or `REVIEWED-THEOREM`; for a pure finite census it is
`NOT_APPLICABLE` with that mode as its basis. `PhaseAArtifactSchema` freezes
the fields below, while
`PhaseAValidityCertificateSchema` freezes the witness types for all
underlying validity obligations. A field that does not apply in one mode
must use an exact `NOT_APPLICABLE` value with a mode-derived basis; it may not
be silently omitted. A raw Phase A artifact must contain at least:

```text
authority and source hashes
S_classify hash and comparison-target-free dependency-closure manifest
classifier or symbolic-proof hash
mode tag and deterministic-order identifier or exact NOT_APPLICABLE basis
finite representatives or an exact symbolic normal-form description
inclusion witnesses or one symbolic inclusion theorem
excluded cases or families and exact exclusion reasons
equivalence-class certificates
generation-schema identifiers, SchemaEq classes, and transport certificates
generation-block decomposition certificates
N_gen values or an exact symbolic value description
invariance and auxiliary-key uniformity certificates
completeness theorem or finite-bound certificate
finite or exact symbolic raw C artifact hash
all underlying witness data required by PhaseAValidityCertificateSchema
one exact outcome-proof input:
  EMPTY       proof that Q is empty;
  SINGLETON   nonempty witness, integer n, and universal N_gen=n proof;
  NONUNIQUE   unequal-count witnesses or an equivalent exact theorem
```

The raw artifact does not contain `PhaseAValidityCertificate`.
`PhaseAArtifactChecker` verifies the artifact and its underlying witness data,
then either rejects or emits that certificate as a separate object binding
the artifact hash and `S_classify` hash. The certificate contains no
comparator input or result. After it verifies, Phase B emits a separate
artifact conforming to `PhaseBComparisonCertificateSchema`:

```text
PhaseBComparisonCertificate = (
  Phase A artifact hash,
  accepted PhaseAValidityCertificate hash,
  S_compare hash,
  comparison_target,
  verified outcome-proof input,
  routed outcome
).
```

`PhaseBComparisonChecker` verifies this binding and the route. In
`PROOF-TERM` mode, a frozen proof kernel checks symbolic exhaustiveness and
the machine checker validates its proof term and kernel pin. In
`REVIEWED-THEOREM` mode, a public theorem review supplies the mathematical
acceptance record; the machine checker verifies its exact identifier, hash,
scope, and manifest but does not pretend to decide arbitrary prose. For a
finite residual census, the checker itself verifies exhaustive coverage.

Within those mode boundaries, the two exact checkers must reject an unknown
identifier, incomplete field, duplicate class, uncovered finite case,
collapsed non-equivalent schema, ambiguous decomposition, count mismatch, read
of `S_compare` during Phase A, dependency cycle, unregistered layer edge,
missing outcome proof, invalid underlying witness, or comparator mismatch.
Rejection, checker failure, or nontermination routes only to
`STOP-INTEGRITY`.

`PhaseAArtifactCheckerTotality` and
`PhaseBComparisonCheckerTotality` are proof obligations over the frozen input
schemas: each checker must terminate with either one accepted certificate or
one exact rejection record. A process timeout or implementation failure is
an operational `STOP-INTEGRITY`, never evidence for `EMPTY` or a count.

An exact proof term may cover an infinite symbolic class; finiteness is not a
precondition for symbolic proof. An ordinary executable audit does not
replace a public reviewed theorem, and a reviewed theorem does not replace an
exhaustive enumerator where the claimed mode is `FINITE-CENSUS`.

## 15. Acceptance test for `READY-DEFINITION`

A reviewer must be able to establish all of the following without reading the
output of the frozen final class. Previously exposed exploratory seed outputs
are risk disclosures, not Phase A output:

1. every slot of `S_classify` and `S_compare` has an exact complete public
   value, definition, or resolvable identifier at a post-fold readback pin;
2. `SourceUniverse`, `SourceClass`, `SourceEq`, and any selected nonempty
   public `X2` have exact structure, action, transports, owner, context, and a
   complete comparison-target-independent selection or reviewed
   owner-adoption scope;
3. `TargetUniverse`, `TargetClass`, `TargetEq`, and any selected public `Y3`
   are nonempty and have exact structure, action, dependent `BoundaryOut`
   fibers, induced `eq3_output_action`, `BoundaryEq`, `BoundaryQuotient`,
   pre-quotient transports, transport-coherence proofs, owner, context, and a complete
   comparison-target-independent selection or reviewed owner-adoption scope;
4. `GenSchemaUniverse`, `GenSchemaClass`, `SchemaEq`, every source, version,
   status, selection or adoption, nonemptiness, completeness, `GenEq`, and
   transport are frozen before candidate output, with schema `s` retained as
   a substantive `LiftIndex` coordinate;
5. one generation block is defined independently of multiplicity, with exact
   gauge-group, chirality, antiparticle, neutrino, color, weak-component,
   hypercharge, anomaly, residual, field-content, and mixing-data rules;
6. `LiftTagSet`, `LiftIndex`, `LiftSigma`, every tagged lift type, substantive
   and auxiliary key domain, their nonemptiness witnesses, codomain, totality,
   action law, context, and overlap are exact;
7. `A` is the complete comparison-target-independent admissible class
   relative to the frozen small profile scope, and that scope is fixed by
   theorem or reviewed pre-result adoption rather than merely by a probe
   ansatz;
8. `LiftEq` is an exact structural equivalence, respects every transport, and
   cannot read multiplicity or count;
9. `boundary_eval`, each `SchemaCheck_s`, and each `residual_rule_s` form a
   total count-free chain before `A`; `boundary_output`, `GenDecomp_s`, and
   `multiplicity_s` then form one total exact chain on `A`; auxiliary-key
   uniformity, schema transport, and LiftEq descent are proved before `N_gen`
   is defined, while substantive alternatives remain in `Q`;
10. the definition order, separated classification and comparison dependency
    graphs, and their derived union are complete, public, acyclic,
    status-ceiling aware, correctly gated, and repinned after the fold;
11. the tagged classifier or symbolic proof is terminating, exact, sound,
    complete, and supplies a decidable outcome proof object;
12. the Phase A and Phase B artifact or certificate schemas and total checkers
    cover inclusion, exclusion, equivalence, output, count, completeness,
    validity, rejection, and routing;
13. Phase A cannot read `S_compare` or `comparison_target`, its immutable
    output precedes Phase B, and exposed exploration is fully disclosed;
14. the routing is syntactically open to `PASS-COUNT` and
    `FAIL-NONTHREE`, and neither is assumed or excluded by a
    comparison-loaded definition;
15. a verified `PhaseAValidityCertificate` is required first, and `EMPTY`,
    `NONUNIQUE-COUNT`, and `STOP-INTEGRITY` cannot be mislabeled as a
    singleton count;
16. `SourceClass`, `TargetClass`, `GenSchemaClass`, `LiftTagSet`, every
    `K_sub`, and every `K_aux` are nonempty; a scientific `EMPTY` can arise
    only because every lift fiber is empty or every lift fails `Adm`, in both
    cases proving that the complete admissible class `A` is empty; and
17. no physical interpretation is stronger than its separately registered
    dictionary status.

If any item fails, the only valid state is `STOP-PREDEFINITION`.
`READY-DEFINITION` would say only that a later scientific question is well
posed. It would not assert existence, count, uniqueness, Standard-Model
identification, or positive closure.

## 16. Required owner decisions

Public v72 does not determine the following choices. They require an explicit
owner-reviewed decision before this note can leave `STOP-PREDEFINITION`:

```text
OD0   RESOLVED: retain #685; close #687 as duplicate and relinquish its P-ID;
      companion PR #688 merged and rescanned as compatible
OD1   adopt COUNT-ONLY, or stop and replace this tuple with a complete
      FULL-STRUCTURE contract
OD2   SourceUniverse, SourceClass, SourceEq, and the L2 source disposition
OD3   TargetUniverse, TargetClass, TargetEq, BoundaryOut,
      eq3_output_action, BoundaryEq, BoundaryQuotient, output transport, and
      output-transport coherence, and the L3 target disposition
OD4   GenSchemaUniverse, GenSchemaClass, SchemaEq, every source, version,
      status, disposition, selection or adoption, nonemptiness, completeness,
      and all one-generation conventions
OD5   multiplicity and residual-sector rules
OD6   nonempty LiftTagSet, LiftIndex, LiftUniverse, lift disposition, every
      exact tagged LiftType, and each totality law
OD7   complete admissible class, profile-scope basis, schema-coordinate
      treatment, and the frozen substantive-versus-auxiliary key partition
OD8   lift and output equivalences
OD9   boundary_eval, every SchemaCheck and residual route, boundary_output,
      schema-indexed GenDecomp and multiplicity, raw_count, descent, and total
      invariant N_gen
OD10  complete separated classification and comparison definition orders and
      dependency DAGs, their acyclic unions, and any missing definition-only
      gate fold
OD11  symbolic, finite-census, or hybrid completeness mode
OD12  gate routing for validity-first STOP-INTEGRITY, EMPTY,
      NONUNIQUE-COUNT, and any residual diagnostic
OD13  scheduler disposition while the preceding fields are unresolved
OD14  disposition of all result-exposed algebraic, orbifold, curvature, and
      historical candidate seeds
```

No owner decision may be made by choosing the branch that returns three. A
new candidate profile requires comparison-target-independent criteria frozen
before its run. A result-exposed candidate instead requires an independent
architectural rationale, complete disclosure, and an explicitly
architecture-relative postdiction ceiling; it cannot be relabeled as a
pre-output prediction.

## 17. Current definition decision

Applying section 15 at the pinned commit gives:

```text
STOP-PREDEFINITION
```

Reason:

```text
the authority, owner, endpoints, gate, and dependency floor are public;
the source and target universes and selection rules, L2 source, L3 target,
generation-schema provenance, LiftIndex and lift universe, complete
admissible class, profile-scope basis, output and decomposition maps,
equivalence, count descent, complete dependency graph, certificate split,
and completeness method are unresolved.
```

This is the only result of this note. It is a definition audit, not a
scientific `EMPTY`, `FAIL-NONTHREE`, or falsification of `GENERATIONS-L3`.
It also records that the current `READY` scheduler label is insufficient for
a run. Changing that label requires a separate Canon proposal.

## 18. Future formal lane, still forbidden

Only after all owner decisions are public, the definition is reviewed as
`READY-DEFINITION`, and the required Canon gate and scope repairs are merged
and read back from `main` may a separate collision scan reserve a fresh
formal identifier.

That later preregistration must freeze the six policy fields, the complete
`S_gen` tuple, the Phase A and Phase B interfaces, source hashes, exact
checker, stopping rules, and all outcome routes before execution. No
diagnostic computation performed during definition work may later be
presented as blinded formal evidence.

## 19. Debt firewall

This note creates no Canon, Registry, Frontier, gate, dependency, evidence,
claim status, release, theorem, derived dictionary, probe, verifier, formal
run, generation count, Standard-Model boundary, decoder field, apparatus,
event, occurrence law, stream, measure, metrology, or experiment.

It does not select the toral, curvature, `W_5`, color, hypercharge, `2I`, E8,
icosian, spin-lift, mass-ladder, or historical defect route. It does not
alter the autonomous update `U`. Its sole purpose is to expose and type every
decision that must precede an honest attack on `GENERATIONS-L3`.
