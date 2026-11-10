"""Operational provenance tests. No scientific verifier or network is executed."""
from __future__ import annotations

from contextlib import redirect_stdout
from copy import deepcopy
import io
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

try:
    from tools import release_verification as rv
except ModuleNotFoundError:
    import release_verification as rv


class FakeAPI:
    def __init__(self):
        self.objects = {}
        self.lists = {}
        self.bytes = {}
        self.calls = []

    def json(self, path):
        self.calls.append(path)
        return deepcopy(self.objects[path])

    def pages(self, path, key=None):
        self.calls.append(path)
        return deepcopy(self.lists[path])

    def raw(self, path, binary=False):
        self.calls.append(path)
        return self.bytes[path]


def archive(raw, filename=rv.RECEIPT_FILE):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as bundle:
        bundle.writestr(filename, raw)
    return stream.getvalue()


class VerificationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.root = self.directory / "repo"
        self.root.mkdir()
        rv.git(self.root, "init", "-b", "main")
        rv.git(self.root, "config", "user.name", "Fixture")
        rv.git(self.root, "config", "user.email", "fixture@example.invalid")
        rv.git(self.root, "config", "core.autocrlf", "false")
        self.write(rv.WORKFLOW, "name: policy\n")
        self.write("STATUS.md", "STATE: ACTIVE\nTAG: canon-v112\nCONTENT_COMMIT: " + "a" * 40 + "\n")
        self.write("canon/SHA256SUMS", "fixture checksum\n")
        for name in ("DONE", "ABANDONED"):
            for filename in ("PREREG.md", "verify.py"):
                self.write(f"probes/{name}/{filename}", "fixture\n")
            self.write(f"probes/{name}/RESULT.md", "Status: " + ("PASS" if name == "DONE" else "ABANDONED") + "\n")
        self.write("probes/DONE/EXPECTED.txt", "probe output\n")
        self.write("probes/DONE/RUN.md", "fixture run\n")
        self.write("reproduce/SMALL/verify.py", "fixture\n")
        self.write("reproduce/SMALL/EXPECTED.txt", "reproduction output\n")
        self.base = self.commit("base")
        self.write(rv.WORKFLOW, "name: policy\n# frozen controller fixture\n")
        self.head = self.commit("candidate")
        self.tree = rv.git(self.root, "rev-parse", "HEAD^{tree}")
        self.synthetic = rv.git(self.root, "commit-tree", self.tree, "-p", self.base, "-p", self.head, "-m", "synthetic PR")
        self.merge = rv.git(self.root, "commit-tree", self.tree, "-p", self.base, "-p", self.head, "-m", "reviewed merge")
        rv.git(self.root, "checkout", "--detach", self.merge)
        rv.git(self.root, "tag", "-a", "canon-v112", "-m", "fixture tag")
        self.current = rv.snapshot(self.root)
        self.repo = {"id": rv.REPOSITORY_ID, "full_name": rv.REPOSITORY}
        self.transfer = {"base": self.base, "head": self.head, "pr_number": 12}
        self.api = FakeAPI()
        self.run = self.run_record(100, self.head, "candidate", "pull_request")
        self.api.objects["actions/runs/100/attempts/1"] = self.run
        pr = {"number": 12, "merged": True, "state": "closed", "merge_commit_sha": self.merge,
              "head": {"sha": self.head, "repo": self.repo}, "base": {"ref": "main", "repo": self.repo}}
        self.api.lists[f"commits/{self.merge}/pulls"] = [pr]
        self.api.objects["pulls/12"] = pr
        self.api.objects["git/commits/" + self.synthetic] = {
            "sha": self.synthetic, "tree": {"sha": self.tree}, "parents": [{"sha": self.base}, {"sha": self.head}]}
        self.api.lists[self.query(self.merge, "push")] = []
        self.api.lists[self.query(self.head, "pull_request")] = [self.run]
        jobs = [self.job(201 + i, "architecture-" + arch, label,
                        (*rv.STATIC_STEPS, rv.REPLAY_STEP, rv.UPLOAD_STEP))
                for i, (arch, label) in enumerate(rv.ARCHITECTURES.items())]
        jobs.append(self.job(203, "check", "ubuntu-latest", ("Complete required architecture checks",)))
        self.api.lists["actions/runs/100/attempts/1/jobs"] = jobs
        self.api.lists["actions/runs/100/artifacts"] = []
        self.receipts = {}
        for i, (arch, label) in enumerate(rv.ARCHITECTURES.items()):
            receipt = {"schema": rv.RECEIPT_SCHEMA, "mode": "executed", "complete": True,
                "repository": rv.REPOSITORY, "repository_id": rv.REPOSITORY_ID,
                "workflow_id": rv.WORKFLOW_ID, "workflow_path": rv.WORKFLOW,
                **self.current, "commit": self.head, "workflow_commit": self.synthetic,
                "event": "pull_request", "ref": "refs/pull/12/merge", "pr_number": 12, "base": self.base,
                "run_id": 100, "run_attempt": 1, "architecture": arch, "runner_label": label,
                "system": "Linux", "platform": "Linux-fixture", "python": "3.12.9",
                "python_implementation": "CPython",
                **{category: rv.parse_replay(self.root, category, self.output(category))
                   for category in ("probes", "reproduce")}}
            self.receipts[arch] = receipt
            self.add_artifact(100, 1000 + i, f"complete-verification-{arch}-attempt-1",
                              rv.encode(receipt), rv.RECEIPT_FILE, self.head, "candidate")

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode())

    def commit(self, message):
        rv.git(self.root, "add", ".")  # Only the small isolated fixture repository.
        rv.git(self.root, "commit", "-m", message)
        return rv.git(self.root, "rev-parse", "HEAD")

    def query(self, commit, event):
        return f"actions/workflows/{rv.WORKFLOW_ID}/runs?head_sha={commit}&event={event}&status=success"

    def run_record(self, run_id, commit, branch, event, attempt=1):
        return {"id": run_id, "run_attempt": attempt, "head_sha": commit, "head_branch": branch,
                "event": event, "path": rv.WORKFLOW, "workflow_id": rv.WORKFLOW_ID,
                "repository": self.repo, "head_repository": self.repo,
                "status": "completed", "conclusion": "success"}

    def job(self, job_id, name, label, steps, run_id=100, attempt=1, commit=None):
        return {"id": job_id, "name": name, "run_id": run_id, "run_attempt": attempt,
                "head_sha": commit or self.head, "status": "completed", "conclusion": "success",
                "labels": [label], "runner_group_name": "GitHub Actions",
                "steps": [{"name": s, "status": "completed", "conclusion": "success"} for s in steps]}

    def add_artifact(self, run_id, artifact_id, name, raw, filename, commit, branch):
        blob = archive(raw, filename)
        artifact = {"id": artifact_id, "name": name, "size_in_bytes": len(blob),
            "digest": "sha256:" + rv.sha(blob), "expired": False,
            "workflow_run": {"id": run_id, "head_sha": commit, "head_branch": branch,
                             "repository_id": rv.REPOSITORY_ID, "head_repository_id": rv.REPOSITORY_ID}}
        self.api.lists.setdefault(f"actions/runs/{run_id}/artifacts", []).append(artifact)
        self.api.bytes[f"actions/artifacts/{artifact_id}/zip"] = blob

    def replace_receipt(self, api, receipt, index=0):
        blob = archive(rv.encode(receipt))
        artifact = api.lists["actions/runs/100/artifacts"][index]
        artifact.update(size_in_bytes=len(blob), digest="sha256:" + rv.sha(blob))
        api.bytes[f"actions/artifacts/{artifact['id']}/zip"] = blob

    def output(self, category):
        prefix = "VERIFY" if category == "probes" else "REPRODUCE"
        name = "DONE" if category == "probes" else "SMALL"
        path = self.root / category / name
        line = f"{prefix} PASS {name} {rv.sha((path / 'verify.py').read_bytes())} {rv.sha((path / 'EXPECTED.txt').read_bytes())}\n"
        if category == "probes":
            line += "VERIFY ABANDONED ABANDONED no completed gate, nothing to reproduce\n"
        return line.encode()

    def environment(self, event="push", tag=False):
        ref = "refs/tags/canon-v112" if tag else "refs/heads/main"
        revision = self.merge
        payload = {"after": self.merge, "before": self.base}
        if event == "pull_request":
            ref, revision = "refs/pull/12/merge", self.synthetic
            payload = {"number": 12, "pull_request": {"head": {"sha": self.head, "repo": self.repo},
                       "base": {"sha": self.base, "ref": "main", "repo": self.repo}}}
        elif event == "release":
            payload = {"release": {"tag_name": "canon-v112", "draft": False, "prerelease": False}}
        path = self.directory / "event.json"
        path.write_bytes(rv.encode(payload))
        return {"GITHUB_ACTIONS": "true", "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_REPOSITORY": rv.REPOSITORY, "GITHUB_REPOSITORY_ID": str(rv.REPOSITORY_ID),
            "GITHUB_EVENT_NAME": event, "GITHUB_EVENT_PATH": str(path), "GITHUB_REF": ref,
            "GITHUB_SHA": revision, "GITHUB_WORKFLOW_SHA": revision,
            "GITHUB_WORKFLOW_REF": rv.REPOSITORY + "/" + rv.WORKFLOW + "@" + ref,
            "GITHUB_RUN_ID": "200", "GITHUB_RUN_ATTEMPT": "2", "GITHUB_OUTPUT": str(self.directory / "output")}

    def pair(self, api=None):
        return rv.verified_pair(self.root, api or self.api)

    def test_valid_pair_binds_both_original_jobs_and_exact_inventory(self):
        proof = self.pair()
        self.assertEqual(proof["source_commit"], self.head)
        self.assertEqual(proof["activation_commit"], self.merge)
        self.assertEqual(set(proof["architectures"]), {"x86_64", "aarch64"})
        self.assertEqual(rv.verified_pair(self.root, self.api, proof), proof)
        self.assertIn("actions/runs/100/attempts/1", self.api.calls)
        self.assertNotIn("actions/runs/100", self.api.calls)

    def test_executed_main_pair_is_accepted_only_at_its_exact_commit(self):
        run = deepcopy(self.run)
        run.update(head_sha=self.merge, head_branch="main", event="push")
        self.api.lists[self.query(self.merge, "push")] = [run]
        self.api.objects["actions/runs/100/attempts/1"] = run
        self.api.lists[f"commits/{self.merge}/pulls"] = []
        self.api.objects["git/commits/" + self.merge] = {
            "sha": self.merge, "tree": {"sha": self.tree}, "parents": [{"sha": self.base}, {"sha": self.head}]}
        for job in self.api.lists["actions/runs/100/attempts/1/jobs"]:
            job["head_sha"] = self.merge
        for i, arch in enumerate(rv.ARCHITECTURES):
            receipt = deepcopy(self.receipts[arch])
            receipt.update(commit=self.merge, workflow_commit=self.merge, event="push", ref="refs/heads/main", pr_number=None)
            self.replace_receipt(self.api, receipt, i)
            self.api.lists["actions/runs/100/artifacts"][i]["workflow_run"].update(head_sha=self.merge, head_branch="main")
        proof = self.pair()
        self.assertEqual(proof["source_commit"], self.merge)
        self.assertEqual(proof["source_event"], "push")
        self.assertEqual(rv.verified_pair(self.root, self.api, proof), proof)
        self.assertNotIn(f"commits/{self.merge}/pulls", self.api.calls)
        current = dict(self.current, commit=self.head)
        with self.assertRaisesRegex(ValueError, "unrelated main"):
            rv.load_pair(self.root, self.api, run, current, self.transfer)

    def test_untrusted_run_cannot_supply_pair(self):
        for field, value in (("event", "workflow_dispatch"), ("path", "other.yml"), ("workflow_id", 1),
                             ("status", "in_progress"), ("conclusion", "failure"), ("head_sha", "f" * 40),
                             ("repository", {"id": 2, "full_name": rv.REPOSITORY}),
                             ("head_repository", {"id": 2, "full_name": "fork/repo"})):
            run = deepcopy(self.run); run[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                rv.load_pair(self.root, self.api, run, self.current, self.transfer)

    def test_partial_failed_or_wrong_architecture_jobs_are_rejected(self):
        route = "actions/runs/100/attempts/1/jobs"
        cases = [(0, "conclusion", "failure"), (1, "conclusion", "skipped"),
                 (0, "labels", ["self-hosted"]), (0, "runner_group_name", "Other"),
                 (1, "run_attempt", 2), (1, "head_sha", "f" * 40), (2, "conclusion", "skipped"),
                 (0, "steps", [{"name": rv.REPLAY_STEP, "status": "completed", "conclusion": "success"}])]
        for index, field, value in cases:
            api = deepcopy(self.api); api.lists[route][index][field] = value
            with self.subTest(index=index, field=field), self.assertRaises(ValueError): self.pair(api)
        api = deepcopy(self.api); api.lists[route].pop(1)
        with self.assertRaises(ValueError): self.pair(api)

    def test_missing_expired_mixed_attempt_or_replaced_artifact_is_rejected(self):
        route = "actions/runs/100/artifacts"
        for field, value in (("expired", True), ("digest", "sha256:" + "0" * 64),
                             ("size_in_bytes", 1), ("name", "complete-verification-x86_64-attempt-2"),
                             ("workflow_run", {"id": 999})):
            api = deepcopy(self.api); api.lists[route][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): self.pair(api)
        api = deepcopy(self.api); api.lists[route].pop()
        with self.assertRaises(ValueError): self.pair(api)

    def test_forged_receipt_cannot_change_source_runtime_or_scope(self):
        for field, value in (("mode", "reused"), ("complete", False), ("complete", 1),
                             ("tree", "f" * 40), ("inventory_sha256", "0" * 64),
                             ("workflow_sha256", "0" * 64), ("workflow_commit", "bad"),
                             ("workflow_commit", None), ("python", None),
                             ("commit", self.merge), ("base", "f" * 40), ("pr_number", 13),
                             ("run_attempt", 2), ("architecture", "aarch64"),
                             ("python", "3.13.1"), ("system", "Windows"),
                             ("python_implementation", "PyPy"), ("probes", {}), ("reproduce", {})):
            api = deepcopy(self.api); receipt = deepcopy(self.receipts["x86_64"]); receipt[field] = value
            self.replace_receipt(api, receipt)
            with self.subTest(field=field, value=value), self.assertRaises(ValueError): self.pair(api)

    def test_completed_probe_cannot_be_disguised_as_abandoned(self):
        receipt = deepcopy(self.receipts["x86_64"])
        receipt["probes"]["DONE"] = {"result": "ABANDONED"}
        self.replace_receipt(self.api, receipt)
        with self.assertRaises(ValueError): self.pair()

    def test_workflow_tree_and_synthetic_parents_must_match(self):
        route = "git/commits/" + self.synthetic
        for field, value in (("tree", {"sha": "f" * 40}), ("parents", [{"sha": self.head}])):
            api = deepcopy(self.api); api.objects[route][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): self.pair(api)

    def test_wrong_pr_head_or_repository_cannot_supply_merge_evidence(self):
        for side, field, value in (("head", "sha", "f" * 40), ("base", "ref", "other"),
                                  ("head", "repo", {"id": 3, "full_name": "fork/repo"})):
            api = deepcopy(self.api); api.objects["pulls/12"][side][field] = value
            with self.subTest(side=side, field=field), self.assertRaises(ValueError): self.pair(api)

    def test_dirty_or_changed_merge_tree_cannot_reuse_pair(self):
        self.write("new.txt", "new source\n")
        with self.assertRaisesRegex(ValueError, "clean"): self.pair()
        changed = self.commit("changed merge tree")
        self.api.lists[self.query(changed, "push")] = []
        with self.assertRaisesRegex(ValueError, "no complete"): self.pair()

    def test_replay_requires_complete_unique_exact_dispositions(self):
        valid = self.output("probes")
        for output in (b"", valid + valid, valid.replace(b"PASS DONE", b"PASS ../escape"),
                       valid.replace(b"VERIFY PASS DONE", b"VERIFY PASS UNKNOWN"),
                       valid.splitlines(keepends=True)[0]):
            with self.subTest(output=output[:50]), self.assertRaises(ValueError):
                rv.parse_replay(self.root, "probes", output)

    def test_complete_selection_preserves_one_probe_rule(self):
        self.assertTrue(rv.full_scope(self.root, self.base))
        for name in ("DONE", "ABANDONED"):
            self.write(f"probes/{name}/PREREG.md", "changed\n")
        self.commit("two probe changes")
        with self.assertRaisesRegex(ValueError, "one probe"): rv.full_scope(self.root, self.base)

    def test_pr_complete_execution_checks_out_immutable_head(self):
        rv.git(self.root, "checkout", "--detach", self.synthetic)
        context = rv.prepare_complete_context(self.root, self.environment("pull_request"), self.base)
        self.assertEqual(rv.git(self.root, "rev-parse", "HEAD"), self.head)
        self.assertEqual(context["workflow_commit"], self.synthetic)

    def test_stale_candidate_or_foreign_workflow_context_fails(self):
        environment = self.environment("pull_request")
        self.write("other.txt", "different tested merge\n"); self.commit("stale")
        with self.assertRaisesRegex(ValueError, "tested merge tree"):
            rv.prepare_complete_context(self.root, environment, self.base)
        environment["GITHUB_WORKFLOW_REF"] = "foreign/workflow"
        with self.assertRaisesRegex(ValueError, "workflow ref"): rv.github_context(self.root, environment)

    def test_main_reuse_does_not_replay_or_mint_a_new_execution_receipt(self):
        environment = self.environment()
        destination = self.directory / "receipt.json"
        with patch.object(rv, "replay") as replay, redirect_stdout(io.StringIO()):
            rv.architecture(self.root, self.base, destination, environment, self.api)
        replay.assert_not_called()
        self.assertFalse(destination.exists())
        self.assertEqual(Path(environment["GITHUB_OUTPUT"]).read_text(), "complete=false\n")

    def test_missing_main_proof_falls_back_to_both_full_runners(self):
        environment = self.environment()
        destination = self.directory / "receipt.json"
        def replay(root, script, base=None):
            self.assertIsNone(base)
            return self.output("probes" if script == "check_verifier.py" else "reproduce")
        with patch.object(rv, "verified_pair", side_effect=ValueError("unavailable")), \
             patch.object(rv, "replay", side_effect=replay) as execute, \
             patch.object(rv.platform, "system", return_value="Linux"), \
             patch.object(rv.platform, "machine", return_value="x86_64"), \
             patch.object(rv.sys, "version_info", (3, 12, 9)), redirect_stdout(io.StringIO()):
            rv.architecture(self.root, self.base, destination, environment, self.api)
        self.assertEqual(execute.call_count, 2)
        receipt = rv.decode(destination.read_bytes())
        self.assertEqual(receipt["event"], "push")
        self.assertEqual(receipt["commit"], self.merge)
        self.assertEqual(receipt["mode"], "executed")

    def test_api_timeout_falls_back_and_changed_event_identity_cannot_skip(self):
        environment = self.environment()
        with patch.object(rv, "verified_pair", side_effect=subprocess.TimeoutExpired("gh", 60)), \
             patch.object(rv, "full_scope", return_value=False), patch.object(rv, "replay") as execute, \
             redirect_stdout(io.StringIO()):
            rv.architecture(self.root, self.base, self.directory / "receipt.json", environment, self.api)
        self.assertEqual(execute.call_count, 2)
        Path(environment["GITHUB_EVENT_PATH"]).write_bytes(rv.encode({"before": self.base, "after": self.head}))
        with self.assertRaisesRegex(ValueError, "main push identity"):
            rv.architecture(self.root, self.base, self.directory / "receipt.json", environment, self.api)

    def test_null_receipt_fields_trigger_full_fallback_without_a_skip(self):
        environment = self.environment()
        for field in ("python", "workflow_commit"):
            api = deepcopy(self.api)
            receipt = deepcopy(self.receipts["x86_64"]); receipt[field] = None
            self.replace_receipt(api, receipt)
            with self.subTest(field=field), redirect_stdout(io.StringIO()), \
                 patch.object(rv, "replay", side_effect=ValueError("full replay attempted")) as execute, \
                 self.assertRaisesRegex(ValueError, "full replay attempted"):
                rv.architecture(self.root, self.base, self.directory / "receipt.json", environment, api)
            self.assertEqual(execute.call_args.args, (self.root, "check_verifier.py"))
            self.assertFalse((self.directory / "receipt.json").exists())

    def test_partial_and_failed_execution_cannot_create_complete_receipt(self):
        environment = self.environment("pull_request")
        destination = self.directory / "receipt.json"
        with patch.object(rv, "full_scope", return_value=False), patch.object(rv, "replay") as execute:
            rv.architecture(self.root, self.base, destination, environment, self.api)
        self.assertEqual([c.args[2] for c in execute.call_args_list], [self.base, self.base])
        self.assertFalse(destination.exists())
        with patch.object(rv, "replay", side_effect=ValueError("failed verifier")), self.assertRaises(ValueError):
            rv.architecture(self.root, self.base, destination, environment, self.api)
        self.assertFalse(destination.exists())

    def test_scientific_children_receive_no_controller_credentials(self):
        result = SimpleNamespace(returncode=0, stdout=b"runner output\n", stderr=b"")
        with patch.dict(os.environ, {"GH_TOKEN": "fixture", "ACTIONS_RUNTIME_TOKEN": "fixture"}), \
             patch.object(rv.subprocess, "run", return_value=result) as run, patch.object(rv.sys, "stdout"):
            self.assertEqual(rv.replay(self.root, "check_verifier.py", self.base), result.stdout)
        environment = run.call_args.kwargs["env"]
        self.assertNotIn("GH_TOKEN", environment)
        self.assertNotIn("ACTIONS_RUNTIME_TOKEN", environment)
        self.assertEqual(run.call_args.args[0][-2:], ["--base", self.base])

    def test_tag_only_runs_static_activation_and_records_frozen_origins(self):
        destination = self.directory / "activation-manifest.json"
        system_run = subprocess.run
        commands = []
        def execute(command, **kwargs):
            if "tools/check_activation.py" in command:
                self.assertNotIn("--full", command)
                self.assertIn("--post-activation", command)
                commands.append(command)
                return SimpleNamespace(returncode=0)
            return system_run(command, **kwargs)
        with patch.object(rv.subprocess, "run", side_effect=execute), \
             patch.object(rv, "verified_pair", return_value=self.pair()), \
             patch.object(rv, "manifest", return_value={}), redirect_stdout(io.StringIO()):
            rv.publication(self.root, "canon-v112", destination, self.environment(tag=True), self.api)
        data = rv.decode(destination.read_bytes())
        self.assertEqual(data["publication"]["run_attempt"], 2)
        self.assertEqual(data["verification"]["source_run_id"], 100)
        self.assertEqual(len(commands), 1)

    def test_release_event_creates_no_replacement_manifest(self):
        destination = self.directory / "activation-manifest.json"
        system_run = subprocess.run
        def execute(command, **kwargs):
            if "tools/check_activation.py" in command:
                self.assertNotIn("--full", command)
                return SimpleNamespace(returncode=0)
            return system_run(command, **kwargs)
        with patch.object(rv.subprocess, "run", side_effect=execute), patch.object(rv, "manifest") as generate:
            rv.publication(self.root, "canon-v112", destination, self.environment("release", tag=True), self.api)
        generate.assert_not_called()
        self.assertFalse(destination.exists())

    def install_release(self, draft=False):
        origin = {"tag": "canon-v112", "tag_object": rv.git(self.root, "rev-parse", "refs/tags/canon-v112"),
                  "workflow_commit": self.merge, "run_id": 200, "run_attempt": 2}
        data = rv.manifest(self.root, "a" * 40, self.merge, False)
        data.update(verification=self.pair(), publication=origin)
        raw = rv.encode(data)
        self.api.objects["actions/runs/200/attempts/2"] = self.run_record(200, self.merge, "canon-v112", "push", 2)
        job = self.job(400, "publication", "ubuntu-latest", (*rv.STATIC_STEPS,
            "Run activation readback on immutable publication events", "Preserve tag readback manifest"),
            run_id=200, attempt=2, commit=self.merge)
        self.api.lists["actions/runs/200/attempts/2/jobs"] = [job]
        self.add_artifact(200, 2000, "canon-v112-activation-manifest-attempt-2", raw,
                          "activation-manifest.json", self.merge, "canon-v112")
        entries = []
        for asset_id, name, content in ((51, "activation-manifest.json", raw),
                                       (52, "SHA256SUMS", (self.root / "canon/SHA256SUMS").read_bytes())):
            entries.append({"id": asset_id, "name": name, "state": "uploaded", "size": len(content),
                            "digest": "sha256:" + rv.sha(content)})
            self.api.bytes[f"releases/assets/{asset_id}"] = content
        release = {"id": 500, "tag_name": "canon-v112", "target_commitish": self.merge,
                   "draft": draft, "prerelease": False, "immutable": not draft, "assets": entries}
        self.api.objects["releases/500"] = release
        self.api.objects["releases/tags/canon-v112"] = release
        self.api.lists["releases"] = [release]

    def test_published_and_draft_assets_match_original_pinned_tag_attempt(self):
        for draft in (False, True):
            if draft:
                self.api.lists["actions/runs/200/artifacts"] = []
            self.install_release(draft)
            with redirect_stdout(io.StringIO()): rv.assets(self.root, "canon-v112", self.api, draft=draft)
            self.assertIn("actions/runs/200/attempts/2", self.api.calls)

    def test_replaced_manifest_with_valid_new_asset_hash_is_rejected(self):
        self.install_release()
        raw = self.api.bytes["releases/assets/51"] + b"\n"
        self.api.bytes["releases/assets/51"] = raw
        self.api.objects["releases/500"]["assets"][0].update(size=len(raw), digest="sha256:" + rv.sha(raw))
        with self.assertRaisesRegex(ValueError, "differs from original"):
            rv.assets(self.root, "canon-v112", self.api)

    def test_failed_tag_job_expired_original_or_wrong_release_fails(self):
        self.install_release()
        for route, field, value in (("actions/runs/200/attempts/2", "conclusion", "failure"),
                                     ("releases/500", "target_commitish", self.head),
                                     ("releases/500", "immutable", False), ("releases/500", "draft", True)):
            api = deepcopy(self.api); api.objects[route][field] = value
            with self.subTest(route=route, field=field), self.assertRaises(ValueError):
                rv.assets(self.root, "canon-v112", api)
        self.api.lists["actions/runs/200/artifacts"][0]["expired"] = True
        with self.assertRaises(ValueError): rv.assets(self.root, "canon-v112", self.api)

    def test_missing_proof_cannot_generate_tag_manifest(self):
        destination = self.directory / "activation-manifest.json"
        with patch.object(rv, "verified_pair", side_effect=ValueError("missing")), self.assertRaises(ValueError):
            rv.publication(self.root, "canon-v112", destination, self.environment(tag=True), self.api)
        self.assertFalse(destination.exists())

    def test_duplicate_json_keys_archive_paths_and_existing_outputs_fail(self):
        with self.assertRaises(ValueError): rv.decode(b'{"complete":true,"complete":false}')
        blob = archive(b"{}", "../architecture-verification.json")
        metadata = {"size_in_bytes": len(blob), "digest": "sha256:" + rv.sha(blob), "expired": False}
        with self.assertRaises(ValueError): rv.unpack(blob, metadata, rv.RECEIPT_FILE)
        with self.assertRaises(ValueError): rv.outside_checkout(self.root, self.root / "receipt.json")
        path = self.directory / "existing"; path.write_text("preserve")
        with self.assertRaises(ValueError): rv.outside_checkout(self.root, path)

    def test_api_transport_has_fixed_host_and_read_only_method(self):
        with patch.object(rv.subprocess, "run", return_value=SimpleNamespace(stdout=b"fixture")) as run:
            self.assertEqual(rv.GitHub().raw("actions/runs/100"), b"fixture")
        command = run.call_args.args[0]
        self.assertEqual(command[command.index("--hostname") + 1], "github.com")
        self.assertEqual(command[command.index("--method") + 1], "GET")


if __name__ == "__main__":
    unittest.main()
