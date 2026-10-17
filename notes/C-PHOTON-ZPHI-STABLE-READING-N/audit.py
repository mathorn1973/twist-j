#!/usr/bin/env python3
"""Frozen exact finite audit for #1404. No external input or floating point."""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import gcd
from functools import reduce
import json

ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
SIGMA = (2, -1)
OFF = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
PAIRS = tuple(combinations(range(4), 2))
TRIPLES = tuple(combinations(range(4), 3))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def scale(c, x):
    return (c * x[0], c * x[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def conjugate(x):
    return (x[0] + x[1], -x[1])


def sign(x):
    a, b = 2 * x[0] + x[1], x[1]
    sg = lambda z: (z > 0) - (z < 0)
    if not a:
        return sg(b)
    if not b or a * b > 0:
        return sg(a)
    difference = a * a - 5 * b * b
    return sg(difference) if a > 0 else -sg(difference)


def dot(x, y):
    result = ZERO
    for a, b in zip(x, y):
        result = add(result, mul(a, b))
    return result


def apply(matrix, x):
    return [sum(coef * x[j] for j, coef in row.items()) for row in matrix]


def ring_apply(matrix, x):
    return list(zip(apply(matrix, [a for a, _ in x]),
                    apply(matrix, [b for _, b in x])))


def incidence(dims):
    sites = tuple(product(*(range(d) for d in dims)))
    vertex = {x: i for i, x in enumerate(sites)}
    edges = {(x, ij): n for n, (x, ij) in enumerate(product(sites, PAIRS))}
    shift = lambda x, v: tuple((a + b) % d for a, b, d in zip(x, v, dims))
    diff = lambda x, y: tuple(a - b for a, b in zip(x, y))
    G = []
    for x, ij in edges:
        i, j = ij
        row = {}
        for v, c in ((vertex[x], -1), (vertex[shift(x, diff(OFF[j], OFF[i]))], 1)):
            row[v] = row.get(v, 0) + c
        G.append({v: c for v, c in row.items() if c})
    C = []
    for x in sites:
        for i, j, k in TRIPLES:
            for orientation in (1, -1):
                if orientation == 1:
                    terms = ((i, (i, j), 1), (j, (j, k), 1), (i, (i, k), -1))
                else:
                    terms = ((j, (i, j), -1), (k, (j, k), -1), (k, (i, k), 1))
                row = {}
                for at, ij, coeff in terms:
                    pos = shift(x, tuple(orientation * z for z in OFF[at]))
                    e = edges[(pos, ij)]
                    row[e] = row.get(e, 0) + coeff
                C.append({e: c for e, c in row.items() if c})
    P = [dict() for _ in edges]
    for face in C:
        boundary = {}
        for e, c in face.items():
            for v, d in G[e].items():
                boundary[v] = boundary.get(v, 0) + c * d
            for f, d in face.items():
                P[e][f] = P[e].get(f, 0) + c * d
        assert all(v == 0 for v in boundary.values()), 'CG'
    P = [{e: c for e, c in row.items() if c} for row in P]
    assert all(P[j].get(i, 0) == c for i, row in enumerate(P) for j, c in row.items())
    return G, C, P


def divergence(G, field):
    count = 1 + max(v for row in G for v in row)
    out = [ZERO] * count
    for row, x in zip(G, field):
        for v, c in row.items():
            out[v] = add(out[v], scale(c, x))
    return out


def step(P, cur, old, current):
    return [sub(sub(sub(scale(2, a), b), mul(SIGMA, p)), j)
            for a, b, p, j in zip(cur, old, ring_apply(P, cur), current)]


def block_step(P, cur, old, current):
    u, v = [x[0] for x in cur], [x[1] for x in cur]
    pu, pv = apply(P, u), apply(P, v)
    return [(2 * u[i] - old[i][0] - 2 * pu[i] + pv[i] - current[i][0],
             2 * v[i] - old[i][1] + pu[i] - pv[i] - current[i][1])
            for i in range(len(cur))]


def energy(P, cur, old):
    d = [sub(x, y) for x, y in zip(cur, old)]
    return add(dot(d, d), mul(SIGMA, dot(cur, ring_apply(P, old))))


def embedding(x, which):
    return (F(2 * x[0] + x[1], 2), F(which * x[1], 2))


def radical_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def radical_step(P, cur, old, current, which):
    coeff = (F(3, 2), F(-which, 2))
    return [sub(sub(sub(scale(2, a), b), radical_mul(coeff, p)), j)
            for a, b, p, j in zip(cur, old, ring_apply(P, cur), current)]


def mprod(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def determinant(a):
    n = len(a)
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        value = (-1) ** inversions
        for i in range(n):
            value *= a[i][p[i]]
        total += value
    return total


def main():
    assert mul(PHI, PHI) == add(PHI, ONE)
    assert mul(SIGMA, conjugate(SIGMA)) == ONE
    assert sign(SIGMA) == 1 and sign(sub((F(1, 2), 0), SIGMA)) == 1
    pairs = tuple(product(range(-3, 4), repeat=2))
    for x in pairs:
        assert conjugate(conjugate(x)) == x
        assert mul(x, conjugate(x)) == (x[0]**2 + x[0]*x[1] - x[1]**2, 0)
        assert sign(mul(x, x)) == (x != ZERO)
        for y in pairs:
            assert embedding(mul(x, y), 1) == radical_mul(embedding(x, 1), embedding(y, 1))
            assert conjugate(mul(x, y)) == mul(conjugate(x), conjugate(y))

    records = []
    total_basis = 0
    small_P = None
    for dims in ((2, 2, 2), (3, 2, 2)):
        G, C, P = incidence(dims)
        E = len(P)
        zero = [ZERO] * E
        eight = [((1, -1, 0, 1, 0, 0)[i % 6], 0) for i in range(E)]
        assert ring_apply(P, eight) == [scale(8, x) for x in eight]
        for column in range(4 * E):
            cur, old = zero[:], zero[:]
            slot, component = divmod(column % (2 * E), 2)
            target = cur if column < 2 * E else old
            target[slot] = (1, 0) if component == 0 else (0, 1)
            nxt = step(P, cur, old, zero)
            assert nxt == block_step(P, cur, old, zero)
            assert step(P, cur, nxt, zero) == old
        total_basis += 4 * E
        final_energy = []
        for forced in (False, True):
            old = zero[:]
            cur = [(C[0].get(i, 0), C[3].get(i, 0)) for i in range(E)]
            initial_energy = energy(P, cur, old)
            assert sign(initial_energy) > 0
            old_rad = {w: [embedding(x, w) for x in old] for w in (1, -1)}
            cur_rad = {w: [embedding(x, w) for x in cur] for w in (1, -1)}
            for n in range(1, 25):
                current = zero[:]
                if forced:
                    current[n % E] = (n % 3 - 1, 0)
                    i = (3 * n + 1) % E
                    current[i] = add(current[i], (0, n % 5 - 2))
                nxt = step(P, cur, old, current)
                assert nxt == block_step(P, cur, old, current)
                assert step(P, cur, nxt, current) == old
                difference = [sub(a, b) for a, b in zip(nxt, old)]
                assert sub(energy(P, nxt, cur), energy(P, cur, old)) == neg(dot(current, difference))
                rho_old = divergence(G, [sub(a, b) for a, b in zip(cur, old)])
                rho_new = divergence(G, [sub(a, b) for a, b in zip(nxt, cur)])
                div_j = divergence(G, current)
                assert rho_new == [sub(a, b) for a, b in zip(rho_old, div_j)]
                for w in (1, -1):
                    nxt_rad = radical_step(P, cur_rad[w], old_rad[w],
                                           [embedding(x, w) for x in current], w)
                    assert nxt_rad == [embedding(x, w) for x in nxt]
                    old_rad[w], cur_rad[w] = cur_rad[w], nxt_rad
                d = [sub(a, b) for a, b in zip(nxt, cur)]
                lower = mul(sub(ONE, scale(2, SIGMA)), dot(d, d))
                assert sign(sub(energy(P, nxt, cur), lower)) >= 0
                if not forced:
                    assert energy(P, nxt, cur) == initial_energy
                old, cur = cur, nxt
            final_energy.append(list(energy(P, cur, old)))
        records.append({'torus': list(dims), 'cells': [len(G)//6, E, len(C)],
                        'free_forced_steps': [24, 24], 'final_doubled_energies': final_energy})
        if dims == (2, 2, 2):
            small_P = P

    P = small_P
    v = None
    for j in range(len(P)):
        y = [int(i == j) for i in range(len(P))]
        for lam in (0, 4, 6, 8):
            y = [p - lam * a for p, a in zip(apply(P, y), y)]
        if any(y):
            d = reduce(gcd, y)
            v = [a // d for a in y]
            break
    assert v is not None and apply(P, v) == [2*a for a in v]
    assert reduce(gcd, v) == 1
    normal = sum(a*a for a in v)
    factor, previous_energy = ONE, None
    for m in range(13):
        state = [scale(a, factor) for a in v]
        assert reduce(gcd, [z for x in state for z in x]) == 1
        en = energy(P, state, [ZERO]*len(P))
        assert en == scale(normal, mul(factor, factor)) and sign(en) > 0
        if previous_energy is not None:
            assert sign(sub(previous_energy, en)) > 0
        previous_energy, factor = en, mul(SIGMA, factor)

    mode_polys = {}
    identity = [[int(i == j) for j in range(4)] for i in range(4)]
    for lam in (0, 2, 4, 6, 8):
        T = [[2-2*lam, lam, -1, 0], [lam, 2-lam, 0, -1],
             [1, 0, 0, 0], [0, 1, 0, 0]]
        assert determinant(T) == 1
        coefficients = [1, 3*lam-4, lam*lam-6*lam+6, 3*lam-4, 1]
        value = [[0]*4 for _ in range(4)]
        power = identity
        for c in coefficients:
            value = [[value[i][j]+c*power[i][j] for j in range(4)] for i in range(4)]
            power = mprod(power, T)
        assert not any(x for row in value for x in row)
        mode_polys[str(lam)] = coefficients
    kappa = (6, 8)
    assert sign(sub(kappa, (F(325, 18), 0))) > 0
    assert sign(sub((F(362, 19), 0), kappa)) > 0
    old, cur = ZERO, ONE
    sequence = [list(old), list(cur)]
    for _ in range(16):
        old, cur = cur, sub(mul(sub((2, 0), scale(8, SIGMA)), cur), old)
        sequence.append(list(cur))

    Mphi = [[0, 1], [1, 1]]
    continuous = 0
    for a, b, c, d in product(range(-2, 3), repeat=4):
        B = [[a, b], [c, d]]
        condition = (b == c and d == a + c)
        assert condition == (mprod(B, Mphi) == mprod(Mphi, B))
        assert condition == ((b-c, d-a-c) == ZERO)
        continuous += condition
    assert continuous == 19
    unit = ONE
    for _ in range(13):
        assert mul(unit, conjugate(unit)) == ONE
        assert sign(unit) > 0 and sign(conjugate(unit)) > 0
        unit = mul(unit, SIGMA)

    spatial_offsets = ((0,0,0), (1,1,0), (1,0,1), (0,1,1))
    moment = {}
    for i, j in PAIRS:
        vec = tuple(b-a for a, b in zip(spatial_offsets[i], spatial_offsets[j]))
        for axes in product(range(3), repeat=4):
            powers = tuple(axes.count(k) for k in range(3))
            value = 1
            for axis in axes:
                value *= vec[axis]
            moment[powers] = moment.get(powers, 0) + value
    moment = {p: c for p, c in moment.items() if c}
    expected = {(4,0,0):4, (0,4,0):4, (0,0,4):4,
                (2,2,0):12, (2,0,2):12, (0,2,2):12}
    assert moment == expected
    r4 = {p: (1 if 4 in p else 2) for p in moment}
    quartic = {p: -F(moment[p],96)+F(r4[p],32) for p in moment}
    axis = quartic[(4,0,0)]
    diagonal = sum(quartic.values())/9
    assert axis == -F(1,96) and diagonal == -F(7,288)
    time_axis = add(scale(axis,SIGMA), scale(F(1,48),mul(SIGMA,SIGMA)))
    time_diag = add(scale(diagonal,SIGMA), scale(F(1,48),mul(SIGMA,SIGMA)))
    assert time_axis == (F(8,96), -F(5,96))
    assert time_diag == (F(16,288), -F(11,288))
    assert sub(time_diag,time_axis) == scale(-F(1,72),SIGMA)

    result = {'status':'PASS; NON-CANONICAL exact finite audit, no photon quantum',
              'ring_pair_products':len(pairs)**2, 'tori':records,
              'complete_integer_basis_columns':total_basis,
              'primitive_fixed_stiffness':2, 'primitive_unit_scalings':13,
              'primitive_mode_squared_norm':normal,
              'mode_polynomials_ascending':mode_polys,
              'lambda8_ring_sequence':sequence, 'conjugate_growth_bounds':[18,19],
              'continuous_coefficient_matrices':[continuous,625],
              'spatial_quartic_axis_diagonal':[str(axis),str(diagonal)],
              'temporal_quartic_axis':[str(x) for x in time_axis],
              'temporal_quartic_diagonal':[str(x) for x in time_diag]}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
