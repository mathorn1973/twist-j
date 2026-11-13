#!/usr/bin/env python3
"""Exact prospective audit for C-PHOTON-REPLICA-COMPLETION-BOUND-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.

The scientific scope, thresholds and interpretation are frozen in PREREG.md.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, lcm


@lru_cache(None)
def matchings(tokens: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], ...]:
    if not tokens:
        return ((),)
    if len(tokens) % 2:
        return ()
    first, rest = tokens[0], tokens[1:]
    out: list[tuple[tuple[int, int], ...]] = []
    for i, mate in enumerate(rest):
        remaining = rest[:i] + rest[i + 1 :]
        for tail in matchings(remaining):
            out.append(((first, mate),) + tail)
    return tuple(out)


def partitions(m: int):
    """All labelled pair/one-charged-block partitions for m tokens."""
    tokens = tuple(range(m))
    for h in (0, 5, 10):
        if h > m or (m - h) % 2:
            continue
        r = (m - h) // 2
        denominator = comb(r + h, h) * factorial(r)
        for charged in combinations(tokens, h):
            chosen = set(charged)
            rest = tuple(t for t in tokens if t not in chosen)
            for pairs in matchings(rest):
                blocks: tuple[tuple[int, ...], ...] = tuple(pairs)
                if h:
                    blocks = blocks + (tuple(charged),)
                yield h, denominator, blocks


def signings(blocks: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    """Compatible token sign masks for a fixed partition."""
    masks = (0,)
    for block in blocks:
        if len(block) == 2:
            alternatives = (1 << block[0], 1 << block[1])
        else:
            alternatives = (0, sum(1 << t for t in block))
        masks = tuple(mask | addition for mask in masks for addition in alternatives)
    return masks


def face_table_audit() -> None:
    expected = {
        (-2, 0): Fraction(1, 4),
        (2, 0): Fraction(1, 4),
        (-1, 1): Fraction(1, 2),
        (1, 1): Fraction(1, 2),
        (0, 0): Fraction(1),
        (0, 2): Fraction(1, 4),
    }
    seen = set()
    for u, v in product((-1, 0, 1), repeat=2):
        s, d = u + v, u - v
        weight = Fraction(1, 2 ** (int(u != 0) + int(v != 0)))
        assert expected[s, abs(d)] == weight
        assert (s + d) // 2 == u
        assert (s - d) // 2 == v
        seen.add((u, v))
    assert len(seen) == 9
    print("FACE_TABLE PASS ordered_pairs=9")


def star_audit() -> None:
    stars = [u for u in product((-1, 0, 1), repeat=6) if sum(u) % 5 == 0]
    assert len(stars) == 153
    census = Counter()
    for u in stars:
        for v in stars:
            m = sum(abs(x - y) for x, y in zip(u, v))
            delta = sum(u) - sum(v)
            assert delta % 5 == 0
            charge = abs(delta) // 5
            assert charge in (0, 1, 2)
            if charge == 0:
                assert m % 2 == 0
            elif charge == 1:
                assert m in (5, 7)
            else:
                assert m == 10
            census[m, charge] += 1
    expected_keys = {(m, 0) for m in range(0, 13, 2)} | {(5, 1), (7, 1), (10, 2)}
    assert set(census) == expected_keys
    print("ACTUAL_STARS PASS states=153 ordered_pairs=23409")
    print("STAR_CENSUS " + " ".join(f"{m}:{q}={n}" for (m, q), n in sorted(census.items())))


TABLES: dict[int, tuple[int, tuple[tuple[int, int, tuple[int, ...]], ...]]] = {}


def token_audit() -> None:
    n_partitions = 0
    n_assignments = 0
    n_admissible = 0
    for m in range(13):
        entries = list(partitions(m))
        scale = lcm(*(denominator for _, denominator, _ in entries)) if entries else 1
        counts = [0] * (1 << m)
        records = []
        for h, denominator, blocks in entries:
            coeff = scale // denominator
            masks = signings(blocks)
            assert len(set(masks)) == 1 << len(blocks)
            for mask in masks:
                total = 2 * mask.bit_count() - m
                assert total % 5 == 0
                assert abs(total) == h
                counts[mask] += coeff
            records.append((h, coeff, masks))
        for mask in range(1 << m):
            admissible = (2 * mask.bit_count() - m) % 5 == 0
            assert counts[mask] == scale * int(admissible)
            n_admissible += int(admissible)
        TABLES[m] = scale, tuple(records)
        n_partitions += len(entries)
        n_assignments += 1 << m
    assert (n_partitions, n_assignments, n_admissible) == (18862, 8191, 1719)
    print("TOKEN_PROJECTOR PASS partitions=18862 signs=8191 admissible=1719")


def token_face_map(amplitudes: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for face, amplitude in enumerate(amplitudes):
        out.extend([face] * amplitude)
    return tuple(out)


@lru_cache(None)
def face_groups(amplitudes: tuple[int, ...]):
    """Aggregate partition weights by tied-face sign set and |current|."""
    r, m = len(amplitudes), sum(amplitudes)
    token_blocks = []
    offset = 0
    for a in amplitudes:
        token_blocks.append(((1 << a) - 1) << offset)
        offset += a
    token_to_face = {}
    for bits in range(1 << r):
        expanded = sum(token_blocks[i] for i in range(r) if bits & (1 << i))
        token_to_face[expanded] = bits

    scale, records = TABLES[m]
    groups: dict[tuple[int, int], int] = defaultdict(int)
    for h, coeff, masks in records:
        allowed = 0
        for mask in masks:
            bits = token_to_face.get(mask)
            if bits is not None:
                allowed |= 1 << bits
        if allowed:
            groups[allowed, h // 5] += coeff
    return scale, tuple((allowed, q, coeff) for (allowed, q), coeff in sorted(groups.items()))


@lru_cache(None)
def relations(r: int) -> tuple[int, ...]:
    """All signed set-partition relations on r face signs."""
    out: list[int] = []

    def visit(labels: tuple[int, ...], relative: tuple[int, ...], k: int) -> None:
        if len(labels) == r:
            mask = 0
            for signs in range(1 << k):
                bits = sum((((signs >> labels[i]) & 1) ^ relative[i]) << i for i in range(r))
                mask |= 1 << bits
            out.append(mask)
            return
        for block in range(k):
            for sign in (0, 1):
                visit(labels + (block,), relative + (sign,), k)
        visit(labels + (k,), relative + (0,), k + 1)

    visit((), (), 0)
    assert len(out) == len(set(out))
    return tuple(out)


def completion_audit() -> None:
    expected_relations = (1, 1, 3, 11, 49, 257, 1539)
    cases = 0
    zero_cases = 0
    maximum = Fraction(0)
    witness = None

    for r in range(7):
        assert len(relations(r)) == expected_relations[r]
        for doubled in range(r + 1):
            amplitudes = (1,) * (r - doubled) + (2,) * doubled
            scale, groups = face_groups(amplitudes)

            valid = 0
            charged = 0
            twice = 0
            for bits in range(1 << r):
                total = sum(v if bits & (1 << i) else -v for i, v in enumerate(amplitudes))
                if total % 5 == 0:
                    valid |= 1 << bits
                    if total:
                        charged |= 1 << bits
                    if abs(total) == 10:
                        twice |= 1 << bits

            for exterior in relations(r):
                cases += 1
                mass = 0
                first = 0
                second = 0
                for allowed, q, coeff in groups:
                    count = (allowed & exterior).bit_count()
                    if count:
                        assert count & (count - 1) == 0
                    mass += coeff * count
                    first += coeff * count * int(q != 0)
                    second += coeff * count * q * q

                direct = (valid & exterior).bit_count()
                numerator = (charged & exterior).bit_count()
                q2 = numerator + 3 * (twice & exterior).bit_count()

                assert mass == scale * direct
                assert first == scale * numerator
                assert second == scale * q2

                if direct:
                    fraction = Fraction(numerator, direct)
                    if fraction > maximum:
                        maximum = fraction
                        witness = (r, doubled, direct, numerator)
                else:
                    zero_cases += 1
                    assert (mass, first, second) == (0, 0, 0)

    assert cases == 12616
    assert maximum == 1
    assert witness is not None
    print(f"EXTERIOR_COMPLETIONS PASS cases={cases} inadmissible={zero_cases}")
    print(
        "CONDITIONAL_CHARGE_MAX exact=1 "
        f"witness_faces={witness[0]} doubled_faces={witness[1]} "
        f"admissible_signings={witness[2]}"
    )


def gluing_audit() -> None:
    fixtures = (
        (
            (1,) * 7,
            (
                ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1)),
                ((0, 1), (1, 1), (2, -1), (3, -1), (5, 1), (6, 1)),
            ),
        ),
        (
            (1, 1, 2, 2),
            (
                ((0, 1), (1, 1), (2, 1), (3, 1)),
                ((0, 1), (1, -1), (2, 1), (3, -1)),
            ),
        ),
        (
            (2,) * 6,
            (
                ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1)),
                ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1)),
            ),
        ),
    )

    covariance_entries = 0
    for amplitudes, edges in fixtures:
        r = len(amplitudes)
        edge_weights = []
        denominator = 1

        for edge in edges:
            local_amplitudes = tuple(amplitudes[i] for i, _ in edge)
            scale, groups = face_groups(local_amplitudes)
            denominator *= scale
            weights = [0] * (1 << r)

            for bits in range(1 << r):
                local_bits = 0
                for j, (face, eps) in enumerate(edge):
                    positive = bool(bits & (1 << face))
                    if eps < 0:
                        positive = not positive
                    if positive:
                        local_bits |= 1 << j
                for allowed, _, coeff in groups:
                    if allowed & (1 << local_bits):
                        weights[bits] += coeff
            edge_weights.append(weights)

        combined = [1] * (1 << r)
        for weights in edge_weights:
            combined = [a * b for a, b in zip(combined, weights)]

        direct_vectors = []
        for bits in range(1 << r):
            x = tuple(amplitudes[i] if bits & (1 << i) else -amplitudes[i] for i in range(r))
            ok = all(sum(eps * x[i] for i, eps in edge) % 5 == 0 for edge in edges)
            assert combined[bits] == denominator * int(ok)
            if ok:
                direct_vectors.append(x)

        assert direct_vectors
        for i, j in product(range(r), repeat=2):
            lhs = sum(
                combined[bits]
                * (amplitudes[i] if bits & (1 << i) else -amplitudes[i])
                * (amplitudes[j] if bits & (1 << j) else -amplitudes[j])
                for bits in range(1 << r)
            )
            rhs = denominator * sum(x[i] * x[j] for x in direct_vectors)
            assert lhs == rhs
            covariance_entries += 1

    assert covariance_entries == 101
    print("GLUING PASS fixtures=3 covariance_entries=101")


Cell = tuple[tuple[int, ...], tuple[int, ...]]
Chain = dict[Cell, int]


def shift(x: tuple[int, ...], axis: int, amount: int, L: int) -> tuple[int, ...]:
    return tuple((value + (amount if i == axis else 0)) % L for i, value in enumerate(x))


def combine(*terms: tuple[int, Chain]) -> Chain:
    out: dict[Cell, int] = defaultdict(int)
    for factor, chain in terms:
        for cell_key, value in chain.items():
            out[cell_key] += factor * value
    return {cell_key: value for cell_key, value in out.items() if value}


def cell(x: tuple[int, ...], axes: tuple[int, ...]) -> Chain:
    return {(x, axes): 1}


def boundary(chain: Chain, L: int) -> Chain:
    out: dict[Cell, int] = defaultdict(int)
    for (x, axes), coefficient in chain.items():
        for k, axis in enumerate(axes):
            rest = axes[:k] + axes[k + 1 :]
            sign = coefficient * (-1 if k % 2 else 1)
            out[shift(x, axis, 1, L), rest] += sign
            out[x, rest] -= sign
    return {key: value for key, value in out.items() if value}


def defect(x: tuple[int, ...], L: int) -> Chain:
    cubes = combine(
        (-1, cell(x, (0, 1, 2))),
        (1, cell(shift(x, 2, -1, L), (0, 1, 2))),
        (-1, cell(x, (0, 1, 3))),
        (1, cell(shift(x, 3, -1, L), (0, 1, 3))),
    )
    return combine((1, boundary(cubes, L)), (-5, cell(x, (0, 1))))


def incidence(chain: Chain, L: int):
    faces = sorted(chain)
    out: dict[Cell, list[tuple[int, int]]] = defaultdict(list)
    for i, face in enumerate(faces):
        for edge, eps in boundary({face: 1}, L).items():
            out[edge].append((i, eps))
    return faces, out


def support_connected(n: Chain, L: int) -> tuple[bool, Counter, int]:
    faces, edges = incidence(n, L)
    adjacent = [set() for _ in faces]
    degree_census = Counter()
    charged_edges = 0

    for incidences in edges.values():
        degree_census[len(incidences)] += 1
        values = [eps * n[faces[i]] for i, eps in incidences]
        total = sum(values)
        assert total % 5 == 0
        assert len(values) in (2, 5)
        if total:
            assert abs(total) == 5
            charged_edges += 1
        root = incidences[0][0]
        for i, _ in incidences[1:]:
            adjacent[root].add(i)
            adjacent[i].add(root)

    seen = {0}
    queue = [0]
    while queue:
        here = queue.pop()
        for other in adjacent[here]:
            if other not in seen:
                seen.add(other)
                queue.append(other)

    return len(seen) == len(faces), degree_census, charged_edges


def cup_audit() -> None:
    L = 4
    origin = (0, 0, 0, 0)
    center = cell(origin, (0, 1))
    cups = [center]

    for axis in (2, 3):
        positive = boundary(cell(origin, (0, 1, axis)), L)
        negative = boundary(cell(shift(origin, axis, -1, L), (0, 1, axis)), L)
        cups.extend(
            (
                combine((1, center), (1, positive)),
                combine((1, center), (-1, negative)),
            )
        )

    assert [len(cup) for cup in cups] == [1, 5, 5, 5, 5]
    support = set().union(*(set(cup) for cup in cups))
    assert len(support) == 21

    b = boundary(center, L)
    assert all(boundary(cup, L) == b for cup in cups)

    all_cups = combine(*((1, cup) for cup in cups))
    assert all_cups == {p: -v for p, v in defect(origin, L).items()}

    connected, degree_census, charged_edges = support_connected(all_cups, L)
    assert connected
    assert degree_census == Counter({2: 32, 5: 4})
    assert charged_edges == 4

    faces = sorted(support)
    states = []
    for t in product((-1, 0, 1), repeat=5):
        if sum(t) % 5:
            continue
        n = combine(*((coefficient, cup) for coefficient, cup in zip(t, cups)))
        assert not boundary(boundary(n, L), L)
        if sum(t):
            assert boundary(n, L) == {edge: sum(t) * value for edge, value in b.items()}
        else:
            assert not boundary(n, L)
        vector = tuple(n.get(face, 0) for face in faces)
        weight = 1 << (21 - len(n))
        states.append((vector, weight))

    assert len(states) == 53
    Z = sum(w for _, w in states)
    assert all(sum(w * v[i] for v, w in states) == 0 for i in range(21))

    direct = [[0] * 21 for _ in range(21)]
    replica = [[0] * 21 for _ in range(21)]

    for v, w in states:
        for i in range(21):
            for j in range(21):
                direct[i][j] += w * v[i] * v[j]

    for v, w in states:
        for u, z in states:
            d = tuple(x - y for x, y in zip(v, u))
            weight = w * z
            for i in range(21):
                for j in range(21):
                    replica[i][j] += weight * d[i] * d[j]

    assert all(
        replica[i][j] == 2 * Z * direct[i][j]
        for i, j in product(range(21), repeat=2)
    )
    print("FOUR_CUP PASS states=53 replica_pairs=2809 covariance_entries=441")


def forced_local_connectivity(amplitudes: tuple[int, ...], expected_q: int) -> int:
    """Count compatible labelled partitions and verify every one joins all faces."""
    m = sum(amplitudes)
    token_to_face = token_face_map(amplitudes)
    compatible = 0

    tied_masks = set()
    offset = 0
    for bits in range(1 << len(amplitudes)):
        token_mask = 0
        for face, amplitude in enumerate(amplitudes):
            if bits & (1 << face):
                token_mask |= ((1 << amplitude) - 1) << offset
            offset += amplitude
        tied_masks.add(token_mask)
        offset = 0

    for h, _, blocks in partitions(m):
        masks = set(signings(blocks))
        if not (masks & tied_masks):
            continue
        compatible += 1
        assert h // 5 == expected_q

        graph = [set() for _ in amplitudes]
        for block in blocks:
            touched = sorted({token_to_face[token] for token in block})
            for a in touched:
                for b in touched:
                    if a != b:
                        graph[a].add(b)

        seen = {0}
        queue = [0]
        while queue:
            here = queue.pop()
            for other in graph[here]:
                if other not in seen:
                    seen.add(other)
                    queue.append(other)
        assert len(seen) == len(amplitudes)

    assert compatible > 0
    return compatible


def tube_audit() -> None:
    pair_partitions = forced_local_connectivity((2, 2), 0)
    ten_partitions = forced_local_connectivity((2,) * 5, 2)
    assert pair_partitions == 2
    assert ten_partitions == 1

    origin = (0, 0, 0, 0)
    support_sizes = []

    for D in (3, 4, 5, 8, 13):
        L = 2 * D + 4
        end = shift(origin, 1, D + 1, L)
        tube = combine(
            *((1, cell(shift(origin, 1, k, L), (0, 1, 2))) for k in range(1, D + 1))
        )
        n = combine(
            (1, defect(origin, L)),
            (1, defect(end, L)),
            (-1, boundary(tube, L)),
        )

        assert set(n.values()) <= {-1, 1}
        assert len(n) == 4 * D + 40
        support_sizes.append(len(n))

        current5 = boundary(n, L)
        target = combine(
            (-5, boundary(cell(origin, (0, 1)), L)),
            (-5, boundary(cell(end, (0, 1)), L)),
        )
        assert current5 == target
        assert not boundary(current5, L)

        connected, _, charged_edges = support_connected(n, L)
        assert connected
        assert charged_edges == 8

        e = (origin, (0,))
        f = (end, (0,))
        assert current5[e] == current5[f] == -5

        # Replica pair n1=n, n2=-n gives d=2n and a=2 on every active face.
        # Every neutral degree-two edge then has exactly two cross-face pairings.
        # Every charged degree-five edge has exactly one ten-block.
        # Since the support graph is connected, every compatible auxiliary
        # wiring has one component containing both marked charged blocks.
        difference_product = (2 * current5[e] // 5) * (2 * current5[f] // 5)
        assert difference_product == 4

        A = [0] * L
        for (x, axes), value in n.items():
            if axes == (0, 1):
                A[x[1]] += 2 * value
        assert A == [-10 if r in (0, D + 1) else 0 for r in range(L)]

        H = [value // 5 for value in A]
        assert all(value % 5 == 0 for value in A)
        median = sorted(H)[L // 2]
        ell = sum(abs(value - median) for value in H)
        assert ell == 4

    assert support_sizes == [52, 56, 60, 72, 92]
    print(
        "TORUS_WITNESS PASS D=3,4,5,8,13 "
        "conditional_connection=1 difference_current_product=4 ell=4"
    )
    print("UNIFORM_CONDITIONAL_THINNING REFUTED scope=declared_admitted_conditioning")


def root_budget_audit() -> None:
    c = Fraction(5**6, 3**11)
    p = 2 * c / (1 + 2 * c)
    disagreement = 2 * p - Fraction(3, 2) * p * p

    assert c == Fraction(15625, 177147)
    assert p == Fraction(31250, 208397)
    assert p < Fraction(1, 6)
    assert 0 < disagreement < 1

    for a in (Fraction(0), p, Fraction(1, 2), Fraction(1)):
        masses = {-1: a / 2, 0: 1 - a, 1: a / 2}
        direct_disagreement = sum(
            wx * wy
            for x, wx in masses.items()
            for y, wy in masses.items()
            if x != y
        )
        second = sum(
            wx * wy * (x - y) ** 2
            for x, wx in masses.items()
            for y, wy in masses.items()
        )
        assert direct_disagreement == 2 * a - Fraction(3, 2) * a * a
        assert second == 2 * a

    print(f"ROOT_BUDGET PASS p_upper={p} disagreement_upper={disagreement}")


def main() -> None:
    face_table_audit()
    star_audit()
    token_audit()
    completion_audit()
    gluing_audit()
    cup_audit()
    tube_audit()
    root_budget_audit()
    print("AUDIT PASS; uniform_Xi=OPEN; P1=OPEN; no_physical_promotion")


if __name__ == "__main__":
    main()
