#!/usr/bin/env python3
"""Exact audit for the note C-QUADRATIC-MEMORY-NATIVE-WORD-COUNT-N.

NON-CANONICAL.  Python standard library only, integer arithmetic modulo 5,
deterministic, no file writes, no network access.  Every check prints one
line; a failed check prints [FAIL] and the program exits with status 1.

Conventions.  A cell is a vector (p1, p4, p1p, p4p, q, t) of F5^6; W is the
space of the four piston coordinates and R = (q, t).  A pair is z = (cell x,
cell y) in F5^12.  The four constants and the five kernel generators are
restated verbatim from reproduce/kernel-connectivity/verify.py of the
repository (its lines 41 to 73); that file is not imported.  Each generator
is applied to one cell while the other cell is fixed; the couplings are
P(x,y) = (x, y+x) and Q(x,y) = (x+y, y).  Words are compositions applied
right to left.

C = K + 0_2 with K = antidiag(3,2,2,3) on W;  G(x,y) = (x^T K x, x^T K y,
y^T K y) = (a,b,c);  Canon target M(a,b,c) = (3b, 4a+4b+4c, 3b+3c);  reduced
target M0(a,b,c) = (a+c, b, c).
"""
import sys
from itertools import product

sys.stdout.reconfigure(encoding="ascii", newline=chr(10))

P = 5
FAILED = []
COUNT = [0]


def check(label, condition, detail=""):
    COUNT[0] += 1
    if not condition:
        FAILED.append(COUNT[0])
    print("[%s] C%02d %s%s" % ("PASS" if condition else "FAIL", COUNT[0], label,
                               (": " + detail) if detail else ""))


# ---------------------------------------------------------------- matrices
def mm(a, b):
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) % P for col in cols]
            for row in a]


def mv(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) % P for row in a)


def ident(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def tr(a):
    return [list(r) for r in zip(*a)]


def inv(m):
    n = len(m)
    a = [[m[i][j] % P for j in range(n)] + [1 if i == j else 0 for j in range(n)]
         for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if a[r][c])
        a[c], a[piv] = a[piv], a[c]
        iv = pow(a[c][c], 3, P)
        a[c] = [(v * iv) % P for v in a[c]]
        for r in range(n):
            if r != c and a[r][c]:
                f = a[r][c]
                a[r] = [(v - f * w) % P for v, w in zip(a[r], a[c])]
    return [row[n:] for row in a]


def rank(rows):
    m = [list(r) for r in rows]
    rk = 0
    ncol = len(m[0]) if m else 0
    for c in range(ncol):
        piv = next((r for r in range(rk, len(m)) if m[r][c] % P), None)
        if piv is None:
            continue
        m[rk], m[piv] = m[piv], m[rk]
        iv = pow(m[rk][c], 3, P)
        m[rk] = [(v * iv) % P for v in m[rk]]
        for r in range(len(m)):
            if r != rk and m[r][c] % P:
                f = m[r][c]
                m[r] = [(v - f * w) % P for v, w in zip(m[r], m[rk])]
        rk += 1
    return rk


# ------------------------------------------- 1. the kernel generators (verbatim)
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x):
    p1, p4, p1p, p4p, q, t = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-t) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, t = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + t * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + t * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + t * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + t * U_VEC[3]) % 5,
            (1 - q) % 5, (-t) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


CELL = (("a", gen_a), ("b", gen_b), ("c", gen_c), ("d", gen_d), ("e", gen_e))


def affine_of(f, n):
    """(matrix, vector) of the affine map agreeing with f at 0 and at the unit vectors."""
    v = f((0,) * n)
    cols = []
    for j in range(n):
        e = [0] * n
        e[j] = 1
        w = f(tuple(e))
        cols.append([(w[i] - v[i]) % P for i in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)], tuple(v)


STATES6 = list(product(range(P), repeat=6))
CELL_FORM = {}
affine_ok = True
involution_ok = True
for name, g in CELL:
    m, v = affine_of(g, 6)
    CELL_FORM[name] = (m, v)
    for x in STATES6:
        if g(x) != tuple((s + t) % P for s, t in zip(mv(m, x), v)):
            affine_ok = False
        if g(g(x)) != x:
            involution_ok = False
check("the five generators, restated verbatim, are affine involutions on all 15625 cell states",
      affine_ok and involution_ok,
      "translations a %s, b %s, c %s, d %s, e %s" % tuple(CELL_FORM[n][1] for n in "abcde"))


def on_x(g):
    return lambda z: g(z[:6]) + z[6:]


def on_y(g):
    return lambda z: z[:6] + g(z[6:])


def coup_p(z):
    return z[:6] + tuple((z[6 + i] + z[i]) % P for i in range(6))


def coup_q(z):
    return tuple((z[i] + z[6 + i]) % P for i in range(6)) + z[6:]


FUN = {}
for name, g in CELL:
    FUN[name + "x"] = on_x(g)
    FUN[name + "y"] = on_y(g)
FUN["P"] = coup_p
FUN["Q"] = coup_q
NAMES = ["ax", "ay", "bx", "by", "cx", "cy", "dx", "dy", "ex", "ey", "P", "Q"]
LIN = {}
TRA = {}
for name in NAMES:
    LIN[name], TRA[name] = affine_of(FUN[name], 12)


def word(*names):
    """the composition names[0] o names[1] o ... (applied right to left)."""
    def f(z):
        for n in reversed(names):
            z = FUN[n](z)
        return z
    return f


def mpow(m, k):
    r = ident(len(m))
    for _ in range(k):
        r = mm(r, m)
    return r


WIDX = [0, 1, 2, 3, 6, 7, 8, 9]
RIDX = [4, 5, 10, 11]
I12 = ident(12)
check("slotwise generators and couplings: the radical output never depends on the pistons; "
      "P and Q have order 5",
      all(LIN[n][r][c] == 0 for n in NAMES for r in RIDX for c in WIDX)
      and mpow(LIN["P"], 5) == I12 and mpow(LIN["Q"], 5) == I12
      and TRA["P"] == (0,) * 12 and TRA["Q"] == (0,) * 12)

# ------------------------------------------------ 2. eigenbasis and adapted basis
AW = [row[:4] for row in CELL_FORM["a"][0][:4]]
BW = [row[:4] for row in CELL_FORM["b"][0][:4]]
CW = [row[:4] for row in CELL_FORM["c"][0][:4]]
I4 = ident(4)
KM = [[0, 0, 0, 3], [0, 0, 2, 0], [0, 2, 0, 0], [3, 0, 0, 0]]
EV = [(1, 1, 4, 4), (1, 1, 1, 1), (1, 4, 4, 1), (1, 4, 1, 4)]          # ++, +-, -+, --
CHI_A = (1, 1, 4, 4)
CHI_B = (1, 4, 1, 4)
E4 = [[EV[j][i] for j in range(4)] for i in range(4)]                  # columns = eigenvectors
E4I = inv(E4)
check("W-blocks of a and b commute, square to 1, c has the W-block of b; joint eigenvectors "
      "(1,1,4,4), (1,1,1,1), (1,4,4,1), (1,4,1,4); K = antidiag(3,2,2,3) again in that basis",
      mm(AW, BW) == mm(BW, AW) and mm(AW, AW) == I4 and mm(BW, BW) == I4 and CW == BW
      and all(mv(AW, EV[j]) == tuple(CHI_A[j] * t % P for t in EV[j]) for j in range(4))
      and all(mv(BW, EV[j]) == tuple(CHI_B[j] * t % P for t in EV[j]) for j in range(4))
      and mm(mm(tr(E4), KM), E4) == KM)

BASIS = []
for j in range(4):
    BASIS.append(EV[j] + (0, 0) + (0,) * 6)
    BASIS.append((0,) * 6 + EV[j] + (0, 0))
BASIS.append((0, 0, 0, 0, 1, 0) + (0,) * 6)
BASIS.append((0,) * 6 + (0, 0, 0, 0, 1, 0))
BASIS.append((0, 0, 0, 0, 0, 1) + (0,) * 6)
BASIS.append((0,) * 6 + (0, 0, 0, 0, 0, 1))
BM = [[BASIS[j][i] for j in range(12)] for i in range(12)]
BMI = inv(BM)
ADL = {n: mm(mm(BMI, LIN[n]), BM) for n in NAMES}


def block(m, i, j):
    return ((m[2 * i][2 * j], m[2 * i][2 * j + 1]), (m[2 * i + 1][2 * j], m[2 * i + 1][2 * j + 1]))


def dx(e):
    return ((e, 0), (0, 1))


def dy(e):
    return ((1, 0), (0, e))


ZERO2 = ((0, 0), (0, 0))
EXPECT = {}
for slot, dd in (("x", dx), ("y", dy)):
    EXPECT["a" + slot] = [dd(CHI_A[j]) for j in range(4)] + [dd(1), dd(1)]
    EXPECT["b" + slot] = [dd(CHI_B[j]) for j in range(4)] + [dd(4), dd(4)]
    EXPECT["c" + slot] = EXPECT["b" + slot]
    EXPECT["d" + slot] = [dd(4)] * 6
    EXPECT["e" + slot] = [dd(4)] * 6
EXPECT["P"] = [((1, 0), (1, 1))] * 6
EXPECT["Q"] = [((1, 1), (0, 1))] * 6
COUPLING = {"cx": {(0, 5): ((3, 0), (0, 0)), (2, 5): ((2, 0), (0, 0))},
            "cy": {(0, 5): ((0, 0), (0, 3)), (2, 5): ((0, 0), (0, 2))}}
form_ok = True
for n in NAMES:
    for i in range(6):
        for j in range(6):
            want = EXPECT[n][i] if i == j else COUPLING.get(n, {}).get((i, j), ZERO2)
            if block(ADL[n], i, j) != want:
                form_ok = False
check("adapted basis (planes ++, +-, -+, --, q, t): every generator acts on each plane by the "
      "tabulated 2x2 matrix, on the q- and t-planes as on the plane +-, and the only coupling "
      "is t -> planes ++ and -+ in c (u = 3 e_++ + 2 e_-+)", form_ok)


def det2(g):
    return (g[0][0] * g[1][1] - g[0][1] * g[1][0]) % P


PATTERN = {n: tuple(det2(block(ADL[n], j, j)) for j in range(4)) for n in NAMES}
patterns = {(1, 1, 1, 1)}
frontier = [(1, 1, 1, 1)]
while frontier:
    cur = frontier.pop()
    for n in NAMES:
        nxt = tuple(a * b % P for a, b in zip(cur, PATTERN[n]))
        if nxt not in patterns:
            patterns.add(nxt)
            frontier.append(nxt)
PROD_ONE = {p for p in product((1, 4), repeat=4) if p[0] * p[1] * p[2] * p[3] % P == 1}
check("determinant patterns of the generators on the four eigenlines generate exactly the 8 "
      "patterns of product 1", patterns == PROD_ONE and len(patterns) == 8,
      "a %s, b %s, d %s, P %s" % (PATTERN["ax"], PATTERN["bx"], PATTERN["dx"], PATTERN["P"]))


# ------------------------------------------------ 3. Lambda contains SL2^4
def mul2(a, b):
    return (((a[0][0] * b[0][0] + a[0][1] * b[1][0]) % P, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % P),
            ((a[1][0] * b[0][0] + a[1][1] * b[1][0]) % P, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % P))


def inv2(a):
    d = pow(det2(a), 3, P)
    return ((a[1][1] * d % P, -a[0][1] * d % P), (-a[1][0] * d % P, a[0][0] * d % P))


ONE2 = ((1, 0), (0, 1))
MINUS2 = ((4, 0), (0, 4))


def generated(gens):
    seen = {ONE2}
    frontier = [ONE2]
    while frontier:
        cur = frontier.pop()
        for g in gens:
            nxt = mul2(cur, g)
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return seen


def tup(name):
    return tuple(block(ADL[name], j, j) for j in range(4))


def tmul(*ts):
    out = ts[0]
    for t in ts[1:]:
        out = tuple(mul2(a, b) for a, b in zip(out, t))
    return out


def tinv(t):
    return tuple(inv2(a) for a in t)


def tcomm(s, t):
    return tmul(s, t, tinv(s), tinv(t))


T_LOW = block(ADL["P"], 0, 0)
T_UPP = block(ADL["Q"], 0, 0)
SL2 = generated([T_LOW, T_UPP])
AXT, BXT, PT, QT = tup("ax"), tup("bx"), tup("P"), tup("Q")
ABT = tmul(AXT, BXT)
XA = [tmul(AXT, s, tinv(AXT), tinv(s)) for s in (PT, QT)]        # (1, 1, c, c)
XB = [tmul(BXT, s, tinv(BXT), tinv(s)) for s in (PT, QT)]        # (1, c, 1, c)
XAB = [tmul(ABT, s, tinv(ABT), tinv(s)) for s in (PT, QT)]       # (1, c, c, 1)
Y4 = tcomm(XA[0], XB[1])                                         # (1, 1, 1, y)
Y3 = tcomm(XA[0], XAB[1])                                        # (1, 1, y, 1)
Y2 = tcomm(XB[0], XAB[1])                                        # (1, y, 1, 1)
YEL = Y4[3]
shape_ok = (XA[0][0] == ONE2 and XA[0][1] == ONE2 and XA[0][2] == XA[0][3]
            and XB[0][0] == ONE2 and XB[0][2] == ONE2 and XB[0][1] == XB[0][3]
            and XAB[0][0] == ONE2 and XAB[0][3] == ONE2 and XAB[0][1] == XAB[0][2]
            and Y4 == (ONE2, ONE2, ONE2, YEL) and Y3 == (ONE2, ONE2, YEL, ONE2)
            and Y2 == (ONE2, YEL, ONE2, ONE2) and YEL not in (ONE2, MINUS2))
NORMAL = generated([mul2(mul2(r, YEL), inv2(r)) for r in sorted(SL2)])
check("Lambda contains SL2(F5)^4: P, Q generate a diagonal SL2 of order 120; explicit "
      "commutator words give (1,1,1,y), (1,1,y,1), (1,y,1,1) with y not central, and the "
      "conjugates of y generate SL2",
      len(SL2) == 120 and shape_ok and NORMAL == SL2,
      "y = %s; hence |Lambda| = 8 * 120^4 = %d" % (YEL, 8 * 120 ** 4))

# ------------------------------------------------ 4. unipotent part and translations
INVL = {n: inv(ADL[n]) for n in NAMES}
U0 = mm(ADL["cx"], INVL["bx"])
NIL0 = [[(U0[i][j] - (1 if i == j else 0)) % P for j in range(12)] for i in range(12)]
unip_shape = all(NIL0[i][j] == 0 for i in range(12) for j in range(12) if not (i < 8 and j >= 10))
span = [sum(NIL0, [])]
mats = [NIL0]
grew = True
while grew:
    grew = False
    for m in list(mats):
        for n in NAMES:
            c = mm(mm(ADL[n], m), INVL[n])
            flat = sum(c, [])
            if rank(span + [flat]) > rank(span):
                span.append(flat)
                mats.append(c)
                grew = True
touched = sorted({(i // 2, j // 2) for m in mats for i in range(12) for j in range(12) if m[i][j]})
check("c_x b_x^-1 is unipotent with a t -> W part only; its conjugates span all linear maps "
      "from the t-plane to the planes ++ and -+",
      unip_shape and rank(span) == 8 and touched == [(0, 5), (2, 5)], "dimension %d" % rank(span))

WORDS = [("e_x d_x", ("ex", "dx"), (0, 0, 0, 0, 1, 0) + (0,) * 6),
         ("d_x P d_x P", ("dx", "P", "dx", "P"), (0,) * 6 + (2, 1, 3, 4, 1, 1)),
         ("(c_x d_x)^2", ("cx", "dx", "cx", "dx"), (4, 3, 4, 1, 0, 3) + (0,) * 6)]
tspan = []
dims = []
words_ok = True
for label, names, want in WORDS:
    w = word(*names)
    m, v = affine_of(w, 12)                 # 13 direct evaluations of the generator functions
    words_ok &= m == I12 and v == want
    tspan.append(list(v))
    grew = True
    while grew:
        grew = False
        for t in list(tspan):
            for n in NAMES:
                u = list(mv(LIN[n], t))
                if rank(tspan + [u]) > rank(tspan):
                    tspan.append(u)
                    grew = True
    dims.append(rank(tspan))
check("the words e_x d_x, d_x P d_x P, (c_x d_x)^2 (applied right to left) are the translations "
      "by (q_x unit), (2,1,3,4,1,1) in cell y, (4,3,4,1,0,3) in cell x; closures under the "
      "linear parts", words_ok and dims == [2, 8, 12], "dimensions %s" % dims)

GOUT = ((0, 1), (2, 1))
GIN = ((1, 1), (3, 1))
check("Lemma 1(b) of the earlier note: det g_out det g_in = 4, and the pattern (4,4,4,4) "
      "has product 1, so the reduction maps Lambda onto itself",
      det2(GOUT) * det2(GIN) % P == 4 and (4, 4, 4, 4) in patterns)

# ------------------------------------------------ 5. tables for W^2 in piston coordinates
VEC4 = list(product(range(P), repeat=4))
IDX4 = {v: i for i, v in enumerate(VEC4)}
ADD = [[0] * 625 for _ in range(625)]
for i, u in enumerate(VEC4):
    row = ADD[i]
    for j, v in enumerate(VEC4):
        row[j] = IDX4[((u[0] + v[0]) % P, (u[1] + v[1]) % P, (u[2] + v[2]) % P, (u[3] + v[3]) % P)]
KV = [mv(KM, v) for v in VEC4]
QQ = [sum(a * b for a, b in zip(KV[i], VEC4[i])) % P for i in range(625)]
Q25 = [25 * t for t in QQ]
B5 = []
for i in range(625):
    k = KV[i]
    B5.append(bytearray(5 * ((k[0] * v[0] + k[1] * v[1] + k[2] * v[2] + k[3] * v[3]) % P) for v in VEC4))
MCODE = [0] * 125
for g in range(125):
    a, b, c = g // 25, (g // 5) % 5, g % 5
    MCODE[g] = 25 * ((3 * b) % P) + 5 * ((4 * a + 4 * b + 4 * c) % P) + (3 * b + 3 * c) % P
TARGET = []
for i in range(625):
    qi = Q25[i]
    bi = B5[i]
    TARGET.append(bytearray(MCODE[qi + bi[j] + QQ[j]] for j in range(625)))
N8 = 390625


def table(mat, shift=(0, 0, 0, 0)):
    return [IDX4[tuple((mat[r][0] * v[0] + mat[r][1] * v[1] + mat[r][2] * v[2] + mat[r][3] * v[3] + shift[r]) % P
                       for r in range(4))] for v in VEC4]


def diag_map(d):
    """E diag(d) E^-1: the element of A acting by d_j on the j-th eigenline."""
    return mm(mm(E4, [[d[i] if i == j else 0 for j in range(4)] for i in range(4)]), E4I)


def eig_vec(t):
    return mv(E4, t)


ONES = (1, 1, 1, 1)
NONE = (0, 0, 0, 0)


def canon_agreement(dd, nn, d2, t=NONE):
    """Agreement mask on all 5^8 inputs, C = K, Canon target M, of the map of W^2 that is, in
    reduced eigen-coordinates, (x, y) -> (D x + N y + t, D' y) with D = diag(dd), N = diag(nn),
    D' = diag(d2).  In Canon coordinates (substitution of Lemma 1(b)) this is the map
    (x, y) -> ((4D + 3N + 2D') x + (D + 4N + D') y + 2t, (2D + 4N) x + (3D + 2N) y + t)."""
    tp = eig_vec(t)
    a11 = table(diag_map(tuple((4 * a + 3 * b + 2 * c) % P for a, b, c in zip(dd, nn, d2))),
                tuple(2 * v % P for v in tp))
    a12 = table(diag_map(tuple((a + 4 * b + c) % P for a, b, c in zip(dd, nn, d2))))
    a21 = table(diag_map(tuple((2 * a + 4 * b) % P for a, b in zip(dd, nn))), tp)
    a22 = table(diag_map(tuple((3 * a + 2 * b) % P for a, b in zip(dd, nn))))
    out = bytearray(N8)
    q25, b5, qq = Q25, B5, QQ
    for i in range(625):
        r1 = ADD[a11[i]]
        r2 = ADD[a21[i]]
        tg = TARGET[i]
        base = i * 625
        for j in range(625):
            ox = r1[a12[j]]
            oy = r2[a22[j]]
            if q25[ox] + b5[ox][oy] + qq[oy] == tg[j]:
                out[base + j] = 1
    return out


def native_induced(dd, d2):
    """the reduced blocks [[D_j, N_j], [0, D'_j]] on the four eigenlines have determinants +-1
    with product 1, so the map is induced by a native word (Theorem S, Corollaries 1 and 2)."""
    dets = [a * b % P for a, b in zip(dd, d2)]
    return all(x in (1, 4) for x in dets) and dets[0] * dets[1] * dets[2] * dets[3] % P == 1


def inside(mask, sel):
    return sum(1 for a, b in zip(mask, sel) if a and b)


# ------------------------------------------------ 6. tangent words and the set U
SKEW = []
ISOM = 0
for d in product(range(P), repeat=4):
    m = diag_map(d)
    km = mm(KM, m)
    if all((km[i][j] + km[j][i]) % P == 0 for i in range(4) for j in range(4)):
        SKEW.append((d, m))
    if all(d) and mm(mm(tr(m), KM), m) == KM:
        ISOM += 1
nilpotent = sum(1 for d, m in SKEW if any(d) and mm(m, m) == [[0] * 4 for _ in range(4)])
check("K-skew maps in A: 25, all of the form diag(s, r, -r, -s) in the eigenbasis, no nonzero "
      "one nilpotent; isometries of K in A: 16",
      len(SKEW) == 25 and all(d[2] == (-d[1]) % P and d[3] == (-d[0]) % P for d, m in SKEW)
      and nilpotent == 0 and ISOM == 16)

UNION = bytearray(N8)
sizes = {}
for d, m in SKEW:
    mask = canon_agreement(ONES, d, ONES)
    s = sum(mask)
    sizes[s] = sizes.get(s, 0) + 1
    UNION = bytearray(a | b for a, b in zip(UNION, mask))
U_SIZE = N8 - sum(UNION)
check("Proposition T/U, C = K, Canon target M, all 5^8 inputs: agreement sets of the 25 "
      "tangent words have sizes 90625, 80625 (8 times), 78625 (16 times); their union misses "
      "20800 inputs",
      sizes == {90625: 1, 80625: 8, 78625: 16} and U_SIZE == 20800,
      "covered %d, missed %d" % (sum(UNION), U_SIZE))

# half classes in reduced eigen-coordinates
HC = [[0] * 25 for _ in range(25)]                # 1: E0, 2: E12, 3: B'
ZC = [[0] * 25 for _ in range(25)]                # 1: v = 0 or v' = 0
half_count = [0, 0, 0, 0]
zero_count = 0
for x, x2, y, y2 in product(range(P), repeat=4):
    c = (y * y2) % P
    w = (y * x2 - x * y2) % P
    if y == 0 and y2 == 0:
        cls = 1                                   # E0
    elif c == 0 and w == 0:
        cls = 2                                   # E12
    elif c != 0 and w in (c, (-c) % P):
        cls = 3                                   # B'
    else:
        cls = 0
    HC[x * 5 + x2][y * 5 + y2] = cls
    half_count[cls] += 1
    if (x == 0 and y == 0) or (x2 == 0 and y2 == 0):
        ZC[x * 5 + x2][y * 5 + y2] = 1
        zero_count += 1
EIGC = [mv(E4I, v) for v in VEC4]
DKEY = [e[0] * 5 + e[3] for e in EIGC]            # eigenlines ++ and --
AKEY = [e[1] * 5 + e[2] for e in EIGC]            # eigenlines +- and -+
SC = [[IDX4[tuple(k * c % P for c in v)] for v in VEC4] for k in range(P)]
IN_U = bytearray(N8)
IN_U1 = bytearray(N8)
IN_O = bytearray(N8)
gram_on_o = set()
for i in range(625):
    base = i * 625
    for j in range(625):
        xr = ADD[SC[2][i]][SC[3][j]]              # reduced data (2x + 3y, 4x + 2y)
        yr = ADD[SC[4][i]][SC[2][j]]
        cd = HC[DKEY[xr]][DKEY[yr]]
        ca = HC[AKEY[xr]][AKEY[yr]]
        if (cd == 3 and ca in (1, 2)) or (ca == 3 and cd in (1, 2)):
            IN_U[base + j] = 1
            if cd == 2 or ca == 2:
                IN_U1[base + j] = 1
            if (cd == 3 and ZC[AKEY[xr]][AKEY[yr]]) or (ca == 3 and ZC[DKEY[xr]][DKEY[yr]]):
                IN_O[base + j] = 1
                gram_on_o.add(Q25[i] + B5[i][j] + QQ[j])
check("Proposition U: the missed inputs are exactly E x B' u B' x E in reduced "
      "eigen-coordinates (pointwise); |E0| = 25, |E12| = 40, |B'| = 160",
      half_count[1:] == [25, 40, 160] and all(a + b == 1 for a, b in zip(UNION, IN_U)),
      "|U| = %d" % sum(IN_U))
check("test sets: O (one half with a zero vector, the other in B') has 15680 inputs, U1 (one "
      "half in E12, the other in B') has 12800, and U1 lies in O, O in U",
      zero_count == 49 and sum(IN_O) == 15680 and sum(IN_U1) == 12800
      and all(a <= b <= c for a, b, c in zip(IN_U1, IN_O, IN_U)),
      "|O| = %d, |U1| = %d, Gram values on O: %d" % (sum(IN_O), sum(IN_U1), len(gram_on_o)))

# native words of zero translation: the 25 tangent words and 30 further linear ones
LIN_UNION = bytearray(UNION)
lin_native = True
lin_count = 0
for k in (2, 3, 4):
    ki = pow(k, 3, P)
    for psi in range(P):
        for dd, nn, d2 in (((k, 1, 1, 1), (0, psi, (-psi) % P, 0), (ki, 1, 1, 1)),
                           ((1, k, 1, 1), (psi, 0, 0, (-psi) % P), (1, ki, 1, 1))):
            lin_native &= native_induced(dd, d2)
            lin_count += 1
            LIN_UNION = bytearray(a | b for a, b in zip(LIN_UNION, canon_agreement(dd, nn, d2)))
check("Proposition O: the 25 tangent words and %d further maps induced by native words of zero "
      "translation agree with every input outside O and with no input of O" % lin_count,
      lin_native and lin_count == 30 and all(a + b == 1 for a, b in zip(LIN_UNION, IN_O)),
      "covered %d, missed %d" % (sum(LIN_UNION), N8 - sum(LIN_UNION)))

T_WIT = (1, 1, 4, 1)
MASK_T = canon_agreement(ONES, NONE, ONES, T_WIT)
check("Theorem L: 15680 > 24 * 640, and 640 inputs of O are reached by the translation word "
      "(x,y) -> (x + 2y + 2t, 2x + 3y + t), t = e_++ + e_+- + 4 e_-+ + e_--",
      15680 > 24 * 640 and native_induced(ONES, ONES) and inside(MASK_T, IN_O) == 640,
      "agreement set %d, inside O %d" % (sum(MASK_T), inside(MASK_T, IN_O)))

# ------------------------------------------------ 7. the bound 520 on U1
HALF = list(product(range(P), repeat=4))          # (x, y, x', y')
BPRIME = [u for u in HALF if (u[1] * u[3]) % P
          and (u[1] * u[2] - u[0] * u[3]) % P in ((u[1] * u[3]) % P, (-u[1] * u[3]) % P)]
NONZERO2 = [v for v in product(range(P), repeat=2) if any(v)]
ROOTS = [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
psi_max_other = 0
full_tuples = {}
for root in ROOTS:
    rhs = [((x * root[0] + y * root[1]) * (x2 * root[0] + y2 * root[1]) + y * y2 * root[0] * root[0]) % P
           for x, y, x2, y2 in BPRIME]
    lin1 = {a: [(x * a[0] + y * a[1]) % P for x, y, x2, y2 in BPRIME] for a in NONZERO2}
    lin2 = {a: [(x2 * a[0] + y2 * a[1]) % P for x, y, x2, y2 in BPRIME] for a in NONZERO2}
    full_tuples[root] = []
    for a in NONZERO2:
        l1 = lin1[a]
        for a2 in NONZERO2:
            trip = list(zip(l1, lin2[a2], rhs))
            for al in range(P):
                for al2 in range(P):
                    cnt = 0
                    for p1, p2, r in trip:
                        if ((p1 + al) * (p2 + al2) - r) % P == 0:
                            cnt += 1
                    if cnt == 160:
                        full_tuples[root].append((a, al, a2, al2))
                    elif cnt > psi_max_other:
                        psi_max_other = cnt
check("Lemma 2: for the six root points P the count psi_P(A, alpha, A', alpha') on B' is at "
      "most 64, except for P = (0,1) and the four tuples ((0,m), 0, (0,1/m), 0), where it is 160",
      psi_max_other == 64
      and full_tuples[(0, 1)] == [((0, m), 0, (0, pow(m, 3, P)), 0) for m in range(1, P)]
      and all(not full_tuples[r] for r in ROOTS[1:]),
      "largest other value %d over %d tuples" % (psi_max_other, 6 * 24 * 24 * 25))

zmin = {0: 999, 1: 999, 2: 999}
fc_zero = True
family = 0
for m in range(1, P):
    mi = pow(m, 3, P)
    for d in (mi, (-mi) % P):                     # det g = d m = +-1
        for d2 in (m, (-m) % P):                  # det g' = d2 / m = +-1
            for n in range(P):
                for n2 in range(P):
                    for t in range(P):
                        for t2 in range(P):
                            family += 1
                            z = 0
                            for x, y, x2, y2 in BPRIME:
                                xo = d * x + n * y + t
                                yo = m * y
                                xo2 = d2 * x2 + n2 * y2 + t2
                                yo2 = mi * y2
                                if (yo * yo2 - y * y2) % P:
                                    fc_zero = False
                                if (xo * yo2 + yo * xo2 - x * y2 - y * x2) % P == 0:
                                    z += 1
                            k = (t != 0) + (t2 != 0)
                            if z < zmin[k]:
                                zmin[k] = z
both = max(kd * (160 - zmin[ka]) + ka * (160 - zmin[kd]) for kd in range(3) for ka in range(3))
BOUND = max(2 * psi_max_other + 2 * 160, both)
check("Lemma 3: on the 10000 half-maps with g, g' upper triangular, g22 g'22 = 1 and "
      "translations on the x-axis, F^c vanishes on B' and F^b vanishes at 30 points of B' or "
      "more when both translations are nonzero",
      family == 10000 and fc_zero and zmin[2] == 30,
      "least number of zeros by number of nonzero translations: %s" % [zmin[k] for k in range(3)])
check("Proposition W, arithmetic: no map with linear part in Lambda agrees on more than 520 "
      "inputs of U1, and 12800 > 24 * 520",
      BOUND == 520 and 12800 > 24 * BOUND,
      "one half outside the family: at most %d; both inside: at most %d"
      % (2 * psi_max_other + 2 * 160, both))

# ------------------------------------------------ 8. witnesses
MASK_W = canon_agreement(ONES, (0, 0, 1, 1), ONES, ONES)
check("520 is attained: the map with reduced form (x + nu y + t, y), nu = diag(0,0,1,1), "
      "t = e_++ + e_+- + e_-+ + e_--, is induced by a native word and agrees on 520 inputs of U1",
      native_induced(ONES, ONES) and inside(MASK_W, IN_U1) == 520,
      "agreement set %d, inside U1 %d, inside O %d, inside U %d"
      % (sum(MASK_W), inside(MASK_W, IN_U1), inside(MASK_W, IN_O), inside(MASK_W, IN_U)))
check("the translation word of the check for Theorem L agrees on 880 inputs of U",
      inside(MASK_T, IN_U) == 880, "inside U %d" % inside(MASK_T, IN_U))
NU_P = diag_map((0, 0, 1, 0))
km = mm(KM, NU_P)
MASK_P = canon_agreement(ONES, (0, 0, 1, 0), ONES)
check("nu = diag(0,0,1,0) lies in A and is not K-skew; the map with reduced form (x + nu y, y) "
      "is induced by a native word, is not of tangent type and agrees on 40625 inputs",
      mm(NU_P, AW) == mm(AW, NU_P) and mm(NU_P, BW) == mm(BW, NU_P)
      and any((km[i][j] + km[j][i]) % P for i in range(4) for j in range(4))
      and native_induced(ONES, ONES) and sum(MASK_P) == 40625,
      "agreement set %d, inside U %d" % (sum(MASK_P), inside(MASK_P, IN_U)))

# ------------------------------------------------ 9. an explicit cover
# words "sr:t1t2t3t4": reduced map (x, y) -> (x + psi y + t, y) with psi = diag(s, r, -r, -s) and
# t = t1 e_++ + t2 e_+- + t3 e_-+ + t4 e_--; Canon form as in canon_agreement
COVER_WORDS = (
    "00:0000 11:0000 22:0000 44:0000 01:0000 10:0000 34:0000 20:0000 02:0000 "
    "03:0000 30:0000 14:0000 41:0000 12:0000 00:1111 00:1122 00:1133 00:1144 "
    "00:2211 00:2222 00:2233 00:2244 00:3311 00:3322 00:3333 00:3344 00:4411 "
    "00:4422 00:4433 00:4444 02:1312 02:1324 02:1331 02:1343 03:4212 03:4224 "
    "03:4231 03:4243 24:3300 11:2413 11:2421 11:2434 11:2442 13:3300 30:3113 "
    "30:3121 30:3134 30:3142 20:2413 20:2421 20:2434 20:2442 11:1312 11:1324 "
    "11:1331 11:1343 11:1414 11:1423 11:1432 11:1441 01:1100 44:4114 44:4123 "
    "44:4132 44:4141 "
).split()
covered = bytearray(N8)
most_o = 0
most_u1 = 0
for wd in COVER_WORDS:
    s_, r_ = int(wd[0]), int(wd[1])
    t = tuple(int(ch) for ch in wd[3:])
    mask = canon_agreement(ONES, (s_, r_, (-r_) % P, (-s_) % P), ONES, t)
    most_o = max(most_o, inside(mask, IN_O))
    most_u1 = max(most_u1, inside(mask, IN_U1))
    covered = bytearray(a | b for a, b in zip(covered, mask))
check("upper bound: the %d listed maps are induced by native words and their agreement sets "
      "cover all 390625 inputs (C = K, Canon target M)" % len(COVER_WORDS),
      native_induced(ONES, ONES) and sum(covered) == N8 and len(set(COVER_WORDS)) == len(COVER_WORDS)
      and most_o <= 640 and most_u1 <= 520,
      "covered %d, tangent members %d, largest part of O %d, of U1 %d"
      % (sum(covered), sum(1 for wd in COVER_WORDS if wd[3:] == "0000"), most_o, most_u1))

print("%s (%d checks)" % ("ALL CHECKS PASS" if not FAILED else "CHECKS FAILED", COUNT[0]))
sys.exit(1 if FAILED else 0)
