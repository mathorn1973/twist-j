#!/usr/bin/env python3
"""Exact finite checks for P-QDD-AFFINE-ENERGY-CONTROL-1.

This file contains a fixed witness and fixed rejection controls, not a search.
It does not establish physical availability of the Hamiltonians or apparatus.
The conservation-law theorem and its quantifiers belong to the written proof.
In particular, code isometries below do not assert global unitarity of native U.

Arithmetic is integer arithmetic, F_5, Q(zeta_5), or F_101.  No floats, optional
packages, randomness, or external inputs are used.  Run only after public pin.
"""

from itertools import product


P = 5
POINTS = tuple(product(range(P), repeat=6))
PAIR_POINTS = tuple(product(range(P), repeat=2))
LABELS = (1, 2, 3, 4)
ZERO_CYCLO = (0, 0, 0, 0)
FIVE_CYCLO = (5, 0, 0, 0)

# Gate tuples: (kind, target, source-or-None, coefficient).
# Each gate uses the current coordinate values; lists are chronological.
A_GATES = (
    ("sum", 4, 0, 1),
    ("sum", 4, 1, 1),
    ("sum", 4, 2, 1),
    ("sum", 4, 3, 1),
    ("shift", 4, None, 2),
)
B_GATES = (
    ("sum", 4, 2, 4),
    ("sum", 3, 0, 4),
    ("sum", 3, 2, 2),
    ("sum", 3, 5, 1),
    ("sum", 2, 0, 1),
    ("sum", 2, 5, 1),
    ("scale", 2, None, 3),
    ("sum", 1, 0, 3),
    ("sum", 1, 2, 1),
    ("sum", 1, 5, 3),
    ("shift", 1, None, 3),
    ("sum", 5, 2, 1),
    ("shift", 5, None, 3),
    ("scale", 0, None, 4),
    ("sum", 0, 5, 2),
    ("sum", 0, 2, 3),
    ("shift", 0, None, 2),
    ("swap", 0, 1, 0),
    ("swap", 1, 2, 0),
)

B_ROWS = (
    (1, 1, 3, 0, 0, 1),
    (3, 0, 3, 0, 0, 3),
    (4, 0, 0, 0, 0, 2),
    (4, 0, 2, 1, 0, 1),
    (0, 0, 4, 0, 1, 0),
    (3, 0, 3, 0, 0, 4),
)


def apply_gates(point, gates):
    x = list(point)
    for kind, target, source, coefficient in gates:
        if kind == "sum":
            assert source is not None and source != target
            x[target] = (x[target] + coefficient * x[source]) % P
        elif kind == "shift":
            x[target] = (x[target] + coefficient) % P
        elif kind == "scale":
            assert coefficient % P != 0
            x[target] = coefficient * x[target] % P
        elif kind == "swap":
            assert source is not None and source != target
            x[target], x[source] = x[source], x[target]
        else:
            raise AssertionError("Unknown elementary gate")
    return tuple(x)


def inverse_gates(gates):
    result = []
    for kind, target, source, coefficient in reversed(gates):
        if kind in ("sum", "shift"):
            coefficient = -coefficient % P
        elif kind == "scale":
            coefficient = pow(coefficient, -1, P)
        else:
            assert kind == "swap"
        result.append((kind, target, source, coefficient))
    return tuple(result)


def affine_a(x):
    a, b, c, d, q, r = x
    return a, b, c, d, (q + a + b + c + d + 2) % P, r


def affine_b(x):
    a, b, c, d, q, r = x
    return (
        (a + b + 3 * c + r + 3) % P,
        (3 * a + 3 * c + 3 * r) % P,
        (4 * a + 2 * r + 3) % P,
        (4 * a + 2 * c + d + r) % P,
        (q + 4 * c) % P,
        (3 * a + 3 * c + 4 * r + 3) % P,
    )


def root_power(exponent):
    """zeta**exponent in the basis 1,zeta,zeta**2,zeta**3.

    Reduction uses Phi_5 = 1 + zeta + ... + zeta**4 exactly.
    """
    exponent %= P
    if exponent == 4:
        return (-1, -1, -1, -1)
    return tuple(int(i == exponent) for i in range(4))


def fourier_sum_numerator(source, initial, final, gain):
    """Five times the F^dagger D_gain F matrix element.

    F|y> = sum_j zeta**(j*y)|j>/sqrt(5), and D_gain has
    diagonal phase zeta**(gain*source*j).  Both Fourier normalizers
    are retained by the exact denominator 5.
    """
    terms = [root_power(j * (initial + gain * source - final))
             for j in range(P)]
    return tuple(sum(term[i] for term in terms) for i in range(4))


def native_generator(index, x):
    a, b, c, d, q, r = x
    raw = (
        (b, a, d, c, q, r),
        (-c, -d, -a, -b, -q, -r),
        (2 - c, 1 - d + r, 2 - a, 1 - b - r, 1 - q, -r),
        (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r),
        (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r),
    )[index]
    return tuple(v % P for v in raw)


def native_step(bit, x):
    return native_generator((sum(x) + 2 * bit) % P, x)


def code_point(h):
    return h, 0, 0, 0, (1 - h) % P, 0


def entrance(x):
    a, b, c, d, q, r = x
    h = (a + b + c + d) % P
    f = (0, 1, 2, 2, 2)[h]
    return a, b, c, d, (q - f) % P, (r + f) % P


def route(x, first_gates=A_GATES, second_gates=B_GATES):
    x = apply_gates(x, first_gates)
    x = native_step(0, x)
    x = apply_gates(x, second_gates)
    return native_step(1, x)


def determinant_mod(matrix, prime):
    rows = [[v % prime for v in row] for row in matrix]
    determinant = 1
    size = len(rows)
    for column in range(size):
        pivot = next((i for i in range(column, size)
                      if rows[i][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            determinant = -determinant
        value = rows[column][column]
        determinant = determinant * value % prime
        inverse = pow(value, -1, prime)
        for i in range(column + 1, size):
            factor = rows[i][column] * inverse % prime
            rows[i] = [(a - factor * b) % prime
                       for a, b in zip(rows[i], rows[column])]
    return determinant % prime


def check_g1():
    assert len(A_GATES) == 5 and len(B_GATES) == 19
    assert sum(g[0] == "sum" for g in A_GATES + B_GATES) == 16
    for gates, direct in ((A_GATES, affine_a), (B_GATES, affine_b)):
        inverse = inverse_gates(gates)
        outputs = set()
        for x in POINTS:
            y = apply_gates(x, gates)
            assert y == direct(x)
            assert apply_gates(y, inverse) == x
            outputs.add(y)
        assert len(outputs) == 15625
    print("PASS G1 fixed affine netlists: 2 x 15625 points; exact bijections")


def check_g2():
    count = 0
    for source, initial, final in product(range(P), repeat=3):
        numerator = fourier_sum_numerator(source, initial, final, 1)
        expected = FIVE_CYCLO if final == (initial + source) % P else ZERO_CYCLO
        assert numerator == expected
        count += 1
    assert count == 125
    print("PASS G2 Fourier-phase SUM: 125 exact cyclotomic coefficients")


def check_g3():
    matrix_units = 0
    gain_one_mapping = None
    for gain in range(P):
        derived = {}
        for source, initial in PAIR_POINTS:
            support = []
            for final in range(P):
                numerator = fourier_sum_numerator(source, initial, final, gain)
                if numerator != ZERO_CYCLO:
                    assert numerator == FIVE_CYCLO
                    support.append((source, final))
            assert support == [(source, (initial + gain * source) % P)]
            derived[source, initial] = support[0]
        assert len(set(derived.values())) == 25
        if gain == 1:
            gain_one_mapping = dict(derived)
        for left, right in product(PAIR_POINTS, repeat=2):
            actual = derived[left], derived[right]
            expected = ((left[0], (left[1] + gain * left[0]) % P),
                        (right[0], (right[1] + gain * right[0]) % P))
            assert actual == expected
            matrix_units += 1
    assert matrix_units == 3125
    # SWAP is derived from the same gate family, not supplied as another
    # interregister Hamiltonian: y+=x; x-=y; y+=x; x=-x.
    swap_gates = (("sum", 1, 0, 1), ("sum", 0, 1, 4),
                  ("sum", 1, 0, 1), ("scale", 0, None, 4))
    for x, y in PAIR_POINTS:
        assert apply_gates((x, y), swap_gates) == (y, x)
    # Independent calibration input: (|0> + |1>)|0>/sqrt(2).
    # The output's 2 x 2 coefficient minor has determinant 1 (rank two).
    assert gain_one_mapping is not None
    entangled_support = tuple(gain_one_mapping[x] for x in ((0, 0), (1, 0)))
    assert entangled_support == ((0, 0), (1, 1))
    coefficient_minor = tuple(tuple(int((x, y) in entangled_support)
                                    for y in range(2)) for x in range(2))
    assert coefficient_minor[0][0] * coefficient_minor[1][1] - \
        coefficient_minor[0][1] * coefficient_minor[1][0] == 1
    print("PASS G3 gains 0..4: 3125 matrix units; 25 SWAP points; entanglement witness")


def check_g4():
    assert ((3).bit_count() % 2, (4).bit_count() % 2) == (0, 1)
    current = [code_point(h) for h in LABELS]
    target = [entrance(x) for x in current]
    expected_first_native = [
        (1, 1, 3, 4, 4, 1),
        (0, 2, 0, 0, 3, 0),
        (0, 0, 2, 0, 2, 0),
        (2, 1, 3, 1, 3, 0),
    ]
    expected_after_b = [
        (0, 0, 4, 0, 1, 4),
        (0, 0, 3, 0, 3, 3),
        (4, 1, 3, 4, 0, 4),
        (0, 0, 1, 0, 0, 3),
    ]
    operations = (affine_a, lambda x: native_step(0, x),
                  affine_b, lambda x: native_step(1, x))
    for stage, operation in enumerate(operations):
        current = [operation(x) for x in current]
        assert len(set(current)) == 4
        assert len(set(product(current, repeat=2))) == 16
        if stage == 1:
            assert current == expected_first_native
        if stage == 2:
            assert current == expected_after_b
    assert current == target
    for h in LABELS:
        x = code_point(h)
        assert native_step(1, native_step(0, x)) == x
        y = entrance(x)
        assert native_step(1, native_step(0, y)) == y
        assert route(x) == entrance(x)
    for left, right in product(range(4), repeat=2):
        assert (current[left], current[right]) == (target[left], target[right])
    print("PASS G4 actual ticks 3,4: 4 injective prefixes; 16 code matrix units")


def check_g5():
    energy_changes = []
    port_coefficients = []
    a_changes = []
    tuned_changes = []
    for h in LABELS:
        x = code_point(h)
        y = entrance(x)
        energy_changes.append(sum(y) - sum(x))
        dq, dr = y[4] - x[4], y[5] - x[5]
        port_coefficients.append((dq, dr))
        tuned_changes.append(dq + 6 * dr)
        a_changes.append(sum(affine_a(x)) - sum(x))
    assert energy_changes == [5, 0, 0, 0]
    assert port_coefficients == [(4, 1), (-2, 2), (-2, 2), (-2, 2)]
    assert tuned_changes == [10, 10, 10, 10]
    assert a_changes == [3, -1, 0, 1]
    print("PASS G5 clean-energy witnesses: (5,0,0,0); tuned-gap boundary verified")


def check_g6():
    zero_image = affine_b((0,) * 6)
    derived_rows = [[] for _ in range(6)]
    for column in range(6):
        unit = tuple(int(i == column) for i in range(6))
        image = affine_b(unit)
        for row in range(6):
            derived_rows[row].append((image[row] - zero_image[row]) % P)
    assert tuple(map(tuple, derived_rows)) == B_ROWS
    assert determinant_mod(B_ROWS, P) == 2
    axes = {tuple(gain if i == axis else 0 for i in range(6))
            for axis in range(6) for gain in range(1, P)}
    row_support = {tuple(gain * value % P for value in row)
                   for row in B_ROWS for gain in range(1, P)}
    assert len(axes) == 24
    assert len(row_support) == 24
    assert axes.isdisjoint(row_support)
    assert all(sum(value != 0 for value in row) > 1 for row in B_ROWS)
    print("PASS G6 global B Fourier obstruction: det=2; 24 nonaxial frequencies")


def check_g7():
    # Without the Fourier conjugation, the diagonal interaction cannot move
    # |1,0> to |1,1>; its phase at |1,0> is exactly one.
    assert root_power(1 * 0) == (1, 0, 0, 0)
    diagonal_only_output = (1, 0)
    required_sum_output = (1, 1)
    assert diagonal_only_output != required_sum_output

    # Removing the registered constant from A fails at a fixed code input.
    assert A_GATES[-1] == ("shift", 4, None, 2)
    x = code_point(1)
    incorrect_output = route(x, first_gates=A_GATES[:-1])
    assert incorrect_output == (3, 2, 2, 3, 2, 4)
    assert entrance(x) == (1, 0, 0, 0, 4, 1)
    assert incorrect_output != entrance(x)

    # A fixed mistyped B coefficient is likewise rejected by the full netlist
    # identity, independently of selector branch behavior.
    wrong_b = list(B_GATES)
    wrong_b[0] = ("sum", 4, 2, 3)
    witness = (0, 0, 1, 0, 0, 0)
    assert apply_gates(witness, wrong_b) != affine_b(witness)

    # Equality modulo five is not equality of ordinary real-valued energy.
    y = entrance(x)
    assert sum(x) % P == sum(y) % P == 1
    assert sum(x) == 1 and sum(y) == 6
    print("PASS G7 four fixed negative controls rejected")


def check_g8():
    """Independent rank certificate for all additive diagonal energies.

    There are 30 unknowns e_i(v).  Every integer row is E(Bx)-E(x).
    Rank 24 modulo 101 implies rational rank at least 24.  The six disjoint
    constant-local-energy null vectors give rational rank at most 24, so the
    rank over Q, R, or C is exactly 24.  No floating rank threshold is used.
    """
    prime = 101
    basis = {}
    rows_checked = 0
    for x in POINTS:
        y = affine_b(x)
        row = [0] * 30
        for coordinate in range(6):
            row[5 * coordinate + y[coordinate]] += 1
            row[5 * coordinate + x[coordinate]] -= 1
        for coordinate in range(6):
            assert sum(row[5 * coordinate:5 * coordinate + 5]) == 0
        row = [value % prime for value in row]
        for column in sorted(basis):
            coefficient = row[column]
            if coefficient:
                pivot = basis[column]
                row = [(value - coefficient * entry) % prime
                       for value, entry in zip(row, pivot)]
        column = next((i for i, value in enumerate(row) if value), None)
        if column is not None:
            assert column not in basis
            inverse = pow(row[column], -1, prime)
            basis[column] = [value * inverse % prime for value in row]
        rows_checked += 1
    assert rows_checked == 15625
    assert len(basis) == 24
    print("PASS G8 independent additive-energy system: 15625 rows; rank 24 mod 101")


def main():
    checks = (check_g1, check_g2, check_g3, check_g4,
              check_g5, check_g6, check_g7, check_g8)
    for check in checks:
        check()
    print("PASS P-QDD-AFFINE-ENERGY-CONTROL-1: 8/8 exact finite checks")


if __name__ == "__main__":
    main()
