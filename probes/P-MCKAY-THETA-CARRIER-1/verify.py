#!/usr/bin/env python3
# P-MCKAY-THETA-CARRIER-1 verifier. See PREREG.md (the pinned preregistration).
# Stdlib only, exact rational arithmetic,
# no float in any assertion. Decimal prints are labeled witnesses only.
#
# Gates G1..G7 of the prereg. Imports consumed: W-RVM weakened form
# (E(T) = (1/2) log T + (1/2) loglog T + 5, T >= 3), PI enclosure at 15
# digits, Theta_{E8} = E4 witnessed on shells n = 1, 2, 3 by enumeration.
from fractions import Fraction as F
from itertools import product

PI_LO = F(3141592653589793, 10**15)
PI_HI = F(3141592653589794, 10**15)
K_SER = 40  # series depth; tail bounded exactly below


def atanh_series(y, K=K_SER):
    """Exact (lo, hi) for log y, y rational in [1, 2]."""
    u = (y - 1) / (y + 1)          # in [0, 1/3]
    u2 = u * u
    s = F(0)
    up = u
    for k in range(K + 1):
        s += up / (2 * k + 1)
        up *= u2                   # after loop: up = u^(2K+3)
    s *= 2
    if u == 0:
        return (F(0), F(0))
    tail = 2 * up / ((2 * K + 3) * (1 - u2))
    return (s, s + tail)


LOG2 = atanh_series(F(2))


def log_bounds(x):
    """Exact (lo, hi) enclosure of log x for rational x > 0."""
    if x == 1:
        return (F(0), F(0))
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return (-hi, -lo)
    k = 0
    y = x
    while y >= 2:
        y = y / 2
        k += 1
    lo, hi = atanh_series(y)
    return (lo + k * LOG2[0], hi + k * LOG2[1])


def imul(a, b):
    ps = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (min(ps), max(ps))


def log_iv(iv):
    return (log_bounds(iv[0])[0], log_bounds(iv[1])[1])


def E_hi(T):
    """Upper bound of the frozen W-RVM error E(T), T integer >= 3."""
    lt = log_bounds(F(T))
    llt_hi = log_bounds(lt[1])[1]
    return F(1, 2) * lt[1] + F(1, 2) * llt_hi + 5


def M_iv(T):
    """Enclosure of M(T) = (T/2pi)(log(T/2pi) - 1)."""
    a = (F(T) / (2 * PI_HI), F(T) / (2 * PI_LO))
    la = log_iv(a)
    b = (la[0] - 1, la[1] - 1)
    return imul(a, b)


def dec(x, nd=6):
    """Fixed-point decimal string of a Fraction, witness display only."""
    sgn = '-' if x < 0 else ''
    x = abs(x)
    ip = x.numerator // x.denominator
    fr = x - ip
    digs = (fr * 10**nd).numerator // (fr * 10**nd).denominator
    return f"{sgn}{ip}.{digs:0{nd}d}"


checks = []

# G7 sanity first: the log machinery itself.
l2 = log_bounds(F(2))
checks.append(("G7 log2 enclosure in (0.6931, 0.6932)",
               l2[0] > F(6931, 10000) and l2[1] < F(6932, 10000)))

# G1: N(200) >= 68.
n200_lo = M_iv(200)[0] - F(7, 8) - E_hi(200)
checks.append(("G1 N(200) lower bound >= 68 [witness " + dec(n200_lo) + "]",
               n200_lo >= 68))

# G2: N(5) <= 5.
n5_hi = M_iv(5)[1] + F(7, 8) + E_hi(5)
checks.append(("G2 N(5) upper bound < 6 [witness " + dec(n5_hi) + "]",
               n5_hi < 6))

# G3: D = (1/pi) log(201/2pi) + 2 E(201) < 19.
a201 = (F(201) / (2 * PI_HI), F(201) / (2 * PI_LO))
l201_hi = log_iv(a201)[1]
d_hi = l201_hi / PI_LO + 2 * E_hi(201)
checks.append(("G3 interval multiplicity bound D < 19 [witness " + dec(d_hi) + "]",
               d_hi < 19))

# G4: 18 < 240.
checks.append(("G4 max forced multiplicity 18 < shell floor 240", 18 < 240))

# G5: ceil(68/18) = 4 distinct forced eigenvalues > 1 carrier slot.
distinct = (68 + 18 - 1) // 18
checks.append(("G5 distinct forced eigenvalues " + str(distinct) + " > 1 slot",
               distinct == 4 and distinct > 1))

# G6: E8 shells r(2), r(4), r(6) by exhaustive enumeration (D8+ model).
def sigma3(n):
    return sum(d ** 3 for d in range(1, n + 1) if n % d == 0)

cnt = {2: 0, 4: 0, 6: 0}
for x in product(range(-2, 3), repeat=8):
    q = sum(t * t for t in x)
    if q in cnt and sum(x) % 2 == 0:
        cnt[q] += 1
for y in product((-3, -1, 1, 3), repeat=8):   # y = 2x, x half-integer
    q = sum(t * t for t in y)                  # = 4 |x|^2
    if q in (8, 16, 24) and sum(y) % 4 == 0:
        cnt[q // 4] += 1
for n in (1, 2, 3):
    want = 240 * sigma3(n)
    checks.append((f"G6 E8 shell r({2*n}) = 240 sigma3({n}) = {want}",
                   cnt[2 * n] == want))

ok = all(v for _, v in checks)
for name, v in checks:
    print(("PASS " if v else "FAIL ") + name)
print("ASSEMBLY under E5: forced spectrum has >= 4 distinct eigenvalues of")
print("multiplicity <= 18; every f(Delta_E8) has <= 1 nonzero eigenvalue of")
print("multiplicity < 240; 4 > 1, contradiction; the carrier class is empty.")
print(("ALL PASS" if ok else "FAILURES") + f" ({len(checks)} gates)")
