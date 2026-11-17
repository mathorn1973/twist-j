# SPDX-License-Identifier: Apache-2.0
"""Native arithmetic and reference helpers extracted from P-H3-CLK-TO-RAIL-1."""

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from functools import cache
from itertools import product
from struct import Struct


# Native arithmetic, transport, collision and bare reference from P-H3-SAME-RAIL-HOLD-2.

def normalized(coefficients):
    return tuple(value - coefficients[-1] for value in coefficients)


def constant(n):
    return n, 0, 0, 0, 0


def add(*values):
    return tuple(map(sum, zip(*values)))


def scale(n, value):
    return tuple(n * term for term in value)


def subtract(a, b):
    return add(a, scale(-1, b))


def power(k):
    return normalized(tuple(int(i == k % 5) for i in range(5)))


@cache
def multiply(a, b):
    return normalized(tuple(sum(a[i] * b[(k - i) % 5] for i in range(5))
                            for k in range(5)))


@cache
def norm(a):
    return multiply(a, normalized((a[0], *reversed(a[1:]))))


def trace_half(a):
    twice = 5 * a[0] - sum(a)
    assert twice % 2 == 0
    return twice // 2


def even(a):
    return all(value % 2 == 0 for value in a)


def half(a):
    assert even(a)
    return tuple(value // 2 for value in a)


ZERO, ONE = constant(0), constant(1)
RHO = power(1)
J = add(ONE, RHO)
INV_J = scale(-1, add(power(1), power(3)))
THETA = norm(J)


@cache
def contact(a, b, exponent=1):
    delta = subtract(a, b)
    if not even(delta):
        return a, b
    midpoint = half(add(a, b))
    difference = multiply(power(exponent), half(delta))
    return add(midpoint, difference), subtract(midpoint, difference)


@cache
def scatter(cell):
    r0, r2, clk, corr = cell
    matter_gap, field_gap = subtract(r0, r2), subtract(clk, corr)
    if not even(matter_gap) or not even(field_gap):
        return cell, 0
    d, f = half(matter_gap), half(field_gap)
    if d != ZERO and norm(f) == multiply(THETA, norm(d)):
        matter_unit, field_unit, tag = J, INV_J, 1
    elif f != ZERO and norm(d) == multiply(THETA, norm(f)):
        matter_unit, field_unit, tag = INV_J, J, 2
    else:
        return cell, 0
    d, f = multiply(matter_unit, d), multiply(field_unit, f)
    m, a = half(add(r0, r2)), half(add(clk, corr))
    return (add(m, d), subtract(m, d), add(a, f), subtract(a, f)), tag


def transport(field, height, bit, exponent=1):
    after = [list(cell) for cell in field]
    for x, y in product(range(8), range(bit, height, 2)):
        left, right = x * height + y, x * height + (y + 1) % height
        for lane in range(3):
            after[left][lane], after[right][lane] = contact(
                field[left][lane], field[right][lane], exponent
            )
    for x, y in product(range(bit, 8, 2), range(height)):
        left, right = x * height + y, ((x + 1) % 8) * height + y
        after[left][3], after[right][3] = contact(field[left][3], field[right][3], exponent)
    return tuple(map(tuple, after))


def scatter_field(field):
    outputs, tags = zip(*(scatter(cell) for cell in field))
    return outputs, tags


def account(field):
    matter = add(*(value for cell in field for value in cell[:2]))
    radiation = add(*(value for cell in field for value in cell[2:]))
    quadratic = add(*(norm(value) for cell in field for value in cell))
    return matter, radiation, quadratic, trace_half(quadratic)


def clock_ready_fields():
    d = add(constant(2), RHO, power(2))
    k = subtract(J, power(2))
    receiver_stock = subtract(k, scale(2, multiply(multiply(RHO, J), d)))
    paid = scale(2, J)
    triple = constant(-3), constant(-3), constant(5)
    fields = []
    for _ in range(85):
        field = [(ZERO,) * 4] * 32
        for y in range(4):
            field[y] = paid, scale(-1, paid), ONE, triple[0] if y < 2 else receiver_stock
        for x, y in product((1, 2), (0, 1)):
            field[4 * x + y] = ZERO, ZERO, ZERO, triple[x]
        fields.append(tuple(field))
        left, middle = contact(*triple[:2])
        middle, right = contact(middle, triple[2])
        triple = left, middle, right
    return tuple(fields)


HEIGHT, PERIOD, STREAM_TICKS = 4, 622, 3110
HEAD, RECEIVER = 4, 5
TARGET_TICKS = {44: 74, 4: 190}
TARGET_TAGS = {44: 1, 4: 1}
BARE_ACCOUNTS = ((0, 0, 0, 0), (18, 6, 8, 10), (270, 0, 94, 94), 446)
CUT = Struct(">640q")


def from_j(a, b, c, d):
    # The internal basis is (1, rho, rho**2, rho**3, rho**4).
    return normalized((a, c, 0, b, d))


def j_coefficients(value):
    c0, c1, c2, c3, c4 = value
    return c0 - c2, c3 - c2, c1 - c2, c4 - c2


def reported_account(field):
    matter, radiation, quadratic, scalar = account(field)
    return (j_coefficients(matter), j_coefficients(radiation),
            j_coefficients(quadratic), scalar)


def native_step(field, bit):
    after_transport = transport(field, HEIGHT, bit)
    return after_transport, scatter_field(after_transport)[0]


def inverse_step(field, bit):
    return transport(scatter_field(field)[0], HEIGHT, bit, -1)


def trace_cut(digest, field):
    digest.update(CUT.pack(*(value for cell in field for lane in cell for value in lane)))


class Findings:
    def __init__(self):
        self.counts = Counter()
        self.first = {}

    def require(self, predicate, name, witness):
        if not predicate:
            self.counts[name] += 1
            self.first.setdefault(name, witness)

    def equality(self, observed, expected, name, witness):
        if observed != expected:
            self.require(False, name, [*witness, observed, expected])

    def field_equality(self, observed, expected, name, witness):
        if observed != expected:
            for site, (actual, predicted) in enumerate(zip(observed, expected)):
                if actual != predicted:
                    self.require(False, name, [*witness, site, actual, predicted])
                    break


def bare_reference(findings, digest):
    ready = clock_ready_fields()
    ranks = {field: rank for rank, field in enumerate(ready)}
    findings.equality(len(ranks), 85, "unique_ready_fixtures", [])
    cuts, transported, arrivals = [ready[0]], [], {}
    seen = {(ready[0], 0)}
    for tick in range(PERIOD):
        bit = tick % 2
        field = cuts[-1]
        if bit == 0 and field in ranks:
            rank = ranks[field]
            findings.require(rank not in arrivals, "duplicate_ready", [rank, tick])
            arrivals.setdefault(rank, tick)
        post, complete = native_step(field, bit)
        transported.append(post)
        cuts.append(complete)
        for stage, candidate in (("transport", post), ("collision", complete)):
            trace_cut(digest, candidate)
            findings.equality(reported_account(candidate), BARE_ACCOUNTS,
                              "bare_accounts", [tick + 1, stage])
        findings.field_equality(inverse_step(complete, bit), field,
                                "bare_inverse", [tick + 1])
        state = complete, (tick + 1) % 2
        findings.equality(state in seen, tick + 1 == PERIOD, "bare_repeat", [tick + 1])
        seen.add(state)
    findings.field_equality(cuts[-1], cuts[0], "bare_return", [PERIOD])
    findings.equality(len(arrivals), 85, "ready_count", [])
    findings.equality({r: arrivals.get(r) for r in TARGET_TAGS}, TARGET_TICKS,
                      "selected_ready_ticks", [])
    return cuts, transported, arrivals



D = from_j(1, -1, -1, 1)
G = multiply(J, D)
HEAD_CLK = from_j(0, 2, -1, 1)
PASSIVE = RECEIVER
SUPPORT = PASSIVE + 1
R0, R2, CLK, CORR = range(4)
TARGETS = TARGET_TICKS
LAP = PERIOD
HORIZON = 5 * LAP


@dataclass(frozen=True)
class Preparation:
    name: str
    passive_clk: tuple
    support_clk: tuple | None = None

    def stock(self, bare):
        field = list(bare)
        field[HEAD] = (
            D, scale(-1, D), HEAD_CLK, bare[HEAD][CORR]
        )
        field[PASSIVE] = (
            scale(-3, G), scale(-1, G),
            self.passive_clk, bare[PASSIVE][CORR]
        )
        if self.support_clk is not None:
            field[SUPPORT] = (*bare[SUPPORT][:CLK], self.support_clk, bare[SUPPORT][CORR])
        return tuple(field)

    def stock_coordinates(self):
        coordinates = {(cell, lane) for cell in (HEAD, PASSIVE) for lane in (R0, R2, CLK)}
        if self.support_clk is not None:
            coordinates.add((SUPPORT, CLK))
        return coordinates


class Witnesses:
    def __init__(self):
        self.counts = Counter()
        self.first = {}

    def note(self, name, witness):
        self.counts[name] += 1
        self.first.setdefault(name, witness)

    def report(self):
        return {name: {"count": self.counts[name], "first": self.first[name]}
                for name in sorted(self.counts)}


def reported(value):
    return j_coefficients(value)


def mismatch(field, reference, coordinates):
    for cell, lane in coordinates:
        if field[cell][lane] != reference[cell][lane]:
            return [cell, lane, reported(field[cell][lane]), reported(reference[cell][lane])]
    return None



def transition(field, bit, expected_account, events, label, digest):
    after_c = transport(field, HEIGHT, bit)
    after_b, tags = scatter_field(after_c)
    reconstructed_c, inverse_tags = scatter_field(after_b)
    if reconstructed_c != after_c:
        events.note("inverse_B", label)
    if inverse_tags != tuple(3 - tag if tag else 0 for tag in tags):
        events.note("inverse_tags", label)
    next_bit = 1 - bit
    recovered_bit = 1 - next_bit
    if transport(reconstructed_c, HEIGHT, recovered_bit, -1) != field:
        events.note("inverse_C_and_input", label)
    for stage, cut, stage_bit in (("C", after_c, bit), ("B", after_b, next_bit)):
        if account(cut) != expected_account:
            events.note("ring_account", [*label, stage])
        digest.update(bytes((stage_bit,)))
        trace_cut(digest, cut)
    return after_c, after_b, tags, next_bit
