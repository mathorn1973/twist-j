# P-DECODER-POINTED-BATCH-CONFORMANCE-1 preregistration

Status: **FROZEN TARGET / PUBLIC STATUS NONE / NO FORMAL RUN**.

Disclosure: **RESULT-EXPOSED / CHOICE-EXPLICIT / PROOF-FIRST / L1 ONLY**.

```text
owner:          A. M. Thorn
public issue:   https://github.com/mathorn1973/twist-j/issues/820
public base:    1a58703ec17a4c031bb8c450f56162f5aa3e5e5a
authority:      Public Canon v76
candidate:      DECODER-POINTED-BATCH-1
claim:          POINTED-DECODER-PREFIX-CONSISTENCY
branch:         probe/P-DECODER-POINTED-BATCH-CONFORMANCE-1
formal runs:    0
public status:  NONE
```

## 1. Equation, target and scope

Let Omega=N_0 x F_5^6 and let K_* consist of the pointed sequences
`kappa_h(t)=U^t(h)`, t in N_0, with their literal head h=(n0,x). U is the
registered autonomous map: theta(n) is binary digit-sum parity,
sigma(n,x)=(sum(x)+2 theta(n)) mod 5, and U(n,x)=(n+1,g_sigma(x)).
The five generators are exactly the registered affine involutions.

For the one chosen dictionary specified in this directory, define

```text
D_* = D_clock o D_geom o D_matter,
D_*^{<L}(h) = (candidate_id, h, (Frame_h(0),...,Frame_h(L-1))),
Frame_h(t) = (Matter_h(t), Geometry_h(t), Clock_h(t)).
```

Composition retains earlier records and the source as typed inputs; it does
not overwrite one carrier by another. D_matter first defines its source and
matter records. D_geom takes these compatible records and adds the geometry
records. D_clock takes both compatible stages and writes the clock/batch
stream. These are separate from the three field-owner legs D_linear,
D_binary and D_quadratic. PROFILE.json records every ownership assignment.

The **one claim** is the following conditional mathematical statement about
this fixed chosen dictionary, with every clause required:

1. Every pointed h and every finite L have a uniquely defined exact finite
   output. Prefixes agree: truncating D_*^{<L}(h) at M gives D_*^{<M}(h)
   for 0<=M<=L. They define one infinite stream by compatible finite prefixes.
2. Checkpoints are exactly U^t(h). The original five-field QDD direct write
   agrees with ALGEBRAIC-DMATTER on K_QDD (n0=0). The nonzero-counter adapter
   is explicitly an additional choice, not an inherited extension theorem.
3. The selected nontrivial tesseract source has F=dA and dF=0. The distinct
   selected torus source has j=boundary(G), boundary(j)=0 and zero four
   windings. The chosen D3 two-slice state follows the registered homogeneous
   recurrence with the explicit initialization below, for all finite ages.
4. Each batch is precisely a complete finite within-cell Cartesian incidence
   population of fresh signed residual fibres. Its canonical addresses form
   a bijection with that population. Counts, zero semantics, atomic append,
   persistence, reset and passive readback obey the stated mathematical laws.
5. The readout pipeline has no dependency feeding U, no future-record input,
   and no identification of its five-cell counts with the QDD LOW/HIGH slots.
   All record and interface distinctions named below are retained.

This is a theorem about a chosen encoded model. It is **not** the global
physical decoder-completion claim, a uniqueness theorem for decoder choices,
a complete physical apparatus family, a measurement outcome-frequency law,
an empirical fit or the realization of a photon/source/detector. The existing
physical requirements remain explicitly unresolved in PROFILE.json. A PASS
must not be used to change their status.

## 2. Exact carriers, maps and choices

### 2.1 Pointed read convention and matter

Use representatives 0,1,2,3,4 for each pentit and the balanced lift
ell=(0,1,2,-2,-1). Write v=ell(x[:4]) and retain h as auxiliary provenance.
The registered K_QDD inclusion is h=(0,x). For n0>0 the chosen anchor map
`(n0,x)->kappa_(0,x)` applies the same head rule. No later checkpoint, q, r
or counter value enters the values of the anchored QDD write.

In K=Q[zeta]/(1+zeta+...+zeta^4), on the marked basis
B0=(1,zeta,zeta^2,zeta^3), put w=sum_(i=0..3) v_i zeta^i,
lambda=sum_(i=0..3) zeta^i,
and `<a,b>=(1/5)Tr_K/Q(a conjugate(b))`. Conjugation sends zeta to zeta^4.
For nonzero w, the direct rules are

```text
m=<w,w>, low=<w,lambda>/<lambda,lambda> * lambda, high=w-low,
branch_weights=(<low,low>,<high,high>),
T_w(b)=w <b,w>, density=T_w/m,
normalized_weights=branch_weights/m.
```

This is a direct field-level write, independent of the factor-interface
Gram/dagger/projector construction. Exactly five QDD fields are written:
support_state, total_weight, branch_weights, density_state,
normalized_weight_state. For w=0 their exact values are
`ZERO_SUPPORT,0,(0,0),ZERO_DENOMINATOR,ZERO_DENOMINATOR`.
For w!=0 the last two fields are explicitly tagged Density and Normalized.
The Python constructors Density/Normalized (also their JSON type names)
encode the Canon tags DENSITY/NORMALIZED by this declared bijection; no
literal wire-string equality between the two notations is asserted.
Neither is relabelled as a physical effect or probability.

At cut t the additional linear read is the registered F5 covector
`Tr4(x_t)=sum(x_t[:4]) mod5`, and the binary read is theta(n0+t).
This piston-sum covector is different from the field trace above. Both read
the actual checkpoint. The five QDD fields and v remain head anchored.

### 2.2 Geometry and wave choices

There are three distinct tagged carriers, with literal exact equality.

* The tesseract has vertices {0,1}^4 and oriented integer cochains. Select
  A(e1,0)=v0, A(e2,0)=v1, A(e3,0)=v2, A(e2,1)=v3, every other edge zero.
  Here (e_i,j) is the edge at vertex e_i in direction j and indices start
  at zero. Set F=dA with the registered oriented coboundary.
* The separate periodic 2^4 torus has integer chains. Select face coefficients
  G(0,01),G(0,02),G(0,03),G(0,12)=v0,v1,v2,v3, others zero; set j=boundary G.
  The torus current is not the tesseract field. No physical identification
  between the two carriers is made.
* On D3={y in Z^3:sum y even}, select the four sites
  y0=(0,0,0),y1=(1,1,0),y2=(1,0,1),y3=(0,1,1), and choose
  psi0=psi1=sum v_i delta_yi. Use elapsed age m=t, not the absolute n0+t.
  The registered operator at F0=1 is
  `A0 f(y)=(1/324) sum_(s,z in S_s) w_s (f(y)-f(y+z))`,
  with squared norms (2,4,8,10,16) and weights (6,1,15,1,1).
  Evolve `psi_(m+2)=2 psi_(m+1)-psi_m-A0 psi_(m+1)`.

All three injections and the equal two-slice initialization are choices.
The homogeneous transfer is not thereby a forced source propagator, a
retarded Green function, a detector coupling or an F3 physical realization.
No photon production route is opened by this probe.

### 2.3 Five-cell batch, apparatus and clock choices

On the marked integer five-cell augmentation carrier put

```text
d=5(v0,v1,v2,v3,0)-sum(v)*(1,1,1,1,1),
a_t=A^t d,  A=I+g^2-g^3-g^4,  g e_k=e_(k+1 mod5).
```

One A step per relative U tick is explicitly selected. There is no asserted
intertwiner A<->U, and raw J or B never acts on count supports.
For each cell k the S and R fibres both contain |a_t[k]| units. All units
have the sign of a_t[k], and carry independent S/R tags, ordinal 1..|a_t[k]|,
source h and cut t. Empty fibres have size zero and sign zero. The incidence
set is explicitly chosen to be

```text
C_t = disjoint_union_k (S_(t,k) x R_(t,k)).
```

Complete incidence does not follow merely from equal marginal fibre sizes.
The entire finite population is one atomic batch; unit write gain is chosen
to be one. Canonical finite ranges represent the entire set without storing
all its elements. Passive rank/unrank queries inspect already present records
and create no new interaction. New-cut units have fresh identities; none are
transported through A or U.

The output is BATCH_EVENT or ZERO_EVENT for the entire batch. It is never a
randomly selected cell or QDD LOW/HIGH event. Counts are a_t[k]^2. Ratios are
these counts divided by their sum, or ZERO_DENOMINATOR if the sum is zero;
they are finite population ratios only. The all-zero support produces an
empty, explicitly recorded ZERO_EVENT and advances the cut.

The context is the singleton marked model context, with EMPTY_READY and no
phase/seed choice. Controller state is (next_cut, cached_last_batch).
`step` writes current support, advances the actual U checkpoint supplied by
the decoder, computes fresh A support and caches the batch. `persist` gives
exactly that controller. `reset` clears only the cache and preserves next_cut;
it does not rewind the source or history. History is ordered append from cut
zero without gaps or duplicate cuts. A terminal flag means completion of
this atomic mathematical write, not a saturation or physical occurrence law.

Clock reporting uses absolute counter n0+t, relative cut t and exact cycle
coordinate (n0+t)/5. This is the METRO-TICK dictionary, not an SI calibration.
Frame records describe the cut before advancing to U^(t+1)(h).

### 2.4 Equality and complete domain

Admissible sources are all h in Omega, not a target-selected subset. The
three source injections are defined for every balanced v, including zero.
Intermediate domains are compatible graphs of the preceding stages, not
arbitrary forged or mismatched record tuples. Mathematical apparatus supports
are the reachable pairs (U^t h,A^t d) with their exact source/cut tags.

Every stored carrier uses literal tuple/integer/Fraction equality. Sparse
waves have sorted distinct sites and omit zero coefficients. Source history
equality retains the auxiliary source header: two generated infinite streams
in this presented carrier are equal iff their headers agree, because the
header is present and deterministic generation gives the converse. Equality
of physically interpreted histories after discarding provenance is not solved
by this convention. No tail quotient, cell relabelling, phase gauge or physical
equivalence quotient is implicit. Finite history equality is structural.

## 3. Uniform proof, independent of a finite sample

### 3.1 Well-defined original read and anchored extension

The marked cyclotomic representation gives
`<w,w>=sum v_i^2-(sum v_i)^2/5`. Cauchy-Schwarz on four coordinates gives
`(sum v_i)^2<=4 sum v_i^2`, hence m>=sum v_i^2/5>0 for v!=0. Also
`<lambda,lambda>=4/5`. Every nonzero-branch division is therefore by a
positive rational. The zero branch performs no division. Orthogonal line
projection gives low perpendicular high, so the two nonnegative branch
weights sum to m; T_w^2=m T_w and trace(T_w)=m. These are the exact direct
ALGEBRAIC-DMATTER rules on K_QDD. Their value dependencies use only v. Applying
the same rules to a nonzero-counter head is a separately declared total map;
this declaration does not prove it is a canonical physical extension.

### 3.2 Geometric identities and nontriviality

An oriented codimension-two face in d(dA) appears twice with opposite signs,
so dF=0 over Z for every tesseract edge cochain. In the chosen injection the
four origin faces 01,02,03,12 read (-v0,-v1,-v2,-v3). Thus F=0 iff v=0.
The same alternating-boundary cancellation gives boundary^2=0 on the torus.
Its winding cut covectors annihilate every face boundary: opposite parallel
edges in a face have the same cut coefficient and opposite signs. Hence the
selected j is conserved and has four zero windings. For the r-th chosen
origin face with axis pair (i_r,j_r), its distinct shifted edge (e_(i_r),j_r)
has coefficient v_r in this four-face span, so j=0 iff v=0.
These are finite complex identities, not physical
field equations inferred from a model fit.

Each D3 shell is finite, lies in D3, is centrally symmetric, and has maximal
coordinate displacement four. A finite-support rational wave has a finite
union of finitely many shifted supports. The denominator 324 is fixed and
nonzero, so recurrence produces a unique finite-support rational successor.
Induction from the two finite initial slices proves finite computability at
every age and the stated recurrence. This does not assert stability for
every physical wave number or positivity of an occurrence measure.

### 3.3 Batch laws

Centering gives sum d=0, d=0 iff v=0, and
`sum d_k^2=25 sum v_i^2-5(sum v_i)^2=25m`.
Every cyclic shift preserves the augmentation sum, so A preserves its zero
subspace. All a_t are exact integers; finite matrix multiplication gives a
unique a_t at every finite t. In particular a zero initial d remains zero.

At any cut the disjoint block for cell k has exactly |a_k|^2 elements.
Subtracting earlier block sizes locates a unique nonempty block for any
rank in [0,sum a_k^2). Euclidean division by |a_k| gives a unique ordered
pair of ordinals in that block. Conversely their row-major index lies in
the same block. This proves rank/unrank bijectivity for every integer support,
not only for the bounded test set. Distinct cut tags prohibit cross-cut
identity. Empty blocks and the empty whole population are handled explicitly.

`step` and `persist` use the same current event and successor cursor.
Clearing cache cannot alter source, support or the cursor, and the next output
depends on these values rather than the discarded cache. Passive readback
returns a value from an immutable completed record; it changes no state or
history. Ordered append is concatenation at the exact next cut. These facts
prove persistence/reset/readback laws on every compatible reachable support.
They describe the chosen atomic mathematical writer, not a demonstrated
physical instrument implementing it.

### 3.4 Totality, prefixes and autonomous U

Each generator is an affine map F5^6->F5^6. Binary digit sum terminates at
every finite n, so U is total and independent of any record. By induction
the checkpoint at cut t is exactly U^t h and has absolute counter n0+t.
The anchored matter and geometry seeds are uniquely determined before the
stream begins. Sections 3.1--3.3 give a unique finite next value for every
remaining state. Thus each finite cut is computable with finite, though not
uniformly bounded, resources. No claim about polynomial running time is made.

Induction on L constructs a unique output prefix. The step rule has no L or
future-output argument, so increasing the requested horizon cannot change
any earlier record. Compatible prefixes define a unique sequence. U's
transitive input dependencies contain only its current (n,x), fixed constants
and exact arithmetic, not matter, geometry, apparatus or history. This proves
no feedback; it does not prove a physical interpretation of the forward maps.

For v=(1,1,1,1), QDD normalized LOW/HIGH is (1,0), whereas d=(1,1,1,1,-4)
and the five-cell ratio is (1,1,1,1,16)/20. This exact negative control forbids
identifying two different codomains even when both are normalized.

## 4. Accepted code and finite audit gates

The accepted program is verify.py plus exactly these same-directory source
dependencies: kernel.py, geometry.py, apparatus.py, decoder.py,
audit_geometry.py and audit_apparatus.py. PROFILE.json is its only data input;
verify.py also reads kernel.py as source text for its direct-write dependency
and import-boundary audit, and reads all seven dependencies as bytes for the
frozen SHA-256 integrity table before running any scientific gate. All are
pinned together with this PREREG and the
explanatory NON-CANONICAL note. Complete blob IDs, SHA-256 values and byte
counts of every pinned file are recorded in the public readback and RUN.md.

Only Python standard-library integers, Fractions, finite tuples, sparse exact
waves, dataclasses, JSON and AST inspection are used. No external scientific
data, network, subprocess, random seed, numerical tolerance, time-dependent
input or machine-specific target enters the accepted program. CLI JSON output
is a lossless presentation of finite records, not a second scientific gate.
Compilation/static inspection is allowed before the public pin; execution or
import of scientific routines is forbidden before that pin and byte readback.

```text
G01_KERNEL             all 15625 states, five affine generators/involutions,
                       U for both parity cases; theta recursion for n<4096;
                       counters 2,3,7,8,2^80+3 and the declared mixed head
G02_DIRECT_QDD         all625 piston heads; independent Gram-factor audit;
                       n=0 and two changed counter/q/r adapters;
                       density idempotence/trace and five-field dependency audit
G03_PROFILE_OWNERSHIP  required completion-manifest sections, three stages/legs,
                       all18 record schemas and69 uniquely owned fields,
                       exact leg inventories and field references,
                       explicit unresolved physics, no U imports
G04_TESSERACT          independent cubical incidence on all32 edge and24 face
                       bases; d^2=0, six source injections and nontriviality
G05_TORUS             independent periodic incidence, all96 face and64 edge
                       bases; boundary^2=0, windings and six source injections
G06_WAVE              exact complete shell reference and independent pointwise
                       recurrence on zero, four unit sources and (1,-2,2,-1);
                       psi2 for those six sources and psi3 for the mixed source
G07_BATCH             all625 balanced v, explicit Cartesian pair enumeration,
                       rank/unrank, finite ratios/zero, fresh tags, q(d)=25m
G08_PERSIST_ZERO      n0=0,7 crossed with zero, (1,1,1,1), (1,3,2,4) pentits;
                       three cuts, actual U successor, reset/persist/readback,
                       zero append and rejection of history gaps/duplicates
G09_PREFIX            six specified pointed heads, lengths0,1,2,3; actual U,
                       A age, QDD anchoring, geometry/wave age, exact clock,
                       retained header and LOW/HIGH versus five-cell control
G10_TYPES             explicit malformed heads and prefix lengths are rejected
```

The six G09 heads are `(0,(0,0,0,0,0,0))`, `(7,(0,0,0,0,4,3))`,
`(0,(1,0,0,0,0,0))`, `(0,(1,1,1,1,0,0))`,
`(7,(1,3,2,4,1,0))`, `(2^80+3,(1,3,2,4,1,0))`.
G02's two changed heads have (n,q,r)=(1,4,2),(2^80+3,1,3).
Exact fixture details and all finite loops are fixed by the accepted code;
section 3 supplies the uniform argument beyond the finite audits.

## 5. Systematics, prior exposure and failure threshold

The target is deliberately result-exposed. Registered QDD, centering,
Maxwell and photon recurrence identities and the coincidence owner freeze
were read before specifying this candidate. The expected mathematical
identities are consequences of explicitly chosen definitions. This probe
does not claim a blind prediction or evidence that the choices are forced.
It is useful as a complete executable interface with falsifiable conformance,
not as empirical validation of its selected physics dictionary.

The six choices that would otherwise conceal physical debt are recorded:
pointed/reset anchor; provenance-preserving equality; three distinct source
injections and two-slice initialization; A/wave/U age alignment; complete
incidence with unit gain and atomic whole-batch write; singleton context and
cache-only reset. PROFILE.json supplies finer-grained choice identifiers.
They are not registered T claims. If physical source, instrument or occurrence
evidence contradicts a choice, the candidate may fail its later physical gate
even when all present conformance gates pass.

Failure threshold is **zero exceptions and exact equality**, no tolerance.
Any failed required clause or G01--G10 fires the sole claim. Scientific
failures print FIRED/SCIENTIFIC-FIRED and retain exact stdout with exit zero;
they must be published, not repaired in place. An unexpected execution error
or integrity failure yielding no completed gate record disposes this pin by
the repository's abandoned-pin procedure. Never edit the frozen verifier,
dependencies, chosen maps, test set, thresholds or scientific scope to rescue
the outcome. A correction requires a new identifier and new preregistration.

## 6. Action layer, exclusions and disposition

The current action layer is **L1 encoded mathematical conformance**. The
geometry and history records are explicitly typed target data for future
interpretation gates; naming their carriers does not pass an L1->L2 or L4->L5
physical lift. The inherited photon characteristic gate retains only its
registered restricted transfer scope. It creates no source or detector law.

In particular this probe does not test or register
COINCIDENCE-RECORD-FREQUENCY, resolve QDD-INSTRUMENT-APPARATUS,
QDD-INSTRUMENT-CLASS-COMPLETENESS, QDD-TERMINAL-EVENT-SEMANTICS,
BELL-CAUSAL-ACCOUNTING, PHOTON physical realization, SI metrology, a complete
physical geometry selector, or L6 measure/self-location. It does not claim
that its atomic symbolic batch is already an observed apparatus event.
The owner freeze's simultaneous finite population reading, fresh-cut tokens
and probability firewall remain intact. Issue #539 remains its separate
definition/physical-contract lane. No old probe is resumed or reclassified.

After public pin and readback, run once from a clean Linux-compatible checkout
at the exact pin, capture stdout/stderr and source hashes, and preserve the
result. Public independent CI replay on x86_64 and aarch64 must compare exact
bytes. Only the earned conditional mathematical scope may be reported.
One probe per PR, merge without squash or rebase after policy/scientific and
manual security checks. Public claims remain unregistered and Canon unchanged;
any later fold requires its own explicit authority and evidence checks.
