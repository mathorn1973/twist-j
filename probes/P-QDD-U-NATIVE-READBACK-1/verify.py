"""P-QDD-U-NATIVE-READBACK-1 prospective exact verifier.

Self-contained standard-library code. No private imports, runtime repository
reads, network access, random sampling, or floating-point comparisons.
Completed audits emit PASS/FALSIFIED and exit 0. An exception or incomplete
run emits STOP and exits nonzero; it is not a scientific falsification.

This file must not be executed before its public prospective pin.
"""

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
import sys


GROUP_NAMES = (
    "generators_affine_reference",
    "generator_involutions",
    "qdd_matrix_scalar_reference",
    "literal_tm_switch_counts",
    "synchronized_chart",
    "all_head_trajectory_and_readback",
    "fibers_and_preparation_optimum",
    "supported_collision_and_memory_witnesses",
    "enormous_clock_jump",
)
CHART_TIMES = tuple(range(3, 19)) + (
    31, 32, 33, 63, 64, 65, 255, 256, 257,
    2 ** 127, 2 ** 127 + 1, 10 ** 80 + 7,
)
HUGE_TIME = 10 ** 1000 + 123
HUGE_LABELS = (
    (0, 0, 0, 0, 0), (1, 1, 1, 1, 1),
    (0, 1, 2, 3, 4), (4, 3, 2, 1, 0),
) + tuple(tuple(int(i == j) for i in range(5)) for j in range(5))
BALANCED = (0, 1, 2, -2, -1)
PHASE_MAPS = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
SAVED_CLASSES = ((0,), (1, 2), (3, 4))
CLASS_OF_PHASE = (0, 1, 1, 2, 2)
GRAM = tuple(tuple(Q(int(i == j)) - Q(1, 5) for j in range(4))
             for i in range(4))

# Independent affine matrices and constants, in source coordinate order.
AFFINE = (
    (((0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0),
      (0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0),
      (0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)),
     (0, 0, 0, 0, 0, 0)),
    (((0, 0, -1, 0, 0, 0), (0, 0, 0, -1, 0, 0),
      (-1, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, 0),
      (0, 0, 0, 0, -1, 0), (0, 0, 0, 0, 0, -1)),
     (0, 0, 0, 0, 0, 0)),
    (((0, 0, -1, 0, 0, 0), (0, 0, 0, -1, 0, 1),
      (-1, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, -1),
      (0, 0, 0, 0, -1, 0), (0, 0, 0, 0, 0, -1)),
     (2, 1, 2, 1, 1, 0)),
    (((-1, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, 0),
      (0, 0, -1, 0, 0, 0), (0, 0, 0, -1, 0, 0),
      (0, 0, 0, 0, -1, 0), (0, 0, 0, 0, 0, -1)),
     (2, 1, 3, 4, 1, 1)),
    (((-1, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, 0),
      (0, 0, -1, 0, 0, 0), (0, 0, 0, -1, 0, 0),
      (0, 0, 0, 0, -1, 0), (0, 0, 0, 0, 0, -1)),
     (2, 1, 3, 4, 2, 1)),
)


def theta(n):
    return n.bit_count() % 2


def native_generator(index, x):
    p1, p4, p1p, p4p, q, r = x
    if index == 0:
        raw = (p4, p1, p4p, p1p, q, r)
    elif index == 1:
        raw = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif index == 2:
        raw = (-p1p+2, -p4p+1+r, -p1+2, -p4+1-r, 1-q, -r)
    elif index == 3:
        raw = (2-p1, 1-p4, 3-p1p, 4-p4p, 1-q, 1-r)
    elif index == 4:
        raw = (2-p1, 1-p4, 3-p1p, 4-p4p, 2-q, 1-r)
    else:
        raise ValueError("generator index outside frozen source")
    return tuple(a % 5 for a in raw)


def affine_generator(index, x):
    matrix, offset = AFFINE[index]
    return tuple((sum(a*b for a, b in zip(row, x)) + shift) % 5
                 for row, shift in zip(matrix, offset))


def native_step(n, x):
    return native_generator((sum(x) + 2*theta(n)) % 5, x)


def affine_step(n, x):
    return affine_generator((sum(x) + 2*theta(n)) % 5, x)


def switch_sum(m):
    result, sign = 0, 1
    while m:
        result += sign*m
        m //= 2
        sign = -sign
    return result


def chart_parameters(n):
    return (
        1 if (n-3) % 2 == 0 else -1,
        1 if (n+theta(n-1)) % 2 == 0 else -1,
        switch_sum((n-1)//2) - 1,
        4 - 3*theta(n-1),
    )


def decode(n, x):
    t, h, offset, _ = chart_parameters(n)
    p1, p4, p1p, p4p, _, r = x
    return tuple(a % 5 for a in (
        t*(p1+p1p), t*(p4+p4p), h*(p1-p1p-2),
        h*(p4-p4p-1), t*r-offset,
    ))


def encode(n, labels):
    t, h, offset, phase = chart_parameters(n)
    alpha, beta, gamma, delta, epsilon = labels
    a, b = t*alpha, t*beta
    c, d = 2+h*gamma, 1+h*delta
    r = t*(epsilon+offset)
    return tuple(v % 5 for v in (
        3*(a+c), 3*(b+d), 3*(a-c), 3*(b-d), phase-a-b-r, r,
    ))


def jump_from_core(n, x, target):
    return encode(target, decode(n, x))


def initial_path(initial_phase, count=3):
    selected = []
    phase = initial_phase
    for bit in (0, 1, 1)[:count]:
        selected.append((phase+2*bit) % 5)
        phase = PHASE_MAPS[bit][phase]
    return tuple(selected), phase


def reverse_initial(x, initial_phase, count=3):
    selected, _ = initial_path(initial_phase, count)
    for index in reversed(selected):
        x = native_generator(index, x)
    return x


def recover_head(n, current, saved_phase):
    if n >= 3:
        return reverse_initial(encode(3, decode(n, current)), saved_phase)
    return reverse_initial(current, saved_phase, n)


def recover_qdd_candidate(n, current, saved_class):
    if n >= 3:
        return reverse_initial(encode(3, decode(n, current)),
                               SAVED_CLASSES[saved_class][0])
    compatible = tuple(phase for phase in SAVED_CLASSES[saved_class]
                       if initial_path(phase, n)[1] == sum(current) % 5)
    if not compatible:
        return None
    return reverse_initial(current, compatible[0], n)


def zero_record():
    return ("ZERO_SUPPORT", Q(0), (Q(0), Q(0)),
            "ZERO_DENOMINATOR", "ZERO_DENOMINATOR")


def scalar_qdd(pistons):
    v = tuple(BALANCED[a] for a in pistons)
    s, norm = sum(v), sum(a*a for a in v)
    mass = Q(norm) - Q(s*s, 5)
    if mass == 0:
        return zero_record()
    low, high = Q(s*s, 20), Q(norm) - Q(s*s, 4)
    density = tuple(tuple(Q(a)*(Q(b)-Q(s, 5))/mass for b in v) for a in v)
    return ("SUPPORTED", mass, (low, high), ("DENSITY", density),
            ("NORMALIZED", (low/mass, high/mass)))


def gram_pair(a, b):
    return sum((Q(a[i])*GRAM[i][j]*Q(b[j])
                for i in range(4) for j in range(4)), Q(0))


def matrix_qdd(pistons):
    v = tuple(Q(BALANCED[a]) for a in pistons)
    mass = gram_pair(v, v)
    if mass == 0:
        return zero_record()
    low_vector = tuple(sum((Q(1, 4)*v[j] for j in range(4)), Q(0))
                       for _ in range(4))
    high_vector = tuple(a-b for a, b in zip(v, low_vector))
    low, high = gram_pair(low_vector, low_vector), gram_pair(high_vector, high_vector)
    density = tuple(tuple(sum((v[i]*v[k]*GRAM[k][j] for k in range(4)), Q(0))/mass
                          for j in range(4)) for i in range(4))
    return ("SUPPORTED", mass, (low, high), ("DENSITY", density),
            ("NORMALIZED", (low/mass, high/mass)))


def json_value(value):
    if isinstance(value, Q):
        return str(value.numerator) + "/" + str(value.denominator)
    if isinstance(value, dict):
        return {str(key): json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [json_value(item) for item in sorted(value, key=repr)]
    return value


class Group:
    def __init__(self, name):
        self.name = name
        self.checks = 0
        self.failures = 0
        self.first_failure = None
        self.completed = False
        self.exception = None
        self.coverage = {}

    def equal(self, claim, observed, expected, context=None):
        self.checks += 1
        if observed != expected:
            self.failures += 1
            if self.first_failure is None:
                self.first_failure = json_value({
                    "claim": claim, "observed": observed,
                    "expected": expected, "context": context,
                })

    def report(self):
        return {
            "checks": self.checks, "failures": self.failures,
            "completed": self.completed, "coverage": self.coverage,
            "first_failure": self.first_failure, "exception": self.exception,
        }


def build_data():
    heads = tuple(product(range(5), repeat=6))
    labels = tuple(product(range(5), repeat=5))
    pistons = tuple(product(range(5), repeat=4))
    records = {p: scalar_qdd(p) for p in pistons}
    unique = {}
    record_ids = {}
    for p in pistons:
        rec = records[p]
        if rec not in unique:
            unique[rec] = len(unique)
        record_ids[p] = unique[rec]
    return {"heads": heads, "labels": labels, "pistons": pistons,
            "records": records, "record_ids": record_ids,
            "unique_record_count": len(unique)}


def generators_reference(group, data):
    for x in data["heads"]:
        for index in range(5):
            group.equal("source_formula_equals_affine_matrix",
                        native_generator(index, x), affine_generator(index, x),
                        (index, x))
        for bit in range(2):
            phase = sum(x) % 5
            selected = (phase + 2*bit) % 5
            group.equal("inherited_phase_table",
                        sum(native_generator(selected, x)) % 5,
                        PHASE_MAPS[bit][phase], (bit, x))
    group.coverage = {"heads": 15625, "generators": 5,
                      "generator_instances": 78125, "phase_table_instances": 31250}


def involutions(group, data):
    for x in data["heads"]:
        for index in range(5):
            group.equal("source_generator_is_involution",
                        native_generator(index, native_generator(index, x)), x,
                        (index, x))
    group.coverage = {"heads": 15625, "generators": 5, "instances": 78125}


def qdd_reference(group, data):
    for p in data["pistons"]:
        rec = data["records"][p]
        group.equal("all_five_qdd_fields_matrix_equals_scalar", rec, matrix_qdd(p), p)
        group.equal("support_exactly_nonzero_piston", rec[0] == "SUPPORTED", any(p), p)
        negative = tuple((-a) % 5 for a in p)
        group.equal("inherited_common_sign_invariance", rec, data["records"][negative], p)
    group.equal("inherited_complete_record_count", data["unique_record_count"], 313)
    group.coverage = {"piston_inputs": 625, "qdd_fields": 5,
                      "distinct_complete_records_expected": 313}


def literal_switches(group, data):
    count = 0
    group.equal("switch_sum_zero", switch_sum(0), 0, 0)
    for m in range(1, 10001):
        count += int(theta(m) != theta(m-1))
        group.equal("closed_switch_sum_equals_literal_prefix", switch_sum(m), count, m)
    group.coverage = {"prefix_endpoints": 10001, "maximum_endpoint": 10000}


def charts(group, data):
    pairs = 0
    for n in CHART_TIMES:
        for labels in data["labels"]:
            x = encode(n, labels)
            context = (n, labels)
            group.equal("encoded_sheet", sum(x) % 5, 4-3*theta(n-1), context)
            group.equal("decode_encode_inverse", decode(n, x), labels, context)
            group.equal("encode_decode_inverse", encode(n, decode(n, x)), x, context)
            group.equal("native_tick_matches_next_chart", native_step(n, x),
                        encode(n+1, labels), context)
            group.equal("labels_invariant_under_native_tick",
                        decode(n+1, native_step(n, x)), labels, context)
            pairs += 1
    group.coverage = {"labels": 3125, "times": 28, "label_time_pairs": pairs}


def all_trajectories(group, data):
    snapshots = 0
    for head in data["heads"]:
        # Separate dense affine reference for the three-tick initialization.
        prefix = [head]
        for n in range(3):
            prefix.append(affine_step(n, prefix[-1]))
        labels = decode(3, prefix[3])
        old_phase = sum(head) % 5
        saved_class = CLASS_OF_PHASE[old_phase]
        original_record = data["records"][head[:4]]
        current = head
        for n in range(18):
            expected = prefix[n] if n < 3 else encode(n, labels)
            context = (head, n)
            group.equal("direct_trajectory_equals_closed_form", current, expected, context)
            group.equal("saved_phase_recovers_complete_head",
                        recover_head(n, current, old_phase), head, context)
            candidate = recover_qdd_candidate(n, current, saved_class)
            reconstructed = (data["records"][candidate[:4]] if candidate is not None
                             else ("NO_ADMITTED_INITIAL_PHASE",))
            group.equal("saved_class_recovers_all_five_qdd_fields",
                        reconstructed, original_record, context)
            snapshots += 1
            if n != 17:
                current = native_step(n, current)
    group.coverage = {"heads": 15625, "times": 18, "time_range": [0, 17],
                      "snapshots": snapshots, "direct_ticks": 265625,
                      "early_times_included": [0, 1, 2]}


def fibers(group, data):
    inverse_fibers = defaultdict(list)
    for head in data["heads"]:
        image = head
        for n in range(3):
            image = native_step(n, image)
        inverse_fibers[image].append(head)
    group.equal("inherited_image_size", len(inverse_fibers), 3125)
    histogram = Counter()
    maximum, supported_maximum, supported_heads = 0, 0, 0
    selected_supported_domain = set()
    for image, heads in inverse_fibers.items():
        context = image
        group.equal("inherited_fiber_size", len(heads), 5, context)
        group.equal("inherited_one_head_per_phase",
                    sorted(sum(head) % 5 for head in heads), list(range(5)), context)
        counts, supported_counts = Counter(), Counter()
        supported_classes = defaultdict(list)
        for head in heads:
            record_id = data["record_ids"][head[:4]]
            counts[record_id] += 1
            if data["records"][head[:4]][0] == "SUPPORTED":
                supported_counts[record_id] += 1
                supported_classes[record_id].append(head)
                supported_heads += 1
            phase = sum(head) % 5
            group.equal("all_five_inverse_candidates", reverse_initial(image, phase), head,
                        (image, phase))
        a, b, c, d, _, r = image
        piston_a = tuple(v % 5 for v in (d+3-r, c+4, b+4+r, a))
        piston_b = tuple(v % 5 for v in (2-a, 1-b, 3-c, 4-d))
        piston_c = tuple(v % 5 for v in (-c, -d, -a, -b))
        negative_b = tuple((-v) % 5 for v in piston_b)
        negative_c = tuple((-v) % 5 for v in piston_c)
        for phase, formula in ((0, piston_a), (1, piston_b), (3, piston_c)):
            group.equal("inverse_piston_affine_formula",
                        reverse_initial(image, phase)[:4], formula, (image, phase))
        group.equal("class_a_disjoint_from_signed_b",
                    piston_a not in (piston_b, negative_b), True, image)
        group.equal("class_a_disjoint_from_signed_c",
                    piston_a not in (piston_c, negative_c), True, image)
        group.equal("class_b_never_negative_c", piston_b != negative_c, True, image)
        group.equal("class_b_equals_c_exact_affine_condition", piston_b == piston_c,
                    (a-c) % 5 == 2 and (b-d) % 5 == 1, image)
        if supported_counts:
            selected_id = min(supported_counts, key=lambda rid: (-supported_counts[rid], rid))
            selected_heads = supported_classes[selected_id]
        else:
            selected_heads = []
        selected_supported_domain.update(selected_heads)
        selected_records = {data["record_ids"][head[:4]] for head in selected_heads}
        group.equal("constructed_supported_subset_factor_constancy", len(selected_records), 1, image)
        group.equal("constructed_supported_subset_uses_largest_class", len(selected_heads),
                    max(supported_counts.values(), default=0), image)
        pattern = tuple(sorted(counts.values(), reverse=True))
        histogram[pattern] += 1
        maximum += max(counts.values())
        supported_maximum += max(supported_counts.values(), default=0)
        group.equal("at_most_three_complete_records", len(counts) <= 3, True, context)
    group.equal("complete_record_fiber_histogram", dict(histogram),
                {(2, 2, 1): 3000, (4, 1): 125})
    group.equal("maximal_full_record_preparation_domain", maximum, 6500)
    group.equal("maximal_supported_full_record_domain", supported_maximum, 6500)
    group.equal("supported_head_count", supported_heads, 15600)
    group.equal("constructed_supported_domain_cardinality", len(selected_supported_domain), 6500)
    group.equal("constructed_domain_all_supported",
                all(data["records"][head[:4]][0] == "SUPPORTED"
                    for head in selected_supported_domain), True)
    group.coverage = {"heads": 15625, "fibers": len(inverse_fibers),
                      "inverse_candidates": 15625,
                      "full_record_multiplicities": {
                          "2,2,1": histogram.get((2, 2, 1), 0),
                          "4,1": histogram.get((4, 1), 0)},
                      "maximal_domain": maximum,
                      "maximal_supported_domain": supported_maximum,
                      "constructed_supported_domain": len(selected_supported_domain),
                      "affine_classification_fibers": len(inverse_fibers)}


def witnesses(group, data):
    left = (4, 1, 0, 0, 0, 0)
    right = (2, 1, 1, 2, 1, 0)
    merged = (1, 4, 0, 0, 0, 0)
    group.equal("supported_collision_left", native_step(0, left), merged, left)
    group.equal("supported_collision_right", native_step(0, right), merged, right)
    for head, low in ((left, Q(0)), (right, Q(9, 14))):
        rec = data["records"][head[:4]]
        group.equal("collision_head_supported", rec[0], "SUPPORTED", head)
        group.equal("collision_original_low", rec[4][1][0], low, head)
    triples = (
        ((0, 4, 0, 0, 2, 2), Q(1, 16)),
        ((2, 1, 3, 3, 1, 1), Q(1, 256)),
        ((4, 4, 4, 0, 4, 4), Q(3, 8)),
    )
    common = (0, 0, 0, 1, 0, 0)
    lows = []
    for head, low in triples:
        image = head
        for n in range(3):
            image = native_step(n, image)
        rec = data["records"][head[:4]]
        group.equal("three_class_common_image", image, common, head)
        group.equal("three_class_head_supported", rec[0], "SUPPORTED", head)
        group.equal("three_class_original_low", rec[4][1][0], low, head)
        lows.append(rec[4][1][0])
    group.equal("three_distinct_required_values", len(set(lows)), 3)
    group.coverage = {"collision_heads": 2, "three_class_heads": 3,
                      "collision_low_values": ["0/1", "9/14"],
                      "three_class_low_values": ["1/16", "1/256", "3/8"]}


def huge_jump(group, data):
    for labels in HUGE_LABELS:
        origin = encode(3, labels)
        distant = jump_from_core(3, origin, HUGE_TIME)
        group.equal("huge_jump_label_recovery", decode(HUGE_TIME, distant), labels, labels)
        group.equal("huge_jump_local_tick", native_step(HUGE_TIME, distant),
                    encode(HUGE_TIME+1, labels), labels)
        before = encode(HUGE_TIME-17, labels)
        for n in range(HUGE_TIME-17, HUGE_TIME):
            before = native_step(n, before)
        group.equal("huge_jump_matches_seventeen_direct_final_ticks", before, distant, labels)
        middle_time = HUGE_TIME // 2
        middle = jump_from_core(3, origin, middle_time)
        composed = jump_from_core(middle_time, middle, HUGE_TIME)
        group.equal("huge_jump_composition", composed, distant, labels)
    group.coverage = {"representative_labels": len(HUGE_LABELS),
                      "target": "10**1000+123", "direct_tail_ticks_per_label": 17}


FUNCTIONS = (
    generators_reference, involutions, qdd_reference, literal_switches, charts,
    all_trajectories, fibers, witnesses, huge_jump,
)


def main():
    groups = {name: Group(name) for name in GROUP_NAMES}
    setup_exception = None
    try:
        data = build_data()
    except Exception as error:
        data = None
        setup_exception = type(error).__name__
    if data is not None:
        for name, function in zip(GROUP_NAMES, FUNCTIONS):
            group = groups[name]
            try:
                function(group, data)
                group.completed = True
            except Exception as error:
                group.exception = type(error).__name__
    complete = (setup_exception is None and len(FUNCTIONS) == len(GROUP_NAMES)
                and all(group.completed and group.checks > 0 for group in groups.values()))
    total_failures = sum(group.failures for group in groups.values())
    outcome = ("PASS" if total_failures == 0 else "FALSIFIED") if complete else "STOP"
    report = {
        "probe": "P-QDD-U-NATIVE-READBACK-1", "action_layer": "L1",
        "outcome": outcome, "completed_groups": sum(g.completed for g in groups.values()),
        "required_groups": len(GROUP_NAMES),
        "total_exact_checks": sum(g.checks for g in groups.values()),
        "exact_mismatches": total_failures,
        "groups": {name: groups[name].report() for name in GROUP_NAMES},
        "setup_exception": setup_exception,
        "scope": "native chart; original QDD readback obstruction; conditional saved memory; no physical event law",
    }
    raw = json.dumps(json_value(report), ensure_ascii=True, sort_keys=True,
                     separators=(",", ":")).encode("ascii") + b"\n"
    sys.stdout.buffer.write(raw)
    return 0 if complete else 2


if __name__ == "__main__":
    sys.exit(main())
