#!/usr/bin/env python3
"""C-JACOBI-PHASE-CROSS-1 micro-selftest. NON-CANONICAL.

Exact anchor for the phase engine: for p = 1 mod 5 the quintic Jacobi sum
J_p lies in Z[zeta_5] and every one of its four Galois embeddings has
modulus exactly sqrt(p).  Equivalently the rapidity vector of J_p is the
zero vector.  The assertion is made in exact integer arithmetic in
Z[zeta_5]; no floating point enters any gate.

Python 3 standard library only.  Exit 0, empty stderr, deterministic
stdout.
"""

# ---------------------------------------------------------------------------
# Z[zeta_5] in the integral basis (1, zeta, zeta^2, zeta^3), zeta^4 = -1-z-z^2-z^3
# ---------------------------------------------------------------------------

ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)


def from_exponents(counts):
    """counts[j] = coefficient of zeta^j for j = 0..4 -> basis 4-tuple."""
    v = counts[4]
    return tuple(counts[t] - v for t in range(4))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, b):
    c = [0] * 5
    for i in range(4):
        ai = a[i]
        if ai:
            for j in range(4):
                c[(i + j) % 5] += ai * b[j]
    return from_exponents(c)


def gal(a, s):
    """sigma_s : zeta -> zeta^s, s in {1,2,3,4}."""
    c = [0] * 5
    for i in range(4):
        c[(i * s) % 5] += a[i]
    return from_exponents(c)


def conj(a):
    """complex conjugation = sigma_4 (zeta -> zeta^-1)."""
    return gal(a, 4)


def norm(a):
    r = ONE
    for s in (1, 2, 3, 4):
        r = mul(r, gal(a, s))
    return r


def is_rational(a):
    return a[1] == 0 and a[2] == 0 and a[3] == 0


# ---------------------------------------------------------------------------
# Z[phi] = Z + Z*phi, phi = (1+sqrt5)/2, phi^2 = phi + 1.  Pairs (u, v) = u + v*phi.
# ---------------------------------------------------------------------------


def pmul(x, y):
    (u, v), (s, t) = x, y
    # (u+v phi)(s+t phi) = us + (ut+vs) phi + vt phi^2 = (us+vt) + (ut+vs+vt) phi
    return (u * s + v * t, u * t + v * s + v * t)


def psub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def padd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sqrt5_sign(s, t):
    """sign of s + t*sqrt(5) for integers s, t.  Exact."""
    if s == 0 and t == 0:
        return 0
    if s >= 0 and t >= 0:
        return 1
    if s <= 0 and t <= 0:
        return -1
    lhs, rhs = s * s, 5 * t * t
    if lhs == rhs:
        return 0
    if s > 0:
        return 1 if lhs > rhs else -1
    return -1 if lhs > rhs else 1


def psign(x):
    """sign of u + v*phi = sign of ((2u+v) + v*sqrt5)/2.  Exact."""
    u, v = x
    return sqrt5_sign(2 * u + v, v)


def pcmp(x, y):
    return psign(psub(x, y))


# ---------------------------------------------------------------------------
# Exact real and imaginary parts of the principal embedding zeta -> exp(2 pi i/5).
#
#   X = A + B zeta + C zeta^2 + D zeta^3
#   2 Re X   = (2A - B) + (B - C - D) phi                          in Z[phi]
#   2 Im X   = sqrt(3 - phi) * (C - D + B phi)                     3 - phi = |1-zeta|^2
#
# Hence sign(Re X) and sign(Im X) are exact Z[phi] sign tests, and
#   4 |X|^2 = (2 Re X)^2 + (3 - phi) (C - D + B phi)^2   in Z[phi].
# ---------------------------------------------------------------------------

THREE_MINUS_PHI = (3, -1)


def re2(x):
    a, b, c, d = x
    return (2 * a - b, b - c - d)


def im2_reduced(x):
    """the Z[phi] factor of 2 Im X; the discarded factor sqrt(3-phi) is > 0."""
    a, b, c, d = x
    return (c - d, b)


def abs2_times4(x):
    r = re2(x)
    m = im2_reduced(x)
    return padd(pmul(r, r), pmul(THREE_MINUS_PHI, pmul(m, m)))


def quadrant(x):
    """0,1,2,3 for the open quadrants I..IV of the principal embedding."""
    sr = psign(re2(x))
    si = psign(im2_reduced(x))
    if sr == 0 or si == 0:
        return None
    if sr > 0 and si > 0:
        return 0
    if sr < 0 and si > 0:
        return 1
    if sr < 0 and si < 0:
        return 2
    return 3


# ---------------------------------------------------------------------------
# quintic Jacobi sums
# ---------------------------------------------------------------------------


def primitive_root(p):
    n = p - 1
    fac = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fac.add(d)
            n //= d
        d += 1
    if n > 1:
        fac.add(n)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
        g += 1


def index_table(p, g):
    ind = [0] * p
    x = 1
    for k in range(p - 1):
        ind[x] = k
        x = x * g % p
    return ind


def jacobi_sum(p, ind, power=1):
    """J(chi^power, chi^power) with chi(g) = zeta_5, exact in Z[zeta_5]."""
    c = [0] * 5
    for x in range(2, p):
        c[(power * (ind[x] + ind[(1 - x) % p])) % 5] += 1
    return from_exponents(c)


# ---------------------------------------------------------------------------
# the contrast avatar: the modulus generator w_p in Z[phi]
# ---------------------------------------------------------------------------


def qform(a, b):
    """|sigma_1(a+b phi)|^2 + |sigma_2(a+b phi)|^2 = 2a^2 + 2ab + 3b^2."""
    return 2 * a * a + 2 * a * b + 3 * b * b


def qbil(u, v):
    (a, b), (c, d) = u, v
    return 2 * a * c + (a * d + b * c) + 3 * b * d


def shortest_generator(p, r):
    """shortest vector of the ideal (p, phi - r) under the positive definite
    form qform; it has norm exactly +-p, hence generates the ideal."""
    u, v = (p, 0), (-r, 1)
    while True:
        if qform(*u) > qform(*v):
            u, v = v, u
        qu = qform(*u)
        n = qbil(u, v)
        k = (2 * n + qu) // (2 * qu)  # nearest integer to n/qu
        v = (v[0] - k * u[0], v[1] - k * u[1])
        if qform(*v) >= qform(*u):
            return u


def field_norm(a, b):
    return a * a + a * b - b * b


# ---------------------------------------------------------------------------


FAILS = []


def gate(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    line = "%-34s %s" % (name, tag)
    if detail:
        line += "  " + detail
    print(line)


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]


def main():
    print("C-JACOBI-PHASE-CROSS-1 micro-selftest (NON-CANONICAL)")
    print("exact arithmetic in Z[zeta_5] and Z[phi]; no float in any gate")
    print("")

    # --- S0: ring and Galois sanity -------------------------------------
    z5 = ONE
    for _ in range(5):
        z5 = mul(z5, ZETA)
    ok = z5 == ONE
    phi5 = ONE
    for k in range(1, 5):
        e = [0] * 5
        e[k] = 1
        phi5 = add(phi5, from_exponents(e))
    ok = ok and phi5 == (0, 0, 0, 0)
    gate("S0a ring zeta^5=1, Phi_5(zeta)=0", ok)

    ok = True
    probes = [ONE, ZETA, (1, 0, 1, 0), (3, -1, 4, -2), (0, 0, 0, 1)]
    for s in (1, 2, 3, 4):
        for t in (1, 2, 3, 4):
            for x in probes:
                if gal(gal(x, s), t) != gal(x, (s * t) % 5):
                    ok = False
        for x in probes:
            for y in probes:
                if gal(mul(x, y), s) != mul(gal(x, s), gal(y, s)):
                    ok = False
    gate("S0b sigma_a ring homs, composition", ok)

    # conjugation acts as complex conjugation on the principal embedding
    ok = True
    for x in probes:
        if psign(re2(conj(x))) != psign(re2(x)):
            ok = False
        if psign(im2_reduced(conj(x))) != -psign(im2_reduced(x)):
            ok = False
    gate("S0c sigma_4 = complex conjugation", ok)

    # J = 1 + zeta^2, the axiom: N(J) = 1, |J| = 1/phi, arg J = 2 pi/5
    J_axiom = (1, 0, 1, 0)
    ok = norm(J_axiom) == ONE
    ok = ok and quadrant(J_axiom) == 0
    # 4|J|^2 = 4/phi^2 = 4(2 - phi)
    ok = ok and abs2_times4(J_axiom) == (8, -4)
    gate("S0d axiom J=1+zeta^2, N=1, |J|=1/phi", ok)

    # --- S1..S7: the Jacobi sums ----------------------------------------
    small = primes_upto(500)
    test_primes = [p for p in small if p % 5 == 1]
    # frozen large anchors, each verified prime by the sieve below
    big = [1021, 3001, 10061, 29921]
    large = set(primes_upto(30000))
    for p in big:
        if p not in large or p % 5 != 1:
            raise SystemExit("anchor %d is not a prime = 1 mod 5" % p)
    test_primes = test_primes + big
    print("")
    print("test primes p = 1 mod 5: %d values, min %d, max %d"
          % (len(test_primes), min(test_primes), max(test_primes)))
    print("")

    s1 = s2 = s3 = s4 = s5 = s6 = s7 = True
    lam = sub(ONE, ZETA)
    lam2 = mul(lam, lam)
    nlam2 = norm(lam2)[0]
    for p in test_primes:
        g = primitive_root(p)
        ind = index_table(p, g)
        Jp = jacobi_sum(p, ind)

        # S1  J * conj(J) = p exactly
        if mul(Jp, conj(Jp)) != (p, 0, 0, 0):
            s1 = False
        # S2  N(J) = p^2
        if norm(Jp) != (p * p, 0, 0, 0):
            s2 = False
        # S3  every embedding sits on the critical circle: |sigma_a J|^2 = p
        for a in (1, 2, 3, 4):
            if mul(gal(Jp, a), conj(gal(Jp, a))) != (p, 0, 0, 0):
                s3 = False
        # S4  the other quintic characters give the Galois conjugates
        for a in (1, 2, 3, 4):
            if jacobi_sum(p, ind, a) != gal(Jp, a):
                s4 = False
        # S5  J = -1 mod (1 - zeta)^2
        t = sub(Jp, (-1, 0, 0, 0))
        num = t
        for s in (2, 3, 4):
            num = mul(num, gal(lam2, s))
        if any(x % nlam2 for x in num):
            s5 = False
        # S7  independent check of the exact Re/Im machinery:
        #     4 |sigma_a J|^2 = 4p in Z[phi], and the quadrant is well defined
        for a in (1, 2, 3, 4):
            if abs2_times4(gal(Jp, a)) != (4 * p, 0):
                s7 = False
            if quadrant(gal(Jp, a)) is None:
                s7 = False

        # S6  contrast: the modulus avatar w_p is never on the critical circle
        s5mod = pow(g, ind[5] // 2, p) if ind[5] % 2 == 0 else None
        if s5mod is None or pow(s5mod, 2, p) != 5 % p:
            s6 = False
            continue
        inv2 = pow(2, p - 2, p)
        r = min((1 + s5mod) * inv2 % p, (1 - s5mod) * inv2 % p)
        a, b = shortest_generator(p, r)
        if abs(field_norm(a, b)) != p:
            s6 = False
        # |sigma_1(w)|^2 = (a^2+b^2) + (2ab+b^2) phi ; compare with p
        A2 = (a * a + b * b, 2 * a * b + b * b)
        if pcmp(A2, (p, 0)) == 0:
            s6 = False

    gate("S1 J * conj(J) = p in Z[zeta_5]", s1)
    gate("S2 N(J) = p^2", s2)
    gate("S3 |sigma_a J|^2 = p, all a", s3)
    gate("S4 J(chi^a,chi^a) = sigma_a(J)", s4)
    gate("S5 J = -1 mod (1-zeta)^2", s5)
    gate("S6 w_p never on the critical circle", s6)
    gate("S7 4|sigma_a J|^2 = 4p via (3-phi)", s7)

    # --- the headline statement -----------------------------------------
    print("")
    print("rapidity vector of J_p, eta_a = (1/2) log(|sigma_a J_p|^2 / p):")
    print("  |sigma_a J_p|^2 - p = 0 exactly in Z for every a and every")
    print("  tested p, hence eta(J_p) = (0, 0, 0, 0) exactly.")
    print("")
    print("worked witness, smallest split prime:")
    p = 11
    g = primitive_root(p)
    Jp = jacobi_sum(p, index_table(p, g))
    print("  p = %d, least primitive root g = %d, chi(g) = zeta_5" % (p, g))
    print("  J_p = %s in basis (1, zeta, zeta^2, zeta^3)" % (Jp,))
    for a in (1, 2, 3, 4):
        sa = gal(Jp, a)
        print("  sigma_%d(J_p) = %-16s |.|^2 = %s  quadrant = %d"
              % (a, str(sa), mul(sa, conj(sa))[0], quadrant(sa) + 1))
    print("")
    if FAILS:
        print("RESULT FAIL: " + ", ".join(FAILS))
        raise SystemExit(1)
    print("RESULT PASS: all gates")


if __name__ == "__main__":
    main()
