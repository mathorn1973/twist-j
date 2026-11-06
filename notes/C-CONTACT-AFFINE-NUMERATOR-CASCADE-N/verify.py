#!/usr/bin/env python3
"""Exact frozen audit of a direct affine contact source, not a table compiler."""
import hashlib
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
UNIT_J = (1, 0, 1, 0)
U = (1, 0, -1, 0)
J_INV = (0, -1, -1, 0)
DEPTH = 12
WORD = ((0, 1), (0, 2)) + tuple((0, i) for i in range(3, 16))
PRIOR_VALUES = (ZERO, ONE, (0, 1, 0, 0), U, UNIT_J)
CACHE = {}
PAIRS = []
APPLICATIONS = 0


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k*x for x in a)


def multiply(a, b):
    coefficients = [0]*7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            coefficients[i+k] += x*y
    for degree in range(6, 3, -1):
        value = coefficients[degree]
        for position in range(degree-4, degree):
            coefficients[position] -= value
    return tuple(coefficients[:4])


def power(a, exponent):
    result = ONE
    for _ in range(exponent):
        result = multiply(result, a)
    return result


def rho_mul(a):
    # Direct marked-j-basis matrix, independently checked against multiplication.
    b = (-a[3], a[0]-a[3], a[1]-a[3], a[2]-a[3])
    return (-b[3], b[0]-b[3], b[1]-b[3], b[2]-b[3])


def account(a):
    numerator = 5*sum(x*x for x in a)-sum(a)**2
    assert numerator % 2 == 0
    return numerator//2


def contact(a, b):
    key = (a, b)
    if key in CACHE:
        return CACHE[key]
    difference = add(a, scale(b, -1))
    if any(x % 2 for x in difference):
        output = (a, b)
    else:
        s = tuple((x+y)//2 for x, y in zip(a, b))
        t = tuple(x//2 for x in difference)
        rt = rho_mul(t)
        output = (add(s, rt), add(s, scale(rt, -1)))
    c, d = output
    assert add(a, b) == add(c, d)
    assert account(a)+account(b) == account(c)+account(d)
    assert sum(a) % 5 == sum(c) % 5
    assert sum(b) % 5 == sum(d) % 5
    CACHE[key] = output
    PAIRS.append(key)
    return output


def word(state, inverse=False):
    global APPLICATIONS
    state = list(state)
    prefix = []
    for position, (a, b) in enumerate(reversed(WORD) if inverse else WORD):
        for _ in range(4 if inverse else 1):
            state[a], state[b] = contact(state[a], state[b])
            APPLICATIONS += 1
        if not inverse and position < 2:
            prefix.append(tuple(state))
    return tuple(state), prefix


def prepare(q, n, prior=()):
    a = scale(U, 2*(q-1)*n)
    b = scale(add(scale(U, q-1), scale(ONE, 2)), 2*n)
    return (a, b, scale(UNIT_J, 2)) + (ZERO,)*13 + tuple(prior)


def sum_state(state):
    return tuple(sum(z[i] for z in state) for i in range(4))


def scalar_pair(q, n):
    number = q*n+1
    depth = 0
    while number % 2 == 0:
        depth += 1
        number //= 2
    return number, depth


def read_current(state):
    # Reads only active slot0 and cascade slots3..15. No original source access.
    ports = state[3:16]
    depth = 0
    while depth < len(ports) and ports[depth] != ZERO:
        depth += 1
    if depth == len(ports):
        return 'DEPTH_LIMIT'
    assert all(z == ZERO for z in ports[depth:])
    normalized = multiply(power(J_INV, depth+1), state[0])
    number = normalized[0]
    assert normalized == (number, 0, -number, 0)
    return number, depth


def audit(q, n, prior=(), positive=True):
    initial = prepare(q, n, prior)
    expected_account = (40*q*(q-1)+32)*n*n+12+sum(account(z) for z in prior)
    expected_sum = add(scale(add(scale(ONE, q), scale(RHO, -(q-1))), 4*n), scale(UNIT_J, 2))
    for value in prior:
        expected_sum = add(expected_sum, value)
    assert sum(account(z) for z in initial) == expected_account
    assert sum_state(initial) == expected_sum
    final, prefix = word(initial)
    assert prefix[0][0] == scale(U, 2*q*n)
    b = scale(add(scale(ONE, q), scale(RHO, -(q-2))), 2*n)
    assert prefix[0][1] == b
    assert prefix[1][0] == scale(multiply(U, UNIT_J), q*n+1)
    c = add(scale(multiply(U, U), q*n), multiply(UNIT_J, UNIT_J))
    assert prefix[1][2] == c
    assert final[1] == b and final[2] == c
    assert final[16:] == tuple(prior)
    assert sum(account(z) for z in final) == expected_account
    assert sum_state(final) == expected_sum
    assert tuple(sum(z) % 5 for z in initial) == tuple(sum(z) % 5 for z in final)
    m, v = scalar_pair(q, n)
    if positive:
        assert v <= DEPTH
        assert read_current(final) == (m, v)
        assert final[0] == scale(multiply(U, power(UNIT_J, v+1)), m)
        for s in range(1, DEPTH+2):
            if s <= v:
                numerator = scale(multiply(multiply(U, U), power(UNIT_J, s)), q*n+1)
                assert all(value % (1 << s) == 0 for value in numerator)
                expected = tuple(value//(1 << s) for value in numerator)
                assert expected != ZERO
            else:
                expected = ZERO
            assert final[2+s] == expected
        numerator = (1 << v)*m-1
        assert numerator % q == 0 and numerator//q == n
    else:
        assert q == 3 and n == 5461 and v == 14
        assert all(z != ZERO for z in final[3:16])
        assert all(coefficient % 2 == 0 for coefficient in final[0])
        assert read_current(final) == 'DEPTH_LIMIT'
    restored, _ = word(final, inverse=True)
    assert restored == initial
    return final, m, v


def main():
    assert multiply(UNIT_J, J_INV) == ONE
    assert account(U) == 5 and account(UNIT_J) == 3
    for z in (ONE, RHO, U, UNIT_J, J_INV):
        assert multiply(RHO, z) == rho_mul(z)
    boundaries = []
    counts = {}
    for n in range(1, 4096, 2):
        final, m, v = audit(3, n)
        boundaries.append([n, final])
        counts[v] = counts.get(v, 0)+1
    assert set(counts) == set(range(1, 13))
    print('PASS q=3: 2048 exact source/synthesis/cascade/read/inverse cases')
    for q in range(1, 10):
        for n in range(1, 128, 2):
            audit(q, n)
    print('PASS q=1..9: 576 supplied-gain cases, including depth zero')
    for n in (1, 3, 5, 7, 15, 27, 85, 1365, 4095):
        for first in PRIOR_VALUES:
            for second in PRIOR_VALUES:
                audit(3, n, (first, second))
    print('PASS 225 literal occupied-archive extensions and complete inverses')
    audit(3, 5461, positive=False)
    print('PASS outside-depth witness n=5461: DEPTH_LIMIT; native inverse retained')
    # Audit each discovered pair; the growing queue closes all five-cycles.
    index = 0
    while index < len(PAIRS):
        pair = PAIRS[index]
        output = pair
        for _ in range(5):
            output = contact(*output)
        assert output == pair
        index += 1
    edge_hash = hashlib.sha256(''.join(f'{a},{b}\n' for a, b in WORD).encode()).hexdigest()
    boundary_hash = hashlib.sha256(json.dumps(boundaries, separators=(',', ':')).encode()).hexdigest()
    print(f'WORD contacts={len(WORD)} core_slots=16 sha256={edge_hash}')
    print(f'BOUNDARY q=3 sha256={boundary_hash}')
    print('DEPTH_COUNTS '+json.dumps(sorted(counts.items()), separators=(',', ':')))
    print(f'COUNTS forward_cases=2850 native_inverses=2850 primitive_word_applications={APPLICATIONS} distinct_pair_inputs={len(CACHE)}')
    print('PASS C-CONTACT-AFFINE-NUMERATOR-CASCADE-N; selected coherent source, no reload claim')


if __name__ == '__main__':
    main()
