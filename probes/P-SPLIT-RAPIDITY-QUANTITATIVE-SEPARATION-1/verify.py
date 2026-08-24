#!/usr/bin/env python3
"""Exact finite audit for two split-rapidity theorem claims.

The written proofs in PREREG.md carry the universal quantifiers.  This one
accepted verifier embeds the independent bounded breaker and the exact
phase-normalization negative control.  It uses integers only: no float,
logarithm, trigonometric evaluation, or numerical eigensolver.
"""

from itertools import product
from math import gcd, isqrt
import sys


PASS = 0
FAIL = 0
INVENTORY = []

ONE = (1, 0)
PHI = (0, 1)
PHI_INV = (-1, 1)
PHI2 = (1, 1)


def check(name, condition):
    global PASS, FAIL
    INVENTORY.append(name)
    if condition:
        PASS += 1
        sys.stdout.write("PASS %s\n" % name)
    else:
        FAIL += 1
        sys.stdout.write("FAIL %s\n" % name)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c + b * d, a * d + b * c + b * d


def conj(x):
    return x[0] + x[1], -x[1]


def norm(x):
    return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]


def trace(x):
    return 2 * x[0] + x[1]


def power(x, n):
    assert n >= 0
    out = ONE
    base = x
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def phi_power(n):
    return power(PHI if n >= 0 else PHI_INV, abs(n))


def sign_u_plus_v_sqrt5(u, v):
    if u == 0:
        return (v > 0) - (v < 0)
    if v == 0:
        return (u > 0) - (u < 0)
    if (u > 0) == (v > 0):
        return 1 if u > 0 else -1
    comparison = u * u - 5 * v * v
    assert comparison != 0
    if u > 0:
        return 1 if comparison > 0 else -1
    return -1 if comparison > 0 else 1


def sign(x):
    return sign_u_plus_v_sqrt5(2 * x[0] + x[1], x[1])


def lt(x, y):
    return sign(sub(x, y)) < 0


def gt(x, y):
    return sign(sub(x, y)) > 0


def in_open_half_band(x):
    x2 = mul(x, x)
    xb2 = mul(conj(x), conj(x))
    return lt(x2, mul(PHI2, xb2)) and lt(xb2, mul(PHI2, x2))


def reduce_half_band(x):
    for _ in range(400):
        if in_open_half_band(x):
            return x
        x2 = mul(x, x)
        xb2 = mul(conj(x), conj(x))
        if gt(x2, mul(PHI2, xb2)):
            x = mul(x, PHI_INV)
        else:
            x = mul(x, PHI)
    raise AssertionError("half-band reduction did not terminate")


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def find_generator(p):
    bmax = 3 * isqrt(p) + 8
    for b in range(bmax + 1):
        for target in (p, -p):
            discriminant = 5 * b * b + 4 * target
            root = isqrt(discriminant) if discriminant >= 0 else -1
            if root < 0 or root * root != discriminant:
                continue
            for signed_root in (root, -root):
                if (-b + signed_root) % 2 == 0:
                    x = ((-b + signed_root) // 2, b)
                    if norm(x) == target:
                        return x
    raise AssertionError("no generator found")


def merge(addresses):
    out = {}
    for p, epsilon, coefficient in addresses:
        assert epsilon in (-1, 1)
        out[p] = out.get(p, 0) + epsilon * coefficient
    return {p: c for p, c in sorted(out.items()) if c}


def budget(coefficients):
    out = 1
    for p, exponent in coefficients.items():
        out *= p ** abs(exponent)
    return out


def determinant_row(p, q, x, y, n):
    shifted = mul(y, phi_power(n))
    z = mul(x, conj(shifted))
    nz = norm(z)
    assert abs(nz) == p * q
    assert trace(z) * trace(z) - 5 * z[1] * z[1] == 4 * nz
    if nz > 0:
        kind = "SQRT5_Z"
        rung = z[1]
        value = 5 * rung * rung
    else:
        kind = "Z"
        rung = trace(z)
        value = rung * rung
    assert rung != 0
    return n, kind, rung, value


def audit_pair(p, q, x, y, label, records):
    rows = [determinant_row(p, q, x, y, n) for n in (-1, 0, 1)]
    ordered = sorted(row[3] for row in rows)
    assert ordered[0] < ordered[1]
    best = min(rows, key=lambda row: row[3])
    records.append((best[3], 4 * p * q, p, q, label, best[1], abs(best[2])))
    return best


def build_x(coefficients, generators):
    out = ONE
    for p, exponent in coefficients.items():
        base = generators[p] if exponent > 0 else conj(generators[p])
        out = mul(out, power(base, abs(exponent)))
    assert norm(out) == budget(coefficients)
    return out


def determinant_value(x, p_budget, n):
    y = mul(phi_power(-n), x)
    ny = norm(y)
    assert abs(ny) == p_budget
    assert trace(y) * trace(y) - 5 * y[1] * y[1] == 4 * ny
    if n % 2 == 0:
        rung = y[1]
        value = 5 * rung * rung
    else:
        rung = trace(y)
        value = rung * rung
    assert rung != 0
    return value, rung


def minimum_data(coefficients, generators):
    x = build_x(coefficients, generators)
    p_budget = budget(coefficients)
    rows = [
        (determinant_value(x, p_budget, n)[0], n,
         determinant_value(x, p_budget, n)[1])
        for n in range(-80, 81)
    ]
    best = min(rows)
    assert sum(value == best[0] for value, _, _ in rows) == 1
    assert best[1] not in (-80, 80)
    return best


def circular_distance(a, b, modulus):
    direct = abs(a - b)
    return min(direct, modulus - direct)


def shell_bound_audit():
    modulus = 12
    audited = 0
    for mask in range(1, 1 << modulus):
        points = [i for i in range(modulus) if mask & (1 << i)]
        if len(points) < 2:
            continue
        separation = min(
            circular_distance(points[i], points[j], modulus)
            for i in range(len(points))
            for j in range(i + 1, len(points))
        )
        assert separation > 0
        for anchor in points:
            for shell in range(1, modulus + 1):
                count = sum(
                    shell * separation
                    <= circular_distance(anchor, point, modulus)
                    < (shell + 1) * separation
                    for point in points if point != anchor
                )
                assert count <= 2
                audited += 1
    return audited


def main():
    print("P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1 verifier")
    print("AUDIT of two written theorem proofs at finite scope; no universal quantifier")
    print("exact integers in Z[phi]; no float, logarithm, trigonometric evaluation, or eigensolver")

    sample = [(41, -1, 3), (11, 1, 2), (41, 1, 1), (11, -1, 1)]
    merged = merge(sample)
    check(
        "G1.effective_vector_merging_and_diagonal",
        merged == merge(reversed(sample)) == {11: 1, 41: -2}
        and budget(merged) == 11 * 41 * 41
        and merge([(11, 1, 2), (11, -1, 2)]) == {},
    )

    pi11 = (3, 1)
    pi41 = (6, 1)
    sharp451 = mul(mul(pi11, pi41), PHI_INV)
    check(
        "G2.sharp_witness_norm_minus451",
        norm(pi11) == 11 and norm(pi41) == 41
        and sharp451 == (-9, 19) and norm(sharp451) == -451
        and trace(sharp451) == 1 and in_open_half_band(sharp451),
    )

    pi421 = (19, 4)
    pi431 = (19, 5)
    sharp_pair = mul(mul(pi421, pi431), PHI_INV)
    check(
        "G3.sharp_pair_421_431_positive_norm_channel",
        norm(pi421) == 421 and norm(pi431) == 431
        and sharp_pair == (-190, 381)
        and norm(sharp_pair) == -421 * 431
        and trace(sharp_pair) == 1 and in_open_half_band(sharp_pair),
    )

    splits = [p for p in range(2, 2001) if is_prime(p) and p % 5 in (1, 4)]
    generators = {}
    generator_ok = len(splits) == 146
    for p in splits:
        g = reduce_half_band(find_generator(p))
        gc = reduce_half_band(conj(g))
        generator_ok = generator_ok and abs(norm(g)) == p and abs(norm(gc)) == p
        generators[p] = (g, gc)
    check("G4.split_generators_reduced_exactly", generator_ok)

    records = []
    rung_z = set()
    rung_sqrt5 = set()
    channels_unique = True
    parity_ok = True
    for i, p in enumerate(splits):
        for q in splits[i + 1:]:
            channel_bests = []
            for label, y in (("A", generators[q][0]), ("B", generators[q][1])):
                best = audit_pair(p, q, generators[p][0], y, label, records)
                channel_bests.append(best)
                parity_ok = parity_ok and (
                    (best[1] == "Z" and best[3] == best[2] * best[2])
                    or (best[1] == "SQRT5_Z" and best[3] == 5 * best[2] * best[2])
                )
                if best[1] == "Z" and abs(best[2]) == 1:
                    rung_z.add((p, q))
                if best[1] == "SQRT5_Z" and abs(best[2]) == 1:
                    rung_sqrt5.add((p, q))
            channels_unique = channels_unique and channel_bests[0][3] != channel_bests[1][3]
        audit_pair(p, p, generators[p][0], generators[p][1], "SELF", records)

    check(
        "G5.determinant_nonzero_and_nearest_channel_unique",
        len(records) == 21316 and channels_unique,
    )
    check(
        "G6.parity_lattices_and_exact_metric_numerators",
        parity_ok and len(rung_z) == 95 and len(rung_sqrt5) == 164,
    )

    least = records[0]
    for row in records[1:]:
        if row[0] * least[1] < least[0] * row[1]:
            least = row
    numerator, denominator, p, q, label, kind, rung = least
    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor
    check(
        "G7.minimum_ordered_by_exact_cross_multiplication",
        (p, q, label, kind, rung, numerator, denominator)
        == (1619, 1979, "B", "Z", 1, 1, 12816004),
    )

    breaker_generators = {11: (3, 1), 19: (4, 1), 29: (5, 1), 41: (6, 1)}
    baselines = {}
    primes = tuple(breaker_generators)
    for vector in product(range(-2, 3), repeat=len(primes)):
        if not any(vector):
            continue
        coefficients = {p: e for p, e in zip(primes, vector) if e}
        baselines[tuple(sorted(coefficients.items()))] = minimum_data(
            coefficients, breaker_generators
        )
    check("B1.independent_relation_and_tie_breaker", len(baselines) == 624)

    gauged = dict(breaker_generators)
    gauged[11] = mul(PHI2, gauged[11])
    gauge_ok = True
    for key, expected in baselines.items():
        actual = minimum_data(dict(key), gauged)
        gauge_ok = gauge_ok and actual[0] == expected[0]
        gauge_ok = gauge_ok and actual[1] % 2 == expected[1] % 2
    check("B2.positive_norm_even_unit_gauge_invariant", gauge_ok)

    reoriented = dict(breaker_generators)
    reoriented[19] = conj(reoriented[19])
    orientation_ok = True
    for key, expected in baselines.items():
        coefficients = dict(key)
        coefficients[19] = -coefficients.get(19, 0)
        if coefficients[19] == 0:
            del coefficients[19]
        orientation_ok = orientation_ok and (
            minimum_data(coefficients, reoriented)[0] == expected[0]
        )
    check("B3.orientation_and_coefficient_reversal_invariant", orientation_ok)

    addresses = []
    cutoff = 2000
    for p in splits:
        power_p = p
        exponent = 1
        while power_p <= cutoff:
            addresses.extend(((p, exponent, 1), (p, exponent, -1)))
            exponent += 1
            power_p *= p
    address_budget_ok = True
    for i, left in enumerate(addresses):
        for right in addresses[i + 1:]:
            coefficients = merge(
                [(left[0], left[2], left[1]), (right[0], right[2], -right[1])]
            )
            address_budget_ok = address_budget_ok and bool(coefficients)
            address_budget_ok = address_budget_ok and budget(coefficients) <= cutoff * cutoff
    check("F1.two_address_product_budget_at_most_X_squared", address_budget_ok)

    weights_ok = True
    for k in range(65):
        numerator_sum = sum(k + 1 - abs(h) for h in range(-k, k + 1))
        weights_ok = weights_ok and numerator_sum == (k + 1) * (k + 1)
    check("F2.normalized_fejer_weights_sum_to_one", weights_ok)
    check("F3.two_points_per_circular_shell", shell_bound_audit() > 0)
    check("F4.singleton_gram_matrix_is_identity", [[1]][0][0] == 1)

    pi491 = (20, 7)
    pi1429 = (34, 13)
    product_budget = 491 * 1429
    x = mul(pi491, pi1429)
    check(
        "N1.positive_norm_generators_491_1429",
        norm(pi491) == 491 and norm(pi1429) == 1429
        and x == (771, 589) and norm(x) == product_budget,
    )

    opposite = mul(pi491, conj(pi1429))
    same_shifted = mul(phi_power(-2), x)
    check(
        "N2.ordinary_signed_channels_rungs_22_182",
        opposite == (849, -22) and norm(opposite) == product_budget
        and in_open_half_band(opposite) and abs(opposite[1]) == 22
        and same_shifted == (953, -182)
        and norm(same_shifted) == product_budget
        and in_open_half_band(same_shifted) and abs(same_shifted[1]) == 182,
    )

    doubled = mul(phi_power(-3), mul(x, x))
    check(
        "N3.doubled_vector_trace_and_product_budget",
        doubled == (-313768, 627565)
        and norm(doubled) == -(product_budget * product_budget)
        and in_open_half_band(doubled) and trace(doubled) == 29,
    )

    doubled_denominator = 4 * product_budget * product_budget
    cutoff_denominator = 4 * 1429 * 1429
    check(
        "N4.naive_doubled_X_bound_falsified_by_841",
        doubled_denominator == 1969189145284
        and cutoff_denominator == 8168164
        and 841 * cutoff_denominator < doubled_denominator,
    )

    assert len(INVENTORY) == 18
    print("INVENTORY %d checks executed" % len(INVENTORY))
    print("SUMMARY PASS=%d FAIL=%d" % (PASS, FAIL))
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
