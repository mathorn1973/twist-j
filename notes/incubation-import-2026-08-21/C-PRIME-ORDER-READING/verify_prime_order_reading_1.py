# verify_prime_order_reading_1.py
# C-PRIME-ORDER-READING-1, stage A audit of PROP-1.
# Frozen spec: PREREG-C-PRIME-ORDER-READING-1.md
#   sha256 6f90df5d23c8900c80a08c69a06eb70279a8692f18cb53365566320e58cfee21
# with ADDENDUM 1 (corrected path B)
#   sha256 ecc770bf9387834f2d5b98707b355b3aaced51efe83e6d7425694d169268f735
# Python standard library only. Exact integers only. No float anywhere.
# Elements of Z[phi] are pairs (a, b) meaning a + b*phi, phi^2 = phi + 1.

import sys
from math import isqrt

LIMIT = 2000
BWIN = 200          # enumeration window bound, per ADDENDUM 1
NCONTROL = 10       # negative-control primes, per Field 2

def mul(x, y):
    a1, b1 = x
    a2, b2 = y
    return (a1 * a2 + b1 * b2, a1 * b2 + a2 * b1 + b1 * b2)

def sigma(x):
    a, b = x
    return (a + b, -b)

def norm(x):
    a, b = x
    return a * a + a * b - b * b

def tr(x):
    a, b = x
    return 2 * a + b

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def scale(x, c):
    return (x[0] * c, x[1] * c)

def mag(x):
    return max(abs(x[0]), abs(x[1]))

PHI = (0, 1)
PHIINV = (-1, 1)    # phi^-1 = phi - 1

def sqrt_exact(n):
    if n < 0:
        return None
    r = isqrt(n)
    return r if r * r == n else None

# ---- generator construction, path 1: bounded Pell sweep -------------------

def gen_pell(p):
    b = 0
    while True:
        for s in (p, -p):
            d = 5 * b * b + 4 * s
            r = sqrt_exact(d)
            if r is None:
                continue
            for pm in (r, -r):
                if (-b + pm) % 2 == 0:
                    w = ((-b + pm) // 2, b)
                    if abs(norm(w)) == p:
                        return w
        b += 1

# ---- generator construction, path 2: Euclidean gcd ------------------------

def divstep(x, y):
    n = norm(y)
    z = mul(x, sigma(y))            # x / y = z / n exactly

    def rnd(num, den):
        if den < 0:
            num, den = -num, -den
        return (2 * num + den) // (2 * den)

    q = (rnd(z[0], n), rnd(z[1], n))
    r = sub(x, mul(q, y))
    return q, r

def gen_gcd(p):
    k = next(k for k in range(p) if (k * k - k - 1) % p == 0)
    x, y = (p, 0), (k, -1)          # gcd(p, k - phi)
    steps = 0
    while y != (0, 0):
        q, r = divstep(x, y)
        assert abs(norm(r)) < abs(norm(y)), "division step not norm-decreasing"
        x, y = y, r
        steps += 1
    assert abs(norm(x)) == p, "gcd generator has wrong norm"
    return x, steps

# ---- path A: divisibility test (frozen Field 2) ---------------------------

def collide_div(y, n):
    y2 = mul(y, y)
    return y2[0] % n == 0 and y2[1] % n == 0

# ---- path B: exponent enumeration with certified window (ADDENDUM 1) ------

def collide_enum(y, n):
    y2 = mul(y, y)
    m2 = mag(y2)
    for base in (PHI, PHIINV):      # m >= 0 and m < 0
        t = (n, 0)                  # phi^0 * n
        m = 0
        while True:
            if y2 == t or y2 == neg(t):
                return True
            if mag(t) > m2:
                break               # certified crossing: monotone beyond
            m += 1
            assert m <= BWIN, "enumeration window exceeded"
            t = mul(t, base)
    return False

# ---- path B companion: reduced-tuple comparison (non-vacuous uses only) ---

def orbit_rep(w):
    best = None
    for start in (w, neg(w)):
        x = start
        for base in (PHI, PHIINV):
            x = start
            for _ in range(2 * BWIN):
                key = (abs(tr(x)), x[0], x[1])
                if best is None or key < best[0]:
                    best = (key, x)
                if mag(x) > 4 * mag(w) + 10 ** 6:
                    break
                x = mul(x, base)
    return best[1]

def same_orbit(u, v):
    return orbit_rep(u) == orbit_rep(v)

# ---- main -----------------------------------------------------------------

def main():
    fails = 0
    out = []

    def gate(name, ok, detail):
        nonlocal fails
        if not ok:
            fails += 1
        out.append("%s %s %s" % (name, detail, "PASS" if ok else "FAIL"))

    primes = []
    sieve = [True] * LIMIT
    for i in range(2, LIMIT):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, LIMIT, i):
                sieve[j] = False
    split = [p for p in primes if p % 5 in (1, 4)]
    gate("G1 split census below 2000:", len(split) == 146, "%d" % len(split))

    W1, W2 = {}, {}
    ok2 = True
    for p in split:
        W1[p] = gen_pell(p)
        assert abs(norm(W1[p])) == p
        W2[p], _ = gen_gcd(p)
    gate("G2 pell generators |N|=p:", all(abs(norm(W1[p])) == p for p in split),
         "%d/%d" % (len(split), len(split)))
    gate("G3 gcd generators |N|=p, norm-decreasing:", True,
         "%d/%d" % (len(split), len(split)))

    diag_ok = 0
    for p in split:
        n = p * p
        d = collide_div(mul(W1[p], sigma(W2[p])), n)
        c = collide_div(mul(W1[p], W2[p]), n)
        e_d = collide_enum(mul(W1[p], sigma(W2[p])), n)
        e_c = collide_enum(mul(W1[p], W2[p]), n)
        if (d != c) and (d == e_d) and (c == e_c) \
                and d == same_orbit(W1[p], W2[p]) \
                and c == same_orbit(W1[p], sigma(W2[p])):
            diag_ok += 1
    gate("G4 diagonal exactly-one-match, three-way agreement:",
         diag_ok == len(split), "%d/%d" % (diag_ok, len(split)))

    ctrl_ok = 0
    ctrl_total = 0
    for p in split[:NCONTROL]:
        w = W1[p]
        n = p * p
        cases = [
            mul(w, sigma(w)),            # (w, w) direct: y = N(w), rational
            mul(w, sigma(mul(PHI, w))),  # (w, phi w) direct
            (norm(w), 0),                # rational witness y = N(w)
        ]
        for y in cases:
            ctrl_total += 1
            if collide_div(y, n) and collide_enum(y, n):
                ctrl_ok += 1
        if not same_orbit(w, mul(PHI, w)):
            ctrl_ok -= 1
    gate("G5 negative controls fired both paths:",
         ctrl_ok == ctrl_total, "%d/%d" % (ctrl_ok, ctrl_total))

    tests = 0
    coll_a = 0
    coll_b = 0
    agree = 0
    for i in range(len(split)):
        for j in range(i + 1, len(split)):
            p, q = split[i], split[j]
            n = p * q
            for y in (mul(W1[p], sigma(W1[q])), mul(W1[p], W1[q])):
                tests += 1
                a = collide_div(y, n)
                b = collide_enum(y, n)
                if a:
                    coll_a += 1
                if b:
                    coll_b += 1
                if a == b:
                    agree += 1
    gate("G6 pair audit path A collisions:", coll_a == 0,
         "%d/%d" % (coll_a, tests))
    gate("G7 pair audit path B collisions and agreement:",
         coll_b == 0 and agree == tests,
         "%d/%d agree %d/%d" % (coll_b, tests, agree, tests))

    fp = 0
    fp_agree = 0
    for p in split:
        w = W1[p]
        a = collide_div(mul(w, w), p)
        b = collide_enum(mul(w, w), p)
        c = same_orbit(w, sigma(w))
        if a or b or c:
            fp += 1
        if a == b == c:
            fp_agree += 1
    gate("G8 fixed points, three-way agreement:",
         fp == 0 and fp_agree == len(split),
         "%d/%d agree %d/%d" % (fp, len(split), fp_agree, len(split)))

    for line in out:
        sys.stdout.write(line + "\n")
    sys.stdout.write("SUMMARY PASS=%d FAIL=%d\n" % (8 - fails, fails))
    sys.exit(1 if fails else 0)

main()
