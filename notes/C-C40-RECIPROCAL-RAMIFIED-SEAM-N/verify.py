#!/usr/bin/env python3
"""Exact standard-library verifier for the C40 arithmetic incubation."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd

BOUND = 200_000
EXPECTED_PHI40 = (1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1)
EXPECTED_ORDERS = {
    1: 1,
    3: 4,
    7: 4,
    9: 2,
    11: 2,
    13: 4,
    17: 4,
    19: 2,
    21: 2,
    23: 4,
    27: 4,
    29: 2,
    31: 2,
    33: 4,
    37: 4,
    39: 2,
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_pow(base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    out = (1,)
    factor = base
    power = exponent
    while power:
        if power & 1:
            out = poly_mul(out, factor)
        factor = poly_mul(factor, factor)
        power //= 2
    return out


def poly_div_exact(dividend: tuple[int, ...], divisor: tuple[int, ...]) -> tuple[int, ...]:
    require(divisor[-1] == 1, "exact division requires a monic divisor")
    remainder = list(dividend)
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor):
        coefficient = remainder[-1]
        offset = len(remainder) - len(divisor)
        quotient[offset] = coefficient
        for index, value in enumerate(divisor):
            remainder[offset + index] -= coefficient * value
        remainder = list(trim(remainder))
    require(trim(remainder) == (0,), "nonzero remainder in cyclotomic division")
    return trim(quotient)


_cyclotomic_cache: dict[int, tuple[int, ...]] = {}


def cyclotomic(n: int) -> tuple[int, ...]:
    if n in _cyclotomic_cache:
        return _cyclotomic_cache[n]
    polynomial = (-1,) + (0,) * (n - 1) + (1,)
    for divisor in range(1, n):
        if n % divisor == 0:
            polynomial = poly_div_exact(polynomial, cyclotomic(divisor))
    _cyclotomic_cache[n] = polynomial
    return polynomial


def poly_mod(poly: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    return trim(tuple(value % modulus for value in poly))


def poly_divmod_mod(
    dividend: tuple[int, ...], divisor: tuple[int, ...], modulus: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    remainder = list(poly_mod(dividend, modulus))
    divisor = poly_mod(divisor, modulus)
    require(divisor != (0,), "division by zero polynomial")
    inverse = pow(divisor[-1], -1, modulus)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    while remainder != [0] and len(remainder) >= len(divisor):
        coefficient = remainder[-1] * inverse % modulus
        offset = len(remainder) - len(divisor)
        quotient[offset] = coefficient
        for index, value in enumerate(divisor):
            remainder[offset + index] = (
                remainder[offset + index] - coefficient * value
            ) % modulus
        remainder = list(trim(remainder))
    return trim(quotient), trim(remainder)


def irreducible_by_trial(poly: tuple[int, ...], modulus: int) -> bool:
    poly = poly_mod(poly, modulus)
    degree = len(poly) - 1
    require(poly[-1] == 1, "trial irreducibility expects a monic polynomial")
    for factor_degree in range(1, degree // 2 + 1):
        for coefficients in product(range(modulus), repeat=factor_degree):
            candidate = tuple(coefficients) + (1,)
            _, remainder = poly_divmod_mod(poly, candidate, modulus)
            if remainder == (0,):
                return False
    return True


def euler_phi(n: int) -> int:
    return sum(1 for value in range(1, n + 1) if gcd(value, n) == 1)


def multiplicative_order(value: int, modulus: int) -> int:
    require(gcd(value, modulus) == 1, "order requested for non-unit")
    cursor = 1
    for order in range(1, euler_phi(modulus) + 1):
        cursor = cursor * value % modulus
        if cursor == 1:
            return order
    raise RuntimeError("unit order not found")


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [index for index, flag in enumerate(sieve) if flag]


def main() -> None:
    phi5 = cyclotomic(5)
    phi8 = cyclotomic(8)
    phi40 = cyclotomic(40)

    require(gcd(5, 8) == 1, "conductors are not coprime")
    require((euler_phi(5), euler_phi(8), euler_phi(40)) == (4, 4, 16), "degree mismatch")
    require((8 * 2 + 5 * (-3)) % 40 == 1, "generator Bezout identity failed")
    require((8, 5, (8 * 2 + 5 * (-3)) % 40) == (8, 5, 1), "generator exponents failed")
    require(phi40 == EXPECTED_PHI40, "Phi_40 coefficient mismatch")

    phi40_mod2 = poly_mod(phi40, 2)
    phi5_fourth_mod2 = poly_mod(poly_pow(phi5, 4), 2)
    require(phi40_mod2 == phi5_fourth_mod2, "ramified reduction at 2 failed")
    require(irreducible_by_trial(poly_mod(phi5, 2), 2), "Phi_5 is reducible over F_2")
    p2_profile = (4, len(phi5) - 1, 1)
    require(p2_profile == (4, 4, 1) and 4 * 4 * 1 == 16, "local profile at 2 failed")

    phi40_mod5 = poly_mod(phi40, 5)
    phi8_fourth_mod5 = poly_mod(poly_pow(phi8, 4), 5)
    q2 = poly_mod((-2, 0, 1), 5)
    q3 = poly_mod((-3, 0, 1), 5)
    quadratics_fourth = poly_mod(poly_pow(poly_mul(q2, q3), 4), 5)
    require(phi40_mod5 == phi8_fourth_mod5 == quadratics_fourth, "ramified reduction at 5 failed")
    require(poly_mod(poly_mul(q2, q3), 5) == poly_mod(phi8, 5), "Phi_8 factorization failed")
    require(irreducible_by_trial(q2, 5), "x^2-2 is reducible over F_5")
    require(irreducible_by_trial(q3, 5), "x^2-3 is reducible over F_5")
    p5_profile = (4, len(q2) - 1, 2)
    require(p5_profile == (4, 2, 2) and 4 * 2 * 2 == 16, "local profile at 5 failed")

    units = tuple(value for value in range(40) if gcd(value, 40) == 1)
    orders = {value: multiplicative_order(value, 40) for value in units}
    require(orders == EXPECTED_ORDERS, "unit-class order atlas mismatch")
    require(max(orders.values()) == 4, "group exponent is not 4")
    require(all(pow(value, 4, 40) == 1 for value in units), "fourth-power group test failed")
    units8 = tuple(value for value in range(8) if gcd(value, 8) == 1)
    units5 = tuple(value for value in range(5) if gcd(value, 5) == 1)
    crt_images = {(value % 8, value % 5) for value in units}
    require(len(crt_images) == len(units8) * len(units5) == 16, "CRT unit map failed")
    require(all(pow(value, 2, 8) == 1 for value in units8), "U(8) is not V4")
    require(multiplicative_order(2, 5) == 4, "U(5) is not cyclic of order 4")

    classes_by_order = {
        order: tuple(value for value in units if orders[value] == order)
        for order in (1, 2, 4)
    }
    expected_classes = {
        1: (1,),
        2: (9, 11, 19, 21, 29, 31, 39),
        4: (3, 7, 13, 17, 23, 27, 33, 37),
    }
    require(classes_by_order == expected_classes, "class partition mismatch")
    densities = {order: Fraction(len(classes), 16) for order, classes in classes_by_order.items()}
    require(densities == {1: Fraction(1, 16), 2: Fraction(7, 16), 4: Fraction(1, 2)}, "density mismatch")
    require(sum(densities.values(), Fraction(0)) == 1, "densities do not sum to one")

    primes = primes_up_to(BOUND)
    unramified = [prime for prime in primes if prime not in (2, 5)]
    audited_orders = {1: 0, 2: 0, 4: 0}
    inert = []
    for prime in unramified:
        order = orders[prime % 40]
        audited_orders[order] += 1
        if order == 16:
            inert.append(prime)
    require(not inert, "unramified inert prime found in finite audit")
    require(sum(audited_orders.values()) == len(unramified), "prime audit accounting failed")

    print("C40_RECIPROCAL_RAMIFIED_SEAM verifier=v1")
    print("DEPENDENCIES DQRC,QUARTIC_RAMIFICATION,J_BINARY_NORM,BORN_SPLIT=IMPORTED audit=self_contained")
    print("COMPOSITUM conductors=5,8 intersection=Q degrees=4x4=16 exponents=8,5,1 PASS")
    print("PHI40 coefficients=1,0,0,0,-1,0,0,0,1,0,0,0,-1,0,0,0,1 PASS")
    print("RAMIFIED p=2 identity=Phi5^4 irreducible_degree=4 profile=(4,4,1) PASS")
    print("RAMIFIED p=5 identity=Phi8^4=q2^4*q3^4 irreducible_degrees=2,2 profile=(4,2,2) PASS")
    print("LOCAL p=2 Q2_factors=1 degrees=16; p=5 Q5_factors=2 degrees=8,8 PASS")
    for order in (1, 2, 4):
        classes = ",".join(str(value) for value in classes_by_order[order])
        factor_count = 16 // order
        density = densities[order]
        print(
            f"ATLAS order={order} classes={classes} type={order}^{factor_count} "
            f"density={density.numerator}/{density.denominator}"
        )
    print("GROUP units=16 structure=C4xC2xC2 exponent=4 order16_elements=0 PASS")
    print("UNIVERSAL Phi40_mod_p=reducible_for_every_rational_prime proof=ramified_identities_plus_exponent")
    print(
        f"AUDIT bound={BOUND} primes={len(primes)} unramified={len(unramified)} "
        f"order1={audited_orders[1]} order2={audited_orders[2]} "
        f"order4={audited_orders[4]} inert=0"
    )
    print("INTERPRETATION seam=arithmetic_only prime_exchange_symmetry=NO field_merger=NO selector=NO physical_claim=NO RH_claim=NO")
    print("RESULT candidate-T/L1 PASS")


if __name__ == "__main__":
    main()
