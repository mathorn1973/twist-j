#!/usr/bin/env python3
"""P-O5-SQUAREFREE-CORE-1 exact audit.

Frozen scope:
  * exact local O_p = A_p (1-2T) factorization;
  * exact cubic onset of A_p and A_p^{-1};
  * squarefree coefficient formula s_5 = mu * a_F * 1_(5 does not divide n);
  * finite audits of both Dirichlet convolutions;
  * five production-path negative controls.

No analytic continuation, zeta zero, RH/GRH, floating point, or external data.
"""

from __future__ import annotations

import ast
from pathlib import Path


N_COEFF = 50_000
N_CONV = 20_000
SERIES_DEGREE = 16

# Public split-prime local factor O_p(T)=(1-T)^2/(1+T^2).
O_NUM = [1, -2, 1]
O_DEN = [1, 0, 1]

# Frozen squarefree core S_p(T)=1-2T.
CORE = [1, -2]


def trim(a: list[int]) -> list[int]:
    out = list(a)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sub(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
    return trim(out)


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def rat_equal(n1: list[int], d1: list[int], n2: list[int], d2: list[int]) -> bool:
    return trim(mul(n1, d2)) == trim(mul(n2, d1))


def series_div(num: list[int], den: list[int], degree: int) -> list[int]:
    assert den and den[0] == 1
    out = [0] * (degree + 1)
    for k in range(degree + 1):
        rhs = num[k] if k < len(num) else 0
        for j in range(1, min(k, len(den) - 1) + 1):
            rhs -= den[j] * out[k - j]
        out[k] = rhs
    return out


def series_mul(a: list[int], b: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, x in enumerate(a):
        if i > degree:
            break
        for j, y in enumerate(b):
            if i + j > degree:
                break
            out[i + j] += x * y
    return out


A_NUM = list(O_NUM)
A_DEN = mul(O_DEN, CORE)
AINV_NUM = list(A_DEN)
AINV_DEN = list(A_NUM)

A_SERIES = series_div(A_NUM, A_DEN, SERIES_DEGREE)
AINV_SERIES = series_div(AINV_NUM, AINV_DEN, SERIES_DEGREE)
O_SERIES = series_div(O_NUM, O_DEN, SERIES_DEGREE)


def chi5_prime(p: int) -> int:
    r = p % 5
    if r == 0:
        return 0
    if r in (1, 4):
        return 1
    return -1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def spf_sieve(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    p = 2
    while p * p <= limit:
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
        p += 1
    return spf


def factor(n: int, spf: list[int]) -> list[tuple[int, int]]:
    if n == 1:
        return []
    out: list[tuple[int, int]] = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out


def mu_value(fac: list[tuple[int, int]]) -> int:
    for _, e in fac:
        if e >= 2:
            return 0
    return -1 if len(fac) % 2 else 1


def ideal_count(fac: list[tuple[int, int]]) -> int:
    out = 1
    for p, e in fac:
        chi = chi5_prime(p)
        if chi == 1:
            out *= e + 1
        elif chi == -1:
            if e % 2:
                return 0
        else:
            # p=5 is ramified: exactly one ideal at each prime-power norm.
            pass
    return out


def s_core_coeff(fac: list[tuple[int, int]]) -> int:
    out = 1
    for p, e in fac:
        if chi5_prime(p) != 1 or e != 1:
            return 0
        out *= -2
    return out


def s_core_coeff_mut_inert_two(fac: list[tuple[int, int]]) -> int:
    out = 1
    for p, e in fac:
        if (chi5_prime(p) != 1 and p != 2) or e != 1:
            return 0
        out *= -2
    return out


def o_local(e: int) -> int:
    if e == 0:
        return 1
    if e % 2 == 0:
        return 0
    j = (e - 1) // 2
    return -2 if j % 2 == 0 else 2


def o_coeff(fac: list[tuple[int, int]]) -> int:
    out = 1
    for p, e in fac:
        if chi5_prime(p) != 1:
            return 0
        out *= o_local(e)
    return out


def a_coeff(fac: list[tuple[int, int]], local: list[int]) -> int:
    out = 1
    for p, e in fac:
        if chi5_prime(p) != 1:
            return 0
        assert e < len(local)
        out *= local[e]
        if out == 0:
            return 0
    return out


def dirichlet_convolution(x: list[int], y: list[int], limit: int) -> list[int]:
    out = [0] * (limit + 1)
    for d in range(1, limit + 1):
        xd = x[d]
        if xd == 0:
            continue
        m = 1
        while d * m <= limit:
            ym = y[m]
            if ym:
                out[d * m] += xd * ym
            m += 1
    return out


def first_series_defect(num: list[int], den: list[int], degree: int) -> int:
    q = series_div(num, den, degree)
    for k in range(1, degree + 1):
        if q[k] != 0:
            return k
    return -1


def gate_source_firewall() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    allowed = {"__future__", "ast", "pathlib"}
    forbidden_calls = {"float", "complex", "eval", "exec"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert alias.name.split(".")[0] in allowed
        elif isinstance(node, ast.ImportFrom):
            assert (node.module or "").split(".")[0] in allowed
        elif isinstance(node, ast.Constant):
            assert not isinstance(node.value, (float, complex))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in forbidden_calls


def main() -> int:
    # G01: exact local factorization.
    assert rat_equal(mul(A_NUM, CORE), A_DEN, O_NUM, O_DEN)
    print("G01 PASS local O_p = A_p (1-2T)")

    # G02: both local deviations start exactly at T^3.
    assert sub(A_NUM, A_DEN) == [0, 0, 0, 2]
    assert sub(AINV_NUM, AINV_DEN) == [0, 0, 0, -2]
    assert A_SERIES[:3] == [1, 0, 0]
    assert AINV_SERIES[:3] == [1, 0, 0]
    assert A_SERIES[3] == 2
    assert AINV_SERIES[3] == -2
    print("G02 PASS dressing and inverse have exact cubic onset")

    # G03: 11 is the first split prime, and 11^(-1/3) < 9/20 < 1/2.
    primes = [n for n in range(2, 12) if is_prime(n)]
    split = [p for p in primes if chi5_prime(p) == 1]
    assert primes == [2, 3, 5, 7, 11]
    assert split == [11]
    assert 11 * 9**3 > 20**3
    assert 2 * 9 < 20
    print("G03 PASS first split prime 11 and exact 9/20 guard")

    # Build exact arithmetic tables once.
    spf = spf_sieve(N_COEFF)
    factors = [factor(n, spf) if n else [] for n in range(N_COEFF + 1)]

    # G04: all-n written formula, bounded exact audit.
    first_formula_defect = None
    for n in range(1, N_COEFF + 1):
        fac = factors[n]
        lhs = s_core_coeff(fac)
        rhs = mu_value(fac) * ideal_count(fac) * (0 if n % 5 == 0 else 1)
        if lhs != rhs:
            first_formula_defect = n
            break
    assert first_formula_defect is None
    print(f"G04 PASS s_5=mu*a_F*1_(5nmid) through n={N_COEFF}")

    # G05: local power-series products through the frozen degree.
    core_series = [0] * (SERIES_DEGREE + 1)
    core_series[0] = 1
    core_series[1] = -2
    identity_series = [0] * (SERIES_DEGREE + 1)
    identity_series[0] = 1
    assert series_mul(A_SERIES, core_series, SERIES_DEGREE) == O_SERIES
    assert series_mul(A_SERIES, AINV_SERIES, SERIES_DEGREE) == identity_series
    print(f"G05 PASS local formal series through degree {SERIES_DEGREE}")

    # G06: exact rational majorant constants used by the written proof.
    # At r0=9/20:
    # 2/((1-r0^2)(1-2r0)) = 8000/319 < 26.
    # 2/(1-r0)^2 = 800/121 < 7.
    assert 8000 < 26 * 319
    assert 800 < 7 * 121
    print("G06 PASS exact local majorants 26*p^(-3theta), 7*p^(-3theta)")

    # G07: both global Dirichlet convolutions, bounded exact audit.
    s = [0] * (N_CONV + 1)
    o = [0] * (N_CONV + 1)
    a = [0] * (N_CONV + 1)
    b = [0] * (N_CONV + 1)
    for n in range(1, N_CONV + 1):
        fac = factors[n]
        s[n] = s_core_coeff(fac)
        o[n] = o_coeff(fac)
        a[n] = a_coeff(fac, A_SERIES)
        b[n] = a_coeff(fac, AINV_SERIES)
    assert dirichlet_convolution(a, s, N_CONV) == o
    assert dirichlet_convolution(b, o, N_CONV) == s
    print(f"G07 PASS both Dirichlet convolutions through n={N_CONV}")

    # G08: source firewall.
    gate_source_firewall()
    print("G08 PASS stdlib-only exact-integer source firewall")

    # G09: all five frozen production-path breakers.
    b1_num = O_NUM
    b1_den = mul(O_DEN, [1, -1])
    b2_num = O_NUM
    b2_den = mul(O_DEN, O_NUM)
    assert first_series_defect(b1_num, b1_den, 4) == 1
    assert first_series_defect(b2_num, b2_den, 4) == 2

    b3_first = None
    b4_first = None
    for n in range(1, 200):
        fac = factors[n]
        actual = s_core_coeff(fac)
        no_cutoff = mu_value(fac) * ideal_count(fac)
        inert_two = s_core_coeff_mut_inert_two(fac)
        if b3_first is None and actual != no_cutoff:
            b3_first = n
        if b4_first is None and actual != inert_two:
            b4_first = n
    assert b3_first == 5
    assert b4_first == 2

    a_mut_num = O_NUM
    a_mut_den = CORE
    assert not rat_equal(mul(a_mut_num, CORE), a_mut_den, O_NUM, O_DEN)
    assert 11**2 == 121
    print("G09 PASS breakers FIRE B1=11 B2=121 B3=5 B4=2 B5=local")

    print("VERIFY RESULT 9/9 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
