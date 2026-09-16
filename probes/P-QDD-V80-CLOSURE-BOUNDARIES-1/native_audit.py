"""Exact native common-ready audit; execute only after the public joint pin."""

from itertools import product


GOOD_READY = (0, 1)
BAD_READIES = {(0, 0), (3, 0), (3, 3), (1, 3)}
PHASE_MAPS = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
# Generator indices in the temporal order of H_z.
THREE_WORDS = ((0, 2, 4), (3,), (4,), (3, 1, 3), (4, 1, 3))


def theta(n):
    return n.bit_count() & 1


def generator(index, state):
    p1, p4, p1p, p4p, q, r = state
    if index == 0:
        result = (p4, p1, p4p, p1p, q, r)
    elif index == 1:
        result = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif index == 2:
        result = (-p1p + 2, -p4p + 1 + r, -p1 + 2,
                  -p4 + 1 - r, 1 - q, -r)
    elif index == 3:
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    elif index == 4:
        result = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    else:
        raise ValueError("invalid generator")
    return tuple(value % 5 for value in result)


def step(n, state):
    return generator((sum(state) + 2 * theta(n)) % 5, state)


def switch_sum(m):
    total, sign = 0, 1
    while m:
        total += sign * m
        sign = -sign
        m //= 2
    return total


def labels(n, state):
    if n < 3:
        raise ValueError("chart starts at tick three")
    p1, p4, p1p, p4p, _, r = state
    t = 1 if (n - 3) % 2 == 0 else -1
    h = 1 if (n + theta(n - 1)) % 2 == 0 else -1
    shift = switch_sum((n - 1) // 2) - 1
    return tuple(value % 5 for value in
                 (t * (p1 + p1p), t * (p4 + p4p),
                  h * (p1 - p1p - 2), h * (p4 - p4p - 1), t * r - shift))


def tick_three_from_labels(label):
    alpha, beta, gamma, delta, epsilon = label
    return tuple(value % 5 for value in
                 (3 * (alpha + 2 + gamma), 3 * (beta + 1 + delta),
                  3 * (alpha - 2 - gamma), 3 * (beta - 1 - delta),
                  1 - alpha - beta - epsilon, epsilon))


def ready_table(ready):
    q, r = ready
    rows = ((q + 1, r + 1), (1 - q, 1 - r), (2 - q, 1 - r),
            (2 - q, 2 - r), (3 - q, 2 - r))
    return tuple(tuple(value % 5 for value in row) for row in rows)


def initial_word(z, n):
    word = []
    for tick in range(n):
        bit = theta(tick)
        word.append((z + 2 * bit) % 5)
        z = PHASE_MAPS[bit][z]
    return word


def undo_word(state, word):
    for index in reversed(word):
        state = generator(index, state)
    return state


def decode(n, state, ready=GOOD_READY):
    if n < 0 or ready in BAD_READIES:
        raise ValueError("decoder requires nonnegative time and a good ready")
    if n < 3:
        candidates = []
        for z in range(5):
            candidate = undo_word(state, initial_word(z, n))
            if candidate[4:] == ready and sum(candidate) % 5 == z:
                candidates.append(candidate)
        if len(candidates) != 1:
            raise AssertionError("early reader lacks one candidate")
        return candidates[0]
    third = tick_three_from_labels(labels(n, state))
    table = ready_table(ready)
    matches = [z for z in range(5) if table[z] == third[4:]]
    if len(matches) != 1:
        raise AssertionError("late reader lacks one phase")
    z = matches[0]
    candidate = undo_word(third, THREE_WORDS[z])
    if candidate[4:] != ready or sum(candidate) % 5 != z:
        raise AssertionError("late source reconstruction fails its domain")
    return candidate


def audit():
    """Return compact exact coverage lines; mismatches raise AssertionError."""
    sources = tuple(product(range(5), repeat=4))
    checks = 0

    def require(condition, reason):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(reason)

    good_count = bad_count = double_fibres = 0
    for ready in product(range(5), repeat=2):
        table = ready_table(ready)
        require((len(set(table)) == 5) == (ready not in BAD_READIES),
                "ready table criterion")
        fibres = {}
        for source in sources:
            head = source + ready
            current = head
            for tick in range(3):
                current = step(tick, current)
            require(sum(current) % 5 == 1, "tick-three synchronization")
            require(current[4:] == table[sum(head) % 5], "independent A3 table")
            fibres.setdefault(current, []).append(source)
        histogram = {}
        for members in fibres.values():
            histogram[len(members)] = histogram.get(len(members), 0) + 1
        if ready in BAD_READIES:
            bad_count += 1
            require(len(fibres) == 500, "exceptional image size")
            require(histogram == {1: 375, 2: 125}, "exceptional fibres")
            for members in fibres.values():
                if len(members) == 2:
                    left, right = members
                    require(left != right and
                            left != tuple((-value) % 5 for value in right),
                            "exceptional full-QDD sign distinction")
                    double_fibres += 1
        else:
            good_count += 1
            require(len(fibres) == 625, "good image size")
            require(histogram == {1: 625}, "good fibres")
            for current, members in fibres.items():
                require(decode(3, current, ready) == members[0] + ready,
                        "all-good-ready decoder at tick three")

    readbacks = chart_steps = zero_readbacks = 0
    for source in sources:
        head = source + GOOD_READY
        current = head
        first_label = None
        for n in range(65):
            recovered = decode(n, current)
            require(recovered == head, "selected-ready all-source readback")
            require((recovered[:4] == (0, 0, 0, 0)) ==
                    (source == (0, 0, 0, 0)), "zero support retention")
            readbacks += 1
            if source == (0, 0, 0, 0):
                zero_readbacks += 1
            if n >= 3:
                current_label = labels(n, current)
                if n == 3:
                    first_label = current_label
                require(current_label == first_label, "conserved chart label")
                require(sum(current) % 5 == (4 - 3 * theta(n - 1)) % 5,
                        "reachable sheet")
                chart_steps += 1
            current = step(n, current)
    require(good_count == 21 and bad_count == 4, "complete ready census")
    require(double_fibres == 500, "complete conflicting-pair count")
    require(readbacks == 40625 and chart_steps == 38750 and zero_readbacks == 65,
            "exact audit coverage")
    return (
        f"NATIVE common_readies={good_count} exceptional_readies={bad_count}",
        "NATIVE good_image=625 exceptional_image=500 double=125 singleton=375",
        f"NATIVE exceptional_qdd_conflicting_pairs={double_fibres}",
        "NATIVE selected_ready=0,1 sources=625 supported=624",
        f"NATIVE times=0..64 source_readbacks={readbacks} zero_readbacks={zero_readbacks}",
        f"NATIVE times=3..64 conserved_chart_comparisons={chart_steps}",
        f"NATIVE checks={checks} source_retention=EXACT archive=REGENERABLE",
    )
