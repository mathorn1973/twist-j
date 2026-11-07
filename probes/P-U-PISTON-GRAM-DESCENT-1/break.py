#!/usr/bin/env python3
"""Independent exact breaker for P-U-PISTON-GRAM-DESCENT-1.

Status before execution: independently authored, not a scientific result.
PUBLIC / L1; this source creates no Canon authority.

Scientific source read by this author:
  mathorn1973/twist-j, commit
  25a9034379fccb29d1408d505fa5dfd6319b6e6d,
  probes/P-U-PISTON-GRAM-DESCENT-1/PREREG.md,
  12715 UTF-8 bytes, SHA256
  9c6cc1cbbfcd50779f52dcdf1e77b4d6cc8b068b69996ff19807cf6ab7d47a1a.

The author did not read verify.py, PROOF.md, predecessor executable
sources, builder results, or another agent's scientific source. This
program was not imported or executed before its public source freeze.

All generators below are independently transcribed affine matrices over
F5. Completeness uses backward reachability on unordered pairs inside
original reading fibres, rather than successive partition splitting.
The only arithmetic is integer arithmetic. No external input is read.
"""

from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, product
import json
import sys


PROBE = "P-U-PISTON-GRAM-DESCENT-1"
FIELD_ORDER = 5
DIMENSION = 6
STATE_COUNT = FIELD_ORDER ** DIMENSION
BALANCED = (0, 1, 2, -2, -1)
CONTROLS = (0, 1)

# A row has six linear coefficients followed by its affine constant.
# Coordinate order: p1, p4, p1p, p4p, q, r.
AFFINE_GENERATORS = (
    (  # a
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
    ),
    (  # b
        (0, 0, -1, 0, 0, 0, 0),
        (0, 0, 0, -1, 0, 0, 0),
        (-1, 0, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0, -1, 0),
    ),
    (  # c
        (0, 0, -1, 0, 0, 0, 2),
        (0, 0, 0, -1, 0, 1, 1),
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, -1, 1),
        (0, 0, 0, 0, -1, 0, 1),
        (0, 0, 0, 0, 0, -1, 0),
    ),
    (  # d
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, 0, 1),
        (0, 0, -1, 0, 0, 0, 3),
        (0, 0, 0, -1, 0, 0, 4),
        (0, 0, 0, 0, -1, 0, 1),
        (0, 0, 0, 0, 0, -1, 1),
    ),
    (  # e
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, 0, 1),
        (0, 0, -1, 0, 0, 0, 3),
        (0, 0, 0, -1, 0, 0, 4),
        (0, 0, 0, 0, -1, 0, 2),
        (0, 0, 0, 0, 0, -1, 1),
    ),
)


# Entries: control, present trace, generator index, next trace,
# signs on the first and third spatial components of the declared Q.
DECLARED_SHEET_TABLE = (
    (0, 1, 1, 4, -1),
    (0, 4, 4, 4, 1),
    (1, 1, 3, 1, 1),
    (1, 4, 1, 1, -1),
)


def require(condition, message):
    """Preserve every failed check even when Python assertions are disabled."""
    if not condition:
        raise AssertionError(message)


def checkpoint_index(checkpoint):
    """Ordinary six-digit base-five index, first coordinate most significant."""
    require(len(checkpoint) == DIMENSION, "checkpoint dimension")
    value = 0
    for digit in checkpoint:
        require(0 <= digit < FIELD_ORDER, "checkpoint coordinate")
        value = FIELD_ORDER * value + digit
    return value


def affine_image(generator, checkpoint):
    homogeneous = checkpoint + (1,)
    return tuple(
        sum(coefficient * coordinate
            for coefficient, coordinate in zip(row, homogeneous)) % FIELD_ORDER
        for row in AFFINE_GENERATORS[generator]
    )


def selector(checkpoint, control):
    require(control in CONTROLS, "control domain")
    return (sum(checkpoint) + 2 * control) % FIELD_ORDER


def gram_and_det(lifted):
    """Real row Gram and signed determinant of the declared 2x2 reshape."""
    require(len(lifted) == 4, "piston dimension")
    rows = (lifted[:2], lifted[2:])
    gram = tuple(
        sum(left * right for left, right in zip(rows[i], rows[j]))
        for i, j in ((0, 0), (0, 1), (1, 1))
    )
    determinant = rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]
    return gram + (determinant,)


def check_gram_identity(invariants, message):
    aa, bb, cc, dd = invariants
    require(aa * cc - bb * bb == dd * dd, message)


def centered_lift(checkpoint, centre):
    # Subtraction occurs in F5 BEFORE the balanced integer lift.
    return tuple(BALANCED[(checkpoint[i] - centre[i]) % FIELD_ORDER]
                 for i in range(4))


def cone(invariants):
    aa, bb, cc, dd = invariants
    return (aa + cc, aa - cc, 2 * bb, 2 * dd)


def flat_frame(trace, vector):
    require(trace in (1, 4), "flat-frame trace domain")
    sign = 1 if trace == 1 else -1
    return (vector[0], sign * vector[1], vector[2], sign * vector[3])


def histogram(values):
    return [[value, count] for value, count in sorted(Counter(values).items())]


class Components:
    """Union-find with the least checkpoint as the canonical root."""

    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size

    def find(self, element):
        while self.parent[element] != element:
            self.parent[element] = self.parent[self.parent[element]]
            element = self.parent[element]
        return element

    def join(self, left, right):
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return
        if left_root > right_root:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        self.count -= 1


def assemble_native_maps(states):
    require(len(AFFINE_GENERATORS) == 5, "generator count")
    for matrix in AFFINE_GENERATORS:
        require(len(matrix) == DIMENSION, "affine matrix height")
        require(all(len(row) == DIMENSION + 1 for row in matrix),
                "affine matrix width")
    for index, checkpoint in enumerate(states):
        require(checkpoint_index(checkpoint) == index, "lexicographic indexing")

    generator_maps = tuple(
        tuple(checkpoint_index(affine_image(generator, checkpoint))
              for checkpoint in states)
        for generator in range(len(AFFINE_GENERATORS))
    )
    involution_checks = 0
    for generator_map in generator_maps:
        for index, image in enumerate(generator_map):
            require(generator_map[image] == index, "generator involution")
            involution_checks += 1
    require(involution_checks == 78125, "involution audit coverage")

    transitions = tuple(
        tuple(generator_maps[selector(checkpoint, control)][index]
              for index, checkpoint in enumerate(states))
        for control in CONTROLS
    )
    require(all(len(table) == STATE_COUNT for table in transitions),
            "native transition coverage")
    return generator_maps, transitions, involution_checks


def audit_pistons():
    invariants = {}
    piston_identity_count = 0
    for piston in product(range(FIELD_ORDER), repeat=4):
        lifted = tuple(BALANCED[value] for value in piston)
        record = gram_and_det(lifted)
        check_gram_identity(record, "raw signed determinant/Gram identity")
        invariants[piston] = record
        piston_identity_count += 1
    require(piston_identity_count == 625, "raw piston identity coverage")
    return invariants, piston_identity_count


def audit_witness(states, transitions, piston_invariants):
    left = (1, 0, 0, 4, 0, 4)
    right = (4, 0, 0, 1, 0, 4)
    initial_left = piston_invariants[left[:4]]
    initial_right = piston_invariants[right[:4]]
    require(left[4:] + initial_left[:3] == (0, 4, 1, 0, 1),
            "left initial Gram reading")
    require(right[4:] + initial_right[:3] == (0, 4, 1, 0, 1),
            "right initial Gram reading")
    require(initial_left == initial_right == (1, 0, 1, -1),
            "oriented initial witness equality")

    counter = 0
    control = counter.bit_count() % 2
    require(control == 0, "actual witness counter bit")
    require(selector(left, control) == selector(right, control) == 4,
            "native witness selects e")
    next_left = states[transitions[control][checkpoint_index(left)]]
    next_right = states[transitions[control][checkpoint_index(right)]]
    require(next_left == (1, 1, 3, 0, 2, 2), "native left successor")
    require(next_right == (3, 1, 3, 3, 2, 2), "native right successor")
    left_after = piston_invariants[next_left[:4]]
    right_after = piston_invariants[next_right[:4]]
    require(left_after == (2, -2, 4, 2), "left successor signed invariants")
    require(right_after == (5, 2, 8, 6), "right successor signed invariants")
    require(next_left[4:] + left_after[:3] != next_right[4:] + right_after[:3],
            "raw native obstruction")
    require(next_left[4:] + left_after != next_right[4:] + right_after,
            "oriented native obstruction")
    return {
        "left": left,
        "right": right,
        "initial_H": initial_left[:3],
        "initial_D": initial_left[3],
        "next_left": next_left,
        "next_right": next_right,
        "next_left_H": left_after[:3],
        "next_right_H": right_after[:3],
        "next_left_D": left_after[3],
        "next_right_D": right_after[3],
    }


def pair_classification(states, transitions, readings):
    """Find the largest common congruence by backward pair reachability.

    For a pair initially in one reading fibre, depth d is the shortest
    positive length of a binary word whose final readings differ. Pairs
    already in different initial fibres have depth zero and need not be
    enumerated. One-step edges to those pairs seed depth one. Breadth-first
    propagation through reverse edges finds exactly every finite depth.

    Surviving pairs agree under every finite control word. This relation is
    an equivalence relation, refines the initial reading, and is closed
    under both successors. Conversely, every congruence refining the
    initial reading agrees along every word, and therefore cannot contain
    a distinguished pair. Thus survivors give exactly the coarsest common
    congruence, with no singleton assumption.

    P_k is equality under words of length at most k. Within each original
    fibre it retains precisely pairs with depth greater than k, or with no
    finite depth. Descending depth and adding pair edges reconstructs the
    numbers of its equivalence classes; it does not perform the builder's
    successive signature splitting.
    """
    grouped = {}
    for index, reading in enumerate(readings):
        grouped.setdefault(reading, []).append(index)
    fibres = sorted(grouped.values(), key=lambda fibre: fibre[0])
    initial_of = [None] * len(states)
    for fibre in fibres:
        for index in fibre:
            initial_of[index] = fibre[0]
    require(all(value is not None for value in initial_of),
            "initial fibre coverage")

    # Encode an unordered non-diagonal pair by left * N + right, left < right.
    pair_left = []
    pair_right = []
    pair_number = {}
    for fibre in fibres:
        for left, right in combinations(fibre, 2):
            key = left * STATE_COUNT + right
            require(key not in pair_number, "duplicate initial pair")
            pair_number[key] = len(pair_left)
            pair_left.append(left)
            pair_right.append(right)
    require(len(pair_left) == sum(len(fibre) * (len(fibre) - 1) // 2
                                   for fibre in fibres),
            "all initial-fibre pairs enumerated")

    def same_fibre_pair_number(left, right):
        require(left != right, "diagonal pair lookup")
        require(initial_of[left] == initial_of[right],
                "initial-fibre pair lookup")
        if left > right:
            left, right = right, left
        return pair_number[left * STATE_COUNT + right]

    backwards = [[] for _ in pair_left]
    depths = [-1] * len(pair_left)
    queue = deque()
    split_fibres = [set(), set()]
    for pair_id, (left, right) in enumerate(zip(pair_left, pair_right)):
        for control in CONTROLS:
            after_left = transitions[control][left]
            after_right = transitions[control][right]
            if after_left == after_right:
                continue
            if initial_of[after_left] != initial_of[after_right]:
                split_fibres[control].add(initial_of[left])
                if depths[pair_id] < 0:
                    depths[pair_id] = 1
                    queue.append(pair_id)
            else:
                successor_pair = same_fibre_pair_number(after_left, after_right)
                backwards[successor_pair].append(pair_id)

    while queue:
        distinguished = queue.popleft()
        predecessor_depth = depths[distinguished] + 1
        for predecessor in backwards[distinguished]:
            if depths[predecessor] < 0:
                depths[predecessor] = predecessor_depth
                queue.append(predecessor)

    # Exact shortest-word recurrence, including closure of surviving pairs.
    for pair_id, (left, right) in enumerate(zip(pair_left, pair_right)):
        candidates = []
        for control in CONTROLS:
            after_left = transitions[control][left]
            after_right = transitions[control][right]
            if after_left == after_right:
                continue
            if initial_of[after_left] != initial_of[after_right]:
                candidates.append(1)
            else:
                successor_depth = depths[same_fibre_pair_number(
                    after_left, after_right)]
                if successor_depth >= 1:
                    candidates.append(successor_depth + 1)
        expected_depth = min(candidates) if candidates else -1
        require(depths[pair_id] == expected_depth,
                "shortest distinguishing-word recurrence")

    first_split_controls = [len(split_fibres[control]) for control in CONTROLS]
    for control in CONTROLS:
        direct_count = sum(
            len({initial_of[transitions[control][index]] for index in fibre}) > 1
            for fibre in fibres
        )
        require(first_split_controls[control] == direct_count,
                "first split fibre count")

    components = Components(len(states))
    finite_by_depth = {}
    for pair_id, (left, right) in enumerate(zip(pair_left, pair_right)):
        depth = depths[pair_id]
        if depth < 0:
            components.join(left, right)
        else:
            require(depth >= 1, "positive distinguishing-word depth")
            finite_by_depth.setdefault(depth, []).append(pair_id)

    representatives = tuple(components.find(index) for index in range(len(states)))
    stable_sizes = Counter(representatives)
    stable_keys = sorted(stable_sizes)
    require(len(stable_keys) == components.count, "stable component count")
    for index, representative in enumerate(representatives):
        require(representative <= index, "canonical least representative")
        require(representatives[representative] == representative,
                "representative is a member")
        require(initial_of[representative] == initial_of[index],
                "stable partition refines the original reading")

    # This tests transitivity rather than assuming that connected pairs
    # constitute an equivalence relation: any distinguished pair joined
    # through surviving links would fail the reverse implication below.
    for pair_id, (left, right) in enumerate(zip(pair_left, pair_right)):
        require((representatives[left] == representatives[right])
                == (depths[pair_id] < 0),
                "surviving-pair equivalence and transitivity")

    max_depth = max(finite_by_depth, default=0)
    class_counts = [0] * (max_depth + 1)
    class_counts[max_depth] = components.count
    for depth in range(max_depth, 0, -1):
        for pair_id in finite_by_depth.get(depth, ()):
            components.join(pair_left[pair_id], pair_right[pair_id])
        class_counts[depth - 1] = components.count
    require(class_counts[0] == len(fibres), "P0 class count from pair depths")
    require(class_counts[-1] == len(stable_keys), "terminal class count")
    require(all(left < right for left, right in zip(class_counts, class_counts[1:])),
            "strict refinements and first stable termination")
    for index in range(len(states)):
        require(components.find(index) == initial_of[index],
                "pair-depth reconstruction of the full initial fibres")

    # Every extra-label reader must distinguish the terminal blocks inside
    # each original fibre. Increasing least-member ranks give a label
    # alphabet of maximum fibre multiplicity and attain that lower bound.
    fibre_blocks = []
    tag_for_representative = {}
    for fibre in fibres:
        blocks = sorted({representatives[index] for index in fibre})
        fibre_blocks.append(blocks)
        for tag, representative in enumerate(blocks):
            require(representative not in tag_for_representative,
                    "one original fibre for each stable block")
            tag_for_representative[representative] = tag
    multiplicities = [len(blocks) for blocks in fibre_blocks]
    capacity = max(multiplicities)
    chosen_fibre_index = next(index for index, multiplicity in enumerate(multiplicities)
                             if multiplicity == capacity)
    chosen_fibre = fibres[chosen_fibre_index]
    chosen_blocks = fibre_blocks[chosen_fibre_index]

    tagged_readings = tuple(
        (readings[index], tag_for_representative[representatives[index]])
        for index in range(len(states))
    )
    require(len(set(tagged_readings)) == len(stable_keys),
            "sharp tags distinguish exactly the terminal blocks")
    require(all(0 <= tag_for_representative[representative] < capacity
                for representative in stable_keys),
            "attained extra-label alphabet size")
    transition_checks = 0
    for control in CONTROLS:
        induced = {}
        for index, tagged_reading in enumerate(tagged_readings):
            after = transitions[control][index]
            after_representative = representatives[after]
            reference_after = representatives[transitions[control][representatives[index]]]
            require(after_representative == reference_after,
                    "both terminal quotient transitions")
            after_reading = tagged_readings[after]
            if tagged_reading in induced:
                require(induced[tagged_reading] == after_reading,
                        "tagged successor is independent of checkpoint representative")
            else:
                induced[tagged_reading] = after_reading
            transition_checks += 1
        require(len(induced) == len(stable_keys), "total induced tagged map")
    require(transition_checks == 31250, "tagged transition coverage")

    partition_bytes = (",".join(str(value) for value in representatives) + "\n").encode("ascii")
    transition_bytes = "".join(
        ",".join(str(value) for value in (
            representative,
            representatives[transitions[0][representative]],
            representatives[transitions[1][representative]],
        )) + "\n"
        for representative in stable_keys
    ).encode("ascii")
    descends = not any(first_split_controls)
    return {
        "initial_classes": len(fibres),
        "initial_size_histogram": histogram(len(fibre) for fibre in fibres),
        "refinement_class_counts": class_counts,
        "stable_classes": len(stable_keys),
        "stable_size_histogram": histogram(stable_sizes.values()),
        "first_split_controls": first_split_controls,
        "required_extra_labels": capacity,
        "ambiguity_histogram": histogram(multiplicities),
        "tagged_transition_checks": transition_checks,
        "partition_sha256": sha256(partition_bytes).hexdigest(),
        "transition_sha256": sha256(transition_bytes).hexdigest(),
        "maximal_fibre_witness": {
            "reading": readings[chosen_fibre[0]],
            "representatives": [states[representative] for representative in chosen_blocks],
        },
        "descent": "YES" if descends else "NO",
        "positive_hypothesis": "SURVIVES" if descends else "FIRED",
    }


def audit_stable_sheet(states, generator_maps, transitions):
    # Enumerate the fixed-piston equation of d; no uniqueness is assumed.
    fixed_by_d = []
    common_fixed = []
    for piston in product(range(FIELD_ORDER), repeat=4):
        checkpoint = piston + (0, 0)
        fixed = tuple(affine_image(generator, checkpoint)[:4] == piston
                      for generator in (1, 3, 4))
        if fixed[1]:
            fixed_by_d.append(piston)
        if all(fixed):
            common_fixed.append(piston)
    require(fixed_by_d == [(1, 3, 4, 2)], "unique d-fixed piston")
    require(common_fixed == fixed_by_d, "common b,d,e fixed piston")
    centre = fixed_by_d[0]
    for qr in product(range(FIELD_ORDER), repeat=2):
        checkpoint = centre + qr
        for generator in (1, 3, 4):
            require(affine_image(generator, checkpoint)[:4] == centre,
                    "fixed piston independent of q,r")

    lifted = tuple(centered_lift(checkpoint, centre) for checkpoint in states)
    invariants = tuple(gram_and_det(value) for value in lifted)
    centered_identity_checks = 0
    for record in invariants:
        check_gram_identity(record, "centered signed determinant/Gram identity")
        centered_identity_checks += 1
    require(centered_identity_checks == STATE_COUNT, "centered identity coverage")

    declared_actions = {(entry[0], entry[1]): entry for entry in DECLARED_SHEET_TABLE}
    observed_actions = set()
    image_records = set()
    count = 0
    step_checks = 0
    cone_identity_checks = 0
    cone_zero_states = 0
    flat_invariant_checks = 0
    for index, checkpoint in enumerate(states):
        trace = sum(checkpoint) % FIELD_ORDER
        if trace not in (1, 4):
            continue
        count += 1
        vector = cone(invariants[index])
        require(vector[0] * vector[0] - sum(value * value for value in vector[1:]) == 0,
                "integer null-cone identity")
        cone_identity_checks += 1
        image_records.add((trace,) + vector)
        if vector == (0, 0, 0, 0):
            cone_zero_states += 1
        aa, bb, cc, dd = invariants[index]
        for control in CONTROLS:
            generator = selector(checkpoint, control)
            after = transitions[control][index]
            require(after == generator_maps[generator][index],
                    "stable-sheet native selected generator")
            next_trace = sum(states[after]) % FIELD_ORDER
            require(generator in (1, 3, 4), "stable-sheet generator domain")
            sign = -1 if generator == 1 else 1
            action = (control, trace, generator, next_trace, sign)
            require(action == declared_actions[(control, trace)],
                    "declared native stable-sheet action")
            observed_actions.add(action)
            if generator == 1:
                expected_lift = tuple(-value for value in lifted[index][2:] + lifted[index][:2])
                expected_invariants = (cc, bb, aa, -dd)
            else:
                expected_lift = tuple(-value for value in lifted[index])
                expected_invariants = invariants[index]
            require(lifted[after] == expected_lift, "exact lifted centered matrix action")
            require(invariants[after] == expected_invariants,
                    "centered Gram and signed determinant action")
            next_vector = cone(invariants[after])
            require(next_vector == (vector[0], sign * vector[1], vector[2], sign * vector[3]),
                    "specified null-cone action")
            require(flat_frame(trace, vector) == flat_frame(next_trace, next_vector),
                    "flat invariant under both controls")
            flat_invariant_checks += 1
            step_checks += 1
    require(count == 6250, "stable-sheet domain coverage")
    require(step_checks == 12500, "stable-sheet step coverage")
    require(cone_identity_checks == count, "null-cone coverage")
    require(flat_invariant_checks == step_checks, "flat-invariant coverage")
    require(sorted(observed_actions) == list(DECLARED_SHEET_TABLE),
            "complete stable-sheet action table")

    # The full native counter is an unbounded Python integer. Each head
    # starts at literal n=0, then evaluates popcount(n) at each actual n.
    origin_heads_verified = 0
    origin_final_traces = set()
    for initial_index in range(len(states)):
        counter = 0
        current = initial_index
        observed_controls = []
        for unused_step in range(3):
            control = counter.bit_count() % 2
            observed_controls.append(control)
            current = transitions[control][current]
            counter += 1
        require(counter == 3 and observed_controls == [0, 1, 1],
                "actual native origin counter head")
        final_trace = sum(states[current]) % FIELD_ORDER
        require(final_trace == 1, "inherited origin entrance trace")
        origin_final_traces.add(final_trace)
        origin_heads_verified += 1
    require(origin_heads_verified == STATE_COUNT, "origin head coverage")
    require(origin_final_traces == {1}, "uniform origin final trace")
    return {
        "count": count,
        "step_checks": step_checks,
        "centre": centre,
        "origin_heads_verified": origin_heads_verified,
        "origin_final_trace": next(iter(origin_final_traces)),
        "cone_identity_checks": cone_identity_checks,
        "flat_invariant_checks": flat_invariant_checks,
        "cone_images": len(image_records),
        "cone_zero_states": cone_zero_states,
        "action_table": sorted(observed_actions),
    }


def main():
    states = tuple(product(range(FIELD_ORDER), repeat=DIMENSION))
    require(len(states) == STATE_COUNT == 15625, "entire checkpoint domain")
    generator_maps, transitions, involution_checks = assemble_native_maps(states)
    piston_invariants, piston_identity_count = audit_pistons()
    witness = audit_witness(states, transitions, piston_invariants)

    readers = {}
    for name, invariant_count in (("GRAM", 3), ("ORIENTED", 4)):
        readings = tuple(checkpoint[4:] + piston_invariants[checkpoint[:4]][:invariant_count]
                         for checkpoint in states)
        readers[name] = pair_classification(states, transitions, readings)
        require(readers[name]["descent"] == "NO"
                and readers[name]["positive_hypothesis"] == "FIRED",
                "native exposed witness agrees with complete descent decision")

    stable_sheet = audit_stable_sheet(states, generator_maps, transitions)
    result = {
        "probe": PROBE,
        "state_count": len(states),
        "controls": CONTROLS,
        "piston_identity_count": piston_identity_count,
        "generator_involution_checks": involution_checks,
        "status": "COMPLETE",
        "witness": witness,
        "readers": readers,
        "stable_sheet": stable_sheet,
    }
    sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
