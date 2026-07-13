#!/usr/bin/env python3
"""Exact checks for the Public Canon v1 observer/boost reading layer."""

from fractions import Fraction as F
import sys


# Pairs (a, b) represent a + b sqrt(5) in Q(sqrt(5)).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def q(a=0, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def inv(x):
    norm = x[0] * x[0] - 5 * x[1] * x[1]
    if norm == 0:
        raise ZeroDivisionError("zero divisor in Q(sqrt(5))")
    return (x[0] / norm, -x[1] / norm)


def div(x, y):
    return mul(x, inv(y))


def power(x, n):
    if n < 0:
        return power(inv(x), -n)
    out = ONE
    base = x
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


PHI = q(F(1, 2), F(1, 2))
PSI = q(F(1, 2), F(-1, 2))
PHI_INV = inv(PHI)
ALT = (ONE, q(-1))
BJ = (PHI, PHI_INV)


checks = []


def check(name, detail, condition):
    checks.append(bool(condition))
    status = "PASS" if condition else "FAIL"
    print(f"{status} {len(checks):02d} {name:<12} {detail}")


def pair_mul(x, y):
    return (mul(x[0], y[0]), mul(x[1], y[1]))


def pair_pow(x, n):
    return (power(x[0], n), power(x[1], n))


def main():
    ok = mul(PHI, PSI) == q(-1)
    ok &= PHI_INV == neg(PSI)
    ok &= sub(mul(PHI, PHI), PHI) == ONE
    check("GOLDEN-FIELD",
          "phi psi = -1, phi^-1 = -psi, phi^2 = phi + 1 exactly",
          ok)

    limit = 96
    fib = [0, 1]
    luc = [2, 1]
    for _ in range(2, limit + 1):
        fib.append(fib[-1] + fib[-2])
        luc.append(luc[-1] + luc[-2])
    ok = True
    for n in range(limit + 1):
        ok &= add(power(PHI, n), power(PSI, n)) == q(luc[n])
        ok &= sub(power(PHI, n), power(PSI, n)) == q(0, fib[n])
    check("BINET",
          "L_n = phi^n + psi^n and sqrt5 F_n = phi^n - psi^n"
          " for 0 <= n <= 96",
          ok)

    ok = True
    for n in range(limit + 1):
        c_n = add(power(PHI, n), power(PHI_INV, n))
        s_n = sub(power(PHI, n), power(PHI_INV, n))
        if n % 2 == 0:
            ok &= c_n == q(luc[n]) and s_n == q(0, fib[n])
        else:
            ok &= c_n == q(0, fib[n]) and s_n == q(luc[n])
    check("PARITY-SPLIT",
          "(C_n,S_n) = (L_n,sqrt5 F_n) for even n and"
          " (sqrt5 F_n,L_n) for odd n",
          ok)

    ok = True
    betas = []
    for n in range(41):
        c_n = add(power(PHI, n), power(PHI_INV, n))
        s_n = sub(power(PHI, n), power(PHI_INV, n))
        betas.append(div(s_n, c_n))
        ok &= sub(mul(c_n, c_n), mul(s_n, s_n)) == q(4)
        ok &= luc[n] * luc[n] - 5 * fib[n] * fib[n] == 4 * (-1) ** n
    for m in range(21):
        for n in range(21):
            composed = div(add(betas[m], betas[n]),
                           add(ONE, mul(betas[m], betas[n])))
            ok &= composed == betas[m + n]
    check("COUNT-LAW",
          "beta_(m+n) = (beta_m+beta_n)/(1+beta_m beta_n);"
          " C_n^2-S_n^2 = 4 and L_n^2-5F_n^2 = 4(-1)^n",
          ok)

    ok = pair_mul(BJ, ALT) == pair_mul(ALT, BJ)
    step = pair_mul(BJ, ALT)
    ok &= pair_mul(ALT, ALT) == (ONE, ONE)
    ok &= pair_mul(step, step) == pair_mul(BJ, BJ)
    ok &= mul(BJ[0], BJ[1]) == ONE
    ok &= mul(ALT[0], ALT[1]) == q(-1)
    ok &= mul(step[0], step[1]) == q(-1)
    check("BEAT",
          "STEP = B_J A = A B_J, A^2 = I, STEP^2 = B_J^2;"
          " det(B_J,A,STEP) = (1,-1,-1)",
          ok)

    ok = True
    for m in range(25):
        for n in range(25):
            ok &= pair_mul(pair_pow(BJ, m), pair_pow(BJ, n)) == \
                pair_pow(BJ, m + n)
    check("BOOST-INDEX",
          "B_J^m B_J^n = B_J^(m+n) exactly for 0 <= m,n < 25",
          ok)

    mu4 = set(range(4))
    observer = ({0}, {1, 2, 3})
    substrate = ({0, 2}, {1, 3})
    alt = {k: (k + 2) % 4 for k in mu4}
    ok = set().union(*observer) == mu4
    ok &= set().union(*substrate) == mu4
    ok &= sorted(map(len, observer)) == [1, 3]
    ok &= sorted(map(len, substrate)) == [2, 2]
    ok &= all(alt[alt[k]] == k and alt[k] != k for k in mu4)
    ok &= all({k, alt[k]} in substrate for k in mu4)
    check("MU4-SPLIT",
          "observer partition 1+3; alternator k -> k+2 has two"
          " fixed-point-free 2-cycles giving substrate partition 2+2",
          ok)

    p_plus = ((ONE, ZERO), (ZERO, ZERO))
    p_minus = ((ZERO, ZERO), (ZERO, ONE))
    ok = add(p_plus[0][0], p_minus[0][0]) == ONE
    ok &= add(p_plus[1][1], p_minus[1][1]) == ONE
    ok &= BJ[0] == PHI and BJ[1] == PHI_INV
    ok &= ALT == (ONE, q(-1))
    ok &= pair_mul(BJ, ALT) == pair_mul(ALT, BJ)
    check("FROZEN-AXIS",
          "A = diag(1,-1) has complementary axis projectors and"
          " commutes with B_J = diag(phi,phi^-1)",
          ok)

    passed = sum(checks)
    print(f"ALL {passed}/{len(checks)} CHECKS PASS" if passed == len(checks)
          else f"SUMMARY {passed}/{len(checks)} CHECKS PASS")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
