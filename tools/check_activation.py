#!/usr/bin/env python3
"""Full Public Canon activation gate and deterministic dry-run manifest."""

from __future__ import annotations

import argparse
import csv
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys

try:
    from generate_canon_views import generated_views
except ModuleNotFoundError:  # imported as tools.check_activation in tests
    from tools.generate_canon_views import generated_views


EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
EVIDENCE_FIELDS = (
    "claim_id", "evidence_id", "evidence_kind", "location", "sha256",
    "hash_mode", "architecture_requirement",
)
REQUIRED_RECORD_FIELDS = {
    "candidate_commit", "run_base_commit", "reproduction", "verifier_sha256",
    "expected_sha256", "command", "platform", "architecture", "python",
    "exit_code", "stdout_sha256", "stdout_bytes", "stdout_lines",
    "stderr_sha256", "stderr_bytes", "result",
}
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
FORMAL_RECORD = re.compile(
    r"^reproduce/[a-z0-9][a-z0-9-]*/RUNS/(aarch64|x86_64)\.md$"
)
ACTIVATION_METADATA = {"STATUS.md", "README.md", "CITATION.cff"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def post_content_path_allowed(path: str, dry_run: bool) -> bool:
    return bool(FORMAL_RECORD.fullmatch(path)) or (
        not dry_run and path in ACTIVATION_METADATA
    )


def activation_delta_blockers(changed: list[str], dry_run: bool) -> list[str]:
    if dry_run:
        return []
    actual = set(changed)
    if actual == ACTIVATION_METADATA:
        return []
    missing = sorted(ACTIVATION_METADATA - actual)
    extra = sorted(actual - ACTIVATION_METADATA)
    details: list[str] = []
    if missing:
        details.append("missing " + ", ".join(missing))
    if extra:
        details.append("extra " + ", ".join(extra))
    return ["active release delta must be exactly STATUS.md, README.md, "
            "and CITATION.cff (" + "; ".join(details) + ")"]


def git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(["git", *args], cwd=root, capture_output=True)


def read_status(root: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*?)\s*$")
    for line in (root / "STATUS.md").read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def read_evidence(root: Path) -> list[dict[str, str]]:
    path = root / "canon" / "EVIDENCE.tsv"
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != EVIDENCE_FIELDS:
            raise ValueError("EVIDENCE.tsv schema mismatch")
        return list(reader)


def parse_record(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    missing = sorted(REQUIRED_RECORD_FIELDS - set(fields))
    if missing:
        raise ValueError(f"{path} lacks fields: {', '.join(missing)}")
    return fields


def validate_record(
    root: Path,
    reproduction: str,
    architecture: str,
    content_commit: str | None = None,
) -> list[str]:
    blockers: list[str] = []
    directory = root / "reproduce" / reproduction
    record_path = directory / "RUNS" / f"{architecture}.md"
    relative_record = record_path.relative_to(root).as_posix()
    if not record_path.is_file():
        return [f"{reproduction} lacks {architecture} formal record"]
    try:
        fields = parse_record(record_path)
    except ValueError as error:
        return [str(error)]
    verifier = directory / "verify.py"
    expected_path = directory / "EXPECTED.txt"
    verifier_bytes = verifier.read_bytes()
    expected = expected_path.read_bytes()
    candidate = fields["candidate_commit"]
    run_base = fields["run_base_commit"]
    expected_command = f"python3 reproduce/{reproduction}/verify.py"
    exact = {
        "reproduction": reproduction,
        "architecture": architecture,
        "verifier_sha256": sha256_bytes(verifier_bytes),
        "expected_sha256": sha256_bytes(expected),
        "command": expected_command,
        "exit_code": "0",
        "stdout_sha256": sha256_bytes(expected),
        "stdout_bytes": str(len(expected)),
        "stdout_lines": str(len(expected.splitlines())),
        "stderr_sha256": EMPTY_SHA256,
        "stderr_bytes": "0",
        "result": "PASS",
    }
    for field, value in exact.items():
        if fields[field] != value:
            blockers.append(f"{relative_record} {field} mismatch")
    if not fields["platform"] or re.search(r"jas|twister", fields["platform"], re.IGNORECASE):
        blockers.append(f"{relative_record} platform is not neutral")
    if not fields["python"]:
        blockers.append(f"{relative_record} has empty Python version")
    for field, commit in (("candidate_commit", candidate), ("run_base_commit", run_base)):
        if not SHA40.fullmatch(commit):
            blockers.append(f"{relative_record} has invalid {field}")
            continue
        if git(root, "cat-file", "-e", f"{commit}^{{commit}}").returncode:
            blockers.append(f"{relative_record} {field} is unavailable")
    head = git(root, "rev-parse", "HEAD").stdout.decode().strip()
    if SHA40.fullmatch(candidate):
        if git(root, "merge-base", "--is-ancestor", candidate, head).returncode:
            blockers.append(f"{relative_record} candidate is not an ancestor")
        if SHA40.fullmatch(run_base) and git(
            root, "merge-base", "--is-ancestor", candidate, run_base
        ).returncode:
            blockers.append(f"{relative_record} run base predates candidate")
        if content_commit and SHA40.fullmatch(content_commit) and git(
            root, "merge-base", "--is-ancestor", candidate, content_commit
        ).returncode:
            blockers.append(f"{relative_record} candidate is newer than content commit")
        for relative, current in (
            (f"reproduce/{reproduction}/verify.py", verifier_bytes),
            (f"reproduce/{reproduction}/EXPECTED.txt", expected),
        ):
            pinned = git(root, "show", f"{candidate}:{relative}")
            if pinned.returncode or pinned.stdout != current:
                blockers.append(f"{relative_record} differs from candidate {relative}")
    if SHA40.fullmatch(run_base) and git(root, "merge-base", "--is-ancestor", run_base, head).returncode:
        blockers.append(f"{relative_record} run base is not an ancestor")
    return blockers


def architecture_blockers(root: Path, content_commit: str | None = None) -> list[str]:
    rows = read_evidence(root)
    required = sorted({
        Path(row["location"]).name
        for row in rows
        if row["architecture_requirement"] == "two-architecture"
        and row["evidence_kind"] == "REPRODUCTION"
    })
    blockers: list[str] = []
    pairs: set[tuple[str, str]] = set()
    for reproduction in required:
        for architecture in ("aarch64", "x86_64"):
            pairs.add((reproduction, architecture))
    reproduce = root / "reproduce"
    if reproduce.is_dir():
        for record in reproduce.glob("*/RUNS/*.md"):
            pairs.add((record.parents[1].name, record.stem))
    for reproduction, architecture in sorted(pairs):
        blockers.extend(
            validate_record(root, reproduction, architecture, content_commit)
        )
    return blockers


def view_blockers(root: Path) -> list[str]:
    views = generated_views(root)
    blockers: list[str] = []
    frontier = (root / "canon" / "FRONTIER.md").read_text(encoding="utf-8")
    core = (root / "canon" / "CORE.md").read_text(encoding="utf-8")
    changelog = (root / "canon" / "CHANGELOG.md").read_text(encoding="utf-8")
    counts = root / "canon" / "STATUS_COUNTS.tsv"
    if frontier != views["FRONTIER.md"]:
        blockers.append("canon/FRONTIER.md is not the generated registry view")
    if (
        core.count("<!-- BEGIN GENERATED CORE CLAIMS -->") != 1
        or core.count("<!-- END GENERATED CORE CLAIMS -->") != 1
        or views["CORE_CLAIMS.md"] not in core
    ):
        blockers.append("canon/CORE.md lacks the generated core claim block")
    if (
        changelog.count("<!-- BEGIN GENERATED GENESIS COUNTS -->") != 1
        or changelog.count("<!-- END GENERATED GENESIS COUNTS -->") != 1
        or views["CHANGELOG_COUNTS.md"] not in changelog
    ):
        blockers.append("canon/CHANGELOG.md lacks the generated Genesis count block")
    if not counts.is_file() or counts.read_text(encoding="utf-8") != views["STATUS_COUNTS.tsv"]:
        blockers.append("canon/STATUS_COUNTS.tsv is not the generated status view")
    return blockers


def artifact_blockers(root: Path) -> list[str]:
    required = (
        "notes/genesis/recon/RECONSTRUCTION.tsv",
        "notes/genesis/recon/FRONTIER_SPLITS.tsv",
        "data/EXTERNAL_SOURCES.tsv",
        "data/ENGINEERING_DISPOSITION.tsv",
        "notes/ENGINEERING.md",
        "notes/prereg/post-genesis/01-curvature.md",
        "notes/prereg/post-genesis/02-tm-sym2.md",
        "notes/prereg/post-genesis/03-qenv.md",
        "notes/prereg/post-genesis/04-color-measure.md",
        "notes/prereg/post-genesis/05-spin-lift.md",
        "notes/prereg/post-genesis/06-bell-boundary.md",
    )
    return [f"missing Genesis artifact {path}" for path in required if not (root / path).is_file()]


def status_blockers(
    root: Path, dry_run: bool, post_activation: bool, content_commit: str
) -> list[str]:
    fields = read_status(root)
    blockers: list[str] = []
    head = git(root, "rev-parse", "HEAD").stdout.decode().strip()
    if git(root, "status", "--porcelain").stdout.strip():
        blockers.append("activation gate requires a clean worktree")
    if dry_run:
        if fields.get("STATE") != "GENESIS":
            blockers.append("dry-run activation requires STATE: GENESIS")
        if git(root, "tag", "--list", "canon-v1").stdout.strip():
            blockers.append("canon-v1 tag already exists during Genesis")
    else:
        if fields.get("STATE") != "ACTIVE":
            blockers.append("activation gate requires STATE: ACTIVE")
        if not SHA40.fullmatch(fields.get("CONTENT_COMMIT", "")):
            blockers.append("STATUS.md lacks valid CONTENT_COMMIT")
        if fields.get("CONTENT_COMMIT") and fields["CONTENT_COMMIT"] != content_commit:
            blockers.append("STATUS.md CONTENT_COMMIT differs from requested content commit")
        canon_bytes = (root / "canon" / "CANON.md").read_bytes()
        exact = {
            "CANON": "Public Canon v1",
            "AUTHORITY": "mathorn1973/twist-j main",
            "TAG": "canon-v1",
            "CANON_SHA256": sha256_bytes(canon_bytes),
            "CANON_BYTES": str(len(canon_bytes)),
        }
        for field, value in exact.items():
            if fields.get(field) != value:
                blockers.append(f"STATUS.md {field} must be {value}")
        try:
            date.fromisoformat(fields.get("CUTOVER", ""))
        except ValueError:
            blockers.append("STATUS.md CUTOVER must be an ISO date")
    if not SHA40.fullmatch(content_commit):
        blockers.append("content commit must be a full lowercase SHA")
        return blockers
    if git(root, "cat-file", "-e", f"{content_commit}^{{commit}}").returncode:
        blockers.append("content commit is unavailable")
        return blockers
    if git(root, "merge-base", "--is-ancestor", content_commit, head).returncode:
        blockers.append("content commit is not an ancestor of HEAD")
    changed = git(root, "diff", "--name-only", f"{content_commit}..HEAD").stdout.decode().splitlines()
    illegal = [
        path for path in changed
        if not post_content_path_allowed(path, dry_run)
    ]
    if illegal:
        blockers.append(
            "content bundle changes after content commit: " + ", ".join(illegal)
        )
    blockers.extend(activation_delta_blockers(changed, dry_run))
    if post_activation:
        tag = git(root, "rev-parse", "canon-v1^{}")
        if tag.returncode:
            blockers.append("post-activation readback lacks tag canon-v1")
        else:
            activation_commit = tag.stdout.decode().strip()
            if git(root, "merge-base", "--is-ancestor", content_commit, activation_commit).returncode:
                blockers.append("content commit is not an ancestor of activation tag")
            if git(root, "merge-base", "--is-ancestor", activation_commit, head).returncode:
                blockers.append("activation tag is not an ancestor of HEAD")
    return blockers


def run_script(root: Path, script: str, *args: str) -> tuple[bool, str]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, f"tools/{script}", *args],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
    )
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def neutral_platform() -> str:
    fields: dict[str, str] = {}
    path = Path("/etc/os-release")
    if path.is_file():
        for raw in path.read_text(encoding="utf-8").splitlines():
            if "=" in raw:
                key, value = raw.split("=", 1)
                fields[key] = value.strip().strip('"')
    name = {"ubuntu": "Ubuntu", "debian": "Debian"}.get(
        fields.get("ID", "").lower(), fields.get("NAME", platform.system())
    )
    return f"{name} {fields.get('VERSION_ID', platform.release())}".strip()


def normalized_architecture() -> str:
    return {"amd64": "x86_64", "arm64": "aarch64"}.get(
        platform.machine().lower(), platform.machine().lower()
    )


def manifest(
    root: Path, content_commit: str, activation_commit: str, dry_run: bool
) -> dict[str, object]:
    tracked = git(root, "ls-files", "-z")
    if not tracked.returncode:
        paths = [
            root / relative.decode("utf-8")
            for relative in tracked.stdout.split(b"\0") if relative
        ]
    else:
        paths = []
        for relative in (
            "STATUS.md", "POLICY.md", "AGENTS.md", "README.md",
            "CITATION.cff", "LICENSE", ".gitattributes", ".gitignore",
        ):
            path = root / relative
            if path.is_file():
                paths.append(path)
        for name in ("canon", "data", "reproduce", "tools", "notes", "legacy", ".github"):
            directory = root / name
            if directory.is_dir():
                paths.extend(path for path in directory.rglob("*") if path.is_file())
    paths = [
        path for path in paths
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    ]
    files = []
    for path in sorted(set(paths)):
        relative = path.relative_to(root).as_posix()
        data = path.read_bytes()
        files.append({"path": relative, "sha256": sha256_bytes(data), "bytes": len(data)})
    fields = read_status(root)
    return {
        "schema": "twistj-activation-manifest-v1",
        "mode": "dry-run" if dry_run else "active",
        "state": fields.get("STATE", ""),
        "content_commit": content_commit,
        "activation_commit": activation_commit,
        "platform": neutral_platform(),
        "architecture": normalized_architecture(),
        "python": platform.python_version(),
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--post-activation", action="store_true")
    parser.add_argument("--content-commit")
    parser.add_argument("--manifest-out", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    head = git(root, "rev-parse", "HEAD").stdout.decode().strip()
    fields = read_status(root)
    if args.dry_run and args.post_activation:
        parser.error("--dry-run and --post-activation are mutually exclusive")
    if args.content_commit:
        content_commit = args.content_commit
    elif args.dry_run:
        content_commit = head
    else:
        content_commit = fields.get("CONTENT_COMMIT", "")
    blockers: list[str] = []

    checks = ("check_policy.py", "check_canon.py", "check_ledger.py")
    for script in checks:
        passed, output = run_script(root, script)
        print(output)
        if not passed:
            blockers.append(f"{script} failed")

    missing_artifacts = artifact_blockers(root)
    blockers.extend(missing_artifacts)
    if not missing_artifacts:
        for script in (
            "check_genesis_recon.py", "check_external_sources.py",
            "check_preregistration.py",
        ):
            passed, output = run_script(root, script)
            print(output)
            if not passed:
                blockers.append(f"{script} failed")

    if args.full:
        passed, output = run_script(root, "check_reproduce.py")
        print(output)
        if not passed:
            blockers.append("full reproduction replay failed")

    try:
        blockers.extend(view_blockers(root))
        blockers.extend(architecture_blockers(root, content_commit))
    except (RuntimeError, ValueError) as error:
        blockers.append(str(error))
    blockers.extend(
        status_blockers(root, args.dry_run, args.post_activation, content_commit)
    )

    activation_commit = "NOT_DECLARED"
    if args.post_activation:
        tagged = git(root, "rev-parse", "canon-v1^{}")
        if not tagged.returncode:
            activation_commit = tagged.stdout.decode().strip()
    elif not args.dry_run:
        activation_commit = "PENDING_ACTIVATION_MERGE"

    if args.manifest_out is not None:
        output = args.manifest_out.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(
                manifest(root, content_commit, activation_commit, args.dry_run),
                indent=2,
                sort_keys=True,
            ) + "\n",
            encoding="utf-8",
        )
        print(f"ACTIVATION MANIFEST {output}")

    if blockers:
        print(f"ACTIVATION BLOCKED blockers={len(blockers)}")
        for blocker in blockers:
            print(f"- {blocker}")
        raise SystemExit(1)
    print(f"ACTIVATION PASS mode={'dry-run' if args.dry_run else 'active'} full={args.full}")


if __name__ == "__main__":
    main()
