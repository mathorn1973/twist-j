#!/usr/bin/env python3
"""Blind, independent exact checker for P-QDD-INSTRUMENT-U-INDUCED-1.

This program was derived only from PREREG.md.  Its Phase A representation is
deliberately different from the accepted verifier described there: for every
visited oriented cell it packs 5 delays x 6 linear forms x 5 *residue* counts.
The 30 record-subset counts are recovered later by a five-element subset-sum
transform.  Universal predicates are retained as target-free proportionality
summaries.  Targets are constructed only after every orbit count is complete.

The checker covers the decisive scientific predicates REAL-SINGLE,
REAL-LONG, REAL-CENSUS and INFO, both dependence counts, and the C1--C3
generator/update/channel integrity layer.  It intentionally does not attempt
the induced post-object, family, or accepted-verifier serialization checks.

Python standard library only.  All arithmetic is integer or Fraction; there
is no floating-point path.
"""

from fractions import Fraction
from itertools import product


MOD = 5
STATE_COUNT = 5 ** 6
PISTON_COUNT = 5 ** 4
CLASS_COUNT = 313
ORIENTED_COUNT = 625
MAX_REGISTER_TIME = 16388

WINDOW_SINGLE = (512, 2048)
WINDOW_LONG = (2048, 16384)
SINGLE_SEEDS = STATE_COUNT
LONG_SEEDS = PISTON_COUNT

LAMBDAS = ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4))
DELAYS = (1, 2, 3, 4, 5)
BLOCK_COUNT = len(DELAYS) * len(LAMBDAS)
SUBSET_FULL = (1 << 30) - 1       # bits correspond to subset masks 1..30

# A lane holds one residue-bin count.  30 bits also makes multiplication of a
# per-seed lane by another per-seed event total carry-free:
# 14336**2 < 2**28 < 2**30.
LANE_BITS = 30
LANE_MASK = (1 << LANE_BITS) - 1
BLOCK_BITS = 5 * LANE_BITS
BLOCK_MASK = (1 << BLOCK_BITS) - 1

BALANCED = (0, 1, 2, -2, -1)


class IntegrityStop(RuntimeError):
    """Raised only for an architecture/integrity failure."""


def require(condition, label):
    if not condition:
        raise IntegrityStop(label)


def encode(x):
    value = 0
    for coordinate in x:
        value = MOD * value + coordinate
    return value


def decode(value):
    out = [0] * 6
    for index in range(5, -1, -1):
        value, out[index] = divmod(value, MOD)
    return tuple(out)


def decode_piston(value):
    out = [0] * 4
    for index in range(3, -1, -1):
        value, out[index] = divmod(value, MOD)
    return tuple(out)


# Main dynamics uses these affine tables.  The literal formulas below are a
# separately expressed transcription used for the exhaustive cross-audit.
AFFINE = (
    (
        ((0, 1, 0, 0, 0, 0),
         (1, 0, 0, 0, 0, 0),
         (0, 0, 0, 1, 0, 0),
         (0, 0, 1, 0, 0, 0),
         (0, 0, 0, 0, 1, 0),
         (0, 0, 0, 0, 0, 1)),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        ((0, 0, 4, 0, 0, 0),
         (0, 0, 0, 4, 0, 0),
         (4, 0, 0, 0, 0, 0),
         (0, 4, 0, 0, 0, 0),
         (0, 0, 0, 0, 4, 0),
         (0, 0, 0, 0, 0, 4)),
        (0, 0, 0, 0, 0, 0),
    ),
    (
        ((0, 0, 4, 0, 0, 0),
         (0, 0, 0, 4, 0, 1),
         (4, 0, 0, 0, 0, 0),
         (0, 4, 0, 0, 0, 4),
         (0, 0, 0, 0, 4, 0),
         (0, 0, 0, 0, 0, 4)),
        (2, 1, 2, 1, 1, 0),
    ),
    (
        ((4, 0, 0, 0, 0, 0),
         (0, 4, 0, 0, 0, 0),
         (0, 0, 4, 0, 0, 0),
         (0, 0, 0, 4, 0, 0),
         (0, 0, 0, 0, 4, 0),
         (0, 0, 0, 0, 0, 4)),
        (2, 1, 3, 4, 1, 1),
    ),
    (
        ((4, 0, 0, 0, 0, 0),
         (0, 4, 0, 0, 0, 0),
         (0, 0, 4, 0, 0, 0),
         (0, 0, 0, 4, 0, 0),
         (0, 0, 0, 0, 4, 0),
         (0, 0, 0, 0, 0, 4)),
        (2, 1, 3, 4, 2, 1),
    ),
)


def apply_generator(index, x):
    matrix, offset = AFFINE[index]
    return tuple(
        (offset[row] + sum(matrix[row][col] * x[col] for col in range(6))) % MOD
        for row in range(6)
    )


def literal_generator(index, x):
    p1, p4, p1p, p4p, q, r = x
    if index == 0:
        return p4, p1, p4p, p1p, q, r
    if index == 1:
        return (-p1p) % MOD, (-p4p) % MOD, (-p1) % MOD, (-p4) % MOD, (-q) % MOD, (-r) % MOD
    if index == 2:
        return (
            (-p1p + 2) % MOD,
            (-p4p + 1 + r) % MOD,
            (-p1 + 2) % MOD,
            (-p4 + 1 - r) % MOD,
            (1 - q) % MOD,
            (-r) % MOD,
        )
    if index == 3:
        constants = (2, 1, 3, 4, 1, 1)
        return tuple((constants[i] - x[i]) % MOD for i in range(6))
    constants = (2, 1, 3, 4, 2, 1)
    return tuple((constants[i] - x[i]) % MOD for i in range(6))


def expected_fiber(index, q, r):
    if index == 0:
        return q, r
    if index == 1:
        return (-q) % MOD, (-r) % MOD
    if index == 2:
        return (1 - q) % MOD, (-r) % MOD
    if index == 3:
        return (1 - q) % MOD, (1 - r) % MOD
    return (2 - q) % MOD, (1 - r) % MOD


def selector(theta, x):
    return (sum(x) + 2 * theta) % MOD


def commutator(g, h, x):
    # All five frozen generators are involutions, so this is
    # g o h o g^{-1} o h^{-1}, with maps composed rightmost first.
    return apply_generator(g, apply_generator(h, apply_generator(g, apply_generator(h, x))))


def translate(x, delta):
    return tuple((x[i] + delta[i]) % MOD for i in range(6))


def build_classes():
    piston_vectors = []
    representatives = set()
    for piston_id in range(PISTON_COUNT):
        piston = decode_piston(piston_id)
        vector = tuple(BALANCED[z] for z in piston)
        piston_vectors.append(vector)
        if any(vector):
            representatives.add(min(vector, tuple(-z for z in vector)))

    ordered = sorted(representatives)
    require(len(ordered) == 312, "C2 nonzero-class count")
    number = {representative: i + 1 for i, representative in enumerate(ordered)}

    piston_class = [0] * PISTON_COUNT
    piston_pre_cell = [0] * PISTON_COUNT
    for piston_id, vector in enumerate(piston_vectors):
        if not any(vector):
            continue
        representative = min(vector, tuple(-z for z in vector))
        cls = number[representative]
        piston_class[piston_id] = cls
        # IDs 2c-1 and 2c are the + and - cells of class c.
        piston_pre_cell[piston_id] = 2 * cls - 1 if vector == representative else 2 * cls

    require(len(set(piston_pre_cell)) == ORIENTED_COUNT, "C2 oriented-cell count")
    require(sum(1 for c in piston_class if c == 0) * 25 == 25, "C2 ZERO checkpoint count")
    return (tuple((0, 0, 0, 0) for _ in range(1)) + tuple(ordered),
            piston_class, piston_pre_cell)


def audit_integrity(class_representatives, piston_class, piston_pre_cell):
    del class_representatives, piston_class
    states = [decode(state_id) for state_id in range(STATE_COUNT)]

    for x in states:
        for generator in range(5):
            y = apply_generator(generator, x)
            require(y == literal_generator(generator, x), "C1 affine/literal generator mismatch")
            require(y[4:] == expected_fiber(generator, x[4], x[5]), "C3 S1 fiber rule")
            require(apply_generator(generator, y) == x, "C1 involution relation")

        y = x
        for _ in range(5):
            y = apply_generator(1, apply_generator(2, y))
        require(y == x, "C1 (bc)^5 relation")

        require(commutator(3, 4, x) == translate(x, (0, 0, 0, 0, 3, 0)), "C1 [d,e]")
        require(commutator(1, 3, x) == translate(x, (0, 0, 0, 0, 3, 3)), "C1 [b,d]")
        require(commutator(1, 4, x) == translate(x, (0, 0, 0, 0, 1, 3)), "C1 [b,e]")

        balanced_sum = sum(BALANCED[z] for z in x[:4]) % MOD
        require(balanced_sum == sum(x[:4]) % MOD, "C3 S2 balanced piston sum")
        for theta in (0, 1):
            expected = (balanced_sum + x[4] + x[5] + 2 * theta) % MOD
            require(selector(theta, x) == expected, "C3 S2 selector factorization")

    require(sorted(piston_pre_cell) == list(range(ORIENTED_COUNT)), "C2 pre-cell bijection")

    selector_witness = None
    direct_c_witness = None
    u_c = (0, 1, 0, -1)
    s_c = (2, 1, 2, 1)

    for theta in (0, 1):
        for piston in product(range(MOD), repeat=4):
            for q in range(MOD):
                for r in range(MOD):
                    x = piston + (q, r)
                    sx = selector(theta, x)
                    y = apply_generator(sx, x)
                    for qp in range(MOD):
                        for rp in range(MOD):
                            xp = piston + (qp, rp)
                            sxp = selector(theta, xp)
                            yp = apply_generator(sxp, xp)

                            if (selector_witness is None and q != qp and r == rp and
                                    sx != sxp and y[:4] != yp[:4]):
                                selector_witness = (theta, piston, (q, r), (qp, rp), sx, sxp, y[:4], yp[:4])

                            if (direct_c_witness is None and r != rp and
                                    (q + r) % MOD == (qp + rp) % MOD and sx == 2 and sxp == 2):
                                base = ((-piston[2] + s_c[0]) % MOD,
                                        (-piston[3] + s_c[1]) % MOD,
                                        (-piston[0] + s_c[2]) % MOD,
                                        (-piston[1] + s_c[3]) % MOD)
                                direct = tuple((y[i] - base[i]) % MOD for i in range(4))
                                directp = tuple((yp[i] - base[i]) % MOD for i in range(4))
                                expected = tuple(((r - rp) * u_c[i]) % MOD for i in range(4))
                                difference = tuple((y[i] - yp[i]) % MOD for i in range(4))
                                if (direct == tuple((r * u_c[i]) % MOD for i in range(4)) and
                                        directp == tuple((rp * u_c[i]) % MOD for i in range(4)) and
                                        difference == expected):
                                    direct_c_witness = (theta, piston, (q, r), (qp, rp), sx, y[:4], yp[:4])

                            if selector_witness is not None and direct_c_witness is not None:
                                return selector_witness, direct_c_witness

    require(selector_witness is not None, "C3 S3_SELECTOR witness absent")
    require(direct_c_witness is not None, "C3 S3_DIRECT_C witness absent")
    return selector_witness, direct_c_witness


def make_transitions():
    theta_bits = tuple(n.bit_count() & 1 for n in range(MAX_REGISTER_TIME))
    transitions = ([0] * STATE_COUNT, [0] * STATE_COUNT)
    for state_id in range(STATE_COUNT):
        x = decode(state_id)
        for theta in (0, 1):
            transitions[theta][state_id] = encode(apply_generator(selector(theta, x), x))
    return theta_bits, (tuple(transitions[0]), tuple(transitions[1]))


def make_fiber_increments():
    increments = [[0] * 25 for _ in DELAYS]
    for delay_index in range(len(DELAYS)):
        for fiber_id in range(25):
            q, r = divmod(fiber_id, MOD)
            packed = 0
            for lambda_index, (alpha, gamma) in enumerate(LAMBDAS):
                residue = (alpha * q + gamma * r) % MOD
                block = delay_index * len(LAMBDAS) + lambda_index
                lane = 5 * block + residue
                packed |= 1 << (LANE_BITS * lane)
            increments[delay_index][fiber_id] = packed
    return tuple(tuple(row) for row in increments)


def packed_bins(packed, block):
    chunk = (packed >> (BLOCK_BITS * block)) & BLOCK_MASK
    return tuple((chunk >> (LANE_BITS * residue)) & LANE_MASK for residue in range(5))


def subset_sums(values):
    sums = [0] * 32
    for mask in range(1, 32):
        bit = mask & -mask
        sums[mask] = sums[mask ^ bit] + values[bit.bit_length() - 1]
    return sums


def unequal_subset_bits(packed, total, reference, reference_total, block, candidates):
    """Return candidate record bits whose two exact rates are unequal."""
    if not candidates:
        return 0
    shift = BLOCK_BITS * block
    chunk = (packed >> shift) & BLOCK_MASK
    reference_chunk = (reference >> shift) & BLOCK_MASK
    # Per-seed cross-products fit in their 30-bit lanes, so this is a cheap
    # exact all-five-residue equality test, without broadword guard tricks.
    # Aggregate census products can exceed a lane; in that case we deliberately
    # bypass the packed shortcut and use the scalar delta calculation below.
    if (total * reference_total < (1 << LANE_BITS) and
            chunk * reference_total == reference_chunk * total):
        return 0
    values = packed_bins(packed, block)
    reference_values = packed_bins(reference, block)
    delta = tuple(values[i] * reference_total - reference_values[i] * total for i in range(5))
    sums = subset_sums(delta)
    unequal = 0
    bits = candidates
    while bits:
        bit = bits & -bits
        mask = bit.bit_length()
        if sums[mask] != 0:
            unequal |= bit
        bits ^= bit
    return unequal


def target_mismatch_bits(packed, total, block, numerator, denominator, candidates):
    """Return candidate record bits whose exact rate misses num/den."""
    values = packed_bins(packed, block)
    sums = subset_sums(values)
    right = total * numerator
    mismatch = 0
    bits = candidates
    while bits:
        bit = bits & -bits
        mask = bit.bit_length()
        if sums[mask] * denominator != right:
            mismatch |= bit
        bits ^= bit
    return mismatch


def new_summary():
    return {
        "reference": [0] * CLASS_COUNT,
        "total": [0] * CLASS_COUNT,
        "different": [[0] * BLOCK_COUNT for _ in range(CLASS_COUNT)],
        "complete": [False] * CLASS_COUNT,
    }


def observe(summary, cls, packed, total):
    if total == 0 or summary["complete"][cls]:
        return
    reference_total = summary["total"][cls]
    if reference_total == 0:
        summary["reference"][cls] = packed
        summary["total"][cls] = total
        return

    reference = summary["reference"][cls]
    # This whole-profile proportionality test is carry-free for both windows.
    if packed * reference_total == reference * total:
        return

    all_complete = True
    differences = summary["different"][cls]
    for block in range(BLOCK_COUNT):
        candidates = SUBSET_FULL & ~differences[block]
        if candidates:
            differences[block] |= unequal_subset_bits(
                packed, total, reference, reference_total, block, candidates
            )
        if differences[block] != SUBSET_FULL:
            all_complete = False
    summary["complete"][cls] = all_complete


def update_oriented_summary(summary, profiles, totals):
    # REAL-ORIENT is sufficient for REAL-CLASS as well: for a fixed class the
    # class count is the disjoint sum of its present orientations, and both
    # have the same sign-invariant target.  Thus this summary is exactly REAL.
    for pre_cell in range(1, ORIENTED_COUNT):
        if totals[pre_cell]:
            observe(summary, (pre_cell + 1) // 2, profiles[pre_cell], totals[pre_cell])


def update_seed_summary(summary, profiles, totals):
    # The seed-dependence definition is class-collapsed and includes ZERO.
    if totals[0]:
        observe(summary, 0, profiles[0], totals[0])
    for cls in range(1, CLASS_COUNT):
        plus = 2 * cls - 1
        minus = 2 * cls
        total = totals[plus] + totals[minus]
        if total:
            observe(summary, cls, profiles[plus] + profiles[minus], total)


def orbit_profile(seed, start, end, theta_bits, transitions, piston_pre_cell, increments):
    last_time = end + max(DELAYS) - 1
    trajectory = [0] * (last_time + 1)
    trajectory[0] = seed
    state = seed
    for n in range(last_time):
        state = transitions[theta_bits[n]][state]
        trajectory[n + 1] = state

    profiles = [0] * ORIENTED_COUNT
    totals = [0] * ORIENTED_COUNT
    inc0, inc1, inc2, inc3, inc4 = increments
    pre_map = piston_pre_cell
    for k in range(start, end):
        pre_cell = pre_map[trajectory[k] // 25]
        event_increment = (
            inc0[trajectory[k + 1] % 25]
            | inc1[trajectory[k + 2] % 25]
            | inc2[trajectory[k + 3] % 25]
            | inc3[trajectory[k + 4] % 25]
            | inc4[trajectory[k + 5] % 25]
        )
        profiles[pre_cell] += event_increment
        totals[pre_cell] += 1

    require(sum(totals) == end - start, "Phase A per-seed event total")
    return profiles, totals


def phase_a_single(theta_bits, transitions, piston_pre_cell, increments):
    oriented_summary = new_summary()
    seed_summary = new_summary()
    aggregate_profiles = [0] * ORIENTED_COUNT
    aggregate_totals = [0] * ORIENTED_COUNT
    start, end = WINDOW_SINGLE

    for seed in range(STATE_COUNT):
        profiles, totals = orbit_profile(
            seed, start, end, theta_bits, transitions, piston_pre_cell, increments
        )
        update_oriented_summary(oriented_summary, profiles, totals)
        update_seed_summary(seed_summary, profiles, totals)
        for pre_cell in range(ORIENTED_COUNT):
            if totals[pre_cell]:
                aggregate_profiles[pre_cell] += profiles[pre_cell]
                aggregate_totals[pre_cell] += totals[pre_cell]

    require(sum(aggregate_totals) == SINGLE_SEEDS * (end - start), "Phase A SINGLE total")
    return oriented_summary, seed_summary, aggregate_profiles, aggregate_totals


def phase_a_long(theta_bits, transitions, piston_pre_cell, increments):
    oriented_summary = new_summary()
    start, end = WINDOW_LONG
    event_total = 0
    seed_count = 0

    # q=r=0 corresponds exactly to state_id = 25*piston_id in this encoding.
    for piston_id in range(PISTON_COUNT):
        seed = 25 * piston_id
        profiles, totals = orbit_profile(
            seed, start, end, theta_bits, transitions, piston_pre_cell, increments
        )
        update_oriented_summary(oriented_summary, profiles, totals)
        event_total += sum(totals)
        seed_count += 1

    require(seed_count == LONG_SEEDS, "Phase A LONG seed count")
    require(event_total == LONG_SEEDS * (end - start), "Phase A LONG total")
    return oriented_summary


def build_targets(class_representatives):
    numerators = [0] * CLASS_COUNT
    denominators = [0] * CLASS_COUNT
    occurrences = set()
    zero_classes = 0

    for cls, vector in enumerate(class_representatives):
        square_sum = sum(z * z for z in vector)
        coordinate_sum = sum(vector)
        m_times_five = 5 * square_sum - coordinate_sum * coordinate_sum
        if m_times_five == 0:
            zero_classes += 1
            require(cls == 0 and vector == (0, 0, 0, 0), "C2 m=0 locus")
            continue
        # (w_low/m) = S^2 / (4*(5*Q-S^2)); no division is used here.
        numerator = coordinate_sum * coordinate_sum
        denominator = 4 * m_times_five
        numerators[cls] = numerator
        denominators[cls] = denominator
        low = Fraction(numerator, denominator)
        occurrences.add((low, 1 - low))

    require(zero_classes == 1, "C2 unique ZERO class")
    require(len(occurrences) == 22, "C2 22 occurrence values")
    return numerators, denominators


def real_masks_from_summary(summary, numerators, denominators):
    alive = [SUBSET_FULL] * BLOCK_COUNT
    for cls in range(1, CLASS_COUNT):
        total = summary["total"][cls]
        if total == 0:
            continue
        packed = summary["reference"][cls]
        differences = summary["different"][cls]
        for block in range(BLOCK_COUNT):
            candidates = alive[block] & ~differences[block]
            if not candidates:
                alive[block] = 0
                continue
            mismatch = target_mismatch_bits(
                packed, total, block, numerators[cls], denominators[cls], candidates
            )
            alive[block] = candidates & ~mismatch
    return alive


def collapse_census(aggregate_profiles, aggregate_totals):
    class_profiles = [0] * CLASS_COUNT
    class_totals = [0] * CLASS_COUNT
    class_profiles[0] = aggregate_profiles[0]
    class_totals[0] = aggregate_totals[0]
    for cls in range(1, CLASS_COUNT):
        plus = 2 * cls - 1
        minus = 2 * cls
        class_profiles[cls] = aggregate_profiles[plus] + aggregate_profiles[minus]
        class_totals[cls] = aggregate_totals[plus] + aggregate_totals[minus]
    return class_profiles, class_totals


def census_real_masks(class_profiles, class_totals, numerators, denominators):
    alive = [SUBSET_FULL] * BLOCK_COUNT
    for cls in range(1, CLASS_COUNT):
        if not class_totals[cls]:
            continue
        for block in range(BLOCK_COUNT):
            if alive[block]:
                alive[block] &= ~target_mismatch_bits(
                    class_profiles[cls], class_totals[cls], block,
                    numerators[cls], denominators[cls], alive[block]
                )
    return alive


def information_masks(class_profiles, class_totals):
    info = [0] * BLOCK_COUNT
    visited = [cls for cls in range(1, CLASS_COUNT) if class_totals[cls]]
    if len(visited) < 2:
        return info
    reference_cls = visited[0]
    for cls in visited[1:]:
        for block in range(BLOCK_COUNT):
            candidates = SUBSET_FULL & ~info[block]
            if candidates:
                info[block] |= unequal_subset_bits(
                    class_profiles[cls], class_totals[cls],
                    class_profiles[reference_cls], class_totals[reference_cls],
                    block, candidates
                )
    return info


def seed_dependence_count(seed_summary):
    return sum(
        differences.bit_count()
        for cls in range(CLASS_COUNT)
        for differences in seed_summary["different"][cls]
    )


def orientation_dependence_count(aggregate_profiles, aggregate_totals):
    count = 0
    for cls in range(1, CLASS_COUNT):
        plus = 2 * cls - 1
        minus = 2 * cls
        if not aggregate_totals[plus] or not aggregate_totals[minus]:
            continue
        for block in range(BLOCK_COUNT):
            unequal = unequal_subset_bits(
                aggregate_profiles[plus], aggregate_totals[plus],
                aggregate_profiles[minus], aggregate_totals[minus],
                block, SUBSET_FULL
            )
            count += unequal.bit_count()
    return count


def pair_name(lambda_index, mask, delay_index):
    alpha, gamma = LAMBDAS[lambda_index]
    return "L%d_%d-M%02d-D%d" % (alpha, gamma, mask, DELAYS[delay_index])


def pairs_from_masks(masks):
    names = []
    # Frozen output enumeration: Lambda order, subset mask, then delay.
    for lambda_index in range(len(LAMBDAS)):
        for mask in range(1, 31):
            bit = 1 << (mask - 1)
            for delay_index in range(len(DELAYS)):
                block = delay_index * len(LAMBDAS) + lambda_index
                if masks[block] & bit:
                    names.append(pair_name(lambda_index, mask, delay_index))
    return names


def print_set(label, masks):
    names = pairs_from_masks(masks)
    print("%s count=%d" % (label, len(names)))
    print("%s pairs=%s" % (label, ",".join(names) if names else "EMPTY"))
    return names


def run():
    require(SINGLE_SEEDS * (WINDOW_SINGLE[1] - WINDOW_SINGLE[0]) == 24000000,
            "SINGLE event bound")
    require(LONG_SEEDS * (WINDOW_LONG[1] - WINDOW_LONG[0]) == 8960000,
            "LONG event bound")
    require(24000000 < (1 << LANE_BITS), "aggregate lane width")
    require((WINDOW_LONG[1] - WINDOW_LONG[0]) ** 2 < (1 << 29),
            "per-seed cross-product width")

    class_representatives, piston_class, piston_pre_cell = build_classes()
    selector_witness, direct_c_witness = audit_integrity(
        class_representatives, piston_class, piston_pre_cell
    )
    theta_bits, transitions = make_transitions()
    increments = make_fiber_increments()

    print("C1 PASS generators relations commutators")
    print("C2-STRUCTURE PASS zero=25 classes=313 oriented=625")
    print("C3 S1-S2 PASS exhaustive_states=15625 drive_bits=2")
    print("S3_SELECTOR %r" % (selector_witness,))
    print("S3_DIRECT_C %r" % (direct_c_witness,))
    print("CHANNEL-PASS")

    # Phase A is entirely target-free.
    single_summary, seed_summary, aggregate_profiles, aggregate_totals = phase_a_single(
        theta_bits, transitions, piston_pre_cell, increments
    )
    long_summary = phase_a_long(theta_bits, transitions, piston_pre_cell, increments)
    class_profiles, class_totals = collapse_census(aggregate_profiles, aggregate_totals)
    info_masks = information_masks(class_profiles, class_totals)
    seed_dependent = seed_dependence_count(seed_summary)
    orientation_dependent = orientation_dependence_count(aggregate_profiles, aggregate_totals)
    print("PHASE-A PASS target-free exact residue summaries")

    # Phase B constructs and consults the occurrence targets.
    numerators, denominators = build_targets(class_representatives)
    print("C2-TARGET PASS m-zero=25 occ-values=22")
    single_masks = real_masks_from_summary(single_summary, numerators, denominators)
    long_masks = real_masks_from_summary(long_summary, numerators, denominators)
    census_masks = census_real_masks(class_profiles, class_totals, numerators, denominators)

    single_names = print_set("REAL-SINGLE", single_masks)
    long_names = print_set("REAL-LONG", long_masks)
    census_names = print_set("REAL-CENSUS", census_masks)
    info_names = print_set("INFO", info_masks)

    print("REGISTER-REALIZED-W" if single_names else "NO-REALIZATION-W")
    print("LONG-REALIZED-W2" if long_names else "LONG-NO-REALIZATION-W2")
    print("CENSUS-REALIZED-W" if census_names else "CENSUS-NO-REALIZATION-W")
    print("RECORD-W info=%d" % len(info_names) if info_names else "NO-RECORD-W")
    print("SEED-DEPENDENT-%d" % seed_dependent)
    print("ORIENTATION-DEPENDENT-%d" % orientation_dependent)
    print("BREAKER-COMPLETE decisive-tags-and-C1-C3-only")
    return 0


def main():
    try:
        return run()
    except IntegrityStop as error:
        print("ARCH-STOP %s" % error)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
