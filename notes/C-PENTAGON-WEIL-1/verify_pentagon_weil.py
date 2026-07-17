#!/usr/bin/env python3
# verify_pentagon_weil.py
# Candidate C-PENTAGON-WEIL-1: exact verification of the G0 kernel of the
# pentagon root-filter normalization  Z_J := MerCont(P0/f5) = zeta,
# with f5(s) = 5^(1-s) - 1 and P0(s) = sum_n c(n) n^(-s),
# c(n) = sum_{k=1..4} zeta_5^(k n).
#
# Discipline: Python 3 standard library only. Exact arithmetic in every
# assertion (integers, Z[zeta_5] four-tuples, Fractions). Floats appear only
# in printed engineering witnesses, never in an assertion.
# Frozen environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
# PYTHONHASHSEED=0 TZ=UTC. Deterministic output.

from fractions import Fraction
import math

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ---------------------------------------------------------------------------
# Z[zeta_5], basis (1, j, j^2, j^3), reduction j^4 = -(1+j+j^2+j^3), j^5 = 1.
# ---------------------------------------------------------------------------
def zmul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    r = [c[0] + c[5], c[1] + c[6], c[2], c[3]]  # fold j^5 -> 1, j^6 -> j
    k4 = c[4]                                    # spread j^4
    return (r[0] - k4, r[1] - k4, r[2] - k4, r[3] - k4)

def zpow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = zmul(r, a)
    return r

J5 = (0, 1, 0, 0)  # j = zeta_5

# C1: root-filter coefficient. For every residue r mod 5:
#     sum_{k=1..4} j^(k r) = 4 if r = 0, else -1, exactly in Z[zeta_5].
# Exhaustive over residues covers all n by periodicity.
ok = True
for r in range(5):
    s = (0, 0, 0, 0)
    for k in range(1, 5):
        t = zpow(J5, (k * r) % 5)
        s = tuple(x + y for x, y in zip(s, t))
    want = (4, 0, 0, 0) if r == 0 else (-1, 0, 0, 0)
    ok = ok and (s == want)
check("C1 c(n) = sum_k zeta_5^(kn) = 5*[5|n] - 1, exhaustive over n mod 5, exact in Z[zeta_5]", ok)

# C2: prod_{k=1..4} (1 - j^k) = 5 exactly in Z[zeta_5].
# This is Phi_5(1) = 5 = N(1 - j). It pins P0(1) = -log 5 with no 2*pi*i
# ambiguity: the four principal logs pair conjugately and their sum is the
# real log of this positive integer.
p = (1, 0, 0, 0)
for k in range(1, 5):
    jk = zpow(J5, k)
    term = tuple((1 if i == 0 else 0) - jk[i] for i in range(4))
    p = zmul(p, term)
check("C2 (1-j)(1-j^2)(1-j^3)(1-j^4) = 5, exact in Z[zeta_5]", p == (5, 0, 0, 0))

# C3: finite root-filter regrouping, the exact skeleton of P0 = f5 * zeta:
#     sum_{n<=N} c(n) n^(-s) = 5^(1-s) * sum_{m<=N/5} m^(-s) - sum_{n<=N} n^(-s)
# exact in Fractions for integer s >= 2 and N a multiple of 5.
ok = True
for s in (2, 3, 4):
    for N in (5, 25, 125, 625):
        lhs = sum(Fraction(4 if n % 5 == 0 else -1) / Fraction(n) ** s
                  for n in range(1, N + 1))
        rhs = (Fraction(1, 5 ** (s - 1))
               * sum(Fraction(1) / Fraction(m) ** s for m in range(1, N // 5 + 1))
               - sum(Fraction(1) / Fraction(n) ** s for n in range(1, N + 1)))
        ok = ok and (lhs == rhs)
check("C3 finite identity sum c(n)n^-s = 5^(1-s) sum m^-s - sum n^-s, s in {2,3,4}, N in {5,25,125,625}, exact Fractions", ok)

# C4: the raw carrier f5*xi cannot satisfy the s <-> 1-s functional equation.
# The pair (2, -1) is s <-> 1-s. Exact rationals:
#     f5(2) = 5^(-1) - 1 = -4/5,   f5(-1) = 5^2 - 1 = 24,
#     ratio f5(2)/f5(-1) = -1/30 != 1.
# Given xi(2) = xi(-1) != 0 [imported: functional equation; xi(2) = pi/6 > 0],
# f5(s)*xi(s) at 2 and -1 differ by the exact factor -1/30, so symmetry fails.
f5_2 = Fraction(1, 5) - 1
f5_m1 = Fraction(25) - 1
check("C4 raw-carrier asymmetry: f5(2) = -4/5, f5(-1) = 24, ratio -1/30 != 1, exact",
      f5_2 == Fraction(-4, 5) and f5_m1 == 24
      and f5_2 / f5_m1 == Fraction(-1, 30) and f5_2 != f5_m1)

# C5: the full period sum vanishes: c(1)+...+c(5) = 0.
# Bounded partial sums; the Dirichlet series converges conditionally for
# Re s > 0 [imported Dirichlet test], so P0(1) = -log 5 is a series value.
check("C5 period sum c(1..5) = 0, exact",
      sum(4 if r % 5 == 0 else -1 for r in range(1, 6)) == 0)

# ---------------------------------------------------------------------------
# Engineering witnesses. Floats, printed only, asserted never.
# ---------------------------------------------------------------------------
N = 10 ** 6
acc = 0.0
for n in range(1, N + 1):
    acc += (4.0 if n % 5 == 0 else -1.0) / n
print("W1 witness sum_{n<=1e6} c(n)/n   = %.12f ; -log 5     = %.12f ; |diff| = %.3e"
      % (acc, -math.log(5.0), abs(acc + math.log(5.0))))

acc2 = 0.0
for n in range(1, N + 1):
    acc2 += (4.0 if n % 5 == 0 else -1.0) / (n * n)
print("W2 witness sum_{n<=1e6} c(n)/n^2 = %.12f ; -2*pi^2/15 = %.12f ; |diff| = %.3e"
      % (acc2, -2.0 * math.pi ** 2 / 15.0, abs(acc2 + 2.0 * math.pi ** 2 / 15.0)))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS G0 kernel at candidate grade" if not FAILED else "FAIL"))
