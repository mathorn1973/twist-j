#!/usr/bin/env python3
"""audit_widder_depth_2b.py

Correction of fired gate CG2 per PREREG-AUDIT-WIDDER-DEPTH-2B.md, frozen
with this file. Exact rational arithmetic only.
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
    for _ in range(n):
        r = cmul(r, x)
    return r


gate("B2-01 (1-i)^4 = -4, the integer certificate of theta = pi/4",
     cpow((F(1), F(-1)), 4) == (F(-4), F(0)))


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


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def cpol_mul(x, y):
    return (pol_add(pol_mul(x[0], y[0]), pol_scal(-1, pol_mul(x[1], y[1]))),
            pol_add(pol_mul(x[0], y[1]), pol_mul(x[1], y[0])))


base = ([F(1), F(1)], [F(1)])
b4 = (([F(1)], [F(0)]))
for _ in range(4):
    b4 = cpol_mul(b4, base)
q2 = cpol_mul(((F(0),), (F(-2),)), b4)
target = [F(0), F(16), F(24), F(8)]
gate("B2-02 symbolic route, lengths normalized: Re[(1-i)^2((u+1)+i)^4] = "
     "8u(u+1)(u+2) exactly", trim(q2[0]) == trim(target))


def eval_pol(p, u):
    acc = F(0)
    for c in reversed(p):
        acc = acc * u + c
    return acc


def q2_direct(u):
    val = cmul(cpow((F(1), F(-1)), 2), cpow((u + 1, F(1)), 4))
    return val[0]


gate("B2-03 independent route: five-point evaluation certificate at "
     "u = 0..4, degree bound four on both sides",
     all(q2_direct(F(u)) == 8 * F(u) * (F(u) + 1) * (F(u) + 2)
         for u in range(5)))

gate("B2-04 positivity and boundary zero: 8u(u+1)(u+2) > 0 for u > 0 and "
     "= 0 at u = 0, by the factored form; spot samples agree",
     8 * F(0) * 1 * 2 == 0
     and all(q2_direct(u) > 0 for u in [F(1, 1000), F(1, 16), F(1), F(100)]))


def re_pow(A, B, j):
    return cpow((F(A), F(-B)), j)[0]


gate("B2-05 k_min(1,1) = 3 by the Re form (Re at k = 2 is exactly 0, at "
     "k = 3 exactly -2), while pi/(2 theta) = 2 exactly: the ceiling form "
     "gives 2 and is wrong at resonance",
     re_pow(1, 1, 1) == 1 and re_pow(1, 1, 2) == 0 and re_pow(1, 1, 3) == -2)

failed = 0
for label, ok in GATES:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failed += 1
print("GATES %d/%d PASS" % (len(GATES) - failed, len(GATES)))
if failed:
    print("DECISION AUDIT-DISAGREEMENT")
    sys.exit(2)
print("DECISION AUDIT-PASS")
sys.exit(0)
