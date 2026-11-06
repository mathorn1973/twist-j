#!/usr/bin/env python3
"""NON-CANONICAL. Kontroly k notes/NOTE-VIETE-ZLATY-ZLOMEK-2026-09-15.md.

Jen standardni knihovna (Python >= 3.8). Kontroly EXACT pouzivaji cela
cisla, Fraction, Z[phi] a Q(zeta5). Kontroly NUM jsou numericke a nejsou
dukazem. Stdout je deterministicky: tiskne se jen PASS/FAIL a pevny text.
"""
import cmath
import math
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

RES = []


def check(kind, name, cond):
    RES.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + kind + " " + name)


# ------------------------------------------------ celociselne polynomy
def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return ptrim(r)


def pscale(k, a):
    return ptrim([k * x for x in a])


def ppow(a, n):
    r = [1]
    for _ in range(n):
        r = pmul(r, a)
    return r


# ------------------------------------------------ A: Viete a polynomy J
# U_n(c) v promenne t = 2c: U_0 = 1, U_1 = t, U_{n+1} = t U_n - U_{n-1}
U = [[1], [0, 1]]
for n in range(1, 13):
    U.append(padd(pmul([0, 1], U[n]), pscale(-1, U[n - 1])))


def m_poly(p):  # U_{p-1} je suda v t, m_p(x) s x = t^2 = 4c^2
    u = U[p - 1]
    assert all(u[i] == 0 for i in range(1, len(u), 2))
    return [u[i] for i in range(0, len(u), 2)]


M = {p: m_poly(p) for p in (3, 5, 7, 11, 13)}
check("EXACT", "A1 U_{p-1}(c) = m_p(4c^2): m_3 = x-1, m_5 = x^2-3x+1 = q, m_7 = x^3-5x^2+6x-1",
      M[3] == [-1, 1] and M[5] == [1, -3, 1] and M[7] == [-1, 6, -5, 1])

ok = True
for p, mp in M.items():
    m = (p - 1) // 2
    lhs = [0]
    for j, a in enumerate(mp):   # a * (w+1)^(2j) * w^(m-j)
        lhs = padd(lhs, pscale(a, pmul(ppow([1, 1], 2 * j), [0] * (m - j) + [1])))
    ok = ok and lhs == [1] * p
check("EXACT", "A2 p=3,5,7,11,13: w^((p-1)/2) m_p(2+w+1/w) = Phi_p(w); pro p=5: (w+1)^4-3w(w+1)^2+w^2 = Phi_5(w)",
      ok)

# ------------------------------------------------ N: Decimal
getcontext().prec = 70


def atan_inv(x):
    x = Decimal(x)
    tot, k, term = Decimal(0), 0, 1 / x
    while abs(term) > Decimal(10) ** -68:
        tot += term / (2 * k + 1) * (1 if k % 2 == 0 else -1)
        term /= x * x
        k += 1
    return tot


PI = 4 * (4 * atan_inv(5) - atan_inv(239))
TWO_OVER_PI = 2 / PI


def dcos(x):
    tot, term, k = Decimal(1), Decimal(1), 0
    while abs(term) > Decimal(10) ** -68:
        k += 1
        term = -term * x * x / ((2 * k - 1) * (2 * k))
        tot += term
    return tot


TOL = Decimal(10) ** -45
r = Decimal(2).sqrt()
P = r / 2
for n in range(2, 91):
    r = (2 + r).sqrt()
    P *= r / 2
check("NUM", "N1 obrazek: prod_{n=1}^{90} sqrt(2+...+sqrt2)/2 = 2/pi na 45 mist", abs(P - TWO_OVER_PI) < TOL)


def digit_product(p, levels):
    h = (p - 1) // 2
    prod = Decimal(1)
    for n in range(1, levels + 1):
        th = PI / Decimal(p) ** n
        prod *= (1 + 2 * sum(dcos(d * th) for d in range(1, h + 1))) / p
    return prod


check("NUM", "N2 prod_n (1/5) sum_{d=-2..2} e^{i pi d/5^n} = 2/pi na 45 mist (40 cislic)",
      abs(digit_product(5, 40) - TWO_OVER_PI) < TOL)
check("NUM", "N3 totez pro p=3 (100 cislic) a p=7 (40 cislic)",
      abs(digit_product(3, 100) - TWO_OVER_PI) < TOL and abs(digit_product(7, 40) - TWO_OVER_PI) < TOL)

# ------------------------------------------------ B: zlaty zlomek a pullback J
def charpoly(A):  # Faddeev-LeVerrier, koeficienty od x^0
    n = len(A)
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    Mk = [[F(0)] * n for _ in range(n)]
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    for k in range(1, n + 1):
        AM = [[sum(F(A[i][t]) * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        Mk = [[AM[i][j] + c[n - k + 1] * I[i][j] for j in range(n)] for i in range(n)]
        AMk = [[sum(F(A[i][t]) * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        c[n - k] = -sum(AMk[i][i] for i in range(n)) / k
    return [int(x) for x in c]


M2 = [[2, 1], [1, 1]]
Mcf = [[1, 1], [1, 0]]
sq = [[sum(Mcf[i][t] * Mcf[t][j] for t in range(2)) for j in range(2)] for i in range(2)]
check("EXACT", "B1 ((1,1),(1,0))^2 = ((2,1),(1,1)) s charakteristickym polynomem x^2-3x+1",
      sq == M2 and charpoly(M2) == [1, -3, 1])


# Q(zeta5): 5 celych koeficientu, kanonicky tvar c[4] = 0
def cz(c):
    t = c[4]
    return tuple(x - t for x in c)


def zmul(a, b):
    r = [0] * 5
    for i in range(5):
        for j in range(5):
            r[(i + j) % 5] += a[i] * b[j]
    return cz(r)


def zadd(a, b):
    return cz([x + y for x, y in zip(a, b)])


def zneg(a):
    return cz([-x for x in a])


def zconj(a):
    return cz([a[(-i) % 5] for i in range(5)])


def zp(k):
    c = [0] * 5
    c[k % 5] = 1
    return cz(c)


ONE, ZERO = zp(0), cz([0] * 5)
J = zadd(ONE, zp(2))


def coords(a):  # souradnice v bazi 1, zeta, zeta^2, zeta^3 (zeta^4 = -1-z-z^2-z^3)
    return [a[i] - a[4] for i in range(4)]


MJ = [[0] * 4 for _ in range(4)]
for k in range(4):
    col = coords(zmul(J, zp(k)))
    for i in range(4):
        MJ[i][k] = col[i]
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
L2 = [[MJ[i][a] * MJ[j][b] - MJ[i][b] * MJ[j][a] for (a, b) in pairs] for (i, j) in pairs]
check("EXACT", "B2 Lambda^2 nasobeni J v bazi 1,z,z^2,z^3: charakteristicky polynom (x^2-3x+1) Phi_10(x)",
      charpoly(L2) == pmul([1, -3, 1], [1, -1, 1, -1, 1]))


def mat_vec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def rank(A):
    A = [[F(x) for x in row] for row in A]
    rk, cols = 0, len(A[0])
    for col in range(cols):
        piv = next((r_ for r_ in range(rk, len(A)) if A[r_][col] != 0), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for r_ in range(len(A)):
            if r_ != rk and A[r_][col] != 0:
                f = A[r_][col] / A[rk][col]
                A[r_] = [x - f * y for x, y in zip(A[r_], A[rk])]
        rk += 1
    return rk


def hyperbolic_basis_ok(A, h1, h2):
    Asq = [[sum(A[i][t] * A[t][j] for t in range(6)) for j in range(6)] for i in range(6)]
    qA = [[Asq[i][j] - 3 * A[i][j] + (1 if i == j else 0) for j in range(6)] for i in range(6)]
    gg = 0
    for i in range(6):
        for j in range(i + 1, 6):
            gg = math.gcd(gg, h1[i] * h2[j] - h1[j] * h2[i])
    return (rank(qA) == 4 and mat_vec(qA, h1) == [0] * 6 and mat_vec(qA, h2) == [0] * 6 and gg == 1
            and mat_vec(A, h1) == [2 * a + b for a, b in zip(h1, h2)]
            and mat_vec(A, h2) == [a + b for a, b in zip(h1, h2)])


L2T = [[L2[j][i] for j in range(6)] for i in range(6)]
check("EXACT", "B3 celociselna hyperbolicka mriz ker q cap Z^6 ma bazi, na ktere je operator presne ((2,1),(1,1)): "
      "Lambda^2(M_J) g1=e01+e03+e23, g2=-(e02+e12+e13); tvar W -> M_J^T W M_J k1=-(e01+e12+e23), "
      "k2=e01+e02-e03+e12+e13+e23",
      hyperbolic_basis_ok(L2, [1, 0, 1, 0, 0, 1], [0, -1, 0, -1, -1, 0])
      and hyperbolic_basis_ok(L2T, [-1, 0, 0, -1, 0, -1], [1, 1, -1, 1, 1, 1]))


def phmul(a, b):  # Z[phi]: (a0 + a1 phi)(b0 + b1 phi), phi^2 = phi + 1
    return (a[0] * b[0] + a[1] * b[1], a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


PSI = (1, -1)
fib = [0, 1]
for _ in range(70):
    fib.append(fib[-1] + fib[-2])
ok, pw = True, (1, 0)
for n in range(1, 61):
    pw = phmul(pw, PSI)
    ok = ok and (-fib[n + 1], fib[n]) == (-pw[0], -pw[1])
check("EXACT", "B4 F_n phi - F_(n+1) = -psi^n pro n = 1..60 (u_n z J-HARMONIC-SEAM = chyby konvergentu)", ok)


def cf_quadratic(P0, Q0, D, terms):  # (P + sqrt D)/Q, D nectverec, Q | D - P^2
    out, P_, Q_ = [], P0, Q0

    def le(a):  # a <= (P + sqrt D)/Q ?
        u = a * Q_ - P_
        if Q_ > 0:
            return u < 0 or u * u < D
        return u > 0 and u * u > D
    for _ in range(terms):
        a = math.floor((P_ + math.sqrt(D)) / Q_)
        while not le(a):
            a -= 1
        while le(a + 1):
            a += 1
        out.append(a)
        P_ = a * Q_ - P_
        Q_ = (D - P_ * P_) // Q_
    return out


check("EXACT", "B5 retezove zlomky: phi = [1;1,1,...], phi^2 = [2;1,1,...], phi^-2 = [0;2,1,1,...] (20 clenu)",
      cf_quadratic(1, 2, 5, 20) == [1] * 20
      and cf_quadratic(3, 2, 5, 20) == [2] + [1] * 19
      and cf_quadratic(-3, -2, 5, 20) == [0, 2] + [1] * 18)

# ------------------------------------------------ C: zlomek, ktery se krouti
DELTA = zadd(ONE, zneg(J))
W = zmul(zp(2), J)
check("EXACT", "C1 delta = 1 - J = -zeta^2 a z^2 - z - zeta^2 J ma koreny J a delta",
      DELTA == zneg(zp(2))
      and zadd(zadd(zmul(J, J), zneg(J)), zneg(W)) == ZERO
      and zadd(zadd(zmul(DELTA, DELTA), zneg(DELTA)), zneg(W)) == ZERO)
PHI = zadd(ONE, zadd(zp(1), zp(4)))
IPHI = zadd(zp(1), zp(4))
NJBAR = zneg(zconj(J))
check("EXACT", "C2 nasobitel v delta je J/delta = -conj(J) = (-zeta^4)(zeta + zeta^4) = e^{3 pi i/5} phi^-1",
      zmul(NJBAR, DELTA) == J and NJBAR == zmul(zneg(zp(4)), IPHI) and zmul(PHI, IPHI) == ONE)
PSI5 = zneg(IPHI)
check("EXACT", "C3 rodina z -> 1 + psi x (psi x - 1)/z: x=1 dava citatel 1 a pevne body psi, phi = A(1); "
      "x=-zeta dava psi x = J a A(-zeta) = 1 - psi x = delta",
      phmul(PSI, (PSI[0] - 1, PSI[1])) == (1, 0) and (1 - PSI[0], -PSI[1]) == (0, 1)
      and zmul(PHI, PHI) == zadd(PHI, ONE)
      and zmul(PSI5, zneg(zp(1))) == J and zadd(ONE, zneg(zmul(PSI5, zneg(zp(1))))) == DELTA)
check("EXACT", "C4 J conj(J) = phi^-2 (|J| = 1/phi < |delta| = 1), sigma_2: (1+zeta^4)(1+zeta) = phi^2",
      zmul(zmul(J, zconj(J)), zmul(PHI, PHI)) == ONE and zmul(zadd(ONE, zp(4)), zadd(ONE, zp(1))) == zmul(PHI, PHI))


def iterate(p, a, steps=600):
    zeta = cmath.exp(2j * math.pi * a / p)
    Jc = 1 + zeta ** 2
    w = zeta ** 2 * Jc
    z = 1 + 0j
    for _ in range(steps):
        z = 1 + w / z
    return z, Jc, 1 - Jc


z1, J1, d1 = iterate(5, 1)
z2, J2, d2 = iterate(5, 2)
z7, J7, d7 = iterate(7, 1)
check("NUM", "C5 iterace: p=5 hlavni vnoreni konverguje k delta, po sigma_2 k J, p=7 hlavni vnoreni k J_7",
      abs(z1 - d1) < 1e-12 and abs(z2 - J2) < 1e-12 and abs(z7 - J7) < 1e-12)

# ------------------------------------------------ D: atribuce
check("EXACT", "D1 m_5 a m_7 nemaji racionalni koren, jsou tedy ireducibilni stupne 2 a 3",
      all(sum(c * x ** i for i, c in enumerate(M[p])) != 0 for p in (5, 7) for x in (1, -1)))

print("SOUHRN %d/%d PASS" % (sum(RES), len(RES)))
sys.exit(0 if all(RES) else 1)
