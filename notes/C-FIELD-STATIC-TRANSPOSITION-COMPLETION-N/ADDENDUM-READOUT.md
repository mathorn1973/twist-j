# Pre-execution addendum: ambiguity survives F-commutation

Status: **NON-CANONICAL, conditional candidate-T, L1.** This is an additive
pre-execution claim T7. PREREG.md remains unchanged. No new or uploaded
scientific program has been run. These two histories were derived by hand
after the first specification freeze and before the joint source-code pin.
This addendum will be included in that joint pin and in both exact audits.
It changes none of T1-T6, their domains, or their failure thresholds.

Use all definitions and the S01/S12 laws in PREREG.md. A complete two-cell
state is (source,receiver,eta,p). The inherited step T first applies G to
both cells and writes the receiver event e in p modulo5, then swaps source
stock with eta (A), then eta with receiver stock (B), and finally applies F
to both cells. All frozen examples have zero source matter and fields, so
its G and F are identities and its reaction event is zero. Define

```text
T01 = S01_receiver after T
T12 = S12_receiver after T.
```

The contacts leave eta and p unchanged. Both complete laws are bijective and
preserve the chosen total energy. Fix the same final old-carrier state Y:

```text
source: zero matter, zero b, E=0, M=0, r=0
receiver: m=R, b=(5v,0,-5v), E=(2,2,1,-4), M=0, r=81
eta=0, p=0, v=(1,0,0,0).
```

The receiver energy is 424. The cell and link energy is therefore 424, or
425 including the same pointer energy 1 used in SOURCE_SELECTION.md of
PR #1424. Both histories keep p=0 throughout, so no assumption about other
pointer energy values is needed by this witness.

Freeze the following initial states, with zero source nonstock coordinates,
eta=0 and p=0 in each:

| Quantity | Input X01 for T01 | Input X12 for T12 |
|---|---|---|
| source stock and energy | 81 | 86 |
| receiver matter | AM | AM |
| receiver b | (0,5v,-5v) | (5v,-5v,0) |
| receiver E | (-2,0,2,-3) | (1,3,1,1) |
| receiver M | (0,0) | (0,0) |
| receiver r | 6 | 6 |
| receiver active y | (-1,0,0,0) | (-1,0,0,0) |
| receiver static sigma | (-1,2) | (2,1) |
| receiver H1 | 343 | 338 |

In both cases H(y)=2 and the AM guard is exactly `6+2-4*2=0`.
G is genuinely accepted and writes e=0. After G the receiver has matter R,
stock 0 and M=(0,-5), with E=(-5,0,5,0) or (-2,3,4,4), respectively.
After A and B, source stock and eta are zero and receiver stock is 81 or 86.
F then gives the following pre-contact states:

```text
01: b=(0,5v,-5v), E=(0,0,0,-5), M=0, r=81
12: b=(5v,-5v,0), E=(3,3,-1,-1), M=0, r=86.
```

They are exactly S01(Y_receiver) and S12(Y_receiver). In the forward final
contact, S01 has price 0 and S12 price +5. Both pass the full admission guard
and produce Y_receiver. Thus `T01(X01)=Y=T12(X12)` as complete old states.
The last receiver energy changes are `424-343=81` and `424-338=86`.

T7. On the union of these two admitted histories there is no exact function
of the final old-carrier state that reads the last receiver energy change
without contact context, even though both completed contacts commute with
G and F. Any real-valued common estimate has worst-case absolute error at
least 5/2 on this pair. One additional distinguishable binary context label
is necessary for this pair and sufficient for the explicitly controlled
two-law family, if it is retained and available to the inverse reader.
This is an abstract code; physical preparation and readable implementation
remain assumptions, and the complete expanded states include the label.

Both programs must evaluate the two full forward histories, all stated
intermediate tuples and energy balances, and exact equality to the same Y.
One differing coordinate, energy or branch outcome fires T7. No finite
enumeration or optimization is needed for this exact two-history witness.
The general impossibility proof is simply that a function cannot take both
values 81 and 86 on the identical argument Y; it is not a finite-to-infinite
inference. Physical source selection and the original fired claims remain
unchanged.
