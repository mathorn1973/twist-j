# The first handoff held, then the second clear failed

**Finite L1 result.** The new common-branch stock held the phase-44 word on the physical upper receiver rail from tick 75 through the read at 190. Phase 4 changed that same rail at tick 191. The head failed to clear at 191, and the next unsolicited upper-rail write occurred at 193. The proposed uninterrupted schedule and full return were falsified. All native accounts and inverse-step checks passed. [Exact output](EXPECTED.txt) · [Preregistration](PREREG.md) · [Run record](RUN.md).

| Event from one preparation | Tick | Exact upper rail in the \(j\) basis | Half-trace |
| --- | ---: | --- | ---: |
| Initial | 0 | \((3,9,3,0)\) | 0 |
| Raw 44 write | 75 | \((-1,1,1,4)\) | −5 |
| Next read, word still held | 190 | \((-1,1,1,4)\) | −5 |
| Raw 4 write | 191 | \((5,3,-1,-2)\) | 10 |
| First extra write | 193 | \((1,5,7,2)\) | −5 |

## Why the clear failed

The preregistered transient was calculated incorrectly for both targets. In a \(B_1\) read, the CLK increment is \((J^{-1}-1)f\) with \(f=(K-U)/2\). In the basis \(1,j,j^2,j^3\), the actual increments were \((0,3,4,3)\) for 44 and \((-1,0,3,3)\) for 4. CORR received the opposite increment. Consequently the first discrepancy against the predicted full field was already at the collision of tick 74. The raw-44 clear still succeeded at 75.

At tick 191, the head CLK difference from the passive CLK before transport was \((-6,-6,0,-2)\). Its CORR difference from the left partner was \((4,2,6,-2)\). Both are in \(2O\), so the two radiation contacts transported. After transport the head had CLK \((-3,-3,-3,-4)\) and CORR \((-5,-4,-4,-5)\). Their difference \((2,1,1,1)\) forbids the collision. The upper write at 191 is real, and its missing clear is visible in the full state.

## Scope of the checks

All 85 fresh preparations were tested. Only 4 and 44 wrote an upper rail, and they produced the same word from fresh stock. Only 44 cleared. In the uninterrupted run there were 19 receiver changes and no full-state return through 3110 ticks. The raw clock and all four decorated account components passed their respective checks, including scalar \(Q=706\). Inversion recovered the full incoming lattice and bit on each decorated tick. A separate same-session implementation using four \(j\)-coefficients reproduced the inputs, writes, missing clear and first extra transition.

The verifier reports PASS for the narrow disjointness test on the two sets of writes found at the scheduled stream positions. Each set contains only one word, from the first lap. Repeated handoffs, the ten-write schedule, and the predicted five words per phase all failed. Those two observed singletons cannot establish a reusable phase identifier. A successor should use the actual post-read CLK and CORR differences at both transported edges when selecting the stock, then repeat the full preregistered checks.
