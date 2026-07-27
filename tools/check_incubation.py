#!/usr/bin/env python3
"""Validate visible, non-canonical incubation contracts.

This checker validates repository syntax and collisions only. It does not prove
mathematical equivalence of scopes or what any agent saw outside Git.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INCUBATION = Path("notes/incubation")
CANDIDATE = re.compile(r"^C-(?:[A-Z0-9]+-)+[1-9][0-9]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CLAIM_ID = re.compile(r"^[A-Z][A-Z0-9-]*$")
PROBE_ID = re.compile(r"^P-[A-Z0-9][A-Z0-9-]*$")
PROBE_BRANCH = re.compile(r"^probe/P-[A-Z0-9][A-Z0-9-]*$")
RESULTS = {"candidate-T", "candidate-D", "candidate-C", "NEGATIVE", "STOP"}
CLAIM_FIELDS = (
    "incubation_id",
    "object_key",
    "claim_key",
    "claim_issue",
    "owner_session",
    "builder_session",
    "status",
    "scope",
    "excluded_scope",
    "dependencies",
    "action_layer",
)
PROMO_FIELDS = (
    "incubation_id",
    "target_issue",
    "target_branch",
    "target_probe_id",
    "target_claim_id",
)
FORBIDDEN_ALTERNATIVES = (" or ", "|", "*", "?", "[", "]", ",")
FORBIDDEN_RUN_FIELDS = {
    "host",
    "hostname",
    "machine",
    "machine_name",
    "machine_nickname",
    "runner_name",
}
PRIVATE_IPV4 = re.compile(
    r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
    r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
)
FIELD = re.compile(r"^([a-z][a-z0-9_]*):[ \t]*(.*?)[ \t]*$")


def parse_fields(path: Path) -> tuple[dict[str, str], dict[str, int]]:
    values: dict[str, str] = {}
    counts: dict[str, int] = defaultdict(int)
    for raw in path.read_text(encoding="utf-8").splitlines():
        match = FIELD.fullmatch(raw)
        if not match:
            continue
        key, value = match.groups()
        counts[key] += 1
        if counts[key] == 1:
            values[key] = value
    return values, dict(counts)


def require_fields(
    path: Path,
    required: tuple[str, ...],
    errors: list[str],
) -> dict[str, str]:
    values, counts = parse_fields(path)
    for field in required:
        count = counts.get(field, 0)
        if count != 1:
            errors.append(
                f"{path.as_posix()}: field {field} appears {count} times, must be exactly 1"
            )
        elif not values[field]:
            errors.append(f"{path.as_posix()}: field {field} is empty")
    return values


def has_alternative(value: str) -> bool:
    lowered = f" {value.lower()} "
    return any(token in lowered if token == " or " else token in value
               for token in FORBIDDEN_ALTERNATIVES)


def check_claim(path: Path, candidate: str, errors: list[str]) -> None:
    values = require_fields(path, CLAIM_FIELDS, errors)
    if not values:
        return
    if values.get("incubation_id") not in {None, candidate}:
        errors.append(f"{path.as_posix()}: incubation_id must equal {candidate}")
    if values.get("status") not in {None, "NO-AUTHORITY"}:
        errors.append(f"{path.as_posix()}: status must be NO-AUTHORITY")
    issue = values.get("claim_issue")
    if issue and not re.fullmatch(r"[1-9][0-9]*", issue):
        errors.append(f"{path.as_posix()}: claim_issue must be a positive integer")
    object_key = values.get("object_key")
    if object_key and ("\t" in object_key or object_key != object_key.strip()):
        errors.append(f"{path.as_posix()}: object_key has invalid whitespace")
    for field in ("claim_key", "owner_session", "builder_session"):
        value = values.get(field)
        if value and any(ch.isspace() for ch in value):
            errors.append(f"{path.as_posix()}: {field} must be one token")


def check_prereg(path: Path, errors: list[str]) -> None:
    values, counts = parse_fields(path)
    revision_count = counts.get("prereg_revision", 0)
    if revision_count != 1:
        errors.append(
            f"{path.as_posix()}: field prereg_revision appears {revision_count} times, "
            "must be exactly 1"
        )
    elif values.get("prereg_revision") not in {"1", "2"}:
        errors.append(f"{path.as_posix()}: prereg_revision must be 1 or 2")
    digest_count = counts.get("prereg_sha256", 0)
    if digest_count > 1:
        errors.append(
            f"{path.as_posix()}: field prereg_sha256 appears {digest_count} times, "
            "must appear at most once"
        )
    digest = values.get("prereg_sha256")
    if digest and not SHA256.fullmatch(digest):
        errors.append(f"{path.as_posix()}: prereg_sha256 must contain 64 lowercase hex digits")


def check_breaker(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    if "verify.py" in lowered or re.search(r"\b(?:from|import)\s+verify\b", lowered):
        errors.append(
            f"{path.as_posix()}: PREMATURE-VERIFIER-DISCLOSURE / STOP: "
            "break.py visibly references verify.py"
        )
    values, counts = parse_fields(path)
    count = counts.get("breaker_session", 0)
    if count != 1:
        errors.append(
            f"{path.as_posix()}: field breaker_session appears {count} times, "
            "must be exactly 1"
        )
    elif not values.get("breaker_session") or any(
        ch.isspace() for ch in values["breaker_session"]
    ):
        errors.append(f"{path.as_posix()}: breaker_session must be one nonempty token")


def check_result(path: Path, errors: list[str]) -> None:
    values, counts = parse_fields(path)
    count = counts.get("result", 0)
    if count != 1:
        errors.append(
            f"{path.as_posix()}: field result appears {count} times, must be exactly 1"
        )
    elif values.get("result") not in RESULTS:
        errors.append(f"{path.as_posix()}: invalid incubation result {values.get('result')!r}")


def check_promo(
    path: Path,
    candidate: str,
    claims: dict[str, list[str]],
    errors: list[str],
) -> None:
    values = require_fields(path, PROMO_FIELDS, errors)
    if not values:
        return
    if values.get("incubation_id") not in {None, candidate}:
        errors.append(f"{path.as_posix()}: incubation_id must equal {candidate}")
    for field in PROMO_FIELDS[1:]:
        value = values.get(field)
        if not value:
            continue
        if has_alternative(value):
            errors.append(
                f"{path.as_posix()}: PROMO-TARGET-AMBIGUOUS / STOP: "
                f"{field} contains an alternative"
            )
        if value != "NONE":
            claims[f"{field}={value}"].append(candidate)
    issue = values.get("target_issue")
    if issue and issue != "NONE" and not re.fullmatch(r"[1-9][0-9]*", issue):
        errors.append(f"{path.as_posix()}: target_issue must be NONE or a positive integer")
    branch = values.get("target_branch")
    if branch and branch != "NONE" and not PROBE_BRANCH.fullmatch(branch):
        errors.append(f"{path.as_posix()}: target_branch must be NONE or probe/P-NAME")
    probe = values.get("target_probe_id")
    if probe and probe != "NONE" and not PROBE_ID.fullmatch(probe):
        errors.append(f"{path.as_posix()}: target_probe_id must be NONE or P-NAME")
    claim = values.get("target_claim_id")
    if claim and claim != "NONE" and not CLAIM_ID.fullmatch(claim):
        errors.append(f"{path.as_posix()}: target_claim_id must be NONE or a claim identifier")


def check_run_records(root: Path, errors: list[str]) -> None:
    paths: list[Path] = []
    for base in (root / "probes", root / "reproduce"):
        if base.exists():
            paths.extend(path for path in base.rglob("*.md") if path.name.startswith("RUN"))
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        if PRIVATE_IPV4.search(text) or ".local" in text.lower():
            errors.append(f"{path.relative_to(root).as_posix()}: private infrastructure is forbidden")
        for number, raw in enumerate(text.splitlines(), 1):
            match = FIELD.fullmatch(raw)
            if match and match.group(1) in FORBIDDEN_RUN_FIELDS:
                errors.append(
                    f"{path.relative_to(root).as_posix()}:{number}: "
                    f"forbidden run-record field {match.group(1)}"
                )


def findings(root: Path = ROOT) -> tuple[list[str], int]:
    errors: list[str] = []
    incubation = root / INCUBATION
    candidates: list[Path] = []
    if incubation.exists():
        for path in sorted(item for item in incubation.iterdir() if item.is_dir()):
            if not CANDIDATE.fullmatch(path.name):
                errors.append(f"{path.relative_to(root).as_posix()}: invalid candidate directory name")
            else:
                candidates.append(path)

    promotion_claims: dict[str, list[str]] = defaultdict(list)
    for candidate_path in candidates:
        candidate = candidate_path.name
        claim = candidate_path / "CLAIM.md"
        prereg = candidate_path / "PREREG.md"
        verifier = candidate_path / "verify.py"
        result = candidate_path / "RESULT.md"
        for required in (claim, prereg, verifier, result):
            if not required.is_file():
                errors.append(f"{required.relative_to(root).as_posix()}: missing required file")
        if claim.is_file():
            check_claim(claim.relative_to(root), candidate, errors)
        if prereg.is_file():
            check_prereg(prereg.relative_to(root), errors)
        breaker = candidate_path / "break.py"
        if breaker.is_file():
            check_breaker(breaker.relative_to(root), errors)
        if result.is_file():
            check_result(result.relative_to(root), errors)
        promo = candidate_path / "PROMO.md"
        if promo.is_file():
            check_promo(promo.relative_to(root), candidate, promotion_claims, errors)

    for target, owners in sorted(promotion_claims.items()):
        if len(owners) > 1:
            errors.append(
                f"PROMO-NAME-COLLISION / STOP: {target} claimed by "
                + " and ".join(sorted(owners))
            )

    check_run_records(root, errors)
    return errors, len(candidates)


def main() -> None:
    errors, candidate_count = findings()
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    if candidate_count == 0:
        print("INCUBATION NOT APPLICABLE")
    else:
        print(f"INCUBATION PASS candidates={candidate_count}")


if __name__ == "__main__":
    main()
