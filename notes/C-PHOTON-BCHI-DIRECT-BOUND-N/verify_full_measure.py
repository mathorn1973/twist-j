#!/usr/bin/env python3
"""Prospective exact full-measure extension audit; NON-CANONICAL candidate-C.

The all-volume proofs are in FULL-MEASURE.md. This finite audit checks
complete specified fibers, forced current sectors and loop incidence.
Publicly pin this file, the proof, preregistration and imported helper
before the first scientific execution. No full covariance or P1 closure.
Original code: A. M. Thorn, Apache-2.0, 24 September 2026.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product

from verify_connected_current import (
    add_chain, boundary, chain_boundary, cup_defect, oriented_components,
)


def clean(chain):
    return {cell: value for cell, value in chain.items() if value}


def fibonacci(n):
    assert n >= 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def aligned_pieces(D):
    assert D >= 3
    L = 2 * D + 4
    origin, other = (0, 0, 0, 0), (0, D + 1, 0, 0)
    pieces = [cup_defect(origin, L)]
    for r in range(1, D + 1):
        pieces.append({p: -v for p, v in
                       boundary(((0, r, 0, 0), (0, 1, 2)), L).items()})
    pieces.append(cup_defect(other, L))
    caps = [((0, r, 0, 0), (0, 2)) for r in range(1, D + 2)]
    capset = set(caps)
    S = defaultdict(int)
    for piece in pieces:
        add_chain(S, piece)
    S = clean(S)
    assert len(S) == 4 * D + 40 and set(S.values()) <= {-1, 1}
    assert not set(S) & capset
    segments = [{p: v for p, v in piece.items() if p not in capset}
                for piece in pieces]
    assert [len(segment) for segment in segments] == [20] + [4] * D + [20]
    assert sum(map(len, segments)) == len(S)
    for i, cap in enumerate(caps):
        assert pieces[i][cap] == 1 and pieces[i + 1][cap] == -1
        assert all(cap not in piece for j, piece in enumerate(pieces)
                   if j not in (i, i + 1))
    J0 = {e: -v for e, v in boundary((origin, (0, 1)), L).items()}
    J1 = {e: -v for e, v in boundary((other, (0, 1)), L).items()}
    J = defaultdict(int)
    add_chain(J, J0)
    add_chain(J, J1)
    assert chain_boundary(S, L) == {e: 5 * v for e, v in J.items()}
    return L, pieces, caps, S, segments, J0, J1


def color_components(noncap, caps, L):
    cap_edges = set().union(*(set(boundary(p, L)) for p in caps))
    assert len(cap_edges) == 4 * len(caps)
    rows = defaultdict(list)
    for p, value in noncap.items():
        for e, sign in boundary(p, L).items():
            rows[e].append((p, sign * value))
    graph = defaultdict(set)
    for edge, row in rows.items():
        if edge in cap_edges:
            continue
        assert len(row) in (2, 5)
        assert (sum(v for _, v in row) == 0 if len(row) == 2
                else abs(sum(v for _, v in row)) == 5)
        first = row[0][0]
        for p, _ in row[1:]:
            graph[first].add(p)
            graph[p].add(first)
    unseen, components = set(noncap), []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        component, queue = {seed}, deque([seed])
        while queue:
            for p in graph[queue.popleft()]:
                if p not in component:
                    component.add(p)
                    unseen.remove(p)
                    queue.append(p)
        components.append(frozenset(component))
    return components


def neutral_bridge(D, L):
    cubes = defaultdict(int)
    for r in range(2, D + 1):
        for z in (0, 1):
            cubes[((0, r, 0, z), (0, 2, 3))] += (-1) ** r
    for r in range(2, D):
        cubes[((0, r, r % 2, 1), (0, 1, 3))] -= 1
    B = chain_boundary(clean(cubes), L)
    assert len(B) == 12 * D - 14 and set(B.values()) <= {-1, 1}
    assert not chain_boundary(B, L)
    rows = defaultdict(list)
    for p in B:
        for e, sign in boundary(p, L).items():
            rows[e].append((p, sign))
    assert all(len(row) == 2 for row in rows.values())
    return B, set(rows)


def unsaturated_geometry(D):
    assert D >= 5 and D % 2 == 1
    L, pieces, caps, S, segments, J0, J1 = aligned_pieces(D)
    B, B_edges = neutral_bridge(D, L)
    assert not set(B) & set(S)
    S_edges = set().union(*(set(boundary(p, L)) for p in S))
    expected_common = set().union(*(set(boundary(p, L)) for p in caps[1:-1]))
    assert S_edges & B_edges == expected_common
    assert not (set(B) & {caps[0], caps[-1]})
    for r in range(2, D + 1):
        assert B[caps[r - 1]] == -(-1) ** r
    total = dict(S)
    total.update(B)
    assert len(total) == 16 * D + 26 and set(total.values()) <= {-1, 1}
    capset = set(caps)
    B_noncap = {p: v for p, v in B.items() if p not in capset}
    assert len(B_noncap) == 11 * D - 13
    noncap = {p: v for p, v in total.items() if p not in capset}
    components = color_components(noncap, caps, L)
    expected = {frozenset(segment) for segment in segments}
    expected.add(frozenset(B_noncap))
    assert set(components) == expected and len(components) == D + 3

    segment_boundaries = [chain_boundary(segment, L) for segment in segments]
    B_boundary = chain_boundary(B_noncap, L)
    lookups = []
    for i, cap in enumerate(caps):
        cap_boundary = boundary(cap, L)
        assert all(not (set(row) & set(cap_boundary))
                   for j, row in enumerate(segment_boundaries) if j not in (i, i + 1))
        beta = B.get(cap, 0)
        if i in (0, D):
            assert beta == 0 and not (set(B_boundary) & set(cap_boundary))
        else:
            assert beta in (-1, 1)
        allowed = (-1, 0, 1) if beta == 0 else tuple(sorted((0, beta)))
        lookup = {}
        for left, right, Y in product((0, 1), repeat=3):
            candidates = []
            for z in allowed:
                if all((left * segment_boundaries[i].get(e, 0)
                        + right * segment_boundaries[i + 1].get(e, 0)
                        + Y * B_boundary.get(e, 0) + z * incidence) % 5 == 0
                       for e, incidence in cap_boundary.items()):
                    candidates.append(z)
            predicted = left - right + beta * Y
            assert candidates == ([predicted] if predicted in allowed else [])
            lookup[(left, right, Y)] = candidates[0] if candidates else None
        lookups.append(lookup)
    return L, pieces, caps, S, B, total, lookups, J0, J1


def audit_unsaturated_fiber(D):
    L, pieces, caps, S, B, total, lookups, J0, J1 = unsaturated_geometry(D)
    e, f = ((0, 0, 0, 0), (0,)), ((0, D + 1, 0, 0), (0,))
    Z = numerator = delta_mean_e = delta_mean_f = F(0)
    count, wall_histogram = 0, defaultdict(int)
    per_Y_Z, per_Y_N = [F(0), F(0)], [F(0), F(0)]
    for Y in (0, 1):
        for colors in product((0, 1), repeat=D + 2):
            cap_values = [lookups[i][(colors[i], colors[i + 1], Y)]
                          for i in range(D + 1)]
            if any(z is None for z in cap_values):
                continue
            first, second = defaultdict(int), defaultdict(int)
            for color, piece in zip(colors, pieces):
                add_chain(first if color else second, piece)
            add_chain(first, B, Y)
            add_chain(second, B, 1 - Y)
            first, second = clean(first), clean(second)
            assert set(first.values()) <= {-1, 1}
            assert set(second.values()) <= {-1, 1}
            combined = defaultdict(int)
            add_chain(combined, first)
            add_chain(combined, second)
            assert clean(combined) == total
            assert all(first.get(p, 0) == z for p, z in zip(caps, cap_values))
            assert all(second.get(p, 0) == total.get(p, 0) - z
                       for p, z in zip(caps, cap_values))
            assert all(abs(total.get(p, 0)) != 2 for p in caps)
            endpoint_walls = (cap_values[0] != 0) + (cap_values[-1] != 0)
            assert len(first) + len(second) == len(total) + 2 * endpoint_walls
            b1, b2 = chain_boundary(first, L), chain_boundary(second, L)
            expected = defaultdict(int)
            add_chain(expected, J0, 5 * colors[0])
            add_chain(expected, J1, 5 * colors[-1])
            assert b1 == clean(expected)
            expected = defaultdict(int)
            add_chain(expected, J0, 5 * (1 - colors[0]))
            add_chain(expected, J1, 5 * (1 - colors[-1]))
            assert b2 == clean(expected)
            de, df = (b1.get(e, 0) - b2.get(e, 0)) // 5, (b1.get(f, 0) - b2.get(f, 0)) // 5
            assert (de, df) == (1 - 2 * colors[0], 1 - 2 * colors[-1])
            weight = F(1, 4 ** endpoint_walls)
            Z += weight
            numerator += weight * de * df
            delta_mean_e += weight * de
            delta_mean_f += weight * df
            per_Y_Z[Y] += weight
            per_Y_N[Y] += weight * de * df
            wall_histogram[endpoint_walls] += 1
            count += 1
    Fplus, Fminus = fibonacci(D + 2), fibonacci(D - 4)
    assert count == 8 * Fplus
    assert dict(wall_histogram) == {0: 2 * Fplus, 1: 4 * Fplus, 2: 2 * Fplus}
    assert per_Y_Z == [F(25, 16) * Fplus] * 2
    assert per_Y_N == [F(9, 16) * Fminus] * 2
    assert Z == F(25, 8) * Fplus
    assert numerator == F(9, 8) * Fminus
    assert delta_mean_e == delta_mean_f == 0
    ratio = F(9, 25) * F(Fminus, Fplus)
    assert numerator / Z == ratio
    assert Z / 2 ** len(total) == F(25 * Fplus, 2 ** (len(total) + 3))
    assert numerator / 2 ** len(total) == F(9 * Fminus, 2 ** (len(total) + 3))
    return count, ratio


def audit_saturated_fiber(D):
    L, pieces, caps, S, segments, J0, J1 = aligned_pieces(D)
    first, second = defaultdict(int), defaultdict(int)
    for i, piece in enumerate(pieces):
        if i % 2:
            add_chain(second, piece, -1)
        else:
            add_chain(first, piece)
    first, second = clean(first), clean(second)
    assert set(first.values()) <= {-1, 1} and set(second.values()) <= {-1, 1}
    total, difference = defaultdict(int), defaultdict(int)
    add_chain(total, first)
    add_chain(total, second)
    add_chain(difference, first)
    add_chain(difference, second, -1)
    total = clean(total)
    assert clean(difference) == S
    assert {p for p, v in total.items() if abs(v) == 2} == set(caps)
    assert all(abs(total[p]) == 1 for p in S)
    for field in (first, second):
        assert all(v % 5 == 0 for v in chain_boundary(field, L).values())
    # At this fixed sum, d is zero on every cap and +/-1 on S. The graph
    # below proves that only the two global orientations of S survive.
    rows = defaultdict(list)
    for p in S:
        for edge, incidence in boundary(p, L).items():
            rows[edge].append((p, incidence))
    matchings = {}
    for edge, row in rows.items():
        assert len(row) in (2, 5)
        if len(row) == 2:
            matchings[edge] = ((row[0][0], row[1][0]),)
    components = oriented_components(sorted(S), rows, matchings)
    assert components is not None and len(components) == 1
    eta = components[0]
    anchor = min(eta)
    sign = S[anchor] * eta[anchor]
    assert all(S[p] == sign * eta[p] for p in S)
    e, f = ((0, 0, 0, 0), (0,)), ((0, D + 1, 0, 0), (0,))
    Z = numerator = F(0)
    images = set()
    for sigma in (-1, 1):
        n1, n2 = {}, {}
        for p in total:
            d = sigma * S.get(p, 0)
            assert (total[p] + d) % 2 == (total[p] - d) % 2 == 0
            n1[p] = (total[p] + d) // 2
            n2[p] = (total[p] - d) // 2
        n1, n2 = clean(n1), clean(n2)
        assert set(n1.values()) <= {-1, 1} and set(n2.values()) <= {-1, 1}
        b1, b2 = chain_boundary(n1, L), chain_boundary(n2, L)
        assert all(v % 5 == 0 for v in b1.values())
        assert all(v % 5 == 0 for v in b2.values())
        de, df = (b1.get(e, 0) - b2.get(e, 0)) // 5, (b1.get(f, 0) - b2.get(f, 0)) // 5
        assert de * df == 1
        assert len(n1) + len(n2) == len(S) + 2 * len(caps)
        weight = F(1, 2 ** (len(n1) + len(n2)))
        Z += weight
        numerator += weight * de * df
        images.add((tuple(sorted(n1.items())), tuple(sorted(n2.items()))))
    assert len(images) == 2
    assert Z == F(1, 2 ** (len(S) + 2 * len(caps) - 1))
    assert numerator / Z == 1
    return len(caps)



def audit_rational_bounds():
    """Check the stated exact constants without square roots or decimals."""
    b_squared = F(6**12, 11**11)
    assert 6**4 < 11**3
    assert b_squared < F(1, 121)
    r = F(12, 11)**4 / F(3, 2)
    assert r == F(13824, 14641)
    assert 0 < r < 1
    assert 1 + F(2, 11) * (F(3, 2) - 1) == F(12, 11)
    return {"b_squared": b_squared, "r": r}


def audit_local_charge_five():
    """Exhaust the six ternary incidences used in the forcing argument."""
    counts = {1: 0, -1: 0}
    for values in product((-1, 0, 1), repeat=6):
        total = sum(values)
        if total not in (-5, 5):
            continue
        sign = total // 5
        assert values.count(sign) == 5
        assert values.count(0) == 1
        assert values.count(-sign) == 0
        counts[sign] += 1
    assert counts == {1: 6, -1: 6}
    return counts


def edge_color(edge):
    x, (direction,) = edge
    return direction, sum(x[a] for a in range(4) if a != direction) % 2


def audit_frozen_sector(L):
    """Certify the complete stated sector on one even periodic L-torus.

    Exported entry point for the prospective combined audit. Intended
    frozen sizes are L=4,6,8. The calculation uses exact integers/Fraction.
    """
    assert isinstance(L, int) and L >= 4 and L % 2 == 0
    V = L**4
    points = list(product(range(L), repeat=4))
    orientations = tuple(combinations(range(4), 2))
    edges = [(x, (direction,)) for x in points for direction in range(4)]
    faces = [(x, axes) for x in points for axes in orientations]
    assert len(points) == V and len(edges) == 4 * V and len(faces) == 6 * V

    s0 = {x: (-1)**(x[1] + x[2] + x[3]) for x in points}
    s1 = {x: (-1)**(x[0] + x[2] + x[3]) for x in points}
    current = {(x, (0,)): s0[x] for x in points}
    current.update({(x, (1,)): s1[x] for x in points})
    assert len(current) == 2 * V
    assert not chain_boundary(current, L)

    incidences = defaultdict(list)
    face_boundaries = {}
    for face in faces:
        face_boundary = boundary(face, L)
        assert len(face_boundary) == 4
        assert set(face_boundary.values()) == {-1, 1}
        face_boundaries[face] = face_boundary
        for edge, incidence in face_boundary.items():
            incidences[edge].append((face, incidence))
    assert set(incidences) == set(edges)
    assert all(len(incidences[edge]) == 6 for edge in edges)

    # A nonzero face at a charged edge must satisfy incidence*n_face=j_e.
    # First derive ONLY the forced zeros from conflicting 01 demands.
    forced = {}
    forced_zero = set()
    compatible_01 = set()
    for x in points:
        face = (x, (0, 1))
        demands_by_direction = defaultdict(list)
        for edge, incidence in face_boundaries[face].items():
            assert edge in current
            direction = edge[1][0]
            demands_by_direction[direction].append(incidence * current[edge])
        assert sorted(demands_by_direction[0]) == [s0[x], s0[x]]
        assert sorted(demands_by_direction[1]) == [-s1[x], -s1[x]]
        demands = set(demands_by_direction[0] + demands_by_direction[1])
        if len(demands) == 2:
            assert demands == {-1, 1}
            assert s0[x] == s1[x]
            forced[face] = 0
            forced_zero.add(face)
        else:
            assert demands == {s0[x]}
            assert s0[x] == -s1[x]
            compatible_01.add(face)
    assert len(forced_zero) == len(compatible_01) == V // 2

    # Every charged star already contains its unique zero. Force all five
    # remaining incidences, checking agreement whenever two stars meet.
    for edge, charge in current.items():
        incident = incidences[edge]
        zero_faces = [face for face, _ in incident if face in forced_zero]
        assert len(zero_faces) == 1
        for face, incidence in incident:
            if face in forced_zero:
                continue
            value = incidence * charge
            assert value in (-1, 1)
            if face in forced:
                assert forced[face] == value
            else:
                forced[face] = value

    expected_fixed = {}
    for x in points:
        expected_fixed[(x, (0, 1))] = (s0[x] - s1[x]) // 2
        expected_fixed[(x, (0, 2))] = s0[x]
        expected_fixed[(x, (0, 3))] = s0[x]
        expected_fixed[(x, (1, 2))] = s1[x]
        expected_fixed[(x, (1, 3))] = s1[x]
    assert forced == expected_fixed
    assert len(forced) == 5 * V
    assert set(forced.values()) == {-1, 0, 1}

    for edge, charge in current.items():
        values = [incidence * forced[face]
                  for face, incidence in incidences[edge]]
        assert values.count(0) == 1
        assert values.count(charge) == 5
        assert sum(values) == 5 * charge

    fixed_nonzero = {face: value for face, value in forced.items() if value}
    assert len(fixed_nonzero) == 9 * V // 2
    expected_boundary = {edge: 5 * value for edge, value in current.items()}
    assert chain_boundary(fixed_nonzero, L) == expected_boundary

    # Derive every remaining equation. It has zero fixed contribution and
    # consists of two 23 variables with opposite coefficients: equality.
    unresolved = {(x, (2, 3)) for x in points}
    assert set(faces) - set(forced) == unresolved
    graph = {face: set() for face in unresolved}
    neutral_equations = 0
    for edge in edges:
        if edge in current:
            assert all(face not in unresolved for face, _ in incidences[edge])
            continue
        assert edge[1][0] in (2, 3)
        fixed_part = sum(incidence * forced.get(face, 0)
                         for face, incidence in incidences[edge]
                         if face not in unresolved)
        unknown_part = [(face, incidence) for face, incidence in incidences[edge]
                        if face in unresolved]
        assert fixed_part == 0 and len(unknown_part) == 2
        (left, left_sign), (right, right_sign) = unknown_part
        assert left != right and left_sign == -right_sign
        assert left[0][:2] == right[0][:2] == edge[0][:2]
        graph[left].add(right)
        graph[right].add(left)
        neutral_equations += 1
    assert neutral_equations == 2 * V
    assert all(len(neighbors) == 4 for neighbors in graph.values())

    # This graph is the exact residual constraint system, so its components
    # certify all free assignments, not merely four sample configurations.
    unseen = set(unresolved)
    planes = {}
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        component = {seed}
        queue = deque([seed])
        while queue:
            face = queue.popleft()
            for adjacent in graph[face]:
                if adjacent not in component:
                    assert adjacent in unseen
                    unseen.remove(adjacent)
                    component.add(adjacent)
                    queue.append(adjacent)
        plane_key = seed[0][:2]
        assert plane_key not in planes
        assert len(component) == L**2
        assert {face[0][:2] for face in component} == {plane_key}
        assert {face[0][2:] for face in component} == set(product(range(L), repeat=2))
        planes[plane_key] = component
    plane_keys = set(product(range(L), repeat=2))
    assert set(planes) == plane_keys and len(planes) == L**2

    assignment_cases = {
        "zero": {key: 0 for key in plane_keys},
        "plus": {key: 1 for key in plane_keys},
        "minus": {key: -1 for key in plane_keys},
        "checkerboard": {key: (-1)**sum(key) for key in plane_keys},
    }
    occupancy_by_case = {}
    for name, assignment in assignment_cases.items():
        chain = dict(fixed_nonzero)
        for key, value in assignment.items():
            assert value in (-1, 0, 1)
            if value:
                for face in planes[key]:
                    chain[face] = value
        assert set(chain.values()) <= {-1, 1}
        assert chain_boundary(chain, L) == expected_boundary
        expected_occupied = 9 * V // 2 + L**2 * sum(value != 0
                                                   for value in assignment.values())
        assert len(chain) == expected_occupied
        occupancy_by_case[name] = len(chain)
        # Vanishing every axial slice is a polynomial certificate for all
        # axis characters, not just a finite set of sampled phases.
        slice_sums = [0] * L
        for (x, axes), value in chain.items():
            if axes == (0, 2):
                slice_sums[x[1]] += value
        assert slice_sums == [0] * L

    # Every plane is an independently assignable ternary variable and costs
    # L^2 occupied faces when nonzero. Check the exact partition expression
    # and the explicit upper bound used for this particular sector.
    plane_weight_sum = 1 + 2 * F(1, 2**(L**2))
    free_factor = plane_weight_sum**(L**2)
    sector_partition = F(1, 2**(9 * V // 2)) * free_factor
    assert L**2 * F(1, 2**(L**2 - 1)) <= F(1, 2048)
    assert 1 < free_factor <= F(2048, 2047) < 2
    assert 0 < sector_partition < F(2, 2**(9 * V // 2))

    # Check the independent-color geometry and the rational Chernoff step;
    # no stochastic independence of the actual edge currents is asserted.
    colors = defaultdict(set)
    for edge in edges:
        colors[edge_color(edge)].add(edge)
    assert len(colors) == 8
    assert all(len(group) == V // 2 for group in colors.values())
    for face in faces:
        assert len({edge_color(edge) for edge in face_boundaries[face]}) == 4
    constants = audit_rational_bounds()
    M = V // 2
    assert M % 4 == 0
    assert F(12, 11)**M / F(3, 2)**(M // 4) == constants["r"]**(V // 8)

    return {
        "L": L,
        "volume": V,
        "charged_edges": len(current),
        "forced_zero_01": len(forced_zero),
        "forced_nonzero_faces": len(fixed_nonzero),
        "neutral_equality_equations": neutral_equations,
        "free_planes": len(planes),
        "faces_per_plane": L**2,
        "checked_assignments": len(assignment_cases),
        "occupancy_by_case": occupancy_by_case,
        "zero_axial_slices": L,
    }



def shifted(x, axis, amount, L):
    y = list(x)
    y[axis] = (y[axis] + amount) % L
    return tuple(y)


def edge_vertices(edge, L):
    x, axis = edge
    return frozenset((x, shifted(x, axis, 1, L)))


def face_boundary(face, L):
    """Four actual positive-edge incidences of an oriented plaquette."""
    x, mu, nu = face
    assert mu < nu
    return {
        (x, mu): 1,
        (shifted(x, mu, 1, L), nu): 1,
        (shifted(x, nu, 1, L), mu): -1,
        (x, nu): -1,
    }


def make_cycle(steps, L):
    """Build a cycle from a walk, independently of the plaquette incidence."""
    origin = (2, 2, 2, 2)
    vertices = [origin]
    gamma = {}
    for axis, sign in steps:
        assert 0 <= axis < 4 and sign in (-1, 1)
        start = vertices[-1]
        end = shifted(start, axis, sign, L)
        edge = (start if sign == 1 else end, axis)
        assert edge not in gamma, "an edge is traversed more than once"
        gamma[edge] = sign
        vertices.append(end)
    assert vertices[-1] == origin, "the walk must close on the torus"
    assert len(set(vertices[:-1])) == len(steps), "the cycle must be simple"
    # Check conservation directly from endpoints, not from face formulas.
    divergence = Counter()
    for edge, coefficient in gamma.items():
        base, axis = edge
        divergence[base] -= coefficient
        divergence[shifted(base, axis, 1, L)] += coefficient
    assert all(value == 0 for value in divergence.values())
    corners = sum(
        steps[i - 1][0] != steps[i][0] for i in range(len(steps))
    )
    return gamma, corners


def rectangle(width, height):
    return (
        [(0, 1)] * width + [(1, 1)] * height
        + [(0, -1)] * width + [(1, -1)] * height
    )


def audit_source_constants():
    # h=log(3); compute cosh(k h) from its exponential definition.
    cosh = lambda k: (F(3) ** k + F(3) ** (-k)) / 2
    a = F(3) ** (-5) * cosh(1) ** 6
    r = cosh(2) / cosh(1) ** 2
    q = a * (1 + 6 * r)
    prefactor = 2 * r * a / (1 - q)
    assert a == F(15625, 177147)
    assert r == F(41, 25)
    assert q == F(169375, 177147) < 1
    assert prefactor == F(25625, 3886)
    tau = F(73, 70)
    truncated = 1 + 12 * F(3, 70) + 66 * F(3, 70)**2 + 220 * F(3, 70)**3
    assert truncated == F(14173, 8575)
    assert tau**12 > truncated > r
    q_contact = q * tau
    contact_prefactor = 2 * r * a * tau / (1 - q_contact)
    assert q_contact == F(2472875, 2480058) < 1
    assert contact_prefactor == F(748250, 7183)
    # This finite inequality is used for m selected edges of one plaquette.
    for m in range(5):
        assert cosh(m) <= cosh(1) ** m * r ** (m * (m - 1) // 2)
    print(f"CONSTANTS a={a} r={r} q={q} prefactor={prefactor}")
    print(f"CONTACT BUDGET O<=ell/12: q={q_contact} prefactor={contact_prefactor}: PASS")
    return a, r, cosh


def audit_cycle(name, steps, L, expected_corners=None,
                expected_contacts=None, expected_histogram=None,
                require_parallel_contact=False):
    a, r = F(15625, 177147), F(41, 25)
    cosh = lambda k: (F(3) ** k + F(3) ** (-k)) / 2
    gamma, corners = make_cycle(steps, L)
    ell = len(gamma)

    # Enumerate every plaquette incident on at least one selected edge.
    # Each positive edge belongs to the two mu-nu faces in every other axis.
    faces = set()
    for x, mu in gamma:
        for nu in range(4):
            if nu == mu:
                continue
            low, high = sorted((mu, nu))
            faces.add((x, low, high))
            faces.add((shifted(x, nu, -1, L), low, high))

    histogram = Counter()
    curl_histogram = Counter()
    multiplicity_sum = 0
    pair_sum = 0
    opposite = 0
    opposite_plus = 0
    opposite_minus = 0
    direct_weight = F(3) ** (-5 * ell)
    for face in sorted(faces):
        incidence = face_boundary(face, L)
        selected = [edge for edge in incidence if edge in gamma]
        m = len(selected)
        assert 1 <= m <= 4
        curl = sum(incidence[edge] * gamma[edge] for edge in selected)
        histogram[m] += 1
        curl_histogram[curl] += 1
        multiplicity_sum += m
        pair_sum += m * (m - 1) // 2
        direct_weight *= cosh(curl)
        for first, second in combinations(selected, 2):
            # Disjoint endpoints detect opposite edges independently of
            # the turn count computed from the ordered walk.
            if edge_vertices(first, L).isdisjoint(edge_vertices(second, L)):
                opposite += 1
                first_sign = incidence[first] * gamma[first]
                second_sign = incidence[second] * gamma[second]
                if first_sign == second_sign:
                    opposite_plus += 1
                else:
                    opposite_minus += 1
                    assert m == 2 and curl == 0

    assert multiplicity_sum == 6 * ell
    assert pair_sum == corners + opposite
    assert opposite == opposite_plus + opposite_minus
    if expected_corners is not None:
        assert corners == expected_corners
    if expected_contacts is not None:
        assert opposite == expected_contacts
    if expected_histogram is not None:
        assert dict(histogram) == expected_histogram
    if require_parallel_contact:
        assert opposite_minus > 0

    bound = a ** ell * r ** (corners + opposite)
    refined = (
        a ** ell * r ** (corners + opposite_plus)
        * F(9, 25) ** opposite_minus
    )
    assert direct_weight <= refined <= bound
    print(
        f"CYCLE {name} L={L} ell={ell} c={corners} O={opposite} "
        f"Oplus={opposite_plus} Ominus={opposite_minus} "
        f"m={dict(sorted(histogram.items()))} "
        f"curl={dict(sorted(curl_histogram.items()))} "
        f"source_to_bound={direct_weight / bound} "
        f"source_to_refined={direct_weight / refined}"
    )


def audit_loop_geometry():
    audit_source_constants()
    audit_cycle("square_1x1", rectangle(1, 1), 8, 4, 2, {1: 20, 4: 1})
    audit_cycle("rectangle_2x2", rectangle(2, 2), 8, 4, 0, {1: 40, 2: 4})
    audit_cycle("rectangle_2x3", rectangle(2, 3), 8, 4, 0, {1: 52, 2: 4})
    audit_cycle("rectangle_1x3", rectangle(1, 3), 8, 4, 3, {1: 40, 2: 1, 3: 2})
    bent = [
        (0, 1), (0, 1), (1, 1), (2, 1),
        (0, -1), (0, -1), (1, -1), (2, -1),
    ]
    audit_cycle("bent_3d", bent, 8, 6, 0, {1: 36, 2: 6})
    audit_cycle("winding_L6", [(0, 1)] * 6, 6, 0, 0, {1: 36})
    # This additional simple cycle exercises the sign-sensitive bound at
    # an actual pair of nearby parallel strands, where curl cancels.
    parallel = [
        (0, 1), (0, 1), (2, 1), (0, -1), (0, -1), (1, 1),
        (2, -1), (0, 1), (0, 1), (1, 1), (2, -1), (0, -1),
        (0, -1), (1, -1), (1, -1), (2, 1),
    ]
    audit_cycle("parallel_contact_3d", parallel, 8, require_parallel_contact=True)



def main():
    print("Full-measure extension audit: NON-CANONICAL finite checks")
    for D in (5, 7, 9):
        count, ratio = audit_unsaturated_fiber(D)
        print(f"D={D}: unsaturated complete pairs={count}, moment={ratio}: PASS")
    for D in (3, 5, 9):
        interfaces = audit_saturated_fiber(D)
        print(f"D={D}: saturated caps={interfaces}, complete pairs=2, moment=1: PASS")
    assert audit_local_charge_five() == {1: 6, -1: 6}
    for L in (4, 6, 8):
        row = audit_frozen_sector(L)
        print("L={L}: forced faces={forced_nonzero_faces}, free planes={free_planes}, "
              "zero axial slices={zero_axial_slices}, current-density bound: PASS".format(**row))
    print("Current-density constant r=13824/14641 < 1: PASS")
    audit_loop_geometry()
    print("RESULT PASS; full signed covariance and positive P1 margin remain unproved")


if __name__ == "__main__":
    main()
