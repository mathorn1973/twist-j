#!/usr/bin/env python3
"""C-QDD-IDEMPOTENCE-DOMINATES-FORK-1 verifier.

Preregistered in PREREG-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1.md,
sha256 8bec43136964f7375b2382af619a365733645c8f99381e1571bb651fd281650f.
Python standard library only. Fraction and int only. No float anywhere.
Own matrix kernel. No import from any probe directory.
Target comparison is the last gate.
"""
import hashlib
import itertools
import os
import subprocess
import sys
from fractions import Fraction as F

N = 4
CHECKS = []


def check(label, ok):
    CHECKS.append((label, bool(ok)))


def mat(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)


I4 = mat([[1 if i == j else 0 for j in range(N)] for i in range(N)])
Z4 = mat([[0] * N for _ in range(N)])
ONE = mat([[1] * N for _ in range(N)])


def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(N)) for i in range(N))


def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(N)) for i in range(N))


def mscal(c, A):
    return tuple(tuple(F(c) * A[i][j] for j in range(N)) for i in range(N))


def mmul(A, B):
    return tuple(tuple(sum(A[i][t] * B[t][j] for t in range(N)) for j in range(N))
                 for i in range(N))


def mT(A):
    return tuple(tuple(A[j][i] for j in range(N)) for i in range(N))


def mv(A, v):
    return tuple(sum(A[i][t] * v[t] for t in range(N)) for i in range(N))


def mpow(A, n):
    out = I4
    for _ in range(n):
        out = mmul(out, A)
    return out


def solve_nullspace(rows, ncol):
    """Exact reduced row echelon; returns a basis of the null space."""
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = F(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncol)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncol
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -M[i][fc]
        basis.append(tuple(v))
    return basis


def minv(A):
    aug = [list(A[i]) + [F(1) if i == j else F(0) for j in range(N)] for i in range(N)]
    for c in range(N):
        p = next(i for i in range(c, N) if aug[i][c] != 0)
        aug[c], aug[p] = aug[p], aug[c]
        inv = F(1) / aug[c][c]
        aug[c] = [x * inv for x in aug[c]]
        for i in range(N):
            if i != c and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [aug[i][j] - f * aug[c][j] for j in range(2 * N)]
    return tuple(tuple(aug[i][N:]) for i in range(N))


# ---------------------------------------------------------------- CA1 carrier
def step(v):
    a, b, c, d = v
    return (a - c + d, b - c, a, b - c + d)


M_J = tuple(tuple(step(tuple(F(1) if t == j else F(0) for t in range(N)))[i]
                  for j in range(N)) for i in range(N))
probe_vecs = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
              (1, 2, 3, 4), (-2, 5, 0, 7)]
check("CA1-01 M_J reproduces the axiom step map on six probe vectors",
      all(mv(M_J, tuple(F(x) for x in v)) == tuple(F(x) for x in step(v))
          for v in probe_vecs))
D = msub(M_J, I4)
check("CA1-02 D = M_J - I has order five, D^5 = I and D != I", mpow(D, 5) == I4 and D != I4)
G = msub(I4, mscal(F(1, 5), ONE))
check("CA1-03 G inverse is I + one one^T", mmul(G, madd(I4, ONE)) == I4)
check("CA1-04 D is G-orthogonal, D^T G D = G", mmul(mT(D), mmul(G, D)) == G)

u = {}
u[2] = tuple(F(-1) for _ in range(N))
for m in range(1, 5):
    u[(2 + m) % 5] = mv(mpow(D, m), u[2])
check("CA1-05 the five simplex vertices sum to zero",
      tuple(sum(u[x][i] for x in range(5)) for i in range(N)) == tuple(F(0) for _ in range(N)))


def gip(x, y):
    return sum(x[i] * sum(G[i][j] * y[j] for j in range(N)) for i in range(N))


check("CA1-06 Gram is 4/5 on the diagonal and -1/5 off it",
      all(gip(u[x], u[y]) == (F(4, 5) if x == y else F(-1, 5))
          for x in range(5) for y in range(5)))

# ---------------------------------------------------------- CA2 group ceiling
B = tuple(tuple(u[j][i] for j in range(4)) for i in range(N))
Binv = minv(B)


def rho_perm(sigma):
    """Linear map sending u_x to u_{sigma(x)}, sigma a tuple of length five."""
    A = tuple(tuple(u[sigma[j]][i] for j in range(4)) for i in range(N))
    return mmul(A, Binv)


ALLPERM = list(itertools.permutations(range(5)))
RHO_ALL = {s: rho_perm(s) for s in ALLPERM}
check("CA2-01 all 120 vertex permutations are realized, distinct, and G-orthogonal",
      len(set(RHO_ALL.values())) == 120
      and all(mmul(mT(R), mmul(G, R)) == G for R in RHO_ALL.values())
      and all(mv(RHO_ALL[s], u[x]) == u[s[x]] for s in ALLPERM for x in range(5)))

AFF = [tuple((b + c * x) % 5 for x in range(5)) for c in (1, 2, 3, 4) for b in range(5)]
check("CA2-02 the affine set has twenty distinct elements and rho(1,1) = D",
      len(set(AFF)) == 20 and RHO_ALL[tuple((1 + x) % 5 for x in range(5))] == D)


def compose(s, t):
    return tuple(s[t[x]] for x in range(5))


check("CA2-03 the affine set is closed under composition and inverse",
      all(compose(s, t) in set(AFF) for s in AFF for t in AFF)
      and all(tuple(sorted(range(5), key=lambda x: s[x])) in set(AFF) for s in AFF))

gen = {tuple(range(5))}
front = [tuple(range(5))]
seeds = [tuple((1 + x) % 5 for x in range(5)), tuple((2 * x) % 5 for x in range(5))]
while front:
    a = front.pop()
    for g in seeds:
        b = compose(g, a)
        if b not in gen:
            gen.add(b)
            front.append(b)
check("CA2-04 the group generated by the J-step and the doubling map is exactly "
      "the twenty affine maps, so the dynamically realized relabelings are 20 of 120",
      gen == set(AFF))


def fixed(s):
    return sum(1 for x in range(5) if s[x] == x)


TRANSP = [s for s in ALLPERM if fixed(s) == 3]
check("CA2-05 fixed-label certificate: every non-identity affine map fixes at most one "
      "label, every transposition fixes exactly three, so no transposition is affine",
      all(fixed(s) <= 1 for s in AFF if s != tuple(range(5)))
      and len(TRANSP) == 10 and all(fixed(s) == 3 for s in TRANSP)
      and not (set(TRANSP) & set(AFF)))

# --------------------------------------------------------------- CA3 stabilizers
STAB = {k: [s for s in ALLPERM if s[k] == k] for k in range(5)}
HSTAB = {k: [s for s in AFF if s[k] == k] for k in range(5)}
check("CA3-01 complete record stabilizer of order 24, affine stabilizer of order 4",
      all(len(STAB[k]) == 24 and len(HSTAB[k]) == 4 for k in range(5)))
check("CA3-02 the complete stabilizer meets the affine group exactly in the affine "
      "stabilizer, index six",
      all(set(STAB[k]) & set(AFF) == set(HSTAB[k]) and 24 // len(HSTAB[k]) == 6
          for k in range(5)))

P, Q, g, R, C, Jm = {}, {}, {}, {}, {}, {}
for k in range(5):
    acc = Z4
    for h in HSTAB[k]:
        acc = madd(acc, RHO_ALL[h])
    P[k] = mscal(F(1, 4), acc)
    Q[k] = msub(I4, P[k])
    g[k] = RHO_ALL[tuple((2 * (x - k) + k) % 5 for x in range(5))]
    R[k] = mscal(F(1, 4), madd(msub(I4, g[k]), msub(mpow(g[k], 2), mpow(g[k], 3))))
    C[k] = msub(Q[k], R[k])
    Jm[k] = mmul(g[k], C[k])


def rank(A):
    return N - len(solve_nullspace([list(r) for r in A], N))


def sharp(A):
    return mmul(madd(I4, ONE), mmul(mT(A), G))


check("CA3-03 P_k rank one self-sharp idempotent fixing u_k; Q_k rank three "
      "self-sharp idempotent; P_k Q_k = 0",
      all(mmul(P[k], P[k]) == P[k] and sharp(P[k]) == P[k] and rank(P[k]) == 1
          and mv(P[k], u[k]) == u[k] and mmul(Q[k], Q[k]) == Q[k]
          and sharp(Q[k]) == Q[k] and rank(Q[k]) == 3 and mmul(P[k], Q[k]) == Z4
          for k in range(5)))
check("CA3-04 g_k has order four; R, C, J are the declared pieces with "
      "R + C = Q, J^2 = -C, J^sharp = -J, ranks 1 and 2",
      all(mpow(g[k], 4) == I4 and mpow(g[k], 2) != I4
          and madd(R[k], C[k]) == Q[k] and mmul(Jm[k], Jm[k]) == mscal(-1, C[k])
          and sharp(Jm[k]) == mscal(-1, Jm[k]) and rank(R[k]) == 1
          and rank(C[k]) == 2 and mmul(R[k], C[k]) == Z4 for k in range(5)))


def centralizer_basis(k, group):
    rows = []
    for i in range(N):
        for j in range(N):
            e = [F(0)] * 16
            e[i * N + j] = F(1)
            for a in range(N):
                for b in range(N):
                    e[a * N + b] -= Q[k][i][a] * Q[k][b][j]
            rows.append(e)
    for h in group:
        Rh = RHO_ALL[h]
        for i in range(N):
            for j in range(N):
                e = [F(0)] * 16
                for t in range(N):
                    e[i * N + t] += Rh[t][j]
                    e[t * N + j] -= Rh[i][t]
                rows.append(e)
    return solve_nullspace(rows, 16)


cs4 = {k: centralizer_basis(k, STAB[k]) for k in range(5)}
cc4 = {k: centralizer_basis(k, HSTAB[k]) for k in range(5)}
def prop(vec, M):
    """True if the 16-vector vec is a nonzero rational multiple of matrix M."""
    a = [M[i][j] for i in range(N) for j in range(N)]
    nz = next((t for t in range(16) if a[t] != 0), None)
    if nz is None or vec[nz] == 0:
        return False
    lam = vec[nz] / a[nz]
    return all(vec[t] == lam * a[t] for t in range(16))


check("CA4-01 the moving-support centralizer of the complete record stabilizer has "
      "dimension exactly one at every token, spanned by Q_k",
      all(len(cs4[k]) == 1 and prop(cs4[k][0], Q[k]) for k in range(5)))
check("CA4-02 the moving-support centralizer of the affine stabilizer has dimension "
      "exactly three at every token, with R, C, J a basis",
      all(len(cc4[k]) == 3 for k in range(5))
      and all(len(solve_nullspace(
          [[R[k][i][j], C[k][i][j], Jm[k][i][j]] for i in range(N) for j in range(N)],
          3)) == 0 for k in range(5))
      and all(all(mmul(X, RHO_ALL[h]) == mmul(RHO_ALL[h], X)
                  for h in HSTAB[k] for X in (R[k], C[k], Jm[k])) for k in range(5)))

# ------------------------------------------------------- CA5 the main statement
NORM = {}
for k in range(5):
    NORM[k] = [mscal(eps, mmul(RHO_ALL[h], Q[k])) for h in STAB[k] for eps in (1, -1)]
check("CA5-01 the record normalizer has 48 distinct members and 24 sign classes at "
      "every token",
      all(len(set(NORM[k])) == 48 for k in range(5))
      and all(len(set(frozenset((T, mscal(-1, T))) for T in NORM[k])) == 24
              for k in range(5)))
check("CA5-02 every normalizer member satisfies the effect equation T^sharp T = Q_k, "
      "ordinary repeatability Q_k T = T, Kraus completeness and zero cross term",
      all(mmul(sharp(T), T) == Q[k] and mmul(Q[k], T) == T
          and madd(mmul(sharp(P[k]), P[k]), mmul(sharp(T), T)) == I4
          and mmul(sharp(P[k]), T) == Z4 for k in range(5) for T in NORM[k]))
surv = {}
for k in range(5):
    surv[k] = [T for T in NORM[k] if mmul(T, T) == T or mmul(T, T) == mscal(-1, T)]
check("CA5-03 MAIN, exhaustive over all 48 members at all five tokens: class level "
      "idempotence T^2 = +-T holds exactly at T = +Q_k and T = -Q_k and fails at the "
      "other 46 members",
      all(sorted(surv[k]) == sorted([Q[k], mscal(-1, Q[k])]) for k in range(5)))
check("CA5-04 the elementwise reason: rho(h) Q_k = +-Q_k holds only at h = identity, "
      "so the standard three dimensional module is faithful and carries no -identity",
      all(sum(1 for h in STAB[k]
              if mmul(RHO_ALL[h], Q[k]) in (Q[k], mscal(-1, Q[k]))) == 1
          for k in range(5)))
tau = {}
for k in range(5):
    other = [x for x in range(5) if x != k]
    s = list(range(5))
    s[other[0]], s[other[1]] = other[1], other[0]
    tau[k] = tuple(s)
check("CA5-05 the fork breaker is exactly of the killed type: T_tau = rho(tau) Q_k is "
      "involutive with T_tau^2 = Q_k, is not +-Q_k, and fails class level idempotence; "
      "tau commutes with exactly 4 of the 24 stabilizer elements",
      all((lambda T: mmul(T, T) == Q[k] and T != Q[k] and T != mscal(-1, Q[k])
           and mmul(T, T) != T and mmul(T, T) != mscal(-1, T))(mmul(RHO_ALL[tau[k]], Q[k]))
          and sum(1 for h in STAB[k]
                  if compose(tau[k], h) == compose(h, tau[k])) == 4
          for k in range(5)))
check("CA5-06 the breaker is not a J-motion: tau is not affine at any token, so no "
      "plenum motion implements the relabeling it encodes",
      all(tau[k] not in set(AFF) for k in range(5)))

# ------------------------------------------------- CA6 the enlarged fork family
TLIST = [F(0), F(1), F(-1), F(1, 2), F(-2), F(3), F(1, 3), F(-1, 5), F(7, 2)]
CIRCLE = [((1 - t * t) / (1 + t * t), (2 * t) / (1 + t * t)) for t in TLIST]
check("CA6-01 the frozen circle list is exact and on the rational unit circle",
      all(r * r + s * s == 1 for (r, s) in CIRCLE) and len(set(CIRCLE)) == len(TLIST))
enl_surv = {}
for k in range(5):
    fam = []
    for h in STAB[k]:
        for e in (1, -1):
            for (r, s) in CIRCLE:
                X = madd(mscal(e, R[k]), madd(mscal(r, C[k]), mscal(s, Jm[k])))
                fam.append((h, e, r, s, mmul(RHO_ALL[h], X)))
    check_eff = all(mmul(sharp(T), T) == Q[k] for (_, _, _, _, T) in fam)
    enl_surv[k] = [(h, e, r, s) for (h, e, r, s, T) in fam
                   if mmul(T, T) == T or mmul(T, T) == mscal(-1, T)]
    if not check_eff:
        enl_surv[k] = None
ident = tuple(range(5))
check("CA6-02 every member of the enlarged family rho(h) X satisfies the effect "
      "equation, and class level idempotence holds exactly at h = identity with "
      "X = +Q_k or X = -Q_k",
      all(enl_surv[k] is not None
          and sorted(enl_surv[k]) == sorted([(ident, 1, F(1), F(0)),
                                             (ident, -1, F(-1), F(0))])
          for k in range(5)))

# ------------------------------------------------ CA8 reproduction of the sealed
REPO = os.getcwd()
SEALED = ["P-QDD-J-CENTRALIZER-TERMINALITY-1",
          "P-QDD-RECORD-COMPLETE-STABILIZER-1",
          "P-QDD-RECORD-NATURALITY-FORK-1"]
env = dict(os.environ)
env.update({"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0", "TZ": "UTC"})
repro = True
for name in SEALED:
    with open(os.path.join(REPO, "probes", name, "EXPECTED.txt"), "rb") as fh:
        exp = fh.read()
    pr = subprocess.run([sys.executable, os.path.join("probes", name, "verify.py")],
                        cwd=REPO, env=env, capture_output=True, timeout=100)
    repro = repro and pr.returncode == 0 and pr.stderr == b"" and pr.stdout == exp
check("CA8-01 all three sealed QDD verifiers reproduce byte-identically from "
      "repository root, exit zero, empty stderr", repro)

# ------------------------------------------------------- CA9 target, deliberately last
E_low = mscal(F(1, 4), ONE)
E_high = msub(I4, E_low)
check("CA9-01 target comparison last: P_2 = E_low and Q_2 = E_high, so the class that "
      "survives in both fork branches is the Lueder class", P[2] == E_low and Q[2] == E_high)

fails = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        fails += 1
print("RESULT %d/%d PASS" % (len(CHECKS) - fails, len(CHECKS)))
sys.exit(1 if fails else 0)
