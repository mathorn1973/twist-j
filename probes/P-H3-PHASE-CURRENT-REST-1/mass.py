# SPDX-License-Identifier: Apache-2.0
"""Exact matter-sector multipliers and equal-ledger transport contrasts."""

from native import cell, empty, h3, ledger, put, reverse, step


ZERO, ONE, RHO = h3.ZERO, h3.ONE, h3.RHO
NEG_ONE = h3.scale(-1, ONE)
RHO2 = h3.mul(RHO, RHO)
MATTER_X, REF_X, REF_Y = 0, 4, 0
MODES = {
    "uniform": ((ONE, ONE, ONE, ONE), (ONE, ONE), ONE),
    "staggered": ((ONE, NEG_ONE, ONE, NEG_ONE), (RHO, RHO), RHO2),
    "cell_antiperiodic": ((ONE, ONE, NEG_ONE, NEG_ONE), (ONE, RHO), RHO),
}


def antipodal(word):
    return word, h3.scale(-1, word), ZERO, ZERO


def launch(profile, reference):
    field = empty()
    for y, word in enumerate(profile):
        put(field, MATTER_X, y, antipodal(word))
    if reference:
        put(field, REF_X, REF_Y, (ZERO, ZERO, ZERO, ONE))
    return field


def pointwise_account(field):
    return tuple(
        h3.ring_sum(h3.h(word) for word in cell(field, x, y))
        for x in range(8)
        for y in range(4)
    )


def expect_cut(observed, expected, local, accounts, label):
    h3.require(tuple(observed) == tuple(expected), f"{label}: complete field")
    h3.require(pointwise_account(observed) == local, f"{label}: pointwise H")
    h3.require(ledger(observed) == accounts, f"{label}: complete ledger")


def audit_mode(name, profile, factors, multiplier, reference):
    initial = launch(profile, reference)
    local = pointwise_account(initial)
    accounts = ledger(initial)
    h3.require(
        accounts == (ZERO, ONE if reference else ZERO, h3.scale(8 + reference, ONE),
                     16 + 2 * reference),
        "mode launch ledger",
    )
    current = initial
    phase = ONE
    even_phases = [ONE]
    snapshots = [tuple(initial)]
    for tick in range(10):
        bit = tick % 2
        post_c, complete, events = step(current, bit)
        phase = h3.mul(factors[bit], phase)
        expected = launch(tuple(h3.mul(phase, value) for value in profile), reference)
        label = f"{name}, reference={reference}, tick={tick + 1}"
        expect_cut(post_c, expected, local, accounts, f"{label} C")
        expect_cut(complete, expected, local, accounts, f"{label} B")
        if reference:
            archive = cell(complete, MATTER_X, 0)[0]
            anchor = cell(complete, REF_X, REF_Y)[3]
            # With the fixed anchor, the off-diagonal / diagonal projector
            # ratio recovers the relative word; the common denominator cancels.
            ratio = h3.mul(
                h3.mul(archive, h3.conj(anchor)), h3.inverse(h3.h(anchor))
            )
            h3.require(ratio == h3.mul(phase, profile[0]), f"{label}: anchored ratio")
        h3.require(not any(events), f"{label}: B idle")
        h3.require(tuple(reverse(complete, bit)) == tuple(current), f"{label}: inverse")
        if bit == 1:
            h3.require(phase == h3.mul(multiplier, even_phases[-1]), f"{label}: multiplier")
            even_phases.append(phase)
        snapshots.append(tuple(complete))
        current = complete

    state_period = 2 if multiplier == ONE else 10
    h3.require(tuple(current) == tuple(initial), f"{name}: return at ten ticks")
    h3.require(
        next(t for t in (2, 4, 6, 8, 10) if snapshots[t] == snapshots[0]) == state_period,
        f"{name}: minimal phase-bit period",
    )
    h3.require(
        len(set(even_phases[:-1])) == (1 if multiplier == ONE else 5),
        f"{name}: order of the multiplier",
    )
    return accounts, local, state_period


def audit_antiperiodic_symbol():
    # The admitted contact is [[A,D],[D,A]], where 2A=1+rho and 2D=1-rho.
    # At z=-1, the second block switches both D signs. Verify the product
    # as a linear operator by testing its scaled columns in the integer ring.
    twice_a, twice_d = h3.add(ONE, RHO), h3.sub(ONE, RHO)
    a_squared = h3.mul(twice_a, twice_a)
    d_squared = h3.mul(twice_d, twice_d)
    diagonal = h3.sub(a_squared, d_squared)
    off_diagonal = h3.sub(h3.mul(twice_a, twice_d), h3.mul(twice_d, twice_a))
    h3.require(diagonal == h3.scale(4, RHO) and off_diagonal == ZERO, "F(-1)=rho I")

    # For any a=b mod 2, C0 admits and returns (u,v,-u,-v).
    # Since u+v=a+b is even, the C1 pairs (v,-u) and (-v,u) also admit.
    # After C1 the same parity condition is preserved by multiplication by rho.
    # Test a nontrivial ring-valued witness with equal residues and differing words.
    a = h3.add(ONE, h3.scale(2, RHO))
    b = h3.add(ONE, h3.scale(-2, RHO2))
    initial = launch((a, b, h3.scale(-1, a), h3.scale(-1, b)), False)
    c0, b0, events0 = step(initial, 0)
    u, v = h3.transport_pair(a, b, False)
    h3.require(h3.even(h3.sub(a, b)) and h3.even(h3.add(u, v)), "guard at both matchings")
    expected_c0 = launch((u, v, h3.scale(-1, u), h3.scale(-1, v)), False)
    h3.require(tuple(c0) == tuple(b0) == tuple(expected_c0) and not any(events0), "C0 profile")
    c1, b1, events1 = step(b0, 1)
    expected_c1 = launch(
        tuple(h3.mul(RHO, word) for word in (a, b, h3.scale(-1, a), h3.scale(-1, b))),
        False,
    )
    h3.require(tuple(c1) == tuple(b1) == tuple(expected_c1) and not any(events1), "C1 profile")
    h3.require(ledger(c0) == ledger(c1) == ledger(initial), "ring witness ledger")
    h3.require(tuple(reverse(b1, 1)) == tuple(b0), "ring witness C1 inverse")
    h3.require(tuple(reverse(b0, 0)) == tuple(initial), "ring witness C0 inverse")


def audit_spread():
    frozen, mobile = empty(), empty()
    for x in range(4):
        put(frozen, x, 0, antipodal(ONE))
    put(mobile, MATTER_X, 0, antipodal(h3.scale(2, ONE)))
    accounts = ledger(frozen)
    h3.require(accounts == (ZERO, ZERO, h3.scale(8, ONE), 16), "spread launch ledger")
    h3.require(ledger(mobile) == accounts, "equal ledger across transport preparations")
    for bit in (0, 1):
        post_c, complete, events = step(frozen, bit)
        h3.require(
            tuple(post_c) == tuple(complete) == tuple(frozen) and not any(events),
            "both frozen matching parities refuse",
        )
        h3.require(tuple(reverse(complete, bit)) == tuple(frozen), "frozen inverse")
    post_c, complete, events = step(mobile, 0)
    expected = empty()
    put(expected, MATTER_X, 0, antipodal(h3.add(ONE, RHO)))
    put(expected, MATTER_X, 1, antipodal(h3.sub(ONE, RHO)))
    h3.require(tuple(post_c) == tuple(complete) == tuple(expected) and not any(events), "spread")
    h3.require(ledger(post_c) == ledger(complete) == accounts, "spread ledger")
    h3.require(tuple(reverse(complete, 0)) == tuple(mobile), "spread inverse")


def run():
    periods = {}
    for reference in (False, True):
        common = None
        for name, (profile, factors, multiplier) in MODES.items():
            accounts, local, period = audit_mode(name, profile, factors, multiplier, reference)
            if common is None:
                common = accounts, local
            h3.require((accounts, local) == common, "common full and pointwise mode accounts")
            periods[name] = period
    audit_antiperiodic_symbol()
    audit_spread()
    return {
        "matter_modes": {
            name: {"two_tick_multiplier_j_coordinates": data[2], "phase_bit_period": periods[name]}
            for name, data in MODES.items()
        },
        "mode_preparations": 6,
        "ticks_per_mode_preparation": 10,
        "mode_Q": 16,
        "mode_Q_with_fixed_reference": 18,
        "equal_ledger_occupied_sites_before_after": [[4, 4], [1, 2]],
    }
