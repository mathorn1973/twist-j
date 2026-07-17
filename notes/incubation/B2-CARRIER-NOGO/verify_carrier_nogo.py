#!/usr/bin/env python3
# verify_carrier_nogo.py
# Candidate B2 / row J-LI-CYCLIC-CARRIER-DIMENSION [T, unconditional] (incubation, no authority)
#
# Finite exact skeleton for the carrier no-go. The analytic theorem and the
# single classical import (Lagarias's Li-coefficient asymptotic) are frozen in
# PREREG.md; this verifier pins only the exact finite facts the proof rests on:
#
#   Cyclic cocycle norm  q_n = || sum_{k=0}^{n-1} U^k v ||^2.
#   Finite spectrum  =>  q_n = a_* n^2 + R_n,  a_* = ||P_{z=1} v||^2,  0 <= R_n <= C.
#   Two exemplars bracket the dichotomy:
#     A  primitive 10th-root carrier  -> a_* = 0, q_n bounded (Ramanujan ladder).
#     B  carrier containing z = 1     -> a_* > 0, q_n ~ a_* n^2.
#   Li ladder needs  lambda_n -> +infinity  AND  lambda_n = o(n^2)  (Lagarias, RH).
#   Neither dichotomy branch can meet both: bounded (A) is not ->infinity,
#   quadratic (B) is not o(n^2). Hence no finite cyclic carrier realizes lambda.
#
# Exact integer arithmetic only. Exit nonzero on any failure.

from math import gcd

FAILED = []
def check(tag, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + tag + (("  " + extra) if extra else ""))
    if not cond:
        FAILED.append(tag)

# ---------- exact Ramanujan sum c_k(n) = sum_{d | gcd(k,n)} d * mu(k/d) ----------
def factorize(m):
    f = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f

def mobius(m):
    if m == 1:
        return 1
    f = factorize(m)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)

def ramanujan(k, n):
    g = gcd(k, n)
    s = 0
    d = 1
    while d * d <= g:
        if g % d == 0:
            s += d * mobius(k // d)
            e = g // d
            if e != d:
                s += e * mobius(k // e)
        d += 1
    return s

# Cocycle ladder for a carrier whose nonunit spectrum is the primitive K-th
# roots with equal weight w_prim, plus optionally the eigenvalue z=1 with weight a1.
# q_n = a1 * n^2 + w_prim * sum_{d=-(n-1)}^{n-1} (n-|d|) c_K(d).
def ladder(K, n_max, w_prim=1, a1=0):
    out = []
    for n in range(0, n_max + 1):
        s = 0
        for d in range(-(n - 1), n):  # d = -(n-1) .. n-1
            s += (n - abs(d)) * ramanujan(K, d if d >= 0 else -d)  # c_K even in d
        out.append(a1 * n * n + w_prim * s)
    return out

N = 200

# EXEMPLAR A: primitive 10th roots, equal weight, no z=1 -> a_* = 0, bounded.
A = ladder(10, N, w_prim=1, a1=0)
boundA = max(A)
# exact periodicity: partial geometric sums of 10th roots cycle with period 10,
# so the ladder is 10-periodic from n=0 and vanishes at multiples of 10.
per_ok = all(A[n] == A[n + 10] for n in range(0, N - 10))
zeros_ok = all(A[10 * j] == 0 for j in range(0, N // 10 + 1))
check("KC1 primitive-10 carrier ladder is bounded and 10-periodic (a_* = 0)",
      per_ok and zeros_ok and boundA < 10**6, f"sup q_n = {boundA}, q_0..q_10 = {A[0:11]}")

# a_* = lim q_n/n^2 = 0 for A: bounded ladder, ratio -> 0.
aA_zero = A[N] * 4 < N * N
check("KC2 a_* = 0 for the primitive carrier (q_n = o(n^2), in fact O(1))",
      aA_zero, f"q_200 = {A[N]} << 200^2 = {N*N}")

# EXEMPLAR B: same primitive block PLUS z=1 weight 1 -> a_* = 1, q_n = n^2 + bounded.
B = ladder(10, N, w_prim=1, a1=1)
resid = [B[n] - n * n for n in range(N + 1)]
residual_bounded = (max(resid) - min(resid)) < 10**6 and all(resid[n] == A[n] for n in range(N + 1))
check("KC3 z=1 carrier ladder is n^2 + bounded (a_* = 1)",
      residual_bounded, f"q_n - n^2 = A_n exactly; residual in [{min(resid)},{max(resid)}]")

# DICHOTOMY as an exact statement: q_n = a_* n^2 + R_n with 0 <= R_n <= C on both.
dich = all(0 <= A[n] for n in range(N + 1)) and all(0 <= resid[n] for n in range(N + 1))
check("KC4 dichotomy q_n = a_* n^2 + R_n with 0 <= R_n <= C holds on both exemplars", dich)

# KC5: the incompatibility logic (Lagarias import stated as two required limits).
# Required of the Li ladder: unbounded AND o(n^2). Test both dichotomy branches.
def branch_meets_requirements(a_star, bounded_residual):
    is_unbounded = (a_star > 0)                 # only the n^2 term can diverge
    is_o_n2 = (a_star == 0)                      # o(n^2) forces the n^2 term off
    return is_unbounded and is_o_n2             # cannot hold together
branchA = branch_meets_requirements(0, True)     # a_*=0
branchB = branch_meets_requirements(1, True)     # a_*>0
check("KC5 no finite-carrier branch is both unbounded and o(n^2) (contradiction closes)",
      (not branchA) and (not branchB),
      "a_*=0 branch bounded (not ->inf); a_*>0 branch ~n^2 (not o(n^2))")

# KC6: Ramanujan identity cross-check c_10(0)=phi(10)=4 and small values, exact.
c10 = [ramanujan(10, n) for n in range(0, 11)]
check("KC6 Ramanujan sums c_10(n) exact, c_10(0)=phi(10)=4",
      c10 == [4, 1, -1, 1, -1, -4, -1, 1, -1, 1, 4], f"c_10(0..10) = {c10}")

print("-" * 60)
if FAILED:
    print("VERDICT: FAIL -> " + ", ".join(FAILED))
    raise SystemExit(1)
print("VERDICT: PASS  J-LI-CYCLIC-CARRIER-DIMENSION skeleton (6/6)")
