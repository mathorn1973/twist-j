# C-DECODER-POINTED-BATCH-1: pointed mathematical decoder candidate

**NON-CANONICAL / CANDIDATE MATHEMATICAL IMPLEMENTATION / PHYSICAL COMPLETION UNRESOLVED**

This document specifies one executable mathematical model in response to the
author's instruction to construct a decoder and record the necessary choices.
The choices below are proposed definitions for this candidate. They are not
public scientific promotions, physical realization certificates, or a claim
that the Canon completion contract has been satisfied.

```text
document_id:           C-DECODER-POINTED-BATCH-1
candidate_id:          DECODER-POINTED-BATCH-1
source_main:           1a58703ec17a4c031bb8c450f56162f5aa3e5e5a
source_state:          ACTIVE
source_canon:          Public Canon v76
source_authority:      mathorn1973/twist-j main
source_tag:            canon-v76
source_content:        07910adb8418742bf52a0d204577b84b38009b18
source_canon_sha256:   c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112
source_canon_bytes:    420539
intended_probe:        P-DECODER-POINTED-BATCH-CONFORMANCE-1
scientific_status:     NONE ASSIGNED BY THIS NOTE
physical_completion:  UNRESOLVED
```

The intended formal source package is
`probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/`, containing `kernel.py`,
`geometry.py`, `apparatus.py`, `decoder.py`, and `verify.py`, together with its
own preregistration and subsequent evidence. This note is not that pin, a
verifier execution, or a result. The package must freeze its accepted source
before any formal execution. Existing results used here are disclosed inputs;
conformance to deliberately chosen maps is not a blind prediction.

## 1. Scope and design choices

The model has all three functional stages and all three reading legs. Its
target is an exact, causal, prefix-total mathematical readout on the specified
pointed source family. It includes an anchored QDD record, a five-cell batch
model, two separate finite Maxwell constructions, and a selected finite-support
photon recurrence. It does not identify these carriers merely because their
data originate from the same four source coefficients.

The following identifiers name candidate choices, not additional Canon claims.

| Choice ID | Definition selected for this candidate |
|---|---|
| `CH-PB-POINTED-OMEGA` | Admit every head `(n0,x)` in `N_0 x F_5^6`; retain the head and ordered forward trajectory. |
| `CH-PB-HEAD-QDD-ADAPTER` | Read QDD from the initial checkpoint through the explicit zero-counter reanchoring map; retain its exact five-field schema. |
| `CH-PB-READING-LEGS` | Retain the trace and binary cuts as distinct readings; assign each additional candidate output to an explicit leg or auxiliary role. |
| `CH-PB-CENTERING` | Send the balanced four-vector `v` to `d=5(v,0)-(sum v)1` in the five-cell augmentation lattice. |
| `CH-PB-A-CLOCK` | Use one integral `A` step per elapsed decoder cut, beginning with `A^0 d`; this is a calibration choice, not a U/A intertwiner. |
| `CH-PB-FULL-BATCH` | Prepare fresh reduced fibres and the complete within-cell Cartesian pair relation at every cut; emit it as one atomic mathematical batch. |
| `CH-PB-ZERO` | Emit an explicit zero event for a zero preparation, with no pairs and no normalized ratio. |
| `CH-PB-TESSERACT-INJECTION` | Place four head coefficients on the four marked tesseract edges specified in section 5. |
| `CH-PB-TORUS-INJECTION` | Independently place those coefficients on four marked faces of the periodic four-torus. |
| `CH-PB-PHOTON-SEED` | Load four specified D3 sites and choose equal initial two-slice wave data. |
| `CH-PB-TIME-ORIGIN` | Distinguish elapsed cut `t` from absolute counter `n=n0+t`; report exact turns `n/5` as the selected clock coordinate. |
| `CH-PB-HISTORY` | Retain the source header, ordered immutable records and literal field equality; no tail, phase, sign, permutation or saturation quotient. |
| `CH-PB-NO-FEEDBACK` | Readouts write only the candidate output history and apparatus scratch state; the kernel update remains exactly U. |
| `CH-PB-PHYSICAL-BOUNDARY` | Treat batches, fields, currents and wave values as mathematical data; no physical occurrence or L6 reading is asserted. |

No claim of uniqueness among other choices is made. In particular, selecting
a family by definition does not prove that it exhausts the admissible physical
apparatuses or all possible decoder readings.

## 2. Source, equality and finite-prefix interface

Use the registered autonomous kernel, with canonical residue representatives
`0,1,2,3,4` for checkpoint coordinates:

```text
Omega = N_0 x F_5^6,
theta_n = s_2(n) mod 2,
z_6(x) = sum_i x_i mod 5,
sigma(n,x) = z_6(x) + 2 theta_n mod 5,
U(n,x) = (n+1, g_sigma(n,x)(x)),
(g_0,g_1,g_2,g_3,g_4) = (a,b,c,d,e).
```

For `s=(n0,x)` define `kappa_s(t)=U^t(s)` for `t>=0`, and set

```text
K_pointed = {kappa_s : s in Omega},
Eq_pointed(kappa_s,kappa_s') iff s=s',
Head(kappa_s)=s,
Eval(kappa_s,t)=U^t(s).
```

These are pointed sequences with their distinguished initial term. They are
not classes modulo a common tail. Equality follows from equality of heads,
not from an unknown-time checkpoint comparison. The public `K_QDD` includes
into this candidate by `kappa_x -> kappa_(0,x)`; no equality `K_QDD=K_pointed`
or new public meaning for the Canon's general symbol `K` is inferred.

The callable interface `Decoder(s).prefix(L)` produces exactly `L` cuts,
numbered `0,...,L-1`, for every nonnegative integer `L`. At `L=0` it returns
the source header and an empty frame tuple. Its mathematical target is a
family `H_L(s)` satisfying

```text
length(H_L(s).frames)=L,
H_L(s).frames[:M]=H_M(s).frames          for 0<=M<=L.
```

The compatible family defines an infinite history mathematically. No finite
call is required to materialize an infinite list. Each output history retains
the literal source header `s` and the fixed candidate version. Canonical
generated histories with the same header use the same deterministic rules;
their complete equality is decided by the header. This equality convention
retains auxiliary source provenance. It is not reconstruction of the source
from physical observations alone.

## 3. Matter stage and the registered quadratic restriction

Write the initial checkpoint as
`x=(p1,p4,p1p,p4p,q,r)` and set

```text
ell(0,1,2,3,4)=(0,1,2,-2,-1),
v=(ell(p1),ell(p4),ell(p1p),ell(p4p)) in {-2,-1,0,1,2}^4,
Anchor0(kappa_(n0,x))=kappa_(0,x).
```

`Anchor0` is a candidate source adapter. It changes the counter in a readout
source representation; it does not reset U, reconstruct an earlier physical
state, or claim that the reanchored future equals the original future.

The anchored quadratic output is exactly

```text
qdd_anchor = D_QDD_direct(Anchor0(kappa_(n0,x))).
```

Its five fields remain precisely
`support_state`, `total_weight`, ordered `branch_weights=(LOW,HIGH)`,
`density_state`, and `normalized_weight_state`, with the Canon's tagged
ZERO branch. The direct definition uses `R_cyc`, `iota_B0` and the balanced
piston map. The factor-side expression is a comparison, not its definition:

```text
G=I_4-11^T/5,
m=v^T G v,
E_low=11^T/4,  E_high=I_4-E_low,
w_low=v^T G E_low v,  w_high=v^T G E_high v,
density=vv^T G/m,
normalized_weights=(w_low/m,w_high/m)       when m>0.
```

When `v=0`, the output is
`(ZERO_SUPPORT,0,(0,0),ZERO_DENOMINATOR,ZERO_DENOMINATOR)` and no division
is performed. No sixth field is added to `MatterData_QDD`.

The implementation represents semantic `DENSITY(matrix)` by the frozen
Python `Density(matrix)` class, and `NORMALIZED(weights)` by
`Normalized(weights)`. JSON uses the corresponding explicit `type` values
`Density` and `Normalized`. Decoding these tags restores the Canon's
semantic record. This is a declared encoding equivalence, not literal
equality of different tag spellings. Matrix and pair payloads remain parts
of the existing density and normalized-weight fields.

At `n0=0` this is the exact existing quadratic restriction. At other heads
the same formula is an explicitly chosen extension through `Anchor0`; its
global-domain interpretation is not inherited from `ALGEBRAIC-DMATTER`.
Later checkpoints do not replace the initial piston in this anchored record.

The separate linear and binary readings at cut `t` use
`(n_t,x_t)=Eval(kappa_s,t)`:

```text
trace4_t = sum(first four coordinates of x_t) mod 5,
theta_t = s_2(n_t) mod 2,
```

The trace character is the registered CODEC-TR4 observable. Its multiplier
identity concerns M_J and is not asserted for arbitrary U transitions.
The binary cut is not the coin selector `beta_1`, a Born multiplier, or a
physical event-frequency law.

## 4. Integral plenum and atomic batch

Let `g e_k=e_(k+1 mod 5)`, `N=11^T`, and

```text
V_Z={d in Z^5 : sum d_k=0},
d(v)=5(v_0,v_1,v_2,v_3,0)-(sum_i v_i)1,
A=I+g^2-g^3-g^4,
a_t=A^t d(v).
```

This centering map has a specified image in `V_Z`; it is not an identification
of the 625 balanced pistons with every integral augmentation vector. The
compatibility identities to audit are

```text
q(d(v))=25 v^T G v,
q(Aa)=5q(a) for a in V_Z,
q(a_t)=5^t q(d(v)).
```

The counted input is `a_t`. The generally nonintegral `U5^t d(v)` is only a
normalized-profile comparison. Raw `J_reg` and the positive polar factor `B`
are not count inputs. No relation `beta(U^t s)=A^t beta(s)` is assumed.
In particular, a zero initial piston keeps this anchored batch preparation
zero even if the separate U trajectory later has a nonzero piston.

For each cell, form fresh signed fibres

```text
U_k^+(a)={(k,+,i):1<=i<=max(a_k,0)},
U_k^-(a)={(k,-,i):1<=i<=max(-a_k,0)},
U_k(a)=U_k^+(a) disjoint-union U_k^-(a),
C_k(a)=U_k^S(a) x U_k^R(a),
C(a)=disjoint-union_(k=0)^4 C_k(a).
```

`S` and `R` are disjoint role tags. Every nonempty cell fibre has one sign.
The mathematical batch at cut `t` is the whole `C(a_t)`, with cell counts
`a_(t,k)^2` and total `q(a_t)`. This complete-incidence rule is a candidate
choice. The two marginals or their Gram contraction do not force it.

One interaction emits one complete batch, including an explicit `ZERO_EVENT`
when `a_t=0`. Its ratio is then the tag `ZERO_DENOMINATOR`. For nonzero
`a_t`, the exact rational five-tuple is `a_(t,k)^2/q(a_t)`. It is a finite
cardinality ratio, not an observed frequency or L6 probability. It is distinct
from QDD's two LOW/HIGH branch weights.

A batch may be represented compactly by its coefficients and the exact
Cartesian comprehensions. Passive indexing uses zero-based lexicographic
order on `(cell,i,j)`, with fibre ordinals starting at one. It returns the
corresponding immutable tagged pair. Indexing or rereading a pair emits no new
interaction and does not turn a simultaneous batch into a temporal sampler.
Signed reduction occurs before preparation; XOR-style activation or passive
enumeration does not perform interference.

The mathematical apparatus interface has these types:

```text
SourceId=(n0,x),  Checkpoint=(n,x),
Support=(source_id,relative_cut,checkpoint,a),
Controller=(next_cut,optional_cached_batch),
ReadyState={EMPTY_READY},
ContextKey={fixed_candidate_profile_and_marked_basis},
Outcome={BATCH_EVENT,ZERO_EVENT}.
```

`prepare` validates the head piston and creates cut zero. `step` emits the
current batch, advances `a` by A, increments the relative cut, and accepts the
next checkpoint only from the separately checked U transition. The apparatus
does not choose a kernel update. `persist` agrees with the next controller
returned by `step`. `reset` clears the cached batch and returns `EMPTY_READY`
without rewinding its cut or erasing history. A new preparation is distinct
from reset. `append` accepts only the same source and consecutive cuts starting
at zero. These laws define one mathematical family; they do not prove physical
apparatus-class completeness, target independence, or realized occurrence.

## 5. Geometry stage: three explicitly separate constructions

All geometry injections below use the initial balanced vector `v`. They do
not use a target frequency, an output-selected embedding, or a later batch.
Sharing `v` is a declared dependency, not a carrier isomorphism.

### 5.1 Tesseract cochains

Use the marked unit tesseract with vertices `{0,1}^4`, axes `0,1,2,3`,
and integral cochains. Cells are ordered first by lexicographic base vertex,
then by increasing active axes. An edge `(b,i)` has `b_i=0`; a face
`(b,i,j)`, `i<j`, has `b_i=b_j=0`. There are 32 edges and 24 faces.

Let `e_i` denote the standard coordinate vector. The chosen edge cochain has
only

```text
A_edge(e_1,0)=v_0,
A_edge(e_2,0)=v_1,
A_edge(e_3,0)=v_2,
A_edge(e_2,1)=v_3
```

nonzero assigned positions. Define

```text
F(b,i,j)=A_edge(b+e_i,j)-A_edge(b,j)
         -A_edge(b+e_j,i)+A_edge(b,i).
```

This is the ordinary cubical coboundary with explicit orientation. The
intended checks include `dF=0` and
`(F(0,0,1),F(0,0,2),F(0,0,3),F(0,1,2))=-v`.
The output is tagged `TESSERACT_3_PLUS_1_INTEGER`.

### 5.2 Periodic torus chains

Independently use the periodic `2^4` cubical torus with vertices `{0,1}^4`.
An oriented edge `(b,i)` ends at `b+e_i mod 2`; every vertex admits all
directions and increasing direction pairs. There are 64 edges and 96 faces.
The face boundary is

```text
partial2(b,i,j)=(b+e_i,j)-(b,j)-(b+e_j,i)+(b,i),
```

with periodic addition. Choose the face chain G to have only

```text
G(0,0,1)=v_0, G(0,0,2)=v_1,
G(0,0,3)=v_2, G(0,1,2)=v_3.
```

Set `j=partial2 G`. The intended conservation and obstruction checks are
`partial1 j=0` and zero winding across each of the four periodic seams.
This output is tagged `PERIODIC_TORUS_2_POWER_4_INTEGER`. The torus face
chain G is not identified with the tesseract cochain F, and no physical
constitutive law relating them is supplied.

The static record types are

```text
TesseractRecord(carrier_tag, edge_A:Z^32, face_F:Z^24),
TorusRecord(carrier_tag, face_G:Z^96, current_j:Z^64),
GeometryRecord(source:Z^4, tesseract:TesseractRecord, torus:TorusRecord).
```

### 5.3 Selected D3 photon recurrence

Use the separate spatial carrier
`D3={y in Z^3 : y_0+y_1+y_2 is even}` and finitely supported rational
functions on it. Set

```text
(y_0,y_1,y_2,y_3)=((0,0,0),(1,1,0),(1,0,1),(0,1,1)),
psi_0=sum_(j=0)^3 v_j delta_(y_j),
psi_1=psi_0.
```

Both the four-site injection and the equal-slice preparation are choices.
For the complete symmetric D3 shells of squared norms `2,4,8,10,16`, take
weights `6,1,15,1,1` and define

```text
(A_F0 f)(y)=(1/324) sum_(shell n, displacement r) w_n (f(y)-f(y+r)),
psi_(t+2)=2 psi_(t+1)-psi_t-A_F0 psi_(t+1).
```

This imports the registered selected transfer rule at its exact normalization;
it does not derive that rule from the kernel. Each finite cut has finite
support because every update uses a finite displacement set. Sparse states
are sorted tuples of `(D3 point,rational coefficient)` with zero coefficients
omitted. There is no wrapping, clipping or finite-box boundary substitution.
The bounded object is a requested finite prefix and its finite support, not a
replacement compact D3 carrier. The wave counter is elapsed `t`, not absolute
`n0+t`. No phase, polarization, propagator residue or physical photon is
established by this source injection and recurrence.

## 6. Stages, ownership and history

The three stages are a feed-forward graph:

```text
kappa_s -> D_matter -> D_geom -> D_clock -> CandidateHistory,
     |          |           |
     +----------+-----------+   explicit orbit/counter reads only.
```

`D_matter` produces the anchored QDD record, source coefficients, and indexed
linear/binary readings. `D_geom` consumes that source record and supplies the
tagged static geometry plus indexed wave states. `D_clock` combines the
accumulated records with the checked U checkpoint and the mathematical batch
at each cut. All indexed evaluations consume only the source and cuts no later
than the requested one as selection inputs. The next checkpoint is computed
from the current one solely to validate the transition; the frame still
records the current cut before the cursor advances. A later observed history
is never a selection input.

The following ownership plan is part of the candidate definition. Nested
record references do not reassign their fields to the enclosing stage.

| Record or field family | Sole stage owner | Reading leg or auxiliary basis |
|---|---|---|
| Exact five `MatterData_QDD` fields | `D_matter` | `D_quadratic`; existing anchored schema |
| Initial balanced piston and source-adapter metadata | `D_matter` | `AUXILIARY`, `CH-PB-HEAD-QDD-ADAPTER` |
| Checkpoint `trace4_t` | `D_matter` | `D_linear`; CODEC-TR4 observable |
| `theta_t` | `D_matter` | `D_binary`; exact counter cut |
| Tagged edge/face/current values and wave states | `D_geom` | Candidate `D_linear` assignments: these injections are linear in v; no CODEC uniqueness is inherited |
| Geometry source copy and carrier tags | `D_geom` | `AUXILIARY`, the three explicit geometry-injection choices |
| Batch coefficients, cell counts, total, finite ratios and complete pair relation | `D_clock` | Candidate `D_quadratic` batch readout, separate from the five QDD fields |
| Source header, checkpoint provenance, relative/absolute counters, context and event tags | `D_clock` | `AUXILIARY`, `CH-PB-HISTORY`, `CH-PB-A-CLOCK` and `CH-PB-ZERO` |
| Clock turns `tick_cycles=(n0+t)/5` | `D_clock` | `AUXILIARY`, `CH-PB-TIME-ORIGIN`; exact reporting unit and origin |
| Immutable references to matter and geometry records | `D_clock` | `AUXILIARY` record assembly; referenced fields retain their owners |

Here `D_linear` on geometry is an explicit candidate assignment,
not an assertion that those maps factor through the single trace character.
The geometry source consumes all four balanced coefficients. No factorization
of the binary leg, geometry or full history through Q is claimed.

For specification, stage domains are the canonical generated record
presentations for the same source and candidate version. A source mismatch is
invalid input, not a second interpretation of a record. The executable
finite-prefix interface constructs those presentations itself, so it does
not need to decide arbitrary equality of user-supplied infinite functions.
More precisely, the geometry domain is the graph of pairs `(k,m)` with
`m=D_matter(k)`, and the clock domain is the graph of triples `(k,m,g)` with
`m=D_matter(k)` and `g=D_geom(k,m)`. Totality on these named graphs does not
assert totality on arbitrary products of independently supplied records.
Every completed record is terminal for that cut while the forward stream may
continue. Functional terminality here is neither physical saturation nor
idempotence of the whole append-only history.

The reporting unit is turns: `tick_cycles=n/5`. The symbolic angular expression
is `2*pi*tick_cycles`, without a floating-point pi or an SI clock calibration.
Keeping the absolute counter in the timestamp and the relative cut in the
recurrences prevents a shifted head from silently receiving a different
initial wave or plenum preparation.

## 7. Dependencies and implementation boundary

Mathematical definitions are imported only at their registered scope:

| Candidate component | Public inputs and limits |
|---|---|
| Kernel source and evaluation | `DEF-CHECKPOINT`, `DEF-ODOMETER-ORBIT`, `DEF-AUTONOMOUS-STATE`, `DEF-ARCHITECTURE`; no derivation of the architecture from J |
| Trace and binary readings | `CODEC-TR4`, `READING-SPLIT`, `RAMIFIED-TM-LIFT`, `TIME-CUT-READING`; no inference of a physical frequency or coin selector |
| Anchored quadratic record | `ALGEBRAIC-DMATTER`, its exact `DEF-QDD-*` source definitions and `QDD-ALGEBRAIC-FACTORIZATION`; five fields only |
| Reduced fibres and pair counts | `J-RESIDUAL-UNIT-NORMAL-FORM`, `J-COINCIDENCE-CARTESIAN-GRAM-SEAM`; fresh units and explicitly chosen complete incidence |
| Full-cell algebraic copy boundary | `J-SIMPLEX-TIGHT-FRAME-DILATION`; no copying through the compressed simplex quotient |
| Integral A profile | `J-PLENUM-POLAR-ORBIT-SEPARATION` and the A/U5 routing boundary of PR #811; B remains separate and unused |
| Finite Maxwell identities | `MAXWELL-BIANCHI`, `MAXWELL-AMPERE-CHAIN`, `MAXWELL-OBSTRUCTION-P`; the source injections are new choices |
| D3 recurrence | `PHOTON-SPATIAL-TEMPORAL-TRANSFER`, `PHOTON-TEMPORAL-CHARACTERISTIC`; the initial wave and kernel coupling are choices |
| Clock reporting | `TIME-CUT-READING`, `METRO-TICK` at their dimensionless scope; no SI or dynamical derivation |
| Submission audit | `DEF-DECODER-COMPLETION-CONTRACT`; schema requirements are not scientific evidence |

The direct QDD implementation must not define itself by calling its comparison
factor map. A separate comparison may check fieldwise agreement, including the
zero branch. The five-field record keeps its existing coefficient-ring,
Gram/dagger/transpose, QCarrier, projector and pairing distinctions. Physical
`effect_ids` and `born_pairing_id` are not algebraic manifest keys.

The module direction is intended to be

```text
kernel.py      exact autonomous state, head readings and QDD arithmetic;
geometry.py    finite chain maps and sparse rational wave recurrence;
apparatus.py   centred A evolution, immutable batch and controller rules;
decoder.py     source checks, ordered stage composition and prefix assembly;
verify.py      independent conformance checks under its own frozen preregistration.
```

The acceptance tests must reject hidden inputs and feedback. The scientific
functions use only their explicit source, cut and fixed definitions: no random
seed, environment-selected parameter, clock time, network, data file, target
frequency or mutable registry read changes the chosen evolution. U is checked
independently of the apparatus component before its next checkpoint is used.

## 8. Constructive proof obligations before a result

The following are proposed proof and conformance obligations. No result for
the intended probe is asserted here.

1. **Total kernel evaluation.** Prove by induction that U remains on Omega
   and advances the counter by one. Every finite evaluator performs finitely
   many exact generator operations. Finite tests audit the formulas; they do
   not replace the induction over unbounded counter values.
2. **Domain and anchored restriction.** Establish the pointed head/sequence
   bijection, the explicit `K_QDD` inclusion, and equality of the quadratic
   restriction with `D_QDD_direct` for every admitted head at `n0=0`.
3. **Independent quadratic agreement.** Compare the field-arithmetic direct
   write with the Gram/projector expression, using exact rationals and the
   common zero rule. Do not infer its physical meaning from that identity.
4. **Centering and integral evolution.** Verify the centering identity,
   its actual image, `A(V_Z) subset V_Z`, and the quadratic scaling identity;
   induction then supplies the every-cut statement.
5. **Batch semantics.** Prove the fresh-fibre normal form, disjoint role tags,
   complete-product cardinality, and passive index bijection. Show that
   positive and zero preparations both produce exactly one atomic event per
   cut, with no duplicate interaction caused by passive enumeration.
6. **Controller coherence.** Check prepare/step/persist/reset and append
   typing, consecutive cursors, immutable prior records and explicit zero
   disposition. The next checkpoint must match the separately computed U
   step; the apparatus has no alternative write target in Omega.
7. **Geometry.** Check the two separate oriented complexes, source-injection
   coordinates, exact coboundary/boundary identities, zero torus winding and
   tagged carrier separation. Conservation of the chosen boundary current is
   mathematical and does not certify a physical source law.
8. **Photon prefix.** Prove that the full finite shell operator maps finite
   support to finite support and retains rational coefficients. Induct on
   elapsed cut for the selected recurrence and check its initial two slices.
9. **Composition.** Prove prefix totality and compatibility by induction on
   the cut. Check disjoint field ownership, the finite dependency DAG, exact
   source/presentation equality, timestamp convention and absence of output
   feedback. Byte-identical replay is separate from these mathematical proofs.

Negative controls should target meaningful alternatives: tail-identifying two
different heads; replacing the anchored preparation by a later checkpoint;
using raw J or nonintegral U5 as a count input; counting unreduced arrivals;
using only diagonal matching; serializing a batch as new interactions;
silently wrapping the D3 wave; conflating the two Maxwell carriers; changing
the time origin; or passing an apparatus-selected next checkpoint. Their exact
preregistered scope and expected behavior belong to the future probe.

## 9. Completion-manifest accounting and physical requirements

A complete mathematical model means that all maps of the chosen source and
output family are specified and the intended all-prefix proofs can be stated.
It does not mean that all normative completion requirements have values or
evidence. In particular, writing a finite manifest or resolving a local
identifier does not discharge a public gate.

The submitted candidate must retain the Canon's carrier, field, stage, leg,
bridge, quadratic, apparatus, physics, measure, closure and obligation
manifest sections. Candidate-defined identifiers resolve to these explicit
definitions; they are not represented as registered claims. Public pins and
evidence must point to their actual later immutable objects. The old QDD
skeletons are historical scoped artifacts, not whole-decoder templates that
may be promoted by changing their labels.

`PROFILE.json` records the concrete fields and exact Python schema names.
`record_field_manifest` inventories every stored field of all 18 declared
schemas: the primary History/Frame surface, tagged QDD payloads, passive
Pair/Fiber views and internal Support/Controller objects. The last two groups
are auxiliary representations with explicit bases. Pure batch properties are
marked separately. `record_schema_manifest` gives the exact class and field
names and each schema's output scope. Counts, ratios and
pair banks are exact properties of the emitted compact batch; JSON need not
materialize its entire Cartesian relation. `mathematical_apparatus_manifest`
names the executable helper maps while the physical `apparatus_manifest`
keeps its required identifiers unresolved.

The new head-to-tesseract, head-to-torus and head-to-D3-preparation maps have
explicit mathematical definitions but no registered L1-to-L2 gate. Their
gate requirements remain `UNRESOLVED`. The existing
`GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC` covers only the already selected
D3 transfer dictionary, restricted here to exact finite-support two-slice
data. It does not certify these new source injections.

The mathematical closure entry is `feeds_U=FALSE`, with writes limited to
immutable output records and the declared apparatus scratch/controller state.
Its proof obligation is the typed dependency and write-target audit, not the
presence of a terminal Boolean. An `AUXILIARY` leg assignment may use
`NOT_APPLICABLE` only with its explicit auxiliary basis. Physical debt must
not be hidden behind that mechanism.

| Normative requirement | State for this candidate |
|---|---|
| QDD algebraic projector targets | The registered LOW/HIGH algebraic identifiers remain available; they are not physical effects. |
| Physical effects, instruments, carrier, context, ready phase, coupling, pointer and reduction | `UNRESOLVED`; the mathematical controller and prepared pair bank are not realization certificates. |
| Physical target comparison, target independence and complete apparatus-family equality/classification | `UNRESOLVED`; defining this one family does not classify outside architectures or prove physical admissibility. |
| Realized outcome/event semantics and occurrence law | `UNRESOLVED`; one synthetic batch per cut is a model rule, not a measured or derived occurrence law. |
| Physical post-state, persistence, update/reset and ZERO_SUPPORT semantics | `UNRESOLVED`; the explicit mathematical versions are candidate implementations only. |
| `QDD-TERMINAL-EVENT-SEMANTICS` | Unchanged; terminal emission is not physical saturation of the complete post-state record. |
| `QDD-INSTRUMENT-CLASS-COMPLETENESS` | Unchanged; finite/unbounded memory and nonlinear, mixed, irrational or differently typed physical architectures are not excluded. |
| Required L1-to-L4/L5 apparatus bridges | `UNRESOLVED`; no newly registered bridge is created by calling a data structure an apparatus. |
| Physical source/current/conservation/propagator/detector chain | `UNRESOLVED`; the named finite injections and chain identities do not establish the physical chain or a constitutive law. |
| L6 measure, Born frequency, normalization, metrology and scheme | `UNRESOLVED`; no L6 reading is asserted or simulated by a random source. |
| Photon phase, polarization and physical readout | Unchanged; selected recurrence and finite-support propagation do not close these obligations or authorize F3 production. |
| Canonical curvature and global decoder-family completeness | Unchanged; this is a chosen mathematical reading family, not a proof of universal physical selection. |
| Bell causal accounting | Unchanged; no physical Bell, locality, signalling or hidden-variable conclusion is made. |

The existing `GATE-L1-L5-LOG-PROJECTION` is not automatically a gate for an
arbitrary richer batch, wave or physical history. The chosen mathematical
history has explicit types, while any requested public L5 or L6 interpretation
must be reviewed at that gate's actual scope or assigned its own named gate.
Similarly, `MEASURE-BORN-VERB` is not a blanket conversion of this five-cell
finite ratio into an observed frequency.

The relevant public owners remain [#107](https://github.com/mathorn1973/twist-j/issues/107)
for the QDD lineage and [#539](https://github.com/mathorn1973/twist-j/issues/539)
for the typed apparatus definition. The retired composite QDD scope and the
unused old `P-DMATTER-TOTAL-1` identifier are not resumed. A later fold, if
justified by separately reviewed evidence, must name the exact new scope it
adopts and preserve all remaining obligations.

## 10. Branch-collision boundary

The read-only branch audit found

```text
origin/claude/decoder-physical-reading-00xa91
  6c2e632b45c73e02702133e79d67359347642e06
origin/claude/coin-minimal-read-type-1c194b
  58eb0655a23648f06d799413072748a948c08c13
```

The first branch's outstanding additions are notes associated with issues
#687, #689 and #690. The second carries the older kappa-definition lane and
scratch witnesses associated with #200. Neither supplies an implemented
whole `D_geom`/`D_clock` candidate that this document may treat as authority.
Their owned scientific scopes and stale constructions are not imported here.
This audit of those two refs does not replace the fresh public issue and pin
collision check required before the intended formal probe.
