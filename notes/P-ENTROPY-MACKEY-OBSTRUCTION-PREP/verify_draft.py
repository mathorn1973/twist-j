#!/usr/bin/env python3
"""Combined exact verifier for P-ENTROPY-MACKEY-OBSTRUCTION.

The source leg derives the integral cyclotomic quotient and its induced J
permutation without an imported representative table.  The inherited target
leg reconstructs the finite target solely from the public generator table,
constructs one global D_5 before component traversal, and uses only the frozen
identity gauge.  The combined decision is the narrow, confirmatory obstruction
surface preregistered in this directory; it makes no independent-method claim
and no claim about all of A_A or ENTROPY-LAYER-BRIDGE.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd
import sys
from typing import Callable, Iterable, Sequence


PROBE_ID = "P-ENTROPY-MACKEY-OBSTRUCTION"
PUBLIC_BASIS = "Public Canon v30"
PUBLIC_SCOPE_ISSUE = 241

P = 5
STATE_WIDTH = 6
CENSUS_WARMUP = 400
CENSUS_WINDOW = 300

State = tuple[int, int, int, int, int, int]
Elem = tuple[int, int]  # r^k s^f in D_5, with k mod 5 and f in {0,1}
Edge = tuple[int, int]  # (previous half, current bit)
Vector4 = tuple[int, int, int, int]
Matrix4 = tuple[tuple[int, int, int, int], ...]

ID: Elem = (0, 0)
ELEMENTS: tuple[Elem, ...] = tuple((k, 0) for k in range(5)) + tuple(
    (k, 1) for k in range(5)
)
EDGE_ORDER: tuple[Edge, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
GAMMA: tuple[Elem, ...] = (ID,)


class InstrumentDefect(RuntimeError):
    """A frozen control or structural instrument condition failed."""


class InputReconstructionDefect(RuntimeError):
    """The public carrier or recurrent-core reconstruction disagreed."""


class TargetGateFailure(RuntimeError):
    """A real-target gate disagreed with the frozen public target specification."""

    def __init__(self, gate: str, message: str) -> None:
        super().__init__(message)
        self.gate = gate


class SourceGateFailure(RuntimeError):
    """A real-source gate disagreed with the frozen public source specification."""

    def __init__(self, gate: str, message: str) -> None:
        super().__init__(message)
        self.gate = gate


class LabelExtractionFailure(RuntimeError):
    """An edge is not represented by exactly one declared D_5 element."""


def require_instrument(condition: bool, message: str) -> None:
    if not condition:
        raise InstrumentDefect(message)


def require_target(condition: bool, gate: str, message: str) -> None:
    if not condition:
        if gate == "C1":
            raise InputReconstructionDefect(message)
        raise TargetGateFailure(gate, message)


def require_source(condition: bool, gate: str, message: str) -> None:
    if not condition:
        raise SourceGateFailure(gate, message)


# ---------------------------------------------------------------------------
# Abstract D_5 and the frozen gauge


def elem_mul(left: Elem, right: Elem) -> Elem:
    """Multiply r^k s^f * r^l s^g with s r s = r^-1."""

    k, f = left
    ell, g = right
    signed_ell = ell if f == 0 else -ell
    return ((k + signed_ell) % 5, (f + g) % 2)


def elem_pow(element: Elem, exponent: int) -> Elem:
    require_instrument(exponent >= 0, "negative D_5 exponent")
    value = ID
    for _ in range(exponent):
        value = elem_mul(value, element)
    return value


def elem_inv(element: Elem) -> Elem:
    candidates = [
        candidate
        for candidate in ELEMENTS
        if elem_mul(element, candidate) == ID
        and elem_mul(candidate, element) == ID
    ]
    require_instrument(len(candidates) == 1, "D_5 inverse is not unique")
    return candidates[0]


def elem_order(element: Elem) -> int:
    value = ID
    for order in range(1, 11):
        value = elem_mul(value, element)
        if value == ID:
            return order
    raise InstrumentDefect("D_5 element order exceeds ten")


def elem_conjugate(gauge: Elem, label: Elem) -> Elem:
    return elem_mul(elem_mul(gauge, label), elem_inv(gauge))


def generated_subgroup(generators: Iterable[Elem]) -> frozenset[Elem]:
    known = {ID}
    pending = list(generators)
    while pending:
        item = pending.pop()
        if item not in known:
            known.add(item)
        snapshot = tuple(known)
        for left in snapshot:
            for right in snapshot:
                value = elem_mul(left, right)
                if value not in known:
                    known.add(value)
                    pending.append(value)
    return frozenset(known)


def elem_text(element: Elem) -> str:
    k, f = element
    if f == 0:
        return "1" if k == 0 else f"r^{k}"
    return "s" if k == 0 else f"r^{k}*s"


def tuple_text(labels: Sequence[Elem]) -> str:
    entries = []
    for edge, label in zip(EDGE_ORDER, labels):
        entries.append(f"({edge[0]},{edge[1]})={elem_text(label)}")
    return "[" + ", ".join(entries) + "]"


def gauge_for_component(_component_key: str) -> Elem:
    """Frozen rule: every component receives the identity gauge.

    The function has no access to an edge label, point, component carrier, or
    search result.  Gamma={1} is a proper subgroup of D_5.
    """

    return ID


def apply_component_gauge(labels: Sequence[Elem], gauge: Elem) -> tuple[Elem, ...]:
    require_instrument(gauge in GAMMA, "gauge rule returned an element outside Gamma")
    return tuple(elem_conjugate(gauge, label) for label in labels)


def validate_abstract_d5_and_gauge() -> None:
    require_instrument(len(ELEMENTS) == 10, "abstract D_5 does not have ten elements")
    require_instrument(len(set(ELEMENTS)) == 10, "abstract D_5 elements repeat")
    for left in ELEMENTS:
        require_instrument(elem_mul(ID, left) == left, "left identity failed")
        require_instrument(elem_mul(left, ID) == left, "right identity failed")
        inverse = elem_inv(left)
        require_instrument(elem_mul(left, inverse) == ID, "right inverse failed")
        require_instrument(elem_mul(inverse, left) == ID, "left inverse failed")
        for middle in ELEMENTS:
            for right in ELEMENTS:
                require_instrument(
                    elem_mul(elem_mul(left, middle), right)
                    == elem_mul(left, elem_mul(middle, right)),
                    "D_5 associativity failed",
                )

    orders = Counter(elem_order(element) for element in ELEMENTS)
    require_instrument(
        orders == Counter({1: 1, 2: 5, 5: 4}),
        "abstract D_5 order census failed",
    )

    gamma_set = frozenset(GAMMA)
    require_instrument(ID in gamma_set, "Gamma omits the identity")
    require_instrument(len(gamma_set) < len(ELEMENTS), "Gamma is not proper")
    for left in gamma_set:
        require_instrument(elem_inv(left) in gamma_set, "Gamma is not inverse closed")
        for right in gamma_set:
            require_instrument(elem_mul(left, right) in gamma_set, "Gamma is not closed")

    # Exercise the general conjugation implementation even though the frozen
    # target gauge is the identity subgroup.
    for gauge in ELEMENTS:
        inverse = elem_inv(gauge)
        for left in ELEMENTS:
            require_instrument(
                elem_conjugate(inverse, elem_conjugate(gauge, left)) == left,
                "gauge conjugation is not invertible",
            )
            for right in ELEMENTS:
                require_instrument(
                    elem_conjugate(gauge, elem_mul(left, right))
                    == elem_mul(
                        elem_conjugate(gauge, left),
                        elem_conjugate(gauge, right),
                    ),
                    "gauge conjugation is not a homomorphism",
                )


# ---------------------------------------------------------------------------
# Label extraction shared by the mandatory controls and the real target


PointsFunction = Callable[[str, int], Sequence[object]]
EdgeMapFunction = Callable[[str, int, int, object], object]
ReferenceFunction = Callable[[str, int, object], object]
ActionFunction = Callable[[Elem, object], object]


def extract_edge_label(
    component_key: str,
    previous_half: int,
    current_bit: int,
    points: PointsFunction,
    edge_map: EdgeMapFunction,
    to_reference: ReferenceFunction,
    action: ActionFunction,
) -> Elem:
    source = tuple(points(component_key, previous_half))
    if not source:
        raise LabelExtractionFailure(
            f"component {component_key} has an empty half {previous_half}"
        )
    candidates = []
    for candidate in ELEMENTS:
        agrees = True
        for point in source:
            actual = to_reference(
                component_key,
                current_bit,
                edge_map(component_key, previous_half, current_bit, point),
            )
            predicted = action(
                candidate,
                to_reference(component_key, previous_half, point),
            )
            if actual != predicted:
                agrees = False
                break
        if agrees:
            candidates.append(candidate)
    if len(candidates) != 1:
        rendered = ",".join(elem_text(item) for item in candidates)
        raise LabelExtractionFailure(
            f"component={component_key} edge=({previous_half},{current_bit}) "
            f"candidate_count={len(candidates)} candidates={rendered}"
        )
    return candidates[0]


def common_cocycle_gate(
    component_keys: Sequence[str],
    points: PointsFunction,
    edge_map: EdgeMapFunction,
    to_reference: ReferenceFunction,
    action: ActionFunction,
) -> tuple[bool, dict[str, tuple[Elem, ...]], dict[str, tuple[Elem, ...]]]:
    raw: dict[str, tuple[Elem, ...]] = {}
    gauged: dict[str, tuple[Elem, ...]] = {}
    for component_key in component_keys:
        labels = tuple(
            extract_edge_label(
                component_key,
                previous_half,
                current_bit,
                points,
                edge_map,
                to_reference,
                action,
            )
            for previous_half, current_bit in EDGE_ORDER
        )
        raw[component_key] = labels
        gauge = gauge_for_component(component_key)
        gauged[component_key] = apply_component_gauge(labels, gauge)

    first = gauged[component_keys[0]]
    accepted = all(gauged[key] == first for key in component_keys)
    return accepted, raw, gauged


def synthetic_interface(
    specifications: dict[str, tuple[Elem, ...]],
) -> tuple[
    tuple[str, ...],
    PointsFunction,
    EdgeMapFunction,
    ReferenceFunction,
    ActionFunction,
]:
    keys = tuple(sorted(specifications))

    def points(_key: str, _half: int) -> Sequence[object]:
        return ELEMENTS

    def edge_map(key: str, previous_half: int, current_bit: int, point: object) -> object:
        coordinate = point
        require_instrument(coordinate in ELEMENTS, "synthetic point is not in D_5")
        edge_index = EDGE_ORDER.index((previous_half, current_bit))
        label = specifications[key][edge_index]
        return elem_mul(label, coordinate)  # type: ignore[arg-type]

    def to_reference(_key: str, _half: int, point: object) -> object:
        return point

    def action(element: Elem, point: object) -> object:
        require_instrument(point in ELEMENTS, "synthetic reference point is not in D_5")
        return elem_mul(element, point)  # type: ignore[arg-type]

    return keys, points, edge_map, to_reference, action


def run_synthetic_case(
    specifications: dict[str, tuple[Elem, ...]],
) -> tuple[bool, dict[str, tuple[Elem, ...]], dict[str, tuple[Elem, ...]]]:
    keys, points, edge_map, to_reference, action = synthetic_interface(specifications)
    return common_cocycle_gate(keys, points, edge_map, to_reference, action)


def run_mandatory_controls() -> None:
    # N1: four regular two-half components.  Each of the four edge fields is
    # pairwise different across the four components; both own edges are
    # reflections in every component.
    n1: dict[str, tuple[Elem, ...]] = {}
    for index in range(4):
        n1[f"N1-{index}"] = (
            (index, 1),
            (index, 0),
            ((2 * index) % 5, 0),
            ((index + 1) % 5, 1),
        )
    for position in range(4):
        require_instrument(
            len({n1[key][position] for key in sorted(n1)}) == 4,
            "N1 does not vary every edge field across components",
        )
    for labels in n1.values():
        require_instrument(labels[0][1] == 1, "N1 first own edge is not a reflection")
        require_instrument(labels[3][1] == 1, "N1 second own edge is not a reflection")
        require_instrument(labels[0] != labels[3], "N1 own reflections are not distinct")
    n1_accepted, _n1_raw, _n1_gauged = run_synthetic_case(n1)
    print(
        "CONTROL N1 components=4 construction=fieldwise-different "
        f"expected=REJECT observed={'ACCEPT' if n1_accepted else 'REJECT'} "
        f"result={'FAIL' if n1_accepted else 'PASS'}"
    )
    require_instrument(not n1_accepted, "N1 was accepted")

    # N2: exactly one of four otherwise identical components changes exactly
    # one cross edge from the identity to a reflection.
    common = ((4, 1), ID, ID, (0, 1))
    n2 = {f"N2-{index}": common for index in range(4)}
    changed = list(common)
    changed[1] = (2, 1)
    n2["N2-3"] = tuple(changed)
    differences = [
        (key, position)
        for key in sorted(n2)
        for position in range(4)
        if n2[key][position] != common[position]
    ]
    require_instrument(
        differences == [("N2-3", 1)],
        "N2 does not contain exactly one single-edge perturbation",
    )
    require_instrument(
        n2["N2-3"][1][1] == 1,
        "N2 perturbation is not a reflection",
    )
    n2_accepted, _n2_raw, _n2_gauged = run_synthetic_case(n2)
    print(
        "CONTROL N2 components=4 perturbation=one-cross-edge-by-one-reflection "
        f"expected=REJECT observed={'ACCEPT' if n2_accepted else 'REJECT'} "
        f"result={'FAIL' if n2_accepted else 'PASS'}"
    )
    require_instrument(not n2_accepted, "N2 was accepted")

    # N3: four components share the same cocycle exactly.
    n3 = {f"N3-{index}": common for index in range(4)}
    n3_accepted, _n3_raw, n3_gauged = run_synthetic_case(n3)
    require_instrument(
        len(set(n3_gauged.values())) == 1,
        "N3 extracted more than one gauged tuple",
    )
    print(
        "CONTROL N3 components=4 construction=one-common-cocycle "
        f"expected=ACCEPT observed={'ACCEPT' if n3_accepted else 'REJECT'} "
        f"result={'PASS' if n3_accepted else 'FAIL'}"
    )
    require_instrument(n3_accepted, "N3 was rejected")


# ---------------------------------------------------------------------------
# Integral source leg and its synthetic controls


I4: Matrix4 = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
C4: Matrix4 = (
    (0, 0, 0, -1),
    (1, 0, 0, -1),
    (0, 1, 0, -1),
    (0, 0, 1, -1),
)
EXPECTED_A: Matrix4 = (
    (-5, 15, -20, 15),
    (-10, 10, -5, -5),
    (5, 5, -10, 10),
    (-15, 20, -15, 5),
)
EXPECTED_M: Matrix4 = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)
EXPECTED_DETERMINANTAL_DIVISORS = (5, 25, 125, 3125)
EXPECTED_SMITH_FACTORS = (5, 5, 5, 25)
EXPECTED_J_CYCLES = ((1, 1), (4, 1), (20, 156))
EXPECTED_SOURCE_COUNTS = (158, 315, 629, 629, 629, 629, 629, 629, 629)


def matrix_add(left: Matrix4, right: Matrix4) -> Matrix4:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(4))
        for i in range(4)
    )


def matrix_sub(left: Matrix4, right: Matrix4) -> Matrix4:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(4))
        for i in range(4)
    )


def matrix_mul(left: Matrix4, right: Matrix4) -> Matrix4:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(4))
            for j in range(4)
        )
        for i in range(4)
    )


def matrix_pow(base: Matrix4, exponent: int) -> Matrix4:
    require_instrument(exponent >= 0, "negative matrix exponent")
    value = I4
    factor = base
    power = exponent
    while power:
        if power & 1:
            value = matrix_mul(value, factor)
        factor = matrix_mul(factor, factor)
        power //= 2
    return value


def matrix_vector(matrix: Matrix4, vector: Vector4) -> Vector4:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(4))
        for i in range(4)
    )  # type: ignore[return-value]


def determinant(rows: Sequence[Sequence[int]]) -> int:
    """Fraction-free Bareiss determinant, with exact-division checks."""

    size = len(rows)
    require_instrument(
        all(len(row) == size for row in rows),
        "determinant input is not square",
    )
    if size == 0:
        return 1
    if size == 1:
        return int(rows[0][0])
    work = [list(map(int, row)) for row in rows]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (
                row
                for row in range(pivot_index, size)
                if work[row][pivot_index] != 0
            ),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                require_instrument(
                    numerator % previous == 0,
                    "Bareiss division is not exact",
                )
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def submatrix(
    matrix: Matrix4,
    row_indices: Sequence[int],
    column_indices: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(matrix[row][column] for column in column_indices)
        for row in row_indices
    )


def determinantal_divisors(matrix: Matrix4) -> tuple[int, int, int, int]:
    values: list[int] = []
    for size in range(1, 5):
        divisor = 0
        for rows in combinations(range(4), size):
            for columns in combinations(range(4), size):
                divisor = gcd(
                    divisor,
                    abs(determinant(submatrix(matrix, rows, columns))),
                )
        require_instrument(divisor > 0, "determinantal divisor vanished")
        values.append(divisor)
    return tuple(values)  # type: ignore[return-value]


def smith_factors(divisors: Sequence[int]) -> tuple[int, int, int, int]:
    require_instrument(len(divisors) == 4, "wrong determinantal-divisor count")
    previous = 1
    factors: list[int] = []
    for divisor in divisors:
        require_instrument(divisor % previous == 0, "invalid determinantal divisors")
        factors.append(divisor // previous)
        previous = divisor
    require_instrument(
        all(factors[index + 1] % factors[index] == 0 for index in range(3)),
        "Smith factors are not divisibility ordered",
    )
    return tuple(factors)  # type: ignore[return-value]


def adjugate(matrix: Matrix4) -> Matrix4:
    entries = [[0 for _ in range(4)] for _ in range(4)]
    for row in range(4):
        for column in range(4):
            minor_rows = tuple(index for index in range(4) if index != row)
            minor_columns = tuple(index for index in range(4) if index != column)
            cofactor = determinant(submatrix(matrix, minor_rows, minor_columns))
            if (row + column) % 2:
                cofactor = -cofactor
            entries[column][row] = cofactor
    return tuple(tuple(row) for row in entries)  # type: ignore[return-value]


def scalar_matrix(scalar: int) -> Matrix4:
    return tuple(
        tuple(scalar if row == column else 0 for column in range(4))
        for row in range(4)
    )


def vector_add(left: Vector4, right: Vector4) -> Vector4:
    return tuple(left[index] + right[index] for index in range(4))  # type: ignore[return-value]


def quotient_signature(
    adjoint: Matrix4,
    modulus: int,
    vector: Vector4,
) -> tuple[int, int, int, int]:
    return tuple(value % modulus for value in matrix_vector(adjoint, vector))


def quotient_representatives(
    adjoint: Matrix4,
    modulus: int,
) -> dict[tuple[int, int, int, int], Vector4]:
    zero: Vector4 = (0, 0, 0, 0)
    basis: tuple[Vector4, ...] = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    )
    zero_signature = quotient_signature(adjoint, modulus, zero)
    representatives = {zero_signature: zero}
    pending: deque[Vector4] = deque((zero,))
    while pending:
        current = pending.popleft()
        for step in basis:
            candidate = vector_add(current, step)
            signature = quotient_signature(adjoint, modulus, candidate)
            if signature not in representatives:
                representatives[signature] = candidate
                pending.append(candidate)
                require_instrument(
                    len(representatives) <= modulus,
                    "quotient enumeration exceeded determinant bound",
                )
    return representatives


def permutation_cycle_census(
    mapping: dict[tuple[int, int, int, int], tuple[int, int, int, int]],
    source_gate: str | None = None,
) -> tuple[tuple[int, int], ...]:
    domain = set(mapping)
    image = set(mapping.values())
    if domain != image:
        missing = min(domain - image, default=None)
        unexpected = min(image - domain, default=None)
        message = (
            "induced J action is not a permutation "
            f"domain_size={len(domain)} image_size={len(image)} "
            f"first_missing_image={missing} first_unexpected_image={unexpected}"
        )
        if source_gate is None:
            raise InstrumentDefect(message)
        raise SourceGateFailure(source_gate, message)

    visited: set[tuple[int, int, int, int]] = set()
    census: Counter[int] = Counter()
    for start in sorted(mapping):
        if start in visited:
            continue
        current = start
        length = 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = mapping[current]
        require_instrument(
            current == start,
            "induced J traversal certificate does not close "
            f"start={start} observed_return={current} length={length}",
        )
        census[length] += 1
    require_instrument(
        len(visited) == len(mapping),
        "induced J traversal certificate misses quotient classes "
        f"visited={len(visited)} domain={len(mapping)}",
    )
    return tuple(sorted(census.items()))


def component_count_from_census(
    census: Sequence[tuple[int, int]],
    level: int,
) -> int:
    factor_size = 2**level
    return sum(multiplicity * gcd(length, factor_size) for length, multiplicity in census)


def two_adic_part(value: int) -> int:
    part = 1
    current = value
    while current % 2 == 0:
        part *= 2
        current //= 2
    return part


def direct_product_orbit_count(length: int, factor_size: int, broken: bool) -> int:
    unseen = set(product(range(length), range(factor_size)))
    count = 0
    while unseen:
        start = min(unseen)
        current = start
        orbit: set[tuple[int, int]] = set()
        while current not in orbit:
            orbit.add(current)
            if broken:
                current = ((current[0] + 1) % length, current[1])
            else:
                current = (
                    (current[0] + 1) % length,
                    (current[1] + 1) % factor_size,
                )
        unseen.difference_update(orbit)
        count += 1
    return count


def add_moduli(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
    moduli: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    return tuple(
        (left[index] + right[index]) % moduli[index]
        for index in range(4)
    )  # type: ignore[return-value]


def translation_action_regularity(
    acting_elements: Sequence[tuple[int, int, int, int]],
    carrier_elements: Sequence[tuple[int, int, int, int]],
    moduli: tuple[int, int, int, int],
) -> tuple[bool, str]:
    acting = frozenset(acting_elements)
    carrier = frozenset(carrier_elements)
    zero = (0, 0, 0, 0)
    if len(acting) != len(acting_elements):
        duplicate = min(
            element
            for element, count in Counter(acting_elements).items()
            if count > 1
        )
        return False, (
            "duplicate_acting_element "
            f"input_size={len(acting_elements)} unique_size={len(acting)} "
            f"first_duplicate={duplicate}"
        )
    if len(carrier) != len(carrier_elements):
        duplicate = min(
            element
            for element, count in Counter(carrier_elements).items()
            if count > 1
        )
        return False, (
            "duplicate_carrier_element "
            f"input_size={len(carrier_elements)} unique_size={len(carrier)} "
            f"first_duplicate={duplicate}"
        )
    if zero not in acting or zero not in carrier:
        return False, (
            "zero_missing "
            f"acting_has_zero={zero in acting} carrier_has_zero={zero in carrier}"
        )
    ordered_acting = tuple(sorted(acting))
    for element in ordered_acting:
        inverse = tuple(
            (-element[index]) % moduli[index]
            for index in range(4)
        )
        if inverse not in acting:
            return False, f"missing_inverse element={element} inverse={inverse}"
        if add_moduli(zero, element, moduli) != element:
            return False, f"zero_action_failed element={element}"
        for other in ordered_acting:
            total = add_moduli(element, other, moduli)
            if total not in acting:
                return False, (
                    "nonclosed_translation_group "
                    f"left={element} right={other} sum={total}"
                )
    zero_orbit = {
        add_moduli(element, zero, moduli)
        for element in ordered_acting
    }
    if zero_orbit != carrier:
        return False, (
            "nontransitive_translation "
            f"orbit_size={len(zero_orbit)} carrier_size={len(carrier)} "
            f"first_missing={min(carrier - zero_orbit, default=None)} "
            f"first_unexpected={min(zero_orbit - carrier, default=None)}"
        )
    if len(zero_orbit) != len(acting):
        return False, (
            "nonfree_translation "
            f"orbit_size={len(zero_orbit)} acting_size={len(acting)}"
        )
    return True, "regular"


def run_source_controls() -> None:
    good: Matrix4 = (
        (5, 0, 0, 0),
        (0, 5, 0, 0),
        (0, 0, 5, 0),
        (0, 0, 0, 25),
    )
    bad: Matrix4 = (
        (4, 0, 0, 0),
        (0, 5, 0, 0),
        (0, 0, 5, 0),
        (0, 0, 0, 25),
    )
    good_factors = smith_factors(determinantal_divisors(good))
    bad_factors = smith_factors(determinantal_divisors(bad))
    require_instrument(good_factors == EXPECTED_SMITH_FACTORS, "N4 good lattice rejected")
    require_instrument(bad_factors != EXPECTED_SMITH_FACTORS, "N4 bad lattice accepted")
    print("CONTROL N4 lattice_changed expected=REJECT observed=REJECT result=PASS")

    identity_points = tuple((index, 0, 0, 0) for index in range(3125))
    identity_mapping = {point: point for point in identity_points}
    identity_census = permutation_cycle_census(identity_mapping)
    require_instrument(identity_census != EXPECTED_J_CYCLES, "N5 identity cycle census accepted")
    print("CONTROL N5 identity_J expected=REJECT observed=REJECT result=PASS")

    plateau_census = ((1, 1), (4, 1), (10, 2), (20, 155))
    plateau_counts = tuple(
        component_count_from_census(plateau_census, level)
        for level in range(3)
    )
    require_instrument(plateau_counts == (159, 317, 629), "N6 fake plateau malformed")
    require_instrument(plateau_counts != EXPECTED_SOURCE_COUNTS[:3], "N6 fake plateau accepted")
    print("CONTROL N6 plateau_only expected=REJECT observed=REJECT result=PASS")

    good_orbits = direct_product_orbit_count(20, 8, broken=False)
    bad_orbits = direct_product_orbit_count(20, 8, broken=True)
    require_instrument(good_orbits == gcd(20, 8) == 4, "N7 good product law rejected")
    require_instrument(bad_orbits != 4, "N7 broken product law accepted")
    print("CONTROL N7 broken_product expected=REJECT observed=REJECT result=PASS")

    synthetic_carrier = tuple(
        product(range(5), range(5), range(5), range(25))
    )
    generated = tuple(
        (0, 0, 0, (5 * multiple) % 25)
        for multiple in range(5)
    )
    require_instrument(len(generated) == 5, "N8 synthetic subgroup has wrong order")
    n8_regular, n8_witness = translation_action_regularity(
        generated,
        synthetic_carrier,
        (5, 5, 5, 25),
    )
    require_instrument(not n8_regular, "N8 nontransitive subgroup accepted")
    require_instrument(
        n8_witness.startswith("nontransitive_translation "),
        f"N8 rejected for the wrong reason: {n8_witness}",
    )
    print("CONTROL N8 nontransitive_translation expected=REJECT observed=REJECT result=PASS")


@dataclass(frozen=True)
class SourceLegResult:
    quotient_size: int
    determinantal_divisors: tuple[int, int, int, int]
    smith_factors: tuple[int, int, int, int]
    cycle_census: tuple[tuple[int, int], ...]
    action_order: int
    component_counts: tuple[int, ...]
    stable_component_count: int
    point_mass: Fraction


def signature_digest(signatures: Iterable[tuple[int, int, int, int]]) -> str:
    digest = sha256()
    for signature in sorted(signatures):
        for coordinate in signature:
            digest.update(coordinate.to_bytes(2, "big"))
    return digest.hexdigest()


def run_source_leg() -> SourceLegResult:
    print("SOURCE_LEG_BEGIN presentation=integer_cokernel")
    phi_c = matrix_add(
        matrix_add(matrix_add(matrix_pow(C4, 4), matrix_pow(C4, 3)), matrix_pow(C4, 2)),
        matrix_add(C4, I4),
    )
    require_instrument(phi_c == tuple(tuple(0 for _ in range(4)) for _ in range(4)), "Phi_5(C) is nonzero")

    derived_a = matrix_pow(matrix_sub(I4, C4), 5)
    derived_m = matrix_add(I4, matrix_pow(C4, 2))
    require_source(
        derived_a == EXPECTED_A,
        "S1",
        f"derived A differs observed={derived_a}",
    )
    require_source(
        derived_m == EXPECTED_M,
        "S1",
        f"derived M differs observed={derived_m}",
    )
    require_instrument(matrix_mul(derived_m, derived_a) == matrix_mul(derived_a, derived_m), "M and A do not commute")

    det_a = determinant(derived_a)
    require_source(det_a == 3125, "S2", f"det(A) differs observed={det_a}")
    adjoint = adjugate(derived_a)
    require_instrument(matrix_mul(derived_a, adjoint) == scalar_matrix(det_a), "A adj(A) identity failed")
    require_instrument(matrix_mul(adjoint, derived_a) == scalar_matrix(det_a), "adj(A) A identity failed")

    divisors = determinantal_divisors(derived_a)
    factors = smith_factors(divisors)
    require_source(
        divisors == EXPECTED_DETERMINANTAL_DIVISORS,
        "S2",
        f"determinantal divisors differ observed={divisors}",
    )
    require_source(
        factors == EXPECTED_SMITH_FACTORS,
        "S2",
        f"Smith factors differ observed={factors}",
    )

    representatives = quotient_representatives(adjoint, abs(det_a))
    require_source(
        len(representatives) == 3125,
        "S2",
        f"quotient cardinality differs observed={len(representatives)}",
    )
    for column in range(4):
        lattice_vector: Vector4 = tuple(derived_a[row][column] for row in range(4))  # type: ignore[assignment]
        require_instrument(
            quotient_signature(adjoint, abs(det_a), lattice_vector) == (0, 0, 0, 0),
            "an A-lattice generator has nonzero quotient signature",
        )

    induced: dict[tuple[int, int, int, int], tuple[int, int, int, int]] = {}
    for signature, representative in representatives.items():
        image_signature = quotient_signature(
            adjoint,
            abs(det_a),
            matrix_vector(derived_m, representative),
        )
        require_source(
            image_signature in representatives,
            "S3",
            "J image leaves quotient "
            f"source_signature={signature} observed_image={image_signature}",
        )
        induced[signature] = image_signature
    census = permutation_cycle_census(induced, source_gate="S3")
    require_source(
        census == EXPECTED_J_CYCLES,
        "S3",
        f"J cycle census differs observed={census}",
    )
    fixed = tuple(signature for signature, image in induced.items() if signature == image)
    first_nonzero_fixed = min(
        (signature for signature in fixed if signature != (0, 0, 0, 0)),
        default=None,
    )
    require_source(
        fixed == ((0, 0, 0, 0),),
        "S3",
        "J fixed class is not uniquely zero "
        f"zero_fixed={(0, 0, 0, 0) in fixed} fixed_count={len(fixed)} "
        f"first_nonzero={first_nonzero_fixed}",
    )

    action_order = 1
    for length, _multiplicity in census:
        action_order = action_order * length // gcd(action_order, length)
    require_source(
        action_order == 20,
        "S3",
        f"J action order differs observed={action_order}",
    )

    counts = tuple(
        component_count_from_census(census, level)
        for level in range(9)
    )
    require_source(
        counts == EXPECTED_SOURCE_COUNTS,
        "S4",
        f"dyadic component counts differ observed={counts}",
    )
    direct_counts = tuple(
        sum(
            multiplicity * direct_product_orbit_count(length, 2**level, broken=False)
            for length, multiplicity in census
        )
        for level in range(9)
    )
    require_instrument(
        direct_counts == counts,
        f"direct dyadic-factor audit differs: direct={direct_counts} formula={counts}",
    )
    stable_count = sum(
        multiplicity * two_adic_part(length)
        for length, multiplicity in census
    )
    require_source(
        stable_count == 629,
        "S4",
        f"all-level stabilized count differs observed={stable_count}",
    )

    signatures = tuple(representatives)
    translation_regular, translation_witness = translation_action_regularity(
        signatures,
        signatures,
        (abs(det_a), abs(det_a), abs(det_a), abs(det_a)),
    )
    require_source(
        translation_regular,
        "S5",
        f"quotient translation action is not regular witness={translation_witness}",
    )
    point_mass = Fraction(1, 2) * Fraction(1, len(representatives))
    require_source(
        point_mass == Fraction(1, 6250),
        "S5",
        f"conditional point mass differs observed={point_mass}",
    )

    print(
        "SOURCE S1 PASS A=(I-C)^5 M=I+C^2 commutation=yes "
        "cyclotomic_relation=yes"
    )
    print(
        "SOURCE S2 PASS determinant=3125 determinantal_divisors={5,25,125,3125} "
        "smith={5,5,5,25} quotient_size=3125 "
        f"quotient_signature_sha256={signature_digest(representatives)}"
    )
    print("SOURCE S3 PASS J_order=20 cycles={1:1,4:1,20:156} fixed=zero")
    print(
        "SOURCE S4 PASS c_src(s_TM=0)=158 c_src(s_TM=1)=315 "
        "c_src(s_TM>=2)=629 audit_levels=0..8 direct_product_audit=PASS theorem=T2"
    )
    print(
        "SOURCE S5 PASS Haar_quotient=uniform one_letter_mass=1/2 "
        "conditional_point_mass=1/6250 translation_action=regular theorem=T5"
    )
    print("SOURCE_LEG_END")
    return SourceLegResult(
        quotient_size=len(representatives),
        determinantal_divisors=divisors,
        smith_factors=factors,
        cycle_census=census,
        action_order=action_order,
        component_counts=counts,
        stable_component_count=stable_count,
        point_mass=point_mass,
    )


# ---------------------------------------------------------------------------
# Public finite generator table and exact carrier reconstruction


def mod5(value: int) -> int:
    return value % P


def trace_state(state: State) -> int:
    return sum(state) % P


def state_id(state: State) -> int:
    value = 0
    for coordinate in state:
        value = P * value + coordinate
    return value


def all_states() -> Iterable[State]:
    for coordinates in product(range(P), repeat=STATE_WIDTH):
        yield coordinates  # type: ignore[misc]


def gen_a(state: State) -> State:
    p1, p4, p1p, p4p, q, r_coordinate = state
    return (p4, p1, p4p, p1p, q, r_coordinate)


def gen_b(state: State) -> State:
    p1, p4, p1p, p4p, q, r_coordinate = state
    return (
        mod5(-p1p),
        mod5(-p4p),
        mod5(-p1),
        mod5(-p4),
        mod5(-q),
        mod5(-r_coordinate),
    )


def gen_c(state: State) -> State:
    p1, p4, p1p, p4p, q, r_coordinate = state
    return (
        mod5(-p1p + 2),
        mod5(-p4p + 1 + r_coordinate),
        mod5(-p1 + 2),
        mod5(-p4 + 1 - r_coordinate),
        mod5(1 - q),
        mod5(-r_coordinate),
    )


def gen_d(state: State) -> State:
    p1, p4, p1p, p4p, q, r_coordinate = state
    return (
        mod5(2 - p1),
        mod5(1 - p4),
        mod5(3 - p1p),
        mod5(4 - p4p),
        mod5(1 - q),
        mod5(1 - r_coordinate),
    )


def gen_e(state: State) -> State:
    p1, p4, p1p, p4p, q, r_coordinate = state
    return (
        mod5(2 - p1),
        mod5(1 - p4),
        mod5(3 - p1p),
        mod5(4 - p4p),
        mod5(2 - q),
        mod5(1 - r_coordinate),
    )


GENERATORS: tuple[Callable[[State], State], ...] = (gen_a, gen_b, gen_c, gen_d, gen_e)


def thue_morse_bit(index: int) -> int:
    parity = 0
    value = index
    while value:
        parity ^= value & 1
        value >>= 1
    return parity


def branch_map(state: State, bit: int) -> State:
    selector = (trace_state(state) + 2 * bit) % P
    return GENERATORS[selector](state)


def compose_bc(state: State) -> State:
    return gen_b(gen_c(state))


def validate_generator_table(carrier: Sequence[State]) -> None:
    trace_constants = (0, 0, 2, 2, 3)
    trace_signs = (1, -1, -1, -1, -1)
    for state in carrier:
        for index, generator in enumerate(GENERATORS):
            image = generator(state)
            require_target(
                generator(image) == state,
                "C1",
                f"generator {index} is not involutive",
            )
            expected_trace = (
                trace_signs[index] * trace_state(state) + trace_constants[index]
            ) % P
            require_target(
                trace_state(image) == expected_trace,
                "C1",
                f"generator {index} violates its trace law",
            )
        image = state
        for _ in range(5):
            image = compose_bc(image)
        require_target(image == state, "C1", "the relation (bc)^5=id failed")


def recurrent_core_from_public_dynamics() -> tuple[tuple[State, ...], tuple[State, ...]]:
    carrier = tuple(all_states())
    require_target(
        len(carrier) == P**STATE_WIDTH == 15625,
        "C1",
        "carrier cardinality mismatch",
    )
    validate_generator_table(carrier)

    current = set(carrier)
    recurrent: set[State] = set()
    final_tick = CENSUS_WARMUP + CENSUS_WINDOW
    for tick in range(final_tick):
        if tick >= CENSUS_WARMUP:
            recurrent.update(current)
        bit = thue_morse_bit(tick)
        current = {branch_map(state, bit) for state in current}
        time_index = tick + 1
        if time_index >= 3:
            expected_sheet = (4 + 2 * bit) % P
            require_target(
                len(current) == 3125,
                "C1",
                f"fixed-time image at n={time_index} does not have 3125 states",
            )
            require_target(
                all(trace_state(state) == expected_sheet for state in current),
                "C1",
                f"fixed-time image at n={time_index} has the wrong sheet",
            )

    core = tuple(sorted(recurrent, key=state_id))
    require_target(len(core) == 6250, "C1", "recurrent core does not have 6250 states")
    require_target(
        {trace_state(state) for state in core} == {1, 4},
        "C1",
        "recurrent core is not exactly on sheets 1 and 4",
    )
    return carrier, core


def state_sequence_hash(states: Sequence[State]) -> str:
    digest = sha256()
    for state in states:
        digest.update(state_id(state).to_bytes(2, "big"))
    return digest.hexdigest()


# ---------------------------------------------------------------------------
# One global D_5, constructed before any component is traversed


def local_second_reflection(state: State) -> State:
    return gen_b(gen_e(gen_b(state)))


def local_rotation(state: State) -> State:
    # Public word d o (b e b), applied right to left.
    return gen_d(local_second_reflection(state))


def local_action(element: Elem, state_on_sheet_one: State) -> State:
    k, reflection_flag = element
    image = gen_d(state_on_sheet_one) if reflection_flag else state_on_sheet_one
    for _ in range(k):
        image = local_rotation(image)
    return image


def global_action(element: Elem, state: State) -> State:
    sheet = trace_state(state)
    if sheet == 1:
        return local_action(element, state)
    if sheet == 4:
        # The public b is one fixed global bridge from sheet 4 to sheet 1.
        return gen_b(local_action(element, gen_b(state)))
    raise TargetGateFailure("G1", f"global D_5 received state on sheet {sheet}")


def permutation_hash(core: Sequence[State], mapping: dict[State, State]) -> str:
    digest = sha256()
    for state in core:
        digest.update(state_id(mapping[state]).to_bytes(2, "big"))
    return digest.hexdigest()


def permutation_cycle_type(
    core: Sequence[State], mapping: dict[State, State]
) -> tuple[tuple[int, int], ...]:
    visited: set[State] = set()
    lengths: Counter[int] = Counter()
    for start in core:
        if start in visited:
            continue
        current = start
        length = 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = mapping[current]
        require_target(current == start, "G1", "permutation cycle does not close at its start")
        lengths[length] += 1
    require_target(len(visited) == len(core), "G1", "permutation misses core states")
    return tuple(sorted(lengths.items()))


def cycle_type_text(cycle_type: Sequence[tuple[int, int]]) -> str:
    return ",".join(f"{length}^{count}" for length, count in cycle_type)


@dataclass(frozen=True)
class GroupConstruction:
    maps: dict[Elem, dict[State, State]]
    hashes: dict[Elem, str]
    cycle_types: dict[Elem, tuple[tuple[int, int], ...]]
    d_element: Elem
    second_reflection_element: Elem


def build_global_group(core: Sequence[State]) -> GroupConstruction:
    core_set = frozenset(core)
    half_one = tuple(state for state in core if trace_state(state) == 1)

    # Check the public line-translation identity before constructing component
    # orbits.  It is a carrier-wide identity on the reference half.
    for state in half_one:
        expected = (
            state[0],
            state[1],
            state[2],
            state[3],
            mod5(state[4] + 3),
            mod5(state[5] + 2),
        )
        require_target(
            local_rotation(state) == expected,
            "G1",
            "d o (b e b) is not the public line translation T_(0,0,0,0,3,2)",
        )

    maps: dict[Elem, dict[State, State]] = {}
    hashes: dict[Elem, str] = {}
    cycle_types: dict[Elem, tuple[tuple[int, int], ...]] = {}
    for element in ELEMENTS:
        mapping = {state: global_action(element, state) for state in core}
        require_target(
            frozenset(mapping.values()) == core_set,
            "G1",
            f"{elem_text(element)} is not a permutation of R",
        )
        maps[element] = mapping
        hashes[element] = permutation_hash(core, mapping)
        cycle_types[element] = permutation_cycle_type(core, mapping)

    require_target(
        len({tuple(maps[element][state] for state in core) for element in ELEMENTS}) == 10,
        "G1",
        "the ten global permutations are not distinct",
    )

    for left in ELEMENTS:
        for right in ELEMENTS:
            product_element = elem_mul(left, right)
            left_map = maps[left]
            right_map = maps[right]
            product_map = maps[product_element]
            for state in core:
                require_target(
                    left_map[right_map[state]] == product_map[state],
                    "G1",
                    f"multiplication table failed for {elem_text(left)}*{elem_text(right)}",
                )

    d_candidates = [
        element
        for element in ELEMENTS
        if all(maps[element][state] == gen_d(state) for state in half_one)
    ]
    second_candidates = [
        element
        for element in ELEMENTS
        if all(
            maps[element][state] == local_second_reflection(state) for state in half_one
        )
    ]
    require_target(len(d_candidates) == 1, "G1", "d has no unique D_5 label")
    require_target(
        len(second_candidates) == 1,
        "G1",
        "b e b has no unique D_5 label",
    )
    return GroupConstruction(
        maps=maps,
        hashes=hashes,
        cycle_types=cycle_types,
        d_element=d_candidates[0],
        second_reflection_element=second_candidates[0],
    )


# ---------------------------------------------------------------------------
# Components are formed only after the global group is fixed


@dataclass(frozen=True)
class Component:
    key: str
    half_zero: tuple[State, ...]
    half_one: tuple[State, ...]
    generic: bool

    def points(self, half: int) -> tuple[State, ...]:
        return self.half_zero if half == 0 else self.half_one


def build_components(
    core: Sequence[State], group: GroupConstruction
) -> tuple[Component, ...]:
    half_one_set = {state for state in core if trace_state(state) == 1}
    half_zero_set = {state for state in core if trace_state(state) == 4}
    unseen = set(half_one_set)
    raw: list[tuple[tuple[State, ...], tuple[State, ...]]] = []

    # min(unseen) is used only to traverse already-defined global orbits.  It
    # does not define any generator, marked reflection, bridge, or gauge.
    while unseen:
        start = min(unseen, key=state_id)
        orbit_one = {group.maps[element][start] for element in ELEMENTS}
        require_target(orbit_one <= half_one_set, "G2", "G orbit leaves sheet 1")
        unseen.difference_update(orbit_one)
        orbit_zero = {gen_b(state) for state in orbit_one}
        require_target(orbit_zero <= half_zero_set, "G2", "b bridge leaves sheet 4")
        raw.append(
            (
                tuple(sorted(orbit_zero, key=state_id)),
                tuple(sorted(orbit_one, key=state_id)),
            )
        )

    raw.sort(key=lambda pair: min(state_id(state) for state in pair[0] + pair[1]))
    components: list[Component] = []
    generic_index = 0
    singlet_index = 0
    for half_zero, half_one in raw:
        size = len(half_one)
        require_target(size in {5, 10}, "G2", f"unexpected half orbit size {size}")
        if size == 10:
            key = f"G{generic_index:03d}"
            generic_index += 1
            generic = True
        else:
            key = f"S{singlet_index:03d}"
            singlet_index += 1
            generic = False
        components.append(Component(key, half_zero, half_one, generic))

    require_target(generic_index == 312, "G2", "generic component count is not 312")
    require_target(singlet_index == 1, "G2", "singlet component count is not one")

    covered_zero = set().union(*(set(component.half_zero) for component in components))
    covered_one = set().union(*(set(component.half_one) for component in components))
    require_target(covered_zero == half_zero_set, "G2", "components do not cover half 0")
    require_target(covered_one == half_one_set, "G2", "components do not cover half 1")
    require_target(
        sum(len(component.half_zero) for component in components) == len(half_zero_set),
        "G2",
        "half-0 component orbits overlap",
    )
    require_target(
        sum(len(component.half_one) for component in components) == len(half_one_set),
        "G2",
        "half-1 component orbits overlap",
    )

    for component in components:
        for half in (0, 1):
            points = component.points(half)
            point_set = set(points)
            for point in points:
                images = [group.maps[element][point] for element in ELEMENTS]
                require_target(
                    set(images) == point_set,
                    "G2",
                    f"G is not transitive on {component.key}/H{half}",
                )
                if component.generic:
                    require_target(
                        len(set(images)) == 10,
                        "G2",
                        f"G is not free on {component.key}/H{half}",
                    )
                else:
                    multiplicities = Counter(images)
                    require_target(
                        len(multiplicities) == 5
                        and set(multiplicities.values()) == {2},
                        "G2",
                        f"singlet stabilizers are not all order two on H{half}",
                    )

        require_target(
            {gen_b(state) for state in component.half_one} == set(component.half_zero),
            "G2",
            f"global b bridge does not pair the halves of {component.key}",
        )

        for previous_half in (0, 1):
            source = component.points(previous_half)
            for current_bit in (0, 1):
                image = {branch_map(state, current_bit) for state in source}
                require_target(
                    image == set(component.points(current_bit)),
                    "G2",
                    f"branch ({previous_half},{current_bit}) is not a component-half bijection "
                    f"on {component.key}",
                )

        for state in component.half_one:
            require_target(
                branch_map(branch_map(state, 0), 1) == state,
                "G2",
                f"cross inverse law fails on {component.key}/H1",
            )
        for state in component.half_zero:
            require_target(
                branch_map(branch_map(state, 1), 0) == state,
                "G2",
                f"cross inverse law fails on {component.key}/H0",
            )

        fixed_zero = sum(branch_map(state, 0) == state for state in component.half_zero)
        fixed_one = sum(branch_map(state, 1) == state for state in component.half_one)
        expected_fixed = 0 if component.generic else 1
        require_target(
            fixed_zero == expected_fixed and fixed_one == expected_fixed,
            "G2",
            f"own-half fixed-point census fails on {component.key}",
        )

    return tuple(components)


def reconstruct_basin_counts(
    carrier: Sequence[State], components: Sequence[Component]
) -> Counter[str]:
    component_of: dict[State, str] = {}
    for component in components:
        for state in component.half_zero + component.half_one:
            require_target(state not in component_of, "C1", "component supports overlap")
            component_of[state] = component.key

    masses: dict[State, int] = {state: 1 for state in carrier}
    for tick in range(CENSUS_WARMUP):
        bit = thue_morse_bit(tick)
        next_masses: dict[State, int] = {}
        for state, mass in masses.items():
            image = branch_map(state, bit)
            next_masses[image] = next_masses.get(image, 0) + mass
        masses = next_masses

    require_target(sum(masses.values()) == 15625, "C1", "basin mass is not conserved")
    require_target(
        all(state in component_of for state in masses),
        "C1",
        "warmup image contains a nonrecurrent state",
    )
    basin_counts: Counter[str] = Counter()
    for state, mass in masses.items():
        basin_counts[component_of[state]] += mass

    for component in components:
        expected = 50 if component.generic else 25
        require_target(
            basin_counts[component.key] == expected,
            "C1",
            f"basin count for {component.key} is not {expected}",
        )
    return basin_counts


# ---------------------------------------------------------------------------
# Direct subgroup orbit menu, with all five reflections separate


def subgroup_specs() -> tuple[tuple[str, tuple[Elem, ...]], ...]:
    rotations = tuple((k, 0) for k in range(5))
    specs: list[tuple[str, tuple[Elem, ...]]] = [
        ("D5", ELEMENTS),
        ("C5", rotations),
    ]
    for k in range(5):
        specs.append((f"C2[{elem_text((k, 1))}]", (ID, (k, 1))))
    specs.append(("TRIVIAL", (ID,)))
    return tuple(specs)


def validate_subgroup(name: str, subgroup: Sequence[Elem]) -> None:
    members = frozenset(subgroup)
    require_target(ID in members, "G5", f"subgroup {name} omits identity")
    for left in members:
        require_target(elem_inv(left) in members, "G5", f"subgroup {name} lacks inverse")
        for right in members:
            require_target(
                elem_mul(left, right) in members,
                "G5",
                f"subgroup {name} is not multiplication closed",
            )


def direct_orbit_count(
    points: Sequence[State],
    subgroup: Sequence[Elem],
    maps: dict[Elem, dict[State, State]],
) -> int:
    point_set = set(points)
    unseen = set(points)
    count = 0
    while unseen:
        start = min(unseen, key=state_id)
        orbit = {maps[element][start] for element in subgroup}
        require_target(orbit <= point_set, "G5", "subgroup orbit leaves target half")
        unseen.difference_update(orbit)
        count += 1
    return count


@dataclass(frozen=True)
class MenuRow:
    name: str
    order: int
    generic_zero: tuple[tuple[int, int], ...]
    generic_one: tuple[tuple[int, int], ...]
    singlet_zero: int
    singlet_one: int
    total_zero: int
    total_one: int


@dataclass(frozen=True)
class MenuResult:
    rows: tuple[MenuRow, ...]
    menu_zero: tuple[int, ...]
    menu_one: tuple[int, ...]
    generic_menu: tuple[int, ...]
    singlet_menu: tuple[int, ...]
    agrees: bool


def counter_tuple(counter: Counter[int]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(counter.items()))


def counter_text(counter_items: Sequence[tuple[int, int]]) -> str:
    return "{" + ",".join(f"{value}:{count}" for value, count in counter_items) + "}"


def compute_menu(
    components: Sequence[Component], group: GroupConstruction
) -> MenuResult:
    generic = tuple(component for component in components if component.generic)
    singlets = tuple(component for component in components if not component.generic)
    require_target(len(generic) == 312, "G5", "menu sees wrong generic count")
    require_target(len(singlets) == 1, "G5", "menu sees wrong singlet count")
    singlet = singlets[0]

    rows: list[MenuRow] = []
    all_expected = True
    expected_by_kind = {
        "D5": (1, 1, 313),
        "C5": (2, 1, 625),
        "C2": (5, 3, 1563),
        "TRIVIAL": (10, 5, 3125),
    }

    for name, subgroup in subgroup_specs():
        validate_subgroup(name, subgroup)
        generic_zero_counts = Counter(
            direct_orbit_count(component.half_zero, subgroup, group.maps)
            for component in generic
        )
        generic_one_counts = Counter(
            direct_orbit_count(component.half_one, subgroup, group.maps)
            for component in generic
        )
        singlet_zero = direct_orbit_count(singlet.half_zero, subgroup, group.maps)
        singlet_one = direct_orbit_count(singlet.half_one, subgroup, group.maps)
        total_zero = sum(value * count for value, count in generic_zero_counts.items()) + singlet_zero
        total_one = sum(value * count for value, count in generic_one_counts.items()) + singlet_one
        row = MenuRow(
            name=name,
            order=len(subgroup),
            generic_zero=counter_tuple(generic_zero_counts),
            generic_one=counter_tuple(generic_one_counts),
            singlet_zero=singlet_zero,
            singlet_one=singlet_one,
            total_zero=total_zero,
            total_one=total_one,
        )
        rows.append(row)

        kind = "C2" if name.startswith("C2[") else name
        expected_generic, expected_singlet, expected_total = expected_by_kind[kind]
        expected_census = ((expected_generic, 312),)
        if not (
            row.generic_zero == expected_census
            and row.generic_one == expected_census
            and row.singlet_zero == expected_singlet
            and row.singlet_one == expected_singlet
            and row.total_zero == expected_total
            and row.total_one == expected_total
        ):
            all_expected = False

    menu_zero = tuple(sorted({row.total_zero for row in rows}))
    menu_one = tuple(sorted({row.total_one for row in rows}))
    generic_menu = tuple(
        sorted(
            {
                value
                for row in rows
                for value, count in row.generic_zero
                if count == 312
            }
        )
    )
    singlet_menu = tuple(sorted({row.singlet_zero for row in rows}))

    agrees = all_expected
    agrees = agrees and menu_zero == (313, 625, 1563, 3125)
    agrees = agrees and menu_one == (313, 625, 1563, 3125)
    agrees = agrees and generic_menu == (1, 2, 5, 10)
    agrees = agrees and singlet_menu == (1, 3, 5)

    return MenuResult(
        rows=tuple(rows),
        menu_zero=menu_zero,
        menu_one=menu_one,
        generic_menu=generic_menu,
        singlet_menu=singlet_menu,
        agrees=agrees,
    )


# ---------------------------------------------------------------------------
# Real common-cocycle extraction: no per-component marking or basepoint


@dataclass(frozen=True)
class CocycleResult:
    common: tuple[Elem, ...]
    raw_census: tuple[tuple[tuple[Elem, ...], int], ...]
    gauge_census: tuple[tuple[Elem, int], ...]


def real_common_cocycle(
    components: Sequence[Component], group: GroupConstruction
) -> CocycleResult:
    by_key = {component.key: component for component in components}
    reference_sets = {
        component.key: frozenset(component.half_one) for component in components
    }
    component_keys = tuple(component.key for component in components)

    def points(key: str, half: int) -> Sequence[object]:
        return by_key[key].points(half)

    def edge_map(
        _key: str, _previous_half: int, current_bit: int, point: object
    ) -> object:
        require_target(isinstance(point, tuple), "G3", "real edge point is not a state")
        return branch_map(point, current_bit)  # type: ignore[arg-type]

    def to_reference(key: str, half: int, point: object) -> object:
        require_target(isinstance(point, tuple), "G3", "reference point is not a state")
        state = point  # type: ignore[assignment]
        reference = gen_b(state) if half == 0 else state
        require_target(
            reference in reference_sets[key],
            "G3",
            f"global b reference bridge leaves component {key}",
        )
        return reference

    def action(element: Elem, point: object) -> object:
        require_target(isinstance(point, tuple), "G3", "action point is not a state")
        return group.maps[element][point]  # type: ignore[index]

    try:
        accepted, raw, gauged = common_cocycle_gate(
            component_keys, points, edge_map, to_reference, action
        )
    except LabelExtractionFailure as exc:
        raise TargetGateFailure("G3", str(exc)) from exc

    require_target(accepted, "G3", "the 313 gauged edge tuples are not identical")
    common = gauged[component_keys[0]]
    raw_counter = Counter(raw.values())
    gauge_counter = Counter(gauge_for_component(key) for key in component_keys)
    return CocycleResult(
        common=common,
        raw_census=tuple(sorted(raw_counter.items(), key=lambda item: tuple_text(item[0]))),
        gauge_census=tuple(sorted(gauge_counter.items())),
    )


def validate_invariant_shape(common: Sequence[Elem]) -> None:
    labels = {edge: label for edge, label in zip(EDGE_ORDER, common)}
    cross = (labels[(0, 1)], labels[(1, 0)])
    own = (labels[(0, 0)], labels[(1, 1)])
    require_target(cross == (ID, ID), "G4", "the two cross edges are not identities")
    require_target(own[0] != own[1], "G4", "the two own-edge reflections coincide")
    require_target(
        all(label != ID and elem_order(label) == 2 for label in own),
        "G4",
        "an own edge is not a nonidentity reflection",
    )
    require_target(
        elem_order(elem_mul(own[0], own[1])) == 5
        and elem_order(elem_mul(own[1], own[0])) == 5,
        "G4",
        "the product of the own-edge reflections does not have order five",
    )
    require_target(
        len(generated_subgroup(own)) == 10,
        "G4",
        "the two own-edge reflections do not generate D_5",
    )


# ---------------------------------------------------------------------------
# Full run and byte-stable report


def tuple_of_ints(values: Sequence[int]) -> str:
    return "{" + ",".join(str(value) for value in values) + "}"


def print_menu(menu: MenuResult) -> None:
    print("G5 DIRECT_ORBIT_MENU_BEGIN halves=H0,H1 subgroups=8")
    for row in menu.rows:
        print(
            f"G5 subgroup={row.name} order={row.order} "
            f"H0_generic_census={counter_text(row.generic_zero)} "
            f"H1_generic_census={counter_text(row.generic_one)} "
            f"H0_singlet={row.singlet_zero} H1_singlet={row.singlet_one} "
            f"H0_total={row.total_zero} H1_total={row.total_one}"
        )
    print(
        f"G5 target_menu_H0={tuple_of_ints(menu.menu_zero)} "
        f"target_menu_H1={tuple_of_ints(menu.menu_one)}"
    )
    print(
        f"generic_menu={tuple_of_ints(menu.generic_menu)} "
        f"singlet_menu={tuple_of_ints(menu.singlet_menu)}"
    )
    print(
        f"G5 DIRECT_ORBIT_MENU_END verdict={'AGREE' if menu.agrees else 'DISAGREE'}"
    )


@dataclass(frozen=True)
class TargetLegResult:
    public_basis: str
    public_scope_issue: int
    carrier_size: int
    recurrent_core_size: int
    recurrent_core_sha256: str
    half_size: int
    generic_component_count: int
    singlet_component_count: int
    group_order: int
    gauge_set: tuple[Elem, ...]
    permutation_hashes: tuple[tuple[Elem, str], ...]
    common_labels: tuple[Elem, ...]
    menu_zero: tuple[int, ...]
    menu_one: tuple[int, ...]
    generic_menu: tuple[int, ...]
    singlet_menu: tuple[int, ...]
    menu_agrees: bool


def _construct_target_leg() -> TargetLegResult:
    carrier, core = recurrent_core_from_public_dynamics()
    half_zero = tuple(state for state in core if trace_state(state) == 4)
    half_one = tuple(state for state in core if trace_state(state) == 1)
    require_target(
        len(half_zero) == len(half_one) == 3125,
        "C1",
        "recurrent halves do not have 3125 states each",
    )
    print(
        f"C1 PASS carrier={len(carrier)} recurrent_core={len(core)} "
        f"H0={len(half_zero)} H1={len(half_one)} "
        f"core_sha256={state_sequence_hash(core)}"
    )

    # This is the C4 fence in executable order: G is completely built and its
    # multiplication table validated before build_components is called.
    group = build_global_group(core)
    print(
        "G1 PASS group=D5 order=10 global_before_components=yes "
        "domain_order=base5_state_id permutation_encoding=big_endian_uint16_targets"
    )
    for element in ELEMENTS:
        print(
            f"G1 permutation={elem_text(element)} sha256={group.hashes[element]} "
            f"cycles={cycle_type_text(group.cycle_types[element])}"
        )
    print(
        f"G1 generator_d={elem_text(group.d_element)} "
        f"generator_beb={elem_text(group.second_reflection_element)} "
        "classification=gauge-dependent-diagnostic"
    )

    components = build_components(core, group)
    basins = reconstruct_basin_counts(carrier, components)
    generic = tuple(component for component in components if component.generic)
    singlet = tuple(component for component in components if not component.generic)
    basin_census = Counter(basins.values())
    require_target(
        basin_census == Counter({50: 312, 25: 1}),
        "C1",
        "basin census differs from 312*50 plus 25",
    )
    print(
        "G2 PASS generic_components=312 generic_half_size=10 "
        "generic_action=free-transitive sides=2 singlet_components=1 "
        "singlet_half_size=5 singlet_action=transitive stabilizer_order=2 sides=2"
    )
    print(
        f"C1 BASINS PASS generic_50={len(generic)} singlet_25={len(singlet)} "
        f"total={sum(basins.values())}"
    )

    # The target menu is computed independently of the common-label verdict.
    # No source count or source-side orbit calculation enters this target-menu
    # calculation; combined main compares the two typed leg results afterward.
    menu = compute_menu(components, group)
    print_menu(menu)

    cocycle = real_common_cocycle(components, group)
    validate_invariant_shape(cocycle.common)
    raw_census_text = ";".join(
        f"{tuple_text(labels)}:{count}" for labels, count in cocycle.raw_census
    )
    gauge_census_text = ",".join(
        f"{elem_text(gauge)}:{count}" for gauge, count in cocycle.gauge_census
    )
    print(
        "G3 PASS common_tuple=yes generic_components=312 singlet_compatible=yes "
        f"gauged_labels={tuple_text(cocycle.common)}"
    )
    print(
        "G3 DIAGNOSTIC gauge_dependent=yes "
        f"raw_tuple_census={{{raw_census_text}}} gauge_census={{{gauge_census_text}}}"
    )
    print(
        "G4 PASS cross_edges=identity own_edges=distinct_reflections "
        "own_product_order=5 generated_group_order=10"
    )
    print(f"TARGET_MENU={'AGREE' if menu.agrees else 'DISAGREE'}")

    return TargetLegResult(
        public_basis=PUBLIC_BASIS,
        public_scope_issue=PUBLIC_SCOPE_ISSUE,
        carrier_size=len(carrier),
        recurrent_core_size=len(core),
        recurrent_core_sha256=state_sequence_hash(core),
        half_size=len(half_zero),
        generic_component_count=len(generic),
        singlet_component_count=len(singlet),
        group_order=len(ELEMENTS),
        gauge_set=GAMMA,
        permutation_hashes=tuple(
            (element, group.hashes[element]) for element in ELEMENTS
        ),
        common_labels=cocycle.common,
        menu_zero=menu.menu_zero,
        menu_one=menu.menu_one,
        generic_menu=menu.generic_menu,
        singlet_menu=menu.singlet_menu,
        menu_agrees=menu.agrees,
    )


def run_target_leg() -> TargetLegResult:
    """Return the target record after the combined main has run all controls."""

    print("TARGET_LEG_BEGIN controls_passed=yes group_prior_to_components=required")
    result = _construct_target_leg()
    print("TARGET_LEG_END")
    return result


def print_header() -> None:
    print(f"PROBE={PROBE_ID}")
    print(f"PUBLIC_BASIS={PUBLIC_BASIS}")
    print(f"PUBLIC_SCOPE_ISSUE={PUBLIC_SCOPE_ISSUE}")
    print("LEG=COMBINED mode=confirmatory independent_methods_claimed=no")
    print("ARITHMETIC=exact_integer_and_Fraction float_assertions=none stdlib_only=yes")
    print("GAUGE_SET Gamma={1} order=1 proper_subset_of_D5=yes")
    print(
        "GAUGE_RULE gamma(component)=1 constant_before_target=yes "
        "component_data_access=no label_search=no"
    )
    print(
        "SCOPE depth=lambda^5 substitution_factor=s_TM>=2 "
        "map=fiberwise_bijective_a.e. action=L2_to_L5 L6=no SI=no"
    )


def mixed_control_solutions(
    source_count: int,
    generic_menu: Sequence[int],
    singlet_menu: Sequence[int],
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (generic, singlet)
        for generic in generic_menu
        for singlet in singlet_menu
        if 312 * generic + singlet == source_count
    )


def main(argv: Sequence[str]) -> int:
    if argv:
        print(f"usage: {sys.argv[0]}", file=sys.stderr)
        return 2
    print_header()
    try:
        # Every mandatory instrument control precedes both real carriers.
        run_mandatory_controls()
        validate_abstract_d5_and_gauge()
        run_source_controls()
        print("CONTROL_D5_GROUP=PASS elements=10 multiplication=elementwise")
        print("CONTROL_GAUGE_MACHINERY=PASS Gamma_order=1 proper=yes")
        print("CONTROLS=PASS order=N1,N2,N3,N4,N5,N6,N7,N8")

        source = run_source_leg()
        target = run_target_leg()

        if not target.menu_agrees:
            raise TargetGateFailure("G5", "complete subgroup menu differs")
        if (
            source.stable_component_count in target.menu_zero
            or source.stable_component_count in target.menu_one
        ):
            raise TargetGateFailure("G5", "source count appears in common-M target menu")
        solutions = mixed_control_solutions(
            source.stable_component_count,
            target.generic_menu,
            target.singlet_menu,
        )
        if solutions != ((2, 5),):
            raise TargetGateFailure("G5", "mixed control lacks unique solution (2,5)")
    except InputReconstructionDefect as exc:
        print(
            "DECISION=STOP_INPUT_RECONSTRUCTION_DEFECT "
            "gate=C1 input_or_public_basis=yes "
            f"reason={exc}"
        )
        return 2
    except SourceGateFailure as exc:
        print(
            f"DECISION=ROUTE-FALSIFIED leg=SOURCE gate={exc.gate} "
            f"reason={exc}"
        )
        print("ENTROPY_LAYER_BRIDGE=OPEN A_A_empty=NOT_CLAIMED")
        return 0
    except TargetGateFailure as exc:
        print(
            f"DECISION=ROUTE-FALSIFIED leg=TARGET gate={exc.gate} "
            f"reason={exc}"
        )
        print("ENTROPY_LAYER_BRIDGE=OPEN A_A_empty=NOT_CLAIMED")
        return 0
    except InstrumentDefect as exc:
        print(f"DECISION=STOP_INSTRUMENT_DEFECT reason={exc}")
        return 2

    print(
        "COMBINED_GATE source_components=629[s_TM>=2] "
        "target_menu={313,625,1563,3125} source_in_menu=no "
        "mixed_control_unique=(2,5)"
    )
    print(
        "DECISION=OBSTRUCTION-CERTIFIED ceiling=C "
        "scope=fixed_lambda^5_fiberwise_bijective_identity_gauge_s_TM>=2"
    )
    print(
        "NONCONCLUSIONS entropy_layer_bridge=OPEN A_A_empty=NOT_CLAIMED "
        "alternative_gauges=UNDECIDED deeper_depth=UNDECIDED "
        "nonbijective=UNDECIDED variable_depth=UNDECIDED L6=no SI=no"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
