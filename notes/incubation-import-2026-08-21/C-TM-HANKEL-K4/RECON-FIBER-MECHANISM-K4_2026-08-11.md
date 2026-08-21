# RECON fiber mechanism, k4, 2026-08-11

NON-CANONICAL. Two runs, abstract tables only; the seventeen reals and the
G6 pair are read nowhere in either script. Purpose: try to KILL T-A
cheaply BEFORE freezing a candidate around it, and find the mechanism
that produces F_109 collisions at all. Scripts
recon_fiber_mechanism_k4.py and recon_fiber_mechanism2_k4.py, logs
recon2.log and recon3.log, all in the fleet handoff repo.

## The structural handle

F_109 contains all ten orbit sums, so two tables in one fiber differ by
SWAPS, each swap flipping one plus and one minus INSIDE one orbit.
Weight-2 fiber neighbours are single swaps, weight-4 are disjoint swap
pairs. Small-weight fiber search is therefore COMPLETE at its radius, not
sampled. This is what makes an attack on T-A possible at all.

## Run 1, blind complete search at radius 4

40 abstract two-profile bases spread through D by a fixed stride:

```text
weight-2 swap moves tested   4948      fiber collisions 0
weight-4 swap moves tested 284859      fiber collisions 0
```

Zero collisions of ANY kind, same-flow included. F_109 fibers are thin:
the map is very close to injective on the two-profile locus, and a blind
neighbourhood search will not kill T-A.

## Run 2, the mechanism behind the one known collision

The known equal-F_109 pair differs in exactly four cells, and the mask is
exactly two swaps: cells 21 and 41 inside orbit 1, type (0,0,1,2), size
12; cells 37 and 61 inside orbit 8, type (1,2,2,2), size 4. A structured
move, not noise.

Applied as a fixed mask to every abstract two-profile table of D:

```text
eligible (mask acts as two swaps)  6943
F_109 preserved                     179
profile flipped                       0
```

So the move is a genuine fiber-generating mechanism with a family of 179
pairs, and T-A survived 179 independent chances to die.

Same-shape sweep, one swap in a size-12 orbit and one in a size-4 orbit,
4752 masks against a 400-table probe: only the known mask registered a
hit. Stated honestly, that is a PROBE-DEPENDENT observation, not a
structural uniqueness claim: F_109 is S_4-equivariant, so the whole S_4
orbit of a live mask is live on the corresponding images of those tables,
and the probe slice is not S_4-closed. The correct reading is that
same-shape moves are rare and concentrated, not that the mask is unique.

## Verdict for the freeze

The cheap kill failed. T-A is not falsifiable by small-weight
neighbourhood search, and the one mechanism in hand never flips the
profile. That is exactly the state in which freezing T-A is scientifically
right rather than premature, and the mechanism gives the successor a real
engine instead of blind sampling.

## T-C, held NON-CANONICAL by owner decision: the cubic [22] frontier

Recorded, not posed. gram22 equality is NOT equality of the [22]
component: the G6 pair differs in all four isotypic components, including
[22], and no S_4 element relates its two tables. The equality is a
collapse of the quadratic O(5) reading. So the intuition that orientation
lives in [22] is not dead, but its quadratic version is; anything left
must sit beyond the Gram quotient, naturally at degree 3 or higher, and
therefore OUTSIDE the frozen parent map with its own ambient accounting.
Building cubic [22] invariants now would mean constructing them against a
pair we already know, which is precisely the search effect this lane
avoids. It waits until T-A is decided.
