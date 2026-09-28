#!/usr/bin/env python3
"""Synthetic analyzer contract tests, executed only after the public pin.

These invented sufficient sums are not lattice observations or scientific
fixtures. They exercise refusal, custody, precedence, and zero-variance rules.
No sampler is imported or invoked.
"""

import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

import analyze


COLUMNS = (
    "L k base chain block n n0 sumT sumT2 sumY0 sumY0sq sumPosT sumNegT "
    "sumW1 sumW0 sumM1 sumM0 sumP1 sumP0 nTpos nTneg target_T_sign_changes "
    "sum_action sum_action2 target_flip_attempts target_flip_accepts "
    "target_endpoint_changes swap_attempts swap_accepts min_swap_accept roundtrips"
).split()


def fixture_text(key):
    size, mode, base, chain = key
    metadata = {
        "format": "twist_cut_transport_blocks_v1", "L": size, "k": mode,
        "base": base, "chain": chain,
        "seed": 202609280000 + 10000 * base + 1000 * size + 100 * mode + chain,
        "replicas": 65, "warmup_sweeps": 2048, "production_sweeps": 16384,
        "block_length": 128, "endpoint_proposal_probability": "0.5",
        "chain_initial": ["cold0", "hot0", "cold1", "hot1", "alt1"][chain],
        "sampling": "every_production_sweep_after_local_sheet_endpoint_and_exchange_updates",
        "cut": "all_01_plaquettes_x0_equals_0",
        "sheet_orbits": "all_x1_slices_every_replica_every_sweep",
        "lambda_ladder": ",".join(str(j / 64) for j in range(65)),
    }
    out = io.StringIO()
    for name, value in metadata.items():
        out.write(f"# {name}\t{value}\n")
    writer = csv.DictWriter(out, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    # Dyadic signs give nonzero block errors at all four frozen scales.
    # Their magnitudes are chosen before execution; no scientific data enter.
    for block in range(128):
        offset = sum(weight * (1 if block & (1 << bit) else -1)
                     for bit, weight in enumerate((8, 6, 4, 3, 2, 1, 1)))
        n0, n1 = 64 + offset, 64 - offset
        signed = -float(offset)
        row = {name: 0 for name in COLUMNS}
        row.update(L=size, k=mode, base=base, chain=chain, block=block,
                   n=128, n0=n0, sumT=signed, sumT2=signed ** 2 / n1,
                   sumY0=-signed, sumY0sq=signed ** 2 / n0,
                   sumPosT=max(signed, 0), sumNegT=max(-signed, 0),
                   sumM0=n0 / 4, sumP0=n0 / 4,
                   sumM1=n1 / 4, sumP1=n1 / 4,
                   nTpos=n1 if signed > 0 else 0, nTneg=n1 if signed < 0 else 0,
                   target_T_sign_changes=0,
                   target_flip_attempts=64, target_flip_accepts=1,
                   target_endpoint_changes=4, swap_attempts=4096,
                   swap_accepts=2048, min_swap_accept=0.5, roundtrips=1)
        writer.writerow(row)
    for edge in range(64):
        out.write(f"# swap_edge\t{edge}\t8192\t4096\n")
    for replica in range(65):
        out.write(f"# replica_roundtrips\t{replica}\t{128 if replica == 0 else 0}\n")
    out.write("# completion\tPASS\n")
    return out.getvalue()


def execution_record(stem, stdout, stderr=b""):
    return {"stem": stem, "exit_code": 0, "seconds": 0.0,
            "stdout_bytes": len(stdout), "stderr_bytes": len(stderr),
            "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
            "stderr_sha256": hashlib.sha256(stderr).hexdigest()}


class AnalyzerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix="cut-analyzer-fixture-")
        cls.directory = Path(cls.temporary.name)
        cls.runs, cls.records = [], []
        for key in analyze.expected_keys():
            stem = analyze.stem_for(key)
            raw = fixture_text(key).encode("utf-8")
            path = cls.directory / (stem + ".tsv")
            path.write_bytes(raw)
            (cls.directory / (stem + ".stderr")).write_bytes(b"")
            cls.runs.append(analyze.read_run(path))
            cls.records.append(execution_record(stem, raw))
        for stem, expected in (("audit", analyze.AUDIT_TEXT),
                               ("analyzer_tests", analyze.TEST_TEXT)):
            raw = expected.encode("utf-8")
            (cls.directory / (stem + ".tsv")).write_bytes(raw)
            (cls.directory / (stem + ".stderr")).write_bytes(b"")
            cls.records.append(execution_record(stem, raw))
        cls.manifest = cls.directory / "execution.json"
        cls.manifest.write_text(json.dumps(cls.records), encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def assert_parse_rejected(self, transform, fragment):
        path = self.directory / "mutation.tsv"
        path.write_text(transform(fixture_text((4, 1, 0, 0))), encoding="utf-8")
        try:
            with self.assertRaisesRegex(analyze.InvalidInput, fragment):
                analyze.read_run(path)
        finally:
            path.unlink()

    def test_complete_synthetic_transport_fixture(self):
        result = analyze.read_execution(self.directory)
        self.assertEqual(result["status"], "TRANSPORT_QUALIFIED")
        self.assertEqual(len(result["groups"]), 4)
        self.assertEqual(result["available_run_count"], 20)
        self.assertFalse(result["execution_errors"])
        for group in result["groups"]:
            self.assertTrue(group["mobility_pass"])
            self.assertTrue(all(item["evaluated_after_mobility"]
                                for item in group["identity_residuals"].values()))
            self.assertEqual(group["pooled"]["signed_ratio"]["label"],
                             "NONINFERENTIAL_ESTIMATE")
        # No inferred interval or squared diagnostic is created by any branch.
        def inspect(value):
            if isinstance(value, dict):
                self.assertTrue(all("interval" not in str(key).lower() for key in value))
                for child in value.values():
                    inspect(child)
            elif isinstance(value, list):
                for child in value:
                    inspect(child)
        inspect(result)

    def test_mobility_precedes_exact_identity(self):
        runs = copy.deepcopy(self.runs)
        for block in runs[0]["blocks"]:
            block["target_endpoint_changes"] = 0
        # Also introduce a known control violation; it must stay unevaluated.
        for run in runs:
            if run["key"][1:3] == (1, 2):
                for block in run["blocks"]:
                    block["sumY0"] += block["n0"]
                    block["sumT"] += block["n"] - block["n0"]
        result = analyze.report(runs)
        self.assertEqual(result["status"], "INCONCLUSIVE_MOBILITY")
        self.assertTrue(any("endpoint_changes" in failure
                            for group in result["groups"] for failure in group["mobility_failures"]))
        self.assertTrue(all(not residual["evaluated_after_mobility"]
                            for group in result["groups"]
                            for residual in group["identity_residuals"].values()))

    def test_control_shift_after_mobility(self):
        runs = copy.deepcopy(self.runs)
        for run in runs:
            if run["key"][1:3] == (1, 2):
                for block in run["blocks"]:
                    block["sumY0"] += block["n0"]
                    block["sumT"] += block["n"] - block["n0"]
        result = analyze.report(runs)
        self.assertEqual(result["status"], "FAIL_CONSISTENCY")
        group = next(g for g in result["groups"] if (g["k"], g["base"]) == (1, 2))
        self.assertTrue(group["mobility_pass"])
        residual = group["identity_residuals"]["reversal_mean_Y"]
        self.assertTrue(residual["evaluated_after_mobility"])
        self.assertFalse(residual["would_pass"])
        self.assertAlmostEqual(residual["residual"], 1.0)

    def test_separated_chain_cannot_inflate_its_agreement_error(self):
        runs = copy.deepcopy(self.runs)
        for block in runs[4]["blocks"]:
            block["sumT"] += 10 * (block["n"] - block["n0"])
        result = analyze.report(runs)
        self.assertEqual(result["status"], "INCONCLUSIVE_MOBILITY")
        failures = result["groups"][0]["mobility_failures"]
        self.assertIn("chain_4:Y1:leave_one_out_disagreement", failures)

    def test_zero_winding_error_is_not_forced_branch_occupation(self):
        zero = {"se_by_block_length": {str(n): 0.0 for n in (128, 256, 512, 1024)}}
        self.assertTrue(analyze.coarsening(zero, "M0")["pass"])
        self.assertFalse(analyze.coarsening(zero, "Y0")["pass"])
        mixed = {"se_by_block_length": {"128": 0.0, "256": 1.0, "512": 1.0, "1024": 1.0}}
        self.assertFalse(analyze.coarsening(mixed, "W0")["pass"])

    def test_batch_ratio_uses_joint_residual_and_all_observations(self):
        blocks = copy.deepcopy(self.runs[0]["blocks"])
        for block in blocks:
            block["sumT"] = 3 * block["n0"]
        summary = analyze.ratio_summary([blocks], "signed_ratio")
        self.assertEqual(summary["mean"], 3.0)
        self.assertEqual(summary["batch_se"], 0.0)
        self.assertEqual(summary["observations"], 16384)

    def test_between_chain_dispersion_is_not_batch_error(self):
        first = copy.deepcopy(self.runs[0]["blocks"])
        second = copy.deepcopy(first)
        # A plain mean avoids denominator fluctuations: two constant but
        # incompatible chain means have zero within-chain batch error.
        for block in first:
            block["sumY0"], block["sumT"] = 0.0, 0.0
        for block in second:
            block["sumY0"], block["sumT"] = float(block["n"]), 0.0
        summary = analyze.ratio_summary([first, second], "Y_unconditional")
        self.assertEqual(summary["mean"], 0.5)
        self.assertEqual(summary["batch_se"], 0.0)
        self.assertGreater(summary["chain_residual_se"], 0.0)

    def test_wrong_seed(self):
        self.assert_parse_rejected(lambda text: text.replace("# seed\t202609284100",
                                                           "# seed\t202609284101"),
                                   "incorrect seed")

    def test_nonfinite_record(self):
        def transform(text):
            lines = text.splitlines()
            header = next(i for i, line in enumerate(lines) if not line.startswith("#"))
            fields = lines[header + 1].split("\t")
            fields[COLUMNS.index("sumT")] = "nan"
            lines[header + 1] = "\t".join(fields)
            return "\n".join(lines) + "\n"
        self.assert_parse_rejected(transform, "nonfinite number")

    def test_sign_split_mismatch(self):
        def transform(text):
            lines = text.splitlines()
            header = next(i for i, line in enumerate(lines) if not line.startswith("#"))
            fields = lines[header + 1].split("\t")
            fields[COLUMNS.index("sumPosT")] = str(float(fields[COLUMNS.index("sumPosT")]) + 1)
            lines[header + 1] = "\t".join(fields)
            return "\n".join(lines) + "\n"
        self.assert_parse_rejected(transform, "sign-split mismatch")

    def test_wrong_custody_hash(self):
        records = copy.deepcopy(self.records)
        records[0]["stdout_sha256"] = "0" * 64
        self.manifest.write_text(json.dumps(records), encoding="utf-8")
        try:
            result = analyze.read_execution(self.directory)
        finally:
            self.manifest.write_text(json.dumps(self.records), encoding="utf-8")
        self.assertEqual(result["status"], "FAIL_IMPLEMENTATION")
        self.assertTrue(any("stdout_sha256 mismatch" in error for error in result["execution_errors"]))
        self.assertTrue(all(not residual["evaluated_after_mobility"]
                            for group in result["groups"]
                            for residual in group["identity_residuals"].values()))

    def test_missing_declared_chain_is_implementation_failure(self):
        result = analyze.report(self.runs[:-1])
        self.assertEqual(result["status"], "FAIL_IMPLEMENTATION")
        self.assertEqual(result["missing_runs"], [[4, 2, 2, 4]])


def main():
    transcript = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AnalyzerTests)
    result = unittest.TextTestRunner(stream=transcript, verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.stderr.write(transcript.getvalue())
        return 1
    sys.stdout.write("NON-CANONICAL analyzer fixture audit\nresult\tPASS\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
