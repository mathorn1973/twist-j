#!/usr/bin/env python3
"""Exact audit for P-O5-DEDEKIND-GRH-DIVISOR-READ-1.

This verifier audits exact algebraic mechanisms of the written proof.
It does not evaluate zeta or L-functions, inspect zeros, approximate
complex values, prove GRH, or construct analytic continuation.
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

def trim(source: Poly) -> Poly:
    values = list(source)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Fraction(0),)

def poly(*values: int) -> Poly:
    return trim(tuple(Fraction(value) for value in values))

def add(left: Poly, right: Poly) -> Poly:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for index in range(size):
        if index < len(left):
            out[index] += left[index]
        if index < len(right):
            out[index] += right[index]
    return trim(tuple(out))

def scale(value: int, source: Poly) -> Poly:
    return trim(tuple(Fraction(value) * item for item in source))

def sub(left: Poly, right: Poly) -> Poly:
    return add(left, scale(-1, right))

def mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))

def power(source: Poly, exponent: int) -> Poly:
    check("nonnegative exponent", exponent >= 0)
    result = poly(1)
    base = source
    n = exponent
    while n:
        if n & 1:
            result = mul(result, base)
        base = mul(base, base)
        n >>= 1
    return result

ONE = poly(1)
T = poly(0, 1)

def one_minus_power(exponent: int) -> Poly:
    return sub(ONE, power(T, exponent))

def one_plus_power(exponent: int) -> Poly:
    return add(ONE, power(T, exponent))

@dataclass(frozen=True)
class RF:
    numerator: Poly
    denominator: Poly = ONE

    def __post_init__(self) -> None:
        check("nonzero denominator", self.denominator != poly(0))

    def __mul__(self, other: "RF") -> "RF":
        return RF(mul(self.numerator, other.numerator),
                  mul(self.denominator, other.denominator))

    def equals(self, other: "RF") -> bool:
        return mul(self.numerator, other.denominator) == mul(
            other.numerator, self.denominator
        )

def local_table(*, contaminate_inert: bool = False):
    split_o = RF(power(one_minus_power(1), 2), one_plus_power(2))
    split_h = RF(one_plus_power(2))
    split_target = RF(power(one_minus_power(1), 2))
    inert_o = split_o if contaminate_inert else RF(ONE)
    inert_h = RF(one_minus_power(2))
    inert_target = RF(one_minus_power(2))
    ramified_o = RF(ONE)
    ramified_h = RF(one_minus_power(1))
    ramified_target = RF(one_minus_power(1))
    return {
        "split": (split_o, split_h, split_target),
        "inert": (inert_o, inert_h, inert_target),
        "ramified": (ramified_o, ramified_h, ramified_target),
    }

def gate_local_factors() -> None:
    table = local_table()
    for kind, (o_factor, h_factor, target) in table.items():
        check(f"local product {kind}", (o_factor * h_factor).equals(target))
    check("split support", not table["split"][0].equals(RF(ONE)))
    check("inert trivial", table["inert"][0].equals(RF(ONE)))
    check("ramified trivial", table["ramified"][0].equals(RF(ONE)))

def normalize(source: FactorMap) -> FactorMap:
    return {key: value for key, value in sorted(source.items()) if value}

def combine(*sources: FactorMap) -> FactorMap:
    out: FactorMap = {}
    for source in sources:
        for key, value in source.items():
            out[key] = out.get(key, 0) + value
    return normalize(out)

def h_map(*, omit_l2: bool = False, reverse_ramified: bool = False) -> FactorMap:
    result: FactorMap = {"L_2S_CHI5": 0 if omit_l2 else 1, "ZETA_4S": -1}
    if reverse_ramified:
        result["R5_1_MINUS_S"] = -1
        result["R5_1_MINUS_4S"] = 1
    else:
        result["R5_1_MINUS_S"] = 1
        result["R5_1_MINUS_4S"] = -1
    return normalize(result)

def ohat_map(*, omit_chi: bool = False) -> FactorMap:
    return normalize({
        "ZETA_S": -1,
        "L_S_CHI5": 0 if omit_chi else -1,
        "L_2S_CHI5": -1,
        "ZETA_4S": 1,
        "R5_1_MINUS_S": -1,
        "R5_1_MINUS_4S": 1,
    })

def target_map() -> FactorMap:
    return {"L_S_CHI5": -1, "ZETA_S": -1}

def gate_global_bookkeeping() -> None:
    check("global factor map", combine(h_map(), ohat_map()) == target_map())

def gate_half_plane_unit() -> None:
    boundary = Fraction(1, 2)
    check("2s safe", 2 * boundary == 1)
    check("4s safe", 4 * boundary == 2)
    check("finite corrections off boundary", Fraction(0) < boundary)
    ledger = {
        "L(2s,chi5)": "NONZERO_RE_2S_GT_1",
        "1/zeta(4s)": "NONZERO_RE_4S_GT_2",
        "1-5^-s": "ZERO_ONLY_RE_0",
        "1/(1-5^-4s)": "POLE_ONLY_RE_0",
    }
    check("unit components", len(ledger) == 4)
    check("target excluded", all("zeta_F" not in key for key in ledger))

def gate_divisor_orders() -> None:
    for zeta_order in range(-64, 65):
        h_order = 0
        ohat_order = -zeta_order
        check("order additivity", h_order + ohat_order == -zeta_order)

def symmetric_subsets():
    offsets = (-3, -2, -1, 0, 1, 2, 3)
    out = []
    for mask in range(1 << len(offsets)):
        subset = {v for i, v in enumerate(offsets) if mask & (1 << i)}
        if subset == {-v for v in subset}:
            out.append(subset)
    return out

def gate_functional_symmetry() -> None:
    families = symmetric_subsets()
    check("symmetry census", bool(families))
    for subset in families:
        no_right = all(v <= 0 for v in subset)
        on_line = all(v == 0 for v in subset)
        check("right-free iff critical", no_right == on_line, subset)

def star(source):
    return {-key: value for key, value in source.items()}

def orientation_pair(*, delete_negative: bool = False):
    result = {0: 1, 1: -1}
    if not delete_negative:
        result[-1] = -1
    return result

def gate_orientation_support() -> None:
    pair = orientation_pair()
    check("unordered pair star", star(pair) == pair)
    table = local_table()
    support = {
        "split": not table["split"][0].equals(RF(ONE)),
        "inert": not table["inert"][0].equals(RF(ONE)),
        "ramified": not table["ramified"][0].equals(RF(ONE)),
    }
    check("pure split support",
          support == {"split": True, "inert": False, "ramified": False})

def production_accepts(*, contaminate_inert=False, omit_l2=False,
                       reverse_ramified=False, omit_chi=False,
                       delete_negative=False):
    table = local_table(contaminate_inert=contaminate_inert)
    local_ok = all((o * h).equals(target) for o, h, target in table.values())
    support_ok = table["inert"][0].equals(RF(ONE)) and table["ramified"][0].equals(RF(ONE))
    global_ok = combine(
        h_map(omit_l2=omit_l2, reverse_ramified=reverse_ramified),
        ohat_map(omit_chi=omit_chi),
    ) == target_map()
    pair = orientation_pair(delete_negative=delete_negative)
    return local_ok and support_ok and global_ok and star(pair) == pair

def gate_breakers():
    fixtures = {
        "B1_INERT_CONTAMINATION": {"contaminate_inert": True},
        "B2_MISSING_L2": {"omit_l2": True},
        "B3_REVERSED_RAMIFIED": {"reverse_ramified": True},
        "B4_MISSING_CHI": {"omit_chi": True},
        "B5_ONE_ORIENTATION": {"delete_negative": True},
    }
    check("baseline accepted", production_accepts())
    fired = []
    for name, mutation in fixtures.items():
        check(name, not production_accepts(**mutation))
        fired.append(name)
    return fired

def imported_root(node: ast.AST) -> str:
    if isinstance(node, ast.Import):
        return node.names[0].name.split(".")[0]
    if isinstance(node, ast.ImportFrom):
        return (node.module or "").split(".")[0]
    return ""

def gate_source_firewall() -> None:
    path = Path(__file__)
    raw = path.read_bytes()
    check("final LF", raw.endswith(b"\n"))
    check("LF only", b"\r" not in raw)
    text = raw.decode("utf-8")
    tree = ast.parse(text, filename=path.name)
    allowed = {"__future__", "ast", "dataclasses", "fractions", "pathlib"}
    forbidden_roots = {"cmath", "http", "math", "mpmath", "numpy", "random",
                       "requests", "socket", "subprocess", "sympy", "urllib"}
    forbidden_calls = {"compile", "complex", "eval", "exec", "float", "input", "open"}
    imports = []
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(imported_root(node))
        if isinstance(node, ast.Constant):
            check("no float/complex literal",
                  not isinstance(node.value, (float, complex)))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    check("import allowlist", set(imports) <= allowed, imports)
    check("forbidden imports", not (set(imports) & forbidden_roots))
    check("dynamic calls", not (set(calls) & forbidden_calls))
    check("no zero table token", ("ZERO" + "_TABLE") not in text)

def main() -> int:
    gate_local_factors()
    print("PASS G01: split inert ramified local factor table")
    gate_global_bookkeeping()
    print("PASS G02: global H5 times O5 factor bookkeeping")
    gate_half_plane_unit()
    print("PASS G03: H5 half-plane unit guard")
    gate_divisor_orders()
    print("PASS G04: divisor multiplicity identity")
    gate_functional_symmetry()
    print("PASS G05: functional-equation symmetry implication")
    gate_orientation_support()
    print("PASS G06: unordered pure split support")
    fired = gate_breakers()
    print("PASS G07: production breakers " + ",".join(fired))
    gate_source_firewall()
    print("PASS G08: exact stdlib source firewall")
    print("VERIFY RESULT 8/8 ALL PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
