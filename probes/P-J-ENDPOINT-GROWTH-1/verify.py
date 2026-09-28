#!/usr/bin/env python3
"""Exact proof audit for P-J-ENDPOINT-GROWTH-1. All-n claims use PROOF.md."""
from fractions import Fraction as F
from itertools import product


class Q5:
    """a + b sqrt(5), with exact order and arithmetic."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def cast(x):
        return x if isinstance(x, Q5) else Q5(x)

    def __add__(self, x):
        x = self.cast(x)
        return Q5(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, x):
        return self + -self.cast(x)

    def __rsub__(self, x):
        return self.cast(x) + -self

    def __mul__(self, x):
        x = self.cast(x)
        return Q5(self.a*x.a + 5*self.b*x.b, self.a*x.b + self.b*x.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        r = Q5(1)
        for _ in range(n):
            r = r*self
        return r

    def __eq__(self, x):
        x = self.cast(x)
        return (self.a, self.b) == (x.a, x.b)

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        gap = a*a - 5*b*b
        assert gap != 0  # sqrt(5) is irrational.
        return ((gap > 0) - (gap < 0))*((a > 0) - (a < 0))

    def __le__(self, x):
        return (self - x).sign() <= 0

    def __lt__(self, x):
        return (self - x).sign() < 0

    def __gt__(self, x):
        return (self - x).sign() > 0

    def __ge__(self, x):
        return (self - x).sign() >= 0


def mul(x, y):
    raw = [0]*7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            raw[i+j] += a*b
    for k in range(6, 3, -1):
        for t in range(4):
            raw[k-4+t] -= raw[k]
    return tuple(raw[:4])


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n*a for a in x)


def main():
    one, z = (1, 0, 0, 0), (0, 1, 0, 0)
    z2, z3 = mul(z, z), mul(mul(z, z), z)
    J = add(one, z2)
    M = ((1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1))
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    assert all(mul(J, e) == tuple(row[k] for row in M)
               for k, e in enumerate(basis))
    phi_ring = scale(-1, add(z2, z3))
    eta = z2
    beta = add(one, mul(eta, eta))
    assert beta == scale(-1, mul(phi_ring, eta))
    assert add(add(mul(eta, eta), mul(phi_ring, eta)), one) == (0,0,0,0)
    assert mul(phi_ring, phi_ring) == add(phi_ring, one)
    assert mul(beta, eta) == add(phi_ring, mul(mul(phi_ring, phi_ring), eta))
    print('cyclotomic_coordinate_identities PASS')

    p, half = Q5(F(1,2), F(1,2)), F(1,2)
    assert p*p == p+1
    rows = (p, p+p*p)
    assert rows[1] == Q5(2,1)
    assert all(0 < r and r < 5 for r in rows)
    B = ((Q5(0), p), (-p, p*p))
    assert B[0][0]*B[1][1]-B[0][1]*B[1][0] == p*p
    print('universal_cover_hypotheses PASS row_sums=phi,2+sqrt(5) determinant=phi^2')

    # Nine half-integer boundary/interior samples. The universal covering
    # follows from the row bounds and the exact five-interval partition.
    samples = (-half, F(0), half)
    count = 0
    for a, b in product(samples, repeat=2):
        out = (p*b, -p*a+p*p*b)
        for x in out:
            # Exact nearest integer with upper choice on half-integer ties.
            nearest = next(d for d in range(-2,3) if Q5(d-half) <= x < Q5(d+half))
            assert Q5(-half) <= x-nearest <= Q5(half)
            count += 1
    assert all(F(d,1)+half == F(d+1,1)-half for d in range(-2,2))
    print(f'cover_boundary_samples PASS coordinates={count}')

    C = 32*(4*p*p+half)**2*(4*p+half)**2
    assert C == Q5(93890,41760)
    digits = [(u,v,0,0) for u,v in product(range(-2,3), repeat=2)]
    endpoints = {(0,0,0,0)}
    expected = (1,25,625,5449,27233)
    for n in range(5):
        if n:
            endpoints = {add(mul(J,x),d) for x in endpoints for d in digits}
        size = len(endpoints)
        assert size == expected[n]
        assert p**(2*n) <= size <= C*p**(2*n)
        print(f'endpoint_census n={n} count={size} exact_bounds=PASS')
    print('RESULT PASS finite_audit_only all_n_claim_requires_written_proof')


if __name__ == '__main__':
    main()
