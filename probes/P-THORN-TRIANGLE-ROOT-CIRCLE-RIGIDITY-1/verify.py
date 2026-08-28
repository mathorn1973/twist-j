#!/usr/bin/env python3
"""Exact audit for P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1.

The universal proof is frozen in PREREG.md. This verifier audits the formal
Laurent identity, the cyclotomic and quadratic reductions, exact branch values,
negative controls, and the pinned primary-seam source boundary. Standard
library only. No floating point, numerical roots, tolerance, randomness,
network, clock, subprocess, or search.
"""

from __future__ import annotations

import ast
import hashlib
from fractions import Fraction
from pathlib import Path


PROBE = "P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1"
CONFIRMED = "THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-CONFIRMED"

BASE_MAIN = "37a0fa95e8a49d2a554651545f33975c1c082bd8"
SOURCE_RESULT_BLOB = "60ad9beb89c0c708ca52c4327f865d759e8a96d5"
SOURCE_PROMO_BLOB = "42b001e781b68178a29dd5bd5f8e56189d4057a9"
CANON_BLOB = "97e9606fc2b2e1e431aa159d8b63180962ead907"
STATUS_BLOB = "80646f07c69d16beb1d2b98ebb21a553c5bb57a2"

PHI5 = (1, 1, 1, 1, 1)
Q_SCALE = (1, -3, 1)
T_RELATION = (-1, 1, 1)  # t^2+t-1


def require(condition, message):
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(number, label, condition):
    require(condition, "G%02d %s" % (number, label))
    print("G%02d %s PASS" % (number, label))


def git_blob_sha(raw):
    header = b"blob " + str(len(raw)).encode("ascii") + b"\0"
    return hashlib.sha1(header + raw).hexdigest()


def read_pinned(path, expected_blob):
    raw = path.read_bytes()
    require(git_blob_sha(raw) == expected_blob, "blob mismatch: " + str(path))
    require(raw.endswith(b"\n"), "missing final LF: " + str(path))
    require(b"\r" not in raw, "non-LF line ending: " + str(path))
    return raw.decode("utf-8")


def poly_trim(poly):
    out = [Fraction(value) for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(left, right):
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        out[index] += Fraction(value)
    for index, value in enumerate(right):
        out[index] += Fraction(value)
    return poly_trim(out)


def poly_neg(poly):
    return poly_trim([-Fraction(value) for value in poly])


def poly_sub(left, right):
    return poly_add(left, poly_neg(right))


def poly_scale(poly, scalar):
    return poly_trim([Fraction(scalar) * Fraction(value) for value in poly])


def poly_mul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            out[left_index + right_index] += Fraction(left_value) * Fraction(right_value)
    return poly_trim(out)


def poly_pow(poly, exponent):
    require(exponent >= 0, "negative polynomial exponent")
    result = [Fraction(1)]
    factor = poly_trim(poly)
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        power >>= 1
    return result


def poly_divmod(numerator, denominator):
    num = poly_trim(numerator)
    den = poly_trim(denominator)
    require(den != [Fraction(0)], "zero polynomial denominator")
    if len(num) < len(den):
        return [Fraction(0)], num
    quotient = [Fraction(0) for _ in range(len(num) - len(den) + 1)]
    work = list(num)
    while len(work) >= len(den) and work != [Fraction(0)]:
        shift = len(work) - len(den)
        factor = work[-1] / den[-1]
        quotient[shift] += factor
        for index, value in enumerate(den):
            work[index + shift] -= factor * value
        work = poly_trim(work)
    return poly_trim(quotient), poly_trim(work)


def poly_mod(poly, modulus):
    return poly_divmod(poly, modulus)[1]


def poly_compose(poly, inner):
    result = [Fraction(0)]
    power = [Fraction(1)]
    for coefficient in poly:
        result = poly_add(result, poly_scale(power, coefficient))
        power = poly_mul(power, inner)
    return poly_trim(result)


def laurent_add(left, right):
    out = dict(left)
    for exponent, value in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + Fraction(value)
    return {exponent: value for exponent, value in out.items() if value}


def laurent_neg(poly):
    return {exponent: -value for exponent, value in poly.items()}


def laurent_sub(left, right):
    return laurent_add(left, laurent_neg(right))


def laurent_mul(left, right):
    out = {}
    for left_exp, left_value in left.items():
        for right_exp, right_value in right.items():
            exponent = left_exp + right_exp
            out[exponent] = out.get(exponent, Fraction(0)) + left_value * right_value
    return {exponent: value for exponent, value in out.items() if value}


def laurent_scale(poly, scalar):
    return {
        exponent: Fraction(scalar) * value
        for exponent, value in poly.items()
        if Fraction(scalar) * value
    }


def laurent_shift(poly, exponent):
    return {power + exponent: value for power, value in poly.items()}


class Q5:
    """Exact a+b*sqrt(5)."""

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        if isinstance(value, Q5):
            return value
        return Q5(value)

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

    def conjugate(self):
        return Q5(self.a, -self.b)

    def norm(self):
        return self.a * self.a - 5 * self.b * self.b

    def inverse(self):
        norm = self.norm()
        require(norm != 0, "inverse of zero in Q(sqrt5)")
        conjugate = self.conjugate()
        return Q5(conjugate.a / norm, conjugate.b / norm)

    def positive(self):
        if self.a >= 0 and self.b >= 0:
            return self.a != 0 or self.b != 0
        if self.a <= 0 and self.b <= 0:
            return False
        if self.b > 0:
            return 5 * self.b * self.b > self.a * self.a
        return self.a * self.a > 5 * self.b * self.b


class GQ:
    """Exact Gaussian rational a+b*i."""

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    @staticmethod
    def coerce(value):
        if isinstance(value, GQ):
            return value
        return GQ(value)

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
        power = exponent
        while power:
            if power & 1:
                result = result * factor
            factor = factor * factor
            power >>= 1
        return result


def source_firewall(root):
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
    allowed = {"__future__", "ast", "hashlib", "fractions", "pathlib"}
    forbidden_imports = {
        "cmath",
        "decimal",
        "math",
        "mpmath",
        "numpy",
        "os",
        "random",
        "requests",
        "secrets",
        "socket",
        "subprocess",
        "sympy",
        "time",
    }
    require(imports <= allowed, "unexpected import set")
    require(not (imports & forbidden_imports), "forbidden import")
    require(not ({"eval", "exec", "compile", "open"} & calls), "forbidden dynamic call")

    status = read_pinned(root / "STATUS.md", STATUS_BLOB)
    canon = read_pinned(root / "canon" / "CANON.md", CANON_BLOB)
    source = read_pinned(
        root / "probes" / "P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1" / "RESULT.md",
        SOURCE_RESULT_BLOB,
    )
    promo = read_pinned(
        root / "notes" / "canon" / "PROMO-CM-ALTERNATING-PRIMARY-LATTICE-SEAM.md",
        SOURCE_PROMO_BLOB,
    )
    prereg = (path.parent / "PREREG.md").read_text(encoding="utf-8")

    status_checks = (
        "STATE:          ACTIVE" in status
        and "CANON:          Public Canon v68" in status
        and "CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581" in status
        and "CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546" in status
        and "CANON_BYTES:    353145" in status
    )
    source_checks = (
        "q(x)=x^2-3x+1" in source
        and "[E_Z : H_Z direct-sum C_Z] = 5" in source
        and "E_Z/(H_Z direct-sum C_Z) = Z/5" in source
        and "PUBLIC CANON STATUS UNCHANGED" in source
        and "scope sha256" in promo
        and "4350d7f162389982e612565e05ab9e89c2ec772da28b0de56331b0ea1cdb8625" in promo
        and "Omega_1 is a convenient basis element" in promo
    )
    canon_checks = (
        "J Jbar = 2 - phi = phi^-2" in canon
        and "s_J^2 = 1 + J Jbar = 3 - phi" in canon
        and "arg J = 2 pi/5" in canon
        and "script-Q phi^2 = 2 pi" in canon
    )
    prereg_checks = (
        "Formal execution count: zero" in prereg
        and "No physical mechanism" in prereg
        and BASE_MAIN in prereg
        and "issue #628" in prereg
    )
    return status_checks and source_checks and canon_checks and prereg_checks


def main():
    root = Path(__file__).resolve().parents[2]

    gate(1, "source_scope_firewall", source_firewall(root))

    one = {0: Fraction(1)}
    z = {1: Fraction(1)}
    zinv = {-1: Fraction(1)}
    t = laurent_add(z, zinv)
    n_value = laurent_mul(t, t)
    s_value = laurent_sub(laurent_scale(one, 2), t)
    closure_defect = laurent_sub(s_value, laurent_add(one, n_value))
    phi5_laurent = {0: Fraction(1), 1: Fraction(1), 2: Fraction(1), 3: Fraction(1), 4: Fraction(1)}
    gate(
        2,
        "unit_circle_laurent_reduction",
        n_value == {-2: Fraction(1), 0: Fraction(2), 2: Fraction(1)}
        and s_value == {-1: Fraction(-1), 0: Fraction(2), 1: Fraction(-1)},
    )
    gate(
        3,
        "closure_equals_phi5",
        laurent_shift(closure_defect, 2) == laurent_neg(phi5_laurent),
    )

    x5_minus_one = (-1, 0, 0, 0, 0, 1)
    quotient, remainder = poly_divmod(x5_minus_one, PHI5)
    primitive = remainder == [Fraction(0)] and quotient == [-1, 1]
    primitive &= all(
        poly_mod(poly_sub(poly_pow((0, 1), exponent), (1,)), PHI5) != [Fraction(0)]
        for exponent in range(1, 5)
    )
    gate(4, "primitive_fifth_order", primitive)

    t_poly = (0, 1)
    n_poly = poly_pow(t_poly, 2)
    s_poly = poly_sub((2,), t_poly)
    q_of_n = poly_compose(Q_SCALE, n_poly)
    inverse_identity = poly_sub(poly_mul(n_poly, poly_sub((3,), n_poly)), (1,))
    quartic_chord = poly_sub(poly_pow(s_poly, 2), poly_scale(n_poly, 5))
    weak_triangle = poly_sub(poly_add(s_poly, poly_sub((3,), n_poly)), (4,))
    gate(
        5,
        "scale_polynomial",
        poly_mod(q_of_n, T_RELATION) == [Fraction(0)],
    )
    gate(
        6,
        "thorn_inverse_and_quartic",
        poly_mod(inverse_identity, T_RELATION) == [Fraction(0)]
        and poly_mod(quartic_chord, T_RELATION) == [Fraction(0)]
        and poly_mod(weak_triangle, T_RELATION) == [Fraction(0)]
        and (Q_SCALE[1] * Q_SCALE[1] - 4 * Q_SCALE[0] * Q_SCALE[2]) == 5,
    )

    n_contract = Q5(Fraction(3, 2), Fraction(-1, 2))
    n_expand = Q5(Fraction(3, 2), Fraction(1, 2))
    s_contract = Q5(Fraction(5, 2), Fraction(-1, 2))
    s_expand = Q5(Fraction(5, 2), Fraction(1, 2))
    q5_zero = Q5(0)
    branch_values = (
        n_contract * n_contract - 3 * n_contract + 1 == q5_zero
        and n_expand * n_expand - 3 * n_expand + 1 == q5_zero
        and s_contract == 1 + n_contract
        and s_expand == 1 + n_expand
        and s_contract * s_contract == 5 * n_contract
        and s_expand * s_expand == 5 * n_expand
        and n_contract * n_expand == 1
    )
    gate(7, "quadratic_branch_values", branch_values)

    trace_contract = Q5(Fraction(-1, 2), Fraction(1, 2))
    trace_expand = Q5(Fraction(-1, 2), Fraction(-1, 2))
    branch_census = (
        trace_contract * trace_contract == n_contract
        and trace_expand * trace_expand == n_expand
        and n_contract.positive()
        and (1 - n_contract).positive()
        and n_expand.positive()
        and (n_expand - 1).positive()
    )
    gate(8, "contracting_expanding_census", branch_census)

    t3 = Fraction(-1)
    n3 = t3 * t3
    s3 = 2 - t3
    third_control = (
        s3 + Fraction(1, n3) == 4
        and s3 != 1 + n3
        and n3 == 1
        and s3 == 3
    )
    gate(9, "weaker_triangle_third_root_control", third_control)

    zi = GQ(0, 1)
    zminus = GQ(-1)
    zr = GQ(Fraction(3, 5), Fraction(4, 5))

    def closure_data(value):
        conjugate = value.conjugate()
        j_value = GQ(1) + value * value
        n_local = j_value * j_value.conjugate()
        s_local = (GQ(1) - value) * (GQ(1) - conjugate)
        phi5_value = sum((value ** exponent for exponent in range(5)), GQ(0))
        return n_local, s_local, s_local - (GQ(1) + n_local), phi5_value

    ni, si, di, pi5i = closure_data(zi)
    nm, sm, dm, pi5m = closure_data(zminus)
    nr, sr, dr, pi5r = closure_data(zr)
    controls = (
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
        and pi5r != 0
    )
    gate(10, "gaussian_rational_controls", controls)

    source_result = (root / "probes" / "P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1" / "RESULT.md").read_text(encoding="utf-8")
    primary_agreement = (
        "q(x)=x^2-3x+1" in source_result
        and "[E_Z : H_Z direct-sum C_Z] = 5" in source_result
        and Q_SCALE == (1, -3, 1)
        and (Q_SCALE[1] * Q_SCALE[1] - 4 * Q_SCALE[0] * Q_SCALE[2]) == 5
    )
    gate(11, "primary_seam_agreement", primary_agreement)

    principal_phi = Q5(Fraction(1, 2), Fraction(1, 2))
    principal_n = Q5(2) - principal_phi
    principal_s = Q5(3) - principal_phi
    principal = (
        principal_n == n_contract
        and principal_s == s_contract
        and principal_s * principal_s == 5 * principal_n
    )
    gate(12, "principal_scalar_and_scope_guard", principal)

    print("DECISION " + CONFIRMED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
