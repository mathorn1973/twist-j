# SPDX-License-Identifier: Apache-2.0
"""Exact, non-Canonical test of a same-rail H3 write and hold."""

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
TARGET_TICKS = {44: 74, 4: 190}
TARGET_TAGS = {44: 1, 4: 1}
BARE_ACCOUNTS = ((0, 0, 0, 0), (18, 6, 8, 10), (270, 0, 94, 94), 446)
FUNDED_ACCOUNTS = ((3, 9, 3, 0), (15, 0, 5, 5), (365, 0, 24, 24), 706)
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


D = from_j(-1, 0, 3, 3)
G = multiply(J, D)
HEAD_CLK = from_j(-4, -6, -3, -5)
DEFECTS = {44: from_j(0, 6, 8, 6), 4: from_j(-2, 0, 6, 6)}
EXPECTED_WORDS = (
    (3, 9, 3, 0),
    (-1, 1, 1, 4),
    (5, 3, -1, -2),
    (1, 5, 7, 2),
    (-3, -3, -5, -4),
)
EXPECTED_LEVELS = (0, -5, 10, -5, 0)
READ_BY_TICK = {tick: rank for rank, tick in TARGET_TICKS.items()}
WRITE_BY_TICK = {tick + 1: rank for rank, tick in TARGET_TICKS.items()}


def expected_cut(bare, writes, active_rank):
    rotation = power(writes)
    midpoint = multiply(subtract(rotation, ONE), G)
    gap = multiply(rotation, D)
    defect = DEFECTS.get(active_rank, ZERO)
    if active_rank is not None:
        gap = multiply(J, gap)
    receiver_word = scale(-1, add(G, scale(2, multiply(rotation, G))))
    expected = list(bare)
    expected[HEAD] = (add(midpoint, gap), subtract(midpoint, gap),
                      add(HEAD_CLK, defect), subtract(bare[HEAD][3], defect))
    expected[RECEIVER] = (receiver_word, ZERO, ONE, bare[RECEIVER][3])
    return tuple(expected)


def expected_tags(bare_transport, head_tag):
    tags = list(scatter_field(bare_transport)[1])
    tags[HEAD], tags[RECEIVER] = head_tag, 0
    return tuple(tags)


def check_tick(findings, digest, incoming, bit, bare_transport, bare_complete,
               writes, read_rank, write_rank, label):
    post, complete, tags, next_bit = transition(findings, incoming, bit, label)
    trace_cut(digest, post)
    trace_cut(digest, complete)
    findings.field_equality(post, expected_cut(bare_transport, writes, write_rank),
                            "transport_state", label)
    findings.field_equality(complete, expected_cut(bare_complete, writes, read_rank),
                            "collision_state", label)
    head_tag = 1 if read_rank is not None else 2 if write_rank is not None else 0
    findings.equality(tags, expected_tags(bare_transport, head_tag), "collision_tags", label)
    findings.equality(next_bit, 1 - bit, "matching_bit", label)
    transported_lanes = [lane for lane in range(2)
                         if post[RECEIVER][lane] != incoming[RECEIVER][lane]]
    findings.equality(transported_lanes, [0] if write_rank is not None else [],
                      "receiver_transport_lanes", label)
    findings.equality(complete[RECEIVER][:2], post[RECEIVER][:2],
                      "receiver_passive_collision", label)
    return complete, next_bit, transported_lanes


def receiver_readout(word):
    trace = 5 * word[0] - sum(word)
    scalar = trace // 2 if trace % 2 == 0 else f"{trace}/2"
    return {"R0": j_coefficients(word), "half_trace": scalar}


def fresh_trials(findings, digest, cuts, transported, arrivals):
    writes = {}
    null_words = set()
    for rank, clock_cut in sorted(arrivals.items()):
        prior = (clock_cut - 1) % PERIOD
        initial = expected_cut(cuts[prior], 0, None)
        trace_cut(digest, initial)
        target = rank if rank in TARGET_TICKS else None
        first, bit, _ = check_tick(
            findings, digest, initial, prior % 2, transported[prior], cuts[prior + 1],
            0, target, None, [rank, 1]
        )
        findings.equality(bit, 0, "fresh_ready_bit", [rank])
        final, bit, movement = check_tick(
            findings, digest, first, bit, transported[clock_cut], cuts[clock_cut + 1],
            int(target is not None), None, target, [rank, 2]
        )
        word = final[RECEIVER][0]
        if movement:
            writes[rank] = word
        elif target is None:
            null_words.add(word)
    findings.equality(sorted(writes), sorted(TARGET_TICKS), "fresh_write_ranks", [])
    findings.equality(sorted(map(j_coefficients, null_words)), [EXPECTED_WORDS[0]],
                      "fresh_null_words", [])
    for rank, word in writes.items():
        findings.equality(receiver_readout(word),
                          {"R0": EXPECTED_WORDS[1], "half_trace": EXPECTED_LEVELS[1]},
                          "fresh_target_word", [rank])
    return writes, null_words


def stream_trial(findings, digest, cuts, transported):
    initial = expected_cut(cuts[0], 0, None)
    field, bit = initial, 0
    trace_cut(digest, field)
    seen = {(field, bit)}
    repeats, writes, reads = [], [], []
    write_count = 0
    for tick in range(1, STREAM_TICKS + 1):
        prior = (tick - 1) % PERIOD
        phase = tick % PERIOD
        read_rank, write_rank = READ_BY_TICK.get(phase), WRITE_BY_TICK.get(phase)
        write_count += int(write_rank is not None)
        field, bit, movement = check_tick(
            findings, digest, field, bit, transported[prior], cuts[prior + 1],
            write_count, read_rank, write_rank, [tick]
        )
        if read_rank is not None:
            reads.append([tick, read_rank, receiver_readout(field[RECEIVER][0])])
        if movement:
            word = field[RECEIVER][0]
            writes.append((tick, write_rank, word))
            word_index = write_count % len(EXPECTED_WORDS)
            findings.equality(receiver_readout(word),
                              {"R0": EXPECTED_WORDS[word_index],
                               "half_trace": EXPECTED_LEVELS[word_index]},
                              "stream_write_word", [tick])
        state = field, bit
        if state in seen:
            repeats.append(tick)
        seen.add(state)
    expected_schedule = sorted((base + tick, rank)
                               for base in range(0, STREAM_TICKS, PERIOD)
                               for tick, rank in WRITE_BY_TICK.items())
    findings.equality([(tick, rank) for tick, rank, _ in writes], expected_schedule,
                      "stream_write_schedule", [])
    return writes, reads, repeats, (field, bit) == (initial, 0)


def main():
    if sys.flags.optimize:
        raise SystemExit("Run without optimization to retain all exact arithmetic checks.")
    sys.stdout.reconfigure(newline="\n")
    bare, fresh, stream, renewal = (Findings() for _ in range(4))
    digest = sha256(b"same-rail-hold-1/bare")
    cuts, transported, arrivals = bare_reference(bare, digest)
    digest.update(b"/fresh")
    fresh_writes, null_words = fresh_trials(fresh, digest, cuts, transported, arrivals)
    digest.update(b"/stream")
    writes, reads, repeats, returned = stream_trial(stream, digest, cuts, transported)
    renewal.equality(repeats, [STREAM_TICKS], "first_recurrence", [])
    renewal.equality(returned, True, "full_field_and_bit_return", [])
    first = [(tick, rank, j_coefficients(word)) for tick, rank, word in writes[:2]]
    stream.equality(first, [(75, 44, EXPECTED_WORDS[1]), (191, 4, EXPECTED_WORDS[2])],
                    "first_44_to_4_transition", [])
    by_phase = {rank: {word for _, actual_rank, word in writes if actual_rank == rank}
                for rank in TARGET_TICKS}
    fresh_decodable = (fresh_writes.keys() == TARGET_TICKS.keys()
                       and fresh_writes[44] != fresh_writes[4])
    stream_decodable = (bool(by_phase[44]) and bool(by_phase[4])
                        and by_phase[44].isdisjoint(by_phase[4]))
    expected_positions = sorted(EXPECTED_WORDS)
    for rank, words in by_phase.items():
        stream.equality(sorted(map(j_coefficients, words)), expected_positions,
                        "phase_visits_all_five_receiver_words", [rank])
    findings = {"bare": bare, "fresh": fresh, "hold": stream, "renewal": renewal}
    gates = {name: "PASS" if not checks.counts else "FALSIFIED"
             for name, checks in findings.items()}
    gates["fresh_phase_only_decoder"] = "PASS" if fresh_decodable else "FALSIFIED"
    gates["stream_phase_only_decoder"] = "PASS" if stream_decodable else "FALSIFIED"
    print(json.dumps({
        "accounts": FUNDED_ACCOUNTS,
        "fresh": {"trials": len(arrivals),
                  "null": [receiver_readout(word) for word in sorted(null_words)],
                  "writes": {rank: receiver_readout(word) for rank, word in fresh_writes.items()}},
        "stream": {"ticks": STREAM_TICKS,
                   "reads": reads,
                   "writes": [[tick, rank, receiver_readout(word)] for tick, rank, word in writes],
                   "words_by_phase": {rank: sorted(map(j_coefficients, words))
                                      for rank, words in by_phase.items()},
                   "shared_ring_words": sorted(map(j_coefficients, by_phase[44] & by_phase[4])),
                   "first_recurrence": repeats[0] if repeats else None,
                   "full_field_and_bit_return": returned},
        "findings": {name: {"counts": dict(checks.counts), "first": checks.first}
                     for name, checks in findings.items() if checks.counts},
        "gates": gates,
        "trace_sha256": digest.hexdigest(),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
