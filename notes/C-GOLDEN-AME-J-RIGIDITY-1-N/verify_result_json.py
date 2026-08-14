#!/usr/bin/env python3
"""Standard-library cross-check of the canonical final result JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


if sys.flags.optimize:
    raise SystemExit("refusing optimized Python: exact verifier requires active assertions")


PACKAGE = Path(__file__).resolve().parent
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
BLOCK_SHA256 = "af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649"
GB_SHA256 = "79db9845615cea94540211a383e49471fe2a92cd02388a7caac92d20f9d76526"
RAW_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(path: Path):
    data = path.read_bytes()
    value = json.loads(data)
    encoded = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")
    assert data == encoded
    return value, data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--block944", required=True, type=Path)
    args = parser.parse_args()

    source_bytes = args.source.read_bytes()
    block_bytes = args.block944.read_bytes()
    assert len(source_bytes) == 8515 and sha256(source_bytes) == SOURCE_SHA256
    assert len(block_bytes) == 8234 and sha256(block_bytes) == BLOCK_SHA256

    result, result_bytes = canonical_json(PACKAGE / "RESULT.json")
    assert result["format"] == "GOLDEN_RIGIDITY_RESULT_V1"
    assert result["public_lock"] == {
        "commit": "bc06e77c86c74dfe1b7b988614a33b5130b877f7",
        "issue": 369,
        "tree": "0f8057a815efee04a1ed47b81336765fa237e84b",
    }
    assert result["scoped_verdict"] == "EXACT_J_RIGID_UP_TO_CONJUGATION"
    assert result["controls"] == "NC0_NC5_ALL_PASS"

    for record in result["artifacts"].values():
        data = (PACKAGE / record["file"]).read_bytes()
        assert len(data) == record["bytes"]
        assert sha256(data) == record["sha256"]

    gb_bytes = (PACKAGE / "FROZEN_ORDER_GB_CERT.json").read_bytes()
    assert len(gb_bytes) == 276630 and sha256(gb_bytes) == GB_SHA256
    gb = json.loads(gb_bytes)
    assert gb["format"] == "GOLDEN_RIGIDITY_FROZEN_ORDER_TRACKED_GB_V1"
    assert gb["ring"] == {
        "domain": "QQ", "order": "lex",
        "variables": ["t", "a", "b", "c", "y", "x"],
    }
    assert len(gb["inputs"]) == 363 and len(gb["basis"]) == 6

    blind, _ = canonical_json(PACKAGE / "TARGET_BLIND_RESULT.json")
    real, _ = canonical_json(PACKAGE / "REAL_POSITIVE_CERT.json")
    target, _ = canonical_json(PACKAGE / "TARGET_EVAL_CERT.json")
    controls, _ = canonical_json(PACKAGE / "CONTROLS_COLUMN_CERT.json")
    evidence, _ = canonical_json(PACKAGE / "EVIDENCE_G3_CONTROLS.json")

    assert blind["target_loaded"] is False
    assert blind["basis_certificate"]["sha256"] == GB_SHA256
    assert blind["raw"]["serialization_sha256"] == RAW_SHA256
    assert blind["classification"]["complex_dimension"] == 0
    assert blind["classification"]["degree"] == 16
    assert blind["classification"]["radical"] is True
    assert blind["classification"]["prime_over_Q"] is True

    assert real["basis_certificate"]["sha256"] == GB_SHA256
    assert real["physical_real_cardinality"] == 16
    assert real["positive_cardinality"] == 2
    assert real["conjugation_pairing"].startswith("epsilon -> -epsilon")

    assert target["blind_basis"]["sha256"] == GB_SHA256
    assert target["complex_radical_mask"] == "111111"
    assert target["positive_universal_mask"] == "111111"
    assert target["positive_cardinality"] == 2
    assert target["normal_forms"] == [[]] * 6
    assert target["field_readback"]["status"] == "PASS"
    assert "Q(zeta_40)" in target["field_readback"]["conclusion"]

    assert all(controls[name]["status"] == "PASS" for name in (
        "NC0", "NC1", "NC2", "NC3", "NC4", "NC5"
    ))
    assert controls["raw_ideal"]["saturated_equals_raw"] is True
    assert controls["NC5"]["column_serialization_sha256"] == evidence[
        "column_serialization_sha256"
    ]
    assert evidence["raw_sha256"] == RAW_SHA256

    exact = result["exact_result"]
    assert exact == {
        "complex_dimension": blind["classification"]["complex_dimension"],
        "complex_radical_mask": target["complex_radical_mask"],
        "degree": blind["classification"]["degree"],
        "field_readback": "Q(zeta_40)",
        "physical_real_cardinality": real["physical_real_cardinality"],
        "positive_cardinality": real["positive_cardinality"],
        "positive_universal_mask": target["positive_universal_mask"],
        "prime_over_Q": blind["classification"]["prime_over_Q"],
        "radical": blind["classification"]["radical"],
        "raw_equals_saturated": controls["raw_ideal"]["saturated_equals_raw"],
        "surviving_ambiguity": "complex_conjugation",
    }

    assert result["source"] == {
        "block944_sha256": BLOCK_SHA256,
        "builder_sha256": "b26844a99db5ff9baf4ed7493ed8c9c7aea28a561c8eeadb2c70fdc77530383c",
        "original_sha256": SOURCE_SHA256,
        "raw_serialization_sha256": RAW_SHA256,
    }
    assert result["independent_replay"]["primary_stdlib"] == {
        "expected_stdout_sha256": "e840cf4eb52d0ec236d25f3666c9b0965235c01e54ad592123eeddb0ba92c043",
        "status": "PASS",
    }
    assert result["independent_replay"]["optional_sympy"] == {
        "expected_stdout_sha256": "5cb4c9c756e25c69bcbb7effe88fde744dbac15e79bd1d7244a5acdcb8405e60",
        "status": "PASS",
    }
    assert result["independent_replay"]["g3_controls"] == {
        "expected_stdout_sha256": "becb3691bc82394519e3067602aa067923aebb977780bfb326f824b3446dfe03",
        "status": "PASS",
    }

    print("GOLDEN_RIGIDITY_RESULT_JSON_VERIFY_V1")
    print(f"PASS SOURCE original={SOURCE_SHA256} block944={BLOCK_SHA256}")
    print(f"PASS RESULT canonical_bytes={len(result_bytes)} sha256={sha256(result_bytes)}")
    print("PASS ARTIFACTS count=7 hashes=YES canonical_json=YES")
    print("PASS CROSSCHECK dimension=0 degree=16 radical=YES prime=YES raw_equals_saturated=YES")
    print("PASS PHYSICAL real=16 positive=2 masks=111111/111111 conjugation_pair=YES")
    print("PASS FIELD Q(zeta_40) controls=NC0_NC5_ALL_PASS independent_replay=PASS")
    print("SUMMARY 6/6 PASS verdict=EXACT_J_RIGID_UP_TO_CONJUGATION")


if __name__ == "__main__":
    main()
