"""Exact occurrence audit for the frozen v80 closure-boundaries probe.

Import is inert. The coordinator calls audit() only after the public pin.
All assertions are integer or Fraction equalities; no random draws occur.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import factorial


SILENT, LOW, HIGH = 0, 1, 2
M_NATIVE = 1024
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def _scan(word, onset, length):
    """Literal inclusive consecutive scan, bounded by length complete cycles."""
    accepted = []
    for offset in range(length * len(word)):
        symbol = word[(onset + offset) % len(word)]
        if symbol != SILENT:
            accepted.append(symbol)
            if len(accepted) == length:
                break
    return tuple(accepted)


def _gap_partition(word):
    positions = tuple(i for i, symbol in enumerate(word) if symbol != SILENT)
    if not positions:
        return (), (), ()
    gaps = []
    owner = [None] * len(word)
    for i, endpoint in enumerate(positions):
        previous = positions[i - 1] if i else positions[-1] - len(word)
        residues = tuple(r % len(word) for r in range(previous + 1, endpoint + 1))
        assert residues
        for residue in residues:
            assert owner[residue] is None
            owner[residue] = i
        gaps.append(residues)
    assert all(i is not None for i in owner)
    return positions, tuple(gaps), tuple(owner)


def _generic_words():
    word_count = onset_count = nonempty_onsets = 0
    for size in range(1, 7):
        for word in product((SILENT, LOW, HIGH), repeat=size):
            word_count += 1
            positions, gaps, owner = _gap_partition(word)
            direct_laws = [defaultdict(Fraction) for _ in range(3)]
            predicted_laws = [defaultdict(Fraction) for _ in range(3)]
            denominator = size * (size + 1) // 2
            for onset in range(size):
                onset_count += 1
                actual = _scan(word, onset, 3)
                if not positions:
                    assert actual == ()
                    continue
                nonempty_onsets += 1
                index = owner[onset]
                predicted = tuple(
                    word[positions[(index + j) % len(positions)]] for j in range(3)
                )
                assert actual == predicted
                for k in range(1, 4):
                    direct_laws[k - 1][actual[:k]] += Fraction(onset + 1, denominator)
            if positions:
                assert sum(len(gap) for gap in gaps) == size
                for index, gap in enumerate(gaps):
                    mass = sum((Fraction(r + 1, denominator) for r in gap), Fraction())
                    predicted = tuple(
                        word[positions[(index + j) % len(positions)]] for j in range(3)
                    )
                    for k in range(1, 4):
                        predicted_laws[k - 1][predicted[:k]] += mass
                for direct, predicted in zip(direct_laws, predicted_laws):
                    assert direct == predicted
                    assert sum(direct.values(), Fraction()) == 1
    assert (word_count, onset_count, nonempty_onsets) == (1092, 6015, 5994)
    return word_count, onset_count


def _cartesian_word(source):
    """Forward enumeration of every occupied Cartesian fibre."""
    word = [SILENT] * M_NATIVE
    amplitude = abs(sum(source))
    for row in range(amplitude):
        for col in range(amplitude):
            address = 8 * row + col
            assert word[address] == SILENT
            word[address] = LOW
    for j, (i, k) in enumerate(PAIRS):
        amplitude = abs(source[i] - source[k])
        for copy in range(5):
            for row in range(amplitude):
                for col in range(amplitude):
                    address = 64 + 16 * (5 * j + copy) + 4 * row + col
                    assert word[address] == SILENT
                    word[address] = HIGH
    return tuple(word)


def _direct_symbol(source, address):
    """Independent inverse decoding of the fixed 1024-address carrier."""
    if address < 64:
        row, col = divmod(address, 8)
        return LOW if row < abs(sum(source)) and col < abs(sum(source)) else SILENT
    if address < 544:
        block, position = divmod(address - 64, 16)
        pair_index, copy = divmod(block, 5)
        assert 0 <= copy < 5
        row, col = divmod(position, 4)
        i, k = PAIRS[pair_index]
        amplitude = abs(source[i] - source[k])
        return HIGH if row < amplitude and col < amplitude else SILENT
    return SILENT


def _all_first_labels(word):
    """Reverse dynamic scan of two periods, with inclusive occupied onsets."""
    labels = [SILENT] * len(word)
    next_symbol = SILENT
    for absolute in range(2 * len(word) - 1, -1, -1):
        symbol = word[absolute % len(word)]
        if symbol != SILENT:
            next_symbol = symbol
        if absolute < len(word):
            labels[absolute] = next_symbol
    return tuple(labels)


def _first_label_formula(source):
    total = sum(source)
    differences = tuple(abs(source[i] - source[k]) for i, k in PAIRS)
    if not any(source):
        return (SILENT,) * M_NATIVE
    if total == 0:
        return (HIGH,) * M_NATIVE
    if not any(differences):
        return (LOW,) * M_NATIVE
    final_pair = max(j for j, difference in enumerate(differences) if difference)
    low_max = 9 * (abs(total) - 1)
    high_max = 123 + 80 * final_pair + 5 * differences[final_pair]
    return tuple(
        LOW if address <= low_max or address > high_max else HIGH
        for address in range(M_NATIVE)
    )


def _native_sources():
    source_count = slot_count = 0
    classes = defaultdict(list)
    records = {}
    for source in product(range(-2, 3), repeat=4):
        source_count += 1
        word = _cartesian_word(source)
        for address in range(M_NATIVE):
            assert word[address] == _direct_symbol(source, address)
            slot_count += 1
        total = sum(source)
        quadratic = sum(value * value for value in source)
        low = total * total
        high = 5 * (4 * quadratic - low)
        accepted_count = low + high
        assert word.count(LOW) == low
        assert word.count(HIGH) == high
        assert (accepted_count == 0) == (not any(source))
        accepted = tuple(symbol for symbol in word if symbol != SILENT)
        assert accepted == (LOW,) * low + (HIGH,) * high
        first = _all_first_labels(word)
        assert first == _first_label_formula(source)
        positions, gaps, owner = _gap_partition(word)
        if accepted_count:
            assert len(positions) == accepted_count
            for onset in range(M_NATIVE):
                assert first[onset] == word[positions[owner[onset]]]
            ratio = Fraction(low, accepted_count)
        else:
            assert first == (SILENT,) * M_NATIVE
            assert not positions and not gaps and not owner
            ratio = None
        if low and high:
            counts = Counter(
                (accepted[i], accepted[(i + 1) % accepted_count])
                for i in range(accepted_count)
            )
            assert counts[(LOW, LOW)] == low - 1
            assert counts[(LOW, HIGH)] == 1
            assert counts[(HIGH, LOW)] == 1
            assert counts[(HIGH, HIGH)] == high - 1
        classes[first].append((source, ratio))
        records[source] = (word, first, ratio)
    assert (source_count, slot_count) == (625, 640000)
    assert sum(len(members) for members in classes.values()) == source_count
    v, w, u = (1, 0, 1, 0), (2, -1, 1, 0), (1, 0, 0, 0)
    expected_first = tuple(
        LOW if address <= 9 or address >= 529 else HIGH for address in range(M_NATIVE)
    )
    assert records[v][1] == records[w][1] == expected_first
    assert records[v][2] == Fraction(1, 6)
    assert records[w][2] == Fraction(1, 26)
    assert (v, Fraction(1, 6)) in classes[expected_first]
    assert (w, Fraction(1, 26)) in classes[expected_first]
    assert records[u][2] == Fraction(1, 16)
    assert Fraction(records[u][1].count(LOW), M_NATIVE) == Fraction(23, 32)
    assert _scan(records[u][0], 0, 2) == (LOW, HIGH)
    assert all(_scan(records[u][0], onset, 2) != (LOW, LOW) for onset in range(M_NATIVE))
    return source_count, slot_count


def _permutation_scans():
    subset_count = permutation_cases = 0
    for size in range(1, 7):
        for mask in range(1, 1 << size):
            subset_count += 1
            selected = frozenset(i for i in range(size) if mask & (1 << i))
            cardinality = len(selected)
            first_counts = Counter()
            order_counts = Counter()
            for order in permutations(range(size)):
                accepted_order = tuple(address for address in order if address in selected)
                assert len(accepted_order) == cardinality
                first_counts[accepted_order[0]] += 1
                order_counts[accepted_order] += 1
                permutation_cases += 1
            assert set(first_counts) == selected
            assert sum(first_counts.values()) == factorial(size)
            assert all(count * cardinality == factorial(size) for count in first_counts.values())
            assert len(order_counts) == factorial(cardinality)
            assert all(
                count * factorial(cardinality) == factorial(size)
                for count in order_counts.values()
            )
            for length in range(1, cardinality + 1):
                prefix_counts = Counter()
                for order, multiplicity in order_counts.items():
                    prefix_counts[order[:length]] += multiplicity
                falling = factorial(cardinality) // factorial(cardinality - length)
                assert len(prefix_counts) == falling
                assert all(count * falling == factorial(size) for count in prefix_counts.values())
    assert subset_count == 120
    assert permutation_cases == 49489
    return subset_count, permutation_cases


def audit():
    """Run frozen exact audits and return compact deterministic output lines."""
    words, onsets = _generic_words()
    sources, slots = _native_sources()
    subsets, orders = _permutation_scans()
    return (
        f"ONSET GAP: ternary_words={words} inclusive_onsets={onsets} first_labels=3 PASS",
        f"ONSET INCIDENCE: sources={sources} slots={slots} first_label_classes=checked PASS",
        "ONSET NONSELECTION: common_first_map=1024/1024 target_v=1/6 target_w=1/26 PASS",
        "ONSET UNIFORM: first_LOW=23/32 accepted_LOW=1/16 periodic_LL=0 PASS",
        f"ONSET PERMUTATION: nonempty_subsets={subsets} permutation_cases={orders} PASS",
        "ONSET SCOPE: exact finite counts; conditional measures only; physical occurrence UNRESOLVED",
    )
