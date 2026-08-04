#!/usr/bin/env python3
"""Exact verifier bytes for P-PHOTON-KAPPA-LEMMA-1.

The copy under notes/ is non-formal review material: running that copy is not
a preregistration pin, formal run, result, reproduction, or public evidence.
After the owner accepts its exact public hash in issue #200 and separately
authorizes the formal branch and pin, these same bytes may be copied
byte-identically to the reserved probe.  The surrounding path, immutable
PREREG, remote readback, and authorization determine whether an execution is
formal; the algorithm and transcript do not change between review and pin.

The checker is self-contained and uses only the Python standard library.  It
combines the strict candidate verification and the independent adversarial
boundary audit reviewed on public main, then implements C1-C7 and S1-S5 from
the merged definition package.  Scientific gates use explicit failures, not
assert, so ``python -O`` cannot disable them.
"""

from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys


WITNESS_FILENAME = "witness_6_3_6_6.json"
WITNESS_BYTES = 280106
WITNESS_SHA256 = (
    "9b664f16830d2b562949933e40b4f1460d9da5645a88beff7bca347b70320313"
)
L_PIN = 3240
F_PIN = 7993
EXPECTED_TOP_KEYS = ("P", "m", "C", "D", "L", "F", "j", "n")
OUTCOME = "BELOW-THRESHOLD"
FORBIDDEN_OUTCOME = "CANDIDATE-REFUTED"

# Reviewed source provenance.  These files are not runtime dependencies.
PRIMARY_REFERENCE_SHA256 = (
    "ff462d724f8c724e5df1987d32bbfa3e71518fbec547b00bc1195b567d9c74c0"
)
FRESH_REFERENCE_SHA256 = (
    "c6ae055d30aaf8ec55020db4df1e250f5a65f805b73e521b3db52b59f5c7b9cb"
)
PHOTON_REFERENCE_SHA256_V35 = (
    "d980aa17cd2e597a2924273ea7079333b63419ff472560a395382fa293667e74"
)


class GateFailure(Exception):
    """A named structural, scientific, or systematic gate failed."""

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


def fail(code, message):
    raise GateFailure(code, message)


def require(condition, code, message):
    if not condition:
        fail(code, message)


def canonical_encode(data):
    try:
        text = json.dumps(
            data,
            ensure_ascii=True,
            allow_nan=False,
            separators=(", ", ": "),
        )
        return text.encode("ascii")
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        fail("C1_CANONICAL_BYTES", "canonical JSON encoding failed: %s" % exc)


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        require(
            key not in out,
            "C1_DUPLICATE_OBJECT",
            "duplicate JSON object name %r" % key,
        )
        out[key] = value
    return out


def reject_json_constant(token):
    fail("C1_NUMERIC_TYPE", "non-integer JSON numeric token %s" % token)


def check_numeric_atoms(value, label="top-level JSON value"):
    if type(value) is int:
        return
    if type(value) is list:
        for index, item in enumerate(value):
            check_numeric_atoms(item, "%s[%d]" % (label, index))
        return
    if type(value) is dict:
        for key, item in value.items():
            check_numeric_atoms(item, "%s.%s" % (label, key))
        return
    fail(
        "C1_NUMERIC_TYPE",
        "%s contains a non-integer atom of type %s"
        % (label, type(value).__name__),
    )


def decode_canonical_json(raw):
    require(
        not raw.startswith(b"\xef\xbb\xbf"),
        "C1_UTF8_BOM",
        "UTF-8 BOM is forbidden",
    )
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        fail("C1_UTF8", "fixture is not strict UTF-8: %s" % exc)
    try:
        data = json.loads(
            text,
            object_pairs_hook=unique_object,
            parse_constant=reject_json_constant,
        )
    except json.JSONDecodeError as exc:
        fail("C1_JSON", "invalid JSON: %s" % exc)
    require(type(data) is dict, "C1_SCHEMA", "top-level JSON value is not an object")
    require(
        tuple(data.keys()) == EXPECTED_TOP_KEYS,
        "C1_TOP_KEYS",
        "top-level key order or set differs from the frozen schema",
    )
    check_numeric_atoms(data)
    require(
        raw == canonical_encode(data),
        "C1_CANONICAL_BYTES",
        "raw bytes differ from the frozen canonical JSON encoding",
    )
    return data


def parse_vertex(raw, label):
    require(
        type(raw) is list and len(raw) == 4,
        "C1_VERTEX_SHAPE",
        "%s vertex is not a four-integer list" % label,
    )
    require(
        all(type(x) is int for x in raw),
        "C1_NUMERIC_TYPE",
        "%s vertex contains a non-integer coordinate" % label,
    )
    return tuple(raw)


def parse_schema(data):
    for field in ("P", "m", "C", "D", "L", "F"):
        require(
            type(data[field]) is int,
            "C1_NUMERIC_TYPE",
            "%s is not a strict integer" % field,
        )
    require(data["L"] > 0, "C1_SCHEMA", "L is not positive")
    require(data["F"] >= 0, "C1_SCHEMA", "F is negative")

    raw_j = data["j"]
    require(type(raw_j) is list, "C1_SCHEMA", "j is not a list")
    current = {}
    j_keys = []
    for index, item in enumerate(raw_j):
        label = "j[%d]" % index
        require(
            type(item) is list and len(item) == 3,
            "C1_EDGE_SHAPE",
            "%s is not [vertex,direction,coefficient]" % label,
        )
        vertex = parse_vertex(item[0], label)
        direction, coefficient = item[1], item[2]
        require(
            type(direction) is int and 0 <= direction < 4,
            "C1_DIRECTION",
            "%s direction is outside 0..3" % label,
        )
        require(
            type(coefficient) is int and coefficient in (-1, 1),
            "C1_COEFFICIENT",
            "%s coefficient is not -1 or +1" % label,
        )
        key = (vertex, direction)
        require(
            key not in current,
            "C1_DUPLICATE_EDGE",
            "%s duplicates an earlier edge" % label,
        )
        current[key] = coefficient
        j_keys.append(key)
    require(
        j_keys == sorted(j_keys),
        "C1_EDGE_ORDER",
        "raw j keys are not strictly lexicographically increasing",
    )

    raw_n = data["n"]
    require(type(raw_n) is list, "C1_SCHEMA", "n is not a list")
    faces = {}
    n_keys = []
    for index, item in enumerate(raw_n):
        label = "n[%d]" % index
        require(
            type(item) is list and len(item) == 4,
            "C1_FACE_SHAPE",
            "%s is not [vertex,a,b,coefficient]" % label,
        )
        vertex = parse_vertex(item[0], label)
        a, b, coefficient = item[1], item[2], item[3]
        require(
            type(a) is int and type(b) is int and 0 <= a < b < 4,
            "C1_FACE_DIRECTIONS",
            "%s face directions are invalid" % label,
        )
        require(
            type(coefficient) is int and coefficient in (-1, 1),
            "C1_COEFFICIENT",
            "%s coefficient is not -1 or +1" % label,
        )
        key = (vertex, a, b)
        require(
            key not in faces,
            "C1_DUPLICATE_FACE",
            "%s duplicates an earlier face" % label,
        )
        faces[key] = coefficient
        n_keys.append(key)
    require(
        n_keys == sorted(n_keys),
        "C1_FACE_ORDER",
        "raw n keys are not strictly lexicographically increasing",
    )
    return current, faces


def unit4(direction, step=1):
    value = [0, 0, 0, 0]
    value[direction] = step
    return tuple(value)


def addv(left, right):
    return tuple(a + b for a, b in zip(left, right))


def primary_face_boundary(face):
    vertex, a, b = face
    return (
        ((vertex, a), 1),
        ((addv(vertex, unit4(a)), b), 1),
        ((addv(vertex, unit4(b)), a), -1),
        ((vertex, b), -1),
    )


def primary_face_chain_boundary(faces):
    result = defaultdict(int)
    for face, coefficient in faces.items():
        for edge, incidence in primary_face_boundary(face):
            result[edge] += coefficient * incidence
    return {edge: coefficient for edge, coefficient in result.items() if coefficient}


def primary_edge_chain_boundary(current):
    result = defaultdict(int)
    for (vertex, direction), coefficient in current.items():
        head = addv(vertex, unit4(direction))
        result[vertex] -= coefficient
        result[head] += coefficient
    return {vertex: coefficient for vertex, coefficient in result.items() if coefficient}


def fresh_step(vertex, direction):
    value = list(vertex)
    value[direction] += 1
    return tuple(value)


def fresh_edge_chain_boundary(current):
    result = {}
    for (vertex, direction), coefficient in current.items():
        head = fresh_step(vertex, direction)
        result[vertex] = result.get(vertex, 0) - coefficient
        result[head] = result.get(head, 0) + coefficient
    return {vertex: coefficient for vertex, coefficient in result.items() if coefficient}


def fresh_face_chain_boundary(faces):
    result = {}
    for (vertex, a, b), coefficient in faces.items():
        va = fresh_step(vertex, a)
        vb = fresh_step(vertex, b)
        terms = (
            ((vertex, a), 1),
            ((va, b), 1),
            ((vb, a), -1),
            ((vertex, b), -1),
        )
        for edge, incidence in terms:
            result[edge] = result.get(edge, 0) + coefficient * incidence
    return {edge: coefficient for edge, coefficient in result.items() if coefficient}


def check_c2(current):
    require(current, "C2_ZERO_CURRENT", "j is empty")
    boundary = primary_edge_chain_boundary(current)
    require(not boundary, "C2_NOT_CLOSED", "partial j is nonzero")
    return boundary


def check_c3(current):
    adjacency = defaultdict(list)
    degrees = defaultdict(int)
    outgoing = {}
    incoming_count = defaultdict(int)
    outgoing_count = defaultdict(int)

    for (vertex, direction), coefficient in current.items():
        head = addv(vertex, unit4(direction))
        adjacency[vertex].append(head)
        adjacency[head].append(vertex)
        degrees[vertex] += 1
        degrees[head] += 1
        tail, oriented_head = (
            (vertex, head) if coefficient > 0 else (head, vertex)
        )
        outgoing.setdefault(tail, []).append((oriented_head, (vertex, direction)))
        outgoing.setdefault(oriented_head, [])
        outgoing_count[tail] += 1
        incoming_count[oriented_head] += 1

    start = next(iter(adjacency))
    seen = {start}
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    require(
        len(seen) == len(adjacency),
        "C3_DISCONNECTED",
        "support graph is disconnected",
    )
    require(
        all(degree % 2 == 0 for degree in degrees.values()),
        "C3_ODD_DEGREE",
        "support graph has an odd vertex degree",
    )
    require(
        all(incoming_count[v] == outgoing_count[v] for v in outgoing),
        "C3_DIRECTED_BALANCE",
        "oriented support is not balanced",
    )

    directed_start = next(iter(outgoing))
    next_index = {vertex: 0 for vertex in outgoing}
    vertex_stack = [directed_start]
    edge_stack = []
    circuit = []
    while vertex_stack:
        vertex = vertex_stack[-1]
        if next_index[vertex] < len(outgoing[vertex]):
            neighbor, edge = outgoing[vertex][next_index[vertex]]
            next_index[vertex] += 1
            vertex_stack.append(neighbor)
            edge_stack.append(edge)
        else:
            vertex_stack.pop()
            if edge_stack:
                circuit.append(edge_stack.pop())
    circuit.reverse()

    require(
        len(circuit) == len(current),
        "C3_EULER_LENGTH",
        "Euler traversal misses support edges",
    )
    require(
        len(set(circuit)) == len(circuit),
        "C3_EULER_REUSE",
        "Euler traversal reuses a support edge",
    )
    cursor = directed_start
    for edge in circuit:
        vertex, direction = edge
        head = addv(vertex, unit4(direction))
        tail, oriented_head = (
            (vertex, head) if current[edge] > 0 else (head, vertex)
        )
        require(
            tail == cursor,
            "C3_EULER_ORIENTATION",
            "Euler traversal is not contiguous with current orientation",
        )
        cursor = oriented_head
    require(
        cursor == directed_start,
        "C3_EULER_OPEN",
        "Euler traversal is not closed",
    )
    return len(adjacency), tuple(sorted(set(degrees.values()))), len(circuit)


def check_c4(faces):
    require(
        len(faces) == F_PIN,
        "C4_FACE_SUPPORT",
        "face support cardinality is not %d" % F_PIN,
    )


def check_c5(current, faces):
    target = {edge: 5 * coefficient for edge, coefficient in current.items()}
    primary_dn = primary_face_chain_boundary(faces)
    require(
        primary_dn == target,
        "C5_BOUNDARY",
        "primary partial n is not 5j",
    )
    fresh_dn = fresh_face_chain_boundary(faces)
    require(
        fresh_dn == target,
        "C5_FRESH_BOUNDARY",
        "fresh partial n is not 5j",
    )
    require(
        fresh_dn == primary_dn,
        "C5_BOUNDARY_DISAGREEMENT",
        "independent face-boundary implementations disagree",
    )
    require(
        fresh_edge_chain_boundary(current) == primary_edge_chain_boundary(current),
        "C5_CURRENT_DISAGREEMENT",
        "independent current-boundary implementations disagree",
    )
    require(
        len(primary_dn) == len(current),
        "C5_SUPPORT_COUNT",
        "boundary support count differs from current support count",
    )
    require(
        set(primary_dn.values()) == {-5, 5},
        "C5_BOUNDARY_VALUES",
        "nonzero boundary values are not exactly -5 and +5",
    )
    require(
        not fresh_edge_chain_boundary(primary_dn),
        "C5_BOUNDARY_SQUARED",
        "partial(partial n) is nonzero",
    )


def check_c6(raw, data, current, faces):
    require(
        data["L"] == len(current),
        "C6_DECLARED_L",
        "declared L disagrees with current support",
    )
    require(
        data["F"] == len(faces),
        "C6_DECLARED_F",
        "declared F disagrees with face support",
    )
    require(len(current) == L_PIN, "C6_PINNED_L", "computed L differs from pin")
    require(len(faces) == F_PIN, "C6_PINNED_F", "computed F differs from pin")
    require(
        len(raw) == WITNESS_BYTES,
        "C6_BYTES",
        "fixture byte count differs from pin",
    )
    require(
        sha256(raw).hexdigest() == WITNESS_SHA256,
        "C6_SHA256",
        "fixture SHA-256 differs from pin",
    )


def check_c7(current, faces):
    length = len(current)
    area = len(faces)
    lhs = 2 ** area
    rhs = 7 ** length
    require(lhs <= rhs, "C7_THRESHOLD", "2^F is greater than 7^L")
    bound = rhs.bit_length() - 1
    require(
        2 ** bound <= rhs < 2 ** (bound + 1),
        "C7_BIT_BOUND",
        "B is not the exact binary floor bound",
    )
    require(bound == 9095, "C7_PINNED_B", "B differs from 9095")
    require(area <= bound, "C7_F_ABOVE_B", "F is greater than B")
    require(bound - area == 1102, "C7_SLACK", "B-F differs from 1102")
    return bound, bound - area


def faces_of_edge(edge):
    vertex, direction = edge
    result = []
    for other in range(4):
        if other == direction:
            continue
        a, b = min(direction, other), max(direction, other)
        result.append((vertex, a, b))
        result.append((addv(vertex, unit4(other, -1)), a, b))
    return result


def loop_edges(steps):
    vertex = (0, 0, 0, 0)
    edges = []
    for direction, sign in steps:
        base = vertex if sign > 0 else addv(vertex, unit4(direction, -1))
        edges.append((base, direction))
        vertex = addv(vertex, unit4(direction, sign))
    return vertex, edges


def greedy_lb(edges):
    support = set(edges)
    counts = {}
    for edge in support:
        for face in faces_of_edge(edge):
            if face not in counts:
                face_edges = {item for item, _incidence in primary_face_boundary(face)}
                counts[face] = len(face_edges & support)
    penalty = sum(count - 1 for count in counts.values() if count > 1)
    return 5 * len(support) - penalty


def ladder(length):
    return (
        ((0, 1),) * length
        + ((1, 1),)
        + ((0, -1),) * length
        + ((1, -1),)
    )


SHAPES = (
    ("square-1x1", ladder(1), 17),
    ("ladder-1x2", ladder(2), 26),
    ("ladder-1x3", ladder(3), 35),
    ("ladder-1x4", ladder(4), 44),
    ("ladder-1x5", ladder(5), 53),
    ("ladder-1x6", ladder(6), 62),
    (
        "square-2x2",
        ((0, 1),) * 2
        + ((1, 1),) * 2
        + ((0, -1),) * 2
        + ((1, -1),) * 2,
        36,
    ),
    (
        "skew-hexagon",
        ((0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)),
        24,
    ),
    (
        "staircase",
        (
            (0, 1),
            (1, 1),
            (0, 1),
            (2, 1),
            (0, -1),
            (1, -1),
            (0, -1),
            (2, -1),
        ),
        31,
    ),
)

EXPECTED_SHAPE_ROWS = (
    ("square-1x1", 4, 17),
    ("ladder-1x2", 6, 26),
    ("ladder-1x3", 8, 35),
    ("ladder-1x4", 10, 44),
    ("ladder-1x5", 12, 53),
    ("ladder-1x6", 14, 62),
    ("square-2x2", 8, 36),
    ("skew-hexagon", 6, 24),
    ("staircase", 8, 31),
)


def check_s1():
    rows = []
    rates = []
    for name, steps, expected_lb in SHAPES:
        endpoint, edges = loop_edges(steps)
        require(endpoint == (0, 0, 0, 0), "S1_OPEN_LOOP", "%s is open" % name)
        require(
            len(set(edges)) == len(edges),
            "S1_EDGE_REUSE",
            "%s reuses an edge" % name,
        )
        bound = greedy_lb(edges)
        require(
            bound == expected_lb,
            "S1_BOUND",
            "%s has LB=%d, expected %d" % (name, bound, expected_lb),
        )
        require(
            2 ** bound > 7 ** len(edges),
            "S1_THRESHOLD",
            "%s does not satisfy 2^LB > 7^L" % name,
        )
        rows.append((name, len(edges), bound))
        rates.append(Fraction(bound, len(edges)))
    require(tuple(rows) == EXPECTED_SHAPE_ROWS, "S1_ROWS", "shape rows differ")
    require(min(rates) == Fraction(31, 8), "S1_MINIMUM", "minimum rate differs")
    return len(rows), min(rates)


def modular_step(vertex, direction, periods):
    value = list(vertex)
    value[direction] = (value[direction] + 1) % periods[direction]
    return tuple(value)


def modular_edge_boundary(current, periods):
    result = defaultdict(int)
    for (vertex, direction), coefficient in current.items():
        result[vertex] -= coefficient
        result[modular_step(vertex, direction, periods)] += coefficient
    return {vertex: coefficient for vertex, coefficient in result.items() if coefficient}


def modular_face_boundary(face, periods):
    vertex, a, b = face
    return (
        ((vertex, a), 1),
        ((modular_step(vertex, a, periods), b), 1),
        ((modular_step(vertex, b, periods), a), -1),
        ((vertex, b), -1),
    )


def modular_face_chain_boundary(faces, periods):
    result = defaultdict(int)
    for face, coefficient in faces.items():
        for edge, incidence in modular_face_boundary(face, periods):
            result[edge] += coefficient * incidence
    return {edge: coefficient for edge, coefficient in result.items() if coefficient}


def modular_component_count(current, periods):
    adjacency = defaultdict(list)
    for vertex, direction in current:
        head = modular_step(vertex, direction, periods)
        adjacency[vertex].append(head)
        adjacency[head].append(vertex)
    unseen = set(adjacency)
    components = 0
    while unseen:
        components += 1
        start = next(iter(unseen))
        seen = {start}
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        unseen.difference_update(seen)
    return components


def check_s2():
    periods = (3, 4, 4, 4)
    current = {}
    faces = {}
    for vertex in product(*(range(period) for period in periods)):
        sigma = -1 if (vertex[1] + vertex[2] + vertex[3]) % 2 else 1
        current[(vertex, 0)] = sigma
        faces[(vertex, 0, 1)] = sigma
        faces[(vertex, 0, 2)] = sigma
        n03 = (sigma - 1) // 2
        if n03:
            faces[(vertex, 0, 3)] = n03
    require(
        not modular_edge_boundary(current, periods),
        "S2_TORUS_CURRENT",
        "modular torus current is not closed",
    )
    target = {edge: 5 * coefficient for edge, coefficient in current.items()}
    require(
        modular_face_chain_boundary(faces, periods) == target,
        "S2_TORUS_FILLING",
        "modular torus filling does not satisfy partial n=5j",
    )
    components = modular_component_count(current, periods)
    require(
        components == 64,
        "S2_COMPONENTS",
        "torus current does not have 64 support components",
    )
    require(
        primary_edge_chain_boundary(current),
        "S2_Z4_CLOSED",
        "ordinary nonperiodic Z^4 reinterpretation is unexpectedly closed",
    )
    return components


def run_semantic_through(data, through_gate):
    raw = canonical_encode(data)
    parsed = decode_canonical_json(raw)
    current, faces = parse_schema(parsed)
    if through_gate == 1:
        return
    check_c2(current)
    if through_gate == 2:
        return
    check_c3(current)
    if through_gate == 3:
        return
    check_c4(faces)
    if through_gate == 4:
        return
    check_c5(current, faces)


def expect_target_failure(data, through_gate, expected_code, label):
    try:
        run_semantic_through(data, through_gate)
    except GateFailure as exc:
        require(
            exc.code == expected_code,
            "S3_WRONG_FAILURE",
            "%s failed at %s instead of %s"
            % (label, exc.code, expected_code),
        )
        return expected_code
    fail("S3_MISSED_FAILURE", "%s did not fail" % label)


def check_s3(data):
    require(
        data["n"][0] == [[0, -2, -1, 0], 0, 2, 1],
        "S3_BASELINE",
        "first face differs from the frozen mutation anchor",
    )
    require(
        data["j"][0] == [[0, -2, 0, 0], 0, -1],
        "S3_BASELINE",
        "first edge differs from the frozen mutation anchor",
    )

    face_flip = deepcopy(data)
    face_flip["n"][0][3] = -1
    code1 = expect_target_failure(face_flip, 5, "C5_BOUNDARY", "face flip")

    edge_delete = deepcopy(data)
    del edge_delete["j"][0]
    code2 = expect_target_failure(
        edge_delete, 2, "C2_NOT_CLOSED", "edge deletion"
    )

    face_duplicate = deepcopy(data)
    face_duplicate["n"].insert(1, deepcopy(face_duplicate["n"][0]))
    code3 = expect_target_failure(
        face_duplicate, 1, "C1_DUPLICATE_FACE", "face duplication"
    )

    coefficient_two = deepcopy(data)
    coefficient_two["j"][0][2] = 2
    code4 = expect_target_failure(
        coefficient_two, 1, "C1_COEFFICIENT", "coefficient two"
    )

    bridge_inverse = deepcopy(data)
    bridge_one = [[1, 1, 0, 0], 3, 1]
    bridge_two = [[2, 1, 0, 0], 3, -1]
    restored_one = [[1, 1, 0, 0], 0, 1]
    restored_two = [[1, 1, 0, 1], 0, -1]
    require(
        bridge_one in bridge_inverse["j"] and bridge_two in bridge_inverse["j"],
        "S3_BASELINE",
        "bridge mutation anchors are absent",
    )
    require(
        restored_one not in bridge_inverse["j"]
        and restored_two not in bridge_inverse["j"],
        "S3_BASELINE",
        "restored bridge edges are unexpectedly present",
    )
    bridge_inverse["j"].remove(bridge_one)
    bridge_inverse["j"].remove(bridge_two)
    bridge_inverse["j"].extend((restored_one, restored_two))
    bridge_inverse["j"].sort(key=lambda item: (tuple(item[0]), item[1]))
    code5 = expect_target_failure(
        bridge_inverse, 3, "C3_DISCONNECTED", "bridge inverse reroute"
    )
    return (code1, code2, code3, code4, code5)


@dataclass(frozen=True)
class Evaluation:
    length: int
    area: int
    vertices: int
    degrees: tuple
    euler_steps: int
    bound: int
    slack: int
    shape_count: int
    minimum_rate: Fraction
    torus_components: int
    mutation_codes: tuple


def evaluate_once(raw):
    data = decode_canonical_json(raw)
    current, faces = parse_schema(data)
    check_c2(current)
    vertices, degrees, euler_steps = check_c3(current)
    check_c4(faces)
    check_c5(current, faces)
    check_c6(raw, data, current, faces)
    bound, slack = check_c7(current, faces)
    shape_count, minimum_rate = check_s1()
    torus_components = check_s2()
    mutation_codes = check_s3(data)
    return Evaluation(
        length=len(current),
        area=len(faces),
        vertices=vertices,
        degrees=degrees,
        euler_steps=euler_steps,
        bound=bound,
        slack=slack,
        shape_count=shape_count,
        minimum_rate=minimum_rate,
        torus_components=torus_components,
        mutation_codes=mutation_codes,
    )


def render_transcript(result):
    require(result.length == L_PIN, "S4_RENDER", "rendered L differs")
    require(result.area == F_PIN, "S4_RENDER", "rendered F differs")
    require(result.degrees == (2, 4), "S4_RENDER", "rendered degrees differ")
    require(
        result.minimum_rate == Fraction(31, 8),
        "S4_RENDER",
        "rendered minimum rate differs",
    )
    codes = result.mutation_codes
    lines = (
        "P-PHOTON-KAPPA-LEMMA-1",
        "PIN PASS witness=%s bytes=%d sha256=%s"
        % (WITNESS_FILENAME, WITNESS_BYTES, WITNESS_SHA256),
        "C1 PASS schema=exact canonical-json=yes j-keys=%d n-keys=%d"
        % (result.length, result.area),
        "C2 PASS current=nonzero partial-j=0",
        "C3 PASS connected=yes vertices=%d degrees=%s euler-steps=%d"
        % (result.vertices, ",".join(str(x) for x in result.degrees), result.euler_steps),
        "C4 PASS face-chain=ternary support=%d" % result.area,
        "C5 PASS partial-n=5j boundary-support=%d boundary-values=-5,5"
        % result.length,
        "C6 PASS L=%d F=%d header-counts=exact pinned-counts=exact"
        % (result.length, result.area),
        "C7 PASS 2^F<=7^L B=%d slack=%d" % (result.bound, result.slack),
        "S1 PASS shapes=%d min-LB/L=%d/%d all-2^LB>7^L"
        % (
            result.shape_count,
            result.minimum_rate.numerator,
            result.minimum_rate.denominator,
        ),
        "S2 PASS torus-periods=3,4,4,4 out-of-carrier=yes components=%d"
        % result.torus_components,
        "S3 PASS mutations=5 face-flip:%s edge-delete:%s "
        "face-duplicate:%s coeff-2:%s bridge-inverse:%s" % codes,
        "S4 PASS evaluations=2 transcript=byte-identical",
        "S5 PASS outcome-vocabulary=%s" % OUTCOME,
        "OUTCOME %s" % OUTCOME,
        "RESULT 12/12 ALL PASS",
    )
    return ("\n".join(lines) + "\n").encode("ascii")


def check_s5(transcript):
    require(
        transcript.endswith(b"\n"),
        "S5_TERMINAL_LF",
        "successful transcript lacks one terminal LF",
    )
    lines = transcript.decode("ascii").splitlines()
    outcome_lines = [line for line in lines if line.startswith("OUTCOME ")]
    require(
        outcome_lines == ["OUTCOME %s" % OUTCOME],
        "S5_OUTCOME",
        "successful transcript has the wrong outcome line",
    )
    require(
        FORBIDDEN_OUTCOME.encode("ascii") not in transcript,
        "S5_VOCABULARY",
        "successful transcript contains superseded outcome vocabulary",
    )


def emit_failure(code, message):
    line = "P-PHOTON-KAPPA-LEMMA-1 STOP %s: %s\n" % (code, message)
    sys.stderr.buffer.write(line.encode("ascii", errors="backslashreplace"))


def main(argv):
    if len(argv) != 1:
        sys.stderr.buffer.write(b"usage: verify.py\n")
        return 2
    witness_path = Path(__file__).resolve().parent / WITNESS_FILENAME
    try:
        try:
            raw_first = witness_path.read_bytes()
            raw_second = witness_path.read_bytes()
        except OSError:
            fail("C6_READ", "cannot read adjacent pinned witness")
        require(
            raw_first == raw_second,
            "S4_INPUT_CHANGED",
            "adjacent witness changed between consecutive reads",
        )
        first = evaluate_once(raw_first)
        second = evaluate_once(raw_second)
        require(
            first == second,
            "S4_EVALUATION",
            "two consecutive evaluations differ",
        )
        transcript_first = render_transcript(first)
        transcript_second = render_transcript(second)
        require(
            transcript_first == transcript_second,
            "S4_TRANSCRIPT",
            "two rendered transcripts differ",
        )
        check_s5(transcript_first)
    except GateFailure as exc:
        emit_failure(exc.code, exc.message)
        return 1
    except Exception as exc:  # defensive STOP; no scientific outcome is emitted
        emit_failure("INTERNAL", "%s: %s" % (type(exc).__name__, exc))
        return 1
    sys.stdout.buffer.write(transcript_first)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
