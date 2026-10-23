#!/usr/bin/env python3
"""Exact finite audit of the causal open-channel reduction.

NON-CANONICAL, L1. Standard library only. The field and complete-circuit
primitive below are copied with attribution from PR #1721, frozen head
d221e10747e009cb1315295a258f1d48e8b75bce, verify.py SHA256
b58173a2853b9880e6ff5374a34b8d891c7bf8176c9f81802c4be2beaa0bd9c2.
The independently assembled projection blocks and history-current audit
are new. No imported scientific code, spatial truncation or fitted phase.
"""

from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations


# Q[z]/Phi_20(z); z is exp(i*pi/10), with z^8=z^6-z^4+z^2-1.
ZERO = (Q(0),) * 8
ONE = (Q(1),) + (Q(0),) * 7


def rat(a, b=1):
    return (Q(a, b),) + (Q(0),) * 7


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


@lru_cache(maxsize=32768)
def mul(a, b):
    if a == ZERO or b == ZERO:
        return ZERO
    v = [Q(0) for _ in range(15)]
    for j, x in enumerate(a):
        if x:
            for k, y in enumerate(b):
                if y:
                    v[j + k] += x * y
    for n in range(14, 7, -1):
        t = v[n]
        v[n - 2] += t
        v[n - 4] -= t
        v[n - 6] += t
        v[n - 8] -= t
    return tuple(v[:8])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


Z = (Q(0), Q(1)) + (Q(0),) * 6
ZPOW = tuple(power(Z, k) for k in range(20))
I = ZPOW[5]
SQRT5 = add(ONE, mul(rat(2), add(ZPOW[4], ZPOW[16])))
C = mul(SQRT5, rat(1, 5))
S = mul(SQRT5, rat(2, 5))
PHASE_BETA = ZPOW[12]
PHASE_G = ZPOW[16]


@lru_cache(maxsize=32768)
def conj(a):
    out = ZERO
    for k, value in enumerate(a):
        if value:
            out = add(out, mul(rat(value), ZPOW[(-k) % 20]))
    return out


def scalar_sum(items):
    out = ZERO
    for value in items:
        out = add(out, value)
    return out


def put(vector, key, value):
    value = add(vector.get(key, ZERO), value)
    if value == ZERO:
        vector.pop(key, None)
    else:
        vector[key] = value


def inner(a, b, weight=lambda key: 1):
    return scalar_sum(
        mul(mul(conj(value), b.get(key, ZERO)), rat(weight(key)))
        for key, value in a.items() if key in b
    )


def apply_columns(vector, column):
    out = {}
    for key, value in vector.items():
        for target, coefficient in column(key):
            put(out, target, mul(coefficient, value))
    return out


# key = (kind, R, r, carrier_position, object_coin, pulse_bank,
#        carrier_label, memory_label, receiver_position, identity_ancilla)
# kind 0 is token; kind 1 is pulse. Ancilla 1 stores fixed charge 8 to right.
def changed(key, **fields):
    names = {"kind": 0, "R": 1, "r": 2, "t": 3, "d": 4,
             "bank": 5, "label": 6, "memory": 7, "z": 8, "aux": 9}
    value = list(key)
    for name, item in fields.items():
        value[names[name]] = item
    return tuple(value)


CONTACT_KEYS = ((0, 1), (0, 2), (1, 0), (1, 3))
ALPHA = (I, neg(I), ZERO, ZERO)
BETA = (ZERO, ZERO, ONE, neg(ONE))


def contact_column(key):
    kind, R, r, t, d, bank, *_ = key
    index = (kind, d)
    if r or R != t or (kind == 1 and bank != 0) or index not in CONTACT_KEYS:
        return [(key, ONE)]
    j = CONTACT_KEYS.index(index)
    out = []
    for i, (kind_out, d_out) in enumerate(CONTACT_KEYS):
        projectors = add(mul(ALPHA[i], conj(ALPHA[j])),
                         mul(BETA[i], conj(BETA[j])))
        rotation = sub(mul(BETA[i], conj(ALPHA[j])),
                       mul(ALPHA[i], conj(BETA[j])))
        value = add(sub(ONE if i == j else ZERO,
                        mul(rat(1, 5), projectors)),
                    mul(rat(2, 5), rotation))
        out.append((changed(key, kind=kind_out, d=d_out, bank=0), value))
    return out


M = tuple(tuple(mul(rat(1, 5), value) for value in row) for row in (
    (ONE, mul(rat(2), I), mul(rat(2), I), rat(-4)),
    (mul(rat(2), I), ONE, rat(-4), mul(rat(2), I)),
    (mul(rat(2), I), rat(-4), ONE, mul(rat(2), I)),
    (rat(-4), mul(rat(2), I), mul(rat(2), I), ONE),
))
PULSE_Q = ((C, neg(S)), (S, C))


def coin_column(key):
    if key[0] == 0:
        return [(changed(key, d=j), M[j][key[4]]) for j in range(4)]
    return [(changed(key, d=j, bank=b), mul(M[j][key[4]], PULSE_Q[b][key[5]]))
            for j in range(4) for b in range(2)]


def stream_column(key):
    dr = (0, -1, 1, 0)[key[4]]
    dR = (-1, 0, 0, 1)[key[4]]
    return [(changed(key, R=key[1] + dR, r=key[2] + dr), ONE)]


def edge_column(key):
    if key[0] == 0:
        return [(key, ONE)]
    if key[5] == 0:
        right = key[3] + 1
        target = changed(key, t=right, bank=1)
        crossing = S
    else:
        right = key[3]
        target = changed(key, t=key[3] - 1, bank=0)
        crossing = neg(S)
    if key[8] == right:
        target = changed(target, label=key[7], memory=key[6])
    return [(key, C), (target, crossing)]


def phase_column(key):
    phase = mul(PHASE_BETA, PHASE_G if key[2] == 0 else ONE)
    return [(key, phase)]


def prepare(vector):
    return apply_columns(apply_columns(vector, contact_column), coin_column)


def evolve(vector):
    vector = prepare(vector)
    for operation in (stream_column, edge_column, phase_column):
        vector = apply_columns(vector, operation)
    return vector


def coordinate(key, species):
    return (key[1] + key[2], key[1] - key[2], key[3], key[8])[species]


def charge_right(key, ell):
    return sum(w * (coordinate(key, species) > ell)
               for species, w in enumerate((2, 2, 4, 2))) + 8 * key[9]


def current_column(key, ell):
    vA = (-1, -1, 1, 1)[key[4]]
    vB = (-1, 1, -1, 1)[key[4]]
    A, B = key[1] + key[2], key[1] - key[2]
    object_current = 2 * (int(A + vA > ell) - int(A > ell)
                          + int(B + vB > ell) - int(B > ell))
    out = [(key, rat(object_current))]
    if key[0] == 1 and ((key[5] == 0 and key[3] == ell)
                        or (key[5] == 1 and key[3] == ell + 1)):
        b = key[5]
        out.append((key, rat(16 if b == 0 else -16, 5)))
        target = changed(key, bank=1 - b, t=ell + 1 if b == 0 else ell)
        if key[8] == ell + 1:
            target = changed(target, label=key[7], memory=key[6])
        out.append((target, rat(8, 5)))
    return out


# The reduction uses a separate projector construction, not contact_column.
def scaled(vector, value):
    return {key: mul(value, a) for key, a in vector.items()
            if mul(value, a) != ZERO}


def summed(*vectors):
    out = {}
    for vector in vectors:
        for key, value in vector.items():
            put(out, key, value)
    return out


def sector(vector, kind):
    return {key: value for key, value in vector.items() if key[0] == kind}


def interface(vector, source, target):
    # V_target V_source^dagger, using unnormalised alpha/beta of norm sqrt(2).
    values = ({1: I, 2: neg(I)}, {0: ONE, 3: neg(ONE)})
    out = {}
    for key, value in vector.items():
        if (key[0] != source or key[2] != 0 or key[1] != key[3]
                or (source == 1 and key[5] != 0) or key[4] not in values[source]):
            continue
        coefficient = mul(mul(conj(values[source][key[4]]), value), rat(1, 2))
        for d, amplitude in values[target].items():
            put(out, changed(key, kind=target, d=d, bank=0),
                mul(amplitude, coefficient))
    return out


def free(vector):
    for operation in (coin_column, stream_column, edge_column, phase_column):
        vector = apply_columns(vector, operation)
    return vector


def block_a(vector):
    return free(summed(vector, scaled(interface(vector, 0, 0), rat(-2, 5))))


def block_b(vector):
    return scaled(free(interface(vector, 1, 0)), rat(-4, 5))


def block_g(vector):
    return scaled(free(interface(vector, 0, 1)), rat(4, 5))


def block_d(vector):
    return free(summed(vector, scaled(interface(vector, 1, 1), rat(-2, 5))))


def iter_a(vector, count):
    for _ in range(count):
        vector = block_a(vector)
    return vector


def token_terms(initial, history, m):
    return [iter_a(initial, m)] + [iter_a(block_b(history[j]), m - 1 - j)
                                    for j in range(m)]


def base_key(kind=0, R=99, r=0, t=99, d=0, bank=0,
             label=1, memory=2, z=100, aux=0):
    return (kind, R, r, t, d, bank, label, memory, z, aux)


def alpha(n=99):
    return {base_key(R=n, t=n, d=1): I,
            base_key(R=n, t=n, d=2): neg(I)}


def beta(n=99):
    return {base_key(kind=1, R=n, t=n, d=0): ONE,
            base_key(kind=1, R=n, t=n, d=3): neg(ONE)}


def dark(n=99):
    # Twice the normalised even inversion-parity state in PROOF_CURRENT.
    return {base_key(R=n-1, r=-1, t=n, d=0): ONE,
            base_key(R=n+1, r=1, t=n, d=3): ONE,
            base_key(R=n-1, r=1, t=n, d=0): neg(ONE),
            base_key(R=n+1, r=-1, t=n, d=3): neg(ONE)}


def fixtures():
    return [alpha(), beta(), beta(100),
            {base_key(kind=1, t=100, d=0, bank=1, label=2, memory=1): ONE},
            {base_key(R=102, r=-3, t=0, d=0): ONE},
            dark(),
            {base_key(kind=1, R=100, r=1, t=99, d=2,
                      label=3, memory=4, z=101, aux=1): ONE},
            {base_key(R=100, t=100, d=3, label=2, memory=1, z=99): ONE}]


def inversion(vector, n):
    return {changed(key, R=2*n-key[1], r=-key[2], d=3-key[4]): value
            for key, value in vector.items()}


def main():
    assert power(Z, 20) == ONE and power(I, 2) == rat(-1)
    assert mul(SQRT5, SQRT5) == rat(5)
    assert mul(power(PHASE_BETA, 2), PHASE_G) == ONE
    print('PASS exact cyclotomic field and source phase cancellation')

    a = alpha()
    w1 = free(a)
    w2 = free(w1)
    w3 = free(w2)
    w4 = free(w3)
    assert inner(a, a) == rat(2)
    moments = [mul(inner(a, v), rat(1, 2)) for v in (a, w1, w2, w3, w4)]
    mu4 = mul(sub(rat(80), mul(rat(28), ZPOW[4])), rat(1, 125))
    assert moments == [ONE, ZERO, rat(4, 5), ZERO, mu4]
    g = [mul(inner(a, iter_a(w1, k)), rat(1, 2)) for k in range(4)]
    g3 = mul(sub(rat(48), mul(rat(28), ZPOW[4])), rat(1, 125))
    assert g == [ZERO, rat(4, 5), ZERO, g3]
    assert g3 != conj(g3)
    assert mul(rat(-16, 25), g[1]) == rat(-64, 125)
    # Coefficients through z^4: (4+F)s = 4-F, F=1+2 mu2 z^2+2 mu4 z^4.
    f = [rat(5), ZERO, mul(rat(2), moments[2]), ZERO, mul(rat(2), moments[4])]
    s = [rat(3, 5), ZERO, rat(-64, 125), ZERO, mul(rat(-16, 25), g3)]
    lhs = [scalar_sum(mul(f[j], s[k-j]) for j in range(k+1)) for k in range(5)]
    rhs = [rat(3), ZERO, neg(f[2]), ZERO, neg(f[4])]
    assert lhs == rhs
    print('PASS source moments mu_0..mu_4, memory g_0..g_3, Schur series and nonreal g_3')

    starts = fixtures()
    steps = 4
    direct = [[v] for v in starts]
    reduced_p = [[sector(v, 1)] for v in starts]
    reconstructed = [[v] for v in starts]
    histories = [[[sector(v, 0)]] for v in starts]
    for i, initial in enumerate(starts):
        t0 = sector(initial, 0)
        for m in range(steps):
            direct[i].append(evolve(direct[i][-1]))
            terms = token_terms(t0, reduced_p[i], m)
            # Direct convolution, rather than advancing a stored token state.
            next_p = summed(block_d(reduced_p[i][m]), block_g(iter_a(t0, m)),
                            *(block_g(iter_a(block_b(reduced_p[i][j]), m-1-j))
                              for j in range(m)))
            assert next_p == summed(block_d(reduced_p[i][m]), block_g(summed(*terms)))
            reduced_p[i].append(next_p)
            next_terms = token_terms(t0, reduced_p[i], m+1)
            histories[i].append(next_terms)
            state = summed(summed(*next_terms), next_p)
            assert state == direct[i][m+1]
            reconstructed[i].append(state)
    print('PASS 8 complete-state histories through 4 periods: exact causal reconstruction')

    prepared = [[prepare(v) for v in states[:-1]] for states in reconstructed]
    local_images = {ell: [[apply_columns(v, lambda key: current_column(key, ell))
                          for v in states] for states in prepared]
                    for ell in (98, 99, 100)}
    charge_pairs = current_pairs = norm_pairs = 0
    for i in range(len(starts)):
        for j in range(len(starts)):
            for m in range(steps+1):
                xi, xj = reconstructed[i][m], reconstructed[j][m]
                assert inner(xi, xj) == inner(starts[i], starts[j])
                norm_pairs += 1
                for ell in (98, 99, 100):
                    weight = lambda key: charge_right(key, ell)
                    # Expanded two-time history Gram, including ALL cross terms.
                    gram = scalar_sum(inner(a0, b0, weight)
                                      for a0 in histories[i][m] for b0 in histories[j][m])
                    gram = add(gram, inner(reduced_p[i][m], reduced_p[j][m], weight))
                    assert gram == inner(direct[i][m], direct[j][m], weight)
                    charge_pairs += 1
                    if m < steps:
                        change = sub(inner(direct[i][m+1], direct[j][m+1], weight), gram)
                        loc = inner(prepared[i][m], local_images[ell][j][m])
                        assert change == loc
                        current_pairs += 1
    assert (norm_pairs, charge_pairs, current_pairs) == (320, 960, 768)
    print('PASS 320 mixed norm, 960 history-charge and 768 native-current pairings')

    # An incoming object carries current even while the pulse remains exactly zero.
    object_input = starts[4]
    object_output = direct[4][1]
    assert all(not sector(v, 1) for v in direct[4])
    actual = sub(inner(object_output, object_output, lambda key: charge_right(key, 99)),
                 inner(object_input, object_input, lambda key: charge_right(key, 99)))
    assert actual == rat(8, 5) and actual != ZERO
    print('PASS open-object counterexample: pulse history zero, native current 8/5')

    # Physical N_R has nonzero cyclic/dark cross terms in the ACTUAL source walk.
    # Remove the global token phase from U_T^2 alpha to obtain W^2 alpha.
    chi = scaled(w2, conj(power(PHASE_BETA, 2)))
    d = dark()
    assert inversion(chi, 99) == scaled(chi, rat(-1))
    assert inversion(d, 99) == d
    assert inner(chi, d) == ZERO
    assert inner(chi, d, lambda key: charge_right(key, 99)) == rat(8, 5)
    combination = summed(chi, d)
    diagonal_only = add(inner(chi, chi, lambda key: charge_right(key, 99)),
                        inner(d, d, lambda key: charge_right(key, 99)))
    assert sub(inner(combination, combination, lambda key: charge_right(key, 99)),
               diagonal_only) == rat(16, 5)
    print('PASS cyclic/dark native-charge interference: cross pairing 8/5 in unnormalised audit')

    # Distinct delays have nonzero Gram entries; diagonal-history deletion is false.
    g0_state = w1
    g2_state = iter_a(w1, 2)
    cross = inner(g0_state, g2_state)
    assert cross == rat(24, 25)
    assert inner(g0_state, g2_state, lambda key: charge_right(key, 99)) == rat(96, 25)
    assert inner(summed(g0_state, g2_state), summed(g0_state, g2_state)) != add(
        inner(g0_state, g0_state), inner(g2_state, g2_state))
    print('PASS coherent memory requires off-diagonal delay pairings')
    print('RESULT: PASS exact finite open-channel audit; no stationary or Hodge promotion')


if __name__ == '__main__':
    main()
