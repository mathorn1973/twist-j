#!/usr/bin/env python3
"""Full v61 evidence coverage for J-ODD-MOTOR-MEDIATED-BRIDGE [T]."""

from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
from runpy import run_path

ROOT = Path(__file__).resolve().parents[2]
ORIGINAL = ROOT / "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2/verify.py"
HARDENING = ROOT / "probes/P-J-ODD-MOTOR-BRIDGE-HARDENING-1/verify.py"
EXPECTED = {
    ORIGINAL: "78b5ae47fbede9449e0a7c706dc12e00661a0d3d63227c57ee6a35de84f3ef42",
    HARDENING: "682e1ccdbdc61597d9c08d594c9ea8a9c56b9364e419bc0c0e893c908977c2c8",
}


def stop(message):
    print("STOP", message)
    raise SystemExit(1)


def load(path):
    if not path.is_file():
        stop("MISSING FROZEN SOURCE " + path.relative_to(ROOT).as_posix())
    digest = sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED[path]:
        stop("SOURCE HASH MISMATCH " + path.relative_to(ROOT).as_posix())
    sink = StringIO()
    with redirect_stdout(sink):
        namespace = run_path(str(path), run_name="__coverage_input__")
    return namespace


old = load(ORIGINAL)
hard = load(HARDENING)

old_keys = ("tok", "bridge", "ctrl", "detok", "decomp", "sign", "triple")
hard_keys = ("carrier_integrity", "h1_ok", "h2_ok", "schur_tokens", "h3_ok")
if any(key not in old for key in old_keys) or any(key not in hard for key in hard_keys):
    stop("FROZEN SOURCE NAMESPACE DRIFT")

native = hard["carrier_integrity"] and hard["h1_ok"]
blocks = len(old["tok"]) == 5 and all(old["tok"]) and old["bridge"]
controls = old["ctrl"]
schur = len(hard["schur_tokens"]) == 5 and all(hard["schur_tokens"]) and hard["h2_ok"]
determinant = old["detok"]
sym2 = old["decomp"]
covariance = old["sign"]
trilinear = old["triple"]
all_ok = all((native, blocks, controls, schur, determinant, sym2, covariance, trilinear))

print("P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2")
print("MODE RESULT-EXPOSED EVIDENCE-MAINTENANCE")
print("LAYER L1 EXACT ARITHMETIC ONLY")
print("FROZEN SOURCE HASHES PASS")
print("G1 NATIVE TWO-SECTOR CRT RANKS 2 2", "PASS" if native else "FAIL")
print("G2-G3 AFFINE TOKEN BLOCK AND BRIDGE COVERAGE", "5/5" if blocks else "FAIL")
print("G4 RAW POWER AND EVEN CONTROLS", "PASS" if controls else "FAIL")
print("G5 EXPLICIT SCHUR TOKEN COVERAGE", "5/5" if schur else "FAIL")
print("G6 FULL DETERMINANT", "PASS" if determinant else "FAIL")
print("G7 SYM2 1+epsilon+2V END_DIM 6 AND HOM VANISHING", "PASS" if sym2 else "FAIL")
print("G8 QPLUS QMINUS COVARIANCE", "PASS" if covariance else "FAIL")
print("G8 TRILINEAR CENSUS", "PASS" if trilinear else "FAIL")
print("REPEATED 2V NONSELECTION BOUNDARY RETAINED")
print("H3 624-CHANNEL-BOX VALUE NOT CONSUMED")
print("PHYSICAL FREQUENCY MATERIAL BORN DECODER APPARATUS NOT CLAIMED")
print("DECISION", "COVERAGE-CERTIFIED" if all_ok else "ROUTE-FALSIFIED")
