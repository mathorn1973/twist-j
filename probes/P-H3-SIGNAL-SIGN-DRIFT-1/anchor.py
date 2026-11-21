# SPDX-License-Identifier: Apache-2.0
"""Audit the primitive anchors and the maximal local residue relation."""

from collections import Counter
from itertools import product

from native import cell, h3, ledger, put, reverse, step, transport


PI = h3.sub(h3.ONE, h3.RHO)
REP = h3.J_POWERS
DIVIDEND = h3.ring_sum(h3.scale(4 - k, REP[(2 * k) % 5]) for k in range(4))


def residue(word):
    return sum(word) % 5


def lift(center, gap):
    return h3.add(center, gap), h3.sub(center, gap)


def encode(m, c, d, f):
    return lift(m, d) + lift(c, f)


def coordinates(words):
    a, b, u, v = map(residue, words)
    return tuple(3 * n % 5 for n in (a + b, u + v, a - b, u - v))


def local_graph():
    adjacency = {}
    okay = True
    counts = Counter()
    for state in product(range(5), repeat=4):
        m, c, d, f = state
        mc, fc = (h3.scale(value, h3.ONE) for value in (m, c))
        gap = h3.scale(d or 5, h3.ONE)
        witnesses = [(h3.scale(f or 5, h3.ONE), 0)]
        for unit, branch in ((h3.J, 1), (h3.J_INV, 2)):
            for sign in (-1, 1):
                fg = h3.scale(sign, h3.mul(unit, gap))
                if residue(fg) == f:
                    witnesses.append((fg, branch))
        neighbors = set()
        for fg, expected in witnesses:
            w = encode(mc, fc, gap, fg)
            out, tag = h3.collision(w)
            h3.require(h3.collision(out)[0] == w, "local collision inverse")
            counts[tag] += 1
            okay &= coordinates(w) == state and tag == expected
            neighbors.add(coordinates(out))
        predicted = {state}
        if f * f % 5 == 4 * d * d % 5:
            predicted.update(((m, c, 2*d % 5, 3*f % 5), (m, c, 3*d % 5, 2*f % 5)))
        okay &= neighbors == predicted
        adjacency[state] = neighbors
    unvisited = set(adjacency)
    sizes = Counter()
    while unvisited:
        visited = {unvisited.pop()}
        stack = list(visited)
        while stack:
            new = adjacency[stack.pop()] - visited
            visited.update(new)
            unvisited.difference_update(new)
            stack.extend(new)
        sizes[len(visited)] += 1
    return {"vertices": len(adjacency), "components_by_size": sorted(sizes.items()),
            "lifts_by_tag": sorted(counts.items()), "predictions": bool(okay and sizes == {1:425, 4:50})}


def sector(field, ny, roles):
    nx = len(field) // (ny * 4)
    values = {(x, y, r): cell(field, ny, x, y)[r]
              for x, y in product(range(nx), range(ny)) for r in roles
              if cell(field, ny, x, y)[r] != h3.ZERO}
    if not values:
        return None, frozenset()
    k = 0
    while not any(residue(w) for w in values.values()):
        for site, w in values.items():
            a = h3.mul(DIVIDEND, w)
            h3.require(all(v % 5 == 0 for v in a), "integral pi division")
            values[site] = tuple(v // 5 for v in a)
        k += 1
    return k, frozenset((x, y) for (x, y, r), w in values.items() if residue(w))


def experiment(k, branch):
    ny = nx = 8
    seed = h3.ONE
    for _ in range(k):
        seed = h3.mul(seed, PI)
    d = h3.scale(2, seed)
    unit = h3.J if branch == 1 else h3.J_INV
    field = [h3.ZERO] * (4 * nx * ny)
    put(field, ny, 2, 2, encode(h3.ZERO, h3.ONE, d, h3.mul(unit, d)))
    put(field, ny, 2, 4, encode(h3.ZERO, h3.ZERO, h3.mul(seed, PI), h3.ZERO))
    initial = transport(tuple(field), ny, 0, backward=True)
    roles = ((0, 1), (2, 3))
    expected = [sector(initial, ny, lanes) for lanes in roles]
    fixed = True
    extra = 0
    bit = 0
    state = initial
    for t in range(12):
        post_c, state, events = step(state, ny, bit)
        if t == 0:
            h3.require(post_c == tuple(field), "recover prescribed cut")
            first_tag = next((tag for x, y, tag in events if (x,y) == (2,2)), 0)
        for cut in (post_c, state):
            fixed &= all(sector(cut, ny, lanes) == reference for lanes, reference in zip(roles, expected))
            extra += any((x,y) not in expected[0][1] and any(cell(cut,ny,x,y)[r] != h3.ZERO for r in roles[0])
                         for x,y in product(range(nx),range(ny)))
        bit ^= 1
    for _ in range(12):
        bit ^= 1
        state = reverse(state, ny, bit)
    h3.require(state == initial and bit == 0, "composed inverse")
    return {"k":k, "branch":branch, "first_tag":first_tag,
            "marks":[[e,sorted(s)] for e,s in expected], "cuts_with_extra_matter":extra,
            "Q":ledger(initial)[-1], "passed": fixed and first_tag==branch and expected[0][0]==k}


def run():
    h3.require(h3.mul(PI, DIVIDEND) == h3.scale(5,h3.ONE), "pi divisor identity")
    return {"local_graph":local_graph(), "sector_trials":[experiment(k,b) for k in range(4) for b in (1,2)]}
