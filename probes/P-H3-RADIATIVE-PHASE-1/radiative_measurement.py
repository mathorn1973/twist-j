# SPDX-License-Identifier: Apache-2.0
"""Matched radiation-only phase measurement under the unchanged H3 law."""


def measurements(native):
    h3 = native.h3
    zero, one, rho, j_unit = h3.ZERO, h3.ONE, h3.RHO, h3.J
    j = h3.J_POWERS[1]
    u = h3.add(j, h3.J_POWERS[4])
    u_inverse = h3.mul(j, h3.J_INV)
    four = h3.scale(4, one)
    length = h3.sub(one, rho)
    near, far, target, reference = (1, 1), (5, 1), (2, 1), (2, 3)
    reference_words = length, h3.scale(-1, length), zero, zero
    accounts = zero, zero, (648, 0, -4, -4), 1300

    def launch(high):
        field = native.empty()
        units = (u_inverse, u) if high else (u, u_inverse)
        for columns, unit in zip(((0, 1), (4, 5)), units):
            gap = h3.scale(4, unit)
            words = gap, h3.scale(-1, gap), four, h3.scale(-1, four)
            for x in columns:
                for y in (0, 1):
                    native.put(field, x, y, words)
        for site in (target, reference):
            native.put(field, *site, reference_words)
        return tuple(field)

    def step(field, bit):
        post_c, post_b, events = native.step(field, bit)
        h3.require(all(native.ledger(cut) == accounts for cut in (field, post_c, post_b)),
                   "full radiation measurement ledger")
        h3.require(tuple(native.reverse(post_b, bit)) == field, "full inverse")
        return post_c, post_b, events

    def read(before, cuts, high):
        post_c, post_b, events = cuts
        unit = h3.J_INV if high else j_unit
        incoming_gap = h3.mul(length, unit)
        receipt = h3.scale(-2, incoming_gap)
        expected_corr = h3.scale(-4, unit)

        h3.require(native.cell(before, *target) == reference_words, "fixed whole pre-C receiver")
        h3.require(native.cell(before, *near)[3] == expected_corr, "exact source CORR word")
        h3.require(h3.even(expected_corr), "horizontal CORR contact admits")
        incoming = native.cell(post_c, *target)
        h3.require(incoming == (*reference_words[:3], receipt),
                   "only incoming CORR differs at the fixed matter receiver")

        tag = next((code for x, y, code in events if (x, y) == target), 0)
        outgoing = native.cell(post_b, *target)
        expected_tag = 2 if high else 1
        h3.require(tag == expected_tag, "radiation-selective native B branch")
        h3.require(outgoing[:2] == (incoming_gap, h3.scale(-1, incoming_gap))
                   and outgoing[:2] != incoming[:2], "exact measured material write")
        h3.require(all(native.cell(cut, *reference) == reference_words for cut in cuts[:2]),
                   "common reference remains fixed")
        h3.require(h3.mul(unit, length) == outgoing[0], "exact target/reference ratio")
        return {"post_c": incoming, "post_b": outgoing, "tag": tag,
                "reference": native.cell(post_b, *reference), "ratio": unit}

    def swap_corr(field):
        result = list(field)
        first, second = native.ix(*near, 3), native.ix(*far, 3)
        result[first], result[second] = result[second], result[first]
        return tuple(result)

    live, swapped = {}, {}
    for high, name in ((False, "low"), (True, "high")):
        initial = launch(high)
        t1c, t1b, t1events = step(initial, 0)
        h3.require(t1c == initial, "first matching fixes all prepared tiles and test pairs")
        h3.require(all(native.cell(t1b, *site) == reference_words for site in (target, reference)),
                   "first tick leaves test and reference unchanged")
        expected_source_tag = 1 if high else 2
        h3.require((*near, expected_source_tag) in t1events, "exact original source tag")
        t2 = step(t1b, 1)
        live[name] = read(t1b, t2, high)
        h3.require(tuple(native.reverse(native.reverse(t2[1], 1), 0)) == initial,
                   "whole live two-tick inverse")

        intervention = swap_corr(t1b)
        changed = tuple(index for index, (a, b) in enumerate(zip(t1b, intervention)) if a != b)
        h3.require(changed == (native.ix(*near, 3), native.ix(*far, 3)),
                   "the reciprocal intervention changes only two CORR rails")
        counterfactual = step(intervention, 1)
        swapped[name] = read(intervention, counterfactual, not high)
        recovered = swap_corr(native.reverse(counterfactual[1], 1))
        h3.require(recovered == t1b and tuple(native.reverse(recovered, 0)) == initial,
                   "whole two-tick inverse including reciprocal CORR swap")

    h3.require(swapped["high"] == live["low"] and swapped["low"] == live["high"],
               "both interventions switch the complete local measured response")
    relative = h3.mul(live["low"]["ratio"], j_unit)
    h3.require(relative == h3.mul(rho, h3.T)
               and h3.mul(relative, live["high"]["ratio"]) == live["low"]["ratio"],
               "relative phase contrast is rho with positive factor theta")
    return {
        "ledger": accounts,
        "source_site": near,
        "other_source_site": far,
        "target_site": target,
        "reference_site": reference,
        "live": live,
        "reciprocal_corr_only": swapped,
        "low_ratio_divided_by_high_ratio": relative,
    }
