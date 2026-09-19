#!/usr/bin/env python3
"""Independent exact finite breaker; known predictions, not blind discovery.

Written from PROOF.md and the frozen native-readback proof, without reading
the builder verifier or earlier note code. No external packages or data.
The clock sample audits an all-clock proof; it does not establish that proof.
"""

from collections import Counter, defaultdict, deque
from itertools import product


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def generator(letter, state):
    """Five involutions, evaluated directly in native coordinate order."""
    u, v, w, h, q, r = state
    if letter == 0:
        answer = v, u, h, w, q, r
    elif letter == 1:
        answer = -w, -h, -u, -v, -q, -r
    elif letter == 2:
        answer = 2 - w, 1 + r - h, 2 - u, 1 - r - v, 1 - q, -r
    elif letter == 3:
        answer = 2 - u, 1 - v, 3 - w, 4 - h, 1 - q, 1 - r
    elif letter == 4:
        answer = 2 - u, 1 - v, 3 - w, 4 - h, 2 - q, 1 - r
    else:
        raise AssertionError("generator index outside F5")
    return tuple(value % 5 for value in answer)


def trace(state):
    return sum(state) % 5


def driven(state, control):
    return generator((trace(state) + 2 * control) % 5, state)


def theta(clock):
    return clock.bit_count() % 2


def sign_pair(pair):
    positive = tuple(value % 5 for value in pair)
    negative = tuple((-value) % 5 for value in positive)
    return min(positive, negative)


def oriented_quotient(state):
    u, v, w, h, q, r = state
    phase = trace(state)
    total = u + v + w + h
    difference = u + v - w - h - 3
    if phase == 0:
        answer = total - 1, -difference - 2 * r
    elif phase in (1, 2):
        answer = total, difference
    else:
        answer = total, -difference
    return tuple(value % 5 for value in answer)


def quotient(state):
    return sign_pair(oriented_quotient(state))


def quotient_of_label(label):
    alpha, beta, gamma, delta, epsilon = label
    return sign_pair((alpha + beta, gamma + delta))


def alternating_halves(value):
    """Compute the integer closed sum, not the builder's recursion."""
    result = 0
    coefficient = 1
    while value:
        result += coefficient * value
        coefficient = -coefficient
        value //= 2
    return result


def direct_label(clock, state):
    require(clock >= 3, "chart used before synchronization")
    u, v, w, h, q, r = state
    parity = 1 if (clock - 3) % 2 == 0 else -1
    twist = 1 if (clock + theta(clock - 1)) % 2 == 0 else -1
    carry = alternating_halves((clock - 1) // 2) - 1
    values = (
        parity * (u + w),
        parity * (v + h),
        twist * (u - w - 2),
        twist * (v - h - 1),
        parity * r - carry,
    )
    return tuple(value % 5 for value in values)


def anchor_label(state):
    """Tick-three label, independently written without clock arithmetic."""
    u, v, w, h, q, r = state
    return ((u + w) % 5, (v + h) % 5, (u - w - 2) % 5,
            (v - h - 1) % 5, r)


def unwind_to_three(clock, state):
    """Undo the synchronized word using its actual generator involutions."""
    for tick in range(clock - 1, 2, -1):
        previous_phase = (4 - 3 * theta(tick - 1)) % 5
        letter = (previous_phase + 2 * theta(tick)) % 5
        state = generator(letter, state)
        require(trace(state) == previous_phase, "inverse word left its sheet")
    return state


def initial_head(phase, anchor):
    """Apply the five independently registered inverse words chronologically."""
    words = ((4, 2, 0), (3,), (4,), (3, 1, 3), (3, 1, 4))
    state = anchor
    for letter in words[phase]:
        state = generator(letter, state)
    return state


def main():
    states = tuple(product(range(5), repeat=6))
    neighbours = {state: [] for state in states}
    quotient_fibres = defaultdict(set)
    orientation_counts = Counter()
    phase_maps = {}
    for state in states:
        quotient_fibres[quotient(state)].add(state)
        orientation_counts[trace(state), oriented_quotient(state)] += 1
        for letter in range(5):
            require(generator(letter, generator(letter, state)) == state,
                    "native generator is not involutive")
        for control in (0, 1):
            successor = driven(state, control)
            neighbours[state].append(successor)
            neighbours[successor].append(state)
            require(quotient(successor) == quotient(state), "Q edge defect")
            key = trace(state), control
            if key in phase_maps:
                require(phase_maps[key] == trace(successor), "phase is not closed")
            phase_maps[key] = trace(successor)

    unseen = set(states)
    components = []
    while unseen:
        first = min(unseen)
        unseen.remove(first)
        component = {first}
        queue = deque([first])
        while queue:
            state = queue.popleft()
            for successor in neighbours[state]:
                if successor in unseen:
                    unseen.remove(successor)
                    component.add(successor)
                    queue.append(successor)
        require(component == quotient_fibres[quotient(first)],
                "weak component differs from its exact Q fibre")
        components.append(component)
    require(Counter(map(len, components)) == Counter({625: 1, 1250: 12}),
            "wrong weak component census")
    require(len(orientation_counts) == 125 and set(orientation_counts.values()) == {125},
            "oriented Q phase-fibre census differs")
    require(tuple(phase_maps[z, 0] for z in range(5)) == (0, 4, 0, 4, 4),
            "control-zero phase table differs")
    require(tuple(phase_maps[z, 1] for z in range(5)) == (2, 1, 1, 3, 1),
            "control-one phase table differs")

    anchors = {}
    heads_by_label = defaultdict(list)
    head_product = set()
    for head in states:
        state = head
        for control in (0, 1, 1):
            state = driven(state, control)
        require(trace(state) == 1, "three-step synchronization defect")
        label = anchor_label(state)
        if label in anchors:
            require(anchors[label] == state, "anchor chart collision")
        anchors[label] = state
        heads_by_label[label].append(head)
        pair = label, trace(head)
        require(pair not in head_product, "head Cartesian product collision")
        head_product.add(pair)
        require(quotient(head) == quotient_of_label(label), "initial Q factor defect")
        require(initial_head(trace(head), state) == head, "initial inverse word defect")
    all_labels = set(product(range(5), repeat=5))
    require(set(anchors) == all_labels, "retained chart is not onto F5^5")
    require(Counter(map(len, heads_by_label.values())) == Counter({5: 3125}),
            "E3 fibre census differs")
    require(all({trace(head) for head in heads} == set(range(5))
                for heads in heads_by_label.values()), "E3 fibre omits a phase")
    require(head_product == set(product(all_labels, range(5))),
            "head map is not the full Cartesian product")
    label_quotients = Counter(quotient_of_label(label) for label in all_labels)
    require(Counter(label_quotients.values()) == Counter({125: 1, 250: 12}),
            "Q projection label-fibre census differs")

    current = dict(anchors)
    audited_states = 0
    for clock in range(3, 16):
        require(len(set(current.values())) == 3125, "tail transition merged labels")
        for label, state in current.items():
            require(trace(state) == (4 - 3 * theta(clock - 1)) % 5,
                    "tail sheet formula differs")
            anchor = unwind_to_three(clock, state)
            require(anchor == anchors[label], "inverse word failed to recover E3")
            require(direct_label(clock, state) == anchor_label(anchor) == label,
                    "direct chart differs from inverse-word chart")
            require(quotient(state) == quotient_of_label(label), "tail Q factor defect")
            if clock == 3:
                require((trace(state) + 2 * theta(clock)) % 5 == 1,
                        "current selector reset defect")
            audited_states += 1
        if clock < 15:
            current = {label: driven(state, theta(clock))
                       for label, state in current.items()}

    first = (0, 0, 0, 0, 0)
    second = (0, 0, 0, 0, 1)
    require(first != second and quotient_of_label(first) == quotient_of_label(second),
            "strict-subclass witness failed")
    print("INDEPENDENT finite breaker; expected claims exposed; no blind discovery")
    print("native heads=15625; involutions=5; selected edges=31250")
    print("weak components=13; sizes=1x625,12x1250; exact Q fibres=PASS")
    print("E3 labels=3125; heads per label=5; initial phases per label=5")
    print("head Cartesian product=3125x5; inverse initial words=PASS")
    print("Q label fibres=1x125,12x250; retained-label refinement=STRICT")
    print("inverse-word chart clocks=3..15; state audits=" + str(audited_states))
    print("selector reset=PASS; all-clock and arbitrary-target claims require proof")
    print("BREAKERS=PASS")


if __name__ == "__main__":
    main()
