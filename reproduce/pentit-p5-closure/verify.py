#!/usr/bin/env python3
"""Exact public witness for the pentit boundary and p=5 root selector.

Standard-library only.  All finite-field arithmetic is represented by integer
pairs in F_25 = F_5[t]/(t^2 - 2); no floats or numerical approximations enter.
"""

import sys


P = 5
J_IMAGE = 2
CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


def add(x, y):
    return ((x[0] + y[0]) % 5, (x[1] + y[1]) % 5)


def mul(x, y):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5,
            (x[0] * y[1] + x[1] * y[0]) % 5)


def power(x, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out


def order(x):
    out = x
    n = 1
    while out != (1, 0):
        out = mul(out, x)
        n += 1
    return n


def main():
    tau = (0, 1)
    j_image = (J_IMAGE, 0)
    phi_image = (3, 0)
    minus_one = (4, 0)

    # 01. The ramified reductions of J and phi are 2 and 3.  The latter is
    # the unique (double) root of x^2-x-1 in F_5.  Thus tau^2 = J and
    # tau^6 = phi, so tau^3 is an exact square root of phi.
    phi_roots = [x for x in range(5) if (x * x - x - 1) % 5 == 0]
    ok = all((x * x) % 5 != 2 for x in range(5))
    ok &= phi_roots == [3]
    ok &= power(tau, 2) == j_image
    ok &= power(tau, 4) == minus_one
    ok &= power(tau, 6) == phi_image
    ok &= mul(power(tau, 3), power(tau, 3)) == phi_image
    ok &= order(tau) == 8
    check("ROOTS",
          "in F_25 = F_5[t]/(t^2-2), J -> 2 and phi -> 3;"
          " tau=t has tau^2=J, tau^4=-1, tau^6=phi, hence"
          " sqrt(phi)=tau^3; tau has exact order 8", ok)

    # 02. The finite-field norm is x^(5+1).  Check the entire tau ladder,
    # including the inverse-power form in F_5*.
    ok = True
    for k in range(24):
        x = power(tau, k)
        norm = mul(x, power(x, 5))
        expected = pow(3, k, 5)
        inverse_ladder = pow(2, (-k) % 4, 5)
        ok &= norm == (expected, 0)
        ok &= expected == inverse_ladder
    check("NORM-LADDER",
          "for k=0..23, N(tau^k)=tau^(6k)=3^k=2^(-k)"
          " in F_5* exactly", ok)

    # 03. The time-source and half-root reciprocity statements use only the
    # exact order-four scalar i_5=2 and the root identities above.
    i5 = (2, 0)
    sqrt_j = tau
    sqrt_phi = power(tau, 3)
    ok = order(i5) == 4
    ok &= power(i5, 2) == minus_one
    ok &= mul(sqrt_j, sqrt_phi) == minus_one
    ok &= mul(mul(sqrt_j, power(sqrt_j, 5)),
              mul(sqrt_phi, power(sqrt_phi, 5))) == (1, 0)
    ok &= mul(j_image, phi_image) == (1, 0)
    check("SOURCE",
          "i_5=2 has order 4 and reaches -1 after two steps;"
          " sqrt(J)sqrt(phi)=tau^4=-1, the two norms multiply to 1,"
          " and phi=J^-1 in F_5", ok)

    # 04. V_+ is defined publicly as the sign quotient of F_5*.  Its two
    # classes are explicit and its nontrivial class squares to the identity.
    units = {1, 2, 3, 4}
    sign = {1, 4}
    cosets = {frozenset((a * h) % 5 for h in sign) for a in units}
    ok = cosets == {frozenset({1, 4}), frozenset({2, 3})}
    ok &= all(frozenset((a * b) % 5 for b in c) in cosets
              for a in units for c in cosets)
    ok &= frozenset({2, 3}) == frozenset((2 * x) % 5 for x in sign)
    ok &= (2 * 2) % 5 in sign
    check("QUBIT",
          "V_+ := F_5*/{+-1} has exactly the two classes"
          " {1,4} and {2,3}; the quotient is cyclic of order 2", ok)

    # 05. Root selection is a linear identity, not a thirteen-witness
    # independence claim: 2(p-2)=p+1 is equivalent to p=5.
    p = P
    ok = (2 * (p - 2) == p + 1) == (p == 5)
    ok &= 2 * (p - 2) - (p + 1) == p - 5
    ok &= all(((2 * (q - 2) == q + 1) == (q == 5))
              for q in range(2, 200))
    check("P5-ROOT",
          "for every positive prime p, (p-2)/(p+1)=1/2 iff p=5;"
          " after clearing the positive denominator the difference is p-5",
          ok)

    print("TWIST-J pentit and p=5 closure witness (exact arithmetic)")
    print("F_25 roots, norm ladder, time-source reciprocity, the sign quotient, and root selection")
    print()
    passed = 0
    for i, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        passed += int(ok)
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" %
          (passed, len(CHECKS),
           "ALL PASS" if passed == len(CHECKS) else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
