# Result: preparation, native information boundary and conditional event record

Status: `T` proposed by the separately reviewed exact proofs; non-canonical
candidate until a separate public fold.
Outcome: `NATIVE-OBSERVABILITY-CLASSIFIED; CONDITIONAL-PREPARATION-TO-RECORD-PROVED`,
subject to required pull-request acceptance on both architectures.
Action layer: L1 only.

## What the complete native apparatus history carries

For an arbitrary common driver and a fixed source-independent apparatus
ready state `(q,r)`, the complete native apparatus history depends on the
four initial pistons only through their sum `kappa` modulo five. Every
generator closes on `(z,q,r)`. The proof is an exact commuting identity
followed by induction for all times, not an extrapolation of finite traces.

For the fixed-origin Thue-Morse driver, the complete all-time observation
equivalence is decided by the first three observations `(A0,A1,A2)`:

| Ready states | Complete source classes | Minimum final observation |
| --- | --- | --- |
| 21 generic readies | five piston-sum classes, 125 sources each | A1 |
| `(0,0)`, `(1,3)`, `(3,3)` | five piston-sum classes, 125 sources each | A2 |
| `(3,0)` | sums 2 and 4 combined, the other three separate | A1 |

The exceptional combined class has 250 sources. Across all 125 initial
quotient states, the numbers of distinct prefixes through times 0,1,2,3
are exactly **25,121,124,124**. A source function has an exact reader of
the entire apparatus history if and only if it is constant on these
classes. When it exists, the two-step prefix suffices. This covers arbitrary
nonlinear history functions and deterministic processors with arbitrary
memory and a common source-independent initial state.

Late tails carry less information for three readies. From tick 3 onward,
all sources have the same z phase and the apparatus updates are common
bijections. Tails agree exactly when A3 agrees. Each of the four exceptional
readies in the table has four tail classes; the other 21 have five. An
earlier transient distinction remains available only if its observation
was retained. A late-tail reader cannot recover it retroactively.

Every complete native source class contains different QDD LOW values.
For example the piston sources `1000` and `2400` have the same sum but
LOW weights **1/16 and 1/96**. They produce identical apparatus histories
for all 25 ready states and every common driver. Likewise `0000` and
`1400` have identical apparatus histories but different support tags.
These full native states never merge: at every step they select the same
bijective generator. This is an information boundary of the chosen port,
not loss of the distinction in the full state.

Consequently no downstream reader, output, stored record, stopping rule or
limiting frequency computed solely from that common apparatus transcript
can distinguish either pair. Supplying arbitrary processing memory does
not change that fact. Even the augmented `(z,q,r)` port fails the same-sum
witnesses, although it reveals kappa immediately. This augmented port must
not be confused with the A-only minimum-horizon classification.

## One explicit conditional preparation-to-record chain

The positive construction has four declared resources: capture and retain
the original balanced piston vector `v` before tick one; admit complete
Cartesian incidence of integer channels; acquire ordered native clock
bits; and provide fresh record cells and an archive. These are additional
observer resources. They are not derived coordinates or operations of U.

One fixed algorithm then performs the complete chain:

1. **Preparation.** Capture `v=ell(p)`, with `ell=(0,1,2,-2,-1)`. Form the
   signed channel `s=sum(v)` and five copies of each difference `vi-vj`.
   The total is 31 channel instances, with the same rule for every source.
2. **Reader.** A fixed 1024-address universe contains 64 potential LOW
   slots, 480 HIGH slots and 480 permanently empty padding slots. A channel
   of magnitude a occupies the complete `a by a` square of its channel's
   slots. A causal 2560-bit Thue-Morse window recovers the current phase
   modulo 1024 and addresses one slot. The reader receives no absolute
   counter and no numerical QDD probability.
3. **Outcome.** Each addressed occupied slot emits its single LOW or HIGH
   label; an empty slot emits SILENT. An incomplete window returns
   UNAVAILABLE, and invalid input returns ERROR. The zero source is
   ZERO_SUPPORT and produces no event.
4. **Write and read.** For an event e, a controlled cell permutation swaps
   BLANK with e and fixes the third cell symbol. The protocol requires a
   fresh BLANK cell and rejects an occupied cell. It appends the full
   record `(source_before, source_after, phase, fine_slot, sign, event,
   old_cell, written_cell)` and preserves all earlier records. A repeated
   query reads the same archive without stepping, emitting or appending.

The captured source before and after is identical. This says that the
observer retains its original source, not that native pistons stop evolving.
The first-hit query is simply the oldest accepted archive record; it is
unavailable while the archive is empty. No second sticky outcome register
is hidden in that definition. A SILENT tick appends no cell or record.

The implemented stream wrapper uses direct successive theta bits. The
alternative native checkpoint map `z_n=4-3*theta_(n-1)`, followed by phase
decoding and a +1 shift, is proved and audited in every legal generating
context. A separate end-to-end z-history record wrapper is not claimed.

The local controlled cell operation is reversible. Fresh-cell allocation
and the growing archive are explicit resources; this is not a claim that
the entire acquisition/archive protocol is a closed reversible native
system. Applying the inverse swap with its retained control can undo the
local cell write; a physical reset protocol and reusable storage supply
remain outside this result. All source/channel information is retained;
no collapse or post-measurement saturation is asserted.

## Exact frequencies and the first-outcome boundary

For `Qv=sum(v_i^2)`, complete incidence gives

```text
A = s^2,
B = 5*sum_(i<j)(vi-vj)^2,
D = A+B = 20*Qv-4*s^2.
```

The identity `sum_(i<j)(vi-vj)^2=4*Qv-s^2` proves these counts.
For every nonzero source, D is positive and at most 320. Each 1024
consecutive natural ticks contains exactly A LOW, B HIGH and D accepted
events. The accepted LOW ratio is therefore exactly

```text
A/D = s^2 / (4*(5*Qv-s^2)),
```

which equals the exposed QDD algebraic weight for all 624 supported
sources. The proof also gives exact counts for every intermediate prefix
and every fixed starting phase. No ratio is supplied to the constructor.
However, its fixed analyzer was designed using the already known QDD
formula. This is an algebraic implementation, not a blind prediction or
an independently selected physical reading.

For source `(1,0,0,0)`, A=1 and B=15. Starting at phase 0 produces LOW as
the first accepted result; starting at phase 64 produces HIGH first. The
audited starts are actual native ticks 3072 and 3136. Both subsequent
continuous runs have the same long-term accepted LOW ratio 1/16.
Observing only phase 0 each cycle gives all LOW, while observing only phase
64 gives all HIGH. Both invocation calendars have density 1/1024, and the
clock may still be acquired continuously. Thus fixed-source counting
neither fixes the first result of a new preparation nor supplies a Born
law across arbitrarily scheduled fresh preparations.

## Formal execution and custody

The preregistration, three proof files and verifier were publicly frozen
at `19b69962ba0365d39546029a3f02dd7e05e38ba5`, fetched and compared byte for
byte before the first execution. The clean Ubuntu x86_64 run completed
all six required groups with **1082026 exact comparisons, zero mismatches,
zero exit status, empty stderr and no exception**. These comparisons are
an exhaustive algebraic audit, not independent physical experiments.

Coverage includes all 15625 native states under all five generators and
both selector bits; every ordered pair of 125 quotient states; all 25
readies and all 625 piston sources; all 16384 phase-factor generating
contexts, representing 8188 distinct legal 2560-bit words; all 640000
source/address pairs; and 14336 chronological stream updates with complete
record and every-prefix count checks. The source classification preceded
the QDD target comparisons in the accepted program.

The actual stdout has 8352 bytes and SHA-256
`5d56f69ce88fff71c433903cfa95305c2c5c7e51c1db16fb7064715f7338d7ef`.
RUN.md records the public pin, every accepted file identity and the neutral
execution environment. All pinned files remained unchanged. No mathematical
falsifier fired. The two required GitHub architecture jobs must replay the
same verifier against the same committed EXPECTED bytes.

## Remaining physical obligations

The proof closes the native port's complete source-information boundary
and makes one conditional preparation-to-symbol-to-record construction
explicit. It does not derive physical source capture, Cartesian incidence,
clock acquisition, an invocation calendar, exclusive physical occurrence,
post-measurement dynamics or the availability/reset of storage from U.
The port-only negative theorem also does not exclude a different explicitly
declared coupling, apparatus split, intervention or source-bearing port.

Those changes require their own typed construction and independently
selected physical meaning. The full physical decoder and the existing
QDD-INSTRUMENT-APPARATUS, realization and calibration owners remain open.
Public Canon v78, U, prior sealed probes and all owner contracts are unchanged.
