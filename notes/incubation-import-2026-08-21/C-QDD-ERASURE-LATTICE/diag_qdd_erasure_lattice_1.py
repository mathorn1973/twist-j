#!/usr/bin/env python3
# C-QDD-ERASURE-LATTICE-1 diagnosis leg for the fired breaker line B4b.
# Post-run analysis with its own identity and hash. It edits nothing frozen.
# Question: which four algebraic members survive the B4b filter
# {+-rho(h) Q_k : h in S_k} cap {admitted, D_k-covariant}, and do they
# equal the E3 member list {+-Q_k, +-(R_k - C_k)}?
# Exact arithmetic only. Python standard library only.

from fractions import Fraction as F
import sys

def mat(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)

def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))

def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def smul(c, A):
    c = F(c)
    return tuple(tuple(c * A[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))

def mT(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def eye(n):
    return tuple(tuple(F(1) if i == j else F(0) for j in range(n))
                 for i in range(n))

def zeros(n, m):
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(n))

def minv(A):
    n = len(A)
    M = [list(A[i]) + [F(1) if i == j else F(0) for j in range(n)]
         for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return tuple(tuple(row[n:]) for row in M)

def pcomp(p, q):
    return tuple(p[q[x]] for x in range(5))

PID = (0, 1, 2, 3, 4)

def all_perms():
    out = []
    def rec(pref, rest):
        if not rest:
            out.append(tuple(pref))
            return
        for i, x in enumerate(rest):
            rec(pref + [x], rest[:i] + rest[i + 1:])
    rec([], [0, 1, 2, 3, 4])
    return sorted(out)

def closure(gens):
    S = {PID}
    S.update(gens)
    frontier = list(S)
    while frontier:
        new = []
        cur = list(S)
        for a in frontier:
            for b in cur:
                for c in (pcomp(a, b), pcomp(b, a)):
                    if c not in S:
                        S.add(c)
                        new.append(c)
        frontier = new
    return frozenset(S)

MJ = mat([[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]])
I4 = eye(4)
D = msub(MJ, I4)
G = msub(I4, smul(F(1, 5), mat([[1] * 4] * 4)))
GINV = minv(G)

def sharp(X):
    return mmul(GINV, mmul(mT(X), G))

def apply(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(4)) for i in range(4))

e0 = (F(1), F(0), F(0), F(0))
U = [e0]
for _ in range(4):
    U.append(apply(D, U[-1]))
B = tuple(tuple(U[j][i] for j in range(4)) for i in range(4))
BINV = minv(B)

def rho(p):
    cols = []
    for x in range(4):
        t = p[x]
        if t < 4:
            c = [F(0)] * 4
            c[t] = F(1)
        else:
            c = [F(-1)] * 4
        cols.append(c)
    Mp = tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
    return mmul(B, mmul(Mp, BINV))

PERMS = all_perms()
RHO = {p: rho(p) for p in PERMS}
K = 2

def mult_perm(a, k):
    return tuple((k + a * (x - k)) % 5 for x in range(5))

Sk = sorted(p for p in PERMS if p[K] == K)
Hk = frozenset(mult_perm(a, K) for a in (1, 2, 3, 4))
o8 = set()
for s in Sk:
    if s in Hk:
        continue
    cl = closure(sorted(Hk) + [s])
    if len(cl) == 8:
        o8.add(cl)
Dk = sorted(next(iter(o8)))
Dk_m = [RHO[p] for p in Dk]
Pk = zeros(4, 4)
for p in Sk:
    Pk = madd(Pk, RHO[p])
Pk = smul(F(1, 24), Pk)
Qk = msub(I4, Pk)
gperm = mult_perm(2, K)
g = RHO[gperm]
Rk = smul(F(1, 4), madd(msub(I4, g), msub(mmul(g, g), mmul(g, mmul(g, g)))))
Ck = msub(Qk, Rk)
Tstar = msub(Rk, Ck)

def admitted(T):
    return (mmul(T, Pk) == zeros(4, 4) and mmul(Pk, T) == zeros(4, 4)
            and mmul(sharp(T), T) == Qk)

def commutes_all(T, mats):
    return all(mmul(T, m) == mmul(m, T) for m in mats)

survivors = []
for h in Sk:
    T = mmul(RHO[h], Qk)
    for sgn, T2 in (("+", T), ("-", smul(-1, T))):
        if admitted(T2) and commutes_all(T2, Dk_m):
            survivors.append((sgn, h, T2))

print("survivors of the B4b filter, with their h labels:")
names = []
for sgn, h, T2 in survivors:
    if T2 == Qk:
        nm = "+Q_k"
    elif T2 == smul(-1, Qk):
        nm = "-Q_k"
    elif T2 == Tstar:
        nm = "+(R_k - C_k)"
    elif T2 == smul(-1, Tstar):
        nm = "-(R_k - C_k)"
    else:
        nm = "UNEXPECTED"
    names.append(nm)
    print("  sign %s  h = %s  ->  %s" % (sgn, h, nm))

gsq = pcomp(gperm, gperm)
central = all(pcomp(gsq, p) == pcomp(p, gsq) for p in Dk)

def cycles(p):
    seen = [False] * 5
    out = []
    for s in range(5):
        if seen[s]:
            continue
        c = [s]
        seen[s] = True
        x = p[s]
        while x != s:
            c.append(x)
            seen[x] = True
            x = p[x]
        out.append(tuple(c))
    return out

ct = sorted(len(c) for c in cycles(gsq))
print("checks:")
print("  survivor count = %d (4 expected after diagnosis)" % len(survivors))
print("  survivor set equals E3 member list {+-Q, +-(R-C)}: %s"
      % (sorted(names) == sorted(["+Q_k", "-Q_k", "+(R_k - C_k)",
                                  "-(R_k - C_k)"])))
print("  g^2 = %s, cycle type %s (double transposition fixing k)" % (gsq, ct))
print("  g^2 central in D_k: %s" % central)
print("  rho(g^2) Q_k == R_k - C_k: %s" % (mmul(RHO[gsq], Qk) == Tstar))
print("  Z(D_k) nontrivial on moving space explains the second class;")
print("  Z(S_k) is trivial, which is why the S rung is unique.")
ok = (len(survivors) == 4
      and sorted(names) == sorted(["+Q_k", "-Q_k", "+(R_k - C_k)",
                                   "-(R_k - C_k)"])
      and central and mmul(RHO[gsq], Qk) == Tstar)
print("DIAGNOSIS: %s" % ("breaker auxiliary expectation was wrong; the four "
      "survivors are exactly the E3 member list; E3 CONFIRMED by the "
      "independent route; no candidate falsifier fires" if ok
      else "UNRESOLVED, candidate STOP"))
sys.exit(0 if ok else 2)
