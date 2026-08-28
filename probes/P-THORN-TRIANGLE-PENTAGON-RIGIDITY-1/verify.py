#!/usr/bin/env python3
"""Exact audit for P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1.

The written proof in PREREG.md carries the universal quantifier. This verifier
uses exact Laurent-polynomial, rational, Q(sqrt(5)), and Gaussian-rational
arithmetic only. Standard library only; no floating point or search.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

PROBE = "P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1"
DECISION = "THORN-TRIANGLE-PENTAGON-RIGIDITY-CONFIRMED"
PHI5 = (1, 1, 1, 1, 1)
T_REL = (-1, 1, 1)  # t^2+t-1
Q_N = (1, -3, 1)    # N^2-3N+1


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(number: int, label: str, condition: bool) -> None:
    require(condition, f"G{number:02d} {label}")
    print(f"G{number:02d} {label} PASS")


def trim(poly):
    out = [Fraction(value) for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left, right):
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += Fraction(value)
    for index, value in enumerate(right):
        out[index] += Fraction(value)
    return trim(out)


def scale(poly, scalar):
    return trim([Fraction(scalar) * Fraction(value) for value in poly])


def sub(left, right):
    return add(left, scale(right, -1))


def mul(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] += Fraction(left_value) * Fraction(right_value)
    return trim(out)


def power(poly, exponent):
    require(exponent >= 0, "negative polynomial exponent")
    result = (1,)
    factor = trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = mul(result, factor)
        factor = mul(factor, factor)
        remaining >>= 1
    return result


def divmod_poly(numerator, denominator):
    num = list(trim(numerator))
    den = trim(denominator)
    require(den != (0,), "zero polynomial denominator")
    if len(num) < len(den):
        return (0,), tuple(num)
    quotient = [Fraction(0)] * (len(num) - len(den) + 1)
    while len(num) >= len(den) and trim(num) != (0,):
        num = list(trim(num))
        shift = len(num) - len(den)
        factor = num[-1] / den[-1]
        quotient[shift] += factor
        for index, value in enumerate(den):
            num[index + shift] -= factor * value
    return trim(quotient), trim(num)


def mod_poly(poly, modulus):
    return divmod_poly(poly, modulus)[1]


def compose(poly, inner):
    result = (0,)
    inner_power = (1,)
    for coefficient in poly:
        result = add(result, scale(inner_power, coefficient))
        inner_power = mul(inner_power, inner)
    return trim(result)


def l_add(left, right):
    out = dict(left)
    for exponent, value in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + Fraction(value)
    return {exponent: value for exponent, value in out.items() if value}


def l_scale(poly, scalar):
    return {
        exponent: Fraction(scalar) * value
        for exponent, value in poly.items()
        if Fraction(scalar) * value
    }


def l_sub(left, right):
    return l_add(left, l_scale(right, -1))


def l_mul(left, right):
    out = {}
    for left_exp, left_value in left.items():
        for right_exp, right_value in right.items():
            exponent = left_exp + right_exp
            out[exponent] = out.get(exponent, Fraction(0)) + left_value * right_value
    return {exponent: value for exponent, value in out.items() if value}


def l_shift(poly, shift):
    return {exponent + shift: value for exponent, value in poly.items()}


class Q5:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Q5) else Q5(value)

    def __add__(self, other):
        value = Q5.coerce(other)
        return Q5(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q5.coerce(other))

    def __rsub__(self, other):
        return Q5.coerce(other) - self

    def __mul__(self, other):
        value = Q5.coerce(other)
        return Q5(
            self.a * value.a + 5 * self.b * value.b,
            self.a * value.b + self.b * value.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        value = Q5.coerce(other)
        return self.a == value.a and self.b == value.b

    def positive(self):
        if self.a >= 0 and self.b >= 0:
            return self.a != 0 or self.b != 0
        if self.a <= 0 and self.b <= 0:
            return False
        if self.b > 0:
            return 5 * self.b * self.b > self.a * self.a
        return self.a * self.a > 5 * self.b * self.b


class GQ:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, GQ) else GQ(value)

    def __add__(self, other):
        value = GQ.coerce(other)
        return GQ(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self):
        return GQ(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-GQ.coerce(other))

    def __rsub__(self, other):
        return GQ.coerce(other) - self

    def __mul__(self, other):
        value = GQ.coerce(other)
        return GQ(
            self.a * value.a - self.b * value.b,
            self.a * value.b + self.b * value.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        value = GQ.coerce(other)
        return self.a == value.a and self.b == value.b

    def conjugate(self):
        return GQ(self.a, -self.b)

    def norm(self):
        return self.a * self.a + self.b * self.b

    def __pow__(self, exponent):
        require(exponent >= 0, "negative Gaussian exponent")
        result = GQ(1)
        factor = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result * factor
            factor = factor * factor
            remaining >>= 1
        return result


def source_firewall() -> bool:
    path = Path(__file__)
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), "verifier lacks final LF")
    require(b"\r" not in raw, "verifier is not LF-only")
    tree = ast.parse(raw.decode("utf-8"))
    imports = set()
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            require(not isinstance(node.value, (float, complex)), "float or complex literal")
        elif isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.add(node.func.id)
    require(imports <= {"__future__", "ast", "fractions", "pathlib"}, "unexpected import")
    require(not ({"eval", "exec", "compile", "open"} & calls), "dynamic execution call")

    prereg = (path.parent / "PREREG.md").read_text(encoding="utf-8")
    required = (
        "Status: preregistered protocol only. Formal execution count: zero.",
        "P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1",
        "Status: ABANDONED.",
        "P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1",
        "THORN-TRIANGLE-PENTAGON-RIGIDITY",
        "S_z = 1 + N_z",
        "Phi_5(z)",
        "No physical mechanism",
        "Hurwitz",
        "ACTION_LAYER:   L1",
    )
    return all(item in prereg for item in required)


def closure_data(value):
    conjugate = value.conjugate()
    j_value = GQ(1) + value * value
    n_value = j_value * j_value.conjugate()
    s_value = (GQ(1) - value) * (GQ(1) - conjugate)
    phi5_value = sum((value ** exponent for exponent in range(5)), GQ(0))
    return n_value, s_value, s_value - (GQ(1) + n_value), phi5_value


def main() -> int:
    gate(1, "source_scope_firewall", source_firewall())

    one = {0: Fraction(1)}
    z = {1: Fraction(1)}
    zinv = {-1: Fraction(1)}
    t = l_add(z, zinv)
    n_value = l_mul(t, t)
    s_value = l_sub(l_scale(one, 2), t)
    closure_defect = l_sub(s_value, l_add(one, n_value))
    phi5_laurent = {exponent: Fraction(1) for exponent in range(5)}
    gate(
        2,
        "unit_circle_laurent_reduction",
        n_value == {-2: Fraction(1), 0: Fraction(2), 2: Fraction(1)}
        and s_value == {-1: Fraction(-1), 0: Fraction(2), 1: Fraction(-1)},
    )
    gate(
        3,
        "closure_equals_phi5",
        l_shift(closure_defect, 2) == l_scale(phi5_laurent, -1),
    )

    x5_minus_one = (-1, 0, 0, 0, 0, 1)
    quotient, remainder = divmod_poly(x5_minus_one, PHI5)
    exact_order = remainder == (0,) and quotient == (-1, 1)
    exact_order &= all(
        mod_poly(sub(power((0, 1), exponent), (1,)), PHI5) != (0,)
        for exponent in range(1, 5)
    )
    gate(4, "primitive_fifth_order", exact_order)

    t_poly = (0, 1)
    n_poly = power(t_poly, 2)
    s_poly = sub((2,), t_poly)
    gate(
        5,
        "scale_polynomial",
        mod_poly(compose(Q_N, n_poly), T_REL) == (0,),
    )

    inverse_identity = sub(mul(n_poly, sub((3,), n_poly)), (1,))
    quartic_chord = sub(power(s_poly, 2), scale(n_poly, 5))
    weak_triangle = sub(add(s_poly, sub((3,), n_poly)), (4,))
    gate(
        6,
        "thorn_inverse_and_quartic",
        mod_poly(inverse_identity, T_REL) == (0,)
        and mod_poly(quartic_chord, T_REL) == (0,)
        and mod_poly(weak_triangle, T_REL) == (0,)
        and Q_N[1] * Q_N[1] - 4 * Q_N[0] * Q_N[2] == 5,
    )

    n_contract = Q5(Fraction(3, 2), Fraction(-1, 2))
    n_expand = Q5(Fraction(3, 2), Fraction(1, 2))
    s_contract = Q5(Fraction(5, 2), Fraction(-1, 2))
    s_expand = Q5(Fraction(5, 2), Fraction(1, 2))
    gate(
        7,
        "quadratic_branch_values",
        n_contract * n_contract - 3 * n_contract + 1 == Q5(0)
        and n_expand * n_expand - 3 * n_expand + 1 == Q5(0)
        and s_contract == 1 + n_contract
        and s_expand == 1 + n_expand
        and s_contract * s_contract == 5 * n_contract
        and s_expand * s_expand == 5 * n_expand
        and n_contract * n_expand == 1,
    )

    trace_contract = Q5(Fraction(-1, 2), Fraction(1, 2))
    trace_expand = Q5(Fraction(-1, 2), Fraction(-1, 2))
    gate(
        8,
        "contracting_expanding_census",
        trace_contract * trace_contract == n_contract
        and trace_expand * trace_expand == n_expand
        and n_contract.positive()
        and (1 - n_contract).positive()
        and n_expand.positive()
        and (n_expand - 1).positive(),
    )

    t3 = Fraction(-1)
    n3 = t3 * t3
    s3 = 2 - t3
    gate(
        9,
        "weaker_triangle_third_root_control",
        s3 + Fraction(1, n3) == 4 and s3 != 1 + n3 and n3 == 1 and s3 == 3,
    )

    zi = GQ(0, 1)
    zminus = GQ(-1)
    zr = GQ(Fraction(3, 5), Fraction(4, 5))
    ni, si, di, pi5i = closure_data(zi)
    _nm, _sm, dm, pi5m = closure_data(zminus)
    _nr, _sr, dr, pi5r = closure_data(zr)
    gate(
        10,
        "gaussian_rational_controls",
        zi.norm() == 1
        and ni == 0
        and si == 2
        and di != 0
        and pi5i != 0
        and zminus.norm() == 1
        and dm != 0
        and pi5m != 0
        and zr.norm() == 1
        and dr == GQ(Fraction(-41, 25))
        and pi5r != 0,
    )

    phi = Q5(Fraction(1, 2), Fraction(1, 2))
    principal_n = Q5(2) - phi
    principal_s = Q5(3) - phi
    gate(
        11,
        "principal_golden_chord_square",
        principal_n == n_contract
        and principal_s == s_contract
        and principal_s * principal_s == 5 * principal_n,
    )

    gate(
        12,
        "scope_and_nonselection_guard",
        Q_N == (1, -3, 1)
        and PHI5 == (1, 1, 1, 1, 1)
        and PROBE in (Path(__file__).parent / "PREREG.md").read_text(encoding="utf-8"),
    )

    print("DECISION " + DECISION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
