#!/usr/bin/env python3
"""verify_lambda_grid_audit_1b.py

Correction leg for check A3-07 of verify_lambda_grid_audit_1.py (pinned run
recorded as FAIL). Diagnosis: the Horner shift kept a spurious trailing zero,
so the leading coefficient was read from the wrong slot; the computed
coefficients themselves were correct, for example Phi_5(x+1) = [5,10,10,5,1].
This leg re-runs only the Eisenstein certificates with the representation
fixed, and adds an independent mod-5 congruence certificate
Phi_(5^k)(x+1) = x^phi(5^k) mod 5. Exact integer arithmetic only.
"""

import sys

CHECKS = []


def check(label, cond):
    CHECKS.append((label, bool(cond)))


def cyclotomic_5k(k):
    n = 5 ** (k - 1)
    c = [0] * (4 * n + 1)
    for t in range(5):
        c[n * t] = 1
    return c


def shift_poly(c):
    res = [0]
    for coeff in reversed(c):
        new = [0] * (len(res) + 1)
        for i, a in enumerate(res):
            new[i] += a
            new[i + 1] += a
        new[0] += coeff
        res = new
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


for k in (1, 2, 3):
    deg = 4 * 5 ** (k - 1)
    sh = shift_poly(cyclotomic_5k(k))
    check("B3-07a k=%d degree preserved, monic" % k,
          len(sh) == deg + 1 and sh[-1] == 1)
    check("B3-07b k=%d constant term exactly 5, not divisible by 25" % k,
          sh[0] == 5 and sh[0] % 25 != 0)
    check("B3-07c k=%d all middle coefficients divisible by 5" % k,
          all(x % 5 == 0 for x in sh[1:-1]))
    check("B3-07d k=%d independent congruence Phi(x+1) = x^deg mod 5" % k,
          [x % 5 for x in sh] == [0] * deg + [1])

failures = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failures += 1
print("RESULT %d/%d PASS" % (len(CHECKS) - failures, len(CHECKS)))
sys.exit(1 if failures else 0)
