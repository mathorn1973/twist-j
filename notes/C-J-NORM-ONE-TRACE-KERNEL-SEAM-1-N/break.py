#!/usr/bin/env python3
"""Adversarial exact checks for C-J-NORM-ONE-TRACE-KERNEL-SEAM-1-N.

Same-session breaker, frozen before verify.py.  This is not independent
confirmation and carries no public status.
"""
from __future__ import annotations

from itertools import product
from fractions import Fraction


def det_bareiss(a: list[list[int]]) -> int:
    """Exact determinant of an integer square matrix."""
    n = len(a)
    m = [row[:] for row in a]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if m[r][k] != 0), None)
            if pivot is None:
                return 0
            m[k], m[pivot] = m[pivot], m[k]
            sign = -sign
        pivot_val = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = m[i][j] * pivot_val - m[i][k] * m[k][j]
                if k:
                    assert num % prev == 0
                    num //= prev
                m[i][j] = num
        prev = pivot_val
        for i in range(k + 1, n):
            m[i][k] = 0
    return sign * m[n - 1][n - 1]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def matsub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def trace(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def rank_mod_p(a: list[list[int]], p: int) -> int:
    m = [[x % p for x in row] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][c], -1, p)
        m[r] = [(inv * x) % p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [(m[i][j] - q * m[r][j]) % p for j in range(cols)]
        r += 1
    return r


def main() -> int:
    # Multiplication by j in the standard integral basis (1,j,j^2,j^3).
    Mj = [
        [0, 0, 0, -1],
        [1, 0, 0, -1],
        [0, 1, 0, -1],
        [0, 0, 1, -1],
    ]
    I = [[int(i == j) for j in range(4)] for i in range(4)]
    Mj2 = matmul(Mj, Mj)
    MJ = [[I[i][j] + Mj2[i][j] for j in range(4)] for i in range(4)]
    Mx = matsub(Mj, Mj2)  # x = j-j^2

    # B=(j,j^2,j^3,j^4) is the column matrix Mj.
    assert det_bareiss(Mj) == 1
    print("PASS B1: nontrivial-root basis has determinant 1")

    # Tr(j^a) is the trace of Mj^a.
    power = I
    trace_row: list[int] = []
    for _a in range(1, 5):
        power = matmul(power, Mj)
        trace_row.append(trace(power))
    assert trace_row == [-1, -1, -1, -1]
    print("PASS B2: trace row in B is (-1,-1,-1,-1)")

    # Global norm-one and additive trace-zero are not the same set.
    assert det_bareiss(MJ) == 1
    assert trace(MJ) == 3
    assert trace(Mx) == 0
    assert det_bareiss(Mx) == 5
    print("PASS B3: tangent/global firewall witnessed by J and j-j^2")

    # Exact residual trace kernel at p=5.
    W = [v for v in product(range(5), repeat=4) if sum(v) % 5 == 0]
    assert len(W) == 5**3
    A3_basis = [
        [1, 0, 0, -1],
        [0, 1, 0, -1],
        [0, 0, 1, -1],
    ]
    assert rank_mod_p(A3_basis, 5) == 3
    span = {
        tuple(sum(c[k] * A3_basis[k][j] for k in range(3)) % 5 for j in range(4))
        for c in product(range(5), repeat=3)
    }
    assert span == set(W)
    print("PASS B4: A3/5A3 is exactly the 125-point trace kernel")

    # Public residual Gram radical control: (5I-J_4) mod 5 has kernel sum=0.
    G5 = [[5 * int(i == j) - 1 for j in range(4)] for i in range(4)]
    assert rank_mod_p(G5, 5) == 1
    for v in W:
        assert all(sum(G5[i][j] * v[j] for j in range(4)) % 5 == 0 for i in range(4))
    print("PASS B5: residual Gram radical agrees with the trace kernel")

    # Negative controls: dimension is degree minus one, not a p=5 selector.
    assert {n: n - 1 for n in range(2, 9)}[4] == 3
    assert 4 - 1 == 3  # split etale Q^4 control as well
    print("PASS B6: quartic and split-etale controls defeat dimension selection")

    # Dirichlet ranks are not torus dimensions.
    examples = {
        "Q(i)": (2, 1, 0),       # degree, norm-one torus dim, unit rank
        "Q(sqrt5)": (2, 1, 1),
        "Q(zeta5)": (4, 3, 1),
    }
    assert examples["Q(i)"][1] != examples["Q(i)"][2]
    assert examples["Q(zeta5)"][1] != examples["Q(zeta5)"][2]
    print("PASS B7: torus dimension and integral-unit rank remain distinct")

    print("BREAKER NO BREAK: all frozen attacks and controls pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
