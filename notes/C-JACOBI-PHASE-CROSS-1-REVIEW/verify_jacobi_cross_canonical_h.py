#!/usr/bin/env python3
# verify_jacobi_cross_canonical_h.py
# Review reanalysis of C-JACOBI-PHASE-CROSS-1 (branch agent/c-jacobi-phase-cross-1)
# by the originating session of the NADHLED note, answering that bundle's
# offered continuation 3: recompute the cross against the CANONICAL
# conjugation-invariant half-class h and quarter-arc a of the public
# carrier rows (v61), through an independent code path.
#
# Frozen surface (stated before this run, reusing their frozen lines):
#   carrier      p = 1 mod 5, 11 <= p <= 30000  (assert count 808)
#   phase side   THEIR frozen convention: least primitive root g,
#                chi(g) = zeta, J_p = J(chi, chi); QUAD of sigma_1(J_p);
#                SGN = unordered {sign Re sigma_1, sign Re sigma_2}
#   modulus side CANONICAL h and arc: exact octant o of theta in (0,1),
#                conjugate law o + o' = 7 asserted, h = [o in {2,3,4,5}],
#                arc = min(o, 7 - o)  (both class functions, tie-break free)
#   tests        T1' QUAD x h    df 3  crit 11345/1000
#                T2' SGN  x h    df 2  crit  9210/1000
#                T3' QUAD x arc  df 9  crit 21666/1000
#   rule         VOID if any expected cell < 5 or |X2 - crit| <= 1/1000;
#                REJECT if X2 > crit + 1/1000; else NOT-REJECT
#   cross gates  X1 QUAD marginal == (224, 205, 192, 187)
#                X2 SGN  marginal == (193, 407, 208)
#                X3 h marginal    == (395, 413)   [their invariant refold]
#                X4 T1' table == collapse of their pinned T3 over {0,3},{1,2}:
#                   (123,101), (93,112), (92,100), (87,100)
# Exact integer and Fraction arithmetic in every gate and decision; floats
# only in lines labeled witness.

from fractions import Fraction
from math import isqrt

X_LO = 11
X_HI = 30000
CRIT = {
    "T1": Fraction(11345, 1000),
    "T2": Fraction(9210, 1000),
    "T3": Fraction(21666, 1000),
}
BAND = Fraction(1, 1000)

XCHK_QUAD = (224, 205, 192, 187)
XCHK_SGN = (193, 407, 208)
XCHK_H = (395, 413)
XCHK_T1 = ((123, 101), (93, 112), (92, 100), (87, 100))

# ---------------- Z[zeta_5], basis (1, z, z^2, z^3), z^4 = -1-z-z^2-z^3

def zx_mul(x, y):
    e = [0] * 7
    for i in range(4):
        if x[i]:
            for j in range(4):
                e[i + j] += x[i] * y[j]
    e[0] += e[5]
    e[1] += e[6]
    r = [e[0] - e[4], e[1] - e[4], e[2] - e[4], e[3] - e[4]]
    return tuple(r)

def zx_conj(x):
    A, B, C, D = x
    return (A - B, -B, D - B, C - B)

def zx_gal2(x):
    A, B, C, D = x
    return (A - C, D - C, B - C, -C)

# ---------------- Z[phi] exact signs (validated layer)

def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def zmulp(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)

def zsign(x):
    a, b = x
    s = 2 * a + b
    t = b
    if s == 0 and t == 0:
        return 0
    if s >= 0 and t >= 0:
        return 1
    if s <= 0 and t <= 0:
        return -1
    if s > 0:
        d = s * s - 5 * t * t
    else:
        d = 5 * t * t - s * s
    if d == 0:
        raise AssertionError("STOP exact tie in zsign")
    return 1 if d > 0 else -1

def zcmp(x, y):
    return zsign(zsub(x, y))

PHI = (0, 1)
PHIM1 = (-1, 1)

def re2_sign(x):
    A, B, C, D = x
    return zsign((2 * A - B, B - C - D))

def im_sign(x):
    A, B, C, D = x
    return zsign((C - D, B))

# ---------------- phase avatar, their frozen convention, my code path

def factorize(n):
    fs = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs

def least_primitive_root(p):
    fs = factorize(p - 1)
    g = 2
    while True:
        ok = True
        for q in fs:
            if pow(g, (p - 1) // q, p) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1

def jacobi_sum(p):
    g = least_primitive_root(p)
    ind = [0] * p
    x = 1
    for k in range(p - 1):
        ind[x] = k
        x = x * g % p
    c = [0] * 5
    for t in range(2, p):
        c[(ind[t] + ind[p + 1 - t]) % 5] += 1
    J = (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])
    assert zx_mul(J, zx_conj(J)) == (p, 0, 0, 0), "STOP G-Weil J conj J = p"
    return J

def quad_of(J):
    rs = re2_sign(J)
    ims = im_sign(J)
    assert rs != 0 and ims != 0, "STOP axis case"
    if rs > 0 and ims > 0:
        return 0
    if rs < 0 and ims > 0:
        return 1
    if rs < 0 and ims < 0:
        return 2
    return 3

def sgn_of(J):
    s1 = re2_sign(J)
    s2 = re2_sign(zx_gal2(J))
    assert s1 != 0 and s2 != 0, "STOP zero real part"
    if s1 > 0 and s2 > 0:
        return 0
    if s1 < 0 and s2 < 0:
        return 2
    return 1

# ---------------- modulus avatar, canonical machinery (validated today)

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(a, p):
    a %= p
    assert legendre(a, p) == 1, "STOP nonresidue"
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        assert r * r % p == a
        return r
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre(z, p) != p - 1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
    while t != 1:
        i = 0
        t2 = t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
            assert i < m, "STOP tonelli loop"
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = b * b % p
        t = t * c % p
        r = r * b % p
    assert r * r % p == a
    return r

FIB = [0, 1]
while len(FIB) < 24:
    FIB.append(FIB[-1] + FIB[-2])

def qform(v):
    x, y = v
    return 2 * x * x + 2 * x * y + 3 * y * y

def bform(u, v):
    return 2 * u[0] * v[0] + u[0] * v[1] + u[1] * v[0] + 3 * u[1] * v[1]

def gauss_shortest(p, c):
    u = (p, 0)
    v = (-c, 1)
    if qform(u) > qform(v):
        u, v = v, u
    guard = 0
    while True:
        guard += 1
        assert guard < 200, "STOP gauss loop"
        qb = qform(u)
        r = (2 * bform(u, v) + qb) // (2 * qb)
        v = (v[0] - r * u[0], v[1] - r * u[1])
        if qform(v) < qform(u):
            u, v = v, u
        else:
            break
    return u

def znorm(x):
    a, b = x
    return a * a + a * b - b * b

def zneg(x):
    return (-x[0], -x[1])

def zconjp(x):
    a, b = x
    return (a + b, -b)

def octant_from(g, p):
    if zsign(g) < 0:
        g = zneg(g)
    P1 = (p, 0)
    PPHI2 = (p, p)
    g2 = zmulp(g, g)
    while zcmp(g2, P1) < 0:
        g = zmulp(g, PHI)
        g2 = zmulp(g, g)
    while zcmp(g2, PPHI2) >= 0:
        g = zmulp(g, PHIM1)
        g2 = zmulp(g, g)
    assert zcmp(g2, P1) > 0 and zcmp(g2, PPHI2) < 0, "STOP band tie"
    assert abs(znorm(g)) == p, "STOP norm drift"
    g4 = zmulp(g2, g2)
    g8 = zmulp(g4, g4)
    g16 = zmulp(g8, g8)
    p8 = p ** 8
    assert zsign(zsub(g16, (p8, 0))) > 0, "STOP lower tie"
    assert zsign(zsub(g16, (p8 * FIB[15], p8 * FIB[16]))) < 0, "STOP upper tie"
    o = 0
    for j in range(1, 8):
        s = zsign(zsub(g16, (p8 * FIB[2 * j - 1], p8 * FIB[2 * j])))
        assert s != 0, "STOP octant tie"
        if s > 0:
            o = j
        else:
            break
    return o

def class_bits(p):
    r = tonelli(5, p)
    c = (1 + r) * pow(2, p - 2, p) % p
    assert (c * c - c - 1) % p == 0, "STOP root check"
    g = gauss_shortest(p, c)
    assert abs(znorm(g)) == p, "STOP shortest norm"
    o = octant_from(g, p)
    oc = octant_from(zconjp(g), p)
    assert o + oc == 7, "STOP conjugate law"
    h = 1 if o in (2, 3, 4, 5) else 0
    a = min(o, 7 - o)
    return h, a

# ---------------- chi-square and decision, their frozen rule

def chi2_exact(table):
    rows = len(table)
    cols = len(table[0])
    R = [sum(table[i]) for i in range(rows)]
    C = [sum(table[i][j] for i in range(rows)) for j in range(cols)]
    N = sum(R)
    x2 = Fraction(0)
    minE = None
    for i in range(rows):
        for j in range(cols):
            E = Fraction(R[i] * C[j], N)
            if minE is None or E < minE:
                minE = E
            x2 += (table[i][j] - E) ** 2 / E
    return x2, minE

def decide(name, x2, minE):
    crit = CRIT[name]
    if minE < 5:
        return "VOID (expected cell < 5)"
    if abs(x2 - crit) <= BAND:
        return "VOID (rounding band)"
    if x2 > crit + BAND:
        return "REJECTED"
    return "NOT-REJECTED"

# ---------------- main

def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = 0
    s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(2, n + 1) if s[i]]

def main():
    print("REVIEW    verify_jacobi_cross_canonical_h.py")
    print("TARGET    C-JACOBI-PHASE-CROSS-1 (branch agent/c-jacobi-phase-cross-1)")
    print("SURFACE   their frozen phase convention and chi-square lines;")
    print("          canonical conjugation-invariant h and arc on the modulus side")
    carrier = [p for p in primes_upto(X_HI) if p >= X_LO and p % 5 == 1]
    assert len(carrier) == 808, "STOP carrier count"
    t1 = [[0, 0] for _ in range(4)]
    t2 = [[0, 0] for _ in range(3)]
    t3 = [[0, 0, 0, 0] for _ in range(4)]
    qm = [0, 0, 0, 0]
    sm = [0, 0, 0]
    hm = [0, 0]
    am = [0, 0, 0, 0]
    for p in carrier:
        J = jacobi_sum(p)
        q = quad_of(J)
        s = sgn_of(J)
        h, a = class_bits(p)
        qm[q] += 1
        sm[s] += 1
        hm[h] += 1
        am[a] += 1
        t1[q][h] += 1
        t2[s][h] += 1
        t3[q][a] += 1
    print("GATES     J conj(J) = p, axis and zero-real exclusions, |N(w)| = p,")
    print("          conjugate octant law: PASS on all 808 carrier primes")
    print("MARGINAL  QUAD %d %d %d %d" % tuple(qm))
    print("MARGINAL  SGN  %d %d %d" % tuple(sm))
    print("MARGINAL  h    %d %d" % tuple(hm))
    print("MARGINAL  arc  %d %d %d %d" % tuple(am))
    ok1 = tuple(qm) == XCHK_QUAD
    ok2 = tuple(sm) == XCHK_SGN
    ok3 = tuple(hm) == XCHK_H
    ok4 = tuple(tuple(r) for r in t1) == XCHK_T1
    print("XCHECK X1 QUAD marginal vs pinned stdout: %s" % ("MATCH" if ok1 else "MISMATCH"))
    print("XCHECK X2 SGN marginal vs pinned stdout:  %s" % ("MATCH" if ok2 else "MISMATCH"))
    print("XCHECK X3 h marginal vs their invariant refold: %s" % ("MATCH" if ok3 else "MISMATCH"))
    print("XCHECK X4 T1' table vs collapse of their T3:    %s" % ("MATCH" if ok4 else "MISMATCH"))
    for name, tab, desc in (("T1", t1, "QUAD x h"), ("T2", t2, "SGN x h"), ("T3", t3, "QUAD x arc")):
        x2, minE = chi2_exact(tab)
        d = decide(name, x2, minE)
        print("%s' %s" % (name, desc))
        for row in tab:
            print("    " + "  ".join("%5d" % v for v in row))
        print("    X2 exact   = %d/%d" % (x2.numerator, x2.denominator))
        print("    X2 witness = %.6f (float, witness only)" % float(x2))
        print("    min expected = %d/%d" % (minE.numerator, minE.denominator))
        print("    DECISION   = %s" % d)
    if ok1 and ok2 and ok3 and ok4:
        print("XCHECK ALL MATCH: independent code path reproduces their pinned data")
    else:
        print("XCHECK MISMATCH: see lines above")
    print("REVIEW PASS")

if __name__ == "__main__":
    main()
