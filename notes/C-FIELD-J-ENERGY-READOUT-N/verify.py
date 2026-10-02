#!/usr/bin/env python3
"""NON-CANONICAL exact L1 audit. Execute only after the registered public pin.

Universal identities use sparse formal polynomials, not sampled vectors.
Finite chain trajectories audit the written all-time induction only.
No local project modules, files, network, randomness or floating point.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import json
import sys


AF = ((1, 0, 1, 0), (0, 1, 0, 1), (-2, 1, -1, 1), (1, -3, 1, -2))
BF = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
CC = ((0, 1, 0, 0), (0, 0, 1, -1), (1, -1, 0, -1), (0, 1, -2, 1))
CI = ((2, -2, 1, -1), (1, 0, 0, 0), (1, -1, 0, -1), (1, -2, 0, -1))
Z = ((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1))
MJ = ((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1))
LM = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
VI = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
K = ((2, 0, -1, -1), (0, 2, 0, -1), (-1, 0, 2, 0), (-1, -1, 0, 2))
KI5 = ((6, 2, 3, 4), (2, 4, 1, 3), (3, 1, 4, 2), (4, 3, 2, 6))
CRAW = ((1, -1), (-1, 0), (0, 1), (0, 1))
KM = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
I4 = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
ZERO4 = (0, 0, 0, 0)
ZERO6 = (0, 0, 0, 0, 0, 0)
ZM = (ZERO4, ZERO4, ZERO4)
R = ((1, -2, 1, 0), ZERO4, ZERO4)
AM = ((1, 0, 0, 0), (0, -1, 0, 0), (0, -1, 1, 0))
ONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
W1 = (0, 0, 1, 0)
INTERVALS = ((-3, 3), (-2, 2), (-2, 2), (-3, 3))


class Polynomial:
    """Exact Q[a,b,c,d], represented by all nonzero monomial coefficients."""

    def __init__(self, terms):
        if isinstance(terms, Polynomial):
            terms = terms.terms
        elif isinstance(terms, (int, Fraction)):
            terms = {(0, 0, 0, 0): terms}
        self.terms = {m: Fraction(v) for m, v in terms.items() if v}

    def __add__(self, other):
        out = self.terms.copy()
        for m, v in Polynomial(other).terms.items():
            out[m] = out.get(m, 0) + v
        return Polynomial(out)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({m: -v for m, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-Polynomial(other))

    def __rsub__(self, other):
        return Polynomial(other) + (-self)

    def __mul__(self, other):
        out = {}
        for m, v in self.terms.items():
            for n, w in Polynomial(other).terms.items():
                exponent = tuple(x + y for x, y in zip(m, n))
                out[exponent] = out.get(exponent, 0) + v * w
        return Polynomial(out)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.terms == Polynomial(other).terms

    def __repr__(self):
        return repr(sorted(self.terms.items()))


def mv(matrix, vector):
    return tuple(sum(x * y for x, y in zip(row, vector)) for row in matrix)


def transpose(matrix):
    return tuple(zip(*matrix))


def mm(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in columns)
                 for row in left)


def matrix_add(left, right, sign=1):
    return tuple(tuple(a + sign * b for a, b in zip(x, y))
                 for x, y in zip(left, right))


def matrix_scale(matrix, scalar):
    return tuple(tuple(scalar * a for a in row) for row in matrix)


def ring_mul(left, right):
    # Cyclic degree-five convolution, followed by eliminating j^4.
    out = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[(i + j) % 5] += x * y
    return tuple(out[i] - out[4] for i in range(4))


def automorphism(vector, exponent):
    out = [0] * 5
    for i, x in enumerate(vector):
        out[(exponent * i) % 5] += x
    return tuple(out[i] - out[4] for i in range(4))


def trace(vector):
    return 4 * vector[0] - sum(vector[1:])


def h(vector):
    a, b, c, d = vector
    return (2*a*a - 2*a*b + 3*b*b + c*c + d*d
            + 2*a*c - a*d - b*c + 3*b*d)


def uv(vector):
    a, b, c, d = vector
    return (a*a + b*b + c*c + d*d - a*b - b*c - c*d,
            a*b + b*c + c*d - a*c - a*d - b*d)


def norm(vector):
    u, v = uv(vector)
    return u*u + u*v - v*v


def pair(vector):
    return h(mv(CC, vector)), h(mv(CC, mv(MJ, vector)))


def reading(vector):
    e0, e1 = pair(vector)
    return e0, e1, tuple(x % 5 for x in vector)


def inverse(datum):
    if type(datum) is not tuple or len(datum) != 3:
        return None
    e0, e1, residue = datum
    if type(e0) is not int or type(e1) is not int:
        return None
    if type(residue) is not tuple or len(residue) != 4:
        return None
    if any(type(x) is not int or x < 0 or x > 4 for x in residue):
        return None
    if not 0 <= e0 <= 5:
        return None
    if e0 == 0:
        return (ZERO4, ZERO4) if e1 == 0 and residue == ZERO4 else None
    n = -e0*e0 + 3*e0*e1 - e1*e1
    if e1 <= 0 or not 1 <= n <= 31:
        return None
    choices = [tuple(x for x in range(lo, hi + 1) if x % 5 == r)
               for (lo, hi), r in zip(INTERVALS, residue)]
    matches = [a for a in product(*choices) if pair(a) == (e0, e1)]
    if len(matches) != 1:
        return None
    a = matches[0]
    return a, mv(CC, a)


def symbolic_audit():
    assert mm(CC, CI) == mm(CI, CC) == I4
    assert mm(AF, CC) == mm(CC, Z)
    assert matrix_add(I4, mm(Z, Z)) == MJ
    jf = matrix_add(I4, mm(AF, AF))
    assert mm(jf, CC) == mm(CC, MJ)
    assert mm(mm(transpose(AF), BF), AF) == BF
    assert mm(mm(transpose(CC), BF), CC) == K
    assert mm(K, KI5) == mm(KI5, K) == matrix_scale(I4, 5)
    assert mm(matrix_add(I4, AF, -1),
              matrix_add(I4, mm(AF, AF), -1)) == LM
    assert mm(AF, LM) == mm(LM, AF)
    assert mm(LM, VI) == mm(VI, LM) == matrix_scale(I4, 5)
    assert mm(mm(transpose(LM), BF), LM) == matrix_scale(BF, 5)
    power = I4
    for _ in range(5):
        power = mm(AF, power)
    assert power == I4
    variables = tuple(Polynomial({tuple(int(i == j) for i in range(4)): 1})
                      for j in range(4))
    a, b, c, d = variables
    u, v = uv(variables)
    e0, e1 = pair(variables)
    assert e0 == a*a + b*b + c*c + d*d - a*c - a*d - b*d
    assert e0 == u + v and e1 == u
    absolute_square = ring_mul(variables, automorphism(variables, 4))
    assert absolute_square == (u, Polynomial(0), -v, -v)
    assert trace(absolute_square) == 2 * (e0 + e1)
    assert trace(absolute_square) == 5*sum(x*x for x in variables)-sum(variables)*sum(variables)
    ja = ring_mul(J, variables)
    assert ja == mv(MJ, variables)
    j_absolute_square = ring_mul(ja, automorphism(ja, 4))
    assert trace(j_absolute_square) == 2 * (4*e1 - e0)
    assert uv(ja) == (2*u - v, v - u)
    n = ring_mul(absolute_square, automorphism(absolute_square, 2))
    expected_n = -e0*e0 + 3*e0*e1 - e1*e1
    assert n == (expected_n, Polynomial(0), Polynomial(0), Polynomial(0))
    assert expected_n == norm(variables)
    assert ring_mul(J, automorphism(J, 4)) == (2, 0, 1, 1)
    assert pair(J) == (1, 2)
    assert h(mv(AF, mv(CC, J))) == 1
    assert mv(CC, J) == (0, 1, 1, -2)
    assert mv(jf, mv(CC, J)) == (-1, 2, 2, -4)
    return {"method": "all_multivariate_coefficients",
            "variables": 4, "maximum_degree": 4}


def sector_audit():
    forward = {}
    shells = Counter()
    members = []
    scanned = 0
    for a in product(*(range(lo, hi + 1) for lo, hi in INTERVALS)):
        scanned += 1
        energy = h(mv(CC, a))
        assert energy >= 0
        if energy > 5:
            continue
        shells[energy] += 1
        members.append(a)
        key = reading(a)
        assert key not in forward
        forward[key] = a
        assert inverse(key) == (a, mv(CC, a))
        assert 0 <= norm(a) <= 31
        assert 0 <= key[1] <= 13
    assert scanned == 1225
    shell_counts = [shells[i] for i in range(6)]
    assert shell_counts == [1, 20, 30, 60, 60, 120]
    assert len(members) == len(forward) == 291
    max_norm = max(norm(a) for a in members)
    assert max_norm == 31
    checked = 0
    accepted = 0
    residues = tuple(product(range(5), repeat=4))
    for e0, e1, residue in product(range(6), range(14), residues):
        key = e0, e1, residue
        output = inverse(key)
        expected = forward.get(key)
        assert output == (None if expected is None else (expected, mv(CC, expected)))
        checked += 1
        accepted += output is not None
    assert checked == 52500 and accepted == 291
    outside = 0
    for e0, e1, residue in product((-1, 6), (-1, 0, 1, 13, 14, 10000), residues):
        assert inverse((e0, e1, residue)) is None
        outside += 1
    for e0, e1, residue in product(range(6), (-1, 14, 10000), residues):
        assert inverse((e0, e1, residue)) is None
        outside += 1
    malformed = (
        None, [], {}, 0, (), (0,), (0, 0), (0, 0, ZERO4, 0),
        ([0], 0, ZERO4), (True, 0, ZERO4), (0, False, ZERO4),
        (Fraction(0), 0, ZERO4), (0, "0", ZERO4), (0, 0, [0, 0, 0, 0]),
        (0, 0, (0, 0, 0)), (0, 0, (0, 0, 0, 0, 0)),
        (0, 0, (False, 0, 0, 0)), (0, 0, (Fraction(0), 0, 0, 0)),
        (0, 0, (-1, 0, 0, 0)), (0, 0, (5, 0, 0, 0)),
    )
    assert all(inverse(x) is None for x in malformed)
    j = (0, 1, 0, 0)
    assert pair(ONE) == pair(j) == (1, 1)
    assert inverse(reading(ONE))[0] == ONE
    assert inverse(reading(j))[0] == j
    assert inverse(reading(ONE)) != inverse(reading(j))
    seeds = tuple(mv(CC, a) for a in members if h(mv(CC, a)) == 1)
    return seeds, {"scanned": scanned, "states": len(members),
                   "shells": shell_counts, "max_norm": max_norm,
                   "complete_key_checks": checked, "accepted_keys": accepted,
                   "outside_key_checks": outside, "malformed_checks": len(malformed)}


def low(vector):
    s = sum(vector)
    denominator = 4 * trace(ring_mul(vector, automorphism(vector, 4)))
    return None if denominator == 0 else Fraction(s*s, denominator)


def source_audit():
    w2 = mv(AF, W1)
    assert w2 == (1, 0, -1, 1)
    assert h(W1) == h(w2) == 1
    first = mv(CI, mv(LM, W1))
    second = mv(CI, mv(LM, w2))
    ell = ring_mul((1, -1, 0, 0), (1, 0, -1, 0))
    assert first == ell == (1, -1, -1, 1)
    assert second == ring_mul((0, 1, 0, 0), ell) == (-1, 0, -2, -2)
    assert all(-2 <= x <= 2 for a in (first, second) for x in a)
    assert uv(first) == uv(second) == (5, 0)
    assert pair(first) == pair(second) == (5, 5)
    assert norm(first) == norm(second) == 25
    assert trace(ring_mul(first, automorphism(first, 4))) == 20
    assert trace(ring_mul(second, automorphism(second, 4))) == 20
    assert low(first) == 0 and low(second) == Fraction(5, 16)
    assert low(ZERO4) is None
    return {"energy_pairs": [[5, 5], [5, 5]], "full_traces": [20, 20],
            "low_ratios": [[0, 1], [5, 16]]}


def embed(y, static=(0, 0)):
    a, b, c, d = y
    u, v = static
    return a-b+u, -a+u, b+v, b+u-v, c, d


def split(raw):
    e0, e1, e2, e3, m0, m1 = raw
    numerators = (2*e0-3*e1+e2+e3, -e0-e1+2*e2+2*e3,
                  2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3)
    if any(x % 5 for x in numerators):
        return None
    a, b, u, v = (x // 5 for x in numerators)
    return (a, b, m0, m1), (u, v)


def react(cell):
    matter, spectators, raw, resource = cell
    if matter not in (R, AM):
        return cell, "NONENDPOINT", 0
    parts = split(raw)
    if parts is None:
        return cell, "NONSPLIT", 0
    y, static = parts
    if matter == R:
        if (y[0] + 2*y[1]) % 5 or (y[2] + 2*y[3]) % 5:
            return cell, "OFFIMAGE", 0
        numerator = mv(VI, y)
        assert all(x % 5 == 0 for x in numerator)
        x = tuple(x // 5 for x in numerator)
        resource_new = resource + 4*h(x) - 2
        if resource_new < 0:
            return cell, "R_FUND", 0
        return (AM, spectators, embed(x, static), resource_new), "R_ACCEPT", 1
    resource_new = resource + 2 - 4*h(y)
    if resource_new < 0:
        return cell, "AM_FUND", 0
    return (R, spectators, embed(mv(LM, y), static), resource_new), "AM_ACCEPT", 0


def free_field(raw):
    electric, magnetic = raw[:4], raw[4:]
    cm = mv(CRAW, magnetic)
    electric_new = tuple(x + y for x, y in zip(electric, cm))
    correction = mv(transpose(CRAW), electric_new)
    magnetic_new = tuple(x - y for x, y in zip(magnetic, correction))
    return electric_new + magnetic_new


def energy(state):
    cells, channels, pointer = state
    assert 0 <= pointer < 5
    total = 1 + sum(channels)
    for matter, spectators, raw, resource in cells:
        assert resource >= 0
        for vector in matter + spectators:
            total += sum(x*y for x, y in zip(vector, mv(KM, vector)))
        electric, magnetic = raw[:4], raw[4:]
        total += (sum(x*x for x in raw)
                  + sum(x*y for x, y in zip(electric, mv(CRAW, magnetic)))
                  + resource)
    assert all(x >= 0 for x in channels)
    return total


def prepare(n, seed):
    cells = [(R, ZM, embed(mv(LM, seed)), 0)]
    cells += [(ZM, ZM, ZERO6, 0) for _ in range(n - 2)]
    cells += [(R, ZM, ZERO6, 0)]
    return tuple(cells), (0,) * (n - 1), 0


def layer(state, which):
    old_cells, old_channels, pointer = state
    cells, channels = list(old_cells), list(old_channels)
    branches = ()
    if which == "G":
        branches_list = []
        for i, cell in enumerate(cells):
            cells[i], branch, event = react(cell)
            branches_list.append(branch)
            if i == len(cells) - 1:
                pointer = (pointer + event) % 5
        branches = tuple(branches_list)
    elif which == "A":
        for j in range(len(channels)):
            old_resource = cells[j][3]
            cells[j] = cells[j][:3] + (channels[j],)
            channels[j] = old_resource
    elif which == "B":
        for j in range(len(channels)):
            old_resource = cells[j + 1][3]
            cells[j + 1] = cells[j + 1][:3] + (channels[j],)
            channels[j] = old_resource
    elif which == "F":
        cells = [(m, b, free_field(z), r) for m, b, z, r in cells]
    else:
        raise ValueError(which)
    return (tuple(cells), tuple(channels), pointer), branches


def shared_coordinates(state):
    cells, channels, pointer = state
    source = cells[0]
    # Only the source raw field is omitted; all other stored data are compared.
    return (source[0], source[1], source[3]), cells[1:], channels, pointer


def induction_invariant(state, phase):
    cells, channels, pointer = state
    source = cells[0]
    assert h(phase) == 1
    assert source[0] in (R, AM)
    expected = mv(LM, phase) if source[0] == R else phase
    assert source[2] == embed(expected)
    assert all(cell[1] == ZM for cell in cells)
    assert all(cell[2] == ZERO6 for cell in cells[1:])
    assert all(cell[0] == ZM for cell in cells[1:-1])
    assert cells[-1][0] in (R, AM)
    assert energy(state) == 42


def chain_audit(seeds):
    assert len(seeds) == 20 and W1 in seeds
    comparisons = 0
    source_coverage, receiver_coverage = set(), set()
    for n in range(2, 7):
        baseline = prepare(n, W1)
        reference = [shared_coordinates(baseline)]
        for _ in range(80):
            for which in ("G", "A", "B", "F"):
                baseline, _branches = layer(baseline, which)
                reference.append(shared_coordinates(baseline))
        for seed in seeds:
            state, phase = prepare(n, seed), seed
            index = 0
            assert shared_coordinates(state) == reference[index]
            induction_invariant(state, phase)
            for _ in range(80):
                for which in ("G", "A", "B", "F"):
                    state, branches = layer(state, which)
                    if which == "G":
                        source_coverage.add(branches[0])
                        receiver_coverage.add(branches[-1])
                    if which == "F":
                        phase = mv(AF, phase)
                    index += 1
                    assert shared_coordinates(state) == reference[index]
                    induction_invariant(state, phase)
                    comparisons += 1
    assert comparisons == 32000
    assert source_coverage == {"R_ACCEPT", "AM_ACCEPT", "AM_FUND"}
    assert receiver_coverage == {"R_ACCEPT", "AM_ACCEPT", "R_FUND"}
    return {"lengths": [2, 3, 4, 5, 6], "seeds": len(seeds),
            "macrosteps_per_run": 80, "layer_comparisons": comparisons,
            "source_branches": sorted(source_coverage),
            "receiver_branches": sorted(receiver_coverage),
            "all_time_basis": "written_substep_induction"}


def rejection_audit():
    spectators = ((1, 0, 0, 0), (0, -1, 0, 0), (0, 0, 1, -1))
    rejected = (
        ((ZM, spectators, ZERO6, 7), "NONENDPOINT"),
        ((R, spectators, (1, 0, 0, 0, 0, 0), 7), "NONSPLIT"),
        ((R, spectators, embed((1, 0, 0, 0)), 7), "OFFIMAGE"),
        ((R, spectators, embed((0, 0, 1, 0)), 7), "OFFIMAGE"),
        ((R, spectators, ZERO6, 1), "R_FUND"),
        ((AM, spectators, embed(W1), 1), "AM_FUND"),
    )
    for cell, reason in rejected:
        assert react(cell) == (cell, reason, 0)
    accepted = (
        (R, ZERO4, 2), (AM, ZERO4, 0),
        (R, mv(LM, W1), 0), (AM, W1, 2),
    )
    for matter, active, resource in accepted:
        cell = matter, spectators, embed(active, (1, -1)), resource
        output, branch, event = react(cell)
        assert branch == ("R_ACCEPT" if matter == R else "AM_ACCEPT")
        assert event == int(matter == R)
        assert output[1] == spectators and split(output[2])[1] == (1, -1)
        assert react(output)[0] == cell
        assert energy(((cell,), (), 0)) == energy(((output,), (), 0))
    return {"rejected_fixtures": len(rejected), "accepted_fixtures": len(accepted)}


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact audit requires assertions enabled")
    symbolic = symbolic_audit()
    seeds, sector = sector_audit()
    sources = source_audit()
    local = rejection_audit()
    chain = chain_audit(seeds)
    result = {"candidate": "C-FIELD-J-ENERGY-READOUT-N", "status": "PASS",
              "layer": "L1", "symbolic": symbolic, "sector": sector,
              "sources": sources, "local_branches": local, "chain_audit": chain}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
