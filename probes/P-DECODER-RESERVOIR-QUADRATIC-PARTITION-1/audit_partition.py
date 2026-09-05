"""Independent exact finite audits; the uniform claims require PROOF.md."""
from dataclasses import FrozenInstanceError
from fractions import Fraction as F
from itertools import combinations, permutations, product

import partition as candidate


ORIGIN = (0, 0, 0)
NEAR = (1, 1, 0)
SOURCE_SITES = (ORIGIN, NEAR, (1, 0, 1), (0, 1, 1), (2, 0, 0))


def _field(values):
    return tuple(sorted((x, a) for x, a in values.items() if a))


def _shift(x, z):
    return tuple(a + b for a, b in zip(x, z))


def _stencil():
    values = {}
    for prototype, weight in (((1, 1, 0), 6), ((2, 0, 0), 1),
                              ((2, 2, 0), 15), ((3, 1, 0), 1), ((4, 0, 0), 1)):
        for ordering in permutations(prototype):
            for signs in product((-1, 1), repeat=3):
                values[tuple(a * s for a, s in zip(ordering, signs))] = F(weight, 324)
    return tuple(sorted(values.items()))


def _neighbor_sum(values, offsets):
    answer = {}
    for x, a in values.items():
        for z, c in offsets:
            y = _shift(x, z)
            answer[y] = answer.get(y, F(0)) + c * a
    return answer


def _reference(z, gamma, offsets):
    total = sum(z, F(0))
    u = {}
    v = dict(_field(dict(zip(SOURCE_SITES, (F(a) - total / 5 for a in z + (0,))))))
    states, ports = [(u, v)], []
    for _ in range(3):
        neighbors = _neighbor_sum(v, offsets)
        w = {}
        for x in set(u) | set(v) | set(neighbors) | set(gamma):
            g = gamma.get(x, F(0))
            h_v = F(10, 9) * v.get(x, F(0)) + neighbors.get(x, F(0))
            w[x] = (h_v - (1 - g / 2) * u.get(x, F(0))) / (1 + g / 2)
        w = dict(_field(w))
        ports.append({x: (u.get(x, F(0)) - w.get(x, F(0))) / 2 for x in gamma})
        u, v = v, w
        states.append((u, v))
    return tuple(states), tuple(ports)


def _energy(pair, offsets):
    u, v = pair
    kinetic = sum(((v.get(x, F(0)) - u.get(x, F(0))) ** 2
                   for x in set(u) | set(v)), F(0))
    neighbors = _neighbor_sum(v, offsets)
    mixed = sum((a * (F(8, 9) * v.get(x, F(0)) - neighbors.get(x, F(0)))
                 for x, a in u.items()), F(0))
    return (kinetic + mixed) / 2


def _sum_matrices(values):
    return tuple(tuple(sum((value[i][j] for value in values), F(0))
                       for j in range(4)) for i in range(4))


def _outer(row, factor=F(1)):
    return tuple(tuple(factor * a * b for b in row) for a in row)


def _quad(value, z):
    return sum((z[i] * z[j] * value[i][j] for i in range(4) for j in range(4)), F(0))


def _multiply(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(4)), F(0))
                       for j in range(4)) for i in range(4))


def _transpose(a):
    return tuple(tuple(a[j][i] for j in range(4)) for i in range(4))


def _det(value):
    answer = F(0)
    for permutation in permutations(range(len(value))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(value)) for j in range(i + 1, len(value)))
        term = F(-1 if inversions % 2 else 1)
        for i, j in enumerate(permutation):
            term *= value[i][j]
        answer += term
    return answer


def _is_psd(value):
    if value != _transpose(value):
        return False
    return all(_det(tuple(tuple(value[i][j] for j in indices) for i in indices)) >= 0
               for size in range(1, 5) for indices in combinations(range(4), size))


def _data():
    offsets = _stencil()
    basis = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    pairs = tuple(combinations(range(4), 2))
    sources = basis + tuple(tuple(basis[i][k] + basis[j][k] for k in range(4)) for i, j in pairs)
    result = []
    for gamma in ({}, {ORIGIN: F(2)}, {ORIGIN: F(1)}, {ORIGIN: F(2), NEAR: F(1, 2)}):
        context = candidate.reservoir.Context(_field(gamma), F(1))
        actual = candidate.build_prefix(context, 3)
        reference = tuple(_reference(z, gamma, offsets) for z in sources)
        residuals = []
        for horizon in range(4):
            energies = tuple(_energy(states[horizon], offsets) for states, _ in reference)
            value = [[F(0) for _ in range(4)] for _ in range(4)]
            for i in range(4):
                value[i][i] = 2 * energies[i]
            for k, (i, j) in enumerate(pairs):
                value[i][j] = value[j][i] = energies[4 + k] - energies[i] - energies[j]
            residuals.append(tuple(tuple(row) for row in value))
        result.append((context, actual, reference, tuple(residuals)))
    return offsets, sources, tuple(result)


def _g01_types_zero(data):
    _, _, records = data
    context, parts, _, _ = records[1]
    one = parts[1]
    zero = (0, 0, 0, 0)
    bad = (lambda: candidate.build(context, -1), lambda: candidate.build(context, True),
           lambda: candidate.build(object(), 0), lambda: candidate.matrix(((1, 2),)),
           lambda: candidate.matrix(((0.5, 0, 0, 0),) * 4),
           lambda: candidate.state_operator((1, 2, 3)),
           lambda: candidate.state_operator((True, 0, 0, 0)),
           lambda: candidate.group_forms(one, ()),
           lambda: candidate.group_forms(one, ((0, 0),)),
           lambda: candidate.group_forms(one, ((-1,),)),
           lambda: candidate.group_forms(one, ((True,),)),
           lambda: candidate.Partition(context.gamma, 1, (), one.residual))
    for function in bad:
        try:
            function()
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("invalid typed input accepted")
    for _, partitions, _, _ in records:
        for partition in partitions:
            assert candidate.normalized_shares(partition, zero) == "ZERO_DENOMINATOR"
    assert candidate.state_operator(zero) == "ZERO_DENOMINATOR"
    try:
        one.horizon = 7
    except FrozenInstanceError:
        pass
    else:
        raise AssertionError("mutable partition")


def _g02_independent_propagation(data):
    offsets, sources, records = data
    assert len(offsets) == 60 and sum((c for _, c in offsets), F(0)) == F(8, 9)
    assert candidate.wave.stencil() == offsets
    for context, partitions, reference, _ in records:
        gamma = dict(context.gamma)
        for horizon, partition in enumerate(partitions):
            assert (partition.gamma, partition.horizon) == (context.gamma, horizon)
            assert tuple((s.tick, s.site) for s in partition.slots) == tuple(
                (tick, x) for tick in range(horizon) for x in sorted(gamma))
            for slot in partition.slots:
                row = tuple(reference[i][1][slot.tick][slot.site] for i in range(4))
                assert slot.row == row
                assert slot.matrix == _outer(row, 2 * gamma[slot.site])
                for z, (_, ports) in zip(sources, reference):
                    assert sum((a * b for a, b in zip(row, z)), F(0)) == ports[slot.tick][slot.site]


def _g03_residual_partition_psd(data):
    metric = tuple(tuple(F(i == j) - F(1, 5) for j in range(4)) for i in range(4))
    assert candidate.gram() == metric
    for _, partitions, _, residuals in data[2]:
        for partition, independent_residual in zip(partitions, residuals):
            assert partition.residual == independent_residual
            forms = tuple(slot.matrix for slot in partition.slots) + (independent_residual,)
            assert all(_is_psd(form) for form in forms)
            assert _sum_matrices(forms) == metric
        assert partitions[0].residual == metric and partitions[0].slots == ()


def _g04_prefix_grouping(data):
    for context, partitions, _, _ in data[2]:
        for horizon, partition in enumerate(partitions):
            assert partition.slots == partitions[3].slots[:horizon * len(context.gamma)]
            count = len(partition.slots)
            groupings = (tuple((i,) for i in range(count)), (tuple(range(count)),),
                         tuple(tuple(i for i, s in enumerate(partition.slots) if s.site == x)
                               for x, _ in context.gamma))
            for groups in groupings:
                expected = tuple(_sum_matrices(tuple(partition.slots[i].matrix for i in group))
                                 for group in groups) + (partition.residual,)
                assert candidate.group_forms(partition, groups) == expected
                assert _sum_matrices(expected) == candidate.gram()
            if horizon < 3:
                next_partition = partitions[horizon + 1]
                new_forms = tuple(s.matrix for s in next_partition.slots if s.tick == horizon)
                assert partition.residual == _sum_matrices((next_partition.residual,) + new_forms)
        assert candidate.build(context, 0) == partitions[0]


def _g05_g_metric_trace(data):
    metric = candidate.gram()
    inverse = tuple(tuple(F(i == j) + 1 for j in range(4)) for i in range(4))
    identity = tuple(tuple(F(i == j) for j in range(4)) for i in range(4))
    assert candidate.gram_inverse() == inverse and _multiply(metric, inverse) == identity
    vectors = ((1, 0, 0, 0), (1, -1, 0, 0), (1, 1, 1, 1), (F(1, 2), -2, 1, F(-1, 3)))
    for _, partitions, _, _ in data[2]:
        for partition in partitions:
            forms = tuple(s.matrix for s in partition.slots) + (partition.residual,)
            effects = candidate.operator_forms(partition)
            assert effects == tuple(_multiply(inverse, form) for form in forms)
            assert _sum_matrices(effects) == identity
            assert all(_multiply(metric, effect) == _multiply(_transpose(effect), metric) for effect in effects)
            for z in vectors:
                mass = _quad(metric, z)
                shares = tuple(_quad(form, z) / mass for form in forms)
                assert candidate.normalized_shares(partition, z) == shares
                assert all(a >= 0 for a in shares) and sum(shares, F(0)) == 1
                rho = candidate.state_operator(z)
                assert sum((rho[i][i] for i in range(4)), F(0)) == 1
                assert _multiply(rho, rho) == rho
                assert _multiply(metric, rho) == _multiply(_transpose(rho), metric)
                for effect, share in zip(effects, shares):
                    product_matrix = _multiply(rho, effect)
                    assert sum((product_matrix[i][i] for i in range(4)), F(0)) == share
                    assert candidate.trace(candidate.matmul(rho, effect)) == share
    example = candidate.operator_forms(data[2][1][1][1])[0]
    assert example != _transpose(example)  # G-self-adjoint need not mean Euclidean symmetric.


def _g06_first_port_row(data):
    h = tuple(F(a, 1620) for a in (1421, -349, -349, -349))
    z_high, z_low = (1, -1, 0, 0), (1, 1, 1, 1)
    assert sum((a * b for a, b in zip(h, z_high)), F(0)) == F(59, 54)
    assert sum(h, F(0)) == F(187, 810)
    for context, partitions, _, _ in data[2][1:]:
        gamma = dict(context.gamma)[ORIGIN]
        row = tuple(-a / (2 + gamma) for a in h)
        expected_matrix = _outer(h, 2 * gamma / (2 + gamma) ** 2)
        for partition in partitions[1:]:
            slot = next(s for s in partition.slots if s.tick == 0 and s.site == ORIGIN)
            assert slot.row == row and slot.matrix == expected_matrix
        if gamma == 2:
            assert expected_matrix == _outer(h, F(1, 4))


def _g07_postprocessing_obstruction(data):
    low = tuple(tuple(F(1, 20) for _ in range(4)) for _ in range(4))
    high = tuple(tuple(F(i == j) - F(1, 4) for j in range(4)) for i in range(4))
    z_high, z_low = (1, -1, 0, 0), (1, 1, 1, 1)
    assert _sum_matrices((low, high)) == candidate.gram()
    assert _quad(low, z_high) == 0 and _quad(high, z_low) == 0
    assert _is_psd(low) and _is_psd(high)
    for _, partitions, _, _ in data[2][1:]:
        for partition in partitions[1:]:
            mixed = next(s.matrix for s in partition.slots if s.tick == 0 and s.site == ORIGIN)
            assert _quad(mixed, z_high) > 0 and _quad(mixed, z_low) > 0
            # These are the exact premises of the nonnegative postprocessing
            # lemma: the HIGH witness forces alpha=0, the LOW witness alpha=1.
            # No finite sample of alpha is substituted for that uniform proof.
            pooled = _sum_matrices(tuple(s.matrix for s in partition.slots))
            assert _quad(pooled, z_high) > 0 and _quad(pooled, z_low) > 0


def _g08_threshold_boundary(data):
    context, partitions, _, _ = data[2][1]
    partition = partitions[1]
    z, scaled = (1, -1, 0, 0), (3, -3, 0, 0)
    heat = candidate.quadratic(partition.slots[0].matrix, z) / 2
    assert heat == F(3481, 23328)
    assert candidate.quadratic(partition.slots[0].matrix, scaled) / 2 == 9 * heat
    assert candidate.normalized_shares(partition, z) == candidate.normalized_shares(partition, scaled)
    assert candidate.reservoir.threshold_counts(_field({ORIGIN: heat}), context) == ((ORIGIN, 0),)
    assert candidate.reservoir.threshold_counts(_field({ORIGIN: 9 * heat}), context) == ((ORIGIN, 1),)
    changed_threshold = candidate.reservoir.Context(context.gamma, F(7))
    assert candidate.build(changed_threshold, 1) == partition


def run_checks():
    data = _data()
    checks = (("G01_TYPES_ZERO", _g01_types_zero),
              ("G02_INDEPENDENT_PROPAGATION", _g02_independent_propagation),
              ("G03_RESIDUAL_PARTITION_PSD", _g03_residual_partition_psd),
              ("G04_PREFIX_GROUPING", _g04_prefix_grouping),
              ("G05_G_METRIC_TRACE", _g05_g_metric_trace),
              ("G06_FIRST_PORT_ROW", _g06_first_port_row),
              ("G07_POSTPROCESSING_OBSTRUCTION", _g07_postprocessing_obstruction),
              ("G08_THRESHOLD_BOUNDARY", _g08_threshold_boundary))
    answer = []
    for name, function in checks:
        try:
            function(data)
        except AssertionError:
            answer.append((name, False))
        else:
            answer.append((name, True))
    return answer
