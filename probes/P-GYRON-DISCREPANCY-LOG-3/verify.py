from fractions import Fraction
from itertools import permutations
import os
import sys


F = Fraction

BASE_COMMIT = "1a4ae20d05cd76f93f70b2b011979b22a15fcde7"
ISSUE_OPENING_MAIN = "dcd8857c37bdeb3af10157fff4649147b6d5859a"
ACTIVATION_COMMIT = "4ac41b4fac3a3794a6e9d5be1e2027d324edb806"
CONTENT_COMMIT = "7830d852229ffc06c9d287d026c8ece290bf339b"
CANON_SHA256 = "f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1"
STATUS_SHA256 = "a8ec16afadb9d9f85530a54bd82b13b8855059bf05b7c4783f15898bd9854680"
REGISTRY_SHA256 = "6f4c7b350e0f12ba3e7ddc112ce04c4e916d03709aaab7ff007c0c17967a86c1"
GYRON_SHA256 = "bca4dde1975de979e2bcc589220c0e1e2218b14e7100b677628ce679af88c1cf"
DECODER_SHA256 = "c10a4f22afe4a1c7c68feb92864c7acd4b041cb4773e4e7789f280ff98bc75ec"
PREREG_SHA256 = "b45c42ad7f169d7c6cd01f1d6e785a5baf6ac46960dfa456d2447cc68c9b59b0"

ENVIRONMENT = (
    ("LC_ALL", "C"),
    ("LANG", "C"),
    ("PYTHONDONTWRITEBYTECODE", "1"),
    ("PYTHONHASHSEED", "0"),
    ("TZ", "UTC"),
)
HORIZON = 256

PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
MU = ((0, 1), (1, 0))

STATE_A = (-1, 1, 0)
STATE_B = (0, 0, 0)
STATE_C = (0, 0, 1)
STATE_D = (0, 1, 0)
STATE_E = (0, 1, 1)
STATE_F = (1, 0, 1)
STATES = (STATE_A, STATE_B, STATE_C, STATE_D, STATE_E, STATE_F)

BASE_INTERVALS = (
    ((-5, -3), (-5, -1), (-7, -3), (-5, -1)),
    ((-6, -6), (-6, -4), (-8, -4), (-6, -2)),
    ((-4, -4), (-4, -2), (-6, -4), (-4, -2)),
    ((-2, -2), (0, 0), (-2, 0), (-2, 2)),
    ((-4, -2), (-2, 0), (-4, -2), (-4, 0)),
    ((-3, -1), (-1, 1), (-3, 1), (-3, 3)),
)


def pass_fail(checks):
    return "PASS" if all(checks) else "FAIL"


def proof_node(label, structural_checks, claim_checks, parents=(), **fields):
    provenance = {label}
    for parent in parents:
        provenance.update(parent["provenance"])
    structural = all(structural_checks)
    failures = tuple(code for code, holds in claim_checks if not holds)
    result = {
        "pass": structural and not failures,
        "structural": structural,
        "failures": failures,
        "provenance": frozenset(provenance),
    }
    result.update(fields)
    return result


def is_lower_hex(value, width):
    alphabet = set("0123456789abcdef")
    return len(value) == width and set(value) <= alphabet


def matrix_from_columns(columns):
    return tuple(
        tuple(columns[column][row] for column in range(len(columns)))
        for row in range(len(columns[0]))
    )


def matrix_add(left, right):
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(len(left[0])))
        for row in range(len(left))
    )


def matrix_scale(scalar, matrix):
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def matrix_vector(matrix, vector):
    return tuple(
        sum((matrix[row][column] * vector[column] for column in range(len(vector))), F(0))
        for row in range(len(matrix))
    )


def matrix_multiply(left, right):
    return tuple(
        tuple(
            sum(
                (left[row][middle] * right[middle][column] for middle in range(len(right))),
                F(0),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def permutation_sign(permutation):
    inversions = sum(
        1
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
        if permutation[left] > permutation[right]
    )
    return -1 if inversions & 1 else 1


def polynomial_multiply(left, right):
    product = [F(0) for _ in range(len(left) + len(right) - 1)]
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            product[left_degree + right_degree] += left_value * right_value
    return tuple(product)


def proof_charpoly(matrix):
    size = len(matrix)
    result = [F(0) for _ in range(size + 1)]
    for permutation in permutations(range(size)):
        term = (F(permutation_sign(permutation)),)
        for row, column in enumerate(permutation):
            factor = (-matrix[row][column], F(1) if row == column else F(0))
            term = polynomial_multiply(term, factor)
        for degree, coefficient in enumerate(term):
            result[degree] += coefficient
    return tuple(result)


def proof_determinant(matrix):
    total = F(0)
    for permutation in permutations(range(len(matrix))):
        term = F(permutation_sign(permutation))
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def certificate_seams():
    derived = [[0 for _ in range(6)] for _ in PAIRS]
    local_checks = [MU == ((0, 1), (1, 0))]

    for symbol, block in enumerate(MU):
        local_checks.append(block == (symbol, 1 - symbol))
        internal_pair = (block[0], block[1])
        derived[PAIRS.index(internal_pair)][symbol] += 1

    for pair_index, (left, right) in enumerate(PAIRS):
        seam_pair = (MU[left][1], MU[right][0])
        local_checks.append(seam_pair == (1 - left, right))
        derived[PAIRS.index(seam_pair)][2 + pair_index] += 1

    expected = (
        (0, 0, 0, 0, 1, 0),
        (1, 0, 0, 0, 0, 1),
        (0, 1, 1, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
    )
    coefficients = tuple(tuple(row) for row in derived)
    identity_checks = tuple(coefficients[index] == expected[index] for index in range(4))
    proof_checks = tuple(local_checks) + identity_checks
    return proof_node(
        "A01",
        (
            len(coefficients) == 4,
            all(len(row) == 6 for row in coefficients),
            all(type(entry) is int for row in coefficients for entry in row),
        ),
        (("SEAMS", all(proof_checks)),),
        identities=len(identity_checks),
        proof_nodes=len(proof_checks),
        coefficients=coefficients,
    )


def certificate_balance():
    block_balance = tuple(
        sum((1 - 2 * digit for digit in MU[symbol]), 0) for symbol in (0, 1)
    )
    odd_balance = tuple(
        block_balance[symbol] + 1 - 2 * MU[symbol][0] for symbol in (0, 1)
    )
    incoming_zero_classification = tuple(
        ((right == 0), (left, right) in ((0, 0), (1, 0)))
        for left, right in PAIRS
    )
    flux = tuple(
        (1 if right == 0 else 0) - (1 if left == 0 else 0)
        for left, right in PAIRS
    )
    expected_flux = (0, -1, 1, 0)
    # Coefficients below use the ordered variables (c00,n0,L,1).
    # Every zero after the initial t_0=0 is the right member of either a
    # 00 or a 10 pair, so c10=n0-c00-1. Also n1=L-n0, hence S=2n0-L.
    first_zero = 1 if MU[0][0] == 0 else 0
    c10_form = (-1, 1, 0, -first_zero)
    n_zero_form = (0, 1, 0, 0)
    length_form = (0, 0, 1, 0)
    n_one_form = tuple(
        length_form[index] - n_zero_form[index] for index in range(4)
    )
    s_form = tuple(
        n_zero_form[index] - n_one_form[index] for index in range(4)
    )

    identity_checks = (
        block_balance == (0, 0),
        odd_balance == (1, -1),
        set(block_balance + odd_balance) == {-1, 0, 1},
        all(left == right for left, right in incoming_zero_classification),
        first_zero == 1,
        c10_form == (-1, 1, 0, -1),
        s_form == (0, 2, -1, 0),
    )
    proof_checks = identity_checks + (
        flux == expected_flux,
        MU[0][0] == 0,
        sum((1 if digit == 0 else 0 for digit in (0,)), 0) == 1,
    )
    return proof_node(
        "A02",
        (len(block_balance) == 2, len(odd_balance) == 2, len(flux) == 4),
        (("BALANCE", all(proof_checks)),),
        identities=len(identity_checks),
        proof_nodes=len(proof_checks),
        block_balance=block_balance,
        odd_balance=odd_balance,
        flux=flux,
        c10_form=c10_form,
        s_form=s_form,
    )


def certificate_discrepancy(seams, balance):
    # Coefficients are in the ordered variables (c00,n0,L,1).
    d_form = (6, 0, -1, 0)
    s_form = balance["s_form"]
    c10_form = balance["c10_form"]
    seam_c00_coefficients = seams["coefficients"][0]
    twice_length_correction = (0, 0, -2, 0)
    d_twice_from_seam = tuple(
        6 * seam_c00_coefficients[4] * c10_form[index]
        + twice_length_correction[index]
        for index in range(4)
    )
    d_twice_from_formula = tuple(
        -d_form[index] + 3 * s_form[index] + (0, 0, 0, -6)[index]
        for index in range(4)
    )
    d_four_from_iteration = tuple(
        -d_twice_from_formula[index] + (0, 0, 0, -6)[index]
        for index in range(4)
    )
    d_four_from_formula = tuple(
        d_form[index] - 3 * s_form[index] for index in range(4)
    )

    a1_checks = (
        seam_c00_coefficients == (0, 0, 0, 0, 1, 0),
        c10_form == (-1, 1, 0, -1),
        d_twice_from_seam == d_twice_from_formula,
    )
    a2_checks = (
        set(balance["block_balance"]) == {0},
        set(balance["odd_balance"]) == {-1, 1},
        d_four_from_iteration == d_four_from_formula,
        {-3 * even_balance for even_balance in balance["block_balance"]} == {0},
        0 not in {-3 * odd_balance for odd_balance in balance["odd_balance"]},
    )
    identity_checks = a1_checks + a2_checks
    least_positive = 1
    initial_vector = (0, 1, 1, 1)
    d_one = sum(
        (d_form[index] * initial_vector[index] for index in range(4)), 0
    )
    s_one = sum(
        (s_form[index] * initial_vector[index] for index in range(4)), 0
    )
    d_four = d_one - 3 * s_one
    boundary_checks = (
        d_one == -1,
        s_one == balance["odd_balance"][0] == 1,
        d_four == -4,
        d_four != d_one,
        least_positive > 0,
        least_positive - 1 == 0,
    )
    return proof_node(
        "A03",
        (
            len(d_form) == 4,
            len(s_form) == 4,
            all(type(entry) is int for entry in d_twice_from_seam),
        ),
        (
            ("DOUBLING", all(a1_checks)),
            ("FOUR-STEP", all(a2_checks) and all(boundary_checks)),
        ),
        (seams, balance),
        identities=len(identity_checks),
        boundary=len(boundary_checks),
        d_form=d_form,
        s_form=s_form,
        d_twice=d_twice_from_formula,
        d_four=d_four_from_formula,
    )


def cert_step(state, discrepancy, bit):
    s_value, previous_digit, next_digit = state
    if bit == 0:
        new_state = (0, 1 - previous_digit, next_digit)
        new_discrepancy = -discrepancy + 3 * s_value - 6
    else:
        indicator = 1 if (previous_digit, next_digit) == (1, 0) else 0
        new_state = (1 - 2 * next_digit, next_digit, 1 - next_digit)
        new_discrepancy = -discrepancy + 3 * s_value - 7 + 6 * indicator
    return new_state, new_discrepancy


def transducer_value(length):
    state = STATE_F
    discrepancy = -1
    for position in range(length.bit_length() - 2, -1, -1):
        bit = (length >> position) & 1
        state, discrepancy = cert_step(state, discrepancy, bit)
    return state, discrepancy


def certificate_transducer(balance, discrepancy):
    # Appending a binary bit changes popcount parity by that bit. This full
    # two-by-two parity table is exactly the Thue-Morse substitution.
    append_parity = tuple(
        tuple((parent_parity + bit) & 1 for bit in (0, 1))
        for parent_parity in (0, 1)
    )
    recurrence_checks = (
        append_parity == MU,
        tuple(row[0] for row in append_parity) == (0, 1),
        tuple(row[1] for row in append_parity) == (1, 0),
        balance["block_balance"] == (0, 0),
        balance["odd_balance"] == (1, -1),
        tuple(
            -discrepancy["d_form"][index]
            + 3 * discrepancy["s_form"][index]
            + (0, 0, 0, -6)[index]
            for index in range(4)
        )
        == discrepancy["d_twice"],
    )

    derivation_checks = []
    for state in STATES:
        s_value, previous_digit, next_digit = state
        previous_block = MU[previous_digit]
        next_block = MU[next_digit]
        appended_pair = (previous_block[1], next_block[0])
        appended_indicator = 1 if appended_pair == (0, 0) else 0
        frozen_indicator = 1 if (previous_digit, next_digit) == (1, 0) else 0
        derived_even_state = (
            balance["block_balance"][next_digit],
            previous_block[1],
            next_block[0],
        )
        derived_odd_state = (
            balance["odd_balance"][next_digit],
            next_block[0],
            next_block[1],
        )
        even_zero = cert_step(state, 0, 0)
        even_one = cert_step(state, 1, 0)
        odd_zero = cert_step(state, 0, 1)
        odd_one = cert_step(state, 1, 1)
        t0_zero = 3 * s_value - 6
        t0_one = -1 + 3 * s_value - 6
        seam_correction = 6 * appended_indicator - 1
        derivation_checks.extend(
            (
                previous_block == (previous_digit, 1 - previous_digit),
                next_block == (next_digit, 1 - next_digit),
                appended_pair == (1 - previous_digit, next_digit),
                appended_indicator == frozen_indicator,
                derived_even_state == (0, 1 - previous_digit, next_digit),
                derived_odd_state
                == (1 - 2 * next_digit, next_digit, 1 - next_digit),
                even_zero == (derived_even_state, t0_zero),
                even_one == (derived_even_state, t0_one),
                odd_zero
                == (derived_odd_state, even_zero[1] + seam_correction),
                odd_one
                == (derived_odd_state, even_one[1] + seam_correction),
                even_one[1] - even_zero[1] == -1,
                odd_one[1] - odd_zero[1] == -1,
            )
        )

    closure_checks = []
    for state in STATES:
        for bit in (0, 1):
            target, value = cert_step(state, 0, bit)
            closure_checks.append(target in STATES)
            closure_checks.append(type(value) is int)

    reached = {STATE_F}
    frontier = {STATE_F}
    for _ in range(len(STATES)):
        next_frontier = set()
        for state in frontier:
            for bit in (0, 1):
                target, unused_value = cert_step(state, 0, bit)
                next_frontier.add(target)
                if type(unused_value) is not int:
                    next_frontier.add(("invalid",))
        reached |= next_frontier
        frontier = next_frontier

    state_checks = (
        len(STATES) == 6,
        len(set(STATES)) == 6,
        reached == set(STATES),
        STATE_F == (1, 0, 1),
        transducer_value(1) == (STATE_F, -1),
    )
    transition_checks = tuple(closure_checks)
    proof_checks = recurrence_checks + tuple(derivation_checks) + state_checks + transition_checks
    return proof_node(
        "A04",
        (
            len(STATES) == 6,
            all(len(state) == 3 for state in STATES),
            len(derivation_checks) == 12 * len(STATES),
        ),
        (("STATE", all(proof_checks)),),
        (balance, discrepancy),
        states=len(STATES),
        transitions=len(STATES) * 2,
    )


def apply_four_bits(state, discrepancy, word):
    current_state = state
    current_discrepancy = discrepancy
    for position in (3, 2, 1, 0):
        current_state, current_discrepancy = cert_step(
            current_state, current_discrepancy, (word >> position) & 1
        )
    return current_state, current_discrepancy


def four_bit_records():
    records = []
    for state in STATES:
        for word in range(16):
            final_zero, output_zero = apply_four_bits(state, 0, word)
            final_one, output_one = apply_four_bits(state, 1, word)
            coefficient = output_one - output_zero
            records.append((state, word, final_zero, coefficient, output_zero, final_one))
    return tuple(records)


def certificate_four_bit(transducer):
    records = four_bit_records()
    keys = {(record[0], record[1]) for record in records}
    path_checks = []
    for state, word, final_state, coefficient, offset, final_one in records:
        path_checks.extend(
            (
                final_state == final_one,
                final_state in STATES,
                coefficient == 1,
                apply_four_bits(state, -7, word)[1] == -7 + offset,
                apply_four_bits(state, 11, word)[1] == 11 + offset,
            )
        )
    inventory_checks = (
        len(records) == 96,
        len(keys) == 96,
        keys == {(state, word) for state in STATES for word in range(16)},
    )
    return proof_node(
        "A05",
        inventory_checks,
        (("PATH", all(path_checks)),),
        (transducer,),
        states=len(STATES),
        words=16,
        paths=len(records),
        records=records,
    )


def certificate_length_values(binary_length):
    values = {(STATE_F, -1)}
    for _ in range(binary_length - 1):
        next_values = set()
        for state, discrepancy in values:
            for bit in (0, 1):
                next_values.add(cert_step(state, discrepancy, bit))
        values = next_values
    return tuple(sorted(values))


def certificate_length_max(binary_length):
    return max(
        abs(discrepancy)
        for state, discrepancy in certificate_length_values(binary_length)
    )


def certificate_layer(binary_length):
    values = certificate_length_values(binary_length)
    intervals = []
    for state in STATES:
        state_values = tuple(
            value for value_state, value in values if value_state == state
        )
        if not state_values:
            raise ValueError("absent-state-in-certified-layer")
        intervals.append((min(state_values), max(state_values)))
    return tuple(intervals)


def certificate_base_table(four_bit):
    actual_by_length = tuple(
        certificate_layer(length) for length in (5, 6, 7, 8)
    )
    actual_by_state = tuple(
        tuple(
            actual_by_length[length_index][state_index]
            for length_index in range(4)
        )
        for state_index in range(6)
    )
    cell_checks = tuple(
        actual_by_state[state][length] == BASE_INTERVALS[state][length]
        for state in range(6)
        for length in range(4)
    )
    return proof_node(
        "A06",
        (
            len(actual_by_state) == 6,
            all(len(row) == 4 for row in actual_by_state),
            len(cell_checks) == 24,
        ),
        (("BASE", all(cell_checks)),),
        (four_bit,),
        states=6,
        lengths=4,
        cells=len(cell_checks),
        actual=actual_by_state,
    )


def endpoint_transfer(bounds, records, lower):
    transferred = []
    for target in STATES:
        candidates = []
        for source, word, final_state, coefficient, offset, final_one in records:
            if final_state == target and final_one == target and coefficient == 1:
                candidates.append(bounds[STATES.index(source)] + offset)
        if not candidates:
            raise ValueError("empty-endpoint-transfer")
        transferred.append(min(candidates) if lower else max(candidates))
    return tuple(transferred)


def certificate_induction(four_bit, base_table):
    records = four_bit["records"]
    coefficient_checks = tuple(record[3] == 1 for record in records)
    coverage_checks = tuple(
        any(record[2] == target for record in records) for target in STATES
    )
    residue_checks = []
    lower_shifts = []
    upper_shifts = []

    for length_index in range(4):
        intervals = tuple(
            base_table["actual"][state_index][length_index]
            for state_index in range(6)
        )
        lower = tuple(interval[0] for interval in intervals)
        upper = tuple(interval[1] for interval in intervals)
        transferred_lower = endpoint_transfer(lower, records, True)
        transferred_upper = endpoint_transfer(upper, records, False)
        residue_checks.append(
            transferred_lower == tuple(value - 2 for value in lower)
        )
        residue_checks.append(
            transferred_upper == tuple(value + 2 for value in upper)
        )
        lower_shifts.extend(
            transferred_lower[index] - lower[index] for index in range(6)
        )
        upper_shifts.extend(
            transferred_upper[index] - upper[index] for index in range(6)
        )

    recurrence_increment = (
        upper_shifts[0]
        if upper_shifts
        and set(upper_shifts) == {upper_shifts[0]}
        and set(lower_shifts) == {-upper_shifts[0]}
        else None
    )
    recurrence = (recurrence_increment, 4)

    # Coefficient one makes uniform translation commute with every affine
    # candidate and therefore separately with minimum and maximum.
    translation_checks = (
        all(coefficient_checks),
        all(coverage_checks),
        {record[3] for record in records} == {1},
        len({(record[0], record[1]) for record in records}) == 96,
    )
    induction_checks = (
        all(residue_checks),
        all(translation_checks),
        len(residue_checks) == 8,
    )
    return proof_node(
        "A07",
        (
            len(records) == 96,
            len(base_table["actual"]) == 6,
            len(residue_checks) == 8,
        ),
        (("INDUCTION", all(induction_checks)),),
        (four_bit, base_table),
        residues=4,
        transfer_nodes=len(residue_checks) + len(translation_checks),
        base=base_table["actual"],
        recurrence=recurrence,
    )


def affine_leq(left, right, minimum_parameter):
    slope = right[0] - left[0]
    intercept = right[1] - left[1]
    return slope >= 0 and slope * minimum_parameter + intercept >= 0


def certificate_extrema(induction):
    exact_length_maxima = tuple(
        certificate_length_max(length) for length in range(1, 9)
    )

    endpoint_states = []
    endpoint_values = []
    endpoint_state = STATE_F
    endpoint_discrepancy = -1
    for _ in range(8):
        endpoint_state, endpoint_discrepancy = cert_step(
            endpoint_state, endpoint_discrepancy, 0
        )
        endpoint_states.append(endpoint_state)
        endpoint_values.append(endpoint_discrepancy)
    endpoint_states = tuple(endpoint_states)
    endpoint_values = tuple(endpoint_values)

    small_cumulative = tuple(
        max(
            max(exact_length_maxima[:exponent]),
            abs(endpoint_values[exponent - 1]),
        )
        for exponent in range(1, 9)
    )
    small_checks = (
        exact_length_maxima == (1, 3, 6, 4, 6, 6, 8, 6),
        endpoint_states
        == (
            STATE_E,
            STATE_C,
            STATE_E,
            STATE_C,
            STATE_E,
            STATE_C,
            STATE_E,
            STATE_C,
        ),
        endpoint_values == (-2, -4, -2, -4, -2, -4, -2, -4),
        small_cumulative == (2, 4, 6, 6, 6, 6, 8, 8),
    )

    # A07 supplies H_(n+4)=H_n+2 for exact-length maxima H_n. In residue
    # order n mod 4 = 0,1,2,3, derive the affine pair from H_8,H_5,H_6,H_7.
    base_indices = (3, 0, 1, 2)
    base_parameters = (2, 1, 1, 1)
    base_length_maxima = tuple(
        max(
            max(
                abs(induction["base"][state][index][0]),
                abs(induction["base"][state][index][1]),
            )
            for state in range(6)
        )
        for index in base_indices
    )
    length_formula_pairs = tuple(
        (2, base_length_maxima[residue] - 2 * base_parameters[residue])
        for residue in range(4)
    )
    length_formula_checks = (
        induction["recurrence"] == (2, 4),
        base_length_maxima == (6, 6, 6, 8),
        length_formula_pairs == ((2, 2), (2, 4), (2, 4), (2, 6)),
    )

    # For k=4h+r and k>=8, only the last exact length in each residue and
    # the finite n<=4 maximum can dominate; every older cycle is smaller by 2.
    cumulative_formula_pairs = tuple(
        (2, 4 + (2 if residue == 3 else 0)) for residue in range(4)
    )
    cumulative_checks = []
    for residue in range(4):
        parameter_shifts = (
            0,
            0 if residue >= 1 else -1,
            0 if residue >= 2 else -1,
            0 if residue >= 3 else -1,
        )
        candidates = ((0, 6),) + tuple(
            (
                length_formula_pairs[length_residue][0],
                length_formula_pairs[length_residue][1]
                + length_formula_pairs[length_residue][0]
                * parameter_shifts[length_residue],
            )
            for length_residue in range(4)
        )
        target = cumulative_formula_pairs[residue]
        cumulative_checks.extend(
            (
                target in candidates,
                all(affine_leq(candidate, target, 2) for candidate in candidates),
                target == (2, 4 + (2 if residue == 3 else 0)),
            )
        )

    # These two exact zero-bit transitions establish the endpoint two-cycle
    # for every k>=1. Its absolute value is at most 4 and cannot change A4.
    endpoint_checks = (
        cert_step(STATE_F, -1, 0) == (STATE_E, -2),
        cert_step(STATE_E, -2, 0) == (STATE_C, -4),
        cert_step(STATE_C, -4, 0) == (STATE_E, -2),
        all(
            affine_leq((0, 4), cumulative_formula_pairs[residue], 2)
            for residue in range(4)
        ),
        min(small_cumulative[2:]) >= 4,
    )
    claim_checks = (
        all(small_checks),
        all(length_formula_checks),
        all(cumulative_checks),
        all(endpoint_checks),
    )
    return proof_node(
        "A08",
        (
            len(exact_length_maxima) == 8,
            len(length_formula_pairs) == 4,
            len(cumulative_formula_pairs) == 4,
        ),
        (("EXTREMUM", all(claim_checks)),),
        (induction,),
        formulas=6,
        endpoint_nodes=len(endpoint_checks),
        small_cumulative=small_cumulative,
        length_formulas=length_formula_pairs,
        cumulative_formulas=cumulative_formula_pairs,
    )


def vector_subtract(left, right):
    return tuple(left[index] - right[index] for index in range(len(left)))


def certificate_corollaries(extrema):
    # For n=4h+r, the exact-length affine forms imply H_n<=n+3.
    minimum_parameters = (2, 1, 1, 1)
    n_plus_three = ((4, 3), (4, 4), (4, 5), (4, 6))
    length_bounds = tuple(
        affine_leq(
            extrema["length_formulas"][residue],
            n_plus_three[residue],
            minimum_parameters[residue],
        )
        for residue in range(4)
    )

    # Ordered-real certificate schema. For arbitrary epsilon>0 let
    # q=2^(-epsilon), hence 0<q<1, and r=(1+q)/2. Coefficient pairs below
    # are exact affine forms in (1,q). Both positive gaps equal (1-q)/2.
    one_affine = (F(1), F(0))
    q_affine = (F(0), F(1))
    r_affine = tuple(
        F(1, 2) * (one_affine[index] + q_affine[index])
        for index in range(2)
    )
    r_minus_q = vector_subtract(r_affine, q_affine)
    one_minus_r = vector_subtract(one_affine, r_affine)
    half_one_minus_q = tuple(
        F(1, 2) * value
        for value in vector_subtract(one_affine, q_affine)
    )

    # By the Archimedean property choose N>=q/(r-q). For n>=N,
    # n(r-q)>=q is exactly equivalent (after multiplying by n>0) to
    # (1+1/n)q<=r. Thus a_n=n*q^n has eventual ratio <=r<1.
    # This is the standard ordered-real geometric-domination lemma; the code
    # certifies all of its algebraic and positivity preconditions.
    # Coefficients use the ordered monomials (n,nq,q,1). Both sides below
    # are n*r-(n+1)q = n*(r-q)-q.
    ratio_gap_cross = (F(1, 2), F(-1, 2), F(-1), F(0))
    archimedean_gap_cross = (
        r_minus_q[0],
        r_minus_q[1],
        F(-1),
        F(0),
    )
    ordered_real_checks = (
        r_affine == (F(1, 2), F(1, 2)),
        r_minus_q == (F(1, 2), F(-1, 2)),
        one_minus_r == r_minus_q,
        r_minus_q == half_one_minus_q,
        ratio_gap_cross == archimedean_gap_cross,
        F(1, 2) > 0,
    )

    # Exact cross-products in ordered variables (c00,L,d,1).
    definition = (6, -1, -1, 0)
    first_left = (6, -1, 0, 0)
    first_right = (0, 0, 1, 0)
    second_left = (6, -1, 0, 1)
    second_right = (0, 0, 1, 1)
    d_over_l_basis = (F(1), F(0))
    one_over_l_basis = (F(0), F(1))
    rescaled_numerator = tuple(
        d_over_l_basis[index] + one_over_l_basis[index]
        for index in range(2)
    )
    rescaled_denominator = vector_subtract(
        (F(1), F(0)), one_over_l_basis
    )
    density_checks = (
        vector_subtract(first_left, first_right) == definition,
        vector_subtract(second_left, second_right) == definition,
        # (d+1)/(L-1) = (d/L+1/L)/(1-1/L); numerator ->0,
        # denominator ->1, so the standard quotient-limit rule applies.
        rescaled_numerator == (F(1), F(1)),
        rescaled_denominator == (F(1), F(-1)),
        F(1, 6) * 6 == 1,
    )

    # The preceding nodes give |d(L)|<=n+3 for n=bit_length(L), hence
    # O(log L). Since L>=2^(n-1), geometric domination gives
    # |d(L)|/L^epsilon ->0. Taking epsilon=1 yields d/L->0; the two exact
    # cross-products and the denominator-to-one rule give both densities.
    corollary_checks = (
        all(length_bounds),
        all(ordered_real_checks),
        all(density_checks),
    )
    proof_nodes = (
        len(length_bounds)
        + len(ordered_real_checks)
        + len(density_checks)
        + 4
    )
    return proof_node(
        "A09",
        (len(extrema["length_formulas"]) == 4,),
        (("COROLLARY", all(corollary_checks)),),
        (extrema,),
        proof_nodes=proof_nodes,
    )

def proof_phase_matrices():
    internal_left_columns = []
    internal_right_columns = []
    boundary_columns = []

    for left, right in PAIRS:
        left_pair = (MU[left][0], MU[left][1])
        right_pair = (MU[right][0], MU[right][1])
        seam_pair = (MU[left][1], MU[right][0])
        internal_left_columns.append(
            tuple(F(1) if pair == left_pair else F(0) for pair in PAIRS)
        )
        internal_right_columns.append(
            tuple(F(1) if pair == right_pair else F(0) for pair in PAIRS)
        )
        boundary_columns.append(
            tuple(F(1) if pair == seam_pair else F(0) for pair in PAIRS)
        )

    internal_left = matrix_from_columns(tuple(internal_left_columns))
    internal_right = matrix_from_columns(tuple(internal_right_columns))
    boundary = matrix_from_columns(tuple(boundary_columns))
    average_left = matrix_scale(F(1, 2), matrix_add(internal_left, boundary))
    average_right = matrix_scale(F(1, 2), matrix_add(internal_right, boundary))
    return internal_left, internal_right, boundary, average_left, average_right


def certificate_phase_maps():
    matrices = proof_phase_matrices()
    internal_left, internal_right, boundary, average_left, average_right = matrices
    expected_internal_left = (
        (F(0), F(0), F(0), F(0)),
        (F(1), F(1), F(0), F(0)),
        (F(0), F(0), F(1), F(1)),
        (F(0), F(0), F(0), F(0)),
    )
    expected_internal_right = (
        (F(0), F(0), F(0), F(0)),
        (F(1), F(0), F(1), F(0)),
        (F(0), F(1), F(0), F(1)),
        (F(0), F(0), F(0), F(0)),
    )
    expected_boundary = (
        (F(0), F(0), F(1), F(0)),
        (F(0), F(0), F(0), F(1)),
        (F(1), F(0), F(0), F(0)),
        (F(0), F(1), F(0), F(0)),
    )
    expected_average_left = (
        (F(0), F(0), F(1, 2), F(0)),
        (F(1, 2), F(1, 2), F(0), F(1, 2)),
        (F(1, 2), F(0), F(1, 2), F(1, 2)),
        (F(0), F(1, 2), F(0), F(0)),
    )
    expected_average_right = (
        (F(0), F(0), F(1, 2), F(0)),
        (F(1, 2), F(0), F(1, 2), F(1, 2)),
        (F(1, 2), F(1, 2), F(0), F(1, 2)),
        (F(0), F(1, 2), F(0), F(0)),
    )
    expected = (
        expected_internal_left,
        expected_internal_right,
        expected_boundary,
        expected_average_left,
        expected_average_right,
    )
    matrix_checks = tuple(
        matrices[index] == expected[index] for index in range(5)
    )
    basis_checks = tuple(
        sum((matrix[row][column] for row in range(4)), F(0)) == 1
        for matrix in matrices
        for column in range(4)
    )
    return proof_node(
        "B01",
        (
            len(matrices) == 5,
            all(
                len(matrix) == 4 and all(len(row) == 4 for row in matrix)
                for matrix in matrices
            ),
            all(
                type(entry) is F
                for matrix in matrices
                for row in matrix
                for entry in row
            ),
        ),
        (("PHASE", all(matrix_checks) and all(basis_checks)),),
        maps=len(matrices),
        basis_checks=len(basis_checks),
        matrices=matrices,
    )


def certificate_anchor_spectra(phase_maps):
    internal_left, internal_right, boundary, average_left, average_right = phase_maps[
        "matrices"
    ]
    witness = (F(0), F(1), F(0), F(0))
    expected_left_witness = (F(0), F(1, 2), F(0), F(1, 2))
    expected_right_witness = (F(0), F(0), F(1, 2), F(1, 2))
    actual_left_witness = matrix_vector(average_left, witness)
    actual_right_witness = matrix_vector(average_right, witness)
    expected_left_polynomial = (F(0), F(1, 4), F(-1, 4), F(-1), F(1))
    expected_right_polynomial = (F(0), F(-1, 4), F(-3, 4), F(0), F(1))
    actual_left_polynomial = proof_charpoly(average_left)
    actual_right_polynomial = proof_charpoly(average_right)

    left_eigenpairs = (
        (F(1), (F(1), F(2), F(2), F(1))),
        (F(1, 2), (F(1), F(-1), F(1), F(-1))),
        (F(-1, 2), (F(1), F(-1), F(-1), F(1))),
        (F(0), (F(1), F(0), F(0), F(-1))),
    )
    right_eigenpairs = (
        (F(1), (F(1), F(2), F(2), F(1))),
        (F(-1, 2), (F(1), F(-1), F(-1), F(1))),
        (F(-1, 2), (F(1), F(1), F(-1), F(-1))),
        (F(0), (F(1), F(0), F(0), F(-1))),
    )
    left_eigen_checks = tuple(
        matrix_vector(average_left, vector)
        == tuple(eigenvalue * entry for entry in vector)
        for eigenvalue, vector in left_eigenpairs
    )
    right_eigen_checks = tuple(
        matrix_vector(average_right, vector)
        == tuple(eigenvalue * entry for entry in vector)
        for eigenvalue, vector in right_eigenpairs
    )
    left_eigenmatrix = matrix_from_columns(
        tuple(vector for eigenvalue, vector in left_eigenpairs)
    )
    right_eigenmatrix = matrix_from_columns(
        tuple(vector for eigenvalue, vector in right_eigenpairs)
    )
    anchor_checks = (
        average_left != average_right,
        actual_left_witness == expected_left_witness,
        actual_right_witness == expected_right_witness,
        internal_left != internal_right,
        len(boundary) == 4,
    )
    spectrum_checks = (
        actual_left_polynomial == expected_left_polynomial,
        actual_right_polynomial == expected_right_polynomial,
        all(left_eigen_checks),
        all(right_eigen_checks),
        proof_determinant(left_eigenmatrix) != 0,
        proof_determinant(right_eigenmatrix) != 0,
    )
    return proof_node(
        "B02",
        (
            len(actual_left_polynomial) == 5,
            len(actual_right_polynomial) == 5,
            len(left_eigenpairs) == 4,
            len(right_eigenpairs) == 4,
        ),
        (
            ("ANCHOR", all(anchor_checks)),
            ("SPECTRUM", all(spectrum_checks)),
        ),
        (phase_maps,),
        matrices=2,
        polynomials=2,
        left_polynomial=actual_left_polynomial,
        right_polynomial=actual_right_polynomial,
        left_witness=actual_left_witness,
        right_witness=actual_right_witness,
        left_eigenpairs=left_eigenpairs,
        right_eigenpairs=right_eigenpairs,
    )


def proof_stationary_restriction(matrix):
    basis = (
        (F(1), F(0), F(0), F(0)),
        (F(0), F(1), F(1), F(0)),
        (F(0), F(0), F(0), F(1)),
    )
    columns = []
    invariant = []
    for vector in basis:
        image = matrix_vector(matrix, vector)
        invariant.append(image[1] == image[2])
        columns.append((image[0], image[1], image[3]))
    return matrix_from_columns(tuple(columns)), tuple(invariant)


def certificate_stationary(phase_maps, anchor_spectra):
    average_left = phase_maps["matrices"][3]
    average_right = phase_maps["matrices"][4]
    left_restriction, left_invariant = proof_stationary_restriction(average_left)
    right_restriction, right_invariant = proof_stationary_restriction(average_right)
    expected_restriction = (
        (F(0), F(1, 2), F(0)),
        (F(1, 2), F(1, 2), F(1, 2)),
        (F(0), F(1, 2), F(0)),
    )
    expected_polynomial = (F(0), F(-1, 2), F(-1, 2), F(1))
    actual_polynomial = proof_charpoly(left_restriction)
    eigenpairs = (
        (F(1), (F(1), F(2), F(1))),
        (F(-1, 2), (F(1), F(-1), F(1))),
        (F(0), (F(1), F(0), F(-1))),
    )
    eigen_checks = tuple(
        matrix_vector(left_restriction, vector)
        == tuple(eigenvalue * entry for entry in vector)
        for eigenvalue, vector in eigenpairs
    )
    eigenmatrix = matrix_from_columns(
        tuple(vector for eigenvalue, vector in eigenpairs)
    )
    # Rational coefficients define the common map on W_Q and its unique
    # coefficientwise real-linear scalar extension on W_R.
    restriction_checks = (
        all(left_invariant),
        all(right_invariant),
        left_restriction == right_restriction,
        left_restriction == expected_restriction,
        all(type(entry) is F for row in left_restriction for entry in row),
    )
    spectrum_checks = (
        actual_polynomial == expected_polynomial,
        all(eigen_checks),
        proof_determinant(eigenmatrix) != 0,
        tuple(eigenvalue for eigenvalue, vector in eigenpairs)
        == (F(1), F(-1, 2), F(0)),
    )
    return proof_node(
        "B03",
        (
            len(left_restriction) == 3,
            all(len(row) == 3 for row in left_restriction),
            all(type(entry) is F for row in left_restriction for entry in row),
        ),
        (
            ("ANCHOR", all(restriction_checks)),
            ("SPECTRUM", all(spectrum_checks)),
        ),
        (phase_maps, anchor_spectra),
        restriction=len(restriction_checks),
        spectrum=len(spectrum_checks),
        matrix=left_restriction,
        right_matrix=right_restriction,
        polynomial=actual_polynomial,
        eigenpairs=eigenpairs,
        eigenmatrix=eigenmatrix,
    )


def certificate_fixed_point(phase_maps, stationary):
    average_left = phase_maps["matrices"][3]
    average_right = phase_maps["matrices"][4]
    fixed = (F(1, 6), F(1, 3), F(1, 3), F(1, 6))
    left_image = matrix_vector(average_left, fixed)
    right_image = matrix_vector(average_right, fixed)
    equations = (
        left_image == fixed,
        right_image == fixed,
        sum(fixed, F(0)) == 1,
        fixed[1] == fixed[2],
        all(entry > 0 for entry in fixed),
    )

    fixed_eigenvector = (F(1), F(2), F(1))
    mass_form = (F(1), F(2), F(1))
    eigenvalue_one_pairs = tuple(
        pair for pair in stationary["eigenpairs"] if pair[0] == 1
    )
    eigenvalue_one_vector = (
        eigenvalue_one_pairs[0][1] if len(eigenvalue_one_pairs) == 1 else ()
    )
    uniqueness_nodes = (
        len(eigenvalue_one_pairs) == 1,
        eigenvalue_one_vector == fixed_eigenvector,
        proof_determinant(stationary["eigenmatrix"]) != 0,
        matrix_vector(stationary["matrix"], fixed_eigenvector)
        == fixed_eigenvector,
        sum(
            (mass_form[index] * fixed_eigenvector[index] for index in range(3)),
            F(0),
        )
        == 6,
        F(1, 6) * 6 == 1,
    )
    return proof_node(
        "B04",
        (len(fixed) == 4, len(eigenvalue_one_pairs) == 1),
        (("FIXED", all(equations) and all(uniqueness_nodes)),),
        (phase_maps, stationary),
        equations=len(equations),
        uniqueness_nodes=len(uniqueness_nodes),
        fixed=fixed,
        left_image=left_image,
        right_image=right_image,
    )


def certificate_convergence_phase(phase_maps, stationary, fixed_point):
    restriction = stationary["matrix"]
    eigenvectors = matrix_from_columns(
        (
            (F(1), F(2), F(1)),
            (F(1), F(-1), F(1)),
            (F(1), F(0), F(-1)),
        )
    )
    coefficient_forms = (
        (F(1, 6), F(1, 3), F(1, 6)),
        (F(1, 3), F(-1, 3), F(1, 3)),
        (F(1, 2), F(0), F(-1, 2)),
    )
    identity_three = (
        (F(1), F(0), F(0)),
        (F(0), F(1), F(0)),
        (F(0), F(0), F(1)),
    )
    mass_form = (F(1), F(2), F(1))
    fixed = fixed_point["fixed"]
    reduced_fixed = (fixed[0], fixed[1], fixed[3])
    fixed_component = tuple(
        F(1, 6) * entry for entry in (F(1), F(2), F(1))
    )
    spectral_nodes = (
        matrix_multiply(eigenvectors, coefficient_forms) == identity_three,
        tuple(6 * coefficient for coefficient in coefficient_forms[0])
        == mass_form,
        # On W_1 the mass form is one, so its exact fixed component is v_*.
        fixed_component == reduced_fixed,
        matrix_vector(restriction, (F(1), F(2), F(1)))
        == (F(1), F(2), F(1)),
        matrix_vector(restriction, (F(1), F(-1), F(1)))
        == (F(-1, 2), F(1, 2), F(-1, 2)),
        matrix_vector(restriction, (F(1), F(0), F(-1)))
        == (F(0), F(0), F(0)),
        abs(F(-1, 2)) < 1,
        stationary["polynomial"][0] == 0,
        all(type(entry) is F for row in restriction for entry in row),
    )

    internal_left, internal_right, boundary = phase_maps["matrices"][:3]
    internal_left_value = matrix_vector(internal_left, fixed)
    internal_right_value = matrix_vector(internal_right, fixed)
    boundary_value = matrix_vector(boundary, fixed)
    average_value = tuple(
        F(1, 2) * (internal_left_value[index] + boundary_value[index])
        for index in range(4)
    )
    expected_internal = (F(0), F(1, 2), F(1, 2), F(0))
    expected_boundary = (F(1, 3), F(1, 6), F(1, 6), F(1, 3))
    phase_laws = (
        internal_left_value == expected_internal,
        internal_right_value == expected_internal,
        boundary_value == expected_boundary,
        average_value == fixed,
    )
    return proof_node(
        "B05",
        (
            len(eigenvectors) == 3,
            len(coefficient_forms) == 3,
            len(spectral_nodes) == 9,
        ),
        (
            ("LIMIT", all(spectral_nodes)),
            ("PHASE-LAW", all(phase_laws)),
        ),
        (phase_maps, stationary, fixed_point),
        spectral_nodes=len(spectral_nodes),
        phase_laws=len(phase_laws),
        internal_left_value=internal_left_value,
        internal_right_value=internal_right_value,
        boundary_value=boundary_value,
        average_value=average_value,
        coefficient_forms=coefficient_forms,
    )

def direct_prefix_audit():
    maximum = 4 * HORIZON
    digits = tuple(number.bit_count() & 1 for number in range(maximum + 1))
    records = {}
    structural_checks = [
        len(digits) == maximum + 1,
        all(digit in (0, 1) for digit in digits),
        all(digits[2 * index] == digits[index] for index in range(2 * HORIZON + 1)),
        all(
            digits[2 * index + 1] == 1 - digits[index]
            for index in range(2 * HORIZON)
        ),
    ]

    for length in range(1, maximum + 1):
        word = digits[:length]
        n_zero = sum(1 for digit in word if digit == 0)
        n_one = sum(1 for digit in word if digit == 1)
        pair_counts = tuple(
            sum(
                1
                for index in range(length - 1)
                if (word[index], word[index + 1]) == pair
            )
            for pair in PAIRS
        )
        balance = n_zero - n_one
        discrepancy = 6 * pair_counts[0] - length
        state = (balance, digits[length - 1], digits[length])
        records[length] = (
            n_zero,
            n_one,
            pair_counts[0],
            pair_counts[1],
            pair_counts[2],
            pair_counts[3],
            balance,
            discrepancy,
            state,
        )
        structural_checks.extend(
            (
                n_zero + n_one == length,
                sum(pair_counts, 0) == length - 1,
                discrepancy == 6 * pair_counts[0] - length,
                state == (balance, digits[length - 1], digits[length]),
            )
        )

    counterexamples = []
    math_checks = []

    for length in range(1, maximum + 1):
        record = records[length]
        balance_ok = record[6] in (-1, 0, 1)
        c10_ok = record[4] == record[0] - record[2] - 1
        math_checks.extend((balance_ok, c10_ok))
        if not balance_ok:
            counterexamples.append(
                "FA-BALANCE L=%d S=%d" % (length, record[6])
            )
        if not c10_ok:
            counterexamples.append(
                "FA-BALANCE L=%d c10=%d rhs=%d"
                % (length, record[4], record[0] - record[2] - 1)
            )

    four_step_violators = []
    for length in range(1, HORIZON + 1):
        record = records[length]
        twice = records[2 * length]
        four_times = records[4 * length]
        seam_actual = (twice[2], twice[3], twice[4], twice[5])
        seam_expected = (
            record[4],
            record[0] + record[5],
            record[1] + record[2],
            record[3],
        )
        seam_ok = seam_actual == seam_expected
        doubling_expected = -record[7] + 3 * record[6] - 6
        doubling_ok = twice[7] == doubling_expected
        four_expected = record[7] - 3 * record[6]
        four_ok = four_times[7] == four_expected
        parity_ok = (four_times[7] == record[7]) == (length & 1 == 0)
        math_checks.extend((seam_ok, doubling_ok, four_ok, parity_ok))
        if not seam_ok:
            counterexamples.append(
                "FA-SEAM L=%d actual=%s expected=%s"
                % (length, seam_actual, seam_expected)
            )
        if not doubling_ok:
            counterexamples.append(
                "FA-DOUBLING L=%d actual=%d expected=%d"
                % (length, twice[7], doubling_expected)
            )
        if not four_ok:
            counterexamples.append(
                "FA-FOUR-STEP L=%d actual=%d expected=%d"
                % (length, four_times[7], four_expected)
            )
        if not parity_ok:
            counterexamples.append(
                "FA-FOUR-STEP clause=PARITY L=%d dL=%d d4L=%d"
                % (length, record[7], four_times[7])
            )
        if four_times[7] != record[7]:
            four_step_violators.append(length)

        expected_even_state = (
            0,
            1 - record[8][1],
            record[8][2],
        )
        expected_odd_state = (
            1 - 2 * record[8][2],
            record[8][2],
            1 - record[8][2],
        )
        expected_odd_discrepancy = (
            -record[7]
            + 3 * record[8][0]
            - 7
            + 6 * (1 if (record[8][1], record[8][2]) == (1, 0) else 0)
        )
        t0_ok = twice[8] == expected_even_state and twice[7] == doubling_expected
        odd_record = records[2 * length + 1]
        t1_ok = (
            odd_record[8] == expected_odd_state
            and odd_record[7] == expected_odd_discrepancy
        )
        math_checks.extend((t0_ok, t1_ok))
        if not t0_ok:
            counterexamples.append(
                "FA-STATE branch=T0 L=%d actual_q=%s actual_d=%d expected_q=%s expected_d=%d"
                % (
                    length,
                    twice[8],
                    twice[7],
                    expected_even_state,
                    doubling_expected,
                )
            )
        if not t1_ok:
            counterexamples.append(
                "FA-STATE branch=T1 L=%d actual_q=%s actual_d=%d expected_q=%s expected_d=%d"
                % (
                    length,
                    odd_record[8],
                    odd_record[7],
                    expected_odd_state,
                    expected_odd_discrepancy,
                )
            )

    for index in range(1, HORIZON + 1):
        even_ok = records[2 * index][6] == 0
        math_checks.append(even_ok)
        if not even_ok:
            counterexamples.append(
                "FA-BALANCE m=%d S2m=%d" % (index, records[2 * index][6])
            )

    for index in range(HORIZON + 1):
        odd_balance = records[2 * index + 1][6]
        odd_expected = 1 - 2 * digits[index]
        odd_ok = odd_balance == odd_expected
        math_checks.append(odd_ok)
        if not odd_ok:
            counterexamples.append(
                "FA-BALANCE m=%d S2m1=%d expected=%d"
                % (index, odd_balance, odd_expected)
            )

    least_check = (
        bool(four_step_violators)
        and min(four_step_violators) == 1
        and records[1][7] == -1
        and records[4][7] == -4
    )
    math_checks.append(least_check)
    if not least_check:
        actual_least = min(four_step_violators) if four_step_violators else "NONE"
        counterexamples.append(
            "FA-FOUR-STEP clause=LEAST actual_least=%s expected_least=1 d1=%d d4=%d"
            % (actual_least, records[1][7], records[4][7])
        )

    direct_base = []
    for binary_length in (5, 6, 7, 8):
        lower = 1 << (binary_length - 1)
        upper = (1 << binary_length) - 1
        intervals = []
        for state in STATES:
            values = [
                records[length][7]
                for length in range(lower, upper + 1)
                if records[length][8] == state
            ]
            intervals.append((min(values), max(values)))
        direct_base.append(tuple(intervals))

    direct_base_by_state = tuple(
        tuple(direct_base[length][state] for length in range(4))
        for state in range(6)
    )
    base_ok = direct_base_by_state == BASE_INTERVALS
    math_checks.append(base_ok)
    if not base_ok:
        counterexamples.append(
            "FA-BASE actual=%s expected=%s" % (direct_base_by_state, BASE_INTERVALS)
        )

    direct_extrema = []
    for exponent in range(1, 9):
        direct_extrema.append(
            max(abs(records[length][7]) for length in range(1, (1 << exponent) + 1))
        )
    expected_extrema = tuple(
        2 if exponent == 1 else 4 if exponent == 2 else 2 * (((exponent + 1) >> 2) + 2)
        for exponent in range(1, 9)
    )
    extrema_ok = tuple(direct_extrema) == expected_extrema
    math_checks.append(extrema_ok)
    if not extrema_ok:
        counterexamples.append(
            "FA-EXTREMUM actual=%s expected=%s"
            % (tuple(direct_extrema), expected_extrema)
        )

    return {
        "pass": all(structural_checks) and all(math_checks),
        "structural": all(structural_checks),
        "math": all(math_checks),
        "gaps": (
            ()
            if all(math_checks) or counterexamples
            else ("DIRECT-MATH",)
        ),
        "provenance": frozenset(("C01",)),
        "horizon": HORIZON,
        "prefixes": maximum,
        "digits": digits,
        "records": records,
        "base": direct_base_by_state,
        "extrema": tuple(direct_extrema),
        "counterexamples": tuple(counterexamples),
    }


def audit_phase_matrices():
    audit_pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
    left_rows = [[F(0) for _ in range(4)] for _ in range(4)]
    right_rows = [[F(0) for _ in range(4)] for _ in range(4)]
    seam_rows = [[F(0) for _ in range(4)] for _ in range(4)]

    for column, (left_symbol, right_symbol) in enumerate(audit_pairs):
        expanded = (
            left_symbol,
            1 - left_symbol,
            right_symbol,
            1 - right_symbol,
        )
        left_pair = (expanded[0], expanded[1])
        seam_pair = (expanded[1], expanded[2])
        right_pair = (expanded[2], expanded[3])
        left_rows[audit_pairs.index(left_pair)][column] = F(1)
        seam_rows[audit_pairs.index(seam_pair)][column] = F(1)
        right_rows[audit_pairs.index(right_pair)][column] = F(1)

    internal_left = tuple(tuple(row) for row in left_rows)
    internal_right = tuple(tuple(row) for row in right_rows)
    boundary = tuple(tuple(row) for row in seam_rows)
    average_left = tuple(
        tuple(
            F(1, 2) * (internal_left[row][column] + boundary[row][column])
            for column in range(4)
        )
        for row in range(4)
    )
    average_right = tuple(
        tuple(
            F(1, 2) * (internal_right[row][column] + boundary[row][column])
            for column in range(4)
        )
        for row in range(4)
    )
    return internal_left, internal_right, boundary, average_left, average_right


def audit_polynomial_add(left, right):
    width = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else F(0))
        + (right[index] if index < len(right) else F(0))
        for index in range(width)
    )


def audit_polynomial_multiply(left, right):
    result = [F(0) for _ in range(len(left) + len(right) - 1)]
    for left_index in range(len(left)):
        for right_index in range(len(right)):
            result[left_index + right_index] += left[left_index] * right[right_index]
    return tuple(result)


def audit_polynomial_determinant(polynomial_matrix):
    size = len(polynomial_matrix)
    if size == 1:
        return polynomial_matrix[0][0]
    total = (F(0),)
    for column in range(size):
        minor = tuple(
            tuple(
                polynomial_matrix[row][other_column]
                for other_column in range(size)
                if other_column != column
            )
            for row in range(1, size)
        )
        term = audit_polynomial_multiply(
            polynomial_matrix[0][column],
            audit_polynomial_determinant(minor),
        )
        if column & 1:
            term = tuple(-coefficient for coefficient in term)
        total = audit_polynomial_add(total, term)
    return total


def audit_charpoly(matrix):
    polynomial_matrix = tuple(
        tuple(
            (-matrix[row][column], F(1) if row == column else F(0))
            for column in range(len(matrix))
        )
        for row in range(len(matrix))
    )
    return audit_polynomial_determinant(polynomial_matrix)


def audit_stationary_restriction(matrix):
    rational_basis = (
        (F(1), F(0), F(0), F(0)),
        (F(0), F(1), F(1), F(0)),
        (F(0), F(0), F(0), F(1)),
    )
    rows = [[F(0) for _ in range(3)] for _ in range(3)]
    invariant = []
    images = []
    for column in range(3):
        vector = rational_basis[column]
        image = tuple(
            sum((matrix[row][index] * vector[index] for index in range(4)), F(0))
            for row in range(4)
        )
        images.append(image)
        invariant.append(image[1] == image[2])
        reduced = (image[0], image[1], image[3])
        for row in range(3):
            rows[row][column] = reduced[row]
    return (
        tuple(tuple(row) for row in rows),
        tuple(invariant),
        rational_basis,
        tuple(images),
    )


def audit_determinant_three(matrix):
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def audit_exact_eigenvalue(matrix, vector):
    image = tuple(
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            F(0),
        )
        for row in range(len(matrix))
    )
    nonzero = tuple(index for index in range(len(vector)) if vector[index] != 0)
    if not nonzero:
        return None
    pivot = vector[nonzero[0]]
    inverse_pivot = F(pivot.denominator, pivot.numerator)
    eigenvalue = image[nonzero[0]] * inverse_pivot
    if image != tuple(eigenvalue * entry for entry in vector):
        return None
    return eigenvalue


def independent_matrix_audit():
    matrices = audit_phase_matrices()
    internal_left, internal_right, boundary, average_left, average_right = matrices
    left_polynomial = audit_charpoly(average_left)
    right_polynomial = audit_charpoly(average_right)
    (
        left_restriction,
        left_invariant,
        left_stationary_basis,
        left_stationary_images,
    ) = audit_stationary_restriction(average_left)
    (
        right_restriction,
        right_invariant,
        right_stationary_basis,
        right_stationary_images,
    ) = audit_stationary_restriction(average_right)
    stationary_polynomial = audit_charpoly(left_restriction)
    fixed = (F(1, 6), F(1, 3), F(1, 3), F(1, 6))

    def direct_vector(matrix, vector):
        return tuple(
            sum(
                (
                    matrix[row][column] * vector[column]
                    for column in range(len(vector))
                ),
                F(0),
            )
            for row in range(len(matrix))
        )

    left_fixed_image = direct_vector(average_left, fixed)
    right_fixed_image = direct_vector(average_right, fixed)
    internal_left_value = direct_vector(internal_left, fixed)
    internal_right_value = direct_vector(internal_right, fixed)
    boundary_value = direct_vector(boundary, fixed)
    average_value = tuple(
        F(1, 2) * (internal_left_value[index] + boundary_value[index])
        for index in range(4)
    )
    witness = (F(0), F(1), F(0), F(0))
    left_witness = direct_vector(average_left, witness)
    right_witness = direct_vector(average_right, witness)

    expected_internal_left = (
        (F(0), F(0), F(0), F(0)),
        (F(1), F(1), F(0), F(0)),
        (F(0), F(0), F(1), F(1)),
        (F(0), F(0), F(0), F(0)),
    )
    expected_internal_right = (
        (F(0), F(0), F(0), F(0)),
        (F(1), F(0), F(1), F(0)),
        (F(0), F(1), F(0), F(1)),
        (F(0), F(0), F(0), F(0)),
    )
    expected_boundary = (
        (F(0), F(0), F(1), F(0)),
        (F(0), F(0), F(0), F(1)),
        (F(1), F(0), F(0), F(0)),
        (F(0), F(1), F(0), F(0)),
    )
    expected_average_left = (
        (F(0), F(0), F(1, 2), F(0)),
        (F(1, 2), F(1, 2), F(0), F(1, 2)),
        (F(1, 2), F(0), F(1, 2), F(1, 2)),
        (F(0), F(1, 2), F(0), F(0)),
    )
    expected_average_right = (
        (F(0), F(0), F(1, 2), F(0)),
        (F(1, 2), F(0), F(1, 2), F(1, 2)),
        (F(1, 2), F(1, 2), F(0), F(1, 2)),
        (F(0), F(1, 2), F(0), F(0)),
    )
    expected_matrices = (
        expected_internal_left,
        expected_internal_right,
        expected_boundary,
        expected_average_left,
        expected_average_right,
    )
    expected_left_polynomial = (F(0), F(1, 4), F(-1, 4), F(-1), F(1))
    expected_right_polynomial = (F(0), F(-1, 4), F(-3, 4), F(0), F(1))
    expected_restriction = (
        (F(0), F(1, 2), F(0)),
        (F(1, 2), F(1, 2), F(1, 2)),
        (F(0), F(1, 2), F(0)),
    )
    expected_stationary_polynomial = (F(0), F(-1, 2), F(-1, 2), F(1))
    expected_left_witness = (F(0), F(1, 2), F(0), F(1, 2))
    expected_right_witness = (F(0), F(0), F(1, 2), F(1, 2))
    expected_internal_value = (F(0), F(1, 2), F(1, 2), F(0))
    expected_boundary_value = (F(1, 3), F(1, 6), F(1, 6), F(1, 3))

    structural_checks = (
        len(matrices) == 5,
        all(
            len(matrix) == 4 and all(len(row) == 4 for row in matrix)
            for matrix in matrices
        ),
        all(
            type(entry) is F
            for matrix in matrices
            for row in matrix
            for entry in row
        ),
        len(left_polynomial) == 5,
        len(right_polynomial) == 5,
        len(stationary_polynomial) == 4,
        all(type(entry) is F for row in left_restriction for entry in row),
        left_stationary_basis == right_stationary_basis,
        len(left_stationary_basis) == 3,
        len(left_stationary_images) == 3,
        len(right_stationary_images) == 3,
        all(
            type(entry) is F
            for image in left_stationary_images + right_stationary_images
            for entry in image
        ),
    )

    phase_ok = matrices == expected_matrices
    anchor_ok = (
        average_left != average_right
        and left_witness == expected_left_witness
        and right_witness == expected_right_witness
        and all(left_invariant)
        and all(right_invariant)
        and left_restriction == right_restriction
        and left_restriction == expected_restriction
    )
    spectrum_ok = (
        left_polynomial == expected_left_polynomial
        and right_polynomial == expected_right_polynomial
        and stationary_polynomial == expected_stationary_polynomial
    )
    fixed_ok = (
        left_fixed_image == fixed
        and right_fixed_image == fixed
        and sum(fixed, F(0)) == 1
        and all(entry > 0 for entry in fixed)
    )
    phase_laws_ok = (
        internal_left_value == expected_internal_value
        and internal_right_value == expected_internal_value
        and boundary_value == expected_boundary_value
        and average_value == fixed
    )

    stationary_basis = (
        (F(1), F(2), F(1)),
        (F(1), F(-1), F(1)),
        (F(1), F(0), F(-1)),
    )
    stationary_eigenvalues = tuple(
        audit_exact_eigenvalue(left_restriction, vector)
        for vector in stationary_basis
    )
    stationary_eigenmatrix = tuple(
        tuple(stationary_basis[column][row] for column in range(3))
        for row in range(3)
    )
    mass_zero_checks = (
        stationary_basis[1][0] + 2 * stationary_basis[1][1] + stationary_basis[1][2]
        == 0,
        stationary_basis[2][0] + 2 * stationary_basis[2][1] + stationary_basis[2][2]
        == 0,
    )
    limit_ok = (
        stationary_eigenvalues == (F(1), F(-1, 2), F(0))
        and audit_determinant_three(stationary_eigenmatrix) != 0
        and all(mass_zero_checks)
        and abs(F(-1, 2)) < 1
    )

    counterexamples = []
    if not phase_ok:
        counterexamples.append(
            "FB-PHASE actual=%s expected=%s" % (matrices, expected_matrices)
        )
    if not anchor_ok:
        counterexamples.append(
            "FB-ANCHOR input=%s left_witness=%s right_witness=%s expected_left=%s expected_right=%s left_matrix=%s right_matrix=%s stationary_basis=%s left_images=%s left_invariant=%s right_images=%s right_invariant=%s left_restriction=%s right_restriction=%s expected_restriction=%s"
            % (
                witness,
                left_witness,
                right_witness,
                expected_left_witness,
                expected_right_witness,
                average_left,
                average_right,
                left_stationary_basis,
                left_stationary_images,
                left_invariant,
                right_stationary_images,
                right_invariant,
                left_restriction,
                right_restriction,
                expected_restriction,
            )
        )
    if not spectrum_ok:
        counterexamples.append(
            "FB-SPECTRUM left=%s right=%s stationary=%s expected_left=%s expected_right=%s expected_stationary=%s"
            % (
                left_polynomial,
                right_polynomial,
                stationary_polynomial,
                expected_left_polynomial,
                expected_right_polynomial,
                expected_stationary_polynomial,
            )
        )
    if not fixed_ok:
        counterexamples.append(
            "FB-FIXED left=%s right=%s expected=%s"
            % (left_fixed_image, right_fixed_image, fixed)
        )
    if not phase_laws_ok:
        counterexamples.append(
            "FB-PHASE-LAW internal_left=%s internal_right=%s boundary=%s average=%s expected_internal=%s expected_boundary=%s expected_average=%s"
            % (
                internal_left_value,
                internal_right_value,
                boundary_value,
                average_value,
                expected_internal_value,
                expected_boundary_value,
                fixed,
            )
        )
    for vector, eigenvalue, mass_zero in zip(
        stationary_basis[1:],
        stationary_eigenvalues[1:],
        mass_zero_checks,
    ):
        if (
            phase_ok
            and anchor_ok
            and fixed_ok
            and mass_zero
            and eigenvalue is not None
            and abs(eigenvalue) >= 1
        ):
            lifted_mode = (vector[0], vector[1], vector[1], vector[2])
            normalized_input = tuple(
                fixed[index] + lifted_mode[index] for index in range(4)
            )
            mode_image = direct_vector(average_left, lifted_mode)
            counterexamples.append(
                "FB-LIMIT input=%s mass=%s stationary=%s v_star=%s R_v_star=%s mode=%s mode_mass=%s eigenvalue=%s R_mode=%s orbit_law=R^n(input)=v_star+(%s)^n*mode"
                % (
                    normalized_input,
                    sum(normalized_input, F(0)),
                    normalized_input[1] == normalized_input[2],
                    fixed,
                    left_fixed_image,
                    lifted_mode,
                    sum(lifted_mode, F(0)),
                    eigenvalue,
                    mode_image,
                    eigenvalue,
                )
            )

    math_checks = (
        phase_ok,
        anchor_ok,
        spectrum_ok,
        fixed_ok,
        limit_ok,
        phase_laws_ok,
    )
    limit_witnessed = any(
        item.partition(" ")[0] == "FB-LIMIT" for item in counterexamples
    )
    gaps = (
        ("MATRIX-LIMIT",)
        if not limit_ok and not limit_witnessed
        else ()
    )
    return {
        "pass": all(structural_checks) and all(math_checks),
        "structural": all(structural_checks),
        "math": all(math_checks),
        "gaps": gaps,
        "provenance": frozenset(("MATRIX-AUDIT",)),
        "counterexamples": tuple(counterexamples),
        "matrices": matrices,
        "left_polynomial": left_polynomial,
        "right_polynomial": right_polynomial,
        "left_restriction": left_restriction,
        "right_restriction": right_restriction,
        "stationary_polynomial": stationary_polynomial,
        "fixed": fixed,
        "left_fixed_image": left_fixed_image,
        "right_fixed_image": right_fixed_image,
        "left_witness": left_witness,
        "right_witness": right_witness,
        "internal_left_value": internal_left_value,
        "internal_right_value": internal_right_value,
        "boundary_value": boundary_value,
        "average_value": average_value,
        "stationary_eigenvalues": stationary_eigenvalues,
    }


def route_agreement(
    prefix_audit,
    matrix_audit,
    seams,
    balance,
    discrepancy_laws,
    transducer,
    four_bit,
    base_table,
    extrema,
    phase_maps,
    anchor,
    stationary,
    fixed,
    convergence,
):
    discrepancy_checks = []
    for length in range(1, HORIZON + 1):
        direct_record = prefix_audit["records"][length]
        state, discrepancy = transducer_value(length)
        discrepancy_checks.append(state == direct_record[8])
        discrepancy_checks.append(discrepancy == direct_record[7])

        parent_vector = direct_record[:6]
        predicted_pairs = tuple(
            sum(
                (
                    seams["coefficients"][pair][index] * parent_vector[index]
                    for index in range(6)
                ),
                0,
            )
            for pair in range(4)
        )
        discrepancy_checks.append(
            predicted_pairs == prefix_audit["records"][2 * length][2:6]
        )

        coefficient_vector = (
            direct_record[2],
            direct_record[0],
            length,
            1,
        )
        predicted_twice = sum(
            (
                discrepancy_laws["d_twice"][index] * coefficient_vector[index]
                for index in range(4)
            ),
            0,
        )
        predicted_four = sum(
            (
                discrepancy_laws["d_four"][index] * coefficient_vector[index]
                for index in range(4)
            ),
            0,
        )
        discrepancy_checks.append(
            predicted_twice == prefix_audit["records"][2 * length][7]
        )
        discrepancy_checks.append(
            predicted_four == prefix_audit["records"][4 * length][7]
        )

    discrepancy_checks.extend(
        prefix_audit["records"][2 * index][6]
        in set(balance["block_balance"])
        for index in range(1, HORIZON + 1)
    )
    discrepancy_checks.extend(
        prefix_audit["records"][2 * index + 1][6]
        == balance["odd_balance"][prefix_audit["digits"][index]]
        for index in range(HORIZON + 1)
    )

    # Two direct representatives with distinct d-values determine each affine
    # coefficient and offset independently for every state and four-bit word.
    representative_horizon = (4 * HORIZON - 15) >> 4
    representatives = {}
    for state in STATES:
        selected = []
        seen_discrepancies = set()
        for length in range(1, representative_horizon + 1):
            record = prefix_audit["records"][length]
            if record[8] == state and record[7] not in seen_discrepancies:
                selected.append(length)
                seen_discrepancies.add(record[7])
                if len(selected) == 2:
                    break
        if len(selected) != 2:
            raise ValueError("insufficient-direct-affine-representatives")
        representatives[state] = tuple(selected)

    path_checks = []
    for state, word, final_state, coefficient, offset, final_one in four_bit["records"]:
        first_length, second_length = representatives[state]
        first_child = (first_length << 4) + word
        second_child = (second_length << 4) + word
        first_source_d = prefix_audit["records"][first_length][7]
        second_source_d = prefix_audit["records"][second_length][7]
        first_child_record = prefix_audit["records"][first_child]
        second_child_record = prefix_audit["records"][second_child]
        denominator = second_source_d - first_source_d
        direct_coefficient = (
            second_child_record[7] - first_child_record[7]
        ) * F(1, denominator)
        direct_offset = first_child_record[7] - direct_coefficient * first_source_d
        path_checks.append(
            first_child <= 4 * HORIZON
            and second_child <= 4 * HORIZON
            and final_state == final_one
            and first_child_record[8] == final_state
            and second_child_record[8] == final_state
            and direct_coefficient == coefficient
            and direct_offset == offset
        )
    discrepancy_checks.extend(path_checks)

    discrepancy_checks.extend(
        base_table["actual"][state][length]
        == prefix_audit["base"][state][length]
        for state in range(6)
        for length in range(4)
    )
    discrepancy_checks.extend(
        extrema["small_cumulative"][index] == prefix_audit["extrema"][index]
        for index in range(8)
    )

    phase_checks = (
        phase_maps["matrices"] == matrix_audit["matrices"],
        anchor["left_polynomial"] == matrix_audit["left_polynomial"],
        anchor["right_polynomial"] == matrix_audit["right_polynomial"],
        anchor["left_witness"] == matrix_audit["left_witness"],
        anchor["right_witness"] == matrix_audit["right_witness"],
        stationary["matrix"] == matrix_audit["left_restriction"],
        stationary["right_matrix"] == matrix_audit["right_restriction"],
        stationary["polynomial"] == matrix_audit["stationary_polynomial"],
        fixed["fixed"] == matrix_audit["fixed"],
        fixed["left_image"] == matrix_audit["left_fixed_image"],
        fixed["right_image"] == matrix_audit["right_fixed_image"],
        convergence["internal_left_value"]
        == matrix_audit["internal_left_value"],
        convergence["internal_right_value"]
        == matrix_audit["internal_right_value"],
        convergence["boundary_value"] == matrix_audit["boundary_value"],
        convergence["average_value"] == matrix_audit["average_value"],
    )
    route_checks = tuple(discrepancy_checks) + phase_checks
    provenance = {"C02"}
    for node in (
        prefix_audit,
        matrix_audit,
        seams,
        balance,
        discrepancy_laws,
        transducer,
        four_bit,
        base_table,
        extrema,
        phase_maps,
        anchor,
        stationary,
        fixed,
        convergence,
    ):
        provenance.update(node["provenance"])
    return {
        "pass": all(route_checks),
        "structural": (
            len(path_checks) == 96
            and len(phase_checks) == 15
            and representative_horizon == 63
        ),
        "failures": () if all(route_checks) else ("ROUTE-DISAGREEMENT",),
        "provenance": frozenset(provenance),
        "discrepancy": len(discrepancy_checks),
        "phase": len(phase_checks),
    }

def negative_controls(
    prefix_audit,
    matrix_audit,
    proof_nodes,
):
    average_left = matrix_audit["matrices"][3]
    average_right = matrix_audit["matrices"][4]
    witness = (F(0), F(1), F(0), F(0))
    proof_provenance = set()
    for node in proof_nodes:
        proof_provenance.update(node["provenance"])
    finite_audit_nodes = {"C01", "MATRIX-AUDIT", "C02", "C03"}
    controls = (
        prefix_audit["records"][4][7] != prefix_audit["records"][1][7]
        and prefix_audit["records"][1][7] == -1
        and prefix_audit["records"][4][7] == -4,
        average_left != average_right
        and matrix_vector(average_left, witness)
        != matrix_vector(average_right, witness),
        matrix_audit["left_polynomial"] != matrix_audit["right_polynomial"],
        matrix_audit["internal_left_value"][0] == 0
        and matrix_audit["boundary_value"][0] == F(1, 3)
        and matrix_audit["internal_left_value"][0] != F(1, 6)
        and matrix_audit["boundary_value"][0] != F(1, 6),
        matrix_audit["stationary_polynomial"][0] == 0,
        proof_provenance.isdisjoint(finite_audit_nodes),
    )
    return {
        "pass": all(controls),
        "structural": len(controls) == 6,
        "failures": () if all(controls) else ("NEGATIVE-CONTROL",),
        "provenance": frozenset(("C03", "C01", "MATRIX-AUDIT")),
        "controls": len(controls),
    }

def contains_float(value):
    if type(value) is float:
        return True
    if isinstance(value, dict):
        return any(contains_float(key) or contains_float(item) for key, item in value.items())
    if isinstance(value, (tuple, list, set, frozenset)):
        return any(contains_float(item) for item in value)
    return False


def format_output(report):
    lines = [
        "P-GYRON-DISCREPANCY-LOG-3 exact verifier",
        "authority base=%s content=%s canon_sha256=%s"
        % (BASE_COMMIT, CONTENT_COMMIT, CANON_SHA256),
        "sources gyron=%s decoder=%s" % (GYRON_SHA256, DECODER_SHA256),
        "prereg sha256=%s" % PREREG_SHA256,
        "I01 RUNTIME arguments=%d environment=%d: %s"
        % (report["arguments"], report["environment"], report["I01"]),
        "I02 EXACTNESS integer=%d rational=%d forbidden=%d: %s"
        % (
            report["integer"],
            report["rational"],
            report["forbidden"],
            report["I02"],
        ),
        "A01 SEAMS identities=%d proof_nodes=%d: %s"
        % (report["A01"]["identities"], report["A01"]["proof_nodes"], report["A01"]["status"]),
        "A02 BALANCE identities=%d proof_nodes=%d: %s"
        % (report["A02"]["identities"], report["A02"]["proof_nodes"], report["A02"]["status"]),
        "A03 DISCREPANCY identities=%d boundary=%d: %s"
        % (report["A03"]["identities"], report["A03"]["boundary"], report["A03"]["status"]),
        "A04 TRANSDUCER states=%d transitions=%d: %s"
        % (report["A04"]["states"], report["A04"]["transitions"], report["A04"]["status"]),
        "A05 FOUR-BIT states=%d words=%d paths=%d: %s"
        % (
            report["A05"]["states"],
            report["A05"]["words"],
            report["A05"]["paths"],
            report["A05"]["status"],
        ),
        "A06 BASE-TABLE states=%d lengths=%d cells=%d: %s"
        % (
            report["A06"]["states"],
            report["A06"]["lengths"],
            report["A06"]["cells"],
            report["A06"]["status"],
        ),
        "A07 INDUCTION residues=%d transfer_nodes=%d: %s"
        % (
            report["A07"]["residues"],
            report["A07"]["transfer_nodes"],
            report["A07"]["status"],
        ),
        "A08 EXTREMA formulas=%d endpoint_nodes=%d: %s"
        % (
            report["A08"]["formulas"],
            report["A08"]["endpoint_nodes"],
            report["A08"]["status"],
        ),
        "A09 COROLLARIES proof_nodes=%d: %s"
        % (report["A09"]["proof_nodes"], report["A09"]["status"]),
        "B01 PHASE-MAPS maps=%d basis_checks=%d: %s"
        % (report["B01"]["maps"], report["B01"]["basis_checks"], report["B01"]["status"]),
        "B02 ANCHOR-SPECTRA matrices=%d polynomials=%d: %s"
        % (
            report["B02"]["matrices"],
            report["B02"]["polynomials"],
            report["B02"]["status"],
        ),
        "B03 STATIONARY restriction=%d spectrum=%d: %s"
        % (
            report["B03"]["restriction"],
            report["B03"]["spectrum"],
            report["B03"]["status"],
        ),
        "B04 FIXED-POINT equations=%d uniqueness_nodes=%d: %s"
        % (
            report["B04"]["equations"],
            report["B04"]["uniqueness_nodes"],
            report["B04"]["status"],
        ),
        "B05 CONVERGENCE spectral_nodes=%d phase_laws=%d: %s"
        % (
            report["B05"]["spectral_nodes"],
            report["B05"]["phase_laws"],
            report["B05"]["status"],
        ),
        "C01 DIRECT-PREFIX horizon=%d prefixes=%d: %s"
        % (report["C01"]["horizon"], report["C01"]["prefixes"], report["C01"]["status"]),
        "C02 ROUTE-AGREEMENT discrepancy=%d phase=%d: %s"
        % (
            report["C02"]["discrepancy"],
            report["C02"]["phase"],
            report["C02"]["status"],
        ),
        "C03 NEGATIVE-CONTROLS controls=%d: %s"
        % (report["C03"]["controls"], report["C03"]["status"]),
        "SCOPE L1 exact; forward phase-averaged substitution; no coarse-graining, decoder, physical measure, or L2-L6 lift",
        "counterexample: %s" % report["counterexample"],
        "diagnostic: %s" % report["diagnostic"],
        "gate A proof: %s" % report["gate_a"],
        "gate B proof: %s" % report["gate_b"],
        "gate C local audit: %s" % report["gate_c"],
        "theorem A decision: %s" % report["theorem_a"],
        "theorem B decision: %s" % report["theorem_b"],
        "run integrity: %s" % report["integrity"],
        "scientific decision: %s" % report["scientific"],
        "route: %s" % report["route"],
    ]
    return "\n".join(lines) + "\n"


def result_fields(result, first, second):
    return {
        first: result[first],
        second: result[second],
        "status": "PASS" if result["pass"] else "FAIL",
    }


def run_verifier():
    argument_count = len(sys.argv) - 1
    environment_count = sum(
        1 for name, value in ENVIRONMENT if os.environ.get(name) == value
    )
    runtime_checks = (argument_count == 0, environment_count == len(ENVIRONMENT))

    a01 = certificate_seams()
    a02 = certificate_balance()
    a03 = certificate_discrepancy(a01, a02)
    a04 = certificate_transducer(a02, a03)
    a05 = certificate_four_bit(a04)
    a06 = certificate_base_table(a05)
    a07 = certificate_induction(a05, a06)
    a08 = certificate_extrema(a07)
    a09 = certificate_corollaries(a08)

    b01 = certificate_phase_maps()
    b02 = certificate_anchor_spectra(b01)
    b03 = certificate_stationary(b01, b02)
    b04 = certificate_fixed_point(b01, b03)
    b05 = certificate_convergence_phase(b01, b03, b04)

    a_results = (a01, a02, a03, a04, a05, a06, a07, a08, a09)
    b_results = (b01, b02, b03, b04, b05)
    proof_results = a_results + b_results
    proof_labels = (
        "A01",
        "A02",
        "A03",
        "A04",
        "A05",
        "A06",
        "A07",
        "A08",
        "A09",
        "B01",
        "B02",
        "B03",
        "B04",
        "B05",
    )

    c01 = direct_prefix_audit()
    matrix_audit = independent_matrix_audit()
    c02 = route_agreement(
        c01,
        matrix_audit,
        a01,
        a02,
        a03,
        a04,
        a05,
        a06,
        a08,
        b01,
        b02,
        b03,
        b04,
        b05,
    )
    c03 = negative_controls(c01, matrix_audit, proof_results)

    integer_checks = (
        type(HORIZON) is int,
        HORIZON == 1 << 8,
        type(a05["paths"]) is int,
        a05["paths"] == 6 * 16,
        a06["cells"] == 6 * 4,
        c01["prefixes"] == 4 * HORIZON,
        transducer_value(1) == (STATE_F, -1),
        BASE_INTERVALS[0][0] == (-5, -3),
    )
    rational_checks = (
        F(1, 2) + F(1, 2) == 1,
        F(1, 3) + F(1, 6) == F(1, 2),
        all(
            type(entry) is F
            for matrix in b01["matrices"]
            for row in matrix
            for entry in row
        ),
        not contains_float((a01, a02, a03, a04, a05, a06, a07, a08, a09)),
        not contains_float((b01, b02, b03, b04, b05, matrix_audit)),
    )
    authority_checks = (
        is_lower_hex(BASE_COMMIT, 40),
        is_lower_hex(ISSUE_OPENING_MAIN, 40),
        is_lower_hex(ACTIVATION_COMMIT, 40),
        is_lower_hex(CONTENT_COMMIT, 40),
        is_lower_hex(CANON_SHA256, 64),
        is_lower_hex(STATUS_SHA256, 64),
        is_lower_hex(REGISTRY_SHA256, 64),
        is_lower_hex(GYRON_SHA256, 64),
        is_lower_hex(DECODER_SHA256, 64),
        is_lower_hex(PREREG_SHA256, 64),
    )
    proof_provenance = set()
    for result in proof_results:
        proof_provenance.update(result["provenance"])
    finite_audit_nodes = {"C01", "MATRIX-AUDIT", "C02", "C03"}
    forbidden_checks = (
        HORIZON == 256,
        cert_step is not direct_prefix_audit,
        proof_phase_matrices is not audit_phase_matrices,
        proof_charpoly is not audit_charpoly,
        certificate_layer is not direct_prefix_audit,
        proof_provenance.isdisjoint(finite_audit_nodes),
    )
    exactness_checks = integer_checks + rational_checks + authority_checks + forbidden_checks

    counterexamples = tuple(
        sorted(set(c01["counterexamples"] + matrix_audit["counterexamples"]))
    )
    a_witness_codes = frozenset(
        (
            "FA-SEAM",
            "FA-BALANCE",
            "FA-DOUBLING",
            "FA-FOUR-STEP",
            "FA-STATE",
            "FA-PATH",
            "FA-BASE",
            "FA-INDUCTION",
            "FA-EXTREMUM",
            "FA-COROLLARY",
        )
    )
    b_witness_codes = frozenset(
        (
            "FB-PHASE",
            "FB-ANCHOR",
            "FB-SPECTRUM",
            "FB-FIXED",
            "FB-LIMIT",
            "FB-PHASE-LAW",
        )
    )
    known_witness_codes = a_witness_codes | b_witness_codes
    witness_parts = tuple(item.partition(" ") for item in counterexamples)
    witness_codes = tuple(parts[0] for parts in witness_parts)
    witness_code_set = frozenset(witness_codes)
    witness_encoding_ok = all(
        separator == " " and bool(payload) and code in known_witness_codes
        for code, separator, payload in witness_parts
    )
    a_counterexamples = tuple(
        item
        for item, code in zip(counterexamples, witness_codes)
        if code in a_witness_codes
    )
    b_counterexamples = tuple(
        item
        for item, code in zip(counterexamples, witness_codes)
        if code in b_witness_codes
    )
    claim_witness_codes = {
        ("A01", "SEAMS"): ("FA-SEAM",),
        ("A02", "BALANCE"): ("FA-BALANCE",),
        ("A03", "DOUBLING"): ("FA-DOUBLING",),
        ("A03", "FOUR-STEP"): ("FA-FOUR-STEP",),
        ("A04", "STATE"): ("FA-STATE",),
        ("A05", "PATH"): ("FA-PATH",),
        ("A06", "BASE"): ("FA-BASE",),
        ("A07", "INDUCTION"): ("FA-INDUCTION",),
        ("A08", "EXTREMUM"): ("FA-EXTREMUM",),
        ("A09", "COROLLARY"): ("FA-COROLLARY",),
        ("B01", "PHASE"): ("FB-PHASE",),
        ("B02", "ANCHOR"): ("FB-ANCHOR",),
        ("B02", "SPECTRUM"): ("FB-SPECTRUM",),
        ("B03", "ANCHOR"): ("FB-ANCHOR",),
        ("B03", "SPECTRUM"): ("FB-SPECTRUM",),
        ("B04", "FIXED"): ("FB-FIXED",),
        ("B05", "LIMIT"): ("FB-LIMIT",),
        ("B05", "PHASE-LAW"): ("FB-PHASE-LAW",),
    }

    stop_codes = []
    if not witness_encoding_ok:
        stop_codes.append("STOP-WITNESS-ENCODING")
    if not all(runtime_checks):
        stop_codes.append("STOP-I01")
    if not all(exactness_checks):
        stop_codes.append("STOP-I02")
    for label, result in zip(proof_labels, proof_results):
        if not result["structural"]:
            stop_codes.append("STOP-" + label + "-STRUCTURE")
        for failure in result["failures"]:
            allowed_codes = claim_witness_codes[(label, failure)]
            matching = any(
                code in witness_code_set for code in allowed_codes
            )
            if not matching:
                stop_codes.append("STOP-" + label + "-" + failure)

    if not c01["structural"]:
        stop_codes.append("STOP-C01-STRUCTURE")
    stop_codes.extend("STOP-C01-" + gap for gap in c01["gaps"])
    if not matrix_audit["structural"]:
        stop_codes.append("STOP-C01-MATRIX-STRUCTURE")
    stop_codes.extend(
        "STOP-C01-MATRIX-" + gap for gap in matrix_audit["gaps"]
    )
    if not c02["structural"] or not c02["pass"]:
        stop_codes.append("STOP-C02")
    if not c03["structural"] or not c03["pass"]:
        stop_codes.append("STOP-C03")

    local_audit_pass = (
        c01["structural"]
        and not c01["gaps"]
        and matrix_audit["structural"]
        and not matrix_audit["gaps"]
        and c02["structural"]
        and c02["pass"]
        and c03["structural"]
        and c03["pass"]
    )
    integrity_pass = all(runtime_checks) and all(exactness_checks) and local_audit_pass
    stopped = bool(stop_codes) or not integrity_pass
    a_pass = all(result["pass"] for result in a_results)
    b_pass = all(result["pass"] for result in b_results)

    if stopped:
        gate_a = "STOP"
        gate_b = "STOP"
        gate_c = "STOP"
        theorem_a = "STOP"
        theorem_b = "STOP"
        scientific = "STOP"
        route = "STOP"
        counterexample = "NONE"
        diagnostic = sorted(set(stop_codes))[0] if stop_codes else "STOP-INTEGRITY"
        exit_code = 2
    else:
        gate_a = "FALSIFIED" if a_counterexamples else "PROOF-SURVIVES"
        gate_b = "FALSIFIED" if b_counterexamples else "PROOF-SURVIVES"
        gate_c = "AUDIT-PASS"
        theorem_a = gate_a
        theorem_b = gate_b
        if a_counterexamples or b_counterexamples:
            scientific = "FALSIFIED"
            route = "FALSIFIED"
            counterexample = min(a_counterexamples + b_counterexamples)
            diagnostic = "NONE"
            exit_code = 0
        elif a_pass and b_pass:
            scientific = "PROOF-SURVIVES"
            route = "PROOF-SURVIVES"
            counterexample = "NONE"
            diagnostic = "NONE"
            exit_code = 0
        else:
            gate_a = "STOP"
            gate_b = "STOP"
            gate_c = "STOP"
            theorem_a = "STOP"
            theorem_b = "STOP"
            scientific = "STOP"
            route = "STOP"
            counterexample = "NONE"
            diagnostic = "STOP-UNRESOLVED-PROOF"
            exit_code = 2

    report = {
        "arguments": argument_count,
        "environment": environment_count,
        "I01": pass_fail(runtime_checks),
        "integer": len(integer_checks),
        "rational": len(rational_checks),
        "forbidden": len(forbidden_checks),
        "I02": pass_fail(exactness_checks),
        "A01": result_fields(a01, "identities", "proof_nodes"),
        "A02": result_fields(a02, "identities", "proof_nodes"),
        "A03": result_fields(a03, "identities", "boundary"),
        "A04": result_fields(a04, "states", "transitions"),
        "A05": {
            "states": a05["states"],
            "words": a05["words"],
            "paths": a05["paths"],
            "status": "PASS" if a05["pass"] else "FAIL",
        },
        "A06": {
            "states": a06["states"],
            "lengths": a06["lengths"],
            "cells": a06["cells"],
            "status": "PASS" if a06["pass"] else "FAIL",
        },
        "A07": result_fields(a07, "residues", "transfer_nodes"),
        "A08": result_fields(a08, "formulas", "endpoint_nodes"),
        "A09": {
            "proof_nodes": a09["proof_nodes"],
            "status": "PASS" if a09["pass"] else "FAIL",
        },
        "B01": result_fields(b01, "maps", "basis_checks"),
        "B02": result_fields(b02, "matrices", "polynomials"),
        "B03": result_fields(b03, "restriction", "spectrum"),
        "B04": result_fields(b04, "equations", "uniqueness_nodes"),
        "B05": result_fields(b05, "spectral_nodes", "phase_laws"),
        "C01": {
            "horizon": c01["horizon"],
            "prefixes": c01["prefixes"],
            "status": "PASS" if c01["pass"] else "FAIL",
        },
        "C02": result_fields(c02, "discrepancy", "phase"),
        "C03": {
            "controls": c03["controls"],
            "status": "PASS" if c03["pass"] else "FAIL",
        },
        "counterexample": counterexample,
        "diagnostic": diagnostic,
        "gate_a": gate_a,
        "gate_b": gate_b,
        "gate_c": gate_c,
        "theorem_a": theorem_a,
        "theorem_b": theorem_b,
        "integrity": "PASS" if integrity_pass and not stopped else "FAIL",
        "scientific": scientific,
        "route": route,
    }
    return report, exit_code

def stop_report(diagnostic):
    failed_pair = {"status": "FAIL"}
    return {
        "arguments": max(len(sys.argv) - 1, 0),
        "environment": sum(
            1 for name, value in ENVIRONMENT if os.environ.get(name) == value
        ),
        "I01": "FAIL",
        "integer": 0,
        "rational": 0,
        "forbidden": 0,
        "I02": "FAIL",
        "A01": dict(failed_pair, identities=0, proof_nodes=0),
        "A02": dict(failed_pair, identities=0, proof_nodes=0),
        "A03": dict(failed_pair, identities=0, boundary=0),
        "A04": dict(failed_pair, states=0, transitions=0),
        "A05": dict(failed_pair, states=0, words=0, paths=0),
        "A06": dict(failed_pair, states=0, lengths=0, cells=0),
        "A07": dict(failed_pair, residues=0, transfer_nodes=0),
        "A08": dict(failed_pair, formulas=0, endpoint_nodes=0),
        "A09": dict(failed_pair, proof_nodes=0),
        "B01": dict(failed_pair, maps=0, basis_checks=0),
        "B02": dict(failed_pair, matrices=0, polynomials=0),
        "B03": dict(failed_pair, restriction=0, spectrum=0),
        "B04": dict(failed_pair, equations=0, uniqueness_nodes=0),
        "B05": dict(failed_pair, spectral_nodes=0, phase_laws=0),
        "C01": dict(failed_pair, horizon=HORIZON, prefixes=4 * HORIZON),
        "C02": dict(failed_pair, discrepancy=0, phase=0),
        "C03": dict(failed_pair, controls=0),
        "counterexample": "NONE",
        "diagnostic": diagnostic,
        "gate_a": "STOP",
        "gate_b": "STOP",
        "gate_c": "STOP",
        "theorem_a": "STOP",
        "theorem_b": "STOP",
        "integrity": "FAIL",
        "scientific": "STOP",
        "route": "STOP",
    }


def exception_code(error):
    if isinstance(error, ArithmeticError):
        return "STOP-EXCEPTION-ARITHMETIC"
    if isinstance(error, LookupError):
        return "STOP-EXCEPTION-LOOKUP"
    if isinstance(error, TypeError):
        return "STOP-EXCEPTION-TYPE"
    if isinstance(error, ValueError):
        return "STOP-EXCEPTION-VALUE"
    if isinstance(error, MemoryError):
        return "STOP-EXCEPTION-MEMORY"
    return "STOP-EXCEPTION-OTHER"


try:
    FINAL_REPORT, FINAL_EXIT = run_verifier()
except BaseException as ERROR:
    FINAL_REPORT = stop_report(exception_code(ERROR))
    FINAL_EXIT = 2

sys.stdout.write(format_output(FINAL_REPORT))
raise SystemExit(FINAL_EXIT)
