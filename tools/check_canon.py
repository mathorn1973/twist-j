#!/usr/bin/env python3
"""Validate the public Canon bundle and its machine-readable registry."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
CANON_DIR = ROOT / "canon"
REQUIRED_FILES = {
    "CANON.md",
    "CORE.md",
    "FRONTIER.md",
    "REGISTRY.tsv",
    "CHANGELOG.md",
    "SHA256SUMS",
}
HASHED_FILES = (
    "CANON.md",
    "CORE.md",
    "FRONTIER.md",
    "REGISTRY.tsv",
    "CHANGELOG.md",
)
REGISTRY_FIELDS = (
    "claim_id",
    "status",
    "scope",
    "canon_section",
    "evidence",
    "falsifier",
)
STATUSES = {"T-LOCK", "T", "D", "C", "H", "O", "F"}
CLAIM_ID = re.compile(r"^[A-Z][A-Z0-9-]*$")
CLAIM_TOKEN = re.compile(r"\b(?:T-LOCK|T|D|C|H|O|F)-[A-Z0-9][A-Z0-9-]*\b")
FORBIDDEN_CANON_PHRASES = (
    "TWIST_J_Canon_",
    "CROSSPLATFORM_LOCK_RECORD",
    "fold commit",
    "carried forward",
    "JAS 2",
    "TWISTER",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def status_fields() -> dict[str, str]:
    path = ROOT / "STATUS.md"
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*?)\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def exact_token(text: str, token: str) -> bool:
    pattern = rf"(?<![A-Z0-9-]){re.escape(token)}(?![A-Z0-9-])"
    return re.search(pattern, text) is not None


fields = status_fields()
state = fields.get("STATE")

if not CANON_DIR.exists():
    if state == "ACTIVE":
        fail("ACTIVE repository lacks canon/")
    print("CANON NOT APPLICABLE")
    raise SystemExit(0)

citation_path = ROOT / "CITATION.cff"
if not citation_path.is_file():
    fail("public Canon bundle lacks CITATION.cff")
citation = citation_path.read_text(encoding="utf-8")
for field in ("cff-version:", "title:", "authors:", "version:", "license:"):
    if field not in citation:
        fail(f"CITATION.cff lacks {field}")

present = {path.name for path in CANON_DIR.iterdir() if path.is_file()}
missing = sorted(REQUIRED_FILES - present)
if missing:
    fail(f"canon/ lacks: {', '.join(missing)}")

canon = (CANON_DIR / "CANON.md").read_text(encoding="utf-8")
core = (CANON_DIR / "CORE.md").read_text(encoding="utf-8")
frontier = (CANON_DIR / "FRONTIER.md").read_text(encoding="utf-8")
changelog = (CANON_DIR / "CHANGELOG.md").read_text(encoding="utf-8")

version_match = re.search(r"Public Canon v([1-9][0-9]*)", canon)
if not version_match:
    fail("CANON.md lacks a Public Canon vN title")
version = version_match.group(1)
if f"Public Canon v{version}" not in changelog:
    fail("CHANGELOG.md lacks the current Public Canon version")

for phrase in FORBIDDEN_CANON_PHRASES:
    if phrase.lower() in canon.lower():
        fail(f"CANON.md contains internal-history phrase: {phrase}")

registry_path = CANON_DIR / "REGISTRY.tsv"
with registry_path.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    if tuple(reader.fieldnames or ()) != REGISTRY_FIELDS:
        fail("REGISTRY.tsv header must be: " + "\t".join(REGISTRY_FIELDS))
    rows = list(reader)

if not rows:
    fail("REGISTRY.tsv has no claims")

claims: dict[str, dict[str, str]] = {}
for number, row in enumerate(rows, start=2):
    claim = (row.get("claim_id") or "").strip()
    status = (row.get("status") or "").strip()
    if not CLAIM_ID.fullmatch(claim):
        fail(f"REGISTRY.tsv line {number} has invalid claim_id")
    if claim in claims:
        fail(f"REGISTRY.tsv duplicates claim_id: {claim}")
    if status not in STATUSES:
        fail(f"{claim} has invalid status: {status}")
    for field in ("scope", "canon_section", "evidence"):
        if not (row.get(field) or "").strip():
            fail(f"{claim} has empty {field}")
    if (row.get("canon_section") or "").strip() not in canon:
        fail(f"{claim} canon_section is absent from CANON.md")
    if status in {"H", "O", "F"} and not (row.get("falsifier") or "").strip():
        fail(f"{claim} with status {status} lacks falsifier")
    if not exact_token(canon, claim):
        fail(f"{claim} is absent from CANON.md")

    evidence = (row.get("evidence") or "").strip()
    if evidence != "inline" and not evidence.startswith(("https://", "http://")):
        relative_evidence = Path(evidence)
        evidence_path = ROOT / relative_evidence
        if relative_evidence.is_absolute() or ".." in relative_evidence.parts:
            fail(f"{claim} has unsafe evidence path")
        if not evidence_path.exists():
            fail(f"{claim} evidence path does not exist: {evidence}")
    claims[claim] = row

for text_name, text in (("CORE.md", core), ("FRONTIER.md", frontier)):
    for token in CLAIM_TOKEN.findall(text):
        if token not in claims:
            fail(f"{text_name} references unregistered claim: {token}")

frontier_claims = {claim for claim in claims if exact_token(frontier, claim)}
expected_frontier = {
    claim for claim, row in claims.items() if row["status"].strip() in {"H", "O"}
}
missing_frontier = sorted(expected_frontier - frontier_claims)
if missing_frontier:
    fail("FRONTIER.md lacks live claims: " + ", ".join(missing_frontier))

for line in frontier.splitlines():
    if not re.match(r"^\s*-\s+", line):
        continue
    tokens = [claim for claim in claims if exact_token(line, claim)]
    if tokens and claims[tokens[0]]["status"].strip() not in {"H", "O"}:
        fail(f"FRONTIER.md list item starts with closed claim: {tokens[0]}")

sums_path = CANON_DIR / "SHA256SUMS"
sums: dict[str, str] = {}
for number, line in enumerate(sums_path.read_text(encoding="utf-8").splitlines(), start=1):
    match = re.fullmatch(r"([0-9a-f]{64})  (canon/[A-Za-z0-9_.-]+)", line)
    if not match:
        fail(f"SHA256SUMS line {number} has invalid format")
    digest, relative = match.groups()
    if relative in sums:
        fail(f"SHA256SUMS duplicates {relative}")
    sums[relative] = digest

expected_sum_paths = {f"canon/{name}" for name in HASHED_FILES}
if set(sums) != expected_sum_paths:
    fail("SHA256SUMS must cover exactly the five normative Canon files")
for relative, digest in sums.items():
    if sha256(ROOT / relative) != digest:
        fail(f"SHA256SUMS mismatch: {relative}")

if state == "ACTIVE":
    expected = {
        "CANON": f"Public Canon v{version}",
        "AUTHORITY": "mathorn1973/twist-j main",
        "TAG": f"canon-v{version}",
    }
    for field, value in expected.items():
        if fields.get(field) != value:
            fail(f"STATUS.md {field} must be: {value}")
    canon_bytes = (CANON_DIR / "CANON.md").stat().st_size
    if fields.get("CANON_SHA256") != sha256(CANON_DIR / "CANON.md"):
        fail("STATUS.md CANON_SHA256 differs from canon/CANON.md")
    if fields.get("CANON_BYTES") != str(canon_bytes):
        fail("STATUS.md CANON_BYTES differs from canon/CANON.md")
    commit = fields.get("CANON_COMMIT", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        fail("STATUS.md CANON_COMMIT must be a full lowercase SHA")
    if (ROOT / ".git").exists():
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=ROOT
        )
        if result.returncode:
            fail("STATUS.md CANON_COMMIT is not an ancestor of HEAD")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "State: GENESIS" in readme:
        fail("README.md still declares GENESIS while STATUS is ACTIVE")

print(f"CANON PASS v{version} claims={len(claims)}")
