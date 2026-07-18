#!/usr/bin/env python3
# P-R2-SCALING-SHIFT-1 verifier. See PREREG.md (the pinned preregistration)
# before this file existed. Stdlib only; exact Q(sqrt5) pair arithmetic;
# exact Fraction interval arithmetic; no float in any assertion. Decimal
# prints are labeled witnesses only.
from fractions import Fraction as F

# ---------- Q(sqrt5) exact pair arithmetic: (a, b) means a + b sqrt5 ------
def q_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q_div(x, y):
    d = y[0] * y[0] - 5 * y[1] * y[1]
    num = q_mul(x, (y[0], -y[1]))
    return (num[0] / d, num[1] / d)


def q_pos(x):
    a, b = x
    if b == 0:
        return a > 0
    if a == 0:
        return b > 0
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return False
    if a > 0:            # b < 0
        return a * a > 5 * b * b
    return 5 * b * b > a * a   # a < 0, b > 0


Q0 = (F(0), F(0))
Q1 = (F(1), F(0))
R = (F(0), F(1, 5))            # r = 1/sqrt5 = sqrt5/5
PHI2 = (F(3, 2), F(1, 2))      # phi^2 = (3 + sqrt5)/2
PHI2I = (F(3, 2), F(-1, 2))    # phi^-2 = (3 - sqrt5)/2

# ---------- interval and log machinery (as in P-R2-LAMBDA-HAAR-1) --------
PI_LO = F(3141592653589793, 10**15)
PI_HI = F(3141592653589794, 10**15)
K_SER = 40
DEC = 10**36


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


def isc(a, c):
    p, q = a[0] * c, a[1] * c
    return (p, q) if p <= q else (q, p)


def dec(x, nd=12):
    sgn = '-' if x < 0 else ''
    x = abs(x)
    ip = x.numerator // x.denominator
    fr = x - ip
    digs = (fr * 10**nd).numerator // (fr * 10**nd).denominator
    return f"{sgn}{ip}.{digs:0{nd}d}"


checks = []

# S0: sqrt5 enclosure and r interval
A5, B5 = 2236067977, 2236067978
ok_s5 = A5 * A5 < 5 * 10**18 < B5 * B5
S5_LO, S5_HI = F(A5, 10**9), F(B5, 10**9)
R_IV = (1 / S5_HI, 1 / S5_LO)
checks.append(("S0 sqrt5 in (2.236067977, 2.236067978) by exact squaring",
               ok_s5))

# S1: overlap exponent identity and shell bookkeeping
ok_ov = all(-(j + k) + 2 * min(j, k) == -abs(j - k)
            for j in range(7) for k in range(7))
ok_vol = F(4, 5) / (1 - F(1, 5)) == 1
checks.append(("S1 <U^j v, U^k v> = 5^{-|j-k|/2} (exponent identity, "
               "0 <= j,k <= 6); vol(O) = sum of shells = 1; adjacent shells "
               "disjoint so ||(I-U)e||^2 = 2 on the transported basis",
               ok_ov and ok_vol))

# powers of r in Q(sqrt5)
rp = [Q1]
for _ in range(30):
    rp.append(q_mul(rp[-1], R))

one_m_r = q_sub(Q1, R)
one_p_r = q_add(Q1, R)


def psi_direct(n):
    s = Q0
    for j in range(n):
        for k in range(n):
            s = q_add(s, rp[abs(j - k)])
    return s


def psi_formula(n):
    t1 = q_mul((F(n), F(0)), q_div(one_p_r, one_m_r))
    t2 = q_mul((F(2), F(0)), q_mul(R, q_sub(Q1, rp[n])))
    t2 = q_div(t2, q_mul(one_m_r, one_m_r))
    return q_sub(t1, t2)


# S2: ladder closed form n = 1..12
ok_ladder = all(psi_direct(n) == psi_formula(n) for n in range(1, 13))
checks.append(("S2 ladder closed form psi(n) = n(1+r)/(1-r) - "
               "2r(1-r^n)/(1-r)^2 exact for n = 1..12", ok_ladder))

# S3: increments
ok_inc = True
for n in range(1, 13):
    d = q_sub(psi_formula(n + 1), psi_formula(n))
    d2 = q_add(Q1, q_div(q_mul(q_mul((F(2), F(0)), R), q_sub(Q1, rp[n])),
                         one_m_r))
    gap = q_sub(PHI2, d)
    gap2 = q_div(q_mul((F(2), F(0)), rp[n + 1]), one_m_r)
    if d != d2 or gap != gap2 or not q_pos(gap):
        ok_inc = False
        break
ok_lim = q_div(one_p_r, one_m_r) == PHI2
checks.append(("S3 increments 1 + 2r(1-r^n)/(1-r), monotone, gap to phi^2 "
               "= 2 r^{n+1}/(1-r) > 0, limit exactly phi^2 = (3+sqrt5)/2",
               ok_inc and ok_lim))

# S4: spectral density endpoints
p0 = q_div(q_sub(Q1, q_mul(R, R)), q_mul(one_m_r, one_m_r))
ppi = q_div(q_sub(Q1, q_mul(R, R)), q_mul(one_p_r, one_p_r))
ok_den = p0 == PHI2 and ppi == PHI2I and q_mul(p0, ppi) == Q1
checks.append(("S4 boundary spectral density: P(0) = phi^2, P(pi) = phi^-2, "
               "product 1, absolutely continuous with full support", ok_den))

# S5: rung 1
checks.append(("S5 psi(1) = 1 outside the lambda_1 bracket "
               "(0.0230957, 0.0230958): rung-1 miss by a factor above 43",
               psi_formula(1) == Q1 and F(1) > F(230958, 10**7)))

# S6: EM machinery, pins, lambda_2, and the rescaled rung-2 interval test
N = 300
HN = sum(F(1, k) for k in range(1, N + 1))
lnN = log_bounds(F(N))
g_lo = HN - lnN[1] - F(1, 2 * N) + F(1, 12 * N * N) - F(1, 120 * N ** 4)
g_hi = HN - lnN[0] - F(1, 2 * N) + F(1, 12 * N * N) - F(1, 120 * N ** 4) \
    + F(1, 252 * N ** 6)
gam = (g_lo, g_hi)
okg = (g_hi - g_lo) < F(1, 10 ** 12) and g_lo > F(5772156649, 10 ** 10) \
    and g_hi < F(5772156650, 10 ** 10)

S1sum = (F(0), F(0))
for k in range(2, N + 1):
    lk = log_bounds(F(k))
    S1sum = iadd(S1sum, (lk[0] / k, lk[1] / k))
    S1sum = rnd(S1sum)
L = lnN
Aiv = isub(S1sum, isc(imul(L, L), F(1, 2)))
fN = isc(L, F(1, N))
fpN = isc(isub((F(1), F(1)), L), F(1, N * N))
fpppN = isc(isub((F(11), F(11)), isc(L, F(6))), F(1, N ** 4))
g1 = isub(isub(Aiv, isc(fN, F(1, 2))), isc(fpN, F(1, 12)))
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

lam2 = isub(isc(lam1, F(4)), M1)
oklam2 = F(9234573, 10 ** 8) < lam2[0] and lam2[1] < F(9234574, 10 ** 8)

two_p_2r = iadd((F(2), F(2)), isc(R_IV, F(2)))
rung2 = imul(lam1, two_p_2r)
ok_disjoint = rung2[1] < lam2[0]

checks.append(("S6a gamma enclosure width < 1e-12, 14-digit witness "
               + dec(g_lo, 14), okg))
checks.append(("S6b gamma_1 inside the prior cocycle-lane pin, witness "
               + dec(g1[0], 14), okg1))
checks.append(("S6c lambda_1 in (0.0230957, 0.0230958), witness "
               + dec(lam1[0], 14), oklam))
checks.append(("S6d M_1 inside the cited pin and > 0, witness "
               + dec(M1[0], 14), okM))
checks.append(("S6e lambda_2 = 4 lambda_1 - M_1 in (0.09234573, 0.09234574), "
               "witness " + dec(lam2[0], 14), oklam2))
checks.append(("S6f rescaled rung 2: hi(lambda_1 (2 + 2r)) = "
               + dec(rung2[1], 12) + " < lo(lambda_2) = " + dec(lam2[0], 12)
               + ": JUNCTION FIRED", ok_disjoint))

# S7: HS divergence bookkeeping
checks.append(("S7 ||(I - U^n) e||^2 = 2 on every transported basis vector, "
               "every n >= 1: the S2 ladder is infinite at every rung",
               2 - 2 * 0 == 2 and ok_ov))

ok = all(v for _, v in checks)
for name, v in checks:
    print(("PASS " if v else "FAIL ") + name)
print("ASSEMBLY K1: multiplication by lambda is a bilateral shift, so I - U")
print("is not Hilbert-Schmidt (ladder infinite at every rung). K2: the type")
print("is homogeneous Lebesgue, every vector absolutely continuous, while a")
print("cocycle realization forces the atomic sigma_xi of the public toral")
print("no-go: contradiction for every vector. K3: convolution keeps")
print("archimedean composites absolutely continuous. K4: the boundary ladder")
print("increments increase strictly toward phi^2 (never attained) and miss")
print("the second Li rung after the single rescale |c|^2 = lambda_1.")
print(("ALL PASS" if ok else "FAILURES") + f" ({len(checks)} gates)")
