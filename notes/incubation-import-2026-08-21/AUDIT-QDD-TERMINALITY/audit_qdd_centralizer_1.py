#!/usr/bin/env python3
"""audit_qdd_centralizer_1.py

Independent audit of P-QDD-J-CENTRALIZER-TERMINALITY-1 per
PREREG-AUDIT-QDD-TERMINALITY-1 (sha256
d479d89927fa3b42cb48b6f009158bda5469bb6064bf666f46950f001b9a21d0).

Fresh implementation: own Fraction matrix kernel, nothing imported from the
probe directory. The simplex, affine action, stabilizer averages, centralizer,
routes, and target comparison are rebuilt from the axiom step map alone.
Target effects are compared LAST. No float is formed anywhere.
"""

from fractions import Fraction as F
import hashlib
import os
import subprocess
import sys

CHECKS = []


def check(label, cond):
    CHECKS.append((label, bool(cond)))


# ---------------------------------------------------------------------------
# Fraction matrix kernel
# ---------------------------------------------------------------------------

def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def mmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4))
                 for i in range(4))


def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(4)) for i in range(4))


def msub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(4)) for i in range(4))


def mscal(c, A):
    c = F(c)
    return tuple(tuple(c * A[i][j] for j in range(4)) for i in range(4))


def mT(A):
    return tuple(tuple(A[j][i] for j in range(4)) for i in range(4))


def mpow(A, e):
    R = I4
    B = A
    while e:
        if e & 1:
            R = mmul(R, B)
        B = mmul(B, B)
        e >>= 1
    return R


def mv(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) for i in range(4))


def vadd(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def vscal(c, a):
    c = F(c)
    return tuple(c * a[i] for i in range(4))


def trace(A):
    return sum(A[i][i] for i in range(4))


def minv(A):
    # Gauss-Jordan over Fractions
    n = 4
    M = [list(A[i]) + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(2 * n)]
    return tuple(tuple(M[i][n:]) for i in range(n))


def rank(rows):
    rows = [list(r) for r in rows]
    n = len(rows)
    m = len(rows[0]) if rows else 0
    rk = 0
    col = 0
    while rk < n and col < m:
        piv = next((r for r in range(rk, n) if rows[r][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][col]
        rows[rk] = [x / pv for x in rows[rk]]
        for r in range(n):
            if r != rk and rows[r][col] != 0:
                f = rows[r][col]
                rows[r] = [rows[r][j] - f * rows[rk][j] for j in range(m)]
        rk += 1
        col += 1
    return rk


I4 = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
Z4 = mat([[0] * 4] * 4)
ONEC = (F(1), F(1), F(1), F(1))

# ---------------------------------------------------------------------------
# QA1: phase motor and simplex from the axiom step
# ---------------------------------------------------------------------------

M_J = mat([[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]])


def axiom_step(v):
    a, b, c, d = v
    return (a - c + d, b - c, a, b - c + d)


basis_probe = [(F(1), F(0), F(0), F(0)), (F(0), F(1), F(0), F(0)),
               (F(0), F(0), F(1), F(0)), (F(0), F(0), F(0), F(1)),
               (F(1), F(2), F(3), F(4)), (F(2), F(-1), F(0), F(5))]
check("Q1-01 M_J equals the axiom step map on six probe vectors",
      all(mv(M_J, v) == axiom_step(v) for v in basis_probe))

D = msub(M_J, I4)
check("Q1-02 D^5 = I", mpow(D, 5) == I4)

E11 = mat([[1] * 4] * 4)
G = msub(I4, mscal(F(1, 5), E11))
GINV = madd(I4, E11)
check("Q1-03 G inverse is I + one one^T", mmul(G, GINV) == I4)
check("Q1-04 D^T G D = G", mmul(mT(D), mmul(G, D)) == G)


def sharp(A):
    return mmul(GINV, mmul(mT(A), G))


e0 = (F(1), F(0), F(0), F(0))
u = [e0]
for _ in range(4):
    u.append(mv(D, u[-1]))

check("Q1-05 simplex sum is zero",
      vadd(vadd(u[0], u[1]), vadd(u[2], vadd(u[3], u[4]))) == (F(0),) * 4)
check("Q1-06 u_2 = -one", u[2] == vscal(-1, ONEC))


def gdot(a, b):
    gb = mv(G, b)
    return sum(a[i] * gb[i] for i in range(4))


gram_ok = all(gdot(u[x], u[y]) == (F(4, 5) if x == y else F(-1, 5))
              for x in range(5) for y in range(5))
check("Q1-07 Gram is 4/5 diagonal and -1/5 off", gram_ok)

# affine representation
B = tuple(tuple(u[j][i] for j in range(4)) for i in range(4))   # columns u_0..u_3
BINV = minv(B)


def u_of(t):
    t %= 5
    if t <= 3:
        return u[t]
    return vscal(-1, vadd(vadd(u[0], u[1]), vadd(u[2], u[3])))


def rho(c, b):
    img = tuple(tuple(u_of(b + c * x)[i] for x in range(4)) for i in range(4))
    return mmul(img, BINV)


RHO = {(c, b): rho(c, b) for c in range(1, 5) for b in range(5)}
check("Q1-08 rho(c,b) u_x = u_(b+cx) for all twenty maps and all five x",
      all(mv(RHO[(c, b)], u[x]) == u[(b + c * x) % 5]
          for (c, b) in RHO for x in range(5)))
check("Q1-09 rho(1,1) = D", RHO[(1, 1)] == D)
check("Q1-10 group law on all four hundred pairs",
      all(mmul(RHO[(c, b)], RHO[(cc, bb)]) == RHO[((c * cc) % 5, (b + c * bb) % 5)]
          for (c, b) in RHO for (cc, bb) in RHO))
check("Q1-11 all twenty maps G-orthogonal and pairwise distinct",
      all(mmul(mT(RHO[k]), mmul(G, RHO[k])) == G for k in RHO)
      and len(set(RHO.values())) == 20)

# stabilizer averages
P = {}
Q = {}
g = {}
R = {}
C = {}
Jm = {}
for k in range(5):
    acc = Z4
    for a in range(1, 5):
        acc = madd(acc, RHO[(a, (k * (1 - a)) % 5)])
    P[k] = mscal(F(1, 4), acc)
    Q[k] = msub(I4, P[k])
    g[k] = RHO[(2, (-k) % 5)]

check("Q1-12 P_k idempotent, self-sharp, rank 1, image Q u_k",
      all(mmul(P[k], P[k]) == P[k] and sharp(P[k]) == P[k]
          and rank(P[k]) == 1 and mv(P[k], u[k]) == u[k] for k in range(5)))
check("Q1-13 Q_k idempotent, self-sharp, rank 3, P_k Q_k = 0",
      all(mmul(Q[k], Q[k]) == Q[k] and sharp(Q[k]) == Q[k]
          and rank(Q[k]) == 3 and mmul(P[k], Q[k]) == Z4 for k in range(5)))
check("Q1-14 g_k has order four; traces of g, g^2, g^3, g^4 are 0, 0, 0, 4, so "
      "the characteristic polynomial is x^4 - 1 = (x-1)(x+1)(x^2+1)",
      all(mpow(g[k], 4) == I4 and mpow(g[k], 2) != I4
          and trace(g[k]) == 0 and trace(mpow(g[k], 2)) == 0
          and trace(mpow(g[k], 3)) == 0 and trace(mpow(g[k], 4)) == 4
          for k in range(5)))

for k in range(5):
    R[k] = mscal(F(1, 4), madd(msub(I4, g[k]), msub(mpow(g[k], 2), mpow(g[k], 3))))
    C[k] = msub(Q[k], R[k])
    Jm[k] = mmul(g[k], C[k])

table_ok = True
for k in range(5):
    table_ok = table_ok and mmul(R[k], R[k]) == R[k] and sharp(R[k]) == R[k]
    table_ok = table_ok and mmul(C[k], C[k]) == C[k] and sharp(C[k]) == C[k]
    table_ok = table_ok and mmul(R[k], C[k]) == Z4 and mmul(C[k], R[k]) == Z4
    table_ok = table_ok and madd(R[k], C[k]) == Q[k]
    table_ok = table_ok and mmul(Jm[k], C[k]) == Jm[k] and mmul(C[k], Jm[k]) == Jm[k]
    table_ok = table_ok and mmul(Jm[k], Jm[k]) == mscal(-1, C[k])
    table_ok = table_ok and sharp(Jm[k]) == mscal(-1, Jm[k])
    table_ok = table_ok and mmul(R[k], Jm[k]) == Z4 and mmul(Jm[k], R[k]) == Z4
    table_ok = table_ok and rank(R[k]) == 1 and rank(C[k]) == 2
    for X in (R[k], C[k], Jm[k]):
        table_ok = table_ok and mmul(P[k], X) == Z4 and mmul(X, P[k]) == Z4
check("Q1-15 full R, C, J multiplication table at all five tokens, "
      "including J^2 = -C and J^sharp = -J", table_ok)

# centralizer nullspace: T P = 0, P T = 0, T g = g T; 48 equations, 16 unknowns
null_ok = True
for k in range(5):
    rows = []
    for i in range(4):
        for j in range(4):
            # equation family indexed by target entry (i, j); unknown T_{ab}
            rowTP = [F(0)] * 16
            rowPT = [F(0)] * 16
            rowCM = [F(0)] * 16
            for a in range(4):
                for b in range(4):
                    idx = 4 * a + b
                    rowTP[idx] += (P[k][b][j] if a == i else F(0))
                    rowPT[idx] += (P[k][i][a] if b == j else F(0))
                    rowCM[idx] += (g[k][b][j] if a == i else F(0)) - (g[k][i][a] if b == j else F(0))
            rows.extend([rowTP, rowPT, rowCM])
    rk_sys = rank(rows)
    nullity = 16 - rk_sys
    span = [sum([list(X[i]) for i in range(4)], []) for X in (R[k], C[k], Jm[k])]
    null_ok = null_ok and nullity == 3 and rank(span) == 3
    for X in (R[k], C[k], Jm[k]):
        null_ok = null_ok and mmul(X, P[k]) == Z4 and mmul(P[k], X) == Z4 \
            and mmul(X, g[k]) == mmul(g[k], X)
check("Q1-16 centralizer nullity is exactly three at every token and "
      "{R, C, J} is a basis of it", null_ok)

transport_ok = True
for (c, b) in RHO:
    rinv = sharp(RHO[(c, b)])
    for k in range(5):
        kk = (b + c * k) % 5
        for X, Y in ((R, R), (C, C), (Jm, Jm), (P, P), (Q, Q)):
            transport_ok = transport_ok and mmul(RHO[(c, b)], mmul(X[k], rinv)) == Y[kk]
check("Q1-17 affine transport of P, Q, R, C, J across tokens, all twenty maps",
      transport_ok)


def Tmem(k, e, r, s):
    return madd(mscal(e, R[k]), madd(mscal(r, C[k]), mscal(s, Jm[k])))


# QA2 negative route
tlist = [F(0), F(1), F(-1), F(1, 2), F(-2), F(3), F(1, 3), F(-1, 5), F(7, 2)]


def circle(t):
    return (F(1), (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


k0 = 2
members = [Tmem(k0, *circle(t)) for t in tlist]
check("Q2-01 every rational-circle member satisfies the exact effect equation "
      "T^sharp T = Q", all(mmul(sharp(T), T) == Q[k0] for T in members))
inj = True
for i in range(len(members)):
    for j in range(i + 1, len(members)):
        inj = inj and members[i] != members[j] and members[i] != mscal(-1, members[j])
check("Q2-02 pairwise physically distinct: T(t) != +-T(u) on the t list", inj)
check("Q2-03 Kraus completeness and cross term: P^sharp P + T^sharp T = I and "
      "P^sharp T = 0",
      all(madd(mmul(sharp(P[k0]), P[k0]), mmul(sharp(T), T)) == I4
          and mmul(sharp(P[k0]), T) == Z4 for T in members))
check("Q2-04 ordinary repeatability for every member: Q T = T",
      all(mmul(Q[k0], T) == T for T in members))

invol = {(1, 1): Tmem(k0, 1, 1, 0), (1, -1): Tmem(k0, 1, -1, 0),
         (-1, 1): Tmem(k0, -1, 1, 0), (-1, -1): Tmem(k0, -1, -1, 0)}
check("Q2-05 the four self-adjoint involutive members: s = 0 forced by "
      "sharp-symmetry, each satisfies T^2 = Q",
      all(sharp(T) == T and mmul(T, T) == Q[k0] for T in invol.values())
      and all(sharp(Tmem(k0, 1, r, s)) != Tmem(k0, 1, r, s)
              for (r, s) in [(F(3, 5), F(4, 5)), (F(0), F(1))]))
check("Q2-06 modulo sign exactly two physical classes: [Q] and [R - C]",
      invol[(1, 1)] == Q[k0]
      and invol[(-1, -1)] == mscal(-1, Q[k0])
      and invol[(-1, 1)] == mscal(-1, invol[(1, -1)])
      and invol[(1, -1)] != Q[k0] and invol[(1, -1)] != mscal(-1, Q[k0]))

# QA3 positive route
wR = None
wC = None
for j in range(4):
    colR = tuple(R[k0][i][j] for i in range(4))
    if any(colR) and wR is None:
        wR = colR
    colC = tuple(C[k0][i][j] for i in range(4))
    if any(colC) and wC is None:
        wC = colC
w_mix = vadd(wR, wC)


def dependent(a, b):
    for i in range(4):
        for j in range(i + 1, 4):
            if a[i] * b[j] - a[j] * b[i] != 0:
                return False
    return True


nonterm = [Tmem(k0, *circle(t)) for t in tlist if t != 0] + [invol[(1, -1)], invol[(-1, 1)]]
check("Q3-01 mixed-line witness: every sampled non +-Q member moves the line "
      "of w_R + w_C", all(not dependent(mv(T, w_mix), w_mix) for T in nonterm))
check("Q3-02 ray terminality holds at +Q and -Q on the witness set",
      all(dependent(mv(mscal(sgn, Q[k0]), v), v)
          for sgn in (1, -1) for v in [wR, wC, w_mix, mv(Jm[k0], wC)]))
check("Q3-03 strict idempotence T^2 = T holds in the class exactly at "
      "(e, r, s) = (1, 1, 0), that is T = Q",
      mmul(Q[k0], Q[k0]) == Q[k0]
      and all(mmul(T, T) != T for T in nonterm)
      and mmul(mscal(-1, Q[k0]), mscal(-1, Q[k0])) != mscal(-1, Q[k0]))

# QA6 added reduction: class-level idempotence
pm_ok = mmul(Q[k0], Q[k0]) == Q[k0]
mQ = mscal(-1, Q[k0])
pm_ok = pm_ok and mmul(mQ, mQ) == mscal(-1, mQ)
for T in nonterm:
    T2 = mmul(T, T)
    pm_ok = pm_ok and T2 != T and T2 != mscal(-1, T)
check("Q6-01 class-level idempotence T^2 = +-T holds exactly at T = +-Q on "
      "the sampled class", pm_ok)
RmC = invol[(1, -1)]
check("Q6-02 R - C is an explicit non-terminal involution: (R-C)^2 = Q and "
      "Q != +-(R-C)", mmul(RmC, RmC) == Q[k0]
      and Q[k0] != RmC and Q[k0] != mscal(-1, RmC))

# QA4 target comparison, deliberately last
E_low = mscal(F(1, 4), E11)
E_high = msub(I4, E_low)
check("Q4-01 target comparison last: P_2 = E_low and Q_2 = E_high",
      P[2] == E_low and Q[2] == E_high)
check("Q4-02 every sampled member realizes the frozen effects at k = 2",
      all(mmul(sharp(T), T) == E_high for T in members))

# QA5 reproduction of the sealed verifier
REPO = "/home/claude/twist-j"
SEALED = {
    "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/PREREG.md":
        "3274806fc70df8793040ab881b6d2ebf256ff485cae794d326b7fb7b941907fd",
    "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py":
        "992f1bcc6b9651a3bf349b5b03c460622b56f8a09790e0b4551cf5180881d2ac",
    "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/exact_matrix.py":
        "12b87e67a4c523428230f2a1acfd88e82697b710456e7c5e69e3f43ba5da8525",
    "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/EXPECTED.txt":
        "fc40a4568cd30ca107d3d48589a070e9896f1f61a5606b995cd9d345fbbe44e4",
}
pin_ok = True
for path, hh in SEALED.items():
    with open(os.path.join(REPO, path), "rb") as fh:
        pin_ok = pin_ok and hashlib.sha256(fh.read()).hexdigest() == hh
check("Q5-01 all four sealed files match the RUN.md pin hashes", pin_ok)

with open(os.path.join(REPO, "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/EXPECTED.txt"), "rb") as fh:
    expected = fh.read()
env = dict(os.environ)
env.update({"LC_ALL": "C", "LANG": "C", "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0", "TZ": "UTC"})
proc = subprocess.run([sys.executable, "probes/P-QDD-J-CENTRALIZER-TERMINALITY-1/verify.py"],
                      cwd=REPO, env=env, capture_output=True, timeout=120)
check("Q5-02 sealed verifier reproduces byte-identically, exit 0, empty stderr",
      proc.returncode == 0 and proc.stderr == b"" and proc.stdout == expected)

failures = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failures += 1
print("RESULT %d/%d PASS" % (len(CHECKS) - failures, len(CHECKS)))
sys.exit(1 if failures else 0)
