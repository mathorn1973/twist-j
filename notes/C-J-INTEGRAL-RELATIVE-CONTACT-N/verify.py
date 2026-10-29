#!/usr/bin/env python3
"""Frozen supplementary integer audit, not a public P-probe.

A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
All universal assertions are proved separately in PROOF.md.
"""
from itertools import product

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(k, a):
    return tuple(k * x for x in a)


def canonical(five):
    return tuple(five[k] - five[4] for k in range(4))


def jp(k):
    c = [0] * 5
    c[k % 5] = 1
    return canonical(c)


def mul(a, b):
    c = [0] * 5
    for i in range(4):
        for k in range(4):
            c[(i + k) % 5] += a[i] * b[k]
    return canonical(c)


def conj(a):
    c = [0] * 5
    for i in range(4):
        c[(-i) % 5] += a[i]
    return canonical(c)


def q(a):
    twice = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert twice % 2 == 0
    return twice // 2


def q_trace(a):
    b = mul(a, conj(a))
    tr = 4 * b[0] - sum(b[1:])
    assert tr % 2 == 0
    return tr // 2


RHO = jp(2)
J = add(ONE, RHO)


def admitted(pair):
    return all((x - y) % 2 == 0 for x, y in zip(*pair))


def half(a):
    assert all(x % 2 == 0 for x in a)
    return tuple(x // 2 for x in a)


def contact(pair, power=1):
    x, y = pair
    if not admitted(pair):
        return pair
    s, t = half(add(x, y)), half(sub(x, y))
    rt = mul(jp(2 * power), t)
    return add(s, rt), sub(s, rt)


def matrix_numerators(pair):
    x, y = pair
    a, b = add(ONE, RHO), sub(ONE, RHO)
    return add(mul(a, x), mul(b, y)), add(mul(b, x), mul(a, y))


def energy(state):
    return sum(q(x) for x in state)


def total(state):
    s = ZERO
    for x in state:
        s = add(s, x)
    return s


def reduction(pair, modulus):
    return tuple(tuple(x % modulus for x in a) for a in pair)


def ramified(pair):
    return tuple(sum(a) % 5 for a in pair)


def triple(state):
    a, b = contact(state[:2])
    b, c = contact((b, state[2]))
    return a, b, c


def triple_inverse(state):
    b, c = contact(state[1:], -1)
    a, b = contact((state[0], b), -1)
    return a, b, c


def reverse_order(state):
    b, c = contact(state[1:])
    a, b = contact((state[0], b))
    return a, b, c


def main():
    assert mul(J, neg(add(jp(1), jp(2)))) == ONE
    assert mul(mul(RHO, RHO), RHO) == jp(1)
    assert mul(RHO, conj(RHO)) == ONE
    roots = tuple(scale(sign, jp(r)) for sign in (-1, 1) for r in range(5))
    assert len(set(roots)) == 10
    minimal = set()
    scalar_count = 0
    for a in product(range(-2, 3), repeat=4):
        scalar_count += 1
        assert q(a) == q_trace(a)
        assert 2 * q(a) >= sum(x * x for x in a)
        if a != ZERO:
            assert q(a) >= 2
        if q(a) == 2:
            minimal.add(a)
    assert scalar_count == 625 and minimal == set(roots)
    print('PASS 1 scalar trace/minimum regression: 625 states; 10 minimum roots')

    sample = (ZERO,) + tuple(scale(s, jp(r)) for s in (-1, 1) for r in range(4))
    maps = sum_preserving = checks = 0
    for swap in (False, True):
        for u, v in product(roots, repeat=2):
            maps += 1
            is_sum = True
            for x, y in product(sample, repeat=2):
                pair = (y, x) if swap else (x, y)
                image = mul(u, pair[0]), mul(v, pair[1])
                assert energy(image) == energy((x, y))
                is_sum = is_sum and total(image) == total((x, y))
                checks += 1
            assert is_sum == (u == ONE and v == ONE)
            sum_preserving += int(is_sum)
    assert (maps, sum_preserving, checks) == (200, 2, 16200)
    print('PASS 2 classified monomial family regression: 200 maps; 16200 cases; 2 sum maps')

    parity_count = parity_accept = composition_count = 0
    parity_scalars = tuple(product((0, 1), repeat=4))
    for pair in product(parity_scalars, repeat=2):
        parity_count += 1
        parity_accept += int(admitted(pair))
        nums = matrix_numerators(pair)
        integral = all(c % 2 == 0 for a in nums for c in a)
        assert integral == admitted(pair)
        for r, s in product(range(5), repeat=2):
            assert contact(contact(pair, r), s) == contact(pair, r + s)
            composition_count += 1
    assert (parity_count, parity_accept, composition_count) == (256, 16, 6400)
    print('PASS 3 exact admission: 256 parity pairs; 16 admitted; 6400 composition cases')

    states = tuple(product((-1, 0, 1), repeat=4))
    count = accepted = 0
    for pair in product(states, repeat=2):
        count += 1
        x, y = pair
        image = contact(pair)
        assert contact(image, -1) == pair
        assert contact(contact(pair, -1)) == pair
        assert admitted(image) == admitted(pair)
        assert total(image) == total(pair)
        assert energy(image) == energy(pair)
        assert ramified(image) == ramified(pair)
        assert contact((y, x)) == (image[1], image[0])
        shifted = add(x, jp(1)), add(y, jp(1))
        assert contact(shifted) == (add(image[0], jp(1)), add(image[1], jp(1)))
        assert contact((mul(J, x), mul(J, y))) == tuple(mul(J, a) for a in image)
        cur = pair
        for _ in range(5):
            cur = contact(cur)
        assert cur == pair
        nums = matrix_numerators(pair)
        if admitted(pair):
            accepted += 1
            assert image == tuple(half(a) for a in nums)
            assert sub(image[0], image[1]) == mul(RHO, sub(x, y))
        else:
            assert image == pair
            assert any(c % 2 for a in nums for c in a)
    assert (count, accepted, count - accepted) == (6561, 625, 5936)
    print('PASS 4 complete coefficient box: 6561 pairs; 625 accepted; 5936 refused')

    cur, idle = (scale(2, ONE), ZERO), (ZERO, ZERO)
    for n in range(100):
        assert cur == (add(ONE, jp(2 * n)), sub(ONE, jp(2 * n)))
        assert idle == (ZERO, ZERO)
        assert tuple(q(a) for a in cur) == ((8, 0) if n % 5 == 0 else (3, 5))
        if n % 5 == 0:
            assert cur[1] == idle[1]
            assert contact(cur)[1] != contact(idle)[1]
        cur, idle = contact(cur), contact(idle)
    print('PASS 5 fixed-source continuing orbit: 100 cuts; exact return and repeated sensitivity')

    for modulus in range(2, 32):
        if modulus % 2 == 0:
            a, b = (ZERO, ZERO), (scale(modulus, ONE), ZERO)
        else:
            a, b = (scale(2, ONE), ZERO), (scale(modulus + 2, ONE), ZERO)
        assert reduction(a, modulus) == reduction(b, modulus)
        assert reduction(contact(a), modulus) != reduction(contact(b), modulus)
    print('PASS 6 finite-reduction witnesses: all 30 integer moduli 2..31')

    alphabet = (ZERO,) + roots
    count3 = 0
    for state in product(alphabet, repeat=3):
        count3 += 1
        image = triple(state)
        assert triple_inverse(image) == state
        assert triple(triple_inverse(state)) == state
        assert energy(image) == energy(state)
        assert total(image) == total(state)
    assert count3 == 1331
    seed = (scale(4, ONE), ZERO, ZERO)
    expected = (scale(2, J), sub(ONE, jp(4)), mul(sub(ONE, RHO), sub(ONE, RHO)))
    assert triple(seed) == expected
    assert tuple(q(a) for a in expected) == (12, 5, 15)
    assert reverse_order(seed) == (scale(2, J), scale(2, sub(ONE, RHO)), ZERO)
    assert tuple(q(a) for a in reverse_order(seed)) == (12, 20, 0)
    print('PASS 7 three slots: 1331 states; two-edge transfer (12,5,15); order control (12,20,0)')

    fixtures = ((4, 0, 0), (0, 4, 0), (0, 0, 4), (2, 2, 0), (2, 0, 2), (0, 2, 2))
    visits = 0
    for fixture in fixtures:
        state = tuple(scale(x, ONE) for x in fixture)
        e, s = energy(state), total(state)
        for _ in range(100):
            image = triple(state)
            assert triple_inverse(image) == state
            assert energy(image) == e and total(image) == s
            state = image
            visits += 1
    assert visits == 600
    print('PASS 8 occupied continuations: 6 fixed preparations, 600 full steps')

    assert contact((ONE, ZERO)) == (ONE, ZERO)
    assert contact((scale(2, ONE), ZERO)) != (scale(2, ONE), ZERO)
    assert any(c % 2 for a in matrix_numerators((ONE, ZERO)) for c in a)
    bare_j_step = (add(ONE, J), sub(ONE, J))
    assert energy(bare_j_step) == 10 != 8
    assert q(J) == 3 != q(ONE)
    assert triple(seed) != reverse_order(seed)
    print('PASS 9 negative controls: additivity, illegal division, bare-J cost and edge-order change')
    print('RESULT 9/9 PASS; supplementary finite audit; no independent or canonical acceptance')


if __name__ == '__main__':
    main()
