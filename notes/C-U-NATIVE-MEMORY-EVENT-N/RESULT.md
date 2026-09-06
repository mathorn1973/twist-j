# Native memory and fixed-event reader: result

Status: **NON-CANONICAL incubation; candidate-T; L1 only.** Issue #861.
Authority remains Public Canon v78. No Canon or sealed probe was changed.

## Exact disposition

The candidate `V(next)=-V(x)` is true throughout X14 for both control bits.
Its sign quotient supplies exactly 313 invariant messages: 312 fibres of
20 checkpoints and one of 10. Every fixed invariant checkpoint reader
factors through this quotient. An explicit target-independent preparation
and readback realizes every message without an added register.

This is static storage. Every actual synchronized native trajectory visits
every point of its record fibre with positive limiting frequency. Hence any
eventually constant fixed checkpoint reader was already constant on that
whole fibre. A permanent blank-to-written transition after synchronization
is impossible in this precise reader class under unchanged U. The protected
record also cannot recover distinct original QDD records after native mergers.

The exact clock has 100 reachable states, one strongly connected component
and period one. Its per-letter densities are 1/150 for equal adjacent bits
and 1/75 for unequal adjacent bits. The proof establishes convergence along
every prefix length. The finite audit supplies a shorter primitive
certificate than the analytic bound: M^29 has minimum entry 1778335 and
row sum 536870912, yielding contraction factor 89759353/134217728.

## Complete fixed-reader spectra

Let F_D be all rationals in [0,1] with reduced denominator at most D.
The table refers to one fixed chart orbit. All 3125 chart labels were checked.

| Reading | Nonzero protected vector | Zero protected vector |
| --- | --- | --- |
| Binary checkpoint density | k/20, 0<=k<=20 | k/10, 0<=k<=10 |
| Decorated density, all ticks | k/60, 0<=k<=60 | k/30, 0<=k<=30 |
| Decorated density conditional on either driver bit | k/30, 0<=k<=30 | k/15, 0<=k<=15 |
| LOW fraction among accepted events | F_60, 1103 values | F_30, 279 values |
| Accepted LOW fraction restricted to either bit | F_30, 279 values | F_15, 73 values |

Every atom is assigned whole to LOW, HIGH or SILENT. Empty acceptance is
UNDEFINED. No reader is selected by a target comparison, and the table does
not assert simultaneous realization of independent targets on overlapping
orbits by one common reader.

There are 22 distinct supported QDD LOW weights from 624 nonzero piston
tuples (15600 supported heads). Eight fail even the largest permitted
accepted-event set F_60:

    1/256, 1/176, 1/136, 1/96, 9/224, 9/104, 9/64, 49/64.

In particular the least positive possible accepted frequency in this class
is 1/60, excluding 1/256. The weight 9/14 is individually attainable with
acceptance, but that existence supplies no physical choice of a reader.
EXPECTED.txt retains the complete comparison for every weight and mode.

Thus the protected-register route succeeds as mathematical storage and
fails as a permanent post-synchronization writing mechanism in the frozen
class. The fixed-event-reader route fails to realize the entire supported
QDD weight law. This is not a theorem that general physical sampling is
impossible, and it does not close QDD-INSTRUMENT-APPARATUS, its children,
the physical decoder, or any L1-to-L5/L6 bridge.

## Evidence and review

The first recorded Linux x86_64 execution passed all 463333 exact checks,
exit 0 and empty stderr, at the immutable code pin recorded in RUN.md.
The proofs give algebraic and all-prefix arguments; finite large-clock
samples only audit them. A separate same-session mathematical review checked
the component proof, four-digit clock certificate, contraction and prefix
argument, atom collisions, and complete integer allocation argument.
This was collaborative review, not blind independent confirmation.

The verifier is self-contained standard-library code. It has no network,
filesystem reads or writes, subprocesses, private imports, randomness,
floating point, external data, credentials, or target-selected reader.
All added material is textual and below the policy size limit; no workflow,
license or public authority changed. Public promotion requires its own
named, prospective, result-exposed probe and required architecture checks.
