# SPDX-License-Identifier: Apache-2.0
"""Exact, non-Canonical test of a two-phase H3 material readout."""

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
TARGET_TAGS = {4: 1, 44: 2}
TARGET_TICKS = {4: 190, 44: 74}
BARE_ACCOUNTS = ((0, 0, 0, 0), (18, 6, 8, 10), (270, 0, 94, 94), 446)
FUNDED_ACCOUNTS = ((-6, -3, 9, 0), (13, 6, 9, 7), (465, 0, 109, 109), 821)
CUT = Struct(">640q")


def from_j(a, b, c, d):
    # The internal basis is (1, rho, rho**2, rho**3, rho**4).
    return normalized((a, c, 0, b, d))


D = from_j(-2, -1, -2, 0)
HEAD_CLK = from_j(-6, 0, 1, -3)
PASSIVE_PAIR = (from_j(0, -3, 6, -3), from_j(-6, 0, 3, 3))
PASSIVE_CLK = ONE
GAPS = {4: multiply(J, D), 44: multiply(INV_J, D)}
DEFECTS = {4: from_j(-2, -1, -2, 0), 44: from_j(0, 1, 3, 1)}
READ_VALUES = {4: from_j(0, 0, 3, -1), 44: from_j(-2, 0, -1, -5)}
OUTPUTS = {4: (from_j(-6, -5, -2, -7), PASSIVE_PAIR[1]),
           44: (PASSIVE_PAIR[0], from_j(-2, -2, -5, -1))}
OUTPUT_LEVELS = {4: -20, 44: 0}
IDLE_LEVEL = -15
INITIAL_STOCK = ((D, scale(-1, D), HEAD_CLK), (*PASSIVE_PAIR, PASSIVE_CLK))


def stocks(field):
    return field[HEAD][:3], field[RECEIVER][:3]


def install_stocks(field, stock):
    prepared = list(field)
    for site, rails in zip((HEAD, RECEIVER), stock):
        prepared[site] = (*rails, field[site][3])
    return tuple(prepared)


def projection(field, bare, defect=ZERO):
    projected = list(install_stocks(field, stocks(bare)))
    projected[HEAD] = (*projected[HEAD][:3], subtract(projected[HEAD][3], defect))
    return tuple(projected)


def expected_stock(rank, stage):
    if rank not in TARGET_TAGS or stage == "initial" or stage == "read_transport":
        return INITIAL_STOCK
    prepared_gap = GAPS[rank]
    defect = DEFECTS[rank]
    if stage == "read_collision":
        return ((prepared_gap, scale(-1, prepared_gap), subtract(HEAD_CLK, defect)),
                INITIAL_STOCK[1])
    center = multiply(subtract(RHO, ONE), prepared_gap)
    if rank == 44:
        center = scale(-1, center)
    gap = multiply(RHO, prepared_gap if stage == "write_transport" else D)
    clk = subtract(HEAD_CLK, defect) if stage == "write_transport" else HEAD_CLK
    return ((add(center, gap), subtract(center, gap), clk),
            (*OUTPUTS[rank], PASSIVE_CLK))


def receiver_scalar(pair, baseline=0):
    total = add(*pair)
    twice = 5 * total[0] - sum(total) - 2 * baseline
    return twice // 2 if twice % 2 == 0 else f"{twice}/2"


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


def transition(findings, incoming, bit, tick_label):
    post = transport(incoming, HEIGHT, bit)
    complete, tags = scatter_field(post)
    recovered, inverse_tags = scatter_field(complete)
    findings.field_equality(recovered, post, "inverse_collision", tick_label)
    findings.equality(inverse_tags, tuple(3 - tag if tag else 0 for tag in tags),
                      "inverse_tags", tick_label)
    for stage, candidate in (("transport", post), ("collision", complete)):
        findings.equality(reported_account(candidate), FUNDED_ACCOUNTS,
                          "funded_accounts", [*tick_label, stage])
    next_bit = 1 - bit
    recovered_bit = 1 - next_bit
    findings.equality((transport(recovered, HEIGHT, recovered_bit, -1), recovered_bit)
                      == (incoming, bit), True, "inverse_full_state", tick_label)
    return post, complete, tags, next_bit


def check_controlled_cut(findings, digest, field, bare, rank, stage):
    trace_cut(digest, field)
    defect = DEFECTS.get(rank, ZERO) if stage in ("read_collision", "write_transport") else ZERO
    findings.field_equality(projection(field, bare, defect), bare,
                            "clock_projection", [rank, stage])
    findings.equality(stocks(field), expected_stock(rank, stage),
                      "charged_stock", [rank, stage])
    written = stage in ("write_transport", "write_collision")
    expected_level = OUTPUT_LEVELS.get(rank, IDLE_LEVEL) if written else IDLE_LEVEL
    findings.equality(receiver_scalar(field[RECEIVER][:2]), expected_level,
                      "receiver_scalar", [rank, stage])


def controlled_trials(findings, digest, cuts, transported, arrivals):
    output = {}
    write_ranks = []
    for rank in sorted(arrivals):
        raw_cut = arrivals[rank]
        incoming = (raw_cut - 1) % PERIOD
        field = install_stocks(cuts[incoming], INITIAL_STOCK)
        check_controlled_cut(findings, digest, field, cuts[incoming], rank, "initial")
        post, first, tags, write_bit = transition(findings, field, incoming % 2, [rank, 1])
        findings.equality(write_bit, raw_cut % 2, "ready_bit", [rank])
        first_tag = TARGET_TAGS.get(rank, 0)
        findings.equality((tags[HEAD], tags[RECEIVER]), (first_tag, 0),
                          "read_tags", [rank])
        check_controlled_cut(findings, digest, post, transported[incoming], rank, "read_transport")
        check_controlled_cut(findings, digest, first, cuts[raw_cut], rank, "read_collision")
        if rank in READ_VALUES:
            findings.equality(post[HEAD][3], READ_VALUES[rank], "selected_corr", [rank])

        post, second, tags, next_bit = transition(findings, first, write_bit, [rank, 2])
        reverse_tag = 3 - first_tag if first_tag else 0
        findings.equality((tags[HEAD], tags[RECEIVER]), (reverse_tag, 0),
                          "write_tags", [rank])
        check_controlled_cut(findings, digest, post, transported[raw_cut], rank, "write_transport")
        check_controlled_cut(findings, digest, second, cuts[raw_cut + 1], rank, "write_collision")
        findings.equality(next_bit, (raw_cut + 1) % 2, "next_bit", [rank])
        before, observed = first[RECEIVER][:2], second[RECEIVER][:2]
        changed_lanes = [lane for lane in range(2) if before[lane] != observed[lane]]
        findings.equality(changed_lanes, {4: [0], 44: [1]}.get(rank, []),
                          "receiver_changed_lanes", [rank])
        findings.equality(post[RECEIVER][:2], observed, "receiver_collision_quiet", [rank])
        if changed_lanes:
            write_ranks.append(rank)
            output[rank] = {
                "pair": [j_coefficients(x) for x in observed],
                "scalar": receiver_scalar(observed),
                "scalar_delta": receiver_scalar(observed, IDLE_LEVEL),
            }
    findings.equality(write_ranks, sorted(TARGET_TAGS), "write_ranks", [])
    findings.require(len(set((*OUTPUTS.values(), PASSIVE_PAIR))) == 3,
                     "distinct_prospective_pairs", [])
    return {"trials": len(arrivals), "write_ranks": write_ranks, "writes": output,
            "idle_pair": [j_coefficients(x) for x in PASSIVE_PAIR], "idle_scalar": IDLE_LEVEL}


def stream_trial(integrity, digest, cuts, transported):
    initial = install_stocks(cuts[0], INITIAL_STOCK)
    field, bit = initial, 0
    trace_cut(digest, field)
    counts = Counter()
    first = {}
    joint_returns = []
    passive_writes = []
    checkpoints = {}
    reads_at = {tick: rank for rank, tick in TARGET_TICKS.items()}
    writes_at = {tick + 1: rank for rank, tick in TARGET_TICKS.items()}
    expected_held_pair = PASSIVE_PAIR

    def record(name, tick, **details):
        counts[name] += 1
        first.setdefault(name, {"tick": tick, **details})

    def compare_clock(name, actual, expected, tick):
        if actual == expected:
            counts[name + "_equal"] += 1
        else:
            site = next(index for index, pair in enumerate(zip(actual, expected))
                        if pair[0] != pair[1])
            record(name + "_departure", tick, site=site,
                   actual=[j_coefficients(value) for value in actual[site]],
                   expected=[j_coefficients(value) for value in expected[site]])

    for tick in range(1, STREAM_TICKS + 1):
        part = (tick - 1) % PERIOD
        phase = tick % PERIOD
        read_rank, write_rank = reads_at.get(phase), writes_at.get(phase)
        old_passive = field[RECEIVER][:2]
        post, field, tags, bit = transition(integrity, field, bit, [tick])
        integrity.equality(bit, tick % 2, "clock_bit", [tick])
        trace_cut(digest, post)
        trace_cut(digest, field)
        bare_post, bare_complete = transported[part], cuts[part + 1]
        compare_clock("clock_transport", projection(post, bare_post), bare_post, tick)
        compare_clock("clock_collision", projection(field, bare_complete), bare_complete, tick)
        if phase % 2 == 0:
            compare_clock("clock_at_even_cut", projection(field, bare_complete), bare_complete, tick)
        compare_clock("clock_transport_with_expected_defect",
                      projection(post, bare_post, DEFECTS.get(write_rank, ZERO)), bare_post, tick)
        compare_clock("clock_collision_with_expected_defect",
                      projection(field, bare_complete, DEFECTS.get(read_rank, ZERO)),
                      bare_complete, tick)
        if write_rank is not None:
            compare_clock("clock_at_write_cut", projection(field, bare_complete), bare_complete, tick)
            expected = expected_stock(write_rank, "write_collision")
            if stocks(field) == expected:
                counts["charged_stock_at_write_cut_equal"] += 1
            else:
                record("charged_stock_at_write_cut_departure", tick, rank=write_rank,
                       actual=[[j_coefficients(x) for x in cell] for cell in stocks(field)],
                       expected=[[j_coefficients(x) for x in cell] for cell in expected])
            expected_held_pair = OUTPUTS[write_rank]
        desired_tag = TARGET_TAGS[read_rank] if read_rank is not None else (
            3 - TARGET_TAGS[write_rank] if write_rank is not None else 0)
        if (tags[HEAD], tags[RECEIVER]) != (desired_tag, 0):
            record("stock_tag_departure", tick, actual=[tags[HEAD], tags[RECEIVER]],
                   expected=[desired_tag, 0])
        transported_pair = post[RECEIVER][:2]
        current = field[RECEIVER][:2]
        transported_lanes = [i for i in range(2) if old_passive[i] != transported_pair[i]]
        desired_lanes = {4: [0], 44: [1]}.get(write_rank, [])
        if transported_lanes != desired_lanes:
            record("passive_transport_lane_departure", tick,
                   actual=transported_lanes, expected=desired_lanes)
        if current != transported_pair:
            record("passive_collision_departure", tick,
                   actual=[j_coefficients(x) for x in current])
        if current != old_passive:
            passive_writes.append(tick)
            record("passive_write", tick, pair=[j_coefficients(x) for x in current],
                   scalar=receiver_scalar(current))
        if current != expected_held_pair:
            record("held_pair_departure", tick, actual=[j_coefficients(x) for x in current],
                   expected=[j_coefficients(x) for x in expected_held_pair])
        if phase == 0:
            checkpoints[tick] = {
                "clock": projection(field, bare_complete) == bare_complete,
                "charged_stock": stocks(field) == INITIAL_STOCK,
                "full_field_and_bit": field == initial and bit == 0,
            }
        if field == initial and bit == 0:
            joint_returns.append(tick)
    restoration_failures = (
        "clock_transport_with_expected_defect_departure",
        "clock_collision_with_expected_defect_departure",
        "charged_stock_at_write_cut_departure",
        "stock_tag_departure",
        "passive_transport_lane_departure",
        "passive_collision_departure",
        "held_pair_departure",
    )
    return {"ticks": STREAM_TICKS, "counts": dict(counts), "first": first,
            "phase_zero_checkpoints": checkpoints, "joint_return_ticks": joint_returns,
            "passive_write_ticks": passive_writes,
            "restoration": "COUNTEREXAMPLE" if any(counts[k] for k in restoration_failures)
            else "HOLDS_ON_TESTED_HORIZON",
            "joint_return_at_horizon": STREAM_TICKS in joint_returns,
            "continuous_gate": "PASS" if (
                STREAM_TICKS in joint_returns and not any(counts[k] for k in restoration_failures)
            ) else "FALSIFIED"}


def main():
    if sys.flags.optimize:
        raise SystemExit("Run without optimization to retain all exact arithmetic checks.")
    sys.stdout.reconfigure(newline="\n")
    bare, controlled, stream_integrity = Findings(), Findings(), Findings()
    digest = sha256(b"bare")
    cuts, transported, arrivals = bare_reference(bare, digest)
    digest.update(b"controlled")
    trials = controlled_trials(controlled, digest, cuts, transported, arrivals)
    digest.update(b"stream")
    stream = stream_trial(stream_integrity, digest, cuts, transported)
    groups = {"bare": bare, "controlled": controlled, "stream_integrity": stream_integrity}
    gates = {name: "FALSIFIED" if group.counts else "PASS" for name, group in groups.items()}
    gates["continuous_addressing"] = stream["continuous_gate"]
    print(json.dumps({
        "accounts": FUNDED_ACCOUNTS,
        "controlled": trials,
        "falsifiers": {name: {key: {"count": count, "first": findings.first[key]}
                              for key, count in findings.counts.items()}
                       for name, findings in groups.items()},
        "gates": gates,
        "status": "PASS" if all(gate == "PASS" for gate in gates.values()) else "FALSIFIED",
        "stream": stream,
        "trace_sha256": digest.hexdigest(),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()