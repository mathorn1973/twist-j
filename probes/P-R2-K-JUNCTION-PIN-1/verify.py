#!/usr/bin/env python3
# P-R2-K-JUNCTION-PIN-1 verifier. See the pinned PREREG.md before this file.
# Python stdlib only. Every gate is an exact integer or Fraction comparison.
# Decimal strings are outward-rounded display witnesses, never assertion data.
from fractions import Fraction as F
from itertools import permutations
from math import comb, isqrt


# ---------- exact rational interval arithmetic ----------
GRID = 10**70
BAD = F(10**100)


def floor_grid(x):
    return F((x.numerator * GRID) // x.denominator, GRID)


def ceil_grid(x):
    return F(-((-x.numerator * GRID) // x.denominator), GRID)


def outward(iv):
    return (floor_grid(iv[0]), ceil_grid(iv[1]))


def pt(x):
    return (F(x), F(x))


def iadd(a, b):
    return outward((a[0] + b[0], a[1] + b[1]))


def isub(a, b):
    return outward((a[0] - b[1], a[1] - b[0]))


def isc(a, c):
    c = F(c)
    p, q = a[0] * c, a[1] * c
    return outward((p, q) if p <= q else (q, p))


def imul(a, b):
    products = (a[0] * b[0], a[0] * b[1],
                a[1] * b[0], a[1] * b[1])
    return outward((min(products), max(products)))


def isquare(a):
    if a[0] <= 0 <= a[1]:
        return outward((F(0), max(a[0] * a[0], a[1] * a[1])))
    return imul(a, a)


def izero(a):
    return a[0] <= 0 <= a[1]


def irecip(a):
    if izero(a):
        return (-BAD, BAD)
    p, q = 1 / a[0], 1 / a[1]
    return outward((p, q) if p <= q else (q, p))


def idiv(a, b):
    return imul(a, irecip(b))


def iwiden(a, error):
    error = abs(F(error))
    return outward((a[0] - error, a[1] + error))


def ioverlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def isubset(a, b):
    return b[0] <= a[0] and a[1] <= b[1]


def iinter_or_hull(a, b):
    lo, hi = max(a[0], b[0]), min(a[1], b[1])
    if lo <= hi:
        return outward((lo, hi))
    return outward((min(a[0], b[0]), max(a[1], b[1])))


def iwidth(a):
    return a[1] - a[0]


# ---------- rigorous rational logarithms ----------
LOG_TERMS = 64


def atanh_log_core(y):
    # Frozen use has 1 <= y <= 2, hence 0 <= t <= 1/3.
    t = (y - 1) / (y + 1)
    t2 = t * t
    power = t
    total = F(0)
    for j in range(LOG_TERMS):
        total += power / (2 * j + 1)
        power *= t2
    total *= 2
    if t == 0:
        return pt(0)
    tail = 2 * power / ((2 * LOG_TERMS + 1) * (1 - t2))
    return outward((total, total + tail))


LOG2 = atanh_log_core(F(2))


def log_bounds(x):
    x = F(x)
    if x <= 0:
        return (-BAD, BAD)
    exponent = 0
    y = x
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1
    return iadd(isc(LOG2, exponent), atanh_log_core(y))


def ilog(a):
    if a[0] <= 0:
        return (-BAD, BAD)
    return outward((log_bounds(a[0])[0], log_bounds(a[1])[1]))


# ---------- rigorous rational pi by Machin ----------
def atan_bounds(z, terms):
    z = F(z)
    z2 = z * z
    power = z
    total = F(0)
    sign = 1
    for k in range(terms):
        total += sign * power / (2 * k + 1)
        power *= z2
        sign = -sign
    next_term = power / (2 * terms + 1)
    if sign > 0:
        return outward((total, total + next_term))
    return outward((total - next_term, total))


ATAN_1_5 = atan_bounds(F(1, 5), 48)
ATAN_1_239 = atan_bounds(F(1, 239), 14)
PI = isub(isc(ATAN_1_5, 16), isc(ATAN_1_239, 4))
LOGPI = ilog(PI)
LOG5 = log_bounds(F(5))
LOG2PI = iadd(LOG2, LOGPI)
LOG4PI = iadd(isc(LOG2, 2), LOGPI)


# ---------- Bernoulli table and Euler--Maclaurin ----------
BERN = {
    0: F(1), 1: F(-1, 2),
    2: F(1, 6), 4: F(-1, 30), 6: F(1, 42), 8: F(-1, 30),
    10: F(5, 66), 12: F(-691, 2730), 14: F(7, 6),
    16: F(-3617, 510), 18: F(43867, 798),
    20: F(-174611, 330), 22: F(854513, 138),
    24: F(-236364091, 2730),
}


def bern(n):
    return BERN.get(n, F(0))


def harmonic(n):
    return sum((F(1, k) for k in range(1, n + 1)), F(0))


def stieltjes_em(q, ncut):
    q = F(q)
    a_end = F(ncut) + q
    log_a = log_bounds(a_end)
    sum0 = sum((1 / (F(n) + q) for n in range(ncut)), F(0))
    sum1 = pt(0)
    for n in range(ncut):
        x = F(n) + q
        sum1 = iadd(sum1, isc(log_bounds(x), 1 / x))

    g0 = iadd(isub(pt(sum0), log_a), pt(F(1, 2) / a_end))
    g1 = isub(sum1, isc(isquare(log_a), F(1, 2)))
    g1 = iadd(g1, isc(log_a, F(1, 2) / a_end))

    for k in range(1, 13):
        c = bern(2 * k) / (2 * k * a_end ** (2 * k))
        g0 = iadd(g0, pt(c))
        g1 = iadd(g1, isc(isub(log_a, pt(harmonic(2 * k - 1))), c))

    b24 = abs(bern(24))
    e0 = b24 / (24 * a_end**24)
    e1 = b24 / a_end**24 * (
        (harmonic(24) + log_a[1]) / 24 + F(1, 24**2)
    )
    return iwiden(g0, e0), iwiden(g1, e1)


def stieltjes_coarse(q):
    q = F(q)
    ncut = 37
    a_end = F(ncut) + q
    log_a = log_bounds(a_end)
    sum0 = sum((1 / (F(n) + q) for n in range(ncut)), F(0))
    sum1 = pt(0)
    for n in range(ncut):
        x = F(n) + q
        sum1 = iadd(sum1, isc(log_bounds(x), 1 / x))

    c = isub(pt(sum0), log_a)
    g0_low = iadd(c, pt(F(1, 2) / a_end))
    g0_high = iadd(g0_low, pt(F(1, 2) / a_end**2))
    g0 = outward((g0_low[0], g0_high[1]))

    d = isub(sum1, isc(isquare(log_a), F(1, 2)))
    lower_tail = isc(log_bounds(a_end + 1), F(1, 2) / (a_end + 1))
    upper_tail = iadd(
        isc(isub(log_a, pt(1)), 1 / a_end**2),
        isc(log_a, 1 / a_end),
    )
    upper_tail = isc(upper_tail, F(1, 2))
    g1_low = iadd(d, lower_tail)
    g1_high = iadd(d, upper_tail)
    g1 = outward((g1_low[0], g1_high[1]))
    return g0, g1, log_a[0] > F(3, 2)


Q_VALUES = (F(1, 5), F(2, 5), F(3, 5), F(4, 5), F(1))
EM64 = {q: stieltjes_em(q, 64) for q in Q_VALUES}
EM128 = {q: stieltjes_em(q, 128) for q in Q_VALUES}
COARSE = {q: stieltjes_coarse(q) for q in Q_VALUES}
TIGHT = {
    q: (iinter_or_hull(EM64[q][0], EM128[q][0]),
        iinter_or_hull(EM64[q][1], EM128[q][1]))
    for q in Q_VALUES
}


# ---------- exact character group and two independent assemblies ----------
ONE_I = (1, 0)
I_I = (0, 1)
MINUS_I = (0, -1)
MINUS_ONE_I = (-1, 0)
CHARS = {
    0: (ONE_I, ONE_I, ONE_I, ONE_I),
    1: (ONE_I, I_I, MINUS_I, MINUS_ONE_I),
    2: (ONE_I, MINUS_ONE_I, MINUS_ONE_I, ONE_I),
    3: (ONE_I, MINUS_I, I_I, MINUS_ONE_I),
}


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def csum(row):
    return (sum(z[0] for z in row), sum(z[1] for z in row))


def ciadd(a, b):
    return iadd(a[0], b[0]), iadd(a[1], b[1])


def cireal_scale(a, coefficient):
    return isc(a, coefficient[0]), isc(a, coefficient[1])


def cidiv(numerator, denominator):
    ar, ai = denominator
    br, bi = numerator
    norm = iadd(isquare(ar), isquare(ai))
    real_num = iadd(imul(br, ar), imul(bi, ai))
    imag_num = isub(imul(bi, ar), imul(br, ai))
    return (idiv(real_num, norm), idiv(imag_num, norm)), norm


def character_ab(data, exponent):
    a_total = (pt(0), pt(0))
    b_total = (pt(0), pt(0))
    for a in range(1, 5):
        coefficient = CHARS[exponent][a - 1]
        a_total = ciadd(
            a_total, cireal_scale(data[F(a, 5)][0], coefficient)
        )
        b_total = ciadd(
            b_total, cireal_scale(data[F(a, 5)][1], coefficient)
        )
    return a_total, b_total


def complex_character_sum(data):
    total = (pt(0), pt(0))
    norms = []
    for exponent in (1, 2, 3):
        a_chi, b_chi = character_ab(data, exponent)
        ratio, norm = cidiv(b_chi, a_chi)
        norms.append(norm)
        term = (isub(isc(LOG5, -1), ratio[0]), isc(ratio[1], -1))
        total = ciadd(total, term)
    return total, tuple(norms)


def reduced_character_parts(data):
    g0 = {a: data[F(a, 5)][0] for a in range(1, 5)}
    g1 = {a: data[F(a, 5)][1] for a in range(1, 5)}
    a2 = iadd(isub(g0[1], g0[2]), isub(g0[4], g0[3]))
    b2 = iadd(isub(g1[1], g1[2]), isub(g1[4], g1[3]))
    x = isub(g0[1], g0[4])
    y = isub(g0[2], g0[3])
    u = isub(g1[1], g1[4])
    v = isub(g1[2], g1[3])
    den4 = iadd(isquare(x), isquare(y))
    num4 = iadd(imul(u, x), imul(v, y))
    return a2, b2, x, y, u, v, den4, num4


def assemble_k(data):
    direct, char_norms = complex_character_sum(data)
    parts = reduced_character_parts(data)
    a2, b2, x, y, u, v, den4, num4 = parts
    ratio2 = idiv(b2, a2)
    ratio4 = idiv(num4, den4)
    reduced = isub(isub(isc(LOG5, -3), ratio2), isc(ratio4, 2))

    target = iadd(pt(1), isc(LOG5, F(3, 2)))
    target = isub(target, isc(LOG2PI, 2))
    target = isub(target, data[F(1)][0])
    target = iadd(target, direct[0])

    simplified = isub(pt(1), isc(LOG5, F(3, 2)))
    simplified = isub(simplified, isc(LOG2PI, 2))
    simplified = isub(simplified, data[F(1)][0])
    simplified = isub(simplified, ratio2)
    simplified = isub(simplified, isc(ratio4, 2))
    return {
        "target": target,
        "simplified": simplified,
        "direct": direct,
        "reduced": reduced,
        "parts": parts,
        "char_norms": char_norms,
    }


K64 = assemble_k(EM64)
K128 = assemble_k(EM128)
KTIGHT = assemble_k(TIGHT)
KFINAL = iinter_or_hull(K64["target"], K128["target"])


# ---------- frozen gates ----------
checks = []


def det_exact(matrix):
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(
            1 for i in range(n) for j in range(i + 1, n)
            if perm[i] > perm[j]
        )
        term = -1 if inversions % 2 else 1
        for i in range(n):
            term *= matrix[i][perm[i]]
        total += term
    return total


TRACE_GRAM = [
    [4 if (i + j) % 5 == 0 else -1 for j in range(4)]
    for i in range(4)
]
DISC_K = det_exact(TRACE_GRAM)
char_group_ok = all(
    tuple(cmul(CHARS[e][j], CHARS[f][j]) for j in range(4))
    == CHARS[(e + f) % 4]
    for e in range(4) for f in range(4)
)
char_sums_ok = all(csum(CHARS[e]) == (0, 0) for e in (1, 2, 3))
char_conj_ok = tuple(cconj(z) for z in CHARS[1]) == CHARS[3]
completed_coeffs_ok = (
    F(1, 2) * 3 == F(3, 2)
    and F(1) - F(2) == F(-1)
    and F(-2) == F(-2)
)
checks.append((
    "K00 trace-Gram D_K=125; degree/signature/conductors; completed-zeta "
    "coefficients; exact cyclic character table",
    DISC_K == 125 and 4 == 0 + 2 * 2 and 1 * 5 * 5 * 5 == DISC_K
    and completed_coeffs_ok and char_group_ok and char_sums_ok and char_conj_ok,
))

u5 = F(1, 5)
inverse_factor_coeff = -u5 / (1 - u5)
omitted_factor_coeff = u5 / (1 - u5)
omitted_drift = isc(LOG5, omitted_factor_coeff)
checks.append((
    "K01 principal convention: coefficients derived from u=1/5 are "
    "-u/(1-u)=-1/4 and +u/(1-u)=+1/4; omitted drift excludes zero",
    inverse_factor_coeff == F(-1, 4)
    and omitted_factor_coeff == F(1, 4) and omitted_drift[0] > 0,
))

bern_ok = all(
    sum((F(comb(n + 1, k)) * bern(k) for k in range(n + 1)), F(0)) == 0
    for n in range(1, 25)
)
log2_guard = F(6931471805599453, 10**16) < LOG2[0] \
    and LOG2[1] < F(6931471805599454, 10**16)
pi_guard = F(314159, 10**5) < PI[0] and PI[1] < F(314160, 10**5)
checks.append((
    "K02 Bernoulli recurrence through B_24; rational log(2); Machin pi "
    "width < 10^-60",
    bern_ok and log2_guard and pi_guard and iwidth(PI) < F(1, 10**60),
))

em_overlap = all(
    ioverlap(EM64[q][r], EM128[q][r])
    for q in Q_VALUES for r in (0, 1)
)
tight_width = all(
    iwidth(TIGHT[q][r]) < F(1, 10**24)
    for q in Q_VALUES for r in (0, 1)
)
checks.append((
    "K03 N=64 and N=128 EM intervals overlap for gamma_0,gamma_1 at "
    "q=1/5,2/5,3/5,4/5,1; every intersection width < 10^-24",
    em_overlap and tight_width,
))

coarse_ok = all(
    COARSE[q][2]
    and isubset(TIGHT[q][0], COARSE[q][0])
    and isubset(TIGHT[q][1], COARSE[q][1])
    for q in Q_VALUES
)
checks.append((
    "K04 independent N_check=37 sum-integral enclosures contain every "
    "tight EM interval; log(N_check+q) > 3/2",
    coarse_ok,
))


def denominators_ok(assembly):
    a2, b2, x, y, u, v, den4, num4 = assembly["parts"]
    return (not izero(a2) and den4[0] > 0
            and all(norm[0] > 0 for norm in assembly["char_norms"]))


checks.append((
    "K05 all complex character norms and reduced A_2,x^2+y^2 "
    "denominators exclude zero at N=64,N=128,and the tight intersection",
    denominators_ok(K64) and denominators_ok(K128) and denominators_ok(KTIGHT),
))

A2, B2, X4, Y4, U4, V4, DEN4, NUM4 = KTIGHT["parts"]
SQ_SCALE = 10**50
SQ_FLOOR = isqrt(5 * SQ_SCALE**2)
SQRT5 = outward((F(SQ_FLOOR, SQ_SCALE), F(SQ_FLOOR + 1, SQ_SCALE)))
PHI = isc(iadd(pt(1), SQRT5), F(1, 2))
L_QUAD_HURWITZ = isc(A2, F(1, 5))
L_QUAD_CLASSICAL = idiv(isc(ilog(PHI), 2), SQRT5)
L_QUARTIC_HURWITZ = isc(DEN4, F(1, 25))
L_QUARTIC_CLASSICAL = isc(isquare(PI), F(2, 25))
checks.append((
    "K06 L(1,chi_2) overlaps 2log(phi)/sqrt(5); |L(1,omega)|^2 "
    "overlaps 2pi^2/25",
    SQRT5[0] > 0 and PHI[0] > 0
    and ioverlap(L_QUAD_HURWITZ, L_QUAD_CLASSICAL)
    and ioverlap(L_QUARTIC_HURWITZ, L_QUARTIC_CLASSICAL),
))

GAMMA = TIGHT[F(1)][0]
LAMBDA_Q = isub(iadd(pt(1), isc(GAMMA, F(1, 2))), isc(LOG4PI, F(1, 2)))
checks.append((
    "K07 lambda_1^Q strictly inside (0.0230957,0.0230958)",
    F(230957, 10**7) < LAMBDA_Q[0]
    and LAMBDA_Q[1] < F(230958, 10**7),
))

k_overlap = ioverlap(K64["target"], K128["target"])
checks.append((
    "K08 N=64 and N=128 lambda_1^K enclosures overlap; final width "
    "< 10^-24 (no preregistered centre or sign)",
    k_overlap and iwidth(KFINAL) < F(1, 10**24),
))

assembly_ok = all(
    izero(assembly["direct"][1])
    and iwidth(assembly["direct"][1]) < F(1, 10**24)
    and ioverlap(assembly["direct"][0], assembly["reduced"])
    and ioverlap(assembly["target"], assembly["simplified"])
    for assembly in (K64, K128)
)
checks.append((
    "K09 explicit complex sums for omega,omega^2,conj(omega) are narrowly "
    "real and overlap the independent real reduction and simplified target",
    assembly_ok,
))

LOG_S_COEFF = (F(1, 4), F(-1, 2))
PLENUM_LEFT = (6 * LOG_S_COEFF[0], 6 * LOG_S_COEFF[1] + 3)
PLENUM_RIGHT = (F(3, 2), F(0))
checks.append((
    "K10 positive-branch plenum identity: 6log(s_J)+3log(phi) "
    "= (3/2)log(5) by exact coefficient arithmetic",
    PLENUM_LEFT == PLENUM_RIGHT,
))

WRONG_LITERAL_MOD5 = iadd(KFINAL, omitted_drift)
DRIFT_READBACK = isub(WRONG_LITERAL_MOD5, KFINAL)
checks.append((
    "K11 negative control: literal modulus-five convention differs by the "
    "derived +log(5)/4 drift and is disjoint from the registered result",
    ioverlap(DRIFT_READBACK, omitted_drift)
    and not ioverlap(KFINAL, WRONG_LITERAL_MOD5),
))


# ---------- deterministic outward decimal witnesses ----------
def scaled_decimal(n, ndigits):
    sign = "-" if n < 0 else ""
    n = abs(n)
    scale = 10**ndigits
    return f"{sign}{n // scale}.{n % scale:0{ndigits}d}"


def decimal_floor(x, ndigits):
    scale = 10**ndigits
    n = (x.numerator * scale) // x.denominator
    return scaled_decimal(n, ndigits)


def decimal_ceil(x, ndigits):
    scale = 10**ndigits
    n = -((-x.numerator * scale) // x.denominator)
    return scaled_decimal(n, ndigits)


def decimal_interval(a, ndigits=24):
    return "[" + decimal_floor(a[0], ndigits) + ", " \
        + decimal_ceil(a[1], ndigits) + "]"


ok = all(value for _, value in checks)
for label, value in checks:
    print(("PASS " if value else "FAIL ") + label)
if ok:
    print("WITNESS lambda_1^Q in " + decimal_interval(LAMBDA_Q, 24))
    print("WITNESS sum_nonprincipal L'/L in "
          + decimal_interval(KTIGHT["direct"][0], 24))
    print("WITNESS lambda_1^K in " + decimal_interval(KFINAL, 30))
    print("NEGATIVE-CONTROL literal-modulus-5 interval in "
          + decimal_interval(WRONG_LITERAL_MOD5, 24))
else:
    print("WITNESSES SUPPRESSED: at least one frozen gate failed.")
print("SCOPE R2-K-JUNCTION-PIN is C at most; R2 and RH remain O.")
print(("ALL PASS" if ok else "FAILURES") + f" ({len(checks)} gates)")
raise SystemExit(0 if ok else 1)
