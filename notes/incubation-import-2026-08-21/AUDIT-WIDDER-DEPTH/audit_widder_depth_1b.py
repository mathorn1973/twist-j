#!/usr/bin/env python3
"""audit_widder_depth_1b.py

Correction leg of AUDIT-EULER-WIDDER-DEPTH, per PREREG-AUDIT-WIDDER-DEPTH-1B,
frozen with this file. Tests why gate WA7 of leg 1 fired and whether the
corrected masking statement holds.

Exact rational arithmetic only; Q(i) as Fraction pairs; no float, no math.
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


def zed(beta, gamma):
    beta = F(beta)
    gamma = F(gamma)
    return gamma * gamma + beta * (1 - beta), gamma * (2 * beta - 1)


def pair_term(k, A, B, u, fk):
    mz = (A, -B)
    w = (u + A, -B)
    val = cdiv(cpow(mz, k), cpow(w, 2 * k))
    return 2 * fk * val[0]


def kmin_isolated(A, B, cap=4000):
    if B == 0:
        return None
    mz = (A, -B)
    acc = (F(1), F(0))
    for k in range(1, cap + 1):
        acc = cmul(acc, mz)
        if acc[0] < 0:
            return k
    return None


UGRID = [F(1, 1000), F(1, 100), F(1, 10), F(1, 2), F(1), F(2), F(10), F(100)]
BACKGROUND = [F(14), F(21), F(25), F(30), F(32), F(37), F(40), F(43), F(48)]

# XA1 weight ordering in height, at fixed level and u
order_ok = True
K_ORD = 6
fk_ord = F(fact(2 * K_ORD - 1))
for u in UGRID:
    prev = None
    for gamma in [F(1), F(2), F(5), F(14), F(50), F(100)]:
        A, B = zed(F(1, 2), gamma)
        v = pair_term(K_ORD, A, B, u, fk_ord)
        if prev is not None:
            order_ok = order_ok and v < prev
        prev = v
gate("XA1 at fixed level and u the contribution magnitude strictly decreases "
     "with the height of an on-line pole", order_ok)

# XA2 masking of an off-line pair placed ABOVE part of the on-line spectrum
Ao, Bo = zed(F(3, 4), F(50))
K = kmin_isolated(Ao, Bo)
fk = F(fact(2 * K - 1))
mask_rows = []
mask_ok = True
neg_seen = 0
for u in UGRID:
    neg = pair_term(K, Ao, Bo, u, fk)
    tot = neg
    biggest = F(0)
    for gamma in BACKGROUND:
        Ac, Bc = zed(F(1, 2), gamma)
        c = pair_term(K, Ac, Bc, u, fk)
        tot += c
        if c > biggest:
            biggest = c
    if neg < 0:
        neg_seen += 1
        mask_rows.append((u, neg, tot, biggest))
        if tot <= 0:
            mask_ok = False
gate("XA2 masking: at the exact first negative degree of an off-line pair at "
     "height 50, the lower on-line background keeps the aggregate positive at "
     "every sampled u where the pair itself is negative",
     mask_ok and neg_seen > 0)

# XA3 leg-1 control: off-line pair BELOW the whole background stays negative
Al, Bl = zed(F(3, 4), F(2))
KL = kmin_isolated(Al, Bl)
fkl = F(fact(2 * KL - 1))
survived = 0
sampled_neg = 0
for u in UGRID:
    neg = pair_term(KL, Al, Bl, u, fkl)
    if neg >= 0:
        continue
    sampled_neg += 1
    tot = neg
    for gamma in BACKGROUND:
        Ac, Bc = zed(F(1, 2), gamma)
        tot += pair_term(KL, Ac, Bc, u, fkl)
    if tot < 0:
        survived += 1
gate("XA3 leg-1 diagnosis: an off-line pair sitting below the whole "
     "background keeps the aggregate negative, which is exactly why WA7 fired",
     sampled_neg > 0 and survived == sampled_neg)

# XA4 the domination ratio at the masked level
ratio_ok = True
ratios = []
for u, neg, tot, biggest in mask_rows:
    r = biggest / (-neg)
    ratios.append((u, r))
    if r <= 10 ** 6:
        ratio_ok = False
gate("XA4 the dominant positive term exceeds the negative term by more than "
     "10^6 at every masked sample", ratio_ok and len(ratios) > 0)

# XA5 the closed reading: weight decay in the level, at fixed height
decay_ok = True
A5, B5 = zed(F(1, 2), F(14))
for u in [F(1, 10), F(1)]:
    prev_ratio = None
    for k in (4, 6, 8, 10):
        fkk = F(fact(2 * k - 1))
        v = pair_term(k, A5, B5, u, fkk)
        norm = v / F(fact(2 * k - 1))
        # normalized weight must fall like A^(-k): compare successive ratios
        if prev_ratio is not None:
            decay_ok = decay_ok and norm < prev_ratio
        prev_ratio = norm
gate("XA5 at fixed height the factorial-normalized weight falls strictly with "
     "the level, so depth amplifies the lowest poles", decay_ok)

failed = 0
for label, ok in GATES:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failed += 1

print("OFFLINE-PROBE rho=3/4+50i first negative degree %d" % K)
print("LEG1-CONTROL  rho=3/4+2i first negative degree %d, sampled negatives "
      "%d, survived background %d" % (KL, sampled_neg, survived))
for u, r in ratios:
    print("RATIO u=%s dominant_positive_over_negative_exceeds_10p%d"
          % (u, len(str(int(r))) - 1))
print("GATES %d/%d PASS" % (len(GATES) - failed, len(GATES)))
if failed:
    print("DECISION AUDIT-DISAGREEMENT")
    sys.exit(2)
print("DECISION AUDIT-PASS")
sys.exit(0)
