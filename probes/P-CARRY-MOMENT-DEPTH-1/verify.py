#!/usr/bin/env python3
"""Exact finite audit of the separately proved carry-moment theorem.

NON-CANONICAL. Standard library only. No original handoff code or tables are
loaded. All scientific predicates use integers or fractions. Success writes
one deterministic JSON document; a discrepancy or incomplete run exits nonzero.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
import sys
from time import monotonic


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)
LAMBDA = (1, -1, 0, 0)
PHI = (0, 0, -1, -1)
PHI_INV = (-1, 0, -1, -1)
J = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)
COUNTS = (0, 1, 2, 3, 4)
BALANCED = (-2, -1, 0, 1, 2)
MAX_N = 100
BRUTE_N = 4
TIME_LIMIT_SECONDS = 540
STATE_LIMIT = 50000


class Discrepancy(Exception):
    pass


class Incomplete(Exception):
    pass


def require(condition, message):
    if not condition:
        raise Discrepancy(message)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(x, k):
    return tuple(k * a for a in x)


def mul(x, y):
    """Convolution reduced by 1 + z + z^2 + z^3 + z^4, degree high to low."""
    coefficients = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        top = coefficients[degree]
        for lower in range(degree - 4, degree):
            coefficients[lower] -= top
    return tuple(coefficients[:4])


def power(x, exponent):
    require(exponent >= 0, "negative exponent in polynomial power")
    result = ONE
    while exponent:
        if exponent & 1:
            result = mul(result, x)
        x = mul(x, x)
        exponent //= 2
    return result


def conjugate(x):
    a, b, c, d = x
    return a - b, -b, d - b, c - b


def trace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]


def quadratic(x):
    return 5 * sum(a * a for a in x) - sum(x) ** 2


def divide_lambda(x):
    """Exact integral division, used only after testing the residue."""
    require(all(type(a) is int for a in x), "noninteger carry coefficient")
    require(sum(x) % 5 == 0, "nonintegral lambda division")
    q = sum(x) // 5
    a, b, c, _ = x
    return a - q, a + b - 2 * q, a + b + c - 3 * q, q


def inverse_lambda_field():
    return F(4, 5), F(3, 5), F(2, 5), F(1, 5)


def representative(residue, digits):
    return (residue - digits[0]) % 5 + digits[0]


def valuation_from_integer(u, s):
    remainder = sub(u, scale(ONE, s))
    if remainder == ZERO:
        return None
    valuation = 0
    while sum(remainder) % 5 == 0:
        remainder = divide_lambda(remainder)
        valuation += 1
        if valuation > 64:
            raise Incomplete("valuation exceeded declared finite audit budget")
    return valuation


def admission(u, digits):
    s = representative(sum(u), digits)
    require(s % 5 != 0, "unit has zero residue")
    h = valuation_from_integer(u, s)
    if h not in (1, 2, 3):
        raise ValueError("the moment theorem is not admitted at this depth")
    return s, h


def scalar_moment(s, digits):
    return F(sum(b * representative(s * b, digits) for b in digits), 5)


def step(u, carry, b, digits):
    raw = add(carry, scale(u, b))
    a = representative(sum(raw), digits)
    return a, divide_lambda(sub(raw, scale(ONE, a)))


def fraction_pair(x):
    value = F(x)
    return [value.numerator, value.denominator]


def checkpoint(deadline):
    if monotonic() > deadline:
        raise Incomplete("540 second execution budget exhausted")


def ring_preflight():
    require(power(ZETA, 5) == ONE, "zeta order identity")
    total = ZERO
    for k in range(5):
        total = add(total, power(ZETA, k))
    require(total == ZERO, "cyclotomic relation")
    require(mul(PHI, PHI_INV) == ONE, "phi inverse")
    require(mul(J, J_INV) == ONE, "J inverse")
    require(mul(LAMBDA, inverse_lambda_field()) == ONE, "lambda inverse")
    require(mul(LAMBDA, conjugate(LAMBDA)) == add(ONE, mul(J, conjugate(J))),
            "lambda and J norm identity")
    require(J == mul(ZETA, PHI_INV), "J phase and modulus identity")
    require(quadratic(J_INV) == 6, "inverse J trace")
    # min |sigma(lambda)|^2 = (5 - sqrt(5))/2 > (47/40)^2.
    comparison = F(5) - 2 * F(47, 40) ** 2
    require(comparison > 0 and comparison ** 2 > 5, "rational contraction bound")
    for coefficients in product(range(-2, 3), repeat=4):
        require(quadratic(coefficients) == trace(mul(coefficients, conjugate(coefficients))),
                "trace/Gram quadratic disagreement")
        require(conjugate(conjugate(coefficients)) == coefficients, "conjugation involution")
        if sum(coefficients) % 5 == 0:
            require(mul(LAMBDA, divide_lambda(coefficients)) == coefficients,
                    "integral division roundtrip")


def exact_predictions(u, digits):
    """Predictions use only the proved h-prefix rule, never observed DP moments."""
    s, h = admission(u, digits)
    mu = sum(digits) // 5
    initial_m = scalar_moment(s, digits)
    a = mul(sub(u, ONE), conjugate(sub(u, ONE)))
    b = add(mul(u, conjugate(u)), ONE)
    c = add(u, conjugate(u))
    inverse_lambda = inverse_lambda_field()
    inverse_norm = mul(inverse_lambda, conjugate(inverse_lambda))
    lambda_powers = [ONE]
    norm_powers = [ONE]
    for _ in range(MAX_N):
        lambda_powers.append(mul(lambda_powers[-1], inverse_lambda))
        norm_powers.append(mul(norm_powers[-1], inverse_norm))
    limits = mu * mu * quadratic(sub(u, ONE)) + 2 * quadratic(mul(u, J_INV)) + 12
    s_n = ZERO
    g_n = ZERO
    predictions = []
    for n in range(1, MAX_N + 1):
        s_n = add(s_n, lambda_powers[n])
        g_n = add(g_n, norm_powers[n])
        correction = ZERO
        for i in range(min(h, n)):
            correction = add(correction, norm_powers[n - i])
        expected = (mu * mu * trace(mul(a, mul(s_n, conjugate(s_n))))
                    + 2 * trace(mul(b, g_n))
                    + (mu * mu - initial_m) * trace(mul(c, correction)))
        mean = scale(mul(sub(u, ONE), s_n), mu)
        r = F(40, 47)
        bound = (mu * mu * quadratic(sub(u, ONE)) * (2 * r ** n + r ** (2 * n))
                 + (2 * quadratic(mul(u, J_INV)) + 12) * r ** (2 * n)
                 + abs(mu * mu - initial_m) * (quadratic(u) + 4)
                 * sum(r ** (2 * (n - i)) for i in range(min(h, n))))
        predictions.append((expected, mean, bound))
    return s, h, mu, initial_m, limits, predictions


def independent_word_image(u, word, digits):
    """Multiply the complete integer word once, then extract output digits."""
    value = ZERO
    p = ONE
    for b in word:
        value = add(value, scale(p, b))
        p = mul(p, LAMBDA)
    remainder = mul(u, value)
    output = []
    for _ in word:
        a = representative(sum(remainder), digits)
        output.append(a)
        remainder = divide_lambda(sub(remainder, scale(ONE, a)))
    return tuple(output), remainder


def brute_audit(u, digits, snapshots, deadline):
    mu = sum(digits) // 5
    words_checked = 0
    mixed_checked = 0
    covariance_checked = 0
    for n in range(1, BRUTE_N + 1):
        histogram = Counter()
        images = set()
        mixed = [[0] * n for _ in range(n)]
        centered = {(i, j): ZERO for i in range(n) for j in range(i + 1, n)}
        for word in product(digits, repeat=n):
            output, carry = independent_word_image(u, word, digits)
            histogram[carry] += 1
            images.add(output)
            stream_carry = ZERO
            stream_output = []
            increments = []
            for b in word:
                a, stream_carry = step(u, stream_carry, b, digits)
                stream_output.append(a)
                increments.append(sub(sub(scale(u, b), scale(ONE, a)),
                                      scale(sub(u, ONE), mu)))
            require((tuple(stream_output), stream_carry) == (output, carry),
                    "whole-word and streaming disagreement")
            for i in range(n):
                for j in range(n):
                    mixed[i][j] += word[i] * output[j]
            for pair in centered:
                i, j = pair
                centered[pair] = add(centered[pair], mul(increments[i], conjugate(increments[j])))
            words_checked += 1
        require(histogram == snapshots[n], "brute force and DP carry law disagree")
        require(len(images) == 5 ** n, "finite word bijection failure")
        for i in range(n):
            for j in range(n):
                if i != j:
                    require(mixed[i][j] == mu * mu * 5 ** n,
                            "off-diagonal mixed moment disagreement")
                    mixed_checked += 1
        for value in centered.values():
            require(value == ZERO, "nonzero centered increment cross-covariance")
            covariance_checked += 1
        checkpoint(deadline)
    return words_checked, mixed_checked, covariance_checked


def audit_case(label, u, inverse, digits, expected_limit, deadline, digest):
    require(mul(u, inverse) == ONE, label + ": not inverse units")
    s, h, mu, initial_m, limit, predictions = exact_predictions(u, digits)
    require(limit == expected_limit, label + ": declared limit value")
    counts = {ZERO: 1}
    total = 1
    edges = {}
    q_values = {}
    snapshots = {}
    max_support = 1
    mirror_edges = 0
    tail_checks = 0
    for n, (predicted, expected_mean, tail) in enumerate(predictions, 1):
        checkpoint(deadline)
        following = Counter()
        output_counts = Counter()
        mixed_sum = 0
        for carry, weight in counts.items():
            if carry not in edges:
                row = tuple(step(u, carry, b, digits) for b in digits)
                edges[carry] = row
                for b, (a, next_carry) in zip(digits, row):
                    require(add(carry, scale(u, b)) == add(scale(ONE, a), mul(LAMBDA, next_carry)),
                            label + ": local carry identity")
                    mirror = scale(mul(inverse, carry), -1)
                    back_digit, back_carry = step(inverse, mirror, a, digits)
                    require(back_digit == b and back_carry == scale(mul(inverse, next_carry), -1),
                            label + ": inverse edge mirror")
                    mirror_edges += 1
            for b, (a, next_carry) in zip(digits, edges[carry]):
                following[next_carry] += weight
                output_counts[a] += weight
                mixed_sum += weight * a * b
        require(all(output_counts[a] == total for a in digits), label + ": output marginal")
        observed_m = F(mixed_sum, total * 5)
        predicted_m = initial_m if n - 1 < h else mu * mu
        require(observed_m == predicted_m, label + ": prefix cross moment")
        counts = dict(following)
        total *= 5
        require(sum(counts.values()) == total, label + ": total word weight")
        if len(counts) > STATE_LIMIT:
            raise Incomplete("50000-state audit budget exceeded")
        max_support = max(max_support, len(counts))
        for carry in counts:
            if carry not in q_values:
                q = quadratic(carry)
                require(q == trace(mul(carry, conjugate(carry))) and q >= 0,
                        label + ": state quadratic form")
                q_values[carry] = q
        observed = F(sum(weight * q_values[carry] for carry, weight in counts.items()), total)
        require(observed == predicted, label + ": finite moment formula")
        observed_mean = tuple(F(sum(weight * carry[j] for carry, weight in counts.items()), total)
                              for j in range(4))
        require(observed_mean == expected_mean, label + ": mean carry vector")
        residues = [0] * 5
        for carry, weight in counts.items():
            residues[sum(carry) % 5] += weight
        require(residues == ([total, 0, 0, 0, 0] if n < h else [total // 5] * 5),
                label + ": delayed residue uniformity")
        if n >= h:
            require(abs(observed - limit) <= tail, label + ": rational tail bound")
            tail_checks += 1
        if n <= BRUTE_N:
            snapshots[n] = counts.copy()
        digest.update(json.dumps([label, n, fraction_pair(observed), fraction_pair(observed_m),
                                  len(counts)], separators=(",", ":")).encode() + b"\n")
    closure = None
    if digits == COUNTS and label in ("counts:J", "counts:J_inverse"):
        require(len(edges) == 1649, label + ": known complete carry count")
        vertices = set(edges)
        require({target for row in edges.values() for _, target in row} == vertices,
                label + ": carry closure")
        distance = {ZERO: 0}
        pending = deque([ZERO])
        while pending:
            state = pending.popleft()
            for _, target in edges[state]:
                if target not in distance:
                    distance[target] = distance[state] + 1
                    pending.append(target)
        require(set(distance) == vertices and max(distance.values()) == 28,
                label + ": first-reach depth")
        expected_max = 274 if label == "counts:J" else 706
        require(max(q_values[x] for x in vertices) == expected_max, label + ": maximum Q")
        closure = {"states": len(vertices), "edges": 5 * len(vertices),
                   "maximum_first_reach": max(distance.values()), "maximum_Q": expected_max}
    brute = brute_audit(u, digits, snapshots, deadline)
    return {"case": label, "h": h, "s": s, "initial_m": fraction_pair(initial_m),
            "limit": fraction_pair(limit), "finite_moment_checks": MAX_N,
            "tail_checks": tail_checks, "maximum_support": max_support,
            "mirror_edges": mirror_edges, "brute_words": brute[0],
            "off_diagonal_mixed_checks": brute[1], "cross_covariance_checks": brute[2],
            "mean_at_N100": fraction_pair(observed), "known_closure": closure}


def family_audit():
    rows = []
    distinct_units = set()
    for sign, k, m in product((1, -1), range(5), range(-3, 4)):
        real = power(PHI if m >= 0 else PHI_INV, abs(m))
        u = scale(mul(power(ZETA, k), real), sign)
        require(u not in distinct_units, "duplicate unit in the 70-parameter family")
        distinct_units.add(u)
        inverse_real = power(PHI_INV if m >= 0 else PHI, abs(m))
        inverse = scale(mul(power(ZETA, (-k) % 5), inverse_real), sign)
        require(mul(u, inverse) == ONE, "family inverse")
        depths = []
        for digits in (COUNTS, BALANCED):
            s = representative(sum(u), digits)
            h = valuation_from_integer(u, s)
            expected_h = 1 if k else (2 if m else None)
            if expected_h is None:
                require(h not in (1, 2, 3), "rational unit incorrectly admitted")
            else:
                require(h == expected_h, "family mixing depth")
            depths.append(h)
        if k == 0 and m == 0:
            continue
        q_count = 4 * quadratic(sub(u, ONE)) + 2 * quadratic(mul(u, J_INV)) + 12
        q_balanced = 2 * quadratic(mul(u, J_INV)) + 12
        require(q_count >= 36 and q_balanced >= 20, "family lower bound")
        rows.append((sign, k, m, q_count, q_balanced, depths[0]))
    require(len(distinct_units) == 70 and len(rows) == 68, "family admission count")
    counting_min = sorted((s, k, m) for s, k, m, qc, _, _ in rows if qc == 36)
    balanced_min = sorted((s, k, m) for s, k, m, _, qb, _ in rows if qb == 20)
    require(counting_min == [(1, 1, -1), (1, 4, -1)], "counting minimizers")
    require(balanced_min == sorted(product((1, -1), range(5), (-1,))), "balanced minimizers")
    require(sum(h == 1 for *_, h in rows) == 56 and sum(h == 2 for *_, h in rows) == 12,
            "family depth partition")
    return {"examined": 70, "admitted": 68, "depth_one": 56, "depth_two": 12,
            "counting_minimizers": counting_min, "balanced_minimizers": balanced_min,
            "rows_sha256": sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()}


def negative_controls():
    checks = 0
    for u in (ONE, scale(ONE, -1)):
        for b in BALANCED:
            a, carry = step(u, ZERO, b, BALANCED)
            require(carry == ZERO and a == u[0] * b, "balanced rational zero-carry control")
            checks += 1
        algebraic_functional = 2 * quadratic(mul(u, J_INV)) + 12
        require(algebraic_functional == 24, "unadmitted functional distinction")
    excluded = []
    for label, u in (("one", ONE), ("minus_one", scale(ONE, -1)),
                     ("phi_power_five", power(PHI, 5))):
        for digits in (COUNTS, BALANCED):
            try:
                exact_predictions(u, digits)
            except ValueError:
                excluded.append([label, "counts" if digits == COUNTS else "balanced"])
            else:
                raise Discrepancy("unadmitted unit reached the prediction formula")
    require(power(PHI, 5) == add(scale(PHI, 5), scale(ONE, 3)), "phi fifth-power identity")
    for digits in (COUNTS, BALANCED):
        s = representative(sum(power(PHI, 5)), digits)
        require(valuation_from_integer(power(PHI, 5), s) == 4, "phi^5 boundary depth")
    return {"zero_carry_transition_checks": checks,
            "zero_carry_scope": "all word lengths by zero-state closure",
            "rejected_prediction_cases": excluded,
            "phi_power_five_depth": 4, "balanced_rational_actual_Q": 0,
            "balanced_rational_unadmitted_functional": 24}


def main():
    deadline = monotonic() + TIME_LIMIT_SECONDS
    ring_preflight()
    family = family_audit()
    controls = negative_controls()
    zeta_inverse = power(ZETA, 4)
    base = [("zeta", ZETA, zeta_inverse, 64, 24),
            ("phi", PHI, PHI_INV, 64, 40),
            ("J", J, J_INV, 36, 20),
            ("J_inverse", J_INV, J, 64, 40),
            ("phi_inverse", PHI_INV, PHI, 76, 20)]
    cases = [("counts:" + name, u, inv, COUNTS, q0) for name, u, inv, q0, _ in base]
    cases += [("balanced:" + name, u, inv, BALANCED, q2) for name, u, inv, _, q2 in base]
    cases += [("balanced:minus_phi", scale(PHI, -1), scale(PHI_INV, -1), BALANCED, 40),
              ("balanced:minus_phi_inverse", scale(PHI_INV, -1), scale(PHI, -1), BALANCED, 20)]
    digest = sha256()
    summaries = [audit_case(*case, deadline, digest) for case in cases]
    checkpoint(deadline)
    result = {"schema": "twistj-carry-moment-audit-v1", "status": "PASS",
              "scientific_status": "NON-CANONICAL", "maximum_N": MAX_N,
              "finite_moment_checks": sum(x["finite_moment_checks"] for x in summaries),
              "tail_checks": sum(x["tail_checks"] for x in summaries),
              "brute_words": sum(x["brute_words"] for x in summaries),
              "facts_sha256": digest.hexdigest(), "family": family,
              "negative_controls": controls, "cases": summaries}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Incomplete as error:
        print("INCOMPLETE: " + str(error), file=sys.stderr)
        raise SystemExit(2)
    except Discrepancy as error:
        print("FALSIFIER: " + str(error), file=sys.stderr)
        raise SystemExit(1)
