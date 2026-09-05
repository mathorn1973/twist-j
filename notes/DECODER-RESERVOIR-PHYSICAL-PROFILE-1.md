# Decoder reservoir physical profile 1

**NON-CANONICAL / PROPOSED PROFILE / STOP-DEFINITION / PHYSICAL REALIZATION UNRESOLVED**

This document selects one exact mathematical interface and proposes physical
roles for it. Selection of the interface is a design choice, not adoption of
its physical interpretation. The accompanying
[JSON inventory](DECODER-RESERVOIR-PHYSICAL-PROFILE-1.json) resolves local
mathematical identifiers and separately lists unresolved physical identifiers.
It is not a conforming completed #539 manifest, a new probe, a formal result,
or a whole-decoder completion certificate.

```text
profile_id: RRP1-PROFILE
basis_main: 4e794a01aec719a4536f2028ecbfd2f876a19e2b
authority: ACTIVE Public Canon v76
canon_content: 07910adb8418742bf52a0d204577b84b38009b18
canon_sha256: c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112
canon_bytes: 420539
mathematical_layer: L1
proposed_physical_roles: source / L4 support-apparatus / L5 record
physical_lifts: UNRESOLVED
formal_execution_for_this_profile: NONE
feeds_U: FALSE
```

## 1. Source and context: one declared family

The source is a **pointed** forward U orbit, represented by its full head
`h=(n0,x0) in N_0 x F_5^6`. Its later checkpoints are exactly `U^t(h)`.
Use the autonomous update specified by the active Canon; no port, threshold,
record or context changes it. Literal head equality decides source equality,
because U is deterministic. No quotient of unpointed trajectories is used.

The new source adapter `RRP1-MAP-SIGNED-HEAD` reads

```text
beta(0,1,2,3,4)=(0,1,2,-2,-1),
z=(beta(x0_0),beta(x0_1),beta(x0_2),beta(x0_3)).
```

The signed vector is an auxiliary head read, not reconstructed from the
five-field QDD record identifying z and -z. The last two checkpoint
coordinates and n0 remain in provenance; they do not enter z. The profile
does not reset n0 to zero. The orbit-to-head read on nonzero-counter sources
is an explicit adapter choice.

A mathematical context is

```text
c=(Gamma,q,N),
Gamma : D3 -> Q_(>=0), finite support R,
Gamma(x)>0 on R, zero entries omitted, duplicate sites rejected,
q in Q_(>0), N in N_0.
```

D3 is the marked infinite lattice `{x in Z^3:sum x_i is even}`.
Gamma sites are in lexicographic order. Empty R and N=0 are admitted.
The source injection, pair order, cold-slot convention, record equality and
clock convention below are fixed by this profile ID. They are not selectable
per event. For each preselected c, the mathematical reading is `D^c_N` on
all pointed source orbits. Its mathematical context map is constant c.

The physically admissible source subset `K_c`, physical ContextEq and
physical selection `C:K -> ContextKey` are **UNRESOLVED**. Gamma, q and N
are family indices fixed before source comparison, not hidden inputs to U
or freely fitted universal constants. Identification of c with the actual
apparatus needs an independent physical law/dictionary or source-to-context
rule. Contexts for different physical settings may differ. Competing readings
of the same physical context require an independent selection/occurrence
rule or physical equivalence; global singleton uniqueness is not required.

For this proposal the explicit mathematical supported-source predicate is
`z!=0`. The zero-amplitude branch has its own disposition below. This
partition is not inferred from a later ratio, and it is not a physical
particle-presence predicate. A nonzero supported source need not produce
any threshold crossing.

## 2. Preparation and clock adapter

Let `Wave=C_c(D3,Q)`, with sorted distinct rational nonzero entries, and
`Pair=(previous,current)`. Put

```text
s=sum_i z_i,
y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)),
coeff=(z0-s/5,z1-s/5,z2-s/5,z3-s/5,-s/5),
S(z)=sum_j coeff_j delta_(y_j),
P0=(0,S(z)).
```

This is the #823 source, not #821's four-site two-slice seed. Its known
isometry `||S(z)||^2=m(z)=sum z_i^2-s^2/5` is disclosed as target-exposed
source design. No physical independence follows from the norm match.

Preparation completes the one source kick before the cold coupling acts.
At that point the ledger is zero and the signed tape empty. ReadyState is
the singleton `COLD_FRESH_EMPTY`: zero incoming slots, no prior interaction,
no ready phase chosen from desired counts. The physical meaning, availability
and preparation of those slots remain unresolved.

Select **one coupled transition per subsequent U update** as a labeling
convention:

```text
prepared pair P0: preparation label n0;
batch t: P_t -> P_(t+1),             0 <= t < N;
start checkpoint: U^t(h),            start counter n0+t;
completed checkpoint: U^(t+1)(h),    availability counter n0+t+1.
```

Thus first batch t=0 becomes available at n0+1. No event exists merely
because its start label is available. This supplies an explicit mathematical
clock adapter, not a derived physical clock, a wave/U intertwining theorem,
a frequency, or an SI scale. For t>0, z is not re-read and the source is not
re-kicked. Later U checkpoints provide provenance only.

A fixed c has a maximum exposure N; every prefix of length k<=N is defined
with the same c. Changing only N preserves generated wave/tape/crossing
values on common prefixes after the explicitly declared relabeling of
exposure metadata. Whole records with different c remain unequal. A longer
exposure is not a reset or another source preparation.

## 3. Selected coupling and ledger

The fixed wave operator is the five-shell operator of #823:

```text
(Lv)(x)=sum_d c_d[v(x)-v(x+d)],
squared shell lengths=(2,4,8,10,16),
weights=(6,1,15,1,1), c_d=weight/324, sum_d c_d=8/9,
E(u,v)=||v-u||^2/2+<u,Lv>/2.
```

The operational profile uses the cold specialization of #825:

```text
w_x=[2v_x-(Lv)_x-(1-Gamma_x/2)u_x]/(1+Gamma_x/2),
b_x=-(w_x-u_x)/2                     for x in R,
d_x=Gamma_x b_x^2,
P'=(v,w), heat'=heat+d, tape'=tape concatenated with b.
```

Outside R the wave step is free. The denominator is positive. Each finite
step has finite support. A fresh incoming zero slot is consumed at every
active port on every step; outgoing slots are retained and never recycled.
At most `N*|R|` slots are used in one declared exposure. The family permits
arbitrarily large finite exposures; no uniform finite physical capacity is
thereby certified.

For a generated prefix, the three expressions

```text
sum_(s<t,x) Gamma_x b_(s,x)^2,
sum_x heat_(t,x),
sum_x [q Count_(t,x)+remainder_(t,x)]
```

account for the **same** energy, where
`Count_x=floor(heat_x/q)` and `remainder_x=heat_x-q Count_x`.
They are not independent stores. The exact inherited budget is
`E(P_t)+sum heat_t=E(P0)=m(z)/2`.

For each site, step t emits the inclusive interval
`Count_before(x)+1,...,Count_after(x)`, if nonempty. Every interval at every
site belongs to the same atomic batch. The outcome is
`THRESHOLD_CROSSINGS` with all these intervals, or `NO_CROSSINGS`.
Zero or multiple threshold crossings per batch are ordinary output; no
selection of one crossing is performed. Exactly one accounting EventRecord
is created per transition. Site/ordinal is a lifetime address within one history;
tick is transition provenance. The proposed physical role is a calorimetric
threshold record, not an exclusive LOW/HIGH outcome or photon count.

## 4. Complete narrowed mathematical interface

The following record carriers are newly specified wrapper types, not new
Python classes already present in a completed probe.

- SourceRecord: full head h and its signed z.
- ApparatusState: SourceRecord, c, t, signed tape of length t, and heat
  equal to its exact weighted-square summary; `0<=t<=N`.
- SupportCarrier: the wave pair.
- RecordDelta: source/context, tick, pair before/after, full immutable
  apparatus_before/apparatus_after snapshots including their complete signed
  tapes, signed outgoing b,
  deposit d, heat before/after, counts before/after, remainder after,
  crossing intervals, outcome tag and start/completion checkpoints.
- EventRecord: that complete RecordDelta with the mathematical
  `transition_complete=TRUE` tag.
- HistoryState: source/context, P0, current pair, current ApparatusState and
  the immutable ordered EventRecords.

Every role has its own named literal equality in the JSON. Exact rationals
are reduced numerator/positive-denominator pairs; integers and booleans have
different types; sparse fields omit zeros; count vectors include every
active channel including zero counts. The record includes signed b and both
wave states. Equality of heat, counts, QDD weights or sign-quotient data is
not equality of these complete records. The physical equalities remain
unresolved.

The maps are fixed as follows.

| Local map | Exact domain and result |
|---|---|
| `SOURCE` | Pointed orbit head -> SourceRecord by the signed adapter. |
| `CONTEXT_c` | SourceRecord -> the already fixed c. No output-based selection. |
| `SUPPORT` | SourceRecord -> SUPPORTED(source) if z!=0, otherwise UNSUPPORTED_ZERO(source). |
| `READY` | SupportedSource x c -> COLD_FRESH_EMPTY. |
| `PREPARE` | SupportedSource x c x the ready singleton -> (P0, source/c/t=0/empty tape/zero heat). |
| `STEP` | Pair x coherent ApparatusState x matching c with t<N -> (outcome, next pair, next apparatus, RecordDelta), using the cold formulas and clock adapter. |
| `EMIT` | The compatible output tuple of STEP -> complete EventRecord. Exact domain is STEP's image; no field is dropped. |
| `PERSIST` | Old apparatus x outcome x a matching EventRecord -> record.apparatus_after. Exact domain requires literal equality of the old apparatus with record.apparatus_before, matching outcome and the coherent STEP extension; it agrees with STEP. |
| `APPEND` | History x EventRecord compatible with its last pair/state/source/context and next tick -> extended History. Domain compatibility is explicit, not assumed for arbitrary concatenations. |
| `TERMINAL_M` | EventRecord -> 1. This means the complete transition has been computed, not physical event saturation. |
| `ZERO_SUPPORT` | Zero-amplitude SourceRecord x c -> NO_EVENT_ZERO_SOURCE carrying its unique zero-wave, zero-ledger N-step History, initialized directly as specified below. |
| `RESET_REQUEST` | ApparatusState x matching c -> REJECTED_RESET_DISABLED containing the unchanged apparatus. |
| `READ_N` | Every SourceRecord x fixed c -> its unique N-step History, using zero disposition where needed. |
| `REREAD` | Existing EventRecord -> that same record, with no STEP, tape append or counter increment. |

Each is total on its stated mathematical domain, by its explicit formula or
finite induction. A malformed or incompatible input is outside the domain;
this note does not claim a total application on the unrestricted Cartesian
product. N=0 gives no events and the prepared pair unchanged. Nonempty
support with no crossings, positive subthreshold heat, and a dark mode
remain distinct from the zero-source disposition.

For z=0, ZERO_SUPPORT directly initializes `P0=(0,0)` and the coherent
`(source,c,0,empty tape,zero heat)` apparatus. It does not call PREPARE,
whose domain is SupportedSource. ApparatusState admits zero-source records,
so STEP and EMIT then construct exactly N mathematical EventRecords, each
with outcome NO_CROSSINGS, zero pair, deposit and ledger, and the ordinary
successive checkpoint labels. READ_N returns this same History; ZERO_SUPPORT
additionally wraps it in NO_EVENT_ZERO_SOURCE. That tag denotes absence of
threshold crossings on the zero branch, not absence of computed transition
records, and does not adopt physical #539 NO_EVENT semantics.

The selected wrapper STEP records are stronger than the compact old Batch:
they add source/clock and complete before/after apparatus provenance. STEP
owns these snapshots, including all prior signed tape values. EMIT therefore
preserves the entire STEP output tuple: its outcome, next pair and next
apparatus are present in RecordDelta. Immutable prefixes may share storage,
but equality compares their complete values. ApparatusState contains no
EventRecord, so the nested snapshots introduce no reference cycle. Snapshot
copies are descriptions of the same energy store, not additional stores.
The STEP domain includes coherent tape/heat states, not only histories
reachable from this profile's preparation; full snapshots preserve that
distinction. READ_N and HistoryState retain the separate generated-history
restriction. Their proposed wrapper
has no execution evidence. The inherited coupling law and the new wrapper
interface must not be conflated.

**Reset boundary:** RESET_REQUEST is deliberately not #539's
`reset:ApparatusState x ContextKey -> ReadyState x ApparatusState`.
It returns a different tagged codomain. Fresh preparation starts a separate
history and does not erase an occupied tape. This mismatch keeps the #539
adapter STOP-DEFINITION until a compatible typed reset/domain ruling or a
separately reviewed schema change is supplied. No implicit reset from #821
is imported.

Field ownership is single-valued: SOURCE owns h,z; CONTEXT owns c; the clock
adapter owns the U/checkpoint labels; STEP owns wave/port/deposit and ledger
updates plus full apparatus_before/apparatus_after snapshots; the threshold
projection within STEP owns intervals/outcome;
EMIT only packages those owned fields and adds its completion tag; APPEND
owns history extension. Records, counts, q and N never feed the wave law;
Gamma and old pair do. No profile output feeds U.

The JSON closure targets name the constructed successor Pair, ApparatusState
(including tape and heat), RecordDelta, EventRecord and HistoryState. These
are functional constructions of new immutable values, not in-place writes.
They neither mutate Omega/U nor modify the autonomous kernel or selector.
An empty list of output writes is therefore not used to express no feedback.

## 5. Proposed physical roles and open identifiers

A proposed role is a question to be validated, not a resolved physical ID.
The JSON contains every apparatus-manifest slot from the active Canon.

| Proposed role | Selected mathematical value | Physical owner/selection still required |
|---|---|---|
| Preparation/source | Signed head -> S(z) -> P0 | Physical K_c, source-to-apparatus relation, meaning of marked sites and source kick. |
| Context and read cut | Gamma,q,N and one transition/U-label convention | Independent C or physical context identification, phase/clock/space and SI dictionary. |
| Support/apparatus | Scalar D3 pair, finite port array, unused zero slots and tape | Physical carrier, preparation and resource/capacity certificates; no photon/polarization identification. |
| Constitutive interaction | The selected rational port law | Physical input/output variables and calibration; independent response test below. |
| Pointer and record | Signed port response, deposited energy, complete threshold batch | Physical signal/pointer, resolution, full record equality and post-state instruments. |
| Persistence and completion | Immutable tape; complete mathematical transition; rejected reset | Physical memory law, reset/domain ruling, event completion and any independently justified saturation law. |
| Family and occurrence | Contextual mathematical family; all threshold intervals | Whole physical-family equality/membership/completeness and ordered realized-event law. |

The targets `DEF-QDD-PROJECTOR-LOW/HIGH` remain algebraic comparison
targets only. No Gamma, ready state, source convention, pointer, phase,
channel partition or threshold is selected from those projectors or from
desired Born rates. This profile proposes calorimetric records and makes
no equality claim with QDD LOW/HIGH or the A/U5 incidence population.

The narrowed context family is not the complete admissible physical family.
Whole-family equality must account for ready phases, memory, transitions
and future response; finite/unbounded memory, nonlinear, mixed, irrational
and differently typed alternatives are not excluded by selecting this model.
Multiple physically distinguishable contexts are permitted. No new global
uniqueness obligation is introduced.

## 6. Parameter provenance and a prospective discriminant

| Datum | Provenance and selected meaning | Physical status |
|---|---|---|
| U, head carrier, balanced convention | Active Canon and #821 implementation; head-to-profile composition newly specified here. | Physical source adapter UNRESOLVED. |
| Five marked source sites and centering | #823 disclosed QDD-norm-exposed choice. | Physical placement/coupling UNRESOLVED. |
| L, its 1/324 scale and E convention | #823/#825 immutable mathematical dependencies. | Physical energy/current/propagator identification UNRESOLVED. |
| Gamma | Fixed rational conductance context; not inferred from outputs. | Constitutive value/units and calibration UNRESOLVED. |
| q | Fixed positive rational energy threshold; independent of source/counts. | Pointer threshold/calibration UNRESOLVED. |
| N and one step per U update | Preselected exposure and new clock-label choice. | Physical cut, time and space mapping UNRESOLVED. |
| Zero incoming slots and finite tape budget | Selected cold preparation; N times the number of active sites. | Background, phase, reset and capacity realization UNRESOLVED. |

No new universal dimensionless parameter is declared derived. Apparatus
settings may index a physical context, but their assignment still needs
independent ownership. SI conversions must respect the active calibration
scope; attaching units or fitting extra constants does not satisfy it.

A concrete **prospective** discriminator uses the old general port law,

```text
p=(w-u)/2, f=g(2a-p), b=a-p.
```

For a diagnostic zero pair and one incoming pulse a=A at port x,
`A!=0, Gamma(x)=g>0`, it predicts exactly

```text
w_x=4g A/(2+g), b_x=(2-g)A/(2+g),
E_new=8g^2 A^2/(2+g)^2,
r=b_x/A in (-1,1), g=2(1-r)/(1+r).
```

This is a proposed signed constitutive response law, conditional on a
physical identification of a,b and their common calibration. General warm
diagnostics are a separately declared calibration domain, not an extra
runtime input to the cold D^c profile or to U. Their transfer is signed
`Gamma(b^2-a^2)`, not the cold deposit `Gamma*b^2`.

An independent prepared-source validation can use signed z=(1,0,0,0), which
is in the balanced head domain. At the origin, let
`h=(HSz)_0=1421/1620`, with H=2I-L. The first cold response would be

```text
w_0=2h/(2+g), b_0=-h/(2+g), D_0=g h^2/(2+g)^2.
```

The signed response identifies `g=-h/b_0-2` if its observable and scales
are independently owned. Energy alone does not: `D_0/h^2` is unchanged
by `g -> 4/g` and has maximum 1/8 at g=2. The ambiguity must be resolved
by a predeclared signed-response or incoming-control observation, never by
choosing the branch giving desired Born weights.

Calibration and validation data must be distinct: identify g and the
observable scales using one predeclared diagnostic; predict a different
predeclared source/pulse/context response without refitting g. Separately
validate the pointer threshold before evaluating occurrence statistics.
All conditions, uncertainties and failure thresholds of an actual physical
test would need their own preregistration and source manifest. No pulse
measurement, formal experiment, calibration or physical PASS exists here.
If signed observables are not owned, the identifiability claim remains
only algebraic and the physical task remains STOP.

## 7. Evidence, decisions and next boundary

Local source handles in the JSON resolve these fixed public inputs:
[pointed result](../probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/RESULT.md),
[wave result](../probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/RESULT.md),
[reservoir result](../probes/P-DECODER-RESERVOIR-COUPLING-1/RESULT.md).
The source pins are respectively
`69c9dc34f57d5f9943681761eb6386a17d4bfc47`,
`30ab237b4dcb339115517f67b883ca4cc3e00c32` and
`550420d188a45c4929e300ca6aabcde812f4d65a`.
These results remain unregistered; none proves the new wrapper or physical
profile. The induced quadratic partition is a separately coordinated
mathematical task, not this profile's evidence.

The relevant requirements are the
[Canon decoder completion contract](https://github.com/mathorn1973/twist-j/blob/4e794a01aec719a4536f2028ecbfd2f876a19e2b/canon/CANON.md#L648-L840),
the apparatus manifest at Canon lines 744-770 and its physical boundary at
1832-1907, and the
[#539 typed proposal](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
(carriers/equalities 100-138, maps 163-190, ownership 234-282).
The JSON maps to these roles but does not claim their full schema or layer
conformance. New wrapper records would require their own stage/leg/field
inventory when integrated into a whole decoder; existing PROFILE.json is
not edited or silently widened.

The current disposition is STOP-DEFINITION. A future test of one proposed
constitutive law needs its own frozen source/context, observable ownership,
calibration and test contract. Such a test need not enumerate the whole
physical family. A decoder-completion submission additionally needs the
reset typing decision, complete scoped physical family/equalities and named
layer-gate contracts. Positive closure evidence must concern that same
frozen profile. Failure of an exact mathematical identity would
concern the new mathematical claim at its own scope; one failed candidate
does not prove physical apparatus impossibility. A fully independently
admissible witness can refute a claimed class completeness or terminality
statement only under that owner's exact frozen conditions. No negative
owner closure is attempted here.

QDD apparatus, terminal-event and class-completeness obligations remain open.
The proposed mathematical transition-complete flag does not imply COMM-SAT.
COINCIDENCE-RECORD-FREQUENCY remains candidate-H / UNTESTED / STOP,
unregistered: its simultaneous complete incidence population is not a
temporal reservoir-click sample. Bell accounting and L6 measure/self-location
remain separate. The #744 photon identification chain and #756 F3
NOT_SATISFIED remain unchanged; production #742 is FORBIDDEN.
