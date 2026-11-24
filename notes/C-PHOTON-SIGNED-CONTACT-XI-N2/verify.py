#!/usr/bin/env python3
"""Exact audit for C-PHOTON-SIGNED-CONTACT-XI-N2.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
"""

from __future__ import annotations

from fractions import Fraction


Point = tuple[int, int, int]
EdgeKey = tuple[Point, int]

WITNESS: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 1, 1),
    (0, 1, 0),
    (1, 1, 0),
    (1, 1, -1),
    (0, 1, -1),
    (0, 0, -1),
)


def add(p: Point, s: Point) -> Point:
    return p[0] + s[0], p[1] + s[1], p[2] + s[2]


def constants():
    a = Fraction(15625, 177147)
    r = Fraction(41, 25)
    s = Fraction(9, 25)
    tau = Fraction(73, 70)
    q0 = a * (1 + 6 * r)
    A = 2 * r * a * tau
    q = q0 * tau

    assert q0 == Fraction(169375, 177147)
    assert A == Fraction(374125, 1240029)
    assert q == Fraction(2472875, 2480058)
    assert s < r
    assert tau**12 > r
    assert q < 1

    # Exact cleared integer witnesses.
    assert 9 * 25 < 41 * 25
    assert 73**12 * 25 > 41 * 70**12
    assert 2472875 < 2480058

    print(
        "CONSTANTS PASS "
        f"a={a} r={r} s={s} tau={tau} q0={q0} A={A} q={q}"
    )
    return a, r, s, tau, A, q


def cycle_edges(vertices: tuple[Point, ...]) -> dict[EdgeKey, int]:
    assert len(vertices) == len(set(vertices))
    edges: dict[EdgeKey, int] = {}
    n = len(vertices)

    for k, p in enumerate(vertices):
        q = vertices[(k + 1) % n]
        diff = tuple(q[i] - p[i] for i in range(3))
        axes = [i for i, d in enumerate(diff) if d]
        assert len(axes) == 1
        axis = axes[0]
        assert abs(diff[axis]) == 1

        if diff[axis] == 1:
            key = (p, axis)
            coeff = 1
        else:
            key = (q, axis)
            coeff = -1

        assert key not in edges
        edges[key] = coeff

    assert len(edges) == n
    return edges


def plaquette_boundary(base: Point, a: int, b: int) -> dict[EdgeKey, int]:
    assert a < b
    ea = tuple(1 if i == a else 0 for i in range(3))
    eb = tuple(1 if i == b else 0 for i in range(3))

    return {
        (add(base, ea), b): 1,
        (base, b): -1,
        (add(base, eb), a): -1,
        (base, a): 1,
    }


def contact_counts(vertices: tuple[Point, ...]) -> tuple[int, int, tuple]:
    edges = cycle_edges(vertices)
    items = list(edges.items())
    Oplus = Ominus = 0
    details = []

    for i in range(len(items)):
        (base1, axis1), coeff1 = items[i]
        for j in range(i + 1, len(items)):
            (base2, axis2), coeff2 = items[j]
            if axis1 != axis2:
                continue

            diff = tuple(base2[k] - base1[k] for k in range(3))
            nz = [k for k, d in enumerate(diff) if d]
            if len(nz) != 1:
                continue

            transverse = nz[0]
            if transverse == axis1 or abs(diff[transverse]) != 1:
                continue

            low = base1 if diff[transverse] == 1 else base2
            a, b = sorted((axis1, transverse))
            boundary = plaquette_boundary(low, a, b)
            key1 = (base1, axis1)
            key2 = (base2, axis1)
            assert key1 in boundary and key2 in boundary

            signed1 = coeff1 * boundary[key1]
            signed2 = coeff2 * boundary[key2]
            assert signed1 in (-1, 1)
            assert signed2 in (-1, 1)

            kind = "+" if signed1 == signed2 else "-"
            if kind == "+":
                Oplus += 1
            else:
                Ominus += 1
            details.append((key1, coeff1, key2, coeff2, (low, a, b), kind))

    return Oplus, Ominus, tuple(details)


def witness_audit(r: Fraction, s: Fraction, tau: Fraction) -> None:
    vertices = WITNESS
    assert len(vertices) == 10
    assert len(set(vertices)) == 10

    edges = cycle_edges(vertices)
    assert len(edges) == 10

    # Closure in each coordinate.
    net = [0, 0, 0]
    for (_, axis), coeff in edges.items():
        net[axis] += coeff
    assert net == [0, 0, 0]

    Oplus, Ominus, details = contact_counts(vertices)
    assert Oplus == 2
    assert Ominus == 1
    O = Oplus + Ominus
    assert O == 3
    assert 12 * O > len(vertices)

    signed_factor = (r**Oplus) * (s**Ominus)
    assert signed_factor == Fraction(15129, 15625)
    assert signed_factor < 1
    assert 1 < tau ** len(vertices)
    assert signed_factor < tau ** len(vertices)

    print(
        "WITNESS PASS "
        f"m={len(vertices)} Oplus={Oplus} Ominus={Ominus} O={O} "
        f"signed_factor={signed_factor} tau_power={tau**len(vertices)}"
    )
    for index, item in enumerate(details, 1):
        print(f"CONTACT_{index} {item}")


def implication_audit(r: Fraction, s: Fraction, tau: Fraction) -> None:
    # The theorem is symbolic:
    # s<r, 12O<=m => r^Oplus s^Ominus <= r^O <= r^(m/12) < tau^m.
    # Audit exact integer cases over a broad finite grid for mutation control.
    checked = 0
    for m in range(4, 241):
        for op in range(0, m + 1):
            for om in range(0, m + 1 - op):
                O = op + om
                if 12 * O <= m:
                    assert (r**op) * (s**om) <= tau**m
                    checked += 1
    assert checked > 0
    print(f"IMPLICATION_AUDIT PASS finite_cases={checked}")


def S3(q: Fraction) -> Fraction:
    return (1 + 4 * q + q * q) / (1 - q) ** 4 - 1 - 8 * q - 27 * q * q


def bound_audit(A: Fraction, q: Fraction) -> None:
    C = A * S3(q) / 64
    expected = Fraction(
        19289287085600601415245438839426542724609375,
        48127709445264405068802290089074432,
    )
    assert C == expected
    print(f"BOUND PASS C_SC={C}")


def main() -> None:
    _, r, s, tau, A, q = constants()
    implication_audit(r, s, tau)
    witness_audit(r, s, tau)
    bound_audit(A, q)
    print("AUDIT PASS; signed_contact_class=STRICT_EXTENSION; full_Xi=OPEN; P1=OPEN")


if __name__ == "__main__":
    main()
