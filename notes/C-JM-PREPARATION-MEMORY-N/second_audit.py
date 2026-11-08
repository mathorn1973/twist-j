#!/usr/bin/env python3
"""Result-exposed second scalar/polynomial audit; no import of verify.py."""
from fractions import Fraction as R
from math import isqrt


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def evaluate(coeff, x):
    out = 0
    for a in reversed(coeff):
        out = out*x+a
    return out


def main():
    p = lambda t: R(1, 1+8*t*t)
    weights = R(354161, 735212), R(381051, 735212)
    assert sum(weights) == 1
    mean = sum(w*p(t) for w, t in zip(weights, [40, 42]))
    assert mean == p(41)
    gap = sum(w*p(t)**2 for w, t in zip(weights, [40, 42]))-mean**2
    assert gap == (p(40)-p(41))*(p(41)-p(42))
    assert gap == R(15936, 1210262180216419) > 0
    probability = lambda t: (2*p(t)-1)**2/2
    assert sum(w*probability(t) for w, t in zip(weights, [40, 42]))-probability(41) == 2*gap
    # The even and odd normalized-support blocks have eigenvalues +2gap,-2gap.
    assert R(2)*gap == R(31872, 1210262180216419)
    print('SECOND AUDIT: scalar first/second moments and optimal effect PASS')

    left = [1, 10, 18, 16]
    right = [-1, -27, -32, -3]
    C = (sum(x*x for x in left)+sum(left)**2)/R(5)+sum(x*x for x in right)/R(4)
    assert C == R(19639, 20)
    for Q in range(8, 20001):
        m = isqrt((C.numerator*Q)//(C.denominator*1681))
        assert (41*m)**2 <= C*Q < (41*(m+1))**2
        n = isqrt((Q-8)//13448)
        assert 8+13448*n*n <= Q < 8+13448*(n+1)**2
        assert 2*n+1 <= 2*m+1
    print('SECOND AUDIT: exact block-bound cuts for Q=8..20000 PASS')

    # Independent coefficient construction rather than source-evaluation products.
    for m in range(0, 6):
        coeff = [1]
        for j in range(-m, m+1):
            coeff = multiply(coeff, [-41*j, 1])
        assert len(coeff)-1 == 2*m+1
        for x in range(-41*(m+1)+1, 41*(m+1)):
            assert (evaluate(coeff, x) == 0) == (x % 41 == 0)
    print('SECOND AUDIT: root-polynomial coefficients and zero set PASS')

    for t in range(-60, 61):
        coeff = [R(t*(t-41), 3362), 1-R(t*t, 1681), R(t*(t+41), 3362)]
        for k in (0, 1, 2):
            assert sum(c*s**k for c, s in zip(coeff, [-41, 0, 41])) == t**k
    print('SECOND AUDIT: entire degree-two line interpolation PASS')

    for a, b in [(41, 40), (41, 42), (-41, 40), (-41, -42)]:
        overlap2 = R((1+8*a*b)**2, (1+8*a*a)*(1+8*b*b))
        assert 0 < overlap2 < 1
        assert overlap2**2 != overlap2
    print('SECOND AUDIT: nonorthogonal-copy and perfect-discrimination controls PASS')
    print('SECOND AUDIT PASS; not blind or additional architecture')


if __name__ == '__main__':
    main()
