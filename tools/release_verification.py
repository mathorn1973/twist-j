#!/usr/bin/env python3
"""Execute complete architecture evidence once; verify its origin before reuse.

This is an operational controller. Scientific verifiers, their environments,
limits and expected bytes remain governed by the existing replay runners.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile
import zipfile

try:
    from tools.check_activation import manifest, read_status
    from tools.check_release_manifest import validate_manifest
    from tools import probe_records
except ModuleNotFoundError:
    from check_activation import manifest, read_status
    from check_release_manifest import validate_manifest
    import probe_records

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "mathorn1973/twist-j"
REPOSITORY_ID = 1298077581
WORKFLOW_ID = 311597448
WORKFLOW = ".github/workflows/policy.yml"
ARCHITECTURES = {"x86_64": "ubuntu-latest", "aarch64": "ubuntu-24.04-arm"}
RECEIPT_SCHEMA = "twistj-complete-verification-v1"
PROOF_SCHEMA = "twistj-verification-reuse-v1"
RECEIPT_FILE = "architecture-verification.json"
REPLAY_STEP = "Replay or reuse verified evidence"
UPLOAD_STEP = "Preserve complete architecture verification"
STATIC_STEPS = (
    "Run python tools/check_policy.py",
    "Run python -m unittest discover -s tools -p 'test_*.py'",
    "Run python tools/check_canon.py",
    "Run python tools/check_ledger.py",
    "Run python tools/check_gate_contract.py",
)
CONTROLS = {
    WORKFLOW, "POLICY.md", "AGENTS.md", "STATUS.md",
    "tools/release_verification.py", "tools/check_policy.py",
    "tools/check_activation.py", "tools/check_release_manifest.py",
    "tools/check_verifier.py", "tools/check_reproduce.py",
    "tools/probe_replay_context.py", "tools/probe_replay_contexts.json",
    "tools/probe_records.py", "tools/policy_file_rules.py",
}
SHA40 = re.compile(r"[0-9a-f]{40}")
SHA256 = re.compile(r"[0-9a-f]{64}")
MAX_ARCHIVE = 8 * 1024 * 1024
MAX_ENTRY = 4 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def exact(data, expected, label):
    require(isinstance(data, dict), label + " is not an object")
    require(all(type(data.get(k)) is type(v) and data[k] == v for k, v in expected.items()),
            label + " identity mismatch")


def positive(value):
    require(type(value) is int and value > 0, "invalid positive identifier")
    return value


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(data):
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode("utf-8")


def decode(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def git_bytes(root, *args):
    return subprocess.run(["git", *args], cwd=root, check=True,
                          capture_output=True).stdout


def git(root, *args):
    return git_bytes(root, *args).decode().strip()


def clean(root):
    require(not git(root, "status", "--porcelain"), "verification requires a clean checkout")


def snapshot(root):
    clean(root)
    files = manifest(root, "", "", False)["files"]
    return {"commit": git(root, "rev-parse", "HEAD"),
            "tree": git(root, "rev-parse", "HEAD^{tree}"),
            "inventory_sha256": sha(encode(files)),
            "workflow_sha256": sha((root / WORKFLOW).read_bytes())}


def names(root, directory):
    return sorted(p.name for p in (root / directory).iterdir() if p.is_dir())


def parse_replay(root, category, output):
    """Require one genuine runner disposition for every current directory."""
    records = {}
    inventory = names(root, category)
    prefix = "VERIFY" if category == "probes" else "REPRODUCE"
    for line in output.decode("utf-8").splitlines():
        match = re.fullmatch(prefix + r" PASS (\S+) ([0-9a-f]{64}) ([0-9a-f]{64})", line)
        abandoned = re.fullmatch(r"VERIFY ABANDONED (\S+) no completed gate, nothing to reproduce", line)
        if match:
            name, verifier, expected = match.groups()
            require(name in inventory, "unexpected replay path")
            require(name not in records, "duplicate replay disposition: " + name)
            directory = root / category / name
            require(verifier == sha((directory / "verify.py").read_bytes()), "verifier hash mismatch")
            require(expected == sha((directory / "EXPECTED.txt").read_bytes()), "stdout hash mismatch")
            records[name] = {"result": "PASS", "verifier_sha256": verifier, "stdout_sha256": expected}
        elif abandoned and category == "probes":
            name = abandoned.group(1)
            require(name not in records, "duplicate abandoned disposition")
            records[name] = {"result": "ABANDONED"}
    validate_records(root, category, records)
    return records


def validate_records(root, category, records):
    require(isinstance(records, dict) and sorted(records) == names(root, category),
            "receipt has incomplete " + category + " inventory")
    for name, record in records.items():
        directory = root / category / name
        if category == "probes":
            result = (directory / "RESULT.md").read_text(encoding="utf-8")
            present = {p.name for p in directory.iterdir() if p.is_file()}
            require(not probe_records.problems(present, result), "invalid probe record: " + name)
            if probe_records.declares_abandoned(result):
                require(record == {"result": "ABANDONED"}, "abandoned disposition mismatch: " + name)
                continue
        expected = {"result": "PASS", "verifier_sha256": sha((directory / "verify.py").read_bytes()),
                    "stdout_sha256": sha((directory / "EXPECTED.txt").read_bytes())}
        require(record == expected, "receipt replay mismatch: " + name)


def full_scope(root, base):
    require(bool(SHA40.fullmatch(base)), "invalid comparison base")
    changed = git(root, "diff", "--name-only", base + "...HEAD").splitlines()
    # A complete replay must not bypass the unchanged changed-path runner's
    # one-probe-per-PR rule by omitting --base.
    probes = {p.split("/")[1] for p in changed if p.startswith("probes/") and p.count("/") >= 2}
    require(len(probes) <= 1, "a pull request may change only one probe directory")
    return any(p.startswith("canon/") or p in CONTROLS for p in changed)


def github_context(root, environment):
    exact(dict(environment), {"GITHUB_ACTIONS": "true", "GITHUB_SERVER_URL": "https://github.com",
          "GITHUB_REPOSITORY": REPOSITORY, "GITHUB_REPOSITORY_ID": str(REPOSITORY_ID)}, "CI context")
    event = decode(Path(environment["GITHUB_EVENT_PATH"]).read_bytes())
    event_name = environment["GITHUB_EVENT_NAME"]
    require(event_name in {"pull_request", "push", "release"}, "unsupported CI event")
    ref = environment["GITHUB_REF"]
    require(environment["GITHUB_WORKFLOW_REF"] == REPOSITORY + "/" + WORKFLOW + "@" + ref,
            "foreign workflow ref")
    revision = environment["GITHUB_SHA"]
    require(bool(SHA40.fullmatch(revision)) and revision == environment["GITHUB_WORKFLOW_SHA"],
            "workflow revision mismatch")
    require(git_bytes(root, "show", revision + ":" + WORKFLOW) ==
            (root / WORKFLOW).read_bytes(), "executing workflow differs from checkout")
    for key in ("GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT"):
        require(bool(re.fullmatch(r"[1-9][0-9]*", environment[key])), "invalid CI run identity")
    return event_name, event, ref, revision


def prepare_complete_context(root, environment, base):
    kind, event, ref, workflow_commit = github_context(root, environment)
    pr_number = None
    if kind == "pull_request":
        pr = event["pull_request"]
        pr_number = positive(event["number"])
        require(ref == f"refs/pull/{pr_number}/merge", "unexpected PR ref")
        for side in ("head", "base"):
            exact(pr[side]["repo"], {"id": REPOSITORY_ID, "full_name": REPOSITORY}, "PR repository")
        require(pr["base"]["ref"] == "main" and pr["base"]["sha"] == base, "PR base mismatch")
        candidate = pr["head"]["sha"]
        require(bool(SHA40.fullmatch(candidate)), "invalid PR head")
        git(root, "merge-base", "--is-ancestor", base, candidate)
        require(git(root, "rev-parse", candidate + "^{tree}") == git(root, "rev-parse", "HEAD^{tree}"),
                "refresh the candidate: tested merge tree differs from PR head")
        # Execute science at the immutable candidate, not the synthetic merge SHA.
        git(root, "checkout", "--detach", candidate)
    else:
        require(kind == "push" and ref == "refs/heads/main", "only PR or main can execute a complete receipt")
        candidate = git(root, "rev-parse", "HEAD")
        require(candidate == workflow_commit and event["after"] == candidate and event["before"] == base,
                "main push identity mismatch")
        git(root, "merge-base", "--is-ancestor", base, candidate)
    return {"event": kind, "ref": ref, "pr_number": pr_number, "base": base,
            "workflow_commit": workflow_commit,
            "run_id": int(environment["GITHUB_RUN_ID"]),
            "run_attempt": int(environment["GITHUB_RUN_ATTEMPT"])}


def replay(root, script, base=None):
    command = [sys.executable, "tools/" + script]
    if base is not None:
        command += ["--base", base]
    environment = os.environ.copy()
    for key in ("GH_TOKEN", "GITHUB_TOKEN", "ACTIONS_RUNTIME_TOKEN", "ACTIONS_RESULTS_TOKEN"):
        environment.pop(key, None)
    result = subprocess.run(command, cwd=root, env=environment, capture_output=True)
    sys.stdout.buffer.write(result.stdout)
    sys.stdout.buffer.write(result.stderr)
    sys.stdout.flush()
    require(result.returncode == 0, "replay failed: " + script)
    return result.stdout


class GitHub:
    """Read-only REST transport. No arbitrary host, shell interpolation or writes."""
    def raw(self, path, binary=False):
        command = ["gh", "api", "--hostname", "github.com", "--method", "GET",
                   "repos/" + REPOSITORY + "/" + path]
        if binary:
            command += ["-H", "Accept: application/octet-stream"]
        return subprocess.run(command, check=True, capture_output=True, timeout=60).stdout

    def json(self, path):
        return decode(self.raw(path))

    def pages(self, path, key=None):
        collected = []
        for page in range(1, 11):
            data = self.json(path + ("&" if "?" in path else "?") + f"per_page=100&page={page}")
            items = data[key] if key else data
            require(isinstance(items, list), "invalid API page")
            collected.extend(items)
            if len(items) < 100:
                return collected
        raise ValueError("API pagination exceeded audit bound")


def unpack(archive, metadata, filename):
    require(len(archive) <= MAX_ARCHIVE, "oversized artifact archive")
    exact(metadata, {"size_in_bytes": len(archive), "digest": "sha256:" + sha(archive), "expired": False},
          "artifact bytes")
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        require(bundle.namelist() == [filename], "artifact entry set mismatch")
        info = bundle.infolist()[0]
        require(info.file_size <= MAX_ENTRY and not info.is_dir() and not info.flag_bits & 1,
                "invalid artifact entry")
        return bundle.read(filename)


def successful_steps(job, required):
    exact(job, {"status": "completed", "conclusion": "success"}, "job")
    steps = job.get("steps")
    require(isinstance(steps, list), "missing job steps")
    for name in required:
        selected = [step for step in steps if step.get("name") == name]
        require(len(selected) == 1, "missing or repeated step: " + name)
        exact(selected[0], {"status": "completed", "conclusion": "success"}, "step " + name)
    require(all(s.get("status") == "completed" and s.get("conclusion") in {"success", "skipped"}
                for s in steps), "unsuccessful job step")


def transfer_context(root, api, current=None):
    current = current or snapshot(root)
    parents = git(root, "show", "-s", "--format=%P", current["commit"]).split()
    if len(parents) != 2:
        return current, None
    base, head = parents
    if git(root, "rev-parse", head + "^{tree}") != current["tree"]:
        return current, None
    try:
        git(root, "merge-base", "--is-ancestor", base, head)
    except subprocess.CalledProcessError:
        return current, None
    associated = api.pages("commits/" + current["commit"] + "/pulls")
    matching = [p for p in associated if p.get("merge_commit_sha") == current["commit"]
                and p.get("head", {}).get("sha") == head]
    require(len(matching) == 1, "merge must identify exactly one reviewed PR")
    pr = api.json("pulls/" + str(positive(matching[0]["number"])))
    exact(pr, {"number": matching[0]["number"], "state": "closed", "merged": True,
               "merge_commit_sha": current["commit"]}, "merged PR")
    exact(pr["head"], {"sha": head}, "merged PR head")
    exact(pr["base"], {"ref": "main"}, "merged PR base")
    for side in ("head", "base"):
        exact(pr[side]["repo"], {"id": REPOSITORY_ID, "full_name": REPOSITORY}, "merged PR repository")
    return current, {"base": base, "head": head, "pr_number": pr["number"]}


def validate_receipt(root, receipt, current, run, architecture, transfer, api):
    source = run["head_sha"]
    exact(receipt, {"schema": RECEIPT_SCHEMA, "mode": "executed", "complete": True,
          "repository": REPOSITORY, "repository_id": REPOSITORY_ID,
          "workflow_id": WORKFLOW_ID, "workflow_path": WORKFLOW,
          "run_id": run["id"], "run_attempt": run["run_attempt"],
          "commit": source, "tree": current["tree"],
          "workflow_sha256": current["workflow_sha256"], "inventory_sha256": current["inventory_sha256"],
          "architecture": architecture, "runner_label": ARCHITECTURES[architecture],
          "python_implementation": "CPython", "system": "Linux", "event": run["event"]}, "complete receipt")
    require(isinstance(receipt.get("python"), str)
            and bool(re.fullmatch(r"3\.12\.[0-9]+", receipt["python"])), "unapproved Python contract")
    require(isinstance(receipt.get("platform"), str) and receipt["platform"].startswith("Linux-"),
            "missing neutral platform")
    revision = receipt.get("workflow_commit", "")
    require(isinstance(revision, str) and bool(SHA40.fullmatch(revision)), "invalid workflow revision")
    workflow_commit = api.json("git/commits/" + revision)
    exact(workflow_commit, {"sha": revision}, "source workflow commit")
    exact(workflow_commit["tree"], {"sha": current["tree"]}, "source workflow tree")
    if run["event"] == "pull_request":
        require(transfer is not None and source == transfer["head"], "unrelated PR receipt")
        exact(receipt, {"base": transfer["base"], "pr_number": transfer["pr_number"],
              "ref": f"refs/pull/{transfer['pr_number']}/merge"}, "PR receipt lineage")
        if revision != source:
            require([p["sha"] for p in workflow_commit["parents"]] == [transfer["base"], source],
                    "synthetic workflow merge lineage mismatch")
    else:
        exact(receipt, {"ref": "refs/heads/main", "pr_number": None, "workflow_commit": source}, "main receipt")
        require(source == current["commit"] and run["head_branch"] == "main", "unrelated main receipt")
        require(isinstance(receipt.get("base"), str) and bool(SHA40.fullmatch(receipt["base"])),
                "invalid main comparison base")
        git(root, "merge-base", "--is-ancestor", receipt["base"], source)
    for category in ("probes", "reproduce"):
        validate_records(root, category, receipt.get(category))


def load_pair(root, api, run, current, transfer):
    exact(run, {"status": "completed", "conclusion": "success", "path": WORKFLOW,
          "workflow_id": WORKFLOW_ID}, "source workflow run")
    for key in ("repository", "head_repository"):
        exact(run[key], {"id": REPOSITORY_ID, "full_name": REPOSITORY}, "source run repository")
    require(run["event"] in {"pull_request", "push"}, "wrong source event")
    positive(run["id"]); positive(run["run_attempt"])
    require(isinstance(run.get("head_sha"), str) and bool(SHA40.fullmatch(run["head_sha"])), "invalid source head")
    jobs = api.pages(f"actions/runs/{run['id']}/attempts/{run['run_attempt']}/jobs", "jobs")
    aggregates = [j for j in jobs if j.get("name") == "check"]
    require(len(aggregates) == 1, "missing aggregate check")
    exact(aggregates[0], {"run_id": run["id"], "run_attempt": run["run_attempt"],
                        "head_sha": run["head_sha"], "status": "completed",
                        "conclusion": "success"}, "aggregate check")
    successful_steps(aggregates[0], ("Complete required architecture checks",))
    artifacts = api.pages(f"actions/runs/{run['id']}/artifacts", "artifacts")
    evidence = {}
    for architecture, label in ARCHITECTURES.items():
        selected = [j for j in jobs if j.get("name") == "architecture-" + architecture]
        require(len(selected) == 1, "missing architecture job: " + architecture)
        job = selected[0]
        exact(job, {"run_id": run["id"], "run_attempt": run["run_attempt"], "head_sha": run["head_sha"],
              "labels": [label], "runner_group_name": "GitHub Actions"}, "architecture job")
        positive(job["id"])
        successful_steps(job, (*STATIC_STEPS, REPLAY_STEP, UPLOAD_STEP))
        artifact_name = f"complete-verification-{architecture}-attempt-{run['run_attempt']}"
        selected = [a for a in artifacts if a.get("name") == artifact_name]
        require(len(selected) == 1, "missing complete architecture artifact: " + architecture)
        artifact = selected[0]
        positive(artifact["id"])
        exact(artifact["workflow_run"], {"id": run["id"], "head_sha": run["head_sha"],
              "head_branch": run["head_branch"], "repository_id": REPOSITORY_ID,
              "head_repository_id": REPOSITORY_ID}, "architecture artifact origin")
        archive = api.raw(f"actions/artifacts/{artifact['id']}/zip")
        raw = unpack(archive, artifact, RECEIPT_FILE)
        receipt = decode(raw)
        validate_receipt(root, receipt, current, run, architecture, transfer, api)
        evidence[architecture] = {"job_id": job["id"], "artifact_id": artifact["id"],
            "artifact_sha256": sha(archive), "receipt_sha256": sha(raw), "receipt": receipt}
    require(evidence["x86_64"]["receipt"]["probes"] == evidence["aarch64"]["receipt"]["probes"]
            and evidence["x86_64"]["receipt"]["reproduce"] == evidence["aarch64"]["receipt"]["reproduce"],
            "architecture dispositions differ")
    return {"schema": PROOF_SCHEMA, "source_run_id": run["id"], "source_run_attempt": run["run_attempt"],
            "source_event": run["event"], "source_commit": run["head_sha"],
            "activation_commit": current["commit"], "tree": current["tree"],
            "inventory_sha256": current["inventory_sha256"], "workflow_sha256": current["workflow_sha256"],
            "architectures": evidence}


def verified_pair(root, api, expected=None):
    current = snapshot(root)
    if expected is not None:
        exact(expected, {"schema": PROOF_SCHEMA, "activation_commit": current["commit"]}, "embedded verification")
        run_id = positive(expected["source_run_id"])
        attempt = positive(expected["source_run_attempt"])
        run = api.json(f"actions/runs/{run_id}/attempts/{attempt}")
        exact(run, {"id": run_id, "run_attempt": attempt}, "pinned source attempt")
        transfer = transfer_context(root, api, current)[1] if run["event"] == "pull_request" else None
        proof = load_pair(root, api, run, current, transfer)
        require(proof == expected, "embedded verification differs from original CI evidence")
        return proof
    errors = []
    for event in ("push", "pull_request"):
        # An actually executed exact-commit main pair has no PR-transfer
        # dependency. Check it before requesting any merge-lineage metadata.
        transfer = transfer_context(root, api, current)[1] if event == "pull_request" else None
        if event == "pull_request" and transfer is None:
            continue
        commit = transfer["head"] if transfer else current["commit"]
        runs = api.pages(f"actions/workflows/{WORKFLOW_ID}/runs?head_sha={commit}&event={event}&status=success",
                         "workflow_runs")
        for run in sorted(runs, key=lambda x: x["id"], reverse=True):
            try:
                require(run["head_sha"] == commit and run["event"] == event, "source run query mismatch")
                return load_pair(root, api, run, current, transfer)
            except (ValueError, KeyError, OSError, subprocess.SubprocessError, zipfile.BadZipFile) as error:
                errors.append(str(error))
    raise ValueError("no complete trusted architecture pair" + (": " + "; ".join(errors[:3]) if errors else ""))


def outside_checkout(root, path):
    destination = path.resolve()
    require(not destination.is_relative_to(root.resolve()), "receipt/manifest output must be outside checkout")
    require(not destination.exists(), "refusing to replace existing output")
    destination.parent.mkdir(parents=True, exist_ok=True)
    return destination


def output_complete(environment, complete):
    with Path(environment["GITHUB_OUTPUT"]).open("a", encoding="utf-8") as output:
        output.write("complete=" + str(complete).lower() + "\n")


def architecture(root, base, destination, environment, api):
    kind, event, ref, revision = github_context(root, environment)
    require(kind in {"push", "pull_request"}, "architecture event mismatch")
    complete = full_scope(root, base)
    if kind == "push":
        require(ref == "refs/heads/main" and revision == git(root, "rev-parse", "HEAD"), "main context mismatch")
        require(event["after"] == revision and event["before"] == base, "main push identity mismatch")
        git(root, "merge-base", "--is-ancestor", base, revision)
        try:
            proof = verified_pair(root, api)
        except (ValueError, KeyError, OSError, subprocess.SubprocessError, zipfile.BadZipFile) as error:
            print("VERIFICATION NOT REUSED: " + str(error), flush=True)
        else:
            print(f"VERIFICATION REUSE PASS run={proof['source_run_id']} attempt={proof['source_run_attempt']} "
                  f"proof_sha256={sha(encode(proof))} architectures=aarch64,x86_64 scientific_replay=False")
            output_complete(environment, False)
            return
    if not complete:
        replay(root, "check_verifier.py", base)
        replay(root, "check_reproduce.py", base)
        output_complete(environment, False)
        return
    context = prepare_complete_context(root, environment, base)
    before = snapshot(root)
    outputs = {"probes": replay(root, "check_verifier.py"),
               "reproduce": replay(root, "check_reproduce.py")}
    require(snapshot(root) == before, "complete replay changed its source context")
    architecture_name = {"AMD64": "x86_64", "arm64": "aarch64"}.get(platform.machine(), platform.machine())
    require(architecture_name in ARCHITECTURES and platform.system() == "Linux"
            and platform.python_implementation() == "CPython" and sys.version_info[:2] == (3, 12),
            "complete evidence requires the approved Linux/CPython 3.12 architecture")
    receipt = {"schema": RECEIPT_SCHEMA, "mode": "executed", "complete": True,
        "repository": REPOSITORY, "repository_id": REPOSITORY_ID, "workflow_id": WORKFLOW_ID,
        "workflow_path": WORKFLOW, **context, **before,
        "architecture": architecture_name, "runner_label": ARCHITECTURES[architecture_name],
        "system": platform.system(), "platform": platform.platform(),
        "python": platform.python_version(), "python_implementation": platform.python_implementation(),
        **{category: parse_replay(root, category, output) for category, output in outputs.items()}}
    outside_checkout(root, destination).write_bytes(encode(receipt))
    output_complete(environment, True)
    print("COMPLETE VERIFICATION RECEIPT PASS architecture=" + architecture_name)


def tag_identity(root, expected_tag):
    fields = read_status(root)
    require(bool(re.fullmatch(r"canon-v[1-9][0-9]*", expected_tag)) and fields["TAG"] == expected_tag,
            "tag differs from current release identity")
    require(git(root, "cat-file", "-t", "refs/tags/" + expected_tag) == "tag", "annotated tag required")
    commit = git(root, "rev-parse", expected_tag + "^{commit}")
    require(commit == git(root, "rev-parse", "HEAD"), "checkout must be the exact tag target")
    return fields, commit


def publication(root, expected_tag, destination, environment, api):
    kind, event, ref, revision = github_context(root, environment)
    fields, commit = tag_identity(root, expected_tag)
    require(kind in {"push", "release"} and ref == "refs/tags/" + expected_tag and revision == commit,
            "publication CI identity mismatch")
    if kind == "release":
        exact(event["release"], {"tag_name": expected_tag, "draft": False, "prerelease": False}, "release event")
    proof = verified_pair(root, api) if kind == "push" else None
    subprocess.run([sys.executable, "-B", "tools/check_activation.py", "--post-activation",
                    "--expected-tag", expected_tag], cwd=root, check=True)
    if proof is not None:
        data = manifest(root, fields["CONTENT_COMMIT"], commit, False)
        data["verification"] = proof
        data["publication"] = {"tag": expected_tag, "tag_object": git(root, "rev-parse", "refs/tags/" + expected_tag),
            "workflow_commit": revision, "run_id": int(environment["GITHUB_RUN_ID"]),
            "run_attempt": int(environment["GITHUB_RUN_ATTEMPT"])}
        outside_checkout(root, destination).write_bytes(encode(data))
        print(f"VERIFIED TAG MANIFEST PASS source_run={proof['source_run_id']} full_pair=True scientific_replay=False")


def original_tag_manifest(root, expected_tag, api, origin):
    _, commit = tag_identity(root, expected_tag)
    exact(origin, {"tag": expected_tag, "tag_object": git(root, "rev-parse", "refs/tags/" + expected_tag),
                   "workflow_commit": commit}, "original tag identity")
    run_id, attempt = positive(origin["run_id"]), positive(origin["run_attempt"])
    run = api.json(f"actions/runs/{run_id}/attempts/{attempt}")
    exact(run, {"id": run_id, "run_attempt": attempt, "head_sha": commit, "head_branch": expected_tag,
          "event": "push", "path": WORKFLOW, "workflow_id": WORKFLOW_ID,
          "status": "completed", "conclusion": "success"}, "original tag run")
    for key in ("repository", "head_repository"):
        exact(run[key], {"id": REPOSITORY_ID, "full_name": REPOSITORY}, "tag repository")
    jobs = api.pages(f"actions/runs/{run_id}/attempts/{attempt}/jobs", "jobs")
    selected = [j for j in jobs if j.get("name") == "publication"]
    require(len(selected) == 1, "missing original publication job")
    job = selected[0]
    positive(job["id"])
    exact(job, {"run_id": run_id, "run_attempt": attempt, "head_sha": commit,
          "labels": ["ubuntu-latest"], "runner_group_name": "GitHub Actions"}, "tag job")
    successful_steps(job, (*STATIC_STEPS, "Run activation readback on immutable publication events",
                            "Preserve tag readback manifest"))
    artifacts = api.pages(f"actions/runs/{run_id}/artifacts", "artifacts")
    wanted = f"{expected_tag}-activation-manifest-attempt-{attempt}"
    selected = [a for a in artifacts if a.get("name") == wanted]
    require(len(selected) == 1, "missing original tag artifact")
    artifact = selected[0]
    positive(artifact["id"])
    exact(artifact["workflow_run"], {"id": run_id, "head_sha": commit, "head_branch": expected_tag,
          "repository_id": REPOSITORY_ID, "head_repository_id": REPOSITORY_ID}, "tag artifact origin")
    raw = unpack(api.raw(f"actions/artifacts/{artifact['id']}/zip"), artifact, "activation-manifest.json")
    data = decode(raw)
    require(data["publication"] == origin, "manifest names a different tag attempt")
    verified_pair(root, api, data["verification"])
    return raw


def assets(root, expected_tag, api, release_id=None, draft=False):
    fields, commit = tag_identity(root, expected_tag)
    if release_id is None:
        if draft:
            matches = [r for r in api.pages("releases") if r.get("tag_name") == expected_tag and r.get("draft") is True]
            require(len(matches) == 1, "expected one draft release")
            release_id = matches[0]["id"]
        else:
            release_id = api.json("releases/tags/" + expected_tag)["id"]
    release = api.json("releases/" + str(positive(release_id)))
    exact(release, {"id": release_id, "tag_name": expected_tag, "target_commitish": commit,
          "draft": draft, "prerelease": False}, "release")
    if not draft:
        exact(release, {"immutable": True}, "published release")
        exact(api.json("releases/tags/" + expected_tag), {"id": release_id}, "published tag lookup")
    entries = release.get("assets")
    require(isinstance(entries, list) and len(entries) == 2
            and {a.get("name") for a in entries} == {"activation-manifest.json", "SHA256SUMS"},
            "release must have exactly two original assets")
    downloaded = {}
    for item in entries:
        data = api.raw("releases/assets/" + str(positive(item["id"])), binary=True)
        exact(item, {"state": "uploaded", "size": len(data), "digest": "sha256:" + sha(data)}, "release asset")
        downloaded[item["name"]] = data
    # The asset selects a frozen attempt, not the latest run. Its untrusted
    # origin is accepted only after API metadata and original artifact readback.
    origin = decode(downloaded["activation-manifest.json"])["publication"]
    original = original_tag_manifest(root, expected_tag, api, origin)
    require(downloaded["activation-manifest.json"] == original, "manifest asset differs from original tag artifact")
    require(downloaded["SHA256SUMS"] == (root / "canon/SHA256SUMS").read_bytes(), "checksum asset differs from tag")
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "activation-manifest.json"
        path.write_bytes(original)
        validate_manifest(root, path, fields["CONTENT_COMMIT"], commit)
    clean(root)
    print(f"RELEASE ASSETS PASS tag={expected_tag} draft={draft} original_tag_artifact=True full_pair=True scientific_replay=False")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    arch = commands.add_parser("architecture")
    arch.add_argument("--base", required=True)
    arch.add_argument("--receipt-out", type=Path, required=True)
    pub = commands.add_parser("publication")
    pub.add_argument("--expected-tag", required=True)
    pub.add_argument("--manifest-out", type=Path, required=True)
    asset = commands.add_parser("assets")
    asset.add_argument("--expected-tag", required=True)
    asset.add_argument("--release-id", type=int)
    asset.add_argument("--draft", action="store_true")
    args = parser.parse_args()
    api = GitHub()
    try:
        if args.command == "architecture":
            architecture(ROOT, args.base, args.receipt_out, os.environ, api)
        elif args.command == "publication":
            publication(ROOT, args.expected_tag, args.manifest_out, os.environ, api)
        else:
            assets(ROOT, args.expected_tag, api, args.release_id, args.draft)
    except (ValueError, KeyError, OSError, subprocess.SubprocessError, zipfile.BadZipFile) as error:
        raise SystemExit("VERIFICATION FAIL: " + str(error)) from error


if __name__ == "__main__":
    main()
