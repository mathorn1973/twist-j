#!/usr/bin/env python3
"""Validate auditable non-canonical incubation contracts.

The checker validates repository syntax, Git ancestry, and target collisions.
It does not prove mathematical equivalence of scopes or information exchanged
outside Git.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
INCUBATION = Path("notes/incubation")
CANDIDATE = re.compile(r"^C-(?:[A-Z0-9]+-)+[1-9][0-9]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA = re.compile(r"^[0-9a-f]{40}$")
CLAIM_ID = re.compile(r"^[A-Z][A-Z0-9-]*$")
PROBE_ID = re.compile(r"^P-[A-Z0-9][A-Z0-9-]*$")
PROBE_BRANCH = re.compile(r"^probe/P-[A-Z0-9][A-Z0-9-]*$")
RESULTS = {"candidate-T", "candidate-D", "candidate-C", "NEGATIVE", "STOP"}
CLAIM_FIELDS = (
    "incubation_id", "object_key", "claim_key", "claim_issue",
    "owner_session", "builder_session", "status", "scope",
    "excluded_scope", "dependencies", "action_layer",
)
PROMO_FIELDS = (
    "incubation_id", "target_issue", "target_branch",
    "target_probe_id", "target_claim_id",
)
FORBIDDEN_ALTERNATIVES = (" or ", "|", "*", "?", "[", "]", ",")
FIELD = re.compile(r"^([a-z][a-z0-9_]*):[ \t]*(.*?)[ \t]*$")
PY_CONSTANT = {
    "breaker_session": re.compile(
        r"(?m)^BREAKER_SESSION\s*=\s*['\"]([A-Za-z0-9._:-]+)['\"]\s*$"
    ),
    "prereg_revision": re.compile(r"(?m)^PREREG_REVISION\s*=\s*([12])\s*$"),
    "prereg_sha256": re.compile(
        r"(?m)^PREREG_SHA256\s*=\s*['\"]([0-9a-f]{64})['\"]\s*$"
    ),
}
VERIFIER_PATH = re.compile(r"(?:^|/)verify-r[12]\.py$")
ALLOWED_CANDIDATE_ROOT = {
    "CLAIM.md", "PREREG-r1.md", "PREREG-r2.md",
    "verify-r1.py", "verify-r2.py", "BREAK-r1.md", "BREAK-r2.md",
    "RESULT.md", "PROMO.md",
}
RUN_FIELDS = (
    "run_format", "candidate_commit", "prereg_sha256", "verifier_sha256",
    "expected_sha256", "stdout_sha256", "expected_bytes", "stdout_bytes",
    "stderr_bytes", "exit_code", "command", "platform", "architecture", "python",
)
RUN_PLATFORMS = {"Ubuntu 24.04"}
RUN_ARCHITECTURES = {"x86_64", "aarch64"}
PRIVATE_IPV4 = re.compile(
    r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|"
    r"172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
)
MDNS_HOST = re.compile(r"(?<![/A-Za-z0-9_.-])(?:[A-Za-z0-9-]+\.)+local\b", re.I)


class GitError(RuntimeError):
    pass


def git(root: Path, *args: str) -> str:
    process = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    if process.returncode != 0:
        raise GitError(process.stderr.strip() or "git command failed")
    return process.stdout


def is_git_repository(root: Path) -> bool:
    try:
        return git(root, "rev-parse", "--is-inside-work-tree").strip() == "true"
    except GitError:
        return False


def parse_fields(path: Path, errors: list[str]) -> tuple[dict[str, str], dict[str, int]]:
    values: dict[str, str] = {}
    counts: dict[str, int] = defaultdict(int)
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw.strip()
        stripped_match = FIELD.fullmatch(stripped)
        if stripped_match and raw != stripped:
            errors.append(f"{path.as_posix()}:{number}: indented manifest field")
            continue
        match = FIELD.fullmatch(raw)
        if not match:
            continue
        key, value = match.groups()
        counts[key] += 1
        if counts[key] == 1:
            values[key] = value
    return values, dict(counts)


def require_fields(
    path: Path, required: tuple[str, ...], errors: list[str]
) -> tuple[dict[str, str], dict[str, int]]:
    values, counts = parse_fields(path, errors)
    for field in required:
        count = counts.get(field, 0)
        if count != 1:
            errors.append(
                f"{path.as_posix()}: field {field} appears {count} times, must be exactly 1"
            )
        elif not values[field]:
            errors.append(f"{path.as_posix()}: field {field} is empty")
    return values, counts


def has_alternative(value: str) -> bool:
    lowered = f" {value.lower()} "
    return any(
        token in lowered if token == " or " else token in value
        for token in FORBIDDEN_ALTERNATIVES
    )


def check_claim(path: Path, candidate: str, errors: list[str]) -> None:
    values, _ = require_fields(path, CLAIM_FIELDS, errors)
    if values.get("incubation_id") not in {None, candidate}:
        errors.append(f"{path.as_posix()}: incubation_id must equal {candidate}")
    if values.get("status") not in {None, "NO-AUTHORITY"}:
        errors.append(f"{path.as_posix()}: status must be NO-AUTHORITY")
    issue = values.get("claim_issue")
    if issue and not re.fullmatch(r"[1-9][0-9]*", issue):
        errors.append(f"{path.as_posix()}: claim_issue must be a positive integer")
    for field in ("object_key", "claim_key", "owner_session", "builder_session"):
        value = values.get(field)
        if value and any(ch.isspace() for ch in value):
            errors.append(f"{path.as_posix()}: {field} must be one token")


def check_prereg(path: Path, revision: int, errors: list[str]) -> None:
    values, counts = parse_fields(path, errors)
    count = counts.get("prereg_revision", 0)
    if count != 1:
        errors.append(
            f"{path.as_posix()}: field prereg_revision appears {count} times, must be exactly 1"
        )
    elif values.get("prereg_revision") != str(revision):
        errors.append(f"{path.as_posix()}: prereg_revision must be {revision}")


def parse_python_breaker(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    result: dict[str, str] = {}
    for field, pattern in PY_CONSTANT.items():
        matches = pattern.findall(text)
        if len(matches) != 1:
            errors.append(
                f"{path.as_posix()}: {field} declaration appears {len(matches)} times, "
                "must be exactly 1"
            )
        else:
            result[field] = matches[0]
    return result


def parse_break_report(path: Path, errors: list[str]) -> dict[str, str]:
    required = (
        "breaker_session", "prereg_revision", "prereg_sha256",
        "stop_reason", "missing_types",
    )
    values, _ = require_fields(path, required, errors)
    if values.get("stop_reason") not in {None, "BLIND-BREAKER-UNDERSPECIFIED"}:
        errors.append(
            f"{path.as_posix()}: stop_reason must be BLIND-BREAKER-UNDERSPECIFIED"
        )
    if values.get("missing_types") in {None, "", "NONE", "none"}:
        errors.append(f"{path.as_posix()}: missing_types must be nonempty")
    if values.get("prereg_sha256") and not SHA256.fullmatch(values["prereg_sha256"]):
        errors.append(f"{path.as_posix()}: prereg_sha256 must be 64 lowercase hex digits")
    return values


def path_history(root: Path, relative: str) -> list[str]:
    output = git(root, "log", "--format=%H", "--", relative)
    return [line for line in output.splitlines() if line]


def add_commit(root: Path, relative: str) -> str:
    output = git(root, "log", "--diff-filter=A", "--format=%H", "--reverse", "--", relative)
    commits = [line for line in output.splitlines() if line]
    if len(commits) != 1:
        raise GitError(f"{relative}: expected one add commit, found {len(commits)}")
    return commits[0]


def commit_parents(root: Path, commit: str) -> list[str]:
    return [item for item in git(root, "show", "-s", "--format=%P", commit).split() if item]


def changed_paths_at_commit(root: Path, commit: str) -> list[str]:
    output = git(
        root,
        "diff-tree",
        "--root",
        "--no-commit-id",
        "--name-only",
        "-r",
        commit,
    )
    return sorted(line for line in output.splitlines() if line)


def file_at_commit(root: Path, commit: str, relative: str) -> bytes:
    process = subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{relative}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if process.returncode != 0:
        raise GitError(process.stderr.decode("utf-8", errors="replace").strip())
    return process.stdout


def verifier_in_ancestry(root: Path, commit: str, candidate_relative: str) -> str | None:
    commits = [line for line in git(root, "rev-list", commit).splitlines() if line]
    for ancestor in commits:
        names = git(root, "ls-tree", "-r", "--name-only", ancestor, "--", candidate_relative)
        for name in names.splitlines():
            if VERIFIER_PATH.search(name):
                return f"{ancestor}:{name}"
    return None


def check_frozen_history(root: Path, relative: str, errors: list[str]) -> None:
    try:
        history = path_history(root, relative)
    except GitError as exc:
        errors.append(f"{relative}: GIT-DAG-UNAVAILABLE / STOP: {exc}")
        return
    if len(history) != 1:
        errors.append(f"{relative}: frozen file has {len(history)} content commits, must have 1")


def check_breaker_dag(
    root: Path,
    candidate_relative: str,
    artifact_relative: str,
    metadata: dict[str, str],
    revision: int,
    errors: list[str],
) -> None:
    if not is_git_repository(root):
        errors.append(f"{artifact_relative}: GIT-DAG-UNAVAILABLE / STOP")
        return
    if metadata.get("prereg_revision") not in {None, str(revision)}:
        errors.append(f"{artifact_relative}: prereg_revision must be {revision}")
    prereg_relative = f"{candidate_relative}/PREREG-r{revision}.md"
    try:
        artifact_commit = add_commit(root, artifact_relative)
        prereg_commit = add_commit(root, prereg_relative)
        parents = commit_parents(root, artifact_commit)
        if parents != [prereg_commit]:
            errors.append(
                f"{artifact_relative}: BREAKER-NOT-DIRECT-CHILD / STOP: "
                f"freeze commit must be the direct child of {prereg_commit}"
            )
        changed = changed_paths_at_commit(root, artifact_commit)
        if changed != [artifact_relative]:
            errors.append(
                f"{artifact_relative}: BREAKER-FREEZE-SCOPE / STOP: "
                "freeze commit must change exactly the breaker artifact"
            )
        prereg_bytes = file_at_commit(root, artifact_commit, prereg_relative)
        digest = hashlib.sha256(prereg_bytes).hexdigest()
        if metadata.get("prereg_sha256") not in {None, digest}:
            errors.append(
                f"{artifact_relative}: prereg_sha256 does not match {prereg_relative} at add commit"
            )
        leak = verifier_in_ancestry(root, artifact_commit, candidate_relative)
        if leak:
            errors.append(
                f"{artifact_relative}: BREAKER-VERIFIER-ANCESTRY / STOP: verifier reachable at {leak}"
            )
        check_frozen_history(root, artifact_relative, errors)
    except GitError as exc:
        errors.append(f"{artifact_relative}: GIT-DAG-UNAVAILABLE / STOP: {exc}")


def check_result(path: Path, errors: list[str]) -> dict[str, str]:
    values, counts = parse_fields(path, errors)
    count = counts.get("result", 0)
    if count != 1:
        errors.append(
            f"{path.as_posix()}: field result appears {count} times, must be exactly 1"
        )
        return values
    result = values.get("result")
    if result not in RESULTS:
        errors.append(f"{path.as_posix()}: invalid incubation result {result!r}")
    if result == "STOP":
        stop_count = counts.get("stop_reason", 0)
        if stop_count != 1:
            errors.append(
                f"{path.as_posix()}: field stop_reason appears {stop_count} times, must be exactly 1"
            )
    return values


def check_promo(
    path: Path,
    candidate: str,
    claims: dict[str, list[str]],
    errors: list[str],
) -> None:
    values, _ = require_fields(path, PROMO_FIELDS, errors)
    if values.get("incubation_id") not in {None, candidate}:
        errors.append(f"{path.as_posix()}: incubation_id must equal {candidate}")
    for field in PROMO_FIELDS[1:]:
        value = values.get(field)
        if not value:
            continue
        if has_alternative(value):
            errors.append(
                f"{path.as_posix()}: PROMO-TARGET-AMBIGUOUS / STOP: {field} contains an alternative"
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


def check_candidate_shape(candidate_path: Path, root: Path, errors: list[str]) -> None:
    relative = candidate_path.relative_to(root).as_posix()
    for item in sorted(candidate_path.rglob("*")):
        if item.is_dir():
            continue
        subpath = item.relative_to(candidate_path).as_posix()
        if subpath in ALLOWED_CANDIDATE_ROOT:
            continue
        if subpath in {"break/r1/break.py", "break/r2/break.py"}:
            continue
        errors.append(f"{relative}/{subpath}: invalid candidate file path")


def check_run_record(path: Path, root: Path, errors: list[str]) -> None:
    relative = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8")
    for number, raw in enumerate(text.splitlines(), 1):
        if raw and not FIELD.fullmatch(raw):
            errors.append(f"{relative}:{number}: run record must contain field lines only")
    values, counts = parse_fields(path, errors)
    for field in RUN_FIELDS:
        count = counts.get(field, 0)
        if count != 1:
            errors.append(f"{relative}: field {field} appears {count} times, must be exactly 1")
    for field in sorted(set(counts) - set(RUN_FIELDS)):
        errors.append(f"{relative}: unknown run-record field {field}")
    if values.get("run_format") not in {None, "2"}:
        errors.append(f"{relative}: run_format must be 2")
    if values.get("candidate_commit") and not GIT_SHA.fullmatch(values["candidate_commit"]):
        errors.append(f"{relative}: candidate_commit must be 40 lowercase hex digits")
    for field in ("prereg_sha256", "verifier_sha256", "expected_sha256", "stdout_sha256"):
        value = values.get(field)
        if value and not SHA256.fullmatch(value):
            errors.append(f"{relative}: {field} must be 64 lowercase hex digits")
    for field in ("expected_bytes", "stdout_bytes", "stderr_bytes", "exit_code"):
        value = values.get(field)
        if value and not re.fullmatch(r"0|[1-9][0-9]*", value):
            errors.append(f"{relative}: {field} must be a nonnegative integer")
    if values.get("exit_code") not in {None, "0"}:
        errors.append(f"{relative}: exit_code must be 0")
    if values.get("stderr_bytes") not in {None, "0"}:
        errors.append(f"{relative}: stderr_bytes must be 0")
    if values.get("platform") not in {None, *RUN_PLATFORMS}:
        errors.append(f"{relative}: platform is not allowed")
    if values.get("architecture") not in {None, *RUN_ARCHITECTURES}:
        errors.append(f"{relative}: architecture must be x86_64 or aarch64")
    python_version = values.get("python")
    if python_version and not re.fullmatch(r"3\.(?:12|13)\.[0-9]+", python_version):
        errors.append(f"{relative}: python must be an exact supported 3.12 or 3.13 version")
    if PRIVATE_IPV4.search(text) or MDNS_HOST.search(text):
        errors.append(f"{relative}: private infrastructure is forbidden")


def changed_paths_from_git(root: Path, base_sha: str) -> set[str]:
    if not GIT_SHA.fullmatch(base_sha):
        raise GitError("base SHA must contain 40 lowercase hex digits")
    output = git(root, "diff", "--name-only", "--diff-filter=ACMR", f"{base_sha}...HEAD")
    return {line for line in output.splitlines() if line}


def run_record_paths(
    root: Path,
    base_sha: str | None,
    changed_files: set[str] | None,
    errors: list[str],
) -> list[Path]:
    if changed_files is None and base_sha is not None:
        try:
            changed_files = changed_paths_from_git(root, base_sha)
        except GitError as exc:
            errors.append(f"RUN-RECORD-BASE-UNAVAILABLE / STOP: {exc}")
            return []
    paths: list[Path] = []
    for base in (root / "probes", root / "reproduce"):
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if not path.name.startswith("RUN"):
                continue
            relative = path.relative_to(root).as_posix()
            if changed_files is not None:
                if relative in changed_files:
                    paths.append(path)
            else:
                values, _ = parse_fields(path, [])
                if values.get("run_format") == "2":
                    paths.append(path)
    return sorted(paths)


def findings(
    root: Path = ROOT,
    base_sha: str | None = None,
    changed_files: set[str] | None = None,
) -> tuple[list[str], int]:
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
        candidate_relative = candidate_path.relative_to(root).as_posix()
        check_candidate_shape(candidate_path, root, errors)
        claim = candidate_path / "CLAIM.md"
        if not claim.is_file():
            errors.append(f"{claim.relative_to(root).as_posix()}: missing required file")
        else:
            check_claim(claim, candidate, errors)

        sessions: dict[int, str] = {}
        latest_revision = 0
        executable_breakers: set[int] = set()
        reports: set[int] = set()
        for revision in (1, 2):
            prereg = candidate_path / f"PREREG-r{revision}.md"
            verifier = candidate_path / f"verify-r{revision}.py"
            breaker = candidate_path / "break" / f"r{revision}" / "break.py"
            report = candidate_path / f"BREAK-r{revision}.md"
            present = any(path.is_file() for path in (prereg, verifier, breaker, report))
            if present:
                latest_revision = revision
                if not prereg.is_file():
                    errors.append(f"{prereg.relative_to(root).as_posix()}: missing required file")
                else:
                    check_prereg(prereg, revision, errors)
                    if is_git_repository(root):
                        check_frozen_history(root, prereg.relative_to(root).as_posix(), errors)
            if breaker.is_file() and report.is_file():
                errors.append(
                    f"{candidate_relative}: revision {revision} has both executable breaker and STOP report"
                )
            artifact: Path | None = None
            metadata: dict[str, str] = {}
            if breaker.is_file():
                executable_breakers.add(revision)
                artifact = breaker
                metadata = parse_python_breaker(breaker, errors)
            elif report.is_file():
                reports.add(revision)
                artifact = report
                metadata = parse_break_report(report, errors)
            if artifact is not None:
                session = metadata.get("breaker_session")
                if session:
                    sessions[revision] = session
                check_breaker_dag(
                    root,
                    candidate_relative,
                    artifact.relative_to(root).as_posix(),
                    metadata,
                    revision,
                    errors,
                )
            if verifier.is_file() and is_git_repository(root):
                check_frozen_history(root, verifier.relative_to(root).as_posix(), errors)

        if latest_revision == 2:
            if 1 not in reports:
                errors.append(f"{candidate_relative}: revision 2 requires BREAK-r1.md")
            if 1 in sessions and 2 in sessions and sessions[1] == sessions[2]:
                errors.append(f"{candidate_relative}: revision 2 must use a different breaker_session")

        result_path = candidate_path / "RESULT.md"
        result_values: dict[str, str] = {}
        if result_path.is_file():
            result_values = check_result(result_path, errors)
        promo = candidate_path / "PROMO.md"
        if promo.is_file():
            if not result_path.is_file():
                errors.append(f"{result_path.relative_to(root).as_posix()}: required when PROMO.md exists")
            if latest_revision == 0:
                errors.append(f"{candidate_relative}: PROMO.md requires a preregistration revision")
            elif latest_revision not in executable_breakers:
                if not (
                    result_values.get("result") == "STOP"
                    and result_values.get("stop_reason") == "BLIND-BREAKER-UNDERSPECIFIED"
                    and latest_revision in reports
                ):
                    errors.append(
                        f"{candidate_relative}: PROMO.md requires the latest executable breaker or exact underspecified STOP"
                    )
            check_promo(promo, candidate, promotion_claims, errors)

    for target, owners in sorted(promotion_claims.items()):
        if len(owners) > 1:
            errors.append(
                f"PROMO-NAME-COLLISION / STOP: {target} claimed by "
                + " and ".join(sorted(owners))
            )

    for path in run_record_paths(root, base_sha, changed_files, errors):
        check_run_record(path, root, errors)
    return sorted(errors), len(candidates)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", help="base commit for changed RUN record checks")
    args = parser.parse_args()
    errors, candidate_count = findings(base_sha=args.base)
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
