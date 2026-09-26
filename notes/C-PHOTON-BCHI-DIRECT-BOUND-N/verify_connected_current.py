#!/usr/bin/env python3
"""Exact connected-current audit; NON-CANONICAL, candidate-C only.

The universal argument is in CONNECTED-CURRENT.md. No scientific execution
is permitted before the public pin described in CONNECTED-PREREG-20260924.md.
These finite checks prove no correlation decay or positive P1 gap.
"""

from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial


def shifted(x, direction, amount=1):
    y = list(x)
    y[direction] += amount
    return tuple(y)


def boundary(cell, L):
    x, axes = cell
    answer = defaultdict(int)
    for i, direction in enumerate(axes):
        other = axes[:i] + axes[i + 1:]
        sign = (-1) ** i
        upper = tuple(t % L for t in shifted(x, direction))
        lower = tuple(t % L for t in x)
        answer[(upper, other)] += sign
        answer[(lower, other)] -= sign
    return {cell: value for cell, value in answer.items() if value}


def chain_boundary(chain, L):
    answer = defaultdict(int)
    for cell, coefficient in chain.items():
        for face, incidence in boundary(cell, L).items():
            answer[face] += coefficient * incidence
    return {cell: value for cell, value in answer.items() if value}


def add_chain(target, source, multiplier=1):
    for cell, value in source.items():
        target[cell] += multiplier * value


def cup_defect(x, L):
    cubes = defaultdict(int)
    for direction in (2, 3):
        axes = (0, 1, direction)
        cubes[(tuple(t % L for t in x), axes)] -= 1
        cubes[(tuple(t % L for t in shifted(x, direction, -1)), axes)] += 1
    answer = defaultdict(int, chain_boundary(cubes, L))
    answer[(tuple(t % L for t in x), (0, 1))] -= 5
    return {cell: value for cell, value in answer.items() if value}


def verify_tube(D):
    assert D >= 3
    L = 2 * D + 4
    origin = (0, 0, 0, 0)
    other = (0, 0, 0, D)
    first = cup_defect(origin, L)
    second = cup_defect(other, L)
    assert len(first) == len(second) == 21
    assert set(first.values()) <= {-1, 1}
    assert set(second.values()) <= {-1, 1}

    tube = {((0, 0, 1, k), (0, 1, 3)): 1 for k in range(D)}
    chain = defaultdict(int)
    add_chain(chain, first)
    add_chain(chain, second, -1)
    add_chain(chain, chain_boundary(tube, L), -1)
    chain = {cell: value for cell, value in chain.items() if value}
    assert len(chain) == 4 * D + 40
    assert set(chain.values()) <= {-1, 1}

    expected_current = defaultdict(int)
    add_chain(expected_current, boundary((origin, (0, 1)), L), -1)
    add_chain(expected_current, boundary((other, (0, 1)), L))
    expected_current = {
        edge: value for edge, value in expected_current.items() if value
    }
    current_boundary = chain_boundary(chain, L)
    assert current_boundary == {
        edge: 5 * value for edge, value in expected_current.items()
    }
    assert len(expected_current) == 8

    incidences = defaultdict(list)
    for face in chain:
        for edge, sign in boundary(face, L).items():
            incidences[edge].append((face, sign))
    degrees = defaultdict(int)
    graph = defaultdict(list)
    for edge, incident in incidences.items():
        degree = len(incident)
        degrees[degree] += 1
        assert degree in (2, 5)
        signed_sum = sum(sign * chain[face] for face, sign in incident)
        assert signed_sum == 5 * expected_current.get(edge, 0)
        first_face, first_sign = incident[0]
        for face, sign in incident[1:]:
            relation = (-1 if degree == 2 else 1) * first_sign * sign
            graph[first_face].append((face, relation))
            graph[face].append((first_face, relation))
    assert degrees == {2: 8 * D + 60, 5: 8}

    # An admissible orientation solves pairwise +/- relations. One
    # connected consistent graph gives exactly two signings, irrespective
    # of the number of faces. This does not enumerate 2^|supp(n)| states.
    anchor = next(iter(chain))
    relative_sign = {anchor: 1}
    queue = deque([anchor])
    while queue:
        face = queue.popleft()
        for adjacent, relation in graph[face]:
            value = relative_sign[face] * relation
            if adjacent in relative_sign:
                assert relative_sign[adjacent] == value
            else:
                relative_sign[adjacent] = value
                queue.append(adjacent)
    assert set(relative_sign) == set(chain)
    sign = chain[anchor]
    assert all(chain[face] == sign * value
               for face, value in relative_sign.items())

    # Current support has two graph components, each of four edges.
    vertex_edges = defaultdict(set)
    for edge in expected_current:
        x, (direction,) = edge
        vertex_edges[x].add(edge)
        endpoint = tuple(t % L for t in shifted(x, direction))
        vertex_edges[endpoint].add(edge)
    unseen = set(expected_current)
    current_component_sizes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        queue = deque([seed])
        while queue:
            x, (direction,) = queue.popleft()
            endpoint = tuple(t % L for t in shifted(x, direction))
            for vertex in (x, endpoint):
                for adjacent in vertex_edges[vertex]:
                    if adjacent not in component:
                        component.add(adjacent)
                        unseen.remove(adjacent)
                        queue.append(adjacent)
        current_component_sizes.append(len(component))
    assert sorted(current_component_sizes) == [4, 4]

    e = (origin, (0,))
    f = (other, (0,))
    assert expected_current[e] == -1
    assert expected_current[f] == 1
    assert expected_current[e] * expected_current[f] == -1
    assert min(D, L - D) == D
    # The two oppositely oriented loops have identical x_1 coordinates.
    # Their complete axis current form factor vanishes identically. The
    # conditional far-edge product is NOT a lower bound on axis chi.
    axis_coefficients = defaultdict(int)
    for (x, axes), value in expected_current.items():
        if axes == (0,):
            axis_coefficients[x[1]] += value
    assert not any(axis_coefficients.values())
    return L, len(chain), degrees[2]


def audit_local_pairings():
    counts = defaultdict(int)
    for values in product((-1, 0, 1), repeat=6):
        if sum(values) % 5:
            continue
        degree = sum(v != 0 for v in values)
        counts[degree] += 1
        if degree == 5:
            assert abs(sum(values)) == 5
            continue
        assert degree in (0, 2, 4, 6) and sum(values) == 0
        plus = [i for i, v in enumerate(values) if v == 1]
        minus = [i for i, v in enumerate(values) if v == -1]
        mass = F(0)
        for negative in permutations(minus):
            matching = list(zip(plus, negative))
            mass += F(1, factorial(len(plus)))
            for switches in product((-1, 1), repeat=len(plus)):
                changed = list(values)
                for (p, q), sign in zip(matching, switches):
                    changed[p] *= sign
                    changed[q] *= sign
                assert sum(changed) == 0
                assert sum(v != 0 for v in changed) == degree
                assert all(changed[p] == -changed[q] for p, q in matching)
        assert mass == 1
    assert dict(counts) == {0: 1, 2: 30, 4: 90, 5: 12, 6: 20}
    print("Local incidence census: 153 admissible patterns, neutral=141, charged=12; pairing weights: PASS")


def all_matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for i in range(1, len(items)):
        rest = items[1:i] + items[i + 1:]
        for tail in all_matchings(rest):
            yield ((first, items[i]),) + tail


def oriented_components(faces, incidences, matching):
    graph = defaultdict(list)
    for edge, incident in incidences.items():
        signs = dict(incident)
        if len(incident) == 5:
            pairs = [(incident[0][0], face) for face, _ in incident[1:]]
            local_sign = 1
        else:
            pairs = matching[edge]
            assert sorted(p for pair in pairs for p in pair) == sorted(signs)
            local_sign = -1
        for p, q in pairs:
            relation = local_sign * signs[p] * signs[q]
            graph[p].append((q, relation))
            graph[q].append((p, relation))
    unseen = set(faces)
    components = []
    while unseen:
        first = min(unseen)
        relative = {first: 1}
        queue = deque([first])
        unseen.remove(first)
        while queue:
            p = queue.popleft()
            for q, relation in graph[p]:
                value = relative[p] * relation
                if q in relative:
                    if relative[q] != value:
                        return None
                else:
                    relative[q] = value
                    unseen.remove(q)
                    queue.append(q)
        components.append(relative)
    return components


def audit_touching_cubes():
    L = 8
    first = boundary(((0, 0, 0, 0), (0, 1, 2)), L)
    second = boundary(((0, 0, L - 1, 0), (0, 2, 3)), L)
    assert not set(first) & set(second)
    faces = sorted(set(first) | set(second))
    assert len(faces) == 12
    incidences = defaultdict(list)
    for p in faces:
        for e, sign in boundary(p, L).items():
            incidences[e].append((p, sign))
    degree_counts = defaultdict(int)
    for incident in incidences.values():
        degree_counts[len(incident)] += 1
    assert dict(degree_counts) == {2: 22, 4: 1}
    common = next(e for e, inc in incidences.items() if len(inc) == 4)
    assert common == ((0, 0, 0, 0), (0,))
    index = {p: i for i, p in enumerate(faces)}
    rows = [[(index[p], sign) for p, sign in inc]
            for inc in incidences.values()]
    orientations = [n for n in product((-1, 1), repeat=12)
                    if all(sum(sign * n[i] for i, sign in row) % 5 == 0
                           for row in rows)]
    assert len(orientations) == 4
    original_mass = F(len(orientations), 2 ** 12)
    original_cov = [[sum(F(n[i] * n[j], 2 ** 12) for n in orientations)
                     for j in range(12)] for i in range(12)]
    augmented_cov = [[F(0) for _ in faces] for _ in faces]
    base_matching = {e: ((inc[0][0], inc[1][0]),)
                     for e, inc in incidences.items() if len(inc) == 2}
    matching_masses = []
    component_counts = []
    for pairs in all_matchings(tuple(p for p, _ in incidences[common])):
        matching = dict(base_matching)
        matching[common] = pairs
        components = oriented_components(faces, incidences, matching)
        assert components is not None
        component_counts.append(len(components))
        weight = F(1, 2 ** 13)  # 2^-12 times 1/2! at the common edge
        matching_masses.append(weight * 2 ** len(components))
        for signs in product((-1, 1), repeat=len(components)):
            n = {p: sign * value for sign, part in zip(signs, components)
                 for p, value in part.items()}
            assert tuple(n[p] for p in faces) in orientations
            assert not chain_boundary(n, L)
            for i, p in enumerate(faces):
                for j, q in enumerate(faces):
                    augmented_cov[i][j] += weight * n[p] * n[q]
    assert sorted(component_counts) == [1, 1, 2]
    assert sum(matching_masses) == original_mass == F(1, 1024)
    assert sorted(m / original_mass for m in matching_masses) == [F(1, 4), F(1, 4), F(1, 2)]
    assert augmented_cov == original_cov
    print("Touching cubes: faces=12, signings=4, pairing probabilities=1/2,1/4,1/4; all face covariances: PASS")


def audit_source_constant():
    def cosh_log3(m):
        return (F(3 ** m) + F(1, 3 ** m)) / 2
    c = F(1, 3 ** 20) * cosh_log3(4) * F(5, 3) ** 20
    assert c == F(3281 * 5 ** 20, 3 ** 44)
    assert c == F(312900543212890625, 984770902183611232881)
    assert c < F(1, 3000)
    for signs in product((-1, 1), repeat=4):
        local = F(1, 3 ** 20) * cosh_log3(abs(sum(signs))) * F(5, 3) ** 20
        assert local <= c
    for k in range(1, 9):
        odds = (2 * c) ** k
        assert odds / (1 + odds) < F(1, 1 + 1500 ** k)
        if k % 2 == 0:
            signed_odds = 2 ** (k - 1) * c ** k
            assert signed_odds / (1 + signed_odds) < F(1, 1 + 2 * 1500 ** k)
    print(f"Integrated block constant c={c}<1/3000: PASS")
    print("Circulation bounds: one<1/1501, pair<1/2250001, absolute covariance<1/4500001: PASS")


def main():
    print("C-PHOTON-BCHI-DIRECT-BOUND-N connected-current audit (NON-CANONICAL)")
    audit_local_pairings()
    audit_touching_cubes()
    for D in (3, 4, 8, 16, 32):
        L, faces, neutral_edges = verify_tube(D)
        print(f"D={D} L={L}: faces={faces}, neutral_edges={neutral_edges}, "
              "charged_edges=8, pairing_components=1, signings=2, "
              "current_components=2, conditional_product=-1, axis_form_factor=0: PASS")
    audit_source_constant()
    print("RESULT PASS; no distance-decay or P1 conclusion")


if __name__ == "__main__":
    main()
