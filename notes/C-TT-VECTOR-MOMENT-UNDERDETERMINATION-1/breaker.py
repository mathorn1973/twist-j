#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
breaker.py
candidate C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1

An honest attempt to break S1(iv) and S2 on a code path that shares nothing
with verify.py. verify.py sums over enumerated configurations. This file never
enumerates a configuration: it evaluates every expectation in closed form by
character orthogonality on Z/5 and on {+1,-1}, then compares the two paths.

  law A   : E[ prod_x v_x^{p_x} conj(v_x)^{q_x} ]
            = 1 if p_x - q_x = 0 mod 5 for every x, else 0
  law B_0 : = 1 if sum_x (p_x - q_x) = 0 mod 5 and p_x + q_x even for every x,
            else 0

Break attempts:
  BRK-1  full sweep of all 1001 monomials of total degree <= 4 by closed form,
         looking for any separator at degree <= 3 that verify.py missed.
  BRK-2  independent derivation of the degree-4 separator set from the closed
         forms alone, compared against the predicted 20.
  BRK-3  cross-check of both closed forms against direct enumeration on every
         one of the 1001 monomials, on both laws.
  BRK-4  search for any deterministic-modulus law on one site with P = 0 that
         satisfies the Wick fourth moment, by exact reasoning on the modulus.
  BRK-5  a wider hypothesis sweep: for every m in Z/5 check whether B_m shares
         all degree <= 3 data with A, which would widen the counterexample
         family beyond the pair actually claimed.

Exact arithmetic only, integers and Fraction. No float anywhere.
Python standard library only.
"""

import sys
from fractions import Fraction
from itertools import product, combinations_with_replacement

N = 5
FAILS = []
GATES = 0


def gate(name, ok, detail=""):
    global GATES
    GATES += 1
    line = "BREAK %-46s %s" % (name, "PASS" if ok else "FAIL")
    if not ok:
        FAILS.append(name)
    if detail:
        line += "  " + detail
    print(line)


# ------------------------------------------------------- closed form path

def cf_A(p, q):
    """Closed form expectation under law A. Returns an integer, 0 or 1."""
    for x in range(N):
        if (p[x] - q[x]) % N != 0:
            return 0
    return 1


def cf_B(p, q, m):
    """Closed form expectation under law B_m. Integer 0 or 1 times z^power.

    v_x = z^{t0 + m x} eps_x. The monomial is
        z^{t0 * S} * z^{m * W} * prod_x eps_x^{p_x + q_x}
    with S = sum_x (p_x - q_x) and W = sum_x x (p_x - q_x).
    Averaging over t0 kills it unless S = 0 mod 5; averaging over eps kills it
    unless every p_x + q_x is even. The surviving value is z^{m W mod 5}.
    Returned as (coefficient, exponent) with coefficient in {0, 1}.
    """
    for x in range(N):
        if (p[x] + q[x]) % 2 != 0:
            return (0, 0)
    S = sum(p[x] - q[x] for x in range(N))
    if S % N != 0:
        return (0, 0)
    W = sum(x * (p[x] - q[x]) for x in range(N))
    return (1, (m * W) % N)


# ------------------------------------------------- direct enumeration path

def enum_law_A():
    w = Fraction(1, N ** N)
    return [(w, tuple((1, t[x]) for x in range(N)))
            for t in product(range(N), repeat=N)]


def enum_law_B(m):
    w = Fraction(1, N * 2 ** N)
    out = []
    for t0 in range(N):
        for eps in product((1, -1), repeat=N):
            out.append((w, tuple((eps[x], (t0 + m * x) % N) for x in range(N))))
    return out


def red5(v):
    c = v[4]
    return (v[0] - c, v[1] - c, v[2] - c, v[3] - c)


def enum_expect(law, p, q):
    n = [p[x] - q[x] for x in range(N)]
    par = [(p[x] + q[x]) & 1 for x in range(N)]
    acc = [Fraction(0)] * N
    for w, cfg in law:
        sgn = 1
        e = 0
        for x in range(N):
            s, ex = cfg[x]
            if par[x] and s < 0:
                sgn = -sgn
            if n[x]:
                e += n[x] * ex
        acc[e % N] += w if sgn > 0 else -w
    return red5(acc)


def q_from_unit(coef, expo):
    v = [Fraction(0)] * N
    v[expo % N] = Fraction(coef)
    return red5(v)


# ------------------------------------------------------------------ sweeps

def monomials(maxdeg):
    for deg in range(maxdeg + 1):
        for combo in combinations_with_replacement(range(2 * N), deg):
            p = [0] * N
            q = [0] * N
            for s in combo:
                if s < N:
                    p[s] += 1
                else:
                    q[s - N] += 1
            yield deg, tuple(p), tuple(q)


def main():
    print("C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 breaker")
    print("closed-form character sums, independent of the verifier code path")
    print("")

    mons = list(monomials(4))
    gate("sweep.monomial.count.1001", len(mons) == 1001, "n=%d" % len(mons))

    # BRK-1 and BRK-2, separators by closed form only
    seps_by_deg = {0: [], 1: [], 2: [], 3: [], 4: []}
    for deg, p, q in mons:
        ea = cf_A(p, q)
        cb, eb_exp = cf_B(p, q, 0)
        # under B_0 the surviving exponent is always 0 since m = 0
        same = (ea == cb and eb_exp == 0)
        if not same:
            seps_by_deg[deg].append((p, q, ea, (cb, eb_exp)))

    for d in (0, 1, 2, 3):
        gate("BRK-1.no.separator.at.degree.%d" % d, len(seps_by_deg[d]) == 0,
             "n=%d" % len(seps_by_deg[d]))

    predicted = set()
    for x in range(N):
        for y in range(N):
            if x != y:
                p = [0] * N
                q = [0] * N
                p[x] = 2
                q[y] = 2
                predicted.add((tuple(p), tuple(q)))
    found = set((p, q) for p, q, ea, eb in seps_by_deg[4])
    gate("BRK-2.degree4.separator.count.20", len(found) == 20,
         "n=%d" % len(found))
    gate("BRK-2.degree4.separator.set.matches.prediction", found == predicted)
    gate("BRK-2.degree4.values.A0.B1",
         all(ea == 0 and eb == (1, 0) for p, q, ea, eb in seps_by_deg[4]))

    # BRK-3, bind the closed form to enumeration on every monomial
    LA = enum_law_A()
    LB = enum_law_B(0)
    bad_a = 0
    bad_b = 0
    for deg, p, q in mons:
        va = enum_expect(LA, p, q)
        if va != q_from_unit(cf_A(p, q), 0):
            bad_a += 1
        cb, ex = cf_B(p, q, 0)
        vb = enum_expect(LB, p, q)
        if vb != q_from_unit(cb, ex):
            bad_b += 1
    gate("BRK-3.closedform.equals.enumeration.A", bad_a == 0,
         "mismatches=%d" % bad_a)
    gate("BRK-3.closedform.equals.enumeration.B0", bad_b == 0,
         "mismatches=%d" % bad_b)

    # BRK-4, can any deterministic-modulus one-site law satisfy Wick
    # |v|^2 = a^2 a.s. forces E[|v|^4] = a^4 exactly. Wick with P = 0 forces
    # 2 * C^2 = 2 a^4. Equality needs a^4 = 2 a^4, hence a = 0.
    # Scan a over a finite exact grid of positive rationals as a witness that
    # no positive scale rescues it. This is exact rational arithmetic.
    survivors = []
    for num in range(1, 13):
        for den in range(1, 13):
            a2 = Fraction(num, den)
            if a2 <= 0:
                continue
            lhs = a2 * a2          # E[|v|^4] = a^4
            rhs = 2 * a2 * a2      # Wick value
            if lhs == rhs:
                survivors.append(a2)
    gate("BRK-4.wick.survivors.at.positive.scale.none",
         len(survivors) == 0, "survivors=%d over 144 exact scales"
         % len(survivors))

    # BRK-5, does the counterexample family widen beyond B_0
    widened = []
    for m in range(N):
        ok = True
        for deg, p, q in mons:
            if deg > 3:
                continue
            cb, ex = cf_B(p, q, m)
            if q_from_unit(cb, ex) != q_from_unit(cf_A(p, q), 0):
                ok = False
                break
        if ok:
            widened.append(m)
    gate("BRK-5.all.B_m.share.degree.le3.data.with.A",
         widened == [0, 1, 2, 3, 4], "m=%s" % ",".join(str(x) for x in widened))

    # and the peak position of each B_m, derived from the closed form alone
    peaks = []
    for m in range(N):
        # C^w_{r,0} = E[v_r^2 conj(v_0)^2]; p has 2 at r, q has 2 at 0
        row = []
        for r in range(N):
            p = [0] * N
            q = [0] * N
            p[r] += 2
            q[0] += 2
            row.append(cf_B(tuple(p), tuple(q), m))
        # row[r] = (1, 2 m r); S(k) = sum_r z^{2 m r - k r} = 5 delta_{k, 2m}
        acc = [0] * N
        for k in range(N):
            s = 0
            for r in range(N):
                c, e = row[r]
                if c and (e - k * r) % N == 0:
                    s += c
                elif c:
                    s = s  # contributes off the rational line, handled below
            acc[k] = s
        peaks.append(max(range(N), key=lambda k: acc[k]))
    gate("BRK-5.peak.position.equals.2m.mod.5",
         peaks == [(2 * m) % N for m in range(N)],
         "peaks=%s" % ",".join(str(x) for x in peaks))

    print("")
    print("BREAKER SUMMARY gates=%d fails=%d breaks=%d" %
          (GATES, len(FAILS), len(FAILS)))
    if FAILS:
        for f in FAILS:
            print("BROKEN %s" % f)
        print("BREAKER VERDICT BREAK FOUND")
        return 1
    print("BREAKER VERDICT NO BREAK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
