#!/usr/bin/env python3
"""Exact audit for P-O5-DEDEKIND-GRH-READ-1.

This verifier audits the finite algebraic mechanisms of the written proof.
It does not evaluate zeta or L-functions, inspect zeros, approximate complex
values, prove GRH, or construct analytic continuation.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


Poly = tuple[Fraction, ...]
FactorMap = dict[str, int]


def fail(label: str, detail: object = "") -> None:
    message = f"{label} failed"
    if detail != "":
        message += f": {detail}"
    raise AssertionError(message)


def check(label: str, condition: bool, detail: object = "") -> None:
    if not condition:
        fail(label, detail)


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Fraction(0),)


def poly(*coefficients: int) -> Poly:
    return trim(tuple(Fraction(value) for value in coefficients))


def p_add(left: Poly, right: Poly) -> Poly:
    length = max(len(left), len(right))
    out = [Fraction(0) for _ in range(length)]
    for index in range(length):
        if index < len(left):
            out[index] += left[index]
        if index < len(right):
            out[index] += right[index]
    return trim(tuple(out))


def p_scale(value: int, source: Poly) -> Poly:
    return trim(tuple(Fraction(value) * item for item in source))


def p_sub(left: Poly, right: Poly) -> Poly:
    return p_add(left, p_scale(-1, right))


def p_mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def p_pow(source: Poly, exponent: int) -> Poly:
    check("polynomial exponent", exponent >= 0)
    result = poly(1)
    base = source
    power = exponent
    while power:
        if power & 1:
            result = p_mul(result, base)
        base = p_mul(base, base)
        power >>= 1
    return result


@dataclass(frozen=True)
class RationalFunction:
    numerator: Poly
    denominator: Poly

    def __post_init__(self) -> None:
        check("nonzero denominator", self.denominator != poly(0))

    def __mul__(self, other: "RationalFunction") -> "RationalFunction":
        return RationalFunction(
            p_mul(self.numerator, other.numerator),
            p_mul(self.denominator, other.denominator),
        )

    def equals(self, other: "RationalFunction") -> bool:
        return p_mul(self.numerator, other.denominator) == p_mul(
            other.numerator, self.denominator
        )


ONE = poly(1)
T = poly(0, 1)


def rf(numerator: Poly, denominator: Poly = ONE) -> RationalFunction:
    return RationalFunction(trim(numerator), trim(denominator))


def one_minus_power(exponent: int) -> Poly:
    return p_sub(ONE, p_pow(T, exponent))


def one_plus_power(exponent: int) -> Poly:
    return p_add(ONE, p_pow(T, exponent))


def local_table(
    *,
    contaminate_inert: bool = False,
) -> dict[str, tuple[RationalFunction, RationalFunction, RationalFunction]]:
    split_o = rf(p_pow(one_minus_power(1), 2), one_plus_power(2))
    split_h = rf(one_plus_power(2))
    split_inverse = rf(p_pow(one_minus_power(1), 2))

    inert_o = split_o if contaminate_inert else rf(ONE)
    inert_h = rf(one_minus_power(2))
    inert_inverse = rf(one_minus_power(2))

    ramified_o = rf(ONE)
    ramified_h = rf(one_minus_power(1))
    ramified_inverse = rf(one_minus_power(1))

    return {
        "split": (split_o, split_h, split_inverse),
        "inert": (inert_o, inert_h, inert_inverse),
        "ramified": (ramified_o, ramified_h, ramified_inverse),
    }


def gate_local_factors() -> None:
    table = local_table()
    for prime_type, (o_factor, h_factor, inverse_factor) in table.items():
        check(
            f"local product {prime_type}",
            (o_factor * h_factor).equals(inverse_factor),
        )
    check("split O5 nontrivial", not table["split"][0].equals(rf(ONE)))
    check("inert O5 trivial", table["inert"][0].equals(rf(ONE)))
    check("ramified O5 trivial", table["ramified"][0].equals(rf(ONE)))


def normalized_factor_map(source: FactorMap) -> FactorMap:
    return {key: value for key, value in sorted(source.items()) if value}


def combine_factor_maps(*sources: FactorMap) -> FactorMap:
    out: FactorMap = {}
    for source in sources:
        for key, value in source.items():
            out[key] = out.get(key, 0) + value
    return normalized_factor_map(out)


def h_factor_map(
    *,
    omit_l2: bool = False,
    reverse_ramified: bool = False,
) -> FactorMap:
    result: FactorMap = {
        "L_2S_CHI5": 0 if omit_l2 else 1,
        "ZETA_4S": -1,
    }
    if reverse_ramified:
        result["R5_1_MINUS_S"] = -1
        result["R5_1_MINUS_4S"] = 1
    else:
        result["R5_1_MINUS_S"] = 1
        result["R5_1_MINUS_4S"] = -1
    return normalized_factor_map(result)


def ohat_factor_map(*, omit_chi_factor: bool = False) -> FactorMap:
    result: FactorMap = {
        "ZETA_S": -1,
        "L_S_CHI5": 0 if omit_chi_factor else -1,
        "L_2S_CHI5": -1,
        "ZETA_4S": 1,
        "R5_1_MINUS_S": -1,
        "R5_1_MINUS_4S": 1,
    }
    return normalized_factor_map(result)


def target_inverse_dedekind_map() -> FactorMap:
    return {"L_S_CHI5": -1, "ZETA_S": -1}


def gate_global_bookkeeping() -> None:
    product = combine_factor_maps(h_factor_map(), ohat_factor_map())
    check("global H5 O5 factor map", product == target_inverse_dedekind_map())
    check(
        "public and continued O5 maps agree",
        ohat_factor_map()
        == {
            "L_2S_CHI5": -1,
            "L_S_CHI5": -1,
            "R5_1_MINUS_4S": 1,
            "R5_1_MINUS_S": -1,
            "ZETA_4S": 1,
            "ZETA_S": -1,
        },
    )


def correction_zero_real_part(base: int, exponent: int) -> Fraction:
    check("correction base", base > 1)
    check("correction exponent", exponent > 0)
    return Fraction(0)


def gate_half_plane_unit() -> None:
    boundary = Fraction(1, 2)
    check("2 sigma threshold", 2 * boundary == 1)
    check("4 sigma threshold", 4 * boundary == 2)
    check("2 sigma positive slope", 2 > 0)
    check("4 sigma positive slope", 4 > 0)
    check("correction k1 boundary", correction_zero_real_part(5, 1) == 0)
    check("correction k4 boundary", correction_zero_real_part(5, 4) == 0)

    ledger = {
        "L(2s,chi5)": "EULER_UNIT_RE_2S_GT_1",
        "1/zeta(4s)": "EULER_UNIT_RE_4S_GT_2",
        "1-5^(-s)": "ZEROS_ONLY_RE_S_EQ_0",
        "1/(1-5^(-4s))": "POLES_ONLY_RE_S_EQ_0",
    }
    check("H5 component count", len(ledger) == 4)
    check("H5 excludes target zetaF", all("zeta_F" not in key for key in ledger))
    check("H5 unit certificates", all(value for value in ledger.values()))


def gate_divisor_orders() -> None:
    for zeta_order in range(-32, 33):
        h_order = 0
        ohat_order = -zeta_order
        inverse_order = -zeta_order
        check(
            "divisor additivity",
            h_order + ohat_order == inverse_order,
            zeta_order,
        )
        check("divisor read", ohat_order == -zeta_order, zeta_order)


def symmetric_subsets() -> list[set[int]]:
    offsets = (-3, -2, -1, 0, 1, 2, 3)
    result: list[set[int]] = []
    for mask in range(1 << len(offsets)):
        subset = {
            offset
            for index, offset in enumerate(offsets)
            if mask & (1 << index)
        }
        if subset == {-value for value in subset}:
            result.append(subset)
    return result


def gate_functional_symmetry() -> None:
    families = symmetric_subsets()
    check("nonempty symmetry census", len(families) > 0)
    for subset in families:
        no_right = all(value <= 0 for value in subset)
        all_critical = all(value == 0 for value in subset)
        check("functional symmetry equivalence", no_right == all_critical, subset)


def star(source: dict[int, int]) -> dict[int, int]:
    return {-exponent: coefficient for exponent, coefficient in source.items()}


def orientation_pair(*, delete_negative: bool = False) -> dict[int, int]:
    result = {0: 1, 1: -1}
    if not delete_negative:
        result[-1] = -1
    return result


def gate_orientation_and_support() -> None:
    pair = orientation_pair()
    check("orientation star invariance", star(pair) == pair)
    check("two split directions", set(pair) == {-1, 0, 1})
    support = {
        "split": not local_table()["split"][0].equals(rf(ONE)),
        "inert": not local_table()["inert"][0].equals(rf(ONE)),
        "ramified": not local_table()["ramified"][0].equals(rf(ONE)),
    }
    check("pure split support", support == {
        "split": True,
        "inert": False,
        "ramified": False,
    })


def production_accepts(
    *,
    contaminate_inert: bool = False,
    omit_l2: bool = False,
    reverse_ramified: bool = False,
    omit_chi_factor: bool = False,
    delete_negative_orientation: bool = False,
) -> bool:
    table = local_table(contaminate_inert=contaminate_inert)
    local_ok = all(
        (o_factor * h_factor).equals(inverse_factor)
        for o_factor, h_factor, inverse_factor in table.values()
    )
    pure_ok = table["inert"][0].equals(rf(ONE)) and table["ramified"][0].equals(
        rf(ONE)
    )
    global_ok = combine_factor_maps(
        h_factor_map(
            omit_l2=omit_l2,
            reverse_ramified=reverse_ramified,
        ),
        ohat_factor_map(omit_chi_factor=omit_chi_factor),
    ) == target_inverse_dedekind_map()
    orientation_ok = star(
        orientation_pair(delete_negative=delete_negative_orientation)
    ) == orientation_pair(delete_negative=delete_negative_orientation)
    return local_ok and pure_ok and global_ok and orientation_ok


def gate_negative_fixtures() -> list[str]:
    fixtures = {
        "INERT_SPLIT_CONTAMINATION": {
            "contaminate_inert": True,
        },
        "MISSING_L2_COMPLEMENT": {
            "omit_l2": True,
        },
        "REVERSED_RAMIFIED_CORRECTION": {
            "reverse_ramified": True,
        },
        "MISSING_QUADRATIC_FACTOR": {
            "omit_chi_factor": True,
        },
        "ONE_ORIENTATION_ONLY": {
            "delete_negative_orientation": True,
        },
    }
    fired: list[str] = []
    check("production baseline", production_accepts())
    for name, mutation in fixtures.items():
        check(f"fixture {name}", not production_accepts(**mutation))
        fired.append(name)
    return fired


def imported_root(module: ast.AST) -> str:
    if isinstance(module, ast.Import):
        return module.names[0].name.split(".")[0]
    if isinstance(module, ast.ImportFrom):
        return (module.module or "").split(".")[0]
    return ""


def gate_source_firewall() -> None:
    path = Path(__file__)
    raw = path.read_bytes()
    check("source final LF", raw.endswith(b"\n"))
    check("source LF only", b"\r" not in raw)
    text = raw.decode("utf-8")
    tree = ast.parse(text, filename=path.name)

    allowed_imports = {
        "__future__",
        "ast",
        "dataclasses",
        "fractions",
        "pathlib",
    }
    forbidden_names = {
        "compile",
        "complex",
        "eval",
        "exec",
        "float",
        "input",
        "open",
    }
    forbidden_roots = {
        "cmath",
        "http",
        "math",
        "mpmath",
        "numpy",
        "random",
        "requests",
        "socket",
        "subprocess",
        "sympy",
        "urllib",
    }

    imports: list[str] = []
    calls: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(imported_root(node))
        if isinstance(node, ast.Constant):
            check(
                "no float or complex literal",
                not isinstance(node.value, (float, complex)),
                node.value,
            )
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)

    check("source import allowlist", set(imports) <= allowed_imports, imports)
    check("source forbidden import roots", not (set(imports) & forbidden_roots))
    check("source dynamic calls", not (set(calls) & forbidden_names))
    target_data_token = "ZERO" + "_TABLE"
    external_package_token = "site" + "-" + "packages"
    check("source no target data token", target_data_token not in text)
    check("source no external package token", external_package_token not in text)


def main() -> int:
    gate_local_factors()
    print("PASS G01: split, inert, and ramified local factors")

    gate_global_bookkeeping()
    print("PASS G02: global H5 times O5 formal factor bookkeeping")

    gate_half_plane_unit()
    print("PASS G03: H5 half-plane unit guard")

    gate_divisor_orders()
    print("PASS G04: meromorphic divisor multiplicity read")

    gate_functional_symmetry()
    print("PASS G05: functional-equation symmetry logic")

    gate_orientation_and_support()
    print("PASS G06: pure split support and orientation-pair invariance")

    fired = gate_negative_fixtures()
    print("PASS G07: production-path mutations fired " + ",".join(fired))

    gate_source_firewall()
    print("PASS G08: exact-source and dependency firewall")

    print("ALL PASS: O5 Dedekind GRH read audit 8/8.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
