#!/usr/bin/env python3
"""Exact audit for the note C-QUADRATIC-MEMORY-AFFINE-BRANCH-COUNT-N.

NON-CANONICAL.  Python standard library only, integer arithmetic modulo 5,
deterministic, no file writes, no network access.  Every check prints one
line; a failed check prints [FAIL] and the program exits with status 1.

Conventions.  Vectors of F5^n are tuples, indexed with the first coordinate
most significant.  For a symmetric C the Gram map is
G(x,y) = (x^T C x, x^T C y, y^T C y) = (a,b,c).  Canon target
M(a,b,c) = (3b, 4a+4b+4c, 3b+3c); reduced target M0(a,b,c) = (a+c, b, c).
A tangent branch is (x,y) -> (x + psi y, y) with C psi antisymmetric; it
agrees with M0 at (x,y) exactly when 2B(x, psi y) + q(psi y) = q(y).
"""
import sys
from itertools import combinations, product

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


def tr(a):
    return [list(row) for row in zip(*a)]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zeros(n):
    return [[0] * n for _ in range(n)]


def madd(a, b):
    return [[(x + y) % P for x, y in zip(r, s)] for r, s in zip(a, b)]


def mscale(s, a):
    return [[s * x % P for x in row] for row in a]


def kron(a, b):
    return [[x * y % P for x in ra for y in rb] for ra in a for rb in b]


def minv(a):
    n = len(a)
    w = [list(row) + [int(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for col in range(n):
        piv = next(i for i in range(col, n) if w[i][col] % P)
        w[col], w[piv] = w[piv], w[col]
        s = pow(w[col][col], -1, P)
        w[col] = [x * s % P for x in w[col]]
        for i in range(n):
            if i != col and w[i][col]:
                k = w[i][col]
                w[i] = [(x - k * y) % P for x, y in zip(w[i], w[col])]
    return [row[n:] for row in w]


def det(a):
    n = len(a)
    if n == 1:
        return a[0][0] % P
    return sum((-1) ** j * a[0][j] * det([row[:j] + row[j + 1:] for row in a[1:]])
               for j in range(n)) % P


def diag(d):
    return [[d[i] if i == j else 0 for j in range(len(d))]
            for i in range(len(d))]


def is_antisym(a):
    n = len(a)
    return all((a[i][j] + a[j][i]) % P == 0
               for i in range(n) for j in range(n))


def qd(cd, v):
    return sum(c * a * a for c, a in zip(cd, v)) % P


def bd(cd, u, v):
    return sum(c * a * b for c, a, b in zip(cd, u, v)) % P


def sym2(g):
    (p, q), (s, u) = g
    return [[p * p % P, 2 * p * q % P, q * q % P],
            [p * s % P, (p * u + q * s) % P, q * u % P],
            [s * s % P, 2 * s * u % P, u * u % P]]


def proj_point(v):
    k = next(x for x in v if x % P)
    s = pow(k, -1, P)
    return tuple(x * s % P for x in v)


# ------------------------------------------------- 1. reading and reduction
B_MARK = [[1, 4, 2], [4, 0, 1], [3, 4, 4]]
L5 = [[3, 3, 2], [3, 4, 2], [3, 2, 0]]
M = [[0, 3, 0], [4, 4, 4], [0, 3, 3]]
M0 = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
G_OUT = [[0, 1], [2, 1]]
G_IN = [[1, 1], [3, 1]]
G_OUT_INV = [[2, 3], [1, 0]]
G_IN_INV = [[2, 3], [4, 2]]

check("marked reading: B M = L5 B, (1,1,2)B = (1,2,1), (1,1,2)L5 B = (3,4,1)",
      mm(B_MARK, M) == mm(L5, B_MARK)
      and mm([[1, 1, 2]], B_MARK) == [[1, 2, 1]]
      and mm(mm([[1, 1, 2]], L5), B_MARK) == [[3, 4, 1]])
check("reduction: Sym2(g_out) M Sym2(g_in) = M0, with the stated inverses",
      mm(mm(sym2(G_OUT), M), sym2(G_IN)) == M0
      and mm(G_OUT, G_OUT_INV) == ident(2) and mm(G_IN, G_IN_INV) == ident(2))


def gram_action_ok():
    cd = (1, 2)
    for g in (G_OUT, G_IN, G_OUT_INV, G_IN_INV):
        s2 = sym2(g)
        for x in product(range(P), repeat=2):
            for y in product(range(P), repeat=2):
                x2 = tuple((g[0][0] * a + g[0][1] * b) % P for a, b in zip(x, y))
                y2 = tuple((g[1][0] * a + g[1][1] * b) % P for a, b in zip(x, y))
                lhs = (qd(cd, x2), bd(cd, x2, y2), qd(cd, y2))
                if lhs != mv(s2, (qd(cd, x), bd(cd, x, y), qd(cd, y))):
                    return False
    return True


check("Gram action G((g x 1)z) = Sym2(g) G(z): exhaustive on F5^4 for the four g",
      gram_action_ok())
check("Lemma 3 identity: lambda M0 = (la, lb, la+lc), det L' = det L + la^2, all 125 lambda",
      all(mm([list(l)], M0) == [[l[0], l[1], (l[0] + l[2]) % P]]
          and (4 * l[0] * (l[0] + l[2]) - l[1] * l[1]) % P
          == (4 * l[0] * l[2] - l[1] * l[1] + 4 * l[0] * l[0]) % P
          for l in product(range(P), repeat=3)))


def weight_lemma_small():
    """Lemma A for N = 1 (degree <= 4) and N = 2 (degree <= 2), all polynomials."""
    worst1 = 0
    for co in product(range(P), repeat=5):
        if not any(co):
            continue
        deg = max(k for k in range(5) if co[k])
        total = 0
        for a in range(P):
            if sum(c * a ** k for k, c in enumerate(co)) % P == 0:
                d1 = sum(k * c * a ** (k - 1) for k, c in enumerate(co) if k) % P
                total += 2 if d1 == 0 else 1
        if total > deg:
            return None
        worst1 = max(worst1, total - deg)
    tight2 = 0
    for c0, c1, c2, c3, c4, c5 in product(range(P), repeat=6):
        if c3 or c4 or c5:
            deg = 2
        elif c1 or c2:
            deg = 1
        elif c0:
            deg = 0
        else:
            continue
        total = 0
        for u in range(P):
            for v in range(P):
                if (c0 + c1 * u + c2 * v + c3 * u * u + c4 * u * v + c5 * v * v) % P == 0:
                    du = (c1 + 2 * c3 * u + c4 * v) % P
                    dv = (c2 + c4 * u + 2 * c5 * v) % P
                    total += 2 if du == 0 and dv == 0 else 1
        if total > deg * 5:
            return None
        tight2 += total == deg * 5
    return worst1, tight2


WL = weight_lemma_small()
check("Lemma A, all univariate P of degree <= 4 and all bivariate P of degree <= 2",
      WL is not None, "bivariate cases with equality: %s" % (WL[1] if WL else "-"))

# ------------------------------------------------------ 2. quaternion pair
LI = [[0, 4, 0, 0], [1, 0, 0, 0], [0, 0, 0, 4], [0, 0, 1, 0]]
LJ = [[0, 0, 4, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 4, 0, 0]]
I4 = ident(4)
NEG_I4 = mscale(4, I4)
ZERO4 = zeros(4)
SIX = [(3, 0), (0, 1), (1, 1), (2, 3), (4, 2), (4, 3)]
DP = madd(LI, mscale(2, LJ))
DM = madd(LI, mscale(3, LJ))

check("Li, Lj antisymmetric, Li^2 = Lj^2 = -I, Li Lj + Lj Li = 0",
      is_antisym(LI) and is_antisym(LJ) and mm(LI, LI) == NEG_I4
      and mm(LJ, LJ) == NEG_I4 and madd(mm(LI, LJ), mm(LJ, LI)) == ZERO4)
check("six pairs: alpha^2 + beta^2 - 1 = alpha (mod 5); six distinct points of P1(F5)",
      all((a * a + b * b - 1 - a) % P == 0 for a, b in SIX)
      and len({proj_point(p) for p in SIX}) == 6)
check("D+ = Li + 2 Lj, D- = Li + 3 Lj: squares 0, D+ D- + D- D+ = I; the six pairs "
      "are a D+ + b D- with (a,b) on the cross through (4,4)",
      mm(DP, DP) == ZERO4 and mm(DM, DM) == ZERO4
      and madd(mm(DP, DM), mm(DM, DP)) == I4
      and sorted(((3 * a + 4 * b) % P, (3 * a + b) % P) for a, b in SIX)
      == [(0, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 4)])


def psi_six(pair):
    return madd(mscale(pair[0], LI), mscale(pair[1], LJ))


def block(a, b, c, d):
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def canon_branch(psi):
    """(x,y) -> (x + 2y + psi(3x+4y), 2x + 3y + psi(4x+2y))."""
    return block(madd(I4, mscale(3, psi)), madd(mscale(2, I4), mscale(4, psi)),
                 madd(mscale(2, I4), mscale(4, psi)), madd(mscale(3, I4), mscale(2, psi)))


def reduced_branch(psi):
    return block(I4, psi, ZERO4, I4)


check("Canon formula equals (g_out^-1 x 1)(x + psi y, y)(g_in^-1 x 1) for the six psi",
      all(canon_branch(psi_six(p))
          == mm(mm(kron(G_OUT_INV, I4), reduced_branch(psi_six(p))), kron(G_IN_INV, I4))
          for p in SIX))

# ------------------------------------------------------- tables for F5^4
VEC4 = [tuple((i // 5 ** (3 - k)) % 5 for k in range(4)) for i in range(625)]
IDX4 = {v: i for i, v in enumerate(VEC4)}
PACK4 = [sum(d << (4 * (3 - k)) for k, d in enumerate(v)) for v in VEC4]
RED = [0] * 65536
for _p in range(65536):
    RED[_p] = ((((_p >> 12) & 15) % 5 * 5 + ((_p >> 8) & 15) % 5) * 5
               + ((_p >> 4) & 15) % 5) * 5 + (_p & 15) % 5
DOT = [bytes((a * w + b * x + c * y + d * z) % 5 for (w, x, y, z) in VEC4)
       for (a, b, c, d) in VEC4]
DOT5 = [bytes(5 * t for t in row) for row in DOT]
FULL625 = (1 << 625) - 1
ZERO8 = (0,) * 8


def cover_stats(cmat, branches, target, want_fibres=False):
    """Direct evaluation of G(Az + t) = target*G(z) at every z of F5^8.

    branches: list of (A, t) with A an 8 x 8 matrix and t a vector of F5^8.
    """
    cidx = [IDX4[mv(cmat, v)] for v in VEC4]
    qt = [DOT[cidx[i]][i] for i in range(625)]
    q25 = [25 * t for t in qt]
    b5 = [DOT5[cidx[i]] for i in range(625)]
    mt = [0] * 125
    for g in range(125):
        t = mv(target, (g // 25, (g // 5) % 5, g % 5))
        mt[g] = t[0] * 25 + t[1] * 5 + t[2]
    tg = [0] * 390625
    for x in range(625):
        row = b5[x]
        base = x * 625
        qx = q25[x]
        for y in range(625):
            tg[base + y] = mt[qx + row[y] + qt[y]]
    pat = bytearray(390625)
    sizes = []
    bc_all = []
    outs = []
    red = RED
    for bit, (a, tvec) in enumerate(branches):
        ax = [row[:4] for row in a]
        ay = [row[4:] for row in a]
        tp = (PACK4[IDX4[tuple(tvec[:4])]] << 16) | PACK4[IDX4[tuple(tvec[4:])]]
        xp = []
        yp = []
        for v in VEC4:
            u = mv(ax, v)
            xp.append(((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]]) + tp)
            u = mv(ay, v)
            yp.append((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]])
        mask = 1 << bit
        size = 0
        bc = 0
        out = {} if want_fibres else None
        for x in range(625):
            xv = xp[x]
            base = x * 625
            for y in range(625):
                s = xv + yp[y]
                xi = red[s >> 16]
                yi = red[s & 65535]
                g2 = q25[xi] + b5[xi][yi] + qt[yi]
                want = tg[base + y]
                if g2 == want:
                    pat[base + y] |= mask
                    size += 1
                    if want_fibres:
                        out[base + y] = xi * 625 + yi
                if g2 % 25 == want % 25:
                    bc += 1
        sizes.append(size)
        bc_all.append(bc == 390625)
        outs.append(out)
    hist = [0] * (1 << len(branches))
    for v in pat:
        hist[v] += 1
    result = {"sizes": sizes, "uncovered": hist[0], "bc_identical": bc_all,
              "drop": [hist[1 << i] + hist[0] for i in range(len(branches))],
              "multi": {}}
    for v, n in enumerate(hist):
        if n:
            k = bin(v).count("1")
            result["multi"][k] = result["multi"].get(k, 0) + n
    if want_fibres:
        mult = {}
        for i, out in enumerate(outs):
            single = 1 << i
            for z, w in out.items():
                if pat[z] == single:
                    mult[w] = mult.get(w, 0) + 1
        fib = {}
        for n in mult.values():
            fib[n] = fib.get(n, 0) + 1
        result["forced"] = sum(mult.values())
        result["fibres"] = fib
    result["covered"] = bytes(1 if v else 0 for v in pat)
    return result


# ------------------------------------------------ 3. six-cover, C = I4
SIX_CANON = [(canon_branch(psi_six(p)), ZERO8) for p in SIX]
st = cover_stats(I4, SIX_CANON, M, True)
check("C = I4, Canon target M, all 5^8 inputs: the six linear branches cover",
      st["uncovered"] == 0,
      "uncovered %d, agreement sizes %s" % (st["uncovered"], st["sizes"]))
check("C = I4: no five of the six branches cover",
      all(n > 0 for n in st["drop"]), "left uncovered %s" % st["drop"])
check("C = I4: every input agrees with exactly one or with all six branches",
      st["multi"] == {1: 369600, 6: 21025},
      "one branch %d, six branches %d" % (st["multi"].get(1, 0), st["multi"].get(6, 0)))
check("C = I4: outputs forced by inputs with one agreeing branch reach multiplicity 4",
      st["forced"] == 369600 and max(st["fibres"]) == 4,
      "outputs by multiplicity %s" % sorted(st["fibres"].items()))
st0 = cover_stats(I4, [(reduced_branch(psi_six(p)), ZERO8) for p in SIX], M0)
check("C = I4, reduced target M0, branches (x + psi y, y): same cover, b and c preserved",
      st0["uncovered"] == 0 and st0["sizes"] == st["sizes"] and st0["drop"] == st["drop"]
      and all(st0["bc_identical"]))

# ------------------------------------------------ 4. the Canon's K
K_CANON = [[0, 0, 0, 3], [0, 0, 2, 0], [0, 2, 0, 0], [3, 0, 0, 0]]
P_K = [[1, 2, 0, 0], [0, 0, 1, 2], [0, 0, 4, 2], [1, 3, 0, 0]]
P_K_INV = minv(P_K)
check("K = antidiag(3,2,2,3): det K = 1 (a square) and P^T K P = I4 for the stated P",
      det(K_CANON) == 1 and mm(mm(tr(P_K), K_CANON), P_K) == I4)
SIX_K = []
k_skew = True
for pair in SIX:
    psi_k = mm(mm(P_K, psi_six(pair)), P_K_INV)
    k_skew &= is_antisym(mm(K_CANON, psi_k))
    SIX_K.append((canon_branch(psi_k), ZERO8))
stk = cover_stats(K_CANON, SIX_K, M)
check("C = K, Canon target M, all 5^8 inputs: the six transported branches cover, no five do",
      k_skew and stk["uncovered"] == 0 and all(n > 0 for n in stk["drop"])
      and stk["sizes"] == st["sizes"],
      "uncovered %d, drop-one %s" % (stk["uncovered"], stk["drop"]))


# ------------------------------------------------ 5. non-tangent sanity family
def unit8(k):
    return tuple(int(i == k) for i in range(8))


def perturbed(base, i, j):
    a = [list(row) for row in base]
    a[i][j] = (a[i][j] + 1) % P
    return a


NONTAN = []
for _psi in (ZERO4, LI):
    _base = reduced_branch(_psi)
    NONTAN += [(_base, unit8(0)), (_base, unit8(4))]
    NONTAN += [(perturbed(_base, i, j), ZERO8) for i, j in ((0, 1), (0, 5), (4, 0), (4, 5))]
NONTAN.append((perturbed(reduced_branch(ZERO4), 0, 4), unit8(0)))
snt_sizes = []
snt_tangent = []
for _k in range(0, len(NONTAN), 7):
    _s = cover_stats(I4, NONTAN[_k:_k + 7], M0)
    snt_sizes += _s["sizes"]
    snt_tangent += _s["bc_identical"]
check("Lemma 3 sanity (not a proof): 13 non-tangent affine branches, |Z| <= 4*5^6 = 62500",
      not any(snt_tangent) and max(snt_sizes) <= 62500,
      "sizes %s" % snt_sizes)

# ------------------------------------------------ 6. constants of Theorem 1
CLASSES = [(3, 1), (3, 2), (4, 1), (4, 2), (5, 1), (5, 2), (6, 1), (6, 2)]
WITT = {(3, 1): 1, (3, 2): 1, (4, 1): 2, (4, 2): 1,
        (5, 1): 2, (5, 2): 2, (6, 1): 3, (6, 2): 2}


def cdiag(r, delta):
    return tuple([1] * (r - 1) + [delta])


def norm_counts(s, delta):
    cd = cdiag(s, delta)
    h = [0] * 5
    for v in product(range(P), repeat=s):
        h[qd(cd, v)] += 1
    return h


NC = {}
for _s in range(1, 7):
    for _d in (1, 2):
        NC[_s, _d] = norm_counts(_s, _d)
N0 = {cl: NC[cl][0] for cl in CLASSES}
check("isotropic counts N_r(0) by enumeration",
      [N0[cl] for cl in CLASSES] == [25, 25, 145, 105, 625, 625, 3225, 3025]
      and [NC[1, 1][0], NC[2, 1][0], NC[2, 2][0]] == [1, 9, 1],
      " ".join("(%d,%d):%d" % (cl[0], cl[1], N0[cl]) for cl in CLASSES))
check("theta = 1 - N_r(0)/5^r >= 96/125 in every class",
      all(125 * (5 ** cl[0] - N0[cl]) >= 96 * 5 ** cl[0] for cl in CLASSES),
      " ".join("%d/%d" % (5 ** cl[0] - N0[cl], 5 ** cl[0]) for cl in CLASSES))
check("case table (100 + 10k - k^2)/125 < 1 for k = 0..4",
      all(100 + 10 * k - k * k < 125 for k in range(5)),
      " ".join("%d/125" % (100 + 10 * k - k * k) for k in range(5)))
check("thresholds 4(5-k)/(5(6-k)) < 96/125 for k = 1..5",
      all(125 * 4 * (5 - k) < 96 * 5 * (6 - k) for k in range(1, 6)),
      " ".join("%d/%d" % (4 * (5 - k), 5 * (6 - k)) for k in range(1, 6)))

# ------------------------------------------------ 7. tangent type, rank 4
PAIRS4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SH = 20


def tangent_rank4(delta):
    cd = cdiag(4, delta)
    cinv = [pow(c, -1, P) for c in cd]
    cidx = [IDX4[tuple(c * a % P for c, a in zip(cd, v))] for v in VEC4]
    qt = [DOT[cidx[i]][i] for i in range(625)]
    # slice counts by direct enumeration: T[n][c] = #{x : q(x+n) - q(x) = c}
    slice_ok = True
    tcount = []
    for n in range(625):
        h = [0] * 5
        pn = PACK4[n]
        for x in range(625):
            h[(qt[RED[PACK4[x] + pn]] - qt[x]) % 5] += 1
        tcount.append(h)
        slice_ok &= (h == [625, 0, 0, 0, 0]) if n == 0 else (h == [125] * 5)
    tot = [0] * 15625
    par3 = list(product(range(P), repeat=3))
    red = RED
    for y in range(625):
        yv = VEC4[y]
        c = qt[y]
        w = []
        for a, b in PAIRS4:
            u = [0, 0, 0, 0]
            u[a] = cinv[a] * yv[b] % P
            u[b] = (-cinv[b] * yv[a]) % P
            w.append(u)
        pk1 = [PACK4[IDX4[tuple((p0 * w[0][k] + p1 * w[1][k] + p2 * w[2][k]) % P
                                for k in range(4))]] for p0, p1, p2 in par3]
        pk2 = [PACK4[IDX4[tuple((p0 * w[3][k] + p1 * w[4][k] + p2 * w[5][k]) % P
                                for k in range(4))]] for p0, p1, p2 in par3]
        brow = DOT[cidx[y]]
        val = []
        for n in range(625):
            v = tcount[n][c] if brow[n] == 0 else 0      # needs B(psi y, y) = 0
            if n == 0:
                v += 1 << SH                               # y in ker psi
                if c == 0:
                    v += 1 << (2 * SH)                     # isotropic y in ker psi
                else:
                    v += 1 << (4 * SH)                     # non-isotropic y in ker psi
            if c != 0 and qt[n] == 0:
                v += 1 << (3 * SH)                         # q(psi y) = 0, q(y) != 0
            if brow[n] != 0:
                v += 1 << (5 * SH)                         # would violate skewness
            val.append(v)
        for i in range(125):
            a = pk1[i]
            lo = i * 125
            tot[lo:lo + 125] = [t + val[red[a + b]] for t, b in zip(tot[lo:lo + 125], pk2)]
    mask = (1 << SH) - 1
    sizes = {}
    formula_ok = True
    skew_ok = True
    best_a0 = 0
    for t in tot:
        size = t & mask
        ker = (t >> SH) & mask
        keriso = (t >> (2 * SH)) & mask
        a0 = (t >> (3 * SH)) & mask
        kernon = (t >> (4 * SH)) & mask
        skew_ok &= (t >> (5 * SH)) == 0
        formula_ok &= size == 125 * (625 - ker) + 625 * keriso
        sizes[size] = sizes.get(size, 0) + 1
        if kernon == 0:
            best_a0 = max(best_a0, a0)
    return slice_ok, skew_ok, formula_ok, sizes, best_a0


T4 = {}
for _d in (1, 2):
    T4[_d] = tangent_rank4(_d)
    _so, _sk, _fo, _sz, _ba = T4[_d]
    check("rank 4, delta = %d: slice counts #{x: q(x+n) = q(x) + c} are 125 (n != 0), "
          "625 [c = 0] (n = 0)" % _d, _so and _sk)
    check("rank 4, delta = %d: |Z_psi| = 125 (625 - |ker|) + 625 #iso(ker), all 15625 skew "
          "psi; maximum 5^7 + 4*5^(3+w)" % _d,
          _fo and max(_sz) == 5 ** 7 + 4 * 5 ** (3 + WITT[4, _d]),
          "sizes %s" % sorted(_sz.items()))


# ------------------------------------------------ 8. rank 3; explicit maxima
def slice_hist(cd, n):
    h = [0] * 5
    for x in product(range(P), repeat=len(cd)):
        h[sum(c * ((a + b) * (a + b) - a * a) for c, a, b in zip(cd, x, n)) % P] += 1
    return h


def tangent_size(cd, psi):
    """|Z_psi| by slices: for each y the x with q(x + psi y) = q(x) + q(y)."""
    if not is_antisym(mm(diag(cd), psi)):
        return None
    cache = {}
    total = 0
    for y in product(range(P), repeat=len(cd)):
        n = mv(psi, y)
        if bd(cd, n, y):
            return None
        if n not in cache:
            cache[n] = slice_hist(cd, n)
        total += cache[n][qd(cd, y)]
    return total


def rank3_data(delta):
    cd = cdiag(3, delta)
    cinv = [pow(c, -1, P) for c in cd]
    best = 0
    best_a0 = 0
    vecs = list(product(range(P), repeat=3))
    for p01, p02, p12 in product(range(P), repeat=3):
        k = [[0, p01, p02], [-p01 % P, 0, p12], [-p02 % P, -p12 % P, 0]]
        psi = [[cinv[i] * k[i][j] % P for j in range(3)] for i in range(3)]
        best = max(best, tangent_size(cd, psi))
        if all(qd(cd, y) == 0 or any(mv(psi, y)) for y in vecs):
            best_a0 = max(best_a0, sum(1 for y in vecs
                                       if qd(cd, y) and qd(cd, mv(psi, y)) == 0))
    return best, best_a0


R3 = {d: rank3_data(d) for d in (1, 2)}
check("rank 3: maximal |Z_psi| over all 125 skew psi is 5^5 + 4*5^3 = 3625, both delta",
      R3[1][0] == 3625 and R3[2][0] == 3625, "%d %d" % (R3[1][0], R3[2][0]))


def wedge(cd, u, v):
    """psi y = B(v,y) u - B(u,y) v."""
    n = len(cd)
    return [[(u[i] * cd[j] * v[j] - v[i] * cd[j] * u[j]) % P for j in range(n)]
            for i in range(n)]


UNIT = {n: [tuple(int(i == j) for j in range(n)) for i in range(n)] for n in (5, 6)}
MAXIMA = {}
for _d in (1, 2):
    MAXIMA[5, _d] = tangent_size(cdiag(5, _d),
                                 wedge(cdiag(5, _d), (1, 2, 0, 0, 0), UNIT[5][4]))
MAXIMA[6, 1] = tangent_size(cdiag(6, 1), zeros(6))
MAXIMA[6, 2] = tangent_size(cdiag(6, 2), wedge(cdiag(6, 2), UNIT[6][4], UNIT[6][5]))
check("explicit tangent branches attain 5^(2r-1) + 4*5^(r+w-1) for ranks 5 and 6",
      all(MAXIMA[cl] == 5 ** (2 * cl[0] - 1) + 4 * 5 ** (cl[0] + WITT[cl] - 1) for cl in MAXIMA),
      " ".join("(%d,%d):%d" % (cl[0], cl[1], MAXIMA[cl]) for cl in sorted(MAXIMA)))
check("5^(2r-1) + 4*5^(r+w-1) exceeds the non-tangent bound 4*5^(2r-2) in every class",
      all(5 ** (2 * cl[0] - 1) + 4 * 5 ** (cl[0] + WITT[cl] - 1) > 4 * 5 ** (2 * cl[0] - 2)
          for cl in CLASSES))

# ------------------------------------------------ 9. pencil covers, rank 5 and 6
VEC3 = list(product(range(P), repeat=3))
IDX3 = {v: i for i, v in enumerate(VEC3)}
HM3 = []
for _m in VEC3:
    _masks = [0] * 5
    for _i, _x in enumerate(VEC3):
        _masks[(_m[0] * _x[0] + _m[1] * _x[1] + _m[2] * _x[2]) % P] |= 1 << _i
    HM3.append(_masks)


def level_mask(m, t, cache):
    """Bitmask over x in F5^r (index = first coordinate most significant) of m.x = t."""
    key = (m, t)
    got = cache.get(key)
    if got is None:
        r = len(m)
        hi = m[:r - 3]
        rows = HM3[IDX3[m[r - 3:]]]
        got = 0
        for hidx, h in enumerate(product(range(P), repeat=r - 3)):
            got |= rows[(t - sum(a * b for a, b in zip(hi, h))) % P] << (125 * hidx)
        cache[key] = got
    return got


def tangent_cover(cd, maps):
    """Exhaustive over all (x,y): union of the agreement sets of the tangent branches.

    Returns (number of uncovered inputs, number of individually redundant branches).
    """
    r = len(cd)
    full = (1 << 5 ** r) - 1
    cache = {}
    nb = len(maps)
    uncovered = 0
    needed = [False] * nb
    for y in product(range(P), repeat=r):
        qy = qd(cd, y)
        masks = []
        for psi in maps:
            n = mv(psi, y)
            if any(n):
                cn = tuple(c * a % P for c, a in zip(cd, n))
                masks.append(level_mask(cn, 3 * (qy - qd(cd, n)) % P, cache))
            else:
                masks.append(full if qy == 0 else 0)
        pre = [0] * (nb + 1)
        for i in range(nb):
            pre[i + 1] = pre[i] | masks[i]
        if pre[nb] != full:
            uncovered += bin(full & ~pre[nb]).count("1")
        suf = 0
        for i in range(nb - 1, -1, -1):
            if not needed[i] and (pre[i] | suf) != full:
                needed[i] = True
            suf |= masks[i]
    return uncovered, nb - sum(needed)


def vadd(u, v, s=1):
    return tuple((a + s * b) % P for a, b in zip(u, v))


def vsc(s, u):
    return tuple(s * a % P for a in u)


def lift(cd, basis, sigma, x4):
    """r x r matrix of y -> sum_k (X c(y))_k v_k, c_l(y) = B(v_l, y)/sigma."""
    r = len(cd)
    si = pow(sigma, -1, P)
    coord = [[si * cd[j] * basis[l][j] % P for j in range(r)] for l in range(4)]
    xc = mm(x4, coord)
    return [[sum(basis[k][i] * xc[k][j] for k in range(4)) % P for j in range(r)]
            for i in range(r)]


def pencil_setup(r, delta):
    cd = cdiag(r, delta)
    e = [tuple(int(i == j) for j in range(r)) for i in range(r)]
    if r == 5:
        if delta == 1:
            lines, sigma = e, 1
        else:
            lines = [vadd(e[0], e[1]), vadd(e[0], e[1], 4), vadd(e[2], e[3]),
                     vadd(e[2], e[3], 4), e[4]]
            sigma = 2
        served = [(1, 2, 3, 4), (3,), (1, 3), (3,)]
        groups = [([lines[k] for k in range(5) if k != j], sigma, kap)
                  for j, kap in enumerate(served)]
    else:
        if delta == 1:
            w4 = [[e[2], e[3], e[4], e[5]], [e[0], e[1], e[4], e[5]],
                  [e[0], e[1], e[2], e[3]]]
        else:
            pl = [(e[0], vadd(e[1], e[2])), (e[3], vadd(e[1], e[2], 4)), (e[4], e[5])]
            w4 = []
            for j in range(3):
                (p1, n1), (p2, n2) = [pl[k] for k in range(3) if k != j]
                w4.append([p1, p2, vadd(vsc(2, n1), vsc(2, n2)),
                           vadd(vsc(2, n1), vsc(2, n2), 4)])
        served = [(1, 2, 3, 4), (1, 2, 3, 4), (3,)]
        groups = [(w4[j], 1, served[j]) for j in range(3)]
    return cd, groups


def pencil_cover(r, delta):
    cd, groups = pencil_setup(r, delta)
    cm = diag(cd)
    ok = True
    maps = [zeros(r)]
    for basis, sigma, kap in groups:
        ok &= all(bd(cd, basis[k], basis[l]) == (sigma if k == l else 0)
                  for k in range(4) for l in range(4))
        dp = lift(cd, basis, sigma, DP)
        dm = lift(cd, basis, sigma, DM)
        pr = lift(cd, basis, sigma, I4)
        c4 = mm(mm(tr(pr), cm), pr)
        ok &= is_antisym(mm(cm, dp)) and is_antisym(mm(cm, dm))
        ok &= mm(mm(tr(dp), cm), dp) == zeros(r) and mm(mm(tr(dm), cm), dm) == zeros(r)
        ok &= madd(mm(mm(tr(dp), cm), dm), mm(mm(tr(dm), cm), dp)) == mscale(4, c4)
        pts = [(1, t) for t in range(P)] + [(0, k) for k in kap]
        maps += [madd(mscale(a, dp), mscale(b, dm)) for a, b in pts]
    uncovered, redundant = tangent_cover(cd, maps)
    sample = direct_slices(cd, maps, 127 if r == 5 else 1303)
    return ok, len(maps), uncovered, redundant, sample


def direct_slices(cd, maps, step):
    """Direct evaluation of all three Gram conditions on whole slices over sampled y."""
    r = len(cd)
    slices = 0
    for idx in range(0, 5 ** r, step):
        y = tuple((idx // 5 ** (r - 1 - k)) % 5 for k in range(r))
        qy = qd(cd, y)
        images = [mv(psi, y) for psi in maps]
        for x in product(range(P), repeat=r):
            qx = qd(cd, x)
            bxy = bd(cd, x, y)
            for n in images:
                x2 = tuple((a + b) % P for a, b in zip(x, n))
                if qd(cd, x2) == (qx + qy) % P and bd(cd, x2, y) == bxy:
                    break
            else:
                return None
        slices += 1
    return slices


check("pencil points (1,t), t in F5, and (0,kappa): six directions, ab + kappa = kappa a + b",
      all(len({proj_point(p) for p in [(1, t) for t in range(P)] + [(0, k)]}) == 6
          and all((-a * b - k + k * a + b) % P == 0
                  for a, b in [(1, t) for t in range(P)] + [(0, k)])
          for k in range(1, P)))
PC = {}
for _r in (5, 6):
    for _d in (1, 2):
        PC[_r, _d] = pencil_cover(_r, _d)
        _ok, _nb, _unc, _redu, _smp = PC[_r, _d]
        check("rank %d, delta = %d: %d tangent branches cover all 5^%d inputs"
              % (_r, _d, _nb, 2 * _r),
              _ok and _unc == 0 and _smp is not None and _nb == (29 if _r == 5 else 25),
              "uncovered %d, redundant branches %d, %s slices re-evaluated directly"
              % (_unc, _redu, _smp))

# ------------------------------------------------ 10. rank 4, delta = 2
COVER42 = ("020300 122421 333344 100340 202411 011334 211432 422003 024103 330111 "
           "301124 041410 441211 131021 110302 133400 003441 021423 423402 232043 "
           "304322 310343 444240 204204 320133").split()


def cover_rank4_delta2():
    cd = cdiag(4, 2)
    cm = diag(cd)
    cinv = [pow(c, -1, P) for c in cd]
    maps = []
    skew = True
    for word in COVER42:
        k = zeros(4)
        for (a, b), ch in zip(PAIRS4, word):
            k[a][b] = int(ch)
            k[b][a] = -int(ch) % P
        psi = [[cinv[i] * k[i][j] % P for j in range(4)] for i in range(4)]
        skew &= is_antisym(mm(cm, psi))
        maps.append(psi)
    uncovered, redundant = tangent_cover(cd, maps)
    # independent direct evaluation of G(f(z)) = M0 G(z) at every z of F5^8
    acc = bytearray(390625)
    for lo in range(0, len(maps), 7):
        part = cover_stats(cm, [(reduced_branch(psi), ZERO8) for psi in maps[lo:lo + 7]], M0)
        acc = bytearray(a | b for a, b in zip(acc, part["covered"]))
    return skew and len(set(COVER42)) == 25, uncovered, redundant, acc.count(0)


C42 = cover_rank4_delta2()
check("rank 4, delta = 2: the 25 listed tangent branches cover all 5^8 inputs",
      C42[0] and C42[1] == 0 and C42[3] == 0,
      "uncovered %d (level sets), %d (direct evaluation), redundant branches %d"
      % (C42[1], C42[3], C42[2]))
SIXRED = tangent_cover(cdiag(4, 1), [psi_six(p) for p in SIX])
check("cross-check of the cover routine on the six branches of rank 4, delta = 1",
      SIXRED == (0, 0))


# ------------------------------------------------ 11. six tangent branches
def plane_lemma():
    pts = [(a, b) for a in range(P) for b in range(P)]
    dirs = [(1, s) for s in range(P)] + [(0, 1)]
    qualifying = 0
    for qa, qb, qc in product(range(P), repeat=3):
        qv = {n: (qa * n[0] * n[0] + qb * n[0] * n[1] + qc * n[1] * n[1]) % P for n in pts}
        disc = (qb * qb - 4 * qa * qc) % P
        iso_dirs = [d for d in dirs if qv[d] == 0]
        for la, lb in product(range(P), repeat=2):
            for c in range(1, P):
                zs = {n for n in pts if (qv[n] + la * n[0] + lb * n[1] - c) % P == 0}
                if all(any((s * d[0] % P, s * d[1] % P) in zs for s in range(1, P))
                       for d in dirs):
                    qualifying += 1
                    if disc not in (1, 4) or len(iso_dirs) != 2:
                        return None
                    for d in iso_dirs:
                        if sum((s * d[0] % P, s * d[1] % P) in zs
                               for s in range(1, P)) != 1:
                            return None
                    if sum(1 for n in zs if qv[n] == 0) != 2:
                        return None
    return qualifying


def line_covers():
    pts = [(a, b) for a in range(P) for b in range(P)]
    dirs = [(1, s) for s in range(P)] + [(0, 1)]
    lines = []
    for di, d in enumerate(dirs):
        seen = set()
        for p in pts:
            m = 0
            for s in range(P):
                m |= 1 << (((p[0] + s * d[0]) % P) * 5 + (p[1] + s * d[1]) % P)
            if m not in seen:
                seen.add(m)
                lines.append((di, m))
    full = (1 << 25) - 1
    with_class = 0
    pencils = 0
    bad = 0
    for k in range(1, 7):
        for comb in combinations(lines, k):
            acc = 0
            for _, m in comb:
                acc |= m
            if acc != full:
                continue
            ds = [d for d, _ in comb]
            if any(ds.count(d) == 5 for d in range(6)):
                with_class += 1
                continue
            common = full
            for _, m in comb:
                common &= m
            if k == 6 and len(set(ds)) == 6 and bin(common).count("1") == 1:
                pencils += 1
            else:
                bad += 1
    return len(lines), with_class, pencils, bad


PL = plane_lemma()
check("plane lemma, all 12500 conics Q + L - c of F5^2 with c != 0",
      PL is not None, "%s meet all six directions; each has exactly two isotropic zeros" % PL)
LC = line_covers()
check("covers of F5^2 by at most six lines: a complete parallel class or six concurrent lines",
      LC[0] == 30 and LC[3] == 0, "%d with a parallel class, %d pencils" % (LC[1], LC[2]))
A0 = {(4, 1): T4[1][4], (4, 2): T4[2][4], (3, 1): R3[1][1], (3, 2): R3[2][1]}
check("rank 4, delta = 2: at most 105 non-isotropic y with q(psi y) = 0; 6*105 < 2*520",
      A0[4, 2] <= 105 and 6 * 105 < 2 * (625 - N0[4, 2]),
      "maximum found %d (for delta = 1: %d)" % (A0[4, 2], A0[4, 1]))
check("rank 3: at most 25 non-isotropic y with q(psi y) = 0; 6*25 < 2*100",
      max(A0[3, 1], A0[3, 2]) <= 25 and 6 * 25 < 2 * (125 - N0[3, 1]),
      "maxima found %d %d" % (A0[3, 1], A0[3, 2]))
check("rank 5 and (6,2): 6*25*N_3(0) < 2*2500 and 6*max(N_6(0), 625*N_2(0)) < 2*12600",
      NC[3, 1][0] == NC[3, 2][0] == 25 and 6 * 25 * 25 < 2 * (3125 - N0[5, 1])
      and 6 * max(N0[6, 2], 625 * NC[2, 2][0]) < 2 * (15625 - N0[6, 2]),
      "3750 < %d, %d < %d" % (2 * (3125 - N0[5, 1]), 6 * max(N0[6, 2], 625),
                              2 * (15625 - N0[6, 2])))

# ------------------------------------------------ 12. fibres of size two (Theorem 3)
def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return ((a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3) % P,
            (a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2) % P,
            (a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1) % P,
            (a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0) % P)


def qinv(u):
    n = pow(sum(t * t for t in u) % P, -1, P)
    return (u[0] * n % P, -u[1] * n % P, -u[2] * n % P, -u[3] * n % P)


def conj_matrix(u):
    """4 x 4 matrix of x -> u x u^-1 in the basis 1, i, j, k."""
    ui = qinv(u)
    cols = [qmul(qmul(u, e), ui) for e in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


U_FIB = [(1, 0, 0, 0), (0, 1, 2, 1), (0, 1, 3, 1), (0, 1, 4, 2), (1, 0, 0, 4), (1, 2, 0, 1)]
K_FIB = [conj_matrix(u) for u in U_FIB]
RHO = [[row[1:] for row in k[1:]] for k in K_FIB]
K_FIB_LISTED = [
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    [[1, 0, 0, 0], [0, 1, 4, 2], [0, 4, 2, 4], [0, 2, 4, 1]],
    [[1, 0, 0, 0], [0, 1, 1, 2], [0, 1, 2, 1], [0, 2, 1, 1]],
    [[1, 0, 0, 0], [0, 1, 3, 4], [0, 3, 1, 1], [0, 4, 1, 2]],
    [[1, 0, 0, 0], [0, 0, 1, 0], [0, 4, 0, 0], [0, 0, 0, 1]],
    [[1, 0, 0, 0], [0, 4, 3, 4], [0, 2, 1, 1], [0, 4, 4, 3]],
]
check("Theorem 3: k_i = conjugation by u_i are the listed isometries; left multiplication by "
      "i, j on quaternions is Li, Lj",
      K_FIB == K_FIB_LISTED and all(mm(tr(k), k) == I4 for k in K_FIB)
      and all(mv(LI, v) == qmul((0, 1, 0, 0), v) and mv(LJ, v) == qmul((0, 0, 1, 0), v)
              for v in VEC4))

# the model on F5^3: theta -> rho_i(theta + a_i) on the plane theta.a_i = (1 - N_i)/2
A_FIB = [(a, b, 0) for a, b in SIX]
N_FIB = [(a * a + b * b) % P for a, b in SIX]
FREE_LINE = [(2, 0, z) for z in range(P)]


def dot3(u, v):
    return sum(a * b for a, b in zip(u, v)) % P


def tau_model():
    cnt = {}
    planes_ok = True
    for t in VEC3:
        on = [i for i in range(6) if dot3(t, A_FIB[i]) == (1 - N_FIB[i]) * 3 % P]
        planes_ok &= on == list(range(6)) if t in FREE_LINE else len(on) == 1
        i = on[0]                                   # the unique branch, or branch 1 on the free line
        img = mv(RHO[i], tuple((x + y) % P for x, y in zip(t, A_FIB[i])))
        planes_ok &= dot3(img, img) == (dot3(t, t) + 1) % P
        cnt[img] = cnt.get(img, 0) + 1
    hist = [sum(1 for t in VEC3 if cnt.get(t, 0) == m) for m in range(4)]
    return planes_ok, hist


def sigma_model():
    lines = sorted({proj_point(w) for w in VEC3 if any(w) and dot3(w, w) == 0})
    classes = [(e, m) for e in lines for m in VEC3 if dot3(m, e) == 0]
    cnt = {}
    ok = len(lines) == 6 and len(classes) == 150
    for e, m in classes:
        on = [i for i in range(6) if dot3(A_FIB[i], m) == 0]
        ok &= len(on) == (6 if m[0] == 0 and m[1] == 0 else 1)
        i = on[0]
        img = (proj_point(mv(RHO[i], e)), mv(RHO[i], m))
        ok &= dot3(img[0], img[1]) == 0
        cnt[img] = cnt.get(img, 0) + 1
    hist = [sum(1 for cl in classes if cnt.get(cl, 0) == m) for m in range(4)]
    return ok, hist


TAU = tau_model()
check("Theorem 3, model on F5^3 (non-isotropic slices): the piecewise map tau has fibres <= 2",
      TAU[0] and TAU[1][3] == 0, "points with 0, 1, 2 preimages: %d, %d, %d" % tuple(TAU[1][:3]))
SIG = sigma_model()
check("Theorem 3, model on the 150 classes (isotropic slices): the map sigma has fibres <= 2",
      SIG[0] and SIG[1][3] == 0, "classes with 0, 1, 2 preimages: %d, %d, %d" % tuple(SIG[1][:3]))


def selector_fibres(cmat, branches, target):
    """Selector: the unique agreeing branch, or the first branch if all six agree.
    Direct evaluation at every z of F5^8.  Returns (agreement ok, multiplicities by output,
    Gram class by data point, image of the Gram class map)."""
    cidx = [IDX4[mv(cmat, v)] for v in VEC4]
    qt = [DOT[cidx[i]][i] for i in range(625)]
    q25 = [25 * t for t in qt]
    b5 = [DOT5[cidx[i]] for i in range(625)]
    mt = [0] * 125
    for g in range(125):
        t = mv(target, (g // 25, (g // 5) % 5, g % 5))
        mt[g] = t[0] * 25 + t[1] * 5 + t[2]
    gram = bytearray(390625)
    for x in range(625):
        row = b5[x]
        base = x * 625
        qx = q25[x]
        for y in range(625):
            gram[base + y] = qx + row[y] + qt[y]
    pat = bytearray(390625)
    outs = []
    red = RED
    for bit, a in enumerate(branches):
        ax = [row[:4] for row in a]
        ay = [row[4:] for row in a]
        xp = []
        yp = []
        for v in VEC4:
            u = mv(ax, v)
            xp.append((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]])
            u = mv(ay, v)
            yp.append((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]])
        mask = 1 << bit
        out = {}
        for x in range(625):
            xv = xp[x]
            base = x * 625
            for y in range(625):
                s = xv + yp[y]
                xi = red[s >> 16]
                yi = red[s & 65535]
                if q25[xi] + b5[xi][yi] + qt[yi] == mt[gram[base + y]]:
                    pat[base + y] |= mask
                    out[base + y] = xi * 625 + yi
        outs.append(out)
    which = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4, 32: 5, 63: 0}
    mult = bytearray(390625)
    ok = True
    for z in range(390625):
        i = which.get(pat[z])
        if i is None:
            ok = False
            break
        mult[outs[i][z]] += 1
    return ok, mult, gram, mt


def continuation_flow(mult, gram, mt):
    """p(M g) = p(g) + F2(g) - F0(M g) along the orbits of the Gram classes; 0 <= p <= F0 + F1."""
    f = [[0] * 125 for _ in range(3)]
    for o in range(390625):
        f[mult[o]][gram[o]] += 1
    seen = set()
    total = 0
    feasible = True
    lengths = {}
    for g0 in range(125):
        if g0 in seen:
            continue
        orb = [g0]
        seen.add(g0)
        h = mt[g0]
        while h != g0:
            orb.append(h)
            seen.add(h)
            h = mt[h]
        lengths[len(orb)] = lengths.get(len(orb), 0) + 1
        dd = [0]
        for j in range(len(orb) - 1):
            dd.append(dd[-1] + f[2][orb[j]] - f[0][orb[j + 1]])
        feasible &= dd[-1] + f[2][orb[-1]] - f[0][orb[0]] == dd[0]
        lo = max(0, max(-x for x in dd))
        hi = min(f[0][o] + f[1][o] - x for o, x in zip(orb, dd))
        feasible &= lo <= hi
        total += sum(lo + x for x in dd)
    return feasible, total, sum(f[2]), sorted(lengths.items())


FIB_BRANCHES = [mm(block(k, ZERO4, ZERO4, k), canon_branch(psi_six(p))) for p, k in zip(SIX, K_FIB)]
FOK, FMULT, FGRAM, FMT = selector_fibres(I4, FIB_BRANCHES, M)
FH = [sum(1 for v in FMULT if v == m) for m in range(4)]
check("Theorem 3: C = I4, Canon target M, all 5^8 inputs: the selector satisfies the Gram identity "
      "and every output has at most two preimages",
      FOK and FH[3] == 0 and max(FMULT) == 2 and FH[1] + 2 * FH[2] == 390625
      and FH[2] == 2400 * TAU[1][2] + 600 * SIG[1][2],
      "outputs with 0, 1, 2 preimages: %d, %d, %d" % tuple(FH[:3]))
PPK = block(P_K, ZERO4, ZERO4, P_K)
PPKI = block(P_K_INV, ZERO4, ZERO4, P_K_INV)
KOK, KMULT, KGRAM, KMT = selector_fibres(K_CANON, [mm(mm(PPK, a), PPKI) for a in FIB_BRANCHES], M)
KH = [sum(1 for v in KMULT if v == m) for m in range(4)]
check("Theorem 3: C = K, Canon target M, all 5^8 inputs: the transported selector has fibres <= 2",
      KOK and KH == FH, "outputs with 0, 1, 2 preimages: %d, %d, %d" % tuple(KH[:3]))
FLOW = continuation_flow(FMULT, FGRAM, FMT)
check("Proposition 6: the flow p(Mg) = p(g) + F2(g) - F0(Mg), 0 <= p <= F0 + F1, has a solution "
      "on every orbit of Gram classes",
      FLOW[0], "orbit lengths %s, fibre-2 outputs %d, pass-through states %d, reachable set %d"
      % (FLOW[3], FLOW[2], FLOW[1], 390625 + FLOW[2] + FLOW[1]))

# ------------------------------------------------ 13. a complete permutation (Proposition 7)
# occupied layer, reduced coordinates: theta -> shear a (words "theta:a"), class (e,m) -> conjugation
OCC_SHEAR_WORDS = (
    "001:103 002:433 003:201 004:324 011:433 012:304 013:111 014:130 021:421 "
    "022:111 023:311 024:402 030:324 031:111 032:304 033:201 034:433 041:311 "
    "042:421 043:301 044:402 101:201 104:103 110:301 111:201 112:111 114:324 "
    "122:031 134:311 140:130 141:130 144:130 200:402 202:421 203:031 213:002 "
    "214:201 220:130 222:031 223:421 230:402 232:103 233:433 234:111 301:304 "
    "302:130 303:433 310:311 320:103 321:304 322:031 323:402 330:433 332:421 "
    "333:402 340:421 343:002 400:433 401:402 403:031 410:031 411:301 414:304 "
    "420:421 430:311 431:301 434:031 440:201 441:301 443:002 "
).split()
OCC_CONJ_U = [(1, 1, 1, 0), (1, 1, 1, 4)]
OCC_CONJ_WORDS = (
    "012012:0 012024:0 012031:0 012043:0 013013:0 013021:0 013034:0 013042:0 013121:1 "
    "013134:1 013142:0 013213:1 013234:0 013242:1 013313:1 013321:0 013342:1 013413:0 "
    "013421:1 013434:1 102132:0 102142:0 102214:0 102234:0 102321:0 102341:0 102413:0 "
    "102423:0 120121:1 120242:1 120313:1 120434:1 130130:0 130132:0 130134:1 130210:0 "
    "130213:1 130214:0 130340:0 130341:0 130342:1 130420:0 130421:1 130423:0 "
).split()
OCC_SHEAR = {tuple(int(ch) for ch in w[:3]): tuple(int(ch) for ch in w[4:]) for w in OCC_SHEAR_WORDS}
OCC_CONJ = {(tuple(int(ch) for ch in w[:3]), tuple(int(ch) for ch in w[3:6])): int(w[7])
            for w in OCC_CONJ_WORDS}


def complete_permutation():
    """Reduced step (C = I4, target M0): (z,0) -> (Phi(z), bit); (o,1) -> shear or conjugation.
    The permutation for the Canon target M applies the two substitutions of Lemma 1(b) at
    every step; all checks are made for it.  Returns statistics, or None on any failure."""
    n = 390625
    red_br = [mm(block(k, ZERO4, ZERO4, k), reduced_branch(psi_six(p))) for p, k in zip(SIX, K_FIB)]
    # ready layer by direct evaluation
    qt = [DOT[i][i] for i in range(625)]
    gram = bytearray(n)
    for x in range(625):
        row = DOT5[x]
        base = x * 625
        qx = 25 * qt[x]
        for y in range(625):
            gram[base + y] = qx + row[y] + qt[y]
    m0 = [((g // 25 + g % 5) % 5) * 25 + (g // 5 % 5) * 5 + g % 5 for g in range(125)]
    phi = [-1] * n
    br = bytearray(n)
    agree_cnt = bytearray(n)
    red = RED
    for bi in range(5, -1, -1):                      # descending, so the smallest agreeing index wins
        a = red_br[bi]
        ax = [row[:4] for row in a]
        ay = [row[4:] for row in a]
        xp = []
        yp = []
        for v in VEC4:
            u = mv(ax, v)
            xp.append((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]])
            u = mv(ay, v)
            yp.append((PACK4[IDX4[u[:4]]] << 16) | PACK4[IDX4[u[4:]]])
        for x in range(625):
            xv = xp[x]
            base = x * 625
            for y in range(625):
                s = xv + yp[y]
                xi = red[s >> 16]
                yi = red[s & 65535]
                o = xi * 625 + yi
                if gram[o] == m0[gram[base + y]]:
                    phi[base + y] = o
                    br[base + y] = bi
                    agree_cnt[base + y] += 1
    if min(phi) < 0 or any(c not in (1, 6) for c in set(agree_cnt)):
        return None
    mult = bytearray(n)
    minbr = bytearray([9]) * n
    for z in range(n):
        o = phi[z]
        mult[o] += 1
        if br[z] < minbr[o]:
            minbr[o] = br[z]
    if max(mult) > 2:
        return None
    T = {}
    for z in range(n):
        o = phi[z]
        T[z] = o + n * (1 if br[z] > minbr[o] else 0)
    # occupied layer
    conj = [conj_matrix(u) for u in OCC_CONJ_U]
    conj_idx = [[IDX4[mv(k, v)] for v in VEC4] for k in conj]
    inv = [0, 1, 3, 2, 4]
    iso_lines = sorted({proj_point(w) for w in VEC3 if any(w) and dot3(w, w) == 0})
    arrivals = {}
    for y in range(1, 625):
        yv = VEC4[y]
        ybar = (yv[0], -yv[1] % P, -yv[2] % P, -yv[3] % P)
        qy = qt[y]
        if qy:
            sh = {th: IDX4[qmul((0,) + a, yv)] for th, a in OCC_SHEAR.items()}
            qi = inv[qy]
            for x in range(625):
                w = qmul(VEC4[x], ybar)
                th = (w[1] * qi % P, w[2] * qi % P, w[3] * qi % P)
                ay_idx = sh.get(th)
                if ay_idx is not None:
                    x2 = red[PACK4[x] + PACK4[ay_idx]]
                    arrivals.setdefault(x2 * 625 + y, []).append((OCC_SHEAR[th], x * 625 + y))
        else:
            e = next(l for l in iso_lines if not any(qmul((0,) + l, yv)))
            for x in range(625):
                w = qmul(VEC4[x], ybar)
                r = OCC_CONJ.get((e, w[1:]))
                if r is not None:
                    o2 = conj_idx[r][x] * 625 + conj_idx[r][y]
                    arrivals.setdefault(o2, []).append(((9, 9, 9), x * 625 + y))
    for o2, lst in arrivals.items():
        lst.sort()
        for rank, (a, o) in enumerate(lst):
            # the first arrival takes the ready slot if the target has no preimage under Phi
            T[n + o] = o2 + n * (0 if (rank == 0 and mult[o2] == 0) else 1)
    if set(T.values()) != set(T):
        return None                               # T does not permute the ready layer and the table states
    # Canon coordinates: T_M(z,b) = (S_out^-1 x 1) T (S_in^-1 x 1), S^-1 as in Lemma 1(b):
    # S_in^-1 (x,y) = (2x + 3y, 4x + 2y),  S_out^-1 (x,y) = (2x + 3y, x); Canon target M
    sc = [[IDX4[tuple(s * t % P for t in v)] for v in VEC4] for s in range(P)]

    def lin(c11, c12, c21, c22):
        table = [0] * n
        for x in range(625):
            p1 = PACK4[sc[c11][x]]
            p2 = PACK4[sc[c21][x]]
            base = x * 625
            for y in range(625):
                table[base + y] = red[p1 + PACK4[sc[c12][y]]] * 625 + red[p2 + PACK4[sc[c22][y]]]
        return table

    s_in_inv = lin(2, 3, 4, 2)
    s_out_inv = lin(2, 3, 1, 0)
    mt = [0] * 125
    for g in range(125):
        t = mv(M, (g // 25, (g // 5) % 5, g % 5))
        mt[g] = t[0] * 25 + t[1] * 5 + t[2]
    TM = {}
    for s in range(2 * n):
        t = T.get(s_in_inv[s % n] + n * (s // n))
        if t is not None:
            TM[s] = s_out_inv[t % n] + n * (t // n)
    # exact checks on the reachable set, Canon target M
    reach = bytearray(2 * n)
    frontier = list(range(n))
    for s in frontier:
        reach[s] = 1
    occupied = 0
    while frontier:
        nxt = []
        for s in frontier:
            t = TM.get(s)
            if t is None:
                return None                       # a reachable state without a map
            if gram[t % n] != mt[gram[s % n]]:
                return None                       # Gram identity fails
            if not reach[t]:
                reach[t] = 1
                nxt.append(t)
                occupied += t >= n
        frontier = nxt
    size = sum(reach)
    if occupied != 2400 * len(OCC_SHEAR) + 600 * len(OCC_CONJ):
        return None                               # the occupied reachable states are not those of the tables
    images = set()
    for s in range(2 * n):
        if reach[s]:
            images.add(TM[s])
    if len(images) != size:
        return None                               # not injective on the reachable set
    # cycles
    seen = bytearray(2 * n)
    ncyc = 0
    longest = 0
    for s in range(2 * n):
        if reach[s] and not seen[s]:
            length = 0
            t = s
            while not seen[t]:
                seen[t] = 1
                t = TM[t]
                length += 1
            ncyc += 1
            longest = max(longest, length)
    return size, occupied, ncyc, longest, len(set(OCC_SHEAR.values())), len(OCC_CONJ_U)


CT = complete_permutation()
check("Proposition 7: Canon target M, all 781250 states: T built from the six branches (bit 0) "
      "and from shears and conjugations (bit 1) permutes its reachable set, Gram identity on it",
      CT is not None,
      "reachable %s, occupied %s, cycles %s, longest %s, shears %s, conjugations %s"
      % (CT if CT else ("-",) * 6))

print("%s (%d checks)" % ("ALL CHECKS PASS" if not FAILED else "CHECKS FAILED", COUNT[0]))
sys.exit(1 if FAILED else 0)
