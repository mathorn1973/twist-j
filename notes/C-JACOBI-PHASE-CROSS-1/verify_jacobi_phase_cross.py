#!/usr/bin/env python3
"""C-JACOBI-PHASE-CROSS-1 census. NON-CANONICAL.

Joint law of the two integer avatars of a split prime p = 1 mod 5:

    J_p   quintic Jacobi sum in Z[zeta_5]   -> angular datum QUAD, SGN
    w_p   generator of a prime of Z[phi]    -> rapidity datum QUART, H

Every gate, bin boundary and chi-square decision is exact: integer and
Fraction arithmetic only.  Floating point appears exclusively in lines
explicitly labelled "witness".

Decision lines are frozen in PREREG_C-JACOBI-PHASE-CROSS-1.md and are
reproduced verbatim in FROZEN below.

Python 3 standard library only.  Exit 0, empty stderr, deterministic stdout.
"""

from fractions import Fraction

# frozen decision surface, copied from the preregistration
FROZEN = (
    ("T1", "QUAD x H", 4, 2, 3, Fraction(11345, 1000)),
    ("T2", "SGN  x H", 3, 2, 2, Fraction(9210, 1000)),
    ("T3", "QUAD x QUART", 4, 4, 9, Fraction(21666, 1000)),
)
BAND = Fraction(1, 1000)
PMIN, PMAX = 11, 30000

# ---------------------------------------------------------------------------
# Z[zeta_5], basis (1, zeta, zeta^2, zeta^3), zeta^4 = -1 - z - z^2 - z^3
# ---------------------------------------------------------------------------

ONE = (1, 0, 0, 0)


def from_exponents(counts):
    v = counts[4]
    return tuple(counts[t] - v for t in range(4))


def mul(a, b):
    c = [0] * 5
    for i in range(4):
        ai = a[i]
        if ai:
            for j in range(4):
                c[(i + j) % 5] += ai * b[j]
    return from_exponents(c)


def gal(a, s):
    c = [0] * 5
    for i in range(4):
        c[(i * s) % 5] += a[i]
    return from_exponents(c)


def conj(a):
    return gal(a, 4)


# ---------------------------------------------------------------------------
# Z[phi]: pairs (u, v) = u + v phi, phi^2 = phi + 1
# ---------------------------------------------------------------------------


def pmul(x, y):
    (u, v), (s, t) = x, y
    return (u * s + v * t, u * t + v * s + v * t)


def padd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def psub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def sqrt5_sign(s, t):
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
    return sqrt5_sign(2 * x[0] + x[1], x[1])


def pcmp(x, y):
    return psign(psub(x, y))


def pfloat(x):
    """witness only."""
    return x[0] + x[1] * (1 + 5 ** 0.5) / 2


PHI = (0, 1)
PHI2 = (1, 1)
PHI_INV2 = (2, -1)  # phi^-2 = 2 - phi

# ---------------------------------------------------------------------------
# exact Re / Im of the principal embedding
# ---------------------------------------------------------------------------

THREE_MINUS_PHI = (3, -1)


def re2(x):
    a, b, c, d = x
    return (2 * a - b, b - c - d)


def im2_reduced(x):
    a, b, c, d = x
    return (c - d, b)


def abs2_times4(x):
    r = re2(x)
    m = im2_reduced(x)
    return padd(pmul(r, r), pmul(THREE_MINUS_PHI, pmul(m, m)))


def quadrant(x):
    sr = psign(re2(x))
    si = psign(im2_reduced(x))
    if sr == 0 or si == 0:
        return None
    if sr > 0:
        return 0 if si > 0 else 3
    return 1 if si > 0 else 2


# ---------------------------------------------------------------------------
# arithmetic helpers
# ---------------------------------------------------------------------------


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if s[i]:
            s[i * i:: i] = bytearray(len(s[i * i:: i]))
        i += 1
    return [i for i in range(2, n + 1) if s[i]]


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


def qform(a, b):
    return 2 * a * a + 2 * a * b + 3 * b * b


def qbil(u, v):
    (a, b), (c, d) = u, v
    return 2 * a * c + (a * d + b * c) + 3 * b * d


def shortest_generator(p, r):
    u, v = (p, 0), (-r, 1)
    while True:
        if qform(*u) > qform(*v):
            u, v = v, u
        qu = qform(*u)
        k = (2 * qbil(u, v) + qu) // (2 * qu)
        v = (v[0] - k * u[0], v[1] - k * u[1])
        if qform(*v) >= qform(*u):
            return u


# ---------------------------------------------------------------------------
# per-prime record
# ---------------------------------------------------------------------------

FAILS = []


def fail(name):
    if name not in FAILS:
        FAILS.append(name)


def record(p):
    g = primitive_root(p)
    ind = [0] * p
    x = 1
    for k in range(p - 1):
        ind[x] = k
        x = x * g % p

    # phase avatar
    c = [0] * 5
    for x in range(2, p):
        c[(ind[x] + ind[(1 - x) % p]) % 5] += 1
    Jp = from_exponents(c)
    if mul(Jp, conj(Jp)) != (p, 0, 0, 0):
        fail("G1 |J_p|^2 = p")
    if abs2_times4(Jp) != (4 * p, 0):
        fail("G2 4|J_p|^2 = 4p via (3-phi)")
    q = quadrant(Jp)
    if q is None:
        fail("G3 quadrant well defined")
        q = 0
    s1 = psign(re2(Jp))
    s2 = psign(re2(gal(Jp, 2)))
    if s1 == 0 or s2 == 0:
        fail("G4 SGN well defined")
    sgn = {2: 0, 0: 1, -2: 2}[s1 + s2]

    # modulus avatar
    if ind[5] % 2:
        fail("G5 5 is a square mod p")
        return None
    t = pow(g, ind[5] // 2, p)
    if pow(t, 2, p) != 5 % p:
        fail("G5 5 is a square mod p")
        return None
    inv2 = pow(2, p - 2, p)
    r = min((1 + t) * inv2 % p, (1 - t) * inv2 % p)
    if (r * r - r - 1) % p:
        fail("G6 r_p is a root of x^2-x-1")
    a, b = shortest_generator(p, r)
    if abs(a * a + a * b - b * b) != p:
        fail("G7 |N(w_p)| = p")
    A2 = (a * a + b * b, 2 * a * b + b * b)
    if psign(A2) <= 0:
        fail("G8 A2 > 0")
    guard = 0
    while pcmp(A2, (p, 0)) < 0:
        A2 = pmul(A2, PHI2)
        guard += 1
        if guard > 200:
            fail("G9 normalization terminates")
            break
    while pcmp(A2, pmul((p, 0), PHI2)) >= 0:
        A2 = pmul(A2, PHI_INV2)
        guard += 1
        if guard > 200:
            fail("G9 normalization terminates")
            break
    if pcmp(A2, (p, 0)) < 0 or pcmp(A2, pmul((p, 0), PHI2)) >= 0:
        fail("G10 A2 in [p, p phi^2)")
    if pcmp(A2, (p, 0)) == 0:
        fail("G11 w_p off the critical circle")

    # quartile of eta in [0, L): compare Y = A2^2 with p^2 phi^j
    Y = pmul(A2, A2)
    p2 = (p * p, 0)
    quart = None
    ladder = [p2]
    for _ in range(4):
        ladder.append(pmul(ladder[-1], PHI))
    for j in range(4):
        if pcmp(Y, ladder[j]) >= 0 and pcmp(Y, ladder[j + 1]) < 0:
            quart = j
    if quart is None:
        fail("G12 quartile well defined")
        quart = 0
    h = 0 if quart < 2 else 1
    return q, sgn, quart, h


# ---------------------------------------------------------------------------
# exact Pearson chi-square
# ---------------------------------------------------------------------------


def chisq(table):
    rows = len(table)
    cols = len(table[0])
    n = sum(sum(r) for r in table)
    rt = [sum(r) for r in table]
    ct = [sum(table[i][j] for i in range(rows)) for j in range(cols)]
    stat = Fraction(0)
    minexp = None
    for i in range(rows):
        for j in range(cols):
            e = Fraction(rt[i] * ct[j], n)
            if minexp is None or e < minexp:
                minexp = e
            if e == 0:
                continue
            d = Fraction(table[i][j]) - e
            stat += d * d / e
    return stat, minexp


def decide(stat, minexp, crit):
    if minexp < 5:
        return "VOID (expected cell < 5)"
    if abs(stat - crit) <= BAND:
        return "VOID (inside rounding band)"
    if stat > crit + BAND:
        return "REJECT independence"
    return "NOT-REJECTED"


def show_table(title, rlab, clab, table):
    print("  " + title)
    w = max(len(s) for s in rlab) + 1
    print("    " + " " * w + "".join("%8s" % s for s in clab) + "%9s" % "total")
    for i, r in enumerate(table):
        print("    " + rlab[i].ljust(w) + "".join("%8d" % v for v in r)
              + "%9d" % sum(r))
    tot = [sum(table[i][j] for i in range(len(table))) for j in range(len(clab))]
    print("    " + "total".ljust(w) + "".join("%8d" % v for v in tot)
          + "%9d" % sum(tot))


# ---------------------------------------------------------------------------


def main():
    print("C-JACOBI-PHASE-CROSS-1 census (NON-CANONICAL)")
    print("frozen surface: PREREG_C-JACOBI-PHASE-CROSS-1.md")
    print("exact arithmetic in Z[zeta_5], Z[phi], Fraction; floats are"
          " witnesses only")
    print("")

    carrier = [p for p in primes_upto(PMAX) if p % 5 == 1 and p >= PMIN]
    print("carrier: p = 1 mod 5, %d <= p <= %d, count %d, first %d, last %d"
          % (PMIN, PMAX, len(carrier), carrier[0], carrier[-1]))
    print("")

    t1 = [[0] * 2 for _ in range(4)]
    t2 = [[0] * 2 for _ in range(3)]
    t3 = [[0] * 4 for _ in range(4)]
    for p in carrier:
        rec = record(p)
        if rec is None:
            continue
        q, sgn, quart, h = rec
        t1[q][h] += 1
        t2[sgn][h] += 1
        t3[q][quart] += 1

    if FAILS:
        print("EXACT GATES FAIL: " + ", ".join(FAILS))
        raise SystemExit(1)
    print("exact gates G1..G12: PASS on all %d carrier primes" % len(carrier))
    print("  G1  |J_p|^2 = p in Z[zeta_5]        (Weil, phase avatar)")
    print("  G2  4|J_p|^2 = 4p via 3 - phi        (Re/Im machinery audit)")
    print("  G3  quadrant of sigma_1(J_p) open    (no axis case)")
    print("  G7  |N(w_p)| = p                     (shortest vector generates)")
    print("  G10 eta_p normalized into [0, L)")
    print("  G11 w_p never on the critical circle (the cross is nondegenerate)")
    print("")

    qlab = ["QI", "QII", "QIII", "QIV"]
    slab = ["(+,+)", "mixed", "(-,-)"]
    hlab = ["h=0", "h=1"]
    klab = ["k=0", "k=1", "k=2", "k=3"]

    print("marginals")
    print("  QUAD  " + "  ".join("%s=%d" % (qlab[i], sum(t1[i]))
                                 for i in range(4)))
    print("  SGN   " + "  ".join("%s=%d" % (slab[i], sum(t2[i]))
                                 for i in range(3)))
    print("  H     " + "  ".join("%s=%d" % (hlab[j],
                                            sum(t1[i][j] for i in range(4)))
                                 for j in range(2)))
    print("  QUART " + "  ".join("%s=%d" % (klab[j],
                                            sum(t3[i][j] for i in range(4)))
                                 for j in range(4)))
    print("")

    for (name, title, _, _, df, crit), table, rlab, clab in (
        (FROZEN[0], t1, qlab, hlab),
        (FROZEN[1], t2, slab, hlab),
        (FROZEN[2], t3, qlab, klab),
    ):
        print("%s  %s" % (name, title))
        show_table("contingency", rlab, clab, table)
        stat, minexp = chisq(table)
        print("    X^2 exact      = %d / %d" % (stat.numerator,
                                                stat.denominator))
        print("    X^2 witness    = %.6f   (float, witness only)"
              % float(stat))
        print("    min expected   = %d / %d" % (minexp.numerator,
                                                minexp.denominator))
        print("    df             = %d" % df)
        print("    frozen crit    = %s" % str(crit))
        print("    DECISION       = %s" % decide(stat, minexp, crit))
        print("")

    print("phase avatar rapidity: eta(J_p) = (0,0,0,0) exactly, every p"
          " (gate G1).")
    print("modulus avatar rapidity: eta(w_p) != 0, every p (gate G11).")
    print("RESULT PASS: all exact gates; decisions as printed above")


if __name__ == "__main__":
    main()
