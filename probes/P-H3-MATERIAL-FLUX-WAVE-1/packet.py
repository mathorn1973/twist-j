# SPDX-License-Identifier: Apache-2.0
"""Exact passive packet experiment on the zero-matter native H3 sector."""

from fractions import Fraction
from itertools import product

from native import h3, transport


CELLS = 192
RADIUS = 16
CUTS = {40: 20, 80: 40}
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
RHO_INV = (0, 0, 0, 1)
PHI = (0, 0, -1, -1)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k * x for x in a)


def mul(a, b):
    c = [0] * 5
    for x, ax in enumerate(a):
        for y, by in enumerate(b):
            c[(x + y) % 5] += ax * by
    return tuple(c[i] - c[4] for i in range(4))


def conj(a):
    return (a[0] - a[1], -a[1], a[3] - a[1], a[2] - a[1])


def norm(a):
    return mul(a, conj(a))


def trace(a):
    return 5 * a[0] - sum(a)


def total(words):
    result = ZERO
    for word in words:
        result = add(result, word)
    return result


def sign(x):
    return (x > 0) - (x < 0)


def real_sign(a, b, embedding):
    """Exact sign of a + b*phi, where phi=(1±sqrt(5))/2."""
    r = 2 * a + b
    s = b if embedding == 1 else -b
    if r == 0 or s == 0 or sign(r) == sign(s):
        return sign(r or s)
    return sign(r) * sign(r * r - 5 * s * s)


def embedding_sign(a, embedding):
    assert a[1] == 0 and a[2] == a[3]
    return real_sign(a[0], -a[2], embedding)


def phase_signs(a, embedding):
    twice_real = add(a, conj(a))
    if embedding == 1:
        imag = real_sign(a[2] - a[3], a[1], 1)
    else:
        imag = real_sign(a[1], a[3] - a[2], 1)
    return (embedding_sign(twice_real, embedding), imag)


def half(a):
    return tuple(x // 2 for x in a)


def even(a):
    return all(x % 2 == 0 for x in a)


def step(row, p, inverse=False):
    nxt = row.copy()
    refused = 0
    for x in range(p, len(row), 2):
        y = (x + 1) % len(row)
        a, b = row[x], row[y]
        delta = sub(a, b)
        if not even(delta):
            refused += 1
            continue
        if a != b:
            # Multiplication in the declared integral basis by rho or rho^-1.
            h0, h1, h2, h3 = half(delta)
            if inverse:
                rotated = (h2 - h1, h3 - h1, -h1, h0 - h1)
            else:
                rotated = (h3 - h2, -h2, h0 - h2, h1 - h2)
            center = half(add(a, b))
            nxt[x], nxt[y] = add(center, rotated), sub(center, rotated)
    return nxt, refused


def compare_full_cut(row, nxt, bit, inverse=False):
    field = [ZERO] * (8 * len(row))
    expected = field.copy()
    field[3::8] = row
    expected[3::8] = nxt
    assert transport(tuple(field), 2, bit, backward=inverse) == tuple(expected)


def launch():
    row = [ZERO] * (2 * CELLS)
    paid = 2 ** max(CUTS)
    vector = (scale(sub(RHO, RHO_INV), -250), add(scale(ONE, 1188), scale(PHI, 412)))
    for n in range(1 - RADIUS, RADIUS):
        taper = (RADIUS ** 2 - n * n) ** 4
        modulator = add(scale(ONE, 32), scale(sub(RHO, RHO_INV), n))
        for s, v in enumerate(vector):
            sign_stagger = -1 if n % 2 else 1
            row[2 * (n % CELLS) + s] = scale(mul(v, modulator), paid * taper * sign_stagger)
    return row


def mirror(row):
    return [row[(1 - x) % len(row)] for x in range(len(row))]


def signed_cell(n):
    return (n + CELLS // 2) % CELLS - CELLS // 2


def stock_and_moment(row):
    stock = ZERO
    moment = ZERO
    for x, word in enumerate(row):
        if word != ZERO:
            h = norm(word)
            stock = add(stock, h)
            moment = add(moment, scale(h, signed_cell(x // 2)))
    return stock, moment


def first_difference_stock(row):
    # Undo the carrier stagger by taking the sum of adjacent cells.
    return total(norm(add(row[x], row[(x + 2) % len(row)])) for x in range(len(row)))


def account(row):
    h, _ = stock_and_moment(row)
    assert trace(h) % 2 == 0
    return (ZERO, total(row), h, trace(h) // 2)


J = add(ONE, RHO)
L = sub(ONE, RHO)
THETA = norm(J)


def virtual_branch(corr):
    """One-cut native B diagnostic with r0=L, r2=-L and CLK=0."""
    if not even(corr):
        return 0
    f = half(corr)
    if norm(f) == mul(THETA, norm(L)):
        return 1
    if f != ZERO and norm(L) == mul(THETA, norm(f)):
        return 2
    return 0


def speed_test(stock, moment, steps, direction, embedding):
    low, high = ((Fraction(4, 5), Fraction(1)), (Fraction(2, 5), Fraction(3, 4)))[embedding - 1]
    directed = scale(moment, direction)
    at_least = embedding_sign(sub(scale(directed, low.denominator), scale(stock, steps * low.numerator)), embedding)
    at_most = embedding_sign(sub(scale(stock, steps * high.numerator), scale(directed, high.denominator)), embedding)
    return at_least >= 0 and at_most >= 0


def speed_lower_bound(stock, moment, steps, direction, embedding):
    resolution = 10000
    numerator = scale(moment, resolution * direction)
    denominator = scale(stock, steps)
    lower, upper = -CELLS * resolution, CELLS * resolution
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if embedding_sign(sub(numerator, scale(denominator, middle)), embedding) >= 0:
            lower = middle
        else:
            upper = middle
    return lower


def window_stock(row, center):
    return total(norm(row[2 * (n % CELLS) + s]) for n in range(center - 4, center + 5) for s in (0, 1))


def follow(initial, direction):
    row = initial
    ledger = account(row)
    target_sites = {d: (-2 * d if direction == -1 else 2 * d + 1) for d in CUTS.values()}
    first_word = {d: None for d in target_sites}
    first_b = {d: None for d in target_sites}
    cuts = {}
    refused = 0
    for tick in range(1, max(CUTS) + 1):
        bit = (tick - 1) % 2
        nxt, blocked = step(row, bit)
        if tick in (1, 2):
            compare_full_cut(row, nxt, bit)
        row = nxt
        refused += blocked
        assert account(row) == ledger
        for d, site in target_sites.items():
            incoming = row[site]
            if incoming != ZERO and first_word[d] is None:
                first_word[d] = tick
            branch = virtual_branch(incoming)
            assert branch == h3.collision((L, scale(L, -1), ZERO, incoming))[1]
            if branch and first_b[d] is None:
                first_b[d] = (tick, branch)
        if tick in CUTS:
            distance = CUTS[tick]
            stock, moment = stock_and_moment(row)
            incoming = row[target_sites[distance]]
            word = scale(incoming, -1 if distance % 2 else 1)
            cuts[str(tick)] = {
                "distance_cells": distance,
                "word": word,
                "word_phase_signs": [phase_signs(word, a) for a in (1, 2)] if word != ZERO else None,
                "virtual_B": virtual_branch(incoming),
                "centroid_numerators": moment,
                "near_receiver_H": window_stock(row, direction * distance),
                "opposite_window_H": window_stock(row, -direction * distance),
                "speed_intervals_pass": [speed_test(stock, moment, tick // 2, direction, a) for a in (1, 2)],
                "speed_floor_times_10000": [speed_lower_bound(stock, moment, tick // 2, direction, a) for a in (1, 2)],
            }
    assert refused == 0
    for tick in range(max(CUTS), 0, -1):
        bit = (tick - 1) % 2
        previous, blocked = step(row, bit, inverse=True)
        if tick in (max(CUTS), max(CUTS) - 1):
            compare_full_cut(row, previous, bit, inverse=True)
        row = previous
        assert blocked == 0
    assert row == initial
    first, last = (cuts[str(t)]["word"] for t in CUTS)
    cross_word = mul(last, conj(first))
    phase_defined = first != ZERO and last != ZERO
    return {
        "initial_account": ledger,
        "cuts_post_C_pre_B": cuts,
        "first_nonzero": first_word,
        "first_causal_tick": {d: 2 * (d - RADIUS + 1) + 1 for d in target_sites},
        "first_virtual_B": first_b,
        "phase_ratio_numerator": cross_word if phase_defined else None,
        "phase_ratio_denominator": norm(first) if phase_defined else None,
        "phase_ratio_signs": [phase_signs(cross_word, a) for a in (1, 2)] if phase_defined else None,
        "inverse_restored": True,
        "full_C_cross_checks_forward_reverse": [2, 2],
        "parity_refusals": refused,
    }


def d3_shape():
    # Sum the frozen weighted shell symbol after restricting k to the x axis.
    weights = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
    second = fourth = 0
    for x, y, z in product(range(-4, 5), repeat=3):
        w = weights.get(x * x + y * y + z * z, 0)
        second += w * x * x
        fourth += w * x ** 4
    assert second == 648
    d3 = Fraction(1, 12) - Fraction(fourth, 24 * 324)
    # h3 coefficient in Q(phi) is (phi-2)/48. D3 is rational.
    # Equality would require the phi coefficient to vanish.
    return {
        "direction": "D3 x axis",
        "calibration": "k=q and omega_H3=sqrt(nu_1)*omega_D3, both embeddings",
        "D3_linear_slope_squared_after_calibration": [2, 1, 4],
        "H3_slope_squared_phi_tuples_embedding_1_2": [[2, 1, 4], [3, -1, 4]],
        "H3_quartic_over_slope_squared_phi_tuples_embedding_1_2": [[-2, 1, 48], [-1, -1, 48]],
        "phi_tuple_convention": "[a,b,c] means (a+b*(1+sqrt(5))/2)/c",
        "D3_quartic_over_slope_squared": [d3.numerator, d3.denominator],
        "tangent_matches": [True, False],
        "quartic_matches": [False, False],
    }


def run():
    left = launch()
    right = mirror(left)
    stock = account(left)[2]
    assert stock_and_moment(left)[1] == ZERO
    assert account(right) == account(left)
    spectral = first_difference_stock(left)
    return {
        "left": follow(left, -1),
        "right": follow(right, 1),
        "initial_spectral_second_moment_numerator": spectral,
        "initial_spectral_second_moment_denominator": stock,
        "single_loaded_detector_H_increment": scale(norm(L), 2),
        "initial_spectral_second_moment_below_one_sixteenth": [
            embedding_sign(sub(stock, scale(spectral, 16)), a) >= 0 for a in (1, 2)
        ],
        "D3": d3_shape(),
    }
