#!/usr/bin/env python3
"""Exact correction audit for C-HOMOGENEOUS-RECORD-RETENTION-N (review items R1, R2).

PUBLIC, NON-CANONICAL. Design-exposed audit of exact identities stated in
notes/C-HOMOGENEOUS-RECORD-RETENTION-N/PROOF.md after correction; not a
registered probe. Contract: notes/C-HOMOGENEOUS-RECORD-RETENTION-N/CORRECTION_PROTOCOL.md.

The local law is taken from the pinned original verifier
reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py after its bytes and
SHA-256 are checked. That file and the original EXPECTED.txt are the only
files read. Python standard library only; no floating point, no network, no
randomness. Assertions guard every exact check.
"""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
ORIGINAL = ROOT / "reproduce" / "C-HOMOGENEOUS-RECORD-RETENTION-N"
ORIGINAL_VERIFY = ("verify.py", 33053,
                   "a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7")
ORIGINAL_EXPECTED = ("EXPECTED.txt", 1162,
                     "dccec8381f051efede09b61cea2b15c6735a883a4286e2d13c131bc2ea0164d3")
Z_REC = 100
STEPS = 4

CHECKS = {"n": 0}


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    CHECKS["n"] += 1


def load_original():
    for name, size, digest in (ORIGINAL_VERIFY, ORIGINAL_EXPECTED):
        data = (ORIGINAL / name).read_bytes()
        check(len(data) == size, f"original {name} byte count")
        check(hashlib.sha256(data).hexdigest() == digest, f"original {name} SHA-256")
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("retention_pin_24cc067", ORIGINAL / "verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ============================================================================
# GROUP 1: WRONG_MEMORY_BALANCE (R1)
# ============================================================================

MEMORY_INPUTS = (
    ("q=0", {(0, 0): (1, 0), (0, 1): (0, 1), (2, 1): (1, -1)}),
    ("q=1", {(1, 0): (2, 0), (1, 1): (1, 0)}),
    ("q=5/9", None),  # the entangled intermediate input PHI_TEST of the original
)


def free_crossing(o, z: int) -> dict:
    """Bank-1 pulse at x = z-1 (it hops across the receiver bond) with a distant
    object that cannot reach a contact within STEPS macrosteps."""
    s: dict = {}
    o.add_to(s, ("P", z - 20, 3, 0, z - 1, 0, 1, None, None), o.f_gauss(1, 0))
    return s


def audit_wrong_memory_balance(o, z: int = Z_REC, steps: int = STEPS) -> int:
    start = CHECKS["n"]
    left = o.carrier_left(z)
    spatial_inputs = (("mixed", o.initial_spatial(z)), ("free crossing", free_crossing(o, z)))
    summary = []
    for mem_name, phi in MEMORY_INPUTS:
        if phi is None:
            phi = o.PHI_TEST
        norm = sum(a * a + b * b for (a, b) in phi.values())
        off = sum(a * a + b * b for (k, _), (a, b) in phi.items() if k != 1)
        for sp_name, spatial in spatial_inputs:
            phys = o.calibrate(o.tensor_memory(spatial, phi), z)
            nonzero_current = 0
            unweighted_holds = 0
            for n in range(steps + 1):
                p = o.total_weight(phys, lambda k: k[-2] != 1)
                lam = o.total_weight(spatial, left)
                check(p == o.f_canon(o.f_int(lam, off)),
                      f"{mem_name} {sp_name} n={n}: p_n = (1-q) Lambda_n^2")
                if mem_name == "q=1":
                    check(o.f_iszero(p), f"{sp_name} n={n}: q=1 gives p_n = 0")
                if n == steps:
                    break
                inc = o.current_increment(phys, z)            # = 2 (L_{n+1} - 125^2 L_n)
                nxt = o.law_step(phys, z, True)
                lam_l0 = o.total_weight(phys, left)
                lam_l1 = o.total_weight(nxt, left)
                check(o.f_canon(o.f_int(o.f_sub(lam_l1, o.f_int(lam_l0, 15625)), 2)) == inc,
                      f"{mem_name} {sp_name} n={n}: carrier-left balance (2)")
                p1 = o.total_weight(nxt, lambda k: k[-2] != 1)
                dp2 = o.f_canon(o.f_int(o.f_sub(p1, o.f_int(p, 15625)), 2))
                check(o.f_canon(o.f_int(dp2, norm)) == o.f_canon(o.f_int(inc, off)),
                      f"{mem_name} {sp_name} n={n}: weighted wrong-memory balance (2')")
                if not o.f_iszero(inc):
                    nonzero_current += 1
                    if dp2 == inc:
                        unweighted_holds += 1
                phys = nxt
                spatial = o.law_step(spatial, z, False)
            check(nonzero_current > 0, f"{mem_name} {sp_name}: nonzero carrier current occurs")
            if mem_name == "q=0":
                check(unweighted_holds == nonzero_current,
                      f"{sp_name}: unweighted balance holds for q=0")
            else:
                check(unweighted_holds == 0,
                      f"{mem_name} {sp_name}: unweighted balance fails at every nonzero-current step")
            summary.append(f"{mem_name}/{sp_name}:{nonzero_current}")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 1 WRONG_MEMORY_BALANCE: {n} checks; steps={steps}; "
          f"nonzero-current steps {' '.join(summary)}; unweighted form holds only for q=0")
    return n


# ============================================================================
# GROUP 2: INPUT_CLASS (R1)
# ============================================================================

def audit_input_class(o, z: int = Z_REC, steps: int = STEPS) -> int:
    start = CHECKS["n"]
    left = o.carrier_left(z)
    chi_a: dict = {}
    chi_b: dict = {}
    o.add_to(chi_a, ("P", z - 30, 2, 1, z - 2, 0, 1, None, None), o.f_gauss(1, 0))
    o.add_to(chi_b, ("P", z - 40, -2, 2, z + 3, 1, 1, None, None), o.f_gauss(1, 0))
    theta: dict = {}
    for spatial, k, ref in ((chi_a, 0, 0), (chi_b, 1, 1)):
        for key, value in spatial.items():
            o.add_to(theta, key[:6] + (1, k, ref), value)
    phys = o.calibrate(theta, z)
    product_fails = 0
    for n in range(steps + 1):
        p = o.total_weight(phys, lambda k: k[-2] != 1)
        lam_a = o.total_weight(chi_a, left)
        lam_b = o.total_weight(chi_b, left)
        check(p == lam_a, f"n={n}: correlated input obeys Remark 1.3")
        # product formula misread with q = 1/2 from the memory marginal:
        # p =? (1 - q) (Lambda_A^2 + Lambda_B^2) with unit-norm components
        if o.f_canon(o.f_int(p, 2)) != o.f_canon(o.f_add(lam_a, lam_b)):
            product_fails += 1
        if n < steps:
            phys = o.law_step(phys, z, True)
            chi_a = o.law_step(chi_a, z, False)
            chi_b = o.law_step(chi_b, z, False)
    check(product_fails > 0, "product formula fails for a correlated input")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 2 INPUT_CLASS: {n} checks; correlated label-1 input follows Remark 1.3; "
          f"product formula fails at {product_fails} of {steps + 1} times")
    return n


# ============================================================================
# GROUP 3: COMMUTATOR_CONTROL (R2)
# ============================================================================

def audit_commutator_control(o, z: int = Z_REC) -> int:
    start = CHECKS["n"]
    e = {(z - 1, 0): 1}
    after = o.pulse_step_1d(e)                                   # V 1_{x<z} e = V e
    cut_after = {k: v for k, v in after.items() if k[0] < z}     # 1_{x<z} V e
    check(after.get((z, 1)) == 2, "bank-1 pulse at z-1 reaches bank 2 at z (amplitude 2/5)")
    check(after != cut_after, "free pulse step does not commute with 1_{x<z}")
    n = CHECKS["n"] - start
    print(f"PASS GROUP 3 COMMUTATOR_CONTROL: {n} checks; [V, 1_(x<z)] != 0 witnessed at z-1 -> z")
    return n


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("Exact audit requires assertions enabled")
    sys.stdout.reconfigure(newline="\n")
    original = load_original()
    print(f"PASS GROUP 0 CUSTODY: {CHECKS['n']} checks; original verify.py and EXPECTED.txt "
          "match the 24cc067 pin")
    total = CHECKS["n"]
    total += audit_wrong_memory_balance(original)
    total += audit_input_class(original)
    total += audit_commutator_control(original)
    print("SCOPE: R1-R2 correction audit of exact identities only; Theorem 6 bound, "
          "original verifier and original stdout unchanged")
    print(f"AUDIT PASS C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N total_checks={total}")


if __name__ == "__main__":
    main()
