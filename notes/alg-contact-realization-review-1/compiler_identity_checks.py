#!/usr/bin/env python3
"""Finite symbol audit of SPEC B.2--B.3; not the universal compiler.

Import defines functions only. run_checks() is a scientific gate and must not
be called before the accepted public pin. Products act right to left.

The audit evaluates B3/B4 on five symbols, all ordered transposition pairs
on six symbols, and Even/Attach2/B6 on old sets of size 3 through 6. A fixed
outside sentinel checks support at every construction. These finite tests do
not enumerate arbitrary carrier sizes, the list of 16^k words, or N-3 steps.
The universal conclusions remain the substitution identities and termination
proofs in SPEC B.2--B.4 and the connectivity proof in SPEC section 5.3.
"""

from itertools import combinations, permutations, product


def need(condition, label, witness=None):
    if not condition:
        raise ValueError({"assertion": label, "witness": witness})


def identity(n):
    return tuple(range(n))


def mul(*words):
    """Return w0 o w1 o ...; no reversal of syntactic product order."""
    if not words:
        raise ValueError("mul needs an ambient permutation")
    result = identity(len(words[0]))
    for word in words:
        result = tuple(result[word[i]] for i in range(len(result)))
    return result


def inv(word):
    result = [0] * len(word)
    for i, j in enumerate(word):
        result[j] = i
    return tuple(result)


def cycle(n, points):
    result = list(range(n))
    for i, point in enumerate(points):
        result[point] = points[(i + 1) % len(points)]
    return tuple(result)


def comm(f, g):
    return mul(f, g, inv(f), inv(g))


def parity(word, old):
    images = [word[i] for i in old]
    return sum(images[i] > images[j] for i in range(len(old))
               for j in range(i + 1, len(old))) % 2


def stars(old, n):
    a, b = old[:2]
    return {x: cycle(n, (a, b, x)) for x in old[2:]}


def k_word(i, j, old, star):
    a, b = old[:2]
    need(i != j and b not in (i, j), "B3.arguments", (i, j))
    if i == a:
        return inv(star[j])
    if j == a:
        return star[i]
    return mul(star[j], inv(star[i]), inv(star[j]))


def c_word(i, j, k, old, star):
    b = old[1]
    points = (i, j, k)
    need(len(set(points)) == 3, "B4.arguments", points)
    if b in points:
        t = points.index(b)
        rotated = points[t:] + points[:t]
        return k_word(rotated[1], rotated[2], old, star)
    return mul(k_word(i, j, old, star), k_word(j, k, old, star))


def pair_word(first, second, old, star, n):
    """The literal three cases of the adjacent transposition rule in B.2."""
    intersection = set(first) & set(second)
    if len(intersection) == 2:
        return identity(n)
    if len(intersection) == 1:
        shared = next(iter(intersection))
        p = next(x for x in first if x != shared)
        q = next(x for x in second if x != shared)
        return c_word(p, shared, q, old, star)
    a, b = sorted(first)
    c, d = sorted(second)
    return mul(c_word(a, c, b, old, star), c_word(a, c, d, old, star))


def even_word(word, old, star):
    """Evaluate the canonical Even_U syntax using the current star words."""
    n = len(word)
    need(not parity(word, old), "Even.even_input", (old, word))
    visited = set()
    transpositions = []
    for start in sorted(old):
        if start in visited:
            continue
        points = []
        current = start
        while current not in visited:
            need(current in old, "Even.closed_support", (old, word, current))
            visited.add(current)
            points.append(current)
            current = word[current]
        need(current == start, "Even.cycle_closure", (start, current))
        transpositions.extend((start, x) for x in reversed(points[1:]))
    need(len(transpositions) % 2 == 0, "Even.pair_count")
    result = identity(n)
    for i in range(0, len(transpositions), 2):
        result = mul(result, pair_word(transpositions[i], transpositions[i+1],
                                      old, star, n))
    return result


def normalize_edge(points, old, old_count):
    """Rotate, never reverse, the oriented edge according to B.3."""
    for offset in range(3):
        rotated = points[offset:] + points[:offset]
        if tuple(point in old for point in rotated) == (True,)*old_count + (False,)*(3-old_count):
            return rotated
    raise ValueError({"assertion": "B3.edge_membership", "witness": points})


def prescribed_map(old, n, p, q):
    a, b = old[:2]
    remaining = iter(x for x in sorted(old) if x not in (a, b))
    result = list(range(n))
    for source in sorted(old):
        result[source] = a if source == p else b if source == q else next(remaining)
    return tuple(result)


def attach2(points, old, star, n):
    """B5, including the distinct |U|=3 odd-orientation branch."""
    p, q, x = normalize_edge(points, old, 2)
    edge = cycle(n, (p, q, x))
    mapping = prescribed_map(old, n, p, q)
    branch = "even"
    if parity(mapping, old):
        if len(old) >= 4:
            repair = tuple(v for v in sorted(old) if v not in old[:2])[:2]
            mapping = mul(cycle(n, repair), mapping)
            branch = "odd_size_at_least_4"
        else:
            edge = inv(edge)
            p, q = q, p
            mapping = prescribed_map(old, n, p, q)
            branch = "odd_size_3"
    need(not parity(mapping, old), "B5.repaired_parity", (old, points))
    need((mapping[p], mapping[q]) == tuple(old[:2]), "B5.anchor_images", (old, points))
    transport = even_word(mapping, old, star)
    result = mul(transport, edge, inv(transport))
    return result, x, branch


def run_checks():
    """Run the bounded finite audit only; return actual counted rows."""
    counts = {"B3_rows": 0, "B4_rows": 0, "transposition_pairs": 0,
              "pair_equal": 0, "pair_shared": 0, "pair_disjoint": 0,
              "even_permutations": 0, "attach2_rows": 0, "B6_rows": 0}
    old = tuple(range(5))
    n = 6  # Outside sentinel 5 must remain fixed.
    star = stars(old, n)
    for i, j in permutations((0, 2, 3, 4), 2):
        need(k_word(i, j, old, star) == cycle(n, (1, i, j)), "B3.identity", (i, j))
        counts["B3_rows"] += 1
    for points in permutations(old, 3):
        need(c_word(*points, old, star) == cycle(n, points), "B4.identity", points)
        counts["B4_rows"] += 1
    old = tuple(range(6))
    n = 7
    star = stars(old, n)
    transpositions = tuple(combinations(old, 2))
    for first, second in product(transpositions, repeat=2):
        result = pair_word(first, second, old, star, n)
        need(result == mul(cycle(n, first), cycle(n, second)),
             "B2.transposition_pair", (first, second))
        counts["transposition_pairs"] += 1
        kind = {2: "pair_equal", 1: "pair_shared", 0: "pair_disjoint"}[len(set(first) & set(second))]
        counts[kind] += 1
    attach_branches = {"even": 0, "odd_size_at_least_4": 0, "odd_size_3": 0}
    for size in range(3, 7):
        old = tuple(range(size))
        n = size + 3  # two possible new points and one untouched sentinel
        star = stars(old, n)
        for images in permutations(old):
            word = images + tuple(range(size, n))
            if not parity(word, old):
                need(even_word(word, old, star) == word,
                     "B2.canonical_even", (size, word))
                counts["even_permutations"] += 1
        for p, q in permutations(old, 2):
            points = (p, q, size)
            for offset in range(3):
                rotated = points[offset:] + points[:offset]
                result, x, branch = attach2(rotated, old, star, n)
                need(x == size and result == cycle(n, (0, 1, size)),
                     "B5.attach2", (size, rotated, branch))
                attach_branches[branch] += 1
                counts["attach2_rows"] += 1
        for p in old:
            q, r = tuple(v for v in old if v != p)[:2]
            for x, y in ((size, size+1), (size+1, size)):
                points = (p, x, y)
                for offset in range(3):
                    rotated = points[offset:] + points[:offset]
                    normalized = normalize_edge(rotated, old, 1)
                    edge = cycle(n, normalized)
                    derived = comm(c_word(p, q, r, old, star), edge)
                    need(derived == cycle(n, (p, q, x)), "B6.commutator", (size, rotated))
                    first, new_x, _ = attach2((p, q, x), old, star, n)
                    need(new_x == x and first == cycle(n, (0, 1, x)), "B6.first_attach", (size, rotated))
                    larger = tuple(sorted(old+(x,)))
                    updated = dict(star)
                    updated[x] = first
                    second, new_y, _ = attach2(normalized, larger, updated, n)
                    need(new_y == y and second == cycle(n, (0, 1, y)), "B6.second_attach", (size, rotated))
                    need(all(updated[t] == star[t] for t in star), "B6.old_stars_preserved")
                    counts["B6_rows"] += 1
    expected = {"B3_rows": 12, "B4_rows": 60, "transposition_pairs": 225,
                "pair_equal": 15, "pair_shared": 120, "pair_disjoint": 90,
                "even_permutations": 435, "attach2_rows": 204, "B6_rows": 108}
    need(counts == expected, "compiler.finite_row_counts", counts)
    need(all(value > 0 for value in attach_branches.values()), "B5.all_parity_branches", attach_branches)
    return {"mode": "finite_enumeration", "counts": counts,
            "attach2_branch_counts": attach_branches,
            "ambient_sizes": [6, 7, 8, 9], "old_sizes": [3, 4, 5, 6],
            "proof_dependencies": ["SPEC B.2 (B3,B4,Even)", "SPEC B.3 (B5,B6)",
                                   "SPEC 5.3 and B.4 (connectivity, termination)"]}
