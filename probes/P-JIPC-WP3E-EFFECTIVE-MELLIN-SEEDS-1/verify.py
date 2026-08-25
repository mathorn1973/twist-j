#!/usr/bin/env python3
"""Finite exact audit for the written WP3E effective Mellin-seed proof.

The theorem is carried by the accompanying written proof.  This zero-input
program only audits exact arithmetic, frozen definitions, quantitative proof
controls, and bounded sample enclosures used by that proof.
"""

from fractions import Fraction


class IntegrityFailure(Exception):
    pass


class ControlRejection(Exception):
    def __init__(self, gate):
        self.gate = gate
        super().__init__(gate)


def require(condition, gate):
    if not condition:
        raise IntegrityFailure(gate)


def scientific(condition, gate, fired):
    if not condition and gate not in fired:
        fired.append(gate)


def q(numerator, denominator=1):
    require(type(numerator) is int, "Q_NUMERATOR_TYPE")
    require(type(denominator) is int, "Q_DENOMINATOR_TYPE")
    require(denominator != 0, "Q_ZERO_DENOMINATOR")
    return Fraction(numerator, denominator)


def as_q(value):
    require(type(value) is int or type(value) is Fraction, "Q_VALUE_TYPE")
    return Fraction(value)


def floor_q(value):
    value = as_q(value)
    return value.numerator // value.denominator


def ceil_q(value):
    value = as_q(value)
    return -((-value.numerator) // value.denominator)


def pow2_minus(bits):
    require(type(bits) is int and bits >= 0, "DYADIC_BITS")
    return q(1, 1 << bits)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = as_q(lo)
        hi = lo if hi is None else as_q(hi)
        require(lo <= hi, "INTERVAL_ORDER")
        self.lo = lo
        self.hi = hi

    @staticmethod
    def point(value):
        return Interval(value)

    @property
    def width(self):
        return self.hi - self.lo

    @property
    def midpoint(self):
        return (self.lo + self.hi) / 2

    @property
    def radius(self):
        return self.width / 2

    @property
    def max_abs(self):
        return max(abs(self.lo), abs(self.hi))

    def contains(self, value):
        value = as_q(value)
        return self.lo <= value <= self.hi

    def overlaps(self, other):
        other = as_interval(other)
        return not (self.hi < other.lo or other.hi < self.lo)

    def widen(self, error):
        error = as_q(error)
        require(error >= 0, "INTERVAL_WIDEN_NONNEGATIVE")
        return Interval(self.lo - error, self.hi + error)

    def outward_dyadic(self, bits):
        require(type(bits) is int and bits >= 0, "INTERVAL_DYADIC_BITS")
        denominator = 1 << bits
        lo = q(floor_q(self.lo * denominator), denominator)
        hi = q(ceil_q(self.hi * denominator), denominator)
        return Interval(lo, hi)

    def reciprocal(self):
        require(not (self.lo <= 0 <= self.hi), "INTERVAL_RECIPROCAL_ZERO")
        return Interval(q(1) / self.hi, q(1) / self.lo)

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * as_interval(other).reciprocal()


def as_interval(value):
    if type(value) is Interval:
        return value
    return Interval.point(value)


class ComplexBox:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = as_interval(re)
        self.im = as_interval(im)

    @staticmethod
    def point(re=0, im=0):
        return ComplexBox(Interval.point(re), Interval.point(im))

    @property
    def radius(self):
        return max(self.re.radius, self.im.radius)

    def overlaps(self, other):
        require(type(other) is ComplexBox, "COMPLEX_BOX_TYPE")
        return self.re.overlaps(other.re) and self.im.overlaps(other.im)

    def widen(self, error):
        error = as_q(error)
        require(error >= 0, "COMPLEX_WIDEN_NONNEGATIVE")
        return ComplexBox(self.re.widen(error), self.im.widen(error))

    def scale(self, real_factor):
        real_factor = as_interval(real_factor)
        return ComplexBox(self.re * real_factor, self.im * real_factor)

    def __add__(self, other):
        other = as_complex_box(other)
        return ComplexBox(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return ComplexBox(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-as_complex_box(other))

    def __mul__(self, other):
        other = as_complex_box(other)
        return ComplexBox(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__


def as_complex_box(value):
    if type(value) is ComplexBox:
        return value
    if type(value) is Interval:
        return ComplexBox(value, 0)
    return ComplexBox.point(value, 0)


def factorial(n):
    require(type(n) is int and n >= 0, "FACTORIAL_INPUT")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def exp_small_nonnegative(value, bits):
    value = as_q(value)
    require(0 <= value <= q(1, 2), "EXP_SMALL_DOMAIN")
    if value == 0:
        return Interval.point(1)
    target = pow2_minus(bits)
    term = q(1)
    total = q(1)
    index = 0
    while True:
        next_term = term * value / (index + 1)
        ratio = value / (index + 2)
        if ratio < 1:
            tail = next_term / (1 - ratio)
            if tail <= target:
                return Interval(total, total + tail)
        term = next_term
        total += term
        index += 1
        require(index <= 16384, "EXP_SMALL_TERMINATION")


def exp_nonnegative_point(value, bits):
    value = as_q(value)
    require(value >= 0, "EXP_NONNEGATIVE_DOMAIN")
    if value == 0:
        return Interval.point(1)
    reduced = value
    halvings = 0
    while reduced > q(1, 2):
        reduced /= 2
        halvings += 1
        require(halvings <= 4096, "EXP_RANGE_REDUCTION")
    work = bits + halvings + max(4, ceil_q(value)) + 4
    while True:
        result = exp_small_nonnegative(reduced, work + 2).outward_dyadic(work)
        for unused in range(halvings):
            result = (result * result).outward_dyadic(work)
        candidate = result.outward_dyadic(bits + 2)
        if candidate.width <= pow2_minus(bits):
            return candidate
        work += 6
        require(work <= bits + 4096, "EXP_POSITIVE_TERMINATION")


def exp_point(value, bits):
    value = as_q(value)
    if value >= 0:
        return exp_nonnegative_point(value, bits)
    decay = floor_q(-value)
    if decay >= bits:
        return Interval(0, pow2_minus(min(decay, bits + 64)))
    work = bits + 4
    while True:
        positive = exp_nonnegative_point(-value, work)
        candidate = positive.reciprocal().outward_dyadic(work)
        if candidate.width <= pow2_minus(bits):
            return candidate
        work += 4
        require(work <= bits + 4096, "EXP_NEGATIVE_TERMINATION")


def exp_interval(value, bits):
    value = as_interval(value)
    if value.hi <= -bits:
        decay = min(floor_q(-value.hi), bits + 64)
        return Interval(0, pow2_minus(decay))
    lo = exp_point(value.lo, bits + 2).lo
    hi = exp_point(value.hi, bits + 2).hi
    return Interval(lo, hi).outward_dyadic(bits)


def sin_point(value, bits):
    value = as_q(value)
    if value == 0:
        return Interval.point(0)
    absolute = abs(value)
    target = pow2_minus(bits)
    index = 0
    term = value
    total = term
    while True:
        error = absolute ** (2 * index + 2) / factorial(2 * index + 2)
        if error <= target:
            candidate = Interval(total - error, total + error).outward_dyadic(bits + 2)
            if candidate.width <= target:
                return candidate
        index += 1
        term *= -(value * value) / ((2 * index) * (2 * index + 1))
        total += term
        require(index <= 16384, "SIN_TERMINATION")


def cos_point(value, bits):
    value = as_q(value)
    absolute = abs(value)
    target = pow2_minus(bits)
    index = 0
    term = q(1)
    total = term
    while True:
        error = absolute ** (2 * index + 1) / factorial(2 * index + 1)
        if error <= target:
            candidate = Interval(total - error, total + error).outward_dyadic(bits + 2)
            if candidate.width <= target:
                return candidate
        index += 1
        term *= -(value * value) / ((2 * index - 1) * (2 * index))
        total += term
        require(index <= 16384, "COS_TERMINATION")


def sin_interval(value, bits):
    value = as_interval(value)
    return sin_point(value.midpoint, bits + 2).widen(value.radius)


def cos_interval(value, bits):
    value = as_interval(value)
    return cos_point(value.midpoint, bits + 2).widen(value.radius)


def complex_exp_box(value, bits):
    require(type(value) is ComplexBox, "COMPLEX_EXP_INPUT")
    real_exp = exp_interval(value.re, bits + 3)
    return ComplexBox(
        (real_exp * cos_interval(value.im, bits + 3)).outward_dyadic(bits),
        (real_exp * sin_interval(value.im, bits + 3)).outward_dyadic(bits),
    )


def atan_reciprocal_interval(base, terms):
    require(type(base) is int and base >= 2, "ATAN_BASE")
    require(type(terms) is int and terms >= 1, "ATAN_TERMS")
    total = q(0)
    for index in range(terms):
        term = q(1, (2 * index + 1) * (base ** (2 * index + 1)))
        total = total + term if index % 2 == 0 else total - term
    index = terms
    next_term = q(1, (2 * index + 1) * (base ** (2 * index + 1)))
    next_term = next_term if index % 2 == 0 else -next_term
    return Interval(min(total, total + next_term), max(total, total + next_term))


MACHIN_COEFFICIENTS = (16, 5, -4, 239)
P_STRICT_LOWER = q(3)
P_STRICT_UPPER = q(16, 5)
MIDPOINT_FACTOR = q(1, 4)
PANEL_START = 8
PANEL_MULTIPLIER = 2
ENTIRE_MARKER = "FINITE_MIDPOINT_EXPONENTIAL_SUM"
TCB_ID = "COMPLEX_BALL_MELLIN_TCB/v1"
CARRIER_RULE = "T_IS_CARRIED_BY_PREREG_WRITTEN_PROOF_NOT_THIS_AUDIT"


def machin_interval(bits):
    require(type(bits) is int and bits >= 0, "MACHIN_BITS")
    guard_machin_coefficients(MACHIN_COEFFICIENTS)
    coefficient_five, base_five, coefficient_239, base_239 = MACHIN_COEFFICIENTS
    terms = 1
    target = pow2_minus(bits)
    while True:
        atan_five = atan_reciprocal_interval(base_five, terms)
        atan_239 = atan_reciprocal_interval(base_239, terms)
        candidate = (
            coefficient_five * atan_five + coefficient_239 * atan_239
        ).outward_dyadic(bits + 3)
        if candidate.width <= target:
            return candidate
        terms += 1
        require(terms <= 4096, "MACHIN_TERMINATION")


SEED_ROWS = (
    ("E", q(2), q(1), q(0), q(1), "E_ONLY"),
    ("O", q(2), q(1), q(1), q(1), "O_ONLY"),
    ("C", q(4), q(2), q(0), q(2), "C_ONLY"),
)

EXPECTED_SEED_ROWS = (
    ("E", q(2), q(1), q(0), q(1), "E_ONLY"),
    ("O", q(2), q(1), q(1), q(1), "O_ONLY"),
    ("C", q(4), q(2), q(0), q(2), "C_ONLY"),
)

SEED_TUPLE_CONTROL = tuple(row[:5] for row in SEED_ROWS)
BRANCH_PROVENANCE_CONTROL = tuple((row[0], row[5]) for row in SEED_ROWS)
LEFT_TAIL_CONTROL = ("FLOOR_RATE_CUT", 2)
RIGHT_TAIL_CONTROL = ("EXP_MINUS_CUT", 2)
CUT_MINIMALITY_CONTROL = "FIRST_L_AND_R_MEETING_BUDGET"
MACHIN_BOUNDS_CONTROL = (P_STRICT_LOWER, P_STRICT_UPPER)
PANEL_REFINEMENT_CONTROL = (PANEL_START, PANEL_MULTIPLIER)


def seed_row(label):
    guard_seed_tuples(SEED_TUPLE_CONTROL)
    guard_branch_provenance(BRANCH_PROVENANCE_CONTROL)
    rows = [row for row in SEED_ROWS if row[0] == label]
    require(len(rows) == 1, "SEED_LOOKUP_" + label)
    return rows[0]


def left_tail_bound(label, sigma_min, cut):
    guard_left_tail(LEFT_TAIL_CONTROL)
    unused_method, dyadic_base = LEFT_TAIL_CONTROL
    unused_label, amplitude, multiplier, shift, unused_gaussian, unused_provenance = seed_row(label)
    sigma_min = as_q(sigma_min)
    require(type(cut) is int and cut >= 0, "LEFT_CUT")
    rate = multiplier * sigma_min + shift
    require(rate > 0, "LEFT_TAIL_RATE")
    exponent = max(0, floor_q(rate * cut))
    return amplitude * q(1, dyadic_base ** exponent) / rate


def right_tail_start(label, sigma_max):
    guard_machin_bounds(MACHIN_BOUNDS_CONTROL)
    unused_label, unused_amplitude, multiplier, shift, gaussian, unused_provenance = seed_row(label)
    sigma_max = as_q(sigma_max)
    growth = multiplier * sigma_max + shift
    return max(1, ceil_q((growth + 1) / (2 * gaussian * P_STRICT_LOWER)))


def right_tail_bound(label, cut):
    guard_right_tail(RIGHT_TAIL_CONTROL)
    unused_method, dyadic_base = RIGHT_TAIL_CONTROL
    unused_label, amplitude, unused_multiplier, unused_shift, unused_gaussian, unused_provenance = seed_row(label)
    require(type(cut) is int and cut >= 1, "RIGHT_CUT")
    return amplitude * q(1, dyadic_base ** cut)


def select_cuts(label, sigma_min, sigma_max, budget):
    guard_cut_minimality(CUT_MINIMALITY_CONTROL)
    budget = as_q(budget)
    require(budget > 0, "TAIL_BUDGET")
    left = 1
    while left_tail_bound(label, sigma_min, left) > budget:
        left += 1
        require(left <= 4096, "LEFT_CUT_TERMINATION")
    right = right_tail_start(label, sigma_max)
    while right_tail_bound(label, right) > budget:
        right += 1
        require(right <= 4096, "RIGHT_CUT_TERMINATION")
    return left, right


def seed_integrand_box(label, sigma, tau, u_interval, p_interval, bits):
    unused_label, amplitude, multiplier, shift, gaussian, unused_provenance = seed_row(label)
    sigma = as_q(sigma)
    tau = as_q(tau)
    u_interval = as_interval(u_interval)
    p_interval = as_interval(p_interval)
    exp_two_u = exp_interval(2 * u_interval, bits + 3)
    real_part = (multiplier * sigma + shift) * u_interval - gaussian * p_interval * exp_two_u
    imaginary_part = multiplier * tau * u_interval
    return complex_exp_box(ComplexBox(real_part, imaginary_part), bits + 3).scale(amplitude)


def finite_midpoint_sum(label, sigma, tau, left, right, panels, bits, p_interval):
    require(type(panels) is int and panels >= 1, "MIDPOINT_PANELS")
    lo = -q(left)
    hi = q(right)
    step = (hi - lo) / panels
    total = ComplexBox.point(0, 0)
    for index in range(panels):
        midpoint = lo + (2 * index + 1) * step / 2
        value = seed_integrand_box(
            label,
            sigma,
            tau,
            Interval.point(midpoint),
            p_interval,
            bits,
        )
        total += value.scale(step)
    return total


def derivative_bound(label, re_lo, re_hi, im_lo, im_hi, cell, bits):
    guard_machin_bounds(MACHIN_BOUNDS_CONTROL)
    unused_label, amplitude, multiplier, shift, gaussian, unused_provenance = seed_row(label)
    cell = as_interval(cell)
    real_coefficient = multiplier * Interval(re_lo, re_hi) + shift
    imaginary_bound = multiplier * max(abs(as_q(im_lo)), abs(as_q(im_hi)))
    p_interval = Interval(P_STRICT_LOWER, P_STRICT_UPPER)
    exp_two_u = exp_interval(2 * cell, bits + 4)
    real_exponent = real_coefficient * cell - gaussian * p_interval * exp_two_u
    envelope = exp_interval(real_exponent, bits + 4).hi
    coefficient_bound = real_coefficient.max_abs + imaginary_bound
    slope = coefficient_bound + 2 * gaussian * p_interval.hi * exp_two_u.hi
    return amplitude * slope * envelope


def global_derivative_bound(label, re_lo, re_hi, im_lo, im_hi, right, bits):
    guard_machin_bounds(MACHIN_BOUNDS_CONTROL)
    unused_label, amplitude, multiplier, shift, gaussian, unused_provenance = seed_row(label)
    re_lo = as_q(re_lo)
    re_hi = as_q(re_hi)
    im_lo = as_q(im_lo)
    im_hi = as_q(im_hi)
    require(type(right) is int and right >= 1, "GLOBAL_BOUND_RIGHT")
    real_size = max(abs(multiplier * re_lo + shift), abs(multiplier * re_hi + shift))
    imaginary_size = multiplier * max(abs(im_lo), abs(im_hi))
    z_bound = real_size + imaginary_size
    exp_two_right = exp_point(2 * right, bits + 4).hi
    growth = multiplier * re_hi + shift
    compact_envelope = exp_point(growth * right, bits + 4).hi
    return amplitude * compact_envelope * (
        z_bound + 2 * gaussian * P_STRICT_UPPER * exp_two_right
    )


def cellwise_midpoint_error(label, re_lo, re_hi, im_lo, im_hi, left, right, panels, bits):
    guard_midpoint_factor(MIDPOINT_FACTOR)
    require(type(panels) is int and panels >= 1, "ERROR_PANELS")
    lo = -q(left)
    hi = q(right)
    step = (hi - lo) / panels
    total = q(0)
    global_bound = global_derivative_bound(
        label, re_lo, re_hi, im_lo, im_hi, right, bits
    )
    for index in range(panels):
        cell = Interval(lo + index * step, lo + (index + 1) * step)
        local_bound = derivative_bound(label, re_lo, re_hi, im_lo, im_hi, cell, bits)
        executed_bound = min(local_bound, global_bound)
        require(executed_bound <= global_bound, "CELL_BOUND_GLOBAL_DOMINATION")
        total += executed_bound * step * step * MIDPOINT_FACTOR
    return total


class UniformName:
    __slots__ = (
        "label",
        "provenance",
        "re_lo",
        "re_hi",
        "im_lo",
        "im_hi",
        "precision_bits",
        "left",
        "right",
        "panels",
        "tail_error",
        "quadrature_error",
        "previous_quadrature_error",
        "certified",
        "entire_expression",
    )

    def __init__(
        self,
        label,
        provenance,
        re_lo,
        re_hi,
        im_lo,
        im_hi,
        precision_bits,
        left,
        right,
        panels,
        tail_error,
        quadrature_error,
        previous_quadrature_error,
        certified,
    ):
        guard_entire_marker(ENTIRE_MARKER)
        self.label = label
        self.provenance = provenance
        self.re_lo = as_q(re_lo)
        self.re_hi = as_q(re_hi)
        self.im_lo = as_q(im_lo)
        self.im_hi = as_q(im_hi)
        self.precision_bits = precision_bits
        self.left = left
        self.right = right
        self.panels = panels
        self.tail_error = as_q(tail_error)
        self.quadrature_error = as_q(quadrature_error)
        self.previous_quadrature_error = (
            None if previous_quadrature_error is None else as_q(previous_quadrature_error)
        )
        self.certified = certified
        self.entire_expression = ENTIRE_MARKER

    @property
    def uniform_error(self):
        return self.tail_error + self.quadrature_error


def build_uniform_name(label, re_lo, re_hi, im_lo, im_hi, bits):
    guard_panel_refinement(PANEL_REFINEMENT_CONTROL)
    re_lo = as_q(re_lo)
    re_hi = as_q(re_hi)
    im_lo = as_q(im_lo)
    im_hi = as_q(im_hi)
    require(0 < re_lo <= re_hi, "COMPACT_REAL_DOMAIN")
    require(im_lo <= im_hi, "COMPACT_IMAGINARY_DOMAIN")
    require(type(bits) is int and bits >= 0, "NAME_BITS")
    row = seed_row(label)
    target = pow2_minus(bits)
    tail_budget = target / 8
    left, right = select_cuts(label, re_lo, re_hi, tail_budget)
    tails = left_tail_bound(label, re_lo, left) + right_tail_bound(label, right)
    panels = PANEL_START
    previous = None
    while panels <= (1 << 20):
        error = cellwise_midpoint_error(
            label, re_lo, re_hi, im_lo, im_hi, left, right, panels, bits + 12
        )
        if tails + error <= target / 2:
            return UniformName(
                label,
                row[5],
                re_lo,
                re_hi,
                im_lo,
                im_hi,
                bits,
                left,
                right,
                panels,
                tails,
                error,
                previous,
                True,
            )
        previous = error
        panels *= PANEL_MULTIPLIER
    return UniformName(
        label,
        row[5],
        re_lo,
        re_hi,
        im_lo,
        im_hi,
        bits,
        left,
        right,
        panels // 2,
        tails,
        previous,
        None,
        False,
    )


def evaluate_uniform_name(name, sigma, tau, bits):
    require(type(name) is UniformName, "NAME_TYPE")
    sigma = as_q(sigma)
    tau = as_q(tau)
    require(name.re_lo <= sigma <= name.re_hi, "NAME_POINT_REAL")
    require(name.im_lo <= tau <= name.im_hi, "NAME_POINT_IMAGINARY")
    require(type(bits) is int and 0 <= bits <= name.precision_bits, "NAME_EVALUATION_BITS")
    work = bits + 12
    last = None
    for unused in range(64):
        p_interval = machin_interval(work + 4)
        core = finite_midpoint_sum(
            name.label,
            sigma,
            tau,
            name.left,
            name.right,
            name.panels,
            work,
            p_interval,
        )
        last = core.widen(name.uniform_error)
        if last.radius <= pow2_minus(bits):
            return last, True
        work += 6
    require(last is not None, "NAME_EVALUATION_EMPTY")
    return last, False


def independent_e(re_lo, re_hi, im_lo, im_hi, bits):
    return build_uniform_name("E", re_lo, re_hi, im_lo, im_hi, bits)


def independent_o(re_lo, re_hi, im_lo, im_hi, bits):
    return build_uniform_name("O", re_lo, re_hi, im_lo, im_hi, bits)


def independent_c(re_lo, re_hi, im_lo, im_hi, bits):
    return build_uniform_name("C", re_lo, re_hi, im_lo, im_hi, bits)


PROOF_CONTROLS = (
    ("MACHIN_COEFFICIENTS", MACHIN_COEFFICIENTS),
    ("MACHIN_STRICT_BOUNDS", MACHIN_BOUNDS_CONTROL),
    ("SEED_TUPLES", SEED_TUPLE_CONTROL),
    ("BRANCH_PROVENANCE", BRANCH_PROVENANCE_CONTROL),
    ("LEFT_TAIL_FORMULA", LEFT_TAIL_CONTROL),
    ("RIGHT_TAIL_FORMULA", RIGHT_TAIL_CONTROL),
    ("CUT_MINIMALITY", CUT_MINIMALITY_CONTROL),
    ("MIDPOINT_CELL_ERROR", MIDPOINT_FACTOR),
    ("PANEL_REFINEMENT", PANEL_REFINEMENT_CONTROL),
    ("FINITE_ENTIRE_APPROXIMANT", ENTIRE_MARKER),
    ("RELATIVE_TCB_SCOPE", TCB_ID),
    ("WRITTEN_PROOF_CARRIER", CARRIER_RULE),
)


def reject_control(condition, gate):
    if not condition:
        raise ControlRejection(gate)


def guard_machin_coefficients(value):
    reject_control(value == (16, 5, -4, 239), "MACHIN_COEFFICIENTS")


def guard_machin_bounds(value):
    reject_control(value == (q(3), q(16, 5)), "MACHIN_STRICT_BOUNDS")


def guard_seed_tuples(value):
    expected = (
        ("E", q(2), q(1), q(0), q(1)),
        ("O", q(2), q(1), q(1), q(1)),
        ("C", q(4), q(2), q(0), q(2)),
    )
    reject_control(value == expected, "SEED_TUPLES")


def guard_branch_provenance(value):
    expected = (("E", "E_ONLY"), ("O", "O_ONLY"), ("C", "C_ONLY"))
    reject_control(value == expected, "BRANCH_PROVENANCE")


def guard_left_tail(value):
    reject_control(value == ("FLOOR_RATE_CUT", 2), "LEFT_TAIL_FORMULA")


def guard_right_tail(value):
    reject_control(value == ("EXP_MINUS_CUT", 2), "RIGHT_TAIL_FORMULA")


def guard_cut_minimality(value):
    reject_control(value == "FIRST_L_AND_R_MEETING_BUDGET", "CUT_MINIMALITY")


def guard_midpoint_factor(value):
    reject_control(value == q(1, 4), "MIDPOINT_CELL_ERROR")


def guard_panel_refinement(value):
    reject_control(value == (8, 2), "PANEL_REFINEMENT")


def guard_entire_marker(value):
    reject_control(value == "FINITE_MIDPOINT_EXPONENTIAL_SUM",
                   "FINITE_ENTIRE_APPROXIMANT")


def guard_tcb_scope(value):
    reject_control(value == "COMPLEX_BALL_MELLIN_TCB/v1", "RELATIVE_TCB_SCOPE")


def guard_written_carrier(value):
    reject_control(value == "T_IS_CARRIED_BY_PREREG_WRITTEN_PROOF_NOT_THIS_AUDIT",
                   "WRITTEN_PROOF_CARRIER")


def enforce_control(gate, value):
    guards = (
        ("MACHIN_COEFFICIENTS", guard_machin_coefficients),
        ("MACHIN_STRICT_BOUNDS", guard_machin_bounds),
        ("SEED_TUPLES", guard_seed_tuples),
        ("BRANCH_PROVENANCE", guard_branch_provenance),
        ("LEFT_TAIL_FORMULA", guard_left_tail),
        ("RIGHT_TAIL_FORMULA", guard_right_tail),
        ("CUT_MINIMALITY", guard_cut_minimality),
        ("MIDPOINT_CELL_ERROR", guard_midpoint_factor),
        ("PANEL_REFINEMENT", guard_panel_refinement),
        ("FINITE_ENTIRE_APPROXIMANT", guard_entire_marker),
        ("RELATIVE_TCB_SCOPE", guard_tcb_scope),
        ("WRITTEN_PROOF_CARRIER", guard_written_carrier),
    )
    for expected_gate, guard in guards:
        if gate == expected_gate:
            guard(value)
            return
    raise ControlRejection("UNKNOWN_CONTROL")


def negative_control_value(gate):
    if gate == "MACHIN_COEFFICIENTS":
        return (15, 5, -4, 239)
    if gate == "MACHIN_STRICT_BOUNDS":
        return (q(3), q(17, 5))
    if gate == "SEED_TUPLES":
        return (
            ("E", q(2), q(1), q(0), q(1)),
            ("O", q(2), q(1), q(0), q(1)),
            ("C", q(4), q(2), q(0), q(2)),
        )
    if gate == "BRANCH_PROVENANCE":
        return (("E", "E_ONLY"), ("O", "E_ONLY"), ("C", "C_ONLY"))
    if gate == "LEFT_TAIL_FORMULA":
        return ("CEIL_RATE_CUT", 2)
    if gate == "RIGHT_TAIL_FORMULA":
        return ("EXP_MINUS_CUT", 3)
    if gate == "CUT_MINIMALITY":
        return "ANY_ACCEPTED_CUT"
    if gate == "MIDPOINT_CELL_ERROR":
        return q(1, 2)
    if gate == "PANEL_REFINEMENT":
        return (8, 3)
    if gate == "FINITE_ENTIRE_APPROXIMANT":
        return "FINITE_POINT_SAMPLE_TABLE"
    if gate == "RELATIVE_TCB_SCOPE":
        return "UNFROZEN_TCB"
    if gate == "WRITTEN_PROOF_CARRIER":
        return "FINITE_AUDIT_CARRIES_T"
    require(False, "UNKNOWN_NEGATIVE_CONTROL")


def audit_control_mutations():
    require(type(PROOF_CONTROLS) is tuple and len(PROOF_CONTROLS) == 12,
            "PROOF_CONTROL_BASELINE_SHAPE")
    for gate, value in PROOF_CONTROLS:
        enforce_control(gate, value)
    rejected = 0
    for gate, value in PROOF_CONTROLS:
        try:
            enforce_control(gate, negative_control_value(gate))
        except ControlRejection as error:
            require(error.gate == gate, "PROOF_CONTROL_WRONG_GUARD_" + gate)
            rejected += 1
        else:
            require(False, "PROOF_CONTROL_ACCEPTED_" + gate)
    require(rejected == 12, "PROOF_CONTROL_MUTATIONS")
    return rejected


def audit_arithmetic():
    interval = Interval(q(1, 3), q(2, 3))
    require((interval + interval).contains(1), "ARITHMETIC_INTERVAL_ADD")
    require((interval * interval).contains(q(1, 4)), "ARITHMETIC_INTERVAL_MUL")
    require(interval.reciprocal().contains(2), "ARITHMETIC_INTERVAL_RECIPROCAL")
    require(interval.outward_dyadic(4).lo <= interval.lo, "ARITHMETIC_DYADIC_LO")
    require(interval.outward_dyadic(4).hi >= interval.hi, "ARITHMETIC_DYADIC_HI")
    product = ComplexBox.point(1, 1) * ComplexBox.point(1, -1)
    require(product.re.contains(2) and product.im.contains(0), "ARITHMETIC_COMPLEX_MUL")


def audit_cut_contract(name, fired):
    target = pow2_minus(name.precision_bits)
    budget = target / 8
    scientific(left_tail_bound(name.label, name.re_lo, name.left) <= budget,
               "LEFT_TAIL_BUDGET_" + name.label, fired)
    if name.left > 1:
        scientific(left_tail_bound(name.label, name.re_lo, name.left - 1) > budget,
                   "LEFT_CUT_MINIMALITY_" + name.label, fired)
    start = right_tail_start(name.label, name.re_hi)
    scientific(name.right >= start, "RIGHT_CUT_THRESHOLD_" + name.label, fired)
    scientific(right_tail_bound(name.label, name.right) <= budget,
               "RIGHT_TAIL_BUDGET_" + name.label, fired)
    if name.right > start:
        scientific(right_tail_bound(name.label, name.right - 1) > budget,
                   "RIGHT_CUT_MINIMALITY_" + name.label, fired)
    scientific(name.tail_error <= target / 4, "COMBINED_TAIL_BUDGET_" + name.label, fired)


def audit_midpoint_contract(name, fired):
    global_bound = global_derivative_bound(
        name.label,
        name.re_lo,
        name.re_hi,
        name.im_lo,
        name.im_hi,
        name.right,
        name.precision_bits + 12,
    )
    length = q(name.left + name.right)
    global_error = global_bound * length * length * MIDPOINT_FACTOR / name.panels
    scientific(name.quadrature_error <= global_error,
               "MIDPOINT_GLOBAL_DOMINATION_" + name.label, fired)


def main():
    fired = []
    guard_tcb_scope(TCB_ID)
    guard_written_carrier(CARRIER_RULE)
    audit_arithmetic()

    p_interval = machin_interval(16)
    scientific(p_interval.width <= pow2_minus(16), "MACHIN_WIDTH", fired)
    scientific(p_interval.lo > 3 and p_interval.hi < q(16, 5), "MACHIN_STRICT_BOUNDS", fired)
    scientific(SEED_ROWS == EXPECTED_SEED_ROWS, "FIXED_SEED_TUPLES", fired)

    constructors = (
        (independent_e, "E", "E_ONLY"),
        (independent_o, "O", "O_ONLY"),
        (independent_c, "C", "C_ONLY"),
    )
    compact_names = []
    for constructor, label, provenance in constructors:
        name = constructor(q(1), q(3, 2), q(-1, 2), q(1, 2), 1)
        compact_names.append(name)
        scientific(name.label == label and name.provenance == provenance,
                   "BRANCH_PROVENANCE_" + label, fired)
        scientific(name.certified, "UNIFORM_NAME_CERTIFICATION_" + label, fired)
        audit_cut_contract(name, fired)
        scientific(name.entire_expression == ENTIRE_MARKER,
                   "FINITE_ENTIRE_MARKER_" + label, fired)
        scientific(name.uniform_error <= pow2_minus(2),
                   "UNIFORM_ERROR_BUDGET_" + label, fired)
        scientific(name.panels >= PANEL_START and name.panels & (name.panels - 1) == 0,
                   "PANEL_DOUBLING_" + label, fired)
        audit_midpoint_contract(name, fired)
        if name.panels > PANEL_START and name.previous_quadrature_error is not None:
            scientific(name.tail_error + name.previous_quadrature_error > pow2_minus(2),
                       "FIRST_ACCEPTED_REFINEMENT_" + label, fired)

    for constructor, label, unused_provenance in constructors:
        coarse_name = constructor(q(3, 2), q(3, 2), q(1, 2), q(1, 2), 2)
        fine_name = constructor(q(3, 2), q(3, 2), q(1, 2), q(1, 2), 3)
        scientific(coarse_name.certified, "COARSE_NAME_CERTIFICATION_" + label, fired)
        scientific(fine_name.certified, "FINE_NAME_CERTIFICATION_" + label, fired)
        audit_cut_contract(coarse_name, fired)
        audit_cut_contract(fine_name, fired)
        audit_midpoint_contract(coarse_name, fired)
        audit_midpoint_contract(fine_name, fired)
        if coarse_name.certified and fine_name.certified:
            coarse_ball, coarse_ok = evaluate_uniform_name(coarse_name, q(3, 2), q(1, 2), 2)
            fine_ball, fine_ok = evaluate_uniform_name(fine_name, q(3, 2), q(1, 2), 3)
            scientific(coarse_ok and coarse_ball.radius <= pow2_minus(2),
                       "COARSE_SAMPLE_BALL_" + label, fired)
            scientific(fine_ok and fine_ball.radius <= pow2_minus(3),
                       "FINE_SAMPLE_BALL_" + label, fired)
            scientific(coarse_ball.overlaps(fine_ball), "SAMPLE_BALL_OVERLAP_" + label, fired)

    require(len(compact_names) == 3, "COMPACT_NAME_COUNT")
    require(audit_control_mutations() == 12, "PROOF_CONTROL_COUNT")

    print("JIPC_WP3E_EFFECTIVE_MELLIN_SEEDS_AUDIT 1")
    if fired:
        print("SCIENTIFIC_FALSIFIER FIRED " + ",".join(fired))
        print("THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT")
        print("RESULT FIRED")
        return 0

    print("ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS")
    print("MACHIN_ATAN 3<P<16/5 BITS=16 PASS")
    print("SEED_TUPLES E,O,C PASS")
    print("BRANCH_PROVENANCE INDEPENDENT PASS")
    print("TAIL_BOUNDS LEFT_RIGHT CUTS PASS")
    print("MIDPOINT_REFINEMENT CELLWISE PASS")
    print("FINITE_APPROXIMANTS K=[1,3/2]x[-1/2,1/2] PASS")
    print("SAMPLE_BALLS S=3/2+i/2 BITS=2,3 PASS")
    print("PROOF_CONTROLS 12/12 PASS")
    print("THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT")
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
