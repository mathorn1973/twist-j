#!/usr/bin/env python3
"""Frozen exact audit of the declared D3 cochain comparison; no physics gate."""
from fractions import Fraction as Q
from itertools import combinations, product
import json

B = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
EDGES = tuple(combinations(range(4), 2))
TRIPLES = tuple(combinations(range(4), 3))
FACES = tuple((s, t) for s in (1, -1) for t in TRIPLES)

def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))

def neg(a):
    return tuple(-x for x in a)

V = tuple(sub(B[j], B[i]) for i, j in EDGES)
LOOKUP = {v: (e, 1) for e, v in enumerate(V)}
LOOKUP.update({neg(v): (e, -1) for e, v in enumerate(V)})

def face_terms(sign, triple):
    pts = [tuple(sign*x for x in B[i]) for i in triple]
    out = []
    for p, q in zip(pts, pts[1:] + pts[:1]):
        edge, direction = LOOKUP[sub(q, p)]
        out.append((edge, p if direction == 1 else q, direction))
    return out

def transpose(a):
    return [list(x) for x in zip(*a)]

def mm(a, b):
    out = [[0]*len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x*y
    return out

def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def zero(a):
    return all(not x for row in a for x in row)

def rank(a):
    a = [list(map(Q, row)) for row in a]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [x/pivot for x in a[r]]
        for i in range(r+1, len(a)):
            t = a[i][c]
            if t:
                a[i] = [x-t*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r

def shifted(a, value):
    return [[x-value*(i == j) for j, x in enumerate(row)]
            for i, row in enumerate(a)]

def real_complex(L):
    vertices = tuple(product(range(L), repeat=3))
    pos = {x: i for i, x in enumerate(vertices)}
    def at(x, p):
        return pos[tuple((x[i]+p[i]) % L for i in range(3))]
    G = [[0]*len(vertices) for _ in range(6*len(vertices))]
    C = [[0]*(6*len(vertices)) for _ in range(8*len(vertices))]
    for ix, x in enumerate(vertices):
        for e, v in enumerate(V):
            G[6*ix+e][at(x, v)] += 1
            G[6*ix+e][ix] -= 1
        for f, (s, t) in enumerate(FACES):
            for e, p, d in face_terms(s, t):
                C[8*ix+f][6*at(x, p)+e] += d
    return G, C

# Exact Gaussian integers are pairs (real, imaginary).
ONE, ZERO = (1, 0), (0, 0)
ROOTS = (ONE, (0, 1), (-1, 0), (0, -1))

def ga(a, b):
    return (a[0]+b[0], a[1]+b[1])

def gm(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def gc(a):
    return (a[0], -a[1])

def gs(d, a):
    return (d*a[0], d*a[1])

def phase(p, z):
    out = ONE
    for n, zz in zip(p, z):
        for _ in range(abs(n)):
            out = gm(out, zz if n >= 0 else gc(zz))
    return out

def gmm(a, b):
    out = [[ZERO]*len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for j in range(len(b[0])):
            for k, x in enumerate(row):
                out[i][j] = ga(out[i][j], gm(x, b[k][j]))
    return out

def bloch(z):
    C = [[ZERO]*6 for _ in FACES]
    for f, (s, t) in enumerate(FACES):
        for e, p, d in face_terms(s, t):
            C[f][e] = ga(C[f][e], gs(d, phase(p, z)))
    G = [[ga(phase(v, z), (-1, 0))] for v in V]
    assert all(x == ZERO for row in gmm(C, G) for x in row)
    star = [[gc(C[r][c]) for r in range(8)] for c in range(6)]
    return gmm(star, C)

def charpoly(a):
    n = len(a)
    p = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    traces = [0]
    for _ in range(n):
        p = gmm(p, a)
        tr = ZERO
        for i in range(n):
            tr = ga(tr, p[i][i])
        assert tr[1] == 0
        traces.append(tr[0])
    coeff = [1]
    for m in range(1, n+1):
        s = -sum(coeff[m-i]*traces[i] for i in range(1, m+1))
        assert s % m == 0
        coeff.append(s//m)
    return coeff

def polymul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def energy(a, b, P, sigma):
    d = [x-y for x, y in zip(a, b)]
    return (dot(d, d)+sigma*dot(a, mv(P, b)))/2

def main():
    G, C = real_complex(2)
    GT, CT = transpose(G), transpose(C)
    assert zero(mm(C, G))
    assert (rank(G), rank(C)) == (7, 38)
    P = mm(CT, C)
    mult = {l: 48-rank(shifted(P, l)) for l in (0, 2, 4, 6, 8)}
    assert mult == {0: 10, 2: 8, 4: 12, 6: 8, 8: 10}
    assert sum(mult.values()) == 48
    for z in product(ROOTS, repeat=3):
        S = ONE
        for zz in z:
            S = ga(S, zz)
        r2 = gm(gc(S), S)[0]
        quad = [16-r2, -8, 1]
        expected = polymul(polymul([0, 1], [-8, 1]), polymul(quad, quad))
        assert charpoly(bloch(z)) == list(reversed(expected))

    euclid = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1))
    vectors = [sub(euclid[j], euclid[i]) for i, j in EDGES]
    moment = [[sum(v[i]*v[j] for v in vectors) for j in range(3)] for i in range(3)]
    assert moment == [[4, 0, 0], [0, 4, 0], [0, 0, 4]]

    sigma = Q(1, 4)
    initial = [Q(row[0]) for row in CT]
    final_energies = []
    for forced in (False, True):
        prev, a = [Q(0)]*48, initial[:]
        initial_energy = energy(a, prev, P, sigma)
        for n in range(1, 17):
            j = [Q(0)]*48
            if forced:
                j[n % 48] = Q(n % 3-1)
            Pa = mv(P, a)
            nxt = [2*x-y-sigma*p-current for x, y, p, current in zip(a, prev, Pa, j)]
            back = [2*x-y-sigma*p-current for x, y, p, current in zip(a, nxt, Pa, j)]
            assert back == prev
            rho0 = mv(GT, [x-y for x, y in zip(a, prev)])
            rho1 = mv(GT, [x-y for x, y in zip(nxt, a)])
            assert rho1 == [x-y for x, y in zip(rho0, mv(GT, j))]
            delta = energy(nxt, a, P, sigma)-energy(a, prev, P, sigma)
            assert delta == -dot(j, [x-y for x, y in zip(nxt, prev)])/2
            if not forced:
                assert energy(nxt, a, P, sigma) == initial_energy
                num0 = [4**(n-1)*x for x in prev]
                num1 = [4**n*x for x in a]
                num2 = [4**(n+1)*x for x in nxt]
                assert all(x.denominator == 1 for x in num0+num1+num2)
                assert num2 == [8*x-y-16*z for x, y, z in zip(num1, mv(P, num1), num0)]
            prev, a = a, nxt
        final_energies.append(str(energy(a, prev, P, sigma)))

    unit = [Q(0)]*48
    unit[0] = Q(1)
    rational_next = [2*x-sigma*y for x, y in zip(unit, mv(P, unit))]
    assert any(x.denominator != 1 for x in rational_next)
    mode = None
    for ix in range(48):
        v = [int(i == ix) for i in range(48)]
        for lam in (0, 2, 4, 6):
            v = mv(shifted(P, lam), v)
        if any(v):
            mode = v
            break
    assert mode is not None and mv(P, mode) == [8*x for x in mode]
    assert 6*6-4 == 32
    scalar = [0, 1]
    for _ in range(8):
        scalar.append(-6*scalar[-1]-scalar[-2])
    assert abs(scalar[-1]) > abs(scalar[-2]) > 1

    wrong = [row[:] for row in C]
    col = next(i for i, x in enumerate(wrong[0]) if x)
    wrong[0][col] *= -1
    assert not zero(mm(wrong, G))
    half = [row for i, row in enumerate(C) if i % 8 < 4]
    assert rank(half) == 24
    gradient = [row[0] for row in G]
    assert not any(mv(P, gradient)) and any(mv(GT, gradient))
    print(json.dumps({
        'status': 'PASS; NON-CANONICAL finite audit, not a physical photon',
        'vertices_edges_faces': [8, 48, 64],
        'ranks_G_C': [7, 38],
        'eigenvalue_multiplicities': mult,
        'exact_Bloch_phase_triples': 64,
        'edge_second_moment': moment,
        'free_and_forced_steps': [16, 16],
        'final_comparison_energies': final_energies,
        'unit_integer_step_eigenvalue': 8,
        'unit_step_scalar_sequence': scalar,
        'rational_step_preserves_raw_integer_fields': False,
        'negative_triangle_omission_rank': 24,
        'wrong_orientation_breaks_CG': True,
        'dropped_Gauss_admits_longitudinal_ramp': True
    }, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
