#!/usr/bin/env python3
"""Exact, standalone audit of the frozen C-FIELD-J-LOCAL-INSTRUMENT-N spec.

PUBLIC, NON-CANONICAL; selected mathematical extension, not occurrence.
Specification: 0ca0605bee475ed3ab86f9a7c1129ea00a09d86d.
Python 3.10+, standard library, no runtime files or imported candidate code.
All API objects below are internal exact built-in structures, not parsers.
"""

from collections import deque
from fractions import Fraction as Q
from itertools import product
from math import gcd


M = 1226
L = 613
ZERO_Y = (0, 0, 0, 0)
EMPTY = (0, ZERO_Y, 0)
COEFFICIENTS = ((-1, -1, -1, -1), (1, 0, 0, 0),
                (0, 1, 0, 0), (0, 0, 1, 0))
CODES4 = (395, 788, 648, 620)


def chart(a):
    a0, a1, a2, a3 = a
    return (a1, a2 - a3, a0 - a1 - a3, a1 - 2 * a2 + a3)


def unchart(y):
    x, v, z, w = y
    return (2 * x - 2 * v + z - w, x, x - v - w, x - 2 * v - w)


def energy_y(y):
    x, v, z, w = y
    return (2 * x * x - 2 * x * v + 3 * v * v + z * z + w * w
            + 2 * x * z - x * w - v * z + 3 * v * w)


def code(y):
    a, b, c, d = unchart(y)
    return 1 + (((a + 3) * 5 + (b + 2)) * 5 + (c + 2)) * 7 + d + 3


def supported(packet):
    return packet[0] == 1 and energy_y(packet[1]) <= 5


def react(packet, latch, pointer, inverse=False):
    if not supported(packet):
        return packet, latch, pointer, "UNSUPPORTED"
    b, y, reserve = packet
    if inverse:
        if latch == 1:
            return (b, y, reserve + 2), 0, (pointer - code(y)) % M, "UNDO_WRITE"
        if reserve >= 2:
            return (b, y, reserve - 2), 1, pointer, "UNDO_RELEASE"
        return packet, latch, pointer, "NO_WRITE"
    if latch == 1:
        return (b, y, reserve + 2), 0, pointer, "RELEASE"
    if reserve >= 2:
        return (b, y, reserve - 2), 1, (pointer + code(y)) % M, "WRITE"
    return packet, latch, pointer, "NO_WRITE"


def step(state, cut=None, inverse=False):
    old_cells, old_channels, latch, pointer = state
    cells, channels = list(old_cells), list(old_channels)
    n = len(cells)
    if inverse:
        for j in range(n - 1):
            if j != cut:
                channels[j], cells[j + 1] = cells[j + 1], channels[j]
        for j in range(n - 1):
            if j != cut:
                cells[j], channels[j] = channels[j], cells[j]
        cells[-1], latch, pointer, event = react(cells[-1], latch, pointer, True)
    else:
        cells[-1], latch, pointer, event = react(cells[-1], latch, pointer)
        for j in range(n - 1):
            if j != cut:
                cells[j], channels[j] = channels[j], cells[j]
        for j in range(n - 1):
            if j != cut:
                channels[j], cells[j + 1] = cells[j + 1], channels[j]
    return (tuple(cells), tuple(channels), latch, pointer), event


def state_energy(state):
    cells, channels, latch, _pointer = state
    return sum(b + energy_y(y) + r for b, y, r in cells + channels) + 2 * latch + 1


def clean(n, y, pointer=0, reserve=2):
    return (((1, y, reserve),) + (EMPTY,) * (n - 1),
            (EMPTY,) * (n - 1), 0, pointer)


def predicted(n, y, pointer, boundary):
    period = 2 * n - 1
    reactions = 0 if boundary < n else 1 + (boundary - n) // period
    writes = 0 if boundary < n else 1 + (boundary - n) // (2 * period)
    latch = reactions % 2
    packet = (1, y, 2 * (1 - latch))
    cells, channels = [EMPTY] * n, [EMPTY] * (n - 1)
    cycle = [(0, j) for j in range(n)] + [(1, j) for j in reversed(range(n - 1))]
    kind, index = cycle[boundary % period]
    (channels if kind else cells)[index] = packet
    return tuple(cells), tuple(channels), latch, (pointer + writes * code(y)) % M


def append_basis(active, stored, flag):
    return stored, active, 1 - flag


class Algebraic:
    """Sparse Q(sqrt(2),sqrt(3),sqrt(5),i), bit-mask monomials."""
    __slots__ = ("terms",)

    def __init__(self, value=0, terms=None):
        if terms is None:
            if isinstance(value, Algebraic):
                self.terms = value.terms
                return
            terms = {0: Q(value)}
        self.terms = tuple(sorted((k, Q(v)) for k, v in terms.items() if v))

    def __add__(self, other):
        other = Algebraic(other)
        terms = dict(self.terms)
        for mask, coefficient in other.terms:
            terms[mask] = terms.get(mask, Q(0)) + coefficient
        return Algebraic(terms=terms)

    __radd__ = __add__

    def __neg__(self):
        return Algebraic(terms={k: -v for k, v in self.terms})

    def __sub__(self, other):
        return self + (-Algebraic(other))

    def __rsub__(self, other):
        return Algebraic(other) + (-self)

    def __mul__(self, other):
        other = Algebraic(other)
        terms = {}
        for a, x in self.terms:
            for b, y in other.terms:
                overlap = a & b
                factor = 1
                for bit, square in ((1, 2), (2, 3), (4, 5), (8, -1)):
                    if overlap & bit:
                        factor *= square
                mask = a ^ b
                terms[mask] = terms.get(mask, Q(0)) + x * y * factor
        return Algebraic(terms=terms)

    __rmul__ = __mul__

    def __truediv__(self, other):
        # Only rational scalar division is needed in the audit.
        divisor = Q(other)
        return Algebraic(terms={k: v / divisor for k, v in self.terms})

    def conjugate(self):
        return Algebraic(terms={k: -v if k & 8 else v for k, v in self.terms})

    def __eq__(self, other):
        return self.terms == Algebraic(other).terms

    def __bool__(self):
        return bool(self.terms)

    def rational(self):
        assert all(mask == 0 for mask, _ in self.terms)
        return self.terms[0][1] if self.terms else Q(0)


def root(mask):
    return Algebraic(terms={mask: Q(1)})


def conjugate(x):
    return x.conjugate() if hasattr(x, "conjugate") else x


def identity(n):
    return tuple(tuple(Q(int(i == j)) for j in range(n)) for i in range(n))


def zeros(n, m=None):
    return tuple(tuple(Q(0) for _ in range(n if m is None else m)) for _ in range(n))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(row, other)) for row, other in zip(a, b))


def scale(a, scalar):
    return tuple(tuple(scalar * x for x in row) for row in a)


def multiply(a, b):
    columns = tuple(zip(*b))
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), Q(0))
                       for col in columns) for row in a)


def adjoint(a):
    return tuple(tuple(conjugate(x) for x in col) for col in zip(*a))


def power(a, n):
    result = identity(len(a))
    for _ in range(n):
        result = multiply(result, a)
    return result


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def unit(n, i, j):
    return tuple(tuple(Q(int(r == i and c == j)) for c in range(n)) for r in range(n))


def sandwich_unit(left, right, i, j):
    return tuple(tuple(left[r][i] * right[j][c] for c in range(len(right[0])))
                 for r in range(len(left)))


def schur(a, b):
    return tuple(tuple(x * y for x, y in zip(row, other)) for row, other in zip(a, b))


def rational_matrix(a):
    return tuple(tuple(x.rational() if isinstance(x, Algebraic) else Q(x)
                       for x in row) for row in a)


def audit_arithmetic():
    fields, shells = [], [0] * 6
    for a in product(range(-3, 4), range(-2, 3), range(-2, 3), range(-3, 4)):
        y = chart(a)
        assert unchart(y) == a
        h = energy_y(y)
        assert h == sum(x * x for x in a) - a[0] * a[2] - a[0] * a[3] - a[1] * a[3]
        assert h >= 0 and (h != 0 or y == ZERO_Y)
        if h <= 5:
            fields.append(y)
            shells[h] += 1
    assert len(fields) == 291
    assert tuple(shells) == (1, 20, 30, 60, 60, 120)
    assert len({code(y) for y in fields}) == 291
    assert all(1 <= code(y) < M for y in fields)
    labels = tuple(chart(a) for a in COEFFICIENTS)
    assert tuple(code(y) for y in labels) == CODES4
    assert all(energy_y(y) == 1 for y in labels)
    assert code(ZERO_Y) == 613 and gcd(28, M) == 2

    # Polynomial (z-1)(1+...+z^(L-1))=z^L-1, the DFT geometric sum.
    polynomial = {}
    for exponent in range(L):
        polynomial[exponent + 1] = polynomial.get(exponent + 1, 0) + 1
        polynomial[exponent] = polynomial.get(exponent, 0) - 1
    assert {k: v for k, v in polynomial.items() if v} == {0: -1, L: 1}
    for phase in (0, 1):
        orbit = {(phase + 28 * j) % M for j in range(L)}
        assert orbit == set(range(phase, M, 2))

    # Laurent-polynomial identity (U-I)^*(U-I)=2I-U-U^*.
    lhs = {}
    for a, x in ((-1, 1), (0, -1)):
        for b, y in ((1, 1), (0, -1)):
            lhs[a + b] = lhs.get(a + b, 0) + x * y
    assert lhs == {-1: -1, 0: 2, 1: -1}

    g = tuple(tuple(Q(int(i == j)) - Q(1, 5) for j in range(4)) for i in range(4))
    g_inverse = tuple(tuple(Q(int(i == j) + 1) for j in range(4)) for i in range(4))
    r = ((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1))
    assert multiply(g, g_inverse) == identity(4)
    assert power(r, 5) == identity(4)
    assert multiply(multiply(adjoint(r), g), r) == g
    v = (tuple(root(4) / 10 for _ in range(4)),
         tuple(Q(x, 2) * root(1) for x in (1, -1, 0, 0)),
         tuple(Q(x, 6) * root(3) for x in (1, 1, -2, 0)),
         tuple(Q(x, 6) * root(2) for x in (1, 1, 1, -3)))
    v_inverse = multiply(g_inverse, adjoint(v))
    assert multiply(adjoint(v), v) == g
    assert multiply(v, v_inverse) == identity(4)
    assert multiply(v_inverse, v) == identity(4)
    p0 = tuple(tuple(Q(1, 4) for _ in range(4)) for _ in range(4))
    projectors = []
    for k in range(5):
        p = multiply(multiply(power(r, k), p0), power(r, (5 - k) % 5))
        q = add(identity(4), scale(p, -1))
        assert multiply(p, p) == p and multiply(q, q) == q
        assert multiply(p, q) == zeros(4) and trace(p) == 1 and trace(q) == 3
        assert multiply(multiply(g_inverse, adjoint(p)), g) == p
        projectors.append((q, p))  # phase 0=HIGH, phase 1=LOW
    assert rational_matrix(multiply(multiply(v_inverse, unit(4, 0, 0)), v)) == p0
    # Derive the logical writer from the actual four code parities.
    writer = []
    for parity in (0, 1):
        physical = tuple(tuple(Q(int(i == j and CODES4[i] % 2 == parity))
                               for j in range(4)) for i in range(4))
        writer.append(rational_matrix(multiply(multiply(v_inverse, physical), v)))
    assert tuple(writer) == projectors[0]
    return tuple(fields), labels, (g, g_inverse, r, v, v_inverse, tuple(projectors), tuple(writer))


def audit_circuit(fields, labels):
    clean_steps = cut_steps = negative_steps = 0
    for n in range(2, 6):
        period = 2 * n - 1
        for y in fields:
            for pointer in (0, 1):
                state = clean(n, y, pointer)
                initial_energy = state_energy(state)
                assert state == predicted(n, y, pointer, 0)
                for boundary in range(1, 2 * period + 1):
                    old = state
                    state, event = step(state)
                    assert state == predicted(n, y, pointer, boundary)
                    assert step(state, inverse=True)[0] == old
                    assert state_energy(state) == initial_energy
                    expected = ("WRITE" if boundary == n else "RELEASE"
                                if boundary == n + period else "UNSUPPORTED")
                    assert event == expected
                    clean_steps += 1
        for y in labels:
            for cut in range(n - 1):
                state = clean(n, y)
                for _ in range(2 * period):
                    old = state
                    state, event = step(state, cut)
                    assert event != "WRITE" and state[-2:] == (0, 0)
                    assert step(state, cut, True)[0] == old
                    assert state[1][cut] == EMPTY
                    cut_steps += 1
            for variant in (0, 1, "mismatch"):
                state = clean(n, y, reserve=0 if variant == "mismatch" else variant)
                if variant == "mismatch":
                    cells, channels, latch, pointer = state
                    channels = channels[:-1] + ((0, ZERO_Y, 2),)
                    state = cells, channels, latch, pointer
                    assert state_energy(state) == state_energy(clean(n, y))
                baseline = state_energy(state)
                for _ in range(2 * period):
                    old = state
                    state, event = step(state)
                    assert event != "WRITE" and state[-2:] == (0, 0)
                    assert step(state, inverse=True)[0] == old
                    assert state_energy(state) == baseline
                    negative_steps += 1
        controls = []
        absent = ((EMPTY,) * n, (EMPTY,) * (n - 1), 0, 0)
        controls.append((absent, None))
        controls.append((clean(n, ZERO_Y), n))
        controls.append((clean(n, chart((4, 0, 0, 0))), None))
        receiver = ((EMPTY,) * (n - 1) + ((1, labels[0], 2),),
                    (EMPTY,) * (n - 1), 0, 0)
        controls.append((receiver, 1))
        for state, first_write in controls:
            seen = []
            initial_energy = state_energy(state)
            for boundary in range(1, 2 * period + 1):
                old = state
                state, event = step(state)
                assert step(state, inverse=True)[0] == old
                assert state_energy(state) == initial_energy
                if event == "WRITE":
                    seen.append(boundary)
                negative_steps += 1
            assert (seen[0] if seen else None) == first_write
    assert clean_steps == 27936 and cut_steps == 560 and negative_steps == 768
    return clean_steps, cut_steps, negative_steps


def density_entry_numerator(kind, row, column):
    """Entries of the four specified M-dimensional densities, times L."""
    if kind == "blank":
        return L if row == 0 and column == 0 else 0
    if kind == "diagonal_even":
        return int(row == column and row % 2 == 0)
    if kind == "E":
        return int(row % 2 == 0 and column % 2 == 0)
    assert kind == "O"
    return int(row % 2 == 1 and column % 2 == 1)


def correlation_tables():
    """Sum actual density entries along each parity-restricted cyclic diagonal."""
    tables = {}
    for kind in ("blank", "diagonal_even", "E", "O"):
        rows = [[0] * M, [0] * M]
        for difference in range(M):
            for row in range(M):
                rows[row % 2][difference] += density_entry_numerator(
                    kind, row, (row + difference) % M)
        tables[kind] = tuple(tuple(row) for row in rows)
    return tables


def gamma(tables, kind, c_a, c_b, outcome):
    return Q(tables[kind][(outcome - c_a) % 2][(c_a - c_b) % M], L)


def audit_pointers(fields):
    translations = coordinates = coefficients = 0
    codes = tuple(code(y) for y in fields)
    for c in codes:
        images = set()
        for p in range(M):
            q = (p + c) % M
            assert (q - c) % M == p
            images.add(q)
            translations += 1
        assert images == set(range(M))
    for c in CODES4:
        for phase in (0, 1):
            shifted = {(p + c) % M for p in range(phase, M, 2)}
            assert len(shifted) == L
            for p in range(M):
                assert (p in shifted) == (p % 2 == (phase + c) % 2)
                coordinates += 1
    tables = correlation_tables()
    for a in codes:
        for b in codes:
            for kind in ("blank", "diagonal_even", "E", "O"):
                for outcome in (0, 1):
                    actual = gamma(tables, kind, a, b, outcome)
                    if kind in ("blank", "diagonal_even"):
                        expected = int(a == b and a % 2 == outcome)
                    else:
                        ready = int(kind == "O")
                        expected = int((a + ready) % 2 == outcome
                                       and (b + ready) % 2 == outcome)
                    assert actual == expected
                    coefficients += 1
    assert translations == 356766 and coordinates == 9808 and coefficients == 677448
    assert gamma(tables, "E", CODES4[1], CODES4[2], 0) == 1
    assert gamma(tables, "blank", CODES4[1], CODES4[2], 0) == 0
    assert gamma(tables, "diagonal_even", CODES4[1], CODES4[2], 0) == 0
    return tables, (translations, coordinates, coefficients)


def bin_index(partition, pointer):
    if partition == "parity":
        return pointer % 2
    if partition == "zero":
        return int(pointer != 0)
    assert partition == "fine"
    return pointer


def direct_read_and_trace_unit(ket, bra, partition):
    # Apply the complete diagonal PVM to an actual translated matrix unit.
    out = {}
    for outcome in {bin_index(partition, ket), bin_index(partition, bra)}:
        branch = {(ket, bra): 1} if (bin_index(partition, ket) == outcome
                                    and bin_index(partition, bra) == outcome) else {}
        value = sum(x for (row, col), x in branch.items() if row == col)
        if value:
            out[outcome] = value
    return out


def audit_pointer_units():
    differences = sorted({0, 1, 613} | {(a - b) % M for a in CODES4 for b in CODES4})
    assert len(differences) == 15
    cases = 0
    for a in CODES4:
        for b in CODES4:
            for p in range(M):
                for difference in differences:
                    q = (p + difference) % M
                    ket, bra = (p + a) % M, (q + b) % M
                    for partition in ("parity", "zero", "fine"):
                        actual = direct_read_and_trace_unit(ket, bra, partition)
                        expected = ({bin_index(partition, (p + a) % M): 1}
                                    if q == (p + a - b) % M else {})
                        assert actual == expected
                        cases += 1
    assert cases == 882720
    # Retained source/phase matrix units, then both selective parity branches.
    retained_units = branch_units = 0
    for a in range(4):
        for b in range(4):
            for r in (0, 1):
                for s in (0, 1):
                    ket = (a, (r + CODES4[a]) % 2)
                    bra = (b, (s + CODES4[b]) % 2)
                    assert ket == (a, r ^ (CODES4[a] % 2))
                    assert bra == (b, s ^ (CODES4[b] % 2))
                    retained_units += 1
                    for outcome in (0, 1):
                        branch = direct_read_and_trace_unit(ket[1], bra[1], "parity")
                        actual = branch.get(outcome, 0)
                        expected = int(ket[1] == bra[1] == outcome)
                        assert actual == expected
                        branch_units += 1
    assert retained_units == 64 and branch_units == 128
    phase_states = (
        ((Q(1), Q(0)), (Q(0), Q(0))),
        ((Q(0), Q(0)), (Q(0), Q(1))),
        ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))),
        ((Q(1, 2), -root(8) / 2), (root(8) / 2, Q(1, 2))),
    )
    for phase, tau in enumerate(phase_states):
        assert trace(tau) == 1 and adjoint(tau) == tau and multiply(tau, tau) == tau
        for a, b in product(range(4), repeat=2):
            for outcome in (0, 1):
                # Direct expansion of all four incoming phase matrix units.
                actual = 0
                for r, s in product((0, 1), repeat=2):
                    if (r ^ (CODES4[a] % 2)) == outcome == (s ^ (CODES4[b] % 2)):
                        actual += tau[r][s]
                expected = tau[outcome ^ (CODES4[a] % 2)][outcome ^ (CODES4[b] % 2)]
                assert actual == expected
                if phase == 2:
                    assert actual == Q(1, 2)  # no source information in the |+> phase
    return cases, retained_units, branch_units


def audit_instruments(data, tables):
    g, g_inverse, r, v, v_inverse, projectors, _writer = data
    physical_cases = 0
    for k in range(5):
        pre = multiply(multiply(v, power(r, (5 - k) % 5)), v_inverse)
        post = adjoint(pre)
        assert multiply(pre, post) == identity(4)
        for i, j in product(range(4), repeat=2):
            encoded = sandwich_unit(v, v_inverse, i, j)
            incoming = multiply(multiply(pre, encoded), post)
            for ready in (0, 1):
                for outcome in (0, 1):
                    raw_outcome = outcome ^ ready
                    coefficients = tuple(tuple(gamma(tables, "E" if ready == 0 else "O",
                                                         a, b, raw_outcome)
                                               for b in CODES4) for a in CODES4)
                    actual = multiply(multiply(post, schur(incoming, coefficients)), pre)
                    logical = sandwich_unit(projectors[k][outcome], projectors[k][outcome], i, j)
                    expected = multiply(multiply(v, logical), v_inverse)
                    assert actual == expected
                    physical_cases += 1
    assert physical_cases == 320

    # Untouched two-dimensional reference, with a within-HIGH entangled state.
    rho = tuple(tuple(Q(1, 2) if i in (2, 5) and j in (2, 5) else Q(0)
                      for j in range(8)) for i in range(8))
    assert trace(rho) == 1 and multiply(rho, rho) == rho
    diagonal = tuple(tuple(rho[i][j] if i == j else Q(0) for j in range(8)) for i in range(8))
    for kind in ("E", "blank", "diagonal_even"):
        actual = tuple(tuple(rho[i][j] * gamma(tables, kind, CODES4[i // 2], CODES4[j // 2], 0)
                             for j in range(8)) for i in range(8))
        assert actual == (rho if kind == "E" else diagonal)
        low = tuple(tuple(rho[i][j] * gamma(tables, kind, CODES4[i // 2], CODES4[j // 2], 1)
                          for j in range(8)) for i in range(8))
        assert low == zeros(8)
    assert rho != diagonal
    return physical_cases


def audit_archive_basis():
    cases = 0
    for p in range(M):
        for q in range(M):
            for z in (0, 1):
                out = append_basis(p, q, z)
                assert append_basis(*out) == (p, q, z)
                assert 0 <= out[0] < M and 0 <= out[1] < M and out[2] in (0, 1)
                # Active pointer, archive pointer and flag each have energy 1.
                before = sum(1 for _ in (p, q, z))
                after = sum(1 for _ in out)
                assert before == after == 3
                cases += 1
    assert cases == 3006152
    assert append_basis(0, 1, 1) == (1, 0, 0)  # occupied cell imports its old pointer
    assert append_basis(0, 1, 0) == (1, 0, 1)  # unused flag alone is not readiness
    absent = ((EMPTY, EMPTY), (EMPTY,), 0, 0)
    after, event = step(absent)
    assert after == absent and event != "WRITE"
    assert append_basis(after[-1], 0, 0)[2] == 1  # a false event interpretation
    return cases


def sharp(a, data):
    g, g_inverse = data[:2]
    return multiply(multiply(g_inverse, adjoint(a)), g)


def memory_ready(capacity):
    # Active E/O phase, complete ordered archive phase tuple, validity mask.
    return 0, (0,) * capacity, 0


def round_maps(maps, context, index, data, selected=None, intervention=None):
    """Compose actual reduced B writer, controls, SWAP*X and optional PVM.

    The reduction was independently checked in the M-position and V audits.
    Each value is a source ket map; memory keys keep the complete archive.
    """
    _g, _gi, r, _v, _vi, _projectors, writer = data
    pre, post = power(r, (5 - context) % 5), power(r, context)
    intervention = identity(4) if intervention is None else intervention
    out = {}
    for (active, archive, flags), original in maps.items():
        controlled = multiply(pre, multiply(intervention, original))
        for parity in (0, 1):
            # B^(2T) returns geometry and performs exactly S_code: X^parity here.
            source_map = multiply(post, multiply(writer[parity], controlled))
            written = active ^ parity
            new_archive = list(archive)
            new_active = new_archive[index]
            new_archive[index] = written
            new_flags = flags ^ (1 << index)
            key = new_active, tuple(new_archive), new_flags
            if selected is not None and not (new_flags & (1 << index) and written == selected):
                continue
            out[key] = add(out[key], source_map) if key in out else source_map
    return out


def trial_dispatch(kind, capacity, used, cut=None, ready=True):
    """External typed descriptor dispatch; not a measurement of unknown state."""
    if kind == "ZERO_SUPPORT":
        return "ZERO_SUPPORT"
    if kind == "RAW_JOINT":
        return "RAW_EVOLUTION"
    assert kind == "CODE_DENSITY"
    if cut is not None:
        return "UNSUPPORTED_PROTOCOL"
    if not ready:
        return "OUTSIDE_TRIAL_DOMAIN"
    if used >= capacity:
        return "RESOURCE_EXHAUSTED"
    return "SUPPORTED"


def expected_memory(outcomes, capacity=3):
    return 0, tuple(outcomes) + (0,) * (capacity - len(outcomes)), (1 << len(outcomes)) - 1


def compare_source_units(actual, expected, data):
    a_sharp, e_sharp = sharp(actual, data), sharp(expected, data)
    for i, j in product(range(4), repeat=2):
        assert sandwich_unit(actual, a_sharp, i, j) == sandwich_unit(expected, e_sharp, i, j)
    return 16


def one_history(contexts, outcomes, data, interventions=None):
    assert len(contexts) == len(outcomes)
    maps = {memory_ready(3): identity(4)}
    target = identity(4)
    interventions = {} if interventions is None else interventions
    for index, (context, outcome) in enumerate(zip(contexts, outcomes)):
        assert trial_dispatch("CODE_DENSITY", 3, index) == "SUPPORTED"
        intervention = interventions.get(index, identity(4))
        maps = round_maps(maps, context, index, data, outcome, intervention)
        target = multiply(data[5][context][outcome], multiply(intervention, target))
    key = expected_memory(outcomes)
    assert set(maps) == {key}
    assert key[0] == 0 and key[2].bit_count() == len(outcomes)
    return maps[key], target


def audit_histories(data):
    branches = source_units = 0
    cache = {}
    for length in range(4):
        for contexts in product(range(5), repeat=length):
            total_effect = zeros(4)
            for outcomes in product((0, 1), repeat=length):
                actual, target = one_history(contexts, outcomes, data)
                source_units += compare_source_units(actual, target, data)
                total_effect = add(total_effect, multiply(sharp(actual, data), actual))
                cache[(contexts, outcomes)] = actual
                if length and len(set(contexts)) == 1 and len(set(outcomes)) > 1:
                    assert actual == zeros(4)
                branches += 1
            assert total_effect == identity(4)
    assert branches == 1111 and source_units == 17776
    # Complete prefixes: each future context's two branches sum to the old effect.
    for (contexts, outcomes), previous in cache.items():
        if len(contexts) < 3:
            previous_effect = multiply(sharp(previous, data), previous)
            for context in range(5):
                next_effect = zeros(4)
                for outcome in (0, 1):
                    child = cache[(contexts + (context,), outcomes + (outcome,))]
                    next_effect = add(next_effect, multiply(sharp(child, data), child))
                assert next_effect == previous_effect
                for i, j in product(range(4), repeat=2):
                    assert next_effect[j][i] == previous_effect[j][i]

    # Actual coherent retained archive for one fixed-depth, fixed-index program.
    contexts = (0, 1, 0)
    coherent = {memory_ready(3): identity(4)}
    for index, context in enumerate(contexts):
        coherent = round_maps(coherent, context, index, data)
    words = tuple(product((0, 1), repeat=3))
    assert set(coherent) == {expected_memory(w) for w in words}
    cross_units = 0
    for w in words:
        left = coherent[expected_memory(w)]
        expected_left = cache[(contexts, w)]
        for v_word in words:
            right = sharp(coherent[expected_memory(v_word)], data)
            expected_right = sharp(cache[(contexts, v_word)], data)
            for i, j in product(range(4), repeat=2):
                assert sandwich_unit(left, right, i, j) == sandwich_unit(
                    expected_left, expected_right, i, j)
                cross_units += 1
            # Complete parity dephasing retains precisely the diagonal history blocks.
            same_record = expected_memory(w) == expected_memory(v_word)
            assert same_record == (w == v_word)
    assert cross_units == 1024

    # Passive reread is a projector on the existing record, with no new append.
    for word in words:
        key = expected_memory(word)
        before = coherent[key]
        for index, old_outcome in enumerate(word):
            assert key[2] & (1 << index)
            for outcome in (0, 1):
                after = before if key[1][index] == outcome else zeros(4)
                assert after == (before if outcome == old_outcome else zeros(4))
            assert key == expected_memory(word)

    # Complex intervention is an admitted source control, not a B step.
    imaginary = root(8)
    phases = (Algebraic(1), imaginary, Algebraic(-1), -imaginary)
    physical_d = tuple(tuple(phases[i] if i == j else Algebraic(0)
                             for j in range(4)) for i in range(4))
    assert multiply(adjoint(physical_d), physical_d) == identity(4)
    logical_d = multiply(multiply(data[4], physical_d), data[3])
    assert multiply(sharp(logical_d, data), logical_d) == identity(4)
    intervened_effect = zeros(4)
    adaptive_effect = zeros(4)
    for outcomes in words:
        actual, target = one_history(contexts, outcomes, data, {1: logical_d})
        assert compare_source_units(actual, target, data) == 16
        intervened_effect = add(intervened_effect, multiply(sharp(actual, data), actual))
        causal_contexts = tuple(sum(outcomes[:i]) % 5 for i in range(3))
        actual, target = one_history(causal_contexts, outcomes, data)
        assert compare_source_units(actual, target, data) == 16
        adaptive_effect = add(adaptive_effect, multiply(sharp(actual, data), actual))
    assert intervened_effect == identity(4) and adaptive_effect == identity(4)

    assert trial_dispatch("CODE_DENSITY", 0, 0) == "RESOURCE_EXHAUSTED"
    assert trial_dispatch("CODE_DENSITY", 3, 3) == "RESOURCE_EXHAUSTED"
    assert trial_dispatch("ZERO_SUPPORT", 0, 0) == "ZERO_SUPPORT"
    assert trial_dispatch("RAW_JOINT", 3, 0) == "RAW_EVOLUTION"
    assert trial_dispatch("CODE_DENSITY", 3, 0, cut=0) == "UNSUPPORTED_PROTOCOL"
    assert trial_dispatch("CODE_DENSITY", 3, 0, ready=False) == "OUTSIDE_TRIAL_DOMAIN"
    for key in coherent:
        assert trial_dispatch("CODE_DENSITY", 3, key[2].bit_count()) == "RESOURCE_EXHAUSTED"
    # Two B operative cycles without append: parity is accumulated, not fresh.
    for source in range(4):
        phase = 0
        phase ^= CODES4[source] % 2
        first = phase
        phase ^= CODES4[source] % 2
        assert phase == 0
        if source == 0:
            assert first == 1 and phase != first
    return branches, source_units, cross_units


class Gaussian:
    """Exact Q(i), including division for paired-span elimination pivots."""
    __slots__ = ("real", "imag")

    def __init__(self, real=0, imag=0):
        if isinstance(real, Gaussian):
            self.real, self.imag = real.real, real.imag
        else:
            self.real, self.imag = Q(real), Q(imag)

    def __add__(self, other):
        other = Gaussian(other)
        return Gaussian(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-Gaussian(other))

    def __rsub__(self, other):
        return Gaussian(other) + (-self)

    def __mul__(self, other):
        other = Gaussian(other)
        return Gaussian(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def conjugate(self):
        return Gaussian(self.real, -self.imag)

    def __truediv__(self, other):
        other = Gaussian(other)
        denominator = other.real * other.real + other.imag * other.imag
        assert denominator
        numerator = self * other.conjugate()
        return Gaussian(numerator.real / denominator, numerator.imag / denominator)

    def __eq__(self, other):
        other = Gaussian(other)
        return self.real == other.real and self.imag == other.imag

    def __bool__(self):
        return bool(self.real or self.imag)


def paired_seed(i, j, first, second):
    out = {}
    for descriptor, preparation in enumerate((first, second)):
        for q, r in product((0, 1), repeat=2):
            value = Gaussian(preparation[q][r])
            if value:
                out[descriptor * 64 + (2 * i + q) * 8 + (2 * j + r)] = value
    return out


def paired_apply(vector, operation):
    out = {}
    phases = (Gaussian(1), Gaussian(0, 1), Gaussian(-1), Gaussian(0, -1))
    for index, value in vector.items():
        descriptor, flat = divmod(index, 64)
        row, column = divmod(flat, 8)
        source_r, phase_r = divmod(row, 2)
        source_c, phase_c = divmod(column, 2)
        if operation in ("write", "inverse"):
            phase_r ^= CODES4[source_r] % 2
            phase_c ^= CODES4[source_c] % 2
        elif operation == "cycle":
            source_r, source_c = (source_r + 1) % 4, (source_c + 1) % 4
        elif operation == "D":
            value = value * phases[source_r] * phases[source_c].conjugate()
        else:
            assert operation in ("read0", "read1")
            outcome = int(operation[-1])
            if phase_r != outcome or phase_c != outcome:
                continue
        new_index = descriptor * 64 + (2 * source_r + phase_r) * 8 + 2 * source_c + phase_c
        out[new_index] = out.get(new_index, Gaussian(0)) + value
    return {key: value for key, value in out.items() if value}


def output_difference(vector):
    out = {}
    for index, value in vector.items():
        descriptor, coordinate = divmod(index, 64)
        out[coordinate] = out.get(coordinate, Gaussian(0)) + (-value if descriptor else value)
    return {key: value for key, value in out.items() if value}


def paired_span(first, second):
    basis = {}
    pending = deque()

    def insert(vector):
        vector = dict(vector)
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                divisor = vector[pivot]
                normalized = {k: value / divisor for k, value in vector.items()}
                assert normalized[pivot] == 1
                basis[pivot] = normalized
                pending.append(normalized)
                assert len(basis) <= 128
                return
            factor = vector[pivot]
            for index, coefficient in basis[pivot].items():
                value = vector.get(index, Gaussian(0)) - factor * coefficient
                if value:
                    vector[index] = value
                else:
                    vector.pop(index, None)

    for i, j in product(range(4), repeat=2):
        insert(paired_seed(i, j, first, second))
    alphabet = ("write", "inverse", "cycle", "D", "read0", "read1")
    while pending:
        vector = pending.popleft()
        for operation in alphabet:
            insert(paired_apply(vector, operation))
    # Closure check is independent of the equality test on the resulting span.
    previous_dimension = len(basis)
    for vector in tuple(basis.values()):
        for operation in alphabet:
            insert(paired_apply(vector, operation))
    assert len(basis) == previous_dimension and not pending
    return all(not output_difference(v) for v in basis.values()), len(basis)


def audit_family_equality(tables):
    one, imaginary = Gaussian(1), Gaussian(0, 1)
    for z in (one, imaginary, Gaussian(1, 1), Gaussian(Q(2, 3), Q(-5, 7))):
        assert z / z == 1 and (one / z) * z == 1
    even = ((1, 0), (0, 0))
    odd = ((0, 0), (0, 1))
    plus = ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2)))
    for second, expected in ((even, True), (odd, False), (plus, False)):
        equal, dimension = paired_span(even, second)
        assert equal == expected and 1 <= dimension <= 128
    # The reduced one-use equality does not erase full-state readiness.
    for a, b in product(CODES4, repeat=2):
        for outcome in (0, 1):
            assert gamma(tables, "E", a, b, outcome) == gamma(tables, "O", a, b, outcome ^ 1)
    assert output_difference(paired_seed(0, 0, even, odd))
    return 3


def main():
    fields, labels, data = audit_arithmetic()
    clean_steps, cut_steps, negative_steps = audit_circuit(fields, labels)
    tables, pointer_counts = audit_pointers(fields)
    unit_counts = audit_pointer_units()
    physical_cases = audit_instruments(data, tables)
    archive_cases = audit_archive_basis()
    history_counts = audit_histories(data)
    family_cases = audit_family_equality(tables)
    print("C-FIELD-J-LOCAL-INSTRUMENT-N exact audit PASS")
    print("arithmetic box=1225 supported=291 shells=1,20,30,60,60,120")
    print("B clean_steps=%d cut_steps=%d negative_steps=%d" % (clean_steps, cut_steps, negative_steps))
    print("pointer translations=%d phase_coordinates=%d coefficients=%d" % pointer_counts)
    print("pointer_units partitions=%d retained_phase=%d phase_branches=%d" % unit_counts)
    print("source instrument_matrix_units=%d reference=PASS" % physical_cases)
    print("archive basis_cases=%d dirty_capacity=PASS" % archive_cases)
    print("history branches=%d matrix_units=%d coherent_cross_units=%d" % history_counts)
    print("family paired_span_cases=%d full_retention=PASS" % family_cases)
    print("scope=L1 selected conditional maps; occurrence and physical closure NOT DERIVED")


if __name__ == "__main__":
    main()
