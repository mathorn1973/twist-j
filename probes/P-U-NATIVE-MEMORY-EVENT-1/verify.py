"""Formal result-exposed proof audit for P-U-NATIVE-MEMORY-EVENT-1.

This self-contained standard-library verifier must be committed and publicly
pushed before execution. No source import, external data, floating point,
random sample, physical measure, or selected physical reading is used.
Scientific disagreements are retained as FALSIFIED; implementation failures
are STOP. Frequency classification precedes construction of the QDD targets.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd
import json
import sys


NAME = "P-U-NATIVE-MEMORY-EVENT-1"
BALANCED = (0, 1, 2, -2, -1)


def neg(values):
    return tuple(-v % 5 for v in values)


def theta(n):
    return n.bit_count() % 2


def switch_sum(m):
    total, sign = 0, 1
    while m:
        total += sign * m
        m //= 2
        sign = -sign
    return total


def generator(index, x):
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
        raise ValueError("generator outside frozen domain")
    return tuple(v % 5 for v in raw)


def step_bit(x, bit):
    return generator((sum(x) + 2 * bit) % 5, x)


def record_vector(x):
    a, b, c, d, _, _ = x
    z = sum(x) % 5
    if z not in (1, 4):
        raise ValueError("record evaluated outside X14")
    chi = 1 if z == 1 else -1
    return tuple(v % 5 for v in (a + c, b + d, chi * (a - c - 2),
                                chi * (b - d - 1)))


def record(x):
    v = record_vector(x)
    return min(v, neg(v))


def record_encode(v):
    """Target-independent static codebook: z=1, r=0, one sign representative."""
    a, b, gamma, delta = v
    c, d = 2 + gamma, 1 + delta
    return tuple(t % 5 for t in (3 * (a + c), 3 * (b + d),
                                3 * (a - c), 3 * (b - d), 1 - a - b, 0))


def encode_time(n, label):
    t = 1 if n % 2 else -1
    h = 1 if (n + theta(n - 1)) % 2 == 0 else -1
    offset = switch_sum((n - 1) // 2) - 1
    z = 4 - 3 * theta(n - 1)
    alpha, beta, gamma, delta, epsilon = label
    a, b = t * alpha, t * beta
    c, d = 2 + h * gamma, 1 + h * delta
    r = t * (epsilon + offset)
    return tuple(v % 5 for v in (3 * (a + c), 3 * (b + d),
                                3 * (a - c), 3 * (b - d), z - a - b - r, r))


def clock_transition(c, digit):
    r, s, u, v = c
    if digit == 0:
        return (2 * r % 5, (2 * r - s) % 5, u, 1 - u)
    return ((2 * r + 1) % 5, (2 * r + 1 - s) % 5, 1 - u, v)


def clock_literal(m):
    return (m % 5, switch_sum(m) % 5, theta(m), theta(m + 1))


def clock_from_digits(m):
    c = (0, 0, 0, 1)
    for digit in bin(m)[2:]:
        c = clock_transition(c, int(digit))
    return c


def clock_checkpoint(c, label, parity):
    _, s, u, v = c
    t = 1 if parity == "odd" else -1
    h = -1 if u == 0 else 1
    z = 4 - 3 * u if parity == "odd" else 1 + 3 * u
    bit = 1 - u if parity == "odd" else v
    alpha, beta, gamma, delta, epsilon = label
    a, b = t * alpha, t * beta
    cc, d = 2 + h * gamma, 1 + h * delta
    r = t * (epsilon + s - 1)
    x = tuple(w % 5 for w in (3 * (a + cc), 3 * (b + d),
                             3 * (a - cc), 3 * (b - d), z - a - b - r, r))
    return x, bit


def reachable(start, adjacency):
    distance = {start: 0}
    pending = deque([start])
    while pending:
        current = pending.popleft()
        for target in adjacency[current]:
            if target not in distance:
                distance[target] = distance[current] + 1
                pending.append(target)
    return distance


def sccs(adjacency):
    """Iterative Kosaraju, retaining the complete directed graph."""
    seen, finish = set(), []
    for start in sorted(adjacency):
        if start in seen:
            continue
        stack = [(start, False)]
        while stack:
            node, leave = stack.pop()
            if leave:
                finish.append(node)
            elif node not in seen:
                seen.add(node)
                stack.append((node, True))
                stack.extend((target, False) for target in reversed(adjacency[node])
                             if target not in seen)
    reverse = {node: [] for node in adjacency}
    for node, targets in adjacency.items():
        for target in targets:
            reverse[target].append(node)
    seen, components = set(), []
    for start in reversed(finish):
        if start in seen:
            continue
        component, stack = set(), [start]
        seen.add(start)
        while stack:
            node = stack.pop()
            component.add(node)
            for target in reverse[node]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        components.append(frozenset(component))
    return tuple(sorted(components, key=lambda values: min(values))), reverse


def graph_period(adjacency, start):
    distance = reachable(start, adjacency)
    if len(distance) != len(adjacency):
        raise ValueError("period requested for a non-reachable graph")
    return reduce(gcd, (abs(distance[x] + 1 - distance[y])
                        for x in adjacency for y in adjacency[x]), 0)


def json_value(value):
    if isinstance(value, Fraction):
        return str(value.numerator) + "/" + str(value.denominator)
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [json_value(item) for item in sorted(value)]
    return value


class Audit:
    def __init__(self):
        self.checks = Counter()
        self.failures = []
        self.failure_count = 0
        self.data = {}

    def equal(self, group, claim, actual, expected, context=None):
        self.checks[group] += 1
        if actual != expected:
            self.failure_count += 1
            if len(self.failures) < 20:
                self.failures.append({"group": group, "claim": claim,
                                      "actual": actual, "expected": expected,
                                      "context": context})


def audit_memory(audit):
    states = tuple(x for x in product(range(5), repeat=6) if sum(x) % 5 in (1, 4))
    adjacency = {x: tuple(step_bit(x, bit) for bit in (0, 1)) for x in states}
    fibres = defaultdict(set)
    for x in states:
        fibres[record(x)].add(x)
        for bit, y in enumerate(adjacency[x]):
            audit.equal("A", "stable_domain", sum(y) % 5 in (1, 4), True, (x, bit))
            audit.equal("A", "candidate_V_next_equals_minus_V", record_vector(y),
                        neg(record_vector(x)), (x, bit))
            audit.equal("A", "candidate_record_invariance", record(y), record(x), (x, bit))
            audit.equal("A", "each_directed_edge_has_reverse", x in adjacency[y],
                        True, (x, bit))
    components, _ = sccs(adjacency)
    audit.equal("A", "stable_checkpoint_count", len(states), 6250)
    audit.equal("A", "predicted_record_count", len(fibres), 313)
    histogram = Counter(len(v) for v in fibres.values())
    audit.equal("A", "predicted_fibre_size_histogram", dict(histogram), {10: 1, 20: 312})
    audit.equal("A", "complete_SCCs_are_exact_record_fibres", set(components),
                {frozenset(v) for v in fibres.values()})
    for key in sorted(fibres):
        audit.equal("F", "static_codebook_readback", record(record_encode(key)), key, key)
    audit.data["memory"] = {
        "checkpoints": len(states), "directed_edges": 2 * len(states),
        "record_classes": len(fibres), "fibre_size_histogram": dict(histogram),
        "strong_component_sizes": dict(Counter(len(v) for v in components)),
        "all_fixed_invariant_readers": "exactly maps factoring through the SCC partition",
        "codebook": "lexicographic sign representative; z=1; r=0; no endogenous write",
    }
    return fibres


def audit_clock(audit):
    origin = (0, 0, 0, 1)
    graph, pending = {}, deque([origin])
    while pending:
        c = pending.popleft()
        if c in graph:
            continue
        graph[c] = tuple(clock_transition(c, digit) for digit in (0, 1))
        pending.extend(target for target in graph[c] if target not in graph)
    components, reverse = sccs(graph)
    audit.equal("B", "nominal_clock_domain_reached", len(graph), 100)
    audit.equal("B", "strongly_connected_clock", len(components), 1)
    period = graph_period(graph, origin)
    audit.equal("B", "clock_period", period, 1)
    switch_count = 0
    for m in range(65536):
        if m:
            switch_count += int(theta(m) != theta(m - 1))
        literal = clock_literal(m)
        audit.equal("B", "literal_switch_count", switch_sum(m), switch_count, m)
        audit.equal("B", "clock_digit_recursion", clock_from_digits(m), literal, m)
        for digit in (0, 1):
            if 2 * m + digit <= 65535:
                audit.equal("B", "literal_successor_recursion", clock_transition(literal, digit),
                            clock_literal(2 * m + digit), (m, digit))
    weights = {c: 1 if c[2] == c[3] else 2 for c in graph}
    incoming = Counter()
    for c, destinations in graph.items():
        for target in destinations:
            incoming[target] += weights[c]
    for c in sorted(graph):
        audit.equal("B", "rational_stationary_integer_certificate", incoming[c],
                    2 * weights[c], c)
    audit.equal("B", "stationary_integer_denominator", sum(weights.values()), 150)
    outward, inward = reachable(origin, graph), reachable(origin, reverse)
    if len(inward) != len(graph) or graph[origin][0] != origin:
        audit.data["clock"] = {"states": len(graph), "period": period,
                               "primitive_certificate": "NOT_ESTABLISHED"}
        return None
    length = max(outward.values()) + max(inward.values())
    # Path via origin, padded by its 0-loop, proves every M**length entry >= 1.
    # Integer propagation independently verifies the same matrix certificate.
    minimum, maximum = None, 0
    for start in sorted(graph):
        counts = {start: 1}
        for _ in range(length):
            following = Counter()
            for c, count in counts.items():
                for target in graph[c]:
                    following[target] += count
            counts = following
        row_min = min(counts.get(c, 0) for c in graph)
        minimum = row_min if minimum is None else min(minimum, row_min)
        maximum = max(maximum, max(counts.values()))
        audit.equal("B", "primitive_integer_power_positive", row_min > 0, True, start)
        audit.equal("B", "primitive_power_row_sum", sum(counts.values()), 2 ** length, start)
    # A separate short-word affine certificate uses k=s+r modulo five.
    word_specs = (("0000", 0, 0, 0), ("0110", 1, 0, 0),
                  ("1010", 0, 1, 0), ("1000", 3, 3, 1))
    for c in sorted(graph):
        r, s, u, _ = c
        for word, dr, dk, flip in word_specs:
            image = c
            for digit in word:
                image = clock_transition(image, int(digit))
            rr, ss, uu, vv = image
            audit.equal("B", "four_digit_affine_certificate",
                        (rr, (rr + ss) % 5, uu, vv),
                        ((r + dr) % 5, (r + s + dk) % 5, u ^ flip, 1 - (u ^ flip)),
                        (c, word))
    audit.data["clock"] = {
        "states": len(graph), "SCC_sizes": [len(v) for v in components],
        "period": period, "literal_audit_m_inclusive": [0, 65535],
        "stationary": "pi(r,s,u,v)=1/150 if u=v; 2/150 otherwise",
        "stationary_weight_histogram": dict(Counter(weights.values())),
        "max_distance_to_origin": max(inward.values()),
        "max_distance_from_origin": max(outward.values()),
        "primitive_power": length, "primitive_power_min_entry": minimum,
        "primitive_power_max_entry": maximum,
        "row_mass": 2 ** length,
        "contraction_factor": Fraction(2 ** length - len(graph) * minimum, 2 ** length),
        "all_prefix_proof": "PROOF.md; uniform dyadic blocks plus arbitrary-prefix remainder bound",
    }
    if any(incoming[c] != 2 * weights[c] for c in graph):
        return None
    return weights


def normalized_profile(atoms):
    positive = tuple(sorted(v for v in atoms.values() if v > 0))
    divisor = reduce(gcd, positive)
    return tuple(v // divisor for v in positive)


def profile_description(weights):
    return {"atoms": len(weights), "integer_atom_weights": dict(Counter(weights)),
            "denominator": sum(weights)}


def audit_pushforward(audit, clock_weights, fibres):
    labels = tuple(product(range(5), repeat=5))
    joint_profiles = Counter()
    profile_examples = {}
    missing_support = 0
    for label in labels:
        checkpoint, decorated = Counter(), Counter()
        for c, weight in clock_weights.items():
            for parity in ("odd", "even"):
                x, bit = clock_checkpoint(c, label, parity)
                checkpoint[x] += weight
                decorated[(x, bit)] += weight
        audit.equal("C", "checkpoint_pushforward_total", sum(checkpoint.values()), 300, label)
        audit.equal("C", "decorated_pushforward_total", sum(decorated.values()), 300, label)
        key = min(label[:4], neg(label[:4]))
        support_matches = set(checkpoint) == fibres[key]
        audit.equal("E", "trajectory_support_is_whole_record_component", support_matches, True, label)
        missing_support += int(not support_matches)
        bit_profiles = []
        for bit in (0, 1):
            bit_atoms = {x: weight for (x, b), weight in decorated.items() if b == bit}
            audit.equal("C", "control_bit_frequency_one_half", sum(bit_atoms.values()), 150,
                        (label, bit))
            bit_profiles.append(normalized_profile(bit_atoms))
        joint = (normalized_profile(checkpoint), normalized_profile(decorated),
                 bit_profiles[0], bit_profiles[1])
        joint_profiles[joint] += 1
        profile_examples.setdefault(joint, label)
        for n in range(3, 35):
            x = encode_time(n, label)
            audit.equal("C", "native_tick_equals_chart", step_bit(x, theta(n)),
                        encode_time(n + 1, label), (label, n))
            m = (n - 1) // 2 if n % 2 else (n - 2) // 2
            parity = "odd" if n % 2 else "even"
            audit.equal("C", "clock_chart_equals_inherited_chart",
                        clock_checkpoint(clock_literal(m), label, parity), (x, theta(n)),
                        (label, n))
    for label in labels[:9]:
        for n in (2 ** 127, 10 ** 100 + 123):
            x = encode_time(n, label)
            audit.equal("C", "huge_time_native_tick", step_bit(x, theta(n)),
                        encode_time(n + 1, label), (label, str(n)))
            m = (n - 1) // 2 if n % 2 else (n - 2) // 2
            parity = "odd" if n % 2 else "even"
            audit.equal("C", "huge_time_clock_chart",
                        clock_checkpoint(clock_from_digits(m), label, parity), (x, theta(n)),
                        (label, str(n)))
    ordered = sorted(joint_profiles, key=lambda joint: (len(joint[0]), joint))
    expected_zero = ((1,) * 10, (1,) * 10 + (2,) * 10,
                     (1,) * 5 + (2,) * 5, (1,) * 5 + (2,) * 5)
    expected_nonzero = ((1,) * 20, (1,) * 10 + (2,) * 10 + (3,) * 10,
                        (1,) * 5 + (2,) * 5 + (3,) * 5,
                        (1,) * 5 + (2,) * 5 + (3,) * 5)
    audit.equal("C", "analytical_pushforward_profile_prediction", dict(joint_profiles),
                {expected_zero: 5, expected_nonzero: 3120})
    audit.data["pushforward"] = {
        "all_labels": len(labels), "native_times_inclusive": [3, 34],
        "enormous_time_labels": 9, "enormous_times": ["2**127", "10**100+123"],
        "profiles": [dict({"profile_id": index, "labels": joint_profiles[joint],
                           "first_label": profile_examples[joint]},
                          **{name: profile_description(weights)
                             for name, weights in zip(("checkpoint", "decorated", "bit0", "bit1"), joint)})
                     for index, joint in enumerate(ordered)],
        "component_full_support_failures": missing_support,
        "eventual_record": "positive frequency at every component checkpoint forces eventual constants to be component constants",
    }
    return ordered


def subset_sums(weights):
    possible = {0}
    for weight in weights:
        possible |= {value + weight for value in possible}
    return frozenset(possible)


def two_bin_sums(weights):
    """Whole atoms only. The third alternative leaves an atom SILENT."""
    possible = {(0, 0)}
    for weight in weights:
        possible = possible | {(low + weight, high) for low, high in possible} | {
            (low, high + weight) for low, high in possible}
    return frozenset(possible)


def classify_profile(weights):
    total = sum(weights)
    sums = subset_sums(weights)
    pairs = two_bin_sums(weights)
    rates = frozenset(Fraction(low, low + high) for low, high in pairs if low + high)
    fractions = frozenset(Fraction(value, total) for value in sums)
    full_triangle = frozenset((a, b) for a in range(total + 1) for b in range(total - a + 1))
    farey = frozenset(Fraction(numerator, denominator)
                     for denominator in range(1, total + 1)
                     for numerator in range(denominator + 1))
    description = dict(profile_description(weights), **{
        "subset_sum_count": len(sums),
        "subset_sums": {"all_integers_from": 0, "through": total}
        if sums == frozenset(range(total + 1)) else sorted(sums),
        "two_bin_pair_count": len(pairs),
        "two_bin_sums": "all (a,b) integers >=0 with a+b<=denominator"
        if pairs == full_triangle else sorted(pairs),
        "accepted_ratio_count": len(rates),
        "accepted_ratios": "all reduced rationals in [0,1] with denominator<=atom_denominator"
        if rates == farey else sorted(rates),
        "empty_acceptance": "UNDEFINED; (0,0) excluded from accepted ratios",
    })
    return (description, fractions, rates, sums == frozenset(range(total + 1)),
            pairs == full_triangle, rates == farey)


def audit_classification(audit, joint_profiles):
    unique = sorted({weights for joint in joint_profiles for weights in joint},
                    key=lambda weights: (sum(weights), len(weights), weights))
    classified = {}
    descriptions = []
    for index, weights in enumerate(unique):
        description, absolute, accepted, full_sums, full_pairs, full_rates = classify_profile(weights)
        description["atom_profile_id"] = index
        classified[weights] = (index, absolute, accepted)
        descriptions.append(description)
        audit.equal("D", "binary_extremes_attainable", {Fraction(0), Fraction(1)} <= absolute,
                    True, index)
        audit.equal("D", "acceptance_extremes_attainable", {Fraction(0), Fraction(1)} <= accepted,
                    True, index)
        audit.equal("D", "analytical_all_subset_sums_prediction", full_sums, True, index)
        audit.equal("D", "analytical_all_two_bin_pairs_prediction", full_pairs, True, index)
        audit.equal("D", "analytical_full_Farey_set_prediction", full_rates, True, index)
    joint_ids = [{name: classified[weights][0]
                  for name, weights in zip(("checkpoint", "decorated", "bit0", "bit1"), joint)}
                 for joint in joint_profiles]
    audit.data["target_independent_frequency_classification"] = {
        "atom_profiles": descriptions, "joint_profile_atom_ids": joint_ids,
        "bit_restriction": "bit0/bit1 frequencies are conditioned on that bit; absolute rates are half these values",
        "completeness": "dynamic programming allocates each distinct positive atom whole to LOW, HIGH, or SILENT",
        "selection": "none; these are complete attainable sets, not adopted physical readers",
    }
    return classified


def qdd_low(pistons):
    v = tuple(BALANCED[a] for a in pistons)
    norm, s = sum(a * a for a in v), sum(v)
    if norm == 0:
        return None
    return Fraction(s * s, 4 * (5 * norm - s * s))


def audit_targets_and_loss(audit, joint_profiles, classified):
    # Deliberately constructed only AFTER all atom and reading sets are complete.
    targets = Counter(qdd_low(p) for p in product(range(5), repeat=4) if any(p))
    rows = []
    for target in sorted(targets):
        row = {"LOW": target, "supported_pistons": targets[target],
               "supported_heads": 25 * targets[target], "by_joint_profile": []}
        for joint in joint_profiles:
            membership = {}
            for name, weights in zip(("checkpoint", "decorated", "bit0", "bit1"), joint):
                _, absolute, accepted = classified[weights]
                membership[name + "_unconditional" if name in ("checkpoint", "decorated")
                           else name + "_conditional"] = target in absolute
                membership[name + "_accepted_ratio"] = target in accepted
                if name in ("bit0", "bit1"):
                    membership[name + "_absolute"] = target in {v / 2 for v in absolute}
            row["by_joint_profile"].append(membership)
        rows.append(row)
    audit.equal("D", "all_supported_pistons_compared", sum(targets.values()), 624)
    audit.equal("D", "known_target_1_over_256_present", Fraction(1, 256) in targets, True)
    audit.equal("D", "known_target_9_over_14_present", Fraction(9, 14) in targets, True)
    left, right = (4, 1, 0, 0, 0, 0), (2, 1, 1, 2, 1, 0)
    merged = (1, 4, 0, 0, 0, 0)
    audit.equal("F", "original_head_collision_left", step_bit(left, 0), merged)
    audit.equal("F", "original_head_collision_right", step_bit(right, 0), merged)
    audit.equal("F", "distinct_original_QDD_LOW_left", qdd_low(left[:4]), Fraction(0))
    audit.equal("F", "distinct_original_QDD_LOW_right", qdd_low(right[:4]), Fraction(9, 14))
    synchronized = merged
    for n in (1, 2):
        synchronized = step_bit(synchronized, theta(n))
    audit.equal("F", "collision_enters_synchronized_domain", sum(synchronized) % 5, 1)
    audit.data["QDD_comparison_after_classification"] = {
        "distinct_LOW_targets": len(targets), "supported_pistons": sum(targets.values()),
        "supported_heads": 25 * sum(targets.values()), "rows": rows,
        "every_target_individually_attainable_on_each_decorated_profile": all(
            all(target in classified[joint[1]][2] for target in targets)
            for joint in joint_profiles),
        "simultaneous_reading": "per-orbit membership does not supply one reader realizing all head targets simultaneously",
    }
    audit.data["original_record_loss"] = {
        "heads": [left, right], "one_tick_common_state": merged,
        "original_LOW": [Fraction(0), Fraction(9, 14)],
        "synchronized_common_state": synchronized,
        "common_protected_record": record(synchronized),
        "disposition": "native protected sign class cannot recover distinct original records after merging",
    }
    current_left = (1, 0, 0, 0, 0, 0)
    current_right = (1, 1, 3, 4, 1, 1)
    audit.equal("F", "current_QDD_witness_native_edge", step_bit(current_left, 1), current_right)
    audit.equal("F", "current_QDD_witness_same_record", record(current_left), record(current_right))
    audit.equal("F", "current_QDD_witness_LOW_left", qdd_low(current_left[:4]), Fraction(1, 16))
    audit.equal("F", "current_QDD_witness_LOW_right", qdd_low(current_right[:4]), Fraction(1, 136))
    audit.data["current_QDD_nonfactorization"] = {
        "states": [current_left, current_right], "bit": 1,
        "common_protected_record": record(current_left),
        "current_LOW": [Fraction(1, 16), Fraction(1, 136)],
    }


def main():
    audit = Audit()
    exception = None
    try:
        fibres = audit_memory(audit)
        clock_weights = audit_clock(audit)
        if clock_weights is None:
            audit.data["dependent_work"] = "C-D-E frequency work unavailable: clock certificate failed"
        else:
            profiles = audit_pushforward(audit, clock_weights, fibres)
            classified = audit_classification(audit, profiles)
            audit_targets_and_loss(audit, profiles, classified)
    except Exception as error:
        exception = {"type": type(error).__name__, "message": str(error)}
    complete = exception is None and all(audit.checks[name] for name in "ABCDEF")
    outcome = ("PASS" if not audit.failure_count else "FALSIFIED") if complete else "STOP"
    report = {
        "name": NAME, "status": "formal result-exposed proof audit", "layer": "L1",
        "outcome": outcome, "complete": complete, "checks_by_package": dict(audit.checks),
        "total_exact_checks": sum(audit.checks.values()), "mismatches": audit.failure_count,
        "first_mismatches": audit.failures, "exception": exception, "results": audit.data,
        "boundaries": "static storage is not endogenous writing; density is not occurrence selection; no physical decoder closure",
    }
    raw = json.dumps(json_value(report), sort_keys=True, ensure_ascii=True,
                     separators=(",", ":")).encode("ascii") + b"\n"
    sys.stdout.buffer.write(raw)
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
