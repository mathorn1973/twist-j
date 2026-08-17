#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
breaker.py
candidate C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2

An honest attempt to break P1, P2, P3, P5 and P6 on a code path sharing
nothing with verify.py. verify.py sums over enumerated configurations and
compares complete pushforward measures. This file never enumerates a measure
for its primary claims: it works in closed form by character orthogonality,

  E_A[M]     = 1 if n_x = 0 mod 5 for every x, else 0
  E_{B_m}[M] = z^{m W} if every p_x + q_x is even and S = 0 mod 5, else 0

with n_x = p_x - q_x, S = sum n_x, W = sum x n_x, and it proves the action
statements at the moment level: a monomial composed with an action is a
relabeled or Galois-twisted monomial, so measure identities become closed-form
identities checkable degree by degree.

Break attempts:
  BRK-1  separator inventory per degree 0..5 for all 15 pairs of the six laws
         by closed form: assert 0,0,0,0 then exactly 20 at degree 4 for every
         pair, then at degree 5 exactly the ten fifth powers for A-pairs and
         zero for B-pairs.
  BRK-2  the value table by independent formula: on the twenty, W = 2(x - y),
         so E_{B_m} = z^{2m(x-y)}; assert against cf directly.
  BRK-3  cross-bind closed form to full enumeration on every monomial of
         degree at most 5, on all six laws. This is the one place enumeration
         appears, as the binding between the two paths, not as the claim.
  BRK-4  the diagonal collapse at every degree up to 6: for every monomial,
         every u, every law, sigma_u(cf(p o u, q o u)) = cf(p, q), where
         (p o u)_y = p[(u y) mod 5]. This proves D-invariance of every moment
         of degree at most 6, strictly beyond the verifier's measure check.
  BRK-5  the orbit statements at the moment level, degree at most 4:
         cf_{B_m}(p o u, q o u) = cf_{B_{u^-1 m}}(p, q)   [rho]
         sigma_u(cf_{B_m}(p, q)) = cf_{B_{u m}}(p, q)     [gamma]
  BRK-6  fixed-modulus Wick gap at exact rational scales: no positive a with
         a^4 = 2 a^4 over a 144-point exact grid.

Exact arithmetic only, integers and Fraction. No float anywhere.
Python standard library only.
"""

import sys
from fractions import Fraction
from itertools import product, combinations_with_replacement

N = 5
INV = {1: 1, 2: 3, 3: 2, 4: 4}
UNITS = (1, 2, 3, 4)
FAILS = []
GATES = 0


def gate(name, ok, detail=""):
    global GATES
    GATES += 1
    line = "BREAK %-52s %s" % (name, "PASS" if ok else "FAIL")
    if not ok:
        FAILS.append(name)
    if detail:
        line += "  " + detail
    print(line)


# ------------------------------------------------------- closed form path
# A closed-form value is (coef, expo) meaning coef * z^expo, coef in {0, 1}.

def cf(nm, p, q):
    if nm == "A":
        for x in range(N):
            if (p[x] - q[x]) % N != 0:
                return (0, 0)
        return (1, 0)
    m = int(nm[1])
    for x in range(N):
        if (p[x] + q[x]) % 2 != 0:
            return (0, 0)
    S = sum(p[x] - q[x] for x in range(N))
    if S % N != 0:
        return (0, 0)
    W = sum(x * (p[x] - q[x]) for x in range(N))
    return (1, (m * W) % N)


def sig(u, val):
    c, e = val
    return (c, (u * e) % N) if c else (0, 0)


def relabel(u, vec):
    return tuple(vec[(u * y) % N] for y in range(N))


# ------------------------------------------------- direct enumeration path

def enum_law(nm):
    if nm == "A":
        w = Fraction(1, N ** N)
        return [(w, tuple((1, t[x]) for x in range(N)))
                for t in product(range(N), repeat=N)]
    m = int(nm[1])
    w = Fraction(1, N * 2 ** N)
    out = []
    for t0 in range(N):
        for eps in product((1, -1), repeat=N):
            out.append((w, tuple((eps[x], (t0 + m * x) % N)
                                 for x in range(N))))
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


def as_field(val):
    c, e = val
    v = [Fraction(0)] * N
    v[e % N] = Fraction(c)
    return red5(v)


def monomials_of_degree(deg):
    for combo in combinations_with_replacement(range(2 * N), deg):
        p = [0] * N
        q = [0] * N
        for s in combo:
            if s < N:
                p[s] += 1
            else:
                q[s - N] += 1
        yield tuple(p), tuple(q)


SIX = ("A", "B0", "B1", "B2", "B3", "B4")


def main():
    print("C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 breaker")
    print("closed-form character sums, independent of the verifier code path")
    print("")

    # cache closed-form values by degree
    by_deg = {}
    for deg in range(7):
        cur = []
        for p, q in monomials_of_degree(deg):
            cur.append((p, q, {nm: cf(nm, p, q) for nm in SIX}))
        by_deg[deg] = cur
    gate("count.deg.le6.8008",
         sum(len(by_deg[d]) for d in range(7)) == 8008,
         "n=%d" % sum(len(by_deg[d]) for d in range(7)))

    # BRK-1 separator inventory per degree, all 15 pairs
    twenty = set()
    for x in range(N):
        for y in range(N):
            if x != y:
                pp = [0] * N
                qq = [0] * N
                pp[x] = 2
                qq[y] = 2
                twenty.add((tuple(pp), tuple(qq)))
    tens = set()
    for x in range(N):
        pp = [0] * N
        pp[x] = 5
        tens.add((tuple(pp), (0,) * N))
        tens.add(((0,) * N, tuple(pp)))

    pairs = [(a, b) for i, a in enumerate(SIX) for b in SIX[i + 1:]]
    ok_le3 = True
    for d in range(4):
        for p, q, V in by_deg[d]:
            ref = V["A"]
            if any(V[nm] != ref for nm in SIX):
                ok_le3 = False
    gate("BRK-1.no.separator.deg.le3.any.pair", ok_le3)

    ok4 = True
    for a, b in pairs:
        seps = set((p, q) for p, q, V in by_deg[4] if V[a] != V[b])
        if seps != twenty:
            ok4 = False
    gate("BRK-1.deg4.separators.exactly.twenty.15.pairs", ok4)

    ok5a = True
    for m in range(N):
        nm = "B%d" % m
        seps = set((p, q) for p, q, V in by_deg[5] if V["A"] != V[nm])
        vals_ok = all((V["A"] == (1, 0) and V[nm] == (0, 0))
                      for p, q, V in by_deg[5] if (p, q) in seps)
        if seps != tens or not vals_ok:
            ok5a = False
    gate("BRK-1.deg5.A.pairs.exactly.ten.fifth.powers", ok5a)

    ok5b = all(V["B%d" % i] == V["B%d" % j]
               for p, q, V in by_deg[5]
               for i in range(N) for j in range(i + 1, N))
    gate("BRK-1.deg5.B.pairs.none", ok5b)

    # BRK-2 value table by independent W formula
    ok2 = True
    for x in range(N):
        for y in range(N):
            if x == y:
                continue
            pp = [0] * N
            qq = [0] * N
            pp[x] = 2
            qq[y] = 2
            for m in range(N):
                want = (1, (2 * m * (x - y)) % N)
                if cf("B%d" % m, tuple(pp), tuple(qq)) != want:
                    ok2 = False
            if cf("A", tuple(pp), tuple(qq)) != (0, 0):
                ok2 = False
    gate("BRK-2.value.table.z.2m.xminusy", ok2)

    # BRK-3 cross-bind closed form to enumeration, deg <= 5, all six laws
    laws = {nm: enum_law(nm) for nm in SIX}
    mism = 0
    for d in range(6):
        for p, q, V in by_deg[d]:
            for nm in SIX:
                if enum_expect(laws[nm], p, q) != as_field(V[nm]):
                    mism += 1
    gate("BRK-3.closedform.equals.enumeration.deg.le5",
         mism == 0, "mismatches=%d" % mism)

    # BRK-4 diagonal collapse at every degree up to 6
    bad4 = 0
    for d in range(7):
        for p, q, V in by_deg[d]:
            for u in UNITS:
                pu = relabel(u, p)
                qu = relabel(u, q)
                for nm in SIX:
                    if sig(u, cf(nm, pu, qu)) != V[nm]:
                        bad4 += 1
    gate("BRK-4.diagonal.moment.identity.deg.le6",
         bad4 == 0, "violations=%d" % bad4)

    # BRK-5 orbit statements at the moment level, deg <= 4
    bad_r = 0
    bad_g = 0
    for d in range(5):
        for p, q, V in by_deg[d]:
            for u in UNITS:
                pu = relabel(u, p)
                qu = relabel(u, q)
                for m in range(N):
                    if cf("B%d" % m, pu, qu) != \
                       cf("B%d" % ((INV[u] * m) % N), p, q):
                        bad_r += 1
                    if sig(u, cf("B%d" % m, p, q)) != \
                       cf("B%d" % ((u * m) % N), p, q):
                        bad_g += 1
    gate("BRK-5.rho.orbit.moment.identity.deg.le4",
         bad_r == 0, "violations=%d" % bad_r)
    gate("BRK-5.gamma.orbit.moment.identity.deg.le4",
         bad_g == 0, "violations=%d" % bad_g)

    # BRK-6 Wick gap at exact positive rational scales
    survivors = 0
    for num in range(1, 13):
        for den in range(1, 13):
            a2 = Fraction(num, den)
            if a2 * a2 == 2 * a2 * a2:
                survivors += 1
    gate("BRK-6.wick.survivors.none", survivors == 0,
         "survivors=%d over 144 exact scales" % survivors)

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
