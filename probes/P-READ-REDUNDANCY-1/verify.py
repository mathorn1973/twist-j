#!/usr/bin/env python3
# verify.py for probes/P-READ-REDUNDANCY-1
# Preregistration: probes/P-READ-REDUNDANCY-1/PREREG.md, issue 216.
# Python 3 standard library only. Exact arithmetic: int and Fraction only,
# Q(sqrt5) as exact pairs (a, b) meaning a + b*sqrt5. No float anywhere in any
# assertion or any emitted field. Deterministic output. Exit 0 iff every gate
# passes.

import itertools
import sys
from fractions import Fraction
from math import factorial, floor

RESULTS = []


def check(tag, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "%s %s" % (tag, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


# --------------------------------------------------------------- partitions
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


# ------------------------------------------------------------------ rings
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
    """q a Fraction. True iff q lies in Z_S, that is Z localized at the primes
    S. S is None for Q, where every prime is inverted."""
    if S is None:
        return True
    return prime_factors(q.denominator) <= set(S)


print("P-READ-REDUNDANCY-1 verifier")
print("basis: Public Canon v27, tag canon-v27, content commit 116b62ed")
print("scope: A no-feedback tolerance; B prime-support bound; C fences")
print("arithmetic: int and Fraction only; no float in this file")
print("")

# ===================================================================== A
# A. Absence of feedback alone does not bound finite read redundancy.

# A1: composition closure. A three-node funnel equals its polynomial.
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
    if funnel_sample(x1, x2) != (x1 + x2) ** 2 - 3:
        ok = False
check("A1 composition closure: funnel equals its polynomial, 10 points", ok)


# A2: the TYPED witness at m = 6. Six ports typed by the offset unit-interval
# index; the funnel is a wire from the type-0 port to the output. Zero
# arithmetic nodes, so the map is total, acyclic, feedback free and integral.
def w6_typed(ports):
    """ports: list of (type_k, value). Output: the value at type 0."""
    out = None
    for k, val in ports:
        if k == 0:
            out = val
    return out


ok = True
values = [Fraction(0), Fraction(1), Fraction(-2, 3), Fraction(355, 113),
          Fraction(10 ** 12 + 7, 998244353), Fraction(-89, 55)]
values_s5 = [(Fraction(1, 5), Fraction(2, 5)),
             (Fraction(0), Fraction(1)),
             (Fraction(-3, 4), Fraction(7, 11))]
perms = [(0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0), (2, 0, 5, 1, 4, 3),
         (1, 2, 3, 4, 5, 0), (3, 1, 4, 0, 5, 2), (2, 5, 0, 4, 1, 3),
         (1, 0, 3, 2, 5, 4), (4, 2, 5, 3, 0, 1)]
types6 = [-3, -2, -1, 0, 1, 2]
for v in values + values_s5:
    for pm in perms:
        if w6_typed([(types6[i], v) for i in pm]) != v:
            ok = False
check("A2 TYPED witness carries m = 6 over Z, 8 port orders, Q and Q(sqrt5)",
      ok, "%d values" % len(values + values_s5))

# A3: the sixfold cover exists and its offsets are translation invariant with
# distinct unit-interval types.
ok = True
for x in (Fraction(7, 3), Fraction(-5, 4), Fraction(22, 7), Fraction(355, 113)):
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
        if offs != offs0 or sorted(floor(o) for o in offs) != types6:
            ok = False
check("A3 sixfold cover: 6 sheets, shift-invariant offsets, distinct types",
      ok)


# A4: the PART pole. The diagonal common-value map carries every m. It relies
# on equality of the copies and never verifies it; verification would be the
# reconciliation channel.
def diag_read(t):
    return t[0]


ok = True
for m in range(1, 9):
    for v in (Fraction(4, 9), Fraction(-1), Fraction(17)):
        t = (v,) * m
        if len(set(t)) != 1 or diag_read(t) != v:
            ok = False
check("A4 PART pole: diagonal common-value map carries every m in 1..8", ok)

# A5: the WALL. Over Q every multiplicity carries, so the graph never
# obstructs; the ring does.
ok = all(in_ZS(Fraction(1, m), None) for m in range(1, 13))
check("A5 WALL: over Q every m in 1..12 carries", ok)

# ===================================================================== B
# B. CARRY(m, ANON+TOTAL, Z_S) holds iff every prime factor of m lies in S.

# B1: orbit counts, closed formula against explicit enumeration.
ok = True
for m in (1, 2, 5, 6):
    for weight in (1, 2, 3, 4):
        for lam in partitions(weight, m):
            if orbit_count_formula(lam, m) != orbit_count_enum(lam, m):
                ok = False
check("B1 orbit counts formula equals enumeration, m in {1,2,5,6}, "
      "weight <= 4", ok)

# B2: the weight-1 stratum is exactly {(1)} with orbit count m, and every
# basis element has diagonal degree equal to its weight. This is the stratum
# structure the symbolic necessity proof uses.
ok = True
for m in (1, 2, 5, 6):
    if partitions(1, m) != [(1,)] or orbit_count_formula((1,), m) != m:
        ok = False
    for weight in (1, 2, 3, 4):
        for lam in partitions(weight, m):
            cnt = orbit_count_formula(lam, m)
            for v in (Fraction(7), Fraction(-3, 2)):
                if msym_eval(lam, (v,) * m) != cnt * v ** weight:
                    ok = False
check("B2 weight-1 stratum is {(1)} with orbit m; diagonal degree = weight",
      ok)

# B3: the ring table, against the prime-support rule and against hand cells.
ok = True
for m in (1, 2, 3, 4, 5, 6, 10, 12):
    for S in (frozenset(), frozenset({2}), frozenset({5}),
              frozenset({2, 5}), frozenset({2, 3, 5})):
        if in_ZS(Fraction(1, m), S) != (prime_factors(m) <= S):
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
check("B3 ring table: 1/m in Z_S iff primes(m) subset S, hand cells agree",
      ok)

# B4: sufficiency witnesses P = e_1/m over the minimal ring.
ok = True
for m, S in ((1, frozenset()), (2, frozenset({2})), (5, frozenset({5})),
             (6, frozenset({2, 3, 5})), (10, frozenset({2, 5}))):
    coeff = Fraction(1, m)
    if not in_ZS(coeff, S):
        ok = False
    for v in (Fraction(9, 7), Fraction(-11, 4), Fraction(0), Fraction(5)):
        if coeff * msym_eval((1,), (v,) * m) != v:
            ok = False
check("B4 sufficiency: P = e_1/m carries m over Z_S with primes(m) in S", ok)


# B5: necessity by exhaustion at m = 2. Independent code path: candidates are
# evaluated semantically on the diagonal; the coefficient argument of B2 is
# not reused.
def msym_diag_int(lam, m, v):
    padded = tuple(list(lam) + [0] * (m - len(lam)))
    total = 0
    for perm in set(itertools.permutations(padded)):
        term = 1
        for e in perm:
            term *= v ** e
        total += term
    return total


lams2 = [(1,), (2,), (1, 1), (3,), (2, 1), (4,), (3, 1), (2, 2)]
VS = (1, 2, 3, 4, 5)
D2 = {lam: tuple(msym_diag_int(lam, 2, v) for v in VS) for lam in lams2}
hits = []
count = 0
for coeffs in itertools.product(range(-2, 3), repeat=len(lams2)):
    count += 1
    s = 0
    for c, lam in zip(coeffs, lams2):
        if c:
            s += c * D2[lam][0]
    if s != 1:
        continue
    good = True
    for vi in range(1, len(VS)):
        s = 0
        for c, lam in zip(coeffs, lams2):
            if c:
                s += c * D2[lam][vi]
        if s != VS[vi]:
            good = False
            break
    if good:
        hits.append(coeffs)
check("B5 necessity at m = 2: %d integer symmetric candidates" % count,
      not hits, "zero satisfy the diagonal identity" if not hits
      else str(hits[:3]))

# B6: necessity by exhaustion at m = 6, dyadic power-sum family
# (a p_1 + b p_1^2 + c p_2)/2^k. Diagonal: p_1 = 6v, p_1^2 = 36 v^2,
# p_2 = 6 v^2.
hits = []
count = 0
for k in range(0, 7):
    two_k = 2 ** k
    for a in range(-32, 33):
        base = 6 * a
        for b in range(-32, 33):
            for c in range(-32, 33):
                count += 1
                quad = 36 * b + 6 * c
                if base + quad != two_k:
                    continue
                if 12 * a + 4 * quad != 2 * two_k:
                    continue
                if 18 * a + 9 * quad != 3 * two_k:
                    continue
                hits.append((a, b, c, k))
check("B6 necessity at m = 6, dyadic power-sum family: %d candidates" % count,
      not hits, "zero satisfy the diagonal identity" if not hits
      else str(hits[:3]))

# B7: necessity by exhaustion at m = 6, dyadic elementary family
# (a e_1 + b e_2 + c e_3)/2^k. Diagonal: e_1 = 6v, e_2 = 15 v^2, e_3 = 20 v^3.
# Tested semantically at v in {1,2,3} without using the structural insight.
hits = []
count = 0
for k in range(0, 7):
    two_k = 2 ** k
    for a in range(-32, 33):
        for b in range(-32, 33):
            for c in range(-32, 33):
                count += 1
                good = True
                for v in (1, 2, 3):
                    if a * 6 * v + b * 15 * v * v + c * 20 * v ** 3 \
                            != two_k * v:
                        good = False
                        break
                if good:
                    hits.append((a, b, c, k))
check("B7 necessity at m = 6, dyadic elementary family: %d candidates" % count,
      not hits, "zero satisfy the diagonal identity" if not hits
      else str(hits[:3]))

# B8: independent cross-check of one ring cell, by a route that does not use
# the prime-support rule: solve 6a = 10^k directly.
found = [(a, k) for k in range(0, 13)
         for a in [10 ** k // 6] if 6 * a == 10 ** k]
independent_no = not found
rule_no = not ({2, 3} <= {2, 5})
check("B8 cross-check 1/6 in Z[1/10]: direct scan agrees with the rule",
      independent_no == rule_no,
      "both say no" if independent_no and rule_no else "MISMATCH")

# ===================================================================== C
# C. Fences. The result informs MINIMAL-READ-DERIVATION and nothing more.

# C1: the registered places.
S25 = frozenset({2, 5})
ok = in_ZS(Fraction(1, 1), frozenset())            # rung w = 1, free over Z
ok = ok and in_ZS(Fraction(1, 2), frozenset({2}))  # generic w = 1, read place
ok = ok and not in_ZS(Fraction(1, 6), S25)         # generic w = 3, obstructed
ok = ok and in_ZS(Fraction(1, 5), S25)             # rung w = 3, write place
ok = ok and not in_ZS(Fraction(1, 5), frozenset({2}))
check("C1 registered places: m=1 free; m=2 needs 2; m=6 needs 3 and is "
      "obstructed; m=5 needs 5", ok)

# C2: the blindness table. The selector is a prime-support selector, not a
# smaller-is-better principle: on {6,10} it forces the LARGER cover.
carr = lambda m: in_ZS(Fraction(1, m), S25)
ok = (carr(2), carr(6)) == (True, False)
ok = ok and (carr(2), carr(10)) == (True, True)
ok = ok and (carr(6), carr(10)) == (False, True)
check("C2 blindness: {2,6} forces 2; {2,10} nonunique; {6,10} forces 10", ok)

# C3: the range asymmetry, exact. Recorded so the m = 2 exclusion is not
# claimed to rest on the coherent range.
b1sq = Fraction(1, 5)
ok = (36 * b1sq > 1) and (4 * b1sq < 1)
check("C3 range: (6 beta_1)^2 = 36/5 > 1; (2 beta_1)^2 = 4/5 < 1", ok)

print("")
npass = sum(1 for r in RESULTS if r)
print("SUMMARY %d/%d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
