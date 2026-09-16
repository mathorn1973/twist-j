"""ACCEPTED PROTOCOL / NON-CANONICAL / RESULT-EXPOSED / ZERO RUNS AT PIN.

Future exact audit of a direct 40-mode circuit against independent 5x5 maps.
No downloads, physical data, floats, stochastic trials or mutable outputs.
The written proof carries universal mixer and lattice claims; finite gates
audit its identities, not an empirical result or an infinite enumeration.
"""

from fractions import Fraction as F
from itertools import permutations, product

import apparatus as circuit
import record_audit


def zero(n, m=None):
    return tuple(tuple(F(0) for _ in range(n if m is None else m)) for _ in range(n))


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(c, a):
    return tuple(tuple(F(c) * x for x in row) for row in a)


def trans(a):
    return tuple(zip(*a))


def mm(a, b):
    bt = trans(b)
    return tuple(tuple(sum((x*y for x, y in zip(row, col)), F(0))
                       for col in bt) for row in a)


def mv(a, v):
    return tuple(sum((x*y for x, y in zip(row, v)), F(0)) for row in a)


def outer(a, b):
    return tuple(tuple(x*y for y in b) for x in a)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def vadd(a, b):
    return tuple(x+y for x, y in zip(a, b))


def vscale(c, v):
    return tuple(F(c)*x for x in v)


def unit(n, i):
    return tuple(F(j == i) for j in range(n))


I5 = eye(5)
PI = add(I5, scale(F(-1, 5), tuple(tuple(F(1) for _ in range(5)) for _ in range(5))))
BASIS = tuple(vadd(unit(5, i), vscale(-1, unit(5, 4))) for i in range(4))


def simplex(k):
    return tuple(F(i == k) - F(1, 5) for i in range(5))


def reference(k):
    """Independent cell formulas, not the circuit's path-gate construction."""
    g = tuple(tuple(F(i == (2*j-k) % 5) for j in range(5)) for i in range(5))
    powers = [I5]
    for _ in range(3):
        powers.append(mm(g, powers[-1]))
    p = scale(F(5, 4), outer(simplex(k), simplex(k)))
    q = add(PI, scale(-1, p))
    r = scale(F(1, 4), add(add(PI, scale(-1, mm(g, PI))),
                           add(mm(powers[2], PI), scale(-1, mm(powers[3], PI)))))
    c = add(q, scale(-1, r))
    j = mm(g, c)
    kraus = (p, r, scale(F(1, 2), add(c, j)), scale(F(1, 2), add(c, scale(-1, j))))
    return p, q, r, c, j, tuple(powers), kraus


REF = tuple(reference(k) for k in range(5))


def refmap(k, variant, branch, rho):
    p, q, _, _, _, powers, _ = REF[k]
    low = mm(mm(p, rho), p)
    if branch == 0:
        return low
    if variant == "E":
        return mm(mm(q, rho), q)
    twirl = zero(5)
    for g in powers:
        twirl = add(twirl, scale(F(1, 4), mm(mm(g, rho), trans(g))))
    return add(twirl, scale(-1, low))


def maps_from_terminals(k, variant, terminal=circuit.terminal):
    """Extract all circuit Kraus maps on the entire basis of V."""
    images = tuple(terminal(k, variant, b) for b in BASIS)
    return tuple(tuple(tuple(images[column][path][row] for column in range(4))
                       for row in range(4)) for path in range(len(images[0])))


def super_from_kraus(kraus):
    # rho=sum_{p,q} rho[p,q] BASIS[p] BASIS[q]^T. Its top-left block is rho.
    return tuple(tuple(sum((a[i][p]*a[j][q] for a in kraus), F(0))
                       for p in range(4) for q in range(4))
                 for i in range(4) for j in range(4))


def reference_super(k, variant, branch):
    columns = []
    for p in range(4):
        for q in range(4):
            out = refmap(k, variant, branch, outer(BASIS[p], BASIS[q]))
            columns.append(tuple(out[i][j] for i in range(4) for j in range(4)))
    return trans(tuple(columns))


def coarse_super(kraus, variant, branch):
    chosen = tuple(a for path, a in enumerate(kraus)
                   if circuit.branch_of_channel(variant, path) == branch)
    return super_from_kraus(chosen)


def gate_01_full_circuit():
    for k in range(5):
        v_columns, e_columns, r_columns = [], [], []
        for x in range(40):
            basis = unit(40, x)
            v = circuit.apply_v(basis, k)
            e = circuit.apply_e(basis, k)
            r = circuit.apply_r(basis, k)
            v_columns.append(v)
            e_columns.append(e)
            r_columns.append(r)
            assert circuit.apply_v(v, k, inverse=True) == basis
            assert circuit.apply_v(circuit.apply_v(basis, k, inverse=True), k) == basis
            fourth = basis
            for _ in range(4):
                fourth = circuit.apply_v(fourth, k)
            assert fourth == basis
            assert circuit.apply_e(e, k) == basis
            assert circuit.apply_v(circuit.apply_flag(r), k, inverse=True) == basis
            assert circuit.apply_flag(circuit.apply_flag(basis)) == basis
            assert all(16 % z.denominator == 0 for z in e)
        for columns in (v_columns, e_columns, r_columns):
            assert all(dot(columns[i], columns[j]) == int(i == j)
                       for i in range(40) for j in range(40))
        # All 32 basis states of the restricted ambient space remain in it.
        for r in range(4):
            for b in range(2):
                for vector in BASIS:
                    state = tuple(vector[x] if (rr, bb) == (r, b) else F(0)
                                  for rr in range(4) for bb in range(2) for x in range(5))
                    for out in (circuit.apply_v(state, k), circuit.apply_e(state, k),
                                circuit.apply_r(state, k)):
                        assert all(sum(out[10*rr+5*bb:10*rr+5*bb+5], F(0)) == 0
                                   for rr in range(4) for bb in range(2))


def gate_02_prepared_and_system_maps():
    # External source-label comparison only; never an input to circuit construction.
    # Decoder order Y0,...,Y4 is transported to phase labels 0,1,3,4,2.
    beta = (0, 1, 3, 4, 2)
    source_images = []
    low_images = []
    for i in range(4):
        centered = tuple(F(j == i) - F(1, 5) for j in range(5))
        phase_vector = tuple(centered[beta.index(label)] for label in range(5))
        source_images.append(phase_vector)
        low_images.append(circuit.terminal(2, "E", phase_vector)[0])
    for i, j in product(range(4), repeat=2):
        assert dot(source_images[i], source_images[j]) == F(i == j) - F(1, 5)
        assert dot(low_images[i], low_images[j]) == F(1, 20)
    for k in range(5):
        p, q, r, c, j, powers, reference_kraus = REF[k]
        assert tuple(sum(a[i][i] for i in range(5)) for a in (p, r, c)) == (1, 1, 2)
        for a in (p, r, c):
            assert trans(a) == a and mm(a, a) == a
        assert mm(p, r) == mm(p, c) == mm(r, c) == zero(5)
        assert trans(j) == scale(-1, j) and mm(j, j) == scale(-1, c)
        assert scale(F(1, 4), sum_matrices(tuple(mm(g, PI) for g in powers))) == p
        for v in BASIS + (tuple(F(0) for _ in range(5)),):
            assert circuit.terminal(k, "E", v) == (mv(p, v), mv(q, v))
            assert circuit.terminal(k, "R", v) == tuple(mv(a, v) for a in reference_kraus)
        for variant in ("E", "R"):
            kraus = maps_from_terminals(k, variant)
            for branch in (0, 1):
                actual = coarse_super(kraus, variant, branch)
                independent = reference_super(k, variant, branch)
                assert actual == independent
                assert mm(actual, actual) == actual
            lo = coarse_super(kraus, variant, 0)
            hi = coarse_super(kraus, variant, 1)
            assert mm(lo, hi) == mm(hi, lo) == zero(16)
            # Trace preservation in the nonorthogonal e_i-e_4 system basis.
            metric = tuple(tuple(F(1 + int(i == j)) for j in range(4)) for i in range(4))
            assert sum_matrices(tuple(mm(mm(trans(a), metric), a) for a in kraus)) == metric


def sum_matrices(matrices):
    result = zero(len(matrices[0]), len(matrices[0][0]))
    for a in matrices:
        result = add(result, a)
    return result


def gate_03_all_two_stage_maps():
    # Fine paths are retained across both apparatuses. No coherent merging
    # of different first histories is hidden in the density-map composition.
    systems = {(k, v): maps_from_terminals(k, v) for k in range(5) for v in ("E", "R")}
    refs = {(k, v, b): reference_super(k, v, b)
            for k in range(5) for v in ("E", "R") for b in (0, 1)}
    for k, l, first, second in product(range(5), range(5), ("E", "R"), ("E", "R")):
        left, right = systems[k, first], systems[l, second]
        sequences = {(i, j): mm(b, a) for i, a in enumerate(left) for j, b in enumerate(right)}
        # Independently feed the direct circuit through both stages on all V basis vectors.
        for column, v in enumerate(BASIS):
            once = circuit.terminal(k, first, v)
            for i, a in enumerate(once):
                for j, out in enumerate(circuit.terminal(l, second, a)):
                    coefficients = tuple(sequences[i, j][row][column] for row in range(4))
                    assert out == coefficients + (-sum(coefficients, F(0)),)
        for b1, b2 in product((0, 1), repeat=2):
            maps = tuple(a for (i, j), a in sequences.items()
                         if circuit.branch_of_channel(first, i) == b1
                         and circuit.branch_of_channel(second, j) == b2)
            assert super_from_kraus(maps) == mm(refs[l, second, b2], refs[k, first, b1])


def gate_04_discriminating_preparations():
    for k in range(5):
        a, b, c = (k+1) % 5, (k+2) % 5, (k+4) % 5
        v = vadd(unit(5, a), vscale(-1, unit(5, c)))
        assert circuit.q(v) == 2
        for variant, at_b, at_a in (("E", F(0), F(5, 8)), ("R", F(5, 16), F(5, 16))):
            terminal = circuit.terminal(k, variant, v)
            high = tuple(w for index, w in enumerate(terminal)
                         if circuit.branch_of_channel(variant, index) == 1)
            assert sum((circuit.q(w) for w in high), F(0)) == 2
            assert sum((circuit.q(circuit.terminal(b, "E", w)[0]) for w in high), F(0))/2 == at_b
            assert sum((circuit.q(circuit.terminal(a, "E", w)[0]) for w in high), F(0))/2 == at_a
        for j in range(5):
            if j == k:
                continue
            source = simplex(j)
            for variant, joint in (("E", F(225, 256)), ("R", F(75, 256))):
                paths = circuit.terminal(k, variant, source)
                high = tuple(w for index, w in enumerate(paths)
                             if circuit.branch_of_channel(variant, index) == 1)
                mass = sum((circuit.q(w) for w in high), F(0))
                numerator = sum((circuit.q(circuit.terminal(j, "E", w)[0]) for w in high), F(0))
                assert mass/circuit.q(source) == F(15, 16)
                assert numerator/circuit.q(source) == joint
                assert numerator/mass == (F(15, 16) if variant == "E" else F(5, 16))


def gate_05_balanced_class_audit():
    # A finite audit of universal proof identities: all 24 group orders,
    # all 16 balanced column signs, and genuinely different rational completions.
    cases = [(circuit.W, order) for order in permutations(range(4))]
    for signs in product((-1, 1), repeat=4):
        cases.append((tuple(tuple(signs[i]*x for x in row) for i, row in enumerate(circuit.W)), (0, 1, 2, 3)))
    for t in (F(-2), F(-1, 3), F(1, 2), F(3)):
        cosine, sine = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        completion = ( (F(1), F(0), F(0), F(0)),
                       (F(0), cosine, -sine, F(0)),
                       (F(0), sine, cosine, F(0)),
                       (F(0), F(0), F(0), F(1)) )
        cases.append((mm(circuit.W, completion), (0, 1, 2, 3)))
    for k in range(5):
        for mixer, order in cases:
            assert all(mixer[i][0]**2 == F(1, 4) for i in range(4))
            custom = lambda kk, vv, x: circuit.terminal_with_mixer(kk, vv, x, mixer, order)
            for v in BASIS:
                assert custom(k, "E", v) == circuit.terminal(k, "E", v)
            actual_r = maps_from_terminals(k, "R", custom)
            for branch in (0, 1):
                assert coarse_super(actual_r, "R", branch) == reference_super(k, "R", branch)


def gate_06_lattices_and_polynomial():
    # Conjugating V by H makes it the integral controlled permutation D.
    h = scale(2, circuit.W)
    h_inv = scale(F(1, 4), h)
    for k in range(5):
        for r, b in product(range(4), range(2)):
            for vector in BASIS:
                state = tuple(vector[x] if (rr, bb) == (r, b) else F(0)
                              for rr in range(4) for bb in range(2) for x in range(5))
                conjugate = circuit._mix(circuit.apply_v(circuit._mix(state, h_inv), k), h)
                moved = [F(0)] * 40
                for x in range(5):
                    moved[10*r+5*b+(k+pow(2, r, 5)*(x-k)) % 5] = vector[x]
                assert conjugate == tuple(moved)
    # Concrete failure of path projection on H^-1 L^4, L=A4.
    primitive = BASIS[0]
    member = tuple(primitive[x]/4 if b == 0 else F(0)
                   for r in range(4) for b in range(2) for x in range(5))
    assert all(x.denominator == 1 for x in circuit._mix(member, h))
    projected = member[:10] + (F(0),)*30
    assert any(x.denominator != 1 for x in circuit._mix(projected, h))
    # Every ordered distinct pair contains the stated invariant reflection plane.
    for i, j in permutations(range(5), 2):
        reflection_i = add(scale(2, REF[i][0]), scale(-1, PI))
        reflection_j = add(scale(2, REF[j][0]), scale(-1, PI))
        for v in (simplex(i), simplex(j)):
            state = vadd(circuit.prepare(v, 0), vscale(-1, circuit.prepare(v, 1)))
            e = circuit.apply_e(state, i)
            rv = mv(reflection_i, v)
            assert e == vadd(circuit.prepare(rv, 0), vscale(-1, circuit.prepare(rv, 1)))
            once = circuit.apply_e(circuit.apply_e(state, j), i)
            twice = circuit.apply_e(circuit.apply_e(once, j), i)
            assert vadd(vadd(vscale(4, twice), vscale(7, once)), vscale(4, state)) == (F(0),)*40
            assert mv(mm(reflection_i, reflection_j), v) == once[:5]
        assert dot(simplex(i), simplex(j))**2/(circuit.q(simplex(i))*circuit.q(simplex(j))) == F(1, 16)
    assert F(7, 4)**2 - 4 == F(-15, 16)


def gate_07_zero_and_validation():
    for k in range(5):
        for variant, count in (("E", 2), ("R", 4)):
            assert circuit.terminal(k, variant, (F(0),)*5) == ((F(0),)*5,)*count
    bad_calls = (
        lambda: circuit.terminal(True, "E", BASIS[0]),
        lambda: circuit.terminal(5, "E", BASIS[0]),
        lambda: circuit.terminal(0, "unknown", BASIS[0]),
        lambda: circuit.terminal(0, "E", (1, 0, 0, 0, 0)),
        lambda: circuit.terminal(0, "E", (True, 0, 0, 0, -1)),
        lambda: circuit.apply_v((F(0),)*40, 0, order=(0, 0, 2, 3)),
    )
    for call in bad_calls:
        try:
            call()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input was accepted")


def gate_08_record_model():
    count = record_audit.run_checks(circuit.terminal)
    assert type(count) is int and count > 0


def main():
    gates = (
        ("G01_FULL_CIRCUIT", gate_01_full_circuit),
        ("G02_PREPARED_COMPLETE_SYSTEM_MAPS", gate_02_prepared_and_system_maps),
        ("G03_ALL_TWO_STAGE_MAPS", gate_03_all_two_stage_maps),
        ("G04_DISCRIMINATING_PREPARATIONS", gate_04_discriminating_preparations),
        ("G05_BALANCED_CLASS_AUDIT", gate_05_balanced_class_audit),
        ("G06_LATTICES_AND_POLYNOMIAL", gate_06_lattices_and_polynomial),
        ("G07_ZERO_AND_VALIDATION", gate_07_zero_and_validation),
        ("G08_RECORD_MODEL", gate_08_record_model),
    )
    for name, gate in gates:
        gate()
        print(name + " PASS")
    print("P-QDD-STABILIZER-APPARATUS-1 EXACT MODEL AUDIT PASS")


if __name__ == "__main__":
    main()
