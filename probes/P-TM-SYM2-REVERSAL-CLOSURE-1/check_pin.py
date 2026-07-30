#!/usr/bin/env python3
# P-TM-SYM2-REVERSAL-CLOSURE-1 static pin gate.
#
# Run from the repository root with no arguments:
#   python3 probes/P-TM-SYM2-REVERSAL-CLOSURE-1/check_pin.py
#
# Reads bytes and parses source only. It must not and does not import,
# compile to executable form, or execute verify.py, and it decides no
# scientific quantity. Exit 0 with deterministic stdout means the pin
# inventory is statically well-formed; any defect exits 1.
import ast
import hashlib
import os
import re
import sys

PROBE_DIR = "probes/P-TM-SYM2-REVERSAL-CLOSURE-1/"
INVENTORY = [
    "PREREG.md",
    "verify.py",
    "check_pin.py",
    "SOURCE-PREDEFINITION.md",
    "SOURCE-MEASURE1-EXPECTED.txt",
    "SOURCE-SEMILINEAR-EXPECTED.txt",
]
SOURCE_SHA = {
    "SOURCE-PREDEFINITION.md":
        "557b27c65870f25903b08c8830bfd55c0e91f5caa1221d6f2fedb2ff8e90add1",
    "SOURCE-MEASURE1-EXPECTED.txt":
        "395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f",
    "SOURCE-SEMILINEAR-EXPECTED.txt":
        "47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19",
}
ALLOWED_IMPORTS = {"hashlib", "itertools", "re", "sys", "fractions"}

failures = []


def gate(label, ok):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        failures.append(label)


data = {}
try:
    with os.scandir(PROBE_DIR) as entries:
        disk_entries = list(entries)
    data = {name: open(PROBE_DIR + name, "rb").read()
            for name in INVENTORY}
except OSError:
    disk_entries = []
    data = {}
inventory_exact = (
    sorted(e.name for e in disk_entries) == sorted(INVENTORY)
    and all(e.is_file(follow_symlinks=False) for e in disk_entries)
    and len(data) == len(INVENTORY)
)
gate("G1 pin inventory is exactly the six declared regular files",
     inventory_exact)
if not inventory_exact:
    print("RESULT: FAIL")
    sys.exit(1)

def ascii_lf(b):
    try:
        b.decode("ascii", "strict")
    except UnicodeDecodeError:
        return False
    return b"\r" not in b and b.endswith(b"\n")


gate("G2 all pin files are ASCII, LF-only, and final-LF terminated",
     all(ascii_lf(b) for b in data.values()))

gate("G3 the three source snapshots are byte-identical to their "
     "pinned SHA-256",
     all(hashlib.sha256(data[n]).hexdigest() == h
         for n, h in SOURCE_SHA.items()))

prereg = data["PREREG.md"].decode("ascii")
vsha = hashlib.sha256(data["verify.py"]).hexdigest()
m = re.search(r"verify\.py SHA-256:\s+([0-9a-f]{64})", prereg)
gate("G4 PREREG resolves owner fields and verifier SHA-256, matching "
     "the pinned verify.py bytes",
     m is not None and m.group(1) == vsha and "XXXX" not in prereg
     and "OWNER-FILL" not in prereg)

tree = ast.parse(data["verify.py"].decode("ascii"))
imports = set()
floats = 0
argv_use = 0
dynamic_code = 0
static_strings = {}


def static_string(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return static_strings.get(node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = static_string(node.left)
        right = static_string(node.right)
        if left is not None and right is not None:
            return left + right
    return None


for statement in tree.body:
    if isinstance(statement, ast.Assign) and len(statement.targets) == 1:
        target = statement.targets[0]
        value = static_string(statement.value)
        if isinstance(target, ast.Name) and value is not None:
            static_strings[target.id] = value

allowed_reads = {
    PROBE_DIR + "SOURCE-MEASURE1-EXPECTED.txt",
    PROBE_DIR + "SOURCE-SEMILINEAR-EXPECTED.txt",
}
open_paths = []
bad_open = 0
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for a in node.names:
            imports.add(a.name.split(".")[0])
    elif isinstance(node, ast.ImportFrom):
        imports.add((node.module or "").split(".")[0])
    elif isinstance(node, ast.Constant) and isinstance(node.value, float):
        floats += 1
    elif isinstance(node, ast.Attribute) and node.attr == "argv":
        argv_use += 1
    elif isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name) and f.id in {
                "__import__", "compile", "eval", "exec"}:
            dynamic_code += 1
        if isinstance(f, ast.Name) and f.id == "open":
            path = static_string(node.args[0]) if node.args else None
            mode = static_string(node.args[1]) if len(node.args) > 1 else "r"
            for keyword in node.keywords:
                if keyword.arg == "mode":
                    mode = static_string(keyword.value)
            open_paths.append(path)
            if path not in allowed_reads or mode != "rb":
                bad_open += 1
gate("G5 verify.py uses only the frozen imports and no dynamic code",
     imports <= ALLOWED_IMPORTS and dynamic_code == 0)
gate("G6 verify.py contains no float constant", floats == 0)
gate("G7 verify.py reads no process arguments", argv_use == 0)
gate("G8 verify.py has exactly the two resolved probe-local rb reads",
     bad_open == 0 and sorted(open_paths) == sorted(allowed_reads))

src = data["verify.py"].decode("ascii")
expected_names = {node.id for node in ast.walk(tree)
                  if isinstance(node, ast.Name)
                  and node.id.upper().startswith("EXPECTED")}
result_line = re.compile(
    r"^(?:ROUTE|TRANSLATION_N|TRANSLATION_R|TRANSLATION_NR|"
    r"TRANSPORT_N|TRANSPORT_R|TRANSPORT_NR|EXTENDED_ORBIT_COUNT|"
    r"EXTENDED_ORBIT_SIZES):\s+.+$")
literal_results = [node.value for node in ast.walk(tree)
                   if isinstance(node, ast.Constant)
                   and isinstance(node.value, str)
                   and result_line.match(node.value)
                   and "%" not in node.value and "{" not in node.value]
gate("G9 verify.py carries both route grammars with no EXPECTED_* "
     "identifier or populated literal scientific-result line",
     "REVERSAL-TOGGLE" in src and "REVERSAL-SILENT" in src
     and not expected_names and not literal_results)

if failures:
    print("RESULT: FAIL (%d)" % len(failures))
    sys.exit(1)
print("RESULT: PASS (static pin gate green)")
