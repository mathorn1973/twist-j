# CORR restores the head radiation and exposes a material limit on hold

**Finite L1 result.** A funded horizontal CORR contact distinguishes phases 44 and 4 on one receiver rail and restores both radiation rails of the head on the work tick. Every other fresh input leaves the receiver word untouched through that tick. The best of the three relay preparations holds the phase-4 word through tick 11. Its native upper matter contact changes the word on tick 12, and two different last phases give exactly the same word at the same age on tick 337. A reusable phase register on this rail therefore fails for these preparations. [Protocol](PREREG.md) · [exact primary output](EXPECTED.txt) · [execution and replay](RUN.md).

## What the second tick writes

Coordinates below use the basis (1,j,j²,j³). Read is tick 1 and work is tick 2, counted from the bare predecessor of each fresh card. Both steps use native transport C followed by collision B. All 85 cards of each preparation started with the same receiver matter stock. The common initial upper word was (−9,0,−3,−3).

| Fresh card | R₀ after work C | R₀ after work B, with relay | Head / receiver work branches |
| --- | --- | --- | --- |
| 44 | (−3,2,−5,1) | (−3,2,−5,1) | B2 / identity |
| 4 | (−3,2,−5,1) | (−5,0,−5,0) | B2 / B2 |
| Each of 83 others | (−9,0,−3,−3) | (−9,0,−3,−3) | Receiver word unchanged throughout both ticks |

The no-relay control ends at (−3,2,−5,1) for both targets. With the relay, the raw-4 even CLK edge joins equal values (−2,0,−1,0). The change comes through CORR. At raw 4 the work transport changes receiver CORR from (0,0,3,−1) to (−4,2,1,−2), making the radiation half-gap D. The receiver takes B2. At raw 44 the corresponding horizontal contact refuses. Cards 3 and 43 have a later word change on tick 4 in all four preparations.

At both targets the head executes B1 then B2. Its paid CLK returns to (0,2,−1,1). Its CORR returns to the exact reference value, (0,0,3,−1) at raw 4 and (−2,0,−1,−5) at raw 44. The head material half-gap becomes ρD, with the original norm 5. Its actual matter rails are now (−1,0,3,−2) and (−5,−2,−1,−2). Thus the head recovers its radiation and its gap norm while its matter midpoint changes. The full carrier still differs at (0,1). From the physical raw-zero launch the relay already changes CORR there on tick 2 C, before the first expected read. None of the three relay launches from raw zero produced a state-qualified read within 1000000 ticks.

## Hold, ambiguity and full return

| Preparation | Q | First loss after fresh 4 | First loss after fresh 44 | First complete return from the raw-4 predecessor |
| --- | ---: | --- | --- | ---: |
| Control, no relay | 637 | Holds until next write | Holds until next write | 3110 |
| CORR relay | 719 | 3 B | 2878 C | 3600 |
| Relay + CLK support | 722 | 4 C | 2878 C | 57770 |
| Relay + CLK and matter supports | 725 | 12 C | 12482 C | 264800 |

In Q719 the inverse receiver collision B1 undoes the fresh raw-4 write. Q722 blocks that inverse and the next even upper matter edge reopens. Q725 delays this contact further. On tick 12 C it changes R₀ from (−5,0,−5,0) to (2,4,1,3). The receiver collision at this tick is identity.

The Q725 raw-44 history holds its fresh word until tick 12482 C. In the separately initialized raw-4 history, tick 337 B gives exactly the raw-44 word (−3,2,−5,1). At 337 B the two histories are at the same cut, 335 ticks after their distinct net writes on tick 2. Neither has an intervening qualified work. This single witness rules out decoding the last phase from the receiver word even when its age and matching bit are supplied. It compares two admissible histories. The complete Q725 orbit from the raw-4 predecessor contains only raw-4 qualified writes, with three distinct words, at ticks 2, 35602 and 153430. The rail changes outside qualified work 69492 times on this orbit.

Across all 85 starts the no-relay control returns at exactly 3110, holds between all ten qualified writes and has the same five-word class for both phases. The three funded relay designs give no trial containing both qualified phases in the 3110-tick all-input sweep. An empty class cannot establish separation. [All registered starts and per-run digests](SWEEP.txt).

A subsequent all-input coverage check ran Q725 from each predecessor to first complete return or 1000000 ticks. Of 85 starts, 54 return at 2160, four at 220488 (ranks 23, 28, 33, 38), and one at 264800 (rank 4). The remaining 26 had no return within the bound. Every one of the 85 has an actual receiver change outside qualified work. In 83 starts no read qualifies within the covered interval. From the other two, only the starting phase qualifies. All returns include every rail and the matching bit. The finite violations disprove continuous valid operation independently of the 26 unknown periods. [Additional coverage, one row per predecessor](COVERAGE.txt).

## Why a single matter support reaches its limit

A local consequence of the contact law explains the 12 C failure and constrains the next design. Let H, A, R be the upper head, auxiliary and receiver values immediately after work tick 2, with H≡R modulo 2O and H≠R. Suppose the receiver holds at every intervening substep. Suppose collisions leave the head and auxiliary upper rails unchanged and the auxiliary's even contact leaves it fixed, up to the next loss or tick 12 C. Each even head–receiver edge that preserves the receiver also preserves the head, by conservation of their sum. The only possible head changes are the five odd contacts with the same auxiliary.

Their map preserves the midpoint and multiplies the half-difference by ρ on its admitted domain. That domain is invariant, and a refused pair stays fixed. Consequently the fifth such contact returns the head exactly to H. The even tick 12 edge must now change the receiver by (1−ρ)(H−R)/2, which is nonzero. An initially refused auxiliary edge gives the earlier loss at tick 4 C. The Q725 phase-4 trajectory attains the five-contact bound. This argument is conditional on the stated rail and collision guards. A future persistent design must change at least one of them before recontact, for example by a native collision that removes the head's returning upper value and restores the CORR supply before the next read. That mechanism remains open.

## Conservation and reversibility

Each row gives the exact sums over all 128 rails. The last column is half the field trace of the Hermitian sum.

| Preparation | Matter sum | Radiation sum | Hermitian sum | Q |
| --- | --- | --- | --- | ---: |
| no_bridge | (−12,0,−4,−4) | (16,8,6,11) | (394,0,151,151) | 637 |
| bridge | (−12,0,−4,−4) | (19,12,10,19) | (439,0,159,159) | 719 |
| supported | (−12,0,−4,−4) | (19,11,9,19) | (440,0,158,158) | 722 |
| material_support | (−13,0,−5,−4) | (19,11,9,19) | (442,0,159,159) | 725 |

There were zero account or inverse violations. The primary checked both substeps and reconstructed all incoming rails and the bit on every tick. The separate C++ implementation checked each newly used nonidentity map, sampled whole-state inverses and searched for literal complete returns. This is a tested separation between reversible network evolution and retention on one receiver rail, at the circuit level of H3.
