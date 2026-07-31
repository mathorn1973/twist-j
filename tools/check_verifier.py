#!/usr/bin/env python3
"""Reproduce every probe changed by a pull request."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import os
import platform as host_platform
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PROBES = ROOT / "probes"
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
RUN_MACHINE_NICKNAMES = ("JAS 2", "TWISTER")
LOCAL_LEG_FIELDS = (
    "platform",
    "architecture",
    "python",
    "exit_code",
    "stdout_sha256",
    "stdout_bytes",
    "stdout_lines",
    "stderr_sha256",
    "stderr_bytes",
)
GITHUB_LEG_FIELDS = (
    "platform",
    "architecture",
    "python",
    "verifier_sha256",
    "stdout_sha256",
)
GITHUB_OUTCOMES = (
    ("status", "PASS"),
    ("verdict", "VERIFY PASS"),
    ("byte_identity", "PASS"),
    ("replay", "PASS"),
)
LEG_MACHINE_FIELDS = set(LOCAL_LEG_FIELDS) | set(GITHUB_LEG_FIELDS) | {
    name for name, _ in GITHUB_OUTCOMES
}
REPEATED_LEG_FIELDS = LEG_MACHINE_FIELDS
GITHUB_PREFIXES = ("github", "x86", "x86_64")
SINGLETON_FIELDS = ("pin_commit", "command")
REQUIRED = {
    "pin_commit",
    "verifier_sha256",
    "command",
    "platform",
    "architecture",
    "python",
    "exit_code",
    "stdout_sha256",
    "stdout_bytes",
    "stdout_lines",
    "stderr_sha256",
    "stderr_bytes",
}


@dataclass(frozen=True)
class RunRecord:
    fields: dict[str, str]
    sections: dict[str, dict[str, str]]
    occurrences: dict[str, tuple[str, ...]]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def touches_canon(paths: "list[str]") -> bool:
    """True when a changed path lies under canon/.

    A Canon change can invalidate a verifier that reads canon/ at run time even
    though that verifier's own directory is untouched, so the changed-path
    selection below widens to every directory when this returns True.
    """
    return any(Path(raw).parts[:1] == ("canon",) for raw in paths if raw)


def changed_probes(base: str | None) -> list[Path]:
    if not PROBES.exists():
        return []
    if not base:
        return sorted(path for path in PROBES.iterdir() if path.is_dir())
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base):
        fail("base SHA must contain 40 hexadecimal characters")
    command = ["git", "diff", "--name-only", f"{base}...HEAD"]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        fail(f"cannot read changed paths: {result.stderr.strip()}")
    changed = result.stdout.splitlines()
    names = set()
    for raw in changed:
        parts = Path(raw).parts
        if len(parts) >= 3 and parts[0] == "probes":
            names.add(parts[1])
    if len(names) > 1:
        fail("a pull request may change only one probe directory")
    if touches_canon(changed):
        print("VERIFY FULL SWEEP canon change")
        return sorted(path for path in PROBES.iterdir() if path.is_dir())
    return [PROBES / name for name in sorted(names)]


def parse_run(text: str, label: str) -> RunRecord:
    """Parse the legacy flat view and preserve every level-two run section."""
    fields: dict[str, str] = {}
    sections: dict[str, dict[str, str]] = {}
    occurrences: dict[str, list[str]] = {}
    pattern = re.compile(r"^([a-z][a-z0-9_]*):\s*(.*?)\s*$")
    heading_pattern = re.compile(r"^##\s+(.+?)\s*$")
    section: str | None = None
    for line in text.splitlines():
        heading = heading_pattern.match(line)
        if heading:
            section = heading.group(1).strip().lower()
            if section in sections:
                fail(f"{label} repeats section {section!r}")
            sections[section] = {}
            continue
        match = pattern.match(line)
        if match:
            key, value = match.groups()
            # The first occurrence belongs to the local leg in house records.
            fields.setdefault(key, value)
            occurrences.setdefault(key, []).append(value)
            if section is not None:
                scoped = sections[section]
                if key in scoped:
                    fail(f"{label} repeats {key} inside section {section!r}")
                scoped[key] = value
    for key in SINGLETON_FIELDS:
        if len(occurrences.get(key, ())) > 1:
            fail(f"{label} repeats singleton field {key}")
    for key in REQUIRED:
        if key not in fields and f"local_{key}" in fields:
            fields[key] = fields[f"local_{key}"]
    missing = sorted(REQUIRED - fields.keys())
    if missing:
        fail(f"{label} lacks fields: {', '.join(missing)}")
    return RunRecord(
        fields=fields,
        sections=sections,
        occurrences={key: tuple(values) for key, values in occurrences.items()},
    )


def read_run(path: Path) -> RunRecord:
    return parse_run(
        path.read_text(encoding="utf-8"),
        path.relative_to(ROOT).as_posix(),
    )


def leg_fields(
    section: dict[str, str],
    prefix: str,
    names: tuple[str, ...],
    probe: str,
) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in names:
        plain = section.get(name)
        explicit = section.get(f"{prefix}_{name}")
        if plain is not None and explicit is not None and plain != explicit:
            fail(f"{probe} has conflicting {prefix} {name}")
        value = explicit if explicit is not None else plain
        if value is None:
            fail(f"{probe} lacks {prefix} {name}")
        result[name] = value
    return result


def optional_leg_field(
    section: dict[str, str],
    prefix: str,
    name: str,
    probe: str,
) -> str | None:
    plain = section.get(name)
    explicit = section.get(f"{prefix}_{name}")
    if plain is not None and explicit is not None and plain != explicit:
        fail(f"{probe} has conflicting {prefix} {name}")
    return explicit if explicit is not None else plain


def named_fields(
    fields: dict[str, str],
    prefix: str,
    names: tuple[str, ...],
    probe: str,
) -> dict[str, str]:
    result: dict[str, str] = {}
    for name in names:
        key = f"{prefix}_{name}"
        if key not in fields:
            fail(f"{probe} lacks {prefix} {name}")
        result[name] = fields[key]
    return result


def named_aliases(record: RunRecord) -> list[str]:
    return [
        prefix
        for prefix in GITHUB_PREFIXES
        if any(
            f"{prefix}_{name}" in record.occurrences
            for name in LEG_MACHINE_FIELDS
        )
    ]


def require_named_singletons(
    record: RunRecord,
    prefixes: tuple[str, ...],
    probe: str,
) -> None:
    for prefix in prefixes:
        for name in LEG_MACHINE_FIELDS:
            key = f"{prefix}_{name}"
            count = len(record.occurrences.get(key, ()))
            if count > 1:
                fail(f"{probe} repeats named run field {key}")


def validate_structured_occurrences(
    record: RunRecord,
    local_section: dict[str, str],
    github_section: dict[str, str],
    probe: str,
) -> None:
    for name in LEG_MACHINE_FIELDS:
        expected = int(name in local_section) + int(name in github_section)
        if name == "verifier_sha256":
            expected += 1
        actual = len(record.occurrences.get(name, ()))
        if actual != expected:
            fail(f"{probe} has unexpected occurrences of {name}")
    for prefix, section in (
        ("local", local_section),
        ("github", github_section),
    ):
        for name in LEG_MACHINE_FIELDS:
            key = f"{prefix}_{name}"
            expected = int(key in section)
            actual = len(record.occurrences.get(key, ()))
            if actual != expected:
                fail(f"{probe} has unexpected occurrences of {key}")
    aliases = named_aliases(record)
    if any(prefix in {"x86", "x86_64"} for prefix in aliases):
        fail(f"{probe} mixes structured and named GitHub leg formats")


def classify_leg_pair(
    local: dict[str, str],
    github: dict[str, str],
    probe: str,
    verifier_hash: str,
    expected_hash: str,
    github_success: bool,
) -> str:
    for label, leg in (("local", local), ("GitHub", github)):
        for name in ("platform", "architecture", "python"):
            if not leg[name]:
                fail(f"{probe} has empty recorded {label} {name}")
    if local["architecture"] not in {"aarch64", "x86_64"}:
        fail(f"{probe} local architecture must be x86_64 or aarch64")
    if github["architecture"] != "x86_64":
        fail(f"{probe} recorded GitHub architecture must be x86_64")
    if local["exit_code"] != "0":
        fail(f"{probe} recorded local exit_code is not zero")
    if (
        local["stderr_sha256"] != EMPTY_SHA256
        or local["stderr_bytes"] != "0"
    ):
        fail(f"{probe} recorded local stderr is not empty")
    if local["stdout_sha256"] != expected_hash:
        fail(f"{probe} recorded local stdout differs from EXPECTED.txt")
    if github["stdout_sha256"] != expected_hash:
        fail(f"{probe} recorded GitHub stdout differs from EXPECTED.txt")
    if github["verifier_sha256"] != verifier_hash:
        fail(f"{probe} recorded GitHub verifier SHA-256 differs")
    if not github_success:
        fail(f"{probe} lacks a successful recorded GitHub leg")
    if local["architecture"] == "aarch64":
        return "TWO-ARCHITECTURE"
    return "REPRODUCTION-ONLY"


def recorded_leg_class(
    record: RunRecord,
    probe: str,
    verifier_hash: str,
    expected_hash: str,
) -> str:
    """Validate structured legs and classify their architecture evidence."""
    local_section = record.sections.get("local formal leg")
    github_section = record.sections.get("required github leg")
    if local_section is None and github_section is None:
        repeated = sorted(
            key
            for key in REPEATED_LEG_FIELDS
            if len(record.occurrences.get(key, ())) > 1
        )
        if repeated:
            fail(
                f"{probe} repeats unstructured run fields: "
                + ", ".join(repeated)
            )
        aliases = named_aliases(record)
        if len(aliases) > 1:
            fail(f"{probe} has multiple named GitHub leg formats")
        has_named_local = any(
            f"local_{name}" in record.occurrences
            for name in LEG_MACHINE_FIELDS
        )
        if not aliases:
            if has_named_local:
                fail(f"{probe} has a named local leg without a GitHub leg")
            return "LEGACY"
        prefix = aliases[0]
        require_named_singletons(
            record,
            ("local", prefix),
            probe,
        )
        required = GITHUB_LEG_FIELDS + ("exit_code", "stderr_bytes")
        missing = [
            name
            for name in required
            if f"{prefix}_{name}" not in record.fields
        ]
        strict_named = (
            prefix != "github"
            or has_named_local
            or any(
                f"github_{name}" in record.fields
                for name in (
                    "verifier_sha256",
                    "stdout_sha256",
                    "exit_code",
                    "stderr_bytes",
                )
            )
        )
        if missing:
            if strict_named:
                fail(
                    f"{probe} has incomplete {prefix} leg: "
                    + ", ".join(missing)
                )
            return "LEGACY"
        local = {
            name: record.fields[name]
            for name in LOCAL_LEG_FIELDS
        }
        if has_named_local:
            local = named_fields(
                record.fields, "local", LOCAL_LEG_FIELDS, probe
            )
            for name, value in local.items():
                if record.fields[name] != value:
                    fail(f"{probe} has conflicting flat/local {name}")
            local_verifier = record.fields.get("local_verifier_sha256")
            if local_verifier is not None and local_verifier != verifier_hash:
                fail(f"{probe} recorded local verifier SHA-256 differs")
        github = named_fields(
            record.fields, prefix, GITHUB_LEG_FIELDS, probe
        )
        github_exit = record.fields[f"{prefix}_exit_code"]
        github_stderr_bytes = record.fields[f"{prefix}_stderr_bytes"]
        if github_exit != "0":
            fail(f"{probe} recorded GitHub exit_code is not zero")
        if github_stderr_bytes != "0":
            fail(f"{probe} recorded GitHub stderr is not empty")
        github_stderr_hash = record.fields.get(f"{prefix}_stderr_sha256")
        if github_stderr_hash is not None and github_stderr_hash != EMPTY_SHA256:
            fail(f"{probe} recorded GitHub stderr SHA-256 is not empty")
        for suffix, accepted in GITHUB_OUTCOMES:
            value = record.fields.get(f"{prefix}_{suffix}")
            if value is not None and value != accepted:
                fail(f"{probe} recorded GitHub {suffix} is not {accepted}")
        return classify_leg_pair(
            local,
            github,
            probe,
            verifier_hash,
            expected_hash,
            github_success=True,
        )
    if local_section is None or github_section is None:
        fail(f"{probe} has only one structured run leg")

    validate_structured_occurrences(
        record,
        local_section,
        github_section,
        probe,
    )
    local = leg_fields(local_section, "local", LOCAL_LEG_FIELDS, probe)
    github = leg_fields(github_section, "github", GITHUB_LEG_FIELDS, probe)
    for name, value in local.items():
        if record.fields[name] != value:
            fail(f"{probe} has conflicting flat/local {name}")
    local_verifier = optional_leg_field(
        local_section, "local", "verifier_sha256", probe
    )
    if local_verifier is not None and local_verifier != verifier_hash:
        fail(f"{probe} recorded local verifier SHA-256 differs")

    github_exit = optional_leg_field(
        github_section, "github", "exit_code", probe
    )
    github_stderr_bytes = optional_leg_field(
        github_section, "github", "stderr_bytes", probe
    )
    github_stderr_hash = optional_leg_field(
        github_section, "github", "stderr_sha256", probe
    )
    if github_exit is not None and github_exit != "0":
        fail(f"{probe} recorded GitHub exit_code is not zero")
    if github_stderr_bytes is not None and github_stderr_bytes != "0":
        fail(f"{probe} recorded GitHub stderr is not empty")
    if github_stderr_hash is not None and github_stderr_hash != EMPTY_SHA256:
        fail(f"{probe} recorded GitHub stderr SHA-256 is not empty")
    if (github_exit is None) != (github_stderr_bytes is None):
        fail(f"{probe} has incomplete GitHub exit/stderr fields")

    outcomes = {}
    for name, accepted in GITHUB_OUTCOMES:
        value = optional_leg_field(
            github_section, "github", name, probe
        )
        if value is not None and value != accepted:
            fail(f"{probe} recorded GitHub {name} is not {accepted}")
        outcomes[name] = value
    explicit_success = github_exit is not None and github_stderr_bytes is not None
    # Older records store the checker's terminal PASS instead of exit/stderr
    # fields. The present job independently reruns and enforces both conditions.
    legacy_success = (
        outcomes["status"] == "PASS"
        and outcomes["verdict"] == "VERIFY PASS"
    )
    return classify_leg_pair(
        local,
        github,
        probe,
        verifier_hash,
        expected_hash,
        github_success=explicit_success or legacy_success,
    )


def as_nonnegative_int(value: str, field: str, probe: str) -> int:
    try:
        number = int(value)
    except ValueError:
        fail(f"{probe} has invalid {field}")
    if number < 0:
        fail(f"{probe} has negative {field}")
    return number


def reproduce(probe: Path) -> None:
    name = probe.name
    verifier = probe / "verify.py"
    expected_path = probe / "EXPECTED.txt"
    run_path = probe / "RUN.md"
    for path in (verifier, expected_path, run_path):
        if not path.is_file():
            fail(f"{name} lacks {path.name}")

    record = read_run(run_path)
    fields = record.fields
    relative_verifier = verifier.relative_to(ROOT).as_posix()
    expected_command = f"python3 {relative_verifier}"
    if fields["command"] != expected_command:
        fail(f"{name} command must be: {expected_command}")
    if not re.fullmatch(r"[0-9a-f]{40}", fields["pin_commit"]):
        fail(f"{name} pin_commit must be a full lowercase SHA")
    for field in ("platform", "architecture", "python"):
        if not fields[field]:
            fail(f"{name} has empty {field}")
    if fields["architecture"] not in {"x86_64", "aarch64"}:
        fail(f"{name} architecture must be x86_64 or aarch64")

    verifier_bytes = verifier.read_bytes()
    verifier_hash = sha256(verifier_bytes)
    if fields["verifier_sha256"] != verifier_hash:
        fail(f"{name} verifier SHA-256 differs from RUN.md")
    pinned = subprocess.run(
        ["git", "show", f"{fields['pin_commit']}:{relative_verifier}"],
        cwd=ROOT,
        capture_output=True,
    )
    if pinned.returncode or sha256(pinned.stdout) != verifier_hash:
        fail(f"{name} verifier does not match its pin_commit")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", fields["pin_commit"], "HEAD"],
        cwd=ROOT,
    )
    if ancestor.returncode:
        fail(f"{name} pin_commit is not an ancestor of HEAD")

    expected = expected_path.read_bytes()
    if fields["stdout_sha256"] != sha256(expected):
        fail(f"{name} EXPECTED.txt SHA-256 differs from RUN.md")
    if as_nonnegative_int(fields["stdout_bytes"], "stdout_bytes", name) != len(expected):
        fail(f"{name} EXPECTED.txt byte count differs from RUN.md")
    if as_nonnegative_int(fields["stdout_lines"], "stdout_lines", name) != len(expected.splitlines()):
        fail(f"{name} EXPECTED.txt line count differs from RUN.md")
    if fields["exit_code"] != "0":
        fail(f"{name} local exit_code is not zero")
    if fields["stderr_sha256"] != EMPTY_SHA256 or fields["stderr_bytes"] != "0":
        fail(f"{name} local stderr is not empty")
    leg_class = recorded_leg_class(
        record,
        name,
        verifier_hash,
        sha256(expected),
    )

    if os.environ.get("GITHUB_ACTIONS") == "true":
        github_architecture = host_platform.machine()
        if github_architecture not in {"x86_64", "aarch64"}:
            fail(
                f"{name} GitHub runner architecture must be x86_64 or "
                f"aarch64, received {github_architecture}"
            )
        print(f"VERIFY ARCHITECTURE {name} {github_architecture}")

    environment = os.environ.copy()
    environment.update(
        {
            "LC_ALL": "C",
            "LANG": "C",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "TZ": "UTC",
        }
    )
    result = subprocess.run(
        [sys.executable, relative_verifier],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        timeout=600,
    )
    if result.returncode != 0:
        fail(f"{name} GitHub run exits {result.returncode}")
    if result.stderr:
        fail(f"{name} GitHub run writes {len(result.stderr)} stderr bytes")
    if result.stdout != expected:
        fail(
            f"{name} stdout mismatch: expected {sha256(expected)}, "
            f"received {sha256(result.stdout)}"
        )
    if leg_class != "LEGACY":
        print(f"RUN RECORD {name} {leg_class}")
    print(f"VERIFY PASS {name} {verifier_hash} {sha256(result.stdout)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    args = parser.parse_args()
    probes = changed_probes(args.base)
    if not probes:
        print("VERIFY NOT APPLICABLE")
        return
    for probe in probes:
        reproduce(probe)


if __name__ == "__main__":
    main()
