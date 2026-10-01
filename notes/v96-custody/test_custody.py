"""SOFTWARE/SYNTHETIC regression only, never a physical/formal scientific gate."""

import copy
from fractions import Fraction
from hashlib import sha256
import unittest

from schema import VERSION, ROLES, OFFSETS, Incident, contract, frame_keys, hash_object, packet, q
from project_target import project
from assess_target import assess
from metrology import COMPONENTS, expanded_uncertainty, integrate
from custody import (Witnessed, acquisition_binding, campaign_target_decision, framed_commitment,
                     lock_verdicts, release_permit, verify_commitment)
from acquisition import Capture, SyntheticAdapter, confirm_acquisition, retain
from audit_unblinded import (audit_target_and_source, full_state, replay_projection,
                            source_equality, source_origin)


def fixture(positive=False, work="1"):
    """Artificial unit-test tables; intentionally not claimed as the pinned law."""
    positive_table, null_table, grid = [], [], []
    for step, layer in frame_keys():
        end = Fraction(0) if not step else 10 * (step - 1) + OFFSETS[layer]
        grid.append(["0"] if not step else [str(end - Fraction(1, 10)), str(end)])
        base = {"step": step, "layer": layer, "coordinates": [0] * 31, "p": 0,
                "counts": dict.fromkeys(ROLES, 0)}
        null_table.append(copy.deepcopy(base))
        if step == 2 and layer in "BF":
            base["counts"]["r_2"] = 2
            base["coordinates"][30] = 2
        if step >= 3:
            base["p"] = 1
        if step == 3:
            base["coordinates"][0] = 1
            base["counts"]["B_2"] = 2
        positive_table.append(base)
    frozen = {"schema": VERSION, "kind": "PUBLIC_PREDICTIONS", "positive_tables": [positive_table],
              "null_table": null_table, "read_grid_s": grid, "optical_codes": [0, 1, 2, 3, 4]}
    frames = []
    table = positive_table if positive else null_table
    for expected, times in zip(table, grid):
        readings = [{"t_s": time, "coordinates": expected["coordinates"][:], "p": expected["p"],
                     "optical": expected["p"], "angle_deg": str(72 * expected["p"]), "temperature_C": "23",
                     "banks": {r: {"energy_J": str(Fraction(expected["counts"][r], 2)), "U_J": "1/1000", "voltage_V": "5"} for r in ROLES},
                     "flags": []} for time in times]
        frames.append({"step": expected["step"], "layer": expected["layer"], "readings": readings})
    zero = [{"t0_s": "0", "t1_s": "100", "V": "5", "I": "0", "flags": []}]
    ports = {r: copy.deepcopy(zero) for r in ROLES}
    if positive:
        ports["B_2"] = [
            {"t0_s": "0", "t1_s": "20", "V": "5", "I": "0", "flags": []},
            {"t0_s": "20", "t1_s": "22", "V": "5", "I": str(Fraction(work) / 10), "flags": []},
            {"t0_s": "22", "t1_s": "100", "V": "5", "I": "0", "flags": []}]
    target = {"frames": frames, "ports": ports,
              "uncertainty": {"time_s": "1/1000", "first_work_J": "1/100", "whole_abs_J": "1/1000",
                              "slot_abs_J": ["1/1000"] * 10}, "flags": []}
    inputs = {"raw": b"SYNTHETIC independent unit-test fixture", "calibration": b"synthetic calibration",
              "settings": b"synthetic sampling", "reducer": b"synthetic reducer source"}
    reduction = {"kind": "CALIBRATED_OBSERVATIONS", "origin": "SYNTHETIC", "target": target,
                 **{name + "_sha256": sha256(data).hexdigest() for name, data in inputs.items()}}
    return project(reduction, "0" * 32), frozen, reduction, inputs


def ledger():
    from audit_unblinded import OTHER_COMPONENTS
    components = dict.fromkeys(OTHER_COMPONENTS, "0")
    components["cartridge_contacts_probes"] = "1/100"
    return {"interval_s": ["0", "22"], "other_upper_J": components,
            "balances": {r: {"residual_J": "0", "U_J": "1/1000", "independent_measurement_sha256": "a" * 64} for r in ROLES}}


def locking():
    observed, frozen, _, _ = fixture()
    verdict = assess(observed, frozen)
    roster = [f"{i:032x}" for i in range(400)]
    verdicts = [{**verdict, "id": item} for item in roster]
    locked = lock_verdicts(roster, verdicts, hash_object(frozen))
    return roster, locked


class TestOnlyWitness:
    """No timestamp/security claim; only exercises consumer verification order."""
    def verify(self, receipt, expected, purpose):
        if receipt != (purpose + expected).encode("ascii"):
            raise Incident("test receipt mismatch")
        return Witnessed(expected, purpose, {"PREPARATION": 10, "RAW_CORPUS": 40, "VERDICTS": 50}[purpose], "TEST_ONLY")


class TestOnlyAcquisitionWitness:
    """Explicit mock of independently retained event records; no real receipts."""
    def __init__(self, begin=20, end=30):
        self.begin, self.end = begin, end

    def verify(self, receipt, expected, purpose):
        if receipt != (purpose + expected).encode("ascii"):
            raise Incident("test acquisition event binding mismatch")
        return Witnessed(expected, purpose,
                         {"ACQUISITION_START": self.begin, "ACQUISITION_END": self.end}[purpose],
                         "TEST_ONLY_ACQUISITION")


class Regressions(unittest.TestCase):
    def test_synthetic_null_and_positive_target_paths(self):
        for positive in (False, True):
            observed, frozen, _, _ = fixture(positive)
            verdict = assess(observed, frozen)
            self.assertEqual(verdict["positive" if positive else "null"], "SATISFIED")
            self.assertEqual(verdict["null" if positive else "positive"], "FAILED")
            self.assertIn("SYNTHETIC", verdict["findings"])

    def test_signed_cancellation_does_not_hide_absolute_work(self):
        observed, frozen, _, _ = fixture()
        observed["ports"]["B_2"] = [
            {"t0_s": "0", "t1_s": "1", "V": "1", "I": "1", "flags": []},
            {"t0_s": "1", "t1_s": "2", "V": "1", "I": "-1", "flags": []},
            {"t0_s": "2", "t1_s": "100", "V": "1", "I": "0", "flags": []}]
        self.assertEqual(integrate(observed["ports"]["B_2"], 0, 100), (0, 2))
        self.assertEqual(assess(observed, frozen)["null"], "FAILED")

    def test_target_can_satisfy_while_origin_fails(self):
        observed, frozen, _, _ = fixture(True, "24/25")
        verdict = assess(observed, frozen)
        self.assertEqual(verdict["positive"], "SATISFIED")
        origin = source_origin(observed, ledger())
        self.assertEqual(origin["source_lower_J"], "47/50")
        self.assertEqual(origin["status"], "FAILED")
        audit = audit_target_and_source(observed, verdict, "positive", ledger(), "SYNTHETIC")
        self.assertFalse(audit["campaign_pass"])
        self.assertEqual(audit["eligibility"], "NOT_CONFIRMATORY")

    def test_gross_backtransfer_cannot_be_counted_as_work(self):
        observed, frozen, _, _ = fixture(True)
        observed["ports"]["B_2"][1:2] = [
            {"t0_s": "20", "t1_s": "21", "V": "1", "I": "1", "flags": []},
            {"t0_s": "21", "t1_s": "22", "V": "1", "I": "-1", "flags": []}]
        self.assertEqual(assess(observed, frozen)["positive"], "FAILED")

    def test_missing_uncertainty_never_becomes_zero(self):
        observed, frozen, _, _ = fixture(True)
        observed["uncertainty"]["first_work_J"] = None
        self.assertEqual(assess(observed, frozen)["positive"], "INDETERMINATE")
        observed, frozen, _, _ = fixture()
        observed["uncertainty"]["whole_abs_J"] = None
        self.assertEqual(assess(observed, frozen)["null"], "INDETERMINATE")

    def test_expected_model_is_not_acquisition(self):
        _, _, reduction, _ = fixture()
        reduction["kind"] = "EXPECTED_MODEL_TRACE"
        with self.assertRaises(Incident):
            project(reduction, "0" * 32)

    def test_every_input_byte_is_bound_and_replayed(self):
        observed, _, reduction, inputs = fixture()
        self.assertEqual(replay_projection(reduction, observed, inputs, lambda *args: reduction), "PROJECTION_IDENTICAL")
        for name in inputs:
            changed = {**inputs, name: inputs[name] + b"x"}
            with self.subTest(name=name), self.assertRaises(Incident):
                replay_projection(reduction, observed, changed, lambda *args: reduction)
        with self.assertRaises(Incident):
            replay_projection(reduction, observed, inputs, None)
        changed = copy.deepcopy(reduction)
        changed["target"]["frames"][0]["readings"][0]["p"] = 1
        with self.assertRaises(Incident):
            replay_projection(reduction, observed, inputs, lambda *args: changed)

    def test_projection_removes_all_identifying_channels(self):
        _, _, reduction, _ = fixture()
        target = reduction["target"]
        forbidden = ("serial", "persistent_alias", "absolute_timestamp", "route", "cut_lock", "configuration",
                     "source_seed", "acquisition_order", "calibration_reference", "operator_notes", "filename", "unblinding_key")
        for name in forbidden:
            target[name] = "SECRET"
            target["frames"][0]["readings"][0][name] = "SECRET"
            target["frames"][0]["readings"][0]["banks"]["B_2"][name] = "SECRET"
            target["ports"]["B_2"][0][name] = "SECRET"
        projected = project(reduction, "0" * 32)
        from schema import canonical
        self.assertNotIn(b"SECRET", canonical(projected))
        for name in forbidden:
            bad = copy.deepcopy(projected)
            bad[name] = "SECRET"
            with self.subTest(name=name), self.assertRaises(Incident):
                assess(bad, fixture()[1])
        bad = copy.deepcopy(projected)
        bad["frames"][0]["readings"][0]["banks"]["B_2"]["serial"] = "SECRET"
        with self.assertRaises(Incident):
            packet(bad)

    def test_time_saturation_pointer_and_missing_samples(self):
        for fault in ("TIMING", "SATURATION", "POINTER", "MISSING"):
            observed, frozen, _, _ = fixture()
            first = observed["frames"][1]["readings"][0]
            if fault == "TIMING":
                first["t_s"] = "19/10" if first["t_s"] != "19/10" else "2"
            elif fault == "SATURATION":
                first["flags"] = ["SATURATION"]
            elif fault == "POINTER":
                first["p"] = 7
            else:
                observed["frames"][1]["readings"] = []
            with self.subTest(fault=fault):
                self.assertNotEqual(assess(observed, frozen)["null"], "SATISFIED")

    def test_missing_or_duplicate_frames_do_not_zip_truncate(self):
        observed, frozen, _, _ = fixture()
        observed["frames"].pop()
        self.assertEqual(assess(observed, frozen)["null"], "INDETERMINATE")
        observed, frozen, _, _ = fixture()
        observed["frames"].append(observed["frames"][-1])
        self.assertEqual(assess(observed, frozen)["null"], "INDETERMINATE")

    def test_nested_synthetic_survives_every_assessment_path(self):
        for location in ("reading", "port"):
            observed, frozen, reduction, _ = fixture(True)
            observed["flags"] = []
            if location == "reading":
                observed["frames"][2]["readings"][0]["flags"] = ["SYNTHETIC"]
            else:
                observed["ports"]["Z_2"][0]["flags"] = ["SYNTHETIC"]
            verdict = assess(observed, frozen)
            self.assertIn("SYNTHETIC", verdict["findings"])
            self.assertEqual(audit_target_and_source(observed, verdict, "positive", ledger(),
                                                    "MEASURED")["eligibility"], "NOT_CONFIRMATORY")
            observed["frames"].pop()
            incomplete = assess(observed, frozen)
            self.assertIn("FRAME_ROSTER", incomplete["findings"])
            self.assertIn("SYNTHETIC", incomplete["findings"])
        observed, frozen, reduction, _ = fixture(True)
        observed["frames"].pop()
        self.assertIn("SYNTHETIC", assess(observed, frozen)["findings"])
        reduction["origin"] = "MEASURED"
        reduction["target"]["frames"][2]["readings"][0]["flags"] = ["SYNTHETIC"]
        self.assertIn("SYNTHETIC", project(reduction, "0" * 32)["flags"])
        observed, frozen, _, _ = fixture(True)
        verdict = assess(observed, frozen)
        # Even a hypothetical stale/stripped packet cannot remove the locked
        # provenance marker merely by changing the external origin label.
        observed["flags"] = []
        verdict["packet_sha256"] = hash_object(observed)
        self.assertEqual(audit_target_and_source(observed, verdict, "positive", ledger(),
                                                "MEASURED")["eligibility"], "NOT_CONFIRMATORY")

    def test_required_local_series_cannot_be_empty_or_gapped(self):
        for role in ROLES:
            for missing in ("empty", "gap"):
                observed, frozen, _, _ = fixture(True)
                if missing == "empty":
                    observed["ports"][role] = []
                else:
                    observed["ports"][role][0]["t0_s"] = "1"
                verdict = assess(observed, frozen)
                self.assertEqual(verdict["positive"], "INDETERMINATE")
                self.assertIn("LOCAL_PORTS_MISSING", verdict["findings"])

    def test_known_failure_precedes_missing_frame(self):
        observed, frozen, _, _ = fixture()
        observed["frames"].pop()
        observed["frames"][0]["readings"][0]["flags"] = ["SATURATION"]
        verdict = assess(observed, frozen)
        self.assertEqual(verdict["null"], "FAILED")
        self.assertEqual(verdict["findings"], ["FRAME_ROSTER", "SATURATION", "SYNTHETIC"])

    def test_commitment_nonce_and_framing_byte_tamper(self):
        nonce = bytes(range(32))
        files = {"a": b"bc", "d": b"ef"}
        commitment = framed_commitment(files, nonce)
        verify_commitment(files, nonce, commitment)
        self.assertNotEqual(commitment, framed_commitment({"ab": b"c", "d": b"ef"}, nonce))
        for changed, secret in (({"a": b"bd", "d": b"ef"}, nonce), (files, b"z" * 32), (files, nonce[:31])):
            with self.assertRaises(Incident):
                verify_commitment(changed, secret, commitment)

    def test_399_and_duplicate_verdicts_rejected(self):
        roster, locked = locking()
        for verdicts in (locked["verdicts"][:399], locked["verdicts"][:399] + [locked["verdicts"][0]]):
            with self.assertRaises(Incident):
                lock_verdicts(roster, verdicts, locked["contract_sha256"])

    def test_local_time_is_not_independent_and_early_unblind_blocks(self):
        roster, locked = locking()
        commitments = {"PREPARATION": "a" * 64, "RAW_CORPUS": "b" * 64, "VERDICTS": hash_object(locked)}
        receipts = {p: (p + d).encode("ascii") for p, d in commitments.items()}
        common = (roster, locked, commitments, receipts)
        binding = acquisition_binding(roster, commitments)
        events = {p: (p + binding).encode("ascii") for p in ("ACQUISITION_START", "ACQUISITION_END")}
        with self.assertRaises(Incident):
            release_permit(*common, None, events, TestOnlyAcquisitionWitness(), [], True)
        with self.assertRaises(Incident):
            release_permit(*common, TestOnlyWitness(), events, None, [], True)
        permit = release_permit(*common, TestOnlyWitness(), events, TestOnlyAcquisitionWitness(), [], True)
        self.assertEqual(permit["kind"], "RELEASE_PERMIT")
        self.assertEqual(permit["acquisition_binding_sha256"], binding)
        self.assertEqual((permit["acquisition_start_ns"], permit["acquisition_end_ns"]), (20, 30))
        for begin, end, incidents, sealed in ((5, 30, [], True), (20, 45, [], True), (20, 30, ["KEY_LEAK"], True), (20, 30, [], False)):
            with self.assertRaises(Incident):
                release_permit(*common, TestOnlyWitness(), events, TestOnlyAcquisitionWitness(begin, end), incidents, sealed)
        receipts["VERDICTS"] = b"local timestamp asserted independent"
        with self.assertRaises(Incident):
            release_permit(*common, TestOnlyWitness(), events, TestOnlyAcquisitionWitness(), [], True)

    def test_acquisition_events_bind_preparation_raw_and_roster(self):
        roster, locked = locking()
        commitments = {"PREPARATION": "a" * 64, "RAW_CORPUS": "b" * 64, "VERDICTS": hash_object(locked)}
        binding = acquisition_binding(roster, commitments)
        events = {p: (p + binding).encode("ascii") for p in ("ACQUISITION_START", "ACQUISITION_END")}
        for field in ("PREPARATION", "RAW_CORPUS"):
            changed = {**commitments, field: "c" * 64}
            receipts = {p: (p + d).encode("ascii") for p, d in changed.items()}
            with self.assertRaises(Incident):
                release_permit(roster, locked, changed, receipts, TestOnlyWitness(), events,
                               TestOnlyAcquisitionWitness(), [], True)
        changed_roster = roster[:-1] + ["f" * 32]
        changed_verdicts = copy.deepcopy(locked["verdicts"])
        changed_verdicts[-1]["id"] = "f" * 32
        changed_lock = lock_verdicts(changed_roster, changed_verdicts, locked["contract_sha256"])
        changed = {**commitments, "VERDICTS": hash_object(changed_lock)}
        receipts = {p: (p + d).encode("ascii") for p, d in changed.items()}
        with self.assertRaises(Incident):
            release_permit(changed_roster, changed_lock, changed, receipts, TestOnlyWitness(), events,
                           TestOnlyAcquisitionWitness(), [], True)
        receipts = {p: (p + d).encode("ascii") for p, d in commitments.items()}
        for malformed in ({"ACQUISITION_START": 20, "ACQUISITION_END": 30},
                          {"ACQUISITION_START": b"local start", "ACQUISITION_END": b"local end"},
                          {"ACQUISITION_START": events["ACQUISITION_START"]}):
            with self.assertRaises(Incident):
                release_permit(roster, locked, commitments, receipts, TestOnlyWitness(), malformed,
                               TestOnlyAcquisitionWitness(), [], True)

    def test_synthetic_origin_cannot_be_relabelled_confirmatory(self):
        roster, locked = locking()
        labels = {item: ("positive", "offimage", "cut0", "cut1")[i // 100] for i, item in enumerate(roster)}
        # Even forged external origin labels cannot erase the locked marker.
        self.assertEqual(campaign_target_decision(locked, labels, dict.fromkeys(roster, "MEASURED"), []), "NOT_CONFIRMATORY")
        capture = SyntheticAdapter(b"fixture").capture(b"settings")
        with self.assertRaises(Incident):
            confirm_acquisition(capture, None)
        with self.assertRaises(Incident):
            confirm_acquisition(Capture("MEASURED", capture.raw_bytes, capture.acquisition_receipt), None)
        with self.assertRaises(Incident):
            retain(capture, None, "test", "1", "Apache-2.0")

    def test_causal_interval_missing_bound_and_initial_equality(self):
        observed, _, _, _ = fixture(True)
        data = ledger()
        data["interval_s"] = ["20", "22"]
        with self.assertRaises(Incident):
            source_origin(observed, data)
        data = ledger()
        data["other_upper_J"]["unresolved"] = None
        self.assertEqual(source_origin(observed, data)["status"], "INDETERMINATE")
        self.assertEqual(source_equality("5", "5", "1/100"), "SATISFIED")
        self.assertEqual(source_equality("5", "51/10", "1/100"), "FAILED")
        self.assertEqual(source_equality("5", "5", None), "INDETERMINATE")

    def test_covariance_is_not_rss_without_correlations(self):
        matrix = [["0" for _ in COMPONENTS] for _ in COMPONENTS]
        matrix[0][0] = matrix[1][1] = "1/1000000"
        model = {"components": list(COMPONENTS), "covariance_J2": matrix, "coverage_factor": "2",
                 "dof": "30", "justification_sha256": "f" * 64}
        uncorrelated = expanded_uncertainty(model)
        matrix[0][1] = matrix[1][0] = "1/1000000"
        self.assertEqual(expanded_uncertainty(model), Fraction(1, 250))
        self.assertGreater(expanded_uncertainty(model), uncorrelated)
        matrix[0][1] = matrix[1][0] = "1/500000"
        with self.assertRaises(Incident):
            expanded_uncertainty(model)
        model.pop("coverage_factor")
        with self.assertRaises(Incident):
            expanded_uncertainty(model)

    def test_gaps_overlaps_and_noncanonical_values(self):
        observed, _, _, _ = fixture()
        series = observed["ports"]["B_2"]
        series[0]["t0_s"] = "1"
        self.assertIsNone(integrate(series, 0, 100))
        series.append(copy.deepcopy(series[0]))
        with self.assertRaises(Incident):
            integrate(series, 1, 100)
        for value in ("NaN", "Infinity", "01", "0/1", "-0", "1.0", True):
            with self.subTest(value=value), self.assertRaises(Incident):
                q(value)

    def test_complete_96_coordinates_and_inverse_tables_are_separate(self):
        names = [f"{r}_{i}" for i in range(3) for r in ("B", "Z", "r")] + ["q0", "q1"]
        expected = [{"index": i, "coordinates": [0] * 96, "counts": dict.fromkeys(names, 0)} for i in range(41)]
        actual = [{"index": i, "coordinates": [0] * 96, "banks": {n: {"energy_J": "0", "U_J": "1/1000", "voltage_V": "5"} for n in names}, "flags": ["SYNTHETIC"]} for i in range(41)]
        self.assertEqual(full_state(actual, expected), "SATISFIED")
        actual[35]["coordinates"][73] = 1
        self.assertEqual(full_state(actual, expected), "FAILED")
        self.assertEqual(full_state(actual[:40], expected), "INDETERMINATE")
        with self.assertRaises(Incident):
            full_state(actual, expected, inverse=True)


if __name__ == "__main__":
    unittest.main()
