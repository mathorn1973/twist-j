# Frontier attack map at Public Canon v66 (NON-CANONICAL)

```text
STATUS:                    ANALYSIS / CLOSURE-AND-FALSIFICATION PLAN PROPOSAL
REVISION:                  2 (owner public review applied, 2026-08-26)
AUTHORITY:                 NOT CANON
PUBLIC CANON:              Public Canon v66 / canon-v66
PUBLIC CONTENT COMMIT:     8f11ec18825aa769308132254e8de35663006a1a
PUBLIC CANON SHA-256:      76de4fb05f7d1aed803e581a7d470e6ed8fd63923603ebe780e91990fb0be279
SCOPE:                     ALL 30 LIVE O/H ROWS OF canon/REGISTRY.tsv
METHOD:                    QUOTE-ANCHORED REDUCTION + ADVERSARIAL VERIFICATION
VERIFICATION RECORD:       28 CONFIRMED / 2 WEAK / 0 REFUTED (see section 2)
COMPANION TABLE:           REDUCTION.tsv (one row per live claim, quote-anchored)
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON/TABLE/STATUS CHANGE: NONE
```

## 0. Revision log

Revision 1 was reviewed publicly by the owner on 2026-08-26 with the verdict
"orientation map yes, executable plan not yet". Revision 2 applies every
review finding. The corrections, so that revision 1 is not silently
reinterpreted:

1. C1 counted "four rows" while naming three; and it overstated jointness —
   the registry keeps O1 separate from O2 and Bell separate from QDD, so one
   carry-bank adoption does not jointly close those rows. C1 is now stated as
   a shared *species* of missing physical adoption, instantiated per row
   through that row's own contract (section 4).
2. C2 was framed as a "core blocking object"; it is a shared *work pattern*,
   not a shared dependency. The ledger carries no dependency among most of
   its rows. `FRW-INHOM` in particular closes by a single construction and is
   reclassified (sections 3, 4).
3. "One freeze serves two obligations" for unbounded memory was type-invalid:
   a physical apparatus family and a metrological protocol class have
   different carriers, equalities and outputs. Two separate typed contracts
   are needed; what can be shared is a template — and an owner lane for
   exactly that template already exists
   ([issue #539](https://github.com/mathorn1973/twist-j/issues/539),
   `DEF-TYPED-APPARATUS-RECORD-CONTRACT`), which revision 1 missed (section 4).
4. C4 is not a ledger-supported common core: no dependency links
   `QUANT-SUBSTRATE`, `NEUTRON-DELTA-EM`, `DRESS-CROSSCOUNT`; the
   substrate-coupling attack decides only the first. The `COLOR`/`PROTON`
   "one freeze, two rows" claim is downgraded to a possible, unproven schema
   reuse (section 4).
5. Direct registry errors fixed: the `MINIMAL-READ-DERIVATION` negative
   witness; the alleged unfalsifiability of `QDD-INSTRUMENT-APPARATUS` and
   `BELL-CAUSAL-ACCOUNTING` (both carry conditional negative closes over a
   frozen complete class); "RH-equivalent" for `LAMBDA-COCYCLE-ANGLES`
   (correct: RH **plus** the grid condition); "nothing missing" for
   `QUADRATIC-DECODER-DATA` (row-specific obligations remain) (section 5).
6. The phase plan is replaced by the owner-reviewed order; revision 1's
   "Phase 0 — no new objects" in fact introduced a new identity, gate,
   extended domain and probe (section 6).
7. The `ENTROPY-LAYER-BRIDGE` "one lemma from a negative close" claim is
   withdrawn: the registered no-go is finite-cylindrical only; the negative
   route needs a genuine rigidity theorem, and three divergent entropy
   branches must be dispositioned first (section 5).
8. Counting errors fixed: C1 rows (three, not four); the kill list heading
   (it named nineteen under a heading of eighteen; the regrouped list in
   section 5 now counts twenty, of which five are actionable now).

`REDUCTION.tsv` gains a `relation` column making the mapping semantics
explicit per row (`pattern` / `species` / `convention` / `standalone`), so C2
membership can no longer be read as a dependency claim.

## 1. Question and method

The owner's conjecture: the 27 O rows have relations, and at the core a part
of them is really one thing. This note tests that conjecture against the
ledger and derives an attack order whose steps are ranked by what *decides*
(closes or falsifies) rather than what merely prepares.

Method. Each of the 30 live rows was read against its full `canon/REGISTRY.tsv`
row, its `canon/FRONTIER.md` entry, its `canon/DEPENDENCIES.tsv` edges in both
directions, its gate ownership in `canon/GATES.tsv`, and the relevant
`canon/CANON.md` passages. Every blocking object attributed to a row carries a
verbatim quote from that row's own scope or falsifier text. A synthesis stage
reduced the rows to a minimal set of shared debts, testing three prior
hypotheses (H1: one physical event/measure law; H2: one recurring
classification method; H3: one scale-selector-to-dictionary chain) rather than
assuming any. Every entry of the resulting reduction map was adversarially
re-verified against the registry text by independent checks instructed to
refute, and all 30 quotes were re-matched verbatim (whitespace-normalized)
against the live registry before filing.

## 2. Verification record

28 of 30 mappings CONFIRMED, 2 WEAK, 0 REFUTED. The two WEAK entries, recorded
so the map is not read as stronger than it is:

- `BELL-CAUSAL-ACCOUNTING` — the C1 debt genuinely covers the instrument map,
  realized outcomes and the kernel `P(a,b|x,y,lambda)`, but the row's STOP
  demands one preregistered attack with further independent fields
  (setting-selection mechanism, correlation/CHSH conventions, measurement
  independence or a frozen replacement, both no-signalling equalities, the
  dimensional audit) that no shared debt carries. Discharging C1 alone does
  not discharge the row.
- `ALPHA-S-RUNNING` — the C3 scheme conventions are needed to *type* its match
  condition, but the positive close equally requires the running itself to be
  derived from the 3/4 seed; C3 makes the row scorable, not closed.

## 3. Verdict on "one thing"

The conjecture is right that a shared structure exists and right that it is
much smaller than 30 rows. Stated precisely, with the revision-2 corrections:

**The dominant shared structure is one method, not one object, and membership
in it is a work pattern, not a dependency.** Nineteen rows are stuck at some
stage of the same engine — the completed admissible-class run, in typed terms
the triple `(P, Comp, Dec)`:

```text
P     a frozen typed package: carrier, whole-family equality, normalization,
      admissible-class boundary, acyclic dependency graph;
Comp  a completeness theorem: every admitted object lies in exactly one
      declared family of P;
Dec   a counted-survivor decision |S| in {0, 1, >=2} under every registered
      constraint.
```

The Canon carries roughly ten pending instances of this triple on different
carriers and has **never completed one positively**. The only finished run
anywhere is the fired-negative `GATE-L1-L5-TM-SYM2-SELECTOR-STREAM`
(48 selectors in four free projective-linear gauge orbits, NONCANONICAL):
proof the engine executes, and the template for what "done" looks like.
Because the carriers differ, nothing transfers between instances except the
template and the discipline; the ledger carries **no dependency** among most
of these rows, and closing one instance closes no other. Within the pattern,
rows split by stage: *definition-starved* rows cannot yet pose their class
(`COLOR-MEASURE-SELECTION`, `TT-SOURCE`, `TT-VECTOR-STATE-NORMALIZATION`,
`SQRT-PHI-TIME-GRAVITY`, `DE-CONFORMAL-WEIGHT`, `PROTON-RESIDUAL-IS-QCD`,
`SCHEME-DICTIONARY`); *classification-starved* rows have a posed class but no
completeness proof or decision (`QDD-INSTRUMENT-CLASS-COMPLETENESS`,
`METRO-ADMISSIBILITY`, `METRO-ADMISSIBILITY-DIM`, `METRO-REDUCTION-CALCULUS`
obligations B/D/E, `CURVATURE-OPERATOR-CANONICAL`,
`TRACEKERNEL-CURVATURE-FORCING`, `MINIMAL-READ-DERIVATION`,
`ENTROPY-LAYER-BRIDGE`, the selector half of `METRO-EDGE-SCALE`).
`FRW-INHOM` is the exception inside the count: it closes positively by a
**single construction** ("an inhomogeneous source construction that reproduces
the public FRW-CANONICAL-FORM identities in the homogeneous limit") and needs
no classification at all.

**The unbounded-memory gap is one named hole, two typed contracts.** Two O
rows name the class verbatim — `QDD-INSTRUMENT-CLASS-COMPLETENESS` ("finite
and unbounded memory") and `METRO-ADMISSIBILITY` ("unbounded-memory
adaptive") — and nothing anywhere in the Canon covers it. But a physical
apparatus family and a metrological protocol class have different carriers,
equalities and outputs, so **one freeze cannot serve both**: what is shared is
the missing template and the zero coverage, and two separate typed contracts
must be written. The template lane already exists:
[issue #539](https://github.com/mathorn1973/twist-j/issues/539) defines
`DEF-TYPED-APPARATUS-RECORD-CONTRACT`, one manifest schema with per-row
profile adapters (QDD data, QDD apparatus, minimal read, linear reading
lift), created precisely so that profiles are instantiated separately and "the
shared schema creates no shared scientific conclusion".

**The event-layer debt is one species, three separate contracts.** The
realized-event and sampling law — O1 transducer (physical context key,
selected ready phase, persistence/reset semantics, ZERO_SUPPORT handling,
exact ordered occurrence law), a registered L1-to-L5 gate that does not exist
in `canon/GATES.tsv`, the terminal-saturation semantics, the induced outcome
kernel — is the same *kind* of missing physical adoption behind exactly three
rows: `QDD-INSTRUMENT-APPARATUS`, `QDD-TERMINAL-EVENT-SEMANTICS`, and
(partially, section 2) `BELL-CAUSAL-ACCOUNTING`. The registry keeps them
formally separate — "O1 remains a separate typed realized-event/sampling
obligation", and on the Bell side "existing QDD obligations remain separate" —
so one adoption drafted once still closes each row only through that row's own
contract. The mathematics beneath all three is fully frozen (the 22-context
Euclidean carry bank, the canonical pure-record map, the frozen effect pair);
all 21 theorems `BOUNDED_BY` the apparatus row narrow the picture, none
supplies the law.

**H3 is false as stated.** `SCHEME-DICTIONARY` owns no gate, and the SI clause
sits in `METRO-EDGE-SCALE`'s registry scope. The empirical wing hangs on three
sibling tokens of one convention species (SI clause over the single `m_e`
bridge; named measurement scheme with scale/threshold and window semantics;
shadow-to-mu inference rule), not on one selector-to-dictionary chain.

**The substrate trio is one debt species, not a common core.** No ledger
dependency links `QUANT-SUBSTRATE`, `NEUTRON-DELTA-EM` and
`DRESS-CROSSCOUNT`; they share only the *kind* of missing object (alpha-power
correction machinery above the closed exact seed/tree theorems). The
substrate-coupling attack decides `QUANT-SUBSTRATE` alone; the other two have
their own witnesses.

**Outside every shared debt (5 rows):** `GENERATIONS-L3` (READY, and the only
READY row owning a registered gate in `canon/GATES.tsv`),
`QUADRATIC-DECODER-DATA` (what is missing is row-specific: the global
`K_QDD = K` identification, the binding gate, and a domain extension that
actually distinguishes the dagger/transpose pair — not any shared object),
`DE-W-CONSTANT` and `NS-TILT` (external survey releases against frozen or
freezable thresholds), `LAMBDA-COCYCLE-ANGLES` (decidable positively only by
external mathematics: the cocycle vector exists **iff RH holds and** every
Cayley angle lies on the `2 pi (1/4) Z[1/5]` grid — RH-plus-grid, strictly
stronger than RH; the internal residual-bound test is one-sided).

## 4. The four shared debts

Semantics: a *debt* groups rows missing the same kind of object. Only the
seven explicit live-to-live edges in `canon/DEPENDENCIES.tsv` are
dependencies; everything else here is pattern or species membership, per the
`relation` column of `REDUCTION.tsv`.

**C1 — EVENT-LAW** (species; 3 rows). One kind of physical adoption,
instantiated per row through its own contract. First freezable piece: one
candidate O1 predefinition on the already-frozen mathematics — adopt the
22-context carry bank as the transducer, declare reduced-p the physical
context key, select one ready-phase vector with a persistence/reset law and
ZERO_SUPPORT branch, state the ordered occurrence law, register the missing
L1-to-L5 gate. The natural vehicle is the QDD-apparatus profile adapter of
issue #539's contract. Auditing that single candidate against the row's
occurrence-law and target-independence conditions is decisive for what O1
still lacks — for that row.

**C2 — FREEZE-CLASSIFY-DECIDE** (pattern; 19 rows). The engine of section 3.
First freezable pieces are per-lane and independent; the two unbounded-memory
contracts (METRO protocol-side and QDD apparatus-side, separately typed,
template from issue #539) are the highest-leverage pair because they are the
only place where two O-row falsifiers name the same uncovered class verbatim.

**C3 — EXACT-TO-MEASURED** (convention species; 5 rows: `METRO-EDGE-SCALE`,
`SCHEME-DICTIONARY`, `ALPHA-S-RUNNING`, `QNM-LEAVER-MU`,
`METRO-ADMISSIBILITY` via R7). Three unwritten convention tokens of one
species. First freezable piece: `SCHEME-DICTIONARY`'s complete STOP list as
one definition-and-manifest package (seed domain `alpha* = 1/5`, strong root
`3/4`, seed ratio `15 : 4` from `reproduce/coupling-metrology`; one named
scheme with scale/threshold conventions; the total map with equality and
window semantics; pinned source manifests; the acyclic dependency graph) —
pure definition work that simultaneously types `ALPHA-S-RUNNING`'s close
condition. The Leaver continued-fraction half of `QNM-LEAVER-MU` is already
computation-ready over the closed Regge-Wheeler potential.

**C4 — SUBSTRATE-DYNAMICS** (species; 3 rows, no ledger dependency among
them). First freezable piece: one candidate substrate-coupling predefinition
with frozen action normalization and regularization, scored immediately by
exact arithmetic against the frozen Schwinger target
`J Jbar / script-Q = 1/(2 pi)`. This decides `QUANT-SUBSTRATE` alone: a
completed failing realization gate fires it negatively, so a finished attempt
is decisive either way — for that one row. Whether the same machinery later
grounds `NEUTRON-DELTA-EM`'s compression channel or `DRESS-CROSSCOUNT`'s
crossing count is open and not claimed.

## 5. Kill list

Twenty of the thirty rows carry a negative route. Grouped by what the single
firing witness needs — five are actionable now; the rest are conditional on a
finished derivation, a frozen complete class, or external data. Corrections
against revision 1 are marked.

**Actionable now** (finite exact computation over already-pinned objects):

- `METRO-REDUCTION-CALCULUS` — one exact transport failure of obligation D at
  the smallest frozen scope (q=2, k=2 over the pinned 1024-tuple family), or
  one allowed/forbidden collision in the catalogue.
- `METRO-ADMISSIBILITY-DIM` — one exact admitted counterexample to soundness,
  completeness, coherence, total normalization or reduction invariance of
  `Cert_joint` versus direct translated-box averages over the enumerated
  q=2, a=2, r=1 families.
- `METRO-EDGE-SCALE` — two inequivalent selectors surviving every named gate;
  the NONCANONICAL outcome shape has already fired once
  (`GATE-L1-L5-TM-SYM2-SELECTOR-STREAM`).
- `LAMBDA-COCYCLE-ANGLES` (one-sided) — one exact finite violation of
  `0 <= M - t_n <= 2M` by certified interval arithmetic; the instrument can
  only fire the row, never confirm it.
- `QUADRATIC-DECODER-DATA` — the only negative clause not already contradicted
  by the exact factorization theorem is "an unregistered input is required";
  an acyclicity/completeness audit of the row's transitive closure decides it.

**Armed by a finished derivation** (binary on completion; an unfinished
attempt decides nothing):

- `GENERATIONS-L3` — the owned gate is binary with no STOP branch: a completed
  L2-to-L3 derivation closes positively at three or fires at anything else.
- `QUANT-SUBSTRATE` — a completed substrate-coupling candidate through the
  Schwinger physical-realization gate closes or fires against the exact
  arithmetic target `1/(2 pi)`.
- `CURVATURE-OPERATOR-CANONICAL` — the classification decision itself carries
  both negative arms (NONUNIQUE, EMPTY).
- `TRACEKERNEL-CURVATURE-FORCING` — once the upstream class is public and
  nonempty, one violating member decides; the eight-of-480 `GL_2(F_5)`
  equivariance boundary is a pre-typed exact negative route.

**Conditional on a frozen complete class or a rigidity theorem** *(revision 2:
this group replaces both revision-1 errors — the misstated `MINIMAL-READ`
witness and the "not falsifiable at all" paragraph)*:

- `MINIMAL-READ-DERIVATION` — fires only when the complete admissible decoder
  class is proved nonempty **and** either contains fully compliant `beta_1`
  and `beta_3` realizations or uniquely forces `beta_3`. One `beta_3` witness
  alone does not fire it; the complete class comes first.
- `ENTROPY-LAYER-BRIDGE` — *(downgraded)* the registered cylinder no-go
  (global solution count zero over all 522 pure-word systems) covers
  finite-cylindrical maps only; the negative close `A_A = empty` needs a
  genuine rigidity theorem extending it to all measurable maps while
  preserving exact equivariance and `Law_W`. Before any of that, the three
  divergent entropy branches must be dispositioned
  (`codex/entropy-mackey-consolidation`, `notes/entropy-selection-recon`,
  `notes/entropy-selection-recon-breaker-m2` per
  `notes/BRANCH-LEDGER-2026-08-24/DISPOSITIONS.tsv`).
- `QDD-INSTRUMENT-APPARATUS` — closes negatively "only for a frozen complete
  admissible physical class proved empty or unable to realize the pair or
  event law"; falsifiable, conditional on the complete class being frozen
  first. Until then, failure to provide sampling remains STOP.
- `QDD-INSTRUMENT-CLASS-COMPLETENESS` — one independently admissible apparatus
  outside a claimed class or violating a claimed family equality; conditional
  on a class being claimed.
- `QDD-TERMINAL-EVENT-SEMANTICS` — a typed admissible completed physical event
  whose post-state record retains a nonzero residual commutator; conditional
  on the C1 event framework existing (a bare mathematical witness is
  explicitly not a physical falsifier).
- `BELL-CAUSAL-ACCOUNTING` — "a complete internally inconsistent contract or
  exact impossibility result for a frozen full admissible class may close
  negatively"; falsifiable, conditional on the complete contract or class.

**External data** (no internal action can fire them; freezing the arming rule
is the internal work):

- `DE-W-CONSTANT` — see section 6, step 1: rule R1 is evaluable today against
  the published DESI DR2 headline constant-w posterior, by a **new** public
  probe.
- `NS-TILT` — fires against CMB-S4; its arming probe (exclusion threshold,
  carrier semantics, labeled non-firing Planck/ACT witnesses) is unwritten.
- `DRESS-CROSSCOUNT` — an exact labeled witness departing from `72 alpha^4`
  at the 0.204 ppm scale.
- `NEUTRON-DELTA-EM` — conditional on a C4 derivation: a derived compression
  channel value outside the measured tier window.
- `QNM-LEAVER-MU` — conditional on the C3 inference rule: an exact spectrum
  incompatible with the preregistered mu interval.

Removed from the list against revision 1: `TT-VECTOR-STATE-NORMALIZATION` —
its negative clause is class-level ("every admissible normalization" must
violate the TT identities or need an extra free input), so no single witness
fires it; a candidate fourth-moment adoption decides its own fate, not the
row's, and an adoption is not a derivation.

## 6. Attack order (owner-reviewed)

The order below replaces revision 1's phases; it is the owner's reviewed
sequence, with the mechanics filled in. POLICY sequencing (predefinition,
owner freeze, preregistration, verifier) applies to every formal step, and
every adoption or ratification named is an owner decision this note does not
make.

**1. A new public probe for `DE-W-CONSTANT` rule R1.** DESI DR2 (Results II,
arXiv:2503.14738, table 5) reports for the headline flat `wCDM` combination
DESI+CMB `w = -1.055 +/- 0.036`. Against the target `-14/15` the frozen
Gaussian witness is exact:

```text
|-1.055 + 14/15| / 0.036 = 365/108 > 322/125
```

with `322/125 = 2.576` the two-sided 99 percent point. If DESI+CMB satisfies
the already-frozen HEADLINE definition, R1 fires and `DE-W-CONSTANT [H]` goes
to `F`. Per the owner review this must be decided by a **new** public probe,
not an amendment of `P-DE-W-ARMING-1` (whose RESULT recorded R1 as PENDING
with no in-carrier posterior on the frozen record). Either outcome is a
registered decision: fired, or a labeled non-firing witness with the reason.

**2. `GENERATIONS-L3`.** The only READY row owning a registered gate in
`canon/GATES.tsv`, and the gate is binary with no STOP branch. Preregister
one FORMAL probe for the L2-to-L3 lift; a completed derivation decides the
row and the gate either way.

**3. Dispose the open specification lanes and divergent branches.**
[Issue #107](https://github.com/mathorn1973/twist-j/issues/107)
(`P-DMATTER-TOTAL-1` predefinition lane — the registered vehicle for the
`QUADRATIC-DECODER-DATA` closing package: the `K_QDD = K` identification, the
binding gate, the domain extension distinguishing dagger/transpose);
[issue #539](https://github.com/mathorn1973/twist-j/issues/539)
(`DEF-TYPED-APPARATUS-RECORD-CONTRACT` — the shared manifest template whose
profile adapters are the correct form for the separate typed contracts of
step 5); and the divergent branches named in
`notes/BRANCH-LEDGER-2026-08-24/DISPOSITIONS.tsv` — the three entropy
branches and the two `p-dmatter-total-1` branches
(`notes/p-dmatter-total-1-direct-readout`,
`notes/p-dmatter-total-1-owner-decision-input`) — so that no later freeze
collides with content that exists only on an unmerged ref.

**4. The finite METRO negative tests.** Obligation D's stream transport at
q=2, k=2 over the pinned 1024-tuple family (one exact failure closes
`METRO-REDUCTION-CALCULUS` negatively; success freezes the transport
pattern), and `Cert_joint` with its terminating checker versus direct
translated-box averages over the enumerated q=2, a=2, r=1 families
(`METRO-ADMISSIBILITY-DIM`).

**5. The separate typed contracts.** Instantiated from the issue #539
template, each with its own carrier, equality and output: the METRO
unbounded-memory protocol child (R3), the QDD apparatus-side unbounded-memory
disposal clause, the QDD apparatus profile itself, and the curvature package
(the frozen quadruple carrier/measure/projection-group/commutator-choice for
`CURVATURE-OPERATOR-CANONICAL`). Two unbounded-memory contracts, not one.
Alongside: the phase-gauge equality computation (each candidate whole-family
equality tested against the proved exact inequivalent phase families —
collapse is a contradiction, distinctness forces a phase-indexed class).

**6. Only then the expensive completeness theorems, and last the physical
adoptions.** The classification decisions of `CURVATURE-OPERATOR-CANONICAL`
(then `TRACEKERNEL` over every member), `METRO-EDGE-SCALE`'s selector
comparison, the `MINIMAL-READ` complete-class work, the entropy rigidity
question — and only at the end the adoptions that are one-shot freezes: the
TT fourth-moment law (an adoption, not a derivation), the C3 conventions, and
the C1 event-law candidates (audits against the forbidden-input lists first;
the honest failure mode of the apparatus lane remains permanent STOP,
"SAMPLING NOT PROVIDED rather than impossible").

## 7. Boundary

This note is `NON-CANONICAL`. It creates no claim, definition, candidate ID,
probe, preregistration, verifier, evidence row, gate, dependency, owner
decision or Canon change. The reduction map describes the ledger; it does not
bind it. Only the seven explicit live-to-live `DEPENDENCIES.tsv` edges are
dependencies; every other grouping here is pattern or species membership.
Every step of section 6 that touches the Canon requires its own POLICY
sequence. The two WEAK verdicts of section 2 and the corrections of section 0
are part of the record and cap what the map may be cited as proving.
