"""Author-code-blind exact check, derived from the exposed preregistration.

Original code by A. M. Thorn / independent Codex scope-review session.
Apache-2.0. No scientific execution before the public joint pin.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import lcm


def native_generator(x, which):
    a, b, c, d, q, r = x
    answers = (
        (b, a, d, c, q, r),
        (-c, -d, -a, -b, -q, -r),
        (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
        (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
        (2-a, 1-b, 3-c, 4-d, 2-q, 1-r),
    )
    return tuple(t % 5 for t in answers[which])


def quotient(x):
    return (sum(x) % 5, x[4], x[5])


def quotient_generator(t, which):
    z, q, r = t
    table = ((z, q, r), (-z, -q, -r), (2-z, 1-q, -r),
             (2-z, 1-q, 1-r), (3-z, 2-q, 1-r))
    return tuple(u % 5 for u in table[which])


def target(p):
    if p == (0, 0, 0, 0):
        return None
    v = tuple(t if t <= 2 else t-5 for t in p)
    s, n = sum(v), sum(t*t for t in v)
    assert n > 0 and 5*n-s*s > 0
    return F(s*s, 4*(5*n-s*s))


def coefficient_census():
    # Coefficients of (sum_(v=-2)^2 X^v Y^(v*v))^4.
    # This never constructs a four-source tuple or sorts source labels.
    coefficients = Counter({(0, 0): 1})
    for _ in range(4):
        following = Counter()
        for (s, n), count in coefficients.items():
            for v in range(-2, 3):
                following[s+v, n+v*v] += count
        coefficients = following
    assert sum(coefficients.values()) == 625
    assert coefficients[0, 0] == 1
    result = Counter()
    for (s, n), count in coefficients.items():
        if n:
            result[F(s*s, 4*(5*n-s*s))] += count
    return result


def interval_optimum(weights, bins):
    # Complete 1D minimax interval partition, returning diameter not radius.
    # Any five-center cover can be assigned in nearest-center order, so its
    # blocks may be taken contiguous. Every possible cut is considered.
    previous = [None] * (len(weights)+1)
    previous[0] = F(0)
    for used in range(1, bins+1):
        current = [None] * (len(weights)+1)
        for end in range(used, len(weights)+1):
            candidates = [max(previous[start], weights[end-1]-weights[start])
                          for start in range(used-1, end)
                          if previous[start] is not None]
            current[end] = min(candidates)
        previous = current
    return previous[-1]


def check():
    # Exact commuting identity on the entire finite native checkpoint domain.
    # Infinite history and arbitrary common-seed processing still use induction.
    for x in product(range(5), repeat=6):
        t = quotient(x)
        for g in range(5):
            assert quotient(native_generator(x, g)) == quotient_generator(t, g)
        for bit in (0, 1):
            g = (t[0] + 2*bit) % 5
            assert quotient(native_generator(x, g)) == quotient_generator(t, g)

    points = list(product(range(5), repeat=4))
    zero = (0, 0, 0, 0)
    assert target(zero) is None
    beta = {p: target(p) for p in points if p != zero}
    expected_pairs = (
        ('0',84), ('1/256',24), ('1/176',48), ('1/136',32),
        ('1/96',24), ('1/56',48), ('1/46',36), ('1/26',48),
        ('9/224',24), ('1/16',56), ('9/104',24), ('2/17',24),
        ('9/64',24), ('5/32',8), ('1/6',24), ('2/7',24),
        ('5/16',24), ('3/8',16), ('5/8',8), ('9/14',12),
        ('49/64',8), ('1',4),
    )
    expected = Counter({F(w): n for w, n in expected_pairs})
    assert Counter(beta.values()) == coefficient_census() == expected
    assert len(beta) == sum(expected.values()) == 624 and len(expected) == 22
    assert sum(count for w, count in expected.items() if w > F(5,32)) == 120

    obstruction = ((1,4,0,0),(1,0,0,0),(1,1,0,0),
                   (1,1,1,0),(2,1,1,2),(1,1,1,1))
    assert [beta[p] for p in obstruction] == list(map(F,
            ('0','1/16','1/6','3/8','9/14','1')))
    packed = [tuple(map(int, p)) for p in
              ('0014','0012','0112','1112','1222','1111')]
    packing = [beta[p] for p in packed]
    assert packing == list(map(F, ('0','9/64','2/7','5/8','49/64','1')))
    assert min(b-a for a, b in zip(packing, packing[1:])) == F(9,64)
    assert interval_optimum(sorted(expected), 5) == F(9,64)

    intervals = [(F(a), F(b)) for a, b in
                 (('0','1/46'),('1/26','1/6'),('2/7','3/8'),
                  ('5/8','49/64'),('1','1'))]
    centers = [(a+b)/2 for a, b in intervals]
    assert centers == list(map(F, ('1/92','4/39','37/112','89/128','1')))
    assignment = {}
    for p, w in beta.items():
        choices = [i for i,(a,b) in enumerate(intervals) if a <= w <= b]
        assert len(choices) == 1
        assignment[p] = (choices[0], 0, 0, 0)
    assert max(abs(beta[p]-centers[sum(assignment[p]) % 5])
               for p in beta) == F(9,128)
    # All rational response tables admit the explicitly supplied finite seed.
    denominator = lcm(*(c.denominator for c in centers))
    assert all((c*denominator).denominator == 1 for c in centers)

    ready_outputs = []
    for k in range(5):
        x = (k, 0, 0, 0, 0, 1)
        ready_outputs.append(native_generator(x, sum(x) % 5)[4:])
    assert ready_outputs == [(0,4),(1,4),(1,0),(2,0),(0,1)]

    ordered = sorted(beta, key=lambda p: (beta[p], p))
    buckets = [[p for p in points if sum(p) % 5 == k] for k in range(5)]
    assert list(map(len, buckets)) == [125]*5
    # The original beta=1 source belongs to a supported bin of size >=124.
    assert 120 < 124 and F(1)-F(5,32) == F(27,32)
    expected_extremes = [(F(a), F(b)) for a,b in
                         (('0','1/176'),('1/176','1/56'),
                          ('1/56','1/16'),('1/16','5/32'),('5/32','1'))]
    for short_bin in range(5):
        mapping, responses, ends = {}, [], []
        offset = 0
        for k in range(5):
            size = 124 if k == short_bin else 125
            block = ordered[offset:offset+size]
            offset += size
            low, high = beta[block[0]], beta[block[-1]]
            ends.append((low, high))
            responses.append((low+high)/2)
            mapping.update(zip(block, buckets[k][:size]))
        mapping[zero] = buckets[short_bin][-1]
        assert offset == 624 and len(mapping) == len(set(mapping.values())) == 625
        assert max(abs(beta[p]-responses[sum(mapping[p]) % 5])
                   for p in beta) == F(27,64)
        assert sum(sum(mapping[p]) % 5 == short_bin for p in beta) == 124
        assert sum(mapping[zero]) % 5 == short_bin
        denominator = lcm(*(c.denominator for c in responses))
        assert all((c*denominator).denominator == 1 for c in responses)
        if short_bin == 0:
            assert ends == expected_extremes
            assert responses == list(map(F,
                    ('1/352','29/2464','9/224','7/64','37/64')))

    return ('INDEPENDENT_BREAKER_A PASS sources=624 weights=22 high=120 '
            'free=9/128 faithful=27/64')


if __name__ == '__main__':
    print(check())
