# SPDX-License-Identifier: Apache-2.0
"""Exact projected currents and a matter-sign symmetry of native H3."""

from native import cell, empty, h3, ix, ledger, put, reverse, step
from phase import build


NX, NY = 8, 4
ZERO = h3.ZERO
RHO = h3.RHO
RHO2 = h3.mul(RHO, RHO)
ONE_MINUS_RHO = h3.sub(h3.ONE, RHO)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ell(value):
    return value[3] - value[1]


def residue(value):
    return sum(value) % 5


def edge_current(first, second):
    difference = h3.sub(first, second)
    if any(coefficient % 2 for coefficient in difference):
        return ZERO
    midpoint_difference = tuple(coefficient // 2 for coefficient in difference)
    return h3.mul(ONE_MINUS_RHO, midpoint_difference)


def species(cell_value, group):
    start = 2 * group
    return h3.add(cell_value[start], cell_value[start + 1])


def sign_flip(field):
    transformed = empty()
    for x in range(NX):
        for y in range(NY):
            r0, r2, clk, corr = cell(field, x, y)
            put(transformed, x, y, (h3.scale(-1, r2), h3.scale(-1, r0), clk, corr))
    return tuple(transformed)


def oriented_edges(bit):
    for rail in range(4):
        if rail == 3:
            for x in range(bit, NX, 2):
                for y in range(NY):
                    yield rail, (x, y), ((x + 1) % NX, y)
        else:
            for x in range(NX):
                for y in range(bit, NY, 2):
                    yield rail, (x, y), (x, (y + 1) % NY)


def check_continuity(before, post_c, post_b, bit):
    sites = {(x, y): [ZERO, ZERO] for x in range(NX) for y in range(NY)}
    for rail, first, second in oriented_edges(bit):
        i, k = ix(*first, rail), ix(*second, rail)
        current = edge_current(before[i], before[k])
        require(residue(current) == 0, "Current escapes the cyclotomic ideal")
        require(post_c[i] == h3.sub(before[i], current), "Wrong outgoing rail current")
        require(post_c[k] == h3.add(before[k], current), "Wrong incoming rail current")
        group = rail // 2
        sites[first][group] = h3.sub(sites[first][group], current)
        sites[second][group] = h3.add(sites[second][group], current)

    for site, net_inflow in sites.items():
        initial, transported, collided = (cell(field, *site) for field in (before, post_c, post_b))
        for group in range(2):
            old, after_c, after_b = (species(value, group) for value in (initial, transported, collided))
            require(after_c == after_b, "A collision changes a local species sum")
            require(after_b == h3.add(old, net_inflow[group]), "Native continuity fails")
            require(ell(after_b) - ell(old) == ell(net_inflow[group]), "Integer continuity fails")
            require(residue(old) == residue(after_b), "A local mod-5 species residue moves")


def first_tick_currents(field):
    result = []
    for x in range(5):
        first, second = cell(field, x, 0), cell(field, x, 1)
        current = h3.add(edge_current(first[0], second[0]), edge_current(first[1], second[1]))
        result.append(ell(current))
    return result


def run():
    # Every C matching treats the two matter rails identically. Simultaneous
    # negation and interchange therefore commute with C, including parity.
    # At B the same transformation sends the matter center to its negative
    # and leaves the matter difference and both radiation registers fixed.
    # It preserves the branch, the updated difference and the event tag.
    # The matching bit is also fixed, so the symmetry holds at every tick.
    centers = (RHO2, h3.ONE, h3.scale(-1, RHO2))
    primitive = tuple(ell(edge_current(h3.scale(2 * sign, RHO2), ZERO)) for sign in (1, -1))
    require(primitive == (1, -1), "The selected projection is not primitive on these active edges")

    first_tick = {"plus": [], "neutral": [], "minus": []}
    checked_full_ticks = 0
    active_b = {"plus": 0, "neutral": 0, "minus": 0}
    for code in range(5):
        # The neutral control has a nonzero ring center whose projection is zero.
        fields = [tuple(build(code, center)) for center in centers]
        for name, field, expected in zip(first_tick, fields, (2, 0, -2)):
            currents = first_tick_currents(field)
            require(currents == [expected] * 5, "Unexpected projected current on the first matching")
            first_tick[name].append(currents)
        require(sign_flip(fields[0]) == fields[2], "Prepared signs are not related by the full symmetry")
        starting_ledgers = [ledger(field) for field in fields]
        for tick in range(85):
            bit = tick % 2
            cuts = [step(field, bit) for field in fields]
            for index, (name, old, (post_c, post_b, events)) in enumerate(zip(first_tick, fields, cuts)):
                check_continuity(old, post_c, post_b, bit)
                require(ledger(post_c) == starting_ledgers[index], "Post-C native ledger changed")
                require(ledger(post_b) == starting_ledgers[index], "Full native ledger changed")
                require(tuple(reverse(post_b, bit)) == old, "Complete native inverse failed")
                active_b[name] += len(events)
                checked_full_ticks += 1

            plus_c, plus_b, plus_events = cuts[0]
            minus_c, minus_b, minus_events = cuts[2]
            require(sign_flip(plus_c) == tuple(minus_c), "Post-C symmetry broken")
            require(sign_flip(plus_b) == tuple(minus_b), "Full-step symmetry broken")
            require(plus_events == minus_events, "The collision records distinguish the opposite signs")
            for left, right in ((plus_c, minus_c), (plus_b, minus_b)):
                require(
                    all(cell(left, x, y)[2:] == cell(right, x, y)[2:] for x, y in oriented_sites()),
                    "A radiation coordinate distinguishes the opposite signs",
                )
            fields = [tuple(cut[1]) for cut in cuts]

    require(active_b["plus"] > 0, "The sign comparison contains no active B collisions")
    return {
        "primitive_projected_edge_currents": list(primitive),
        "first_tick_all_five_edges_for_each_code": first_tick,
        "checked_native_full_ticks": checked_full_ticks,
        "active_b_events_by_preparation": active_b,
        "matter_and_radiation_continuity": True,
        "site_mod5_residues_frozen": True,
        "signed_pair_radiation_and_collision_records_identical": True,
        "radiation_only_sign_reader_excluded_on_signed_pairs": True,
    }


def oriented_sites():
    return ((x, y) for x in range(NX) for y in range(NY))
