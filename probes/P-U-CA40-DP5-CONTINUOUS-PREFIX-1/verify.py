#!/usr/bin/env python3
"""Exact support audit for P-U-CA40-DP5-CONTINUOUS-PREFIX-1.

Read only the adjacent rational tableau header. No candidate import, floating
emulation, propagation, timing, or numerical outcome prediction is performed.
The DP5/Hermite fixtures are inherited from the previous public DP5 probe;
New checks concern continuous prefix geometry and reset-sensitive chains,
not numerical accuracy or the compiled implementation.
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


def prefix_checks(c):
    dt, checkpoints, node_checks = Q(1, 160000), 0, 0
    for sign in (-1, 1):
        for labels in ((4, 3), (4, 4), (1, 1)):
            segments = [s for s in range(80) if any((label+s//16) % 5 == 0 for label in labels)]
            size = len(segments)
            require(size == (32 if labels == (4, 3) else 16), 'occupied segment inventory')
            segment = segments[0]
            require(segment == (64 if labels == (1, 1) else 16), 'first active segment')
            require(all(not any((label+s//16) % 5 == 0 for label in labels)
                        for s in range(segment)), 'exact zero-response prehistory')
            previous = segment*dt
            for checkpoint in range(4):
                qa, qc = 4*checkpoint, 3*checkpoint
                baseline = [dt*(segment+Q(qa+j, 512)) for j in range(5)]
                candidate = [dt*(segment+Q(qc+j, 384)) for j in range(4)]
                require(candidate[0] == baseline[0] and candidate[-1] == baseline[-1] and
                        candidate[-1]-candidate[0] == Q(1, 20480000) and
                        candidate[0] == previous and
                        candidate[-1] == dt*(segment+Q(checkpoint+1, 128)),
                        'adjacent blocks and equal cumulative checkpoint time')
                previous = candidate[-1]
                require(set(baseline) & set(candidate) == {baseline[0], baseline[-1]} and
                        not set(baseline) <= set(candidate) and not set(candidate) <= set(baseline),
                        'certificate-cell grids are nonnested')
                halves = [dt*(segment+Q(2*qc+j, 768)) for j in range(7)]
                require(candidate == halves[::2] and set(halves) & set(baseline) ==
                        {baseline[0], baseline[2], baseline[-1]}, 'DP halfstep boundary geometry')
                require(segment*dt <= candidate[0] < candidate[-1] <= (segment+1)*dt,
                        'no amplitude switch inside prefix block')
                require(dt*Q(2, 384) != candidate[-1]-candidate[0] and
                        candidate[0] != dt*Q(qc, 384),
                        'wrong duration and discarded absolute-clock controls')
                for cell in range(3):
                    start, h = candidate[cell], dt/384
                    for half in range(2):
                        for node in c:
                            direct = start+h*(half+node)/2
                            absolute = dt*(segment+Q(qc+cell, 384)+Q(half, 768)+node/768)
                            require(direct == absolute and start <= direct <= start+h,
                                    'absolute two-half DP stage clock')
                            node_checks += 1
                checkpoints += 1
            require(previous-segment*dt == Q(1, 5120000), 'whole prefix duration')
    return {'matched_checkpoints': checkpoints, 'wrong_duration_controls': checkpoints,
            'absolute_clock_controls': checkpoints, 'nonnested_grid_checks': checkpoints,
            'halfstep_grid_checks': checkpoints, 'absolute_DP_stage_nodes': node_checks,
            'dark_prehistory_checks': 6, 'continuous_prefix_duration_checks': 6}


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
                'two exposed targets in checkpoint-case-column layout')
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


def comparison_checks():
    count = 0
    for dimension in (2, 4, 8):
        for seed in range(5):
            truth = [Q(3, 5), Q(4, 5)]+[Q(0)]*(dimension-2)
            errors = [[Q(i-seed, 64) for i in range(dimension)],
                      [Q(2*seed-i+1, 256) for i in range(dimension)]]
            radii = [sum(map(abs, row), Q(0)) for row in errors]
            require(norm_squared(truth) == 1, 'common normalized target')
            require(all(norm_squared(row) <= radius*radius for row, radius in zip(errors, radii)),
                    'valid individual radii')
            for a, b in ((0, 1),):
                delta = [x-y for x, y in zip(errors[a], errors[b])]
                exact_square = norm_squared(delta)
                require(exact_square <= (radii[a]+radii[b])**2, 'pairwise triangle')
                squares = [square_interval(x-Q(1, 1024), x+Q(1, 1024)) for x in delta]
                lo2, hi2 = (sum((x[k] for x in squares), Q(0)) for k in (0, 1))
                lo, hi = sqrt_interval(lo2)[0], sqrt_interval(hi2)[1]
                require(lo*lo <= exact_square <= hi*hi and
                        classify(lo, hi, radii[a]+radii[b]) != 'INCONSISTENT', 'enclosed distance')
                count += 1
    require(square_interval(Q(-1, 8), Q(1, 4))[0] == 0 and
            min(Q(-1, 8)**2, Q(1, 4)**2) > 0, 'naive interval-square mutant')
    cases = ((Q(0), Q(1, 2), Q(1, 2), 'COMPATIBLE'),
             (Q(1, 2), Q(3, 4), Q(1, 4), 'INCONSISTENT'),
             (Q(1, 4), Q(3, 4), Q(1, 2), 'UNRESOLVED'),
             (Q(1, 2), Q(3, 4), Q(1, 2), 'UNRESOLVED'))
    for lo, hi, radius, expected in cases:
        require(classify(lo, hi, radius) == expected, 'classification boundary')
    require(classify(Q(0), Q(1), Q(1, 2)) == 'UNRESOLVED', 'upper-only failure mutant')
    require(classify(Q(1, 2), Q(1, 2), Q(1, 8)) == 'INCONSISTENT', 'underclaimed radius')
    screens = ((Q(0), Q(0), True), (Q(1, 1024), Q(0), False),
               (Q(1, 32), Q(1, 32), True), (Q(33, 1024), Q(1, 32), False),
               (Q(1, 64), Q(1, 32), True))
    for proposed, baseline, expected in screens:
        require((proposed <= baseline) is expected, 'zero-safe onefold engineering screen')
    timing_cases = (((Q(1), Q(2)), (Q(2), Q(2)), True),
                    ((Q(1), Q(3)), (Q(2), Q(2)), False),
                    ((Q(1), Q(4)), (Q(2), Q(2)), False),
                    ((Q(1, 8), Q(3, 16)), (Q(1, 4), Q(1, 4)), True))
    for candidate, baseline, expected in timing_cases:
        require((sum(candidate) < sum(baseline)) is expected and
                (sum(candidate)/2 < sum(baseline)/2) is expected, 'exact two-observation speed screen')
    return {'two_arm_pair_triangles': count, 'norm_enclosure_cases': count,
            'classification_cases': 4, 'naive_square_controls': 1,
            'upper_only_failure_controls': 1, 'underclaimed_radius_controls': 1,
            'onefold_screen_cases': len(screens), 'two_observation_speed_cases': len(timing_cases)}


def run_checks():
    a, b, c = read_tableau()
    counts = order_checks(a, b, c)
    for result in (fsal_checks(a, b, c), hermite_checks(), prefix_checks(c),
                   thermal_column_checks(), comparison_checks(), chain_checks()):
        counts.update(result)
    return {'status': 'PASS', 'probe': 'P-U-CA40-DP5-CONTINUOUS-PREFIX-1',
            'scope': 'exact_tableau_reconstruction_and_continuous_prefix_support',
            'counts': counts, 'arithmetic': 'stdlib_Fraction', 'kernel_executed': False,
            'IEEE_emulated': False, 'numerical_accuracy_established': False,
            'performance_established': False, 'full_trajectory_certificate': False}


if __name__ == '__main__':
    sys.stdout.buffer.write((json.dumps(run_checks(), sort_keys=True,
                                       separators=(',', ':'))+'\n').encode('ascii'))
