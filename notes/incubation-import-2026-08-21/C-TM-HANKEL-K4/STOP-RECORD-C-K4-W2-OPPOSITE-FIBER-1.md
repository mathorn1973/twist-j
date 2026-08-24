# C-K4-W2-OPPOSITE-FIBER-1: killed UNUSED before any accepted run

```text
STATUS:  DEAD, id retired without ever being run as an accepted run.
         No verifier hash was pinned, no stdout was pinned, no gate
         produced a result, no threshold moved. The defect is in the cost
         of the frozen design, not in any claim.
PREREG   sha256 458b4ecf2cd5ac36c11476be64d613ad581a9359d5c50d144edd916fe4c81ea6
         frozen and archived; it stands as written and is not amended.
DATE     2026-08-11
```

## What the build-time measurement showed

The frozen design enumerates V_m per pattern and computes both endpoint
profiles exactly at every leaf. Two numbers, measured before any run:

```text
free bits per pattern, histogram over the 252 weight-2 masks
    6 free bits: 72 patterns      7 free bits: 36 patterns
    9 free bits:  6 patterns     19 free bits: 138 patterns
leaves to exhaust, sum of 2^free                    about 72 million
measured leaf rate, exact profiles by two paths     about 600 per second
```

That is roughly 33 hours on the x86_64 leg and several times that on the
aarch64 leg, which makes the required byte-identical two-platform run
impractical rather than merely slow. The frozen node budget of 3000000
per pattern is adequate, so the design is DECIDABLE; it is the wall time
that kills it, and wall time was explicitly denied any scientific
standing in the freeze. The correct conclusion is therefore that the
design is sound and unaffordable, not that a threshold should move.

Since Field 5 makes the freeze absolute at its SHA-256, the budget, the
orders and the leaf rule cannot be edited. The id dies unused and a
successor carries the corrected design. Nothing was computed against this
freeze, so nothing is retracted and no result is lost.

## Two things the aborted build did establish, and they are worth keeping

FIRST, a proven safe spectral filter now exists, which the frozen id
explicitly declined to claim. Both target profiles have an odd negative
index, 7 and 9, so both force det K < 0. The determinant is therefore a
NECESSARY condition that can never discard a reachable target inertia,
and it is exact and cheaper than a full inertia by a large factor. The
frozen id could not use it; a successor can, and must prove it in its own
G1 rather than assert it.

SECOND, a structural split of the pattern class. 114 of the 252 patterns
have at most 9 free bits and together need only 12288 leaves, which is
seconds of work: that sub-class can be decided COMPLETELY. The remaining
138 patterns carry 19 free bits each and hold all 72 million leaves. The
split is not an artifact of the search; it is a property of how strongly
the fiber equations pin each pattern, and it means a complete answer for
a well-defined half of the class is available immediately while the other
half waits for either compute or a theorem.

A first reachability probe over three patterns, 720 deterministic
free-bit assignments, found ZERO endpoints of either target profile. That
is a hint about where the answer lies and it is NOT evidence: it gates
nothing, it is disclosed here, and it must not enter a successor's
construction.

## What the successor should carry, for the owner to arbitrate

```text
1  the determinant filter, proven in its own gate, applied before any
   full inertia, with both exact paths still required on every survivor
   and on every reported witness
2  the complete decision of the 114 cheap patterns as a first-class
   result, reported per pattern
3  an honest budget for the 138 expensive patterns, with UNDECIDED
   reported per pattern and INCOMPLETE as the global verdict if any
   remains, exactly as the owner froze the semantics
4  no change to the fiber-first direction, the forbidden inputs, or the
   three global outcomes
```

The alternative the owner already named stays open and is now more
attractive than it was an hour ago: the structural no-go route, where the
weight-2 flip is a low-rank change of the operator and the question is
whether it can move two negative directions to positive without a zero
endpoint mode. That route needs no compute at all if it works.
