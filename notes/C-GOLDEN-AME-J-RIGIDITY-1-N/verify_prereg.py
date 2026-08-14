#!/usr/bin/env python3
"""Target-free verifier for public preregistration issue #369.

This program checks authority, immutable source bytes, the raw-constructor
AST/import firewall, and the two already permitted construction/toy-method
transcripts.  It never imports a target evaluator and performs no Groebner,
radical, saturation, elimination, branch, or target-relation computation.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Mapping


CANON_BYTES = 222_760
CANON_SHA256 = "6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff"
ACTIVATION_COMMIT = "6545c1d0de61ff4696eb3de1a258139e8891f436"
CONTENT_COMMIT = "62628ca4da2d938e4e3a122d35c0d93a6debc27f"

ORIGINAL_PIN = {
    "bytes": 8515,
    "sha256": "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae",
    "git_blob_sha1": "e0d0e171d58b3360c39595d677ffc401a466112d",
}
BLOCK944_PIN = {
    "bytes": 8234,
    "sha256": "af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649",
    "git_blob_sha1": "caab29cb76e60e3165abf70931cf35e387b6e3b1",
}

RAW_MODULE_SHA256 = "b26844a99db5ff9baf4ed7493ed8c9c7aea28a561c8eeadb2c70fdc77530383c"
PRELOCK_AUDIT_SHA256 = "63a2d9a012e1abfcfe636e499bcb4c0041df86a7db6ec7a133b5f824c7ea3ac9"
CAS_SELFTEST_SHA256 = "ff928f0d566e29b40a26fd7637e2095c6e7b9b4e0ec40323385274cf2aa9b1c7"
PRELOCK_EXPECTED_SHA256 = "db6b65ae3243096f663778ced57ee9f5682fffc01b27ff74d7d150d197eb9c79"
CAS_EXPECTED_SHA256 = "500ccdbdd9a64ef8a3fc62c280f621ef519960f7c491e9bf454c8cfb44b7aa48"

EQUATION_COORDINATES = "3889"
ACTIVE_EQUATIONS = "383"
SERIALIZATION_BYTES = "136262"
SERIALIZATION_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"

EXPECTED_RAW_IMPORTS = (
    ("from", "__future__", 0, (("annotations", None),)),
    ("from", "collections", 0, (("Counter", None), ("defaultdict", None))),
    ("from", "dataclasses", 0, (("dataclass", None),)),
    ("import", None, 0, (("hashlib", None),)),
    ("import", None, 0, (("json", None),)),
    ("import", None, 0, (("re", None),)),
    (
        "from",
        "typing",
        0,
        (("Iterable", None), ("Iterator", None), ("Mapping", None), ("Sequence", None)),
    ),
)

FORBIDDEN_DYNAMIC_CALLS = {
    "__import__",
    "compile",
    "eval",
    "exec",
    "import_module",
    "open",
    "popen",
    "run",
    "system",
}

FORBIDDEN_SEMANTIC_NAMES = {
    "cyclotomic",
    "eliminant",
    "elimination",
    "factorization",
    "golden_ratio",
    "groebner",
    "ideal_membership",
    "locator",
    "phi20",
    "radical",
    "resultant",
    "root_of_unity",
    "saturation",
    "sqrt5",
    "zeta5",
    "zeta20",
    "zeta40",
    "zeta_5",
    "zeta_20",
    "zeta_40",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify_bytes(path: Path, pin: Mapping[str, object], *, git_blob: bool = False) -> bytes:
    require(path.is_file(), f"missing file: {path.name}")
    data = path.read_bytes()
    require(len(data) == pin["bytes"], f"byte-count mismatch: {path.name}")
    require(sha256_bytes(data) == pin["sha256"], f"SHA-256 mismatch: {path.name}")
    if git_blob:
        require(
            git_blob_sha1(data) == pin["git_blob_sha1"],
            f"git-blob mismatch: {path.name}",
        )
    return data


def status_fields(status_text: str) -> dict[str, str]:
    wanted = {
        "STATE",
        "CANON",
        "AUTHORITY",
        "TAG",
        "CONTENT_COMMIT",
        "CANON_SHA256",
        "CANON_BYTES",
    }
    output = {}
    for line in status_text.splitlines():
        match = re.match(r"^([A-Z0-9_]+):\s+(.+?)\s*$", line)
        if match and match.group(1) in wanted:
            output[match.group(1)] = match.group(2)
    return output


def verify_authority(repo_root: Path, package: Path) -> None:
    status = status_fields((repo_root / "STATUS.md").read_text("utf-8"))
    expected_status = {
        "STATE": "ACTIVE",
        "CANON": "Public Canon v46",
        "AUTHORITY": "mathorn1973/twist-j main",
        "TAG": "canon-v46",
        "CONTENT_COMMIT": CONTENT_COMMIT,
        "CANON_SHA256": CANON_SHA256,
        "CANON_BYTES": str(CANON_BYTES),
    }
    require(status == expected_status, "STATUS.md authority tuple mismatch")

    canon = (repo_root / "canon" / "CANON.md").read_bytes()
    require(len(canon) == CANON_BYTES, "Canon byte-count mismatch")
    require(sha256_bytes(canon) == CANON_SHA256, "Canon SHA-256 mismatch")

    pins = json.loads((package / "SOURCE_PINS.json").read_text("utf-8"))
    lock = pins["public_lock"]
    require(lock["issue_number"] == 369, "public issue lock mismatch")
    require(lock["branch"] == "notes/c-golden-ame-j-rigidity-1-n", "branch lock mismatch")
    authority = pins["public_canon_v46"]
    require(authority["activation_commit"] == ACTIVATION_COMMIT, "activation pin mismatch")
    require(authority["content_commit"] == CONTENT_COMMIT, "content pin mismatch")
    require(authority["canon_bytes"] == CANON_BYTES, "manifest Canon bytes mismatch")
    require(authority["canon_sha256"] == CANON_SHA256, "manifest Canon hash mismatch")

    files = pins["upstream"]["files"]
    for name, frozen in (("AME46_ORIGINAL.m", ORIGINAL_PIN), ("block944.m", BLOCK944_PIN)):
        for key in ("bytes", "sha256", "git_blob_sha1"):
            require(files[name][key] == frozen[key], f"manifest source pin mismatch: {name}:{key}")
    seal = pins["prelock_structural_freeze"]
    require(seal["coordinate_records_including_xy"] == int(EQUATION_COORDINATES), "manifest record count mismatch")
    require(seal["nonzero_coordinate_records_including_xy"] == int(ACTIVE_EQUATIONS), "manifest active count mismatch")
    require(seal["serialization_bytes"] == int(SERIALIZATION_BYTES), "manifest serialization bytes mismatch")
    require(seal["serialization_sha256"] == SERIALIZATION_SHA256, "manifest serialization hash mismatch")


def import_signature(tree: ast.Module):
    output = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            output.append(
                ("import", None, 0, tuple((alias.name, alias.asname) for alias in node.names))
            )
        elif isinstance(node, ast.ImportFrom):
            output.append(
                (
                    "from",
                    node.module,
                    node.level,
                    tuple((alias.name, alias.asname) for alias in node.names),
                )
            )
    return tuple(output)


def call_name(call: ast.Call) -> str | None:
    if isinstance(call.func, ast.Name):
        return call.func.id
    if isinstance(call.func, ast.Attribute):
        return call.func.attr
    return None


def verify_raw_firewall(package: Path) -> int:
    raw_path = package / "golden_symbolic.py"
    raw = raw_path.read_bytes()
    require(sha256_bytes(raw) == RAW_MODULE_SHA256, "raw-module hash mismatch")
    tree = ast.parse(raw.decode("utf-8"), filename=raw_path.name)
    require(import_signature(tree) == EXPECTED_RAW_IMPORTS, "raw-module import firewall mismatch")

    dynamic_calls = {
        name
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        for name in (call_name(node),)
        if name in FORBIDDEN_DYNAMIC_CALLS
    }
    require(not dynamic_calls, f"forbidden raw dynamic calls: {sorted(dynamic_calls)}")

    semantic_names = {
        node.id.lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Name) and node.id.lower() in FORBIDDEN_SEMANTIC_NAMES
    }
    semantic_names |= {
        node.attr.lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.Attribute) and node.attr.lower() in FORBIDDEN_SEMANTIC_NAMES
    }
    require(not semantic_names, f"forbidden raw semantic names: {sorted(semantic_names)}")

    direct = next(
        (
            node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == "construct_a_direct"
        ),
        None,
    )
    require(direct is not None, "raw direct constructor missing")
    require(not any(isinstance(node, ast.BinOp) for node in ast.walk(direct)), "source-value arithmetic entered direct parser")
    direct_calls = {
        name
        for node in ast.walk(direct)
        if isinstance(node, ast.Call)
        for name in (call_name(node),)
        if name is not None
    }
    allowed_direct_calls = {
        "AssertionError",
        "ValueError",
        "_parse_literal_rows",
        "decode",
        "divmod",
        "findall",
        "int",
        "len",
        "range",
        "str",
        "verify_pin",
    }
    require(direct_calls <= allowed_direct_calls, f"direct-parser call firewall mismatch: {sorted(direct_calls - allowed_direct_calls)}")
    return len(EXPECTED_RAW_IMPORTS)


def run_child(package: Path, arguments: list[str], expected_name: str, expected_hash: str) -> bytes:
    expected = (package / expected_name).read_bytes()
    require(sha256_bytes(expected) == expected_hash, f"expected transcript hash mismatch: {expected_name}")
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    completed = subprocess.run(
        [sys.executable, "-B", *arguments],
        cwd=package,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
        check=False,
    )
    require(completed.returncode == 0, f"child exit mismatch: {arguments[0]}")
    require(completed.stderr == b"", f"child stderr not empty: {arguments[0]}")
    require(completed.stdout == expected, f"child stdout mismatch: {expected_name}")
    return completed.stdout


def parse_key_values(transcript: bytes) -> dict[str, str]:
    output = {}
    for line in transcript.decode("utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            output[key] = value
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--original", required=True, type=Path)
    parser.add_argument("--block944", required=True, type=Path)
    args = parser.parse_args()

    package = Path(__file__).resolve().parent
    repo_root = package.parents[1]
    require((repo_root / "STATUS.md").is_file(), "repository root not found")

    verify_authority(repo_root, package)
    original = verify_bytes(args.original, ORIGINAL_PIN, git_blob=True)
    block944 = verify_bytes(args.block944, BLOCK944_PIN, git_blob=True)
    require(original != block944, "source paths unexpectedly identical")

    raw_import_count = verify_raw_firewall(package)
    require(sha256_bytes((package / "prelock_audit.py").read_bytes()) == PRELOCK_AUDIT_SHA256, "prelock-audit hash mismatch")
    require(sha256_bytes((package / "cas_selftest.py").read_bytes()) == CAS_SELFTEST_SHA256, "CAS-selftest hash mismatch")

    prelock = run_child(
        package,
        ["prelock_audit.py", str(args.original.resolve()), "--block944", str(args.block944.resolve())],
        "PRELOCK_EXPECTED.txt",
        PRELOCK_EXPECTED_SHA256,
    )
    values = parse_key_values(prelock)
    required_values = {
        "EQUATION_COORDINATES_INCLUDING_XY": EQUATION_COORDINATES,
        "ACTIVE_EQUATIONS_INCLUDING_XY": ACTIVE_EQUATIONS,
        "EQUATION_SERIALIZATION_BYTES": SERIALIZATION_BYTES,
        "EQUATION_SERIALIZATION_SHA256": SERIALIZATION_SHA256,
        "GROEBNER": "NOT_RUN",
        "RADICAL": "NOT_RUN",
        "ELIMINATION": "NOT_RUN",
        "SATURATION": "NOT_RUN",
        "TARGET_RELATION_TESTS": "NOT_RUN",
        "STATUS": "PASS",
    }
    for key, expected in required_values.items():
        require(values.get(key) == expected, f"prelock mandatory value mismatch: {key}")

    cas_output = run_child(
        package,
        ["cas_selftest.py"],
        "CAS_SELFTEST_EXPECTED.txt",
        CAS_EXPECTED_SHA256,
    )
    require(cas_output.endswith(b"SUMMARY 7/7 PASS\n"), "CAS self-test summary mismatch")

    print("GOLDEN_RIGIDITY_PREREG_VERIFY_V1")
    print(f"PASS AUTHORITY canon_bytes={CANON_BYTES} canon_sha256={CANON_SHA256}")
    print(f"PASS SOURCES original_sha256={ORIGINAL_PIN['sha256']} block944_sha256={BLOCK944_PIN['sha256']}")
    print(f"PASS RAW_FIREWALL imports={raw_import_count} ast=PASS raw_sha256={RAW_MODULE_SHA256}")
    print(
        "PASS PRELOCK "
        f"records={EQUATION_COORDINATES} active={ACTIVE_EQUATIONS} "
        f"serialization_bytes={SERIALIZATION_BYTES} serialization_sha256={SERIALIZATION_SHA256}"
    )
    print("PASS TOY_CAS_SELFTEST summary=7/7")
    print("PASS TARGET_STAGE=NOT_CALLED")
    print("SUMMARY 6/6 PASS")


if __name__ == "__main__":
    main()
