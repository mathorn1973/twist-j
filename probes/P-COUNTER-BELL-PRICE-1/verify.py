#!/usr/bin/env python3
"""Verifier for C-COUNTER-BELL-PRICE-N. Candidate, no authority.

Preregistration: PREREG-C-COUNTER-BELL-PRICE-N.md, sha256
c412e70327439d687edcab82acfb54b4ceb185378b7c02feef4db37383bf3ad8.
Standard library only. Exact arithmetic only (Fraction, Q(sqrt 2) pairs).
"""
import hashlib
import random
import sys
from fractions import Fraction as F
from itertools import product

OUT = []
FAILS = []


def say(line):
    OUT.append(line)


def check(name, cond, detail=""):
    tag = "PASS" if cond else "FAIL"
    if not cond:
        FAILS.append(name)
    say(f"{name:<44} {tag}" + (f"  {detail}" if detail else ""))


# ---------------------------------------------------------------- Q(sqrt 2)
class Q2:
    """a + b sqrt(2) with a, b Fractions."""

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return Q2(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def sign(self):
        a, b = self.a, self.b
        if a >= 0 and b >= 0:
            return 0 if (a == 0 and b == 0) else 1
        if a <= 0 and b <= 0:
            return -1
        if a > 0:  # b < 0
            return 1 if a * a > 2 * b * b else (-1 if a * a < 2 * b * b else 0)
        return 1 if 2 * b * b > a * a else (-1 if 2 * b * b < a * a else 0)

    def __eq__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return self.a == o.a and self.b == o.b

    def __lt__(self, o):
        return (self - o).sign() < 0

    def __le__(self, o):
        return (self - o).sign() <= 0

    def __repr__(self):
        return f"({self.a})+({self.b})sqrt2"


def qmin(values):
    m = values[0]
    for v in values[1:]:
        if v < m:
            m = v
    return m


# ------------------------------------------------------------ counter models
# A model: settings list X, latent list of labels, mu[(x,y)][lam] weight,
# alpha[(x,lam)] = prob of first outcome letter, beta[(y,lam)] likewise.
# Outcome letters: index 0 and 1. CHSH: 0 -> +1, 1 -> -1. QDD: 0 -> L, 1 -> H.

def behaviour(X, lams, mu, alpha, beta):
    p = {}
    for x in X:
        for y in X:
            for a in (0, 1):
                for b in (0, 1):
                    s = 0
                    for lam in lams:
                        pa = alpha[(x, lam)] if a == 0 else 1 - alpha[(x, lam)]
                        pb = beta[(y, lam)] if b == 0 else 1 - beta[(y, lam)]
                        s = s + mu[(x, y)][lam] * pa * pb
                    p[(x, y, a, b)] = s
    return p


def overlap(X, lams, mu):
    tot = 0
    for lam in lams:
        vals = [mu[(x, y)][lam] for x in X for y in X]
        tot = tot + (qmin(vals) if isinstance(vals[0], Q2) else min(vals))
    return 1 - tot


def det_model(X, lams, types):
    """alpha, beta from deterministic types: types[lam] = (Aset, Bset) of
    settings giving letter 0."""
    alpha, beta = {}, {}
    for lam in lams:
        A, B = types[lam]
        for x in X:
            alpha[(x, lam)] = F(1) if x in A else F(0)
            beta[(x, lam)] = F(1) if x in B else F(0)
    return alpha, beta


def chsh(p):
    def E(x, y):
        return p[(x, y, 0, 0)] + p[(x, y, 1, 1)] - p[(x, y, 0, 1)] - p[(x, y, 1, 0)]
    return E(0, 0) + E(0, 1) + E(1, 0) - E(1, 1)


Z5 = list(range(5))


def qdd_B(p):
    s = 0
    for k in Z5:
        for l in Z5:
            s = s + (2 * p[(k, l, 0, 0)] if k == l else -p[(k, l, 0, 0)])
    return s


def signalling(X, p):
    worst = F(0)
    for x in X:
        for y in X:
            for y2 in X:
                pa1 = p[(x, y, 0, 0)] + p[(x, y, 0, 1)]
                pa2 = p[(x, y2, 0, 0)] + p[(x, y2, 0, 1)]
                worst = max(worst, abs(pa1 - pa2))
            # Bob side
            for x2 in X:
                pb1 = p[(x, y, 0, 0)] + p[(x, y, 1, 0)]
                pb2 = p[(x2, y, 0, 0)] + p[(x2, y, 1, 0)]
                worst = max(worst, abs(pb1 - pb2))
    return worst


def rand_dist(rng, n):
    while True:
        w = [rng.randint(0, 12) for _ in range(n)]
        if sum(w) > 0:
            t = sum(w)
            return [F(v, t) for v in w]


def rand_model(rng, X, n, mode):
    lams = list(range(n))
    mu = {}
    if mode == 0:
        for x in X:
            for y in X:
                d = rand_dist(rng, n)
                mu[(x, y)] = {lam: d[lam] for lam in lams}
    else:
        eps = F(rng.randint(0, 12), 12)
        nu = rand_dist(rng, n)
        for x in X:
            for y in X:
                r = rand_dist(rng, n)
                mu[(x, y)] = {lam: (1 - eps) * nu[lam] + eps * r[lam] for lam in lams}
    alpha = {(x, lam): F(rng.randint(0, 12), 12) for x in X for lam in lams}
    beta = {(y, lam): F(rng.randint(0, 12), 12) for y in X for lam in lams}
    return lams, mu, alpha, beta


def check_split(X, lams, mu, eps):
    nu = {lam: min(mu[(x, y)][lam] for x in X for y in X) for lam in lams}
    for x in X:
        for y in X:
            r = [mu[(x, y)][lam] - nu[lam] for lam in lams]
            if any(v < 0 for v in r) or sum(r) != eps:
                return False
    return True


def determinize_check(X, lams, mu, alpha, beta, p, eps):
    """Latent -> (lam, s, t) with deterministic strings. Full enumeration."""
    m = len(X)
    newp = {key: F(0) for key in p}
    newov = F(0)
    for lam in lams:
        for s in product((0, 1), repeat=m):
            wa = F(1)
            for i, x in enumerate(X):
                wa *= alpha[(x, lam)] if s[i] == 0 else 1 - alpha[(x, lam)]
            if wa == 0:
                continue
            for t in product((0, 1), repeat=m):
                w = wa
                for j, y in enumerate(X):
                    w *= beta[(y, lam)] if t[j] == 0 else 1 - beta[(y, lam)]
                if w == 0:
                    continue
                vals = []
                for i, x in enumerate(X):
                    for j, y in enumerate(X):
                        v = mu[(x, y)][lam] * w
                        vals.append(v)
                        newp[(x, y, s[i], t[j])] += v
                newov += min(vals)
    return newp == p and (1 - newov) == eps


# ======================================================================= main
def main():
    rng = random.Random(20260923)
    say("C-COUNTER-BELL-PRICE-N verifier")
    say("prereg sha256 c412e70327439d687edcab82acfb54b4ceb185378b7c02feef4db37383bf3ad8")

    # ------------------------------------------------------------ CHSH part
    X2 = [0, 1]
    types16 = []
    for A0, A1, B0, B1 in product((0, 1), repeat=4):
        A = {x for x, v in zip(X2, (A0, A1)) if v == 0}
        B = {y for y, v in zip(X2, (B0, B1)) if v == 0}
        types16.append((A, B))
    vals = []
    for T in types16:
        lams = [0]
        mu = {(x, y): {0: F(1)} for x in X2 for y in X2}
        al, be = det_model(X2, lams, {0: T})
        vals.append(chsh(behaviour(X2, lams, mu, al, be)))
    check("B1 CHSH 16 local types max |S| = 2", max(abs(v) for v in vals) == 2
          and sorted(set(vals)) == [-2, 2], f"values {sorted(set(vals))}")

    n_models = 400
    worst_c3, worst_c6 = None, None
    ok1 = ok2 = True
    for i in range(n_models):
        lams, mu, al, be = rand_model(rng, X2, 1 + i % 6, i % 2)
        p = behaviour(X2, lams, mu, al, be)
        eps = overlap(X2, lams, mu)
        ok1 = ok1 and check_split(X2, lams, mu, eps)
        ok2 = ok2 and determinize_check(X2, lams, mu, al, be, p, eps)
        s3 = abs(chsh(p)) - 2 - 2 * eps
        s6 = signalling(X2, p) - eps
        worst_c3 = s3 if worst_c3 is None else max(worst_c3, s3)
        worst_c6 = s6 if worst_c6 is None else max(worst_c6, s6)
    check("C1 split nu + r_xy, mass eps (CHSH, 400)", ok1)
    check("C2 determinization keeps p, eps (CHSH, 400)", ok2)
    check("C3 bound |S| <= 2 + 2eps (400 models)", worst_c3 <= 0, f"max slack {worst_c3}")
    check("C6 bound signalling <= eps (CHSH, 400)", worst_c6 <= 0, f"max slack {worst_c6}")

    eps_list = [F(0), F(1, 16), F(3, 128), F(1, 7), F(1, 3), F(1, 2), F(2, 3), F(1)]
    ok3 = True
    for eps in eps_list:
        lams = ["c"] + [f"{x}{y}" for x in X2 for y in X2]
        types = {"c": ({0, 1}, {0, 1})}
        for x in X2:
            for y in X2:
                # Alice letter 0 at x; Bob letter 0 iff sign +, so E_xy = sign
                types[f"{x}{y}"] = ({x}, {y} if (x, y) != (1, 1) else set())
        mu = {(x, y): {lam: F(0) for lam in lams} for x in X2 for y in X2}
        for x in X2:
            for y in X2:
                mu[(x, y)]["c"] = 1 - eps
                mu[(x, y)][f"{x}{y}"] = mu[(x, y)][f"{x}{y}"] + eps
        al, be = det_model(X2, lams, types)
        p = behaviour(X2, lams, mu, al, be)
        ok3 = ok3 and chsh(p) == 2 + 2 * eps and overlap(X2, lams, mu) == eps
    check("C3 attained S = 2 + 2eps, overlap eps (8)", ok3)

    et = Q2(-1, 1)  # sqrt2 - 1
    lams = ["c"] + [f"{x}{y}" for x in X2 for y in X2]
    types = {"c": ({0, 1}, {0, 1})}
    for x in X2:
        for y in X2:
            types[f"{x}{y}"] = ({x}, {y} if (x, y) != (1, 1) else set())
    mu = {(x, y): {lam: Q2(0) for lam in lams} for x in X2 for y in X2}
    for x in X2:
        for y in X2:
            mu[(x, y)]["c"] = Q2(1) - et
            mu[(x, y)][f"{x}{y}"] = mu[(x, y)][f"{x}{y}"] + et
    al, be = det_model(X2, lams, types)
    al = {k: Q2(v) for k, v in al.items()}
    be = {k: Q2(v) for k, v in be.items()}
    p = behaviour(X2, lams, mu, al, be)
    S = chsh(p)
    ovl = overlap(X2, lams, mu)
    check("C3 Tsirelson: eps = sqrt2-1 gives S = 2sqrt2",
          S == Q2(0, 2) and ovl == et and Q2(0) < et and et < Q2(1), f"S = {S}")
    below = Q2(2 + 2 * F(2, 5)) < Q2(0, 2)
    above = Q2(0, 2) < Q2(2 + 2 * F(5, 12))
    check("C3 bracket 2/5 < sqrt2-1 < 5/12 via bound", below and above)

    # signalling attained
    ok6 = True
    for eps in eps_list:
        lams = ["c", "y0", "y1"]
        types = {"c": ({0, 1}, {0, 1}), "y0": ({0, 1}, {0, 1}), "y1": (set(), {0, 1})}
        mu = {(x, y): {"c": 1 - eps, "y0": eps if y == 0 else F(0),
                       "y1": eps if y == 1 else F(0)} for x in X2 for y in X2}
        al, be = det_model(X2, lams, types)
        p = behaviour(X2, lams, mu, al, be)
        ok6 = ok6 and signalling(X2, p) == eps and overlap(X2, lams, mu) == eps
    check("C6 signalling = eps attained (8)", ok6)

    # ------------------------------------------------------ five-context part
    masks = list(range(32))

    def mset(m):
        return {k for k in Z5 if (m >> k) & 1}

    local_vals = []
    for ma in masks:
        for mb in masks:
            A, B = mset(ma), mset(mb)
            lams = [0]
            mu = {(x, y): {0: F(1)} for x in Z5 for y in Z5}
            al, be = det_model(Z5, lams, {0: (A, B)})
            v = qdd_B(behaviour(Z5, lams, mu, al, be))
            c = len(A & B)
            if v != 3 * c - len(A) * len(B):
                local_vals.append(None)
            local_vals.append(v)
    check("B2 1024 types: B = 3c - ab, max 2",
          None not in local_vals and max(local_vals) == 2)

    worst_c4, worst_q6 = None, None
    ok1 = ok2 = True
    n_det = 0
    for i in range(n_models):
        n = 1 + i % 6
        lams, mu, al, be = rand_model(rng, Z5, n, i % 2)
        p = behaviour(Z5, lams, mu, al, be)
        eps = overlap(Z5, lams, mu)
        ok1 = ok1 and check_split(Z5, lams, mu, eps)
        if n <= 2:
            n_det += 1
            ok2 = ok2 and determinize_check(Z5, lams, mu, al, be, p, eps)
        s4 = qdd_B(p) - 2 - 8 * eps
        s6 = signalling(Z5, p) - eps
        worst_c4 = s4 if worst_c4 is None else max(worst_c4, s4)
        worst_q6 = s6 if worst_q6 is None else max(worst_q6, s6)
    check("C1 split nu + r_xy, mass eps (QDD, 400)", ok1)
    check(f"C2 determinization (QDD, {n_det} with |L|<=2)", ok2)
    check("C4 bound B <= 2 + 8eps (400 models)", worst_c4 <= 0, f"max slack {worst_c4}")
    check("C6 bound signalling <= eps (QDD, 400)", worst_q6 <= 0, f"max slack {worst_q6}")

    ok4 = True
    for eps in eps_list:
        lams = ["c"] + [(k, l) for k in Z5 for l in Z5]
        types = {"c": ({0}, {0})}
        for k in Z5:
            for l in Z5:
                types[(k, l)] = ({k}, {k}) if k == l else (set(), set())
        mu = {(x, y): {lam: F(0) for lam in lams} for x in Z5 for y in Z5}
        for x in Z5:
            for y in Z5:
                mu[(x, y)]["c"] = 1 - eps
                mu[(x, y)][(x, y)] = eps
        al, be = det_model(Z5, lams, types)
        p = behaviour(Z5, lams, mu, al, be)
        ok4 = ok4 and qdd_B(p) == 2 + 8 * eps and overlap(Z5, lams, mu) == eps
    check("C4 attained B = 2 + 8eps, overlap eps (8)", ok4)
    check("C4 value 35/16 at eps = 3/128", 2 + 8 * F(3, 128) == F(35, 16))

    # ---------------------------------------------------- full ETH-QDD-2 table
    P = {}
    for k in Z5:
        for l in Z5:
            row = (F(1, 4), F(0), F(0), F(3, 4)) if k == l else \
                (F(1, 64), F(15, 64), F(15, 64), F(33, 64))
            for idx, (a, b) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
                P[(k, l, a, b)] = row[idx]
    norm = all(sum(P[(k, l, a, b)] for a in (0, 1) for b in (0, 1)) == 1
               for k in Z5 for l in Z5)
    margA = all(P[(k, l, 0, 0)] + P[(k, l, 0, 1)] == F(1, 4) for k in Z5 for l in Z5)
    margB = all(P[(k, l, 0, 0)] + P[(k, l, 1, 0)] == F(1, 4) for k in Z5 for l in Z5)
    corr = all(P[(k, l, 0, 0)] + P[(k, l, 1, 1)] - P[(k, l, 0, 1)] - P[(k, l, 1, 0)]
               == F(1, 16) + (F(15, 16) if k == l else 0) for k in Z5 for l in Z5)
    check("T0 table: normalized, marginals 1/4, E, B",
          norm and margA and margB and corr and qdd_B(P) == F(35, 16))

    # primal point: 10/64 on each singleton A=B={k}, 1/64 on each pair
    prim = {}
    for m in masks:
        S_ = mset(m)
        if len(S_) == 1:
            prim[m] = F(10, 64)
        elif len(S_) == 2:
            prim[m] = F(1, 64)
    w = sum(prim.values())
    Lw = {key: F(0) for key in P}
    for m, y_ in prim.items():
        S_ = mset(m)
        for k in Z5:
            for l in Z5:
                a = 0 if k in S_ else 1
                b = 0 if l in S_ else 1
                Lw[(k, l, a, b)] += y_
    resid_ok = all(P[key] - Lw[key] >= 0 for key in P)
    check("C5 primal: local weight 15/16, P - wL >= 0", w == F(15, 16) and resid_ok)

    # explicit counter model from the decomposition (lemma, direction <=)
    lams = [("loc", m) for m in prim] + [("cp", x, y, a, b) for x in Z5 for y in Z5
                                         for a in (0, 1) for b in (0, 1)]
    types = {}
    for m in prim:
        types[("loc", m)] = (mset(m), mset(m))
    for x in Z5:
        for y in Z5:
            for a in (0, 1):
                for b in (0, 1):
                    types[("cp", x, y, a, b)] = (set(Z5) if a == 0 else set(),
                                                 set(Z5) if b == 0 else set())
    mu = {(x, y): {lam: F(0) for lam in lams} for x in Z5 for y in Z5}
    for x in Z5:
        for y in Z5:
            for m, y_ in prim.items():
                mu[(x, y)][("loc", m)] = y_
            for a in (0, 1):
                for b in (0, 1):
                    mu[(x, y)][("cp", x, y, a, b)] = P[(x, y, a, b)] - Lw[(x, y, a, b)]
    massok = all(sum(mu[(x, y)].values()) == 1 for x in Z5 for y in Z5)
    al, be = det_model(Z5, lams, types)
    pm = behaviour(Z5, lams, mu, al, be)
    epsm = overlap(Z5, lams, mu)
    check("C5 counter model reproduces P, eps = 1/16", massok and pm == P and epsm == F(1, 16))

    # dual certificate on all 1024 types (lemma direction >= via weak duality)
    def z(k, l, a, b):
        if k == l:
            return F(1) if a != b else F(0)
        if (a, b) == (0, 0):
            return F(1, 4)
        if (a, b) == (1, 1):
            return F(1, 12)
        return F(0)

    dual_min = None
    for ma in masks:
        for mb in masks:
            A, B = mset(ma), mset(mb)
            tot = F(0)
            for k in Z5:
                for l in Z5:
                    tot += z(k, l, 0 if k in A else 1, 0 if l in B else 1)
            dual_min = tot if dual_min is None else min(dual_min, tot)
    dual_obj = sum(z(*key) * P[key] for key in P)
    check("C5 dual: every type covered (min >= 1)", dual_min >= 1, f"min {dual_min}")
    check("C5 dual objective 15/16 = primal", dual_obj == F(15, 16) == w)
    check("C5 eps_T = 1 - w* = 1/16", 1 - dual_obj == F(1, 16))

    # nu part of any counter model is a local setting-independent sub-behaviour:
    # verified on the constructed model: nu-mass = 1 - eps and nu-behaviour <= P
    nu = {lam: min(mu[(x, y)][lam] for x in Z5 for y in Z5) for lam in lams}
    nub = {key: F(0) for key in P}
    for lam in lams:
        if nu[lam] == 0:
            continue
        A, B = types[lam]
        for k in Z5:
            for l in Z5:
                nub[(k, l, 0 if k in A else 1, 0 if l in B else 1)] += nu[lam]
    check("C5 lemma: nu-part local, mass 1-eps, <= P",
          sum(nu.values()) == 1 - epsm and all(nub[key] <= P[key] for key in P))

    say(f"failures {len(FAILS)}")
    say("RESULT " + ("ALL PASS" if not FAILS else "FALSIFIER FIRED: " + ",".join(FAILS)))
    body = "\n".join(OUT) + "\n"
    sys.stdout.write(body)
    sys.stdout.write("digest " + hashlib.sha256(body.encode()).hexdigest() + "\n")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
