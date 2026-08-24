#!/usr/bin/env python3
"""P-AFFINE-QUADRATIC-READING-1 accepted verifier.

Exact arithmetic only: int, Fraction, and ordered Fraction pairs (a, b) read as
a + b sqrt5. No float, no complex, no randomness, no network, no subprocess, no
external data, no filesystem read or write. Zero arguments. Deterministic
stdout with no environment or platform field, so stdout is byte-identical on
every architecture. Run from the repository root:

    python3 probes/P-AFFINE-QUADRATIC-READING-1/verify.py

Public notation, pinned in block N below: M_J = m_J is the full step for
J = 1 + zeta_5^2, and D_J := M_J - I = m_{zeta_5^2} is the motor.
"""

from fractions import Fraction as F

CHECKS = []


def check(label, ok):
    CHECKS.append((label, bool(ok)))


# ---------------------------------------------------------------- matrices

def mm(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msc(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mtr(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def rank(rows):
    A = [list(r) for r in rows]
    n = len(A)
    m = len(A[0]) if n else 0
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        p = A[r][c]
        A[r] = [v / p for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
        if r == n:
            break
    return r


def det(M):
    A = [list(r) for r in M]
    n = len(A)
    d = F(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] / A[c][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[c])]
    return d


def flat(A):
    return [A[i][j] for i in range(len(A)) for j in range(len(A[0]))]


# ------------------------------------------------- Q(zeta_5) as Q^4, basis
# 1, zeta, zeta^2, zeta^3 with zeta^4 = -1 - zeta - zeta^2 - zeta^3.

def kmul(a, b):
    c = [F(0)] * 5
    for i in range(4):
        if a[i]:
            for j in range(4):
                if b[j]:
                    c[(i + j) % 5] += a[i] * b[j]
    return [c[k] - c[4] for k in range(4)]


def kel(*t):
    return [F(x) for x in t]


BASIS = [kel(1, 0, 0, 0), kel(0, 1, 0, 0), kel(0, 0, 1, 0), kel(0, 0, 0, 1)]
ONE = BASIS[0]
ZETA = BASIS[1]
ZPOW = BASIS + [kel(-1, -1, -1, -1)]


def mult_matrix(w):
    cols = [kmul(w, e) for e in BASIS]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def galois_matrix(k):
    cols = []
    for j in range(4):
        c = [F(0)] * 5
        c[(j * k) % 5] = F(1)
        cols.append([c[i] - c[4] for i in range(4)])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def apply(A, v):
    return [sum(A[i][j] * v[j] for j in range(4)) for i in range(4)]


def ktrace(w):
    return 4 * w[0] - w[1] - w[2] - w[3]


I4 = ident(4)
M1 = mult_matrix(ZETA)                    # m_zeta
DJ = mm(M1, M1)                           # motor D_J = m_{zeta^2}
MJ = mult_matrix(kel(1, 0, 1, 0))         # full step M_J = m_{1 + zeta^2}
U = galois_matrix(2)                      # u: zeta -> zeta^2
CJ = galois_matrix(4)                     # c = u^2, complex conjugation
UINV = mm(U, mm(U, U))

# ------------------------------------------------------ N. notation pins

check("N1 M_J equals I + D_J", meq(MJ, madd(I4, DJ)))
check("N2 det(M_J - I) equals det(D_J) equals 1", det(msub(MJ, I4)) == 1 and det(DJ) == 1)
check("N3 det(D_J - I) equals 5", det(msub(DJ, I4)) == 5)


def phi5(A):
    n = len(A)
    A2 = mm(A, A)
    A3 = mm(A2, A)
    A4 = mm(A3, A)
    return madd(madd(A4, A3), madd(A2, madd(A, ident(n))))


check("N4 Phi_5(D_J) vanishes and D_J has order five",
      meq(phi5(DJ), zeros(4, 4)) and meq(mm(DJ, mm(DJ, mm(DJ, mm(DJ, DJ)))), I4))
check("N5 I, D_J, D_J^2, D_J^3 independent so Phi_5 is the minimal polynomial",
      rank([flat(I4), flat(DJ), flat(mm(DJ, DJ)), flat(mm(DJ, mm(DJ, DJ)))]) == 4)
MJ2 = mm(MJ, MJ)
MJ3 = mm(MJ2, MJ)
MJ4 = mm(MJ3, MJ)
check("N6 M_J satisfies x^4 - 3x^3 + 4x^2 - 2x + 1 equals Phi_5(x - 1)",
      meq(madd(msub(madd(MJ4, msc(F(4), MJ2)), madd(msc(F(3), MJ3), msc(F(2), MJ))), I4),
          zeros(4, 4)))

# Phi_5 irreducible over Q. Every root has modulus one, so an integer monic
# factorization has all coefficients bounded by two; the search below is
# exhaustive well beyond that bound.
lin = all(1 + t + t * t + t ** 3 + t ** 4 != 0 for t in (-1, 1))
quad = True
for b, d in ((1, 1), (-1, -1)):
    for a in range(-8, 9):
        for c in range(-8, 9):
            if (a + c, b + d + a * c, a * d + b * c, b * d) == (1, 1, 1, 1):
                quad = False
check("N7 Phi_5 irreducible over Q by exhaustive bounded integer factorization", lin and quad)

# ------------------------------------------------------------- G. the group

check("G1 relations u D_J u^-1 equals D_J^2, u^4 equals I, D_J^5 equals I",
      meq(mm(U, mm(DJ, UINV)), mm(DJ, DJ)) and meq(mm(U, mm(U, mm(U, U))), I4))


def keyof(A):
    return tuple(tuple(r) for r in A)


seen = {keyof(I4): I4}
front = [I4]
while front:
    nxt = []
    for A in front:
        for g in (DJ, U):
            B = mm(A, g)
            if keyof(B) not in seen:
                seen[keyof(B)] = B
                nxt.append(B)
    front = nxt
GROUP = list(seen.values())
check("G2 the closure of D_J and u has exactly twenty elements", len(GROUP) == 20)

AFFINE = [(a, b) for a in (1, 2, 3, 4) for b in range(5)]
check("G3 the affine action is sharply two-transitive on five points",
      len({((a * 0 + b) % 5, (a * 1 + b) % 5) for a, b in AFFINE}) == 20 and len(AFFINE) == 20)
left = {(x, y) for x in range(5) for y in range(5)}
orbits = 0
while left:
    p = sorted(left)[0]
    orb = {((a * p[0] + b) % 5, (a * p[1] + b) % 5) for a, b in AFFINE}
    left -= orb
    orbits += 1
check("G4 the action has exactly two orbits on ordered pairs", orbits == 2)

# ------------------------------------------------- P. the permutation model

T5 = [[F(i == (j + 1) % 5) for j in range(5)] for i in range(5)]
S5 = [[F(i == (2 * j) % 5) for j in range(5)] for i in range(5)]
I5 = ident(5)
ONES5 = [[F(1)] * 5 for _ in range(5)]
P = [[ZPOW[x][i] for x in range(5)] for i in range(4)]

check("P1 P sends e_x to zeta^x and intertwines T with m_zeta and s_2 with u",
      meq(mm(P, T5), mm(M1, P)) and meq(mm(P, S5), mm(U, P)))
check("P2 P intertwines T^2 with the motor D_J", meq(mm(P, mm(T5, T5)), mm(DJ, P)))
check("P3 P has rank four and annihilates the all ones vector",
      rank(P) == 4 and all(sum(P[i][j] for j in range(5)) == 0 for i in range(4)))
check("P4 the full step is I + T^2 on the augmentation",
      meq(mm(P, madd(I5, mm(T5, T5))), mm(MJ, P)))

# ------------------------------------- E. absolute irreducibility of V over Q


def commutant_dim(gens, n):
    rows = []
    for t in range(n * n):
        X = zeros(n, n)
        X[t // n][t % n] = F(1)
        row = []
        for g in gens:
            row += flat(msub(mm(X, g), mm(g, X)))
        rows.append(row)
    return n * n - rank(rows)


check("E1 the rational endomorphism algebra of V under the full group is one dimensional",
      commutant_dim([DJ, U], 4) == 1)
check("E2 the character square sum over the group equals the group order",
      sum(sum(g[i][i] for i in range(4)) ** 2 for g in GROUP) == 20)
check("E3 control: under the motor alone the endomorphism algebra is four dimensional",
      commutant_dim([DJ], 4) == 4)

# ------------------------------------------------ C. the degree-two census

SYM = [(i, j) for i in range(4) for j in range(i, 4)]
ALT = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def sym_basis(t):
    B = zeros(4, 4)
    i, j = SYM[t]
    B[i][j] = F(1)
    B[j][i] = F(1)
    return B


def alt_basis(t):
    B = zeros(4, 4)
    i, j = ALT[t]
    B[i][j] = F(1)
    B[j][i] = F(-1)
    return B


def form_fixed_dim(gens, basis_fn, count):
    rows = []
    for t in range(count):
        B = basis_fn(t)
        row = []
        for g in gens:
            row += flat(msub(mm(mtr(g), mm(B, g)), B))
        rows.append(row)
    return count - rank(rows)


def linear_fixed_dim(gens):
    rows = []
    for t in range(4):
        l = [[F(j == t) for j in range(4)]]
        row = []
        for g in gens:
            row += flat(msub(mm(l, g), l))
        rows.append(row)
    return 4 - rank(rows)


def gram(a):
    G = zeros(4, 4)
    for i in range(4):
        for j in range(4):
            G[i][j] = ktrace(kmul(a, kmul(BASIS[i], apply(CJ, BASIS[j])))) / 2
    return G


QPLUS = gram(ONE)
S5EL = kel(-1, 0, -2, -2)
QMINUS = gram(S5EL)

check("C1 no nonzero invariant linear functional under the full group",
      linear_fixed_dim([DJ, U]) == 0)
check("C2 the invariant symmetric space under the full group is one dimensional",
      form_fixed_dim([DJ, U], sym_basis, 10) == 1)
check("C3 that line is spanned by the norm form q_plus",
      meq(mm(mtr(DJ), mm(QPLUS, DJ)), QPLUS) and meq(mm(mtr(U), mm(QPLUS, U)), QPLUS)
      and not meq(QPLUS, zeros(4, 4)))
check("C4 no nonzero invariant alternating form under the full group",
      form_fixed_dim([DJ, U], alt_basis, 6) == 0)
check("C5 q_plus is positive definite with leading minors 2, 15/4, 25/4, 125/16",
      [det([r[:k] for r in QPLUS[:k]]) for k in (1, 2, 3, 4)]
      == [F(2), F(15, 4), F(25, 4), F(125, 16)])
check("C6 control: under the motor alone the invariant symmetric space is two dimensional",
      form_fixed_dim([DJ], sym_basis, 10) == 2
      and rank([[QPLUS[i][j] for i, j in SYM], [QMINUS[i][j] for i, j in SYM]]) == 2)
check("C7 control: under the motor alone the invariant alternating space is two dimensional",
      form_fixed_dim([DJ], alt_basis, 6) == 2)
check("C8 the second symmetric channel is Galois odd, which is what kills it",
      meq(mm(mtr(DJ), mm(QMINUS, DJ)), QMINUS)
      and meq(mm(mtr(U), mm(QMINUS, U)), msc(F(-1), QMINUS)))

# ------------------------------------------ B. Burnside route, independent


def bilinear_fixed_dim(gens, n):
    rows = []
    for t in range(n * n):
        B = zeros(n, n)
        B[t // n][t % n] = F(1)
        row = []
        for g in gens:
            row += flat(msub(mm(mtr(g), mm(B, g)), B))
        rows.append(row)
    return n * n - rank(rows)


check("B1 invariant bilinear forms on the five point module span I and the all ones matrix",
      bilinear_fixed_dim([T5, S5], 5) == 2
      and meq(mm(mtr(T5), mm(I5, T5)), I5) and meq(mm(mtr(S5), mm(I5, S5)), I5)
      and meq(mm(mtr(T5), mm(ONES5, T5)), ONES5) and meq(mm(mtr(S5), mm(ONES5, S5)), ONES5))
check("B2 the all ones form dies on the augmentation, leaving exactly one",
      all(sum(P[i][j] for j in range(5)) == 0 for i in range(4)))

# --------------------------------- K. the Q(sqrt5) control on the motor alone

Z5 = (F(0), F(0))


def q5(a, b=0):
    return (F(a), F(b))


def q5a(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5s(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5m(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5inv(x):
    d = x[0] * x[0] - 5 * x[1] * x[1]
    return (x[0] / d, -x[1] / d)


def w_mm(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = Z5
            for t in range(len(B)):
                s = q5a(s, q5m(A[i][t], B[t][j]))
            row.append(s)
        out.append(row)
    return out


def w_add(A, B):
    return [[q5a(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def w_sub(A, B):
    return [[q5s(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def w_sc(c, A):
    return [[q5m(c, A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def w_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def w_rank(M):
    A = [list(r) for r in M]
    n, m, r = len(A), len(A[0]), 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i][c] != Z5:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        p = q5inv(A[r][c])
        A[r] = [q5m(p, v) for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] != Z5:
                f = A[i][c]
                A[i] = [q5s(x, q5m(f, y)) for x, y in zip(A[i], A[r])]
        r += 1
    return r


PHI = q5(F(1, 2), F(1, 2))
PSI = q5(F(1, 2), F(-1, 2))
W0 = [[Z5] * 4 for _ in range(4)]
WI = [[q5(1) if i == j else Z5 for j in range(4)] for i in range(4)]
WD = [[q5(DJ[i][j]) for j in range(4)] for i in range(4)]
WU = [[q5(U[i][j]) for j in range(4)] for i in range(4)]
WUI = [[q5(UINV[i][j]) for j in range(4)] for i in range(4)]
PROD = [q5(1), q5a(PHI, PSI), q5a(q5(2), q5m(PHI, PSI)), q5a(PHI, PSI), q5(1)]
check("K1 Phi_5 splits over Q(sqrt5) into the two golden quadratics",
      q5m(PHI, PSI) == q5(-1) and PROD == [q5(1), q5(1), q5(1), q5(1), q5(1)])
GQ = w_add(w_add(w_mm(WD, WD), w_sc(PSI, WD)), WI)
EPROJ = w_sc(q5(0, F(1, 5)), w_mm(w_add(WD, w_sc(PHI, WI)), GQ))
check("K2 over Q(sqrt5) the motor admits a lossy equivariant idempotent of rank two",
      w_eq(w_mm(EPROJ, EPROJ), EPROJ) and w_eq(w_mm(EPROJ, WD), w_mm(WD, EPROJ))
      and w_rank(EPROJ) == 2 and not w_eq(EPROJ, W0) and not w_eq(EPROJ, WI))
check("K3 the Galois generator carries that idempotent to its complement",
      w_eq(w_mm(WU, w_mm(EPROJ, WUI)), w_sub(WI, EPROJ)))

# ------------------------------------------------------- T. target last

check("T1 pullback identity: the unique invariant form is the five point Euclidean form",
      meq(mm(mtr(P), mm(QPLUS, P)), msub(msc(F(5, 2), I5), msc(F(1, 2), ONES5))))
ONES4 = [[F(1)] * 4 for _ in range(4)]
check("T2 the two frozen public constant matrices are positive rational multiples of q_plus",
      meq(msub(msc(F(5), I4), ONES4), msc(F(2), QPLUS))
      and meq(msub(I4, msc(F(1, 5), ONES4)), msc(F(2, 5), QPLUS)))

# --------------------------------------------------------------- report

fails = 0
for label, ok in CHECKS:
    print(("PASS " if ok else "FAIL ") + label)
    fails += not ok
if fails:
    print("DECISION AFFINE-QUADRATIC-READING-FIRED")
    print(f"FIRED count={fails}")
else:
    print("DECISION AFFINE-QUADRATIC-READING-CONFIRMED")
    print("LINEAR dim=0")
    print("ALTERNATING dim=0")
    print("SYMMETRIC dim=1 span=q_plus definite=positive")
    print("MOTOR_ONLY symmetric=2 alternating=2 endomorphism=4")
    print("ABSOLUTE endomorphism=1 route=rational_rank_field_independent")
    print("TARGET frozen_constants=positive_rational_multiples_of_q_plus")
print("SCOPE L1 only; no apparatus, instrument, selector, L5 stream or L6 measure")
print(f"RESULT {len(CHECKS) - fails}/{len(CHECKS)} PASS")
raise SystemExit(1 if fails else 0)
