"""Frozen anonymous two-row H3 reader and the row-0 pulse-return rule."""

import json
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calibrate import build_bank

LABELS = ("POS", "NEG", "ABSTAIN")
ZERO = (0, 0, 0, 0)
WORD_BYTES = 2
SLOTS = 160
SLOT_ONE = int.from_bytes(b"\x01\x00" * SLOTS, "little")
SLOT_GUARD = int.from_bytes(b"\x00\x80" * SLOTS, "little")
PULSE = "000111110001"


def signed_words(record):
    if type(record) is not list or len(record) != 80:
        raise ValueError("expected 80 even ticks from 98 through 256")
    rows = [[], []]
    for tick in record:
        if type(tick) is not list or len(tick) != 2:
            raise ValueError("expected exactly two rows at each tick")
        for row, word in zip(rows, tick, strict=True):
            if type(word) is not list or len(word) != 4 or any(type(n) is not int for n in word):
                raise ValueError("expected a four-integer word")
            if gcd(*word) not in (0, 1):
                raise ValueError("expected signed primitive words")
            row.append(tuple(word))
    return tuple(rows[0]), tuple(rows[1])


def pack_words(word_ids):
    data = b"".join(word_id.to_bytes(WORD_BYTES, "little") for word_id in word_ids)
    return int.from_bytes(data, "little")


def activity_mask(word_ids):
    return sum(1 << (index * 16 + 15) for index, word_id in enumerate(word_ids) if word_id)


def template_score(observed, observed_activity, reference, reference_activity):
    different = observed ^ reference
    # The high bit guards each 16-bit lane against borrowing from its neighbor.
    # Subtracting one per lane clears the guard precisely when the lane was zero.
    equal_lanes = SLOT_GUARD & ~((different | SLOT_GUARD) - SLOT_ONE)
    matches = (equal_lanes & observed_activity & reference_activity).bit_count()
    activity_distance = (observed_activity ^ reference_activity).bit_count()
    direction_distance = (observed_activity | reference_activity).bit_count() - 3 * matches
    return activity_distance, direction_distance


def original_call(observed, activity, templates, exact_control):
    if exact_control:
        return "ABSTAIN"
    best_activity = {}
    best_direction = {}
    for label in LABELS:
        distances = [
            template_score(observed, activity, reference, reference_activity)
            for reference, reference_activity in templates[label]
        ]
        best_activity[label] = min(distance[0] for distance in distances)
        best_direction[label] = min(distance[1] for distance in distances)

    margin = 2 * (best_activity["NEG"] - best_activity["POS"])
    margin += best_direction["NEG"] - best_direction["POS"]
    if margin == 0:
        return "ABSTAIN"
    sign = "POS" if margin > 0 else "NEG"
    control_distance = best_direction["ABSTAIN"]
    if control_distance <= best_direction[sign] - 2:
        return "ABSTAIN"
    if (best_activity["ABSTAIN"] <= min(best_activity["POS"], best_activity["NEG"])
            and control_distance <= best_direction[sign]):
        return "ABSTAIN"
    return sign


def six_word_call(row, motif, before, after):
    for start in range(len(row) - len(motif) + 1):
        stop = start + len(motif)
        if row[start:stop] == motif:
            if start and row[start - 1] in before:
                return "POS"
            if stop < len(row) and row[stop] in after:
                return "POS"
    return "ABSTAIN"


def rotate(word):
    a, b, c, d = word
    return d - c, -c, a - c, b - c


def rotations(word):
    orbit = [word]
    for _ in range(4):
        orbit.append(rotate(orbit[-1]))
    return tuple(orbit)


def flank_votes(rows, contexts):
    for row, lane in enumerate(rows):
        for start, seed in enumerate(lane[:len(lane) - 4]):
            if seed == ZERO:
                continue
            orbit = rotations(seed)
            stop = start + 5
            if lane[start:stop] != orbit:
                continue
            power = orbit.index(min(orbit))
            side_samples = ((-1, lane[max(0, start - 4):start][::-1]),
                            (1, lane[stop:stop + 4]))
            for side, samples in side_samples:
                words = []
                for sample in samples:
                    words.append(rotations(sample)[power])
                    flank = tuple(words)
                    label = contexts.get((row, side, flank))
                    if label is not None:
                        yield label, (row, start, side, flank)


def support(start, side, length):
    if side == -1:
        return start - length, start + 4
    return start, start + 4 + length


def independent(first, second):
    row_1, start_1, side_1, words_1 = first
    row_2, start_2, side_2, words_2 = second
    if row_1 == row_2:
        low_1, high_1 = support(start_1, side_1, len(words_1))
        low_2, high_2 = support(start_2, side_2, len(words_2))
        if low_1 <= high_2 and low_2 <= high_1:
            return False
    common = min(len(words_1), len(words_2))
    return side_1 != side_2 or words_1[:common] != words_2[:common]


def orbit_call(rows, contexts):
    votes = list(flank_votes(rows, contexts))
    labels = {label for label, _ in votes}
    if labels not in ({"POS"}, {"NEG"}):
        return "ABSTAIN"
    incidences = [
        (incidence, min(rotations(incidence[3][0])))
        for _, incidence in votes
        if incidence[3][0] != ZERO
    ]
    for index, (first, first_orbit) in enumerate(incidences):
        for second, second_orbit in incidences[index + 1:]:
            if first_orbit != second_orbit and independent(first, second):
                return next(iter(labels))
    return "ABSTAIN"


def load_reader(kernel_path):
    spec = build_bank(kernel_path)
    words = tuple(tuple(word) for word in spec["words"])
    word_index = {word: index for index, word in enumerate(words)}
    templates = {
        label: [(pack_words(ids), activity_mask(ids)) for ids in spec["templates"][label]]
        for label in LABELS
    }
    controls = {packed for packed, _ in templates["ABSTAIN"]}
    contexts = {
        (row, side, tuple(words[index] for index in ids)): label
        for row, side, ids, label in spec["orbit"]
    }
    motif = tuple(words[index] for index in spec["motif"])
    before = {words[index] for index in spec["before"]}
    after = {words[index] for index in spec["after"]}
    unknown_word = len(words)

    def read(record):
        rows = signed_words(record)
        word_ids = [word_index.get(word, unknown_word) for pair in zip(*rows, strict=True) for word in pair]
        observed = pack_words(word_ids)
        exact_control = observed in controls
        original = original_call(observed, activity_mask(word_ids), templates, exact_control)
        six = original
        if six == "ABSTAIN" and not exact_control:
            six = six_word_call(rows[1], motif, before, after)
        orbit = six
        if orbit == "ABSTAIN" and not exact_control:
            orbit = orbit_call(rows, contexts)
        onset = next((98 + 2 * index for index, word in enumerate(rows[1]) if word != ZERO), None)
        baseline = "POS" if orbit == "NEG" and onset == 118 else orbit
        match = "".join("0" if word == ZERO else "1" for word in rows[0][:12]) == PULSE
        selected = "POS" if baseline == "ABSTAIN" and not exact_control and match else baseline
        return {"original": original, "six": six, "orbit": orbit, "row1_onset": onset,
                "baseline": baseline, "exact_control": exact_control,
                "match": match, "selected": selected}

    return read


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def main(argv):
    if len(argv) == 2 and argv[0] == "one":
        sys.stdout.buffer.write(canonical(load_reader(Path(argv[1]))(json.load(sys.stdin))))
    elif len(argv) == 4 and argv[0] == "batch":
        records = json.loads(Path(argv[2]).read_bytes())
        if type(records) is not list:
            raise ValueError("anonymous batch must be a list of records")
        read = load_reader(Path(argv[1]))
        cache = {}
        results = []
        for record in records:
            key = canonical(record)
            if key not in cache:
                cache[key] = read(record)
            results.append(cache[key])
        with Path(argv[3]).open("xb") as stream:
            stream.write(canonical(results))
    else:
        raise SystemExit("usage: reader.py one KERNEL | reader.py batch KERNEL ANON OUT")


if __name__ == "__main__":
    main(sys.argv[1:])
