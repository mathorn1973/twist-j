#!/usr/bin/env python3
"""NON-CANONICAL exact adversarial audit, independently written from PREREG.

Prior exposure: the count 13, sizes 625/1250, five-sheet incidence, and
F_5^2/sign proposal were disclosed. This is not blind discovery. This source
does not import or inspect the builder, its output, or the separate probe.
The caller must freeze this file's hash before the first execution.
"""

from collections import Counter, defaultdict, deque
from itertools import combinations, product


FIELD = range(5)


def require(condition, label, witness=None):
    if not condition:
        raise AssertionError((label, witness))


def reduce(values):
    return tuple(value % 5 for value in values)


def trace(point):
    return sum(point) % 5


def letter(point, name):
    """Literal independent coordinate implementation of the native letters."""
    p, s, P, S, q, r = point
    if name == 0:
        result = s, p, S, P, q, r
    elif name == 1:
        result = -P, -S, -p, -s, -q, -r
    elif name == 2:
        result = 2 - P, 1 + r - S, 2 - p, 1 - r - s, 1 - q, -r
    elif name == 3:
        result = 2 - p, 1 - s, 3 - P, 4 - S, 1 - q, 1 - r
    elif name == 4:
        result = 2 - p, 1 - s, 3 - P, 4 - S, 2 - q, 1 - r
    else:
        raise ValueError(name)
    return reduce(result)


def selected(point, bit):
    return letter(point, (trace(point) + 2 * bit) % 5)


def sign_class(vector):
    vector = reduce(vector)
    return min(vector, reduce(-value for value in vector))


def oriented_label(point):
    p, s, P, S, q, r = point
    total = p + s + P + S
    difference = p + s - P - S - 3
    sheet = trace(point)
    if sheet == 0:
        return reduce((total - 1, -difference - 2 * r))
    if sheet in (1, 2):
        return reduce((total, difference))
    return reduce((total, -difference))


def terminal_label(point):
    require(trace(point) in (1, 4), "terminal domain", point)
    p, s, P, S, q, r = point
    chi = 1 if trace(point) == 1 else -1
    return reduce((p + P, s + S, chi * (p - P - 2), chi * (s - S - 1)))


def components(vertices, neighbors):
    """BFS uses only actual edges, never a proposed invariant or its count."""
    unseen = set(vertices)
    result = []
    for seed in sorted(vertices):
        if seed not in unseen:
            continue
        unseen.remove(seed)
        found = {seed}
        queue = deque([seed])
        while queue:
            here = queue.popleft()
            for there in neighbors[here]:
                if there in unseen:
                    unseen.remove(there)
                    found.add(there)
                    queue.append(there)
        result.append(found)
    require(not unseen, "BFS lost vertices", sorted(unseen)[:1])
    return result


def H(vector):
    alpha, beta, gamma, delta = vector
    return reduce((beta, alpha, delta - 1, gamma + 1))


def G(vector, k):
    alpha, beta, gamma, delta = vector
    return reduce((beta + 3, alpha - 3, delta + k, gamma - k))


def determinant(matrix):
    if not matrix:
        return 1
    return sum(
        (-1) ** column * value * determinant(
            [row[:column] + row[column + 1:] for row in matrix[1:]]
        )
        for column, value in enumerate(matrix[0])
    )


def main():
    states = tuple(product(FIELD, repeat=6))
    neighbors = {point: set() for point in states}
    oriented_fibres = defaultdict(set)
    quotient_fibres = defaultdict(set)
    oriented_sheet_counts = Counter()
    quotient_sheet_counts = Counter()
    observed_tables = [[set() for _ in FIELD] for _ in (0, 1)]
    edge_checks = 0

    for point in states:
        z = trace(point)
        kappa = oriented_label(point)
        label = sign_class(kappa)
        oriented_fibres[kappa].add(point)
        quotient_fibres[label].add(point)
        oriented_sheet_counts[kappa, z] += 1
        quotient_sheet_counts[label, z] += 1
        generator_traces = (z, -z, 2 - z, 2 - z, 3 - z)
        for name in FIELD:
            transformed = letter(point, name)
            require(letter(transformed, name) == point, "letter involution", (point, name))
            require(trace(transformed) == generator_traces[name] % 5,
                    "letter trace law", (point, name, transformed))
        for bit in (0, 1):
            transformed = selected(point, bit)
            neighbors[point].add(transformed)
            neighbors[transformed].add(point)
            observed_tables[bit][z].add(trace(transformed))
            require(sign_class(oriented_label(transformed)) == label,
                    "Q not invariant", (point, bit, transformed))
            edge_checks += 1

    require(len(states) == 15625 and edge_checks == 31250, "carrier/edge coverage")
    require(set(oriented_fibres) == set(product(FIELD, repeat=2)), "oriented image")
    require(set(map(len, oriented_fibres.values())) == {625}, "oriented fibre size")
    require(len(oriented_sheet_counts) == 125 and set(oriented_sheet_counts.values()) == {125},
            "oriented sheet fibre size")
    require(len(quotient_fibres) == 13, "prior predicted Q count", len(quotient_fibres))
    for label, fibre in quotient_fibres.items():
        expected_size = 625 if label == (0, 0) else 1250
        require(len(fibre) == expected_size, "wrong Q fibre size", (label, len(fibre)))
        for z in FIELD:
            require(quotient_sheet_counts[label, z] == expected_size // 5,
                    "wrong Q sheet fibre size", (label, z, quotient_sheet_counts[label, z]))

    graph_components = components(states, neighbors)
    actual_sets = {frozenset(part) for part in graph_components}
    predicted_sets = {frozenset(part) for part in quotient_fibres.values()}
    require(actual_sets == predicted_sets, "BFS components differ from Q fibres",
            (len(actual_sets), len(predicted_sets)))
    require(len(graph_components) == 13, "prior predicted component count", len(graph_components))
    histogram = Counter(map(len, graph_components))
    require(histogram == Counter({625: 1, 1250: 12}), "prior predicted histogram", histogram)

    terminal_states = tuple(point for point in states if trace(point) in (1, 4))
    terminal_fibres = defaultdict(set)
    for point in terminal_states:
        vector = terminal_label(point)
        terminal_fibres[sign_class(vector)].add(point)
        require(oriented_label(point) == reduce((vector[0] + vector[1], vector[2] + vector[3])),
                "terminal projection disagrees with kappa", point)
        for bit in (0, 1):
            transformed = selected(point, bit)
            require(terminal_label(transformed) == reduce(-value for value in vector),
                    "registered V sign update", (point, bit))
    terminal_components = components(terminal_states, neighbors)
    require({frozenset(part) for part in terminal_components}
            == {frozenset(part) for part in terminal_fibres.values()},
            "terminal components not registered R fibres")
    require(len(terminal_components) == 313, "registered terminal count", len(terminal_components))

    def check_path(path):
        for left, right in zip(path, path[1:]):
            require(right in neighbors[left], "proposed path uses a nonedge", (left, right))

    h_available = defaultdict(set)
    g_available = defaultdict(set)
    escape_checks = 0
    for point in states:
        z = trace(point)
        if z == 3:
            left = letter(point, 3)
            swapped = letter(point, 0)
            right = letter(swapped, 3)
            check_path((left, point, swapped, right))
            vector = terminal_label(left)
            require(terminal_label(right) == H(vector), "H bridge formula", point)
            h_available[vector].add(point[5])
            escape = (point, left)
        elif z == 0:
            middle = letter(point, 2)
            left = letter(middle, 4)
            swapped = letter(point, 0)
            other_middle = letter(swapped, 2)
            right = letter(other_middle, 4)
            check_path((left, middle, point, swapped, other_middle, right))
            vector = terminal_label(left)
            k = (1 + 2 * point[5]) % 5
            require(terminal_label(right) == G(vector, k), "G bridge formula", (point, k))
            g_available[vector].add(k)
            escape = (point, middle, left)
        elif z == 2:
            escape = (point, letter(point, 4))
        else:
            continue
        check_path(escape)
        require(trace(escape[-1]) in (1, 4), "transient escape failed", escape)
        escape_checks += 1
    all_vectors = set(product(FIELD, repeat=4))
    require(set(h_available) == all_vectors and set(g_available) == all_vectors,
            "bridge missing a terminal vector")
    require(all(values == set(FIELD) for values in h_available.values()),
            "H bridge unavailable at a fibre coordinate")
    require(all(values == set(FIELD) for values in g_available.values()),
            "G bridge missing a k at fixed V")
    require(escape_checks == 9375, "transient escape coverage", escape_checks)

    translations = set()
    for vector in all_vectors:
        for k in FIELD:
            translated = G(H(vector), k)
            displacement = reduce(b - a for a, b in zip(vector, translated))
            require(displacement == reduce((3, -3, k + 1, -k - 1)),
                    "G_k H translation", (vector, k, displacement))
            translations.add(displacement)
    kernel = {vector for vector in all_vectors
              if (vector[0] + vector[1]) % 5 == 0 and (vector[2] + vector[3]) % 5 == 0}
    generated = {(0, 0, 0, 0)}
    queue = deque(generated)
    while queue:
        here = queue.popleft()
        for displacement in translations:
            there = reduce(a + b for a, b in zip(here, displacement))
            if there not in generated:
                generated.add(there)
                queue.append(there)
    require(generated == kernel, "bridge translations fail to span the kernel")

    quadratic_image = defaultdict(set)
    directions = defaultdict(set)
    for u, v in product(FIELD, repeat=2):
        quad = reduce((u * u, u * v, v * v))
        quadratic_image[quad].add((u, v))
        require((quad[0] * quad[2] - quad[1] * quad[1]) % 5 == 0,
                "quadratic rank", (u, v, quad))
        if (u, v) != (0, 0):
            pivot = u if u else v
            directions[reduce((u * pow(pivot, -1, 5), v * pow(pivot, -1, 5)))].add(quad)
    for quad, vectors in quadratic_image.items():
        representative = min(vectors)
        require(vectors == {representative, reduce(-value for value in representative)},
                "quadratic collision outside sign", (quad, vectors))
    require(len(quadratic_image) == 13, "quadratic image cardinality", len(quadratic_image))
    require(len(directions) == 6 and {len(values) for values in directions.values()} == {2},
            "quadratic projective multiplicities")

    expected_tables = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    require(observed_tables == [[{entry} for entry in row] for row in expected_tables],
            "selector trace tables", observed_tables)
    reset_traces = set()
    reset_indices = set()
    for head in states:
        point = head
        for bit in (0, 1, 1):
            point = selected(point, bit)
        reset_traces.add(trace(point))
        reset_indices.add((trace(point) + 2 * ((3).bit_count() % 2)) % 5)
    require(reset_traces == {1} and reset_indices == {1}, "three-step selector reset")
    # This four-case transition identity supports induction for every n>=3;
    # no finite-time prefix is being substituted for that induction.
    for previous_bit, current_bit in product((0, 1), repeat=2):
        z = 4 - 3 * previous_bit
        require(expected_tables[current_bit][z] == 4 - 3 * current_bit,
                "all-time trace induction step", (previous_bit, current_bit))
    require(set(quotient_sheet_counts) == set(product(quotient_fibres, FIELD)),
            "Q versus initial-trace incidence is incomplete")
    # The full trace/index history is a function of its initial trace because
    # the trace tables are closed. Every Q label occurs on every such sheet.
    same_trace_witness = None
    seed = states[0]
    for point in states:
        if trace(point) == trace(seed) and sign_class(oriented_label(point)) != sign_class(oriented_label(seed)):
            same_trace_witness = (seed, point)
            break
    require(same_trace_witness is not None, "failed to exhibit selector information loss")

    basis5 = [tuple(int(row == column) for row in FIELD) for column in FIELD]

    def shift(vector, amount):
        return tuple(vector[(row - amount) % 5] for row in FIELD)

    def j_action(vector):
        return tuple(a + b for a, b in zip(vector, shift(vector, 2)))

    for z in FIELD:
        for bit in (0, 1):
            selector = shift(basis5[z], 2 * bit)
            require(selector == basis5[(z + 2 * bit) % 5] and sum(selector) == 1,
                    "selector free-module action", (z, bit))
            superposition = j_action(basis5[z])
            require(sum(superposition) == 2 and selector != superposition,
                    "selector confused with I+C^2", (z, bit))
            require(sum(selector) % 5 != sum(superposition) % 5,
                    "augmentation distinction lost modulo five", (z, bit))
    a4_basis = [tuple(a - b for a, b in zip(basis5[column], basis5[0])) for column in range(1, 5)]
    a4_images = [j_action(vector) for vector in a4_basis]
    require(all(sum(vector) == 0 for vector in a4_images), "J leaves augmentation lattice")
    matrix = [[a4_images[column][row] for column in range(4)] for row in range(1, 5)]
    require(determinant(matrix) == 1, "A4 J invertibility", matrix)
    pairs = list(combinations(range(4), 2))
    exterior = [[matrix[i][k] * matrix[j][l] - matrix[i][l] * matrix[j][k]
                 for k, l in pairs] for i, j in pairs]
    require(determinant(exterior) == 1, "exterior-square invertibility", exterior)

    labels = sorted(quotient_fibres)
    assigned = {label: tuple(int(row == column) for row in range(6)) if column < 6 else (0,) * 6
                for column, label in enumerate(labels)}
    require(len(set(assigned.values())) == 7, "nonconstant six-spanning assignment witness")
    require({assigned[label] for label in labels[:6]}
            == {tuple(int(row == column) for row in range(6)) for column in range(6)},
            "assignment fails to contain all six coordinate vectors")
    require(all(len({assigned[sign_class(oriented_label(point))] for point in part}) == 1
                for part in graph_components), "assignment does not factor through graph")

    print("NON-CANONICAL L1 independent implementation audit")
    print("prior exposure: 13 components; sizes 625 and 12*1250; every trace sheet")
    print("states=15625 selected_edges=31250 generator_trace_checks=78125")
    print("oriented_kappa_values=25 fibre_size=625 per_sheet=125")
    print("BFS_components=13 histogram=625:1,1250:12 exact_Q_fibre_equality=PASS")
    print("terminal_BFS_components=313 exact_R_fibre_equality=PASS")
    print("H_bridges=3125 G_bridges=3125 every_V_every_k=PASS transient_escapes=9375")
    print("translation_kernel_size=25 exact_kernel_equality=PASS")
    print("quadratic_image=13 projective_directions=6 multiplicity_per_direction=2")
    print("trace_tables=(0,4,0,4,4);(2,1,1,3,1) reset_z3=1 reset_i3=1")
    print("all_n_trace_induction_cases=4 Q_initial_trace_incidence=13*5")
    print("same_trace_different_Q_witness=" + repr(same_trace_witness))
    print("selector_augmentation=1 J_sum_augmentation=2 A4_det=1 exterior_det=1")
    print("chosen_six_spanning_source_assignment=PASS image_size=7")
    print("RESULT=PASS; finite exact audit, no physical or characteristic-zero source selection")


if __name__ == "__main__":
    main()
