#!/usr/bin/env python3
"""Complete shell E=32, S=4 for the absolute triple contact.

NON-CANONICAL / L1. Adapted from the already exposed 2026-11-02 review audit.
Python standard library, integers only. No imports from other verifiers,
shell fixtures or classifiers. This is not a new independent review.
Computational statements and stdout are unchanged from that source.
"""
import collections
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
FOUR = (4, 0, 0, 0)


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def minus(x, y):
    return tuple(a - b for a, b in zip(x, y))


def Q(x):
    twice = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert twice % 2 == 0
    return twice // 2


def rho_times(x):
    """Multiply by j^2 in the five-entry cyclic presentation, then normalize.

    Appending a zero fifth coefficient and cyclically shifting is legal by
    j^5=1. Subtract the fifth coefficient from all entries using Phi5(j)=0.
    This is a separate implementation from previous four-entry formulas.
    """
    five = x + (0,)
    shifted = five[-2:] + five[:-2]
    return tuple(shifted[i] - shifted[4] for i in range(4))


def C(a, b):
    difference = minus(a, b)
    if any(coefficient % 2 for coefficient in difference):
        return a, b
    relative = tuple(coefficient // 2 for coefficient in difference)
    increment = minus(rho_times(relative), relative)
    return plus(a, increment), minus(b, increment)


def F(state):
    a, b = C(state[0], state[1])
    b, c = C(b, state[2])
    return a, b, c


def energy(state):
    return sum(Q(a) for a in state)


def total(state):
    return plus(plus(state[0], state[1]), state[2])


def difference_coordinates(state):
    return minus(state[0], state[1]) + minus(state[1], state[2])


def M(state):
    u, v = minus(state[0], state[1]), minus(state[1], state[2])
    return Q(u) + Q(v) + Q(plus(u, v))


def g(state):
    return int(sorted(Q(a) for a in state) == [0, 0, 32])


def coordinate_bound_identity(x, i):
    others = [j for j in range(4) if j != i]
    rhs = sum((2 * x[j] - x[i]) ** 2 for j in others)
    rhs += 2 * sum((x[j] - x[k]) ** 2 for j, k in itertools.combinations(others, 2))
    assert 4 * Q(x) - 5 * x[i] ** 2 == rhs
    return rhs


def enumerate_shell():
    # Analytically 4Q(x)-5x_i^2 is the nonnegative sum of squares above.
    # Hence Q<=32 => 5x_i^2<=128 => |x_i|<=5. This is a proved complete box.
    vectors = []
    by_q = collections.defaultdict(list)
    for vector in itertools.product(range(-5, 6), repeat=4):
        q = Q(vector)
        if q <= 32:
            assert q >= 0 and (q != 0 or vector == ZERO)
            assert all(coordinate_bound_identity(vector, i) >= 0 for i in range(4))
            vectors.append(vector)
            by_q[q].append(vector)
    shell = []
    pairs_checked = 0
    for qa, aa in sorted(by_q.items()):
        for qb, bb in sorted(by_q.items()):
            if qa + qb > 32:
                continue
            for a in aa:
                for b in bb:
                    c = minus(minus(FOUR, a), b)
                    pairs_checked += 1
                    if Q(c) == 32 - qa - qb:
                        assert max(map(abs, c)) <= 5
                        shell.append((a, b, c))
    shell.sort()
    assert len(set(shell)) == len(shell)
    return shell, len(vectors), pairs_checked, dict(sorted(collections.Counter(Q(v) for v in vectors).items()))


def cycle_decomposition(permutation):
    unseen = set(range(len(permutation)))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        current = start
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = permutation[current]
        assert current == start
        cycles.append(cycle)
    return cycles


def primitive_word(word):
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(word[i] == word[i % period] for i in range(len(word))):
            return tuple(word[:period])
    raise AssertionError('unreachable')


def mod_partition(states, modulus, differences=False):
    groups = collections.defaultdict(list)
    for i, state in enumerate(states):
        coordinates = difference_coordinates(state) if differences else sum(state, ())
        groups[tuple(c % modulus for c in coordinates)].append(i)
    collision = next((members for members in groups.values() if len(members) > 1), None)
    return groups, collision


def main():
    shell, vector_count, pair_count, vector_q_counts = enumerate_shell()
    assert len(shell) == 2895
    index = {state: i for i, state in enumerate(shell)}
    permutation = []
    for state in shell:
        assert energy(state) == 32 and total(state) == FOUR and M(state) == 64
        after = F(state)
        assert energy(after) == 32 and total(after) == FOUR and M(after) == 64
        assert after in index
        permutation.append(index[after])
    assert sorted(permutation) == list(range(len(shell)))
    cycles = cycle_decomposition(permutation)
    histogram = collections.Counter(map(len, cycles))
    expected = {1: 2218, 5: 72, 9: 26, 21: 2, 41: 1}
    assert dict(histogram) == expected
    marker = [g(state) for state in shell]
    marker_indices = [i for i, bit in enumerate(marker) if bit]
    assert len(marker_indices) == 3
    forever_unmarked = []
    marked_cycles = []
    signatures = [None] * len(shell)
    for cycle in cycles:
        bits = [marker[i] for i in cycle]
        if not any(bits):
            forever_unmarked.extend(cycle)
        else:
            assert sum(bits) == 1 and len(cycle) in (21, 41)
            marked_cycles.append({'period': len(cycle), 'indices': cycle,
                                  'marker_state': shell[cycle[bits.index(1)]]})
        for offset, state_index in enumerate(cycle):
            word = bits[offset:] + bits[:offset]
            signatures[state_index] = primitive_word(word)
    assert len(forever_unmarked) == 2812
    infinite_groups = collections.defaultdict(list)
    for i, signature in enumerate(signatures):
        infinite_groups[signature].append(i)
    assert len(infinite_groups) == 63
    infinite_size_hist = collections.Counter(map(len, infinite_groups.values()))
    assert dict(infinite_size_hist) == {2812: 1, 2: 21, 1: 41}

    # Complete prefix partitions, including the sample at n=0.
    current = list(range(len(shell)))
    prefixes = [0] * len(shell)
    prefix_counts = [1]
    first_complete_horizon = None
    horizon41_witness = None
    for length in range(1, 84):
        prefixes = [2 * prefix + marker[state] for prefix, state in zip(prefixes, current)]
        current = [permutation[state] for state in current]
        groups = collections.defaultdict(list)
        for i, prefix in enumerate(prefixes):
            groups[prefix].append(i)
        prefix_counts.append(len(groups))
        ambiguous = [members for members in groups.values()
                     if len({signatures[i] for i in members}) > 1]
        if length == 41:
            assert ambiguous
            first = ambiguous[0][0]
            second = next(i for i in ambiguous[0] if signatures[i] != signatures[first])
            horizon41_witness = {
                'first_state': shell[first], 'second_state': shell[second],
                'first_infinite_word': ''.join(map(str, signatures[first])),
                'second_infinite_word': ''.join(map(str, signatures[second])),
                'common_41_sample_prefix': format(prefixes[first], '041b'),
            }
        if not ambiguous:
            first_complete_horizon = length
            assert len(groups) == len(infinite_groups)
            break
    assert first_complete_horizon == 42
    assert prefix_counts[41] < 63 and prefix_counts[42] == 63

    modular_results = []
    smallest_absolute = smallest_differences = None
    for k in range(5):
        modulus = 2 ** k
        abs_groups, abs_collision = mod_partition(shell, modulus)
        diff_groups, diff_collision = mod_partition(shell, modulus, True)
        # Sum S fixed and 3 invertible modulo 2^k: equal difference residues
        # iff equal absolute residues. Check equality of the partitions, too.
        abs_sets = {tuple(v) for v in abs_groups.values()}
        diff_sets = {tuple(v) for v in diff_groups.values()}
        assert abs_sets == diff_sets
        if abs_collision is None and smallest_absolute is None:
            smallest_absolute = k
        if diff_collision is None and smallest_differences is None:
            smallest_differences = k
        modular_results.append({
            'k': k, 'modulus': modulus,
            'absolute_residue_classes': len(abs_groups),
            'difference_residue_classes': len(diff_groups),
            'absolute_injective': abs_collision is None,
            'differences_injective': diff_collision is None,
            'same_partition_at_fixed_sum': True,
            'collision_witness': ([shell[abs_collision[0]], shell[abs_collision[1]]]
                                  if abs_collision is not None else None),
        })
    assert smallest_absolute == smallest_differences == 3

    # Also distinguish coefficient reduction modulo the rational integer 5
    # (O/5O, 625 elements) from the one-dimensional residue modulo (1-j).
    integer_moduli = []
    for modulus in range(2, 9):
        abs_groups, abs_collision = mod_partition(shell, modulus)
        diff_groups, diff_collision = mod_partition(shell, modulus, True)
        integer_moduli.append({
            'modulus': modulus,
            'absolute_residue_classes': len(abs_groups),
            'difference_residue_classes': len(diff_groups),
            'absolute_injective': abs_collision is None,
            'differences_injective': diff_collision is None,
            'absolute_collision_witness': ([shell[abs_collision[0]], shell[abs_collision[1]]]
                                           if abs_collision is not None else None),
            'difference_collision_witness': ([shell[diff_collision[0]], shell[diff_collision[1]]]
                                             if diff_collision is not None else None),
        })
    mod5 = next(row for row in integer_moduli if row['modulus'] == 5)
    assert mod5['absolute_injective'] and mod5['differences_injective']
    named_mod4_collision = ((FOUR, ZERO, ZERO), (ZERO, FOUR, ZERO))
    assert all(state in index for state in named_mod4_collision)
    assert tuple(c % 4 for c in sum(named_mod4_collision[0], ())) == tuple(
        c % 4 for c in sum(named_mod4_collision[1], ()))
    assert tuple(c % 4 for c in difference_coordinates(named_mod4_collision[0])) == tuple(
        c % 4 for c in difference_coordinates(named_mod4_collision[1]))

    result = {
        'status': 'PASS',
        'implementation': 'new absolute three-slot implementation; cyclic five-coefficient rho multiplication; no old-code imports',
        'coefficient_bound': {
            'proved_identity': '4Q(a)-5a_i^2=sum_{j!=i}(2a_j-a_i)^2+2sum_{j<k,j,k!=i}(a_j-a_k)^2',
            'consequence': 'Q<=32 implies all four coefficients in [-5,5]',
            'single_vectors_Q_at_most_32': vector_count,
            'single_vector_Q_histogram': vector_q_counts,
            'ordered_a_b_pairs_with_Qsum_at_most_32': pair_count,
            'third_slot': 'c=4-a-b; retain iff Q(c)=32-Q(a)-Q(b)',
        },
        'shell': {'E': 32, 'S': list(FOUR), 'M': 64, 'states': len(shell),
                  'cycles': len(cycles), 'cycle_count_by_period': dict(sorted(histogram.items()))},
        'marker': {'definition': 'sorted(Q(a),Q(b),Q(c))=[0,0,32]',
                   'marked_states': [shell[i] for i in marker_indices],
                   'marked_state_count': len(marker_indices),
                   'marked_cycle_periods': sorted(x['period'] for x in marked_cycles),
                   'one_mark_each_marked_cycle': True,
                   'forever_unmarked_states': len(forever_unmarked)},
        'binary_reading': {'infinite_classes': len(infinite_groups),
                           'class_size_histogram': dict(sorted(infinite_size_hist.items())),
                           'sample_origin': 'n=0 included; L samples are n=0,...,L-1',
                           'minimum_separating_samples': first_complete_horizon,
                           'latest_needed_sample_index': first_complete_horizon - 1,
                           'prefix_class_counts_from_L0': prefix_counts,
                           'sharpness_collision_at_L41': horizon41_witness},
        'modular_reading': {'minimum_k_absolute': smallest_absolute,
                            'minimum_k_differences': smallest_differences,
                            'minimum_power_of_two_modulus': 8,
                            'results': modular_results,
                            'rational_integer_moduli_2_through_8': integer_moduli,
                            'modulo_5_is_coefficient_reduction': 'O/5O, size 625 per slot; not O/(1-j), size 5',
                            'modulo_5_absolute_and_differences_injective': True,
                            'named_modulo_4_collision': named_mod4_collision,
                            'general_sufficient_bound': 'fixed M and S: absolute reduction modulo m is injective if 3m^2>M; differences also if gcd(3,m)=1'},
    }
    (HERE / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    # Complete finite witness, sufficient for independent rowwise checking.
    witness = {'states': shell, 'F_index': permutation, 'g': marker,
               'cycles': cycles,
               'infinite_classes': [{'word': ''.join(map(str, signature)), 'indices': members}
                                    for signature, members in sorted(infinite_groups.items())]}
    (HERE / 'shell_witness.json').write_text(json.dumps(witness, separators=(',', ':')) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
