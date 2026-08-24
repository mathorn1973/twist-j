#!/usr/bin/env python3
# witness_d9_falsifier.py
# Independent verification of the fired D8/D9 falsifier (k = 3 scope) found
# by verify_tm_hankel_xor_defect_4.py (addendum-3 sweep, gate GC).
# This executes the falsifier protocol frozen in
# PREREG-C-TM-HANKEL-XOR-DEFECT-1.md rows D8, D9; it freezes nothing new.
# Python stdlib only. Exact integers and Fractions only. No float.
# Env: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
# INERTIA_ORDER NEG ZERO POS.

import sys
from fractions import Fraction

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

def pdeg(p):
    d = len(p) - 1
    while d > 0 and p[d] == 0:
        d -= 1
    return d

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

def sqfree(p):
    a = [Fraction(v) for v in p]
    b = [Fraction((i + 1) * p[i + 1]) for i in range(len(p) - 1)]
    if not b:
        return p[:]

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
        return p[:]
    x = [Fraction(v) for v in p]
    dy = len(a) - 1
    qout = [Fraction(0)] * (len(x) - dy)
    while len(x) - 1 >= dy:
        dx = len(x) - 1
        f = x[dx] / a[dy]
        qout[dx - dy] = f
        for i in range(dy + 1):
            x[dx - dy + i] -= f * a[i]
        x.pop()
    return primitive(qout)

def deflate_half(q):
    x = [Fraction(v) for v in q]
    qout = [Fraction(0)] * (len(x) - 1)
    while len(x) - 1 >= 1:
        dx = len(x) - 1
        f = x[dx] / 2
        qout[dx - 1] = f
        x[dx - 1] += f
        x.pop()
    assert all(v == 0 for v in x)
    return primitive(qout)

def count01(q, depth=64):
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
        r = count01(qd, depth - 1)
        return None if r is None else 1 + r
    qR = half_right(q)
    a = count01(qL, depth - 1)
    b = count01(qR, depth - 1)
    if a is None or b is None:
        return None
    return a + b

def blocks(P):
    k = len(P)
    M = 1 << k
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        i = lb.bit_length() - 1
        nS[x] = nS[x ^ lb] * P[i]
    K = [[c_general(nS[S] * nS[T], P) for T in range(M)] for S in range(M)]
    Kx = [[c_general(nS[S ^ T], P) for T in range(M)] for S in range(M)]
    R = [[K[S][T] - Kx[S][T] for T in range(M)] for S in range(M)]
    return M, nS, K, Kx, R

def is_extremal(P):
    M, nS = (1 << len(P)), None
    k = len(P)
    M = 1 << k
    nS = [1] * M
    for x in range(1, M):
        lb = x & (-x)
        i = lb.bit_length() - 1
        nS[x] = nS[x ^ lb] * P[i]
    return all(t(nS[x]) == (1 if (pc(x) & 1) else -1) for x in range(M))

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

def main():
    print("D8/D9 falsifier witness verification, k = 3 scope")
    print("INERTIA_ORDER NEG ZERO POS")
    W = [(5, 101, 293), (83, 89, 263), (149, 269, 293)]
    for P in W:
        P = list(P)
        ok_ex = is_extremal(P)
        M, nS, K, Kx, R = blocks(P)
        i1 = inertia_sym(K)
        D = lead_minors(K)
        via_minors = "SINGULAR_OR_ZERO_MINOR" if D is None else str(
            sum(1 for a, bqq in zip([1] + D[:-1], D)
                if (a > 0) != (bqq > 0)))
        detK = det_bareiss(K)
        xs = list(range(M + 1))
        ys = []
        for s in xs:
            A = [[Kx[i][j] + s * R[i][j] for j in range(M)]
                 for i in range(M)]
            ys.append(det_bareiss(A))
        poly = lagrange_int(xs, ys)
        nr = count01(sqfree(poly))
        print("WITNESS P=%s n=%d extremal=%s K NEG=%d ZERO=%d POS=%d "
              "detK=%d minorsNEG=%s pencil_roots_open01=%s p0=%d p1=%d" % (
                  str(P), P[0] * P[1] * P[2], "YES" if ok_ex else "NO",
                  i1[0], i1[1], i1[2], detK, via_minors,
                  str(nr), poly[0], sum(poly)))
    # exhaustive minimal-witness scan, all extremal triples n <= 200000
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
    bad = []
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
            if is_extremal(ps):
                cnt += 1
                M2, nS2, K2, Kx2, R2 = blocks(ps)
                ii = inertia_sym(K2)
                if ii != (4, 0, 4):
                    bad.append((n, ps, ii))
        n += 2
    print("SCAN extremal triples n<=200000: count=%d nonbalanced=%d" % (
        cnt, len(bad)))
    for n, ps, ii in bad:
        print("SCANBAD n=%d P=%s K NEG=%d ZERO=%d POS=%d" % (
            n, str(ps), ii[0], ii[1], ii[2]))
    # direct recount over p<q<r <= 300 without the sweep bitset
    def evil(limit):
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
    ev = evil(300)
    fails = []
    tot = 0
    for a in range(len(ev)):
        for b in range(a + 1, len(ev)):
            for c in range(b + 1, len(ev)):
                p, q, r = ev[a], ev[b], ev[c]
                if (t(p * q) == -1 and t(p * r) == -1 and t(q * r) == -1
                        and t(p * q * r) == 1):
                    tot += 1
                    M2, nS2, K2, Kx2, R2 = blocks([p, q, r])
                    ii = inertia_sym(K2)
                    if ii != (4, 0, 4):
                        fails.append((p, q, r, ii))
    print("RECOUNT triples p<q<r<=300: total=%d fails=%d" % (tot, len(fails)))
    for p, q, r, ii in fails:
        print("RECOUNTFAIL P=[%d,%d,%d] NEG=%d ZERO=%d POS=%d" % (
            p, q, r, ii[0], ii[1], ii[2]))
    print("END")
    return 0

if __name__ == "__main__":
    sys.exit(main())
