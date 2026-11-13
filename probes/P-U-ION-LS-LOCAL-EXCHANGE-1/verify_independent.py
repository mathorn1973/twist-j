#!/usr/bin/env python3
"""Independent exact fixed-profile LS and carrier audit; execute only after pin.

Arithmetic is Q(i,sqrt(2)), represented in the basis (1,sqrt(2),i,i*sqrt(2)).
The twenty raw-loop phases are checked as polynomials, not numerically sampled.
Only the declared contact columns are claimed for the complete contact word.
No physical calibration, motion truncation, numerical integration or primary
scientific implementation is imported by this independent executable.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
import sys


ZERO = (F(0), F(0), F(0), F(0))
ONE = (F(1), F(0), F(0), F(0))
IMAG = (F(0), F(0), F(1), F(0))
HALF_ROOT = (F(0), F(1, 2), F(0), F(0))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (a*e + 2*b*f - c*g - 2*d*h,
            a*f + b*e - c*h - d*g,
            a*g + 2*b*h + c*e + 2*d*f,
            a*h + b*g + c*f + d*e)


def conjugate(x):
    return x[0], x[1], -x[2], -x[3]


def scale(x, scalar):
    return tuple(scalar * a for a in x)


def field_sum(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def identity(size):
    return [[ONE if row == col else ZERO for col in range(size)] for row in range(size)]


def product(left, right):
    size = len(left)
    return [[field_sum(mul(left[row][k], right[k][col]) for k in range(size))
             for col in range(size)] for row in range(size)]


def adjoint(matrix):
    return [[conjugate(matrix[col][row]) for col in range(len(matrix))]
            for row in range(len(matrix))]


def rotation(a, b, angle, phase):
    """R_ab: angle and phase are integer multiples of pi/2."""
    require(a != b and 0 <= a < 5 and 0 <= b < 5, "rotation labels")
    cosines = (ONE, HALF_ROOT, ZERO, neg(HALF_ROOT), neg(ONE),
               neg(HALF_ROOT), ZERO, HALF_ROOT)
    sines = (ZERO, HALF_ROOT, ONE, HALF_ROOT, ZERO,
             neg(HALF_ROOT), neg(ONE), neg(HALF_ROOT))
    c, s = cosines[angle % 8], sines[angle % 8]
    phase_value = (ONE, IMAG, neg(ONE), neg(IMAG))[phase % 4]
    result = identity(5)
    result[a][a] = result[b][b] = c
    minus_i_s = mul(neg(IMAG), s)
    result[a][b] = mul(minus_i_s, conjugate(phase_value))
    result[b][a] = mul(minus_i_s, phase_value)
    return result


def inverse_word(word):
    return [(j, angle, (phase + 2) % 4) for j, angle, phase in reversed(word)]


def local_word(word):
    """Word entries are chronological common star carrier pulses."""
    result = identity(5)
    for j, angle, phase in word:
        require(j in (1, 2, 3, 4) and angle in (1, 2, 4), "undeclared carrier primitive")
        result = product(rotation(0, j, angle, phase), result)
    return result


def embedded_word(c, j, angle, phase):
    require(c in (1, 4) and j != c and 0 <= j < 5, "embedded rotation labels")
    if j == 0:
        return [(c, angle, (-phase) % 4)]
    # T=R_0c(pi,0); chronological T^dagger,R_0j(theta,phi-pi/2),T.
    return [(c, 2, 2), (j, angle, (phase - 1) % 4), (c, 2, 0)]


def transpose_labels(u, v):
    """Physical star pulses implementing a label transposition, including phases."""
    require(u != v, "empty transposition")
    if u == 0:
        return [(v, 2, 0)]
    if v == 0:
        return [(u, 2, 0)]
    return [(u, 2, 0), (v, 2, 0), (u, 2, 0)]


def permutation_word(permutation):
    # Greedily correct output labels rather than decomposing into cycles.
    current = list(range(5))
    pulses = []
    for source in range(5):
        if current[source] == permutation[source]:
            continue
        u, v = current[source], permutation[source]
        pulses.extend(transpose_labels(u, v))
        current = [v if image == u else u if image == v else image for image in current]
    require(current == list(permutation), "permutation compiler label mismatch")
    return pulses


def monomial_image(matrix):
    images, phases = [], []
    for col in range(5):
        support = [row for row in range(5) if matrix[row][col] != ZERO]
        require(len(support) == 1, "compiled frame is not monomial")
        row = support[0]
        amplitude = matrix[row][col]
        require(mul(conjugate(amplitude), amplitude) == ONE, "frame phase not unit modulus")
        images.append(row)
        phases.append(amplitude)
    require(len(set(images)) == 5, "compiled monomial is not a permutation")
    return images, phases


def phase_polynomial(u, v):
    """(d_u-d_v)^2 as coefficients of unordered quadratic monomials."""
    result = {}
    for first, second, coefficient in ((u, u, 1), (v, v, 1), (u, v, -2)):
        key = tuple(sorted((first, second)))
        result[key] = result.get(key, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def fixed_profile_echo():
    """Compile the 20 affine frames and derive the common echo phase exactly."""
    frames = []
    carrier_count = 0
    for multiplier in range(1, 5):
        for offset in range(5):
            permutation = [(multiplier*j + offset) % 5 for j in range(5)]
            word = permutation_word(permutation)
            matrix = local_word(word)
            images, phases = monomial_image(matrix)
            require(images == permutation, "affine frame support mismatch")
            require(product(local_word(inverse_word(word)), matrix) == identity(5),
                    "compiled affine frame inverse failed")
            frames.append((images, phases))
            carrier_count += 2 * len(word)
    require(len(frames) == 20, "incomplete affine frame family")

    # B=5*sum(d_j^2)-(sum d_j)^2.  Neither d_j nor B is fitted to output.
    twice_b = {(j, j): 8 for j in range(5)}
    twice_b.update({(j, k): -4 for j in range(5) for k in range(j + 1, 5)})
    diagonal = []
    for s in range(5):
        for q in range(5):
            total = {}
            for images, phases in frames:
                pair_phase = mul(phases[s], phases[q])
                require(mul(conjugate(pair_phase), pair_phase) == ONE,
                        "monomial phases did not cancel in raw-loop conjugation")
                polynomial = phase_polynomial(images[s], images[q])
                for key, value in polynomial.items():
                    total[key] = total.get(key, 0) + value
            total = {key: value for key, value in total.items() if value}
            if not total:
                require(s == q, "unexpected zero phase polynomial")
                diagonal.append(ONE)
            else:
                require(s != q and total == twice_b, "fixed-profile twirl polynomial mismatch")
                # The raw-loop exponent is -K*lambda_*^2*(d_u-d_v)^2.
                # K*lambda_*^2=pi/(4B), B>0 gives -pi/2 after the twirl.
                phase_in_pi_units = -F(1, 4) * 2
                require(phase_in_pi_units == -F(1, 2), "echo calibration factor")
                diagonal.append(neg(IMAG))
    for s in range(5):
        coverage = [sum(images[s] == level for images, _ in frames) for level in range(5)]
        require(coverage == [4] * 5, "fixed local diagonal phase not scalar after twirl")
    return diagonal, carrier_count


def basis_vector(s, q):
    return [ONE if index == 5*s + q else ZERO for index in range(25)]


def collective_carrier(state, pulse):
    j, angle, phase = pulse
    require(j in (1, 2, 3, 4) and angle in (1, 2, 4), "invalid physical carrier pulse")
    local = rotation(0, j, angle, phase)
    intermediate = list(state)
    for q in range(5):
        first, second = state[q], state[5*j + q]
        intermediate[q] = add(mul(local[0][0], first), mul(local[0][j], second))
        intermediate[5*j + q] = add(mul(local[j][0], first), mul(local[j][j], second))
    result = list(intermediate)
    for s in range(5):
        first, second = intermediate[5*s], intermediate[5*s + j]
        result[5*s] = add(mul(local[0][0], first), mul(local[0][j], second))
        result[5*s + j] = add(mul(local[j][0], first), mul(local[j][j], second))
    return result


def apply_word(state, word, echo):
    for pulse in word:
        if pulse is None:
            state = [mul(value, phase) for value, phase in zip(state, echo)]
        else:
            state = collective_carrier(state, pulse)
    return state


def triple_echo_word(c, j):
    x = embedded_word(c, j, 1, 1)
    y = embedded_word(c, j, 1, 0)
    # Exact frozen chronology: G, Vx^dagger, G, Vx, Vy^dagger, G, Vy.
    return [None, *inverse_word(x), None, *x, *inverse_word(y), None, *y]


def audit():
    require(mul(IMAG, IMAG) == neg(ONE), "i squared")
    require(mul(HALF_ROOT, HALF_ROOT) == scale(ONE, F(1, 2)), "sqrt-two field normalization")
    echo, echo_carriers = fixed_profile_echo()
    embedded_checks = 0
    for c in (1, 4):
        for j in range(5):
            if j == c:
                continue
            for phase in (0, 1):
                word = embedded_word(c, j, 1, phase)
                compiled = local_word(word)
                require(compiled == rotation(c, j, 1, phase), "embedded star compilation phase")
                require(product(adjoint(compiled), compiled) == identity(5), "embedded unitarity")
                require(local_word(inverse_word(word)) == adjoint(compiled), "embedded inverse")
                embedded_checks += 1

    block_columns = 0
    target_columns = 0
    contact_counts = {}
    for c in (1, 4):
        complete = []
        for j in range(5):
            if j == c:
                continue
            block = triple_echo_word(c, j)
            active = {c, j}
            for s in range(5):
                for q in range(5):
                    if s in active and q in active:
                        expected = [mul(neg(IMAG), value) for value in basis_vector(q, s)]
                    else:
                        phase = ONE if s == q else IMAG
                        expected = [mul(phase, value) for value in basis_vector(s, q)]
                    require(apply_word(basis_vector(s, q), block, echo) == expected,
                            "complete embedded triple-echo action")
                    block_columns += 1
            complete.extend(block)
        correction = [(j, 4, 0) for j in range(1, 5) if j != c]
        d_c = local_word(correction)
        require(d_c == [[(ONE if row == c else neg(ONE)) if row == col else ZERO
                         for col in range(5)] for row in range(5)], "D_c carrier phase correction")
        complete.extend(correction)
        for s in range(5):
            actual = apply_word(basis_vector(s, c), complete, echo)
            require(actual == basis_vector(c, s), "actual coherent contact column or phase failed")
            target_columns += 1
        echo_count = sum(pulse is None for pulse in complete)
        exterior_carriers = len(complete) - echo_count
        contact_counts[str(c)] = {
            "echo_blocks": echo_count,
            "raw_ls_loops": 20 * echo_count,
            "exterior_collective_star_carriers": exterior_carriers,
            "compiled_echo_collective_star_carriers": echo_count * echo_carriers,
        }
    require(embedded_checks == 16 and block_columns == 200 and target_columns == 10,
            "declared exact audit coverage")
    return {
        "status": "PASS",
        "arithmetic": "Q(i,sqrt(2)); exact Fraction coefficients",
        "affine_frames": 20,
        "echo_phase_entries": 25,
        "each_local_level_visits": 4,
        "off_diagonal_polynomial": "2*(5*sum(d_j^2)-(sum(d_j))^2)",
        "echo_unequal_phase": "-i",
        "echo_frame_collective_star_carriers": echo_carriers,
        "embedded_rotation_checks": embedded_checks,
        "complete_triple_echo_columns": block_columns,
        "actual_contact_columns": target_columns,
        "contact_counts": contact_counts,
        "input_independent_echo_global_phase_factored": True,
        "full_25_input_swap_claim": False,
        "physical_calibration": "NOT_PROVIDED",
    }


if __name__ == "__main__":
    sys.stdout.buffer.write((json.dumps(audit(), sort_keys=True, separators=(",", ":")) + "\n")
                            .encode("utf-8"))
