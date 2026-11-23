# Three silent positive packets recovered at the outgoing H3 port

**Status C.** The row-0 pulse-return rule supplied three correct positive writes on previously silent intact packets in the two preregistered fresh panels. All 11 registered predicates passed. This finite L1 result applies to the x13 to x14 port on the periodic 288 by 2 station frozen in this probe, with receivers at x12 and x13 and the reference at x23. The same pin fixes the predecessor reader and its row-1 correction at tick 118. [Preregistration](PREREG.md)

## Preregistered fresh panels

| Outcome | Ordinary | Stress | Combined |
| --- | ---: | ---: | ---: |
| FULL correct before the row-0 rule | 800/800 | 797/800 | 1,597/1,600 |
| FULL correct after the row-0 rule | 800/800 | 800/800 | 1,600/1,600 |
| SWAP correct against donor orientation | 800/800 | 800/800 | 1,600/1,600 |
| Isolated HEAD silent | 800/800 | 800/800 | 1,600/1,600 |
| Isolated TAIL silent | 800/800 | 800/800 | 1,600/1,600 |
| Quiet controls silent | 10/10 | 10/10 | 20/20 |

The predecessor was silent on three positive FULL presentations out of 800 positives. All three were recovered. The rule retained every previously signed call, including all 34 intact POS calls from the row-1 tick-118 correction. It added no wrong FULL or SWAP calls, and the exact-control veto held. All 20 directed FULL groups scored 80/80 across the two panels. The three matching SWAP copies also changed from ABSTAIN to their correct donor sign. The intact denominator excludes these copies. All 1,600 SWAP traces matched their reversed FULL donors word for word, and all 1,600 HEAD traces matched their reversals.

Of the 3,226 fresh presentations on which the predecessor abstained, 224 passed the exact-control veto. The added rule made six correct writes and zero wrong writes on those 224 presentations. These were the three intact positives, their three exchanged copies and 218 isolated tails. The veto screened all heads, all quiet controls and the other 1,382 isolated tails. No control matched the pattern. All 800 negative intact packets already had signed readings, so the forecast concerning a new plus on an abstaining negative had zero opportunities. Across all intact packets, the pattern appeared on 120 of 800 positives and 0 of 800 negatives. The two opened panels give the same opportunity counts.

## The three new writes

All three cases were FULL, directed 0 to 1, with mask phase 2. They were the only silent FULL cases in that direction and phase. Each passed the exact-control veto. At the even ticks from 98 through 120, the first row gave the registered activity pattern `000111110001`. It was active at 104, 106, 108, 110 and 112, silent at 114, 116 and 118, and active again at 120. Each new POS was issued at tick 256.

| Fresh signed gain | Paired opened gain | First nonzero late row-1 transfer in both | Fresh predecessor | Fresh final |
| ---: | ---: | ---: | --- | --- |
| −1216 | +832 | 144 | ABSTAIN | POS |
| +1088 | −960 | 186 | ABSTAIN | POS |
| +1216 | −832 | 238 | ABSTAIN | POS |

All six rescues shared the same raw row-0 sequence across all 80 late samples. The signed gains in each pair differ by 2048. Their raw row-1 words first differ at the common onset shown in the table. Across the stress panel, 600 fresh FULL presentations had an opened counterpart with the same direction and mask phase and a gain congruent modulo 2048. In 536 of those pairs, the complete raw two-row port trace matched at all 123 recorded ticks.

The public comparator contains 735 distinct projections from all 6,420 presentations in the two opened panels. The three fresh rescues have distinct two-row projections absent from this comparator. Their differences from the paired opened rescues occur only in row 1. The added pulse rule reads row 0. In total, 213 distinct fresh FULL projections were absent from the comparator. Among the 155 absent positive FULL projections, the predecessor was silent on three, and the rule recovered all three.

## Opened replication and verification

The two opened panels reproduced 1,597 correct FULL calls and three abstentions before the rule, followed by 1,600 correct FULL calls and no writes among 3,220 controls. The three opened rescues were all 0 to 1 at mask phase 2. Their signed gains and first nonzero late row-1 ticks were −832 at 238, +832 at 144 and −960 at 186. All 34 opened intact row-1 corrections were preserved.

The reader preserves each signed baseline output and withholds a write under the exact-control veto. These two guarantees establish predicates 7 and 8 in the verifier's declaration order. Complete correctness on FULL and SWAP (predicates 1 and 2) implies zero wrong additions in those arms (predicates 4 and 5). The separate opened-panel replication forecast is enforced by `historical_guard`, which aborts the verifier on failure. The frozen preregistration describes the procedure in prose without separate labels for the equation, systematics and action layer specified in [POLICY section 3](../../POLICY.md#3-one-probe-one-branch).

The public record dates three publications in order. The first fixed the rule, verifier and fresh roster. The second committed the hashes of the shuffled inputs and answers at `dad53aa85bf7e003507525ac343ac69d273e6064`. The third disclosed the permutation seed and the result. The frozen reader is deterministic, so shuffling can change only the order of its answers. The opening audit checked all 6,420 answers against the committed bytes and the canonical answer hash matched the verifier's hash. This verifies custody. The timing of any private evaluation remains unverified.

The verifier ran on Linux x86_64 under CPython 3.10.12 in 292 seconds and exited successfully with empty stderr. The exact scores by direction, predicate results and answer hash are in [EXPECTED.txt](EXPECTED.txt). The public pin, opening and reproduction commands are in [RUN.md](RUN.md).
