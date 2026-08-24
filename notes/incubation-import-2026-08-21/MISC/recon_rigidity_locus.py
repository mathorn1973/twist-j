#!/usr/bin/env python3
# recon_rigidity_locus.py
# RECON, NON-FORMAL. After the L1 firing in verify_tm_hankel_xor_defect_5:
# cross-tabulate six-direction rigidity against the det class over all
# 2^19 abstract tables, and test rigidity on the REAL extremal triples.
# Exact integers only.

import sys

def pc(x):
    return bin(x).count("1")

def t(n):
    return -1 if (pc(n) & 1) else 1

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
    return (neg, z, pos)

def matmul(A, B):
    n = len(A)
    m = len(B[0])
    l = len(B)
    return [[sum(A[i][x] * B[x][j] for x in range(l)) for j in range(m)]
            for i in range(n)]

def transpose(A):
    return [list(r) for r in zip(*A)]

def code(m):
    return 9 * m[0] + 3 * m[1] + m[2]

ALLM = sorted([(a, b, c) for a in range(3) for b in range(3)
               for c in range(3)], key=code)
FREE = [m for m in ALLM if max(m) == 2]
BINARY = [m for m in ALLM if max(m) <= 1]
FIDX = {m: j for j, m in enumerate(FREE)}
BVAL = {m: (1 if ((m[0] + m[1] + m[2]) & 1) else -1) for m in BINARY}

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

def W_matrix(M):
    return [[(1 << (pc(T) - pc(S))) if (S & T) == S else 0
             for T in range(M)] for S in range(M)]

ORDER = [1, 2, 4, 3, 5, 6, 7]

def reduce_weight(X):
    return [[X[ORDER[i]][ORDER[j]] for j in range(7)] for i in range(7)]

def g6_rigid_and_det(G):
    M = [r[:] for r in G]
    prev = 1
    D = []
    okpat = True
    for k in range(7):
        piv = M[k][k]
        if k < 6 and piv == 0:
            okpat = False
            break
        D.append(piv)
        if k == 6:
            break
        Mk = M[k]
        for i in range(k + 1, 7):
            Mi = M[i]
            mik = Mi[k]
            for j in range(k + 1, 7):
                Mi[j] = (Mi[j] * piv - mik * Mk[j]) // prev
        prev = piv
    if okpat and len(D) == 7:
        d1, d2, d3, d4, d5, d6, d7 = D
        if d1 > 0 and d2 > 0 and d3 > 0 and d4 < 0 and d5 > 0 and d6 < 0:
            return True, -d7
    G6 = [row[:6] for row in G[:6]]
    i6 = inertia_sym(G6)
    C = berkowitz(G)
    detG = -C[7]
    return (i6 == (3, 0, 3)), -detG

def main():
    K0, Mj = build_linear_forms()
    W8 = W_matrix(8)
    G0 = reduce_weight(matmul(transpose(W8), matmul(K0, W8)))
    Nj = [reduce_weight(matmul(transpose(W8), matmul(Mj[j], W8)))
          for j in range(19)]
    eps = [1] * 19
    G = [[G0[i][j] + sum(Nj[jj][i][j] for jj in range(19))
          for j in range(7)] for i in range(7)]
    NST = 1 << 19
    tab = {}
    nonrigid_hist = {}
    b = 0
    i = 0
    while True:
        rigid, detK = g6_rigid_and_det(G)
        cl = 0 if detK > 0 else (1 if detK == 0 else 2)
        key = (rigid, cl)
        tab[key] = tab.get(key, 0) + 1
        if not rigid:
            G6 = [row[:6] for row in G[:6]]
            i6 = inertia_sym(G6)
            nonrigid_hist[i6] = nonrigid_hist.get(i6, 0) + 1
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
    print("RECON rigidity locus, INERTIA NEG ZERO POS, class 0 pos 1 zero 2 neg")
    for key in sorted(tab):
        print("CROSSTAB rigid=%s class=%d count=%d" % (
            "YES" if key[0] else "NO", key[1], tab[key]))
    for i6 in sorted(nonrigid_hist):
        print("NONRIGID G6 NEG=%d ZERO=%d POS=%d count=%d" % (
            i6[0], i6[1], i6[2], nonrigid_hist[i6]))
    # real triples p<q<r <= 300
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
    tot = 0
    nonrigid_real = []
    for a in range(len(ev)):
        for bq in range(a + 1, len(ev)):
            for cr in range(bq + 1, len(ev)):
                p, q, r = ev[a], ev[bq], ev[cr]
                if not (t(p * q) == -1 and t(p * r) == -1
                        and t(q * r) == -1 and t(p * q * r) == 1):
                    continue
                tot += 1
                bb = 0
                for j, m in enumerate(FREE):
                    if t(p ** m[0] * q ** m[1] * r ** m[2]) == -1:
                        bb |= 1 << j
                Gx = [[G0[i2][j2] + sum(
                    (-1 if (bb >> jj) & 1 else 1) * Nj[jj][i2][j2]
                    for jj in range(19)) for j2 in range(7)]
                    for i2 in range(7)]
                rigid, detK = g6_rigid_and_det(Gx)
                if not rigid:
                    G6 = [row[:6] for row in Gx[:6]]
                    nonrigid_real.append((p, q, r, inertia_sym(G6), detK))
    print("REAL triples p<q<r<=300: total=%d nonrigid=%d" % (
        tot, len(nonrigid_real)))
    for p, q, r, i6, detK in nonrigid_real:
        print("REALNONRIGID P=[%d,%d,%d] G6 NEG=%d ZERO=%d POS=%d detK=%d" % (
            p, q, r, i6[0], i6[1], i6[2], detK))
    print("RECON END")
    return 0

if __name__ == "__main__":
    sys.exit(main())
