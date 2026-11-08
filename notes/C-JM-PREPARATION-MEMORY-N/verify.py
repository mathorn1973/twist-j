#!/usr/bin/env python3
"""Exact one-architecture audit of the frozen preparation-memory candidate.
No external packages, floating point, sampling, or physical claims.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt


def transpose(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def diag(v):
    return [[F(v[i]) if i == j else F(0) for j in range(len(v))]
            for i in range(len(v))]


def outer(v, w):
    return [[x*y for y in w] for x in v]


def mv(a, x):
    return [sum(t*u for t, u in zip(row, x)) for row in a]


def dot(x, y):
    return sum(t*u for t, u in zip(x, y))


def kron(a, b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def projector(y, g):
    gy = mv(g, y)
    n = dot(y, gy)
    assert n > 0
    return scale(F(1, n), outer(y, gy))


def mixture(weighted):
    pairs = list(weighted)
    n = len(pairs[0][1])
    out = [[F(0) for _ in range(n)] for _ in range(n)]
    for weight, a in pairs:
        out = add(out, scale(weight, a))
    return out


def tensor_power(a, k):
    out = [[F(1)]]
    for _ in range(k):
        out = kron(out, a)
    return out


def source_ok(z):
    return (z[5]-z[6]-z[7]) % 3 == 0


def q(z):
    a, b = z[:4], z[4:]
    return 5*sum(x*x for x in a)-sum(a)**2+4*sum(x*x for x in b)


ELL = [1, 10, 18, 16, -1, -27, -32, -3]
G = [[F(0) for _ in range(8)] for _ in range(8)]
GI = [[F(0) for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i < 4 and j < 4:
            G[i][j] = F(5*(i == j)-1)
            GI[i][j] = F(1+(i == j), 5)
        elif i == j:
            G[i][j], GI[i][j] = F(4), F(1, 4)
GH = [[F(0) for _ in range(9)] for _ in range(9)]
GHI = [[F(0) for _ in range(9)] for _ in range(9)]
GH[0][0] = GHI[0][0] = F(1)
for i in range(8):
    for j in range(8):
        GH[i+1][j+1], GHI[i+1][j+1] = G[i][j], GI[i][j]
C = dot(ELL, mv(GI, ELL))


def m_bound(Q):
    return isqrt((C.numerator*Q)//(C.denominator*41**2))


def lower_bound(Q):
    return 2*isqrt((Q-8)//(8*41**2))+1


def response(z, j):
    return F((dot(ELL, z)-41*j)**2, 1+q(z))/(C+1681*j*j)


def product_response(z, Q):
    out = F(1)
    m = m_bound(Q)
    for j in range(-m, m+1):
        out *= response(z, j)
    return out


def beta(Q):
    m = m_bound(Q)
    den = F((Q+1)**(2*m+1))
    for j in range(-m, m+1):
        den *= C+1681*j*j
    return 1/den


def main():
    print('C-JM-PREPARATION-MEMORY-N EXACT AUDIT v1')
    # Known collision and genuinely new held-label two-copy comparison.
    g2 = diag([1, 8])
    lam = F(354161, 735212)
    p = {t: F(1, 1+8*t*t) for t in (40, 41, 42)}
    assert p[41] == lam*p[40]+(1-lam)*p[42]
    on = [(F(1, 2), projector([1, t], g2)) for t in (-41, 41)]
    off = [(w/2, projector([1, t], g2))
           for w, mag in [(lam, 40), (1-lam, 42)] for t in (-mag, mag)]
    rho = mixture(on)
    assert rho == mixture(off)
    held_on = mixture((w, kron(a, a)) for w, a in on)
    held_off = mixture((w, kron(a, a)) for w, a in off)
    delta = add(held_off, scale(-1, held_on))
    V = lam*(1-lam)*(p[40]-p[42])**2
    assert V > 0
    ref = diag([1, 0])
    assert tr(mm(delta, kron(ref, ref))) == V
    assert tr(delta) == 0
    assert tr(mm(delta, delta)) == 8*V*V
    assert mm(mm(delta, delta), delta) == scale(4*V*V, delta)
    g4 = kron(g2, g2)
    assert mm(g4, delta) == mm(transpose(delta), g4)
    effect = projector([8, 0, 0, -1], g4)
    assert mm(effect, effect) == effect and tr(effect) == 1
    assert tr(mm(delta, effect)) == 2*V
    for k in range(1, 5):
        assert tensor_power(mixture(on), k) == tensor_power(mixture(off), k)
    print('ONE-COPY COLLISION PASS')
    print('REDRAW tensor powers k=1..4 PASS')
    print('HOLD two-reference gap =', V)
    print('HOLD trace distance and fixed-effect gap =', 2*V)
    print('HOLD trace-distance polynomial certificate PASS')

    assert mm(G, GI) == eye(8)
    assert mm(GH, GHI) == eye(9)
    assert C == F(19639, 20)
    print('DUAL seam coefficient C =', C)
    interval_count = 0
    zero_count = 0
    for Q in (8, 16, 14112):
        m = m_bound(Q)
        L = isqrt((C.numerator*Q)//C.denominator)
        for n in range(-L, L+1):
            polynomial = 1
            for j in range(-m, m+1):
                polynomial *= n-41*j
            assert (polynomial == 0) == (n % 41 == 0)
            interval_count += 1
            zero_count += polynomial == 0
        if Q >= 16:
            assert lower_bound(Q) <= 2*m+1
        print('Q', Q, 'interval', L, 'settings/copies', 2*m+1,
              'one-sided lower', lower_bound(Q))
    assert 2*m_bound(14112)+1 == 181 and lower_bound(14112) == 3
    print('COMPLETE INTEGER-INTERVAL CHECKS', interval_count, 'zeros', zero_count)

    # The effects are fixed by the bound, not by a successful source sample.
    m = m_bound(14112)
    for j in range(-m, m+1):
        L = [-41*j]+ELL
        u = mv(GHI, L)
        norm = dot(L, u)
        assert norm == C+1681*j*j and norm > 0
        E = scale(1/norm, outer(u, L))
        assert E == projector(u, GH)
        assert mm(E, E) == E and tr(E) == 1
        assert mm(GH, E) == mm(transpose(E), GH)
    print('181 RATIONAL PROJECTORS PASS')

    # Small complete ternary-coordinate family with the source congruence.
    tested = 0
    B32 = beta(32)
    for zz in product((-1, 0, 1), repeat=8):
        z = list(zz)
        if not source_ok(z) or not 0 < q(z) <= 32:
            continue
        h = product_response(z, 32)
        seam = dot(ELL, z) % 41 == 0
        assert 0 <= h <= 1 and (h == 0) == seam
        if not seam:
            assert h >= B32
        tested += 1
    print('TERNARY admitted pure-source controls', tested, 'PASS')

    # Held versus redrawn all-on mixture: same single-system source alphabet.
    z0 = [1, 0, 0, 0, 1, 0, 0, 0]
    z41 = [41, 0, 0, 0, -41, 0, 0, 0]
    assert all(source_ok(z) and 0 < q(z) <= 14112 and dot(ELL, z) % 41 == 0
               for z in [z0, z41])
    assert product_response(z0, 14112) == product_response(z41, 14112) == 0
    redraw = F(1)
    for j in range(-m, m+1):
        averaged = (response(z0, j)+response(z41, j))/2
        assert averaged > 0
        redraw *= averaged
    assert redraw > 0
    print('ALL-ON HOLD zero; same-alphabet REDRAW positive PASS')

    # At Q=14112, three on-seam preparations force the k=2 line no-go.
    def yline(t):
        return [1, 1+t, 1-t]
    coeff = [F(-20, 1681), F(1680, 1681), F(21, 1681)]
    curve = lambda t: [a*b for a in yline(t) for b in yline(t)]
    target = curve(1)
    got = [sum(c*curve(t)[i] for c, t in zip(coeff, [-41, 0, 41]))
           for i in range(9)]
    assert got == target
    for t in [-41, 0, 41]:
        z = [1+t, 0, 0, 0, 1-t, 0, 0, 0]
        assert q(z) <= 14112 and dot(ELL, z) % 41 == 0
    print('k=2 DARKNESS OBSTRUCTION: exact line interpolation PASS')

    for Q in (16, 13456, 14112, 1000000, 100000000):
        assert lower_bound(Q) <= 2*m_bound(Q)+1
        print('BLOCK BOUNDS', Q, lower_bound(Q), 2*m_bound(Q)+1)
    b = beta(14112)
    assert 0 < b < 1
    print('BETA_14112 numerator_bits', b.numerator.bit_length(),
          'denominator_bits', b.denominator.bit_length())
    print('ALL FROZEN FINITE CHECKS PASS')


if __name__ == '__main__':
    main()
