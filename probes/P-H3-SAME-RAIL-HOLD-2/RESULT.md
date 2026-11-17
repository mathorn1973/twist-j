# A renewable same-rail counter and its phase ambiguity

**Finite L1 result.** In a single native H3 circuit the upper rail held the phase-44 write from tick 75 through the next read at tick 190, took a second value at the phase-4 write at 191, and remained fixed between every subsequent pair of writes. All 85 fresh trials, full accounts, inverse steps, ten-transfer schedule and complete period passed. Both preregistered tests of absolute phase identification were falsified. [Exact output](EXPECTED.txt) · [Execution record](RUN.md) · [Preregistration](PREREG.md).

## What the receiver holds

| From the same initial preparation | Tick | Upper rail in the \(1,j,j^2,j^3\) basis | Half-trace |
| --- | ---: | --- | ---: |
| Prepared receiver | 0 | \((-9,0,-3,-3)\) | −15 |
| Raw 44 write | 75 | \((-3,2,-5,1)\) | −5 |
| Raw 4 read, preceding word still held | 190 | \((-3,2,-5,1)\) | −5 |
| Raw 4 write | 191 | \((3,4,3,5)\) | 0 |

In all fresh two-tick trials the two targets alone triggered upper-rail transport. Both produced \((-3,2,-5,1)\) when started from the same fresh stock. The other 83 inputs kept the initial word. The passive lower rail stayed zero. No preparation intervened between the two writes in the table.

## Why the clock clears after each write

At both target cuts the head takes \(B_1\). Write \(D=(1,-1,-1,1)\), \(g=JD\), and \(n\) for the number of completed work contacts. The receiver word is \(P_n=-g-2\rho^n g\). The head's material midpoint and half-gap at a cleared cut are \((\rho^n-1)g\) and \(\rho^n D\). The read multiplies that half-gap by \(J\). The selected upper-rail contact advances its orientation by \(\rho\), preserving its Hermitian norm. The next collision can clear by \(B_2\) when the read's radiation half-gap survives transport.

The previous Q706 stock lost that half-gap at tick 191. In Q616, immediately before each work transport, both radiation-edge differences have an odd coefficient:

| Raw phase | Head CLK minus receiver CLK | Head CORR minus left-neighbor CORR |
| --- | --- | --- |
| 44 | \((-2,3,0,0)\) | \((0,1,0,-6)\) |
| 4 | \((-3,0,-1,0)\) | \((5,4,9,2)\) |

Both radiation contacts therefore leave their inputs in place, and the native \(B_2\) restores the head CLK and the bare CORR on that same work tick. The verifier checked the entire bare carrier and all funded coordinates on both substeps, including at the two former failure times 77 and 193. The [earlier failed experiment](https://github.com/mathorn1973/twist-j/blob/cd45ae66e915131e6456c9c5972d8448498f5836/probes/P-H3-SAME-RAIL-HOLD-1/RESULT.md) retains its original output.

## The complete cycle

Each 622-tick bare-clock lap contains two work events. Across five laps the full receiver-write schedule was 75, 191, 697, 813, 1319, 1435, 1941, 2057, 2563 and 2679. No other transport or collision changed either passive matter rail. The first repeated complete state and bit occurred at tick 3110 and equaled the initial preparation exactly. The autonomous deterministic dynamics therefore repeats this schedule on subsequent cycles.

At each transport and collision, the full matter sum was \((-9,0,-3,-3)\), the radiation sum \((19,8,7,11)\), and the Hermitian sum \((380,0,144,144)\), with scalar account \(Q=616\). Every decorated tick recovered its complete input by collision inversion and inverse transport. A separate same-session replay using four-coefficient \(j\)-basis arithmetic agreed on all 85 trials, on every substep in the five-lap run, on all ten receiver changes and on the first full return at 3110.

## Why the last phase cannot be decoded from this rail

Five successive transfers visit five different exact ring words because \(\rho\) has order five and \(g\ne0\). In lap \(k\), raw 44 writes \(P_{2k+1}\) and raw 4 writes \(P_{2k+2}\), starting at \(k=0\). Both sequences traverse every residue modulo five. For a concrete coincidence, tick 75 (44) and tick 1435 (4) both store \((-3,2,-5,1)\). Even a reader of all four coefficients must assign the same value to that pair of observations. This is a held count of selected contacts modulo five. Other raw ranks contribute zero to the count.

The head already carries a target-dependent transient. Its post-read CLK is \((-1,3,0,0)\) for 44 and \((-2,0,-1,0)\) for 4, in different classes modulo \(2O\). A next construction could use these classes to select different material changes while clearing the radiation disturbance they create. Its decisive test would require two distinct words from equal initial receiver stock, disjoint output classes over the complete coupled cycle, and a full forward return. The present construction meets the return and hold requirements; it has a common material advance for both reads.
