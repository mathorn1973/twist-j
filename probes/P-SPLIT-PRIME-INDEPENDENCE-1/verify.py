#!/usr/bin/env python3
# P-SPLIT-PRIME-INDEPENDENCE-1 verifier
# Frozen against PREREG.md in this probe directory. Every check below maps to
# exactly one Field 1 gate clause and the verifier asserts nothing beyond
# them. AUDIT of the written proofs at finite scope; carries no universal
# quantifier. Standard library only, exact integers, no float, no logarithm,
# nothing inexact in any assertion or printed field.
# Elements of Z[phi] are integer pairs (a, b) meaning a + b phi, phi^2 = phi+1.
import sys

PASS = 0
FAIL = 0
INVENTORY = []

BOUND = 120          # split primes below this
BWIN = 200           # hard exponent window for decision path B
STRIDE = 7           # frozen cross-check stride for path B
SHIFT_J = 8          # frozen nonzero shift for the non-vacuity clause
GAUGE_N = 200        # frozen gauge sample size
GAUGE_J = (-2, -1, 1, 3)


def check(name, cond):
    global PASS, FAIL
    INVENTORY.append(name)
    if cond:
        PASS += 1
        sys.stdout.write("PASS %s\n" % name)
    else:
        FAIL += 1
        sys.stdout.write("FAIL %s\n" % name)


# ---------- exact arithmetic in Z[phi] ----------

def mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def conj(x):
    return (x[0] + x[1], -x[1])


def norm(x):
    return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]


def trace(x):
    return 2 * x[0] + x[1]


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def smul(x, c):
    return (x[0] * c, x[1] * c)


def mag(x):
    return max(abs(x[0]), abs(x[1]))


def sgn(x):
    """exact sign of a + b phi under the embedding phi -> (1+sqrt5)/2"""
    A = 2 * x[0] + x[1]
    B = x[1]
    if A == 0 and B == 0:
        return 0
    if A >= 0 and B >= 0:
        return 1
    if A <= 0 and B <= 0:
        return -1
    d = A * A - 5 * B * B
    if A > 0:
        return 1 if d > 0 else -1
    return -1 if d > 0 else 1


ONE = (1, 0)
PHI = (0, 1)
PHIINV = (-1, 1)
PHI2 = (1, 1)
PHI2INV = (2, -1)


def phi_k(k):
    r = ONE
    b = PHI if k >= 0 else PHIINV
    for _ in range(abs(k)):
        r = mul(r, b)
    return r


def phi2_k(k):
    r = ONE
    b = PHI2 if k >= 0 else PHI2INV
    for _ in range(abs(k)):
        r = mul(r, b)
    return r


def isqrt_exact(n):
    if n < 0:
        return None
    r = 0
    bit = 1 << ((n.bit_length() + 1) // 2 * 2)
    while bit > n:
        bit >>= 2
    while bit:
        if n >= r + bit:
            n -= r + bit
            r = (r >> 1) + bit
        else:
            r >>= 1
        bit >>= 2
    return r


def is_square(n):
    if n < 0:
        return None
    r = isqrt_exact(n)
    return r if r * r == n else None


# ---------- even-index Lucas numbers, the registered criterion ----------

def even_lucas(limit):
    out = {}
    a, b = 2, 3          # L_0, L_2
    m = 0
    while a <= limit:
        out[a] = m
        a, b = b, 3 * b - a
        m += 1
    return out


LUCAS_LIMIT = 1 << 200
EVEN_LUCAS = even_lucas(LUCAS_LIMIT)


def is_even_phi_power(w):
    """w integral with N(w)=1. Registered decision: |Tr(w)| must be an
    even-index Lucas number, followed by exact comparison. Returns the
    exponent m with w = +- phi^(2m), or None."""
    if norm(w) != 1:
        return None
    t = abs(trace(w))
    if t not in EVEN_LUCAS:
        return None
    m = EVEN_LUCAS[t]
    for mm in (m, -m):
        p = phi2_k(mm)
        if w == p or w == neg(p):
            return mm
    return None


# ---------- the two decision paths ----------

def cls_zero_A(X, Y):
    """Path A. Decide rho(X)/rho(Y) = +- phi^(2n) by exact divisibility in
    Z[phi] followed by the registered Lucas trace test."""
    U = smul(mul(X, X), norm(Y))
    V = smul(mul(Y, Y), norm(X))
    nv = norm(V)
    if nv == 0:
        return None
    q = mul(U, conj(V))
    if q[0] % nv or q[1] % nv:
        return False
    w = (q[0] // nv, q[1] // nv)
    return is_even_phi_power(w) is not None


def cls_zero_B(X, Y):
    """Path B. Exponent enumeration over the frozen hard window, structurally
    independent of path A: no division and no trace test."""
    U = smul(mul(X, X), norm(Y))
    V = smul(mul(Y, Y), norm(X))
    t = V
    if U == t or U == neg(t):
        return True
    up = V
    dn = V
    for _ in range(BWIN):
        up = mul(up, PHI2)
        if U == up or U == neg(up):
            return True
        dn = mul(dn, PHI2INV)
        if U == dn or U == neg(dn):
            return True
    return False


# ---------- setup ----------

def sieve(limit):
    s = [True] * limit
    out = []
    for i in range(2, limit):
        if s[i]:
            out.append(i)
            for j in range(i * i, limit, i):
                s[j] = False
    return out


def generator_of(p):
    """bounded Diophantine sweep on |a^2 + a b - b^2| = p"""
    b = 0
    while True:
        for s in (p, -p):
            d = 5 * b * b + 4 * s
            r = is_square(d)
            if r is None:
                continue
            for pm in (r, -r):
                if (-b + pm) % 2 == 0:
                    w = ((-b + pm) // 2, b)
                    if abs(norm(w)) == p:
                        return w
        b += 1


def in_half_period(x, p):
    """exact: p/phi < sigma+(x)^2 < p phi, i.e. |eta(x)| < (log phi)/2"""
    sq = mul(x, x)
    lo = (-p, p)
    hi = (0, p)
    return sgn(sub(sq, lo)) > 0 and sgn(sub(hi, sq)) > 0


def on_endpoint(x, p):
    sq = mul(x, x)
    return sq == (-p, p) or sq == (0, p)


def main():
    sys.stdout.write("P-SPLIT-PRIME-INDEPENDENCE-1 verifier\n")
    sys.stdout.write("AUDIT of the written proofs at finite scope; "
                     "no universal quantifier\n")
    sys.stdout.write("exact integers in Z[phi] throughout; no logarithm, "
                     "no float, no numerical eigenvalue\n")

    primes = sieve(BOUND)
    split = [p for p in primes if p % 5 in (1, 4)]
    check("G1.split_census_matches_residue_rule",
          split == [11, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109])

    gens = {}
    ok_norm = True
    for p in split:
        w = generator_of(p)
        gens[p] = w
        if abs(norm(w)) != p:
            ok_norm = False
    check("G1.generators_have_absolute_norm_p", ok_norm)
    check("G1.tested_ideals_are_principal_by_exhibited_generator",
          all(abs(norm(gens[p])) == p for p in split))
    sys.stdout.write("G1 split primes below %d: %d, generators exhibited\n"
                     % (BOUND, len(split)))

    # ---- G2 lucas criterion against direct comparison ----
    ok_lucas = True
    for m in range(-10, 11):
        w = phi2_k(m)
        for ww in (w, neg(w)):
            if is_even_phi_power(ww) != m and is_even_phi_power(ww) != -m:
                ok_lucas = False
        odd = mul(phi2_k(m), PHI)
        if is_even_phi_power(odd) is not None:
            ok_lucas = False
    check("G2.lucas_trace_test_matches_direct_power_comparison", ok_lucas)

    # ---- G3 the relation search, with the G2 cross-check woven in ----
    fams = []
    for p in split:
        fams.append(((p,), 8))
    for i in range(len(split)):
        for j in range(i + 1, len(split)):
            fams.append(((split[i], split[j]), 4))
    for i in range(len(split)):
        for j in range(i + 1, len(split)):
            for k in range(j + 1, len(split)):
                fams.append(((split[i], split[j], split[k]), 2))
    first8 = split[:8]
    for i in range(len(first8)):
        for j in range(i + 1, len(first8)):
            for k in range(j + 1, len(first8)):
                for l in range(k + 1, len(first8)):
                    fams.append(((first8[i], first8[j], first8[k],
                                  first8[l]), 1))

    def vectors(k, B):
        if k == 0:
            yield ()
            return
        for head in range(-B, B + 1):
            for tail in vectors(k - 1, B):
                yield (head,) + tail

    relations = 0
    tests = 0
    cross = 0
    disagree = 0
    for fam, B in fams:
        gs = [gens[p] for p in fam]
        for vec in vectors(len(fam), B):
            if all(m == 0 for m in vec):
                continue
            X = ONE
            Y = ONE
            for g, m in zip(gs, vec):
                if m > 0:
                    for _ in range(m):
                        X = mul(X, g)
                elif m < 0:
                    for _ in range(-m):
                        Y = mul(Y, g)
            tests += 1
            a = cls_zero_A(X, Y)
            if a:
                relations += 1
            if tests % STRIDE == 0 or a:
                cross += 1
                if cls_zero_B(X, Y) != a:
                    disagree += 1
    check("G3.no_integer_relation_in_the_frozen_boxes", relations == 0)
    check("G2.class_zero_decision_two_independent_paths_agree", disagree == 0)
    sys.stdout.write("G3 families %d, coefficient vectors tested %d, "
                     "relations found %d\n" % (len(fams), tests, relations))
    sys.stdout.write("G2 path-B cross-checks %d, disagreements %d\n"
                     % (cross, disagree))

    # ---- G4 positive controls, which MUST fire ----
    ctrl = 0
    fired = 0
    for p in (2, 3, 7, 13, 17, 23, 37, 43):        # inert, residue +-2 mod 5
        if p % 5 in (2, 3):
            ctrl += 1
            if cls_zero_A((p, 0), ONE) and cls_zero_B((p, 0), ONE):
                fired += 1
    ctrl += 1                                        # ramified sqrt5 = 2phi-1
    if cls_zero_A((-1, 2), ONE) and cls_zero_B((-1, 2), ONE):
        fired += 1
    for p in split[:6]:                              # pi times its conjugate
        ctrl += 1
        w = gens[p]
        if cls_zero_A(mul(w, conj(w)), ONE) and cls_zero_B(mul(w, conj(w)),
                                                           ONE):
            fired += 1
    for j in (-3, -1, 1, 2, 5):                      # pure unit powers
        ctrl += 1
        if cls_zero_A(phi_k(j), ONE) and cls_zero_B(phi_k(j), ONE):
            fired += 1
    for p in split[:6]:                              # same class, shifted
        ctrl += 1
        w = gens[p]
        if cls_zero_A(w, mul(w, phi_k(3))) and cls_zero_B(w, mul(w,
                                                                phi_k(3))):
            fired += 1
    check("G4.positive_controls_all_fire", ctrl == fired and ctrl > 0)
    sys.stdout.write("G4 positive controls %d of %d fired under both paths\n"
                     % (fired, ctrl))

    # ---- G5 the reduction and the height content ----
    uniq = True
    endpoint = False
    both_above = True
    height_id = True
    nonvac = True
    red = {}
    for p in split:
        hits = [j for j in range(-40, 41)
                if in_half_period(mul(gens[p], phi_k(j)), p)]
        if len(hits) != 1:
            uniq = False
        r = mul(gens[p], phi_k(hits[0])) if hits else gens[p]
        red[p] = r
        for j in range(-40, 41):
            if on_endpoint(mul(gens[p], phi_k(j)), p):
                endpoint = True
        if not (sgn(sub(mul(r, r), ONE)) > 0
                and sgn(sub(mul(conj(r), conj(r)), ONE)) > 0):
            both_above = False
        if abs(norm(r)) != p:
            height_id = False
        s = mul(r, phi_k(SHIFT_J))
        if sgn(sub(mul(conj(s), conj(s)), ONE)) > 0:
            nonvac = False
    check("G5.reduced_representative_exists_and_is_unique", uniq)
    check("G5.half_period_endpoint_never_attained", not endpoint)
    check("G5.reduced_generator_has_both_embeddings_above_one", both_above)
    check("G5.height_identity_product_of_embeddings_equals_p", height_id)
    check("G5.unreduced_generator_fails_the_embedding_test", nonvac)

    # ---- G6 gauge invariance of the claim A verdicts ----
    gauge_ok = True
    seen = 0
    for i in range(len(split)):
        for j in range(i + 1, len(split)):
            if seen >= GAUGE_N:
                break
            p, q = split[i], split[j]
            base = cls_zero_A(mul(gens[p], gens[q]), ONE)
            for jj in GAUGE_J:
                v = mul(gens[p], phi_k(jj))
                if cls_zero_A(mul(v, gens[q]), ONE) != base:
                    gauge_ok = False
                if cls_zero_A(mul(neg(v), gens[q]), ONE) != base:
                    gauge_ok = False
            if cls_zero_A(mul(conj(gens[p]), gens[q]),
                          ONE) != cls_zero_A(gens[q], gens[p]):
                gauge_ok = False
            seen += 1
        if seen >= GAUGE_N:
            break
    check("G6.verdicts_are_invariant_under_the_declared_gauge", gauge_ok)
    sys.stdout.write("G6 gauge instances %d, exponents %s\n"
                     % (seen, ",".join(str(x) for x in GAUGE_J)))

    sys.stdout.write("INVENTORY %d checks executed\n" % len(INVENTORY))
    sys.stdout.write("SUMMARY PASS=%d FAIL=%d\n" % (PASS, FAIL))
    sys.exit(1 if FAIL else 0)


main()
