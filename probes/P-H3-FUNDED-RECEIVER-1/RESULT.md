# A fixed funded receiver holds a two-edge source-dependent write

**Finite computational candidate, L1.** Recipe 324 uses the same initial stock redistribution on every one of the 85 ready-clock predecessors. On raw 43, a native source B2 at tick 125 causes the first receiver difference 32 ticks later. At tick 157 B the actual receiver writes a new ordered matter pair relative to its pre-B value. The arm in which the source B2 was undone stays idle. Both arms retain their respective exact pairs at 158 C and 158 B. The actual write restores the receiver's launch word. [Frozen protocol](PREREG.md) · [Primary transcript](EXPECTED.txt) · [Execution record](RUN.md).

## One physical preparation for every rank

Use the (1,j,j²,j³) basis, with J=1+j². Put t=−j⁴=(1,1,1,1) and w=Jt=(1,0,1,1). Recipe 324 reduces to the following single operation for all 85 inputs.

| Site | At launch |
| --- | --- |
| Receiver (7,3) | Set (R0,R2,CLK,CORR) to (w,−w,2t,0) in the previously empty cell. |
| Payer (7,1) | Replace CORR q=(3,4,4,8) by q−2t=(1,2,2,6). |
| Balance (4,1) | Put (v,−v) into the empty matter pair with v=(−1,−1,1,−1). |

All other words keep their original launch values. In particular, the original six clock CORR words are exact for 85/85, and the 85 complete launch fields are distinct. The source, initial matching bit and forward H3 law are unchanged at initialization. Later source histories are allowed to respond to the preparation.

The matter sums of both inserted pairs cancel, and the CLK addition exactly matches the CORR debit. The remaining identity is h(q)−h(q−2t)=h(2t)+2h(w)+2h(v). Each term is evaluated in the ring. M=(−9,2,−2,−3), U=(19,7,5,19), H=(463,0,152,152) and Q=774 agree with the original ingress at launch and on every tested cut.

## Which contact writes, and why the inverse stays idle

In recipe 324 there were 124 source B2 events across 17 of the 85 inputs. Of these, 115 launched west. Four events gave a first isolated CORR difference at the target, two produced direct local work and one produced an exactly held work. All four first arrivals occurred on raw 43. The source event at tick 65 also led to an actual write, which failed retention. The event at tick 125 has the following witness. Recipes 300 and 408 use exactly the same launch on this rank and provide a full two-arm witness in their primary records.

| Cut | Actual receiver | Matched comparison |
| --- | --- | --- |
| Before 157 C | Matter (t,−t), CLK (2,1,2,2), CORR j | Same entire recipient |
| After 157 C | Same three non-CORR words; CORR j | Same three non-CORR words; CORR (1,2,0,3) |
| After 157 B | B1, matter (w,−w), CLK 2t, CORR 0 | Idle, matter (t,−t) |
| After 158 C | Matter (w,−w), CLK w, CORR 0 | Matter (t,−t) |
| After 158 B | Idle, matter (w,−w) | Idle, matter (t,−t) |

Absolute tick 157 selects the westward (0,3) to (7,3) CORR edge. In the actual arm the donor (6,2,2,4) has different parity from j, so the transport is refused. In the comparison arm the donor (4,1,2,4) and recipient j have equal parity, so the contact changes CORR. B1 in the actual arm sees matter half-gap t and radiation half-gap w=Jt. The comparison radiation half-gap is nonintegral. On the following transport the actual CLK changes from 2t to w, while both matter rails stay fixed. Since w has odd coefficients and CORR is zero, the next B cannot reverse the write. The first and last edge directions are west; intermediate paths over 32 ticks were not identified.

The receptor is initialized with (w,−w). It already carries another word by the time the signal arrives. The established operation is therefore a source-controlled return to a stored word with exact retention through the next tick. The registered test did not require a blank launch receiver, a never-before-seen output, a universal write across ranks, or a full clock-cycle hold.

## Family census

Each row groups preparation IDs and includes all 85 starts per ID. Columns count source-event comparisons. Repeated preparations, ranks and emission times can describe the same physical write.

| Preparation | Modes | Source events | Isolated first arrivals | Direct writes | Held writes |
| --- | ---: | ---: | ---: | ---: | ---: |
| Unfunded | 1 | 170 | 1 | 0 | 0 |
| Permutations and contacts at launch | 247 | 57,880 | 65 | 48 | 0 |
| Directly funded from a radiation payer | 64 | 8,288 | 135 | 55 | 6 |
| Whole native preimage | 8 | 1,689 | 29 | 29 | 0 |
| Initial column projection, with declared fallback | 8 | 1,006 | 18 | 6 | 2 |

All eight held rows are on raw 43. The four strict westward rows (300, 324, 408, 411) share the same initial state and receiver event. The two column-projection rows used the declared fallback on this rank. Four other rows followed eastward launches and converted later than their first isolated receiver contrast. Distinct initial-state counts are recorded per mode.

The earlier raw-0 target remains informative. Whole-preimage mode 400 placed (−J,J,−2,0) at 91 C and retained the source emission at 81 B. The receiver wrote (−1,1) under B2. The next C kept the matter pair, and 92 B restored (−J,J) by B1. This is one exact failure of the hold test. Its six input clock words differ from the original projection. The fixed launch recipe 324 above requires no inverse-designed initial state or mapping from phase labels to actions.

## Evidence limits

The 247-recipe raw-0 pilot on first westward arrivals was known before the public pin and is explicitly disclosed there. The complete census and its extended work and hold tests were executed after public byte readback. Full native reversibility includes the physical register state, so a local word can be restored while information remains elsewhere. Independent scientific review and generalization beyond this finite fixture remain open.

## Retention over the rest of the recorded window

A post-run analysis replayed recipe 324 for all 85 inputs in Python. All 124 event projections matched its frozen native-table digest. It then replayed each held row and grouped identical launch fields, ranks, emission ticks and write ages. The eight rows reduce to three distinct launch-and-event witnesses, all on rank 43. In each the actual B1 restores its exact launch pair (w,−w), while the comparison holds (t,−t) at that cut. [Analysis code](followup.py) · [Exact records](RETENTION.txt).

| Equivalent modes on this rank | Emission | Held write | First later cut with equal actual and comparison matter | First later change of actual word |
| --- | ---: | ---: | ---: | ---: |
| 300, 324, 408, 411 | 125 west | 157 B | 165 B | 166 B |
| 303, 327 | 106 east | 152 B | 159 B | 161 B |
| 306, 330 | 106 east | 134 B | 141 B | 152 B |

For the fixed recipe 324, the live receiver had first left its launch pair at 9 B. Across the interval from 157 B through 165 C inclusive, the restored word remained exact and distinguishable from the comparison. At 165 B the comparison caught up. The actual word stayed exact through 166 C. The listed cuts are first losses; the records allow subsequent recurrence.
