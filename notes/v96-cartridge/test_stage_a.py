"""SOFTWARE/SYNTHETIC only. No hardware is connected by these tests."""

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import unittest
from keysight_acquire import FrozenSettings, Keysight34465A
from stage_a import Invalid, calibrated_energy, design_budget, difference_uncertainty, evaluate_hold, number, sqrt_upper


def hold():
    return {"kind": "STAGE_A_HOLD", "origin": "SYNTHETIC", "horizon_s": 200, "level": 41,
            "missing": False, "initial_energy_J": "41/2", "final_energy_J": "2049/100",
            "initial_map_U_J": "1/1000", "final_map_U_J": "1/1000", "minimum_voltage_V": "48", "maximum_voltage_V": "49",
            "voltage_U_V": "1/1000",
            "injection_upper_J": "1/1000", "charger_connected": False, "saturation": False,
            "both_terminals_disconnected": True, "elapsed_s": "200", "time_U_s": "1/1000",
            "read_windows": 81, "probe_on_s": "81/5", "difference_uncertainty": {
                "u0_J": "1/1000", "u1_J": "1/1000", "covariance_J2": "0",
                "coverage_factor": "2", "dof": "30", "unresolved_U_J": "1/1000",
                "justification_sha256": "a" * 64}}


class SyntheticTransport:
    origin = "SYNTHETIC"
    identity = "Keysight Technologies,34465A,SYNTHETIC,FIXTURE"

    def __init__(self):
        self.writes = []
        self.errors = ["+0,No error"]
        self.response = "+5.00000000E-01,+4.99999990E-01"
        self.overrides = {}
        self.fault_command = None

    def write(self, command):
        self.writes.append(command)

    def query(self, command):
        if command == self.fault_command:
            raise OSError("synthetic transport failure")
        if command in self.overrides:
            return self.overrides[command]
        if command == "SYST:ERR?":
            return self.errors.pop(0) if self.errors else "+0,No error"
        return {"*IDN?": self.identity, "TRIG:SOUR?": "EXT", "TRIG:SLOP?": "POS",
                "VOLT:DC:RANG?": "1", "VOLT:DC:NPLC?": "1", "FETC?": self.response,
                "VOLT:DC:RANG:AUTO?": "0", "VOLT:DC:ZERO:AUTO?": "0", "SAMP:COUN?": "+1",
                "TRIG:COUN?": "+2", "SAMP:COUN:PRET?": "+0", "TRIG:DEL?": "+0.000E+00", "TRIG:DEL:AUTO?": "0"}[command]


def device():
    transport = SyntheticTransport()
    settings = FrozenSettings(sha256(transport.identity.encode("ascii")).hexdigest(), "c" * 64, 2)
    metadata = {"specimen": "SYNTHETIC", "dock": "SYNTHETIC", "temperature_C": "23", "history": "charge",
                "protocol_sha256": "d" * 64, "external_trigger_times_s": ["191/100", "197/100"],
                "measurement_complete_times_s": ["193/100", "199/100"],
                "time_U_s": "1/1000", "probe_on_intervals_s": [["9/5", "2"]],
                "both_poles_open_between_windows": True, "acquisition_receipt_sha256": "f" * 64}
    return transport, Keysight34465A(transport, settings), metadata


class StageATests(unittest.TestCase):
    def test_conditional_divider_arithmetic(self):
        self.assertEqual(design_budget(200)["probe_on_s"], "81/5")
        self.assertLess(Fraction(design_budget(200)["divider_upper_J"]), Fraction(1, 2000))
        self.assertGreater(Fraction(design_budget(200)["divider_upper_J"]), Fraction(design_budget(100)["divider_upper_J"]))

    def test_valid_numerical_hold_is_not_qualification(self):
        result = evaluate_hold(hold())
        self.assertEqual(result["status"], "SATISFIED_NUMERICAL_HOLD")
        self.assertEqual(result["qualification"], "NOT_CONFIRMATORY")

    def test_injection_cannot_mask_loss(self):
        record = hold()
        record["final_energy_J"] = record["initial_energy_J"]
        record["injection_upper_J"] = "3/100"
        self.assertEqual(evaluate_hold(record)["status"], "FAILED")

    def test_no_doubled_200s_limit(self):
        record = hold()
        record["final_energy_J"] = "2047/100"
        self.assertEqual(evaluate_hold(record)["status"], "FAILED")

    def test_same_20mJ_limit_at_both_horizons(self):
        for horizon, windows in ((100, 41), (200, 81)):
            record = hold()
            record.update(horizon_s=horizon, elapsed_s=str(horizon), read_windows=windows, probe_on_s=str(Fraction(windows, 5)))
            record["difference_uncertainty"].update(u0_J="0", u1_J="0", covariance_J2="0", unresolved_U_J="0")
            record["injection_upper_J"] = "0"
            record["final_energy_J"] = "512/25"  # Exactly 20 mJ loss.
            self.assertEqual(evaluate_hold(record)["status"], "SATISFIED_NUMERICAL_HOLD")
            record["final_energy_J"] = str(Fraction(41, 2) - Fraction(20001, 1000000))
            self.assertEqual(evaluate_hold(record)["status"], "FAILED")

    def test_no_float_window_or_shorter_probe_exposure(self):
        record = hold()
        record["read_windows"] = 81.0
        with self.assertRaises(Invalid):
            evaluate_hold(record)
        for on_time in ("0", "81/10", "161/10"):
            record = hold()
            record["probe_on_s"] = on_time
            self.assertEqual(evaluate_hold(record)["status"], "FAILED")

    def test_nonfinite_noncanonical_and_unknown_uncertainty_rejected(self):
        for value in ("NaN", "Infinity", "1/0", "0.0", "-0", 0, False, None):
            with self.subTest(value=value), self.assertRaises(Invalid):
                number(value)
        for field in ("u0_J", "u1_J", "coverage_factor", "covariance_J2", "unresolved_U_J", "dof"):
            record = hold()
            record["difference_uncertainty"][field] = None
            with self.subTest(field=field), self.assertRaises(Invalid):
                evaluate_hold(record)
        model = hold()["difference_uncertainty"]
        del model["covariance_J2"]
        with self.assertRaises(Invalid):
            difference_uncertainty(model)

    def test_exact_sqrt_rounds_outward(self):
        for value in (Fraction(0), Fraction(1, 1000000), Fraction(2), Fraction(1, 7)):
            upper = sqrt_upper(value)
            self.assertGreaterEqual(upper * upper, value)
            if upper:
                self.assertLess((upper - Fraction(1, 10**12)) ** 2, value)

    def test_missing_uncertainty(self):
        record = hold()
        record["difference_uncertainty"] = None
        self.assertEqual(evaluate_hold(record)["status"], "INDETERMINATE")

    def test_actual_voltage_bounds_include_uncertainty(self):
        for field, value in (("minimum_voltage_V", "47/10"), ("maximum_voltage_V", "50")):
            record = hold()
            record[field] = value
            result = evaluate_hold(record)
            self.assertEqual(result["status"], "FAILED")
            self.assertIn("VOLTAGE_RANGE", result["faults"])
        record = hold()
        record["voltage_U_V"] = None
        self.assertEqual(evaluate_hold(record)["status"], "INDETERMINATE")

    def test_charging_timing_duty_and_saturation(self):
        for field, value in (("charger_connected", True), ("saturation", True), ("both_terminals_disconnected", False),
                             ("elapsed_s", "201"), ("read_windows", 80), ("probe_on_s", "17")):
            record = hold()
            record[field] = value
            with self.subTest(field=field):
                self.assertEqual(evaluate_hold(record)["status"], "FAILED")

    def test_difference_covariance(self):
        model = hold()["difference_uncertainty"]
        independent = difference_uncertainty(model)
        model["covariance_J2"] = "1/1000000"
        self.assertLess(difference_uncertainty(model), independent)
        model["covariance_J2"] = "1/500000"
        with self.assertRaises(Invalid):
            difference_uncertainty(model)

    def test_energy_map_requires_correct_history_and_no_extrapolation(self):
        calibration = {"kind": "MEASURED_ENERGY_MAP", "origin": "SYNTHETIC", "specimen": "S", "dock": "D",
                       "temperature_C": "23", "history": "charge", "protocol_sha256": "a" * 64,
                       "interpolation_U_J": "1/1000", "knots": [
                           {"voltage_V": "5", "energy_inc_J": "0", "U_J": "1/1000"},
                           {"voltage_V": "6", "energy_inc_J": "1/10", "U_J": "1/1000"}]}
        def evaluate(voltage="11/2", history="charge"):
            return calibrated_energy(calibration, "S", "D", "23", history, "a" * 64, voltage)
        self.assertEqual(evaluate()["energy_inc_J"], "1/20")
        for voltage, history in (("7", "charge"), ("11/2", "discharge")):
            with self.assertRaises(Invalid):
                evaluate(voltage, history)
        calibration["kind"] = "NOMINAL_CV2"
        with self.assertRaises(Invalid):
            evaluate()

    def test_real_scpi_commands_synthetic_transport(self):
        transport, adapter, metadata = device()
        adapter.arm()
        result = adapter.fetch(metadata)
        self.assertEqual(result["origin"], "SYNTHETIC")
        self.assertEqual(result["voltage_V"][0], "1/2")
        self.assertIn("TRIG:SOUR EXT", transport.writes)
        self.assertIn("INIT", transport.writes)
        self.assertFalse(any("OUTP" in command for command in transport.writes))

    def test_transport_origin_cannot_be_promoted_after_arm(self):
        transport, adapter, metadata = device()
        adapter.arm()
        transport.origin = "MEASURED"
        with self.assertRaisesRegex(Invalid, "provenance"):
            adapter.fetch(metadata)
        self.assertFalse(adapter.armed)

    def test_failed_rearm_consumes_admission(self):
        transport, adapter, metadata = device()
        adapter.arm()
        transport.identity = transport.identity.replace("34465A", "34461A")
        with self.assertRaises(Invalid):
            adapter.arm()
        self.assertFalse(adapter.armed)
        with self.assertRaises(Invalid):
            adapter.fetch(metadata)

    def test_missing_probe_disconnection_and_capture_timing_rejected(self):
        for field, value in (("both_poles_open_between_windows", False), ("both_poles_open_between_windows", "true"),
                             ("probe_on_intervals_s", []), ("probe_on_intervals_s", [["9/5", "21/10"]]),
                             ("external_trigger_times_s", ["37/20", "197/100"]),
                             ("measurement_complete_times_s", ["193/100", "201/100"]),
                             ("measurement_complete_times_s", []), ("time_U_s", "1/100")):
            _, adapter, metadata = device()
            adapter.arm()
            metadata[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(Invalid):
                adapter.fetch(metadata)
            self.assertFalse(adapter.armed)

    def test_capture_metadata_snapshot_is_not_caller_alias(self):
        _, adapter, metadata = device()
        adapter.arm()
        captured = adapter.fetch(metadata)
        metadata["specimen"] = "changed"
        metadata["external_trigger_times_s"].clear()
        self.assertEqual(captured["metadata"]["specimen"], "SYNTHETIC")
        self.assertEqual(len(captured["metadata"]["external_trigger_times_s"]), 2)

    def test_ten_plc_rejected_for_original_read_window(self):
        transport, adapter, _ = device()
        settings = FrozenSettings(adapter.settings.idn_sha256, adapter.settings.calibration_sha256, 2, nplc="10")
        with self.assertRaisesRegex(Invalid, "100 ms"):
            Keysight34465A(transport, settings)

    def test_ignored_instrument_settings_do_not_arm(self):
        for query, value in (("SAMP:COUN?", "2"), ("TRIG:COUN?", "1"), ("VOLT:DC:ZERO:AUTO?", "1"),
                             ("VOLT:DC:RANG:AUTO?", "1"), ("TRIG:DEL?", ".1"),
                             ("TRIG:DEL:AUTO?", "1"), ("SAMP:COUN:PRET?", "1"), ("VOLT:DC:NPLC?", "NaN")):
            transport, adapter, _ = device()
            transport.overrides[query] = value
            with self.subTest(query=query), self.assertRaises(Invalid):
                adapter.arm()
            self.assertFalse(adapter.armed)

    def test_initiation_fetch_errors_and_transport_timeout_fail_closed(self):
        transport, adapter, metadata = device()
        transport.errors = ["+0,No error", "+0,No error", "-100,INIT error"]
        with self.assertRaises(Invalid):
            adapter.arm()
        self.assertFalse(adapter.armed)
        transport, adapter, metadata = device()
        adapter.arm()
        transport.errors = ["-100,Fetch error"]
        with self.assertRaises(Invalid):
            adapter.fetch(metadata)
        self.assertFalse(adapter.armed)
        transport, adapter, metadata = device()
        adapter.arm()
        transport.fault_command = "FETC?"
        with self.assertRaises(OSError):
            adapter.fetch(metadata)
        self.assertFalse(adapter.armed)

    def test_failed_and_indeterminate_cli_exit_nonzero(self):
        script = Path(__file__).with_name("stage_a.py")
        for field, value, expected in (("charger_connected", True, 2), ("difference_uncertainty", None, 3)):
            record = hold()
            record[field] = value
            result = subprocess.run([sys.executable, "-B", str(script), "--hold", "-"],
                                    input=json.dumps(record), capture_output=True, text=True)
            self.assertEqual(result.returncode, expected)
            self.assertNotEqual(json.loads(result.stdout)["status"], "SATISFIED_NUMERICAL_HOLD")

    def test_identity_and_existing_error_fail_before_configuration(self):
        transport, adapter, _ = device()
        transport.identity = transport.identity.replace("34465A", "34461A")
        with self.assertRaises(Invalid):
            adapter.arm()
        self.assertEqual(transport.writes, [])
        transport, adapter, _ = device()
        transport.errors = ["-100,Error", "+0,No error"]
        with self.assertRaises(Invalid):
            adapter.arm()
        self.assertEqual(transport.writes, [])

    def test_overload_missing_and_bad_timestamps(self):
        for response in ("9.9E37,1", "NaN,1", "1"):
            transport, adapter, metadata = device()
            transport.response = response
            adapter.arm()
            with self.assertRaises(Invalid):
                adapter.fetch(metadata)
            self.assertFalse(adapter.armed)
        _, adapter, metadata = device()
        adapter.arm()
        metadata["external_trigger_times_s"] = ["2", "1"]
        with self.assertRaises(Invalid):
            adapter.fetch(metadata)


if __name__ == "__main__":
    unittest.main()
