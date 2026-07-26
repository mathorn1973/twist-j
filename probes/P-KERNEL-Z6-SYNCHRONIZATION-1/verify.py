#!/usr/bin/env python3
"""Exact L1 proof audit for P-KERNEL-Z6-SYNCHRONIZATION-1.

The all-n conclusion is carried by the symbolic certificates frozen in
PREREG.md. This verifier audits their finite premises, complete proof cases,
and two independent exact implementations. It reads no files.
"""

import os
import sys
from collections import Counter
from itertools import product


P = 5
STATE_COUNT = P**6
SHEET_COUNT = P**5
X14_COUNT = 2 * SHEET_COUNT
BASE_COMMIT = "4ac41b4fac3a3794a6e9d5be1e2027d324edb806"
OWNER_SCOPE_SHA256 = (
    "abcb22785e37c2fbaae7860856b1ca8762ccc2b4c1b4b50fcf763fb273bbd2e0"
)
PREREG_SHA256 = (
    "e783a3a16891804f0c97b5b80744b0bb4ec5dcee1f8b2ae4f479283e2b48703a"
)
REQUIRED_ENVIRONMENT = (
    ("LC_ALL", "C"),
    ("LANG", "C"),
    ("PYTHONDONTWRITEBYTECODE", "1"),
    ("PYTHONHASHSEED", "0"),
    ("TZ", "UTC"),
)

EXPECTED_SHEET_TABLE = (
    (0, 4, 0, 4, 4),
    (2, 1, 1, 3, 1),
)
TRACE_AFFINE = (
    (1, 0),
    (-1, 0),
    (-1, 2),
    (-1, 2),
    (-1, 3),
)
EXPECTED_ADJACENT_CASES = (
    (0, 0, 4, 4, 4),
    (0, 1, 4, 1, 1),
    (1, 0, 1, 1, 4),
    (1, 1, 1, 3, 1),
)
PERIOD_CONTROLS = (
    (1, 0),
    (2, 0),
    (3, 17),
    (31, 1024),
    (32, 9999),
    (12345, 67890),
)
PROOF_RULE_ARITY = {
    "BINARY-INDUCTION": 0,
    "BIT-LENGTH-BOUND": 0,
    "CONTRADICTION": 2,
    "INJECTIVE-RECODING": 2,
    "FUNCTION-CONTRAPOSITION": 1,
    "PIGEONHOLE": 0,
    "FUNCTION-INDUCTION": 1,
    "FUNCTION-CONGRUENCE": 1,
}
P03_PROOF_GRAPH = (
    ("TM-COMPLEMENT", "BINARY-INDUCTION", ()),
    ("WIDTH-MARGIN", "BIT-LENGTH-BOUND", ()),
    (
        "TM-NONPERIODIC",
        "CONTRADICTION",
        ("TM-COMPLEMENT", "WIDTH-MARGIN"),
    ),
    (
        "TRACE-NONPERIODIC",
        "INJECTIVE-RECODING",
        ("TM-NONPERIODIC", "S1"),
    ),
    (
        "STATE-NONPERIODIC",
        "FUNCTION-CONTRAPOSITION",
        ("TRACE-NONPERIODIC",),
    ),
)
P04_PROOF_GRAPH = (
    ("FINITE-COLLISION", "PIGEONHOLE", ()),
    (
        "FINITE-ORBIT-PERIODIC",
        "FUNCTION-INDUCTION",
        ("FINITE-COLLISION",),
    ),
    (
        "PROJECTED-ORBIT-PERIODIC",
        "FUNCTION-CONGRUENCE",
        ("FINITE-ORBIT-PERIODIC",),
    ),
    (
        "NO-FINITE-REALIZATION",
        "CONTRADICTION",
        ("PROJECTED-ORBIT-PERIODIC", "P03"),
    ),
)


def mod5(values):
    return tuple(value % P for value in values)


def generator_a(state):
    p1, p4, p1p, p4p, q, r = state
    return (p4, p1, p4p, p1p, q, r)


def generator_b(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5((-p1p, -p4p, -p1, -p4, -q, -r))


def generator_c(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5(
        (
            -p1p + 2,
            -p4p + 1 + r,
            -p1 + 2,
            -p4 + 1 - r,
            1 - q,
            -r,
        )
    )


def generator_d(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5((2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r))


def generator_e(state):
    p1, p4, p1p, p4p, q, r = state
    return mod5((2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r))


COORDINATE_GENERATORS = (
    generator_a,
    generator_b,
    generator_c,
    generator_d,
    generator_e,
)

# Independent matrix-affine encoding of the same five frozen formulas.
AFFINE_MATRICES = (
    (
        (0, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 0),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 1),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, -1),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    (
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0),
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 0),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    (
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0),
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 0),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
)
AFFINE_OFFSETS = (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0),
    (2, 1, 2, 1, 1, 0),
    (2, 1, 3, 4, 1, 1),
    (2, 1, 3, 4, 2, 1),
)


def affine_apply(index, state):
    matrix = AFFINE_MATRICES[index]
    offset = AFFINE_OFFSETS[index]
    return tuple(
        (sum(coefficient * value for coefficient, value in zip(row, state))
         + constant)
        % P
        for row, constant in zip(matrix, offset)
    )


def trace6(state):
    return sum(state) % P


def valid_state(state):
    return (
        isinstance(state, tuple)
        and len(state) == 6
        and all(isinstance(value, int) and 0 <= value < P for value in state)
    )


def popcount(value):
    if value < 0:
        raise ValueError("popcount domain")
    count = 0
    while value:
        count += value & 1
        value >>= 1
    return count


def thue_morse(index):
    return popcount(index) & 1


def thue_morse_recursive(index):
    if index == 0:
        return 0
    return thue_morse_recursive(index >> 1) ^ (index & 1)


def q_label(index):
    if index < 1:
        raise ValueError("q_label domain")
    return (4 + 2 * thue_morse(index - 1)) % P


def q_label_recursive(index):
    if index < 1:
        raise ValueError("q_label_recursive domain")
    return (4 + 2 * thue_morse_recursive(index - 1)) % P


def direct_trajectory(seed, maximum_time):
    states = [seed]
    state = seed
    for index in range(maximum_time):
        selector = (trace6(state) + 2 * thue_morse(index)) % P
        state = COORDINATE_GENERATORS[selector](state)
        states.append(state)
    return tuple(states)


def affine_full_trajectory(seed, maximum_time):
    states = [seed]
    state = seed
    for index in range(maximum_time):
        bit = thue_morse_recursive(index)
        selector = (trace6(state) + 2 * bit) % P
        state = affine_apply(selector, state)
        states.append(state)
    return tuple(states)


def affine_trajectory_for_bits(seed, bits):
    state = seed
    for bit in bits:
        selector = (trace6(state) + 2 * bit) % P
        state = affine_apply(selector, state)
    return state


def independent_sheet(sheet):
    for first_five in product(range(P), repeat=5):
        last = (sheet - sum(first_five)) % P
        yield first_five + (last,)


def affine_trace(generator_index, sheet):
    coefficient, constant = TRACE_AFFINE[generator_index]
    return (coefficient * sheet + constant) % P


def sheet_target(bit, sheet):
    generator_index = (sheet + 2 * bit) % P
    return affine_trace(generator_index, sheet)


def state_text(state):
    return "(" + ",".join(str(value) for value in state) + ")"


def expression_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def expression_subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def validate_proof_graph(graph, external_nodes, terminal_node):
    known = set(external_nodes)
    internal = set()
    for node, rule, premises in graph:
        if node in known or node in internal:
            return False
        if rule not in PROOF_RULE_ARITY:
            return False
        if len(premises) != PROOF_RULE_ARITY[rule]:
            return False
        if any(premise not in known and premise not in internal
               for premise in premises):
            return False
        internal.add(node)
    return bool(graph) and graph[-1][0] == terminal_node


def is_bijection(images, target_states):
    return (
        len(images) == len(target_states)
        and len(set(images)) == len(target_states)
        and set(images) == set(target_states)
    )


def mapping_failure(clause, index, initial_sheet, target_sheet, seed_images,
                    target_states):
    for seed, image in seed_images:
        if trace6(image) != target_sheet:
            return (
                "%s n=%d z=%d kind=wrong-sheet seed=%s image=%s "
                "expected_sheet=%d"
                % (
                    clause,
                    index,
                    initial_sheet,
                    state_text(seed),
                    state_text(image),
                    target_sheet,
                )
            )

    counts = Counter(image for _, image in seed_images)
    for endpoint in target_states:
        count = counts.get(endpoint, 0)
        if count != 1:
            preimages = [
                seed for seed, image in seed_images if image == endpoint
            ][:2]
            preimage_text = (
                "NONE"
                if not preimages
                else "/".join(state_text(seed) for seed in preimages)
            )
            return (
                "%s n=%d z=%d kind=not-bijection endpoint=%s "
                "preimage_count=%d sample_preimages=%s audited_domain=%d"
                % (
                    clause,
                    index,
                    initial_sheet,
                    state_text(endpoint),
                    count,
                    preimage_text,
                    len(seed_images),
                )
            )
    return None


def fiber_failure(clause, index, expected_count, seed_images, target_states):
    counts = Counter(image for _, image in seed_images)
    for endpoint in target_states:
        count = counts.get(endpoint, 0)
        if count != expected_count:
            return (
                "%s n=%d kind=fiber endpoint=%s preimage_count=%d "
                "expected=%d audited_domain=%d"
                % (
                    clause,
                    index,
                    state_text(endpoint),
                    count,
                    expected_count,
                    len(seed_images),
                )
            )
    return None


def collect_candidate_failures(trajectories_by_sheet, target_sheets,
                               label_function):
    failures = []
    s1_maps = 0
    s2_maps = 0
    fibers = 0
    for index in range(3, 7):
        target_sheet = label_function(index)
        combined = []
        for initial_sheet in range(P):
            seed_images = tuple(
                (seed, trajectory[index])
                for seed, trajectory in trajectories_by_sheet[initial_sheet]
            )
            s1_maps += 1
            failure = mapping_failure(
                "S1",
                index,
                initial_sheet,
                target_sheet,
                seed_images,
                target_sheets[target_sheet],
            )
            if failure is not None:
                failures.append(failure)
            combined.extend(seed_images)
        fibers += 1
        failure = fiber_failure(
            "S1",
            index,
            5,
            tuple(combined),
            target_sheets[target_sheet],
        )
        if failure is not None:
            failures.append(failure)

    for index in range(1, 7):
        target_sheet = label_function(index)
        combined = []
        for initial_sheet in (1, 4):
            seed_images = tuple(
                (seed, trajectory[index])
                for seed, trajectory in trajectories_by_sheet[initial_sheet]
            )
            s2_maps += 1
            failure = mapping_failure(
                "S2",
                index,
                initial_sheet,
                target_sheet,
                seed_images,
                target_sheets[target_sheet],
            )
            if failure is not None:
                failures.append(failure)
            combined.extend(seed_images)
        fibers += 1
        failure = fiber_failure(
            "S2",
            index,
            2,
            tuple(combined),
            target_sheets[target_sheet],
        )
        if failure is not None:
            failures.append(failure)
    return failures, s1_maps, s2_maps, fibers


def period_counterwitness(period, threshold):
    if period < 1 or threshold < 0:
        raise ValueError("period witness domain")
    width_floor = (period + threshold).bit_length() + 1
    weight = popcount(period - 1)
    width = width_floor + ((width_floor - weight) & 1)
    left_index = (1 << width) - period
    right_index = 1 << width
    return width, left_index, right_index, weight


def validate_period_counterwitness(period, threshold):
    width, left_index, right_index, weight = period_counterwitness(
        period, threshold
    )
    return (
        left_index >= threshold
        and 0 < period < right_index
        and popcount(left_index) == width - weight
        and thue_morse(left_index) == 0
        and thue_morse(right_index) == 1
        and right_index - left_index == period
    )


def finite_orbit_certificate(mapping, start):
    seen = {}
    sequence = []
    state = start
    while state not in seen:
        seen[state] = len(sequence)
        sequence.append(state)
        state = mapping[state]
    preperiod = seen[state]
    period = len(sequence) - preperiod
    return preperiod, period, tuple(sequence), state


def finite_projection_controls():
    controls_ok = True
    map_count = 0
    projection_count = 0
    for size in range(1, 5):
        for mapping in product(range(size), repeat=size):
            map_count += 1
            preperiod, period, sequence, repeated_state = (
                finite_orbit_certificate(mapping, 0)
            )
            controls_ok &= (
                len(sequence) <= size
                and period >= 1
                and sequence[preperiod] == repeated_state
                and mapping[sequence[-1]] == repeated_state
            )
            for projection in product(range(3), repeat=size):
                projection_count += 1
                state = 0
                values = []
                for _ in range(preperiod + 2 * period):
                    values.append(projection[state])
                    state = mapping[state]
                controls_ok &= all(
                    values[index] == values[index + period]
                    for index in range(preperiod, preperiod + period)
                )
    return controls_ok, map_count, projection_count


def empty_result():
    return {
        "arguments": 0,
        "environment": 0,
        "states": 0,
        "sheets": 0,
        "sheet_size": 0,
        "x14": 0,
        "coordinate_applications": 0,
        "affine_applications": 0,
        "table_transitions": 0,
        "branch_restrictions": 0,
        "branch_states": 0,
        "trajectories": 0,
        "times": 0,
        "s1_maps": 0,
        "s2_maps": 0,
        "fibers": 0,
        "base_s1": 0,
        "base_s2": 0,
        "adjacent_cases": 0,
        "aperiodicity_nodes": 0,
        "aperiodicity_controls": 0,
        "finite_state_nodes": 0,
        "finite_state_controls": 0,
        "i01": False,
        "i02": False,
        "i03": False,
        "a01": False,
        "a02": False,
        "d01": False,
        "d02": False,
        "p01": False,
        "p02": False,
        "p03": False,
        "p04": False,
        "r01": False,
        "stop_reasons": [],
        "counterexamples": [],
    }


def stop(result, code):
    result["stop_reasons"].append(code)


def finish(result):
    stop_codes = sorted(set(result["stop_reasons"]))
    counterexamples = sorted(set(result["counterexamples"]))
    if stop_codes:
        result["diagnostic"] = stop_codes[0]
        result["counterexample"] = "NONE"
        result["integrity"] = "FAIL"
        result["decision"] = "STOP"
        result["route"] = "STOP"
        result["exit"] = 1
    elif counterexamples:
        result["diagnostic"] = "NONE"
        result["counterexample"] = counterexamples[0]
        result["integrity"] = "PASS"
        result["decision"] = "FALSIFIED"
        result["route"] = "FALSIFIED"
        result["exit"] = 0
    else:
        result["diagnostic"] = "NONE"
        result["counterexample"] = "NONE"
        result["integrity"] = "PASS"
        result["decision"] = "PROOF-SURVIVES"
        result["route"] = "PROOF-SURVIVES"
        result["exit"] = 0
    return result


def audit():
    result = empty_result()

    result["arguments"] = max(0, len(sys.argv) - 1)
    result["environment"] = sum(
        os.environ.get(name) == value
        for name, value in REQUIRED_ENVIRONMENT
    )
    result["i01"] = (
        result["arguments"] == 0
        and result["environment"] == len(REQUIRED_ENVIRONMENT)
    )
    if not result["i01"]:
        stop(result, "I01-RUNTIME")
        return finish(result)

    states = tuple(product(range(P), repeat=6))
    direct_sheets = tuple(
        tuple(state for state in states if trace6(state) == sheet)
        for sheet in range(P)
    )
    sheet_route = tuple(
        tuple(independent_sheet(sheet))
        for sheet in range(P)
    )
    result["states"] = len(states)
    result["sheets"] = len(direct_sheets)
    result["sheet_size"] = (
        min(len(sheet) for sheet in direct_sheets)
        if direct_sheets
        else 0
    )
    result["x14"] = len(direct_sheets[1]) + len(direct_sheets[4])
    result["i02"] = (
        len(states) == STATE_COUNT
        and len(set(states)) == STATE_COUNT
        and len(direct_sheets) == P
        and all(len(sheet) == SHEET_COUNT for sheet in direct_sheets)
        and all(len(sheet) == SHEET_COUNT for sheet in sheet_route)
        and all(
            set(direct_sheets[sheet]) == set(sheet_route[sheet])
            for sheet in range(P)
        )
        and result["x14"] == X14_COUNT
        and len(set(direct_sheets[1]) | set(direct_sheets[4])) == X14_COUNT
    )
    if not result["i02"]:
        stop(result, "I02-CARRIER")
        return finish(result)

    coordinate_images = [set() for _ in range(P)]
    affine_images = [set() for _ in range(P)]
    generators_ok = True
    for state in states:
        initial_trace = trace6(state)
        for generator_index, generator in enumerate(COORDINATE_GENERATORS):
            coordinate_image = generator(state)
            affine_image = affine_apply(generator_index, state)
            result["coordinate_applications"] += 1
            result["affine_applications"] += 1
            coordinate_images[generator_index].add(coordinate_image)
            affine_images[generator_index].add(affine_image)
            coefficient, constant = TRACE_AFFINE[generator_index]
            expected_trace = (
                coefficient * initial_trace + constant
            ) % P
            generators_ok &= (
                valid_state(coordinate_image)
                and valid_state(affine_image)
                and coordinate_image == affine_image
                and generator(coordinate_image) == state
                and affine_apply(generator_index, affine_image) == state
                and trace6(coordinate_image) == expected_trace
                and trace6(affine_image) == expected_trace
            )
    generators_ok &= all(
        len(images) == STATE_COUNT
        for images in coordinate_images + affine_images
    )
    result["i03"] = (
        generators_ok
        and result["coordinate_applications"] == P * STATE_COUNT
        and result["affine_applications"] == P * STATE_COUNT
    )
    if not result["i03"]:
        stop(result, "I03-GENERATORS")
        return finish(result)

    derived_table = tuple(
        tuple(sheet_target(bit, sheet) for sheet in range(P))
        for bit in (0, 1)
    )
    result["table_transitions"] = sum(len(row) for row in derived_table)
    result["a01"] = (
        derived_table == EXPECTED_SHEET_TABLE
        and result["table_transitions"] == 10
    )
    if not result["a01"]:
        stop(result, "A01-SHEET-TABLE")

    branch_certificates = {}
    branches_ok = True
    for bit in (0, 1):
        for sheet in range(P):
            generator_index = (sheet + 2 * bit) % P
            target_sheet = EXPECTED_SHEET_TABLE[bit][sheet]
            images = tuple(
                affine_apply(generator_index, state)
                for state in sheet_route[sheet]
            )
            result["branch_restrictions"] += 1
            result["branch_states"] += len(images)
            branch_ok = (
                all(trace6(image) == target_sheet for image in images)
                and is_bijection(images, sheet_route[target_sheet])
            )
            branch_certificates[(bit, sheet)] = branch_ok
            branches_ok &= branch_ok
    result["a02"] = (
        branches_ok
        and result["branch_restrictions"] == 10
        and result["branch_states"] == 10 * SHEET_COUNT
    )
    if not result["a02"]:
        stop(result, "A02-BRANCH-BIJECTIONS")

    trajectories = []
    trajectories_by_sheet = [[] for _ in range(P)]
    affine_trajectories_by_sheet = [[] for _ in range(P)]
    trajectories_ok = True
    affine_trajectories_ok = True
    route_observations_ok = True
    for seed in states:
        trajectory = direct_trajectory(seed, 6)
        affine_trajectory = affine_full_trajectory(seed, 6)
        initial_sheet = trace6(seed)
        trajectories.append((seed, trajectory))
        trajectories_by_sheet[initial_sheet].append((seed, trajectory))
        affine_trajectories_by_sheet[initial_sheet].append(
            (seed, affine_trajectory)
        )
        trajectories_ok &= (
            len(trajectory) == 7
            and trajectory[0] == seed
            and all(valid_state(state) for state in trajectory)
        )
        affine_trajectories_ok &= (
            len(affine_trajectory) == 7
            and affine_trajectory[0] == seed
            and all(valid_state(state) for state in affine_trajectory)
        )
        route_observations_ok &= trajectory == affine_trajectory
    result["trajectories"] = len(trajectories)
    result["times"] = 7
    result["d01"] = (
        trajectories_ok
        and result["trajectories"] == STATE_COUNT
        and all(
            len(sheet_trajectories) == SHEET_COUNT
            for sheet_trajectories in trajectories_by_sheet
        )
    )
    if not result["d01"]:
        stop(result, "D01-DIRECT")

    (
        direct_counterexamples,
        direct_s1_maps,
        direct_s2_maps,
        direct_fibers,
    ) = collect_candidate_failures(
        trajectories_by_sheet,
        direct_sheets,
        q_label,
    )
    (
        affine_counterexamples,
        affine_s1_maps,
        affine_s2_maps,
        affine_fibers,
    ) = collect_candidate_failures(
        affine_trajectories_by_sheet,
        sheet_route,
        q_label_recursive,
    )
    result["counterexamples"].extend(direct_counterexamples)
    result["s1_maps"] = direct_s1_maps
    result["s2_maps"] = direct_s2_maps
    result["fibers"] = direct_fibers
    result["d02"] = (
        not direct_counterexamples
        and direct_s1_maps == 20
        and direct_s2_maps == 12
        and direct_fibers == 10
    )
    affine_candidate_ok = (
        affine_trajectories_ok
        and not affine_counterexamples
        and affine_s1_maps == 20
        and affine_s2_maps == 12
        and affine_fibers == 10
    )

    tm_prefix_coordinate = tuple(thue_morse(index) for index in range(7))
    tm_prefix_recursive = tuple(
        thue_morse_recursive(index) for index in range(7)
    )
    base_bits = (0, 1, 1)
    sheet_sets = [tuple(range(P))]
    current_sheets = set(range(P))
    for bit in base_bits:
        current_sheets = {
            sheet_target(bit, sheet)
            for sheet in current_sheets
        }
        sheet_sets.append(tuple(sorted(current_sheets)))
    expected_sheet_sets = (
        (0, 1, 2, 3, 4),
        (0, 4),
        (1, 2),
        (1,),
    )

    base_s1_ok = True
    for initial_sheet in range(P):
        images = tuple(
            affine_trajectory_for_bits(seed, base_bits)
            for seed in sheet_route[initial_sheet]
        )
        result["base_s1"] += 1
        base_s1_ok &= (
            all(trace6(image) == 1 for image in images)
            and is_bijection(images, sheet_route[1])
        )

    base_s2_ok = True
    for initial_sheet in (1, 4):
        images = tuple(
            affine_trajectory_for_bits(seed, (0,))
            for seed in sheet_route[initial_sheet]
        )
        result["base_s2"] += 1
        base_s2_ok &= (
            all(trace6(image) == 4 for image in images)
            and is_bijection(images, sheet_route[4])
        )

    p01_structure_ok = (
        tm_prefix_coordinate == tm_prefix_recursive
        and tm_prefix_coordinate[:3] == base_bits
        and tuple(sheet_sets) == expected_sheet_sets
        and q_label(3) == 1
        and q_label_recursive(3) == 1
        and result["base_s1"] == 5
        and result["base_s2"] == 2
    )
    result["p01"] = (
        p01_structure_ok
        and base_s1_ok
        and base_s2_ok
    )

    derived_cases = []
    induction_branches_ok = True
    for previous_bit in (0, 1):
        for current_bit in (0, 1):
            current_sheet = (4 + 2 * previous_bit) % P
            selector = (current_sheet + 2 * current_bit) % P
            next_sheet = sheet_target(current_bit, current_sheet)
            derived_cases.append(
                (
                    previous_bit,
                    current_bit,
                    current_sheet,
                    selector,
                    next_sheet,
                )
            )
            result["adjacent_cases"] += 1
            induction_branches_ok &= (
                next_sheet == (4 + 2 * current_bit) % P
                and branch_certificates[(current_bit, current_sheet)]
            )

    fiber_logic_ok = (
        len(set().union(*(set(sheet) for sheet in sheet_route))) == STATE_COUNT
        and all(
            set(sheet_route[left]).isdisjoint(set(sheet_route[right]))
            for left in range(P)
            for right in range(left + 1, P)
        )
        and 5 * SHEET_COUNT == STATE_COUNT
        and 2 * SHEET_COUNT == X14_COUNT
    )
    p02_structure_ok = (
        tuple(derived_cases) == EXPECTED_ADJACENT_CASES
        and induction_branches_ok
        and fiber_logic_ok
        and result["adjacent_cases"] == 4
    )
    result["p02"] = p02_structure_ok

    # Universal complement induction in affine coefficients of (width, weight).
    complement_base = (
        ((1 << 0) - 1) - 0 == 0
        and popcount(0) == 0
    )
    complement_step = True
    for bit in (0, 1):
        prior_complement_weight = (1, -1, 0)
        new_complement_bit = (0, 0, 1 - bit)
        next_width = (1, 0, 1)
        next_input_weight = (0, 1, bit)
        derived_weight = expression_add(
            prior_complement_weight,
            new_complement_bit,
        )
        required_weight = expression_subtract(
            next_width,
            next_input_weight,
        )
        complement_step &= derived_weight == required_weight

    parity_cases = []
    for width_floor_parity in (0, 1):
        for weight_parity in (0, 1):
            residue = (width_floor_parity - weight_parity) % 2
            selected_width_parity = (width_floor_parity + residue) % 2
            contradiction_parity = (
                selected_width_parity - weight_parity
            ) % 2
            parity_cases.append(
                (
                    width_floor_parity,
                    weight_parity,
                    residue,
                    selected_width_parity,
                    contradiction_parity,
                )
            )
    parity_choice = (
        len(parity_cases) == 4
        and all(case[-1] == 0 for case in parity_cases)
    )
    period_controls_ok = all(
        validate_period_counterwitness(period, threshold)
        for period, threshold in PERIOD_CONTROLS
    )
    recoding_values = tuple((4 + 2 * bit) % P for bit in (0, 1))
    recoding_injective = (
        recoding_values == (4, 1)
        and len(set(recoding_values)) == 2
    )
    p03_graph_ok = validate_proof_graph(
        P03_PROOF_GRAPH,
        ("S1",),
        "STATE-NONPERIODIC",
    )
    p03_structure_nodes = (
        complement_base,
        complement_step,
        parity_choice,
        recoding_injective,
        p03_graph_ok,
    )
    p03_structure_ok = all(p03_structure_nodes)
    result["aperiodicity_nodes"] = len(p03_structure_nodes)
    result["aperiodicity_controls"] = len(PERIOD_CONTROLS)
    result["p03"] = (
        p03_structure_ok
        and period_controls_ok
        and result["p01"]
        and result["p02"]
    )

    finite_controls_ok, finite_map_count, finite_projection_count = (
        finite_projection_controls()
    )
    orbit_term_count = (1, 1)
    finite_state_count = (1, 0)
    cardinality_surplus = expression_subtract(
        orbit_term_count,
        finite_state_count,
    )
    pigeonhole_schema = (
        cardinality_surplus == (0, 1)
        and cardinality_surplus[0] == 0
        and cardinality_surplus[1] > 0
    )

    left_orbit_index = (1, 0, 1, 0)
    right_orbit_index = (0, 1, 1, 0)
    one_iteration = (0, 0, 0, 1)
    next_offset = (0, 0, 1, 1)
    propagated_left = expression_add(left_orbit_index, one_iteration)
    propagated_right = expression_add(right_orbit_index, one_iteration)
    required_left = expression_add((1, 0, 0, 0), next_offset)
    required_right = expression_add((0, 1, 0, 0), next_offset)
    propagation_schema = (
        propagated_left == required_left
        and propagated_right == required_right
        and expression_subtract(right_orbit_index, left_orbit_index)
        == (-1, 1, 0, 0)
    )

    state_equality = (
        "EQ",
        ("ORBIT", left_orbit_index),
        ("ORBIT", right_orbit_index),
    )
    projected_equality = (
        "EQ",
        ("PI", state_equality[1]),
        ("PI", state_equality[2]),
    )
    projection_schema = (
        projected_equality[0] == "EQ"
        and projected_equality[1][0] == "PI"
        and projected_equality[2][0] == "PI"
        and projected_equality[1][1] == state_equality[1]
        and projected_equality[2][1] == state_equality[2]
    )
    p04_graph_ok = validate_proof_graph(
        P04_PROOF_GRAPH,
        ("P03",),
        "NO-FINITE-REALIZATION",
    )
    p04_structure_nodes = (
        pigeonhole_schema,
        propagation_schema,
        projection_schema,
        p04_graph_ok,
    )
    p04_structure_ok = all(p04_structure_nodes)
    finite_controls_complete = (
        finite_controls_ok
        and finite_map_count == sum(
            size**size for size in range(1, 5)
        )
        and finite_projection_count == sum(
            (size**size) * (3**size) for size in range(1, 5)
        )
    )
    result["finite_state_nodes"] = len(p04_structure_nodes)
    result["finite_state_controls"] = finite_projection_count
    result["p04"] = (
        p04_structure_ok
        and finite_controls_complete
        and result["p03"]
    )

    sheet_candidate_ok = result["p01"] and result["p02"]
    direct_candidate_ok = result["d02"]
    result["r01"] = (
        route_observations_ok
        and affine_trajectories_ok
        and sorted(set(direct_counterexamples))
        == sorted(set(affine_counterexamples))
        and direct_candidate_ok == affine_candidate_ok
        and affine_candidate_ok == sheet_candidate_ok
        and tm_prefix_coordinate == tm_prefix_recursive
        and result["i03"]
    )
    if not result["r01"]:
        stop(result, "R01-ROUTE-AGREEMENT")

    if not p01_structure_ok:
        stop(result, "P01-STRUCTURE")
    if not p02_structure_ok:
        stop(result, "P02-STRUCTURE")
    if not p03_structure_ok or not period_controls_ok:
        stop(result, "P03-PROOF-GAP")
    if not p04_structure_ok or not finite_controls_complete:
        stop(result, "P04-PROOF-GAP")

    if not result["counterexamples"]:
        if not result["d02"]:
            stop(result, "D02-INCOMPLETE")
        if not result["p01"]:
            stop(result, "P01-PROOF-GAP")
        if not result["p02"]:
            stop(result, "P02-PROOF-GAP")
        if not result["p03"]:
            stop(result, "P03-PROOF-GAP")
        if not result["p04"]:
            stop(result, "P04-PROOF-GAP")

    return finish(result)


def status(value):
    return "PASS" if value else "FAIL"


def render_bytes(result):
    lines = [
        "P-KERNEL-Z6-SYNCHRONIZATION-1 exact verifier",
        "authority base=%s owner_scope=%s"
        % (BASE_COMMIT, OWNER_SCOPE_SHA256),
        "prereg sha256=%s" % PREREG_SHA256,
        "I01 RUNTIME arguments=%d environment=%d: %s"
        % (
            result["arguments"],
            result["environment"],
            status(result["i01"]),
        ),
        "I02 CARRIER states=%d sheets=%d sheet_size=%d x14=%d: %s"
        % (
            result["states"],
            result["sheets"],
            result["sheet_size"],
            result["x14"],
            status(result["i02"]),
        ),
        "I03 GENERATORS coordinate=%d affine=%d: %s"
        % (
            result["coordinate_applications"],
            result["affine_applications"],
            status(result["i03"]),
        ),
        "A01 SHEET-TABLE transitions=%d: %s"
        % (result["table_transitions"], status(result["a01"])),
        "A02 BRANCH-BIJECTIONS restrictions=%d states=%d: %s"
        % (
            result["branch_restrictions"],
            result["branch_states"],
            status(result["a02"]),
        ),
        "D01 DIRECT trajectories=%d times=%d: %s"
        % (
            result["trajectories"],
            result["times"],
            status(result["d01"]),
        ),
        "D02 FIXED-TIME s1_maps=%d s2_maps=%d fibers=%d: %s"
        % (
            result["s1_maps"],
            result["s2_maps"],
            result["fibers"],
            status(result["d02"]),
        ),
        "P01 BASE s1=%d s2=%d: %s"
        % (
            result["base_s1"],
            result["base_s2"],
            status(result["p01"]),
        ),
        "P02 INDUCTION adjacent_cases=%d: %s"
        % (result["adjacent_cases"], status(result["p02"])),
        "P03 APERIODICITY symbolic_nodes=%d controls=%d: %s"
        % (
            result["aperiodicity_nodes"],
            result["aperiodicity_controls"],
            status(result["p03"]),
        ),
        "P04 FINITE-STATE symbolic_nodes=%d controls=%d: %s"
        % (
            result["finite_state_nodes"],
            result["finite_state_controls"],
            status(result["p04"]),
        ),
        "R01 ROUTE-AGREEMENT direct_and_sheet: %s"
        % status(result["r01"]),
        "SCOPE L1 only; fixed-time fibers; no autonomous-state completion",
        "counterexample: %s" % result["counterexample"],
        "diagnostic: %s" % result["diagnostic"],
        "run integrity: %s" % result["integrity"],
        "scientific decision: %s" % result["decision"],
        "route: %s" % result["route"],
    ]
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        result = audit()
        payload = render_bytes(result)
    except BaseException as error:
        result = empty_result()
        stop(result, "E-EXCEPTION-" + type(error).__name__.upper())
        result = finish(result)
        payload = render_bytes(result)
    sys.stdout.buffer.write(payload)
    return result["exit"]


if __name__ == "__main__":
    sys.exit(main())
