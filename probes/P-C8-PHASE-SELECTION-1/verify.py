#!/usr/bin/env python3
"""Exact verifier for P-C8-PHASE-SELECTION-1.

Finite-field elements are pairs (a,b) representing a + b*tau in
F_25 = F_5[tau]/(tau^2-2). Phase representations are odd exponents mod 8.
"""

from itertools import product

P = 5


def add(x, y):
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def mul(x, y):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def power(x, n):
    out = (1, 0)
    base = x
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def order(x):
    assert x != (0, 0)
    y = (1, 0)
    for n in range(1, 25):
        y = mul(y, x)
        if y == (1, 0):
            return n
    raise AssertionError(("order not found", x))


def frob(x):
    return power(x, 5)


def B(k):
    return (5 * k) % 8


def O(k):
    return (-k) % 8


def BO(k):
    return B(O(k))


def main():
    elems = list(product(range(P), repeat=2))
    tau = (0, 1)
    minus_tau = (0, 4)
    j = (2, 0)
    j_inv = (3, 0)

    # G1: exact root pair and Frobenius.
    roots = sorted(x for x in elems if mul(x, x) == j)
    assert roots == [tau, minus_tau], roots
    assert order(tau) == 8
    assert order(minus_tau) == 8
    for a in range(P):
        assert frob((a, 0)) == (a, 0)
    assert frob(j) == j
    assert frob(tau) == minus_tau == power(tau, 5)
    assert frob(minus_tau) == tau
    assert all(frob(r) != r for r in roots)
    print("G1 PASS: R={tau,-tau}; Frobenius fixes F5 and J_lambda and swaps both roots")

    # G2: four representation labels and Klein-four torsor.
    E = (1, 3, 5, 7)
    assert tuple(k for k in range(8) if len({(k * n) % 8 for n in range(8)}) == 8) == E
    for k in E:
        assert B(B(k)) == k
        assert O(O(k)) == k
        assert B(O(k)) == O(B(k))
        assert B(k) == (k + 4) % 8

        orbit = {k, B(k), O(k), BO(k)}
        assert orbit == set(E), (k, orbit)

        # Freeness: no nonidentity Klein element fixes k.
        assert B(k) != k
        assert O(k) != k
        assert BO(k) != k
    print("G2 PASS: B:k->5k and O:k->-k generate a free transitive Klein-four action")

    # G3: finite hypotheses of the natural-selector no-go.
    # The intrinsic datum is Frobenius-fixed as a set, but has no fixed root.
    assert {frob(r) for r in roots} == set(roots)
    assert not [r for r in roots if frob(r) == r]
    for k in E:
        assert B(k) != k
    print("G3 PASS: Frobenius-fixed source datum has no fixed root or fixed phase representation")

    # G4: the sign-branch symmetry does NOT kill the C4 orientation.
    assert mul(power(tau, 3), power(tau, 3)) == j_inv
    assert mul(power(tau, 7), power(tau, 7)) == j_inv
    assert j_inv != j

    plus_orientation = {k for k in E if (2 * k) % 8 == 2}
    minus_orientation = {k for k in E if (2 * k) % 8 == 6}
    assert plus_orientation == {1, 5}
    assert minus_orientation == {3, 7}
    assert {B(k) for k in plus_orientation} == plus_orientation
    assert {B(k) for k in minus_orientation} == minus_orientation
    assert {O(k) for k in plus_orientation} == minus_orientation
    assert {O(k) for k in minus_orientation} == plus_orientation
    print("G4 PASS: Frobenius preserves C4 orientation; target conjugation exchanges S and S^-1")

    # G5: no fixed k under the full declared symmetry.
    fixed_all = [k for k in E if B(k) == k and O(k) == k]
    assert fixed_all == []
    print("G5 PASS: with both binary choices unselected, no symmetry-fixed k exists")

    print("VERDICT PASS: sign-branch relative no-go; C4 orientation remains a separate open selection debt")


if __name__ == "__main__":
    main()
