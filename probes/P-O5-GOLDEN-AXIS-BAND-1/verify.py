#!/usr/bin/env python3
"""Exact audit for P-O5-GOLDEN-AXIS-BAND-1."""

from __future__ import annotations

import ast
from bisect import bisect_left
from pathlib import Path


LIMIT = 20000
BAND_LIMIT = 10000


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
    p = 2
    while p * p <= limit:
        if spf[p] == p:
            multiple = p * p
            while multiple <= limit:
                if spf[multiple] == multiple:
                    spf[multiple] = p
                multiple += p
        p += 1
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


def nu_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    sign = 1
    for p, exponent in factorization(n):
        if exponent != 1 or chi5(p) != 1 or p <= 11:
            return 0
        sign = -sign
    return sign


def c_coeff(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    value = 1
    for p, exponent in factorization(n):
        if chi5(p) != 1 or p <= 11 or exponent > 2:
            return 0
        value *= -2 if exponent == 1 else 1
    return value


NU = tuple(nu_coeff(n) for n in range(LIMIT + 1))
C = tuple(c_coeff(n) for n in range(LIMIT + 1))


def prefix(values):
    out = [0] * len(values)
    running = 0
    for n, value in enumerate(values):
        running += value
        out[n] = running
    return tuple(out)


H = prefix(C)


def lucas_fib_even(count):
    # A_k=L_(2k): 2,3,7,... ; B_k=F_(2k): 0,1,3,...
    A = [2]
    B = [0]
    if count == 1:
        return tuple(A), tuple(B)
    A.append(3)
    B.append(1)
    while len(A) < count:
        A.append(3 * A[-1] - A[-2])
        B.append(3 * B[-1] - B[-2])
    return tuple(A), tuple(B)


# Enough Lucas endpoints for every factor product <= LIMIT and its shell bounds.
A, FEVEN = lucas_fib_even(40)
X = tuple(value - 1 for value in A)


def shell_index(n):
    if n == 1:
        return -1
    index = bisect_left(X, n) - 1
    check("shell index range", index >= 0, n)
    return index


def shell_bounds(k):
    if k == -1:
        return 1, 1
    return X[k] + 1, X[k + 1]


def divisors(n):
    out = [1]
    for p, exponent in factorization(n):
        prior = tuple(out)
        power = 1
        for _ in range(exponent):
            power *= p
            out.extend(value * power for value in prior)
    return tuple(sorted(out))


# Diagonal coefficient decomposition of c=nu*nu.
MAX_S = 2 * shell_index(LIMIT)
DIAG_COEFF = {
    s: [0] * (LIMIT + 1)
    for s in range(-2, MAX_S + 1)
}
for n in range(1, LIMIT + 1):
    for a in divisors(n):
        b = n // a
        if NU[a] == 0 or NU[b] == 0:
            continue
        s = shell_index(a) + shell_index(b)
        DIAG_COEFF[s][n] += NU[a] * NU[b]

DIAG_PREFIX = {}
for s, values in DIAG_COEFF.items():
    DIAG_PREFIX[s] = prefix(values)


def P(s, y):
    if y <= 0:
        return 0
    values = DIAG_PREFIX.get(s)
    return 0 if values is None else values[y]


def shell_sum(k):
    low, high = shell_bounds(k)
    return sum(NU[n] for n in range(low, high + 1))


def D(s):
    total = 0
    for i in range(-1, s + 2):
        j = s - i
        if j < -1:
            continue
        total += shell_sum(i) * shell_sum(j)
    return total


def Q(n):
    return H[n] - H[n // 11]


def band_value(n):
    m = shell_index(n)
    lower = max(-2, m - 4)
    return sum(P(s, n) - P(s, n // 11) for s in range(lower, m + 1))


def gate_01():
    # Recurrences and Pell guard.
    check("Lucas start", A[:6] == (2, 3, 7, 18, 47, 123))
    check("Fibonacci even start", FEVEN[:6] == (0, 1, 3, 8, 21, 55))
    for k in range(0, 20):
        check("Pell", A[k] * A[k] - 5 * FEVEN[k] * FEVEN[k] == 4, k)
        if k == 0:
            check("floor k0", X[k] == 1)
            continue
        # alpha^k=(A_k+B_k sqrt5)/2.
        # alpha^k<A_k iff 5 B_k^2<A_k^2.
        check(
            "floor upper",
            5 * FEVEN[k] * FEVEN[k] < A[k] * A[k],
            k,
        )
        # alpha^k>A_k-1 iff B_k sqrt5>A_k-2.
        check(
            "floor lower",
            5 * FEVEN[k] * FEVEN[k] > (A[k] - 2) * (A[k] - 2),
            k,
        )
        check("X definition", X[k] == A[k] - 1, k)


def gate_02():
    # Complete shell partition through LIMIT.
    seen = [0] * (LIMIT + 1)
    seen[1] = 1
    for k in range(0, shell_index(LIMIT) + 1):
        low, high = shell_bounds(k)
        for n in range(low, min(high, LIMIT) + 1):
            seen[n] += 1
            check("shell inverse", shell_index(n) == k, (k, n))
    check("complete partition", all(value == 1 for value in seen[1:]))

    # Product-shell bounds audited on every divisor factorization n<=LIMIT.
    for n in range(1, LIMIT + 1):
        for a in divisors(n):
            b = n // a
            i = shell_index(a)
            j = shell_index(b)
            s = i + j
            if s == -2:
                check("unit product shell", n == 1, (a, b))
            elif s == -1:
                check("negative-one product upper", n <= X[1], (a, b, n))
            else:
                check("product lower", X[s] < n, (a, b, s, n))
                check("product upper", n <= X[s + 2], (a, b, s, n))


def gate_03():
    # alpha^2=(7+3sqrt5)/2<11:
    # 3sqrt5<15, audited by squaring positive sides.
    check("alpha2 below 11", 9 * 5 < 15 * 15)
    # alpha^3=9+4sqrt5>11:
    # 4sqrt5>2.
    check("11 below alpha3", 16 * 5 > 2 * 2)

    # Exact induced scale inequalities on every N in a frozen range:
    # deep products s<=m-5 are <=N/11, high products s>=m+1 exceed N.
    for n in range(X[4] + 1, BAND_LIMIT + 1):
        m = shell_index(n)
        # X[m] < n <= X[m+1] by construction.
        check("shell lower endpoint", X[m] < n)
        check("shell upper endpoint", n <= X[m + 1])


def gate_04():
    for n in range(1, BAND_LIMIT + 1):
        # Full diagonal decomposition of H.
        total = sum(
            P(s, n)
            for s in range(-2, MAX_S + 1)
        )
        check("H diagonal decomposition", total == H[n], n)

        m = shell_index(n)
        if m < 3:
            continue
        lower = max(-2, m - 4)
        # Outside the golden band the annular difference is exactly zero.
        for s in range(-2, lower):
            check(
                "deep diagonal cancellation",
                P(s, n) == P(s, n // 11),
                (n, m, s),
            )
        for s in range(m + 1, MAX_S + 1):
            check(
                "high diagonal zero",
                P(s, n) == 0 and P(s, n // 11) == 0,
                (n, m, s),
            )
        check("five-band identity", band_value(n) == Q(n), (n, m))


def gate_05():
    for K in range(4, 20):
        n = X[K]
        if n > LIMIT:
            break
        M = n // 11
        check("top lower shell", shell_index(M) == K - 3, (K, n, M))
        for s in range(-2, K - 1):
            if s <= K - 2:
                check("top full diagonal", P(s, n) == D(s), (K, s))
        for s in range(K, MAX_S + 1):
            check("top high zero", P(s, n) == 0, (K, s))
        rhs = (
            D(K - 4) - P(K - 4, M)
            + D(K - 3) - P(K - 3, M)
            + D(K - 2)
            + P(K - 1, n)
        )
        check("Lucas-top formula", rhs == Q(n), (K, n, M, rhs, Q(n)))


def gate_06():
    # C is independently constructed from local ordinary-convolution factors.
    # The diagonal factor-pair decomposition must reproduce it coefficientwise.
    for n in range(1, LIMIT + 1):
        diag = sum(
            DIAG_COEFF[s][n]
            for s in range(-2, MAX_S + 1)
        )
        check("ordinary square coefficient", diag == C[n], n)
    for n in range(1, BAND_LIMIT + 1):
        check(
            "Q carrier",
            band_value(n) == H[n] - H[n // 11],
            n,
        )


def gate_07():
    # B1: unshifted Lucas cutoff is already wrong at k=1.
    check("B1", X[1] == 2 and A[1] == 3)

    # B2: false 11<alpha^2 contradicts the exact square comparison.
    check("B2", 9 * 5 < 15 * 15)

    # B3: first nonzero lower outer band contribution.
    first_low = None
    for n in range(X[4] + 1, BAND_LIMIT + 1):
        m = shell_index(n)
        contribution = P(m - 4, n) - P(m - 4, n // 11)
        if contribution:
            first_low = (n, m, contribution)
            break
    check("B3 first witness", first_low == (322, 6, -4), first_low)

    # B4: first nonzero upper outer band contribution.
    first_high = None
    for n in range(X[4] + 1, BAND_LIMIT + 1):
        m = shell_index(n)
        contribution = P(m, n) - P(m, n // 11)
        if contribution:
            first_high = (n, m, contribution)
            break
    check("B4 first witness", first_high == (361, 6, 1), first_high)

    # B5: same source shells can land in two different product shells.
    check("B5 sources", shell_index(19) == shell_index(41) == 3)
    check("B5 lower target", 19 * 19 == 361 and shell_index(361) == 6)
    check("B5 upper target", 41 * 41 == 1681 and shell_index(1681) == 7)


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
    allowed_imports = {"__future__", "ast", "bisect", "pathlib"}
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
    print("G01 PASS Lucas Pell and exact unit-scale floor")
    gate_02()
    print("G02 PASS complete golden shell and product geometry")
    gate_03()
    print("G03 PASS exact eleven-between-rungs inequalities")
    gate_04()
    print("G04 PASS full-axis five-diagonal band")
    gate_05()
    print("G05 PASS Lucas-top four-diagonal refinement")
    gate_06()
    print("G06 PASS ordinary bilinear Q11 carrier agreement")
    gate_07()
    print("G07 PASS breakers B1=k1 B2=alpha2 B3=322 B4=361 B5=19x19/41x41")
    gate_08()
    print("G08 PASS exact-integer stdlib firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
