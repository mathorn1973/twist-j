# Two-tick material read and the first failure under reuse

**L1 finite result.** A single H3 clock and a single prepared receiver distinguished raw phases 4 and 44 in all 85 fresh trials. Both writes occurred at transport on the second tick. The complete clock carrier was restored on that tick for every input. Continuous addressing from one initial preparation was falsified at tick 77. The full account and the inverse passed throughout the 3110-tick run. The machine-readable verdict for the conjunction is **FALSIFIED**. [Preregistration](PREREG.md) · [Exact output](EXPECTED.txt) · [Execution record](RUN.md).

## One receiver, three observable values

Observe the same scalar \(\mathrm{Tr}(R_0+R_2)/2\) of the receiver at \((1,1)\) on every trial. Raw rank is an input label used by the verifier to score the outcome. H3 chooses every collision and transport from the current lattice state and its native matching bit.

| Fresh input | Count | Head collision on ticks 1, 2 | Passive rail changed | Scalar after tick 2 | Change from initial value |
| --- | ---: | --- | --- | ---: | ---: |
| Raw 4 | 1 | \(B_1,B_2\) | \(R_0\) only | −20 | −5 |
| Raw 44 | 1 | \(B_2,B_1\) | \(R_2\) only | 0 | +15 |
| Other raw phases | 83 | Identity, identity | Neither | −15 | 0 |

The receiver started every trial at the same ordered pair \(((0,-3,6,-3),(-6,0,3,3))\) in the basis \(1,j,j^2,j^3\). For phase 4 its first rail became \((-6,-5,-2,-7)\). For phase 44 its second rail became \((-2,-2,-5,-1)\). The zero scalar for 44 therefore identifies a changed material state. No target wrote on the first tick.

## What returns after a fresh write

Take \(D=(-2,-1,-2,0)\) as the initial head half-gap. The read sends it to \(g=JD\) for raw 4 and \(g=J^{-1}D\) for raw 44. The single admitted vertical work contact sends \(g\) to \(\rho g\). Because \(h(\rho g)=h(g)\), the head satisfies the reverse branch predicate on that same forward tick. Its CLK returns to the funded value. All CORR coordinates, the other bare coordinates and the matching bit agree exactly with the uninstrumented clock at the corresponding cut. Both funded sites were checked separately.

The write survives in matter. The head's half-gap becomes \(\rho D\) and its midpoint changes by half the negative of the receiver's matter-sum increment. Thus the output and its compensating change are both present on the very cut on which the clock recovers.

At every tested transport and collision, the matter sum was \((-6,-3,9,0)\), the radiation sum was \((13,6,9,7)\), and the Hermitian sum over all 128 rails was \((465,0,109,109)\). The scalar account was \(821\), including the paid receiver and head. Collision inversion followed by inverse transport recovered the complete incoming field and matching bit on all 170 fresh-trial ticks and all 3110 continuously evolved ticks.

## What fails when the written receiver is used again

The uninterrupted run started at raw zero. It correctly wrote phase 44 at tick 75. At tick 77 the upper receiver rail changed from \((0,-3,6,-3)\) to \((-4,-1,4,-4)\), while the lower rail still held its phase-44 value. The corresponding head upper rail before this transport was \((0,3,4,3)\). Its difference from the receiver rail was \((0,6,-2,6)\), a nonzero member of \(2O\). The earlier write had therefore left the next upper contact enabled. No head collision at tick 76 was needed to open it.

The expected raw-4 read at tick 190 then took the identity branch. A rail movement at tick 191 consequently did not implement the specified raw-4 read followed by its write. Over 3110 ticks the receiver changed on 639 ticks. The projected bare clock returned at lap boundaries 622, 1244, 1866 and 3110, and differed at 2488. The funded entries had not all returned at any of these five boundaries. No full field-and-bit return occurred at any tick from 1 through 3110.

A separate same-session implementation using four-coefficient polynomial reduction directly in the \(j\) basis reproduced the 85 fresh outcomes, the 639 receiver changes, the first extra write at 77 and the absence of a joint return through 3110. It also followed the unstocked row \((1,3)\) at tick 1942, where an even material difference admitted transport into a previously zero rail. The formal transcript is the output of the pinned verifier.

## Recurrence and the next construction

A full return must eventually occur for this prepared finite-energy lattice. If \(z=\sum_{i=0}^3 a_i j^i\), then
\[
\mathrm{Tr}(z\bar z)=5\sum_i a_i^2-\left(\sum_i a_i\right)^2\ \ge\ \sum_i a_i^2 .
\]
Here the sum of traces over the whole field is \(2Q=1642\), so each of its 512 integer coefficients has absolute value at most 40. Including the two possible matching bits still gives a finite set. \(C_b\) is invertible because the active difference retains even parity and is rotated by a unit. \(B\) exchanges the two disjoint nontrivial branch domains and is its own inverse. Hence the tick map permutes this finite account shell. The complete period exceeds the tested 3110 ticks. The matching bit forces it to be even, hence at least 3112. Its exact value remains open. Any full return also repeats the extra write in the next traversal.

For persistent **absolute** output pairs, the two fresh words already identify an encoding constraint. They are \((u_4,v_0)\) and \((u_0,v_{44})\) with \(u_4\ne u_0,\ v_{44}\ne v_0\). Changing only the upper rail of the held phase-44 word necessarily leaves \(v_{44}\) in place. A direct switch to the phase-4 word thus requires changes to both rails or a different encoding. The observed failure at 77 occurs even before that switch. A next test can require one autonomously rearmed receiver with two distinguishable levels on the same held register and score a 44-to-4 transition from one initial preparation. Its first falsifiers should be an unsolicited work contact after 75 or a wrong level on the subsequent phase-4 completion. Neither a reset between inputs nor an externally chosen edge belongs in that test.
