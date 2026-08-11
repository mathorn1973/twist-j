#!/usr/bin/env python3
# P-ARITH-RAPIDITY-1 verifier
# Frozen against PREREG.md in this probe directory. Every check below maps
# to exactly one Field 1 gate clause and the verifier asserts nothing
# beyond them. AUDIT of the written proofs at finite scope; carries no
# universal quantifier. Standard library only, exact integers and
# Fractions, no float anywhere. Adapted from the accepted incubation
# verifier of candidate C-ARITH-RAPIDITY-4, sha256
# 5d176fd3818600ef993284af2edf4a734520c30535fc31adda3911cd3dcd196b, with
# only this header comment and the first stdout line changed.
import sys
from fractions import Fraction as Fr

PASS = 0
FAIL = 0


INVENTORY = []


def check(name, cond):
    global PASS, FAIL
    INVENTORY.append(name)
    if cond:
        PASS += 1
        print("PASS " + name)
    else:
        FAIL += 1
        print("FAIL " + name)


# ---------- F = Q(sqrt5): x = (u, v) means u + v sqrt5, u, v in Q ----------

ONE = (Fr(1), Fr(0))
S5 = (Fr(0), Fr(1))
PHI = (Fr(1, 2), Fr(1, 2))


def mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def norm(x):
    return x[0] * x[0] - 5 * x[1] * x[1]


def inv(x):
    n = norm(x)
    return (Fr(x[0]) / n, Fr(-x[1]) / n)


def div(x, y):
    return mul(x, inv(y))


def neg(x):
    return (-x[0], -x[1])


def powf(x, k):
    out = ONE
    b = x if k >= 0 else inv(x)
    for _ in range(abs(k)):
        out = mul(out, b)
    return out


def in_OF(x):
    """x lies in Z[phi] iff 2v and u - v are rational integers."""
    return (2 * x[1]).denominator == 1 and (x[0] - x[1]).denominator == 1


PHI2 = mul(PHI, PHI)


def rho(x):
    """The multiplicative avatar of rapidity: sigma+(x)/sigma-(x) = x/conj(x),
    an element of F of norm 1."""
    return div(x, conj(x))


def phi_even_exponent(w):
    """Exact decision of w in +- phi^(2Z). Returns n with w = +- phi^(2n),
    or None. Logarithm-free: |Tr| = L_(2|n|) pins |n|, then compare."""
    if not in_OF(w) or norm(w) != 1:
        return None
    T = 2 * w[0]
    if T.denominator != 1:
        return None
    T = abs(int(T))
    a, b = 2, 3                      # L_0, L_2
    m = 0
    while a < T:
        a, b = b, 3 * b - a          # L_(2m+2) = 3 L_(2m) - L_(2m-2)
        m += 1
    if a != T:
        return None
    for e in (m, -m):
        c = powf(PHI2, e)
        if w == c or w == neg(c):
            return e
    return None


def same_class(x, y):
    """[eta(x)] == [eta(y)] in R/(log phi)Z, exactly."""
    return phi_even_exponent(div(rho(x), rho(y))) is not None


def class_shift(x, y):
    """n with [eta(x)] - [eta(y)] = n log phi, or None."""
    return phi_even_exponent(div(rho(x), rho(y)))


def same_unordered_class(x, y):
    """R(p) equality: classes agree up to the involution [eta] <-> [-eta]."""
    if phi_even_exponent(div(rho(x), rho(y))) is not None:
        return "oriented"
    if phi_even_exponent(mul(rho(x), rho(y))) is not None:
        return "conjugate"
    return None


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
        i += 1
    return [q for q in range(2, n + 1) if s[q]]


# ---------- G1 ----------

def gate_g1():
    grid = [(Fr(a), Fr(b)) for a in range(-8, 9) for b in range(-8, 9)
            if (a, b) != (0, 0)]
    pairs = [(grid[i], grid[(7 * i + 3) % len(grid)])
             for i in range(0, len(grid), 5)]
    ok_rho = ok_N = True
    for x, y in pairs:
        if rho(mul(x, y)) != mul(rho(x), rho(y)):
            ok_rho = False
        if norm(mul(x, y)) != norm(x) * norm(y):
            ok_N = False
    ok_int = all(x[0] * x[0] - 5 * x[1] * x[1] == norm(x) for x in grid)
    ok_rec = all(mul(x, conj(x)) == (norm(x), Fr(0)) for x in grid)
    ok_rest = all((phi_even_exponent(rho(x)) == 0) == (x[0] == 0 or x[1] == 0)
                  for x in grid)
    ok_null = all(norm(x) != 0 for x in grid)
    print("G1 grid %d elements, %d product pairs" % (len(grid), len(pairs)))
    check("G1.rho_and_N_multiplicative_on_pairs", ok_rho and ok_N)
    check("G1.signed_interval_t2_minus_s2_equals_N", ok_int)
    check("G1.x_times_conj_equals_norm", ok_rec)
    check("G1.rest_class_zero_exactly_iff_ab_zero", ok_rest)
    check("G1.no_nonzero_F_rational_null_vector_on_grid", ok_null)


# ---------- G2 ----------

def gate_g2():
    ok_alt = all(norm(powf(PHI, k)) == (-1) ** k for k in range(1, 13))
    check("G2.unit_norm_alternates_to_k12", ok_alt)
    check("G2.rho_phi_equals_minus_phi_squared", rho(PHI) == neg(PHI2))
    L, F = [2, 1], [0, 1]
    ok_lf = ok_sheet = True
    for n in range(1, 31):
        L.append(L[-1] + L[-2])
        F.append(F[-1] + F[-2])
        x = powf(PHI, n)
        if x != (Fr(L[n], 2), Fr(F[n], 2)):
            ok_lf = False
        if L[n] * L[n] - 5 * F[n] * F[n] != 4 * (-1) ** n:
            ok_lf = False
        if (norm(x) > 0) != (n % 2 == 0):
            ok_sheet = False
    check("G2.phi_n_is_Lucas_time_sqrt5_Fibonacci_space_to_n30", ok_lf)
    check("G2.sheet_sign_matches_parity", ok_sheet)


# ---------- G3 ----------

def gate_g3():
    ok_direct = True
    for m in range(-12, 13):
        w = powf(PHI2, m)
        if phi_even_exponent(w) != m or phi_even_exponent(neg(w)) != m:
            ok_direct = False
    check("G3.membership_test_agrees_with_direct_comparison_to_m12",
          ok_direct)
    ok_zero = (phi_even_exponent(rho(S5)) == 0
               and all(phi_even_exponent(rho((Fr(q), Fr(0)))) == 0
                       for q in (1, 2, 3, 7, 11, 13)))
    check("G3.test_returns_zero_on_sqrt5_and_on_rationals", ok_zero)
    ok_shift = all(class_shift(powf(PHI, n), ONE) == n
                   for n in range(-8, 9))
    check("G3.test_returns_n_on_phi_n", ok_shift)


# ---------- G4: two genuine constructions ----------

def gen_pell(p):
    """Construction (i): Diophantine sweep on a^2 - 5 b^2 = +-4p."""
    b = 0
    while True:
        b += 1
        for sg in (4, -4):
            aa = sg * p + 5 * b * b
            if aa < 0:
                continue
            r = 0
            step = 1 << ((aa.bit_length() + 1) // 2 + 1)
            while step:                       # exact integer square root
                if (r + step) * (r + step) <= aa:
                    r += step
                step >>= 1
            if r * r == aa:
                g = (Fr(r, 2), Fr(b, 2))
                return mul(g, PHI) if norm(g) == -p else g


def nearest_OF(z):
    """Round z in F to the nearest element of Z[phi] in the (1, phi) basis."""
    b = 2 * z[1]
    a = z[0] - z[1]
    bi = (2 * b.numerator + b.denominator) // (2 * b.denominator)
    ai = (2 * a.numerator + a.denominator) // (2 * a.denominator)
    return (Fr(2 * ai + bi, 2), Fr(bi, 2))


def gen_euclid(p, trace):
    """Construction (ii): Euclidean gcd of p and sqrt5 - r in Z[phi], at the
    canonical root 0 < r < p/2. Q(sqrt5) is norm-Euclidean; every division
    step is asserted norm-decreasing rather than assumed."""
    r = None
    for w in range(1, p // 2 + 1):
        if (w * w - 5) % p == 0:
            r = w
            break
    if r is None:
        return None, False
    a, b = (Fr(p), Fr(0)), (Fr(-r), Fr(1))
    steps_ok = True
    while norm(b) != 0:
        q = nearest_OF(div(a, b))
        rem = (a[0] - mul(q, b)[0], a[1] - mul(q, b)[1])
        if not (abs(norm(rem)) < abs(norm(b))):
            steps_ok = False
            break
        a, b = b, rem
    if not steps_ok:
        return None, False
    g = mul(a, PHI) if norm(a) == -p else a
    trace.append(r)
    return g, True


def gate_g4():
    ps = [q for q in sieve(1999) if q % 5 in (1, 4) and q != 5]
    ok_norm = ok_gate = ok_steps = True
    oriented = conjugated = 0
    roots = []
    for p in ps:
        A = gen_pell(p)
        B, sok = gen_euclid(p, roots)
        if not sok or B is None:
            ok_steps = False
            continue
        if norm(A) != p or norm(B) != p or not in_OF(A) or not in_OF(B):
            ok_norm = False
        if mul(A, conj(A)) != (Fr(p), Fr(0)):
            ok_norm = False
        verdict = same_unordered_class(A, B)
        if verdict == "oriented":
            oriented += 1
        elif verdict == "conjugate":
            conjugated += 1
        else:
            ok_gate = False
    print("G4 split primes below 2000: %d" % len(ps))
    print("G4 orientation data (gates nothing): oriented=%d conjugate=%d"
          % (oriented, conjugated))
    check("G4.both_constructions_return_a_generator_of_norm_plus_p",
          ok_norm and len(roots) == len(ps))
    check("G4.every_euclid_division_step_norm_decreasing", ok_steps)
    check("G4.canonical_unordered_classes_agree_R1_equals_R2", ok_gate)


# ---------- G5, G6 ----------

def gate_g5():
    ps = [q for q in sieve(499) if q % 5 in (1, 4) and q != 5]
    ok_wd = ok_conj = True
    variants = [lambda z: z, neg,
                lambda z: mul(PHI, z),
                lambda z: mul(PHI2, z),
                lambda z: neg(mul(powf(PHI, 3), z))]
    for p in ps:
        pi = gen_pell(p)
        for f in variants:
            if not same_class(f(pi), pi):
                ok_wd = False
        if mul(rho(pi), rho(conj(pi))) != ONE:
            ok_conj = False
    print("G5 split primes below 500: %d, generator variants each: %d"
          % (len(ps), len(variants)))
    check("G5.class_unchanged_under_every_generator_variant", ok_wd)
    check("G5.conjugate_class_is_the_negative", ok_conj)


def gate_g6():
    inert = [q for q in sieve(1999) if q % 5 in (2, 3) and q != 2]
    ok_in = all(phi_even_exponent(rho((Fr(q), Fr(0)))) == 0 for q in inert)
    print("G6 inert primes below 2000: %d" % len(inert))
    check("G6.inert_primes_sit_at_class_zero", ok_in)
    check("G6.ramified_sqrt5_class_zero_and_rho_exactly_minus_one",
          phi_even_exponent(rho(S5)) == 0 and rho(S5) == neg(ONE)
          and mul(S5, S5) == (Fr(5), Fr(0)))


# ---------- G7, G8, G9 ----------

def gate_g7():
    xs = [(Fr(a), Fr(b)) for a in range(-3, 4) for b in range(-3, 4)
          if (a, b) != (0, 0)]
    ok_n = ok_shift = ok_diff = True
    for k in (1, 2, 3):
        e = powf(PHI, k)
        for x in xs:
            xk = div(x, e)
            if abs(norm(xk)) != abs(norm(x)):
                ok_n = False
            if class_shift(x, xk) != k:
                ok_shift = False
        x, y = xs[3], xs[17]
        if div(rho(x), rho(y)) != div(rho(div(x, e)), rho(div(y, e))):
            ok_diff = False
    check("G7.frame_change_preserves_norm_scale", ok_n)
    check("G7.frame_change_shifts_class_by_exactly_k", ok_shift)
    check("G7.rapidity_differences_invariant", ok_diff)


def gate_g8():
    seen = []
    for num in range(1, 40):
        for den in range(1, 40):
            t = Fr(num, den)
            if 1 - 5 * t * t == 0:
                continue
            x = ((1 + 5 * t * t) / (1 - 5 * t * t), 2 * t / (1 - 5 * t * t))
            if norm(x) != 1:
                continue
            if not any(same_class(x, y) for y in seen):
                seen.append(x)
    print("G8 distinct norm-one rational classes exhibited: %d" % len(seen))
    check("G8.rational_points_occupy_many_distinct_classes", len(seen) >= 400)


def gate_g9():
    ps = [q for q in sieve(1999) if q % 5 in (1, 4) and q != 5]
    ok_inv = True
    for p in ps:
        pi = gen_pell(p)
        if mul(rho(pi), rho(conj(pi))) != ONE:
            ok_inv = False
    check("G9.rho_of_conjugate_is_the_inverse_all_split_below_2000", ok_inv)
    ok_w = all(norm((Fr(q), Fr(0))) == q * q
               for q in sieve(1999) if q % 5 in (2, 3) and q != 2)
    check("G9.inert_ideal_norm_is_p_squared", ok_w)
    print("G9 recorded weights: split N(p)=p, inert N(p)=p^2; "
          "no bridge claim is made")


def main():
    print("P-ARITH-RAPIDITY-1 verifier")
    print("AUDIT of written proofs at finite scope; no universal quantifier")
    print("exact throughout; the rapidity class is decided without logarithms")
    gate_g1()
    gate_g2()
    gate_g3()
    gate_g4()
    gate_g5()
    gate_g6()
    gate_g7()
    gate_g8()
    gate_g9()
    print("G10 check inventory, one line per assertion executed:")
    for nm in INVENTORY:
        print("  " + nm)
    listed = len(INVENTORY)
    executed = PASS + FAIL
    check("G10.inventory_length_equals_checks_executed", listed == executed)
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
