# SPDX-License-Identifier: Apache-2.0
"""Bounded exact search for compact cold material profiles in native H3."""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import lcm

from native import h3, ledger, put, reverse, step


ZERO = h3.ZERO
HORIZON = 24
WIDTHS = (2, 3, 4)
AMPLITUDES = (
    h3.ONE, h3.scale(2, h3.ONE), h3.J, h3.conj(h3.J),
    h3.scale(2, h3.J), h3.scale(2, h3.conj(h3.J)), h3.RHO, h3.RHO_INV,
)
ALPHABET = tuple(sorted({ZERO, *(h3.scale(sign, word)
                                for word in AMPLITUDES for sign in (-1, 1))}))
ALPHABET_SET = frozenset(ALPHABET)
UNITS = tuple(
    (sign, exponent, h3.scale(sign, h3.J_POWERS[2 * exponent % 5]))
    for sign in (1, -1) for exponent in range(5)
)


@lru_cache(maxsize=131072)
def contact(a, b):
    pair = h3.transport_pair(a, b, False)
    refused = a != b and not h3.even(h3.sub(a, b))
    return pair, refused


def unwrapped_step(start, profile, bit):
    end = start + len(profile) - 1
    lower = start - ((start - bit) % 2)
    result, refusals = [], 0
    for y in range(lower, end + 1, 2):
        a = profile[y - start] if y >= start else ZERO
        b = profile[y + 1 - start] if y + 1 <= end else ZERO
        pair, refused = contact(a, b)
        result.extend(pair)
        refusals += refused
    first = next(i for i, word in enumerate(result) if word != ZERO)
    last = len(result) - next(i for i, word in enumerate(reversed(result)) if word != ZERO)
    return lower + first, tuple(result[first:last]), refusals


def seeds():
    for width in WIDTHS:
        for prefix in product(ALPHABET, repeat=width - 1):
            if prefix[0] == ZERO:
                continue
            final = h3.scale(-1, h3.ring_sum(prefix))
            if final != ZERO and final in ALPHABET_SET:
                yield prefix + (final,)
    # Extend beyond zero total without expanding the full width-four search.
    for left, right in product(ALPHABET, repeat=2):
        if left == ZERO or right == ZERO:
            continue
        for middle in ((), (ZERO,), (h3.ONE,), (h3.scale(-1, h3.ONE),)):
            seed = (left,) + middle + (right,)
            if h3.ring_sum(seed) != ZERO:
                yield seed


def relative_return(seed, anchor):
    variants = {
        tuple(h3.mul(unit, word) for word in seed): (sign, exponent)
        for sign, exponent, unit in UNITS
    }
    start, profile = anchor, seed
    refusals = 0
    unchanged = True
    for tick in range(1, HORIZON + 1):
        start, profile, refused = unwrapped_step(start, profile, (tick - 1) % 2)
        refusals += refused
        displacement = start - anchor
        unchanged &= displacement == 0 and profile == seed
        if (displacement - tick) % 2 or len(profile) != len(seed):
            continue
        phase = variants.get(profile)
        if phase is not None:
            return (tick, displacement, phase, unchanged), refusals
    return None, refusals


def word_pair(word, sector):
    return word, h3.scale(-1, word) if sector == "ANTIPODAL" else ZERO


def embed(nx, ny, col, offset, anchor, profile, sector):
    field = [ZERO] * (4 * nx * ny)
    h3.require(0 < offset + anchor <= offset + anchor + len(profile) - 1 < ny - 1,
               "unwrapped profile stays away from torus seam")
    for j, word in enumerate(profile):
        put(field, ny, col, offset + anchor + j, word_pair(word, sector) + (ZERO, ZERO))
    return tuple(field)


def field_support(field, ny):
    return tuple(
        (i // (4 * ny), (i // 4) % ny)
        for i in range(0, len(field), 4)
        if field[i:i + 4] != (ZERO,) * 4
    )


def word_pair_at(field, ny, x, y):
    start = 4 * (x * ny + y)
    return field[start:start + 2]

def replay(seed, anchor, horizon, sector, reflected, nx, extra_height):
    # An even lift of unwrapped zero preserves active bond labels.
    pad = horizon + 4
    offset = pad + pad % 2
    ny = 2 * offset + len(seed) + extra_height
    ny += ny % 2
    col = nx // 2
    initial = embed(nx, ny, col, offset, anchor, seed, sector)
    start, profile, state = anchor, seed, initial
    if reflected:
        # y -> 1-y sends each active lower endpoint p to -p, of the same color.
        reflection = 2 * offset + 1
        state = embed(nx, ny, col, offset, 2 - anchor - len(seed),
                       seed[::-1], sector)
    initial_ledger = ledger(state)
    equal, no_b = True, True
    initial_support = set(field_support(state, ny))
    last_support = ()
    new_sites = {}
    for tick in range(horizon):
        bit = tick % 2
        c, b, tags = step(state, ny, bit)
        h3.require(reverse(b, ny, bit) == state and ledger(b) == initial_ledger,
                   "native drift inverse and complete ledger")
        start, profile, _ = unwrapped_step(start, profile, bit)
        if reflected:
            start_image = reflection - (offset + start + len(profile) - 1) - offset
            profile_image = profile[::-1]
        else:
            start_image, profile_image = start, profile
        expected = embed(nx, ny, col, offset, start_image, profile_image, sector)
        equal &= c == expected and b == expected
        no_b &= not tags
        state = b
        last_support = field_support(state, ny)
        for x, y in last_support:
            if (x, y) not in initial_support and (x, y) not in new_sites:
                q = sum(h3.scalar_account(h3.h(word))
                        for word in word_pair_at(state, ny, x, y))
                new_sites[x, y] = (tick + 1, q)
    return {
        "geometry": [nx, ny], "sector": sector, "reflected": reflected,
        "steps": horizon, "native_match": equal, "no_b": no_b,
        "initial_ledger": initial_ledger, "terminal_support_xy": last_support,
        "initial_support_xy": sorted(initial_support),
        "new_sites_tick_q": [[x, y, tick, q]
                             for (x, y), (tick, q) in sorted(new_sites.items())],
    }


def controls():
    return (
        (0, (h3.ONE, h3.scale(-1, h3.ONE))),
        (1, (h3.scale(-2, h3.ONE), ZERO, h3.scale(2, h3.ONE))),
        (0, (h3.scale(2, h3.J), h3.scale(-2, h3.J), h3.RHO, h3.scale(-1, h3.RHO))),
    )


def phase_order(sign, exponent):
    return lcm(1 if sign == 1 else 2, 1 if exponent == 0 else 5)


def fraction_pair(n, d):
    value = Fraction(n, d)
    return [value.numerator, value.denominator]


def run():
    counts = Counter()
    by_width = {width: Counter() for width in WIDTHS}
    by_period = Counter()
    by_total = {"ZERO": Counter(), "NONZERO": Counter()}
    witnesses = []
    for seed in seeds():
        total_group = by_total["ZERO" if h3.ring_sum(seed) == ZERO else "NONZERO"]
        for anchor in (0, 1):
            match, refusals = relative_return(seed, anchor)
            local = by_width[len(seed)]
            kind = "NO_RETURN_THROUGH_24"
            if match is not None:
                tick, shift, (sign, exponent), unchanged = match
                by_period[tick] += 1
                if shift == 0:
                    if unchanged:
                        kind = "STATIC_FIELD"
                    elif (sign, exponent) == (1, 0):
                        kind = "ZERO_SHIFT_EXACT_INTERNAL_RETURN"
                    else:
                        kind = "ZERO_SHIFT_PHASE_INTERNAL_RETURN"
                elif not refusals:
                    kind = "SHIFT_WITHOUT_REFUSAL"
                else:
                    kind = "SHIFT_WITH_REFUSAL"
                if shift:
                    repeats = lcm(phase_order(sign, exponent), 1 if tick % 2 == 0 else 2)
                    replays = [
                        replay(seed, anchor, tick, "SINGLE", False, 4, 0),
                        replay(seed, anchor, tick, "ANTIPODAL", True, 8, 6),
                    ]
                    witnesses.append({
                        "seed_start": anchor, "seed": seed, "relative_period": tick,
                        "shift_y": shift, "phase_sign": sign, "phase_rho_exponent": exponent,
                        "nontrivial_refusals": refusals, "exact_full_period": repeats * tick,
                        "exact_full_shift_y": repeats * shift, "speed": fraction_pair(shift, tick),
                        "native_replays": replays, "lightfront_speed": abs(shift) == tick,
                    })
            counts[kind] += 1
            local[kind] += 1
            total_group[kind] += 1
            counts["PROFILES_WITH_A_REFUSAL"] += bool(refusals)
            local["PROFILES_WITH_A_REFUSAL"] += bool(refusals)
    replays = [
        {"seed_start": anchor, "seed": seed, "runs": [
            replay(seed, anchor, HORIZON, "SINGLE", False, 4, 0),
            replay(seed, anchor, HORIZON, "ANTIPODAL", True, 8, 6),
        ]}
        for anchor, seed in controls()
    ]
    all_replays = [row for case in replays for row in case["runs"]]
    all_replays.extend(row for case in witnesses for row in case["native_replays"])
    positive_off_seed_q = any(q > 0 for row in all_replays
                              for _, _, _, q in row["new_sites_tick_q"])
    return {
        "passed": all(row["native_match"] and row["no_b"] for row in all_replays)
                  and not witnesses and positive_off_seed_q,
        "tested_profiles": sum(value for key, value in counts.items()
                               if key != "PROFILES_WITH_A_REFUSAL"),
        "horizon": HORIZON, "alphabet_size": len(ALPHABET), "counts": dict(counts),
        "counts_by_width": {width: dict(local) for width, local in by_width.items()},
        "counts_by_total": {kind: dict(local) for kind, local in by_total.items()},
        "has_positive_off_seed_site_q": positive_off_seed_q,
        "relative_return_periods": dict(by_period), "witnesses": witnesses,
        "controls": replays,
    }
