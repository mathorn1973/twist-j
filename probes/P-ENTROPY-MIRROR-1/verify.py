#!/usr/bin/env python3
"""Exact verifier for P-ENTROPY-MIRROR-1.

Rebuild the Public Canon v4 driven kernel and decide the six frozen finite
mirror-law gates. Standard library only; no filesystem writes.
"""

import sys


CHECKS = []
S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)
N = 5 ** 6


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    return tuple((-x[i]) % 5 for i in (2, 3, 0, 1, 4, 5))


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return tuple(
        (b4[i] + S_VEC[i] + r * U_VEC[i]) % 5 for i in range(4)
    ) + ((1 - q) % 5, (-r) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def decode(i):
    digits = []
    for _ in range(6):
        digits.append(i % 5)
        i //= 5
    return tuple(digits)


def encode(x):
    value = 0
    for digit in reversed(x):
        value = 5 * value + digit
    return value


def build_letters():
    letters = []
    for theta in (0, 1):
        table = []
        for i in range(N):
            state = decode(i)
            z = sum(state) % 5
            table.append(encode(GENS[(z + 2 * theta) % 5](state)))
        letters.append(tuple(table))
    return tuple(letters)


def thue_morse(length):
    return tuple(bin(n).count("1") & 1 for n in range(length))


def census(F, tm):
    warm = [F[tm[n]] for n in range(400)]
    window = [F[tm[n]] for n in range(400, 700)]
    signatures = set()
    for seed in range(N):
        state = seed
        for table in warm:
            state = table[state]
        orbit = set()
        for table in window:
            orbit.add(state)
            state = table[state]
        signatures.add(frozenset(orbit))
    components = sorted(signatures, key=lambda c: (len(c), min(c)))
    support = set()
    for component in components:
        support |= component
    return support, components


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(g)))


def cycle_type(mapping, points):
    remaining = set(points)
    sizes = {}
    while remaining:
        start = next(iter(remaining))
        length = 0
        q = start
        while q in remaining:
            remaining.discard(q)
            length += 1
            q = mapping[q]
        if q != start:
            return None
        sizes[length] = sizes.get(length, 0) + 1
    return sizes


def orbit_partition(points, generators):
    points = sorted(points)
    parent = {p: p for p in points}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    for p in points:
        for generator in generators:
            q = generator[p]
            root_p, root_q = find(p), find(q)
            if root_p != root_q:
                parent[root_p] = root_q
    cells = {}
    for p in points:
        cells.setdefault(find(p), set()).add(p)
    return [frozenset(cell) for cell in cells.values()]


def main():
    tm = thue_morse(1 << 16)
    F = build_letters()
    support, components = census(F, tm)
    H = (
        frozenset(F[0][x] for x in support),
        frozenset(F[1][x] for x in support),
    )

    sizes = sorted(len(component) for component in components)
    singlet = next(component for component in components if len(component) == 10)
    singlet_id = components.index(singlet)
    check(
        "M01 CORE        recurrent core 6250 on 313 letter-invariant"
        " components (312 x 20 + 1 x 10); halves disjoint 3125 + 3125",
        len(support) == 6250
        and len(components) == 313
        and sizes.count(20) == 312
        and sizes.count(10) == 1
        and len(H[0]) == len(H[1]) == 3125
        and H[0].isdisjoint(H[1])
        and all(
            F[eps][x] in component
            for component in components
            for eps in (0, 1)
            for x in component
        ),
    )

    mirror_ok = True
    fixed_states = []
    for eps in (0, 1):
        mirror_ok = mirror_ok and cycle_type(F[eps], H[eps]) == {
            1: 1,
            2: 1562,
        }
        fixed = [x for x in H[eps] if F[eps][x] == x]
        mirror_ok = mirror_ok and len(fixed) == 1 and fixed[0] in singlet
        fixed_states.append(fixed[0] if fixed else -1)
    check(
        "M02 MIRROR      each letter restricted to its own half is an"
        " involution, cycle type {1: 1, 2: 1562}; its unique fixed state"
        " lies in the singlet component",
        mirror_ok,
    )

    alternation_ok = all(F[1][F[0][x]] == x for x in H[1]) and all(
        F[0][F[1][x]] == x for x in H[0]
    )
    check(
        "M03 ALTERNATION F_1 o F_0 = id on H_1 and F_0 o F_1 = id on"
        " H_0: the cross restrictions are mutually inverse",
        alternation_ok,
    )

    phi_1 = (compose(F[1], F[0]), compose(F[0], F[1]))
    phi_2 = (
        compose(phi_1[1], phi_1[0]),
        compose(phi_1[0], phi_1[1]),
    )
    cells_by_half = {0: [], 1: []}
    cell_of = {}
    cell_component = {}
    swap_ok = True
    for component_id, component in enumerate(components):
        for half in (0, 1):
            points = component & H[half]
            outer = (half - 2) % 2
            generators = [compose(phi_2[outer], phi_2[eps]) for eps in (0, 1)]
            cells = orbit_partition(points, generators)
            swap_ok = swap_ok and all(len(cell) == 5 for cell in cells)
            expected = 1 if len(component) == 10 else 2
            swap_ok = swap_ok and len(cells) == expected
            for cell in cells:
                cells_by_half[half].append(cell)
                cell_component[cell] = component_id
                for state in cell:
                    cell_of[state] = cell
    swap_ok = (
        swap_ok
        and len(cells_by_half[0]) == 625
        and len(cells_by_half[1]) == 625
    )

    T = [{}, {}]
    for eps in (0, 1):
        for half in (0, 1):
            for cell in cells_by_half[half]:
                images = {cell_of[F[eps][state]] for state in cell}
                if len(images) != 1:
                    swap_ok = False
                    T[eps][cell] = cell
                else:
                    T[eps][cell] = next(iter(images))
    for eps in (0, 1):
        swap_ok = swap_ok and cycle_type(T[eps], cells_by_half[eps]) == {
            1: 1,
            2: 312,
        }
        for cell in cells_by_half[eps]:
            image = T[eps][cell]
            swap_ok = swap_ok and cell_component[image] == cell_component[cell]
            if cell_component[cell] == singlet_id:
                swap_ok = swap_ok and image == cell
            else:
                swap_ok = swap_ok and image != cell
    check(
        "M04 SWAP        every one-tick letter fixes the singlet"
        " pentagon of its own half and swaps the two pentagons of every"
        " 20-component-half, cycle type {1: 1, 2: 312}",
        swap_ok,
    )

    coordinates = {}
    gauge_ok = True
    for half in (0, 1):
        generator_table = compose(phi_2[half], phi_2[1 - half])
        for cell in cells_by_half[half]:
            origin = min(cell)
            coordinate = {}
            state = origin
            for value in range(5):
                coordinate[state] = value
                state = generator_table[state]
            gauge_ok = gauge_ok and state == origin and len(coordinate) == 5
            coordinates[cell] = coordinate

    reflection_ok = gauge_ok
    order_census = {((4, 0), (4, 2)): 0, ((4, 2), (4, 0)): 0}
    for half in (0, 1):
        for cell in cells_by_half[half]:
            pair_by_letter = []
            for eps in (0, 1):
                source = coordinates[cell]
                target = coordinates[T[eps][cell]]
                values = [None] * 5
                for state, x in source.items():
                    values[x] = target[F[eps][state]]
                b = values[0]
                a = (values[1] - b) % 5
                reflection_ok = reflection_ok and all(
                    values[x] == (a * x + b) % 5 for x in range(5)
                )
                reflection_ok = reflection_ok and a == 4
                pair_by_letter.append((a, b))
            key = tuple(pair_by_letter)
            if key in order_census:
                order_census[key] += 1
            else:
                reflection_ok = False
    reflection_ok = reflection_ok and order_census == {
        ((4, 0), (4, 2)): 625,
        ((4, 2), (4, 0)): 625,
    }
    check(
        "M05 REFLECTION  in the frozen coherent level-2 gauge every"
        " one-tick cell map has multiplier 4 = -1; the letter pair is"
        " {(4,0), (4,2)} in some order on every cell, each order on"
        " exactly 625 cells",
        reflection_ok,
    )

    consistency_ok = all(
        T[0][T[1][cell]] == T[0][T[0][cell]] for cell in cells_by_half[0]
    ) and all(
        T[1][T[0][cell]] == T[1][T[1][cell]] for cell in cells_by_half[1]
    )
    consistency_ok = consistency_ok and all(
        T[1][T[0][cell]] == T[1][T[1][cell]] for cell in cells_by_half[0]
    ) and all(
        T[0][T[1][cell]] == T[0][T[0][cell]] for cell in cells_by_half[1]
    )
    check(
        "M06 CONSISTENCY the cell-level composition identities"
        " T_a o T_b = T_a o T_a hold on both halves for both mixed orders",
        consistency_ok,
    )

    print("P-ENTROPY-MIRROR-1 exact verifier")
    print("finite mirror law of the Public Canon v4 driven kernel")
    print()
    print(
        "WITNESS fixed state of F_0 on H_0: %d %s"
        % (fixed_states[0], decode(fixed_states[0]))
    )
    print(
        "WITNESS fixed state of F_1 on H_1: %d %s"
        % (fixed_states[1], decode(fixed_states[1]))
    )
    print()
    passed = 0
    for index, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        passed += int(ok)
        print("%s %02d %s" % (tag, index, name))
    print()
    print(
        "RESULT %d/%d %s"
        % (
            passed,
            len(CHECKS),
            "ALL PASS" if passed == len(CHECKS) else "FAILURES PRESENT",
        )
    )
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
