# Gravity chain witness

The closed gravity chain at the equation layer, in exact arithmetic:
integers, rationals, Q(sqrt5) pairs, the cyclotomic ring Z[zeta_5],
and formal Laurent monomial rings over Q. No floats anywhere; pi is
carried as a formal symbol and no transcendental number is evaluated.

Verified: the modulus chord J Jbar = 2 - phi = phi^-2 exactly in
Z[zeta_5] with N(J) = 1; the Kahler jet h(t) = phi^2/(1 + t) with
order 0 jet phi^2 and the capacity monomial V_geo = (4 pi)^3 phi^2 =
64 pi^3 phi^2, the odd pi^3 carrier of the parity law; the rank 1
lapse action closing the FRW (00) constraint algebra exactly (the
lapse variation gives 3 H^2 = lambda rho, lambda = 216 pi gives
H^2 = 72 pi rho, the coefficient 3 = C(3, 2) counts the spatial
2-planes, the Euler-Lagrange chain gives the second Friedmann
equation, and the Hamiltonian constraint takes the canonical form);
the forced fiber multiplier k_f = 1 from the master closure against
G_nat = 27 = d^3 with V_cell = 2 (d+1)^2 d^3 pi = 864 pi carrying
exactly one fiber 2 pi; the fiber circle J = zeta (zeta + zeta^4)
with zeta + zeta^4 = phi - 1 > 0; and the equation layer of the SI
bridge: alpha B g = 1 identically, g = 2^5 phi^2 sqrt(3 - phi)
carried through its exact square g^2 = 1024 phi^4 (3 - phi) with
3 - phi = |1 - zeta_5|^2, the geometric factor (32/33)^2 =
(2^5/(2^5 + 1))^2, and the wall spelling ell_P / lambda_e =
(32/33) alpha^10 / sqrt(g) squared onto 27 (ell_G/lambda_e)^2 = G_T.
The SI value of Newton's constant is not claimed here; it stays on
the metrology frontier.

Evidence for registry claims KAHLER-CAPACITY, FRW-CANONICAL-FORM,
GRAVITY-BRIDGE-LAW. Check map: 01 to 03 KAHLER-CAPACITY; 04 to 10
FRW-CANONICAL-FORM; 11 and 12 GRAVITY-BRIDGE-LAW.

Run from the repository root:

```
python3 reproduce/gravity-chain/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 12/12 ALL PASS,
exit 0, no stderr.
