"""Exact finite audit for P-PHOTON-INCIDENCE-GLOBAL-CARRIER-1.

All polynomials are sparse elements of the integral group ring of the
integer time lattice and D3. Shifts use endpoint anchors. The universal
null-set statement uses the accompanying proof, not a momentum sample.
"""

from collections import Counter
from itertools import permutations, product
from math import prod


ORIGIN = (0, 0, 0)
SHELL_WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
SCALE = 324
BASIS = ((1, 1, 0), (1, 0, 1), (0, 1, 1))


def require(condition, label):
    if not condition:
        print(f"BREAK {label}")
        raise SystemExit(1)


def add_displacement(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale_displacement(factor, displacement):
    return tuple(factor * coordinate for coordinate in displacement)


def squared_length(displacement):
    return sum(coordinate * coordinate for coordinate in displacement)


def shift(displacement=ORIGIN, *, time=0, coefficient=1):
    return {(time, *displacement): coefficient}


def scale_polynomial(factor, polynomial):
    return {
        exponent: factor * coefficient
        for exponent, coefficient in polynomial.items()
        if factor * coefficient
    }


def add_polynomials(*polynomials):
    terms = Counter()
    for polynomial in polynomials:
        terms.update(polynomial)
    return {exponent: coefficient for exponent, coefficient in terms.items() if coefficient}


def multiply(left, right):
    terms = Counter()
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exponent, right_exponent))
            terms[exponent] += left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in terms.items() if coefficient}


def difference(displacement):
    return add_polynomials(shift(displacement), shift(coefficient=-1))


def representative(displacement):
    first = next(coordinate for coordinate in displacement if coordinate)
    sign = 1 if first > 0 else -1
    return scale_displacement(sign, displacement), sign


def primitive_coordinates(displacement):
    x, y, z = displacement
    numerators = (x + y - z, x + z - y, y + z - x)
    require(all(value % 2 == 0 for value in numerators), "F01 spatial lattice membership")
    return tuple(value // 2 for value in numerators)


def shell_geometry():
    shells = {
        displacement: SHELL_WEIGHTS[squared_length(displacement)]
        for displacement in product(range(-4, 5), repeat=3)
        if squared_length(displacement) in SHELL_WEIGHTS
    }
    counts = Counter(squared_length(displacement) for displacement in shells)
    require(counts == {2: 12, 4: 6, 8: 12, 10: 24, 16: 6}, "F01 shell census")
    pairs = {
        displacement: weight
        for displacement, weight in shells.items()
        if representative(displacement)[1] == 1
    }
    nearest = tuple(displacement for displacement in pairs if squared_length(displacement) == 2)
    require(len(pairs) == 30 and len(nearest) == 6, "F01 pair census")
    for displacement in shells:
        coordinates = primitive_coordinates(displacement)
        rebuilt = tuple(
            sum(n * base[axis] for n, base in zip(coordinates, BASIS))
            for axis in range(3)
        )
        require(rebuilt == displacement, "F01 primitive coordinates")
    basis_matrix = tuple(primitive_coordinates(base) for base in BASIS)
    require(basis_matrix == ((1, 0, 0), (0, 1, 0), (0, 0, 1)), "F01 basis inverse")
    require(set(BASIS) <= set(nearest), "F01 generation by nearest pairs")
    return shells, pairs, nearest


def coordinate_group():
    return tuple(
        tuple(sign * (axis + 1) for axis, sign in zip(order, signs))
        for order in permutations(range(3))
        for signs in product((-1, 1), repeat=3)
    )


def act(group_element, displacement):
    return tuple(
        displacement[abs(axis) - 1] if axis > 0 else -displacement[-axis - 1]
        for axis in group_element
    )


def act_on_polynomial(group_element, polynomial):
    return {
        (exponent[0], *act(group_element, exponent[1:])): coefficient
        for exponent, coefficient in polynomial.items()
    }


def path_row(displacement, nearest_set):
    if displacement in nearest_set:
        return {displacement: shift()}
    prefix = ORIGIN
    row = {}
    for count, base in zip(primitive_coordinates(displacement), BASIS):
        indices = range(count) if count >= 0 else range(count, 0)
        sign = 1 if count >= 0 else -1
        terms = [
            shift(add_displacement(prefix, scale_displacement(index, base)), coefficient=sign)
            for index in indices
        ]
        if terms:
            row[base] = add_polynomials(*terms)
        prefix = add_displacement(prefix, scale_displacement(count, base))
    require(prefix == displacement, "F02 path endpoint")
    return row


def apply_row(row):
    return add_polynomials(
        *(multiply(polynomial, difference(base)) for base, polynomial in row.items())
    )


def transport_row(group_element, displacement, row, *, anchored=True):
    output, output_sign = representative(act(group_element, displacement))
    transformed_row = {}
    for base, polynomial in row.items():
        transformed_base, input_sign = representative(act(group_element, base))
        anchor = ORIGIN
        if anchored:
            # D_{-v}=-T_{-v} D_v. The output uses the inverse multiplier.
            if output_sign == -1:
                anchor = output
            if input_sign == -1:
                anchor = add_displacement(anchor, scale_displacement(-1, transformed_base))
        multiplier = shift(anchor, coefficient=output_sign * input_sign)
        transformed_row[transformed_base] = multiply(
            multiplier, act_on_polynomial(group_element, polynomial)
        )
    return output, transformed_row


def audit_centered_deck(displacement, row):
    output_coordinates = primitive_coordinates(displacement)
    for base, polynomial in row.items():
        input_coordinates = primitive_coordinates(base)
        for lag, *anchor in polynomial:
            require(lag == 0, "F04 spatial row contains time")
            centered = add_displacement(
                scale_displacement(2, anchor),
                add_displacement(base, scale_displacement(-1, displacement)),
            )
            centered_coordinates = primitive_coordinates(centered)
            require(
                tuple(value % 2 for value in centered_coordinates)
                == tuple((a + b) % 2 for a, b in zip(input_coordinates, output_coordinates)),
                "F04 centered deck signs",
            )


def audit_rows(pairs, nearest):
    nearest_set = set(nearest)
    rows = {displacement: path_row(displacement, nearest_set) for displacement in pairs}
    for displacement, row in rows.items():
        require(apply_row(row) == difference(displacement), "F02 incidence factorization")
    group = coordinate_group()
    require(len(group) == len(set(group)) == 48, "F03 signed-coordinate group")
    transported_count = 0
    sign_reversals = 0
    for group_element in group:
        seen = set()
        for displacement, row in rows.items():
            transformed, transformed_row = transport_row(group_element, displacement, row)
            seen.add(transformed)
            require(pairs.get(transformed) == pairs[displacement], "F03 shell transport")
            require(
                set(transformed_row) <= nearest_set,
                "F03 transported nearest domain",
            )
            require(
                apply_row(transformed_row) == difference(transformed),
                "F03 anchored incidence transport",
            )
            if transformed in nearest_set:
                require(transformed_row == {transformed: shift()}, "F04 metric identity rows")
            audit_centered_deck(transformed, transformed_row)
            transported_count += 1
            sign_reversals += representative(act(group_element, displacement))[1] == -1
        require(seen == set(pairs), "F03 transported row census")
    require(transported_count == 1440 and sign_reversals == 720, "F03 transport totals")
    require(min(pairs[base] for base in nearest) == 6, "F04 metric floor")
    return rows, transported_count


def weighted_moment(pairs, axes):
    return sum(
        weight * prod(displacement[axis] for axis in axes)
        for displacement, weight in pairs.items()
    )


def audit_moments(pairs):
    for i, j in product(range(3), repeat=2):
        expected = 324 if i == j else 0
        require(weighted_moment(pairs, (i, j)) == expected, "F01 paired second moment")
    for axes in product(range(3), repeat=4):
        multiplicities = sorted(Counter(axes).values())
        expected = 0
        if multiplicities == [4]:
            expected = 1584
        elif multiplicities == [2, 2]:
            expected = 528
        require(weighted_moment(pairs, axes) == expected, "F01 paired fourth moment")


def spatial_dirichlet(pairs):
    return add_polynomials(
        *(
            multiply(
                difference(scale_displacement(-1, displacement)),
                scale_polynomial(weight, difference(displacement)),
            )
            for displacement, weight in pairs.items()
        )
    )


def directed_operator(shells, connection):
    return add_polynomials(
        *(
            add_polynomials(
                shift(coefficient=weight),
                shift(displacement, coefficient=-weight * connection(displacement)),
            )
            for displacement, weight in shells.items()
        )
    )


def audit_operators(shells, pairs):
    spatial = spatial_dirichlet(pairs)
    selected = directed_operator(shells, lambda displacement: 1)
    require(spatial == selected and len(spatial) == 61, "F06 spatial operator equality")

    forward = shift(time=1)
    backward = shift(time=-1)
    temporal = multiply(
        add_polynomials(forward, shift(coefficient=-1)),
        add_polynomials(backward, shift(coefficient=-1)),
    )
    source = add_polynomials(scale_polynomial(SCALE, temporal), scale_polynomial(-1, spatial))
    recurrence = add_polynomials(
        shift(time=1, coefficient=SCALE),
        shift(time=-1, coefficient=SCALE),
        shift(coefficient=-2 * SCALE),
        selected,
    )
    require(source == scale_polynomial(-1, recurrence), "F06 variational recurrence")

    # Scale the first row of lambda I - T by 324 to keep integer coefficients.
    top_left = add_polynomials(
        shift(time=1, coefficient=SCALE), shift(coefficient=-2 * SCALE), selected
    )
    top_right = shift(coefficient=SCALE)
    bottom_left = shift(coefficient=-1)
    determinant = add_polynomials(
        multiply(top_left, forward), scale_polynomial(-1, multiply(top_right, bottom_left))
    )
    require(
        determinant == scale_polynomial(-1, multiply(forward, source)),
        "F07 exact characteristic",
    )
    return spatial, temporal


def torsion_numerator(pairs, bits):
    # Each term is sin^2(pi * dot(bits, primitive_coordinates(v)) / 2).
    return sum(
        weight
        for displacement, weight in pairs.items()
        if sum(bit * coordinate for bit, coordinate in zip(bits, primitive_coordinates(displacement))) % 2
    )


def audit_torsion(pairs):
    numerators = Counter(torsion_numerator(pairs, bits) for bits in product((0, 1), repeat=3))
    require(numerators == {0: 1, 27: 4, 32: 3}, "F08 reciprocal two-torsion census")


def character_sign(displacement):
    return 1 if (sum(displacement) // 2) % 2 == 0 else -1


def at_real_character(polynomial, temporal_sign, spatial_sign):
    return sum(
        coefficient * (temporal_sign if lag % 2 else 1) * spatial_sign((x, y, z))
        for (lag, x, y, z), coefficient in polynomial.items()
    )


def audit_controls(shells, pairs, rows, spatial, temporal):
    v = (2, 0, 0)
    altered = dict(rows[v])
    altered[BASIS[0]] = add_polynomials(altered[BASIS[0]], shift())
    require(
        apply_row(altered) == add_polynomials(difference(v), difference(BASIS[0]))
        and apply_row(altered) != difference(v),
        "CONTROL corrupt_row",
    )
    inversion = (-1, -2, -3)
    transformed, unanchored = transport_row(inversion, v, rows[v], anchored=False)
    require(
        transformed == v and apply_row(unanchored).get((0, *v), 0) == 0
        and difference(v)[(0, *v)] == 1,
        "CONTROL orientation",
    )

    # This connection is a flat character, but fixed-gauge equality is literal.
    require(
        all(
            character_sign(add_displacement(v, w)) == character_sign(v) * character_sign(w)
            for v, w in product(shells, repeat=2)
        ),
        "CONTROL character sign",
    )
    nontrivial_gauge = directed_operator(shells, character_sign)
    require(
        at_real_character(spatial, 1, lambda displacement: 1) == 0
        and at_real_character(nontrivial_gauge, 1, lambda displacement: 1) == 108
        and nontrivial_gauge != spatial,
        "CONTROL fixed_gauge",
    )

    control_momentum = (1, 1, 1)
    require(torsion_numerator(pairs, control_momentum) == 27, "CONTROL spatial mode")
    wrong_weight = {
        displacement: weight + (squared_length(displacement) == 2)
        for displacement, weight in pairs.items()
    }
    require(
        weighted_moment(wrong_weight, (0, 0)) == 328
        and torsion_numerator(wrong_weight, control_momentum) == 30,
        "CONTROL bad_weight",
    )
    missing_pair = dict(pairs)
    del missing_pair[BASIS[0]]
    require(
        len(missing_pair) == 29 and torsion_numerator(missing_pair, control_momentum) == 21,
        "CONTROL missing_pair",
    )

    # lambda = (5 + i sqrt(11))/6 has norm one. For a unit lambda,
    # lambda + lambda^-1 = 2 Re(lambda), here 5/3.
    require(5**2 + 11 == 6**2, "CONTROL unit temporal witness")
    spatial_numerator = 27
    spatial_denominator = 81
    temporal_numerator = 6 - 5
    temporal_denominator = 3
    require(
        temporal_numerator * spatial_denominator == spatial_numerator * temporal_denominator,
        "CONTROL temporal witness lies on operational characteristic",
    )

    # Evaluate c=2 and eta=1 using common denominators.
    changed_time = 2 * temporal_numerator * spatial_denominator
    unchanged_space = spatial_numerator * temporal_denominator
    require(
        3 * (changed_time - unchanged_space) == temporal_denominator * spatial_denominator,
        "CONTROL c",
    )
    time_fourth = temporal_numerator**2
    require(
        9 * time_fourth == temporal_denominator**2,
        "CONTROL eta",
    )

    # The zero vector is null over every base point. At (lambda=-1,k=0)
    # the marked graph point instead has temporal square 4 and zero space.
    require(
        at_real_character(temporal, -1, lambda displacement: 1) == 4
        and at_real_character(spatial, -1, lambda displacement: 1) == 0,
        "CONTROL off_graph",
    )


def main():
    shells, pairs, nearest = shell_geometry()
    rows, transported_count = audit_rows(pairs, nearest)
    audit_moments(pairs)
    spatial, temporal = audit_operators(shells, pairs)
    audit_torsion(pairs)
    audit_controls(shells, pairs, rows, spatial, temporal)

    print(f"PASS shells: directed={len(shells)} paired={len(pairs)} nearest={len(nearest)}")
    print(f"PASS incidence: groups=48 transported_rows={transported_count}")
    print("PASS moments: paired_second=324I quartic_isotropic=true")
    print(f"PASS forms: spatial_terms={len(spatial)} metric_floor=6/81")
    print("PASS characteristic: det(lambda I-T)=-lambda Q")
    print("PASS torsion: zero=1 one_third=4 thirty_two_over_eighty_one=3")
    print("PASS controls: corrupt_row orientation fixed_gauge bad_weight missing_pair c eta off_graph")
    print("PASS PHOTON-INCIDENCE-GLOBAL-CARRIER-1")


if __name__ == "__main__":
    main()
