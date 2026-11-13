#!/usr/bin/env python3
# check_arrow_in_modulus.py
# Exact arithmetic in Z[zeta_5], basis 1, j, j^2, j^3, j^4 = -(1+j+j^2+j^3).
# Standard library only. No float anywhere. Every assertion is an integer identity.
# Companion of notes/ARROW-IN-MODULUS-2026-10-23/NOTE-ARROW-IN-MODULUS-2026-10-23-CZ.md
# (NON-CANONICAL). Run from the repository root:
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
#   python3 notes/ARROW-IN-MODULUS-2026-10-23/check_arrow_in_modulus.py

def red(v):
    v = list(v) + [0] * (5 - len(v)); a = v[4]
    return [v[0] - a, v[1] - a, v[2] - a, v[3] - a]

def mul(x, y):
    r = [0] * 5
    for i in range(4):
        for k in range(4):
            r[(i + k) % 5] += x[i] * y[k]
    return red(r)

def sigma(x, a):            # Galois: j -> j^a
    r = [0] * 5
    for i in range(4):
        r[(i * a) % 5] += x[i]
    return red(r)

def pw(x, n):
    P = [1, 0, 0, 0]
    for _ in range(n):
        P = mul(P, x)
    return P

def ordmod(x, m, cap=10 ** 6):
    P = [1, 0, 0, 0]; n = 0
    while True:
        P = [c % m for c in mul(P, x)]; n += 1
        if P == [1 % m, 0, 0, 0] or n > cap:
            return n

ONE = [1, 0, 0, 0]; j = [0, 1, 0, 0]
J = [1, 0, 1, 0]                # 1 + j^2
JINV = [0, -1, -1, 0]           # -j - j^2
PHI = [0, 0, -1, -1]            # -j^2 - j^3
MU10 = [[s * c for c in pw(j, k)] for s in (1, -1) for k in range(5)]

fails = 0
def check(name, ok):
    global fails
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails += 1

print("== A  the inverse step")
check("A1 J * J^-1 = 1", mul(J, JINV) == ONE)
check("A2 J^-1 = phi * conj(j)", mul(PHI, sigma(j, 4)) == JINV)
check("A3 J^-1 = phi^2 * conj(J)", mul(pw(PHI, 2), sigma(J, 4)) == JINV)
check("A4 J * phi = j", mul(J, PHI) == j)
check("A5 J^5 * phi^5 = 1", mul(pw(J, 5), pw(PHI, 5)) == ONE)

print("== B  Galois and the inverse")
for a in (1, 2, 3, 4):
    check("B1 sigma_%d(J) != J^-1" % a, sigma(J, a) != JINV)
tors = {}
for a in (1, 2, 3, 4):
    q = mul(JINV, sigma(JINV, a))          # J^-1 / sigma_a(J)
    tors[a] = q in MU10
    print("   a=%d  J^-1 / sigma_a(J) = %s  in mu_10: %s" % (a, q, tors[a]))
check("B2 inversion up to torsion exactly for the place swap a in {2,3}",
      tors == {1: False, 2: True, 3: True, 4: False})
check("B3 J^-1 / sigma_2(J) = -j^2 = zeta_10^-1", mul(JINV, sigma(JINV, 2)) == [0, 0, -1, 0])
check("B4 J^-1 / sigma_3(J) = -j = zeta_10^-3", mul(JINV, sigma(JINV, 3)) == [0, -1, 0, 0])
check("B5 J^-1 / sigma_4(J) = phi^2 (not torsion)", mul(JINV, sigma(JINV, 4)) == pw(PHI, 2))
check("B6 sigma_2 o sigma_2 = sigma_4 on J", sigma(sigma(J, 2), 2) == sigma(J, 4))
check("B7 the only Galois element of order 2 (sigma_4) does not invert J up to torsion",
      not tors[4])
# B8: no linear conjugacy at all (the trace argument of C-J-U-D-ARROW-LOCALITY-N, U2).
# Trace of multiplication by x on the Z-basis 1, j, j^2, j^3 equals Tr_(K/Q)(x);
# Tr(j^k) = -1 for k = 1..4 and Tr(1) = 4.
def trace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]
check("B8 Tr(J) = 3 and Tr(J^-1) = 2, so M_J and M_J^-1 are not conjugate in GL_4(Q)",
      trace(J) == 3 and trace(JINV) == 2)

print("== C  closed world: J periodic modulo rational m, ord_m(J) = lcm(5, ord_m(phi))")
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
allok = True
for m in (2, 3, 4, 5, 7, 11, 13):
    oJ, oP = ordmod(J, m), ordmod(PHI, m)
    ok = (oJ == lcm(5, oP))
    allok &= ok
    print("   m=%2d  ord(J)=%3d  ord(phi)=%3d  lcm(5,ord phi)=%3d  %s" % (m, oJ, oP, lcm(5, oP), ok))
check("C1 residue period law holds for m in {2,3,4,5,7,11,13}", allok)

print("== D  integer size runs away in both time directions (no arrow in coefficient size)")
F = [0, 1]
while len(F) < 40: F.append(F[-1] + F[-2])
allok = True
for n in (5, 10, 15, 20):
    f = max(map(abs, pw(J, n))); b = max(map(abs, pw(JINV, n)))
    ok = (f == F[n + 1] and b == F[n])
    allok &= ok
    print("   n=%2d  |J^n|_inf=%5d  |J^-n|_inf=%5d  (F_%d, F_%d)  %s" % (n, f, b, n + 1, n, ok))
check("D1 |J^n|_inf = F_(n+1), |J^-n|_inf = F_n for n in {5,10,15,20}: same rate phi both ways", allok)

print("ALL PASS" if fails == 0 else "FAILURES: %d" % fails)
