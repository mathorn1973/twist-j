#!/usr/bin/env python3
# Breaker: C-NATIVE-FIBRE-PENTIT-WIGNER-N. Independent code path, written after the first
# pinned verifier run. NON-CANONICAL, L1 only. Standard library only, exact arithmetic, no float.
# Independence from the verifier:
#   generators are retyped from canon/CANON.md lines 580-584, nothing is imported from the repo;
#   cyclotomic arithmetic uses the basis 1, z, z^2, z^3 with reduction by z^4 = -1-z-z^2-z^3;
#   the Wigner function is built from Weyl expectation values, not from the parity formula;
#   line operators are tested by vanishing 2x2 minors, not by idempotence;
#   invariant forms use explicit pullback matrices, a different elimination and Pfaffians;
#   signs in Q(sqrt5) are decided by rational brackets of sqrt5, not by comparing squares.
# It needs no repository checkout. Run with:
#   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <this file>
import hashlib
import itertools
import sys
from fractions import Fraction as Fr

RES = []


def check(cid, text, cond):
    RES.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + cid + " " + text)


def info(text):
    print("     " + text)


# ------------------------------------------------------------ generators from the Canon text
def ga(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gb(x):
    p1, p4, p1p, p4p, q, r = x
    return (-p1p % 5, -p4p % 5, -p1 % 5, -p4 % 5, -q % 5, -r % 5)


def gc(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p + 2) % 5, (-p4p + 1 + r) % 5, (-p1 + 2) % 5, (-p4 + 1 - r) % 5, (1 - q) % 5, -r % 5)


def gd(x):
    p1, p4, p1p, p4p, q, r = x
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5, (1 - q) % 5, (1 - r) % 5)


def ge(x):
    p1, p4, p1p, p4p, q, r = x
    return ((2 - p1) % 5, (1 - p4) % 5, (3 - p1p) % 5, (4 - p4p) % 5, (2 - q) % 5, (1 - r) % 5)


G = (ga, gb, gc, gd, ge)
ALL = list(itertools.product(range(5), repeat=6))
F2 = list(itertools.product(range(5), repeat=2))


def tm(n):
    t = 0
    while n:
        t ^= n & 1
        n >>= 1
    return t


def step(n, x):
    return G[(sum(x) + 2 * tm(n)) % 5](x)


# ------------------------------------------------------------ Z[z] in the basis 1,z,z^2,z^3
def zmul(a, b):
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    c[0] += c[5]
    c[1] += c[6]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def zconj(a):
    return (a[0] - a[1], -a[1], a[3] - a[1], a[2] - a[1])


ZP = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1)]
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def zint(n):
    return (n, 0, 0, 0)


def mat_zero():
    return [[ZERO] * 5 for _ in range(5)]


def mat_mul(X, Y):
    Z = mat_zero()
    for i in range(5):
        for j in range(5):
            acc = ZERO
            for k in range(5):
                if X[i][k] != ZERO and Y[k][j] != ZERO:
                    acc = zadd(acc, zmul(X[i][k], Y[k][j]))
            Z[i][j] = acc
    return Z


def mat_add(X, Y):
    return [[zadd(X[i][j], Y[i][j]) for j in range(5)] for i in range(5)]


def mat_scal(s, X):
    return [[zmul(s, X[i][j]) for j in range(5)] for i in range(5)]


def mat_tr(X):
    acc = ZERO
    for i in range(5):
        acc = zadd(acc, X[i][i])
    return acc


def A(u):
    q, r = u
    X = mat_zero()
    for j in range(5):
        X[(2 * q - j) % 5][j] = ZP[(2 * r * (q - j)) % 5]
    return X


def D(v):
    q, r = v
    X = mat_zero()
    for k in range(5):
        X[(k + q) % 5][k] = ZP[(3 * q * r + r * k) % 5]
    return X


IDM = mat_zero()
for i in range(5):
    IDM[i][i] = ONE
AM = {u: A(u) for u in F2}
DM = {v: D(v) for v in F2}

# ------------------------------------------------------------ exact sign in Q(sqrt5) by brackets
def sqrt5_bracket(k):
    lo, hi = Fr(2), Fr(3)
    for _ in range(k):
        mid = (lo + hi) / 2
        if mid * mid < 5:
            lo = mid
        else:
            hi = mid
    return lo, hi


def sgn(x, y):
    if y == 0:
        return (x > 0) - (x < 0)
    k = 8
    while True:
        lo, hi = sqrt5_bracket(k)
        a, b = x + y * lo, x + y * hi
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        k += 8


def real_q5(a, den):
    # a in Z[z], real iff a1 = 0 and a2 = a3; value a0 + a2 (z^2+z^3) = (a0 - a2/2) - (a2/2) sqrt5
    assert a[1] == 0 and a[2] == a[3], "not real"
    return (Fr(2 * a[0] - a[2], 2 * den), Fr(-a[2], 2 * den))


# ============================================================ PART A
print("PART A")
cent = {}
ok = True
for name, g in zip("bcde", G[1:]):
    t = g((0, 0, 0, 0, 0, 0))[4:]
    ok &= all(g(x)[4:] == ((t[0] - x[4]) % 5, (t[1] - x[5]) % 5) for x in ALL)
    cent[name] = ((3 * t[0]) % 5, (3 * t[1]) % 5)
ok &= all(ga(x)[4:] == x[4:] for x in ALL)
check("A1", "fibre action from the retyped Canon formulas: identity for a, reflections with centres (0,0),(3,0),(3,3),(1,3)",
      ok and [cent[n] for n in "bcde"] == [(0, 0), (3, 0), (3, 3), (1, 3)])

perms = set()
gens = [tuple(F2.index(((2 * cent[n][0] - u[0]) % 5, (2 * cent[n][1] - u[1]) % 5)) for u in F2) for n in "bcde"]
todo = [tuple(range(25))]
perms.add(todo[0])
while todo:
    cur = todo.pop()
    for g in gens:
        h = tuple(g[cur[i]] for i in range(25))
        if h not in perms:
            perms.add(h)
            todo.append(h)
n_trans = 0
n_refl = 0
for h in perms:
    img0 = F2[h[0]]
    if all(F2[h[i]] == ((F2[i][0] + img0[0]) % 5, (F2[i][1] + img0[1]) % 5) for i in range(25)):
        n_trans += 1
    elif all(F2[h[i]] == ((img0[0] - F2[i][0]) % 5, (img0[1] - F2[i][1]) % 5) for i in range(25)):
        n_refl += 1
check("A2", "closure as permutations of the 25 points has order 50: 25 translations and 25 reflections",
      len(perms) == 50 and n_trans == 25 and n_refl == 25)

a3 = all(mat_mul(AM[u], AM[u]) == IDM for u in F2)
a3 &= all(AM[u][i][j] == zconj(AM[u][j][i]) for u in F2 for i in range(5) for j in range(5))
a3 &= all(mat_tr(AM[u]) == ONE for u in F2)
check("A3a", "dense A_u: involution, Hermitian, trace 1", a3)
a3b = True
a3c = True
for s in F2:
    for u in F2:
        pr = mat_mul(AM[s], AM[u])
        a3b &= mat_tr(pr) == (zint(5) if s == u else ZERO)
        a3c &= mat_mul(pr, AM[s]) == AM[((2 * s[0] - u[0]) % 5, (2 * s[1] - u[1]) % 5)]
check("A3b", "dense Tr(A_s A_u) = 5 delta for all 625 pairs", a3b)
check("A3c", "dense A_s A_u A_s = A_(2s-u) for all 625 pairs", a3c)
tot = mat_zero()
for u in F2:
    tot = mat_add(tot, AM[u])
totD = mat_zero()
for v in F2:
    totD = mat_add(totD, DM[v])
par5 = mat_zero()
for k in range(5):
    par5[(-k) % 5][k] = zint(5)
four = True
for u in F2:
    acc = mat_zero()
    for v in F2:
        acc = mat_add(acc, mat_scal(ZP[(u[1] * v[0] - u[0] * v[1]) % 5], DM[v]))
    four &= acc == mat_scal(zint(5), AM[u])
check("A3d", "sum_u A_u = 5 I, sum_v D_v = 5 Par, and 5 A_u = sum_v z^(r q' - q r') D_v for all u",
      tot == mat_scal(zint(5), IDM) and totD == par5 and four)
check("A3e", "conjugation by A at the four native centres reproduces the four native fibre maps on all 25 indices",
      all(mat_mul(mat_mul(AM[cent[n]], AM[u]), AM[cent[n]]) == AM[g(((0, 0, 0, 0) + u))[4:]]
          for n, g in zip("bcde", G[1:]) for u in F2))

# invariant alternating forms: explicit pullback matrices on the 15 upper coefficients
PR = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def linpart(g):
    c = g((0,) * 6)
    cols = [g(tuple(1 if k == i else 0 for k in range(6))) for i in range(6)]
    return [[(cols[j][i] - c[i]) % 5 for j in range(6)] for i in range(6)]


def pullback(L):
    M = [[0] * 15 for _ in range(15)]
    for col, (i, j) in enumerate(PR):
        E = [[0] * 6 for _ in range(6)]
        E[i][j] = 1
        E[j][i] = 4
        T = [[sum(L[k][r] * E[k][l] for k in range(6)) % 5 for l in range(6)] for r in range(6)]
        Wm = [[sum(T[r][l] * L[l][s] for l in range(6)) % 5 for s in range(6)] for r in range(6)]
        for row, (r, s) in enumerate(PR):
            M[row][col] = Wm[r][s]
    return M


def kernel_mod5(rows, n):
    # elimination scanning columns from the last to the first
    rows = [r[:] for r in rows]
    piv = {}
    rk = 0
    for c in range(n - 1, -1, -1):
        p = None
        for i in range(rk, len(rows)):
            if rows[i][c] % 5:
                p = i
                break
        if p is None:
            continue
        rows[rk], rows[p] = rows[p], rows[rk]
        inv = pow(rows[rk][c], 3, 5)
        rows[rk] = [(t * inv) % 5 for t in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % 5:
                f = rows[i][c]
                rows[i] = [(x - f * y) % 5 for x, y in zip(rows[i], rows[rk])]
        piv[c] = rk
        rk += 1
    basis = []
    for fc in range(n):
        if fc in piv:
            continue
        v = [0] * n
        v[fc] = 1
        for c, ri in piv.items():
            v[c] = (-rows[ri][fc]) % 5
        basis.append(v)
    return basis


def pf4(w, i, j, k, l):
    return (w[i][j] * w[k][l] - w[i][k] * w[j][l] + w[i][l] * w[j][k]) % 5


def pf6(w):
    tot6 = 0
    rest = [1, 2, 3, 4, 5]
    for idx, j in enumerate(rest):
        o = [t for t in rest if t != j]
        tot6 += (-1) ** idx * w[0][j] * pf4(w, o[0], o[1], o[2], o[3])
    return tot6 % 5


LIN = {n: linpart(g) for n, g in zip("abcde", G)}
PB = {n: pullback(LIN[n]) for n in "abc"}
found = {}
high_rank = 0
total_nonzero = 0
for ma, mb, mc in itertools.product((1, 2, 3, 4), repeat=3):
    rows = []
    for n, m in (("a", ma), ("b", mb), ("c", mc)):
        for i in range(15):
            row = PB[n][i][:]
            row[i] = (row[i] - m) % 5
            rows.append(row)
    basis = kernel_mod5(rows, 15)
    if basis:
        found[(ma, mb, mc)] = len(basis)
    for co in itertools.product(range(5), repeat=len(basis)):
        if not any(co):
            continue
        total_nonzero += 1
        vec = [sum(c * b[k] for c, b in zip(co, basis)) % 5 for k in range(15)]
        w = [[0] * 6 for _ in range(6)]
        for k, (i, j) in enumerate(PR):
            w[i][j] = vec[k]
            w[j][i] = (-vec[k]) % 5
        if pf6(w) or any(pf4(w, *q4) for q4 in itertools.combinations(range(6), 4)):
            high_rank += 1
check("A4", "pullback kernels: nonzero only for (1,1,1),(4,1,1),(1,4,4),(4,4,4) with dims 3,3,1,1; all 256 nonzero forms have every 4x4 Pfaffian and the 6x6 Pfaffian zero",
      sorted(found.items()) == [((1, 1, 1), 3), ((1, 4, 4), 1), ((4, 1, 1), 3), ((4, 4, 4), 1)]
      and total_nonzero == 256 and high_rank == 0)

x0 = (0, 0, 0, 0, 0, 0)
x1 = (2, 1, 2, 1, 1, 0)
hist = []
for bit in (0, 1):
    cnt = {}
    for x in ALL:
        y = G[(sum(x) + 2 * bit) % 5](x)
        cnt[y] = cnt.get(y, 0) + 1
    h = {}
    for c in cnt.values():
        h[c] = h.get(c, 0) + 1
    hist.append((len(cnt), sorted(h.items())))
info("selected one-step map, images and preimage histogram for bit 0 and 1: " + str(hist))
check("A5a", "collision 000000 / 212110 at n=0, and images 6250 and 9375",
      step(0, x0) == x0 and step(0, x1) == x0 and hist[0][0] == 6250 and hist[1][0] == 9375)
cur = {}
for x in ALL:
    y = step(2, step(1, step(0, x)))
    cur[y] = cur.get(y, 0) + 1
sync = len(cur) == 3125 and set(cur.values()) == {5}
states = set(cur)
rule = {(0, 0): 4, (1, 1): 3, (0, 1): 1, (1, 0): 1}
common = True
bij = True
LAST = 1500
for n in range(3, LAST + 1):
    bit = tm(n)
    sel = {(sum(x) + 2 * bit) % 5 for x in states}
    common &= sel == {rule[(tm(n - 1), bit)]}
    nxt = {G[(sum(x) + 2 * bit) % 5](x) for x in states}
    bij &= len(nxt) == len(states)
    states = nxt
check("A5b", "sync to 3125 states with 5 preimages each; one common generator by the clock-pair rule and bijectivity on ticks 3..1500",
      sync and common and bij)

# ============================================================ PART B
print("PART B")
LINES = []
for al, be in [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]:
    for gam in range(5):
        LINES.append(frozenset(u for u in F2 if (al * u[0] + be * u[1]) % 5 == gam))
PI5 = []
for L in LINES:
    X = mat_zero()
    for u in sorted(L):
        X = mat_add(X, AM[u])
    PI5.append(X)
rank1 = True
for X in PI5:
    rank1 &= mat_tr(X) == zint(5)
    rank1 &= all(X[i][j] == zconj(X[j][i]) for i in range(5) for j in range(5))
    for i, k in itertools.combinations(range(5), 2):
        for j, l in itertools.combinations(range(5), 2):
            rank1 &= zmul(X[i][j], X[k][l]) == zmul(X[i][l], X[k][j])
check("B1a", "30 lines as solution sets; each line operator is Hermitian, trace 1 and of rank one by vanishing 2x2 minors", len(set(LINES)) == 30 and rank1)
inter = True
for L, X in zip(LINES, PI5):
    for M, Y in zip(LINES, PI5):
        acc = ZERO
        for i in range(5):
            for j in range(5):
                if X[i][j] != ZERO and Y[j][i] != ZERO:
                    acc = zadd(acc, zmul(X[i][j], Y[j][i]))
        inter &= acc == zint(5 * len(L & M))
check("B1b", "Tr(Pi_L Pi_M) = |L cap M|/5 for all 900 pairs", inter)


def wigner_weyl(w):
    # real integer vector; chi(v) = w^T D_v w, W(u) = (1/(25|w|^2)) sum_v z^(r q' - q r') chi(v)
    n2 = sum(t * t for t in w)
    chi = {}
    for (q, r) in F2:
        acc = ZERO
        for k in range(5):
            f = w[(k + q) % 5] * w[k]
            if f:
                zp = ZP[(3 * q * r + r * k) % 5]
                acc = (acc[0] + f * zp[0], acc[1] + f * zp[1], acc[2] + f * zp[2], acc[3] + f * zp[3])
        chi[(q, r)] = acc
    W = {}
    for u in F2:
        acc = ZERO
        for v in F2:
            acc = zadd(acc, zmul(ZP[(u[1] * v[0] - u[0] * v[1]) % 5], chi[v]))
        W[u] = real_q5(acc, 25 * n2)
    return W


def neg_of(W):
    sx = sy = Fr(0)
    for (x, y) in W.values():
        if sgn(x, y) < 0:
            sx -= x
            sy -= y
    return (sx, sy)


LOW = [4, -1, -1, -1, -1]
WL = wigner_weyl(LOW)
mult = {}
for val in WL.values():
    mult[val] = mult.get(val, 0) + 1
check("B4", "Weyl-route LOW Wigner multiset and negativity sqrt5/5",
      mult == {(Fr(1, 5), Fr(0)): 1, (Fr(3, 20), Fr(0)): 4, (Fr(-1, 20), Fr(0)): 4,
               (Fr(1, 40), Fr(1, 40)): 8, (Fr(1, 40), Fr(-1, 40)): 8}
      and neg_of(WL) == (Fr(0), Fr(1, 5)))


def line_probs(w):
    n2 = sum(t * t for t in w)
    out = []
    for X in PI5:
        acc = ZERO
        for i in range(5):
            for j in range(5):
                f = w[i] * w[j]
                if f:
                    e = X[i][j]
                    acc = (acc[0] + f * e[0], acc[1] + f * e[1], acc[2] + f * e[2], acc[3] + f * e[3])
        out.append(real_q5(acc, 5 * n2))
    return out


def invert(pl):
    mu = {}
    for u in F2:
        sx = sy = Fr(0)
        for L, pv in zip(LINES, pl):
            if u in L:
                sx += pv[0]
                sy += pv[1]
        mu[u] = ((sx - 1) / 5, sy / 5)
    return mu


ELL = (0, 1, 2, -2, -1)
inv_ok = invert(line_probs(LOW)) == WL
neg_all = True
bound_all = True
low_ok = True
table = []
for pv in itertools.product(range(5), repeat=4):
    if not any(pv):
        continue
    v = [ELL[t] for t in pv]
    s = sum(v)
    Q = sum(t * t for t in v)
    w = [-s] + [5 * t - s for t in v]
    W = wigner_weyl(w)
    inv_ok &= invert(line_probs(w)) == W
    Nv = neg_of(W)
    neg_all &= sgn(*Nv) > 0
    bound_all &= sgn(Nv[0], Nv[1] - Fr(1, 20)) >= 0
    ox = oy = Fr(0)
    for u in F2:
        ox += W[u][0] * WL[u][0] + 5 * W[u][1] * WL[u][1]
        oy += W[u][0] * WL[u][1] + W[u][1] * WL[u][0]
    low_ok &= (5 * ox, 5 * oy) == (Fr(s * s, 4 * (5 * Q - s * s)), Fr(0))
    table.append(("".join(str(t) for t in pv), Nv))
blob = "".join(nm + " " + str(Nv[0]) + " " + str(Nv[1]) + "\n" for nm, Nv in table).encode("ascii")
tab_sha = hashlib.sha256(blob).hexdigest()
info("negativity table sha256 by the Weyl route " + tab_sha)
check("B2", "inversion from dense line probabilities equals the Weyl-route W for LOW and all 624", inv_ok)
check("B3", "all 624 negativities are positive and at least sqrt5/20", neg_all and bound_all)
check("B5", "overlap with LOW equals s^2/(4(5Q-s^2)) for all 624", low_ok)
vals = {}
for nm, Nv in table:
    vals[Nv] = vals.get(Nv, 0) + 1
nmin = None
nmax = None
for val in vals:
    if nmin is None or sgn(val[0] - nmin[0], val[1] - nmin[1]) < 0:
        nmin = val
    if nmax is None or sgn(val[0] - nmax[0], val[1] - nmax[1]) > 0:
        nmax = val
check("B6", "table hash equals the verifier's; 39 distinct values; minimum (1+sqrt5)/10 at 32 preparations including 1400; maximum 29/220 + (8/55) sqrt5 at 16",
      tab_sha == "c423a1edf376c9cdbd0653b4e89a284ed16e9bfea69586c3cb1c5e208351c905"
      and len(vals) == 39 and nmin == (Fr(1, 10), Fr(1, 10)) and vals[nmin] == 32
      and dict(table)["1400"] == nmin and nmax == (Fr(29, 220), Fr(8, 55)) and vals[nmax] == 16)

# ============================================================ counterexample searches
print("SEARCH")
# S1: every nonzero integer sum-zero vector with entries in [-6,6] at d=5: row r=0 of W.
# 5|w|^2 W(q,0) = c(2q) is an integer; claims: sum zero, a negative entry, negative mass^2 >= (5|w|^2)^2/80.
cnt = 0
bad = 0
for w in itertools.product(range(-6, 7), repeat=4):
    last = -sum(w)
    if abs(last) > 6 or not (any(w) or last):
        continue
    w = w + (last,)
    cnt += 1
    n2 = sum(t * t for t in w)
    c = [sum(w[k] * w[(m - k) % 5] for k in range(5)) for m in range(5)]
    neg = -sum(t for t in c if t < 0)
    if sum(c) != 0 or neg == 0 or 80 * neg * neg < 25 * n2 * n2:
        bad += 1
info("S1 vectors tested: " + str(cnt) + ", violations: " + str(bad))
check("S1", "no integer sum-zero vector with entries in [-6,6] violates the row-zero statement or the bound sqrt5/20", cnt > 0 and bad == 0)

# S2: full negativity by the Weyl route on the box [-3,3]: is anything below the census minimum (1+sqrt5)/10?
cnt2 = 0
below = []
lowest = None
for w in itertools.product(range(-3, 4), repeat=4):
    last = -sum(w)
    if abs(last) > 3 or not (any(w) or last):
        continue
    w = list(w) + [last]
    cnt2 += 1
    Nv = neg_of(wigner_weyl(w))
    if lowest is None or sgn(Nv[0] - lowest[0][0], Nv[1] - lowest[0][1]) < 0:
        lowest = (Nv, tuple(w))
    if sgn(Nv[0] - Fr(1, 10), Nv[1] - Fr(1, 10)) < 0:
        below.append(tuple(w))
info("S2 vectors tested: " + str(cnt2) + "; lowest negativity (" + str(lowest[0][0]) + ") + (" + str(lowest[0][1]) + ")*sqrt5 at " + str(lowest[1]))
info("S2 vectors below (1+sqrt5)/10: " + str(len(below)) + ("" if not below else "; first " + str(below[0])))
check("S2", "every sum-zero vector in the box [-3,3] has positive negativity at least sqrt5/20 (B3); values below the census minimum are reported, not forbidden",
      cnt2 > 0 and sgn(lowest[0][0], lowest[0][1] - Fr(1, 20)) >= 0)

# S3: the row-zero argument in other odd dimensions d = 3, 7, 9
s3 = True
s3n = {}
for d, box in ((3, 4), (7, 1), (9, 1)):
    n_d = 0
    for w in itertools.product(range(-box, box + 1), repeat=d - 1):
        last = -sum(w)
        if abs(last) > box or not (any(w) or last):
            continue
        w = w + (last,)
        n_d += 1
        n2 = sum(t * t for t in w)
        c = [sum(w[k] * w[(m - k) % d] for k in range(d)) for m in range(d)]
        neg = -sum(t for t in c if t < 0)
        s3 &= sum(c) == 0 and neg > 0 and 4 * d * (d - 1) * neg * neg >= d * d * n2 * n2
    s3n[d] = n_d
info("S3 vectors tested by dimension: " + str(sorted(s3n.items())))
check("S3", "row-zero statement and bound 1/(2 sqrt(d(d-1))) hold on the tested boxes for d = 3, 7, 9", s3)

# S4: scope remark of B3: the complex sum-zero Fourier vector is a line state (nonnegative Wigner function)
psi = [ZP[k] for k in range(5)]
ok4 = True
Wc = {}
for u in F2:
    acc = ZERO
    for v in F2:
        chi = ZERO
        for k in range(5):
            term = zmul(zconj(psi[(k + v[0]) % 5]), zmul(ZP[(3 * v[0] * v[1] + v[1] * k) % 5], psi[k]))
            chi = zadd(chi, term)
        acc = zadd(acc, zmul(ZP[(u[1] * v[0] - u[0] * v[1]) % 5], chi))
    Wc[u] = real_q5(acc, 25 * 5)
support = sorted(u for u in F2 if Wc[u] != (Fr(0), Fr(0)))
ok4 = all(Wc[u] == (Fr(1, 5), Fr(0)) for u in support) and len(support) == 5 and frozenset(support) in set(LINES)
info("S4 support of the Fourier vector's Wigner function: " + str(support))
check("S4", "the complex sum-zero vector (1,z,z^2,z^3,z^4) has Wigner function 1/5 on one line and 0 elsewhere", ok4)

print("SUMMARY %d of %d checks PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
