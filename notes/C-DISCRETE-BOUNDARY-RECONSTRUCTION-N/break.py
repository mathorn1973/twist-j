#!/usr/bin/env python3
"""Independent exact audit of the frozen boundary-reconstruction preregistration.

NON-CANONICAL, L1. The only scientific specification used to author this file
was PREREG.md at e092feb641e859d7d959e72f3ab39ec88d4fc53c. No existing scientific
implementation, primary verifier, proof or result was consulted.

Ranks use sparse elimination over F5. Cube extensions are constructed by a
unit-cube recurrence and compared with the proposed face formula on every
face unit vector. Graph kernels use fundamental cycles of a spanning forest;
their independence, full divergence, support and rank-nullity completeness
are checked separately. Nothing is sampled. The program reads no data files.

AUDIT PASS concerns only the specified finite audits. Universal quantifiers
and the general inverse criterion remain written-proof obligations. The
comparison updates imply no physical or native-U identification.

Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
"""

from collections import deque
from itertools import product
from typing import NamedTuple


P = 5


def require(condition, message):
    """Keep scientific checks active even if Python optimization is enabled."""
    if not condition:
        raise AssertionError(message)


def row_rank(rows):
    """Exact sparse row elimination; columns are integer coordinate labels."""
    pivots = {}
    for source in rows:
        row = {column: value % P for column, value in source.items() if value % P}
        while row:
            column = min(row)
            if column not in pivots:
                inverse = pow(row[column], -1, P)
                pivots[column] = {
                    j: value * inverse % P for j, value in row.items()
                }
                break
            factor = row[column]
            for j, value in pivots[column].items():
                residue = (row.get(j, 0) - factor * value) % P
                if residue:
                    row[j] = residue
                else:
                    row.pop(j, None)
    return len(pivots)


def sparse(vector):
    return {i: value for i, value in enumerate(vector) if value}


def scaled(vector, multiplier):
    return tuple(multiplier * value % P for value in vector)


def read(vector, coordinates):
    return tuple(vector[i] for i in coordinates)


def annihilates(rows, vector):
    return all(
        sum(value * vector[i] for i, value in row.items()) % P == 0
        for row in rows
    )


def cube_constraints(n, index):
    rows = []
    for lower in product(range(n - 1), repeat=3):
        row = {}
        for offset in product(range(2), repeat=3):
            vertex = tuple(lower[a] + offset[a] for a in range(3))
            row[index[vertex]] = 1 if sum(offset) % 2 else P - 1
        rows.append(row)
    return rows


def sweep_extension(n, vertices, face_values):
    """Solve each unit cube for its upper vertex in lexicographic order."""
    values = dict(face_values)
    for i, j, k in product(range(1, n), repeat=3):
        values[i, j, k] = (
            values[i, j, k - 1]
            + values[i, j - 1, k]
            + values[i - 1, j, k]
            - values[i, j - 1, k - 1]
            - values[i - 1, j, k - 1]
            - values[i - 1, j - 1, k]
            + values[i - 1, j - 1, k - 1]
        ) % P
    return tuple(values[v] for v in vertices)


def face_formula(vertices, face_values):
    return tuple(
        (
            face_values[i, j, 0]
            + face_values[i, 0, k]
            + face_values[0, j, k]
            - face_values[i, 0, 0]
            - face_values[0, j, 0]
            - face_values[0, 0, k]
            + face_values[0, 0, 0]
        ) % P
        for i, j, k in vertices
    )


def audit_cube(n):
    vertices = tuple(product(range(n), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    face = tuple(vertex for vertex in vertices if 0 in vertex)
    face_indices = tuple(index[vertex] for vertex in face)
    constraints = cube_constraints(n, index)
    rank = row_rank(constraints)
    stacked_rank = row_rank(constraints + [{i: 1} for i in face_indices])
    hidden = len(vertices) - stacked_rank
    require(len(face) == 3 * n * n - 3 * n + 1, "cube face union count")
    require(rank == (n - 1) ** 3, "cube constraint rank")
    require(hidden == 0, "cube common kernel is nonzero")
    require(len(vertices) - rank == len(face), "cube dimension")

    extensions = []
    for marked in face:
        face_values = {vertex: int(vertex == marked) for vertex in face}
        unit = tuple(face_values[vertex] for vertex in face)
        field = sweep_extension(n, vertices, face_values)
        require(field == face_formula(vertices, face_values), "cube formula")
        require(annihilates(constraints, field), "cube unit constraints")
        require(read(field, face_indices) == unit, "cube unit readback")
        extensions.append(field)

        for multiplier in (2, 3):
            changed = scaled(field, multiplier)
            changed_face = {
                vertex: multiplier * face_values[vertex] % P for vertex in face
            }
            require(annihilates(constraints, changed), "cube update preservation")
            require(
                read(changed, face_indices) == scaled(unit, multiplier),
                "cube boundary intertwining",
            )
            require(
                sweep_extension(n, vertices, changed_face) == changed,
                "cube updated sweep reconstruction",
            )
            require(
                face_formula(vertices, changed_face) == changed,
                "cube updated formula reconstruction",
            )
        require(scaled(scaled(field, 2), 3) == field, "cube U3 U2 inverse")
        require(scaled(scaled(field, 3), 2) == field, "cube U2 U3 inverse")

    # Every operation above is linear. Unit vectors therefore audit the entire
    # face-to-field maps; stacked full rank proves uniqueness for their images.
    require(len(extensions) == len(face), "cube complete face basis")
    require(row_rank(map(sparse, extensions)) == len(face), "cube basis rank")
    return (
        f"CUBE N={n} vertices={len(vertices)} face={len(face)} rank={rank} "
        f"hidden={hidden} basis={len(extensions)} update=PASS"
    )


class Graph(NamedTuple):
    vertices: tuple
    labels: tuple
    edges: tuple


class CycleSpace(NamedTuple):
    rank: int
    basis: tuple
    tree: tuple
    chords: tuple
    components: int


def grid_graph(n, periodic=False):
    vertices = tuple(product(range(n), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    labels = []
    edges = []
    for vertex in vertices:
        for axis in range(3):
            if not periodic and vertex[axis] == n - 1:
                continue
            head = list(vertex)
            head[axis] = (head[axis] + 1) % n if periodic else head[axis] + 1
            labels.append((vertex, axis))
            edges.append((index[vertex], index[tuple(head)]))
    require(len(set(labels)) == len(labels), "distinct directed edge labels")
    return Graph(vertices, tuple(labels), tuple(edges))


def incidence_rows(graph, vertex_ids, edge_ids):
    rows = {vertex: {} for vertex in vertex_ids}
    for edge in edge_ids:
        tail, head = graph.edges[edge]
        require(tail in rows and head in rows, "incidence vertex carrier")
        rows[tail][edge] = (rows[tail].get(edge, 0) - 1) % P
        rows[head][edge] = (rows[head].get(edge, 0) + 1) % P
    return tuple(rows.values())


def divergence(graph, vector):
    require(len(vector) == len(graph.edges), "complete edge field length")
    values = [0] * len(graph.vertices)
    for value, (tail, head) in zip(vector, graph.edges):
        values[tail] -= value
        values[head] += value
    return tuple(value % P for value in values)


def cycle_space(graph, vertex_ids, edge_ids):
    """Construct and audit a complete kernel, embedded in all graph edges.

    Each non-tree edge closes one tree path. Its coefficient on its own
    chord is one and on every other chord is zero. These vectors are
    independent. Actual incidence rank and rank-nullity then certify that
    they span the complete kernel, including multigraph wrapping labels.
    """
    vertex_ids = tuple(vertex_ids)
    edge_ids = tuple(edge_ids)
    require(len(set(vertex_ids)) == len(vertex_ids), "unique subgraph vertices")
    require(len(set(edge_ids)) == len(edge_ids), "unique subgraph edges")
    roots = {vertex: vertex for vertex in vertex_ids}
    adjacency = {vertex: [] for vertex in vertex_ids}

    def root(vertex):
        while roots[vertex] != vertex:
            roots[vertex] = roots[roots[vertex]]
            vertex = roots[vertex]
        return vertex

    tree = []
    chords = []
    for edge in edge_ids:
        tail, head = graph.edges[edge]
        require(tail in roots and head in roots, "cycle subgraph endpoints")
        tail_root, head_root = root(tail), root(head)
        if tail_root == head_root:
            chords.append(edge)
        else:
            roots[tail_root] = head_root
            tree.append(edge)
            adjacency[tail].append((head, edge, 1))
            adjacency[head].append((tail, edge, P - 1))

    components = len({root(vertex) for vertex in vertex_ids})
    rank = row_rank(incidence_rows(graph, vertex_ids, edge_ids))
    require(rank == len(tree), "incidence rank versus forest size")
    require(len(tree) + components == len(vertex_ids), "forest components")
    require(len(tree) + len(chords) == len(edge_ids), "forest edge partition")
    outside = tuple(i for i in range(len(graph.edges)) if i not in set(edge_ids))
    zero_divergence = (0,) * len(graph.vertices)
    basis = []

    for chord in chords:
        tail, head = graph.edges[chord]
        # The chord goes tail -> head; its cancellation path goes head -> tail.
        paths = {head: None}
        queue = deque([head])
        while tail not in paths:
            require(bool(queue), "missing fundamental-cycle tree path")
            vertex = queue.popleft()
            for neighbor, edge, sign in adjacency[vertex]:
                if neighbor not in paths:
                    paths[neighbor] = (vertex, edge, sign)
                    queue.append(neighbor)
        values = [0] * len(graph.edges)
        values[chord] = 1
        vertex = tail
        while vertex != head:
            previous, edge, sign = paths[vertex]
            values[edge] = (values[edge] + sign) % P
            vertex = previous
        vector = tuple(values)
        require(divergence(graph, vector) == zero_divergence, "cycle divergence")
        require(read(vector, outside) == (0,) * len(outside), "cycle support")
        require(
            read(vector, chords) == tuple(int(edge == chord) for edge in chords),
            "fundamental-cycle chord identity",
        )
        basis.append(vector)

    require(len(basis) == len(edge_ids) - rank, "complete graph kernel size")
    require(row_rank(map(sparse, basis)) == len(basis), "graph basis independence")
    return CycleSpace(rank, tuple(basis), tuple(tree), tuple(chords), components)


def box_partition(graph, n):
    outer = {
        i for i, vertex in enumerate(graph.vertices)
        if any(coordinate in (0, n - 1) for coordinate in vertex)
    }
    interior = tuple(i for i in range(len(graph.vertices)) if i not in outer)
    interior_set = set(interior)
    require(
        interior_set == {
            i for i, vertex in enumerate(graph.vertices)
            if all(1 <= coordinate <= n - 2 for coordinate in vertex)
        },
        "literal interior vertex partition",
    )
    observed = tuple(
        i for i, (tail, head) in enumerate(graph.edges)
        if tail in outer or head in outer
    )
    unobserved = tuple(
        i for i, (tail, head) in enumerate(graph.edges)
        if tail in interior_set and head in interior_set
    )
    require(set(observed).isdisjoint(unobserved), "disjoint box reader partition")
    require(
        set(observed) | set(unobserved) == set(range(len(graph.edges))),
        "complete box reader partition",
    )
    return interior, observed, unobserved


def audit_gauss(n):
    graph = grid_graph(n)
    interior, observed, unobserved = box_partition(graph, n)
    kernel = cycle_space(graph, interior, unobserved)
    for vector in kernel.basis:
        require(
            read(vector, observed) == (0,) * len(observed),
            "Gauss complete observed edge data",
        )
    m = n - 2
    anticipated = 0 if n == 2 else 2 * m ** 3 - 3 * m * m + 1
    require(len(graph.vertices) == n ** 3, "Gauss explicit vertex count")
    require(len(graph.edges) == 3 * n * n * (n - 1), "Gauss explicit edge count")
    require(len(interior) == m ** 3, "Gauss interior count")
    require(len(unobserved) == 3 * m * m * (m - 1), "Gauss interior edge count")
    require(kernel.components == int(bool(interior)), "Gauss interior connectivity")
    require(len(kernel.basis) == anticipated, "Gauss anticipated kernel dimension")
    return (
        f"GAUSS N={n} vertices={len(graph.vertices)} edges={len(graph.edges)} "
        f"observed={len(observed)} interior={len(interior)} "
        f"interior_edges={len(unobserved)} rank={kernel.rank} "
        f"hidden={len(kernel.basis)}"
    )


def walk_field(graph, walk, wrapping):
    """Translate the marked walk into the literal directed edge labels."""
    lookup = {label: i for i, label in enumerate(graph.labels)}
    vertex_index = {vertex: i for i, vertex in enumerate(graph.vertices)}
    require(walk[0] == walk[-1], "closed marked witness")
    values = [0] * len(graph.edges)
    for tail, head in zip(walk, walk[1:]):
        axes = [axis for axis in range(3) if tail[axis] != head[axis]]
        require(len(axes) == 1, "marked witness single-axis step")
        axis = axes[0]
        if wrapping or head[axis] == tail[axis] + 1:
            edge = lookup[tail, axis]
            require(
                graph.edges[edge] == (vertex_index[tail], vertex_index[head]),
                "marked forward label",
            )
            values[edge] = (values[edge] + 1) % P
        else:
            require(head[axis] == tail[axis] - 1, "marked reverse unit step")
            edge = lookup[head, axis]
            require(
                graph.edges[edge] == (vertex_index[head], vertex_index[tail]),
                "marked backward label",
            )
            values[edge] = (values[edge] - 1) % P
    return tuple(values)


def audit_history(graph, witness, observed, support_region):
    zero = (0,) * len(graph.edges)
    zero_divergence = (0,) * len(graph.vertices)
    zero_reader = (0,) * len(observed)
    support = tuple(i for i, value in enumerate(witness) if value)
    require(len(support) == 4 and witness != zero, "marked four-edge support")
    require(set(support).issubset(support_region), "marked region support")
    require(divergence(graph, zero) == zero_divergence, "zero charge reference")
    require(divergence(graph, witness) == divergence(graph, zero), "same charge")
    require(read(witness, observed) == read(zero, observed), "same complete reader")
    require(scaled(zero, 2) == zero, "zero-field update")

    history = []
    current = witness
    for phase in range(4):
        # Retain and check every edge of all four states, including all zeros.
        history.append(current)
        require(current == scaled(witness, pow(2, phase, P)), "phase evolution")
        require(divergence(graph, current) == zero_divergence, "phase divergence")
        require(read(current, observed) == zero_reader, "phase complete reader")
        require(
            tuple(i for i, value in enumerate(current) if value) == support,
            "phase complete support",
        )
        require(scaled(scaled(current, 2), 3) == current, "phase inverse update")
        current = scaled(current, 2)
    require(current == witness, "four-phase orbit closure")
    require(len(set(history)) == 4, "four distinct complete phase states")
    period = next(
        step for step in range(1, 5)
        if scaled(witness, pow(2, step, P)) == witness
    )
    require(period == 4, "marked witness least period")
    return len(support), period


def audit_torus():
    graph = grid_graph(2, periodic=True)
    all_vertices = tuple(range(len(graph.vertices)))
    all_edges = tuple(range(len(graph.edges)))
    require(len(graph.vertices) == 8 and len(graph.edges) == 24, "torus carrier")
    whole = cycle_space(graph, all_vertices, all_edges)
    require(whole.rank == 7 and len(whole.basis) == 17, "original torus dimensions")

    region = tuple(i for i, vertex in enumerate(graph.vertices) if vertex[0] == 0)
    region_set = set(region)
    internal = tuple(
        i for i, (tail, head) in enumerate(graph.edges)
        if tail in region_set and head in region_set
    )
    cut = tuple(
        i for i, (tail, head) in enumerate(graph.edges)
        if (tail in region_set) != (head in region_set)
    )
    complement_internal = tuple(
        i for i, (tail, head) in enumerate(graph.edges)
        if tail not in region_set and head not in region_set
    )
    partition = internal + cut + complement_internal
    require(len(set(partition)) == len(partition), "torus disjoint edge partition")
    require(set(partition) == set(all_edges), "torus complete edge partition")
    restricted = cycle_space(graph, region, internal)
    noncut = tuple(i for i in all_edges if i not in set(cut))
    full_cut = cycle_space(graph, all_vertices, noncut)
    full_reader_rows = incidence_rows(graph, all_vertices, all_edges) + tuple(
        {i: 1} for i in cut
    )
    full_cut_hidden = len(all_edges) - row_rank(full_reader_rows)
    require(full_cut_hidden == len(full_cut.basis), "full-cut reader nullity")
    require(full_cut.components == 2, "full-cut two graph components")
    for vector in restricted.basis + full_cut.basis:
        require(read(vector, cut) == (0,) * len(cut), "torus complete cut values")

    witness = walk_field(
        graph,
        ((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (0, 0, 0)),
        wrapping=True,
    )
    require(all(value == 1 for value in witness if value), "torus forward coefficients")
    support, period = audit_history(graph, witness, cut, set(internal))
    lines = (
        f"TORUS vertices=8 edges=24 rank={whole.rank} hidden={len(whole.basis)}",
        f"TORUS_REGION vertices={len(region)} internal_edges={len(internal)} "
        f"cut_edges={len(cut)} rank={restricted.rank} hidden={len(restricted.basis)} "
        f"full_cut_hidden={full_cut_hidden}",
    )
    return lines, (support, period)


def audit_box_witness():
    graph = grid_graph(4)
    _, observed, unobserved = box_partition(graph, 4)
    witness = walk_field(
        graph,
        ((1, 1, 1), (2, 1, 1), (2, 2, 1), (1, 2, 1), (1, 1, 1)),
        wrapping=False,
    )
    require(sorted(value for value in witness if value) == [1, 1, 4, 4], "box signs")
    return audit_history(graph, witness, observed, set(unobserved))


def main():
    print("C-DISCRETE-BOUNDARY-RECONSTRUCTION-N exact audit")
    print("STATUS NON-CANONICAL L1")
    for n in range(2, 7):
        print(audit_cube(n))
    for n in range(2, 8):
        print(audit_gauss(n))
    torus_lines, torus_witness = audit_torus()
    for line in torus_lines:
        print(line)
    support, period = audit_box_witness()
    print(f"WITNESS BOX_N4 support={support} divergence=ZERO boundary=ZERO period={period}")
    support, period = torus_witness
    print(
        f"WITNESS TORUS_REGION support={support} divergence=ZERO boundary=ZERO "
        f"period={period}"
    )
    print("NATIVE_BRIDGE NOT_PROVIDED")
    print("AUDIT PASS")


if __name__ == "__main__":
    main()
