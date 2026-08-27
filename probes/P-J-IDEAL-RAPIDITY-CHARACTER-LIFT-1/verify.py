#!/usr/bin/env python3
"""Exact verifier draft for P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1.

This file is intentionally standard-library only and uses integer arithmetic
throughout.  It is a pre-pin draft: importing it is inert, and the public
formal run is performed only after PREREG and verifier acceptance.
"""

import ast
import itertools
import math
import pathlib
import sys


P_MAX = 997
E_MAX = 8
N_GLOBAL = 20_000
N_C0 = 10_000
N_O5 = 5_000

SPLIT6 = (11, 19, 29, 31, 41, 59)
MULTIPLIERS = (1, 2, 5, 10)

_ROOT_CACHE = {}


def require(condition, label):
    if not condition:
        raise RuntimeError("FAIL " + label)


# ---------------------------------------------------------------------------
# Exact scalar arithmetic


def chi5(n):
    residue = n % 5
    if residue == 0:
        return 0
    if residue in (1, 4):
        return 1
    return -1


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    bound = math.isqrt(n)
    for divisor in range(3, bound + 1, 2):
        if n % divisor == 0:
            return False
    return True


def primes_upto(limit):
    return tuple(n for n in range(2, limit + 1) if is_prime(n))


def spf_sieve(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if spf[multiple] == multiple:
                spf[multiple] = prime
    return spf


def factor_with_spf(n, spf):
    require(n >= 1, "factor-positive")
    factors = []
    while n > 1:
        prime = spf[n]
        exponent = 0
        while n % prime == 0:
            n //= prime
            exponent += 1
        factors.append((prime, exponent))
    return tuple(factors)


def divisors_from_factors(factors):
    divisors = [1]
    for prime, exponent in factors:
        old = tuple(divisors)
        power = 1
        enlarged = []
        for current_exponent in range(exponent + 1):
            for divisor in old:
                enlarged.append(divisor * power)
            power *= prime
        divisors = enlarged
    return tuple(sorted(divisors))


def mu_rota_table(limit):
    """Rota inversion on the divisibility poset, without factorization."""
    mu = [0] * (limit + 1)
    proper_sum = [0] * (limit + 1)
    mu[1] = 1
    for n in range(1, limit + 1):
        if n > 1:
            mu[n] = -proper_sum[n]
        for multiple in range(2 * n, limit + 1, n):
            proper_sum[multiple] += mu[n]
    return mu


def mu_trial(n):
    """Independent squarefree trial-division reference."""
    require(n >= 1, "mu-trial-positive")
    remaining = n
    sign = 1
    prime = 2
    while prime <= math.isqrt(remaining):
        if remaining % prime == 0:
            remaining //= prime
            if remaining % prime == 0:
                return 0
            sign = -sign
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        sign = -sign
    return sign


def prime_type(prime):
    value = chi5(prime)
    if value == 1:
        return "split"
    if value == -1:
        return "inert"
    require(prime == 5, "only-five-ramifies")
    return "ramified"


def roots_phi(prime):
    if prime not in _ROOT_CACHE:
        roots = tuple(
            residue
            for residue in range(prime)
            if (residue * residue - residue - 1) % prime == 0
        )
        _ROOT_CACHE[prime] = roots
    return _ROOT_CACHE[prime]


def prime_type_from_roots(prime):
    """Prime-ideal type derived from the actual quotient-root census."""
    roots = roots_phi(prime)
    if prime == 5:
        require(len(roots) == 1, "ramified-root-census")
        return "ramified"
    if len(roots) == 2:
        return "split"
    require(len(roots) == 0, "inert-root-census")
    return "inert"


# ---------------------------------------------------------------------------
# Projective fixed lines and the corrected root-to-ideal pairing


def normalize_line(u, v, prime):
    u %= prime
    v %= prime
    require((u, v) != (0, 0), "nonzero-projective-vector")
    if u == 0:
        return (0, 1)
    inverse = pow(u, prime - 2, prime)
    return (1, (v * inverse) % prime)


def projective_lines(prime):
    return ((0, 1),) + tuple((1, slope) for slope in range(prime))


def apply_phi_matrix(line, prime):
    u, v = line
    return normalize_line(v, u + v, prime)


def fixed_lines(prime):
    return tuple(
        sorted(
            line
            for line in projective_lines(prime)
            if apply_phi_matrix(line, prime) == line
        )
    )


def prime_ideal_kernel_line(root, prime):
    """The line of P_root=(p,phi-root) modulo p."""
    return normalize_line(-root, 1, prime)


def eigenline(root, prime):
    return normalize_line(1, root, prime)


# ---------------------------------------------------------------------------
# Sparse Laurent polynomials over the free split-prime rapidity lattice


ZERO = {}
ONE = {(): 1}


def normalize_monomial(monomial, key_map=None):
    exponents = {}
    for prime, exponent in monomial:
        key = prime if key_map is None else key_map.get(prime, prime)
        exponents[key] = exponents.get(key, 0) + exponent
    return tuple(
        (key, exponents[key])
        for key in sorted(exponents)
        if exponents[key] != 0
    )


def monomial(prime, exponent):
    if exponent == 0:
        return ()
    return ((prime, exponent),)


def multiply_monomials(left, right, key_map=None):
    return normalize_monomial(left + right, key_map)


def poly_from_terms(terms, key_map=None):
    coefficients = {}
    for raw_monomial, coefficient in terms:
        if coefficient == 0:
            continue
        normalized = normalize_monomial(raw_monomial, key_map)
        coefficients[normalized] = coefficients.get(normalized, 0) + coefficient
    return {
        term: coefficients[term]
        for term in sorted(coefficients)
        if coefficients[term] != 0
    }


def poly_add(left, right):
    return poly_from_terms(tuple(left.items()) + tuple(right.items()))


def poly_scale(coefficient, polynomial):
    if coefficient == 0:
        return {}
    return poly_from_terms(
        (term, coefficient * value)
        for term, value in sorted(polynomial.items())
    )


def poly_mul(left, right, key_map=None):
    if not left or not right:
        return {}
    terms = []
    for left_term, left_value in sorted(left.items()):
        for right_term, right_value in sorted(right.items()):
            product_term = multiply_monomials(left_term, right_term, key_map)
            terms.append((product_term, left_value * right_value))
    return poly_from_terms(terms)


def poly_star(polynomial):
    return poly_from_terms(
        (
            tuple((prime, -exponent) for prime, exponent in term),
            coefficient,
        )
        for term, coefficient in sorted(polynomial.items())
    )


def augmentation(polynomial):
    return sum(polynomial.values())


def constant_term(polynomial):
    return polynomial.get((), 0)


def l1_norm(polynomial):
    return sum(abs(value) for value in polynomial.values())


def l2_squared(polynomial):
    return sum(value * value for value in polynomial.values())


def serialize_poly(polynomial):
    pieces = []
    for term, coefficient in sorted(polynomial.items()):
        word = ",".join(
            str(prime) + "^" + str(exponent) for prime, exponent in term
        )
        pieces.append(str(coefficient) + ":" + word)
    return ";".join(pieces)


# ---------------------------------------------------------------------------
# Prime-ideal valuation choices and the refined ideal pushforward


def mu_f_from_valuations(valuations):
    if any(exponent >= 2 for exponent in valuations):
        return 0
    return -1 if sum(valuations) % 2 else 1


def ideal_choice_terms(
    prime,
    rational_exponent,
    orientation_mode="correct",
    type_override=None,
):
    """Individual prime-ideal choices before Laurent aggregation."""
    kind = (
        prime_type_from_roots(prime)
        if type_override is None
        else type_override
    )

    if kind == "split":
        roots = roots_phi(prime)
        require(len(roots) == 2, "split-has-two-prime-ideal-roots")
        if orientation_mode == "correct":
            orientation_signs = (1, -1)
        elif orientation_mode == "duplicate":
            orientation_signs = (1, 1)
        else:
            raise RuntimeError("FAIL unknown-orientation-mode")

        terms = []
        for first_valuation in range(rational_exponent + 1):
            second_valuation = rational_exponent - first_valuation
            coefficient = mu_f_from_valuations(
                (first_valuation, second_valuation)
            )
            rapidity_exponent = (
                orientation_signs[0] * first_valuation
                + orientation_signs[1] * second_valuation
            )
            terms.append((monomial(prime, rapidity_exponent), coefficient))
        return tuple(terms)

    if kind == "inert":
        if rational_exponent % 2:
            return ()
        valuation = rational_exponent // 2
        return (((), mu_f_from_valuations((valuation,))),)

    require(kind == "ramified", "known-prime-type")
    return (
        (
            (),
            mu_f_from_valuations((rational_exponent,)),
        ),
    )


def local_b_from_choices(
    prime,
    rational_exponent,
    orientation_mode="correct",
    type_override=None,
):
    return poly_from_terms(
        ideal_choice_terms(
            prime,
            rational_exponent,
            orientation_mode,
            type_override,
        )
    )


def local_b_closed(prime, exponent):
    kind = prime_type(prime)
    if kind == "split":
        if exponent == 0:
            return dict(ONE)
        if exponent == 1:
            return poly_from_terms(
                (
                    (monomial(prime, 1), -1),
                    (monomial(prime, -1), -1),
                )
            )
        if exponent == 2:
            return dict(ONE)
        return {}

    if kind == "inert":
        if exponent == 0:
            return dict(ONE)
        if exponent == 2:
            return {(): -1}
        return {}

    if exponent == 0:
        return dict(ONE)
    if exponent == 1:
        return {(): -1}
    return {}


def chi_prime_power(prime, exponent):
    if exponent == 0:
        return 1
    return chi5(prime) ** exponent


def local_u_from_choices(
    prime,
    exponent,
    orientation_mode="correct",
    type_override=None,
    omit_split_character=False,
):
    total = {}
    for b_exponent in range(exponent + 1):
        character_exponent = exponent - b_exponent
        weight = chi_prime_power(prime, character_exponent)
        if (
            omit_split_character
            and prime_type(prime) == "split"
            and character_exponent > 0
        ):
            weight = 0
        contribution = poly_scale(
            weight,
            local_b_from_choices(
                prime,
                b_exponent,
                orientation_mode,
                type_override,
            ),
        )
        total = poly_add(total, contribution)
    return total


def local_u_closed(prime, exponent):
    kind = prime_type(prime)
    if exponent == 0:
        return dict(ONE)
    if kind == "split":
        neutral = 1 if exponent == 1 else 2
        return poly_from_terms(
            (
                ((), neutral),
                (monomial(prime, 1), -1),
                (monomial(prime, -1), -1),
            )
        )
    if exponent == 1:
        return {(): -1}
    return {}


def local_u_recurrence(prime, exponent):
    """Coefficient recurrence from denominator cross-multiplication."""
    kind = prime_type(prime)
    previous = {}
    current = {}
    for degree in range(exponent + 1):
        numerator = local_b_closed(prime, degree)
        if kind == "split":
            current = poly_add(numerator, previous)
        elif kind == "inert":
            current = poly_add(numerator, poly_scale(-1, previous))
        else:
            current = numerator
        previous = current
    return current


def refined_b(n, spf):
    result = dict(ONE)
    for prime, exponent in factor_with_spf(n, spf):
        result = poly_mul(result, local_b_from_choices(prime, exponent))
    return result


def bold_mu_convolution(n, refined_b_table, spf):
    total = {}
    factors = factor_with_spf(n, spf)
    for divisor in divisors_from_factors(factors):
        total = poly_add(
            total,
            poly_scale(chi5(n // divisor), refined_b_table[divisor]),
        )
    return total


def bold_mu_product(n, spf):
    result = dict(ONE)
    for prime, exponent in factor_with_spf(n, spf):
        result = poly_mul(result, local_u_closed(prime, exponent))
    return result


def scalar_b_closed(n, spf):
    result = 1
    for prime, exponent in factor_with_spf(n, spf):
        kind = prime_type(prime)
        if kind == "split":
            local = (1, -2, 1)[exponent] if exponent <= 2 else 0
        elif kind == "inert":
            local = -1 if exponent == 2 else 0
        else:
            local = -1 if exponent == 1 else 0
        result *= local
    return result


# ---------------------------------------------------------------------------
# Scalar coefficient constructions for C0 and O5


def dirichlet_convolution(left, right, limit):
    output = [0] * (limit + 1)
    for first in range(1, limit + 1):
        first_value = left[first]
        if first_value == 0:
            continue
        for second in range(1, limit // first + 1):
            second_value = right[second]
            if second_value != 0:
                output[first * second] += first_value * second_value
    return output


def c0_local_value(n, spf):
    value = 1
    for prime, exponent in factor_with_spf(n, spf):
        if prime_type(prime) == "split":
            local = 1 if exponent == 1 else 2
        else:
            local = -1 if exponent == 1 else 0
        value *= local
    return value


def c0_analytic_arrays(limit, mu):
    character = [0] * (limit + 1)
    square_character = [0] * (limit + 1)
    fourth_mu = [0] * (limit + 1)
    correction_5 = [0] * (limit + 1)

    for n in range(1, limit + 1):
        character[n] = chi5(n)

    root = 1
    while root * root <= limit:
        square_character[root * root] = chi5(root)
        root += 1

    root = 1
    while root * root * root * root <= limit:
        fourth_mu[root * root * root * root] = mu[root]
        root += 1

    power = 1
    exponent = 0
    while power <= limit:
        residue = exponent % 4
        if residue == 0:
            correction_5[power] = 1
        elif residue == 1:
            correction_5[power] = -1
        power *= 5
        exponent += 1

    first = dirichlet_convolution(character, square_character, limit)
    base = dirichlet_convolution(first, fourth_mu, limit)
    full = dirichlet_convolution(base, correction_5, limit)
    return base, full


def orientation_local_coefficient(exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return 0
    half_index = (exponent - 1) // 2
    return -2 if half_index % 2 == 0 else 2


def scalar_series_convolution(left, right, max_exponent):
    output = [0] * (max_exponent + 1)
    for exponent in range(max_exponent + 1):
        output[exponent] = sum(
            left[index] * right[exponent - index]
            for index in range(exponent + 1)
        )
    return output


def orientation_euler_coefficients(limit):
    coefficients = [0] * (limit + 1)
    coefficients[1] = 1
    for prime in primes_upto(limit):
        if prime_type(prime) != "split":
            continue
        local_powers = [(1, 1)]
        power = prime
        exponent = 1
        while power <= limit:
            coefficient = orientation_local_coefficient(exponent)
            if coefficient != 0:
                local_powers.append((power, coefficient))
            power *= prime
            exponent += 1

        updated = [0] * (limit + 1)
        for n in range(1, limit + 1):
            if coefficients[n] == 0:
                continue
            for prime_power, local_value in local_powers:
                product = n * prime_power
                if product <= limit:
                    updated[product] += coefficients[n] * local_value
        coefficients = updated
    return coefficients


def orientation_analytic_coefficients(limit, mu):
    zeta_four = [0] * (limit + 1)
    inverse_zeta = [0] * (limit + 1)
    inverse_l = [0] * (limit + 1)
    inverse_l_two = [0] * (limit + 1)
    correction_5 = [0] * (limit + 1)

    root = 1
    while root * root * root * root <= limit:
        zeta_four[root * root * root * root] = 1
        root += 1

    for n in range(1, limit + 1):
        inverse_zeta[n] = mu[n]
        inverse_l[n] = mu[n] * chi5(n)

    root = 1
    while root * root <= limit:
        inverse_l_two[root * root] = mu[root] * chi5(root)
        root += 1

    power = 1
    for exponent in range(4):
        if power <= limit:
            correction_5[power] = 1
        power *= 5

    first = dirichlet_convolution(zeta_four, inverse_zeta, limit)
    second = dirichlet_convolution(first, inverse_l, limit)
    third = dirichlet_convolution(second, inverse_l_two, limit)
    return dirichlet_convolution(third, correction_5, limit)


# ---------------------------------------------------------------------------
# Gates


def gate_01_projective(primes):
    for prime in primes:
        roots = roots_phi(prime)
        fixed = fixed_lines(prime)
        require(len(fixed) == 1 + chi5(prime), "G01-fixed-count")
        require(
            fixed == tuple(sorted(eigenline(root, prime) for root in roots)),
            "G01-fixed-root-lines",
        )
        for root in roots:
            conjugate_root = (1 - root) % prime
            require(
                conjugate_root in roots,
                "G01-galois-root-pair",
            )
            require(
                prime_ideal_kernel_line(root, prime)
                == eigenline(conjugate_root, prime),
                "G01-corrected-root-ideal-pairing",
            )
    require(roots_phi(5) == (3,), "G01-five-double-root")
    require(
        prime_ideal_kernel_line(4, 11) == eigenline(8, 11),
        "G01-p11-cross-label-positive",
    )
    require(
        prime_ideal_kernel_line(4, 11) != eigenline(4, 11),
        "G01-p11-same-root-fires",
    )


def gate_02_local_ideal_choices(primes):
    for prime in primes:
        for exponent in range(E_MAX + 1):
            from_choices = local_b_from_choices(prime, exponent)
            require(
                from_choices == local_b_closed(prime, exponent),
                "G02-ideal-choice-b",
            )
            lifted = local_u_from_choices(prime, exponent)
            require(
                lifted == local_u_closed(prime, exponent),
                "G02-character-lift-u",
            )
            require(
                lifted == local_u_recurrence(prime, exponent),
                "G02-cross-multiplied-recurrence",
            )
            require(poly_star(lifted) == lifted, "G02-galois-star")
            rational_local = 1 if exponent == 0 else (-1 if exponent == 1 else 0)
            require(
                augmentation(lifted) == rational_local,
                "G02-local-augmentation",
            )


def gate_03_global(spf, mu):
    refined_table = [{} for _ in range(N_GLOBAL + 1)]
    lifted_table = [{} for _ in range(N_GLOBAL + 1)]

    for n in range(1, N_GLOBAL + 1):
        refined_table[n] = refined_b(n, spf)
        require(
            augmentation(refined_table[n]) == scalar_b_closed(n, spf),
            "G03-refined-b-augmentation",
        )

    for n in range(1, N_GLOBAL + 1):
        lifted = bold_mu_convolution(n, refined_table, spf)
        lifted_table[n] = lifted
        require(lifted == bold_mu_product(n, spf), "G03-global-two-routes")
        require(augmentation(lifted) == mu[n], "G03-rota-augmentation")
        require(augmentation(lifted) == mu_trial(n), "G03-trial-augmentation")

    return refined_table, lifted_table


def shell_from_words(split_primes, multiplier):
    terms = []
    multiplier_sign = mu_trial(multiplier)
    for word in itertools.product((-1, 0, 1), repeat=len(split_primes)):
        coefficient = multiplier_sign
        exponents = []
        for prime, choice in zip(split_primes, word):
            if choice != 0:
                coefficient = -coefficient
                exponents.append((prime, choice))
        terms.append((tuple(exponents), coefficient))
    return poly_from_terms(terms)


def shell_from_pipeline(split_primes, multiplier, spf):
    result = dict(ONE)
    for prime in split_primes:
        result = poly_mul(result, local_u_from_choices(prime, 1))
    for prime, exponent in factor_with_spf(multiplier, spf):
        result = poly_mul(result, local_u_from_choices(prime, exponent))
    return result


def gate_04_shell_census(spf):
    for mask in range(1 << len(SPLIT6)):
        chosen = tuple(
            prime
            for index, prime in enumerate(SPLIT6)
            if mask & (1 << index)
        )
        split_count = len(chosen)
        expected_size = 3 ** split_count
        for multiplier in MULTIPLIERS:
            shell = shell_from_pipeline(chosen, multiplier, spf)
            expected = shell_from_words(chosen, multiplier)
            require(shell == expected, "G04-word-pipeline-equality")
            require(len(shell) == expected_size, "G04-support")
            require(l1_norm(shell) == expected_size, "G04-l1")
            require(l2_squared(shell) == expected_size, "G04-l2-squared")
            require(
                all(abs(value) == 1 for value in shell.values()),
                "G04-unit-coefficients",
            )
            expected_augmentation = (
                mu_trial(multiplier)
                * (-1 if split_count % 2 else 1)
            )
            require(
                augmentation(shell) == expected_augmentation,
                "G04-augmentation",
            )

    for prime in SPLIT6:
        for exponent in range(2, E_MAX + 1):
            split_square = local_u_from_choices(prime, exponent)
            require(split_square, "G04-split-square-nonzero")
            require(
                augmentation(split_square) == 0,
                "G04-split-square-cancels",
            )
            require(
                split_square == local_u_closed(prime, exponent),
                "G04-split-square-form",
            )
            require(len(split_square) == 3, "G04-split-square-support")
            require(l1_norm(split_square) == 4, "G04-split-square-l1")
            require(
                l2_squared(split_square) == 6,
                "G04-split-square-l2-squared",
            )

    for prime in (2, 5):
        for exponent in range(2, E_MAX + 1):
            require(
                not local_u_from_choices(prime, exponent),
                "G04-nonsplit-square-kills",
            )


def gate_05_zero_channel(lifted_table, spf, primes):
    for prime in primes:
        kind = prime_type(prime)
        for exponent in range(E_MAX + 1):
            extracted = constant_term(
                local_u_from_choices(prime, exponent)
            )
            if exponent == 0:
                expected = 1
            elif kind == "split":
                expected = 1 if exponent == 1 else 2
            else:
                expected = -1 if exponent == 1 else 0
            require(extracted == expected, "G05-local-c0-extraction")

    c0 = [0] * (N_C0 + 1)
    for n in range(1, N_C0 + 1):
        c0[n] = constant_term(lifted_table[n])
        require(c0[n] == c0_local_value(n, spf), "G05-c0-local")
    return c0


def gate_06_c0_analytic(c0, mu):
    base, analytic = c0_analytic_arrays(N_C0, mu)
    require(c0 == analytic, "G06-c0-analytic-dirichlet")
    return base


def gate_07_c0_o5(primes, c0, mu):
    target = [0] * (E_MAX + 1)
    target[0] = 1
    target[1] = -1
    for prime in primes:
        c0_series = [
            constant_term(local_u_from_choices(prime, exponent))
            for exponent in range(E_MAX + 1)
        ]
        if prime_type(prime) == "split":
            orientation_series = [
                orientation_local_coefficient(exponent)
                for exponent in range(E_MAX + 1)
            ]
        else:
            orientation_series = [1] + [0] * E_MAX
        require(
            scalar_series_convolution(
                c0_series,
                orientation_series,
                E_MAX,
            )
            == target,
            "G07-local-c0-o5",
        )

    euler = orientation_euler_coefficients(N_O5)
    analytic = orientation_analytic_coefficients(N_O5, mu)
    require(euler == analytic, "G07-o5-two-routes")

    zero_channel = c0[: N_O5 + 1]
    rational_inverse_zeta = dirichlet_convolution(
        zero_channel,
        euler,
        N_O5,
    )
    require(
        rational_inverse_zeta == mu[: N_O5 + 1],
        "G07-c0-o5-mu",
    )


def gate_08_triangle(lifted_table, mu):
    checkpoints = {10, 100, 1_000, N_O5}
    cumulative_l1 = 0
    squarefree_count = 0
    checked = 0

    for n in range(1, N_O5 + 1):
        lifted = lifted_table[n]
        require(
            abs(augmentation(lifted)) <= l1_norm(lifted),
            "G08-pointwise-triangle",
        )
        cumulative_l1 += l1_norm(lifted)
        squarefree_count += abs(mu[n])
        if n in checkpoints:
            require(
                cumulative_l1 >= squarefree_count,
                "G08-summatory-triangle",
            )
            require(
                4 * squarefree_count > n,
                "G08-elementary-linear-squarefree-lower-bound",
            )
            checked += 1
    require(checked == len(checkpoints), "G08-all-checkpoints")


def first_difference(left, right, start, stop):
    for index in range(start, stop + 1):
        if left[index] != right[index]:
            return index
    return 0


def gate_09_pipeline_breakers(lifted_table, c0, c0_base, primes):
    # B01: collapse X_p to 1 before extracting the neutral coefficient.
    b01 = 0
    for n in range(2, N_C0 + 1):
        collapsed = poly_from_terms((((), augmentation(lifted_table[n])),))
        if constant_term(collapsed) != constant_term(lifted_table[n]):
            b01 = n
            break
    require(b01 == 11, "G09-B01-collapse-before-c0")

    # B02: omit the split character denominator in the actual convolution.
    b02 = 0
    for prime in primes:
        if prime_type(prime) != "split":
            continue
        mutated = local_u_from_choices(
            prime,
            1,
            omit_split_character=True,
        )
        if mutated != local_u_closed(prime, 1):
            b02 = prime
            break
    require(b02 == 11, "G09-B02-omit-split-denominator")

    # B03: omit the ramified Euler correction from the analytic C0 route.
    b03 = first_difference(c0_base, c0, 1, N_C0)
    require(b03 == 5, "G09-B03-omit-five-correction")

    # B04: duplicate both split orientations inside the ideal-choice builder.
    b04 = 0
    for prime in primes:
        if prime_type(prime) != "split":
            continue
        duplicated = local_u_from_choices(
            prime,
            1,
            orientation_mode="duplicate",
        )
        if poly_star(duplicated) != duplicated:
            b04 = prime
            break
    require(b04 == 11, "G09-B04-duplicate-orientation")

    # B05: send the ramified prime through the inert ideal-choice branch.
    ramified_mutation = local_u_from_choices(
        5,
        1,
        type_override="inert",
    )
    b05 = 5 if augmentation(ramified_mutation) != mu_trial(5) else 0
    require(b05 == 5, "G09-B05-ramified-as-inert")

    # B06: identify two independent split-prime Laurent variables.
    collapsed_variables = poly_mul(
        local_u_from_choices(11, 1),
        local_u_from_choices(19, 1),
        key_map={11: 0, 19: 0},
    )
    independent_variables = poly_mul(
        local_u_from_choices(11, 1),
        local_u_from_choices(19, 1),
    )
    b06 = 11 * 19 if (
        len(independent_variables) == 9
        and len(collapsed_variables) == 5
    ) else 0
    require(b06 == 209, "G09-B06-collapse-independent-variables")

    return (b01, b02, b03, b04, b05, b06)


def source_firewall(path):
    raw = path.read_bytes()
    require(b"\r" not in raw, "G10-lf-source")
    source = raw.decode("utf-8")
    tree = ast.parse(source, filename=str(path))

    allowed_imports = {
        "ast",
        "itertools",
        "math",
        "pathlib",
        "sys",
    }
    forbidden_calls = {
        "__import__",
        "complex",
        "eval",
        "exec",
        "float",
        "getenv",
        "log",
        "exp",
        "round",
        "sqrt",
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            require(
                not isinstance(node.value, (float, complex)),
                "G10-no-inexact-constants",
            )
        if isinstance(node, ast.BinOp):
            require(not isinstance(node.op, ast.Div), "G10-no-true-division")
            if isinstance(node.op, ast.Pow):
                require(
                    not (
                        isinstance(node.right, ast.UnaryOp)
                        and isinstance(node.right.op, ast.USub)
                        and isinstance(node.right.operand, ast.Constant)
                        and isinstance(node.right.operand.value, int)
                    ),
                    "G10-no-negative-integer-power",
                )
        if isinstance(node, ast.Import):
            for alias in node.names:
                require(alias.name in allowed_imports, "G10-import-allowlist")
        if isinstance(node, ast.ImportFrom):
            require(
                node.module in allowed_imports,
                "G10-from-import-allowlist",
            )
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                require(
                    node.func.id not in forbidden_calls,
                    "G10-forbidden-call",
                )
                if node.func.id == "pow" and len(node.args) >= 2:
                    exponent = node.args[1]
                    require(
                        not (
                            isinstance(exponent, ast.UnaryOp)
                            and isinstance(exponent.op, ast.USub)
                            and isinstance(exponent.operand, ast.Constant)
                            and isinstance(exponent.operand.value, int)
                        ),
                        "G10-no-negative-pow-argument",
                    )
            if isinstance(node.func, ast.Attribute):
                require(
                    not (
                        isinstance(node.func.value, ast.Name)
                        and node.func.value.id in ("cmath", "math")
                        and node.func.attr == "sqrt"
                    ),
                    "G10-no-inexact-sqrt",
                )

    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    graph = {name: set() for name in functions}
    for name, function in functions.items():
        for node in ast.walk(function):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id in functions
            ):
                graph[name].add(node.func.id)

    reachable = set()
    frontier = ["refined_b"]
    while frontier:
        name = frontier.pop()
        if name in reachable:
            continue
        reachable.add(name)
        frontier.extend(sorted(graph.get(name, ())))

    construction_oracles = {
        "bold_mu_product",
        "c0_local_value",
        "chi5",
        "local_b_closed",
        "local_u_closed",
        "mu_rota_table",
        "mu_trial",
        "orientation_local_coefficient",
        "prime_type",
    }
    require(
        reachable.isdisjoint(construction_oracles),
        "G10-refined-ideal-construction-firewall",
    )


def gate_10_reynolds_firewall(lifted_table):
    for prime in SPLIT6:
        pair = poly_from_terms(
            (
                (monomial(prime, 1), -1),
                (monomial(prime, -1), -1),
            )
        )
        new_degree_one = local_u_closed(prime, 1)
        new_degree_two = local_u_closed(prime, 2)
        require(
            poly_scale(2, new_degree_one) != pair,
            "G10-reynolds-degree-one-distinction",
        )
        require(
            augmentation(pair) == -2
            and augmentation(new_degree_one) == -1,
            "G10-reynolds-shared-scalar-augmentation",
        )
        require(
            new_degree_two != {}
            and augmentation(new_degree_two) == 0,
            "G10-reynolds-degree-two-distinction",
        )

    source_firewall(pathlib.Path(__file__))
    samples = (1, 2, 5, 11, 19, 209, N_GLOBAL)
    for n in samples:
        serialized = serialize_poly(lifted_table[n])
        rebuilt = poly_from_terms(tuple(lifted_table[n].items()))
        require(
            serialized == serialize_poly(rebuilt),
            "G10-deterministic-laurent-serialization",
        )


def main():
    sys.stdout.reconfigure(newline="\n")
    require(len(sys.argv) == 1, "no-command-line-arguments")

    spf = spf_sieve(N_GLOBAL)
    primes = primes_upto(P_MAX)
    mu = mu_rota_table(N_GLOBAL)

    gate_01_projective(primes)
    gate_02_local_ideal_choices(primes)
    _, lifted_table = gate_03_global(spf, mu)
    gate_04_shell_census(spf)
    c0 = gate_05_zero_channel(lifted_table, spf, primes)
    c0_base = gate_06_c0_analytic(c0, mu)
    gate_07_c0_o5(primes, c0, mu)
    gate_08_triangle(lifted_table, mu)
    breakers = gate_09_pipeline_breakers(
        lifted_table,
        c0,
        c0_base,
        primes,
    )
    gate_10_reynolds_firewall(lifted_table)

    lines = (
        "G01 projective-fixed-line-character p<=997 PASS",
        "G02 ideal-choice-local-lift e<=8 PASS",
        "G03 global-character-lift n<=20000 PASS",
        "G04 orientation-shell-census split6 multipliers=1,2,5,10 PASS",
        "G05 zero-rapidity-channel n<=10000 PASS",
        "G06 C0-analytic-convolution n<=10000 PASS",
        "G07 C0-O5 local e<=8 global n<=5000 PASS",
        "G08 direct-l1-triangle no-go checkpoints<=5000 PASS",
        "G09 pipeline-breakers 6/6 FIRE "
        + ",".join(str(value) for value in breakers),
        "G10 Reynolds-distinction AST-LF-callgraph-firewall PASS",
        "VERIFY RESULT 10/10 ALL PASS",
    )
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
