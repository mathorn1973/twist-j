#!/usr/bin/env python3
"""NON-CANONICAL development certifier for a conditional finite energy relation.

Python 3.12 standard library. No instrument interface, scientific gate, or
physical qualification. All decisions and reported bounds use Fraction.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from types import ModuleType


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NAMES = tuple(v for i in range(3) for v in (f"B{i}", f"Z{i}", f"r{i}")) + ("q0", "q1")
KINDS = (
    "prepare idle_per_second read_dissipation read_injection swap_dissipation "
    "swap_injection conversion_dissipation auxiliary_startup current_tail "
    "switching_dissipation equalization_residual transient_sag transient_overshoot "
    "target_bank_heat other_unresolved_upper energy_uncertainty idle_difference_uncertainty "
    "source_equality_uncertainty work_uncertainty swap_uncertainty "
    "control_resolution negative_abs_work_per_G negative_abs_work_outside_G_per_macrostep"
).split()
PRIMARY_SHA = "11009d50a61a6e158aeffd9f1fde5bd867ccfb286b38029f985774d9155eb705"
LOCAL_SHA = "42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59"
LAW_PIN = "312d0a90b24d5f9e743096f0ee2a477cda719a10"
DESIGN_PIN = "4756a3df650b91fb1d30806b0fb2aaac00e50cc2"


@dataclass
class Linear:
    constant: Q
    terms: dict

    def __add__(self, other):
        if not isinstance(other, Linear):
            other = Linear(Q(other), {})
        terms = dict(self.terms)
        for k, v in other.terms.items():
            terms[k] = terms.get(k, Q(0)) + v
        return Linear(self.constant + other.constant, {k: v for k, v in terms.items() if v})

    __radd__ = __add__

    def __neg__(self):
        return Linear(-self.constant, {k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Linear) else -Q(other))

    def value(self, budgets):
        return self.constant + sum((v * budgets[k] for k, v in self.terms.items()), Q(0))

    def record(self):
        return {"constant": str(self.constant), "terms": {k: str(v) for k, v in sorted(self.terms.items())}}


def parameter(name, factor=1):
    return Linear(Q(0), {name: Q(factor)})


class Affine:
    """Affine form over independent scalar boxes or sum-zero hexagons."""

    def __init__(self, constant=0, terms=None):
        self.constant = Q(constant)
        self.terms = terms or {}
        self._bounds = {}

    def __add__(self, other):
        if not isinstance(other, Affine):
            other = Affine(other)
        terms = dict(self.terms)
        for key, values in other.terms.items():
            old = terms.get(key, (Q(0),) * len(values))
            row = tuple(a + b for a, b in zip(old, values))
            if any(row):
                terms[key] = row
            else:
                terms.pop(key, None)
        return Affine(self.constant + other.constant, terms)

    __radd__ = __add__

    def __mul__(self, scalar):
        scalar = Q(scalar)
        return Affine(self.constant * scalar, {k: tuple(scalar * x for x in v) for k, v in self.terms.items()} if scalar else {})

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other if isinstance(other, Affine) else -Q(other))

    def bound(self, groups, upper=True):
        if upper in self._bounds:
            return self._bounds[upper]
        terms = {}
        for key, values in self.terms.items():
            kind, shape = groups[key]
            if shape == "loss":
                support = max(values[0], Q(0)) if upper else min(values[0], Q(0))
            elif shape == "signed":
                support = abs(values[0]) * (1 if upper else -1)
            elif shape == "zero_sum":
                support = (max(values) - min(values)) * (1 if upper else -1)
            else:
                raise ValueError("unknown uncertainty set")
            terms[kind] = terms.get(kind, Q(0)) + support
        result = Linear(self.constant, {k: v for k, v in terms.items() if v})
        self._bounds[upper] = result
        return result

    def witness(self, groups, budgets, upper=True):
        """An exact attainable corner of the declared affine uncertainty set."""
        result, value = {}, self.constant
        for key, row in self.terms.items():
            kind, shape = groups[key]
            sign = 1 if upper else -1
            if shape == "loss":
                corner = (Q(int(sign * row[0] > 0)),)
            elif shape == "signed":
                corner = (Q(sign if row[0] >= 0 else -sign),)
            else:
                corners = ((Q(a), Q(b), Q(c)) for a, b, c in
                           ((1, 0, -1), (1, -1, 0), (0, 1, -1), (0, -1, 1), (-1, 1, 0), (-1, 0, 1)))
                corner = max(corners, key=lambda v: sign * sum(a * b for a, b in zip(v, row)))
            values = tuple(x * budgets[kind] for x in corner)
            value += sum(a * b for a, b in zip(values, row))
            result[key] = {"kind": kind, "values_J": list(map(str, values))}
        assert value == self.bound(groups, upper).value(budgets)
        return {"value_J": str(value), "uncertainty_corner": result}


def load_model(path):
    model = json.loads(Path(path).read_text(encoding="utf-8"))
    if model.get("schema") != "twistj-reserve-budget/1":
        raise ValueError("unsupported budget schema")
    if model.get("provenance") != "HYPOTHETICAL_ENGINEERING_INPUT_NOT_MEASURED" or model.get("qualification") != "UNQUALIFIED":
        raise ValueError("this development tool cannot promote inputs to qualification")
    if model.get("law_pin") != LAW_PIN or model.get("design_pin") != DESIGN_PIN:
        raise ValueError("source pin mismatch")
    if set(model["budgets_J"]) != set(KINDS):
        raise ValueError("missing or unknown budget categories")
    for value in model["budgets_J"].values():
        if not isinstance(value, str) or Q(value) < 0:
            raise ValueError("budgets must be nonnegative exact rational strings")
    return model


def load_law():
    path = ROOT / "notes/C-FIELD-WORK-RECORD-UNIT-N/primary.py"
    data = path.read_bytes()
    if sha256(data).hexdigest() != PRIMARY_SHA:
        raise ValueError("pinned #1316 implementation hash mismatch")
    module = ModuleType("declared_work_record_law")
    module.__file__ = str(path)
    exec(compile(data, str(path), "exec"), module.__dict__)
    module.local()  # Independently checks the inherited #1310 local hash.
    return module


def bank_counts(state, law):
    p = law.local()
    cells, channels, _ = state
    result = []
    for m, b, z, r in cells:
        result += [sum(p.matter_energy(v) for v in m + b), p.raw_energy(z), r]
    return tuple(result) + tuple(channels)


def declared_trace(law, configuration, mode, seed):
    cut = {"positive": None, "offimage": None, "cut0": 0, "cut1": 1}[configuration]
    initial = law.initial(3, seed, offimage=configuration == "offimage")
    directions = {"forward100": (False,) * 10,
                  "forward_inverse200": (False,) * 10 + (True,) * 10,
                  "inverse_forward200": (True,) * 10 + (False,) * 10}[mode]
    state = initial
    result = []
    for step, inverse in enumerate(directions, 1):
        for kind, post in law.layers(state, 3, cut, inverse):
            result.append((step, inverse, kind, state, post))
            state = post
    if len(directions) == 20 and state != initial:
        raise ValueError("declared full-state inverse identity failed")
    return initial, result


class Certifier:
    def __init__(self, model, configuration, mode):
        self.model = model
        self.budgets = {k: Q(v) for k, v in model["budgets_J"].items()}
        self.configuration, self.mode = configuration, mode
        self.groups, self.constraints, self.layers = {}, [], []
        self.time = Q(0)
        self.location = "preparation"
        self.first_violation = None
        self.injection_upper = Linear(Q(0), {})
        self.gross_heat_upper = Linear(Q(0), {})
        self.bank_heat = Affine()
        self.bank_injection = Affine()
        self.auxiliary_starts = 0
        self.accepted_gates = 0
        self.serials = list(NAMES)
        self.events = []

    def variable(self, label, kind, shape="loss", factor=1):
        key = f"{self.location}:{label}"
        if key in self.groups:
            raise ValueError("uncertainty identity reused")
        self.groups[key] = kind, shape
        return Affine(0, {key: (Q(factor),)})

    def residuals(self, label):
        key = f"{self.location}:{label}"
        if key in self.groups:
            raise ValueError("uncertainty identity reused")
        self.groups[key] = "equalization_residual", "zero_sum"
        return [Affine(0, {key: tuple(Q(int(i == j)) for j in range(3))}) for i in range(3)]

    def require(self, label, lhs, upper, scope="encoding", expression=None, direction=True):
        upper = Q(upper)
        value = lhs.value(self.budgets)
        item = {"time_s": str(self.time), "operation": self.location,
                "configuration": self.configuration, "mode": self.mode,
                "quantity": label, "scope": scope, "lhs": lhs.record(),
                "upper": str(upper), "value": str(value), "margin": str(upper - value)}
        self.constraints.append(item)
        if value > upper and self.first_violation is None:
            self.first_violation = dict(item)
            self.first_violation["meaning"] = "Declared envelope cannot certify this bound; a physical failure is not inferred."
            if expression is not None:
                self.first_violation["witness"] = expression.witness(self.groups, self.budgets, direction)

    def contract(self):
        p = parameter
        for name, bound in (("energy_uncertainty", Q(".020")), ("work_uncertainty", Q(".010")),
                            ("equalization_residual", Q(".005")), ("control_resolution", Q(".001"))):
            self.require(name, p(name), bound)
        self.require("source_preparation_equality", p("prepare", 6) + p("source_equality_uncertainty", 2), ".010", "work")
        # Compare the same physical serial before/after the complete A/B slot.
        # The frozen predicate does not subtract a fitted passive/read drift.
        self.require("swap_absolute_disturbance", p("swap_dissipation") + p("swap_injection")
                     + p("idle_per_second", Q("2.5")) + p("read_dissipation")
                     + p("read_injection") + p("swap_uncertainty", 2), ".005")
        contract = self.model["conditional_operation_contract"]
        for key in ("no_commanded_baseline_withdrawal", "transient_energy_inside_endpoint_hull_plus_bounds",
                    "donor_startup_metered_and_fully_reset", "no_external_replenishment", "no_hidden_auxiliary_path"):
            if contract.get(key) is not True:
                raise ValueError("missing conditional operation assumption: " + key)
        if Q(contract["auxiliary_READY_J"]) != 0:
            raise ValueError("nonzero READY auxiliary storage needs a new declared relation")
        transfers = contract["G_transfers_max"]
        if type(transfers) is not int or not 1 <= transfers <= 32:
            raise ValueError("G transfer limit must be an integer in 1..32")
        for key, bound in (("G_duration_upper_s", "1.7"), ("swap_duration_upper_s", "2.2"),
                           ("F_duration_upper_s", ".1"), ("timestamp_uncertainty_s", ".001")):
            actual = Q(contract[key])
            if actual < 0:
                raise ValueError("negative operation duration")
            self.require(key, Linear(actual, {}), bound)

    def snapshot(self, energies, counts, previous=None):
        rows = []
        low = Q(self.model["conditional_energy_map"]["increment_at_4_7V_upper_J"])
        high = Q(self.model["conditional_energy_map"]["increment_at_50V_lower_J"])
        base_low, base_high = map(Q, self.model["conditional_energy_map"]["baseline_J"])
        if not base_low <= base_high or not low < 0 < high or base_low + low <= 0:
            raise ValueError("invalid conditional calibration enclosure")
        for j, (energy, count) in enumerate(zip(energies, counts)):
            if type(count) is not int or not 0 <= count <= 41:
                raise ValueError("bank count outside declared shell")
            lo, hi = energy.bound(self.groups, False), energy.bound(self.groups)
            tolerance = Q(".020") if self.location == "preparation" else Q(".240")
            # The affine form encloses true energy. A possible meter estimate
            # differs by U; the frozen acceptance adds another U to that estimate.
            self.require(NAMES[j] + ":positive_error", hi - Q(count, 2) + parameter("energy_uncertainty", 2), tolerance, expression=energy)
            self.require(NAMES[j] + ":negative_error", -lo + Q(count, 2) + parameter("energy_uncertainty", 2), tolerance, expression=energy, direction=False)
            self.require(NAMES[j] + ":voltage_floor", -lo, -low, expression=energy, direction=False)
            self.require(NAMES[j] + ":voltage_ceiling", hi, high, expression=energy)
            if previous is not None:
                for label, endpoint in (("before", previous[j]), ("after", energy)):
                    self.require(NAMES[j] + ":transient_floor_" + label,
                                 -endpoint.bound(self.groups, False) + parameter("transient_sag"), -low,
                                 expression=endpoint, direction=False)
                    self.require(NAMES[j] + ":transient_ceiling_" + label,
                                 endpoint.bound(self.groups) + parameter("transient_overshoot"), high, expression=endpoint)
            rows.append({"bank": NAMES[j], "serial": self.serials[j], "count": count,
                         "increment_J": [str(lo.value(self.budgets)), str(hi.value(self.budgets))],
                         "absolute_stored_J": [str(lo.value(self.budgets) + base_low), str(hi.value(self.budgets) + base_high)],
                         "lower_certificate": lo.record(), "upper_certificate": hi.record()})
        return rows

    def redistribute(self, energies, old_counts, new_counts, cell, accepted):
        if sum(old_counts) != sum(new_counts):
            raise ValueError("G must preserve the exact local count sum")
        if not accepted:
            if tuple(old_counts) != tuple(new_counts):
                raise ValueError("rejected G changed counts")
            self.events.append({"cell": cell, "action": "rejected_identity", "S": sum(new_counts)})
            return list(energies)
        total_count = sum(new_counts)
        if total_count == 0:
            raise ValueError("accepted G with S=0 is impossible for the pinned reaction endpoints; no division performed")
        number = self.model["conditional_operation_contract"]["G_transfers_max"]
        loss = Affine()
        for kind, factor in (("conversion_dissipation", 1), ("auxiliary_startup", number),
                             ("current_tail", number), ("switching_dissipation", number)):
            loss += self.variable(f"G{cell}:{kind}", kind, factor=factor)
            self.gross_heat_upper += parameter(kind, factor)
        remaining = sum(energies, Affine()) - loss
        self.bank_heat += loss
        residual = self.residuals(f"G{cell}:xi")
        post = [remaining * Q(n, total_count) + xi for n, xi in zip(new_counts, residual)]
        assert (sum(post, Affine()) - remaining).bound(self.groups).constant == 0
        assert not (sum(post, Affine()) - remaining).bound(self.groups).terms
        self.accepted_gates += 1
        self.auxiliary_starts += number
        self.events.append({"cell": cell, "action": "accepted_proportional_relation", "S": total_count,
                            "auxiliary_starts_upper": number, "each_start_draw_J": ["0", str(self.budgets["auxiliary_startup"])],
                            "auxiliary_peak_J": ["0", str(self.budgets["auxiliary_startup"])],
                            "auxiliary_READY_before_after_J": ["0", "0"],
                            "each_reset": "metered dissipation of that start's draw; no buffer carried to another donor",
                            "gross_dissipation_upper_J": str(loss.bound(self.groups).value(self.budgets)),
                            "xi_sum_J": "0"})
        return post

    def certify(self, law, initial, trace):
        self.contract()
        counts = bank_counts(initial, law)
        if sum(counts) != 41:
            raise ValueError("not the declared H3=41 preparations")
        energies = [Affine(Q(n, 2)) + self.variable(name, "prepare", "signed") for name, n in zip(NAMES, counts)]
        self.layers.append({"time_s": "0", "layer": "preparation", "banks": self.snapshot(energies, counts),
                            "auxiliaries_READY_J": {f"converter{i}": "0" for i in range(3)}})
        initial_total = sum(energies, Affine())
        negative_gates = 0
        reads = 0
        for step, inverse, kind, state, post_state in trace:
            self.location = f"step{step}:{'inverse' if inverse else 'forward'}:{kind}"
            self.events = []
            previous = list(energies)
            before_counts, after_counts = bank_counts(state, law), bank_counts(post_state, law)
            duration = {"G": Q(2), "A": Q("2.5"), "B": Q("2.5"), "F": Q(3)}[kind]
            if kind == "G":
                for i in range(3):
                    indices = slice(3 * i, 3 * i + 3)
                    accepted = state[0][i] != post_state[0][i]
                    energies[indices] = self.redistribute(energies[indices], before_counts[indices], after_counts[indices], i, accepted)
            elif kind in ("A", "B"):
                cut = {"positive": None, "offimage": None, "cut0": 0, "cut1": 1}[self.configuration]
                for j in range(2):
                    if j == cut:
                        self.events.append({"contact": f"{kind}{j}", "action": "physically_cut_identity"})
                        continue
                    a, b = (3 * (j if kind == "A" else j + 1) + 2), 9 + j
                    energies[a], energies[b] = energies[b], energies[a]
                    self.serials[a], self.serials[b] = self.serials[b], self.serials[a]
                    for index in (a, b):
                        disturbance_loss = self.variable(f"swap:{NAMES[index]}:loss", "swap_dissipation")
                        disturbance_injection = self.variable(f"swap:{NAMES[index]}:injection", "swap_injection", "signed")
                        energies[index] += disturbance_injection - disturbance_loss
                        self.bank_heat += disturbance_loss
                        self.bank_injection += disturbance_injection
                        self.gross_heat_upper += parameter("swap_dissipation")
                        self.injection_upper += parameter("swap_injection")
                    self.events.append({"contact": f"{kind}{j}", "action": "whole_cartridge_swap", "banks": [NAMES[a], NAMES[b]]})
            removed, injected = [], []
            for j in range(11):
                drain = self.variable(f"{NAMES[j]}:idle", "idle_per_second", factor=duration)
                drain += self.variable(f"{NAMES[j]}:read", "read_dissipation")
                injection = self.variable(f"{NAMES[j]}:probe_injection", "read_injection", "signed")
                energies[j] += injection - drain
                self.bank_heat += drain
                self.bank_injection += injection
                removed.append(drain)
                injected.append(injection)
            self.gross_heat_upper += parameter("idle_per_second", 11 * duration) + parameter("read_dissipation", 11)
            self.injection_upper += parameter("read_injection", 11)
            self.time += duration
            reads += 1
            self.require("per_serial_idle_dissipation", parameter("idle_per_second", self.time) + parameter("read_dissipation", reads)
                         + parameter("idle_difference_uncertainty", 2), ".020")
            if kind == "G" and self.configuration == "positive" and self.mode != "inverse_forward200" and step == 3:
                # Signed B2 terminal work over the entire G slot: storage change
                # plus local dissipation, minus non-port probe injection.
                work = energies[6] - previous[6] + removed[6] - injected[6]
                work += self.variable("B2:internal_heat", "target_bank_heat")
                lower, upper = work.bound(self.groups, False), work.bound(self.groups)
                other = parameter("prepare", 6) + parameter("other_unresolved_upper") + self.injection_upper
                self.require("first_work_lower", -lower + parameter("work_uncertainty", 2), "-.950", "work", work, False)
                self.require("first_work_upper", upper + parameter("work_uncertainty", 2), "1.050", "work", work)
                self.require("first_work_other_energy", other, ".010", "work")
                self.require("first_work_source_attributable", -lower + parameter("work_uncertainty", 2) + other, "-.950", "work", work, False)
                self.events.append({"action": "separate_first_work_test", "net_signed_work_J": [str(lower.value(self.budgets)), str(upper.value(self.budgets))],
                                    "other_upper_J": str(other.value(self.budgets)),
                                    "resource_net_depletion_J": [str((previous[8] - energies[8]).bound(self.groups, False).value(self.budgets)), str((previous[8] - energies[8]).bound(self.groups).value(self.budgets))],
                                    "source_attributable_accepted_lower_J": str(lower.value(self.budgets) - 2 * self.budgets["work_uncertainty"] - other.value(self.budgets))})
            if kind == "G" and self.configuration != "positive":
                if state[0][2] != post_state[0][2]:
                    raise ValueError("negative declared target unexpectedly reacts")
                negative_gates += 1
                self.require("negative_target_abs_work_per_G_including_uncertainty", parameter("negative_abs_work_per_G"), ".010", "work")
            if self.configuration != "positive" and kind == ("G" if inverse else "F"):
                # A whole 100 s bound includes the eight non-G seconds of
                # every macrostep. Net endpoint energy alone cannot bound
                # out-and-back port current during those isolated slots.
                count = (step - 1) % 10 + 1
                self.require("negative_target_abs_work_100s_block",
                             parameter("negative_abs_work_per_G", count)
                             + parameter("negative_abs_work_outside_G_per_macrostep", count), ".020", "work")
            rows = self.snapshot(energies, after_counts, previous)
            total = sum(energies, Affine())
            closure = total - initial_total + self.bank_heat - self.bank_injection
            if closure.bound(self.groups).value(self.budgets) or closure.bound(self.groups, False).value(self.budgets):
                raise ValueError("conditional bank/auxiliary ledger does not close")
            self.layers.append({"time_s": str(self.time), "layer": self.location, "banks": rows, "events": self.events,
                                "auxiliaries_READY_J": {f"converter{i}": "0" for i in range(3)},
                                "total_increment_J": [str(total.bound(self.groups, False).value(self.budgets)), str(total.bound(self.groups).value(self.budgets))],
                                "gross_dissipation_upper_J": str(self.gross_heat_upper.value(self.budgets)),
                                "positive_uncontrolled_injection_upper_J": str(self.injection_upper.value(self.budgets)),
                                "signed_external_bank_input_J": [str(-self.injection_upper.value(self.budgets)), str(self.injection_upper.value(self.budgets))],
                                "conditional_bank_auxiliary_balance_residual_J": "0",
                                "net_storage_change_J": [str((total - initial_total).bound(self.groups, False).value(self.budgets)), str((total - initial_total).bound(self.groups).value(self.budgets))]})
        encoding_failure = next((c for c in self.constraints if c["scope"] == "encoding" and Q(c["margin"]) < 0), None)
        work_failure = next((c for c in self.constraints if c["scope"] == "work" and Q(c["margin"]) < 0), None)
        worst = min(self.constraints, key=lambda c: Q(c["margin"]))
        worst_bank = min((c for c in self.constraints if c["quantity"].endswith((":positive_error", ":negative_error"))), key=lambda c: Q(c["margin"]))
        return {"configuration": self.configuration, "mode": self.mode,
                "status": "CONDITIONAL" if self.first_violation is None else "NOT_CERTIFIED",
                "encoding_status": "CONDITIONAL" if encoding_failure is None else "NOT_CERTIFIED",
                "work_status": "CONDITIONAL" if work_failure is None else "NOT_CERTIFIED",
                "work_scope": ("No forward step-3 first-work predicate in inverse-first mode." if self.mode == "inverse_forward200" and self.configuration == "positive"
                               else "Signed source-attributed first receiving work." if self.configuration == "positive"
                               else "Absolute target work per G and each 100 s block."),
                "first_violation": self.first_violation, "smallest_constraint_margin": worst,
                "smallest_bank_dec_margin": worst_bank,
                "horizon_s": str(self.time), "accepted_G": self.accepted_gates,
                "auxiliary_starts_upper": self.auxiliary_starts, "layers": self.layers, "constraints": self.constraints}


def maximum_budgets(results, budgets, include_work):
    constraints = [c for result in results for c in result["constraints"] if include_work or c["scope"] == "encoding"]
    parsed = [(c, Q(c["value"]), Q(c["upper"]), {k: Q(v) for k, v in c["lhs"]["terms"].items()}) for c in constraints]
    answer = {}
    for name in KINDS:
        upper, lower, limiter = None, Q(0), None
        for c, value, ceiling, coefficients in parsed:
            coefficient = coefficients.get(name, Q(0))
            fixed = value - coefficient * budgets[name]
            if coefficient > 0:
                candidate = (ceiling - fixed) / coefficient
                if upper is None or candidate < upper:
                    upper, limiter = candidate, c
            elif coefficient < 0:
                lower = max(lower, (ceiling - fixed) / coefficient)
            elif fixed > ceiling:
                lower, upper, limiter = Q(1), Q(0), c
                break
        answer[name] = {"minimum": str(lower), "maximum": str(upper) if upper is not None else None,
                        "feasible": upper is None or lower <= upper,
                        "limiting_constraint": limiter}
    return answer


def build_report(model):
    law = load_law()
    p = law.local()
    seeds = tuple(w for w in product(range(-2, 3), range(-3, 4), range(-2, 3), range(-4, 5)) if p.active_energy(w) == 1)
    if len(seeds) != 20:
        raise ValueError("pinned unit seed census mismatch")
    modes = ("forward100", "forward_inverse200", "inverse_forward200")
    results, classes = [], []
    for configuration in ("positive", "offimage", "cut0", "cut1"):
        for mode in modes:
            initial, trace = declared_trace(law, configuration, mode, p.W)
            signature = [(step, inverse, kind, bank_counts(pre, law), bank_counts(post, law),
                          tuple(pre[0][i] != post[0][i] for i in range(3))) for step, inverse, kind, pre, post in trace]
            # Pure declared-law equivalence, including the known holdout vector;
            # this is not system tuning, HIL, or a confirmation trial.
            checked = (p.W,) if configuration == "offimage" else seeds
            for seed in checked:
                _, other = declared_trace(law, configuration, mode, seed)
                sig = [(a, b, c, bank_counts(d, law), bank_counts(e, law), tuple(d[0][i] != e[0][i] for i in range(3))) for a, b, c, d, e in other]
                if sig != signature:
                    raise ValueError("seed energy-trajectory class mismatch")
            classes.append({"configuration": configuration, "mode": mode, "declared_preparations": len(checked),
                            "energy_trace_sha256": sha256(json.dumps(signature, separators=(",", ":")).encode()).hexdigest()})
            results.append(Certifier(model, configuration, mode).certify(law, initial, trace))
    budgets = {k: Q(v) for k, v in model["budgets_J"].items()}
    return {"schema": "twistj-reserve-certificate/1", "provenance": "SOFTWARE_DEVELOPMENT_KNOWN_MODEL",
            "status": "CONDITIONAL" if all(r["status"] == "CONDITIONAL" for r in results) else "NOT_CERTIFIED",
            "physical_qualification": "NOT_PERFORMED", "scientific_run": "NOT_PERFORMED",
            "arithmetic": "Python fractions.Fraction; no floating-point assertion",
            "source_hashes": {"primary.py": PRIMARY_SHA, "inherited_verify.py": LOCAL_SHA},
            "model": model, "seed_classes": classes, "unit_seeds": seeds,
            "preparation_nonempty_witness": "Every bank exactly n/2 J above its reference; all initial error variables 0; auxiliaries READY=0.",
            "results": results, "maximum_budget_enc_oper_only": maximum_budgets(results, budgets, False),
            "maximum_budget_including_work": maximum_budgets(results, budgets, True),
            "maximum_budget_semantics": "One category varies at a time with all other supplied budgets fixed. Exact supremum for this sufficient affine enclosure, not optimal physical loss tolerance. Simultaneously taking every maximum is invalid."}


def counterexample():
    incoming = (Q("8.780"), Q(0), Q(".780"))
    uncertainty = Q(".020")
    assert abs(incoming[0] - 9) + uncertainty == Q(".240")
    assert abs(incoming[2] - 1) + uncertainty == Q(".240")
    total, required = sum(incoming), Q(10) - Q(".240") + uncertainty
    assert total == Q("9.560") and required == Q("9.780") and total < required
    return {"status": "KNOWN_COUNTEREXAMPLE", "input_sum_J": str(total), "required_B_J": str(required),
            "shortfall_J": str(required - total), "assumptions": "No losses, no injection, no commanded baseline withdrawal; zero output accounts cannot finance B by baseline borrowing."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=Path, default=HERE / "budgets-v1.json")
    parser.add_argument("--output", type=Path, required=True, help="Generated certificate path outside the repository")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error("generated development results must stay outside the tracked worktree")
    model = load_model(args.budget)
    report = build_report(model)
    report["counterexample"] = counterexample()
    report["input_sha256"] = sha256(args.budget.read_bytes()).hexdigest()
    report["certifier_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode()
    output.write_bytes(data)
    print(json.dumps({"status": report["status"], "qualification": "NOT_PERFORMED", "traces": len(report["results"]),
                      "layers": sum(len(r["layers"]) for r in report["results"]), "certificate_sha256": sha256(data).hexdigest(),
                      "certificate_bytes": len(data)}, sort_keys=True))
    return 0 if report["status"] == "CONDITIONAL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
