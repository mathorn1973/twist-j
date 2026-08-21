# PREREG C-K4-FIBER-EQUATION-SOLVER-1

```text
CANDIDATE:    C-K4-FIBER-EQUATION-SOLVER-1
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
NAME:         deliberately NOT called FIBER-RELATION. This candidate is a
              fiber-equation solver with a BOUNDED pattern classification.
              The global fiber relation of F_109 is not characterized here
              and no wording of this document may suggest otherwise.
PUBLIC BASIS: Public Canon v44, main = tag canon-v44 =
              1417b533944e85106901079cc73ae7a0c3c42dc2, STATE ACTIVE
PARENTS:      the three frozen k4 candidates; the last of them,
              C-K4-PARENT109-FLOW-FACTOR-1, is SEALED and dead: both legs
              complete, stdout 469322f7..., T-A unfired at its scope,
              F_14 fired
RECON IN:     RECON-FIBER-EQUATIONS-K4, disclosed; the equations of G1 and
              the two vacuous obstructions come from there
LAYER:        L1 only. One session per candidate; this document claims it.
```

## The correction the owner's G2b needs, stated before the freeze

The owner proposed adding the profile conditions to the solver so that
OPPOSITE could become INFEASIBLE quickly even while FIBER stays
UNDECIDED. That cannot be done as stated, and the reason is structural,
not a matter of effort: the fiber conditions are linear in the table for
a fixed pattern, but the profile condition is SPECTRAL, the inertia of a
16 by 16 integer matrix that depends linearly on the table. It is not a
linear constraint and cannot be added to the linear system. Worse, the
obvious cheap proxy is empty: both frozen profiles have an odd negative
count, 7 and 9, so the determinant sign is negative in both and does not
separate them.

What is available instead, and what is frozen here: OPPOSITE is decided
by ENUMERATING fiber solutions and testing each one's two endpoints
directly. That makes OPPOSITE-FEASIBLE cheap when it happens, since one
witness suffices, but makes OPPOSITE-INFEASIBLE expensive, since it needs
the solution set of that pattern exhausted. The decision logic below is
written for that asymmetry rather than around it.

## Field 1. EQUATION (gates in the owner's order)

```
G1  FIBER-EQUATIONS. For a fixed flip pattern m, F_109(v) = F_109(v - 2m)
    if and only if
        sum_{j in O} m_j = 0                       for each of 10 orbits
        B(L_a(v), L_b(m)) + B(L_a(m), L_b(v))
            = 2 B(L_a(m), L_b(m))                  each sector, a <= b
    The derivation is the bilinear expansion of B(L_a(v - 2m),
    L_b(v - 2m)) and is a written proof, printed in full by the verifier.
    Gate: the predicate computed from these equations agrees with direct
    F_109 comparison on the frozen audit set of Field 3, every instance.
    The audit is [C] at finite scope and is NOT the source of the
    universal quantifier, which the proof carries.
G2  PATTERN-COVER, SCOPE-RESTRICTED AND SAID SO. The pattern class of
    this candidate is exactly the 252 weight-2 patterns: one plus cell
    and one minus cell inside one orbit, enumerated completely, with no
    quotient and no sampling. Completeness of the cover is NOT proven:
    there is no theorem here bounding the weight of a fiber difference
    mask, so a fiber pair of higher weight is not excluded by anything in
    this candidate. Consequence, frozen: even a fully decided sweep with
    zero UNDECIDED proves a statement about the weight-2 pattern class
    ONLY, and proves nothing about T-A over S_pm.
G3  EXACT-01-SOLVER, tri-state, twice. Substituting v = 1 - 2z turns each
    fiber equation into sum_j A_ij z_j = c_i over z in {0,1}^65 with z
    pinned on the pattern; every c_i is an integer, which the verifier
    asserts rather than assumes. For each pattern, two problems:
        FIBER      is there any z at all
        OPPOSITE   is there a z whose two endpoints both lie in S_pm with
                   opposite flow, decided by enumerating fiber solutions
                   and computing both profiles exactly
    Each problem returns exactly one of
        FEASIBLE     explicit witness, plus a direct recheck of F_109
                     equality and of both endpoint inertias by two exact
                     paths
        INFEASIBLE   the deterministic search tree exhausted within the
                     node budget
        UNDECIDED    exactly B nodes visited, no witness, tree not
                     exhausted
    Frozen solver, no scientific threshold may be a time limit; wall
    time is an operational figure only:
        B = 100000 nodes per problem
        variable order: static, by decreasing coefficient mass
                        sum_i |A_ij|, ties by ascending cell index
        branch order:   z_j = 0 first, then z_j = 1
        propagation:    interval bounds per row, lo_i and hi_i over the
                        unassigned coefficients; prune when c_i is
                        outside; force a variable when exactly one of
                        its two values survives the bound test on some
                        row; iterate to fixpoint before branching
        solution cap for OPPOSITE: K = 200 fiber solutions per pattern,
                        after which OPPOSITE is UNDECIDED for it
        no randomness, no restarts, no time-based cutoff
G4  T-A DECISION, and the classification state above it.
    Per-pattern outcomes aggregate to two independent verdicts:
        N_U = number of patterns with FIBER UNDECIDED
        classification of the weight-2 class is COMPLETE iff N_U = 0,
        otherwise it is INCOMPLETE. INCOMPLETE is NOT an integrity STOP
        and does not make the candidate defective; it forbids any
        statement about the class as a whole, and a successor with a
        larger budget or better propagation takes a NEW id.
    T-A verdict:
        FIRED      any pattern returns OPPOSITE-FEASIBLE. The explicit
                   pair kills T-A over S_pm outright.
        PROVED     unreachable in this candidate and retained only so
                   the logic is complete: it would require every pattern
                   OPPOSITE-INFEASIBLE together with a PROVEN cover,
                   which G2 does not have.
        UNRESOLVED anything else. [H] unchanged, no evidence claimed in
                   either direction.
G5  REGRESSION READBACK, last. The mask {21, 41, 37, 61} with its 191
    known realizations, the G6 pair, the equal-F_109 same-flow pair, and
    the sealed E' counts are checked against the machinery for
    consistency with the earlier records. They are construction inputs
    nowhere, they add no independent evidence, and they can only expose
    an implementation error or a contradiction.
```

## Field 2. CODE

`verify_k4_fiber_equation_solver_1.py`, assembled from the sealed parent
machinery plus the equation builder and the solver; hash recorded after
this freeze. Python standard library only; exact integer arithmetic and
Fractions; no float anywhere; deterministic stdout; environment LC_ALL=C
LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Two platforms,
byte-identical stdout. No declared wall-clock threshold: the node budget
B is the only bound with scientific standing, so the run is as long as it
is and the recorded time is operational.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. The G1 audit set is frozen:
the twelve bases of the sealed E' taken by the stride of the recon, all
their weight-2 patterns, and all disjoint weight-4 pairs from the first
fourteen of their patterns, exactly as the recon enumerated them, giving
1413 instances. The G3 pattern class is the 252 weight-2 patterns. The
G5 regression objects are named in G5 and enter nowhere else.

## Field 4. SYSTEMATICS

```
S1  polarization t(1) = -1 fixed.
S2  scope discipline: G3 quantifies over the frozen weight-2 pattern
    class; the FIRED direction of T-A carries to S_pm because an
    explicit pair is a pair, and no other direction carries.
S3  independence: every FEASIBLE witness is rechecked by a direct path,
    coordinate-by-coordinate F_109 comparison plus endpoint inertias by
    two exact paths.
S4  disclosed vacuous obstructions, motivating the solver and nothing
    else: the rational relaxation kills zero of 252 patterns, free
    dimensions 33 to 52, and the parity certificate kills zero of 252
    and zero of 29478 structurally enumerated weight-4 patterns. These
    numbers move no threshold after this pin.
S5  UNDECIDED is a property of a problem instance under the frozen
    budget. It is never counted toward FEASIBLE or INFEASIBLE, never
    reported as a scope on which something was proven, and never
    redefines the pattern class. Computational difficulty does not
    become a mathematical definition.
```

## Field 5. FAILURE THRESHOLD

Prereg freeze absolute at the SHA-256 of this file. Verifier construction
and debugging before the accepted run is ordinary work, disclosed by
superseded hashes; the accepted run is declared once by pinning verifier
and stdout. After that pin: a FAIL line fires the gated claim; a defect
in the verifier rather than in a claim, a gate name exceeding its test, a
check beyond this specification, or any change to B, K, the orders, the
propagation or the pattern class is an integrity STOP, and the candidate
dies under this id. INCOMPLETE classification and UNRESOLVED T-A are
ordinary outcomes, not STOPs, and are reported as such.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Carried verbatim from the sealed predecessor:

No claim is made that F_109 separates tables, S_4 orbits, isotypic
components, or arbitrary invariant-polynomial classes. The sole question
is whether flow is constant on every fiber of the frozen map F_109 over
the frozen two-profile locus S_pm of the stratum S.

Additionally not claimed: any characterization of the global fiber
relation; any bound on the weight of a fiber difference mask; any
statement about T-A from a clean weight-2 sweep; PROVED in any form; the
cubic [22] frontier, still asleep; minimality or sufficiency of anything;
the completeness of the seventeen at their bound; anything about zeta
zeros, RH, Weil positivity, explicit formulae, the infinite operator, J,
p = 5, decoder, measure, physical readings, or L2-L6 lifts. No registry
row, no status movement, no public movement from this candidate alone.
