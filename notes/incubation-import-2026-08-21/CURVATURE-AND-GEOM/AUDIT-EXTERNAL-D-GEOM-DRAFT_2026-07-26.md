# Audit of an external prereg draft: C-D-GEOM-UNIQUENESS-1

```
SESSION:   audit-external-d-geom-draft-2026-07-26
STATUS:    AUDIT ONLY. No candidate opened, no prereg, no freeze, no decision
           computation. No authority.
SUBJECT:   an externally authored draft prereg "PREREG C-D-GEOM-UNIQUENESS-1"
           brought into the project for brainstorming, 2026-07-26.
CURRENCY:  public main 91854391 (merge PR #154, fold/canon-v22-replay,
           2026-07-25). STATUS.md STATE ACTIVE, CANON Public Canon v22,
           CONTENT_COMMIT dd455edf, CANON_SHA256 67b12868, CANON_BYTES 113066.
           canon/SHA256SUMS 5 of 5 OK.
VERDICT:   DO NOT FREEZE. Two gates are unrunnable against v22, one gate is
           near-vacuous, the uniqueness clause is undecidable as written, and
           the obligation the draft targets already exists as a better-posed
           public row. Retarget, do not patch.
```

## 1. What the draft gets right

The basis pin in its section 0 is exact and current: v22, content commit
dd455edf, canon SHA-256 67b12868, 113066 bytes all match public main today,
and the five canon sums verify. The target is also the right one: the
geometric leg of the decoder is the decoder row that has never moved
(CHANGELOG carries "CURVATURE-OPERATOR-CANONICAL remains [O]" at three
separate folds). Three components are worth keeping and are named in
section 6 below.

## 2. Kill 1. The draft's gate N1 asks a verifier to reproduce a falsified number

Draft section 2 states "(Tr(C^2) = -21/8 stands at the public label; any use
of the numerical value is declared and controlled)", and gate N1 requires the
induced operators to reproduce "the registered commutator spectrum (and the
controlled Tr(C^2) label if used)".

The public label of -21/8 is F.

```
CURVATURE-TRACE-VALUE          F   the registered proposal
    Tr_V(K_hist^2) = -21/8 for the frozen historical operator is false;
    the exact value is -881/8                                [REGISTRY.tsv:140]
CURVATURE-HISTORICAL-TRACE     T   dim V = 818, Tr_V(K_hist^2) = -881/8
    exactly; no spectrum, canonical selection, or continuum  [REGISTRY.tsv:139]
```

Three numbers appear in the draft's neighbourhood and no two of them agree.
Exact re-derivation in Q(sqrt5), integer pairs, no floats:

```
printed historical spectrum {+- i phi^n : n = -2..2}
    Tr(K^2) = -2(1 + L_2 + L_4) = -2(1 + 3 + 7) = -22          exact
asserted in the draft                                  -21/8
public registered value for K_hist                     -881/8  [T]
-22 = -21/8 ? false        -22 = -881/8 ? false
```

Independent denominator argument, sufficient on its own: the draft's own
spectrum line writes the nonzero eigenvalues as +- i phi^n / d with d = 3, so
Tr(C^2) = -(2/9) sum phi^(2n) with sum phi^(2n) in Z[phi]; the denominator
divides 9 and can never be 8. The spectrum line and the -21/8 line inside the
draft contradict each other before either meets the public canon.

Consequence: N1 as frozen fires against the candidate by construction. A
verifier written to it would either fail or, worse, be quietly repaired after
the fact, which moves a threshold.

## 3. Kill 2. There is no registered public spectrum for N1 to reproduce

```
CANON.md, section 2:  "None of these facts selects a canonical spatial-curvature
operator. CURVATURE-OPERATOR-CANONICAL [O] asks whether the public architecture
determines exactly one equivalence class after the carrier, measure, projection
group, and ambient versus intrinsic commutator choice are fixed publicly. No
golden spectrum or continuum-curvature reading is asserted."
```

N1 has no public referent. The spectrum {0^27, +- i phi^n / d} is development
line material; importing it into a public-target prereg breaks the draft's own
section 0 derivation rule ("the development line is not cited, quoted, named or
leaned on as authority") in the same document that states it.

## 4. Kill 3. The obligation already exists, better posed, and is blocked on
owner rulings, not on a new candidate

```
CURVATURE-OPERATOR-CANONICAL  [O]  FRONTIER.md, program DECODER_CORE
    Queue: ROOT; STOP; FORMAL.
    Decision: UNIQUE if exactly one class survives, NONUNIQUE if at least two,
    EMPTY if none, STOP if the classification is incomplete or inexact.
```

The public row fixes the choice axes first (carrier, measure, projection group,
ambient versus intrinsic commutator) and then counts equivalence classes. That
is a finite exact classification. The draft instead quantifies over an
unspecified class of typed maps and asserts in section 3 that "every clause is
decidable in exact arithmetic or by finite enumeration". That is false for
clause (B) and for the first line of its falsifier ("no map satisfying (A)
exists"): non-existence and uniqueness over an unbounded function class are not
finitely enumerable. The public row is the same question made decidable.

The project has already been here. `claude/C-CURVATURE-OPERATOR-CANONICAL_RECON_2026-07-18.md`
established the fork (NARROW: admissible choices are the fully typed registered
options only, today exactly one tuple, so UNIQUE by enumeration but arguably
vacuous; GENERATIVE: everything constructible from registered public objects, a
real selection theorem, any of the four outcomes reachable) and named the three
owner rulings a freeze needs (R1 choice space, R2 the frozen equivalence
relation, R3 whether STOP closes). Those rulings are still outstanding at v22.
Re-checked today: no second typed carrier, no reduced-operator row, no second
measure or projection group typed for this construction exists in v22, so the
fork is unchanged since v8.

`claude/NADHLED-DEKODER-A-METROLOGIE_2026-07-25.md` adds the reason the row
resists: K_hist has Tr_V(K^2) = -881/8 < 0, the modulus channel is hyperbolic
and admits no torsion condition, so a canonical class does not exist without a
declared normalization and the row does not declare one. That reframes STOP
from "not tried hard enough" to a scope defect in the row itself.

## 5. Kill 4. The draft's status frame is not available on the public line

```
draft, section 1:  "D_clock and D_matter stand at T-LOCK (rho_gyron = 1/6).
                    D_geom remains T-LOCK candidate."
```

Public policy carries no T-LOCK, and REGISTRY.tsv contains zero occurrences of
it. Worse, the two objects the draft treats as closed are publicly open or
absent:

```
QUADRATIC-DECODER-DATA  [O]  the typed D_matter action ... Queue ROOT; STOP
                             Decision: STOP until the coefficient ring, carrier,
                             common total domain, Gram, dagger, MatterData
                             schema, write map ... are published
D_clock                      no registry row exists
READING-SPLIT           [D]  "no totality, uniqueness, or completeness of the
                             decoder is claimed"
```

So the draft's gate N7 (COMPOSITION: D_geom accepts the typed output of
D_matter and feeds a typed input acceptable to D_clock) has an undefined input
type and an undefined output type on the target line. The candidate is blocked
by an open row it assumes closed. This is the dependency error that removes the
whole section 1 framing, not a wording problem.

Same class of error, smaller: "the sealed Queen formula" for alpha is publicly
ALPHA-FORM [D], "the committed Queen form"; "sealed DeWitt form (v176 /
XXXVIII)" is publicly DEWITT-TWELVES [T] plus CONFORMAL-PREFACTOR [D]
(K_chi5 = 1/(864 pi), c_hom = 1/(72 pi)). Internal build and part numbers are
machine-forbidden in public normative text. The public rows exist and are
usable; the draft reaches past them for weaker provenance.

## 6. Kill 5. Gate N3 is near-vacuous, verified exactly

GRAVITY-BRIDGE-LAW [D] carries four displayed relations. The draft's N3 asks
that "the four gravity-bridge identities hold identically". Exact audit,
Q(sqrt5) integer pairs plus symbolic exponent triples, no floats:

```
alpha B g = 1                with B := alpha^-1 / g   TAUTOLOGY. The registry
    states the definition in the same clause. Zero content; alpha is never used.
g = 2^5 phi^2 sqrt(3 - phi)  a definition of g. The checkable residue is
    g^2 = 1024 phi^4 (3 - phi) = 5120 + 2048 sqrt5 exactly, and
    3 - phi = |1 - zeta_5|^2 = (5 - sqrt5)/2 exactly. Both verified. Both are
    already GRAVITY-BRIDGE-LAW, not something a D_geom candidate earns.
G_T = (32/33)^2 alpha^20 / g   and   l_P / lambda_e = (32/33) alpha^10 / sqrt(g)
    (l_P / lambda_e)^2 = (1024/1089, alpha^20, g^-1) = G_T identically.
    One identity written twice.
```

Independent content of N3: one exact Q(sqrt5) identity and one squaring. A
candidate passing N3 has demonstrated nothing about the geometric leg while
producing four green lines of output. That is worse than a missing gate,
because it manufactures the appearance of confirmation.

Related: N4 (NO-EXTRA-PARAM) cannot prove absence of a free parameter by
injecting one and observing rejection; that tests detection of the injected
shape only. The public precedent for doing this correctly is a routed outcome,
not a gate: the DE-TRACE-DENSITY underdetermination result witnessed
circularity by an adversarial scan of 307 rationals against the registered
relation set, and P-QS-COUPLING carries FREE-PARAMETER as a first-class leaf of
its decision tree. Route it, do not gate it.

## 7. The unfirable escape hatch

```
draft, clause (B):  "... or differ by a term invisible at the sealed 2-jet /
                     homogeneous L2 scope (boundary term or O(h^3))."
```

Any counterexample to uniqueness can be declared invisible at the declared
scope, so the falsifier cannot fire. A preregistration whose falsifier admits
a post hoc invisibility clause is not preregistered. The recon's R2 already
names the repair: freeze the equivalence relation before the run (proposal:
similarity over Q up to a nonzero rational scalar) and publish a robustness
table across strict equality, similarity, similarity up to scale, and
isospectrality, so the verdict is either relation-robust or shown not to be.

NOTE added 2026-07-26 after the R2 work: that repair is itself now corrected.
The four relations do not form a ladder, and "similarity up to scale" is the
one choice that must NOT be primary. See
claude/R2-SPEC-CURVATURE-OPERATOR-EQUIVALENCE_2026-07-26.md.

## 8. What survives from the draft

```
N5 REDUCTION-INVAR   the right instinct, wrong home. It is the recon's R2:
                     the verdict must be invariant under a frozen equivalence
                     relation, with the robustness table published.
N6 METRO-COMPAT      keep. The period-1 average bridge to
                     C-METRO-DIM-CRITERION is real and computable.
clause (D) acyclicity  keep the write-channel content, drop the free-will and
                     consciousness language. OBSERVER-WRITE-PORT [H] is about
                     output schemas and write channels, nothing else.
```

## 9. Answer to the draft's closing question

The draft asks whether to edit a gate, rename the candidate, tighten the
uniqueness clause, or write a verifier skeleton. None of the four. Every one of
them sits downstream of the blocker: the target row exists, is better posed,
and is stalled on three owner rulings plus, since 2026-07-25, a fourth question
about whether the row must declare its own normalization before it can close as
anything but STOP.

The honest next artifact is one of two, and it is the owner's ruling which:

```
A  the NARROW classification. Freeze the single registered tuple
   (V, counting, <b,d>-Reynolds with P_0, commutator (a,c)), enumerate,
   certify completeness, close UNIQUE by absence of registered alternatives.
   Cheap, honest, and explicitly labelled as certifying absence of
   alternatives rather than proving selection.
B  the GENERATIVE classification. Freeze the named list per axis verbatim
   (projection group from <b,d>, the return group H_1 of COLOR-RETURN-D5,
   the full verb; measure from counting, the Galois Gram, the Born weight;
   commutator from the registered letter pairs), enumerate exactly, count
   classes under the frozen R2 relation. A real selection theorem; any of
   the four outcomes reachable; cost dominated by exact rational linear
   algebra at dim 818 per tuple.
C  the scope repair first. Propose amending CURVATURE-OPERATOR-CANONICAL to
   declare its normalization, on the argument that the modulus channel is
   hyperbolic (Tr_V(K^2) < 0) and no canonical class exists without an
   anchor; otherwise record that the row as written can only close STOP.
```

OWNER RULING, 2026-07-26: none of A, B, C yet. R1 stays open; R2 is specified
first. See claude/R2-SPEC-CURVATURE-OPERATOR-EQUIVALENCE_2026-07-26.md.

## 10. Non-claims

Nothing here computes or predicts the outcome of the row. No candidate is
opened, no id is claimed, no threshold is set. The exact arithmetic in sections
2 and 6 is audit arithmetic against published public rows; it is not a probe,
carries no status label of its own, and would need its own preregistration and
two-platform pin to become one.
