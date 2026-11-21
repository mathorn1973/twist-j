# A recurrent H3 write supplies a native B1/B2 decision

**Candidate C, finite L1 computation.** On the unchanged rank-43 orbit, writer 1 repeats a B2 write, its ordered output reaches receiver 0, and receiver 0 executes B1. A different native emission on the same directed edge reaches the same receiver in exactly the same pre-C state and with the same incoming radiation. It executes B2. Both material contacts change the receiver. The original functional renewals at writer 28 have a different outcome. Their outputs produced zero downstream material transfers in the stated census. [Preregistration](PREREG.md) · [Exact data](EXPECTED.txt)

## A matched receiver with two actual transfers

Each word below denotes an ordered antipodal pair by its first rail, in the basis $(1,j,j^2,j^3)$. Both reads use matching bit zero on edge 1 to 0.

| Earlier matching writer B2 | Emission | Emitted word | Read | Receiver material after C | Receiver B | Material after B |
| ---: | ---: | --- | ---: | --- | --- | --- |
| 330940 | 598058 B2 | (2,0,0,0) | 598060 | (−1,−1,−2,−2) | B1 | (−1,1,−1,−1) |
| | 720019 B1 | (0,2,0,2) | 720028 | (−3,0,−1,−2) | B2 | (−1,0,0,−2) |

The earlier B2 at 330940 has the same writer, matching, complete pre-C writer, ordered input material, incoming radiation and ordered output material as the B2 at 598058. In both cases C moves material at the writer and at its upstream donor. The donor gives up the input on the first occurrence and has recovered it at the second. After each listed emission, both emitted rails stay unchanged at the writer through every intervening C and B until contact with receiver 0. The second row supplies a native B1 writer as the comparison.

The receiver's initial four rails at both encounters are $(−2,−2,0,−2)$, its negative, $(1,0,0,0)$ and $(−3,−4,−2,−4)$. Its two incoming radiation rails also match exactly. For the H3 collision let $d$ be the material half-difference after C, $f$ the radiation half-difference and $h$ the Hermitian norm. Here $f=(2,2,1,2)$ in both cases. The exact norm values explain the branch choice.

| Quantity | Value in the j basis |
| --- | --- |
| $\Theta=h(J)$ | (2,0,1,1) |
| $h(d_1)$ | (3,0,−1,−1) |
| $h(f)=\Theta h(d_1)$ | (5,0,2,2) |
| $h(d_2)=\Theta h(f)$ | (12,0,7,7) |

The first equality selects B1, the second B2. Both evaluations use events that actually occurred. The two full fields have different histories. The determination by the word applies to the receiver's stated local inputs. A supplementary five-coordinate Python replay from the original launch through tick 735779 reproduced all four distinct reported encounters, including these two. [Replay and hashes](RUN.md#supplementary-replay-of-the-four-reported-encounters)

## Coverage and the original proposed chain

The 85 unchanged launches cover 1,851,392 ticks and all 32 sites. The scan found 104,259 recurrent B2 writes under the local repeat signature. Counts below are unordered pairs of encounters and can share an encounter. Columns and rows overlap.

| Source condition | All matched B1/B2 pairs | Material moves on a qualifying arm | Material moves on both arms |
| --- | ---: | ---: | ---: |
| At least one original functional renewal at 28 (A) | 0 | 0 | 0 |
| At least one original 181 B renewal (A181) | 0 | 0 | 0 |
| Both original functional renewals (AA) | 0 | 0 | 0 |
| At least one recurrent local B2 (R) | 60 | 8 | 1 |
| Both recurrent local B2 (RR) | 4 | 4 | 0 |

Two of the 60 pairs occur on rank 0 and 58 on rank 43. All eight pairs with material change on a recurrent arm occur on rank 43. The sole two-transfer pair is given above. A second witness on edge 3 to 0 has recurrent B2 writers on both arms. The 735778 B emission arrives at 735779, changes the receiving material and gives B1. The 354162 B emission faces a parity refusal at 354163 and the receiver gives B2. That read leaves the pre-C material unchanged. All four RR pairs have material transfer on exactly one arm.

The primary test for the writer of the v114 second-write claim returned zero. The original classifier recovered 842, 826 and 12,938 later functional writes on ranks 0, 22 and 43, respectively. Across those 14,606 writes, 14,613 contacts occurred while the ordered word still had continuous provenance. At zero of these contacts did C change the receiver's material, and zero receivers executed a material-changing B. In particular all three 181 B outputs face refusal on both material rails at 182 C and the receiver executes B0. The bound is the registered family and horizons, with no conclusion about eventual behavior outside them.

The corpus, clock, ledger and matching evolve from the published inputs. No writer output was exchanged to obtain either receiver branch. Selection of an original functional write at 28 uses its historical paid control only on a separate copy. All statements are finite, Q9 remains open, and Public Canon v114 retains its registered statuses. [Execution record](RUN.md)
