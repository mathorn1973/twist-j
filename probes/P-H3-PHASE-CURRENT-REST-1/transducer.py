# SPDX-License-Identifier: Apache-2.0
"""A native source, material phase reader and horizontal radiation export."""

from native import cell, empty, h3, ledger, put, reverse, step


ZERO, ONE = h3.ZERO, h3.ONE
J, J_INV, RHO, THETA = h3.J, h3.J_INV, h3.RHO, h3.T
j, j_inv = h3.J_POWERS[1], h3.J_POWERS[4]
TWO = h3.scale(2, ONE)
UNIT = h3.add(j, j_inv)
UNIT_INV = h3.mul(j, J_INV)
SOURCE, READER, EXPORT = (1, 1), (1, 2), (2, 1)
READ_GAP = h3.scale(2, j)
READ_RADIATION = ONE, h3.sub(ONE, h3.scale(4, J))


def fill_tile(field, columns, rows, words):
    for x in columns:
        for y in rows:
            put(field, x, y, words)


def source_tile(unit):
    d = h3.scale(2, unit)
    return d, h3.scale(-1, d), TWO, h3.scale(-1, TWO)


def prepare(high, receiver_launch):
    field = empty()
    near, far = (UNIT_INV, UNIT) if high else (UNIT, UNIT_INV)
    fill_tile(field, (0, 1), (0, 1), source_tile(near))
    fill_tile(field, (4, 5), (0, 1), source_tile(far))
    fill_tile(field, (0, 1), (2, 3), receiver_launch)
    return tuple(field)


def matter_gap(words):
    return h3.half(h3.sub(words[0], words[1]))


def matter_center(words):
    return h3.half(h3.add(words[0], words[1]))


def site_q(words):
    return h3.scalar_account(h3.ring_sum(map(h3.h, words)))


def golden_coefficient(real_word):
    return -real_word[2]


def source_coefficients(before, after):
    return {
        "matter_before": golden_coefficient(h3.ring_sum(map(h3.h, before[:2]))),
        "radiation_before": golden_coefficient(h3.ring_sum(map(h3.h, before[2:]))),
        "matter_after": golden_coefficient(h3.ring_sum(map(h3.h, after[:2]))),
        "radiation_after": golden_coefficient(h3.ring_sum(map(h3.h, after[2:]))),
    }


def tag(events, site):
    return next((code for x, y, code in events if (x, y) == site), 0)


def check_receive(previous, stages, gap, expected_tag):
    post_c, post_b, events = stages
    source, reader = cell(previous, *SOURCE), cell(previous, *READER)
    h3.require(all(h3.even(h3.sub(source[i], reader[i])) for i in range(2)),
               "both incoming material contacts admit")
    h3.require(h3.even(source[2]) and not h3.even(reader[2]),
               "common CLK parity refusal")
    h3.require(not h3.even(reader[3]) and cell(previous, 2, 2)[3] == ZERO,
               "common CORR parity refusal")

    incoming = cell(post_c, *READER)
    final = cell(post_b, *READER)
    expected = h3.half(h3.add(h3.mul(J, READ_GAP), h3.mul(h3.sub(ONE, RHO), gap)))
    h3.require(matter_gap(incoming) == expected, "exact received material word")
    expected_norm = h3.scale(4, ONE) if gap == READ_GAP else (1, 0, -1, -1)
    h3.require(h3.h(expected) == expected_norm, "exact phase-sensitive norm")
    h3.require(incoming[2:] == READ_RADIATION, "radiation-identical receiver")
    h3.require(h3.half(h3.sub(*incoming[2:])) == h3.scale(2, J), "common field half-gap")
    h3.require(tag(events, READER) == expected_tag, "incorrect receiving decision")
    h3.require((final[:2] != incoming[:2]) == (expected_tag == 1), "actual reader write")
    return {"post_c": incoming, "post_b": final, "tag": expected_tag}


def check_export(previous, post_c):
    donor_corr = cell(previous, *SOURCE)[3]
    h3.require(cell(previous, *EXPORT) == (ZERO,) * 4, "initially empty export site")
    h3.require(h3.even(donor_corr), "export contact admits")
    expected = h3.mul(h3.sub(ONE, RHO), h3.half(donor_corr))
    received = cell(post_c, *EXPORT)
    h3.require(expected != ZERO and received == (ZERO, ZERO, ZERO, expected),
               "exact horizontal radiation receipt")
    return received[3]


def audited_step(field, bit, expected):
    cuts = step(field, bit)
    h3.require(all(ledger(cut) == expected for cut in (field, *cuts[:2])),
               "funded source-to-reader ledger")
    h3.require(tuple(reverse(cuts[1], bit)) == field, "exact tick inversion")
    h3.require(all(matter_center(cell(cut, x, y)) == ZERO
                   for cut in (field, *cuts[:2]) for x in range(8) for y in range(4)),
               "matter pair remains antipodal with zero species current")
    return cuts


def check_source(launch, first, high):
    post_c, post_b, events = first
    incoming, emitted = cell(post_c, *SOURCE), cell(post_b, *SOURCE)
    d, f = matter_gap(incoming), TWO
    dn, fn = matter_gap(emitted), h3.half(h3.sub(*emitted[2:]))
    source_tag, gap, field_unit = ((1, h3.scale(2, j), J_INV) if high
                                   else (2, h3.scale(2, j_inv), J))
    h3.require(incoming == cell(launch, *SOURCE) and tag(events, SOURCE) == source_tag,
               "exact first native source branch")
    h3.require(emitted == (gap, h3.scale(-1, gap), h3.mul(f, field_unit),
                           h3.scale(-1, h3.mul(f, field_unit))), "exact emitted cell")
    kick_unit = J if high else J_INV
    h3.require(h3.mul(d, f) == h3.mul(dn, fn), "source gap product conserved")
    h3.require(h3.mul(dn, f) == h3.mul(h3.mul(kick_unit, kick_unit), h3.mul(d, fn)),
               "opposite native relative phase kicks")
    return d, dn, source_tag


def run():
    h3.require(h3.conj(UNIT) == UNIT and h3.conj(UNIT_INV) == UNIT_INV
               and h3.mul(UNIT, UNIT_INV) == ONE, "same real sign in each embedding")
    # phi = -(rho + rho^-1); its coefficient in a real word is -word[2].
    phi = h3.scale(-1, h3.add(RHO, h3.RHO_INV))
    low_norm = h3.sub(h3.scale(8, ONE), h3.scale(4, phi))
    high_norm = h3.add(h3.scale(4, ONE), h3.scale(4, phi))
    h3.require(low_norm == h3.scale(4, THETA)
               and h3.mul(high_norm, THETA) == h3.scale(4, ONE),
               "opposite golden source coefficients")
    desired = READ_GAP, h3.scale(-1, READ_GAP), *READ_RADIATION
    receiver_launch, inverse_tag = h3.collision(desired)
    h3.require(inverse_tag == 1, "chosen receiver inverse")
    launches = {high: prepare(high, receiver_launch) for high in (False, True)}
    expected = ledger(launches[False])
    h3.require(expected == (ZERO, (-8, 0, -16, 0), (296, 0, 48, 48), 544),
               "declared complete source accounts")
    for x in range(8):
        for y in range(4):
            low, high = (cell(launches[arm], x, y) for arm in (False, True))
            h3.require(low[2:] == high[2:] and site_q(low) == site_q(high),
                       "identical initial site Q and radiation")

    first = {high: audited_step(launch, 0, expected) for high, launch in launches.items()}
    h3.require(all(first[high][0] == launches[high] for high in (False, True)),
               "first C leaves the prepared tiles fixed")
    summaries = {}
    for high, name, norm in ((False, "low", low_norm), (True, "high", high_norm)):
        _, post_b, events = first[high]
        h3.require(cell(post_b, *READER) == desired and tag(events, READER) == 2,
                   "same receiver prepared by first native B")
        d, dn, source_tag = check_source(launches[high], first[high], high)
        h3.require(h3.h(d) == norm and site_q(cell(launches[high], *SOURCE)) == 40,
                   "equal traced local source Q and distinct Hermitian account")
        second = audited_step(post_b, 1, expected)
        h3.require(reverse(reverse(second[1], 1), 0) == launches[high],
                   "complete live two-tick inverse")
        coefficients = source_coefficients(cell(first[high][0], *SOURCE), cell(post_b, *SOURCE))
        signed = 8 if high else -8
        h3.require(coefficients == {
            "matter_before": signed, "radiation_before": 0,
            "matter_after": 0, "radiation_after": signed,
        }, "signed source coefficient transferred from material to radiation")
        live = check_receive(post_b, second, dn, 1 if high else 0)
        receipt = check_export(post_b, second[0])
        receipt_norm = h3.h(receipt)
        receipt_coefficient = golden_coefficient(receipt_norm)
        h3.require(receipt_coefficient == (4 if high else -1),
                   "exact golden coefficient at horizontal export")

        other = cell(first[not high][1], *SOURCE)
        substituted = list(post_b)
        put(substituted, *SOURCE, (*other[:2], *cell(post_b, *SOURCE)[2:]))
        swapped_start = tuple(substituted)
        swapped = audited_step(swapped_start, 1, expected)
        recovered = list(reverse(swapped[1], 1))
        original_writer = cell(post_b, *SOURCE)
        put(recovered, *SOURCE, (*original_writer[:2], *cell(recovered, *SOURCE)[2:]))
        h3.require(tuple(recovered) == post_b and reverse(recovered, 0) == launches[high],
                   "complete reciprocal two-tick inverse with inverse word swap")
        alternative = check_receive(swapped_start, swapped, matter_gap(other), 0 if high else 1)
        h3.require(check_export(swapped_start, swapped[0]) == receipt,
                   "material-only substitution preserves contemporaneous radiation receipt")
        summaries[name] = {
            "initial_gap": d,
            "initial_gap_norm": norm,
            "golden_coefficient": golden_coefficient(norm),
            "source_tag": source_tag,
            "emitted_gap": dn,
            "live_reader": live,
            "reciprocal_word_only_reader": alternative,
            "source_golden_coefficients": coefficients,
            "horizontal_receipt": receipt,
            "horizontal_receipt_norm": receipt_norm,
            "horizontal_receipt_golden_coefficient": receipt_coefficient,
        }

    low, high = summaries["low"], summaries["high"]
    h3.require(low["horizontal_receipt"] != high["horizontal_receipt"],
               "distinct exported radiation words")
    h3.require(h3.add(low["horizontal_receipt"], high["horizontal_receipt"]) != ZERO,
               "exported radiation words are not additive negatives")
    for actual, counterpart in ((low, high), (high, low)):
        h3.require(actual["reciprocal_word_only_reader"] == counterpart["live_reader"],
                   "reciprocal substitutions reproduce exact opposite receiver endpoints")
    return {
        "ledger": expected,
        "initial_site_Q_matched": True,
        "source_site_Q": 40,
        "matter_species_current_zero": True,
        "source_site": SOURCE,
        "receiver_site": READER,
        "horizontal_receipt_site": EXPORT,
        "arms": summaries,
    }
