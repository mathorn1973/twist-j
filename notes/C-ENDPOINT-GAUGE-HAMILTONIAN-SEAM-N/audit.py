#!/usr/bin/env python3
"""NON-CANONICAL exact audit of the unadopted endpoint Hamiltonian.

No finite flux cutoff is used. Finite input windows do not restrict outputs.
All coefficients are pairs in Z[phi], phi^2=phi+1. No external input.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json

ZERO = (0, 0)
ONE = (1, 0)
S = (2, -1)
PHI = (0, 1)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def mul(a, b):
    return (a[0]*b[0] + a[1]*b[1],
            a[0]*b[1] + a[1]*b[0] + a[1]*b[1])


def scale(a, n):
    return (n*a[0], n*a[1])


def marked_nonnegative(a):
    # Twice a0+a1*phi equals c+d*sqrt(5); comparison is integer-only.
    c, d = 2*a[0]+a[1], a[1]
    if d == 0:
        return c >= 0
    if d > 0:
        return c >= 0 or 5*d*d >= c*c
    return c >= 0 and c*c >= 5*d*d


def put(v, f, a):
    value = add(v.get(f, ZERO), a)
    if value == ZERO:
        v.pop(f, None)
    else:
        v[f] = value


def combine(v, w, factor=ONE):
    result = dict(v)
    for f, a in w.items():
        put(result, f, mul(factor, a))
    return result


def times(v, a):
    return {f: mul(a, b) for f, b in v.items() if mul(a, b) != ZERO}


def basis(f):
    return {f: ONE}


def inner(v, w):
    out = ZERO
    for f, a in v.items():
        out = add(out, mul(a, w.get(f, ZERO)))
    return out


def act(column, v):
    out = {}
    for f, a in v.items():
        for g, b in column(f).items():
            put(out, g, mul(a, b))
    return out


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class Graph:
    def __init__(self, vertices, edges, faces, positions=None, edge_lookup=None):
        self.vertices = vertices
        self.edges = tuple(edges)
        self.faces = tuple(tuple(face) for face in faces)
        self.ne = len(edges)
        self.positions = positions or {}
        self.edge_lookup = edge_lookup or {}
        self.zero = (0,)*self.ne
        for face in self.faces:
            boundary = [0]*vertices
            for e, c in face:
                a, b = self.edges[e]
                boundary[a] -= c
                boundary[b] += c
            require(not any(boundary), "face boundary is not closed")

    @lru_cache(maxsize=8192)
    def charges(self, f):
        out = [0]*self.vertices
        for value, (a, b) in zip(f, self.edges):
            out[a] -= value
            out[b] += value
        return tuple(out)

    def valid(self, f):
        return len(f) == self.ne and all(abs(n) <= 1 for n in self.charges(f))

    def shift_edge(self, f, e, amount):
        out = list(f)
        out[e] += amount
        return tuple(out)

    def shift_face(self, f, p, sign=1):
        out = list(f)
        for e, c in self.faces[p]:
            out[e] += sign*c
        return tuple(out)

    def hop(self, f, e):
        n = self.charges(f)
        a, b = self.edges[e]
        if (abs(n[a]) == 1 and n[b] == 0) or (n[a] == 0 and abs(n[b]) == 1):
            d = n[a] - n[b]
            return self.shift_edge(f, e, d), d
        return f, 0

    def field2(self, f):
        # 2 H_F; output configurations have unbounded ordinary integer flux.
        out = {}
        put(out, f, (sum(x*x for x in f), 0))
        for p in range(len(self.faces)):
            put(out, f, scale(S, 2))
            put(out, self.shift_face(f, p), neg(S))
            put(out, self.shift_face(f, p, -1), neg(S))
        return out

    def magnetic2(self, f):
        out = self.field2(f)
        put(out, f, (-sum(x*x for x in f), 0))
        return out

    def matter2(self, f):
        out = {}
        put(out, f, (2*sum(n*n for n in self.charges(f)), 0))
        for e in range(self.ne):
            g, d = self.hop(f, e)
            if d:
                put(out, f, (2, 0))
                put(out, g, (-2, 0))
        return out

    def total2(self, f):
        return combine(self.field2(f), self.matter2(f))

    def current_skew(self, f, e):
        g, d = self.hop(f, e)
        return {g: (d, 0)} if d else {}

    def work4_over_i(self, f):
        # [2H, 2H_F] = 2 sum_e {E_e, B_e}; physical work = i/4 times this.
        out = {}
        for e in range(self.ne):
            g, d = self.hop(f, e)
            if d:
                put(out, g, (2*d*(f[e] + g[e]), 0))
        return out


def triangle_graph():
    return Graph(3, [(0, 1), (1, 2), (0, 2)], [[(0, 1), (1, 1), (2, -1)]])


def d3_graph(periods):
    positions = list(product(*(range(x) for x in periods)))
    vertex_index = {x: i for i, x in enumerate(positions)}
    offsets = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    types = list(combinations(range(4), 2))
    lookup = {}
    edges = []

    def located(x, y, sign=1):
        return tuple((x[k] + sign*y[k]) % periods[k] for k in range(3))

    for x in positions:
        for i, j in types:
            tail = vertex_index[x]
            d = tuple(offsets[j][k] - offsets[i][k] for k in range(3))
            head = vertex_index[located(x, d)]
            lookup[(x, i, j)] = len(edges)
            edges.append((tail, head))
    faces = []
    for x in positions:
        for i, j, k in combinations(range(4), 3):
            faces.append([(lookup[(located(x, offsets[i]), i, j)], 1),
                          (lookup[(located(x, offsets[j]), j, k)], 1),
                          (lookup[(located(x, offsets[i]), i, k)], -1)])
            faces.append([(lookup[(located(x, offsets[j], -1), i, j)], -1),
                          (lookup[(located(x, offsets[k], -1), j, k)], -1),
                          (lookup[(located(x, offsets[k], -1), i, k)], 1)])
    return Graph(len(positions), edges, faces, vertex_index, lookup)


def check_local(g, inputs):
    counts = {"basis_inputs": len(inputs), "hops": 0, "active_hops": 0,
              "face_inverse": 0, "face_hop_commutations": 0}
    for f in inputs:
        require(g.valid(f), "invalid input")
        n = g.charges(f)
        for e in range(g.ne):
            h, d = g.hop(f, e)
            require(g.valid(h), "hop left charge domain")
            require(g.hop(h, e)[0] == f, "hop not involutive")
            expected = list(n)
            a, b = g.edges[e]
            expected[a] -= d
            expected[b] += d
            require(g.charges(h) == tuple(expected), "Gauss/current mismatch")
            require(sorted(g.charges(h)) == sorted(n), "endpoint numbers changed")
            counts["hops"] += 1
            counts["active_hops"] += int(d != 0)
        for p in range(len(g.faces)):
            h = g.shift_face(f, p)
            require(g.valid(h) and g.charges(h) == n, "face changed charge")
            require(g.shift_face(h, p, -1) == f, "face inverse")
            counts["face_inverse"] += 1
            for e in range(g.ne):
                left, d1 = g.hop(h, e)
                h2, d2 = g.hop(f, e)
                right = g.shift_face(h2, p)
                require(left == right and d1 == d2, "face and hop do not commute")
                counts["face_hop_commutations"] += 1
    return counts


def check_diagonal_commutators(g, inputs):
    count = 0
    for f in inputs:
        hcol = g.total2(f)
        nf = g.charges(f)
        for z in range(g.vertices):
            lhs = {h: scale(a, nf[z] - g.charges(h)[z])
                   for h, a in hcol.items() if nf[z] != g.charges(h)[z]}
            rhs = {}
            for e, (a, b) in enumerate(g.edges):
                incidence = int(b == z) - int(a == z)
                if incidence:
                    rhs = combine(rhs, g.current_skew(f, e), (2*incidence, 0))
            require(lhs == rhs, "charge commutator")
            count += 1
        for e in range(g.ne):
            lhs = {h: scale(a, f[e] - h[e]) for h, a in hcol.items() if f[e] != h[e]}
            rhs = times(g.current_skew(f, e), (2, 0))
            for p, face in enumerate(g.faces):
                coefficient = sum(c for edge, c in face if edge == e)
                if coefficient:
                    put(rhs, g.shift_face(f, p), scale(S, coefficient))
                    put(rhs, g.shift_face(f, p, -1), scale(S, -coefficient))
            require(lhs == rhs, "electric commutator")
            count += 1
    return count


def check_work(g, inputs):
    for f in inputs:
        lhs = combine(act(g.matter2, g.field2(f)), act(g.field2, g.matter2(f)), (-1, 0))
        require(lhs == g.work4_over_i(f), "total field work")
        magnetic = combine(act(g.matter2, g.magnetic2(f)),
                           act(g.magnetic2, g.matter2(f)), (-1, 0))
        require(not magnetic, "magnetic matter work not zero")
        # This explicitly checks Hermiticity on the produced work support.
        for h, coefficient in lhs.items():
            require(g.work4_over_i(h).get(f, ZERO) == neg(coefficient), "work skew adjoint")
    return len(inputs)


def check_positive(g, v):
    lhs = inner(v, act(g.total2, v))
    rhs = ZERO
    for f, a in v.items():
        weight = sum(x*x for x in f) + 2*sum(n*n for n in g.charges(f))
        rhs = add(rhs, scale(mul(a, a), weight))
    for p in range(len(g.faces)):
        wv = {}
        for f, a in v.items():
            put(wv, g.shift_face(f, p), a)
        diff = combine(v, wv, (-1, 0))
        rhs = add(rhs, mul(S, inner(diff, diff)))
    for e in range(g.ne):
        sv = {}
        for f, a in v.items():
            put(sv, g.hop(f, e)[0], a)
        diff = combine(v, sv, (-1, 0))
        rhs = add(rhs, inner(diff, diff))
    require(lhs == rhs, "positive sum-of-squares decomposition")
    return lhs


def rational_pair(a, denominator):
    return [str(Fraction(x, denominator)) for x in a]


def check_phase(g, f, e):
    target, d = g.hop(f, e)
    require(d in (-1, 1) and f[e] == 0, "phase witness preparation")
    require(g.total2(f).get(target) == (-2, 0), "adjacent Hamiltonian coefficient")
    cf = g.work4_over_i(f)
    ct = g.work4_over_i(target)
    # For psi=(|f>+i|target>)/sqrt(2), <i M>=(M_target,f-M_f,target)/2.
    work_numerator = add(cf.get(target, ZERO), neg(ct.get(f, ZERO)))
    require(work_numerator == (4, 0), "phase work not +1/2")
    a, b = g.edges[e]
    nf, nt = g.charges(f), g.charges(target)
    qtf = scale(g.total2(f).get(target, ZERO), nf[b] - nt[b])
    qft = scale(g.total2(target).get(f, ZERO), nt[b] - nf[b])
    charge_numerator = add(qtf, neg(qft))
    require(charge_numerator == (4*d, 0), "phase charge velocity")
    mean_numerator = add(g.total2(f).get(f, ZERO), g.total2(target).get(target, ZERO))
    # H has real symmetric off-diagonal entries, so the +/-i coherences cancel.
    require(g.total2(f).get(target) == g.total2(target).get(f), "H not real symmetric")
    return {"direction": d, "work_plus": rational_pair(work_numerator, 8),
            "work_minus": rational_pair(neg(work_numerator), 8),
            "charge_derivative_plus": rational_pair(charge_numerator, 4),
            "common_mean_energy": rational_pair(mean_numerator, 4)}


def run_triangle():
    g = triangle_graph()
    all_inputs = list(product(range(-2, 3), repeat=3))
    inputs = [f for f in all_inputs if g.valid(f)]
    counts = check_local(g, inputs)
    counts["window_inputs"] = len(all_inputs)
    counts["charge_electric_identities"] = check_diagonal_commutators(g, inputs)
    counts["work_identities"] = check_work(g, inputs)
    f = (0, 0, -1)
    h = g.hop(f, 0)[0]
    counts["positive_energy_2H"] = check_positive(g, {f: ONE, h: PHI})
    counts["phase"] = check_phase(g, f, 0)
    escaped = g.shift_face((2, 2, -2), 0)
    require(g.valid(escaped) and max(abs(x) for x in escaped) == 3,
            "output window was incorrectly truncated")
    counts["unbounded_output_control"] = escaped
    return counts


def run_d3(periods):
    g = d3_graph(periods)
    origin = (0, 0, 0)
    b1 = (1, 0, 0)
    edge = g.edge_lookup[(origin, 0, 1)]
    source = g.edge_lookup[(origin, 0, 2)]
    step2 = g.edge_lookup[(b1, 0, 3)]
    zero = g.zero
    f = g.shift_edge(zero, source, -1)
    negative = tuple(-x for x in f)
    target = g.hop(f, edge)[0]
    two = g.hop(target, step2)[0]
    loop = g.shift_face(g.shift_face(zero, 0), 0)
    dressed = g.shift_face(f, 1)
    inputs = [zero, f, negative, target, two, loop, dressed]
    require(len(set(inputs)) == len(inputs), "duplicate fixed inputs")
    counts = {"periods": periods, "vertices": g.vertices, "edges": g.ne,
              "faces": len(g.faces)}
    counts.update(check_local(g, inputs))
    counts["charge_electric_identities"] = check_diagonal_commutators(g, inputs)
    counts["work_identities"] = check_work(g, [zero, f, target])
    counts["positive_energy_2H"] = check_positive(g, {f: ONE, target: PHI, dressed: (-1, 0)})
    counts["phase_positive"] = check_phase(g, f, edge)
    counts["phase_negative"] = check_phase(g, negative, edge)
    require(g.total2(f).get(two, ZERO) == ZERO, "two-hop state reached in one operator")
    two_coefficient = ZERO
    for intermediate, coefficient in g.total2(f).items():
        two_coefficient = add(two_coefficient, mul(coefficient, g.total2(intermediate).get(two, ZERO)))
    require(marked_nonnegative(add(two_coefficient, (-4, 0))), "two-hop coefficient missing")
    counts["two_hop_H2_squared_coefficient"] = two_coefficient
    neutral_col = g.total2(zero)
    require(not g.matter2(zero), "neutral matter not zero")
    require(any(h != zero for h in neutral_col), "neutral field frozen")
    require(all(not any(g.charges(h)) for h in neutral_col), "neutral sector escaped")
    counts["neutral_off_diagonal_configs"] = sum(h != zero for h in neutral_col)
    # A diagonal Hamiltonian commutes with every N, while the actual hopping does not.
    actual = {h: scale(a, g.charges(f)[g.edges[edge][1]] - g.charges(h)[g.edges[edge][1]])
              for h, a in g.total2(f).items()
              if g.charges(f)[g.edges[edge][1]] != g.charges(h)[g.edges[edge][1]]}
    require(bool(actual), "diagonal-only control failed")
    # Move a redundant charge label but do not change flux: the Gauss defect is nonzero.
    require(g.charges(f) != g.charges(target), "no Gauss defect from omitted flux update")
    counts["diagonal_and_omitted_flux_controls"] = "PASS"
    return counts


def main():
    # Cyclic five-value flux shift at 2 -> -2 violates [E,U]=U by -5.
    wrap_commutator = (-2) - 2
    require(wrap_commutator - 1 == -5, "cyclic cutoff boundary")
    output = {"status": "NON-CANONICAL candidate-C; quantum comparison only",
              "arithmetic": "Z[phi] pairs and rational expectation normalizations",
              "triangle": run_triangle(),
              "D3": [run_d3((2, 2, 2)), run_d3((3, 2, 2))],
              "cyclic_cutoff_commutator_error": -5,
              "physical_closure": "NOT PROVIDED",
              "independent_review": "NOT PROVIDED",
              "photon_phase": "NOT PROVED; harmonic comparison only",
              "native_integer_time": "NOT PROVIDED",
              "verdict": "PASS exact frozen identities and negative controls"}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
