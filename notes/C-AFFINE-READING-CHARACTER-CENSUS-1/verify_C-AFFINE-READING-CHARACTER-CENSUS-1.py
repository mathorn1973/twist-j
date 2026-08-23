#!/usr/bin/env python3
# C-AFFINE-READING-CHARACTER-CENSUS-1 accepted verifier.
# Exact arithmetic only. Python standard library only. No float in any
# assertion, no randomness, no external data, no environment input, no network.
from fractions import Fraction as Q
from itertools import product

# ---------------------------------------------------------------- primitives
def eye(n=4):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]

def zeros(n=4, m=None):
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

def eq(X, Y):
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
        p = next((i for i in range(r, rows) if a[i][j]), None)
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

# ---------------------------------------------------------------- carrier, G1
MJ = [[Q(1), Q(0), Q(-1), Q(1)],
      [Q(0), Q(1), Q(-1), Q(0)],
      [Q(1), Q(0), Q(0), Q(0)],
      [Q(0), Q(1), Q(-1), Q(1)]]
D = msub(MJ, eye())

def charpoly(X):
    n = len(X)
    Mk = zeros(n)
    cs = [Q(1)]
    for k in range(1, n + 1):
        Mk = madd(mm(X, Mk), sc(cs[-1], eye(n)))
        cs.append(-tr(mm(X, Mk)) / k)
    return cs

def mv(X, v):
    return [sum(a * b for a, b in zip(r, v)) for r in X]

e0 = [Q(1), Q(0), Q(0), Q(0)]
vv = [mv(mpow(D, k), e0) for k in range(5)]

def colmat(vs):
    return [[vs[j][i] for j in range(len(vs))] for i in range(4)]

Binv = inv(colmat(vv[:4]))

def rho_of(a, b):
    return mm(colmat([vv[(a * x + b) % 5] for x in range(4)]), Binv)

GRP = [(a, b) for a in (1, 2, 3, 4) for b in range(5)]
RHO = {g: rho_of(*g) for g in GRP}

def gmul(g, h):
    a, b = g
    c, d = h
    return ((a * c) % 5, (b + a * d) % 5)

g1_pow = eq(mpow(D, 5), eye())
g1_chi = charpoly(MJ) == [Q(1), Q(-3), Q(4), Q(-2), Q(1)]
g1_sum = all(sum(vv[x][i] for x in range(5)) == 0 for i in range(4))
g1_hom = all(eq(mm(RHO[g], RHO[h]), RHO[gmul(g, h)]) for g in GRP for h in GRP)
g1_step = eq(RHO[(1, 1)], D)
G1 = g1_pow and g1_chi and g1_sum and g1_hom and g1_step

# ------------------------------------------------- Gaussian rational scalars
def cx(re, im=0):
    return (Q(re), Q(im))

def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def cconj(x):
    return (x[0], -x[1])

I_UNIT = [cx(1), cx(0, 1), cx(-1), cx(0, -1)]
LOG2 = {1: 0, 2: 1, 4: 2, 3: 3}

def lam(r, g):
    return I_UNIT[(r * LOG2[g[0]]) % 4]

# ------------------------------------------------------------------- G2
g2_hom = all(cmul(lam(r, g), lam(r, h)) == lam(r, gmul(g, h))
             for r in range(4) for g in GRP for h in GRP)
g2_distinct = len({tuple(lam(r, g) for g in GRP) for r in range(4)}) == 4
g2_eps = all(cmul(lam(1, g), lam(1, g)) == lam(2, g) for g in GRP)
G2 = g2_hom and g2_distinct and g2_eps

def eps_val(g):
    return 1 if g[0] in (1, 4) else -1

g2_epsmatch = all(lam(2, g) == cx(eps_val(g)) for g in GRP)
G2 = G2 and g2_epsmatch

# ------------------------------------------- Sym^d operators, Method A
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
        for j in range(4):
            c = row[j]
            if not c:
                continue
            key = list(mon)
            key[j] += 1
            key = tuple(key)
            out[key] = out.get(key, Q(0)) + co * c
    return {k: v for k, v in out.items() if v}

def sym_op(R, d, mons, index):
    # column alpha is the expansion of prod_i ( (R x)_i )^alpha_i
    n = len(mons)
    S = [[Q(0)] * n for _ in range(n)]
    for col, alpha in enumerate(mons):
        poly = {(0, 0, 0, 0): Q(1)}
        for i in range(4):
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
invariant_basis = {}
A_parity_ok = True
for d in range(DMAX_A + 1):
    mons = monomials(d)
    index = {m: i for i, m in enumerate(mons)}
    ops = {g: sym_op(RHO[g], d, mons, index) for g in GRP}
    for r in range(4):
        n = len(mons)
        Are = [[Q(0)] * n for _ in range(n)]
        Aim = [[Q(0)] * n for _ in range(n)]
        for g in GRP:
            w = cconj(lam(r, g))
            S = ops[g]
            for i in range(n):
                for j in range(n):
                    s = S[i][j]
                    if s:
                        Are[i][j] += w[0] * s
                        Aim[i][j] += w[1] * s
        Are = sc(Q(1, 20), Are)
        Aim = sc(Q(1, 20), Aim)
        rk, par = crank(Are, Aim)
        if par:
            A_parity_ok = False
        methodA[(r, d)] = rk
        if r == 0:
            piv = rref_pivots(tp(Are))
            invariant_basis[d] = [
                ({mons[i]: Are[i][c] for i in range(n) if Are[i][c]})
                for c in piv]

# ------------------------------------------------ Molien series, Method B
DMAX_B = 12

def det_poly(R):
    # det(I - t R) as an exact coefficient list of length 5
    cs = charpoly(R)  # x^4 + cs1 x^3 + cs2 x^2 + cs3 x + cs4
    # det(I - tR) = t^4 * det((1/t) I - R) = t^4 * charpoly(R)(1/t)
    return [Q(1), cs[1], cs[2], cs[3], cs[4]]

def series_inv(p, n):
    s = [Q(1)]
    for k in range(1, n + 1):
        acc = Q(0)
        for j in range(1, min(k, 4) + 1):
            acc += p[j] * s[k - j]
        s.append(-acc)
    return s

SER = {g: series_inv(det_poly(RHO[g]), DMAX_B) for g in GRP}

def chi_V(g):
    return sum(1 for x in range(5) if (g[0] * x + g[1]) % 5 == x) - 1

methodB = {}
B_integral = True
for r in range(4):
    for d in range(DMAX_B + 1):
        acc = cx(0)
        for g in GRP:
            acc = cadd(acc, cmul(cconj(lam(r, g)), cx(SER[g][d])))
        val = (acc[0] / 20, acc[1] / 20)
        if val[1] != 0 or val[0].denominator != 1 or val[0] < 0:
            B_integral = False
        methodB[(r, d)] = int(val[0])

mult_V = {}
for d in range(DMAX_B + 1):
    acc = sum(Q(chi_V(g)) * SER[g][d] for g in GRP) / 20
    if acc.denominator != 1 or acc < 0:
        B_integral = False
    mult_V[d] = int(acc)

# ------------------------------------------------------------------ G3, G4
G3 = all(methodA[(r, 1)] == 0 and methodB[(r, 1)] == 0 for r in range(4))

Gm = msub(eye(), sc(Q(1, 5), [[Q(1)] * 4 for _ in range(4)]))
qp = sc(Q(5, 2), Gm)
qm = [[Q(0), Q(1), Q(-1), Q(-1)],
      [Q(1), Q(0), Q(1), Q(-1)],
      [Q(-1), Q(1), Q(0), Q(1)],
      [Q(-1), Q(-1), Q(1), Q(0)]]
forms_ok = all(eq(mm(mm(tp(RHO[g]), qp), RHO[g]), qp) and
               eq(mm(mm(tp(RHO[g]), qm), RHO[g]), sc(eps_val(g), qm))
               for g in GRP)
G4 = (methodA[(0, 2)] == 1 and methodA[(2, 2)] == 1 and
      methodA[(1, 2)] == 0 and methodA[(3, 2)] == 0 and
      all(methodA[(r, 2)] == methodB[(r, 2)] for r in range(4)) and forms_ok)

# --------------------------------------------------------------------- G5
G5 = all(methodA[(r, d)] == methodB[(r, d)]
         for r in range(4) for d in range(DMAX_A + 1))

# --------------------------------------------------------------------- G6
def binom3(d):
    return (d + 1) * (d + 2) * (d + 3) // 6

G6a = all(sum(methodB[(r, d)] for r in range(4)) + 4 * mult_V[d] == binom3(d)
          for d in range(DMAX_A + 1))
G6b = all(methodB[(1, d)] == methodB[(3, d)] for d in range(DMAX_B + 1))
G6 = G6a and G6b and B_integral and A_parity_ok

# --------------------------------------------------------------------- G7
chi_values = sorted({chi_V(g) for g in GRP})
no_minus_I = all(not eq(RHO[g], sc(-1, eye())) for g in GRP)
odd_degrees = [d for d in range(1, DMAX_B + 1, 2) if methodB[(0, d)] > 0]
d_odd = odd_degrees[0] if odd_degrees else 0
G7 = (chi_values == [-1, 0, 4]) and no_minus_I and (d_odd >= 3)

# --------------------------------------------------------------------- G8
def qform(F, x):
    return sum(F[i][j] * x[i] * x[j] for i in range(4) for j in range(4))

wit_x = None
for cand in product((-1, 0, 1), repeat=4):
    xv = [Q(c) for c in cand]
    if qform(qm, xv) != 0:
        wit_x = xv
        break
wit_g = next(g for g in GRP if eps_val(g) == -1)
wit_y = mv(RHO[wit_g], wit_x)
G8 = (wit_x is not None and
      qform(qp, wit_y) == qform(qp, wit_x) and
      qform(qm, wit_y) == -qform(qm, wit_x) and
      qform(qm, wit_x) != 0)

# --------------------------------------------------------------------- G9
TEST = [tuple(Q(c) for c in t) for t in product((-2, -1, 0, 1, 2), repeat=4)
        if any(t)]

def evalpoly(poly, x):
    acc = Q(0)
    for mon, co in poly.items():
        term = co
        for i in range(4):
            for _ in range(mon[i]):
                term *= x[i]
        acc += term
    return acc

basis_all = [p for d in range(DMAX_A + 1) for p in invariant_basis[d]]
buckets = {}
for x in TEST:
    key = tuple(evalpoly(p, x) for p in basis_all)
    buckets.setdefault(key, []).append(x)

def same_orbit(x, y):
    return any(tuple(mv(RHO[g], list(x))) == y for g in GRP)

separating = True
collisions = 0
for key, members in buckets.items():
    base = members[0]
    for other in members[1:]:
        if not same_orbit(base, other):
            separating = False
            collisions += 1
G9LABEL = "SEPARATING-AT-5" if separating else "NON-SEPARATING-AT-5"

minus_pairs = [x for x in TEST
               if not same_orbit(x, tuple(-c for c in x))]
sign_read = all(
    tuple(evalpoly(p, x) for p in basis_all) !=
    tuple(evalpoly(p, tuple(-c for c in x)) for p in basis_all)
    for x in minus_pairs[:1]) if minus_pairs else False

OK = G1 and G2 and G3 and G4 and G5 and G6 and G7 and G8

print('C-AFFINE-READING-CHARACTER-CENSUS-1')
print('LAYER L1 EXACT ARITHMETIC ONLY')
print('CANDIDATE NO AUTHORITY')
print('G1 CARRIER INTEGRITY', 'PASS' if G1 else 'FAIL')
print('G2 FOUR LINEAR CHARACTERS', 'PASS' if G2 else 'FAIL')
print('G3 LINEAR VOID IN EVERY CHARACTER SECTOR', 'PASS' if G3 else 'FAIL')
print('G4 QUADRATIC SECTOR 1 AND EPSILON ONLY', 'PASS' if G4 else 'FAIL')
print('G5 METHOD A EQUALS METHOD B THROUGH DEGREE', DMAX_A,
      'PASS' if G5 else 'FAIL')
print('G6 TOTAL DIMENSION AND GALOIS PAIRING', 'PASS' if G6 else 'FAIL')
print('G7 NO ELEMENT ACTS AS MINUS I', 'PASS' if G7 else 'FAIL')
print('G8 SIGN WITNESS', 'PASS' if G8 else 'FAIL')
print('CHI_V VALUE SET', ' '.join(str(c) for c in chi_values))
print('SMALLEST ODD INVARIANT DEGREE', d_odd)
for d in range(DMAX_A + 1):
    print('DEGREE', d, 'DIM', binom3(d),
          'M1', methodB[(0, d)], 'MEPS', methodB[(2, d)],
          'MI', methodB[(1, d)], 'MIBAR', methodB[(3, d)],
          'MV', mult_V[d])
print('MOLIEN INVARIANT COEFFICIENTS 0 TO', DMAX_B,
      ' '.join(str(methodB[(0, d)]) for d in range(DMAX_B + 1)))
print('MOLIEN EPSILON COEFFICIENTS 0 TO', DMAX_B,
      ' '.join(str(methodB[(2, d)]) for d in range(DMAX_B + 1)))
print('MOLIEN ORDER FOUR COEFFICIENTS 0 TO', DMAX_B,
      ' '.join(str(methodB[(1, d)]) for d in range(DMAX_B + 1)))
print('G9 RECORDED', G9LABEL, 'COLLISIONS', collisions)
print('SIGN PAIR SEPARATED BY INVARIANTS', 'YES' if sign_read else 'NO')
print('NO APPARATUS RECORD MEASUREMENT BORN LIGHT MATTER COSMOLOGY CLAIMED')
print('DECISION', 'READING-CENSUS-CERTIFIED' if OK else 'ROUTE-FALSIFIED')
