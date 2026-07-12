#!/usr/bin/env python3
# TWIST-J abelian face weights witness. Exact integer arithmetic in
# Z[zeta_5], basis {1, j, j^2, j^3}. No floats, standard library only.
#
# Claim BORN-FACE-WEIGHTS: the five abelian face weights
# w(k) = |1 + zeta_5^k|^2 are exact in Q(sqrt5):
# w(0) = 4, 2 w(1) = 2 w(4) = 3 + sqrt5, 2 w(2) = 2 w(3) = 3 - sqrt5,
# with total mass 10, the sigma_2 Galois pairing w(1) -> w(2), and the
# tilt w(1) + w(4) - w(2) - w(3) = 2 sqrt5 (so the normalized tilt is
# sqrt5 / 5). Here sqrt5 = 1 + 2 (j + j^4) inside Z[zeta_5].

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
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += x[i] * y[k]
    r = c[:4]
    r[0] -= c[4]
    r[1] -= c[4]
    r[2] -= c[4]
    r[3] -= c[4]
    r[0] += c[5]
    r[1] += c[6]
    return tuple(r)


def power(x, n):
    r = ONE
    for _ in range(n):
        r = mul(r, x)
    return r


def sigma(x, k):
    r = ZERO
    for i in range(4):
        r = add(r, scal(x[i], power(JGEN, (i * k) % 5)))
    return r


def w(k):
    a = add(ONE, power(JGEN, k % 5))
    b = add(ONE, power(JGEN, (5 - k) % 5))
    return mul(a, b)


CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def main():
    sqrt5 = add(ONE, scal(2, add(JGEN, power(JGEN, 4))))
    weights = [w(k) for k in range(5)]

    check("SQRT5   (1 + 2 (j + j^4))^2 = 5", mul(sqrt5, sqrt5) == (5, 0, 0, 0))
    check("W0      w(0) = 4", weights[0] == (4, 0, 0, 0))
    check("W1      2 w(1) = 3 + sqrt5",
          scal(2, weights[1]) == add((3, 0, 0, 0), sqrt5))
    check("W2      2 w(2) = 3 - sqrt5",
          scal(2, weights[2]) == sub((3, 0, 0, 0), sqrt5))
    check("CONJ    w(3) = w(2) and w(4) = w(1)",
          weights[3] == weights[2] and weights[4] == weights[1])
    total = ZERO
    for x in weights:
        total = add(total, x)
    check("MASS    w(0) + w(1) + w(2) + w(3) + w(4) = 10",
          total == (10, 0, 0, 0))
    check("GALOIS  sigma_2 w(1) = w(2)", sigma(weights[1], 2) == weights[2])
    tilt = sub(add(weights[1], weights[4]), add(weights[2], weights[3]))
    check("TILT    w(1) + w(4) - w(2) - w(3) = 2 sqrt5",
          tilt == scal(2, sqrt5))

    print("TWIST-J abelian face weights witness"
          " (exact integer arithmetic in Z[zeta_5])")
    print("w(k) = |1 + zeta_5^k|^2 = (1 + j^k)(1 + j^(5-k));"
          " sqrt5 = 1 + 2 (j + j^4)")
    print()
    passed = 0
    for i, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
