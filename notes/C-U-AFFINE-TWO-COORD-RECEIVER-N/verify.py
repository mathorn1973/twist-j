#!/usr/bin/env python3
"""Result-exposed exact audit. NON-CANONICAL, L1; no old verifier imports.

The second matrix path is a same-author cross-check, not independent-agent
confirmation. Infinite statements are proved in PROOF.md, not by simulation.
"""
from itertools import product
from collections import Counter
import json

F5 = range(5)
TD = (2, 1, 3, 4, 1, 1)
TE = (2, 1, 3, 4, 2, 1)
TRACE = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))


def mod(x):
    return tuple(t % 5 for t in x)


def gen(k, x):
    a, u, c, v, q, r = x
    if k == 0:
        return (u, a, v, c, q, r)
    if k == 1:
        return mod((-c, -v, -a, -u, -q, -r))
    if k == 2:
        return mod((2-c, 1-v+r, 2-a, 1-u-r, 1-q, -r))
    if k == 3:
        return mod((2-a, 1-u, 3-c, 4-v, 1-q, 1-r))
    if k == 4:
        return mod((2-a, 1-u, 3-c, 4-v, 2-q, 1-r))
    raise ValueError('invalid generator')


def matrix_gen(k, x):
    rows = [dict() for _ in F5] + [dict()]
    offset = (0,) * 6
    if k == 0:
        for i, j in enumerate((1, 0, 3, 2, 4, 5)):
            rows[i][j] = 1
    elif k == 1:
        for i, j in enumerate((2, 3, 0, 1, 4, 5)):
            rows[i][j] = -1
    elif k == 2:
        for i, j in enumerate((2, 3, 0, 1, 4, 5)):
            rows[i][j] = -1
        rows[1][5] = 1
        rows[3][5] = -1
        offset = (2, 1, 2, 1, 1, 0)
    elif k in (3, 4):
        for i in range(6):
            rows[i][i] = -1
        offset = TD if k == 3 else TE
    else:
        raise ValueError('invalid matrix generator')
    return tuple((sum(a*x[j] for j, a in row.items()) + offset[i]) % 5
                 for i, row in enumerate(rows))


def step(x, t):
    return gen((sum(x) + 2*t) % 5, x)


def theta(n):
    return n.bit_count() % 2


def fields(x):
    a, u, c, v, q, r = x
    A, B, C, D, sigma, w = mod((a+c, u+v, a-c-2, u-v-1, q+r, q-r))
    H = (sigma + 3*(A-B)) % 5
    return A, B, C, D, sigma, w, H


def chart2(x):
    A, B, C, D, sigma, w, H = fields(x)
    return D, H, x[0], x[2], B, w


def inverse2(y):
    D, H, a, c, B, w = y
    sigma = (H-3*(a+c-B)) % 5
    return mod((a, 3*(B+D+1), c, 3*(B-D-1),
                3*(sigma+w), 3*(sigma-w)))


def chart3(x):
    a, u, c, v, q, r = x
    return u, v, (q+r) % 5, a, c, (q-r) % 5


def inverse3(y):
    u, v, sigma, a, c, w = y
    return mod((a, u, c, v, 3*(sigma+w), 3*(sigma-w)))


def read2(y):
    D, H = y
    if H == 0:
        return (4-3*D) % 5
    if H in (2, 3):
        return (4-2*D) % 5
    return None


def read3(y):
    u, v, sigma = y
    B, D = (u+v) % 5, (u-v-1) % 5
    Z = (2*B+sigma) % 5
    if B == 2 and sigma == 3:
        assert Z == 2
        return u
    if B in (2, 3) and Z in (1, 4):
        return (4-B*Z*D) % 5
    return None


def read_first(x):
    A, B, C, D, sigma, w, H = fields(x)
    assert A == B and H == sigma
    return (2-A*(2*A+H)*C) % 5


def initial(lam, mu):
    return mod((lam, 0, 2-lam, 0, -1-mu, mu-1))


def tail_point(lam, mu, B, z, r):
    C = (2-lam)*pow(B*z % 5, -1, 5) % 5
    D = (4-mu)*pow(B*z % 5, -1, 5) % 5
    return mod((3*(B+C+2), 3*(B+D+1), 3*(B-C-2),
                3*(B-D-1), z-2*B-r, r))


def main():
    report = {}
    all_states = tuple(product(F5, repeat=6))
    image0, image1 = set(), set()
    origin_routes = Counter()
    for x in all_states:
        assert inverse2(chart2(x)) == x
        assert chart2(inverse2(x)) == x
        assert inverse3(chart3(x)) == x
        assert chart3(inverse3(x)) == x
        for k in F5:
            assert gen(k, x) == matrix_gen(k, x)
            assert gen(k, gen(k, x)) == x
        for t, image in ((0, image0), (1, image1)):
            y = step(x, t)
            assert sum(y) % 5 == TRACE[t][sum(x) % 5]
            image.add(y)
        x1 = step(x, 0)
        x2 = step(x1, 1)
        x3 = step(x2, 1)
        z0, z1, z2, z3 = (sum(y) % 5 for y in (x, x1, x2, x3))
        assert z2 in (1, 2) and z3 == 1
        offset = TD if z2 == 1 else TE
        assert mod(a+b for a, b in zip(x2, x3)) == offset
        origin_routes[(z0, z1, z2, z3)] += 1
    assert len(image0) == 6250 and len(image1) == 9375
    assert all(sum(x) % 5 != 0 for x in image1)
    expected_routes = {(0,0,2,1):3125, (1,4,1,1):3125, (2,0,2,1):3125,
                       (3,4,1,1):3125, (4,4,1,1):3125}
    assert dict(origin_routes) == expected_routes
    report['global'] = {'states':len(all_states), 'coordinate_inverse_checks':4*len(all_states),
                        'generator_matrix_checks':5*len(all_states),
                        'selected_trace_checks':2*len(all_states),
                        'image_sizes':[len(image0),len(image1)],
                        'origin_routes':[[*k,v] for k,v in sorted(origin_routes.items())]}

    tails = {}
    bare, reduced = {m:set() for m in F5}, {m:set() for m in F5}
    for lam, mu, B, z, r in product(F5, F5, (2,3), (1,4), F5):
        x = tail_point(lam, mu, B, z, r)
        assert x not in tails
        tails[x] = (lam, mu)
        bare[mu].add((x[1],x[3]))
        reduced[mu].add(chart2(x)[:2])
    assert len(tails) == 500
    for x, (lam,mu) in tails.items():
        assert read2(chart2(x)[:2]) == read3(chart3(x)[:3]) == mu
        assert read_first(x) == lam
        for t in (0,1):
            y = step(x,t)
            assert tails[y] == (lam,mu)
    for mu in F5:
        expected = {((3-2*mu)%5,0), ((2*mu+2)%5,2), ((2*mu+2)%5,3)}
        assert reduced[mu] == expected
        assert len(bare[mu]) == (2 if mu==4 else 4)
    classes = sorted({tuple(m for m in F5 if bare[m]==bare[mu]) for mu in F5})
    assert classes == [(0,3),(1,2),(4,)]
    report['tail'] = {'states':len(tails),'all_control_edges':2*len(tails),
                      'bare_pair_classes':classes,'reduced_support_sizes':[len(reduced[m]) for m in F5]}

    states = {(lam,mu):initial(lam,mu) for lam,mu in product(F5,repeat=2)}
    prefixes = 0
    for n in range(5,1025):
        assert len({fields(x)[4] for x in states.values()}) == 1
        assert len({fields(x)[6] for x in states.values()}) == 1
        for (lam,mu),x in states.items():
            expected = None if n in (5,7) else lam if n==6 else mu
            assert read2(chart2(x)[:2]) == expected
            assert read3(chart3(x)[:3]) == expected
            if n in (5,7):
                assert chart2(x)[:2] == (4,4)
                assert chart3(x)[:3] == (0,0,3)
                assert x == initial(lam,mu)
            if n>=9:
                assert tails[x] == (lam,mu)
                assert read_first(x) == lam
            if n<9:
                assert (sum(x)+2*theta(n)) % 5 == (0,0,2,4)[n-5]
                prefixes += 1
        states = {key:step(x,theta(n)) for key,x in states.items()}
    report['prepared'] = {'pairs':25,'prefix_edges':prefixes,'trajectory_checkpoint_checks':25*1020,
                          'first_counter':5,'last_checked_counter':1024}

    starts = []
    for n in range(4096):
        word = tuple(theta(n+j) for j in range(4))
        criterion = n % 2 == 1 and tuple(theta(n//2+j) for j in range(3)) == (1,0,1)
        assert (word == (0,0,1,1)) == criterion
        if criterion:
            assert theta(n-1) == 1
            starts.append(n)
    assert starts[:5] == [5,23,29,39,53]
    for k in range(4,32):
        n = 3*(1<<k)+5
        assert tuple(theta(n+j) for j in range(4)) == (0,0,1,1)
        assert theta(n-1) == 1
    report['clock'] = {'criterion_indices':4096,'first_starts':starts[:5],
                       'explicit_family_k':[4,31],'explicit_family_checks':28}
    report['status'] = 'PASS / NON-CANONICAL / candidate-C / L1'
    report['universal_claims'] = 'PROOF.md; finite audit is not an all-time proof'
    print(json.dumps(report,sort_keys=True,separators=(',',':')))


if __name__ == '__main__':
    main()
