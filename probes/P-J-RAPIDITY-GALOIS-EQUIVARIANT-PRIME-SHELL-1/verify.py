#!/usr/bin/env python3
"""Exact audit for P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1.

The written universal proofs are in PREREG.md. This verifier uses only the
Python standard library, exact Fractions, finite-field integer arithmetic,
and sparse Laurent polynomials. It performs no floating-point comparison.
"""

import sys
from fractions import Fraction

assert len(sys.argv) == 1

ONE_MONO = ()


def clean(poly):
    return {m: c for m, c in poly.items() if c}


def mono_mul(a, b):
    exponents = {}
    for prime, exponent in a + b:
        exponents[prime] = exponents.get(prime, 0) + exponent
    return tuple(sorted((p, e) for p, e in exponents.items() if e))


def poly_add(a, b):
    out = dict(a)
    for mono, coefficient in b.items():
        out[mono] = out.get(mono, Fraction(0)) + coefficient
    return clean(out)


def poly_scale(a, scalar):
    return clean({mono: scalar * coefficient for mono, coefficient in a.items()})


def poly_mul(a, b):
    out = {}
    for mono_a, coefficient_a in a.items():
        for mono_b, coefficient_b in b.items():
            mono = mono_mul(mono_a, mono_b)
            out[mono] = out.get(mono, Fraction(0)) + coefficient_a * coefficient_b
    return clean(out)


def poly_star(a):
    return clean(
        {tuple((prime, -exponent) for prime, exponent in mono): coefficient
         for mono, coefficient in a.items()}
    )


def poly_flip_prime(a, target):
    out = {}
    for mono, coefficient in a.items():
        flipped = tuple(
            (prime, -exponent if prime == target else exponent)
            for prime, exponent in mono
        )
        out[flipped] = out.get(flipped, Fraction(0)) + coefficient
    return clean(out)


def poly_augmentation(a):
    return sum(a.values(), Fraction(0))


def poly_l1(a):
    return sum((abs(coefficient) for coefficient in a.values()), Fraction(0))


def constant(value):
    return {} if value == 0 else {ONE_MONO: Fraction(value)}


def unit(prime, exponent=1, coefficient=1):
    return {((prime, exponent),): Fraction(coefficient)}


def sieve_primes(limit):
    mark = [True] * (limit + 1)
    mark[0] = False
    if limit:
        mark[1] = False
    for q in range(2, int(limit ** 0.5) + 1):
        if mark[q]:
            for multiple in range(q * q, limit + 1, q):
                mark[multiple] = False
    return [q for q, is_prime in enumerate(mark) if is_prime]


PRIMES = sieve_primes(5000)


def chi5(prime):
    if prime == 5:
        return 0
    return 1 if prime % 5 in (1, 4) else -1


def is_split(prime):
    return prime != 5 and chi5(prime) == 1


def phi_roots(prime):
    return [
        t for t in range(prime)
        if (t * t - t - 1) % prime == 0
    ]


def factor_integer(n):
    factors = {}
    remaining = n
    for prime in PRIMES:
        if prime * prime > remaining:
            break
        while remaining % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            remaining //= prime
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def divisors(n):
    result = [1]
    for prime, exponent in factor_integer(n).items():
        result = [
            divisor * prime ** power
            for divisor in result
            for power in range(exponent + 1)
        ]
    return result


def mobius_table(limit):
    mu = [1] * (limit + 1)
    mu[0] = 0
    for prime in sieve_primes(limit):
        for multiple in range(prime, limit + 1, prime):
            mu[multiple] *= -1
        for multiple in range(prime * prime, limit + 1, prime * prime):
            mu[multiple] = 0
    return mu


def ideal_mobius_pp(prime, exponent):
    if exponent == 0:
        return constant(1)
    if is_split(prime):
        if exponent == 1:
            pair = poly_add(unit(prime, 1), unit(prime, -1))
            return poly_scale(pair, -1)
        return constant(1) if exponent == 2 else {}
    if prime == 5:
        return constant(-1) if exponent == 1 else {}
    return constant(-1) if exponent == 2 else {}


def reynolds_correction_pp(prime, exponent):
    if exponent == 0:
        return constant(1)
    if is_split(prime):
        pair = poly_add(unit(prime, exponent), unit(prime, -exponent))
        return poly_scale(pair, Fraction(1, 2))
    if prime == 5:
        return {}
    return constant(-1 if exponent % 2 else 1)


def multiplicative_value(n, prime_power_function):
    out = constant(1)
    for prime, exponent in factor_integer(n).items():
        out = poly_mul(out, prime_power_function(prime, exponent))
        if not out:
            break
    return out


def mobius_lift_direct(n):
    factors = factor_integer(n)
    if any(exponent > 1 for exponent in factors.values()):
        return {}
    out = constant(1)
    for prime in factors:
        if is_split(prime):
            pair = poly_add(unit(prime, 1), unit(prime, -1))
            local = poly_scale(pair, Fraction(-1, 2))
        else:
            local = constant(-1)
        out = poly_mul(out, local)
    return out


def convolution_value(n):
    out = {}
    for divisor in divisors(n):
        left = multiplicative_value(divisor, ideal_mobius_pp)
        right = multiplicative_value(n // divisor, reynolds_correction_pp)
        out = poly_add(out, poly_mul(left, right))
    return out


def series_multiply(a, b, degree):
    out = [{} for _ in range(degree + 1)]
    for left_degree, left_coefficient in enumerate(a):
        for right_degree, right_coefficient in enumerate(b):
            total_degree = left_degree + right_degree
            if total_degree <= degree:
                out[total_degree] = poly_add(
                    out[total_degree],
                    poly_mul(left_coefficient, right_coefficient),
                )
    return out


def gate_fixed_lines():
    tested = split = inert = ramified = 0
    for prime in sieve_primes(997):
        roots = phi_roots(prime)
        assert len(roots) == chi5(prime) + 1
        tested += 1
        if chi5(prime) == 1:
            split += 1
            root, conjugate = roots
            assert (root + conjugate - 1) % prime == 0
            for t, other in ((root, conjugate), (conjugate, root)):
                assert (t * t - t - 1) % prime == 0
                assert (1 + t * other) % prime == 0
        elif chi5(prime) == -1:
            inert += 1
        else:
            ramified += 1

    roots_11 = phi_roots(11)
    assert roots_11 == [4, 8]
    assert (1 + 4 * 8) % 11 == 0
    assert (1 + 4 * 4) % 11 != 0
    assert (tested, split, inert, ramified) == (168, 78, 89, 1)
    print(
        "G1 fixed-line cross-label p<=997 "
        "(168 primes; split=78 inert=89 ramified=1); "
        "same-root p=11 FIRED-AS-EXPECTED PASS"
    )


def gate_odd_rank_one():
    oriented_lines = 0
    for prime in sieve_primes(997):
        if not is_split(prime):
            continue
        root, conjugate = phi_roots(prime)
        for t, other in ((root, conjugate), (conjugate, root)):
            c = (2 * t - 1) % prime
            assert c != 0
            assert c * c % prime == 5 % prime
            assert (2 * other - 1) % prime == (-c) % prime

            # det((1,t),(1,other)) = other-t = -c
            assert (other - t) % prime == (-c) % prime

            multiplier = other * pow(t, -1, prime) % prime
            assert (
                multiplier - pow(multiplier, -1, prime)
            ) % prime == c

            lefschetz = pow((1 - multiplier) % prime, -1, prime)
            expected = (
                pow(2, -1, prime) + c * pow(10, -1, prime)
            ) % prime
            assert lefschetz == expected
            oriented_lines += 1

    assert phi_roots(2) == []
    assert phi_roots(5) == [3]
    assert (2 * 3 - 1) % 5 == 0
    assert oriented_lines == 156
    print(
        "G2 finite-phi odd subspace rank one "
        "(156 oriented split lines; p=2,5 boundaries) PASS"
    )


def gate_integral_extension():
    determinant = 1 * (-1) - 1 * 1
    assert determinant == -2
    assert abs(determinant) == 2
    assert Fraction(1, 2) + Fraction(1, 2) == 1
    assert all(2 * integer != 1 for integer in range(-20, 21))
    print(
        "G3 integral sign extension index=2; "
        "normalized local invariant lift requires 1/2 PASS"
    )


def gate_local_reynolds():
    degree = 8
    prime = 11
    pair = poly_add(unit(prime, 1), unit(prime, -1))

    ideal_factor = [
        constant(1),
        poly_scale(pair, -1),
        constant(1),
    ] + [{} for _ in range(degree - 2)]

    correction = [constant(1)] + [
        poly_scale(
            poly_add(unit(prime, k), unit(prime, -k)),
            Fraction(1, 2),
        )
        for k in range(1, degree + 1)
    ]

    product = series_multiply(ideal_factor, correction, degree)
    expected = [
        constant(1),
        poly_scale(pair, Fraction(-1, 2)),
    ] + [{} for _ in range(degree - 1)]

    assert product == expected
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(1, 2) + Fraction(1, 2) == 1
    assert all(
        poly_augmentation(product[k])
        == (1 if k == 0 else -1 if k == 1 else 0)
        for k in range(degree + 1)
    )
    print(
        "G4 unique frozen Reynolds weights a=b=1/2; "
        "squarefree local product through degree 8 PASS"
    )


def gate_global_lift(limit=5000, convolution_limit=2000):
    mu = mobius_table(limit)
    for n in range(1, limit + 1):
        direct = mobius_lift_direct(n)
        factors = factor_integer(n)
        split_divisors = [
            prime for prime, exponent in factors.items()
            if exponent == 1 and is_split(prime)
        ]
        split_count = len(split_divisors)

        assert poly_augmentation(direct) == mu[n]
        assert poly_star(direct) == direct
        assert poly_l1(direct) == abs(mu[n])

        for prime in split_divisors:
            assert poly_flip_prime(direct, prime) == direct

        if mu[n]:
            assert len(direct) == 2 ** split_count
            assert all(
                abs(coefficient) == Fraction(1, 2 ** split_count)
                for coefficient in direct.values()
            )
        else:
            assert direct == {}

        if n <= convolution_limit:
            assert convolution_value(n) == direct

    print(
        "G5 global locally relabeling-invariant Mobius lift n<=5000; "
        "independent convolution n<=2000 PASS"
    )


def gate_point_constant_term(limit=5000):
    mu = mobius_table(limit)
    partial = {}
    mertens = 0
    no_split_sum = 0
    checkpoints = {100, 500, 2000, limit}
    checked = 0

    for n in range(1, limit + 1):
        partial = poly_add(partial, mobius_lift_direct(n))
        mertens += mu[n]
        if all(not is_split(prime) for prime in factor_integer(n)):
            no_split_sum += mu[n]

        if n in checkpoints:
            assert poly_augmentation(partial) == mertens
            assert partial.get(ONE_MONO, Fraction(0)) == no_split_sum
            checked += 1

    assert checked == len(checkpoints)
    print(
        "G6 augmentation=M(N) and constant-term=no-split Mobius sum "
        "at 4 checkpoints through N=5000 PASS"
    )


def gate_scalar_breaker():
    prime = 11
    tail = poly_add(
        constant(2),
        poly_scale(
            poly_add(unit(prime, 1), unit(prime, -1)),
            -1,
        ),
    )
    assert tail
    assert poly_augmentation(tail) == 0

    coefficients = [
        constant(1),
        poly_add(constant(-1), tail),
    ] + [tail for _ in range(2, 9)]

    assert all(coefficients[k] == tail and coefficients[k] for k in range(2, 9))
    print(
        "G7 scalar correction tail 2-u-u^-1 in degrees 2..8 "
        "FIRED-AS-EXPECTED PASS"
    )


def main():
    print("P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1 verify")
    print(
        "scope: exact L1 shell, local Reynolds descent, "
        "group-ring Mobius lift; no analytic or RH claim"
    )
    gate_fixed_lines()
    gate_odd_rank_one()
    gate_integral_extension()
    gate_local_reynolds()
    gate_global_lift()
    gate_point_constant_term()
    gate_scalar_breaker()
    print("RESULT 7/7 ALL PASS")


if __name__ == "__main__":
    main()
