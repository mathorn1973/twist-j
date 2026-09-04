#!/usr/bin/env python3
"""Exact p=5 centering-image audit. RESULT-EXPOSED; L1 only."""

from itertools import permutations


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    if not a or not b or any(len(row) != len(b) for row in a):
        raise ValueError("incompatible matrix dimensions")
    width = len(b[0])
    if any(len(row) != width for row in b):
        raise ValueError("ragged matrix")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(width)] for i in range(len(a))]


def scale(a, scalar):
    return [[scalar * value for value in row] for row in a]


def determinant(a):
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("determinant requires a nonempty square matrix")
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        term = -1 if inversions % 2 else 1
        for i in range(n):
            term *= a[i][perm[i]]
        total += term
    return total


def main():
    i5, i4 = identity(5), identity(4)
    ones = [[1] for _ in range(5)]
    zero_column = [[0] for _ in range(5)]
    d = [[5 * i5[i][j] - 1 for j in range(5)] for i in range(5)]
    f = [[int(i == j) - int(i == 4) for j in range(4)]
         for i in range(5)]
    g = [[int(i == (j + 1) % 5) for j in range(5)] for i in range(5)]
    g2 = multiply(g, g)
    j_operator = [[i5[i][j] + g2[i][j] for j in range(5)]
                  for i in range(5)]

    b_image = [row[:4] for row in d]
    m_image = [row[:] for row in b_image[:4]]
    d_f = multiply(d, f)
    r_restriction = [row[:] for row in d_f[:4]]
    u_smith = [[1, 1, 1, 1], [1, 2, 1, 1],
               [1, 1, 2, 1], [1, 1, 1, 2]]
    v_smith = [[1, -1, -1, -1], [0, 1, 0, 0],
               [0, 0, 1, 0], [0, 0, 0, 1]]
    smith_values = (1, 5, 5, 5)
    smith = [[smith_values[i] * i4[i][j] for j in range(4)]
             for i in range(4)]

    g_powers = [i5]
    for _ in range(5):
        g_powers.append(multiply(g_powers[-1], g))

    gates = []
    gates.append(("G01", "CARRIER", (
        f[:4] == i4
        and all(sum(f[i][j] for i in range(5)) == 0 for j in range(4))
        and g_powers[5] == i5
        and all(g_powers[k] != i5 for k in range(1, 5))
        and multiply(g, ones) == ones
    )))
    gates.append(("G02", "KERNEL_IMAGE_PREMISES", (
        multiply(d, ones) == zero_column
        and all(d[i][k] - d[j][k] == 5 * (int(i == k) - int(j == k))
                for i in range(5) for j in range(5) for k in range(5))
        and all(sum(d[i][j] for i in range(5)) == 0 for j in range(5))
        and all((d[i][j] - d[0][j]) % 5 == 0
                for i in range(5) for j in range(5))
        and d_f == scale(f, 5)
    )))
    gates.append(("G03", "IMAGE_BASIS_INDEX", (
        all(d[i][4] == -sum(b_image[i]) for i in range(5))
        and multiply(f, m_image) == b_image
        and m_image == [[5 * i4[i][j] - 1 for j in range(4)]
                       for i in range(4)]
        and determinant(m_image) == 125
    )))
    gates.append(("G04", "SMITH_COKERNEL", (
        determinant(u_smith) == 1
        and determinant(v_smith) == 1
        and multiply(multiply(u_smith, m_image), v_smith) == smith
        and all(value > 0 for value in smith_values)
        and all(smith_values[k + 1] % smith_values[k] == 0 for k in range(3))
        and determinant(smith) == 125
        and smith_values == (1, 5, 5, 5)
    )))
    gates.append(("G05", "RESTRICTION_DISTINCTION", (
        multiply(f, r_restriction) == d_f
        and r_restriction == scale(i4, 5)
        and determinant(r_restriction) == 625
        and r_restriction != m_image
        and not (determinant(r_restriction) == 125)
    )))
    gates.append(("G06", "CENTERING_COMMUTATION", (
        multiply(d, d) == scale(d, 5)
        and multiply(d, g) == multiply(g, d)
        and multiply(d, j_operator) == multiply(j_operator, d)
    )))

    print("PROBE P-J-PLENUM-CENTERING-INDEX-1")
    print("MODE RESULT-EXPOSED PROOF-FIRST L1")
    for gate_id, name, passed in gates:
        print("CHECK", gate_id, name, "PASS" if passed else "FIRED")
    confirmed = all(passed for _, _, passed in gates)
    print("CLAIM J-CENTERING-IMAGE-INDEX", "CONFIRMED" if confirmed else "FIRED")
    print("TERMINAL", "CONFIRMED" if confirmed else "SCIENTIFIC-FIRED")


if __name__ == "__main__":
    main()
