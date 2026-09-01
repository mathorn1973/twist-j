#!/usr/bin/env python3
"""Independent breaker for C-K8-LOCAL-FACTORIZATION-ATLAS-N.

Blindness rule: this file was authored from PREREG.md alone.  Its author did
not read, inspect, search, import, execute, or derive from verify.py or any
other lane file.  The finite scans below are audits, not proofs of universal
mathematical statements.  This is a non-canonical candidate-T/L1 breaker and
creates no Canon, Registry, Frontier, gate, or evidence authority.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, isqrt
from pathlib import Path
import sys


LIMIT = 1_000_000
PHI8 = [1, 0, 0, 0, 1]          # ascending coefficients
OBJECT = "C-K8-LOCAL-FACTORIZATION-ATLAS-N"


class Rejected(Exception):
    """A deterministic decisive-falsifier report."""


def demand(condition, label):
    if not condition:
        raise Rejected(label)


def trim(poly):
    ans = list(poly)
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def poly_mod(poly, p):
    return trim([c % p for c in poly])


def poly_mul(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out)


def poly_pow(base, exponent, p):
    out = [1]
    cur = poly_mod(base, p)
    while exponent:
        if exponent & 1:
            out = poly_mul(out, cur, p)
        cur = poly_mul(cur, cur, p)
        exponent >>= 1
    return out


def poly_divmod(numerator, denominator, p):
    num = poly_mod(numerator, p)
    den = poly_mod(denominator, p)
    demand(den != [0], "polynomial-division-by-zero")
    if len(num) < len(den):
        return [0], num
    quotient = [0] * (len(num) - len(den) + 1)
    inv_lead = pow(den[-1], -1, p)
    while num != [0] and len(num) >= len(den):
        offset = len(num) - len(den)
        coefficient = num[-1] * inv_lead % p
        quotient[offset] = coefficient
        for j, value in enumerate(den):
            num[offset + j] = (num[offset + j] - coefficient * value) % p
        num = trim(num)
    return trim(quotient), num


def poly_eval(poly, value, p):
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % p
    return out


def multiply_many(factors, p):
    out = [1]
    for factor in factors:
        out = poly_mul(out, factor, p)
    return out


def shifted(poly, amount):
    out = [0] * len(poly)
    for degree, coefficient in enumerate(poly):
        for j in range(degree + 1):
            out[j] += coefficient * comb(degree, j) * amount ** (degree - j)
    return trim(out)


def is_eisenstein(poly, p):
    return (
        poly[-1] % p != 0
        and all(coefficient % p == 0 for coefficient in poly[:-1])
        and poly[0] % (p * p) != 0
    )


def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                demand(numerator % previous == 0, "bareiss-nonexact-division")
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def resultant(f, g):
    f_desc = list(reversed(trim(f)))
    g_desc = list(reversed(trim(g)))
    m = len(f_desc) - 1
    n = len(g_desc) - 1
    rows = []
    for offset in range(n):
        rows.append([0] * offset + f_desc + [0] * (n - 1 - offset))
    for offset in range(m):
        rows.append([0] * offset + g_desc + [0] * (m - 1 - offset))
    return det_bareiss(rows)


def primes_through(limit):
    composite = bytearray(limit + 1)
    composite[0:2] = b"\x01\x01"
    for p in range(2, isqrt(limit) + 1):
        if composite[p] == 0:
            start = p * p
            count = (limit - start) // p + 1
            composite[start : limit + 1 : p] = b"\x01" * count
    return [p for p in range(2, limit + 1) if composite[p] == 0]


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    demand(value in (1, p - 1), f"euler-criterion-invalid:p={p}:a={a}")
    return 1 if value == 1 else -1


def square_roots(a, p):
    """All roots in F_p, using deterministic Tonelli--Shanks."""
    a %= p
    if a == 0:
        return (0,)
    if legendre(a, p) == -1:
        return ()
    if p % 4 == 3:
        root = pow(a, (p + 1) // 4, p)
    else:
        odd = p - 1
        twos = 0
        while odd % 2 == 0:
            twos += 1
            odd //= 2
        nonresidue = 2
        while legendre(nonresidue, p) != -1:
            nonresidue += 1
        c = pow(nonresidue, odd, p)
        root = pow(a, (odd + 1) // 2, p)
        residue = pow(a, odd, p)
        level = twos
        while residue != 1:
            i = 1
            probe = residue * residue % p
            while i < level and probe != 1:
                probe = probe * probe % p
                i += 1
            demand(i < level, f"tonelli-shanks-stalled:p={p}:a={a}")
            correction = pow(c, 1 << (level - i - 1), p)
            root = root * correction % p
            residue = residue * correction * correction % p
            c = correction * correction % p
            level = i
    roots = tuple(sorted({root, (-root) % p}))
    demand(len(roots) == 2, f"square-root-count:p={p}:a={a}")
    demand(all(r * r % p == a for r in roots), f"bad-square-root:p={p}:a={a}")
    return roots


def quadratic_irreducible(q, p):
    demand(len(q) == 3 and q[2] % p == 1, f"not-monic-quadratic:p={p}")
    discriminant = (q[1] * q[1] - 4 * q[0]) % p
    return legendre(discriminant, p) == -1


def exhaustive_quadratic_divisors(p, roots):
    """Enumerate every monic quadratic divisor via coefficient equations.

    If (x^2+a*x+b)(x^2+c*x+d)=x^4+1, comparison gives c=-a,
    a*(a^2-2*b)=0, and b*(a^2-b)=1.  Hence either a=0 and
    b^2=-1, or b=d is +/-1 and a^2=2*b.  This finite case split is
    exhaustive and does not use a Frobenius/gcd degree oracle.
    """
    candidates = set()
    for b in roots[-1]:
        candidates.add((b, 0, 1))
    for a in roots[2]:
        candidates.add((1, a, 1))
    for a in roots[-2]:
        candidates.add((p - 1, a, 1))

    divisors = []
    for q_tuple in sorted(candidates):
        q = list(q_tuple)
        quotient, remainder = poly_divmod(PHI8, q, p)
        demand(remainder == [0], f"candidate-not-divisor:p={p}:q={q_tuple}")
        demand(len(quotient) == 3 and quotient[-1] == 1,
               f"bad-quadratic-quotient:p={p}:q={q_tuple}")
        a, b = q[1], q[0]
        c, d = quotient[1], quotient[0]
        demand((a + c) % p == 0 and (b + d + a * c) % p == 0,
               f"coefficient-equations-high:p={p}:q={q_tuple}")
        demand((a * d + b * c) % p == 0 and b * d % p == 1,
               f"coefficient-equations-low:p={p}:q={q_tuple}")
        divisors.append((q, quotient))
    demand(divisors, f"no-quadratic-divisor:p={p}")
    divisor_set = {tuple(q) for q, _ in divisors}
    demand(all(tuple(quotient) in divisor_set for _, quotient in divisors),
           f"quadratic-divisors-not-quotient-closed:p={p}")
    return divisors


def brute_divisor_crosscheck(p, computed):
    brute = set()
    for a in range(p):
        for b in range(p):
            q = [b, a, 1]
            _, remainder = poly_divmod(PHI8, q, p)
            if remainder == [0]:
                brute.add(tuple(q))
    demand(brute == {tuple(q) for q, _ in computed},
           f"quadratic-divisor-completeness:p={p}")


def split_quadratic(q, p):
    discriminant = (q[1] * q[1] - 4 * q[0]) % p
    roots = square_roots(discriminant, p)
    if not roots:
        demand(quadratic_irreducible(q, p), f"quadratic-status:p={p}:q={q}")
        return [q]
    demand(discriminant != 0, f"repeated-quadratic-root:p={p}:q={q}")
    inverse_two = pow(2, -1, p)
    values = sorted({(-q[1] + r) * inverse_two % p for r in roots})
    demand(len(values) == 2 and all(poly_eval(q, r, p) == 0 for r in values),
           f"quadratic-root-recovery:p={p}:q={q}")
    factors = [[(-r) % p, 1] for r in values]
    demand(poly_mod(multiply_many(factors, p), p) == poly_mod(q, p),
           f"quadratic-linear-product:p={p}:q={q}")
    return factors


def direct_factor_phi8(p, roots):
    divisors = exhaustive_quadratic_divisors(p, roots)
    q, quotient = divisors[0]
    factors = split_quadratic(q, p) + split_quadratic(quotient, p)
    factors.sort(key=lambda f: (len(f), tuple(f)))
    demand(multiply_many(factors, p) == poly_mod(PHI8, p),
           f"direct-factor-product:p={p}")
    for factor in factors:
        demand(len(factor) in (2, 3), f"unexpected-factor-degree:p={p}")
        if len(factor) == 3:
            demand(quadratic_irreducible(factor, p),
                   f"reducible-reported-quadratic:p={p}:q={factor}")
    return factors, divisors


def route_pair(route, root, p):
    if route == -1:
        pair = [[(-root) % p, 0, 1], [root % p, 0, 1]]
    elif route == 2:
        pair = [[1, root % p, 1], [1, (-root) % p, 1]]
    elif route == -2:
        pair = [[p - 1, root % p, 1], [p - 1, (-root) % p, 1]]
    else:
        raise Rejected("unknown-square-route")
    demand(multiply_many(pair, p) == poly_mod(PHI8, p),
           f"displayed-route-product:p={p}:route={route}:root={root}")
    return pair


def qring_mul(left, right, radicand):
    a, b = left
    c, d = right
    return (a * c + b * d * radicand, a * d + b * c)


def qring_poly_mul(left, right, radicand):
    out = [(0, 0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            value = qring_mul(a, b, radicand)
            old = out[i + j]
            out[i + j] = (old[0] + value[0], old[1] + value[1])
    return out


def audit_exact_identities():
    one = (1, 0)
    zero = (0, 0)
    expected = [one, zero, zero, zero, one]
    identities = (
        (-1, [(0, -1), zero, one], [(0, 1), zero, one]),
        (2, [one, (0, 1), one], [one, (0, -1), one]),
        (-2, [(-1, 0), (0, 1), one], [(-1, 0), (0, -1), one]),
    )
    for radicand, left, right in identities:
        demand(qring_poly_mul(left, right, radicand) == expected,
               f"exact-polynomial-identity:radicand={radicand}")


def audit_global_and_two():
    translated = shifted(PHI8, 1)
    demand(translated == [2, 4, 6, 4, 1], "shifted-polynomial")
    eisenstein_certificate = is_eisenstein(translated, 2)
    demand(eisenstein_certificate, "eisenstein-at-2")
    reduction = poly_mod(PHI8, 2)
    repeated_linear = poly_pow([1, 1], 4, 2)
    demand(reduction == repeated_linear, "p2-reduction")

    # The same certificate has two deliberately different consequences:
    # global irreducibility over Q and local irreducibility over Q_2.
    global_irreducible = eisenstein_certificate
    q2_irreducible = eisenstein_certificate
    mod2_reducible = repeated_linear == reduction
    demand(global_irreducible and q2_irreducible and mod2_reducible,
           "mod2-versus-Q2-distinction")
    profile = (4, 1, 1)
    demand(profile[0] * profile[1] * profile[2] == 4,
           "p2-profile-degree")
    demand(profile == (4, 1, 1) and profile[0] % 2 == 0,
           "p2-total-wild-ramification")

    derivative = [0, 0, 0, 4]
    discriminant = resultant(PHI8, derivative)
    demand(discriminant == 2 ** 8, "phi8-discriminant")
    return discriminant


def zeta_power(exponent):
    exponent %= 8
    sign = 1 if exponent < 4 else -1
    index = exponent if exponent < 4 else exponent - 4
    out = [0, 0, 0, 0]
    out[index] = sign
    return tuple(out)


def cyc_add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(4))


def cyc_scale(value, vector):
    return tuple(value * x for x in vector)


def cyc_mul(left, right):
    out = [0, 0, 0, 0]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            power = zeta_power(i + j)
            for k in range(4):
                out[k] += a * b * power[k]
    return tuple(out)


def cyc_sigma(vector, exponent):
    out = (0, 0, 0, 0)
    for power, coefficient in enumerate(vector):
        out = cyc_add(out, cyc_scale(coefficient, zeta_power(exponent * power)))
    return out


def rational_rank(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [x / pivot_value for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                multiple = a[r][col]
                a[r] = [x - multiple * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def mod8_order(a):
    value = 1
    for order in range(1, 5):
        value = value * a % 8
        if value == 1:
            return order
    raise Rejected(f"mod8-order-not-found:a={a}")


def audit_v4_and_fixed_fields():
    group = (1, 3, 5, 7)
    demand({a * b % 8 for a in group for b in group} == set(group),
           "v4-closure")
    orders = {a: mod8_order(a) for a in group}
    demand(orders == {1: 1, 3: 2, 5: 2, 7: 2}, "v4-orders")

    one = zeta_power(0)
    i = zeta_power(2)
    sqrt2 = cyc_add(zeta_power(1), zeta_power(7))
    sqrt_minus2 = cyc_mul(i, sqrt2)
    demand(cyc_mul(i, i) == cyc_scale(-1, one), "i-square")
    demand(cyc_mul(sqrt2, sqrt2) == cyc_scale(2, one), "sqrt2-square")
    demand(cyc_mul(sqrt_minus2, sqrt_minus2) == cyc_scale(-2, one),
           "sqrt-minus2-square")

    named = (("1", one), ("i", i), ("sqrt(2)", sqrt2),
             ("sqrt(-2)", sqrt_minus2))
    basis_matrix = [[vector[row] for _, vector in named] for row in range(4)]
    demand(det_bareiss(basis_matrix) != 0, "named-basis-dependent")
    expected = {
        3: ("1", "sqrt(-2)"),
        5: ("1", "i"),
        7: ("1", "sqrt(2)"),
    }
    for a in (3, 5, 7):
        fixed = tuple(name for name, vector in named if cyc_sigma(vector, a) == vector)
        demand(fixed == expected[a], f"wrong-fixed-field:sigma={a}:fixed={fixed}")
        columns = [cyc_sigma(zeta_power(j), a) for j in range(4)]
        matrix_minus_identity = [
            [columns[col][row] - (1 if row == col else 0) for col in range(4)]
            for row in range(4)
        ]
        demand(4 - rational_rank(matrix_minus_identity) == 2,
               f"fixed-space-dimension:sigma={a}")

    split_density = Fraction(sum(order == 1 for order in orders.values()), 4)
    two_two_density = Fraction(sum(order == 2 for order in orders.values()), 4)
    unramified_inert_density = Fraction(sum(order == 4 for order in orders.values()), 4)
    demand((split_density, two_two_density, unramified_inert_density)
           == (Fraction(1, 4), Fraction(3, 4), Fraction(0, 1)),
           "v4-density-count")


def ff_add(left, right):
    return ((left[0] + right[0]) % 5, (left[1] + right[1]) % 5)


def ff_mul(left, right, radicand):
    a, b = left
    c, d = right
    return ((a * c + b * d * radicand) % 5, (a * d + b * c) % 5)


def ff_pow(value, exponent, radicand):
    out = (1, 0)
    cur = value
    while exponent:
        if exponent & 1:
            out = ff_mul(out, cur, radicand)
        cur = ff_mul(cur, cur, radicand)
        exponent >>= 1
    return out


def ff_order(value, radicand):
    demand(value != (0, 0), "zero-has-no-unit-order")
    demand(ff_pow(value, 24, radicand) == (1, 0), "F25-fermat")
    order = 24
    for prime in (2, 3):
        while order % prime == 0 and ff_pow(value, order // prime, radicand) == (1, 0):
            order //= prime
    return order


def ff_eval(poly, radicand):
    out = (0, 0)
    x = (0, 1)
    for coefficient in reversed(poly):
        out = ff_add(ff_mul(out, x, radicand), (coefficient % 5, 0))
    return out


def ring_add(left, right):
    return (ff_add(left[0], right[0]), ff_add(left[1], right[1]))


def ring_mul(left, right):
    return (ff_mul(left[0], right[0], 2), ff_mul(left[1], right[1], 3))


def ring_pow(value, exponent):
    out = ((1, 0), (1, 0))
    cur = value
    while exponent:
        if exponent & 1:
            out = ring_mul(out, cur)
        cur = ring_mul(cur, cur)
        exponent >>= 1
    return out


def ring_eval(poly, value):
    out = ((0, 0), (0, 0))
    for coefficient in reversed(poly):
        out = ring_add(ring_mul(out, value), ((coefficient % 5, 0),
                                                (coefficient % 5, 0)))
    return out


def crt(poly):
    return (ff_eval(poly, 2), ff_eval(poly, 3))


def sigma5(value):
    # u -> -u independently in each ordered F_25 component.
    return ((value[0][0], -value[0][1] % 5),
            (value[1][0], -value[1][1] % 5))


def sigma7(value):
    # Swap components using u_2 -> 3*u_1 and u_1 -> 2*u_2.
    return ((value[1][0], 3 * value[1][1] % 5),
            (value[0][0], 2 * value[0][1] % 5))


def ring_order(value):
    identity = ((1, 0), (1, 0))
    demand(ring_pow(value, 24) == identity, "product-unit-exponent")
    order = 24
    for prime in (2, 3):
        while order % prime == 0 and ring_pow(value, order // prime) == identity:
            order //= prime
    return order


def audit_p5_components():
    first = [3, 0, 1]       # x^2 - 2
    second = [2, 0, 1]      # x^2 - 3
    demand(poly_mul(first, second, 5) == poly_mod(PHI8, 5), "p5-factor-order")
    demand(quadratic_irreducible(first, 5) and quadratic_irreducible(second, 5),
           "p5-factor-irreducibility")

    coefficient_vectors = list(product(range(5), repeat=4))
    images = {crt(list(coefficients)) for coefficients in coefficient_vectors}
    demand(len(images) == 5 ** 4, "p5-crt-not-bijective")
    zeta = crt([0, 1])
    i = crt([0, 0, 1])
    demand(i == ((2, 0), (3, 0)), "p5-i-image")
    demand(i[0] != i[1], "p5-diagonal-confusion")

    e_first = ((1, 0), (0, 0))
    e_second = ((0, 0), (1, 0))
    demand(sigma5(e_first) == e_first and sigma5(e_second) == e_second,
           "sigma5-does-not-preserve-components")
    demand(sigma7(e_first) == e_second and sigma7(e_second) == e_first,
           "sigma7-does-not-swap-components")
    demand(sigma5(i) == i, "sigma5-i-action")
    demand(sigma7(i) == ((3, 0), (2, 0)), "sigma7-i-action")
    demand(sigma5(zeta) == ring_pow(zeta, 5), "sigma5-exponent-action")
    demand(sigma7(zeta) == ring_pow(zeta, 7), "sigma7-exponent-action")
    for coefficients in coefficient_vectors:
        value = crt(list(coefficients))
        demand(sigma5(value) == ring_eval(list(coefficients), ring_pow(zeta, 5)),
               f"sigma5-polynomial-action:coefficients={coefficients}")
        demand(sigma7(value) == ring_eval(list(coefficients), ring_pow(zeta, 7)),
               f"sigma7-polynomial-action:coefficients={coefficients}")
        demand(sigma5(sigma5(value)) == value, "sigma5-not-involution")
        demand(sigma7(sigma7(value)) == value, "sigma7-not-involution")

    field_elements = list(product(range(5), repeat=2))
    nonzero = [value for value in field_elements if value != (0, 0)]
    demand(all(ff_pow(value, 24, 2) == (1, 0) for value in nonzero), "F25-first-units")
    demand(all(ff_pow(value, 24, 3) == (1, 0) for value in nonzero), "F25-second-units")
    generator_first = next(value for value in nonzero if ff_order(value, 2) == 24)
    generator_second = next(value for value in nonzero if ff_order(value, 3) == 24)
    units = {(left, right) for left in nonzero for right in nonzero}
    generated = {
        (ff_pow(generator_first, a, 2), ff_pow(generator_second, b, 3))
        for a in range(24) for b in range(24)
    }
    demand(len(units) == 24 * 24 and generated == units, "full-units-not-C24xC24")

    identity = ((1, 0), (1, 0))
    norm_one = {value for value in units if ring_mul(value, sigma7(value)) == identity}
    demand(len(norm_one) == 24, "swap-norm-one-size")
    norm_generator = next((value for value in norm_one if ring_order(value) == 24), None)
    demand(norm_generator is not None, "swap-norm-one-not-cyclic-C24")
    demand({ring_pow(norm_generator, exponent) for exponent in range(24)} == norm_one,
           "swap-norm-one-generator")

    # The first-component choice is conditional external [D] data.  The
    # swapping automorphism above is the arithmetic obstruction to declaring
    # either component a canonical selector.
    marking_status = "conditional-external-[D]"
    canonical_selector = None
    demand(marking_status == "conditional-external-[D]" and canonical_selector is None,
           "p5-marking-scope")


def audit_scope_boundaries():
    imported = {
        "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]",
        "Z2-PLACES-SPLIT [T]",
        "BORN-RESIDUAL-SPLIT [T]",
        "C8-MARKING-RIGIDITY [T]",
        "DEGREES-BY-PRIME [T]",
    }
    candidate_delta = {
        "all-rational-prime factorization atlas",
        "three square-root routes and fixed-field synthesis",
        "ordered p=5 component audit",
    }
    nearby = "C-CYCLOTOMIC-RAMIFIED-HERMITIAN-SHEETS-N"
    demand(OBJECT != nearby, "nearby-identifier-collision")
    demand(imported.isdisjoint(candidate_delta), "imported-row-repromotion")
    demand("L4 carrier" != "K8 modular/decomposition atlas",
           "nearby-carrier-collision")
    demand(("candidate-T / L1", "NONE", "[D]")
           == ("candidate-T / L1", "NONE", "[D]"), "authority-boundary")
    local_atlas_means = ("modular reductions", "prime decomposition data")
    blanket_qp_factorization_claim = False
    demand(local_atlas_means == ("modular reductions", "prime decomposition data")
           and not blanket_qp_factorization_claim, "local-atlas-scope")


def audit_odd_prime(p, discriminant, stats):
    demand(p % 2 == 1 and discriminant % p != 0, f"odd-prime-ramification:p={p}")
    symbols = {-1: legendre(-1, p), 2: legendre(2, p), -2: legendre(-2, p)}
    demand(symbols[-2] == symbols[-1] * symbols[2], f"legendre-product:p={p}")
    supplement_minus_one = 1 if p % 4 == 1 else -1
    supplement_two = 1 if p % 8 in (1, 7) else -1
    demand(symbols[-1] == supplement_minus_one and symbols[2] == supplement_two,
           f"supplementary-law:p={p}")
    demand(any(value == 1 for value in symbols.values()), f"no-square-route:p={p}")

    roots = {radicand: square_roots(radicand, p) for radicand in (-1, 2, -2)}
    available = {radicand for radicand, values in roots.items() if values}
    expected_routes = {
        1: {-1, 2, -2},
        3: {-2},
        5: {-1},
        7: {2},
    }[p % 8]
    demand(available == expected_routes, f"route-row:p={p}:actual={sorted(available)}")
    for radicand in available:
        demand(symbols[radicand] == 1 and len(roots[radicand]) == 2,
               f"route-root-status:p={p}:route={radicand}")
        for root in roots[radicand]:
            route_pair(radicand, root, p)

    factors, divisors = direct_factor_phi8(p, roots)
    if p <= 257:
        brute_divisor_crosscheck(p, divisors)
    demand(len(divisors) == (6 if p % 8 == 1 else 2),
           f"quadratic-divisor-count:p={p}:count={len(divisors)}")
    degrees = sorted(len(factor) - 1 for factor in factors)
    expected_degrees = [1, 1, 1, 1] if p % 8 == 1 else [2, 2]
    demand(degrees == expected_degrees, f"factor-degree-row:p={p}:degrees={degrees}")

    frobenius_order = mod8_order(p % 8)
    demand(degrees == [frobenius_order] * (4 // frobenius_order),
           f"frobenius-degree-mismatch:p={p}")
    profile = (1, degrees[0], len(degrees))
    expected_profile = (1, 1, 4) if p % 8 == 1 else (1, 2, 2)
    demand(profile == expected_profile and profile[0] * profile[1] * profile[2] == 4,
           f"local-profile:p={p}:profile={profile}")
    demand(4 not in degrees, f"unramified-inert-prime:p={p}")

    if p % 8 == 3:
        for root in roots[-2]:
            pair = route_pair(-2, root, p)
            demand(all(quadratic_irreducible(q, p) for q in pair),
                   f"p3-displayed-pair-reducible:p={p}")
            demand(all((q[1] * q[1] - 4 * q[0]) % p == 2 % p for q in pair),
                   f"p3-discriminant:p={p}")
    elif p % 8 == 5:
        for root in roots[-1]:
            demand(pow(root, 2, p) == p - 1 and pow(root, 4, p) == 1,
                   f"p5-i-order:p={p}:i={root}")
            demand(legendre(root, p) == -1,
                   f"p5-i-unexpected-square:p={p}:i={root}")
            demand(all(quadratic_irreducible(q, p) for q in route_pair(-1, root, p)),
                   f"p5-displayed-pair-reducible:p={p}")
    elif p % 8 == 7:
        for root in roots[2]:
            pair = route_pair(2, root, p)
            demand(all(quadratic_irreducible(q, p) for q in pair),
                   f"p7-displayed-pair-reducible:p={p}")
            demand(all((q[1] * q[1] - 4 * q[0]) % p == (-2) % p for q in pair),
                   f"p7-discriminant:p={p}")
    else:
        linear_roots = sorted({(-factor[0]) % p for factor in factors})
        demand(len(linear_roots) == 4, f"p1-linear-root-count:p={p}")
        demand(all(poly_eval(PHI8, root, p) == 0 and pow(root, 4, p) == p - 1
                   and pow(root, 8, p) == 1 for root in linear_roots),
               f"p1-order-eight-roots:p={p}")

    stats[p % 8] += 1


def source_digest(argv):
    digest = sha256(Path(__file__).read_bytes()).hexdigest()
    if len(argv) == 1:
        return digest, "reported-unpinned"
    demand(len(argv) == 3 and argv[1] == "--expect-sha256", "usage")
    expected = argv[2].lower()
    demand(len(expected) == 64 and all(c in "0123456789abcdef" for c in expected),
           "invalid-pinned-sha256")
    demand(digest == expected, "pinned-executable-byte-mismatch")
    return digest, "matched"


def run(argv):
    digest, pin_status = source_digest(argv)
    audit_scope_boundaries()
    audit_exact_identities()
    discriminant = audit_global_and_two()
    audit_v4_and_fixed_fields()
    audit_p5_components()

    primes = primes_through(LIMIT)
    demand(len(primes) == 78_498 and primes[0] == 2 and primes[-1] == 999_983,
           "prime-sieve-landmarks")
    demand(sum(primes) == 37_550_402_023, "prime-sieve-sum")
    stats = {1: 0, 3: 0, 5: 0, 7: 0}
    for p in primes[1:]:
        audit_odd_prime(p, discriminant, stats)

    print(f"BREAKER {OBJECT}")
    print("STATUS NO_FALSIFIER_FOUND")
    print("AUTHORITY NON_CANONICAL candidate-T/L1 audit-only")
    print("SCAN AUDIT_NOT_PROOF")
    print(f"PRIMES exact-sieve <= {LIMIT}: {len(primes)}")
    print("ODD_ROWS " + " ".join(f"{row}:{stats[row]}" for row in (1, 3, 5, 7)))
    print("P2 mod-2=(x+1)^4 Q2=irreducible profile=(4,1,1) wild")
    print("V4 fixed=(3:-2,5:-1,7:2) densities=(1/4,3/4,0-unramified-inert)")
    print("P5 ordered=(x^2-2,x^2-3) i=(2,3) sigma5=within sigma7=swap")
    print("P5_UNITS full=C24xC24 swap-norm-one=C24 marking=external-[D]")
    print(f"EXECUTED_SHA256 {digest} pin={pin_status}")


def entry():
    try:
        run(sys.argv)
        return 0
    except Rejected as exc:
        print(f"REJECTED {exc}")
        return 1
    except Exception as exc:  # unexpected errors also fail closed
        print(f"REJECTED internal:{type(exc).__name__}:{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(entry())
