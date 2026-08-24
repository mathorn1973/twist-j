#!/usr/bin/env python3
# C-QDD-ERASURE-LATTICE-1 breaker. Candidate lane, no authority.
# Independent attack pass: different algorithms than the verifier.
#   B1 full subgroup lattice of S_k by BFS closure (all subgroups, not
#      only 2-generated), then the containment filter.
#   B2 centralizer dimensions by exact group-averaging projector ranks.
#   B3 motor emptiness on the 4-dimensional polynomial parametrization.
#   B4 direct searches for laws that would refute the rung class lists.
#   B5 full ladder recompute at a second token by the averaging method.
# Exact arithmetic only. Python standard library only. No fail-fast.

from fractions import Fraction as F
import sys

FINDINGS = []

def report(name, broken, note=""):
    tag = "BREAK" if broken else "HOLDS"
    if broken:
        FINDINGS.append(name)
    print("%s %s%s" % (name, tag, (" " + note) if note else ""))

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

def rank_rows(rows):
    R = [list(r) for r in rows]
    if not R:
        return 0
    m = len(R[0])
    rank = 0
    row = 0
    for col in range(m):
        piv = None
        for r in range(row, len(R)):
            if R[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        R[row], R[piv] = R[piv], R[row]
        pv = R[row][col]
        R[row] = [x / pv for x in R[row]]
        for r in range(len(R)):
            if r != row and R[r][col] != 0:
                f = R[r][col]
                R[r] = [a - f * b for a, b in zip(R[r], R[row])]
        row += 1
        rank += 1
    return rank

def flat(A):
    return tuple(A[i][j] for i in range(len(A)) for j in range(len(A[0])))

# permutations
def pcomp(p, q):
    return tuple(p[q[x]] for x in range(5))

def pinv(p):
    r = [0] * 5
    for x in range(5):
        r[p[x]] = x
    return tuple(r)

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

# frozen objects, rebuilt
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
cyc = (1, 2, 3, 4, 0)

def mult_perm(a, k):
    return tuple((k + a * (x - k)) % 5 for x in range(5))

# ---------- B1 full subgroup lattice of S_k ----------

K = 2
Sk = sorted(p for p in PERMS if p[K] == K)
SkSet = frozenset(Sk)
subgroups = set()
frontier = [frozenset([PID])]
subgroups.add(frozenset([PID]))
while frontier:
    nxt = []
    for Ssub in frontier:
        for x in Sk:
            if x in Ssub:
                continue
            cl = closure(sorted(Ssub) + [x])
            if cl <= SkSet and cl not in subgroups:
                subgroups.add(cl)
                nxt.append(cl)
    frontier = nxt
report("B1a-subgroup-census-of-S4", len(subgroups) != 30,
       "found %d subgroups (expected 30)" % len(subgroups))
Hk = frozenset(mult_perm(a, K) for a in (1, 2, 3, 4))
containing = sorted((len(s) for s in subgroups if Hk <= s))
report("B1b-containment-filter", containing != [4, 8, 24],
       "orders over H_k: %s (expected [4, 8, 24])" % containing)
Dk = next(s for s in subgroups if Hk <= s and len(s) == 8)

# ---------- B2 averaging-projector ranks ----------

EIJ = []
for i in range(4):
    for j in range(4):
        Z = [[F(0)] * 4 for _ in range(4)]
        Z[i][j] = F(1)
        EIJ.append(mat(Z))

def avg_map_rank(mats, compress=None):
    n = len(mats)
    invs = [minv(m) for m in mats]
    rows = []
    for Bv in EIJ:
        acc = zeros(4, 4)
        for m, mi in zip(mats, invs):
            acc = madd(acc, mmul(m, mmul(Bv, mi)))
        acc = smul(F(1, n), acc)
        if compress is not None:
            acc = mmul(compress, mmul(acc, compress))
        rows.append(flat(acc))
    return rank_rows(rows)

Sk_m = [RHO[p] for p in Sk]
Hk_m = [RHO[p] for p in sorted(Hk)]
Dk_m = [RHO[p] for p in sorted(Dk)]
Pk = zeros(4, 4)
for m in Sk_m:
    Pk = madd(Pk, m)
Pk = smul(F(1, 24), Pk)
Qk = msub(I4, Pk)
full_dims = (avg_map_rank(Hk_m), avg_map_rank(Dk_m), avg_map_rank(Sk_m))
report("B2a-full-commutant-dims", full_dims != (4, 3, 2),
       "End(V) dims %s (expected (4, 3, 2))" % (full_dims,))
mov_dims = (avg_map_rank(Hk_m, Qk), avg_map_rank(Dk_m, Qk),
            avg_map_rank(Sk_m, Qk))
report("B2b-moving-space-dims", mov_dims != (3, 2, 1),
       "Q_kV dims %s (expected (3, 2, 1))" % (mov_dims,))
C5_m = [RHO[p] for p in sorted(closure([cyc]))]
S5_m = [RHO[p] for p in PERMS]
big_dims = (avg_map_rank(C5_m), avg_map_rank(S5_m))
report("B2c-C5-and-S5-commutants", big_dims != (4, 1),
       "dims %s (expected (4, 1))" % (big_dims,))

# ---------- B3 motor emptiness, polynomial route ----------

D2 = mmul(D, D)
D3 = mmul(D2, D)
pows = [I4, D, D2, D3]
rows = []
for P in pows:
    rows.append(flat(mmul(P, Pk)))
r = rank_rows(rows)
# solutions a with sum a_i (D^i P_k) = 0 form a space of dim 4 - r
report("B3a-motor-annihilator-dim", (4 - r) != 0,
       "solution dim %d (expected 0)" % (4 - r))
# a direct attempted witness: the field trick, (sum a_i D^i) u_K = 0 needs
# a nonzero polynomial in D killing a nonzero vector; try all monomials
mono_break = False
for P in pows:
    if apply(P, U[K]) == (F(0),) * 4:
        mono_break = True
report("B3b-monomial-kill-attempt", mono_break)

# ---------- B4 rung class searches ----------

gperm = mult_perm(2, K)
g = RHO[gperm]
Rk = smul(F(1, 4), madd(msub(I4, g), msub(mmul(g, g), mmul(g, mmul(g, g)))))
Ck = msub(Qk, Rk)
Jk = mmul(g, Ck)

def admitted(T):
    return (mmul(T, Pk) == zeros(4, 4) and mmul(Pk, T) == zeros(4, 4)
            and mmul(sharp(T), T) == Qk)

def commutes_all(T, mats):
    return all(mmul(T, m) == mmul(m, T) for m in mats)

# B4a: circle members with s != 0 must fail D_k covariance
b4a = False
for t in (F(1), F(1, 2), F(1, 3), F(2, 3), F(3, 4)):
    r = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    T = madd(smul(F(1), Rk), madd(smul(r, Ck), smul(s, Jk)))
    if not admitted(T):
        b4a = True
    if commutes_all(T, Dk_m):
        b4a = True
report("B4a-circle-points-fail-Dk", b4a)

# B4b: the 48-member normalizer family rho(h) Q_k, h in S_k, +-:
# which are D_k covariant AND admitted? expect exactly +-Q_k
survivors = []
for h in Sk:
    T = mmul(RHO[h], Qk)
    for T2 in (T, smul(-1, T)):
        if admitted(T2) and commutes_all(T2, Dk_m):
            survivors.append(T2)
uniq = []
for T in survivors:
    if not any(T == X for X in uniq):
        uniq.append(T)
report("B4b-normalizer-family-Dk-filter",
       sorted(flat(x) for x in uniq) != sorted([flat(Qk), flat(smul(-1, Qk))]),
       "survivors %d algebraic (expected 2: +Q, -Q)" % len(uniq))

# B4c: brute search for an admitted D_k-covariant law outside the four:
# solve the covariance space directly by averaging image basis
def avg_image_basis(mats, compress):
    invs = [minv(m) for m in mats]
    imgs = []
    for Bv in EIJ:
        acc = zeros(4, 4)
        for m, mi in zip(mats, invs):
            acc = madd(acc, mmul(m, mmul(Bv, mi)))
        acc = smul(F(1, len(mats)), acc)
        acc = mmul(compress, mmul(acc, compress))
        imgs.append(acc)
    basis = []
    rows = []
    for A in imgs:
        cand = rows + [flat(A)]
        if rank_rows(cand) > len(rows):
            rows.append(flat(A))
            basis.append(A)
    return basis

bD = avg_image_basis(Dk_m, Qk)
b4c = len(bD) != 2
# with basis {X1, X2}, T = x X1 + y X2; check that the admitted set maps
# bijectively onto {+-Q, +-(R-C)} by comparing against the four directly:
four = [madd(smul(r, Rk), smul(c, Ck)) for r in (F(1), F(-1))
        for c in (F(1), F(-1))]
span_rows = [flat(x) for x in bD]
for T in four:
    if rank_rows(span_rows + [flat(T)]) != len(span_rows):
        b4c = True  # four not inside the averaged span: contradiction
report("B4c-Dk-covariant-space-vs-four", b4c,
       "avg image dim %d (expected 2), four members inside" % len(bD))

# B4d: S rung by averaging: image dim must be 1 and contain Q_k
bS = avg_image_basis(Sk_m, Qk)
b4d = len(bS) != 1 or rank_rows([flat(bS[0]), flat(Qk)]) != 1
report("B4d-S-covariant-space-dim-1-Qline", b4d)

# ---------- B5 second token, kk = 4, averaging method ----------

KK = 4
Sk2 = sorted(p for p in PERMS if p[KK] == KK)
Hk2 = frozenset(mult_perm(a, KK) for a in (1, 2, 3, 4))
o8 = set()
for s in Sk2:
    if s in Hk2:
        continue
    cl = closure(sorted(Hk2) + [s])
    if len(cl) == 8:
        o8.add(cl)
b5_lattice = len(o8) != 1
Dk2 = next(iter(o8)) if len(o8) == 1 else None
P2 = zeros(4, 4)
for p in Sk2:
    P2 = madd(P2, RHO[p])
P2 = smul(F(1, 24), P2)
Q2 = msub(I4, P2)
d2 = (avg_map_rank([RHO[p] for p in sorted(Hk2)], Q2),
      avg_map_rank([RHO[p] for p in sorted(Dk2)], Q2) if Dk2 else -1,
      avg_map_rank([RHO[p] for p in Sk2], Q2))
report("B5-second-token-ladder", b5_lattice or d2 != (3, 2, 1),
       "token 4 dims %s (expected (3, 2, 1))" % (d2,))

# ---------- summary ----------

print("FINDINGS %d of 10" % len(FINDINGS))
if FINDINGS:
    print("BROKEN: " + ", ".join(FINDINGS))
    sys.exit(2)
print("BREAKER VERDICT: no break found; E1-E5 withstand the independent pass")
sys.exit(0)
