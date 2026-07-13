#!/usr/bin/env python3
"""Find formal Canon status labels without a sentence-local registry id."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
STATUSES = ("T-LOCK", "T", "D", "C", "H", "O", "F")
STATUS_GROUP = re.compile(
    r"\[(?P<body>[^\]]*\b(?:T-LOCK|T|D|C|H|O|F)\b[^\]]*)\]"
)
STATUS_TOKEN = re.compile(r"(?<![A-Z0-9-])(T-LOCK|T|D|C|H|O|F)(?![A-Z0-9-])")
PROSE_STATUS = re.compile(
    r"\b(?:stands?\s+)?at\s+"
    r"(?P<first>T-LOCK|T|D|C|H|O|F)"
    r"(?:\s+and\s+(?P<second>T-LOCK|T|D|C|H|O|F))?\b"
)
SENTENCE_BOUNDARY = re.compile(r"[.!?](?:\s+|$)")


@dataclass(frozen=True)
class Finding:
    line: int
    label: str
    statuses: tuple[str, ...]
    registry_ids: tuple[str, ...]
    missing_statuses: tuple[str, ...]
    sentence: str


def registry(path: Path) -> dict[str, str]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {
            row["claim_id"].strip(): row["status"].strip()
            for row in csv.DictReader(handle, delimiter="\t")
        }


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def sentence_span(text: str, start: int, end: int) -> tuple[int, int]:
    left = 0
    for match in SENTENCE_BOUNDARY.finditer(text, 0, start):
        left = match.end()
    right_match = SENTENCE_BOUNDARY.search(text, end)
    right = right_match.end() if right_match else len(text)
    return left, right


def exact_token(text: str, token: str) -> bool:
    return re.search(
        rf"(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])", text
    ) is not None


def findings(text: str, claims: dict[str, str]) -> list[Finding]:
    result: list[Finding] = []
    markers: list[tuple[int, int, str, tuple[str, ...]]] = []
    for match in STATUS_GROUP.finditer(text):
        statuses = tuple(dict.fromkeys(STATUS_TOKEN.findall(match.group("body"))))
        markers.append((match.start(), match.end(), match.group(0), statuses))
    for match in PROSE_STATUS.finditer(text):
        if any(start <= match.start() and match.end() <= end
               for start, end, _, _ in markers):
            continue
        statuses = tuple(status for status in match.groups() if status)
        markers.append((match.start(), match.end(), match.group(0), statuses))

    for start, end, label, statuses in sorted(markers):
        left, right = sentence_span(text, start, end)
        sentence = " ".join(text[left:right].split())
        ids = tuple(claim for claim in claims if exact_token(sentence, claim))
        covered = {claims[claim] for claim in ids}
        missing = tuple(status for status in statuses if status not in covered)
        if missing:
            result.append(Finding(
                line=line_number(text, start), label=label, statuses=statuses,
                registry_ids=ids, missing_statuses=missing, sentence=sentence
            ))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    canon_path = args.root / "canon" / "CANON.md"
    registry_path = args.root / "canon" / "REGISTRY.tsv"
    problems = findings(
        canon_path.read_text(encoding="utf-8"), registry(registry_path)
    )
    for problem in problems:
        ids = ",".join(problem.registry_ids) or "-"
        missing = ",".join(problem.missing_statuses)
        print(
            f"UNMAPPED line={problem.line} label={problem.label} "
            f"missing={missing} local_ids={ids}"
        )
        print(f"  {problem.sentence}")
    if problems:
        print(f"STATUS LABELS FAIL unmapped={len(problems)}")
        raise SystemExit(1)
    print("STATUS LABELS PASS")


if __name__ == "__main__":
    main()
