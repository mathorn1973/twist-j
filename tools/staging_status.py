#!/usr/bin/env python3
"""Report the asynchronous Phase A prep/staging pipeline from Git refs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SYNTHESIS_REF = "refs/remotes/origin/synthesis/canon-v1"
STAGING_PREFIX = "refs/remotes/origin/staging/canon-v1-"
PREP_PREFIX = "refs/remotes/origin/prep/canon-v1-"
NAME = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA = re.compile(r"[0-9a-f]{40}")
ARCHITECTURES = {"aarch64", "x86_64"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if check and result.returncode:
        fail(result.stderr.decode("utf-8", "replace").strip() or "git failed")
    return result


def output(*args: str) -> str:
    return git(*args).stdout.decode("utf-8", "replace").strip()


def fetch_pipeline() -> None:
    refspecs = [
        "+refs/heads/synthesis/canon-v1:refs/remotes/origin/synthesis/canon-v1",
        "+refs/heads/staging/canon-v1-*:refs/remotes/origin/staging/canon-v1-*",
        "+refs/heads/prep/canon-v1-*:refs/remotes/origin/prep/canon-v1-*",
    ]
    git("fetch", "--prune", "origin", *refspecs)


def refs(prefix: str) -> list[str]:
    directory = prefix.rsplit("/", 1)[0] + "/"
    raw = output("for-each-ref", "--format=%(refname)", directory)
    return [line for line in raw.splitlines() if line.startswith(prefix)]


def sha(ref: str) -> str:
    value = output("rev-parse", ref)
    if not SHA.fullmatch(value):
        fail(f"invalid commit for {ref}")
    return value


def is_ancestor(older: str, newer: str) -> bool:
    return not git("merge-base", "--is-ancestor", older, newer, check=False).returncode


def changed_paths(older: str, newer: str) -> list[str]:
    raw = output("diff", "--name-only", f"{older}..{newer}")
    return [line for line in raw.splitlines() if line]


def ref_paths(ref: str, prefix: str) -> list[str]:
    raw = output("ls-tree", "-r", "--name-only", ref, "--", prefix)
    return [line for line in raw.splitlines() if line]


def ref_text(ref: str, path: str) -> str:
    result = git("show", f"{ref}:{path}")
    return result.stdout.decode("utf-8")


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


def branch_name(ref: str, prefix: str) -> str:
    name = ref.removeprefix(prefix)
    if not NAME.fullmatch(name):
        fail(f"invalid pipeline branch name: {ref}")
    return name


def first_candidate(synthesis: str, head: str) -> str | None:
    base = output("merge-base", synthesis, head)
    commits = output("rev-list", "--reverse", f"{base}..{head}").splitlines()
    return commits[0] if commits else None


def candidate_reproduction(candidate: str) -> str | None:
    parents = output("show", "-s", "--format=%P", candidate).split()
    if len(parents) != 1:
        return None
    paths = changed_paths(parents[0], candidate)
    names = {
        match.group(1)
        for path in paths
        if (match := re.fullmatch(r"reproduce/([^/]+)/verify\.py", path))
    }
    return next(iter(names)) if len(names) == 1 else None


def staging_entry(ref: str, synthesis: str) -> dict[str, Any]:
    branch_label = branch_name(ref, STAGING_PREFIX)
    head = sha(ref)
    errors: list[str] = []

    all_record_paths = [
        path
        for path in ref_paths(ref, "reproduce")
        if re.fullmatch(r"reproduce/[^/]+/RUNS/[^/]+\.md", path)
    ]
    all_records = [(path, parse_fields(ref_text(ref, path))) for path in all_record_paths]

    candidate = first_candidate(synthesis, head)
    if candidate is None:
        recorded_candidates = {
            fields.get("candidate_commit", "")
            for _, fields in all_records
            if SHA.fullmatch(fields.get("candidate_commit", ""))
            and is_ancestor(fields["candidate_commit"], head)
        }
        if recorded_candidates:
            candidate = min(
                recorded_candidates,
                key=lambda value: int(output("rev-list", "--count", f"{value}..{head}")),
            )
    if candidate is None or not SHA.fullmatch(candidate):
        errors.append("candidate cannot be inferred")

    records = [
        (path, fields)
        for path, fields in all_records
        if fields.get("candidate_commit") == candidate
    ]
    reproductions = {fields.get("reproduction", "") for _, fields in records}
    reproductions.discard("")
    name = next(iter(reproductions)) if len(reproductions) == 1 else None
    if len(reproductions) > 1:
        errors.append("record reproduction mismatch")
    if name is None and candidate and SHA.fullmatch(candidate):
        name = candidate_reproduction(candidate)
    if name is None:
        name = branch_label
    if not NAME.fullmatch(name):
        errors.append("invalid reproduction name")

    architectures: set[str] = set()
    for path, fields in records:
        architecture = fields.get("architecture", "")
        if architecture not in ARCHITECTURES:
            errors.append(f"invalid architecture in {path}")
            continue
        if Path(path).stem != architecture:
            errors.append(f"record filename mismatch in {path}")
        if fields.get("reproduction") != name:
            errors.append(f"record reproduction mismatch in {path}")
        if Path(path).parts[1] != name:
            errors.append(f"record directory mismatch in {path}")
        architectures.add(architecture)

    candidate_parent = None
    if candidate and SHA.fullmatch(candidate):
        parents = output("show", "-s", "--format=%P", candidate).split()
        if len(parents) != 1:
            errors.append("candidate must have exactly one parent")
        else:
            candidate_parent = parents[0]
        if not is_ancestor(candidate, head):
            errors.append("candidate is not an ancestor of staging head")
        illegal = [
            path
            for path in changed_paths(candidate, head)
            if not path.startswith(f"reproduce/{name}/RUNS/")
        ]
        if illegal:
            errors.append("post-candidate mutation: " + ", ".join(illegal))

    integrated = is_ancestor(head, synthesis)
    if errors:
        state = "BLOCKED"
    elif integrated:
        state = "INTEGRATED"
    elif candidate_parent != synthesis:
        state = "STALE_BASE"
    elif architectures == ARCHITECTURES:
        state = "READY_TO_VALIDATE"
    elif architectures == {"aarch64"}:
        state = "WAIT_X86_64"
    elif architectures == {"x86_64"}:
        state = "WAIT_AARCH64"
    elif not architectures:
        state = "WAIT_FIRST_RUN"
    else:
        state = "BLOCKED"
        errors.append("unexpected architecture set")

    return {
        "kind": "staging",
        "name": name,
        "branch_label": branch_label,
        "branch": ref.removeprefix("refs/remotes/origin/"),
        "head": head,
        "candidate": candidate,
        "candidate_parent": candidate_parent,
        "architectures": sorted(architectures),
        "state": state,
        "errors": errors,
    }


def prep_entry(ref: str, synthesis: str) -> dict[str, Any]:
    name = branch_name(ref, PREP_PREFIX)
    head = sha(ref)
    base = output("merge-base", synthesis, head)
    counts = output("rev-list", "--left-right", "--count", f"{synthesis}...{head}").split()
    synthesis_only, prep_only = (int(counts[0]), int(counts[1]))
    changed = changed_paths(base, head)
    illegal_records = [path for path in changed if "/RUNS/" in path]
    errors = []
    if illegal_records:
        errors.append("prep contains formal run records: " + ", ".join(illegal_records))
    if errors:
        state = "BLOCKED"
    elif is_ancestor(head, synthesis):
        state = "INTEGRATED"
    elif synthesis_only:
        state = "REBASE_REQUIRED"
    else:
        state = "PREP_CURRENT"
    return {
        "kind": "prep",
        "name": name,
        "branch": ref.removeprefix("refs/remotes/origin/"),
        "head": head,
        "merge_base": base,
        "synthesis_only": synthesis_only,
        "prep_only": prep_only,
        "state": state,
        "errors": errors,
    }


def next_action(role: str, staging: list[dict[str, Any]], prep: list[dict[str, Any]]) -> dict[str, Any]:
    wanted = {
        "aarch64": "WAIT_AARCH64",
        "x86_64": "WAIT_X86_64",
        "coordinator": "READY_TO_VALIDATE",
    }
    if role in wanted:
        matches = [entry for entry in staging if entry["state"] == wanted[role]]
        if len(matches) > 1:
            return {"role": role, "action": "BLOCKED", "reason": "multiple eligible staging branches"}
        if not matches:
            return {"role": role, "action": "WAIT"}
        entry = matches[0]
        candidate = entry["candidate"]
        if role == "coordinator":
            command = (
                f"python3 tools/check_staged_reproduction.py {entry['name']} "
                f"--candidate {candidate} --require-architectures aarch64 x86_64"
            )
            action = "VALIDATE_AND_FF_ONLY"
        else:
            command = (
                f"python3 tools/run_staged_reproduction.py {entry['name']} "
                f"--candidate {candidate}"
            )
            action = "RUN_FORMAL_RECORD"
        return {
            "role": role,
            "action": action,
            "name": entry["name"],
            "branch": entry["branch"],
            "candidate": candidate,
            "command": command,
        }

    active = [entry for entry in prep if entry["state"] in {"PREP_CURRENT", "REBASE_REQUIRED"}]
    if not active:
        return {"role": role, "action": "WAIT_FOR_PREP_BRANCH"}
    if len(active) > 1:
        return {"role": role, "action": "CHOOSE_QUEUE_ORDER", "branches": [e["branch"] for e in active]}
    entry = active[0]
    action = "REBASE_PREP" if entry["state"] == "REBASE_REQUIRED" else "CONTINUE_PREP"
    return {"role": role, "action": action, "name": entry["name"], "branch": entry["branch"]}


def text_report(synthesis: str, staging: list[dict[str, Any]], prep: list[dict[str, Any]], action: dict[str, Any]) -> None:
    print(f"TIKTOK synthesis={synthesis}")
    for entry in prep + staging:
        fields = [entry["kind"].upper(), entry["name"], entry["state"], f"head={entry['head']}"]
        if entry.get("branch_label") and entry["branch_label"] != entry["name"]:
            fields.append(f"branch_label={entry['branch_label']}")
        if entry.get("candidate"):
            fields.append(f"candidate={entry['candidate']}")
        if entry.get("architectures"):
            fields.append("architectures=" + ",".join(entry["architectures"]))
        print(" ".join(fields))
        for error in entry["errors"]:
            print(f"  ERROR {error}")
    print("NEXT " + " ".join(f"{key}={value}" for key, value in action.items()))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true", help="fetch synthesis, prep, and staging refs first")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--role",
        choices=("builder", "aarch64", "x86_64", "coordinator"),
        default="builder",
    )
    parser.add_argument("--strict", action="store_true", help="exit nonzero when any branch is blocked or stale")
    args = parser.parse_args()

    if args.fetch:
        fetch_pipeline()
    git("cat-file", "-e", f"{SYNTHESIS_REF}^{{commit}}")
    synthesis = sha(SYNTHESIS_REF)
    staging = [staging_entry(ref, synthesis) for ref in refs(STAGING_PREFIX)]
    prep = [prep_entry(ref, synthesis) for ref in refs(PREP_PREFIX)]
    staging.sort(key=lambda entry: entry["name"])
    prep.sort(key=lambda entry: entry["name"])
    staging_labels = {entry["branch_label"] for entry in staging}
    for entry in prep:
        if entry["name"] in staging_labels and entry["state"] != "BLOCKED":
            entry["state"] = "SUPERSEDED_BY_STAGING"
    active_staging = [entry for entry in staging if entry["state"] != "INTEGRATED"]
    if len(active_staging) > 1:
        branches = ", ".join(entry["branch"] for entry in active_staging)
        for entry in active_staging:
            entry["state"] = "BLOCKED"
            entry["errors"].append("multiple active staging branches: " + branches)
    action = next_action(args.role, staging, prep)
    report = {"synthesis": synthesis, "prep": prep, "staging": staging, "next": action}

    if args.json:
        print(json.dumps(report, sort_keys=True, indent=2))
    else:
        text_report(synthesis, staging, prep, action)

    bad_states = {"BLOCKED", "STALE_BASE", "REBASE_REQUIRED"}
    if args.strict and (
        any(entry["state"] in bad_states for entry in prep + staging)
        or action.get("action") == "BLOCKED"
    ):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
