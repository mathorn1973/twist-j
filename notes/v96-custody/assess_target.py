"""Both frozen forward predicates; no configuration selection or source data."""

import argparse
from fractions import Fraction
from schema import ROLES, canonical, contract, frame_keys, hash_object, load, packet, packet_flags, q
from metrology import integrate

SATISFIED, FAILED, INDETERMINATE = "SATISFIED", "FAILED", "INDETERMINATE"


def combine(outcomes):
    if FAILED in outcomes:
        return FAILED
    return INDETERMINATE if INDETERMINATE in outcomes else SATISFIED


def compare(value, condition):
    return INDETERMINATE if value is None else (SATISFIED if condition(value) else FAILED)


def trace_result(observed, expected, frozen):
    outcomes = []
    for index, frame in enumerate(observed["frames"]):
        predicted = expected[index]
        readings = frame["readings"]
        if [item["t_s"] for item in readings] != frozen["read_grid_s"][index]:
            outcomes.append(INDETERMINATE)
        for item in readings:
            outcomes.extend(compare(got, lambda x, want=want: x == want)
                            for got, want in zip(item["coordinates"], predicted["coordinates"]))
            outcomes.append(compare(item["p"], lambda p: p == predicted["p"] and 0 <= p < 5))
            outcomes.append(compare(item["optical"], lambda c: c == frozen["optical_codes"][predicted["p"]]))
            if item["angle_deg"] is None:
                outcomes.append(INDETERMINATE)
            else:
                # Periodic angle with actual physical p, not a step-number reader.
                delta = (q(item["angle_deg"]) - 72 * predicted["p"] + 180) % 360 - 180
                outcomes.append(SATISFIED if abs(delta) <= 5 else FAILED)
            outcomes.append(compare(item["temperature_C"], lambda t: 22 <= q(t) <= 24))
            for role in ROLES:
                bank = item["banks"][role]
                if any(v is None for v in bank.values()):
                    outcomes.append(INDETERMINATE)
                    continue
                error = abs(q(bank["energy_J"]) - Fraction(predicted["counts"][role], 2)) + q(bank["U_J"])
                limit = Fraction(1, 50) if index == 0 else Fraction(6, 25)
                outcomes.append(SATISFIED if error <= limit and q(bank["U_J"]) <= Fraction(1, 50)
                                and Fraction(47, 10) <= q(bank["voltage_V"]) <= 50 else FAILED)
    return combine(outcomes)


def assess(observed, frozen):
    packet(observed)
    contract(frozen)
    quality = []
    findings = set()
    all_flags = packet_flags(observed)
    for flag in all_flags:
        if flag == "MISSING":
            quality.append(INDETERMINATE)
        elif flag != "SYNTHETIC":
            quality.append(FAILED)
        findings.add(flag)
    uncertainty = observed["uncertainty"]
    quality.append(compare(uncertainty["time_s"], lambda u: q(u) <= Fraction(1, 1000)))
    if [(f["step"], f["layer"]) for f in observed["frames"]] != frame_keys():
        # No zip truncation, duplicate frame, or absent final record may pass.
        # Preserve synthetic provenance and known failures even on this path.
        findings.add("FRAME_ROSTER")
        incomplete = combine(quality + [INDETERMINATE])
        return result(observed, frozen, incomplete, incomplete, sorted(findings))
    # All three independently observed local paths are required packet data.
    # This is a coverage check only: do not sum both ends of one transfer.
    if any(integrate(observed["ports"][role], Fraction(0), Fraction(100)) is None
           for role in ROLES):
        quality.append(INDETERMINATE)
        findings.add("LOCAL_PORTS_MISSING")
    for i, frame in enumerate(observed["frames"]):
        if [r["t_s"] for r in frame["readings"]] != frozen["read_grid_s"][i]:
            # A shifted actual observation is a timing failure; an absent one is
            # indeterminate. Preserve times and missing records verbatim.
            quality.append(FAILED if len(frame["readings"]) == len(frozen["read_grid_s"][i]) else INDETERMINATE)
            findings.add("READ_GRID")
    positive_trace = [trace_result(observed, candidate, frozen) for candidate in frozen["positive_tables"]]
    positive = [SATISFIED if SATISFIED in positive_trace else
                (INDETERMINATE if INDETERMINATE in positive_trace else FAILED)]
    null = [trace_result(observed, frozen["null_table"], frozen)]
    # Entire step-3 G operation incl. quiet/read interval: [20,22] seconds.
    work = integrate(observed["ports"]["B_2"], Fraction(20), Fraction(22))
    U = uncertainty["first_work_J"]
    if work is None or U is None:
        positive.append(INDETERMINATE)
        findings.add("FIRST_WORK_MISSING")
    else:
        lower, upper = work[0] - q(U), work[0] + q(U)
        positive.append(SATISFIED if lower >= Fraction(19, 20) and upper <= Fraction(21, 20)
                        and q(U) <= Fraction(1, 100) else FAILED)
    # Negative target-work predicate uses the same B_2 port as first work.
    # Z_2/r_2 remain genuine local series and independent full-audit accounts;
    # summing both ends of one transfer would double-count its energy.
    for start, end, U, limit in [(Fraction(0), Fraction(100), uncertainty["whole_abs_J"], Fraction(1, 50))] + [
            (Fraction(10 * i), Fraction(10 * i + 2), uncertainty["slot_abs_J"][i], Fraction(1, 100)) for i in range(10)]:
        measured = [integrate(observed["ports"]["B_2"], start, end)]
        if U is None or any(v is None for v in measured):
            null.append(INDETERMINATE)
            findings.add("ABS_WORK_MISSING")
        else:
            null.append(SATISFIED if sum(v[1] for v in measured) + q(U) <= limit else FAILED)
    return result(observed, frozen, combine(positive + quality), combine(null + quality), sorted(findings))


def result(observed, frozen, positive, null, findings):
    return {"id": observed["id"], "packet_sha256": hash_object(observed), "contract_sha256": hash_object(frozen),
            "positive": positive, "null": null, "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet")
    parser.add_argument("contract")
    args = parser.parse_args()
    print(canonical(assess(load(args.packet), load(args.contract))).decode("ascii"))


if __name__ == "__main__":
    main()
