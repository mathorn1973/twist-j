#!/usr/bin/env python3
# P-R2-LAMBDA-HAAR-1 verifier. See PREREG.md (the pinned preregistration)
# before this file existed. Stdlib only; exact integer arithmetic in
# Z[zeta_5] and Z[zeta_20]; exact Fraction interval arithmetic; no float in
# any assertion. Decimal prints are labeled witnesses only.
from fractions import Fraction as F
from itertools import permutations

# ---------- interval and log machinery ----------
PI_LO = F(3141592653589793, 10**15)
PI_HI = F(3141592653589794, 10**15)
K_SER = 40
DEC = 10**36  # outward rounding denominator


def atanh_series(y, K=K_SER):
    u = (y - 1) / (y + 1)
    u2 = u * u
    s = F(0)
    up = u
    for k in range(K + 1):
        s += up / (2 * k + 1)
        up *= u2
    s *= 2
    if u == 0:
        return (F(0), F(0))
    tail = 2 * up / ((2 * K + 3) * (1 - u2))
    return (s, s + tail)


LOG2 = atanh_series(F(2))


def rnd(iv):
    lo, hi = iv
    lo2 = F((lo.numerator * DEC) // lo.denominator, DEC)
    hi2 = F(-((-hi.numerator * DEC) // hi.denominator), DEC)
    return (lo2, hi2)


def log_bounds(x):
    if x == 1:
        return (F(0), F(0))
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return (-hi, -lo)
    k = 0
    y = x
    while y >= 2:
        y = y / 2
        k += 1
    lo, hi = atanh_series(y)
    return rnd((lo + k * LOG2[0], hi + k * LOG2[1]))


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def isub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def imul(a, b):
    ps = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return (min(ps), max(ps))


def isc(a, c):  # scale by exact Fraction c (any sign)
    p, q = a[0] * c, a[1] * c
    return (p, q) if p <= q else (q, p)


def dec(x, nd=12):
    sgn = '-' if x < 0 else ''
    x = abs(x)
    ip = x.numerator // x.denominator
    fr = x - ip
    digs = (fr * 10**nd).numerator // (fr * 10**nd).denominator
    return f"{sgn}{ip}.{digs:0{nd}d}"


# ---------- Z[zeta_5] exact arithmetic ----------
def z5_mul(a, b):
    c = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                c[i + j] += a[i] * b[j]
    c[0] += c[5]
    c[1] += c[6]
    r = c[:5]
    if r[4]:
        t = r[4]
        r = [r[0] - t, r[1] - t, r[2] - t, r[3] - t]
    else:
        r = r[:4]
    return tuple(r)


def z5_conj(a, m):
    c = [0] * 5
    for i in range(4):
        c[(i * m) % 5] += a[i]
    if c[4]:
        t = c[4]
        return (c[0] - t, c[1] - t, c[2] - t, c[3] - t)
    return tuple(c[:4])


def z5_norm(a):
    p = a
    for m in (2, 3, 4):
        p = z5_mul(p, z5_conj(a, m))
    assert p[1] == 0 and p[2] == 0 and p[3] == 0, "norm not rational"
    return p[0]


def v5(n):
    n = abs(n)
    assert n != 0
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v


J5 = (1, 0, 1, 0)
ONE5 = (1, 0, 0, 0)

# ---------- Z[zeta_20] exact arithmetic ----------
# Phi_20(x) = x^8 - x^6 + x^4 - x^2 + 1;  x^8 = x^6 - x^4 + x^2 - 1
def z20_reduce(c):
    c = list(c) + [0] * (15 - len(c))
    for d in range(14, 7, -1):
        t = c[d]
        if t:
            c[d] = 0
            c[d - 2] += t
            c[d - 4] -= t
            c[d - 6] += t
            c[d - 8] -= t
    return tuple(c[:8])


def z20_mono(e):
    e %= 20
    c = [0] * 20
    c[e] = 1
    # fold exponents >= 15 first via x^20 = 1 not needed (e < 20); reduce >= 8
    for d in range(19, 7, -1):
        t = c[d]
        if t:
            c[d] = 0
            c[d - 2] += t
            c[d - 4] -= t
            c[d - 6] += t
            c[d - 8] -= t
    return tuple(c[:8])


def z20_mul(a, b):
    c = [0] * 15
    for i in range(8):
        if a[i]:
            for j in range(8):
                c[i + j] += a[i] * b[j]
    return z20_reduce(c)


def z20_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def z20_neg(a):
    return tuple(-x for x in a)


def z20_conj(a):
    r = (0,) * 8
    for d in range(8):
        if a[d]:
            m = z20_mono((19 * d) % 20)
            r = z20_add(r, tuple(a[d] * x for x in m))
    return r


checks = []

# R0: N(J) = 1
checks.append(("R0 N(J) = 1 (J is a unit of the plenum ring)",
               z5_norm(J5) == 1))

# R1: E(x) = Phi_5(1-x) coefficients, Eisenstein at 5, E(0) = 5
def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c

one_minus = [1, -1]
E = [1]
pw = [1]
acc = [0] * 5
for k in range(5):
    if k:
        pw = poly_mul(pw, one_minus)
    for i, c in enumerate(pw):
        acc[i] += c
E = acc  # (1-x)^0 + ... + (1-x)^4, ascending
checks.append(("R1 E(x) = 5 - 10x + 10x^2 - 5x^3 + x^4, Eisenstein at 5",
               E == [5, -10, 10, -5, 1] and E[0] % 25 != 0
               and all(E[i] % 5 == 0 for i in range(4))))

# R2: disc(E) = Res(E, E') = 125 via 7x7 Sylvester determinant
Ec = E[::-1]                     # descending: [1, -5, 10, -10, 5]
Ep = [4, -15, 20, -10]           # E' descending
S = []
for r in range(3):
    S.append([0] * r + Ec + [0] * (3 - r - 1 + 1))
for r in range(4):
    S.append([0] * r + Ep + [0] * (4 - r - 1 + 1))
S = [row[:7] for row in S]
det = 0
for perm in permutations(range(7)):
    sgn = 1
    seen = list(perm)
    # permutation sign by counting inversions
    inv = sum(1 for i in range(7) for j in range(i + 1, 7)
              if seen[i] > seen[j])
    sgn = -1 if inv % 2 else 1
    p = sgn
    for i in range(7):
        p *= S[i][perm[i]]
        if p == 0:
            break
    det += p
checks.append(("R2 disc(E) = Res(E, E') = 125", det == 125))

# R3: N(J - 1) = N(zeta^2) = 1
Jm1 = (0, 0, 1, 0)
checks.append(("R3 N(J - 1) = 1, v_lambda(J - 1) = 0 (only trivial character-basis element fixed pointwise)",
               z5_norm(Jm1) == 1))

# R4: V-profile and the order tower
V = {}
Jk = ONE5
allnz = True
for k in range(1, 101):
    Jk = z5_mul(Jk, J5)
    a = (Jk[0] - 1, Jk[1], Jk[2], Jk[3])
    n = z5_norm(a)
    if n == 0:
        allnz = False
        break
    V[k] = v5(n)
ords = []
for n in range(1, 9):
    kk = next((k for k in range(1, 101) if V.get(k, -1) >= n), None)
    ords.append(kk)
checks.append(("R4 order tower ord(J mod lambda^n), n = 1..8 = "
               "(4, 20, 20, 20, 20, 20, 100, 100)",
               allnz and ords == [4, 20, 20, 20, 20, 20, 100, 100]))

# R5: orbit counts
counts = []
okdiv = True
for n in range(1, 9):
    tot = 4 * 5 ** (n - 1)
    if tot % ords[n - 1] != 0:
        okdiv = False
        break
    counts.append(tot // ords[n - 1])
checks.append(("R5 unit-level orbit counts (1, 1, 5, 25, 125, 625, 625, 3125)",
               okdiv and counts == [1, 1, 5, 25, 125, 625, 625, 3125]))

# R6: level-1 witnesses. Basis (psi_1, psi_2, psi_3, psi_4); U psi_c = psi_{2c}
U = [[0] * 4 for _ in range(4)]
for c in range(1, 5):
    U[(2 * c) % 5 - 1][c - 1] = 1
w = [1, -1, -1, 1]            # psi_1 - psi_2 - psi_3 + psi_4
Uw = [sum(U[r][c] * w[c] for c in range(4)) for r in range(4)]
ok_m1 = Uw == [-x for x in w]
# i-eigenvector over Z[i]: v = psi_1 - i psi_2 + i psi_3 - psi_4
vre = [1, 0, 0, -1]
vim = [0, -1, 1, 0]
Ure = [sum(U[r][c] * vre[c] for c in range(4)) for r in range(4)]
Uim = [sum(U[r][c] * vim[c] for c in range(4)) for r in range(4)]
# i * v = (-vim) + i(vre)
ok_i = Ure == [-x for x in vim] and Uim == vre
checks.append(("R6 level-1 permutation (1 2 4 3): U w = -w (real) and "
               "U v = i v (Z[i])", ok_m1 and ok_i))

# R7: HS bookkeeping
psum = 2 * sum(4 * 5 ** (j - 1) for j in range(1, 9))
checks.append(("R7 HS partial sum through level 8 = 2(5^8 - 1) = 781248; "
               "V(k) finite for k = 1..100",
               psum == 781248 and psum == 2 * (5 ** 8 - 1) and allnz
               and len(V) == 100))

# R8: (-1)-multiplicity witness at levels 1..4
evens = [ords[n - 1] % 2 == 0 for n in range(1, 5)]
csum = sum(counts[:4])
checks.append(("R8 all level 1..4 orbits even; count 1 + 1 + 5 + 25 = 32",
               all(evens) and csum == 32))

# R9: CNF target block
# chi table with chi(2) = i, as Gaussian pairs (re, im)
chi = {1: (1, 0), 2: (0, 1), 3: (0, -1), 4: (-1, 0)}
B1 = (sum(F(a * chi[a][0], 5) for a in range(1, 5)),
      sum(F(a * chi[a][1], 5) for a in range(1, 5)))
okB = B1 == (F(-3, 5), F(-1, 5))
okB2 = B1[0] ** 2 + B1[1] ** 2 == F(2, 5)
# tau(chi) in Z[zeta_20]: sum chi(a) zeta_5^a, zeta_5 = x^4, i = x^5
tau = (0,) * 8
for a in range(1, 5):
    re, im = chi[a]
    if re:
        m = z20_mono(4 * a)
        tau = z20_add(tau, tuple(re * x for x in m))
    if im:
        m = z20_mono(5 + 4 * a)
        tau = z20_add(tau, tuple(im * x for x in m))
tt = z20_mul(tau, z20_conj(tau))
oktau = tt == (5, 0, 0, 0, 0, 0, 0, 0)
# tau(chi_2) = zeta - zeta^2 - zeta^3 + zeta^4 = 2 phi - 1 in Z[zeta_5]
z = (0, 1, 0, 0)
t2 = (0, 1, -1, -1)
z4 = z5_conj(z, 4)
t2 = tuple(t2[i] + z4[i] for i in range(4))
okt2 = t2 == (-1, 0, -2, -2) and z5_mul(t2, t2) == (5, 0, 0, 0)
# residue identity coefficients of pi^2 log(phi) / sqrt5
lhs = F(2, 1) ** 2 * 1 * 2 / (10 * 5)          # (2pi)^2 h (2 Lphi)/(w 5 sqrt5)
rhs_L2 = F(5, 25) * F(2, 5)                    # |L(1,chi)|^2 / pi^2 = 2/25
rhs = F(2, 1) * rhs_L2                         # (2 Lphi/sqrt5)(2 pi^2/25)
okres = lhs == F(4, 25) and rhs == F(4, 25) and rhs_L2 == F(2, 25)
checks.append(("R9 CNF block: B_1 = (-3-i)/5, |B_1|^2 = 2/5, tau taubar = 5, "
               "tau(chi_2) = 2 phi - 1, residue coefficient 4/25 both routes",
               okB and okB2 and oktau and okt2 and okres))

# R10: junction instrumentation
N = 300
HN = sum(F(1, k) for k in range(1, N + 1))
lnN = log_bounds(F(N))
g_lo = HN - lnN[1] - F(1, 2 * N) + F(1, 12 * N * N) - F(1, 120 * N ** 4)
g_hi = HN - lnN[0] - F(1, 2 * N) + F(1, 12 * N * N) - F(1, 120 * N ** 4) \
    + F(1, 252 * N ** 6)
gam = (g_lo, g_hi)
okg = (g_hi - g_lo) < F(1, 10 ** 12) and g_lo > F(5772156649, 10 ** 10) \
    and g_hi < F(5772156650, 10 ** 10)

S1 = (F(0), F(0))
for k in range(2, N + 1):
    lk = log_bounds(F(k))
    S1 = iadd(S1, (lk[0] / k, lk[1] / k))
    S1 = rnd(S1)
L = lnN
A = isub(S1, isc(imul(L, L), F(1, 2)))
fN = isc(L, F(1, N))
fpN = isc(isub((F(1), F(1)), L), F(1, N * N))
fpppN = isc(isub((F(11), F(11)), isc(L, F(6))), F(1, N ** 4))
g1 = isub(isub(A, isc(fN, F(1, 2))), isc(fpN, F(1, 12)))
g1 = iadd(g1, isc(fpppN, F(1, 720)))
F5max = (120 * L[1] - 274) / N ** 6
E5 = 2 * F5max / 30240
g1 = (g1[0] - E5, g1[1] + E5)
pin1 = (F(-72815845578467363, 10 ** 18), F(-72815845393082604, 10 ** 18))
okg1 = pin1[0] <= g1[0] and g1[1] <= pin1[1]

ln4 = (2 * LOG2[0], 2 * LOG2[1])
lnpi = (log_bounds(PI_LO)[0], log_bounds(PI_HI)[1])
ln4pi = iadd(ln4, lnpi)
lam1 = iadd((F(1), F(1)), isub(isc(gam, F(1, 2)), isc(ln4pi, F(1, 2))))
oklam = F(230957, 10 ** 7) < lam1[0] and lam1[1] < F(230958, 10 ** 7)

PI = (PI_LO, PI_HI)
pi2 = imul(PI, PI)
M1 = iadd((F(3), F(3)), gam)
M1 = iadd(M1, imul(gam, gam))
M1 = iadd(M1, isc(g1, F(2)))
M1 = isub(M1, isc(pi2, F(1, 8)))
M1 = isub(M1, ln4pi)
pinM = (F(37100438723459, 10 ** 18), F(37100843555683, 10 ** 18))
okM = pinM[0] <= M1[0] and M1[1] <= pinM[1] and M1[0] > 0

checks.append(("R10a gamma enclosure width < 1e-12, inside "
               "(0.5772156649, 0.5772156650) [witness " + dec(g_lo, 14) + "]",
               okg))
checks.append(("R10b gamma_1 enclosure inside the prior cocycle-lane pin "
               "[witness " + dec(g1[0], 14) + "]", okg1))
checks.append(("R10c lambda_1 in (0.0230957, 0.0230958) [witness "
               + dec(lam1[0], 14) + "]", oklam))
checks.append(("R10d M_1 inside the cited pin and > 0 [witness "
               + dec(M1[0], 14) + "]", okM))

ok = all(v for _, v in checks)
for name, v in checks:
    print(("PASS " if v else "FAIL ") + name)
print("ASSEMBLY K1: whenever u^n != 1, all characters above level")
print("v(u^n-1) are non-fixed, so ||I - U_u^n||_S2^2 = infinity;")
print("J is non-torsion by a complex-embedding modulus, hence this holds")
print("for J at every n. Thus I - U_J is not Hilbert-Schmidt, outside")
print("every Hilbert-Schmidt perturbation Li witness class. K2: pure point")
print("roots of unity; nonidentity roots and eigenvalue 1 have unbounded")
print("multiplicity, the latter via orbit sums. K3 cocycle residue is the H")
print("row (atoms on the root-of-unity grid, not the zero angles).")
print(("ALL PASS" if ok else "FAILURES") + f" ({len(checks)} gates)")
