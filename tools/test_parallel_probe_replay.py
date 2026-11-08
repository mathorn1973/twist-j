"""Exercise scheduling with tiny spawned workers, never scientific replays."""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch

from tools import check_verifier as verifier


def tiny_worker(probe: Path) -> verifier.ReplayOutcome:
    """One independent fixture directory records real worker intervals."""
    started = time.monotonic()
    setting = json.loads((probe / "input.json").read_text())
    time.sleep(setting.get("delay", 0.01))
    stopped = time.monotonic()
    (probe / "receipt.json").write_text(json.dumps({
        "start": started, "end": stopped, "pid": os.getpid(),
    }))
    if setting.get("raise"):
        raise RuntimeError("fixture worker exception")
    if setting.get("missing"):
        return None
    return verifier.ReplayOutcome(
        probe.name, f"fixture {probe.name}\n", not setting.get("fail", False),
        stopped - started,
    )


class ParallelReplayTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.environment = patch.dict(os.environ, {"TWISTJ_EVIDENCE_DIR": ""})
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def probe(self, name: str, **settings: object) -> Path:
        path = self.root / name
        path.mkdir()
        (path / "input.json").write_text(json.dumps(settings))
        return path

    def run_selected(self, probes: list[Path], exclusive: set[str] | None = None,
                     *, reorder: bool = True):
        output = StringIO()
        exclusive = exclusive or set()
        with redirect_stdout(output):
            result = verifier.replay_selected(
                probes, worker=tiny_worker,
                eligible=lambda probe: probe.name not in exclusive,
                reorder=lambda: reorder,
            )
        return result, output.getvalue()

    @staticmethod
    def receipt(probe: Path) -> dict:
        return json.loads((probe / "receipt.json").read_text())

    def test_real_workers_bound_coverage_and_sorted_output(self) -> None:
        probes = [self.probe(f"P-{i}", delay=0.20 if i == 0 else 0.08)
                  for i in range(6)]
        result, output = self.run_selected(list(reversed(probes)))
        self.assertTrue(result)
        self.assertEqual([line for line in output.splitlines() if line.startswith("fixture ")],
                         [f"fixture {probe.name}" for probe in probes])
        receipts = [self.receipt(probe) for probe in probes]
        self.assertEqual(len({receipt["pid"] for receipt in receipts}), 2)
        events = sorted((r[key], delta) for r in receipts
                        for key, delta in (("start", 1), ("end", -1)))
        active = maximum = 0
        for _, delta in events:
            active += delta
            maximum = max(maximum, active)
        self.assertEqual(active, 0)
        self.assertEqual(maximum, 2)
        self.assertNotIn(os.getpid(), {r["pid"] for r in receipts})
        self.assertEqual(output.count("VERIFY REPLAY TIME "), len(probes))

    def test_all_read_only_work_drains_before_serial_exclusive_phase(self) -> None:
        probes = [self.probe(f"P-{i}", delay=0.07) for i in range(6)]
        result, output = self.run_selected(probes, exclusive={"P-1", "P-3"})
        self.assertTrue(result)
        receipts = [self.receipt(probe) for probe in probes]
        self.assertLessEqual(max(receipts[i]["end"] for i in (0, 2, 4, 5)),
                             receipts[1]["start"])
        self.assertLessEqual(receipts[1]["end"], receipts[3]["start"])
        self.assertEqual([line for line in output.splitlines() if line.startswith("fixture ")],
                         [f"fixture P-{i}" for i in (0, 2, 4, 5, 1, 3)])

    def test_real_fallback_pool_keeps_lazy_alphabetical_barriers(self) -> None:
        probes = [self.probe(f"P-{i}", delay=0.04) for i in range(5)]
        result, output = self.run_selected(probes, exclusive={"P-2"}, reorder=False)
        self.assertTrue(result)
        self.assertIn("VERIFY REPLAY SCHEDULE alphabetical-barriers\n", output)
        receipts = [self.receipt(probe) for probe in probes]
        self.assertLessEqual(max(r["end"] for r in receipts[:2]), receipts[2]["start"])
        self.assertLessEqual(receipts[2]["end"], min(r["start"] for r in receipts[3:]))
        self.assertEqual([line for line in output.splitlines() if line.startswith("fixture ")],
                         [f"fixture {probe.name}" for probe in probes])

    def test_later_selected_work_and_later_failure_are_not_dropped(self) -> None:
        probes = [self.probe("P-0", fail=True), self.probe("P-1"),
                  self.probe("P-2", fail=True), self.probe("P-3")]
        result, output = self.run_selected(probes, exclusive={"P-2"})
        self.assertFalse(result)
        for probe in probes:
            self.assertTrue((probe / "receipt.json").is_file())
            self.assertEqual(output.count(f"fixture {probe.name}\n"), 1)

    def test_unexpected_worker_exception_is_failure_and_retains_traceback(self) -> None:
        probes = [self.probe("P-0", **{"raise": True}), self.probe("P-1")]
        result, output = self.run_selected(probes)
        self.assertFalse(result)
        self.assertIn("Traceback", output)
        self.assertIn("fixture worker exception", output)
        self.assertIn("fixture P-1\n", output)

    def test_missing_worker_outcome_cannot_pass(self) -> None:
        result, output = self.run_selected([self.probe("P-0", missing=True)])
        self.assertFalse(result)
        self.assertIn("missing or mismatched replay outcome", output)

    def test_empty_selection_starts_no_pool(self) -> None:
        with patch.object(verifier, "ProcessPoolExecutor") as pool:
            result, output = self.run_selected([])
        self.assertTrue(result)
        self.assertEqual(output, "")
        pool.assert_not_called()

    def test_single_selection_runs_once(self) -> None:
        probe = self.probe("P-single")
        result, output = self.run_selected([probe])
        self.assertTrue(result)
        self.assertEqual(output.count("fixture P-single\n"), 1)
        self.assertNotEqual(self.receipt(probe)["pid"], os.getpid())

    def test_duplicate_selection_fails_before_launch(self) -> None:
        probe = self.probe("P-duplicate")
        with patch.object(verifier, "ProcessPoolExecutor") as pool:
            with self.assertRaises(SystemExit), redirect_stdout(StringIO()):
                verifier.replay_selected([probe, probe])
        pool.assert_not_called()

    def test_nonempty_evidence_directory_fails_before_launch_without_rewriting(self) -> None:
        with patch.dict(os.environ, {"TWISTJ_EVIDENCE_DIR": "/fixture/shared"}):
            with patch.object(verifier, "ProcessPoolExecutor") as pool:
                with self.assertRaises(SystemExit), redirect_stdout(StringIO()):
                    verifier.replay_selected([self.probe("P-evidence")])
                pool.assert_not_called()
            self.assertEqual(os.environ["TWISTJ_EVIDENCE_DIR"], "/fixture/shared")

    def test_only_matching_named_verifier_bytes_are_parallel_eligible(self) -> None:
        probe = self.probe("P-known")
        source = b"print('fixture')\n"
        (probe / "verify.py").write_bytes(source)
        with patch.object(verifier, "PARALLEL_SOURCE_SHA256",
                          {probe.name: (verifier.sha256(source),
                                        verifier._probe_tree_sha256(probe))}):
            self.assertTrue(verifier._parallel_eligible(probe))
            (probe / "json.py").write_text("# new module shadow\n")
            self.assertFalse(verifier._parallel_eligible(probe))
            (probe / "json.py").unlink()
            (probe / "shadow").symlink_to(probe / "verify.py")
            self.assertFalse(verifier._parallel_eligible(probe))
            (probe / "shadow").unlink()
            self.assertTrue(verifier._parallel_eligible(probe))
            (probe / "verify.py").write_bytes(source + b"# change\n")
            self.assertFalse(verifier._parallel_eligible(probe))
            self.assertFalse(verifier._parallel_eligible(self.probe("P-future")))
            (probe / "verify.py").unlink()
            self.assertFalse(verifier._parallel_eligible(probe))

    def test_shared_build_and_clean_checkout_probes_are_exclusive(self) -> None:
        for name in ("P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1",
                     "P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2"):
            self.assertNotIn(name, verifier.PARALLEL_SOURCE_SHA256)
            self.assertFalse(verifier._parallel_eligible(verifier.PROBES / name))

    def test_all_parallel_admission_precedes_any_exclusive_writer(self) -> None:
        probes = [self.probe(f"P-{i}") for i in range(3)]
        source = b"print('fixture')\n"
        bindings = {}
        for probe in probes[1:]:
            (probe / "verify.py").write_bytes(source)
            bindings[probe.name] = (verifier.sha256(source),
                                    verifier._probe_tree_sha256(probe))
        with patch.object(verifier, "PARALLEL_SOURCE_SHA256", bindings):
            batches = verifier._replay_batches(probes, verifier._parallel_eligible,
                                               reorder=True)
            # Both reviewed readers finish before this exclusive writer starts.
            self.assertEqual(next(batches), probes[1:])
            self.assertEqual(next(batches), [probes[0]])
            (probes[1] / "json.py").write_text("# new import surface\n")
            # There is no later parallel admission for the writer to invalidate.
            with self.assertRaises(StopIteration):
                next(batches)
            self.assertFalse(verifier._parallel_eligible(probes[1]))

    def test_fallback_rechecks_eligibility_after_exclusive_mutation(self) -> None:
        probes = [self.probe(f"P-{i}") for i in range(3)]
        source = b"print('fixture')\n"
        bindings = {}
        for probe in probes[1:]:
            (probe / "verify.py").write_bytes(source)
            bindings[probe.name] = (verifier.sha256(source),
                                    verifier._probe_tree_sha256(probe))
        with patch.object(verifier, "PARALLEL_SOURCE_SHA256", bindings):
            batches = verifier._replay_batches(probes, verifier._parallel_eligible)
            self.assertEqual(next(batches), [probes[0]])
            (probes[1] / "json.py").write_text("# new import surface\n")
            self.assertEqual(next(batches), [probes[1]])
            self.assertEqual(next(batches), [probes[2]])
            with self.assertRaises(StopIteration):
                next(batches)

    def test_complete_source_guard_rejects_new_probe_and_changed_context(self) -> None:
        probe_root = self.root / "probes"
        probe_root.mkdir()
        (probe_root / "P-known").mkdir()
        tool_root = self.root / "tools"
        tool_root.mkdir()
        helper = tool_root / "context.py"
        helper.write_bytes(b"# reviewed context\n")
        with patch.object(verifier, "ROOT", self.root), \
                patch.object(verifier, "PROBES", probe_root), \
                patch.object(verifier, "REORDER_PROBES_SHA256",
                             verifier._probe_tree_sha256(probe_root)), \
                patch.object(verifier, "REORDER_TOOL_NAMESPACE_SHA256",
                             verifier._tool_namespace_sha256()), \
                patch.object(verifier, "REORDER_INPUT_SHA256",
                             {"tools/context.py": verifier.sha256(helper.read_bytes())}):
            self.assertTrue(verifier._global_reorder_eligible())
            shadow = tool_root / "json.py"
            shadow.write_bytes(b"# added import shadow\n")
            self.assertFalse(verifier._global_reorder_eligible())
            shadow.unlink()
            cache = tool_root / "__pycache__"
            cache.mkdir()
            (cache / "context.cpython-312.pyc").write_bytes(b"fixture cache\n")
            self.assertTrue(verifier._global_reorder_eligible())
            future = probe_root / "P-unknown"
            future.mkdir()
            self.assertFalse(verifier._global_reorder_eligible())
            future.rmdir()
            self.assertTrue(verifier._global_reorder_eligible())
            helper.write_bytes(b"# changed context\n")
            self.assertFalse(verifier._global_reorder_eligible())
            helper.unlink()
            self.assertFalse(verifier._global_reorder_eligible())

    def test_submission_priority_keeps_exact_coverage_and_sorted_phase_output(self) -> None:
        probes = [self.probe("P-A"),
                  self.probe("P-TWO-USE-TYPED-READOUT-CLOSURE-1"),
                  self.probe("P-CURVATURE-GAUSS-SPLIT-1"), self.probe("P-Z")]
        order = verifier._submission_order(probes)
        self.assertEqual(order, [probes[2], probes[1], probes[0], probes[3]])
        result, output = self.run_selected(probes)
        self.assertTrue(result)
        self.assertEqual([line for line in output.splitlines() if line.startswith("fixture ")],
                         [f"fixture {probe.name}" for probe in sorted(probes)])
        for probe in probes:
            self.assertTrue((probe / "receipt.json").is_file())

    def test_changed_helper_or_manifest_excludes_typed_readout(self) -> None:
        probe = self.probe("P-TWO-USE-TYPED-READOUT-CLOSURE-1")
        source = b"from apparatus import value\nprint(value)\n"
        (probe / "verify.py").write_bytes(source)
        helper = probe / "apparatus.py"
        saved = b"value = 1\n"
        helper.write_bytes(saved)
        (probe / "DOMAIN.tsv").write_bytes(b"original input\n")
        binding = (verifier.sha256(source), verifier._probe_tree_sha256(probe))
        with patch.object(verifier, "PARALLEL_SOURCE_SHA256", {probe.name: binding}):
            self.assertTrue(verifier._parallel_eligible(probe))
            helper.write_bytes(saved + b"\n# changed helper\n")
            self.assertFalse(verifier._parallel_eligible(probe))
            helper.write_bytes(saved)
            (probe / "DOMAIN.tsv").write_bytes(b"changed input\n")
            self.assertFalse(verifier._parallel_eligible(probe))

    def test_priority_name_cannot_bypass_source_admission(self) -> None:
        priority = self.probe("P-CURVATURE-GAUSS-SPLIT-1", delay=0.02)
        readers = [self.probe("P-A", delay=0.05), self.probe("P-Z", delay=0.05)]
        result, output = self.run_selected([priority, *readers],
                                           exclusive={priority.name})
        self.assertTrue(result)
        self.assertLessEqual(max(self.receipt(p)["end"] for p in readers),
                             self.receipt(priority)["start"])
        self.assertEqual(output.count(f"fixture {priority.name}\n"), 1)
        self.assertEqual(verifier._submission_order(readers), readers)

    def test_worker_wrapper_preserves_printed_failure_and_exception(self) -> None:
        probe = self.probe("P-wrapper")
        def failed(_: Path) -> None:
            print("original failure")
            raise SystemExit(1)
        with patch.object(verifier, "reproduce", side_effect=failed):
            outcome = verifier._replay_worker(probe)
        self.assertFalse(outcome.success)
        self.assertIn("original failure", outcome.output)
        with patch.object(verifier, "reproduce", side_effect=ValueError("unexpected")):
            outcome = verifier._replay_worker(probe)
        self.assertFalse(outcome.success)
        self.assertIn("Traceback", outcome.output)
        self.assertIn("ValueError: unexpected", outcome.output)
        with patch.object(verifier, "reproduce", side_effect=SystemExit(0)):
            self.assertFalse(verifier._replay_worker(probe).success)


if __name__ == "__main__":
    unittest.main()
