#!/usr/bin/env python3
"""Exact audit for P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1.

The written proof in PREREG.md carries the theorem. This verifier uses exact
polynomial arithmetic in Q(zeta_20) and exact Q(sqrt(3)) arithmetic only.
Standard library only; no floating point, numerical roots, or search.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

PROBE = "P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1"
DECISION = "THORN-PLENUM-QUADRANT-CHARACTERIZATION-CONFIRMED"

# Ascending coefficient order.
PHI3 = (1, 1, 1)
PHI5 = (1, 1, 1, 1, 1)
PHI20 = (1, 0, -1, 0, 1, 0, -1, 0, 1)


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


def divmod_poly(numerator, denominator):
    num = list(trim(numerator))
    den = trim(denominator)
    require(den != (0,), "zero polynomial denominator")
    if len(num) < len(den):
        return (0,), tuple(num)

    quotient = [Fraction(0)] * (len(num) - len(den) + 1)
    while len(trim(num)) >= len(den) and trim(num) != (0,):
        num = list(trim(num))
        shift = len(num) - len(den)
        factor = num[-1] / den[-1]
        quotient[shift] += factor
        for index, value in enumerate(den):
            num[index + shift] -= factor * value
    return trim(quotient), trim(num)


def mod_poly(poly, modulus):
    return divmod_poly(poly, modulus)[1]


class K20:
    """Element of Q[r]/Phi_20(r), with r the standard zeta_20 symbol."""

    __slots__ = ("poly",)

    def __init__(self, value=0):
        if isinstance(value, K20):
            self.poly = value.poly
        elif isinstance(value, (tuple, list)):
            self.poly = mod_poly(value, PHI20)
        else:
            self.poly = (Fraction(value),)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, K20) else K20(value)

    def __add__(self, other):
        value = K20.coerce(other)
        return K20(add(self.poly, value.poly))

    __radd__ = __add__

    def __neg__(self):
        return K20(scale(self.poly, -1))

    def __sub__(self, other):
        return self + (-K20.coerce(other))

    def __rsub__(self, other):
        return K20.coerce(other) - self

    def __mul__(self, other):
        value = K20.coerce(other)
        return K20(mul(self.poly, value.poly))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        require(exponent >= 0, "negative K20 exponent")
        result = K20(1)
        factor = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result * factor
            factor = factor * factor
            remaining >>= 1
        return result

    def __eq__(self, other):
        return self.poly == K20.coerce(other).poly

    def conjugate(self):
        out = K20(0)
        for exponent, coefficient in enumerate(self.poly):
            out += coefficient * (R ** ((-exponent) % 20))
        return out


class Q3:
    """Exact a+b sqrt(3), used only by the frozen cubic control."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Q3) else Q3(value)

    def __add__(self, other):
        value = Q3.coerce(other)
        return Q3(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q3.coerce(other))

    def __rsub__(self, other):
        return Q3.coerce(other) - self

    def __mul__(self, other):
        value = Q3.coerce(other)
        return Q3(
            self.a * value.a + 3 * self.b * value.b,
            self.a * value.b + self.b * value.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        value = Q3.coerce(other)
        return self.a == value.a and self.b == value.b

    def positive(self):
        if self.a >= 0 and self.b >= 0:
            return self.a != 0 or self.b != 0
        if self.a <= 0 and self.b <= 0:
            return False
        if self.b > 0:
            return 3 * self.b * self.b > self.a * self.a
        return self.a * self.a > 3 * self.b * self.b


def c3_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def c3_neg(value):
    return (-value[0], -value[1])


def c3_sub(left, right):
    return c3_add(left, c3_neg(right))


def c3_mul(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def c3_conjugate(value):
    return (value[0], -value[1])


R = K20((0, 1))
I = R ** 5
ONE = K20(1)


def sigma(value, exponent):
    """Cyclotomic automorphism r -> r^exponent."""
    out = K20(0)
    for degree, coefficient in enumerate(value.poly):
        out += coefficient * (R ** (degree * exponent))
    return out


def quadrant(exponent):
    """Exact quadrant of the standard embedded r^exponent."""
    residue = exponent % 20
    if 1 <= residue <= 4:
        return "I"
    if 6 <= residue <= 9:
        return "II"
    if 11 <= residue <= 14:
        return "III"
    if 16 <= residue <= 19:
        return "IV"
    raise RuntimeError("STOP: root lies on a coordinate axis")


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
            require(
                not isinstance(node.value, (float, complex)),
                "float or complex literal",
            )
        elif isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.add(node.func.id)

    require(
        imports <= {"__future__", "ast", "fractions", "pathlib"},
        "unexpected import",
    )
    require(
        not ({"eval", "exec", "compile", "open"} & calls),
        "dynamic execution call",
    )

    prereg = (path.parent / "PREREG.md").read_text(encoding="utf-8")
    required = (
        "Status: preregistered protocol only. Formal execution count: zero.",
        "P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1",
        "P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-1",
        "THORN-PLENUM-QUADRANT-CHARACTERIZATION",
        "fixed standard complex embedding",
        "sigma_7(i)=-i",
        "z = zeta_3^2",
        "No selector, physical mechanism, or preferred",
        "ACTION_LAYER:   L1",
    )
    return all(item in prereg for item in required)


def point_data(k):
    z_value = R ** (4 * k)
    j_value = ONE + z_value * z_value
    n_value = j_value * j_value.conjugate()
    s_value = (ONE - z_value) * (ONE - z_value.conjugate())
    t_value = -2 * I * z_value * z_value
    re_value = Fraction(1, 2) * (t_value + t_value.conjugate())
    im_value = -Fraction(1, 2) * I * (t_value - t_value.conjugate())
    return {
        "z": z_value,
        "j": j_value,
        "n": n_value,
        "s": s_value,
        "t": t_value,
        "re": re_value,
        "im": im_value,
    }


def main() -> int:
    gate(1, "source_scope_firewall", source_firewall())

    gate(
        2,
        "cyclotomic_20_carrier",
        R ** 20 == ONE
        and R ** 10 == -ONE
        and I == R ** 5
        and I * I == -ONE
        and PHI20 == (1, 0, -1, 0, 1, 0, -1, 0, 1),
    )

    data = {k: point_data(k) for k in range(1, 5)}
    closure_roots = True
    for values in data.values():
        z_value = values["z"]
        phi5_value = sum((z_value ** exponent for exponent in range(5)), K20(0))
        closure_roots &= phi5_value == K20(0)
        closure_roots &= z_value ** 5 == ONE
        closure_roots &= all(z_value ** exponent != ONE for exponent in range(1, 5))
        closure_roots &= values["s"] == ONE + values["n"]
    gate(3, "source_closure_four_roots", closure_roots)

    exponents = {1: 3, 2: 11, 3: 19, 4: 7}
    quadrants = {1: "I", 2: "III", 3: "IV", 4: "II"}
    table_ok = all(
        values["t"] == 2 * (R ** exponents[k])
        and quadrant(exponents[k]) == quadrants[k]
        for k, values in data.items()
    )
    gate(4, "fixed_i_quadrant_table", table_ok)

    phi = R ** 2 + R ** 18
    beta = phi - ONE
    s_j = R ** 3 + R ** 17

    expected_t = {
        1: s_j + I * phi,
        2: -(phi * s_j) - I * beta,
        3: phi * s_j - I * beta,
        4: -s_j + I * phi,
    }
    gate(
        5,
        "fixed_i_exact_coordinates",
        phi * beta == ONE
        and all(data[k]["t"] == expected_t[k] for k in range(1, 5)),
    )

    mount_ok = True
    for values in data.values():
        mount_ok &= values["t"] * values["t"].conjugate() == 4
        mount_ok &= values["re"] * values["re"] == values["s"]
        mount_ok &= values["im"] * values["im"] * values["n"] == ONE
        mount_ok &= values["im"] == 2 - values["n"]
        mount_ok &= values["t"] == values["re"] + I * values["im"]
    gate(6, "plenum_mount_identities", mount_ok)

    n_contract = beta * beta
    n_expand = phi * phi
    flipped_i_first_quadrant = tuple(
        k for k in range(1, 5) if quadrant(exponents[k] + 10) == "I"
    )
    branch_ok = (
        data[1]["n"] == n_contract
        and data[4]["n"] == n_contract
        and data[2]["n"] == n_expand
        and data[3]["n"] == n_expand
        and data[1]["im"] == phi
        and data[4]["im"] == phi
        and data[2]["im"] == -beta
        and data[3]["im"] == -beta
        and data[4]["z"] == data[1]["z"].conjugate()
        and data[4]["t"] == -data[1]["t"].conjugate()
        and data[3]["z"] == data[2]["z"].conjugate()
        and data[3]["t"] == -data[2]["t"].conjugate()
        and flipped_i_first_quadrant == (2,)
        and -data[2]["t"] == 2 * R
    )
    gate(7, "contraction_and_conjugation_signs", branch_ok)

    first_quadrant_fixed_i = tuple(
        k for k in range(1, 5) if quadrants[k] == "I"
    )
    gate(
        8,
        "fixed_i_first_quadrant_unique",
        first_quadrant_fixed_i == (1,)
        and data[1]["z"] == R ** 4
        and data[1]["t"] == s_j + I * phi,
    )

    units = tuple(
        exponent
        for exponent in range(1, 20)
        if exponent % 2 != 0 and exponent % 5 != 0
    )
    public_z = R ** 4
    public_t = data[1]["t"]

    galois_ok = units == (1, 3, 7, 9, 11, 13, 17, 19)
    galois_ok &= all(
        sigma(public_z, exponent) == R ** ((4 * exponent) % 20)
        and sigma(I, exponent) == R ** ((5 * exponent) % 20)
        and sigma(public_t, exponent) == 2 * R ** ((3 * exponent) % 20)
        for exponent in units
    )

    first_quadrant_full = tuple(
        exponent
        for exponent in units
        if quadrant(3 * exponent) == "I"
    )
    galois_ok &= first_quadrant_full == (1, 7)
    galois_ok &= sigma(public_z, 7) == R ** 8
    galois_ok &= sigma(I, 7) == -I
    galois_ok &= sigma(public_t, 7) == 2 * R
    gate(9, "full_galois_first_quadrant_nonunique", galois_ok)

    fixed_i = tuple(exponent for exponent in units if sigma(I, exponent) == I)
    fixed_i_first_quadrant = tuple(
        exponent
        for exponent in fixed_i
        if quadrant(3 * exponent) == "I"
    )
    gate(
        10,
        "fixed_i_stabilizer_unique",
        fixed_i == (1, 9, 13, 17)
        and fixed_i_first_quadrant == (1,),
    )

    one3 = (Q3(1), Q3(0))
    z3 = (Q3(Fraction(-1, 2)), Q3(0, Fraction(-1, 2)))
    z3_squared = c3_mul(z3, z3)
    j3 = c3_add(one3, z3_squared)
    n3_complex = c3_mul(j3, c3_conjugate(j3))
    s3_complex = c3_mul(
        c3_sub(one3, z3),
        c3_sub(one3, c3_conjugate(z3)),
    )
    t3_complex = c3_mul((Q3(0), Q3(-2)), z3_squared)
    trace3_complex = c3_add(z3, c3_conjugate(z3))
    n3 = n3_complex[0]
    s3 = s3_complex[0]
    re3 = t3_complex[0]
    im3 = t3_complex[1]
    phi5_mod_phi3 = mod_poly(PHI5, PHI3)

    cubic_guard = (
        c3_add(c3_add(z3_squared, z3), one3) == (Q3(0), Q3(0))
        and c3_mul(z3, c3_conjugate(z3)) == one3
        and trace3_complex == (Q3(-1), Q3(0))
        and n3_complex == (Q3(1), Q3(0))
        and s3_complex == (Q3(3), Q3(0))
        and t3_complex == (Q3(0, 1), Q3(1))
        and s3 + Q3(1) == Q3(4)
        and s3 != Q3(1) + n3
        and re3 * re3 == s3
        and im3 * im3 * n3 == Q3(1)
        and re3 * re3 + im3 * im3 == Q3(4)
        and im3 == Q3(2) - n3
        and re3.positive()
        and im3.positive()
        and phi5_mod_phi3 == (1, 1)
        and phi5_mod_phi3 != (0,)
    )
    gate(11, "mounted_third_root_lift_guard", cubic_guard)

    prereg = (Path(__file__).parent / "PREREG.md").read_text(encoding="utf-8")
    gate(
        12,
        "scope_nonselector_guard",
        PROBE in prereg
        and "candidate-T ceiling; L1 only" in prereg
        and "does not derive or physically select" in prereg
        and "No selector, physical mechanism, or preferred embedding" in prereg
        and first_quadrant_full == (1, 7)
        and fixed_i_first_quadrant == (1,),
    )

    print("DECISION " + DECISION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
