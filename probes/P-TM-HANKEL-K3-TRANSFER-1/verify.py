#!/usr/bin/env python3
# P-TM-HANKEL-K3-TRANSFER-1 verify.py
# Pinned together with PREREG.md before the first formal execution.
# Python standard library only. Exact integers and Fractions only.
# No float anywhere. Deterministic stdout. No wall clock, no hostname,
# no machine identifier. Run from the repository root with
# env -i PATH="$PATH" HOME="$HOME" LC_ALL=C LANG=C \
#   PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
#   python3 probes/P-TM-HANKEL-K3-TRANSFER-1/verify.py

import sys
import itertools
from fractions import Fraction

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

def pc2(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

def t(n):
    s = pc(n)
    if s != pc2(n):
        raise AssertionError("popcount mismatch")
    return -1 if (s & 1) else 1

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

def inertia_sym(A):
    C = berkowitz(A)
    n = len(C) - 1
    z = 0
    while z < n and C[n - z] == 0:
        z += 1
    seq = [v for v in C if v != 0]
    pos = sum(1 for i in range(len(seq) - 1) if (seq[i] > 0) != (seq[i + 1] > 0))
    seqm = [(C[i] if ((n - i) & 1) == 0 else -C[i]) for i in range(n + 1)]
    seqm = [v for v in seqm if v != 0]
    neg = sum(1 for i in range(len(seqm) - 1)
              if (seqm[i] > 0) != (seqm[i + 1] > 0))
    assert pos + neg + z == n
    return (neg, z, pos)

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

def det_cross(A):
    d1 = det_bareiss(A)
    C = berkowitz(A)
    n = len(A)
    d2 = C[n] if (n % 2 == 0) else -C[n]
    assert d1 == d2, "det path disagreement"
    return d1

def matmul(A, B):
    n = len(A)
    m = len(B[0])
    l = len(B)
    return [[sum(A[i][x] * B[x][j] for x in range(l)) for j in range(m)]
            for i in range(n)]

def transpose(A):
    return [list(r) for r in zip(*A)]

def cube_products(P):
    k = len(P)
    M = 1 << k
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        i = lb.bit_length() - 1
        nS[x] = nS[x ^ lb] * P[i]
    return M, nS

_BLOCK_MEMO = {}

def build_blocks(P):
    key = tuple(P)
    if key in _BLOCK_MEMO:
        return _BLOCK_MEMO[key]
    M, nS = cube_products(P)
    K = [[c_general(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]
    Kx = [[c_general(nS[S ^ T], P) for T in range(M)] for S in range(M)]
    R = [[K[S][T] - Kx[S][T] for T in range(M)] for S in range(M)]
    _BLOCK_MEMO[key] = (M, nS, K, Kx, R)
    return _BLOCK_MEMO[key]

def W_matrix(M):
    return [[(1 << (pc(T) - pc(S))) if (S & T) == S else 0
             for T in range(M)] for S in range(M)]

def is_extremal_set(P):
    M, nS = cube_products(P)
    return all(t(nS[x]) == (1 if (pc(x) & 1) else -1) for x in range(M))

def evil_primes(limit):
    out = []
    for p in range(3, limit + 1, 2):
        q = 3
        pr = True
        while q * q <= p:
            if p % q == 0:
                pr = False
                break
            q += 2
        if pr and t(p) == 1:
            out.append(p)
    return out

# polynomial helpers for exact root isolation in (0,1)

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

# ---------- G1: bridge, parity, layers ----------

def layer_d(P, U):
    M, nS = cube_products(P)
    full = M - 1
    comp = full ^ U
    bits = [i for i in range(len(P)) if (comp >> i) & 1]
    ubits = [i for i in range(len(P)) if (U >> i) & 1]
    out = {}
    for zi in range(1 << len(bits)):
        z = 0
        for j in range(len(bits)):
            if (zi >> j) & 1:
                z |= 1 << bits[j]
        s = 0
        for vi in range(1 << len(ubits)):
            V = 0
            for j in range(len(ubits)):
                if (vi >> j) & 1:
                    V |= 1 << ubits[j]
            val = c_general(nS[z] * nS[V] * nS[V], P)
            s += val if ((pc(U) - pc(V)) & 1) == 0 else -val
        out[z] = s
    return out

def gate_g1():
    prs2 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    prs3 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    pools = []
    for i in range(len(prs2)):
        for j in range(i + 1, len(prs2)):
            pools.append([prs2[i], prs2[j]])
    for i in range(len(prs3)):
        for j in range(i + 1, len(prs3)):
            for l in range(j + 1, len(prs3)):
                pools.append([prs3[i], prs3[j], prs3[l]])
    pools += [[3, 5, 7, 11], [5, 7, 11, 13], [7, 11, 13, 17],
              [3, 23, 71, 1523], [3, 5, 7, 11, 13], [3, 23, 503, 857, 1879]]
    ok_empty = True
    ok_mod2 = True
    ok_lay = True
    ok_inv = True
    for P in pools:
        M, nS, K, Kx, R = build_blocks(P)
        if any(R[0][j] != 0 or R[j][0] != 0 for j in range(M)):
            ok_empty = False
        if any((R[i][j] - (1 if (i == j and i != 0) else 0)) % 2 != 0
               for i in range(1, M) for j in range(1, M)):
            ok_mod2 = False
        Rt = [[R[i][j] for j in range(1, M)] for i in range(1, M)]
        if det_cross(Rt) % 2 == 0:
            ok_mod2 = False
        dall = {0: {z: c_general(nS[z], P) for z in range(M)}}
        for U in range(1, M):
            d = layer_d(P, U)
            dall[U] = d
            for z, v in d.items():
                if z == 0:
                    if v % 2 == 0:
                        ok_lay = False
                else:
                    if v % 2 != 0:
                        ok_lay = False
            zs = sorted(d.keys())
            m = len(zs)
            Ad = [[d[zs[i] ^ zs[j]] for j in range(m)] for i in range(m)]
            if any((Ad[i][j] - (1 if i == j else 0)) % 2 != 0
                   for i in range(m) for j in range(m)):
                ok_lay = False
            if det_cross(Ad) % 2 == 0:
                ok_lay = False
        for S in range(M):
            for T in range(M):
                U = S & T
                z = S ^ T
                s = 0
                V = U
                while True:
                    s += dall[V][z]
                    if V == 0:
                        break
                    V = (V - 1) & U
                if s != K[S][T]:
                    ok_inv = False
    check("G1.empty_row_and_column (%d sets)" % len(pools), ok_empty)
    check("G1.Rtilde_I_mod2_det_odd", ok_mod2)
    check("G1.layers_parity_identity_fullrank", ok_lay)
    check("G1.layer_inversion_exact", ok_inv)

# ---------- G2, G3: Witt congruence and the k = 2 theorem ----------

def D_diag(M):
    return [[((3 ** pc(S)) if (pc(S) & 1) else -(3 ** pc(S)))
             if S == T else 0 for T in range(M)] for S in range(M)]

def gate_g2_g3():
    m2 = [[1, -2], [-2, 1]]
    u2 = [[1, 2], [0, 1]]
    lhs = matmul(transpose(u2), matmul(m2, u2))
    check("G2.local_identity_diag_1_minus3", lhs == [[1, 0], [0, -3]])
    ev = evil_primes(1000)
    pairs = []
    for i in range(len(ev)):
        for j in range(i + 1, len(ev)):
            if t(ev[i] * ev[j]) == -1:
                pairs.append([ev[i], ev[j]])
    triples = [[3, 23, 71], [5, 23, 53], [5, 29, 53], [5, 23, 71]]
    chains = [[3, 23, 71, 1523], [3, 23, 503, 857, 1879]]
    print("G2 extremal pair count p<q<=1000: %d" % len(pairs))
    ok2 = True
    okpar = True
    for P in pairs + triples + chains:
        if not is_extremal_set(P):
            ok2 = False
            continue
        M, nS, K, Kx, R = build_blocks(P)
        W = W_matrix(M)
        if matmul(transpose(W), matmul(Kx, W)) != D_diag(M):
            ok2 = False
        Rp = matmul(transpose(W), matmul(R, W))
        if any(Rp[0][j] != 0 or Rp[j][0] != 0 for j in range(M)):
            okpar = False
        if any((Rp[i][j] - (1 if (i == j and i != 0) else 0)) % 2 != 0
               for i in range(1, M) for j in range(1, M)):
            okpar = False
    check("G2.witt_congruence_all_%d_extremal_sets" % (
        len(pairs) + len(triples) + len(chains)), ok2)
    check("G2.Rprime_parity_preserved", okpar)
    ok4 = True
    okbound = True
    for P in pairs:
        p, q = P
        A5 = t(p * p)
        B5 = t(q * q)
        D5 = t(p * p * q)
        E5 = t(p * q * q)
        F5 = t(p * p * q * q)
        M, nS, K, Kx, R = build_blocks(P)
        W = W_matrix(M)
        Rp = matmul(transpose(W), matmul(R, W))
        expect = [
            [0, 0, 0, 0],
            [0, A5, 0, A5 + D5],
            [0, 0, B5, B5 + E5],
            [0, A5 + D5, B5 + E5, 3 * D5 + 3 * E5 + F5]]
        if Rp != expect:
            ok4 = False
        if abs(3 * D5 + 3 * E5 + F5) > 7:
            okbound = False
    check("G3.corner_collapse_all_pairs", ok4)
    check("G3.corner_bound_le_7", okbound)
    iso = pairs[:128]
    print("G3 isolation scope: first %d extremal pairs lexicographic"
          % len(iso))
    okroots = True
    okinert = True
    for P in iso:
        M, nS, K, Kx, R = build_blocks(P)
        xs = list(range(M + 1))
        ys = []
        for s in xs:
            Am = [[Kx[i][j] + s * R[i][j] for j in range(M)] for i in range(M)]
            ys.append(det_bareiss(Am))
        poly = lagrange_int(xs, ys)
        if poly[0] == 0 or sum(poly) == 0:
            okroots = False
        else:
            nr = count_open01(pgcd_sqfree(poly))
            if nr != 0:
                okroots = False
        for num, den in ((0, 1), (1, 2), (1, 1)):
            Am = [[den * Kx[i][j] + num * R[i][j] for j in range(M)]
                  for i in range(M)]
            if inertia_sym(Am) != (2, 0, 2):
                okinert = False
    check("G3.zero_pencil_roots_first_128_pairs", okroots)
    check("G3.balanced_inertia_s_0_half_1_first_128", okinert)

# ---------- G4: the k = 3 falsification ----------

def lead_minors(A):
    n = len(A)
    M = [r[:] for r in A]
    prev = 1
    D = []
    for k in range(n):
        piv = M[k][k]
        if piv == 0:
            return None
        D.append(piv)
        if k == n - 1:
            break
        Mk = M[k]
        for i in range(k + 1, n):
            Mi = M[i]
            mik = Mi[k]
            for j in range(k + 1, n):
                Mi[j] = (Mi[j] * piv - mik * Mk[j]) // prev
        prev = piv
    return D

def gate_g4():
    WITS = [((5, 101, 293), -3840), ((83, 89, 263), -768),
            ((149, 269, 293), -9856)]
    okw = True
    for (tr, dexp) in WITS:
        P = list(tr)
        if not is_extremal_set(P):
            okw = False
            continue
        M, nS, K, Kx, R = build_blocks(P)
        i1 = inertia_sym(K)
        D = lead_minors(K)
        neg2 = None
        if D is not None:
            neg2 = 0
            last = 1
            for d in D:
                if (d > 0) != (last > 0):
                    neg2 += 1
                last = d
        detK = det_bareiss(K)
        xs = list(range(M + 1))
        ys = []
        for s in xs:
            Am = [[Kx[i][j] + s * R[i][j] for j in range(M)] for i in range(M)]
            ys.append(det_bareiss(Am))
        poly = lagrange_int(xs, ys)
        nr = count_open01(pgcd_sqfree(poly))
        if not (i1 == (5, 0, 3) and neg2 == 5 and detK == dexp
                and nr == 1 and poly[0] == 3 ** 12):
            okw = False
        print("G4 witness n=%d NEG=%d ZERO=%d POS=%d detK=%d roots01=%d" % (
            P[0] * P[1] * P[2], i1[0], i1[1], i1[2], detK, nr))
    check("G4.three_witnesses_two_paths", okw)
    N = 200000
    spf = list(range(N + 1))
    i = 2
    while i * i <= N:
        if spf[i] == i:
            for j in range(i * i, N + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    cnt = 0
    bad = 0
    n = 1
    while n <= N:
        m = n
        ps = []
        ok = True
        while m > 1:
            p = spf[m]
            m //= p
            if m % p == 0:
                ok = False
                break
            ps.append(p)
        if ok and len(ps) == 3 and ps[0] != 2:
            ps.sort()
            if is_extremal_set(ps):
                cnt += 1
                M2, nS2, K2, Kx2, R2 = build_blocks(ps)
                if inertia_sym(K2) != (4, 0, 4):
                    bad += 1
        n += 2
    check("G4.uniqueness_scan_157_triples_1_nonbalanced",
          cnt == 157 and bad == 1)
    ev = evil_primes(300)
    tot = 0
    fails = 0
    for a in range(len(ev)):
        for b in range(a + 1, len(ev)):
            for c in range(b + 1, len(ev)):
                p, q, r = ev[a], ev[b], ev[c]
                if (t(p * q) == -1 and t(p * r) == -1 and t(q * r) == -1
                        and t(p * q * r) == 1):
                    tot += 1
                    M2, nS2, K2, Kx2, R2 = build_blocks([p, q, r])
                    if inertia_sym(K2) != (4, 0, 4):
                        fails += 1
    check("G4.recount_99_triples_3_fail", tot == 99 and fails == 3)

# ---------- G5, G6, G7: abstract k = 3 structure ----------

def code(m):
    return 9 * m[0] + 3 * m[1] + m[2]

ALLM = sorted([(a, b, c) for a in range(3) for b in range(3)
               for c in range(3)], key=code)
FREE = [m for m in ALLM if max(m) == 2]
BINARY = [m for m in ALLM if max(m) <= 1]
FIDX = {m: j for j, m in enumerate(FREE)}
BVAL = {m: (1 if ((m[0] + m[1] + m[2]) & 1) else -1) for m in BINARY}
TOP4 = [j for j, m in enumerate(FREE)
        if tuple(sorted(m)) in ((1, 2, 2), (2, 2, 2))]
SUB15 = [j for j in range(19) if j not in TOP4]

def msub(m, A):
    return (m[0] - (1 if 0 in A else 0),
            m[1] - (1 if 1 in A else 0),
            m[2] - (1 if 2 in A else 0))

def build_linear_forms():
    K0 = [[0] * 8 for _ in range(8)]
    Mj = [[[0] * 8 for _ in range(8)] for _ in range(19)]
    for S in range(8):
        for T in range(8):
            m = tuple(((S >> i) & 1) + ((T >> i) & 1) for i in range(3))
            supp = [i for i in range(3) if m[i] >= 1]
            for A in range(1 << len(supp)):
                sub = [supp[i] for i in range(len(supp)) if (A >> i) & 1]
                mm = msub(m, set(sub))
                sgn = -1 if (pc(A) & 1) else 1
                if max(mm) <= 1:
                    K0[S][T] += sgn * BVAL[mm]
                else:
                    Mj[FIDX[mm]][S][T] += sgn
    return K0, Mj

ORDER = [1, 2, 4, 3, 5, 6, 7]

def reduce_weight(X):
    return [[X[ORDER[i]][ORDER[j]] for j in range(7)] for i in range(7)]

LTAB = {(-1, -1): 10, (-1, 1): 2, (1, -1): 8, (1, 1): 3}

def gate_g5_g6_g7():
    K0, Mj = build_linear_forms()
    W8 = W_matrix(8)
    G0 = reduce_weight(matmul(transpose(W8), matmul(K0, W8)))
    Nj = [reduce_weight(matmul(transpose(W8), matmul(Mj[j], W8)))
          for j in range(19)]
    ok1 = all(Nj[j][i][k] == 0 for j in TOP4 for i in range(6)
              for k in range(6))
    check("G5.top4_cells_absent_from_G6", ok1)
    ok2a = True
    for ai in (-1, 1):
        for aj in (-1, 1):
            for bij in (-1, 1):
                for bji in (-1, 1):
                    for hij in (-1, 1):
                        s = Fraction(-9 + 3 * bij + 3 * bji + hij) \
                            - Fraction((ai + bij) ** 2, 3 + ai) \
                            - Fraction((aj + bji) ** 2, 3 + aj)
                        if not (s < 0 and -s >= LTAB[(ai, bij)]
                                and -s >= LTAB[(aj, bji)]):
                            ok2a = False
    check("G5.diagonal_L_bounds_32_cases", ok2a)
    ok2b = True
    for ai in (-1, 1):
        for bij in (-1, 1):
            for bik in (-1, 1):
                for gi in (-1, 1):
                    s = Fraction(ai + bij + bik + gi) \
                        - Fraction((ai + bij) * (ai + bik), 3 + ai)
                    if s * s > LTAB[(ai, bij)] * LTAB[(ai, bik)]:
                        ok2b = False
    check("G5.coupling_bound_16_cases", ok2b)
    cnt_neg = cnt_zero = cnt_pos = 0
    ok_tri = True
    ok_negmin = True
    degenerate = []
    BASE6 = [[G0[i][j] + sum(Nj[j2][i][j] for j2 in SUB15)
              for j in range(6)] for i in range(6)]
    for bb in range(1 << 15):
        G6 = [row[:] for row in BASE6]
        for idx, j in enumerate(SUB15):
            if (bb >> idx) & 1:
                Njj = Nj[j]
                for i in range(6):
                    for k in range(6):
                        G6[i][k] -= 2 * Njj[i][k]
        d6 = det_bareiss(G6)
        i6 = inertia_sym(G6)
        if d6 < 0:
            cnt_neg += 1
            if i6 != (3, 0, 3):
                ok_tri = False
        elif d6 == 0:
            cnt_zero += 1
            if i6 != (2, 1, 3):
                ok_tri = False
        else:
            cnt_pos += 1
            if i6 != (2, 0, 4):
                ok_tri = False
        if i6[0] < 2:
            ok_negmin = False
        S2 = [[0] * 3 for _ in range(3)]
        for p in range(3):
            for q in range(3):
                v = 4 * G6[3 + p][3 + q]
                for i in range(3):
                    v -= G6[i][3 + p] * G6[i][3 + q] * (4 // G6[i][i])
                S2[p][q] = v
        m01 = S2[0][0] * S2[1][1] - S2[0][1] ** 2
        m02 = S2[0][0] * S2[2][2] - S2[0][2] ** 2
        m12 = S2[1][1] * S2[2][2] - S2[1][2] ** 2
        if m01 < 0 or m02 < 0 or m12 < 0:
            ok_negmin = False
        if m01 == 0 and m02 == 0 and m12 == 0:
            degenerate.append(tuple(tuple(r) for r in S2))
    check("G5.trichotomy_by_det", ok_tri)
    check("G5.pair_schur_minors_nonneg_neg_at_least_2", ok_negmin)
    check("G5.substrate_census_32398_110_260",
          (cnt_neg, cnt_zero, cnt_pos) == (32398, 110, 260))
    okdeg = (len(degenerate) == 1)
    for S2t in degenerate:
        S2m = [list(r) for r in S2t]
        if inertia_sym(S2m) != (2, 0, 1):
            okdeg = False
        if sorted(abs(S2m[p][q]) for p in range(3)
                  for q in range(3)) != [8] * 9:
            okdeg = False
    check("G5.unique_degenerate_configuration", okdeg)
    # full 2^19 sweep
    o002 = [FIDX[tuple(2 if x == i else 0 for x in range(3))]
            for i in range(3)]
    o022 = [FIDX[tuple(0 if x == i else 2 for x in range(3))]
            for i in range(3)]
    o112 = [FIDX[tuple(2 if x == i else 1 for x in range(3))]
            for i in range(3)]
    o122 = [FIDX[tuple(1 if x == i else 2 for x in range(3))]
            for i in range(3)]
    edges = {}
    for i in range(3):
        for j in range(3):
            if i != j:
                k = 3 - i - j
                m = [0, 0, 0]
                m[i] = 1
                m[j] = 2
                m[k] = 0
                edges[(i, j)] = FIDX[tuple(m)]
    o222 = FIDX[(2, 2, 2)]
    eps = [1] * 19
    G = [[G0[i][j] + sum(Nj[jj][i][j] for jj in range(19))
          for j in range(7)] for i in range(7)]
    NST = 1 << 19
    st_neg = st_zero = st_pos = 0
    cls_counts = [0, 0, 0]
    PROFILES = ((4, 0, 4), (4, 1, 3), (5, 0, 3))
    ok_prof = True
    ok_m3 = True
    ok_m4 = True
    ok_m5 = True
    fallback = 0
    fail_in_neg = fail_in_zero_stratum = 0
    qbuckets = {}
    qcollision = False
    sbuckets = {}
    class_of = bytearray(NST)
    b = 0
    i = 0
    while True:
        M = [r[:] for r in G]
        prev = 1
        pivs = []
        okfast = True
        for k in range(7):
            piv = M[k][k]
            if piv == 0:
                okfast = False
                break
            pivs.append(piv)
            if k == 6:
                break
            Mk = M[k]
            for i2 in range(k + 1, 7):
                Mi = M[i2]
                mik = Mi[k]
                for j2 in range(k + 1, 7):
                    Mi[j2] = (Mi[j2] * piv - mik * Mk[j2]) // prev
            prev = piv
        if okfast:
            d6 = pivs[5]
            d7 = pivs[6]
            neg7 = 0
            last = 1
            for d in pivs:
                if (d > 0) != (last > 0):
                    neg7 += 1
                last = d
            ik = (neg7 + 1, 0, 7 - neg7)
        else:
            fallback += 1
            G6b = [row[:6] for row in G[:6]]
            d6 = det_bareiss(G6b)
            C = berkowitz(G)
            d7 = -C[7]
            n7, z7, p7 = inertia_sym(G)
            ik = (n7 + 1, z7, p7)
        detK = -d7
        cl = 0 if detK > 0 else (1 if detK == 0 else 2)
        if ik != PROFILES[cl]:
            ok_prof = False
        cls_counts[cl] += 1
        class_of[b] = cl
        if d6 < 0:
            st_neg += 1
            if cl == 1:
                fail_in_zero_stratum += 1
            if cl == 2:
                fail_in_neg += 1
        elif d6 == 0:
            st_zero += 1
            if cl != 0:
                ok_m4 = False
        else:
            st_pos += 1
            if cl != 0:
                ok_m3 = False
        if cl != 0 and not (d6 < 0 and detK <= 0):
            ok_m5 = False
        val = [(-1 if (b >> j) & 1 else 1) for j in range(19)]
        sums = (val[o002[0]] + val[o002[1]] + val[o002[2]],
                sum(val[edges[e]] for e in edges),
                val[o022[0]] + val[o022[1]] + val[o022[2]],
                val[o112[0]] + val[o112[1]] + val[o112[2]],
                val[o122[0]] + val[o122[1]] + val[o122[2]],
                val[o222])
        got = sbuckets.get(sums)
        if got is None:
            sbuckets[sums] = cl
        elif got != cl and got != 3:
            sbuckets[sums] = 3
        vecs = []
        for orb in (o002, o022, o112, o122):
            x = [val[orb[0]], val[orb[1]], val[orb[2]]]
            s = x[0] + x[1] + x[2]
            vecs.append((3 * x[0] - s, 3 * x[1] - s, 3 * x[2] - s))
        out = [sum(val[edges[(i3, j3)]] for j3 in range(3) if j3 != i3)
               for i3 in range(3)]
        inn = [sum(val[edges[(i3, j3)]] for i3 in range(3) if i3 != j3)
               for j3 in range(3)]
        so = sum(out)
        vecs.append((3 * out[0] - so, 3 * out[1] - so, 3 * out[2] - so))
        vecs.append((3 * inn[0] - so, 3 * inn[1] - so, 3 * inn[2] - so))
        circ = (val[edges[(0, 1)]] + val[edges[(1, 2)]]
                + val[edges[(2, 0)]] - val[edges[(1, 0)]]
                - val[edges[(2, 1)]] - val[edges[(0, 2)]])
        grams = []
        for r in range(6):
            vr = vecs[r]
            for s2 in range(r, 6):
                vs = vecs[s2]
                grams.append(vr[0] * vs[0] + vr[1] * vs[1] + vr[2] * vs[2])
        key = bytes([v + 12 for v in sums]
                    + [(g + 216) // 2 % 256 for g in grams]
                    + [circ * circ // 4])
        got = qbuckets.get(key)
        if got is None:
            qbuckets[key] = cl
        elif got != cl:
            qcollision = True
        i += 1
        if i == NST:
            break
        j = 0
        ii = i
        while (ii & 1) == 0:
            ii >>= 1
            j += 1
        eps[j] = -eps[j]
        b ^= (1 << j)
        twoe = 2 * eps[j]
        Njj = Nj[j]
        for r in range(7):
            Gr = G[r]
            Nr = Njj[r]
            for cix in range(7):
                Gr[cix] += twoe * Nr[cix]
    print("G5 sweep classes pos=%d zero=%d neg=%d fallback=%d" % (
        cls_counts[0], cls_counts[1], cls_counts[2], fallback))
    check("G5.strata_16x_lift",
          (st_neg, st_zero, st_pos) == (518368, 1760, 4160))
    check("G5.classes_522462_51_1775",
          cls_counts == [522462, 51, 1775])
    check("G5.inertia_profiles_404_413_503", ok_prof)
    check("G5.two_scalar_law", ok_m3 and ok_m4 and ok_m5
          and fail_in_neg == 1775 and fail_in_zero_stratum == 51)
    smixed = sum(1 for v in sbuckets.values() if v == 3)
    check("G6.linear_insufficient_3584_buckets_58_mixed",
          len(sbuckets) == 3584 and smixed == 58)
    check("G6.quadratic_sufficient_88352_buckets_0_mixed",
          len(qbuckets) == 88352 and not qcollision)
    perms3 = list(itertools.permutations(range(3)))
    pms = []
    for sigma in perms3:
        pm = [0] * 19
        for j, m in enumerate(FREE):
            mm = tuple(m[sigma[i]] for i in range(3))
            pm[j] = FIDX[mm]
        pms.append(pm)
    cycs = []
    for pm in pms:
        seen = [False] * 19
        ncyc = 0
        for s in range(19):
            if not seen[s]:
                ncyc += 1
                x = s
                while not seen[x]:
                    seen[x] = True
                    x = pm[x]
        cycs.append(ncyc)
    check("G6.cycle_counts", sorted(cycs) == [7, 7, 12, 12, 12, 19])
    burn = (2 ** 19 + 3 * 2 ** 12 + 2 * 2 ** 7) // 6
    seen = bytearray(NST >> 3)
    orbits = 0
    for bb in range(NST):
        if (seen[bb >> 3] >> (bb & 7)) & 1:
            continue
        orbits += 1
        for pm in pms:
            b2 = 0
            for j in range(19):
                if (bb >> j) & 1:
                    b2 |= 1 << pm[j]
            seen[b2 >> 3] |= 1 << (b2 & 7)
    check("G6.burnside_89472_two_paths", burn == 89472 and orbits == 89472)
    check("G6.proper_quotient_gap_1120", 89472 - len(qbuckets) == 1120)

    def sigbits(p, q, r):
        bb2 = 0
        for j, m in enumerate(FREE):
            if t(p ** m[0] * q ** m[1] * r ** m[2]) == -1:
                bb2 |= 1 << j
        return bb2

    def dets_for(bb2):
        Gx = [[G0[i3][j3] + sum(
            (-1 if (bb2 >> jj) & 1 else 1) * Nj[jj][i3][j3]
            for jj in range(19)) for j3 in range(7)] for i3 in range(7)]
        G6b = [row[:6] for row in Gx[:6]]
        d6b = det_bareiss(G6b)
        C = berkowitz(Gx)
        return d6b, C[7]
    ok7 = True
    for (tr, dexp) in (((5, 101, 293), -3840), ((83, 89, 263), -768),
                       ((149, 269, 293), -9856)):
        if not is_extremal_set(list(tr)):
            ok7 = False
        d6b, dK = dets_for(sigbits(*tr))
        print("G7 witness n=%d detG6=%d detK=%d" % (
            tr[0] * tr[1] * tr[2], d6b, dK))
        if not (d6b < 0 and dK == dexp):
            ok7 = False
    for tr in ((3, 23, 71), (17, 139, 163), (29, 101, 113),
               (43, 53, 263), (53, 83, 263)):
        if not is_extremal_set(list(tr)):
            ok7 = False
        d6b, dK = dets_for(sigbits(*tr))
        if not (d6b >= 0 and dK > 0):
            ok7 = False
    check("G7.real_consistency_two_path", ok7)

def main():
    print("P-TM-HANKEL-K3-TRANSFER-1 verify")
    print("INERTIA_ORDER NEG ZERO POS (named fields in every record)")
    print("FREE cell order (code 9m1+3m2+m3): "
          + " ".join("%d%d%d" % m for m in FREE))
    gate_g1()
    gate_g2_g3()
    gate_g4()
    gate_g5_g6_g7()
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
