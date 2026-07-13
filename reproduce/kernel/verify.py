#!/usr/bin/env python3
# TWIST-J kernel witness: the axiom facts in exact integer arithmetic
# over Z[zeta_5], basis {1, j, j^2, j^3}, with j^4 reduced by
# 1 + j + j^2 + j^3 + j^4 = 0. No floats anywhere. Standard library
# only. Deterministic stdout; exit 0 on full pass.

import sys

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JGEN = (0, 1, 0, 0)               # j = zeta_5
JAX = (1, 0, 1, 0)                # J = 1 + j^2
PHI = (0, 0, -1, -1)              # phi = -j^2 - j^3


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


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


def norm(x):
    p = ONE
    for k in (1, 2, 3, 4):
        p = mul(p, sigma(x, k))
    assert p[1] == 0 and p[2] == 0 and p[3] == 0
    return p[0]


def trace(x):
    t = ZERO
    for k in (1, 2, 3, 4):
        t = add(t, sigma(x, k))
    assert t[1] == 0 and t[2] == 0 and t[3] == 0
    return t[0]


def mul_by_J_matrix():
    cols = [mul(JAX, power(JGEN, k)) for k in range(4)]
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def det4(m):
    def det3(a):
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
                - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
                + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    d = 0
    for c in range(4):
        minor = [[m[r][cc] for cc in range(4) if cc != c]
                 for r in range(1, 4)]
        d += ((-1) ** c) * m[0][c] * det3(minor)
    return d


def step(v):
    a, b, c, d = v
    return (a - c + d, b - c, a, b - c + d)


CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def main():
    j = JGEN
    J = JAX
    phi = PHI

    check("PENTA-ROOT           j^5 = 1", power(j, 5) == ONE)

    s = ONE
    for k in (1, 2, 3, 4):
        s = add(s, power(j, k))
    check("CYCLOTOMIC-RELATION  1 + j + j^2 + j^3 + j^4 = 0", s == ZERO)

    check("AXIOM-COORDINATES    J = 1 + j^2 = (1, 0, 1, 0)",
          add(ONE, power(j, 2)) == J)

    check("NORM-ONE             N(J) = 1", norm(J) == 1)

    check("TRACE-THREE          Tr(J) = 3", trace(J) == 3)

    check("GOLDEN-BRIDGE        J . phi = j", mul(J, phi) == j)

    check("CUBE-LAW             (J - 1)^3 = j", power(sub(J, ONE), 3) == j)

    check("FIFTH-POWER          J^5 . phi^5 = 1",
          mul(power(J, 5), power(phi, 5)) == ONE)

    ok = True
    for v in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
              (2, 3, 5, 7)]:
        if mul(J, v) != step(v):
            ok = False
    check("STEP-IS-J            M_J (a,b,c,d) = (a-c+d, b-c, a, b-c+d)", ok)

    M = mul_by_J_matrix()
    check("DET-IS-NORM          det(M_J) = N(J) = 1", det4(M) == 1)

    check("TRACE-IS-TRACE       tr(M_J) = Tr(J) = 3",
          sum(M[i][i] for i in range(4)) == 3)

    check("GOLDEN-QUADRATIC     phi^2 = phi + 1",
          power(phi, 2) == add(phi, ONE))

    Jbar = sigma(J, 4)
    two_minus_phi = sub(scal(2, ONE), phi)
    ok = (mul(J, Jbar) == two_minus_phi) and \
         (mul(two_minus_phi, power(phi, 2)) == ONE)
    check("MODULUS-CHORD        J Jbar = 2 - phi = phi^-2", ok)

    w = sub(ONE, J)
    check("TENTH-ROOT           (1 - J)^5 = -1, (1 - J)^10 = 1",
          power(w, 5) == neg(ONE) and power(w, 10) == ONE)

    check("RAMIFIED-CHORD       N(1 - j) = 5", norm(sub(ONE, j)) == 5)

    print("TWIST-J kernel witness (exact integer arithmetic in Z[zeta_5])")
    print("basis {1, j, j^2, j^3}; j^4 = -(1 + j + j^2 + j^3); no floats")
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
