#!/usr/bin/env python3
"""Standalone exact finite audit; universal statements belong to PROOF.md.

No external inputs. Python >= 3.10 standard library only.
Scientific mismatches are listed as FALSIFIED with exit zero. An unexpected
exception is deliberately uncaught and is an integrity/runtime STOP.
"""

import json
from itertools import product


NAME = "P-SNAP-OCCURRENCE-IDENTITY-1"
COUNTS = {}
FAILURES = []
STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))


def check(condition, section, case):
    COUNTS[section] = COUNTS.get(section, 0) + 1
    if not condition:
        FAILURES.append((section, case))


def canonical(labels):
    names = {}
    result = []
    for label in labels:
        if label not in names:
            names[label] = len(names)
        result.append(names[label])
    return tuple(result)


def partitions(size):
    """Restricted-growth strings enumerate each equivalence relation once."""
    if size == 0:
        yield ()
        return

    def extend(prefix, maximum):
        if len(prefix) == size:
            yield prefix
            return
        for value in range(maximum + 2):
            yield from extend(prefix + (value,), max(maximum, value))

    yield from extend((0,), 0)


def bell(size):
    """Independent Stirling recurrence for the partition coverage count."""
    row = [1]
    for n in range(1, size + 1):
        previous = row
        row = [0] * (n + 1)
        for k in range(1, n + 1):
            row[k] = previous[k - 1] + (k * previous[k] if k < len(previous) else 0)
    return sum(row)


def orbit_kernel(mu, period, horizon):
    return tuple(t if t < mu else mu + (t - mu) % period for t in range(horizon + 1))


def forward_compatible(labels):
    horizon = len(labels) - 1
    return all(
        labels[i] != labels[j] or labels[i + 1] == labels[j + 1]
        for i in range(horizon) for j in range(i + 1, horizon)
    )


def predecessor_cancellation(labels):
    horizon = len(labels) - 1
    return all(
        labels[i + 1] != labels[j + 1] or labels[i] == labels[j]
        for i in range(horizon) for j in range(i + 1, horizon)
    )


def equivalence_audit():
    section = "FINITE_EQUIVALENCE"
    for n in range(9):
        distinct = tuple(range(n + 1))
        forward_models = {distinct}
        cancellative_models = {distinct}
        for mu in range(n):
            for period in range(1, n - mu + 1):
                model = orbit_kernel(mu, period, n)
                check(model not in forward_models, section, ("unique-model", n, mu, period))
                forward_models.add(model)
                if mu == 0:
                    cancellative_models.add(model)
        count_all = count_forward = count_backward = count_both = 0
        for relation in partitions(n + 1):
            count_all += 1
            forward = forward_compatible(relation)
            backward = predecessor_cancellation(relation)
            count_forward += int(forward)
            count_backward += int(backward)
            count_both += int(forward and backward)
            check(forward == (relation in forward_models), section, ("forward-classification", n, relation))
            check(
                backward == (canonical(relation[::-1]) in forward_models),
                section, ("reversed-classification", n, relation),
            )
            check(
                (forward and backward) == (relation in cancellative_models),
                section, ("both-classification", n, relation),
            )
        check(count_all == bell(n + 1), section, ("complete-partition-coverage", n))
        check(count_forward == 1 + n * (n + 1) // 2, section, ("forward-count", n))
        check(count_backward == count_forward, section, ("backward-count", n))
        check(count_both == n + 1, section, ("cancellative-count", n))


def autonomous_maps():
    section = "AUTONOMOUS_MAPS"
    map_count = start_count = 0
    for size in range(1, 6):
        horizon = 2 * size + 2
        for mapping in product(range(size), repeat=size):
            map_count += 1
            injective = len(set(mapping)) == size
            for start in range(size):
                start_count += 1
                sequence = [start]
                for _ in range(horizon):
                    sequence.append(mapping[sequence[-1]])
                first = {}
                for t, state in enumerate(sequence):
                    if state in first:
                        mu = first[state]
                        period = t - mu
                        break
                    first[state] = t
                else:
                    raise RuntimeError("finite map failed to repeat within the frozen horizon")
                check(mu + period <= size, section, ("first-repeat-bound", size, mapping, start))
                check(
                    canonical(sequence) == orbit_kernel(mu, period, horizon),
                    section, ("full-equality-kernel", size, mapping, start),
                )
                check(forward_compatible(sequence), section, ("forward-kernel", size, mapping, start))
                check(
                    predecessor_cancellation(sequence) == (mu == 0),
                    section, ("orbit-cancellation", size, mapping, start),
                )
                if injective:
                    check(mu == 0, section, ("injective-has-no-tail", size, mapping, start))
                # A second, direct comparison uses every pair of observed endpoints.
                for i in range(horizon + 1):
                    for j in range(i + 1, horizon + 1):
                        predicted = i >= mu and (j - i) % period == 0
                        check(
                            (sequence[i] == sequence[j]) == predicted,
                            section, ("endpoint-pair", size, mapping, start, i, j),
                        )
    check(map_count == sum(size ** size for size in range(1, 6)), section, "map-coverage")
    check(start_count == sum(size ** (size + 1) for size in range(1, 6)), section, "start-coverage")


def words(alphabet, maximum):
    return [word for length in range(maximum + 1) for word in product(alphabet, repeat=length)]


def log_key(kind, word):
    if kind == "EXACT":
        return word
    if kind == "LENGTH_MOD2":
        return len(word) % 2
    if kind == "LENGTH_MOD3":
        return len(word) % 3
    if kind == "PARIKH":
        return (word.count(0), word.count(1))
    if kind == "SET":
        return frozenset(word)
    raise ValueError(kind)


def log_controls():
    section = "LOG_EQUALITY"
    all_words = words((0, 1), 4)
    parents = words((0, 1), 3)
    appended = [(word, bit) for word in parents for bit in (0, 1)]
    # Columns: right congruence, recoverable last, joint predecessor+last,
    # empty separation, same-symbol right cancellation.
    expected = {
        "EXACT": (True, True, True, True, True),
        "LENGTH_MOD2": (True, False, False, False, True),
        "LENGTH_MOD3": (True, False, False, False, True),
        "PARIKH": (True, False, False, True, True),
        "SET": (True, False, False, True, False),
    }
    for kind, wanted in expected.items():
        right = last = joint = empty = same_symbol = True
        for u, v in product(parents, repeat=2):
            equal_parents = log_key(kind, u) == log_key(kind, v)
            for bit in (0, 1):
                equal_children = log_key(kind, u + (bit,)) == log_key(kind, v + (bit,))
                if equal_parents and not equal_children:
                    right = False
                if equal_children and not equal_parents:
                    same_symbol = False
        for (u, a), (v, b) in product(appended, repeat=2):
            if log_key(kind, u + (a,)) == log_key(kind, v + (b,)):
                last = last and a == b
                joint = joint and a == b and log_key(kind, u) == log_key(kind, v)
        for word in all_words[1:]:
            if log_key(kind, word) == log_key(kind, ()):
                empty = False
        actual = (right, last, joint, empty, same_symbol)
        for index, (obtained, required) in enumerate(zip(actual, wanted)):
            check(obtained == required, section, ("classified-control", kind, index))
    check(log_key("LENGTH_MOD2", ()) == log_key("LENGTH_MOD2", (0, 0)),
          section, "mod2-empty-repeat")
    check(log_key("LENGTH_MOD3", ()) == log_key("LENGTH_MOD3", (0, 0, 0)),
          section, "mod3-empty-repeat")
    for kind in ("LENGTH_MOD2", "LENGTH_MOD3"):
        check(log_key(kind, (0,)) == log_key(kind, (1,)), section, ("last-symbol-loss", kind))
    for kind in ("PARIKH", "SET"):
        check(log_key(kind, (0, 1)) == log_key(kind, (1, 0)), section, ("ordered-last-loss", kind))
    check(log_key("SET", (0,)) == log_key("SET", (0, 0))
          and log_key("SET", ()) != log_key("SET", (0,)), section, "set-predecessor-loss")

    section = "SILENT_ERASURE"
    raw = words((0, 1, None), 4)
    erase = lambda word: tuple(symbol for symbol in word if symbol is not None)
    for word in raw:
        accepted = erase(word)
        check(len(accepted) <= len(word), section, ("event-budget", word))
        check(len(accepted) == sum(symbol in (0, 1) for symbol in word),
              section, ("accepted-count", word))
        if len(word) < 4:
            check(erase(word + (None,)) == accepted, section, ("silent-no-append", word))
            for bit in (0, 1):
                check(erase(word + (bit,)) == accepted + (bit,),
                      section, ("accepted-append", word, bit))
    for u, v in product(raw, repeat=2):
        if len(u) + len(v) <= 4:
            check(erase(u + v) == erase(u) + erase(v), section, ("erasure-homomorphism", u, v))
    check(erase((None,)) == () and (None,) != (), section, "raw-tick-versus-accepted-empty")
    check(erase((0, None, 0)) == (0, 0), section, "repeated-payload-retained-twice")


def norm(point):
    x, y = point
    return max(abs(x), abs(y), abs(x - y))


def hex_balls(maximum):
    reached = {(0, 0)}
    result = [set(reached)]
    for _ in range(maximum):
        extended = set(reached)
        for x, y in reached:
            for dx, dy in STEPS:
                extended.add((x + dx, y + dy))
        reached = extended
        result.append(set(reached))
    return result


def rank_tag(tag):
    r, x, y = tag
    if r < 0 or norm((x, y)) > r:
        raise ValueError("rank outside the tagged-ball domain")
    earlier_rows = sum(2 * r + 1 - abs(u) for u in range(-r, x))
    return r ** 3 + earlier_rows + y - max(-r, x - r)


def unrank_tick(tick):
    if tick < 0:
        raise ValueError("negative tick")
    r = 0
    while (r + 1) ** 3 <= tick:
        r += 1
    offset = tick - r ** 3
    for x in range(-r, r + 1):
        lower = max(-r, x - r)
        upper = min(r, x + r)
        width = upper - lower + 1
        if offset < width:
            return (r, x, lower + offset)
        offset -= width
    raise RuntimeError("valid clock address not covered by a complete layer")


def geometry_and_emission():
    section = "TAGGED_GEOMETRY"
    balls = hex_balls(20)
    tags = []
    seen_tags = set()
    previous = 0
    for r, ball in enumerate(balls):
        independent = {
            (x, y) for x in range(-r, r + 1) for y in range(-r, r + 1)
            if norm((x, y)) <= r
        }
        check(ball == independent, section, ("BFS-versus-norm", r))
        check(len(ball) == 3 * r * (r + 1) + 1, section, ("ball-cardinality", r))
        check(len(tags) == r ** 3, section, ("layer-start", r))
        for x, y in sorted(ball):
            tag = (r, x, y)
            tick = len(tags)
            check(tag not in seen_tags, section, ("fresh-tag", tick))
            check(rank_tag(tag) == tick, section, ("lex-rank", tick, tag))
            check(unrank_tick(tick) == tag, section, ("unrank-versus-BFS-order", tick))
            check(rank_tag(unrank_tick(tick)) == tick, section, ("inverse-tick", tick))
            check(r ** 3 <= tick < (r + 1) ** 3, section, ("layer-clock-interval", tick))
            check(r <= tick, section, ("not-before-layer-index", tick))
            tags.append(tag)
            seen_tags.add(tag)
            check(len(seen_tags) == tick + 1, section, ("every-tick-prefix", tick))
        check(len(tags) == (r + 1) ** 3, section, ("completed-layer", r))
        check(len(tags) - previous == len(ball), section, ("one-layer-increment", r))
        previous = len(tags)
        if r:
            check(len(tags) > r + 1, section, ("same-clock-radius-obstruction", r))
    check(len(tags) == 9261, section, "complete-frozen-tag-domain")

    section = "BOUNDED_EMISSION"
    for radius in range(21):
        records = tags[:(radius + 1) ** 3]
        for budget in range(1, 6):
            batches = [records[start:start + budget] for start in range(0, len(records), budget)]
            ticks = len(batches)
            check(all(0 < len(batch) <= budget for batch in batches),
                  section, ("per-tick-budget", radius, budget))
            flattened = [record for batch in batches for record in batch]
            check(flattened == records, section, ("no-loss-or-reordering", radius, budget))
            check(len(set(flattened)) == len(records), section, ("no-duplicate-record", radius, budget))
            check(ticks == (len(records) + budget - 1) // budget,
                  section, ("minimal-ceiling", radius, budget))
            check((ticks - 1) * budget < len(records) <= ticks * budget,
                  section, ("preceding-tick-obstruction", radius, budget))
            for clock, batch in enumerate(batches):
                for slot, record in enumerate(batch):
                    index = clock * budget + slot
                    check(records[index] == record, section, ("batch-slot-address", radius, budget, index))
                    check((clock, slot) == divmod(rank_tag(record), budget),
                          section, ("rank-to-batch-slot", radius, budget, index))
            if budget > 1 and len(records) > 1:
                check(len(batches[0]) > 1, section, ("multiple-events-one-tick", radius, budget))
    check(unrank_tick(0) != unrank_tick(1) and 0 // 2 == 1 // 2,
          section, "distinct-tags-share-batched-tick")


def main():
    equivalence_audit()
    autonomous_maps()
    log_controls()
    geometry_and_emission()
    report = {
        "name": NAME,
        "result": "FALSIFIED" if FAILURES else "PROOF_AUDIT_PASS",
        "counts": COUNTS,
        "total": sum(COUNTS.values()),
        "failures": [{"section": section, "case": case} for section, case in FAILURES],
        "scope": "L1 finite exact audit; occurrence equality and emission resources are explicit",
    }
    print(json.dumps(report, ensure_ascii=True, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
