#!/usr/bin/env python3
"""Exact L1 audit: P-U-GALOIS-CHANNEL-OPTIMUM-1.
A. M. Thorn, Apache-2.0. No Canon status or physical adoption is asserted.
Adapted from accepted issue #1038 audit.py (blob
77e409e07056dcc5476a62df2d337b8418b3874b) and #1037 audit.py (blob
b79159da6c29c27032b0b6ff8072708c8ecd1b23).
Combined finite certificates; no predecessor execution or output reuse.
Do not execute as a formal gate before the required public pin.
"""
from fractions import Fraction as F
import json
import BREAKER

H = ((1, 1, 1, 1), (1, -1, 1, -1),
     (1, 1, -1, -1), (1, -1, -1, 1))


def zeros(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def plus(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def times(q, a):
    return [[q*x for x in row] for row in a]


def mm(a, b):
    out = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        for j, x in enumerate(row):
            if x:
                for k, y in enumerate(b[j]):
                    if y:
                        out[i][k] += x*y
    return out


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def e(n, j):
    return [F(i == j) for i in range(n)]


def outer(v, w):
    return [[x*y for y in w] for x in v]


def norm2(v):
    return sum(x*x for x in v)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def det(a):
    a = [row[:] for row in a]
    d = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            d = -d
        p = a[j][j]
        d *= p
        for i in range(j+1, len(a)):
            q = a[i][j]/p
            for k in range(j, len(a)):
                a[i][k] -= q*a[j][k]
    return d


def channel(ks, v, w):
    out = zeros(4, 4)
    for k in ks:
        out = plus(out, outer(mv(k, v), mv(k, w)))
    return out


def embed(mat, ports, size=20):
    out = identity(size)
    for i, p in enumerate(ports):
        for j, q in enumerate(ports):
            out[p][q] = mat[i][j]
    return out


def f4_block():
    # Each layer has an omitted common sqrt(2) denominator. Their product
    # has denominator 2, with no floating point or radical approximation.
    layers = []
    for pairs in (((0, 1), (2, 3)), ((0, 2), (1, 3))):
        a = zeros(4, 4)
        for i, j in pairs:
            a[i][i], a[i][j], a[j][i], a[j][j] = F(1), F(1), F(1), F(-1)
        assert mm(tr(a), a) == times(2, identity(4))
        layers.append(a)
    return times(F(1, 2), mm(layers[1], layers[0]))


def fraction_json(x):
    if isinstance(x, F):
        return str(x)
    raise TypeError(type(x).__name__)


def main():
    f = times(F(1, 2), H)
    c = [[F(H[k][a], 2) if a == b else F(0) for b in range(4)]
         for k in range(4) for a in range(4)]
    pi = mm(c, tr(c))
    q = plus(identity(16), times(-1, pi))
    d = mm(f, tr(c))
    assert mm(tr(c), c) == identity(4)
    assert mm(tr(f), f) == identity(4)
    assert mm(q, q) == q and trace(q) == 12
    assert mm(d, c) == f
    native = [[F(k == l) for k in range(4) for a in range(4)] for l in range(4)]
    assert mm(native, c) == f
    assert mm(native, tr(native)) == times(4, identity(4))
    ks = [d] + [[q[4*k+a][:] for k in range(4)] for a in range(4)]
    qs = [mv(q, e(16, i)) for i in range(16)]
    ks17 = [d] + [outer(e(4, i//4), qs[i]) for i in range(16)]
    complete17 = zeros(16, 16)
    for k in ks17:
        complete17 = plus(complete17, mm(tr(k), k))
    assert complete17 == identity(16)
    assert all(mm(k, c) == zeros(4, 4) for k in ks17[1:])
    dilation17 = [ks17[mu][k][:] for k in range(4) for mu in range(17)]
    assert mm(tr(dilation17), dilation17) == identity(16)
    assert mm(dilation17, c) == [
        f[k][:] if mu == 0 else [F(0)]*4
        for k in range(4) for mu in range(17)]
    complete = zeros(16, 16)
    for k in ks:
        complete = plus(complete, mm(tr(k), k))
    assert complete == identity(16)
    assert all(mm(k, c) == zeros(4, 4) for k in ks[1:])
    # Residual 16 output ports first, followed by central four.
    u = [q[i][:]+c[i][:] for i in range(16)] + [d[k][:]+[F(0)]*4 for k in range(4)]
    assert mm(tr(u), u) == mm(u, tr(u)) == identity(20)
    dilation = [ks[mu][k][:] for k in range(4) for mu in range(5)]
    assert mm(tr(dilation), dilation) == identity(16)
    unit_checks = cross_checks = 0
    for a in range(4):
        va, fa = mv(c, e(4, a)), mv(f, e(4, a))
        for b in range(4):
            assert channel(ks, va, mv(c, e(4, b))) == outer(fa, mv(f, e(4, b)))
            assert channel(ks17, va, mv(c, e(4, b))) == outer(fa, mv(f, e(4, b)))
            unit_checks += 1
        for i in range(16):
            qi = mv(q, e(16, i))
            assert channel(ks, va, qi) == zeros(4, 4)
            assert channel(ks, qi, va) == zeros(4, 4)
            assert channel(ks17, va, qi) == zeros(4, 4)
            assert channel(ks17, qi, va) == zeros(4, 4)
            cross_checks += 2
    # Independent construction of the loader and the physical-component product.
    block = f4_block()
    assert block == f
    groups = [[4*k+a for k in range(4)] for a in range(4)]
    b20 = identity(20)
    for ports in groups:
        b20 = mm(embed(block, ports), b20)
    neg_ports = [4*k+a for k in range(4) for a in range(4) if H[k][a] == -1]
    z20 = identity(20)
    for i in neg_ports:
        z20[i][i] = F(-1)
    loader = mm(z20, b20)
    loaded = [row[:4] for row in loader]
    assert loaded == c+zeros(4, 4)
    swap = identity(20)
    for a in range(4):
        swap[a], swap[16+a] = swap[16+a], swap[a]
    final_f = embed(block, [16, 17, 18, 19])
    stages = [z20, b20, swap, b20, z20, final_f]
    net = identity(20)
    for stage in stages:
        net = mm(stage, net)
    assert net == u
    assert mm(u, loaded) == zeros(16, 4)+f
    assert mm(tr(loader), loader) == identity(20)
    # Component sequence, preserving fixed phase conventions and all ports.
    def f_entry(ports):
        return {'operation': 'F4', 'ports': ports,
                'hadamard_pairs_in_time_order': [[ports[0], ports[1]], [ports[2], ports[3]],
                                                 [ports[0], ports[2]], [ports[1], ports[3]]]}
    netlist = ([{'operation': 'PHASE_MINUS', 'ports': neg_ports}]
               + [f_entry(ports) for ports in groups]
               + [{'operation': 'SWAP', 'pairs': [[a, 16+a] for a in range(4)]}]
               + [f_entry(ports) for ports in groups]
               + [{'operation': 'PHASE_MINUS', 'ports': neg_ports}, f_entry([16, 17, 18, 19])])
    assert len(neg_ports) == 6
    assert sum(4 for item in netlist if item['operation'] == 'F4') == 36
    # Complete raw output information, including a distinction from #1037.
    raw_densities, raw_powers, coordinate_laws = [], [], []
    raw17_densities = []
    for i in range(16):
        out = channel(ks, e(16, i), e(16, i))
        out17 = channel(ks17, e(16, i), e(16, i))
        raw17_densities.append(out17)
        law = [out[k][k] for k in range(4)]
        assert [out17[k][k] for k in range(4)] == law
        assert trace(out17) == trace(out) == 1
        assert law == [F(5, 8) if k == i//4 else F(1, 8) for k in range(4)]
        vout = mv(u, e(20, i))
        powers = [x*x for x in vout]
        assert sum(powers) == 1
        regrouped = [powers[16+k]+sum(powers[4*k+a] for a in range(4)) for k in range(4)]
        assert regrouped == law
        raw_densities.append(out)
        raw_powers.append(powers)
        coordinate_laws.append(law)
    old00 = outer(mv(d, e(16, 0)), mv(d, e(16, 0)))
    for i in range(16):
        old00[i//4][i//4] += q[i][0]**2
    assert old00 == raw17_densities[0]
    assert old00[0][1] == F(1, 16) and raw_densities[0][0][1] == F(-1, 8)
    agreements = [coordinate_laws[i][i//4] for i in range(16)]
    assert sum(agreements) == 10
    assert min(agreements) == sum(agreements)/16 == F(5, 8)
    assert 1+F(3, 4)*trace(q) == 10
    # A point-exact channel is incompatible with full coherent code transfer.
    point_ks = [[[F(l == k and a == b)
                  for k in range(4) for b in range(4)]
                 for l in range(4)] for a in range(4)]
    point_complete = zeros(16, 16)
    for op in point_ks:
        point_complete = plus(point_complete, mm(tr(op), op))
    assert point_complete == identity(16)
    for i in range(16):
        assert channel(point_ks, e(16, i), e(16, i)) == outer(e(4, i//4), e(4, i//4))
    point_alpha = [F(1, 2)]*4
    coded = mv(c, point_alpha)
    target = outer(mv(f, point_alpha), mv(f, point_alpha))
    point_output = channel(point_ks, coded, coded)
    assert target == outer(e(4, 0), e(4, 0))
    assert point_output == times(F(1, 4), identity(4))
    assert channel(ks, coded, coded) == channel(ks17, coded, coded) == target
    # Exact finite ingredients for the universal auxiliary lower proof.
    simplex = plus(identity(4), times(F(-1, 4), [[F(1)]*4 for _ in range(4)]))
    rs = [mv(simplex, e(4, k)) for k in range(4)]
    minor = [[r[i]**2 for r in rs] for i in range(4)]
    assert det(minor) == F(3, 32)
    effect_ranks, slacks = [], []
    effect_sum = zeros(16, 16)
    for k in range(4):
        effect = zeros(16, 16)
        for a in range(4):
            qi = mv(q, e(16, 4*k+a))
            assert norm2(qi) == F(3, 4)
            effect = plus(effect, outer(qi, qi))
            qa = [[q[i][j] if i % 4 == a and j % 4 == a else F(0)
                   for j in range(16)] for i in range(16)]
            slack = plus(times(F(3, 4), qa), times(-1, outer(qi, qi)))
            assert tr(slack) == slack and mm(slack, slack) == times(F(3, 4), slack)
            assert trace(slack)*F(4, 3) == 2
            slacks.append(2)
        assert trace(effect) == 3 and mm(effect, effect) == times(F(3, 4), effect)
        effect_ranks.append(trace(effect)*F(4, 3))
        effect_sum = plus(effect_sum, effect)
    assert effect_sum == q
    kg = [[sum(ki[r][s]*kj[r][s] for r in range(4) for s in range(16))
           for kj in ks] for ki in ks]
    assert kg == [[F((4 if i == 0 else 3) if i == j else 0) for j in range(5)] for i in range(5)]
    assert det(kg) == 324
    code_controls = []
    for j in range(4):
        alpha = mv(f, e(4, j))
        vin = mv(c, alpha)+[F(0)]*4
        assert all(x*x == F(1, 16) for x in vin[:16])
        output = mv(u, vin)
        assert output == e(20, 16+j)
        code_controls.append({'alpha': alpha, 'bright_port': 16+j})
    complement = []
    for k in range(1, 4):
        for a in range(4):
            vin = mv(loader, e(20, 4*k+a))
            assert mv(u, vin) == vin and norm2(vin) == 1
            complement.append(4*k+a)
    # Nonoptimal exact-code isometry with only four environment states.
    v4 = [[f[l][a]*f[mu][k]*H[k][a] for k in range(4) for a in range(4)]
          for l in range(4) for mu in range(4)]
    assert mm(tr(v4), v4) == identity(16)
    assert mm(v4, c) == [f[l][:] if mu == 0 else [F(0)]*4 for l in range(4) for mu in range(4)]
    for i in range(16):
        out = mv(v4, e(16, i))
        assert [sum(out[4*l+mu]**2 for mu in range(4)) for l in range(4)] == [F(1, 4)]*4
    defect = mv(c, mv(f, e(4, 0)))+[F(0)]*4
    defect[0] = -defect[0]
    dout = mv(u, defect)
    assert norm2(dout) == 1
    assert dout[16:] == [F(7, 8), F(-1, 8), F(-1, 8), F(-1, 8)]
    assert norm2(dout[16:]) == F(13, 16) and norm2(dout[:16]) == F(3, 16)
    # Coarse versus resolved-and-forgotten HIGH measurement, externally assumed.
    y = [F(0), F(1), F(1), F(0)]  # y/sqrt(2), handled in its dyad.
    coarse = times(F(1, 2), outer(y, y))
    fine = zeros(4, 4)
    fine[1][1] = fine[2][2] = F(1, 2)
    bright = coarse
    assert trace(mm(bright, coarse)) == 1 and trace(mm(bright, fine)) == F(1, 2)
    assert channel(ks, [F(0)]*16, [F(0)]*16) == zeros(4, 4)
    print(json.dumps({
        'proposed_probe': 'P-U-GALOIS-CHANNEL-OPTIMUM-1',
        'scope': 'finite exact L1 certificates; theorem acceptance and physical adoption are separate',
        'checks': {'source_matrix_units_per_channel': unit_checks, 'cross_terms_per_channel': cross_checks,
                   'channels_checked': ['Phi5', 'Phi17'],
                   'raw_signal_columns': 16, 'full_unitary_columns': 20, 'complement_controls': len(complement)},
        'certificates': {'auxiliary_dimension_attained': 5, 'effect_ranks': effect_ranks,
                         'outer_product_minor': det(minor), 'kraus_gram': kg, 'kraus_gram_determinant': det(kg),
                         'positive_slack_ranks': slacks, 'coordinate_agreement': F(5, 8)},
        'unitary20': u, 'coupling_netlist': netlist,
        'loader_netlist': [f_entry(ports) for ports in groups]+[{'operation': 'PHASE_MINUS', 'ports': neg_ports}],
        'component_counts': {'coupling_balanced_mixers': 36, 'coupling_negative_phases': 12,
                             'coupling_swaps': 4, 'loader_balanced_mixers': 16, 'loader_negative_phases': 6},
        'raw_signal_output_powers': raw_powers, 'raw_coordinate_laws': coordinate_laws,
        'phi5_raw_densities': raw_densities, 'phi17_raw_densities': raw17_densities,
        'point_exact_control': {'alpha': point_alpha, 'output': point_output, 'target': target},
        'code_controls': code_controls, 'complement_input_labels': complement,
        'four_environment_control_coordinate_law': [F(1, 4)]*4,
        'phase_flip_00_control': {'central_amplitudes': dout[16:], 'central_power': norm2(dout[16:]),
                                  'residual_power': norm2(dout[:16])},
        'high_coherence_control': {'retained_bright_weight': trace(mm(bright, coarse)),
                                   'resolved_then_forgotten_bright_weight': trace(mm(bright, fine))},
        'limits': ['External optical/channel comparison, not U-derived coupling.',
                   'Matched loader cancellation is an explicit validation limitation.',
                   'No prepared apparatus, recorded event, archive, reset or layer lift.',
                   'Finite execution alone does not establish complete-class theorems.']
    }, default=fraction_json, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
    print(BREAKER.check())
