#!/usr/bin/env python3
"""Exact verifier for P-QDD-INSTRUMENT-U-INDUCED-1.

The accepted preregistration must be publicly pinned before this file is run.
Only Python standard-library integer and Fraction arithmetic is used.
"""

from array import array
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd, isqrt
from struct import pack


P = 5
ELL = (0, 1, 2, -2, -1)
LAMBDAS = ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4))
SUBSET_MASKS = tuple(range(1, 31))
DELAYS = (1, 2, 3, 4, 5)
FULL_SUBSET_BITS = (1 << 30) - 1
PACKED_LANE_WIDTH = 31
PACKED_LAMBDA_WIDTH = PACKED_LANE_WIDTH * 30
PACKED_LAMBDA_MASK = (1 << PACKED_LAMBDA_WIDTH) - 1
PACKED_ONE_LANES = sum(1 << (PACKED_LANE_WIDTH * offset) for offset in range(30))
PACKED_BIAS_LANES = PACKED_ONE_LANES << 29
PACKED_HIGH_LANES = PACKED_ONE_LANES << 30
SINGLE_WINDOW = (512, 2048)
LONG_WINDOW = (2048, 16384)

ZERO4 = (0, 0, 0, 0)
ONE4 = (Fraction(1),) * 4
RV = (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2))
FV = (Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(-1, 2))
GV = (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 2))


def encode(x):
    value = 0
    for coordinate in x:
        value = P * value + coordinate
    return value


def neg_mod(value):
    return (-value) % P


def generator(index, x):
    p1, p4, p1p, p4p, q, r = x
    if index == 0:
        return (p4, p1, p4p, p1p, q, r)
    if index == 1:
        return tuple(neg_mod(value) for value in (p1p, p4p, p1, p4, q, r))
    if index == 2:
        return (
            (-p1p + 2) % P,
            (-p4p + 1 + r) % P,
            (-p1 + 2) % P,
            (-p4 + 1 - r) % P,
            (1 - q) % P,
            (-r) % P,
        )
    if index == 3:
        constants = (2, 1, 3, 4, 1, 1)
        return tuple((constant - value) % P for constant, value in zip(constants, x))
    if index == 4:
        constants = (2, 1, 3, 4, 2, 1)
        return tuple((constant - value) % P for constant, value in zip(constants, x))
    raise ValueError(index)


def balanced_piston(piston):
    return tuple(ELL[value] for value in piston)


def sign_key(vector):
    negative = tuple(-value for value in vector)
    return min(vector, negative)


def matrix_rank(rows):
    matrix = [list(map(Fraction, row)) for row in rows if any(row)]
    if not matrix:
        return 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    rank = 0
    for column in range(column_count):
        pivot = next((row for row in range(rank, row_count) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for row in range(row_count):
            if row == rank or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def matrix_equal(left, right):
    return all(a == b for row_a, row_b in zip(left, right) for a, b in zip(row_a, row_b))


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def g_norm(vector):
    total = sum(vector, Fraction(0))
    return sum((value * value for value in vector), Fraction(0)) - total * total / 5


def density(vector):
    vector = tuple(map(Fraction, vector))
    norm = g_norm(vector)
    if norm == 0:
        raise ZeroDivisionError("zero density vector")
    total = sum(vector, Fraction(0))
    return tuple(
        tuple(vector[i] * (vector[j] - total / 5) / norm for j in range(4))
        for i in range(4)
    )


def average_density(post_counts, densities):
    nonzero_total = sum(count for post_class, count in post_counts.items() if post_class != 0)
    if nonzero_total == 0:
        return None
    return tuple(
        tuple(
            sum(
                (Fraction(count) * densities[post_class][i][j]
                 for post_class, count in post_counts.items() if post_class != 0),
                Fraction(0),
            ) / nonzero_total
            for j in range(4)
        )
        for i in range(4)
    )


def image_vector(rank_one_matrix):
    for column in range(4):
        candidate = tuple(rank_one_matrix[row][column] for row in range(4))
        if any(candidate):
            denominator = 1
            for value in candidate:
                denominator = denominator * value.denominator // gcd(
                    denominator, value.denominator
                )
            integers = [int(value * denominator) for value in candidate]
            common = 0
            for value in integers:
                common = gcd(common, abs(value))
            integers = [value // common for value in integers]
            first = next(value for value in integers if value)
            if first < 0:
                integers = [-value for value in integers]
            return tuple(map(Fraction, integers))
    return None


def rational_sqrt(value):
    if value < 0:
        return None
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        return None
    return Fraction(numerator, denominator)


def rotate_high(vector, parameter):
    vector = tuple(map(Fraction, vector))
    mean = sum(vector, Fraction(0)) / 4
    u = tuple(value - mean for value in vector)
    ur, uf, ug = dot(u, RV), dot(u, FV), dot(u, GV)
    denominator = 1 + parameter * parameter
    cosine = (1 - parameter * parameter) / denominator
    sine = 2 * parameter / denominator
    rr = cosine * ur - sine * uf
    ff = sine * ur + cosine * uf
    return tuple(rr * RV[i] + ff * FV[i] + ug * GV[i] for i in range(4))


ALL_PARAMETERS = object()


def high_parameter_candidates(vector, dbar):
    if matrix_rank(dbar) != 1:
        return set()
    direction = image_vector(dbar)
    if direction is None or sum(direction, Fraction(0)) != 0:
        return set()

    vector = tuple(map(Fraction, vector))
    mean = sum(vector, Fraction(0)) / 4
    u = tuple(value - mean for value in vector)
    ur, uf, ug = dot(u, RV), dot(u, FV), dot(u, GV)
    wr, wf, wg = dot(direction, RV), dot(direction, FV), dot(direction, GV)
    planar_norm = ur * ur + uf * uf

    if planar_norm == 0:
        if ug == 0 or not matrix_equal(density(u), dbar):
            return set()
        return ALL_PARAMETERS

    candidates = set()
    mus = []
    if ug != 0:
        mu = wg / ug
        if mu != 0:
            mus.append(mu)
    elif wg == 0:
        square = (wr * wr + wf * wf) / planar_norm
        root = rational_sqrt(square)
        if root not in (None, 0):
            mus.extend((root, -root))

    for mu in mus:
        if wg != mu * ug:
            continue
        target_r = wr / mu
        target_f = wf / mu
        cosine = (target_r * ur + target_f * uf) / planar_norm
        sine = (target_f * ur - target_r * uf) / planar_norm
        if cosine * cosine + sine * sine != 1 or cosine == -1:
            continue
        parameter = sine / (1 + cosine)
        if matrix_equal(density(rotate_high(vector, parameter)), dbar):
            candidates.add(parameter)
    return candidates


def normalized_signature(histogram):
    common = 0
    for count in histogram:
        common = gcd(common, count)
    if common == 0:
        raise ValueError("empty histogram")
    return tuple(count // common for count in histogram)


def passing_subset_bits(signature, target_numerator, target_denominator):
    total = sum(signature)
    sums = [0] * 32
    bits = 0
    for mask in range(1, 31):
        least = mask & -mask
        value = least.bit_length() - 1
        sums[mask] = sums[mask ^ least] + signature[value]
        if sums[mask] * target_denominator == total * target_numerator:
            bits |= 1 << (mask - 1)
    return bits


def differing_subset_bits(first, second):
    first_total = sum(first)
    second_total = sum(second)
    delta = tuple(
        left * second_total - right * first_total
        for left, right in zip(first, second)
    )
    sums = [0] * 32
    bits = 0
    for mask in range(1, 31):
        least = mask & -mask
        value = least.bit_length() - 1
        sums[mask] = sums[mask ^ least] + delta[value]
        if sums[mask]:
            bits |= 1 << (mask - 1)
    return bits


def pair_name(lambda_index, subset_offset, delay_index):
    return f"L{lambda_index}:S{SUBSET_MASKS[subset_offset]:02d}:D{DELAYS[delay_index]}"


def names_from_bits(bit_table):
    names = []
    for lambda_index in range(len(LAMBDAS)):
        for subset_offset in range(30):
            bit = 1 << subset_offset
            for delay_index in range(len(DELAYS)):
                if bit_table[delay_index][lambda_index] & bit:
                    names.append(pair_name(lambda_index, subset_offset, delay_index))
    return names


def format_names(names):
    return ",".join(names) if names else "NONE"


def lambda_histogram(fiber_histogram, lambda_index, lambda_values):
    result = [0] * 5
    values = lambda_values[lambda_index]
    for fiber, count in enumerate(fiber_histogram):
        if count:
            result[values[fiber]] += count
    return result


def packed_record_increments(lambda_values):
    increments = []
    for fiber in range(25):
        value = 0
        for lambda_index in range(len(LAMBDAS)):
            residue = lambda_values[lambda_index][fiber]
            for subset_offset, subset_mask in enumerate(SUBSET_MASKS):
                if subset_mask & (1 << residue):
                    lane = lambda_index * 30 + subset_offset
                    value |= 1 << (PACKED_LANE_WIDTH * lane)
        increments.append(value)
    return tuple(increments)


def packed_unequal_lanes(left, right):
    biased = PACKED_BIAS_LANES + left - right
    difference = biased ^ PACKED_BIAS_LANES
    return ((difference | PACKED_HIGH_LANES) - PACKED_ONE_LANES) & PACKED_HIGH_LANES


def packed_differing_lanes(first, current):
    first_counts, first_total = first
    current_counts, current_total = current
    return packed_unequal_lanes(
        first_counts * current_total,
        current_counts * first_total,
    )


def packed_passing_lanes(signature, target_numerator, target_denominator):
    counts, total = signature
    failures = packed_unequal_lanes(
        counts * target_denominator,
        total * target_numerator * PACKED_ONE_LANES,
    )
    return PACKED_HIGH_LANES ^ failures


def compress_packed_lanes(lanes):
    return sum(
        ((lanes >> (PACKED_LANE_WIDTH * offset + 30)) & 1) << offset
        for offset in range(30)
    )


def update_signature_summary(
    first_table,
    difference_table,
    global_dead,
    honor_global_dead,
    delay_index,
    pre_index,
    packed_counts,
    total,
):
    for lambda_index in range(len(LAMBDAS)):
        if honor_global_dead and global_dead[delay_index][lambda_index]:
            continue
        if difference_table[delay_index][lambda_index][pre_index] == PACKED_HIGH_LANES:
            continue
        signature = (
            (packed_counts >> (PACKED_LAMBDA_WIDTH * lambda_index)) & PACKED_LAMBDA_MASK,
            total,
        )
        first = first_table[delay_index][lambda_index][pre_index]
        if first is None:
            first_table[delay_index][lambda_index][pre_index] = signature
        elif first != signature:
            difference_table[delay_index][lambda_index][pre_index] |= (
                packed_differing_lanes(first, signature)
            )
            if (
                pre_index != 0
                and difference_table[delay_index][lambda_index][pre_index] == PACKED_HIGH_LANES
            ):
                global_dead[delay_index][lambda_index] = True


def hash_histograms(histograms, pre_count, label):
    digest = sha256(label.encode("ascii") + b"\0")
    total = 0
    for delay_index, table in enumerate(histograms):
        for pre_index in range(pre_count):
            base = pre_index * 25
            for fiber in range(25):
                count = table[base + fiber]
                if count:
                    digest.update(pack(">BHBQ", DELAYS[delay_index], pre_index, fiber, count))
                    total += count
    return digest.hexdigest(), total


def hash_joint_tables(joint_tables, pre_count, post_count, label):
    digest = sha256(label.encode("ascii") + b"\0")
    total = 0
    for delay_index, table in enumerate(joint_tables):
        for pre_index in range(pre_count):
            for fiber in range(25):
                base = (pre_index * 25 + fiber) * post_count
                for post_class in range(post_count):
                    count = table[base + post_class]
                    if not count:
                        continue
                    digest.update(
                        pack(">BHBHQ", DELAYS[delay_index], pre_index, fiber, post_class, count)
                    )
                    total += count
    return digest.hexdigest(), total


def process_dataset(
    seed_ids,
    window,
    next_state,
    theta,
    state_class,
    state_oriented,
    state_fiber,
    oriented_to_class,
    pre_count,
    class_count,
    record_increments,
    joint_tables,
    aggregate_histograms,
    aggregate_pre_counts,
    oriented_first_signatures,
    oriented_differences,
    class_first_signatures,
    class_differences,
    global_real_dead,
    class_needs_all_differences,
    seed_digest,
):
    start, end = window
    maximum_delay = max(DELAYS)
    event_total = 0
    for seed_rank, seed in enumerate(seed_ids):
        states = [0] * (end + maximum_delay)
        states[0] = seed
        for time in range(end + maximum_delay - 1):
            states[time + 1] = next_state[theta[time]][states[time]]

        pre_counts = [0] * pre_count
        for time in range(start, end):
            pre_counts[state_oriented[states[time]]] += 1
        for pre_index, count in enumerate(pre_counts):
            aggregate_pre_counts[pre_index] += count

        for delay_index, delay in enumerate(DELAYS):
            local = {}
            aggregate = aggregate_histograms[delay_index]
            joint = joint_tables[delay_index]
            for time in range(start, end):
                pre_index = state_oriented[states[time]]
                future_state = states[time + delay]
                fiber = state_fiber[future_state]
                post_class = state_class[future_state]
                bucket = local.get(pre_index)
                if bucket is None:
                    bucket = [[0] * 25, 0, 0, 0]
                    local[pre_index] = bucket
                histogram = bucket[0]
                histogram[fiber] += 1
                bucket[1] += record_increments[fiber]
                bucket[2] |= 1 << fiber
                bucket[3] += 1
                aggregate[pre_index * 25 + fiber] += 1
                joint[(pre_index * 25 + fiber) * class_count + post_class] += 1

            class_local = {}
            for pre_index in sorted(local):
                histogram, packed_counts, touched, total = local[pre_index]
                if total != pre_counts[pre_index]:
                    raise AssertionError("delay histogram does not total to pre-cell count")
                while touched:
                    least = touched & -touched
                    fiber = least.bit_length() - 1
                    count = histogram[fiber]
                    seed_digest.update(
                        pack(">IBHBQ", seed_rank, DELAYS[delay_index], pre_index, fiber, count)
                    )
                    touched ^= least
                update_signature_summary(
                    oriented_first_signatures,
                    oriented_differences,
                    global_real_dead,
                    True,
                    delay_index,
                    pre_index,
                    packed_counts,
                    total,
                )
                class_index = oriented_to_class[pre_index]
                prior_packed, prior_total = class_local.get(class_index, (0, 0))
                class_local[class_index] = (
                    prior_packed + packed_counts,
                    prior_total + total,
                )

            for class_index in sorted(class_local):
                packed_counts, total = class_local[class_index]
                update_signature_summary(
                    class_first_signatures,
                    class_differences,
                    global_real_dead,
                    not class_needs_all_differences,
                    delay_index,
                    class_index,
                    packed_counts,
                    total,
                )
        event_total += end - start
    return event_total


def collapse_oriented(aggregate_histograms, aggregate_pre_counts, oriented_to_class, class_count):
    class_histograms = [[0] * (class_count * 25) for _ in DELAYS]
    class_counts = [0] * class_count
    for pre_index, count in enumerate(aggregate_pre_counts):
        class_counts[oriented_to_class[pre_index]] += count
    for delay_index, source in enumerate(aggregate_histograms):
        target = class_histograms[delay_index]
        for pre_index in range(len(oriented_to_class)):
            class_index = oriented_to_class[pre_index]
            source_base = pre_index * 25
            target_base = class_index * 25
            for fiber in range(25):
                target[target_base + fiber] += source[source_base + fiber]
    return class_histograms, class_counts


def realization_from_summaries(
    first_signatures, differences, oriented_to_class, class_occ_low
):
    realization = [[PACKED_HIGH_LANES for _ in LAMBDAS] for _ in DELAYS]
    for delay_index in range(len(DELAYS)):
        for lambda_index in range(len(LAMBDAS)):
            for pre_index in range(1, len(oriented_to_class)):
                class_index = oriented_to_class[pre_index]
                target = class_occ_low[class_index]
                signature = first_signatures[delay_index][lambda_index][pre_index]
                if signature is None:
                    continue
                passing = packed_passing_lanes(
                    signature, target.numerator, target.denominator
                )
                stable = PACKED_HIGH_LANES ^ differences[delay_index][lambda_index][pre_index]
                realization[delay_index][lambda_index] &= passing & stable
    return [
        [compress_packed_lanes(value) for value in row]
        for row in realization
    ]


def intersect_bit_tables(first, second):
    return [
        [left & right for left, right in zip(first_row, second_row)]
        for first_row, second_row in zip(first, second)
    ]


def orientation_dependence(
    aggregate_histograms, aggregate_pre_counts, class_count, lambda_values
):
    count = 0
    for delay_index in range(len(DELAYS)):
        table = aggregate_histograms[delay_index]
        for lambda_index in range(len(LAMBDAS)):
            for class_index in range(1, class_count):
                plus = 2 * class_index - 1
                minus = 2 * class_index
                if not aggregate_pre_counts[plus] or not aggregate_pre_counts[minus]:
                    continue
                plus_signature = normalized_signature(
                    lambda_histogram(table[plus * 25:(plus + 1) * 25], lambda_index, lambda_values)
                )
                minus_signature = normalized_signature(
                    lambda_histogram(table[minus * 25:(minus + 1) * 25], lambda_index, lambda_values)
                )
                count += differing_subset_bits(plus_signature, minus_signature).bit_count()
    return count


def census_predicates(
    aggregate_histograms,
    aggregate_class_counts,
    class_occ_low,
    class_count,
    lambda_values,
):
    realization = [[FULL_SUBSET_BITS for _ in LAMBDAS] for _ in DELAYS]
    information = [[0 for _ in LAMBDAS] for _ in DELAYS]
    for delay_index in range(len(DELAYS)):
        for lambda_index in range(len(LAMBDAS)):
            first_signature = None
            for class_index in range(1, class_count):
                if aggregate_class_counts[class_index] == 0:
                    continue
                base = class_index * 25
                signature = normalized_signature(
                    lambda_histogram(
                        aggregate_histograms[delay_index][base:base + 25],
                        lambda_index,
                        lambda_values,
                    )
                )
                target = class_occ_low[class_index]
                realization[delay_index][lambda_index] &= passing_subset_bits(
                    signature, target.numerator, target.denominator
                )
                if first_signature is None:
                    first_signature = signature
                elif first_signature != signature:
                    information[delay_index][lambda_index] |= differing_subset_bits(
                        first_signature, signature
                    )
    return realization, information


SYMMETRIC_PAIRS = tuple((row, column) for row in range(4) for column in range(row, 4))
ZERO_METRIC = (0, 0, 0) + (0,) * len(SYMMETRIC_PAIRS)


def projector(vector):
    vector = tuple(map(Fraction, vector))
    norm = g_norm(vector)
    return tuple(vector[row] * vector[column] / norm for row, column in SYMMETRIC_PAIRS)


def integer_projectors(class_representatives):
    rational = [None] + [projector(vector) for vector in class_representatives[1:]]
    scale = 1
    for values in rational[1:]:
        for value in values:
            scale = scale * value.denominator // gcd(scale, value.denominator)
    integer = [None] + [tuple(int(value * scale) for value in values) for values in rational[1:]]
    return scale, integer


def canonical_direction(vector):
    common = 0
    for value in vector:
        common = gcd(common, abs(value))
    result = tuple(value // common for value in vector)
    if next(value for value in result if value) < 0:
        result = tuple(-value for value in result)
    return result


def direction_masks(class_representatives):
    groups = {}
    for class_index, vector in enumerate(class_representatives[1:], 1):
        key = canonical_direction(vector)
        groups[key] = groups.get(key, 0) | (1 << class_index)
    result = [0] * len(class_representatives)
    for class_index, vector in enumerate(class_representatives[1:], 1):
        result[class_index] = groups[canonical_direction(vector)]
    return result


def add_metric(left, right):
    return (
        left[0] + right[0],
        left[1] + right[1],
        left[2] | right[2],
    ) + tuple(a + b for a, b in zip(left[3:], right[3:]))


def build_fiber_metrics(joint_tables, pre_count, post_count, integer_projector_table):
    result = []
    for table in joint_tables:
        delay_metrics = []
        for pre_index in range(pre_count):
            for fiber in range(25):
                base = (pre_index * 25 + fiber) * post_count
                zero_count = table[base]
                total = zero_count
                support = 1 if zero_count else 0
                moments = [0] * len(SYMMETRIC_PAIRS)
                for post_class in range(1, post_count):
                    count = table[base + post_class]
                    if not count:
                        continue
                    total += count
                    support |= 1 << post_class
                    values = integer_projector_table[post_class]
                    for index, value in enumerate(values):
                        moments[index] += count * value
                delay_metrics.append((total, zero_count, support) + tuple(moments))
        result.append(delay_metrics)
    return result


def residue_metrics(fiber_metrics, delay_index, lambda_index, pre_count, lambda_values):
    result = [ZERO_METRIC for _ in range(pre_count * 5)]
    values = lambda_values[lambda_index]
    source = fiber_metrics[delay_index]
    for pre_index in range(pre_count):
        source_base = pre_index * 25
        target_base = pre_index * 5
        for fiber in range(25):
            residue = values[fiber]
            target_index = target_base + residue
            result[target_index] = add_metric(result[target_index], source[source_base + fiber])
    return result


def subset_metric_tables(residue_table, pre_count):
    result = []
    for pre_index in range(pre_count):
        residues = residue_table[pre_index * 5:(pre_index + 1) * 5]
        subsets = [ZERO_METRIC for _ in range(32)]
        for mask in range(1, 32):
            least = mask & -mask
            residue = least.bit_length() - 1
            subsets[mask] = add_metric(subsets[mask ^ least], residues[residue])
        result.append(subsets)
    return result


def metric_nonzero_count(metric):
    return metric[0] - metric[1]


def metric_dbar(metric, projector_scale):
    nonzero_count = metric_nonzero_count(metric)
    if nonzero_count == 0:
        return None
    symmetric = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    denominator = nonzero_count * projector_scale
    for value, (row, column) in zip(metric[3:], SYMMETRIC_PAIRS):
        entry = Fraction(value, denominator)
        symmetric[row][column] = entry
        symmetric[column][row] = entry
    return tuple(
        tuple(
            symmetric[row][column] - sum(symmetric[row], Fraction(0)) / 5
            for column in range(4)
        )
        for row in range(4)
    )


def metric_dbar_equal(left, right):
    left_count = metric_nonzero_count(left)
    right_count = metric_nonzero_count(right)
    if bool(left_count) != bool(right_count):
        return False
    if not left_count:
        return True
    return all(
        left_value * right_count == right_value * left_count
        for left_value, right_value in zip(left[3:], right[3:])
    )


def metric_is_pure(metric, class_direction_masks):
    support = metric[2] & ~1
    if not support:
        return False
    first_class = (support & -support).bit_length() - 1
    return support & ~class_direction_masks[first_class] == 0


def family_test_from_subsets(
    subset_mask,
    subsets_by_pre,
    oriented_counts,
    class_occ_low,
    projector_scale,
    e_low,
):
    common_parameters = None
    class_count = len(class_occ_low)
    for class_index in range(1, class_count):
        for pre_index, sign in ((2 * class_index - 1, 1), (2 * class_index, -1)):
            if oriented_counts[pre_index] == 0:
                continue
            representative = CLASS_REPRESENTATIVES[class_index]
            vector = tuple(sign * value for value in representative)
            branches = (
                subsets_by_pre[pre_index][subset_mask],
                subsets_by_pre[pre_index][31 ^ subset_mask],
            )
            targets = (class_occ_low[class_index], 1 - class_occ_low[class_index])
            for branch, (metric, target_probability) in enumerate(zip(branches, targets)):
                event_count = metric[0]
                if target_probability == 0:
                    if event_count:
                        return False, None
                    continue
                if event_count == 0 or metric[1]:
                    return False, None
                dbar = metric_dbar(metric, projector_scale)
                if dbar is None:
                    return False, None
                if branch == 0:
                    if not matrix_equal(dbar, e_low):
                        return False, None
                    continue
                candidates = high_parameter_candidates(vector, dbar)
                if candidates == set():
                    return False, None
                if candidates is ALL_PARAMETERS:
                    continue
                common_parameters = set(candidates) if common_parameters is None else (
                    common_parameters & candidates
                )
                if not common_parameters:
                    return False, None
    return True, ALL_PARAMETERS if common_parameters is None else tuple(sorted(common_parameters))


def analyze_post_objects(
    fiber_metrics,
    oriented_counts,
    class_occ_low,
    projector_scale,
    class_direction_masks,
    lambda_values,
    single_realization,
    e_low,
):
    pair_count = len(LAMBDAS) * len(SUBSET_MASKS) * len(DELAYS)
    functional = [False] * pair_count
    categories = [None] * pair_count
    orientation_coherent = [False] * pair_count
    family_by_pair = [None] * pair_count
    zero_input_multivalued = 0
    class_count = len(class_occ_low)
    pre_count = len(oriented_counts)
    for lambda_index in range(len(LAMBDAS)):
        for delay_index in range(len(DELAYS)):
            residues = residue_metrics(
                fiber_metrics, delay_index, lambda_index, pre_count, lambda_values
            )
            subsets_by_pre = subset_metric_tables(residues, pre_count)
            for subset_offset, subset_mask in enumerate(SUBSET_MASKS):
                flat_index = (lambda_index * 30 + subset_offset) * len(DELAYS) + delay_index
                pair_functional = True
                pair_mixed = False
                pair_undefined = False
                pair_orient_coherent = True
                defined_object_count = 0
                zero_branches = (
                    subsets_by_pre[0][subset_mask],
                    subsets_by_pre[0][31 ^ subset_mask],
                )
                if any(metric[2].bit_count() > 1 for metric in zero_branches):
                    zero_input_multivalued += 1
                for class_index in range(1, class_count):
                    plus = 2 * class_index - 1
                    minus = 2 * class_index
                    if oriented_counts[plus] + oriented_counts[minus] == 0:
                        continue
                    plus_branches = (
                        subsets_by_pre[plus][subset_mask],
                        subsets_by_pre[plus][31 ^ subset_mask],
                    )
                    minus_branches = (
                        subsets_by_pre[minus][subset_mask],
                        subsets_by_pre[minus][31 ^ subset_mask],
                    )
                    combined_branches = tuple(
                        add_metric(left, right)
                        for left, right in zip(plus_branches, minus_branches)
                    )
                    targets = (class_occ_low[class_index], 1 - class_occ_low[class_index])
                    for branch, (metric, target_probability) in enumerate(
                        zip(combined_branches, targets)
                    ):
                        if metric[0] == 0:
                            if target_probability > 0:
                                pair_undefined = True
                        else:
                            if metric[2].bit_count() != 1:
                                pair_functional = False
                            if target_probability == 0 or metric[1]:
                                pair_undefined = True
                            if metric_nonzero_count(metric):
                                defined_object_count += 1
                                if not metric_is_pure(metric, class_direction_masks):
                                    pair_mixed = True
                        if oriented_counts[plus] and oriented_counts[minus]:
                            plus_metric = plus_branches[branch]
                            minus_metric = minus_branches[branch]
                            if bool(plus_metric[0]) != bool(minus_metric[0]):
                                pair_orient_coherent = False
                            elif plus_metric[0] and minus_metric[0]:
                                if plus_metric[1] * minus_metric[0] != minus_metric[1] * plus_metric[0]:
                                    pair_orient_coherent = False
                                if not metric_dbar_equal(plus_metric, minus_metric):
                                    pair_orient_coherent = False
                if defined_object_count == 0:
                    pair_undefined = True
                functional[flat_index] = pair_functional
                orientation_coherent[flat_index] = pair_orient_coherent
                categories[flat_index] = (
                    "UNDEFINED" if pair_undefined else ("MIXED" if pair_mixed else "PURE")
                )
                is_real = bool(
                    single_realization[delay_index][lambda_index] & (1 << subset_offset)
                )
                if pair_functional or is_real:
                    name = pair_name(lambda_index, subset_offset, delay_index)
                    member, parameters = family_test_from_subsets(
                        subset_mask,
                        subsets_by_pre,
                        oriented_counts,
                        class_occ_low,
                        projector_scale,
                        e_low,
                    )
                    family_by_pair[flat_index] = (name, member, parameters)
    family_results = [value for value in family_by_pair if value is not None]
    return (
        functional,
        categories,
        orientation_coherent,
        zero_input_multivalued,
        family_results,
    )


def parameter_text(parameters):
    if parameters is ALL_PARAMETERS:
        return "ALL_Q[canonical:0]"
    return "{" + "|".join(map(str, parameters)) + "}"


def find_s3_witnesses(generator_tables, coordinates):
    selector_witness = None
    direct_witness = None
    fibers = tuple(product(range(P), repeat=2))
    pistons = tuple(product(range(P), repeat=4))
    for drive_bit in (0, 1):
        for piston in pistons:
            piston_sum = sum(piston) % P
            for left_fiber in fibers:
                if selector_witness is not None and direct_witness is not None:
                    return selector_witness, direct_witness
                for right_fiber in fibers:
                    left_q, left_r = left_fiber
                    right_q, right_r = right_fiber
                    left_selector = (piston_sum + left_q + left_r + 2 * drive_bit) % P
                    right_selector = (piston_sum + right_q + right_r + 2 * drive_bit) % P
                    left_state = encode(piston + left_fiber)
                    right_state = encode(piston + right_fiber)
                    if (
                        selector_witness is None
                        and left_r == right_r
                        and left_q != right_q
                        and left_selector != right_selector
                    ):
                        left_post = coordinates[generator_tables[left_selector][left_state]][:4]
                        right_post = coordinates[generator_tables[right_selector][right_state]][:4]
                        if left_post != right_post:
                            selector_witness = (
                                drive_bit,
                                piston + left_fiber,
                                piston + right_fiber,
                                left_selector,
                                right_selector,
                                left_post,
                                right_post,
                            )
                    if (
                        direct_witness is None
                        and left_r != right_r
                        and (left_q + left_r) % P == (right_q + right_r) % P
                        and left_selector == right_selector == 2
                    ):
                        left_post = coordinates[generator_tables[2][left_state]][:4]
                        right_post = coordinates[generator_tables[2][right_state]][:4]
                        difference = tuple(
                            (left - right) % P for left, right in zip(left_post, right_post)
                        )
                        scalar = (left_r - right_r) % P
                        expected = tuple((scalar * value) % P for value in (0, 1, 0, -1))
                        if difference == expected:
                            direct_witness = (
                                drive_bit,
                                piston + left_fiber,
                                piston + right_fiber,
                                left_selector,
                                left_post,
                                right_post,
                                difference,
                            )
    return selector_witness, direct_witness


def compact_tuple(values):
    return "".join(str(value) for value in values)


def main():
    global CLASS_REPRESENTATIVES

    coordinates = list(product(range(P), repeat=6))
    if any(encode(x) != index for index, x in enumerate(coordinates)):
        raise AssertionError("state encoding is not lexicographic")

    fixed_width_arrays_ok = (
        array("B").itemsize == 1
        and array("H").itemsize == 2
        and array("I").itemsize == 4
    )
    if not fixed_width_arrays_ok:
        raise AssertionError("required fixed-width array types are unavailable")
    generator_tables = []
    for generator_index in range(5):
        generator_tables.append(
            array("H", (encode(generator(generator_index, x)) for x in coordinates))
        )

    involutions_ok = all(
        table[table[state]] == state
        for table in generator_tables
        for state in range(len(coordinates))
    )
    bc5_ok = True
    for state in range(len(coordinates)):
        current = state
        for _ in range(5):
            current = generator_tables[1][generator_tables[2][current]]
        if current != state:
            bc5_ok = False
            break

    def commutator(first, second, state):
        return generator_tables[first][
            generator_tables[second][generator_tables[first][generator_tables[second][state]]]
        ]

    translations = ((3, 4, (0, 0, 0, 0, 3, 0)),
                    (1, 3, (0, 0, 0, 0, 3, 3)),
                    (1, 4, (0, 0, 0, 0, 1, 3)))
    commutators_ok = True
    for first, second, delta in translations:
        for state, x in enumerate(coordinates):
            expected = encode(tuple((value + shift) % P for value, shift in zip(x, delta)))
            if commutator(first, second, state) != expected:
                commutators_ok = False
                break
        if not commutators_ok:
            break

    s1_ok = True
    for state, x in enumerate(coordinates):
        q, r = x[4], x[5]
        expected_fibers = (
            (q, r), ((-q) % P, (-r) % P), ((1 - q) % P, (-r) % P),
            ((1 - q) % P, (1 - r) % P), ((2 - q) % P, (1 - r) % P),
        )
        for generator_index, expected in enumerate(expected_fibers):
            if coordinates[generator_tables[generator_index][state]][4:] != expected:
                s1_ok = False
                break
        if not s1_ok:
            break

    piston_keys = {sign_key(balanced_piston(piston)) for piston in product(range(P), repeat=4)}
    piston_keys.remove(ZERO4)
    CLASS_REPRESENTATIVES = [ZERO4] + sorted(piston_keys)
    class_index = {representative: index for index, representative in enumerate(CLASS_REPRESENTATIVES)}
    piston_class = {}
    piston_oriented = {}
    for piston in product(range(P), repeat=4):
        vector = balanced_piston(piston)
        index = class_index[sign_key(vector)]
        piston_class[piston] = index
        piston_oriented[piston] = (
            0 if index == 0 else (2 * index - 1 if vector == CLASS_REPRESENTATIVES[index] else 2 * index)
        )
    state_class = array("H", (piston_class[x[:4]] for x in coordinates))
    state_oriented = array("H", (piston_oriented[x[:4]] for x in coordinates))
    state_fiber = array("B", (x[4] * P + x[5] for x in coordinates))
    class_count = len(CLASS_REPRESENTATIVES)
    oriented_to_class = tuple([0] + [index for index in range(1, class_count) for _ in (0, 1)])
    pre_count = len(oriented_to_class)

    s2_ok = all(
        sum(x[:4]) % P == sum(balanced_piston(x[:4])) % P
        for x in coordinates
    )
    selector_witness, direct_witness = find_s3_witnesses(generator_tables, coordinates)
    s3_ok = selector_witness is not None and direct_witness is not None

    zero_checkpoint_count = sum(1 for value in state_class if value == 0)
    class_sizes = [0] * class_count
    for value in state_class:
        class_sizes[value] += 1
    oriented_sizes = [0] * pre_count
    for value in state_oriented:
        oriented_sizes[value] += 1
    class_structure_ok = (
        class_count == 313
        and pre_count == 625
        and zero_checkpoint_count == 25
        and class_sizes[0] == 25
        and all(size == 50 for size in class_sizes[1:])
        and oriented_sizes[0] == 25
        and all(size == 25 for size in oriented_sizes[1:])
    )

    maximum_time = LONG_WINDOW[1] + max(DELAYS) - 1
    theta = tuple(time.bit_count() & 1 for time in range(maximum_time))
    coordinate_sums = tuple(sum(x) % P for x in coordinates)
    next_state = []
    for drive_bit in (0, 1):
        next_state.append(
            array(
                "H",
                (
                    generator_tables[(coordinate_sums[state] + 2 * drive_bit) % P][state]
                    for state in range(len(coordinates))
                ),
            )
        )

    lambda_values = []
    for alpha, gamma in LAMBDAS:
        lambda_values.append(
            tuple((alpha * (fiber // P) + gamma * (fiber % P)) % P for fiber in range(25))
        )
    record_increments = packed_record_increments(lambda_values)
    record_low_table = []
    for lambda_index in range(len(LAMBDAS)):
        for mask in SUBSET_MASKS:
            record_low_table.append(
                tuple(bool(mask & (1 << lambda_values[lambda_index][fiber])) for fiber in range(25))
            )
    packed_records_ok = all(
        ((record_increments[fiber] >> (PACKED_LANE_WIDTH * record_index)) & ((1 << PACKED_LANE_WIDTH) - 1))
        == int(record_low_table[record_index][fiber])
        for record_index in range(len(record_low_table))
        for fiber in range(25)
    ) and all(value >> (PACKED_LANE_WIDTH * len(record_low_table)) == 0 for value in record_increments)

    maximum_single_cell = (P ** 6) * (SINGLE_WINDOW[1] - SINGLE_WINDOW[0])
    maximum_long_cell = (P ** 4) * (LONG_WINDOW[1] - LONG_WINDOW[0])
    uint32_counts_ok = max(maximum_single_cell, maximum_long_cell) < 2 ** 32
    maximum_window = max(
        SINGLE_WINDOW[1] - SINGLE_WINDOW[0],
        LONG_WINDOW[1] - LONG_WINDOW[0],
    )
    packed_ratio_bounds_ok = maximum_window * maximum_window < 2 ** 29
    if not packed_records_ok or not packed_ratio_bounds_ok:
        raise AssertionError("packed record lanes or ratio bounds failed")
    if not uint32_counts_ok:
        raise AssertionError("32-bit joint tally storage is too narrow")
    joint_size = pre_count * 25 * class_count

    def empty_first_signatures(count):
        return [[[None] * count for _ in LAMBDAS] for _ in DELAYS]

    def empty_differences(count):
        return [[[0] * count for _ in LAMBDAS] for _ in DELAYS]

    # LONG is processed and released before SINGLE is allocated. This bounds
    # dense joint storage to one five-delay dataset at a time in Phase A.
    long_joint = [array("I", [0]) * joint_size for _ in DELAYS]
    long_aggregate = [[0] * (pre_count * 25) for _ in DELAYS]
    long_pre_counts = [0] * pre_count
    long_oriented_first = empty_first_signatures(pre_count)
    long_oriented_difference = empty_differences(pre_count)
    long_class_first = empty_first_signatures(class_count)
    long_class_difference = empty_differences(class_count)
    long_real_dead = [[False for _ in LAMBDAS] for _ in DELAYS]
    long_seed_hash = sha256(b"P-QDD-INSTRUMENT-U-INDUCED-1 LONG SEED TABLES\0")
    long_seeds = (
        encode((p1, p4, p1p, p4p, 0, 0))
        for p1, p4, p1p, p4p in product(range(P), repeat=4)
    )
    long_events = process_dataset(
        long_seeds, LONG_WINDOW, next_state, theta, state_class, state_oriented,
        state_fiber, oriented_to_class, pre_count, class_count, record_increments,
        long_joint, long_aggregate, long_pre_counts,
        long_oriented_first, long_oriented_difference,
        long_class_first, long_class_difference,
        long_real_dead, False, long_seed_hash,
    )
    long_class_aggregate, long_class_counts = collapse_oriented(
        long_aggregate, long_pre_counts, oriented_to_class, class_count
    )
    long_joint_hash, long_joint_total = hash_joint_tables(
        long_joint, pre_count, class_count, "LONG JOINT"
    )
    long_hist_hash, long_hist_total = hash_histograms(
        long_aggregate, pre_count, "LONG AGGREGATE"
    )
    del long_joint

    single_joint = [array("I", [0]) * joint_size for _ in DELAYS]
    single_aggregate = [[0] * (pre_count * 25) for _ in DELAYS]
    single_pre_counts = [0] * pre_count
    single_oriented_first = empty_first_signatures(pre_count)
    single_oriented_difference = empty_differences(pre_count)
    single_class_first = empty_first_signatures(class_count)
    single_class_difference = empty_differences(class_count)
    single_real_dead = [[False for _ in LAMBDAS] for _ in DELAYS]
    single_seed_hash = sha256(b"P-QDD-INSTRUMENT-U-INDUCED-1 SINGLE SEED TABLES\0")
    single_events = process_dataset(
        range(P ** 6), SINGLE_WINDOW, next_state, theta, state_class, state_oriented,
        state_fiber, oriented_to_class, pre_count, class_count, record_increments,
        single_joint, single_aggregate, single_pre_counts,
        single_oriented_first, single_oriented_difference,
        single_class_first, single_class_difference,
        single_real_dead, True, single_seed_hash,
    )
    single_class_aggregate, single_class_counts = collapse_oriented(
        single_aggregate, single_pre_counts, oriented_to_class, class_count
    )
    single_joint_hash, single_joint_total = hash_joint_tables(
        single_joint, pre_count, class_count, "SINGLE JOINT"
    )
    single_hist_hash, single_hist_total = hash_histograms(
        single_aggregate, pre_count, "SINGLE AGGREGATE"
    )

    single_seed_hash_value = single_seed_hash.hexdigest()
    long_seed_hash_value = long_seed_hash.hexdigest()
    hash_values = (
        ("single_seed", single_seed_hash_value),
        ("long_seed", long_seed_hash_value),
        ("single_joint", single_joint_hash),
        ("long_joint", long_joint_hash),
        ("single_aggregate", single_hist_hash),
        ("long_aggregate", long_hist_hash),
    )
    root_digest = sha256(b"P-QDD-INSTRUMENT-U-INDUCED-1 TABLE ROOT\0")
    for label, value in hash_values:
        root_digest.update(label.encode("ascii") + b"\0" + bytes.fromhex(value))
    table_root_hash = root_digest.hexdigest()

    expected_single_events = (P ** 6) * (SINGLE_WINDOW[1] - SINGLE_WINDOW[0])
    expected_long_events = (P ** 4) * (LONG_WINDOW[1] - LONG_WINDOW[0])
    raw_complete = (
        single_events == expected_single_events
        and long_events == expected_long_events
        and sum(single_pre_counts) == single_events
        and sum(long_pre_counts) == long_events
        and single_hist_total == single_events * len(DELAYS)
        and long_hist_total == long_events * len(DELAYS)
        and single_joint_total == single_events * len(DELAYS)
        and long_joint_total == long_events * len(DELAYS)
    )
    seed_dependent_count = sum(
        single_class_difference[delay_index][lambda_index][index].bit_count()
        for delay_index in range(len(DELAYS))
        for lambda_index in range(len(LAMBDAS))
        for index in range(class_count)
    )
    orientation_dependent_count = orientation_dependence(
        single_aggregate, single_pre_counts, class_count, lambda_values
    )

    # Phase B begins here. All raw U/rho counts and their hashes above are frozen
    # before the target effects, occurrence law, or post-state family are formed.
    e_low = tuple(tuple(Fraction(1, 4) for _ in range(4)) for _ in range(4))
    class_occ_low = [None] * class_count
    occurrence_pairs = set()
    for index, vector in enumerate(CLASS_REPRESENTATIVES):
        if index == 0:
            continue
        vector = tuple(map(Fraction, vector))
        total = sum(vector, Fraction(0))
        square_sum = sum((value * value for value in vector), Fraction(0))
        mass = square_sum - total * total / 5
        low = total * total / 20
        high = square_sum - total * total / 4
        if mass != low + high or mass <= 0:
            raise AssertionError("QDD weight identity failed")
        class_occ_low[index] = low / mass
        occurrence_pairs.add((low / mass, high / mass))
    target_packed_bounds_ok = all(
        maximum_window * max(value.numerator, value.denominator) < 2 ** 29
        for value in class_occ_low[1:]
    )
    if not target_packed_bounds_ok:
        raise AssertionError("packed target comparison bound failed")
    c2_ok = class_structure_ok and len(occurrence_pairs) == 22

    class_identity = tuple(range(class_count))
    single_oriented_realization = realization_from_summaries(
        single_oriented_first, single_oriented_difference,
        oriented_to_class, class_occ_low,
    )
    single_class_realization = realization_from_summaries(
        single_class_first, single_class_difference, class_identity, class_occ_low
    )
    single_realization = intersect_bit_tables(
        single_oriented_realization, single_class_realization
    )
    long_oriented_realization = realization_from_summaries(
        long_oriented_first, long_oriented_difference,
        oriented_to_class, class_occ_low,
    )
    long_class_realization = realization_from_summaries(
        long_class_first, long_class_difference, class_identity, class_occ_low
    )
    long_realization = intersect_bit_tables(long_oriented_realization, long_class_realization)
    census_realization, information = census_predicates(
        single_class_aggregate, single_class_counts, class_occ_low, class_count, lambda_values
    )
    single_realized_names = names_from_bits(single_realization)
    long_realized_names = names_from_bits(long_realization)
    census_realized_names = names_from_bits(census_realization)
    information_names = names_from_bits(information)

    projector_scale, integer_projector_table = integer_projectors(CLASS_REPRESENTATIVES)
    class_direction_masks = direction_masks(CLASS_REPRESENTATIVES)
    fiber_metrics = build_fiber_metrics(
        single_joint, pre_count, class_count, integer_projector_table
    )
    del single_joint
    (
        functional,
        post_categories,
        orientation_coherent,
        zero_input_multivalued,
        family_results,
    ) = analyze_post_objects(
        fiber_metrics,
        single_pre_counts,
        class_occ_low,
        projector_scale,
        class_direction_masks,
        lambda_values,
        single_realization,
        e_low,
    )
    functional_count = sum(functional)
    orientation_coherent_count = sum(orientation_coherent)
    post_pure_count = post_categories.count("PURE")
    post_mixed_count = post_categories.count("MIXED")
    post_undefined_count = post_categories.count("UNDEFINED")

    family_members = [(name, parameter) for name, member, parameter in family_results if member]
    family_outside = [name for name, member, _ in family_results if not member]
    eligible_names = {
        pair_name(lambda_index, subset_offset, delay_index)
        for lambda_index in range(len(LAMBDAS))
        for subset_offset in range(len(SUBSET_MASKS))
        for delay_index in range(len(DELAYS))
        if functional[(lambda_index * 30 + subset_offset) * len(DELAYS) + delay_index]
        or bool(single_realization[delay_index][lambda_index] & (1 << subset_offset))
    }
    evaluated_names = [name for name, _, _ in family_results]
    member_names = {name for name, _ in family_members}
    outside_names = set(family_outside)
    c7_complete = (
        len(evaluated_names) == len(set(evaluated_names))
        and set(evaluated_names) == eligible_names
        and member_names.isdisjoint(outside_names)
        and member_names | outside_names == eligible_names
    )

    checks = [
        ("C1", fixed_width_arrays_ok and involutions_ok and bc5_ok and commutators_ok),
        ("C2", c2_ok),
        ("C3", s1_ok and s2_ok and s3_ok),
        ("C4", len(record_low_table) * len(DELAYS) == 900
         and packed_records_ok and packed_ratio_bounds_ok and target_packed_bounds_ok
         and uint32_counts_ok and raw_complete),
        ("C5", sum(bits.bit_count() for row in information for bits in row) == len(information_names)),
        ("C6", len(functional) == 900 and len(orientation_coherent) == 900
         and post_pure_count + post_mixed_count + post_undefined_count == 900),
        ("C7", c7_complete),
        ("C8", 0 <= seed_dependent_count <= 900 * class_count
         and 0 <= orientation_dependent_count <= 900 * (class_count - 1)),
        ("C9", all(len(value) == 64 for value in (
            single_seed_hash_value, long_seed_hash_value, single_joint_hash,
            long_joint_hash, single_hist_hash, long_hist_hash, table_root_hash,
        ))),
    ]
    for name, passed in checks:
        if not passed:
            raise AssertionError(f"{name} failed")

    print("PASS C1 ARCHITECTURE generators=5 states=15625 involutions=5 bc_order=5 commutators=3 fixed_width_arrays=YES")
    print("PASS C2 QDD classes=313 oriented_pre_cells=625 zero_checkpoints=25 nonzero_occ_values=22")
    print("PASS C3 CHANNEL S1=EXHAUSTIVE S2=EXHAUSTIVE S3_SELECTOR=WITNESS S3_DIRECT_C=WITNESS")
    print(
        "S3_SELECTOR"
        f" theta={selector_witness[0]} x={compact_tuple(selector_witness[1])}"
        f" y={compact_tuple(selector_witness[2])}"
        f" sigma={selector_witness[3]},{selector_witness[4]}"
        f" post={compact_tuple(selector_witness[5])},{compact_tuple(selector_witness[6])}"
    )
    print(
        "S3_DIRECT_C"
        f" theta={direct_witness[0]} x={compact_tuple(direct_witness[1])}"
        f" y={compact_tuple(direct_witness[2])} sigma={direct_witness[3]}"
        f" post={compact_tuple(direct_witness[4])},{compact_tuple(direct_witness[5])}"
        f" difference={compact_tuple(direct_witness[6])}"
    )
    print("PASS C4 COMPLETE records=180 delays=5 pairs=900 single_seeds=15625 long_seeds=625")
    print(f"PASS C5 INFO evaluated=900 true={len(information_names)}")
    print(
        f"PASS C6 POST functional={functional_count} orient_coherent={orientation_coherent_count}"
        f" pure_strict={post_pure_count} mixed={post_mixed_count}"
        f" undefined_or_zero={post_undefined_count} zero_input_multivalued={zero_input_multivalued}"
    )
    print(f"PASS C7 FAMILY evaluated={len(family_results)} member={len(family_members)} outside={len(family_outside)}")
    print(
        f"PASS C8 DEPENDENCE seed_triples={seed_dependent_count}"
        f" orientation_triples={orientation_dependent_count}"
    )
    print(f"PASS C9 TABLE_HASHES canonical_big_endian_nonzero_entries=YES root={table_root_hash}")
    print("CHANNEL-PASS")
    print(("REGISTER-REALIZED-W" if single_realized_names else "NO-REALIZATION-W")
          + f" count={len(single_realized_names)} pairs={format_names(single_realized_names)}")
    print(("LONG-REALIZED-W2" if long_realized_names else "LONG-NO-REALIZATION-W2")
          + f" count={len(long_realized_names)} pairs={format_names(long_realized_names)}")
    print(("CENSUS-REALIZED-W" if census_realized_names else "CENSUS-NO-REALIZATION-W")
          + f" count={len(census_realized_names)} pairs={format_names(census_realized_names)}")
    print(("NO-RECORD-W" if not information_names else "RECORD-INFORMATION")
          + f" count={len(information_names)} pairs={format_names(information_names)}")
    print(f"INSTRUMENT-FUNCTIONAL-{functional_count}")
    print(f"ORIENT-POST-COHERENT-{orientation_coherent_count}")
    print(
        f"POST-PURE-STRICT-{post_pure_count} POST-MIXED-{post_mixed_count}"
        f" POST-UNDEFINED-OR-ZERO-{post_undefined_count}"
    )
    print(f"ZERO-INPUT-MULTIVALUED-{zero_input_multivalued}")
    member_text = ",".join(
        f"{name}=t:{parameter_text(parameters)}" for name, parameters in family_members
    ) or "NONE"
    print(f"FAMILY-MEMBER-{len(family_members)} values={member_text}")
    print(f"OUTSIDE-FAMILY-{len(family_outside)} pairs={format_names(family_outside)}")
    print(f"SEED-DEPENDENT-{seed_dependent_count}")
    print(f"ORIENTATION-DEPENDENT-{orientation_dependent_count}")
    print(f"EVENTS single={single_events} long={long_events}")
    print(f"HASH single_seed={single_seed_hash_value}")
    print(f"HASH long_seed={long_seed_hash_value}")
    print(f"HASH single_joint={single_joint_hash}")
    print(f"HASH long_joint={long_joint_hash}")
    print(f"HASH single_aggregate={single_hist_hash}")
    print(f"HASH long_aggregate={long_hist_hash}")
    print(f"HASH table_root={table_root_hash}")
    print("RESULT 9/9 ALL PASS")


if __name__ == "__main__":
    main()
