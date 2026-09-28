# Independent analytical review: restricted single-link reachability

**PUBLIC / NON-CANONICAL. Analytical review only; candidate-T ceiling.**

Item: C-PHOTON-RESTRICTED-REACHABILITY-N.

This review used the frozen parent definitions in
`notes/C-PHOTON-TWIST-SNAKE-SECTOR-N/PROOF.md` at
`fc16df1b06d971ca7ef4e2f35eab92d8b9637bdb` and
independent mathematical reasoning. It did not read the other proof agent's
work and did not execute computations or verification code. It is not a blind
two-architecture computational confirmation.

## Verdict

The ideal restricted single-link update graph is connected on each of
`C_0(n)` and `C_-(n)` for even `L >= 4`, `k in {1,2}` and
`1 <= n <= L^2`. The argument below includes link-field fibers, rather than
only the graph of plaquette residues. With positive exact single-link
conditional probabilities, the systematic full-sweep kernel is irreducible
and aperiodic on each class.

No mixing-time estimate follows. No numerical implementation or observed
finite trajectory is certified by this argument. In particular, it does not
change the recorded `INCONCLUSIVE_EQUILIBRATION` outcome or close P1.

## 1. Reduction to bounded occupancies on a dual graph

Fix one twisted 01 slice and put `m = L^2`. Its dual graph is the connected
square torus with `m` vertices and `2m` edges. The original 0- and 1-links
are its oriented edges. Changing one such link by a field element changes
the two adjacent effective plaquette residues by opposite field elements.

For centered representatives `a_p in {-2,-1,0,1,2}`, put

```
x_p = a_p + 2 in {0,1,2,3,4},
T = sum_p x_p = 2m + k + 5w.
```

The fixed source adds `k` to the total residue and does not affect the
incidence matrix of changes. The possible totals are exactly the integers
between `0` and `4m` congruent to `2m+k` modulo five. Incidence on a connected
graph is surjective onto the zero-sum face fields, so every face assignment
with the required total residue has a link-field lift.

A nonwrapping unit transfer from a vertex of occupancy at least one to an
adjacent vertex of occupancy at most three is one permitted single-link
change. It preserves `T`, hence preserves `w` and the global class.

## 2. Fixed-total bounded occupancy lemma

**Lemma.** On any finite connected graph, configurations of integer
occupancies from zero to four with a prescribed total are connected by
adjacent unit transfers that respect these bounds.

One explicit proof uses labeled slots. Replace every vertex by four slots,
join slots within that vertex, and join every slot at one endpoint to every
slot at the other endpoint of an original edge. The resulting slot graph is
connected. Occupancy configurations lift to subsets of slots of the fixed
cardinality. Simple exclusion on a finite connected graph is connected:
along a spanning tree, fix leaves to match a target subset, using the nearest
particle or vacancy in the remaining tree whenever the next leaf disagrees;
the path to the nearest such item has only the opposite kind at its interior,
so successive adjacent exchanges perform the correction. Remove the fixed
leaf and continue. A slot exchange inside one original vertex has no effect
on occupancies. An exchange across an original edge projects to a permitted
unit transfer. Projecting a slot path proves the lemma.

The lemma includes total zero and total `4m`, where there is one occupancy
configuration. It does not assume that a vacancy exists at every vertex or
that a proposed transfer can pass through a saturated vertex directly.

## 3. Monotone descent and ascent of total winding

Let `r` be the least nonnegative residue of `2m+k` modulo five. At any total
`T > r`, one has `T >= 5`. Pick adjacent vertices. By the lemma, redistribute
at fixed `T` so their combined occupancy is

```
t = min(T,8) in {5,6,7,8}.
```

This allocation is feasible even near the upper boundary: if `T > 8`, the
remaining amount `T-8` is at most `4(m-2)`. If their occupancies are `x,y`,
change their residues to `0,t-5`. This is one modulo-five opposite transfer,
since the new pair total is congruent to the old pair total. It lowers the
integer occupancy total by exactly five and lowers `w` by exactly one.
Repeated redistribution and this wrapping move reach total `r` monotonically.
At that total, the lemma permits a chosen canonical arrangement, for example
all `r` chips on a designated face.

For ascent use holes `4-x_p`. The same descent argument for holes increases
`T` by five until its maximum allowed value. It also reaches a fixed canonical
maximum arrangement by transfers at fixed total.

The exact winding extrema of one twisted slice are

```
w_min = -floor((2m+k)/5),
w_max =  floor((2m-k)/5).
```

For the stated parameters, `w_min <= -6` and `w_max >= 6`.

Doing the descent separately on each twisted slice never increases the
global `W_n`. Thus it stays in `C_-(n)` and reaches the same canonical minimum
face layout on every twisted slice. Doing the ascent separately stays in
`C_0(n)` and reaches the same canonical maximum layout. Every face step is
realized by the corresponding original single-link update; no nonlocal face
operation has been substituted for a legal move.

## 4. Link-field fibers, including gauge and torus degrees of freedom

Equal face fields do not imply equal link fields. If two link fields give
the same effective residues on a slice, their difference is in the kernel
of the dual incidence matrix over `F_5`. This kernel is the full cycle space.
Choose a spanning tree and its simple fundamental cycles. Every kernel
element is a field-linear combination of those cycles. This statement
includes contractible and noncontractible cycles, so neither gauge degrees
of freedom nor torus holonomies have been discarded.

To add a coefficient times one simple cycle to the link field, update its
edges in consecutive cyclic order. Every proper partial path changes only
its two endpoint face residues; the interior changes cancel in `F_5`.
Their centered representative sum changes by a multiple of five with
absolute value at most eight. It therefore changes by only `-5`, `0`, or
`5`. During the cycle implementation, the slice winding differs from its
starting value by at most one. At cycle completion its face layout is
restored exactly.

For `C_-(n)`, its integer threshold is

```
B_minus = -floor(n/2)-1,
W_star  = n*w_min,
W_star+1 <= -6n+1 <= B_minus   (n >= 1).
```

Thus every cycle path at the all-minimum layout stays in `C_-(n)`. For
`C_0(n)`, the integer threshold is `B_zero = -floor(n/2)`, and

```
W_star = n*w_max,
W_star-1 >= 6n-1 >= B_zero.
```

Every cycle path at the all-maximum layout stays in `C_0(n)`. The large slack
is material: connecting only fixed-total face configurations would not by
itself establish connectivity of link-field fibers at a restrictive boundary.

Links in directions two and three, and 0- and 1-links of untwisted slices,
do not affect `W_n` and can be changed freely. Changes to the other
plaquette orientations affect only positive weights, not class membership.
After connecting fibers at the common canonical extreme face layout, reverse
the target field's descent or ascent. This connects arbitrary two fields in
the same class by allowed single-link changes.

## 5. From paths to the systematic-sweep kernel

The ideal exact weight `2+2*cos(2*pi*f/5)` is strictly positive for all
`f in F_5`. A candidate link value is therefore assigned positive conditional
probability precisely when its new field lies in the restricted class.
The current link value is always such a candidate.

A single allowed link change can be realized in one full fixed-order sweep:
all links before and after the chosen update retain their values. Every
factor in the probability of this sweep is positive. Concatenating such
sweeps realizes any allowed path with positive probability. Consequently
the systematic-sweep transition matrix is irreducible. An entirely idle
sweep also has positive probability at every field, giving aperiodicity.
The full systematic-sweep kernel need not itself be reversible; that property
is unnecessary here. Its invariance follows from invariance of each
single-link conditional update.

## 6. Scope and remaining gap

The reachability result applies to the exact ideal Markov kernel with the
stated link fields and class restrictions. It does not give a useful lower
bound for path probabilities, a spectral gap, a relaxation time, a bound on
reset bias, or a bound for an observable's finite-run error. A connected
state graph can have extremely slow communication between well populated
regions. Thus the observed ladder disagreement and long-lived untwisted
configurations remain unresolved equilibration problems.

The proof also does not certify floating-point probabilities, pseudorandom
generators, source-code correctness, or the actually executed program.
Those are separate questions. No Canon claim or thermodynamic lower bound
is promoted by this review.

## Pre-pin source review

A separate static source review compared localize.py and its specification
with the parent's subset_logs, schedule, JSON fields and reset code. It
found one descriptive defect, corrected before the pin: initialization
may force slice zero into its class, while the recorded forced flags and
totals count only subsequent twist-advance resets. Null reset distances
mean before the first recorded twist-advance reset. The estimator,
metadata and runner review found no blocking source defect. No program
was executed during this review.
