# C-K4-FIBER-EQUATION-SOLVER-1: all gates PASS, T-A UNRESOLVED, 2026-08-11

```text
STATUS:  incubation candidate, NO AUTHORITY. Every gate passed; no claim
         is promoted. T-A stays [H] with no evidence in either direction.
PREREG   sha256 8158dd5792329dc00131ad938b03af5f068823832cef14a6c1f52da70d7f34ff
VERIFIER verify_k4_fiber_equation_solver_1.py
         sha256 52105ce8979f7ddcc7ee58598c5535218dbdb6b8afdc0627f607180090afef2f
         49821 B, assembled from the sealed parent f487114a...
STDOUT   sha256 f695aa7aa473390df864e6b99c3e253203a6386ca6a0c93bd726ffe62b73594c
         2856 B, exit 0, empty stderr, 8 of 8 checks PASS
LEG 1    x86_64, accepted run, under a minute
LEG 2    aarch64, Debian 13 (trixie), Python 3.13.5, same verifier hash
         confirmed before execution, stdout f695aa7a... byte-identical to
         leg 1, empty stderr, exit 0
SEALED   2026-08-11. Both legs complete, two-architecture evidence
         closed, candidate administratively finished under this id. No
         successor reuses the id and no later run reopens it.
```

## G1, the fiber equations: candidate-T, proof plus audit

The bilinear expansion is printed in full by the verifier and is the
proof; the audit is [C] at finite scope and carries no quantifier. All
1413 frozen instances agree with direct F_109 comparison, and the audit
set count is itself gated. Of those 1413 instances, zero were genuine
fiber pairs: the audit tests the equivalence, not the existence.

## G3, the decisive numbers

```text
FIBER    252 FEASIBLE, 0 INFEASIBLE, 0 UNDECIDED
OPPOSITE 0 FEASIBLE, 0 INFEASIBLE, 252 UNDECIDED
nodes    maximum 53 on any single problem, budget 100000
witness  cells 0 and 2, table 0x4, F_109 equality rechecked directly,
         both endpoint inertias (8, 0, 8) by two exact paths
```

EVERY weight-2 pattern is realizable. Explicit fiber pairs were
constructed, not found: the solver solves the linear system and the
witnesses come out immediately, 53 nodes at worst. The decoupling behind
that speed is structural and worth recording: for a weight-2 pattern only
26 of the 99 rows are nontrivial, because a row (a, b) has a nonzero
coefficient only for cells in the orbits of a and b, and the right hand
side vanishes unless one of them sits in the pattern's own orbit.

## What this settles and what it kills

The thin-fiber reading of every earlier run is now dead as an
explanation. F_109 fibers are NOT thin over the stratum: weight-2 fiber
pairs exist for all 252 patterns, in abundance, since the constrained
variables number about two dozen and the rest are free. The reason
47934 weight-2 moves in the sealed predecessor produced not one fiber
pair is that all of those moves started INSIDE the two-profile locus.
The rarity was never in the fiber condition. It is in the two-profile
condition.

That reframes T-A precisely. The question is no longer whether fibers
are thin but whether the abundant fiber family ever meets S_pm twice
with opposite flow. The witness at 0x4 has both endpoints at (8, 0, 8),
the balanced skeleton, far outside S_pm.

## G4, and the honest limit of the frozen design

```text
classification of the weight-2 class: COMPLETE, N_U = 0
T-A verdict: UNRESOLVED
```

The FIBER side is fully decided with zero UNDECIDED, so the weight-2
pattern class is completely classified. That still proves nothing about
T-A, exactly as the freeze said in advance: no theorem bounds the weight
of a fiber difference mask.

The OPPOSITE side returned UNDECIDED on all 252 patterns, and the design
reason is now explicit and was disclosed in the freeze: the profile is a
spectral condition, so it cannot enter the linear solver and can only
filter enumerated solutions. Each pattern's solution family is enormous,
the frozen enumeration order assigns the unconstrained cells to zero
first, and those tables sit at (8, 0, 8). The first 200 solutions per
pattern therefore never reach S_pm. This is a limitation of the frozen
enumeration, not a fact about T-A, and it must not be read as one.

## G5, regression readback

The known mask reproduces exactly 191 realizations on the sealed E', the
same figure recorded before; the equal-F_109 same-flow pair satisfies the
frozen equations; the G6 pair still agrees on gram22 and differs on the
full map. No implementation error and no contradiction with any earlier
record.

## The successor's problem, stated sharply

Find a table x with x and x XOR m both in S_pm for an admissible pattern
m, or prove that none exists. The linear part is solved; the spectral
part is untouched. Two routes:

```text
1  spectral-driven search: enumerate the fiber family in an order driven
   by the two-profile condition rather than by cell index, for instance
   by starting from tables already known to be two-profile and solving
   the linear system with those cells fixed. Note this changes what is
   pinned, so it is a new frozen design and a new id.
2  incompatibility theorem: show that the fiber equations and the
   two-profile condition cannot both hold at low weight, which would
   prove T-A on the weight-bounded class and, with a cover theorem,
   close it outright.
```

Route 1 is the falsification arm and is cheap to freeze. Route 2 is the
only one that can ever confirm. Neither is opened by this candidate.
