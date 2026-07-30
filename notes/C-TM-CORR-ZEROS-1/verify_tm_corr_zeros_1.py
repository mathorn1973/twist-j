#!/usr/bin/env python3
# verify_tm_corr_zeros_1.py
# C-TM-CORR-ZEROS-1 verifier. Prereg: PREREG-C-TM-CORR-ZEROS-1.md
# Python 3 stdlib only. Exact arithmetic: int and Fraction only. No float
# anywhere in any assertion or any emitted field. Deterministic output.
# Exit 0 iff every gate passes.

import sys
from fractions import Fraction

RESULTS = []


def check(tag, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "%s %s" % (tag, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


# ------------------------------------------------------------------ helpers
def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def blen(n):
    """L(n): binary length. L(0) = 0."""
    return n.bit_length()


def v2_int(n):
    """2-adic valuation of a nonzero integer."""
    return (n & -n).bit_length() - 1


def v2_frac(q):
    """2-adic valuation of a nonzero Fraction."""
    return v2_int(q.numerator) - v2_int(q.denominator)


def tm_bits(limit):
    """t_n = s_2(n) mod 2 for 0 <= n < limit, as a bytearray."""
    t = bytearray(limit)
    for n in range(1, limit):
        t[n] = t[n >> 1] ^ (n & 1)
    return t


def tm_word(limit):
    """u_n in {-1, +1} for 0 <= n < limit."""
    return [1 - 2 * b for b in tm_bits(limit)]


CMAX = (1 << 18) + 4
if CMAX < 200004:
    CMAX = 200004

# c(k) by the L2 recursion, bottom up, exact rationals.
# c(0) = 1; c(1) solves c(1) = -(c(0) + c(1))/2, so 3 c(1) = -1.
C = [Fraction(0)] * (CMAX + 2)
C[0] = Fraction(1)
C[1] = Fraction(-1, 3)
for _k in range(2, CMAX + 2):
    if _k % 2 == 0:
        C[_k] = C[_k >> 1]
    else:
        _m = _k >> 1
        C[_k] = -(C[_m] + C[_m + 1]) / 2


def U(m):
    return 3 * (C[m] + C[m + 1])


def W(m):
    return 3 * (C[m] - C[m + 1])


def lam0(u, w):
    return (w / 2, u + w / 2)


def lam1(u, w):
    return (-w / 2, -u + w / 2)


def uw_deep(m):
    """(U_m, W_m) by transfer-matrix product along the binary expansion of m,
    starting from the root (2, 4). Lambda_0 fixes the root, so leading zeros
    are harmless. Independent of the array C."""
    u, w = Fraction(2), Fraction(4)
    for bit in bin(m)[2:] if m else "0":
        u, w = lam1(u, w) if bit == "1" else lam0(u, w)
    return u, w


def c_deep(k):
    """c(k) with no use of the array C: reduce to the odd part, then one
    transfer-matrix product."""
    q = oddpart(k)
    if q == 1:
        return Fraction(-1, 3)
    return -uw_deep((q - 1) // 2)[0] / 6


print("C-TM-CORR-ZEROS-1 verifier")
print("basis: Public Canon v27, tag canon-v27, content commit 116b62ed")
print("arithmetic: int and Fraction only; no float in this file")
print("")

# --------------------------------------------------------------------- V1
# Zero set on 1 <= k <= 200000 by the memoized rational recursion.
LIM = 200000
zeros = set()
for k in range(1, LIM + 1):
    if C[k] == 0:
        zeros.add(k)
predicted = set()
for k in range(1, LIM + 1):
    if oddpart(k) in (5, 7):
        predicted.add(k)
check("V1 zero set on 1 <= k <= %d equals {k : oddpart(k) in {5,7}}" % LIM,
      zeros == predicted,
      "zeros=%d extra=%d missing=%d"
      % (len(zeros), len(zeros - predicted), len(predicted - zeros)))

# --------------------------------------------------------------------- V2
# L1 identities for all 0 <= m <= 300, 0 <= N <= 300 by direct integer sums.
M2, N2 = 300, 300
need_k = 2 * M2 + 2
need_n = 2 * N2 + need_k + 2
u = tm_word(need_n)
# S[j][n] = S_j(n) for 0 <= j <= need_k, 0 <= n <= 2*N2
SROW = []
for j in range(need_k + 1):
    row = [0] * (2 * N2 + 1)
    acc = 0
    for n in range(2 * N2):
        acc += u[n] * u[n + j]
        row[n + 1] = acc
    SROW.append(row)
ok = True
bad = None
for m in range(M2 + 1):
    for N in range(N2 + 1):
        if SROW[2 * m][2 * N] != 2 * SROW[m][N]:
            ok, bad = False, ("even", m, N)
            break
        if SROW[2 * m + 1][2 * N] != -(SROW[m][N] + SROW[m + 1][N]):
            ok, bad = False, ("odd", m, N)
            break
    if not ok:
        break
check("V2 L1 identities, 0 <= m <= %d, 0 <= N <= %d, direct integer sums"
      % (M2, N2), ok, "" if ok else "first violation %s" % (bad,))

# --------------------------------------------------------------------- V3
# Discrepancy bound for 0 <= k <= 64, N in 1..4096, exact rational compare.
# log_2(N) is irrational for N not a power of two, so the exact inequality
# actually tested is the STRONGER rational one obtained from the exact bound
#     2*log_2(N) + 2 >= 2*(L(N) - 1) + 2 = 2*L(N),
# namely  |S_k(N) - c(k)*N| <= 2^L(k) * 2 * L(N).
K3, N3 = 64, 4096
u3 = tm_word(N3 + K3 + 2)
ok = True
bad = None
worst_num, worst_den = 0, 1  # tightest observed ratio LHS/RHS, exact
for k in range(K3 + 1):
    acc = 0
    ck = C[k]
    pow_k = 1 << blen(k)
    for N in range(1, N3 + 1):
        acc += u3[N - 1] * u3[N - 1 + k]
        lhs = abs(Fraction(acc) - ck * N)
        rhs = Fraction(pow_k * 2 * blen(N))
        if lhs > rhs:
            ok, bad = False, (k, N)
            break
        if lhs * worst_den > Fraction(worst_num) * rhs:
            r = lhs / rhs
            worst_num, worst_den = r.numerator, r.denominator
    if not ok:
        break
check("V3 discrepancy bound, 0 <= k <= %d, 1 <= N <= %d, exact rational"
      % (K3, N3), ok,
      "tightest LHS/RHS = %d/%d" % (worst_num, worst_den) if ok
      else "first violation k=%d N=%d" % bad)

# --------------------------------------------------------------------- V4
# Valuation lemma: pinned base cases, then v_2(U_m) = v_2(W_m) = -(L(m) - 3).
BASE = {0: (Fraction(2), Fraction(4)),
        1: (Fraction(-2), Fraction(0)),
        2: (Fraction(0), Fraction(-2)),
        3: (Fraction(0), Fraction(2))}
ok = True
for m, (uu, ww) in BASE.items():
    if (U(m), W(m)) != (uu, ww):
        ok = False
check("V4a base cases (U_m, W_m) for m in {0,1,2,3} match the pinned values",
      ok)

M4 = 1 << 18
ok = True
bad = None
for m in range(4, M4 + 1):
    um, wm = U(m), W(m)
    if um == 0 or wm == 0:
        ok, bad = False, (m, "vanishes")
        break
    want = -(blen(m) - 3)
    if v2_frac(um) != want or v2_frac(wm) != want:
        ok, bad = False, (m, "valuation")
        break
check("V4b v_2(U_m) = v_2(W_m) = -(L(m) - 3) for 4 <= m <= 2^18", ok,
      "" if ok else "first violation m=%d (%s)" % bad)

# --------------------------------------------------------------------- V5
# Deep k by transfer-matrix product on the binary expansion.
DEEP_ZERO = [5 * 2 ** 100, 7 * 2 ** 100, 5 * 2 ** 400, 7 * 2 ** 400,
             5, 7, 5 * 2 ** 1, 7 * 2 ** 63]
DEEP_NONZERO = [3 * 2 ** 100, 9 * 2 ** 100, 11 * 2 ** 400, 13 * 2 ** 400,
                1 * 2 ** 200, (2 ** 61 - 1) * 2 ** 7,
                (2 ** 199 + 2 ** 71 + 1) * 2 ** 5,
                35 * 2 ** 128, 25 * 2 ** 33, 49 * 2 ** 33]
ok = True
bad = None
for k in DEEP_ZERO:
    if c_deep(k) != 0:
        ok, bad = False, ("expected zero", k)
        break
if ok:
    for k in DEEP_NONZERO:
        if c_deep(k) == 0:
            ok, bad = False, ("expected nonzero", k)
            break
check("V5a deep k by transfer-matrix product: zero iff oddpart in {5,7}",
      ok, "%d zero and %d nonzero pins"
      % (len(DEEP_ZERO), len(DEEP_NONZERO)) if ok else "%s k=%d" % bad)

# V5b: the independent transfer-matrix path agrees with the memoized array
# everywhere both are defined.
ok = True
bad = None
for k in range(1, 20001):
    if c_deep(k) != C[k]:
        ok, bad = False, k
        break
check("V5b transfer-matrix path agrees with the memoized recursion, "
      "1 <= k <= 20000", ok, "" if ok else "first disagreement k=%d" % bad)

# V5c: the unique neighbour coincidence, W_m = 0 iff m = 1.
coincide = [m for m in range(1, LIM + 1) if C[m] == C[m + 1]]
check("V5c c(m) = c(m+1) for exactly one m in 1..%d" % LIM,
      coincide == [1], "m = %s" % coincide)

print("")
npass = sum(1 for r in RESULTS if r)
print("SUMMARY %d/%d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
