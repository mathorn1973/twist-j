#!/usr/bin/env python3
"""Frozen exact audit of one NON-CANONICAL bound-charge/field comparison.

No external input, randomness, floating point, network, or output files.
Ring pairs represent a+b*phi, phi**2=phi+1. This is not a particle derivation.
"""
from itertools import combinations, permutations, product
from math import gcd
import json

ZERO = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
S = (2, -1)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def times(n, a):
    return (n * a[0], n * a[1])


def mul(a, b):
    return (a[0] * b[0] + a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def sm(a):
    return (2 * a[0] - a[1], -a[0] + a[1])


def sign(a):
    r, t = 2 * a[0] + a[1], a[1]
    if t == 0:
        return (r > 0) - (r < 0)
    if r >= 0 and t >= 0:
        return 1
    if r <= 0 and t <= 0:
        return -1
    d = r * r - 5 * t * t
    return ((d > 0) - (d < 0)) * (1 if r > 0 else -1)


def total(values):
    out = ZERO
    for value in values:
        out = add(out, value)
    return out


def va(a, b):
    assert len(a) == len(b)
    return [add(x, y) for x, y in zip(a, b)]


def vs(a, b):
    assert len(a) == len(b)
    return [sub(x, y) for x, y in zip(a, b)]


def dot(a, b):
    assert len(a) == len(b)
    return total(mul(x, y) for x, y in zip(a, b))


def apply(rows, vector):
    return [total(times(c, vector[i]) for i, c in row.items()) for row in rows]


def adjoint(rows, vector, size):
    out = [ZERO] * size
    for row, value in zip(rows, vector):
        for i, c in row.items():
            out[i] = add(out[i], times(c, value))
    return out


class Complex:
    def __init__(self, lengths):
        self.vertices = list(product(*(range(n) for n in lengths)))
        lookup = {x: i for i, x in enumerate(self.vertices)}
        b = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
        pairs = list(combinations(range(4), 2))
        self.edges = [(x, ij) for x in self.vertices for ij in pairs]
        elook = {key: i for i, key in enumerate(self.edges)}
        self.ne = len(self.edges)
        self.nv = len(self.vertices)

        def shift(x, delta):
            return tuple((x[d] + delta[d]) % lengths[d] for d in range(3))

        self.G = []
        for x, (i, j) in self.edges:
            y = shift(x, tuple(b[j][d] - b[i][d] for d in range(3)))
            row = {lookup[x]: -1}
            row[lookup[y]] = row.get(lookup[y], 0) + 1
            self.G.append(row)
        self.C = []
        for x in self.vertices:
            for i, j, k in combinations(range(4), 3):
                for orientation in (1, -1):
                    row = {}
                    for h, t, c in ((i, j, 1), (j, k, 1), (i, k, -1)):
                        delta = b[h] if orientation == 1 else tuple(-z for z in b[t])
                        index = elook[(shift(x, delta), (h, t))]
                        row[index] = row.get(index, 0) + orientation * c
                    self.C.append(row)
        self.P = [{} for _ in self.edges]
        for row in self.C:
            for i, a in row.items():
                for j, c in row.items():
                    self.P[i][j] = self.P[i].get(j, 0) + a * c

    def stiff(self, vector):
        return apply(self.P, vector)

    def div(self, vector):
        return adjoint(self.G, vector, self.nv)


class Law:
    def __init__(self, complex_, selected):
        self.c = complex_
        self.selected = tuple(selected)
        assert len(set(self.selected)) == len(self.selected)
        assert all(0 <= i < self.c.ne for i in self.selected)
        self.m = len(self.selected)
        self.sizes = (self.c.ne, self.c.ne, self.m, self.m)

    def gamma(self, vector):
        out = [ZERO] * self.c.ne
        for i, value in zip(self.selected, vector):
            out[i] = sm(value)
        return out

    def gamma_t(self, vector):
        return [sm(vector[i]) for i in self.selected]

    def zero(self):
        return tuple([ZERO] * n for n in self.sizes)

    def step(self, state, feedback=True):
        a, e, x, v = state
        xn = va(x, v)
        en = vs(vs(e, [sm(z) for z in self.c.stiff(a)]), self.gamma(v))
        an = va(a, en)
        vn = vs(v, [sm(z) for z in xn])
        if feedback:
            vn = va(vn, self.gamma_t(en))
        return an, en, xn, vn

    def inverse(self, state):
        an, en, xn, vn = state
        v = vs(va(vn, [sm(z) for z in xn]), self.gamma_t(en))
        x = vs(xn, v)
        a = vs(an, en)
        e = va(va(en, [sm(z) for z in self.c.stiff(a)]), self.gamma(v))
        return a, e, x, v

    def shear_step(self, state):
        a, e, x, v = state
        d = va(e, self.gamma(x))
        xn = va(x, v)
        # Independent spatial multiplication route: C^T(C A), not stored P.
        pa = adjoint(self.c.C, apply(self.c.C, a), self.c.ne)
        dn = vs(d, [sm(z) for z in pa])
        en = vs(dn, self.gamma(xn))
        return va(a, en), en, xn, va(vs(v, [sm(z) for z in xn]), self.gamma_t(en))

    def parts(self, state):
        a, e, x, v = state
        field = add(dot(e, e), sm(dot(a, self.c.stiff(vs(a, e)))))
        matter = add(dot(v, v), sm(dot(va(x, v), x)))
        interaction = neg(dot(e, self.gamma(v)))
        return field, matter, interaction

    def energy(self, state):
        return total(self.parts(state))

    def defect(self, state):
        return self.c.div(va(state[1], self.gamma(state[2])))

    def charge(self, state):
        return [neg(z) for z in self.c.div(self.gamma(state[2]))]

    def check(self, state, out):
        a, e, x, v = state
        an, en, xn, vn = out
        assert self.inverse(out) == state
        assert self.step(self.inverse(state)) == state
        assert out == self.shear_step(state)
        p, pn = self.parts(state), self.parts(out)
        assert total(p) == total(pn)
        assert sub(pn[0], p[0]) == neg(dot(self.gamma(v), va(en, e)))
        assert sub(pn[1], p[1]) == dot(en, self.gamma(va(vn, v)))
        assert self.defect(state) == self.defect(out)
        assert vs(self.charge(out), self.charge(state)) == [neg(z) for z in self.c.div(self.gamma(v))]
        assert total(self.charge(state)) == ZERO
        ca = apply(self.c.C, a)
        ce_sum = apply(self.c.C, va(en, e))
        ca_prev = apply(self.c.C, vs(a, e))
        ca_next = apply(self.c.C, an)
        for old_b, b, new_b, d in zip(ca_prev, ca, ca_next, ce_sum):
            assert sm(sub(mul(new_b, b), mul(b, old_b))) == sm(mul(b, d))
        pa_incidence = adjoint(self.c.C, ca, self.c.ne)
        j = self.gamma(v)
        for old_e, new_e, pa_i, ji in zip(e, en, pa_incidence, j):
            assert sub(mul(new_e, new_e), mul(old_e, old_e)) == neg(
                mul(add(sm(pa_i), ji), add(new_e, old_e)))
        for m, edge in enumerate(self.selected):
            old_local = sub(add(mul(v[m], v[m]), sm(mul(add(x[m], v[m]), x[m]))),
                            sm(mul(e[edge], v[m])))
            new_local = sub(add(mul(vn[m], vn[m]), sm(mul(add(xn[m], vn[m]), xn[m]))),
                            sm(mul(en[edge], vn[m])))
            assert sub(new_local, old_local) == sm(mul(v[m], add(en[edge], e[edge])))
        cm = apply(self.c.C, vs([times(2, z) for z in a], e))
        xm = va([times(2, z) for z in x], v)
        lower4 = total((sm(dot(cm, cm)), sm(dot(xm, xm)),
                        mul(sub((4, 0), times(10, S)), dot(e, e)),
                        mul(sub((4, 0), times(3, S)), dot(v, v))))
        assert sign(sub(times(4, self.energy(state)), lower4)) >= 0
        assert sign(self.energy(state)) >= 0


def poly_add(a, b):
    out = [ZERO] * max(len(a), len(b))
    for i, z in enumerate(a):
        out[i] = add(out[i], z)
    for i, z in enumerate(b):
        out[i] = add(out[i], z)
    return out


def poly_mul(a, b):
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = add(out[i + j], mul(x, y))
    return out


def characteristic(matrix):
    out = [ZERO] * 5
    for p in permutations(range(4)):
        term = [ONE]
        for i in range(4):
            term = poly_mul(term, [neg(matrix[i][p[i]]), ONE if p[i] == i else ZERO])
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        out = poly_add(out, [times((-1) ** inversions, z) for z in term])
    return out


def main():
    assert mul(S, (1, 1)) == ONE
    assert sm(PHI) == (-1, 1)
    assert sign(sub((2, 0), times(5, S))) > 0
    reports = []
    columns = steps = 0
    for lengths in ((2, 2, 2), (3, 2, 2)):
        c = Complex(lengths)
        for i in range(c.nv):
            f = [ZERO] * c.nv
            f[i] = ONE
            assert all(z == ZERO for z in apply(c.C, apply(c.G, f)))
        for selected in ((), (0,), tuple(range(c.ne))):
            law = Law(c, selected)
            for group, n in enumerate(law.sizes):
                for i in range(n):
                    for unit in (ONE, PHI):
                        state = law.zero()
                        state[group][i] = unit
                        out = law.step(state)
                        law.check(state, out)
                        columns += 1
            state = tuple([((i + 2 * g) % 5 - 2, (2 * i + g) % 3 - 1)
                           for i in range(n)] for g, n in enumerate(law.sizes))
            initial_energy = law.energy(state)
            for _ in range(16):
                out = law.step(state)
                law.check(state, out)
                state = out
                steps += 1
            assert law.energy(state) == initial_energy
            reports.append({'torus': lengths, 'edges': c.ne, 'material_sites': law.m,
                            'initial_doubled_energy': initial_energy})
        law = Law(c, (0,))
        source = law.zero()
        source[3][0] = ONE
        first = law.step(source)
        assert first[2] == [ONE]
        assert first[3] == [sub((2, 0), times(4, S))]
        assert first[0][0] == neg(S) and first[1][0] == neg(S)
        assert all(z == ZERO for z in law.defect(first))
        assert law.energy(source) == law.energy(first) == ONE
        wrong = law.step(source, feedback=False)
        assert sub(law.energy(wrong), ONE) == sub(ONE, times(2, S))
        assert sign(sub(law.energy(wrong), ONE)) > 0
        state = source
        seen_outside = False
        for tick in range(1, 17):
            out = law.step(state)
            law.check(state, out)
            if tick == 2:
                seen_outside = any(z != ZERO for z in out[0][1:])
            state = out
            steps += 1
        assert seen_outside
        scale = ONE
        for _ in range(13):
            scaled = tuple([mul(scale, z) for z in group] for group in source)
            assert law.energy(scaled) == mul(scale, scale)
            assert gcd(*(q for group in scaled for z in group for q in z)) == 1
            assert law.step(scaled) == tuple([mul(scale, z) for z in group] for group in first)
            assert sign(mul(scale, scale)) > 0
            scale = sm(scale)
    polynomials = {}
    for lam in (0, 2, 4, 6, 8):
        a = times(lam, S)
        matrix = [[sub(ONE, a), ONE, ZERO, neg(S)],
                  [neg(a), ONE, ZERO, neg(S)],
                  [ZERO, ZERO, ONE, ONE],
                  [neg(sm(a)), S, neg(S), sub(sub(ONE, S), mul(S, S))]]
        b = sub(times(lam + 4, S), (5, 0))
        d = add((8 - lam, 0), times(lam - 8, S))
        expected = [ONE, b, d, b, ONE]
        assert characteristic(matrix) == expected
        polynomials[str(lam)] = expected
    assert sub(mul(sub((4, 0), times(8, S)), sub((4, 0), S)), times(4, mul(S, S))) == times(12, sub(ONE, times(2, S)))
    assert mul(sub((3, 0), PHI), add(ONE, S)) == times(5, S)
    print(json.dumps({'status': 'PASS; NON-CANONICAL conditional bound-charge comparison',
                      'basis_columns': columns, 'closed_steps': steps,
                      'cases': reports, 'mode_polynomials_ascending': polynomials,
                      'unit_scalings_per_torus': 13,
                      'first_source_doubled_energy': ONE,
                      'missing_feedback_doubled_energy_error': sub(ONE, times(2, S)),
                      'off_source_field_at_step_two': True,
                      'no_particle_or_quantum_identification': True}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
