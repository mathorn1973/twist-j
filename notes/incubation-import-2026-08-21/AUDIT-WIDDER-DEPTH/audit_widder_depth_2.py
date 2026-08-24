#!/usr/bin/env python3
"""audit_widder_depth_2.py

Correction leg 2 of AUDIT-EULER-WIDDER-DEPTH, per
PREREG-AUDIT-WIDDER-DEPTH-2.md, frozen with this file. Verifies the owner's
two corrections and the finite-prefix no-go, and attempts to break them.

Exact rational arithmetic only; Q(i) as Fraction pairs; sign decisions via
the integer polynomial Q_k(u) = Re[(A-iB)^k ((u+A)+iB)^(2k)]. No float, no
math import, no zero table.

Codes: 0 AUDIT-PASS, 1 AUDIT-INTEGRITY-STOP, 2 AUDIT-DISAGREEMENT.
"""

from fractions import Fraction as F
import sys

GATES = []


def gate(label, cond):
    GATES.append((label, bool(cond)))


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cpow(x, n):
    r = (F(1), F(0))
    b = x
    while n:
        if n & 1:
            r = cmul(r, b)
        b = cmul(b, b)
        n >>= 1
    return r


def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def qsign(A, B, k, u):
    """sign of P_k(A,B;u) as sign of Re[(A-iB)^k ((u+A)+iB)^(2k)]."""
    val = cmul(cpow((F(A), F(-B)), k), cpow((u + F(A), F(B)), 2 * k))
    return val[0]


def p_exact(A, B, k, u):
    """exact value of P_k(A,B;u)."""
    num = cmul(cpow((F(A), F(-B)), k), cpow((u + F(A), F(B)), 2 * k))
    den = ((u + F(A)) ** 2 + F(B) ** 2) ** (2 * k)
    return 2 * F(fact(2 * k - 1)) * num[0] / den


def re_pow(A, B, j):
    return cpow((F(A), F(-B)), j)[0]


def kmin_re(A, B, cap=400):
    for k in range(1, cap + 1):
        if re_pow(A, B, k) < 0:
            return k
    return None


UGRID = [F(1, 1000), F(1, 100)] + [F(m, 16) for m in range(1, 65)] + \
        [F(2) ** j for j in range(1, 11)]

# ---------------------------------------------------------------------------
# CG1 the owner counterexample, to the exact reduced fraction
# ---------------------------------------------------------------------------

OWNER_FRACTION = -F(172056926056081143103488000, 51185893014090757)
p8 = p_exact(1, 1, 8, F(1, 2))
gate("CG1 owner counterexample: Re[(1-i)^8] = 16 > 0, yet P_8(1,1;1/2) < 0 "
     "and equals the exact reduced fraction of the review",
     re_pow(1, 1, 8) == 16 and p8 < 0 and p8 == OWNER_FRACTION)

# ---------------------------------------------------------------------------
# CG2 resonance: theta = pi/4 by integer certificate; Q_2 = 8u(u+1)(u+2);
#     k_min = 3 while the ceiling formula gives 2
# ---------------------------------------------------------------------------

res_cert = cpow((F(1), F(-1)), 4) == (F(-4), F(0))

# polynomial identity over Q[u]: real and imaginary parts as coefficient lists
def pol_mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return r


def pol_add(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0))
            for i in range(n)]


def pol_scal(c, p):
    return [F(c) * x for x in p]


def cpol_mul(x, y):
    return (pol_add(pol_mul(x[0], y[0]), pol_scal(-1, pol_mul(x[1], y[1]))),
            pol_add(pol_mul(x[0], y[1]), pol_mul(x[1], y[0])))


def cpol_pow(x, n):
    r = ([F(1)], [F(0)])
    for _ in range(n):
        r = cpol_mul(r, x)
    return r


base = ([F(1), F(1)], [F(1)])          # (u+1) + i
b4 = cpol_pow(base, 4)
q2 = cpol_mul(((F(0),), (F(-2),)), b4)  # (1-i)^2 = -2i times ((u+1)+i)^4
target = [F(0), F(16), F(24), F(8)]     # 8u(u+1)(u+2) = 8u^3 + 24u^2 + 16u
ident_ok = pol_add(q2[0], pol_scal(-1, target)) == [F(0)] * 4
strictly_pos = all(qsign(1, 1, 2, u) > 0 for u in UGRID)
gate("CG2 resonance: (1-i)^4 = -4 certifies theta = pi/4; the level-2 sign "
     "polynomial is exactly 8u(u+1)(u+2), positive on (0,inf) with unattained "
     "zero at the boundary; k_min(1,1) = 3 by the Re form while "
     "ceil(pi/(2 theta)) = 2, so the ceiling form is wrong at resonance",
     res_cert and ident_ok and strictly_pos and kmin_re(1, 1) == 3
     and re_pow(1, 1, 2) == 0 and re_pow(1, 1, 3) == -2)

# ---------------------------------------------------------------------------
# certified arctan machinery for the witness fallback
# ---------------------------------------------------------------------------

def arctan_bounds(x, terms):
    lo = F(0)
    hi = F(0)
    part = F(0)
    for n in range(terms):
        part += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        nxt = x ** (2 * n + 3) / (2 * n + 3)
        if n % 2 == 0:
            hi = part
            lo = part - nxt
        else:
            lo = part
            hi = part + nxt
    return lo, hi


a5 = arctan_bounds(F(1, 5), 15)
a239 = arctan_bounds(F(1, 239), 8)
PI_LO = 4 * (4 * a5[0] - a239[1])
PI_HI = 4 * (4 * a5[1] - a239[0])


def find_witness(A, B, k):
    """exact rational u > 0 with P_k < 0, or None."""
    for u in UGRID:
        if qsign(A, B, k, u) < 0:
            return u
    # certified fallback: t = B/(u+A) scanned below B/A; window pi/2..3pi/2
    tha_lo, tha_hi = arctan_bounds(F(B) / F(A), 200)
    for m in range(1, 64):
        t = F(B) / F(A) * F(m, 64)
        terms = 250 if t > F(9, 10) else 90
        ph_lo, ph_hi = arctan_bounds(t, terms)
        g_lo = k * (2 * ph_lo - tha_hi)
        g_hi = k * (2 * ph_hi - tha_lo)
        if g_lo > PI_HI / 2 and g_hi < 3 * PI_LO / 2:
            u = F(B) / t - F(A)
            if u > 0 and qsign(A, B, k, u) < 0:
                return u
    return None


# ---------------------------------------------------------------------------
# CG3 non-resonant endpoint-return counterexample
# ---------------------------------------------------------------------------

w14 = find_witness(2, 1, 14)
gate("CG3 non-resonant counterexample: Re[(2-i)^14] = 76443 > 0 while "
     "Re[(2-i)^4] = -7 < 0, and an exact rational u witnesses P_14 < 0; the "
     "first audit's per-level criterion is false off resonance too",
     re_pow(2, 1, 14) == 76443 and re_pow(2, 1, 4) == -7 and w14 is not None)

# ---------------------------------------------------------------------------
# CG4 corrected criterion against empirical search, both directions
# ---------------------------------------------------------------------------

PAIRS = [(1, 1), (2, 1), (3, 2), (5, 1), (7, 4)]
crit_ok = True
witness_count = 0
for (A, B) in PAIRS:
    for k in range(1, 21):
        prefix_neg = any(re_pow(A, B, j) < 0 for j in range(1, k + 1))
        if prefix_neg:
            w = find_witness(A, B, k)
            crit_ok = crit_ok and w is not None
            witness_count += 1
        else:
            crit_ok = crit_ok and all(qsign(A, B, k, u) > 0 for u in UGRID)
gate("CG4 corrected criterion: on the full grid, prefix-Re negativity and "
     "empirical negativity agree in both directions, every negative case "
     "carrying an exact rational witness", crit_ok and witness_count > 20)

# ---------------------------------------------------------------------------
# CG5 the two k_min forms agree; owner control points unchanged
# ---------------------------------------------------------------------------

def kmin_floor(A, B):
    """floor(pi/(2 arctan(B/A))) + 1 with certified brackets; None if the
    bracket straddles an integer (then only the Re form decides)."""
    lo, hi = arctan_bounds(F(B) / F(A), 200)
    v_lo = PI_LO / (2 * hi)
    v_hi = PI_HI / (2 * lo)
    f_lo = v_lo.numerator // v_lo.denominator
    f_hi = v_hi.numerator // v_hi.denominator
    if f_lo == f_hi:
        return f_lo + 1
    return None


forms_ok = True
for (A, B) in PAIRS + [(4, 4), (9, 10)]:
    if B > A:
        continue
    km_re = kmin_re(A, B)
    km_fl = kmin_floor(A, B)
    if (A, B) in ((1, 1), (4, 4)):
        # exact resonance: pi/(2 theta) = 2 exactly, floor + 1 = 3
        forms_ok = forms_ok and km_re == 3
    elif km_fl is not None:
        forms_ok = forms_ok and km_re == km_fl


def zed(beta, gamma):
    beta = F(beta)
    gamma = F(gamma)
    return gamma * gamma + beta * (1 - beta), gamma * (2 * beta - 1)


Ac1, Bc1 = zed(F(9, 10), F(1, 2))
Ac2, Bc2 = zed(F(3, 4), F(10))
gate("CG5 floor-plus-one and min-Re forms of k_min agree on the grid, the "
     "resonant points give 3, and the owner control points stay at 2 and 32",
     forms_ok and kmin_re(Ac1, Bc1) == 2 and kmin_re(Ac2, Bc2) == 32)

# ---------------------------------------------------------------------------
# CG6 the finite-prefix no-go family
# ---------------------------------------------------------------------------

nogo_ok = True
for N in (1, 2, 5, 10, 100, 10 ** 6):
    AN = F(N) ** 2 + F(3, 16)
    BN = F(N) / 2
    # rho(rho-1) check for rho = 3/4 + iN
    rr = cmul((F(3, 4), F(N)), (F(-1, 4), F(N)))
    nogo_ok = nogo_ok and rr == (-AN, BN)
    nogo_ok = nogo_ok and BN / AN < F(1, 2 * N)
    kcap = min(N, 40)
    nogo_ok = nogo_ok and all(re_pow(AN, BN, j) > 0 for j in range(1, kcap + 1))
gate("CG6 finite-prefix no-go: for rho_N = 3/4 + iN the exact chain "
     "B/A < 1/(2N) holds, so k theta < 1/2 < pi/2 for every k <= N and one "
     "off-critical configuration passes the whole prefix; prefix-Re positive "
     "on every tested level", nogo_ok)

sample_ok = all(qsign(F(25) + F(3, 16), F(5, 2), k, u) > 0
                for k in range(1, 6) for u in UGRID)
gate("CG6b spot samples for N = 5: levels 1..5 positive at every sampled u",
     sample_ok)

# ---------------------------------------------------------------------------
# CG7 no level-to-level induction
# ---------------------------------------------------------------------------

w1_ok = all(qsign(Ac1, Bc1, 1, u) > 0 for u in UGRID)
w2_wit = find_witness(Ac1, Bc1, 2)
gate("CG7 rho = 9/10 + i/2: W_1 positive at every sample, W_2 negative at an "
     "exact witness; W_k >= 0 does not imply W_(k+1) >= 0 on a single pair",
     w1_ok and w2_wit is not None)

# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

failed = 0
for label, ok in GATES:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failed += 1

print("OWNER-FRACTION exact match: P_8(1,1;1/2) = %s" % p8)
print("WITNESS (2,1,k=14): u = %s" % (w14,))
print("WITNESS (rho=9/10+i/2, W_2): u = %s" % (w2_wit,))
print("WITNESS-COUNT prefix-negative cases carrying exact witnesses: %d"
      % witness_count)
print("GATES %d/%d PASS" % (len(GATES) - failed, len(GATES)))
if failed:
    print("DECISION AUDIT-DISAGREEMENT")
    sys.exit(2)
print("DECISION AUDIT-PASS")
sys.exit(0)
