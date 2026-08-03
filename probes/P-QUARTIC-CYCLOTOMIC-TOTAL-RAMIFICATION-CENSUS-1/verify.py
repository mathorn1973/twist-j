#!/usr/bin/env python3
"""Exact audit for P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1.

The theorem is proved in PREREG.md.  This standard-library program audits
the finite exact certificates in that proof.  It must not be executed before
the public preregistration pin.
"""

from itertools import product
import sys


CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def trim(poly):
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or (0,))


def divisors(n):
    return tuple(value for value in range(1, n + 1) if n % value == 0)


def factor_integer(n):
    factors = {}
    value = n
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            factors[prime] = factors.get(prime, 0) + 1
            value //= prime
        prime += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors


def is_prime(n):
    if n < 2:
        return False
    return factor_integer(n) == {n: 1}


def totient(n):
    result = n
    for prime in factor_integer(n):
        result = result // prime * (prime - 1)
    return result


def poly_mul_int(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def poly_exact_div(dividend, divisor):
    numerator = list(trim(dividend))
    denominator = trim(divisor)
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    while len(numerator) >= len(denominator) and trim(numerator) != (0,):
        shift = len(numerator) - len(denominator)
        lead = numerator[-1]
        divisor_lead = denominator[-1]
        if lead % divisor_lead:
            raise AssertionError("non-exact polynomial division")
        coefficient = lead // divisor_lead
        quotient[shift] += coefficient
        for index, value in enumerate(denominator):
            numerator[shift + index] -= coefficient * value
        numerator = list(trim(numerator))
    if trim(numerator) != (0,):
        raise AssertionError("polynomial remainder is nonzero")
    return trim(quotient)


_CYCLOTOMIC = {}


def cyclotomic(n):
    if n not in _CYCLOTOMIC:
        polynomial = (-1,) + (0,) * (n - 1) + (1,)
        for divisor in divisors(n):
            if divisor < n:
                polynomial = poly_exact_div(polynomial, cyclotomic(divisor))
        _CYCLOTOMIC[n] = trim(polynomial)
    return _CYCLOTOMIC[n]


def poly_eval(poly, value):
    result = 0
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def poly_derivative(poly):
    return trim(tuple(index * poly[index] for index in range(1, len(poly))))


def determinant_bareiss(matrix):
    values = [list(row) for row in matrix]
    size = len(values)
    if size == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if values[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if values[row][pivot_index] != 0
                ),
                None,
            )
            if swap is None:
                return 0
            values[pivot_index], values[swap] = values[swap], values[pivot_index]
            sign *= -1
        pivot = values[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    values[row][column] * pivot
                    - values[row][pivot_index] * values[pivot_index][column]
                )
                if numerator % previous:
                    raise AssertionError("Bareiss division is non-exact")
                values[row][column] = numerator // previous
            values[row][pivot_index] = 0
        previous = pivot
    return sign * values[-1][-1]


def resultant(left, right):
    left = trim(left)
    right = trim(right)
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    size = left_degree + right_degree
    left_descending = tuple(reversed(left))
    right_descending = tuple(reversed(right))
    rows = []
    for shift in range(right_degree):
        rows.append(
            (0,) * shift
            + left_descending
            + (0,) * (size - shift - len(left_descending))
        )
    for shift in range(left_degree):
        rows.append(
            (0,) * shift
            + right_descending
            + (0,) * (size - shift - len(right_descending))
        )
    return determinant_bareiss(rows)


def polynomial_discriminant(poly):
    degree = len(trim(poly)) - 1
    sign = -1 if (degree * (degree - 1) // 2) & 1 else 1
    return sign * resultant(poly, poly_derivative(poly)) // poly[-1]


def cyclotomic_discriminant(n):
    degree = totient(n)
    numerator = n**degree
    denominator = 1
    for prime in factor_integer(n):
        denominator *= prime ** (degree // (prime - 1))
    sign = -1 if (degree // 2) & 1 else 1
    return sign * (numerator // denominator)


def z5_mul(left, right):
    product_coefficients = [0] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product_coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        top = product_coefficients[degree]
        if top:
            for shift in range(4):
                product_coefficients[degree - 4 + shift] -= top
            product_coefficients[degree] = 0
    return tuple(product_coefficients[:4])


def z5_pow(value, exponent):
    result = (1, 0, 0, 0)
    base = value
    power = exponent
    while power:
        if power & 1:
            result = z5_mul(result, base)
        base = z5_mul(base, base)
        power >>= 1
    return result


def z5_poly_eval(poly, value):
    result = (0, 0, 0, 0)
    for coefficient in reversed(poly):
        result = z5_mul(result, value)
        result = (result[0] + coefficient, result[1], result[2], result[3])
    return result


def mod_poly(poly, prime):
    return trim(tuple(coefficient % prime for coefficient in poly))


def poly_mul_mod(left, right, prime):
    return mod_poly(poly_mul_int(left, right), prime)


def poly_pow_mod(value, exponent, prime):
    result = (1,)
    base = mod_poly(value, prime)
    power = exponent
    while power:
        if power & 1:
            result = poly_mul_mod(result, base, prime)
        base = poly_mul_mod(base, base, prime)
        power >>= 1
    return result


def poly_divmod_mod(dividend, divisor, prime):
    numerator = list(mod_poly(dividend, prime))
    denominator = mod_poly(divisor, prime)
    quotient = [0] * max(1, len(numerator) - len(denominator) + 1)
    inverse_lead = pow(denominator[-1], -1, prime)
    while len(numerator) >= len(denominator) and trim(numerator) != (0,):
        shift = len(numerator) - len(denominator)
        coefficient = numerator[-1] * inverse_lead % prime
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            numerator[shift + index] = (
                numerator[shift + index] - coefficient * value
            ) % prime
        numerator = list(trim(numerator))
    return mod_poly(quotient, prime), mod_poly(numerator, prime)


def monic_polynomials(prime, degree):
    for coefficients in product(range(prime), repeat=degree):
        yield tuple(coefficients) + (1,)


def is_irreducible_mod(poly, prime):
    degree = len(trim(poly)) - 1
    if degree <= 1:
        return True
    for factor_degree in range(1, degree // 2 + 1):
        for candidate in monic_polynomials(prime, factor_degree):
            _, remainder = poly_divmod_mod(poly, candidate, prime)
            if remainder == (0,):
                return False
    return True


def factor_monic_mod(poly, prime):
    remaining = mod_poly(poly, prime)
    factors = []
    original_degree = len(remaining) - 1
    for degree in range(1, original_degree + 1):
        for candidate in monic_polynomials(prime, degree):
            if not is_irreducible_mod(candidate, prime):
                continue
            exponent = 0
            while len(remaining) - 1 >= degree:
                quotient, remainder = poly_divmod_mod(remaining, candidate, prime)
                if remainder != (0,):
                    break
                remaining = quotient
                exponent += 1
            if exponent:
                factors.append((candidate, exponent))
            if remaining == (1,):
                return tuple(factors)
    if remaining != (1,):
        raise AssertionError("finite-field factorization incomplete")
    return tuple(factors)


def factor_profile(factors):
    return tuple((exponent, len(factor) - 1) for factor, exponent in factors)


def field_mul(left, right, prime, modulus):
    degree = len(modulus) - 1
    coefficients = [0] * (2 * degree - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i + j] = (coefficients[i + j] + a * b) % prime
    for top_degree in range(2 * degree - 2, degree - 1, -1):
        top = coefficients[top_degree] % prime
        if top:
            for index in range(degree):
                coefficients[top_degree - degree + index] = (
                    coefficients[top_degree - degree + index]
                    - top * modulus[index]
                ) % prime
    return tuple(value % prime for value in coefficients[:degree])


def field_pow(value, exponent, prime, modulus):
    one = (1,) + (0,) * (len(modulus) - 2)
    result = one
    base = value
    power = exponent
    while power:
        if power & 1:
            result = field_mul(result, base, prime, modulus)
        base = field_mul(base, base, prime, modulus)
        power >>= 1
    return result


def field_order(value, prime, modulus):
    one = (1,) + (0,) * (len(modulus) - 2)
    field_size = prime ** (len(modulus) - 1)
    current = one
    for exponent in range(1, field_size):
        current = field_mul(current, value, prime, modulus)
        if current == one:
            return exponent
    return 0


def field_summary(prime, modulus):
    degree = len(modulus) - 1
    elements = tuple(product(range(prime), repeat=degree))
    zero = (0,) * degree
    units = tuple(value for value in elements if value != zero)
    orders = tuple(field_order(value, prime, modulus) for value in units)
    size = prime**degree
    all_fermat = all(
        field_pow(value, size - 1, prime, modulus)
        == (1,) + (0,) * (degree - 1)
        for value in units
    )
    return size, len(units), max(orders), all_fermat


# 01: finite certificate derived from the prime-factor formula for phi.
target = 4
allowed_primes = tuple(
    sorted(
        divisor + 1
        for divisor in divisors(target)
        if is_prime(divisor + 1)
    )
)
prime_power_options = {}
for prime in allowed_primes:
    options = [(1, 1)]
    exponent = 1
    while True:
        contribution = prime ** (exponent - 1) * (prime - 1)
        if target % contribution:
            break
        options.append((prime**exponent, contribution))
        exponent += 1
    prime_power_options[prime] = tuple(options)
phi_four = set()
for option_tuple in product(*(prime_power_options[p] for p in allowed_primes)):
    n = 1
    phi_contribution = 1
    for prime_power, contribution in option_tuple:
        n *= prime_power
        phi_contribution *= contribution
    if phi_contribution == target:
        phi_four.add(n)
phi_certificate_ok = allowed_primes == (2, 3, 5)
phi_certificate_ok &= prime_power_options == {
    2: ((1, 1), (2, 1), (4, 2), (8, 4)),
    3: ((1, 1), (3, 2)),
    5: ((1, 1), (5, 4)),
}
phi_certificate_ok &= phi_four == {5, 8, 10, 12}
phi_certificate_ok &= all(totient(n) == target for n in phi_four)
check(
    "01 TOTIENT      prime-factor certificate gives phi(n)=4 exactly for n={5,8,10,12}",
    phi_certificate_ok,
)


# 02: reconstruct the four cyclotomic polynomials and the field quotient.
expected_cyclotomic = {
    5: (1, 1, 1, 1, 1),
    8: (1, 0, 0, 0, 1),
    10: (1, -1, 1, -1, 1),
    12: (1, 0, -1, 0, 1),
}
cyclotomic_ok = all(
    cyclotomic(n) == expected
    for n, expected in expected_cyclotomic.items()
)
zeta_5 = (0, 1, 0, 0)
zeta_10_inside_k5 = (0, 0, 0, -1)
field_quotient_ok = z5_pow(zeta_10_inside_k5, 2) == zeta_5
field_quotient_ok &= z5_pow(zeta_10_inside_k5, 5) == (-1, 0, 0, 0)
field_quotient_ok &= z5_pow(zeta_10_inside_k5, 10) == (1, 0, 0, 0)
field_quotient_ok &= z5_poly_eval(cyclotomic(10), zeta_10_inside_k5) == (0, 0, 0, 0)
check(
    "02 FIELDS       Phi_5,Phi_8,Phi_10,Phi_12 are reconstructed and zeta_10=-zeta_5^3 with zeta_10^2=zeta_5",
    cyclotomic_ok and field_quotient_ok,
)


# 03: independently compare the cyclotomic formula and polynomial resultants.
expected_discriminants = {5: 125, 8: 256, 10: 125, 12: 144}
discriminants = {
    n: cyclotomic_discriminant(n) for n in expected_discriminants
}
discriminant_ok = discriminants == expected_discriminants
discriminant_ok &= all(
    polynomial_discriminant(cyclotomic(n)) == value
    for n, value in expected_discriminants.items()
)
discriminant_ok &= len({discriminants[n] for n in (5, 8, 12)}) == 3
check(
    "03 DISCRIMINANT disc(K5)=5^3, disc(K8)=2^8, disc(K10)=5^3, disc(K12)=2^4*3^2 by formula and resultant",
    discriminant_ok,
)


# 04-05: exact reductions and independent finite-field factorization.
displayed_factors = {
    (5, 5): ((4, 1), 4),
    (8, 2): ((1, 1), 4),
    (12, 2): ((1, 1, 1), 2),
    (12, 3): ((1, 0, 1), 2),
}
reductions_ok = all(
    mod_poly(cyclotomic(n), prime)
    == poly_pow_mod(factor, exponent, prime)
    for (n, prime), (factor, exponent) in displayed_factors.items()
)
reductions_ok &= is_irreducible_mod((1, 1, 1), 2)
reductions_ok &= is_irreducible_mod((1, 0, 1), 3)
check(
    "04 REDUCTIONS   the four frozen cyclotomic reductions and both quadratic irreducibility claims are exact",
    reductions_ok,
)


factorizations = {
    key: factor_monic_mod(cyclotomic(key[0]), key[1])
    for key in displayed_factors
}
expected_factorizations = {
    key: ((factor, exponent),)
    for key, (factor, exponent) in displayed_factors.items()
}
factorization_ok = factorizations == expected_factorizations
factorization_ok &= factor_profile(factorizations[(5, 5)]) == ((4, 1),)
factorization_ok &= factor_profile(factorizations[(8, 2)]) == ((4, 1),)
factorization_ok &= factor_profile(factorizations[(12, 2)]) == ((2, 2),)
factorization_ok &= factor_profile(factorizations[(12, 3)]) == ((2, 2),)
factorization_ok &= all(
    sum(exponent * (len(factor) - 1) for factor, exponent in factors) == 4
    for factors in factorizations.values()
)
check(
    "05 PROFILES     independent factorization gives (e,f,g)=(4,1,1),(4,1,1),(2,2,1),(2,2,1)",
    factorization_ok,
)


# 06: discriminant support plus the profiles gives the complete total census.
ramified_support = {
    5: set(factor_integer(discriminants[5])),
    8: set(factor_integer(discriminants[8])),
    12: set(factor_integer(discriminants[12])),
}
profile_by_field_prime = {
    (5, 5): factor_profile(factorizations[(5, 5)]),
    (8, 2): factor_profile(factorizations[(8, 2)]),
    (12, 2): factor_profile(factorizations[(12, 2)]),
    (12, 3): factor_profile(factorizations[(12, 3)]),
}
total_pairs = {
    (n, prime)
    for n, support in ramified_support.items()
    for prime in support
    if profile_by_field_prime[(n, prime)] == ((4, 1),)
}
census_ok = ramified_support == {5: {5}, 8: {2}, 12: {2, 3}}
census_ok &= total_pairs == {(5, 5), (8, 2)}
check(
    "06 CENSUS       exactly K5 at 5 and K8 at 2 are totally ramified; K12 at 2 and 3 is not",
    census_ok,
)


# 07: norms identify the two unique total primes with the claimed generators.
norms_ok = poly_eval(cyclotomic(5), 1) == 5
norms_ok &= poly_eval(cyclotomic(8), 1) == 2
norms_ok &= factorizations[(5, 5)] == (((4, 1), 4),)
norms_ok &= factorizations[(8, 2)] == (((1, 1), 4),)
check(
    "07 NORMS        N(1-zeta_5)=5 and N(1-zeta_8)=2 with unique linear total factors",
    norms_ok,
)


# 08: enumerate every nonzero element of the four residue fields.
residue_factors = {
    (5, 5): factorizations[(5, 5)][0][0],
    (8, 2): factorizations[(8, 2)][0][0],
    (12, 2): factorizations[(12, 2)][0][0],
    (12, 3): factorizations[(12, 3)][0][0],
}
residue_summaries = {
    key: field_summary(key[1], modulus)
    for key, modulus in residue_factors.items()
}
residues_ok = residue_summaries == {
    (5, 5): (5, 4, 4, True),
    (8, 2): (2, 1, 1, True),
    (12, 2): (4, 3, 3, True),
    (12, 3): (9, 8, 8, True),
}
residues_ok &= field_order((1,), 2, residue_factors[(8, 2)]) == 1
residues_ok &= field_order((0, 1), 2, residue_factors[(12, 2)]) == 3
residues_ok &= field_order((1, 1), 3, residue_factors[(12, 3)]) == 8
check(
    "08 RESIDUES     unit groups are C4,C1 at the total primes and C3,C8 at the two K12 controls",
    residues_ok,
)


# 09: inherited J reduction, audited directly in the K5 residue quotient.
k5_factor = residue_factors[(5, 5)]
_, j_remainder = poly_divmod_mod((1, 0, 1), k5_factor, 5)
k5_nonzero = set(product(range(5), repeat=1)) - {(0,)}
j_generates = field_order(j_remainder, 5, k5_factor) == 4
j_generates &= {
    field_pow(j_remainder, exponent, 5, k5_factor)
    for exponent in range(4)
} == k5_nonzero
check(
    "09 INHERITED-J  J mod (1-zeta_5)=2 has order 4 and generates F5*; mismatch is STOP",
    j_remainder == (2,) and j_generates,
)


passed = sum(result for _, result in CHECKS)
lines = [
    ("PASS " if result else "FAIL ") + label
    for label, result in CHECKS
]
lines.append(
    "SCOPE L1 TOTAL RAMIFICATION IN FULL QUARTIC CYCLOTOMIC FIELDS ONLY; "
    "K12 RESIDUES ARE NON-TOTAL CONTROLS; NO TWO-PLACE-PHYSICS OR L2-L6 CLAIM"
)
if passed == len(CHECKS):
    lines.append(f"RESULT {passed}/{len(CHECKS)} ALL PASS")
else:
    lines.append(f"RESULT {passed}/{len(CHECKS)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(CHECKS) else 1)
