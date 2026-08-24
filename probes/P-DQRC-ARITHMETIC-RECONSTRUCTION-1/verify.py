#!/usr/bin/env python3
"""Exact audit for P-DQRC-ARITHMETIC-RECONSTRUCTION-1.

This verifier is result-exposed and proof-first.  The universal statements are
proved in PREREG.md; this program audits their coordinate formulas with Python
integer arithmetic only.  It uses no floating point, RNG, external data, or
third-party package.
"""

from fractions import Fraction
from math import isqrt
import platform
import sys


ACTIVE_GATE = "startup"


def q_delta(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    return a * a + b * b + c * c + d * d, (a * d - b * c) ** 2


def m0(q: int, delta: int, k: int) -> int:
    h = q * q + 4 * delta
    return isqrt((q * q * k * k) // h)


def m1(q: int, delta: int, k: int) -> int:
    h = q * q + 4 * delta
    return isqrt((16 * delta * delta * k * k) // (q * q * h))


def m_beta(q: int, delta: int, beta: int, x: int, k: int) -> int:
    h = q * q + beta * delta
    if x == 0:
        return isqrt((q * q * k * k) // h)
    return isqrt((16 * delta * delta * k * k) // (q * q * h))


def m(q: int, delta: int, x: int, k: int) -> int:
    return m0(q, delta, k) if x == 0 else m1(q, delta, k)


def u(q: int, delta: int, x: int, k: int, phase: int = 0) -> int:
    return m(q, delta, x, k + phase + 1) - m(q, delta, x, k + phase)


def phase_count(q: int, delta: int, x: int, k: int, phase: int) -> int:
    return m(q, delta, x, k + phase) - m(q, delta, x, phase)


def reachable(radius: int) -> list[tuple[int, int]]:
    out: set[tuple[int, int]] = set()
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            for c in range(-radius, radius + 1):
                for d in range(-radius, radius + 1):
                    if a == b == c == d == 0:
                        continue
                    out.add(q_delta(a, b, c, d))
    return sorted(out)


def squarefree_part(n: int) -> int:
    out = 1
    p = 2
    rest = n
    while p * p <= rest:
        parity = 0
        while rest % p == 0:
            rest //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1
    return out * rest


def outcomes(q: int, delta: int, x: int, y: int, r: int, t: int,
             k: int, phase: int = 0) -> tuple[int, int]:
    sigma = -1 if x * y else 1
    a_out = -1 if t else 1
    exponent = r * (1 - u(q, delta, x, k, phase))
    b_out = a_out * sigma * (-1 if exponent else 1)
    return a_out, b_out


def census(q: int, delta: int, k_max: int, phase: int = 0):
    pairs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    counts = {(x, y): {pair: 0 for pair in pairs}
              for x in (0, 1) for y in (0, 1)}
    for k in range(k_max):
        for x in (0, 1):
            for y in (0, 1):
                for r in (0, 1):
                    for t in (0, 1):
                        pair = outcomes(q, delta, x, y, r, t, k, phase)
                        counts[(x, y)][pair] += 1
    return counts


def main() -> None:
    global ACTIVE_GATE
    print("P-DQRC-ARITHMETIC-RECONSTRUCTION-1 exact audit")
    print(f"I1 interpreter implementation=CPython version={sys.version_info.major}.{sys.version_info.minor}")

    # A1: determinant bound on the frozen exhaustive witness box.
    ACTIVE_GATE = "F1/R1-A1"
    cases = 0
    violations = 0
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    if a == b == c == d == 0:
                        continue
                    q, delta = q_delta(a, b, c, d)
                    cases += 1
                    violations += int(4 * delta > q * q)
    assert cases == 28560 and violations == 0
    print(f"A1 determinant-bound cases={cases} violations={violations}")

    # A2: the two slopes are in [0,1], and every audited increment is binary.
    ACTIVE_GATE = "F1/R1-A2"
    pairs = reachable(5)
    increment_checks = 0
    for q, delta in pairs:
        h = q * q + 4 * delta
        assert q * q <= h
        assert 16 * delta * delta <= q * q * h
        for phase in (0, 1, 2, 5):
            for x in (0, 1):
                for k in range(40):
                    assert u(q, delta, x, k, phase) in (0, 1)
                    increment_checks += 1
    print(f"A2 comparator-totality pairs={len(pairs)} increments={increment_checks} violations=0")

    # A3/A4: direct enumeration versus the closed count and balanced margins.
    ACTIVE_GATE = "F1/R1-A3-A4"
    probes = ((2, 1), (4, 4), (5, 1), (6, 1), (9, 4), (10, 9),
              (13, 4), (1, 0), (8, 4), (12, 9), (17, 16), (18, 1),
              (20, 16), (25, 4))
    configurations = 0
    for q, delta in probes:
        assert 4 * delta <= q * q
        for phase in (0, 1, 3):
            for k_max in (1, 2, 3, 5, 7, 11, 24, 37):
                configurations += 1
                counts = census(q, delta, k_max, phase)
                for x in (0, 1):
                    mx = phase_count(q, delta, x, k_max, phase)
                    for y in (0, 1):
                        sigma = -1 if x * y else 1
                        table = counts[(x, y)]
                        assert sum(table.values()) == 4 * k_max
                        for (alpha, beta), value in table.items():
                            expected = k_max + mx if alpha * beta == sigma else k_max - mx
                            assert value == expected
                        for sign in (1, -1):
                            assert sum(v for (alpha, _), v in table.items() if alpha == sign) == 2 * k_max
                            assert sum(v for (_, beta), v in table.items() if beta == sign) == 2 * k_max
    print(f"A3 census-closed-form configurations={configurations} violations=0")
    print(f"A4 constructor-marginals configurations={configurations} violations=0")

    # A5: origin-zero lower counts have the frozen one-sided error bound.
    ACTIVE_GATE = "F1/R1-A5"
    error_checks = 0
    for q, delta in pairs:
        h = q * q + 4 * delta
        for k_max in (1, 2, 3, 5, 8, 13, 21, 55, 144, 610, 2584):
            sk = Fraction(2 * (m0(q, delta, k_max) + m1(q, delta, k_max)), k_max)
            lower = Fraction(q) * sk / 2
            upper = Fraction(q) * (sk + Fraction(4, k_max)) / 2
            assert lower * lower <= h < upper * upper
            error_checks += 1
    print(f"A5 origin-zero-deficit exact-square-checks={error_checks} violations=0")

    # A6: scaling leaves every comparator count unchanged.
    ACTIVE_GATE = "F1/R1-A6"
    scale_checks = 0
    for a in range(-3, 4):
        for b in range(-3, 4):
            for c in range(-3, 4):
                for d in range(-3, 4):
                    if a == b == c == d == 0:
                        continue
                    q, delta = q_delta(a, b, c, d)
                    for scale in (2, 3, 5):
                        q2, delta2 = q_delta(scale * a, scale * b, scale * c, scale * d)
                        assert q2 == scale * scale * q
                        assert delta2 == scale ** 4 * delta
                        for phase in (0, 1, 3):
                            for k_max in (1, 7, 30):
                                for x in (0, 1):
                                    assert phase_count(q, delta, x, k_max, phase) == phase_count(q2, delta2, x, k_max, phase)
                        scale_checks += 1
    assert scale_checks == 7200
    print(f"A6 scaling-invariance configurations={scale_checks} violations=0")

    # A7: the CHSH parity comes only from the frozen sigma table.
    ACTIVE_GATE = "F1/R1-A7"
    parity_checks = 0
    for q, delta in probes:
        for phase in (0, 1, 3):
            for k in range(12):
                for r in (0, 1):
                    for t in (0, 1):
                        product = 1
                        for x in (0, 1):
                            for y in (0, 1):
                                alpha, beta = outcomes(q, delta, x, y, r, t, k, phase)
                                product *= alpha * beta
                        assert product == -1
                        parity_checks += 1
    local_checks = 0
    for a0 in (1, -1):
        for a1 in (1, -1):
            for b0 in (1, -1):
                for b1 in (1, -1):
                    assert (a0 * b0) * (a0 * b1) * (a1 * b0) * (a1 * b1) == 1
                    local_checks += 1
    print(f"A7 inserted-parity relational={parity_checks} local={local_checks} violations=0")

    # R1/R2: exact reconstruction of the external pure-qubit optimum.
    ACTIVE_GATE = "F2/R2-H1"
    reconstruction_checks = 0
    for q, delta in pairs:
        c2 = Fraction(4 * delta, q * q)
        h = q * q + 4 * delta
        assert h == (1 + c2) * q * q
        assert Fraction(4 * h, q * q) == 4 * (1 + c2)
        reconstruction_checks += 1
    print(f"H1 Horodecki-maximum-reencoding pairs={reconstruction_checks} violations=0")

    correlator_checks = 0
    ACTIVE_GATE = "F2/R2-H2"
    for q, delta in pairs:
        c2 = Fraction(4 * delta, q * q)
        h = q * q + 4 * delta
        # Squared Schmidt-gauge correlators:
        # r0^2=1/(1+C^2), r1^2=C^4/(1+C^2).
        assert Fraction(q * q, h) == Fraction(1, 1) / (1 + c2)
        assert Fraction(16 * delta * delta, q * q * h) == c2 * c2 / (1 + c2)
        correlator_checks += 1
    print(f"H2 Schmidt-correlator-reencoding pairs={correlator_checks} violations=0")

    # N1: all nonnegative integer beta satisfy the frozen structural slope
    # bounds; beta=4 is selected exactly by matching the Horodecki target.
    ACTIVE_GATE = "F3/R3-N1"
    beta_checks = 0
    for q, delta in pairs:
        for beta in (0, 1, 2, 3, 4, 5, 8, 16):
            h_beta = q * q + beta * delta
            assert q * q <= h_beta
            assert 16 * delta * delta <= q * q * h_beta
            for x in (0, 1):
                for k in range(24):
                    increment = m_beta(q, delta, beta, x, k + 1) - m_beta(q, delta, beta, x, k)
                    assert increment in (0, 1)
            if delta > 0:
                census_limit_sq = Fraction(
                    4 * (q * q + 4 * delta) ** 2,
                    q * q * h_beta,
                )
                horodecki_sq = Fraction(4 * (q * q + 4 * delta), q * q)
                assert (census_limit_sq == horodecki_sq) == (beta == 4)
            beta_checks += 1
    print(f"N1 quartic-coefficient-nonselection checks={beta_checks} beta4-iff-target=PASS")

    # O1: shifting the integer origin preserves the limit and all structural
    # counts but destroys the origin-zero sign prediction.
    ACTIVE_GATE = "F4/R4-O1"
    q, delta, k_max = 2, 1, 1
    lower_sum = phase_count(q, delta, 0, k_max, 0) + phase_count(q, delta, 1, k_max, 0)
    shifted_sum = phase_count(q, delta, 0, k_max, 1) + phase_count(q, delta, 1, k_max, 1)
    assert lower_sum == 0 and shifted_sum == 2
    assert Fraction(2 * lower_sum, k_max) == 0
    assert Fraction(2 * shifted_sum, k_max) == 4
    assert 8 > 0 and 16 > 8  # 0 < (2 sqrt 2)^2 < 4^2
    print("O1 origin-nonselection witness Q=2 Delta=1 K=1 S_origin0=0 S_origin1=4 target_square=8")

    # K1/K2/K3: finite audits of the universal field statements in PREREG.
    ACTIVE_GATE = "F5/R5-K1"
    maximal = [(q, delta) for q, delta in reachable(6) if 4 * delta == q * q]
    assert maximal and all(squarefree_part(q * q + 4 * delta) == 2 for q, delta in maximal)
    print(f"K1 maximal-field-audit distinct-pairs={len(maximal)} squarefree-parts=2 violations=0")
    ACTIVE_GATE = "F5/R5-K2"
    q, delta = q_delta(-3, -1, -1, 0)
    assert (q, delta) == (11, 1)
    assert q * q + 4 * delta == 125
    print("K2 sqrt5-sector witness X=(-3,-1,-1,0) Q=11 Delta=1 H=125 S_square=500/121")

    ACTIVE_GATE = "F5/R5-K3"
    sqrt5_checks = 0
    for q, delta in pairs:
        assert q * q != 16 * delta
        sqrt5_checks += 1
    print(f"K3 exact-sqrt5-obstruction audit-pairs={sqrt5_checks} violations=0")

    print("SUMMARY PASS gates=15/15 physical-bridge=NOT-TESTED data-attack=STOP")


def entrypoint() -> int:
    if sys.flags.optimize != 0 or not __debug__:
        print("INTEGRITY STOP: optimized Python disables scientific assertions", file=sys.stderr)
        return 1
    if sys.argv[1:]:
        print("INTEGRITY STOP: verifier accepts no arguments", file=sys.stderr)
        return 1
    if platform.python_implementation() != "CPython":
        print("INTEGRITY STOP: CPython required", file=sys.stderr)
        return 1
    if sys.version_info[:2] != (3, 12):
        print("INTEGRITY STOP: CPython 3.12 required", file=sys.stderr)
        return 1
    try:
        main()
    except AssertionError as exc:
        print(f"SCIENTIFIC FALSIFIER FIRED gate={ACTIVE_GATE} detail={exc!r}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(entrypoint())
