# Color ladder witness

The eleven-rung ladder from the recurrent D5 return group to the
integral binary-icosahedral color core, reproduced in exact arithmetic.
The verifier uses integers, rationals, Q(sqrt5) pairs, finite fields,
cyclotomic coefficient tuples, exact character tables, and exact
polynomial arithmetic. It uses the Python standard library only, with
no floats, random choices, timestamps, or external data.

Rung 3 is deliberately split. The registered dynamical-color
falsifier fires: the special-linear image of the dynamical census
symmetries is only Z_2. The kinematical product-affine normalizer then
closes on 40 x 480 = 19200 exact census symmetries, with special-linear
image GL_2(F_5) of order 480 along the 3 = 1 + 2 split. This is a
boundary of the result, not a defect hidden by the harness.

The remaining blocks verify the binary icosahedral core SL_2(F_5), its
class equation and ramified trace table; the full golden character
table, dicyclic loop lift, readouts, and Brauer shadow; affine E8 under
tensoring with the spin row, the Catalan bridge and the first finite
deviation 133 = 132 + 1; the rational moment fingerprint and Lucas
formula; the spectral class measure and the invariant degrees
(12, 20, 30) with one relation at 60; the Dickson pair and the free
modular degrees (6, 20); Klein's integer relation and its
Artin-Schreier shadow; and the integral two-generator lift whose
reduction is bijective onto SL_2(F_5).

Evidence map:

- 01: COLOR-RETURN-D5 and the first leg of COLOR-MEASURE-TRANSPORT.
- 02: COLOR-TORSOR-HOLONOMY and COLOR-SPLIT-12.
- 03: COLOR-DYNAMICAL-NOGO, with the registered falsifier fired.
- 04: COLOR-KIN-NORMALIZER and COLOR-KINEMATICAL-GL2.
- 05: COLOR-CORE-2I.
- 06: COLOR-GOLDEN-TABLE.
- 07: COLOR-MCKAY-E8 and COLOR-MEASURE-TRANSPORT.
- 08: COLOR-MOMENT-FINGERPRINT.
- 09: COLOR-SPECTRAL-INVARIANTS and COLOR-MEASURE-TRANSPORT.
- 10: COLOR-DICKSON-RAMIFICATION.
- 11: COLOR-KLEIN-REDUCTION.
- 12: COLOR-INTEGRAL-LIFT.

Run from the repository root:

```
python3 reproduce/color-ladder/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 12/12 ALL PASS,
exit 0, no stderr.
