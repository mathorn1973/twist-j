# Born quartet witness

The Born quartet in the read place residual algebra A_8 = Z[zeta_8]/5
= F_5[X]/(X^4 + 1), with the Born involution star: X -> X^7 and the
Born norm N_B(a) = a star(a). Exact integer arithmetic throughout; no
positivity is claimed in the finite read.

Verified: the Born unit group is cyclic of order 24 with zeta_8 of
order 8; the half angle identity (1 + u)^2 = u N_B(1 + u) holds on
every Born unit; the bisector norm has a star fixed square root
exactly on the squares of the unit group (12 of 24, the norm gate),
and the normalized bisector H = (1 + u)/r with H^2 = u and
N_B(H) = 1 exists exactly on the 11 non antipodal gated units: at
u = -1 the bisector vanishes and the only square root of its norm
is 0, not invertible, so normalization is undefined there; zeta_8
is ungated, so its halving forces the quadratic step. The residual splits: x^4 + 1 =
(x^2 + 2)(x^2 + 3) mod 5 with inversion swapping the factors, and
x^2 + 1 = (x - 2)(x - 3) mod 5 with conjugation swapping the roots.
The quarter turn spinor: det(1 - B) = 2 and (1 - B)^2 = -2 B over Z,
and R = (1 - B)/sqrt2 is an order 8 element of SL_2(F_25) with
R^2 = -B. The staircase: root orders 4, 8, 16 are first realized at
F_5, F_25, F_625 (two quadratic steps), with minimality checked
against every smaller degree (16 divides none of 4, 24, 124),
explicit witnesses, and irreducibility checked exhaustively.

Evidence for registry claims BORN-HALF-ANGLE, BORN-RESIDUAL-SPLIT,
SPIN-BISECTOR, BORN-ORDER-STAIRCASE.

Run from the repository root:

```
python3 reproduce/born-quartet/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 11/11 ALL PASS,
exit 0, no stderr.
