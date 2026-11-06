#!/usr/bin/env python3
"""Exact finite audit of the full encoded circuit and its physical cut.

NON-CANONICAL, L1. Standard library only. No numerical boundary condition,
momentum fitting, scattering-channel projection, or external data are used.
The universal statements are proved in the accompanying proof files.
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


def fixtures():
    keys = []
    # Both contact sites, every object coin, both arrangements and pulse banks.
    for R in (99, 100):
        for d in range(4):
            keys.append((0, R, 0, R, d, 0, 1, 2, 100, 0))
            for bank in range(2):
                keys.append((1, R, 0, R, d, bank, 1, 2, 100, 0))
    # Both incident pulse banks with the same object spectators and swapped labels.
    for d in range(4):
        keys.append((1, 99, 0, 100, d, 1, 2, 1, 100, 0))
    # Dark/contact-orthogonal directions, noncontact relative positions,
    # receiver at another site, and orthogonal occupied ancillary states.
    keys.extend((
        (0, 99, 1, 99, 1, 0, 2, 1, 100, 0),
        (1, 100, -1, 99, 2, 0, 2, 1, 100, 0),
        (1, 99, 0, 99, 0, 0, 1, 2, 101, 0),
        (1, 99, 0, 100, 0, 1, 1, 2, 101, 0),
        (0, 100, 0, 100, 2, 0, 1, 2, 100, 1),
        (1, 99, 0, 100, 3, 1, 2, 1, 100, 1),
    ))
    assert len(keys) == len(set(keys)) == 34
    return keys


def boundary_form(key_i, key_j, out_i, out_j, species, ell):
    ni, nj = coordinate(key_i, species), coordinate(key_j, species)
    if ni not in (ell, ell + 1) or nj not in (ell, ell + 1):
        return ZERO
    if ni == nj == ell + 1:
        return neg(inner(out_i, out_j,
                         lambda key: coordinate(key, species) == ell))
    return inner(out_i, out_j,
                 lambda key: coordinate(key, species) == ell + 1)


def determinant(matrix):
    n = len(matrix)
    out = ZERO
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        value = rat(-1 if inversions % 2 else 1)
        for i in range(n):
            value = mul(value, matrix[i][perm[i]])
        out = add(out, value)
    return out


def main():
    assert power(Z, 20) == ONE and ZPOW[10] == rat(-1)
    assert mul(I, I) == rat(-1) and mul(SQRT5, SQRT5) == rat(5)
    assert add(mul(C, C), mul(S, S)) == ONE
    for k in range(20):
        assert mul(ZPOW[k], conj(ZPOW[k])) == ONE
    print("PASS exact cyclotomic field: Phi20, phases, coin normalization")

    keys = fixtures()
    inputs = [{key: ONE} for key in keys]
    prepared = [prepare(vector) for vector in inputs]
    outputs = [evolve(vector) for vector in inputs]
    for i, left in enumerate(outputs):
        for j, right in enumerate(outputs):
            assert inner(left, right) == (ONE if i == j else ZERO)
    print("PASS complete encoded circuit: 34 columns, 1156 unitary pairings")

    currents_by_cut = {}
    for ell in (98, 99, 100):
        currents = [apply_columns(vector, lambda key: current_column(key, ell))
                    for vector in prepared]
        currents_by_cut[ell] = currents
        for i in range(len(keys)):
            for j in range(len(keys)):
                direct = sub(inner(outputs[i], outputs[j],
                                   lambda key: charge_right(key, ell)),
                             inner(inputs[i], inputs[j],
                                   lambda key: charge_right(key, ell)))
                derived = inner(prepared[i], currents[j])
                assert direct == derived, ("native-current", ell, i, j)
    print("PASS physical current: 3468 exact mixed pairings at cuts 98.5,99.5,100.5")

    for species in range(4):
        for i, key_i in enumerate(keys):
            for j, key_j in enumerate(keys):
                direct = sub(inner(outputs[i], outputs[j],
                                   lambda key: coordinate(key, species) > 99),
                             inner(inputs[i], inputs[j],
                                   lambda key: coordinate(key, species) > 99))
                boundary = boundary_form(key_i, key_j, outputs[i], outputs[j], species, 99)
                assert direct == boundary, ("Green", species, i, j)
                if species == 3:
                    assert boundary == ZERO
    print("PASS full slice Green form: 4624 pairings, standing receiver included")

    # Direct finite-interval continuity from two adjacent cuts, including
    # each coherent mixed pairing; no stationary plane-wave norm is used.
    for i in range(len(keys)):
        for j in range(len(keys)):
            density = lambda key: charge_right(key, 98) - charge_right(key, 100)
            change = sub(inner(outputs[i], outputs[j], density),
                         inner(inputs[i], inputs[j], density))
            incoming = currents_by_cut[98][j]
            outgoing = currents_by_cut[100][j]
            assert change == sub(inner(prepared[i], incoming), inner(prepared[i], outgoing))
    print("PASS local continuity: 1156 two-site mixed balances, no spectator trace")

    # At P=0 the exact free object characteristic polynomial is
    # (lambda-1)^2[lambda^2-2(cos(q)-4)lambda/5+1].
    # These finite coefficient evaluations audit the proof's determinant
    # identity; they do not replace its algebraic proof or Weyl sequence.
    samples = 0
    for qphase in (ONE, I, rat(-1), neg(I), ZPOW[4], ZPOW[8]):
        diag = (ONE, qphase, conj(qphase), ONE)
        cosq = mul(rat(1, 2), add(qphase, conj(qphase)))
        for spectral in (rat(0), ONE, I, rat(2), ZPOW[4]):
            matrix = [[sub(spectral if i == j else ZERO, mul(diag[i], M[i][j]))
                       for j in range(4)] for i in range(4)]
            rhs = mul(power(sub(spectral, ONE), 2),
                      add(sub(power(spectral, 2),
                              mul(mul(rat(2, 5), sub(cosq, rat(4))), spectral)), ONE))
            assert determinant(matrix) == rhs
            samples += 1
    # sqrt(5) in (11/5,9/4) gives phi in (8/5,13/8), hence
    # 4-5*phi/2 in (-1/16,0); the window adds at most 1/200.
    assert Q(11, 5) ** 2 < 5 < Q(9, 4) ** 2
    assert -1 < Q(-1, 16) - Q(1, 200) < Q(1, 200) < 1
    print("PASS open-token premise: 30 free-symbol identities and exact whole-window bounds")
    print("RESULT PASS: finite audit only; universal current, relation and no-inverse use proofs")


if __name__ == "__main__":
    main()
