#!/usr/bin/env python3
"""Independent common-cocycle breaker for PREREG-BREAKER-MACKEY4-2.

The full mode reconstructs the finite carrier solely from the public generator
table embedded below.  The group is constructed globally on the recurrent
core before component orbits are formed.  Component traversal never selects a
group generator, rotation, reflection, bridge, or gauge.

The ``--synthetic-only`` mode touches D_5 data only.  It exists so the frozen
negative controls and abstract group/gauge machinery can be checked before the
target code is pinned without opening the claim carrier.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import platform
import sys
from typing import Callable, Iterable, Sequence


P = 5
STATE_WIDTH = 6
CENSUS_WARMUP = 400
CENSUS_WINDOW = 300

# Every use of this source count has the frozen substitution-level scope in
# its name or adjacent text: r >= 2.
SOURCE_COMPONENT_COUNT_R_GE_2 = 629

State = tuple[int, int, int, int, int, int]
Elem = tuple[int, int]  # r^k s^f in D_5, with k mod 5 and f in {0,1}
Edge = tuple[int, int]  # (previous half, current bit)

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
    """A real-target gate disagreed with the frozen candidate specification."""

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
    mixed_solutions: tuple[tuple[int, int], ...]
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
    mixed_solutions = tuple(
        (a_value, b_value)
        for a_value in generic_menu
        for b_value in singlet_menu
        if 312 * a_value + b_value == SOURCE_COMPONENT_COUNT_R_GE_2
    )

    agrees = all_expected
    agrees = agrees and menu_zero == (313, 625, 1563, 3125)
    agrees = agrees and menu_one == (313, 625, 1563, 3125)
    agrees = agrees and SOURCE_COMPONENT_COUNT_R_GE_2 not in menu_zero
    agrees = agrees and SOURCE_COMPONENT_COUNT_R_GE_2 not in menu_one
    agrees = agrees and generic_menu == (1, 2, 5, 10)
    agrees = agrees and singlet_menu == (1, 3, 5)
    agrees = agrees and mixed_solutions == ((2, 5),)

    return MenuResult(
        rows=tuple(rows),
        menu_zero=menu_zero,
        menu_one=menu_one,
        generic_menu=generic_menu,
        singlet_menu=singlet_menu,
        mixed_solutions=mixed_solutions,
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
        "G5 exclusion[scope=r>=2] "
        f"source_count={SOURCE_COMPONENT_COUNT_R_GE_2} "
        f"in_H0={'yes' if SOURCE_COMPONENT_COUNT_R_GE_2 in menu.menu_zero else 'no'} "
        f"in_H1={'yes' if SOURCE_COMPONENT_COUNT_R_GE_2 in menu.menu_one else 'no'}"
    )
    solution_text = ",".join(f"({a},{b})" for a, b in menu.mixed_solutions)
    print(
        "G5 mixed_control[scope=r>=2] equation=312*a+b "
        f"generic_menu={tuple_of_ints(menu.generic_menu)} "
        f"singlet_menu={tuple_of_ints(menu.singlet_menu)} "
        f"source_count={SOURCE_COMPONENT_COUNT_R_GE_2} solutions={{{solution_text}}}"
    )
    print(
        f"G5 DIRECT_ORBIT_MENU_END verdict={'AGREE' if menu.agrees else 'DISAGREE'}"
    )


def run_full_target() -> bool:
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

    # G5 is computed from the built target independently of the common-label
    # verdict, so the open breaker-1 retirement ruling needs no third tool.
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

    common_verdict = True
    if common_verdict:
        print(
            "B2-F4 CONFIRMED_BY_AN_INDEPENDENT_ROUTE grade=candidate "
            "platforms=1 promotion=none"
        )
    if not menu.agrees:
        print(
            "B2-F5 COUNTING_DISAGREEMENT first_class=yes "
            "common_cocycle_verdict_unchanged=yes"
        )
    else:
        print("B2-F5 COUNTING_AGREEMENT result=PASS")
    print(
        "SCOPE fixed_depth=lambda^5 fiberwise_bijective_Route_A_subansatz "
        "substitution_levels=r>=2 L2_to_L5=yes L6=no SI=no"
    )
    print(
        "NONCONCLUSIONS entropy_layer_bridge=OPEN A_A_empty=NOT_CLAIMED "
        "deeper_depth=UNDECIDED nonbijective=UNDECIDED variable_depth=UNDECIDED "
        "r_greater_than_2_collars=UNDECIDED"
    )
    return menu.agrees


def print_header(mode: str) -> None:
    print("INSTRUMENT=PREREG-BREAKER-MACKEY4-2 status=NON-CANONICAL")
    print(
        f"MODE={mode} platform_system={platform.system()} "
        f"architecture={platform.machine()} python={platform.python_version()}"
    )
    print("ARITHMETIC=exact_integer float_assertions=none stdlib_only=yes")
    print("GAUGE_SET Gamma={1} order=1 proper_subset_of_D5=yes")
    print(
        "GAUGE_RULE gamma(component)=1 constant_before_target=yes "
        "component_data_access=no label_search=no"
    )


def main(argv: Sequence[str]) -> int:
    allowed = {"--synthetic-only"}
    unknown = [argument for argument in argv if argument not in allowed]
    if unknown:
        print(f"usage: {sys.argv[0]} [--synthetic-only]", file=sys.stderr)
        return 2
    synthetic_only = "--synthetic-only" in argv
    print_header("SYNTHETIC_ONLY" if synthetic_only else "FULL_TARGET")

    try:
        # Frozen order: N1, then N2, then N3.  No target function is called
        # before all three verdicts are printed and accepted.
        run_mandatory_controls()
        validate_abstract_d5_and_gauge()
        print("SYNTHETIC D5_GROUP=PASS elements=10 multiplication=elementwise")
        print("SYNTHETIC GAUGE_MACHINERY=PASS Gamma_order=1 proper=yes")
        print("SYNTHETIC_CONTROLS=PASS order=N1,N2,N3")
    except InstrumentDefect as exc:
        print(f"B2-F2 DEFECTIVE_INSTRUMENT stage=synthetic reason={exc}")
        print("CLAIM_CARRIER_EXECUTED=NO")
        return 2

    if synthetic_only:
        print("PREPIN_CHECK_COMPLETE allowed_scope=synthetic_D5_group_gauge_only")
        print("CLAIM_CARRIER_EXECUTED=NO")
        return 0

    print("TARGET_GATE_BEGIN controls_passed=yes group_prior_to_components=required")
    try:
        counting_agrees = run_full_target()
    except InputReconstructionDefect as exc:
        print(
            "INPUT_RECONSTRUCTION_DEFECT STOP gate=C1 input_or_public_basis=yes "
            f"reason={exc}"
        )
        print("CANDIDATE_ROUTE=STOPPED scientific_disagreement=no threshold_movement=no")
        return 1
    except TargetGateFailure as exc:
        print(
            f"B2-F1 DISAGREEMENT gate={exc.gate} first_class=yes reason={exc}"
        )
        print("CANDIDATE_ROUTE=STOPPED threshold_movement=no")
        return 1
    except InstrumentDefect as exc:
        print(f"B2-F2 DEFECTIVE_INSTRUMENT stage=target reason={exc}")
        return 2

    print("TARGET_GATE_END")
    return 0 if counting_agrees else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
