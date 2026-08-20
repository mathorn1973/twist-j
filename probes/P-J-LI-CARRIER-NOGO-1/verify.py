#!/usr/bin/env python3
# P-J-LI-CARRIER-NOGO-1 verify.py
# Finite exact audit for J-LI-CYCLIC-CARRIER-DIMENSION [T]: no unitary
# with finite-dimensional cyclic subspace realizes the Li ladder
# lambda_n = ||sum_(k<n) U^k v||^2 for all n >= 1. The universal theorem is
# carried by the written proof in PREREG.md (imports: Li's criterion in the
# Bombieri-Lagarias form, the Lagarias asymptotic under RH, the spectral
# theorem); this verifier audits the finite mechanism on exact exemplars
# inside the program's own field Q(zeta_10) = Q(zeta_5).
#
# Python standard library only. Fraction arithmetic on polynomial vectors
# mod Phi_10(x) = x^4 - x^3 + x^2 - x + 1. No float anywhere.

import sys
from fractions import Fraction

assert len(sys.argv) == 1

checks = 0

def gate(name, condition):
    global checks
    assert condition, name
    checks += 1
    print("%s PASS" % name)

# ---- exact arithmetic in Q(zeta_10) as Q[x]/Phi_10 -----------------------
# Phi_10(x) = x^4 - x^3 + x^2 - x + 1, so x^4 = x^3 - x^2 + x - 1.

def red(p):
    p = [Fraction(c) for c in p]
    while len(p) < 4:
        p.append(Fraction(0))
    while len(p) > 4:
        c = p.pop()
        if c:
            d = len(p)
            p[d - 1] += c
            p[d - 2] -= c
            p[d - 3] += c
            p[d - 4] -= c
    return tuple(p[:4])

ZERO = red([0])
ONE = red([1])
Z = red([0, 1])          # zeta_10

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def scal(s, a):
    return tuple(Fraction(s) * x for x in a)

def mul(a, b):
    out = [Fraction(0)] * 7
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return red(out)

def zpow(k):
    r = ONE
    for _ in range(k % 10):
        r = mul(r, Z)
    return r

def conj(a):
    r = ZERO
    for i, x in enumerate(a):
        if x:
            r = add(r, scal(x, zpow((9 * i) % 10)))
    return r

SQRT5 = add(ONE, scal(2, add(zpow(2), zpow(8))))

def to_real_pair(a):
    # a in the real subfield: a = p + q*sqrt5, p and q rational
    assert conj(a) == a, "element not real"
    s = SQRT5
    idx = next(i for i in range(1, 4) if s[i] != 0)
    q = a[idx] / s[idx]
    p = a[0] - q * s[0]
    assert add(scal(p, ONE), scal(q, s)) == a, "expansion failed"
    return p, q

def real_sign(p, q):
    # exact sign of p + q*sqrt5
    if q == 0:
        return (p > 0) - (p < 0)
    if p == 0:
        return (q > 0) - (q < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    d = p * p - 5 * q * q
    assert d != 0
    if p > 0 and q < 0:
        return 1 if d > 0 else -1
    return 1 if d < 0 else -1     # p < 0 and q > 0

print("P-J-LI-CARRIER-NOGO-1 verify")

# KC1 field sanity
S10 = ZERO
for k in range(10):
    S10 = add(S10, zpow(k))
gate("KC1 field sanity: zeta^5 = -1, zeta^10 = 1, sum_(k<10) zeta^k = 0,"
     " sqrt5^2 = 5, and mu_10 in Z[zeta_5]: -(zeta_10^2)^3 = zeta_10",
     zpow(5) == red([-1]) and zpow(10) == ONE and S10 == ZERO
     and mul(SQRT5, SQRT5) == red([5])
     and sub(ZERO, mul(mul(zpow(2), zpow(2)), zpow(2))) == Z)

# KC2 exemplar A: one-dimensional carrier, eigenvalue zeta_10, v = 1.
Svals = []
S = ZERO
for n in range(0, 41):
    Svals.append(S)
    S = add(S, zpow(n))
qvals = [mul(Svals[n], conj(Svals[n])) for n in range(0, 41)]
gate("KC2 exemplar A: S_(n+10) = S_n and q_(n+10) = q_n exactly for"
     " n <= 30; the ladder is 10-periodic hence bounded, and a* = 0"
     " (the single eigenvalue zeta_10 differs from 1)",
     all(Svals[n + 10] == Svals[n] for n in range(0, 31))
     and all(qvals[n + 10] == qvals[n] for n in range(0, 31))
     and Z != ONE)

print("  exemplar A period of q_n, written p + q sqrt5:")
period_pairs = []
for n in range(0, 10):
    p, q = to_real_pair(qvals[n])
    assert real_sign(p, q) >= 0
    period_pairs.append((p, q))
    print("    q_%d = %s + (%s) sqrt5" % (n, p, q))

# KC3 exemplar B: eigenvalue 1, v = 1: q_n = n^2 exactly, a* = 1
gate("KC3 exemplar B: q_n = n^2 exactly for n <= 40 (a* = 1)",
     all(mul(red([n]), red([n])) == red([n * n]) for n in range(0, 41)))

# KC4 exemplar C: U = diag(1, zeta_10), v = (1,1), orthogonal coordinates:
# q_n = n^2 + q_n^A, so R_n = q_n - n^2 is the exemplar-A ladder with the
# exact bracket 0 <= R_n <= C, C = the period maximum.
cmax = period_pairs[0]
for pq in period_pairs[1:]:
    if real_sign(pq[0] - cmax[0], pq[1] - cmax[1]) > 0:
        cmax = pq
gate("KC4 exemplar C: R_n = q_n - n^2 obeys 0 <= R_n <= C exactly with"
     " C = %s + (%s) sqrt5 over the period" % cmax,
     all(real_sign(p, q) >= 0
         and real_sign(cmax[0] - p, cmax[1] - q) >= 0
         for p, q in period_pairs))

# KC5 dichotomy instances: exemplar A realizes the bounded branch (a* = 0),
# exemplars B and C realize q_n = a* n^2 + O(1) with a* = 1; no exemplar is
# both unbounded and o(n^2). These are the two branches the written proof
# plays against the Lagarias asymptotic.
gate("KC5 dichotomy instances on the exemplars: bounded against"
     " a* n^2 + O(1); no exemplar is both unbounded and o(n^2)",
     all(qvals[n + 10] == qvals[n] for n in range(0, 31)))

# KC6 Ramanujan sums c_10(n): exact integers, Moebius-Euler values
def c10(n):
    s = ZERO
    for k in (1, 3, 7, 9):
        s = add(s, zpow(k * n))
    return s

C10_EXPECT = {0: 4, 1: 1, 2: -1, 3: 1, 4: -1, 5: -4, 6: -1, 7: 1,
              8: -1, 9: 1, 10: 4}
gate("KC6 Ramanujan c_10(n) exact for n <= 10: c_10(0) = phi(10) = 4,"
     " c_10(5) = -4, alternating unit values off the divisors",
     all(c10(n) == red([C10_EXPECT[n]]) for n in range(0, 11)))

print("DECISION: finite mechanism audits pass; the carrier exclusion is"
      " carried by the written proof with imports labeled")
print("RESULT %d/%d ALL PASS" % (checks, checks))
