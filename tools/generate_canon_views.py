#!/usr/bin/env python3
"""Generate deterministic Canon summaries from the public ledgers.

During parallel Genesis preparation this command writes only to an explicit
output directory.  The final reconciliation commit decides when the generated
views replace or enter the five hashed Canon files.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

try:
    from check_ledger import validate
except ModuleNotFoundError:  # imported as tools.generate_canon_views in tests
    from tools.check_ledger import validate


REGISTRY_FIELDS = (
    "claim_id", "status", "scope", "canon_section", "evidence", "falsifier"
)
CORE_SELECTION_FIELDS = ("rank", "claim_id")


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != fields:
            raise ValueError(f"{path.name} schema mismatch")
        return list(reader)


def wrap_claim(claim: str, status: str, scope: str, decision: str | None = None) -> str:
    lines = [f"- {claim} [{status}]: {scope}"]
    if decision:
        lines.append(f"  Decision: {decision}")
    return "\n".join(lines)


def render_frontier(rows: list[dict[str, str]]) -> str:
    live = [row for row in rows if row["status"] in {"H", "O"}]
    groups = (
        ("Hypotheses", "H"),
        ("Open obligations", "O"),
    )
    parts = [
        "# TWIST-J frontier",
        "",
        "This file is generated from `canon/REGISTRY.tsv`. Every live row has",
        "one public scope and one concrete falsifier or decision condition.",
        "Closed claims are excluded.",
    ]
    for title, status in groups:
        parts.extend(["", f"## {title} [{status}]", ""])
        selected = sorted(
            (row for row in live if row["status"] == status),
            key=lambda row: row["claim_id"],
        )
        parts.extend(
            wrap_claim(row["claim_id"], status, row["scope"], row["falsifier"])
            for row in selected
        )
    parts.extend(["", f"Live total: {len(live)}.", ""])
    return "\n".join(parts)


def render_core_claims(
    registry: dict[str, dict[str, str]], selection: list[dict[str, str]]
) -> str:
    ordered = sorted(selection, key=lambda row: int(row["rank"]))
    parts = [
        "<!-- BEGIN GENERATED CORE CLAIMS -->",
        "The stable orientation claims are generated from the registry:",
        "",
    ]
    parts.extend(
        wrap_claim(claim, registry[claim]["status"], registry[claim]["scope"])
        for claim in (row["claim_id"] for row in ordered)
    )
    parts.extend(["", "<!-- END GENERATED CORE CLAIMS -->", ""])
    return "\n".join(parts)


def render_counts(root: Path, rows: list[dict[str, str]]) -> str:
    statuses = {status: 0 for status in ("T-LOCK", "T", "D", "C", "H", "O", "F")}
    for row in rows:
        statuses[row["status"]] += 1
    reproductions = sorted(
        path.name for path in (root / "reproduce").iterdir() if path.is_dir()
    )
    evidence_rows = read_tsv(root / "canon" / "EVIDENCE.tsv", (
        "claim_id", "evidence_id", "evidence_kind", "location", "sha256",
        "hash_mode", "architecture_requirement",
    ))
    architecture: dict[str, int] = {}
    for row in evidence_rows:
        key = row["architecture_requirement"]
        architecture[key] = architecture.get(key, 0) + 1
    lines = ["metric\tvalue", f"claims\t{len(rows)}"]
    lines.extend(f"status_{status}\t{statuses[status]}" for status in statuses)
    lines.extend((
        f"live_H_O\t{statuses['H'] + statuses['O']}",
        f"reproductions\t{len(reproductions)}",
    ))
    lines.extend(
        f"evidence_{key}\t{architecture[key]}" for key in sorted(architecture)
    )
    lines.append("")
    return "\n".join(lines)


def generated_views(root: Path) -> dict[str, str]:
    validate(root)
    rows = read_tsv(root / "canon" / "REGISTRY.tsv", REGISTRY_FIELDS)
    registry = {row["claim_id"]: row for row in rows}
    selection = read_tsv(
        root / "canon" / "CORE_SELECTION.tsv", CORE_SELECTION_FIELDS
    )
    return {
        "FRONTIER.md": render_frontier(rows),
        "CORE_CLAIMS.md": render_core_claims(registry, selection),
        "STATUS_COUNTS.tsv": render_counts(root, rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output-dir", type=Path)
    group.add_argument("--check-dir", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        views = generated_views(root)
    except (ValueError, RuntimeError) as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)

    if args.output_dir is not None:
        output = args.output_dir.resolve()
        output.mkdir(parents=True, exist_ok=True)
        for name, content in views.items():
            (output / name).write_text(content, encoding="utf-8")
        print(
            "CANON VIEWS GENERATED "
            + " ".join(f"{name}={len(content.encode('utf-8'))}" for name, content in views.items())
        )
        return

    check = args.check_dir.resolve()
    differences: list[str] = []
    for name, content in views.items():
        path = check / name
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            differences.append(name)
    if differences:
        print("FAIL: generated Canon views differ: " + ", ".join(differences))
        raise SystemExit(1)
    print("CANON VIEWS PASS " + ",".join(sorted(views)))


if __name__ == "__main__":
    main()
