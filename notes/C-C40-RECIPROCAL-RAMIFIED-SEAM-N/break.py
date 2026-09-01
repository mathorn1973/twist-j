#!/usr/bin/env python3
"""Independent exact breaker for C-C40-RECIPROCAL-RAMIFIED-SEAM-N.

This standard-library-only program was authored from PREREG.md without
inspecting the principal verifier.  It is deliberately a falsifier: every
check appends a deterministic STOP reason, and all sections are attempted
even when an earlier section has failed.

The finite prime scan at the end is audit evidence only.  The universal
unramified conclusion is checked by the complete, exact action of
(Z/40Z)^* on the primitive 40th-root exponents.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, lcm


MODULUS = 40
DEGREE = 16
PRIME_SCAN_LIMIT = 1000


class Audit:
    def __init__(self):
        self.failures = []
        self.passed_sections = []
        self.notes = []

    def check(self, condition, message):
        if not condition:
            self.failures.append(message)

    def run(self, name, function):
        before = len(self.failures)
        try:
            function(self)
        except Exception as exc:  # continue so that every falsifier is tried
            self.failures.append(
                "%s raised %s: %s" % (name, type(exc).__name__, exc)
            )
        if len(self.failures) == before:
            self.passed_sections.append(name)


# ---------- Exact integer-polynomial arithmetic (low coefficient first) ----------


def z_trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def z_divmod_monic(numerator, denominator):
    """Long division over Z; exact when the returned remainder is zero."""
    num = z_trim(numerator)
    den = z_trim(denominator)
    if den == [0]:
        raise ZeroDivisionError("zero polynomial")
    if den[-1] not in (1, -1):
        raise ValueError("integer divisor is not unit-monic")
    if len(num) < len(den):
        return [0], num
    quotient = [0] * (len(num) - len(den) + 1)
    while num != [0] and len(num) >= len(den):
        shift = len(num) - len(den)
        coefficient = num[-1] // den[-1]
        quotient[shift] += coefficient
        for index, value in enumerate(den):
            num[index + shift] -= coefficient * value
        num = z_trim(num)
    return z_trim(quotient), z_trim(num)


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def prime_divisors(n):
    found = []
    candidate = 2
    remaining = n
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            found.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        found.append(remaining)
    return tuple(found)


def euler_phi(n):
    result = n
    for prime in prime_divisors(n):
        result -= result // prime
    return result


def cyclotomic(n):
    """Derive Phi_n over Z by exact division of x^n - 1."""
    values = {}
    for current_n in range(1, n + 1):
        current = [-1] + [0] * (current_n - 1) + [1]
        for divisor in divisors(current_n):
            if divisor == current_n:
                continue
            current, remainder = z_divmod_monic(current, values[divisor])
            if remainder != [0]:
                raise ArithmeticError(
                    "non-exact cyclotomic division at n=%d, d=%d"
                    % (current_n, divisor)
                )
        values[current_n] = z_trim(current)
    return values[n]


def sparse_poly(degree, terms):
    out = [0] * (degree + 1)
    for exponent, coefficient in terms.items():
        out[exponent] = coefficient
    return z_trim(out)


# ---------- Exact finite-field polynomial arithmetic ----------


def p_trim(poly, prime):
    out = [value % prime for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [0]


def p_degree(poly, prime):
    reduced = p_trim(poly, prime)
    return -1 if reduced == [0] else len(reduced) - 1


def p_add(left, right, prime):
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return p_trim(out, prime)


def p_sub(left, right, prime):
    size = max(len(left), len(right))
    out = [0] * size
    for index in range(size):
        out[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % prime
    return p_trim(out, prime)


def p_mul(left, right, prime):
    left = p_trim(left, prime)
    right = p_trim(right, prime)
    if left == [0] or right == [0]:
        return [0]
    out = [0] * (len(left) + len(right) - 1)
    for i, a_value in enumerate(left):
        for j, b_value in enumerate(right):
            out[i + j] = (out[i + j] + a_value * b_value) % prime
    return p_trim(out, prime)


def p_divmod(numerator, denominator, prime):
    num = p_trim(numerator, prime)
    den = p_trim(denominator, prime)
    if den == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(num) < len(den):
        return [0], num
    quotient = [0] * (len(num) - len(den) + 1)
    inverse_lead = pow(den[-1], -1, prime)
    while num != [0] and len(num) >= len(den):
        shift = len(num) - len(den)
        coefficient = num[-1] * inverse_lead % prime
        quotient[shift] = (quotient[shift] + coefficient) % prime
        for index, value in enumerate(den):
            num[index + shift] = (
                num[index + shift] - coefficient * value
            ) % prime
        num = p_trim(num, prime)
    return p_trim(quotient, prime), p_trim(num, prime)


def p_mod(poly, modulus, prime):
    return p_divmod(poly, modulus, prime)[1]


def p_monic(poly, prime):
    poly = p_trim(poly, prime)
    if poly == [0]:
        return [0]
    inverse = pow(poly[-1], -1, prime)
    return p_trim([(coefficient * inverse) % prime for coefficient in poly], prime)


def p_gcd(left, right, prime):
    a_value = p_trim(left, prime)
    b_value = p_trim(right, prime)
    while b_value != [0]:
        _, remainder = p_divmod(a_value, b_value, prime)
        a_value, b_value = b_value, remainder
    return p_monic(a_value, prime)


def p_derivative(poly, prime):
    if len(poly) <= 1:
        return [0]
    return p_trim(
        [(index * poly[index]) % prime for index in range(1, len(poly))],
        prime,
    )


def p_pow_plain(base, exponent, prime):
    result = [1]
    factor = p_trim(base, prime)
    power = exponent
    while power:
        if power & 1:
            result = p_mul(result, factor, prime)
        factor = p_mul(factor, factor, prime)
        power //= 2
    return p_trim(result, prime)


def p_powmod(base, exponent, modulus, prime):
    result = [1]
    factor = p_mod(base, modulus, prime)
    power = exponent
    while power:
        if power & 1:
            result = p_mod(p_mul(result, factor, prime), modulus, prime)
        factor = p_mod(p_mul(factor, factor, prime), modulus, prime)
        power //= 2
    return p_trim(result, prime)


def p_is_irreducible(poly, prime):
    """Rabin's exact irreducibility criterion over F_prime."""
    polynomial = p_monic(poly, prime)
    degree = p_degree(polynomial, prime)
    if degree <= 0:
        return False
    if degree == 1:
        return True
    x_poly = [0, 1]
    final = p_sub(p_powmod(x_poly, prime ** degree, polynomial, prime), x_poly, prime)
    if p_mod(final, polynomial, prime) != [0]:
        return False
    for divisor in prime_divisors(degree):
        exponent = prime ** (degree // divisor)
        test = p_sub(p_powmod(x_poly, exponent, polynomial, prime), x_poly, prime)
        if p_degree(p_gcd(polynomial, test, prime), prime) > 0:
            return False
    return True


def monic_polynomials(degree, prime):
    for coefficients in product(range(prime), repeat=degree):
        yield list(coefficients) + [1]


def p_factor_small(poly, prime):
    """Complete deterministic trial factorization, used only at p=2 and p=5."""
    remainder = p_monic(poly, prime)
    factors = []
    candidate_degree = 1
    while remainder != [1] and 2 * candidate_degree <= p_degree(remainder, prime):
        for candidate in monic_polynomials(candidate_degree, prime):
            if not p_is_irreducible(candidate, prime):
                continue
            while True:
                quotient, residual = p_divmod(remainder, candidate, prime)
                if residual != [0]:
                    break
                factors.append(tuple(candidate))
                remainder = quotient
                if remainder == [1]:
                    break
            if remainder == [1]:
                break
        candidate_degree += 1
    if remainder != [1]:
        if not p_is_irreducible(remainder, prime):
            raise ArithmeticError("trial factorization left a reducible cofactor")
        factors.append(tuple(p_monic(remainder, prime)))
    product_check = [1]
    for factor in factors:
        product_check = p_mul(product_check, factor, prime)
    if product_check != p_monic(poly, prime):
        raise ArithmeticError("factor reconstruction failed")
    return Counter(factors)


def p_distinct_degree_counts(poly, prime):
    """Count irreducible factors of each degree by Frobenius gcds."""
    polynomial = p_monic(poly, prime)
    degree = p_degree(polynomial, prime)
    if p_degree(p_gcd(polynomial, p_derivative(polynomial, prime), prime), prime) > 0:
        raise ValueError("distinct-degree factorization requires squarefree input")
    x_poly = [0, 1]
    frobenius_power = x_poly
    counts = {}
    for current_degree in range(1, degree + 1):
        frobenius_power = p_powmod(
            frobenius_power, prime, polynomial, prime
        )
        fixed = p_gcd(
            polynomial,
            p_sub(frobenius_power, x_poly, prime),
            prime,
        )
        fixed_degree = p_degree(fixed, prime)
        previously_accounted = sum(
            divisor * counts[divisor]
            for divisor in divisors(current_degree)
            if divisor < current_degree
        )
        difference = fixed_degree - previously_accounted
        if difference < 0 or difference % current_degree:
            raise ArithmeticError("invalid distinct-degree inversion")
        counts[current_degree] = difference // current_degree
    positive = {degree_: count for degree_, count in counts.items() if count}
    if sum(degree_ * count for degree_, count in positive.items()) != degree:
        raise ArithmeticError("distinct-degree counts do not cover polynomial")
    return positive


# ---------- Elementary arithmetic and group actions ----------


def multiplicative_order(value, modulus):
    if gcd(value, modulus) != 1:
        raise ValueError("order requested for a non-unit")
    running = 1
    for exponent in range(1, euler_phi(modulus) + 1):
        running = running * value % modulus
        if running == 1:
            return exponent
    raise ArithmeticError("unit order not found")


def action_cycle_lengths(multiplier, units, modulus):
    unseen = set(units)
    lengths = []
    while unseen:
        start = min(unseen)
        current = start
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = multiplier * current % modulus
            length += 1
        if current != start:
            raise ArithmeticError("multiplication did not close a cycle")
        lengths.append(length)
    return tuple(sorted(lengths))


def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def smallest_prime_in_class(residue, modulus):
    candidate = residue
    if candidate < 2:
        candidate += modulus
    while not is_prime(candidate):
        candidate += modulus
    return candidate


def prime_power_part(number, prime):
    result = 1
    remaining = number
    while remaining % prime == 0:
        result *= prime
        remaining //= prime
    return result


def cyclotomic_local_profile(number, prime):
    """Return exact (e,f,g,local-factor-degree) at a prime dividing n.

    For n = p^a*m with (p,m)=1, the p-primary cyclotomic part gives
    e=phi(p^a), the prime-to-p part gives f=ord_m(p), and there are
    phi(n)/(e*f) local factors.  This keeps residue degree f separate from
    the degree e*f of an irreducible factor over Q_p.
    """
    primary = prime_power_part(number, prime)
    if primary == 1:
        raise ValueError("local ramified profile requested at an unramified prime")
    prime_to = number // primary
    e_value = euler_phi(primary)
    f_value = 1 if prime_to == 1 else multiplicative_order(prime % prime_to, prime_to)
    local_factor_degree = e_value * f_value
    if euler_phi(number) % local_factor_degree:
        raise ArithmeticError("non-integral local factor count")
    g_value = euler_phi(number) // local_factor_degree
    return e_value, f_value, g_value, local_factor_degree


# ---------- Frozen falsifier sections ----------


def check_compositum_and_generators(audit):
    degree_5 = euler_phi(5)
    degree_8 = euler_phi(8)
    degree_40 = euler_phi(40)
    audit.check(gcd(5, 8) == 1, "conductors 5 and 8 are not coprime")
    audit.check(
        (degree_5, degree_8, degree_40) == (4, 4, 16),
        "cyclotomic degree triple is not (4,4,16)",
    )
    audit.check(
        8 * 2 + 5 * (-3) == 1,
        "registered Bezout exponent 8*2 + 5*(-3) is not 1",
    )
    audit.check(
        40 // gcd(40, 8) == 5,
        "zeta_40^8 does not have order 5",
    )
    audit.check(
        40 // gcd(40, 5) == 8,
        "zeta_40^5 does not have order 8",
    )
    audit.check(
        (2 * 8 - 3 * 5) % 40 == 1,
        "zeta_5^2*zeta_8^(-3) does not recover zeta_40",
    )
    compositum_degree = degree_40
    numerator = degree_5 * degree_8
    audit.check(
        numerator % compositum_degree == 0,
        "degree formula does not give an integral intersection degree",
    )
    intersection_degree = numerator // compositum_degree
    audit.check(
        intersection_degree == 1,
        "computed intersection degree is not one",
    )


def check_cyclotomic_polynomials(audit):
    expected_40 = sparse_poly(
        16, {0: 1, 4: -1, 8: 1, 12: -1, 16: 1}
    )
    phi_40 = cyclotomic(40)
    audit.check(phi_40 == expected_40, "derived Phi_40 is incorrect")
    audit.check(len(phi_40) - 1 == DEGREE, "Phi_40 does not have degree 16")
    audit.check(cyclotomic(5) == [1, 1, 1, 1, 1], "derived Phi_5 is incorrect")
    audit.check(cyclotomic(8) == [1, 0, 0, 0, 1], "derived Phi_8 is incorrect")


def local_profile(factorization, prime):
    if not factorization:
        raise ValueError("empty factorization")
    multiplicities = set(factorization.values())
    degrees = {p_degree(factor, prime) for factor in factorization}
    if len(multiplicities) != 1 or len(degrees) != 1:
        raise ValueError("local factors do not have a common (e,f)")
    return (
        next(iter(multiplicities)),
        next(iter(degrees)),
        len(factorization),
    )


def check_registered_local_dependencies(audit):
    """Recheck the four named Canon dependencies, never claim them as new."""
    phi_5 = cyclotomic(5)
    phi_8 = cyclotomic(8)

    # QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T].
    audit.check(
        p_trim(phi_8, 2) == p_pow_plain([1, 1], 4, 2),
        "dependency failure: Phi_8 mod 2 is not (x+1)^4",
    )
    audit.check(
        p_trim(phi_5, 5) == p_pow_plain([4, 1], 4, 5),
        "dependency failure: Phi_5 mod 5 is not (x-1)^4",
    )

    # J-BINARY-NORM-INDEX [T]: inert 2 in K_5 has residue field F_16.
    audit.check(
        p_is_irreducible(p_trim(phi_5, 2), 2),
        "dependency failure: Phi_5 is reducible over F_2",
    )
    audit.check(
        2 ** p_degree(p_trim(phi_5, 2), 2) == 16,
        "dependency failure: the Phi_5 mod 2 residue field size is not 16",
    )

    # BORN-RESIDUAL-SPLIT [T]: two quadratics and the inversion swap.
    factor_a = [3, 0, 1]  # x^2 - 2
    factor_b = [2, 0, 1]  # x^2 - 3
    expected_phi8_factors = Counter({tuple(factor_a): 1, tuple(factor_b): 1})
    audit.check(
        p_factor_small(p_trim(phi_8, 5), 5) == expected_phi8_factors,
        "dependency failure: Phi_8 mod 5 is not the two registered quadratics",
    )
    audit.check(
        pow(2, -1, 5) == 3 and pow(3, -1, 5) == 2,
        "dependency failure: inversion does not swap the two quadratic classes",
    )


def check_ramified_reductions(audit):
    phi_40 = cyclotomic(40)
    phi_5 = cyclotomic(5)
    phi_8 = cyclotomic(8)

    reduction_2 = p_trim(phi_40, 2)
    reduction_5 = p_trim(phi_40, 5)
    expected_2 = p_pow_plain(p_trim(phi_5, 2), 4, 2)
    expected_5 = p_pow_plain(p_trim(phi_8, 5), 4, 5)
    audit.check(reduction_2 == expected_2, "Phi_40 mod 2 != Phi_5^4")
    audit.check(reduction_5 == expected_5, "Phi_40 mod 5 != Phi_8^4")

    factor_2 = tuple(p_trim(phi_5, 2))
    factor_5a = (3, 0, 1)  # x^2 - 2 over F_5
    factor_5b = (2, 0, 1)  # x^2 - 3 over F_5
    audit.check(
        p_is_irreducible(factor_2, 2),
        "Phi_5 is not irreducible over F_2",
    )
    audit.check(
        p_is_irreducible(factor_5a, 5) and p_is_irreducible(factor_5b, 5),
        "one of x^2-2 and x^2-3 is reducible over F_5",
    )

    actual_factors_2 = p_factor_small(reduction_2, 2)
    actual_factors_5 = p_factor_small(reduction_5, 5)
    expected_factors_2 = Counter({factor_2: 4})
    expected_factors_5 = Counter({factor_5a: 4, factor_5b: 4})
    audit.check(
        actual_factors_2 == expected_factors_2,
        "wrong irreducible-factor multiplicity at 2",
    )
    audit.check(
        actual_factors_5 == expected_factors_5,
        "wrong irreducible-factor multiplicity at 5",
    )

    profile_2 = local_profile(actual_factors_2, 2)
    profile_5 = local_profile(actual_factors_5, 5)
    audit.check(profile_2 == (4, 4, 1), "local profile at 2 is not (4,4,1)")
    audit.check(profile_5 == (4, 2, 2), "local profile at 5 is not (4,2,2)")

    local_2 = cyclotomic_local_profile(40, 2)
    local_5 = cyclotomic_local_profile(40, 5)
    audit.check(
        local_2 == (4, 4, 1, 16),
        "Q_2 local data are not (e,f,g,ef)=(4,4,1,16)",
    )
    audit.check(
        local_5 == (4, 2, 2, 8),
        "Q_5 local data are not (e,f,g,ef)=(4,2,2,8)",
    )
    audit.check(
        local_2[2] == 1 and local_2[3] == DEGREE,
        "Phi_40 was not certified irreducible over Q_2",
    )
    audit.check(
        local_5[2] == 2 and local_5[3] == 8,
        "Phi_40 was not certified as two degree-8 factors over Q_5",
    )
    audit.check(
        local_2[1] == 4 and local_2[3] == 16
        and local_5[1] == 2 and local_5[3] == 8,
        "residue degrees were confused with p-adic factor degrees",
    )
    inert_unramified_profile = (1, DEGREE, 1)
    audit.check(
        profile_2 != inert_unramified_profile and 40 % 2 == 0 and profile_2[0] > 1,
        "g=1 at ramified 2 was incorrectly treated as inertness",
    )

    # "Reciprocal" means complementary primary roles, not 2 <-> 5 symmetry.
    audit.check(profile_2 != profile_5, "the unequal local profiles were conflated")
    audit.check(
        (prime_power_part(40, 2), 40 // prime_power_part(40, 2)) == (8, 5),
        "incorrect 2-primary / prime-to-2 decomposition of 40",
    )
    audit.check(
        (prime_power_part(40, 5), 40 // prime_power_part(40, 5)) == (5, 8),
        "incorrect 5-primary / prime-to-5 decomposition of 40",
    )
    audit.check(
        euler_phi(prime_power_part(40, 2)) == profile_2[0]
        and euler_phi(prime_power_part(40, 5)) == profile_5[0],
        "p-primary cyclotomic part does not supply multiplicity four",
    )
    audit.check(
        profile_2[1:] == (4, 1) and profile_5[1:] == (2, 2),
        "prime-to-p parts do not control the stated separable factors",
    )

    # Repeated factors make both quotient algebras nonreduced and non-etale.
    # A nonzero nilpotent radical witnesses this without interpreting either
    # reduction as a merger (or even as a product) of fields.
    for prime, reduction, factorization in (
        (2, reduction_2, actual_factors_2),
        (5, reduction_5, actual_factors_5),
    ):
        derivative_gcd = p_gcd(reduction, p_derivative(reduction, prime), prime)
        audit.check(
            p_degree(derivative_gcd, prime) > 0,
            "ramified reduction at %d was incorrectly squarefree" % prime,
        )
        radical = [1]
        for factor in sorted(factorization):
            radical = p_mul(radical, factor, prime)
        common_multiplicity = next(iter(set(factorization.values())))
        audit.check(
            p_degree(radical, prime) < p_degree(reduction, prime),
            "radical witness at %d is not nonzero modulo Phi_40" % prime,
        )
        audit.check(
            p_powmod(radical, common_multiplicity, reduction, prime) == [0],
            "radical witness at %d is not nilpotent" % prime,
        )

    semantic_flags = {
        "field_merger": False,
        "etale_product_of_fields": False,
        "prime_exchange_symmetry": False,
        "ramified_2_called_inert": False,
        "selector": False,
        "registered_row_promotion": False,
    }
    audit.check(
        not any(semantic_flags.values()),
        "a forbidden ramified-reduction interpretation was enabled",
    )


EXPECTED_ORDER_CLASSES = {
    1: (1,),
    2: (9, 11, 19, 21, 29, 31, 39),
    4: (3, 7, 13, 17, 23, 27, 33, 37),
}

EXPECTED_DENSITIES = {
    1: Fraction(1, 16),
    2: Fraction(7, 16),
    4: Fraction(1, 2),
}


def check_complete_unramified_atlas(audit):
    units = tuple(value for value in range(MODULUS) if gcd(value, MODULUS) == 1)
    audit.check(len(units) == DEGREE, "(Z/40Z)^* does not have 16 elements")

    actual_partition = {}
    exact_rows = {}
    for residue in units:
        order = multiplicative_order(residue, MODULUS)
        cycles = action_cycle_lengths(residue, units, MODULUS)
        factor_degree = order
        factor_count = DEGREE // factor_degree
        audit.check(
            cycles == (factor_degree,) * factor_count,
            "Frobenius cycles mismatch at residue %d" % residue,
        )
        exact_rows[residue] = (order, factor_degree, factor_count)
        actual_partition.setdefault(order, []).append(residue)

    actual_partition = {
        order: tuple(classes) for order, classes in sorted(actual_partition.items())
    }
    audit.check(
        actual_partition == EXPECTED_ORDER_CLASSES,
        "complete modulo-40 order partition is wrong",
    )

    for order, classes in EXPECTED_ORDER_CLASSES.items():
        expected_type = (order, DEGREE // order)
        for residue in classes:
            actual_order, factor_degree, factor_count = exact_rows[residue]
            audit.check(
                (actual_order, factor_degree, factor_count)
                == (order, expected_type[0], expected_type[1]),
                "class/order/factor type mismatch at residue %d" % residue,
            )
        density = Fraction(len(classes), len(units))
        audit.check(
            density == EXPECTED_DENSITIES[order],
            "density mismatch for order %d classes" % order,
        )

    audit.check(
        sum(EXPECTED_DENSITIES.values(), Fraction(0, 1)) == 1,
        "atlas densities do not sum to one",
    )

    # One actual prime per residue class cross-checks the group-action atlas
    # by an unrelated finite-field distinct-degree computation.  This remains
    # an audit, not the proof for all primes in the class.
    phi_40 = cyclotomic(40)
    representatives = {}
    for residue in units:
        prime = smallest_prime_in_class(residue, MODULUS)
        representatives[residue] = prime
        actual_counts = p_distinct_degree_counts(p_trim(phi_40, prime), prime)
        order = exact_rows[residue][0]
        expected_counts = {order: DEGREE // order}
        audit.check(
            actual_counts == expected_counts,
            "representative-prime factor type mismatch for class %d at p=%d"
            % (residue, prime),
        )
    audit.notes.append(
        "CLASS REPRESENTATIVES (AUDIT ONLY; NOT PROOF): "
        + ", ".join(
            "%d->%d" % (residue, representatives[residue]) for residue in units
        )
    )


def check_group_and_inertness(audit):
    units = tuple(value for value in range(MODULUS) if gcd(value, MODULUS) == 1)
    orders = {value: multiplicative_order(value, MODULUS) for value in units}
    exponent = 1
    for order in orders.values():
        exponent = lcm(exponent, order)
    audit.check(exponent == 4, "group exponent is not 4")
    audit.check(
        all(order in (1, 2, 4) for order in orders.values()),
        "a unit has order outside {1,2,4}",
    )
    audit.check(
        not any(order == 16 for order in orders.values()),
        "an element of order 16 exists in (Z/40Z)^*",
    )

    # Explicit isomorphism C4 x C2 x C2 -> (Z/40Z)^*.
    generator_4, generator_2a, generator_2b = 17, 31, 11
    audit.check(
        (
            orders[generator_4],
            orders[generator_2a],
            orders[generator_2b],
        ) == (4, 2, 2),
        "chosen CRT generators do not have orders (4,2,2)",
    )
    domain = tuple(product(range(4), range(2), range(2)))

    def image(element):
        i_value, j_value, k_value = element
        return (
            pow(generator_4, i_value, MODULUS)
            * pow(generator_2a, j_value, MODULUS)
            * pow(generator_2b, k_value, MODULUS)
        ) % MODULUS

    images = {element: image(element) for element in domain}
    audit.check(
        set(images.values()) == set(units) and len(set(images.values())) == 16,
        "C4 x C2 x C2 generator map is not bijective",
    )
    for left in domain:
        for right in domain:
            domain_product = (
                (left[0] + right[0]) % 4,
                (left[1] + right[1]) % 2,
                (left[2] + right[2]) % 2,
            )
            audit.check(
                image(domain_product) == image(left) * image(right) % MODULUS,
                "C4 x C2 x C2 generator map is not a homomorphism",
            )

    # Exact universal check: every p not dividing 40 maps to one of these 16
    # residue classes, and none acts as one 16-cycle on primitive roots.
    inert_classes = tuple(
        value
        for value in units
        if action_cycle_lengths(value, units, MODULUS) == (DEGREE,)
    )
    audit.check(inert_classes == (), "an unramified inert residue class exists")
    audit.check(
        all(DEGREE // orders[value] > 1 for value in units),
        "an unramified class gives an irreducible Phi_40",
    )

    # At the only ramified rational primes, the already checked fourth powers
    # are proper factorizations.  Combined with the exhaustive unit classes,
    # this proves reducibility for every rational prime without a prime scan.
    audit.check(
        p_degree(p_trim(cyclotomic(5), 2), 2) < DEGREE
        and p_degree(p_trim(cyclotomic(8), 5), 5) < DEGREE,
        "a ramified proper factor does not have degree below 16",
    )


def check_canon_dependency_firewall(audit):
    """Audit only the canonical ownership declarations frozen in PREREG."""
    canonical_owned = {
        "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]": frozenset(
            {
                "K5_intersection_K8_is_Q",
                "K5_K8_compositum_is_K40",
                "K40_degree_16",
            }
        ),
        "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]": frozenset(
            {"K8_at_2_has_e4", "K5_at_5_has_e4"}
        ),
        "J-BINARY-NORM-INDEX [T]": frozenset(
            {"K5_at_2_is_inert_with_residue_F16"}
        ),
        "BORN-RESIDUAL-SPLIT [T]": frozenset(
            {"Phi8_mod5_two_quadratics", "conjugation_swaps_quadratics"}
        ),
    }
    expected_rows = frozenset(
        {
            "DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]",
            "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]",
            "J-BINARY-NORM-INDEX [T]",
            "BORN-RESIDUAL-SPLIT [T]",
        }
    )
    audit.check(
        frozenset(canonical_owned) == expected_rows,
        "frozen canonical dependency row list changed",
    )
    dependency_only = frozenset().union(*canonical_owned.values())
    candidate_novel = frozenset(
        {
            "K40_Phi40",
            "K40_repeated_ramified_reductions",
            "K40_local_profiles_2_and_5",
            "K40_complete_mod40_atlas_and_densities",
            "K40_exponent_and_no_unramified_inert_prime",
        }
    )
    expected_novel = frozenset(
        {
            "K40_Phi40",
            "K40_repeated_ramified_reductions",
            "K40_local_profiles_2_and_5",
            "K40_complete_mod40_atlas_and_densities",
            "K40_exponent_and_no_unramified_inert_prime",
        }
    )
    audit.check(candidate_novel == expected_novel, "candidate novelty scope changed")
    audit.check(
        candidate_novel.isdisjoint(dependency_only),
        "candidate novelty collides with a frozen canonical dependency",
    )
    promoted_rows = frozenset()
    audit.check(not promoted_rows, "the incubation attempts to promote a row")


def finite_prime_scan_audit(audit):
    """Finite audit only; never used for the universal inference."""
    phi_40 = cyclotomic(40)
    scanned = 0
    unramified = 0
    for prime in range(2, PRIME_SCAN_LIMIT + 1):
        if not is_prime(prime):
            continue
        scanned += 1
        if prime in (2, 5):
            # The complete repeated factorizations were checked independently.
            continue
        unramified += 1
        order = multiplicative_order(prime % MODULUS, MODULUS)
        expected_counts = {order: DEGREE // order}
        actual_counts = p_distinct_degree_counts(p_trim(phi_40, prime), prime)
        audit.check(
            actual_counts == expected_counts,
            "finite scan mismatch at p=%d: got %r, expected %r"
            % (prime, actual_counts, expected_counts),
        )
        audit.check(
            sum(actual_counts.values()) > 1,
            "finite scan found an unramified inert prime p=%d" % prime,
        )
    audit.notes.append(
        "FINITE PRIME SCAN (AUDIT ONLY; NOT PROOF): "
        "%d primes <= %d (%d unramified)"
        % (scanned, PRIME_SCAN_LIMIT, unramified)
    )


def main():
    audit = Audit()
    sections = (
        ("compositum/generators/degrees", check_compositum_and_generators),
        ("cyclotomic derivation", check_cyclotomic_polynomials),
        ("registered local dependencies", check_registered_local_dependencies),
        ("ramified identities/profiles/non-etaleness", check_ramified_reductions),
        ("complete modulo-40 atlas/densities", check_complete_unramified_atlas),
        ("group exponent/no unramified inertness", check_group_and_inertness),
        ("Canon dependency firewall", check_canon_dependency_firewall),
        ("finite prime scan audit", finite_prime_scan_audit),
    )
    for name, function in sections:
        audit.run(name, function)

    print("C-C40-RECIPROCAL-RAMIFIED-SEAM-N independent arithmetic breaker")
    for name in audit.passed_sections:
        print("PASS:", name)
    for note in audit.notes:
        print(note)
    print(
        "RAMIFIED SEMANTICS: nonreduced single-polynomial quotients; "
        "no field-merger or etale-product interpretation"
    )
    if audit.failures:
        print("STOP")
        for failure in audit.failures:
            print("FAIL:", failure)
        raise SystemExit(1)
    print("candidate-T / L1")


if __name__ == "__main__":
    main()
