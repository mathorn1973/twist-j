"""P-U-FINITE-HISTORY-EVENT-1: prospective, result-exposed exact proof audit.

Commit, push and publicly read back the complete accepted pin before execution.
This is a self-contained standard-library verifier: no runtime repository reads,
imports of other verifiers, random inputs, floats, network, or file writes.
Every finite enumeration audits an accompanying universal proof. Reader memory
is an explicit observation resource, not an added native apparatus or event law.
"""

from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache, reduce
from hashlib import sha256
from itertools import product
from math import gcd
import json
import sys


NAME = "P-U-FINITE-HISTORY-EVENT-1"
PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
TRIPLES = ((0, 0, 1), (0, 1, 0), (0, 1, 1),
           (1, 0, 0), (1, 0, 1), (1, 1, 0))
BALANCED = (0, 1, 2, -2, -1)


def theta(n):
    return n.bit_count() % 2


def switch_sum(m):
    value, sign = 0, 1
    while m:
        value += sign * m
        sign = -sign
        m //= 2
    return value


def next_power_two(n):
    return 1 << (n - 1).bit_length()


def phase_length(k):
    return 1 if k == 0 else 5 * (1 << (k - 1))


def phase_from_history(word, k):
    """Causal word is oldest-to-latest; output is its endpoint modulo 2**k."""
    if k == 0:
        return 0
    length = phase_length(k)
    if len(word) < length:
        raise ValueError("insufficient frozen causal history")
    word = word[-length:]
    parity = None
    for i in range(4):
        if word[length - 5 + i] == word[length - 4 + i]:
            parity = (1 + i) % 2
            break
    if parity is None:
        # A generated legal word with no recognized phase is a scientific
        # disagreement to retain, not a reason to abort the remaining audit.
        return -1
    if k == 1:
        return parity
    parent_length = phase_length(k - 1)
    parent = bytes(word[length - 1 - parity - 2 * j]
                   for j in reversed(range(parent_length)))
    parent_phase = phase_from_history(parent, k - 1)
    return -1 if parent_phase < 0 else parity + 2 * parent_phase


def recognized_cell(word, k):
    modulus = 1 << k
    if len(word) != 3 * modulus:
        raise ValueError("recognized cell requires exactly three block lengths")
    phase = phase_from_history(word, k)
    if phase < 0:
        return -1, ()
    parent = tuple(word[3 * modulus - 1 - phase - t * modulus] for t in (2, 1, 0))
    return phase, parent


def substitution_blocks(size):
    if size < 1 or size & (size - 1):
        raise ValueError("substitution size must be a positive power of two")
    zero = bytes((0,))
    while len(zero) < size:
        zero = bytes(v for bit in zero for v in (bit, 1 - bit))
    return zero, bytes(1 - bit for bit in zero)


def factor_contexts(length):
    """All parent pairs and all aligned offsets; no empirically selected sample."""
    size = next_power_two(length)
    blocks = substitution_blocks(size)
    for pair in PAIRS:
        expanded = blocks[pair[0]] + blocks[pair[1]]
        weight = 1 if pair[0] == pair[1] else 2
        for offset in range(size):
            yield expanded[offset:offset + length], offset, weight, pair


@lru_cache(maxsize=None)
def legal_words(length):
    if length < 1:
        raise ValueError("observer length must be positive")
    return frozenset(word for word, _, _, _ in factor_contexts(length))


def read_causal_phase(word, k):
    """Public reader: input is only the bounded current word and fixed k."""
    length = phase_length(k)
    if len(word) > length:
        return {"tag": "ERROR", "reason": "INVALID_LENGTH", "word": word}
    if any(bit not in (0, 1) for bit in word):
        return {"tag": "ERROR", "reason": "NONBINARY_WORD", "word": word}
    if len(word) < length:
        return {"tag": "UNAVAILABLE", "word": word}
    if word not in legal_words(length):
        return {"tag": "ERROR", "reason": "ILLEGAL_COMPLETE_WORD", "word": word}
    phase = phase_from_history(word, k)
    if phase < 0:
        return {"tag": "ERROR", "reason": "PHASE_NOT_RECOGNIZED", "word": word}
    return {"tag": "OBSERVED", "phase": phase, "word": word}


def capture_phase(word, bit, k):
    """One causal append/drop update; no clock or source-head argument."""
    if bit not in (0, 1):
        return word, {"tag": "ERROR", "reason": "NONBINARY_INPUT",
                      "word": word, "rejected_input": bit}
    following = (word + bytes((bit,)))[-phase_length(k):]
    return following, read_causal_phase(following, k)


def read_causal_event(word, k, a, b):
    """The complete event reader has fixed parameters and no counter input."""
    if not (0 <= a <= b <= 1 << k and b >= 1):
        raise ValueError("invalid fixed event-reader context")
    reading = read_causal_phase(word, k)
    if reading["tag"] != "OBSERVED":
        return reading
    return {"tag": "OBSERVED", "event": residue_event(reading["phase"], a, b),
            "word": word}


def native_generator(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        raw = (b, a, d, c, q, r)
    elif index == 1:
        raw = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        raw = (-c + 2, -d + 1 + r, -a + 2, -b + 1 - r, 1 - q, -r)
    elif index == 3:
        raw = (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r)
    elif index == 4:
        raw = (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r)
    else:
        raise ValueError("unknown native generator")
    return tuple(v % 5 for v in raw)


def native_step(x, bit):
    return native_generator((sum(x) + 2 * bit) % 5, x)


def clock_transition(c, digit):
    r, s, u, v = c
    if digit == 0:
        return (2 * r % 5, (2 * r - s) % 5, u, 1 - u)
    return ((2 * r + 1) % 5, (2 * r + 1 - s) % 5, 1 - u, v)


def clock_literal(m):
    return (m % 5, switch_sum(m) % 5, theta(m), theta(m + 1))


def distances(start, graph):
    result = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for target in graph[node]:
            if target not in result:
                result[target] = result[node] + 1
                queue.append(target)
    return result


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
                self.examples.append({"group": group, "claim": claim,
                                      "actual": actual, "expected": expected,
                                      "context": context})


def dyadic_thirds(value):
    denominator = value.denominator
    while denominator % 2 == 0:
        denominator //= 2
    return denominator in (1, 3)


def factor_summary(counts, denominator):
    digest = sha256()
    histogram = Counter()
    for word, count in sorted(counts.items()):
        weight = Fraction(count, denominator)
        histogram[weight] += 1
        digest.update((word.hex() + ":" + str(weight.numerator) + "/" +
                       str(weight.denominator) + "\n").encode("ascii"))
    return {"distinct_factors": len(counts),
            "atom_weight_histogram": {str(w): histogram[w] for w in sorted(histogram)},
            "factor_frequency_table_sha256": digest.hexdigest()}


def audit_phase_factors(audit):
    rows = []
    contexts = 0
    for k in range(1, 9):
        length, modulus = phase_length(k), 1 << k
        block_size = next_power_two(length)
        zero, one = substitution_blocks(block_size)
        audit.equal("A", "substitution_equals_literal_TM",
                    zero, bytes(theta(n) for n in range(block_size)), k)
        audit.equal("A", "substitution_complement", one, bytes(1 - b for b in zero), k)
        atoms, phase_counts = Counter(), Counter()
        for word, offset, weight, pair in factor_contexts(length):
            expected = (offset + length - 1) % modulus
            observed = phase_from_history(word, k)
            context = (k, pair, offset)
            audit.equal("A", "causal_endpoint_phase_on_every_context", observed, expected, context)
            atoms[word] += weight
            phase_counts[observed] += weight
            # A synchronized z_n equals 4-3*theta_(n-1). The native present
            # time is therefore one later than the endpoint of this word.
            z_word = bytes(4 - 3 * bit for bit in word)
            decoded = bytes((4 - z) // 3 for z in z_word)
            audit.equal("D", "native_phase_history_roundtrip", decoded, word, context)
            audit.equal("D", "native_current_time_phase_plus_one",
                        (phase_from_history(decoded, k) + 1) % modulus,
                        (offset + length) % modulus, context)
            contexts += 1
        denominator = 6 * block_size
        audit.equal("A", "factor_frequency_total", sum(atoms.values()), denominator, k)
        audit.equal("A", "all_residue_classes_recognized", sorted(phase_counts), list(range(modulus)), k)
        for phase in range(modulus):
            audit.equal("A", "uniform_recognized_residue_frequency",
                        phase_counts[phase] * modulus, denominator, (k, phase))
        for word, count in atoms.items():
            audit.equal("B", "every_phase_window_atom_is_dyadic_third",
                        dyadic_thirds(Fraction(count, denominator)), True, (k, word))
        rows.append(dict({"k": k, "history_length": length, "modulus": modulus,
                          "parent_block_length": block_size, "contexts": 4 * block_size},
                         **factor_summary(atoms, denominator)))
    audit.equal("A", "registered_phase_context_count", contexts, 8160)
    audit.results["causal_phase_decoder"] = {
        "contexts": contexts, "rows": rows,
        "orientation": "history oldest-to-latest; residue of latest bit index",
        "history_640": "sufficient for phase modulo 256; no minimality claim",
    }


def audit_uniform_partitions(audit):
    rows = []
    contexts = 0
    for k in range(9):
        modulus = 1 << k
        length = 3 * modulus
        block_size = next_power_two(length)
        denominator = 6 * block_size
        blocks = substitution_blocks(block_size)
        audit.equal("B", "uniform_substitution_equals_literal_TM", blocks[0],
                    bytes(theta(n) for n in range(block_size)), k)
        audit.equal("B", "uniform_substitution_complement", blocks[1],
                    bytes(1 - bit for bit in blocks[0]), k)
        atoms, cells = Counter(), Counter()
        for word, offset, weight, pair in factor_contexts(length):
            cell = recognized_cell(word, k)
            audit.equal("B", "uniform_window_phase", cell[0],
                        (offset + length - 1) % modulus, (k, pair, offset))
            audit.equal("B", "recognized_parent_triple_is_legal", cell[1] in TRIPLES,
                        True, (k, pair, offset))
            atoms[word] += weight
            cells[cell] += weight
            contexts += 1
        expected_cells = tuple(product(range(modulus), TRIPLES))
        audit.equal("B", "complete_recognized_cell_set", sorted(cells), sorted(expected_cells), k)
        audit.equal("B", "uniform_window_frequency_total", sum(atoms.values()), denominator, k)
        for cell in expected_cells:
            audit.equal("B", "all_6M_cells_have_exact_equal_frequency",
                        cells[cell] * 6 * modulus, denominator, (k, cell))
        numerator = 0
        audit.equal("B", "zero_cell_prefix_weight", numerator, 0, k)
        for index, cell in enumerate(expected_cells, 1):
            numerator += cells[cell]
            audit.equal("B", "every_prefix_of_canonical_cell_order_realizes_grid",
                        numerator * 6 * modulus, index * denominator, (k, index))
        for word, count in atoms.items():
            audit.equal("B", "every_uniform_window_atom_is_dyadic_third",
                        dyadic_thirds(Fraction(count, denominator)), True, (k, word))
        rows.append(dict({"k": k, "history_length": length,
                          "recognized_cells": len(cells),
                          "cell_weight": Fraction(1, 6 * modulus),
                          "contexts": 4 * block_size}, **factor_summary(atoms, denominator)))
    audit.equal("B", "registered_uniform_context_count", contexts, 8176)
    audit.results["clock_only_spectrum"] = {
        "contexts": contexts, "rows": rows,
        "unconditional_union": "Z[1/2]/3 intersect [0,1]",
        "accepted_ratio_union": "Q intersect [0,1]",
        "universal_basis": "CLOCK-PROOF.md; every factor is a parent-pair cylinder sum; uniform 6M partitions exhaust the dyadic-thirds grids",
        "scope": "finite TM history only; checkpoint readers are outside this spectrum claim",
    }


def residue_event(phase, a, b):
    if phase < a:
        return "LOW"
    if phase < b:
        return "HIGH"
    return "SILENT"


def audit_residue_templates(audit):
    templates = {}
    pairs = 0
    phase_allocations = 0
    for b in range(1, 257):
        modulus = next_power_two(b)
        for a in range(b + 1):
            counts = Counter(residue_event(phase, a, b) for phase in range(modulus))
            audit.equal("C", "target_independent_template_LOW_count", counts["LOW"], a, (a, b))
            audit.equal("C", "target_independent_template_HIGH_count", counts["HIGH"], b - a, (a, b))
            audit.equal("C", "target_independent_template_SILENT_count", counts["SILENT"], modulus - b, (a, b))
            accepted = counts["LOW"] + counts["HIGH"]
            audit.equal("C", "template_acceptance_is_nonempty", accepted > 0, True, (a, b))
            value = Fraction(counts["LOW"], accepted)
            audit.equal("C", "exact_accepted_template_ratio", value, Fraction(a, b), (a, b))
            if gcd(a, b) == 1:
                templates[value] = {"a": a, "b": b, "modulus": modulus,
                                    "phase_history_length": phase_length(modulus.bit_length() - 1),
                                    "LOW_mass": Fraction(a, modulus),
                                    "HIGH_mass": Fraction(b - a, modulus),
                                    "acceptance_mass": Fraction(b, modulus)}
            pairs += 1
            phase_allocations += modulus
    audit.equal("C", "registered_template_parameter_count", pairs, 33152)
    audit.results["target_independent_event_family"] = {
        "parameter_pairs": pairs, "phase_allocations": phase_allocations,
        "distinct_reduced_ratios": len(templates),
        "rule": "LOW if residue<a; HIGH if a<=residue<b; SILENT otherwise",
        "parameters": "all integers 0<=a<=b, b>=1; finite audit b<=256",
        "empty_acceptance": "undefined for a general reader accepting no cell; excluded from ratios",
        "physical_selection": "none; all family parameters precede QDD comparison",
    }
    return templates


def audit_native_phase(audit):
    stable = 0
    for x in product(range(5), repeat=6):
        z = sum(x) % 5
        if z not in (1, 4):
            continue
        stable += 1
        for bit in (0, 1):
            y = native_step(x, bit)
            audit.equal("D", "native_phase_encodes_previous_driver_bit",
                        sum(y) % 5, 4 - 3 * bit, (x, bit))
    audit.equal("D", "complete_stable_checkpoint_count", stable, 6250)
    audit.results["native_history_bridge"] = {
        "checkpoints": stable, "driver_choices": 2,
        "identity": "z_n=4-3*theta_(n-1) after synchronization",
        "clock_shift": "+1 modulo M after decoding the z-history endpoint",
        "resource": "finite observation history; no claim the native checkpoint stores it",
    }


def audit_primitive_clock(audit):
    origin = (0, 0, 0, 1)
    graph, queue = {}, deque([origin])
    while queue:
        c = queue.popleft()
        if c in graph:
            continue
        graph[c] = tuple(clock_transition(c, digit) for digit in (0, 1))
        queue.extend(target for target in graph[c] if target not in graph)
    reverse = {c: [] for c in graph}
    weights = {c: 1 if c[2] == c[3] else 2 for c in graph}
    incoming = Counter()
    for c, targets in graph.items():
        for target in targets:
            reverse[target].append(c)
            incoming[target] += weights[c]
    audit.equal("E", "complete_reachable_clock", len(graph), 100)
    audit.equal("E", "origin_zero_digit_loop", graph[origin][0], origin)
    outward, inward = distances(origin, graph), distances(origin, reverse)
    audit.equal("E", "clock_strong_connectivity", len(inward), len(graph))
    period = reduce(gcd, (abs(outward[x] + 1 - outward[y])
                          for x in graph for y in graph[x]), 0)
    audit.equal("E", "clock_period", period, 1)
    for c in sorted(graph):
        audit.equal("E", "stationary_integer_vector", incoming[c], 2 * weights[c], c)
    audit.equal("E", "stationary_denominator", sum(weights.values()), 150)
    pair_counts = Counter()
    for c, weight in weights.items():
        pair_counts[c[2:]] += weight
    for pair in PAIRS:
        audit.equal("E", "parent_pair_density_used_for_factor_enumeration",
                    Fraction(pair_counts[pair], 150),
                    Fraction(1 if pair[0] == pair[1] else 2, 6), pair)
    literal_switches = 0
    for m in range(65536):
        if m:
            literal_switches += int(theta(m) != theta(m - 1))
        audit.equal("E", "literal_switch_recurrence", switch_sum(m), literal_switches, m)
        for digit in (0, 1):
            audit.equal("E", "literal_clock_recursion",
                        clock_transition(clock_literal(m), digit), clock_literal(2 * m + digit),
                        (m, digit))
    if len(inward) != len(graph):
        audit.results["primitive_native_clock"] = {
            "states": len(graph), "primitive_certificate": "NOT_ESTABLISHED"}
        return
    power = max(outward.values()) + max(inward.values())
    minimum = None
    for start in sorted(graph):
        counts = {start: 1}
        for _ in range(power):
            following = Counter()
            for c, count in counts.items():
                for target in graph[c]:
                    following[target] += count
            counts = following
        row_minimum = min(counts.get(c, 0) for c in graph)
        minimum = row_minimum if minimum is None else min(minimum, row_minimum)
        audit.equal("E", "positive_integer_substitution_power", row_minimum > 0, True, start)
        audit.equal("E", "substitution_power_row_total", sum(counts.values()), 2 ** power, start)
    audit.results["primitive_native_clock"] = {
        "states": len(graph), "period": period, "primitive_power": power,
        "minimum_integer_power_entry": minimum, "power_row_sum": 2 ** power,
        "contraction_factor": Fraction(2 ** power - len(graph) * minimum, 2 ** power),
        "literal_clock_audit": [0, 65535],
        "stationary_weights": "1/150 for equal bits; 2/150 for unequal bits",
        "finite_history_recurrence": "MEMORY-PROOF.md; primitive substitution recurrence transported through inherited native chart",
    }


def audit_observer_buffer(audit):
    captured_bits = 0
    complete_reads = 0
    warmup_reads = 0
    for k in range(9):
        length, modulus = phase_length(k), 1 << k
        event_a, event_b = modulus // 3, max(1, modulus - 1)
        word = b""
        audit.equal("F", "buffer_initialization", read_causal_phase(word, k),
                    {"tag": "UNAVAILABLE", "word": b""}, k)
        for n in range(length + 2 * modulus):
            before = word
            word, reading = capture_phase(word, theta(n), k)
            reference = bytes(theta(j) for j in range(max(0, n - length + 1), n + 1))
            audit.equal("F", "causal_buffer_complete_ordered_word", word, reference, (k, n))
            audit.equal("F", "buffer_only_appends_then_drops_oldest",
                        word, (before + bytes((theta(n),)))[-length:], (k, n))
            audit.equal("F", "buffer_fill_length", len(word), min(length, n + 1), (k, n))
            audit.equal("F", "read_is_only_function_of_current_bounded_word",
                        reading, read_causal_phase(bytes(word), k), (k, n))
            if n < length - 1:
                audit.equal("F", "warmup_never_emits_event", reading["tag"], "UNAVAILABLE", (k, n))
                warmup_reads += 1
            else:
                audit.equal("F", "complete_native_window_is_valid", reading["tag"], "OBSERVED", (k, n))
                audit.equal("F", "streamed_phase_without_counter_input",
                            reading.get("phase"), n % modulus, (k, n))
                complete_reads += 1
            event_reading = read_causal_event(word, k, event_a, event_b)
            if n < length - 1:
                audit.equal("F", "event_wrapper_preserves_warmup", event_reading["tag"],
                            "UNAVAILABLE", (k, n))
            else:
                audit.equal("F", "causal_event_wrapper_matches_fixed_template",
                            event_reading.get("event"),
                            residue_event(n % modulus, event_a, event_b), (k, n))
            captured_bits += 1
        for rejected in (-1, 2, None, "0"):
            unchanged, reading = capture_phase(word, rejected, k)
            audit.equal("F", "nonbinary_capture_preserves_buffer", unchanged, word, (k, rejected))
            audit.equal("F", "nonbinary_capture_is_ERROR", reading["tag"], "ERROR", (k, rejected))
            audit.equal("F", "rejected_input_is_retained", reading.get("rejected_input"), rejected, (k, rejected))
        invalid = bytes((2,)) * length
        audit.equal("F", "nonbinary_complete_word_is_ERROR",
                    read_causal_phase(invalid, k)["tag"], "ERROR", k)
        for invalid in (bytes((0,)) * length, bytes((1,)) * length):
            if k:
                reading = read_causal_phase(invalid, k)
                audit.equal("F", "illegal_complete_clock_word_is_ERROR", reading["tag"], "ERROR", (k, invalid))
                audit.equal("F", "illegal_complete_word_evidence_retained", reading["word"], invalid, (k, invalid))
                audit.equal("F", "event_wrapper_rejects_illegal_complete_words",
                            read_causal_event(invalid, k, event_a, event_b)["tag"], "ERROR", (k, invalid))
        audit.equal("F", "overlength_word_is_ERROR",
                    read_causal_phase(word + bytes((0,)), k)["tag"], "ERROR", k)
    # Complete validation of the smallest nontrivial reader language, rather
    # than testing only a few selected rejected words.
    for values in product((0, 1), repeat=phase_length(1)):
        word = bytes(values)
        expected = "OBSERVED" if word in legal_words(phase_length(1)) else "ERROR"
        audit.equal("F", "all_32_length_five_binary_words_validated",
                    read_causal_phase(word, 1)["tag"], expected, word)
    audit.equal("F", "buffer_equality_is_order_sensitive", bytes((0, 1)) == bytes((1, 0)), False)
    audit.results["observer_resource_contract"] = {
        "levels": [0, 8], "capture_length_per_level": "L_k+2*2**k; L_0=1",
        "captured_bits": captured_bits, "complete_reads": complete_reads,
        "warmup_reads": warmup_reads, "length_five_validation_domain": 32,
        "state": "ordered binary word of length at most L; initially empty",
        "update": "append one supplied bit; drop oldest when full; no clock input",
        "validation": "complete exact substitution-factor language; ERROR retains rejected evidence",
        "event_wrapper_test_context": "a=floor(M/3), b=max(1,M-1), fixed before any QDD comparison",
        "feeds_U": False, "physical_realization": "not supplied",
    }


def qdd_low(pistons):
    balanced = tuple(BALANCED[v] for v in pistons)
    norm, total = sum(v * v for v in balanced), sum(balanced)
    if norm == 0:
        return None
    return Fraction(total * total, 4 * (5 * norm - total * total))


def audit_qdd_comparison_and_loss(audit, templates):
    # The target-independent family and its complete parameter audit above
    # have finished before the first QDD head or target is evaluated here.
    targets = Counter(qdd_low(p) for p in product(range(5), repeat=4) if any(p))
    rows = []
    for target in sorted(targets):
        audit.equal("F", "supported_QDD_weight_in_frozen_template_family", target in templates,
                    True, target)
        rows.append(dict({"LOW": target, "supported_pistons": targets[target],
                          "supported_heads": 25 * targets[target]},
                         **templates.get(target, {"template": "ABSENT"})))
    audit.equal("F", "complete_supported_piston_domain", sum(targets.values()), 624)
    audit.equal("F", "inherited_QDD_weight_count", len(targets), 22)
    audit.equal("F", "inherited_denominator_ceiling", max(p.denominator for p in targets), 256)
    audit.equal("F", "known_denominator_256_template_history",
                templates.get(Fraction(1, 256), {}).get("phase_history_length"), 640)
    left, right = (4, 1, 0, 0, 0, 0), (2, 1, 1, 2, 1, 0)
    common = (1, 4, 0, 0, 0, 0)
    audit.equal("F", "original_native_merger_left", native_step(left, 0), common)
    audit.equal("F", "original_native_merger_right", native_step(right, 0), common)
    audit.equal("F", "different_erased_original_LOW_left", qdd_low(left[:4]), Fraction(0))
    audit.equal("F", "different_erased_original_LOW_right", qdd_low(right[:4]), Fraction(9, 14))
    audit.results["QDD_comparison_only_after_family_freeze"] = {
        "supported_pistons": sum(targets.values()), "supported_heads": 25 * sum(targets.values()),
        "distinct_targets": len(targets), "rows": rows,
        "comparison": "all 22 weights occur as family parameters; no physical parameter selector or shared head-to-parameter map is supplied",
    }
    audit.results["original_record_and_writing_boundary"] = {
        "merging_heads": [left, right], "common_tick_one_state": common,
        "erased_original_LOW": [Fraction(0), Fraction(9, 14)],
        "finite_history": "a window wholly after merging cannot restore the lost distinction",
        "permanent_writing": "recurrence excludes an eventually constant finite-history reader that changed value after its synchronized valid-history domain began",
        "finite_retention_or_reset": "not excluded generally; no endogenous implementation claimed",
    }


def main():
    audit = Audit()
    exception = None
    try:
        audit_phase_factors(audit)
        audit_uniform_partitions(audit)
        templates = audit_residue_templates(audit)
        audit_native_phase(audit)
        audit_primitive_clock(audit)
        audit_observer_buffer(audit)
        audit_qdd_comparison_and_loss(audit, templates)
    except Exception as error:
        exception = {"type": type(error).__name__, "message": str(error)}
    complete = exception is None and all(audit.checks[group] for group in "ABCDEF")
    outcome = ("PASS" if audit.failures == 0 else "FALSIFIED") if complete else "STOP"
    report = {
        "name": NAME, "status": "formal result-exposed proof audit", "action_layer": "L1",
        "outcome": outcome, "complete": complete, "checks_by_group": dict(audit.checks),
        "total_exact_checks": sum(audit.checks.values()), "mismatches": audit.failures,
        "first_mismatches": audit.examples, "exception": exception, "results": audit.results,
        "boundaries": "finite observation memory and rate realization do not supply native writing, physical parameter selection, an exclusive event law, or decoder closure",
    }
    raw = json.dumps(json_value(report), ensure_ascii=True, sort_keys=True,
                     separators=(",", ":")).encode("ascii") + b"\n"
    sys.stdout.buffer.write(raw)
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
