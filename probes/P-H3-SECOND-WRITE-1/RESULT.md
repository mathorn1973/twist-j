# The same H3 receiver writes again at 181 B

**Finite computational candidate, L1.** On raw input **43**, a single launch of the unchanged four-wire H3 circuit gives a word-controlled B2 at **159 B** and again at **181 B** in cell (7,0). At 179 C contact restores the ordered material word W at (7,3). At 180 C another contact restores the worker's CLK. On 181 the worker has exactly the same four pre-C values, both incoming post-C radiation values and all four post-B values as on 159. Replacing only W on the read bond by the old word T, through a compensated full-field exchange, changes the second worker outcome to B0. From launch the actual trajectory uses only the native update of the field and matching bit. [Exact output](EXPECTED.txt) · [Frozen protocol](PREREG.md) · [Execution record](RUN.md).

## Where the 22 ticks go

The word is the ordered pair ±w, with w=(1,0,1,1) in the (1,j,j²,j³) basis. The first read consumes it on 159 C. The same matter bond and the adjacent CLK bond each preserve their midpoint and rotate their half-gap by ρ=j² on admitted contacts. Five such rotations return a half-gap to its starting value. Their relative timing matters. This short interval was also reconstructed directly from the literal field after the primary measurement. [Local contact replay](local_trace.py).

| Cut on input 43 | What happens |
| --- | --- |
| 160 B | The worker executes native B1 and locally reverses the previous B2. The rest of the field continues forward. |
| 167 C to 169 B | W reappears on 167 C and reaches the next read bond. On 169 C that contact consumes W, but the worker's incoming CLK is (−1,1,−1,0) and B stays idle. |
| 170 B and 171 B | The worker executes B2 with the same local outputs as at 159. Its matching bit is 0 and the memory lacks W. On 171 B a native B1 reverses that local B2. |
| 179 C | The (7,3)–(7,0) matter contact sends first rails (1,0,0,2) and (−1,0,0,0) to w and (−1,0,−1,1). The second rails have opposite sign. Both sites take B0. |
| 180 C/B | The memory holds W at both cuts. The (7,0)–(7,1) CLK contact restores worker CLK=(0,2,0,2). The worker's CORR is zero. |
| 181 C/B | The live contact changes the worker's first material rail from (−1,0,−1,1) to (1,1,0,2). The native B2 writes (0,1,0,1) and its negative on the two material rails. Reading consumes W again. |

The last uninterrupted interval of W before the read begins on 179 C. The earliest later restoration with the original **B1** mechanism (T to W at the memory) is 226 B. Ordinary **C** transport has already restored the word needed for the second write.

## Which intervention changes the second write?

| Raw 43 intervention on a comparison copy | At 181 B | First qualifying work after tick 159 |
| --- | --- | ---: |
| Actual field | B2 | 181 |
| Exchange W for the reserve T at (4,1), immediately before 181 C | B0, worker material stays unchanged through C and B | Single-tick comparison |
| Omit the original source B2 at 125 | B0 | 597 |
| Omit the first worker B2 at 159 | B1 | 169 |
| Omit the subsequent source B2 at 167 | B2 with the same worker pre-C and incoming radiation | 181 |

The remote word exchange preserves M,U,H,Q and agrees with a direct substitution at the worker's matter contact. Both arms have exactly the same worker before C and the same radiation at B. This isolates the effect of the restored word. The omissions at 125 and 159 also change the worker's later inputs and shift the timing of work. The 167 source event was the only fresh B2 at that source in the tested post-159 lookback. Undoing it does not disturb the 181 write. These control copies do not drive or reset the actual field.

## All 85 inputs and the exact account

The full launch list matches the published four-wire list for [#2024](https://github.com/mathorn1973/twist-j/pull/2024) byte for byte in its ordered encoding. All inputs retain their six original CORR words. Ranks 0, 22 and 43 are the three inputs with the qualifying first write at 159. The second-write test applies to those three. All 82 other inputs still undergo the complete native forward and inverse audit and the unconditional B2 census.

| Input | Ticks from launch | First later word-controlled write | Later word-controlled B2 count | With exact original worker readiness |
| --- | ---: | ---: | ---: | ---: |
| 0 | 65,536 | 181 | 842 | 722 |
| 22 | 65,536 | 181 | 826 | 627 |
| 43 | 1,048,576 | 181 | 12,938 | 10,331 |
| Other 82 | 8,192 each | Outside the 159-first-write condition | — | — |

Each count excludes the original 159 write. The exact-readiness column is a subset of the preceding column. No full launch field and bit returned during any of these scans. The observed 22-tick delay is the time between the first two qualifying writes on these inputs. The material of the second write can recur while the rest of the lattice continues to change.

Across **1,851,392** native ticks, the verifier checks M=(−9,2,−2,−3), U=(19,7,5,19), H=(463,0,152,152) and Q=774 after each C and each B. Every one-step inverse and all 85 complete terminal-to-launch inverses recover the full required state, including the matching bit for each complete run. The independent five-coefficient Python implementation rechecks the initial window on all 85, the later reads on all three first writers, and saved raw-43 fields at the registered events. The million-tick census uses the native four-coefficient kernel.

A separate [finite-state recurrence argument](RECURRENCE.md) bounds eventual full-field repetition. Its proof does not give the observed latency. The measured mechanism renews the local word and worker within the forward circuit; the initial four-wire preparation remains supplied as in the predecessor.
