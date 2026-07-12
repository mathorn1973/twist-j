# Dirac ladder witness

The closed Dirac ladder of the electron, its checkerboard, and its
alternator base, in exact arithmetic: integers, rationals, Q(sqrt5)
pairs, Gaussian integers, and Laurent polynomials over Z[i]. No floats
anywhere; standard library only.

Verified: the light cone pair u = 2 phi^n, v = 2 phi^-n with u v = 4
exactly and the Pell parity L^2 - 5 F^2 = 4 (-1)^n; the spinor floor
N(phi) = -1 with even rungs halving and odd rungs obstructed
(x^4 - x^2 - 1 irreducible over Q, phi^3 = 2 + sqrt5 not a square in
Q(sqrt5)); the ladder root Fm with Fm^2 the cat map, Z conjugate to
the modulus carrier, the mod 5 towers of order 20 = 4p and 10 = 2p
with -I at half period, the single Jordan block J_4(2) of the
J-carrier and an explicit 1-jet conjugacy; the Dirac step
D_J(m)(z) = S(z)(I + i m X) with coefficient set {1, i m}, the mass
free trace, the momentum free determinant 1 + m^2 (electron 5 = p),
the exact mass shell Ehat^2 - phat^2 = m^2, and the unitarized rest
coin of infinite order; the distinct place attached involutions chi5
(conductor 5) and chi8 (conductor 8) with charge conjugation as the
Gaussian place swap above 5; the checkerboard skeleton (one binomial
pair per case) resumming to the Gaussian tower (1 + 2i)^n with
c^2 + d^2 = 5^n and the zone edges -5I and -I; the fermionizer
Phi_f(s) = 1 - 2^(1-s) with eta(-5) = 1/4; the beat STEP = B_J A with
A^2 = I; and the Thue-Morse breath tower.

Evidence for registry claims DIRAC-LADDER, LADDER-LIGHTCONE,
SPINOR-FLOOR, FIB-ROOT-TIES, FIB-ROOT-CARRIER, DIRAC-STEP-THEOREMS,
DIRAC-STEP, LADDER-SPIN-PLACES, CHECKERBOARD-GAUSS-TOWER, FERMIONIZER,
LADDER-ALTERNATOR-BASIS, TM-BREATH-TOWER. Check map: 01
LADDER-LIGHTCONE; 02 SPINOR-FLOOR; 03 to 05 FIB-ROOT-TIES and
FIB-ROOT-CARRIER; 06 DIRAC-STEP; 07 to 09 DIRAC-STEP-THEOREMS; 10 and
11 LADDER-SPIN-PLACES; 12 and 13 CHECKERBOARD-GAUSS-TOWER; 14
FERMIONIZER; 15 LADDER-ALTERNATOR-BASIS; 16 TM-BREATH-TOWER; checks 01
to 13 together witness the DIRAC-LADDER dictionary closure.

Run from the repository root:

```
python3 reproduce/dirac-ladder/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 16/16 ALL PASS,
exit 0, no stderr.
