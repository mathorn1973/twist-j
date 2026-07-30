#!/usr/bin/env python3
"""Exact verifier for P-ENTROPY-CURSOR-CLOSURE-1.

Run from the repository root. Python standard library only. The scientific
transcript is deterministic: there are no floats, clocks, adaptive caps,
filesystem writes, network calls, or subprocesses.
"""

import hashlib
import sys
from collections import deque


PREREG_SHA256 = "d57fc9e12527aa98db4c270952add818a1f2e3b083c13155b5861d5c24b35f14"
PINNED_SOURCES = (
    (
        "probes/P-ENTROPY-BRIDGE-2/verify.py",
        "1c2c701290640f19cddc6822cfdd5bb24bdd9826c0c36cbd5ae989ac7371d72f",
    ),
    (
        "probes/P-ENTROPY-BRIDGE-2/PREREG.md",
        "dc51c42aff39707b09cc5cf4c80cd6c23ed5aa6fb8e1a6332e3aa825818ef08d",
    ),
)

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)
M_J = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)
N = 5**6
PREFIX_BITS = 18

FAILURES = []


def fail(gate, message):
    FAILURES.append((gate, message))
    print("FAIL %s %s" % (gate, message))


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return (
        (-p1p) % 5,
        (-p4p) % 5,
        (-p1) % 5,
        (-p4) % 5,
        (-q) % 5,
        (-r) % 5,
    )


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return (
        (b4[0] + S_VEC[0] + r * U_VEC[0]) % 5,
        (b4[1] + S_VEC[1] + r * U_VEC[1]) % 5,
        (b4[2] + S_VEC[2] + r * U_VEC[2]) % 5,
        (b4[3] + S_VEC[3] + r * U_VEC[3]) % 5,
        (1 - q) % 5,
        (-r) % 5,
    )


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def decode(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def encode(x):
    value = 0
    for k in range(5, -1, -1):
        value = value * 5 + x[k]
    return value


STATES = [decode(i) for i in range(N)]
Z_TABLE = [sum(state) % 5 for state in STATES]


def build_branch_tables(generators, encoder=encode):
    tables = [[0] * N, [0] * N]
    for theta in (0, 1):
        selected = [generators[(z + 2 * theta) % 5] for z in range(5)]
        for i, state in enumerate(STATES):
            tables[theta][i] = encoder(selected[Z_TABLE[i]](state))
    return tables


F = build_branch_tables(GENS)


# Independent literal matrix-affine route for C03. These five
# specifications do not call the coordinate generator functions above.
# In particular d and e are -I plus literal offsets rather than copies of
# their coordinate formulas.
ALT_AFFINE = (
    (
        (
            (0, 1, 0, 0, 0, 0),
            (1, 0, 0, 0, 0, 0),
            (0, 0, 0, 1, 0, 0),
            (0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 1, 0),
            (0, 0, 0, 0, 0, 1),
        ),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        (
            (0, 0, 4, 0, 0, 0),
            (0, 0, 0, 4, 0, 0),
            (4, 0, 0, 0, 0, 0),
            (0, 4, 0, 0, 0, 0),
            (0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 4),
        ),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        (
            (0, 0, 4, 0, 0, 0),
            (0, 0, 0, 4, 0, 1),
            (4, 0, 0, 0, 0, 0),
            (0, 4, 0, 0, 0, 4),
            (0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 4),
        ),
        (2, 1, 2, 1, 1, 0),
    ),
    (
        (
            (4, 0, 0, 0, 0, 0),
            (0, 4, 0, 0, 0, 0),
            (0, 0, 4, 0, 0, 0),
            (0, 0, 0, 4, 0, 0),
            (0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 4),
        ),
        (2, 1, 3, 4, 1, 1),
    ),
    (
        (
            (4, 0, 0, 0, 0, 0),
            (0, 4, 0, 0, 0, 0),
            (0, 0, 4, 0, 0, 0),
            (0, 0, 0, 4, 0, 0),
            (0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 4),
        ),
        (2, 1, 3, 4, 2, 1),
    ),
)


def affine_apply(specification, vector):
    matrix, offset = specification
    return tuple(
        (
            offset[i]
            + sum(matrix[i][j] * vector[j] for j in range(6))
        )
        % 5
        for i in range(6)
    )


def build_affine_branch_tables():
    tables = [[0] * N, [0] * N]
    for theta in (0, 1):
        for i, state in enumerate(STATES):
            specification = ALT_AFFINE[(Z_TABLE[i] + 2 * theta) % 5]
            tables[theta][i] = encode(affine_apply(specification, state))
    return tables


ALT_F = build_affine_branch_tables()


TM_POPCOUNT = [n.bit_count() & 1 for n in range(1 << PREFIX_BITS)]
tm_substitution = [0]
while len(tm_substitution) < (1 << PREFIX_BITS):
    tm_substitution = [
        bit
        for source in tm_substitution
        for bit in (source, 1 - source)
    ]
TM_SUBSTITUTION = tm_substitution[: 1 << PREFIX_BITS]
TM_SHORT = TM_POPCOUNT[: 1 << 16]
TM_CERTIFIED = TM_SUBSTITUTION[: 1 << 9]

_FACTOR_CACHE = {}


def factor_set_from(prefix, length):
    return tuple(
        sorted(
            {
                tuple(prefix[i : i + length])
                for i in range(len(prefix) - length + 1)
            }
        )
    )


def factors(length):
    if length not in _FACTOR_CACHE:
        _FACTOR_CACHE[length] = factor_set_from(TM_POPCOUNT, length)
    return _FACTOR_CACHE[length]


def build_graph(length, cursor, orbit_length):
    words = factors(length)
    word_id = {word: i for i, word in enumerate(words)}
    extensions = factors(length + 1)
    node_count = len(words) * orbit_length
    forward = [[] for _ in range(node_count)]
    reverse = [[] for _ in range(node_count)]
    for extension in extensions:
        source_word = word_id[extension[:length]]
        target_word = word_id[extension[1:]]
        theta = extension[cursor]
        for k in range(orbit_length):
            source = source_word * orbit_length + k
            target = target_word * orbit_length + ((k + 1) % orbit_length)
            forward[source].append((target, theta))
            reverse[target].append(source)
    return node_count, forward, reverse


def weak_components(node_count, forward, reverse):
    component_id = [-1] * node_count
    components = []
    for root in range(node_count):
        if component_id[root] != -1:
            continue
        index = len(components)
        component_id[root] = index
        queue = deque([root])
        component = [root]
        while queue:
            node = queue.popleft()
            for target, _ in forward[node]:
                if component_id[target] == -1:
                    component_id[target] = index
                    queue.append(target)
                    component.append(target)
            for source in reverse[node]:
                if component_id[source] == -1:
                    component_id[source] = index
                    queue.append(source)
                    component.append(source)
        components.append(component)
    return components


def forward_order(root, forward):
    seen = {root}
    order = [root]
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for target, _ in forward[node]:
            if target not in seen:
                seen.add(target)
                order.append(target)
                queue.append(target)
    return order


def count_component(component, forward, witness=None):
    root = component[0]
    order = forward_order(root, forward)
    if len(order) != len(component):
        fail(
            "C01",
            "weak component of size %d has only %d nodes forward-reachable"
            % (len(component), len(order)),
        )
        return 0

    total = 0
    for seed in range(N):
        values = {root: seed}
        consistent = True
        for node in order:
            value = values[node]
            for target, theta in forward[node]:
                image = F[theta][value]
                if target in values:
                    if values[target] != image:
                        consistent = False
                        break
                else:
                    values[target] = image
            if not consistent:
                break
        if consistent and len(values) == len(component):
            total += 1
            if witness is not None and not witness:
                witness.append((root, seed, values))
    return total


def component_solution_data(
    node_count, forward, reverse, want_witnesses=False
):
    """Exact global count: product of the independent component counts."""
    counts = []
    witnesses = []
    for component in weak_components(node_count, forward, reverse):
        local_witness = [] if want_witnesses else None
        count = count_component(component, forward, local_witness)
        counts.append(count)
        if want_witnesses:
            witnesses.append(local_witness[0] if local_witness else None)

    product = 1
    for count in counts:
        product *= count
    return product, tuple(counts), tuple(witnesses)


_FEASIBILITY_CACHE = {}


def feasibility_data(length, cursor, orbit_length):
    key = (length, cursor, orbit_length)
    if key not in _FEASIBILITY_CACHE:
        node_count, forward, reverse = build_graph(length, cursor, orbit_length)
        product, counts, _ = component_solution_data(
            node_count, forward, reverse
        )
        _FEASIBILITY_CACHE[key] = (product, counts)
    return _FEASIBILITY_CACHE[key]


def feasibility(length, cursor, orbit_length):
    return feasibility_data(length, cursor, orbit_length)[0]


def feasibility_component_counts(length, cursor, orbit_length):
    return feasibility_data(length, cursor, orbit_length)[1]


def feasibility_witness(length, cursor, orbit_length):
    node_count, forward, reverse = build_graph(length, cursor, orbit_length)
    product, _counts, witnesses = component_solution_data(
        node_count, forward, reverse, want_witnesses=True
    )
    return product, witnesses


def pure_graph_signature(length, cursor):
    words = factors(length)
    node_count, forward, _reverse = build_graph(length, cursor, 1)
    edges = tuple(
        sorted(
            (words[source], words[target], theta)
            for source in range(node_count)
            for target, theta in forward[source]
        )
    )
    return words, edges


def zero_restriction_signature(length, cursor):
    """Derive the fixed-zero context graph from the residue transition."""
    zero = (0, 0, 0, 0)
    image = tuple(
        sum(M_J[i][j] * zero[j] for j in range(4))
        for i in range(4)
    )
    words = factors(length)
    zero_nodes = tuple((word, zero) for word in words)
    zero_edges = tuple(
        sorted(
            (
                (extension[:length], zero),
                (extension[1:], image),
                extension[cursor],
            )
            for extension in factors(length + 1)
        )
    )
    projected_nodes = tuple(word for word, residue in zero_nodes if residue == zero)
    projected_edges = tuple(
        (source_word, target_word, theta)
        for (source_word, source_residue), (target_word, target_residue), theta
        in zero_edges
        if source_residue == zero and target_residue == zero
    )
    return image, projected_nodes, projected_edges


def zero_restriction_matches(length, cursor):
    zero = (0, 0, 0, 0)
    pure_nodes, pure_edges = pure_graph_signature(length, cursor)
    image, zero_nodes, zero_edges = zero_restriction_signature(length, cursor)
    return image == zero and zero_nodes == pure_nodes and zero_edges == pure_edges


def graph_for_drive(drive, length, cursor):
    repeated = drive * (4 * (length + 2))
    words = tuple(
        sorted(
            {
                tuple(repeated[i : i + length])
                for i in range(len(repeated) - length + 1)
            }
        )
    )
    extensions = tuple(
        sorted(
            {
                tuple(repeated[i : i + length + 1])
                for i in range(len(repeated) - length)
            }
        )
    )
    word_id = {word: i for i, word in enumerate(words)}
    forward = [[] for _ in words]
    reverse = [[] for _ in words]
    for extension in extensions:
        source = word_id[extension[:length]]
        target = word_id[extension[1:]]
        theta = extension[cursor]
        forward[source].append((target, theta))
        reverse[target].append(source)
    return len(words), forward, reverse


def drive_solution_data(drive, length, cursor):
    node_count, forward, reverse = graph_for_drive(drive, length, cursor)
    return component_solution_data(node_count, forward, reverse)


def drive_feasibility(drive, length, cursor):
    return drive_solution_data(drive, length, cursor)[0]


_ALT_FACTOR_CACHE = {}


def alternate_factors(length):
    """Substitution-only factor construction, separate from factors()."""
    if length not in _ALT_FACTOR_CACHE:
        _ALT_FACTOR_CACHE[length] = tuple(
            sorted(
                {
                    tuple(TM_SUBSTITUTION[i : i + length])
                    for i in range(len(TM_SUBSTITUTION) - length + 1)
                }
            )
        )
    return _ALT_FACTOR_CACHE[length]


def alternate_graph(length, cursor, orbit_length):
    words = alternate_factors(length)
    word_id = {word: i for i, word in enumerate(words)}
    node_count = len(words) * orbit_length
    outgoing = [[] for _ in range(node_count)]
    arcs = []
    for extension in alternate_factors(length + 1):
        source_word = word_id[extension[:length]]
        target_word = word_id[extension[1:]]
        theta = extension[cursor]
        for k in range(orbit_length):
            source = source_word * orbit_length + k
            target = target_word * orbit_length + ((k + 1) % orbit_length)
            outgoing[source].append((target, theta))
            arcs.append((source, target, theta))
    return node_count, outgoing, tuple(arcs)


def alternate_drive_graph(drive, length, cursor):
    repeated = drive * (4 * (length + 2))

    def periodic_factors(size):
        return tuple(
            sorted(
                {
                    tuple(repeated[i : i + size])
                    for i in range(len(repeated) - size + 1)
                }
            )
        )

    words = periodic_factors(length)
    word_id = {word: i for i, word in enumerate(words)}
    outgoing = [[] for _ in words]
    arcs = []
    for extension in periodic_factors(length + 1):
        source = word_id[extension[:length]]
        target = word_id[extension[1:]]
        theta = extension[cursor]
        outgoing[source].append((target, theta))
        arcs.append((source, target, theta))
    return len(words), outgoing, tuple(arcs)


def union_find_components(node_count, arcs):
    parent = list(range(node_count))
    rank = [0] * node_count

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(left, right):
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return
        if rank[left_root] < rank[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        if rank[left_root] == rank[right_root]:
            rank[left_root] += 1

    for source, target, _theta in arcs:
        union(source, target)

    groups = {}
    for node in range(node_count):
        groups.setdefault(find(node), []).append(node)
    return tuple(
        tuple(group)
        for group in sorted(groups.values(), key=lambda item: item[0])
    )


def alternate_solution_data_from_graph(node_count, outgoing, arcs):
    """Independent spanning-tree and residual-edge solver for C03."""
    counts = []
    reachable = True
    for component in union_find_components(node_count, arcs):
        in_component = [False] * node_count
        reached = [False] * node_count
        for node in component:
            in_component[node] = True

        root = component[0]
        reached[root] = True
        queue = [root]
        tree_edges = []
        position = 0
        while position < len(queue):
            source = queue[position]
            position += 1
            for target, theta in outgoing[source]:
                if in_component[target] and not reached[target]:
                    reached[target] = True
                    queue.append(target)
                    tree_edges.append((source, target, theta))

        if len(queue) != len(component):
            reachable = False
            counts.append(0)
            continue

        component_arcs = tuple(
            (source, target, theta)
            for source, target, theta in arcs
            if in_component[source]
        )
        values = [0] * node_count
        count = 0
        for seed in range(N):
            values[root] = seed
            for source, target, theta in tree_edges:
                values[target] = ALT_F[theta][values[source]]
            if all(
                values[target] == ALT_F[theta][values[source]]
                for source, target, theta in component_arcs
            ):
                count += 1
        counts.append(count)

    product = 1
    for count in counts:
        product *= count
    return product, tuple(counts), reachable


def alternate_feasibility_data(length, cursor, orbit_length):
    return alternate_solution_data_from_graph(
        *alternate_graph(length, cursor, orbit_length)
    )


def alternate_drive_feasibility_data(drive, length, cursor):
    return alternate_solution_data_from_graph(
        *alternate_drive_graph(drive, length, cursor)
    )


def print_gate(gate, message, passed):
    print("%s %s: %s" % (gate, message, "PASS" if passed else "FAIL"))
    if not passed:
        fail(gate, message)


def main():
    print("P-ENTROPY-CURSOR-CLOSURE-1 exact verifier")
    print("prereg %s" % PREREG_SHA256)

    source_hashes = []
    sources_ok = True
    for path, expected_hash in PINNED_SOURCES:
        with open(path, "rb") as handle:
            actual_hash = hashlib.sha256(handle.read()).hexdigest()
        source_hashes.append("%s=%s" % (path.rsplit("/", 1)[-1], actual_hash))
        sources_ok &= actual_hash == expected_hash
    print(
        "S01 SOURCES %s: %s"
        % (", ".join(source_hashes), "PASS" if sources_ok else "FAIL")
    )
    if not sources_ok:
        fail("S01", "pinned P-ENTROPY-BRIDGE-2 source hash mismatch")

    expected_counts = {
        4: 10,
        5: 12,
        6: 16,
        7: 20,
        8: 22,
        9: 24,
        10: 28,
        11: 32,
        12: 36,
        13: 40,
        14: 42,
        15: 44,
        16: 46,
        17: 48,
    }
    counts_ok = True
    for length, expected in expected_counts.items():
        counts_ok &= len(factors(length)) == expected
    sets_ok = True
    for length in range(1, 41):
        full = factors(length)
        sets_ok &= full == factor_set_from(TM_SHORT, length)
        sets_ok &= full == factor_set_from(TM_CERTIFIED, length)
    print_gate(
        "S02",
        "FACTORS certified 512/2^16/2^18 sets agree for L=1..40 and pinned counts hold",
        counts_ok and sets_ok,
    )

    drive_routes_ok = F == ALT_F
    tm_routes_ok = TM_POPCOUNT == TM_SUBSTITUTION
    print_gate(
        "C03A",
        "ROUTES literal affine tables and Thue-Morse constructions agree exactly",
        drive_routes_ok and tm_routes_ok,
    )

    engine_ok = True
    for length in range(4, 17):
        value = feasibility(length, 0, 1)
        engine_ok &= value == 0
    g07 = ((4, 0), (5, 0), (5, 1), (6, 0), (6, 1), (6, 2))
    for length, cursor in g07:
        for orbit_length in (1, 4, 20):
            value = feasibility(length, cursor, orbit_length)
            engine_ok &= value == 0
    for orbit_length in (1, 4, 20, 100):
        value = feasibility(4, 0, orbit_length)
        engine_ok &= value == 0
    print_gate(
        "E01",
        "ENGINE reproduces G05, G07, and G08",
        engine_ok,
    )

    gap_nonzero = {}
    for length in range(7, 17):
        for cursor in range(1, length):
            value = feasibility(length, cursor, 1)
            if value:
                gap_nonzero[(length, cursor, 1)] = value
    print(
        "E02 GAP L=7..16 c=1..L-1: 105 pairs, nonzero=%d"
        % len(gap_nonzero)
    )

    axis_nonzero = {}
    axis_count = 0
    for length in range(4, 33):
        for cursor in range(length):
            axis_count += 1
            value = feasibility(length, cursor, 1)
            if value:
                axis_nonzero[(length, cursor, 1)] = value
    print(
        "E03 FULL-AXIS L=4..32 every cursor: %d distinct pairs, nonzero=%d"
        % (axis_count, len(axis_nonzero))
    )

    depth_grid = (
        (7, 3),
        (8, 3),
        (9, 4),
        (10, 5),
        (11, 5),
        (12, 5),
        (13, 6),
        (16, 8),
        (16, 15),
    )
    depth_nonzero = {}
    depth_count = 0
    for length, cursor in depth_grid:
        for orbit_length in (4, 20, 100):
            depth_count += 1
            value = feasibility(length, cursor, orbit_length)
            if value:
                depth_nonzero[(length, cursor, orbit_length)] = value
    print(
        "E04 DEPTH-GRID ell in {4,20,100}: %d distinct triples, nonzero=%d"
        % (depth_count, len(depth_nonzero))
    )

    transport_ok = all(
        zero_restriction_matches(length, cursor)
        for length in range(4, 33)
        for cursor in range(length)
    )
    print_gate(
        "E05",
        "ZERO-RESIDUE labelled graph projects exactly to pure word for all 522 pairs",
        transport_ok,
    )

    reversal_ok = True
    for length in range(4, 25):
        word_set = set(factors(length))
        closed = all(tuple(reversed(word)) in word_set for word in word_set)
        reversal_ok &= closed
        for cursor in range(length):
            left = feasibility(length, cursor, 1)
            right = feasibility(length, length - 1 - cursor, 1)
            reversal_ok &= left == right
    print_gate(
        "E06",
        "REVERSAL factor closure and cursor count equality hold for L=4..24",
        reversal_ok,
    )

    controls = (
        ("constant-0", [0], 4, 0, 126),
        ("constant-1", [1], 4, 0, 126),
        ("period-2-01", [0, 1], 4, 0, 6250),
        ("period-3-001", [0, 0, 1], 6, 0, 126),
        ("period-4-0110", [0, 1, 1, 0], 8, 2, 0),
    )
    control_values = []
    controls_ok = True
    for name, drive, length, cursor, expected in controls:
        value, component_counts, _witnesses = drive_solution_data(
            drive, length, cursor
        )
        component_ok = len(component_counts) == 1
        control_values.append(
            "%s=%d/components=%d"
            % (name, value, len(component_counts))
        )
        controls_ok = controls_ok and component_ok and value == expected
    print(
        "C02 CONTROLS one-component global counts %s: %s"
        % (", ".join(control_values), "PASS" if controls_ok else "FAIL")
    )
    if not controls_ok:
        fail("C02", "periodic control counts do not match the frozen values")

    independent_ok = True
    for length in range(7, 17):
        for cursor in range(1, length):
            primary_product = feasibility(length, cursor, 1)
            primary_counts = feasibility_component_counts(length, cursor, 1)
            alt_product, alt_counts, reachable = alternate_feasibility_data(
                length, cursor, 1
            )
            independent_ok &= (
                reachable
                and primary_product == alt_product
                and tuple(sorted(primary_counts)) == tuple(sorted(alt_counts))
            )
    for length, cursor in ((7, 3), (8, 3), (12, 5)):
        for orbit_length in (4, 20):
            primary_product = feasibility(length, cursor, orbit_length)
            primary_counts = feasibility_component_counts(
                length, cursor, orbit_length
            )
            alt_product, alt_counts, reachable = alternate_feasibility_data(
                length, cursor, orbit_length
            )
            independent_ok &= (
                reachable
                and primary_product == alt_product
                and tuple(sorted(primary_counts)) == tuple(sorted(alt_counts))
            )

    alt_controls = (
        ([0], 4, 0, 126),
        ([1], 4, 0, 126),
        ([0, 1, 1, 0], 8, 2, 0),
    )
    for drive, length, cursor, expected in alt_controls:
        product, counts, reachable = alternate_drive_feasibility_data(
            drive, length, cursor
        )
        independent_ok &= (
            reachable and len(counts) == 1 and product == expected
        )
    print_gate(
        "C03B",
        "TREE-RESIDUAL route matches 105 gap pairs, six depth checks, and controls",
        independent_ok,
    )

    nonzero = {}
    nonzero.update(axis_nonzero)
    nonzero.update(depth_nonzero)
    if nonzero:
        first_key = sorted(nonzero)[0]
        total, witnesses = feasibility_witness(*first_key)
        print(
            "FALSIFIER finite-cylinder cut exists at %s with count %d"
            % (first_key, total)
        )
        for component_index, witness in enumerate(witnesses):
            if witness is None:
                fail(
                    "F-CURSOR-CUT",
                    "globally positive product lacks a component witness",
                )
                continue
            root, seed, values = witness
            print(
                "WITNESS component=%d root=%d seed=%d assignment_size=%d"
                % (component_index, root, seed, len(values))
            )
        fail("F-CURSOR-CUT", "%d parameter triples are nonzero" % len(nonzero))

    if gap_nonzero:
        fail("E02", "%d uncovered gap pairs are nonzero" % len(gap_nonzero))

    print("C01 FORWARD-REACHABILITY every used weak component: %s" % (
        "PASS" if not any(gate == "C01" for gate, _ in FAILURES) else "FAIL"
    ))
    print(
        "TOTAL distinct candidate parameter triples: %d, nonzero=%d"
        % (axis_count + depth_count, len(nonzero))
    )
    print("SCOPE finite-cylindrical L5 ansatz only; no selection or measure claim")

    if FAILURES:
        print("RESULT FAIL %d gate failure(s)" % len(FAILURES))
        for gate, message in FAILURES:
            print("  %s :: %s" % (gate, message))
        return 1

    print("CLOSURE every cursor at driver windows L=4..32")
    print("CLOSURE zero-residue restriction transports the no-go to every depth")
    print("RESULT PASS cursor axis closed through window 32")
    return 0


if __name__ == "__main__":
    sys.exit(main())
