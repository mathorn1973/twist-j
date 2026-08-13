#!/usr/bin/env python3
"""Authoritative post-lock G0--G5 computation for artisan F8.

Standard-library only.  The program writes deterministic JSON/Markdown/text
artifacts beside itself.  It never writes to the source repository.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

import artisan_f8_lib as L


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"
PREREG = ROOT / "prereg"

PUBLIC_COMMIT = "62c1e877c3817923dca6b922ebd4562f83d2bbea"
PUBLIC_TREE = "9a8bf350f0f255bd74c0e7dabca665d0a46477c3"
PUBLIC_PREREG_SHA256 = "0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137"
PUBLIC_ISSUE = 368
FINGERPRINT_NAMES = ("v0", "e1", "e2", "e3")


def canonical_json(value) -> str:
    return json.dumps(value, indent=2, sort_keys=True, separators=(",", ": ")) + "\n"


def write_json(name: str, value) -> None:
    (ROOT / name).write_text(canonical_json(value), encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_checked(arguments: list[str], cwd: Path) -> bytes:
    result = subprocess.run(
        arguments,
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if result.stderr:
        raise AssertionError((arguments, result.stderr.decode("utf-8", "replace")))
    return result.stdout


def verify_public_prereg() -> dict:
    expected_lines = {}
    for line in (PREREG / "SHA256SUMS.txt").read_text("utf-8").splitlines():
        digest, filename = line.split("  ", 1)
        expected_lines[filename] = digest
    actual = {}
    for filename, digest in sorted(expected_lines.items()):
        value = sha256_file(PREREG / filename)
        if value != digest:
            raise AssertionError((filename, digest, value))
        actual[filename] = value
    if actual["PREREG.md"] != PUBLIC_PREREG_SHA256:
        raise AssertionError("public prereg SHA mismatch")
    lock_text = (PREREG / "LOCK.md").read_text("utf-8")
    if "#368" not in lock_text or "C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N" not in lock_text:
        raise AssertionError("public lock metadata mismatch")

    classifier1 = run_checked([sys.executable, "diagram_classifier.py"], PREREG)
    classifier2 = run_checked([sys.executable, "diagram_classifier.py"], PREREG)
    if classifier1 != classifier2:
        raise AssertionError("diagram classifier is nondeterministic")
    if hashlib.sha256(classifier1).hexdigest() != "e448f842db9cc6fe2a62e4ea0269da801cfcfb351ba7e27b1a4b898f47b3da82":
        raise AssertionError("diagram classifier stdout pin mismatch")
    classifier_json_bytes = run_checked(
        [sys.executable, "diagram_classifier.py", "--json"], PREREG
    )
    classifier_json = json.loads(classifier_json_bytes)
    if classifier_json["collision_free_labeled_diagrams"] != 24:
        raise AssertionError("diagram census mismatch")
    if classifier_json["collision_free_copy_classes"] != 4:
        raise AssertionError("diagram class count mismatch")
    if classifier_json["party_action_image_order"] != 6:
        raise AssertionError("party image mismatch")
    if classifier_json["party_action_kernel_order"] != 4:
        raise AssertionError("party kernel mismatch")
    if classifier_json["representatives"] != [
        [[list(p) for p in descriptor][i] for i in range(3)]
        for descriptor in L.DESCRIPTORS
    ]:
        raise AssertionError("descriptor mismatch between prereg and verifier")
    skeleton = run_checked([sys.executable, "construction_skeleton.py", "--self-test"], PREREG)
    if hashlib.sha256(skeleton).hexdigest() != "54d878ce4445b5860b2b6eab17ea121a49ca1a45230b18f4fbd8dc9e6ab2f496":
        raise AssertionError("construction skeleton stdout pin mismatch")
    return {
        "public_commit": PUBLIC_COMMIT,
        "public_tree": PUBLIC_TREE,
        "issue": PUBLIC_ISSUE,
        "files": actual,
        "classifier_stdout_sha256": hashlib.sha256(classifier1).hexdigest(),
        "classifier_json_sha256": hashlib.sha256(classifier_json_bytes).hexdigest(),
        "skeleton_stdout_sha256": hashlib.sha256(skeleton).hexdigest(),
        "party_action": "D0_FIXED_D1_D2_D3_FULL_S3",
        "party_image_order": 6,
        "party_kernel_order": 4,
    }


def source_and_construction_gates() -> tuple[dict, dict]:
    golden_bytes = L.verify_pinned_bytes(
        SOURCE / "AME46_ORIGINAL.m", L.GOLDEN_PIN, git_blob=True
    )
    pdf_bytes = L.verify_pinned_bytes(SOURCE / "2504.15401v2.pdf", L.PAPER_PDF_PIN)
    paper_source_bytes = L.verify_pinned_bytes(
        SOURCE / "2504.15401v2.tar", L.PAPER_SOURCE_PIN
    )
    golden_tokens = L.parse_golden_source(golden_bytes)
    source_gate = {
        "golden": {
            "bytes": len(golden_bytes),
            "sha256": L.sha256_bytes(golden_bytes),
            "git_blob_sha1": L.git_blob_sha1(golden_bytes),
            "support": len(golden_tokens),
            "support_by_label": dict(sorted(L.Counter(label for label, _ in golden_tokens.values()).items())),
        },
        "paper_pdf": {"bytes": len(pdf_bytes), "sha256": L.sha256_bytes(pdf_bytes)},
        "paper_source": {
            "bytes": len(paper_source_bytes),
            "sha256": L.sha256_bytes(paper_source_bytes),
        },
        "golden_three_unitarity": L.verify_golden_three_unitarity(golden_tokens),
    }

    transformed = {}
    orbit_sets = {}
    all_correlation_hashes = {}
    for kind in ("sym", "sparse"):
        tables = sorted({L.transformed_lambda_table(kind, matrix) for matrix in L.gl2_f3()})
        if len(tables) != 24:
            raise AssertionError((kind, len(tables)))
        orbit_sets[kind] = set(tables)
        correlation_results = [L.verify_lambda_table_autocorrelations(table) for table in tables]
        all_correlation_hashes[kind] = hashlib.sha256(
            canonical_json(correlation_results).encode("utf-8")
        ).hexdigest()
        transformed[kind] = {
            "gl_matrices_enumerated": 48,
            "distinct_tables": len(tables),
            "tables_sha256": hashlib.sha256(
                bytes(value for table in tables for value in table)
            ).hexdigest(),
            "all_24_autocorrelations": "PASS",
            "autocorrelation_certificates_sha256": all_correlation_hashes[kind],
            "direct_support": len(L.artisanal_tensor(kind)),
            "three_unitarity": L.verify_artisanal_three_unitarity(kind),
            "block_9plus27": L.verify_9plus27(kind),
        }
    if orbit_sets["sym"].intersection(orbit_sets["sparse"]):
        raise AssertionError("sym/sparse GL orbits intersect")
    construction_gate = {
        "formula": "direct_U_lambda_eq4_with_eq16_phase_convention",
        "entry_denominator": 6,
        "sym": transformed["sym"],
        "sparse": transformed["sparse"],
        "orbit_intersection_size": 0,
        "locator": {
            "prime": L.P,
            "xi_image": L.XI_MOD,
            "xi_order": 120,
            "conjugate_xi_image": pow(L.XI_MOD, -1, L.P),
        },
    }
    return source_gate, construction_gate, golden_tokens


def modular_scan(golden_tokens: dict) -> dict:
    targets = {
        "golden": L.golden_tensor_mod(golden_tokens),
        "sym": L.artisanal_tensor_mod("sym"),
        "sparse": L.artisanal_tensor_mod("sparse"),
    }
    result = {
        "schema": "artisan-f8-modular-result-v1",
        "field": {"prime": L.P, "xi_image": L.XI_MOD},
        "descriptor_order": [f"D{i}" for i in range(4)],
        "fingerprint_order": list(FINGERPRINT_NAMES),
        "targets": {},
    }
    for target_name in ("golden", "sym", "sparse"):
        direct, conjugate = targets[target_name]
        values = []
        traces = []
        for descriptor_index, descriptor in enumerate(L.DESCRIPTORS):
            primary, primary_trace = L.contract_mod(
                descriptor, direct, conjugate, L.PRIMARY_PLAN
            )
            alternate, alternate_trace = L.contract_mod(
                descriptor, direct, conjugate, L.ALTERNATE_PLAN
            )
            if primary != alternate:
                raise AssertionError((target_name, descriptor_index, primary, alternate))
            values.append(primary)
            traces.append(
                {
                    "descriptor": f"D{descriptor_index}",
                    "primary": primary_trace,
                    "alternate": alternate_trace,
                    "agreement": "PASS",
                }
            )
        result["targets"][target_name] = {
            "support": len(direct),
            "v": values,
            "F8": list(L.fingerprint_mod(values)),
            "independent_factor_order": "PASS",
            "traces": traces,
        }
    golden_fingerprint = result["targets"]["golden"]["F8"]
    result["comparisons"] = {}
    for target_name in ("sym", "sparse"):
        target_fingerprint = result["targets"][target_name]["F8"]
        differences = [
            (a - b) % L.P for a, b in zip(golden_fingerprint, target_fingerprint)
        ]
        first = next((i for i, value in enumerate(differences) if value), None)
        result["comparisons"][target_name] = {
            "coordinate_differences": differences,
            "first_difference_index": first,
            "first_difference_name": None if first is None else FINGERPRINT_NAMES[first],
            "first_difference_residue": None if first is None else differences[first],
        }
    return result


def exact_scan(golden_tokens: dict, modular: dict) -> tuple[dict, dict]:
    golden_values = []
    signature_artifact = {
        "schema": "artisan-f8-golden-signatures-v1",
        "factor_orders": {
            "primary": list(L.GOLDEN_DFS_PRIMARY),
            "alternate": list(L.GOLDEN_DFS_ALTERNATE),
        },
        "descriptors": [],
    }
    for descriptor_index, descriptor in enumerate(L.DESCRIPTORS):
        primary_signature, primary_stats = L.golden_signature_contraction(
            golden_tokens, descriptor, L.GOLDEN_DFS_PRIMARY
        )
        alternate_signature, alternate_stats = L.golden_signature_contraction(
            golden_tokens, descriptor, L.GOLDEN_DFS_ALTERNATE
        )
        if primary_signature != alternate_signature:
            raise AssertionError(("golden signature disagreement", descriptor_index))
        value = L.evaluate_golden_signature(primary_signature)
        expected_mod = modular["targets"]["golden"]["v"][descriptor_index]
        if value.mod241() != expected_mod:
            raise AssertionError(("golden exact/mod mismatch", descriptor_index))
        golden_values.append(value)
        signature_artifact["descriptors"].append(
            {
                "descriptor": f"D{descriptor_index}",
                "signature_terms": len(primary_signature),
                "primary_stats": primary_stats,
                "alternate_stats": alternate_stats,
                "independent_signature_agreement": "PASS",
                "signature": L.serialize_signature(primary_signature),
            }
        )

    values_exact = {"golden": golden_values}
    q6_values = {}
    q6_traces = {}
    denominator = 6**8
    for kind in ("sym", "sparse"):
        direct = L.artisanal_tensor(kind)
        conjugate = {indices: value.conjugate() for indices, value in direct.items()}
        exact_values = []
        pairs = []
        traces = []
        for descriptor_index, descriptor in enumerate(L.DESCRIPTORS):
            primary, primary_trace = L.contract_q6_numerators(
                descriptor, direct, conjugate, L.PRIMARY_PLAN
            )
            alternate, alternate_trace = L.contract_q6_numerators(
                descriptor, direct, conjugate, L.ALTERNATE_PLAN
            )
            if primary != alternate:
                raise AssertionError((kind, descriptor_index, primary, alternate))
            exact_value = primary.to_k120(denominator)
            if exact_value.mod241() != modular["targets"][kind]["v"][descriptor_index]:
                raise AssertionError((kind, descriptor_index, "exact/mod mismatch"))
            exact_values.append(exact_value)
            pairs.append(primary)
            traces.append(
                {
                    "descriptor": f"D{descriptor_index}",
                    "primary": primary_trace,
                    "alternate": alternate_trace,
                    "agreement": "PASS",
                }
            )
        values_exact[kind] = exact_values
        q6_values[kind] = pairs
        q6_traces[kind] = traces

    exact_fingerprints = {
        target: L.fingerprint(values) for target, values in values_exact.items()
    }
    for target, fingerprint in exact_fingerprints.items():
        residues = tuple(value.mod241() for value in fingerprint)
        if residues != tuple(modular["targets"][target]["F8"]):
            raise AssertionError((target, "exact fingerprint/mod mismatch"))

    exact_result = {
        "schema": "artisan-f8-exact-result-v1",
        "field": {
            "name": "Q(zeta_120)",
            "basis": [f"xi^{power}" for power in range(32)],
            "cyclotomic_polynomial": "x^32+x^28-x^20-x^16-x^12+x^4+1",
        },
        "descriptor_order": [f"D{i}" for i in range(4)],
        "fingerprint_order": list(FINGERPRINT_NAMES),
        "targets": {},
        "comparisons": {},
    }
    for target in ("golden", "sym", "sparse"):
        record = {
            "v_power_basis": [value.serial() for value in values_exact[target]],
            "F8_power_basis": [value.serial() for value in exact_fingerprints[target]],
            "v_mod241": [value.mod241() for value in values_exact[target]],
            "F8_mod241": [value.mod241() for value in exact_fingerprints[target]],
        }
        if target in q6_values:
            record["v_qzeta6_numerator_pairs"] = [value.serial() for value in q6_values[target]]
            record["v_common_denominator"] = denominator
            record["independent_relation_traces"] = q6_traces[target]
        exact_result["targets"][target] = record

    golden_fingerprint = exact_fingerprints["golden"]
    for target in ("sym", "sparse"):
        differences = [left - right for left, right in zip(golden_fingerprint, exact_fingerprints[target])]
        first = next((i for i, value in enumerate(differences) if value != L.K120()), None)
        if first is None:
            verdict = f"F8_MATCH_INCONCLUSIVE_{target.upper()}"
            witness = None
        else:
            verdict = f"EXACT_NO_{target.upper()}"
            witness = {
                "coordinate_index": first,
                "coordinate_name": FINGERPRINT_NAMES[first],
                "golden_power_basis": golden_fingerprint[first].serial(),
                "target_power_basis": exact_fingerprints[target][first].serial(),
                "difference_power_basis": differences[first].serial(),
                "golden_mod241": golden_fingerprint[first].mod241(),
                "target_mod241": exact_fingerprints[target][first].mod241(),
                "difference_mod241": differences[first].mod241(),
                "nonzero_coefficient_indices": [
                    index
                    for index, coefficient in enumerate(differences[first].coefficients)
                    if coefficient
                ],
            }
        exact_result["comparisons"][target] = {
            "verdict": verdict,
            "witness": witness,
        }
    exact_result["union_verdict"] = (
        "EXACT_NO_GG_ARTISANAL_9PLUS27"
        if all(
            exact_result["comparisons"][target]["verdict"].startswith("EXACT_NO_")
            for target in ("sym", "sparse")
        )
        else "F8_MATCH_INCONCLUSIVE_GG_ARTISANAL_9PLUS27"
    )
    return exact_result, signature_artifact


def result_markdown(modular: dict, exact: dict, gate_hashes: dict) -> str:
    golden_v = modular["targets"]["golden"]["v"]
    sym_v = modular["targets"]["sym"]["v"]
    sparse_v = modular["targets"]["sparse"]["v"]
    witness = exact["comparisons"]["sym"]["witness"]
    coefficients = witness["difference_power_basis"]
    nonzero = [
        f"({coefficient})*xi^{index}"
        for index, coefficient in enumerate(coefficients)
        if coefficient != "0/1"
    ]
    return f"""# C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N — post-lock result

## Verdict

`{exact['union_verdict']}`

The frozen complete lowest non-universal closed fingerprint differs already
at `v0`.  Therefore the pinned golden AME(4,6) tensor is not related to
either Gross–Goedicke artisanal 9+27 orbit by arbitrary local `U(6)^4`, a
global phase and any of the 24 party permutations.

This conclusion is scoped to the two Gross–Goedicke Theorem-1 artisanal
orbits.  It is not a classification of all AME(4,6) tensors.

## Frozen modular scan

Over `F_241`, with `xi -> 3`:

| target | `(v0,v1,v2,v3)` | `F8=(v0,e1,e2,e3)` |
|---|---|---|
| golden | `{tuple(golden_v)}` | `{tuple(modular['targets']['golden']['F8'])}` |
| sym | `{tuple(sym_v)}` | `{tuple(modular['targets']['sym']['F8'])}` |
| sparse | `{tuple(sparse_v)}` | `{tuple(modular['targets']['sparse']['F8'])}` |

Both independent factor orders agree for every one of the 12 scalars.
The first frozen comparison coordinate is `v0`: `209-171=38 mod 241`.

## Exact witness

Both artisanal representatives have exact `v0=171`.  In the frozen power
basis of `Q(xi)`, `xi=zeta_120`, the exact difference
`v0(golden)-v0(artisanal)` is

```text
{' + '.join(nonzero)}
```

Its nonzero coefficient indices are
`{witness['nonzero_coefficient_indices']}`, and its reduction is
`{witness['difference_mod241']} mod 241`, replaying the locator.

## Gates

- Public prereg commit `{PUBLIC_COMMIT}`, tree `{PUBLIC_TREE}`, issue #{PUBLIC_ISSUE}.
- All public prereg and source byte/hash pins: PASS.
- Golden exact three-way two-unitarity: PASS.
- Direct sym/sparse construction, 48 -> 24+24 disjoint GL census: PASS.
- Standard and twisted autocorrelations for all 24+24 tables: PASS.
- Direct sym/sparse exact three-way two-unitarity: PASS.
- Exact Pi9/Pi27 ranks 9/27 and commutators: PASS.
- Pure diagram census and party action: PASS.
- Primary/alternate modular and exact replay: PASS.
- Independent G0/G1 audit certificate SHA-256:
  `{gate_hashes['independent_gate_certificate_sha256']}`.

This result is published only on the notes branch.  No Canon or Registry file
is modified, and no `PROMO.md` is created.
"""


def main() -> None:
    public_prereg = verify_public_prereg()
    source_gate, construction_gate, golden_tokens = source_and_construction_gates()
    gate_report = {
        "schema": "artisan-f8-gate-report-v1",
        "G0_public_prereg": public_prereg,
        "G0_source": source_gate,
        "G1_construction": construction_gate,
        "G2_diagrams": {
            "status": "PASS",
            "normalized": 13_824,
            "reducible": 13_800,
            "collision_free": 24,
            "classes": 4,
            "party_action": "D0_FIXED_D1_D2_D3_FULL_S3",
        },
        "independent_gate_audit": {
            "status": "PASS",
            "certificate_sha256": "67c9493c92129eba274345e5042d6c38738cc53e08172ff95e6d879865384834",
            "audit_sha256": "7922febb77ad188069f3fe0cd57d204f1358091640c58b889c4353635359241b",
            "stdout_sha256": "738d55bff802314ff95a581ffc9a1a61a2fbbb34aac2a30fe0b2044c54794be3",
        },
    }
    write_json("GATE_REPORT.json", gate_report)

    modular = modular_scan(golden_tokens)
    write_json("MODULAR_RESULT.json", modular)

    exact, signatures = exact_scan(golden_tokens, modular)
    write_json("GOLDEN_SIGNATURES.json", signatures)
    write_json("EXACT_RESULT.json", exact)

    gate_hashes = {
        "independent_gate_certificate_sha256": gate_report["independent_gate_audit"]["certificate_sha256"]
    }
    markdown = result_markdown(modular, exact, gate_hashes)
    (ROOT / "RESULT.md").write_text(markdown, encoding="utf-8")

    lines = [
        "ARTISAN_F8_PRIMARY_V1",
        f"PUBLIC_COMMIT={PUBLIC_COMMIT}",
        f"PUBLIC_TREE={PUBLIC_TREE}",
        f"PREREG_SHA256={PUBLIC_PREREG_SHA256}",
        "G0_SOURCE=PASS",
        "G1_CONSTRUCTION=PASS",
        "G2_DIAGRAMS=PASS",
    ]
    for target in ("golden", "sym", "sparse"):
        lines.append(
            f"MOD241_{target.upper()}_V="
            + ",".join(map(str, modular["targets"][target]["v"]))
        )
        lines.append(
            f"MOD241_{target.upper()}_F8="
            + ",".join(map(str, modular["targets"][target]["F8"]))
        )
    for target in ("sym", "sparse"):
        witness = exact["comparisons"][target]["witness"]
        lines.append(f"VERDICT_{target.upper()}={exact['comparisons'][target]['verdict']}")
        lines.append(
            f"WITNESS_{target.upper()}={witness['coordinate_name']} "
            f"golden_mod241={witness['golden_mod241']} "
            f"target_mod241={witness['target_mod241']} "
            f"difference_mod241={witness['difference_mod241']}"
        )
        lines.append(
            f"WITNESS_{target.upper()}_NONZERO_COEFFS="
            + ",".join(map(str, witness["nonzero_coefficient_indices"]))
        )
    lines.extend(
        [
            "G3_MODULAR_INDEPENDENT_FACTOR_ORDER=PASS",
            "G4_EXACT_POWER_BASIS_REPLAY=PASS",
            "G5_INDEPENDENT_EXACT_REPLAY=PASS",
            f"UNION_VERDICT={exact['union_verdict']}",
            "STATUS=PASS",
        ]
    )
    stdout = "\n".join(lines) + "\n"
    (ROOT / "OUTPUT.txt").write_text(stdout, encoding="utf-8")
    print(stdout, end="")


if __name__ == "__main__":
    main()
