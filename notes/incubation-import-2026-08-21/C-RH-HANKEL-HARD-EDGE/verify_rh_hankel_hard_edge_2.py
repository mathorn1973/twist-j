#!/usr/bin/env python3
# verify_rh_hankel_hard_edge_2.py
# P-RH-HANKEL-HARD-EDGE-2: successor probe, fork B. Identical double gate
# to HE-1, single scale change c_d = (33/4) d + 21, affine family only,
# plus the extended-range Fourier DATA-SCAN and the detection-ceiling
# table T*(d). Parent pins in PREREG-P-RH-HANKEL-HARD-EDGE-2.md.
# Python standard library only. Every assertion uses int or Fraction.
# Floats never appear anywhere in this file. Deterministic output.
#
# Env: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
import sys
from fractions import Fraction as Fr
from math import gcd

CHECKS = []


def report(name, ok):
    CHECKS.append((name, ok))
    print("%s: %s" % (name, "PASS" if ok else "FAIL"))


def dec6(fr):
    n = fr.numerator
    d = fr.denominator
    if n == 0:
        return "0"
    sgn = "-" if n < 0 else "+"
    n = abs(n)
    shift = 7 - (len(str(n)) - len(str(d)))
    def mant(sh):
        if sh >= 0:
            return (n * 10 ** sh) // d
        return n // (d * 10 ** (-sh))
    m = mant(shift)
    while m < 10 ** 6:
        shift += 1
        m = mant(shift)
    while m >= 10 ** 7:
        shift -= 1
        m = mant(shift)
    s = str(m)
    return "%s%s.%se%+d" % (sgn, s[0], s[1:7], 6 - shift)


def pstrip(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return pstrip([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                   for i in range(n)])


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] += x * y
    return pstrip(r)


def pscale(a, s):
    return pstrip([x * s for x in a])


def pderiv(p):
    if len(p) == 1:
        return [0]
    return pstrip([p[i] * i for i in range(1, len(p))])


def to_int(p):
    dens = [Fr(x).denominator for x in p]
    L = 1
    for q in dens:
        L = L // gcd(L, q) * q
    ints = [int(Fr(x) * L) for x in p]
    g = 0
    for x in ints:
        g = gcd(g, abs(x))
    if g > 1:
        ints = [x // g for x in ints]
    return pstrip(ints)


def sign_at(p, x):
    u = x.numerator
    w = x.denominator
    n = len(p) - 1
    acc = 0
    wp = 1
    for i in range(n, -1, -1):
        acc = acc * u + p[i] * wp
        if i > 0:
            wp *= w
    return (acc > 0) - (acc < 0)


def sign_inf(p):
    c = p[-1]
    return (c > 0) - (c < 0)


def poly_mod(f, g):
    r = [Fr(x) for x in f]
    glist = [Fr(x) for x in g]
    lg = glist[-1]
    while len(r) >= len(glist) and not (len(r) == 1 and r[0] == 0):
        q = r[-1] / lg
        shift = len(r) - len(glist)
        for i in range(len(glist)):
            r[shift + i] -= q * glist[i]
        r = pstrip(r)
        if len(r) == 1 and r[0] == 0:
            break
    return r


def sturm_chain(p_int):
    chain = [list(p_int), to_int(pderiv(p_int))]
    while True:
        f, g = chain[-2], chain[-1]
        if len(g) == 1 and g[0] == 0:
            chain.pop()
            break
        r = poly_mod(f, g)
        if len(r) == 1 and r[0] == 0:
            break
        r = [-x for x in r]
        chain.append(to_int(r))
        if len(chain[-1]) == 1:
            break
    return chain


def variations(signs):
    v = 0
    prev = 0
    for s in signs:
        if s == 0:
            continue
        if prev != 0 and s != prev:
            v += 1
        prev = s
    return v


def V_at(chain, x):
    return variations([sign_at(p, x) for p in chain])


def V_inf(chain):
    return variations([sign_inf(p) for p in chain])


def count_open_inf(chain, a):
    return V_at(chain, a) - V_inf(chain)


def count_in(chain, a, b):
    return V_at(chain, a) - V_at(chain, b)


def iroot_ceil(n, k):
    if n <= 1:
        return n
    lo, hi = 1, 1
    while hi ** k < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** k >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def root_bound(p):
    n = len(p) - 1
    cn = abs(p[-1])
    best = 1
    for i in range(n):
        ci = abs(p[i])
        if ci == 0:
            continue
        ratio = -(-ci // cn)
        r = iroot_ceil(ratio, n - i) + 1
        if r > best:
            best = r
    return Fr(2 * best)


def isolate(chain, G, a, b, depth=0):
    k = count_in(chain, a, b)
    if k == 0:
        return []
    if k == 1:
        return [(a, b)]
    if depth > 300:
        raise RuntimeError("isolation depth exceeded")
    m = (a + b) / 2
    bump = (b - a) / 10 ** 9
    tries = 0
    while sign_at(G, m) == 0:
        m = m + bump
        tries += 1
        if tries > 50:
            raise RuntimeError("cannot avoid root at midpoint")
    return isolate(chain, G, a, m, depth + 1) + isolate(chain, G, m, b, depth + 1)


MMAX = 99


def build_R():
    theta = [[Fr(1)], [Fr(1), Fr(1)]]
    for m in range(2, MMAX + 1):
        t = pscale(theta[m - 1], Fr(2 * m - 1))
        x2 = [Fr(0), Fr(0)] + theta[m - 2]
        theta.append(padd(t, x2))
    R = []
    fact = 1
    for m in range(MMAX + 1):
        if m > 0:
            fact *= m
        R.append(pscale(theta[m], Fr(1, 2 ** m * fact)))
    return R


def R_closed(m):
    from math import factorial
    return [Fr(factorial(2 * m - k) * 2 ** k,
               4 ** m * factorial(m) * factorial(k) * factorial(m - k))
            for k in range(m + 1)]


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cdiv(x, y):
    d = y[0] * y[0] + y[1] * y[1]
    return ((x[0] * y[0] + x[1] * y[1]) / d, (x[1] * y[0] - x[0] * y[1]) / d)


def cpolyval(p, z):
    acc = (Fr(0), Fr(0))
    for c in reversed(p):
        acc = cmul(acc, z)
        acc = cadd(acc, (Fr(c), Fr(0)))
    return acc


def V_value(alpha2, c, P):
    c2 = (c * c, Fr(0))
    den = (c2[0] - alpha2[0], -alpha2[1])
    q = cdiv(c2, den)
    two_minus_q = (2 - q[0], -q[1])
    Pq = cpolyval(P, q)
    val = cmul(cmul(q, two_minus_q), cmul(Pq, Pq))
    return 2 * val[0]


DSET = [2, 4, 8, 16, 24]
EXTD = [32, 48]
CEILD = [8, 16, 24, 32, 48]
LOG2_LO = Fr(693147, 10 ** 6)
LOG2_HI = Fr(693148, 10 ** 6)
SQRT2_LO = Fr(14142, 10 ** 4)
SQRT2_HI = Fr(14143, 10 ** 4)
THETAS = [Fr(0), Fr(-399, 100), Fr(-19599, 100), Fr(-575, 16)]
ALPHAS = [
    ("alpha1", Fr(1, 10), Fr(2)),
    ("alpha2", Fr(1, 10), Fr(14)),
    ("alpha3", Fr(1, 4), Fr(6)),
]
MATCH = {"alpha1": Fr(-399, 100), "alpha2": Fr(-19599, 100),
         "alpha3": Fr(-575, 16)}
DELTAS = [Fr(1, 10), Fr(1, 4)]


def cscale(d):
    return Fr(33, 4) * d + 21


def members(d):
    c = cscale(d)
    out = []
    out.append(("F0", "-", [Fr(0)] * d + [Fr(1)]))
    for th in THETAS:
        a = 1 + th / (c * c)
        out.append(("F1", str(th), [Fr(0)] * d + [-a, Fr(1)]))
    return out


def gate_G(P, R):
    k = pmul([Fr(0), Fr(2), Fr(-1)], pmul(P, P))
    G = [Fr(0)]
    for m in range(1, len(k)):
        if k[m] != 0:
            G = padd(G, pscale(R[m - 1], k[m]))
    return to_int(G)


def gate_b(P, d, R):
    c = cscale(d)
    Gi = gate_G(P, R)
    xlo = c * LOG2_LO
    xhi = c * LOG2_HI
    if sign_inf(Gi) >= 0:
        return ("FAIL", -1, "leading sign nonnegative")
    chain = sturm_chain(Gi)
    a_cnt = xlo
    if sign_at(Gi, a_cnt) == 0:
        a_cnt = a_cnt + Fr(1, 10 ** 12)
    nroots = count_open_inf(chain, a_cnt)
    samples = [xlo, xhi]
    if nroots > 0:
        B = root_bound(Gi)
        if B <= a_cnt:
            B = a_cnt + 1
        while count_in(chain, a_cnt, B) < nroots:
            B = B * 2
        ivs = isolate(chain, Gi, a_cnt, B)
        ivs.sort(key=lambda t: t[0])
        for (u, v) in ivs:
            samples.append(v)
    pos_pts = [x for x in samples if sign_at(Gi, x) > 0]
    if not pos_pts:
        return ("PASS", nroots, "")
    if any(x >= xhi for x in pos_pts):
        return ("FAIL", nroots, "positive at or beyond xhi")
    return ("AMBIGUOUS", nroots, "positive only in gray zone")


def main():
    print("P-RH-HANKEL-HARD-EDGE-2 verifier")
    print("successor of HE-1, fork B: affine family, hard edge"
          " c_d = (33/4) d + 21")
    print("D = {2,4,8,16,24}, EXT data-scan d in {32,48},"
          " ceiling grid T = k/2, k = 1..100")

    # CHECK 0
    ok = True
    ok &= SQRT2_LO * SQRT2_LO < 2 < SQRT2_HI * SQRT2_HI
    K = 30
    def exp_lower(x):
        s = Fr(0)
        t = Fr(1)
        for k in range(K + 1):
            s += t
            t = t * x / (k + 1)
        return s
    def exp_upper(x):
        from math import factorial
        return exp_lower(x) + x ** (K + 1) / (factorial(K + 1) * (1 - x))
    ok &= exp_upper(LOG2_LO) < 2
    ok &= exp_lower(LOG2_HI) > 2
    ok &= 33 * LOG2_LO > 16 * SQRT2_HI
    report("CHECK 0 enclosures and kappa witness", bool(ok))

    # CHECK 1
    R = build_R()
    ok = True
    for m in range(MMAX + 1):
        ok &= R[m] == R_closed(m)
    report("CHECK 1 Bessel R_m recurrence equals closed form, m<=99", bool(ok))

    # CHECK 2
    from math import comb
    ok = R[0] == [Fr(1)]
    ok &= R[1] == [Fr(1, 2), Fr(1, 2)]
    for m in range(MMAX + 1):
        ok &= R[m][0] == Fr(comb(2 * m, m), 4 ** m)
    report("CHECK 2 Fourier spot identities", bool(ok))

    # CHECK 3: Gate B certificates on D
    verdicts = {}
    for d in DSET:
        for (fam, tag, P) in members(d):
            v, nr, note = gate_b(P, d, R)
            verdicts[(fam, tag, d)] = v
            extra = (" note=" + note.replace(" ", "_")) if note else ""
            print("GATEB family=%s theta=%s d=%d verdict=%s roots_beyond=%d%s"
                  % (fam, tag, d, v, nr, extra))

    # CHECK 3X: extended DATA-SCAN (never gating)
    for d in EXTD:
        c = cscale(d)
        xlo = c * LOG2_LO
        for th in [Fr(0), Fr(-399, 100)]:
            a = 1 + th / (c * c)
            P = [Fr(0)] * d + [-a, Fr(1)]
            Gi = gate_G(P, R)
            s0 = sign_at(Gi, xlo)
            npos = 0
            first_pos = "NONE"
            for j in range(1, 121):
                x = xlo + Fr(j, 2)
                s = sign_at(Gi, x)
                if s > 0:
                    npos += 1
                    if first_pos == "NONE":
                        first_pos = "j=%d" % j
            print("EXTSCAN family=F1 theta=%s d=%d sign(xlo)=%+d"
                  " grid_pos=%d first_pos=%s leading=%+d"
                  % (th, d, s0, npos, first_pos, sign_inf(Gi)))

    # CHECK 4: Gate A at d = 24, margins, ceiling table
    d24 = 24
    c24 = cscale(d24)
    gate_a = {}
    for (name, de, T) in ALPHAS:
        alpha2 = (de * de - T * T, 2 * de * T)
        for (fam, tag, P) in members(d24):
            V = V_value(alpha2, c24, P)
            s = (V > 0) - (V < 0)
            gate_a[(fam, tag, name)] = V
            print("GATEA d=24 family=%s theta=%s %s V_sign=%+d V~=%s"
                  % (fam, tag, name, s, dec6(V)))
    for (name, de, T) in ALPHAS:
        alpha2 = (de * de - T * T, 2 * de * T)
        th = MATCH[name]
        for d in DSET:
            c = cscale(d)
            a = 1 + th / (c * c)
            P = [Fr(0)] * d + [-a, Fr(1)]
            V = V_value(alpha2, c, P)
            s = (V > 0) - (V < 0)
            print("MARGIN family=F1 %s theta=%s d=%d V_sign=%+d V~=%s"
                  % (name, th, d, s, dec6(V)))
    for de in DELTAS:
        for d in CEILD:
            c = cscale(d)
            n_fail = 0
            t_ff = "NONE"
            for k in range(1, 101):
                T = Fr(k, 2)
                th = de * de - T * T
                a = 1 + th / (c * c)
                P = [Fr(0)] * d + [-a, Fr(1)]
                alpha2 = (th, 2 * de * T)
                V = V_value(alpha2, c, P)
                if V >= 0:
                    n_fail += 1
                    if t_ff == "NONE":
                        t_ff = str(T)
            print("CEILING delta=%s d=%d T_ff=%s n_fail=%d"
                  % (de, d, t_ff, n_fail))

    # CHECK 5: control
    Vc = gate_a[("F0", "-", "alpha1")]
    report("CHECK 5 control F0 alpha1 d=24 V>0", Vc > 0)

    # survival
    okb = all(verdicts[(f, t, d)] == "PASS"
              for (f, t, d) in verdicts if f == "F1")
    oka = True
    for (name, de, T) in ALPHAS:
        oka &= gate_a[("F1", str(MATCH[name]), name)] < 0
    surv = okb and oka
    print("SURVIVAL F1 gateB=%s gateA=%s verdict=%s"
          % ("PASS" if okb else "FAIL", "PASS" if oka else "FAIL",
             "SURVIVES" if surv else "FAILS"))
    print("STOPGATE affine-hard-edge fired=%s" % ("NO" if surv else "YES"))
    if surv:
        print("ROUTE ARMED: step-3 obligation = tail majorant over the"
              " measured ceiling frontier; T2 lane opens next regardless")
    else:
        print("ROUTE CLOSED: [F-bounded, AFFINE HARD EDGE]; T2 lane only")

    npass = sum(1 for (_, o) in CHECKS if o)
    failed = [n for (n, o) in CHECKS if not o]
    print("CHECKS: %d of %d PASS, FAILED: %s"
          % (npass, len(CHECKS), ",".join(failed) if failed else "none"))
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
