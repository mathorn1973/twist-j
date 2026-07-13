#!/usr/bin/env python3
# TWIST-J foundations and places witness. Exact arithmetic only:
# integers, rationals, Q(sqrt5) pairs, the cyclotomic rings Z[zeta_5]
# and Z[zeta_8], Gaussian integers, and F_25 as pairs over F_5.
# Standard library only, no floats anywhere.
#
# The arc: the autonomous counter coordinate on the nonnegative
# forward orbit of the 2-adic odometer (the drive bit is the finite
# binary digit-sum parity, with exact recursions theta_2n = theta_n and
# theta_(2n+1) = 1 - theta_n and the carry parity law); the self similar
# time quantum tower on
# Z/5^k, T^(5^k) = i_5 I with i_5^4 = 1 and period exactly 4 x 5^k,
# computed for k = 1 to 4; the degree split by prime (sqrt5 at
# zeta_5, sqrt2 and i at zeta_8, neither in the unique quadratic
# subfield Q(sqrt5) of Q(zeta_5)); the Z2 family split (one Galois
# involution at zeta_5, a complete Klein four at zeta_8, the Gaussian
# split 5 = (2 + i)(2 - i) swapped by conjugation); the bilocation of
# i; and the silver sibling (m = sqrt(i) with the silver unit of norm
# -1 mirroring tau = sqrt(J) inside F_25, where the step collapses to
# the doubling J = 2).
#
# Claims verified: ODOMETER-INTERNALIZED, TIME-QUANTUM-TOWER,
# DEGREES-BY-PRIME, Z2-PLACES-SPLIT, I-BILOCATED, SILVER-SIBLING.
# READING-SPLIT is carried inline in the Canon (each leg separately
# registered); CURVATURE-TRACE-VALUE stays a live open row and
# nothing here claims it. This file computes the time quantum statement
# for k = 1 to 4 only and makes no all-k claim.

import sys
from fractions import Fraction as Fr

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------------ Q(sqrt5): a + b sqrt5
PHI = (Fr(1, 2), Fr(1, 2))


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


# ------------------------------------------------ Z[zeta_5], basis 1..z^3
def zmul5(a, b):
    c = [0] * 5
    for i in range(4):
        for j in range(4):
            c[(i + j) % 5] += a[i] * b[j]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


# ------------------------------------------------ Z[zeta_8], basis 1..m^3
def zmul8(a, b):
    c = [0] * 7
    for i in range(4):
        for j in range(4):
            c[i + j] += a[i] * b[j]
    # m^4 = -1, m^5 = -m, m^6 = -m^2
    return (c[0] - c[4], c[1] - c[5], c[2] - c[6], c[3])


# ------------------------------------------------ Gaussian integers
def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


# ------------------------------------------------ F_25 = F_5[t]/(t^2 - 2)
def f25_mul(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5,
            (x[0] * y[1] + x[1] * y[0]) % 5)


# ------------------------------------------------ 4x4 matrices mod 5^k
MJ = ((1, 0, -1, 1),
      (0, 1, -1, 0),
      (1, 0, 0, 0),
      (0, 1, -1, 1))


def mmul4(a, b, mod):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(4)) % mod
                       for j in range(4)) for i in range(4))


def mpow4(a, e, mod):
    r = tuple(tuple(1 if i == j else 0 for j in range(4))
              for i in range(4))
    a = tuple(tuple(x % mod for x in row) for row in a)
    while e:
        if e & 1:
            r = mmul4(r, a, mod)
        a = mmul4(a, a, mod)
        e >>= 1
    return r


def main():
    # ------------------------------ 01 the internalized counter
    def t_bit(n):
        return bin(n).count("1") & 1

    ok = True
    for n in range(8192):
        ok &= t_bit(2 * n) == t_bit(n)
        ok &= t_bit(2 * n + 1) == 1 - t_bit(n)
    for n in range(8192):
        r = 0
        while (n >> r) & 1:
            r += 1
        ok &= (t_bit(n + 1) != t_bit(n)) == (r % 2 == 0)
    # the autonomous closure: maintain the drive bit by the local
    # carry rule alone (flip exactly when the carry chain has even
    # length), never calling a global popcount, and match the
    # external Thue-Morse list on a long window
    reg = 0
    par = 0
    ok_orbit = True
    for n in range(100000):
        if par != t_bit(n):
            ok_orbit = False
            break
        r = 0
        while (reg >> r) & 1:
            r += 1
        if r % 2 == 0:
            par ^= 1
        reg += 1
    ok &= ok_orbit
    check("ODOMETER",
          "the autonomous counter is the nonnegative forward orbit of"
          " the 2-adic odometer: the drive bit theta_n is the finite"
          " binary digit-sum parity, with the exact recursions"
          " theta_2n = theta_n and theta_(2n+1) = 1 - theta_n and the"
          " carry parity law"
          " (the bit flips exactly when the carry chain has even"
          " length), verified exhaustively below 2^13; the drive read"
          " from the counter coordinate alone reproduces the reference"
          " word on the full window; no parity function on all of Z_2"
          " is asserted", ok)

    # ------------------------------ 02 the time quantum tower
    ok = True
    for k in (1, 2, 3, 4):
        mod = 5 ** k
        p5k = mpow4(MJ, 5 ** k, mod)
        scal = p5k[0][0]
        ok &= all(p5k[i][j] == (scal if i == j else 0)
                  for i in range(4) for j in range(4))
        ok &= scal % 5 == 2
        ok &= pow(scal, 4, mod) == 1 and pow(scal, 2, mod) != 1
        ident = tuple(tuple(1 if i == j else 0 for j in range(4))
                      for i in range(4))
        a = tuple(tuple(x % mod for x in row) for row in MJ)
        r = a
        order = 1
        while r != ident:
            r = mmul4(r, a, mod)
            order += 1
        ok &= order == 4 * 5 ** k
    check("TOWER",
          "the self similar time quantum, computed for k = 1 to 4: on"
          " Z/5^k the step operator satisfies T^(5^k) = i_5 I with the"
          " scalar of exact multiplicative order 4 and i_5 = 2 mod 5,"
          " and the period of M_J is exactly 4 x 5^k (the order found"
          " by direct search); no all-k theorem is claimed", ok)

    # ------------------------------ 03 the degrees split by prime
    # sqrt5 at zeta_5: (2 phi - 1)^2 = 5 with 2 phi - 1 = z - z^2 - z^3 + z^4
    # z^4 = -1 - z - z^2 - z^3, so z - z^2 - z^3 + z^4 = -1 - 2 z^2 - 2 z^3
    tau5 = (-1, 0, -2, -2)
    ok = zmul5(tau5, tau5) == (5, 0, 0, 0)
    # sqrt2 and i at zeta_8
    m = (0, 1, 0, 0)
    sqrt2 = (0, 1, 0, -1)  # m + m^-1 = m - m^3
    ok &= zmul8(sqrt2, sqrt2) == (2, 0, 0, 0)
    i8 = zmul8(m, m)
    ok &= i8 == (0, 0, 1, 0)
    ok &= zmul8(i8, i8) == (-1, 0, 0, 0)
    # sqrt2 not in Q(sqrt5): (a + b sqrt5)^2 = 2 forces 2ab = 0;
    # b = 0 gives a^2 = 2, a = 0 gives b^2 = 2/5, and neither
    # x^2 - 2 nor y^2 - 10 (y = 5b) has a rational root: any rational
    # root of a monic integer polynomial is an integer divisor of the
    # constant term, and the finite candidate lists fail.
    ok &= all(c * c != 2 for c in (1, -1, 2, -2))
    ok &= all(c * c != 10 for c in (1, -1, 2, -2, 5, -5, 10, -10))
    # i not in Q(sqrt5): (a + b sqrt5)^2 = -1 forces a^2 + 5 b^2 = -1,
    # a sum of squares equal to a negative rational: impossible.
    ok &= all(q5_mul((Fr(A), Fr(B)), (Fr(A), Fr(B)))
              == (Fr(A) ** 2 + 5 * Fr(B) ** 2, 2 * Fr(A) * Fr(B))
              and Fr(A) ** 2 + 5 * Fr(B) ** 2 >= 0
              for A in range(-3, 4) for B in range(-3, 4))
    # order 5 native magic at prime 5, order 8 foreign magic at prime 2
    zk = (0, 1, 0, 0)
    acc = zk
    o5 = 1
    while acc != (1, 0, 0, 0):
        acc = zmul5(acc, zk)
        o5 += 1
    acc = m
    o8 = 1
    while acc != (1, 0, 0, 0):
        acc = zmul8(acc, m)
        o8 += 1
    ok &= o5 == 5 and o8 == 8
    check("GRADINGS",
          "the degrees split by prime: sqrt5 lives at zeta_5,"
          " (2 phi - 1)^2 = 5 exactly in Z[zeta_5]; sqrt2 and i live"
          " at zeta_8, (m + m^-1)^2 = 2 and m^2 = i with i^2 = -1 in"
          " Z[zeta_8]; neither sqrt2 nor i lies in Q(sqrt5) (finite"
          " rational root exclusion, and a sum of squares is never"
          " negative); the native magic has order 5 = p and the"
          " foreign magic order 8 = 2^3", ok)

    # ------------------------------ 04 one involution at zeta_5
    g5 = [a for a in range(1, 5)]
    inv5 = [a for a in g5 if a != 1 and (a * a) % 5 == 1]
    ok = inv5 == [4]
    ok &= sorted(pow(2, k, 5) for k in range(1, 5)) == [1, 2, 3, 4]
    # the unique index 2 subgroup of C_4 is {1, 4}: the only order 2
    # subgroup, hence exactly one quadratic subfield, and it is
    # Q(sqrt5) because 2 phi - 1 is fixed by z -> z^4
    def conj5(v):
        # z -> z^4 = -1 - z - z^2 - z^3 on the power basis
        return (v[0] - v[1], -v[1], v[3] - v[1], v[2] - v[1])

    ok &= conj5(tau5) == tau5
    ok &= conj5((0, 1, 0, 0)) == (-1, -1, -1, -1)
    ok &= all(conj5(conj5(w)) == w
              for w in ((1, 2, 3, 4), (0, 1, 0, 0), (-1, 0, -2, -2)))
    subgroups2 = [s for s in ((1, 4), (1, 2), (1, 3))
                  if all((a * b) % 5 in s for a in s for b in s)]
    ok &= subgroups2 == [(1, 4)]
    check("ONE-INVOL",
          "the Galois group of the zeta_5 place is cyclic of order 4"
          " (2 generates all of F_5*) with exactly one involution,"
          " a = 4, hence exactly one order 2 subgroup {1, 4} and"
          " exactly one quadratic subfield; it is Q(sqrt5), since"
          " 2 phi - 1 is fixed by z -> z^-1: the place where the"
          " forces split has one mirror", ok)

    # ------------------------------ 05 the Klein four at zeta_8
    g8 = [a for a in (1, 3, 5, 7)]
    ok = all((a * a) % 8 == 1 for a in g8)
    ok &= len([a for a in g8 if a != 1]) == 3
    ok &= all((a * b) % 8 in g8 for a in g8 for b in g8)
    check("KLEIN-FOUR",
          "the Galois group of the zeta_8 place is the complete Klein"
          " four group: every one of 3, 5, 7 squares to 1 mod 8, so"
          " every nontrivial symmetry of the foreign place is an"
          " involution; two places, two shapes of Z2 family", ok)

    # ------------------------------ 06 the Gaussian split of p
    a = (2, 1)
    b = (2, -1)
    ok = gmul(a, b) == (5, 0)
    ok &= a[0] * a[0] + a[1] * a[1] == 5
    ok &= b[0] * b[0] + b[1] * b[1] == 5
    ok &= (a[0], -a[1]) == b and (b[0], -b[1]) == a
    ok &= 5 % 4 == 1
    check("GAUSS-SPLIT",
          "the magic prime splits at the foreign place:"
          " 5 = (2 + i)(2 - i) exactly in Z[i], both factors of norm"
          " 5, and complex conjugation swaps the two Gaussian primes:"
          " charge conjugation is the swap of the two primes above p",
          ok)

    # ------------------------------ 07 i is bilocated
    ok = pow(2, 2, 5) == 4 == 5 - 1
    ok &= pow(2, 4, 5) == 1 and pow(2, 2, 5) != 1
    ok &= zmul8(m, m) == (0, 0, 1, 0)
    ok &= zmul8(zmul8(m, m), zmul8(m, m)) == (-1, 0, 0, 0)
    check("BILOCATED",
          "i is bilocated: at v_5 it is the order 4 element 2 of F_5*"
          " (2^2 = -1, exact order 4), at v_2 it is zeta_8^2 (m^2"
          " squares to -1); the two are identified only over Q, never"
          " merged", ok)

    # ------------------------------ 08 the silver sibling
    ok = zmul8(m, m) == (0, 0, 1, 0)  # m = sqrt(i)
    silver = (1, 1, 0, -1)  # 1 + sqrt2
    conj = (1, -1, 0, 1)    # 1 - sqrt2
    ok &= zmul8(silver, conj) == (-1, 0, 0, 0)  # norm -1
    # F_25 = F_5[t]/(t^2 - 2): tau^2 = 2, and 2 is the image of J at
    # the ramified place (the step charpoly collapses to (x - 2)^4)
    tau = (0, 1)
    ok &= f25_mul(tau, tau) == (2, 0)
    # F_25* is cyclic of order 24: exhibit a generator and check its
    # exact order; 2 is a non square in F_5 so t^2 - 2 is irreducible
    ok &= all((c * c) % 5 != 2 for c in range(5))
    orders = {}
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            g = (a, b)
            acc = g
            order = 1
            while acc != (1, 0):
                acc = f25_mul(acc, g)
                order += 1
            orders[g] = order
    ok &= len(orders) == 24
    ok &= all(24 % o == 0 for o in orders.values())
    ok &= max(orders.values()) == 24
    ok &= sum(1 for o in orders.values() if o == 24) == 8
    ok &= orders[(0, 1)] == 8  # ord(tau) = 8: tau^2 = 2 of order 4
    tau4 = f25_mul(f25_mul(tau, tau), f25_mul(tau, tau))
    ok &= tau4 == (4, 0) and (4 - (-1)) % 5 == 0
    check("SILVER",
          "the silver sibling: m = zeta_8 = sqrt(i) at prime 2, the"
          " silver unit 1 + sqrt2 has norm exactly -1; at prime 5,"
          " inside F_25 = F_5(sqrt 2) (2 is a non square, checked on"
          " all residues), tau^2 = 2 = the image of J at the ramified"
          " place and tau^4 = -1 with ord(tau) = 8, and F_25* is"
          " cyclic of order 24 (all 24 element orders divide 24, an"
          " order 24 element exists, and exactly phi(24) = 8 generate):"
          " the square root of the axiom has a mirror at the foreign"
          " place", ok)

    print("TWIST-J foundations and places witness (exact arithmetic)")
    print("Omega = N_0 x F_5^6; N_0 is the forward odometer orbit; the"
          " time quantum tower M_J^(5^k) = i_5 I holds for k = 1 to 4")
    print("sqrt5 at zeta_5, sqrt2 and i at zeta_8; one involution"
          " against a Klein four; 5 = (2 + i)(2 - i); tau^2 = J = 2 in"
          " F_25")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
