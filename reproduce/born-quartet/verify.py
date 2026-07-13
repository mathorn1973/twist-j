#!/usr/bin/env python3
# TWIST-J Born quartet witness. Exact integer arithmetic, no floats,
# standard library only.
#
# The read place residual algebra is A_8 = Z[zeta_8]/5 =
# F_5[X]/(X^4 + 1), with the Born involution star: X -> X^7 (inversion
# of the phase) and the Born norm N_B(a) = a star(a). No positivity is
# claimed in the finite read; probabilities are the decoder step.
#
# Claims verified: BORN-HALF-ANGLE, BORN-RESIDUAL-SPLIT,
# SPIN-BISECTOR, BORN-ORDER-STAIRCASE.

import sys

P = 5

# ---------------------------------------------------- A_8 arithmetic
ONE8 = (1, 0, 0, 0)
X8 = (0, 1, 0, 0)
MINUS1 = (4, 0, 0, 0)


def a8_add(a, b):
    return tuple((a[i] + b[i]) % P for i in range(4))


def a8_mul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] = (c[i + k] + a[i] * b[k]) % P
    # X^4 = -1
    return ((c[0] - c[4]) % P, (c[1] - c[5]) % P,
            (c[2] - c[6]) % P, c[3] % P)


def a8_star(a):
    # X -> X^7 = -X^3: (a0, a1, a2, a3) -> (a0, -a3, -a2, -a1)
    return (a[0], (-a[3]) % P, (-a[2]) % P, (-a[1]) % P)


def a8_norm(a):
    return a8_mul(a, a8_star(a))


def a8_all():
    for i in range(625):
        v = []
        n = i
        for _ in range(4):
            v.append(n % 5)
            n //= 5
        yield tuple(v)


def a8_order(u):
    r = u
    n = 1
    while r != ONE8:
        r = a8_mul(r, u)
        n += 1
        if n > 625:
            return 0
    return n


# ------------------------------------------- F_25 = F_5[x]/(x^2 + 2)
F25_ONE = (1, 0)


def f25_mul(a, b):
    # (a0 + a1 x)(b0 + b1 x), x^2 = -2 = 3
    return ((a[0] * b[0] + 3 * a[1] * b[1]) % P,
            (a[0] * b[1] + a[1] * b[0]) % P)


def f25_pow(a, n):
    r = F25_ONE
    for _ in range(n):
        r = f25_mul(r, a)
    return r


def mat_mul(A, B):
    out = []
    for i in range(2):
        row = []
        for j in range(2):
            acc = (0, 0)
            for k in range(2):
                m = f25_mul(A[i][k], B[k][j])
                acc = ((acc[0] + m[0]) % P, (acc[1] + m[1]) % P)
            row.append(acc)
        out.append(tuple(row))
    return tuple(out)


def mat_det(A):
    d1 = f25_mul(A[0][0], A[1][1])
    d2 = f25_mul(A[0][1], A[1][0])
    return ((d1[0] - d2[0]) % P, (d1[1] - d2[1]) % P)


def mat_scal(c, A):
    return tuple(tuple(f25_mul(c, A[i][j]) for j in range(2))
                 for i in range(2))


# ---------------------------------------- F_625 = F_5[y]/(y^4 - 2)
def f625_mul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] = (c[i + k] + a[i] * b[k]) % P
    # y^4 = 2
    return ((c[0] + 2 * c[4]) % P, (c[1] + 2 * c[5]) % P,
            (c[2] + 2 * c[6]) % P, c[3] % P)


def f625_pow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = f625_mul(r, a)
    return r


# ------------------------------------------------ polynomials mod 5
def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            out[i + k] = (out[i + k] + x * y) % P
    return out


CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def main():
    # 01 the involution is well behaved
    ok = all(a8_star(a8_star(a)) == a for a in a8_all())
    ok = ok and all(a8_star(a8_norm(a)) == a8_norm(a) for a in a8_all())
    pw = X8
    for _ in range(6):
        pw = a8_mul(pw, X8)
    ok = ok and a8_star(X8) == pw
    check("STAR         star is an involution, star fixes every Born"
          " norm, star(X) = X^7", ok)

    # 02 the Born unit group is cyclic of order 24
    units = [u for u in a8_all() if a8_norm(u) == ONE8]
    orders = [a8_order(u) for u in units]
    ok = (len(units) == 24 and max(orders) == 24
          and all(24 % n == 0 for n in orders)
          and a8_order(X8) == 8)
    check("BORN-UNITS   the Born unit group of A_8 is cyclic of order"
          " 24; zeta_8 has order 8", ok)

    # 03 the half angle identity on every Born unit
    ok = True
    for u in units:
        one_u = a8_add(ONE8, u)
        if a8_mul(one_u, one_u) != a8_mul(u, a8_norm(one_u)):
            ok = False
            break
    check("HALF-ANGLE   (1 + u)^2 = u N_B(1 + u) on all 24 Born units",
          ok)

    # 04 the norm gate is exactly the square subgroup
    gated = set()
    for u in units:
        d = a8_norm(a8_add(ONE8, u))
        if any(a8_mul(r, r) == d and a8_star(r) == r for r in a8_all()):
            gated.add(u)
    squares = {a8_mul(v, v) for v in units}
    ok = (gated == squares and len(gated) == 12
          and X8 not in gated)
    check("NORM-GATE    the bisector norm has a star fixed root exactly"
          " on the squares of the unit group (12 of 24; at the antipode"
          " the root is 0); zeta_8 is ungated: its halving forces the"
          " quadratic step", ok)

    # 05 the normalized bisector witness on the whole gated half
    ok = True
    count = 0
    for u in sorted(gated):
        if u == MINUS1:
            continue
        found = False
        for r in a8_all():
            if a8_mul(r, r) != a8_norm(a8_add(ONE8, u)):
                continue
            if a8_star(r) != r:
                continue
            rinv = None
            for w in a8_all():
                if a8_mul(r, w) == ONE8:
                    rinv = w
                    break
            if rinv is None:
                continue
            H = a8_mul(a8_add(ONE8, u), rinv)
            if a8_mul(H, H) == u and a8_norm(H) == ONE8:
                found = True
                break
        if not found:
            ok = False
        else:
            count += 1
    zero = (0, 0, 0, 0)
    nilpotents = [r for r in a8_all() if a8_mul(r, r) == zero]
    anti = (nilpotents == [zero]
            and all(a8_mul(zero, w) != ONE8 for w in a8_all()))
    ok = ok and count == 11 and anti
    check("BISECTOR     the normalized bisector exists exactly on the 11"
          " non antipodal gated units (H^2 = u, N_B(H) = 1); at u = -1"
          " the bisector vanishes: the only square root of its norm is"
          " 0, not invertible", ok)

    # 06 the residual split at prime 2, conductor 8
    lhs = poly_mul([2, 0, 1], [3, 0, 1])          # (x^2+2)(x^2+3)
    split8 = lhs == [1, 0, 0, 0, 1]               # x^4 + 1
    rev = [c % P for c in (2, 0, 1)][::-1]        # reverse of x^2 + 2
    monic = [(c * 3) % P for c in rev]            # normalize by 2^-1 = 3
    swap8 = monic == [3, 0, 1]                    # lands on x^2 + 3
    check("SPLIT-8      x^4 + 1 = (x^2 + 2)(x^2 + 3) mod 5; inversion"
          " swaps the two factors", split8 and swap8)

    # 07 the residual split at the Gaussian ring
    lhs = poly_mul([(-2) % P, 1], [(-3) % P, 1])  # (x - 2)(x - 3)
    split4 = lhs == [1, 0, 1]                     # x^2 + 1
    swap4 = (-2) % P == 3 and (-3) % P == 2       # conjugation swaps roots
    check("SPLIT-4      x^2 + 1 = (x - 2)(x - 3) mod 5; conjugation"
          " swaps the two roots", split4 and swap4)

    # 08 the integer skeleton of the spinor
    B = ((0, -1), (1, 0))

    def imul(A, C):
        return tuple(tuple(sum(A[i][k] * C[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))

    I2 = ((1, 0), (0, 1))
    S = ((1, 1), (-1, 1))                         # 1 - B
    B2 = imul(B, B)
    ok = (B2 == ((-1, 0), (0, -1)) and imul(B2, B2) == I2
          and S[0][0] * S[1][1] - S[0][1] * S[1][0] == 2
          and imul(S, S) == ((0, 2), (-2, 0)))
    check("SPIN-Z       B^2 = -I, B^4 = I, det(1 - B) = 2,"
          " (1 - B)^2 = -2 B over Z", ok)

    # 09 the SL_2(F_25) shadow of the spinor
    s = (0, 2)                                    # s = 2x, s^2 = 2
    ok = f25_mul(s, s) == (2, 0)
    sinv = f25_mul((3, 0), s)                     # s^-1 = 3 s
    ok = ok and f25_mul(s, sinv) == F25_ONE
    Sf = (((1, 0), (1, 0)), ((4, 0), (1, 0)))     # 1 - B over F_25
    R = mat_scal(sinv, Sf)
    ok = ok and mat_det(R) == F25_ONE
    R2 = mat_mul(R, R)
    negB = (((0, 0), (1, 0)), ((4, 0), (0, 0)))   # -B over F_25
    ok = ok and R2 == negB
    R4 = mat_mul(R2, R2)
    R8 = mat_mul(R4, R4)
    negI = (((4, 0), (0, 0)), ((0, 0), (4, 0)))
    posI = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    ok = ok and R4 == negI and R8 == posI
    check("SPIN-F25     R = (1 - B)/sqrt2 in SL_2(F_25): det R = 1,"
          " R^2 = -B, R^4 = -I, R^8 = I", ok)

    # 10 the staircase divisibilities and the two quadratic steps
    ok = (4 % 4 == 0 and 4 % 8 != 0 and 24 % 8 == 0
          and 4 % 16 != 0 and 24 % 16 != 0 and 124 % 16 != 0
          and 624 % 16 == 0
          and 25 == 5 ** 2 and 625 == 25 ** 2)
    check("STAIRCASE    4 | 4; 8 not | 4, 8 | 24; 16 not | 4, 16 not |"
          " 24, 16 not | 124, 16 | 624; two quadratic steps", ok)

    # 11 explicit witnesses of orders 8 and 16, with irreducibility
    x = (0, 1)
    ok = all(((r * r + 2) % P) != 0 for r in range(5))
    ok = ok and f25_pow(x, 4) == (4, 0) and f25_pow(x, 8) == (1, 0)
    quartic = [3, 0, 0, 0, 1]                     # y^4 - 2 = y^4 + 3
    ok = ok and all(((r ** 4 - 2) % P) != 0 for r in range(5))
    irr = True
    for b in range(5):
        for c in range(5):
            for e in range(5):
                for f in range(5):
                    if poly_mul([c, b, 1], [f, e, 1]) == quartic:
                        irr = False
    ok = ok and irr
    y = (0, 1, 0, 0)
    ok = ok and f625_pow(y, 8) == (4, 0, 0, 0) and \
        f625_pow(y, 16) == (1, 0, 0, 0)
    check("WITNESSES    order 8 first at F_25 (x, x^2 = -2); order 16"
          " first at F_625 (y, y^4 = 2); both moduli irreducible", ok)

    print("TWIST-J Born quartet witness (exact integer arithmetic)")
    print("A_8 = Z[zeta_8]/5 = F_5[X]/(X^4 + 1); star: X -> X^7;"
          " N_B(a) = a star(a)")
    print("no positivity is claimed in the finite read")
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
