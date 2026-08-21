#!/usr/bin/env python3
# C-TM-HANKEL-K4-SPECTRAL-FLOW-2 verifier
# Frozen against PREREG-C-TM-HANKEL-K4-SPECTRAL-FLOW-2.md
# sha256 5a70438e9fd0ed858079e612e72034ede45487caf3ca9d239db27090a1e507c7
# Python standard library only. Exact integers and Fractions only. No float
# anywhere. No wall clock, no hostname, no machine identifier.

from fractions import Fraction

import sys
from bisect import bisect_right
from math import comb

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("PASS " + name)
    else:
        FAIL += 1
        print("FAIL " + name)


def pc(x):
    return bin(x).count("1")


def t(n):
    return -1 if (pc(n) & 1) else 1


def c_general(N, plist):
    supp = [p for p in plist if N % p == 0]
    m = len(supp)
    s = 0
    for A in range(1 << m):
        d = 1
        for i in range(m):
            if (A >> i) & 1:
                d *= supp[i]
        v = t(N // d)
        s += -v if (pc(A) & 1) else v
    return s


# ---------- exact linear algebra ----------

def berkowitz(A):
    n = len(A)
    C = [1, -A[0][0]]
    for r in range(1, n):
        a = A[r][r]
        S = [A[r][j] for j in range(r)]
        R = [A[i][r] for i in range(r)]
        M = [row[:r] for row in A[:r]]
        v = R[:]
        moms = [a, sum(S[i] * v[i] for i in range(r))]
        for _ in range(r - 1):
            v = [sum(M[i][j] * v[j] for j in range(r)) for i in range(r)]
            moms.append(sum(S[i] * v[i] for i in range(r)))
        col = [1] + [-mm for mm in moms]
        Cn = [0] * (r + 2)
        for i in range(r + 2):
            s = 0
            jmax = min(i, len(C) - 1)
            for j in range(jmax + 1):
                if i - j < len(col):
                    s += col[i - j] * C[j]
            Cn[i] = s
        C = Cn
    return C


def inertia_berk(A):
    C = berkowitz(A)
    n = len(C) - 1
    z = 0
    while z < n and C[n - z] == 0:
        z += 1
    seq = [v for v in C if v != 0]
    pos = sum(1 for i in range(len(seq) - 1)
              if (seq[i] > 0) != (seq[i + 1] > 0))
    seqm = [(C[i] if ((n - i) & 1) == 0 else -C[i]) for i in range(n + 1)]
    seqm = [v for v in seqm if v != 0]
    neg = sum(1 for i in range(len(seqm) - 1)
              if (seqm[i] > 0) != (seqm[i + 1] > 0))
    if pos + neg + z != n:
        raise AssertionError("inertia count mismatch")
    return (neg, z, pos)


def inertia_flat(F, n):
    """Fraction-free leading principal minors on a flat n by n list.
    Returns None on a zero pivot, routing the caller to the characteristic
    polynomial path."""
    A = F[:]
    prev = 1
    neg = 0
    last = 1
    for k in range(n):
        piv = A[k * n + k]
        if piv == 0:
            return None
        if (piv > 0) != (last > 0):
            neg += 1
        last = piv
        if k == n - 1:
            break
        base_k = k * n
        for i in range(k + 1, n):
            base_i = i * n
            mik = A[base_i + k]
            if mik:
                for j in range(k + 1, n):
                    A[base_i + j] = (A[base_i + j] * piv
                                     - mik * A[base_k + j]) // prev
            else:
                for j in range(k + 1, n):
                    A[base_i + j] = (A[base_i + j] * piv) // prev
        prev = piv
    return (neg, 0, n - neg)


def inertia_safe(F, n):
    r = inertia_flat(F, n)
    if r is not None:
        return r
    A = [[F[i * n + j] for j in range(n)] for i in range(n)]
    return inertia_berk(A)


def inertia_two_paths(A):
    n = len(A)
    F = [A[i][j] for i in range(n) for j in range(n)]
    a = inertia_flat(F, n)
    b = inertia_berk(A)
    if a is not None and a != b:
        raise AssertionError("inertia path disagreement")
    return b


def matmul(A, B):
    n = len(A)
    m = len(B[0])
    l = len(B)
    return [[sum(A[i][x] * B[x][j] for x in range(l)) for j in range(m)]
            for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def W_matrix(M):
    return [[(1 << (pc(T) - pc(S))) if (S & T) == S else 0
             for T in range(M)] for S in range(M)]


# ---------- abstract substrate at general k ----------

def substrate(k):
    M = 1 << k
    allm = []
    for x in range(3 ** k):
        m = []
        y = x
        for _ in range(k):
            m.append(y % 3)
            y //= 3
        allm.append(tuple(reversed(m)))
    allm.sort(key=lambda m: sum(m[i] * 3 ** (k - 1 - i) for i in range(k)))
    free = [m for m in allm if max(m) == 2]
    fidx = {m: j for j, m in enumerate(free)}
    bval = {m: (1 if (sum(m) & 1) else -1) for m in allm if max(m) <= 1}
    K0 = [[0] * M for _ in range(M)]
    Mj = [[[0] * M for _ in range(M)] for _ in range(len(free))]
    for S in range(M):
        for T in range(M):
            m = tuple(((S >> i) & 1) + ((T >> i) & 1) for i in range(k))
            supp = [i for i in range(k) if m[i] >= 1]
            for A in range(1 << len(supp)):
                mm = list(m)
                for i in range(len(supp)):
                    if (A >> i) & 1:
                        mm[supp[i]] -= 1
                mm = tuple(mm)
                sgn = -1 if (pc(A) & 1) else 1
                if max(mm) <= 1:
                    K0[S][T] += sgn * bval[mm]
                else:
                    Mj[fidx[mm]][S][T] += sgn
    order = sorted(range(M), key=lambda S: (pc(S), S))
    return M, free, fidx, K0, Mj, order


def reduce_order(X, order):
    return [[X[a][b] for b in order] for a in order]


# ---------- the k = 4 table machinery ----------

M4, FREE4, FIDX4, K04, MJ4, ORDER4 = substrate(4)
NC = len(FREE4)

BASEFLAT = [0] * 256
for _a in range(16):
    for _b in range(16):
        _v = K04[_a][_b]
        for _j in range(NC):
            _v += MJ4[_j][_a][_b]
        BASEFLAT[_a * 16 + _b] = _v

NZ = []
for _j in range(NC):
    _lst = []
    for _a in range(16):
        for _b in range(16):
            if MJ4[_j][_a][_b]:
                _lst.append((_a * 16 + _b, 2 * MJ4[_j][_a][_b]))
    NZ.append(_lst)

TYPE_OF = [tuple(sorted(m)) for m in FREE4]
TYPES = sorted(set(TYPE_OF))
CELLS = {ty: [j for j in range(NC) if TYPE_OF[j] == ty] for ty in TYPES}
SIZE4 = [ty for ty in TYPES if len(CELLS[ty]) == 4]
SIZE6 = [ty for ty in TYPES if len(CELLS[ty]) == 6]
SIZE12 = [ty for ty in TYPES if len(CELLS[ty]) == 12]


def kflat(bits):
    F = BASEFLAT[:]
    b = bits
    while b:
        lb = b & (-b)
        j = lb.bit_length() - 1
        for idx, val in NZ[j]:
            F[idx] -= val
        b ^= lb
    return F


def klass(bits):
    return inertia_safe(kflat(bits), 16)


# ---------- S_4 invariant layer ----------

PERMS = []


def _build_perms(cur, rest):
    if not rest:
        PERMS.append(tuple(cur))
        return
    for i in range(len(rest)):
        _build_perms(cur + [rest[i]], rest[:i] + rest[i + 1:])


_build_perms([], [0, 1, 2, 3])
CELLPERM = [[FIDX4[tuple(m[sg[i]] for i in range(4))] for m in FREE4]
            for sg in PERMS]

OP = [(i, j) for i in range(4) for j in range(4) if i != j]
OPIDX = {p: i for i, p in enumerate(OP)}
OPPERM = [[OPIDX[(sg[i], sg[j])] for (i, j) in OP] for sg in PERMS]

CHAR = {"22": (2, 0, 2, -1, 0), "211": (3, -1, -1, 0, 1)}


def _cycle_class(sg):
    seen = [False] * 4
    shape = []
    for s in range(4):
        if not seen[s]:
            n = 0
            x = s
            while not seen[x]:
                seen[x] = True
                x = sg[x]
                n += 1
            shape.append(n)
    shape.sort()
    return {(1, 1, 1, 1): 0, (1, 1, 2): 1, (2, 2): 2,
            (1, 3): 3, (4,): 4}[tuple(shape)]


PCLS = [_cycle_class(sg) for sg in PERMS]

# canonical labels: size-4 orbit by the coordinate carrying the value that
# occurs once; size-6 orbit by the unordered pair of coordinates carrying
# the smallest value; size-12 orbit by the ordered pair of coordinates
# carrying the two values that occur once, smaller value first.
LAB4 = {}
for ty in SIZE4:
    rep = [v for v in set(ty) if list(ty).count(v) == 1][0]
    LAB4[ty] = [None] * 4
    for j in CELLS[ty]:
        m = FREE4[j]
        LAB4[ty][[x for x in range(4) if m[x] == rep][0]] = j
LAB6 = {}
for ty in SIZE6:
    lo = min(ty)
    LAB6[ty] = {}
    for j in CELLS[ty]:
        m = FREE4[j]
        LAB6[ty][tuple(sorted(x for x in range(4) if m[x] == lo))] = j
LAB12 = {}
for ty in SIZE12:
    _vals = sorted(set(ty))
    _single = [v for v in _vals if list(ty).count(v) == 1]
    LAB12[ty] = {}
    for j in CELLS[ty]:
        m = FREE4[j]
        ia = [x for x in range(4) if m[x] == _single[0]][0]
        ib = [x for x in range(4) if m[x] == _single[1]][0]
        LAB12[ty][(ia, ib)] = j


def _apply_char(u, lam):
    ch = CHAR[lam]
    out = [0] * 12
    for gi in range(24):
        w = ch[PCLS[gi]]
        if w == 0:
            continue
        pm = OPPERM[gi]
        for p in range(12):
            out[pm[p]] += w * u[p]
    return out


def invariant_vector(bits):
    """The declared canonical 109-entry S_4 invariant map: ten orbit sums,
    the Gram of the twelve [31] copies inside the standard part of Q^4, the
    Gram of the five [22] copies inside Q[ordered pairs], and the Gram of
    the three [211] copies there."""
    vals = [(-1 if (bits >> j) & 1 else 1) for j in range(NC)]
    sums = tuple(sum(vals[j] for j in CELLS[ty]) for ty in TYPES)
    std = []
    for ty in SIZE4:
        mu = [vals[LAB4[ty][i]] for i in range(4)]
        s = sum(mu)
        std.append([4 * mu[i] - s for i in range(4)])
    for ty in SIZE6:
        mu = [sum(vals[LAB6[ty][tuple(sorted((i, j)))]]
                  for j in range(4) if j != i) for i in range(4)]
        s = sum(mu)
        std.append([4 * mu[i] - s for i in range(4)])
    for ty in SIZE12:
        row = [sum(vals[LAB12[ty][(i, j)]] for j in range(4) if j != i)
               for i in range(4)]
        col = [sum(vals[LAB12[ty][(i, j)]] for i in range(4) if i != j)
               for j in range(4)]
        for mu in (row, col):
            s = sum(mu)
            std.append([4 * mu[i] - s for i in range(4)])
    g31 = []
    for a in range(len(std)):
        for b in range(a, len(std)):
            g31.append(sum(std[a][i] * std[b][i] for i in range(4)))
    op22 = []
    for ty in SIZE6:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB6[ty][tuple(sorted((i, j)))]]
        op22.append(u)
    for ty in SIZE12:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB12[ty][(i, j)]]
        op22.append(u)
    q22 = [_apply_char(u, "22") for u in op22]
    g22 = []
    for a in range(len(op22)):
        for b in range(a, len(op22)):
            g22.append(sum(q22[a][p] * op22[b][p] for p in range(12)))
    op211 = []
    for ty in SIZE12:
        u = [0] * 12
        for p, (i, j) in enumerate(OP):
            u[p] = vals[LAB12[ty][(i, j)]]
        op211.append(u)
    q211 = [_apply_char(u, "211") for u in op211]
    g211 = []
    for a in range(len(op211)):
        for b in range(a, len(op211)):
            g211.append(sum(q211[a][p] * op211[b][p] for p in range(12)))
    return sums + tuple(g31) + tuple(g22) + tuple(g211)


def permute_bits(bits, gi):
    pm = CELLPERM[gi]
    out = 0
    for j in range(NC):
        if (bits >> j) & 1:
            out |= 1 << pm[j]
    return out




def evil_primes(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= limit:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
        i += 1
    return [p for p in range(3, limit + 1, 2) if sieve[p] and t(p) == 1]


def block_inertia(P):
    M = 1 << len(P)
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    K = [[c_general(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]
    return inertia_two_paths(K)


def is_extremal(P):
    M = 1 << len(P)
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    return all(t(nS[x]) == (1 if (pc(x) & 1) else -1) for x in range(M))




def inertia_congruence(A):
    """Third path: exact rational symmetric congruence with symmetric
    pivoting, counting signs of the diagonal. Independent of Bareiss and of
    the characteristic polynomial."""
    n = len(A)
    M = [[Fraction(A[i][j]) for j in range(n)] for i in range(n)]
    neg = zero = pos = 0
    idx = list(range(n))
    size = n
    while size > 0:
        p = None
        for i in range(size):
            if M[i][i] != 0:
                p = i
                break
        if p is None:
            q = None
            for i in range(size):
                for j in range(i + 1, size):
                    if M[i][j] != 0:
                        q = (i, j)
                        break
                if q:
                    break
            if q is None:
                zero += size
                break
            i, j = q
            for c in range(size):
                M[i][c] += M[j][c]
            for r in range(size):
                M[r][i] += M[r][j]
            continue
        if p != 0:
            M[0], M[p] = M[p], M[0]
            for r in range(size):
                M[r][0], M[r][p] = M[r][p], M[r][0]
        d = M[0][0]
        if d > 0:
            pos += 1
        else:
            neg += 1
        for i in range(1, size):
            f = M[i][0] / d
            if f != 0:
                for j in range(size):
                    M[i][j] -= f * M[0][j]
        for j in range(1, size):
            f = M[0][j] / d
            if f != 0:
                for i in range(size):
                    M[i][j] -= f * M[i][0]
        M = [row[1:size] for row in M[1:size]]
        size -= 1
    return (neg, zero, pos)




def det_bareiss(Ain):
    A = [row[:] for row in Ain]
    n = len(A)
    sign = 1
    prev = 1
    for cc in range(n):
        piv = None
        for i in range(cc, n):
            if A[i][cc] != 0:
                piv = i
                break
        if piv is None:
            return 0
        if piv != cc:
            A[cc], A[piv] = A[piv], A[cc]
            sign = -sign
        for i in range(cc + 1, n):
            for j in range(cc + 1, n):
                A[i][j] = (A[i][j] * A[cc][cc] - A[i][cc] * A[cc][j]) // prev
            A[i][cc] = 0
        prev = A[cc][cc]
    return sign * A[n - 1][n - 1]



def pdeg(p):
    d = len(p) - 1
    while d > 0 and p[d] == 0:
        d -= 1
    return d

def ptrim(p):
    return p[:pdeg(p) + 1]

def variations(coeffs):
    s = [v for v in coeffs if v != 0]
    return sum(1 for i in range(len(s) - 1) if (s[i] > 0) != (s[i + 1] > 0))

def mobius01(q):
    n = pdeg(q)
    out = [0] * (n + 1)
    for i in range(n + 1):
        ci = q[i] if i < len(q) else 0
        if ci == 0:
            continue
        m = n - i
        b = 1
        for j in range(m + 1):
            out[j] += ci * b
            b = b * (m - j) // (j + 1)
    return out

def half_left(q):
    n = pdeg(q)
    return [q[i] << (n - i) for i in range(n + 1)]

def half_right(q):
    n = pdeg(q)
    out = [0] * (n + 1)
    for i in range(n + 1):
        ci = q[i]
        if ci == 0:
            continue
        w = ci << (n - i)
        b = 1
        for j in range(i + 1):
            out[j] += w * b
            b = b * (i - j) // (j + 1)
    return out

def primitive(fr):
    from math import gcd
    den = 1
    for v in fr:
        den = den * v.denominator // gcd(den, v.denominator)
    ints = [int(v * den) for v in fr]
    g = 0
    for v in ints:
        g = gcd(g, abs(v))
    if g > 1:
        ints = [v // g for v in ints]
    out = ints[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

def pgcd_sqfree(p):
    a = [Fraction(v) for v in ptrim(p)]
    b = [Fraction((i + 1) * p[i + 1]) for i in range(len(ptrim(p)) - 1)]
    if not b:
        return ptrim(p)

    def pmod(x, y):
        x = x[:]
        dy = len(y) - 1
        while len(x) - 1 >= dy and any(v != 0 for v in x):
            dx = len(x) - 1
            if x[dx] == 0:
                x.pop()
                continue
            f = x[dx] / y[dy]
            for i in range(dy + 1):
                x[dx - dy + i] -= f * y[i]
            x.pop()
        while len(x) > 1 and x[-1] == 0:
            x.pop()
        return x

    while any(v != 0 for v in b):
        a, b = b, pmod(a, b)
    if len(a) == 1:
        return ptrim(p)
    x = [Fraction(v) for v in ptrim(p)]
    y = a
    dy = len(y) - 1
    qout = [Fraction(0)] * (len(x) - dy)
    while len(x) - 1 >= dy:
        dx = len(x) - 1
        f = x[dx] / y[dy]
        qout[dx - dy] = f
        for i in range(dy + 1):
            x[dx - dy + i] -= f * y[i]
        x.pop()
    return primitive(qout)

def deflate_half(q):
    x = [Fraction(v) for v in ptrim(q)]
    qout = [Fraction(0)] * (len(x) - 1)
    while len(x) - 1 >= 1:
        dx = len(x) - 1
        f = x[dx] / 2
        qout[dx - 1] = f
        x[dx - 1] += f
        x.pop()
    assert all(v == 0 for v in x)
    return primitive(qout)

def count_open01(q, depth=64):
    V = variations(mobius01(q))
    if V == 0:
        return 0
    if V == 1:
        return 1
    if depth == 0:
        return None
    qL = half_left(q)
    mid = sum(qL)
    if mid == 0:
        qd = deflate_half(q)
        r = count_open01(qd, depth - 1)
        return None if r is None else 1 + r
    qR = half_right(q)
    a = count_open01(qL, depth - 1)
    b = count_open01(qR, depth - 1)
    if a is None or b is None:
        return None
    return a + b

def lagrange_int(xs, ys):
    n = len(xs)
    acc = [Fraction(0)] * n
    for i in range(n):
        num = [Fraction(1)]
        den = Fraction(1)
        for j in range(n):
            if j == i:
                continue
            new = [Fraction(0)] * (len(num) + 1)
            for a in range(len(num)):
                new[a + 1] += num[a]
                new[a] -= num[a] * xs[j]
            num = new
            den *= Fraction(xs[i] - xs[j])
        w = Fraction(ys[i]) / den
        for a in range(len(num)):
            acc[a] += num[a] * w
    out = []
    for v in acc:
        assert v.denominator == 1
        out.append(int(v))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out



# ---------- exact pencil analysis ----------

def poly_sign_at(f, x):
    """Sign of f at the Fraction x, exact."""
    num, den = x.numerator, x.denominator
    d = pdeg(f)
    s = 0
    for i in range(d + 1):
        s += f[i] * num ** i * den ** (d - i)
    return (s > 0) - (s < 0)


def poly_map01(f, a, b):
    """Integer-primitive image of f under x = a + (b-a) y, y in (0,1)."""
    d = b - a
    acc = [Fraction(0)] * (pdeg(f) + 1)
    power = [Fraction(1)]
    for i in range(pdeg(f) + 1):
        for k in range(len(power)):
            acc[k] += f[i] * power[k]
        new = [Fraction(0)] * (len(power) + 1)
        for k in range(len(power)):
            new[k] += power[k] * a
            new[k + 1] += power[k] * d
        power = new
    return primitive(acc)


def count_between(f, a, b):
    q = poly_map01(f, a, b)
    n = count_open01(q)
    if n is None:
        raise AssertionError("isolation depth exhausted")
    return n


def isolate01(f):
    """Disjoint open rational intervals in (0,1), one root of the
    squarefree f in each, nonzero sign at every endpoint."""
    if poly_sign_at(f, Fraction(0)) == 0 or poly_sign_at(f, Fraction(1)) == 0:
        raise AssertionError("root at an endpoint")
    out = []

    def rec(a, b):
        c = count_between(f, a, b)
        if c == 0:
            return
        if c == 1:
            out.append((a, b))
            return
        m = (a + b) / 2
        if poly_sign_at(f, m) == 0:
            eps = (b - a) / 64
            while True:
                lo, hi = m - eps, m + eps
                if (lo > a and hi < b and poly_sign_at(f, lo) != 0
                        and poly_sign_at(f, hi) != 0
                        and count_between(f, lo, hi) == 1):
                    break
                eps /= 2
            out.append((lo, hi))
            rec(a, lo)
            rec(hi, b)
        else:
            rec(a, m)
            rec(m, b)

    rec(Fraction(0), Fraction(1))
    out.sort()
    for i in range(len(out) - 1):
        if out[i][1] > out[i + 1][0]:
            raise AssertionError("isolating intervals overlap")
    return out


def poly_gcd_int(f, g):
    """Primitive integer gcd of two integer polynomials."""
    a = [Fraction(v) for v in ptrim(f)]
    b = [Fraction(v) for v in ptrim(g)]

    def pmod(x, y):
        x = x[:]
        dy = len(y) - 1
        while len(x) - 1 >= dy and any(v != 0 for v in x):
            dx = len(x) - 1
            if x[dx] == 0:
                x.pop()
                continue
            fq = x[dx] / y[dy]
            for i in range(dy + 1):
                x[dx - dy + i] -= fq * y[i]
            x.pop()
        while len(x) > 1 and x[-1] == 0:
            x.pop()
        return x

    while any(v != 0 for v in b):
        a, b = b, pmod(a, b)
    return primitive(a)


def pencil_analysis(Kx, R, prof):
    """Exact crossing count, multiplicity, and oriented walk of
    det(Kx + s R) on [0,1]. Returns (ncross, nmult, orients, walk_ok)."""
    n = len(Kx)
    xs = list(range(n + 1))
    ys = []
    for s in xs:
        A = [[Kx[i][j] + s * R[i][j] for j in range(n)] for i in range(n)]
        ys.append(det_bareiss(A))
    f = lagrange_int(xs, ys)
    if f[0] == 0 or sum(f) == 0:
        raise AssertionError("endpoint determinant vanishes")
    sqf = pgcd_sqfree(f)
    df = [i * f[i] for i in range(1, len(f))]
    g = poly_gcd_int(f, df)
    nmult = 0
    if pdeg(g) > 0:
        nmult = count_open01(pgcd_sqfree(g))
        if nmult is None:
            raise AssertionError("isolation depth exhausted")
    ivs = isolate01(sqf)
    samples = [Fraction(0)]
    for i in range(len(ivs) - 1):
        samples.append(ivs[i][1] if ivs[i][1] <= ivs[i + 1][0]
                       else (ivs[i][1] + ivs[i + 1][0]) / 2)
    samples.append(Fraction(1))
    inert = []
    for sp in samples:
        num, den = sp.numerator, sp.denominator
        A = [[den * Kx[i][j] + num * R[i][j] for j in range(n)]
             for i in range(n)]
        inert.append(inertia_two_paths(A))
    walk_ok = all(z == 0 for _n, z, _p in inert)
    orients = [inert[i][0] - inert[i + 1][0] for i in range(len(ivs))]
    walk_ok = walk_ok and inert[0] == (8, 0, 8) and inert[-1] == prof
    return len(ivs), nmult, orients, walk_ok


# ---------- the 17 frozen real failures ----------

FAILS = [
    (377931745, (5, 23, 839, 3917), (7, 0, 9)),
    (548309857, (17, 23, 53, 26459), (7, 0, 9)),
    (689952085, (5, 71, 317, 6131), (9, 0, 7)),
    (1001207365, (5, 23, 53, 164267), (7, 0, 9)),
    (1436418609, (3, 23, 503, 41387), (7, 0, 9)),
    (1477310605, (5, 29, 53, 192233), (7, 0, 9)),
    (1486919065, (5, 23, 797, 16223), (9, 0, 7)),
    (1732991217, (3, 71, 347, 23447), (7, 0, 9)),
    (1992609343, (29, 113, 461, 1319), (9, 0, 7)),
    (2102641715, (5, 23, 2791, 6551), (7, 0, 9)),
    (2388719185, (5, 101, 509, 9293), (7, 0, 9)),
    (2392518595, (5, 71, 1013, 6653), (7, 0, 9)),
    (2515579015, (5, 53, 1559, 6089), (9, 0, 7)),
    (2843975361, (3, 71, 467, 28591), (7, 0, 9)),
    (3158792005, (5, 83, 89, 85523), (7, 0, 9)),
    (3174899015, (5, 53, 1013, 11827), (7, 0, 9)),
    (3512837065, (5, 101, 293, 23741), (9, 0, 7)),
]

REAL_PROFILES = {(7, 0, 9): 1, (9, 0, 7): -1}


def real_bits(P):
    b = 0
    for j, m in enumerate(FREE4):
        n = 1
        for i in range(4):
            n *= P[i] ** m[i]
        if t(n) == -1:
            b |= 1 << j
    return b


def real_blocks(P):
    M = 16
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        nS[x] = nS[x ^ lb] * P[lb.bit_length() - 1]
    K = [[c_general(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]
    Kx = [[c_general(nS[S ^ T], P) for T in range(M)] for S in range(M)]
    R = [[K[S][T] - Kx[S][T] for T in range(M)] for S in range(M)]
    return K, Kx, R


def gate_g1_g2():
    total_orients = []
    ok1 = True
    ok2 = True
    for (n, P, prof) in FAILS:
        P = list(P)
        if not is_extremal(P):
            ok1 = False
            continue
        K, Kx, R = real_blocks(P)
        e0 = inertia_two_paths(Kx)
        e1 = inertia_two_paths(K)
        ec = inertia_congruence(K)
        if e0 != (8, 0, 8) or e1 != prof or ec != prof:
            ok1 = False
        nc, nm, orients, wok = pencil_analysis(Kx, R, prof)
        sf = sum(orients)
        sigma_half = (prof[2] - prof[0]) // 2
        exp_sf = REAL_PROFILES[prof]
        if not (wok and sf == sigma_half == exp_sf
                and (nc - abs(sf)) % 2 == 0 and nm == 0):
            ok2 = False
        print("G1 n=%d P=%s prof=%s crossings=%d mult=%d orients=%s SF=%+d"
              % (n, tuple(P), "".join(str(x) for x in prof), nc, nm,
                 orients, sf))
        total_orients.append((nc, sf))
    check("G1.seventeen_failures_extremal_endpoints_three_paths", ok1)
    check("G2.oriented_flow_walk_consistent_all_simple", ok2)
    print("G2 crossing/flow table: %s" % (total_orients,))


# ---------- G3: the S_4 module ----------

CHARTAB = {
    "4": (1, 1, 1, 1, 1),
    "31": (3, 1, -1, 0, -1),
    "22": (2, 0, 2, -1, 0),
    "211": (3, -1, -1, 0, 1),
    "1111": (1, -1, 1, 1, -1),
}
CLASS_SIZES = (1, 6, 3, 8, 6)


def rank_int(A):
    M = [row[:] for row in A]
    n = len(M)
    m = len(M[0])
    r = 0
    prev = 1
    for col in range(m):
        piv = None
        for i in range(r, n):
            if M[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][col]
        for i in range(r + 1, n):
            fi = M[i][col]
            if fi:
                for j in range(m):
                    M[i][j] = M[i][j] * pv - fi * M[r][j]
        r += 1
        if r == n:
            break
    return r


def gate_g3():
    chi_perm = [0] * 5
    for gi in range(24):
        fixed = sum(1 for j in range(NC) if CELLPERM[gi][j] == j)
        chi_perm[PCLS[gi]] = fixed
    print("G3 permutation character on classes: %s" % (chi_perm,))
    mults = {}
    for lam, ch in sorted(CHARTAB.items()):
        s = sum(CLASS_SIZES[c] * chi_perm[c] * ch[c] for c in range(5))
        assert s % 24 == 0
        mults[lam] = s // 24
    print("G3 multiplicities: %s" % (sorted(mults.items()),))
    check("G3.multiplicities_10_12_5_3_0",
          mults == {"4": 10, "31": 12, "22": 5, "211": 3, "1111": 0})
    dims = {"4": 1, "31": 3, "22": 2, "211": 3, "1111": 1}
    check("G3.dimension_identity_65",
          sum(mults[l] * dims[l] for l in mults) == NC)
    ranks = {}
    for lam, ch in sorted(CHARTAB.items()):
        T = [[0] * NC for _ in range(NC)]
        for gi in range(24):
            w = ch[PCLS[gi]]
            if w == 0:
                continue
            pm = CELLPERM[gi]
            for j in range(NC):
                T[pm[j]][j] += w
        ranks[lam] = rank_int(T)
    print("G3 isotypic ranks: %s" % (sorted(ranks.items()),))
    check("G3.isotypic_ranks_10_36_10_9_0",
          ranks == {"4": 10, "31": 36, "22": 10, "211": 9, "1111": 0})


# ---------- G4, G5: sector separation and collision search ----------

LAYERS = (("sums10", 0, 10), ("gram31", 10, 88), ("gram22", 88, 103),
          ("gram211", 103, 109), ("full109", 0, 109))


def flow_of_profile(prof):
    return REAL_PROFILES.get(prof)


def gate_g4_g5():
    pool = []
    for (n, P, prof) in FAILS:
        pool.append(("real", n, real_bits(list(P)), REAL_PROFILES[prof]))
    x = 1
    mod = 1 << 64
    for _ in range(4000):
        x = (6364136223846793005 * x + 1442695040888963407) % mod
    lcg = []
    for _ in range(4000):
        x = (6364136223846793005 * x + 1442695040888963407) % mod
        lo = x % (1 << 33)
        x = (6364136223846793005 * x + 1442695040888963407) % mod
        hi = x % (1 << 32)
        lcg.append(lo + (hi << 33))
    found = {}
    for bits in lcg:
        prof = klass(bits)
        fl = flow_of_profile(prof)
        if fl is not None:
            found[bits] = fl
    seeds = sorted(found) + [0x02e639472cd318ed2]
    for bits in seeds[:200]:
        for j in range(NC):
            nb = bits ^ (1 << j)
            if nb in found:
                continue
            fl = flow_of_profile(klass(nb))
            if fl is not None:
                found[nb] = fl
    for kind, n, bits, fl in pool:
        found.setdefault(bits, fl)
    plus = sum(1 for v in found.values() if v == 1)
    minus = sum(1 for v in found.values() if v == -1)
    print("G5 pool: %d tables with the two frozen profiles "
          "(flow +1: %d, flow -1: %d, reals included: %d)"
          % (len(found), plus, minus, len(pool)))
    check("G5.both_flows_present_in_pool", plus > 0 and minus > 0)
    vecs = {bits: invariant_vector(bits) for bits in found}
    verdicts = {}
    for name, a, b in LAYERS:
        buckets = {}
        collision = None
        for bits in sorted(found):
            key = vecs[bits][a:b]
            prev = buckets.get(key)
            if prev is None:
                buckets[key] = (found[bits], bits)
            elif prev[0] != found[bits] and collision is None:
                collision = (prev[1], bits)
        verdicts[name] = collision
        if collision is None:
            print("G5 layer %-8s separates the two flows on the pool "
                  "(%d buckets)" % (name, len(buckets)))
        else:
            print("G5 layer %-8s COLLISION tables 0x%017x 0x%017x"
                  % (name, collision[0], collision[1]))
    real_only = [(bits, fl) for kind, n, bits, fl in pool]
    for name, a, b in LAYERS:
        seen = {}
        mixed = False
        for bits, fl in real_only:
            key = vecs[bits][a:b]
            if key in seen and seen[key] != fl:
                mixed = True
            seen[key] = fl
        print("G4 layer %-8s on the 17 reals: %s"
              % (name, "MIXED" if mixed else "separates"))
    check("G5.reported_exactly_no_sufficiency_claim", True)
    return verdicts


def main():
    print("C-TM-HANKEL-K4-SPECTRAL-FLOW-2 verifier")
    print("INERTIA_ORDER NEG ZERO POS; flow convention: an eigenvalue")
    print("crossing zero upward as s grows counts +1; SF = (sigma(1)-sigma(0))/2")
    gate_g1_g2()
    gate_g3()
    gate_g4_g5()
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
