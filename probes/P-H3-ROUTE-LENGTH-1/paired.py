# SPDX-License-Identifier: Apache-2.0
"""Paired route arrivals, local collision responses and exact chord phase."""

from dataclasses import dataclass

from fixture import stock
import kernel as k
import phase


ARRIVAL_HORIZON = 64
CONVERSION_WINDOW = 4
HORIZON = ARRIVAL_HORIZON + CONVERSION_WINDOW + 1
A = k.HEAD + 3
R0, CORR = k.R0, k.CORR
COMPARISONS = (
    ("plus_zero", "plus", "zero"),
    ("minus_zero", "minus", "zero"),
    ("plus_minus", "plus", "minus"),
)


@dataclass(frozen=True)
class Cut:
    bit: int
    before: tuple
    transported: tuple
    complete: tuple
    tags: tuple


def trace(initial, rank, distance, sign):
    field, bit = initial, 1
    steps = [None]  # Positive indices are native observation ticks.
    account = k.account(initial)
    for tick in range(1, HORIZON + 1):
        transported = k.transport(field, k.HEIGHT, bit)
        complete, tags = k.scatter_field(transported)
        if k.account(transported) != account or k.account(complete) != account:
            raise AssertionError(("account", rank, distance, sign, tick))
        restored_c, reverse_tags = k.scatter_field(complete)
        if restored_c != transported or reverse_tags != tuple(
            3 - tag if tag else 0 for tag in tags
        ):
            raise AssertionError(("inverse B", rank, distance, sign, tick))
        next_bit = 1 - bit
        if k.transport(restored_c, k.HEIGHT, 1 - next_bit, -1) != field:
            raise AssertionError(("inverse C", rank, distance, sign, tick))
        steps.append(Cut(bit, field, transported, complete, tags))
        field, bit = complete, next_bit
    return steps


def lane_pair(cuts, stage, site, lane):
    return tuple(getattr(cut, stage)[site][lane] for cut in cuts)


def differs(values):
    left, right = values
    return left != right


def word_pair(values):
    return tuple(k.j_coefficients(value) for value in values)


def cell_pair(cuts, stage):
    return tuple(word_pair(getattr(cut, stage)[A]) for cut in cuts)


def following_contact(cuts, original):
    after_c = lane_pair(cuts, "transported", A, R0)
    after_b = lane_pair(cuts, "complete", A, R0)
    return {
        "survives": differs(after_c) and differs(after_b),
        "retains": after_c == original and after_b == original,
        "retains_each_word": tuple(
            before == c == b for before, c, b in zip(original, after_c, after_b)
        ),
        "next_c_words": word_pair(after_c),
        "next_b_words": word_pair(after_b),
    }


def collision_response(cuts):
    c_words = lane_pair(cuts, "transported", A, R0)
    b_words = lane_pair(cuts, "complete", A, R0)
    moves = tuple(c != b for c, b in zip(c_words, b_words))
    direction = {
        (True, False): "activation",
        (False, True): "suppression",
        (True, True): "both",
        (False, False): "neither",
    }[moves]
    return c_words, b_words, moves, direction


def compare(left, right, name, rank, distance):
    result = {
        "rank": rank, "distance": distance, "comparison": name,
        "first_tick": 0, "donor_x": -1, "local_equal": False,
        "donor_differs": False, "matter_equal": False,
        "first_three_equal": False, "isolated": False, "hit": False,
        "survives": False, "retains": False, "radiation_echo": False,
        "conversion_tick": 0, "conversion_left_tag": 0,
        "conversion_right_tag": 0, "conversion_left_moves": False,
        "conversion_right_moves": False, "conversion_survives": False,
        "conversion_retains": False, "arrival": None, "conversion": None,
    }
    for tick in range(1, ARRIVAL_HORIZON + 1):
        cuts = left[tick], right[tick]
        if differs(lane_pair(cuts, "transported", A, CORR)):
            break
    else:
        return result

    donor_x = 2 if cuts[0].bit else 0
    donor = donor_x * k.HEIGHT + A % k.HEIGHT
    local_equal = not differs(cell_pair(cuts, "before"))
    donor_values = lane_pair(cuts, "before", donor, CORR)
    c_left, c_right = cell_pair(cuts, "transported")
    matter_equal = c_left[:2] == c_right[:2]
    first_three_equal = c_left[:3] == c_right[:3]
    donor_differs = differs(donor_values)
    isolated = local_equal and donor_differs and first_three_equal
    _, b_words, _, direction = collision_response(cuts)
    hit = isolated and differs(b_words)
    next_cuts = left[tick + 1], right[tick + 1]
    radiation_echo = all(
        differs(lane_pair(next_cuts, stage, A, CORR))
        for stage in ("transported", "complete")
    )
    persistence = following_contact(next_cuts, b_words) if hit else None
    result.update(
        first_tick=tick, donor_x=donor_x, local_equal=local_equal,
        donor_differs=donor_differs, matter_equal=matter_equal,
        first_three_equal=first_three_equal, isolated=isolated, hit=hit,
        survives=hit and persistence["survives"], retains=hit and persistence["retains"],
        radiation_echo=radiation_echo,
        arrival={
            "bit": cuts[0].bit,
            "donor_pre_c_corr": word_pair(donor_values),
            "pre_c_cells": cell_pair(cuts, "before"),
            "post_c_cells": (c_left, c_right),
            "post_b_words": word_pair(b_words),
            "tags": tuple(cut.tags[A] for cut in cuts),
            "direction": direction,
            "following_contact": persistence,
        },
    )

    for conversion_tick in range(tick, tick + CONVERSION_WINDOW + 1):
        cuts = left[conversion_tick], right[conversion_tick]
        c_left, c_right = cell_pair(cuts, "transported")
        if c_left[:3] != c_right[:3] or c_left[CORR] == c_right[CORR]:
            continue
        _, b_words, moves, direction = collision_response(cuts)
        if not differs(b_words):
            continue
        left_tag, right_tag = (cut.tags[A] for cut in cuts)
        next_cuts = left[conversion_tick + 1], right[conversion_tick + 1]
        persistence = following_contact(next_cuts, b_words)
        result.update(
            conversion_tick=conversion_tick,
            conversion_left_tag=left_tag, conversion_right_tag=right_tag,
            conversion_left_moves=moves[0], conversion_right_moves=moves[1],
            conversion_survives=persistence["survives"],
            conversion_retains=persistence["retains"],
            conversion={
                "direction": direction,
                "post_c_cells": (c_left, c_right),
                "post_b_words": word_pair(b_words),
                "following_contact": persistence,
            },
        )
        break
    return result


def phase_report(steps):
    def z(field):
        return k.j_coefficients(k.subtract(field[A][R0], field[k.HEAD][R0]))

    path = [z(steps[1].before)]
    for cut in steps[1:ARRIVAL_HORIZON + 1]:
        path.extend((z(cut.transported), z(cut.complete)))
    result = phase.summarize(path)
    if result["continuous_complete"]:
        result.pop("components")
    else:
        result["local_totals"] = {
            name: sum(part[name] for part in result["components"])
            for name in ("ray_crossings", "signed_sector_displacement", "full_signed_turns")
        }
    return result


def paired_phase(left, right):
    if not left["continuous_complete"] or not right["continuous_complete"]:
        return None
    if left["initial_value"] != right["initial_value"]:
        raise AssertionError("paired phase needs a common initial value")
    crossings = left["ray_crossings"] - right["ray_crossings"]
    end_sector_delta = left["final_sector"] - right["final_sector"]
    branch_order = phase.sign(end_sector_delta) or phase.determinant_sign(
        right["final_value"], left["final_value"]
    )
    return {
        "sign": phase.sign(crossings) or branch_order,
        "ray_crossing_delta": crossings,
        "signed_sector_delta": end_sector_delta + 5 * crossings,
        "endpoint_branch_order": branch_order,
        "end_values": (left["final_value"], right["final_value"]),
    }


def run(cuts, arrivals):
    """Return four route rows per rank, with all three matched comparisons."""
    records = []
    if set(arrivals) != set(range(85)):
        raise AssertionError("expected all 85 fresh ranks")
    for rank, arrival in sorted(arrivals.items()):
        offset = (arrival - 1) % k.PERIOD
        if offset % 2 != 1:
            raise AssertionError(("predecessor bit", rank, offset))
        bare = cuts[offset]
        zero = trace(stock(bare), rank, 0, 0)
        zero_phase = phase_report(zero)
        for distance in range(1, 5):
            arms = {"zero": zero}
            for label, sign in (("plus", 1), ("minus", -1)):
                arms[label] = trace(stock(bare, distance, sign), rank, distance, sign)
            phase_arms = {
                "zero": zero_phase,
                "plus": phase_report(arms["plus"]),
                "minus": phase_report(arms["minus"]),
            }
            comparisons = {}
            for name, left, right in COMPARISONS:
                paired = compare(arms[left], arms[right], name, rank, distance)
                paired["phase"] = paired_phase(phase_arms[left], phase_arms[right])
                comparisons[name] = paired
            records.append({
                "rank": rank, "distance": distance, "predecessor_offset": offset,
                "source_x": (1 + distance) % 8,
                "accounts": {
                    label: k.reported_account(steps[1].before)
                    for label, steps in arms.items()
                },
                "phase_arms": phase_arms,
                "comparisons": comparisons,
            })
    return {
        "horizon": HORIZON,
        "arrival_horizon": ARRIVAL_HORIZON,
        "conversion_window": CONVERSION_WINDOW,
        "audited_native_steps": 85 * (1 + 2 * 4) * HORIZON,
        "records": records,
    }
