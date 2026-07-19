#!/usr/bin/env python3
"""Audit the architecture map against the machine-readable Canon ledgers.

The report is deliberately non-normative. It reads the current ledgers and
answers three narrow questions that are easy to misstate in prose:

* Is DEF-ARCHITECTURE a literal graph root or a high-load hub?
* Which section-16 wall claims inherit DEF-ARCHITECTURE transitively?
* Are the four all-313-attractor theorem rows explicitly bounded by CENSUS-313?

Only the Python standard library is used. The default report exits zero even
when it finds documentation or dependency debt. ``--strict`` turns such debt
into a nonzero exit status, which makes the script suitable for review gates.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


ARCHITECTURE_ITEM = "DEF-ARCHITECTURE"
CENSUS_ITEM = "CENSUS-313"
WALL_SECTION = "16. p = 5 and the wall"
CENSUS_CONSUMERS = (
    "COLOR-RETURN-D5",
    "COLOR-TORSOR-HOLONOMY",
    "COLOR-KIN-NORMALIZER",
    "ELECTRON-SIGN-LAWS",
)

REGISTRY_FIELDS = (
    "claim_id",
    "status",
    "scope",
    "canon_section",
    "evidence",
    "falsifier",
)
NORMATIVE_FIELDS = (
    "item_id",
    "item_type",
    "claim_id",
    "status",
    "layer",
    "gate_ids",
    "statement_source",
)
DEPENDENCY_FIELDS = ("item_id", "depends_on", "relation", "basis")
EVIDENCE_FIELDS = (
    "claim_id",
    "evidence_id",
    "evidence_kind",
    "location",
    "sha256",
    "hash_mode",
    "architecture_requirement",
)
STATUS_COUNT_FIELDS = ("metric", "value")


class AuditError(RuntimeError):
    """Raised when a ledger is malformed or internally inconsistent."""


def read_tsv(path: Path, expected_fields: Sequence[str]) -> list[dict[str, str]]:
    if not path.is_file():
        raise AuditError(f"missing ledger: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = tuple(reader.fieldnames or ())
        if fields != tuple(expected_fields):
            expected = "\t".join(expected_fields)
            raise AuditError(f"{path.name} header must be: {expected}")
        return list(reader)


def unique_index(
    rows: Iterable[Mapping[str, str]], key: str, source_name: str
) -> dict[str, Mapping[str, str]]:
    result: dict[str, Mapping[str, str]] = {}
    for row in rows:
        value = row[key].strip()
        if not value:
            raise AuditError(f"{source_name} has an empty {key}")
        if value in result:
            raise AuditError(f"{source_name} duplicates {value}")
        result[value] = row
    return result


def dependency_graph(
    items: Iterable[str],
    dependencies: Iterable[Mapping[str, str]],
    relation: str | None = None,
) -> dict[str, set[str]]:
    graph = {item: set() for item in items}
    for row in dependencies:
        if relation is not None and row["relation"].strip() != relation:
            continue
        item = row["item_id"].strip()
        target = row["depends_on"].strip()
        if item not in graph or target not in graph:
            raise AuditError(
                f"DEPENDENCIES.tsv names an unknown item in {item} -> {target}"
            )
        graph[item].add(target)
    return graph


def reaches(graph: Mapping[str, set[str]], start: str, target: str) -> bool:
    """Return whether ``start`` transitively depends on ``target``."""

    if start == target:
        return True
    seen: set[str] = set()
    stack = list(graph.get(start, ()))
    while stack:
        item = stack.pop()
        if item == target:
            return True
        if item in seen:
            continue
        seen.add(item)
        stack.extend(graph.get(item, ()))
    return False


@dataclass(frozen=True)
class AuditReport:
    claims: int
    status_counts: dict[str, int]
    evidence_counts: dict[str, int]
    direct_architecture_requires: tuple[str, ...]
    transitive_architecture_dependents: tuple[str, ...]
    dependency_terminals: tuple[str, ...]
    wall_architecture_dependent: tuple[str, ...]
    wall_architecture_free: tuple[str, ...]
    census_edges: dict[str, tuple[str, ...]]
    census_missing: tuple[str, ...]
    census_wrong_relation: tuple[str, ...]
    count_mismatches: tuple[str, ...]

    @property
    def debt(self) -> tuple[str, ...]:
        messages = list(self.count_mismatches)
        if self.census_missing:
            messages.append(
                "missing CENSUS-313 bounds: " + ", ".join(self.census_missing)
            )
        if self.census_wrong_relation:
            messages.append(
                "CENSUS-313 edges must include BOUNDED_BY, not a theorem premise: "
                + ", ".join(self.census_wrong_relation)
            )
        if not self.wall_architecture_dependent:
            messages.append(
                "section 16 currently has no architecture-dependent claim; "
                "review the map's split"
            )
        if not self.wall_architecture_free:
            messages.append(
                "section 16 currently has no architecture-free claim; "
                "review the map's split"
            )
        return tuple(messages)

    def to_json_dict(self) -> dict[str, object]:
        return {
            "claims": self.claims,
            "status_counts": self.status_counts,
            "evidence_counts": self.evidence_counts,
            "architecture": {
                "direct_requires_count": len(self.direct_architecture_requires),
                "direct_requires": list(self.direct_architecture_requires),
                "transitive_dependents_count": len(
                    self.transitive_architecture_dependents
                ),
                "transitive_dependents": list(
                    self.transitive_architecture_dependents
                ),
                "dependency_terminal_count": len(self.dependency_terminals),
                "dependency_terminals": list(self.dependency_terminals),
            },
            "wall_section": {
                "canon_section": WALL_SECTION,
                "architecture_dependent": list(self.wall_architecture_dependent),
                "architecture_free": list(self.wall_architecture_free),
            },
            "census_313": {
                "edges": {
                    item: list(relations)
                    for item, relations in sorted(self.census_edges.items())
                },
                "missing": list(self.census_missing),
                "wrong_relation": list(self.census_wrong_relation),
            },
            "count_mismatches": list(self.count_mismatches),
            "debt": list(self.debt),
        }


def audit(root: Path) -> AuditReport:
    canon = root / "canon"
    registry_rows = read_tsv(canon / "REGISTRY.tsv", REGISTRY_FIELDS)
    normative_rows = read_tsv(canon / "NORMATIVE.tsv", NORMATIVE_FIELDS)
    dependency_rows = read_tsv(canon / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS)
    evidence_rows = read_tsv(canon / "EVIDENCE.tsv", EVIDENCE_FIELDS)
    status_count_rows = read_tsv(canon / "STATUS_COUNTS.tsv", STATUS_COUNT_FIELDS)

    registry = unique_index(registry_rows, "claim_id", "REGISTRY.tsv")
    normative = unique_index(normative_rows, "item_id", "NORMATIVE.tsv")
    evidence_by_claim = unique_index(evidence_rows, "claim_id", "EVIDENCE.tsv")
    status_count_table = unique_index(
        status_count_rows, "metric", "STATUS_COUNTS.tsv"
    )

    for claim in registry:
        if claim not in normative:
            raise AuditError(f"NORMATIVE.tsv lacks registered claim {claim}")
        if claim not in evidence_by_claim:
            raise AuditError(f"EVIDENCE.tsv lacks registered claim {claim}")
    extra_evidence = sorted(set(evidence_by_claim) - set(registry))
    if extra_evidence:
        raise AuditError(
            "EVIDENCE.tsv names unregistered claims: " + ", ".join(extra_evidence)
        )

    requires_graph = dependency_graph(
        normative, dependency_rows, relation="REQUIRES"
    )
    declared_graph = dependency_graph(normative, dependency_rows)
    direct_architecture = tuple(
        sorted(
            row["item_id"].strip()
            for row in dependency_rows
            if row["relation"].strip() == "REQUIRES"
            and row["depends_on"].strip() == ARCHITECTURE_ITEM
        )
    )
    transitive_architecture = tuple(
        sorted(
            item
            for item in normative
            if item != ARCHITECTURE_ITEM
            and reaches(requires_graph, item, ARCHITECTURE_ITEM)
        )
    )
    terminals = tuple(
        sorted(item for item, targets in declared_graph.items() if not targets)
    )

    wall_claims = tuple(
        sorted(
            claim
            for claim, row in registry.items()
            if row["canon_section"].strip() == WALL_SECTION
        )
    )
    wall_dependent = tuple(
        claim
        for claim in wall_claims
        if reaches(requires_graph, claim, ARCHITECTURE_ITEM)
    )
    wall_free = tuple(claim for claim in wall_claims if claim not in wall_dependent)

    census_edges: dict[str, tuple[str, ...]] = {}
    for consumer in CENSUS_CONSUMERS:
        if consumer not in normative:
            raise AuditError(f"NORMATIVE.tsv lacks expected census consumer {consumer}")
        relations = tuple(
            sorted(
                {
                    row["relation"].strip()
                    for row in dependency_rows
                    if row["item_id"].strip() == consumer
                    and row["depends_on"].strip() == CENSUS_ITEM
                }
            )
        )
        census_edges[consumer] = relations
    census_missing = tuple(
        item for item in CENSUS_CONSUMERS if not census_edges[item]
    )
    census_wrong_relation = tuple(
        item
        for item in CENSUS_CONSUMERS
        if census_edges[item] and "BOUNDED_BY" not in census_edges[item]
    )

    status_counts = dict(
        sorted(Counter(row["status"].strip() for row in registry_rows).items())
    )
    evidence_counts = dict(
        sorted(
            Counter(
                row["architecture_requirement"].strip() for row in evidence_rows
            ).items()
        )
    )

    expected_metrics = {"claims": len(registry_rows)}
    expected_metrics.update(
        {f"status_{status}": count for status, count in status_counts.items()}
    )
    expected_metrics.update(
        {
            f"evidence_{architecture}": count
            for architecture, count in evidence_counts.items()
        }
    )
    count_mismatches: list[str] = []
    for metric, calculated in sorted(expected_metrics.items()):
        row = status_count_table.get(metric)
        if row is None:
            count_mismatches.append(f"STATUS_COUNTS.tsv lacks {metric}")
            continue
        try:
            recorded = int(row["value"].strip())
        except ValueError as exc:
            raise AuditError(f"STATUS_COUNTS.tsv has a non-integer {metric}") from exc
        if recorded != calculated:
            count_mismatches.append(
                f"{metric}: recorded {recorded}, calculated {calculated}"
            )

    return AuditReport(
        claims=len(registry_rows),
        status_counts=status_counts,
        evidence_counts=evidence_counts,
        direct_architecture_requires=direct_architecture,
        transitive_architecture_dependents=transitive_architecture,
        dependency_terminals=terminals,
        wall_architecture_dependent=wall_dependent,
        wall_architecture_free=wall_free,
        census_edges=census_edges,
        census_missing=census_missing,
        census_wrong_relation=census_wrong_relation,
        count_mismatches=tuple(count_mismatches),
    )


def format_items(items: Sequence[str]) -> str:
    return ", ".join(items) if items else "(none)"


def render_text(report: AuditReport) -> str:
    lines = [
        "TWIST-J architecture-map ledger audit",
        "======================================",
        f"claims: {report.claims}",
        "status counts: "
        + ", ".join(f"{key}={value}" for key, value in report.status_counts.items()),
        "evidence counts: "
        + ", ".join(
            f"{key}={value}" for key, value in report.evidence_counts.items()
        ),
        "",
        "Architecture topology",
        "---------------------",
        f"direct REQUIRES -> {ARCHITECTURE_ITEM}: "
        f"{len(report.direct_architecture_requires)}",
        f"transitive REQUIRES -> {ARCHITECTURE_ITEM}: "
        f"{len(report.transitive_architecture_dependents)}",
        f"declared-dependency terminals: {len(report.dependency_terminals)}",
        "terminal items: " + format_items(report.dependency_terminals),
        "",
        "Section-16 wall split",
        "---------------------",
        "architecture-dependent: "
        + format_items(report.wall_architecture_dependent),
        "architecture-free: " + format_items(report.wall_architecture_free),
        "",
        "CENSUS-313 bounds",
        "-----------------",
    ]
    for item in CENSUS_CONSUMERS:
        lines.append(f"{item}: {format_items(report.census_edges[item])}")
    lines.extend(["", "Debt", "----"])
    if report.debt:
        lines.extend(f"- {message}" for message in report.debt)
    else:
        lines.append("none")
    return "\n".join(lines) + "\n"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: parent of tools/)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="report format",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 when the report contains count or dependency debt",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = audit(args.root.resolve())
    except (AuditError, OSError) as exc:
        print(f"architecture-map audit error: {exc}")
        return 2

    if args.format == "json":
        print(json.dumps(report.to_json_dict(), indent=2, sort_keys=True))
    else:
        print(render_text(report), end="")
    return 1 if args.strict and report.debt else 0


if __name__ == "__main__":
    raise SystemExit(main())
