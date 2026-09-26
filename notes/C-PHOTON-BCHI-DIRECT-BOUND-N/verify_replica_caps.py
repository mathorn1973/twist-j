#!/usr/bin/env python3
"""Exact replica-cap fiber audit; unexecuted before its public pin.

NON-CANONICAL candidate-C. This audits a specified conditional fiber of
the original product measure, not unconditional covariance decay.
"""

from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import product
from math import comb

from verify_connected_current import add_chain, boundary, chain_boundary, cup_defect


def nonzero(chain):
    return {cell: value for cell, value in chain.items() if value}


def replica_geometry(D):
    assert D >= 3
    L = 2 * D + 4
    origin, other = (0, 0, 0, 0), (0, D + 1, 0, 0)
    pieces = [cup_defect(origin, L)]
    for r in range(1, D + 1):
        pieces.append({face: -value for face, value in
                       boundary(((0, r, 0, 0), (0, 1, 2)), L).items()})
    pieces.append(cup_defect(other, L))
    caps = [((0, r, 0, 0), (0, 2)) for r in range(1, D + 2)]
    capset = set(caps)
    total = defaultdict(int)
    for piece in pieces:
        add_chain(total, piece)
    total = nonzero(total)
    assert len(total) == 4 * D + 40
    assert set(total.values()) <= {-1, 1}
    assert not (set(total) & capset)
    assert set().union(*(set(piece) for piece in pieces)) == set(total) | capset
    segments = [{face: value for face, value in piece.items() if face not in capset}
                for piece in pieces]
    assert [len(segment) for segment in segments] == [20] + [4] * D + [20]
    assert sum(len(segment) for segment in segments) == len(total)
    assert set().union(*(set(segment) for segment in segments)) == set(total)
    for r, cap in enumerate(caps):
        assert pieces[r][cap] == 1
        assert pieces[r + 1][cap] == -1
        assert all(cap not in piece for i, piece in enumerate(pieces)
                   if i not in (r, r + 1))

    cap_boundaries = [boundary(cap, L) for cap in caps]
    cap_edges = set().union(*(set(row) for row in cap_boundaries))
    assert sum(len(row) for row in cap_boundaries) == len(cap_edges)
    incidences = defaultdict(list)
    for face, value in total.items():
        for edge, incidence in boundary(face, L).items():
            incidences[edge].append((face, incidence * value))

    # These are necessary equality constraints on replica colors, not
    # guessed segment labels. They exclude every edge incident on a cap.
    graph = defaultdict(set)
    for edge, row in incidences.items():
        if edge in cap_edges:
            continue
        assert len(row) in (2, 5)
        if len(row) == 2:
            assert sum(value for _, value in row) == 0
        else:
            assert abs(sum(value for _, value in row)) == 5
        first = row[0][0]
        for face, _ in row[1:]:
            graph[first].add(face)
            graph[face].add(first)
    unseen, components = set(total), []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        component, queue = {seed}, deque([seed])
        while queue:
            for face in graph[queue.popleft()]:
                if face not in component:
                    component.add(face)
                    unseen.remove(face)
                    queue.append(face)
        components.append(frozenset(component))
    assert set(components) == {frozenset(segment) for segment in segments}
    assert len(components) == D + 2

    segment_boundaries = [chain_boundary(segment, L) for segment in segments]
    cap_lookup = []
    for r, cap_boundary in enumerate(cap_boundaries):
        assert all(not (set(row) & set(cap_boundary))
                   for i, row in enumerate(segment_boundaries)
                   if i not in (r, r + 1))
        lookup = {}
        for left, right in product((0, 1), repeat=2):
            candidates = []
            for cap_value in (-1, 0, 1):
                if all((left * segment_boundaries[r].get(edge, 0)
                        + right * segment_boundaries[r + 1].get(edge, 0)
                        + cap_value * incidence) % 5 == 0
                       for edge, incidence in cap_boundary.items()):
                    candidates.append(cap_value)
            assert candidates == [left - right]
            lookup[(left, right)] = candidates[0]
        cap_lookup.append(lookup)

    # Every untested edge has no cap and already imposes just the component
    # equality above. Each binary coloring and the unique local caps is
    # therefore a complete, not sampled, parameterization of the fiber.
    first_current = {edge: -value for edge, value in
                     boundary((origin, (0, 1)), L).items()}
    last_current = {edge: -value for edge, value in
                    boundary((other, (0, 1)), L).items()}
    total_current = defaultdict(int)
    add_chain(total_current, first_current)
    add_chain(total_current, last_current)
    assert chain_boundary(total, L) == {edge: 5 * value
                                        for edge, value in total_current.items()}
    return (L, pieces, segments, caps, total, cap_lookup,
            first_current, last_current)


def audit_replica_fiber(D):
    (L, pieces, segments, caps, total, lookup,
     first_current, last_current) = replica_geometry(D)
    e, f = ((0, 0, 0, 0), (0,)), ((0, D + 1, 0, 0), (0,))
    Z = N = first_mean = last_mean = same_replica_product = F(0)
    histogram = defaultdict(int)
    count = 0
    for colors in product((0, 1), repeat=D + 2):
        first, second = defaultdict(int), defaultdict(int)
        for color, piece in zip(colors, pieces):
            add_chain(first if color else second, piece)
        first, second = nonzero(first), nonzero(second)
        assert set(first.values()) <= {-1, 1}
        assert set(second.values()) <= {-1, 1}
        combined = defaultdict(int)
        add_chain(combined, first)
        add_chain(combined, second)
        assert nonzero(combined) == total
        walls = 0
        for r, cap in enumerate(caps):
            value = lookup[r][colors[r:r + 2]]
            assert first.get(cap, 0) == value
            assert second.get(cap, 0) == -value
            walls += value != 0
        assert len(first) + len(second) == len(total) + 2 * walls
        first_boundary = chain_boundary(first, L)
        second_boundary = chain_boundary(second, L)
        expected = defaultdict(int)
        add_chain(expected, first_current, 5 * colors[0])
        add_chain(expected, last_current, 5 * colors[-1])
        assert first_boundary == nonzero(expected)
        expected = defaultdict(int)
        add_chain(expected, first_current, 5 * (1 - colors[0]))
        add_chain(expected, last_current, 5 * (1 - colors[-1]))
        assert second_boundary == nonzero(expected)
        assert all(value % 5 == 0 for value in first_boundary.values())
        assert all(value % 5 == 0 for value in second_boundary.values())
        j1e, j1f = first_boundary.get(e, 0) // 5, first_boundary.get(f, 0) // 5
        de = (first_boundary.get(e, 0) - second_boundary.get(e, 0)) // 5
        df = (first_boundary.get(f, 0) - second_boundary.get(f, 0)) // 5
        assert (de, df) == (1 - 2 * colors[0], 1 - 2 * colors[-1])
        assert de * df == (-1) ** walls
        weight = F(1, 4 ** walls)  # common factor 2^-|S| restored below
        Z += weight
        N += weight * de * df
        first_mean += weight * j1e
        last_mean += weight * j1f
        same_replica_product += weight * j1e * j1f
        histogram[walls] += 1
        count += 1
    interfaces = D + 1
    assert count == 2 ** (D + 2)
    assert dict(histogram) == {h: 2 * comb(interfaces, h)
                              for h in range(interfaces + 1)}
    assert Z == 2 * F(5, 4) ** interfaces
    assert N == 2 * F(3, 4) ** interfaces
    ratio = F(3, 5) ** interfaces
    assert N / Z == ratio
    assert first_mean / Z == last_mean / Z == F(-1, 2)
    assert same_replica_product / Z == (1 + ratio) / 4
    assert same_replica_product / Z - F(1, 4) == ratio / 4
    actual_mass = Z / 2 ** len(total)
    actual_signed_mass = N / 2 ** len(total)
    assert actual_mass == F(1, 2 ** (len(total) - 1)) * F(5, 4) ** interfaces
    assert actual_signed_mass == F(1, 2 ** (len(total) - 1)) * F(3, 4) ** interfaces
    return count, ratio


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def audit_transfer(D):
    replica_geometry(D)
    T = [[F(1), F(1, 4)], [F(1, 4), F(1)]]
    power = [[F(1), F(0)], [F(0), F(1)]]
    for _ in range(D + 1):
        power = matmul(power, T)
    Z = sum(sum(row) for row in power)
    N = power[0][0] + power[1][1] - power[0][1] - power[1][0]
    assert Z == 2 * F(5, 4) ** (D + 1)
    assert N == 2 * F(3, 4) ** (D + 1)
    assert N / Z == F(3, 5) ** (D + 1)
    return D + 2


def cell_vertices(cell, L):
    x, axes = cell
    return {tuple((x[a] + sum(bit for axis, bit in zip(axes, bits)
                             if axis == a)) % L for a in range(4))
            for bits in product((0, 1), repeat=len(axes))}


def audit_zero_sector_packing(L):
    centers = list(product(range(1, 4 * (L // 4), 4), repeat=4))
    assert len(centers) == (L // 4) ** 4
    patches, currents, used_faces, used_vertices, used_edges = [], [], set(), set(), set()
    for center in centers:
        patch = cup_defect(center, L)
        current = {edge: -v for edge, v in boundary((center, (0, 1)), L).items()}
        vertices = set().union(*(cell_vertices(p, L) for p in patch))
        assert len(patch) == 21 and set(patch.values()) <= {-1, 1}
        assert chain_boundary(patch, L) == {e: 5 * v for e, v in current.items()}
        assert not (set(patch) & used_faces)
        assert not (vertices & used_vertices)
        assert not (set(current) & used_edges)
        assert all(abs(v[a] - center[a]) <= 1 for v in vertices for a in range(4))
        used_faces.update(patch)
        used_vertices.update(vertices)
        used_edges.update(current)
        patches.append(patch)
        currents.append(current)
    k = len(patches)
    assert len(used_faces) == 21 * k and len(used_edges) == 4 * k
    # A neutral background off every patch. These finite tests illustrate
    # the injection; its all-background proof is in REPLICA-CAPS.md.
    cube = boundary(((3, 3, 3, 3), (0, 1, 2)), L)
    assert not chain_boundary(cube, L)
    assert not (set(cube) & used_faces)
    backgrounds = [{}, cube, {p: -v for p, v in cube.items()}]
    tested = min(k, 4)
    images = set()
    for background in backgrounds:
        for signs in product((-1, 0, 1), repeat=tested):
            field = defaultdict(int, background)
            expected_current = defaultdict(int)
            for sigma, patch, current in zip(signs, patches, currents):
                add_chain(field, patch, sigma)
                add_chain(expected_current, current, sigma)
            field = nonzero(field)
            expected_current = nonzero(expected_current)
            assert set(field.values()) <= {-1, 1}
            assert chain_boundary(field, L) == {e: 5 * v for e, v in expected_current.items()}
            inserted = sum(sigma != 0 for sigma in signs)
            assert len(field) == len(background) + 21 * inserted
            restored = defaultdict(int, field)
            recovered = []
            for patch, current in zip(patches[:tested], currents[:tested]):
                edge = min(current)
                sigma = expected_current.get(edge, 0) * current[edge]
                recovered.append(sigma)
                add_chain(restored, patch, -sigma)
            assert tuple(recovered) == signs and nonzero(restored) == background
            key = tuple(sorted(field.items()))
            assert key not in images
            images.add(key)
    assert len(images) == 3 ** (tested + 1)
    epsilon = F(1, 2 ** 41)
    lower_ratio = sum(F(comb(k, m)) * epsilon ** m for m in range(k + 1))
    assert lower_ratio == (1 + epsilon) ** k > 1
    assert F(1, 2 ** 20) * F(1, 2 ** 21) == epsilon
    return k, len(images)


def main():
    print("Replica cap audit: NON-CANONICAL conditional fiber only")
    for D in (3, 4, 8):
        count, ratio = audit_replica_fiber(D)
        print(f"D={D}: complete fiber={count}, interfaces={D+1}, "
              f"difference-current correlation={ratio}: PASS")
    for D in (16, 32):
        segments = audit_transfer(D)
        print(f"D={D}: geometry={segments} segments, exact transfer: PASS")
    print("Single-replica conditional covariance is one quarter of the difference moment")
    for L in (4, 6, 8, 10, 12):
        k, images = audit_zero_sector_packing(L)
        print(f"L={L}: disjoint four-cups={k}, injective finite images={images}, "
              "2^-41 binomial factor: PASS")
    print("RESULT PASS; no full-measure distance bound or positive P1 gap")


if __name__ == "__main__":
    main()
