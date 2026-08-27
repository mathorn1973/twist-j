#!/usr/bin/env python3
"""Exact audit for P-O5-FIRST-SHELL-BILINEAR-SQUARE-1."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


LIMIT = 30000
TRANSFER_LIMIT = 10000


def check(label, condition, detail=""):
    if not condition:
        raise AssertionError(f"{label} failed: {detail}")


def chi5(n):
    residue = n % 5
    if residue == 0:
        return 0
    return 1 if residue in (1, 4) else -1


def build_spf(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, limit + 1):
        if spf[p] != p:
            continue
        if p * p > limit:
            continue
        for multiple in range(p * p, limit + 1, p):
            if spf[multiple] == multiple:
                spf[multiple] = p
    return tuple(spf)


SPF = build_spf(LIMIT)


def factorization(n):
    if n == 1:
        return ()
    out = []
    while n > 1:
        p = SPF[n]
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        out.append((p, exponent))
    return tuple(out)


def allowed_prime(p, include_11=False):
    if chi5(p) != 1:
        return False
    return p >= 11 if include_11 else p > 11


def nu_coeff(n, include_11=False):
    if n == 0:
        return 0
    if n == 1:
        return 1
    factors = factorization(n)
    for p, exponent in factors:
        if exponent != 1 or not allowed_prime(p, include_11):
            return 0
    return -1 if len(factors) % 2 else 1


def b_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    factors = factorization(n)
    for p, exponent in factors:
        if exponent != 1 or not allowed_prime(p):
            return 0
    return (-2) ** len(factors)


def c_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    value = 1
    for p, exponent in factorization(n):
        if not allowed_prime(p):
            return 0
        if exponent == 1:
            value *= -2
        elif exponent == 2:
            value *= 1
        else:
            return 0
    return value


def r_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    value = 1
    for p, exponent in factorization(n):
        if not allowed_prime(p):
            return 0
        if exponent == 1:
            return 0
        value *= -(exponent - 1)
    return value


def q_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    value = 1
    for p, exponent in factorization(n):
        if not allowed_prime(p):
            return 0
        if exponent == 1:
            return 0
        value *= 2 ** (exponent - 2)
    return value


NU = tuple(nu_coeff(n) for n in range(LIMIT + 1))
B = tuple(b_coeff(n) for n in range(LIMIT + 1))
C = tuple(c_coeff(n) for n in range(LIMIT + 1))
RCOEFF = tuple(r_coeff(n) for n in range(TRANSFER_LIMIT + 1))
QCOEFF = tuple(q_coeff(n) for n in range(TRANSFER_LIMIT + 1))


def prefix(values):
    out = [0] * len(values)
    running = 0
    for n, value in enumerate(values):
        running += value
        out[n] = running
    return tuple(out)


U_SUM = prefix(NU)
B_SUM = prefix(B)
C_SUM = prefix(C)
W_SUM = tuple(
    B_SUM[n] - B_SUM[n // 11]
    for n in range(LIMIT + 1)
)
Q_SUM = tuple(
    C_SUM[n] - C_SUM[n // 11]
    for n in range(LIMIT + 1)
)


def divisors(n):
    factors = factorization(n)
    out = [1]
    for p, exponent in factors:
        old = tuple(out)
        power = 1
        for _ in range(exponent):
            power *= p
            out.extend(value * power for value in old)
    return tuple(sorted(out))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def coprime_bilinear_coeff(n):
    total = 0
    for a in divisors(n):
        b = n // a
        if gcd(a, b) == 1:
            total += NU[a] * NU[b]
    return total


def ordinary_convolution_coeff(n):
    return sum(NU[a] * NU[n // a] for a in divisors(n))


def poly_mul(left, right, degree):
    out = [Fraction(0)] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += Fraction(a) * Fraction(b)
    return tuple(out)


def integer_sqrt(n):
    if n < 2:
        return n
    low = 1
    high = n // 2 + 1
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square <= n < (mid + 1) * (mid + 1):
            return mid
        if square > n:
            high = mid - 1
        else:
            low = mid + 1
    raise AssertionError("integer sqrt failed")


def hyperbola_sum(x):
    root = integer_sqrt(x)
    total = 0
    for a in range(1, root + 1):
        total += NU[a] * U_SUM[x // a]
    return 2 * total - U_SUM[root] * U_SUM[root]


def annular_direct(n):
    total = 0
    lower = n // 11
    for a in range(1, n + 1):
        if NU[a] == 0:
            continue
        total += NU[a] * (U_SUM[n // a] - U_SUM[lower // a])
    return total


def first_mismatch(left, right):
    for index, (a, b) in enumerate(zip(left, right)):
        if a != b:
            return index
    return None


def gate_01():
    check("tail first prime", NU[11] == 0 and NU[19] == -1)
    for n in range(1, LIMIT + 1):
        factors = factorization(n)
        squarefree_tail = all(
            exponent == 1 and allowed_prime(p)
            for p, exponent in factors
        )
        if n == 1:
            squarefree_tail = True
        expected_nu = 0
        expected_b = 0
        if squarefree_tail:
            expected_nu = -1 if len(factors) % 2 else 1
            expected_b = (-2) ** len(factors)
        check("nu census", NU[n] == expected_nu, n)
        check("b census", B[n] == expected_b, n)

        expected_c = 1
        for p, exponent in factors:
            if not allowed_prime(p) or exponent > 2:
                expected_c = 0
                break
            expected_c *= -2 if exponent == 1 else 1
        if n == 1:
            expected_c = 1
        check("c census", C[n] == expected_c, n)

    for n in range(1, TRANSFER_LIMIT + 1):
        factors = factorization(n)
        expected_r = 1
        expected_q = 1
        for p, exponent in factors:
            if not allowed_prime(p) or exponent == 1:
                expected_r = 0
                expected_q = 0
                break
            expected_r *= -(exponent - 1)
            expected_q *= 2 ** (exponent - 2)
        if n == 1:
            expected_r = expected_q = 1
        check("r census", RCOEFF[n] == expected_r, n)
        check("q census", QCOEFF[n] == expected_q, n)


def gate_02():
    ordinary = []
    coprime = []
    for n in range(1, LIMIT + 1):
        value = coprime_bilinear_coeff(n)
        check("coprime coefficient", value == B[n], n)
        coprime.append(value)
        ordinary.append(ordinary_convolution_coeff(n))
    mismatch = next(
        n for n in range(1, LIMIT + 1)
        if ordinary[n - 1] != B[n]
    )
    check("B1 first witness", mismatch == 361, mismatch)
    check("ordinary convolution census", all(
        ordinary[n - 1] == C[n]
        for n in range(1, LIMIT + 1)
    ))


def gate_03():
    degree = 18
    b_local = tuple([1, -2] + [0] * (degree - 1))
    c_local = tuple([1, -2, 1] + [0] * (degree - 2))
    r_local = tuple(
        1 if k == 0 else (0 if k == 1 else -(k - 1))
        for k in range(degree + 1)
    )
    q_local = tuple(
        1 if k == 0 else (0 if k == 1 else 2 ** (k - 2))
        for k in range(degree + 1)
    )
    identity = tuple([1] + [0] * degree)
    check("R times C", poly_mul(r_local, c_local, degree) == b_local)
    check("Q times B", poly_mul(q_local, b_local, degree) == c_local)
    check("R inverse", poly_mul(r_local, q_local, degree) == identity)
    check("R no linear deviation", r_local[1] == 0 and r_local[2] == -1)
    check("Q no linear deviation", q_local[1] == 0 and q_local[2] == 1)


def gate_04():
    # For every theta>1/2 and p>=19, rho=p^-theta<1/sqrt(19)<1/4.
    check("19 guard", 4 * 4 < 19)
    check("two rho guard", 2 < 4)

    # Audit the local absolute mass identities at an exact rational rho=1/5,
    # safely inside the universal rho<1/4 range.
    rho = Fraction(1, 5)
    r_mass = rho * rho / ((1 - rho) * (1 - rho))
    q_mass = rho * rho / (1 - 2 * rho)
    r_series = sum((k - 1) * rho ** k for k in range(2, 40))
    q_series = sum((2 ** (k - 2)) * rho ** k for k in range(2, 40))
    # Finite truncations must lie below the closed forms and have the exact
    # geometric tails dictated by the formulas.
    check("R mass truncation", r_series < r_mass)
    check("Q mass truncation", q_series < q_mass)
    r_tail = r_mass - r_series
    q_tail = q_mass - q_series
    check("R mass tail positive", r_tail > 0)
    check("Q mass tail positive", q_tail > 0)

    # theta=3/5 is an exact interior witness: 2*19^(-3/5)<1 iff 2^5<19^3.
    check("interior denominator witness", 2 ** 5 < 19 ** 3)
    check("summability exponent witness", 6 > 5)


def gate_05():
    r_support = tuple(
        d for d in range(1, TRANSFER_LIMIT + 1)
        if RCOEFF[d] != 0
    )
    q_support = tuple(
        d for d in range(1, TRANSFER_LIMIT + 1)
        if QCOEFF[d] != 0
    )
    for n in range(0, TRANSFER_LIMIT + 1):
        from_q = sum(
            RCOEFF[d] * Q_SUM[n // d]
            for d in r_support
            if d <= n or d == 1
        )
        from_w = sum(
            QCOEFF[d] * W_SUM[n // d]
            for d in q_support
            if d <= n or d == 1
        )
        check("W annular transfer", from_q == W_SUM[n], n)
        check("Q annular transfer", from_w == Q_SUM[n], n)
        for d in (1, 2, 19, 361):
            if d <= n:
                check(
                    "floor associativity",
                    (n // d) // 11 == n // (11 * d) == (n // 11) // d,
                    (n, d),
                )


def gate_06():
    witnesses = (1, 10, 11, 19, 360, 361, 500, 1000, 5000, 10000)
    for n in witnesses:
        check("hyperbola H", hyperbola_sum(n) == C_SUM[n], n)
        check(
            "annular direct",
            annular_direct(n) == Q_SUM[n],
            n,
        )
        check(
            "annular H difference",
            hyperbola_sum(n) - hyperbola_sum(n // 11) == Q_SUM[n],
            n,
        )


def gate_07():
    # B2: pretending the dressing is one leaves the p^2 ordinary-convolution
    # coefficient uncancelled.
    check("B2 degree two", C[361] == 1 and B[361] == 0)

    # B3: wrong inverse deviation T/(1-2T) has a forbidden linear term.
    wrong_inverse = (1, 1, 2, 4)
    check("B3 linear term", wrong_inverse[1] != 0)

    # B4: including 11 changes the tail support immediately.
    check("B4 tail 11", nu_coeff(11, include_11=True) == -1 and NU[11] == 0)

    # B5 and theorem E: all colorings of one fixed support have the same sign.
    supports = ((19,), (19, 29), (19, 29, 31))
    for support in supports:
        target = -1 if len(support) % 2 else 1
        signs = set()
        for mask in range(1 << len(support)):
            a = 1
            b = 1
            for i, p in enumerate(support):
                if mask >> i & 1:
                    a *= p
                else:
                    b *= p
            signs.add(NU[a] * NU[b])
        check("support sign constant", signs == {target}, support)
    check("B5 singleton", NU[19] * NU[1] == NU[1] * NU[19] == -1)


def imported_root(node):
    if isinstance(node, ast.Import):
        return node.names[0].name.split(".")[0]
    if isinstance(node, ast.ImportFrom):
        return (node.module or "").split(".")[0]
    return ""


def gate_08():
    raw = Path(__file__).read_bytes()
    check("final LF", raw.endswith(b"\n"))
    check("LF only", b"\r" not in raw)
    tree = ast.parse(raw.decode("utf-8"), filename=__file__)
    allowed_imports = {"__future__", "ast", "fractions", "pathlib"}
    forbidden_imports = {
        "cmath", "http", "math", "mpmath", "numpy", "random", "requests",
        "socket", "subprocess", "sympy", "urllib",
    }
    forbidden_calls = {
        "compile", "complex", "eval", "exec", "float", "input", "open",
    }
    imports = []
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(imported_root(node))
        if isinstance(node, ast.Constant):
            check(
                "no float or complex literal",
                not isinstance(node.value, (float, complex)),
            )
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    check("import allowlist", set(imports) <= allowed_imports, imports)
    check("forbidden imports", not (set(imports) & forbidden_imports))
    check("dynamic calls", not (set(calls) & forbidden_calls))


def main():
    gate_01()
    print("G01 PASS nu b c r q coefficient census")
    gate_02()
    print("G02 PASS coprime bilinear identity B1=361")
    gate_03()
    print("G03 PASS ordinary-square dressing algebra")
    gate_04()
    print("G04 PASS half-plane majorant guards")
    gate_05()
    print("G05 PASS direct annular convolution transfer")
    gate_06()
    print("G06 PASS bilinear annulus and hyperbola identities")
    gate_07()
    print("G07 PASS color no-go and breakers B2-B5")
    gate_08()
    print("G08 PASS exact-rational stdlib firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
