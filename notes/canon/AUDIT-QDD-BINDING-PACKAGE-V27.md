# AUDIT-QDD-BINDING-PACKAGE-V27

```text
STATUS:                  NON-CANONICAL ADVERSARIAL AUDIT
AUTHORITY:               NOT CANON
AUDITED DOCUMENT:        notes/canon/P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md
AUDITED OWNER DECISION:  BINDING-PACKAGE, 2026-07-30, claim issue 107
PUBLIC BASE:             Public Canon v27, tag canon-v27
PUBLIC CONTENT COMMIT:   116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256:    c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
PUBLIC CANON BYTES:      150959
DATE:                    2026-07-30
VERDICT:                 FOLD UNSAFE TODAY
QDD STATUS:              O / STOP, correctly, and unchanged by this audit
FORMAL RUN:              NONE
```

This note changes no claim, status, scope, gate, frontier, count, hash, tag,
release, or authority. It creates no identifier and authorizes no execution.
It records the result of an adversarial audit of the definitions the package
marks `FROZEN`, so that those defects are fixed in a note rather than after a
normative fold has made them normative.

Every witness asserted here is reproduced by the support file
`notes/canon/AUDIT-QDD-BINDING-PACKAGE-V27-CHECKER.py`, whose transcript is
pinned in section 8.

## 0. What this audit did

Seven independent auditors attacked seven angles of the package, each followed
by an adversarial judge instructed to refute its auditor, followed by one
consolidation. Separately the coordinating session re-derived the decisive
numbers first-hand. Section 9 records which findings are first-hand and which
are reported.

The audit was proof-first and result-exposed, as the package's own section 0
requires: the domain is 15625 points and fully enumerable in seconds, so
nothing here is a blind selection experiment.

## 1. Verdict

**The fold as scoped — freeze the types and the gate, then probe — is not safe
to write today.** It would freeze a type whose central map has no content, a
gate that cannot route negative and that no checker enforces, and a ledger
delta that the repository's own tooling rejects.

**`QUADRATIC-DECODER-DATA` is correctly left at `O / STOP`, but for the
opposite reason a reader of the defect list might infer.** No registered
falsifier fired. The row is not at `O` because it is failing. It is at `O`
because it has not begun to close: of the fourteen items the registered
falsifier requires to be public before a positive close, the exact write map is
not public and the complete dependency graph is neither complete nor
installable.

## 2. The registered falsifier: nothing fired

The registered falsifier of `QUADRATIC-DECODER-DATA` closes negatively on five
conditions. After the audit:

```text
1  the action is ill typed
   NOT FOUND mathematically. Found only as editorial type defects in the
   frozen text; see section 4. Every field of the displayed composite
   typechecks once a slot is chosen, and the slots are provably identical.

2  an included field is not constant on Q-fibres
   NOT FOUND, and structurally unfirable for the displayed map:
   0 of 313 fibres carry a non-constant record.

3  two states distinguished by the typed action have equal Q
   NOT FOUND, and impossible for the displayed map: the five-field record
   produces 313 distinct values on 313 carrier elements, so F_QDD is
   injective on QCarrier.

4  normalization fails
   NOT FOUND: 0 violations of w_low + w_high = m, 0 negative weights, and
   p_low + p_high = 1 on every nonzero class.

5  an unregistered input is required
   NOT FOUND for the computable half: the record is exactly independent of
   q and r, and depends on each of the four piston coordinates.
```

Two caveats travel with conditions 2 and 3. On the composite
`F_QDD o Q_QDD o beta_QDD` those tests are tautological, since that map
factors through `Q` by construction; the substantive version bites on
`D_QDD_direct`, which is not implementable from the frozen text and therefore
**could not be tested**. And any construction of even degree in `w` and
`sigma_4(w)` factors through `Q` automatically, which is why defect B5 below
matters.

The displayed decoder leg is total, exactly normalized, allowlist-compliant,
constant on `Q`-fibres, and injective on the carrier. That is a genuine
positive result of the package's own arithmetic and should be recorded as one.
It is not sufficient to close the row.

## 3. Blocking defects

### B1. The frozen B4 clause does not determine its own central object

Section 8 marks `B4 OUTPUT` `FROZEN`. B4's entire specification of
`D_QDD_direct` is one sentence: use field multiplication, `sigma_4`, and
`Tr_(Q(zeta_5)/Q)` to form the five fields. No formula is displayed for any
field. Unrecoverable from the text: the pairing itself, never written as
`<x,y> = (1/5) Tr(x sigma_4(y))`; the constant `1/5`; a definition of
`sigma_4`, a string that occurs exactly once in the package and is defined
nowhere; the two subspaces; the rank-one operator; the
`End_Q(Q(zeta_5)) -> M_4(Q)` convention; and the branch order.

Seven auditors implemented roughly fifteen inequivalent readings between them.
Exactly one reproduces the theorem target; the others miss on between 480 of
625 and 15600 of 15625 of the domain. A clause marked `FROZEN` whose central
map admits fifteen implementations is not a definition, and the theorem target
`D_QDD_direct = F_QDD o Q_QDD o beta_QDD` cannot be stated, let alone tested.

Sits in `B4 OUTPUT`.

### B2. B4's own words name the wrong subspace, and the gap is 12000 of 15625 states

Under the `B1` bridge `iota_0` in the frozen basis
`B0 = (1, zeta, zeta^2, zeta^3)`:

```text
im(E_low)  = span(1,1,1,1) = 1 + zeta + zeta^2 + zeta^3 = -zeta^4
Tr(-zeta^4) = 1, not 0, and -zeta^4 is not rational
im(E_high) = {v : sum v_i = 0}
ker Tr     = {v : 5 v_0 = sum v_i}
```

So `im(E_low)` is **not** the rational line `Q.1` and `im(E_high)` is **not**
the trace kernel. B4 nevertheless calls the split "rational-line and
trace-kernel branch weights".

Taking those words literally and projecting onto `Q.1` disagrees with B3's
frozen effects on **480 of 625 carriers = 12000 of 15625 checkpoints**.
Smallest witness, where the amplitude is literally the rational number 1:

```text
v = (1, 0, 0, 0)
  B3 frozen effects:   (w_low, w_high) = (1/20, 3/4)
  B4 literal words:    (w_low, w_high) = (4/5, 0)
  both sum to m = 4/5
```

The package's own upstream note names the object correctly.
`notes/canon/P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` section 3 defines
`lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4`, calls it **the low line**,
identifies `pi_low` and `pi_high` with exactly these projectors, gives the
closed forms `w_low = s^2/20` and `w_high = sum v_i^2 - s^2/4`, and explicitly
rejects the shifted window `(zeta, ..., zeta^4)` — the one basis in which
`E_low` *would* be the rational-line projector — as "a new selector decision,
not an inherited public fact". B4 therefore imports a description belonging to
a rejected frame.

Under the low-line reading the theorem target holds with zero mismatches, so
the mathematics is sound and the registered falsifier did **not** fire. What
fails is the frozen wording: a fold freezes words, and these words are false in
the basis `B1` freezes.

Sits in `B4 OUTPUT`, in contradiction with `B3 PHYSICAL READ`.

### B3. The frozen B5 ledger delta does not pass the repository's own checker

Applying the eight proposed rows verbatim to a scratch copy of v27 gives
`FAIL: DEPENDENCIES.tsv line 349 names unknown item`; after adding `NORMATIVE`
rows for the new `DEF-QDD-*` identifiers it fails again on the gate row.
The checkout confirms the preconditions: `canon/` contains **zero** occurrences
of `DEF-QDD`, `canon/GATES.tsv` holds 11 gates and **zero** QDD rows, and
`NORMATIVE.tsv` gives `QUADRATIC-DECODER-DATA` an empty `gate_ids` column.

The row `QUADRATIC-DECODER-DATA -> GATE-L1-L6-QDD-BORN-READOUT` is a category
error. Gates bind through the owner's `gate_ids` column, and **0 of 345**
existing dependency edges point at a `GATE-*`. Beyond that the delta omits
every mandatory field: `relation` and `basis` on all eight rows, the gate's
`decision_condition`, the owner's `gate_ids` edit, and the seven `NORMATIVE`
columns for all 23 declared `DEF-QDD-*` identifiers.

`B5 CLOSURE` is marked `FROZEN`. A frozen delta the tooling rejects cannot be
folded.

### B4. The gate the fold is meant to freeze is mechanically inert

`NORMATIVE.tsv` records the owner's layer as `MULTI`. The cross-layer rule in
`tools/check_ledger.py` fires only when both endpoint layers lie in `L1..L6`,
so it never fires for any QDD edge. The controlled pair was run: the full
wiring with the gate at layer `MULTI` passes, and the identical configuration
with no gate registered at all also passes, with byte-identical counts except
`gates=12` against `gates=11`.

The gate becomes load-bearing only if the owner's layer changes `MULTI -> L6`,
an edit the package never proposes. Freezing "the gate" as written freezes a
decoration.

Sits in `B5 CLOSURE`.

### B5. The gate's decision condition prescribes its own answer

Section 5 closes the gate positively "only when the complete typed direct write
factors through `Q_QDD`, every nonzero output gives the displayed normalized
two-outcome measure, the zero output remains explicitly tagged". That measure
is displayed in section 4. And "factors through `Q_QDD`" discriminates nothing:
every construction of even degree in `w` and `sigma_4(w)` factors through `Q`
automatically, and every candidate reading actually built was constant on all
313 `Q`-fibres.

This is exactly the construction that
`notes/canon/AMEND-TM-SYM2-PHYSICAL-MEASURE-SCOPE.md` exists to remove: a row
that states its answer before it states its question converts an obligation
into a target with a slot for a construction fitted to it. The corrected
TM-SYM2 language is the model — values "read off the bridge rather than imposed
on it". A gate that cannot route negative must not be frozen.

Sits in `B5 CLOSURE` and section 5.

### B6. The effect adoption collides with a standing prohibition the package never cites

`notes/canon/P-DMATTER-TOTAL-1-PHYSICAL-INSTRUMENT-PREDEFINITION.md` section 2
freezes the same two matrices as `CAND-EFFECT-GRAM-LOW` and
`CAND-EFFECT-GRAM-HIGH`, holds them `ALGEBRAIC_ONLY`, and states verbatim:

> Those two identifiers remain `ALGEBRAIC_ONLY`. They are explicitly forbidden
> from filling the public `quadratic_manifest.effect_ids` slot.

The package fills that slot with the same matrices under the fresh names
`DEF-QDD-EFFECT-LOW` and `DEF-QDD-EFFECT-HIGH`, and nowhere cites the
predefinition. Whether a rename lifts the prohibition is an owner ruling, not a
computation. Until that ruling exists in writing, a fold would install
identifiers around a live prohibition.

Sits in `B3 PHYSICAL READ`.

## 4. Fixable defects

Real, but each repairable in a line or two without reopening any science. None
changes a number.

```text
F1  NORMALIZED is not a constructor of its own codomain. B4 emits
    NORMALIZED(...) while section 5 defines
    TaggedMeasure_QDD = ZERO_DENOMINATOR | MEASURE(...). Each name occurs
    once and no line ties them.
F2  F_QDD's argument slot is unstated. QCarrier_QDD is a set of ordered
    pairs, but every displayed formula takes a single matrix A. Harmless only
    because the two slots are identical on all 313 elements.
F3  The Gram adjoint ^sharp is used in a frozen identity but has no
    identifier and no declared domain.
F4  The section-6 arrow convention is inverted between the DAG block and the
    delta block.
F5  The "complete" dependency graph omits six of the package's own declared
    identifiers, including all five write_target_ids and
    DEF-QDD-EQ-POINTED-ORBIT.
```

## 5. The 313 collision with an excluded leg

The package discloses `|QCarrier| = 313`, zero fibre 25, nonzero fibre 50. Those
numbers are exact and their origin is the `+-v` identification: `Q_QDD(v)`
collapses to `v v^T` because B2 freezes `v^dagger = v^T`, giving
`313 = 1 + (5^4 - 1)/2`, lifted 25-fold over `K_QDD` because `beta_QDD` ignores
`q` and `r`, so `25 + 312 * 50 = 15625`.

`CENSUS-313 [C]` has the **identical profile**: 313 attractors, 312 basins of
50 and one basin of 25, covering the same 15625 states. Its registered
arithmetic origin is different, `313 = 13^2 + 12^2`.

Running the registered kernel and comparing the two partitions of `F_5^6`
directly:

```text
census basins    313 blocks, {50: 312, 25: 1}
QDD Q-fibres     313 blocks, {50: 312, 25: 1}
blocks in common 0
the two size-25 blocks are disjoint, intersection 0
```

The QDD zero fibre is `{p1 = p4 = p1p = p4p = 0}`; the census singlet basin is
not. So the coincidence is numerical and there is **no** cross-leg identity —
which is the outcome the registered scope requires, since it explicitly
excludes the binary Thue-Morse and census legs.

That is the good news. The defect is that the package discloses `313` and the
`25/50` profile among the "facts visible before this package" and never
mentions `CENSUS-313`. This repository fences numerical coincidences
explicitly — `GYRON-DENSITY`'s falsifier ends with "another occurrence of the
number 1/6 on another carrier is outside scope". An unflagged collision of both
the count and the whole multiplicity structure is a hole in the disclosure that
a later preregistration must close, or a reader will take it for a binding.

## 6. The one refuted angle

The angle `dagger-collapse` was refuted by its judge and is carried here as
unsettled in its characterisation only.

Its auditor claimed the frozen theorem target **fails** on 12000 of 15625
states because of an accidental basis slip. The judge showed the diagnosis is
contradicted by `P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` section 3, which
the auditor had not read, and then built the direct write purely on the
cyclotomic side and got zero mismatches on every field with the low line.

The arithmetic is settled and uncontested: with the low line the branch split
matches on 625 of 625; with the literal rational line it misses on 480 of 625.
What is unsettled is only whether to report this as "the frozen target fails"
or as "a naming defect in a frozen clause, the target holding under the
intended reading". This note takes the second reading and carries the finding
as B2. **No claim is made anywhere in this note that a registered falsifier
fired on this angle.**

The other six angles were sustained by their judges.

## 7. Ordered actions before a fold is written

```text
1  Replace B4's direct-write sentence with displayed formulas. Define
   sigma_4 = (zeta -> zeta^4). Display <x,y> = (1/5) Tr(x sigma_4(y)) with
   the 1/5 written. Display the branch line as Q.(1 + zeta + zeta^2 + zeta^3)
   and call it the LOW LINE. Delete "rational-line and trace-kernel". Display
   the rank-one operator, the End_Q -> M_4(Q) convention, and the branch
   order. Re-run the target on all 15625 checkpoints and record the result.
2  Decide in writing which of two things B4 is. Either D_QDD_direct is
   independent, in which case the field manifest must stop naming
   DEF-QDD-QPAIR and the F-side formulas as the source and emit rule of four
   of the five fields; or it is a re-notation, in which case drop the
   theorem-target framing. The package currently claims both.
3  Rewrite the gate's decision condition so it can route negative, using the
   corrected TM-SYM2 language as the model.
4  Fix the layer field or drop the gate claim. Either MULTI -> L6, which makes
   the L1 -> L6 gate genuinely enforced, or stop describing the package as
   supplying a scope-valid binding gate. Note that an L1 -> L6 span would be
   the widest in the ledger; that should be argued, not assumed.
5  Rewrite the B5 delta, delete the dependency row pointing at a gate,
   register the gate in GATES.tsv with a non-empty decision_condition and in
   the owner's gate_ids, supply relation, basis and the NORMATIVE columns for
   every new identifier, then run tools/check_ledger.py and paste the PASS
   line into the package.
6  Settle statement_source. All 230 existing normative items point at
   canon/CANON.md. Pointing new items at a file stamped AUTHORITY: NOT CANON
   contradicts POLICY section 5; pointing them at CANON.md changes the Canon
   hash and forces a version. The header "CANON / TABLE CHANGE: NONE" survives
   neither.
7  Obtain and cite an explicit owner ruling on the effect prohibition.
8  Split SCOPE_EXCLUDED out of this fold. No tool enforces its admissibility
   condition, its carve-out for the fourteen QDD requirements is not
   representable in its four fields, and a contract change of that reach
   should not ride along with one leg's binding.
9  Extend the section 0 disclosure: the 312 nonzero fibres and the covering
   identity; that F_QDD is injective on QCarrier so two of the five negative
   routes are structurally unfirable for the displayed map; the 480/625
   ambiguity the package's own words permit; that G is exactly one fifth of
   the sigma_4-twisted trace Gram; that v^dagger = v^T collapses the ordered
   pair onto the diagonal on all 313 elements; and one sentence recording the
   313 collision of section 5 together with the fact that the partitions
   differ.
10 Only then a probe, scoped for reproducibility of an exact computation
   rather than discovery, and with a decision condition that is not checkable
   only by the computation that produced it.
```

## 8. Checker transcript

`notes/canon/AUDIT-QDD-BINDING-PACKAGE-V27-CHECKER.py`, run from the
repository root under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`,
Linux x86_64, Python 3.12.3, exit 0, empty stderr, about 3 s:

```text
AUDIT-QDD-BINDING-PACKAGE-V27 checker
frozen objects from P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md
arithmetic: int and Fraction only; no float in this file

M1 |V_eff| = 5^4 OK  625
M2 |QCarrier| = 1 + (5^4 - 1)/2 OK  313
M3 Q_QDD has both slots equal on every carrier element, since B2 freezes v^dagger = v^T OK  313 of 313 on the diagonal
M4 V_eff fibre histogram of v -> v v^T OK  {1: 1, 2: 312}, the +-v identification
M5 K_QDD fibre histogram, beta ignores q and r OK  {25: 1, 50: 312}, 25 + 312*50 = 15625
A1 G is invertible with the stated inverse OK
A2 sigma_4-twisted trace Gram equals 5 G exactly OK  Tr(z^i sigma_4(z^j)) = 4 on the diagonal, -1 off
A3 E_low and E_high are idempotent, ^sharp-self-adjoint, and sum to I OK  ranks 1 and 3
A4 m(A) >= 0 on V_eff and m(A) = 0 exactly at v = 0 OK
A5 w_low, w_high >= 0 on V_eff OK
A6 w_low + w_high = m on V_eff OK  NORM-QDD-BRANCH-SUM holds on all 625
A7 degenerate two-outcome reads are present and counted OK  w_low = 0 on 84 nonzero v; w_high = 0 on 4, the constant vectors
R1 every field is constant on every Q-fibre OK  0 of 313 fibres carry a non-constant record
R2 the five-field record separates QCarrier OK  313 distinct records for 313 carrier elements, so F_QDD is injective and no two states with equal Q can be distinguished
R3 the density field alone does NOT separate OK  273 of 313; A G / m erases the scale, so v and 2v collapse
R4 NORM-QDD-TWO-OUTCOME: p_low + p_high = 1 on every nonzero class OK
C1 Tr(x sigma_4(x)) = 5 m(A) on every nonzero class OK  the cyclotomic total weight and the matrix m are the same object
C2 the low line lambda_B = 1 + zeta + zeta^2 + zeta^3 spans im(E_low) OK  Tr(lambda_B) = 1, so lambda_B is NOT in the trace kernel and the line is NOT the rational line Q.1
C3 E_low reproduces the low-line closed form w_low = s^2/20 OK  matches P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md section 3
W1 B4's literal 'rational line' disagrees with B3's frozen effects OK  480 of 625 carriers = 12000 of 15625 checkpoints
W2 smallest witness and both branch pairs OK  v = (1,0,0,0): frozen (1/20, 3/4) vs literal (4/5, 0), both sum to 4/5
X1 the census reproduces its registered basin profile OK  313 attractors, basins 312 x 50 and 1 x 25
X2 the QDD Q-fibres have the identical profile OK  313 fibres, 312 x 50 and 1 x 25, same as the census
X3 the two partitions are nevertheless different OK  0 blocks in common, so the coincidence of 313 and of the {312x50, 1x25} profile is numerical, not a cross-leg identity
X4 even the two size-25 blocks are disjoint OK  QDD zero fibre is {p1=p4=p1p=p4p=0}; the census singlet basin is not
L1 canon/ contains no DEF-QDD identifier OK  0 hits
L2 canon/GATES.tsv has no QDD gate OK  11 gates registered, 0 of them QDD
L3 NORMATIVE.tsv gives the owner layer MULTI and no gate_ids OK  layer=MULTI gate_ids=<empty>
L4 no dependency edge in the ledger points at a gate OK  0 of 345 edges

SUMMARY 29/29 witnesses reproduce
```

The checker section `X` transcribes the kernel of `reproduce/census/verify.py`
in order to compare partitions; it does not modify or rerun that reproduction.

## 9. Provenance

Established **first-hand** by the coordinating session, with independently
written scripts, and reproduced by the pinned checker: the whole of section 8,
that is the finite manifest and its `+-v` origin, the Gram and effect algebra,
the record's constancy and injectivity, the twisted trace identity, the low
line and its closed form, the 480 of 625 gap with its smallest witness, the
census comparison, and the four ledger facts. The verbatim quotations from
`P-DMATTER-TOTAL-1-PHYSICAL-INSTRUMENT-PREDEFINITION.md` section 2 and
`P-DMATTER-TOTAL-1-CYCLOTOMIC-REALIZATION.md` section 3 were read directly from
the checkout.

**Reported by the multi-agent audit and not re-executed** by the coordinating
session: the `tools/check_ledger.py` failure at `DEPENDENCIES.tsv` line 349 and
the controlled gate pair `gates=12` against `gates=11`; the count of roughly
fifteen inequivalent readings of `D_QDD_direct`; the 272 alternative admissible
effect families; and the detailed section-4 against section-6 contradictions
listed as F1 to F5. Those should be re-run by whoever writes the fold.

No formal execution, no probe, no preregistration, and no public identifier is
created by this note.
