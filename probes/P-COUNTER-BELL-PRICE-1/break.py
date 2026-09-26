#!/usr/bin/env python3
"""Breaker for C-COUNTER-BELL-PRICE-N. Independent code paths only.

BR1  full exact simplex (Bland) over all 1024 deterministic types, no
     symmetry, no hand certificate: max local weight w* under P.
BR2  adversarial exact hill climb on counter models against the C3 and C4
     bounds (tries to exceed 2 + 2eps and 2 + 8eps).
BR3  merge attack: merging latents with identical responses can lower the
     overlap of a model; check no merge of the C5 model drops below 1/16.
BR4  second reading of the table: rebuild P from marginals 1/4 and the
     correlator E = 1/16 + (15/16) delta only.
Stdlib, Fraction only.
"""
import hashlib
import random
import sys
from fractions import Fraction as F
from itertools import product

OUT = []


def say(s):
    OUT.append(s)


Z5 = range(5)
KEYS = [(k, l, a, b) for k in Z5 for l in Z5 for a in (0, 1) for b in (0, 1)]


# ------------------------------------------------------------------ BR4
def table_from_marginals_and_E():
    P = {}
    for k in Z5:
        for l in Z5:
            E = F(1, 16) + (F(15, 16) if k == l else 0)
            ll = E / 4
            lh = F(1, 4) - ll
            P[(k, l, 0, 0)] = ll
            P[(k, l, 0, 1)] = lh
            P[(k, l, 1, 0)] = lh
            P[(k, l, 1, 1)] = 1 - ll - 2 * lh
    return P


# ------------------------------------------------------------------ BR1
def simplex_max(A, bvec, c):
    """max c.y s.t. A y <= b, y >= 0, b >= 0. Dense Fraction tableau, Bland."""
    m, n = len(A), len(c)
    T = [A[i][:] + [F(1) if j == i else F(0) for j in range(m)] + [bvec[i]]
         for i in range(m)]
    obj = [-v for v in c] + [F(0)] * m + [F(0)]
    basis = [n + i for i in range(m)]
    pivots = 0
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            break
        best, leave = None, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            raise RuntimeError("unbounded")
        pv = T[leave][enter]
        T[leave] = [v / pv for v in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [vi - f * vl for vi, vl in zip(T[i], T[leave])]
        f = obj[enter]
        obj = [vo - f * vl for vo, vl in zip(obj, T[leave])]
        basis[leave] = enter
        pivots += 1
    y = [F(0)] * n
    for i, bj in enumerate(basis):
        if bj < n:
            y[bj] = T[i][-1]
    return obj[-1], y, pivots


def type_outcome(ma, mb, k, l):
    return (0 if (ma >> k) & 1 else 1, 0 if (mb >> l) & 1 else 1)


def br1(P):
    types = [(ma, mb) for ma in range(32) for mb in range(32)]
    A = [[F(0)] * len(types) for _ in KEYS]
    idx = {key: i for i, key in enumerate(KEYS)}
    for j, (ma, mb) in enumerate(types):
        for k in Z5:
            for l in Z5:
                a, b = type_outcome(ma, mb, k, l)
                A[idx[(k, l, a, b)]][j] = F(1)
    val, y, piv = simplex_max(A, [P[key] for key in KEYS], [F(1)] * len(types))
    # re-verify primal feasibility independently of the tableau
    feas = all(sum(A[i][j] * y[j] for j in range(len(types)) if y[j]) <= P[KEYS[i]]
               for i in range(len(KEYS))) and all(v >= 0 for v in y)
    support = sorted((bin(ma).count("1"), bin(mb).count("1"), ma == mb)
                     for (ma, mb), v in zip(types, y) if v)
    return val, feas, piv, support


# ------------------------------------------------------------------ models
def behaviour(X, lams, mu, resp):
    p = {}
    for x in X:
        for y in X:
            for a in (0, 1):
                for b in (0, 1):
                    p[(x, y, a, b)] = sum(mu[(x, y)][lam] for lam in lams
                                          if resp[lam][0][x] == a and resp[lam][1][y] == b)
    return p


def overlap(X, lams, mu):
    return 1 - sum(min(mu[(x, y)][lam] for x in X for y in X) for lam in lams)


def chsh(p):
    E = lambda x, y: p[(x, y, 0, 0)] + p[(x, y, 1, 1)] - p[(x, y, 0, 1)] - p[(x, y, 1, 0)]
    return E(0, 0) + E(0, 1) + E(1, 0) - E(1, 1)


def qddB(p):
    return sum((2 if k == l else -1) * p[(k, l, 0, 0)] for k in Z5 for l in Z5)


def br2(rng, X, score, rounds, nlam):
    """Hill climb: random deterministic responses, move mass 1/24 between
    latents inside one conditional, keep moves that raise score - bound."""
    best = None
    for r in range(rounds):
        lams = list(range(nlam))
        resp = {lam: (tuple(rng.randint(0, 1) for _ in X),
                      tuple(rng.randint(0, 1) for _ in X)) for lam in lams}
        mu = {}
        for x in X:
            for y in X:
                w = [rng.randint(1, 6) for _ in lams]
                t = sum(w)
                mu[(x, y)] = {lam: F(v, t) for lam, v in zip(lams, w)}
        cur = score(behaviour(X, lams, mu, resp), overlap(X, lams, mu))
        for _ in range(60):
            x, y = rng.choice(X), rng.choice(X)
            i, j = rng.sample(lams, 2)
            step = min(F(1, 24), mu[(x, y)][i])
            if step == 0:
                continue
            mu[(x, y)][i] -= step
            mu[(x, y)][j] += step
            new = score(behaviour(X, lams, mu, resp), overlap(X, lams, mu))
            if new >= cur:
                cur = new
            else:
                mu[(x, y)][i] += step
                mu[(x, y)][j] -= step
        best = cur if best is None else max(best, cur)
    return best


# ------------------------------------------------------------------ BR3
def br3(P, rng):
    # rebuild the C5 model with the verifier's primal point, then merge
    prim = {}
    for m in range(32):
        c = bin(m).count("1")
        if c == 1:
            prim[m] = F(10, 64)
        elif c == 2:
            prim[m] = F(1, 64)
    lams, resp, mu = [], {}, {(x, y): {} for x in Z5 for y in Z5}
    Lw = {key: F(0) for key in KEYS}
    for m, w in prim.items():
        lam = ("loc", m)
        lams.append(lam)
        r = tuple(0 if (m >> k) & 1 else 1 for k in Z5)
        resp[lam] = (r, r)
        for x in Z5:
            for y in Z5:
                mu[(x, y)][lam] = w
                Lw[(x, y, r[x], r[y])] += w
    for x in Z5:
        for y in Z5:
            for a in (0, 1):
                for b in (0, 1):
                    lam = ("cp", x, y, a, b)
                    lams.append(lam)
                    resp[lam] = (tuple([a] * 5), tuple([b] * 5))
    for lam in lams:
        if lam[0] == "cp":
            for x in Z5:
                for y in Z5:
                    _, xx, yy, a, b = lam
                    mu[(x, y)][lam] = P[(x, y, a, b)] - Lw[(x, y, a, b)] if (x, y) == (xx, yy) else F(0)
    base_ok = behaviour(Z5, lams, mu, resp) == P
    eps0 = overlap(Z5, lams, mu)
    # full merge by identical response
    groups = {}
    for lam in lams:
        groups.setdefault(resp[lam], []).append(lam)
    mlams = list(groups)
    mmu = {(x, y): {g: sum(mu[(x, y)][lam] for lam in groups[g]) for g in mlams}
           for x in Z5 for y in Z5}
    mresp = {g: g for g in mlams}
    merged_ok = behaviour(Z5, mlams, mmu, mresp) == P
    eps_merged = overlap(Z5, mlams, mmu)
    # random partial merges of same-response latents
    worst = eps_merged
    for _ in range(200):
        part = {}
        for lam in lams:
            key = (resp[lam], rng.randint(0, 2))
            part.setdefault(key, []).append(lam)
        pl = list(part)
        pmu = {(x, y): {g: sum(mu[(x, y)][lam] for lam in part[g]) for g in pl}
               for x in Z5 for y in Z5}
        worst = min(worst, overlap(Z5, pl, pmu))
    return base_ok, eps0, merged_ok, eps_merged, worst


def main():
    rng = random.Random(9230)
    say("C-COUNTER-BELL-PRICE-N breaker")
    P = table_from_marginals_and_E()
    ok4 = qddB(P) == F(35, 16) and all(v >= 0 for v in P.values())
    say(f"BR4 table rebuilt from marginals and E: B = {qddB(P)}, nonnegative {ok4}")
    say(f"BR4 entries diag {[str(P[(0,0,a,b)]) for a in (0,1) for b in (0,1)]}"
        f" off {[str(P[(0,1,a,b)]) for a in (0,1) for b in (0,1)]}")

    val, feas, piv, support = br1(P)
    say(f"BR1 full simplex over 1024 types: w* = {val}, eps_T = {1 - val}, "
        f"feasible {feas}, pivots {piv}")
    say(f"BR1 support (|A|, |B|, A==B) multiset: {sorted(set(support))}")

    b3 = br2(rng, [0, 1], lambda p, e: abs(chsh(p)) - 2 - 2 * e, 150, 5)
    say(f"BR2 CHSH hill climb, best |S| - 2 - 2eps = {b3}")
    b4 = br2(rng, list(Z5), lambda p, e: qddB(p) - 2 - 8 * e, 40, 6)
    say(f"BR2 QDD hill climb, best B - 2 - 8eps = {b4}")

    base_ok, e0, mok, em, worst = br3(P, rng)
    say(f"BR3 C5 model reproduces P {base_ok}, eps {e0}; full merge reproduces P {mok}, "
        f"eps {em}; min eps over 200 partial merges {worst}")

    broken = (not ok4) or val != F(15, 16) or not feas or b3 > 0 or b4 > 0 \
        or not base_ok or not mok or worst < F(1, 16)
    say("BREAKER RESULT " + ("BREAK" if broken else "NO BREAK"))
    body = "\n".join(OUT) + "\n"
    sys.stdout.write(body)
    sys.stdout.write("digest " + hashlib.sha256(body.encode()).hexdigest() + "\n")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
