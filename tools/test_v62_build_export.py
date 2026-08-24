#!/usr/bin/env python3
"""Temporary non-canonical builder/exporter for the frozen Public Canon v62 maintenance fold."""

from __future__ import annotations

import base64
import csv
import hashlib
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

CLAIM = "J-ODD-MOTOR-MEDIATED-BRIDGE"
OLD_PATH = "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2"
OLD_HASH = "03db973566ae068b5ed8eb65f4e79ae13af398ac067f325c26a25c1553bf636b"
NEW_PATH = "probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2"
NEW_HASH = "f6b2ca8bf117ee709eba29356b4e5ad61e60801c1975e5405cab1fefbbaa624b"
SCOPE_HASH = "a1f5d43376bafced23478edd0857dfc2c2d1566ee960db32e8d67d493191ad9a"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rewrite_tsv(path: Path, key: str, mutate) -> None:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = tuple(reader.fieldnames or ())
        rows = list(reader)
    matches = [row for row in rows if row[key] == CLAIM]
    if len(matches) != 1:
        raise AssertionError(f"{path.name}: target rows={len(matches)}")
    mutate(matches[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def patch_status_separation(work: Path) -> None:
    path = work / "reproduce/status-separation/verify.py"
    text = path.read_text(encoding="utf-8")
    replacements = {
        '"registry and companion-ledger counts match Public Canon v61"':
            '"registry and companion-ledger counts match Public Canon v62"',
        "and len(history) == 845": "and len(history) == 846",
        f'"T", "THEOREM", "{OLD_PATH}",\n            "{OLD_HASH}",':
            f'"T", "THEOREM", "{NEW_PATH}",\n            "{NEW_HASH}",',
        'and row["evidence_location"] == v61_rows[claim][2]\n'
        '            and row["evidence_sha256"] == v61_rows[claim][3]':
            'and row["evidence_location"] == (\n'
            f'                "{OLD_PATH}" if claim == "{CLAIM}"\n'
            '                else v61_rows[claim][2]\n'
            '            )\n'
            '            and row["evidence_sha256"] == (\n'
            f'                "{OLD_HASH}" if claim == "{CLAIM}"\n'
            '                else v61_rows[claim][3]\n'
            '            )',
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise AssertionError(f"status-separation replacement count {text.count(old)} for {old[:60]}")
        text = text.replace(old, new, 1)

    anchor = "    fw_requires = {}\n"
    if text.count(anchor) != 1:
        raise AssertionError("status-separation V62 insertion anchor mismatch")
    block = f'''    v62_events = [
        row for row in history
        if row["claim_id"] == "{CLAIM}"
        and row["event_id"] == "CANON62-EVIDENCE-{CLAIM}"
    ]
    checks.append((
        "V62-MAINTENANCE",
        "v62 changes only the odd-motor evidence pointer and one lifecycle event while status, scope, dependencies, gates and science counts stay fixed",
        len(v62_events) == 1
        and has_status(index, "{CLAIM}", "T")
        and scope_sha256(index, "{CLAIM}") == "{SCOPE_HASH}"
        and index["{CLAIM}"]["evidence"] == "{NEW_PATH}"
        and evidence["{CLAIM}"]["evidence_id"] == "EV-{CLAIM}"
        and evidence["{CLAIM}"]["evidence_kind"] == "PUBLIC_PROBE"
        and evidence["{CLAIM}"]["location"] == "{NEW_PATH}"
        and evidence["{CLAIM}"]["sha256"] == "{NEW_HASH}"
        and evidence["{CLAIM}"]["hash_mode"] == "bundle-manifest-sha256-v1"
        and evidence["{CLAIM}"]["architecture_requirement"] == "two-architecture"
        and {{
            (row["depends_on"], row["relation"])
            for row in dependencies if row["item_id"] == "{CLAIM}"
        }} == {{
            ("AFFINE-READING-DEGREE-CENSUS", "REQUIRES"),
            ("AFFINE-QUADRATIC-FORM-UNIQUENESS", "REQUIRES"),
        }}
        and normative["{CLAIM}"]["status"] == "T"
        and normative["{CLAIM}"]["layer"] == "L1"
        and normative["{CLAIM}"]["gate_ids"] == ""
        and all(row["owner_item_id"] != "{CLAIM}" for row in gates.values())
        and v62_events[0]["event_sequence"] == "2"
        and v62_events[0]["event_date"] == "2026-08-24"
        and v62_events[0]["release"] == "canon-v62-candidate"
        and v62_events[0]["event_type"] == "EVIDENCE_CHANGE"
        and v62_events[0]["previous_status"] == "T"
        and v62_events[0]["new_status"] == "T"
        and v62_events[0]["scope_sha256"] == "{SCOPE_HASH}"
        and v62_events[0]["evidence_id"] == "EV-{CLAIM}"
        and v62_events[0]["evidence_location"] == "{NEW_PATH}"
        and v62_events[0]["evidence_sha256"] == "{NEW_HASH}"
    ))

'''
    text = text.replace(anchor, block + anchor, 1)
    path.write_text(text, encoding="utf-8", newline="\n")

    readme_path = work / "reproduce/status-separation/README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if "RESULT 54/54 ALL PASS" not in readme:
        raise AssertionError("status-separation README result anchor missing")
    readme = readme.replace("RESULT 54/54 ALL PASS", "RESULT 55/55 ALL PASS", 1)
    anchor = "The v61 count check reads the folded tree"
    if readme.count(anchor) != 1:
        raise AssertionError("status-separation README v61 anchor mismatch")
    paragraph = (
        "The v62 count check reads the maintenance tree (324 claims, 23 reproductions, "
        "11 gates). The V62-MAINTENANCE check requires the odd-motor theorem to retain "
        "its T status, exact scope, dependencies, layer and no-gate boundary while its "
        "single current evidence pointer moves to the completed two-architecture "
        "COVERAGE-2 bundle and HISTORY records exactly one sequence-2 EVIDENCE_CHANGE. "
        "No scientific count or status moves.\n\n"
    )
    readme = readme.replace(anchor, paragraph + anchor, 1)
    readme_path.write_text(readme, encoding="utf-8", newline="\n")

    result = subprocess.run(
        [sys.executable, "reproduce/status-separation/verify.py"],
        cwd=work, capture_output=True, check=False,
    )
    if result.returncode != 0 or result.stderr:
        raise AssertionError(
            "patched status-separation failed: "
            + result.stdout.decode("utf-8", "replace")
            + result.stderr.decode("utf-8", "replace")
        )
    (work / "reproduce/status-separation/EXPECTED.txt").write_bytes(result.stdout)


def build_candidate(root: Path, work: Path) -> tuple[list[str], str, int]:
    canon_dir = work / "canon"
    frontier_before = (canon_dir / "FRONTIER.md").read_bytes()
    status_counts_before = (canon_dir / "STATUS_COUNTS.tsv").read_bytes()
    deps_before = (canon_dir / "DEPENDENCIES.tsv").read_bytes()
    normative_before = (canon_dir / "NORMATIVE.tsv").read_bytes()
    gates_before = (canon_dir / "GATES.tsv").read_bytes()
    programs_before = (canon_dir / "FRONTIER_PROGRAMS.tsv").read_bytes()

    canon_path = canon_dir / "CANON.md"
    canon = canon_path.read_text(encoding="utf-8")
    head, sep, tail = canon.partition("\n---\n")
    if not sep or "# TWIST-J Public Canon v61" not in head:
        raise AssertionError("CANON current release title missing")
    head = head.replace("Public Canon v61", "Public Canon v62")
    old_sentence = f"Evidence is `{OLD_PATH}`."
    new_sentence = f"Evidence is `{NEW_PATH}`."
    if tail.count(old_sentence) != 1:
        raise AssertionError(f"CANON evidence sentence count={tail.count(old_sentence)}")
    tail = tail.replace(old_sentence, new_sentence, 1)
    canon_path.write_text(head + sep + tail, encoding="utf-8", newline="\n")

    def mutate_registry(row):
        if row["status"] != "T" or sha256_bytes(row["scope"].encode()) != SCOPE_HASH:
            raise AssertionError("REGISTRY target status/scope drift")
        if row["evidence"] != OLD_PATH:
            raise AssertionError("REGISTRY old evidence mismatch")
        row["evidence"] = NEW_PATH
    rewrite_tsv(canon_dir / "REGISTRY.tsv", "claim_id", mutate_registry)

    def mutate_evidence(row):
        if row["evidence_id"] != f"EV-{CLAIM}" or row["location"] != OLD_PATH or row["sha256"] != OLD_HASH:
            raise AssertionError("EVIDENCE target old row mismatch")
        if row["architecture_requirement"] != "two-architecture":
            raise AssertionError("EVIDENCE architecture drift")
        row["location"] = NEW_PATH
        row["sha256"] = NEW_HASH
    rewrite_tsv(canon_dir / "EVIDENCE.tsv", "claim_id", mutate_evidence)

    history_path = canon_dir / "HISTORY.tsv"
    history = history_path.read_text(encoding="utf-8")
    if f"CANON62-EVIDENCE-{CLAIM}\t" in history:
        raise AssertionError("v62 history event already exists")
    event = "\t".join((
        f"CANON62-EVIDENCE-{CLAIM}", "2", "2026-08-24", "canon-v62-candidate",
        CLAIM, "EVIDENCE_CHANGE", "T", "T", SCOPE_HASH, f"EV-{CLAIM}",
        NEW_PATH, NEW_HASH,
        "Public Canon v62 re-pins the unchanged T theorem to the complete RESULT-EXPOSED two-architecture coverage bundle; status, scope, falsifier, dependencies, gate surface and scientific content are unchanged, and the stopped predecessor supplies no evidence.",
    ))
    if history and not history.endswith("\n"):
        history += "\n"
    history_path.write_text(history + event + "\n", encoding="utf-8", newline="\n")

    changelog_path = canon_dir / "CHANGELOG.md"
    changelog = changelog_path.read_text(encoding="utf-8")
    header = "# Canon changelog (public series)\n\n"
    if not changelog.startswith(header):
        raise AssertionError("CHANGELOG header mismatch")
    v62 = f'''## Public Canon v62

<!-- BEGIN GENERATED CURRENT COUNTS -->
PLACEHOLDER
<!-- END GENERATED CURRENT COUNTS -->

Public Canon v62 is an integrity and evidence-maintenance release. It adds no
scientific claim, status move, scope move, dependency move, gate verdict,
physical dictionary or layer lift. Scientific registry counts are unchanged
from v61.

The released tree incorporates the already merged gate-contract maintenance
from PR #541. Every public gate row remains governed by the closed `gate_kind`
contract, including the explicit same-layer `OPEN_DECISION` case; no gate row
or verdict changes in this fold.

`J-ODD-MOTOR-MEDIATED-BRIDGE [T]` keeps its v61 status, scope, falsifier,
dependencies and nonselection boundary. Its single current evidence pointer is
re-pinned from `{OLD_PATH}` to
`{NEW_PATH}`, the complete RESULT-EXPOSED
two-architecture evidence-maintenance bundle. That bundle combines the frozen
G2-G8 implementation with the later native-sector and explicit-Schur
hardening, while explicitly not consuming the 624-channel-box H3 value.
The stopped COVERAGE-1 predecessor supplies no evidence.

The v62 ledger change is:

```text
claims: 324, unchanged,
T: 202, D: 43, C: 33, H: 3, O: 27, F: 16, unchanged,
live H/O: 30, unchanged,
normative items: 370, unchanged,
dependencies: 581, unchanged,
evidence rows: 324, unchanged,
gates: 11, unchanged,
history rows: 845 + 1 evidence-change event = 846,
two-architecture evidence: 240, unchanged,
reproduction witnesses: 23, unchanged.
```

'''
    changelog_path.write_text(
        header + v62 + changelog[len(header):], encoding="utf-8", newline="\n"
    )

    patch_status_separation(work)

    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work), "--apply"],
        cwd=work, check=True, text=True,
    )
    if (canon_dir / "FRONTIER.md").read_bytes() != frontier_before:
        raise AssertionError("FRONTIER changed although no live row moved")
    if (canon_dir / "STATUS_COUNTS.tsv").read_bytes() != status_counts_before:
        raise AssertionError("STATUS_COUNTS changed although science counts are frozen")
    for name, before in (
        ("DEPENDENCIES.tsv", deps_before), ("NORMATIVE.tsv", normative_before),
        ("GATES.tsv", gates_before), ("FRONTIER_PROGRAMS.tsv", programs_before),
    ):
        if (canon_dir / name).read_bytes() != before:
            raise AssertionError(f"{name} changed in maintenance fold")

    hashed = ("CANON.md", "CORE.md", "FRONTIER.md", "REGISTRY.tsv", "CHANGELOG.md")
    sums = []
    for name in hashed:
        sums.append(f"{sha256_bytes((canon_dir / name).read_bytes())}  canon/{name}\n")
    (canon_dir / "SHA256SUMS").write_text("".join(sums), encoding="utf-8", newline="\n")

    subprocess.run([sys.executable, "tools/check_policy.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_canon.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_ledger.py"], cwd=work, check=True, text=True)
    subprocess.run([sys.executable, "tools/check_gate_contract.py"], cwd=work, check=True, text=True)
    subprocess.run(
        [sys.executable, "tools/generate_canon_views.py", "--root", str(work),
         "--check-dir", str(canon_dir)],
        cwd=work, check=True, text=True,
    )
    result = subprocess.run(
        [sys.executable, "reproduce/status-separation/verify.py"],
        cwd=work, capture_output=True, check=False,
    )
    if result.returncode != 0 or result.stderr or result.stdout != (work / "reproduce/status-separation/EXPECTED.txt").read_bytes():
        raise AssertionError("status-separation exact replay mismatch")

    canon_hash = sha256_bytes(canon_path.read_bytes())
    canon_bytes = canon_path.stat().st_size
    export_files = [
        "canon/CANON.md", "canon/CORE.md", "canon/FRONTIER.md",
        "canon/REGISTRY.tsv", "canon/EVIDENCE.tsv", "canon/HISTORY.tsv",
        "canon/CHANGELOG.md", "canon/STATUS_COUNTS.tsv", "canon/SHA256SUMS",
        "reproduce/status-separation/verify.py",
        "reproduce/status-separation/EXPECTED.txt",
        "reproduce/status-separation/README.md",
    ]
    return export_files, canon_hash, canon_bytes


class V62BuildExportTest(unittest.TestCase):
    def test_build_validate_and_export(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as td:
            work = Path(td) / "repo"
            shutil.copytree(
                root, work,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
            )
            export_files, canon_hash, canon_bytes = build_candidate(root, work)
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for relative in export_files:
                    archive.writestr(relative, (work / relative).read_bytes())
            payload = buffer.getvalue()
            encoded = base64.b64encode(payload).decode("ascii")
            print(
                f"V62_BUILD_PASS canon_sha256={canon_hash} canon_bytes={canon_bytes} "
                f"files={len(export_files)} zip_bytes={len(payload)} zip_sha256={sha256_bytes(payload)}"
            )
            print("V62_EXPORT_BEGIN")
            for offset in range(0, len(encoded), 6000):
                print(f"V62_EXPORT_CHUNK {offset//6000:04d} {encoded[offset:offset+6000]}")
            print("V62_EXPORT_END")


if __name__ == "__main__":
    unittest.main()
