#!/usr/bin/env python3
"""Result-exposed, code-independent PR1871 implementation attack.

Written from the frozen review preregistration and permitted symbolic source
documents only. Internal basis: (1,rho,rho**2,rho**3), rho=j**2.
No author executable, literal word, scientific output, or log is imported.
Do not execute before public source pin and readback.
"""

import argparse
from functools import cache
import hashlib
import itertools
import json


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 1, 0, 0)
U = (1, -1, 0, 0)
W = (1, 1, 0, 0)
B = (1, 0, 1, 0)
TARGET_HEAD = "26731e2bd7f1394b4d274528525e6d78cbe6bbf9"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    cyclic = [0] * 5
    for i in range(4):
        for k in range(4):
            cyclic[(i + k) % 5] += a[i] * b[k]
    return tuple(cyclic[i] - cyclic[4] for i in range(4))


def rho_matrix(z):
    a, b, c, d = z
    return (-d, a - d, b - d, c - d)


@cache
def rho_power(exponent):
    result = ONE
    for _ in range(exponent % 5):
        result = rho_matrix(result)
    return result


@cache
def hermitian(z):
    a, b, c, d = z
    conjugate = (a - b, -b, d - b, c - b)
    return mul(z, conjugate)


@cache
def q(z):
    return 2 * sum(x * x for x in z) - sum(z[i] * z[k]
                  for i in range(4) for k in range(i + 1, 4))


def canonical(z):
    a, b, c, d = z
    return [a - c, d - c, b - c, -c]


def raw_contact(a, b):
    delta = tuple(a[i] - b[i] for i in range(4))
    if any(x & 1 for x in delta):
        return (a, b)
    twist = rho_matrix(delta)
    return (tuple((a[i] + b[i] + twist[i]) // 2 for i in range(4)),
            tuple((a[i] + b[i] - twist[i]) // 2 for i in range(4)))


@cache
def source_phase(a):
    a %= 9
    if a == 0:
        return (ZERO, (2, 0, 0, 0), ZERO)
    e = a if a <= 4 else a - 4
    minus = add(ONE, neg(rho_power(e)))
    plus = add(ONE, rho_power(e))
    return (minus, plus, ZERO) if a <= 4 else (ZERO, plus, minus)


@cache
def clock_phase(k):
    z = mul(rho_power(k), W)
    return (z, neg(z))


@cache
def bank(label):
    pairs = [neg(B), B] * 5
    if label is not None:
        require(0 <= label < 5, "bank label outside Z/5")
        changed = rho_matrix(B)
        pairs[2 * label : 2 * label + 2] = [neg(changed), changed]
    return tuple(pairs)


def render(a, k, selector, labels, queued_a, queued_k):
    require(len(labels) == 4 and selector in (0, 1, 2), "bad analytic chart")
    selector_slots = [ZERO] * 3
    selector_slots[selector] = U
    result = list(source_phase(a)) + list(clock_phase(k)) + [ZERO]
    result += selector_slots + [W, ZERO]
    for label in labels:
        result.extend(bank(label))
    result += list(source_phase(queued_a)) + list(clock_phase(queued_k))
    require(len(result) == 56, "analytic state omitted coordinates")
    return result


def compile_words():
    # Each building block is reconstructed from the allowed displayed equations.
    O, A0, O2, T = [(1, 5)], [(5, 9)], [(9, 10)], [(3, 4)]
    F = [(0, 1), (1, 2)]
    F_INV = [(1, 2)] * 4 + [(0, 1)] * 4

    def commutator(c, inverse=False):
        bc = [(c, 9)]
        if inverse:
            return bc + A0 + bc * 4 + A0 * 4
        return A0 + bc + A0 * 4 + bc * 4

    def scan(base):
        result = []
        for p in range(5):
            left, right = base + 2 * p, base + 2 * p + 1
            k = ([(3, left)] * 4 + [(left, right)] * 4
                 + [(3, left), (left, right)])
            result += [(3, 10)] + k + [(3, 10)] * 4 + T
        return result

    def selected(c, base):
        return commutator(c) + O2 + scan(base) + O2 * 4 + commutator(c, True)

    def controlled_swap(c, d):
        dword = ([(9, c)] * 3 + [(9, d)] * 3
                 + [(9, c), (9, d), (9, c)])
        return A0 + dword + A0 * 4 + dword

    r = O + selected(6, 11) + selected(7, 21)
    r += controlled_swap(7, 8) + controlled_swap(6, 7) + O * 4
    s = r + F_INV + r + F + F + T
    require(len(r) == 261 and len(s) == 535, "symbolic word reconstruction length")

    def embed(edges, stage):
        def address(i):
            return i + 20 if stage == 1 and 11 <= i <= 30 else i
        return tuple((address(i), address(j)) for i, j in edges)

    rs = (embed(r, 0), embed(r, 1))
    ss = (embed(s, 0), embed(s, 1))
    program = [("C", i, j) for i, j in ss[0]] * 10
    program += [("SWAP", i, 51 + i) for i in range(5)]
    program += [("C", i, j) for i, j in ss[1]] * 10
    require(len(program) == 10705, "mixed program length")
    require(all(i < 31 and j < 31 for i, j in ss[0]), "stage A touches queued/new regions")
    require(all(i not in range(11, 31) and j not in range(11, 31)
                and i < 51 and j < 51 for i, j in ss[1]), "stage B touches protected regions")
    return tuple(r), tuple(s), rs, ss, tuple(F), tuple(F_INV), tuple(T), tuple(program)


class Lane:
    def __init__(self):
        self.pair_cache = {}
        self.contacts = 0
        self.swaps = 0
        self.fixture_contacts = 0

    def contact(self, state, i, j, fixture=False):
        key = (state[i], state[j])
        result = self.pair_cache.get(key)
        if result is None:
            result = raw_contact(*key)
            require(add(*key) == add(*result), "contact sum")
            require(q(key[0]) + q(key[1]) == q(result[0]) + q(result[1]), "contact Q")
            require(add(hermitian(key[0]), hermitian(key[1]))
                    == add(hermitian(result[0]), hermitian(result[1])), "contact Hermitian account")
            require(sum(key[0]) % 5 == sum(result[0]) % 5, "first labelled contact residue")
            require(sum(key[1]) % 5 == sum(result[1]) % 5, "second labelled contact residue")
            delta = add(key[0], neg(key[1]))
            require(rho_matrix(delta) == mul(RHO, delta), "rho matrix versus convolution")
            cycle = key
            for _ in range(5):
                cycle = raw_contact(*cycle)
            require(cycle == key, "contact fifth power")
            inverse = result
            for _ in range(4):
                inverse = raw_contact(*inverse)
            require(inverse == key, "contact native inverse")
            self.pair_cache[key] = result
        state[i], state[j] = result
        if fixture:
            self.fixture_contacts += 1
        else:
            self.contacts += 1

    def swap(self, state, i, j):
        before = (state[i], state[j])
        require(sum(before[0]) % 5 == sum(before[1]) % 5, "reload swaps unequal residues")
        state[i], state[j] = state[j], state[i]
        after = (state[i], state[j])
        require(add(*before) == add(*after), "swap sum")
        require(q(before[0]) + q(before[1]) == q(after[0]) + q(after[1]), "swap Q")
        require(add(hermitian(before[0]), hermitian(before[1]))
                == add(hermitian(after[0]), hermitian(after[1])), "swap Hermitian account")
        self.swaps += 1


RESIDUES = tuple([0, 2, 0, 2, 3] + [0, 0, 0, 0, 2, 0]
                 + [3, 2] * 20 + [0, 2, 0, 2, 3])


def check_full(state, expected):
    require(state == expected, "complete analytic 56-slot checkpoint mismatch")
    require(len(state) == 56, "trajectory width")
    require(tuple(sum(z) % 5 for z in state) == RESIDUES, "complete labelled residues")
    require(sum(q(z) for z in state) == 156, "complete Q")
    require(tuple(sum(z[i] for z in state) for i in range(4)) == (6, 0, 0, 0), "complete sum")
    require(tuple(sum(hermitian(z)[i] for z in state) for i in range(4))
            == (96, 0, 36, 36), "complete Hermitian account")


class InvalidRecord(ValueError):
    pass


def read_records(records):
    # This interface has exactly the forty current bank coordinates, no inputs.
    if len(records) != 40:
        raise InvalidRecord("four complete banks required")
    labels = []
    for start in range(0, 40, 10):
        candidate = tuple(records[start : start + 10])
        matches = [p for p in range(5) if candidate == bank(p)]
        if len(matches) != 1:
            raise InvalidRecord("blank, multiply occupied or malformed bank")
        labels.append(matches[0])
    result = []
    for x, y in (labels[:2], labels[2:]):
        difference = (x - y) % 5
        if difference not in (1, 3):
            raise InvalidRecord("invalid record difference")
        result += [0 if difference == 1 else 1, (-x) % 5]
    return tuple(result)


def reader_mutations():
    # Frozen standalone rejection inventory: 24 explicitly specified mutations.
    reference = list(bank(0) + bank(4) + bank(0) + bank(4))
    require(read_records(reference) == (0, 0, 0, 0), "valid reader control")
    mutations = [("all-four-blank", list(bank(None) * 4))]
    for position in range(4):
        bad = reference.copy()
        bad[10 * position : 10 * position + 10] = bank(None)
        mutations.append((f"blank-bank-{position}", bad))
    double = list(bank(0))
    double[2:4] = [neg(rho_matrix(B)), rho_matrix(B)]
    for position in range(4):
        bad = reference.copy()
        bad[10 * position : 10 * position + 10] = double
        mutations.append((f"double-record-bank-{position}-pairs-0-1", bad))
    for position in range(4):
        bad = reference.copy()
        bad[10 * position] = ZERO
        mutations.append((f"zero-first-coordinate-bank-{position}", bad))
    reversed_record = list(bank(0))
    reversed_record[0], reversed_record[1] = reversed_record[1], reversed_record[0]
    for position in range(4):
        bad = reference.copy()
        bad[10 * position : 10 * position + 10] = reversed_record
        mutations.append((f"reversed-record-pair-bank-{position}", bad))
    for pair in range(2):
        for difference in (0, 2, 4):
            bad = reference.copy()
            bad[20 * pair : 20 * pair + 10] = bank(0)
            bad[20 * pair + 10 : 20 * pair + 20] = bank((-difference) % 5)
            mutations.append((f"invalid-difference-pair-{pair}-d{difference}", bad))
    mutations.append(("truncated-39-coordinates", reference[:-1]))
    require(len(mutations) == 24, "reader rejection inventory changed")
    for name, bad in mutations:
        try:
            read_records(bad)
        except InvalidRecord:
            continue
        raise AssertionError("reader accepted frozen mutation: " + name)
    return [name for name, _ in mutations]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump-data", help="optional scratch-only canonical endpoint/checkpoint JSON")
    args = parser.parse_args()
    r, s, rs, ss, f, finv, t, program = compile_words()
    lane = Lane()
    fixture = list(source_phase(0))
    for tick in range(9):
        for i, j in f:
            lane.contact(fixture, i, j, fixture=True)
        require(tuple(fixture) == source_phase(tick + 1), "analytic nine-cycle source fixture")
    require(lane.fixture_contacts == 18 and len({source_phase(a) for a in range(9)}) == 9,
            "fixture count or source distinctness")
    rejected = reader_mutations()
    checkpoints, endpoints, event_dump = [], [], []
    count_r = count_s = count_reload = count_events = count_inverse = 0
    record_outputs = set()
    common_aux = None

    for inputs in itertools.product((0, 1), range(5), (0, 1), range(5)):
        n, k, m, ell = inputs
        labels = [None] * 4
        state = render(n, k, 0, labels, m, ell)
        initial = state.copy()
        aux = tuple(state[5:51])
        require(len(aux) == 46 and sum(q(z) for z in aux) == 128, "common auxiliary inventory")
        if common_aux is None:
            common_aux = aux
        require(aux == common_aux, "input-dependent auxiliary preparation")
        require(sum(q(z) for z in state[:5]) == sum(q(z) for z in state[51:]) == 14,
                "input cartridge account")
        check_full(state, initial)
        executed = []
        ordinals = [0, 0]  # contacts, all supplied operations; case-local forward only
        selector = 0

        def forward_contact(i, j):
            lane.contact(state, i, j)
            ordinals[0] += 1
            ordinals[1] += 1
            executed.append(("C", i, j))

        def simple_word(edges):
            for i, j in edges:
                forward_contact(i, j)

        def snapshot(kind, stage, step, read_index, expected):
            check_full(state, expected)
            checkpoints.append([list(inputs), kind, stage, step, read_index,
                                [canonical(z) for z in state]])

        for stage, (source_start, clock_start) in enumerate(((n, k), (m, ell))):
            if stage == 1:
                spent = list(source_phase(n + 10)) + list(clock_phase(k))
                queued = list(source_phase(m)) + list(clock_phase(ell))
                for i in range(5):
                    lane.swap(state, i, 51 + i)
                    ordinals[1] += 1
                    executed.append(("SWAP", i, 51 + i))
                    require(state[: i + 1] == queued[: i + 1]
                            and state[51 : 52 + i] == spent[: i + 1], "partial reload disposition")
                snapshot("LOAD", -1, -1, -1, render(m, ell, 0, labels, n + 10, k))
                count_reload += 1
                selector = 0
            queued_a, queued_k = (m, ell) if stage == 0 else (n + 10, k)
            stage_events = []
            stage_offset_c, stage_offset_ops = 5350 * stage, 5355 * stage
            for step in range(10):
                a = (source_start + step) % 9
                clock = (clock_start + step) % 5
                for read_index, phase in enumerate((a, (a - 1) % 9)):
                    if read_index:
                        simple_word(finv)
                    require(state[5] == ZERO, "read started with nonzero marker")
                    onset = None
                    for edge_index, (i, j) in enumerate(rs[stage]):
                        forward_contact(i, j)
                        if edge_index == 0:
                            require(state[5] == (U if phase == 0 else ZERO), "designated onset marker")
                            if state[5] == U:
                                onset = tuple(ordinals)
                    if phase == 0:
                        require(onset is not None, "missing active read onset")
                        if selector < 2:
                            destination = 2 * stage + selector
                            require(labels[destination] is None, "selected bank not fresh on reached layer")
                            labels[destination] = (-clock) % 5
                        selector = (selector + 1) % 3
                        completion = tuple(ordinals)
                        expected_onset = 535 * step + (1 if read_index == 0 else 270)
                        expected_completion = 535 * step + (261 if read_index == 0 else 530)
                        require(onset == (stage_offset_c + expected_onset,
                                          stage_offset_ops + expected_onset), "event onset timing")
                        require(completion == (stage_offset_c + expected_completion,
                                               stage_offset_ops + expected_completion), "event completion timing")
                        stage_events.append([step, read_index, onset[0], onset[1],
                                             completion[0], completion[1]])
                        count_events += 1
                    snapshot("R", stage, step, read_index,
                             render(phase, clock, selector, labels, queued_a, queued_k))
                    count_r += 1
                simple_word(f)
                simple_word(f)
                simple_word(t)
                snapshot("S", stage, step, -1,
                         render(a + 1, clock + 1, selector, labels, queued_a, queued_k))
                count_s += 1
            expected_event_steps = (0, 1, 9) if source_start == 0 else (0, 8, 9)
            require(tuple(row[0] for row in stage_events) == expected_event_steps,
                    "stage event steps")
            first_two = (1, 805) if source_start == 0 else (270, 4281)
            require(tuple(row[2] - stage_offset_c for row in stage_events[:2]) == first_two,
                    "first two designated onsets")
            require(stage_events[1][2] - stage_events[0][2]
                    == (804 if source_start == 0 else 4011), "within-stage onset gap")
            require(selector == 0, "stage did not restore selector A")
            event_dump.append([list(inputs), stage, stage_events])

        require(tuple(executed) == program, "input-dependent or wrongly reconstructed actual program")
        require(ordinals == [10700, 10705], "per-case forward operation count")
        expected_labels = [(-k) % 5, (-(k + (1 if n == 0 else 8))) % 5,
                           (-ell) % 5, (-(ell + (1 if m == 0 else 8))) % 5]
        require(labels == expected_labels, "analytic endpoint record labels")
        expected_final = render(m + 10, ell, 0, expected_labels, n + 10, k)
        check_full(state, expected_final)
        require(read_records(state[11:51]) == inputs, "current-four-bank reader failed input recovery")
        code = tuple(state[11:51])
        require(code not in record_outputs, "four-bank output collision")
        record_outputs.add(code)
        endpoints.append([list(inputs), [canonical(z) for z in state]])
        for kind, i, j in reversed(program):
            if kind == "SWAP":
                lane.swap(state, i, j)
            else:
                for _ in range(4):
                    lane.contact(state, i, j)
        require(state == initial, "complete 56-slot primitive inverse")
        count_inverse += 1

    require((count_r, count_s, count_reload, count_events, count_inverse)
            == (4000, 2000, 100, 600, 100), "frozen checkpoint/event/inverse totals")
    require(lane.contacts == 5350000 and lane.swaps == 1000, "frozen trajectory primitive totals")
    require(len(record_outputs) == 100, "joint output injectivity")

    def encoded(value):
        return json.dumps(value, separators=(",", ":")).encode("ascii")

    operation_bytes = "".join(f"{kind},{i},{j}\n" for kind, i, j in program).encode("ascii")
    r_bytes = "".join(f"{i},{j}\n" for i, j in r).encode("ascii")
    s_bytes = "".join(f"{i},{j}\n" for i, j in s).encode("ascii")
    endpoint_bytes, checkpoint_bytes = encoded(endpoints), encoded(checkpoints)
    if args.dump_data:
        with open(args.dump_data, "wb") as handle:
            handle.write(encoded({"endpoints": endpoints, "checkpoints": checkpoints,
                                  "events": event_dump, "operations": program,
                                  "R_edges": r, "S_edges": s}))
    result = {
        "status": "PASS",
        "scope": "NON-CANONICAL/L1/result-exposed/code-independent/single-x86_64-lane",
        "target_head": TARGET_HEAD,
        "R_contacts": len(r), "S_contacts": len(s),
        "operation_count_forward_per_case": len(program),
        "operation_word_sha256": hashlib.sha256(operation_bytes).hexdigest(),
        "R_edges_sha256": hashlib.sha256(r_bytes).hexdigest(),
        "S_edges_sha256": hashlib.sha256(s_bytes).hexdigest(),
        "endpoint_sha256": hashlib.sha256(endpoint_bytes).hexdigest(),
        "endpoint_bytes": len(endpoint_bytes),
        "checkpoint_sha256": hashlib.sha256(checkpoint_bytes).hexdigest(),
        "checkpoint_bytes": len(checkpoint_bytes),
        "R_checkpoints": count_r, "S_checkpoints": count_s,
        "reload_checkpoints": count_reload, "designated_events": count_events,
        "full_native_inverses": count_inverse,
        "trajectory_contact_applications": lane.contacts,
        "trajectory_swap_applications": lane.swaps,
        "separate_fixture_contacts": lane.fixture_contacts,
        "distinct_ordered_contact_pairs": len(lane.pair_cache),
        "strict_reader_rejections": len(rejected),
        "strict_reader_mutation_names": rejected,
        "four_bank_codes": len(record_outputs),
        "core_complete_slots": 56, "common_auxiliary_slots": 46,
        "common_auxiliary_account": 128, "complete_account": 156,
        "serializer": "REVIEW-SCOPE.md; compact ASCII JSON; canonical j coordinates",
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
