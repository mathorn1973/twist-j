#!/usr/bin/env python3
"""referee_m37_strength.py -- exact finite checks for REFEREE-C-M37-STRENGTH.md.

NON-CANONICAL. Python 3 standard library only; int and fractions.Fraction only.
No floating point anywhere. Deterministic. Run from a clean shell with
    LC_ALL=C PYTHONHASHSEED=0 python3 referee_m37_strength.py
Exit status 0 iff every check passes.
"""
from fractions import Fraction as Fr
import sys

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "REF-CHECK %02d %s: %s" % (len(RESULTS), "PASS" if ok else "FAIL", name)
    if detail:
        line += " [" + detail + "]"
    print(line)


ORD = 12


def ps(c):
    a = [Fr(0)] * (ORD + 1)
    for i, x in enumerate(c[: ORD + 1]):
        a[i] = Fr(x)
    return a


def mul(a, b):
    c = [Fr(0)] * (ORD + 1)
    for i in range(ORD + 1):
        for j in range(ORD + 1 - i):
            c[i + j] += a[i] * b[j]
    return c


def inv(a):
    b = [Fr(0)] * (ORD + 1)
    b[0] = 1 / a[0]
    for n in range(1, ORD + 1):
        b[n] = -sum(a[i] * b[n - i] for i in range(1, n + 1)) / a[0]
    return b


one_m_x = ps([1, -1])
one_m_2x = ps([1, -2])
inv1mx2 = mul(inv(one_m_x), inv(one_m_x))
G_free = mul(one_m_2x, inv1mx2)          # lane's local factor at split p not | k: (1-2x)/(1-x)^2
G_k = inv1mx2                            # lane's local factor at split p | k: 1/(1-x)^2
ratio = mul(G_k, inv(G_free))            # G_{k,p}/G_{1,p}
lane_formula = mul(mul(one_m_x, one_m_x), inv(one_m_2x))   # lane's displayed (1-x)^2/(1-2x)
correct = inv(one_m_2x)                  # 1/(1-2x)

# REF-CHECK 01: the residue k-factor ratio is 1/(1-2x), and is NOT the lane's (1-x)^2/(1-2x)
check("G_{k,p}/G_{1,p} = 1/(1-2x) as formal series to x^%d, and differs from the lane's (1-x)^2/(1-2x)" % ORD,
      ratio == correct and ratio != lane_formula,
      "ratio coefficients " + ",".join(str(c) for c in ratio[:5]) + ",...; lane's " + ",".join(str(c) for c in lane_formula[:5]) + ",...")

# REF-CHECK 02: numerical instance at p = 11, s = 2 (x = 1/121), exact rationals
X = Fr(1, 121)
true_ratio = (1 / (1 - X) ** 2) / ((1 - 2 * X) / (1 - X) ** 2)
check("at p=11, s=2: G_k/G_1 = 121/119 = 1/(1-2x); lane's formula gives 14400/14399",
      true_ratio == Fr(121, 119) and true_ratio == 1 / (1 - 2 * X) and (1 - X) ** 2 / (1 - 2 * X) == Fr(14400, 14399),
      "true %s, lane %s" % (true_ratio, (1 - X) ** 2 / (1 - 2 * X)))

# REF-CHECK 03: nu_sigma, a_sigma, b_sigma against (A39)-(A40) at sigma = 51/200; beta_pole values
s = Fr(51, 200)
a = (2860 * s - 169) / 9578
b = (1261 - 2860 * s) / 3528
b1 = Fr(13, 194) - Fr(1430, 4789) * ((1 - s) - Fr(139, 194))      # (A39) second segment at u = 1 - sigma
b0 = Fr(13, 84) - Fr(715, 1764) * (2 * s - Fr(1, 2))              # (A39) first segment at u = 2 sigma
nu = a + b
ok3 = (a == Fr(5603, 95780) and b == Fr(5317, 35280) and b1 == a and b0 == b
       and nu == Fr(7069361, 33791184) and 2 * nu < 1
       and 1 - nu / (2 - Fr(99, 100)) == Fr(676493371, 853227396)
       and 1 - nu / 2 == Fr(60513007, 67582368))
check("a_sigma = b_1(1-sigma) = 5603/95780, b_sigma = b_0(2 sigma) = 5317/35280, nu = 7069361/33791184, beta_pole values as quoted",
      ok3, "2nu = %s" % (2 * nu))

# REF-CHECK 04: beta*(kappa) is exactly where sup_t |Pi_rho| = |R| U^{beta-sigma}/b meets T_0 = U^{1-sigma} T^{-1/2}
ok4 = True
for k in (Fr(0), Fr(1, 2), Fr(49, 50), Fr(99, 100), Fr(1)):
    eU = 2 - k                       # U = T^{eU}
    beta_sup = 1 - Fr(1, 2) / eU     # eU*(beta - 1) = -1/2
    ok4 = ok4 and beta_sup == (3 - 2 * k) / (4 - 2 * k)
check("sup-versus-L2 reading: U^{beta-1} = T^{-1/2} at U = T^{2-kappa} iff beta = (3-2kappa)/(4-2kappa), kappa in {0,1/2,49/50,99/100,1}", ok4)

# REF-CHECK 05: (P7) at x and x/2 needs x >= 1.6e10, not 8e9; (P8) is printed for Y >= 10^12
x_min_P7 = 2 * 8 * 10 ** 9
check("(P7) at both endpoints of (x/2, x] requires x >= 1.6e10 (lane wrote 8e9); (P8) as printed needs Y >= 10^12",
      x_min_P7 == 16 * 10 ** 9 and x_min_P7 > 8 * 10 ** 9 and 10 ** 12 > x_min_P7, "x >= %d" % x_min_P7)

npass = sum(RESULTS)
print("CHECKS: %d of %d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
