# The restored word triggers a native worker write on tick 159

**Finite computational candidate, L1.** A single fixed four-wire input preparation accepts all 85 original clock inputs. On inputs **0, 22 and 43**, the memory at (7,3) restores the ordered matter pair (w,−w) on 157 B, holds it over the entire next tick, and causes a separate cell at (7,0) to execute B2 on 159 B. H3 selects the bond and the collision from the evolving field and matching bit. The remaining 82 inputs give no worker write satisfying this causal test in the registered window. [All 85 rows for both preparations](EXPECTED.txt) · [Literal launch](launch43.json) · [Frozen protocol](PREREG.md).

| Launch preparation | Distinct inputs with six exact clock words | Source B2 at 125 | Restoration at 157 B | Strict worker B2 with both controls |
| --- | ---: | ---: | ---: | --- |
| Two CLK shifts computed from the six-word sum | 85 | 64 | 3 | 0, 22, 43 |
| Four original CLK inputs routed with constant offsets | 85 | 4 | 3 | 0, 22, 43 |

For the four-wire preparation the fourth source event occurs on input 64. It does not restore the material word at 157 B. Both preparations begin from exactly the same physical field on input 43. Their agreement there confirms reproducibility of that field. Their differing source counts on other inputs show the dependence on launch preparation.

## What the stored word does

At 125 B, site (1,3) emits through B2. On 157 C the two histories first differ at the memory. At 157 B the actual B1 restores ±w, with w=(1,0,1,1), while the history with the single source emission undone holds ±t, with t=(1,1,1,1). On 159 C the native vertical matching couples the memory to its neighbor across the periodic boundary. The four worker inputs at the beginning of this contact and both post-C radiation rails agree between histories.

| Worker on input 43 | First matter rail before C | After C | After B | Branch |
| --- | --- | --- | --- | --- |
| Actual H3 | (−1,0,−1,1) | (1,1,0,2) | (0,1,0,1) | B2 |
| Earlier source B2 undone | (−1,0,−1,1) | (−1,0,−1,1) | (−1,0,−1,1) | B0 |
| Swap the memory word with a remote ±t immediately before C | (−1,0,−1,1) | (−1,0,−1,1) | (−1,0,−1,1) | B0 |

The second material rail is the negative of the first. The remote exchange uses site (4,1), preserves the whole ledger and leaves the worker's incoming radiation identical. On the live arm the material contact gives h(u)=(5,0,3,3), equal to h(J)h(f) for the unchanged incoming radiation half-gap f=(0,1,0,1). In both controls h(u)=(4,0,1,1), and the worker remains idle. Thus perturbing only the earlier emission or exchanging the stored word both remove the worker write. The actual circuit executes neither intervention. Reading consumes ±w at 159 C.

## What is fixed at launch

The literal 32-site field was found by designing around a known event on input 43. From this public field the four-wire construction copies the six original CORR words and loads four CLK rails by the same formula on every input. Each target CLK receives the original input at its source plus a constant. The other 118 of 128 rail values stay fixed across inputs. Site indices are 4x+y.

| Source CLK | Target CLK | Fixed offset in (1,j,j²,j³) |
| ---: | ---: | --- |
| 0 | 7 | (−2,0,−1,0) |
| 1 | 28 | (−3,0,−1,0) |
| 2 | 8 | (1,0,2,3) |
| 3 | 31 | (0,1,0,1) |

All 85 input fields are distinct and retain their six original CORR words. Other rails differ from the bare clock circuit, including the matter at the four source-CLK sites on input 43. Native generation of this initial preparation and renewal of the consumed word for a later autonomous write remain open. The experiment establishes a downstream material operation on three input phases through 164 B, with all 85 tested. It does not establish a periodic controller or an exclusive detector of phase 43.

The C++ and Python dynamics agree on every one of the 170 instrumented rows. Both C and B preserve M=(−9,2,−2,−3), U=(19,7,5,19), H=(463,0,152,152) and Q=774. A separate forward loop driven only by the field and bit reproduces all three actual worker cuts on input 43, then the complete 164-tick inverse recovers all 128 rail words and the launch bit for every start. [Execution record](RUN.md).
