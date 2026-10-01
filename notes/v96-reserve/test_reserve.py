"""Exact SOFTWARE development regressions; these are not a formal gate."""

from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
import unittest

import certify as c


class ReserveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = c.load_model(c.HERE / "budgets-v1.json")
        cls.law = c.load_law()

    def engine(self):
        return c.Certifier(deepcopy(self.model), "positive", "forward100")

    def test_known_dec_counterexample_exact(self):
        result = c.counterexample()
        self.assertEqual(Q(result["input_sum_J"]), Q("9.560"))
        self.assertEqual(Q(result["required_B_J"]), Q("9.780"))
        self.assertEqual(Q(result["shortfall_J"]), Q(".220"))

    def test_zero_sum_support_against_all_six_vertices(self):
        engine = self.engine()
        xi = engine.residuals("residual")
        for weights in product(range(-2, 3), repeat=3):
            expression = sum((a * b for a, b in zip(weights, xi)), c.Affine())
            values = [sum(a * b for a, b in zip(weights, vertex)) for vertex in
                      ((1, 0, -1), (1, -1, 0), (0, 1, -1), (0, -1, 1), (-1, 1, 0), (-1, 0, 1))]
            self.assertEqual(expression.bound(engine.groups).value(engine.budgets), max(values) * engine.budgets["equalization_residual"])
            self.assertEqual(expression.bound(engine.groups, False).value(engine.budgets), min(values) * engine.budgets["equalization_residual"])
        total = sum(xi, c.Affine())
        self.assertEqual(total.bound(engine.groups).value(engine.budgets), 0)
        self.assertEqual(total.bound(engine.groups, False).value(engine.budgets), 0)

    def test_gate_deficit_identity_and_zero_account_baseline_droop(self):
        engine = self.engine()
        before = [c.Affine(9), c.Affine(0), c.Affine(1)]
        after = engine.redistribute(before, (18, 0, 2), (20, 0, 0), 2, True)
        total_loss = sum(before, c.Affine()) - sum(after, c.Affine())
        deficit = c.Affine(10) - after[0]
        # d'_B = (20/20)(sum d + L) - xi_B, with sum d=0.
        xi = engine.residuals("independent_only_for_shape")
        self.assertEqual((deficit - total_loss).bound(engine.groups).value(engine.budgets), engine.budgets["equalization_residual"])
        self.assertLess(after[1].bound(engine.groups, False).value(engine.budgets), 0)
        self.assertEqual(after[1].bound(engine.groups).value(engine.budgets), engine.budgets["equalization_residual"])
        self.assertEqual(sum(xi, c.Affine()).bound(engine.groups).value(engine.budgets), 0)

    def test_zero_sum_and_rejected_inputs_never_divide(self):
        engine = self.engine()
        zero = [c.Affine(), c.Affine(), c.Affine()]
        self.assertEqual(engine.redistribute(zero, (0, 0, 0), (0, 0, 0), 1, False), zero)
        with self.assertRaisesRegex(ValueError, "S=0"):
            engine.redistribute(zero, (0, 0, 0), (0, 0, 0), 1, True)
        with self.assertRaisesRegex(ValueError, "preserve"):
            engine.redistribute(zero, (0, 0, 0), (1, 0, 0), 1, True)

    def test_initial_preparation_is_nonempty_and_contains_exact_counts(self):
        engine = self.engine()
        initial = self.law.initial(3, self.law.local().W)
        counts = c.bank_counts(initial, self.law)
        self.assertEqual(len(counts), 11)
        self.assertEqual(sum(counts), 41)
        rows = engine.snapshot([c.Affine(Q(n, 2)) for n in counts], counts)
        self.assertIsNone(engine.first_violation)
        for row in rows:
            self.assertEqual(tuple(map(Q, row["increment_J"])), (Q(row["count"], 2),) * 2)

    def test_injection_cannot_mask_idle_dissipation(self):
        model = deepcopy(self.model)
        model["budgets_J"]["idle_per_second"] = "1/100"
        model["budgets_J"]["read_injection"] = "1/10"
        engine = c.Certifier(model, "offimage", "forward100")
        initial, trace = c.declared_trace(self.law, "offimage", "forward100", self.law.local().W)
        result = engine.certify(self.law, initial, trace[:1])
        self.assertEqual(result["status"], "NOT_CERTIFIED")
        idle = next(v for v in result["constraints"] if v["quantity"] == "per_serial_idle_dissipation")
        self.assertLess(Q(idle["margin"]), 0)
        self.assertNotIn("read_injection", idle["lhs"]["terms"])

    def test_first_failed_bank_has_exact_reproducible_corner(self):
        model = deepcopy(self.model)
        model["budgets_J"]["conversion_dissipation"] = "1"
        engine = c.Certifier(model, "positive", "forward100")
        initial, trace = c.declared_trace(self.law, "positive", "forward100", self.law.local().W)
        result = engine.certify(self.law, initial, trace[:1])
        failure = result["first_violation"]
        self.assertEqual(result["status"], "NOT_CERTIFIED")
        self.assertEqual(failure["operation"], "step1:forward:G")
        self.assertIn("witness", failure)
        self.assertLess(Q(failure["margin"]), 0)
        self.assertTrue(failure["witness"]["uncertainty_corner"])

    def test_deadline_is_an_explicit_unsatisfied_condition(self):
        model = deepcopy(self.model)
        model["conditional_operation_contract"]["G_duration_upper_s"] = "2"
        engine = c.Certifier(model, "positive", "forward100")
        engine.contract()
        self.assertEqual(engine.first_violation["quantity"], "G_duration_upper_s")
        self.assertEqual(Q(engine.first_violation["margin"]), Q("-.3"))

    def test_nonzero_ready_auxiliary_cannot_be_hidden(self):
        model = deepcopy(self.model)
        model["conditional_operation_contract"]["auxiliary_READY_J"] = "1/100"
        engine = c.Certifier(model, "positive", "forward100")
        with self.assertRaisesRegex(ValueError, "READY"):
            engine.contract()

    def test_true_energy_enclosure_covers_adversarial_meter_error(self):
        engine = self.engine()
        energy = c.Affine(Q(".001"))
        engine.snapshot([energy] * 11, (0,) * 11)
        row = next(v for v in engine.constraints if v["quantity"] == "B0:positive_error")
        meter_error = engine.budgets["energy_uncertainty"]
        worst_observed_acceptance = Q(".001") + meter_error + meter_error
        self.assertEqual(Q(row["value"]), worst_observed_acceptance)

    def test_work_origin_is_stricter_than_target_lower_bound(self):
        # Here these are measured values, so the frozen predicate subtracts U once.
        measured, uncertainty, other = Q(".960"), Q(".010"), Q(".010")
        self.assertGreaterEqual(measured - uncertainty, Q(".950"))
        self.assertLess(measured - uncertainty - other, Q(".950"))

    def test_idle_hold_near_20mJ_fails_with_difference_uncertainty(self):
        model = deepcopy(self.model)
        model["budgets_J"]["idle_per_second"] = "19/200000"
        model["budgets_J"]["read_dissipation"] = "0"
        engine = c.Certifier(model, "offimage", "forward_inverse200")
        # 19 mJ of true loss is below 20 mJ, but a possible 1 mJ estimate
        # error plus the acceptance predicate's own 1 mJ gives 21 mJ.
        engine.location, engine.time = "idle_200s", Q(200)
        lhs = c.parameter("idle_per_second", 200) + c.parameter("idle_difference_uncertainty", 2)
        engine.require("per_serial_idle_dissipation", lhs, ".020")
        self.assertEqual(Q(engine.first_violation["value"]), Q(".021"))
        self.assertEqual(Q(engine.first_violation["margin"]), Q("-.001"))

    def test_cut0_repeated_reactions_accumulate_all_startups(self):
        initial, trace = c.declared_trace(self.law, "cut0", "forward100", self.law.local().W)
        engine = c.Certifier(deepcopy(self.model), "cut0", "forward100")
        result = engine.certify(self.law, initial, trace)
        self.assertEqual(result["accepted_G"], 10)
        self.assertEqual(result["auxiliary_starts_upper"], 320)
        self.assertEqual(result["status"], "CONDITIONAL")
        self.assertGreater(Q(result["layers"][-1]["gross_dissipation_upper_J"]), Q(".01"))
        self.assertEqual(result["layers"][-1]["positive_uncontrolled_injection_upper_J"], "0")

    def test_non_G_absolute_work_cannot_disappear_from_100s_bound(self):
        model = deepcopy(self.model)
        model["budgets_J"]["negative_abs_work_per_G"] = "0"
        # Zero net out-and-back work can leave every endpoint unchanged while
        # violating the absolute-work bound during the non-G intervals.
        model["budgets_J"]["negative_abs_work_outside_G_per_macrostep"] = "21/10000"
        for mode in ("forward100", "inverse_forward200"):
            initial, trace = c.declared_trace(self.law, "offimage", mode, self.law.local().W)
            engine = c.Certifier(deepcopy(model), "offimage", mode)
            result = engine.certify(self.law, initial, trace)
            self.assertEqual(result["encoding_status"], "CONDITIONAL")
            self.assertEqual(result["work_status"], "NOT_CERTIFIED")
            blocks = [v for v in result["constraints"]
                      if v["quantity"] == "negative_target_abs_work_100s_block"
                      and Q(v["time_s"]) % 100 == 0]
            self.assertEqual(len(blocks), 1 if mode == "forward100" else 2)
            for row in blocks:
                self.assertEqual(Q(row["value"]), Q(".021"))
                self.assertEqual(Q(row["margin"]), Q("-.001"))

    def test_swap_endpoint_difference_includes_idle_and_read_window(self):
        model = deepcopy(self.model)
        model["budgets_J"]["swap_dissipation"] = "2998/1000000"
        engine = c.Certifier(model, "positive", "forward100")
        engine.contract()
        # Contact-only loss plus 2U is 4.998 mJ, but its complete 2.5 s slot
        # plus the read window reaches 5.0015 mJ without an injection credit.
        self.assertEqual(engine.first_violation["quantity"], "swap_absolute_disturbance")
        self.assertEqual(Q(engine.first_violation["value"]), Q(".0050015"))
        self.assertEqual(Q(engine.first_violation["margin"]), Q("-.0000015"))

    def test_both_inverse_orders_return_all_96_words(self):
        for configuration, mode in product(("positive", "offimage", "cut0", "cut1"),
                                            ("forward_inverse200", "inverse_forward200")):
            initial, trace = c.declared_trace(self.law, configuration, mode, self.law.local().W)
            self.assertEqual(trace[-1][-1], initial)
            self.assertEqual(len(self.law.flatten(trace[-1][-1], 3)), 96)
            self.assertEqual(len(trace), 80)

    def test_exact_budget_maximum_is_binding_and_next_fraction_fails(self):
        budgets = {"loss": Q(1)}
        constraints = [{"scope": "encoding", "lhs": {"constant": "2", "terms": {"loss": "3"}},
                        "value": "5", "upper": "8"}]
        # Exercise the public maximum routine with its closed category set.
        all_budgets = {name: Q(0) for name in c.KINDS}
        all_budgets["conversion_dissipation"] = budgets["loss"]
        constraints[0]["lhs"]["terms"] = {"conversion_dissipation": "3"}
        answer = c.maximum_budgets([{"constraints": constraints}], all_budgets, False)
        maximum = Q(answer["conversion_dissipation"]["maximum"])
        self.assertEqual(maximum, 2)
        self.assertEqual(2 + 3 * maximum, 8)
        self.assertGreater(2 + 3 * (maximum + Q(1, 1000)), 8)


if __name__ == "__main__":
    unittest.main()
