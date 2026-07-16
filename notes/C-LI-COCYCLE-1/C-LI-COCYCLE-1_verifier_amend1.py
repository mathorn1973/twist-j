#!/usr/bin/env python3
# C-LI-COCYCLE-1_verifier_amend1.py
# Amendment 1 after the first-class CO6 fire of the frozen run
# (verifier db56b0b1..., stdout eeb42420...). Diagnosis: the frozen CO6
# asserted "recomputed lambda_1 lies INSIDE the rev1 pinned interval", but
# the recomputation used a single-N gamma bracket, which yields a WIDER
# interval that CONTAINS the rev1 interval. The two computations are
# consistent; the guaranteed invariant is nonempty intersection (both
# intervals contain lambda_1), not subset. This amendment:
#   CO6a  recomputes gamma with the same two-N intersection as the rev1
#         verifier (N = 10^5 and 2*10^5, overlap-checked),
#   CO6b  asserts the correct invariant: the recomputed lambda_1 interval
#         and the rev1 pinned interval intersect,
#   CO3a  re-establishes the T_1 gate with the tightened gamma:
#         M1 > 0, lambda_2 > 0, det T_1 > 0.
# The fired run is archived, its threshold is not moved; this file carries
# the corrected invariant under a new pin.
# Discipline: stdlib only, no floats, directed integer intervals, S = 10^18.
# Environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

from fractions import Fraction
S = 10 ** 18

def atanh_iv(t):
    s_lo, s_hi = 0, 0
    acc = (t[0], t[1])
    k = 0
    t2 = ((t[0] * t[0]) // S, -((-(t[1] * t[1])) // S))
    while True:
        s_lo += acc[0] // (2 * k + 1)
        s_hi += -((-acc[1]) // (2 * k + 1))
        acc = ((acc[0] * t2[0]) // S, -((-(acc[1] * t2[1])) // S))
        k += 1
        if acc[1] < (2 * k + 1):
            denom = S - t2[1]
            s_hi += -((-(acc[1] * S)) // (denom * (2 * k + 1))) + 1
            break
    return (s_lo, s_hi)

def ln_of_iv(x):
    t_lo = ((x[0] - S) * S) // (x[0] + S)
    t_hi = -((-((x[1] - S) * S)) // (x[1] + S))
    a = atanh_iv((t_lo, t_hi))
    return (2 * a[0], 2 * a[1])

def arctan_inv_int(q, terms):
    fr = Fraction(0)
    sign = 1
    for k in range(terms):
        fr += Fraction(sign, (2 * k + 1) * q ** (2 * k + 1))
        sign = -sign
    nxt = Fraction(1, (2 * terms + 1) * q ** (2 * terms + 1))
    lo_f, hi_f = (fr - nxt, fr) if sign > 0 else (fr, fr + nxt)
    return ((lo_f.numerator * S) // lo_f.denominator,
            -((-(hi_f.numerator * S)) // hi_f.denominator))

def atanh_inv_odd(m):
    x_lo = S // m
    x_hi = -((-S) // m)
    s_lo, s_hi = 0, 0
    acc_lo, acc_hi = x_lo, x_hi
    k = 0
    m2 = m * m
    while True:
        s_lo += acc_lo // (2 * k + 1)
        s_hi += -((-acc_hi) // (2 * k + 1))
        acc_lo = acc_lo // m2
        acc_hi = -((-acc_hi) // m2)
        k += 1
        if acc_hi < (2 * k + 1):
            s_hi += -((-(acc_hi * m2)) // ((m2 - 1) * (2 * k + 1))) + 1
            break
    return (s_lo, s_hi)

a5 = arctan_inv_int(5, 14)
a239 = arctan_inv_int(239, 6)
pi_iv = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])
ln4pi = ln_of_iv((4 * pi_iv[0], 4 * pi_iv[1]))
pi2_8 = ((pi_iv[0] * pi_iv[0]) // (8 * S), -((-(pi_iv[1] * pi_iv[1])) // (8 * S)))

def gamma_iv(N):
    H_lo = 0
    H_hi = 0
    for k in range(1, N + 1):
        q = S // k
        H_lo += q
        H_hi += q if S % k == 0 else q + 1
    lnN = ln_of_iv((N * S, N * S))
    return (H_lo - lnN[1] - (-((-S) // (2 * N))),
            H_hi - lnN[0] - (S // (2 * (N + 1))))

g1v = gamma_iv(10 ** 5)
g2v = gamma_iv(2 * 10 ** 5)
check("CO6a gamma brackets at N = 1e5 and 2e5 overlap; intersection taken (same construction as the rev1 pinned verifier)",
      max(g1v[0], g2v[0]) <= min(g1v[1], g2v[1]))
gam = (max(g1v[0], g2v[0]), min(g1v[1], g2v[1]))

lam1_lo = S + gam[0] // 2 - (-((-ln4pi[1]) // 2))
lam1_hi = S + (-((-gam[1]) // 2)) - (ln4pi[0] // 2)
REV1_LO, REV1_HI = 23095708964233559, 23095708972138893
check("CO6b corrected invariant: the recomputed lambda_1 interval and the rev1 pinned interval have nonempty intersection (both contain lambda_1)",
      max(lam1_lo, REV1_LO) <= min(lam1_hi, REV1_HI))
print("CO6b witness lambda_1 recomputed in [%d, %d]; rev1 pin [%d, %d] * 10^-18"
      % (lam1_lo, lam1_hi, REV1_LO, REV1_HI))

# gamma_1 EM-2 block (identical to the frozen CO2, which passed)
NG = 10 ** 5
ln_lo, ln_hi = 0, 0
A_lo, A_hi = 0, 0
for k in range(2, NG + 1):
    inc = atanh_inv_odd(2 * k - 1)
    ln_lo += 2 * inc[0]
    ln_hi += 2 * inc[1]
    A_lo += ln_lo // k
    A_hi += -((-ln_hi) // k)
A_lo -= -((-(ln_hi * ln_hi)) // (2 * S))
A_hi -= (ln_lo * ln_lo) // (2 * S)
fN_lo = ln_lo // NG
fN_hi = -((-ln_hi) // NG)
B_hi = -((-(ln_hi - S)) // (12 * NG * NG)) + 1
g1_lo = A_lo - (-((-fN_hi) // 2))
g1_hi = A_hi - (fN_lo // 2) + 2 * B_hi

gam2 = ((gam[0] * gam[0]) // S, -((-(gam[1] * gam[1])) // S))
m1_lo = 3 * S + gam[0] + gam2[0] + 2 * g1_lo - pi2_8[1] - ln4pi[1]
m1_hi = 3 * S + gam[1] + gam2[1] + 2 * g1_hi - pi2_8[0] - ln4pi[0]
lam2_lo = S + gam[0] - gam2[1] - 2 * g1_hi + pi2_8[0] - ln4pi[1]
lam2_hi = S + gam[1] - gam2[0] - 2 * g1_lo + pi2_8[1] - ln4pi[0]
det_lo = (m1_lo * lam2_lo) // S
check("CO3a T_1 gate re-established with the tightened gamma: M1 > 0, lambda_2 > 0, det T_1 > 0",
      m1_lo > 0 and m1_hi < S // 10 ** 4 and lam2_lo > 0 and det_lo > 0)
print("CO3a witness M1 in [%d, %d]; lambda_2 in [%d, %d] * 10^-18"
      % (m1_lo, m1_hi, lam2_lo, lam2_hi))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 1 of C-LI-COCYCLE-1" if not FAILED else "FAIL"))
