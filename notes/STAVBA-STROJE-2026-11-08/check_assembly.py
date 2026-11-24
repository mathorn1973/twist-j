#!/usr/bin/env python3
"""Mechanical consistency check of the machine map against the registry.

NON-CANONICAL audit helper for notes/STAVBA-STROJE-2026-11-08. It creates no
claim and changes no file. It checks that

- every registry claim named in ASSEMBLY.tsv or INTERFACES.tsv exists in
  canon/REGISTRY.tsv with exactly the status written in the map;
- every note or probe identifier named in the map exists as a directory or
  file under notes/, notes/canon/, probes/ or reproduce/;
- every evidence path exists in the working tree;
- every slot of ASSEMBLY.tsv appears in INTERFACES.tsv and every interface
  endpoint is a declared slot;
- every interface kind is one of the four declared kinds.

Python standard library only, exact string comparison, deterministic output.
Exit 0 on PASS, 1 on any mismatch.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REGISTRY = ROOT / "canon" / "REGISTRY.tsv"
KINDS = {
    "proved-composition",
    "same-carrier-composable",
    "declared-not-identified",
    "missing-bridge",
}
CLAIM_TOKEN = re.compile(r"^([A-Z0-9][A-Z0-9-]*)\[([A-Z-]+)\]$")
NOTE_TOKEN = re.compile(r"^(C-[A-Z0-9-]+-N\d*|P-[A-Z0-9-]+-\d+|DEF-[A-Z0-9-]+|[A-Z0-9-]+-N)$")


def read_registry() -> dict[str, str]:
    statuses: dict[str, str] = {}
    with REGISTRY.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        header = next(reader)
        assert header[:2] == ["claim_id", "status"], header
        for row in reader:
            if row:
                statuses[row[0]] = row[1]
    return statuses


def read_tsv(name: str) -> list[dict[str, str]]:
    with (HERE / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def locate(identifier: str) -> bool:
    for base in ("notes", "notes/canon", "probes", "reproduce"):
        if (ROOT / base / identifier).exists():
            return True
        if (ROOT / base / f"{identifier}.md").exists():
            return True
    return False


def check_tokens(field: str, where: str, statuses: dict[str, str], problems: list[str],
                 seen_claims: dict[str, str]) -> None:
    for raw in field.split(";"):
        token = raw.strip()
        if not token or token == "-":
            continue
        claim = CLAIM_TOKEN.match(token)
        if claim:
            claim_id, status = claim.groups()
            actual = statuses.get(claim_id)
            if actual is None:
                problems.append(f"{where}: {claim_id} is not a registry claim")
            elif actual != status:
                problems.append(f"{where}: {claim_id} is {actual} in the registry, map says {status}")
            else:
                seen_claims[claim_id] = status
            continue
        if NOTE_TOKEN.match(token):
            if not locate(token):
                problems.append(f"{where}: {token} not found under notes/, probes/ or reproduce/")
            continue
        problems.append(f"{where}: unrecognised token {token!r}")


def check_paths(field: str, where: str, problems: list[str]) -> None:
    for raw in field.split(";"):
        token = raw.strip()
        if not token or token == "-":
            continue
        path = token.split("::", 1)[0]
        if not (ROOT / path).exists():
            problems.append(f"{where}: evidence path {path} does not exist")


def main() -> int:
    statuses = read_registry()
    assembly = read_tsv("ASSEMBLY.tsv")
    interfaces = read_tsv("INTERFACES.tsv")
    problems: list[str] = []
    seen_claims: dict[str, str] = {}

    slots: list[str] = []
    for row in assembly:
        slot = row["slot"].strip()
        if slot in slots:
            problems.append(f"ASSEMBLY.tsv: duplicate slot {slot}")
        slots.append(slot)
        check_tokens(row["filled_by"], f"ASSEMBLY.tsv {slot} filled_by", statuses, problems, seen_claims)
        check_paths(row["evidence"], f"ASSEMBLY.tsv {slot} evidence", problems)

    touched: set[str] = set()
    for index, row in enumerate(interfaces, start=1):
        src, dst, kind = row["from"].strip(), row["to"].strip(), row["kind"].strip()
        where = f"INTERFACES.tsv row {index} {src}->{dst}"
        if kind not in KINDS:
            problems.append(f"{where}: kind {kind!r} not in {sorted(KINDS)}")
        for end in (src, dst):
            if end not in slots:
                problems.append(f"{where}: endpoint {end} is not a slot of ASSEMBLY.tsv")
            touched.add(end)
        check_tokens(row["evidence"], f"{where} evidence", statuses, problems, seen_claims)

    for slot in slots:
        if slot not in touched:
            problems.append(f"ASSEMBLY.tsv: slot {slot} appears in no interface row")

    by_status: dict[str, int] = {}
    for status in seen_claims.values():
        by_status[status] = by_status.get(status, 0) + 1

    print(f"registry claims: {len(statuses)}")
    print(f"slots: {len(slots)}; interfaces: {len(interfaces)}")
    print("registry claims cited by the map, by status: "
          + ", ".join(f"{k}={by_status[k]}" for k in sorted(by_status)))
    print(f"distinct cited claims: {len(seen_claims)}")
    for line in problems:
        print("FAIL: " + line)
    print("ASSEMBLY PASS" if not problems else f"ASSEMBLY FAIL ({len(problems)} problems)")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
