"""Validators for the policy-compliant aarch64 Genesis artifact package."""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path
import re


class GenesisArtifactError(RuntimeError):
    pass


RECONSTRUCTION_FIELDS = (
    "item_id", "current_claim_id", "action", "public_statement",
    "evidence_required", "post_genesis_probe", "blocker",
)
FRONTIER_SPLIT_FIELDS = (
    "parent_id", "child_id", "child_status", "layer",
    "decision_condition", "dependencies",
)
EXTERNAL_SOURCE_FIELDS = (
    "source_id", "observable", "source_title", "edition", "DOI_or_record",
    "value", "uncertainty", "units", "scheme", "access_date", "local_hash",
    "license",
)
ENGINEERING_FIELDS = (
    "item_id", "canon_locator", "observable", "value", "source_id", "action",
    "evidence_path", "rationale",
)

RECON_ITEMS = {
    "CURVATURE-TRACE-VALUE",
    "CODEC-RATE-SCOPE",
    "BELL-MAGIC-BOUNDARY",
    "KERNEL-CONNECT-ALL-K",
    "PHOTON-RADIATIVE-INDEPENDENCE",
    "FIBER-THRESHOLD",
    "ETA-ALTERNATOR-BRIDGE",
    "LORENTZ-A2A3",
    "TT-GAUGE-PULLBACK",
}
RECON_ACTIONS = {
    "KEEP_PRECISE_O", "KEEP_PRECISE_H", "SPLIT", "RETIRE", "REMOVE_PROSE",
    "PORT_PREREG",
}
SPLIT_COUNTS = {
    "METRO-ADMISSIBILITY": 6,
    "METRO-EDGE-SCALE": 3,
    "QUANT-SUBSTRATE": 2,
    "SCHEME-DICTIONARY": 3,
    "PHOTON-WINDOW-PROOF": 2,
    "LORENTZ-A2A3": 3,
}
LAYERS = {"L1", "L2", "L3", "L4", "L5", "L6", "MULTI", "NOT_APPLICABLE"}
ENGINEERING_ITEMS = {
    "CODATA-ALPHA",
    "HULSE-TAYLOR",
    "MUON-TAU-SIGMA",
    "NEUTRON-PPM",
    "NGEHT-CORRIDOR",
    "CIRCUIT-COUNT",
    "SIX-PLATFORM-BITEXACT",
    "HYDROGEN-HELIUM",
}
ENGINEERING_ACTIONS = {
    "KEEP_MEASURED", "KEEP_ENGINEERING", "MOVE_TO_NOTES", "REMOVE",
    "PUBLIC_C_EVIDENCE",
}
PREREG_FILES = {
    "01-curvature.md",
    "02-tm-sym2.md",
    "03-qenv.md",
    "04-color-measure.md",
    "05-spin-lift.md",
    "06-bell-boundary.md",
}
PREREG_FIELDS = (
    "Claim", "Action layer", "Input object", "Observable", "PASS", "FAIL",
    "Budget", "Stop rule", "Post-pin changes",
)
ID = re.compile(r"^[A-Z][A-Z0-9-]*$")
SOURCE_ID = re.compile(r"^SRC-[A-Z0-9][A-Z0-9-]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def fail(message: str) -> None:
    raise GenesisArtifactError(message)


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"missing {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != fields:
            fail(f"{path.name} header must be: " + "\t".join(fields))
        return list(reader)


def required(row: dict[str, str], field: str, context: str) -> str:
    value = row[field].strip()
    if not value:
        fail(f"{context} has empty {field}")
    return value


def registry_claims(root: Path) -> set[str]:
    path = root / "canon" / "REGISTRY.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["claim_id"].strip() for row in csv.DictReader(handle, delimiter="\t")}


def validate_recon(root: Path) -> tuple[int, int]:
    directory = root / "notes" / "genesis" / "recon"
    recon = read_tsv(directory / "RECONSTRUCTION.tsv", RECONSTRUCTION_FIELDS)
    splits = read_tsv(directory / "FRONTIER_SPLITS.tsv", FRONTIER_SPLIT_FIELDS)
    claims = registry_claims(root)

    seen: set[str] = set()
    for number, row in enumerate(recon, 2):
        context = f"RECONSTRUCTION.tsv line {number}"
        item = required(row, "item_id", context)
        if item not in RECON_ITEMS or item in seen:
            fail(f"{context} has unexpected or duplicate item_id {item}")
        seen.add(item)
        claim = required(row, "current_claim_id", context)
        if claim not in claims:
            fail(f"{item} names unknown current_claim_id {claim}")
        if required(row, "action", context) not in RECON_ACTIONS:
            fail(f"{item} has invalid action")
        if len(required(row, "public_statement", context)) < 20:
            fail(f"{item} public_statement is too short")
        if len(required(row, "evidence_required", context)) < 10:
            fail(f"{item} evidence_required is too short")
        required(row, "post_genesis_probe", context)
        if len(required(row, "blocker", context)) < 10:
            fail(f"{item} blocker is too short")
    missing = sorted(RECON_ITEMS - seen)
    if missing:
        fail("RECONSTRUCTION.tsv lacks: " + ", ".join(missing))

    parent_counts = {parent: 0 for parent in SPLIT_COUNTS}
    declared_children = [row["child_id"].strip() for row in splits]
    children = set(declared_children)
    if len(children) != len(declared_children):
        fail("FRONTIER_SPLITS.tsv duplicates a child_id")
    for number, row in enumerate(splits, 2):
        context = f"FRONTIER_SPLITS.tsv line {number}"
        parent = required(row, "parent_id", context)
        child = required(row, "child_id", context)
        if parent not in SPLIT_COUNTS:
            fail(f"{context} has unexpected parent {parent}")
        if child in claims or not ID.fullmatch(child):
            fail(f"{context} has invalid or colliding child {child}")
        parent_counts[parent] += 1
        if required(row, "child_status", context) not in {"H", "O"}:
            fail(f"{child} must remain H or O during Genesis")
        if required(row, "layer", context) not in LAYERS:
            fail(f"{child} has invalid layer")
        if len(required(row, "decision_condition", context)) < 30:
            fail(f"{child} decision condition is too short")
        dependencies = required(row, "dependencies", context)
        if dependencies != "-":
            for dependency in dependencies.split(";"):
                if dependency.strip() not in claims and dependency.strip() not in children:
                    fail(f"{child} names unknown dependency {dependency.strip()}")
    for parent, expected in SPLIT_COUNTS.items():
        if parent_counts[parent] != expected:
            fail(f"{parent} must split into {expected} children, got {parent_counts[parent]}")
    return len(recon), len(splits)


def validate_sources(root: Path) -> tuple[int, int]:
    sources = read_tsv(root / "data" / "EXTERNAL_SOURCES.tsv", EXTERNAL_SOURCE_FIELDS)
    engineering = read_tsv(
        root / "data" / "ENGINEERING_DISPOSITION.tsv", ENGINEERING_FIELDS
    )
    source_ids: set[str] = set()
    for number, row in enumerate(sources, 2):
        context = f"EXTERNAL_SOURCES.tsv line {number}"
        source_id = required(row, "source_id", context)
        if not SOURCE_ID.fullmatch(source_id) or source_id in source_ids:
            fail(f"{context} has invalid or duplicate source_id")
        source_ids.add(source_id)
        for field in (
            "observable", "source_title", "edition", "DOI_or_record", "value",
            "uncertainty", "units", "scheme", "license",
        ):
            required(row, field, context)
        try:
            date.fromisoformat(required(row, "access_date", context))
        except ValueError:
            fail(f"{source_id} has invalid access_date")
        local_hash = required(row, "local_hash", context)
        if local_hash != "NOT-LOCAL" and not SHA256.fullmatch(local_hash):
            fail(f"{source_id} has invalid local_hash")

    seen_items: set[str] = set()
    for number, row in enumerate(engineering, 2):
        context = f"ENGINEERING_DISPOSITION.tsv line {number}"
        item = required(row, "item_id", context)
        if item not in ENGINEERING_ITEMS or item in seen_items:
            fail(f"{context} has unexpected or duplicate item_id {item}")
        seen_items.add(item)
        for field in ("canon_locator", "observable", "value", "rationale"):
            required(row, field, context)
        action = required(row, "action", context)
        if action not in ENGINEERING_ACTIONS:
            fail(f"{item} has invalid action")
        source_id = row["source_id"].strip()
        evidence_path = row["evidence_path"].strip()
        if action in {"KEEP_MEASURED", "KEEP_ENGINEERING"} and source_id not in source_ids:
            fail(f"{item} retained without a valid source_id")
        if action == "PUBLIC_C_EVIDENCE":
            if not evidence_path or not (root / evidence_path).exists():
                fail(f"{item} public C evidence path is missing")
        if action in {"MOVE_TO_NOTES", "REMOVE"} and not evidence_path:
            fail(f"{item} disposition must name its destination or '-' explicitly")
    missing = sorted(ENGINEERING_ITEMS - seen_items)
    if missing:
        fail("ENGINEERING_DISPOSITION.tsv lacks: " + ", ".join(missing))
    return len(sources), len(engineering)


def validate_prereg(root: Path) -> int:
    directory = root / "notes" / "prereg" / "post-genesis"
    if not directory.is_dir():
        fail(f"missing {directory}")
    present = {path.name for path in directory.iterdir() if path.is_file()}
    missing = sorted(PREREG_FILES - present)
    if missing:
        fail("post-Genesis preregistration drafts lack: " + ", ".join(missing))
    forbidden = sorted(
        path.relative_to(directory).as_posix()
        for path in directory.rglob("*")
        if path.is_file() and path.name in {"RUN.md", "RESULT.md", "EXPECTED.txt"}
    )
    if forbidden:
        fail("Genesis preregistration area contains formal results: " + ", ".join(forbidden))
    for name in sorted(PREREG_FILES):
        text = (directory / name).read_text(encoding="utf-8")
        if "NON-CANONICAL" not in text or "DRAFT" not in text:
            fail(f"{name} must declare NON-CANONICAL DRAFT")
        for field in PREREG_FIELDS:
            if not re.search(rf"(?mi)^\*\*{re.escape(field)}:\*\*\s*\S", text):
                fail(f"{name} lacks field {field}")
        if re.search(r"(?mi)^\*\*(?:Result|Conclusion|Earned status):\*\*", text):
            fail(f"{name} contains a result during Genesis")
    return len(PREREG_FILES)
