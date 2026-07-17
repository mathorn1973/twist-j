#!/usr/bin/env python3
"""Exact dictionary checks for C-LI-Q-MOMENT-1.

Non-formal, proof-audit verifier for the pole-chart (w = s(1-s)) moment
interface: the partial-fraction sigma dictionary, the ladder junction
qw_0 = lambda_1 and qw_1 = M_1, the Catalan chart reversion, the g-to-q
recursion and Moebius chart maps, double-Hankel discipline with the
Hamburger separator, the pentagon log-derivative coefficient identity at
the q-interface, and the counting dichotomy skeleton.

It does not assert Li's criterion, the Stieltjes moment theorem, the
Riemann-von Mangoldt law, the Lagarias asymptotic, nuclear singular
value decay, or any construction of a J-native moment functional.

Discipline: Python stdlib only; Fraction/integer arithmetic in every
asserted value; no files, network, subprocesses, floats, Decimal, or
libm anywhere.
"""

from fractions import Fraction as F
from math import comb

FAILED = []


def check(name, condition):
    print(("PASS " if condition else "FAIL ") + name)
    if not condition:
        FAILED.append(name)


# ---------------------------------------------------------------------------
# Dense polynomials over Q, little-endian coefficient lists.
# ---------------------------------------------------------------------------
def padd(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        if av == 0:
            continue
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [c * v for v in a]


def ppow(a, n):
    out = [F(1)]
    for _ in range(n):
        out = pmul(out, a)
    return out


def ptrunc(a, order):
    return a[:order + 1] + [F(0)] * max(0, order + 1 - len(a))


def pcompose_trunc(outer, inner, order):
    """outer(inner(t)) truncated to the given order; inner must have
    zero constant term."""
    assert len(inner) == 0 or inner[0] == 0
    result = [F(0)] * (order + 1)
    power = [F(1)]
    for k, c in enumerate(outer):
        if k > order:
            break
        if c != 0:
            for i, v in enumerate(power[:order + 1]):
                result[i] += c * v
        power = ptrunc(pmul(power, inner), order)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    out = F(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        pv = a[col][col]
        out *= pv
        for j in range(col, n):
            a[col][j] /= pv
        for r in range(col + 1, n):
            f = a[r][col]
            for j in range(col, n):
                a[r][j] -= f * a[col][j]
    return out


# ---------------------------------------------------------------------------
# Q1: partial-fraction sigma dictionary.
#     1/(x^m (1-x)^m) = sum_j binom(2m-1-j, m-j) (x^-j + (1-x)^-j),
#     verified with cleared denominators as a polynomial identity:
#     1 = sum_j binom(2m-1-j, m-j) (x^(m-j) (1-x)^m + x^m (1-x)^(m-j)).
# ---------------------------------------------------------------------------
ONE_MINUS_X = [F(1), F(-1)]
X = [F(0), F(1)]
ok = True
rows = []
for m in range(1, 7):
    rhs = [F(0)]
    row = []
    for j in range(1, m + 1):
        cmj = F(comb(2 * m - 1 - j, m - j))
        row.append(cmj)
        term1 = pmul(ppow(X, m - j), ppow(ONE_MINUS_X, m))
        term2 = pmul(ppow(X, m), ppow(ONE_MINUS_X, m - j))
        rhs = padd(rhs, pscale(padd(term1, term2), cmj))
    ok = ok and rhs == [F(1)]
    rows.append(row)
ok = ok and rows[0] == [F(1)] and rows[1] == [F(2), F(1)]
ok = ok and rows[2] == [F(6), F(3), F(1)]
ok = ok and rows[3] == [F(20), F(10), F(4), F(1)]
check("Q1 partial-fraction sigma dictionary rows, m=1..6, exact polynomial identity over Q", ok)
print("Q1 witness dictionary rows (sigma_1..sigma_m coefficients): "
      + "; ".join("m=%d: %s" % (m + 1, [int(c) for c in row])
                  for m, row in enumerate(rows[:4])))


# ---------------------------------------------------------------------------
# Q2: junction algebra in the frozen constant module.
#     Basis symbols: 1, gamma, gamma^2, gamma_1, pi^2, log4pi,
#     gamma^3, gamma*gamma_1, gamma_2, zeta3.
# ---------------------------------------------------------------------------
def vadd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def vscale(a, c):
    return {k: c * v for k, v in a.items() if c * v != 0}


SIGMA1 = {"1": F(1), "gamma": F(1, 2), "log4pi": F(-1, 2)}
SIGMA2 = {"1": F(1), "gamma^2": F(1), "gamma_1": F(2), "pi^2": F(-1, 8)}
SIGMA3 = {"1": F(1), "gamma^3": F(1), "gamma*gamma_1": F(3),
          "gamma_2": F(3, 2), "zeta3": F(-7, 8)}
LAMBDA1 = dict(SIGMA1)                          # lambda_1 = sigma_1
LAMBDA2 = vadd(vscale(SIGMA1, F(2)), vscale(SIGMA2, F(-1)))  # 2s1 - s2
M1_FROZEN = {"1": F(3), "gamma": F(1), "gamma^2": F(1),
             "gamma_1": F(2), "pi^2": F(-1, 8), "log4pi": F(-1)}

qw0 = dict(SIGMA1)
qw1 = vadd(vscale(SIGMA1, F(2)), SIGMA2)
qw2 = vadd(vadd(vscale(SIGMA1, F(6)), vscale(SIGMA2, F(3))), SIGMA3)
m1_via_lambda = vadd(vscale(LAMBDA1, F(4)), vscale(LAMBDA2, F(-1)))

ok = qw0 == LAMBDA1
ok = ok and qw1 == M1_FROZEN and m1_via_lambda == M1_FROZEN and qw1 == m1_via_lambda
ok = ok and qw2 == vadd(vadd(vscale(SIGMA1, F(6)), vscale(SIGMA2, F(3))), SIGMA3)
sh1_qw2_part = vadd(qw2, vscale(SIGMA3, F(-1)))  # 6 sigma_1 + 3 sigma_2
ok = ok and sh1_qw2_part == vadd(vscale(SIGMA1, F(6)), vscale(SIGMA2, F(3)))
check("Q2 junction algebra: qw_0 = sigma_1 = lambda_1; qw_1 = 2 sigma_1 + sigma_2 = M_1 = 4 lambda_1 - lambda_2; qw_2 row exact", ok)
print("Q2 witness qw_1 vector: " + repr(sorted((k, str(v)) for k, v in qw1.items())))


# ---------------------------------------------------------------------------
# Q3: Catalan reversion of w = -t - t^2 through order 10.
# ---------------------------------------------------------------------------
CATALAN = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
W_OF_T = [F(0), F(-1), F(-1)]                     # w(t) = -t - t^2
T_OF_W = [F(0)] + [F(-CATALAN[k - 1]) for k in range(1, 11)]
ORDER = 10
ok = pcompose_trunc(W_OF_T, T_OF_W, ORDER) == [F(0), F(1)]
ok = ok and pcompose_trunc(T_OF_W, W_OF_T, ORDER) == [F(0), F(1)]
check("Q3 Catalan reversion: w(t(w)) = w and t(w(t)) = t through order 10, exact", ok)


# ---------------------------------------------------------------------------
# Q4: g-to-q recursion, power sums, Moebius chart maps, scaling covariance.
# ---------------------------------------------------------------------------
def power_sums(bs, depth):
    return [sum(b ** (n + 1) for b in bs) for n in range(depth)]


def g_poly(bs):
    g = [F(1)]
    for b in bs:
        g = pmul(g, [F(1), -b])
    return g


def q_from_recursion(g, depth):
    q = []
    for n in range(depth):
        gn1 = g[n + 1] if n + 1 < len(g) else F(0)
        val = -F(n + 1) * gn1
        for k in range(1, n + 1):
            gk = g[k] if k < len(g) else F(0)
            val -= gk * q[n - k]
        q.append(val)
    return q


ok = True
SPECTRA = [
    [F(1, 2), F(2, 3), F(3, 7), F(2, 9)],
    [F(2), F(2), F(5)],
]
for bs in SPECTRA:
    depth = 9
    q_ps = power_sums(bs, depth)
    q_rec = q_from_recursion(g_poly(bs), depth)
    ok = ok and q_ps == q_rec
    # Moebius chart maps, eigenvalue-wise, both directions.
    for b in bs:
        a = b / (1 - b / 4)
        ok = ok and a / (1 + a / 4) == b
        y = 1 / b
        ok = ok and y - F(1, 4) == 1 / a
    # scaling covariance
    c = F(2, 3)
    q_sc = power_sums([c * b for b in bs], 7)
    ok = ok and all(q_sc[n] == c ** (n + 1) * q_ps[n] for n in range(7))
check("Q4 g-to-q recursion = power sums; Moebius maps b<->a exact and involutive; scaling covariance q_n -> c^(n+1) q_n", ok)


# ---------------------------------------------------------------------------
# Q5: double-Hankel discipline.
# ---------------------------------------------------------------------------
def hankel(q, shift, size):
    return [[q[i + j + shift] for j in range(size)] for i in range(size)]


ok = True
# (i) positive two-atom instance: eta = 1*delta(1/2) + 2*delta(1/3).
q_pos = [F(1, 2) ** (n + 1) + 2 * F(1, 3) ** (n + 1) for n in range(8)]
for shift in (0, 1):
    d1 = determinant(hankel(q_pos, shift, 1))
    d2 = determinant(hankel(q_pos, shift, 2))
    d3 = determinant(hankel(q_pos, shift, 3))
    ok = ok and d1 > 0 and d2 > 0 and d3 == 0
# (ii) Hamburger separator: moments of delta(+1) + delta(-1).
q_ham = [F(1) + F(-1) ** n for n in range(8)]
h0_minors = [determinant(hankel(q_ham, 0, k)) for k in (1, 2, 3)]
h1_2x2 = determinant(hankel(q_ham, 1, 2))
ok = ok and all(d >= 0 for d in h0_minors) and h1_2x2 < 0
# (iii) signed instance fires H^(0) itself.
q_sgn = [F(1) - F(1, 10) * F(1, 2) ** (n + 1) for n in range(4)]
ok = ok and determinant(hankel(q_sgn, 0, 2)) < 0
check("Q5 double-Hankel discipline: positive instance (rank witness), Hamburger separator passes H0 and fires H1, signed instance fires H0", ok)
print("Q5 witness H0 minors of separator: %s ; H1 2x2 det: %s ; signed H0 2x2 det: %s"
      % ([str(d) for d in h0_minors], h1_2x2, determinant(hankel(q_sgn, 0, 2))))


# ---------------------------------------------------------------------------
# Q6: pentagon log-derivative coefficient identity through n = 125,
#     exact in the free Q-module over {log p}.
#     -P0'/P0 coefficients from c(n) = 5*[5|n] - 1 alone must equal
#     Lambda(n) - (log 5) * n * [n = 5^m].
# ---------------------------------------------------------------------------
N6 = 125


def factorize(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


c_coeff = {n: F(4) if n % 5 == 0 else F(-1) for n in range(1, N6 + 1)}
# Dirichlet inverse of P0 (rational coefficients).
inv = {1: 1 / c_coeff[1]}
for n in range(2, N6 + 1):
    acc = F(0)
    for d in range(1, n):
        if n % d == 0:
            acc += inv[d] * c_coeff[n // d]
    inv[n] = -acc / c_coeff[1]
# -P0' has log-vector coefficients c(n) * log n.
neg_p0_prime = {}
for n in range(1, N6 + 1):
    vec = {}
    for p, e in factorize(n).items():
        vec["log%d" % p] = c_coeff[n] * e
    neg_p0_prime[n] = {k: v for k, v in vec.items() if v != 0}
# X = (-P0') * P0^(-1) by Dirichlet convolution.
ok = True
for n in range(1, N6 + 1):
    xvec = {}
    for d in range(1, n + 1):
        if n % d == 0:
            for k, v in neg_p0_prime[d].items():
                val = v * inv[n // d]
                if val != 0:
                    xvec[k] = xvec.get(k, F(0)) + val
    xvec = {k: v for k, v in xvec.items() if v != 0}
    fac = factorize(n)
    target = {}
    if len(fac) == 1:
        p = next(iter(fac))
        target["log%d" % p] = F(1)
        if p == 5:
            target["log5"] = F(1) - F(n)
    target = {k: v for k, v in target.items() if v != 0}
    ok = ok and xvec == target
check("Q6 pentagon stream at the q-interface: coeff(-P0'/P0)(n) = Lambda(n) - (log 5) n [n=5^m] for all n <= 125, exact over the {log p} module", ok)
print("Q6 witness n=5, 25, 125 coefficients of log5: -4, -24, -124 expected; "
      "identity checked coefficientwise")


# ---------------------------------------------------------------------------
# Q7: counting dichotomy skeleton on exact integers (restricted scope:
#     finite skeleton only).  Geometric spectrum b_k = 4^-k gives
#     N(4^-M) = M; the log-polynomial reference shape b_j = (L(j)/j)^2,
#     L(j) = 1 + floor(log2 j), gives N(4^-M) >= M * 2^M on the window.
# ---------------------------------------------------------------------------
def L(j):
    return j.bit_length()


ok = True
for M in range(2, 13):
    n_geo = sum(1 for k in range(1, 4 * M) if F(1, 4 ** k) >= F(1, 4 ** M))
    ok = ok and n_geo == M
    bound = 2 ** M
    n_ref = 0
    j = 1
    limit = bound * (M + 4)
    while j <= limit:
        if j <= bound * L(j):
            n_ref += 1
        j += 1
    ok = ok and n_ref >= M * 2 ** M
check("Q7 counting dichotomy skeleton: geometric N(4^-M) = M exactly; log-polynomial shape N(4^-M) >= M 2^M for M = 2..12 (finite skeleton, restricted scope)", ok)


print("IMPORTED: Hadamard pairing; Stieltjes moment theorem; Riemann-von Mangoldt count; Lagarias asymptotic; nuclear singular-value decay; classical sigma_1..sigma_3 closed forms")
print("NONCLAIM: no J-native A_J/B_J or moment functional is constructed; SH-1 is frozen, not evaluated; G8 and RH remain open")
print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS C-LI-Q-MOMENT-1 dictionary" if not FAILED else "FAIL"))

raise SystemExit(1 if FAILED else 0)
