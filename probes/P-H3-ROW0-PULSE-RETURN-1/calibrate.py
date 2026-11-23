"""Regenerate the predecessor training banks from the exact H3 dynamics."""

from collections import defaultdict
from functools import cache

from physical import Physical, key, projected, roster


ZERO = (0, 0, 0, 0)
ORIGINAL_GAINS = tuple(range(2, 12))
MOTIF_GAINS = (12, 13, 20, 21, 14, 15, 24, 25)
LABELS = ("ABSTAIN", "NEG", "POS")


def training_label(case):
    arm, k, l, _, _ = key(case)
    if arm != "FULL":
        return "ABSTAIN"
    return "POS" if (l - k) % 5 in (1, 3) else "NEG"


def projected_training(simulation, gains):
    unique = set()
    for case in roster(gains):
        if case["arm"] != "SWAP":
            trace, _ = simulation.run(case)
            unique.add((training_label(case), projected(trace)))
    return unique


@cache
def rotations(word):
    result = [word]
    for _ in range(4):
        a, b, c, d = result[-1]
        result.append((d - c, -c, a - c, b - c))
    return tuple(result)


def motion_cycles(lane):
    for start, seed in enumerate(lane[:-4]):
        if seed != ZERO:
            a, b, c, d = seed
            if lane[start + 1] != (d - c, -c, a - c, b - c):
                continue
            orbit = rotations(seed)
            if lane[start:start + 5] == orbit:
                yield start, orbit.index(min(orbit))


def add_contexts(by_flank, by_neighbor, record, label, motif):
    for row, lane in enumerate(zip(*record, strict=True)):
        for start, phase in motion_cycles(lane):
            end = start + 5
            before = lane[max(0, start - 4):start][::-1]
            after = lane[end:end + 4]
            for side, samples in ((-1, before), (1, after)):
                flank = tuple(rotations(word)[phase] for word in samples)
                for length in range(1, len(flank) + 1):
                    by_flank[row, side, flank[:length]].add(label)
                if row == 1 and samples and lane[start:end] == motif:
                    by_neighbor[side, samples[0]].add(label)


def template_word_ids(traces, word_id):
    return [[word_id(word) for word in trace] for trace in sorted(traces)]


def context_key(item):
    row, side, flank = item
    return row, len(flank), -side, flank


def build_bank(kernel_path):
    simulation = Physical(kernel_path)
    # Opened design packet. Read row 1 at even ticks 118 through 126.
    marker = dict(arm="FULL", k=0, l=1, eta=-16, m=2)
    trace, _ = simulation.run(marker)
    motif = tuple(pair[1] for pair in projected(trace)[10:15])
    if len(motif) != 5 or motif[0] == ZERO or motif != rotations(motif[0]):
        raise ValueError("calibration marker did not generate its row-1 cycle")

    original = projected_training(simulation, ORIGINAL_GAINS)
    training = original | projected_training(simulation, MOTIF_GAINS)
    templates = {label: set() for label in LABELS}
    for label, record in original:
        templates[label].add(tuple(word for pair in record for word in pair))

    by_flank = defaultdict(set)
    by_neighbor = defaultdict(set)
    for label, record in training:
        add_contexts(by_flank, by_neighbor, record, label, motif)
    exclusive_neighbors = {
        side: sorted(word for (neighbor_side, word), labels in by_neighbor.items()
                     if side == neighbor_side and labels == {"POS"})
        for side in (-1, 1)
    }

    word_ids = {ZERO: 0}

    def word_id(word):
        return word_ids.setdefault(word, len(word_ids))

    bank = {
        "templates": {label: template_word_ids(traces, word_id)
                      for label, traces in templates.items()},
        "motif": [word_id(word) for word in motif],
        "before": [word_id(word) for word in exclusive_neighbors[-1]],
        "after": [word_id(word) for word in exclusive_neighbors[1]],
        "orbit": [],
    }
    for row, side, flank in sorted(by_flank, key=context_key):
        labels = by_flank[row, side, flank]
        if len(labels) == 1:
            bank["orbit"].append([row, side, [word_id(word) for word in flank], next(iter(labels))])
    bank["words"] = list(word_ids)
    rotations.cache_clear()
    return bank
