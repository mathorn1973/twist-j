#!/usr/bin/env python3
"""Independent RC audit: exact recurrence, Newton traces, and polarization.

No author verifier is imported. No network or mutable Canon input is read.
The written proof, not a finite return search, handles unbounded times.
"""
from fractions import Fraction as Q
from itertools import product


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(c) for c in zip(*a)]


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c*x for x in r] for r in a]


def matrix_of(fn, n):
    return transpose([fn(e) for e in eye(n)])


def block_diag(a, b):
    return [r+[0]*len(b[0]) for r in a]+[[0]*len(a[0])+r for r in b]


def raw_step(c, y):
    m = len(c)
    e, h = y[:m], y[m:]
    ep = [a+b for a, b in zip(e, mv(c, h))]
    hp = [a-b for a, b in zip(h, mv(transpose(c), ep))]
    return ep+hp


def raw_back(c, y):
    m = len(c)
    ep, hp = y[:m], y[m:]
    h = [a+b for a, b in zip(hp, mv(transpose(c), ep))]
    return [a-b for a, b in zip(ep, mv(c, h))]+h


def active_step(g, y):
    k = len(g)
    z, h = y[:k], y[k:]
    zp = [a+b for a, b in zip(z, h)]
    return zp+[a-b for a, b in zip(h, mv(g, zp))]


def raw_energy(c, y):
    m = len(c)
    e, h = y[:m], y[m:]
    return sum(x*x for x in y)+sum(x*t for x, t in zip(e, mv(c, h)))


def gram_of_energy(fn, n):
    # Polarization gives twice the energy matrix without block-form code.
    basis = eye(n)
    diagonal = [fn(e) for e in basis]
    return [[2*diagonal[i] if i == j else
             fn([x+y for x, y in zip(basis[i], basis[j])])-diagonal[i]-diagonal[j]
             for j in range(n)] for i in range(n)]


def charpoly(a):
    # Newton identities; output descending coefficients, no determinant expansion.
    n = len(a)
    power, traces, coeff = eye(n), [None], [Q(1)]
    for k in range(1, n+1):
        power = mul(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
        coeff.append(-sum(coeff[k-j]*traces[j] for j in range(1, k+1))/k)
    assert all(c.denominator == 1 for c in coeff)
    return [int(c) for c in coeff]


def evaluate_poly(coeff, a):
    n = len(a)
    value = [[0]*n for _ in range(n)]
    for c in coeff:
        value = add(mul(value, a), scale(c, eye(n)))
    return value


def psd_inertia(a):
    # Exact symmetric Schur complements; a zero pivot must have a zero row.
    b = [[Q(x) for x in row] for row in a]
    positive = zero = 0
    for i in range(len(b)):
        p = b[i][i]
        assert p >= 0, ('negative pivot', i, p)
        if p == 0:
            assert all(b[i][j] == 0 for j in range(i+1, len(b)))
            zero += 1
        else:
            positive += 1
            for j in range(i+1, len(b)):
                for k in range(i+1, len(b)):
                    b[j][k] -= b[j][i]*b[i][k]/p
    return positive, zero


def diagonal(signs):
    return [[s if i == j else 0 for j in range(len(signs))]
            for i, s in enumerate(signs)]


def divergence(vertices, edges):
    d = [[0]*len(edges) for _ in range(vertices)]
    for j, (tail, head) in enumerate(edges):
        d[tail][j] += 1
        d[head][j] -= 1
    return d


CASES = [
    ('digon', 2, [(0,1),(0,1)], [[1],[-1]], [[2]], [1,0,1], 4),
    ('triangle', 3, [(0,1),(1,2),(2,0)], [[1],[1],[1]], [[3]], [1,1,1], 3),
    ('digon-digon', 2, [(0,1),(0,1),(0,1)], [[1,1],[-1,0],[0,-1]],
     [[2,1],[1,2]], [1,0,1,0,1], 6),
    ('digon-triangle', 3, [(0,1),(0,1),(0,2),(2,1)], [[1,1],[-1,0],[0,-1],[0,-1]],
     [[2,1],[1,3]], [1,1,1,1,1], 5),
    ('triangle-triangle', 4, [(0,1),(1,2),(2,0),(1,3),(3,0)],
     [[1,1],[1,0],[1,0],[0,1],[0,1]], [[3,1],[1,3]], [1,2,2,2,1], None),
]


def audit_case(case):
    name, vertices, edges, c, expected_g, expected_poly, order = case
    m, k = len(c), len(c[0])
    d = divergence(vertices, edges)
    g = mul(transpose(c), c)
    assert g == expected_g
    assert mul(d, c) == [[0]*k for _ in range(vertices)]
    assert psd_inertia(g) == (k, 0)
    a = matrix_of(lambda y: active_step(g, y), 2*k)
    t = matrix_of(lambda y: raw_step(c, y), m+k)
    ti = matrix_of(lambda y: raw_back(c, y), m+k)
    assert mul(t, ti) == mul(ti, t) == eye(m+k)
    p = block_diag(c, eye(k))
    assert mul(t, p) == mul(p, a)
    br = gram_of_energy(lambda y: raw_energy(c, y), m+k)
    ba = gram_of_energy(lambda y: raw_energy(c, mv(p, y)), 2*k)
    assert ba == mul(mul(transpose(p), br), p)
    assert mul(mul(transpose(t), br), t) == br
    assert mul(mul(transpose(a), ba), a) == ba
    assert charpoly(a) == expected_poly
    raw_poly = expected_poly[:]
    for _ in range(m-k):
        raw_poly = [raw_poly[0]]+[raw_poly[i]-raw_poly[i-1] for i in range(1,len(raw_poly))]+[-raw_poly[-1]]
    assert charpoly(t) == raw_poly
    assert raw_poly[-1] == (-1)**(m+k)  # det T = 1
    assert expected_poly[-1] == 1  # active dimension is even
    assert evaluate_poly(expected_poly, a) == [[0]*(2*k) for _ in range(2*k)]
    zeros = int(order is None)
    assert psd_inertia(br) == (m+k-zeros, zeros)
    assert psd_inertia(ba) == (2*k-zeros, zeros)
    assert psd_inertia(add(scale(4, eye(k)), scale(-1, g))) == (k-zeros, zeros)
    # z_(n+2) = (2I-G)z_(n+1)-z_n, checked as a matrix identity.
    ai = matrix_of(lambda y: [a-b for a,b in zip(y[:k],
                         [u+v for u,v in zip(y[k:], mv(g, y[:k]))])]
                         +[u+v for u,v in zip(y[k:], mv(g, y[:k]))], 2*k)
    assert mul(a, ai) == mul(ai, a) == eye(2*k)
    assert add(a, ai) == block_diag(add(scale(2, eye(k)), scale(-1,g)),
                                   add(scale(2, eye(k)), scale(-1,g)))
    if order:
        power = eye(2*k)
        for n in range(1, order+1):
            power = mul(power, a)
            assert (power == eye(2*k)) == (n == order)
    else:
        v, w = [1,1,-2,-2], [0,0,1,1]
        nmat = add(a, eye(4))
        assert mv(nmat, v) == [0]*4 and mv(nmat, w) == v
        assert sum(x*x for x in v) > 0
        assert raw_energy(c, mv(p,v)) == 0
        assert mul(a,a) != eye(4)  # repeated eigenvalue is NOT enough for order two
    # Audit all orientation conjugacies; proof is uniform, not this enumeration.
    count = 0
    for rs in product((-1,1), repeat=m):
        for ss in product((-1,1), repeat=k):
            r, s = diagonal(rs), diagonal(ss)
            cp = mul(mul(r,c),s)
            dp = mul(d,r)
            gp = mul(transpose(cp),cp)
            qr, qa = block_diag(r,s), block_diag(s,s)
            tp = matrix_of(lambda y: raw_step(cp,y),m+k)
            ap = matrix_of(lambda y: active_step(gp,y),2*k)
            pp = block_diag(cp,eye(k))
            assert mul(dp,cp) == [[0]*k for _ in range(vertices)]
            assert gp == mul(mul(s,g),s)
            assert tp == mul(mul(qr,t),qr)
            assert ap == mul(mul(qa,a),qa)
            assert mul(pp,qa) == mul(qr,p)
            bp = gram_of_energy(lambda y: raw_energy(cp,y),m+k)
            assert mul(mul(qr,bp),qr) == br
            count += 1
    if name == 'digon-triangle':
        s = diagonal([1,-1]); q = block_diag(s,s)
        assert mul(c,s) == [[1,-1],[-1,0],[0,1],[0,1]]
        assert mul(mul(q,a),q) == [[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]]
        assert mul(mul(q,ba),q) == [[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]]
    print(name, 'char='+','.join(map(str,expected_poly)), 'det=1',
          'order='+str(order or 'infinite'), 'energy='+('PSD-nullity-1' if zeros else 'PD'),
          'orientations='+str(count), 'PASS')
    return count


def negative_controls():
    c = [[1],[-1]]
    d = divergence(2, [(0,1),(0,1)])
    bad_c = [[-1],[-1]]  # isolated coefficient flip is not an orientation change
    assert mul(d,bad_c) != [[0],[0]]
    b = gram_of_energy(lambda y: raw_energy(c, mv(block_diag(c,eye(1)),y)),2)
    reversed_order = [[-1,1],[-2,1]]
    assert mul(mul(transpose(reversed_order),b),reversed_order) != b
    print('NEGATIVE_CONTROLS isolated-boundary-flip=REJECTED reversed-shear-energy=REJECTED order-two-at-parabolic-boundary=REJECTED')


def main():
    failures, count = [], 0
    for case in CASES:
        try:
            count += audit_case(case)
        except AssertionError as exc:
            failures.append(case[0]); print('SCIENTIFIC_FAIL',case[0],str(exc))
    try:
        negative_controls()
    except AssertionError as exc:
        failures.append('negative-controls'); print('SCIENTIFIC_FAIL negative-controls',str(exc))
    if count != 248:
        failures.append('orientation-total'); print('SCIENTIFIC_FAIL orientation-total',count)
    print('RC_FIELD_CELL_SHEAR_AUDIT_'+('SCIENTIFIC_FAIL' if failures else 'PASS'))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('INTEGRITY_STOP: optimized Python disables assertions')
    main()
