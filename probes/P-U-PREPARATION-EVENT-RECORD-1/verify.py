"""P-U-PREPARATION-EVENT-RECORD-1: prospective, result-exposed proof audit.

Do not execute or import before the complete public pin and byte readback.
Self-contained standard-library exact arithmetic; no runtime source imports,
network, randomness, floating point or file writes. The incidence constructor
uses a disclosed captured source and fresh observer cells, not a native-U write.
The phase-recognition algorithm is inherited from P-U-FINITE-HISTORY-EVENT-1.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import sys


NAME = "P-U-PREPARATION-EVENT-RECORD-1"
BALANCED = (0, 1, 2, -2, -1)
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PARENT_PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
PHASE_MAPS = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
HISTORY_LENGTH = 2560
MODULUS = 1024


def theta(n):
    return n.bit_count() % 2


def generator(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        values = (b, a, d, c, q, r)
    elif index == 1:
        values = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        values = (-c + 2, -d + 1 + r, -a + 2, -b + 1 - r, 1 - q, -r)
    elif index == 3:
        values = (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r)
    elif index == 4:
        values = (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r)
    else:
        raise ValueError("unknown generator")
    return tuple(v % 5 for v in values)


def quotient(x):
    return sum(x) % 5, x[4], x[5]


def quotient_generator(index, state):
    z, q, r = state
    values = ((z, q, r), (-z, -q, -r), (2 - z, 1 - q, -r),
              (2 - z, 1 - q, 1 - r), (3 - z, 2 - q, 1 - r))[index]
    return tuple(v % 5 for v in values)


def native_step(x, bit):
    return generator((sum(x) + 2 * bit) % 5, x)


def quotient_step(state, bit):
    return quotient_generator((state[0] + 2 * bit) % 5, state)


def quotient_prefix(state):
    result = [state]
    for bit in (0, 1, 1):
        result.append(quotient_step(result[-1], bit))
    return tuple(result)


def analytic_history_equal(left, right):
    if left[1:] != right[1:]:
        return False
    return left[0] == right[0] or (left[1:] == (3, 0) and {left[0], right[0]} == {0, 2})


def tail_formula(state):
    z, q, r = state
    values = ((q + 1, r + 1), (1 - q, 1 - r), (2 - q, 1 - r),
              (2 - q, 2 - r), (3 - q, 2 - r))[z]
    return tuple(v % 5 for v in values)


def json_value(value):
    if isinstance(value, Fraction):
        return str(value.numerator) + "/" + str(value.denominator)
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(item) for item in value]
    return value


class Audit:
    def __init__(self):
        self.checks = Counter()
        self.failures = 0
        self.examples = []
        self.results = {}

    def equal(self, group, claim, actual, expected, context=None):
        self.checks[group] += 1
        if actual != expected:
            self.failures += 1
            if len(self.examples) < 20:
                self.examples.append({"group": group, "claim": claim, "actual": actual,
                                      "expected": expected, "context": context})


def audit_native_factor(audit):
    images = [set() for _ in range(5)]
    fibre_counts = Counter()
    for x in product(range(5), repeat=6):
        state = quotient(x)
        fibre_counts[state] += 1
        for index in range(5):
            y = generator(index, x)
            images[index].add(y)
            audit.equal("A", "generator_quotient_commuting_square", quotient(y),
                        quotient_generator(index, state), (x, index))
            audit.equal("A", "generator_involution", generator(index, y), x, (x, index))
        for bit in (0, 1):
            audit.equal("A", "selected_native_quotient_commuting_square",
                        quotient(native_step(x, bit)), quotient_step(state, bit), (x, bit))
    for index, image in enumerate(images):
        audit.equal("A", "generator_is_bijection", len(image), 15625, index)
    audit.equal("A", "complete_quotient_carrier", len(fibre_counts), 125)
    audit.equal("A", "quotient_fibre_sizes", dict(Counter(fibre_counts.values())), {125: 125})
    for state in product(range(5), repeat=3):
        for bit in (0, 1):
            audit.equal("A", "closed_phase_selector_table", quotient_step(state, bit)[0],
                        PHASE_MAPS[bit][state[0]], (state, bit))
    audit.results["native_factor"] = {
        "native_states": 15625, "generators": 5, "driver_choices": 2,
        "quotient_states": len(fibre_counts), "fibre_size": 125,
        "factor": "(z,q,r); all-time closure follows by induction from the commuting square",
        "source_dependence": "at fixed ready(q,r), apparatus history depends only on the initial piston sum modulo five",
    }


def audit_observability(audit):
    states = tuple(product(range(5), repeat=3))
    prefixes = {state: quotient_prefix(state) for state in states}
    histories = {state: tuple(q[1:] for q in prefix) for state, prefix in prefixes.items()}
    for state, prefix in prefixes.items():
        audit.equal("B", "three_tick_synchronization", prefix[3][0], 1, state)
        audit.equal("B", "exact_tail_affine_formula", prefix[3][1:], tail_formula(state), state)
    for left in states:
        for right in states:
            first_two = histories[left][:3] == histories[right][:3]
            through_three = histories[left] == histories[right]
            same_tail_state = prefixes[left][3] == prefixes[right][3]
            audit.equal("B", "complete_history_equivalence_analytic", first_two,
                        analytic_history_equal(left, right), (left, right))
            audit.equal("B", "two_tick_history_decides_all_future_history", first_two,
                        through_three and same_tail_state, (left, right))
            audit.equal("B", "tail_equivalence_exactly_A3", same_tail_state,
                        tail_formula(left) == tail_formula(right), (left, right))
    global_counts = [len({histories[state][:t + 1] for state in states}) for t in range(4)]
    audit.equal("B", "complete_prefix_partition_counts", global_counts, [25, 121, 124, 124])
    ready_rows = []
    source_classes = defaultdict(list)
    for ready in product(range(5), repeat=2):
        subset = tuple((z,) + ready for z in range(5))
        counts = [len({histories[state][:t + 1] for state in subset}) for t in range(4)]
        horizon = next(t for t in range(4) if counts[t] == counts[3])
        predicted = 2 if ready in ((0, 0), (3, 3), (1, 3)) else 1
        audit.equal("B", "minimal_ready_history_horizon", horizon, predicted, ready)
        audit.equal("B", "ready_full_history_class_count", counts[3],
                    4 if ready == (3, 0) else 5, ready)
        tail_count = len({tail_formula(state) for state in subset})
        audit.equal("B", "ready_tail_class_count", tail_count,
                    4 if ready in ((0, 0), (3, 0), (3, 3), (1, 3)) else 5, ready)
        ready_rows.append({"ready": ready, "prefix_classes": counts,
                           "minimal_horizon": horizon, "tail_classes": tail_count})
        for piston in product(range(5), repeat=4):
            x = piston + ready
            state = quotient(x)
            native = [x]
            for bit in (0, 1, 1):
                native.append(native_step(native[-1], bit))
            actual = tuple(y[4:] for y in native)
            audit.equal("B", "every_ready_source_matches_quotient_history", actual, histories[state], x)
            source_classes[actual[:3]].append(piston)
    class_types = Counter(tuple(sorted({sum(p) % 5 for p in sources}))
                          for sources in source_classes.values())
    audit.equal("B", "source_class_sum_types", dict(class_types),
                {(0,): 25, (1,): 25, (2,): 24, (3,): 25, (4,): 24, (2, 4): 1})
    audit.results["native_observability"] = {
        "quotient_states": 125, "ordered_state_pairs": 15625,
        "prefix_partition_counts": global_counts, "ready_rows": ready_rows,
        "source_classes": len(source_classes), "source_class_types": dict(class_types),
        "unique_full_history_collision": {"ready": (3, 0), "initial_phases": (0, 2),
                                          "initial_piston_sums": (2, 4)},
        "reader_sufficiency": "a source datum admits an exact apparatus-history reader iff it is constant on every admitted observation class",
    }
    return source_classes


def phase_from_history(word, k=10):
    if k == 0:
        return 0
    length = 5 * (1 << (k - 1))
    if len(word) < length:
        raise ValueError("insufficient causal history")
    word = word[-length:]
    parity = None
    for i in range(4):
        if word[length - 5 + i] == word[length - 4 + i]:
            parity = (1 + i) % 2
            break
    if parity is None:
        return -1
    if k == 1:
        return parity
    parent_length = 5 * (1 << (k - 2))
    parent = bytes(word[length - 1 - parity - 2 * j] for j in reversed(range(parent_length)))
    previous = phase_from_history(parent, k - 1)
    return -1 if previous < 0 else parity + 2 * previous


def audit_phase(audit):
    size = 4096
    zero = b"\x00"
    while len(zero) < size:
        zero = bytes(value for bit in zero for value in (bit, 1 - bit))
    blocks = (zero, bytes(1 - bit for bit in zero))
    audit.equal("C", "phase_substitution_equals_literal_TM", zero,
                bytes(theta(n) for n in range(size)))
    audit.equal("C", "complement_substitution_equals_literal_TM", blocks[1],
                bytes(theta(size + n) for n in range(size)))
    language = set()
    residue_weights = Counter()
    contexts = 0
    for pair in PARENT_PAIRS:
        expanded = blocks[pair[0]] + blocks[pair[1]]
        weight = 1 if pair[0] == pair[1] else 2
        for offset in range(size):
            word = expanded[offset:offset + HISTORY_LENGTH]
            phase = phase_from_history(word)
            audit.equal("C", "causal_phase_every_legal_generating_context", phase,
                        (offset + HISTORY_LENGTH - 1) % MODULUS, (pair, offset))
            z_word = bytes(4 - 3 * bit for bit in word)
            decoded = bytes((4 - z) // 3 for z in z_word)
            audit.equal("C", "native_z_history_roundtrip", decoded, word, (pair, offset))
            audit.equal("C", "native_z_history_current_phase_plus_one",
                        (phase_from_history(decoded) + 1) % MODULUS,
                        (offset + HISTORY_LENGTH) % MODULUS, (pair, offset))
            language.add(word)
            residue_weights[phase] += weight
            contexts += 1
    audit.equal("C", "complete_phase_context_count", contexts, 16384)
    audit.equal("C", "all_1024_phases_recognized", sorted(residue_weights), list(range(MODULUS)))
    for phase in range(MODULUS):
        audit.equal("C", "uniform_phase_frequency", residue_weights[phase] * MODULUS, 6 * size, phase)
    audit.results["causal_slot_phase"] = {
        "history_bits": HISTORY_LENGTH, "modulus": MODULUS, "parent_block_size": size,
        "generating_contexts": contexts, "legal_words": len(language),
        "phase_density": Fraction(1, MODULUS), "minimality": "not claimed",
        "source": "inherited causal TM recognition and factor-frequency theorem; no absolute time input to reader",
    }
    return frozenset(language)


def capture_source(piston):
    return tuple(BALANCED[value] for value in piston)


def channel_amplitudes(source):
    return (sum(source),) + tuple(source[i] - source[j] for i, j in PAIRS for _ in range(5))


def slot_event(source, phase):
    """Only captured signed coordinates and reconstructed phase; no weight input."""
    if not 0 <= phase < MODULUS:
        raise ValueError("phase outside frozen slot carrier")
    if phase < 64:
        row, column = divmod(phase, 8)
        amplitude = abs(sum(source))
        return 1 if row < amplitude and column < amplitude else 0
    if phase < 544:
        channel, local = divmod(phase - 64, 16)
        pair_index, _ = divmod(channel, 5)
        row, column = divmod(local, 4)
        i, j = PAIRS[pair_index]
        amplitude = abs(source[i] - source[j])
        return 2 if row < amplitude and column < amplitude else 0
    return 0


def incidence_reference(source):
    slots = []
    amplitudes = channel_amplitudes(source)
    for channel, amplitude in enumerate(amplitudes):
        side = 8 if channel == 0 else 4
        label = 1 if channel == 0 else 2
        for row in range(side):
            for column in range(side):
                slots.append(label if row < abs(amplitude) and column < abs(amplitude) else 0)
    return tuple(slots) + (0,) * (MODULUS - len(slots))


def audit_incidence(audit):
    census = {}
    digest = sha256()
    channel_count = 0
    for piston in product(range(5), repeat=4):
        source = capture_source(piston)
        amplitudes = channel_amplitudes(source)
        audit.equal("D", "exact_channel_count", len(amplitudes), 31, piston)
        total, norm = sum(source), sum(v * v for v in source)
        difference_energy = sum((source[i] - source[j]) ** 2 for i, j in PAIRS)
        audit.equal("D", "complete_difference_square_identity", difference_energy,
                    4 * norm - total * total, piston)
        for channel, amplitude in enumerate(amplitudes):
            bound = 8 if channel == 0 else 4
            audit.equal("D", "integer_channel_fits_fixed_slot_square", abs(amplitude) <= bound, True,
                        (piston, channel))
            channel_count += 1
        reference = incidence_reference(source)
        actual = tuple(slot_event(source, phase) for phase in range(MODULUS))
        for phase, (observed, expected) in enumerate(zip(actual, reference)):
            audit.equal("D", "every_source_slot_matches_independent_channel_expansion", observed,
                        expected, (piston, phase))
        counts = Counter(actual)
        audit.equal("D", "LOW_incidence_count", counts[1], total * total, piston)
        audit.equal("D", "HIGH_incidence_count", counts[2], 5 * difference_energy, piston)
        audit.equal("D", "total_occupied_incidence_count", counts[1] + counts[2],
                    20 * norm - 4 * total * total, piston)
        audit.equal("D", "all_padding_slots_are_SILENT", actual[544:], (0,) * 480, piston)
        audit.equal("D", "zero_source_iff_empty_occupancy", counts[1] + counts[2] == 0,
                    not any(source), piston)
        census[piston] = {"LOW": counts[1], "HIGH": counts[2], "SILENT": counts[0]}
        digest.update(bytes(piston) + bytes(actual))
    audit.results["source_incidence_constructor"] = {
        "sources": len(census), "source_slot_pairs": len(census) * MODULUS,
        "channel_instances": channel_count, "channels": 31,
        "potential_slots": {"LOW": 64, "HIGH": 480, "padding": 480},
        "source_output_word_table_sha256": digest.hexdigest(),
        "source_snapshot": "captured balanced first four head coordinates before native tick one; immutable observer resource",
        "design_status": "explicit incidence design with QDD algebra already known; not independent physical selection",
    }
    return census


def cell_swap(cell, event):
    if cell not in (0, 1, 2) or event not in (0, 1, 2):
        raise ValueError("outside ternary cell alphabet")
    if event == 0:
        return cell
    if cell == 0:
        return event
    if cell == event:
        return 0
    return cell


def slot_details(source, phase):
    if phase < 64:
        row, column = divmod(phase, 8)
        amplitude = sum(source)
        descriptor = ("LOW", row, column)
    elif phase < 544:
        channel, local = divmod(phase - 64, 16)
        pair_index, copy = divmod(channel, 5)
        row, column = divmod(local, 4)
        i, j = PAIRS[pair_index]
        amplitude = source[i] - source[j]
        descriptor = ("HIGH", i, j, copy, row, column)
    else:
        amplitude, descriptor = 0, ("PADDING", phase)
    sign = (amplitude > 0) - (amplitude < 0)
    return descriptor, sign


def fresh_record(source, phase, cell=0):
    """Protocol admission is stricter than the underlying reversible swap."""
    if cell != 0:
        return {"status": "ERROR", "reason": "CELL_NOT_BLANK", "rejected_cell": cell}
    event = slot_event(source, phase)
    if event == 0:
        return {"status": "ERROR", "reason": "NO_ACCEPTED_EVENT"}
    descriptor, sign = slot_details(source, phase)
    # before source, after source, phase, fine slot, signed-channel sign,
    # event label, old cell, written cell. All entries are retained literally.
    record = (source, source, phase, descriptor, sign, event, cell, cell_swap(cell, event))
    return {"status": "RECORDED", "record": record}


def causal_event_read(source, word, language):
    if any(bit not in (0, 1) for bit in word):
        return {"status": "ERROR", "disposition": "ERROR", "rejected_word": word}
    if len(word) < HISTORY_LENGTH:
        return {"status": "UNAVAILABLE", "disposition": "UNAVAILABLE"}
    if len(word) != HISTORY_LENGTH or word not in language:
        return {"status": "ERROR", "disposition": "ERROR", "rejected_word": word}
    phase = phase_from_history(word)
    if phase < 0:
        return {"status": "ERROR", "disposition": "ERROR", "rejected_word": word}
    if not any(source):
        return {"status": "ZERO_SUPPORT", "disposition": "NO_EVENT", "event": 0, "phase": phase}
    event = slot_event(source, phase)
    return {"status": "SUPPORTED", "disposition": "EVENT" if event else "NO_EVENT",
            "event": event, "phase": phase}


def observer_step(state, bit, language):
    source, word, records = state
    if bit not in (0, 1):
        return state, {"status": "ERROR", "disposition": "ERROR", "rejected_input": bit}
    following = (word + bytes((bit,)))[-HISTORY_LENGTH:]
    reading = causal_event_read(source, following, language)
    event = reading.get("event", 0)
    if event:
        admitted = fresh_record(source, reading["phase"])
        if admitted["status"] != "RECORDED":
            return (source, following, records), admitted
        records = records + (admitted["record"],)
    return (source, following, records), reading


def first_hit(records):
    return records[0] if records else None


def audit_records(audit, language, census):
    for event in (0, 1, 2):
        images = tuple(cell_swap(cell, event) for cell in (0, 1, 2))
        audit.equal("E", "controlled_ternary_swap_is_bijection", sorted(images), [0, 1, 2], event)
        audit.equal("E", "fresh_blank_cell_records_event", cell_swap(0, event), event, event)
        for cell in (0, 1, 2):
            audit.equal("E", "controlled_ternary_swap_is_involution",
                        cell_swap(cell_swap(cell, event), event), cell, (cell, event))
    for phase in (0, 64):
        for occupied_cell in (1, 2):
            rejected = fresh_record((1, 0, 0, 0), phase, occupied_cell)
            audit.equal("E", "fresh_cell_protocol_rejects_occupied_cell", rejected["status"], "ERROR",
                        (phase, occupied_cell))
            audit.equal("E", "fresh_cell_protocol_retains_rejected_cell", rejected.get("rejected_cell"),
                        occupied_cell, (phase, occupied_cell))
    pistons = ((0, 0, 0, 0), (1, 0, 0, 0), (1, 4, 0, 0),
               (2, 2, 2, 2), (2, 2, 3, 3), (4, 1, 0, 0), (2, 1, 1, 2))
    rows = []
    for piston in pistons:
        source = capture_source(piston)
        audit.equal("E", "empty_capture_is_UNAVAILABLE",
                    causal_event_read(source, b"", language)["status"], "UNAVAILABLE", piston)
        audit.equal("E", "illegal_complete_capture_is_ERROR",
                    causal_event_read(source, bytes(HISTORY_LENGTH), language)["status"], "ERROR", piston)
        audit.equal("E", "nonbinary_short_capture_is_ERROR",
                    causal_event_read(source, b"\x02", language)["status"], "ERROR", piston)
        audit.equal("E", "nonbinary_complete_capture_is_ERROR",
                    causal_event_read(source, bytes((2,)) * HISTORY_LENGTH, language)["status"], "ERROR", piston)
        for start_phase in (0, 64):
            n0 = 3072 + start_phase
            initial_word = bytes(theta(n) for n in range(n0 - HISTORY_LENGTH, n0))
            state = (source, initial_word, ())
            first = None
            counts = Counter()
            reference = incidence_reference(source)
            prefix_counts = [{0: 0, 1: 0, 2: 0}]
            for offset in range(MODULUS):
                following_counts = dict(prefix_counts[-1])
                following_counts[reference[(start_phase + offset) % MODULUS]] += 1
                prefix_counts.append(following_counts)
            for n in range(n0, n0 + MODULUS):
                before = state
                state, reading = observer_step(state, theta(n), language)
                expected_event = slot_event(source, n % MODULUS)
                audit.equal("E", "causal_stream_event_equals_slot_constructor",
                            reading.get("event"), expected_event, (piston, start_phase, n - n0))
                audit.equal("E", "captured_source_never_changes", state[0], before[0])
                audit.equal("E", "all_older_cells_are_retained", state[2][:len(before[2])], before[2])
                audit.equal("E", "exactly_one_fresh_cell_per_accepted_tick",
                            len(state[2]) - len(before[2]), int(expected_event != 0))
                snapshot = state
                reread = causal_event_read(state[0], state[1], language)
                audit.equal("E", "passive_read_is_idempotent", reread, reading)
                audit.equal("E", "passive_read_does_not_append_or_mutate", state, snapshot)
                if expected_event and first is None:
                    first = fresh_record(source, n % MODULUS)["record"]
                audit.equal("E", "first_hit_is_retained_oldest_cell", first_hit(state[2]), first)
                counts[reading.get("event")] += 1
                elapsed = n - n0 + 1
                cycles, remainder = divmod(elapsed, MODULUS)
                expected_counts = {label: cycles * prefix_counts[MODULUS][label] + prefix_counts[remainder][label]
                                   for label in (0, 1, 2)}
                audit.equal("E", "every_prefix_count_matches_exact_cycle_remainder_formula",
                            {label: counts[label] for label in (0, 1, 2)}, expected_counts,
                            (piston, start_phase, elapsed))
                if expected_event and state[2]:
                    written = state[2][-1]
                    descriptor, sign = slot_details(source, n % MODULUS)
                    audit.equal("E", "complete_accepted_record_payload", written,
                                (source, source, n % MODULUS, descriptor, sign, expected_event, 0, expected_event))
            audit.equal("E", "record_cycle_counts_match_all_source_census",
                        {"LOW": counts[1], "HIGH": counts[2], "SILENT": counts[0]}, census[piston])
            audit.equal("E", "fresh_record_count", len(state[2]), counts[1] + counts[2])
            unchanged, bad = observer_step(state, 2, language)
            audit.equal("E", "invalid_input_preserves_observer_state", unchanged, state)
            audit.equal("E", "invalid_input_has_ERROR_status", bad["status"], "ERROR")
            rows.append({"piston": piston, "start_phase": start_phase,
                         "first_hit": None if first is None else {"phase": first[2], "event": first[5]},
                         "retained_cells": len(state[2]), "LOW": counts[1], "HIGH": counts[2]})
    control = (1, 0, 0, 0)
    audit.equal("E", "phase_zero_schedule_LOW", slot_event(control, 0), 1)
    audit.equal("E", "phase_64_schedule_HIGH", slot_event(control, 64), 2)
    audit.results["conditional_fresh_record_protocol"] = {
        "alphabet": {0: "BLANK", 1: "LOW", 2: "HIGH"},
        "controlled_swaps": "BLANK<->LOW; BLANK<->HIGH; SILENT identity",
        "streams": rows, "stream_ticks": len(rows) * MODULUS,
        "initial_tick": "3072+start_phase; preceding 2560 literal native bits initialize the observer buffer",
        "first_hit": "oldest accepted cell; undefined before any acceptance; no extra sticky register",
        "record_payload": "captured source before/after, phase, fine slot, sign, outcome, old BLANK cell and written cell",
        "schedule_counterexample": "source(1,0,0,0): phase0-only invocations all LOW; phase64-only all HIGH",
        "scope": "fresh-cell permutation is reversible; append-only allocation and physical source/cell realization are separate premises",
    }


def qdd_low(piston):
    source = capture_source(piston)
    norm, total = sum(v * v for v in source), sum(source)
    return None if norm == 0 else Fraction(total * total, 4 * (5 * norm - total * total))


def signed_record(piston):
    return min(piston, tuple(-v % 5 for v in piston))


def audit_targets(audit, classes, census):
    # No target QDD value has been evaluated in any prior work package.
    targets = Counter(qdd_low(p) for p in product(range(5), repeat=4) if any(p))
    rows_by_type = {}
    class_type_counts = Counter()
    for history, sources in classes.items():
        sums = tuple(sorted({sum(p) % 5 for p in sources}))
        weights = Counter(qdd_low(p) for p in sources if any(p))
        complete_records = {signed_record(p) for p in sources}
        row = {"piston_sums": sums, "pistons": len(sources),
               "supported_pistons": sum(weights.values()),
               "complete_QDD_records": len(complete_records),
               "LOW_histogram": {str(w): weights[w] for w in sorted(weights)}}
        if sums in rows_by_type:
            audit.equal("F", "ready_independence_of_source_class_target_census", row, rows_by_type[sums], sums)
        else:
            rows_by_type[sums] = row
        class_type_counts[sums] += 1
        audit.equal("F", "QDD_LOW_not_constant_on_apparatus_source_class", len(weights) > 1, True, history)
    for ready in product(range(5), repeat=2):
        left, right = (1, 0, 0, 0) + ready, (2, 4, 0, 0) + ready
        audit.equal("F", "same_sum_different_QDD_sources_have_same_quotient", quotient(left), quotient(right), ready)
        audit.equal("F", "same_sum_LOW_left", qdd_low(left[:4]), Fraction(1, 16), ready)
        audit.equal("F", "same_sum_LOW_right", qdd_low(right[:4]), Fraction(1, 96), ready)
        zero, supported = (0, 0, 0, 0) + ready, (1, 4, 0, 0) + ready
        audit.equal("F", "zero_and_supported_have_same_quotient", quotient(zero), quotient(supported), ready)
        audit.equal("F", "zero_support_tag", qdd_low(zero[:4]), None, ready)
        audit.equal("F", "supported_control_LOW", qdd_low(supported[:4]), Fraction(0), ready)
    for piston, counts in census.items():
        value = qdd_low(piston)
        occupied = counts["LOW"] + counts["HIGH"]
        if value is None:
            audit.equal("F", "zero_support_constructor_has_no_accepted_event", occupied, 0, piston)
        else:
            audit.equal("F", "supported_source_has_accepted_events", occupied > 0, True, piston)
            observed = Fraction(counts["LOW"], occupied) if occupied else None
            audit.equal("F", "incidence_accepted_ratio_equals_QDD_only_after_construction", observed, value, piston)
    audit.equal("F", "all_supported_QDD_pistons", sum(targets.values()), 624)
    audit.equal("F", "all_supported_QDD_weight_values", len(targets), 22)
    audit.results["QDD_comparison_after_native_and_incidence_classification"] = {
        "native_source_class_types": [dict(rows_by_type[sums], classes=class_type_counts[sums])
                                       for sums in sorted(rows_by_type)],
        "supported_target_histogram": {str(w): targets[w] for w in sorted(targets)},
        "native_port": "every native observation source class contains different QDD values; even zero support is not generally observable",
        "conditional_constructor": "all 624 supported captured sources have the exact algebraic accepted ratio; zero source accepts nothing",
        "selection": "source capture, integer incidence, clock capture and fresh-cell allocation are disclosed design premises, not derived physical selection",
    }


def main():
    audit = Audit()
    exception = None
    try:
        audit_native_factor(audit)
        classes = audit_observability(audit)
        language = audit_phase(audit)
        census = audit_incidence(audit)
        audit_records(audit, language, census)
        audit_targets(audit, classes, census)
    except Exception as error:
        exception = {"type": type(error).__name__, "message": str(error)}
    complete = exception is None and all(audit.checks[group] for group in "ABCDEF")
    outcome = ("PASS" if not audit.failures else "FALSIFIED") if complete else "STOP"
    report = {"name": NAME, "status": "formal result-exposed proof audit", "layer": "L1",
              "outcome": outcome, "complete": complete, "checks_by_group": dict(audit.checks),
              "total_exact_checks": sum(audit.checks.values()), "mismatches": audit.failures,
              "first_mismatches": audit.examples, "exception": exception, "results": audit.results,
              "boundary": "native-port information boundary plus explicit conditional observer construction; no native apparatus, Born occurrence or physical decoder closure"}
    raw = json.dumps(json_value(report), sort_keys=True, ensure_ascii=True,
                     separators=(",", ":")).encode("ascii") + b"\n"
    sys.stdout.buffer.write(raw)
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
