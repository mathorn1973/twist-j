"""Exercise historical replay with tiny synthetic probes, never scientific ones."""

from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools import check_verifier
from tools import probe_replay_context as context


NAME = "P-REPLAY-FIXTURE"
PREDEF = "notes/canon/C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md"
INPUTS = {"canon/CANON.md": b"v82 canon", "STATUS.md": b"v82 status", PREDEF: b"predef"}
EXPECTED = b"v82 canon|v82 status|predef\n"
SCRIPT = (
    "from pathlib import Path\nimport sys\n"
    "root = Path(__file__).resolve().parents[2]\n"
    f"paths = {list(INPUTS)!r}\n"
    "sys.stdout.buffer.write(b'|'.join((root/p).read_bytes() for p in paths)+b'\\n')\n"
).encode("ascii")


def blob_spec(data: bytes) -> dict:
    return {
        "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
    }


class ReplayContextTests(unittest.TestCase):
    def setUp(self) -> None:
        for allowance, paths in ((context.ADMITTED_CONTEXT_PATHS, frozenset(INPUTS)),
                                 (context.ADMITTED_BUNDLE_PATHS, frozenset())):
            patcher = patch.dict(allowance, {NAME: paths})
            patcher.start()
            self.addCleanup(patcher.stop)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        self.probe = self.root / "probes" / NAME
        self.probe.mkdir(parents=True)
        self.write(f"probes/{NAME}/verify.py", SCRIPT)
        self.script = SCRIPT
        self.write(f"probes/{NAME}/PREREG.md", b"frozen fixture context\n")
        for path, data in INPUTS.items():
            self.write(path, data)
        self.pin = self.commit("pin")
        self.entry = {
            "pin_commit": self.pin,
            "verifier": blob_spec(SCRIPT),
            "prereg": blob_spec(b"frozen fixture context\n"),
            "context_files": {path: blob_spec(data) for path, data in INPUTS.items()},
        }
        self.manifest = {"schema": 1, "probes": {NAME: self.entry}}
        self.save_manifest()
        self.write(f"probes/{NAME}/EXPECTED.txt", EXPECTED)
        run = (
            f"pin_commit: {self.pin}\n"
            f"verifier_sha256: {blob_spec(SCRIPT)['sha256']}\n"
            f"command: python3 probes/{NAME}/verify.py\n"
            "platform: synthetic fixture\narchitecture: x86_64\npython: Python 3.12\n"
            f"exit_code: 0\nstdout_sha256: {hashlib.sha256(EXPECTED).hexdigest()}\n"
            f"stdout_bytes: {len(EXPECTED)}\nstdout_lines: 1\n"
            f"stderr_sha256: {hashlib.sha256(b'').hexdigest()}\nstderr_bytes: 0\n"
        )
        self.write(f"probes/{NAME}/RUN.md", run.encode())
        self.write(f"probes/{NAME}/RESULT.md", b"Status: PASS\n")

    def git(self, *args: str) -> bytes:
        return subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.PIPE)

    def commit(self, message: str) -> str:
        self.git("add", ".")
        self.git("-c", "user.name=Replay Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgSign=false", "commit", "-qm", message)
        return self.git("rev-parse", "HEAD").decode().strip()

    def write(self, relative: str, data: bytes) -> None:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def save_manifest(self) -> None:
        self.write(context.MANIFEST, (json.dumps(self.manifest) + "\n").encode())

    def replay(self) -> str:
        output = StringIO()
        with patch.object(check_verifier, "ROOT", self.root), redirect_stdout(output):
            check_verifier.reproduce(self.probe)
        return output.getvalue()

    def context_failure(self, contains: str) -> None:
        with self.assertRaisesRegex(context.ReplayContextError, contains):
            with context.execution_root(self.root, NAME, self.pin, self.script):
                self.fail("invalid context reached execution")

    def make_bundle_fixture(self) -> dict[str, bytes]:
        """A tiny nested wrapper with source hashes, not a scientific program."""
        prefix = f"probes/{NAME}/"
        self.script = (
            "from pathlib import Path\nimport hashlib,json,subprocess,sys\n"
            "here=Path(__file__).resolve().parent\n"
            "for name,digest in json.loads((here/'INPUTS.json').read_bytes()).items():\n"
            " assert hashlib.sha256((here/name).read_bytes()).hexdigest()==digest\n"
            "assert (here/'PREREG.md').is_file()\n"
            "result=subprocess.run([sys.executable,str(here/'companion.py')],capture_output=True)\n"
            "assert result.returncode==0 and not result.stderr\n"
            "sys.stdout.buffer.write(result.stdout)\n"
        ).encode()
        companion = (
            "from pathlib import Path\nimport hashlib,json,sys\n"
            "from fixture_helper import payload\n"
            "here=Path(__file__).resolve().parent\nroot=here.parents[1]\n"
            "for path,digest in json.loads((here/'SOURCE.json').read_bytes()).items():\n"
            " assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest\n"
            f"paths={list(INPUTS)!r}\n"
            "sys.stdout.buffer.write(payload(root,paths))\n"
        ).encode()
        helper = b"def payload(root,paths):\n return b'|'.join((root/p).read_bytes() for p in paths)+b'\\n'\n"
        source = json.dumps({p: hashlib.sha256(b).hexdigest() for p, b in INPUTS.items()}).encode()
        local = {"verify.py": self.script, "PREREG.md": b"frozen fixture context\n",
                 "companion.py": companion, "fixture_helper.py": helper, "SOURCE.json": source}
        local["INPUTS.json"] = json.dumps(
            {p: hashlib.sha256(b).hexdigest() for p, b in local.items()}
        ).encode()
        for name, data in local.items():
            self.write(prefix + name, data)
        self.write(prefix + "ambient.py", b"raise RuntimeError('not admitted')\n")
        old_pin = self.pin
        self.pin = self.entry["pin_commit"] = self.commit("nested wrapper pin")
        self.entry["verifier"] = blob_spec(self.script)
        self.entry["bundle_files"] = {
            prefix + name: blob_spec(local[name])
            for name in ("companion.py", "fixture_helper.py", "SOURCE.json", "INPUTS.json")
        }
        context.ADMITTED_BUNDLE_PATHS[NAME] = frozenset(self.entry["bundle_files"])
        self.save_manifest()
        run_path = self.probe / "RUN.md"
        run = run_path.read_bytes().replace(old_pin.encode(), self.pin.encode())
        run = run.replace(blob_spec(SCRIPT)["sha256"].encode(),
                          blob_spec(self.script)["sha256"].encode())
        run_path.write_bytes(run)
        return {prefix + name: data for name, data in local.items()}

    def test_nested_wrapper_replays_exact_sources_and_unchanged_bundle(self) -> None:
        local = self.make_bundle_fixture()
        for path in INPUTS:
            self.write(path, b"later current authority")
        self.commit("later authority")
        output = self.replay()
        self.assertIn(f"VERIFY PASS {NAME}", output)
        with redirect_stdout(StringIO()):
            with context.execution_root(self.root, NAME, self.pin, self.script) as isolated:
                files = {p.relative_to(isolated).as_posix(): p.read_bytes()
                         for p in isolated.rglob("*") if p.is_file()}
                self.assertEqual(files, {**INPUTS, **local})
        self.assertFalse(isolated.exists())
        for path in INPUTS:
            self.assertEqual((self.root / path).read_bytes(), b"later current authority")

    def test_every_current_bundle_file_must_equal_its_pin(self) -> None:
        local = self.make_bundle_fixture()
        for path in self.entry["bundle_files"]:
            with self.subTest(path=path):
                self.write(path, local[path] + b"changed")
                self.context_failure("current bundle differs")
                self.write(path, local[path])

    def test_missing_current_bundle_file_is_rejected(self) -> None:
        self.make_bundle_fixture()
        (self.probe / "companion.py").unlink()
        self.context_failure("regular current file")

    def test_missing_registered_bundle_file_is_rejected(self) -> None:
        self.make_bundle_fixture()
        del self.entry["bundle_files"][f"probes/{NAME}/companion.py"]
        self.save_manifest()
        self.context_failure("exactly the permitted bundle paths")

    def test_missing_registered_context_file_is_rejected(self) -> None:
        del self.entry["context_files"]["STATUS.md"]
        self.save_manifest()
        self.context_failure("exactly the permitted context paths")

    def test_unlisted_bundle_path_is_rejected(self) -> None:
        self.make_bundle_fixture()
        for path in ("../companion.py", "tools/injected.py", "canon/CANON.md",
                     f"probes/{NAME}/../companion.py", f"probes/{NAME}/RUN.md"):
            with self.subTest(path=path):
                self.entry["bundle_files"][path] = blob_spec(b"payload")
                self.save_manifest()
                self.context_failure("exactly the permitted bundle paths")
                del self.entry["bundle_files"][path]

    def test_bundle_blob_hash_and_size_are_binding(self) -> None:
        self.make_bundle_fixture()
        spec = self.entry["bundle_files"][f"probes/{NAME}/companion.py"]
        original = dict(spec)
        for field, value, error in (("sha256", "0" * 64, "SHA-256 differs"),
                                    ("bytes", spec["bytes"] + 1, "Git byte count differs"),
                                    ("git_blob", "0" * 40, "registered regular Git blob")):
            with self.subTest(field=field):
                spec.update(original)
                spec[field] = value
                self.save_manifest()
                self.context_failure(error)

    def test_duplicate_bundle_key_is_rejected(self) -> None:
        self.make_bundle_fixture()
        data = json.dumps(self.manifest).replace('"bundle_files": {',
                                               '"bundle_files": {"x": {}, "x": {}, ')
        self.write(context.MANIFEST, data.encode())
        self.context_failure("repeats x")

    def test_unknown_probe_cannot_reuse_another_path_allowance(self) -> None:
        self.manifest["probes"] = {"P-UNREVIEWED": self.entry}
        self.save_manifest()
        self.context_failure("no reviewed replay path allowance")

    def test_current_canon_changes_replay_frozen_bytes_without_modifying_checkout(self) -> None:
        for path in INPUTS:
            self.write(path, b"new current content")
        self.commit("next release")
        output = self.replay()
        self.assertIn(f"VERIFY HISTORICAL CONTEXT {NAME} {self.pin} 3 inputs", output)
        self.assertIn(f"VERIFY PASS {NAME}", output)
        for path in INPUTS:
            self.assertEqual((self.root / path).read_bytes(), b"new current content")

    def test_materialized_tree_is_exact_and_removed_after_use(self) -> None:
        with redirect_stdout(StringIO()):
            with context.execution_root(self.root, NAME, self.pin, SCRIPT) as isolated:
                self.assertNotEqual(isolated, self.root)
                files = {p.relative_to(isolated).as_posix(): p.read_bytes()
                         for p in isolated.rglob("*") if p.is_file()}
                self.assertEqual(files, {**INPUTS, f"probes/{NAME}/verify.py": SCRIPT})
        self.assertFalse(isolated.exists())

    def test_unregistered_probe_keeps_standard_current_tree_replay(self) -> None:
        self.manifest["probes"] = {}
        self.save_manifest()
        self.assertNotIn("HISTORICAL", self.replay())
        self.write("canon/CANON.md", b"changed")
        with redirect_stdout(StringIO()), self.assertRaises(SystemExit):
            self.replay()

    def test_run_and_expected_checks_are_not_bypassed(self) -> None:
        self.write(f"probes/{NAME}/EXPECTED.txt", b"forged\n")
        output = StringIO()
        with patch.object(check_verifier, "ROOT", self.root), redirect_stdout(output):
            with self.assertRaises(SystemExit):
                check_verifier.reproduce(self.probe)
        self.assertIn("EXPECTED.txt SHA-256 differs", output.getvalue())
        self.assertNotIn("HISTORICAL", output.getvalue())

    def test_current_verifier_tamper_rejected_even_if_run_hash_is_updated(self) -> None:
        modified = SCRIPT + b"# changed\n"
        self.write(f"probes/{NAME}/verify.py", modified)
        with self.assertRaisesRegex(context.ReplayContextError, "current verifier differs"):
            with context.execution_root(self.root, NAME, self.pin, modified):
                self.fail("tampered verifier executed")

    def test_current_prereg_tamper_rejected(self) -> None:
        self.write(f"probes/{NAME}/PREREG.md", b"changed context declaration")
        self.context_failure("current prereg differs")

    def test_context_hash_size_and_blob_tampering_rejected(self) -> None:
        spec = self.entry["context_files"]["STATUS.md"]
        original = dict(spec)
        for field, value, error in (
            ("sha256", "0" * 64, "SHA-256 differs"),
            ("bytes", spec["bytes"] + 1, "Git byte count differs"),
            ("git_blob", "0" * 40, "registered regular Git blob"),
        ):
            with self.subTest(field=field):
                spec.update(original)
                spec[field] = value
                self.save_manifest()
                self.context_failure(error)

    def test_verifier_identity_in_registration_is_binding(self) -> None:
        self.entry["verifier"]["sha256"] = "0" * 64
        self.save_manifest()
        self.context_failure("SHA-256 differs")

    def test_nonancestor_context_is_rejected(self) -> None:
        self.git("checkout", "--orphan", "unrelated")
        self.commit("unrelated root")
        self.context_failure("merge-base failed")

    def test_run_pin_must_equal_registered_pin(self) -> None:
        self.entry["pin_commit"] = "0" * 40
        self.save_manifest()
        self.context_failure("RUN pin differs")

    def test_missing_context_blob_cannot_fall_back_to_current_file(self) -> None:
        self.git("rm", "STATUS.md")
        new_pin = self.commit("pin without status")
        self.pin = self.entry["pin_commit"] = new_pin
        self.save_manifest()
        self.write("STATUS.md", INPUTS["STATUS.md"])
        self.context_failure("registered regular Git blob")

    def test_git_symlink_mode_is_rejected_before_materialization(self) -> None:
        # Construct a Git link entry without requiring host symlink privileges.
        blob = self.entry["context_files"]["STATUS.md"]["git_blob"]
        self.git("update-index", "--cacheinfo", f"120000,{blob},STATUS.md")
        self.git("-c", "user.name=Replay Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgSign=false", "commit", "-qm", "link entry")
        self.pin = self.entry["pin_commit"] = self.git("rev-parse", "HEAD").decode().strip()
        self.save_manifest()
        self.context_failure("registered regular Git blob")

    def test_unlisted_paths_commands_and_traversal_are_rejected(self) -> None:
        for bad_path in ("../STATUS.md", "/STATUS.md", "C:/STATUS.md", "tools/injected.py",
                         "canon/../STATUS.md", "canon\\CANON.md"):
            with self.subTest(path=bad_path):
                self.entry["context_files"][bad_path] = blob_spec(b"payload")
                self.save_manifest()
                self.context_failure("exactly the permitted context paths")
                del self.entry["context_files"][bad_path]
        self.entry["command"] = "arbitrary command"
        self.save_manifest()
        self.context_failure("invalid fields")

    def test_duplicate_json_key_cannot_select_a_second_registration(self) -> None:
        self.write(context.MANIFEST, b'{"schema":1,"schema":1,"probes":{}}')
        self.context_failure("repeats schema")

    def test_missing_manifest_fails_closed(self) -> None:
        (self.root / context.MANIFEST).unlink()
        self.context_failure("must be a regular current file")

    def test_context_control_change_selects_registered_probe(self) -> None:
        base = self.commit("closed fixture with registration")
        for path in sorted(context.REPLAY_CONTROL_PATHS):
            with self.subTest(path=path):
                target = self.root / path
                previous = target.read_bytes() if target.exists() else b"# fixture\n"
                self.write(path, previous + b"\n")
                self.commit("runner maintenance")
                with patch.object(check_verifier, "ROOT", self.root), \
                     patch.object(check_verifier, "PROBES", self.root / "probes"):
                    self.assertEqual(check_verifier.changed_probes(base), [self.probe])
                base = self.git("rev-parse", "HEAD").decode().strip()

    def test_canon_change_still_selects_every_probe(self) -> None:
        other = self.root / "probes" / "P-OTHER-FIXTURE"
        other.mkdir()
        (other / "verify.py").write_bytes(b"# other")
        base = self.commit("two probes")
        self.write("canon/CANON.md", b"new canon")
        self.commit("canon update")
        with patch.object(check_verifier, "ROOT", self.root), \
             patch.object(check_verifier, "PROBES", self.root / "probes"), \
             redirect_stdout(StringIO()):
            self.assertEqual(set(check_verifier.changed_probes(base)), {self.probe, other})


class ReviewedRegistrationTests(unittest.TestCase):
    """Read only custody metadata; never import or execute a scientific file."""

    def test_early_source_registration_covers_both_complete_manifests(self) -> None:
        root = Path(__file__).resolve().parents[1]
        name = "P-U-EARLY-SOURCE-FIBRE-CONTACT-1"
        prefix = f"probes/{name}/"
        entry = context.registrations(root)[name]
        source = json.loads((root / prefix / "SOURCE.json").read_bytes())
        self.assertEqual(set(entry["context_files"]), set(source["files"]))
        for path, spec in entry["context_files"].items():
            self.assertEqual({key: spec[key] for key in ("sha256", "bytes")},
                             source["files"][path])
        listed = dict(line.split("  ", 1)[::-1] for line in
                      (root / prefix / "INPUTS.sha256").read_text().splitlines())
        local = {**entry["bundle_files"], prefix + "verify.py": entry["verifier"],
                 prefix + "PREREG.md": entry["prereg"]}
        self.assertEqual(set(local), {prefix + p for p in listed} | {prefix + "INPUTS.sha256"})
        for path, spec in local.items():
            context.verify_bytes((root / path).read_bytes(), spec, path)
            if path != prefix + "INPUTS.sha256":
                self.assertEqual(spec["sha256"], listed[path.removeprefix(prefix)])

    def test_control_changes_select_both_registered_probes(self) -> None:
        root = Path(__file__).resolve().parents[1]
        expected = [root / "probes" / name for name in sorted(context.registrations(root))]
        self.assertEqual(len(expected), 2)
        for path in context.REPLAY_CONTROL_PATHS:
            with self.subTest(path=path):
                result = subprocess.CompletedProcess([], 0, path + "\n", "")
                with patch.object(check_verifier, "ROOT", root), \
                     patch.object(check_verifier, "PROBES", root / "probes"), \
                     patch.object(check_verifier.subprocess, "run", return_value=result):
                    self.assertEqual(check_verifier.changed_probes("0" * 40), expected)


if __name__ == "__main__":
    unittest.main()
