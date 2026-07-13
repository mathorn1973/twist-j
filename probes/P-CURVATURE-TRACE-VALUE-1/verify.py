#!/usr/bin/env python3
"""Exact verifier for P-CURVATURE-TRACE-VALUE-1.

This file is a pre-pin candidate. It must not be executed or imported before
its reviewed bytes are committed and pushed as the immutable preregistration
pin.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import sys


P = 5
D = 6
RULING_MERGE = "f9aac76ac9b1355fe45b9d675de7a8ec40cc9588"
RULING_SHA256 = "cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb"
THRESHOLD = Fraction(-21, 8)
STATES = tuple(product(range(P), repeat=D))
POWERS = tuple(P ** (D - 1 - i) for i in range(D))


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]
State = tuple[int, ...]


def state_id(x: State) -> int:
    return sum(value * weight for value, weight in zip(x, POWERS))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(D)) % P
            for j in range(D)
        )
        for i in range(D)
    )


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(D)) % P
        for i in range(D)
    )


def vector_add(left: Vector, right: Vector) -> Vector:
    return tuple((a + b) % P for a, b in zip(left, right))


@dataclass(frozen=True, order=True)
class Affine:
    matrix: Matrix
    vector: Vector

    def __call__(self, x: State) -> State:
        return vector_add(matrix_vector(self.matrix, x), self.vector)


IDENTITY_MATRIX = tuple(
    tuple(1 if i == j else 0 for j in range(D)) for i in range(D)
)
ZERO_VECTOR = (0,) * D
IDENTITY = Affine(IDENTITY_MATRIX, ZERO_VECTOR)


def affine(rows: tuple[tuple[int, ...], ...], vector: Vector) -> Affine:
    return Affine(
        tuple(tuple(value % P for value in row) for row in rows),
        tuple(value % P for value in vector),
    )


def compose(g: Affine, h: Affine) -> Affine:
    """Return g o h, so the returned map sends x to g(h(x))."""
    return Affine(
        matrix_multiply(g.matrix, h.matrix),
        vector_add(matrix_vector(g.matrix, h.vector), g.vector),
    )


A_GEN = affine(
    (
        (0, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    ZERO_VECTOR,
)

B_GEN = affine(
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 0),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    ZERO_VECTOR,
)

C_GEN = affine(
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 1),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, -1),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    (2, 1, 2, 1, 1, 0),
)

D_GEN = affine(
    tuple(
        tuple(-1 if i == j else 0 for j in range(D)) for i in range(D)
    ),
    (2, 1, 3, 4, 1, 1),
)

E_GEN = affine(
    tuple(
        tuple(-1 if i == j else 0 for j in range(D)) for i in range(D)
    ),
    (2, 1, 3, 4, 2, 1),
)

GENERATORS = (
    ("a", A_GEN),
    ("b", B_GEN),
    ("c", C_GEN),
    ("d", D_GEN),
    ("e", E_GEN),
)


def group_closure(generators: tuple[Affine, ...]) -> tuple[Affine, ...]:
    ordered_generators = tuple(sorted(generators))
    seen = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in ordered_generators:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return tuple(sorted(seen))


def group_is_closed(group: tuple[Affine, ...]) -> bool:
    members = set(group)
    return (
        IDENTITY in members
        and all(compose(left, right) in members for left in group for right in group)
    )


def group_has_inverses(group: tuple[Affine, ...]) -> bool:
    return all(
        any(
            compose(g, h) == IDENTITY and compose(h, g) == IDENTITY
            for h in group
        )
        for g in group
    )


def orbit_partition(
    group: tuple[Affine, ...],
) -> tuple[tuple[tuple[State, ...], ...], tuple[int, ...]]:
    labels = [-1] * len(STATES)
    orbits: list[tuple[State, ...]] = []
    for x in STATES:
        index = state_id(x)
        if labels[index] >= 0:
            continue
        orbit = tuple(sorted({g(x) for g in group}))
        orbit_index = len(orbits)
        for y in orbit:
            labels[state_id(y)] = orbit_index
        orbits.append(orbit)
    return tuple(orbits), tuple(labels)


def orbit_partition_is_exact(
    orbits: tuple[tuple[State, ...], ...], labels: tuple[int, ...]
) -> bool:
    flattened = tuple(sorted(x for orbit in orbits for x in orbit))
    least_states = tuple(orbit[0] for orbit in orbits)
    return (
        flattened == STATES
        and len(labels) == len(STATES)
        and all(labels[state_id(x)] == i for i, orbit in enumerate(orbits) for x in orbit)
        and least_states == tuple(sorted(least_states))
    )


def route_a(
    orbits: tuple[tuple[State, ...], ...],
    labels: tuple[int, ...],
    ac: Affine,
    ca: Affine,
) -> tuple[Fraction, int, int, bool, bool, bool]:
    sizes = tuple(len(orbit) for orbit in orbits)
    incidence: dict[tuple[int, int], int] = defaultdict(int)
    mapped_states = 0

    for j, orbit in enumerate(orbits):
        for x in orbit:
            incidence[(labels[state_id(ac(x))], j)] += 1
            incidence[(labels[state_id(ca(x))], j)] -= 1
            mapped_states += 1

    keys = set(incidence)
    keys.update((j, i) for i, j in incidence)
    skew = all(incidence.get((j, i), 0) == -incidence.get((i, j), 0) for i, j in keys)
    column_zero = all(
        sum(incidence.get((i, j), 0) for i in range(len(orbits))) == 0
        for j in range(len(orbits))
    )
    row_zero = all(
        sum(incidence.get((i, j), 0) for j in range(len(orbits))) == 0
        for i in range(len(orbits))
    )

    trace = Fraction(0)
    active_entries = 0
    for (i, j), value in sorted(incidence.items()):
        if value:
            active_entries += 1
            trace -= Fraction(value * value, sizes[i] * sizes[j])

    return trace, active_entries, mapped_states, skew, row_zero, column_zero


def matrix_rank_mod_p(rows: tuple[tuple[int, ...], ...]) -> int:
    matrix = [[value % P for value in row] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    rank = 0
    for column in range(column_count):
        pivot = next(
            (i for i in range(rank, row_count) if matrix[i][column] % P),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, P)
        matrix[rank] = [(inverse * value) % P for value in matrix[rank]]
        for i in range(row_count):
            if i != rank and matrix[i][column] % P:
                factor = matrix[i][column] % P
                matrix[i] = [
                    (matrix[i][j] - factor * matrix[rank][j]) % P
                    for j in range(column_count)
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def fixed_point_count(g: Affine) -> tuple[int, bool]:
    coefficient = tuple(
        tuple(
            (g.matrix[i][j] - (1 if i == j else 0)) % P
            for j in range(D)
        )
        for i in range(D)
    )
    augmented = tuple(
        coefficient[i] + ((-g.vector[i]) % P,) for i in range(D)
    )
    rank_coefficient = matrix_rank_mod_p(coefficient)
    rank_augmented = matrix_rank_mod_p(augmented)
    if rank_coefficient != rank_augmented:
        return 0, True
    count = P ** (D - rank_coefficient)
    return count, 0 <= rank_coefficient <= D


def is_power_of_five_or_zero(value: int) -> bool:
    if value == 0:
        return True
    while value % P == 0:
        value //= P
    return value == 1


def route_b(
    group: tuple[Affine, ...], ac: Affine, ca: Affine
) -> tuple[Fraction, int, bool]:
    total = 0
    term_count = 0
    fixed_point_audit = True
    signed_words = (
        (1, ac, ac),
        (-1, ac, ca),
        (-1, ca, ac),
        (1, ca, ca),
    )
    for h in group:
        for k in group:
            for sign, left_word, right_word in signed_words:
                word = compose(compose(compose(h, left_word), k), right_word)
                fixed_points, rank_ok = fixed_point_count(word)
                total += sign * fixed_points
                term_count += 1
                fixed_point_audit = (
                    fixed_point_audit
                    and rank_ok
                    and is_power_of_five_or_zero(fixed_points)
                )
    return Fraction(total, len(group) ** 2), term_count, fixed_point_audit


def indicator_commutator_value(
    x: State,
    orbit_label: int,
    labels: tuple[int, ...],
    ac: Affine,
    ca: Affine,
) -> int:
    return int(labels[state_id(ca(x))] == orbit_label) - int(
        labels[state_id(ac(x))] == orbit_label
    )


def polynomial_multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


def historical_checksum() -> tuple[int, tuple[int, ...]]:
    polynomial = polynomial_multiply(
        polynomial_multiply((1, 0, 1), (1, 0, 3, 0, 1)),
        (1, 0, 7, 0, 1),
    )
    return -2 * polynomial[8], polynomial


def format_status(value: bool) -> str:
    return "PASS" if value else "FAIL"


def format_fraction(value: Fraction) -> str:
    return f"numerator={value.numerator} denominator={value.denominator}"


def compute() -> tuple[list[tuple[str, bool]], dict[str, object]]:
    carrier_ok = (
        len(STATES) == P**D
        and len({state_id(x) for x in STATES}) == len(STATES)
        and all(len(x) == D and all(0 <= value < P for value in x) for x in STATES)
    )

    involutions = tuple(compose(g, g) == IDENTITY for _, g in GENERATORS)
    composition_ok = all(
        compose(g, h)(x) == g(h(x))
        for _, g in GENERATORS
        for _, h in GENERATORS
        for x in STATES
    )
    koopman_ok = composition_ok and all(
        compose(compose(g, h), compose(h, g)) == IDENTITY
        and compose(compose(h, g), compose(g, h)) == IDENTITY
        for _, g in GENERATORS
        for _, h in GENERATORS
    )

    ac = compose(A_GEN, C_GEN)
    ca = compose(C_GEN, A_GEN)
    raw_skew_ok = compose(ac, ca) == IDENTITY and compose(ca, ac) == IDENTITY

    group = group_closure((B_GEN, D_GEN))
    group_ok = (
        len(group) == 20
        and group_is_closed(group)
        and group_has_inverses(group)
        and group == tuple(sorted(group))
    )

    orbits, labels = orbit_partition(group)
    census = Counter(len(orbit) for orbit in orbits)
    partition_ok = orbit_partition_is_exact(orbits, labels)
    census_ok = census == Counter({5: 1, 10: 74, 20: 744})
    invariant_dimension = len(orbits)
    rank_p = invariant_dimension - 1
    dimensions_ok = invariant_dimension == 819 and rank_p == 818
    projector_ok = group_ok and partition_ok

    zero_label = labels[state_id((0, 0, 0, 0, 0, 0))]
    witness_x = (0, 0, 1, 3, 0, 1)
    witness_y = (2, 1, 2, 1, 1, 0)
    witness_x_value = indicator_commutator_value(witness_x, zero_label, labels, ac, ca)
    witness_y_value = indicator_commutator_value(witness_y, zero_label, labels, ac, ca)
    witness_ok = (
        labels[state_id(witness_x)] == labels[state_id(witness_y)]
        and witness_x_value == 0
        and witness_y_value == -1
    )

    (
        trace_a,
        active_entries,
        mapped_states,
        incidence_skew,
        row_zero,
        column_zero,
    ) = route_a(orbits, labels, ac, ca)
    route_a_complete = (
        mapped_states == len(STATES)
        and isinstance(trace_a, Fraction)
    )
    constant_both_sides_ok = row_zero and column_zero
    compression_identities_ok = (
        projector_ok and raw_skew_ok and constant_both_sides_ok
    )
    k_endomorphism_ok = projector_ok and constant_both_sides_ok
    k_skew_ok = incidence_skew

    trace_b, word_terms, fixed_point_audit = route_b(group, ac, ca)
    route_b_complete = (
        word_terms == 1600
        and fixed_point_audit
        and isinstance(trace_b, Fraction)
    )

    agreement = trace_a == trace_b
    checksum, polynomial = historical_checksum()
    expected_polynomial = (1, 0, 11, 0, 33, 0, 33, 0, 11, 0, 1)
    checksum_ok = checksum == -22 and polynomial == expected_polynomial

    affine_integer_ok = all(
        type(value) is int
        for affine_map in tuple(g for _, g in GENERATORS) + group
        for row in affine_map.matrix
        for value in row
    ) and all(
        type(value) is int
        for affine_map in tuple(g for _, g in GENERATORS) + group
        for value in affine_map.vector
    )
    exact_arithmetic_ok = (
        affine_integer_ok
        and isinstance(trace_a, Fraction)
        and isinstance(trace_b, Fraction)
        and fixed_point_audit
    )
    deterministic_output_ok = (
        tuple(sorted(group)) == group
        and tuple(orbit[0] for orbit in orbits)
        == tuple(sorted(orbit[0] for orbit in orbits))
        and isinstance(trace_a.numerator, int)
        and isinstance(trace_b.numerator, int)
    )

    audits = [
        ("I01", carrier_ok and all(involutions)),
        ("I02", composition_ok and koopman_ok),
        ("I03", group_ok and partition_ok and census_ok),
        ("I04", projector_ok and dimensions_ok),
        ("I05", witness_ok),
        (
            "I06",
            raw_skew_ok
            and constant_both_sides_ok
            and compression_identities_ok,
        ),
        ("I07", k_endomorphism_ok and k_skew_ok),
        ("I08", route_a_complete and incidence_skew),
        ("I09", route_b_complete),
        ("I10", agreement),
        ("I11", checksum_ok),
        ("I12", exact_arithmetic_ok),
        ("I13", deterministic_output_ok),
    ]
    report: dict[str, object] = {
        "involutions": sum(involutions),
        "composition_ok": composition_ok,
        "koopman_ok": koopman_ok,
        "group_ok": group_ok,
        "group_order": len(group),
        "partition_ok": partition_ok,
        "census_ok": census_ok,
        "census": census,
        "projector_ok": projector_ok,
        "invariant_dimension": invariant_dimension,
        "rank_p": rank_p,
        "witness_ok": witness_ok,
        "witness_x_value": witness_x_value,
        "witness_y_value": witness_y_value,
        "compression_identities_ok": compression_identities_ok,
        "k_skew_ok": k_skew_ok,
        "trace_a": trace_a,
        "active_entries": active_entries,
        "mapped_states": mapped_states,
        "trace_b": trace_b,
        "word_terms": word_terms,
        "agreement": agreement,
        "checksum": checksum,
        "polynomial": polynomial,
    }
    return audits, report


def print_report(audits: list[tuple[str, bool]], report: dict[str, object]) -> int:
    passed = sum(value for _, value in audits)
    complete = passed == len(audits)
    census = report["census"]
    assert isinstance(census, Counter)
    trace_a = report["trace_a"]
    trace_b = report["trace_b"]
    assert isinstance(trace_a, Fraction)
    assert isinstance(trace_b, Fraction)

    print("P-CURVATURE-TRACE-VALUE-1")
    print(f"RULING merge={RULING_MERGE} sha256={RULING_SHA256}")
    print(f"CARRIER states={len(STATES)}")
    print(
        "GENERATORS "
        f"{format_status(report['involutions'] == 5)} involutions={report['involutions']}"
    )
    print(f"KOOPMAN {format_status(bool(report['koopman_ok']))}")
    print(
        "H "
        f"{format_status(bool(report['group_ok']) and bool(report['partition_ok']) and bool(report['census_ok']))} "
        f"order={report['group_order']} "
        f"orbits=5:{census.get(5, 0)},10:{census.get(10, 0)},20:{census.get(20, 0)}"
    )
    print(
        "PROJECTOR "
        f"{format_status(bool(report['projector_ok']) and report['invariant_dimension'] == 819 and report['rank_p'] == 818)} "
        f"invariant_dim={report['invariant_dimension']} rank_P={report['rank_p']}"
    )
    print(
        "WITNESS "
        f"{format_status(bool(report['witness_ok']))} "
        f"x_value={report['witness_x_value']} y_value={report['witness_y_value']}"
    )
    print(
        f"COMPRESSION {format_status(bool(report['compression_identities_ok']))}"
    )
    print(f"SKEW {format_status(bool(report['k_skew_ok']))}")
    print(
        f"ROUTE_A {format_fraction(trace_a)} "
        f"active_entries={report['active_entries']} mapped_states={report['mapped_states']}"
    )
    print(
        f"ROUTE_B {format_fraction(trace_b)} word_terms={report['word_terms']}"
    )
    print(f"AGREEMENT {format_status(bool(report['agreement']))}")
    polynomial = report["polynomial"]
    assert isinstance(polynomial, tuple)
    polynomial_text = ",".join(str(value) for value in polynomial)
    print(
        "HISTORICAL_CHECKSUM "
        f"value={report['checksum']} polynomial_ascending={polynomial_text} "
        "scope=historical-only"
    )
    print("AUDIT " + " ".join(f"{name}={'P' if value else 'F'}" for name, value in audits))
    print(f"AUDIT {'PASS' if complete else 'FAIL'} {passed}/{len(audits)}")

    if not complete:
        print("DECISION STOP")
        print("RESULT INVALID")
        return 1
    if trace_a != THRESHOLD:
        print("DECISION NEGATIVE")
    else:
        print("DECISION TRACE-SURVIVES")
    print("RESULT VALID")
    return 0


def print_exception_stop(error: BaseException) -> int:
    print("P-CURVATURE-TRACE-VALUE-1")
    print(f"RULING merge={RULING_MERGE} sha256={RULING_SHA256}")
    print(f"ERROR type={type(error).__name__}")
    print("AUDIT " + " ".join(f"I{i:02d}=F" for i in range(1, 14)))
    print("AUDIT FAIL 0/13")
    print("DECISION STOP")
    print("RESULT INVALID")
    return 1


def main() -> int:
    try:
        audits, report = compute()
        return print_report(audits, report)
    except BaseException as error:
        if isinstance(error, (KeyboardInterrupt, SystemExit)):
            raise
        return print_exception_stop(error)


if __name__ == "__main__":
    sys.exit(main())
