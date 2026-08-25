#!/usr/bin/env python3
"""Exact audit for P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1.

Standard library only.  Polynomials use low-to-high coefficient order.
The global theorem is proved in PREREG.md; this verifier audits the frozen
finite counterexample surface and exact target/falsifier controls.
"""

from fractions import Fraction


PROBE = "P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1"
CONFIRMED = "J-SIGNED-TRACE-MAHLER-RIGIDITY-CONFIRMED"
FIRED = "J-SIGNED-TRACE-MAHLER-RIGIDITY-FIRED"


def require(condition, message):
    if not condition:
        raise RuntimeError("STOP: " + message)


def sign(value):
    return (value > 0) - (value < 0)


def trim(poly):
    out = [Fraction(value) for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [Fraction(0)]


def poly_add(left, right):
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def poly_scale(poly, scalar):
    scalar = Fraction(scalar)
    return trim([scalar * value for value in poly])


def poly_mul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += left_value * right_value
    return trim(out)


def poly_pow(poly, exponent):
    require(exponent >= 0, "negative polynomial exponent")
    result = [Fraction(1)]
    factor = trim(poly)
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        power >>= 1
    return result


def poly_derivative(poly):
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def poly_eval(poly, point):
    point = Fraction(point)
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def poly_divmod(numerator, denominator):
    numerator = trim(numerator)
    denominator = trim(denominator)
    require(denominator != [Fraction(0)], "polynomial division by zero")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0) for _ in range(len(numerator) - len(denominator) + 1)]
    remainder = numerator[:]
    while remainder != [Fraction(0)] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] / denominator[-1]
        quotient[shift] += factor
        for index, coefficient in enumerate(denominator):
            remainder[index + shift] -= factor * coefficient
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def sturm_sequence(poly):
    first = trim(poly)
    second = poly_derivative(first)
    require(second != [Fraction(0)], "constant polynomial in Sturm sequence")
    sequence = [first, second]
    while True:
        _, remainder = poly_divmod(sequence[-2], sequence[-1])
        if remainder == [Fraction(0)]:
            break
        sequence.append(poly_scale(remainder, -1))
    return sequence


def sign_at_infinity(poly, direction):
    leading_sign = sign(trim(poly)[-1])
    degree = len(trim(poly)) - 1
    if direction < 0 and degree % 2:
        leading_sign = -leading_sign
    return leading_sign


def sign_at_side(poly, point, direction):
    derivative = trim(poly)
    order = 0
    while True:
        value = poly_eval(derivative, point)
        if value != 0:
            value_sign = sign(value)
            if direction < 0 and order % 2:
                value_sign = -value_sign
            return value_sign
        require(derivative != [Fraction(0)], "zero Sturm polynomial")
        derivative = poly_derivative(derivative)
        order += 1


def variations(signs):
    nonzero = [value for value in signs if value]
    return sum(left != right for left, right in zip(nonzero, nonzero[1:]))


def strict_roots_outside_three(poly):
    sequence = sturm_sequence(poly)
    at_negative_infinity = variations(
        [sign_at_infinity(item, -1) for item in sequence]
    )
    just_left_of_minus_three = variations(
        [sign_at_side(item, -3, -1) for item in sequence]
    )
    just_right_of_three = variations(
        [sign_at_side(item, 3, 1) for item in sequence]
    )
    at_positive_infinity = variations(
        [sign_at_infinity(item, 1) for item in sequence]
    )
    left_count = at_negative_infinity - just_left_of_minus_three
    right_count = just_right_of_three - at_positive_infinity
    require(left_count >= 0 and right_count >= 0, "invalid Sturm root count")
    return left_count + right_count


def fixed_add(left, right):
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def fixed_shift(poly):
    return [Fraction(0)] + list(poly)


def bezout_matrix(real_poly, imaginary_poly, degree):
    real_poly = list(real_poly) + [Fraction(0)] * (degree + 1 - len(real_poly))
    imaginary_poly = list(imaginary_poly) + [Fraction(0)] * (
        degree + 1 - len(imaginary_poly)
    )
    numerator = [
        [Fraction(0) for _ in range(degree + 1)]
        for _ in range(degree + 1)
    ]
    for x_degree in range(degree + 1):
        for y_degree in range(degree + 1):
            numerator[x_degree][y_degree] += (
                real_poly[x_degree] * imaginary_poly[y_degree]
            )
            numerator[x_degree][y_degree] -= (
                imaginary_poly[x_degree] * real_poly[y_degree]
            )

    quotient = [None for _ in range(degree)]
    quotient[degree - 1] = numerator[degree][:]
    for x_degree in range(degree - 1, 0, -1):
        quotient[x_degree - 1] = fixed_add(
            numerator[x_degree], fixed_shift(quotient[x_degree])
        )

    expected_constant = [-value for value in fixed_shift(quotient[0])]
    width = max(len(expected_constant), len(numerator[0]))
    expected_constant += [Fraction(0)] * (width - len(expected_constant))
    actual_constant = numerator[0] + [Fraction(0)] * (width - len(numerator[0]))
    require(expected_constant == actual_constant, "Bezout division remainder")

    matrix = []
    for x_degree in range(degree):
        row = quotient[x_degree] + [Fraction(0)] * (
            degree + 1 - len(quotient[x_degree])
        )
        require(all(value == 0 for value in row[degree:]), "oversize Bezout row")
        matrix.append(row[:degree])
    require(
        all(matrix[i][j] == matrix[j][i] for i in range(degree) for j in range(degree)),
        "asymmetric Bezoutian",
    )
    return matrix


def reorder_symmetric(matrix, leading_indices):
    order = list(leading_indices) + [
        index for index in range(len(matrix)) if index not in leading_indices
    ]
    return [[matrix[row][column] for column in order] for row in order]


def symmetric_inertia(matrix):
    current = [[Fraction(value) for value in row] for row in matrix]
    require(
        all(len(row) == len(current) for row in current), "nonsquare symmetric form"
    )
    positive = negative = zero = 0
    while current:
        size = len(current)
        require(
            all(current[i][j] == current[j][i] for i in range(size) for j in range(size)),
            "inertia input lost symmetry",
        )
        diagonal = next((index for index in range(size) if current[index][index]), None)
        if diagonal is not None:
            current = reorder_symmetric(current, [diagonal])
            pivot = current[0][0]
            if pivot > 0:
                positive += 1
            else:
                negative += 1
            current = [
                [
                    current[row][column]
                    - current[row][0] * current[0][column] / pivot
                    for column in range(1, size)
                ]
                for row in range(1, size)
            ]
            continue

        off_diagonal = None
        for row in range(size):
            for column in range(row + 1, size):
                if current[row][column]:
                    off_diagonal = (row, column)
                    break
            if off_diagonal is not None:
                break
        if off_diagonal is None:
            zero += size
            break

        first, second = off_diagonal
        current = reorder_symmetric(current, [first, second])
        coupling = current[0][1]
        require(
            current[0][0] == 0 and current[1][1] == 0 and coupling != 0,
            "invalid two-by-two inertia pivot",
        )
        positive += 1
        negative += 1
        current = [
            [
                current[row][column]
                - (
                    current[row][0] * current[1][column]
                    + current[row][1] * current[0][column]
                )
                / coupling
                for column in range(2, size)
            ]
            for row in range(2, size)
        ]
    return positive, negative, zero


def split_at_imaginary_axis(poly):
    real = [Fraction(0) for _ in poly]
    imaginary = [Fraction(0) for _ in poly]
    for degree, coefficient in enumerate(poly):
        residue = degree % 4
        if residue == 0:
            real[degree] += coefficient
        elif residue == 1:
            imaginary[degree] += coefficient
        elif residue == 2:
            real[degree] -= coefficient
        else:
            imaginary[degree] -= coefficient
    return trim(real), trim(imaginary)


def half_plane_profile(poly):
    poly = trim(poly)
    degree = len(poly) - 1
    require(degree >= 1, "constant half-plane polynomial")
    real, imaginary = split_at_imaginary_axis(poly)
    matrix = bezout_matrix(real, imaginary, degree)
    return symmetric_inertia(matrix)


def f_poly(a, b, c):
    return [Fraction(1), Fraction(c), Fraction(b), Fraction(a), Fraction(1)]


def cayley_poly(a, b, c):
    coefficients = f_poly(a, b, c)
    plus = [Fraction(1), Fraction(1)]
    minus = [Fraction(-1), Fraction(1)]
    result = [Fraction(0)]
    for degree, coefficient in enumerate(coefficients):
        term = poly_mul(poly_pow(plus, degree), poly_pow(minus, 4 - degree))
        result = poly_add(result, poly_scale(term, coefficient))
    require(len(result) == 5, "Cayley transform lost degree")
    require(result[4] == a + b + c + 2, "Cayley leading coefficient")
    require(result[3] == 2 * (a - c), "Cayley cubic coefficient")
    require(result[3] != 0, "frozen parity failed Cayley regularity")
    return result


def root_profile(a, b, c):
    right, left, axis = half_plane_profile(cayley_poly(a, b, c))
    require(right + left + axis == 4, "half-plane inertia dimension")
    return right, left, axis


def h_poly(a, b, c):
    return [
        Fraction(4 * b - a * a - c * c),
        Fraction(a * c - 4),
        Fraction(-b),
        Fraction(1),
    ]


def mod_two_class(a, b, c):
    parity = (a % 2, b % 2, c % 2)
    if parity == (0, 0, 1):
        return "p_L"
    if parity == (1, 0, 0):
        return "p_R"
    return "none"


def bit_degree(poly):
    return poly.bit_length() - 1


def bit_remainder(numerator, denominator):
    require(denominator != 0, "binary polynomial division by zero")
    remainder = numerator
    denominator_degree = bit_degree(denominator)
    while remainder and bit_degree(remainder) >= denominator_degree:
        remainder ^= denominator << (bit_degree(remainder) - denominator_degree)
    return remainder


def gf16_mul(left, right, modulus):
    result = 0
    factor = left
    multiplier = right
    while multiplier:
        if multiplier & 1:
            result ^= factor
        multiplier >>= 1
        factor <<= 1
        if factor & 0b10000:
            factor ^= modulus
    require(result < 16, "GF(16) reduction overflow")
    return result


def gf16_pow(base, exponent, modulus):
    result = 1
    factor = base
    power = exponent
    while power:
        if power & 1:
            result = gf16_mul(result, factor, modulus)
        factor = gf16_mul(factor, factor, modulus)
        power >>= 1
    return result


def binary_control(modulus):
    no_linear_root = (modulus & 1) == 1 and modulus.bit_count() % 2 == 1
    no_quadratic_factor = bit_remainder(modulus, 0b111) != 0
    order_fifteen = (
        gf16_pow(0b10, 15, modulus) == 1
        and gf16_pow(0b10, 5, modulus) != 1
        and gf16_pow(0b10, 3, modulus) != 1
    )
    return no_linear_root and no_quadratic_factor and order_fifteen


def sign_q_sqrt5(rational, radical):
    rational = Fraction(rational)
    radical = Fraction(radical)
    if radical == 0:
        return sign(rational)
    if rational == 0:
        return sign(radical)
    if rational > 0 and radical > 0:
        return 1
    if rational < 0 and radical < 0:
        return -1
    comparison = rational * rational - 5 * radical * radical
    if rational > 0 and radical < 0:
        return sign(comparison)
    return -sign(comparison)


def shifted_phi_five():
    result = [Fraction(0)]
    x_minus_one = [Fraction(-1), Fraction(1)]
    for degree in range(5):
        result = poly_add(result, poly_pow(x_minus_one, degree))
    return result


def negate_variable(poly):
    return trim([(-coefficient if degree % 2 else coefficient) for degree, coefficient in enumerate(poly)])


def format_pairs(pairs):
    if not pairs:
        return "none"
    return ",".join("(%d,%d)" % pair for pair in pairs)


def format_counts(counts):
    parts = ["%d:%d" % (key, counts[key]) for key in sorted(counts)]
    return ",".join(parts) if parts else "none"


def finite_a2_audit(require_a3):
    total = 0
    h_outside_rows = 0
    residual_profiles = {}
    residual_unit_rows = 0
    survivors = []
    for b in range(-15, 16):
        for c in range(-10, 11):
            if b % 2 or c % 2:
                continue
            if require_a3 and b + c != 2:
                continue
            total += 1
            if strict_roots_outside_three(h_poly(-3, b, c)):
                h_outside_rows += 1
                continue
            outside, inside, axis = root_profile(-3, b, c)
            if axis:
                residual_unit_rows += 1
                continue
            require(outside + inside == 4, "residual root profile dimension")
            residual_profiles[outside] = residual_profiles.get(outside, 0) + 1
            if outside == 2:
                survivors.append((b, c))
    return total, h_outside_rows, residual_profiles, residual_unit_rows, survivors


def main():
    # Calibrate the Bezoutian sign convention and exact inertia implementation.
    require(half_plane_profile([-1, 1]) == (1, 0, 0), "right-half-plane calibration")
    require(half_plane_profile([1, 1]) == (0, 1, 0), "left-half-plane calibration")
    require(
        half_plane_profile([1, -2, 1]) == (2, 0, 0),
        "quadratic right-half-plane calibration",
    )
    require(
        half_plane_profile([1, 2, 1]) == (0, 2, 0),
        "quadratic left-half-plane calibration",
    )
    require(
        half_plane_profile([-2, 1, 1]) == (1, 1, 0),
        "nonsymmetric split half-plane calibration",
    )

    p_l_modulus = 0b10011
    p_r_modulus = 0b11001
    binary_l = binary_control(p_l_modulus)
    binary_r = binary_control(p_r_modulus)

    target = f_poly(-3, 4, -2)
    target_identity = target == shifted_phi_five()
    target_profile = root_profile(-3, 4, -2)
    target_h_factor = h_poly(-3, 4, -2) == poly_mul(
        [Fraction(-3), Fraction(1)],
        [Fraction(-1), Fraction(-1), Fraction(1)],
    )
    target_control = (
        mod_two_class(-3, 4, -2) == "p_R"
        and target_identity
        and target_profile == (2, 2, 0)
        and target_h_factor
        and poly_eval(target, 1) == 1
        and strict_roots_outside_three(h_poly(-3, 4, -2)) == 0
    )

    lower = (-1, 0, 0)
    lower_profile = root_profile(*lower)
    landau_strict = 3 < 4 and sign_q_sqrt5(-1, 1) > 0
    lower_control = (
        mod_two_class(*lower) == "p_R"
        and lower_profile == (2, 2, 0)
        and landau_strict
    )

    oriented_tie = (3, 4, 2)
    left_tie = (-2, 4, -3)
    oriented_tie_control = (
        f_poly(*oriented_tie) == negate_variable(target)
        and mod_two_class(*oriented_tie) == "p_R"
        and root_profile(*oriented_tie) == (2, 2, 0)
        and strict_roots_outside_three(h_poly(*oriented_tie)) == 0
    )
    left_tie_control = (
        f_poly(*left_tie) == list(reversed(target))
        and mod_two_class(*left_tie) == "p_L"
        and root_profile(*left_tie) == (2, 2, 0)
        and strict_roots_outside_three(h_poly(*left_tie)) == 0
    )

    window_control = (
        sign_q_sqrt5(5, -2) > 0
        and sign_q_sqrt5(7, -3) > 0
    )
    a0_rows = a1_rows = 0
    for a in range(-10, 11):
        for b in range(-15, 16):
            for c in range(-10, 11):
                binary_class = mod_two_class(a, b, c)
                if binary_class in ("p_L", "p_R"):
                    a0_rows += 1
                if binary_class == "p_R":
                    a1_rows += 1

    a2 = finite_a2_audit(False)
    a3 = finite_a2_audit(True)
    a2_total, a2_h_outside, a2_profiles, a2_units, a2_survivors = a2
    a3_total, a3_h_outside, a3_profiles, a3_units, a3_survivors = a3

    surface_ok = (
        window_control
        and a0_rows == 3300
        and a1_rows == 1650
        and a2_total == 165
        and a3_total == 11
        and a2_h_outside + sum(a2_profiles.values()) + a2_units == a2_total
        and a3_h_outside + sum(a3_profiles.values()) + a3_units == a3_total
    )
    controls_ok = all(
        (
            binary_l,
            binary_r,
            target_control,
            lower_control,
            oriented_tie_control,
            left_tie_control,
            surface_ok,
        )
    )
    a0_negative = lower_control and oriented_tie_control and left_tie_control
    a1_negative = lower_control and oriented_tie_control
    a2_positive = (
        a2_total == 165
        and a2_h_outside == 127
        and a2_profiles == {1: 8, 2: 1, 3: 29}
        and a2_units == 0
        and a2_survivors == [(4, -2)]
    )
    a3_positive = (
        a3_total == 11
        and a3_h_outside == 10
        and a3_profiles == {2: 1}
        and a3_units == 0
        and a3_survivors == [(4, -2)]
    )
    decision = CONFIRMED if all(
        (controls_ok, a0_negative, a1_negative, a2_positive, a3_positive)
    ) else FIRED

    print("PROBE " + PROBE)
    print(
        "BINARY p_L_irreducible_order15=%s p_R_irreducible_order15=%s"
        % ("PASS" if binary_l else "FAIL", "PASS" if binary_r else "FAIL")
    )
    print(
        "TARGET profile=%d/%d/%d phi5_shift=%s H_factor=%s"
        % (
            target_profile[0],
            target_profile[1],
            target_profile[2],
            "PASS" if target_identity else "FAIL",
            "PASS" if target_h_factor else "FAIL",
        )
    )
    print(
        "A0 %s candidates=%d F_LOWER=%s F_TIE_R=%s F_TIE_L=%s"
        % (
            "FALSE" if a0_negative else "FIRED",
            a0_rows,
            "PASS" if lower_control else "FAIL",
            "PASS" if oriented_tie_control else "FAIL",
            "PASS" if left_tie_control else "FAIL",
        )
    )
    print(
        "A1 %s candidates=%d F_LOWER=%s F_TIE=%s"
        % (
            "FALSE" if a1_negative else "FIRED",
            a1_rows,
            "PASS" if lower_control else "FAIL",
            "PASS" if oriented_tie_control else "FAIL",
        )
    )
    print(
        "A2 %s candidates=%d H_outside=%d residual=%d profiles=%s unit=%d survivors=%s"
        % (
            "TRUE" if a2_positive else "FIRED",
            a2_total,
            a2_h_outside,
            a2_total - a2_h_outside,
            format_counts(a2_profiles),
            a2_units,
            format_pairs(a2_survivors),
        )
    )
    print(
        "A3 %s candidates=%d H_outside=%d residual=%d profiles=%s unit=%d survivors=%s"
        % (
            "TRUE" if a3_positive else "FIRED",
            a3_total,
            a3_h_outside,
            a3_total - a3_h_outside,
            format_counts(a3_profiles),
            a3_units,
            format_pairs(a3_survivors),
        )
    )
    print("SURFACE complete=%s" % ("PASS" if surface_ok else "FAIL"))
    print("DECISION " + decision)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
