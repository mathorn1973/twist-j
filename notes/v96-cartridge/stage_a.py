"""NON-CANONICAL: calibrated Stage-A reduction; no CV^2 energy substitution."""

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import isqrt
import sys


class Invalid(ValueError):
    pass


def check(condition, message):
    if not condition:
        raise Invalid(message)


def number(value):
    check(type(value) is str, "exact rational string required")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise Invalid("finite exact rational required") from exc
    check(str(result) == value, "canonical rational required")
    return result


def keys(value, required, label):
    check(type(value) is dict and set(value) == required, label + " schema")


def digest(value, label):
    check(type(value) is str and len(value) == 64 and all(c in "0123456789abcdef" for c in value), label + " hash")


def sqrt_upper(value):
    check(value >= 0, "negative variance")
    scale = 10**12
    root = isqrt(value.numerator * scale * scale // value.denominator)
    if root * root * value.denominator < value.numerator * scale * scale:
        root += 1
    return Fraction(root, scale)


def calibrated_energy(calibration, specimen, dock, temperature, history, protocol_sha256, voltage):
    """Interpolation inside a measured map with an explicitly qualified bound.

    All knots and interpolation/temperature bounds require external evidence.
    This routine never creates them from nominal capacitance.
    """
    keys(calibration, {"kind", "origin", "specimen", "dock", "temperature_C", "history", "protocol_sha256", "knots", "interpolation_U_J"}, "calibration")
    check(calibration["kind"] == "MEASURED_ENERGY_MAP", "nominal capacitor/model map forbidden")
    check(calibration["origin"] in ("MEASURED", "SYNTHETIC"), "map provenance")
    check((calibration["specimen"], calibration["dock"], calibration["temperature_C"], calibration["history"], calibration["protocol_sha256"])
          == (specimen, dock, temperature, history, protocol_sha256), "wrong specimen/dock/temperature/history/protocol")
    volts = number(voltage)
    check(Fraction(47, 10) <= volts <= 50, "voltage outside physical range")
    for value in (specimen, dock, history):
        check(type(value) is str and value.strip(), "calibration context identifier")
    number(temperature)
    digest(protocol_sha256, "protocol")
    knots = calibration["knots"]
    check(type(knots) is list and len(knots) >= 2, "calibration knots absent")
    for knot in knots:
        keys(knot, {"voltage_V", "energy_inc_J", "U_J"}, "calibration knot")
    parsed = [(number(k["voltage_V"]), number(k["energy_inc_J"]), number(k["U_J"])) for k in knots]
    check(all(u >= 0 for _, _, u in parsed), "negative energy uncertainty")
    check(all(parsed[i + 1][0] > parsed[i][0] and parsed[i + 1][1] > parsed[i][1] for i in range(len(parsed) - 1)), "non-single-valued calibration")
    for (v0, e0, u0), (v1, e1, u1) in zip(parsed, parsed[1:]):
        if v0 <= volts <= v1:
            fraction = (volts - v0) / (v1 - v0)
            extra = number(calibration["interpolation_U_J"])
            check(extra >= 0, "interpolation uncertainty")
            value = e0 + fraction * (e1 - e0)
            bound = (1 - fraction) * u0 + fraction * u1 + extra
            return {"energy_inc_J": str(value), "U_J": str(bound), "origin": calibration["origin"]}
    raise Invalid("no energy-map extrapolation")


def difference_uncertainty(model):
    """k sqrt(u0^2+u1^2-2cov), plus conservative unresolved expanded bound."""
    required = {"u0_J", "u1_J", "covariance_J2", "coverage_factor", "dof", "unresolved_U_J", "justification_sha256"}
    keys(model, required, "complete difference uncertainty")
    u0, u1 = number(model["u0_J"]), number(model["u1_J"])
    cov, k = number(model["covariance_J2"]), number(model["coverage_factor"])
    extra = number(model["unresolved_U_J"])
    check(u0 >= 0 and u1 >= 0 and abs(cov) <= u0 * u1, "invalid covariance")
    check(k >= 1 and number(model["dof"]) > 0 and extra >= 0, "coverage/uncertainty unavailable")
    digest(model["justification_sha256"], "uncertainty justification")
    return k * sqrt_upper(u0 * u0 + u1 * u1 - 2 * cov) + extra


def evaluate_hold(record):
    """Numerical hold decision; authenticated specimen qualification is separate."""
    keys(record, {"kind", "origin", "horizon_s", "level", "missing", "initial_energy_J", "final_energy_J",
                  "initial_map_U_J", "final_map_U_J", "minimum_voltage_V", "maximum_voltage_V", "voltage_U_V",
                  "injection_upper_J", "charger_connected", "saturation", "both_terminals_disconnected",
                  "elapsed_s", "time_U_s", "read_windows", "probe_on_s", "difference_uncertainty"}, "hold")
    check(record["origin"] in ("MEASURED", "SYNTHETIC"), "observation provenance")
    check(record["kind"] == "STAGE_A_HOLD", "observation type")
    check(type(record["horizon_s"]) is int and record["horizon_s"] in (100, 200), "both original horizons only")
    check(type(record["level"]) is int and 0 <= record["level"] <= 41, "qualified n=0..41")
    for flag in ("missing", "charger_connected", "saturation", "both_terminals_disconnected"):
        check(type(record[flag]) is bool, "Boolean physical flag required")
    if record["missing"] or any(record[k] is None for k in ("initial_energy_J", "final_energy_J", "initial_map_U_J", "final_map_U_J",
                                                          "minimum_voltage_V", "maximum_voltage_V", "voltage_U_V", "injection_upper_J", "difference_uncertainty")):
        return {"status": "INDETERMINATE", "origin": record["origin"], "qualification": "NOT_ESTABLISHED", "loss_upper_J": None}
    faults = []
    if record["charger_connected"] or record["saturation"] or not record["both_terminals_disconnected"]:
        faults.append("HARDWARE_OR_ACQUISITION_FAULT")
    check(number(record["time_U_s"]) >= 0 and number(record["probe_on_s"]) >= 0, "negative uncertainty/time")
    if number(record["elapsed_s"]) != record["horizon_s"] or number(record["time_U_s"]) > Fraction(1, 1000):
        faults.append("TIMING")
    expected_windows = 41 if record["horizon_s"] == 100 else 81
    check(type(record["read_windows"]) is int, "integer read-window count required")
    if record["read_windows"] != expected_windows:
        faults.append("DUTY_CYCLE")
    # Frozen candidate protocol: each of the windows has 100 ms front-end
    # settling followed by 100 ms read. A zero/short exposure is not the
    # assembled sensing-path test even though it appears to reduce leakage.
    if number(record["probe_on_s"]) != Fraction(expected_windows, 5):
        faults.append("PROBE_ON_TIME")
    initial, final = number(record["initial_energy_J"]), number(record["final_energy_J"])
    u_initial, u_final = number(record["initial_map_U_J"]), number(record["final_map_U_J"])
    check(u_initial >= 0 and u_final >= 0, "negative map uncertainty")
    nominal = Fraction(record["level"], 2)
    if abs(initial - nominal) + u_initial > Fraction(1, 50) or max(u_initial, u_final) > Fraction(1, 50):
        faults.append("PREPARATION_OR_MAP_UNCERTAINTY")
    if abs(final - nominal) + u_final > Fraction(6, 25):
        faults.append("FINAL_DECODING")
    minimum, maximum = number(record["minimum_voltage_V"]), number(record["maximum_voltage_V"])
    voltage_u = number(record["voltage_U_V"])
    check(voltage_u >= 0, "negative voltage uncertainty")
    # This uncertainty must cover calibration and unobserved extrema in the
    # supplied time envelope, not just an isolated DMM accuracy specification.
    if minimum > maximum or minimum - voltage_u < Fraction(47, 10) or maximum + voltage_u > 50:
        faults.append("VOLTAGE_RANGE")
    U = difference_uncertainty(record["difference_uncertainty"])
    injection = number(record["injection_upper_J"])
    check(injection >= 0, "negative injection bound")
    upper = initial - final + U + injection
    # An injection can mask actual dissipation; add its entire upper bound.
    # Apparent gain outside the complete budget is an inconsistent energy map.
    if upper < 0 or upper > Fraction(1, 50):
        faults.append("HOLD_ENERGY")
    status = "FAILED" if faults else "SATISFIED_NUMERICAL_HOLD"
    return {"status": status, "origin": record["origin"], "qualification": "NOT_CONFIRMATORY" if record["origin"] == "SYNTHETIC" else "PENDING_AUTHENTICATED_FULL_STAGE_A",
            "loss_upper_J": str(upper), "U_difference_J": str(U), "faults": faults}


def design_budget(horizon_s):
    """Conditional arithmetic, NOT evidence of component leakage or calibration."""
    check(type(horizon_s) is int and horizon_s in (100, 200), "horizon")
    windows = 41 if horizon_s == 100 else 81
    on_time = Fraction(windows, 5)  # 100 ms settle + original 100 ms read
    minimum_divider_R = Fraction(91_000_000) * Fraction(95, 100)
    divider = Fraction(50 * 50) * on_time / minimum_divider_R
    return {"scope": "CONDITIONAL_DESIGN_ARITHMETIC", "horizon_s": horizon_s,
            "windows": windows, "probe_on_s": str(on_time), "divider_upper_J": str(divider),
            "total_limit_J": "1/50", "unqualified_other_budget_J": str(Fraction(1, 50) - divider)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hold")
    args = parser.parse_args()
    if args.hold:
        if args.hold == "-":
            result = evaluate_hold(json.load(sys.stdin))
        else:
            with open(args.hold, encoding="utf-8") as stream:
                result = evaluate_hold(json.load(stream))
    else:
        result = [design_budget(100), design_budget(200)]
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    if args.hold:
        return {"SATISFIED_NUMERICAL_HOLD": 0, "FAILED": 2, "INDETERMINATE": 3}[result["status"]]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
