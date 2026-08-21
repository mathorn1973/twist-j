#!/usr/bin/env python3
"""Validate supplemental public Lean audits without executing Lean."""

from __future__ import annotations

import csv
from datetime import date
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tomllib
from urllib.parse import unquote, urlparse


AUDIT_FIELDS = (
    "audit_id", "audit_kind", "profile", "claim_id", "coverage", "status_effect",
    "canon_tag", "content_commit", "claim_scope_sha256", "location",
    "source_commit", "source_sha256", "records_sha256", "hash_mode",
)
EVENT_FIELDS = (
    "event_id", "event_sequence", "audit_id", "event_type", "event_date",
    "reason", "replacement_audit_id",
)
COVERAGE_FIELDS = (
    "claim_id", "theorem_name", "covered_statement", "unformalized_scope",
)
DEPENDENCY_FIELDS = ("name", "source", "revision", "license")
AXIOM_FIELDS = ("theorem_name", "axioms")
AUDIT_ID = re.compile(r"^A-LEAN-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
EVENT_ID = re.compile(r"^AE-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
THEOREM_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_'.]*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
CANON_TAG = re.compile(r"^canon-v[1-9][0-9]*$")
TOOLCHAIN = re.compile(r"^leanprover/lean4:v([0-9]+\.[0-9]+\.[0-9]+)\n?$")
SOURCE_HASH_MODE = "lean-audit-source-sha256-v1"
AUDIT_PROFILE = "LEAN4-RECORDED-V1"
REQUIRED_SOURCE_FILES = {
    "README.md", "COVERAGE.tsv", "DEPENDENCIES.tsv", "Audit.lean",
    "lean-toolchain", "lakefile.toml", "lake-manifest.json",
    "MATHLIB-MANIFEST.json",
}
REQUIRED_RECORD_FILES = {"AXIOMS.tsv", "EXPECTED.txt", "RUN.md", "RESULT.md"}
RECORD_FILES = REQUIRED_RECORD_FILES
RUN_FIELDS = {
    "source_commit", "source_sha256", "working_directory", "command", "exit_code",
    "stdout_sha256", "stdout_bytes", "stderr_bytes", "platform",
    "architecture", "lean_version", "lake_version", "clean_before",
    "clean_after", "fresh_clone", "lake_state_before_fetch",
    "dependency_checkouts_verified", "network", "secrets",
}
RESULT_FIELDS = {"audit_id", "result", "claim_effect"}
ALLOWED_AXIOMS = {"Classical.choice", "Quot.sound", "propext"}
ALLOWED_LICENSES = {
    "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MIT", "MPL-2.0",
}
FORBIDDEN_LEAN = (
    (re.compile(r"\bsorry\b"), "sorry"),
    (re.compile(r"\badmit\b"), "admit"),
    (re.compile(r"\bsorryAx\b"), "sorryAx"),
    (re.compile(r"(?m)^(?!\s*#print\s+axioms\b).*?\baxioms?\b"), "package-local axiom"),
    (re.compile(r"\bconstants?\b"), "constant declaration"),
    (re.compile(r"\bopaque\b"), "opaque declaration"),
    (re.compile(r"\bpartial\b"), "partial declaration"),
    (re.compile(r"\bunsafe\b"), "unsafe"),
    (re.compile(r"\bprivate\b"), "private declaration"),
    (re.compile(r"\bimplemented_by\b"), "implemented_by"),
    (re.compile(r"\bnative_decide\b"), "native_decide"),
    (re.compile(r"\bofReduceBool\b"), "ofReduceBool"),
    (re.compile(r"\bextern\b"), "extern declaration"),
    (
        re.compile(
            r"\b(?:run_cmd|run_tac|initialize|builtin_initialize|elab|"
            r"elab_rules|macro|macro_rules|syntax|declare_syntax_cat|"
            r"command_elab|builtin_command_parser|namespace|attribute|"
            r"notation|infix|infixl|infixr|prefix|postfix)\b"
        ),
        "metaprogramming or namespace command",
    ),
    (re.compile(r"@\["), "attribute declaration"),
    (re.compile(r"`"), "syntax quotation"),
    (
        re.compile(
            r"(?m)^\s*#(?:eval|execute|run|reduce|check|synth|guard|"
            r"guard_msgs|lint|find|min_imports|time)\b"
        ),
        "output or execution command",
    ),
)


class AuditError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise AuditError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def public_https_url(value: str) -> bool:
    parsed = urlparse(value)
    try:
        port = parsed.port
    except ValueError:
        return False
    path_parts = [part for part in parsed.path.split("/") if part]
    safe_part = re.compile(r"^[A-Za-z0-9_.-]+$")
    return bool(
        parsed.scheme == "https"
        and parsed.hostname == "github.com"
        and port in {None, 443}
        and parsed.username is None and parsed.password is None
        and not parsed.query and not parsed.fragment
        and len(path_parts) == 2
        and all(part not in {".", ".."} and safe_part.fullmatch(part) for part in path_parts)
    )


def points_to_supplemental_audits(value: str) -> bool:
    decoded = value.strip()
    for _ in range(4):
        expanded = unquote(decoded)
        if expanded == decoded:
            break
        decoded = expanded
    normalized = decoded.replace("\\", "/").lower()
    parsed = urlparse(normalized)
    path = unquote(parsed.path) if parsed.scheme else normalized
    parts = [part for part in path.split("/") if part not in {"", "."}]
    return "audits" in parts or "A-LEAN-" in decoded.upper()


def markdown_section_value(text: str, heading: str, context: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        fail(f"{context} lacks {marker}")
    tail = text.split(marker, 1)[1]
    section = tail.split("\n## ", 1)[0]
    lines = [line.strip() for line in section.splitlines() if line.strip()]
    if len(lines) != 1:
        fail(f"{context} {marker} must contain exactly one normalized value")
    return lines[0]


def parse_tsv(text: str, fields: tuple[str, ...], label: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    if tuple(reader.fieldnames or ()) != fields:
        fail(f"{label} header must be: " + "\t".join(fields))
    rows = list(reader)
    for number, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            fail(f"{label} line {number} has the wrong number of columns")
    return rows


def read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"missing {path}")
    return parse_tsv(path.read_text(encoding="utf-8"), fields, str(path))


def require_text(row: dict[str, str], field: str, context: str) -> str:
    value = row[field].strip()
    if not value:
        fail(f"{context} has empty {field}")
    return value


def read_record(path: Path, required: set[str]) -> dict[str, str]:
    if not path.is_file():
        fail(f"missing {path}")
    fields: dict[str, str] = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_]*):\s*(\S.*?)\s*", line)
        if not match:
            fail(f"{path} line {number} is not a structured field")
        key, value = match.groups()
        if key not in required:
            fail(f"{path} line {number} has unknown field {key}")
        if key in fields:
            fail(f"{path} line {number} duplicates {key}")
        fields[key] = value
    missing = sorted(required - fields.keys())
    if missing:
        fail(f"{path} lacks fields: " + ", ".join(missing))
    return fields


def read_strict_json(path: Path, context: str) -> object:
    def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                fail(f"{context} duplicates JSON key {key}")
            result[key] = value
        return result

    try:
        return json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=unique_object,
        )
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        fail(f"{context} is invalid JSON: {error}")


def git(
    root: Path,
    *arguments: str,
    allow_failure: bool = False,
) -> subprocess.CompletedProcess[bytes]:
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", *arguments],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode and not allow_failure:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        fail(f"git {' '.join(arguments)} failed: {detail}")
    return completed


def git_text(root: Path, *arguments: str) -> str:
    return git(root, *arguments).stdout.decode("utf-8")


def commit_exists(root: Path, commit: str) -> bool:
    return bool(COMMIT.fullmatch(commit)) and not git(
        root, "cat-file", "-e", f"{commit}^{{commit}}", allow_failure=True,
    ).returncode


def github_event_for_root(root: Path) -> dict[str, object]:
    event_path = os.environ.get("GITHUB_EVENT_PATH", "").strip()
    workspace = os.environ.get("GITHUB_WORKSPACE", "").strip()
    if not event_path or not workspace:
        return {}
    try:
        if root.resolve() != Path(workspace).resolve():
            return {}
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return {}
    return event if isinstance(event, dict) else {}


def require_commit(root: Path, commit: str, context: str) -> None:
    if not COMMIT.fullmatch(commit):
        fail(f"{context} is not a full commit SHA")
    if not commit_exists(root, commit):
        fail(f"{context} does not exist in public history")


def require_ancestor(root: Path, ancestor: str, descendant: str, context: str) -> None:
    if git(
        root, "merge-base", "--is-ancestor", ancestor, descendant,
        allow_failure=True,
    ).returncode:
        fail(f"{context} is not an ancestor of {descendant}")


def parse_status(text: str, context: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([A-Z][A-Z0-9_]*):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2)
    for required in ("TAG", "CONTENT_COMMIT"):
        if required not in fields:
            fail(f"{context} lacks {required}")
    return fields


def manifest_sha256(items: list[tuple[str, bytes]]) -> str:
    lines = [f"{sha256_bytes(data)}  {path}\n" for path, data in sorted(items)]
    return sha256_bytes("".join(lines).encode("utf-8"))


def is_source_file(relative: Path) -> bool:
    return relative.name not in RECORD_FILES and ".lake" not in relative.parts


def allowed_package_file(relative: Path) -> bool:
    return bool(
        relative.suffix in {".lean", ".md", ".tsv", ".json", ".txt", ".toml"}
        or relative.name == "lean-toolchain"
        or relative.name.startswith(("LICENSE", "NOTICE"))
    )


def source_sha256(package: Path, root: Path) -> str:
    items: list[tuple[str, bytes]] = []
    for path in package.rglob("*"):
        if path.is_file() and is_source_file(path.relative_to(package)):
            items.append((path.relative_to(root).as_posix(), path.read_bytes()))
    return manifest_sha256(items)


def records_sha256(package: Path, root: Path) -> str:
    items = [
        ((package / name).relative_to(root).as_posix(), (package / name).read_bytes())
        for name in sorted(RECORD_FILES)
    ]
    return manifest_sha256(items)


def source_sha256_at_commit(
    root: Path,
    location: str,
    commit: str,
) -> tuple[str, set[str]]:
    raw_names = git(
        root, "ls-tree", "-r", "-z", "--name-only", commit, "--", location,
    ).stdout
    names = {
        name for name in raw_names.decode("utf-8").split("\0") if name
    }
    if not names:
        fail(f"source_commit {commit} lacks {location}")
    items: list[tuple[str, bytes]] = []
    relative_names: set[str] = set()
    prefix = location + "/"
    for name in sorted(names):
        if not name.startswith(prefix):
            fail(f"source_commit {commit} has unsafe path {name}")
        relative = Path(name[len(prefix):])
        relative_names.add(relative.as_posix())
        if is_source_file(relative):
            items.append((name, git(root, "show", f"{commit}:{name}").stdout))
    return manifest_sha256(items), relative_names


def strip_lean_comments_and_strings(text: str, context: str) -> str:
    output: list[str] = []
    index = 0
    block_depth = 0
    in_string = False
    while index < len(text):
        pair = text[index:index + 2]
        if block_depth:
            if pair == "/-":
                block_depth += 1
                index += 2
            elif pair == "-/":
                block_depth -= 1
                index += 2
            else:
                if text[index] == "\n":
                    output.append("\n")
                index += 1
            continue
        if in_string:
            if text[index] == "\\":
                index += 2
            elif text[index] == '"':
                in_string = False
                index += 1
            else:
                if text[index] == "\n":
                    output.append("\n")
                index += 1
            continue
        if pair == "--":
            newline = text.find("\n", index + 2)
            output.append(" ")
            if newline < 0:
                break
            output.append("\n")
            index = newline + 1
        elif pair == "/-":
            output.append(" ")
            block_depth = 1
            index += 2
        elif text[index] == '"':
            output.append(" ")
            in_string = True
            index += 1
        else:
            output.append(text[index])
            index += 1
    if block_depth or in_string:
        fail(f"{context} has an unterminated comment or string")
    return "".join(output)


def printed_axioms(output: str, theorem: str, context: str) -> list[str]:
    theorem_pattern = re.compile(
        rf"(?<![A-Za-z0-9_']){re.escape(theorem)}(?![A-Za-z0-9_'])"
    )
    candidates = [
        line.strip() for line in output.splitlines()
        if theorem_pattern.search(line) and "axiom" in line.lower()
    ]
    if len(candidates) != 1:
        fail(f"{context} must have exactly one #print axioms output line")
    line = candidates[0]
    if "does not depend on any axioms" in line:
        return []
    match = re.search(r"depends on axioms:\s*\[(.*?)\]\s*$", line)
    if not match:
        fail(f"{context} has unrecognized #print axioms output")
    body = match.group(1).strip()
    return [] if not body else sorted(part.strip() for part in body.split(","))


def validate_canon_pin(root: Path, row: dict[str, str], context: str) -> None:
    tag = row["canon_tag"].strip()
    content_commit = row["content_commit"].strip()
    claim = row["claim_id"].strip()
    if not CANON_TAG.fullmatch(tag):
        fail(f"{context} has invalid canon_tag")
    tag_commit = git_text(root, "rev-list", "-n", "1", tag).strip()
    if not COMMIT.fullmatch(tag_commit):
        fail(f"{context} names a missing Canon tag")
    require_ancestor(root, tag_commit, "HEAD", f"Canon tag {tag}")
    status = parse_status(
        git_text(root, "show", f"{tag}:STATUS.md"), f"{tag}:STATUS.md",
    )
    if status["TAG"] != tag or status["CONTENT_COMMIT"] != content_commit:
        fail(f"{context} Canon tag and content_commit do not match tagged STATUS.md")
    require_commit(root, content_commit, f"{context} content_commit")
    require_ancestor(root, content_commit, tag_commit, f"{context} content_commit")
    registry_text = git_text(root, "show", f"{content_commit}:canon/REGISTRY.tsv")
    registry_rows = parse_tsv(
        registry_text,
        ("claim_id", "status", "scope", "canon_section", "evidence", "falsifier"),
        f"{content_commit}:canon/REGISTRY.tsv",
    )
    matches = [entry for entry in registry_rows if entry["claim_id"].strip() == claim]
    if len(matches) != 1 or matches[0]["status"].strip() not in {"T", "T-LOCK"}:
        fail(f"{context} does not map a theorem claim at the pinned Canon edition")
    expected_scope = sha256_bytes(matches[0]["scope"].encode("utf-8"))
    if row["claim_scope_sha256"].strip() != expected_scope:
        fail(f"{context} scope hash differs from the pinned Canon edition")


def validate_source_pin(root: Path, row: dict[str, str], context: str) -> None:
    audit_id = row["audit_id"].strip()
    location = row["location"].strip()
    source_commit = row["source_commit"].strip()
    require_commit(root, source_commit, f"{context} source_commit")
    require_ancestor(root, source_commit, "HEAD", f"{context} source_commit")
    tag_commit = git_text(root, "rev-list", "-n", "1", row["canon_tag"].strip()).strip()
    require_ancestor(
        root, tag_commit, source_commit,
        f"{context} Canon tag at source pin",
    )
    pinned_digest, pinned_names = source_sha256_at_commit(root, location, source_commit)
    forbidden_at_pin = sorted(RECORD_FILES & {Path(name).name for name in pinned_names})
    if forbidden_at_pin:
        fail(f"{audit_id} source pin already contains run records: " + ", ".join(forbidden_at_pin))
    missing_sources = sorted(REQUIRED_SOURCE_FILES - {Path(name).name for name in pinned_names})
    if missing_sources:
        fail(f"{audit_id} source pin lacks files: " + ", ".join(missing_sources))
    if row["source_sha256"].strip() != pinned_digest:
        fail(f"{audit_id} source hash differs from source_commit")
    for name in pinned_names:
        relative = Path(name)
        if len(relative.parts) != 1 or not allowed_package_file(relative):
            fail(f"{audit_id} source pin contains unsupported file {name}")
    pinned_index = git(
        root, "show", f"{source_commit}:audits/INDEX.tsv", allow_failure=True,
    )
    if pinned_index.returncode == 0:
        pinned_rows = parse_tsv(
            pinned_index.stdout.decode("utf-8"), AUDIT_FIELDS,
            f"{source_commit}:audits/INDEX.tsv",
        )
        if any(entry["audit_id"].strip() == audit_id for entry in pinned_rows):
            fail(f"{audit_id} was indexed before its recorded run")


def validate_package(package: Path, root: Path, row: dict[str, str]) -> None:
    audit_id = row["audit_id"].strip()
    claim = row["claim_id"].strip()
    for item in package.rglob("*"):
        relative = item.relative_to(package)
        if ".lake" in relative.parts:
            continue
        if item.is_symlink():
            fail(f"{audit_id} contains symlink {item.relative_to(root)}")
        if item.is_dir():
            continue
        if not allowed_package_file(relative):
            fail(f"{audit_id} contains unsupported file {item.relative_to(root)}")
    present = {path.name for path in package.iterdir() if path.is_file()}
    missing = sorted((REQUIRED_SOURCE_FILES | REQUIRED_RECORD_FILES) - present)
    if missing:
        fail(f"{audit_id} lacks files: " + ", ".join(missing))
    if any(path.is_dir() and path.name != ".lake" for path in package.iterdir()):
        fail(f"{audit_id} first trust profile forbids nested source directories")

    readme = (package / "README.md").read_text(encoding="utf-8")
    for heading in (
        "Status: SUPPLEMENTAL PUBLIC AUDIT", "## Scope", "## Trust boundary",
        "## Accepted axioms", "## Dependency provenance", "## Upstream closure",
    ):
        if heading not in readme:
            fail(f"{audit_id} README lacks {heading}")

    toolchain_text = (package / "lean-toolchain").read_text(encoding="utf-8")
    toolchain_match = TOOLCHAIN.fullmatch(toolchain_text)
    if not toolchain_match:
        fail(f"{audit_id} has mutable or invalid lean-toolchain")
    lean_version = toolchain_match.group(1)

    manifest = read_strict_json(
        package / "lake-manifest.json", f"{audit_id} lake-manifest.json",
    )
    manifest_keys = {
        "version", "packagesDir", "packages", "name", "lakeDir",
        "fixedToolchain",
    }
    if not isinstance(manifest, dict) or set(manifest) != manifest_keys:
        fail(f"{audit_id} lake-manifest.json does not use manifest profile 1.2.0")
    if (
        manifest["version"] != "1.2.0"
        or manifest["packagesDir"] != ".lake/packages"
        or not isinstance(manifest["name"], str)
        or not manifest["name"].strip()
        or manifest["lakeDir"] != ".lake"
        or manifest["fixedToolchain"] is not False
    ):
        fail(f"{audit_id} lake-manifest.json has unsafe root configuration")
    packages = manifest.get("packages") if isinstance(manifest, dict) else None
    if not isinstance(packages, list):
        fail(f"{audit_id} lake-manifest.json lacks a packages list")
    manifest_dependencies: dict[str, tuple[str, str]] = {}
    manifest_direct_dependencies: dict[str, tuple[str, str]] = {}
    manifest_entries: dict[str, dict[str, object]] = {}
    for dependency in packages:
        if not isinstance(dependency, dict):
            fail(f"{audit_id} has invalid Lake dependency entry")
        dependency_keys = {
            "name", "type", "url", "rev", "inputRev", "subDir", "scope",
            "manifestFile", "inherited", "configFile",
        }
        if set(dependency) != dependency_keys:
            fail(f"{audit_id} Lake dependency has unsupported manifest keys")
        string_fields = ("name", "type", "url", "rev", "scope", "manifestFile", "configFile")
        if any(not isinstance(dependency[field], str) for field in string_fields):
            fail(f"{audit_id} Lake dependency has invalid field types")
        name = dependency["name"].strip()
        kind = dependency["type"].strip()
        source = dependency["url"].strip()
        revision = dependency["rev"].strip()
        input_revision = dependency.get("inputRev")
        inherited = dependency.get("inherited")
        if not name or name in manifest_dependencies:
            fail(f"{audit_id} has missing or duplicate Lake dependency name")
        if (
            kind != "git" or not public_https_url(source)
            or not COMMIT.fullmatch(revision)
        ):
            fail(f"{audit_id} dependency {name} is not a public full-SHA git pin")
        if input_revision is not None and (
            not isinstance(input_revision, str) or not input_revision.strip()
        ):
            fail(f"{audit_id} dependency {name} has invalid inputRev")
        if not isinstance(inherited, bool):
            fail(f"{audit_id} dependency {name} has invalid inherited flag")
        if not isinstance(dependency.get("scope"), str):
            fail(f"{audit_id} dependency {name} has invalid scope")
        if dependency.get("subDir") is not None:
            fail(f"{audit_id} dependency {name} uses a forbidden subdirectory")
        if dependency.get("manifestFile") != "lake-manifest.json":
            fail(f"{audit_id} dependency {name} has an unsafe manifestFile")
        if dependency.get("configFile") not in {"lakefile.lean", "lakefile.toml"}:
            fail(f"{audit_id} dependency {name} has an unsafe configFile")
        manifest_dependencies[name] = (source, revision)
        manifest_entries[name] = dependency
        if not inherited:
            if input_revision not in {None, revision}:
                fail(f"{audit_id} direct dependency {name} has a mutable inputRev")
            manifest_direct_dependencies[name] = (source, revision)

    if set(manifest_direct_dependencies) != {"mathlib"}:
        fail(f"{audit_id} manifest must have only Mathlib as a direct dependency")
    mathlib_revision = manifest_direct_dependencies["mathlib"][1]
    expected_upstream_url = (
        "https://github.com/leanprover-community/mathlib4/blob/"
        f"{mathlib_revision}/lake-manifest.json"
    )
    if markdown_section_value(
        readme, "Upstream closure", f"{audit_id} README",
    ) != expected_upstream_url:
        fail(f"{audit_id} README upstream closure does not match the Mathlib pin")

    upstream_manifest = read_strict_json(
        package / "MATHLIB-MANIFEST.json", f"{audit_id} MATHLIB-MANIFEST.json",
    )
    if not isinstance(upstream_manifest, dict) or set(upstream_manifest) != manifest_keys:
        fail(f"{audit_id} MATHLIB-MANIFEST.json does not use manifest profile 1.2.0")
    if (
        upstream_manifest["version"] != "1.2.0"
        or upstream_manifest["packagesDir"] != ".lake/packages"
        or upstream_manifest["name"] != "mathlib"
        or upstream_manifest["lakeDir"] != ".lake"
        or not isinstance(upstream_manifest["fixedToolchain"], bool)
        or not isinstance(upstream_manifest["packages"], list)
    ):
        fail(f"{audit_id} MATHLIB-MANIFEST.json has unsafe root configuration")
    upstream_entries: dict[str, dict[str, object]] = {}
    for dependency in upstream_manifest["packages"]:
        if not isinstance(dependency, dict) or set(dependency) != dependency_keys:
            fail(f"{audit_id} MATHLIB-MANIFEST.json has an invalid dependency entry")
        if any(not isinstance(dependency[field], str) for field in string_fields):
            fail(f"{audit_id} MATHLIB-MANIFEST.json has invalid dependency types")
        name = dependency["name"].strip()
        input_revision = dependency["inputRev"]
        if (
            not name or name in upstream_entries
            or dependency["type"] != "git"
            or not public_https_url(dependency["url"])
            or not COMMIT.fullmatch(dependency["rev"])
            or (input_revision is not None and (
                not isinstance(input_revision, str) or not input_revision.strip()
            ))
            or not isinstance(dependency["inherited"], bool)
            or dependency["subDir"] is not None
            or dependency["manifestFile"] != "lake-manifest.json"
            or dependency["configFile"] not in {"lakefile.lean", "lakefile.toml"}
        ):
            fail(f"{audit_id} MATHLIB-MANIFEST.json has an unsafe dependency entry")
        upstream_entries[name] = dependency
    inherited_entries = {
        name: entry for name, entry in manifest_entries.items()
        if entry["inherited"] is True
    }
    if set(inherited_entries) != set(upstream_entries):
        fail(f"{audit_id} inherited dependency closure differs from its Mathlib snapshot")
    for name, upstream_entry in upstream_entries.items():
        expected_entry = dict(upstream_entry)
        expected_entry["inherited"] = True
        if inherited_entries[name] != expected_entry:
            fail(f"{audit_id} inherited dependency {name} differs from its Mathlib snapshot")

    dependency_rows = read_tsv(package / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS)
    declared_dependencies: dict[str, tuple[str, str]] = {}
    dependency_names: list[str] = []
    for number, dependency in enumerate(dependency_rows, 2):
        dependency_context = f"{audit_id} DEPENDENCIES.tsv line {number}"
        name = require_text(dependency, "name", dependency_context)
        source = require_text(dependency, "source", dependency_context)
        revision = require_text(dependency, "revision", dependency_context)
        license_name = require_text(dependency, "license", dependency_context)
        if name in declared_dependencies:
            fail(f"{audit_id} DEPENDENCIES.tsv duplicates {name}")
        if not public_https_url(source) or not COMMIT.fullmatch(revision):
            fail(f"{dependency_context} is not a public full-SHA pin")
        if license_name not in ALLOWED_LICENSES:
            fail(f"{dependency_context} has an unapproved SPDX licence")
        declared_dependencies[name] = (source, revision)
        dependency_names.append(name)
    if dependency_names != sorted(dependency_names):
        fail(f"{audit_id} DEPENDENCIES.tsv rows must be sorted by name")
    if declared_dependencies != manifest_dependencies:
        fail(f"{audit_id} dependency manifest differs from lake-manifest.json")

    try:
        lakefile = tomllib.loads((package / "lakefile.toml").read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        fail(f"{audit_id} has invalid lakefile.toml: {error}")
    if set(lakefile) != {"name", "version", "defaultTargets", "require", "lean_lib"}:
        fail(f"{audit_id} lakefile.toml has unsupported keys")
    if not isinstance(lakefile["name"], str) or not lakefile["name"].strip():
        fail(f"{audit_id} lakefile.toml has invalid name")
    if manifest["name"] != lakefile["name"]:
        fail(f"{audit_id} lakefile.toml name differs from lake-manifest.json")
    if not isinstance(lakefile["version"], str) or not re.fullmatch(
        r"[0-9]+\.[0-9]+\.[0-9]+", lakefile["version"],
    ):
        fail(f"{audit_id} lakefile.toml has invalid version")
    if lakefile["defaultTargets"] != ["LeanAudit"]:
        fail(f"{audit_id} lakefile.toml must use only LeanAudit as default target")
    if lakefile["lean_lib"] != [{"name": "LeanAudit"}]:
        fail(f"{audit_id} lakefile.toml must declare exactly one LeanAudit library")
    direct_dependencies: dict[str, tuple[str, str]] = {}
    if not isinstance(lakefile["require"], list):
        fail(f"{audit_id} lakefile.toml require must be a list")
    for dependency in lakefile["require"]:
        if not isinstance(dependency, dict) or set(dependency) != {"name", "git", "rev"}:
            fail(f"{audit_id} lakefile.toml has an unsupported dependency declaration")
        if any(not isinstance(dependency[field], str) for field in ("name", "git", "rev")):
            fail(f"{audit_id} lakefile.toml dependency fields must be strings")
        name = dependency["name"]
        source = dependency["git"]
        revision = dependency["rev"]
        if (
            name in direct_dependencies or not public_https_url(source)
            or not COMMIT.fullmatch(revision)
        ):
            fail(f"{audit_id} lakefile.toml dependency {name} is not a full-SHA git pin")
        direct_dependencies[name] = (source, revision)
    if any(manifest_dependencies.get(name) != pin for name, pin in direct_dependencies.items()):
        fail(f"{audit_id} lakefile.toml differs from lake-manifest.json")
    if manifest_direct_dependencies != direct_dependencies:
        fail(f"{audit_id} inherited dependency flags differ from lakefile.toml")
    expected_mathlib = "https://github.com/leanprover-community/mathlib4.git"
    if (
        set(direct_dependencies) != {"mathlib"}
        or direct_dependencies["mathlib"][0] != expected_mathlib
    ):
        fail(f"{audit_id} first trust profile permits only the official mathlib direct dependency")

    coverage_rows = read_tsv(package / "COVERAGE.tsv", COVERAGE_FIELDS)
    if not coverage_rows:
        fail(f"{audit_id} COVERAGE.tsv is empty")
    theorem_names: list[str] = []
    exclusions: list[str] = []
    for number, coverage_row in enumerate(coverage_rows, 2):
        coverage_context = f"{audit_id} COVERAGE.tsv line {number}"
        if require_text(coverage_row, "claim_id", coverage_context) != claim:
            fail(f"{coverage_context} names another claim")
        theorem = require_text(coverage_row, "theorem_name", coverage_context)
        if not THEOREM_NAME.fullmatch(theorem) or theorem in theorem_names:
            fail(f"{coverage_context} has invalid or duplicate theorem_name")
        require_text(coverage_row, "covered_statement", coverage_context)
        exclusions.append(require_text(coverage_row, "unformalized_scope", coverage_context))
        theorem_names.append(theorem)
    if theorem_names != sorted(theorem_names):
        fail(f"{audit_id} COVERAGE.tsv rows must be sorted by theorem_name")
    if row["coverage"].strip() == "EXACT" and any(value != "NONE" for value in exclusions):
        fail(f"{audit_id} EXACT coverage names unformalized scope")
    if row["coverage"].strip() == "PARTIAL" and all(value == "NONE" for value in exclusions):
        fail(f"{audit_id} PARTIAL coverage must name an exclusion")

    proof_sources = sorted(package.glob("*.lean"))
    if package / "Audit.lean" not in proof_sources:
        fail(f"{audit_id} lacks Audit.lean")
    stripped_sources: dict[str, str] = {}
    for source in proof_sources:
        code = strip_lean_comments_and_strings(
            source.read_text(encoding="utf-8"), f"{audit_id} {source.name}",
        )
        global_auto_implicit = re.findall(
            r"(?m)^\s*set_option\s+autoImplicit\s+false\s*$", code,
        )
        if len(global_auto_implicit) != 1:
            fail(
                f"{audit_id} {source.name} must set autoImplicit false "
                "once as a global standalone command"
            )
        significant_lines = [line.strip() for line in code.splitlines() if line.strip()]
        option_index = significant_lines.index("set_option autoImplicit false")
        if any(
            line != "prelude" and not re.fullmatch(r"import\s+\S.*", line)
            for line in significant_lines[:option_index]
        ):
            fail(f"{audit_id} {source.name} must disable autoImplicit before declarations")
        if re.search(r"set_option\s+autoImplicit\s+false\s+in\b", code):
            fail(f"{audit_id} {source.name} must not scope autoImplicit false")
        if re.search(r"set_option\s+autoImplicit\s+true", code):
            fail(f"{audit_id} {source.name} must not re-enable autoImplicit")
        for pattern, label in FORBIDDEN_LEAN:
            if pattern.search(code):
                fail(f"{audit_id} {source.name} contains forbidden {label}")
        for command in re.finditer(r"#(?:[^\W\d]\w*|«)", code):
            line_start = code.rfind("\n", 0, command.start()) + 1
            line_end = code.find("\n", command.end())
            if line_end < 0:
                line_end = len(code)
            line = code[line_start:line_end]
            if source.name != "Audit.lean" or not re.fullmatch(
                r"\s*#print\s+axioms\s+[A-Za-z_][A-Za-z0-9_'.]*\s*", line,
            ):
                fail(
                    f"{audit_id} {source.name} contains a command other than "
                    "top-level exact #print axioms"
                )
        stripped_sources[source.name] = code
    entrypoint = stripped_sources["Audit.lean"]
    printed_theorems: list[str] = []
    for line in entrypoint.splitlines():
        if "#print" not in line:
            continue
        match = re.fullmatch(
            r"\s*#print\s+axioms\s+([A-Za-z_][A-Za-z0-9_'.]*)\s*", line,
        )
        if not match:
            fail(f"{audit_id} Audit.lean has a non-top-level #print command")
        printed_theorems.append(match.group(1))
    if printed_theorems != theorem_names:
        fail(f"{audit_id} Audit.lean #print axioms commands differ from COVERAGE.tsv")
    for theorem in theorem_names:
        declaration = (
            rf"(?m)^\s*(?:protected\s+)?(?:theorem|lemma)\s+"
            rf"{re.escape(theorem)}(?![A-Za-z0-9_'])"
        )
        if not re.search(declaration, entrypoint):
            fail(f"{audit_id} Audit.lean does not declare {theorem}")

    axiom_rows = read_tsv(package / "AXIOMS.tsv", AXIOM_FIELDS)
    axiom_names: list[str] = []
    recorded_axioms: set[str] = set()
    expected_output = (package / "EXPECTED.txt").read_text(encoding="utf-8")
    if not expected_output:
        fail(f"{audit_id} EXPECTED.txt is empty")
    for number, axiom_row in enumerate(axiom_rows, 2):
        axiom_context = f"{audit_id} AXIOMS.tsv line {number}"
        theorem = require_text(axiom_row, "theorem_name", axiom_context)
        axiom_value = require_text(axiom_row, "axioms", axiom_context)
        if theorem in axiom_names:
            fail(f"{audit_id} AXIOMS.tsv duplicates {theorem}")
        if axiom_value == "NONE":
            axioms: list[str] = []
        else:
            axioms = axiom_value.split(";")
            if axioms != sorted(set(axioms)) or not set(axioms) <= ALLOWED_AXIOMS:
                fail(f"{axiom_context} has unapproved or unsorted axioms")
        if printed_axioms(expected_output, theorem, axiom_context) != axioms:
            fail(f"{axiom_context} differs from EXPECTED.txt")
        recorded_axioms.update(axioms)
        axiom_names.append(theorem)
    if axiom_names != theorem_names:
        fail(f"{audit_id} AXIOMS.tsv differs from COVERAGE.tsv")
    normalized_axioms = "NONE" if not recorded_axioms else ";".join(sorted(recorded_axioms))
    if markdown_section_value(readme, "Accepted axioms", f"{audit_id} README") != normalized_axioms:
        fail(f"{audit_id} README accepted axioms differ from AXIOMS.tsv")

    current_source_digest = source_sha256(package, root)
    if row["source_sha256"].strip() != current_source_digest:
        fail(f"{audit_id} current source differs from its source pin")
    current_records_digest = records_sha256(package, root)
    if row["records_sha256"].strip() != current_records_digest:
        fail(f"{audit_id} records hash differs")

    run = read_record(package / "RUN.md", RUN_FIELDS)
    if run["source_commit"] != row["source_commit"].strip():
        fail(f"{audit_id} RUN.md source_commit differs from INDEX.tsv")
    if run["source_sha256"] != current_source_digest:
        fail(f"{audit_id} RUN.md source_sha256 differs from INDEX.tsv")
    if run["working_directory"] != row["location"].strip():
        fail(f"{audit_id} RUN.md working_directory must be its package location")
    if run["command"] != "lake env lean Audit.lean":
        fail(f"{audit_id} command must be lake env lean Audit.lean")
    integer_fields: dict[str, int] = {}
    for field in ("exit_code", "stdout_bytes", "stderr_bytes"):
        try:
            integer_fields[field] = int(run[field])
        except ValueError:
            fail(f"{audit_id} RUN.md has invalid {field}")
    if integer_fields["exit_code"] != 0 or integer_fields["stderr_bytes"] != 0:
        fail(f"{audit_id} recorded audit did not pass cleanly")
    expected_bytes = (package / "EXPECTED.txt").read_bytes()
    if (
        run["stdout_sha256"] != sha256_bytes(expected_bytes)
        or integer_fields["stdout_bytes"] != len(expected_bytes)
    ):
        fail(f"{audit_id} RUN.md stdout record differs from EXPECTED.txt")
    if run["lean_version"] != lean_version:
        fail(f"{audit_id} RUN.md lean_version differs from lean-toolchain")
    if run["clean_before"] != "true" or run["clean_after"] != "true":
        fail(f"{audit_id} RUN.md must record clean_before and clean_after as true")
    if (
        run["fresh_clone"] != "true"
        or run["lake_state_before_fetch"] != "absent"
        or run["dependency_checkouts_verified"] != "true"
        or run["network"] != "disabled"
        or run["secrets"] != "none"
    ):
        fail(f"{audit_id} RUN.md does not record the isolated replay profile")

    result = read_record(package / "RESULT.md", RESULT_FIELDS)
    if result != {
        "audit_id": audit_id, "result": "RECORDED_PASS", "claim_effect": "NONE",
    }:
        fail(f"{audit_id} RESULT.md is not a status-neutral RECORDED_PASS")


def current_status(root: Path) -> dict[str, str]:
    return parse_status((root / "STATUS.md").read_text(encoding="utf-8"), "STATUS.md")


def current_registry(root: Path) -> dict[str, dict[str, str]]:
    rows = read_tsv(
        root / "canon" / "REGISTRY.tsv",
        ("claim_id", "status", "scope", "canon_section", "evidence", "falsifier"),
    )
    return {row["claim_id"].strip(): row for row in rows}


def validate_events(
    rows: list[dict[str, str]],
    audits_by_id: dict[str, dict[str, str]],
) -> None:
    seen_events: set[str] = set()
    seen_audits: set[str] = set()
    supersessions: dict[str, str] = {}
    previous_date: date | None = None
    for number, row in enumerate(rows, 2):
        context = f"audits/EVENTS.tsv line {number}"
        for field in EVENT_FIELDS:
            require_text(row, field, context)
        event_id = row["event_id"].strip()
        audit_id = row["audit_id"].strip()
        event_type = row["event_type"].strip()
        replacement = row["replacement_audit_id"].strip()
        try:
            sequence = int(row["event_sequence"].strip())
        except ValueError:
            fail(f"{context} has invalid event_sequence")
        if sequence != number - 1:
            fail(f"{context} event_sequence must preserve append order")
        if not EVENT_ID.fullmatch(event_id) or event_id in seen_events:
            fail(f"{context} has invalid or duplicate event_id")
        if audit_id not in audits_by_id or audit_id in seen_audits:
            fail(f"{context} names an unknown or already qualified audit")
        if event_type not in {"WITHDRAWN", "SUPERSEDED"}:
            fail(f"{context} has invalid event_type")
        try:
            event_date = date.fromisoformat(row["event_date"].strip())
        except ValueError:
            fail(f"{context} has invalid event_date")
        if event_date > date.today():
            fail(f"{context} event_date is in the future")
        if previous_date is not None and event_date < previous_date:
            fail(f"{context} event_date moves backwards")
        previous_date = event_date
        if len(row["reason"].strip()) < 20:
            fail(f"{context} reason is too short")
        if event_type == "WITHDRAWN" and replacement != "-":
            fail(f"{context} WITHDRAWN event must use replacement_audit_id -")
        if event_type == "SUPERSEDED" and (
            replacement not in audits_by_id or replacement == audit_id
        ):
            fail(f"{context} SUPERSEDED event needs another existing audit")
        if event_type == "SUPERSEDED":
            if replacement in seen_audits:
                fail(f"{context} replacement audit was already qualified at this event")
            if (
                audits_by_id[audit_id]["claim_id"].strip()
                != audits_by_id[replacement]["claim_id"].strip()
            ):
                fail(f"{context} replacement audit maps another claim")
            if (
                audits_by_id[audit_id]["claim_scope_sha256"].strip()
                != audits_by_id[replacement]["claim_scope_sha256"].strip()
            ):
                fail(f"{context} replacement audit maps another claim scope")
            coverage_rank = {"PARTIAL": 0, "EXACT": 1}
            old_coverage = audits_by_id[audit_id]["coverage"].strip()
            new_coverage = audits_by_id[replacement]["coverage"].strip()
            if coverage_rank[new_coverage] < coverage_rank[old_coverage]:
                fail(f"{context} replacement audit weakens coverage")
            supersessions[audit_id] = replacement
        seen_events.add(event_id)
        seen_audits.add(audit_id)
    for start in supersessions:
        path: set[str] = set()
        current = start
        while current in supersessions:
            if current in path:
                fail("audits/EVENTS.tsv contains a supersession cycle")
            path.add(current)
            current = supersessions[current]


def detect_base_commit(root: Path) -> str | None:
    explicit = os.environ.get("AUDIT_BASE_SHA", "").strip()
    if COMMIT.fullmatch(explicit):
        return explicit
    event = github_event_for_root(root)
    if event:
        pull_base = event.get("pull_request", {}).get("base", {}).get("sha", "")
        before = event.get("before", "")
        for candidate in (pull_base, before):
            if COMMIT.fullmatch(candidate) and candidate != "0" * 40:
                return candidate
    branch = git_text(root, "rev-parse", "--abbrev-ref", "HEAD").strip()
    if branch != "main":
        merge_base = git(
            root, "merge-base", "HEAD", "origin/main", allow_failure=True,
        )
        candidate = merge_base.stdout.decode("utf-8").strip()
        if COMMIT.fullmatch(candidate):
            return candidate
    return None


def index_at_commit(root: Path, commit: str) -> list[dict[str, str]] | None:
    shown = git(
        root, "show", f"{commit}:audits/INDEX.tsv", allow_failure=True,
    )
    if shown.returncode:
        return None
    return parse_tsv(
        shown.stdout.decode("utf-8"), AUDIT_FIELDS,
        f"{commit}:audits/INDEX.tsv",
    )


def events_at_commit(root: Path, commit: str) -> list[dict[str, str]] | None:
    shown = git(
        root, "show", f"{commit}:audits/EVENTS.tsv", allow_failure=True,
    )
    if shown.returncode:
        return None
    return parse_tsv(
        shown.stdout.decode("utf-8"), EVENT_FIELDS,
        f"{commit}:audits/EVENTS.tsv",
    )


def detect_audit_head(root: Path, base_commit: str) -> str:
    explicit = os.environ.get("AUDIT_HEAD_SHA", "").strip()
    if COMMIT.fullmatch(explicit):
        return explicit
    event = github_event_for_root(root)
    if event:
        pull_head = event.get("pull_request", {}).get("head", {}).get("sha", "")
        if COMMIT.fullmatch(pull_head):
            return pull_head
    head = git_text(root, "rev-parse", "HEAD").strip()
    parents = git_text(root, "rev-list", "--parents", "-n", "1", head).split()
    if len(parents) == 3 and base_commit in parents[1:]:
        other = [parent for parent in parents[1:] if parent != base_commit]
        if len(other) == 1:
            return other[0]
    return head


def validate_change_set(
    root: Path,
    rows: list[dict[str, str]],
    event_rows: list[dict[str, str]],
    base_commit: str | None,
) -> None:
    if base_commit is None:
        return
    require_commit(root, base_commit, "audit comparison base")
    base_rows = index_at_commit(root, base_commit)
    if base_rows is None:
        return  # Bootstrap policy pull request.
    base_event_rows = events_at_commit(root, base_commit)
    if base_event_rows is None:
        fail("audit comparison base lacks EVENTS.tsv")
    base_by_id = {row["audit_id"].strip(): row for row in base_rows}
    current_by_id = {row["audit_id"].strip(): row for row in rows}
    removed = sorted(set(base_by_id) - set(current_by_id))
    changed = sorted(
        audit_id for audit_id in set(base_by_id) & set(current_by_id)
        if base_by_id[audit_id] != current_by_id[audit_id]
    )
    if removed or changed:
        fail("sealed audit rows are immutable: " + ", ".join(removed + changed))
    added = sorted(set(current_by_id) - set(base_by_id))
    base_events = {row["event_id"].strip(): row for row in base_event_rows}
    current_events = {row["event_id"].strip(): row for row in event_rows}
    removed_events = sorted(set(base_events) - set(current_events))
    changed_events = sorted(
        event_id for event_id in set(base_events) & set(current_events)
        if base_events[event_id] != current_events[event_id]
    )
    if removed_events or changed_events:
        fail(
            "audit qualification events are append-only: "
            + ", ".join(removed_events + changed_events)
        )
    added_events = sorted(set(current_events) - set(base_events))
    changed_paths = {
        path for path in git_text(
            root, "diff", "--name-only", base_commit, "HEAD",
        ).splitlines() if path
    }
    audit_payload_changes = {
        path for path in changed_paths
        if path in {"audits/INDEX.tsv", "audits/EVENTS.tsv"}
        or path.startswith("audits/lean/")
    }
    if not added:
        if added_events:
            if len(added_events) != 1 or changed_paths != {"audits/EVENTS.tsv"}:
                fail("one audit-qualification pull request may append exactly one event")
            event_head = detect_audit_head(root, base_commit)
            event_line = git_text(
                root, "rev-list", "--parents", "-n", "1", event_head,
            ).split()
            if len(event_line) != 2:
                fail("an audit-qualification pull request must use one non-merge commit")
            event_parent = event_line[1]
            if git(
                root, "merge-base", "--is-ancestor", event_parent, base_commit,
                allow_failure=True,
            ).returncode:
                fail("an audit-qualification pull request must use one non-merge commit")
            event_changes = {
                path for path in git_text(
                    root, "diff", "--name-only", event_parent, event_head,
                ).splitlines() if path
            }
            if event_changes != {"audits/EVENTS.tsv"}:
                fail("an audit-qualification pull request must use one non-merge commit")
            return
        if audit_payload_changes:
            fail("audit package changed without a new audit_id")
        return
    if added_events:
        fail("a new audit package and a qualification event require separate pull requests")
    if len(added) != 1:
        fail("one pull request may add exactly one Lean audit package")
    audit_id = added[0]
    row = current_by_id[audit_id]
    allowed_prefix = f"audits/lean/{audit_id}/"
    unsupported = sorted(
        path for path in changed_paths
        if path != "audits/INDEX.tsv" and not path.startswith(allowed_prefix)
    )
    if unsupported:
        fail("Lean audit pull request changes unrelated paths: " + ", ".join(unsupported))
    source_commit = row["source_commit"].strip()
    audit_head = detect_audit_head(root, base_commit)
    require_commit(root, audit_head, f"{audit_id} record commit")
    source_line = git_text(
        root, "rev-list", "--parents", "-n", "1", source_commit,
    ).split()
    record_line = git_text(
        root, "rev-list", "--parents", "-n", "1", audit_head,
    ).split()
    if len(source_line) != 2 or len(record_line) != 2:
        fail(f"{audit_id} source and record commits must not be merge commits")
    source_parent = source_line[1]
    record_parent = record_line[1]
    require_ancestor(
        root, source_parent, base_commit,
        f"{audit_id} source-branch base",
    )
    if record_parent != source_commit:
        fail(f"{audit_id} must have exactly one source commit and one record commit")
    source_changes = {
        path for path in git_text(
            root, "diff", "--name-only", source_parent, source_commit,
        ).splitlines() if path
    }
    if not source_changes or any(
        not path.startswith(allowed_prefix)
        or Path(path).name in RECORD_FILES
        for path in source_changes
    ):
        fail(f"{audit_id} source commit changes files outside its immutable source package")
    expected_record_changes = {
        "audits/INDEX.tsv",
        *(f"{allowed_prefix}{name}" for name in RECORD_FILES),
    }
    record_changes = {
        path for path in git_text(
            root, "diff", "--name-only", source_commit, audit_head,
        ).splitlines() if path
    }
    if record_changes != expected_record_changes:
        fail(f"{audit_id} record commit must add only the index and four records")
    status = current_status(root)
    if (
        row["canon_tag"].strip() != status["TAG"]
        or row["content_commit"].strip() != status["CONTENT_COMMIT"]
    ):
        fail(f"{audit_id} new audit must target the current public Canon edition")
    registry = current_registry(root)
    claim = row["claim_id"].strip()
    if claim not in registry or registry[claim]["status"].strip() not in {"T", "T-LOCK"}:
        fail(f"{audit_id} new audit must target a current theorem claim")
    expected_scope = sha256_bytes(registry[claim]["scope"].encode("utf-8"))
    if row["claim_scope_sha256"].strip() != expected_scope:
        fail(f"{audit_id} new audit scope differs from the current registry")


def validate(root: Path, base_commit: str | None = None) -> int:
    audits = root / "audits"
    allowed_entries = {"README.md", "INDEX.tsv", "EVENTS.tsv", "lean"}
    if not audits.is_dir():
        fail("missing audits directory")
    unexpected = sorted(path.name for path in audits.iterdir() if path.name not in allowed_entries)
    if unexpected:
        fail("audits contains unsupported entries: " + ", ".join(unexpected))
    rows = read_tsv(audits / "INDEX.tsv", AUDIT_FIELDS)
    event_rows = read_tsv(audits / "EVENTS.tsv", EVENT_FIELDS)

    with (root / "canon" / "EVIDENCE.tsv").open(encoding="utf-8", newline="") as handle:
        for number, evidence in enumerate(csv.DictReader(handle, delimiter="\t"), 2):
            if any(
                points_to_supplemental_audits(evidence.get(field, ""))
                for field in ("evidence_id", "location")
            ):
                fail(f"EVIDENCE.tsv line {number} uses a supplemental audit as primary evidence")
    with (root / "canon" / "REGISTRY.tsv").open(encoding="utf-8", newline="") as handle:
        for number, claim in enumerate(csv.DictReader(handle, delimiter="\t"), 2):
            if points_to_supplemental_audits(claim["evidence"]):
                fail(f"REGISTRY.tsv line {number} uses a supplemental audit as primary evidence")
    with (root / "canon" / "HISTORY.tsv").open(encoding="utf-8", newline="") as handle:
        for number, event in enumerate(csv.DictReader(handle, delimiter="\t"), 2):
            if any(
                points_to_supplemental_audits(event.get(field, ""))
                for field in ("evidence_id", "evidence_location")
            ):
                fail(f"HISTORY.tsv line {number} uses a supplemental audit as primary evidence")

    seen_ids: set[str] = set()
    seen_locations: set[str] = set()
    ordered_ids: list[str] = []
    indexed_directories: set[str] = set()
    for number, row in enumerate(rows, 2):
        context = f"audits/INDEX.tsv line {number}"
        for field in AUDIT_FIELDS:
            require_text(row, field, context)
        audit_id = row["audit_id"].strip()
        if not AUDIT_ID.fullmatch(audit_id) or audit_id in seen_ids:
            fail(f"{context} has invalid or duplicate audit_id")
        if row["audit_kind"].strip() != "LEAN4":
            fail(f"{context} has invalid audit_kind")
        if row["profile"].strip() != AUDIT_PROFILE:
            fail(f"{context} has invalid audit profile")
        if row["coverage"].strip() not in {"EXACT", "PARTIAL"}:
            fail(f"{context} has invalid coverage")
        if row["status_effect"].strip() != "NONE":
            fail(f"{context} must have status_effect NONE")
        if not SHA256.fullmatch(row["claim_scope_sha256"].strip()):
            fail(f"{context} has invalid claim scope hash")
        location = row["location"].strip()
        if location != f"audits/lean/{audit_id}" or location in seen_locations:
            fail(f"{context} has invalid or duplicate location")
        if not SHA256.fullmatch(row["source_sha256"].strip()):
            fail(f"{context} has invalid source_sha256")
        if not SHA256.fullmatch(row["records_sha256"].strip()):
            fail(f"{context} has invalid records_sha256")
        if row["hash_mode"].strip() != SOURCE_HASH_MODE:
            fail(f"{context} has invalid hash_mode")
        validate_canon_pin(root, row, context)
        validate_source_pin(root, row, context)
        package = root / Path(location)
        if not package.is_dir():
            fail(f"{audit_id} package is missing")
        validate_package(package, root, row)
        seen_ids.add(audit_id)
        seen_locations.add(location)
        indexed_directories.add(audit_id)
        ordered_ids.append(audit_id)
    if ordered_ids != sorted(ordered_ids):
        fail("audits/INDEX.tsv rows must be sorted by audit_id")

    lean_root = audits / "lean"
    if lean_root.exists():
        actual_directories = {path.name for path in lean_root.iterdir() if path.is_dir()}
        unexpected_files = sorted(path.name for path in lean_root.iterdir() if not path.is_dir())
        if unexpected_files:
            fail("audits/lean contains files outside packages: " + ", ".join(unexpected_files))
        unindexed = sorted(actual_directories - indexed_directories)
        missing = sorted(indexed_directories - actual_directories)
        if unindexed:
            fail("unindexed Lean audit packages: " + ", ".join(unindexed))
        if missing:
            fail("indexed Lean audit packages are missing: " + ", ".join(missing))
    elif indexed_directories:
        fail("audits/lean is missing")

    validate_events(event_rows, {row["audit_id"].strip(): row for row in rows})
    validate_change_set(
        root, rows, event_rows,
        base_commit if base_commit is not None else detect_base_commit(root),
    )
    return len(rows)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    try:
        count = validate(root)
    except AuditError as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"AUDITS PASS lean={count}")


if __name__ == "__main__":
    main()
