#!/usr/bin/env python3
"""NON-CANONICAL. Kontroly k notes/NOTE-BAUER-IKOSAEDR-KROUCENA-STOPA-2026-09-15.md.

Jen standardni knihovna (Python >= 3.8). Kontroly EXACT pouzivaji cela cisla,
Fraction, Q(sqrt5) a Q(zeta5). Kontroly NUM jsou numericke a nejsou dukazem.
Stdout je deterministicky: tiskne se jen PASS/FAIL a pevny text.
"""
import itertools
import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F
from math import gcd

RES = []


def check(kind, name, cond):
    RES.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + kind + " " + name)


# ---------------------------------------------------------------- Q(zeta5)
# prvek = 5 celych koeficientu u zeta^0..zeta^4, kanonicky tvar c[4] = 0
def cz(c):
    t = c[4]
    return tuple(x - t for x in c)


def zmul(a, b):
    r = [0] * 5
    for i in range(5):
        if a[i]:
            for j in range(5):
                r[(i + j) % 5] += a[i] * b[j]
    return cz(r)


def zadd(a, b):
    return cz([x + y for x, y in zip(a, b)])


def zscal(k, a):
    return cz([k * x for x in a])


def zconj(a):
    return cz([a[(-i) % 5] for i in range(5)])


def zp(k):
    c = [0] * 5
    c[k % 5] = 1
    return cz(c)


ZERO = cz([0] * 5)
ONE = zp(0)


def wp(n):  # w = e^{i pi/5} = -zeta^3
    n %= 10
    return zscal(-1 if n % 2 else 1, zp(3 * n))


J = zadd(ONE, zp(2))
PHI = zadd(ONE, zadd(zp(1), zp(4)))          # phi = 1 + zeta + zeta^4
IPHI = zadd(zp(1), zp(4))                     # 1/phi = zeta + zeta^4

# ---------------------------------------------------------------- K: Klein a J
def pdivmod(num, den):  # koeficienty od nejvyssi mocniny, den monicky
    num = list(num)
    q = []
    for i in range(len(num) - len(den) + 1):
        c = num[i]
        q.append(c)
        for j, d in enumerate(den):
            num[i + j] -= c * d
    return q, num[len(num) - len(den) + 1:]


mJ = [1, 0, 0, 0, 0]
acc = [0, 0, 0, 0, 1]
for k in range(1, 5):          # sum_{k=0}^{4} (u-1)^k
    p = [1]
    for _ in range(k):
        p = [a - b for a, b in zip(p + [0], [0] + p)]
    p = [0] * (5 - len(p)) + p
    acc = [a + b for a, b in zip(acc, p)]
mJ = acc
kleinf = [1, 0, 0, 0, 0, 11, 0, 0, 0, 0, -1]  # u^10 + 11 u^5 - 1 = f(u,1)/u
_, rem = pdivmod(kleinf, mJ)
check("EXACT", "K1 Phi5(u-1) = u^4-3u^3+4u^2-2u+1 deli u^10+11u^5-1, tj. f(J,1)=0",
      mJ == [1, -3, 4, -2, 1] and all(r == 0 for r in rem))
check("EXACT", "K2 J*conj(J) = 1/phi^2 (horni prstenec |z|=1/phi), konjugaty 1+zeta^(+-1) maji phi^2",
      zmul(zmul(J, zconj(J)), zmul(PHI, PHI)) == ONE
      and zmul(zadd(ONE, zp(1)), zadd(ONE, zp(4))) == zmul(PHI, PHI))

# ---------------------------------------------------------------- A: ikosiany 2I
class Q5:
    __slots__ = ("a", "b")

    def __init__(s, a=0, b=0):
        s.a = F(a)
        s.b = F(b)

    def __add__(s, o):
        return Q5(s.a + o.a, s.b + o.b)

    def __sub__(s, o):
        return Q5(s.a - o.a, s.b - o.b)

    def __neg__(s):
        return Q5(-s.a, -s.b)

    def __mul__(s, o):
        return Q5(s.a * o.a + s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)

    def __eq__(s, o):
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b))

    def key(s):
        return (s.a, s.b)


Z0, E1, H = Q5(), Q5(1), Q5(F(1, 2))
PH, IPH = Q5(0, 1), Q5(-1, 1)


def qm(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def qc(x):
    return (x[0], -x[1], -x[2], -x[3])


def act(q, v):
    return qm(qm(q, (Z0,) + v), qc(q))[1:]


def qkey(x):
    return tuple(c.key() for c in x)


Gs = set()
for i in range(4):
    for s in (E1, -E1):
        e = [Z0] * 4
        e[i] = s
        Gs.add(tuple(e))
for sg in itertools.product((H, -H), repeat=4):
    Gs.add(tuple(sg))
base = [Z0, H, IPH * H, PH * H]
for p in itertools.permutations(range(4)):
    if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2:
        continue
    for sg in itertools.product((1, -1), repeat=4):
        Gs.add(tuple(base[p[i]] if sg[i] == 1 else -base[p[i]] for i in range(4)))
G = sorted(Gs, key=qkey)
g = next(q for q in G if q[0] == PH * H)      # rad 10, realna cast cos(pi/5)
N0 = g[1:]
K = [(E1, Z0, Z0, Z0)]
for _ in range(9):
    K.append(qm(K[-1], g))
verts = []
for q in G:
    v = act(q, N0)
    if v not in verts:
        verts.append(v)
check("EXACT", "A1 |2I|=120 uzavrene, K=<g> radu 10 = stabilizator vrcholu, 12 vrcholu",
      len(G) == 120 and all(qm(x, y) in Gs for x in G for y in G[:24])
      and qm(K[-1], g) == K[0] and len(set(K)) == 10
      and set(K) == {q for q in G if act(q, N0) == N0} and len(verts) == 12)


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def fl(x):
    return float(x.a) + float(x.b) * (1 + 5 ** 0.5) / 2


dvals = sorted({fl(dot(N0, v)) for v in verts})
ring = [v for v in verts if abs(fl(dot(N0, v)) - dvals[2]) < 1e-9]
reps = {}
for q in G:
    reps.setdefault(act(q, N0), q)
vid = {v: i for i, v in enumerate(verts)}
kid = {k: j for j, k in enumerate(K)}
steps = [q for q in G if act(q, N0) in ring]

tables = []
for t in steps:
    tab = {}
    for p, v in enumerate(verts):
        for j, k in enumerate(K):
            y = qm(qm(reps[v], k), t)
            u = act(y, N0)
            tab[p, j] = (vid[u], kid[qm(qc(reps[u]), y)])
    tables.append(tab)


def Tmat(tab, m):  # skalovano 10x
    T = {}
    for (p, j), (q, jp) in tab.items():
        T[p, q] = zadd(T.get((p, q), ZERO), wp(m * (j - jp)))
    return T


def tr3(T):  # skalovano 1000x
    rows = {}
    for (p, q), val in T.items():
        rows.setdefault(p, []).append((q, val))
    tot = ZERO
    for i in range(12):
        for j, a in rows[i]:
            for k, b in rows[j]:
                c = T.get((k, i))
                if c is not None:
                    tot = zadd(tot, zmul(zmul(a, b), c))
    return tot


def herm(T):
    return all(T.get((q, p), ZERO) == zconj(v) for (p, q), v in T.items())


ok_mod = ok_herm = ok_untw = True
herm_count = {}
for m in range(10):
    target = zscal(480 * 480, zmul(zadd(ONE, wp(m)), zadd(ONE, wp(-m))))
    herm_count[m] = 0
    for tab in tables:
        T = Tmat(tab, m)
        tr = tr3(T)
        if zmul(tr, zconj(tr)) != target:
            ok_mod = False
        if m == 0 and tr != zscal(960, ONE):
            ok_untw = False
        if herm(T):
            herm_count[m] += 1
            if m % 2 == 0 and tr != zscal(480, zadd(wp(2 * m), wp(-2 * m))):
                ok_herm = False
check("EXACT", "A2 vsech 10 charakteru K, vsech 50 kroku: |Tr T^3|^2 = (12/25)^2 |1+w^m|^2",
      ok_mod and len(steps) == 50)
check("EXACT", "A3 netwistovana stopa = 24/25 pro vsech 50 kroku", ok_untw)
check("EXACT", "A4 hermitovske kroky: sude m realne (12/25)(w^2m + w^-2m), liche m zadny hermitovsky",
      ok_herm and all(herm_count[m] > 0 for m in range(0, 10, 2))
      and all(herm_count[m] == 0 for m in range(1, 10, 2)))
T4 = [tr3(Tmat(tab, 4)) for tab in tables if herm(Tmat(tab, 4))]
check("EXACT", "A5 chi(g)=w^4=zeta5^2: hermitovska stopa = (12/25) zeta5^4 J",
      len(T4) > 0 and all(x == zscal(480, zmul(zp(4), J)) for x in T4))

# ---------------------------------------------------------------- B: uroven N
def level(N):
    def mul(A, B):
        return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N,
                (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)

    def neg(A):
        return tuple((-x) % N for x in A)

    def cv(v):
        return min(v, ((-v[0]) % N, (-v[1]) % N))

    def actm(A, v):
        return cv(((A[0] * v[0] + A[1] * v[1]) % N, (A[2] * v[0] + A[3] * v[1]) % N))

    def inv(A):
        return (A[3], (-A[1]) % N, (-A[2]) % N, A[0])

    I2, S = (1, 0, 0, 1), (0, N - 1, 1, 0)

    def Tp(b):
        return (1, b % N, 0, 1)

    SL = [A for A in itertools.product(range(N), repeat=4) if (A[0] * A[3] - A[1] * A[2]) % N == 1]
    sols = {}
    for a, b, c in itertools.product(range(N), repeat=3):
        P = mul(mul(mul(mul(mul(Tp(a), S), Tp(b)), S), Tp(c)), S)
        if P in (I2, neg(I2)):
            sols[a, b, c] = P
    okA = sols == {(1, 1, 1): neg(I2), (N - 1, N - 1, N - 1): I2}
    e = (1, 0)
    cusps = sorted({actm(A, e) for A in SL})
    idx = {v: i for i, v in enumerate(cusps)}
    V = len(cusps)
    rep = {}
    for A in SL:
        rep.setdefault(actm(A, e), A)
    Kex = {}
    for b in range(N):
        Kex[Tp(b)] = b
        Kex[neg(Tp(b))] = b
    step = {}
    for p, v in enumerate(cusps):
        for b in range(N):
            y = mul(mul(rep[v], Tp(b)), S)
            q = actm(y, e)
            step[p, b] = (idx[q], Kex[mul(inv(rep[q]), y)])
    Hh = {}
    for p in range(V):
        for b1, b2, b3 in itertools.product(range(N), repeat=3):
            q1, f1 = step[p, b1]
            q2, f2 = step[q1, b2]
            q3, f3 = step[q2, b3]
            if q3 == p:
                h = (b1 - f1 + b2 - f2 + b3 - f3) % N
                Hh[h] = Hh.get(h, 0) + 1
    PSL = len(SL) // 2
    pred = {}
    for h in (3 % N, (-3) % N):
        pred[h] = pred.get(h, 0) + PSL
    okB = Hh == pred and V * N == PSL
    J2 = F(1)
    for p in range(2, N + 1):
        if N % p == 0 and all(p % r for r in range(2, p)):
            J2 *= F(p * p - 1, p * p)
    okC = F(sum(Hh.values()), N ** 3) == J2 and F(PSL, N ** 3) == J2 / 2
    E, Fc = V * N // 2, sum(Hh.values()) // 6
    genus = 1 - (V - E + Fc) // 2
    Kset = [A for A in SL if actm(A, e) == e]
    orb = {}
    for i, v in enumerate(cusps):
        xi = inv(rep[v])
        for j, w in enumerate(cusps):
            u = actm(xi, w)
            kk = min(actm(k, u) for k in Kset)
            orb.setdefault(kk, [[] for _ in range(V)])[i].append(j)
    mats = list(orb.values())

    def prod(A, B):
        r = {}
        for i in range(V):
            for k in A[i]:
                for j in B[k]:
                    r[i, j] = r.get((i, j), 0) + 1
        return r
    gel = all(prod(A, B) == prod(B, A) for A in mats for B in mats)
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    elem2 = all((u * u) % N in (1, N - 1) for u in units)
    onestep = all(((6 - 1) * m) % N == 0 or ((6 + 1) * m) % N == 0 for m in range(N))
    return okA, okB, okC, genus, gel, elem2, onestep


rows = {N: level(N) for N in range(3, 14)}
check("EXACT", "B1 pro N=3..13: T^a S T^b S T^c S = +-I jen pro a=b=c=1 (-I) a a=b=c=-1 (+I)",
      all(r[0] for r in rows.values()))
check("EXACT", "B2 pro N=3..13: holonomie uzavrenych 3-prochazek je jen +-3, kazda |PSL| krat",
      all(r[1] for r in rows.values()))
check("EXACT", "B3 pro N=3..13: netwistovana stopa J_2(N)/N^2, vaha |PSL|/N^3 = J_2(N)/(2N^2)",
      all(r[2] for r in rows.values()))
check("EXACT", "B4 genus 0 presne pro N<=5 (genera 0,0,0,1,3,5,10,13,26,25,50)",
      [rows[N][3] for N in range(3, 14)] == [0, 0, 0, 1, 3, 5, 10, 13, 26, 25, 50])
check("EXACT", "B5 Heckeho algebra komutativni presne kdyz u^2 = +-1 pro vsechny jednotky mod N (3..13)",
      all(r[4] == r[5] for r in rows.values())
      and [N for N in rows if rows[N][4]] == [3, 4, 5, 6, 8, 10, 12])
check("EXACT", "B6 tvar 1 + jeden krok presne pro N in {5,7}; spolu s komutativitou jen N=5",
      [N for N in rows if rows[N][6]] == [5, 7]
      and [N for N in rows if rows[N][6] and rows[N][4]] == [5])

# spinorova verze na urovni 5: K = <-T> radu 10
N = 5


def mul5(A, B):
    return ((A[0] * B[0] + A[1] * B[2]) % N, (A[0] * B[1] + A[1] * B[3]) % N,
            (A[2] * B[0] + A[3] * B[2]) % N, (A[2] * B[1] + A[3] * B[3]) % N)


def cv5(v):
    return min(v, ((-v[0]) % N, (-v[1]) % N))


def act5(A, v):
    return cv5(((A[0] * v[0] + A[1] * v[1]) % N, (A[2] * v[0] + A[3] * v[1]) % N))


SL5 = [A for A in itertools.product(range(N), repeat=4) if (A[0] * A[3] - A[1] * A[2]) % N == 1]
mT = (4, 4, 0, 4)
gens, X = [], (1, 0, 0, 1)
for _ in range(10):
    gens.append(X)
    X = mul5(X, mT)
kex = {k: i for i, k in enumerate(gens)}
cus = sorted({act5(A, (1, 0)) for A in SL5})
ix = {v: i for i, v in enumerate(cus)}
rp = {}
for A in SL5:
    rp.setdefault(act5(A, (1, 0)), A)
st = {}
for p, v in enumerate(cus):
    for e_ in range(10):
        y = mul5(mul5(rp[v], gens[e_]), (0, 4, 1, 0))
        q = act5(y, (1, 0))
        A = rp[q]
        st[p, e_] = (ix[q], kex[mul5((A[3], (-A[1]) % N, (-A[2]) % N, A[0]), y)])
Hs = {}
for p in range(12):
    for a, b, c in itertools.product(range(10), repeat=3):
        q1, f1 = st[p, a]
        q2, f2 = st[q1, b]
        q3, f3 = st[q2, c]
        if q3 == p:
            h = (a - f1 + b - f2 + c - f3) % 10
            Hs[h] = Hs.get(h, 0) + 1
check("EXACT", "B7 spinor, uroven 5, K=<-T>: holonomie jen 2 a 3, kazda 480 krat, tj. |Tr| = (12/25)|1+w^m|",
      len(gens) == len(set(gens)) == 10 and Hs == {2: 480, 3: 480})

# ---------------------------------------------------------------- C: kontinuum
def mat(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


RY = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]


def RZ(c, s):
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


okpoly = True
for c2, s2, c3, s3 in itertools.product(range(3), repeat=4):
    M = mat(mat(mat(mat(RY, RZ(c2, s2)), RY), RZ(c3, s3)), RY)
    col = [M[0][2], M[1][2], M[2][2]]
    if col != [-c3, c2 * s3, s2 * s3]:
        okpoly = False
okfull = True
for s in (1, -1):
    M = mat(mat(mat(mat(mat(RZ(0, s), RY), RZ(0, s)), RY), RZ(0, s)), RY)
    if M != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        okfull = False
check("EXACT", "C1 R_y R_z(a2) R_y R_z(a3) R_y N = (-cos a3, cos a2 sin a3, sin a2 sin a3); "
      "reseni jen a1=a2=a3=+-pi/2", okpoly and okfull)


def dvals(m, nmax):
    b = 2 * m
    P0, P1 = 1.0, -b / 2
    out = [P0, P1]
    for n in range(2, nmax + 1):
        P2 = ((2 * n + b - 1) * (-b * b) * P1 - 2 * (n - 1) * (n + b - 1) * (2 * n + b) * P0) / (
            2 * n * (n + b) * (2 * n + b - 2))
        out.append(P2)
        P0, P1 = P1, P2
    return [x / 2 ** m for x in out]


okser = True
for m in range(5):
    d = dvals(m, 600000)
    L = 60000.0
    s = math.fsum((2 * (n + m) + 1) * d[n] ** 3 * math.exp(-((n + m) / L) ** 2) for n in range(len(d)))
    if abs(s - 2 / math.pi * math.cos(m * math.pi / 2)) > 1e-8:
        okser = False
check("NUM", "C2 sum_l (2l+1) d^l_mm(pi/2)^3 = (2/pi) cos(m pi/2) pro m=0..4, gaussovske vyhlazeni, tol 1e-8",
      okser)

# ---------------------------------------------------------------- D: zlaty sourozenec
getcontext().prec = 60


def atan_inv(x):
    x = Decimal(x)
    tot, k, term = Decimal(0), 0, 1 / x
    while abs(term) > Decimal(10) ** -58:
        tot += term / (2 * k + 1) * (1 if k % 2 == 0 else -1)
        term /= x * x
        k += 1
    return tot


PI = 4 * (4 * atan_inv(5) - atan_inv(239))
s5 = Decimal(5).sqrt()
phi = (1 + s5) / 2
z = 1 / phi ** 6
tot, n = Decimal(0), 0
while True:
    term = Decimal(math.comb(2 * n, n) ** 3) / Decimal(64) ** n * (1 + (5 + s5) * n) * z ** n
    tot += term
    if term < Decimal(10) ** -55:
        break
    n += 1
check("NUM", "D1 sum C(2n,n)^3/64^n (1+(5+sqrt5)n) phi^(-6n) = phi^(5/2)/pi na 45 mist",
      abs(tot - phi ** 2 * phi.sqrt() / PI) < Decimal(10) ** -45)
check("EXACT", "D2 (J conj J)^3 = phi^(-6): parametr rady je jen modul J",
      zmul(zmul(zmul(J, zconj(J)), zmul(J, zconj(J))), zmul(J, zconj(J)))
      == zmul(zmul(IPHI, IPHI), zmul(zmul(IPHI, IPHI), zmul(IPHI, IPHI))))

print("SOUHRN %d/%d PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
