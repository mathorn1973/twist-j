#!/usr/bin/env python3
# recon_outlier_autopsy.py
# RECON, NON-FORMAL. Autopsy of the (dNEG,dPOS) = (-3,0) transfer outliers
# from the k=2 pool of recon_hankel_xor_defect.py. Exact integers only.

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
    return M, nS, K, Kx

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
print("RECON outlier autopsy, k=2 pool, shift = (dNEG, dPOS) named explicitly")
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p, q = primes[i], primes[j]
        M, nS, K, Kx = blocks([p, q])
        iK = inertia_sym(K)
        iKx = inertia_sym(Kx)
        dneg = iK[0] - iKx[0]
        dpos = iK[2] - iKx[2]
        if (dneg, dpos) == (-3, 0):
            print("OUTLIER pair p=%d q=%d n=%d" % (p, q, p * q))
            print("  letters t(p)=%d t(q)=%d t(pq)=%d  "
                  "t(p2)=%d t(q2)=%d t(p2q)=%d t(pq2)=%d t(p2q2)=%d" % (
                      t(p), t(q), t(p * q), t(p * p), t(q * q),
                      t(p * p * q), t(p * q * q), t(p * p * q * q)))
            print("  K    NEG=%d ZERO=%d POS=%d" % iK)
            print("  Kxor NEG=%d ZERO=%d POS=%d" % iKx)
            # extremal conditions: t(p)=+1, t(q)=+1, t(pq)=-1
            fails = []
            if t(p) != 1:
                fails.append("t(p)=+1")
            if t(q) != 1:
                fails.append("t(q)=+1")
            if t(p * q) != -1:
                fails.append("t(pq)=-1")
            print("  extremal conditions violated: %s" % ", ".join(fails))
            # first Y=empty cancellation failure: for S != T with I nonempty
            # or diagonal backbone mismatch; scan the closed t-form Y=0 term
            first = None
            for S in range(M):
                for T in range(M):
                    I = S & T
                    D = S ^ T
                    s0 = 0
                    X = D
                    while True:
                        s0 += t(nS[I] * nS[X])
                        if X == 0:
                            break
                        X = (X - 1) & D
                    want = 0
                    if S == T:
                        want = (3 ** pc(S)) if (pc(S) & 1) else -(3 ** pc(S))
                        want //= 3 ** pc(S)
                        want *= 1
                        # backbone contribution of Y=0 at S=T is
                        # (-1)^(|S|+1), before the 3^|S| weight
                    if s0 != ((1 if (pc(S) & 1) else -1) if S == T else 0):
                        if first is None:
                            first = (S, T, s0)
            if first is not None:
                S, T, s0 = first
                print("  first Y=empty cancellation failure at (S,T)="
                      "(%d,%d) I=%d D=%d: sum_X t(n_I n_X) = %d" % (
                          S, T, S & T, S ^ T, s0))
            else:
                print("  Y=empty term behaves extremally everywhere")
print("RECON END")
