# PLAN: decoder sector after Public Canon v27

```text
DATE        2026-07-29
STATUS      NON-CANONICAL working plan. No authority. Creates no claim,
            moves no status, changes no scope. Scheduling and scoping only.
BASIS       Public Canon v27, mathorn1973/twist-j main, verified by clone
            today: STATE ACTIVE, tag canon-v27, CONTENT_COMMIT
            116b62edf505914d96fcd65318d97f3675c53f85, CANON_SHA256
            c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6,
            150959 bytes, canon/SHA256SUMS 5 of 5 OK, tag and content commit
            ancestors of main (head b0a53eb, merge of PR #209),
            tools/check_canon.py, check_ledger.py, check_policy.py all PASS.
            Registry snapshot: 214 claims, 28 live H/O.
INTERNAL    Not consulted this session (no credentials). Nothing below
            asserts internal-line state.
INPUT       The owner-endorsed decoder-sector audit of 2026-07-29
            (in-session). This plan adopts its method reading and corrects
            its state table where v27's merge overtook it.
```

## 0. Corrections to the input audit, against the repository

1. The audit's closing table reads `v27 Draft, main je v26`. Overtaken:
   v27 merged and is ACTIVE on main as of today. Everything below builds
   on v27 as sealed, which strengthens the audit's plan rather than
   weakening it: the breaker can now pin against a sealed basis instead
   of a moving draft.
2. `O-DECOHERENCE-CLAUSE` and `O-COIN-CANONICAL` never existed publicly
   and received no public retirement or history event (firewall in
   `notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md`, section 6, and
   CANON.md). The audit's point 1 ("today closed one of those items") is
   correct at mechanism level and as internal provenance; publicly the
   closure is carried by the new rows, not by a retirement.
3. Everything else in the audit checks out against the repository:
   the bound `||V_bar_N - V_inf|| <= 1/(Nr) <= sqrt5/(2N)` with P1, P2
   declared premises; `GATE-L5-L1-MINIMAL-READ` registered (GATES.tsv,
   OPEN_SELECTION); multiplicities 2 versus 6 generic, 1 versus 5 on
   rungs; constants sqrt5/2 versus sqrt5; squared gaps 16/5 versus 4/5;
   the counter-selector MAXIMAL-REACH named and not adopted.

## 1. What v27 settled. Do not re-litigate.

```text
DRIFT-IS-THE-READ        [T, L5]  reflection D, division-free spectral
                                  skeleton, nonclosing gap, exact drift and
                                  coherent range, all-N uniform bound;
                                  read interpretation conditional on P1, P2
COIN-SELECTION-CONDITIONAL [T]    admissible pair {beta_1, beta_3} exactly;
                                  S1, S2 select beta_1; S3 selects beta_3;
                                  no selector adopted by the theorem
COIN-MINIMAL-READ        [H, L1]  Canon adopts beta_1 by MINIMAL-READ;
                                  MAXIMAL-REACH named, unadopted
MINIMAL-READ-DERIVATION  [O]      owns GATE-L5-L1-MINIMAL-READ
                                  (OPEN_SELECTION)
Evidence                          probes/P-BOOST-COHERENCE-1, issue #206,
                                  8 groups, 477 checks, aarch64 and GitHub
                                  x86_64 byte-identical, bundle sha256
                                  0e2c9daa...
```

Consumed project docs, recorded here so no session re-runs them:
`PROMO-C-BOOST-COHERENCE-1`, `PROMO-C-BOOST-COHERENCE-2`, and
`DECISION-PROPOSAL-COIN-SELECTOR-NAMING_2026-07-29` are consumed by the
v27 fold (names and the H plus O split adopted essentially verbatim).
They stay in the project as provenance. Do not edit them; they belong to
their sessions.

The method template today validated, adopted as this plan's method: do
not ask the decoder to produce content; check first whether the algebra
already does it. The mechanism question "why does the read see the drift
and not the tick" was answered by Cesaro-averaging the unitary itself,
with an explicit uniform bound, no decoherence model, no new decoder
axiom. The decoder only had to not stand in the way.

## 2. The sector map after v27

The derivation route to `MINIMAL-READ-DERIVATION [O]` is conditional on
six preconditions (`notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md`,
section 5):

```text
1  OBSERVER-WRITE-PORT [H] closes positively for a completed typed decoder
2  the complete admissible protocol class is public
3  a typed map identifies cover sheets with terminal output reads
4  the accumulator and its equality or reconciliation rule are public
5  an exact theorem relates absence of feedback to a bound on admissible
   read redundancy
6  the L5-to-L1 action-layer boundary has its own named gate
```

State of each: 6 is DONE (the gate exists). 2, 3, 4 are definition work,
part owner, part session. 1 is the long pole: OBSERVER-WRITE-PORT is the
terminal sink of the only dependency subtree in the live set, behind
METRO-REDUCTION-CALCULUS, METRO-ADMISSIBILITY, METRO-ADMISSIBILITY-DIM
and QUADRATIC-DECODER-DATA (see CLOSING-SLATE_2026-07-27). 5 is the
single mathematically unknown item, and it is cheap to attack.

That asymmetry is the plan: attack 5 first. If 5 dies, the definition
debts 2 to 4 lose their purpose for this route and nobody pays them by
inertia. If 5 survives with a theorem, the debts become worth paying and
the route has a spine. Either outcome reprices the whole sector for the
cost of one session.

The decision text of the O row is outcome-complete and quoted here so no
session inflates a partial result: positive closure needs the complete
typed derivation forcing w = 1 and beta_1; negative closure needs the
complete admissible class proved nonempty and either both compliant
realizations or beta_3 forced; failure of one favored route, including
the no-feedback route, is STOP unless it classifies the complete class.
A breaker outcome therefore NEVER closes the row by itself. It informs
the route and it can kill the route. That is worth a session; it is not
worth a status.

## 3. Workstream A, first move: C-READ-REDUNDANCY-1

```text
CANDIDATE   C-READ-REDUNDANCY-1 (id free in project and public line as of
            today: no issue, branch, probe directory or registry row
            touches the redundancy question; 13 open issues checked)
TARGET      informs MINIMAL-READ-DERIVATION [O] on the public line;
            promotion, if any, via PROMO and the public probe protocol
QUESTION    precondition 5: does absence of feedback alone bound
            admissible read redundancy?
ORDER       breaker first. Construct before deriving.
```

The breaker, as in the audit's point 6: construct a one-way funnel with
no feedback that consistently carries the sixfold cover. Explicitly: a
finite acyclic graph, single terminal accumulator, exact integer maps,
no output-to-state edge; inputs are 2w = 6 sheets carrying the same
velocity datum under six distinct band descriptions; required output is
one total, well-defined terminal read of that velocity.

The definitional boundary, named now because it decides what the result
means. The public row lists "cover-to-output map" and "accumulator or
equality rule" as UNDEFINED. So "no reconciliation channel" has no
sealed formalization yet, and a breaker against a straw class proves
nothing. The candidate must therefore:

```text
a  cite every clause of its funnel class to a public row where possible
   (CORE.md decoder typing: outputs never feed the state update;
   DEF-DECODER-COMPLETION-CONTRACT manifest shape; the O row's own text);
b  declare every clause it cannot cite as an auxiliary hypothesis, listed
   in prereg field 4, systematics;
c  compute at BOTH poles of the undefined clause: the permissive class
   (projection onto one sheet allowed) and the restrictive class (output
   total, invariant under sheet permutation, equality tests forbidden);
d  locate the flipping clause: the weakest restriction under which the
   sixfold carry becomes impossible.
```

The deliverable is (d), whichever way the bit falls. The permissive pole
almost certainly admits a trivial carry; that alone already proves that
no-feedback ALONE bounds nothing and that the route needs a named extra
clause. The restrictive pole is the real question. The boundary between
them is the missing definition that preconditions 3 and 4 must freeze,
extracted constructively instead of guessed.

Outcome map, fixed before compute, mapped to the ADOPT note's own
sentences:

```text
W6   a compliant funnel carries 2w = 6            the budget cannot select
     in the restrictive class                     2 over 6; the route as
                                                  sketched is dead
WALL the construction generalizes to every        route dead entirely
     finite 2w                                    ("tolerates arbitrary
                                                  finite read multiplicity
                                                  kills this route only")
OBS  exhaustive search to the declared size       candidate obstruction
     bound finds no carry, and a structural       theorem = precondition 5;
     obstruction is extracted and proved          candidate-T if proved for
                                                  all sizes, candidate-C at
                                                  finite range
NULL no carry found, no obstruction extracted     candidate-C, declared
                                                  range, route undecided
```

In every branch `MINIMAL-READ-DERIVATION` stays O and `COIN-MINIMAL-READ`
stays H, per their own decision texts. In W6 and WALL the H row survives
as an adopted premise and MAXIMAL-REACH gains nothing: killing a
derivation of MINIMAL-READ does not derive MAXIMAL-REACH.

Discipline: six-field prereg (draft in the appendix), frozen with SHA-256
by the claiming session before any compute; exact arithmetic, stdlib
only; layer L5 read structure over an L1 coin carrier, no lift performed,
`GATE-L5-L1-MINIMAL-READ` untouched. One session, one candidate.
Estimated cost one session. Falsification and confirmation cost the same
here, which is the best ratio of information to work in the sector.

## 4. Workstream B, second: C-READ-COVARIANCE-1, the P1 debt

P1, translation covariance of the read, is the premise the audit's point
5 correctly localizes as new visible debt inside DRIFT-IS-THE-READ [T].
Same shape, breaker first:

```text
B1  construct a read satisfying every sealed clause of the same funnel
    class that VIOLATES translation covariance and still returns a
    well-defined long-window limit different from the drift.
    Exists: P1 is a genuine independent axis. It stays a premise, the
    theorem keeps its conditional form, and the program stops trying to
    derive it. That is a clean, honest terminal state.
B2  if every attempt collapses for one identifiable reason, that reason
    is the covariance-derivation candidate, and P1 may lift from premise
    to conclusion in a later public probe.
```

Not in scope: anchoring P1 or P2 to MEASURE-BORN-VERB or any other row.
The ADOPT note names that as separate work; smuggling it in here would be
an unnamed layer lift.

Ordering: after A returns, same or next session window. A's funnel-class
formalization is the reusable infrastructure for B; writing B first would
build it twice.

## 5. Workstream C, gated: the blindness test of the budget

Runs ONLY if A ends in OBS (an obstruction theorem exists). This is the
audit's point 7, adopted as discipline: an argument that derives
everything derives nothing.

```text
CANDIDATE   C-BUDGET-BLIND-D-1 (open only after A closes OBS)
TEST        apply the obstruction machinery to a target whose answer it
            was never fed: the count of geometry axes. d = 3 must appear
            nowhere in the prereg, the code, or any bound.
READINGS    machinery outputs 3        large; own lane, own named gate next
            machinery outputs nothing  the budget stays a coin argument;
                                       say so without inflation
            machinery needs d as input circle; candidate-F for the
                                       generalization, first-class,
                                       archived; the coin result stands
```

Separate session, separate candidate, independent code path. The person
or session that proved the obstruction must not write the blind test.

## 6. Workstream D, parallel and public: fold the occupancy lane

`PROMO-C-BOOST-OCCUPANCY-1` (project, 2026-07-29) is packaged, additive,
and collision-free as of today: no open issue, no branch, no registry row
touches occupancy. It is the one lane from today's sector work with no
public movement.

```text
ACTION      standard public probe protocol: claim issue, branch
            probe/P-BOOST-OCCUPANCY-1, freeze PREREG from the candidate
            prereg with public wording, two-architecture run, fold
            BOOST-OCCUPANCY-FLOOR [T, L5] plus BOOST-OBSERVED-VELOCITY
            [O, L6 fork a/b/c] additively at the next integer fold
WHY NOW     it completes today's mechanism result from the other side:
            DRIFT-IS-THE-READ proves the coherent read returns the drift;
            the occupancy floor prices the incoherent repair out
            (E[x^2] >= beta_1 m). Mechanism proved, repair floored.
COST        one session, verifier already exists at one-platform grade
```

## 7. Hygiene, mostly owner decisions, unchanged by today

```text
METRO-REDUCTION-CALCULUS   obligations B, D, E remain (ARROWS folded [C]
                           in v26). Still the only leverage-positive row
                           and ALSO route precondition 1 infrastructure
                           (the subtree under OBSERVER-WRITE-PORT). Keep
                           one session on it, per the CLOSING-SLATE.
Five stalled lanes         contract open decision 3; dispositions per
                           CLOSING-SLATE tier 4 (retire, F, or rebase).
                           Note C-C8-BILINEAR-SHADOW folded in v26 and is
                           off that list.
TM-SYM2-PHYSICAL-MEASURE   the one owner-STOP; approve a successor L5
                           source or retire. v27 left it unchanged.
Czech exposition           CO_TWIST_DOOPRAVDY_JE_SYNTEZA2 still asserts
                           Tr(C^2) = -21/8 against the registry's F;
                           live value -881/8. Needs its correction pass.
Newer unfolded PROMOs      IMPEDANCE-TOLL, CASIMIR-COEFFICIENT,
                           ARCH-UNIVERSALITY, RG-NO-FLOW, LARMOR-TREE-GATE,
                           TM-SYM2-TWOFOLD-NOGO, FRONTIER-WELLPOSEDNESS,
                           PENTAGON-ONLY-DILATIONS. Outside this sector
                           plan; rank them by the slate's method, do not
                           let them accrete silently.
```

## 8. Sequencing

```text
NOW        A  C-READ-REDUNDANCY-1      one session, breaker first
PARALLEL   D  occupancy public fold    one session, public protocol
PARALLEL   METRO B, D, E               one session, public protocol
NEXT       B  C-READ-COVARIANCE-1     after A returns, reuses A's class
GATED      C  C-BUDGET-BLIND-D-1      only after A ends OBS; independent
                                       session and code path
```

Rules that bind every slot: one candidate or probe per named session;
prereg frozen with SHA-256 before first compute; exact arithmetic, no
float in any assertion; thresholds never move; a fired falsifier is
archived, never deleted; no lift without its own named gate; promotion
only through PROMO and the public protocol; sealed folds are integer
versioned.

## 9. What this plan does not do

No canon edit. No status move. No adoption of MAXIMAL-REACH. No P1 or P2
anchoring. No claim about d = 3 or universal c (C is a test of an
argument, not a claim about d). No direct work on OBSERVER-WRITE-PORT,
which stays blocked by four rows and is reached through METRO, not
poked.

## Falsifier for this plan

This plan is wrong, and must be corrected before use, if any quoted pin,
row text, gate, multiplicity, constant, or decision condition differs
from mathorn1973/twist-j main at tag canon-v27; if a public issue,
branch, probe directory, or registry row claiming the redundancy
question or the occupancy fold existed at the basis time (collision
missed); if the six route preconditions differ from
notes/canon/ADOPT-COIN-MINIMAL-READ-2026-07-29.md section 5; or if
PROMO-C-BOOST-OCCUPANCY-1 differs from what section 6 asserts of it.

## Appendix: prereg draft for C-READ-REDUNDANCY-1

UNFROZEN DRAFT. The claiming session freezes it, records the SHA-256,
and only then computes. No data opened, no assertion executed before the
freeze. Six fields per the incubation contract:

```text
1  EQUATION / STATEMENT
   Funnel class F(2w): finite DAG G with input sheets s_1..s_2w, exact
   maps in the declared coefficient ring at every node, single terminal
   accumulator t, no edge from any output back to the L1 update
   (CORE.md: decoder outputs never feed the state update), acyclicity of
   G. Cover datum: one velocity value presented under 2w distinct band
   descriptions (the 2w open-band sheets of the w-cover away from a
   rung, per COIN-SELECTION-CONDITIONAL). Claim under test, quoted from
   the route: "whether a multiplicity-2w cover delivers redundant
   terminal reads that the architecture cannot reconcile and whether the
   smallest integer-admissible value, w = 1, is forced."
   Two poles, both computed:
     PERMISSIVE: t may depend on any subset of sheets.
     RESTRICTIVE: t total on the domain, invariant under every
     permutation of the 2w sheets, no equality or comparison test on
     sheet values (the candidate's formalization of "no reconciliation
     channel"; auxiliary, see field 4).
   Test instance w = 3 (the beta_3 cover, 6 sheets); generalization to
   all finite w attempted only if a w = 3 witness exists.
2  CODE
   Python 3 stdlib only. Fraction and exact Q(sqrt5) pairs; no float in
   any assertion. Enumerate F(6) up to the declared size bound; breaker
   searches for a witness funnel; verifier re-checks any witness clause
   by clause by an independent code path. Runtime under 120 s. Neutral
   environment fields, LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
   PYTHONHASHSEED=0 TZ=UTC.
3  CARRIER / DATA
   The enumerated funnel family is the data; no external data. Size
   bound (node count, fan-in, map degree) fixed at freeze, stated in the
   frozen text, never moved after.
4  SYSTEMATICS
   Clauses citable to public rows: no-feedback (CORE.md), acyclicity,
   terminal accumulator, coefficient ring. Auxiliary clauses (not
   citable, declared candidate hypotheses): the RESTRICTIVE pole's
   permutation invariance and the ban on equality tests. Known risks:
   family too narrow (a NULL at bound n proves only candidate-C at
   range n); straw-class risk mitigated by computing both poles and
   reporting the flipping clause, not one bit.
5  FAILURE THRESHOLD / OUTCOME MAP
   W6, WALL, OBS, NULL exactly as in section 3 of the plan, with their
   labels; every outcome archived; a fired falsifier is first-class; no
   threshold moves after the freeze.
6  ACTION LAYER
   L5 read structure over the L1 coin carrier. No lift performed.
   GATE-L5-L1-MINIMAL-READ is owned by MINIMAL-READ-DERIVATION [O] and
   is not touched by this candidate.
```
