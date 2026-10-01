"""Post-disclosure replay and source audit; target success never implies origin."""

import argparse
from fractions import Fraction
from hashlib import sha256
from schema import canonical, hash_object, keys, load, nonnegative, packet_flags, q, require
from assess_target import FAILED, INDETERMINATE, SATISFIED, combine
from project_target import project
from metrology import integrate

OTHER_COMPONENTS = ("cartridge_contacts_probes", "sensor_control_injection", "initial_converter_storage",
                    "receiver_other_storage", "baseline_depletion", "unresolved")


def replay_projection(reduction, observed_packet, input_bytes, reducer):
    """Every raw/calibration/settings/code input is byte-bound before replay.

    reducer is the independently reviewed adapter for the frozen raw schema,
    not the controller or a model-table generator. Never import/execute code
    from an untrusted bundle. Supply a known implementation from the gate pin.
    """
    keys(input_bytes, ("raw", "calibration", "settings", "reducer"))
    for name, data in input_bytes.items():
        require(type(data) is bytes, "original bytes required")
        require(sha256(data).hexdigest() == reduction[name + "_sha256"], "changed " + name)
    require(reducer is not None, "frozen instrument reduction unavailable")
    recomputed = reducer(input_bytes["raw"], input_bytes["calibration"], input_bytes["settings"])
    require(hash_object(recomputed) == hash_object(reduction), "raw/calibration reduction mismatch")
    require(project(recomputed, observed_packet["id"]) == observed_packet, "locked target projection mismatch")
    return "PROJECTION_IDENTICAL"


def source_origin(observed_packet, ledger):
    """Non-path energy across source G0 (0 s) through target G2 end (22 s)."""
    keys(ledger, ("interval_s", "other_upper_J", "balances"))
    require(ledger["interval_s"] == ["0", "22"], "full causal source-to-target interval required")
    keys(ledger["other_upper_J"], OTHER_COMPONENTS)
    components = ledger["other_upper_J"]
    if any(v is None for v in components.values()):
        return {"status": INDETERMINATE, "reason": "UNBOUNDED_NONPATH", "source_lower_J": None}
    other = sum(nonnegative(v) for v in components.values())
    first = integrate(observed_packet["ports"]["B_2"], Fraction(20), Fraction(22))
    U = observed_packet["uncertainty"]["first_work_J"]
    if first is None or U is None:
        return {"status": INDETERMINATE, "reason": "MISSING_WORK", "source_lower_J": None}
    lower = first[0] - nonnegative(U) - other
    checks = [SATISFIED if other <= Fraction(1, 100) and lower >= Fraction(19, 20)
              and q(U) <= Fraction(1, 100) else FAILED]
    balances = ledger["balances"]
    # Independent B_2 stored-energy gain, r_2 depletion and Z_2 account must
    # close separately. A residual called heat cannot stand in for these.
    keys(balances, ("B_2", "Z_2", "r_2"))
    for item in balances.values():
        keys(item, ("residual_J", "U_J", "independent_measurement_sha256"))
        if any(v is None for v in item.values()):
            checks.append(INDETERMINATE)
            continue
        from schema import digest
        digest(item["independent_measurement_sha256"])
        bound = nonnegative(item["U_J"])
        checks.append(SATISFIED if abs(q(item["residual_J"])) <= bound <= Fraction(1, 50) else FAILED)
    return {"status": combine(checks), "reason": "SOURCE_WORK_AND_BALANCES",
            "source_lower_J": str(lower), "other_upper_J": str(other)}


def source_equality(positive_energy_J, offimage_energy_J, U_difference_J):
    if None in (positive_energy_J, offimage_energy_J, U_difference_J):
        return INDETERMINATE
    difference = abs(q(positive_energy_J) - q(offimage_energy_J)) + nonnegative(U_difference_J)
    return SATISFIED if difference <= Fraction(1, 100) else FAILED


def full_state(observations, predictions, inverse=False):
    """Independent full observations vs separate pre-frozen prediction table.

    Forward: INIT+40 layer boundaries. Each inverse block: INIT+80 boundaries.
    Caller verifies prediction bytes in preparation commitment and acquisition
    provenance independently; shape alone cannot prove either provenance.
    """
    needed = 81 if inverse else 41
    require(type(predictions) is list and len(predictions) == needed, "frozen full prediction count")
    if type(observations) is not list or len(observations) != needed:
        return INDETERMINATE
    checks = []
    bank_names = tuple([f"{role}_{i}" for i in range(3) for role in ("B", "Z", "r")] + ["q0", "q1"])
    for position, (actual, expected) in enumerate(zip(observations, predictions)):
        keys(actual, ("index", "coordinates", "banks", "flags"))
        keys(expected, ("index", "coordinates", "counts"))
        require(expected["index"] == position, "frozen full frame order")
        if actual["index"] != position:
            checks.append(FAILED)
        from schema import coordinates, flags, bank
        coordinates(expected["coordinates"], 96)
        require(None not in expected["coordinates"], "incomplete prediction")
        coordinates(actual["coordinates"], 96)
        flags(actual["flags"])
        if any(v is None for v in actual["coordinates"]) or "MISSING" in actual["flags"]:
            checks.append(INDETERMINATE)
        elif actual["coordinates"] != expected["coordinates"]:
            checks.append(FAILED)
        if any(f not in ("MISSING", "SYNTHETIC") for f in actual["flags"]):
            checks.append(FAILED)
        keys(actual["banks"], bank_names)
        keys(expected["counts"], bank_names)
        for name in bank_names:
            item = actual["banks"][name]
            bank(item)
            count = expected["counts"][name]
            require(type(count) is int and 0 <= count <= 41, "expected count")
            if any(v is None for v in item.values()):
                checks.append(INDETERMINATE)
                continue
            limit = Fraction(1, 50) if position == 0 else Fraction(6, 25)
            checks.append(SATISFIED if abs(q(item["energy_J"]) - Fraction(count, 2)) + q(item["U_J"]) <= limit
                          and q(item["U_J"]) <= Fraction(1, 50) and Fraction(47, 10) <= q(item["voltage_V"]) <= 50 else FAILED)
    return combine(checks)


def audit_target_and_source(observed_packet, locked_verdict, configuration, ledger, origin):
    require(configuration in ("positive", "offimage", "cut0", "cut1"), "configuration")
    require(locked_verdict["packet_sha256"] == hash_object(observed_packet), "packet differs from locked verdict")
    require(locked_verdict["id"] == observed_packet["id"], "wrong locked ID")
    target = locked_verdict["positive" if configuration == "positive" else "null"]
    provenance = source_origin(observed_packet, ledger) if configuration == "positive" else {
        "status": "NOT_APPLICABLE_TO_NULL_FIRST_WORK", "reason": "FULL_NULL_STATE_STILL_REQUIRED"}
    synthetic = ("SYNTHETIC" in packet_flags(observed_packet) or
                 "SYNTHETIC" in locked_verdict.get("findings", []))
    return {"target": target, "source_origin": provenance,
            "eligibility": "NOT_CONFIRMATORY" if origin != "MEASURED" or synthetic
            else "PENDING_AUTHENTICATED_FULL_AUDIT", "campaign_pass": False}


def main():
    parser = argparse.ArgumentParser(description="Partial numerical audit only; authenticated replay/full gate still required")
    parser.add_argument("packet")
    parser.add_argument("verdict")
    parser.add_argument("ledger")
    parser.add_argument("configuration", choices=("positive", "offimage", "cut0", "cut1"))
    parser.add_argument("--origin", choices=("MEASURED", "SYNTHETIC"), required=True)
    args = parser.parse_args()
    from schema import packet
    observed = packet(load(args.packet))
    print(canonical(audit_target_and_source(observed, load(args.verdict), args.configuration,
                                           load(args.ledger), args.origin)).decode("ascii"))


if __name__ == "__main__":
    main()
