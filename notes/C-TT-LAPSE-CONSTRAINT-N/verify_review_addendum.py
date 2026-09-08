#!/usr/bin/env python3
# C-TT-LAPSE-CONSTRAINT-N, review addendum certificate. NON-CANONICAL, no authority.
# Frozen successor to verify_fixture_corrected.py; the earlier files are not modified.
# Exact arithmetic only (Fraction); symbolic polynomial identities where a universal
# statement is made. Standard library only. No float in any assertion.
#
# What this file certifies, each as an exact polynomial identity or an exact array
# equality, in response to the review of 2026-09-08:
#   A1  the discrete product identity L(h^2) = 2 h (L h) - 2 g(h) as a polynomial
#       identity in the five site values (not a check on K1 values only)
#   A2  sigma_ii - sigma_i = (1/2) L(h^2) and tau_ii - tau_i = (1/2) Pi(h^2) for all
#       ten K1 words; the values 3/40 and -1/20 at cut 0, unit a^2
#   A3  the projected residual L tau_i - sigma_i = -mean(sigma_i) 1 for all words
#   A4  symbolic Euler-Lagrange certificate: the seven sector equations hold as
#       polynomial identities in every field variable, every source variable and the
#       formal inverse scale il = 1/lambda (not an audit of sampled configurations)
#   A5  the lapse variables occur only linearly, and the lapse equation at a slice
#       contains no lapse variable of any slice (F2 as a polynomial statement)
#   A6  computed coefficient census of the action polynomial: every coefficient is a
#       rational multiple of il^0 or il^1
#   A7  the vector witness h_13(n,r) = n f(r), all else zero, no source, satisfies
#       every displayed equation: the system does not exclude it (momentum constraints
#       are absent because the shift was set to zero before variation)
#   A8  time placement: the same-time sum Z_n = sum sigma_i is not conserved by the
#       free TT equation (Z_1 - Z_0 = (1/4)||L f||^2 for h_0 = h_1 = f), while the
#       staggered form with <h_n, L h_(n+1)> is conserved

from fractions import Fraction as Fr
from itertools import permutations, product
import random

random.seed(20260908)
CHECKS = []


def check(tag, ok):
    CHECKS.append((tag, bool(ok)))


# ---------------------------------------------------------------- polynomials over Q
def P(var=None, c=Fr(1)):
    if var is None:
        return {(): Fr(c)}
    return {((var, 1),): Fr(c)}


def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, Fr(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def pscale(p, s):
    return {k: v * s for k, v in p.items() if v * s != 0}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            d = dict(k1)
            for var, e in k2:
                d[var] = d.get(var, 0) + e
            k = tuple(sorted(d.items()))
            out[k] = out.get(k, Fr(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def psum(ps):
    out = {}
    for p in ps:
        out = padd(out, p)
    return out


def pdiff(p, var):
    out = {}
    for k, v in p.items():
        d = dict(k)
        e = d.get(var, 0)
        if e == 0:
            continue
        d[var] = e - 1
        if d[var] == 0:
            del d[var]
        kk = tuple(sorted(d.items()))
        out[kk] = out.get(kk, Fr(0)) + v * e
    return {k: v for k, v in out.items() if v != 0}


def peq(p, q):
    return padd(p, pscale(q, -1)) == {}


def pdeg_in(p, var):
    return max((dict(k).get(var, 0) for k in p), default=0)


# ---------------------------------------------------------------- planar stencil
shells = {(1, 1, 0): Fr(6, 324), (2, 0, 0): Fr(1, 324), (2, 2, 0): Fr(15, 324),
          (3, 1, 0): Fr(1, 324), (4, 0, 0): Fr(1, 324)}
vectors = {}
for base, c in shells.items():
    S = set()
    for p in set(permutations(base)):
        for signs in product((1, -1), repeat=3):
            S.add(tuple(s * x for s, x in zip(signs, p)))
    for v in S:
        vectors[v] = c
by3 = {}
for v, c in vectors.items():
    by3[v[2] % 5] = by3.get(v[2] % 5, Fr(0)) + c
rates = {k: by3[k] for k in (1, 2, 3, 4)}
check("stencil rates 29,65,65,29 /324", [rates[k] * 324 for k in (1, 2, 3, 4)] == [29, 65, 65, 29])


def L(f):
    return [sum(rates[k] * (f[r] - f[(r + k) % 5]) for k in rates) for r in range(5)]


def Lpoly(f):  # f: list of 5 polynomials
    return [psum([pscale(padd(f[r], pscale(f[(r + k) % 5], -1)), rates[k]) for k in rates]) for r in range(5)]


def g_density(f):
    return [Fr(1, 2) * sum(rates[k] * (f[r] - f[(r + k) % 5]) ** 2 for k in rates) for r in range(5)]


def g_poly(f):
    return [pscale(psum([pscale(pmul(padd(f[r], pscale(f[(r + k) % 5], -1)),
                                     padd(f[r], pscale(f[(r + k) % 5], -1))), rates[k]) for k in rates]), Fr(1, 2))
            for r in range(5)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------- A1 product identity (symbolic)
h = [P("h%d" % r) for r in range(5)]
h2 = [pmul(h[r], h[r]) for r in range(5)]
lhs = Lpoly(h2)
Lh = Lpoly(h)
gh = g_poly(h)
rhs = [padd(pscale(pmul(h[r], Lh[r]), 2), pscale(gh[r], -2)) for r in range(5)]
check("A1 L(h^2) = 2 h L h - 2 g(h) holds as a polynomial identity in h_0..h_4",
      all(peq(lhs[r], rhs[r]) for r in range(5)))

# ---------------------------------------------------------------- K1 words and the two transcriptions
words = {"0010": Fr(1, 12), "0011": Fr(1, 12), "0100": Fr(1, 12), "0101": Fr(1, 12),
         "0110": Fr(1, 6), "1001": Fr(1, 6), "1010": Fr(1, 12), "1011": Fr(1, 12),
         "1100": Fr(1, 12), "1101": Fr(1, 12)}


def u(w, t):
    b = [int(ch) for ch in w]
    return b[t + 2] - b[t]


def iota(w, t):
    ut = u(w, t)
    return [Fr(1, 2) if (r == ut % 5 or r == (ut + 1) % 5) else Fr(0) for r in range(5)]


def sigma_i(w):
    h0, h1 = iota(w, 0), iota(w, 1)
    g = g_density(h0)
    return [Fr(1, 4) * ((h1[r] - h0[r]) ** 2 + g[r]) for r in range(5)]


def sigma_ii(w):
    h0, h1 = iota(w, 0), iota(w, 1)
    g = g_density(h0)
    Lh0 = L(h0)
    return [Fr(1, 4) * (h1[r] - h0[r]) ** 2 - Fr(3, 4) * g[r] + h0[r] * Lh0[r] for r in range(5)]


# rational pseudo-inverse of L on the mean-zero subspace, by exact Gaussian elimination
def solve_mean_zero(rhs):
    # solve L x = rhs with sum x = 0; rhs must have zero sum
    assert sum(rhs) == 0
    Lm = [L([Fr(int(i == j)) for i in range(5)]) for j in range(5)]   # columns
    A = [[Lm[j][i] for j in range(5)] + [rhs[i]] for i in range(5)]   # rows of L | rhs
    A.append([Fr(1)] * 5 + [Fr(0)])                                    # sum x = 0
    # Gaussian elimination on 6x5 augmented, exact
    rows, cols = 6, 5
    piv = 0
    pivcols = []
    for c in range(cols):
        pr = None
        for r in range(piv, rows):
            if A[r][c] != 0:
                pr = r
                break
        if pr is None:
            continue
        A[piv], A[pr] = A[pr], A[piv]
        inv = 1 / A[piv][c]
        A[piv] = [x * inv for x in A[piv]]
        for r in range(rows):
            if r != piv and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[piv])]
        pivcols.append(c)
        piv += 1
    assert pivcols == [0, 1, 2, 3, 4]
    assert all(A[r][5] == 0 for r in range(5, rows))
    x = [A[i][5] for i in range(5)]
    assert L(x) == rhs and sum(x) == 0
    return x


def tau_of(sig):
    m = sum(sig) / 5
    return solve_mean_zero([s - m for s in sig])


ok2 = True
ok3 = True
for w in words:
    si, sii = sigma_i(w), sigma_ii(w)
    h0 = iota(w, 0)
    Lh2 = L([x * x for x in h0])
    ok2 &= all(sii[r] - si[r] == Lh2[r] / 2 for r in range(5))
    ti, tii = tau_of(si), tau_of(sii)
    h2m = sum(x * x for x in h0) / 5
    ok2 &= all(tii[r] - ti[r] == (h0[r] * h0[r] - h2m) / 2 for r in range(5))
    ok2 &= all((tii[r] - ti[r] == Fr(3, 40)) if h0[r] != 0 else (tii[r] - ti[r] == Fr(-1, 20)) for r in range(5))
    Lti = L(ti)
    ok3 &= all(Lti[r] - si[r] == -sum(si) / 5 for r in range(5))
check("A2 sigma_ii - sigma_i = (1/2) L(h^2) and tau_ii - tau_i = (1/2) Pi(h^2) = +3/40 occupied, -1/20 empty, all ten words", ok2)
check("A3 projected residual: L tau_i - sigma_i = -mean(sigma_i) 1 for all ten words (not a solution of the full constraint)", ok3)

# ---------------------------------------------------------------- A4/A5/A6 symbolic action and Euler-Lagrange certificate
FIELDS = ("hp", "hx", "h13", "h23", "tau", "ell", "n")
il = P("il")   # formal 1/lambda
V = {(f, n, r): P("%s_%d_%d" % (f, n, r)) for f in FIELDS for n in range(3) for r in range(5)}
SRC = {(n, r): P("src_%d_%d" % (n, r)) for n in range(3) for r in range(5)}
half_il = pscale(il, Fr(1, 2))
terms = []
for n in (0, 1):
    for r in range(5):
        D_ = {f: padd(V[f, n + 1, r], pscale(V[f, n, r], -1)) for f in FIELDS}
        kin = psum([pscale(pmul(D_[f], D_[f]), Fr(1, 2)) for f in ("hp", "hx", "h13", "h23")])
        kin = padd(kin, pscale(pmul(D_["tau"], D_["tau"]), Fr(-1, 2)))
        kin = padd(kin, pscale(pmul(D_["tau"], D_["ell"]), -1))
        terms.append(pmul(half_il, kin))
for n in range(3):
    Lt = Lpoly([V["tau", n, r] for r in range(5)])
    Lp = Lpoly([V["hp", n, r] for r in range(5)])
    Lx = Lpoly([V["hx", n, r] for r in range(5)])
    for r in range(5):
        grad = padd(padd(pscale(pmul(V["tau", n, r], Lt[r]), Fr(1, 2)), pscale(pmul(V["hp", n, r], Lp[r]), Fr(-1, 2))),
                    pscale(pmul(V["hx", n, r], Lx[r]), Fr(-1, 2)))
        lapse = pscale(pmul(V["n", n, r], Lt[r]), 2)
        terms.append(pmul(half_il, padd(grad, lapse)))
        terms.append(pscale(pmul(V["n", n, r], SRC[n, r]), Fr(-1, 2)))
        terms.append(pscale(pmul(SRC[n, r], padd(V["hp", n, r], pscale(V["ell", n, r], Fr(-1, 2)))), Fr(1, 2)))
ACTION = psum(terms)


def name(f, n, r):
    return "%s_%d_%d" % (f, n, r)


def dd_poly(f, r):
    return padd(padd(V[f, 2, r], pscale(V[f, 1, r], -2)), V[f, 0, r])


n = 1
Lt1 = Lpoly([V["tau", n, r] for r in range(5)])
Lp1 = Lpoly([V["hp", n, r] for r in range(5)])
Lx1 = Lpoly([V["hx", n, r] for r in range(5)])
Ln1 = Lpoly([V["n", n, r] for r in range(5)])
ok4 = True
for r in range(5):
    claimed = {
        "hp": padd(pmul(pscale(il, Fr(-1, 2)), padd(dd_poly("hp", r), Lp1[r])), pscale(SRC[n, r], Fr(1, 2))),
        "hx": pmul(pscale(il, Fr(-1, 2)), padd(dd_poly("hx", r), Lx1[r])),
        "h13": pmul(pscale(il, Fr(-1, 2)), dd_poly("h13", r)),
        "h23": pmul(pscale(il, Fr(-1, 2)), dd_poly("h23", r)),
        "tau": padd(pmul(pscale(il, Fr(1, 2)), padd(padd(dd_poly("tau", r), dd_poly("ell", r)), Lt1[r])), pmul(il, Ln1[r])),
        "ell": padd(pmul(pscale(il, Fr(1, 2)), dd_poly("tau", r)), pscale(SRC[n, r], Fr(-1, 4))),
        "n": padd(pmul(il, Lt1[r]), pscale(SRC[n, r], Fr(-1, 2))),
    }
    for f in FIELDS:
        ok4 &= peq(pdiff(ACTION, name(f, n, r)), claimed[f])
check("A4 Euler-Lagrange certificate: the seven sector equations at the interior slice hold as polynomial identities in all 105 field, 15 source and il variables", ok4)

# A5: lapse linear, and its equation free of lapse variables
lapse_vars = [name("n", nn, r) for nn in range(3) for r in range(5)]
ok5 = all(pdeg_in(ACTION, v) == 1 for v in lapse_vars)
for r in range(5):
    eq = pdiff(ACTION, name("n", 1, r))
    ok5 &= all(pdeg_in(eq, v) == 0 for v in lapse_vars)
    # also no product of two distinct lapse variables anywhere in the action
ok5 &= all(sum(1 for var, e in k if var.startswith("n_")) <= 1 for k in ACTION)
check("A5 lapse occurs only linearly in the action; the lapse equation contains no lapse variable (F2 as a polynomial statement)", ok5)

# A6: coefficient census, computed
census = {}
for k, v in ACTION.items():
    d = dict(k)
    ild = d.get("il", 0)
    census.setdefault(ild, set()).add(v)
check("A6 every action coefficient is a rational multiple of il^0 or il^1 (computed census, not a declaration)",
      set(census.keys()) == {0, 1})

# ---------------------------------------------------------------- A7 vector witness
f_wit = [Fr(1), Fr(-2), Fr(3), Fr(-1), Fr(-1)]   # nonconstant, mean zero
check("A7 witness profile is nonconstant with zero mean and L f != 0", sum(f_wit) == 0 and any(x != 0 for x in L(f_wit)))
subs = {}
for (f, nn, r), _ in V.items():
    subs[name(f, nn, r)] = Fr(nn) * f_wit[r] if f == "h13" else Fr(0)
for (nn, r), _ in SRC.items():
    subs["src_%d_%d" % (nn, r)] = Fr(0)
subs["il"] = Fr(1, 7)


def peval(p, s):
    tot = Fr(0)
    for k, v in p.items():
        t = v
        for var, e in k:
            t *= s[var] ** e
        tot += t
    return tot


ok7 = True
for f in FIELDS:
    for r in range(5):
        ok7 &= peval(pdiff(ACTION, name(f, 1, r)), subs) == 0
check("A7 h_13(n,r) = n f(r), all else zero, no source: every displayed equation is satisfied; the system does not exclude this inhomogeneous vector velocity", ok7)

# ---------------------------------------------------------------- A8 time placement of the source sum
def free_step(hn, hm):
    Lh = L(hn)
    return [2 * hn[r] - hm[r] - Lh[r] for r in range(5)]


def Z(hn, hn1):
    return Fr(1, 4) * (sum((a - b) ** 2 for a, b in zip(hn1, hn)) + dot(hn, L(hn)))


def E_stag(hn, hn1):
    return Fr(1, 2) * sum((a - b) ** 2 for a, b in zip(hn1, hn)) + Fr(1, 2) * dot(hn, L(hn1))


ok8 = True
for trial in range(6):
    f = [Fr(random.randint(-4, 4)) for _ in range(5)]
    if not any(x != 0 for x in L(f)):
        continue
    h0, h1 = f, f
    h2 = free_step(h1, h0)
    h3 = free_step(h2, h1)
    ok8 &= (Z(h1, h2) - Z(h0, h1) == Fr(1, 4) * dot(L(f), L(f)))
    ok8 &= (E_stag(h0, h1) == E_stag(h1, h2) == E_stag(h2, h3))
# the four static K1 words under the proposed free continuation
for w in ("0011", "0101", "1010", "1100"):
    f = iota(w, 0)
    h2 = free_step(f, f)
    ok8 &= (Z(f, h2) - Z(f, f) == Fr(1, 4) * dot(L(f), L(f))) and dot(L(f), L(f)) > 0
    ok8 &= (E_stag(f, f) == E_stag(f, h2))
check("A8 Z_n = sum sigma_i is not conserved by the free TT equation (Z_1 - Z_0 = (1/4)||L f||^2 > 0 for h_0 = h_1 = f), the staggered <h_n, L h_(n+1)> form is conserved; holds for the four static K1 words", ok8)

# ---------------------------------------------------------------- report
print("C-TT-LAPSE-CONSTRAINT-N review addendum certificate, exact arithmetic")
for tag, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + tag)
bad = [t for t, ok in CHECKS if not ok]
print("checks:", len(CHECKS), "failed:", len(bad))
print()
print("action polynomial: %d monomials; coefficient census by il-degree:" % len(ACTION))
for ild in sorted(census):
    print("  il^%d: %s" % (ild, sorted(census[ild])))
print()
print("transcription difference at cut 0, unit a^2 (tau_ii - tau_i), word 0010:", [str(x) for x in
      (lambda ti, tii: [tii[r] - ti[r] for r in range(5)])(tau_of(sigma_i("0010")), tau_of(sigma_ii("0010")))])
print("projected residual, word 0010: L tau_i - sigma_i =", [str(x) for x in
      (lambda ti, si: [L(ti)[r] - si[r] for r in range(5)])(tau_of(sigma_i("0010")), sigma_i("0010"))])
print("vector witness f =", [str(x) for x in f_wit], " L f =", [str(x) for x in L(f_wit)])
print("static word 0101: Z_1 - Z_0 =", str(Z(iota("0101", 0), free_step(iota("0101", 0), iota("0101", 0))) - Z(iota("0101", 0), iota("0101", 0))))
raise SystemExit(1 if bad else 0)
