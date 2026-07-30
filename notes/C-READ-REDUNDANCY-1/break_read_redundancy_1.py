#!/usr/bin/env python3
# break_read_redundancy_1.py
# C-READ-REDUNDANCY-1 breaker: independent legs attacking the candidate.
# Prereg: claude/PREREG-C-READ-REDUNDANCY-1.md
# (sha256 334cb3bf9ef6feaccaa7e48c809e0f2f880c6686c025eee96474fb31c743d0d2).
# Python 3 stdlib only. Exact integer and Fraction arithmetic; no float.
# Exit 1 iff a falsifier fires (witness printed). Exit 0 otherwise.

import sys
import itertools
from fractions import Fraction

FIRED = []


def report(tag, fired, detail=""):
    line = "%s %s" % (tag, "FIRED" if fired else "no counterexample")
    if detail:
        line += "  " + detail
    print(line)
    if fired:
        FIRED.append(tag)


print("C-READ-REDUNDANCY-1 breaker")
print("independent code path; semantic evaluation, no reuse of the")
print("verifier's coefficient argument")
print("")

# --------------------------------------------------------------------- B1
# F1 attack: m = 2, ANON class. Monomial-symmetric basis, weight <= 4,
# integer coefficients in [-2, 2]. Semantic diagonal test at v in 1..5.
# The candidate says: no member satisfies P(v, v) = v on all five points.
lams2 = [(1,), (2,), (1, 1), (3,), (2, 1), (4,), (3, 1), (2, 2)]


def msym_diag_int(lam, m, v):
    """m_lam evaluated at (v, .., v) by explicit orbit enumeration, ints."""
    padded = tuple(list(lam) + [0] * (m - len(lam)))
    total = 0
    for perm in set(itertools.permutations(padded)):
        term = 1
        for e in perm:
            term *= v ** e
        total += term
    return total


VS = (1, 2, 3, 4, 5)
D2 = {lam: tuple(msym_diag_int(lam, 2, v) for v in VS) for lam in lams2}
hits = []
count = 0
rng = range(-2, 3)
for coeffs in itertools.product(rng, repeat=len(lams2)):
    count += 1
    # semantic test at v = 1 first (cheap filter), then the rest
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
report("B1 (F1) m=2 symmetric integer accumulators, %d candidates" % count,
       bool(hits), str(hits[:3]) if hits else "zero satisfy the diagonal")

# --------------------------------------------------------------------- B2
# F4 attack: m = 6, dyadic ANON TOTAL family (a p1 + b p1^2 + c p2)/2^k,
# a, b, c in [-32, 32], k in 0..6. Diagonal: p1 = 6v, p1^2 = 36 v^2,
# p2 = 6 v^2. Semantic test at v in {1, 2, 3}.
hits = []
count = 0
for k in range(0, 7):
    two_k = 2 ** k
    for a in range(-32, 33):
        base = 6 * a  # v-linear part at v = 1 contribution: 6a
        for b in range(-32, 33):
            for c in range(-32, 33):
                count += 1
                quad = 36 * b + 6 * c
                # v = 1: 6a + quad = 2^k * 1
                if base + quad != two_k:
                    continue
                # v = 2: 12a + 4 quad = 2^k * 2 ; v = 3: 18a + 9 quad = 3*2^k
                if 12 * a + 4 * quad != 2 * two_k:
                    continue
                if 18 * a + 9 * quad != 3 * two_k:
                    continue
                hits.append((a, b, c, k))
report("B2 (F4) m=6 dyadic power-sum family, %d candidates" % count,
       bool(hits), str(hits[:3]) if hits else "zero satisfy the diagonal")

# --------------------------------------------------------------------- B2b
# F4 attack, second family: elementary symmetric (a e1 + b e2 + c e3)/2^k.
# Diagonal at m = 6: e1 = 6v, e2 = 15 v^2, e3 = 20 v^3.
hits = []
count = 0
for k in range(0, 7):
    two_k = 2 ** k
    for a in range(-32, 33):
        for b in range(-32, 33):
            for c in range(-32, 33):
                count += 1
                # identity in v needs: 6a = 2^k, 15b = 0, 20c = 0 ; test
                # semantically at v in {1, 2, 3} without using that insight
                ok = True
                for v in (1, 2, 3):
                    if a * 6 * v + b * 15 * v * v + c * 20 * v ** 3 \
                            != two_k * v:
                        ok = False
                        break
                if ok:
                    hits.append((a, b, c, k))
report("B2b (F4) m=6 dyadic elementary family, %d candidates" % count,
       bool(hits), str(hits[:3]) if hits else "zero satisfy the diagonal")

# --------------------------------------------------------------------- B3
# F2 attack: the W6 typed projection witness, 50 exact values, fixed
# deterministic port permutations, large numerators, Q(sqrt5) pairs.
def w6_typed(ports):
    out = None
    for k, val in ports:
        if k == 0:
            out = val
    return out


types6 = [-3, -2, -1, 0, 1, 2]
vals = []
seed_nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
             1597, 2584, 4181, 6765, 10946]
for i, n in enumerate(seed_nums):
    vals.append(Fraction((-1) ** i * (n ** 3 + 7), 2 * n + 1))
    vals.append(Fraction(n * 10 ** 9 + 1, n + 3))
for a, b in [(1, 2), (0, 1), (-3, 7), (5, -5), (123, 456)]:
    vals.append((Fraction(a, 5), Fraction(b, 5)))  # a/5 + (b/5) sqrt5
vals.append(Fraction(0))
vals = vals[:50]
perms = [(0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0), (3, 1, 4, 0, 5, 2),
         (2, 5, 0, 4, 1, 3), (1, 0, 3, 2, 5, 4), (4, 2, 5, 3, 0, 1),
         (0, 2, 4, 1, 3, 5), (5, 3, 1, 4, 2, 0)]
bad = None
for v in vals:
    for pm in perms:
        ports = [(types6[i], v) for i in pm]
        if w6_typed(ports) != v:
            bad = (v, pm)
            break
    if bad:
        break
report("B3 (F2) W6 typed witness, 50 values x 8 port orders",
       bad is not None, str(bad) if bad else "output = v every time")

# --------------------------------------------------------------------- B4
# Repair attempts for the m = 6 carry inside integer style. Informational:
# their failure supports S3 and cannot fire a falsifier.
def strip_primes(n, primes):
    for p in primes:
        while n % p == 0 and n != 0:
            n //= p
    return n


r1_fail = all(strip_primes(6 * v, (2,)) != v for v in (1, 3, 5, 7))
r2_fail = all(strip_primes(6 * v, (2, 5)) != v for v in (1, 3, 7, 9))
print("B4 repair 1 (strip powers of 2 from 6v): %s"
      % ("fails, residue 3v" if r1_fail else "UNEXPECTEDLY WORKS"))
print("B4 repair 2 (strip powers of 2 and 5 from 6v): %s"
      % ("fails, factor 3 survives" if r2_fail else "UNEXPECTEDLY WORKS"))
if not (r1_fail and r2_fail):
    FIRED.append("B4")

# --------------------------------------------------------------------- B5
# F3 cross-check: is 1/6 in Z[1/10]? Independent route: solve 6 a = 10^k.
found = [(a, k) for k in range(0, 13)
         for a in [10 ** k // 6] if 6 * a == 10 ** k]
independent_no = not found
# verifier's route: prime support of 6 = {2, 3} is not inside {2, 5}
verifier_no = not ({2, 3} <= {2, 5})
report("B5 (F3) 1/6 in Z[1/10]: independent scan vs prime-support rule",
       independent_no != verifier_no,
       "both say NO" if independent_no and verifier_no else "MISMATCH")

print("")
if FIRED:
    print("FALSIFIER FIRED: %s" % ", ".join(FIRED))
    sys.exit(1)
print("NO FALSIFIER FIRED")
sys.exit(0)
