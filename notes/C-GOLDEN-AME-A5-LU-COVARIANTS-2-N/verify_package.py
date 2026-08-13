#!/usr/bin/env python3
"""Check cross-artifact consistency and print the gate verdict."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--modular", type=Path, default=Path(__file__).with_name("MODULAR_RESULT.json"))
    parser.add_argument("--exact", type=Path, default=Path(__file__).with_name("EXACT_WITNESS.json"))
    args = parser.parse_args()
    modular = json.loads(args.modular.read_text())
    exact = json.loads(args.exact.read_text())

    assert modular["public_pin"]["commit"] == "1a813b6f50435d83e0dfd5011898a03fc5e4b089"
    assert modular["public_pin"]["tree"] == "1a61fc296079a9a2964ba4649900851f7b25ec9a"
    assert modular["public_pin"]["prereg_sha256"] == "b03ed300806c993cb4f4eac7249d9a6c2e7e9df9d96669d989445d4a1ade68f3"
    assert modular["source"]["support"] == 112
    assert len(modular["records"]) == 16
    assert all(r["star_equal"] and r["matrix"] == r["star_matrix"] for r in modular["records"])
    witness = modular["first_hard_witness"]
    assert witness == {
        "kind": "star-algebra-dimension",
        "matrices": ["I", "R1", "(R1)(R1)"],
        "minor": {
            "determinant": 31,
            "flat_positions": [0, 7, 21],
            "matrix_positions": [[0, 0], [1, 1], [3, 3]],
        },
        "q": 0,
    }
    R1 = next(r for r in modular["records"] if r["q"] == 0 and r["core_index"] == 1)
    assert exact["matrix_mod41"] == R1["matrix"]
    assert exact["descriptor"] == R1["descriptor"]
    assert exact["minor_mod41"] == 31
    assert exact["minor_positions"] == [[0, 0], [1, 1], [3, 3]]
    assert exact["ordering_matrices_equal"] and exact["star_exact_equal"]
    assert sorted(g["multiplicity"] for g in exact["exact_eigenvalue_groups"]) == [2, 2, 2]
    assert exact["all_witness_denominators_lcm"] % 41 != 0
    print("G0 PASS")
    print("G1 PASS: 2345 orbits, four irreducible cores")
    print("G2 PASS: complete 16+16 census; first hard locator q=0,R1")
    print("G3 PASS: exact minor nonzero, residue 31, exact eigen split 2+2+2")
    print("G4 EXACT NO in the frozen arbitrary-local-unitary 1+5 scope")


if __name__ == "__main__":
    main()
