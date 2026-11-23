"""Replay and score the historical and prospective H3 pulse-return panels."""

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from physical import KERNEL_SHA256, NATIVE_TICKS, Physical, key, projected, roster
from reader import LABELS, canonical, load_reader


PANELS = ("ordinary", "stress")
HISTORICAL_GAINS = ((705, 706, 707, 708), (768, 832, 896, 960))
FRESH_GAINS = ((961, 962, 963, 964), (1024, 1088, 1152, 1216))
ARMS = ("FULL", "SWAP", "HEAD", "TAIL", "Q")
READOUTS = ("original", "six", "orbit", "baseline", "selected")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("ascii")


def digest(value):
    return sha256(value).hexdigest()


def truth(case):
    arm, k, l, _, _ = key(case)
    if arm not in ("FULL", "SWAP"):
        return "ABSTAIN"
    difference = l - k if arm == "FULL" else k - l
    return "POS" if difference % 5 in (1, 3) else "NEG"


def read_projection(record, read, cache):
    if record in cache:
        return cache[record]
    call = read(json.loads(record))
    required = set(READOUTS) | {"row1_onset", "exact_control", "match"}
    require(set(call) == required and all(call[name] in LABELS for name in READOUTS),
            "reader returned an invalid call")
    require(type(call["exact_control"]) is bool and type(call["match"]) is bool,
            "reader returned an invalid flag")
    cache[record] = call
    return call


def panel(physics, gains, comparator, read, cache, past_row0):
    cases = roster(gains)
    require(len(cases) == 3210, "incorrect roster size")
    raw_by_key = {}
    evidence = []
    for case in cases:
        raw, _ = physics.run(case)
        require(len(raw) == len(NATIVE_TICKS), "incorrect native record length")
        case_key = key(case)
        require(case_key not in raw_by_key or (case["arm"] == "Q" and raw_by_key[case_key] == raw),
                "unexpected repeated case or unequal quiet native records")
        raw_by_key[case_key] = raw
        projection = compact(projected(raw))
        call = read_projection(projection, read, cache)
        row = dict(case, truth=truth(case), projection=projection, call=call)
        if comparator is not None:
            row["absent_from_public_comparator"] = projection not in comparator
        if case["arm"] == "FULL" and call["baseline"] == "ABSTAIN":
            raw_row0 = tuple(tick[0] for tick in raw[-80:])
            row["raw_late_row0"] = raw_row0
            if past_row0 is not None:
                row["matches_historical_rescue_row0"] = raw_row0 in past_row0
        evidence.append(row)
    counts = Counter()
    for (arm, k, l, eta, m), raw in raw_by_key.items():
        if arm in ("HEAD", "SWAP"):
            twin = ("FULL" if arm == "SWAP" else "HEAD", l, k, eta, m)
            counts[arm] += int(raw == raw_by_key[twin])
    return evidence, {
        "native_head_matches": counts["HEAD"], "native_swap_matches": counts["SWAP"],
        "native_row_transfers": len(cases) * len(NATIVE_TICKS) * 2,
    }


def outcome(rows, mode, signed):
    counts = Counter()
    for row in rows:
        call = row["call"][mode]
        if signed:
            value = signed_outcome(call, row["truth"])
        else:
            value = "silent" if call == "ABSTAIN" else "writes"
        counts[value] += 1
    fields = ("correct", "silent", "wrong") if signed else ("silent", "writes")
    return {"presentations": len(rows), **{field: counts[field] for field in fields}}


def signed_outcome(call, target):
    if call == "ABSTAIN":
        return "silent"
    return "correct" if call == target else "wrong"


def marginal(rows):
    opportunity = [row for row in rows if row["call"]["baseline"] == "ABSTAIN"]
    results = outcome(opportunity, "selected", signed=True)
    fingerprints = {row["projection"] for row in rows}
    distinct = defaultdict(set)
    for row in opportunity:
        label = signed_outcome(row["call"]["selected"], row["truth"])
        distinct[label].add(row["projection"])
    return {
        "presentations": len(rows), "distinct_projections": len(fingerprints),
        "opportunities": len(opportunity), "correct_additions": results["correct"],
        "wrong_additions": results["wrong"], "still_silent": results["silent"],
        "distinct_opportunities": len({row["projection"] for row in opportunity}),
        "distinct_correct_additions": len(distinct["correct"]), "distinct_wrong_additions": len(distinct["wrong"]),
        "distinct_still_silent": len(distinct["silent"]),
    }


def summary(rows, compare=False):
    arms = {arm: [] for arm in ARMS}
    fronts = defaultdict(list)
    for row in rows:
        arms[row["arm"]].append(row)
        if row["arm"] == "FULL":
            fronts[row["k"], row["l"]].append(row)
    full = arms["FULL"]
    opportunities = []
    for row in full:
        if row["call"]["baseline"] != "ABSTAIN":
            continue
        report = {name: value for name, value in row.items()
                  if name not in ("projection", "raw_late_row0")}
        if compare:
            report["projected_sha256"] = digest(row["projection"])
            report["raw_late_row0_sha256"] = digest(compact(row["raw_late_row0"]))
        opportunities.append(report)
    return {
        "presentations": len(rows),
        "arms": {arm: {mode: outcome(arms[arm], mode, arm in ("FULL", "SWAP"))
                       for mode in READOUTS} for arm in ARMS},
        "fronts": [
            {"pair": [a, b], "directions": [
                {"direction": [k, l], "truth": truth(dict(arm="FULL", k=k, l=l, eta=0, m=0)),
                 "baseline": outcome(fronts[k, l], "baseline", signed=True),
                 "selected": outcome(fronts[k, l], "selected", signed=True),
                 **({"absent_from_public_comparator": marginal(
                     [row for row in fronts[k, l] if row["absent_from_public_comparator"]])}
                    if compare else {})}
                for k, l in ((a, b), (b, a))
            ]} for a, b in combinations(range(5), 2)
        ],
        "marginal_full": marginal(full),
        "marginal_positive_full": marginal([row for row in full if row["truth"] == "POS"]),
        "marginal_swap": marginal(arms["SWAP"]),
        **({
            "marginal_full_absent_from_public_comparator": marginal(
                [row for row in full if row["absent_from_public_comparator"]]),
            "marginal_positive_full_absent_from_public_comparator": marginal(
                [row for row in full if row["truth"] == "POS" and row["absent_from_public_comparator"]]),
            "marginal_full_present_in_public_comparator": marginal(
                [row for row in full if not row["absent_from_public_comparator"]]),
        } if compare else {}),
        "marginal_positive_0_to_1_phase_2": marginal(
            [row for row in full if (row["k"], row["l"], row["m"]) == (0, 1, 2)]),
        "intact_row1_onset_flips": sum(
            row["call"]["orbit"] == "NEG" and row["call"]["row1_onset"] == 118
            and row["call"]["baseline"] == row["call"]["selected"] == "POS" for row in full
        ),
        "signed_baseline_changes": sum(
            row["call"]["baseline"] not in ("ABSTAIN", row["call"]["selected"]) for row in rows),
        "exact_control_writes": sum(row["call"]["exact_control"] and row["call"]["selected"] != "ABSTAIN"
                                   for row in rows),
        "full_opportunities": opportunities,
    }


def prediction(summary, panels):
    arms = summary["arms"]
    full, swap = (arms[name]["selected"] for name in ("FULL", "SWAP"))
    marginal_full = summary["marginal_full"]
    target = summary["marginal_positive_0_to_1_phase_2"]

    def verdict(condition):
        return "PASS" if condition else "FAIL"

    def opportunity_verdict(data, all_required=False):
        if data["opportunities"] == 0:
            return "INCONCLUSIVE"
        count = data["correct_additions"]
        return verdict(count == data["opportunities"] if all_required else count > 0)

    return {
        "all_full_correct": verdict(full["correct"] == full["presentations"]),
        "all_swap_donor_correct": verdict(swap["correct"] == swap["presentations"]),
        "all_controls_silent": verdict(all(arms[a]["selected"]["writes"] == 0
                                           for a in ("HEAD", "TAIL", "Q"))),
        "no_wrong_full_additions": verdict(marginal_full["wrong_additions"] == 0),
        "no_wrong_swap_additions": verdict(summary["marginal_swap"]["wrong_additions"] == 0),
        "native_swaps_and_heads_match": verdict(all(
            panels[name]["physical"][kind] == 800
            for name in PANELS for kind in ("native_head_matches", "native_swap_matches")
        )),
        "signed_baseline_preserved": verdict(summary["signed_baseline_changes"] == 0),
        "exact_control_veto_preserved": verdict(summary["exact_control_writes"] == 0),
        "correct_full_addition": opportunity_verdict(summary["marginal_positive_full"]),
        "correct_positive_full_addition_absent_from_public_comparator": opportunity_verdict(
            summary["marginal_positive_full_absent_from_public_comparator"]),
        "all_silent_0_to_1_phase_2_recovered": opportunity_verdict(target, all_required=True),
    }


def historical_guard(totals):
    arms = totals["arms"]
    require(arms["FULL"]["baseline"] == {"presentations": 1600, "correct": 1597, "silent": 3, "wrong": 0},
            "historical intact baseline differs")
    require(totals["intact_row1_onset_flips"] == 34, "historical intact row-1 flip count differs")
    for arm in ("FULL", "SWAP"):
        require(arms[arm]["selected"] == {"presentations": 1600, "correct": 1600, "silent": 0, "wrong": 0},
                f"historical {arm} selected outcomes differ")
    for arm in ("HEAD", "TAIL", "Q"):
        require(arms[arm]["baseline"]["writes"] == arms[arm]["selected"]["writes"] == 0,
                f"historical {arm} control writes differ")
    rescued = totals["full_opportunities"]
    require(len(rescued) == 3 and all(
        (row["k"], row["l"], row["m"]) == (0, 1, 2)
        and row["truth"] == row["call"]["selected"] == "POS" for row in rescued
    ), "historical intact rescue outcomes differ")
    require(totals["signed_baseline_changes"] == totals["exact_control_writes"] == 0,
            "historical predecessor preservation differs")


def verify(root):
    physics, read, cache = Physical(root), load_reader(root), {}
    historical, history_rows = {}, []
    for name, gains in zip(PANELS, HISTORICAL_GAINS, strict=True):
        rows, physical = panel(physics, gains, None, read, cache, None)
        require(physical["native_swap_matches"] == physical["native_head_matches"] == 800,
                f"historical {name} native symmetries differ")
        historical[name] = {"gains": gains, "physical": physical, **summary(rows)}
        history_rows.extend(rows)
    historical["totals"] = summary(history_rows)
    historical_guard(historical["totals"])
    comparator = {row["projection"] for row in history_rows}
    past_row0 = {row["raw_late_row0"] for row in history_rows if "raw_late_row0" in row}

    fresh, fresh_rows = {}, []
    for name, gains in zip(PANELS, FRESH_GAINS, strict=True):
        rows, physical = panel(physics, gains, comparator, read, cache, past_row0)
        fresh[name] = {"gains": gains, "physical": physical, **summary(rows, compare=True)}
        fresh_rows.extend(rows)
    fresh["totals"] = summary(fresh_rows, compare=True)
    predicates = prediction(fresh["totals"], fresh)
    status = next((label for label in ("FAIL", "INCONCLUSIVE") if label in predicates.values()), "PASS")
    return {
        "historical": historical, "fresh": fresh, "predicates": predicates, "status": status,
        "canonical_calls_sha256": digest(canonical([row["call"] for row in fresh_rows])),
        "kernel_sha256": KERNEL_SHA256,
        "public_comparator": {
            "panels": dict(zip(PANELS, HISTORICAL_GAINS, strict=True)),
            "presentations": len(history_rows),
            "distinct_projections": len(comparator),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HERE.parent.parent,
                        help="repository root containing the pinned H3 kernel")
    args = parser.parse_args()
    report = verify(args.root)
    sys.stdout.buffer.write(canonical(report))


if __name__ == "__main__":
    main()
