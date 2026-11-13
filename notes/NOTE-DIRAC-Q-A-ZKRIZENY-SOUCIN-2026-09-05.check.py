# NON-CANONICAL in-session checks for NOTE-DIRAC-Q-A-ZKRIZENY-SOUCIN_2026-09-05_CZ
# Standard library only. Exact arithmetic (Fraction). No float in any assertion.
# Carrier: K = Q(j), j = zeta_5, ordered basis (1, j, j^2, j^3), j^4 = -1-j-j^2-j^3.
from fractions import Fraction as F

def red(c):
    v = [F(0)] * 4
    for k, a in c.items():
        k %= 5
        if k == 4:
            for i in range(4): v[i] -= a
        else: v[k] += a
    return v

def mulmat(el):                      # matrix of x -> (el) * x
    cols = []
    for b in range(4):
        c = {}
        for k, a in el.items(): c[(k + b) % 5] = c.get((k + b) % 5, F(0)) + a
        cols.append(red(c))
    return [[cols[b][r] for b in range(4)] for r in range(4)]

def galmat(t):                       # Galois j -> j^t
    cols = [red({(t * b) % 5: F(1)}) for b in range(4)]
    return [[cols[b][r] for b in range(4)] for r in range(4)]

def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tp(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def sub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sc(a, A): return [[a * x for x in r] for r in A]
def inv(A):
    m = len(A); M = [r[:] + [F(1) if i == j else F(0) for j in range(m)] for i, r in enumerate(A)]
    for c in range(m):
        p = next(r for r in range(c, m) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(m):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [r[m:] for r in M]
def det(A):
    m = len(A); M = [r[:] for r in A]; d = F(1)
    for c in range(m):
        p = next((r for r in range(c, m) if M[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]; pv = M[c][c]
        for r in range(c + 1, m):
            if M[r][c] != 0:
                f = M[r][c] / pv; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d

I4    = [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
MJ    = mulmat({0: F(1), 2: F(1)})              # J    = 1 + j^2
MJb   = mulmat({0: F(1), 3: F(1)})              # Jbar = 1 + j^3
Mphi  = mulmat({2: F(-1), 3: F(-1)})            # phi  = -j^2 - j^3
M2phi = sub(sc(F(2), I4), Mphi)                 # 2 - phi = phi^-2
H     = [[F(4, 5) if (a - b) % 5 == 0 else F(-1, 5) for b in range(4)] for a in range(4)]
adj   = mm(mm(inv(H), tp(MJ)), H)               # adjoint of M_J wrt h = (1/5)Tr(x ybar)
G3    = galmat(3)
ok    = []

def chk(name, cond): ok.append(bool(cond)); print(("PASS  " if cond else "FAIL  ") + name)

chk("1  M_J is not a scalar matrix (Dirac: not a c-number)",
    MJ != sc(MJ[0][0], I4))
chk("2  Euclidean form: M_J M_J^T != M_J^T M_J  (3 vs 2 at entry 11)",
    mm(MJ, tp(MJ)) != mm(tp(MJ), MJ) and mm(MJ, tp(MJ))[0][0] == 3 and mm(tp(MJ), MJ)[0][0] == 2)
chk("3  h = (1/5)Tr(x ybar): adjoint of M_J is M_Jbar, det H = 1/5",
    adj == MJb and det(H) == F(1, 5))
chk("4  h-normality: [M_J, M_J*] = 0",
    mm(MJ, adj) == mm(adj, MJ))
chk("5  M_J M_J* = M_(2-phi) = M_(2+j^2+j^3) = M_(phi^-2)",
    mm(MJ, adj) == M2phi == mulmat({0: F(2), 2: F(1), 3: F(1)}))
T3 = sub(sc(F(3), I4), Mphi)
chk("6  (3I - M_phi)^2 = 5(2I - M_phi), so B = (1/sqrt5)(3I - M_phi), B^2 = M_J M_J*",
    mm(T3, T3) == sc(F(5), M2phi) and T3 != sc(F(0), I4))
chk("7  Galois gamma_3 has order 4 and does not commute with M_J",
    mm(mm(mm(G3, G3), G3), G3) == I4 and mm(G3, MJ) != mm(MJ, G3))
chk("8  crossed-product relation gamma M_x gamma^-1 = M_gamma(x)",
    mm(mm(G3, MJ), inv(G3)) == mulmat({0: F(1), 1: F(1)}))     # gamma_3(J) = 1 + j^6 = 1 + j
gp = [I4]
for _ in range(3): gp.append(mm(gp[-1], G3))
basis = [[x for row in mm(mulmat({i: F(1)}), gp[k]) for x in row] for i in range(4) for k in range(4)]
Mtx = [[basis[c][r] for c in range(16)] for r in range(16)]
chk("9  [End_Z(O_K) : O_K x| C_4] = 5^6 = 15625",
    abs(det(Mtx)) == 15625)
E = [[F(1) if (i, j) == (0, 0) else F(0) for j in range(4)] for i in range(4)]
sol = [sum(inv(Mtx)[i][k] * [x for row in E for x in row][k] for k in range(16)) for i in range(16)]
chk("10 coordinate projection E is outside O_K x| C_4, denominators exactly {1,5}",
    not all(x.denominator == 1 for x in sol) and {x.denominator for x in sol} == {1, 5})
chk("11 delta = 1 - J = -j^2 and delta + delta^-1 = -j^2 - j^3 = phi",
    sub(I4, MJ) == mulmat({2: F(-1)}) and
    [a + b for a, b in zip(red({2: F(-1)}), red({3: F(-1)}))] == red({2: F(-1), 3: F(-1)}))
chk("12 Tr(delta^n), n=0..9 = (4,1,-1,1,-1,-4,-1,1,-1,1)",
    [sum(mulmat({(2 * n) % 5: F((-1) ** n)})[i][i] for i in range(4)) for n in range(10)]
    == [F(x) for x in (4, 1, -1, 1, -1, -4, -1, 1, -1, 1)])
print("\n%d of %d PASS" % (sum(ok), len(ok)))
