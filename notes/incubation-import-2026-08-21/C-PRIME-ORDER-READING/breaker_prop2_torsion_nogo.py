#!/usr/bin/env python3
# breaker_prop2_torsion_nogo.py
#
# Independent attack on PROP-2 (torsion no-go), PROP-2b (isogeny-stable
# separation) and the proposed PROP-2c (Q-linear independence) of
# claude/PROOF-PROP-2-RAPIDITY-TORSION-NOGO_2026-08-11.md.
#
# NON-CANONICAL. This is a breaker, not evidence for a universal statement.
# Python standard library only. Exact integer arithmetic. No float anywhere,
# not in assertions and not in the search steering: the candidate exponent n
# is located by exact sign comparisons in Z[phi], so every branch is certified.
#
# Independence from the reviewed text: the breaker never uses Lemma E. It
# tests equality of place-1 absolute values by exact sign determination, and
# only afterwards asks whether the two elements really agree up to sign. If
# Lemma E were false, the two answers would disagree and the run would say so.
#
# Representation: x = (a, b) means a + b*phi in O = Z[phi], phi^2 = phi + 1.
# Place 1 sends phi to (1+sqrt5)/2, place 2 sends phi to (1-sqrt5)/2.

import hashlib
import sys

ONE = (1, 0)
PHI = (0, 1)


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def neg(x):
    return (-x[0], -x[1])


def conj(x):
    a, b = x
    return (a + b, -b)


def norm(x):
    a, b = x
    return a * a + a * b - b * b


def power(x, k):
    assert k >= 0
    r = ONE
    base = x
    while k:
        if k & 1:
            r = mul(r, base)
        base = mul(base, base)
        k >>= 1
    return r


def sign1(x):
    """Exact sign of the place-1 image of a + b*phi. Integer arithmetic only."""
    a, b = x
    s = 2 * a + b           # place-1 image is (s + b*sqrt5) / 2
    if s == 0 and b == 0:
        return 0
    if s >= 0 and b >= 0:
        return 1
    if s <= 0 and b <= 0:
        return -1
    if s > 0:               # b < 0: positive iff s > |b|*sqrt5
        return 1 if s * s > 5 * b * b else -1
    return -1 if s * s > 5 * b * b else 1   # s < 0, b > 0


def absval(x):
    """Representative with positive place-1 image."""
    return x if sign1(x) > 0 else neg(x)


def cmp1(x, y):
    """Exact comparison of place-1 images."""
    return sign1((x[0] - y[0], x[1] - y[1]))


def find_exponent(A, C):
    """Locate the unique integer n, if any, with |A|_1 = |C|_1 * phi^(2n).

    Returns (n, True) on an exact hit, (None, False) otherwise. Exact
    throughout: the bracket is found by doubling and bisection on exact sign
    comparisons, never by a logarithm.
    """
    A = absval(A)
    C = absval(C)
    assert sign1(A) > 0 and sign1(C) > 0

    def g(n):
        # sign of |A|_1 - |C|_1 * phi^(2n), cleared of negative powers
        if n >= 0:
            return cmp1(A, mul(C, power(PHI, 2 * n)))
        return cmp1(mul(A, power(PHI, -2 * n)), C)

    s0 = g(0)
    if s0 == 0:
        return 0, True
    if s0 > 0:
        lo, hi = 0, 1
        while g(hi) > 0:
            lo, hi = hi, hi * 2 if hi else 1
            if hi > 4096:
                raise RuntimeError("runaway bracket")
        if g(hi) == 0:
            return hi, True
    else:
        hi, lo = 0, -1
        while g(lo) < 0:
            hi, lo = lo, lo * 2
            if lo < -4096:
                raise RuntimeError("runaway bracket")
        if g(lo) == 0:
            return lo, True
    while hi - lo > 1:
        mid = (lo + hi) // 2
        s = g(mid)
        if s == 0:
            return mid, True
        if s > 0:
            lo = mid
        else:
            hi = mid
    return None, False


def equals_up_to_sign(A, C, n):
    """Exact element test A == +-C*phi^(2n) in O."""
    if n >= 0:
        R = mul(C, power(PHI, 2 * n))
        L = A
    else:
        R = C
        L = mul(A, power(PHI, -2 * n))
    return L == R or L == neg(R)


def relation_hit(num, den):
    """Is num/den = +- phi^(2n) for some integer n? Exact."""
    n, found = find_exponent(num, den)
    if not found:
        return None
    return (n, equals_up_to_sign(num, den, n))


def is_prime(k):
    if k < 2:
        return False
    d = 2
    while d * d <= k:
        if k % d == 0:
            return False
        d += 1
    return True


def generator(p):
    """A generator w of one prime above a split p, |N(w)| = p. Brute force."""
    K = 1
    while K * K <= 4 * p + 4:
        K += 1
    K *= 2
    for b in range(0, K):
        for a in range(-K, K + 1):
            if abs(norm((a, b))) == p:
                return (a, b)
    return None


def split_primes(limit):
    return [p for p in range(2, limit + 1)
            if is_prime(p) and p % 5 in (1, 4)]


LINES = []


def say(s=""):
    LINES.append(s)


def torsion_hit(w, m):
    """Does m*r(P) = 0 hold, i.e. (w/sigma w)^m = +- phi^(2n)?"""
    return relation_hit(power(w, m), power(conj(w), m))


def pair_hit(wp, wq, m, opposite):
    """m*r(P) = -+ m*r(Q).  opposite=False: same orientation."""
    if opposite:
        num = mul(power(wp, m), power(wq, m))
        den = mul(power(conj(wp), m), power(conj(wq), m))
    else:
        num = mul(power(wp, m), power(conj(wq), m))
        den = mul(power(conj(wp), m), power(wq, m))
    return relation_hit(num, den)


def combo_hit(ws, coeffs):
    """Is prod (w_i/sigma w_i)^(m_i) = +- phi^(2n)?"""
    num, den = ONE, ONE
    for w, m in zip(ws, coeffs):
        if m > 0:
            num = mul(num, power(w, m))
            den = mul(den, power(conj(w), m))
        elif m < 0:
            num = mul(num, power(conj(w), -m))
            den = mul(den, power(w, -m))
    return relation_hit(num, den)


def vectors(k, lo, hi):
    if k == 0:
        yield ()
        return
    for head in range(lo, hi + 1):
        for tail in vectors(k - 1, lo, hi):
            yield (head,) + tail


def main():
    say("BREAKER PROP-2 / PROP-2b / PROP-2c   exact, stdlib, no float")
    say("field Q(sqrt5), O = Z[phi], phi^2 = phi + 1")
    say()

    # ---- structural self-checks -------------------------------------
    say("[S] structural identities")
    say("  sigma(phi)*(-phi) == 1        : %s" % (mul(conj(PHI), neg(PHI)) == ONE))
    say("  N(phi) == -1                  : %s" % (norm(PHI) == -1))
    say("  phi^2 == phi + 1              : %s" % (power(PHI, 2) == (1, 1)))
    say("  sqrt5 = 2phi-1, N == -5       : %s" % (norm((-1, 2)) == -5))
    say()

    # ---- positive controls ------------------------------------------
    # The search must FIND a relation where one demonstrably exists.
    say("[C] positive controls (a silent breaker is a broken breaker)")
    ctrl = []
    ctrl.append(("synthetic A = phi^6 * C, expect n=3",
                 relation_hit(mul(power(PHI, 6), (3, 5)), (3, 5)) == (3, True)))
    ctrl.append(("synthetic A = -phi^(-4) * C, expect n=-2",
                 relation_hit(neg((7, 2)), mul((7, 2), power(PHI, 4))) == (-2, True)))
    inert = [p for p in range(2, 60) if is_prime(p) and p % 5 in (2, 3)]
    ok = all(torsion_hit((p, 0), m) == (0, True) for p in inert for m in (1, 2, 3, 7))
    ctrl.append(("inert primes %s sit at the zero class" % inert[:5], ok))
    ram = (-1, 2)                                   # sqrt5
    ctrl.append(("ramified 5: sqrt5 sits at the zero class",
                 all(torsion_hit(ram, m) == (0, True) for m in (1, 2, 3, 7))))
    w11 = generator(11)
    ctrl.append(("same p, opposite orientation P vs sigma(P) always collides",
                 all(pair_hit(w11, conj(w11), m, True) is not None
                     for m in range(1, 13))))
    for name, good in ctrl:
        say("  %-58s : %s" % (name, "FOUND" if good else "MISSED"))
    if not all(g for _, g in ctrl):
        say("  CONTROL FAILURE. Nothing below is trustworthy.")
        return 1
    say()

    P_MAX = 300
    sp = split_primes(P_MAX)
    gens = {}
    say("[G] generators for the %d split primes below %d" % (len(sp), P_MAX))
    bad = 0
    for p in sp:
        w = generator(p)
        if w is None or abs(norm(w)) != p:
            bad += 1
            continue
        gens[p] = w
    say("  class number one witnessed: every split p has a generator : %s"
        % (bad == 0 and len(gens) == len(sp)))
    say("  norms |N(w)| = p verified exactly                         : True")
    say()

    # ---- gauge invariance -------------------------------------------
    say("[I] gauge invariance of the verdict (generator change, orientation)")
    gauge_bad = 0
    for p in sp[:8]:
        w = gens[p]
        for alt in (mul(w, PHI), mul(w, power(PHI, 3)), neg(w), conj(w),
                    mul(conj(w), neg(PHI))):
            for m in (1, 2, 3, 5):
                a = torsion_hit(w, m) is not None
                b = torsion_hit(alt, m) is not None
                if a != b:
                    gauge_bad += 1
    say("  verdict changed under a gauge move                        : %d" % gauge_bad)
    say()

    # ---- T2  PROP-2 --------------------------------------------------
    M1 = 64
    say("[T2] PROP-2 torsion no-go: m*r(P) = 0 for 1 <= m <= %d" % M1)
    hits, tests, lemE = [], 0, 0
    for p in sp:
        for m in range(1, M1 + 1):
            tests += 1
            h = torsion_hit(gens[p], m)
            if h is not None:
                hits.append((p, m, h))
                if not h[1]:
                    lemE += 1
    say("  tests                                                     : %d" % tests)
    say("  torsion hits                                              : %d" % len(hits))
    say("  place-1 equalities that were NOT +-phi^(2n) (Lemma E fail) : %d" % lemE)
    say()

    # ---- T2b  PROP-2b ------------------------------------------------
    M2 = 16
    say("[T2b] PROP-2b separation: m*r(P) = +- m*r(Q), p != q, 1 <= m <= %d" % M2)
    ph, tests2, lemE2 = [], 0, 0
    for i in range(len(sp)):
        for j in range(i + 1, len(sp)):
            wp, wq = gens[sp[i]], gens[sp[j]]
            for m in range(1, M2 + 1):
                for opp in (False, True):
                    tests2 += 1
                    h = pair_hit(wp, wq, m, opp)
                    if h is not None:
                        ph.append((sp[i], sp[j], m, opp, h))
                        if not h[1]:
                            lemE2 += 1
    say("  tests                                                     : %d" % tests2)
    say("  collisions                                                : %d" % len(ph))
    say("  place-1 equalities that were NOT +-phi^(2n) (Lemma E fail) : %d" % lemE2)
    say()

    # ---- T2c  proposed PROP-2c --------------------------------------
    say("[T2c] proposed PROP-2c: sum_i m_i t_i = n log phi, boxes over split p")
    boxes = [(sp[:6], 2), (sp[:4], 4), (sp[6:11], 3)]
    ch, tests3, lemE3 = [], 0, 0
    for prs, R in boxes:
        ws = [gens[p] for p in prs]
        for v in vectors(len(prs), -R, R):
            if all(c == 0 for c in v):
                continue
            tests3 += 1
            h = combo_hit(ws, v)
            if h is not None:
                ch.append((prs, v, h))
                if not h[1]:
                    lemE3 += 1
        say("  box %-28s coeffs in [-%d,%d]" % (str(prs), R, R))
    say("  tests                                                     : %d" % tests3)
    say("  relations found                                           : %d" % len(ch))
    say("  place-1 equalities that were NOT +-phi^(2n) (Lemma E fail) : %d" % lemE3)
    say()

    broken = len(hits) + len(ph) + len(ch) + gauge_bad + bad
    say("VERDICT")
    say("  controls found                                            : %d/%d"
        % (sum(1 for _, g in ctrl if g), len(ctrl)))
    say("  total certified tests                                     : %d"
        % (tests + tests2 + tests3))
    say("  counterexamples                                           : %d" % broken)
    say("  status                                                    : %s"
        % ("PROP-2, PROP-2b, PROP-2c SURVIVED at audited range"
           if broken == 0 else "BROKEN"))
    return 0


if __name__ == "__main__":
    rc = main()
    text = "\n".join(LINES) + "\n"
    sys.stdout.write(text)
    sys.stdout.write("stdout_sha256_of_the_above = %s\n"
                     % hashlib.sha256(text.encode()).hexdigest())
    sys.exit(rc)
