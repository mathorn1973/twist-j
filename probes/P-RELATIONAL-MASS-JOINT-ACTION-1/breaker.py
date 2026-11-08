#!/usr/bin/env python3
"""Independent exact Picard audit of the preregistered joint action.

The field uses one reduced integer triple (a, b, d), denoting
(a + b*phi)/d.  Formal roots are solved by their square coefficients;
formal reciprocals use the product recurrence.  Neither companion source
nor predecessor scientific code is read or imported.
"""

from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import sys


ORDER = 4


class GateFailure(Exception):
    """An explicitly tested, deterministic scientific gate failure."""


def require(condition, code):
    if not condition:
        raise GateFailure(code)


class F:
    """Immutable-by-convention normalized integer-triple Q(phi)."""

    __slots__ = ("a", "b", "d")

    def __init__(self, a=0, b=0, d=1):
        if not d:
            raise ZeroDivisionError("zero field denominator")
        if d < 0:
            a, b, d = -a, -b, -d
        common = gcd(gcd(abs(a), abs(b)), d)
        self.a, self.b, self.d = a // common, b // common, d // common

    @staticmethod
    def lift(other):
        if isinstance(other, F):
            return other
        if isinstance(other, int):
            return F(other)
        return NotImplemented

    def __bool__(self):
        return bool(self.a or self.b)

    def __eq__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return (self.a, self.b, self.d) == (other.a, other.b, other.d)

    def __neg__(self):
        return F(-self.a, -self.b, self.d)

    def __add__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        if not self:
            return other
        if not other:
            return self
        common = gcd(self.d, other.d)
        left, right = other.d // common, self.d // common
        return F(self.a * left + other.a * right,
                 self.b * left + other.b * right, self.d * left)

    __radd__ = __add__

    def __sub__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return self + (-other)

    def __rsub__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return other + (-self)

    def __mul__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        if not self or not other:
            return F()
        return F(self.a * other.a + self.b * other.b,
                 self.a * other.b + self.b * other.a + self.b * other.b,
                 self.d * other.d)

    __rmul__ = __mul__

    def reciprocal(self):
        norm = self.a * self.a + self.a * self.b - self.b * self.b
        if not norm:
            raise ZeroDivisionError("zero field element")
        return F(self.d * (self.a + self.b), -self.d * self.b, norm)

    def __truediv__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return self * other.reciprocal()

    def __rtruediv__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return other * self.reciprocal()

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            return NotImplemented
        result, base = F(1), self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def sign(self):
        # 2d*self = (2a+b) + b*sqrt(5); compare integer squares only.
        c, b = 2 * self.a + self.b, self.b
        if not b:
            return (c > 0) - (c < 0)
        if not c:
            return (b > 0) - (b < 0)
        if (c > 0) == (b > 0):
            return 1 if c > 0 else -1
        difference = c * c - 5 * b * b
        return ((c > 0) - (c < 0)) * ((difference > 0) - (difference < 0))

    def encode(self):
        def rational(n, d):
            divisor = gcd(abs(n), d)
            n, d = n // divisor, d // divisor
            return str(n) if d == 1 else str(n) + "/" + str(d)
        return rational(self.a, self.d) + "," + rational(self.b, self.d)


ZERO, ONE = F(), F(1)


class P:
    """Degree-four truncated formal series with exact field coefficients."""

    __slots__ = ("c",)

    def __init__(self, coefficients):
        self.c = tuple(coefficients)

    @staticmethod
    def constant(value):
        value = F.lift(value)
        if value is NotImplemented:
            raise TypeError("series constant is not in Q(phi)")
        return P((value,) + (ZERO,) * ORDER)

    @staticmethod
    def lift(other):
        if isinstance(other, P):
            return other
        if isinstance(other, (F, int)):
            return P.constant(other)
        return NotImplemented

    def __eq__(self, other):
        other = P.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return self.c == other.c

    def __neg__(self):
        return P(tuple(-value for value in self.c))

    def __add__(self, other):
        other = P.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return P(tuple(x + y for x, y in zip(self.c, other.c)))

    __radd__ = __add__

    def __sub__(self, other):
        other = P.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return P(tuple(x - y for x, y in zip(self.c, other.c)))

    def __rsub__(self, other):
        other = P.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return other - self

    def __mul__(self, other):
        if isinstance(other, (F, int)):
            return P(tuple(value * other for value in self.c))
        if not isinstance(other, P):
            return NotImplemented
        result = [ZERO] * (ORDER + 1)
        for i, a in enumerate(self.c):
            if a:
                for j in range(ORDER + 1 - i):
                    b = other.c[j]
                    if b:
                        result[i + j] = result[i + j] + a * b
        return P(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = F.lift(other)
        if other is NotImplemented:
            return NotImplemented
        return self * other.reciprocal()

    def reciprocal(self, code):
        require(bool(self.c[0]), code)
        result = [self.c[0].reciprocal()]
        for m in range(1, ORDER + 1):
            total = sum((self.c[j] * result[m - j]
                         for j in range(1, m + 1)), ZERO)
            result.append(-result[0] * total)
        answer = P(result)
        require(self * answer == 1, code)
        return answer

    def root(self, root0, code):
        require(root0.sign() > 0 and root0 * root0 == self.c[0], code)
        result = [root0]
        for m in range(1, ORDER + 1):
            cross = sum((result[j] * result[m - j]
                         for j in range(1, m)), ZERO)
            result.append((self.c[m] - cross) / (2 * root0))
        answer = P(result)
        require(answer * answer == self, code)
        return answer

    def derivative(self):
        return P(tuple(self.c[m + 1] * (m + 1) for m in range(ORDER))
                 + (ZERO,))

    def integral(self):
        return P((ZERO,) + tuple(self.c[m - 1] / m
                                for m in range(1, ORDER + 1)))

    def shift(self):
        return P((ZERO,) + self.c[:ORDER])


PZERO = P.constant(ZERO)
MZERO = (PZERO,) * 4
VZERO = (PZERO,) * 2
POSITIONS_ZERO = (VZERO,) * 5


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, scalar):
    return tuple(value * scalar for value in a)


def transpose(a):
    return a[0], a[2], a[1], a[3]


def multiply(a, b):
    return (a[0] * b[0] + a[1] * b[2],
            a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2],
            a[2] * b[1] + a[3] * b[3])


def mv(a, v):
    return a[0] * v[0] + a[1] * v[1], a[2] * v[0] + a[3] * v[1]


def outer(v, w):
    return v[0] * w[0], v[0] * w[1], v[1] * w[0], v[1] * w[1]


def trace(a):
    return a[0] + a[3]


def determinant(a):
    return a[0] * a[3] - a[1] * a[2]


def inverse(a, code):
    d = determinant(a)
    require(bool(d), code)
    answer = scale((a[3], -a[1], -a[2], a[0]), d.reciprocal())
    require(multiply(a, answer) == (ONE, ZERO, ZERO, ONE), code)
    return answer


def quadratic(g, v):
    w = mv(g, v)
    return v[0] * w[0] + v[1] * w[1]


def constant(values):
    return tuple(P.constant(value) for value in values)


def values_at(entries, degree):
    return tuple(value.c[degree] for value in entries)


def initials(entries):
    return constant(values_at(entries, 0))


def positive_metric(g, code):
    require(g[1] == g[2] and g[0].sign() > 0 and determinant(g).sign() > 0,
            code)


def same_through(a, b, degree):
    return all(x.c[:degree + 1] == y.c[:degree + 1] for x, y in zip(a, b))


def stationary(series):
    return all(not value for value in series.c[1:])


def momentum(counts, covectors):
    result = (ZERO, ZERO)
    for n, p in zip(counts, covectors):
        result = add(result, scale(p, n))
    return result


def matter(g, counts, covectors, root0, code):
    energy, tensor = PZERO, MZERO
    lengths, reciprocals = [], []
    for n, p in zip(counts, covectors):
        if n:
            length = quadratic(g, p).root(root0, code)
            reciprocal = length.reciprocal(code)
            energy = energy + n * length
            tensor = add(tensor, scale(outer(p, p), n * reciprocal))
            lengths.append(length)
            reciprocals.append(reciprocal)
        else:
            lengths.append(None)
            reciprocals.append(None)
    return energy, tensor, tuple(lengths), tuple(reciprocals)


def invariants(state, counts, covectors, root0=ONE, code="F04_EXCHANGE"):
    g, pi, positions = state
    energy, tensor, lengths, reciprocals = matter(g, counts, covectors, root0, code)
    gp = multiply(g, pi)
    kinetic = trace(multiply(gp, gp)) / 2
    dilation = trace(gp)
    charge = scale(gp, 2)
    for n, x, p in zip(counts, positions, covectors):
        if n:
            charge = add(charge, scale(outer(x, p), n))
    total_p = momentum(counts, covectors)
    mass = energy * energy - quadratic(g, total_p)
    return {"K": kinetic, "E": energy, "D": mass, "C": dilation,
            "J": charge, "P": total_p, "T": tensor,
            "lengths": lengths, "reciprocals": reciprocals}


def flow_rhs(state, counts, covectors, code):
    g, pi, positions = state
    _, tensor, _, reciprocals = matter(g, counts, covectors, ONE, code)
    dg = multiply(multiply(g, pi), g)
    dpi = sub(scale(multiply(multiply(pi, g), pi), -1), scale(tensor, F(1, 0, 2)))
    dx = tuple(scale(mv(g, p), r) if n else VZERO
               for n, p, r in zip(counts, covectors, reciprocals))
    return dg, dpi, dx


def dg_rhs(old, new, counts, covectors, old_root, new_root, code):
    go, po, xo = old
    gn, pn, xn = new
    summed_g, summed_pi = add(go, gn), add(po, pn)
    a = scale(add(multiply(multiply(po, summed_g), po),
                  multiply(multiply(pn, summed_g), pn)), F(1, 0, 4))
    b = scale(add(multiply(multiply(go, summed_pi), go),
                  multiply(multiply(gn, summed_pi), gn)), F(1, 0, 4))
    _, _, old_lengths, _ = matter(go, counts, covectors, old_root, code)
    _, _, new_lengths, _ = matter(gn, counts, covectors, new_root, code)
    q, dx = MZERO, []
    for n, p, lo, ln in zip(counts, covectors, old_lengths, new_lengths):
        if n:
            denominator = lo + ln
            reciprocal = denominator.reciprocal(code)
            q = add(q, scale(outer(p, p), n * reciprocal))
            dx.append(scale(mv(summed_g, p), reciprocal))
        else:
            dx.append(VZERO)
    return (b, scale(add(a, q), -1), tuple(dx)), (a, b, q)


def integrate_state(initial, derivative, discrete):
    operation = P.shift if discrete else P.integral
    g0, p0, x0 = initial
    dg, dp, dx = derivative
    g = add(g0, tuple(operation(value) for value in dg))
    p = add(p0, tuple(operation(value) for value in dp))
    x = tuple(add(old, tuple(operation(value) for value in velocity))
              for old, velocity in zip(x0, dx))
    return g, p, x


def picard_flow(initial, counts, covectors):
    state = initial
    for _ in range(ORDER):
        state = integrate_state(initial, flow_rhs(state, counts, covectors,
                                                  "F03_FLOW"), False)
    return state


def picard_dg(initial, counts, covectors):
    state = initial
    for _ in range(ORDER):
        rhs, _ = dg_rhs(initial, state, counts, covectors, ONE, ONE, "F05_DG")
        state = integrate_state(initial, rhs, True)
    return state


def initial_state(state):
    g, pi, x = state
    return initials(g), initials(pi), tuple(initials(v) for v in x)


def audit_basic(state, initial, counts, code):
    g, pi, positions = state
    require(g[1] == g[2] and pi[1] == pi[2], code)
    require(initial_state(state) == initial, code)
    require(all(n or x == VZERO for n, x in zip(counts, positions)), code)


def audit_flow(state, initial, counts, covectors, code="F03_FLOW"):
    audit_basic(state, initial, counts, code)
    computed = invariants(state, counts, covectors, code=code)
    rhs = flow_rhs(state, counts, covectors, code)
    g, pi, positions = state
    require(same_through(tuple(v.derivative() for v in g), rhs[0], ORDER - 1), code)
    require(same_through(tuple(v.derivative() for v in pi), rhs[1], ORDER - 1), code)
    for n, x, velocity in zip(counts, positions, rhs[2]):
        if n:
            require(same_through(tuple(v.derivative() for v in x), velocity,
                                 ORDER - 1), code)
    exchange_code = "F04_EXCHANGE" if code == "F03_FLOW" else code
    require(stationary(computed["K"] + computed["E"]), exchange_code)
    require(all(stationary(entry) for entry in computed["J"]),
            "F06_CHARGE" if code == "F03_FLOW" else code)
    dg = tuple(v.derivative() for v in g)
    exchange = trace(multiply(computed["T"], dg)) / 2
    require(same_through((computed["E"].derivative(),), (exchange,), ORDER - 1),
            exchange_code)
    require(same_through((computed["K"].derivative(),), (-exchange,), ORDER - 1),
            exchange_code)
    require(same_through((computed["C"].derivative(),), (-computed["E"] / 2,),
                         ORDER - 1), exchange_code)
    return computed


def formal_defect(initial, state):
    g0, pi0, _ = initial
    g, pi, _ = state
    middle_g, middle_pi = scale(add(g, g0), F(1, 0, 2)), scale(add(pi, pi0), F(1, 0, 2))
    d, e = sub(g, g0), sub(pi, pi0)
    dn, me = multiply(d, middle_pi), multiply(middle_g, e)
    return tuple((entry / 2).shift()
                 for entry in sub(multiply(dn, dn), multiply(me, me)))


def audit_dg(state, initial, counts, covectors, code="F05_DG"):
    audit_basic(state, initial, counts, code)
    rhs, (_, b, q) = dg_rhs(initial, state, counts, covectors, ONE, ONE, code)
    require(state == integrate_state(initial, rhs, True), code)
    computed = invariants(state, counts, covectors, code=code)
    old = invariants(initial, counts, covectors, code=code)
    require(stationary(computed["K"] + computed["E"]), code)
    exchange = trace(multiply(b, q)).shift()
    require(computed["E"] - old["E"] == exchange, code)
    require(computed["K"] - old["K"] == -exchange, code)
    charge_code = "F06_CHARGE" if code == "F05_DG" else code
    actual = sub(computed["J"], old["J"])
    require(actual == formal_defect(initial, state), charge_code)
    if all(entry == 0 for entry in initial[1]):
        gt = multiply(initial[0], old["T"])
        cubic = scale(multiply(gt, gt), F(-1, 0, 8))
        require(values_at(actual, 3) == values_at(cubic, 0), charge_code)
    return computed


def directional_kinetic(g, pi, direction_g, direction_pi):
    parameter = P((ZERO, ONE, ZERO, ZERO, ZERO))
    perturbed_g = add(constant(g), scale(direction_g, parameter))
    perturbed_pi = add(constant(pi), scale(direction_pi, parameter))
    gp = multiply(perturbed_g, perturbed_pi)
    return (trace(multiply(gp, gp)) / 2).c[1]


def audit_variations(g, pi, counts, covectors):
    zero_matrix = (ZERO,) * 4
    directions = ((ONE, ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO, ONE),
                  (ZERO, ONE, ONE, ZERO))
    tensor = matter(constant(g), counts, covectors, ONE, "F04_EXCHANGE")[1]
    tensor0 = values_at(tensor, 0)
    parameter = P((ZERO, ONE, ZERO, ZERO, ZERO))
    for s in directions:
        actual_g = directional_kinetic(g, pi, s, zero_matrix)
        actual_pi = directional_kinetic(g, pi, zero_matrix, s)
        expected_g = trace(multiply(multiply(multiply(pi, g), pi), s))
        expected_pi = trace(multiply(multiply(multiply(g, pi), g), s))
        require(actual_g == expected_g and actual_pi == expected_pi, "F04_EXCHANGE")
        perturbed = add(constant(g), scale(s, parameter))
        actual_e = matter(perturbed, counts, covectors, ONE, "F04_EXCHANGE")[0].c[1]
        require(actual_e == trace(multiply(tensor0, s)) / 2, "F04_EXCHANGE")


def encode(entries):
    return ",".join(value.encode() for value in entries)


def fields(state, computed, degree):
    g, pi, positions = state
    flat_positions = tuple(value for position in positions for value in position)
    arrays = (g, pi, flat_positions, (computed["K"],), (computed["E"],),
              (computed["D"],), (computed["C"],), computed["J"])
    require(tuple(len(values) * 2 for values in arrays) == (8, 8, 20, 2, 2, 2, 2, 8),
            "F10_PAYLOAD")
    return "|".join(encode(values_at(values, degree)) for values in arrays)


def transform(state, a, ai):
    g, pi, positions = state
    return (multiply(multiply(a, g), transpose(a)),
            multiply(multiply(transpose(ai), pi), ai),
            tuple(mv(a, x) for x in positions))


def finite_witness(g0, ginv, covectors):
    code = "F08_WITNESS"
    counts = (1,) * 5
    h = F(1100, 0, 1921)
    old_g = scale(g0, F(36, 0, 25))
    new_pi = scale(ginv, -1)
    old = constant(old_g), MZERO, POSITIONS_ZERO
    new_x = tuple(constant(scale(mv(g0, p), F(1220, 0, 1921))) for p in covectors)
    new = constant(g0), constant(new_pi), new_x
    positive_metric(old_g, code)
    positive_metric(g0, code)
    require(h.sign() > 0, code)
    for p in covectors:
        require(quadratic(old_g, p) == F(6, 0, 5) ** 2, code)
        require(quadratic(g0, p) == ONE, code)
    first = invariants(old, counts, covectors, F(6, 0, 5), code)
    last = invariants(new, counts, covectors, ONE, code)
    rhs, (a, b, q) = dg_rhs(old, new, counts, covectors, F(6, 0, 5), ONE, code)
    require(sub(new[0], old[0]) == scale(rhs[0], h), code)
    require(sub(new[1], old[1]) == scale(rhs[1], h), code)
    require(all(sub(xn, xo) == scale(v, h)
                for xn, xo, v in zip(new[2], old[2], rhs[2])), code)
    require(a == constant(scale(ginv, F(61, 0, 100))), code)
    require(b == constant(scale(g0, F(-1921, 0, 2500))), code)
    require(q == constant(scale(ginv, F(25, 0, 22))), code)
    require(add(a, q) == constant(scale(ginv, F(1921, 0, 1100))), code)
    require(first["K"] == 0 and last["K"] == 1, code)
    require(first["E"] == 6 and last["E"] == 5, code)
    require(first["K"] + first["E"] == 6 and last["K"] + last["E"] == 6, code)
    require(first["P"] == (ZERO, ZERO) == last["P"], code)
    require(first["D"] == 36 and last["D"] == 25, code)
    require(first["C"] == 0 and last["C"] == -2, code)
    expected_charge = constant((F(-792, 0, 1921), ZERO, ZERO, F(-792, 0, 1921)))
    require(first["J"] == MZERO and last["J"] == expected_charge, code)
    d, e = sub(new[0], old[0]), sub(new[1], old[1])
    mid_g, mid_pi = scale(add(new[0], old[0]), F(1, 0, 2)), scale(add(new[1], old[1]), F(1, 0, 2))
    dn, me = multiply(d, mid_pi), multiply(mid_g, e)
    actual_defect = sub(last["J"], first["J"])
    require(actual_defect == scale(sub(multiply(dn, dn), multiply(me, me)), h / 2), code)
    require(last["K"] - first["K"] == trace(multiply(a, d)) + trace(multiply(b, e)), code)
    transfer = h * trace(multiply(b, q))
    require(last["E"] - first["E"] == transfer, code)
    require(last["K"] - first["K"] == -transfer, code)

    # Differentiate the declared scalar endpoint equations at the witness.
    x, y, xx, yy = F(36, 0, 25), ZERO, ONE, F(-1)
    sx, sxx = F(6, 0, 5), ONE
    require(sx.sign() > 0 and sxx.sign() > 0 and sx * sx == x and sxx * sxx == xx, code)
    require(xx - x - h * (x * x + xx * xx) * (y + yy) / 4 == 0, code)
    require(yy - y + h * (y * y + yy * yy) * (x + xx) / 4
            + 5 * h / (2 * (sx + sxx)) == 0, code)
    f1_X = 1 - h * xx * (y + yy) / 2
    f1_Y = -h * (x * x + xx * xx) / 4
    f2_X = h * (y * y + yy * yy) / 4 - 5 * h / (4 * sxx * (sx + sxx) ** 2)
    f2_Y = 1 + h * yy * (x + xx) / 2
    f1_x = -1 - h * x * (y + yy) / 2
    f1_y = f1_Y
    f2_x = h * (y * y + yy * yy) / 4 - 5 * h / (4 * sx * (sx + sxx) ** 2)
    f2_y = -1 + h * y * (x + xx) / 2
    output_det = determinant((f1_X, f1_Y, f2_X, f2_Y))
    input_det = determinant((f1_x, f1_y, f2_x, f2_y))
    require(output_det.sign() > 0 and input_det.sign() > 0, code)
    ratio = input_det / output_det
    require(output_det == F(1423025, 0, 1921 ** 2), code)
    require(input_det == F(6875, 0, 6 * 1921), code)
    require(ratio == F(528275, 0, 341526) and ratio != ONE, code)
    return old, new, first, last, actual_defect, output_det, input_det, ratio


def negative_controls(g0, ginv, covectors, witness):
    detected = []
    code = "F09_NEGATIVE_CONTROL"

    single = (1, 0, 0, 0, 0)
    base = constant(g0), MZERO, POSITIONS_ZERO
    one = invariants(base, single, covectors, code=code)
    wrong_source = sub(scale(one["T"], one["E"]), constant(outer(one["P"], one["P"])))
    correct_source = scale(one["T"], F(1, 0, 2))
    require(wrong_source == MZERO and correct_source != scale(wrong_source, F(1, 0, 2)), code)
    detected.append("NC01")

    zero_matrix = (ZERO,) * 4
    dg = multiply(multiply(g0, ginv), g0)
    wrong_dpi = zero_matrix
    wrong_hdot = directional_kinetic(g0, ginv, dg, wrong_dpi)
    correct_dpi = scale(multiply(multiply(ginv, g0), ginv), -1)
    correct_hdot = directional_kinetic(g0, ginv, dg, correct_dpi)
    require(bool(wrong_hdot) and not correct_hdot, code)
    detected.append("NC02")

    double = (2, 0, 0, 0, 0)
    # Differentiate the actual matter norm with respect to each component
    # of the occupied covector; the unweighted pairing omits division by n.
    parameter = P((ZERO, ONE, ZERO, ZERO, ZERO))
    gradient = []
    for component in range(2):
        pp = tuple(P.constant(covectors[0][j]) + (parameter if j == component else PZERO)
                   for j in range(2))
        energy = double[0] * quadratic(constant(g0), pp).root(ONE, code)
        gradient.append(energy.c[1])
    wrong_velocity = tuple(gradient)
    right_velocity = values_at(flow_rhs(base, double, covectors, code)[2][0], 0)
    require(wrong_velocity == scale(right_velocity, 2) and wrong_velocity != right_velocity, code)
    detected.append("NC03")

    offdiag = (ZERO, ONE, ONE, ZERO)
    true_derivative = directional_kinetic(g0, offdiag, offdiag, zero_matrix)
    gradient_g = multiply(multiply(offdiag, g0), offdiag)
    half_derivative = gradient_g[1]
    gamma = F(-1, 1)
    require(true_derivative == gamma and half_derivative == gamma / 2
            and true_derivative != half_derivative, code)
    detected.append("NC04")

    _, _, old, new, defect, _, _, ratio = witness
    require(new["E"] != old["E"], code)
    detected.append("NC05")
    require(defect == sub(new["J"], old["J"]) and defect != MZERO, code)
    detected.append("NC06")
    require(ratio != ONE, code)
    detected.append("NC07")
    energy = old["K"] + old["E"]
    clock_momentum = P.constant(F(-6))
    require(energy == 6 and energy != 0 and clock_momentum + energy == 0, code)
    detected.append("NC08")
    return detected


def authority():
    records = (
        ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
        ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
        ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
        ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
        ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
    )
    root = Path(__file__).resolve().parents[2]
    checked = 0
    for name, size, digest in records:
        try:
            data = (root / name).read_bytes()
        except OSError as error:
            raise GateFailure("F01_AUTHORITY") from error
        require(len(data) == size and sha256(data).hexdigest() == digest, "F01_AUTHORITY")
        checked += 1
    return checked


def certificate():
    authority_count = authority()
    phi, gamma = F(0, 1), F(-1, 1)
    require(phi * phi == phi + 1 and phi.sign() > 0 and (phi - 1).sign() > 0,
            "F02_GEOMETRY")
    g0 = (ONE, gamma / 2, gamma / 2, ONE)
    covectors = ((ONE, ZERO), (ZERO, ONE), (F(-1), gamma),
                 (-gamma, -gamma), (gamma, F(-1)))
    positive_metric(g0, "F02_GEOMETRY")
    ginv = inverse(g0, "F02_GEOMETRY")
    require(all(quadratic(g0, p) == ONE for p in covectors), "F02_GEOMETRY")
    require(momentum((1,) * 5, covectors) == (ZERO, ZERO), "F02_GEOMETRY")
    second = (ZERO,) * 4
    for p in covectors:
        second = add(second, outer(p, p))
    require(second == scale(ginv, F(5, 0, 2)), "F02_GEOMETRY")
    momenta = ((ZERO,) * 4, ginv, scale(ginv, -1),
               (ONE, ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO, ONE),
               (ZERO, ONE, ONE, ZERO), (ZERO, F(-1), F(-1), ZERO))
    counts_box = tuple(product(range(2), repeat=5))
    require(len(counts_box) == 32 and len(momenta) == 7, "F10_PAYLOAD")
    payload = ["G|" + encode(g0) + "|" + encode(tuple(v for p in covectors for v in p))]
    for index, pi in enumerate(momenta):
        payload.append("B|" + str(index) + "|" + encode(pi))
    trajectory_count, flow_rows, dg_rows = 0, 0, 0
    bases = {}
    base_keys = (((1, 0, 1, 0, 0), 5), ((1, 1, 1, 1, 1), 0))
    for counts in counts_box:
        ntext = "".join(str(n) for n in counts)
        total_p = momentum(counts, covectors)
        acount = sum(counts[k] * counts[(k + 1) % 5] for k in range(5))
        bcount = sum(counts[k] * counts[(k + 2) % 5] for k in range(5))
        for index, pi in enumerate(momenta):
            initial = constant(g0), constant(pi), POSITIONS_ZERO
            audit_variations(g0, pi, counts, covectors)
            flow = picard_flow(initial, counts, covectors)
            dg = picard_dg(initial, counts, covectors)
            flow_i = audit_flow(flow, initial, counts, covectors)
            dg_i = audit_dg(dg, initial, counts, covectors)
            require(same_through(flow[0], dg[0], 2) and same_through(flow[1], dg[1], 2)
                    and all(same_through(x, y, 2) for x, y in zip(flow[2], dg[2])), "F05_DG")
            expected_d0 = (3 - phi) * acount + (2 + phi) * bcount
            require(flow_i["D"].c[0] == expected_d0 == dg_i["D"].c[0], "F02_GEOMETRY")
            payload.append("C|" + ntext + "|" + str(index) + "|" + str(sum(counts))
                           + "|" + encode(total_p) + "|" + flow_i["D"].c[0].encode())
            for method, state, computed in (("FLOW", flow, flow_i), ("DG", dg, dg_i)):
                for degree in range(ORDER + 1):
                    payload.append("S|" + ntext + "|" + str(index) + "|" + method
                                   + "|" + str(degree) + "|" + fields(state, computed, degree))
                    if method == "FLOW":
                        flow_rows += 1
                    else:
                        dg_rows += 1
            trajectory_count += 1
            if (counts, index) in base_keys:
                bases[(counts, index)] = ((flow, flow_i), (dg, dg_i))

    changes = ((ONE, ONE, ZERO, ONE), (ZERO, ONE, ONE, ZERO),
               (F(2), ZERO, ZERO, ONE))
    covariance_count, covariance_rows = 0, 0
    covariance_methods = set()
    for counts, index in base_keys:
        ntext = "".join(str(n) for n in counts)
        for a in changes:
            ai = inverse(a, "F07_COVARIANCE")
            transformed_p = tuple(mv(transpose(ai), p) for p in covectors)
            payload.append("A|" + str(covariance_count) + "|" + ntext + "|" + str(index)
                           + "|" + encode(a) + "|" + encode(tuple(v for p in transformed_p for v in p)))
            for method, (source, source_i) in zip(("FLOW", "DG"), bases[(counts, index)]):
                state = transform(source, a, ai)
                initial = initial_state(state)
                positive_metric(values_at(state[0], 0), "F07_COVARIANCE")
                require(all(quadratic(values_at(state[0], 0), p) == ONE
                            for p in transformed_p), "F07_COVARIANCE")
                audit = audit_flow if method == "FLOW" else audit_dg
                computed = audit(state, initial, counts, transformed_p, "F07_COVARIANCE")
                require(all(computed[key] == source_i[key] for key in ("K", "E", "D", "C")),
                        "F07_COVARIANCE")
                require(computed["J"] == multiply(multiply(a, source_i["J"]), ai),
                        "F07_COVARIANCE")
                require(computed["P"] == mv(transpose(ai), source_i["P"]), "F07_COVARIANCE")
                for degree in range(ORDER + 1):
                    payload.append("Y|" + str(covariance_count) + "|" + method + "|" + str(degree)
                                   + "|" + fields(state, computed, degree))
                    covariance_rows += 1
                covariance_methods.add(method)
            covariance_count += 1

    witness = finite_witness(g0, ginv, covectors)
    old, new, old_i, new_i, defect, output_det, input_det, ratio = witness
    finite_count = 0
    payload.append("W|1100/1921")
    for endpoint, (state, computed) in enumerate(((old, old_i), (new, new_i))):
        payload.append("F|" + str(endpoint) + "|" + fields(state, computed, 0))
    payload.append("R|DG_J_DEFECT|" + encode(values_at(defect, 0)) + "|" + output_det.encode()
                   + "|" + input_det.encode() + "|" + ratio.encode())
    finite_count += 1
    controls = negative_controls(g0, ginv, covectors, witness)
    for control in controls:
        payload.append("N|" + control + "|DETECTED")

    require(authority_count == 5 and trajectory_count == len(counts_box) * len(momenta) == 224,
            "F10_PAYLOAD")
    require(flow_rows == dg_rows == trajectory_count * (ORDER + 1) == 1120, "F10_PAYLOAD")
    require(covariance_count == len(base_keys) * len(changes) == 6
            and len(covariance_methods) == 2 and covariance_rows == 60, "F10_PAYLOAD")
    require(finite_count == 1 and controls == ["NC" + str(i).zfill(2) for i in range(1, 9)],
            "F10_PAYLOAD")
    expected_records = (1 + len(momenta) + trajectory_count * (1 + 2 * (ORDER + 1))
                        + covariance_count * (1 + len(covariance_methods) * (ORDER + 1))
                        + finite_count * 4 + len(controls))
    require(len(payload) == expected_records == 2550, "F10_PAYLOAD")
    require(all("\n" not in record and "\r" not in record and record.isascii()
                for record in payload), "F10_PAYLOAD")
    payload_bytes = ("\n".join(payload) + "\n").encode("ascii")
    lines = (
        "CERTIFICATE=P-RELATIONAL-MASS-JOINT-ACTION-1",
        "AUTHORITY_FILES=" + str(authority_count),
        "COUNT_PREPARATIONS=" + str(len(counts_box)),
        "MOMENTUM_CASES=" + str(len(momenta)),
        "TRAJECTORY_CASES=" + str(trajectory_count),
        "FORMAL_ORDER=" + str(ORDER),
        "FLOW_COEFFICIENTS=" + str(flow_rows),
        "DG_COEFFICIENTS=" + str(dg_rows),
        "COVARIANCE_CASES=" + str(covariance_count),
        "COVARIANCE_METHODS=" + str(len(covariance_methods)),
        "FINITE_EXCHANGE_CASES=" + str(finite_count),
        "NEGATIVE_CONTROLS=" + str(len(controls)),
        "PAYLOAD_RECORDS=" + str(len(payload)),
        "PAYLOAD_SHA256=" + sha256(payload_bytes).hexdigest(),
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 15, "F10_PAYLOAD")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        result = certificate()
    except GateFailure as failure:
        result = ("FALSIFIER=" + str(failure) + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(result)


if __name__ == "__main__":
    main()
