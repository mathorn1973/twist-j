#!/usr/bin/env python3
"""Static, result-neutral pin checker for P-TM-SYM2-SEMILINEAR-GAUGE-1.

This checker reads bytes and parses Python source with ``ast``.  It never
imports, compiles, or executes verify.py and never solves an incidence case.
"""

from __future__ import annotations

import ast
import hashlib
import re
import sys
from pathlib import Path
from typing import Any


PROBE_ID = "P-TM-SYM2-SEMILINEAR-GAUGE-1"
PROBE_DIR = Path(__file__).resolve().parent

PIN_VERIFY_SHA256 = "f526af796e0fd2951d5b136b17f786045a932214744040dfd0b86e47c50b3590"

EXPECTED_FILES = frozenset(
    {
        "PREREG.md",
        "verify.py",
        "check_pin.py",
        "SOURCE-PREDEFINITION.md",
        "SOURCE-MEASURE1-EXPECTED.txt",
    }
)

FORBIDDEN_PREPIN_FILES = frozenset({"EXPECTED.txt", "RUN.md", "RESULT.md"})

SOURCE_SPECS = {
    "SOURCE-PREDEFINITION.md": {
        "sha256": "9f5dfe902bb0ff9fc19c4bdc4fb1095301a55bd00201f770ab81a36899c2273f",
        "bytes": 25896,
        "lf": 776,
        "cr": 0,
        "markers": (
            b"## 7. Semilinear realization group and effective gauge",
            b"## 8. Analytic ceiling, dichotomy, and scientific routes",
            b"## 9. Contract for the future exact scan",
            b"These are all 96",
            b"LINEAR-ONLY",
            b"SEMILINEAR-DOUBLE",
        ),
    },
    "SOURCE-MEASURE1-EXPECTED.txt": {
        "sha256": "395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f",
        "bytes": 9879,
        "lf": 79,
        "cr": 0,
        "markers": (
            b"AUDIT: line-set projective stabilizer order 60; Aut(Lines, sigma_line) order 12",
            b"AUDIT: gauge action free: yes",
            b"B5 ORBIT 4: size 12",
            b"ROUTE: NEGATIVE (N2: the canonicality test returns NONCANONICAL)",
            b"RESULT: PASS (all certificates green in mode --evaluate)",
        ),
    },
}

REQUIRED_PREREG_MARKERS = (
    "# PREREG. P-TM-SYM2-SEMILINEAR-GAUGE-1",
    "public formal lock:     issue #134",
    "branch parent:          87c1a0a42a23ad68612cabcddd1c91fd784c9150",
    "SOURCE-PREDEFINITION.md",
    "9f5dfe902bb0ff9fc19c4bdc4fb1095301a55bd00201f770ab81a36899c2273f",
    "SOURCE-MEASURE1-EXPECTED.txt",
    "395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f",
    "B tau^e(v_i) = lambda_i v_(p(i))",
    "Exactly `2*48=96` incidence cases",
    "LINEAR-ONLY",
    "SEMILINEAR-DOUBLE",
    "c=(1,0)  -> residual invariant chi_F",
    "c=(0,1)  -> residual invariant chi_Q",
    "c=(1,1)  -> residual invariant chi_Q chi_F",
    "## 7. Frozen failure threshold",
    "## 8. Action layer and debt firewall",
    "scientific layer:       L5 structural candidate equivalence only",
    "excluded layer:         L6 physical measure",
    "deterministic runs:     exactly 1",
    "one owner-authorized JAS 2 or JAS 4 Linux runner",
    "No Studio execution belongs to this lane.",
)

ALLOWED_IMPORT_ROOTS = frozenset(
    {
        "__future__",
        "ast",
        "collections",
        "dataclasses",
        "enum",
        "fractions",
        "functools",
        "hashlib",
        "itertools",
        "json",
        "math",
        "operator",
        "pathlib",
        "re",
        "sys",
        "typing",
    }
)

REQUIRED_FUNCTIONS = frozenset(
    {
        "enumerate_w",
        "enumerate_selectors",
        "build_incidence_system",
        "projective_frame_candidate",
        "frame_completeness_certificate",
        "rref",
        "verify_rref_certificate",
        "determinant_polynomial_coefficients",
        "choose_invertible_witness",
        "verify_incidence_witness",
        "semilinear_compose",
        "semilinear_inverse",
        "faithfulness_certificate",
        "character_pair",
        "selector_orbits",
        "completeness_certificate",
        "emit_transcript",
        "main",
    }
)

REQUIRED_CONSTANTS: dict[str, Any] = {
    "PROBE_ID": PROBE_ID,
    "SOURCE_PREDEFINITION_FILENAME": "SOURCE-PREDEFINITION.md",
    "SOURCE_MEASURE1_EXPECTED_FILENAME": "SOURCE-MEASURE1-EXPECTED.txt",
    "SOURCE_PREDEFINITION_SHA256": SOURCE_SPECS["SOURCE-PREDEFINITION.md"][
        "sha256"
    ],
    "SOURCE_MEASURE1_EXPECTED_SHA256": SOURCE_SPECS[
        "SOURCE-MEASURE1-EXPECTED.txt"
    ]["sha256"],
    "SCAN_EXPONENTS": (0, 1),
    "W_ORDER_THEOREM": 48,
    "SELECTOR_COUNT_THEOREM": 48,
    "SCAN_CASE_COUNT_THEOREM": 96,
    "LINEAR_GAUGE_ORDER_THEOREM": 12,
    "POSSIBLE_GAMMA_ORDERS": (12, 24),
    "DETERMINANT_GRID": (0, 1, 2, 3),
    "COSET_CHARACTER_CASES": ((1, 0), (0, 1), (1, 1)),
    "RESIDUAL_INVARIANT_BY_CHARACTER": {
        (1, 0): "chi_F",
        (0, 1): "chi_Q",
        (1, 1): "chi_Q chi_F",
    },
    "SCIENTIFIC_ROUTES": ("LINEAR-ONLY", "SEMILINEAR-DOUBLE"),
    "STOP_ROUTE": "STOP",
}

REQUIRED_SOURCE_MARKERS = (
    "CASE_TABLE_SHA256",
    "ACCEPTED_REALIZATIONS",
    "ROUTE",
    "GAMMA_SL_ORDER",
    "EXPONENT_ONE_COUNT",
    "COSET_CHARACTER",
    "RESIDUAL_INVARIANT",
    "SELECTOR_ORBIT_COUNT",
    "SELECTOR_ORBIT_SIZES",
    "RESULT",
    "PASS",
)

FORBIDDEN_CALL_NAMES = frozenset(
    {
        "__import__",
        "breakpoint",
        "compile",
        "eval",
        "exec",
        "exit",
        "input",
        "open",
        "quit",
    }
)

FORBIDDEN_ATTRIBUTE_CALLS = frozenset(
    {
        "Popen",
        "check_call",
        "check_output",
        "chmod",
        "connect",
        "download",
        "execv",
        "execve",
        "fork",
        "import_module",
        "mkdir",
        "open",
        "remove",
        "rename",
        "replace",
        "request",
        "rmdir",
        "run",
        "send",
        "socket",
        "spawn",
        "start",
        "symlink_to",
        "system",
        "touch",
        "unlink",
        "urlopen",
        "write_bytes",
        "write_text",
    }
)

FORBIDDEN_RESULT_NAMES = frozenset(
    {
        "EXPECTED_ROUTE",
        "EXPECTED_SCIENTIFIC_ROUTE",
        "EXPECTED_EXPONENT_ONE",
        "EXPECTED_EXPONENT_ONE_COUNT",
        "EXPECTED_GAMMA_ORDER",
        "EXPECTED_GAMMA_SL_ORDER",
        "EXPECTED_COSET_CHARACTER",
        "EXPECTED_RESIDUAL_INVARIANT",
        "EXPECTED_SELECTOR_ORBITS",
        "EXPECTED_ORBIT_PARTITION",
        "EXPECTED_OUTPUT_SHA256",
        "FORMAL_OUTPUT_SHA256",
        "PINNED_RESULT",
        "SEMILINEAR_WITNESS",
    }
)

FORBIDDEN_LITERAL_STRINGS = frozenset(
    {
        "EXPECTED.txt",
        "RUN.md",
        "RESULT.md",
        "ROUTE: LINEAR-ONLY",
        "ROUTE: SEMILINEAR-DOUBLE",
    }
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def add_error(errors: list[str], code: str) -> None:
    errors.append(code)


def read_regular_file(name: str, errors: list[str]) -> bytes | None:
    path = PROBE_DIR / name
    if path.is_symlink():
        add_error(errors, f"{name}:symlink-forbidden")
        return None
    if not path.is_file():
        add_error(errors, f"{name}:missing-or-nonregular")
        return None
    try:
        return path.read_bytes()
    except OSError:
        add_error(errors, f"{name}:read-failed")
        return None


def check_inventory(errors: list[str]) -> None:
    try:
        entries = list(PROBE_DIR.iterdir())
    except OSError:
        add_error(errors, "inventory:read-failed")
        return

    actual = {entry.name for entry in entries}
    for name in sorted(EXPECTED_FILES - actual):
        add_error(errors, f"inventory:missing:{name}")
    for name in sorted(actual - EXPECTED_FILES):
        add_error(errors, f"inventory:unexpected:{name}")
    for name in sorted(FORBIDDEN_PREPIN_FILES & actual):
        add_error(errors, f"inventory:formal-result-forbidden:{name}")

    for entry in sorted(entries, key=lambda item: item.name):
        if entry.name not in EXPECTED_FILES:
            continue
        if entry.is_symlink() or not entry.is_file():
            add_error(errors, f"inventory:nonregular:{entry.name}")


def check_text_file(
    name: str, data: bytes | None, errors: list[str]
) -> str | None:
    if data is None:
        return None
    if data.startswith(b"\xef\xbb\xbf"):
        add_error(errors, f"{name}:utf8-bom-forbidden")
    if b"\x00" in data:
        add_error(errors, f"{name}:nul-forbidden")
    if b"\r" in data:
        add_error(errors, f"{name}:cr-forbidden")
    if data and not data.endswith(b"\n"):
        add_error(errors, f"{name}:missing-final-lf")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        add_error(errors, f"{name}:not-utf8")
        return None


def check_sources(errors: list[str]) -> None:
    for name, spec in SOURCE_SPECS.items():
        data = read_regular_file(name, errors)
        if data is None:
            continue
        if len(data) != spec["bytes"]:
            add_error(errors, f"{name}:byte-count")
        if data.count(b"\n") != spec["lf"]:
            add_error(errors, f"{name}:lf-count")
        if data.count(b"\r") != spec["cr"]:
            add_error(errors, f"{name}:cr-count")
        if sha256_bytes(data) != spec["sha256"]:
            add_error(errors, f"{name}:sha256")
        for marker in spec["markers"]:
            if marker not in data:
                add_error(
                    errors,
                    f"{name}:marker:{sha256_bytes(marker)[:12]}",
                )


def check_prereg(errors: list[str]) -> None:
    data = read_regular_file("PREREG.md", errors)
    text = check_text_file("PREREG.md", data, errors)
    if text is None:
        return
    for marker in REQUIRED_PREREG_MARKERS:
        if marker not in text:
            add_error(
                errors,
                f"PREREG.md:marker:{sha256_bytes(marker.encode())[:12]}",
            )
    if not re.fullmatch(r"[0-9a-f]{64}", PIN_VERIFY_SHA256):
        add_error(errors, "verify.py:pin-sha-placeholder-unresolved")
    expected_line = f"verify.py SHA-256: {PIN_VERIFY_SHA256}"
    if expected_line not in text:
        add_error(errors, "PREREG.md:verify-sha-line")


def imported_roots(tree: ast.AST) -> set[str]:
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(alias.name.split(".", 1)[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                roots.add("<relative>")
            elif node.module:
                roots.add(node.module.split(".", 1)[0])
    return roots


def top_level_constants(tree: ast.Module) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for node in tree.body:
        name: str | None = None
        value_node: ast.AST | None = None
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                name = target.id
                value_node = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            value_node = node.value
        if name is None or value_node is None:
            continue
        try:
            values[name] = ast.literal_eval(value_node)
        except (ValueError, TypeError, SyntaxError):
            continue
    return values


def string_literals(tree: ast.AST) -> set[str]:
    return {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }


def has_zero_argument_main_guard(tree: ast.Module) -> bool:
    for node in tree.body:
        if not isinstance(node, ast.If):
            continue
        test = node.test
        if not isinstance(test, ast.Compare):
            continue
        if not isinstance(test.left, ast.Name) or test.left.id != "__name__":
            continue
        if len(test.ops) != 1 or not isinstance(test.ops[0], ast.Eq):
            continue
        if len(test.comparators) != 1:
            continue
        comparator = test.comparators[0]
        if not (
            isinstance(comparator, ast.Constant)
            and comparator.value == "__main__"
        ):
            continue
        for child in ast.walk(node):
            if not isinstance(child, ast.Call):
                continue
            if isinstance(child.func, ast.Name) and child.func.id == "main":
                if not child.args and not child.keywords:
                    return True
            if (
                isinstance(child.func, ast.Name)
                and child.func.id == "SystemExit"
                and child.args
            ):
                first = child.args[0]
                if (
                    isinstance(first, ast.Call)
                    and isinstance(first.func, ast.Name)
                    and first.func.id == "main"
                    and not first.args
                    and not first.keywords
                ):
                    return True
    return False


def check_main_signature(
    functions: dict[str, ast.FunctionDef | ast.AsyncFunctionDef],
    errors: list[str],
) -> None:
    node = functions.get("main")
    if node is None:
        return
    args = node.args
    if (
        args.posonlyargs
        or args.args
        or args.kwonlyargs
        or args.vararg is not None
        or args.kwarg is not None
    ):
        add_error(errors, "verify.py:main-must-have-zero-arguments")


def check_calls_and_attributes(tree: ast.Module, errors: list[str]) -> None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in FORBIDDEN_CALL_NAMES:
                    add_error(errors, f"verify.py:forbidden-call:{node.func.id}")
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr in FORBIDDEN_ATTRIBUTE_CALLS:
                    add_error(
                        errors,
                        f"verify.py:forbidden-attribute-call:{node.func.attr}",
                    )
        if isinstance(node, ast.Attribute):
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "sys"
                and node.attr in {"argv", "stderr"}
            ):
                add_error(errors, f"verify.py:forbidden-sys-{node.attr}")
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            add_error(errors, "verify.py:float-literal-forbidden")


def check_required_calls(tree: ast.Module, errors: list[str]) -> None:
    called = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    for name in sorted(REQUIRED_FUNCTIONS - {"main"}):
        if name not in called:
            add_error(errors, f"verify.py:required-function-not-called:{name}")


def check_neutrality(
    tree: ast.Module, constants: dict[str, Any], errors: list[str]
) -> None:
    for name in sorted(FORBIDDEN_RESULT_NAMES & constants.keys()):
        add_error(errors, f"verify.py:forbidden-result-constant:{name}")

    for name, value in sorted(constants.items()):
        upper = name.upper()
        if upper.startswith("EXPONENT_ONE_") and isinstance(
            value, (tuple, list, dict)
        ):
            if len(value) != 0:
                add_error(
                    errors,
                    f"verify.py:embedded-exponent-one-data:{name}",
                )
        if "EXPECTED" in upper and not upper.startswith(
            "SOURCE_MEASURE1_EXPECTED"
        ):
            if name not in {
                "W_ORDER_THEOREM",
                "SELECTOR_COUNT_THEOREM",
                "SCAN_CASE_COUNT_THEOREM",
            }:
                add_error(errors, f"verify.py:unexpected-result-name:{name}")

    literals = string_literals(tree)
    for value in sorted(FORBIDDEN_LITERAL_STRINGS & literals):
        add_error(
            errors,
            f"verify.py:forbidden-literal:{sha256_bytes(value.encode())[:12]}",
        )

    for value in literals:
        normalized = value.replace("\\", "/")
        if "P-TM-SYM2-MEASURE-1/verify.py" in normalized:
            add_error(errors, "verify.py:old-verifier-access")


def check_verify(errors: list[str]) -> None:
    data = read_regular_file("verify.py", errors)
    text = check_text_file("verify.py", data, errors)
    if data is None or text is None:
        return

    if re.fullmatch(r"[0-9a-f]{64}", PIN_VERIFY_SHA256):
        if sha256_bytes(data) != PIN_VERIFY_SHA256:
            add_error(errors, "verify.py:sha256")

    try:
        tree = ast.parse(text, filename="verify.py", mode="exec")
    except SyntaxError:
        add_error(errors, "verify.py:syntax")
        return

    roots = imported_roots(tree)
    for root in sorted(roots - ALLOWED_IMPORT_ROOTS):
        add_error(errors, f"verify.py:forbidden-import:{root}")

    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    for name in sorted(REQUIRED_FUNCTIONS - functions.keys()):
        add_error(errors, f"verify.py:required-function-missing:{name}")
    if any(
        isinstance(node, ast.AsyncFunctionDef) for node in functions.values()
    ):
        add_error(errors, "verify.py:async-function-forbidden")

    check_main_signature(functions, errors)
    if not has_zero_argument_main_guard(tree):
        add_error(errors, "verify.py:zero-argument-main-guard")

    constants = top_level_constants(tree)
    for name, expected in REQUIRED_CONSTANTS.items():
        if name not in constants:
            add_error(errors, f"verify.py:required-constant-missing:{name}")
        elif constants[name] != expected:
            add_error(errors, f"verify.py:required-constant-value:{name}")

    for marker in REQUIRED_SOURCE_MARKERS:
        if marker not in text:
            add_error(errors, f"verify.py:source-marker:{marker}")

    check_calls_and_attributes(tree, errors)
    check_required_calls(tree, errors)
    check_neutrality(tree, constants, errors)


def run_checks() -> list[str]:
    errors: list[str] = []
    check_inventory(errors)
    check_sources(errors)
    check_prereg(errors)
    check_verify(errors)
    return sorted(set(errors))


def main() -> int:
    try:
        errors = run_checks()
    except Exception as exc:
        print("PIN-CHECK: FAIL")
        print(f"ERROR: internal-check:{type(exc).__name__}")
        return 1

    if errors:
        print("PIN-CHECK: FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"PIN-CHECK: PASS {PROBE_ID}")
    print("MODE: static AST/source/hash/inventory only")
    print("FORMAL-EVALUATION: NOT RUN")
    print("RESULT-NEUTRALITY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
