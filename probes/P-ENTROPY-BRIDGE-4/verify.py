#!/usr/bin/env python3
# P-ENTROPY-BRIDGE-4 exact verifier. Finite pentagon quotient, equivariance,
# quotient holonomy, affine cocycle, and bounded component-local no-go.
# Exact integer arithmetic, Python standard library only, no filesystem writes.

import sys
from collections import deque
from itertools import product

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)
N = 5 ** 6
CHECKS = []


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-r) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + r * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + r * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + r * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + r * U_VEC[3]) % 5,
            (1 - q) % 5, (-r) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = 5 * i + x[k]
    return i


STATES = tuple(dec(i) for i in range(N))
ZTAB = tuple(sum(s) % 5 for s in STATES)


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def compose(f, g):
    """Return f after g for state tables or local permutations."""
    return tuple(f[g[i]] for i in range(len(g)))


def perm_group(generators):
    n = len(generators[0])
    identity = tuple(range(n))
    group = {identity}
    frontier = [identity]
    while frontier:
        g = frontier.pop()
        for h in generators:
            for candidate in (compose(g, h), compose(h, g)):
                if candidate not in group:
                    group.add(candidate)
                    frontier.append(candidate)
    return group


def local_perm(points, mapping):
    points = tuple(sorted(points))
    index = {x: i for i, x in enumerate(points)}
    try:
        return tuple(index[mapping[x]] for x in points)
    except KeyError:
        return None


def group_cells(points, group):
    points = tuple(sorted(points))
    unseen = set(range(len(points)))
    cells = []
    while unseen:
        i = min(unseen)
        orbit = {g[i] for g in group}
        unseen -= orbit
        cells.append(frozenset(points[j] for j in orbit))
    return frozenset(cells)


def build_kernel():
    F = []
    for theta in (0, 1):
        gt = tuple(GENS[(z + 2 * theta) % 5] for z in range(5))
        F.append(tuple(enc(gt[ZTAB[i]](STATES[i])) for i in range(N)))
    return tuple(F)


def census(F, tm):
    warm = tuple(F[tm[n]] for n in range(400))
    window = tuple(F[tm[n]] for n in range(400, 700))
    signatures = set()
    support = set()
    for seed in range(N):
        state = seed
        for step in warm:
            state = step[state]
        seen = set()
        for step in window:
            seen.add(state)
            state = step[state]
        signature = frozenset(seen)
        signatures.add(signature)
        support.update(signature)
    components = tuple(sorted(signatures, key=lambda a: (len(a), min(a))))
    return frozenset(support), components


def block_maps(F):
    # Phi^(k+1)_eps = Phi^(k)_(1-eps) after Phi^(k)_eps.
    blocks = [(F[0], F[1])]
    for _ in range(10):
        prev = blocks[-1]
        blocks.append((compose(prev[1], prev[0]),
                       compose(prev[0], prev[1])))
    return tuple(blocks)


def return_group(blocks, component_half, half, k):
    outer_eps = (half - k) % 2
    generators = []
    for eps in (0, 1):
        ret = compose(blocks[k][outer_eps], blocks[k][eps])
        perm = local_perm(component_half, ret)
        if perm is None:
            return None
        generators.append(perm)
    return perm_group(tuple(generators))


def matmul(A, B, mod):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) % mod
                       for j in range(4)) for i in range(4))


I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
ZM = ((0, 0, 0, -1), (1, 0, 0, -1),
      (0, 1, 0, -1), (0, 0, 1, -1))
LM = tuple(tuple(I4[i][j] - ZM[i][j] for j in range(4))
           for i in range(4))
MJ = ((1, 0, -1, 1), (0, 1, -1, 0),
      (1, 0, 0, 0), (0, 1, -1, 1))


def matpow(A, exponent, mod):
    result = I4
    base = tuple(tuple(x % mod for x in row) for row in A)
    while exponent:
        if exponent & 1:
            result = matmul(result, base, mod)
        base = matmul(base, base, mod)
        exponent >>= 1
    return result


def lambda_images_mod5():
    images = {}
    power = I4
    for depth in range(1, 5):
        power = matmul(power, LM, 5)
        images[depth] = {
            tuple(sum(power[i][j] * v[j] for j in range(4)) % 5
                  for i in range(4))
            for v in product(range(5), repeat=4)
        }
    return images


LAMBDA_IMAGES = lambda_images_mod5()


def member_lambda(depth, vector):
    vector = tuple(x % 25 for x in vector)
    if depth <= 4:
        return tuple(x % 5 for x in vector) in LAMBDA_IMAGES[depth]
    if depth >= 8:
        return all(x == 0 for x in vector)
    if any(x % 5 for x in vector):
        return False
    divided = tuple((x // 5) % 5 for x in vector)
    return divided in LAMBDA_IMAGES[depth - 4]


def element_plus_one(exponent):
    power = matpow(MJ, exponent, 25)
    return tuple((power[i][0] + (1 if i == 0 else 0)) % 25
                 for i in range(4))


def factors(tm, length, cache):
    if length not in cache:
        cache[length] = tuple(sorted({tuple(tm[i:i + length])
                                      for i in range(len(tm) - length)}))
    return cache[length]


def component_feasibility(F, tm, allowed, length, cursor, clock, cache):
    words = factors(tm, length, cache)
    word_id = {word: i for i, word in enumerate(words)}
    extensions = factors(tm, length + 1, cache)
    node_count = len(words) * clock
    adjacency = [[] for _ in range(node_count)]
    for word in extensions:
        source = word_id[word[:length]]
        target = word_id[word[1:]]
        theta = word[cursor]
        for tick in range(clock):
            adjacency[source * clock + tick].append(
                (target * clock + ((tick + 1) % clock), theta))
    reverse = [[] for _ in range(node_count)]
    for source, edges in enumerate(adjacency):
        for target, _ in edges:
            reverse[target].append(source)

    assigned_piece = [-1] * node_count
    total = 0
    piece_id = 0
    allowed = tuple(sorted(allowed))
    for root in range(node_count):
        if assigned_piece[root] != -1:
            continue
        queue = deque([root])
        assigned_piece[root] = piece_id
        piece = [root]
        while queue:
            node = queue.popleft()
            neighbors = [target for target, _ in adjacency[node]] + reverse[node]
            for target in neighbors:
                if assigned_piece[target] == -1:
                    assigned_piece[target] = piece_id
                    queue.append(target)
                    piece.append(target)
        piece_id += 1

        directed = [root]
        reached = {root}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for target, _ in adjacency[node]:
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
                    directed.append(target)

        for seed in allowed:
            values = {root: seed}
            consistent = True
            for node in directed:
                value = values.get(node)
                if value is None:
                    consistent = False
                    break
                for target, theta in adjacency[node]:
                    new_value = F[theta][value]
                    old_value = values.get(target)
                    if old_value is None:
                        values[target] = new_value
                    elif old_value != new_value:
                        consistent = False
                        break
                if not consistent:
                    break
            if consistent and len(values) == len(piece):
                total += 1
    return total


# Filled from the disclosed, explicitly non-formal development replay before
# the preregistration pin. Each row is (k, eps, sorted unique (a,b) pairs).
EXPECTED_AFFINE = (
    (0, 0, ((4, 0), (4, 2))),
    (0, 1, ((4, 0), (4, 2))),
    (1, 0, ((1, 0), (1, 3))),
    (1, 1, ((1, 0), (1, 3))),
    (2, 0, ((1, 1), (1, 3))),
    (2, 1, ((1, 1), (1, 3))),
    (3, 0, ((1, 1), (1, 4))),
    (3, 1, ((1, 1), (1, 4))),
    (4, 0, ((1, 0), (1, 3))),
    (4, 1, ((1, 0), (1, 3))),
    (5, 0, ((1, 0), (1, 3))),
    (5, 1, ((1, 0), (1, 3))),
    (6, 0, ((1, 1), (1, 3))),
    (6, 1, ((1, 1), (1, 3))),
    (7, 0, ((1, 1), (1, 4))),
    (7, 1, ((1, 1), (1, 4))),
    (8, 0, ((1, 0), (1, 3))),
    (8, 1, ((1, 0), (1, 3))),
    (9, 0, ((1, 0), (1, 3))),
    (9, 1, ((1, 0), (1, 3))),
    (10, 0, ((1, 1), (1, 3))),
    (10, 1, ((1, 1), (1, 3))),
)


def main():
    tm = tuple(n.bit_count() & 1 for n in range(1 << 16))
    F = build_kernel()
    recurrent, components = census(F, tm)
    halves = (frozenset(F[0][x] for x in recurrent),
              frozenset(F[1][x] for x in recurrent))
    blocks = block_maps(F)

    check("G01 CORE           recurrent core 6250 on 313 components;"
          " 312 of size 20 and one of size 10; halves 3125 + 3125",
          len(recurrent) == 6250 and len(components) == 313
          and [len(c) for c in components].count(20) == 312
          and [len(c) for c in components].count(10) == 1
          and len(halves[0]) == len(halves[1]) == 3125
          and halves[0].isdisjoint(halves[1]))

    j10 = element_plus_one(10)
    j2 = element_plus_one(2)
    check("G02 ARITHMETIC     J^10 + 1 lies in lambda^6 O but not"
          " lambda^7 O; J^2 + 1 lies in lambda O but not lambda^2 O",
          member_lambda(6, j10) and not member_lambda(7, j10)
          and member_lambda(1, j2) and not member_lambda(2, j2))

    invariant = all(F[eps][x] in component
                    for component in components for eps in (0, 1)
                    for x in component)
    parity = True
    for k in range(11):
        for eps in (0, 1):
            target = halves[(eps + k) % 2]
            for source in halves:
                parity = parity and {blocks[k][eps][x] for x in source} == target
    check("G03 FRAME          each component is invariant under both"
          " letters; Im Phi^(k)_eps = H_(eps+k mod 2) bijectively on"
          " both source halves for k = 0..10", invariant and parity)

    partitions = {}
    groups = {}
    pentagon_ok = True
    totals = {0: 0, 1: 0}
    for component_id, component in enumerate(components):
        for half in (0, 1):
            points = component & halves[half]
            baseline = None
            for k in range(11):
                group = return_group(blocks, points, half, k)
                if group is None:
                    pentagon_ok = False
                    continue
                cells = group_cells(points, group)
                groups[(component_id, half, k)] = group
                partitions[(component_id, half, k)] = cells
                if k == 0:
                    pentagon_ok = pentagon_ok and len(group) == 1
                    continue
                pentagon_ok = pentagon_ok and len(group) == 5
                pentagon_ok = pentagon_ok and all(len(cell) == 5 for cell in cells)
                if baseline is None:
                    baseline = cells
                    totals[half] += len(cells)
                else:
                    pentagon_ok = pentagon_ok and cells == baseline
            expected_cells = 1 if len(component) == 10 else 2
            pentagon_ok = pentagon_ok and len(baseline or ()) == expected_cells
    check("G04 PENTAGONS      k = 0 vertex groups are trivial; for every"
          " component and half the k = 1..10 groups are cyclic order 5,"
          " with constant five-cells: 2 per 20-half, 1 per singlet-half,"
          " 625 = 5^4 per full half",
          pentagon_ok and totals == {0: 625, 1: 625})

    base_cells = {}
    cell_of = {}
    equivariant = True
    for component_id, component in enumerate(components):
        for half in (0, 1):
            cells = partitions[(component_id, half, 2)]
            base_cells[(component_id, half)] = cells
            for cell in cells:
                for state in cell:
                    cell_of[state] = cell
    for cell in set(cell_of.values()):
        for eps in (0, 1):
            image_cells = {cell_of[F[eps][state]] for state in cell}
            equivariant = equivariant and len(image_cells) == 1
    check("G05 EQUIVARIANCE   both one-tick branch maps carry every"
          " canonical pentagon cell onto one canonical pentagon cell",
          equivariant)

    quotient_trivial = True
    for component_id, component in enumerate(components):
        for half in (0, 1):
            points = component & halves[half]
            outer_eps_by_k = {k: (half - k) % 2 for k in range(1, 9)}
            for k, outer_eps in outer_eps_by_k.items():
                for eps in (0, 1):
                    ret = compose(blocks[k][outer_eps], blocks[k][eps])
                    for cell in base_cells[(component_id, half)]:
                        quotient_trivial = quotient_trivial and {
                            cell_of[ret[state]] for state in cell
                        } == {cell}
    check("G06 QUOTIENT       the induced vertex holonomy on the"
          " pentagon-class quotient is trivial for k = 1..8",
          quotient_trivial)

    coordinates = {}
    gauge_ok = True
    for component_id, component in enumerate(components):
        for half in (0, 1):
            # The named level-2 cross-letter return fixes the orientation
            # coherently on every cell of this component-half. Choosing an
            # arbitrary group element separately in each cell would erase
            # the multiplier information by a cellwise change of gauge.
            generator_table = compose(blocks[2][half], blocks[2][1 - half])
            for cell in base_cells[(component_id, half)]:
                ordered = tuple(sorted(cell))
                origin = ordered[0]
                coord = {}
                state = origin
                for value in range(5):
                    coord[state] = value
                    state = generator_table[state]
                gauge_ok = gauge_ok and state == origin and len(coord) == 5
                coordinates[cell] = coord

    affine_ok = gauge_ok
    affine_rows = []
    singlet_id = next(i for i, c in enumerate(components) if len(c) == 10)
    for k in range(11):
        for eps in (0, 1):
            per_component = {}
            for component_id, component in enumerate(components):
                pairs = set()
                for half in (0, 1):
                    for cell in base_cells[(component_id, half)]:
                        destination_cells = {
                            cell_of[blocks[k][eps][state]] for state in cell
                        }
                        if len(destination_cells) != 1:
                            affine_ok = False
                            continue
                        destination = next(iter(destination_cells))
                        source_coord = coordinates[cell]
                        destination_coord = coordinates[destination]
                        values = [None] * 5
                        for state, x in source_coord.items():
                            values[x] = destination_coord[blocks[k][eps][state]]
                        b = values[0]
                        a = (values[1] - b) % 5
                        affine_ok = affine_ok and a in (1, 2, 3, 4)
                        affine_ok = affine_ok and all(
                            values[x] == (a * x + b) % 5 for x in range(5)
                        )
                        pairs.add((a, b))
                per_component[component_id] = tuple(sorted(pairs))
            reference = per_component[singlet_id]
            affine_ok = affine_ok and all(row == reference
                                          for row in per_component.values())
            affine_rows.append((k, eps, reference))
    row_map = {(k, eps): pairs for k, eps, pairs in affine_rows}
    period_ok = all(row_map[(k, eps)] == row_map[(k + 4, eps)]
                    for eps in (0, 1) for k in range(1, 7))
    affine_ok = affine_ok and period_ok
    affine_ok = affine_ok and tuple(affine_rows) == EXPECTED_AFFINE
    check("G07 AFFINE         every level-k cell map is affine over F_5"
          " in the canonical level-2 gauge; all 313 component spectra"
          " equal the frozen table and repeat with period 4, k = 1..10",
          affine_ok)

    clocks = (1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 80)
    positions = lambda length: (0, length // 2, length - 1)
    singlet = components[singlet_id]
    canonical_20 = min((c for c in components if len(c) == 20), key=min)
    cache = {}
    no_go_ok = True
    no_go_cases = 0
    for component in (singlet, canonical_20):
        for length in range(4, 17):
            for cursor in positions(length):
                for clock in clocks:
                    count = component_feasibility(
                        F, tm, component, length, cursor, clock, cache
                    )
                    no_go_ok = no_go_ok and count == 0
                    no_go_cases += 1
    for length in range(17, 31):
        for cursor in positions(length):
            count = component_feasibility(
                F, tm, singlet, length, cursor, 4, cache
            )
            no_go_ok = no_go_ok and count == 0
            no_go_cases += 1
    check("G08 BOUNDED-NOGO   zero component-local cylinder solutions in"
          " all 900 frozen cases: singlet and canonical 20-component,"
          " L = 4..16, three cursor positions, eleven clocks; plus"
          " singlet clock 4 through L = 30", no_go_ok and no_go_cases == 900)

    print("P-ENTROPY-BRIDGE-4 exact verifier")
    print("finite pentagon quotient of the driven kernel; component and")
    print("block-map frame; equivariance; trivial finite quotient holonomy;")
    print("canonical affine F_5 cocycle; bounded component-local no-go")
    print()
    print("AFFINE TABLE")
    for k, eps, pairs in affine_rows:
        encoded = " ".join("%d,%d" % pair for pair in pairs)
        print("k=%02d eps=%d %s" % (k, eps, encoded))
    print()
    passed = 0
    for index, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        passed += int(ok)
        print("%s %02d %s" % (tag, index, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
