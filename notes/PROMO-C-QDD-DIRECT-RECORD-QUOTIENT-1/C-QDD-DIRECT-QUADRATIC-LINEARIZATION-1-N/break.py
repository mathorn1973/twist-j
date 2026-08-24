#!/usr/bin/env python3
"""Independent breaker for C-QDD-DIRECT-QUADRATIC-LINEARIZATION-1-N.

Uses only integer symmetric-coordinate rows. It does not import verify.py.
It attacks uniqueness and records the expected nonlinear-extension failure.
"""

from fractions import Fraction as F
from itertools import product

PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))
L = (-2, -1, 0, 1, 2)


def row(v):
    return tuple(F(v[i] * v[j]) for i, j in PAIRS)


def rref_rank(rows):
    a = [list(r) for r in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    rows = [row(v) for v in product(L, repeat=4)]
    rank = rref_rank(rows)
    nullity = 10 - rank
    assert rank == 10 and nullity == 0

    # Fibre attack: q(v)=q(w) must be exactly w=+-v on this rational grid.
    fibres = {}
    for v in product(L, repeat=4):
        fibres.setdefault(row(v), []).append(v)
    assert len(fibres) == 313
    bad = []
    for xs in fibres.values():
        if len(xs) == 1:
            if xs[0] != (0, 0, 0, 0):
                bad.append(xs)
        elif len(xs) == 2:
            if tuple(-x for x in xs[0]) != xs[1] and tuple(-x for x in xs[1]) != xs[0]:
                bad.append(xs)
        else:
            bad.append(xs)
    assert not bad

    # Expected scope breaker. The cubic p(A_00)=A_00(A_00-1)(A_00-4)
    # vanishes on every q(v), because A_00=v_0^2 in {0,1,4}, but not at A_00=2.
    vals = {v[0] * v[0] for v in product(L, repeat=4)}
    assert vals == {0, 1, 4}
    def p(x):
        return x * (x - 1) * (x - 4)
    assert all(p(x) == 0 for x in vals)
    assert p(2) == -4

    # Density-only scale breaker: e_1 and 2e_1 give the same rank-one normalized
    # projector but different total weights. The full tagged record must retain m.
    assert row((1, 0, 0, 0)) != row((2, 0, 0, 0))

    print("C-QDD-DIRECT-QUADRATIC-LINEARIZATION-1-N BREAKER")
    print(f"LINEAR_PERTURBATION_NULLITY {nullity} PASS")
    print("Q_FIBRES exactly_sign_or_zero PASS")
    print("NONLINEAR_EXTENSION_UNIQUENESS FIRED expected cubic=A00(A00-1)(A00-4)")
    print("DENSITY_ONLY_SCALE_UNIQUENESS FIRED expected")
    print("VERDICT candidate survives only at frozen rational-linear full-record scope")


if __name__ == "__main__":
    main()
