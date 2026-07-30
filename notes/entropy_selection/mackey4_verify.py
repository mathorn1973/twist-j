#!/usr/bin/env python3
"""Primary exact route for C-ENTROPY-MACKEY-OBSTRUCTION-4-N.

NON-CANONICAL incubation. No public claim or Canon status.

This program reconstructs the depth-five source, the complete finite target,
the common D5 cocycle, all eight D5 subgroups, and the conditional Haar
pushforward lemma. It does not import any earlier Mackey candidate.

Python standard library only. Exact integer and Fraction arithmetic only.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product

PRIME = 5
DEPTH = 5
Q5_SIZE = PRIME**DEPTH
STATE_COUNT = PRIME**6

GATES: list[tuple[str, bool]] = []


def gate(tag: str, claim: str, ok: bool, detail: str = "") -> None:
    GATES.append((tag, bool(ok)))
    suffix = f"  {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} {tag} {claim}{suffix}")


# ---------------------------------------------------------------------------
# O/lambda^5, exact lambda-coordinate model
# ---------------------------------------------------------------------------

Vector4 = tuple[int, int, int, int]
Matrix4 = tuple[Vector4, Vector4, Vector4, Vector4]

IDENTITY4: Matrix4 = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
ZETA_MATRIX: Matrix4 = (
    (0, 0, 0, -1),
    (1, 0, 0, -1),
    (0, 1, 0, -1),
    (0, 0, 1, -1),
)
J_POWER_MATRIX: Matrix4 = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)
LAMBDA_TO_POWER: Matrix4 = (
    (1, 1, 1, 1),
    (0, -1, -2, -3),
    (0, 0, 1, 3),
    (0, 0, 0, -1),
)
POWER_TO_LAMBDA = LAMBDA_TO_POWER
LAMBDA4_RELATION: Vector4 = (-5, 10, -10, 5)


def mat_vec(matrix: Matrix4, vector: Vector4) -> Vector4:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(4)) for i in range(4)
    )  # type: ignore[return-value]


def lambda_to_power(vector: Vector4) -> Vector4:
    return mat_vec(LAMBDA_TO_POWER, vector)


def power_to_lambda(vector: Vector4) -> Vector4:
    return mat_vec(POWER_TO_LAMBDA, vector)


def decode_q5(index: int) -> tuple[int, int, int, int, int]:
    if not 0 <= index < Q5_SIZE:
        raise ValueError("Q5 index out of range")
    digits = []
    value = index
    for _ in range(5):
        digits.append(value % 5)
        value //= 5
    return tuple(digits)  # type: ignore[return-value]


def encode_q5(digits: tuple[int, int, int, int, int]) -> int:
    value = 0
    place = 1
    for digit in digits:
        if not 0 <= digit < 5:
            raise ValueError("Q5 digit out of range")
        value += digit * place
        place *= 5
    return value


def q5_from_lambda(vector: Vector4) -> int:
    a0 = vector[0] % 25
    a1 = vector[1] % 5
    a2 = vector[2] % 5
    a3 = vector[3] % 5
    d0 = a0 % 5
    d4 = ((d0 - a0) // 5) % 5
    return encode_q5((d0, a1, a2, a3, d4))


def q5_lambda(index: int) -> Vector4:
    d0, d1, d2, d3, d4 = decode_q5(index)
    return ((d0 - 5 * d4) % 25, d1, d2, d3)


def q5_from_power(vector: Vector4) -> int:
    return q5_from_lambda(power_to_lambda(vector))


def q5_add(left: int, right: int) -> int:
    a = q5_lambda(left)
    b = q5_lambda(right)
    return q5_from_lambda(tuple(a[i] + b[i] for i in range(4)))


def q5_neg(value: int) -> int:
    a = q5_lambda(value)
    return q5_from_lambda(tuple(-x for x in a))


def q5_mul(left: int, right: int) -> int:
    a = q5_lambda(left)
    b = q5_lambda(right)
    raw = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            raw[i + j] += x * y
    for degree in range(6, 3, -1):
        coefficient = raw[degree]
        if coefficient == 0:
            continue
        raw[degree] = 0
        offset = degree - 4
        for j, relation_coefficient in enumerate(LAMBDA4_RELATION):
            raw[offset + j] += coefficient * relation_coefficient
    return q5_from_lambda(tuple(raw[:4]))


def q5_mul_j(value: int) -> int:
    power = lambda_to_power(q5_lambda(value))
    return q5_from_power(mat_vec(J_POWER_MATRIX, power))


def permutation_cycle_type(mapping: tuple[int, ...], points: tuple[int, ...] | None = None) -> Counter[int]:
    if points is None:
        points = tuple(range(len(mapping)))
    remaining = set(points)
    result: Counter[int] = Counter()
    while remaining:
        start = min(remaining)
        current = start
        length = 0
        while current in remaining:
            remaining.remove(current)
            current = mapping[current]
            length += 1
        if current != start:
            raise ValueError("mapping is not a permutation on the carrier")
        result[length] += 1
    return result


# ---------------------------------------------------------------------------
# Public finite kernel and recurrent carrier
# ---------------------------------------------------------------------------

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def decode_state(index: int) -> tuple[int, int, int, int, int, int]:
    digits = []
    value = index
    for _ in range(6):
        digits.append(value % 5)
        value //= 5
    return tuple(digits)  # type: ignore[return-value]


def encode_state(state: tuple[int, int, int, int, int, int]) -> int:
    value = 0
    for digit in reversed(state):
        value = 5 * value + digit
    return value


def gen_a(x: tuple[int, ...]) -> tuple[int, ...]:
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((-x[i]) % 5 for i in (2, 3, 0, 1, 4, 5))


def gen_c(x: tuple[int, ...]) -> tuple[int, ...]:
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return tuple((b4[i] + S_VEC[i] + r * U_VEC[i]) % 5 for i in range(4)) + (
        (1 - q) % 5,
        (-r) % 5,
    )


def gen_d(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENERATORS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(right)))


def build_public_tables() -> tuple[
    tuple[tuple[int, ...], ...], tuple[tuple[int, ...], tuple[int, ...]], tuple[int, ...]
]:
    decoded = tuple(decode_state(i) for i in range(STATE_COUNT))
    traces = tuple(sum(state) % 5 for state in decoded)
    generator_tables = tuple(
        tuple(encode_state(generator(state)) for state in decoded)
        for generator in GENERATORS
    )
    letters = tuple(
        tuple(generator_tables[(traces[state] + 2 * epsilon) % 5][state] for state in range(STATE_COUNT))
        for epsilon in (0, 1)
    )
    return generator_tables, letters, traces  # type: ignore[return-value]


def thue_morse(n: int) -> int:
    return n.bit_count() & 1


def recurrent_census(letters: tuple[tuple[int, ...], tuple[int, ...]]) -> tuple[frozenset[int], tuple[frozenset[int], ...]]:
    current = list(range(STATE_COUNT))
    for n in range(400):
        table = letters[thue_morse(n)]
        current = [table[state] for state in current]
    windows = [set() for _ in range(STATE_COUNT)]
    for n in range(400, 700):
        table = letters[thue_morse(n)]
        for seed, state in enumerate(current):
            windows[seed].add(state)
        current = [table[state] for state in current]
    components = tuple(
        sorted(set(map(frozenset, windows)), key=lambda component: (len(component), min(component)))
    )
    support = frozenset(state for component in components for state in component)
    return support, components


# ---------------------------------------------------------------------------
# D5 return group and common cocycle reconstruction
# ---------------------------------------------------------------------------


def abstract_d5(
    generator_tables: tuple[tuple[int, ...], ...]
) -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, ...], ...],
    tuple[int, ...],
    tuple[tuple[str, int], ...],
]:
    identity = tuple(range(STATE_COUNT))
    b = generator_tables[1]
    d = generator_tables[3]
    e = generator_tables[4]
    beb = compose(b, compose(e, b))
    rotation = compose(d, beb)
    powers = [identity]
    for _ in range(4):
        powers.append(compose(rotation, powers[-1]))
    h1 = tuple(powers[a] for a in range(5)) + tuple(
        compose(powers[a], d) for a in range(5)
    )
    names = tuple(("rot", a) for a in range(5)) + tuple(("ref", a) for a in range(5))
    if len(set(h1)) != 10:
        raise AssertionError("return group is not D5 of order 10")
    h0 = tuple(compose(b, compose(element, b)) for element in h1)
    index = {element: i for i, element in enumerate(h1)}
    multiplication = tuple(
        tuple(index[compose(h1[i], h1[j])] for j in range(10)) for i in range(10)
    )
    inverses = tuple(
        next(j for j in range(10) if multiplication[i][j] == 0 and multiplication[j][i] == 0)
        for i in range(10)
    )
    return h0, h1, multiplication, inverses, names


def generic_labels(
    component: frozenset[int],
    half_points: tuple[set[int], set[int]],
    h0: tuple[tuple[int, ...], ...],
    h1: tuple[tuple[int, ...], ...],
) -> dict[int, tuple[int, dict[int, int]]]:
    result: dict[int, tuple[int, dict[int, int]]] = {}
    for half, group in ((0, h0), (1, h1)):
        points = sorted(component & half_points[half])
        base = points[0]
        images = [element[base] for element in group]
        if len(set(images)) != 10 or set(images) != set(points):
            raise AssertionError("generic half is not a free D5 torsor")
        result[half] = (base, {state: label for label, state in enumerate(images)})
    return result


def map_labels(
    source_labels: dict[int, int],
    target_labels: dict[int, int],
    letter: tuple[int, ...],
) -> tuple[int, ...]:
    output = [0] * 10
    for state, label in source_labels.items():
        output[label] = target_labels[letter[state]]
    if len(set(output)) != 10:
        raise AssertionError("one-tick map is not bijective on a generic torsor")
    return tuple(output)


def left_translation_label(mapping: tuple[int, ...], multiplication: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(
        element
        for element in range(10)
        if all(mapping[g] == multiplication[element][g] for g in range(10))
    )


def right_translation_label(mapping: tuple[int, ...], multiplication: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(
        element
        for element in range(10)
        if all(mapping[g] == multiplication[g][element] for g in range(10))
    )


def transformed_mapping(
    mapping: tuple[int, ...],
    source_gauge: int,
    target_gauge: int,
    multiplication: tuple[tuple[int, ...], ...],
    inverses: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        multiplication[mapping[multiplication[g][source_gauge]]][inverses[target_gauge]]
        for g in range(10)
    )


def left_cosets(
    multiplication: tuple[tuple[int, ...], ...], subgroup: frozenset[int]
) -> tuple[frozenset[int], ...]:
    return tuple(
        sorted(
            {
                frozenset(multiplication[g][h] for h in subgroup)
                for g in range(10)
            },
            key=lambda coset: tuple(sorted(coset)),
        )
    )


def orbit_count_on_set(
    subgroup: frozenset[int],
    points: tuple[object, ...],
    action,
) -> int:
    remaining = set(range(len(points)))
    count = 0
    while remaining:
        count += 1
        seed = min(remaining)
        orbit = {action(element, seed) for element in subgroup}
        remaining.difference_update(orbit)
    return count


def enumerate_subgroups(
    multiplication: tuple[tuple[int, ...], ...], inverses: tuple[int, ...]
) -> tuple[frozenset[int], ...]:
    subgroups = []
    for mask in range(1 << 10):
        if not (mask & 1):
            continue
        subset = frozenset(i for i in range(10) if mask & (1 << i))
        if any(inverses[i] not in subset for i in subset):
            continue
        if any(multiplication[i][j] not in subset for i in subset for j in subset):
            continue
        subgroups.append(subset)
    return tuple(sorted(subgroups, key=lambda group: (len(group), tuple(sorted(group)))))


def generated_subgroup(
    generators: tuple[int, ...], multiplication: tuple[tuple[int, ...], ...]
) -> frozenset[int]:
    group = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            for candidate in (
                multiplication[generator][current], multiplication[current][generator]
            ):
                if candidate not in group:
                    group.add(candidate)
                    frontier.append(candidate)
    return frozenset(group)


# ---------------------------------------------------------------------------
# Main exact audit
# ---------------------------------------------------------------------------


def main() -> int:
    print("C-ENTROPY-MACKEY-OBSTRUCTION-4-N PRIMARY")
    print("STATUS NON-CANONICAL; PRIMARY ROUTE ONLY; BREAKER REQUIRED")
    print("SCOPE fixed lambda-depth five, fiberwise bijective Route A subclass, r>=2")
    print()

    q5_forms = {q5_lambda(index) for index in range(Q5_SIZE)}
    additive_basis = (
        q5_from_lambda((1, 0, 0, 0)),
        q5_from_lambda((0, 1, 0, 0)),
        q5_from_lambda((0, 0, 1, 0)),
        q5_from_lambda((0, 0, 0, 1)),
    )

    def additive_order(value: int) -> int:
        current = 0
        for order in range(1, 26):
            current = q5_add(current, value)
            if current == 0:
                return order
        raise AssertionError("additive order exceeds 25")

    gate(
        "S01",
        "Q5 has 3125 canonical classes and additive type Z/25 + (Z/5)^3",
        len(q5_forms) == Q5_SIZE
        and tuple(additive_order(value) for value in additive_basis) == (25, 5, 5, 5),
        "orders=(25,5,5,5)",
    )

    j_mapping = tuple(q5_mul_j(index) for index in range(Q5_SIZE))
    source_type = permutation_cycle_type(j_mapping)
    gate(
        "S02",
        "multiplication by J is a permutation of cycle type 1^1 4^1 20^156",
        len(set(j_mapping)) == Q5_SIZE
        and source_type == Counter({20: 156, 4: 1, 1: 1}),
        f"cycle_type={dict(sorted(source_type.items()))}",
    )

    finite_source_counts = {
        r: 1 + min(2**r, 4) + 156 * min(2**r, 4) for r in range(8)
    }
    expected_source_counts = {0: 158, 1: 315, **{r: 629 for r in range(2, 8)}}
    gate(
        "S03",
        "the finite dyadic component formula stabilizes at 629 exactly for r>=2",
        finite_source_counts == expected_source_counts,
        "r0=158 r1=315 r2..7=629",
    )

    generators, letters, traces = build_public_tables()
    support, components = recurrent_census(letters)
    component_sizes = Counter(map(len, components))
    half_points = (
        {state for state in support if traces[state] == 4},
        {state for state in support if traces[state] == 1},
    )
    target_core_ok = (
        len(support) == 6250
        and len(components) == 313
        and component_sizes == Counter({20: 312, 10: 1})
        and tuple(map(len, half_points)) == (3125, 3125)
        and half_points[0].isdisjoint(half_points[1])
        and all(
            letters[epsilon][state] in component
            for component in components
            for epsilon in (0, 1)
            for state in component
        )
    )
    gate(
        "T01",
        "the complete recurrent target is 312x20 plus one x10 with two 3125 halves",
        target_core_ok,
        f"components={dict(sorted(component_sizes.items()))}",
    )

    h0, h1, multiplication, inverses, names = abstract_d5(generators)
    expected_edges = {(0, 0): 9, (0, 1): 0, (1, 0): 0, (1, 1): 5}
    gauge_census: Counter[int] = Counter()
    generic_ok = True
    generic_count = 0
    singlet_index = -1

    for component_index, component in enumerate(components):
        if len(component) == 10:
            singlet_index = component_index
            continue
        generic_count += 1
        labels = generic_labels(component, half_points, h0, h1)
        map_01 = map_labels(labels[0][1], labels[1][1], letters[1])
        right = right_translation_label(map_01, multiplication)
        if len(right) != 1 or right[0] not in (0, 7):
            generic_ok = False
            continue
        cross_gauge = right[0]
        gauge_census[cross_gauge] += 1
        gauges = {0: 0, 1: cross_gauge}
        for half in (0, 1):
            for epsilon in (0, 1):
                raw = map_labels(labels[half][1], labels[epsilon][1], letters[epsilon])
                normalized = transformed_mapping(
                    raw,
                    gauges[half],
                    gauges[epsilon],
                    multiplication,
                    inverses,
                )
                left = left_translation_label(normalized, multiplication)
                if left != (expected_edges[(half, epsilon)],):
                    generic_ok = False
    gate(
        "T02",
        "all 312 generic halves admit one fixed gauge with common D5 edge cocycle",
        generic_ok
        and generic_count == 312
        and gauge_census == Counter({0: 157, 7: 155}),
        "edges=(ref4,id,id,ref0); gauges id=157 ref2=155",
    )

    if singlet_index < 0:
        raise AssertionError("singlet target component missing")
    singlet = components[singlet_index]
    singlet_labels: dict[int, dict[int, frozenset[int]]] = {}
    singlet_ok = True
    stabilizers = []
    for half, group in ((0, h0), (1, h1)):
        points = sorted(singlet & half_points[half])
        base = points[0]
        labels_by_state: dict[int, list[int]] = defaultdict(list)
        for label, element in enumerate(group):
            labels_by_state[element[base]].append(label)
        cosets = {state: frozenset(labels) for state, labels in labels_by_state.items()}
        singlet_labels[half] = cosets
        stabilizers.append(cosets[base])
        singlet_ok = singlet_ok and len(points) == 5 and len(cosets) == 5
    singlet_ok = singlet_ok and stabilizers == [frozenset({0, 7}), frozenset({0, 7})]
    for half in (0, 1):
        for epsilon in (0, 1):
            element = expected_edges[(half, epsilon)]
            for state, coset in singlet_labels[half].items():
                predicted = frozenset(multiplication[element][g] for g in coset)
                actual = singlet_labels[epsilon][letters[epsilon][state]]
                if predicted != actual:
                    singlet_ok = False
    gate(
        "T03",
        "the singlet is D5/C2 and carries the same common edge cocycle",
        singlet_ok,
        "stabilizer={id,ref2}; edges=(ref4,id,id,ref0)",
    )

    cocycle_generators = tuple(sorted(set(expected_edges.values())))
    generated = generated_subgroup(cocycle_generators, multiplication)
    gate(
        "T04",
        "the two nontrivial common edge labels generate D5",
        len(generated) == 10,
        "ref4 and ref0 generate order 10",
    )

    subgroups = enumerate_subgroups(multiplication, inverses)
    subgroup_sizes = Counter(map(len, subgroups))
    reflection_subgroups = [
        subgroup
        for subgroup in subgroups
        if len(subgroup) == 2 and any(names[element][0] == "ref" for element in subgroup)
    ]
    h_stabilizer = frozenset({0, 7})
    singlet_cosets = left_cosets(multiplication, h_stabilizer)
    coset_index = {coset: index for index, coset in enumerate(singlet_cosets)}

    def regular_action(element: int, point: int) -> int:
        return multiplication[element][point]

    def singlet_action(element: int, point: int) -> int:
        image = frozenset(multiplication[element][g] for g in singlet_cosets[point])
        return coset_index[image]

    menu_rows = []
    for subgroup in subgroups:
        regular_orbits = orbit_count_on_set(
            subgroup, tuple(range(10)), regular_action
        )
        singlet_orbits = orbit_count_on_set(
            subgroup, tuple(singlet_cosets), singlet_action
        )
        total = 312 * regular_orbits + singlet_orbits
        menu_rows.append((subgroup, regular_orbits, singlet_orbits, total))

    total_menu = sorted(set(row[3] for row in menu_rows))
    complete_subgroups_ok = (
        len(subgroups) == 8
        and subgroup_sizes == Counter({2: 5, 1: 1, 5: 1, 10: 1})
        and len(reflection_subgroups) == 5
        and total_menu == [313, 625, 1563, 3125]
    )
    gate(
        "M01",
        "all eight D5 subgroups give the complete target component menu",
        complete_subgroups_ok,
        "menu={313,625,1563,3125}; five C2 subgroups enumerated",
    )

    c2_rows = [row for row in menu_rows if len(row[0]) == 2]
    burnside_ok = all(
        regular_orbits == 5 and singlet_orbits == 3 and total == 1563
        for _, regular_orbits, singlet_orbits, total in c2_rows
    )
    gate(
        "M02",
        "every reflection subgroup has 5 regular and 3 singlet orbits",
        burnside_ok and len(c2_rows) == 5,
        "312*5+3=1563",
    )

    generic_menu = sorted(set(row[1] for row in menu_rows))
    singlet_menu = sorted(set(row[2] for row in menu_rows))
    mixed_solutions = [
        (a, b)
        for a in generic_menu
        for b in singlet_menu
        if 312 * a + b == 629
    ]
    common_pairs = {(row[1], row[2]) for row in menu_rows}
    gate(
        "M03",
        "the mixed negative control has unique solution (2,5), unavailable to one common subgroup",
        mixed_solutions == [(2, 5)] and (2, 5) not in common_pairs,
        "mixed requires C5 on generic blocks and trivial M on singlet",
    )

    obstruction_ok = 629 not in total_menu
    gate(
        "M04",
        "source component count 629 is absent from the common-M target menu",
        obstruction_ok,
        "629 not in {313,625,1563,3125}",
    )

    zero = 0
    additive_inverse_ok = all(q5_add(value, q5_neg(value)) == zero for value in range(Q5_SIZE))
    haar_coset_mass = Fraction(1, Q5_SIZE)
    state_mass = Fraction(1, 2) * haar_coset_mass
    haar_ok = (
        additive_inverse_ok
        and Q5_SIZE * haar_coset_mass == 1
        and state_mass == Fraction(1, 6250)
        and 6250 * state_mass == 1
    )
    gate(
        "H01",
        "translation invariance gives uniform Haar mass on Q5 cosets",
        haar_ok,
        "coset=1/3125; half x coset=1/6250",
    )

    route_a_ok = obstruction_ok and generic_ok and singlet_ok and haar_ok
    gate(
        "D01",
        "the exact primary route excludes the fixed-depth-five fiberwise-bijective subclass",
        route_a_ok,
        "conditional on the written Mackey theorem and r>=2 scope",
    )

    print()
    passed = sum(ok for _, ok in GATES)
    total = len(GATES)
    print(f"SUMMARY {passed}/{total} PASS")
    if passed != total:
        print("DECISION PRIMARY ROUTE FALSIFIED OR BLOCKED")
        return 1
    print("DECISION PRIMARY ROUTE SURVIVES; INDEPENDENT BREAKER REQUIRED")
    print("PUBLIC ENTROPY-LAYER-BRIDGE REMAINS O / STOP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
