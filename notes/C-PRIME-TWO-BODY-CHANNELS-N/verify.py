#!/usr/bin/env python3
"""Prospective exact note audit; no public promotion or physical claim."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from math import gcd, isqrt, lcm


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c + b*d, a*d + b*c + b*d


def bar(x):
    return x[0] + x[1], -x[1]


def norm(x):
    a, b = x
    return a*a + a*b - b*b


def trace(x):
    return 2*x[0] + x[1]


def div(x, y):
    d = norm(y)
    if d == 0:
        raise ZeroDivisionError('zero field denominator')
    p = mul(x, bar(y))
    return Q(p[0])/Q(d), Q(p[1])/Q(d)


def future(x):
    return trace(x) > 0 and norm(x) > 0


def integral(x):
    return all(Q(t).denominator == 1 for t in x)


def denominator(x):
    return lcm(*(Q(t).denominator for t in x))


def reflect(z, x):
    return div(mul(z, bar(x)), bar(z))


def field_candidates(z, r, s):
    if not future(z) or r <= 0 or s <= 0:
        raise ValueError('positive total and positive integer norms required')
    T = norm(z)
    D = T + r - s
    delta = D*D - 4*T*r
    if not (0 < D < 2*T) or delta < 0 or delta % 5:
        return set()
    u = isqrt(delta // 5)
    if 5*u*u != delta or (D-u) % 2:
        return set()
    return {div(((D-b)//2, b), bar(z)) for b in {-u, u}}


def channels(z, r, s):
    ans = set()
    for x in field_candidates(z, r, s):
        if integral(x):
            v = tuple(int(a) for a in x)
            assert future(v) and future(sub(z, v))
            assert norm(v) == r and norm(sub(z, v)) == s
            ans.add(v)
    return ans


def enumerate_outputs(z):
    A, _ = z
    out = defaultdict(set)
    for a in range(1, A):
        for b in range(-2*a+1, 2*a):
            x = (a, b)
            y = sub(z, x)
            if future(x) and future(y):
                out[(norm(x), norm(y))].add(x)
    return out


def nearest(x):
    return (2*x.numerator + x.denominator) // (2*x.denominator)


def ring_gcd(x, y):
    while y != (0, 0):
        qr = div(x, y)
        q = tuple(nearest(t) for t in qr)
        rem = sub(x, mul(q, y))
        assert rem == (0, 0) or abs(norm(rem)) < abs(norm(y))
        x, y = y, rem
    return x


@lru_cache(maxsize=None)
def factor(n):
    if n < 1:
        raise ValueError('positive integer required')
    ans = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            ans.append((p, e))
        p += 1
    if n > 1:
        ans.append((n, 1))
    return tuple(ans)


@lru_cache(maxsize=None)
def roots(p):
    return tuple(t for t in range(p) if (t*t-t-1) % p == 0)


def root_valuation(x, p, root, bound):
    modulus = p
    value = 0
    for k in range(1, bound+1):
        assert (root*root-root-1) % modulus == 0
        if (x[0] + x[1]*root) % modulus:
            break
        value = k
        if k < bound:
            quotient = (root*root-root-1) // modulus
            shift = (-quotient * pow((2*root-1) % p, -1, p)) % p
            root += shift*modulus
            modulus *= p
    return value


@lru_cache(maxsize=None)
def split_values(x, p):
    rr = roots(p)
    assert len(rr) == 2
    bound = dict(factor(abs(norm(x)))).get(p, 0)
    vals = tuple(root_valuation(x, p, t, bound) for t in rr)
    assert sum(vals) == bound
    return vals


def expected_denominator(x, z):
    d = 1
    for p, _ in factor(norm(z)):
        if p % 5 in (1, 4):
            a, b = split_values(z, p)
            c, e = split_values(x, p)
            d *= p ** max(0, b-a-e, a-b-c)
        else:
            assert len(roots(p)) != 2
    return d


def total_imbalance(z):
    d = 1
    for p, _ in factor(norm(z)):
        if p % 5 in (1, 4):
            a, b = split_values(z, p)
            d *= p ** abs(a-b)
    return d


def collision(x, y):
    z = add(x, y)
    rx = reflect(z, x)
    if integral(rx):
        rx = tuple(int(a) for a in rx)
        return rx, sub(z, rx)
    return x, y


def main():
    box = [(a, b) for a in range(1, 9) for b in range(-8, 9)
           if future((a, b))]
    # G1 includes every absent channel in its exact finite norm rectangle.
    digest = sha256()
    tested = admitted = states = 0
    histogram = [0, 0, 0]
    for z in box:
        brute = enumerate_outputs(z)
        T = norm(z)
        assert all(0 < r < T and 0 < s < T for r, s in brute)
        for r in range(1, T):
            for s in range(1, T):
                got = channels(z, r, s)
                want = brute.get((r, s), set())
                assert got == want, ('channel mismatch', z, r, s, got, want)
                assert len(got) <= 2
                tested += 1
                admitted += bool(got)
                states += len(got)
                histogram[len(got)] += 1
                tail = ';'.join(f'{a},{b}' for a, b in sorted(got))
                digest.update(f'{z[0]},{z[1]}|{r},{s}|{tail}\n'.encode('ascii'))
    print(f'G1 PASS totals={len(box)} norm_pairs={tested} admitted={admitted} states={states}')
    print('CHANNEL_CARDINALITIES ' + ','.join(map(str, histogram)))
    print('CHANNEL_LEDGER_SHA256 ' + digest.hexdigest())
    pairs = primitive = integral_reflections = distinct_reflections = 0
    for x in box:
        for y in box:
            z = add(x, y)
            rx, ry = reflect(z, x), reflect(z, y)
            assert future(rx) and future(ry)
            assert add(rx, ry) == z
            assert norm(rx) == norm(x) and norm(ry) == norm(y)
            assert reflect(z, rx) == x and reflect(z, ry) == y
            assert integral(rx) == integral(ry)
            d = denominator(rx)
            assert denominator(ry) == d and norm(z) % d == 0
            assert d == expected_denominator(x, z), ('prime denominator', x, y)
            assert all(p % 5 in (1, 4) for p, _ in factor(d))
            dt = denominator(div(z, bar(z)))
            assert dt == total_imbalance(z)
            is_primitive = abs(norm(ring_gcd(x, y))) == 1
            if is_primitive:
                primitive += 1
                assert d == dt
                assert integral(rx) == integral(div(z, bar(z)))
            # Direct element gcd audits the denominator IDEAL, not just d.
            g = ring_gcd(bar(z), mul(z, bar(x)))
            ideal_generator = div(bar(z), g)
            assert integral(ideal_generator)
            assert (abs(norm(ideal_generator)) == 1) == integral(rx)
            out = collision(x, y)
            assert collision(*out) == (x, y)
            assert add(*out) == z
            assert norm(out[0]) == norm(x) and norm(out[1]) == norm(y)
            pairs += 1
            integral_reflections += integral(rx)
            distinct_reflections += integral(rx) and rx != x
    print(f'G2 PASS pairs={pairs} primitive={primitive} integral_reflections={integral_reflections} distinct={distinct_reflections}')
    for c in range(1, 65):
        z = (c+1, c)
        T = c*c + 3*c + 1
        rx = reflect(z, (1, 0))
        assert norm(z) == T
        assert rx == (Q(2*c*c+2*c+1, T), Q(3*c*c+2*c, T))
        assert denominator(rx) == T // gcd(T, 5)
        assert integral(rx) == (c == 1)
    assert reflect((2, 1), (1, 0)) == (1, 1)
    assert reflect((3, 2), (1, 0)) == (Q(13, 11), Q(16, 11))
    assert reflect((4, 3), (1, 0)) == (Q(25, 19), Q(33, 19))
    z = (18, 23)
    assert norm(z) == 209 and 29*29-4*209 == 5
    fields = field_candidates(z, 1, 181)
    assert fields == {(Q(13, 11), Q(16, 11)), (Q(25, 19), Q(33, 19))}
    assert channels(z, 1, 181) == set()
    z0 = (15, -1)
    assert norm(z0) == 209 and (1, 0) in channels(z0, 1, 181)
    print('G3 PASS family_c=1..64 denominators_c_1_2_3=1,11,19 blocked_209_channel=0 same_norm_control=allowed')
    witness = ((1, 1), (3, -1))
    assert tuple(map(norm, witness)) == (1, 5)
    assert collision(*witness) == ((2, -1), (2, 1)) != witness
    print(f'G4 PASS total_involution_controls={pairs} unequal_norm_nonuniqueness=1,5')
    print('STATUS NON-CANONICAL candidate-C audit; written proofs candidate-T; no independent review')


if __name__ == '__main__':
    main()
