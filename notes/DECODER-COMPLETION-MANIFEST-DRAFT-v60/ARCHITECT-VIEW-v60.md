# S1 — Principal-Architect Assessment of TWIST-J Public Canon v60

**NON-CANONICAL.** Non-normative assessment, no authority, no Canon change,
no file under `canon/` touched. Paths of the form `C:/j/twist-j-manifest/...`
refer to the author's local working area and are not part of this repository.

Role of this document: a software-architecture review of the TWIST-J v60 public
canon, treating the programme as a large software system. It is a diagnostic
instrument in the notes/NON-CANONICAL lane: it changes no status, is not a
submission, and asserts nothing beyond what the cited sources assert.

Sources: the Read-phase working files R1–R5 in `C:/j/twist-j-manifest/work/`
(each line-cited against the v60 checkout at `C:/j/twist-j`), and the canon
sources themselves where noted. Line citations of the form `CANON.md L…` refer
to `C:/j/twist-j/canon/CANON.md` at tag `canon-v60` (content commit
`18b21bdaf2c2…`, R5 §0). Status letters: [T] theorem, [D] dictionary reading,
[C] computation, [H] hypothesis, [O] open obligation, [F] falsified.

Framing honored throughout (owner's instruction): J-uniqueness is **out of
scope** — the canon's "no uniqueness of J" disclaimers are fine and not under
review. The two questions under review are:

- **(a) Sufficiency** — does this architecture suffice for complete physics?
- **(b) Decoder forcing** — is there a forced (canonical-up-to-equivalence)
  decoder, several inequivalent ones, or none?

---

## 1. SYSTEM DECOMPOSITION

The system decomposes cleanly into five planes. For each: the contract, and
the implementation status against that contract.

### 1.1 Runtime (kernel): `U` on `Omega = N_0 x F_5^6`

**Contract.** A closed, autonomous, exact deterministic update:
`U(n, psi) = (n+1, g_sigma(psi))` with drive bit `theta_n = s_2(n) mod 2`
(Thue–Morse parity carried by exact local counter closure — no external tape),
selector `sigma = z_6(psi) + 2 theta_n mod 5`, dispatching one of five
registered generators `a..e` (CANON.md L295–313; R1 §1.1). Event logs are
**derived orbit records, not state** (L310–312) — the runtime has no hidden
mutable state beyond `(n, psi)`.

**Status: IMPLEMENTED and closed.** ODOMETER-INTERNALIZED [D] certifies
autonomy; FIRED-COMMUTATOR-NOGO [T] characterizes fired dynamics as spatially
abelian (R1 §1.1). The one honest caveat the canon itself files at the top of
section 3: *"No derivation or uniqueness of this architecture from J or M_J is
claimed"* (CANON.md L1863–1864; R2 §5). In software terms: the runtime is a
frozen, fully specified reference implementation, but the runtime **spec is a
declared input** (DEF-ARCHITECTURE — at v10 already the largest interposer,
159 direct REQUIRES edges, declared *beside* J, not derived from it; R5 §3.1).
That is acceptable for both owner questions, which quantify over this runtime
as given.

### 1.2 Data plane: `K`, orbit records, logs

**Contract.** `K` = the set of forward `U`-orbits (CANON.md L455) is the
decoder's base set; the quadratic leg refines it to the pointed
`K_QDD = {(U^n(0,x))_{n>=0} : x in F_5^6}` (DEF-QDD-DOMAIN-K0, L1138–1141;
15625 orbits). Record types `MatterData / GeometryData / ObservableHistory`
are **open record types**: "fields exist only where a registered claim defines
them" (L455–457) — the type system is deliberately coupled to the registry.

**Status: PARTIALLY IMPLEMENTED.**

| Data object | Status |
|---|---|
| `K`, `K_QDD` | defined; `K_QDD` fully typed with head convention |
| `MatterData_QDD` | the **only** concrete record schema in v60: 5 typed fields with tags, fixed ZERO branch, no computation rule (DEF-QDD-MATTER-RECORD, L1192–1204) |
| `MatterData` (generic) | open type, no fixed field list |
| `GeometryData`, `ObservableHistory` | **typed names only — zero registered fields** (R1 §1.3) |
| Logs | derived records `(lambda(U^k omega_0))_{k>=0}` for registered `lambda` only |

Architecturally this is a schema-on-read data plane with exactly one table
defined out of three.

### 1.3 API / view layer: the decoder

**Contract.** A **read-only typed partial interface, not a completed total
map** (CANON.md L454): three functional stages
`D_matter -> D_geom -> D_clock` (partial maps with explicit `dom(...)`,
L459–467) crossed with three independent reading legs
`D_linear / D_binary / D_quadratic` (READING-SPLIT [D], L1092–1096). Stages
and legs are **independent axes**; nothing transfers between legs via a shared
stage (L504–505). Dependency graph declared acyclic: "None of these outputs
feeds U" (L473–474). Totality, uniqueness, completeness of `D` are explicitly
**not claimed** (L474–475); "No umbrella full-decoder completeness claim is
registered" (L477–478).

**Status: TYPED, SPARSELY IMPLEMENTED.** Detailed matrix in section 2.

The read-only property deserves an architect's note: it is a **declared
property of the interface, not a theorem about all extensions** (R1 §4.1). A
writeback extension is not forbidden — it is priced: it requires seven new
public artifacts (newly typed architecture, output schema, write-channel type,
autonomous-state codomain, protocol class, dependency graph, separately
registered + preregistered claim; CANON.md L480–487), and registering it would
be a *new* architecture, not a falsification of this one. v60 even exhibits
the pattern in miniature: the direct read-only port `b_W` is proved a forced
singleton in its frozen class with `feeds_U = false`, **and ownership is
deliberately not adopted** (QDD-PURE-RECORD-PORT-UNIQUENESS [T],
L1503–1514; R1 §4.3).

### 1.4 Spec + test ledger: registry, evidence, gates as CI

**Contract.** `REGISTRY.tsv` (320 claim rows) is the normative spec ledger
with a rigid status ladder `T-LOCK > T > D > C > H > O > F` and the rule "no
summary may exceed the status or scope of its source" (POLICY.md L27–33; R5
§1.1). `DEPENDENCIES.tsv` (577 edges) is the dependency graph, machine-checked
acyclic by `tools/check_ledger.py`, with typed edge semantics (a T row cannot
REQUIRE a C/O row; the honest relation is BOUNDED_BY — R5 §3.2). Evidence
classes (INLINE_CANON / REPRODUCTION / PUBLIC_PROBE) each carry an
architecture requirement; the computation gate is **byte-identical stdout on
x86_64 and aarch64** against a committed `EXPECTED.txt` (POLICY.md L136–155).
Probes are the preregistered test suites: six frozen PREREG fields, immutable
thresholds, sealed after execution (R5 §1.4). `GATES.tsv` is the cross-layer
CI: **11 gates**, every L1–L6 lift must name one; a bridge with no gate is by
construction UNRESOLVED (R5 §1.6).

**Status: IMPLEMENTED and unusually disciplined.** Gate topology as of v60:
1 closed by construction (L1→L5 log projection), 2 dictionary lifts closed at
D only (Born reading; TM-SYM2 Born measure — explicitly *no all-lift
uniqueness*), **1 terminal FIRED_NEGATIVE** (GATE-L1-L5-TM-SYM2-SELECTOR-STREAM
— later work "does not reopen, move, or repair" it), and 7 OPEN lifts/
selections including two that point *downward* (L2→L1 tracekernel selection,
L5→L1 minimal-read selection) (R5 §1.6 table). In CI terms: of 11 pipelines,
one is green by definition, two are green at documentation grade, one is
permanently red, seven have never passed. **No theorem-grade lift into L5 or
L6 exists anywhere.**

### 1.5 Interface schema (IDL): DEF-DECODER-COMPLETION-CONTRACT

**Contract.** CANON.md L489–645 (+ factor-canonicity overlay to ~L1090)
defines, "for audit purposes only," the schema a decoder-completion candidate
must publish: 6 top-level id slots, 10 manifest families
(`carrier / record_field / stage / leg / bridge / quadratic / physics /
measure / closure / obligation`), plus 7 overlay manifest families with
tri/quad-state claims (`RESOLVED/UNRESOLVED/NOT_APPLICABLE`,
`TRUE/FALSE/UNRESOLVED`, `DEFINED/NONE/NOT_CLAIMED/UNRESOLVED`); **no bare
null anywhere** (L618–627); totality only relative to named domains; an
8-row forbidden-inheritance table (L1065–1080); and a non-evidence clause —
"syntactic conformance … is not evidence and cannot change a public status"
(L634–645) (R1 §2–3).

**Status: SCHEMA ONLY, ZERO INSTANCES.** v60 publishes no candidate, no
`candidate_id`, no filled slot; the canon's disclaimers jointly cover the QDD
corpus: "These results fill no decoder-completion-contract field" for the
post-v59 results (L1618–1619) and "Nothing here fills the decoder completion
contract" for Route A (L1128–1129) (R1 §6.2 item 1). The IDL
exists; no implementation has ever been compiled against it. Our own draft
(the sibling task) is the first instantiation attempt, and by the
non-evidence clause it is a diagnostic, nothing more.

### 1.6 Release process: canon versions

**Contract.** Authority = public `main` at the declared tag; `STATUS.md`
decides; anything else is "a release candidate, not a second authority"
(R5 §1.1). Releases fold already-merged, sealed probes into registry rows;
thresholds never move post-pin; fired falsifiers are preserved, not deleted.

**Status: FUNCTIONING, conservative.** v55→v60 arc: 280→320 claims, T
165→199, gates 10→11, reproduction witnesses constant at 23; each release is
a conservative fold with almost no pre-existing row moving (R5 §2). Notable
release-engineering precedents: v57 *tightened* a frozen clause rather than
folding it verbatim and recorded the deviation as a deviation; v60
deliberately consolidated probe sub-rows into 13 named theorem scopes rather
than mechanically minting 40 rows (R5 §2.3, §2.6). This is a release process
most software organizations would envy: append-mostly, evidence-gated,
regression-preserving.

### 1.7 One-paragraph verdict on the decomposition

The system has a complete, frozen runtime; a data plane with one of three
record types implemented; an API layer that is fully *typed* but mostly
*unimplemented*; a spec/test ledger and release process that are genuinely
strong; and an IDL for API completion with zero instances. The architecture's
distinguishing virtue is that **every gap is typed and owned** — there are no
silent nulls anywhere in the design, only named UNRESOLVED slots with named
owning claims.

---

## 2. INTERFACE ANALYSIS: the decoder matrix

### 2.1 The stage × leg matrix

Stages and legs are independent axes (CANON.md L504–505), so the honest
picture is a 3×3 matrix plus per-axis infrastructure. Legend:
**REG** = registered content at [T]/[C] grade; **DICT** = registered [D]
reading; **TYPED** = typed name/signature only; **OPEN** = named [O] owner.

| | `D_linear` | `D_binary` | `D_quadratic` |
|---|---|---|---|
| **`D_matter`** | CODEC-TR4 [T] — the linear readout algebra: `Tr_4(M_J x) = 2 Tr_4(x) − 5 x_c`, scalar multiples of `Tr_4` the only multiplier-reading covectors (L2137–2149) — **REG** | GYRON-DENSITY [T] rho=1/6; matter channel reads the isolated TM pair `(0,0)` of density 1/6 via TIME-CUT-READING [D] (L1103–1121) — **REG + DICT** | **The load-bearing cell.** Full exact algebra exists (QDD Route A: `D_QDD_direct = F_QDD ∘ Q_QDD ∘ beta_QDD`, 15625/15625 checkpoints, 313 fibres, QDD-ALGEBRAIC-FACTORIZATION [T] L1230–1241) + the only concrete record schema (MatterData_QDD) — but the decoder action itself is **OPEN**: QUADRATIC-DECODER-DATA [O] is STOP; Route A fills no contract field ("Nothing here fills the decoder completion contract", L1128–1129) — **REG algebra, UNADOPTED; OPEN owner** |
| **`D_geom`** | (no registered geometry content on the linear leg) — **TYPED** | spatial channel sits on the silent pair `a,c`: CURVATURE-HISTORICAL-TRACE [T] (`Tr_V(K_hist^2) = −881/8`), CURVATURE-HISTORICAL-GAUSS-SPLIT [T], KERNEL-MACRO-READING [D] (space = affine translational sector) — but the operator is "one historical construction, now typed exactly," **canonical selection OPEN**: CURVATURE-OPERATOR-CANONICAL [O], TRACEKERNEL-CURVATURE-FORCING [O] (R1 §5.5) — **REG witness + DICT, canonicity OPEN** | piston wedge annex (PISTON-2X2-RESHAPE-WEDGE [T], wedge-blindness of occurrence weights) explicitly claims nothing about what a decoder should read (R1 §5.4) — **REG algebra, no reading** |
| **`D_clock`** | — **TYPED** | dimensionless tick `2 pi/5` per tick (METRO-TICK [T]) read through TIME-CUT-READING [D] — **REG + DICT, dimensionless only** | — **TYPED** |

Codomain status: `MatterData_QDD` concrete; **`GeometryData` and
`ObservableHistory` have zero registered fields** (R1 §1.3). So the D_geom
and D_clock rows of the matrix have no typed output schema to land in — they
are signatures over undeclared record types.

### 2.2 Where the layering is clean

1. **Stage/leg orthogonality is enforced, not just declared.** Cross-leg
   relations exist *only* as explicit `bridge_manifest` rows with layers and
   gates; the 8-row forbidden-inheritance table (L1065–1080) forbids exactly
   the inferences a sloppy design would make silently (quadratic
   factorization → binary factorization; effect equality → instrument
   equality; common numeric value → typed bridge; one MatterData field →
   every field). The v60 disclosure is a model instance: `|QCarrier_QDD| =
   313` equals the CENSUS-313 attractor count, from a different origin,
   partitions sharing no block — "No cross-leg identity is claimed"
   (R1 §5.4/disclosure). A weaker architecture would have folded that
   numerical coincidence into a claim.
2. **The acyclic read-only dependency graph** with the writeback boundary
   priced explicitly (7 artifacts) — the design separates (i) emitting a
   record, (ii) declaring no write target, (iii) proving completion-wide
   terminality, which naive designs conflate (R1 §2.10).
3. **Equality as a declared datum.** Every carrier declares its own
   `equality_id`; QCarrier keeps two typed slots even where coordinate values
   coincide (DEF-QDD-QCARRIER-EQUALITY: "equal coordinate values do not
   collapse the two typed slots"). This is disciplined nominal typing.
4. **Adopted inputs are labeled as inputs.** The effect pair
   `E_low/E_high` and Born pairing are "adopted dictionary inputs … not
   derived from J" (L1189–1190); the magnetic axiom pair is "an explicit
   INPUT" (R3 §1). No fitted parameter masquerades as a derivation.

### 2.3 Where responsibilities leak (or thin out)

1. **The quadratic cell holds an unadopted reference implementation.**
   Route A supplies exact referents for every one of the 12
   `quadratic_manifest` slots (R1 §5.2 table), the keystone factorization is
   theorem-grade, the direct port `b_W` is proved unique in its frozen class —
   and yet QUADRATIC-DECODER-DATA stays STOP because *adoption* (ownership,
   the registered write map, the L4→L1 gate) is withheld. This is not a leak
   but a deliberate gap between "code exists and passes tests" and "code is
   merged as *the* implementation." An architect should flag it as the
   cheapest large win in the system: the adoption decision is governance
   work, not new mathematics — but it is precisely the decision the canon
   refuses to make without a forcing or selection principle, which is
   question (b).
2. **D_geom is a stage with a witness but no codomain.** A curvature
   operator exists as a typed historical construction with exact invariants,
   but `GeometryData` has no fields, so nothing typed can be emitted. The
   stage signature `D_geom : K x MatterData -> GeometryData` is currently a
   function into an empty record type.
3. **D_clock is terminal but empty.** Its entire registered content is the
   dimensionless tick; the bridge that would fill it
   (SQRT-PHI-TIME-GRAVITY [O]) is STOP with its source domain, branch
   selector, and Y-to-D_clock map all unfrozen (R4 §1).
4. **One genuine soft spot: CENTER-SPLIT-SELECTION [D]** rests on a declared
   *external import* (4D Z_N self-duality window) — the only dictionary in
   the surveyed foundations whose door is not internal algebra (R2 §1). The
   registry fences it ("never promoted past the import"), but it is the one
   place where an outside dependency is load-bearing for a reading.
5. **The leg/stage matrix is sparse by declaration, not by accident** — but
   the sparseness is asymmetric: D_matter × D_quadratic has ~30 [T] rows of
   machinery; D_geom and D_clock have essentially one construction and one
   tick. The API surface is deep in one cell and nominal elsewhere.

---

## 3. THE FORCED-DECODER QUESTION AS SOFTWARE

### 3.1 Precise formulation

Fix the published IDL (DEF-DECODER-COMPLETION-CONTRACT) and, per scope, a
**frozen candidate class** and a **frozen candidate equivalence** — the
contract requires the equivalence to be an independently frozen typed output
isomorphism `h : Y_1 -> Y_2` preserving every owned field, equality,
normalization, effect, outcome label, orientation datum, and transport, with
`h ∘ D_1 = D_2` on the common domain, and requires
reflexivity/symmetry/transitivity/closure proved on the complete class before
classes are counted; "a bijection invented after seeing the output does not
define an admissible equivalence" (CANON.md L757–774; R1 §3.5). Then the
three outcomes are:

- **FORCED DECODER** = *uniqueness of implementation up to the frozen
  equivalence*: the contract (plus the registered constraints) is satisfied
  by exactly one equivalence class of implementations. The contract even
  provides the universal-property formalism for asserting this: the
  **maximal-invariant** clause — `D` strictly invariant under the frozen
  invisible-transformation class, every admissible invariant `A` factoring
  through `D` by a unique typed mediator `A_bar` with `A = A_bar ∘ D_bar`,
  with completeness of all four ingredient classes proved (L776–806; R1
  §3.6). In category-theory-flavored software terms: the decoder is the
  universal (initial/terminal) object in the frozen category of admissible
  readouts, and every other readout is a view derived from it.
- **SEVERAL DECODERS** = the contract is satisfiable by at least two
  implementations *not* related by any admissible `h` — inequivalent
  implementations of one spec. Note the discipline: "inequivalent" is only
  well-typed once the reduction/equivalence calculus is complete, which is
  why METRO-REDUCTION-CALCULUS sits under this question (R4 §3.1 item 3).
- **NO DECODER** = the contract is unsatisfiable over the frozen class
  (class provably empty).

Crucially the canon's own obligations are *natively instrumented* with
exactly this trichotomy. CURVATURE-OPERATOR-CANONICAL closes with the literal
verdict alphabet **{UNIQUE, NONUNIQUE, EMPTY, STOP}** (REG L180; R4 §1);
METRO-EDGE-SCALE "closes negatively if two inequivalent selectors survive
every named gate, so no canonical selector exists" (REGISTRY.tsv L157);
COLOR-MEASURE-SELECTION's
NEG is "no lift or more than one inequivalent lift." The forcing question is
not a philosophical gloss we are adding — it is compiled into the closure
conditions.

### 3.2 Row-by-row mapping of the three outcomes

| Canon row | Decides forcing for | FORCED when | SEVERAL when | NONE when |
|---|---|---|---|---|
| CURVATURE-OPERATOR-CANONICAL [O] (ROOT) | D_geom stage map / geometry carrier choice | verdict UNIQUE | NONUNIQUE | EMPTY |
| MINIMAL-READ-DERIVATION [O] (ROOT; GATE-L5-L1-MINIMAL-READ) | `read_convention_id` — the L5-read → L1 coin | complete typed derivation uniquely forces `w=1, beta_1` *without* MINIMAL-READ as premise | complete nonempty class contains compliant beta_1 AND beta_3 realizations | (unique beta_3 = forced-but-different; class-empty branch not separately named) |
| Factor-canonicity overlay (DEF, L647–1090) | any one (stage, leg, scope) | maximal-invariant DEFINED with all four conditions proved + nontriviality certificate | candidate class counted at ≥2 equivalence classes | class completeness proof yields zero members |
| METRO-EDGE-SCALE [O] | metrology selector on the phi ladder + SI clause | canonical selector derived | "two inequivalent selectors survive every named gate" | — |
| COLOR-MEASURE-SELECTION [O] (ROOT) | color-sector L4→L6 measure | exactly one canonical normalized lift | more than one inequivalent lift | no lift |
| ENTROPY-LAYER-BRIDGE [O] (ROOT; GATE-L2-L5-ENTROPY-BRIDGE) | *existence* of the measure-theoretic bridge on the binary leg (measurable equivariant map with exact pushforward Law_W; L2→L5 — upstream prerequisite of any future L6 reading, which would need its own gate) | (existence row, not uniqueness: POS = class `A_A` nonempty by one exhibited exact map) | — | NEG only by a complete theorem `A_A = empty` |
| TT-VECTOR-STATE-NORMALIZATION, DE-CONFORMAL-WEIGHT [O] | sector-local normalization / dictionary selection | unique admissible normalization / unique Delta_DE selection | — | every admissible one violates constraints |
| QDD nonselection corpus [T]/[C] | instrument / apparatus / encoding selection by the current API | — | — | (see §3.3: proves *underdetermination*, a fourth, weaker statement) |

The minimal decisive set for question (b), per the frontier graph:
**{CURVATURE-OPERATOR-CANONICAL, MINIMAL-READ-DERIVATION,
METRO-REDUCTION-CALCULUS}** — one verdict each on geometry, read convention,
and the equivalence calculus that makes "inequivalent" well-typed (R4 §3.1).
Any NONUNIQUE outcome already answers the owner's question in the "several
decoders" direction without waiting for the rest.

### 3.3 What the QDD nonselection results already prove — and why it is a result

In software terms, the v59–v60 QDD corpus proves theorems of the form:

> **The currently published API surface does not select the implementation.**

Specifically (all [T] unless noted, R1 §5.3):

- QDD-INSTRUMENT-NONSELECTION: at fixed effects/weights, the injection into
  post-state instrument classes admits a rational orthogonal dilation
  *universally* — existence of a dilation is available to every candidate,
  hence selects none.
- QDD-J-AFFINE-APPARATUS-NONSELECTION, QDD-J-CENTRALIZER-NONSELECTION, and
  the record/terminality block: each plausible selection principle (ray
  terminality, strict idempotence, S_4 record-partition naturality) does pin
  the Lueder class — but each is "a conditional selector, not a law derived
  from J, Omega, U, the decoder, the record protocol or Nature"
  (CANON.md L1368–1370). I.e. *if you add axiom X, the implementation is
  pinned; nothing in the system forces axiom X.*
- QDD-U-INDUCED-FINITE-NONSELECTION [C]: 900 record-delay pairs classified,
  eligible set empty — the frozen occurrence law is realized by nothing in
  that family.
- Static-encoding nonselection: at least two disjoint exact encodings of the
  pure-record port into K decode the same records; "the decoder signature
  does not select an encoding" (L1495–1501).
- And one **local forcing positive**: QDD-PURE-RECORD-PORT-UNIQUENESS — the
  direct read-only port `b_W([v]) = (v^T G v, vv^T G/(v^T G v))` is a
  *forced singleton in its frozen class* (L1503–1514). So forcing theorems
  are provable in this system when the class is right; the machinery is not
  vacuous.

An architect must state plainly: **this is specification-completeness
analysis, and the negative results are deliverables, not failures.** They
establish that the current interface underdetermines the implementation —
which is exactly what one needs to know before asking question (b) honestly.
They carve the boundary between "what the spec pins" (the factorization
identity, the port in its frozen class, the projector pair inside its stated
class) and "what only an added axiom pins" (instrument, apparatus, encoding,
event semantics). The forced-decoder question is thereby sharpened from "is
there a canonical decoder?" to "**which additional frozen class/axiom, if
any, is itself forced by the registered architecture?**" — and that is
precisely what the O2a noncircularity fence demands (a positive principle
stated *without* COMM-SAT, Xi_T=0, idempotence, ±Q, Lueder, or the target
effects as inputs, with an independently testable consequence; R5 §2.6).

### 3.4 Honest architect's expectation

Nothing in v60 predicts the verdict. But the shape of the evidence is
informative: every attempted *internal* selection principle so far is either
conditional (QDD), noncanonical (TM-SYM2 selector stream — 48 selectors in 4
free gauge orbits, gate FIRED_NEGATIVE), or open. The one unconditional
forcing theorem (`b_W`) lives in a narrow frozen class. A defensible prior is
that forcing, where it exists, will be **class-relative** — "unique within
this published frozen class" — and the programme-level question will reduce
to whether the class freezes are themselves forced. The contract anticipates
exactly this regress: that is what the maximal-invariant completeness
conditions (all four, including completeness of the invisible-transformation
class) are for.

---

## 4. SUFFICIENCY AUDIT

### 4.1 Domain matrix: exact algebra / registered reading / physical completion

Consolidated from R2 (foundations: CANON sections 1, 3, 4, 9, 10) and R3
(physics: sections 5–8, 11–17). "Physical completion" = measure + dynamics +
SI/continuum contact, per R2's tiering.

| Domain | Exact algebra [T]/[C] | Registered reading [D] | Physical completion |
|---|---|---|---|
| EM / Maxwell | strong (projections, center-split, monopole fifths, full finite Maxwell chain MAXWELL-BIANCHI/GAUSS/AMPERE/OBSTRUCTION-P) | AXIOM-PROJECTION-DICTIONARY, MAXWELL-CLOSED, ABELIAN-FACE-DICTIONARY, CENTER-SPLIT-SELECTION (on an external import) | **ABSENT**: no continuum limit, no Lorentz force/EOM, no U(1) dynamics; no Coulomb-phase statement exists in either direction — the falsified pair PHOTON-KAPPA-LEMMA/PHOTON-WINDOW-PROOF **[F]×2** fell on the photon-window route, and the canon expressly states no massless-Coulomb-phase conclusion follows from it (CANON.md L3711–3713) |
| Photon | strong (window coordinates, universal bit, kappa bounds) | none dedicated | **FALSIFIED ROUTE**: PHOTON-KAPPA-LEMMA [F], PHOTON-WINDOW-PROOF [F]; no propagator, no physical-photon conclusion |
| Electron | strong (16 identities, double cover, sign laws, Dirac-step theorems, Gaussian tower) | best-read domain: g=2, sign, Dirac step, ladder root — zero fitted parameters | **OPEN**: coupling (QUANT-SUBSTRATE [O]), no 3+1 field theory, no SI mass |
| SR / boosts | deepest [T] ladder (drift theorem, coin classification, split-prime rapidity block) | 4 unforced [D] rows on one axis | **OPEN**: forcing (MINIMAL-READ-DERIVATION [O]), no rotations sector, no SI c |
| Kernel / census | enormous (CENSUS-313, synchronization, wedge, carry, TM blocks) | exactly **one** [D] (KERNEL-MACRO-READING: space) | **OPEN×2**: measure (ENTROPY-LAYER-BRIDGE [O]), clock/gravity (SQRT-PHI-TIME-GRAVITY [O]); widest algebra-to-physics gap |
| CP/T/CPT | clean involution algebra (Z2-PLACES-SPLIT) | one dictionary sentence in TWO-PLACE-PHYSICS | **ABSENT**: no physical CPT operator, no CP violation, no T dynamics |
| Two places | deep number theory (ramification census, h=1, regulator = 2 log phi, CM pencil, L4 phase) | TWO-PLACE-PHYSICS, I-BILOCATED, SILVER-SIBLING — the decoder's architectural skeleton | **OPEN**: QUADRATIC-DECODER-DATA [O]; forcing of the write/read assignment explicitly not claimed |
| Forces (finite Maxwell + gravity channel) | exact finite chain complex | force dictionaries (FORCE-AS-CURVATURE, COULOMB-PROJECTION, FORCE-POLAR-SIGN) | **ABSENT**: no continuum/scaling theorem, no charge EOM |
| alpha | ALPHA-SEED [T] (1/p), ALPHA-PREFACTOR-UNIFICATION [T] | committed D-form; alpha^-1 = 137.035999190 as **fenced witness** vs CODATA, deliberately not a prediction | **OPEN**: bridge from seed to form underived; running/scheme both [O] |
| Masses | exact coefficient identities (MU-TAU-COEFFICIENT, MU-EXCHANGE-IDENTITY, PARITY-LAW) | committed D-forms on the **single SI anchor m_e** | **OPEN**: no mass mechanism; neutron [O], proton residual [O]; absolute scale behind METRO-EDGE-SCALE [O] |
| Born / quantum probability | BORN-FACE-WEIGHTS [T], staircase, bisector | MEASURE-BORN-VERB [D]; TM-SYM2-PHYSICAL-MEASURE closes one of the two L5→L6 dictionary gates **at D** (frozen lift, no all-lift uniqueness; the other being GATE-L5-L6-BORN-READING); the third L5→L6 gate, GATE-L5-L6-METRO-NORMALIZATION, is open | **OPEN**: no positivity at T, no collapse/update rule, no general-observable Born rule |
| Qubit / Bell | exact magic boundary, Horodecki reencoding census | relational-area reading (conditional on external Hilbert structure) | **OPEN**: BELL-CAUSAL-ACCOUNTING [O] untouched; direction of theorems is QM → integer reencoding, "not conversely"; PHIBIT-NOT-TAU [F] |
| Color / QCD | D5/2I/E8 ladder, character tables, McKay rungs | COLOR-LADDER-DICTIONARY (su(3) by dictionary) | **FALSIFIED + OPEN**: dynamical color [F]; COLOR-MEASURE-SELECTION [O]; no running/confinement/hadrons |
| Gravity / cosmology | KAHLER-CAPACITY, FRW-CANONICAL-FORM, TT-LINEAR-ZERO | GRAVITY-BRIDGE-LAW [D] (`alpha B g = 1`, G_T = (32/33)^2 alpha^20/g, G_nat = 27); cosmology register | **OPEN**: SI value of G explicitly withheld ("stays on the frontier"); no Einstein equations; FRW-INHOM [O]; live [H] exposure NS-TILT, DE-W-CONSTANT |
| Gravitational waves | TT moment underdetermination, Schwarzschild endpoint | TT-SQUARING-DECODER, POL-READ | **OPEN**: emission map TT-SOURCE [O] — no waveforms; QNM-LEAVER-MU [O] |
| Metrology / SI | METRO-TICK [T] (2 pi/5), DEWITT-TWELVES, finite-state rationality | — | **OPEN**: METRO-EDGE-SCALE [O] holds the SI clause; nothing converts a dimensionless form into an SI quantity |

### 4.2 The systemic pattern

Two sentences summarize the whole matrix (R3 synthesis):

1. **The [D] layer carries all physics; the [T] layer is finite algebra.**
   Every physically named object enters only through a dictionary row over an
   exact skeleton, and every dictionary carries an explicit
   no-uniqueness/no-forcing fence.
2. **Dynamics is the systemic absence.** No equations of motion, no
   interaction dynamics, no mass mechanism, no running couplings, no emission
   map. The architecture reads static exact structure; every dynamical law is
   either imported at a family scope (Regge–Wheeler) or open.

### 4.3 What "complete physics" still requires — the explicit list

In interface terms, sufficiency currently fails at the **observable
interface**, not in the kernel (R4 §3.2). The missing items, each with its
owner:

1. **A measure route.** ENTROPY-LAYER-BRIDGE [O] closes the L2→L5 measure
   bridge on the binary/census leg (GATE-L2-L5-ENTROPY-BRIDGE; a further,
   not-yet-existing gate would be needed for an L6 probability reading);
   COLOR-MEASURE-SELECTION [O] is the only live obligation owning an actual
   gate into L6 (L4→L6). Both closed L5→L6 gates (BORN-READING;
   TM-SYM2-BORN-MEASURE) are dictionary lifts at D; the TM-SYM2 lift is
   frozen and carries no all-lift uniqueness. Without these there are no
   probabilities, hence no statistical predictions.
2. **Sampling / realized events (O1).** "SAMPLING NOT PROVIDED" — the
   architecture supplies no physical context key, ready phase, persistent
   update, or registered L1→L5 gate (CANON.md L1576–1579). No detector
   exists. Note the symmetric fence: SAMPLING IMPOSSIBLE is also *not*
   claimed (L1620).
3. **Event semantics (O2a/O2b).** What a completed measurement event *means*
   (noncircularly), and the complete apparatus class with family-level frozen
   equality. Both STOP.
4. **SI bridges.** METRO-EDGE-SCALE [O] (the SI clause — blocks G in SI, the
   absolute mass scale, and every dimensionful number) and
   SCHEME-DICTIONARY [O] (contact with measured couplings at a named scale).
   The system currently emits exact dimensionless rationals and algebraic
   numbers; nothing emits a second, a meter, or a kilogram.
5. **Continuum statements.** No continuum limit anywhere: not for Maxwell,
   not for the FRW cell, not for the boost axis (1+1-dimensional only), no
   scaling theorem (ENTROPY-RG-RETURN explicitly disclaims one), no 3+1
   spacetime.
6. **Bell/locality accounting.** BELL-CAUSAL-ACCOUNTING [O] polices every
   probability-bearing cross-layer bridge and is semantically downstream of
   both O1 and an L6 measure.

### 4.4 Missing-because-open vs missing-by-design

This distinction matters for a fair audit:

**Missing by design (not defects):**
- **Writeback / observer back-action.** The decoder is read-only *by
  declared architecture*; an extension is priced (7 artifacts, L480–487),
  not forbidden. Absence of a write port is a scoping decision.
- **J-uniqueness and architecture-derivation.** "No derivation or uniqueness
  of this architecture from J" is a declared boundary of DEF-ARCHITECTURE —
  and out of scope for this review by the owner's framing.
- **Unregistered engineering readouts** (section 17): excluded from the
  normative canon by policy, not by inability.
- **Fenced witnesses.** The sub-ppb alpha agreement, mu/tau sigma levels,
  Hulse–Taylor 99.83% are deliberately *not* claims — the design refuses to
  book unearned predictive credit. An auditor should score this as integrity,
  not as absence.

**Missing because open (genuine incompleteness, each with a named [O] owner):**
the entire list of §4.3, plus sector items (mass mechanism, QCD dynamics,
emission map, rotation sector, mixing matrices). Every one is a registered
obligation with a frozen closure condition — the system knows exactly what it
is missing, which is rare.

**Missing with a falsified route (neither open nor by design):** the photon's
physical-existence route ([F]×2), dynamical color [F], the TM-SYM2 selector
stream [F] (terminal gate), the phibit reading [F]. The canon archives these
as live constraints — dead code kept as regression tests.

### 4.5 Sufficiency verdict

As a physics *engine*, v60 is a complete and verified kernel with a mostly
unimplemented I/O subsystem. The claim "this architecture suffices for
complete physics" is today **neither established nor refuted**: it is
formally open behind ~12 named obligations, and — importantly for the owner —
the system is *instrumented to refute it cheaply*: three READY sufficiency
tests (GENERATIONS-L3: does the architecture produce exactly three
generations; QUANT-SUBSTRATE: does the substrate realize the Schwinger
first-order coefficient; TT-VECTOR-STATE-NORMALIZATION: does an admissible
normalization yield a numerical r_T(k)) can each end in a NEG that would be a
sufficiency counterexample at [F]-grade cost (R4 §3.2 item 5).

---

## 5. RISK REGISTER + ROADMAP

### 5.1 Risk register

| # | Risk | Severity | Exposure / mitigation |
|---|---|---|---|
| R-1 | **Single deepest formal choke point: METRO-REDUCTION-CALCULUS [O].** It defines the reduction equivalence under which "inequivalent" is well-typed; the ledger records it gating METRO-ADMISSIBILITY(-DIM) (DEP L402/L407), and by a semantic reading — not a recorded TSV edge — the complete-admissible-class quantifiers in the NEG branches of MINIMAL-READ-DERIVATION and METRO-EDGE-SCALE sit behind the same construction (R4 §1 flags this as inference). Three of the manifest's four measure/read slot families trace back to it (R4 §3.3). | Critical | Unblockable by anyone but its owner; B partially discharged (METRO-FORBIDDEN-WITNESSES [C]); D and E remain. Highest-priority formal work item. |
| R-2 | **The observable interface is entirely open** (no measure, no sampling, no SI). Question (a) cannot close positively while any of ENTROPY-LAYER-BRIDGE, QDD O1, METRO-EDGE-SCALE stand. | Critical | Parallelizable across three independent owners (see backlog). |
| R-3 | **Forcing may regress into class-freezing.** Every unconditional selection so far is class-relative; the risk is an infinite regress of "unique within the frozen class, class not forced." | High | The contract's maximal-invariant completeness conditions and the O2a noncircularity fence are exactly the mitigations: they force the regress to terminate in publicly frozen, complete classes or in an honest NOT_CLAIMED. |
| R-4 | **Empirical tripwires.** DE-W-CONSTANT [H] is the sharpest: current DESI DR2 / DES Y6 evolving-DE witnesses (up to 21/5 sigma for DESI DR2 with DESY5; DES Y6 reaches 30/10 sigma only on shared data and 11/5 alone) fire nothing because no single headline combination reaches 5 sigma and the two-collaboration route is blocked by the frozen shared-primary-dataset (disjointness) clause; a qualifying disjoint pair at ≥3 sigma each would fire it. NS-TILT [H] awaits CMB-S4. | High (uncontrollable) | Cannot be worked, only survived; monitors, not backlog items. A fire would falsify a register reading, not the kernel. |
| R-5 | **Two [F] pillars removed load-bearing routes** (photon window; dynamical color). The domains now have no live route to their physical object. | Medium | Honest state; roughening question and kinematical color remain open ground for new routes. Not maskable. |
| R-6 | **DEF-ARCHITECTURE as unforced hub** — the runtime spec itself is the largest interposer. | Medium (fenced) | Out of scope for (a)/(b) as framed, but ENTROPY-LAYER-BRIDGE is on record as "the strongest available discharge path for the architecture mezikus" (R5 §3.1) — closing it would also shrink this risk. |
| R-7 | **Process risk: none observed.** Ledger machine-checked, thresholds immutable, two-architecture gate, terminal gates unrepairable. The governance layer is the system's strongest component. | Low | Maintain. |

### 5.2 Backlog, phrased as a software plan

**Epic A — cheap verdicts, start immediately (all READY ROOT, parallel):**
- A1 GENERATIONS-L3 — derive the L3 generation count; NEG (≠3) is a
  sufficiency counterexample.
- A2 QUANT-SUBSTRATE — the Schwinger/Larmor physical gates; a failed
  physical-realization gate fires it.
- A3 TT-VECTOR-STATE-NORMALIZATION — the only route to a numerical r_T(k);
  also a sector-local forced-vs-free test.
These are the system's cheapest integration tests: no live upstream, each
decides by direct construction (R4 §2.3 stratum 0).

**Epic B — the forcing verdicts (question b), parallel with A:**
- B1 CURVATURE-OPERATOR-CANONICAL — the literal UNIQUE/NONUNIQUE/EMPTY
  verdict; sole unblocker of TRACEKERNEL-CURVATURE-FORCING (DEP L561).
  Highest-value single row for (b).
- B2 MINIMAL-READ-DERIVATION — POS branch (a forcing derivation) attackable
  now; the NEG branch's wait on Epic C's class completion is the semantic
  reading flagged in R-1, not a recorded TSV edge.
- B3 (long pole) METRO-REDUCTION-CALCULUS — the equivalence calculus itself.
Any NONUNIQUE result anywhere in B answers (b) as "several inequivalent
decoders" and can short-circuit the epic.

**Epic C — the observable interface (question a), three independent tracks:**
- C1 Measure: ENTROPY-LAYER-BRIDGE (exhibit one exact equivariant map — POS
  needs a single witness, which makes it construction-shaped, not
  classification-shaped) ∥ COLOR-MEASURE-SELECTION.
- C2 Events: QDD O1 (sampling: context key, ready phase, persistent update,
  L1→L5 gate — the carry bank has already fixed the state space, §5.4) +
  O2a (noncircular event-completion principle) + O2b (apparatus-class
  completeness). O2a and O2b are independent of each other and of C1
  (R4 §2.3).
- C3 Units: METRO-REDUCTION-CALCULUS → METRO-ADMISSIBILITY(-DIM) (recorded,
  DEP L402/L407) → METRO-EDGE-SCALE (SI clause; this last link is the
  semantic reading flagged in R-1, not a recorded TSV edge) ∥
  SCHEME-DICTIONARY (measured couplings). Shares B3 as its root under that
  same qualified reading.

**Epic D — decoder adoption:** QUADRATIC-DECODER-DATA. All 12
`quadratic_manifest` referents exist (Route A); what is missing is the
adoption decision with its registered write map and dependency graph. Sensibly
sequenced *after* B1/B2 give a first forcing signal (adopting an unforced
implementation is precisely what the canon has declined to do), or fillable
in a manifest as the explicit "candidate implementation, adoption pending
forcing verdict."

**Epic E — completion coverage (behind C):** SQRT-PHI-TIME-GRAVITY (D_clock
bridge; SI portion behind C3), TT-SOURCE, BELL-CAUSAL-ACCOUNTING (semantically
behind C1+C2), FRW-INHOM, PROTON-RESIDUAL-IS-QCD, ALPHA-S-RUNNING (behind
SCHEME-DICTIONARY), DE-CONFORMAL-WEIGHT, NEUTRON-DELTA-EM, QNM-LEAVER-MU,
DRESS-CROSSCOUNT.

**Monitors (not workable):** DE-W-CONSTANT, NS-TILT, LAMBDA-COCYCLE-ANGLES
(ENRICHMENT, off every critical path) — empirical/mathematical-fire-only
tripwires; plus the armed clauses inside [O] rows (72 alpha^4 witness in
DRESS-CROSSCOUNT; measured-window NEG clauses in NEUTRON-DELTA-EM /
ALPHA-S-RUNNING).

**Definition of done for a fully RESOLVED completion manifest:** the 12-row
core {QUADRATIC-DECODER-DATA, ENTROPY-LAYER-BRIDGE, SCHEME-DICTIONARY,
METRO-REDUCTION-CALCULUS, METRO-EDGE-SCALE, QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS, QDD-INSTRUMENT-CLASS-COMPLETENESS,
SQRT-PHI-TIME-GRAVITY, CURVATURE-OPERATOR-CANONICAL, MINIMAL-READ-DERIVATION,
COLOR-MEASURE-SELECTION}; 14 with TT-SOURCE and BELL-CAUSAL-ACCOUNTING for
full physics/bridge coverage (R4 §3.3). A manifest may be *published* today
with UNRESOLVED slots — and should be, as the tracking artifact.

### 5.3 Why the v60 additions genuinely advance the goal

**The O2 split** (QDD-TERMINAL-EVENT-SEMANTICS + QDD-INSTRUMENT-CLASS-
COMPLETENESS, R5 §2.6) is a textbook decomposition of a blocked monolithic
requirement into two independently attackable, *testable* specs:

- O2a converts "what does measurement completion mean" into a noncircularity
  contract: the principle must be stated **without** the answer's signature
  ingredients (COMM-SAT, Xi_T=0, idempotence, ±Q, Lueder, target effects) as
  inputs, and must carry an independently testable consequence outside the
  selector target. This is exactly the anti-overfitting rule a spec needs so
  that a future "derivation" of the collapse law is not the collapse law
  restated. It directly serves question (b): it defines what would count as a
  *forced* event semantics.
- O2b converts "which apparatuses exist" into a class-completeness contract
  with equality frozen on **whole apparatus families** (memory, ready phases,
  phase transitions, future-output dependence) *before* target comparison —
  closing the loophole where a class is quietly gerrymandered around the
  intended answer. It supplies the "complete admissible physical class" that
  every QDD NEG clause quantifies over — without it, no negative verdict is
  even well-posed.
- Governance value: the parent closes only when O1 + both children close
  *compatibly* — the conjunction is explicit, so partial progress cannot
  masquerade as closure.

**The carry bank** (QDD-EVENT-CONTEXT-BANK [T],
`B = 19702414515172535913561087541248 = 2^66·3^2·7^4·11·13^2·17^2·23`,
104 bits, R5 §2.6) advances O1 the way a good systems result advances an
open protocol problem: it proves the **exact class-relative minimal state
space** of any deterministic, frequency-exact, schedule-invariant sampler for
the 22 Route A contexts — every reachable B-state realization is
transducer-isomorphic to the bank; distinct-context transitions commute;
arbitrary interleaving preserves exact frequency and discrepancy. In other
words: the state machine of the future detector is now a normal form, and
what remains open is exactly and only the *physics binding* — the context
key, the ready phase, the persistent update, and the L1→L5 gate (CANON.md
L1576–1579). O1's remaining surface is thereby reduced from "design a
sampler" to "bind this canonical sampler to the architecture" — a strictly
smaller, precisely enumerated obligation. And both fences are kept: SAMPLING
NOT PROVIDED, and SAMPLING IMPOSSIBLE not claimed — the question stays live
in both directions.

Both additions also improve the *instrumentation* of the owner's questions:
the O2 split adds the noncircularity discipline that keeps a future forcing
claim honest, and the bank turns part of the sufficiency frontier from
open-ended search into a bounded binding problem.

### 5.4 Closing assessment

TWIST-J v60 is, as software, an unusually well-governed system with an
inverted maturity profile: the kernel and the QA/release machinery are
production-grade; the public API is a fully typed but sparsely implemented
interface whose one deep cell (quadratic D_matter) holds a verified,
unadopted reference implementation; and the specification for completing the
API (the contract) exists with zero instances. The two owner questions are
not rhetorical postures but are *compiled into the ledger*: (b) as literal
UNIQUE/NONUNIQUE/EMPTY closure alphabets on five live rows, (a) as a 12-row
obligation set concentrated at the observable interface (measure, sampling,
SI). The QDD nonselection corpus has already delivered the first
architecture-level result on (b): the current API surface provably does not
select its implementation, and each candidate selection principle is exactly
one added axiom away — which converts the forced-decoder question into the
sharply posed form the O2a fence demands. The fastest path to information is
the three READY sufficiency tests plus the two attackable forcing verdicts;
the deepest investment is METRO-REDUCTION-CALCULUS, on which the
well-typedness of "inequivalent decoder" itself depends.

---

**Revision note.** Rev 2, 2026-08-22: six factual corrections + two
citation-precision fixes applied per adversarial fact-check V2; central
theses unchanged.
