#!/usr/bin/env python3
"""Exact finite audit of the positive full-replica pair/five wiring.

PUBLIC, NON-CANONICAL. Author: A. M. Thorn. Apache-2.0.
Only the Python standard library is used. This is not a lattice simulation
or a proof of a uniform component moment, clustering, or P1.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from math import lcm

# Weight of each unordered partition of labelled tokens, indexed by
# (total number of tokens, number of five-blocks).
WEIGHT = {
    (0, 0): F(1), (2, 0): F(1), (4, 0): F(1, 2),
    (5, 1): F(1), (6, 0): F(1, 6), (7, 1): F(1, 6),
    (8, 0): F(1, 24), (9, 1): F(1, 42),
    (10, 0): F(25, 3024), (10, 2): F(1, 126),
    (11, 1): F(1, 336), (12, 0): F(5, 3696),
    (12, 2): F(1, 1386),
}
EXPECTED_PARTITIONS = (1, 0, 1, 0, 3, 1, 15, 21, 105, 378, 1071, 6930, 18711)
EXPECTED_ADMISSIBLE = (1, 0, 2, 0, 6, 2, 20, 14, 70, 72, 254, 330, 948)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def partitions_of(tokens):
    """Every unordered partition into pairs/fives exactly once."""
    if not tokens:
        return ((),)
    first, rest = tokens[0], tokens[1:]
    result = []
    for size in (2, 5):
        if size > len(tokens):
            continue
        for others in combinations(rest, size - 1):
            chosen = set(others)
            remaining = tuple(t for t in rest if t not in chosen)
            for tail in partitions_of(remaining):
                result.append(((first,) + others,) + tail)
    return tuple(result)


def active_partitions(m):
    for partition in partitions_of(tuple(range(m))):
        b = sum(len(block) == 5 for block in partition)
        weight = WEIGHT.get((m, b), F(0))
        if weight:
            yield partition, weight


def denominator(m):
    return lcm(*(w.denominator for (mm, _), w in WEIGHT.items() if mm == m))


def compatible_masks(partition):
    """Generate sign masks directly from the blocks, not from a count formula."""
    masks = [0]
    for block in partition:
        if len(block) == 2:
            choices = (1 << block[0], 1 << block[1])
        else:
            choices = (0, sum(1 << t for t in block))
        masks = [mask | choice for mask in masks for choice in choices]
    return masks


def face_table():
    table = {(-2, 0): F(1, 4), (2, 0): F(1, 4),
             (-1, 1): F(1, 2), (1, 1): F(1, 2),
             (0, 0): F(1), (0, 2): F(1, 4)}
    seen = set()
    for n1, n2 in product((-1, 0, 1), repeat=2):
        s, d = n1 + n2, n1 - n2
        a = abs(d)
        weight = F(1, 2 ** (int(n1 != 0) + int(n2 != 0)))
        require(table[s, a] == weight, "face weight")
        require((s + d) // 2 == n1 and (s - d) // 2 == n2, "face inverse")
        seen.add((s, d))
    require(len(seen) == 9, "face bijection")
    print("face_table: 9 ordered pairs, exact inverse and weights PASS")


def local_projectors():
    grand_partitions = grand_admissible = grand_masks = 0
    for m in range(13):
        den = denominator(m)
        sums = [0] * (1 << m)
        count = 0
        for partition, weight in active_partitions(m):
            count += 1
            scaled = weight * den
            require(scaled.denominator == 1, "integer scaling")
            for mask in compatible_masks(partition):
                sums[mask] += scaled.numerator
        admissible = 0
        for mask, actual in enumerate(sums):
            valid = (2 * mask.bit_count() - m) % 5 == 0
            admissible += int(valid)
            require(actual == (den if valid else 0), f"projector m={m}, mask={mask}")
        require(count == EXPECTED_PARTITIONS[m], f"partition count m={m}")
        require(admissible == EXPECTED_ADMISSIBLE[m], f"admissible count m={m}")
        grand_partitions += count
        grand_admissible += admissible
        grand_masks += len(sums)
    require((grand_partitions, grand_admissible, grand_masks) == (27237, 1719, 8191),
            "projector totals")
    print("local_projectors: m=0..12; partitions=27237; sign_masks=8191; admissible=1719 PASS")
    # Independently sum the five-block weights at fixed neutral incidence signs.
    for m, expected in ((10, F(1, 126)), (12, F(2, 77))):
        mask = (1 << (m // 2)) - 1
        total = F(0)
        for partition, weight in active_partitions(m):
            if any(len(b) == 5 for b in partition) and mask in compatible_masks(partition):
                total += weight
        require(total == expected, f"neutral mixing m={m}")
    print("neutral_edge_mixtures: m10 two_fives=1/126; m12 two_fives=2/77 PASS")


def solve_graph(nfaces, constraints):
    """Return components and +/- relative signs, or None for inconsistency."""
    graph = [[] for _ in range(nfaces)]
    for u, v, relation in constraints:
        graph[u].append((v, relation))
        graph[v].append((u, relation))
    signs = [0] * nfaces
    components = []
    for root in range(nfaces):
        if signs[root]:
            continue
        signs[root] = 1
        component = []
        stack = [root]
        while stack:
            u = stack.pop()
            component.append(u)
            for v, relation in graph[u]:
                target = signs[u] * relation
                if signs[v] == 0:
                    signs[v] = target
                    stack.append(v)
                elif signs[v] != target:
                    return None
        components.append(component)
    return components, signs


def constraints_for(a, eps, partition):
    owner = tuple(p for p, amplitude in enumerate(a) for _ in range(amplitude))
    constraints = []
    for block in partition:
        p = owner[block[0]]
        for token in block[1:]:
            q = owner[token]
            multiplier = -1 if len(block) == 2 else 1
            constraints.append((p, q, multiplier * eps[p] * eps[q]))
    return constraints


def graph_fixture(a, incidences):
    """Compare direct tied-face signs with complete unsigned graph sums.

    The one/two-row incidence fixtures are algebraic tests; they are not
    claimed to be a complete periodic cubical complex.
    """
    nfaces, m = len(a), sum(a)
    choices = tuple(active_partitions(m))
    den = denominator(m) ** len(incidences)
    direct_z = 0
    direct_matrix = [[0] * nfaces for _ in a]
    for signs in product((-1, 1), repeat=nfaces):
        d = [a[p] * signs[p] for p in range(nfaces)]
        if any(sum(eps[p] * d[p] for p in range(nfaces)) % 5 for eps in incidences):
            continue
        direct_z += 1
        for p in range(nfaces):
            for q in range(nfaces):
                direct_matrix[p][q] += d[p] * d[q]
    graph_z = 0
    graph_matrix = [[0] * nfaces for _ in a]
    consistent_count = 0
    for selections in product(choices, repeat=len(incidences)):
        weight = F(1)
        constraints = []
        for eps, (partition, local_weight) in zip(incidences, selections):
            weight *= local_weight
            constraints.extend(constraints_for(a, eps, partition))
        solved = solve_graph(nfaces, constraints)
        if solved is None:
            continue
        consistent_count += 1
        components, signs = solved
        mass = weight * den * (2 ** len(components))
        require(mass.denominator == 1, "graph integer scaling")
        mass = mass.numerator
        graph_z += mass
        for component in components:
            for p in component:
                for q in component:
                    graph_matrix[p][q] += mass * a[p] * signs[p] * a[q] * signs[q]
    require(graph_z == den * direct_z, f"graph partition a={a}")
    for p in range(nfaces):
        for q in range(nfaces):
            require(graph_matrix[p][q] == den * direct_matrix[p][q],
                    f"graph covariance a={a}, pair={p,q}")
    return direct_z, consistent_count


def graph_tests():
    fixtures = ((1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1),
                (2, 1, 1, 1, 1, 1), (2, 2, 1, 1, 1, 1),
                (2, 2, 2, 1, 1, 1), (2, 2, 2, 2, 2),
                (2, 2, 2, 2, 1, 1), (2, 2, 2, 2, 2, 1),
                (2, 2, 2, 2, 2, 2))
    for a in fixtures:
        eps = tuple(1 if p % 2 == 0 else -1 for p in range(len(a)))
        z, consistent = graph_fixture(a, (eps,))
        if a == (2, 2, 2, 2, 2):
            require((z, consistent) == (2, 126), "double-current fixture")
        if a == (2, 2, 2, 2, 2, 2):
            require(z == 20, "six doubled faces")
    graph_fixture((1,) * 6, ((1,) * 6, (1, 1, -1, -1, -1, -1)))
    print("tied_face_graphs: 9 one-edge fixtures and 1 two-edge fixture; all covariance entries PASS")
    print("double_current_fixture: 5 doubled faces; signs=2; consistent wirings=126 PASS")


def add(chain, cell, value):
    chain[cell] = chain.get(cell, 0) + value
    if not chain[cell]:
        del chain[cell]


def boundary(chain):
    result = {}
    for (x, axes), value in chain.items():
        for i, axis in enumerate(axes):
            lower_axes = axes[:i] + axes[i + 1:]
            upper = list(x)
            upper[axis] += 1
            sign = (-1) ** i
            add(result, (tuple(upper), lower_axes), sign * value)
            add(result, (x, lower_axes), -sign * value)
    return result


def four_cup():
    origin = (0, 0, 0, 0)
    central = (origin, (0, 1))
    generators = [{central: -1}]
    for axes, x, sign in (((0, 1, 2), origin, -1),
                          ((0, 1, 2), (0, 0, -1, 0), 1),
                          ((0, 1, 3), origin, -1),
                          ((0, 1, 3), (0, 0, 0, -1), 1)):
        wall = boundary({(x, axes): sign})
        require(wall[central] == 1, "cup central coefficient")
        add(wall, central, -1)
        generators.append(wall)
    faces = tuple(sorted(set().union(*(set(g) for g in generators))))
    require(len(faces) == 21 and sum(map(len, generators)) == 21, "disjoint cup generators")
    loop = boundary({central: -1})
    require(all(boundary(g) == loop for g in generators), "common cup boundary")
    edge_incidence = {}
    for index, face in enumerate(faces):
        for edge, sign in boundary({face: 1}).items():
            edge_incidence.setdefault(edge, []).append((index, sign))
    require(sorted(len(v) for v in edge_incidence.values()) == [2] * 32 + [5] * 4,
            "cup incidence census")
    neutral_constraints = []
    for entries in edge_incidence.values():
        if len(entries) == 2:
            (p, ep), (q, eq) = entries
            neutral_constraints.append((p, q, -ep * eq))
    neutral_solution = solve_graph(21, neutral_constraints)
    require(neutral_solution is not None, "cup neutral consistency")
    require(sorted(map(len, neutral_solution[0])) == [1, 5, 5, 5, 5],
            "complete cup generator classification")
    states = []
    for coefficients in product((-1, 0, 1), repeat=5):
        if sum(coefficients) % 5:
            continue
        n = {}
        for c, generator in zip(coefficients, generators):
            for p, value in generator.items():
                add(n, p, c * value)
        require(all(abs(v) == 1 for v in n.values()), "ternary cup")
        bd = boundary(n)
        require(all(v % 5 == 0 for v in bd.values()), "cup modulo closure")
        require(boundary(bd) == {}, "boundary squared")
        vector = tuple(n.get(p, 0) for p in faces)
        states.append((vector, 2 ** (21 - len(n))))
    require(len(states) == 53, "full cup state count")
    z = sum(w for _, w in states)
    first = [sum(w * v[p] for v, w in states) for p in range(21)]
    require(not any(first), "cup reversal")
    moment = [[sum(w * v[p] * v[q] for v, w in states)
               for q in range(21)] for p in range(21)]
    replica = [[0] * 21 for _ in range(21)]
    pairs = 0
    for (v, w), (u, w2) in product(states, repeat=2):
        d = tuple(v[p] - u[p] for p in range(21))
        s = tuple(v[p] + u[p] for p in range(21))
        require(all((s[p] + d[p]) // 2 == v[p] and
                    (s[p] - d[p]) // 2 == u[p] for p in range(21)), "cup replica inverse")
        bd_d = boundary({faces[p]: d[p] for p in range(21) if d[p]})
        require(all(vv % 5 == 0 for vv in bd_d.values()), "replica closure")
        for p in range(21):
            for q in range(21):
                replica[p][q] += w * w2 * d[p] * d[q]
        pairs += 1
    for p in range(21):
        for q in range(21):
            require(replica[p][q] == 2 * z * moment[p][q], "replica factor one-half")
    require(pairs == 2809, "replica count")
    print("four_cup: 21 faces; 53 standalone states; 2809 replica pairs; 441 covariance entries PASS")


def main():
    face_table()
    local_projectors()
    graph_tests()
    four_cup()
    print("RESULT PASS (finite exact audit only; uniform moments and P1 not tested)")


if __name__ == "__main__":
    main()
