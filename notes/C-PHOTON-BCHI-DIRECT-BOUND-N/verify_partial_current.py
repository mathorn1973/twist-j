#!/usr/bin/env python3
"""Exact finite audit of the partial-current bridge; NON-CANONICAL.

This is not a simulation, a covariance-tail certificate, or a formal P-probe.
The proof supplies the universal mixed-Haar argument. This audit checks its
projectors, inherited polynomial identity, physical four-cup fixture, and
normalization constants using integers and Fraction only.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import prod


def add(*polys):
    out = defaultdict(F)
    for p in polys:
        for key, value in p.items():
            out[key] += value
    return {k: v for k, v in out.items() if v}


def scale(p, c):
    return {k: v * c for k, v in p.items() if v * c}


def mul(p, q):
    out = defaultdict(F)
    for (a, b), x in p.items():
        for (c, d), y in q.items():
            out[a + c, b + d] += x * y
    return {k: v for k, v in out.items() if v}


def power(p, n):
    out = {(0, 0): F(1)}
    for _ in range(n):
        out = mul(out, p)
    return out


def audit_polynomial():
    one, x, y = {(0, 0): F(1)}, {(1, 0): F(1)}, {(0, 1): F(1)}
    x2, y2 = power(x, 2), power(y, 2)
    a = scale(add(one, x2, y2), 2)
    b = add(scale(x, 2), scale(mul(x, y), 2), y2)
    lhs = add(power(a, 2), scale(power(b, 2), -1),
              scale(one, -4), scale(x2, -4))
    rhs = add(scale(power(add(y, scale(x2, F(-1, 2)),
                              scale(mul(x, y), F(-1, 4))), 2), 8),
              scale(power(x, 4), F(25, 16)),
              mul(power(add(y, scale(x, F(-1, 2))), 2),
                  add(scale(y2, 3), scale(mul(x, y), -1), scale(x2, F(7, 4)))))
    assert lhs == rhs
    assert add(scale(y2, 3), scale(mul(x, y), -1), scale(x2, F(7, 4))) == add(
        scale(power(add(y, scale(x, F(-1, 6))), 2), 3), scale(x2, F(5, 3)))
    print("Inherited four-edge polynomial/SOS identities: PASS")


def boundary(cell, L):
    base, axes = cell
    out = defaultdict(int)
    for i, axis in enumerate(axes):
        face_axes = axes[:i] + axes[i + 1:]
        upper = list(base)
        upper[axis] = (upper[axis] + 1) % L
        sign = (-1) ** i
        out[(tuple(upper), face_axes)] += sign
        out[(base, face_axes)] -= sign
    return {k: v for k, v in out.items() if v}


def kernel_mod5(matrix):
    a = [[v % 5 for v in row] for row in matrix]
    n = len(a[0])
    pivot = []
    row = 0
    for col in range(n):
        pos = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pos is None:
            continue
        a[row], a[pos] = a[pos], a[row]
        inv = pow(a[row][col], -1, 5)
        a[row] = [(v * inv) % 5 for v in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(u - c * v) % 5 for u, v in zip(a[i], a[row])]
        pivot.append(col)
        row += 1
        if row == len(a):
            break
    basis = []
    for col in range(n):
        if col in pivot:
            continue
        v = [0] * n
        v[col] = 1
        for i, pc in enumerate(pivot):
            v[pc] = -a[i][col] % 5
        basis.append(v)
    return len(pivot), basis


def audit_four_cups(L):
    origin = (0, 0, 0, 0)
    p = (origin, (0, 1))
    cups = []
    for axis in (2, 3):
        for side in (-1, 1):
            base = list(origin)
            if side < 0:
                base[axis] = L - 1
            b = boundary((tuple(base), (0, 1, axis)), L)
            assert abs(b[p]) == 1
            cups.append({face: value * b[p] for face, value in b.items()})
    faces = sorted(set().union(*(c.keys() for c in cups)))
    assert len(faces) == 21
    bounds = [boundary(face, L) for face in faces]
    edges = sorted(set().union(*(b.keys() for b in bounds)))
    matrix = [[b.get(e, 0) for b in bounds] for e in edges]
    rank, basis = kernel_mod5(matrix)
    assert rank == 17 and len(basis) == 4
    target = boundary(p, L)
    weights = defaultdict(F)
    count = 0
    for coeff in product(range(5), repeat=4):
        residues = [sum(coeff[k] * basis[k][i] for k in range(4)) % 5
                    for i in range(21)]
        if any(v not in (0, 1, 4) for v in residues):
            continue
        n = [-1 if v == 4 else v for v in residues]
        d = [sum(a * v for a, v in zip(row, n)) for row in matrix]
        assert all(v % 5 == 0 for v in d)
        j = {e: v // 5 for e, v in zip(edges, d) if v}
        charge = next((s for s in (-1, 0, 1)
                       if j == {e: s * v for e, v in target.items() if s * v}), None)
        assert charge is not None
        weights[charge] += F(1, 2 ** sum(v != 0 for v in n))
        count += 1
    assert count == 53
    assert weights[0] == F(596163, 524288)
    assert weights[-1] == weights[1] == F(1, 2097152)
    probability = (weights[-1] + weights[1]) / sum(weights.values())
    assert probability == F(1, 1192327)
    assert weights[1] <= weights[0] / 16
    print(f"Four-cup zero-exterior fixture L={L}: faces=21 rank={rank} "
          f"states={count} Q0={weights[0]} Qplus={weights[1]} Pcircle={probability}: PASS")


def audit_projectors():
    for charge in range(-6, 7):
        # Haar integration extracts one exact frequency; the Z5 average
        # extracts every frequency divisible by five. Six plaquettes meet
        # a lattice edge, so these are all possible incidence sums.
        exact = [int(charge == 5 * a) for a in (-1, 0, 1)]
        assert sum(exact) == int(charge % 5 == 0)
    print("Mixed Haar/Z5 edge-projector partition for incidence -6..6: PASS")


def audit_normalization():
    for k in range(1, 9):
        signs = list(product((-1, 1), repeat=k))
        q0 = F(16 ** k)
        event = F(len(signs), q0 + len(signs))
        assert event == F(1, 1 + 8 ** k)
        # These are extremizers of the relaxed mass inequalities only.
        # They are not asserted to occur in the lattice measure.
        if k % 2 == 0:
            positive = sum(prod(s) == 1 for s in signs)
            signed = F(positive, q0 + positive)
            assert signed == F(1, 1 + 2 * 8 ** k)
            assert all(prod(tuple(-v for v in s)) == prod(s) for s in signs)
    q0, qpp, qpm = F(256), F(1), F(0)
    z = q0 + 2 * qpp + 2 * qpm
    assert 2 * (qpp - qpm) / z == F(1, 129)
    assert 2 * F(1) / (F(16) + 2) == F(1, 9)
    print("Normalized circulation bounds: one=1/9, pair=1/65, signed_pair=1/129: PASS")
    print("Abstract two-pattern covariance can remain 1/129 with no distance parameter: PASS")


def main():
    print("C-PHOTON-BCHI-DIRECT-BOUND-N partial-current audit (NON-CANONICAL)")
    audit_projectors()
    audit_polynomial()
    for L in (4, 6):
        audit_four_cups(L)
    audit_normalization()
    print("RESULT PASS")


if __name__ == "__main__":
    main()
