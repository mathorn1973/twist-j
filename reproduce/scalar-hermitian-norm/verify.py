#!/usr/bin/env python3
"""Exact exploratory audit. No network, writes, or public-probe semantics."""

from itertools import product
from math import gcd, isqrt
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")


def mul(a, b):
    """Multiply in Z[X]/(1+X+X^2+X^3+X^4), degree < 4 basis."""
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    for i in range(6, 3, -1):
        value = c[i]
        for k in range(4):
            c[i - 4 + k] -= value
    return tuple(c[:4])


def conjugate(x):
    a, b, c, d = x
    return a - b, -b, d - b, c - b


def hermitian(x):
    h = mul(x, conjugate(x))
    assert h[1] == 0 and h[2] == h[3]
    return h[0], -h[2]


def direct_forms(x):
    a, b, c, d = x
    return (a*a - a*b + b*b - b*c + c*c - c*d + d*d,
            a*b - a*c - a*d + b*c - b*d + c*d)


def factor(n):
    assert n >= 1
    answer = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            answer[p] = answer.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        answer[n] = answer.get(n, 0) + 1
    return answer


def is_scalar_norm(u, v):
    """The proved integral norm theorem, expressed with N and gcd(u,v)."""
    if (u, v) == (0, 0):
        return True
    trace = 2*u + v
    absolute = u*u + u*v - v*v
    if trace <= 0 or absolute <= 0:
        return False
    common = factor(gcd(abs(u), abs(v)))
    for p, exponent in factor(absolute).items():
        residue = p % 5
        if residue in (2, 3) and exponent % 4:
            return False
        if residue == 4 and (exponent % 2 or common.get(p, 0) % 2):
            return False
    return True


def pair_is_realized(s, t):
    if (s, t) == (0, 0):
        return True
    if (s+t) % 5:
        return False
    return is_scalar_norm((s+t)//5, (3*s-2*t)//5)


def small_polynomial_product(a, b, modulus):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[i+k] = (out[i+k] + x*y) % modulus
    return out


def main():
    j = (0, 1, 0, 0)
    phi = (0, 0, -1, -1)
    J = (1, 0, 1, 0)
    assert mul(J, phi) == j
    assert hermitian(J) == (2, -1)
    assert hermitian((1, -1, 0, 0)) == (3, -1)
    assert mul(phi, phi) == (1, 0, -1, -1)
    print('PASS ring: J*phi=j; H(J)=2-phi; H(1-j)=3-phi')

    witnesses = {
        4: (2, 0, 0, 0),
        124: (-6, 6, 2, 6),
        844: (-18, 12, 12, -8),
    }
    for target, vector in witnesses.items():
        assert hermitian(vector) == (target, 0)
    print('PASS witnesses: scalar norms 4,124,844')

    squares19 = {a*a % 19 for a in range(19)}
    assert 2 not in squares19 and 12 not in squares19
    assert small_polynomial_product([1, 5, 1], [1, 15, 1], 19) == [1]*5
    assert all(5779 % d for d in range(2, isqrt(5779)+1))
    assert 5779 % 5 == 4
    print('PASS prime obstructions: reciprocal irreducible factors at19; 5779 prime=4 mod5')

    G = [[5*int(i == k)-1 for k in range(4)] for i in range(4)]
    inverse_times_five = [[int(i == k)+1 for k in range(4)] for i in range(4)]
    assert [[sum(G[i][k]*inverse_times_five[k][l] for k in range(4))
             for l in range(4)] for i in range(4)] == [
                 [5*int(i == l) for l in range(4)] for i in range(4)]

    trace_bound = 40
    coefficient_bound = isqrt(4*trace_bound//5)
    assert coefficient_bound == 5
    observed = set()
    residues = set()
    norm19_hits = 0
    checked = 0
    for vector in product(range(-5, 6), repeat=4):
        checked += 1
        u, v = hermitian(vector)
        assert (u, v) == direct_forms(vector)
        s, t = 2*u+v, 3*u-v
        uj, vj = hermitian(mul(J, vector))
        assert (uj, vj) == (2*u-v, v-u)
        assert t == 2*uj+vj
        assert (s+t, 3*s-2*t) == (5*u, 5*v)
        assert 3*s*t-s*s-t*t == 5*(u*u+u*v-v*v)
        assert 2*s == 5*sum(c*c for c in vector)-sum(vector)**2
        assert (u+3*v) % 5 == sum(vector)**2 % 5
        assert pair_is_realized(s, t)
        residues.add((s % 5, t % 5))
        if (u, v) == (19, 0):
            norm19_hits += 1
        if 0 < s <= trace_bound:
            observed.add((s, t))
    assert checked == 14641 and norm19_hits == 0
    assert residues == {(0, 0), (2, 3), (3, 2)}
    print('PASS complete norm19 box: 14641 integer vectors; 0 witnesses')
    print('PASS exact two-trace, norm, Gram, residue and J-transition identities: 14641 vectors')

    # If h is positive with trace s, t=S(J*alpha) is between phi^-2*s
    # and phi^2*s, hence 0<t<3s. The coefficient bound above covers
    # EVERY possible scalar for s<=40, independently of the norm test.
    predicted = {(s, t) for s in range(1, trace_bound+1)
                 for t in range(1, 3*s) if pair_is_realized(s, t)}
    assert predicted == observed
    assert pair_is_realized(0, 0)
    assert not pair_is_realized(38, 57)  # h=19, N=361, odd gcd valuation
    print(f'PASS exact trace-image theorem vs complete trace<=40 census: {len(observed)} pairs')

    L = [2, 3]
    while len(L) <= 12:
        L.append(3*L[-1]-L[-2])
    assert [L[n]+1 for n in (1, 3, 5, 7, 9)] == [4, 19, 124, 844, 5779]
    for n, value in enumerate(L):
        assert value % 5 == 2*((-1)**n) % 5
        assert not is_scalar_norm(value, 0)
        if n % 2 == 0:
            assert not is_scalar_norm(value+1, 0)
    assert [is_scalar_norm(L[n]+1, 0) for n in (1, 3, 5, 7, 9)] == [True, False, True, True, False]
    print('PASS sequence examples: Q1 yes,Q3 no,Q5 yes,Q7 yes,Q9 no; residues n=0..12')

    allowed = {tuple(sorted(x)) for x in product((0, 1, 4), repeat=3)
               if all((x[i]+x[k]) % 5 in (0, 1, 4)
                      for i in range(3) for k in range(i+1, 3))}
    assert allowed == {(0, 0, 0), (0, 0, 1), (0, 0, 4), (0, 1, 4)}
    print('PASS three-carrier residue classification: four unordered patterns')
    print('EXPLORATORY AUDIT PASS; analytical proofs and physical scope remain separate')


if __name__ == '__main__':
    main()
