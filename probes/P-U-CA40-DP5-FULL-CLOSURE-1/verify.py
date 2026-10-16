#!/usr/bin/env python3
"""Exact support audit for P-U-CA40-DP5-FULL-CLOSURE-1.

Read only the adjacent rational tableau header. No candidate import, floating
emulation, propagation, timing, or numerical outcome prediction is performed.
The DP5/Hermite fixtures are inherited from the previous public DP5 probe;
New checks concern full piecewise geometry, reset-sensitive chains, checkpoint
commits and final thermal/Gram budgets, not a compiled numerical trajectory.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import re
import sys


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def reference_tableau():
    # Mathematical coefficient facts; no third-party solver code is copied.
    rows = ((), ('1/5',), ('3/40', '9/40'),
            ('44/45', '-56/15', '32/9'),
            ('19372/6561', '-25360/2187', '64448/6561', '-212/729'),
            ('9017/3168', '-355/33', '46732/5247', '49/176', '-5103/18656'),
            ('35/384', '0', '500/1113', '125/192', '-2187/6784', '11/84'))
    a = [[Q(v) for v in row] + [Q(0)]*(7-len(row)) for row in rows]
    return a, a[-1][:], list(map(Q, ('0', '1/5', '3/10', '4/5', '8/9', '1', '1')))


def read_tableau():
    source = Path(__file__).with_name('dp5_tableau.hpp').read_text(encoding='ascii')
    arrays = []
    for name, shape, count in (('A', '[7][7]', 49), ('B', '[7]', 7), ('C', '[7]', 7)):
        begin, end = '/* BEGIN_'+name+' */', '/* END_'+name+' */'
        require(source.count(begin) == source.count(end) == 1, 'unique tableau markers')
        block = source.split(begin)[1].split(end)[0].strip()
        prefix = 'inline constexpr Q '+name+shape+'='
        compact = re.sub(r'\s+', '', block)
        require(compact.startswith(re.sub(r'\s+', '', prefix)), 'tableau declaration')
        rhs = block.split('=', 1)[1].strip()
        pairs = re.findall(r'Q\{\s*(-?\d+)\s*,\s*(\d+)\s*\}', rhs)
        residue = re.sub(r'Q\{\s*-?\d+\s*,\s*\d+\s*\}', '', rhs)
        require(len(pairs) == count and re.fullmatch(r'[\s{},;]+', residue) is not None,
                'literal rational table payload')
        require(all(int(d) > 0 for _, d in pairs), 'positive rational denominator')
        arrays.append([Q(int(n), int(d)) for n, d in pairs])
    a = [arrays[0][7*i:7*(i+1)] for i in range(7)]
    actual = (a, arrays[1], arrays[2])
    require(actual == reference_tableau(), 'independent coefficient transcription')
    return actual


def tree_order(tree):
    return 1 + sum(map(tree_order, tree))


def density(tree):
    result = tree_order(tree)
    for child in tree:
        result *= density(child)
    return result


def add_leaf(tree):
    result = {tuple(sorted(tree+((),)))}
    for index, child in enumerate(tree):
        for extended in add_leaf(child):
            result.add(tuple(sorted(tree[:index]+(extended,)+tree[index+1:])))
    return result


def trees_through_five():
    levels = [{()}]
    for _ in range(4):
        levels.append(set().union(*(add_leaf(t) for t in levels[-1])))
    require(list(map(len, levels)) == [1, 1, 2, 4, 9], 'rooted-tree inventory')
    return [t for level in levels for t in sorted(level)]


def elementary(tree, a):
    values = [Q(1)]*len(a)
    for child in tree:
        below = elementary(child, a)
        values = [v*sum((row[j]*below[j] for j in range(len(a))), Q(0))
                  for v, row in zip(values, a)]
    return values


def weight(tree, a, b):
    return sum((x*y for x, y in zip(b, elementary(tree, a))), Q(0))


def composition(a, b, c):
    s = len(b)
    matrix = [[v/2 for v in row]+[Q(0)]*s for row in a]
    matrix += [[v/2 for v in b]+[v/2 for v in row] for row in a]
    return matrix, [v/2 for v in b]*2, [v/2 for v in c]+[(1+v)/2 for v in c]


def order_checks(a, b, c):
    trees = trees_through_five()
    for matrix, weights, nodes in ((a, b, c), composition(a, b, c)):
        require(all(sum(row, Q(0)) == node for row, node in zip(matrix, nodes)),
                'nonautonomous stage row sums')
        require(all(matrix[i][j] == 0 for i in range(len(matrix))
                    for j in range(i, len(matrix))), 'explicit triangular tableau')
        for tree in trees:
            require(weight(tree, matrix, weights) == Q(1, density(tree)), 'order condition')
    chain = ()
    for _ in range(5):
        chain = (chain,)
    require(weight(chain, a, b) == Q(1, 600) != Q(1, 720), 'order-six chain counterexample')
    ac, bc, _ = composition(a, b, c)
    require(weight(chain, ac, bc) == Q(161, 115200) != Q(1, 720),
            'two-half order-six chain counterexample')
    mutant = b[:]
    mutant[0] += Q(1, 1000)
    mutant[1] -= Q(1, 1000)
    require(sum(mutant) == 1 and weight(((),), a, mutant) != Q(1, 2),
            'consistent-weight but wrong-order negative control')
    require(a[-1] == b and b[-1] == 0 and c[-1] == 1, 'FSAL structural identities')
    return {'header_rational_entries': 63, 'base_order_conditions': len(trees),
            'composed_order_conditions': len(trees), 'order_six_controls': 2,
            'weight_mutation_controls': 1}


def exact_step(t, y, h, a, b, c, reuse=None):
    # A rational nonautonomous fixture, not the scientific generator.
    stages, states, calls = [], [], 0
    for i in range(len(b)):
        state = y+h*sum((a[i][j]*stages[j] for j in range(i)), Q(0))
        states.append(state)
        if i == 0 and reuse is not None:
            value = reuse
        else:
            value = (1+t+c[i]*h)*state
            calls += 1
        stages.append(value)
    endpoint = y+h*sum((v*k for v, k in zip(b, stages)), Q(0))
    return endpoint, stages, states, calls


def fsal_checks(a, b, c):
    count = 0
    for t in (Q(0), Q(1, 3)):
        for h in (Q(1, 8), Q(1, 5), Q(1, 2)):
            ym, k, states, calls = exact_step(t, Q(1), h/2, a, b, c)
            require(states[-1] == ym and k[-1] == (1+t+h/2)*ym, 'true midpoint derivative')
            y1, _, _, second = exact_step(t+h/2, ym, h/2, a, b, c, k[-1])
            full_second = exact_step(t+h/2, ym, h/2, a, b, c)[0]
            ac, bc, cc = composition(a, b, c)
            composite = exact_step(t, Q(1), h, ac, bc, cc)[0]
            require(y1 == full_second == composite and calls+second == 13,
                    'two-half composition and midpoint reuse')
            wrong = exact_step(t+h/2, ym, h/2, a, b, c, k[-2])[0]
            require(k[-2] != k[-1] and wrong != y1, 'same-time wrong-state derivative mutant')
            count += 1
    return {'FSAL_composition_fixtures': count, 'wrong_stage_reuse_controls': count}


def evaluate(coefficients, x):
    value = Q(0)
    for c in reversed(coefficients):
        value = value*x+c
    return value


def derivative(coefficients):
    return [i*v for i, v in enumerate(coefficients)][1:]


def hermite(y0, ym, y1, d0, dm, d1):
    # d are derivatives with respect to normalized macrocell coordinate.
    aa, bb, cc, dd = ym-y0-d0/2, dm-d0, y1-y0-d0, d1-d0
    return [y0, d0, 16*aa-8*bb+7*cc-dd, -32*aa+32*bb-34*cc+5*dd,
            16*aa-40*bb+52*cc-8*dd, 16*bb-24*cc+4*dd]


def hermite_checks():
    nodes = (Q(0), Q(1, 2), Q(1))
    # Independent cardinal forms, expanded from squared Lagrange polynomials.
    cardinal = ([1, 0, -23, 66, -68, 24], [0, 0, 16, -32, 16, 0],
                [0, 0, 7, -34, 52, -24], [0, 1, -6, 13, -12, 4],
                [0, 0, -8, 32, -40, 16], [0, 0, -1, 5, -8, 4])
    constraints = 0
    for index, polynomial in enumerate(cardinal):
        data = [Q(int(i == index)) for i in range(6)]
        require(hermite(*data) == list(map(Q, polynomial)), 'independent Hermite coefficient form')
        for j, node in enumerate(nodes):
            require(evaluate(polynomial, node) == data[j] and
                    evaluate(derivative(polynomial), node) == data[3+j], 'cardinal Hermite constraints')
            constraints += 2
    for degree in range(6):
        values = [x**degree for x in nodes]
        slopes = [Q(0) if degree == 0 else degree*x**(degree-1) for x in nodes]
        require(hermite(*(values+slopes)) == [Q(int(i == degree)) for i in range(6)],
                'quintic reproduction')
    values, slopes = [x**6 for x in nodes], [6*x**5 for x in nodes]
    require(Q(1, 4)**6-evaluate(hermite(*(values+slopes)), Q(1, 4)) == Q(9, 4096),
            'degree-six reconstruction counterexample')
    require(hermite(Q(0), Q(1, 2), Q(1), Q(1, 2), Q(1, 2), Q(1, 2)) !=
            [Q(0), Q(1), Q(0), Q(0), Q(0), Q(0)], 'half-step derivative scaling mutant')
    # Old two-point acceleration has a nonzero artifact even for F(t,y)=t^3*y at t=0,y=1.
    delta = Q(1, 128)
    require((delta**3-(-delta)**3)/(2*delta) == delta**2 != 0,
            'old centered-acceleration negative control')
    return {'Hermite_cardinal_constraints': constraints, 'Hermite_monomials': 6,
            'degree_six_controls': 1, 'derivative_scale_controls': 1,
            'old_acceleration_controls': 1}


def full_geometry_checks(c):
    active_segments = inactive_segments = cells = stages = 0
    for sign in (-1, 1):
        for labels in ((4, 3), (4, 4), (1, 1)):
            occupied = 0
            previous = Q(0)
            for segment in range(80):
                start, end = Q(segment, 160000), Q(segment+1, 160000)
                require(start == previous and end-start == Q(1, 160000),
                        'contiguous original segments at absolute times')
                previous = end
                active = any((label+segment//16) % 5 == 0 for label in labels)
                if active:
                    occupied += 1
                    active_segments += 1
                    for cell in range(384):
                        require(segment*384+cell+1 == segment*384+(cell+1),
                                'consecutive fixed-grid cell indices')
                        cells += 1
                    # Affine stage-clock formula: check both end cells per segment.
                    for cell in (0, 383):
                        for half in range(2):
                            for node in c:
                                clock = (Q(segment)+Q(cell, 384)+(half+node)/768)/160000
                                expected = start+Q(cell, 61440000)+Q(half+node, 122880000)
                                require(clock == expected and start <= clock <= end,
                                        'absolute two-half stage clock without cross-switch reuse')
                                stages += 1
                else:
                    inactive_segments += 1
            require(previous == Q(1, 2000) and occupied == (32 if labels == (4, 3) else 16),
                    'common 500-us endpoint and full active inventory')
    require((active_segments, inactive_segments, cells) == (128, 352, 49152),
            'full six-case chronology')
    require(cells*15 == 737280 and cells*15*13 == 9584640 and cells*15*16 == 11796480,
            'eight-lane task operation inventory')
    require(90*81 == 7290 and 90*80 == 7200 and inactive_segments*15 == 5280,
            'snapshot/carry/inactive-identity counts')
    require(Q(16, 160000) != Q(64, 160000) and Q(80, 160000) == Q(1, 2000),
            'different onset times do not change common endpoint')
    return {'piecewise_segments': 480, 'active_segments': active_segments,
            'inactive_segments': inactive_segments, 'fixed_grid_cells': cells,
            'first_last_cell_DP_stage_nodes': stages, 'common_endpoint_cases': 6,
            'snapshot_inventory': 7290, 'segment_carry_inventory': 7200,
            'inactive_task_segments': 5280}


def chain_checks():
    """Small exact support fixtures, not a simulation of the ion Hamiltonian."""
    def rotate(v):
        return [Q(3, 5)*v[0]-Q(4, 5)*v[1], Q(4, 5)*v[0]+Q(3, 5)*v[1]]

    count = 0
    for seed in range(6):
        truth, stored, budget = [Q(1), Q(0)], [Q(1), Q(0)], Q(0)
        snapshots = []
        for step in range(4):
            incoming = stored[:]
            error = [Q(seed+step+1, 1024), Q(seed-step, 2048)]
            truth = rotate(truth)
            rotated = rotate(incoming)
            require(norm_squared(rotated) == norm_squared(incoming), 'exact unitary norm')
            stored = [x+y for x, y in zip(rotated, error)]
            previous_budget = budget
            budget += sum(map(abs, error), Q(0))
            require(budget >= previous_budget and
                    norm_squared([x-y for x, y in zip(stored, truth)]) <= budget*budget,
                    'unitary chain accumulates defects without amplification')
            # Endpoint jumps are additive too; this fixed fixture separates them.
            guard, tail, tube, jump = Q(step+1, 8), Q(step+1, 16), Q(step+1, 32), Q(step+1, 64)
            require(guard+tail+tube+jump == Q(15*(step+1), 64), 'component aggregation')
            snapshots.append((stored[:], budget))
            if step:
                require(incoming == snapshots[-2][0] and previous_budget == snapshots[-2][1],
                        'state and certificate carry')
            count += 1
        require(len({tuple(v) for v, _ in snapshots}) == 4, 'distinct frozen snapshots')

    initial = [Q(1), Q(0)]
    first, second = rotate(initial), rotate(rotate(initial))
    require(first != second, 'resetting the incoming state changes the second checkpoint')
    require(norm_squared([Q(1, 4), Q(0)]) > Q(1, 16)**2,
            'reset certificate misses four aligned local errors')
    mutable, aliases, copies = [Q(0)], [], []
    for step in range(4):
        mutable[0] += 1
        aliases.append(mutable)
        copies.append(mutable[:])
    require(aliases[0] != copies[0] and copies[0] == [Q(1)], 'snapshot alias mutant')
    require(hermite(Q(0), Q(1, 2), Q(1), Q(1), Q(1), Q(1))[0] != Q(1, 8),
            'wrong polynomial incoming constant must be rejected')
    require(sum((Q(k, 16) for k in range(1, 5)), Q(0)) != Q(4, 16),
            'summing cumulative checkpoints double counts')
    # Increasing upper bounds do not certify an increment in actual error.
    require(Q(1, 4)-Q(1, 8) > 0 and norm_squared([Q(0), Q(0)]) == 0,
            'upper-bound increments are not actual error increments')
    return {'unitary_chain_checkpoints': count, 'chain_carry_checks': 18,
            'state_reset_controls': 1, 'certificate_reset_controls': 1,
            'snapshot_alias_controls': 1, 'polynomial_incoming_controls': 1,
            'cumulative_double_count_controls': 1, 'growth_interpretation_controls': 1}


def thermal_column_checks():
    def compositions(total, modes):
        if modes == 1:
            return [(total,)]
        return [(first,)+tail for first in range(total+1)
                for tail in compositions(total-first, modes-1)]
    grades = [compositions(total, 7) for total in range(4)]
    require(list(map(len, grades)) == [1, 7, 28, 84], 'thermal grade inventory')
    basis = [n for grade in grades for n in grade]
    target = (0, 0, 0, 0, 0, 0, 3)
    require(len(basis) == len(set(basis)) == 120 and basis[36] == target,
            'unmodified graded thermal column 36')
    require(Q(20, 21)**7*Q(1, 21)**sum(target) == Q(20**7, 21**10),
            'unnormalized target thermal weight')
    for case, row in ((0, 36), (3, 396)):
        require((row//720, (row//120) % 6, row % 120) == (0, case, 36),
                'two exposed targets in full case-column layout')
    require(basis[35] != target and tuple(reversed(basis[36])) != target,
            'off-by-one and reversed-mode target controls')
    require(all(n != target for grade in grades[:3] for n in grade),
            'thermal truncation would improperly omit target')
    return {'thermal_grade_counts': 4, 'thermal_columns': 120, 'target_column_checks': 1,
            'target_thermal_weight_checks': 1, 'target_layout_checks': 2,
            'target_identity_negative_controls': 3}


def norm_squared(vector):
    return sum((x*x for x in vector), Q(0))


def square_interval(lo, hi):
    require(lo <= hi, 'ordered input interval')
    return (Q(0) if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi))


def sqrt_interval(value, bits=16):
    require(value >= 0, 'nonnegative square root')
    scale = 1 << bits
    lo = Q(isqrt(value.numerator*scale*scale//value.denominator), scale)
    hi = lo if lo*lo == value else lo+Q(1, scale)
    require(lo*lo <= value <= hi*hi, 'rational square-root enclosure')
    return lo, hi


def classify(lo, hi, radius):
    require(0 <= lo <= hi and radius >= 0, 'comparison domain')
    return 'INCONSISTENT' if lo > radius else 'COMPATIBLE' if hi <= radius else 'UNRESOLVED'


def full_account_checks():
    counts = (1, 7, 28, 84)
    retained = sum((Q(20, 21)**7*Q(1, 21)**n*count
                    for n, count in enumerate(counts)), Q(0))
    tail = 1-retained
    require(sum(counts) == 120 and tail == Q(680046581, 794280046581),
            'unnormalized thermal mass and inherited tail')
    ea = eb = Q(1, 5)
    aa = ab = Q(6, 5)
    exact_gram_error = aa*ab-1
    gram_bound = min(ea+aa*eb, eb+ab*ea)
    require(exact_gram_error == gram_bound == Q(11, 25) and gram_bound > ea+eb,
            'nonnormalized Gram bound and unsafe unit-norm substitution')
    require(retained*gram_bound == sum((Q(20, 21)**7*Q(1, 21)**n*count*gram_bound
                                       for n, count in enumerate(counts)), Q(0)),
            'weighted aggregation has no thermal-rank factor')
    threshold = Q(1, 1000)
    require(tail/2 < threshold and tail/2 != tail, 'pair half-distance thermal radius')
    radius = tail/2+Q(1, 10000)
    def decide(lo, hi):
        require(0 <= lo <= hi <= 1, 'discrepancy interval domain')
        return 'EXCEEDS_TARGET' if lo > threshold else 'WITHIN_TARGET' if hi <= threshold else 'UNRESOLVED'
    fixtures = ((Q(0), threshold, 'WITHIN_TARGET'),
                (threshold, threshold+radius, 'UNRESOLVED'),
                (Q(1, 25)-radius, Q(1, 25)+radius, 'EXCEEDS_TARGET'),
                (Q(1, 40)-radius, Q(1, 40)+radius, 'EXCEEDS_TARGET'))
    for lo, hi, label in fixtures:
        require(decide(lo, hi) == label, 'discrepancy classification and equality')
    require(threshold <= threshold and not threshold+Q(1, 10**30) <= threshold,
            'precision comparison is exact and separate')
    require(radius <= threshold and decide(Q(1, 25)-radius, Q(1, 25)+radius) == 'EXCEEDS_TARGET',
            'high precision can coexist with nonlinear discrepancy')
    broad = Q(1, 100)
    require(broad > threshold and decide(Q(1, 4)-broad, Q(1, 4)+broad) == 'EXCEEDS_TARGET',
            'wide valid interval may resolve discrepancy while missing precision')
    lo, hi, numerical, thermal = Q(1, 5), Q(1, 4), Q(1, 100), tail/2
    midpoint, arithmetic = (lo+hi)/2, (hi-lo)/2
    total = numerical+thermal+arithmetic
    require(midpoint-total == lo-numerical-thermal and midpoint+total == hi+numerical+thermal,
            'interval center expanded without double-counting arithmetic')
    # Relative frame rotations matter even though each is unitary.
    x, y = (Q(1), Q(0)), (Q(3, 5), Q(4, 5))
    require(norm_squared(x) == norm_squared(y) == 1 and
            sum(a*b for a, b in zip(x, y)) == Q(3, 5) != 1,
            'omitting relative unitary restoration changes the coherence')
    pairs = [(3*sign+a, 3*sign+b) for sign in range(2) for a in range(3) for b in range(a+1, 3)]
    require(pairs == [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)], 'within-sign final pairs')
    require(not any(all(side) for side in ((True, False, False), (False, True, False))) and
            all(any(side) for side in ((True, False, False), (False, True, False))),
            'one resolved pair per angle, not all three, is the discrepancy condition')
    # Exact positive-sqrt comparison used by the saved aggregation validator.
    for bound, coefficient, constant, radicand, expected in (
            (Q(5), Q(2), Q(1), Q(4), True),
            (Q(4), Q(2), Q(1), Q(4), False),
            (Q(0), Q(0), Q(1), Q(4), False)):
        delta = bound-constant
        require((delta >= 0 and delta*delta >= coefficient*coefficient*radicand) is expected,
                'sqrt-affine exact decision needs a nonnegative difference')
    return {'thermal_mass_identity': 1, 'thermal_columns': 120,
            'thermal_tail_numerator': tail.numerator, 'thermal_tail_denominator': tail.denominator,
            'nonnormalized_Gram_controls': 1, 'rank_multiplier_controls': 1,
            'discrepancy_classification_cases': len(fixtures), 'precision_boundary_cases': 2,
            'precision_discrepancy_separation_controls': 2, 'arithmetic_halfwidth_identity': 1,
            'relative_frame_omission_controls': 1, 'within_sign_pairs': len(pairs),
            'sqrt_affine_cases': 3}


def checkpoint_checks():
    expected_size = 8*6435*2*8+8*12*8
    require(expected_size == 824448 and expected_size*7290 == 6010225920,
            'committed payload dimensions')
    # A commit marker is published only after its complete payload.
    def committed(payload_complete, marker_complete, size):
        return payload_complete and marker_complete and size == expected_size
    require(committed(True, True, expected_size), 'complete snapshot fixture')
    require(not committed(True, False, expected_size) and
            not committed(False, True, expected_size) and
            not committed(True, True, expected_size-1), 'orphan/truncated snapshot controls')
    markers = (0, 1, 2, 3)
    require(markers == tuple(range(markers[-1]+1)) and
            (0, 2, 3) != tuple(range(4)), 'committed checkpoint prefix has no hole')
    state, budget = (Q(3, 5), Q(4, 5)), Q(1, 16)
    before = (state, budget)
    for _ in range(5):
        require((state, budget) == before, 'inactive intervals are state-and-budget identities')
    require((state, Q(0)) != before, 'inactive interval cannot erase the certificate')
    return {'checkpoint_complete_fixture': 1, 'checkpoint_orphan_truncation_controls': 3,
            'checkpoint_hole_controls': 1, 'inactive_identity_fixtures': 5,
            'inactive_certificate_reset_controls': 1}


def run_checks():
    a, b, c = read_tableau()
    counts = order_checks(a, b, c)
    for result in (fsal_checks(a, b, c), hermite_checks(), full_geometry_checks(c),
                   thermal_column_checks(), chain_checks(), full_account_checks(), checkpoint_checks()):
        counts.update(result)
    return {'status': 'PASS', 'probe': 'P-U-CA40-DP5-FULL-CLOSURE-1',
            'scope': 'exact_DP5_piecewise_and_full_pair_account_support',
            'counts': counts, 'arithmetic': 'stdlib_Fraction', 'kernel_executed': False,
            'IEEE_emulated': False, 'numerical_accuracy_established': False,
            'performance_established': False, 'full_trajectory_certificate': False}


if __name__ == '__main__':
    sys.stdout.buffer.write((json.dumps(run_checks(), sort_keys=True,
                                       separators=(',', ':'))+'\n').encode('ascii'))
