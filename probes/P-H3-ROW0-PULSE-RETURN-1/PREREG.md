# Reading a pulse return behind the second H3 receiver

**Status O.** Prospective finite L1 probe. A. M. Thorn owns the probe reserved in [issue #2058](https://github.com/mathorn1973/twist-j/issues/2058).

Can a local read of the outgoing wave recover the orientation of an intact positive packet when the existing station abstains? The prediction is at least one additional correct plus, preservation of every previous sign and silence on every isolated or quiet control.

## Where and when to read

Use the integer evolution in the [public H3 kernel](../../reproduce/h3-referenced-record/verify.py) at content commit `0b6ae8e23d7086715b908cce6e1755d2898f55fc`. Its SHA-256 is `4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`. On a periodic two-row lattice of width 288, the leading source word starts at x1. Keep the stock in each row at x12 and x13 and the common x23 reference fixed for every presentation. Both material receivers return their scattered radiation to the evolving wave. Their exact integer stocks, source preparation, tick ordering, interventions and readout bond are specified in [physical.py](physical.py).

Observe only the two transfer words on x13 to x14 at each even tick from 98 through 256 inclusive. Each word has four integer coefficients. Divide it by their positive gcd, preserving sign and the zero word. The reader receives only this one record of 80 pairs. It writes once, at tick 256.

Let b be the locked predecessor decision, including its exact-control veto and row-1 onset correction. The latter changes an orbit-stage NEG to POS if the first nonzero late row-1 word occurs at tick 118. The [calibration](calibrate.py) computes the predecessor in memory using the public H3 evolution on fixed small-gain packets. It constructs signed primitive templates at absolute gains 2 through 11. For the two context rules it additionally uses gains 12, 13, 20, 21, 14, 15, 24 and 25. The row-1 motif comes from the opened calibration packet 0 to 1, mask phase 2, gain -16, at ticks 118 through 126. None of the prospective gains enters calibration. The exact scoring function and its tie and control rules are in [reader.py](reader.py).

For row 0 only, set a bit when any coefficient is nonzero at t = 98, 100, ..., 120. Return POS exactly when b is ABSTAIN, the whole projection passes the predecessor's exact-control veto and the twelve bits are `000111110001`. Otherwise return b. The pulse has five active samples at 104 through 112, three silent samples at 114 through 118, then a return at 120. Its row-0 observation at 118 leaves the row-1 correction at that tick intact.

## Packets and controls

For every absolute gain cross both gain signs, all five mask phases and all 20 ordered pairs of distinct fifth-root indices. The unordered pairs are the ten fronts. A FULL packet has positive orientation when (l - k) mod 5 is 1 or 3 and negative orientation otherwise. The sign of the gain controls the mask. In the SWAP intervention, exchange all radiation at x <= 0 after the first tick between the two reversed packets, with the leading region and matter kept in place. Read the donor's orientation. Generate HEAD and TAIL by the corresponding exchange with a quiet launch. Include ten repeated quiet presentations Q per panel.

| Panel | Previously opened replication gains | Fresh blind gains |
| --- | --- | --- |
| Ordinary | 705, 706, 707, 708 | 961, 962, 963, 964 |
| Stress | 768, 832, 896, 960 | 1024, 1088, 1152, 1216 |

Each pair of panels contains 1,600 FULL, 1,600 SWAP, 1,600 HEAD, 1,600 TAIL and 20 Q. The two new gain families exercise consecutive gains and multiples of 64 beyond the opened ranges. No selection by the observed wave or reader outcome is permitted. Report each of the 20 directed FULL groups. Keep SWAP out of the intact denominator.

## Forecasts and failure thresholds

1. Reproduce the opened intact result reported in #2058. Expect 1,597 correct decisions and three abstentions before the row-0 rule, followed by 1,600 correct intact decisions and zero writes among 3,220 controls. Check preservation of the intact row-1 corrections and the direction and phase of the three rescues.
2. At least one previously silent positive FULL should gain a correct POS. Count all previously silent true positives as opportunities. Any new plus on a true negative or control falsifies specificity. Any altered previously signed call falsifies preservation. Any signed HEAD, TAIL or Q fails the silence forecast.
3. Test complete sign coverage separately. A single wrong or silent decision on FULL or donor-scored SWAP fails complete coverage. Each SWAP should reproduce the entire raw port trace of its reversed FULL. Reversing an isolated HEAD should leave that raw trace unchanged.
4. Specifically predict recovery of every previously silent 0 to 1 FULL at phase 2. For a separate novelty test, freeze the reference set as **all two-row late projections in the 6,420 presentations of the two opened replication panels**. Predict at least one recovery on a positive, previously silent FULL whose complete projection is absent from that set. Count distinct projections as well as presentations. For individual rescues compare the complete raw late row-0 sequence with the opened rescues. A repeated row-0 trace and a new two-row projection can occur together. This public test bounds novelty to the stated comparator.
5. If an opportunity-based predicate has no eligible case, report INCONCLUSIVE. If opportunities exist but its threshold is missed, report FAIL. Report every predicate even when another one fails. The scope is finite L1 packet orientation at the named port.

## Blind commitment and replay

Freeze this document, [verify.py](verify.py), the measurement and scoring code, the gains and a SHA-256 commitment to a random 32-byte permutation secret in [custody.py](custody.py). Push the pin and read the files back before evolving any fresh packet. Concatenate the two fresh rosters in ordinary, stress order. Sort their indices by SHA-256 of the secret followed by the unsigned four-byte big-endian index. Give a separate reader only the shuffled projections and the public code it needs to read them. It outputs one decision record per presentation without labels, truth or the secret.

Publish the SHA-256 digests of the shuffled inputs and blind responses before disclosing the secret and opening the identities. Regenerate the inputs, check each committed answer, then compare the hash of every answer in canonical roster order with the exact verifier's hash. Batch files use compact ASCII JSON with sorted keys and one trailing LF. The seed changes only the order presented to the blind reader. A fresh replay needs only Python 3.10 or later and this repository.

```sh
python3 probes/P-H3-ROW0-PULSE-RETURN-1/verify.py
```

The gain choices, clocks, veto, threshold, two receivers, reference and both readers stay fixed through opening. Record scientific failures and absence of opportunities under this pin.
