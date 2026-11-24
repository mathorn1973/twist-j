#!/usr/bin/env python3
"""Exact audit for C-PHOTON-SIGNED-CONTACT-XI-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
"""

from __future__ import annotations

from fractions import Fraction


Point = tuple[int, int, int]
EdgeKey = tuple[Point, int]

STEPS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
POSITIVE_STEPS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(p: Point, s: Point) -> Point:
    return p[0] + s[0], p[1] + s[1], p[2] + s[2]


def primitive_constants():
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

    print(
        "CONSTANTS PASS "
        f"a={a} r={r} s={s} tau={tau} q0={q0} A={A} q={q}"
    )
    return a, r, s, tau, A, q


def canonical_cycle(vertices: tuple[Point, ...]) -> tuple[Point, ...]:
    n = len(vertices)
    candidates = []
    for seq in (vertices, tuple(reversed(vertices))):
        for k in range(n):
            rot = seq[k:] + seq[:k]
            ox, oy, oz = rot[0]
            norm = tuple((x - ox, y - oy, z - oz) for x, y, z in rot)
            candidates.append(norm)
    return min(candidates)


def enumerate_cycles(max_len: int = 12) -> dict[int, set[tuple[Point, ...]]]:
    out = {m: set() for m in range(4, max_len + 1, 2)}
    origin = (0, 0, 0)

    for m in out:
        def dfs(path: list[Point]) -> None:
            current = path[-1]
            used = len(path) - 1
            remaining = m - used
            dist = abs(current[0]) + abs(current[1]) + abs(current[2])

            if dist > remaining or (remaining - dist) % 2:
                return

            if used == m:
                if current == origin:
                    vertices = tuple(path[:-1])
                    if len(set(vertices)) == m:
                        out[m].add(canonical_cycle(vertices))
                return

            step_set = POSITIVE_STEPS if used == 0 else STEPS
            for step in step_set:
                nxt = add(current, step)
                if nxt == origin:
                    if used + 1 != m:
                        continue
                elif nxt in path:
                    continue
                path.append(nxt)
                dfs(path)
                path.pop()

        dfs([origin])

    return out


def cycle_edges(vertices: tuple[Point, ...]) -> dict[EdgeKey, int]:
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

    # boundary p_ab(x)
    # = + e_b(x+e_a) - e_b(x) - e_a(x+e_b) + e_a(x)
    return {
        (add(base, ea), b): 1,
        (base, b): -1,
        (add(base, eb), a): -1,
        (base, a): 1,
    }


def opposite_contact_counts(vertices: tuple[Point, ...]) -> tuple[int, int]:
    edges = cycle_edges(vertices)
    items = list(edges.items())
    op = om = 0

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
            assert signed1 in (-1, 1) and signed2 in (-1, 1)

            if signed1 == signed2:
                op += 1
            else:
                om += 1

    return op, om


def in_signed_class(m: int, op: int, om: int, r: Fraction, s: Fraction, tau: Fraction) -> bool:
    return (r**op) * (s**om) <= tau**m


def census_audit(r: Fraction, s: Fraction, tau: Fraction) -> None:
    cycles = enumerate_cycles(12)
    total = 0
    signed_class = 0
    old_class = 0
    strict = []
    by_len = []

    for m in sorted(cycles):
        count = sc_count = old_count = 0
        contact_hist: dict[tuple[int, int], int] = {}

        for cyc in cycles[m]:
            op, om = opposite_contact_counts(cyc)
            O = op + om
            sc = in_signed_class(m, op, om, r, s, tau)
            old = 12 * O <= m

            if old:
                assert sc

            if sc:
                sc_count += 1
                signed_class += 1
            if old:
                old_count += 1
                old_class += 1
            if sc and not old and len(strict) < 5:
                strict.append((m, op, om, cyc))

            contact_hist[op, om] = contact_hist.get((op, om), 0) + 1
            count += 1
            total += 1

        by_len.append((m, count, old_count, sc_count, len(contact_hist)))

    assert total > 0
    print(
        "CENSUS PASS "
        f"total={total} old={old_class} signed={signed_class} "
        + " ".join(
            f"m{m}={n}/old{o}/sc{scc}/types{t}"
            for m, n, o, scc, t in by_len
        )
    )

    if strict:
        m, op, om, cyc = strict[0]
        print(
            "STRICT_EXTENSION FOUND "
            f"m={m} Oplus={op} Ominus={om} vertices={cyc}"
        )
    else:
        print("STRICT_EXTENSION NONE_IN_FROZEN_CENSUS")


def S3(q: Fraction) -> Fraction:
    return (1 + 4 * q + q * q) / (1 - q) ** 4 - 1 - 8 * q - 27 * q * q


def bound_audit(A: Fraction, q: Fraction) -> None:
    C12 = A * S3(q) / 64
    expected = Fraction(
        19289287085600601415245438839426542724609375,
        48127709445264405068802290089074432,
    )
    assert C12 == expected
    print(f"BOUND PASS C_SC={C12}")


def main() -> None:
    _, r, s, tau, A, q = primitive_constants()
    census_audit(r, s, tau)
    bound_audit(A, q)
    print("AUDIT PASS; signed_contact_extension=YES; full_Xi=OPEN; P1=OPEN")


if __name__ == "__main__":
    main()
