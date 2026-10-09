#!/usr/bin/env python3
"""Primary finite audit; NON-CANONICAL, L1, exact F5 arithmetic only."""
# SPDX-License-Identifier: Apache-2.0

from itertools import product


P = 5


def nullspace(matrix, width):
    """Dense reduced row elimination; return rank and a full free-column basis."""
    rows = [[entry % P for entry in row] for row in matrix]
    assert all(len(row) == width for row in rows)
    pivots = []
    for column in range(width):
        pivot_row = next(
            (i for i in range(len(pivots), len(rows)) if rows[i][column]), None
        )
        if pivot_row is None:
            continue
        target = len(pivots)
        rows[target], rows[pivot_row] = rows[pivot_row], rows[target]
        reciprocal = pow(rows[target][column], -1, P)
        rows[target] = [(reciprocal * entry) % P for entry in rows[target]]
        for i, row in enumerate(rows):
            if i == target or not row[column]:
                continue
            multiple = row[column]
            rows[i] = [(a - multiple * b) % P for a, b in zip(row, rows[target])]
        pivots.append(column)
        if len(pivots) == len(rows):
            break
    free_columns = [column for column in range(width) if column not in pivots]
    basis = []
    for free in free_columns:
        vector = [0] * width
        vector[free] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = (-rows[i][free]) % P
        basis.append(vector)
    return len(pivots), basis


def rank(matrix, width):
    return nullspace(matrix, width)[0]


def evaluate(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) % P for row in matrix]


def selector(width, columns):
    result = []
    for column in columns:
        row = [0] * width
        row[column] = 1
        result.append(row)
    return result


def extension(vertex, boundary):
    i, j, k = vertex
    return (
        boundary[(i, j, 0)] + boundary[(i, 0, k)] + boundary[(0, j, k)]
        - boundary[(i, 0, 0)] - boundary[(0, j, 0)] - boundary[(0, 0, k)]
        + boundary[(0, 0, 0)]
    ) % P


def audit_cube(n):
    vertices = list(product(range(n), repeat=3))
    index = {vertex: i for i, vertex in enumerate(vertices)}
    boundary = [vertex for vertex in vertices if 0 in vertex]
    constraints = []
    for origin in product(range(n - 1), repeat=3):
        row = [0] * len(vertices)
        for offset in product((0, 1), repeat=3):
            vertex = tuple(a + b for a, b in zip(origin, offset))
            row[index[vertex]] = 1 if sum(offset) % 2 else 4
        constraints.append(row)
    constraint_rank = rank(constraints, len(vertices))
    combined = constraints + selector(len(vertices), [index[v] for v in boundary])
    combined_rank = rank(combined, len(vertices))
    hidden = len(vertices) - combined_rank
    assert constraint_rank == (n - 1) ** 3
    assert len(boundary) == 3 * n * n - 3 * n + 1
    assert len(vertices) - constraint_rank == len(boundary)
    assert hidden == 0
    for marked in boundary:
        data = {v: int(v == marked) for v in boundary}
        field = [extension(v, data) for v in vertices]
        assert not any(evaluate(constraints, field))
        assert [field[index[v]] for v in boundary] == [data[v] for v in boundary]
        evolved = [(2 * value) % P for value in field]
        assert not any(evaluate(constraints, evolved))
        assert [(3 * value) % P for value in evolved] == field
        evolved_data = {v: evolved[index[v]] for v in boundary}
        assert [extension(v, evolved_data) for v in vertices] == evolved
    return (
        f"CUBE N={n} vertices={len(vertices)} face={len(boundary)} "
        f"rank={constraint_rank} hidden={hidden} basis={len(boundary)} update=PASS"
    )


def grid(n, periodic=False):
    vertices = list(product(range(n), repeat=3))
    edges = []
    for tail in vertices:
        for axis in range(3):
            if not periodic and tail[axis] == n - 1:
                continue
            head = list(tail)
            head[axis] = (head[axis] + 1) % n
            edges.append((tail, tuple(head), axis))
    return vertices, edges


def incidence(vertices, edges):
    indices = {vertex: i for i, vertex in enumerate(vertices)}
    rows = [[0] * len(edges) for _ in vertices]
    for i, (tail, head, _) in enumerate(edges):
        rows[indices[tail]][i] = (rows[indices[tail]][i] - 1) % P
        rows[indices[head]][i] = (rows[indices[head]][i] + 1) % P
    return rows


def divergence(vertices, edges, flow):
    values = {vertex: 0 for vertex in vertices}
    for (tail, head, _), value in zip(edges, flow):
        values[tail] -= value
        values[head] += value
    return [values[vertex] % P for vertex in vertices]


def check_kernel(vertices, edges, basis, observed=(), allowed=None):
    assert rank(basis, len(edges)) == len(basis)
    for flow in basis:
        assert len(flow) == len(edges)
        assert not any(divergence(vertices, edges, flow))
        assert all(flow[i] == 0 for i in observed)
        if allowed is not None:
            assert all(value == 0 or i in allowed for i, value in enumerate(flow))


def embed(basis, columns, width):
    result = []
    for small in basis:
        full = [0] * width
        for column, value in zip(columns, small):
            full[column] = value
        result.append(full)
    return result


def audit_gauss(n):
    vertices, edges = grid(n)
    outer = {v for v in vertices if any(c in (0, n - 1) for c in v)}
    interior = [v for v in vertices if v not in outer]
    observed = [i for i, (u, v, _) in enumerate(edges) if u in outer or v in outer]
    unknown = [i for i, (u, v, _) in enumerate(edges) if u not in outer and v not in outer]
    assert set(observed).isdisjoint(unknown)
    assert len(observed) + len(unknown) == len(edges)
    internal_edges = [edges[i] for i in unknown]
    internal_matrix = incidence(interior, internal_edges)
    actual_rank, small_basis = nullspace(internal_matrix, len(internal_edges))
    full_basis = embed(small_basis, unknown, len(edges))
    check_kernel(vertices, edges, full_basis, observed, set(unknown))
    m = n - 2
    expected_dimension = 0 if m == 0 else 2 * m ** 3 - 3 * m * m + 1
    expected_rank = 0 if m == 0 else m ** 3 - 1
    assert len(interior) == m ** 3
    assert len(internal_edges) == 3 * m * m * (m - 1)
    assert len(edges) == 3 * n * n * (n - 1)
    assert actual_rank == expected_rank
    assert len(small_basis) == expected_dimension
    assert actual_rank + len(small_basis) == len(internal_edges)
    return (
        f"GAUSS N={n} vertices={len(vertices)} edges={len(edges)} "
        f"observed={len(observed)} interior={len(interior)} "
        f"interior_edges={len(internal_edges)} rank={actual_rank} hidden={len(small_basis)}"
    )


def cycle_flow(edges, path, periodic=False):
    edge_index = {(tail, axis): i for i, (tail, _, axis) in enumerate(edges)}
    result = [0] * len(edges)
    for tail, head in zip(path, path[1:]):
        axes = [a for a in range(3) if tail[a] != head[a]]
        assert len(axes) == 1
        axis = axes[0]
        if periodic or head[axis] == tail[axis] + 1:
            selected, coefficient = edge_index[(tail, axis)], 1
            assert edges[selected][1] == head
        else:
            assert head[axis] == tail[axis] - 1
            selected, coefficient = edge_index[(head, axis)], -1
            assert edges[selected][1] == tail
        result[selected] = (result[selected] + coefficient) % P
    return result


def witness_line(name, vertices, edges, flow, observed):
    assert any(flow)
    assert not any(divergence(vertices, edges, flow))
    assert all(flow[i] == 0 for i in observed)
    history = []
    current = flow[:]
    for _ in range(4):
        assert not any(divergence(vertices, edges, current))
        assert all(current[i] == 0 for i in observed)
        history.append(tuple(current))
        inverse = [(3 * x) % P for x in current]
        assert [(2 * x) % P for x in inverse] == current
        current = [(2 * x) % P for x in current]
    assert current == flow
    assert len(set(history)) == 4
    period = len(history)
    support = sum(value != 0 for value in flow)
    assert support == 4
    return f"WITNESS {name} support={support} divergence=ZERO boundary=ZERO period={period}"


def audit_torus():
    vertices, edges = grid(2, periodic=True)
    matrix = incidence(vertices, edges)
    full_rank, full_basis = nullspace(matrix, len(edges))
    check_kernel(vertices, edges, full_basis)
    assert full_rank == 7 and len(full_basis) == 17
    region = {v for v in vertices if v[0] == 0}
    internal = [i for i, (u, v, _) in enumerate(edges) if u in region and v in region]
    crossing = [i for i, (u, v, _) in enumerate(edges) if (u in region) != (v in region)]
    restricted_matrix = [[row[i] for i in internal] for row in matrix]
    region_rank, region_basis = nullspace(restricted_matrix, len(internal))
    check_kernel(vertices, edges, embed(region_basis, internal, len(edges)), crossing, set(internal))
    cut_matrix = matrix + selector(len(edges), crossing)
    cut_rank, cut_basis = nullspace(cut_matrix, len(edges))
    check_kernel(vertices, edges, cut_basis, crossing)
    assert region_rank + len(region_basis) == len(internal)
    assert cut_rank + len(cut_basis) == len(edges)
    assert len(region) == 4 and len(internal) == 8 and len(crossing) == 8
    assert region_rank == 3 and len(region_basis) == 5
    assert len(cut_basis) == 10
    path = [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (0, 0, 0)]
    flow = cycle_flow(edges, path, periodic=True)
    assert all(value == 0 or i in internal for i, value in enumerate(flow))
    return (
        f"TORUS vertices={len(vertices)} edges={len(edges)} rank={full_rank} hidden={len(full_basis)}",
        f"TORUS_REGION vertices={len(region)} internal_edges={len(internal)} "
        f"cut_edges={len(crossing)} rank={region_rank} hidden={len(region_basis)} "
        f"full_cut_hidden={len(cut_basis)}",
        witness_line("TORUS_REGION", vertices, edges, flow, crossing),
    )


def main():
    lines = [
        "C-DISCRETE-BOUNDARY-RECONSTRUCTION-N exact audit",
        "STATUS NON-CANONICAL L1",
    ]
    lines.extend(audit_cube(n) for n in range(2, 7))
    lines.extend(audit_gauss(n) for n in range(2, 8))
    torus_line, region_line, torus_witness = audit_torus()
    lines.extend((torus_line, region_line))
    vertices, edges = grid(4)
    outer = {v for v in vertices if any(c in (0, 3) for c in v)}
    observed = [i for i, (u, v, _) in enumerate(edges) if u in outer or v in outer]
    path = [(1, 1, 1), (2, 1, 1), (2, 2, 1), (1, 2, 1), (1, 1, 1)]
    flow = cycle_flow(edges, path)
    lines.append(witness_line("BOX_N4", vertices, edges, flow, observed))
    lines.append(torus_witness)
    lines.extend(("NATIVE_BRIDGE NOT_PROVIDED", "AUDIT PASS"))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
