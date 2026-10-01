#!/usr/bin/env python3
"""Independent rational *arithmetic* checker, not an analog or propagation audit.

Does not import certify.py or the mathematical law. It verifies reported
inequalities, support evaluations, scopes, exact individual maxima and hashes.
The recurrence and physical assumptions still require their separate review.
"""

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def evaluate(linear, budgets):
    return Q(linear["constant"]) + sum((Q(v) * budgets[k] for k, v in linear["terms"].items()), Q(0))


def check(report):
    if report["schema"] != "twistj-reserve-certificate/1" or report["physical_qualification"] != "NOT_PERFORMED" or report["scientific_run"] != "NOT_PERFORMED":
        raise ValueError("unsupported or overstated certificate scope")
    if report["provenance"] != "SOFTWARE_DEVELOPMENT_KNOWN_MODEL":
        raise ValueError("incorrect development provenance")
    budgets = {k: Q(v) for k, v in report["model"]["budgets_J"].items()}
    all_constraints, any_failure = [], False
    seen = set()
    for result in report["results"]:
        key = result["configuration"], result["mode"]
        if key in seen:
            raise ValueError("duplicate configuration/mode")
        seen.add(key)
        actual_failure, previous_time = False, Q(0)
        for layer in result["layers"]:
            time = Q(layer["time_s"])
            if layer["layer"] != "preparation":
                duration = {"G": Q(2), "A": Q("2.5"), "B": Q("2.5"), "F": Q(3)}[layer["layer"][-1]]
                if time - previous_time != duration:
                    raise ValueError("layer time interval mismatch")
                if layer["conditional_bank_auxiliary_balance_residual_J"] != "0":
                    raise ValueError("nonclosing conditional bank balance")
            previous_time = time
            if len(layer["banks"]) != 11 or sum(row["count"] for row in layer["banks"]) != 41:
                raise ValueError("wrong bank inventory or count sum")
            if len({row["serial"] for row in layer["banks"]}) != 11:
                raise ValueError("lost/duplicated bank identity")
            for row in layer["banks"]:
                lo, hi = map(Q, row["increment_J"])
                if lo > hi or evaluate(row["lower_certificate"], budgets) != lo or evaluate(row["upper_certificate"], budgets) != hi:
                    raise ValueError("energy support evaluation mismatch")
        if previous_time != Q(result["horizon_s"]):
            raise ValueError("horizon mismatch")
        for constraint in result["constraints"]:
            value = evaluate(constraint["lhs"], budgets)
            ceiling = Q(constraint["upper"])
            if value != Q(constraint["value"]) or ceiling - value != Q(constraint["margin"]):
                raise ValueError("constraint arithmetic mismatch")
            actual_failure |= value > ceiling
            all_constraints.append((constraint, value, ceiling))
        if result["status"] != ("NOT_CERTIFIED" if actual_failure else "CONDITIONAL"):
            raise ValueError("result status mismatch")
        any_failure |= actual_failure
    expected = {(configuration, mode) for configuration in ("positive", "offimage", "cut0", "cut1")
                for mode in ("forward100", "forward_inverse200", "inverse_forward200")}
    if seen != expected or report["status"] != ("NOT_CERTIFIED" if any_failure else "CONDITIONAL"):
        raise ValueError("coverage or aggregate status mismatch")
    # This is only arithmetic over the supplied inequalities. It does not
    # authenticate that the generator produced all required inequalities.
    for title, include_work in (("maximum_budget_enc_oper_only", False), ("maximum_budget_including_work", True)):
        rows = [(c, v, u, {k: Q(x) for k, x in c["lhs"]["terms"].items()})
                for c, v, u in all_constraints if include_work or c["scope"] == "encoding"]
        for name, maximum in report[title].items():
            lower, upper = Q(0), None
            for _, value, limit, coefficients in rows:
                coefficient = coefficients.get(name, Q(0))
                rest = value - coefficient * budgets[name]
                if coefficient > 0:
                    cap = (limit - rest) / coefficient
                    upper = cap if upper is None else min(upper, cap)
                elif coefficient < 0:
                    lower = max(lower, (limit - rest) / coefficient)
                elif rest > limit:
                    lower, upper = Q(1), Q(0)
                    break
            reported_upper = None if maximum["maximum"] is None else Q(maximum["maximum"])
            if lower != Q(maximum["minimum"]) or upper != reported_upper or maximum["feasible"] != (upper is None or lower <= upper):
                raise ValueError("maximum budget arithmetic mismatch")
    return len(all_constraints)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--sha256", required=True, help="Previously recorded SHA-256 from the certifier's stdout")
    args = parser.parse_args()
    data = args.certificate.read_bytes()
    if sha256(data).hexdigest() != args.sha256:
        raise ValueError("certificate byte hash mismatch")
    report = json.loads(data)
    count = check(report)
    print(f"SOFTWARE arithmetic check: {count} exact inequalities; physical qualification NOT_PERFORMED")


if __name__ == "__main__":
    main()
