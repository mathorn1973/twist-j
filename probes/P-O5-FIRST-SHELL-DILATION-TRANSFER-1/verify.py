#!/usr/bin/env python3
"""Exact audit for P-O5-FIRST-SHELL-DILATION-TRANSFER-1."""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


LIMIT = 20000
SCALE = 11


def check(label, condition, detail=""):
    if not condition:
        raise AssertionError(f"{label} failed: {detail}")


def chi5(n):
    residue = n % 5
    if residue == 0:
        return 0
    return 1 if residue in (1, 4) else -1


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def split_primes(limit):
    return tuple(
        p for p in range(2, limit + 1)
        if is_prime(p) and chi5(p) == 1
    )


def coefficient_table(limit, include_11):
    primes = split_primes(limit)
    if not include_11:
        primes = tuple(p for p in primes if p > 11)
    coefficients = [0] * (limit + 1)
    coefficients[1] = 1

    def extend(start, product, coefficient):
        for index in range(start, len(primes)):
            prime = primes[index]
            nxt = product * prime
            if nxt > limit:
                break
            nxt_coefficient = -2 * coefficient
            check("unique squarefree support", coefficients[nxt] == 0, nxt)
            coefficients[nxt] = nxt_coefficient
            extend(index + 1, nxt, nxt_coefficient)

    extend(0, 1, 1)
    return tuple(coefficients)


def factor_integer(n):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            exponent = 0
            while n % divisor == 0:
                n //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def expected_coefficient(n, include_11):
    if n == 1:
        return 1
    factors = factor_integer(n)
    for prime, exponent in factors:
        if exponent != 1 or chi5(prime) != 1:
            return 0
        if not include_11 and prime <= 11:
            return 0
    return (-2) ** len(factors)


def prefix_sum(coefficients):
    out = [0] * len(coefficients)
    running = 0
    for index, value in enumerate(coefficients):
        running += value
        out[index] = running
    return tuple(out)


def dilates(N, scale=SCALE):
    values = []
    current = N
    while current > 0:
        values.append(current)
        current //= scale
    return tuple(values)


def poly_mul(left, right, degree):
    out = [Fraction(0)] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += Fraction(a) * Fraction(b)
    return tuple(out)


def first_mismatch(left, right):
    for index, (a, b) in enumerate(zip(left, right)):
        if a != b:
            return index
    return None


FULL_COEFFICIENTS = coefficient_table(LIMIT, include_11=True)
TAIL_COEFFICIENTS = coefficient_table(LIMIT, include_11=False)
S_VALUES = prefix_sum(FULL_COEFFICIENTS)
B_VALUES = prefix_sum(TAIL_COEFFICIENTS)
W_VALUES = tuple(
    B_VALUES[N] - B_VALUES[N // SCALE]
    for N in range(LIMIT + 1)
)


def gate_01():
    check("first split primes", split_primes(50) == (11, 19, 29, 31, 41))
    for n in range(1, LIMIT + 1):
        check(
            "full coefficient census",
            FULL_COEFFICIENTS[n] == expected_coefficient(n, True),
            n,
        )
        check(
            "tail coefficient census",
            TAIL_COEFFICIENTS[n] == expected_coefficient(n, False),
            n,
        )


def gate_02():
    witnesses = tuple(range(0, 5001)) + (10000, 20000)
    for N in witnesses:
        check(
            "optional 11 decomposition",
            S_VALUES[N] == B_VALUES[N] - 2 * B_VALUES[N // SCALE],
            N,
        )
        check(
            "annular difference",
            W_VALUES[N] == B_VALUES[N] - B_VALUES[N // SCALE],
            N,
        )
        interval = sum(
            TAIL_COEFFICIENTS[n]
            for n in range(N // SCALE + 1, N + 1)
        )
        check("first terminal shell", W_VALUES[N] == interval, N)


def gate_03():
    witnesses = tuple(range(1, 5001)) + (10000, 20000)
    for N in witnesses:
        orbit = dilates(N)
        from_w_to_b = sum(W_VALUES[value] for value in orbit)
        check("B inversion", from_w_to_b == B_VALUES[N], N)

        from_w_to_s = W_VALUES[N] - sum(
            W_VALUES[value] for value in orbit[1:]
        )
        check("S from W", from_w_to_s == S_VALUES[N], N)

        from_s_to_w = S_VALUES[N]
        for exponent, value in enumerate(orbit[1:]):
            from_s_to_w += (2 ** exponent) * S_VALUES[value]
        check("W from S", from_s_to_w == W_VALUES[N], N)


def gate_04():
    for n in range(1, LIMIT + 1):
        tail = TAIL_COEFFICIENTS[n]
        divided = TAIL_COEFFICIENTS[n // 11] if n % 11 == 0 else 0
        check(
            "coefficient S local factor",
            FULL_COEFFICIENTS[n] == tail - 2 * divided,
            n,
        )

    degree = 16
    one_minus_t = (1, -1)
    one_minus_two_t = (1, -2)
    ratio = tuple([1] + [2 ** (j - 1) for j in range(1, degree + 1)])
    inverse_ratio = tuple([1] + [-1] * degree)
    identity = tuple([1] + [0] * degree)
    check(
        "Dirichlet quotient series",
        poly_mul(one_minus_two_t, ratio, degree) == one_minus_t + (0,) * (degree - 1),
    )
    check(
        "inverse quotient series",
        poly_mul(one_minus_t, inverse_ratio, degree)
        == one_minus_two_t + (0,) * (degree - 1),
    )
    check(
        "quotient inverse",
        poly_mul(ratio, inverse_ratio, degree) == identity,
    )


def gate_05():
    degree = 18
    one_minus_d = (1, -1)
    one_minus_two_d = (1, -2)
    b_from_w = tuple([1] * (degree + 1))
    s_from_w = tuple([1] + [-1] * degree)
    b_from_s = tuple(2 ** j for j in range(degree + 1))
    w_from_s = tuple([1] + [2 ** (j - 1) for j in range(1, degree + 1)])
    identity = tuple([1] + [0] * degree)

    check("B Neumann inverse", poly_mul(one_minus_d, b_from_w, degree) == identity)
    check(
        "S from W operator",
        poly_mul(one_minus_two_d, b_from_w, degree) == s_from_w,
    )
    check("S Neumann inverse", poly_mul(one_minus_two_d, b_from_s, degree) == identity)
    check(
        "W from S operator",
        poly_mul(one_minus_d, b_from_s, degree) == w_from_s,
    )
    check("one third accepted", 2 ** 3 < 11)
    check("one quarter rejected", 2 ** 4 > 11)


def gate_06():
    # Exact algebra for the two absolute coefficient sums.  The universal
    # weighted-norm estimate is proved in PREREG.md from ||D^j||<=11^(-j theta).
    x = Fraction(1, 5)
    first_constant = Fraction(1, 1 - x)
    inverse_constant = Fraction(1 - x, 1 - 2 * x)
    check(
        "first geometric constant",
        first_constant == 1 + x / (1 - x),
    )
    check(
        "inverse geometric constant",
        inverse_constant == 1 + x / (1 - 2 * x),
    )
    check("positive inverse denominator", 1 - 2 * x > 0)


def gate_07():
    wrong_b1 = tuple(
        B_VALUES[N] - B_VALUES[N // 11]
        for N in range(LIMIT + 1)
    )
    check("B1 first witness", first_mismatch(S_VALUES, wrong_b1) == 11)

    wrong_scale = tuple(
        B_VALUES[N] - B_VALUES[N // 19]
        for N in range(LIMIT + 1)
    )
    check("B2 first witness", first_mismatch(W_VALUES, wrong_scale) == 11)

    wrong_b_inversion = [0] * (LIMIT + 1)
    for N in range(1, LIMIT + 1):
        wrong_b_inversion[N] = sum(W_VALUES[value] for value in dilates(N)[1:])
    check("B3 first witness", first_mismatch(B_VALUES, wrong_b_inversion) == 1)

    wrong_inverse = [0] * (LIMIT + 1)
    for N in range(1, LIMIT + 1):
        wrong_inverse[N] = S_VALUES[N] + sum(
            S_VALUES[value] for value in dilates(N)[1:]
        )
    check("B4 first witness", first_mismatch(W_VALUES, wrong_inverse) == 121)

    check("B5 quarter threshold fires", 2 ** 4 > 11 and 2 ** 3 < 11)


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
    print("G01 PASS split and tail coefficient census")
    gate_02()
    print("G02 PASS optional-11 and first-shell identities")
    gate_03()
    print("G03 PASS three finite dilation inversions")
    gate_04()
    print("G04 PASS Dirichlet local-factor quotient")
    gate_05()
    print("G05 PASS exact Neumann operator algebra")
    gate_06()
    print("G06 PASS weighted geometric constants")
    gate_07()
    print("G07 PASS breakers B1=11 B2=11 B3=1 B4=121 B5=1/4")
    gate_08()
    print("G08 PASS exact-rational stdlib firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
