#!/usr/bin/env python3
"""P-AFFINE-READING-CHARACTER-CENSUS-1 accepted verifier.

Exact arithmetic only. Python standard library only. No float in any
assertion, no randomness, no external data, no environment input, no network.
Every gate prints from its own boolean. No gate is a constant true by
inspection.
"""
from fractions import Fraction as Q
from itertools import product

N = 4
ORDER = 20


def eye(n=N):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n=N, m=None):
    m = n if m is None else m
    return [[Q(0)] * m for _ in range(n)]


def mm(X, Y):
    n, k, m = len(X), len(Y), len(Y[0])
    R = [[Q(0)] * m for _ in range(n)]
    for i in range(n):
        Ri = R[i]
        for t in range(k):
            x = X[i][t]
            if x:
                Yt = Y[t]
                for j in range(m):
                    Ri[j] += x * Yt[j]
    return R


def madd(X, Y):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]


def msub(X, Y):
    return [[a - b for a, b in zip(r, s)] for r, s in zip(X, Y)]


def sc(c, X):
    c = Q(c)
    return [[c * a for a in r] for r in X]


def tp(X):
    return [list(r) for r in zip(*X)]


def tr(X):
    return sum(X[i][i] for i in range(len(X)))


def mpow(X, k):
    R = eye(len(X))
    for _ in range(k):
        R = mm(R, X)
    return R


def eqm(X, Y):
    return all(a == b for r, s in zip(X, Y) for a, b in zip(r, s))


def inv(X):
    n = len(X)
    a = [list(X[i]) + list(eye(n)[i]) for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        q = a[j][j]
        a[j] = [x / q for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                f = a[i][j]
                a[i] = [x - f * y for x, y in zip(a[i], a[j])]
    return [r[n:] for r in a]


def rref_pivots(X):
    a = [list(r) for r in X]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    piv = []
    r = 0
    for j in range(cols):
        p = None
        for i in range(r, rows):
            if a[i][j]:
                p = i
                break
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][j]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][j]:
                f = a[i][j]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        piv.append(j)
        r += 1
    return piv


def rank(X):
    return len(rref_pivots(X))


def mv(X, v):
    return [sum(a * b for a, b in zip(r, v)) for r in X]


def charpoly(X):
    n = len(X)
    Mk = zeros(n)
    cs = [Q(1)]
    for k in range(1, n + 1):
        Mk = madd(mm(X, Mk), sc(cs[-1], eye(n)))
        cs.append(-tr(mm(X, Mk)) / k)
    return cs


# ------------------------------------------------------------------ carrier
MJ = [[Q(1), Q(0), Q(-1), Q(1)],
      [Q(0), Q(1), Q(-1), Q(0)],
      [Q(1), Q(0), Q(0), Q(0)],
      [Q(0), Q(1), Q(-1), Q(1)]]
D = msub(MJ, eye())
E0 = [Q(1), Q(0), Q(0), Q(0)]
VV = [mv(mpow(D, k), E0) for k in range(5)]


def colmat(vs):
    return [[vs[j][i] for j in range(len(vs))] for i in range(N)]


BINV = inv(colmat(VV[:4]))
GRP = [(a, b) for a in (1, 2, 3, 4) for b in range(5)]
RHO = {g: mm(colmat([VV[(g[0] * x + g[1]) % 5] for x in range(4)]), BINV)
       for g in GRP}


def gmul(g, h):
    return ((g[0] * h[0]) % 5, (g[1] + g[0] * h[1]) % 5)


G1 = (eqm(mpow(D, 5), eye())
      and charpoly(MJ) == [Q(1), Q(-3), Q(4), Q(-2), Q(1)]
      and all(sum(VV[x][i] for x in range(5)) == 0 for i in range(N))
      and all(eqm(mm(RHO[g], RHO[h]), RHO[gmul(g, h)])
              for g in GRP for h in GRP)
      and eqm(RHO[(1, 1)], D))

# ----------------------------------------------------------- Q(i) scalars
def cx(re, im=0):
    return (Q(re), Q(im))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


IUNIT = [cx(1), cx(0, 1), cx(-1), cx(0, -1)]
LOG2 = {1: 0, 2: 1, 4: 2, 3: 3}


def lam(r, g):
    return IUNIT[(r * LOG2[g[0]]) % 4]


SQUARES = set((k * k) % 5 for k in (1, 2, 3, 4))


def eps_val(g):
    return 1 if g[0] in SQUARES else -1


G2 = (all(cmul(lam(r, g), lam(r, h)) == lam(r, gmul(g, h))
          for r in range(4) for g in GRP for h in GRP)
      and len(set(tuple(lam(r, g) for g in GRP) for r in range(4))) == 4
      and all(cmul(lam(1, g), lam(1, g)) == lam(2, g) for g in GRP)
      and all(lam(2, g) == cx(eps_val(g)) for g in GRP))

# -------------------------------------------------- Sym^d, Method A
def monomials(d):
    out = []
    for a in range(d, -1, -1):
        for b in range(d - a, -1, -1):
            for c in range(d - a - b, -1, -1):
                out.append((a, b, c, d - a - b - c))
    return out


def pmul_lin(poly, row):
    out = {}
    for mon, co in poly.items():
        for j in range(N):
            c = row[j]
            if not c:
                continue
            key = list(mon)
            key[j] += 1
            key = tuple(key)
            out[key] = out.get(key, Q(0)) + co * c
    return dict((k, v) for k, v in out.items() if v)


def sym_op(R, mons, index):
    n = len(mons)
    S = [[Q(0)] * n for _ in range(n)]
    for col, alpha in enumerate(mons):
        poly = {(0, 0, 0, 0): Q(1)}
        for i in range(N):
            for _ in range(alpha[i]):
                poly = pmul_lin(poly, R[i])
        for mon, co in poly.items():
            S[index[mon]][col] = co
    return S


def crank(Are, Aim):
    n = len(Are)
    top = [list(Are[i]) + [-x for x in Aim[i]] for i in range(n)]
    bot = [list(Aim[i]) + list(Are[i]) for i in range(n)]
    r = rank(top + bot)
    return r // 2, r % 2


DMAX_A = 5
methodA = {}
inv_basis = {}
parity_ok = True
extract_ok = True
MONS = {}
SYMOPS = {}
for d in range(DMAX_A + 1):
    mons = monomials(d)
    index = dict((m, i) for i, m in enumerate(mons))
    MONS[d] = mons
    ops = dict((g, sym_op(RHO[g], mons, index)) for g in GRP)
    SYMOPS[d] = ops
    n = len(mons)
    for r in range(4):
        Are = [[Q(0)] * n for _ in range(n)]
        Aim = [[Q(0)] * n for _ in range(n)]
        for g in GRP:
            w = cconj(lam(r, g))
            S = ops[g]
            for i in range(n):
                Si = S[i]
                for j in range(n):
                    s = Si[j]
                    if s:
                        Are[i][j] += w[0] * s
                        Aim[i][j] += w[1] * s
        Are = sc(Q(1, ORDER), Are)
        Aim = sc(Q(1, ORDER), Aim)
        rk, par = crank(Are, Aim)
        if par:
            parity_ok = False
        methodA[(r, d)] = rk
        if r == 0:
            piv = rref_pivots(Are)
            fam = [[Are[i][c] for i in range(n)] for c in piv]
            if len(piv) != rk or rank(fam) != rk:
                extract_ok = False
            for col in fam:
                if not any(col):
                    extract_ok = False
                img = [sum(Are[i][k] * col[k] for k in range(n))
                       for i in range(n)]
                if img != col:
                    extract_ok = False
            inv_basis[d] = [dict((mons[i], col[i])
                                 for i in range(n) if col[i])
                            for col in fam]

# ------------------------------------------------ Molien, Method B
DMAX_B = 12


def series_inv(p, n):
    s = [Q(1)]
    for k in range(1, n + 1):
        acc = Q(0)
        for j in range(1, min(k, 4) + 1):
            acc += p[j] * s[k - j]
        s.append(-acc)
    return s


SER = dict((g, series_inv(charpoly(RHO[g]), DMAX_B)) for g in GRP)


def chi_V(g):
    return sum(1 for x in range(5) if (g[0] * x + g[1]) % 5 == x) - 1


methodB = {}
integral_ok = True
for r in range(4):
    for d in range(DMAX_B + 1):
        acc = cx(0)
        for g in GRP:
            acc = cadd(acc, cmul(cconj(lam(r, g)), cx(SER[g][d])))
        val = (acc[0] / ORDER, acc[1] / ORDER)
        if val[1] != 0 or val[0].denominator != 1 or val[0] < 0:
            integral_ok = False
        methodB[(r, d)] = int(val[0])

multV = {}
for d in range(DMAX_B + 1):
    acc = sum(Q(chi_V(g)) * SER[g][d] for g in GRP) / ORDER
    if acc.denominator != 1 or acc < 0:
        integral_ok = False
    multV[d] = int(acc)

# ------------------------------------------------------------- G3, G4
G3 = all(methodA[(r, 1)] == 0 and methodB[(r, 1)] == 0 for r in range(4))

GRAM = msub(eye(), sc(Q(1, 5), [[Q(1)] * N for _ in range(N)]))
QP = sc(Q(5, 2), GRAM)
QM = [[Q(0), Q(1), Q(-1), Q(-1)],
      [Q(1), Q(0), Q(1), Q(-1)],
      [Q(-1), Q(1), Q(0), Q(1)],
      [Q(-1), Q(-1), Q(1), Q(0)]]
forms_ok = all(eqm(mm(mm(tp(RHO[g]), QP), RHO[g]), QP)
               and eqm(mm(mm(tp(RHO[g]), QM), RHO[g]), sc(eps_val(g), QM))
               for g in GRP)
G4 = (methodA[(0, 2)] == 1 and methodA[(2, 2)] == 1
      and methodA[(1, 2)] == 0 and methodA[(3, 2)] == 0
      and all(methodA[(r, 2)] == methodB[(r, 2)] for r in range(4))
      and forms_ok)

G5 = all(methodA[(r, d)] == methodB[(r, d)]
         for r in range(4) for d in range(DMAX_A + 1))


def binom3(d):
    return (d + 1) * (d + 2) * (d + 3) // 6


CENSUS = {0: (1, 0, 0, 0, 0), 1: (0, 0, 0, 0, 1), 2: (1, 1, 0, 0, 2),
          3: (1, 1, 1, 1, 4), 4: (3, 2, 1, 1, 7), 5: (3, 3, 3, 3, 11)}
G6 = all((methodB[(0, d)], methodB[(2, d)], methodB[(1, d)],
          methodB[(3, d)], multV[d]) == CENSUS[d]
         for d in range(DMAX_A + 1))

G7 = (all(sum(methodB[(r, d)] for r in range(4)) + 4 * multV[d] == binom3(d)
          for d in range(DMAX_A + 1))
      and all(methodB[(1, d)] == methodB[(3, d)] for d in range(DMAX_B + 1))
      and integral_ok)

MOLIEN_1 = [1, 0, 1, 1, 3, 3, 5, 6, 10, 11, 16, 18, 25]
MOLIEN_E = [0, 0, 1, 1, 2, 3, 5, 6, 9, 11, 16, 18, 24]
MOLIEN_I = [0, 0, 0, 1, 1, 3, 3, 6, 7, 11, 13, 18, 21]
G8 = ([methodB[(0, d)] for d in range(DMAX_B + 1)] == MOLIEN_1
      and [methodB[(2, d)] for d in range(DMAX_B + 1)] == MOLIEN_E
      and [methodB[(1, d)] for d in range(DMAX_B + 1)] == MOLIEN_I)

CHIVALS = sorted(set(chi_V(g) for g in GRP))
G9 = (CHIVALS == [-1, 0, 4]
      and all(not eqm(RHO[g], sc(-1, eye())) for g in GRP))

ODD = [d for d in range(1, DMAX_B + 1, 2) if methodB[(0, d)] > 0]
D_ODD = ODD[0] if ODD else 0
G10 = (D_ODD == 3)

# ------------------------------------------------------------- G11
def pzero():
    return {}


def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, Q(0)) + v
    return dict((k, v) for k, v in o.items() if v)


def pmul(a, b):
    o = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            k = tuple(m1[i] + m2[i] for i in range(N))
            o[k] = o.get(k, Q(0)) + c1 * c2
    return dict((k, v) for k, v in o.items() if v)


def pscale(c, a):
    return dict((k, Q(c) * v) for k, v in a.items())


def var(i, e=1):
    m = [0] * N
    m[i] = e
    return {tuple(m): Q(1)}


P1 = padd(padd(var(0), var(1)), padd(var(2), var(3)))
P3 = padd(padd(var(0, 3), var(1, 3)), padd(var(2, 3), var(3, 3)))
QPOLY = pzero()
for i in range(N):
    for j in range(N):
        if QP[i][j]:
            m = [0] * N
            m[i] += 1
            m[j] += 1
            QPOLY = padd(QPOLY, {tuple(m): QP[i][j]})
KSTAR = pscale(Q(1, 3), padd(padd(pmul(pmul(P1, P1), P1),
                                  pscale(6, pmul(P1, QPOLY))),
                             pscale(-25, P3)))


def apply_sym(poly, d, g):
    mons = MONS[d]
    index = dict((m, i) for i, m in enumerate(mons))
    S = SYMOPS[d][g]
    vec = [poly.get(m, Q(0)) for m in mons]
    outv = [sum(S[i][j] * vec[j] for j in range(len(mons)))
            for i in range(len(mons))]
    return dict((mons[i], outv[i]) for i in range(len(mons)) if outv[i])


kstar_int = all(v.denominator == 1 for v in KSTAR.values())
kstar_coeffs = sorted(set(int(v) for v in KSTAR.values())) if kstar_int else []
kstar_fixed = all(apply_sym(KSTAR, 3, g) == KSTAR for g in GRP)
proj3 = inv_basis.get(3, [])
kstar_in_span = False
if len(proj3) == 1:
    base = proj3[0]
    keys = set(base) | set(KSTAR)
    ratios = set()
    for k in keys:
        bv = base.get(k, Q(0))
        kv = KSTAR.get(k, Q(0))
        if bv == 0 and kv == 0:
            continue
        if bv == 0 or kv == 0:
            ratios.add(None)
        else:
            ratios.add(kv / bv)
    kstar_in_span = len(ratios) == 1 and None not in ratios
G11 = (kstar_int and len(KSTAR) == 20 and kstar_coeffs == [-4, 3]
       and kstar_fixed and kstar_in_span)

G12 = extract_ok and parity_ok and all(
    len(inv_basis[d]) == methodB[(0, d)] for d in range(DMAX_A + 1))

# ------------------------------------------------------------- G13
def qform(F, x):
    return sum(F[i][j] * x[i] * x[j] for i in range(N) for j in range(N))


WITX = None
for cand in product((-1, 0, 1), repeat=4):
    xv = [Q(c) for c in cand]
    if qform(QM, xv) != 0:
        WITX = xv
        break
WITG = None
for g in GRP:
    if eps_val(g) == -1:
        WITG = g
        break
G13 = False
if WITX is not None and WITG is not None:
    wy = mv(RHO[WITG], WITX)
    G13 = (qform(QM, WITX) != 0
           and qform(QP, wy) == qform(QP, WITX)
           and qform(QM, wy) == -qform(QM, WITX))

# ------------------------------------------------------------- G14
TEST = [tuple(Q(c) for c in t)
        for t in product((-2, -1, 0, 1, 2), repeat=4) if any(t)]


def evalpoly(poly, x):
    acc = Q(0)
    for mon, co in poly.items():
        term = co
        for i in range(N):
            for _ in range(mon[i]):
                term *= x[i]
        acc += term
    return acc


ORB = {}
for x in TEST:
    if x in ORB:
        continue
    rep = x
    for g in GRP:
        y = tuple(mv(RHO[g], list(x)))
        ORB[y] = rep
ORBIT_COUNT = len(set(ORB[x] for x in TEST))

CUM = []
counts, classes, colls = [], [], []
for d in range(DMAX_A + 1):
    CUM.extend(inv_basis[d])
    counts.append(len(CUM))
    buckets = {}
    for x in TEST:
        key = tuple(evalpoly(p, x) for p in CUM)
        buckets.setdefault(key, []).append(x)
    classes.append(len(buckets))
    bad = 0
    for key in buckets:
        mem = buckets[key]
        for other in mem[1:]:
            if ORB.get(other) is not ORB.get(mem[0]):
                bad += 1
    colls.append(bad)

G14 = (counts == [1, 1, 2, 3, 6, 9]
       and classes == [1, 1, 18, 45, 84, 86]
       and colls == [619, 619, 474, 264, 8, 0]
       and ORBIT_COUNT == 86
       and classes[-1] == ORBIT_COUNT)

GATES = [("G1 CARRIER INTEGRITY", G1),
         ("G2 FOUR LINEAR CHARACTERS", G2),
         ("G3 LINEAR VOID EVERY CHARACTER SECTOR", G3),
         ("G4 QUADRATIC SECTOR ONE AND EPSILON ONLY", G4),
         ("G5 METHOD A EQUALS METHOD B 24 CELLS", G5),
         ("G6 FROZEN CENSUS TABLE THROUGH DEGREE 5", G6),
         ("G7 TOTAL DIMENSION AND GALOIS PAIRING", G7),
         ("G8 FROZEN MOLIEN ROWS THROUGH DEGREE 12", G8),
         ("G9 CHI_V VALUES AND NO MINUS IDENTITY", G9),
         ("G10 SMALLEST ODD INVARIANT DEGREE IS 3", G10),
         ("G11 CUBIC INVARIANT AND CLOSED FORM", G11),
         ("G12 BASIS EXTRACTION RANK INTEGRITY", G12),
         ("G13 SIGN WITNESS", G13),
         ("G14 ORBIT SEPARATION MINIMAL DEGREE 5", G14)]

print('P-AFFINE-READING-CHARACTER-CENSUS-1')
print('LAYER L1 EXACT ARITHMETIC ONLY')
for name, ok in GATES:
    print(name, 'PASS' if ok else 'FAIL')
print('CHI_V VALUE SET', ' '.join(str(c) for c in CHIVALS))
print('SMALLEST ODD INVARIANT DEGREE', D_ODD)
print('CUBIC MONOMIALS', len(KSTAR), 'COEFFICIENT SET',
      ' '.join(str(c) for c in kstar_coeffs))
for d in range(DMAX_A + 1):
    print('DEGREE', d, 'DIM', binom3(d), 'M1', methodB[(0, d)],
          'MEPS', methodB[(2, d)], 'MI', methodB[(1, d)],
          'MIBAR', methodB[(3, d)], 'MV', multV[d])
print('MOLIEN INVARIANT', ' '.join(str(methodB[(0, d)])
                                   for d in range(DMAX_B + 1)))
print('MOLIEN EPSILON', ' '.join(str(methodB[(2, d)])
                                 for d in range(DMAX_B + 1)))
print('MOLIEN ORDER FOUR', ' '.join(str(methodB[(1, d)])
                                    for d in range(DMAX_B + 1)))
print('FINGERPRINT INVARIANTS', ' '.join(str(c) for c in counts))
print('FINGERPRINT CLASSES', ' '.join(str(c) for c in classes))
print('FINGERPRINT COLLISIONS', ' '.join(str(c) for c in colls))
print('EXACT ORBIT COUNT', ORBIT_COUNT)
print('NO APPARATUS RECORD MEASUREMENT BORN LIGHT MATTER COSMOLOGY CLAIMED')
print('DECISION', 'READING-CENSUS-CERTIFIED'
      if all(ok for _, ok in GATES) else 'ROUTE-FALSIFIED')
