#!/usr/bin/env python3
"""Exact public witness for the force and Born dictionary cluster.

The theorem/computed layer is verified with integer and rational arithmetic:

* the finite Weyl commutator on five states;
* the Moore-Penrose Green kernel of the decoder graph C4;
* the Born weights in Z[zeta_5];
* the conjugate readout, Gram, spectrum, MUB, and Plancherel identities.

The associated D rows are dictionary readings of these exact facts.  This
program does not identify the finite C4 kernel with the continuum 1/(4 pi r)
Green law and does not promote a dictionary statement to theorem grade.
"""

import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JGEN = (0, 1, 0, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scal(c, x):
    return tuple(c * a for a in x)


def mul(x, y):
    """Multiply in Z[zeta_5], basis 1,j,j^2,j^3."""
    coeff = [0] * 7
    for i in range(4):
        for k in range(4):
            coeff[i + k] += x[i] * y[k]
    out = coeff[:4]
    # j^4 = -(1+j+j^2+j^3), j^5 = 1, j^6 = j.
    for i in range(4):
        out[i] -= coeff[4]
    out[0] += coeff[5]
    out[1] += coeff[6]
    return tuple(out)


def power(x, n):
    out = ONE
    for _ in range(n):
        out = mul(out, x)
    return out


def sigma(x, k):
    out = ZERO
    for i, coeff in enumerate(x):
        out = add(out, scal(coeff, power(JGEN, (i * k) % 5)))
    return out


def weight(k):
    return mul(add(ONE, power(JGEN, k % 5)),
               add(ONE, power(JGEN, (-k) % 5)))


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    rows = len(left)
    cols = len(right[0])
    middle = len(right)
    return [[sum(left[i][k] * right[k][j] for k in range(middle))
             for j in range(cols)] for i in range(rows)]


def matvec_cyclo(matrix, vector):
    return [sum_cyclo(scal(a, x) for a, x in zip(row, vector))
            for row in matrix]


def sum_cyclo(values):
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def circulant(first_row):
    n = len(first_row)
    return [[first_row[(j - i) % n] for j in range(n)]
            for i in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def shift_matrix(n):
    # (S v)_i = v_(i+1); I+S is convolution by the verb (1,1).
    return [[int(j == (i + 1) % n) for j in range(n)]
            for i in range(n)]


CHECKS = []


def check(name, condition):
    CHECKS.append((name, bool(condition)))


def main():
    # Weyl pair: X e_r = e_(r+1), Z e_r = j^r e_r.
    # A monomial state is (basis index, exponent of j).
    commutator_images = []
    for r in range(5):
        index, phase = r, 0
        index = (index - 1) % 5       # X^-1
        phase = (phase - index) % 5   # Z^-1
        index = (index + 1) % 5       # X
        phase = (phase + index) % 5   # Z
        commutator_images.append((index, phase))
    check("WEYL       Z X Z^-1 X^-1 = j I on all five states",
          commutator_images == [(r, 1) for r in range(5)]
          and power(JGEN, 5) == ONE
          and all(power(JGEN, k) != ONE for k in range(1, 5)))

    # Exact Green pseudoinverse on C4.  H = 16 G avoids fractions.
    laplacian = circulant([2, -1, 0, -1])
    green16 = circulant([5, -1, -3, -1])
    target = [[16 * int(i == j) - 4 for j in range(4)]
              for i in range(4)]
    check("GREEN-C4   L (16 G) = (16 G) L = 16 I - 4 11^T; G 1 = 0",
          matmul(laplacian, green16) == target
          and matmul(green16, laplacian) == target
          and all(sum(row) == 0 for row in green16))

    sqrt5 = add(ONE, scal(2, add(JGEN, power(JGEN, 4))))
    weights = [weight(k) for k in range(5)]
    expected_weights = [
        (4, 0, 0, 0),
        None,
        None,
        None,
        None,
    ]
    expected_weights[1] = expected_weights[4] = scal(
        1, weights[1])
    expected_weights[2] = expected_weights[3] = scal(
        1, weights[2])
    check("BORN       w(0)=4; 2w(1)=3+sqrt5; 2w(2)=3-sqrt5",
          mul(sqrt5, sqrt5) == (5, 0, 0, 0)
          and weights[0] == expected_weights[0]
          and scal(2, weights[1]) == add((3, 0, 0, 0), sqrt5)
          and scal(2, weights[2]) == sub((3, 0, 0, 0), sqrt5)
          and weights[4] == weights[1]
          and weights[3] == weights[2])

    total_weight = sum_cyclo(weights)
    tilt = sub(add(weights[1], weights[4]),
               add(weights[2], weights[3]))
    check("FACE       sum w=10; sigma_2 w(1)=w(2); tilt=2sqrt5",
          total_weight == (10, 0, 0, 0)
          and sigma(weights[1], 2) == weights[2]
          and tilt == scal(2, sqrt5))

    squares_mod5 = {(x * x) % 5 for x in range(1, 5)}
    check("LEGENDRE   (2|5) = -1",
          squares_mod5 == {1, 4} and 2 not in squares_mod5)

    ident5 = identity(5)
    shift = shift_matrix(5)
    read_plus = [[ident5[i][j] + shift[i][j] for j in range(5)]
                 for i in range(5)]
    shift_transpose = transpose(shift)
    read_minus = [[ident5[i][j] + shift_transpose[i][j]
                   for j in range(5)] for i in range(5)]
    gram = matmul(read_plus, read_minus)
    check("READOUT    C_- = C_+^T for the conjugate verb readouts",
          read_minus == transpose(read_plus))
    check("GRAM       C_+ C_+^T = circ(2,1,0,0,1)",
          gram == circulant([2, 1, 0, 0, 1]))

    spectral_ok = True
    for k in range(5):
        vector = [power(JGEN, (k * r) % 5) for r in range(5)]
        left = matvec_cyclo(gram, vector)
        right = [mul(weight(k), entry) for entry in vector]
        spectral_ok = spectral_ok and left == right
    check("SPECTRUM   Gram eigenvalues are w(k), k=0,...,4",
          spectral_ok)

    mub_ok = True
    for r in range(5):
        for k in range(5):
            amplitude = power(JGEN, (r * k) % 5)
            norm_numerator = mul(amplitude, sigma(amplitude, 4))
            # The normalized Fourier entry is amplitude/sqrt(5), so
            # five times its squared modulus is this numerator.
            mub_ok = mub_ok and norm_numerator == ONE
    check("MUB        position/Fourier overlaps have squared modulus 1/5",
          mub_ok)

    coefficient_mass = 1 * 1 + 1 * 1
    check("PLANCHEREL coefficient mass 2; spectral mass 10; ratio 5",
          coefficient_mass == 2
          and total_weight == (10, 0, 0, 0)
          and total_weight == scal(5, (coefficient_mass, 0, 0, 0)))

    print("TWIST-J force and Born dictionary witness")
    print("exact arithmetic: Z, Q via 16G, and Z[zeta_5]")
    print("finite Green scope: C4 pseudoinverse, not the continuum 1/(4 pi r) law")
    print()
    passed = 0
    for index, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s %02d %s" % (tag, index, name))
    print()
    print("RESULT %d/%d %s" % (
        passed,
        len(CHECKS),
        "ALL PASS" if passed == len(CHECKS) else "FAILURES PRESENT",
    ))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
