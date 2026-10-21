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

    def run_selected(self, probes: list[Path], exclusive: set[str] | None = None):
        output = StringIO()
        exclusive = exclusive or set()
        with redirect_stdout(output):
            result = verifier.replay_selected(
                probes, worker=tiny_worker,
                eligible=lambda probe: probe.name not in exclusive,
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

    def test_exclusive_barrier_drains_and_finishes_before_successors(self) -> None:
        probes = [self.probe(f"P-{i}", delay=0.07) for i in range(5)]
        result, _ = self.run_selected(probes, exclusive={"P-2"})
        self.assertTrue(result)
        receipts = [self.receipt(probe) for probe in probes]
        self.assertLessEqual(max(r["end"] for r in receipts[:2]), receipts[2]["start"])
        self.assertLessEqual(receipts[2]["end"], min(r["start"] for r in receipts[3:]))

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

    def test_exclusive_changes_are_rechecked_before_later_eligibility(self) -> None:
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
            # A future exclusive program leaves a module in a later directory.
            (probes[1] / "json.py").write_text("# new import surface\n")
            self.assertEqual(next(batches), [probes[1]])
            self.assertEqual(next(batches), [probes[2]])
            with self.assertRaises(StopIteration):
                next(batches)

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
