#!/usr/bin/env python3
"""Primary exact polynomial audit. No scientific imports from other probes."""

from fractions import Fraction as F
import hashlib
import math
from pathlib import Path
import subprocess
import sys


NAME = "P-INTEGER-LOCAL-AUXILIARY-NOETHER-1"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
Z = F(0)
O = F(1)
G = F(1, 324)
ELL = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), Z, Z, Z)
EDGES = tuple((r, (r + 1) % 5, F(29, 324)) for r in range(5)) + tuple(
    (r, (r + 2) % 5, F(65, 324)) for r in range(5))
AUTHORITY = (
    ("CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    pass


def need(condition, name):
    if not condition:
        raise ScientificFailure(name)


def authority():
    for name, size, digest in AUTHORITY:
        try:
            data = (ROOT / "canon" / name).read_bytes()
        except OSError:
            raise ScientificFailure("F_AUTHORITY") from None
        need(len(data) == size and hashlib.sha256(data).hexdigest() == digest,
             "F_AUTHORITY")


def zeros(rows, columns):
    return [[Z] * columns for _ in range(rows)]


def dot(a, b):
    return sum((v * w for v, w in zip(a, b) if v and w), Z)


def add(a, b, factor=O):
    return [v + factor * w for v, w in zip(a, b)]


def array_add(a, b, factor=O):
    return [add(v, w, factor) for v, w in zip(a, b)]


def array_scale(a, factor):
    return [[factor * value for value in row] for row in a]


def flatten(a):
    return [value for row in a for value in row]


def encode(values):
    return ",".join(str(value) for value in values)


def is_zero(a):
    return all(value == 0 for value in flatten(a))


def mean(a):
    return sum(a, Z) / len(a)


def project(a):
    average = mean(a)
    return [value - average for value in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mv(a, v):
    return [dot(row, v) for row in a]


def mm(a, b):
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    rows = [row[:] + unit for row, unit in zip(a, eye(n))]
    for col in range(n):
        pivot = next((r for r in range(col, n) if rows[r][col]), None)
        need(pivot is not None, "F_CARRIER")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [value / divisor for value in rows[col]]
        for r in range(n):
            if r != col and rows[r][col]:
                factor = rows[r][col]
                rows[r] = add(rows[r], rows[col], -factor)
    return [row[n:] for row in rows]


class Geometry:
    def __init__(self):
        self.B = zeros(10, 5)
        for edge, (tail, head, _) in enumerate(EDGES):
            self.B[edge][head] = O
            self.B[edge][tail] = -O
        self.BT = transpose(self.B)
        self.WB = [[weight * value for value in row]
                   for row, (_, _, weight) in zip(self.B, EDGES)]
        self.L = mm(self.BT, self.WB)
        averaging = [[F(1, 5)] * 5 for _ in range(5)]
        self.Pi = array_add(eye(5), averaging, -O)
        self.Lplus = array_add(inverse(array_add(self.L, averaging)), averaging, -O)
        self.P = array_add(eye(10), mm(mm(self.WB, self.Lplus), self.BT), -O)
        self.PT = transpose(self.P)
        self.Pcyc = array_add(eye(10), array_scale(mm(self.B, self.BT), F(1, 5)), -O)
        self.V = zeros(6, 6)
        for r in range(5):
            self.V[r][:5] = self.L[r][:]
            self.V[r][5] = -G * ELL[r]
            self.V[5][r] = -G * ELL[r]
        self.V[5][5] = O
        self.C = array_add(eye(6), array_scale(self.V, F(1, 2)), -O)

    def check(self):
        need(mm(self.L, self.Lplus) == self.Pi
             and mm(self.Lplus, self.L) == self.Pi
             and mv(self.Lplus, [O] * 5) == [Z] * 5
             and self.Lplus == transpose(self.Lplus), "F_CARRIER")
        need(mm(self.BT, self.B) == array_scale(self.Pi, F(5)), "F_CARRIER")
        need(mm(self.P, self.P) == self.P and is_zero(mm(self.BT, self.P))
             and mm(self.Pcyc, self.Pcyc) == self.Pcyc
             and is_zero(mm(self.BT, self.Pcyc)), "F_CARRIER")
        for r in range(5):
            expected = [F(188 if s == r else -29 if (s - r) % 5 in (1, 4)
                          else -65, 324) for s in range(5)]
            need(self.L[r] == expected, "F_CARRIER")


def empty_multiplier(T):
    return ([Z] * (T + 1), zeros(T + 1, 5), zeros(T + 1, 10))


def multiplier_add(a, b, factor=O):
    return (add(a[0], b[0], factor), array_add(a[1], b[1], factor),
            array_add(a[2], b[2], factor))


def z(q, n, r):
    return F(((q + 2) * (n + 1) * (r + 3) + (n - r) ** 2) % 17 - 8, q + 2)


def fixture(geometry, T, q):
    x = [[z(q, n, r) for r in range(6)] for n in range(T + 1)]
    alpha, lam, shift = empty_multiplier(T)
    tau, p = zeros(T + 1, 5), zeros(T + 1, 10)
    for b in range(1, T + 1):
        alpha[b] = z(q, b, 6)
        lam[b] = project([z(q, b, 7 + r) for r in range(5)])
        tau[b] = project([z(q + 1, b, 12 + r) for r in range(5)])
    for n in range(1, T):
        shift[n] = [z(q, n, 17 + edge) for edge in range(10)]
        p[n] = mv(geometry.Pcyc, [z(q + 1, n, 27 + edge) for edge in range(10)])
    return x, (alpha, lam, shift), tau, p


def parameter_list(T, q):
    for n in range(1, T):
        for r in range(5):
            psi = zeros(T + 1, 5)
            psi[n][r] = O
            yield psi
    yield [[Z] * 5] + [[z(q + 2, n, 37 + r) for r in range(5)]
                       for n in range(1, T)] + [[Z] * 5]


def generator(x, psi):
    T = len(x) - 1
    result = zeros(T + 1, 6)
    for n in range(1, T):
        q = add(x[n + 1], x[n - 1], -O)
        result[n][:5] = [psi[n][r] * q[r] / 2 for r in range(5)]
        result[n][5] = dot(SIGMA, psi[n]) * q[5] / 2
    return result


class AuditState:
    """All derivative calls below use exact finite polynomial identities."""

    def __init__(self, geometry, x):
        self.geo = geometry
        self.x = x
        self.T = len(x) - 1
        self.cx = [mv(geometry.C, row) for row in x]
        self.f = zeros(self.T + 1, 6)
        for n in range(1, self.T):
            self.f[n] = add(add([2 * value for value in self.cx[n]], x[n - 1], -O),
                            x[n + 1], -O)
        self.k = [Z] + [dot(add(self.cx[b], x[b - 1], -O),
                            add(x[b], self.cx[b - 1], -O))
                         for b in range(1, self.T + 1)]
        self.aux_cache = {}

    def action(self, x):
        kinetic = sum((dot(add(x[b], x[b - 1], -O), add(x[b], x[b - 1], -O))
                       for b in range(1, self.T + 1)), Z) / 2
        potential = sum((dot(x[n], mv(self.geo.V, x[n]))
                         for n in range(1, self.T)), Z) / 2
        return kinetic - potential

    def da(self, direction):
        value = (self.action(array_add(self.x, direction))
                 - self.action(array_add(self.x, direction, -O))) / 2
        need(value == dot(flatten(self.f), flatten(direction)), "F_CARRIER")
        return value

    def density(self, x, b):
        now, old = x[b], x[b - 1]
        result = [(now[r] - old[r]) ** 2 / 2 for r in range(5)]
        for tail, head, weight in EDGES:
            term = weight * (now[head] - now[tail]) * (old[head] - old[tail]) / 4
            result[tail] += term
            result[head] += term
        chi_part = ((now[5] - old[5]) ** 2 + now[5] * old[5]) / 2
        for r in range(5):
            result[r] += SIGMA[r] * chi_part
            result[r] -= G * ELL[r] * (old[5] * now[r] + now[5] * old[r]) / 2
        return result

    def current(self, x, n):
        q = add(x[n + 1], x[n - 1], -O)
        result = [weight * (x[n][head] - x[n][tail]) * (q[tail] + q[head]) / 4
                  for tail, head, weight in EDGES]
        result[0] -= G * q[5] * (x[n][0] + x[n][1]) / 4
        return result

    def interaction(self, x, multiplier):
        alpha, lam, shift = multiplier
        total = Z
        for b in range(1, self.T + 1):
            if alpha[b] or any(lam[b]):
                density = self.density(x, b)
                total -= alpha[b] * sum(density, Z) + dot(lam[b], density)
        for n in range(1, self.T):
            if any(shift[n]):
                total += dot(shift[n], self.current(x, n))
        return total

    def di(self, multiplier, direction):
        return (self.interaction(array_add(self.x, direction), multiplier)
                - self.interaction(array_add(self.x, direction, -O), multiplier)) / 2

    def baux(self, multiplier, tau, p):
        _, lam, shift = multiplier
        value = 2 * sum((dot(lam[b], mv(self.geo.L, tau[b]))
                         for b in range(1, self.T + 1)), Z)
        value += 2 * sum((dot(shift[n], add(mv(self.geo.WB, add(tau[n + 1], tau[n], -O)),
                                            p[n])) for n in range(1, self.T)), Z)
        return value

    def gamma(self, psi):
        alpha, lam, shift = empty_multiplier(self.T)
        for b in range(1, self.T + 1):
            difference = add(psi[b], psi[b - 1], -O)
            alpha[b] = mean(difference)
            lam[b] = project(difference)
        for n in range(1, self.T):
            shift[n] = mv(self.geo.B, psi[n])
        return alpha, lam, shift

    def decompose(self, multiplier):
        alpha, lam, shift = multiplier
        vertex = zeros(self.T + 1, 5)
        residual = zeros(self.T + 1, 10)
        for n in range(1, self.T):
            weighted = [EDGES[e][2] * shift[n][e] for e in range(10)]
            vertex[n] = mv(self.geo.Lplus, mv(self.geo.BT, weighted))
            residual[n] = add(shift[n], mv(self.geo.B, vertex[n]), -O)
        local = zeros(self.T + 1, 5)
        for b in range(1, self.T + 1):
            local[b] = add(add(lam[b], vertex[b], -O), vertex[b - 1])
        return vertex, (alpha[:], local, residual)

    def hom_action(self, multiplier):
        return sum((multiplier[0][b] ** 2 * self.k[b]
                    for b in range(1, self.T + 1)), Z) / 2

    def second_action(self, multiplier):
        vertex, residual = self.decompose(multiplier)
        w = generator(self.x, vertex)
        # A is homogeneous quadratic, so Hess_A(w,w)/2=A(w).
        return -self.di(residual, w) + self.action(w) + self.hom_action(multiplier)

    def hom_direction(self, multiplier, t):
        alpha = multiplier[0]
        result = zeros(self.T + 1, 6)
        for n in range(1, self.T):
            right = add(self.x[n], self.cx[n + 1], -O)
            left = add(self.x[n], self.cx[n - 1], -O)
            result[n] = [t[n] * (alpha[n + 1] * right[r] - alpha[n] * left[r]) / 2
                         for r in range(6)]
        return result

    def parameter_data(self, psi):
        key = tuple(flatten(psi))
        if key not in self.aux_cache:
            t = [mean(row) for row in psi]
            uniform = [[value] * 5 for value in t]
            u = generator(self.x, uniform)
            xp, xm = array_add(self.x, u), array_add(self.x, u, -O)
            ftau, jp = zeros(self.T + 1, 5), zeros(self.T + 1, 10)
            for b in range(1, self.T + 1):
                derivative = [(a - bval) / 2 for a, bval in
                              zip(self.density(xp, b), self.density(xm, b))]
                ftau[b] = [value / 2 for value in mv(self.geo.Lplus, project(derivative))]
            for n in range(1, self.T):
                derivative = [(a - bval) / 2 for a, bval in
                              zip(self.current(xp, n), self.current(xm, n))]
                jp[n] = [-value / 2 for value in mv(self.geo.P, derivative)]
            self.aux_cache[key] = (t, uniform, u, ftau, jp)
        return self.aux_cache[key]

    def second_direction(self, multiplier, psi):
        t, uniform, _, ftau, jp = self.parameter_data(psi)
        vertex, _ = self.decompose(multiplier)
        raw = array_add(generator(generator(self.x, psi), vertex),
                        generator(generator(self.x, vertex), uniform), -O)
        raw = array_add(raw, self.hom_direction(multiplier, t))
        alpha = multiplier[0]
        skew = zeros(self.T + 1, 6)
        for n in range(1, self.T):
            skew[n] = [(alpha[n + 1] * (t[n] + t[n + 1]) * self.f[n + 1][r]
                        - alpha[n] * (t[n - 1] + t[n]) * self.f[n - 1][r]) / 8
                       for r in range(6)]
        return raw, skew, ftau, jp

    def carrier_check(self, multiplier, tau, p):
        self.geo.check()
        _, lam, _ = multiplier
        need(all(sum(lam[b], Z) == sum(tau[b], Z) == 0 for b in range(1, self.T + 1))
             and all(mv(self.geo.BT, p[n]) == [Z] * 5 for n in range(1, self.T)),
             "F_CARRIER")
        vertex, reduced = self.decompose(multiplier)
        _, local, weighted_cycle = reduced
        need(is_zero([vertex[0], vertex[-1]])
             and all(sum(row, Z) == 0 for row in vertex)
             and all(sum(row, Z) == 0 for row in local), "F_CARRIER")
        for n in range(1, self.T):
            weighted = [EDGES[e][2] * weighted_cycle[n][e] for e in range(10)]
            need(mv(self.geo.BT, weighted) == [Z] * 5
                 and mv(self.geo.PT, weighted_cycle[n]) == weighted_cycle[n], "F_CARRIER")
        decomposed = 2 * sum((dot(local[b], mv(self.geo.L, tau[b]))
                              for b in range(1, self.T + 1)), Z)
        decomposed += 2 * sum((dot(weighted_cycle[n], p[n])
                               for n in range(1, self.T)), Z)
        need(decomposed == self.baux(multiplier, tau, p), "F_CARRIER")
        for b in range(1, self.T + 1):
            expected = (dot(self.x[b], self.x[b]) + dot(self.x[b - 1], self.x[b - 1])) / 2
            expected -= dot(self.x[b - 1], self.cx[b])
            need(sum(self.density(self.x, b), Z) == expected, "F_CARRIER")

    def tangent_check(self, multiplier, psi, directions):
        raw, skew, ftau, jp = directions
        need(is_zero([raw[0], raw[-1], skew[0], skew[-1]])
             and all(sum(ftau[b], Z) == 0 for b in range(1, self.T + 1))
             and all(mv(self.geo.BT, jp[n]) == [Z] * 5 for n in range(1, self.T)),
             "F_CARRIER")
        gam = self.gamma(psi)
        need(all(sum(row, Z) == 0 for row in gam[1]), "F_CARRIER")
        old_z, old_m = self.decompose(multiplier)
        new_z, new_m = self.decompose(multiplier_add(multiplier, gam))
        need(array_add(new_z, old_z, -O) == [project(row) for row in psi]
             and old_m[1:] == new_m[1:], "F_CARRIER")

    def bracket(self, multiplier, psi, eta):
        gp, ge = self.gamma(psi), self.gamma(eta)
        ep = self.second_direction(multiplier_add(multiplier, gp), eta)
        em = self.second_direction(multiplier_add(multiplier, gp, -O), eta)
        pp = self.second_direction(multiplier_add(multiplier, ge), psi)
        pm = self.second_direction(multiplier_add(multiplier, ge, -O), psi)
        derivatives = [array_scale(array_add(array_add(ep[i], em[i], -O),
                                            array_add(pp[i], pm[i], -O), -O), F(1, 2))
                       for i in range(4)]
        base = array_add(generator(generator(self.x, psi), eta),
                         generator(generator(self.x, eta), psi), -O)
        raw = array_add(base, derivatives[0])
        adjusted = array_add(raw, derivatives[1])
        reversed_adjustment = array_add(raw, derivatives[1], -O)
        need(is_zero(derivatives[2]) and is_zero(derivatives[3]), "F_BRACKET")
        # delta0 M is the state-independent Gamma; delta1 M=delta2 M=0.
        # Their multiplier commutator coefficients are therefore identically
        # zero, and the computed auxiliary coefficients above are zero too.
        t = [mean(row) for row in psi]
        s = [mean(row) for row in eta]
        prediction = zeros(self.T + 1, 6)
        for n in range(1, self.T):
            prediction[n] = [(-(s[n] * t[n + 1] - t[n] * s[n + 1]) * self.f[n + 1][r]
                              - (s[n] * t[n - 1] - t[n] * s[n - 1]) * self.f[n - 1][r]) / 4
                             for r in range(6)]
        need(raw == prediction and is_zero(adjusted), "F_BRACKET")
        need(self.da(raw) == 0, "F_BRACKET")
        return raw, adjusted, reversed_adjustment


def scalar_ward(state, multiplier, psi):
    t, _, u, _, _ = state.parameter_data(psi)
    alpha_only = empty_multiplier(state.T)
    alpha_only[0][:] = multiplier[0][:]
    gamma_t = empty_multiplier(state.T)
    for b in range(1, state.T + 1):
        gamma_t[0][b] = t[b] - t[b - 1]
    dsh = (state.hom_action(multiplier_add(alpha_only, gamma_t))
           - state.hom_action(multiplier_add(alpha_only, gamma_t, -O))) / 2
    total = dsh + state.di(alpha_only, u) + state.da(state.hom_direction(alpha_only, t))
    need(total == 0, "F_SCALAR")


def ward_case(state, multiplier, tau, p, psi, eta, controls):
    gam = state.gamma(psi)
    mp, mmult = multiplier_add(multiplier, gam), multiplier_add(multiplier, gam, -O)
    d0s0 = (state.baux(mp, tau, p) - state.baux(mmult, tau, p)) / 2
    d0i = (state.interaction(state.x, mp) - state.interaction(state.x, mmult)) / 2
    first = generator(state.x, psi)
    d1s0 = state.da(first)
    need(d0s0 == 0 and d0i + d1s0 == 0, "F_LOWER")
    d0s2 = (state.second_action(mp) - state.second_action(mmult)) / 2
    d1i = state.di(multiplier, first)
    direction = state.second_direction(multiplier, psi)
    raw, skew, ftau, jp = direction
    state.tangent_check(multiplier, psi, direction)
    tauwork = (state.baux(multiplier, array_add(tau, ftau), p)
               - state.baux(multiplier, array_add(tau, ftau, -O), p)) / 2
    pwork = (state.baux(multiplier, tau, array_add(p, jp))
             - state.baux(multiplier, tau, array_add(p, jp, -O))) / 2
    adjusted = array_add(raw, skew)
    d2raw = state.da(raw) + tauwork + pwork
    d2adj = state.da(adjusted) + tauwork + pwork
    skewwork = state.da(skew)
    need(skewwork == 0, "F_SKEW")
    need(d0s2 + d1i + d2raw == 0 and d0s2 + d1i + d2adj == 0, "F_WARD")
    scalar_ward(state, multiplier, psi)
    terms = [d0s0, d0i, d1s0, d0s2, d1i, d2raw, d2adj, skewwork]
    denominator = math.lcm(*(value.denominator for value in terms))
    integers = [denominator * value for value in terms]
    need(all(value.denominator == 1 for value in integers)
         and integers[3] + integers[4] + integers[5] == 0
         and integers[3] + integers[4] + integers[6] == 0, "F_INTEGER")
    hom_derivative = (state.hom_action(mp) - state.hom_action(mmult)) / 2
    defects = [d1i + d2adj,
               d0s2 + d1i + d2adj - tauwork,
               d0s2 + d1i + d2adj - pwork,
               d0s2 + d1i + d2adj - 2 * tauwork,
               d0s2 - 2 * hom_derivative + d1i + d2adj,
               hom_derivative + d1i + d2adj]
    for index, value in enumerate(defects):
        controls[index] = controls[index] or value != 0
    raw_bracket, _, _ = state.bracket(multiplier, psi, eta)
    tangent_values = flatten(adjusted) + flatten(ftau[1:]) + flatten(jp[1:state.T])
    return terms, tangent_values, flatten(raw_bracket)


def locality(state, payload):
    basis, labels = [], []
    T = state.T
    for b in range(1, T + 1):
        direction = empty_multiplier(T)
        direction[0][b] = O
        basis.append(direction)
        labels.append(b)
    for b in range(1, T + 1):
        for r in range(4):
            direction = empty_multiplier(T)
            direction[1][b][r], direction[1][b][4] = O, -O
            basis.append(direction)
            labels.append(b)
    for n in range(1, T):
        for edge in range(10):
            direction = empty_multiplier(T)
            direction[2][n][edge] = O
            basis.append(direction)
            labels.append(n)
    need(len(basis) == 65 and state.second_action(empty_multiplier(T)) == 0, "F_LOCALITY")
    singles = [state.second_action(direction) for direction in basis]
    count = 0
    for i in range(len(basis)):
        for j in range(i + 1, len(basis)):
            if abs(labels[i] - labels[j]) > 1:
                mixed = state.second_action(multiplier_add(basis[i], basis[j])) - singles[i] - singles[j]
                need(mixed == 0, "F_LOCALITY")
                payload.append(f"L|{i}|{j}|{mixed}")
                count += 1
    return count


def certificate():
    authority()
    geometry = Geometry()
    payload, controls = [], [False] * 8
    states, cases = 0, 0
    for T in (3, 4, 5, 7):
        for q in (1, 2, 3):
            authority()
            x, multiplier, tau, p = fixture(geometry, T, q)
            state = AuditState(geometry, x)
            state.carrier_check(multiplier, tau, p)
            scalars = [state.action(x), state.baux(multiplier, tau, p),
                       state.interaction(x, multiplier), state.second_action(multiplier)]
            payload.append(f"S|{T}|{q}|" + "|".join(map(str, scalars)))
            eta = [[Z] * 5] + [[z(q + 3, n, 42 + r) for r in range(5)]
                               for n in range(1, T)] + [[Z] * 5]
            for i, psi in enumerate(parameter_list(T, q)):
                terms, tangent, bracket = ward_case(state, multiplier, tau, p, psi, eta, controls)
                payload.append(f"W|{T}|{q}|{i}|" + "|".join(map(str, terms)))
                payload.append(f"G|{T}|{q}|{i}|" + encode(tangent))
                payload.append(f"B|{T}|{q}|{i}|" + encode(bracket))
                cases += 1
            states += 1
    local_x, _, _, _ = fixture(geometry, 5, 1)
    distant = locality(AuditState(geometry, local_x), payload)

    witness_x = zeros(5, 6)
    witness_x[3] = [O, Z, -O, Z, Z, Z]
    witness = AuditState(geometry, witness_x)
    psi, eta = zeros(5, 5), zeros(5, 5)
    psi[1], eta[2] = [O] * 5, [O] * 5
    raw, adjusted, reverse = witness.bracket(empty_multiplier(4), psi, eta)
    expected = zeros(5, 6)
    expected[1] = [-value / 4 for value in witness_x[3]]
    need(raw == expected and is_zero(adjusted), "F_BRACKET")
    controls[6] = raw == expected and not is_zero(raw)
    controls[7] = reverse == array_scale(expected, F(2)) and not is_zero(reverse)
    payload.append("E|RAW|" + encode(flatten(raw)))
    payload.append("E|ADJUSTED|" + encode(flatten(adjusted)))
    for i, detected in enumerate(controls, 1):
        need(detected, "F_CONTROL")
        payload.append(f"N|NC{i:02d}|DETECTED")
    need(states == 12 and cases == 237 and distant == 900, "F_COUNTS")
    digest = hashlib.sha256(("\n".join(payload) + "\n").encode("ascii")).hexdigest()
    lines = [f"CERTIFICATE={NAME}", "AUTHORITY_FILES=5", f"OFF_SHELL_STATES={states}"]
    for label in ("LOWER_ORDER_CASES", "SCALAR_WARD_CASES", "RAW_WARD_CASES",
                  "ADJUSTED_WARD_CASES", "SKEW_WORK_CASES", "TANGENT_CASES", "COMMUTATOR_PAIRS"):
        lines.append(f"{label}={cases}")
    lines += [f"DISTANT_MULTIPLIER_PAIRS={distant}", f"INTEGER_WARD_CASES={cases}",
              "RAW_WITNESS=-1/4,0,1/4,0,0,0", "ADJUSTED_WITNESS=0,0,0,0,0,0",
              f"PAYLOAD_SHA256={digest}", "NEGATIVE_CONTROLS=8", "CERTIFICATE_RESULT=PASS"]
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        primary = certificate()
        try:
            other = subprocess.run([sys.executable, "-I", str(HERE / "breaker.py")],
                                   cwd=ROOT, capture_output=True, timeout=540, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise ScientificFailure("F_BYTES") from None
        need(other.returncode == 0 and other.stderr == b"" and other.stdout == primary, "F_BYTES")
        sys.stdout.buffer.write(primary + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    except ScientificFailure as failure:
        sys.stdout.buffer.write((str(failure) + "\nRESULT=FAIL\n").encode("ascii"))


if __name__ == "__main__":
    main()
