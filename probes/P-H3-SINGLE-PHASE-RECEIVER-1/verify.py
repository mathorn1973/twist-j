# SPDX-License-Identifier: Apache-2.0
"""Exact, non-Canonical test of a single H3 phase predicate and receiver."""

from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import product
import json
from struct import Struct
import sys


# Public native kernel and four-row seed from C-H3-RECURRENT-PHASE-WORKER-N.

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
FUND = constant(1025)


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


HEIGHT = 4
PERIOD = 622
LAPS = 5
TARGET_RANK = 44
CONTROL_RANK = 4
TARGET_TICK = 74
READER = 4
PASSIVE = 5
A = (3, 4, 5, 5, 0)
DEFECT = scale(-1, multiply(FUND, RHO))
READER_CLK = add(A, scale(2, FUND))
EXPECTED_ACCOUNTS = ((8, 0, 0, 0), (2066, 6, 7, 5),
                     (10498377, 0, 2089051, 2089051), 18907703)
BARE_ACCOUNTS = ((0, 0, 0, 0), (18, 6, 8, 10),
                 (270, 0, 94, 94), 446)
CUT = Struct(">640q")


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


def funded_matter(center, difference):
    return add(center, difference), subtract(center, difference)


def expected_stock(transfers, transient=False):
    shift = scale(2, power(transfers))
    reader_center = subtract(constant(2), shift)
    passive_center = add(constant(2), shift)
    reader_gap = FUND if transient else multiply(J, FUND)
    reader_clk = subtract(READER_CLK, DEFECT) if transient else READER_CLK
    return ((*funded_matter(reader_center, reader_gap), reader_clk),
            (*funded_matter(passive_center, FUND), ZERO))


def prepare(field):
    decorated = list(field)
    for site, stock in zip((READER, PASSIVE), expected_stock(0)):
        decorated[site] = (*stock, field[site][3])
    return tuple(decorated)


def projection(field, bare, defect=ZERO):
    """Replace just the prepared rails and subtract the declared transient."""
    projected = list(field)
    for site, delta in ((READER, defect), (PASSIVE, ZERO)):
        projected[site] = (*bare[site][:3], subtract(field[site][3], delta))
    return tuple(projected)


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
    findings.equality(len(set(ready)), 85, "bare_ready_fixtures", [])
    ranks = {field: rank for rank, field in enumerate(ready)}
    cuts, transported, arrival = [ready[0]], [], {}
    for tick in range(PERIOD):
        field = cuts[-1]
        if tick % 2 == 0 and field in ranks:
            rank = ranks[field]
            findings.require(rank not in arrival, "bare_duplicate_ready", [rank, tick])
            arrival.setdefault(rank, tick)
        post_transport, complete = native_step(field, tick % 2)
        transported.append(post_transport)
        cuts.append(complete)
        trace_cut(digest, post_transport)
        trace_cut(digest, complete)
        findings.field_equality(inverse_step(complete, tick % 2), field,
                                "bare_inverse", [tick])
        findings.equality(reported_account(post_transport), BARE_ACCOUNTS,
                          "bare_accounts", [tick, "transport"])
        findings.equality(reported_account(complete), BARE_ACCOUNTS,
                          "bare_accounts", [tick, "complete"])
        if (tick + 1) % 2 == 0:
            findings.equality(complete == ready[0], tick + 1 == PERIOD,
                              "bare_period", [tick + 1])
    findings.equality(len(arrival), 85, "bare_ready_count", [])
    findings.equality(arrival.get(TARGET_RANK), TARGET_TICK, "bare_target_tick", [])
    findings.equality(j_coefficients(A), (-2, 0, -1, -5), "target_value", [])
    hits = [tick + 1 for tick, field in enumerate(transported) if field[READER][3] == A]
    findings.equality(hits, [74, 75], "bare_target_contacts", [])
    return cuts, transported, arrival


def check_complete(findings, field, bare, transfers, transient, witness):
    delta = DEFECT if transient else ZERO
    findings.field_equality(projection(field, bare, delta), bare, "projection", witness)
    actual = field[READER][:3], field[PASSIVE][:3]
    findings.equality(actual, expected_stock(transfers, transient), "complete_stock", witness)
    findings.equality(reported_account(field), EXPECTED_ACCOUNTS, "accounts", witness)


def check_step(findings, digest, field, bit, bare_transport, bare_complete,
               transfers, transient, wire_defect, witness):
    post_transport, complete = native_step(field, bit)
    _, forward_tags = scatter_field(post_transport)
    recovered_post, inverse_tags = scatter_field(complete)
    findings.field_equality(recovered_post, post_transport, "collision_inverse", witness)
    findings.equality(inverse_tags, tuple(3-tag if tag else 0 for tag in forward_tags),
                      "inverse_branches", witness)
    expected_tag = 2 if transient else (1 if wire_defect != ZERO else 0)
    findings.equality((forward_tags[READER], forward_tags[PASSIVE]), (expected_tag, 0),
                      "read_and_reset_branches", witness)
    findings.equality(complete[PASSIVE][:2], post_transport[PASSIVE][:2],
                      "passive_collision_retains_transport", witness)
    trace_cut(digest, post_transport)
    trace_cut(digest, complete)
    findings.field_equality(projection(post_transport, bare_transport, wire_defect),
                            bare_transport, "transport_projection", witness)
    actual = post_transport[READER][:3], post_transport[PASSIVE][:3]
    findings.equality(actual, expected_stock(transfers, wire_defect != ZERO),
                      "transport_stock", witness)
    findings.equality(reported_account(post_transport), EXPECTED_ACCOUNTS,
                      "accounts", [*witness, "transport"])
    findings.field_equality(inverse_step(complete, bit), field, "inverse", witness)
    check_complete(findings, complete, bare_complete, transfers, transient, witness)
    return post_transport, complete


def controlled_trials(findings, digest, cuts, transported, arrival):
    writes = []
    tested = 0
    control = None
    for rank in range(85):
        if rank not in arrival:
            findings.require(False, "missing_trial", [rank])
            continue
        tested += 1
        selected = rank == TARGET_RANK
        incoming = (arrival[rank] - 1) % PERIOD
        outgoing = (incoming + 1) % PERIOD
        initial = prepare(cuts[incoming])
        trace_cut(digest, initial)
        check_complete(findings, initial, cuts[incoming], 0, False, ["trial", rank, 0])
        first_transport, first = check_step(
            findings, digest, initial, incoming % 2, transported[incoming],
            cuts[incoming + 1], 0, selected, ZERO, ["trial", rank, 1])
        _, second = check_step(
            findings, digest, first, outgoing % 2, transported[outgoing],
            cuts[outgoing + 1], int(selected), False, DEFECT if selected else ZERO,
            ["trial", rank, 2])
        finds_first_write = first[PASSIVE][:2] != initial[PASSIVE][:2]
        finds_second_write = second[PASSIVE][:2] != first[PASSIVE][:2]
        if finds_second_write:
            writes.append(rank)
        findings.equality(finds_first_write, False, "trial_early_passive_write", [rank])
        findings.equality(finds_second_write, selected, "trial_passive_write", [rank])
        if rank == CONTROL_RANK:
            candidate = first_transport[READER][3]
            r0, r2, clk, corr = first_transport[READER]
            matter_gap, field_gap = subtract(r0, r2), subtract(clk, corr)
            admitted = even(matter_gap) and even(field_gap)
            distinct = candidate != A
            findings.require(admitted and distinct and even(subtract(A, candidate)),
                             "same_residue_control", [j_coefficients(candidate)])
            control = {"candidate": j_coefficients(candidate), "parity_admits": admitted,
                       "different": distinct}
            if admitted:
                matter_norm, field_norm = norm(half(matter_gap)), norm(half(field_gap))
                branch1 = field_norm == multiply(THETA, matter_norm)
                branch2 = matter_norm == multiply(THETA, field_norm)
                control.update({"branch1_equality": branch1, "branch2_equality": branch2})
                findings.require(not branch1 and not branch2,
                                 "same_residue_resonance", [branch1, branch2])
            findings.require(first[READER] == first_transport[READER],
                             "same_residue_scatter", [first_transport[READER], first[READER]])
    return tested, writes, control


def recurrent_trial(findings, digest, cuts, transported):
    initial = prepare(cuts[0])
    field = initial
    trace_cut(digest, initial)
    check_complete(findings, initial, cuts[0], 0, False, ["recurrent", 0])
    writes = []
    local_changes = []
    returns = 0
    for tick in range(1, PERIOD * LAPS + 1):
        outgoing = (tick - 1) % PERIOD
        lap, phase = divmod(tick, PERIOD)
        write = phase == TARGET_TICK + 1
        prior_passive = field[PASSIVE][:2]
        _, field = check_step(
            findings, digest, field, outgoing % 2, transported[outgoing],
            cuts[outgoing + 1], lap + int(phase > TARGET_TICK), phase == TARGET_TICK,
            DEFECT if write else ZERO, ["recurrent", tick])
        changed = field[PASSIVE][:2] != prior_passive
        if changed:
            writes.append(tick)
            after_q = sum(trace_half(norm(z)) for z in field[PASSIVE][:2])
            before_q = sum(trace_half(norm(z)) for z in prior_passive)
            local_changes.append(after_q - before_q)
        findings.equality(changed, write, "recurrent_passive_write", [tick])
        returned = tick % 2 == 0 and field == initial
        returns += returned
        findings.equality(returned, tick == PERIOD * LAPS, "decorated_period", [tick])
    return writes, local_changes, returns


def main():
    if sys.flags.optimize:
        raise SystemExit("Run without optimization to retain all exact arithmetic checks.")
    sys.stdout.reconfigure(newline="\n")
    bare, trial, orbit = Findings(), Findings(), Findings()
    digest = sha256()
    digest.update(b"bare")
    cuts, transported, arrival = bare_reference(bare, digest)
    digest.update(b"controlled")
    tested, writes, control = controlled_trials(trial, digest, cuts, transported, arrival)
    digest.update(b"recurrent")
    recurrent_writes, local_changes, returns = recurrent_trial(orbit, digest, cuts, transported)
    groups = {"bare": bare, "controlled": trial, "recurrent": orbit}
    print(json.dumps({
        "accounts": reported_account(prepare(cuts[0])),
        "controlled_trials": tested,
        "controlled_write_ranks": writes,
        "decorated_returns": returns,
        "decorated_ticks": PERIOD * LAPS,
        "falsifiers": {group: {key: {"count": count, "first": finding.first[key]}
                                for key, count in finding.counts.items()}
                       for group, finding in groups.items()},
        "gates": {group: "FALSIFIED" if finding.counts else "PASS"
                  for group, finding in groups.items()},
        "recurrent_write_ticks": recurrent_writes,
        "passive_scalar_changes": local_changes,
        "same_residue_control": control,
        "status": "FALSIFIED" if any(finding.counts for finding in groups.values()) else "PASS",
        "trace_sha256": digest.hexdigest(),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
