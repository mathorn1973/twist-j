"""Exact proof audit for P-U-FINITE-READER-INDEPENDENCE-1.

NO EXECUTION BEFORE PUBLIC IMMUTABLE PIN AND BYTE READBACK.
Self-contained standard library; no data access, random sampling or floats.
A completed mathematical disagreement is retained with exit 0; an exception
is an incomplete STOP, not evidence against a mathematical or physical law.
"""

from collections import Counter, deque
from functools import lru_cache
from itertools import product
import hashlib
import json


NAME = "P-U-FINITE-READER-INDEPENDENCE-1"
ALPHABET = tuple(product(range(5), range(5), range(2), range(2)))
ORIGIN = (0, 0, 0, 1)
ORDERS = (1, 2, 3, 4, 8, 12)
SILENT = 2


class Audit:
    def __init__(self):
        self.counts = Counter()
        self.failures = []

    def check(self, group, condition, witness):
        self.counts[group] += 1
        if not condition:
            self.failures.append([group, witness])


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def theta(n):
    return n.bit_count() % 2


def switch_sum(m):
    total, sign = 0, 1
    while m:
        total += sign * m
        m //= 2
        sign = -sign
    return total


def clock(m):
    return m % 5, switch_sum(m) % 5, theta(m), theta(m + 1)


def transition(c, digit):
    r, s, u, v = c
    if digit == 0:
        return 2 * r % 5, (2 * r - s) % 5, u, 1 - u
    return (2 * r + 1) % 5, (2 * r + 1 - s) % 5, 1 - u, v


def native_step(n, x):
    a, b, c, d, q, r = x
    index = (sum(x) + 2 * theta(n)) % 5
    if index == 0:
        raw = b, a, d, c, q, r
    elif index == 1:
        raw = -c, -d, -a, -b, -q, -r
    elif index == 2:
        raw = -c + 2, -d + 1 + r, -a + 2, -b + 1 - r, 1 - q, -r
    elif index == 3:
        raw = 2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r
    else:
        raw = 2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r
    return tuple(v % 5 for v in raw)


def decode(n, x):
    a, b, c, d, _, r = x
    t = 1 if n % 2 else -1
    h = 1 if (n + theta(n - 1)) % 2 == 0 else -1
    offset = switch_sum((n - 1) // 2) - 1
    return tuple(v % 5 for v in
                 (t * (a + c), t * (b + d), h * (a - c - 2),
                  h * (b - d - 1), t * r - offset))


def encode(n, label):
    t = 1 if n % 2 else -1
    h = 1 if (n + theta(n - 1)) % 2 == 0 else -1
    offset = switch_sum((n - 1) // 2) - 1
    alpha, beta, gamma, delta, epsilon = label
    a, b, c, d = t * alpha, t * beta, 2 + h * gamma, 1 + h * delta
    r = t * (epsilon + offset)
    z = 4 - 3 * theta(n - 1)
    return tuple(v % 5 for v in
                 (3 * (a + c), 3 * (b + d), 3 * (a - c), 3 * (b - d),
                  z - a - b - r, r))


def morphism(c, label, parity):
    _, s, u, v = c
    t = 1 if parity else -1
    h = -1 if u == 0 else 1
    z = 4 - 3 * u if parity else 1 + 3 * u
    bit = 1 - u if parity else v
    alpha, beta, gamma, delta, epsilon = label
    a, b, cc, d = t * alpha, t * beta, 2 + h * gamma, 1 + h * delta
    r = t * (epsilon + s - 1)
    x = tuple(w % 5 for w in
              (3 * (a + cc), 3 * (b + d), 3 * (a - cc), 3 * (b - d),
               z - a - b - r, r))
    return x, bit


def audit_native(audit):
    labels = set()
    for head in product(range(5), repeat=6):
        x = head
        label = None
        for n in range(12):
            if n == 3:
                label = decode(n, x)
                labels.add(label)
            if n >= 3:
                audit.check("native", encode(n, label) == x, [head, n, "chart"])
                audit.check("native", morphism(clock((n - 1) // 2), label,
                                               n % 2) == (x, theta(n)),
                            [head, n, "morphism"])
            x = native_step(n, x)
    audit.check("native", len(labels) == 3125, ["chart_count", len(labels)])
    return {"origin_zero_heads": 15625, "last_compared_tick": 11,
            "synchronized_charts": len(labels), "counter": "unbounded native n"}


def substitution_entry(root, depth, offset):
    c = root
    for position in range(depth - 1, -1, -1):
        c = transition(c, (offset >> position) & 1)
    return c


def audit_clock(audit):
    audit.check("clock", transition(ORIGIN, 0) == ORIGIN, "prolongable_origin")
    for m in range(4096):
        for digit in (0, 1):
            audit.check("clock", transition(clock(m), digit) == clock(2 * m + digit),
                        ["literal_recurrence", m, digit])
    for root in ALPHABET:
        reachable = {root}
        for _ in range(77):
            reachable = {transition(c, digit) for c in reachable for digit in (0, 1)}
        audit.check("clock", reachable == set(ALPHABET), ["primitive_77", root])

    # Every internal pair is legal since all clock letters are reachable.
    # A boundary pair is legal by applying sigma to a previously legal pair.
    # The certificate tracks a pair inside sigma**depth(root), by offset.
    witnesses = {}
    pending = deque()
    for root in ALPHABET:
        pair = transition(root, 0), transition(root, 1)
        if pair not in witnesses:
            witnesses[pair] = root, 1, 0
            pending.append(pair)
    while pending:
        pair = pending.popleft()
        root, depth, offset = witnesses[pair]
        child = transition(pair[0], 1), transition(pair[1], 0)
        if child not in witnesses:
            witnesses[child] = root, depth + 1, 2 * offset + 1
            pending.append(child)
    for pair, (root, depth, offset) in sorted(witnesses.items()):
        found = (substitution_entry(root, depth, offset),
                 substitution_entry(root, depth, offset + 1))
        audit.check("clock", found == pair, ["pair_witness", pair, root, depth, offset])
        audit.check("clock", (transition(pair[0], 1), transition(pair[1], 0)) in witnesses,
                    ["pair_closed", pair])
    literal = tuple(clock(m) for m in range(4096))
    for i in range(len(literal) - 1):
        audit.check("clock", (literal[i], literal[i + 1]) in witnesses, ["pair_cover", i])
    return {"alphabet_size": 100, "primitive_power": 77,
            "complete_legal_pairs": len(witnesses),
            "largest_pair_certificate_depth": max(item[1] for item in witnesses.values()),
            "pair_certificate_sha256": digest(sorted(witnesses.items())),
            "literal_prefix_is_not_completeness_evidence": True}


@lru_cache(maxsize=None)
def tm_image(letter, depth):
    word = (letter,)
    for _ in range(depth):
        word = tuple(v for a in word for v in (a, 1 - a))
    return word


@lru_cache(maxsize=None)
def tm_language(length):
    depth = (length - 1).bit_length()
    size = 1 << depth
    words = set()
    for a, b in product((0, 1), repeat=2):
        doubled = tm_image(a, depth) + tm_image(b, depth)
        for offset in range(size):
            words.add(doubled[offset:offset + length])
    return tuple(sorted(words))


def apply_reader(word, width, table):
    if width == 1:
        return tuple(table[a] for a in word)
    return tuple(table[2 * word[i] + word[i + 1]] for i in range(len(word) - 1))


def accepted(word):
    return tuple(a for a in word if a != SILENT)


def block_set(word, length):
    return {word[i:i + length] for i in range(len(word) - length + 1)}


def audit_readers(audit):
    direct_bits = tuple(theta(n) for n in range(8192))
    audit.check("language", direct_bits == tm_image(0, 13), "literal_vs_substitution")
    for a in (0, 1):
        audit.check("language", block_set(tm_image(a, 3), 2) == set(product((0, 1), repeat=2)),
                    ["all_pairs_in_eight_block", a])
    lengths = {16 + width - 1 for width in (1, 2)}
    lengths |= {width + 16 * (k - 1) for width in (1, 2) for k in ORDERS}
    for length in sorted(lengths):
        exact = set(tm_language(length))
        audit.check("language", exact == block_set(direct_bits, length), ["factor_equality", length])
        audit.check("language", len(exact) <= 8 * length, ["binary_linear_bound", length, len(exact)])

    rows = []
    no_event = 0
    for width in (1, 2):
        for table in product((0, 1, SILENT), repeat=2 ** width):
            if all(value == SILENT for value in table):
                no_event += 1
                audit.check("readers", not accepted(apply_reader(direct_bits, width, table)),
                            ["empty", width, table])
                continue
            for word in tm_language(width + 15):
                audit.check("readers", bool(accepted(apply_reader(word, width, table))),
                            ["gap_16", width, table, word])
            direct_output = accepted(apply_reader(direct_bits, width, table))
            supports = []
            for k in ORDERS:
                length = width + 16 * (k - 1)
                support = set()
                for word in tm_language(length):
                    outputs = apply_reader(word, width, table)
                    if outputs[0] != SILENT:
                        retained = accepted(outputs)
                        audit.check("readers", len(retained) >= k,
                                    ["k_inside_span", width, table, k, word])
                        if len(retained) >= k:
                            support.add(retained[:k])
                observed = block_set(direct_output, k)
                audit.check("readers", support == observed,
                            ["accepted_support_equality", width, table, k])
                audit.check("readers", len(support) <= 8 * length,
                            ["accepted_linear_bound", width, table, k, len(support)])
                supports.append([k, len(support), digest(sorted(support))])
                if k == 12:
                    audit.check("readers", len(support) < 2 ** k,
                                ["missing_word_exists", width, table])
                    missing = next((word for word in product((0, 1), repeat=k)
                                    if word not in support), None)
                    audit.check("readers", missing is not None and missing not in observed,
                                ["missing_word_independent_readback", width, table, missing])
            rows.append([width, table, supports, missing])
    return {"tables": 90, "no_event_tables": no_event, "active_tables": len(rows),
            "common_certified_gap": 16, "accepted_orders": ORDERS,
            "missing_word_order": 12, "complete_reader_table_sha256": digest(rows),
            "whole_native_reader_class_exhausted": False}


def de_bruijn(order):
    mask = (1 << (order - 1)) - 1
    next_edge = [0] * (1 << (order - 1))
    vertices, edges, reverse = [0], [], []
    while vertices:
        vertex = vertices[-1]
        if next_edge[vertex] < 2:
            bit = next_edge[vertex]
            next_edge[vertex] += 1
            vertices.append(((vertex << 1) | bit) & mask)
            edges.append(bit)
        else:
            vertices.pop()
            if edges:
                reverse.append(edges.pop())
    return tuple(reversed(reverse))


def cyclic_counts(word, length):
    return Counter(tuple(word[(i + j) % len(word)] for j in range(length))
                   for i in range(len(word)))


def phase_table(length, modulus, audit):
    depth = max((length - 1).bit_length(), modulus.bit_length() - 1)
    size = 1 << depth
    table = {}
    for a, b in product((0, 1), repeat=2):
        doubled = tm_image(a, depth) + tm_image(b, depth)
        for offset in range(size):
            word = doubled[offset:offset + length]
            phase = (offset + length - 1) % modulus
            audit.check("horizons", word not in table or table[word] == phase,
                        ["phase_unique", length, modulus, offset, a, b])
            table[word] = phase
    audit.check("horizons", set(table.values()) == set(range(modulus)),
                ["all_phases", length, modulus])
    return table


def audit_horizons(audit):
    rows = []
    for h in range(1, 9):
        modulus = 1 << h
        length = 5 * (1 << (h - 1))
        cycle = de_bruijn(h)
        audit.check("horizons", len(cycle) == modulus, ["cycle_length", h])
        for j in range(1, h + 1):
            counts = cyclic_counts(cycle, j)
            expected = 1 << (h - j)
            audit.check("horizons", set(counts) == set(product((0, 1), repeat=j)),
                        ["complete_support", h, j])
            audit.check("horizons", set(counts.values()) == {expected},
                        ["exact_product_frequency", h, j])
        larger = cyclic_counts(cycle, h + 1)
        audit.check("horizons", len(larger) == modulus < 1 << (h + 1),
                    ["next_order_failure", h])
        phases = phase_table(length, modulus, audit)
        bits = tuple(theta(n) for n in range(length + 3 + 2 * modulus))
        for n in range(length + 2, length + 2 + 2 * modulus):
            word = bits[n - length + 1:n + 1]
            audit.check("horizons", phases.get(word) == n % modulus,
                        ["actual_counter_phase", h, n])
            if word in phases:
                audit.check("horizons", cycle[phases[word]] == cycle[n % modulus],
                            ["native_finite_window_output", h, n])
        rows.append({"horizon": h, "window": length, "phase_contexts": len(phases),
                     "period": modulus, "cycle_sha256": digest(cycle)})
    return {"rows": rows, "all_orders_at_once": False,
            "minimum_window_claim": False, "physical_trial_law": "NOT_SUPPLIED"}


def main():
    audit = Audit()
    result = {"probe": NAME, "native": audit_native(audit),
              "clock": audit_clock(audit), "finite_reader_audit": audit_readers(audit),
              "finite_horizon_positive_controls": audit_horizons(audit)}
    result.update({"status": "FALSIFIED" if audit.failures else "PROOF_AUDIT_PASS",
                   "exact_checks": dict(sorted(audit.counts.items())),
                   "total_exact_checks": sum(audit.counts.values()),
                   "failures": audit.failures,
                   "universal_evidence": "PROOF.md, not finite enumeration",
                   "physical_occurrence": "STOP_DEFINITION",
                   "canon": "UNCHANGED"})
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
