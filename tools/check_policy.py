#!/usr/bin/env python3
"""Dependency-free repository policy gate."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024

ALLOWED_ROOT = {
    ".gitattributes", ".github", ".gitignore", "AGENTS.md", "CITATION.cff",
    "LICENSE", "POLICY.md", "README.md", "STATUS.md", "canon", "data",
    "legacy", "notes", "probes", "reproduce", "tools",
}
FORBIDDEN_SUFFIXES = {
    ".bak", ".bin", ".dll", ".dylib", ".env", ".exe", ".jam", ".key",
    ".log", ".pem", ".pt", ".pth", ".pyc", ".so", ".token",
}
BASE_STATUS_FIELDS = {"STATE", "CANON", "AUTHORITY", "CUTOVER"}
ACTIVE_STATUS_FIELDS = {
    "TAG", "CANON_COMMIT", "CANON_SHA256", "CANON_BYTES",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def tracked_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            yield path


def read_status() -> dict[str, str]:
    fields: dict[str, str] = {}
    pattern = re.compile(r"^([A-Z][A-Z0-9_]*):\s*(.*?)\s*$")
    for line in (ROOT / "STATUS.md").read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            fields[match.group(1)] = match.group(2)
    return fields


for path in sorted(ROOT.iterdir()):
    if path.name != ".git" and path.name not in ALLOWED_ROOT:
        fail(f"unapproved root entry: {path.name}")

for path in tracked_files():
    relative = path.relative_to(ROOT)
    if path.stat().st_size > MAX_BYTES:
        fail(f"file exceeds 5 MiB: {relative}")
    if path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name.startswith(".env"):
        fail(f"forbidden file: {relative}")

status = read_status()
missing_status = sorted(BASE_STATUS_FIELDS - status.keys())
if missing_status:
    fail("STATUS.md lacks fields: " + ", ".join(missing_status))

state = status["STATE"]
if state not in {"GENESIS", "ACTIVE"}:
    fail("STATUS.md STATE must be GENESIS or ACTIVE")
if state == "GENESIS":
    if status["AUTHORITY"] != "mathorn1973/twistj-jam":
        fail("GENESIS authority must remain mathorn1973/twistj-jam")
    if status["CUTOVER"] != "NOT DECLARED":
        fail("GENESIS CUTOVER must be NOT DECLARED")
else:
    missing_active = sorted(ACTIVE_STATUS_FIELDS - status.keys())
    if missing_active:
        fail("ACTIVE STATUS.md lacks fields: " + ", ".join(missing_active))
    if status["AUTHORITY"] != "mathorn1973/twist-j main":
        fail("ACTIVE authority must be mathorn1973/twist-j main")
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", status["CUTOVER"]):
        fail("ACTIVE CUTOVER must be an ISO date")
    if not re.fullmatch(r"canon-v[1-9][0-9]*", status["TAG"]):
        fail("ACTIVE TAG must be canon-vN")
    if not re.fullmatch(r"[0-9a-f]{40}", status["CANON_COMMIT"]):
        fail("ACTIVE CANON_COMMIT must be a full lowercase SHA")
    if not re.fullmatch(r"[0-9a-f]{64}", status["CANON_SHA256"]):
        fail("ACTIVE CANON_SHA256 must contain 64 lowercase hex characters")
    if not status["CANON_BYTES"].isdigit() or int(status["CANON_BYTES"]) <= 0:
        fail("ACTIVE CANON_BYTES must be a positive integer")

probes = ROOT / "probes"
if probes.exists():
    for probe in sorted(path for path in probes.iterdir() if path.is_dir()):
        if not probe.name.startswith("P-"):
            fail(f"probe directory must start P-: {probe.name}")
        for required in (
            "PREREG.md", "verify.py", "EXPECTED.txt", "RUN.md", "RESULT.md"
        ):
            if not (probe / required).is_file():
                fail(f"{probe.name} lacks {required}")

reproduce = ROOT / "reproduce"
if reproduce.exists():
    for item in sorted(path for path in reproduce.iterdir() if path.is_dir()):
        for required in ("verify.py", "EXPECTED.txt", "README.md"):
            if not (item / required).is_file():
                fail(f"{item.name} lacks {required}")

workflows = ROOT / ".github" / "workflows"
workflow_files = {path.name for path in workflows.iterdir() if path.is_file()}
if workflow_files != {"policy.yml"}:
    fail("policy.yml must be the only workflow")
workflow = (workflows / "policy.yml").read_text(encoding="utf-8")
for invariant in (
    "permissions:\n  contents: read",
    "timeout-minutes: 15",
    "actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5",
    "persist-credentials: false",
    "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
    "python tools/check_policy.py",
    "python tools/check_canon.py",
    "python tools/check_verifier.py --base \"$BASE_SHA\"",
    "python tools/check_reproduce.py --base \"$BASE_SHA\"",
):
    if invariant not in workflow:
        fail(f"workflow lacks security invariant: {invariant}")
if "pull_request_target:" in workflow:
    fail("pull_request_target is forbidden")

print("POLICY PASS")
