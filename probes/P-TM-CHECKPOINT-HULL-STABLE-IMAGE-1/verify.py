#!/usr/bin/env python3
"""Exact accepted audit for P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1.

Standard library only. Exact integer arithmetic. No file, network, subprocess,
clock, random, or external scientific input. Public claim lock #780 is
embedded as an integrity constant.
"""

import itertools
import os
import sys


PROBE_ID = "P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1"
TARGET_CLAIM = "TM-CHECKPOINT-HULL-STABLE-IMAGE"
CLAIM_LOCK = "#780"
BASE_COMMIT = "8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9"
CANON_TAG = "canon-v74"
CONTENT_COMMIT = "2561f7dcadcbbf683ce7b36219ea67378d879a5a"
CANON_SHA256 = (
    "2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e"
)
REQUIRED_ENVIRONMENT = (
    ("LC_ALL", "C"),
    ("LANG", "C"),
    ("PYTHONDONTWRITEBYTECODE", "1"),
    ("PYTHONHASHSEED", "0"),
    ("TZ", "UTC"),
)

MOD = 5
S_C = (2, 1, 2, 1)
U_C = (0, 1, 0, 4)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)
WSTAR = "10100101"
REGISTERED_FACTOR_COUNTS = (
    2, 4, 6, 10, 12, 16, 20, 22,
    24, 28, 32, 36, 40, 42, 44, 46,
)


class Stop(Exception):
    """Integrity stop: no scientific decision."""


class Falsified(Exception):
    """Exact counterexample to a frozen scientific audit gate."""


LINES = []


def emit(line):
    LINES.append(line)


def gate(tag, condition, detail):
    if not condition:
        raise Falsified(tag + " " + detail)
    emit(tag + " " + detail + ": PASS")


def g_a(state):
    p1, p4, p1p, p4p, q, r = state
    return (p4, p1, p4p, p1p, q, r)


def g_b(state):
    p1, p4, p1p, p4p, q, r = state
    return (
        (-p1p) % MOD,
        (-p4p) % MOD,
        (-p1) % MOD,
        (-p4) % MOD,
        (-q) % MOD,
        (-r) % MOD,
    )


def g_c(state):
    p1, p4, p1p, p4p, q, r = state
    b4 = ((-p1p) % MOD, (-p4p) % MOD,
          (-p1) % MOD, (-p4) % MOD)
    piston = tuple(
        (b4[index] + S_C[index] + r * U_C[index]) % MOD
        for index in range(4)
    )
    return piston + ((1 - q) % MOD, (-r) % MOD)


def g_d(state):
    return tuple((C_D[index] - state[index]) % MOD for index in range(6))


def g_e(state):
    centre = tuple((C_D[index] + V_E[index]) % MOD for index in range(6))
    return tuple((centre[index] - state[index]) % MOD for index in range(6))


GENERATORS = (g_a, g_b, g_c, g_d, g_e)


def z6(state):
    return sum(state) % MOD


def substitute(word):
    return "".join("01" if symbol == "0" else "10" for symbol in word)


def factors(word, length):
    return {
        word[index:index + length]
        for index in range(len(word) - length + 1)
    }


class Window:
    """Finite exact chart for the local two-sided hull identities."""

    __slots__ = ("lo", "bits")

    def __init__(self, lo, bits):
        self.lo = lo
        self.bits = tuple(bits)

    def at(self, index):
        offset = index - self.lo
        if offset < 0 or offset >= len(self.bits):
            raise Stop("WINDOW_ACCESS_OUTSIDE_FROZEN_CHART")
        return self.bits[offset]

    def __eq__(self, other):
        return (
            isinstance(other, Window)
            and self.lo == other.lo
            and self.bits == other.bits
        )


def shift_k(window):
    return Window(window.lo - 1, window.bits)


def unshift_k(window):
    return Window(window.lo + 1, window.bits)


def rho(window):
    high = window.lo + len(window.bits)
    return Window(-high, reversed(window.bits))


def h_leaf(window):
    return (4 + 2 * window.at(-1)) % MOD


def i_stab(window):
    return (4 + 2 * (window.at(-1) + window.at(0))) % MOD


def v_hull(window, state):
    selector = (z6(state) + 2 * window.at(0)) % MOD
    return shift_k(window), GENERATORS[selector](state)


def inverse_stab(window, state):
    previous = unshift_k(window)
    return previous, GENERATORS[i_stab(previous)](state)


def r_cp(window, state):
    return rho(window), GENERATORS[i_stab(window)](state)


def audit():
    emit(PROBE_ID + " exact L1 audit")
    emit("target claim=" + TARGET_CLAIM)
    emit("authority=" + CANON_TAG + " base=" + BASE_COMMIT)
    emit("content commit=" + CONTENT_COMMIT)
    emit("canon sha256=" + CANON_SHA256)

    if len(sys.argv) != 1:
        raise Stop("I01 ARGUMENTS")
    if CLAIM_LOCK != "#780":
        raise Stop("I01 UNRESOLVED_CLAIM_LOCK")
    for key, expected in REQUIRED_ENVIRONMENT:
        if os.environ.get(key) != expected:
            raise Stop("I01 ENVIRONMENT_" + key)
    emit("I01 identity arguments=0 environment=5 claim-lock-resolved: PASS")

    states = list(itertools.product(range(MOD), repeat=6))
    leaves = {
        value: [state for state in states if z6(state) == value]
        for value in range(MOD)
    }
    leaf_sets = {value: frozenset(leaves[value]) for value in range(MOD)}

    involutions = all(
        generator(generator(state)) == state
        for generator in GENERATORS
        for state in states
    )
    bc_order = True
    for state in states:
        current = state
        for _ in range(5):
            current = g_c(g_b(current))
        if current != state:
            bc_order = False
            break

    trace_laws = (
        lambda value: value % MOD,
        lambda value: (-value) % MOD,
        lambda value: (2 - value) % MOD,
        lambda value: (2 - value) % MOD,
        lambda value: (3 - value) % MOD,
    )
    traces = all(
        z6(GENERATORS[index](state)) == trace_laws[index](z6(state))
        for index in range(5)
        for state in states
    )
    sheet_maps = {
        bit: tuple(
            trace_laws[(value + 2 * bit) % MOD](value)
            for value in range(MOD)
        )
        for bit in (0, 1)
    }
    expected_maps = {
        0: (0, 4, 0, 4, 4),
        1: (2, 1, 1, 3, 1),
    }
    gate(
        "C01",
        involutions and bc_order and traces and sheet_maps == expected_maps,
        "generators involutions (bc)^5 trace-laws sheet-maps",
    )

    arrows = True
    for bit in (0, 1):
        for source in range(MOD):
            selector = (source + 2 * bit) % MOD
            target = sheet_maps[bit][source]
            image = frozenset(
                GENERATORS[selector](state) for state in leaves[source]
            )
            if image != leaf_sets[target] or len(image) != 3125:
                arrows = False
    gate("C02", arrows, "all-ten-sheet-arrows full-leaf-bijections")

    word_sub = "0"
    for _ in range(18):
        word_sub = substitute(word_sub)
    word_popcount = "".join(
        str(index.bit_count() & 1) for index in range(1 << 18)
    )
    factor_sets = {}
    factor_counts = []
    finite_reversal = True
    for length in range(1, 17):
        current_factors = factors(word_sub, length)
        factor_sets[length] = current_factors
        factor_counts.append(len(current_factors))
        finite_reversal = finite_reversal and {
            factor[::-1] for factor in current_factors
        } == current_factors

    even_dyadic_palindromes = True
    for exponent in range(2, 19, 2):
        block = word_sub[:1 << exponent]
        if block != block[::-1]:
            even_dyadic_palindromes = False
            break
    gate(
        "L01",
        word_sub == word_popcount
        and tuple(factor_counts) == REGISTERED_FACTOR_COUNTS
        and finite_reversal
        and even_dyadic_palindromes,
        "substitution-popcount factor-counts finite-reversal dyadic-audit",
    )

    branch_table = []
    stable_arrows = True
    for previous in (0, 1):
        for current in (0, 1):
            selector = (4 + 2 * (previous + current)) % MOD
            branch_table.append(selector)
            source = (4 + 2 * previous) % MOD
            target = (4 + 2 * current) % MOD
            image = frozenset(
                GENERATORS[selector](state) for state in leaves[source]
            )
            if image != leaf_sets[target]:
                stable_arrows = False
            if any(
                (z6(state) + 2 * current) % MOD != selector
                for state in leaves[source]
            ):
                stable_arrows = False
    gate(
        "S01",
        tuple(branch_table) == (4, 1, 1, 3) and stable_arrows,
        "SC1 branch-table=e,b,b,d invariant-full-leaf-maps",
    )

    factors12 = sorted(factor_sets[12])
    inverse_ok = True
    inverse_instances = 0
    for factor in factors12:
        window = Window(-6, (int(symbol) for symbol in factor))
        for state in leaves[h_leaf(window)]:
            point = (window, state)
            if inverse_stab(*v_hull(*point)) != point:
                inverse_ok = False
                break
            if v_hull(*inverse_stab(*point)) != point:
                inverse_ok = False
                break
            inverse_instances += 1
        if not inverse_ok:
            break
    gate(
        "S02",
        inverse_ok,
        "SC2 two-sided-inverse instances=" + str(inverse_instances),
    )

    reversal_bookkeeping = True
    reversor_ok = True
    reversor_instances = 0
    for factor in factors12:
        window = Window(-6, (int(symbol) for symbol in factor))
        if i_stab(rho(window)) != i_stab(window):
            reversal_bookkeeping = False
        if rho(rho(window)) != window:
            reversal_bookkeeping = False
        if rho(shift_k(rho(window))) != unshift_k(window):
            reversal_bookkeeping = False
        for state in leaves[h_leaf(window)]:
            point = (window, state)
            if r_cp(*r_cp(*point)) != point:
                reversor_ok = False
                break
            if r_cp(*v_hull(*r_cp(*point))) != inverse_stab(*point):
                reversor_ok = False
                break
            reversor_instances += 1
        if not reversor_ok:
            break
    gate(
        "S03",
        reversal_bookkeeping and reversor_ok,
        "SC3 rho-and-reversor instances=" + str(reversor_instances),
    )

    nine_sync = True
    for factor in sorted(factor_sets[9]):
        images = set()
        for initial in range(MOD):
            value = initial
            for symbol in factor:
                value = sheet_maps[int(symbol)][value]
            images.add(value)
        required = (4 + 2 * int(factor[-1])) % MOD
        if images != {required}:
            nine_sync = False

    nonsync8 = []
    for factor in sorted(factor_sets[8]):
        images = set()
        for initial in range(MOD):
            value = initial
            for symbol in factor:
                value = sheet_maps[int(symbol)][value]
            images.add(value)
        if len(images) > 1:
            nonsync8.append((factor, tuple(sorted(images))))

    start = word_sub.index(WSTAR, 6)
    witness_window = Window(
        -6,
        (
            int(symbol)
            for symbol in word_sub[start - 6:start + 14]
        ),
    )
    witness_state = (0, 0, 0, 0, 0, 0)
    for _ in range(8):
        witness_window, witness_state = v_hull(
            witness_window, witness_state
        )
    witness_off_stable = (
        z6(witness_state) == 2
        and h_leaf(witness_window) == 1
        and z6(witness_state) != h_leaf(witness_window)
    )
    gate(
        "S04",
        nine_sync
        and nonsync8 == [(WSTAR, (1, 2))]
        and witness_off_stable,
        "SC4 nine-step-stable-image unique-eight-obstruction sharp-witness",
    )

    y = (0, 4, 0, 0, 0, 0)
    psi_b = g_b(y)
    psi_d = g_d(y)
    factor0 = sorted(factor for factor in factors12 if factor[6] == "0")[0]
    window0 = Window(-6, (int(symbol) for symbol in factor0))
    image_b = v_hull(window0, psi_b)
    image_d = v_hull(window0, psi_d)
    collision = (
        z6(y) == 4
        and z6(psi_b) == 1
        and z6(psi_d) == 3
        and psi_b != psi_d
        and image_b == image_d
        and image_b[1] == y
    )
    gate("S05", collision, "SC5 explicit-full-hull-collision")

    stable_surjectivity = inverse_ok and stable_arrows
    finite_history_reduction = nine_sync and witness_off_stable
    gate(
        "S06",
        stable_surjectivity and finite_history_reduction,
        "SC6 finite-natural-extension-reductions written-proof-load-bearing",
    )

    emit("RESULT PASS gates=9 scope=SC1-SC6 layer=L1")


def main():
    try:
        audit()
    except Stop as error:
        for line in LINES:
            print(line)
        print("STOP " + str(error))
        return 1
    except Falsified as error:
        for line in LINES:
            print(line)
        print("FALSIFIED " + str(error))
        return 2
    except Exception as error:
        for line in LINES:
            print(line)
        print("STOP UNEXPECTED " + type(error).__name__ + " " + str(error))
        return 1

    for line in LINES:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
