#!/usr/bin/env python3
"""Independent executable audit for P-INTEGER-PRIMITIVE-SOURCE-METRIC-1.

The breaker author read PREREG.md and the public Canon, but did not read or
import this probe's primary verify.py or PROOF.md. The author participated
in specification discussion and saw a teammate's analytical report; this
is independence of implementation code, not independence of all context.

Hermitian gates below are direct formulas on eight integer coordinates.
K1 and its rational reference use explicit, separately written full matrices.
The canonical initial slices are literal data checked against the word bits.
No other probe implementation is imported, opened, or executed.
"""

from fractions import Fraction
import hashlib
import math
from pathlib import Path
import sys


PROBE_ID = "P-INTEGER-PRIMITIVE-SOURCE-METRIC-1"
M = 324
M2 = 104976
DIPOLE = (1, -1, 0, 0, 0)
SOURCE_CYCLE = (1, 2, 2, 1, 0, 0)
ZERO_H = (0, 0, 0, 0, 0, 0, 0, 0)
D_H = (0, 0, 1, 0, 0, 0, 0, 0)
Z_H = (1, 0, 1, 0, 0, 1, 0, 0)

# A full matrix, not the author's circulant indexing algorithm.
C_MATRIX = (
    (460, 29, 65, 65, 29),
    (29, 460, 29, 65, 65),
    (65, 29, 460, 29, 65),
    (65, 65, 29, 460, 29),
    (29, 65, 65, 29, 460),
)
L_NUMERATOR = (
    (188, -29, -65, -65, -29),
    (-29, 188, -29, -65, -65),
    (-65, -29, 188, -29, -65),
    (-65, -65, -29, 188, -29),
    (-29, -65, -65, -29, 188),
)

# Rows are (word, initial numerator P_0, initial numerator P_1).
# The repeated slices for distinct words are intentionally retained.
INITIAL_SLICES = (
    ("0010", (0, 1, 1, 0, 0), (1, 1, 0, 0, 0)),
    ("0011", (0, 1, 1, 0, 0), (0, 1, 1, 0, 0)),
    ("0100", (1, 1, 0, 0, 0), (1, 0, 0, 0, 1)),
    ("0101", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0)),
    ("0110", (0, 1, 1, 0, 0), (1, 0, 0, 0, 1)),
    ("1001", (1, 0, 0, 0, 1), (0, 1, 1, 0, 0)),
    ("1010", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0)),
    ("1011", (1, 1, 0, 0, 0), (0, 1, 1, 0, 0)),
    ("1100", (1, 0, 0, 0, 1), (1, 0, 0, 0, 1)),
    ("1101", (1, 0, 0, 0, 1), (1, 1, 0, 0, 0)),
)
EXPECTED_WORD_ORDER = (
    "0010", "0011", "0100", "0101", "0110",
    "1001", "1010", "1011", "1100", "1101",
)

# These bytes were independently read and hashed before authoring this file.
AUTHORITY = (
    ("CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)

FALSIFIER_KEYS = frozenset((
    "AUTHORITY", "RING", "TRANSPORT", "COST", "BARE_INVERSE",
    "FUNDED_INVERSE", "CONSERVATION", "BRANCH", "IMAGE_GUARD",
    "INITIAL_DATA", "SOURCE_PATTERN", "DENOMINATOR", "MEAN",
    "RECURRENCE", "LORENTZ", "RESPONSE_BOUND", "ACTION", "PREFIX",
    "SHARP_BUDGET", "DETECTOR", "FIXED_COUNTER", "CONTROL", "PERIOD",
    "CERTIFICATE", "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    """Only an observed violation of a preregistered scientific check."""

    def __init__(self, key):
        if key not in FALSIFIER_KEYS:
            raise ValueError("unregistered falsifier key")
        self.key = key
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def integer_tuple(value, length):
    return (isinstance(value, tuple) and len(value) == length
            and all(type(entry) is int for entry in value))


def matrix_vector(matrix, vector):
    return tuple(sum(coefficient * entry
                     for coefficient, entry in zip(row, vector))
                 for row in matrix)


def square_sum(vector):
    return sum(entry * entry for entry in vector)


def real_product(x, y):
    """Product of real pairs using phi^2 = phi + 1."""
    x0, x1 = x
    y0, y1 = y
    return (x0 * y0 + x1 * y1,
            x0 * y1 + x1 * y0 + x1 * y1)


def off_diagonal_norm(c):
    """c*conjugate(c) as an independent real pair.

    j+j^-1 = phi-1, and j^2+j^-2 = j^3+j^-3 = -phi.
    """
    c0, c1, c2, c3 = c
    adjacent = c0 * c1 + c1 * c2 + c2 * c3
    other = c0 * c2 + c0 * c3 + c1 * c3
    return (square_sum(c) - adjacent, adjacent - other)


def times_j(c):
    c0, c1, c2, c3 = c
    return (-c3, c0 - c3, c1 - c3, c2 - c3)


def times_j_inverse(c):
    c0, c1, c2, c3 = c
    return (c1 - c0, c2 - c0, c3 - c0, -c0)


def hermitian_A(h):
    """a -> (2-phi)a, d -> (1+phi)d, c -> j*c."""
    a0, a1, d0, d1 = h[:4]
    return (2 * a0 - a1, -a0 + a1, d0 + d1, d0 + 2 * d1,
            *times_j(h[4:]))


def hermitian_A_inverse(h):
    """a -> (1+phi)a, d -> (2-phi)d, c -> j^-1*c."""
    a0, a1, d0, d1 = h[:4]
    return (a0 + a1, a0 + 2 * a1, 2 * d0 - d1, -d0 + d1,
            *times_j_inverse(h[4:]))


def hermitian_B(h, shear):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    return (
        a0 + shear * (2 * c0 - c1) + shear * shear * d0,
        a1 + shear * (c1 - c2 - c3) + shear * shear * d1,
        d0, d1,
        c0 + shear * d0, c1, c2 - shear * d1, c3 - shear * d1,
    )


def hermitian_cost(h):
    a0, a1, d0, d1 = h[:4]
    return (4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
            + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
            + 10 * square_sum(h[4:]) - 2 * sum(h[4:]) ** 2)


def hermitian_cost_via_real_pairs(h):
    """Trace of a^2+d^2+2*c*cbar, using Tr_K(u+v*phi)=4u+2v."""
    aa = real_product(h[:2], h[:2])
    dd = real_product(h[2:4], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return 4 * (aa[0] + dd[0] + 2 * cc[0]) + 2 * (aa[1] + dd[1] + 2 * cc[1])


def hermitian_determinant(h):
    ad = real_product(h[:2], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return (ad[0] - cc[0], ad[1] - cc[1])


def core_member(core):
    if not isinstance(core, tuple) or len(core) != 9:
        return False
    s, q, h, reference, detector, numerator, previous, counter, phase = core
    return (
        type(s) is int and type(q) is int
        and all(integer_tuple(register, 8) for register in (h, reference, detector))
        and integer_tuple(numerator, 5) and integer_tuple(previous, 5)
        and type(counter) is int and counter >= 1
        and type(phase) is int and 0 <= phase < 7
    )


def state_member(state):
    return (isinstance(state, tuple) and len(state) == 3
            and core_member(state[0]) and type(state[1]) is int and state[1] >= 0
            and type(state[2]) is int and state[2] in (-1, 1))


def core_cost(core):
    s, q, h, reference, detector, numerator, previous, counter, _ = core
    return (1 + s * s - s * q + q * q
            + hermitian_cost(h) + hermitian_cost(reference) + hermitian_cost(detector)
            + counter + square_sum(numerator) + square_sum(previous))


def bare_height(core):
    return 7 * (core[7] - 1) + core[8]


def next_core(core, coupling=1):
    s, q, h, reference, detector, numerator, previous, counter, phase = core
    if phase == 0:
        s, q = s - q, s
    elif phase == 1:
        h = hermitian_B(h, -q)
    elif phase == 2:
        h = hermitian_A_inverse(h)
    elif phase == 3:
        h = hermitian_B(h, q)
    elif phase == 4:
        h = hermitian_A(h)
    elif phase == 5:
        detector = tuple(z + value - base
                         for z, value, base in zip(detector, h, reference))
    elif phase == 6:
        multiplier = M if counter == 1 else M2
        force = 2 * coupling * (h[5] - reference[5])
        applied = matrix_vector(C_MATRIX, numerator)
        following = tuple(value - multiplier * old + force * dipole
                          for value, old, dipole in zip(applied, previous, DIPOLE))
        numerator, previous = following, numerator
        counter += 1
    else:
        raise ValueError("phase outside carrier")
    return (s, q, h, reference, detector, numerator, previous, counter, (phase + 1) % 7)


def previous_core(core, coupling=1):
    s, q, h, reference, detector, numerator, previous, counter, phase = core
    if phase == 0:
        if counter == 1:
            return None
        divisor = M if counter == 2 else M2
        force = 2 * coupling * (h[5] - reference[5])
        applied = matrix_vector(C_MATRIX, previous)
        residual = tuple(value - now + force * dipole
                         for value, now, dipole in zip(applied, numerator, DIPOLE))
        if any(entry % divisor for entry in residual):
            return None
        numerator, previous = previous, tuple(entry // divisor for entry in residual)
        counter -= 1
    elif phase == 1:
        s, q = q, q - s
    elif phase == 2:
        h = hermitian_B(h, q)
    elif phase == 3:
        h = hermitian_A(h)
    elif phase == 4:
        h = hermitian_B(h, -q)
    elif phase == 5:
        h = hermitian_A_inverse(h)
    elif phase == 6:
        detector = tuple(z - value + base
                         for z, value, base in zip(detector, h, reference))
    else:
        raise ValueError("phase outside carrier")
    return (s, q, h, reference, detector, numerator, previous, counter, (phase - 1) % 7)


def reverse_direction(state):
    return (state[0], state[1], -state[2])


def funded_step(state, coupling=1):
    core, bank, direction = state
    if direction == 1:
        target = next_core(core, coupling)
    elif direction == -1:
        target = previous_core(core, coupling)
    else:
        raise ValueError("direction outside carrier")
    ceiling = core_cost(core) + bank
    if target is None or core_cost(target) > ceiling:
        return (core, bank, -direction)
    return (target, ceiling - core_cost(target), direction)


def conjugate_inverse(state, coupling=1):
    return reverse_direction(funded_step(reverse_direction(state), coupling))


def initial_pair(word):
    for label, first, second in INITIAL_SLICES:
        if label == word:
            return first, second
    raise ValueError("word outside frozen table")


def ready_core(word, source):
    first, second = initial_pair(word)
    return (source, 0, D_H, D_H, Z_H, second, first, 1, 0)


def hermitian_fixtures():
    fixtures = [ZERO_H]
    for index in range(8):
        basis = tuple(1 if site == index else 0 for site in range(8))
        fixtures.append(basis)
        fixtures.append(tuple(-entry for entry in basis))
    fixtures.extend(((1, -1, 2, 0, -2, 1, 0, 1),
                     (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(fixtures) == 19, "CERTIFICATE")
    return tuple(fixtures)


def fixture_core(fixtures, index, counter, phase):
    return (
        index % 3 - 1, (index // 3) % 3 - 1,
        fixtures[index], fixtures[(index + 5) % 19], fixtures[(index + 11) % 19],
        (index - 9, 1, -2, 0, 3), (2, -1, 0, 1, 9 - index), counter, phase,
    )


def check_authority():
    repository = Path(__file__).resolve().parents[2]
    checked = 0
    for name, size, expected_hash in AUTHORITY:
        path = repository / "canon" / name
        require(path.is_file(), "AUTHORITY")
        payload = path.read_bytes()
        require(len(payload) == size, "AUTHORITY")
        require(hashlib.sha256(payload).hexdigest() == expected_hash, "AUTHORITY")
        checked += 1
    require(checked == 5, "CERTIFICATE")
    return checked


def check_initial_data_and_ring():
    require(tuple(row[0] for row in INITIAL_SLICES) == EXPECTED_WORD_ORDER,
            "INITIAL_DATA")
    require(len(set(EXPECTED_WORD_ORDER)) == 10, "INITIAL_DATA")
    for word, first, second in INITIAL_SLICES:
        bits = tuple(int(bit) for bit in word)
        require(len(bits) == 4 and all(bit in (0, 1) for bit in bits), "INITIAL_DATA")
        for t, recorded in enumerate((first, second)):
            location = bits[t + 2] - bits[t]
            from_bits = tuple(int((site - location) % 5 in (0, 1)) for site in range(5))
            require(recorded == from_bits and sum(recorded) == 2, "INITIAL_DATA")
    require(real_product((0, 1), (-1, 1)) == (1, 0), "RING")
    require(real_product((0, 1), (0, 1)) == (1, 1), "RING")
    for index in range(4):
        start = tuple(int(site == index) for site in range(4))
        current = start
        orbit = []
        for _ in range(5):
            orbit.append(current)
            require(times_j_inverse(times_j(current)) == current, "RING")
            current = times_j(current)
        require(current == start, "RING")
        require(tuple(sum(vector[site] for vector in orbit) for site in range(4))
                == (0, 0, 0, 0), "RING")
    for r in range(5):
        require(sum(C_MATRIX[r]) == 648 and sum(L_NUMERATOR[r]) == 0, "INITIAL_DATA")
        for s in range(5):
            require(C_MATRIX[r][s] == C_MATRIX[s][r], "INITIAL_DATA")
            require(C_MATRIX[r][s] + L_NUMERATOR[r][s] == 648 * int(r == s),
                    "INITIAL_DATA")


def check_hermitian_cost(h):
    require(integer_tuple(h, 8), "TRANSPORT")
    value = hermitian_cost(h)
    require(value == hermitian_cost_via_real_pairs(h), "COST")
    require(value >= 2 * square_sum(h), "COST")
    require((value == 0) == (h == ZERO_H), "COST")


def check_transports(fixtures):
    count = 0
    for h in fixtures:
        check_hermitian_cost(h)
        images = (
            (hermitian_A(h), hermitian_A_inverse),
            (hermitian_A_inverse(h), hermitian_A),
        )
        for image, undo in images:
            check_hermitian_cost(image)
            require(undo(image) == h, "TRANSPORT")
            require(hermitian_determinant(image) == hermitian_determinant(h), "TRANSPORT")
            count += 1
        for shear in (-2, -1, 0, 1, 2):
            image = hermitian_B(h, shear)
            check_hermitian_cost(image)
            require(hermitian_B(image, -shear) == h, "TRANSPORT")
            require(hermitian_determinant(image) == hermitian_determinant(h), "TRANSPORT")
            count += 1
    require(count == 133, "CERTIFICATE")
    return count


def check_funded_entry(state, branches):
    require(state_member(state), "BRANCH")
    core, bank, direction = state
    observed = funded_step(state)
    require(state_member(observed), "BRANCH")
    require(core_cost(core) + bank == core_cost(observed[0]) + observed[1], "CONSERVATION")
    require(conjugate_inverse(observed) == state, "FUNDED_INVERSE")
    require(funded_step(conjugate_inverse(state)) == state, "FUNDED_INVERSE")

    attempted = next_core(core) if direction == 1 else previous_core(core)
    if attempted is None:
        expected = (core, bank, -direction)
        branches.add("domain")
    else:
        residual_bank = bank + core_cost(core) - core_cost(attempted)
        if residual_bank < 0:
            expected = (core, bank, -direction)
            branches.add("bank")
        else:
            expected = (attempted, residual_bank, direction)
            branches.add("move")
    require(observed == expected, "BRANCH")


def check_full_carrier(fixtures):
    core_count = 0
    funded_count = 0
    branches = set()
    for index in range(19):
        for counter in (1, 2, 3):
            for phase in range(7):
                core = fixture_core(fixtures, index, counter, phase)
                image = next_core(core)
                require(core_member(core) and core_member(image), "BARE_INVERSE")
                require(previous_core(image) == core, "BARE_INVERSE")
                require(bare_height(image) == bare_height(core) + 1, "BARE_INVERSE")
                core_count += 1
                for candidate in (core, image):
                    increase = core_cost(next_core(candidate)) - core_cost(candidate)
                    banks = (0, 1, 772, max(0, increase - 1),
                             max(0, increase), max(0, increase + 1))
                    for bank in banks:
                        for direction in (-1, 1):
                            check_funded_entry((candidate, bank, direction), branches)
                            funded_count += 1
    require(core_count == 399 and funded_count == 9576, "CERTIFICATE")
    require(branches == {"domain", "bank", "move"}, "BRANCH")

    corrupt_count = 0
    for index in range(19):
        lower = fixture_core(fixtures, index, 1, 0)
        require(previous_core(lower) is None, "IMAGE_GUARD")
        require(funded_step((lower, 1000000000, -1)) == (lower, 1000000000, 1),
                "IMAGE_GUARD")
        for predecessor_counter in (1, 2):
            predecessor = fixture_core(fixtures, index, predecessor_counter, 6)
            image = next_core(predecessor)
            changed_numerator = tuple(value + int(site == 2)
                                      for site, value in enumerate(image[5]))
            corruption = (*image[:5], changed_numerator, *image[6:])
            require(core_member(corruption), "IMAGE_GUARD")
            require(previous_core(corruption) is None, "IMAGE_GUARD")
            require(funded_step((corruption, 1000000000, -1))
                    == (corruption, 1000000000, 1), "IMAGE_GUARD")
            corrupt_count += 1
    require(corrupt_count == 38, "CERTIFICATE")
    return core_count, funded_count, corrupt_count


def reader_denominator(counter):
    return 2 if counter == 0 else 2 * M ** (counter - 1)


def rational_reference(word, source, coupling=1):
    first, second = initial_pair(word)
    result = [tuple(Fraction(value, 2) for value in first),
              tuple(Fraction(value, 2) for value in second)]
    for counter in range(1, 24):
        applied = matrix_vector(C_MATRIX, result[counter])
        amplitude = Fraction(coupling * source * SOURCE_CYCLE[(counter - 1) % 6],
                             M ** counter)
        result.append(tuple(value / M - old + amplitude * dipole
                            for value, old, dipole
                            in zip(applied, result[counter - 1], DIPOLE)))
    return result


def metric_diagonal(value):
    return (Fraction(-1), 1 + value, 1 - value, Fraction(1))


def check_field_record(numerator, counter, expected, free):
    denominator = reader_denominator(counter)
    require(integer_tuple(numerator, 5), "DENOMINATOR")
    common = denominator
    for value in numerator:
        common = math.gcd(common, value)
    require(common == 1, "DENOMINATOR")
    values = tuple(Fraction(value, denominator) for value in numerator)
    reduced_denominator = 1
    for value in values:
        reduced_denominator = (reduced_denominator * value.denominator
                               // math.gcd(reduced_denominator, value.denominator))
    require(reduced_denominator == denominator, "DENOMINATOR")
    require(sum(numerator) == denominator and sum(values) == 1, "MEAN")
    require(values == expected, "RECURRENCE")
    require(max(abs(value) for value in numerator) >= (denominator + 4) // 5, "COST")
    require(5 * square_sum(numerator) >= denominator * denominator, "COST")
    require(5 * (square_sum(numerator) + denominator * denominator)
            >= 6 * denominator * denominator, "COST")
    for value, free_value in zip(values, free):
        require(Fraction(-299, 500) < value < Fraction(499, 500), "LORENTZ")
        diagonal = metric_diagonal(value)
        require(diagonal[1] > Fraction(201, 500)
                and diagonal[2] > Fraction(1, 500), "LORENTZ")
        require(value * value - 1 < Fraction(-999, 250000), "LORENTZ")
        require(abs(value - free_value) < Fraction(1, 125), "RESPONSE_BOUND")
    return values


def local_action(value, previous, following, source):
    kinetic = sum(((now - old) ** 2 + (later - now) ** 2
                   for now, old, later in zip(value, previous, following)), Fraction(0))
    spatial = sum((entry * laplacian for entry, laplacian
                   in zip(value, matrix_vector(L_NUMERATOR, value))), Fraction(0))
    interaction = sum((current * force for current, force in zip(value, source)), Fraction(0))
    return kinetic / 2 - spatial / (2 * M) + interaction


def check_histories():
    payload_hash = hashlib.sha256()
    record_count = 0
    variation_count = 0
    for word, first, second in INITIAL_SLICES:
        free = rational_reference(word, 0)
        for source in (-1, 0, 1):
            reference = rational_reference(word, source)
            numerators = [first, second]
            source_values = {}
            core = ready_core(word, source)
            for counter in range(1, 24):
                require(core[7:] == (counter, 0), "RECURRENCE")
                for _ in range(6):
                    core = next_core(core)
                require(core[7:] == (counter, 6), "SOURCE_PATTERN")
                observed_source = core[2][5] - core[3][5]
                require(observed_source == source * SOURCE_CYCLE[(counter - 1) % 6],
                        "SOURCE_PATTERN")
                source_values[counter] = observed_source
                before_field = core
                core = next_core(core)
                require(previous_core(core) == before_field, "BARE_INVERSE")
                require(core[7:] == (counter + 1, 0), "RECURRENCE")
                numerators.append(core[5])
            require(len(numerators) == 25, "CERTIFICATE")

            history = []
            for counter, numerator in enumerate(numerators):
                values = check_field_record(numerator, counter, reference[counter], free[counter])
                if source == 0:
                    require(values == free[counter], "CONTROL")
                history.append(values)
                denominator = reader_denominator(counter)
                record = (word + "|" + str(source) + "|" + str(counter) + "|"
                          + ",".join(str(value) for value in numerator) + "|"
                          + str(denominator) + "\n")
                payload_hash.update(record.encode("ascii"))
                record_count += 1

            for counter in range(1, 24):
                laplacian = matrix_vector(L_NUMERATOR, history[counter])
                target = tuple(Fraction(source_values[counter] * dipole, M ** counter)
                               for dipole in DIPOLE)
                residual = tuple(later - 2 * now + old + spatial / M
                                 for later, now, old, spatial
                                 in zip(history[counter + 1], history[counter],
                                        history[counter - 1], laplacian))
                require(residual == target, "RECURRENCE")

            for counter in (1, 2, 7, 23):
                forcing = tuple(Fraction(source_values[counter] * dipole, M ** counter)
                                for dipole in DIPOLE)
                for site in range(5):
                    plus = tuple(value + int(index == site)
                                 for index, value in enumerate(history[counter]))
                    minus = tuple(value - int(index == site)
                                  for index, value in enumerate(history[counter]))
                    plus_value = local_action(plus, history[counter - 1], history[counter + 1], forcing)
                    minus_value = local_action(minus, history[counter - 1], history[counter + 1], forcing)
                    require((plus_value - minus_value) / 2 == 0, "ACTION")
                    variation_count += 1
    require(record_count == 750 and variation_count == 600, "CERTIFICATE")
    return record_count, payload_hash.hexdigest(), variation_count


def first_funded_block(source, bank, coupling=1):
    state = (ready_core("0010", source), bank, 1)
    total = core_cost(state[0]) + bank
    history = [state]
    for _ in range(7):
        state = funded_step(state, coupling)
        require(state_member(state), "BRANCH")
        require(core_cost(state[0]) + state[1] == total, "CONSERVATION")
        history.append(state)
    return history


def check_detector(core, expected_coefficient):
    h, reference, detector = core[2:5]
    require(detector[5] == expected_coefficient, "DETECTOR")
    recovered = tuple(value - current + baseline
                      for value, current, baseline in zip(detector, h, reference))
    require(recovered == Z_H, "DETECTOR")


def check_fixed_counter_and_controls():
    prescribed_prefix = {
        -1: (31, 31, 43, 63, 147, 377, 747, 344440),
        1: (31, 31, 43, 63, 147, 377, 803, 347088),
    }
    prescribed_second = {
        -1: (487, 167, -230, 130, 94),
        1: (491, 163, -230, 130, 94),
    }
    prefixes = {}
    sharp_banks = {}
    for source in (-1, 1):
        core = ready_core("0010", source)
        energy_list = [core_cost(core)]
        for _ in range(7):
            core = next_core(core)
            energy_list.append(core_cost(core))
        prefixes[source] = tuple(energy_list)
        require(prefixes[source] == prescribed_prefix[source], "PREFIX")
        require(core[5] == prescribed_second[source], "FIXED_COUNTER")
        sharp_banks[source] = max(energy_list) - energy_list[0]
    sharp_pair = (sharp_banks[-1], sharp_banks[1])
    require(sharp_pair == (344409, 347057), "SHARP_BUDGET")
    common_bank = max(sharp_pair)
    require(common_bank == 347057, "SHARP_BUDGET")

    common_histories = {}
    for source in (-1, 1):
        sharp = first_funded_block(source, sharp_banks[source])
        require(sharp[-1][0][7:] == (2, 0)
                and sharp[-1][1:] == (0, 1), "SHARP_BUDGET")
        under = first_funded_block(source, sharp_banks[source] - 1)
        for tick in range(7):
            require(bare_height(under[tick][0]) == tick and under[tick][2] == 1,
                    "SHARP_BUDGET")
        require(under[-1] == reverse_direction(under[-2]), "SHARP_BUDGET")
        require(under[-1][0][7:] == (1, 6), "SHARP_BUDGET")
        common = first_funded_block(source, common_bank)
        for tick, state in enumerate(common):
            require(bare_height(state[0]) == tick and state[2] == 1, "FIXED_COUNTER")
        require(common[-1][0][7:] == (2, 0), "FIXED_COUNTER")
        require(common[-1][0][5] == prescribed_second[source], "FIXED_COUNTER")
        check_detector(common[6][0], 1 + source)
        check_detector(common[7][0], 1 + source)
        common_histories[source] = common

    negative = common_histories[-1][-1]
    positive = common_histories[1][-1]
    final_banks = (negative[1], positive[1])
    require(final_banks == (2648, 0), "SHARP_BUDGET")
    denominator = reader_denominator(negative[0][7])
    require(negative[0][7] == positive[0][7] == 2, "FIXED_COUNTER")
    negative_field = tuple(Fraction(value, denominator) for value in negative[0][5])
    positive_field = tuple(Fraction(value, denominator) for value in positive[0][5])
    contrast = tuple(upper - lower for upper, lower in zip(positive_field, negative_field))
    require(contrast == tuple(Fraction(value, 162) for value in DIPOLE), "FIXED_COUNTER")
    for lower, upper, difference in zip(negative_field, positive_field, contrast):
        matrix_difference = tuple(x - y for x, y
                                  in zip(metric_diagonal(upper), metric_diagonal(lower)))
        require(matrix_difference == (0, difference, -difference, 0), "FIXED_COUNTER")

    controls = set()
    unforced_reference = rational_reference("0010", 0)[2]
    scaled_free = tuple(value * reader_denominator(2) for value in unforced_reference)
    require(all(value.denominator == 1 for value in scaled_free), "CONTROL")
    unforced_numerator = tuple(value.numerator for value in scaled_free)
    control_outputs = []
    for source in (-1, 1):
        history = first_funded_block(source, common_bank, coupling=0)
        require(history[-1][0][7:] == (2, 0) and history[-1][2] == 1, "CONTROL")
        require(history[-1][0][5] == unforced_numerator, "CONTROL")
        check_detector(history[6][0], 1 + source)
        check_detector(history[7][0], 1 + source)
        control_outputs.append(history[-1][0][5])
    require(control_outputs[0] == control_outputs[1], "CONTROL")
    controls.add("coupling_zero")

    for source in (-1, 1):
        image = common_histories[source][-1][0]
        require(previous_core(image) == common_histories[source][-2][0], "IMAGE_GUARD")
        absent_force = tuple(value - now for value, now
                             in zip(matrix_vector(C_MATRIX, image[6]), image[5]))
        require(any(value % M for value in absent_force), "CONTROL")
    controls.add("omitted_inverse_source")

    before = common_histories[1][6][0]
    force = 2 * (before[2][5] - before[3][5])
    wrong_first = tuple(value - M2 * previous + force * dipole
                        for value, previous, dipole
                        in zip(matrix_vector(C_MATRIX, before[5]), before[6], DIPOLE))
    require(sum(wrong_first) != reader_denominator(2), "CONTROL")
    require(wrong_first != positive[0][5], "CONTROL")
    controls.add("wrong_first_multiplier")

    ready = ready_core("0010", 0)
    degenerate = (*ready[:5], (2, 0, 0, 0, 0), *ready[6:])
    require(core_member(degenerate), "CONTROL")
    bad_reading = Fraction(degenerate[5][0], reader_denominator(degenerate[7]))
    require(metric_diagonal(bad_reading) == (-1, 2, 0, 1), "CONTROL")
    require(bad_reading * bad_reading - 1 == 0, "CONTROL")
    controls.add("unrestricted_degeneracy")
    require(controls == {"coupling_zero", "omitted_inverse_source",
                         "wrong_first_multiplier", "unrestricted_degeneracy"}, "CERTIFICATE")

    return (prefixes[-1], prefixes[1], negative[0][5], positive[0][5],
            sharp_pair, final_banks, contrast, len(controls))


def check_cycles():
    fixtures = (
        (-1, 772, 14), (-1, 344409, 18), (-1, 347057, 24), (-1, 344408, 14),
        (1, 772, 14), (1, 344409, 14), (1, 347057, 18), (1, 347056, 14),
    )
    observed_periods = []
    for source, bank, expected_period in fixtures:
        start = (ready_core("0010", source), bank, 1)
        current = start
        total = core_cost(start[0]) + bank
        seen = {start}
        first_return = None
        for tick in range(1, expected_period + 1):
            current = funded_step(current)
            require(state_member(current), "PERIOD")
            require(core_cost(current[0]) + current[1] == total, "CONSERVATION")
            if current == start:
                first_return = tick
                break
            require(current not in seen, "PERIOD")
            seen.add(current)
        require(first_return == expected_period, "PERIOD")
        require(current == start and len(seen) == first_return, "PERIOD")
        observed_periods.append(first_return)
    require(len(observed_periods) == 8, "CERTIFICATE")
    return tuple(observed_periods)


def comma(values):
    return ",".join(str(value) for value in values)


def certificate_bytes():
    authority_count = check_authority()
    check_initial_data_and_ring()
    fixtures = hermitian_fixtures()
    transport_count = check_transports(fixtures)
    core_count, funded_count, image_count = check_full_carrier(fixtures)
    history_count, history_hash, action_count = check_histories()
    (prefix_negative, prefix_positive, second_negative, second_positive,
     sharp, final_banks, contrast, control_count) = check_fixed_counter_and_controls()
    periods = check_cycles()
    require(control_count == 4, "CERTIFICATE")
    lines = (
        "CERTIFICATE=" + PROBE_ID,
        "AUTHORITY_FILES=" + str(authority_count),
        "TRANSPORT_CHECKS=" + str(transport_count),
        "CORE_FIXTURES=" + str(core_count),
        "FUNDED_CASES=" + str(funded_count),
        "IMAGE_DEFECTS=" + str(image_count),
        "HISTORY_RECORDS=" + str(history_count),
        "HISTORY_SHA256=" + history_hash,
        "ACTION_VARIATIONS=" + str(action_count),
        "PREFIX_NEG=" + comma(prefix_negative),
        "PREFIX_POS=" + comma(prefix_positive),
        "P2_NEG=" + comma(second_negative),
        "P2_POS=" + comma(second_positive),
        "SHARP_BANKS=" + comma(sharp),
        "COMMON_FINAL_BANKS=" + comma(final_banks),
        "METRIC_CONTRAST=" + comma(contrast),
        "CYCLE_PERIODS=" + comma(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 19, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate_bytes()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
