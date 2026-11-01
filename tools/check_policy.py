#!/usr/bin/env python3
"""Dependency-free repository policy gate."""

from pathlib import Path
import re
import subprocess

try:  # pragma: no cover - import shim, see check_ledger.py
    from tools import probe_records as _records
    from tools.policy_file_rules import (
        is_forbidden_repository_file,
        public_transcript_integrity_problem,
    )
except ImportError:  # pragma: no cover
    import probe_records as _records
    from policy_file_rules import (
        is_forbidden_repository_file,
        public_transcript_integrity_problem,
    )


ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 5 * 1024 * 1024

ALLOWED_ROOT = {
    ".gitattributes", ".github", ".gitignore", "AGENTS.md", "CITATION.cff",
    "CLAUDE.md", "LICENSE", "POLICY.md", "README.md", "STATUS.md", "canon",
    "data", "legacy", "notes", "probes", "reproduce", "tools",
}
BASE_STATUS_FIELDS = {"STATE", "CANON", "AUTHORITY", "CUTOVER"}
ACTIVE_STATUS_FIELDS = {
    "TAG", "CONTENT_COMMIT", "CANON_SHA256", "CANON_BYTES",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def tracked_files():
    completed = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    for name in completed.stdout.decode("utf-8").split("\0"):
        if name:
            path = ROOT / name
            if path.is_file() or path.is_symlink():
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
    if is_forbidden_repository_file(relative):
        fail(f"forbidden file: {relative}")
    transcript_problem = public_transcript_integrity_problem(path, relative)
    if transcript_problem is not None:
        fail(f"invalid public probe transcript: {relative}: {transcript_problem}")

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
    if not re.fullmatch(r"[0-9a-f]{40}", status["CONTENT_COMMIT"]):
        fail("ACTIVE CONTENT_COMMIT must be a full lowercase SHA")
    if not re.fullmatch(r"[0-9a-f]{64}", status["CANON_SHA256"]):
        fail("ACTIVE CANON_SHA256 must contain 64 lowercase hex characters")
    if not status["CANON_BYTES"].isdigit() or int(status["CANON_BYTES"]) <= 0:
        fail("ACTIVE CANON_BYTES must be a positive integer")

probes = ROOT / "probes"
if probes.exists():
    for probe in sorted(path for path in probes.iterdir() if path.is_dir()):
        if not probe.name.startswith("P-"):
            fail(f"probe directory must start P-: {probe.name}")
        result = probe / "RESULT.md"
        text = result.read_text(encoding="utf-8") if result.is_file() else None
        present = {item.name for item in probe.iterdir() if item.is_file()}
        for problem in _records.problems(present, text):
            fail(f"{probe.name} {problem}")

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
    '  workflow_dispatch:\n\npermissions:',
    'permissions:\n  contents: read\n  actions: read',
    "ref: ${{ github.event_name == 'workflow_dispatch' && '03f010760d85c62795b74b3fa8fde79c2c36be7f' || github.sha }}",
    '      - name: Pin manual recovery to immutable v107\n        if: github.event_name == \'workflow_dispatch\'\n        run: |\n          test "$GITHUB_REPOSITORY" = "mathorn1973/twist-j"\n          test "$GITHUB_SHA" = "$GITHUB_WORKFLOW_SHA"\n          case "$GITHUB_REF" in refs/heads/?*) ;; *) echo "recovery controller requires a branch ref" >&2; exit 1 ;; esac\n          test "$(git rev-parse HEAD)" = "03f010760d85c62795b74b3fa8fde79c2c36be7f"\n          test "$(git cat-file -t refs/tags/canon-v107)" = "tag"\n          test "$(git rev-parse refs/tags/canon-v107)" = "81c57853b7b5126fa2d8ec465b8ad903e2402c04"\n          test "$(git rev-parse \'refs/tags/canon-v107^{commit}\')" = "03f010760d85c62795b74b3fa8fde79c2c36be7f"\n          test "$(git status --porcelain)" = ""\n          echo "RECOVERY CONTROLLER $GITHUB_SHA"\n          echo "RECOVERY RUN $GITHUB_RUN_ID ATTEMPT $GITHUB_RUN_ATTEMPT"\n          echo "RECOVERY SCIENTIFIC CHECKOUT 03f010760d85c62795b74b3fa8fde79c2c36be7f"',
    '      - name: Reproduce every frozen public probe for v107 recovery\n        if: github.event_name == \'workflow_dispatch\'\n        env:\n          PYTHONDONTWRITEBYTECODE: "1"\n        run: python -u tools/check_verifier.py\n      - name: Reproduce every frozen minimal reproduction for v107 recovery\n        if: github.event_name == \'workflow_dispatch\'\n        env:\n          PYTHONDONTWRITEBYTECODE: "1"\n        run: python -u tools/check_reproduce.py',
    "      - name: Run activation readback on immutable publication events\n        if: github.event_name != 'workflow_dispatch'",
    'python -u tools/check_activation.py --post-activation \\\n            --expected-tag canon-v107 \\\n            --manifest-out "$RUNNER_TEMP/v107-recovery/activation-manifest.json"',
    "      - name: Validate v107 recovery assets and bind provenance\n        if: github.event_name == 'workflow_dispatch'",
    "if: (github.ref_type == 'tag' && github.event_name != 'workflow_dispatch') || github.event_name == 'workflow_dispatch'",
    "format('canon-v107-recovery-{0}-{1}', github.run_id, github.run_attempt)",
    "format('{0}/v107-recovery/', runner.temp)",
    'PINNED V107 RECOVERY PASS - complete replay, activation, applicable assets and provenance artifact',
    "permissions:\n  contents: read",
    "jobs:\n  architecture:",
    "name: architecture-${{ matrix.architecture }}",
    "fail-fast: false",
    "architecture: x86_64\n            runner: ubuntu-latest",
    "architecture: aarch64\n            runner: ubuntu-24.04-arm",
    "runs-on: ${{ matrix.runner }}",
    "runs-on: ${{ matrix.runner }}\n    timeout-minutes: 60",
    "  check:\n    if: always() && github.ref_type != 'tag' && github.event_name != 'release' && github.event_name != 'workflow_dispatch'\n    needs: architecture\n    runs-on: ubuntu-latest",
    "needs: architecture\n    runs-on: ubuntu-latest\n    timeout-minutes: 5",
    "if: needs.architecture.result != 'success'",
    "  publication:\n    if: github.ref_type == 'tag' || github.event_name == 'release' || github.event_name == 'workflow_dispatch'\n    runs-on: ubuntu-latest",
    "if: github.ref_type == 'tag' || github.event_name == 'release' || github.event_name == 'workflow_dispatch'\n    runs-on: ubuntu-latest\n    timeout-minutes: 60",
    "actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5",
    "persist-credentials: false",
    "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
    "python tools/check_policy.py",
    "python tools/check_canon.py",
    "python tools/check_ledger.py",
    "python tools/check_verifier.py --base \"$BASE_SHA\"",
    "python tools/check_reproduce.py --base \"$BASE_SHA\"",
    "python tools/check_activation.py --full --post-activation",
    "echo \"TWO-ARCHITECTURE CHECK PASS\"",
):
    if invariant not in workflow:
        fail(f"workflow lacks security invariant: {invariant}")
if workflow.count("runner: ubuntu-latest") != 1:
    fail("workflow must declare exactly one x86_64 matrix runner")
if workflow.count("runner: ubuntu-24.04-arm") != 1:
    fail("workflow must declare exactly one aarch64 matrix runner")
if workflow.count("actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a") != 1:
    fail("workflow must upload the activation manifest exactly once")
publication_at = workflow.find("\n  publication:")
upload_at = workflow.find("actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a")
if publication_at < 0 or upload_at < publication_at:
    fail("activation artifact upload must live only in the publication job")
if "pull_request_target:" in workflow:
    fail("pull_request_target is forbidden")

# Bind the operational receipt implementation reviewed with this controller.
import hashlib
receipt_start = workflow.index('          # BEGIN PINNED V107 RECOVERY RECEIPT\n')
receipt_end_marker = '          # END PINNED V107 RECOVERY RECEIPT\n'
receipt_end = workflow.index(receipt_end_marker, receipt_start) + len(receipt_end_marker)
receipt_source = ''.join(line[10:] if line.startswith('          ') else line for line in workflow[receipt_start:receipt_end].splitlines(keepends=True))
if hashlib.sha256(receipt_source.encode('utf-8')).hexdigest() != 'f1660a1158aa7da17efed781b03161ff125da12360ae5a7fc3fa4288966fe53a':
    fail('v107 recovery receipt differs from its reviewed contract')
for forbidden in ('continue-on-error:', 'workflow_call:', '  inputs:', 'contents: write', 'actions: write'):
    if forbidden in workflow:
        fail('forbidden workflow recovery capability: ' + forbidden)
publication = workflow[publication_at:]
if '--base' in publication:
    fail('publication must not use changed-path replay')
if publication.index('python -u tools/check_verifier.py') > publication.index('python -u tools/check_reproduce.py'):
    fail('recovery probe replay must precede minimal reproductions')
if publication.index('python -u tools/check_reproduce.py') > publication.index('python -u tools/check_activation.py'):
    fail('complete recovery replay must precede activation')
if publication.index('name: Validate v107 recovery assets and bind provenance') > publication.index('name: Preserve tag readback manifest'):
    fail('recovery artifact upload must follow validation')

print("POLICY PASS")
