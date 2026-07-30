#!/usr/bin/env python3
"""Generate deterministic Canon summaries from the public ledgers.

During parallel Genesis preparation this command writes only to an explicit
output directory. The final reconciliation uses `--apply` once to update the
derived views inside the Canon bundle.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re

try:
    from check_ledger import (
        FRONTIER_PROGRAM_FIELDS,
        FRONTIER_PROGRAM_ORDER,
        validate,
    )
except ModuleNotFoundError:  # imported as tools.generate_canon_views in tests
    from tools.check_ledger import (
        FRONTIER_PROGRAM_FIELDS,
        FRONTIER_PROGRAM_ORDER,
        validate,
    )


REGISTRY_FIELDS = (
    "claim_id", "status", "scope", "canon_section", "evidence", "falsifier"
)
CORE_SELECTION_FIELDS = ("rank", "claim_id")


def current_canon_version(text: str) -> str:
    title = text.splitlines()[0] if text.splitlines() else ""
    match = re.fullmatch(r"# TWIST-J Public Canon v([1-9][0-9]*)", title)
    if not match:
        raise ValueError("CANON.md lacks an exact positive whole-number title")
    return match.group(1)


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != fields:
            raise ValueError(f"{path.name} schema mismatch")
        return list(reader)


def wrap_claim(
    claim: str, status: str, scope: str, decision: str | None = None,
    queue: str | None = None,
) -> str:
    lines = [f"- {claim} [{status}]: {scope}"]
    if queue:
        lines.append(f"  Queue: {queue}.")
    if decision:
        lines.append(f"  Decision: {decision}")
    return "\n".join(lines)


FRONTIER_PROGRAM_TITLES = {
    "DECODER_CORE": "Decoder core",
    "MEASURE": "Measure selection",
    "COSMOLOGY": "Geometry and cosmology",
    "TENSOR": "Tensor and radiation",
    "NONABELIAN_QCD": "Nonabelian and QCD",
    "QUANTUM_EM": "Quantum and electromagnetic wall",
    "PHOTON_CONTINUUM": "Photon continuum",
    "ENRICHMENT": "Enrichment",
}


def render_frontier(
    rows: list[dict[str, str]], programs: list[dict[str, str]]
) -> str:
    live = [row for row in rows if row["status"] in {"H", "O"}]
    program_by_claim = {row["claim_id"]: row for row in programs}
    parts = [
        "# TWIST-J frontier",
        "",
        "This file is generated from `canon/REGISTRY.tsv` and grouped by",
        "`canon/FRONTIER_PROGRAMS.tsv`. `REGISTRY.tsv` alone determines which",
        "claims are live and supplies every status, scope, and decision condition.",
        "The program table supplies scheduler labels only. It creates no claim,",
        "status, scope, dependency, layer, gate, evidence, or verifier permission.",
        "Closed claims are excluded.",
    ]
    role_order = {"ROOT": 0, "FOLLOWUP": 1}
    for program_id in FRONTIER_PROGRAM_ORDER:
        selected = sorted(
            (
                row for row in live
                if program_by_claim[row["claim_id"]]["program_id"] == program_id
            ),
            key=lambda row: (
                role_order[program_by_claim[row["claim_id"]]["queue_role"]],
                row["claim_id"],
            ),
        )
        if not selected:
            continue
        title = FRONTIER_PROGRAM_TITLES[program_id]
        parts.extend(["", f"## {title} (`{program_id}`)", ""])
        parts.extend(
            wrap_claim(
                row["claim_id"],
                row["status"],
                row["scope"],
                row["falsifier"],
                "; ".join(
                    program_by_claim[row["claim_id"]][field]
                    for field in ("queue_role", "work_state", "work_mode")
                ),
            )
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


def render_changelog_counts(root: Path, rows: list[dict[str, str]]) -> str:
    statuses = {status: 0 for status in ("T-LOCK", "T", "D", "C", "H", "O", "F")}
    for row in rows:
        statuses[row["status"]] += 1
    reproductions = sum(
        1 for path in (root / "reproduce").iterdir() if path.is_dir()
    )
    return "\n".join((
        "<!-- BEGIN GENERATED CURRENT COUNTS -->",
        f"Registry snapshot: {len(rows)} claims; "
        + ", ".join(f"{statuses[status]} {status}" for status in statuses)
        + f"; {statuses['H'] + statuses['O']} live H/O.",
        f"Reproduction witnesses: {reproductions}.",
        "<!-- END GENERATED CURRENT COUNTS -->",
        "",
    ))


def generated_views(root: Path) -> dict[str, str]:
    validate(root)
    rows = read_tsv(root / "canon" / "REGISTRY.tsv", REGISTRY_FIELDS)
    registry = {row["claim_id"]: row for row in rows}
    selection = read_tsv(
        root / "canon" / "CORE_SELECTION.tsv", CORE_SELECTION_FIELDS
    )
    programs = read_tsv(
        root / "canon" / "FRONTIER_PROGRAMS.tsv", FRONTIER_PROGRAM_FIELDS
    )
    return {
        "FRONTIER.md": render_frontier(rows, programs),
        "CORE_CLAIMS.md": render_core_claims(registry, selection),
        "STATUS_COUNTS.tsv": render_counts(root, rows),
        "CHANGELOG_COUNTS.md": render_changelog_counts(root, rows),
    }


def replace_marked(text: str, block: str, begin: str, end: str) -> str:
    start = text.find(begin)
    if start < 0:
        raise ValueError(f"missing generated block marker: {begin}")
    stop = text.find(end, start)
    if stop < 0:
        raise ValueError(f"missing generated block marker: {end}")
    stop += len(end)
    return text[:start] + block.rstrip("\n") + text[stop:]


def synchronize_core_release(text: str, version: str) -> str:
    replacements = (
        (
            r"(?m)^\*\*Release identity:\*\* Public Canon v[1-9][0-9]*\.",
            f"**Release identity:** Public Canon v{version}.",
        ),
        (
            r"(?m)^Public Canon v[1-9][0-9]* also declares a discrete architecture\.",
            f"Public Canon v{version} also declares a discrete architecture.",
        ),
    )
    for pattern, replacement in replacements:
        text, count = re.subn(pattern, replacement, text)
        if count != 1:
            raise ValueError("CORE.md lacks an exact release-version anchor")
    return text


def apply_views(root: Path, views: dict[str, str]) -> None:
    canon = root / "canon"
    (canon / "FRONTIER.md").write_text(
        views["FRONTIER.md"], encoding="utf-8", newline="\n"
    )
    (canon / "STATUS_COUNTS.tsv").write_text(
        views["STATUS_COUNTS.tsv"], encoding="utf-8", newline="\n"
    )

    core_path = canon / "CORE.md"
    core = core_path.read_text(encoding="utf-8")
    canon_text = (canon / "CANON.md").read_text(encoding="utf-8")
    core = synchronize_core_release(core, current_canon_version(canon_text))
    core_begin = "<!-- BEGIN GENERATED CORE CLAIMS -->"
    core_end = "<!-- END GENERATED CORE CLAIMS -->"
    if core_begin in core:
        core = replace_marked(core, views["CORE_CLAIMS.md"], core_begin, core_end)
    else:
        start = core.find("Stable orientation results:")
        stop = core.find("\nTime is a counter.", start)
        if start < 0 or stop < 0:
            raise ValueError("CORE.md lacks the stable-orientation replacement anchors")
        core = core[:start] + views["CORE_CLAIMS.md"].rstrip("\n") + core[stop:]
    core_path.write_text(core, encoding="utf-8", newline="\n")

    changelog_path = canon / "CHANGELOG.md"
    changelog = changelog_path.read_text(encoding="utf-8")
    count_begin = "<!-- BEGIN GENERATED CURRENT COUNTS -->"
    count_end = "<!-- END GENERATED CURRENT COUNTS -->"
    if count_begin in changelog:
        changelog = replace_marked(
            changelog, views["CHANGELOG_COUNTS.md"], count_begin, count_end
        )
    else:
        version = current_canon_version(canon_text)
        anchor = f"## Public Canon v{version}"
        position = changelog.find(anchor)
        if position < 0:
            raise ValueError(f"CHANGELOG.md lacks the {anchor.removeprefix('## ')} anchor")
        position += len(anchor)
        changelog = (
            changelog[:position]
            + "\n\n"
            + views["CHANGELOG_COUNTS.md"].rstrip("\n")
            + changelog[position:]
        )
    changelog_path.write_text(changelog, encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--output-dir", type=Path)
    group.add_argument("--check-dir", type=Path)
    group.add_argument("--apply", action="store_true")
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
            (output / name).write_text(content, encoding="utf-8", newline="\n")
        print(
            "CANON VIEWS GENERATED "
            + " ".join(f"{name}={len(content.encode('utf-8'))}" for name, content in views.items())
        )
        return

    if args.apply:
        try:
            apply_views(root, views)
        except ValueError as error:
            print(f"FAIL: {error}")
            raise SystemExit(1)
        print("CANON VIEWS APPLIED " + ",".join(sorted(views)))
        return

    check = args.check_dir.resolve()
    differences: list[str] = []
    for name, content in views.items():
        if name == "CORE_CLAIMS.md":
            path = check / "CORE.md"
            matches = False
            if path.is_file():
                core = path.read_text(encoding="utf-8")
                canon_text = (root / "canon" / "CANON.md").read_text(encoding="utf-8")
                version = current_canon_version(canon_text)
                matches = (
                    content.rstrip("\n") in core
                    and synchronize_core_release(core, version) == core
                )
        elif name == "CHANGELOG_COUNTS.md":
            path = check / "CHANGELOG.md"
            matches = path.is_file() and content.rstrip("\n") in path.read_text(encoding="utf-8")
        else:
            path = check / name
            matches = path.is_file() and path.read_text(encoding="utf-8") == content
        if not matches:
            differences.append(name)
    if differences:
        print("FAIL: generated Canon views differ: " + ", ".join(differences))
        raise SystemExit(1)
    print("CANON VIEWS PASS " + ",".join(sorted(views)))


if __name__ == "__main__":
    main()
