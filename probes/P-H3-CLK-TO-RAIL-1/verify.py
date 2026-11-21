# SPDX-License-Identifier: Apache-2.0
"""Exact prospective H3 CLK-to-rail probe with an unchanged native kernel."""

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from functools import cache
from itertools import product
import json
from struct import Struct
import sys


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
FUNDED_ACCOUNTS = ((-9, 0, -3, -3), (19, 8, 7, 11), (380, 0, 144, 144), 616)
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
DEFECTS = {44: from_j(-1, 1, 1, -1), 4: from_j(-2, -2, 0, -1)}
PASSIVE = RECEIVER
SUPPORT = PASSIVE + 1
R0, R2, CLK, CORR = range(4)
TARGETS = TARGET_TICKS
LAP = PERIOD
HORIZON = 5 * LAP
Q717_K = from_j(2, -2, 1, 6)


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


PREPARATIONS = (
    Preparation("open", Q717_K),
    Preparation("sealed", from_j(5, -1, 1, -3)),
    Preparation("supported", Q717_K, from_j(6, -1, 3, 1)),
)


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


def word(field):
    return field[PASSIVE][R0]


def reported(value):
    return j_coefficients(value)


def mismatch(field, reference, coordinates):
    for cell, lane in coordinates:
        if field[cell][lane] != reference[cell][lane]:
            return [cell, lane, reported(field[cell][lane]), reported(reference[cell][lane])]
    return None



def work_contact(field, after_c, after_b):
    difference = subtract(field[HEAD][CLK], field[PASSIVE][CLK])
    return {
        "CLK_difference_before_C": reported(difference),
        "CLK_edge_admitted": even(difference),
        "head_CLK": [reported(cut[HEAD][CLK]) for cut in (field, after_c, after_b)],
        "passive_CLK": [reported(cut[PASSIVE][CLK]) for cut in (field, after_c, after_b)],
        "passive_CORR": [reported(cut[PASSIVE][CORR]) for cut in (field, after_c, after_b)],
    }

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


def run_fresh(preparation, cuts, arrivals, digest):
    checks = Witnesses()
    target_records = {}
    third_changes = {"C": [], "B": []}
    first_third_change = {}
    initial_book = account(preparation.stock(cuts[0]))
    stock = preparation.stock_coordinates()
    coordinates = [(cell, lane) for cell in range(len(cuts[0])) for lane in range(4)]
    projected = [coordinate for coordinate in coordinates if coordinate not in stock]
    radiation = [(cell, lane) for cell, lane in coordinates if lane in (CLK, CORR)]
    for rank, arrival in sorted(arrivals.items()):
        prior = (arrival - 1) % LAP
        field = preparation.stock(cuts[prior])
        expected_account = account(field)
        if expected_account != initial_book:
            checks.note("fresh_initial_book", [rank, reported_account(field)])
        bit = prior % 2
        if bit != 1:
            checks.note("fresh_wrong_start_bit", [rank, bit])
        digest.update(bytes((bit,)))
        trace_cut(digest, field)
        trace = []
        for step in range(1, 4):
            incoming = field
            before = word(incoming)
            after_c, field, tags, bit = transition(
                field, bit, expected_account, checks, [rank, step], digest
            )
            c_word, b_word = word(after_c), word(field)
            moved_c, moved_b = c_word != before, b_word != c_word
            trace.append({
                "R0": [reported(before), reported(c_word), reported(b_word)],
                "tags": [tags[HEAD], tags[PASSIVE]],
            })
            if rank in TARGETS and step == 2:
                work_record = trace[-1]
                work_record["contact"] = work_contact(incoming, after_c, field)
                reference = cuts[(arrival + 1) % LAP]
                work_record["carrier_mismatch_after_B"] = mismatch(field, reference, projected)
                work_record["paid_radiation_mismatch_after_B"] = mismatch(
                    field, preparation.stock(reference), radiation
                )
                active = rank == 4 and preparation.name != "sealed"
                common_word = (-3, 2, -5, 1)
                expected_word = (-5, 0, -5, 0) if active else common_word
                expected_tags = [0, 2] if active else [2, 0]
                if (work_record["R0"][1:] != [common_word, expected_word]
                        or work_record["tags"] != expected_tags):
                    checks.note("fresh_work_prediction", [rank, work_record])
            if step == 3:
                for stage, moved in (("C", moved_c), ("B", moved_b)):
                    if moved:
                        third_changes[stage].append(rank)
                        first_third_change.setdefault(stage, [rank, trace[-1]])
                        if rank in TARGETS:
                            checks.note("fresh_target_retention", [rank, stage, trace[-1]])
            else:
                allowed = rank in TARGETS and step == 2
                for stage, moved in (("C", moved_c), ("B", moved_b)):
                    if moved and not allowed:
                        checks.note("fresh_unscheduled_write", [rank, step, stage, trace[-1]])
                if allowed and (not moved_c or b_word == before):
                    checks.note("fresh_missing_target_write", [rank, trace[-1]])
        if rank in TARGETS:
            if trace[0]["tags"][0] != 1:
                checks.note("fresh_missing_head_read", [rank, trace[0]])
            target_records[rank] = trace
    words = {rank: trace[1]["R0"][2] for rank, trace in target_records.items()}
    distinct = len(words) == 2 and len(set(words.values())) == 2
    return {
        "fresh_trials": len(arrivals),
        "target_trace": target_records,
        "target_endpoints_distinct": distinct,
        "third_tick_changes_all_ranks": third_changes,
        "first_third_tick_change": first_third_change,
        "failures": checks.report(),
    }


def run_stream(preparation, cuts, transported, digest):
    checks = Witnesses()
    field = preparation.stock(cuts[0])
    initial = field
    expected_account = account(field)
    bit = 0
    digest.update(bytes((bit,)))
    trace_cut(digest, field)
    seen = {(field, bit): 0}
    first_repeat = None
    full_return = None
    reference_reads = {base + lap * LAP: rank
                       for lap in range(5) for rank, base in TARGETS.items()}
    reference_work = {tick + 1: rank for tick, rank in reference_reads.items()}
    stock = preparation.stock_coordinates()
    cells = range(len(field))
    projected = [(cell, lane) for cell in cells for lane in range(4)
                 if (cell, lane) not in stock]
    radiation = [(cell, lane) for cell in cells for lane in (CLK, CORR)]
    qualified_reads = {}
    qualified_words = {rank: set() for rank in TARGETS}
    scheduled = []
    pending_recovery = []
    held = word(field)
    hold_lead = 0
    projection_mismatches = Witnesses()
    for tick in range(1, HORIZON + 1):
        pre_index = (tick - 1) % LAP
        incoming_bit = bit
        incoming = field
        before = word(incoming)
        is_read = tick in reference_reads
        read_antecedent = None
        if is_read:
            read_antecedent = mismatch(field, cuts[pre_index], projected)
            if incoming_bit != pre_index % 2:
                read_antecedent = ["bit", incoming_bit, pre_index % 2]
        after_c, field, tags, bit = transition(
            field, bit, expected_account, checks, [tick], digest
        )
        if is_read:
            if read_antecedent is None and tags[HEAD] == 1:
                qualified_reads[tick] = reference_reads[tick]
            else:
                checks.note("unqualified_head_read",
                            [tick, reference_reads[tick], tags[HEAD], read_antecedent])
        c_word, b_word = word(after_c), word(field)
        moved_c, moved_b = c_word != before, b_word != c_word
        if tick in reference_work:
            rank = reference_work[tick]
            qualifying_read = qualified_reads.get(tick - 1) == rank
            completed_write = b_word != before
            if not moved_c or not completed_write:
                checks.note("missing_scheduled_write", [tick, rank, moved_c, completed_write])
            if qualifying_read and completed_write:
                qualified_words[rank].add(reported(b_word))
            else:
                checks.note("missing_qualified_sample", [tick, rank])
            record = {
                "tick": tick, "rank": rank, "qualified_read": qualifying_read,
                "R0": [reported(before), reported(c_word), reported(b_word)],
                "tags": [tags[HEAD], tags[PASSIVE]],
                "contact": work_contact(incoming, after_c, field),
                "carrier_recovery": None, "paid_radiation_recovery": None,
            }
            scheduled.append(record)
            pending_recovery.append(record)
            held = b_word
            hold_lead = tick
        else:
            if moved_c:
                checks.note("unscheduled_R0_change",
                            [tick, "C", reported(before), reported(c_word)])
            if moved_b:
                checks.note("unscheduled_R0_change",
                            [tick, "B", reported(c_word), reported(b_word)])
            for stage, observed in (("C", c_word), ("B", b_word)):
                if observed != held:
                    checks.note("hold_mismatch",
                                [hold_lead, tick, stage, reported(held), reported(observed)])
        for stage, cut, reference, stage_bit, expected_bit in (
            ("C", after_c, transported[pre_index], incoming_bit, pre_index % 2),
            ("B", field, cuts[pre_index + 1], bit, tick % 2),
        ):
            carrier_error = mismatch(cut, reference, projected)
            paid_error = mismatch(cut, preparation.stock(reference), radiation)
            if stage_bit != expected_bit:
                carrier_error = ["bit", stage_bit, expected_bit]
                paid_error = carrier_error
            if carrier_error is not None:
                projection_mismatches.note("carrier", [tick, stage, carrier_error])
            if paid_error is not None:
                projection_mismatches.note("paid_radiation", [tick, stage, paid_error])
            for record in pending_recovery:
                if (tick, stage) == (record["tick"], "C"):
                    continue
                if carrier_error is None and record["carrier_recovery"] is None:
                    record["carrier_recovery"] = [tick, stage]
                if paid_error is None and record["paid_radiation_recovery"] is None:
                    record["paid_radiation_recovery"] = [tick, stage]
            pending_recovery = [record for record in pending_recovery
                                if record["carrier_recovery"] is None
                                or record["paid_radiation_recovery"] is None]
        state = field, bit
        if first_repeat is None and state in seen:
            first_repeat = [seen[state], tick]
        seen.setdefault(state, tick)
        if full_return is None and state == (initial, 0):
            full_return = tick
    first_rank, second_rank = sorted(TARGETS)
    intersection = sorted(qualified_words[first_rank] & qualified_words[second_rank])
    findings = checks.report()
    all_samples = "missing_qualified_sample" not in findings
    distinct_and_held = (
        all_samples and all(qualified_words.values()) and not intersection
        and "missing_scheduled_write" not in findings and "hold_mismatch" not in findings
        and "unscheduled_R0_change" not in findings
    )
    return {
        "account": reported_account(initial),
        "failures": findings,
        "clock_projection_mismatches": projection_mismatches.report(),
        "period_horizon": HORIZON,
        "first_repeat": first_repeat,
        "first_full_return": full_return,
        "qualified_word_classes": {rank: sorted(words)
                                   for rank, words in qualified_words.items()},
        "qualified_class_intersection": intersection,
        "all_ten_qualified": all_samples,
        "distinct_and_held_through_horizon": distinct_and_held,
        "renewable_decoder_verified": distinct_and_held and full_return is not None,
        "scheduled": scheduled,
    }


def main():
    if not __debug__:
        raise RuntimeError("Run without Python optimization so native assertions are active")
    sys.stdout.reconfigure(newline="\n")
    digest = sha256()
    bare_findings = Findings()
    cuts, transported, arrivals = bare_reference(bare_findings, digest)
    if bare_findings.counts:
        raise RuntimeError(f"bare reference failed: {bare_findings.counts}")
    results = {}
    for preparation in PREPARATIONS:
        results[preparation.name] = {
            "fresh": run_fresh(preparation, cuts, arrivals, digest),
            "stream": run_stream(preparation, cuts, transported, digest),
        }
    predicted_accounts = {
        "open": ((-12, 0, -4, -4), (20, 6, 8, 17), (434, 0, 151, 151), 717),
        "sealed": ((-12, 0, -4, -4), (23, 7, 8, 8), (434, 0, 151, 151), 717),
        "supported": ((-12, 0, -4, -4), (26, 5, 11, 18), (487, 0, 180, 180), 794),
    }
    for name, result in results.items():
        result["initial_account_matches_prediction"] = (
            result["stream"]["account"] == predicted_accounts[name]
        )
    fresh_open = results["open"]["fresh"]
    fresh_sealed = results["sealed"]["fresh"]
    fresh_causal = {}
    for rank in sorted(TARGETS):
        opened = fresh_open["target_trace"][rank][1]
        sealed = fresh_sealed["target_trace"][rank][1]
        fresh_causal[rank] = {
            "equal_R0_before_and_after_C": opened["R0"][:2] == sealed["R0"][:2],
            "different_R0_after_B": opened["R0"][2] != sealed["R0"][2],
            "passive_B_tags": [opened["tags"][1], sealed["tags"][1]],
            "CLK_contact_admitted": [opened["contact"]["CLK_edge_admitted"],
                                     sealed["contact"]["CLK_edge_admitted"]],
        }
    output = {
        "trajectory_sha256": digest.hexdigest(),
        "fixtures": results,
        "fresh_CLK_rotation_control": {
            "equal_CLK_norm": norm(PREPARATIONS[0].passive_clk)
                              == norm(PREPARATIONS[1].passive_clk),
            "target_comparisons": fresh_causal,
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
