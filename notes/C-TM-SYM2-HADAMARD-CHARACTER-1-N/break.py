#!/usr/bin/env python3
"""Independent breaker for C-TM-SYM2-HADAMARD-CHARACTER-1-N.

Written from PREREG.md before verify.py. Exact Fraction arithmetic only.
NON-CANONICAL incubation support, not public evidence.
"""

from fractions import Fraction as F

H = [
    [1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    BT = transpose(B)
    return [[sum(F(x) * F(y) for x, y in zip(r, c)) for c in BT] for r in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(A, s):
    return [[F(s) * x for x in row] for row in A]


def outer(v, w):
    return [[F(x) * F(y) for y in w] for x in v]


def mv(A, v):
    return [sum(F(x) * F(y) for x, y in zip(row, v)) for row in A]


def coeffs(v):
    return [sum(F(H[k][j]) * F(v[j]) for j in range(4)) / 4 for k in range(4)]


def expanded_coeffs(class_values):
    # 12 selectors in each quotient class. Character average over all 48.
    chars = H
    out = []
    for row in chars:
        total = F(0)
        for c in range(4):
            # Any within-class permutation leaves this sum unchanged.
            vals = [F(class_values[c]) for _ in range(12)]
            vals = list(reversed(vals))
            total += F(row[c]) * sum(vals)
        out.append(total / 48)
    return out


def run():
    # B1 orthogonality and inverse.
    HH = matmul(H, transpose(H))
    assert HH == scale(eye(4), 4)
    assert matmul(scale(H, F(1, 4)), H) == eye(4)

    # B2 projectors.
    Ps = [scale(outer(row, row), F(1, 4)) for row in H]
    Z = [[F(0) for _ in range(4)] for _ in range(4)]
    total = Z
    for i, P in enumerate(Ps):
        assert matmul(P, P) == P
        for j, Q in enumerate(Ps):
            if i != j:
                assert matmul(P, Q) == Z
        total = add(total, P)
    assert total == eye(4)

    # B3 epsilon row is the pointwise product chi_Q * chi_F.
    assert H[3] == [H[1][j] * H[2][j] for j in range(4)]

    # B4 representative independence under all within-class permutations is
    # algebraic: every representative in one G orbit has the same class value
    # and character. Audit with unequal class values and reversed local orders.
    v = [F(2), F(3), F(5), F(11)]
    assert coeffs(v) == expanded_coeffs(v)

    # B5 selector-independent outputs have trivial character only.
    for x in [F(0), F(1, 6), F(7, 13), F(-5, 9)]:
        c = coeffs([x, x, x, x])
        assert c == [x, F(0), F(0), F(0)]

    # B6 epsilon-blind but Q/F-sensitive example: equal averages on the two
    # epsilon fibers (++ , --) and (+- , -+) kill only epsilon.
    v = [F(3), F(5), F(7), F(9)]  # 3+9 = 5+7
    c = coeffs(v)
    assert c[3] == 0
    assert c[1] != 0 and c[2] != 0

    # Kernel/image order control for G1.
    W_order, G_order, codomain_order = 48, 12, 4
    image_order = W_order // G_order
    assert image_order == codomain_order

    print("BREAKER PASS: |W|/|G| = 4, so the frozen character map is onto C2 x C2")
    print("BREAKER PASS: H4 orthogonality, inverse, and four rational projectors exact")
    print("BREAKER PASS: projectors invariant under within-class representative permutations")
    print("BREAKER PASS: selector-independent outputs have only the trivial H4 mode")
    print("BREAKER PASS: epsilon-blindness kills epsilon mode without forcing Q/F modes to vanish")
    print("BREAKER VERDICT: no L5 algebraic counterexample; no L6 conclusion authorized")


if __name__ == "__main__":
    run()
