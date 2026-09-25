#!/usr/bin/env python3
"""Prospective exact audit of NEUTRAL-SUM.md; NON-CANONICAL.

Run only after the public pin in NEUTRAL-PREREG-20260924.md is read back.
The only imported repository helper is verify_connected_current.py.
This audits finite geometry and exact sums, not the full P1 theorem.
"""

from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import product

from verify_connected_current import add_chain, boundary, chain_boundary, cup_defect


STATES = (-1, 0, 1)
EPS, T = F(1, 2**20), F(1, 16)
E = {-1: F(39207, 2**20), 0: F(36035, 2**15), 1: F(39207, 2**20)}


def clean(chain):
    return {p: v for p, v in chain.items() if v}


def cap_weight(value):
    return F(1) if value == 0 else F(1, 2) if abs(value) == 1 else F(0)


def aligned_pieces(D):
    assert D >= 3
    L = 2 * D + 4
    origins = ((0, 0, 0, 0), (0, D + 1, 0, 0))
    pieces = [cup_defect(origins[0], L)]
    for r in range(1, D + 1):
        pieces.append({p: -v for p, v in
                       boundary(((0, r, 0, 0), (0, 1, 2)), L).items()})
    pieces.append(cup_defect(origins[1], L))
    caps = [((0, r, 0, 0), (0, 2)) for r in range(1, D + 2)]
    S = defaultdict(int)
    for piece in pieces:
        add_chain(S, piece)
    S = clean(S)
    assert len(S) == 4 * D + 40 and set(S.values()) == {-1, 1}
    assert not set(S) & set(caps)
    segments = [{p: v for p, v in piece.items() if p not in set(caps)}
                for piece in pieces]
    assert [len(c) for c in segments] == [20] + [4] * D + [20]
    for i, cap in enumerate(caps):
        assert pieces[i][cap] == 1 and pieces[i + 1][cap] == -1
    return L, origins, pieces, caps, S, segments


def neutral_bridge(D, L):
    assert D >= 5 and D % 2 == 1
    cubes = defaultdict(int)
    for r in range(2, D + 1):
        for z in (0, 1):
            cubes[((0, r, 0, z), (0, 2, 3))] += (-1)**r
    for r in range(2, D):
        cubes[((0, r, r % 2, 1), (0, 1, 3))] -= 1
    B = chain_boundary(clean(cubes), L)
    assert len(B) == 12 * D - 14 and set(B.values()) == {-1, 1}
    assert not chain_boundary(B, L)
    rows = defaultdict(list)
    for p in B:
        for edge, incidence in boundary(p, L).items():
            rows[edge].append((p, incidence * B[p]))
    assert all(len(row) == 2 and sum(v for _, v in row) == 0
               for row in rows.values())
    return B


def equality_components(noncap, caps, L):
    """Degree-two equality only; retain isolated central faces."""
    excluded = set().union(*(set(boundary(p, L)) for p in caps))
    rows = defaultdict(list)
    for p, value in noncap.items():
        for edge, incidence in boundary(p, L).items():
            rows[edge].append((p, incidence * value))
    graph = {p: set() for p in noncap}
    for edge, row in rows.items():
        if edge in excluded:
            continue
        assert len(row) in (2, 5)
        if len(row) == 2:
            assert sum(v for _, v in row) == 0
            p, q = row[0][0], row[1][0]
            graph[p].add(q)
            graph[q].add(p)
        else:
            assert abs(sum(v for _, v in row)) == 5
    unseen, result = set(noncap), []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        found, queue = {start}, deque([start])
        while queue:
            for q in graph[queue.popleft()]:
                if q not in found:
                    found.add(q)
                    unseen.remove(q)
                    queue.append(q)
        result.append(frozenset(found))
    return result


def audit_endpoint(piece, cap, origin, L):
    noncap = {p: v for p, v in piece.items() if p != cap}
    components = sorted(equality_components(noncap, [cap], L), key=lambda c: (len(c), sorted(c)))
    assert [len(c) for c in components] == [1, 4, 5, 5, 5]
    # With size sorting, the open component is index 1.
    mass, source = defaultdict(F), defaultdict(F)
    admitted, charged = 0, 0
    square_boundary = boundary((origin, (0, 1)), L)
    for coefficients in product(STATES, repeat=5):
        partial = {p: noncap[p] * a for a, comp in zip(coefficients, components)
                   for p in comp if a}
        a = coefficients[1]
        restored = dict(partial)
        if a:
            restored[cap] = piece[cap] * a
        actual_boundary = chain_boundary(restored, L)
        coefficient_sum = sum(coefficients)
        expected = {e: -coefficient_sum * sign for e, sign in square_boundary.items()
                    if coefficient_sum}
        assert actual_boundary == expected
        is_closed = all(v % 5 == 0 for v in actual_boundary.values())
        assert is_closed == (coefficient_sum % 5 == 0)
        if not is_closed:
            continue
        k = coefficient_sum // 5
        assert k in STATES
        assert (k != 0) == (len(set(coefficients)) == 1 and coefficients[0] != 0)
        weight = F(1, 2**len(partial))
        mass[a] += weight
        source[a] += k * weight
        admitted += 1
        charged += (k != 0)
    assert dict(mass) == E
    assert dict(source) == {a: EPS * a for a in STATES}
    assert charged == 2
    return components, admitted


def audit_geometry(D):
    L, origins, pieces, caps, S, segments = aligned_pieces(D)
    B = neutral_bridge(D, L)
    assert not set(B) & set(S)
    assert set(B) & set(caps) == set(caps[1:-1])
    assert all(B[caps[r - 1]] == -(-1)**r for r in range(2, D + 1))
    B_noncap = {p: v for p, v in B.items() if p not in set(caps)}
    assert len(B_noncap) == 11 * D - 13
    end0, count0 = audit_endpoint(pieces[0], caps[0], origins[0], L)
    end1, count1 = audit_endpoint(pieces[-1], caps[-1], origins[1], L)
    assert count0 == count1
    noncap = dict(S)
    noncap.update(B_noncap)
    components = equality_components(noncap, caps, L)
    expected = set(end0 + end1 + [frozenset(c) for c in segments[1:-1]]
                   + [frozenset(B_noncap)])
    assert set(components) == expected and len(components) == D + 11
    # Exhaust every ternary local cap assignment against actual mod-five edges.
    rows = [chain_boundary(c, L) for c in segments]
    brow = chain_boundary(B_noncap, L)
    lookups = []
    for i, cap in enumerate(caps):
        cap_boundary = boundary(cap, L)
        beta = B.get(cap, 0)
        lookup = {}
        for a, b, y in product(STATES, repeat=3):
            actual = [z for z in STATES if all(
                (a * rows[i].get(edge, 0) + b * rows[i + 1].get(edge, 0)
                 + y * brow.get(edge, 0) + z * incidence) % 5 == 0
                for edge, incidence in cap_boundary.items())]
            predicted = a - b + beta * y
            assert actual == ([predicted] if predicted in STATES else [])
            lookup[(a, b, y)] = actual[0] if actual else None
        lookups.append(lookup)
    R = set(S) | set(B) | set(caps)
    for origin in origins:
        chosen = (origin, (0,))
        incidences = [p for p in R if chosen in boundary(p, L)]
        assert len(incidences) >= 5
    return L, origins, pieces, caps, S, B, lookups


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def mpow(a, n):
    answer = [[F(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n % 2:
            answer = mm(answer, a)
        a = mm(a, a)
        n //= 2
    return answer


def quadratic(v, matrix):
    return sum(v[i] * matrix[i][j] * v[j] for i in range(3) for j in range(3))


def exact_transfer(D):
    assert D >= 5 and D % 2 == 1
    h, M = (D - 1) // 2, 11 * D - 13
    T0 = [[T, F(1, 8), 0], [F(1, 8), 1, F(1, 8)], [0, F(1, 8), T]]
    Kplus = [[F(1, 2), 1, F(1, 2)], [0, F(1, 2), 1], [0, 0, F(1, 2)]]
    Kminus = [list(row) for row in zip(*Kplus)]
    diagonal = (T, F(1), T)
    r = (2, 1, 2)
    for kernel in (Kplus, Kminus):
        assert all(sum(kernel[i][j] * diagonal[j] * r[j] for j in range(3))
                   <= F(5, 8) * r[i] for i in range(3))
    A = [[1, 8, 1], [0, 16, 8], [0, 0, 1]]
    G = mm([list(row) for row in zip(*A)], A)
    assert G == [[1, 8, 1], [8, 320, 136], [1, 136, 66]]
    P = [[F(x, 1024) for x in row] for row in G]
    z = ((E[1] + E[0] / 2) / 4, E[0] + E[1], (E[1] + E[0] / 2) / 4)
    v = (-EPS / 4, F(0), EPS / 4)
    av = (EPS / 4, EPS, EPS / 4)
    Tpower, Ppower = mpow(T0, D - 1), mpow(P, h)
    Z0, N0, A0 = quadratic(z, Tpower), quadratic(v, Tpower), quadratic(av, Tpower)
    Z1 = F(1, 2**M) * quadratic(z, Ppower)
    N1 = F(1, 2**M) * quadratic(v, Ppower)
    A1 = F(1, 2**M) * quadratic(av, Ppower)
    assert N0 == 2 * EPS**2 * T**D
    assert N1 >= 0
    assert N1 <= 2 * EPS**2 * T * F(1, 2**M) * F(5, 8)**(D - 1)
    assert A1 <= F(5, 4) * EPS**2 * F(1, 2**M) * F(5, 8)**(D - 1)
    assert 2 * A1 <= 2**15 * EPS**2 * F(5, 16384)**D
    assert Z0 + 2 * Z1 >= 1
    return {0: (Z0, N0, A0), -1: (Z1, N1, A1), 1: (Z1, N1, A1)}


def audit_complete_sum(D, actual_fields=True):
    """Enumerate every reduced state after exhaustive endpoint sums.

    If actual_fields=True, additionally construct EVERY current-tagged
    field and check its real lattice coefficients, boundary and weight.
    Neutral endpoint states were all constructed in audit_endpoint.
    """
    L, origins, pieces, caps, S, B, lookups = audit_geometry(D)
    M = 11 * D - 13
    totals = {y: [F(0), F(0), F(0)] for y in STATES}
    counts = {y: 0 for y in STATES}
    tested_fields = 0
    for y in STATES:
        for a in product(STATES, repeat=D + 2):
            cap_values = [lookups[i][(a[i], a[i + 1], y)] for i in range(D + 1)]
            if any(value is None for value in cap_values):
                continue
            common = T**sum(abs(x) for x in a[1:-1]) * F(1, 2**(M * abs(y)))
            for value in cap_values:
                common *= cap_weight(value)
            partition = common * E[a[0]] * E[a[-1]]
            numerator = common * EPS**2 * a[0] * a[-1]
            absolute = abs(numerator)
            totals[y][0] += partition
            totals[y][1] += numerator
            totals[y][2] += absolute
            counts[y] += 1
            if actual_fields and a[0] and a[-1]:
                field = defaultdict(int)
                for coefficient, piece in zip(a, pieces):
                    add_chain(field, piece, coefficient)
                add_chain(field, B, y)
                field = clean(field)
                assert set(field.values()) <= {-1, 1}
                assert all(field.get(p, 0) == value for p, value in zip(caps, cap_values))
                expected = defaultdict(int)
                for origin, coefficient in ((origins[0], a[0]), (origins[1], a[-1])):
                    add_chain(expected, boundary((origin, (0, 1)), L), -5 * coefficient)
                assert chain_boundary(field, L) == clean(expected)
                assert F(1, 2**len(field)) == abs(numerator)
                tested_fields += 1
    exact = exact_transfer(D)
    assert {y: tuple(values) for y, values in totals.items()} == exact
    assert counts[-1] == counts[1]
    return {"D": D, "reduced_states": counts, "actual_charged_fields": tested_fields,
            "Z": str(sum(values[0] for values in totals.values())),
            "N": str(sum(values[1] for values in totals.values()))}


def audit_onecopy():
    # Prospective plan: complete reduced enumeration and real charged-field
    # checks at D=5,7; exact geometry and transfer bounds at D=9,17,33.
    # The root author may freeze a different explicit protocol before any run.
    for D in (5, 7):
        result = audit_complete_sum(D, actual_fields=True)
        print("onecopy", D, "states", result["reduced_states"],
              "fields", result["actual_charged_fields"], "PASS")
    for D in (9, 17, 33):
        audit_geometry(D)
        exact_transfer(D)
        print("geometry-transfer", D, "PASS")
    assert 2700 * F(5, 16384) == F(3375, 4096) < 1
    print("exact-onecopy-neutral-sum PASS; no full-covariance or P1 claim")



# Conditional-variance geometry and form factors.

from collections import Counter
from fractions import Fraction as F
from itertools import product

from verify_connected_current import boundary, chain_boundary, cup_defect


def nl_rotate_chain(chain, permutation, L):
    """Push oriented cubical cells forward under an axis permutation."""
    answer = {}
    for (x, axes), coefficient in chain.items():
        y = [0] * 4
        for old_axis in range(4):
            y[permutation[old_axis]] = x[old_axis] % L
        image_axes = tuple(permutation[axis] for axis in axes)
        inversions = sum(
            image_axes[i] > image_axes[j]
            for i in range(len(image_axes))
            for j in range(i + 1, len(image_axes))
        )
        cell = (tuple(y), tuple(sorted(image_axes)))
        assert cell not in answer
        answer[cell] = coefficient * (-1) ** inversions
    return answer


def nl_cup(center, axes, L):
    if axes == (0, 1):
        return cup_defect(center, L)
    assert axes == (0, 2)
    permutation = (0, 2, 1, 3)
    # This permutation is its own inverse. Build before pushing coordinates.
    inverse_center = tuple(center[permutation[i]] for i in range(4))
    return nl_rotate_chain(cup_defect(inverse_center, L), permutation, L)


def nl_vertices(cell, L):
    base, axes = cell
    answer = set()
    for bits in product((0, 1), repeat=len(axes)):
        point = list(base)
        for axis, bit in zip(axes, bits):
            point[axis] = (point[axis] + bit) % L
        answer.add(tuple(point))
    return answer


def nl_patch_geometry(cup, center, axes, L):
    assert len(cup) == 21
    assert set(cup.values()) <= {-1, 1}
    expected_boundary = {
        edge: -5 * incidence
        for edge, incidence in boundary((center, axes), L).items()
    }
    assert chain_boundary(cup, L) == expected_boundary

    edge_degrees = Counter()
    vertices = set()
    for face in cup:
        vertices.update(nl_vertices(face, L))
        for edge in boundary(face, L):
            edge_degrees[edge] += 1
    assert Counter(edge_degrees.values()) == Counter({2: 32, 5: 4})
    assert sum(edge_degrees.values()) == 84

    # Verify the analytical rectangular vertex box from actual cell vertices.
    for point in vertices:
        for axis in range(4):
            displacement = (point[axis] - center[axis]) % L
            allowed = {0, 1} if axis in axes else {L - 1, 0, 1}
            assert displacement in allowed
    return set(cup), set(edge_degrees), vertices


def nl_packing_centers(L, axes):
    coordinates = [
        range(0, L, 2) if axis in axes
        else range(1, 3 * (L // 3), 3)
        for axis in range(4)
    ]
    return product(*coordinates)


def audit_neutral_lower_packing(L, axes):
    seen_faces = set()
    seen_edges = set()
    seen_vertices = set()
    count = 0
    for center in nl_packing_centers(L, axes):
        cup = nl_cup(center, axes, L)
        faces, edges, vertices = nl_patch_geometry(cup, center, axes, L)
        assert seen_faces.isdisjoint(faces)
        assert seen_edges.isdisjoint(edges), "conditional factors would share an edge"
        assert seen_vertices.isdisjoint(vertices)
        seen_faces.update(faces)
        seen_edges.update(edges)
        seen_vertices.update(vertices)
        count += 1

    expected_count = (L // 2) ** 2 * (L // 3) ** 2
    assert count == expected_count
    assert len(seen_faces) == 21 * count
    assert len(seen_edges) == 36 * count

    rho = F(1, 36 * 2 ** 41)
    c_L = F(count, 2 ** 41 * L ** 4)
    assert c_L == F((L // 3) ** 2, 4 * L ** 2 * 2 ** 41)
    deficit = rho - c_L
    assert deficit == F(
        (L - 3 * (L // 3)) * (L + 3 * (L // 3)),
        36 * L ** 2 * 2 ** 41,
    )
    assert 0 <= deficit <= F(1, 6 * L * 2 ** 41)
    print(
        f"NEUTRAL_LOWER_PACK L={L} axes={axes} k={count} "
        f"faces={len(seen_faces)} edges={len(seen_edges)} "
        f"vertices={len(seen_vertices)} c_L={c_L} deficit={deficit}"
    )


def nl_laurent_norm_square(coefficients):
    answer = Counter()
    for first_power, first_coefficient in coefficients.items():
        for second_power, second_coefficient in coefficients.items():
            answer[first_power - second_power] += (
                first_coefficient * second_coefficient
            )
    return {power: value for power, value in answer.items() if value}


def audit_neutral_lower_formfactors():
    L = 6
    origin = (0, 0, 0, 0)
    expected_slices = {
        (0, 1): {0: -5},
        (0, 2): {-1: -1, 0: -3, 1: -1},
    }
    expected_norms = {
        (0, 1): {0: 25},
        (0, 2): {-2: 1, -1: 6, 0: 11, 1: 6, 2: 1},
    }
    for axes in ((0, 1), (0, 2)):
        cup = nl_cup(origin, axes, L)
        nl_patch_geometry(cup, origin, axes, L)
        slices = Counter()
        for (base, orientation), coefficient in cup.items():
            if orientation != axes:
                continue
            displacement = base[1] % L
            assert displacement in (0, 1, L - 1)
            if displacement == L - 1:
                displacement = -1
            slices[displacement] += coefficient
        slices = {power: value for power, value in slices.items() if value}
        assert slices == expected_slices[axes]
        norm = nl_laurent_norm_square(slices)
        assert norm == expected_norms[axes]
        # The 01 midpoint contributes only a common exp(-it/2), which
        # cancels in the squared norm. The 02 midpoint has no axis-1 shift.
        print(
            f"NEUTRAL_LOWER_FORM axes={axes} "
            f"slices={dict(sorted(slices.items()))} "
            f"norm={dict(sorted(norm.items()))}"
        )

    # Exact insertion-weight and empty-event constants; no floats.
    filling_ratio = F(1, 2 ** 21)
    empty_probability_floor = F(1, 2 ** 21)
    assert 2 * filling_ratio * empty_probability_floor == F(1, 2 ** 41)
    assert F(1, 36) * F(1, 2 ** 41) == F(1, 36 * 2 ** 41)
    # For u=1-cos(t), (3+2cos(t))^2=25-20u+4u^2.
    # The further inequality 2u<=t^2 is analytical, not a finite audit.
    coefficients = {0: 5, 1: -2}
    squared = Counter()
    for i, x in coefficients.items():
        for j, y in coefficients.items():
            squared[i + j] += x * y
    assert dict(squared) == {0: 25, 1: -20, 2: 4}


def audit_neutral_lower():
    audit_neutral_lower_formfactors()
    for L in (4, 6, 8, 10, 12):
        for axes in ((0, 1), (0, 2)):
            audit_neutral_lower_packing(L, axes)
    print("NEUTRAL_LOWER PASS; geometry and constants only, no positive P1 gap")


def cube_cofaces(face, L):
    x, axes = face
    answer = set()
    for direction in range(4):
        if direction in axes:
            continue
        for shift in (0, -1):
            y = list(x)
            y[direction] = (y[direction] + shift) % L
            cube = (tuple(y), tuple(sorted(axes + (direction,))))
            assert face in boundary(cube, L)
            answer.add(cube)
    assert len(answer) == 4
    return answer


def audit_geometric_count():
    from itertools import combinations
    def doubled_midpoint(cell, L):
        base, axes = cell
        return tuple((2 * base[i] + (i in axes)) % (2 * L) for i in range(4))

    def doubled_distance(first, second, L):
        a, b = doubled_midpoint(first, L), doubled_midpoint(second, L)
        return sum(min(abs(x-y), 2*L-abs(x-y)) for x, y in zip(a, b))

    for L in (4, 6):
        for axes in combinations(range(4), 3):
            root = ((0, 0, 0, 0), axes)
            faces = tuple(boundary(root, L))
            assert len(faces) == 6
            neighbors = set()
            for face in faces:
                adjacent = cube_cofaces(face, L) - {root}
                assert len(adjacent) == 3
                assert neighbors.isdisjoint(adjacent)
                neighbors.update(adjacent)
            assert len(neighbors) == 18
            for first, second in combinations(faces, 2):
                assert cube_cofaces(first, L) & cube_cofaces(second, L) == {root}
                assert doubled_distance(first, second, L) <= 2
            for entry in faces:
                exits = [(face, cube) for face in faces if face != entry
                         for cube in cube_cofaces(face, L) - {root}]
                assert len(exits) == 15
                comb_pairs = [
                    (leaf_face, leaf_cube, out_face, out_cube)
                    for leaf_face, leaf_cube in exits
                    for out_face in faces if out_face not in (entry, leaf_face)
                    for out_cube in cube_cofaces(out_face, L) - {root}
                ]
                assert len(comb_pairs) == 180
                assert all(x[1] != x[3] for x in comb_pairs)
        center = ((0, 0, 0, 0), (0, 1))
        cup = cup_defect(center[0], L)
        wall_caps = set(cup) - {center}
        assert len(wall_caps) == 20
        for edge in boundary(center, L):
            assert all(doubled_distance(edge, cap, L) <= 3 for cap in wall_caps)
    assert 18 * 15 * 15 * 15 == 60750
    assert 15 * 12 * 15 == 2700
    assert 6 * 20 == 120
    assert 4 * 5 * 4 * 3 == 240
    q = F(3375, 4096)
    assert 2700 * F(5, 16384) == q < 1
    prefactor = F(120**2 * 240 * 60750, 2700**3 * 2**25)
    assert prefactor == F(1, 3 * 2**20)
    assert prefactor / (1 - q) == F(1, 553728)
    closed_comb_q = F(2700, 2**12)
    assert closed_comb_q == F(675, 1024) < 1
    assert F(60750, 2**21) / (1 - closed_comb_q) == F(30375, 357376)
    path_q = F(15, 16)
    # k=2 term: 18 rooted pairs and two signs, area10. Sum every k>=2.
    assert F(18 * 2, 2**10) / (1 - path_q) == F(9, 16)
    print("GEOMETRY_COUNTS root=18 path=15 comb=2700 endpoint=120 root-placement=240")
    print("SUMMED_COMB ratio=3375/4096 prefactor=1/553728; generated events only")


def audit_aligned_comb(D):
    L, origins, pieces, caps, S, segments = aligned_pieces(D)
    upper = [((0, r, 0, 1), (0, 2, 3)) for r in range(2, D + 1)]
    leaves = [((0, r, 0, 0), (0, 2, 3)) for r in range(2, D + 1)]
    connectors = [((0, r, r % 2, 1), (0, 1, 3)) for r in range(2, D)]
    cubes = upper + leaves + connectors
    assert len(set(cubes)) == 3 * D - 4
    face_owners = defaultdict(list)
    for cube in cubes:
        for face in boundary(cube, L):
            face_owners[face].append(cube)
    assert all(len(owners) in (1, 2) for owners in face_owners.values())
    graph = {cube: set() for cube in cubes}
    for owners in face_owners.values():
        if len(owners) == 2:
            first, second = owners
            graph[first].add(second)
            graph[second].add(first)
    assert sum(map(len, graph.values())) // 2 == len(cubes) - 1
    for i, (top, leaf) in enumerate(zip(upper, leaves)):
        assert graph[leaf] == {top}
        expected = {leaf}
        if i:
            expected.add(connectors[i - 1])
        if i < len(connectors):
            expected.add(connectors[i])
        assert graph[top] == expected
        shared = set(boundary(top, L)) & set(boundary(leaf, L))
        assert len(shared) == 1
        shared_face = next(iter(shared))
        cap = caps[i + 1]
        assert cap in boundary(leaf, L) and cap != shared_face
        assert cap[1] == shared_face[1]  # the opposite, not an arbitrary face
    for i, connector in enumerate(connectors):
        assert graph[connector] == {upper[i], upper[i + 1]}
    boundary_faces = {face for face, owners in face_owners.items() if len(owners) == 1}
    B = neutral_bridge(D, L)
    assert set(B) == boundary_faces
    assert len(B) == 4 * len(cubes) + 2 == 12 * D - 14
    assert len(set(B) - set(caps)) == 11 * D - 13
    assert set(B) & set(caps) == set(caps[1:-1])
    assert not set(B) & set(S)
    for i, piece in enumerate(pieces[1:-1]):
        common = cube_cofaces(caps[i], L) & cube_cofaces(caps[i + 1], L)
        assert len(common) == 1
        cube = next(iter(common))
        assert set(boundary(cube, L)) == set(piece)
    print(f"ALIGNED_COMB D={D} cubes={len(cubes)} boundary={len(B)} noncap={11*D-13}")


def main():
    print("Neutral sums and conditional variance; NON-CANONICAL exact finite audit")
    audit_onecopy()
    audit_geometric_count()
    for D in (5, 7, 9):
        audit_aligned_comb(D)
    audit_neutral_lower()
    print("RESULT PASS; complete P1 and Canon promotion remain unproved")


if __name__ == "__main__":
    main()
