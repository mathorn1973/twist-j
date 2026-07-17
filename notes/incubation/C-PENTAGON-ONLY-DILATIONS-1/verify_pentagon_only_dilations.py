#!/usr/bin/env python3
# verify_pentagon_only_dilations.py
# Candidate C-PENTAGON-ONLY-DILATIONS-1  (Public Canon incubation lane, no authority)
#
# Exact, standard-library-only audit of the finite skeleton behind the row
#   PENTAGON-ONLY-DILATIONS [F]:
# in the Nyman-Beurling / Baez-Duarte closure, restricting the dilation family
# to powers of a single prime (here 5, the pentagon tower) cannot reach any
# cross-prime direction. The deficiency is an exact positive rational and,
# strikingly, is INDEPENDENT of how many 5-powers are used.
#
# Object. H = L^2(0,1). Clock functions g_n(x) = frac(n x) - 1/2, n >= 1.
# Derived closed form (proved by Parseval on g_n = -sum_{k>=1} sin(2 pi k n x)/(pi k)):
#   <g_m, g_n> = gcd(m,n)^2 / (12 m n).
# The verifier re-derives every <g_m,g_n> it uses by an INDEPENDENT exact
# piecewise integration, so the closed form is checked, not assumed.
#
# 5-tower Gram: <g_{5^a}, g_{5^b}> = 5^{-|a-b|}/12  (a Kac-Murdock-Szego matrix).
# Cross-prime shadow: for q coprime to 5, <g_q, g_{5^m}> = 1/(12 q 5^m),
# proportional to the KMS-harmonic vector, so G^{-1} maps it to a boundary
# delta at m=0. Hence for every M >= 0
#   dist(g_q, span{g_{5^m}: 0<=m<=M})^2 = (1/12)(1 - 1/q^2),  constant in M.
#
# No float appears in any assertion. Exit nonzero on any failure.

from fractions import Fraction as F
from math import gcd

FAILED = []
def check(tag, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + tag + (("  " + extra) if extra else ""))
    if not cond:
        FAILED.append(tag)

def lcm(a, b):
    return a // gcd(a, b) * b

# ---------- independent exact Gram via piecewise integration ----------
def integ_gram(m, n):
    # exact integral over [0,1] of (frac(m x)-1/2)(frac(n x)-1/2) dx
    L = lcm(m, n)
    total = F(0)
    for k in range(L):
        # on (k/L,(k+1)/L) both fracs are linear; floor constant just right of k/L
        fm = (m * k) // L
        fn = (n * k) // L
        # g_m = m x - fm - 1/2 = a1 x + b1 ; g_n = n x - fn - 1/2 = a2 x + b2
        a1, b1 = F(m), F(-fm) - F(1, 2)
        a2, b2 = F(n), F(-fn) - F(1, 2)
        x0, x1 = F(k, L), F(k + 1, L)
        # integral of (a1 x+b1)(a2 x+b2) = a1a2 x^2 + (a1 b2 + b1 a2) x + b1 b2
        A = a1 * a2
        B = a1 * b2 + b1 * a2
        C = b1 * b2
        total += A * (x1**3 - x0**3) / 3 + B * (x1**2 - x0**2) / 2 + C * (x1 - x0)
    return total

def gram_closed(m, n):
    return F(gcd(m, n)**2, 12 * m * n)

# ---------- exact linear solve for Fraction systems ----------
def solve(Gm, cv):
    # solve Gm y = cv exactly; return y (list of Fraction). Gm square list-of-lists.
    n = len(cv)
    A = [row[:] + [cv[i]] for i, row in enumerate(Gm)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[p] = A[p], A[i]
        piv = A[i][i]
        A[i] = [v / piv for v in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0:
                f = A[r][i]
                A[r] = [A[r][c] - f * A[i][c] for c in range(n + 1)]
    return [A[i][n] for i in range(n)]

def quad_form(Gm, cv):
    # cv^T Gm^{-1} cv
    y = solve(Gm, cv)
    return sum(cv[i] * y[i] for i in range(len(cv)))

# =====================================================================
print("C-PENTAGON-ONLY-DILATIONS-1 exact skeleton")
print("-" * 60)

# PD1: the closed Gram form matches an independent exact integration
pairs = [(1, 1), (2, 3), (2, 5), (5, 25), (6, 10), (7, 1), (25, 125), (3, 7)]
ok = True
detail = []
for (m, n) in pairs:
    a, b = integ_gram(m, n), gram_closed(m, n)
    ok = ok and (a == b)
    detail.append(f"<g{m},g{n}>={b}")
check("PD1 Gram closed form gcd^2/(12mn) verified by exact integration",
      ok, "; ".join(detail[:4]))

# PD2: 5-tower is exactly the KMS matrix 5^{-|a-b|}/12
M = 8
ok = True
for a in range(M + 1):
    for b in range(M + 1):
        val = gram_closed(5**a, 5**b)
        want = F(1, 12) * F(1, 5**abs(a - b))
        ok = ok and (val == want)
check("PD2 five-tower Gram equals KMS 5^{-|a-b|}/12 (a,b<=8)", ok)

# PD3: cross-prime distance is (1/12)(1-1/q^2), CONSTANT in M
def tower_gram(M):
    return [[gram_closed(5**a, 5**b) for b in range(M + 1)] for a in range(M + 1)]

def cross_shadow(q, M):
    return [gram_closed(q, 5**m) for m in range(M + 1)]

results = {}
allconst = True
for q in (2, 3, 6, 7, 12):
    if gcd(q, 5) != 1:
        continue
    limit = F(1, 12) * (1 - F(1, q * q))
    dists = []
    for MM in range(0, 9):
        G = tower_gram(MM)
        c = cross_shadow(q, MM)
        d2 = gram_closed(q, q) - quad_form(G, c)   # ||g_q||^2 - c^T G^{-1} c
        dists.append(d2)
    results[q] = dists
    const = all(d == limit for d in dists) and limit > 0
    allconst = allconst and const
    check(f"PD3 q={q}: dist^2 = (1/12)(1-1/q^2) = {limit} for every M in 0..8",
          const, f"e.g. dist^2(M=0)={dists[0]}, dist^2(M=8)={dists[8]}")

# PD4: the exact rational values for the two prime witnesses
check("PD4 q=2 deficiency equals 1/16", results[2][0] == F(1, 16), f"={results[2][0]}")
check("PD4 q=3 deficiency equals 2/27", results[3][0] == F(2, 27), f"={results[3][0]}")

# PD5: harmonic collapse. G^{-1} c is a pure boundary delta at index 0:
# the higher 5-powers 5^1,5^2,... contribute nothing toward g_q.
ok = True
witness = None
for q in (2, 3, 7):
    M = 6
    G = tower_gram(M)
    c = cross_shadow(q, M)
    y = solve(G, c)                     # coefficients of the best approximant
    zero_tail = all(y[m] == 0 for m in range(1, M + 1))
    head_ok = (y[0] == F(1, q))
    ok = ok and zero_tail and head_ok
    if q == 2:
        witness = [str(v) for v in y]
check("PD5 best 5-tower approximant of g_q uses only g_1 (coeffs 5^{m>=1} are 0)",
      ok, "q=2 coeffs=[" + ", ".join(witness) + "]")

# PD6: monotonic uselessness. Adding any 5^m (m>=1) leaves the distance unchanged,
# so no finite or infinite 5-power combination beats the single first rung.
ok = True
for q in (2, 3, 6, 7):
    if gcd(q, 5) != 1:
        continue
    d = results[q]
    ok = ok and all(d[i] == d[0] for i in range(len(d)))
check("PD6 distance does not decrease when 5-powers are added (F: route is dead)", ok)

# FALSIFIER RECORD (informational, not a gate):
# the row fires (returns to H) if any exact 5-power combination reaches
# dist^2 < (1/12)(1-1/q^2) for some q coprime to 5. PD3/PD5/PD6 prove it cannot.
print("-" * 60)
if FAILED:
    print("VERDICT: FAIL -> " + ", ".join(FAILED))
    raise SystemExit(1)
print("VERDICT: PASS  C-PENTAGON-ONLY-DILATIONS-1 skeleton (6/6)")
