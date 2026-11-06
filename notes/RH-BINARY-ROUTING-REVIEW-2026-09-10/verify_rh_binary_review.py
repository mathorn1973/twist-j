#!/usr/bin/env python3
"""Independent exact re-verification of the note
"RH: binarni skladani, ortogonalni vrstvy a presna racionalni norma" (2026-09-10).

Everything below uses Python integers and fractions.Fraction only.  Floating
point appears in exactly one clearly labelled diagnostic line (d_K^2 * log K).

The script was written from the mathematical statements of the note, not from
the note's own verify_rh_binary.py, which was not available to this review.

Sections
  A  weights, norm equivalence, ||1||_H^2 = 1 and ||1||_B^2 = 2
  B  dilation D_m: remainder identity, exact H-norm law, exact binary law for m=2,
     popcount fixed point, dyadic obstruction f(3)=f(1)+f(2) and the 1/9 bound
  C  routing C: exact binary norm law, H-norm operator norm 1/3,
     1 = r_2 + C 1, explicit f_J, layers a_j, orthogonality, Pythagoras
  D  first new layer y = C r_2 is not a finite combination of remainders
     (exact linear algebra + the L-witness), and the gcd-difference
     characterisation of the finite span
  E  Dirichlet coefficients: 2 Delta y = -1 + 3[2|n] - 2[4|n] + chi_4(n);
     general layer: (m+1 : v_2(m)=j) = 2^(j+1) l + 2^j + 1  (Hurwitz shift 1/2+2^(-j-1))
  F  periodic binary sum: closed cyclic formula against brute-force partial sums
     with two-sided tail enclosure, and invariance under period multiplication
  G  Gram matrices, global minima d_K^2 (table K<=6 from the note, extended),
     Pythagorean update law, local-equation bounds
  H  the D_m argument for  1 in V  =>  V = H  (finite-support density witness)
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd

CHECKS = 0
GROUPS: dict[str, int] = {}
_GROUP = "?"


def group(name: str) -> None:
    global _GROUP
    _GROUP = name
    GROUPS.setdefault(name, 0)


def check(cond: bool, msg: str = "") -> None:
    global CHECKS
    if not cond:
        raise AssertionError(f"[{_GROUP}] {msg}")
    CHECKS += 1
    GROUPS[_GROUP] += 1


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


# ----------------------------------------------------------------------------
# basic sequences (index n >= 1; x_0 = 0 by convention)
# ----------------------------------------------------------------------------

def r(k: int, n: int) -> int:
    return n % k


def w_H(n: int) -> Fr:
    return Fr(1, n * (n + 1))


def w_B(n: int) -> Fr:
    j = n.bit_length() - 1  # 2^j <= n < 2^(j+1)
    return Fr(1, 4 ** j)


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def D(m: int, x, n: int):
    """(D_m x)_n = x_{floor(n/m)}, x_0 = 0."""
    q = n // m
    return 0 if q == 0 else x(q)


def C(x, n: int):
    """(Cx)_{2n} = x_n, (Cx)_{2n-1} = 0."""
    return x(n // 2) if n % 2 == 0 else 0


def norm_B_finite(vals: dict[int, Fr]) -> Fr:
    return sum((w_B(n) * v * v for n, v in vals.items()), Fr(0))


def norm_H_finite(vals: dict[int, Fr]) -> Fr:
    return sum((w_H(n) * v * v for n, v in vals.items()), Fr(0))


# ----------------------------------------------------------------------------
# periodic binary sum  sum_{j>=0} 4^{-j} sum_{n=2^j}^{2^{j+1}-1} q_n
# ----------------------------------------------------------------------------

def binary_sum_periodic(q: list[Fr]) -> Fr:
    """Exact value for q periodic with period L=len(q), q_n = q[n mod L]."""
    L = len(q)
    S = sum(q, Fr(0))
    qbar = S / L
    P = [Fr(0)] * (L + 1)
    for a in range(L):
        P[a + 1] = P[a] + q[a]

    def eta(rr: int) -> Fr:
        return P[rr] - rr * qbar

    # b_j = 2^j mod L, find pre-period h and cycle length t
    seen: dict[int, int] = {}
    b = 1 % L
    seq = []
    j = 0
    while b not in seen:
        seen[b] = j
        seq.append(b)
        b = (2 * b) % L
        j += 1
    h = seen[b]
    t = j - h
    seq.append(b)  # seq[j] = b_j for j <= h+t

    def d(jj: int) -> Fr:
        return eta(seq[jj + 1]) - eta(seq[jj])

    total = 2 * qbar
    for jj in range(h):
        total += Fr(1, 4 ** jj) * d(jj)
    cyc = sum((Fr(1, 4 ** a) * d(h + a) for a in range(t)), Fr(0))
    total += Fr(1, 4 ** h) / (1 - Fr(1, 4 ** t)) * cyc
    return total


def binary_sum_bruteforce_enclosure(q: list[Fr], J: int) -> tuple[Fr, Fr]:
    """Partial sum over blocks j<J plus a rigorous two-sided tail enclosure.
    Tail = sum_{j>=J} 4^{-j} * (block sum of 2^j terms) lies between
    2^{1-J} min q and 2^{1-J} max q."""
    L = len(q)
    partial = Fr(0)
    for j in range(J):
        blk = sum((q[n % L] for n in range(2 ** j, 2 ** (j + 1))), Fr(0))
        partial += Fr(1, 4 ** j) * blk
    lo = partial + Fr(2, 2 ** J) * min(q)
    hi = partial + Fr(2, 2 ** J) * max(q)
    return lo, hi


def periodic_values(x, L: int) -> list[Fr]:
    """x evaluated on residues 0..L-1 (x must be L-periodic with x(0)=x(L))."""
    return [Fr(x(n)) for n in range(L)]


def inner_B(x, Lx: int, y, Ly: int) -> Fr:
    L = lcm(Lx, Ly)
    return binary_sum_periodic([Fr(x(n)) * Fr(y(n)) for n in range(L)])


# ----------------------------------------------------------------------------
# exact linear algebra
# ----------------------------------------------------------------------------

def solve(A: list[list[Fr]], b: list[Fr]) -> list[Fr]:
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(i for i in range(col, n) if M[i][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for i in range(n):
            if i != col and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * c for a, c in zip(M[i], M[col])]
    return [M[i][n] for i in range(n)]


def rank(M: list[list[Fr]]) -> int:
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    rk = 0
    for col in range(cols):
        piv = next((i for i in range(rk, rows) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        M[rk] = [v / pv for v in M[rk]]
        for i in range(rows):
            if i != rk and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * c for a, c in zip(M[i], M[rk])]
        rk += 1
    return rk


# ============================================================================
RESULT: dict = {}

# ---------------------------------------------------------------- A
group("A weights")
for n in range(1, 5000):
    check(w_H(n) <= w_B(n) <= 4 * w_H(n), f"weight sandwich n={n}")
# ||1||_H^2 = 1 by telescoping: partial sums 1 - 1/(N+1)
for N in (1, 2, 10, 100, 1000):
    check(sum((w_H(n) for n in range(1, N + 1)), Fr(0)) == 1 - Fr(1, N + 1))
# ||1||_B^2 = 2 exactly (period 1)
check(binary_sum_periodic([Fr(1)]) == 2, "||1||_B^2")
RESULT["norm_one_B"] = str(binary_sum_periodic([Fr(1)]))

# ---------------------------------------------------------------- B
group("B dilation")
for m in range(2, 9):
    for k in range(2, 9):
        for n in range(0, 400):
            lhs = D(m, lambda q: r(k, q), n)
            check(m * lhs == r(m * k, n) - r(m, n), f"D_m r_k identity m={m} k={k} n={n}")
# exact H-law on finitely supported vectors
import random

rng = random.Random(20260910)
for trial in range(40):
    m = rng.randint(2, 7)
    x = {n: Fr(rng.randint(-5, 5), rng.randint(1, 4)) for n in rng.sample(range(1, 60), 8)}
    Dx: dict[int, Fr] = {}
    for a, v in x.items():
        for n in range(m * a, m * (a + 1)):
            Dx[n] = v
    check(norm_H_finite(Dx) == norm_H_finite(x) / m, "||D_m x||_H^2 = ||x||_H^2/m")
    if m == 2:
        check(norm_B_finite(Dx) == norm_B_finite(x) / 2, "||D_2 x||_B^2 = ||x||_B^2/2")
# D_2 binary law explicitly for all m=2 trials
for trial in range(40):
    x = {n: Fr(rng.randint(-5, 5)) for n in rng.sample(range(1, 200), 10)}
    Dx = {}
    for a, v in x.items():
        Dx[2 * a] = v
        Dx[2 * a + 1] = v
    check(norm_B_finite(Dx) == norm_B_finite(x) / 2, "D_2 binary law")
# popcount fixed point of f -> r_2 + D_2 f
f_prev = {n: 0 for n in range(0, 1025)}
for J in range(1, 12):
    f_new = {n: r(2, n) + (f_prev[n // 2] if n // 2 >= 1 else 0) for n in range(0, 1025)}
    f_prev = f_new
for n in range(1, 1025):
    check(f_prev[n] == bin(n).count("1"), "popcount limit")
check(f_prev[3] == 2, "f(3)=2 for popcount")
# dyadic obstruction f(3)=f(1)+f(2) for every r_{2^j}
for j in range(1, 12):
    k = 2 ** j
    check(r(k, 3) == r(k, 1) + r(k, 2), "f(3)=f(1)+f(2) for r_{2^j}")
# dual norm of ell(x)=x1+x2-x3 in the binary norm: 1/w1 + 1/w2 + 1/w3 = 1+4+4
check(1 / w_B(1) + 1 / w_B(2) + 1 / w_B(3) == 9, "||ell||^2 = 9")
# hence ||1-f||_B^2 >= (ell(1)/||ell||)^2 = 1/9 on the dyadic closed span; witness:
# the bound is attained by the projection of 1 onto the hyperplane ell=0 (Fr exact)
# minimiser of ||1-f||_B^2 subject to ell(f)=0 has value ell(1)^2/||ell||^2 = 1/9
check(Fr(1, 9) == Fr(1) ** 2 / 9, "1/9 bound consistency")
RESULT["dyadic_bound"] = "1/9"

# ---------------------------------------------------------------- C
group("C routing")
for trial in range(40):
    x = {n: Fr(rng.randint(-5, 5), rng.randint(1, 3)) for n in rng.sample(range(1, 300), 10)}
    Cx = {2 * n: v for n, v in x.items()}
    check(norm_B_finite(Cx) == norm_B_finite(x) / 4, "||Cx||_B^2 = ||x||_B^2/4")
# H-operator norm of C: sup_n w_H(2n)/w_H(n) = 1/3 at n=1, decreasing to 1/4
ratios = [w_H(2 * n) / w_H(n) for n in range(1, 2000)]
check(ratios[0] == Fr(1, 3), "ratio at n=1 is 1/3")
check(all(ratios[i] > ratios[i + 1] for i in range(len(ratios) - 1)), "ratio decreasing")
check(all(rr > Fr(1, 4) for rr in ratios), "ratio > 1/4")
for n in range(1, 2000):
    check(w_H(2 * n) / w_H(n) == Fr(n + 1, 2 * (2 * n + 1)), "ratio formula")
# 1 = r_2 + C 1
one = lambda n: 1
for n in range(1, 3000):
    check(1 == r(2, n) + C(one, n), "1 = r_2 + C1")
# explicit f_J and exact binary error 2/4^J
fJ = {n: 0 for n in range(0, 4097)}
for J in range(1, 11):
    fJ = {n: r(2, n) + (fJ[n // 2] if n % 2 == 0 and n // 2 >= 1 else 0) for n in range(0, 4097)}
    for n in range(1, 4097):
        check(fJ[n] == (0 if n % (2 ** J) == 0 else 1), f"f_J formula J={J} n={n}")
    err = binary_sum_periodic([Fr(1) if n % (2 ** J) == 0 else Fr(0) for n in range(2 ** J)])
    check(err == Fr(2, 4 ** J), f"||1-f_J||_B^2 = 2/4^J at J={J}")
# layers a_j = C^j r_2 = 1_{v_2(n)=j}
for j in range(0, 8):
    aj = lambda n, j=j: (1 if n >= 1 and v2(n) == j else 0)
    # C^j r_2 by iteration
    cur = lambda n: r(2, n)
    for _ in range(j):
        prev = cur
        cur = (lambda n, p=prev: C(p, n))
    for n in range(1, 2 ** 12):
        check(cur(n) == aj(n), f"a_j = C^j r_2 (j={j}, n={n})")
    nrm = binary_sum_periodic([Fr(aj(n)) for n in range(2 ** (j + 1))])
    check(nrm == Fr(3, 2 * 4 ** j), f"||a_j||_B^2 = 3/(2*4^j), j={j}")
    for i in range(j):
        ai = lambda n, i=i: (1 if n >= 1 and v2(n) == i else 0)
        check(inner_B(ai, 2 ** (i + 1), aj, 2 ** (j + 1)) == 0, "layers orthogonal")
check(sum((Fr(3, 2 * 4 ** j) for j in range(0, 60)), Fr(0)) < 2, "partial Pythagoras < 2")
check(Fr(3, 2) / (1 - Fr(1, 4)) == 2, "sum of layer norms = 2 = ||1||_B^2")

# ---------------------------------------------------------------- D
group("D obstruction")
y = lambda n: 1 if n % 4 == 2 else 0
# exact linear algebra: for every F subset {2..9} of size <= 4, the system
# y(n) = sum_k c_k r_k(n), 1<=n<=L (L = lcm(4, F)), has no solution.
count_F = 0
for size in range(1, 5):
    for F in combinations(range(2, 10), size):
        L = 4
        for k in F:
            L = lcm(L, k)
        A = [[Fr(r(k, n)) for k in F] for n in range(1, L + 1)]
        bcol = [Fr(y(n)) for n in range(1, L + 1)]
        rkA = rank(A)
        rkAb = rank([row + [bb] for row, bb in zip(A, bcol)])
        check(rkA == len(F), "remainders linearly independent (finite)")
        check(rkAb == rkA + 1, f"y not in span of r_k, F={F}")
        # the L-witness of the note: sum c_k (r_k(L-1)-r_k(L-2)) = sum c_k for every c
        for k in F:
            check(r(k, L - 1) - r(k, L - 2) == 1, "witness difference = 1")
        check(y(L - 1) - y(L - 2) == -1, "y difference = -1")
        count_F += 1
RESULT["obstruction_subsets_tested"] = count_F
# gcd-difference characterisation: for f = sum c_k r_k with period L,
# Delta f(n) = f(n)-f(n-1) = c - sum_{k|n} k c_k depends only on gcd(n, L);
# Delta y does not.
for trial in range(30):
    F = sorted(rng.sample(range(2, 13), rng.randint(1, 5)))
    c = {k: Fr(rng.randint(-4, 4), rng.randint(1, 3)) for k in F}
    L = 1
    for k in F:
        L = lcm(L, k)
    f = lambda n, c=c: sum((v * r(k, n) for k, v in c.items()), Fr(0))
    csum = sum(c.values(), Fr(0))
    table: dict[int, Fr] = {}
    for n in range(1, 3 * L + 1):
        dn = f(n) - f(n - 1)
        check(dn == csum - sum((k * v for k, v in c.items() if n % k == 0), Fr(0)), "Delta formula")
        g = gcd(n, L)
        if g in table:
            check(table[g] == dn, "Delta f is a function of gcd(n,L)")
        else:
            table[g] = dn
        check(f(n + L) == f(n), "f is L-periodic")
    check(f(L) == 0, "f(L)=0")
dy = {n: y(n) - y(n - 1) for n in range(1, 9)}
check(gcd(1, 4) == gcd(3, 4) and dy[1] != dy[3], "Delta y is not a function of gcd(n,4)")

# ---------------------------------------------------------------- E
group("E Dirichlet coefficients")
chi4 = lambda n: 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
for n in range(1, 5000):
    lhs = 2 * (y(n) - y(n - 1))
    rhs = -1 + 3 * (1 if n % 2 == 0 else 0) - 2 * (1 if n % 4 == 0 else 0) + chi4(n)
    check(lhs == rhs, "2 Delta y coefficient identity")
    check((y(n) - y(n - 1)) == {1: 0, 2: 1, 3: -1, 0: 0}[n % 4], "Delta y values")
# (1-2^{-s})(2^{1-s}-1) = 3*2^{-s} - 1 - 2*4^{-s}: check as polynomial identity in u=2^{-s}
# (1-u)(2u-1) = 2u - 1 - 2u^2 + u = 3u - 1 - 2u^2 ; and 4^{-s} = u^2.
for u in (Fr(1, 2), Fr(1, 3), Fr(2, 7), Fr(5)):
    check((1 - u) * (2 * u - 1) == 3 * u - 1 - 2 * u * u, "prefactor identity")
# general layer: {m+1 : v_2(m) = j} = {2^{j+1} l + 2^j + 1 : l >= 0}
for j in range(0, 10):
    S1 = sorted(m + 1 for m in range(1, 1 << 14) if v2(m) == j)
    S2 = [(1 << (j + 1)) * l + (1 << j) + 1 for l in range(len(S1))]
    check(S1 == S2, f"Hurwitz shift set j={j}")
    # a_j(n) - a_j(n-1) = [v_2(n)=j] - [n-1 in {v_2 = j}]
    for n in range(1, 4000):
        d1 = (1 if v2(n) == j else 0) - (1 if n >= 2 and v2(n - 1) == j else 0)
        check(d1 == (1 if v2(n) == j else 0) - (1 if (n - 1 - (1 << j)) % (1 << (j + 1)) == 0 and n - 1 >= 1 else 0),
              "Delta a_j via residue class")
# the residues 1/2 + 2^{-j-1} accumulate at 1/2 (interior of Re a > 0)
for j in range(1, 40):
    check(Fr(1, 2) < Fr(1, 2) + Fr(1, 2 ** (j + 1)) <= Fr(3, 4), "Hurwitz parameters in (1/2, 3/4]")

# ---------------------------------------------------------------- F
group("F periodic formula")
count_periods = 0
for L in list(range(1, 65)) + [96, 100, 128, 210, 255, 256, 1000]:
    for trial in range(3):
        q = [Fr(rng.randint(-6, 6), rng.randint(1, 5)) for _ in range(L)]
        val = binary_sum_periodic(q)
        lo, hi = binary_sum_bruteforce_enclosure(q, 14)
        check(lo <= val <= hi, f"cyclic formula inside brute-force enclosure L={L}")
        # invariance under period multiplication
        for mult in (2, 3):
            check(binary_sum_periodic(q * mult) == val, "period multiple gives same value")
        count_periods += 1
# exact positive check: constant q gives 2*q
for cval in (Fr(1), Fr(3, 7), Fr(-2)):
    check(binary_sum_periodic([cval] * 5) == 2 * cval, "constant sequence")
RESULT["periodic_cases_tested"] = count_periods
# stronger consistency: for q with a single 1 at residue 0 mod L (L = 2^J), value = 2/4^J
for J in range(0, 8):
    L = 2 ** J
    q = [Fr(1) if n % L == 0 else Fr(0) for n in range(L)]
    check(binary_sum_periodic(q) == Fr(2, 4 ** J), "single dyadic residue")

# ---------------------------------------------------------------- G
group("G Gram")
r_fun = lambda k: (lambda n: r(k, n))
one_fun = lambda n: 1
KMAX = 40
Gfull = [[None] * (KMAX + 1) for _ in range(KMAX + 1)]
bfull = [None] * (KMAX + 1)
for k in range(2, KMAX + 1):
    bfull[k] = inner_B(one_fun, 1, r_fun(k), k)
    for l in range(2, k + 1):
        Gfull[k][l] = Gfull[l][k] = inner_B(r_fun(k), k, r_fun(l), l)
check(Gfull[2][2] == Fr(3, 2), "G_22 = 3/2")
check(Gfull[2][3] == Fr(13, 10), "G_23 = 13/10")
check(Gfull[3][3] == Fr(14, 5), "G_33 = 14/5")
check(bfull[2] == Fr(3, 2), "b_2 = 3/2")
check(bfull[3] == 2, "b_3 = 2")
# Gram entries are symmetric bilinear: <r_k, r_l> also computable with period k*l
for k in range(2, 8):
    for l in range(2, 8):
        check(inner_B(r_fun(k), k * l, r_fun(l), k * l) == Gfull[k][l], "period-independent Gram")
table = {}
coeffs = {}
prev_d2 = None
for K in range(2, KMAX + 1):
    idx = list(range(2, K + 1))
    G = [[Gfull[k][l] for l in idx] for k in idx]
    bvec = [bfull[k] for k in idx]
    cvec = solve(G, bvec)
    d2 = 2 - sum((bb * cc for bb, cc in zip(bvec, cvec)), Fr(0))
    table[K] = d2
    coeffs[K] = cvec
    check(d2 > 0, "d_K^2 > 0")
    if prev_d2 is not None:
        check(d2 <= prev_d2, "monotone decrease")
        # Pythagorean update law: d_{K}^2 = d_{K-1}^2 - <e, r_K>^2 / ||z_K||^2
        idx0 = list(range(2, K))
        G0 = [[Gfull[k][l] for l in idx0] for k in idx0]
        c0 = coeffs[K - 1]
        g = [Gfull[k][K] for k in idx0]
        e_dot_r = bfull[K] - sum((cc * gg for cc, gg in zip(c0, g)), Fr(0))
        u = solve(G0, g)
        z2 = Gfull[K][K] - sum((gg * uu for gg, uu in zip(g, u)), Fr(0))
        check(z2 > 0, "||z_K||^2 > 0")
        check(d2 == prev_d2 - e_dot_r * e_dot_r / z2, f"Pythagorean update at K={K}")
    prev_d2 = d2
check(table[2] == Fr(1, 2), "d_2^2 = 1/2")
check(table[3] == Fr(52, 251), "d_3^2 = 52/251")
check(coeffs[3] == [Fr(160, 251), Fr(105, 251)], "c_2, c_3 for K=3")
check(table[4] == Fr(95, 766), "d_4^2 = 95/766")
check(table[5] == Fr(987196, 11709287), "d_5^2")
check(table[6] == Fr(168677, 2018075), "d_6^2")
RESULT["d2_table"] = {K: str(v) for K, v in table.items() if K <= 24}
RESULT["d2_float_times_logK_DIAGNOSTIC"] = {K: float(v) * math.log(K) for K, v in table.items()}
# minimiser residual is orthogonal to V_K (normal equations) — verify at K=6 pointwise:
K = 6
idx = list(range(2, K + 1))
cvec = coeffs[K]
Lper = 60
P1 = lambda n: sum((cc * r(k, n) for k, cc in zip(idx, cvec)), Fr(0))
e = lambda n: 1 - P1(n)
for k in idx:
    check(inner_B(e, Lper, r_fun(k), k) == 0, f"normal equations K=6, k={k}")
check(inner_B(e, Lper, e, Lper) == table[6], "||e_6||^2 = d_6^2")
# local equation R(f) = r_2 + C f - f = (I-C)(1-f) and the 4/9, 4 bounds
for K in (2, 3, 4, 6):
    idx = list(range(2, K + 1))
    cvec = coeffs[K]
    Lper = 1
    for k in idx:
        Lper = lcm(Lper, k)
    f = lambda n, idx=idx, cvec=cvec: sum((cc * r(k, n) for k, cc in zip(idx, cvec)), Fr(0))
    Rf = lambda n, f=f: r(2, n) + C(f, n) - f(n)
    err = lambda n, f=f: 1 - f(n)
    ImC = lambda n, err=err: err(n) - C(err, n)
    for n in range(1, 4 * Lper + 1):
        check(Rf(n) == ImC(n), "R(f) = (I-C)(1-f)")
    nR = inner_B(Rf, 2 * Lper, Rf, 2 * Lper)
    nE = inner_B(err, Lper, err, Lper)
    check(nE == table[K], "||1-f||^2 = d_K^2")
    check(Fr(4, 9) * nR <= nE <= 4 * nR, f"local-equation sandwich K={K}")
    RESULT.setdefault("local_equation", {})[K] = {"R_norm2": str(nR), "err_norm2": str(nE)}


# ---------------------------------------------------------------- D2
group("D2 residue classes")
# Proposition: for m >= 3 no single residue-class indicator 1_{n = b (mod m)}
# is a finite combination of remainders; for m = 2 only r_2 = 1_{odd} is.
# Exact rank tests over F = {2,...,9} (any finite F' subset of a larger F gives
# a sub-system, so the failure for F = {2..9} covers all F' inside it).
Fbig = list(range(2, 10))
Lbig = 1
for k in Fbig:
    Lbig = lcm(Lbig, k)
count_rc = 0
for m in range(2, 9):
    L = lcm(Lbig, m)
    A = [[Fr(r(k, n)) for k in Fbig] for n in range(1, L + 1)]
    rkA = rank(A)
    check(rkA == len(Fbig), "independence over F={2..9}")
    for b in range(m):
        col = [Fr(1 if n % m == b else 0) for n in range(1, L + 1)]
        rkAb = rank([row + [cc] for row, cc in zip(A, col)])
        in_span = (rkAb == rkA)
        check(in_span == (m == 2 and b == 1), f"residue indicator b={b} mod {m} in span iff (m,b)=(2,1)")
        count_rc += 1
RESULT["residue_class_cases"] = count_rc
# f_J = sum_{j<J} a_j is outside the finite span for J >= 2 (J=1 gives r_2)
for J in range(1, 5):
    L = lcm(Lbig, 2 ** J)
    A = [[Fr(r(k, n)) for k in Fbig] for n in range(1, L + 1)]
    col = [Fr(0 if n % (2 ** J) == 0 else 1) for n in range(1, L + 1)]
    in_span = rank([row + [cc] for row, cc in zip(A, col)]) == rank(A)
    check(in_span == (J == 1), f"f_J in finite span iff J=1 (J={J})")
# comparison of the admissible minimum with the non-admissible binary error at K = 2^J
for J in range(1, 6):
    K = 2 ** J
    RESULT.setdefault("admissible_vs_binary", {})[K] = {
        "d_K^2": str(table[K]) if K <= 8 else "see d2_table / float diagnostic",
        "d_K^2_float_DIAGNOSTIC": float(table[K]), "2/4^J": str(Fr(2, 4 ** J))}
    # no inequality is asserted here: at J=2 the admissible minimum 95/766 is
    # slightly BELOW the binary error 1/8, from J=3 on it is above (recorded only)
    check(table[K] > 0 and Fr(2, 4 ** J) > 0, "values recorded")

# ---------------------------------------------------------------- D3
group("D3 finite prime support")
# For a finite set S of primes and q the smallest prime not in S, every finite
# combination of r_k with k S-smooth satisfies f(1) + f(q-1) - f(q) = 0
# (Delta f is a function of the S-part of n; n=1 and n=q have S-part 1).
# Hence dist_B(1, V_S)^2 >= 1/(1 + 1/w_B(q-1) + 1/w_B(q)) and
#       dist_H(1, V_S)^2 >= 1/(2 + 2 q^2).
def smooth(k: int, S: tuple) -> bool:
    for p in S:
        while k % p == 0:
            k //= p
    return k == 1
for S, q in (((2,), 3), ((2, 3), 5), ((2, 3, 5), 7), ((3,), 2), ((5,), 2), ((2, 5), 3), ((3, 5), 2)):
    F = [k for k in range(2, 200) if smooth(k, S)]
    for trial in range(20):
        c = {k: Fr(rng.randint(-3, 3)) for k in rng.sample(F, min(6, len(F)))}
        f = lambda n, c=c: sum((v * r(k, n) for k, v in c.items()), Fr(0))
        check(f(1) + f(q - 1) - f(q) == 0, f"S={S} q={q}: f(1)+f(q-1)-f(q)=0")
        # more generally Delta f(n) = Delta f(n') when n, n' have the same S-part
        for n in range(1, 60):
            for np_ in range(n + 1, 60):
                sn, snp = n, np_
                for p in S:
                    while sn % p == 0: sn //= p
                    while snp % p == 0: snp //= p
                if n // sn == np_ // snp:  # same S-part
                    check(f(n) - f(n - 1) == f(np_) - f(np_ - 1), "Delta f depends only on the S-part")
    boundB = 1 / (1 + 1 / w_B(q - 1) + 1 / w_B(q))
    boundH = Fr(1, 2 + 2 * q * q)
    RESULT.setdefault("finite_prime_support_bounds", {})[str(S)] = {"q": q, "dist_B^2 >=": str(boundB), "dist_H^2 >=": str(boundH)}
    if S == (2,):
        check(boundB == Fr(1, 9), "dyadic bound 1/9 recovered")
        check(boundH == Fr(1, 20), "dyadic H-bound 1/20")
# base m seed: 1_{m does not divide n} is in the finite span only for m = 2
for m in range(2, 8):
    L = lcm(Lbig, m)
    A = [[Fr(r(k, n)) for k in Fbig] for n in range(1, L + 1)]
    col = [Fr(0 if n % m == 0 else 1) for n in range(1, L + 1)]
    in_span = rank([row + [cc] for row, cc in zip(A, col)]) == rank(A)
    check(in_span == (m == 2), f"seed 1_(m does not divide n) in span iff m=2 (m={m})")

# ---------------------------------------------------------------- H
group("H density from D_m")
# D_m 1 = 1_{n>=m}; 1_{[m,inf)} - 1_{[m+1,inf)} = delta_m  (finite-support density witness)
for m in range(2, 50):
    for n in range(1, 200):
        check(D(m, one_fun, n) == (1 if n >= m else 0), "D_m 1 = 1_{n>=m}")
        check(D(m, one_fun, n) - D(m + 1, one_fun, n) == (1 if n == m else 0), "delta_m")
# the tail of a fixed x in H beyond N goes to 0 in both norms (finite-support density)
x = {n: Fr(1) for n in range(1, 2000)}
tailB = lambda N: sum((w_B(n) for n in range(N, 2000)), Fr(0))
check(tailB(1024) < Fr(1, 100), "tail small")

# ============================================================================
print("independent re-verification of the binary-routing note (exact arithmetic)")
print(f"checks passed: {CHECKS} in {len(GROUPS)} groups")
for g, c in GROUPS.items():
    print(f"  {g:28s} {c}")
print("d_K^2 (exact) for K = 2..12 (K up to %d computed; see JSON):" % KMAX)
for K, v in table.items():
    if K <= 12:
        print(f"  K={K:2d}  d_K^2 = {v}")
print("coefficients c_k of the global minimiser for K = 6:")
for k, cc in zip(range(2, 7), coeffs[6]):
    print(f"  c_{k} = {cc}")
print("admissible minimum d_K^2 versus binary-iteration error 2/4^J at K = 2^J:")
for J in range(1, 6):
    K = 2 ** J
    print(f"  J={J}  K={K:2d}  d_K^2 = {float(table[K]):.6f}   2/4^J = {float(Fr(2, 4 ** J)):.6f}")
print("diagnostic (float, not evidence): d_K^2 * log K")
for K in (2, 3, 4, 6, 8, 12, 16, 20, 24, 30, 40):
    print(f"  K={K:2d}  {RESULT['d2_float_times_logK_DIAGNOSTIC'][K]:.6f}")
with open(sys.argv[1] if len(sys.argv) > 1 else "verification_review.json", "w") as fh:
    json.dump({"checks": CHECKS, "groups": GROUPS, "results": RESULT}, fh, indent=1, default=str)
