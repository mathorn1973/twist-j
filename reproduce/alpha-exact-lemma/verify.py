#!/usr/bin/env python3
# TWIST-J alpha exact lemma witness. Exact integer arithmetic, no
# floats, standard library only.
#
# Claim ALPHA-SEED: for the cyclotomic Galois-trace Gram
# G = p I - 1 1^T on dimension p - 1, the spectrum is
# {1 (once), p (p - 2 times)}; normalized by p it is
# {1/p (once), 1 (p - 2 times)}, and the all-ones trace direction is
# the eigenvector of the small eigenvalue. Verified here for
# p in {3, 5, 7, 11, 13}: eigenvector identities exactly, determinant
# exactly p^(p - 2) by fraction-free Bareiss elimination.

import sys


def gram(p):
    n = p - 1
    return [[(p if i == k else 0) - 1 for k in range(n)] for i in range(n)]


def matvec(m, v):
    return [sum(m[i][k] * v[k] for k in range(len(v))) for i in range(len(m))]


def det_bareiss(matrix):
    m = [row[:] for row in matrix]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if m[i][k] != 0), None)
            if swap is None:
                return 0
            m[k], m[swap] = m[swap], m[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * m[k][k] - m[i][k] * m[k][j]) // prev
            m[i][k] = 0
        prev = m[k][k]
    return sign * m[n - 1][n - 1]


def main():
    print("TWIST-J alpha exact lemma witness (exact integer arithmetic)")
    print("G = p I - 1 1^T on dimension p - 1; spectrum {1, p x (p - 2)};")
    print("normalized {1/p, 1 x (p - 2)}; the trace direction carries 1/p")
    print()
    primes = (3, 5, 7, 11, 13)
    passed = 0
    for p in primes:
        n = p - 1
        g = gram(p)
        ones = [1] * n
        ok = matvec(g, ones) == ones
        for i in range(n - 1):
            v = [0] * n
            v[i] = 1
            v[i + 1] = -1
            if matvec(g, v) != [p * x for x in v]:
                ok = False
        det = det_bareiss(g)
        if det != p ** (p - 2):
            ok = False
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s p = %2d  G u = u on the ones vector; G v = %2d v on the"
              " complement (%2d vectors); det = %d^%d" %
              (tag, p, p, n - 1, p, p - 2))
    print()
    print("RESULT %d/%d %s" % (passed, len(primes),
                               "ALL PASS" if passed == len(primes)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(primes) else 1


if __name__ == "__main__":
    sys.exit(main())
