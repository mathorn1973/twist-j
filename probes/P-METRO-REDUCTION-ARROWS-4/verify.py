#!/usr/bin/env python3
"""
P-METRO-REDUCTION-ARROWS-4

Obligations A (the four declared reduction arrows) and C (pointwise
transported L5-stream invariance) of METRO-REDUCTION-CALCULUS [O],
Public Canon v25.

This is a fresh known-result protocol repair. Prior private development
attempts remain outside the public repository and are not evidence.

Python standard library only. Integer and Fraction arithmetic. No float
appears in any assertion. Deterministic: no randomness, clock, filesystem,
network, subprocess, or dynamic evaluation. Run from the repository root.
"""

import itertools
import sys
from fractions import Fraction


Q, A, WIDTH = 2, 2, 3
BOX = [(x, y) for x in range(8) for y in range(8)]


def enc(idx, q, width):
    """Fixed-width base-q encoding, most significant digit first."""
    digits = []
    value = idx
    for _ in range(width):
        digits.append(value % q)
        value //= q
    return tuple(reversed(digits))


BOXW = [tuple(enc(idx[i], Q, WIDTH) for i in range(A)) for idx in BOX]
BOXW_SWAP = [(words[1], words[0]) for words in BOXW]


def comp_table(delta, n, wordlist, order):
    """Return the composite state map for every encoded input index."""
    out = []
    for words in wordlist:
        mapping = list(range(n))
        for i in order:
            digit_maps = delta[i]
            for u in words[i]:
                digit_map = digit_maps[u]
                mapping = [digit_map[state] for state in mapping]
        out.append(tuple(mapping))
    return out


def apply_word(digit_maps, word, state_value):
    for u in word:
        state_value = digit_maps[u][state_value]
    return state_value


def state_order(delta, words, order, state_value):
    for i in order:
        state_value = apply_word(delta[i], words[i], state_value)
    return state_value


def state(delta, words, state_value):
    return state_order(delta, words, range(len(words)), state_value)


_MONOID_CACHE = {}


def coord_monoid(digit_maps, n):
    key = (n, tuple(digit_maps))
    if key in _MONOID_CACHE:
        return _MONOID_CACHE[key]
    identity = tuple(range(n))
    seen = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for digit_map in digit_maps:
            composed = tuple(digit_map[current[s]] for s in range(n))
            if composed not in seen:
                seen.add(composed)
                frontier.append(composed)
    _MONOID_CACHE[key] = sorted(seen)
    return _MONOID_CACHE[key]


def v_actions(delta, n):
    monoids = [coord_monoid(delta[i], n) for i in range(A)]
    out = set()
    for combination in itertools.product(*monoids):
        mapping = tuple(range(n))
        for coordinate_map in combination:
            mapping = tuple(coordinate_map[mapping[s]] for s in range(n))
        out.add(mapping)
    return sorted(out)


def nerode(actions, output, n):
    signatures = {}
    labels = [0] * n
    for state_value in range(n):
        signature = tuple(output[action[state_value]] for action in actions)
        labels[state_value] = signatures.setdefault(signature, len(signatures))
    return labels


def congruence_failures(delta, labels, n):
    failures = []
    for i in range(A):
        for u in range(Q):
            digit_map = delta[i][u]
            for s in range(n):
                for t in range(s + 1, n):
                    if (
                        labels[s] == labels[t]
                        and labels[digit_map[s]] != labels[digit_map[t]]
                    ):
                        failures.append((i + 1, u, s, t))
    return failures


def sigma_orbit(delta, allowed_starts):
    seen = set(allowed_starts)
    frontier = list(allowed_starts)
    while frontier:
        state_value = frontier.pop()
        for i in range(A):
            for u in range(Q):
                target = delta[i][u][state_value]
                if target not in seen:
                    seen.add(target)
                    frontier.append(target)
    return seen


def v_image(delta, allowed_starts, n):
    return {
        action[state_value]
        for action in v_actions(delta, n)
        for state_value in allowed_starts
    }


def v_closure(delta, allowed_starts, n):
    actions = v_actions(delta, n)
    seen = set(allowed_starts)
    while True:
        grown = {action[s] for action in actions for s in seen} | seen
        if grown == seen:
            return seen
        seen = grown


def families(n):
    all_maps = list(itertools.product(range(n), repeat=n))
    per_coordinate = list(itertools.product(all_maps, repeat=Q))
    outputs = [
        tuple((Fraction(bit),) for bit in bits)
        for bits in itertools.product((0, 1), repeat=n)
    ]
    return per_coordinate, outputs


def relabel(delta, output, phi, n):
    inverse = [0] * n
    for state_value in range(n):
        inverse[phi[state_value]] = state_value
    transported_delta = [
        [
            tuple(
                phi[delta[i][u][inverse[state_value]]]
                for state_value in range(n)
            )
            for u in range(Q)
        ]
        for i in range(A)
    ]
    transported_output = [output[inverse[state_value]] for state_value in range(n)]
    return transported_delta, transported_output


def quotient_protocol(delta, output, labels, n):
    """Build the admitted Nerode quotient after congruence is established."""
    classes = sorted(set(labels))
    representatives = {}
    for state_value in range(n):
        representatives.setdefault(labels[state_value], state_value)
    quotient_delta = []
    for i in range(A):
        coordinate = []
        for u in range(Q):
            coordinate.append(
                tuple(
                    labels[delta[i][u][representatives[class_id]]]
                    for class_id in classes
                )
            )
        quotient_delta.append(coordinate)
    quotient_output = [output[representatives[class_id]] for class_id in classes]
    return quotient_delta, quotient_output


RESULTS = []


def gate(tag, ok, text):
    RESULTS.append((tag, bool(ok), text))


# Frozen witnesses.
W4_DELTA = [
    [(0, 0, 0, 0), (0, 0, 0, 1)],
    [(0, 0, 0, 0), (0, 0, 3, 0)],
]
W4_W = [
    (Fraction(0),),
    (Fraction(1),),
    (Fraction(0),),
    (Fraction(0),),
]
WR_DELTA = [
    [(0, 0, 0, 0), (0, 0, 0, 1)],
    [(0, 0, 0, 0), (2, 0, 3, 0)],
]
WP_DELTA = [
    [(0, 0, 0, 0), (0, 0, 0, 0)],
    [(0, 0, 0, 0), (1, 0, 0, 0)],
]

PC2, WS2 = families(2)
PAIRS2 = [[list(c0), list(c1)] for c0 in PC2 for c1 in PC2]
ORDER = [0, 1]


# E1: arrow 1, relabeling.
ok = True
for delta in PAIRS2:
    original_table = comp_table(delta, 2, BOXW, ORDER)
    for phi in itertools.permutations(range(2)):
        transported_delta, _ = relabel(delta, WS2[0], list(phi), 2)
        transported_table = comp_table(transported_delta, 2, BOXW, ORDER)
        inverse = [0, 0]
        for state_value in range(2):
            inverse[phi[state_value]] = state_value
        for output in WS2:
            transported_output = [output[inverse[s]] for s in range(2)]
            for index in range(len(BOX)):
                for state_value in range(2):
                    if (
                        transported_output[
                            transported_table[index][phi[state_value]]
                        ]
                        != output[original_table[index][state_value]]
                    ):
                        ok = False
gate(
    "E1a",
    ok,
    "arrow 1 relabeling intertwines pointwise on all 1024 protocols of F2, "
    "both bijections, and all 64 indices of BOX",
)

ok = True
original_table = comp_table(W4_DELTA, 4, BOXW, ORDER)
for phi in itertools.permutations(range(4)):
    transported_delta, transported_output = relabel(
        W4_DELTA, W4_W, list(phi), 4
    )
    transported_table = comp_table(transported_delta, 4, BOXW, ORDER)
    for index in range(len(BOX)):
        for state_value in range(4):
            if (
                transported_output[transported_table[index][phi[state_value]]]
                != W4_W[original_table[index][state_value]]
            ):
                ok = False
gate(
    "E1b",
    ok,
    "arrow 1 intertwines on W4 for all 24 bijections; bijectivity is the "
    "complete precondition",
)


# E2: arrow 2, reachable restriction.
ok = True
for delta in PAIRS2:
    for allowed_starts in ({0}, {1}, {0, 1}):
        closure = v_closure(delta, allowed_starts, 2)
        orbit = sigma_orbit(delta, allowed_starts)
        if closure != orbit:
            ok = False
        for state_value in orbit:
            for i in range(A):
                for u in range(Q):
                    if delta[i][u][state_value] not in orbit:
                        ok = False
f3_carrier = frozenset(range(3))
f3_identity = all(
    frozenset(digit_map[state_value] for state_value in f3_carrier)
    <= f3_carrier
    for digit_map in itertools.product(range(3), repeat=3)
)
gate(
    "E2a",
    ok and f3_identity,
    "iterated V-closure equals the Sigma*-orbit on F2 for A0={0},{1},S, "
    "and the result is digit-map closed; F3 has A0=S, hence S_reach=S and "
    "restriction is the identity",
)

ok = True
for delta in PAIRS2:
    original_table = comp_table(delta, 2, BOXW, ORDER)
    orbit = sorted(sigma_orbit(delta, {0}))
    renaming = {state_value: k for k, state_value in enumerate(orbit)}
    restricted_delta = [
        [
            tuple(
                renaming[delta[i][u][state_value]] for state_value in orbit
            )
            for u in range(Q)
        ]
        for i in range(A)
    ]
    restricted_table = comp_table(restricted_delta, len(orbit), BOXW, ORDER)
    for output in WS2:
        restricted_output = [output[state_value] for state_value in orbit]
        for index in range(len(BOX)):
            if (
                restricted_output[restricted_table[index][renaming[0]]]
                != output[original_table[index][0]]
            ):
                ok = False
gate(
    "E2b",
    ok,
    "arrow 2 restriction to S_reach intertwines pointwise on F2 with "
    "A0={0}, over all 64 indices of BOX",
)

one_shot_image = v_image(WR_DELTA, {0}, 4)
sigma_star_orbit = sigma_orbit(WR_DELTA, {0})
gate(
    "E2c",
    one_shot_image < sigma_star_orbit,
    "typing witness WR: the one-shot V-image %s is strictly inside the "
    "Sigma*-orbit %s; only the closure reading types arrow 2 correctly"
    % (sorted(one_shot_image), sorted(sigma_star_orbit)),
)


# E3: arrow 3, multi-action Nerode congruence.
SHORT_WORDS = [(), (0,), (1,), (0, 0), (0, 1), (1, 0), (1, 1)]
ok = True
for delta in (W4_DELTA, WR_DELTA, WP_DELTA):
    for u in range(Q):
        for v1 in SHORT_WORDS:
            for v2 in SHORT_WORDS:
                for state_value in range(4):
                    left = state(delta, ((u,) + v1, v2), state_value)
                    right = state(
                        delta, (v1, v2), delta[0][u][state_value]
                    )
                    if left != right:
                        ok = False
gate(
    "E3a",
    ok,
    "delta_v o delta_(1,u)=delta_(u.v_1,v_2) on every frozen witness "
    "for coordinate words of length <=2; this is the coordinate-1 "
    "congruence identity",
)

actions = v_actions(W4_DELTA, 4)
labels = nerode(actions, W4_W, 4)
failures = congruence_failures(W4_DELTA, labels, 4)
gate(
    "E3b",
    failures == [(2, 1, 0, 2)],
    "W4: ~_V identifies states {0,2}, but delta_(2,1) sends them to "
    "different classes. Failures found: %s" % failures,
)
gate(
    "E3c",
    [failure for failure in failures if failure[0] == 1] == [],
    "W4 has no coordinate-1 congruence failure, as E3a forces",
)

# Exhaustion is grouped by the two coordinate monoids. These monoids determine
# the V-action set and therefore the Nerode labels. For each label set, digit
# maps that break congruence are cached once.
counts = {}
for n in (2, 3):
    all_maps = list(itertools.product(range(n), repeat=n))
    per_coordinate = list(itertools.product(all_maps, repeat=Q))
    integer_outputs = list(itertools.product((0, 1), repeat=n))
    action_cache = {}
    bad_map_cache = {}
    bad_total = 0
    seen_total = 0
    for coordinate_zero in per_coordinate:
        monoid_zero = tuple(coord_monoid(list(coordinate_zero), n))
        for coordinate_one in per_coordinate:
            monoid_one = tuple(coord_monoid(list(coordinate_one), n))
            key = (monoid_zero, monoid_one)
            actions_n = action_cache.get(key)
            if actions_n is None:
                actions_n = action_cache[key] = sorted(
                    {
                        tuple(f1[f0[s]] for s in range(n))
                        for f0 in monoid_zero
                        for f1 in monoid_one
                    }
                )
            for output in integer_outputs:
                seen_total += 1
                cache_key = (key, output)
                bad_maps = bad_map_cache.get(cache_key)
                if bad_maps is None:
                    labels_n = nerode(actions_n, output, n)
                    if len(set(labels_n)) == n:
                        bad_maps = bad_map_cache[cache_key] = frozenset()
                    else:
                        same_class_pairs = [
                            (s, t)
                            for s in range(n)
                            for t in range(s + 1, n)
                            if labels_n[s] == labels_n[t]
                        ]
                        bad_maps = bad_map_cache[cache_key] = frozenset(
                            digit_map
                            for digit_map in all_maps
                            if any(
                                labels_n[digit_map[s]]
                                != labels_n[digit_map[t]]
                                for s, t in same_class_pairs
                            )
                        )
                if bad_maps and (
                    coordinate_zero[0] in bad_maps
                    or coordinate_zero[1] in bad_maps
                    or coordinate_one[0] in bad_maps
                    or coordinate_one[1] in bad_maps
                ):
                    bad_total += 1
    counts[n] = (seen_total, bad_total)

gate(
    "E3d",
    counts[2] == (1024, 0),
    "|S|=2 exhausted: %d protocols, %d congruence counterexamples"
    % counts[2],
)
gate(
    "E3e",
    counts[3] == (4251528, 0),
    "|S|=3 exhausted: %d protocols, %d congruence counterexamples"
    % counts[3],
)
gate(
    "E3f",
    counts[2] == (1024, 0)
    and counts[3] == (4251528, 0)
    and bool(failures),
    "minimality at q=2,a=2,r=1 with binary output: W4 at |S|=4 is "
    "minimal; the arrow-3 congruence precondition is non-vacuous",
)


# E4: arrow 4, coordinate permutation.
arrow_four_pointwise = True
basis_fixed_failures = 0
for delta in PAIRS2:
    original_table = comp_table(delta, 2, BOXW, ORDER)
    transported_delta = [delta[1], delta[0]]
    transported_table = comp_table(
        transported_delta, 2, BOXW_SWAP, [1, 0]
    )
    basis_fixed_table = comp_table(
        transported_delta, 2, BOXW_SWAP, [0, 1]
    )
    for output in WS2:
        for index in range(len(BOX)):
            for state_value in range(2):
                if (
                    output[transported_table[index][state_value]]
                    != output[original_table[index][state_value]]
                ):
                    arrow_four_pointwise = False
                if (
                    output[basis_fixed_table[index][state_value]]
                    != output[original_table[index][state_value]]
                ):
                    basis_fixed_failures += 1
gate(
    "E4a",
    arrow_four_pointwise,
    "arrow 4 with coordinate names, indices, and ordered input basis "
    "transported preserves the pointwise stream on all F2 x BOX",
)
gate(
    "E4b",
    basis_fixed_failures > 0,
    "the basis-fixed lookalike breaks intertwining at %d points of F2 x "
    "BOX; arrow 4 is admitted only with the ordered basis transported"
    % basis_fixed_failures,
)

admitted_composite = tuple(
    WP_DELTA[1][1][WP_DELTA[0][1][s]] for s in range(4)
)
basis_fixed_composite = tuple(
    WP_DELTA[0][1][WP_DELTA[1][1][s]] for s in range(4)
)
gate(
    "E4c",
    admitted_composite != basis_fixed_composite,
    "permutation witness WP: admitted composite %s, basis-fixed "
    "lookalike %s"
    % (list(admitted_composite), list(basis_fixed_composite)),
)


# E5: obligation C, explicit coverage of every admitted arrow.
arrows_one_two_pointwise = True
for delta in PAIRS2:
    original_table = comp_table(delta, 2, BOXW, ORDER)
    relabeled = []
    for phi in itertools.permutations(range(2)):
        transported_delta, _ = relabel(delta, WS2[0], list(phi), 2)
        inverse = [0, 0]
        for state_value in range(2):
            inverse[phi[state_value]] = state_value
        relabeled.append(
            (
                phi,
                inverse,
                comp_table(transported_delta, 2, BOXW, ORDER),
            )
        )
    orbit = sorted(sigma_orbit(delta, {0}))
    renaming = {state_value: k for k, state_value in enumerate(orbit)}
    restricted_delta = [
        [
            tuple(
                renaming[delta[i][u][state_value]] for state_value in orbit
            )
            for u in range(Q)
        ]
        for i in range(A)
    ]
    restricted_table = comp_table(restricted_delta, len(orbit), BOXW, ORDER)
    for output in WS2:
        restricted_output = [output[state_value] for state_value in orbit]
        for index in range(len(BOX)):
            for state_value in range(2):
                base_value = output[original_table[index][state_value]]
                for phi, inverse, transported_table in relabeled:
                    transported_output = [output[inverse[x]] for x in range(2)]
                    if (
                        transported_output[
                            transported_table[index][phi[state_value]]
                        ]
                        != base_value
                    ):
                        arrows_one_two_pointwise = False
            if (
                restricted_output[restricted_table[index][renaming[0]]]
                != output[original_table[index][0]]
            ):
                arrows_one_two_pointwise = False
gate(
    "E5a",
    arrows_one_two_pointwise,
    "obligation C: arrows 1 and 2 preserve pointwise transported L5 "
    "streams on their complete F2 x BOX audits with tau_R=id",
)

arrow_three_pointwise = True
for delta in PAIRS2:
    original_table = comp_table(delta, 2, BOXW, ORDER)
    actions = v_actions(delta, 2)
    for output in WS2:
        labels = nerode(actions, output, 2)
        if congruence_failures(delta, labels, 2):
            arrow_three_pointwise = False
            continue
        quotient_delta, quotient_output = quotient_protocol(
            delta, output, labels, 2
        )
        quotient_table = comp_table(
            quotient_delta, len(set(labels)), BOXW, ORDER
        )
        for index in range(len(BOX)):
            for state_value in range(2):
                if (
                    quotient_output[
                        quotient_table[index][labels[state_value]]
                    ]
                    != output[original_table[index][state_value]]
                ):
                    arrow_three_pointwise = False
gate(
    "E5b",
    arrow_three_pointwise,
    "obligation C: every admitted arrow-3 Nerode quotient on F2 is "
    "well-defined and preserves the pointwise L5 stream on BOX",
)

gate(
    "E5c",
    arrows_one_two_pointwise
    and arrow_three_pointwise
    and arrow_four_pointwise,
    "obligation C covers all four admitted arrows at pointwise L5 scope "
    "with tau_R=id; no L6 decision or normalization lift is claimed",
)


# Report.
print("P-METRO-REDUCTION-ARROWS-4")
print("owner item: METRO-REDUCTION-CALCULUS [O], obligations A and C")
print("scope: pointwise transported L5 streams; no lift to L6")
print("exact integer and Fraction arithmetic, no float in any assertion")
print("")

all_ok = True
for tag, passed, text in RESULTS:
    all_ok &= passed
    print("%-5s %-4s %s" % (tag, "OK" if passed else "FAIL", text))

print("")
print(
    "gates passed: %d of %d"
    % (sum(1 for _, passed, _ in RESULTS if passed), len(RESULTS))
)
print("VERDICT: %s" % ("ALL PASS" if all_ok else "FAILURE"))
print("")
print("NOT CLOSED BY THIS PROBE: obligation B (forbidden transformations),")
print("obligation D (common q^k blocking), obligation E (completeness of")
print("approx_red). METRO-REDUCTION-CALCULUS remains [O] and remains STOP.")
sys.exit(0 if all_ok else 1)
