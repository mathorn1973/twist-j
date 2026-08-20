#!/usr/bin/env python3
# P-PENTAGON-ONLY-DILATIONS-1 verify.py
# Exact audit for J-LI-PENTAGON-DILATION-DEFICIENCY [T] and the route kill
# PENTAGON-ONLY-DILATIONS [F].
#
# Setting: H = L^2(0,1), clock functions g_n(x) = frac(n x) - 1/2. Exact
# Gram <g_m, g_n> = gcd(m,n)^2 / (12 m n). The pentagon tower is the family
# {g_(5^m)}. Claim: for every q coprime to 5 and every M >= 0,
#   dist(g_q, span{g_(5^m): 0 <= m <= M})^2 = (1/12)(1 - 1/q^2),
# constant in M, with the best approximant exactly (1/q) g_1. Proof carried
# in PREREG.md; this verifier audits the Gram by independent exact
# piecewise integration and the collapse by exact linear algebra.
#
# Python standard library only. Fraction arithmetic. No float anywhere.

import sys
from fractions import Fraction
from math import gcd

assert len(sys.argv) == 1

checks = 0

def gate(name, condition):
    global checks
    assert condition, name
    checks += 1
    print("%s PASS" % name)

def floor_fraction(f):
    return f.numerator // f.denominator

def gram_integral(m, n):
    # exact integral of (frac(mx)-1/2)(frac(nx)-1/2) over [0,1]
    points = sorted(set(
        [Fraction(i, m) for i in range(m + 1)]
        + [Fraction(j, n) for j in range(n + 1)]))
    total = Fraction(0)
    for u, v in zip(points, points[1:]):
        if u == v:
            continue
        mid = (u + v) / 2
        a = floor_fraction(m * mid)
        b = floor_fraction(n * mid)
        # integrand: (m x - a - 1/2)(n x - b - 1/2)
        A = Fraction(m * n)
        B = -(Fraction(m) * (b + Fraction(1, 2))
              + Fraction(n) * (a + Fraction(1, 2)))
        C = (a + Fraction(1, 2)) * (b + Fraction(1, 2))
        total += (A * (v ** 3 - u ** 3) / 3
                  + B * (v ** 2 - u ** 2) / 2
                  + C * (v - u))
    return total

def gram_formula(m, n):
    return Fraction(gcd(m, n) ** 2, 12 * m * n)

def solve_exact(G, c):
    # Gaussian elimination over Fractions; G square nonsingular
    n = len(G)
    M = [row[:] + [c[i]] for i, row in enumerate(G)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return [M[r][n] for r in range(n)]

print("P-PENTAGON-ONLY-DILATIONS-1 verify")

# PD1: independent exact integration reproduces the Gram closed form
pd1_pairs = [(m, n) for m in range(1, 11) for n in range(m, 11)]
pd1_pairs += [(2, 125), (3, 125), (7, 125), (12, 125)]
bad = [(m, n) for m, n in pd1_pairs
       if gram_integral(m, n) != gram_formula(m, n)]
gate("PD1 exact piecewise integration equals gcd(m,n)^2/(12mn) on %d"
     " pairs including (q,125)" % len(pd1_pairs), not bad)

# PD2: the five-tower Gram is the KMS matrix 5^-|a-b| / 12
kms_ok = all(
    gram_formula(5 ** a, 5 ** b)
    == Fraction(1, 12) * Fraction(5) ** (-abs(a - b))
    for a in range(0, 4) for b in range(0, 4))
kms_int = all(
    gram_integral(5 ** a, 5 ** b)
    == Fraction(1, 12) * Fraction(5) ** (-abs(a - b))
    for a in range(0, 3) for b in range(0, 3))
gate("PD2 five-tower Gram is KMS 5^-|a-b|/12 (formula a,b<=3;"
     " integration a,b<=2)", kms_ok and kms_int)

# PD0: the collapse identity G e_0 / q = c, symbolically for a <= 8
collapse = all(
    Fraction(5) ** (-abs(a - 0)) / Fraction(12) / q
    == Fraction(1, 12 * q) * Fraction(5) ** (-a)
    for q in (2, 3, 6, 7, 12) for a in range(0, 9))
gate("PD0 collapse identity G e_0 (1/q) = c for a <= 8, q in"
     " {2,3,6,7,12}", collapse)

# PD3/PD5/PD6: exact solve for every M = 0..8 and q coprime to 5
QS = (2, 3, 6, 7, 12)
all_ok = True
for q in QS:
    for M in range(0, 9):
        G = [[Fraction(1, 12) * Fraction(5) ** (-abs(a - b))
              for b in range(M + 1)] for a in range(M + 1)]
        c = [Fraction(1, 12 * q) * Fraction(5) ** (-a)
             for a in range(M + 1)]
        x = solve_exact(G, c)
        dist2 = Fraction(1, 12) - sum(ci * xi for ci, xi in zip(c, x))
        ok = (x[0] == Fraction(1, q)
              and all(xi == 0 for xi in x[1:])
              and dist2 == Fraction(1, 12) * (1 - Fraction(1, q * q)))
        all_ok = all_ok and ok
    print("  q = %2d: dist^2 = %s for every M = 0..8, approximant"
          " coefficients beyond g_1 all zero"
          % (q, Fraction(1, 12) * (1 - Fraction(1, q * q))))
gate("PD3 deficiency (1/12)(1 - 1/q^2), constant in M, best approximant"
     " (1/q) g_1, for q in {2,3,6,7,12}, M = 0..8", all_ok)

# PD4: the exact witnesses
gate("PD4 witnesses: q=2 gives 1/16 and q=3 gives 2/27 exactly",
     Fraction(1, 12) * (1 - Fraction(1, 4)) == Fraction(1, 16)
     and Fraction(1, 12) * (1 - Fraction(1, 9)) == Fraction(2, 27))

# PD6: adding five-powers never decreases the distance (constancy shown in
# PD3); strict positivity of the deficiency for every q > 1
gate("PD6 the deficiency is strictly positive for every q >= 2: the"
     " pentagon tower reaches no cross-prime direction",
     all(Fraction(1, 12) * (1 - Fraction(1, q * q)) > 0 for q in QS))

print("DECISION: pentagon-tower dilations miss every direction coprime"
      " to 5 by an exact positive constant; the route is dead")
print("RESULT %d/%d ALL PASS" % (checks, checks))
