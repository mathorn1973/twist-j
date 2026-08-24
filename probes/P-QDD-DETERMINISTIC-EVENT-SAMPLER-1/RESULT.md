# RESULT. P-QDD-DETERMINISTIC-EVENT-SAMPLER-1

```text
decision:  MECHANICAL-SAMPLER-BOUNDARY
run:       14/14 ALL PASS
exit:      0
stderr:    empty
pin:       2be3c0426791921a258e9354c4694c49d03f607a
stdout:    4e68c88fd00f2da1e5d8dc8d317795b242e7dc5aeb374824caf624f9ce61cdcf
layer:     L1 exact finite arithmetic plus one named L1 to L5 protocol
O1:        remains O
O2:        untouched
sampling:  NOT PROVIDED by the current public architecture
```

## Result first

The exact Route A weights admit a deterministic integer LOW/HIGH word once a
local apparatus invocation count, a phase origin, and a preparation update law
are frozen. This is a constructive mathematical sampler, not yet a physical O1
closure.

The current public architecture supplies none of the three load-bearing
bridges completely. Therefore the scientific decision is a boundary result:
O1 remains open.

## 1. Exact weight carrier

Complete enumeration of the 625 balanced pistons gives exactly one
`ZERO_SUPPORT` piston and 624 supported pistons. The fiber multiplicity 25
recovers the public 25 zero-support and 15600 supported checkpoint split.

The supported carrier has exactly 22 reduced LOW probabilities:

```text
0:84
1/256:24
1/176:48
1/136:32
1/96:24
1/56:48
1/46:36
1/26:48
9/224:24
1/16:56
9/104:24
2/17:24
9/64:24
5/32:8
1/6:24
2/7:24
5/16:24
3/8:16
5/8:8
9/14:12
49/64:8
1:4
```

The reduced denominator set is

```text
{1,6,7,8,14,16,17,26,32,46,56,64,96,104,136,176,224,256}.
```

The maximum denominator is 256.

## 2. Mechanical sampler

For a fixed prepared state with reduced `p_low=a/b`, the frozen lower word

```text
L_p(r)=floor((r+1)a/b)-floor(ra/b)
```

has exact cumulative count

```text
sum_(r=0)^(N-1) L_p(r)=floor(Na/b),
```

prefix discrepancy strictly below one, exactly `a` LOW outcomes in every
cyclic block of length `b`, and least period `b` for `0<a<b`. The endpoint
words are constant.

This is parameter-free after the local counter origin and lower convention are
frozen. It uses integers only and no random seed.

## 3. Phase is not selected by the weight

Every interior probability `a/b` has exactly `b` distinct cyclic phases, all
with the same exact frequency. Across the 20 interior QDD probabilities there
are 1372 such phases.

Thus the weight determines the frequency but not the event at invocation zero.
The zero-phase lower word requires an independently supplied counter origin and
rounding convention. No intrinsic-randomness conclusion follows.

## 4. Finite-memory lower bound

For a deterministic autonomous state cycle of length `L` with reduced LOW
frequency `a/b`, exact counting forces `b|L`. The QDD value `1/256`, occurring
on 24 pistons, therefore requires at least 256 persistent states in this
restricted cycle-memory class.

The binary-pointer times five-token memory register has only 10 basis labels,
so it cannot by itself realize the full QDD probability census in that
restricted memory-only class. This does not exclude use of the system carrier,
global counter, appended record, or a larger apparatus.

## 5. Global-counter schedule no-go

A local invocation counter is invariant under arbitrary gaps in the public
global counter: the `j`-th apparatus call uses `L_p(j)` regardless of when it
occurs.

Replacing the local count by the global tick is not schedule invariant. The
LOW-position subsequence yields all LOW and the HIGH-position subsequence yields
all HIGH for every nonconstant periodic word. A physical admissible schedule
or a local invocation-count bridge must therefore be supplied separately.

Public Canon v59 provides neither a writeback from decoder history into the
autonomous update nor a registered bridge turning terminal functional order
into apparatus invocation memory.

## 6. Changing preparations need a law

For the carried exact accumulator

```text
x_(j+1)=x_j+p_j-e_j,
e_j=1 iff x_j+p_j>=1,
```

all `22^3` ordered triples obey

```text
sum e_j=floor(sum p_j).
```

But order changes the realized word. The same multiset

```text
{1/256,2/7,49/64}
```

gives

```text
(1/256,49/64,2/7) -> H,H,L,
(49/64,2/7,1/256) -> H,L,H,
```

with the same final residual `99/1792`. A changing-preparation protocol must
therefore freeze reset, carry, or state-update semantics.

## Candidate theorem ceiling

After byte-identical public x86_64 and aarch64 replay, a later separate Canon
fold may register at most:

```text
QDD-WEIGHT-DENOMINATOR-CENSUS            [T]
QDD-MECHANICAL-EVENT-SAMPLER             [T]
QDD-EVENT-PHASE-NONSELECTION             [T]
QDD-EVENT-FINITE-MEMORY-LOWER-BOUND      [T]
QDD-GLOBAL-COUNTER-SCHEDULE-NOGO         [T]
QDD-EVENT-COUNTER-ARCHITECTURE-BOUNDARY  [T]
QDD-EVENT-PREPARATION-ORDER-BOUNDARY     [T]
```

The universal statements rest on the written proofs; the verifier is an exact
finite audit.

## Scope firewall

No O2 result. No L6 measure. No randomness or independence theorem. No Bell,
locality, no-signalling, causal, SI, force, or decoder-completion statement. No
claim that the 10-label register exhausts all possible apparatus
architectures. No current-Canon status moves.
