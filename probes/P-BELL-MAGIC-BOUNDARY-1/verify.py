#!/usr/bin/env python3
"""Exact finite CHSH optimization for the zeta_5 and zeta_8 phase sets.

PRE-PIN DRAFT: do not execute the formal gate before the preregistration pin.
Standard library only. No floating-point arithmetic is used.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import isqrt
import sys


Q = Fraction
CHECKS = []


def check(tag, description, condition):
    CHECKS.append((tag, description, bool(condition)))


@dataclass(frozen=True)
class Quad:
    """An exact element a + b sqrt(d), for positive square-free d."""

    a: Fraction
    b: Fraction
    d: int

    def __add__(self, other):
        assert self.d == other.d
        return Quad(self.a + other.a, self.b + other.b, self.d)

    def __sub__(self, other):
        assert self.d == other.d
        return Quad(self.a - other.a, self.b - other.b, self.d)

    def __neg__(self):
        return Quad(-self.a, -self.b, self.d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Q(other)
        if isinstance(other, Fraction):
            return Quad(self.a * other, self.b * other, self.d)
        assert self.d == other.d
        return Quad(
            self.a * other.a + self.d * self.b * other.b,
            self.a * other.b + self.b * other.a,
            self.d,
        )

    __rmul__ = __mul__


def qsign(value):
    return (value > 0) - (value < 0)


def quad_sign(value):
    """Return the exact sign of a + b sqrt(d)."""

    a, b, d = value.a, value.b, value.d
    if not b:
        return qsign(a)
    if not a:
        return qsign(b)
    if qsign(a) == qsign(b):
        return qsign(a)
    square_difference = a * a - d * b * b
    if not square_difference:
        # This cannot occur for nonzero rational a,b and square-free d,
        # but retaining the branch makes the sign routine total.
        return 0
    return qsign(a) if square_difference > 0 else qsign(b)


def quad_compare(left, right):
    return quad_sign(left - right)


def quad_abs(value):
    return value if quad_sign(value) >= 0 else -value


def qtext(value):
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def quad_text(value):
    """Stable closed-form text for a + b sqrt(d)."""

    if not value.b:
        return qtext(value.a)
    magnitude = abs(value.b)
    radical = f"sqrt({value.d})" if magnitude == 1 else (
        f"{qtext(magnitude)}*sqrt({value.d})"
    )
    signed_radical = radical if value.b > 0 else f"-{radical}"
    if not value.a:
        return signed_radical
    operator = "+" if value.b > 0 else "-"
    return f"{qtext(value.a)} {operator} {radical}"


def phase_table(n):
    """Exact table Re(zeta_n^k) in the positive real embedding."""

    if n == 5:
        return (
            Quad(Q(1), Q(0), 5),
            Quad(Q(-1, 4), Q(1, 4), 5),
            Quad(Q(-1, 4), Q(-1, 4), 5),
            Quad(Q(-1, 4), Q(-1, 4), 5),
            Quad(Q(-1, 4), Q(1, 4), 5),
        )
    if n == 8:
        return (
            Quad(Q(1), Q(0), 2),
            Quad(Q(0), Q(1, 2), 2),
            Quad(Q(0), Q(0), 2),
            Quad(Q(0), Q(-1, 2), 2),
            Quad(Q(-1), Q(0), 2),
            Quad(Q(0), Q(-1, 2), 2),
            Quad(Q(0), Q(0), 2),
            Quad(Q(0), Q(1, 2), 2),
        )
    raise ValueError("the preregistered phase sets are n = 5 and n = 8")


def audit_phase_table(n, table):
    one = Quad(Q(1), Q(0), table[0].d)
    zero = Quad(Q(0), Q(0), table[0].d)
    two = Q(2)
    symmetric = all(table[k] == table[(-k) % n] for k in range(n))
    recurrence = all(
        two * table[1] * table[k]
        == table[(k + 1) % n] + table[(k - 1) % n]
        for k in range(n)
    )
    orbit_sum = zero
    for value in table:
        orbit_sum = orbit_sum + value
    bounded = all(
        quad_compare(value, -one) >= 0 and quad_compare(value, one) <= 0
        for value in table
    )
    return (
        len(table) == n
        and table[0] == one
        and symmetric
        and recurrence
        and orbit_sum == zero
        and bounded
    )


def correlation(table, a, b):
    return table[(a - b) % len(table)]


def chsh(table, settings):
    a0, a1, b0, b1 = settings
    raw = (
        correlation(table, a0, b0)
        + correlation(table, a0, b1)
        + correlation(table, a1, b0)
        - correlation(table, a1, b1)
    )
    return quad_abs(raw)


def maximize_full(n, table):
    zero = Quad(Q(0), Q(0), table[0].d)
    best = zero
    maximizers = []
    count = 0
    for settings in product(range(n), repeat=4):
        count += 1
        value = chsh(table, settings)
        comparison = quad_compare(value, best)
        if comparison > 0:
            best = value
            maximizers = [settings]
        elif comparison == 0:
            maximizers.append(settings)
    return best, tuple(maximizers), count


def maximize_reduced(n, table):
    zero = Quad(Q(0), Q(0), table[0].d)
    best = zero
    maximizers = []
    count = 0
    for a1, b0, b1 in product(range(n), repeat=3):
        settings = (0, a1, b0, b1)
        count += 1
        value = chsh(table, settings)
        comparison = quad_compare(value, best)
        if comparison > 0:
            best = value
            maximizers = [settings]
        elif comparison == 0:
            maximizers.append(settings)
    return best, tuple(maximizers), count


def normalize_global_phase(settings, n):
    shift = settings[0]
    return tuple((value - shift) % n for value in settings)


def audit_quotient(n, full_maximizers, reduced_maximizers):
    reduced_set = set(reduced_maximizers)
    lift_counts = {settings: 0 for settings in reduced_maximizers}
    for settings in full_maximizers:
        normalized = normalize_global_phase(settings, n)
        if normalized not in reduced_set:
            return False
        lift_counts[normalized] += 1
    return (
        len(full_maximizers) == n * len(reduced_maximizers)
        and all(count == n for count in lift_counts.values())
    )


def sqrt_interval(d, denominator):
    """Certified rational lower and upper bounds for positive sqrt(d)."""

    scaled_square = d * denominator * denominator
    floor = isqrt(scaled_square)
    lower = Q(floor, denominator)
    if floor * floor == scaled_square:
        return lower, lower
    return lower, Q(floor + 1, denominator)


def compare_qsqrt5_qsqrt2(left, right):
    """Exact comparison of left in Q(sqrt5) and right in Q(sqrt2)."""

    assert left.d == 5 and right.d == 2
    constant = left.a - right.a
    terms = ((left.b, 5), (-right.b, 2))

    # Q(sqrt(5)) intersects Q(sqrt(2)) in Q. Hence equality is possible
    # here exactly when both radical coefficients vanish and constants agree.
    if not left.b and not right.b:
        return qsign(constant)

    denominator = 10
    for _ in range(64):
        lower = constant
        upper = constant
        for coefficient, d in terms:
            root_lower, root_upper = sqrt_interval(d, denominator)
            if coefficient >= 0:
                lower += coefficient * root_lower
                upper += coefficient * root_upper
            else:
                lower += coefficient * root_upper
                upper += coefficient * root_lower
        if lower > 0:
            return 1
        if upper < 0:
            return -1
        denominator *= 10
    raise ArithmeticError("exact cross-field sign was not isolated")


def tuple_text(settings):
    return "(" + ",".join(str(value) for value in settings) + ")"


def main():
    tables = {n: phase_table(n) for n in (5, 8)}
    check(
        "PHASE-TABLES",
        "both root-of-unity real-part tables satisfy all exact identities",
        all(audit_phase_table(n, tables[n]) for n in (5, 8)),
    )

    results = {}
    for n in (5, 8):
        full_value, full_maximizers, full_count = maximize_full(n, tables[n])
        reduced_value, reduced_maximizers, reduced_count = maximize_reduced(
            n, tables[n]
        )
        exact_count = full_count == n ** 4 and reduced_count == n ** 3
        same_value = full_value == reduced_value
        quotient_ok = audit_quotient(n, full_maximizers, reduced_maximizers)
        check(
            f"ENUM-{n}",
            f"full {n ** 4} and quotient {n ** 3} enumerations agree exactly",
            exact_count and same_value and quotient_ok,
        )
        results[n] = (
            full_value,
            full_maximizers,
            reduced_maximizers,
            full_count,
            reduced_count,
        )

    m5 = results[5][0]
    m8 = results[8][0]
    expected_m5 = Quad(Q(1, 2), Q(1), 5)
    expected_m8 = Quad(Q(0), Q(2), 2)
    closed_forms_match = m5 == expected_m5 and m8 == expected_m8
    above_two_5 = quad_compare(m5, Quad(Q(2), Q(0), 5)) > 0
    above_two_8 = quad_compare(m8, Quad(Q(2), Q(0), 2)) > 0
    ordered = compare_qsqrt5_qsqrt2(m5, m8) < 0
    scientific_positive = (
        closed_forms_match and above_two_5 and above_two_8 and ordered
    )

    print("TWIST-J Bell magic boundary probe")
    print("functional E_n(a,b)=Re(zeta_n^(a-b));"
          " S_n=abs(E00+E01+E10-E11)")
    print("exact arithmetic Q(sqrt(5)) and Q(sqrt(2)); no floats")
    print("prediction M_5=1/2+sqrt(5); M_8=2*sqrt(2)")
    for index, (tag, description, ok) in enumerate(CHECKS, 1):
        print(f"{'PASS' if ok else 'FAIL'} {index:02d} {tag:<12} {description}")

    for n in (5, 8):
        value, full_maximizers, reduced_maximizers, full_count, reduced_count = (
            results[n]
        )
        print(
            f"MAX n={n} value={quad_text(value)}"
            f" full_space={full_count} full_maximizers={len(full_maximizers)}"
            f" quotient_space={reduced_count}"
            f" quotient_maximizers={len(reduced_maximizers)}"
        )
        print(
            f"REPS n={n} a0=0 "
            + ";".join(tuple_text(settings) for settings in reduced_maximizers)
        )

    if closed_forms_match:
        print("PREDICTION MATCH both preregistered closed forms")
    else:
        print("PREDICTION MISMATCH at least one preregistered closed form fired")

    if scientific_positive:
        print("DECISION POSITIVE closed forms match and 2 < M_5 < M_8")
    else:
        print("DECISION NEGATIVE a preregistered prediction or comparison fired")

    passed = sum(ok for _, _, ok in CHECKS)
    print(f"RESULT {passed}/{len(CHECKS)} AUDIT CHECKS PASS")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
