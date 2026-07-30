#!/usr/bin/env python3
# verify_read_redundancy_1.py
# C-READ-REDUNDANCY-1 verifier. Prereg: claude/PREREG-C-READ-REDUNDANCY-1.md
# (sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2).
# Python 3 stdlib only. Exact arithmetic: int and Fraction only, Q(sqrt5)
# as exact pairs (a, b) = a + b*sqrt5. No float anywhere. Exit 0 iff all
# checks pass.

import sys
import itertools
from fractions import Fraction
from math import factorial, floor

RESULTS = []


def check(tag, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "%s %s" % (tag, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


# ------------------------------------------------------------- partitions
def partitions(weight, max_parts):
    """All partitions of exactly `weight` into at most `max_parts` parts."""
    out = []

    def gen(n, k, largest, acc):
        if n == 0:
            out.append(tuple(acc))
            return
        if k == 0:
            return
        for first in range(min(n, largest), 0, -1):
            acc.append(first)
            gen(n - first, k - 1, first, acc)
            acc.pop()

    gen(weight, max_parts, weight, [])
    return out


def orbit_count_formula(lam, m):
    padded = list(lam) + [0] * (m - len(lam))
    denom = 1
    for val in set(padded):
        denom *= factorial(padded.count(val))
    return factorial(m) // denom


def orbit_count_enum(lam, m):
    padded = tuple(list(lam) + [0] * (m - len(lam)))
    return len(set(itertools.permutations(padded)))


def msym_eval(lam, xs):
    """Monomial symmetric polynomial m_lam at tuple xs, by explicit orbit."""
    m = len(xs)
    padded = tuple(list(lam) + [0] * (m - len(lam)))
    total = Fraction(0)
    for perm in set(itertools.permutations(padded)):
        term = Fraction(1)
        for x, e in zip(xs, perm):
            term *= Fraction(x) ** e
        total += term
    return total


# ------------------------------------------------------------- rings Z_S
def prime_factors(n):
    n = abs(n)
    ps = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            ps.add(d)
            n //= d
        d += 1
    if n > 1:
        ps.add(n)
    return ps


def in_ZS(q, S):
    """q a Fraction. True iff q lies in Z_S = Z localized at the primes S.
    S == None encodes Q (every prime inverted)."""
    if S is None:
        return True
    return prime_factors(q.denominator) <= set(S)


print("C-READ-REDUNDANCY-1 verifier")
print("basis: Public Canon v27, tag canon-v27, content commit 116b62ed")
print("arithmetic: int and Fraction only; no float in this file")
print("")

# K1: composition closure sample. A three-node funnel equals its polynomial.
def funnel_sample(x1, x2):
    n1 = x1 + x2            # node: addition
    n2 = n1 * n1            # node: multiplication
    n3 = n2 + Fraction(-3)  # node: constant addition, constant in Z
    return n3


ok = True
pts = [(Fraction(a, b), Fraction(c, d))
       for a, b, c, d in [(0, 1, 0, 1), (1, 1, 2, 1), (-3, 2, 5, 7),
                          (22, 7, -1, 3), (10, 3, 10, 3),
                          (-100, 9, 41, 11), (1, 2, 1, 2),
                          (7, 5, -7, 5), (123, 4, 5, 6), (-8, 1, 9, 1)]]
for x1, x2 in pts:
    direct = (x1 + x2) ** 2 - 3
    if funnel_sample(x1, x2) != direct:
        ok = False
check("K1 composition-closure sample (funnel = polynomial), 10 points", ok)

# K2: orbit counts, formula versus explicit enumeration.
ok = True
for m in (1, 2, 5, 6):
    for weight in (1, 2, 3, 4):
        for lam in partitions(weight, m):
            if orbit_count_formula(lam, m) != orbit_count_enum(lam, m):
                ok = False
check("K2 orbit counts formula = enumeration, m in {1,2,5,6}, weight <= 4", ok)

# K3: weight-1 stratum is exactly {(1)} with orbit count m, and every basis
# element has diagonal degree equal to its weight (checked by evaluation).
ok = True
for m in (1, 2, 5, 6):
    if partitions(1, m) != [(1,)]:
        ok = False
    if orbit_count_formula((1,), m) != m:
        ok = False
    for weight in (1, 2, 3, 4):
        for lam in partitions(weight, m):
            cnt = orbit_count_formula(lam, m)
            for v in (Fraction(7), Fraction(-3, 2)):
                if msym_eval(lam, (v,) * m) != cnt * v ** weight:
                    ok = False
check("K3 weight-1 stratum = {(1)}, orbit m; diagonal degree = weight", ok)

# K4: ring membership table for 1/m, against prime-support rule and by hand.
ok = True
for m in (1, 2, 3, 4, 5, 6, 10, 12):
    for S in (frozenset(), frozenset({2}), frozenset({5}),
              frozenset({2, 5}), frozenset({2, 3, 5})):
        got = in_ZS(Fraction(1, m), S)
        want = prime_factors(m) <= S
        if got != want:
            ok = False
hand = [
    (2, frozenset({2}), True), (2, frozenset(), False),
    (6, frozenset({2, 5}), False), (6, frozenset({2, 3, 5}), True),
    (5, frozenset({2, 5}), True), (10, frozenset({2, 5}), True),
    (3, frozenset({2, 5}), False), (1, frozenset(), True),
    (5, frozenset({2}), False),
]
for m, S, want in hand:
    if in_ZS(Fraction(1, m), S) != want:
        ok = False
check("K4 ring table: 1/m in Z_S iff primes(m) subset S; hand cells agree", ok)

# K5: sufficiency witnesses P = e_1/m over the minimal ring.
ok = True
for m, S in ((1, frozenset()), (2, frozenset({2})), (5, frozenset({5})),
             (6, frozenset({2, 3, 5})), (10, frozenset({2, 5}))):
    coeff = Fraction(1, m)
    if not in_ZS(coeff, S):
        ok = False
    for v in (Fraction(9, 7), Fraction(-11, 4), Fraction(0), Fraction(5)):
        if coeff * msym_eval((1,), (v,) * m) != v:
            ok = False
check("K5 sufficiency: P = e_1/m carries m over Z_S with primes(m) in S", ok)

# K6: TYPED witness W6. Six ports typed by the offset unit-interval index;
# the funnel is a wire from the type-0 port to the output. Zero arithmetic.
def w6_typed(ports):
    """ports: list of (type_k, value). Output: value at type 0."""
    out = None
    for k, val in ports:
        if k == 0:
            out = val
    return out


def sqrt5_mul(p, q):
    return (p[0] * q[0] + 5 * p[1] * q[1], p[0] * q[1] + p[1] * q[0])


ok = True
values = [Fraction(0), Fraction(1), Fraction(-2, 3), Fraction(355, 113),
          Fraction(10 ** 12 + 7, 998244353), Fraction(-89, 55)]
values_s5 = [(Fraction(1, 5), Fraction(2, 5)),
             (Fraction(0), Fraction(1)),
             (Fraction(-3, 4), Fraction(7, 11))]
perms = [(0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0), (2, 0, 5, 1, 4, 3),
         (1, 2, 3, 4, 5, 0)]
types6 = [-3, -2, -1, 0, 1, 2]
for v in values + values_s5:
    for pm in perms:
        ports = [(types6[i], v) for i in pm]
        if w6_typed(ports) != v:
            ok = False
check("K6a W6 typed projection returns v, all port orders, Q and Q(sqrt5)", ok)

# K6b: the sixfold cover exists and its offsets are translation invariant
# with distinct unit-interval types.
ok = True
for x in (Fraction(7, 3), Fraction(-5, 4), Fraction(22, 7),
          Fraction(355, 113)):
    for shift in (0, 1, 5):
        y = x + shift
        ns = [n for n in range(floor(y) - 3, floor(y) + 5)
              if abs(y - n) < 3 and y != n]
        if len(ns) != 6:
            ok = False
            continue
        offs = sorted(y - n for n in ns)
        offs0 = sorted(x - n for n in
                       [n for n in range(floor(x) - 3, floor(x) + 5)
                        if abs(x - n) < 3 and x != n])
        if offs != offs0:
            ok = False
        if sorted(floor(o) for o in offs) != types6:
            ok = False
check("K6b sixfold cover: 6 sheets, offsets shift invariant, types distinct", ok)

# K7: W2 dyadic witness. P = (x1 + x2)/2, coefficients in Z[1/2].
ok = in_ZS(Fraction(1, 2), frozenset({2}))
for v in (Fraction(3, 7), Fraction(-9, 2), Fraction(0), Fraction(12)):
    if Fraction(1, 2) * (v + v) != v:
        ok = False
check("K7 W2 dyadic: (x1+x2)/2 carries m = 2 over Z[1/2]", ok)

# K8: PART pole. The diagonal common-value map carries every m.
def diag_read(t):
    return t[0]


ok = True
for m in range(1, 9):
    for v in (Fraction(4, 9), Fraction(-1), Fraction(17)):
        t = (v,) * m
        if len(set(t)) != 1:
            ok = False
        if diag_read(t) != v:
            ok = False
check("K8 PART: diagonal common-value map carries every m in 1..8", ok)

# K9: blindness table over S = {2, 5}.
S25 = frozenset({2, 5})
carr = lambda m: in_ZS(Fraction(1, m), S25)
ok = (carr(2), carr(6)) == (True, False)      # forces the 2-cover
ok = ok and (carr(2), carr(10)) == (True, True)   # nonunique
ok = ok and (carr(6), carr(10)) == (False, True)  # forces the 10-cover
check("K9 blindness: {2,6} forces 2; {2,10} nonunique; {6,10} forces 10", ok)

# K10: the admissible pair, generic and rung multiplicities.
ok = in_ZS(Fraction(1, 1), frozenset())            # w=1 rung, free over Z
ok = ok and in_ZS(Fraction(1, 2), frozenset({2}))  # w=1 generic, read place
ok = ok and not in_ZS(Fraction(1, 6), S25)         # w=3 generic, obstructed
ok = ok and in_ZS(Fraction(1, 5), S25)             # w=3 rung, write place
ok = ok and not in_ZS(Fraction(1, 5), frozenset({2}))
check("K10 pair: m=1 free; m=2 needs prime 2; m=6 obstructed (needs 3); "
      "m=5 needs prime 5", ok)

# K11: WALL over Q: every multiplicity carries; the graph never obstructs.
ok = all(in_ZS(Fraction(1, m), None) for m in range(1, 13))
check("K11 WALL: over Q every m in 1..12 carries", ok)

# K12: range asymmetry, exact. (6 beta_1)^2 = 36/5 > 1; (2 beta_1)^2 = 4/5 < 1.
b1sq = Fraction(1, 5)
ok = (36 * b1sq > 1) and (4 * b1sq < 1)
check("K12 range: (6 beta_1)^2 = 36/5 > 1 exactly; (2 beta_1)^2 = 4/5 < 1", ok)

print("")
npass = sum(1 for r in RESULTS if r)
print("SUMMARY %d/%d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
