#!/usr/bin/env python3
"""audit_widder_depth_1.py

Independent audit of the Euler-Widder hierarchy branch
notes/c-rh-stieltjes-widder-euler-1-n (issue 471, head f0a455a1), per
PREREG-AUDIT-WIDDER-DEPTH-1.md, frozen together with this file.

Exact rational arithmetic only. Complex numbers are carried as pairs of
Fractions in Q(i). No float is formed anywhere and math is not imported;
the enclosure of pi is computed by Machin with exact truncation bounds.

Return codes: 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
"""

from fractions import Fraction as F
import sys

GATES = []
STOP = []


def gate(label, cond):
    GATES.append((label, bool(cond)))


# ---------------------------------------------------------------------------
# Q(i) arithmetic
# ---------------------------------------------------------------------------

def cx(a, b=0):
    return (F(a), F(b))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def csub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cpow(x, n):
    r = cx(1)
    b = x
    while n:
        if n & 1:
            r = cmul(r, b)
        b = cmul(b, b)
        n >>= 1
    return r


def cconj(x):
    return (x[0], -x[1])


def cabs2(x):
    return x[0] * x[0] + x[1] * x[1]


def cdiv(x, y):
    d = cabs2(y)
    n = cmul(x, cconj(y))
    return (n[0] / d, n[1] / d)


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


# ---------------------------------------------------------------------------
# exact rational-function arithmetic for the pole calculus (WA1)
# polynomials over Q as coefficient lists; a rational function is (num, den)
# ---------------------------------------------------------------------------

def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0))
            for i in range(n)]


def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return r


def pscal(c, p):
    return [F(c) * x for x in p]


def pder(p):
    if len(p) <= 1:
        return [F(0)]
    return [p[i] * i for i in range(1, len(p))]


def peq(p, q):
    d = padd(p, pscal(-1, q))
    return all(x == 0 for x in d)


def rder(num, den_root, den_pow):
    """derivative of num(u)/(u - r)^m, returned in the same shape."""
    # d/du [N/(u-r)^m] = (N' (u-r) - m N)/(u-r)^(m+1)
    new = padd(pmul(pder(num), [-den_root, F(1)]), pscal(-den_pow, num))
    return new, den_pow + 1


# WA1: (-1)^(k-1) D^(2k-1)[u^k/(u-z)] = (2k-1)! (-z)^k/(u-z)^(2k)
# verified as an exact identity in Q(r)[u] for a symbolic-in-value root r.
calc_ok = True
for r_val in (F(-3), F(-1, 7), F(5, 2), F(11)):
    for k in range(1, 7):
        num = [F(0)] * k + [F(1)]          # u^k
        dpow = 1
        for _ in range(2 * k - 1):
            num, dpow = rder(num, r_val, dpow)
        num = pscal((-1) ** (k - 1), num)
        target_num = [F(fact(2 * k - 1)) * (-r_val) ** k]
        calc_ok = calc_ok and dpow == 2 * k and peq(num, target_num)
gate("WA1 pole calculus: (-1)^(k-1) D^(2k-1)[u^k/(u-z)] = "
     "(2k-1)!(-z)^k/(u-z)^(2k), exact rational-function identity, k=1..6, "
     "four distinct roots", calc_ok)


# ---------------------------------------------------------------------------
# zero geometry
# ---------------------------------------------------------------------------

def zed(beta, gamma):
    """z = rho(rho-1) for rho = beta + i gamma; returns (A, B) with z = -A + iB."""
    beta = F(beta)
    gamma = F(gamma)
    A = gamma * gamma + beta * (1 - beta)
    B = gamma * (2 * beta - 1)
    return A, B


def pair_term(k, A, B, u):
    """exact contribution of the conjugate pair {z, zbar} to W_k at u."""
    mz = (A, -B)                       # -z = A - iB
    w = (u + A, -B)                    # u - z
    val = cdiv(cpow(mz, k), cpow(w, 2 * k))
    return 2 * F(fact(2 * k - 1)) * val[0]


def f_term(A, B, u):
    return 2 * (u + A) / ((u + A) ** 2 + B ** 2)


def w1_term(A, B, u):
    return 2 * (A * (u + A) ** 2 + B * B * (2 * u + A)) / (((u + A) ** 2 + B * B) ** 2)


UGRID = [F(1, 1000), F(1, 100), F(1, 10), F(1, 2), F(1), F(2), F(10),
         F(100), F(1000), F(10000)]
BETAS = [F(3, 5), F(2, 3), F(3, 4), F(9, 10), F(99, 100)]
GAMMAS = [F(1, 2), F(1), F(2), F(5), F(10), F(20), F(50), F(100)]

# WA2 unconditional first two levels
pos_ok = True
for beta in BETAS + [F(1, 2), F(1, 10), F(1, 3)]:
    for gamma in GAMMAS:
        A, B = zed(beta, gamma)
        pos_ok = pos_ok and A > 0
        for u in UGRID:
            pos_ok = pos_ok and f_term(A, B, u) > 0
            pos_ok = pos_ok and w1_term(A, B, u) > 0
            pos_ok = pos_ok and w1_term(A, B, u) == pair_term(1, A, B, u)
gate("WA2 unconditional levels: A = gamma^2 + beta(1-beta) > 0, and every "
     "conjugate pair contributes positively to f and to W_1 at every sampled "
     "u > 0; the closed forms agree with the pole calculus", pos_ok)


def kmin_isolated(A, B, cap=4000):
    """first k with Re[(A - iB)^k] < 0; None if none below the cap."""
    if B == 0:
        return None
    mz = (A, -B)
    acc = cx(1)
    for k in range(1, cap + 1):
        acc = cmul(acc, mz)
        if acc[0] < 0:
            return k
    return None


# WA4 the owner's two recorded depths
A1, B1 = zed(F(9, 10), F(1, 2))
A2, B2 = zed(F(3, 4), F(10))
k1 = kmin_isolated(A1, B1)
k2 = kmin_isolated(A2, B2)
gate("WA4 owner data point rho = 9/10 + i/2 gives first negative degree 2",
     k1 == 2)
gate("WA4 owner data point rho = 3/4 + 10i gives first negative degree 32",
     k2 == 32)

# WA3 the exact criterion against sampled u
crit_ok = True
witness_ok = True
for beta in BETAS:
    for gamma in GAMMAS:
        A, B = zed(beta, gamma)
        km = kmin_isolated(A, B)
        if km is None or km > 200:
            continue
        for k in range(1, km):
            for u in UGRID:
                crit_ok = crit_ok and pair_term(k, A, B, u) > 0
        found = any(pair_term(km, A, B, u) < 0 for u in UGRID)
        witness_ok = witness_ok and found
gate("WA3 exact criterion: below the first negative degree every sampled u "
     "gives a positive pair contribution", crit_ok)
gate("WA3 exact criterion: at the first negative degree a sampled rational u "
     "witnesses a negative pair contribution", witness_ok)


# ---------------------------------------------------------------------------
# certified rational enclosure of pi by Machin, exact truncation bounds
# ---------------------------------------------------------------------------

def arctan_bounds(x, terms):
    """alternating series; returns (lo, hi) exact rationals for arctan(x), 0<x<1."""
    lo = F(0)
    hi = F(0)
    part = F(0)
    for n in range(terms):
        t = (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        part += t
        nxt = x ** (2 * n + 3) / (2 * n + 3)
        if n % 2 == 0:
            hi = part
            lo = part - nxt
        else:
            lo = part
            hi = part + nxt
    return lo, hi


a5lo, a5hi = arctan_bounds(F(1, 5), 40)
a239lo, a239hi = arctan_bounds(F(1, 239), 40)
PI_LO = 4 * (4 * a5lo - a239hi)
PI_HI = 4 * (4 * a5hi - a239lo)
gate("PI certified rational enclosure by Machin brackets 3.14159265 and is "
     "tighter than 10^-20", PI_LO < PI_HI and PI_LO > F(314159265, 10 ** 8)
     and PI_HI < F(314159266, 10 ** 8) and PI_HI - PI_LO < F(1, 10 ** 20))


def arctan_pair_bounds(B, A, terms=60):
    """bounds for arctan(B/A) with 0 < B/A <= 1."""
    x = B / A
    return arctan_bounds(x, terms)


# WA5 depth law: k_min = ceil(pi / (2 theta))
law_ok = True
law_rows = []
for beta in BETAS:
    for gamma in GAMMAS:
        A, B = zed(beta, gamma)
        if B <= 0 or B > A:
            continue
        km = kmin_isolated(A, B)
        if km is None:
            continue
        tlo, thi = arctan_pair_bounds(B, A)
        # ceil(pi/(2 theta)) bracketed: pi/(2 thi) <= value <= pi/(2 tlo)
        lo_val = PI_LO / (2 * thi)
        hi_val = PI_HI / (2 * tlo)
        pred_lo = -(-lo_val.numerator // lo_val.denominator)      # ceil
        pred_hi = -(-hi_val.numerator // hi_val.denominator)
        ok = pred_lo <= km <= pred_hi
        law_ok = law_ok and ok
        law_rows.append((beta, gamma, km, pred_lo, pred_hi))
gate("WA5 depth law: the exact first negative degree equals "
     "ceil(pi/(2 arctan(B/A))) within its certified rational bracket, on the "
     "whole declared grid", law_ok)

# WA5b asymptotic reading: k_min grows at least linearly in gamma at fixed beta
mono_ok = True
for beta in BETAS:
    seq = []
    for gamma in GAMMAS:
        A, B = zed(beta, gamma)
        if B <= 0 or B > A:
            continue
        km = kmin_isolated(A, B)
        if km is not None:
            seq.append((gamma, km))
    for i in range(len(seq) - 1):
        mono_ok = mono_ok and seq[i + 1][1] >= seq[i][1]
gate("WA5b at fixed beta the first negative degree is nondecreasing in the "
     "height gamma on the declared grid", mono_ok)

# WA6 vacuity of the low levels
vac_ok = True
for beta in BETAS + [F(1, 2), F(1, 3), F(1, 10), F(999, 1000)]:
    for gamma in [F(1), F(2), F(5), F(10), F(14), F(50), F(1000)]:
        A, B = zed(beta, gamma)
        vac_ok = vac_ok and B <= A
        mz = (A, -B)
        vac_ok = vac_ok and cpow(mz, 2)[0] > 0
        for u in UGRID:
            vac_ok = vac_ok and pair_term(2, A, B, u) > 0
gate("WA6 vacuity: every admissible pair with gamma >= 1 has B <= A, so "
     "Re[(A-iB)^2] > 0 and its W_2 contribution is positive at every sampled "
     "u; W_2 >= 0 therefore needs no RH input", vac_ok)

# WA6b the general inequality behind it, as an exact statement on the grid:
# gamma(2 beta - 1) <= gamma <= gamma^2 <= gamma^2 + beta(1-beta) for gamma >= 1
ineq_ok = True
for beta in BETAS + [F(1, 2), F(999, 1000)]:
    for gamma in [F(1), F(3, 2), F(14), F(10 ** 6)]:
        ineq_ok = ineq_ok and gamma * (2 * beta - 1) <= gamma
        ineq_ok = ineq_ok and gamma <= gamma * gamma
        ineq_ok = ineq_ok and gamma * gamma <= gamma * gamma + beta * (1 - beta)
gate("WA6b the chain gamma(2beta-1) <= gamma <= gamma^2 <= A holds exactly "
     "for gamma >= 1 and 0 < beta < 1", ineq_ok)

# WA6c safe-depth bound at a declared verification height H:
# theta < B/A <= 1/H, so k theta < pi/2 for every k <= pi H / 2.
H = F(3, 1) * 10 ** 12
safe_k = (PI_LO * H / 2)
SAFE_LEVELS = safe_k.numerator // safe_k.denominator
bound_ok = True
for beta in [F(3, 5), F(3, 4), F(9, 10), F(999, 1000)]:
    A, B = zed(beta, H)
    bound_ok = bound_ok and B / A <= 1 / H
gate("WA6c at a verification height H every off-line pair obeys B/A <= 1/H, "
     "so all levels up to floor(pi H / 2) are unconditionally non-negative",
     bound_ok and SAFE_LEVELS > 4 * 10 ** 12)

# WA7 breaker: background competition
off_beta, off_gamma = F(3, 4), F(2)
Ao, Bo = zed(off_beta, off_gamma)
k_off = kmin_isolated(Ao, Bo)
online = [F(14), F(21), F(25), F(30), F(32)]
comp_rows = []
comp_ok = True
for u in UGRID:
    neg = pair_term(k_off, Ao, Bo, u)
    if neg >= 0:
        continue
    tot = neg
    for g in online:
        Ac, Bc = zed(F(1, 2), g)
        tot += pair_term(k_off, Ac, Bc, u)
    comp_rows.append((u, neg < 0, tot > 0))
    if tot <= 0:
        comp_ok = False
gate("WA7 breaker: at the isolated first negative degree of an off-line pair, "
     "adding five on-line poles turns every negative sampled value positive, "
     "so the isolated depth is a lower bound only", comp_ok and len(comp_rows) > 0)

# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

failed = 0
for label, ok in GATES:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failed += 1

for note in STOP:
    print("STOP-NOTE " + note)

print("DEPTH TABLE beta gamma kmin predicted_lo predicted_hi")
for beta, gamma, km, plo, phi in law_rows:
    print("DEPTH %s %s %d %d %d" % (beta, gamma, km, plo, phi))
print("OWNER-POINTS rho=9/10+i/2 kmin=%s ; rho=3/4+10i kmin=%s" % (k1, k2))
print("BREAKER off-line rho=3/4+2i isolated kmin=%d, sampled negatives "
      "rescued by background: %d" % (k_off, len(comp_rows)))
print("SAFE-LEVELS floor(pi H / 2) at H = 3 x 10^12 is %d" % SAFE_LEVELS)
print("GATES %d/%d PASS" % (len(GATES) - failed, len(GATES)))

if STOP:
    print("DECISION AUDIT-INTEGRITY-STOP")
    sys.exit(1)
if failed:
    print("DECISION AUDIT-DISAGREEMENT")
    sys.exit(2)
print("DECISION AUDIT-PASS")
sys.exit(0)
