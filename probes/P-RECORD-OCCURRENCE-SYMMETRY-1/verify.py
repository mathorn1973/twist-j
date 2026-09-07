"""Exact finite audits of the pinned, all-domain occurrence proofs."""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm, prod


CHECKS = Counter()


def require(section, condition):
    if not condition:
        raise AssertionError(section)
    CHECKS[section] += 1


def act(p, state):
    return tuple(p[x] for x in state)


def ready_orbits(states, group):
    remaining = set(states)
    result = []
    while remaining:
        representative = min(remaining)
        orbit = {act(p, representative) for p in group}
        remaining.difference_update(orbit)
        result.append((representative, orbit))
    return result


def symmetry_audit():
    section = "symmetry"
    for d in range(1, 5):
        full = list(permutations(range(d)))
        cyclic = [tuple((x + h) % d for x in range(d)) for h in range(d)]
        for group in (full, cyclic):
            for k in range(4):
                states = list(product(range(d), repeat=k))
                orbits = ready_orbits(states, group)
                fixed_sets = []
                for representative, orbit in orbits:
                    stabilizer = [p for p in group if act(p, representative) == representative]
                    fixed = [y for y in range(d) if all(p[y] == y for p in stabilizer)]
                    fixed_sets.append(fixed)
                    require(section, len(orbit) * len(stabilizer) == len(group))
                    for y in range(d):
                        images = {}
                        for p in group:
                            images.setdefault(act(p, representative), set()).add(p[y])
                        well_defined = all(len(values) == 1 for values in images.values())
                        require(section, well_defined == (y in fixed))
                    if k:
                        # First-coordinate selector, with one invariant ready orbit at a time.
                        outputs = Counter(state[0] for state in orbit)
                        require(section, all(outputs[y] * d == len(orbit) for y in range(d)))
                predicted = prod(len(fixed) for fixed in fixed_sets)
                if d <= 3 and k <= 2 and group == full:
                    indices = {state: i for i, state in enumerate(states)}
                    generators = []
                    for j in range(d - 1):
                        p = list(range(d))
                        p[j], p[j + 1] = p[j + 1], p[j]
                        generators.append(tuple(p))
                    actual = 0
                    for outputs in product(range(d), repeat=len(states)):
                        if all(outputs[indices[act(p, state)]] == p[outputs[i]]
                               for p in generators for i, state in enumerate(states)):
                            actual += 1
                    require(section, actual == predicted)
                if k == 0:
                    require(section, predicted == (1 if d == 1 else 0))
                else:
                    total = sum(range(1, len(orbits) + 1))
                    mass = {state: Fraction(i + 1, total * len(orbit))
                            for i, (_, orbit) in enumerate(orbits) for state in orbit}
                    require(section, sum(mass.values()) == 1)
                    require(section, all(sum(mass[s] for s in states if s[0] == y)
                                         == Fraction(1, d) for y in range(d)))
                for state in states:
                    reverse = state[::-1]
                    stabilizer = {p for p in group if act(p, state) == state}
                    reverse_stabilizer = {p for p in group if act(p, reverse) == reverse}
                    require(section, stabilizer == reverse_stabilizer)
                    if k == 2:
                        collapsed = (state[0], state[0])
                        later = {p for p in group if act(p, collapsed) == collapsed}
                        require(section, stabilizer <= later)
                        require(section, all(act(p, collapsed) == (p[state[0]], p[state[0]])
                                             for p in group))
    require(section, ready_orbits([], [(0,)]) == [])
    require(section, prod([]) == 1)


def cycles_of(update):
    remaining = set(range(len(update)))
    cycles = []
    while remaining:
        start = min(remaining)
        cycle = []
        x = start
        while x in remaining:
            remaining.remove(x)
            cycle.append(x)
            x = update[x]
        if x != start:
            raise AssertionError("input is not a permutation")
        cycles.append(cycle)
    return cycles


def tick_word(update, labels, start, horizon):
    result = []
    x = start
    for _ in range(horizon):
        result.append(labels[x])
        x = update[x]
    return result


def cycle_audit():
    section = "cycles"
    for n in range(1, 6):
        for update in permutations(range(n)):
            cycles = cycles_of(update)
            period = lcm(*(len(cycle) for cycle in cycles))
            for labels in product((-1, 0, 1), repeat=n):
                profiles = [(len(c), sum(labels[x] == 0 for x in c),
                             sum(labels[x] == 1 for x in c)) for c in cycles]
                total_low = labels.count(0)
                total_active = n - labels.count(-1)
                criterion = total_active > 0 and all(
                    low + high > 0 and low * total_active == total_low * (low + high)
                    for _, low, high in profiles)
                observed_all = total_active > 0
                for cycle, (length, low, high) in zip(cycles, profiles):
                    active = low + high
                    for start in cycle:
                        period_word = tick_word(update, labels, start, period)
                        accepted = [y for y in period_word if y != -1]
                        require(section, period_word.count(0) * length == period * low)
                        require(section, period_word.count(1) * length == period * high)
                        if not accepted:
                            observed_all = False
                            require(section, active == 0)
                        else:
                            observed_all &= accepted.count(0) * total_active == total_low * len(accepted)
                            require(section, accepted.count(0) * active == len(accepted) * low)
                            prefix = tick_word(update, labels, start, 3 * length)
                            accepted_prefix = [y for y in prefix if y != -1]
                            for horizon in (1, active, 2 * active + 1):
                                count = accepted_prefix[:horizon].count(0)
                                require(section, len(accepted_prefix) >= horizon)
                                require(section, abs(active * count - horizon * low) < active * active)
                        for horizon in (0, n, 2 * n + 1):
                            word = tick_word(update, labels, start, horizon)
                            require(section, abs(length * word.count(0) - horizon * low) < length * length)
                            require(section, abs(length * word.count(1) - horizon * high) < length * length)
                require(section, bool(observed_all) == criterion)
                # Two explicitly normalized stationary ensembles; silent cycles retained.
                for weights in ([len(c) for c in cycles], list(range(1, len(cycles) + 1))):
                    norm = sum(weights)
                    mass = {x: Fraction(w, norm * len(c)) for w, c in zip(weights, cycles) for x in c}
                    require(section, sum(mass.values()) == 1)
                    require(section, all(mass[update[x]] == mass[x] for x in range(n)))
                    num = sum((mass[x] for x in range(n) if labels[x] == 0), Fraction(0))
                    den = sum((mass[x] for x in range(n) if labels[x] != -1), Fraction(0))
                    formula_num = sum(Fraction(w * low, norm * length)
                                      for w, (length, low, _) in zip(weights, profiles))
                    formula_den = sum(Fraction(w * (low + high), norm * length)
                                      for w, (length, low, high) in zip(weights, profiles))
                    require(section, (num, den) == (formula_num, formula_den))
                    if den:
                        require(section, num / den == formula_num / formula_den)
                        if weights == [len(c) for c in cycles]:
                            require(section, num / den == Fraction(total_low, total_active))
                # Converse stationary-mixture construction, on all active cycles.
                active_profiles = [(i, length, low, low + high)
                                   for i, (length, low, high) in enumerate(profiles) if low + high]
                if active_profiles:
                    beta_norm = sum(i + 1 for i, _, _, _ in active_profiles)
                    raw_gamma = [Fraction((i + 1) * length, beta_norm * active)
                                 for i, length, _, active in active_profiles]
                    gamma_norm = sum(raw_gamma)
                    gamma = [value / gamma_norm for value in raw_gamma]
                    num = sum(g * Fraction(low, length)
                              for g, (_, length, low, _) in zip(gamma, active_profiles))
                    den = sum(g * Fraction(active, length)
                              for g, (_, length, _, active) in zip(gamma, active_profiles))
                    target = sum(Fraction((i + 1) * low, beta_norm * active)
                                 for i, _, low, active in active_profiles)
                    require(section, num / den == target)


def cyclic_blocks(word, k):
    return Counter(tuple(word[(start + j) % len(word)] for j in range(k))
                   for start in range(len(word)))


def countermodel_audit():
    section = "countermodels"
    for d in range(2, 7):
        update = tuple(range(d))
        for p in permutations(range(d)):
            require(section, all(update[p[x]] == p[update[x]] for x in range(d)))
        words = [tick_word(update, tuple(range(d)), x, 3) for x in range(d)]
        require(section, all(word == [x, x, x] for x, word in enumerate(words)))
        require(section, Fraction(sum(word[0] == word[1] for word in words), d) == 1)
        require(section, Fraction(1, d) != 1)
    word = (0, 0, 1, 1)
    require(section, cyclic_blocks(word, 1) == Counter({(0,): 2, (1,): 2}))
    require(section, cyclic_blocks(word, 2) == Counter(product((0, 1), repeat=2)))
    require(section, cyclic_blocks(word, 3)[(0, 0, 0)] == 0)
    require(section, Fraction(1, 2) ** 3 == Fraction(1, 8))
    require(section, 16 ** 20 == 2 ** 80)


def de_bruijn(b, k):
    """Euler circuit in the word graph; no randomness or target probabilities."""
    start = (0,) * (k - 1)
    used = {}
    stack = [(start, None)]
    reversed_letters = []
    while stack:
        vertex, incoming = stack[-1]
        digit = used.get(vertex, 0)
        if digit < b:
            used[vertex] = digit + 1
            following = (vertex + (digit,))[1:]
            stack.append((following, digit))
        else:
            stack.pop()
            if incoming is not None:
                reversed_letters.append(incoming)
    return tuple(reversed(reversed_letters))


def capacity_audit():
    section = "capacity"
    # Exhaust every map from N seeds to all binary k-words in this small range.
    for n in range(1, 5):
        for k in range(1, 3):
            outcomes = list(product((0, 1), repeat=k))
            for assignment in product(range(len(outcomes)), repeat=n):
                counts = Counter(assignment)
                full_support = len(counts) == 2 ** k
                require(section, not full_support or n >= 2 ** k)
                for b in range(2, 5):
                    for a in range(1, b):
                        if gcd(a, b) != 1:
                            continue
                        exact_iid = all(counts[i] * b ** k == n * a ** w.count(0) * (b - a) ** w.count(1)
                                        for i, w in enumerate(outcomes))
                        require(section, not exact_iid or n % (b ** k) == 0)
                        require(section, not exact_iid or full_support)
    # Independently audit reduction of the all-LOW fraction, including non-binary bases.
    for b in range(2, 13):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            for k in range(1, 7):
                require(section, Fraction(a ** k, b ** k).denominator == b ** k)
                for n in range(1, 65):
                    require(section, ((n * a ** k) % (b ** k) == 0) == (n % (b ** k) == 0))
    for b in range(2, 6):
        for k in range(1, 5):
            word = de_bruijn(b, k)
            size = b ** k
            require(section, len(word) == size)
            require(section, cyclic_blocks(word, k) == Counter(product(range(b), repeat=k)))
            update = tuple((x + 1) % size for x in range(size))
            require(section, len(cycles_of(update)) == 1)
            require(section, all((update[x] - 1) % size == x for x in range(size)))
            for a in range(1, b):
                if gcd(a, b) != 1:
                    continue
                coarse = tuple(0 if letter < a else 1 for letter in word)
                require(section, coarse.count(0) * b == a * size)
                for horizon in range(1, k + 1):
                    counts = cyclic_blocks(coarse, horizon)
                    for w in product((0, 1), repeat=horizon):
                        require(section, counts[w] * b ** horizon
                                == size * a ** w.count(0) * (b - a) ** w.count(1))
                longer = cyclic_blocks(coarse, k + 1)
                require(section, longer[(0,) * (k + 1)] * b ** (k + 1) != size * a ** (k + 1))


def main():
    symmetry_audit()
    cycle_audit()
    countermodel_audit()
    capacity_audit()
    print("P-RECORD-OCCURRENCE-SYMMETRY-1")
    for section in ("symmetry", "cycles", "countermodels", "capacity"):
        print(f"PASS {section}: {CHECKS[section]} exact checks")
    print("WITNESS uniform stationary identity: every path is constant")
    print("WITNESS 0011: fair pairs; P(000)=0 != 1/8")
    print("BOUND uniform ready p=1/16, k=20: N divisible by 2^80")
    print(f"PASS total: {sum(CHECKS.values())} exact checks")


if __name__ == "__main__":
    main()
