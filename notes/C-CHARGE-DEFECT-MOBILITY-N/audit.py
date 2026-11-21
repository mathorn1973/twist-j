#!/usr/bin/env python3
"""Frozen exact finite audit; NON-CANONICAL. No external inputs or floats."""
from fractions import Fraction
from itertools import combinations, product
import json

Z = (0, 0)
ONE = (1, 0)
PHI = (0, 1)
S = (2, -1)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a, b = x
    c, d = y
    return a*c + b*d, a*d + b*c + b*d


def scale(k, x):
    return k*x[0], k*x[1]


def total(xs):
    ans = Z
    for x in xs:
        ans = add(ans, x)
    return ans


def dot(x, y):
    return total(mul(a, b) for a, b in zip(x, y))


def va(x, y):
    return [add(a, b) for a, b in zip(x, y)]


def vs(x, y):
    return [sub(a, b) for a, b in zip(x, y)]


def vm(a, x):
    return [mul(a, v) for v in x]


class Complex:
    def __init__(self, shape):
        assert len(shape) == 3 and all(n >= 2 and n % 2 == 0 for n in shape)
        self.shape = shape
        self.nodes = list(product(*(range(n) for n in shape)))
        self.idx = {x: i for i, x in enumerate(self.nodes)}
        self.b = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self.types = list(combinations(range(4), 2))
        self.edges = []
        self.lookup = {}
        self.matchings = [[] for _ in range(12)]
        for x in self.nodes:
            for t, (i, j) in enumerate(self.types):
                d = tuple(self.b[j][k] - self.b[i][k] for k in range(3))
                y = self.shift(x, d)
                e = len(self.edges)
                self.edges.append((self.idx[x], self.idx[y]))
                self.lookup[x, i, j] = e
                axis = next(k for k in range(3) if d[k])
                self.matchings[2*t + x[axis] % 2].append(e)
        self.N = len(self.edges)
        self.faces = []
        for x in self.nodes:
            for i, j, k in combinations(range(4), 3):
                self.faces.append([(self.lookup[self.shift(x, self.b[i]), i, j], 1),
                                   (self.lookup[self.shift(x, self.b[j]), j, k], 1),
                                   (self.lookup[self.shift(x, self.b[i]), i, k], -1)])
                minus_j = self.shift(x, tuple(-a for a in self.b[j]))
                minus_k = self.shift(x, tuple(-a for a in self.b[k]))
                self.faces.append([(self.lookup[minus_j, i, j], -1),
                                   (self.lookup[minus_k, j, k], -1),
                                   (self.lookup[minus_k, i, k], 1)])
        for es in self.matchings:
            endpoints = [x for e in es for x in self.edges[e]]
            assert len(endpoints) == len(set(endpoints))
        assert sorted(e for es in self.matchings for e in es) == list(range(self.N))

    def shift(self, x, d):
        return tuple((x[k]+d[k]) % self.shape[k] for k in range(3))

    def gradient(self, f):
        return [sub(f[v], f[u]) for u, v in self.edges]

    def div(self, e):
        out = [Z] * len(self.nodes)
        for value, (u, v) in zip(e, self.edges):
            out[u] = sub(out[u], value)
            out[v] = add(out[v], value)
        return out

    def curl(self, e):
        return [total(scale(sign, e[index]) for index, sign in row) for row in self.faces]

    def adjcurl(self, f):
        out = [Z] * self.N
        for value, row in zip(f, self.faces):
            for e, sign in row:
                out[e] = add(out[e], scale(sign, value))
        return out

    def P(self, e):
        return self.adjcurl(self.curl(e))

    def energy(self, A, E):
        return add(dot(E, E), mul(S, dot(A, self.P(vs(A, E)))))

    def free(self, A, E):
        En = vs(E, vm(S, self.P(A)))
        return va(A, En), En

    def free_inv(self, A, E):
        oldA = vs(A, E)
        return oldA, va(E, vm(S, self.P(oldA)))

    def hop(self, A, E, edge):
        q = self.div(E)
        u, v = self.edges[edge]
        delta = sub(q[u], q[v])
        g = add(sub(scale(2, E[edge]), mul(S, self.P(A)[edge])), delta)
        out = E.copy()
        if g == Z:
            out[edge] = add(out[edge], delta)
            return out, delta
        return out, Z

    def matching(self, A, E, phase):
        q, PA = self.div(E), self.P(A)
        out, current, count = E.copy(), [Z]*self.N, 0
        for e in self.matchings[phase]:
            u, v = self.edges[e]
            delta = sub(q[u], q[v])
            if add(sub(scale(2, E[e]), mul(S, PA[e])), delta) == Z:
                # Independent reflection form, instead of E + delta.
                out[e] = sub(mul(S, PA[e]), E[e])
                current[e] = neg(delta)
                count += delta != Z
        return out, current, count

    def step(self, state):
        A, E, phase = state
        En, j, count = self.matching(A, E, phase)
        An, En = self.free(A, En)
        return (An, En, (phase+1) % 12), j, count

    def inverse(self, state):
        A, E, phase = state
        phase = (phase-1) % 12
        A, E = self.free_inv(A, E)
        E, _, _ = self.matching(A, E, phase)
        return A, E, phase

    def old_step(self, state):
        A, E, x, v = state
        xn = va(x, v)
        En = vs(vs(E, vm(S, self.P(A))), vm(S, v))
        An = va(A, En)
        vn = va(vs(v, vm(S, xn)), vm(S, En))
        return An, En, xn, vn

    def old_charge(self, state):
        _, E, x, _ = state
        rho = vm(neg(S), self.div(x))
        Q = self.div(va(E, vm(S, x)))
        return rho, Q

    def square(self):
        A, E = [Z]*self.N, [Z]*self.N
        o, a, b = (0, 0, 0), self.b[1], self.b[2]
        for key in [(o, 0, 1), (a, 0, 2), (o, 0, 2), (b, 0, 1)]:
            E[self.lookup[key]] = (-1, 0)
        return A, E, 0

    def charge_record(self, E):
        return [[list(x), list(q)] for x, q in zip(self.nodes, self.div(E)) if q != Z]


def poisson(c):
    nv = len(c.nodes)
    mat = [[Fraction(0) for _ in range(nv)] for _ in range(nv)]
    for u, v in c.edges:
        mat[u][u] += 1
        mat[v][v] += 1
        mat[u][v] -= 1
        mat[v][u] -= 1
    rho = [Fraction(0)]*nv
    rho[0] = 1
    rho[c.idx[c.b[1]]] = -1
    aug = [mat[i][:-1] + [rho[i]] for i in range(nv-1)]
    for col in range(nv-1):
        pivot = next(row for row in range(col, nv-1) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divisor = aug[col][col]
        aug[col] = [x/divisor for x in aug[col]]
        for row in range(nv-1):
            if row != col:
                factor = aug[row][col]
                aug[row] = [x-factor*y for x, y in zip(aug[row], aug[col])]
    f = [aug[i][-1] for i in range(nv-1)] + [Fraction(0)]
    E = [f[v]-f[u] for u, v in c.edges]
    got = [Fraction(0)]*nv
    for val, (u, v) in zip(E, c.edges):
        got[u] -= val
        got[v] += val
    assert got == rho
    F = sum(x*x for x in E)
    if c.shape == (2, 2, 2):
        assert F == Fraction(7, 48)
        assert any(x.denominator != 1 for x in E)
        counts = {}
        for t in product(range(2), repeat=3):
            fchar = [Fraction((-1)**sum(a*b for a, b in zip(t, x))) for x in c.nodes]
            ev = sum(mat[0][j]*fchar[j] for j in range(nv))
            assert all(sum(mat[i][j]*fchar[j] for j in range(nv)) == ev*fchar[i]
                       for i in range(nv))
            counts[str(ev)] = counts.get(str(ev), 0) + 1
        assert counts == {'0': 1, '12': 4, '16': 3}
    return str(F)


def audit(shape):
    c = Complex(shape)
    for j in range(len(c.nodes)):
        f = [Z]*len(c.nodes)
        f[j] = ONE
        assert all(x == Z for x in c.curl(c.gradient(f)))
    old_columns = 0
    coef = sub((3, 0), scale(4, S))
    s2 = mul(S, S)
    for component in range(4):
        for e in range(c.N):
            for a in (ONE, PHI):
                state = [[Z]*c.N for _ in range(4)]
                state[component][e] = a
                r0, Q = c.old_charge(state)
                x1 = c.old_step(state)
                r1, Q1 = c.old_charge(x1)
                r2, Q2 = c.old_charge(c.old_step(x1))
                assert Q1 == Q2 == Q
                assert r2 == vs(vs(vm(coef, r1), r0), vm(s2, Q))
                old_columns += 1
    local = 0
    for seed in range(4):
        A = [((i+seed) % 3-1, (2*i+seed) % 3-1) for i in range(c.N)]
        E = [((2*i+seed+1) % 3-1, (i+2*seed) % 3-1) for i in range(c.N)]
        before = c.energy(A, E)
        assert c.free_inv(*c.free(A, E)) == (A, E)
        for e in range(c.N):
            En, d = c.hop(A, E, e)
            back, _ = c.hop(A, En, e)
            assert back == E and c.energy(A, En) == before
            q, qn = c.div(E), c.div(En)
            assert sorted(q) == sorted(qn)
            assert vs(qn, q) == c.div([d if i == e else Z for i in range(c.N)])
            # The unconditional swap has exactly the predicted energy cost.
            u, v = c.edges[e]
            delta = sub(q[u], q[v])
            trial = E.copy()
            trial[e] = add(trial[e], delta)
            bracket = add(sub(scale(2, E[e]), mul(S, c.P(A)[e])), delta)
            assert sub(c.energy(A, trial), before) == mul(delta, bracket)
            local += 1
        for phase in range(12):
            together, _, _ = c.matching(A, E, phase)
            sequential = E.copy()
            for e in reversed(c.matchings[phase]):
                sequential, _ = c.hop(A, sequential, e)
            assert together == sequential
    seed_state = c.square()
    first, _, first_hops = c.step(seed_state)
    a, b = c.idx[c.b[1]], c.idx[c.b[2]]
    target = [Z]*len(c.nodes)
    target[a], target[b] = (2, 0), (-2, 0)
    assert c.div(first[1]) == target and first_hops == 2
    assert c.energy(*first[:2]) == (4, 0)
    state = seed_state
    trace = []
    for n in range(24):
        nxt, j, hops = c.step(state)
        assert c.inverse(nxt) == state
        assert c.energy(*nxt[:2]) == (4, 0)
        assert sorted(c.div(nxt[1])) == sorted(c.div(state[1]))
        assert vs(c.div(nxt[1]), c.div(state[1])) == vm((-1, 0), c.div(j))
        trace.append({'step': n+1, 'hops': hops, 'charge': c.charge_record(nxt[1])})
        state = nxt
    # Neutral field: no defect gate may modify the free wave.
    face = [Z]*len(c.faces)
    face[0] = ONE
    state = ([Z]*c.N, c.adjcurl(face), 0)
    assert c.div(state[1]) == [Z]*len(c.nodes)
    for _ in range(12):
        free = c.free(*state[:2])
        nxt, j, count = c.step(state)
        assert nxt[:2] == free and count == 0 and all(x == Z for x in j)
        state = nxt
    # Every member of the exact countersequence disables the positive-source hop.
    amplitude = ONE
    e0 = c.lookup[(0, 0, 0), 0, 1]
    for m in range(1, 9):
        amplitude = mul(S, amplitude)
        A, E, phase = c.square()
        A[e0] = amplitude
        pert, _, _ = c.step((A, E, phase))
        assert c.div(pert[1])[0] == (2, 0)
        assert c.energy(*pert[:2]) == c.energy(A, E)
        As, Es, phase = c.square()
        As, Es = vm(amplitude, As), vm(amplitude, Es)
        scaled, _, _ = c.step((As, Es, phase))
        assert scaled[:2] == (vm(amplitude, first[0]), vm(amplitude, first[1]))
        assert c.energy(*scaled[:2]) == scale(4, mul(amplitude, amplitude))
    return {'shape': shape, 'vertices_edges_faces': [len(c.nodes), c.N, len(c.faces)],
            'old_charge_basis_columns': old_columns, 'local_gate_cases': local,
            'first_hops': first_hops, 'first_charge': c.charge_record(first[1]),
            'fixed_charge_real_minimum_F': poisson(c),
            'neutral_steps': 12, 'perturbation_and_unit_cases': 8, 'trajectory': trace}


def main():
    results = [audit(shape) for shape in ((2, 2, 2), (4, 2, 2))]
    print(json.dumps({'status': 'PASS; NON-CANONICAL exact finite audit; no physical carrier',
                      'results': results}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
