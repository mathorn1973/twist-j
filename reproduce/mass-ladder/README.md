# Mass ladder witness

The mass ladder theorem layer and the parity law, in exact
arithmetic: integers, rationals, Q(sqrt5) pairs, and formal Laurent
monomial rings over Q. No floats anywhere; pi is a formal symbol and
no transcendental number is evaluated. The sigma comparisons of the
ladder against measurement are fenced witnesses in the Canon text and
are deliberately outside this file: no value is claimed beyond the
committed forms.

Verified: the shared coefficient C = 89/5 = 18 - 1/p with
matter_spatial 18 = (1/2)(12)(3) and 240 C = 4272 an integer; the
exact exchange identity delta mu_tau + 240 delta mu_mu = 0 in Q; the
committed forms mu_mu = 2688/13 - C alpha^2, mu_tau = 3477 +
240 C alpha^2, mu_p = 6 pi^5 (1 + alpha^2/3), and mu_n = mu_p +
deg_v/chi - Delta_EM with Delta_EM open on the frontier; the proton
as the homogeneous odd pi^5 carrier and the neutron as the unique
mixed parity composite; the exact bridges xi phi^2 = 5 = p,
script-Q phi^2 = 2 pi, script-Q/xi = 2 pi/5 = arg J in Q(sqrt5); the
algebraic side of the bridge defect (6 phi^2 = 9 + 3 sqrt5, a root of
the irreducible x^2 - 18x + 36, so delta = 6 phi^2 - 5 pi is nonzero
by Lindemann-Weierstrass); and the parity law under the formal
pi-grading involution iota_pi, which fixes all other generators and
sends pi to -pi, on thirteen named even register entries, three odd
delta carriers at pi degrees 1, 3, 5, and the mixed neutron. This
formal grading is not ordinary complex conjugation, and no larger
census is claimed.

Evidence for registry claims MU-TAU-COEFFICIENT,
MU-EXCHANGE-IDENTITY, MASS-LADDER-FORMS, PARITY-LAW, BRIDGE-DEFECT.
Check map: 01 MU-TAU-COEFFICIENT; 02 MU-EXCHANGE-IDENTITY; 03 to 05
MASS-LADDER-FORMS; 06 and 07 BRIDGE-DEFECT; 08 PARITY-LAW.

Run from the repository root:

```
python3 reproduce/mass-ladder/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 8/8 ALL PASS,
exit 0, no stderr.
