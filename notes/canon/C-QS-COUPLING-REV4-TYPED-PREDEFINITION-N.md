# C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N: typed Schwinger-coupling predefinition (NON-CANONICAL)

~~~text
NOTE STATE:              DRAFT / NON-CANONICAL
DEFINITION DISPOSITION:  STOP-PREDEFINITION / OWNER READBACK REQUIRED
SCIENTIFIC STATUS:       QUANT-SUBSTRATE [O] UNCHANGED
SCIENTIFIC RUN:          NONE
FORMAL PROBE:            NONE
PROBE IDENTIFIER:        NONE RESERVED
PREREGISTRATION:         NONE
VERIFIER:                NONE
COORDINATION LOCK:       issue #689
OWNER ROW:               QUANT-SUBSTRATE [O]
THIS NOTE ACTION LAYER:  NOT_APPLICABLE
PROPOSED GATE PATH:      L1 -> L5 -> L6
CANON CHANGE:            NONE
REGISTRY CHANGE:         NONE
NORMATIVE CHANGE:        NONE
GATE CHANGE:             NONE
STATUS MOVE:             NONE
~~~

Public work-object lock: issue #689.

This note is the commissioned Rev 4 response to the v71 audit of the
unratified Rev 3 owner definition. It defines the types, dataflow, validity
conditions, target-isolation firewall, decision routing, and future gate rows
that must be frozen before a formal Schwinger-coupling probe can exist.

It does not ratify the Rev 3 carrier, vertex, state, reading, normalization,
wall, or equivalence choices. It does not construct a substrate coupling,
compute a coefficient, compare a coefficient with the Schwinger target, or
authorize code. Its present definition disposition is
STOP-PREDEFINITION.

## 1. Authority, collision, and disposition pin

~~~text
repository:                mathorn1973/twist-j
audit/main commit:         7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
Public Canon:              v71
Canon state:               ACTIVE
tag:                       canon-v71
content commit:            a77d720433c19976f9ab663d023ec9364eac34eb
Canon SHA-256:             0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
Canon bytes:               369836
owner:                     QUANT-SUBSTRATE [O]
scheduler:                 QUANTUM_EM / ROOT / READY / FORMAL
work-object issue:         #689
note branch:               notes/c-qs-coupling-rev4-typed-predefinition-n
this file:                 notes/canon/C-QS-COUPLING-REV4-TYPED-PREDEFINITION-N.md
Rev 3 owner draft SHA-256: 93669488f8ffbac90b1fc3cc6aa3310052c04863c0475819fd50a68688ffb543
Rev 3 prereg draft SHA:   1797e3a7c18f4e965f96ffbe64d1d2a0c426b0b73c2179d91b0d035f8810e437
Rev 3 disposition:        UNRATIFIED / SUPERSEDED FOR RE-KEYING
formal pin/run/result:     ABSENT / NOT AUTHORIZED / ABSENT
~~~

The owner selected option (a) in issue #689: commission Rev 4 against
Public Canon v71. No partial ANO was granted to Rev 3. Rev 1 remains
unratified history and Rev 2 remains VOID. The Rev 3 preregistration file is
only a draft and has never been a public pin.

A fresh scan on the stated base found no competing Rev 4 issue, pull request,
branch, formal probe, Registry row, or repository object. Issue #689 is the
sole public lock for exactly this note path and branch. It reserves no
P-QS-COUPLING-1 identifier. A future probe identifier requires a new scan and
a new exact lock after every definition and gate prerequisite in section 18
has closed.

READY in canon/FRONTIER_PROGRAMS.tsv schedules work. It supplies no missing
type and authorizes no verifier or evaluation.

## 2. Exact inherited public surface

The current public surface relevant to this definition is:

~~~text
OWNER
  QUANT-SUBSTRATE [O]
  scope:
    the Larmor gate and the Schwinger physical-realization gate on the
    archimedean wall; production of the first-order electron coefficient
    from a substrate coupling remains open
  NORMATIVE layer:     NOT_APPLICABLE
  NORMATIVE gate_ids:  empty

TARGET
  QUANT-SCHWINGER-TARGET [T]
  exact arithmetic only:
    J Jbar / script-Q = 1/(2 pi)
  explicit exclusions:
    no first-order electron coefficient, substrate coupling, action,
    normalization, regularization, measured observable, or uniqueness

DEPENDENCIES
  QUANT-SUBSTRATE -> DEF-ARCHITECTURE
  QUANT-SUBSTRATE -> QUANT-SCHWINGER-TARGET
  ELECTRON-G-TREE -> QUANT-SUBSTRATE  (BOUNDED_BY)

GATES
  GATE-L1-L5-QS-COUPLING-STREAM: absent
  GATE-L5-L6-SCHWINGER-TERM:     absent
~~~

The absence of both gates is load-bearing. Their names in Rev 3 created no
gate, and this note does not create them. Under the parent-owned topology
option 2 in section 16, a later fold must add both rows to canon/GATES.tsv
and both identifiers to the gate_ids field of the QUANT-SUBSTRATE row in
canon/NORMATIVE.tsv in the same checked change. Under child-owned option 1,
the child row, dependency, gate ownership, and parent aggregation require a
fresh exact proposal; these displayed parent identifiers are not inserted.

The following public rows may be cited only at their exact registered scope:

| Public row | Status | Exact contribution allowed here | Contribution not supplied |
| --- | --- | --- | --- |
| J-PROJECTIONS | T | principal modulus and principal argument of J, including arg J = 2 pi/5 | no physical differential law |
| PI-FROM-J | T | principal-branch logarithmic definition of pi from J | no Schwinger coupling |
| AXIOM-PROJECTION-DICTIONARY | D | argument projection may be read as electromagnetism and phase | no unique reading and no rate |
| DIRAC-STEP | D | declared Dirac step and rest-rung interpretation | no frozen coupled carrier |
| DIRAC-STEP-THEOREMS | T | determinant 5, registered step invariants, and unitarized rest-coin facts | no coupled response |
| CHECKERBOARD-GAUSS-TOWER | T | exact 5^N norm tower for the registered checkerboard data | no normalization for an untyped new coupling |
| KERNEL-CELL-DICTIONARY | D | a Z_5 fiber, deposits in fifths, flux, and Born-square reading | no theorem that A'[Z_5] is the only memory |
| SUBSTRATE-KNIT | T | exact squared overlap 1/5 on its registered bases | no vertex selection |
| BORN-FACE-WEIGHTS | T | five exact abelian face weights in Q(sqrt5) | no new stream or package normalization |
| MEASURE-BORN-VERB | D | the verb may be read through its Born square on the registered face-weight layer | no automatic read for the proposed QS stream |
| METRO-TICK | T | 2 pi/5 per tick on its exact registered scope | no electron response law |
| ELECTRON-G-RATIO | T | exact registered ratio identities and the base quotient 2 | no differential response |
| ELECTRON-G-DOUBLE-COVER | T | exact orbital-to-spinor ratio and closure data | no first-order coefficient |
| ELECTRON-G-TREE | D | g = 2 as the registered flux-to-half-angle quotient | no first-order coefficient and no delta-g law |
| WALL-CIRCLE-LEMMA | T | principal Li_1 and real-part Li_2 wall identities | no coupling, action, or normalization |
| WALL-LI2-RUNG | T | exact s = 2 real-part data and channel ratio 9 | no substrate coupling or Schwinger coefficient |
| J-MODULUS-CHORD | T | Phase B target dependency J Jbar = phi^-2 | no Phase A response |
| BRIDGE-DEFECT | T | Phase B target/ring dependency, including pi transcendence and script-Q phi^2 = 2 pi | excluded in full from Phase A |
| QUANT-SCHWINGER-TARGET | T | the Phase B comparison value only | no Phase A construction |

GATE-L5-L6-BORN-READING is the existing closed dictionary lift owned by
MEASURE-BORN-VERB. If the candidate Born leg consumes that dictionary, its
dependency and scope must be recorded. It is not either proposed QS gate and
does not lift an untyped QS stream by itself.

BRIDGE-DEFECT [T] carries both algebraic bridge data and
script-Q phi^2 = 2 pi. It is excluded in full from the Phase A dependency
closure. The integer 5 needs no import from that row. The Rev 3 use of
xi phi^2 = 5 is therefore dropped, not re-keyed.

Any reference to an internal v184 snapshot is lineage only. It cannot fill a
slot, justify a selection, or enter a certificate.

## 3. Rev 3 audit disposition

The parts of Rev 3 are handled as follows:

| Rev 3 item | Rev 4 disposition |
| --- | --- |
| v20 authority pin | rejected; replaced by the v71 pin in section 1 |
| proposed carrier ring A' | retained only as candidate A1, not adopted |
| finite deposit-pair vertex class | retained only as candidate A2, not adopted |
| rest point and coin branch | retained only as candidate A3, not adopted |
| channel definition of alpha | retained only as candidate A4, not adopted |
| polylogarithmic wall as sole closure | retained only as candidate A5, not adopted |
| proven symmetry core and quarantined automorphisms | retained as a proposed classification task, not as a quotient theorem |
| unnamed registered phase dictionary | rejected; replaced by the typed reading-family contract |
| script-Q in the D5 generator list | prohibited in Phase A |
| target-driven degree ledger | removed from Phase A; optional Phase B diagnostic only |
| admissible iff rates exist | rejected; every raw candidate must receive a total record |
| undefined K when c_w = 0 | repaired by an explicit denominator state |
| claimed 32-state tree and 64-state break round | rejected; replaced by a dependent six-constructor outcome type |
| two named but absent gates | retained only as exact future row proposals |

The following statements are owner adoptions, not public consequences:

~~~text
A1  the carrier coefficient ring is exactly Z[zeta_5, i][1/10]
A2  the complete vertex universe is exactly the 24 nontrivial deposit pairs
A3  z = 1 and a specified antiunitary orbit of v_plus are the complete
    state context
A4  one completed excursion defines the alpha coordinate
A5  the registered wall data are the sole allowed infinite closure resource
A6  delta g = delta theta/(pi/5) is the response law
A7  A'[Z_5] is the only writable memory
A8  the proposed equivalence core is complete
A9  every substantive read-package and context alternative is represented in
    the raw-response family and later coefficient image
A10 the proposed L1 -> L5 -> L6 gate topology is the complete Schwinger
    subpath; it is not asserted to be the complete QUANT-SUBSTRATE parent
    topology
A11 the exact coupled one-tick operator, operator order, and stream
    constructor are frozen by a target-free repair of PREDEF-BLOCKER-QS-1
~~~

Each adoption requires an explicit point-by-point owner ANO against the
future immutable hash of this file or a successor. No inference from
ELECTRON-G-TREE, KERNEL-CELL-DICTIONARY, WALL-LI2-RUNG, or the scheduler
counts as that ANO.

## 4. Dataflow separation

A valid definition consists of two immutable definition contracts and two
later execution records:

~~~text
S_classify_def
  target-free construction, structural equivalence, complete classification,
  typed read packages, raw-response schemas, provenance rules, and Phase A
  artifact/checker schemas

S_compare_def
  validation-first consumption of one immutable Phase A artifact; application
  of a pre-frozen response law and alpha map; coefficient construction; import
  of the registered target; exact comparison; terminal routing; and Phase B
  record/checker schemas

S_QS_def = (S_classify_def, S_compare_def)

S_classify_run
  one PhaseAArtifact value produced under S_classify_def

S_compare_run
  one PhaseBRunRecord value produced under S_compare_def and consuming one
  immutable valid PhaseAArtifact
~~~

`S_classify_def_hash` and `S_compare_def_hash` are each SHA-256 of the
canonical serialization of the corresponding definition tuple. Neither hash
field is a member of its own hashed payload. Execution records carry those
hashes as readback fields; artifact hashes, computed records, value sets,
comparison witnesses, and outcomes are never members of a definition tuple.

The dependency graph is directed. `pre-output structural schemas` below
means only their target-free types, domains, and structural fields; it does
not mean a computed stream, reading, rate, coefficient, or target-dependent
selection:

~~~text
authority pin
    -> carrier and state specifications
    -> complete raw coupling universe
    -> pre-output structural schemas for the action, grading, contexts, and
       package domains
    -> target-free structural checks
    -> target-free structural equivalence and quotient
    -> exact stream construction
    -> typed read-package family over complete context keys
    -> total raw phase/Born response records
    -> target-free raw-response-pair set
    -> immutable Phase A artifact and validity certificate
    -> Phase B response-law and alpha-map application
    -> coefficient-value set
    -> Phase B target import
    -> exact comparator
    -> one terminal outcome
~~~

No Phase B node may affect a predecessor. The Phase A artifact is finalized
and hashed before S_compare_run reads QUANT-SCHWINGER-TARGET. Re-running,
filtering, reordering, selecting a representative, changing a reading,
changing a closure, or changing a normalization after target import is a
definition breach and routes STOP-INTEGRITY.

## 5. Complete definition object

The owner definition must publish a value for every field in the two
definition tuples below and an exact schema for each later execution record.
The displayed PhaseBRunRecord is a value shape only; no run field is filled
at definition time.

~~~text
S_classify_def = (
  ClassificationAuthorityPin,
  PublicSourceTable,
  ForbiddenSourceTable,

  RingSpecUniverse, RingSpecClass, RingSpecEq,
  CarrierUniverse, CarrierClass, CarrierEq,
  CarrierSpec, carrier_owner, carrier_context,
  carrier_nonempty, carrier_completeness,
  carrier_disposition, carrier_selection_or_adoption,

  StateUniverse, StateClass, StateEq,
  StateSpec, state_orbit, state_context,
  state_nonempty, state_completeness,
  state_disposition, state_selection_or_adoption,

  CouplingTag, CouplingIndex,
  CouplingUniverse, CouplingType, CouplingEqRaw,
  vertex, uncoupled_index, raw_nontrivial,
  coupling_nonempty, coupling_completeness,
  coupling_disposition, coupling_selection_or_adoption,

  StructuralCheck, StructuralState,
  StructuralAdmPredicate, StructuralAdmClass,

  SymmetryUniverse, SymmetryAction, SymmetryStatus,
  ProposedEquivalenceGroup, CouplingEq,
  CovarianceAction, quotient_well_defined,

  StreamType, stream_constructor, stream_totality,
  ExcursionGrading, ExcursionEq, order_one_projection,
  normalization_source, normalization_totality,

  SubstantiveContextKey, AuxiliaryContextKey, ContextKey,
  ContextKeyPartition, ContextOccurrenceOrSelection,
  ContextNonempty, ContextCompleteness,

  RateState, ReadingLeg, ReadPackage,
  ReadingFamilyUniverse, ReadingFamilyClass, ReadingFamilyEq,
  PhaseLeg, ChannelLeg, LegOverlap, PackageOverlap,
  ReadPackageMap, ReadPackageEq,
  reading_nonempty, reading_completeness,
  reading_disposition, reading_selection_or_adoption,
  auxiliary_uniformity,

  ConstantAtom, ConstantExpression, ProvenanceDAG,
  PhaseAAllowedSource, PhaseAForbiddenSource,
  provenance_totality, target_isolation,

  ClosureResource, ClosureRule, ClosureEq,
  closure_totality, closure_completeness,
  closure_disposition, closure_selection_or_adoption,

  PhaseTangentRate, ChannelBornRate,
  RawResponseState, RawResponsePair,
  CouplingRecordSchema, record_totality_schema,

  RawClass, ClassifiedClass, EvaluableClass,
  ClassCompletenessCertificateSchema,
  RawResponsePairSetSchema, pair_set_completeness_schema,

  ClassificationMode, ClassificationProofSchema,
  classification_definition_order,
  classification_dependency_DAG,
  PhaseAArtifactSchema,
  PhaseAValidityCertificateSchema,
  PhaseAArtifactChecker,
  PhaseAArtifactCheckerTotality,
  PhaseAFirewallChecker,
  PhaseAFirewallCheckerTotality
).

S_compare_def = (
  ResponseLaw,
  AlphaCarrier, AlphaZero, AlphaEq,
  AlphaTangentCarrier, AlphaTangentZero, AlphaTangentEq, AlphaMap,
  CommonStreamTangent, ElectronGerm, AlphaCoefficientExtraction,
  ChainRuleCertificate,
  ComparisonAuthorityPin,
  ComparisonTarget,
  ComparisonRing,
  target_embedding,
  PhaseBStageState,
  RateMapLift,
  MomentRateConstructor, AlphaTangentRateConstructor,
  MappedRawResponseState, PhaseBRatePairConstructor,
  DenominatorState, DenominatorStateConstructor,
  DenominatorCoefficientInput, CoefficientState,
  CoefficientRecordSchema, CoefficientRecordConstructor,
  coefficient_invariance_schema,
  CoefficientValueSetState,
  all_mandatory_coefficients_exact_with_nonzero_denominators,
  guarded_value_set_completeness_schema,
  ExactEq,
  ExactNeq,
  TargetAccessState,
  ComparisonState,
  Outcome,
  validity_first_router,
  comparator,
  comparison_definition_order,
  comparison_dependency_DAG,
  PhaseBComparisonCertificateSchema,
  PhaseBComparisonChecker,
  PhaseBComparisonCheckerTotality
).

PhaseBRunRecord = (
  S_compare_def_hash,
  PhaseAArtifactHash,
  PhaseAValidityReadback,
  MappedRawResponseTableState,
  DenominatorStateTableState,
  CoefficientRecordTableState,
  CoefficientInvarianceState,
  CoefficientValueSetStateValue,
  FreeParameterAggregateState,
  ComparisonStateValue,
  OutcomeValue,
  PhaseBComparisonCertificate,
  PhaseBRunPayloadHash
).
~~~

The names in `S_classify_def` and `S_compare_def` denote types, schemas,
constructors, exact algorithms, proof obligations, and checkers, never a
future execution value. `S_classify_run` is exactly the PhaseAArtifact record
defined in section 13. `S_compare_run` is one later value of the displayed
PhaseBRunRecord. Its `S_compare_def_hash` is a reference to the externally
computed definition hash, not part of the hashed definition payload.
`PhaseBRunPayloadHash` is SHA-256 of the canonical serialization of every
preceding PhaseBRunRecord field with the hash field itself omitted.

Every definition field must contain an exact public value or definition, a
resolvable public identifier, or the literal UNRESOLVED. A prose synonym, private
notebook, implicit convention, outcome-dependent selection, bare null, or
unhashed generated table is invalid. NOT_APPLICABLE is allowed only when the
controlling schema explicitly permits it and its public basis is recorded.

Every class-level disposition uses exactly one constructor:

~~~text
GLOBAL-CLASS
  a public theorem proves this is the complete class at the claimed scope

FORCED-SELECTION
  an independent public rule selects one member from a complete larger class

OWNER-ADOPTED
  the owner explicitly freezes the class or member as part of the model

ANSATZ-ONLY
  one explored family without a completeness or selection claim

UNRESOLVED
  no valid disposition is frozen
~~~

Carrier, state, coupling, package, context, closure, and equivalence
dispositions are separate fields. Completeness of the 24 deposit-pair census
is only completeness relative to candidate A2. Without GLOBAL-CLASS,
FORCED-SELECTION, or an explicit OWNER-ADOPTED scope, it remains ANSATZ-ONLY
and cannot close QUANT-SUBSTRATE.

## 6. Ring, carrier, state, and coupling types

The predefinition types the Rev 3 proposal without ratifying it.

### 6.1 Ring specification

~~~text
RingSpec = (
  coefficient_ring,
  reading_ring,
  exact_normal_form,
  equality_algorithm,
  involution_sharp,
  embeddings,
  inverted_primes,
  generator_provenance
)
~~~

The current candidate is:

\[
A'=\mathbb Z[\zeta_5,i][1/10],
\qquad
\mathrm{PhasePoint}=\mathbb Q/\mathbb Z,
\qquad
V_{\rm phase}=\text{a frozen exact target-free phase-tangent module},
\qquad
F_{\Pi}=\operatorname{Frac}\!\bigl(\mathbb Q(\sqrt5)[\Pi]\bigr).
\]

Acceptance requires a constructive normal form and equality algorithm for
every ring and carrier, an exact embedding of every output used by a read,
and proof that the list of inverted primes is necessary and complete for the
frozen class. Elements of \(F_{\Pi}\) use reduced coprime polynomial
numerator and denominator over \(\mathbb Q(\sqrt5)\), with a fixed monic
denominator convention. Phase B has the exact specialization
\(\Pi\mapsto\pi\). It is injective because \(\pi\) is transcendental over
\(\mathbb Q(\sqrt5)\).

The Rev 3 Laurent-polynomial ring
\(\mathbb Q(\sqrt5)[\pi,\pi^{-1}]\) is not closed under an arbitrary
quotient \(c_a/c_w\). It is therefore not the comparison carrier. A successor
may use a smaller ring only by proving an exact divisibility or unit
certificate for every admitted quotient.

PhasePoint stores a finite rational phase modulo one full turn where the
root-of-unity hypothesis is proved. It is not a carrier for a signed
stationary rate because it loses winding data and has no canonical rational
lift. The separate module \(V_{\rm phase}\) carries signed infinitesimal
phase responses. Its scalar field, orientation, unit, normal form, equality,
and relationship to a logarithmic derivative of the exact amplitude must be
frozen. Every RATE_EXACT phase rate carries that derivative certificate and
all needed branch or winding coherence. Failure returns a non-success
RateState and routes STOP.

The Rev 3 breaker claim that 1/2 is unavoidable is not a public proof and was
never run under a pin. A larger ring or an added continuous scalar is a new
candidate, not an evaluation-time patch.

### 6.2 Carrier candidate

The candidate carrier has the type:

~~~text
M_D       : rank-2 module over A'
f_0,f_1   : frozen ordered coin basis
R_5       : group algebra A'[Z_5]
M         : M_D tensor R_5
E_k       : R_5 -> R_5, k in Z_5
e_0       : distinguished register basis state
D_rest    : M_D -> M_D
X         : [[0,1],[1,0]] in the frozen coin basis
Z         : [[1,0],[0,-1]] in the frozen coin basis
v_plus    : f_0 + f_1
v_minus   : f_0 - f_1
ZXZ       : -X
P_plus    : (I + X)/2
P_minus   : (I - X)/2
~~~

Before adoption the definition must prove the module ranks, basis
conventions, multiplication law, sharp involution, and exact relationship
between D_rest, X, and the cited DIRAC-STEP scope. KERNEL-CELL-DICTIONARY
permits a Z_5 fiber but does not prove that this carrier or memory is unique.

### 6.3 State candidate

~~~text
fiber:          z = 1
pre-state:      v_plus tensor e_0
candidate mate: v_minus tensor e_0
frozen basis:   {f_sigma tensor e_j}
global map:     K_M(sum_(sigma,j) m_(sigma,j) f_sigma tensor e_j)
                  = sum_(sigma,j) bar(m_(sigma,j)) f_sigma tensor e_(-j)
candidate map:  C = (Z tensor 1) composed with K_M
state orbit:    {v_plus, v_minus} under a future proved C action
reference:      uncoupled D_rest^N(v_plus) tensor e_0
normalization:  candidate 5^N tower with an explicit scope proof
~~~

The state class must be complete for the declared physical context. Calling
z = 1 the rest rung does not by itself prove that no other fiber, coin state,
or coherent state is admissible. Either an independent selection theorem or
an explicit owner adoption must close that choice before READY-DEFINITION.
Plain coefficient conjugation fixes the real vector v_plus and, in the
natural group-algebra basis, fixes each deposit basis vector e_j. It neither
maps v_plus to v_minus nor reverses a register shift. The Rev 3 bar-orbit
statement is therefore rejected. A symbolic tensor Z tensor K_R would not be
well-defined over A' when one factor is linear and the other semilinear. The
candidate instead freezes a basis, defines the global semilinear K_M on M,
and then composes it with Z tensor 1. Calling C antiunitary also requires a
frozen Hermitian form and a proof that C preserves it. Any replacement must
be defined as an operator, proved to preserve the full structure, and
propagated through the coupling indices and all reads.

### 6.4 Coupling universe

For the retained finite proposal:

\[
I_{\rm raw}=\mathbb Z_5^2,\qquad
I_{\rm nt}=I_{\rm raw}\setminus\{(0,0)\},
\]

\[
W_{a,b}=P_+\otimes E_a+P_-\otimes E_b .
\]

The exact type is:

~~~text
CouplingTag   = DEPOSIT_PAIR_V1
CouplingIndex = (CouplingTag, a, b), a,b in Z_5
CouplingType  = End_A'(M)
vertex        : CouplingIndex -> CouplingType
uncoupled     : CouplingIndex -> Bool
~~~

The tagged version prevents a later vertex family from being silently merged
with the deposit-pair family. If another family is admitted, it receives a
new tag, a complete index type, a disjoint overlap rule, and a new owner
readback.

RawClass contains every index in I_nt. A candidate is never removed because
a rate is difficult to compute, fails to close, has zero channel rate, gives
the wrong coefficient, or becomes inconvenient after target import. Every
index receives one total CouplingRecord under section 11.

The claimed exact unitarity, locality, register equivariance, and absence of
momentum dependence are StructuralCheck obligations. They are not
preconditions that may be assumed to discard a failing index.

### 6.5 Exact blocker for the retained action-state pair

The Rev 3 action and pre-state are not merely unproved. Together they make the
proposed two-channel excursion response degenerate.

Because

\[
D_{\rm rest}=I+2iX=(1+2i)P_+ +(1-2i)P_-
\]

and \(v_+=(1,1)\) lies entirely in the \(P_+\) eigenspace,

\[
W_{a,b}(v_+\otimes e_0)=v_+\otimes e_a .
\]

With the Rev 3 order \(U=(D_{\rm rest}\otimes1)W_{a,b}\), exact induction
gives

\[
U^N(v_+\otimes e_0)
  =(1+2i)^N v_+\otimes e_{Na}
\]

for every \(N\). The \(b\) branch never participates. There is one
deterministic register word, not a superposition of emission and
reabsorption paths. The \(e_0\) component is zero unless \(Na=0\) in
\(\mathbb Z_5\); when it returns, its amplitude is exactly the uncoupled
reference and has zero relative phase.

Consequences:

1. the proposed phase shift is either undefined against a zero component or
   exactly zero at a return;
2. the two deposit coordinates cannot both affect the declared response;
3. a formal variable t inserted only after the fact does not create an
   order-one perturbative coefficient of the exact operator;
4. a stationary one-completed-excursion Born rate is not supplied by the
   stated action and state.

This is PREDEF-BLOCKER-QS-1. It is a definition-stage algebraic obstruction,
not a scientific run and not a conclusion about every possible substrate
coupling. READY-DEFINITION requires an exact repair to at least one of the
action, state class, vertex class, excursion notion, or response definition,
followed by a new completeness proof. The repair must be chosen without
reading the Schwinger target.

PREDEF-BLOCKER-QS-1 is a note-local diagnostic label. It is not a Registry
claim, probe identifier, falsifier firing, or status move.

## 7. Exact stream and excursion grading

For a frozen CarrierSpec, StateSpec, and CouplingIndex, the construction must
define:

~~~text
U_i             : exact one-tick operator
Path_N(i)       : complete exact N-tick path decomposition
RegisterWord    : finite word in Z_5 deposits
Excursion       : typed interval leaving e_0 and returning to e_0
ExcursionEq     : equality of intervals plus register words
grade_t         : PathTerm -> N_0
order_one       : Path_N(i) -> all terms with grade_t = 1
Stream_i        : coherent family {Path_N(i)} for N >= 0
StreamEq        : termwise equality after the frozen normal form
~~~

The variable t is bookkeeping only. It is not a matrix entry, coupling
strength, fitted parameter, or physical constant. The definition must prove
that grade_t is independent of a chosen path presentation and that every
order-one term is counted exactly once.

The L1-to-L5 source gate may emit a stream only after:

1. the raw coupling universe is complete;
2. the path decomposition is total and exact;
3. excursion grading is representation independent;
4. the state and normalization contexts are frozen;
5. every undefined construction is represented by an explicit STOP reason.

## 8. Typed reading-package family

The phrase "read through the registered phase dictionary" is retired. A
phase leg and a Born-channel leg have different codomains and are composed;
they are not alternative readings of the same value. The total leg result
type, used unchanged through the CouplingRecord schema, is:

~~~text
RateState(T) =
    RATE_EXACT(value : T, proof)
  | RATE_PROVED_NONEXISTENT(proof)
  | RATE_AMBIGUOUS(values, witness)
  | RATE_UNRESOLVED(reason)

ReadingLeg(Input, Output) = (
  reading_id,
  domain : Input,
  codomain : Output,
  applicability,
  map : Input x ContextKey -> RateState(Output),
  equality_on_output,
  public_sources,
  owner_adoptions
)

PhaseAReadPackage = (
  package_id,
  PhaseLeg,
  ChannelLeg,
  common_context_schema,
  compose : RateState(V_phase) x RateState(Born_rate_carrier)
            -> RawResponseState,
  package_equality,
  package_overlap
)
~~~

ReadingFamilyClass ranges over all admitted PhaseAReadPackage objects.
Alternatives are packages, not the two compositional legs inside one package.
Every package must be applied uniformly to the declared complete structural
class.

The complement of a leg's applicability predicate is never an absent value.
It maps to RATE_PROVED_NONEXISTENT only with an exact proof, to
RATE_AMBIGUOUS when competing values have a witness, and otherwise to
RATE_UNRESOLVED. There is no implicit coercion between a reading wrapper and
a rate wrapper.

### 8.1 Complete context-key space

Every read is indexed by:

~~~text
ContextKey = (SubstantiveContextKey, AuxiliaryContextKey)

SubstantiveContextKey
  a key that can change physical applicability, a raw phase response, a Born
  response, or any later coefficient

AuxiliaryContextKey
  a presentation, representative, basis, serialization, or execution key
  that is claimed not to change those outputs
~~~

The definition must publish:

~~~text
ContextKeyPartition
ContextNonempty
ContextCompleteness
ContextOccurrenceOrSelection
AuxiliaryUniformityProof
~~~

ContextOccurrenceOrSelection must either enumerate every substantive key or
give an independent target-free occurrence or selection rule. A substantive
key may not be quotiented because two outputs happen to agree in one run.
An auxiliary key may be quotiented only after AuxiliaryUniformityProof
establishes equality for every coupling, package, substantive key, and
applicable N-context.

At minimum, the partition must classify the archimedean embedding, logarithm
branch, fiber, state orbit, package identifier, excursion endpoint convention,
stationary-rate convention, normalization presentation, symmetry
representative, and execution presentation. Leaving a key unclassified routes
STOP.

### 8.2 Phase-tangent leg

~~~text
reading_id:
  QS-PHASE-TURN-V1

domain:
  exact order-one e_0-component response relative to the uncoupled
  reference, with its N-indexed stream certificate

codomain:
  an exact stationary signed PhaseTangentRate in V_phase, with an exact
  logarithmic-derivative, orientation, unit, and branch-coherence certificate

context_keys:
  principal archimedean embedding;
  principal branch;
  argument projection context;
  z = 1;
  frozen coin-state orbit;
  order-one excursion grading;
  exact N normalization;
  stationary per-tick convention

map:
  extract only the target-free phase change in turns

equality:
  exact equality in the declared phase-tangent module
~~~

J-PROJECTIONS, METRO-TICK, and AXIOM-PROJECTION-DICTIONARY can support a
turn-normalized principal phase context. The Phase A leg does not apply a
delta-g law, insert pi, construct delta a_e, or know the Schwinger target.

### 8.3 Born-channel leg

~~~text
reading_id:
  QS-EXCURSION-BORN-V1

domain:
  complete order-one excursion terms of the same exact Stream_i

codomain:
  an exact normalized stationary Born-rate record in a declared
  target-free algebraic carrier

context_keys:
  the same coupling index, state orbit, order-one grading, N tower,
  endpoint convention, and stationary per-tick convention as the phase leg

map:
  Born-square aggregation of exactly one completed excursion, with no
  omitted interference or multiplicity term

equality:
  exact equality in the declared codomain
~~~

CHECKERBOARD-GAUSS-TOWER and KERNEL-CELL-DICTIONARY may support pieces of
the normalization and Born interpretation only after an exact scope map is
given. MEASURE-BORN-VERB and BORN-FACE-WEIGHTS must also be named if their
dictionary or face weights are consumed. None automatically normalizes the
new coupled stream.

### 8.4 Leg and package overlap

LegOverlap is defined only for two phase legs or two channel legs with a
common codomain. PackageOverlap is total on every pair of packages after
their legs are composed into the common RawResponseState:

~~~text
DISJOINT
  the declared domains or physical contexts do not overlap

AGREE
  an exact proof shows equal composed outputs on the overlap

COVARIANT
  an exact public transformation relates the composed outputs and the
  transformation is carried into every downstream comparison

CONFLICT
  both apply in the same context and give inequivalent composed outputs

UNRESOLVED
  applicability or equality is not proved
~~~

AGREE never compares a phase-leg value directly with a Born-leg value.
CONFLICT or UNRESOLVED in a package or context affecting either raw response
routes STOP. No preferred package or substantive context may be selected
because a later coefficient matches a target. Reading multiplicity is not
itself a failure; untyped, incomplete, or outcome-dependent multiplicity is.

ReadingFamilyEq is extensional equality of the full typed records, including
leg maps, package composition, context partition, occurrence rule, and
overlap data. Renaming a leg does not create a new family. Changing any
substantive key or package creates a new candidate definition and requires a
new owner readback.

## 9. Constant provenance and target-isolation firewall

Every scalar in the carrier, stream, closure, read, rate, or quotient has an
expression DAG whose leaves are tagged ConstantAtom records:

~~~text
ConstantAtom = (
  value_normal_form,
  source_id,
  source_status,
  source_scope,
  derivation_rule,
  phase,
  allowed_use
)

phase = PHASE_A | PHASE_B
~~~

### 9.1 Phase A allowlist

The allowlist is closed, not illustrative:

- integers and rational operations explicitly admitted by the adopted ring;
- \(\zeta_5\), \(i\), \(J\), and \(\sqrt5\) only through their exact
  public algebraic definitions;
- \(1/5\) only through the adopted ring and, where relevant, the exact
  SUBSTRATE-KNIT scope;
- \(1/2\) only through the adopted ring and a proved need for the frozen
  projectors;
- rational phase points such as \(1/5\) only in PhasePoint, through
  J-PROJECTIONS or METRO-TICK and with the required branch certificate;
- target-free algebraic Born weights only through their exact declared
  public scope.

An allowed value with missing provenance is forbidden. Algebraic equality
with an allowed value does not erase a forbidden source path.

### 9.2 Phase A denylist

The transitive Phase A dependency closure must contain none of:

~~~text
QUANT-SCHWINGER-TARGET
script-Q
script-Q phi^2 = 2 pi
J Jbar / script-Q
pi, 2 pi, inverse pi, or any algebraically equivalent radian normalization
1/(2 pi), whether nominated or not
BRIDGE-DEFECT
WALL-CIRCLE-LEMMA or WALL-LI2-RUNG values containing pi
the measured electron anomaly
any prior or incubation value of K
ResponseLaw, AlphaMap, MomentRate, CoefficientState, or CoefficientValueSet
any target-dependent degree or branch ledger
any internal v184-only source
any selection predicate that asks whether a value matches the target
~~~

The denylist is semantic. Rewriting \(2\pi/5\) as a turn fraction, or hiding
\(\pi\) inside a cached wall value, does not make a radian normalization
admissible. Phase A emits only a target-free exact phase-tangent leg and a
target-free algebraic Born-rate leg. Any wall closure that cannot be reduced and
certified to those target-free output carriers without a denylisted
intermediate leaves STOP-PREDEFINITION.

### 9.3 Phase B pi use

Only Phase B may specialize the formal symbol \(\Pi\) to \(\pi\), apply the
pre-frozen ResponseLaw, construct the alpha germ and coefficient, or import
QUANT-SCHWINGER-TARGET. Its use of pi must still have independent public
provenance from J-PROJECTIONS and PI-FROM-J. Rewriting
script-Q phi^2 as 2 pi is not a ResponseLaw derivation.

### 9.4 Firewall check

PhaseAFirewallChecker must verify:

1. every expression leaf has one provenance record;
2. every Phase A atom is tagged PHASE_A and every transitive source is on
   the Phase A allowlist;
3. no denylisted symbol, row, equality, cached value, or decision predicate
   enters the Phase A dependency DAG;
4. the complete S_compare_def hash, including ResponseLaw and
   AlphaMap, was public and immutable before Phase A execution but was not
   readable by Phase A;
5. the definition and execution orders were fixed before Phase A execution;
6. the Phase A artifact hash was fixed before S_compare_run executed.

Failure of any clause routes STOP-INTEGRITY. It is not a scientific miss.

## 10. Closure and raw-response types

Every constructor is total on its declared raw input. Closure and reading
failure are values, not filters:

~~~text
StreamState =
    STREAM_EXACT(stream, proof)
  | STREAM_PROVED_NONEXISTENT(proof)
  | STREAM_AMBIGUOUS(streams, witness)
  | STREAM_UNRESOLVED(reason)

ClosureState(T) =
    CLOSED_EXACT(value : T, proof)
  | PROVED_NONEXISTENT(proof)
  | AMBIGUOUS(values, witness)
  | UNRESOLVED(reason)
  | OUT_OF_SCOPE(source)

RawResponseState =
    RAW_PAIR_EXACT(phase_turn_rate, channel_Born_rate, coherence_proof)
  | RAW_PAIR_PARAMETRIC(parameters, exact_pair_family, necessity_proof)
  | RAW_PAIR_PROVED_NONEXISTENT(leg, proof)
  | RAW_PAIR_AMBIGUOUS(leg, values, witness)
  | RAW_PAIR_CONFLICT(package_overlap_witness)
  | RAW_PAIR_UNRESOLVED(reason)

RecordValidity =
    RECORD_VALID
  | RECORD_INVALID(integrity_reason)
  | RECORD_UNRESOLVED(reason)
~~~

RateState(T) is the total leg result type already frozen in section 8; this
section does not introduce a second wrapper or a coercion.

Every infinite-N statement must name its summation object, exact limit
definition, topology or eventual identity, and proof. Citing one wall value
does not prove that an arbitrary coupled stream closes. R-WALL remains owner
adoption A5. Because Phase A forbids pi-valued wall constants, a successor
must also prove that any wall-assisted construction reduces to the declared
target-free raw-response carriers without a denylisted intermediate.

For every tuple

\[
(q,r,k_s,k_a)\in
\mathrm{RawClass}\times\mathrm{ReadingFamilyClass}\times
\mathrm{SubstantiveContextKey}\times\mathrm{AuxiliaryContextKey},
\]

the package must return:

~~~text
PhaseTangentRate(q,r,k_s,k_a) : RateState(V_phase)
ChannelBornRate(q,r,k_s,k_a) : RateState(Born_rate_carrier)
RawResponseState(q,r,k_s,k_a)
~~~

The domain of each leg is the raw StreamState and context record, not an
already exact or complete response. The complement of every applicability
predicate must return a named non-success constructor. No tuple may disappear
before its CouplingRecord is serialized.

Phase A defines no MomentRate, alpha coordinate, denominator, coefficient, or
K. For every structurally admitted mandatory tuple, any nonexact raw rate,
ambiguity, conflict, or unresolved state routes STOP. A
RAW_PAIR_PARAMETRIC record remains valid only when its parameter type and
necessity are proved exactly; it is carried to the proposed Phase B
free-parameter route without selection.

## 11. Total coupling records and class completeness

Every q in RawClass receives exactly one outer record, containing one inner
record for every package and complete context key:

~~~text
CouplingRecord(q) = (
  coupling_index,
  carrier_hash,
  state_hash,
  vertex_normal_form,
  structural_state,
  stream_state,
  proposed_equivalence_orbit,
  reading_family_hash,
  package_context_table[
    package_id,
    substantive_context_key,
    auxiliary_context_key,
    phase_leg_result,
    channel_leg_result,
    leg_overlap_state,
    package_overlap_state,
    closure_states,
    raw_response_state,
    free_parameter_state
  ],
  constant_provenance_root,
  free_parameter_aggregate,
  record_validity
)
~~~

StructuralState is:

~~~text
STRUCTURAL_PASS
STRUCTURAL_FAIL(proved violated clause)
STRUCTURAL_UNRESOLVED(reason)
~~~

FreeParameterState is:

~~~text
NO_FREE_PARAMETER(proof)
PROVED_REQUIRED(parameter_type, proof)
FREE_PARAMETER_UNRESOLVED(reason)
~~~

The distinction is essential. PROVED_REQUIRED can feed the proposed future
negative route only after the separate gate fold adopts it.
FREE_PARAMETER_UNRESOLVED is STOP. At v71, the free-parameter leaf is not a
registered scoped scientific falsifier of QUANT-SUBSTRATE; it is only a
definition diagnostic.

FreeParameterState is evaluated per package and substantive context.
free_parameter_aggregate is a total exact aggregation over every mandatory
tuple and auxiliary-uniformity class. It must distinguish no parameter,
class-wide unavoidable parameter, mixed parameterized and parameter-free
realizations, and unresolved coverage. A single problematic tuple cannot be
promoted to a class-wide negative.

The complete classes are:

~~~text
RawClass
  every nontrivial index in the frozen CouplingUniverse

StructuralAdmClass
  exactly the q with STRUCTURAL_PASS under a complete target-free
  StructuralAdmPredicate frozen before any stream or response output

ClassifiedClass
  RawClass plus one total CouplingRecord per index, package, and context key

EvaluableClass
  StructuralAdmClass itself, but only when every mandatory package and
  substantive context has a valid exact or proved-parametric raw response
  and every auxiliary key has a uniformity proof
~~~

EvaluableClass is not a filtered subset created by rate success. If one
structurally admitted mandatory tuple has a missing, nonexistent, ambiguous,
conflicting, or unresolved raw response, the complete artifact routes STOP.
A failure of one favored coupling never closes the class and never authorizes
a negative result.

ClassCompletenessCertificate proves:

1. CouplingIndex is finite or otherwise effectively exhaustive;
2. RawClass equals the complete frozen nontrivial universe;
3. each raw index occurs exactly once;
4. StructuralAdmPredicate is total, predeclared, and target-free;
5. every package, substantive key, and auxiliary key occurs exactly once per
   required raw index;
6. every StructuralCheck and leg is total on its raw domain;
7. auxiliary quotienting is backed by a uniformity proof;
8. every substantive context alternative remains visible;
9. the structural equivalence orbit partition is complete;
10. no outcome, raw response, coefficient, or target value affected
    enumeration, equivalence, order, applicability, or selection;
11. every covariance and excluded action is retained;
12. every unresolved field is surfaced.

NEGATIVE-EMPTY is available only when StructuralAdmClass is proved empty by a
complete target-free StructuralAdmPredicate over all RawClass. Rate
nonexistence, missing closure, zero Phase B denominator, or an unresolved
record can never manufacture emptiness; each routes STOP.

RawResponsePairSet is the full indexed family of raw package outputs over the
structural quotient, every substantive key, and auxiliary-uniformity class.
It is not a set of successful examples.

## 12. Equality, symmetry, and quotient

The structural quotient is frozen before stream construction or any response
output. Four equalities are distinct:

~~~text
CouplingEqRaw
  exact equality of tagged indices and vertex normal forms

CouplingEq
  orbit equivalence under the complete proved equivalence group

RawResponseEq
  exact equality of the full indexed Phase A raw-response records

CoefficientEq
  exact equality in F_Pi during Phase B
~~~

The proposed symmetry inventory is:

~~~text
plain coefficient conjugation
  not the claimed state-orbit map: it fixes v_plus and the natural deposit
  basis

K_M(sum_(sigma,j) m_(sigma,j) f_sigma tensor e_j)
    = sum_(sigma,j) bar(m_(sigma,j)) f_sigma tensor e_(-j)
  explicit global semilinear candidate on the frozen tensor basis; it is not
  an ill-defined tensor of a linear and a semilinear factor

C = (Z tensor 1) composed with K_M
  candidate antiunitary after a Hermitian form is frozen; it sends v_plus to
  v_minus, preserves D_rest, and sends
  W(a,b) to W(-b,-a), not W(-a,-b); candidate semilinear structural
  equivalence only after it preserves every pre-output structural field

Cent_GL(M)(D_rest tensor 1)
  the unit group centralizing the uncoupled tick; too large by itself

Norm_W
  the intersection of Cent_GL(M)(D_rest tensor 1) with the setwise
  normalizer of the frozen tagged W class, further restricted to preserve the
  carrier tags, state context, register algebra, and every field of the
  target-free StructuralAdmPredicate frozen before quotient construction

Norm_W^semi
  an explicit semilinear extension if C is admitted

the full unit centralizer Cent_GL(M)(D_rest tensor 1)
  excluded as an equivalence definition: without structure-preservation
  restrictions it is too large and need not preserve the finite W class

u in (Z/5)^*, E_k -> E_(u k)
  genuine register automorphisms; frozen as COVARIANCE unless an owner
  pre-adopts them as structural gauge on target-free non-output grounds

field sigma_2 and sigma_3
  covariance actions, not identifications

index shifts E_k -> E_(k+c)
  excluded because they do not preserve the unit or product
~~~

ProposedEquivalenceGroup is selected from the structural inventory before
any stream or read is constructed. SymmetryStatus is one of:

~~~text
EQUIVALENCE(structural_action_and_invariance_proof)
COVARIANCE(transformation_proof)
EXCLUDED(counterexample)
UNRESOLVED(reason)
~~~

Only EQUIVALENCE actions generate CouplingEq. COVARIANCE actions remain in
the artifact and may expose different raw responses. An action's status can
never be promoted after inspecting a response or coefficient. UNRESOLVED
actions that could change class membership, context coverage, or a later
coefficient route STOP.

Grading values, package maps, context occurrences, and read outputs do not
enter Norm_W or the pre-output selection of CouplingEq. Their later descent
to the frozen quotient is a separate RawResponseTransport and
AuxiliaryUniformity obligation. Failure of descent routes STOP; it cannot
shrink, enlarge, or otherwise repair CouplingEq after outputs are known.

The Phase A proof must establish:

~~~text
Q_A = StructuralAdmClass / CouplingEq
OrbitPartitionCompleteness
RawResponseTransport
AuxiliaryUniformity
~~~

RawResponseTransport proves exact invariance, or the frozen declared
covariance, of the full package/context record. Failure routes STOP and does
not reclassify the action.

Only in Phase B, after ResponseLaw and AlphaMap are applied, may one define
the total state-valued record

\[
\mathrm{CoefficientRecord}:D_B\longrightarrow\mathrm{CoefficientState},
\qquad
D_B=Q_A\times\mathrm{ReadingFamilyClass}\times
\mathrm{SubstantiveContextKey}.
\]

The scalar map

\[
\overline K:D_B\longrightarrow F_{\Pi},
\qquad
\mathrm{CoefficientValueSet}=\operatorname{image}(\overline K)
\]

exists only under the Phase B guard proving that every mandatory
CoefficientRecord is K_EXACT with an exact nonzero denominator. A zero,
parametric, missing, ambiguous, or unresolved record leaves no such scalar
map or image to inspect; the router consumes the total state-valued records
instead.

Several inequivalent classes or substantive contexts with the same exact K
are value multiplicity. A NONUNIQUE route requires at least two exact
distinct values with witnesses. At v71 this route is a proposed owner route,
not a registered scoped uniqueness falsifier.

## 13. Phase A artifact and checker

ClassificationMode is exactly one of:

~~~text
SYMBOLIC
  a complete proof term checked by a pinned trusted kernel, with theorem
  statement and kernel hashes

FINITE_CENSUS
  exhaustive enumeration of the complete finite typed universe by the
  artifact checker

HYBRID
  a symbolic reduction to a finite residual class plus an exhaustive census
  of that residual class
~~~

ClassificationProof carries the selected mode, statement, domains,
completeness theorem, proof or census payload, checker identity, hashes, and
acceptance result. A prose assertion or self-declared certificate is not a
proof object.

PhaseAArtifact contains:

~~~text
schema_version
authority_pin
S_classify_def_hash
all source file hashes
all adopted-owner-decision hashes
ring, carrier, state, and coupling-universe hashes
definition and execution orders
complete raw index table
complete CouplingRecord table
structural symmetry action and complete orbit-partition tables
reading-package, context-partition, occurrence, and overlap tables
closure and raw-response certificates
auxiliary-uniformity certificates
RawResponseTransport
constant provenance DAG
ClassCompletenessCertificate
ClassificationMode
ClassificationProof
RawResponsePairSet
PhaseAFirewallCertificate
validity summary
PhaseAArtifactPayloadHash
~~~

It contains no comparison target, target row payload, target-derived degree
ledger, ResponseLaw, AlphaMap, MomentRate, denominator, CoefficientState,
CoefficientValueSet, comparison result, expected target match, or Phase B
outcome.

PhaseAValidityCertificate is valid exactly when:

1. the authority and every source hash match;
2. every S_classify_def field is frozen and target-independent;
3. the ClassificationProof is accepted under its frozen mode;
4. the raw class, package family, context spaces, and every record are
   complete;
5. StructuralAdmClass and the structural quotient are well-defined and their
   orbit partition is complete;
6. RawResponseTransport and auxiliary uniformity hold on every required
   record;
7. all unresolved fields are listed and no unresolved field is hidden by
   filtering;
8. the provenance and firewall checks pass;
9. PhaseAArtifactPayloadHash matches the canonical serialization of every
   preceding artifact field, with the hash field itself omitted.

PhaseAArtifactChecker is a total deterministic checker of the artifact
schema, hashes, proof object, census where required, certificates, and
internal coherence. In FINITE_CENSUS it must recompute the exhaustive census.
In SYMBOLIC it must validate the proof term through the pinned kernel. In
HYBRID it must do both on their declared domains. A hash-consistent but
scientifically unsupported ClassCompletenessCertificate is invalid. Checker
success means valid Phase A evidence, not scientific PASS.

The serialization, ordering, and normal forms must be fixed before any formal
run. Hashing a summary while leaving generated tables outside the payload is
invalid.

## 14. Phase B comparison and total outcomes

The complete S_compare_def, including ResponseLaw, AlphaMap, routing, and
target source, is hashed before Phase A executes. Phase A cannot read it.
Only after Phase A has an immutable valid artifact hash may S_compare_run
execute.

Every pre-comparison execution stage is total through the generic wrapper:

~~~text
PhaseBStageState(T) =
    STAGE_NOT_CONSTRUCTED(prior_guard_failure, proof no later stage ran)
  | STAGE_CONSTRUCTED(value : T, construction_certificate)
  | STAGE_INVALID(integrity_reason)
~~~

MappedRawResponseTableState, DenominatorStateTableState,
CoefficientRecordTableState, CoefficientInvarianceState, and
FreeParameterAggregateState are
PhaseBStageState values of their named payload types. An early invalid
Phase A readback therefore produces explicit STAGE_NOT_CONSTRUCTED values
for every later table and certificate. The PhaseBComparisonChecker enforces
dependency order: after one NOT_CONSTRUCTED or INVALID stage, no later stage
may be STAGE_CONSTRUCTED. These wrappers record execution availability; they
do not weaken the scientific RateState, DenominatorState, or
CoefficientState constructors inside a successfully constructed table.

### 14.1 Response and alpha types

~~~text
ResponseLaw : V_phase -> F_Pi

AlphaCarrier = F_Pi[alpha] / (alpha^2)
AlphaZero    = 0
AlphaEq      = coefficientwise exact equality
AlphaTangentCarrier = F_Pi
AlphaTangentZero    = 0 in F_Pi
AlphaTangentEq      = exact equality in F_Pi
AlphaMap            : Born_rate_carrier -> AlphaTangentCarrier
CommonStreamTangent = the frozen first-order stream coordinate used by both
                      the phase and channel legs

ElectronGerm =
  a_e(alpha) = a_e(0) + K alpha mod alpha^2

AlphaCoefficientExtraction(ElectronGerm) = [alpha^1] a_e(alpha)

ChainRuleCertificate:
  [alpha^1] a_e(alpha)
    = (d a_e / d CommonStreamTangent)
      / (d alpha / d CommonStreamTangent)
~~~

The candidate inherited from Rev 3 maps a phase tangent to the electron
moment response through the separately adopted delta-g law, then uses the
definition \(a_e=(g-2)/2\). No public row currently supplies that differential
law. ResponseLaw therefore remains A6, with exact domain, unit conversion,
linearity scope, and provenance required.

If \(x\in V_{\rm phase}\) is frozen in the radian-tangent coordinate, the Rev
3 candidate is

\[
\operatorname{ResponseLaw}_{A6}(x)=\frac{5x}{2\Pi}.
\]

If a successor instead proves and freezes a signed turn-rate coordinate
\(r=x/(2\Pi)\), the same candidate reads \(5r\). Those formulas are
interchangeable only after the unit conversion and its domain are proved.
Selecting the coordinate after inspecting K is forbidden.

AlphaMap must freeze how the channel Born response defines the local alpha
tangent. The excursion bookkeeping symbol t is not alpha. A4 must supply an
exact map, zero, equality, and formal first-order family; it cannot identify
t with alpha by notation. The two derivatives must use the identical
CommonStreamTangent, and the ChainRuleCertificate must prove the displayed
quotient identity before it may be called the registered alpha coefficient.

The exact maps never implicitly unwrap a RateState. For any exact function
`f : A -> B`, the frozen total lift is:

~~~text
RateMapLift(f) : RateState(A) -> RateState(B)
  RATE_EXACT(x, proof)
    -> RATE_EXACT(f(x), mapped_proof)
  RATE_PROVED_NONEXISTENT(proof)
    -> RATE_PROVED_NONEXISTENT(mapped_nonexistence_proof)
  RATE_AMBIGUOUS(values, witness)
    -> RATE_AMBIGUOUS(map(f, values), source_ambiguity_witness)
  RATE_UNRESOLVED(reason)
    -> RATE_UNRESOLVED(mapped_reason)

MomentRateConstructor : RateState(V_phase) -> RateState(F_Pi)
  = RateMapLift(ResponseLaw)

AlphaTangentRateConstructor : RateState(Born_rate_carrier)
                              -> RateState(F_Pi)
  = RateMapLift(AlphaMap)

MappedRawResponseState =
    MAPPED_PAIR_EXACT(moment_rate : F_Pi,
                      alpha_rate : F_Pi,
                      coherence_proof)
  | MAPPED_PAIR_PARAMETRIC(parameters, exact_mapped_family,
                           necessity_proof)
  | MAPPED_PAIR_PROVED_NONEXISTENT(leg, proof)
  | MAPPED_PAIR_AMBIGUOUS(leg, mapped_values, source_witness)
  | MAPPED_PAIR_CONFLICT(package_overlap_witness)
  | MAPPED_PAIR_UNRESOLVED(reason)

PhaseBRatePairConstructor : RawResponseState -> MappedRawResponseState
  RAW_PAIR_EXACT
    -> apply ResponseLaw and AlphaMap to the two exact payload values
  RAW_PAIR_PARAMETRIC
    -> apply both exact maps pointwise to the complete exact family
  RAW_PAIR_PROVED_NONEXISTENT
    -> MAPPED_PAIR_PROVED_NONEXISTENT
  RAW_PAIR_AMBIGUOUS
    -> MAPPED_PAIR_AMBIGUOUS; no image collapse resolves source ambiguity
  RAW_PAIR_CONFLICT
    -> MAPPED_PAIR_CONFLICT
  RAW_PAIR_UNRESOLVED
    -> MAPPED_PAIR_UNRESOLVED

DenominatorState =
    NONZERO_EXACT(alpha_rate, proof)
  | ZERO_EXACT(proof)
  | PARAMETRIC_NONZERO_DOMAIN(parameters, exact_domain, proof)
  | UNRESOLVED(reason)

DenominatorStateConstructor : MappedRawResponseState -> DenominatorState
  MAPPED_PAIR_EXACT(moment_rate, alpha_rate, coherence_proof)
    -> decide AlphaTangentEq(alpha_rate, AlphaTangentZero) exactly;
       return ZERO_EXACT or NONZERO_EXACT with the corresponding proof
  MAPPED_PAIR_PARAMETRIC(parameters, exact_mapped_family, necessity_proof)
    -> PARAMETRIC_NONZERO_DOMAIN only with an exact complete parameter
       domain and proof that every admitted alpha_rate is nonzero;
       otherwise UNRESOLVED
  every nonexact MAPPED_PAIR constructor
    -> UNRESOLVED(source_constructor_witness)

DenominatorCoefficientInput =
  dependent triples (s, d, coherence) where
    s : MappedRawResponseState,
    d : DenominatorState, and
    coherence proves d = DenominatorStateConstructor(s)

CoefficientState =
    K_EXACT(MomentRate / AlphaTangentRate, proof)
  | K_PARAMETRIC(parameters, exact_family, necessity_proof)
  | K_UNDEFINED_ZERO_DENOMINATOR(proof)
  | K_UNDEFINED_MISSING_OR_AMBIGUOUS_INPUT(reason)

CoefficientRecordConstructor : DenominatorCoefficientInput
                               -> CoefficientState
  MAPPED_PAIR_EXACT with coherent NONZERO_EXACT
    -> K_EXACT(moment_rate / alpha_rate, proof)
  MAPPED_PAIR_EXACT with coherent ZERO_EXACT
    -> K_UNDEFINED_ZERO_DENOMINATOR(proof)
  MAPPED_PAIR_EXACT with coherent UNRESOLVED
    -> K_UNDEFINED_MISSING_OR_AMBIGUOUS_INPUT(reason)
  MAPPED_PAIR_PARAMETRIC with coherent PARAMETRIC_NONZERO_DOMAIN
    -> K_PARAMETRIC(parameters, exact_family, necessity_proof)
  MAPPED_PAIR_PARAMETRIC with coherent UNRESOLVED
    -> K_UNDEFINED_MISSING_OR_AMBIGUOUS_INPUT(reason)
  every nonexact MAPPED_PAIR constructor with its coherent denominator state
    -> K_UNDEFINED_MISSING_OR_AMBIGUOUS_INPUT(source_constructor_witness)
~~~

For every structural quotient class, package, and substantive key, Phase B
applies PhaseBRatePairConstructor exactly once to the frozen
RawResponseState. Every input constructor therefore has one explicit output
constructor. The source-ambiguity branch remains non-success even if its
mapped numerical values happen to coincide; resolving it would require a
separately frozen reading-equivalence proof before execution.

Writing

\[
D_B=Q_A\times\mathrm{ReadingFamilyClass}\times
\mathrm{SubstantiveContextKey},
\]

Phase B must construct exactly one total

\[
\mathrm{CoefficientRecord}:D_B\longrightarrow\mathrm{CoefficientState}.
\]

The guard `all_mandatory_coefficients_exact_with_nonzero_denominators`
contains a witness $k_d\in F_{\Pi}$ and an equality
`CoefficientRecord(d) = K_EXACT(k_d, proof_d)` for every $d\in D_B$.
Only under that guard is

\[
\overline K(d)=k_d,
\qquad
\mathrm{CoefficientValueSet}=\{\overline K(d):d\in D_B\}
\]

well-defined. No partial scalar map, filtered domain, or image of only the
successful records is permitted.

The total outer serialization state is:

~~~text
CoefficientValueSetState =
    VALUE_SET_EXACT(CoefficientValueSet, image_proof, payload_hash)
  | VALUE_SET_NOT_CONSTRUCTED(prior_stage_or_exact_guard_failure)
~~~

VALUE_SET_NOT_CONSTRUCTED contains no scalar map, filtered image, or target
value. It exists only so the Phase B record is total before the router sends
the failed guard to its authorized non-image route.

K_EXACT is constructed only after exact nonzero proof. Symbolic cancellation
before that proof is forbidden. In this revision, ZERO_EXACT, a missing raw
rate, an ambiguous package, or an unresolved denominator always routes STOP.
None may be reclassified as coupling nonexistence or used to manufacture an
empty class.

FreeParameterAggregate is:

~~~text
FP_NONE_COMPLETE(proof every required realization is parameter-free)

FP_CLASS_REQUIRED(
  proof the complete nonempty structurally admitted class has no
  parameter-free realization and a new dimensionless parameter is unavoidable
)

FP_MIXED(parameterized_witness, parameter_free_witness)

FP_UNRESOLVED(reason)
~~~

One parameterized candidate does not falsify the existence of another
parameter-free realization. Only FP_CLASS_REQUIRED can inhabit the proposed
NEGATIVE-FREE-PARAMETER route. FP_MIXED and FP_UNRESOLVED route STOP unless a
future owner fold supplies a different exact class-level rule.

### 14.2 Target import

After the response and alpha maps are fixed and the Phase A artifact is
validated, S_compare_run imports:

~~~text
comparison source:  QUANT-SCHWINGER-TARGET [T]
comparison value:   J Jbar / script-Q = 1/(2 pi)
comparison scope:   exact arithmetic scalar only
comparison ring:    F_Pi under the exact identification Pi <-> pi
~~~

target_embedding must be an explicit injective exact map into the common
comparison ring. Numerical approximation, tolerance, decimal agreement, or
symbol-name agreement is forbidden. ExactEq and ExactNeq must be decidable,
complementary, and exhaustive on the admitted normal forms.

The PhaseBRunRecord uses these total access and comparison states:

~~~text
TargetAccessState =
    TARGET_UNREAD(proof no target payload entered the run prefix)
  | TARGET_IMPORTED(source_hash, embedding_readback)

ComparisonState =
    COMPARISON_NOT_RUN(pretarget_route_guard, TARGET_UNREAD)
  | COMPARISON_EXACT_EQ(coefficient, target, TARGET_IMPORTED, ExactEq)
  | COMPARISON_EXACT_NEQ(coefficient, target, TARGET_IMPORTED, ExactNeq)
  | COMPARISON_INVALID(integrity_reason, TargetAccessState)
~~~

COMPARISON_NOT_RUN is mandatory for a pre-target STOP,
NEGATIVE-EMPTY, NEGATIVE-FREE-PARAMETER, or NONUNIQUE route and proves that
the target payload was unread. COMPARISON_INVALID can inhabit only STOP and
records whether the failure occurred before or after target import. PASS and
NEGATIVE-MISS require respectively COMPARISON_EXACT_EQ and
COMPARISON_EXACT_NEQ. Bare null, an implicit N/A witness, or a fabricated
comparison value is invalid.

### 14.3 Guarded outcome partition

The terminal outcome is a dependent sum with exactly six constructors:

~~~text
STOP(
  invalid_or_unresolved_certificate,
  proof no scientific constructor is authorized
)

NEGATIVE-FREE-PARAMETER(
  valid_PhaseA_certificate,
  StructuralAdmClass_nonempty,
  FP_CLASS_REQUIRED,
  prior_guard_negations
)

NEGATIVE-EMPTY(
  valid_PhaseA_certificate,
  StructuralAdmClass_empty_proof,
  prior_guard_negations
)

NONUNIQUE(
  valid_PhaseA_certificate,
  StructuralAdmClass_nonempty,
  FP_NONE_COMPLETE,
  all_mandatory_coefficients_exact_with_nonzero_denominators,
  coefficient_image_cardinality_at_least_two,
  K_1, K_2,
  exact_inequality_proof,
  witness_classes_and_contexts,
  prior_guard_negations
)

PASS(
  valid_PhaseA_certificate,
  StructuralAdmClass_nonempty,
  FP_NONE_COMPLETE,
  all_mandatory_coefficients_exact_with_nonzero_denominators,
  coefficient_image_singleton_certificate,
  unique_coefficient_value,
  exact_equality_to_target,
  prior_guard_negations
)

NEGATIVE-MISS(
  valid_PhaseA_certificate,
  StructuralAdmClass_nonempty,
  FP_NONE_COMPLETE,
  all_mandatory_coefficients_exact_with_nonzero_denominators,
  coefficient_image_singleton_certificate,
  unique_coefficient_value,
  exact_inequality_to_target,
  prior_guard_negations
)
~~~

RoutingState is computed once by this guarded priority:

1. any invalid pin, schema, source, proof, completeness, provenance,
   isolation, context coverage, package, closure, raw rate, quotient,
   transport, denominator, map, or certificate routes STOP;
2. with a valid Phase A certificate, an exactly empty StructuralAdmClass
   routes NEGATIVE-EMPTY;
3. with a nonempty StructuralAdmClass, FP_CLASS_REQUIRED routes
   NEGATIVE-FREE-PARAMETER; FP_MIXED or FP_UNRESOLVED routes STOP;
4. with FP_NONE_COMPLETE, every mandatory coefficient record must be exact
   with nonzero denominator; otherwise STOP;
5. an exact coefficient-image cardinality at least two routes NONUNIQUE;
6. an exact singleton image is compared with the target and routes PASS or
   NEGATIVE-MISS through complementary ExactEq or ExactNeq;
7. every uninhabited, contradictory, or uncovered state routes STOP.

RoutingPartitionCertificate proves coverage, mutual exclusion, priority, and
the negation of every earlier guard carried by a later constructor. An input
that supplies incompatible certificates is invalid and routes STOP. There is
no Cartesian claim of 32 or 64 boolean states. PhaseBComparisonChecker proves
that exactly one constructor is inhabited and checks every attached
certificate.

PASS is a target-isolated postdiction. It is not a blind prediction because
the registered target predates this definition. No priority claim follows
from any outcome.

NEGATIVE-FREE-PARAMETER and NONUNIQUE are proposed owner routes, not current
v71 scientific falsifiers. They become scientific only if the separate
Canon/gate fold explicitly freezes their scopes, class, equality, and
decision conditions. Until then all six labels in this note are definition
constructors only.

## 15. Definition and execution order

The immutable classification definition order is:

~~~text
01 authority and source tables
02 owner-adoption ledger
03 ring normal forms and equality
04 carrier universe and complete carrier class
05 state universe and complete state class
06 tagged coupling universe and complete raw index order
07 pre-output target-free schemas for action inputs and outputs, stream and
   grading types, context-key types, and package domains and codomains; no
   stream, map, read, rate, or coefficient output
08 total target-free StructuralAdmPredicate on already frozen structural
   fields
09 structural symmetry inventory, ProposedEquivalenceGroup, and CouplingEq
10 complete structural orbit partition
11 coupled one-tick action, stream constructor, and excursion-grading maps
12 context-key partition, occurrence or selection, and auxiliary keys
13 reading-package family, leg maps, equality, and overlap
14 closure resources and rules
15 constant provenance rules and Phase A denylist
16 raw phase-tangent and Born-channel rate definitions
17 total raw-response and CouplingRecord schemas
18 RawResponseTransport and auxiliary-uniformity proofs; failure cannot
   revise step 09
19 ClassificationMode, ClassificationProof, and completeness certificate
20 RawResponsePairSet serialization and Phase A checkers
~~~

The execution order is the lexicographic order of the frozen tagged coupling
indices, followed by the frozen check and read orders. Parallel execution is
permitted only if the serialized result is provably identical. No adaptive
ordering based on partial coefficient values is allowed.

The comparison definition order is:

~~~text
01 validate the precommitted S_compare_def_hash
02 read and validate the exact Phase A artifact hash
03 apply the frozen ResponseLaw and AlphaMap uniformly to every raw pair
04 construct the total DenominatorState table from the mapped-response table;
   prove every denominator used for division nonzero
05 construct total Phase B coefficient records only from coherent
   DenominatorCoefficientInput triples produced by steps 03--04
06 prove coefficient transport on the frozen structural quotient
07 aggregate the class-level free-parameter state; only under
   all_mandatory_coefficients_exact_with_nonzero_denominators construct
   Kbar and freeze the complete CoefficientValueSet with a payload hash;
   otherwise serialize VALUE_SET_NOT_CONSTRUCTED without a scalar image
08 route STOP, structural EMPTY, class-required free parameter, and
   NONUNIQUE without reading the target value
09 import QUANT-SCHWINGER-TARGET and the exact embedding only for a valid
   singleton coefficient image
10 compare through complementary ExactEq or ExactNeq
11 serialize one RoutingPartitionCertificate, Phase B certificate, and
   terminal outcome
~~~

## 16. Future gate-row proposal

The following rows are proposals only. They are absent from Public Canon v71.
Tabs shown below are schema fields, not an edit to canon/GATES.tsv.

~~~text
gate_id                             owner_item_id    from_layer  to_layer  gate_kind  decision_condition
GATE-L1-L5-QS-COUPLING-STREAM      QUANT-SUBSTRATE L1          L5        OPEN_LIFT  emits one immutable exact target-free L5 stream and raw-response artifact only when the complete frozen carrier, state, structural class, structural quotient, path decomposition, excursion grading, package family, context coverage, and Phase A certificates are valid for every raw coupling; a complete structurally empty class emits an EMPTY-STREAM record for the downstream gate and is not itself an L6 scientific outcome; any ambiguity, incompleteness, unresolved overlap, failed mandatory raw response, or target-dependent choice routes STOP
GATE-L5-L6-SCHWINGER-TERM          QUANT-SUBSTRATE L5          L6        OPEN_LIFT  consumes only a valid immutable target-free Phase A artifact and uniformly applies the precommitted ResponseLaw and AlphaMap; closes positively exactly when the complete nonempty structural quotient has one exact nonzero-denominator coefficient value equal to QUANT-SCHWINGER-TARGET; closes negatively on an exact miss and, only at the scopes explicitly adopted by this fold, a complete structural EMPTY, a class-wide proved unavoidable free dimensionless parameter, or at least two exact distinct coefficient values; any missing raw response, mixed or unresolved parameter state, zero or unresolved denominator, incomplete quotient, or certificate failure routes STOP
~~~

Under parent-owned topology option 2 below, the same fold must change the
QUANT-SUBSTRATE NORMATIVE row to:

~~~text
layer:     NOT_APPLICABLE
gate_ids:  GATE-L1-L5-QS-COUPLING-STREAM;GATE-L5-L6-SCHWINGER-TERM
~~~

Both proposed rows use the closed gate kind OPEN_LIFT and the existing
OBLIGATION/O owner. Their endpoints are distinct concrete protocol layers.
Because the owner layer is NOT_APPLICABLE, the gate checker permits the two
different target layers. The actual future fold must still pass the then
current tools/check_gate_contract.py and every repository check.

The first gate is target-free. The second gate alone consumes the target.
Neither gate may be simulated by a note, a branch name, or an unregistered
verifier.

These are only the Schwinger subpipeline. Public QUANT-SUBSTRATE also names a
separate Larmor gate. The two rows cannot by themselves type or close the
whole parent obligation. Before a gate fold, the owner must choose one exact
topology:

1. create a separately registered Schwinger child obligation to own these two
   rows, while the QUANT-SUBSTRATE parent and Larmor branch remain open; or
2. keep QUANT-SUBSTRATE as owner of the displayed rows and, in the same
   reviewed topology program, type every missing Larmor gate and the parent
   aggregation rule.

The displayed NORMATIVE gate_ids edit applies only to option 2. Under option
1 the child owner row, parent dependency, and gate ownership require a fresh
exact proposal. No READY-DEFINITION decision is possible while this topology
choice is unresolved.

## 17. Acceptance test for READY-DEFINITION

This lane may move from STOP-PREDEFINITION to READY-DEFINITION only if all
answers below are YES against one immutable definition hash:

| Test | Required proof |
| --- | --- |
| authority | current public Canon and all source rows are exact-pinned |
| carrier | complete nonempty carrier and state classes are frozen |
| dispositions | every class is GLOBAL-CLASS, FORCED-SELECTION, OWNER-ADOPTED, or explicitly non-closing ANSATZ-ONLY |
| ring | exact normal forms, equality, embeddings, and inverted-prime scope are frozen |
| coupling | tagged universe and complete raw class are frozen |
| nondegeneracy | PREDEF-BLOCKER-QS-1 is repaired by a target-independent exact construction |
| action | exact coupled one-tick operator, operator order, and stream constructor are frozen |
| stream | exact total path decomposition and excursion grading are defined |
| contexts | substantive and auxiliary spaces, occurrence or selection, and auxiliary uniformity are complete |
| readings | both total legs, package composition, domain, codomain, equality, partiality, and package overlaps are complete |
| response law | every physical response beyond public rows is explicitly adopted |
| alpha | carrier, zero, equality, channel map, germ, and coefficient extraction are frozen |
| normalization | exact normalization scope and totality are proved |
| closure | every admitted stream is exactly closed or receives a total resolved state |
| provenance | every constant has a complete source DAG |
| isolation | Phase A transitively excludes the entire denylist |
| records | every raw coupling, package, and complete context key has one total raw-response record |
| denominator | AlphaTangentRate is proved nonzero before each quotient |
| symmetry | every possible class-changing action is equivalence, covariance, excluded, or resolved |
| quotient | structural CouplingEq is pre-output; raw transport and Phase B K invariance are proved |
| completeness | ClassificationMode proof, raw class, contexts, records, orbit partition, raw-pair set, and Phase B value set are complete |
| certificates | both artifact checkers are total, sound, and deterministic |
| outcomes | the six constructors and validity-first routing are frozen |
| gates | owner has approved the Schwinger rows plus an exact child-or-parent/Larmor topology |
| D0 discipline | explicit owner ANO names every adoption against the exact hash |

One NO or UNRESOLVED answer leaves STOP-PREDEFINITION. A favored example,
successful local calculation, or target match cannot substitute for any
row.

## 18. Required owner decisions

The next owner readback must answer each item separately:

~~~text
OD1  adopt, replace, or reject A' = Z[zeta_5,i][1/10]
OD2  adopt, replace, or reject M_D tensor A'[Z_5] as the complete carrier
OD3  adopt, replace, or reject the 24 nontrivial deposit-pair vertices as
     the complete coupling universe
OD4  adopt, replace, or reject z = 1 and the specified antiunitary state
     orbit as the complete state context
OD5  adopt, replace, or reject the exact excursion grading
OD6  adopt, replace, or reject the read-package family, context partition,
     and occurrence or selection rules
OD7  explicitly adopt or reject the delta-g response law A6
OD8  adopt, replace, or reject one excursion as the alpha coordinate
OD9  adopt, replace, or reject the normalization scope
OD10 adopt, replace, or reject the wall as the complete closure resource
OD11 approve the constant allowlist, denylist, and provenance rule
OD12 approve the total-record treatment of missing raw rates and zero
     AlphaTangentRate
OD13 approve the symmetry and covariance classification contract
OD14 approve value multiplicity versus coefficient nonuniqueness
OD15 approve the six-constructor terminal outcome type
OD16 approve the exact L1 -> L5 -> L6 Schwinger proposal and choose a
     Schwinger child or complete parent/Larmor topology
OD17 approve the Phase A / Phase B hash and leakage firewall
OD18 adopt, replace, or reject the exact coupled one-tick operator, operator
     order, stream constructor, and target-free repair of
     PREDEF-BLOCKER-QS-1
~~~

An ANO that omits an item is partial and produces a successor revision. It
does not authorize a preregistration.

## 19. Current definition decision

The current decision is:

~~~text
STOP-PREDEFINITION
~~~

Reasons:

1. A1 through A11 remain unratified owner adoptions.
2. The retained Rev 3 action-state pair has the exact degeneracy
   PREDEF-BLOCKER-QS-1.
3. The carrier, state, reading family, normalization, and closure
   completeness proofs do not yet exist at public scope.
4. No exact target-independent per-coupling record or class-completeness
   certificate exists.
5. The two Schwinger gates are absent from v71 and the parent/Larmor topology
   is unresolved.
6. No immutable Phase A schema implementation or checker exists.

This is a definition-stage disposition, not a scientific outcome and not a
change to QUANT-SUBSTRATE [O].

## 20. Future formal lane, still forbidden

The earliest safe formal order is:

1. explicit point-by-point owner ANO against the immutable Rev 4 definition
   hash;
2. a separate public Canon fold adding both Schwinger gate rows under the
   approved child-or-parent topology, typing the remaining parent/Larmor
   route, and adding the correct owner gate_ids, followed by a fresh public
   readback;
3. a fresh collision scan and exact object lock for a new probe identifier;
4. public PREREG.md and accepted verify.py committed and pushed before any
   formal gate execution;
5. static checks only before the immutable pin;
6. formal exact run after the pin, with all terminal outcomes first class;
7. byte-identical stdout on two architectures for any computation-only
   theorem claim;
8. one sealed result fold; no repair in place after execution.

No file in the Rev 1, Rev 2, or Rev 3 incubation lineage may be treated as
the pin. No existing draft verifier may be run as a formal gate.

## 21. Debt firewall

This note creates no Canon, Registry, NORMATIVE, GATES, DEPENDENCIES,
EVIDENCE, HISTORY, or Frontier debt. It introduces no public claim identifier,
probe identifier, apparatus, measurement, measured match, or priority
statement. It does not narrow the Larmor branch of QUANT-SUBSTRATE and does
not claim that the Schwinger branch is the only possible substrate question.

Any promotion must cite the exact future definition hash, preserve every
public source limitation, separate owner adoptions from registered
consequences, and carry the target-isolation firewall into the formal
preregistration without weakening it.
