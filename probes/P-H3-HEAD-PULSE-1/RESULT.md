# A native auxiliary interrupts the returning head

**Finite L1 result.** The same auxiliary collision fires just after both target writes. On raw 4 the receiver's CLK feedback keeps that collision from reversing, so the next head–auxiliary upper contact refuses. On raw 44 the collision reverses and the head continues. This is a phase-conditioned change in the native work path, produced with fixed initial stock and the existing update. The active collision delays the first loss of the raw-4 word from 12 C to 28 C. The held words still coincide across phases. [Preregistration](PREREG.md) · [primary transcript](EXPECTED.txt) · [execution records](RUN.md).

## Fresh input and causal cuts

All five preparations were tested on every one of the 85 fresh predecessors. On the first two ticks only raw 44 and raw 4 cause a change on the upper receiver rail. Both start at (−9,0,−3,−3) and reach (−3,2,−5,1) at the transport of tick 2. At 2 B raw 44 retains that word and raw 4 writes (−5,0,−5,0). At both work cuts the head has its exact paid CLK and reference CORR. Its matter delivers work. The rest of the funded carrier fails the work-cut recovery criterion.

In the ingress-active circuit B2 acts at A=(1,3) on tick 3 for precisely these two fresh ranks. The equal-energy sign control takes no B2 there on tick 3 on any rank. Other fresh starts can fire at later cuts. On the two target histories the immediate B2 inputs at A are identical. Its matter half-gap is −1, its radiation half-gap is (0,1,1,0) and J times that radiation gap is −1. The auxiliary upper output is (3,3,4,1).

| Substep | Raw 4 | Raw 44 |
| --- | --- | --- |
| 3 B | Auxiliary takes B2 | Auxiliary takes B2 |
| 4 C | Neighboring S/A CLK inputs (1,1,1,0) and (−1,−1,−1,0) exchange part of their values | S still has (0,−1,−1,0) and the CLK edge refuses |
| 4 B | Auxiliary takes identity | B1 reverses the auxiliary collision |
| 5 C | Upper A/H residues differ and the contact refuses | The upper contact moves the head |
| 12 C | Receiver still holds its raw-4 word | Receiver still holds its raw-44 word |
| 28 C | First loss of the raw-4 word, to (2,4,1,3) | Raw-44 word still held |

On raw 4 the head upper rail has one nonidentity transport in ticks 3 through 12, against six in the baseline. On raw 44 it has five in both circuits in that interval. These are observed displacements of a specified rail. A common orientation, a turn counter and a recurrent two-phase clock would need additional evidence.

## Controls and finite failures

Times are local to the corresponding target predecessor. All reported first losses occur at transport. Equal-age aliases compare the two distinct tick-2 writes at the same elapsed cut, with the same matching bit and no intervening qualified work in either history.

| Preparation | Q | First loss, raw 4 | First loss, raw 44 | First equal-age alias | First complete return from raw 4 within 1000000 |
| --- | ---: | ---: | ---: | --- | ---: |
| Baseline | 725 | 12 | 12482 | 337 B | 264800 |
| Ingress, active | 774 | 28 | 5184 | 370 B | Above bound |
| Ingress, sign control | 774 | 12 | 3222 | 317 B | 802274 |
| Delayed upper contact, active | 753 | 20 | 13844 | 90 B | 236110 |
| Delayed upper contact, sign control | 753 | 12 | 12482 | 73 B | 506776 |

The delayed active circuit supplies opposite upper values to the even S–A edge on tick 10. The equal-input sign control leaves the pair fixed there. At 11 C the active contact history blocks H–A. The head moves again at 19 C and the raw-4 word is lost at 20 C. This provides a second causal route around the five-contact hypothesis of the [previous result](https://github.com/mathorn1973/twist-j/pull/2012).

At 370 B the ingress-active circuit gives (−3,2,−5,1) in both target histories, 368 ticks after their original distinct net writes. Continuous decoding from R₀, age and bit thus fails. In the 3110-tick raw-zero stream A takes B2 601 times without a single qualified target read. Counting auxiliary collisions alone cannot identify phase or distinguish a successful write. No registered run had both qualified labels on the same trajectory.

For each active design the long census covered all 85 rank predecessors to a full return or one million ticks. The ingress circuit returned within the bound on 54 inputs, the delayed circuit on 59. The other 31 and 26 periods respectively remain bounded below. Each of all 85 runs in each active design exhibited an upper receiver change outside qualified work. The distinct physical raw-zero launch supplied zero qualified reads in all five million-tick tests. The 606 supplemental runs covered 73571204 ticks, counting overlap between runs. [Coverage by input](COVERAGE.txt) · [word-class intersections](ALIASES.txt).

## Exact accounts

| Preparation | Matter sum | Radiation sum | Ring Hermitian sum | Q |
| --- | --- | --- | --- | ---: |
| Baseline | (−13,0,−5,−4) | (19,11,9,19) | (442,0,159,159) | 725 |
| Ingress, active | (−9,2,−2,−3) | (19,7,5,19) | (463,0,152,152) | 774 |
| Ingress, sign control | (−17,−2,−8,−5) | (19,7,5,19) | (463,0,152,152) | 774 |
| Delayed, active | (−10,−1,−6,−3) | (19,11,9,19) | (457,0,161,161) | 753 |
| Delayed, sign control | (−16,1,−4,−5) | (19,11,9,19) | (457,0,161,161) | 753 |

The primary audit found zero account and inverse failures. The separate C++ audit verified all newly used nonidentity maps, with 18203 additional complete-cut account and inverse audits. The sign controls match the Hermitian energy and sector parities. Their full linear matter sums are reported above. The construction establishes reversible read-dependent feedback over a finite interval. Recurring qualified writes with a persistent word on this rail remain open.
