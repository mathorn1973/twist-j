# Coupling and metrology arc witness

The coupling and metrology arc at the exact layer, in exact
arithmetic: integers, rationals, and polynomial or Laurent monomial
rings over Q. No floats anywhere. The unsupported WKB3 ringdown grade
and numerical mu corridor are outside Public Canon v1; the 72 alpha^4
dressing value remains a labeled witness.

Verified: the TT decoder as the complex squaring map h_+ + i h_x =
(v1 + i v2)^2 with kernel exactly {+-1}, the spin double cover, with
|h|^2 = (v1^2 + v2^2)^2 and volume neutrality det(I + H) = 1 - |h|^2
exactly; the one propagation law c = 1 - s^2 on the integer triple
(+1, 0, -3); the Schwarzschild TT endpoint V_s = f (L/r^2 +
2M(1 - s^2)/r^3) with the forced coefficient -6 = 2(1 - 4) at s = 2;
the Stage B bookkeeping inputs mu = 1 and Z_L2 = 1/2, without an
action-germ, Gaussian-state, or Stage B pullback derivation; the density against the
Galois Gram G = p I - 1 1^T with trace exactly 1 and the Born value the
branch G norm, without an instrument-uniqueness claim; the DeWitt dressing
d(1 - lambda d) = 12 = d(d + 1) at lambda = -1, the chain of twelves;
the dimensionless tick clause 1/5 cycle = 2 pi/5 per tick, without a
metrological-admissibility theorem; and the
coupling seeds 3/4 = d/(d + 1) on the spatial base with the EM to
strong seed ratio 15 : 4 exactly.

Evidence for registry claims TT-SQUARING-DECODER,
SCHWARZSCHILD-TT-ENDPOINT, TT-QUADRATIC-GERM, COUPLINGS-DETERMINE,
DEWITT-TWELVES, METRO-TICK, MEASURE-SPATIAL-ONLY, STRONG-SEED. Check
map: 01 and 02 TT-SQUARING-DECODER; 03
SCHWARZSCHILD-TT-ENDPOINT; 04 TT-QUADRATIC-GERM; 05
COUPLINGS-DETERMINE; 06 DEWITT-TWELVES; 07 METRO-TICK; 08
MEASURE-SPATIAL-ONLY and STRONG-SEED.

Run from the repository root:

```
python3 reproduce/coupling-metrology/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 8/8 ALL PASS,
exit 0, no stderr.
