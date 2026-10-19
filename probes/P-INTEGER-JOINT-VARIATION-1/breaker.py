#!/usr/bin/env python3
"""Independent rational/direct-coordinate audit of the prospective model.

Do not execute or import before the complete public pin is read back.
Written from PREREG.md without reading this probe's verify.py or PROOF.md.
The primary and breaker share the specification and assisted-session context;
this is implementation independence, not a claim of a separate laboratory.
This implementation advances Fraction-valued fields and sources and tests
backward integrality. Hermitian arithmetic uses direct eight-coordinate
formulas, including the established A/B and real-pair formulas from #1644.
It neither imports the primary nor reads expected output or proof files.
"""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import sys


PROBE_ID = "P-INTEGER-JOINT-VARIATION-1"
M = 324
DIPOLE = (1, -1, 0, 0, 0)
SOURCE_FREE_CYCLE = (1, 2, 2, 1, 0, 0)
ZERO_H = (0, 0, 0, 0, 0, 0, 0, 0)
D_H = (0, 0, 1, 0, 0, 0, 0, 0)

# Literal encoding, independently checked against the canonical bit formula.
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
    "AUTHORITY", "RING", "TRANSPORT", "HOLONOMY", "COST", "INITIAL_DATA",
    "INTEGER", "BARE_INVERSE", "FUNDED_INVERSE", "CONSERVATION", "BRANCH",
    "IMAGE_GUARD", "RECURRENCE", "MEAN", "SOURCE_READER", "LORENTZ",
    "RESPONSE_BOUND", "SOURCE_BOUND", "ACTION", "OFFSHELL_ACTION",
    "FIXED_COUNTER", "CONTROL", "SHARP_BUDGET", "PERIOD", "CERTIFICATE",
    "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    """An observed violation of a frozen scientific predicate."""

    def __init__(self, key):
        if key not in FALSIFIER_KEYS:
            raise ValueError("unregistered falsifier key")
        self.key = key
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def squared_norm(vector):
    return sum(entry * entry for entry in vector)


def inner_product(left, right):
    return sum(a * b for a, b in zip(left, right))


def integer_tuple(value, length):
    return (isinstance(value, tuple) and len(value) == length
            and all(type(entry) is int for entry in value))


def scale_at(counter):
    if type(counter) is not int or counter < 0:
        raise ValueError("counter outside scale domain")
    return 2 * M ** (counter * (counter - 1) // 2)


def laplacian(field):
    return tuple(Fraction(188 * field[r]
                          - 29 * (field[(r - 1) % 5] + field[(r + 1) % 5])
                          - 65 * (field[(r - 2) % 5] + field[(r + 2) % 5])) / M
                 for r in range(5))


def real_product(left, right):
    a, b = left
    c, d = right
    return (a * c + b * d, a * d + b * c + b * d)


def off_diagonal_norm(c):
    c0, c1, c2, c3 = c
    adjacent = c0 * c1 + c1 * c2 + c2 * c3
    other = c0 * c2 + c0 * c3 + c1 * c3
    return (squared_norm(c) - adjacent, adjacent - other)


def times_j(c):
    c0, c1, c2, c3 = c
    return (-c3, c0 - c3, c1 - c3, c2 - c3)


def times_j_inverse(c):
    c0, c1, c2, c3 = c
    return (c1 - c0, c2 - c0, c3 - c0, -c0)


def hermitian_A(h):
    a0, a1, d0, d1 = h[:4]
    return (2 * a0 - a1, -a0 + a1, d0 + d1, d0 + 2 * d1,
            *times_j(h[4:]))


def hermitian_A_inverse(h):
    a0, a1, d0, d1 = h[:4]
    return (a0 + a1, a0 + 2 * a1, 2 * d0 - d1, -d0 + d1,
            *times_j_inverse(h[4:]))


def hermitian_B(h, t):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    return (a0 + t * (2 * c0 - c1) + t * t * d0,
            a1 + t * (c1 - c2 - c3) + t * t * d1,
            d0, d1, c0 + t * d0, c1, c2 - t * d1, c3 - t * d1)


def hermitian_M(h, t):
    """Direct action of [[1,t*(-2+j-j^2)],[0,1]], without factor gates."""
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    cross0 = -5 * c0 + 5 * c1 - 3 * c2 + c3
    cross1 = 2 * c0 - 3 * c1 + 3 * c2
    return (a0 + t * cross0 + t * t * (9 * d0 - 5 * d1),
            a1 + t * cross1 + t * t * (-5 * d0 + 4 * d1),
            d0, d1,
            c0 + t * (-2 * d0 + d1), c1 + t * d0,
            c2 + t * (-d0 + 2 * d1), c3 + t * d1)


def hermitian_cost(h):
    a0, a1, d0, d1 = h[:4]
    return (4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
            + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
            + 10 * squared_norm(h[4:]) - 2 * sum(h[4:]) ** 2)


def hermitian_trace_cost(h):
    aa = real_product(h[:2], h[:2])
    dd = real_product(h[2:4], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return (4 * (aa[0] + dd[0] + 2 * cc[0])
            + 2 * (aa[1] + dd[1] + 2 * cc[1]))


def hermitian_determinant(h):
    ad = real_product(h[:2], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return (ad[0] - cc[0], ad[1] - cc[1])


def ready_hermitian(numerator):
    return (9 * numerator * numerator, -5 * numerator * numerator, 1, 0,
            -2 * numerator, numerator, -numerator, 0)


def core_member(core):
    if not isinstance(core, tuple) or len(core) != 6:
        return False
    p, w, y, v, h, k = core
    return (integer_tuple(p, 5) and integer_tuple(w, 5)
            and type(y) is int and type(v) is int and integer_tuple(h, 8)
            and type(k) is int and k >= 1)


def state_member(state):
    return (isinstance(state, tuple) and len(state) == 3
            and core_member(state[0]) and type(state[1]) is int and state[1] >= 0
            and type(state[2]) is int and state[2] in (-1, 1))


def decode(core):
    p, w, y, v, _, k = core
    d = scale_at(k)
    previous_d = scale_at(k - 1)
    return (tuple(Fraction(entry, d) for entry in p),
            tuple(Fraction(entry, previous_d) for entry in w),
            Fraction(y, d), Fraction(v, previous_d))


def encode_integer(value, denominator):
    scaled = value * denominator
    require(isinstance(scaled, Fraction) and scaled.denominator == 1, "INTEGER")
    return scaled.numerator


def next_core(core, a, metric_coupling=1, feedback=1, move_hermitian=True):
    """Fraction recurrence; optional flags are separately labelled controls."""
    p, _, y, _, h, k = core
    field, previous_field, source, previous_source = decode(core)
    spatial = laplacian(field)
    next_field = tuple(2 * now - old - spatial_entry
                       + metric_coupling * source * dipole / M ** k
                       for now, old, spatial_entry, dipole in
                       zip(field, previous_field, spatial, DIPOLE))
    next_source = (source - previous_source + a
                   - feedback * inner_product(DIPOLE, field) / M ** k)
    next_d = scale_at(k + 1)
    next_p = tuple(encode_integer(value, next_d) for value in next_field)
    next_y = encode_integer(next_source, next_d)
    next_h = hermitian_M(h, next_y - y) if move_hermitian else h
    return (next_p, p, next_y, y, next_h, k + 1)


def older_numerators(core, a):
    """Recover rational numerators, without the primary's congruence formula."""
    k = core[5]
    if k == 1:
        return None
    field, previous_field, source, previous_source = decode(core)
    n = k - 1
    spatial = laplacian(previous_field)
    older_field = tuple(2 * old - now - spatial_entry
                        + previous_source * dipole / M ** n
                        for old, now, spatial_entry, dipole in
                        zip(previous_field, field, spatial, DIPOLE))
    older_source = (previous_source - source + a
                    - inner_product(DIPOLE, previous_field) / M ** n)
    d = scale_at(k - 2)
    return tuple(value * d for value in older_field) + (older_source * d,)


def previous_core(core, a):
    numerators = older_numerators(core, a)
    if numerators is None or any(value.denominator != 1 for value in numerators):
        return None
    _, w, y, v, h, k = core
    old_w = tuple(value.numerator for value in numerators[:5])
    old_v = numerators[5].numerator
    return (w, old_w, v, old_v, hermitian_M(h, v - y), k - 1)


def core_energy(core):
    p, w, y, v, h, k = core
    return 1 + k + squared_norm(p) + squared_norm(w) + y * y + v * v + hermitian_cost(h)


def reverse(state):
    return (state[0], state[1], -state[2])


def funded_step(state, a):
    core, bank, direction = state
    if direction == 1:
        target = next_core(core, a)
    elif direction == -1:
        target = previous_core(core, a)
    else:
        raise ValueError("direction outside carrier")
    ceiling = core_energy(core) + bank
    if target is None or core_energy(target) > ceiling:
        return (core, bank, -direction)
    return (target, ceiling - core_energy(target), direction)


def inverse_funded(state, a):
    return reverse(funded_step(reverse(state), a))


def initial_pair(word):
    for label, first, second in INITIAL_SLICES:
        if label == word:
            return first, second
    raise ValueError("word outside frozen family")


def ready_core(word, a):
    first, second = initial_pair(word)
    return (second, first, 2 * a, 0, ready_hermitian(2 * a), 1)


def check_authority():
    repository = Path(__file__).resolve().parents[2]
    count = 0
    for name, size, digest in AUTHORITY:
        payload = (repository / "canon" / name).read_bytes()
        require(len(payload) == size and sha256(payload).hexdigest() == digest, "AUTHORITY")
        count += 1
    require(count == 5, "CERTIFICATE")
    return count


def check_initial_data_and_ring():
    expected_order = ("0010", "0011", "0100", "0101", "0110",
                      "1001", "1010", "1011", "1100", "1101")
    require(tuple(row[0] for row in INITIAL_SLICES) == expected_order, "INITIAL_DATA")
    require(len(set(expected_order)) == 10, "INITIAL_DATA")
    for word, first, second in INITIAL_SLICES:
        bits = tuple(int(bit) for bit in word)
        for n, literal in enumerate((first, second)):
            site = bits[n + 2] - bits[n]
            require(literal == tuple(int((r - site) % 5 in (0, 1))
                                     for r in range(5)), "INITIAL_DATA")
    require(real_product((0, 1), (0, 1)) == (1, 1), "RING")
    require(real_product((0, 1), (-1, 1)) == (1, 0), "RING")
    for index in range(4):
        basis = tuple(int(index == site) for site in range(4))
        orbit = []
        current = basis
        for _ in range(5):
            orbit.append(current)
            require(times_j_inverse(times_j(current)) == current, "RING")
            current = times_j(current)
        require(current == basis, "RING")
        require(tuple(sum(row[site] for row in orbit) for site in range(4))
                == (0, 0, 0, 0), "RING")


def hermitian_fixtures():
    fixtures = [ZERO_H]
    for index in range(8):
        basis = tuple(int(index == site) for site in range(8))
        fixtures.extend((basis, tuple(-entry for entry in basis)))
    fixtures.extend(((1, -1, 2, 0, -2, 1, 0, 1),
                     (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(fixtures) == 19, "CERTIFICATE")
    return tuple(fixtures)


def check_h_cost(h):
    require(integer_tuple(h, 8), "TRANSPORT")
    value = hermitian_cost(h)
    require(value == hermitian_trace_cost(h), "COST")
    require(value >= 2 * squared_norm(h), "COST")
    require((value == 0) == (h == ZERO_H), "COST")


def check_transports(fixtures):
    transport_count = 0
    holonomy_count = 0
    for h in fixtures:
        check_h_cost(h)
        for transformed, inverse in ((hermitian_A(h), hermitian_A_inverse),
                                     (hermitian_A_inverse(h), hermitian_A)):
            check_h_cost(transformed)
            require(inverse(transformed) == h, "TRANSPORT")
            require(hermitian_determinant(transformed) == hermitian_determinant(h),
                    "TRANSPORT")
            transport_count += 1
        for t in (-2, -1, 0, 1, 2):
            transformed = hermitian_B(h, t)
            check_h_cost(transformed)
            require(hermitian_B(transformed, -t) == h, "TRANSPORT")
            require(hermitian_determinant(transformed) == hermitian_determinant(h),
                    "TRANSPORT")
            transport_count += 1
            direct = hermitian_M(h, t)
            factors = hermitian_A(hermitian_B(hermitian_A_inverse(
                hermitian_B(h, -t)), t))
            require(direct == factors, "HOLONOMY")
            require(hermitian_M(direct, -t) == h, "HOLONOMY")
            require(hermitian_determinant(direct) == hermitian_determinant(h),
                    "HOLONOMY")
            check_h_cost(direct)
            holonomy_count += 1
    require((transport_count, holonomy_count) == (133, 95), "CERTIFICATE")
    return transport_count, holonomy_count


def check_funded_case(state, a, branches):
    require(state_member(state), "BRANCH")
    core, bank, direction = state
    result = funded_step(state, a)
    require(state_member(result), "BRANCH")
    require(inverse_funded(result, a) == state, "FUNDED_INVERSE")
    require(funded_step(inverse_funded(state, a), a) == state, "FUNDED_INVERSE")
    require(core_energy(result[0]) + result[1] == core_energy(core) + bank,
            "CONSERVATION")
    target = next_core(core, a) if direction == 1 else previous_core(core, a)
    label = "forward" if direction == 1 else "backward"
    if target is None:
        branches.add(label + "_domain")
        expected = reverse(state)
    elif core_energy(target) > core_energy(core) + bank:
        branches.add(label + "_bank")
        expected = reverse(state)
    else:
        branches.add(label + "_move")
        expected = (target, core_energy(core) + bank - core_energy(target), direction)
    require(result == expected, "BRANCH")


def check_core_and_funding(fixtures):
    base = []
    for a in (-1, 0, 1):
        for i in range(19):
            for k in (1, 2, 3):
                core = ((i - 9, 1, -2, 0, 3), (2, -1, 0, 1, 9 - i),
                        i % 5 - 2, (i // 5) % 5 - 2, fixtures[i], k)
                base.append((a, core))
    require(len(base) == 171, "CERTIFICATE")
    decreasing = ((0, 0, 324, 0, 0), (65, 29, 460, 29, 65), 0, 0, D_H, 1)
    require(core_energy(next_core(decreasing, 0)) < core_energy(decreasing), "COST")
    entries = base + [(0, decreasing)]
    core_count = funded_count = 0
    branches = set()
    for a, core in entries:
        image = next_core(core, a)
        require(core_member(core) and core_member(image), "INTEGER")
        require(previous_core(image, a) == core and image[5] == core[5] + 1,
                "BARE_INVERSE")
        backward = previous_core(core, a)
        if backward is not None:
            require(next_core(backward, a) == core, "BARE_INVERSE")
        core_count += 1
        for candidate in (core, image):
            increase = core_energy(next_core(candidate, a)) - core_energy(candidate)
            banks = (0, 1, 772, max(0, increase - 1),
                     max(0, increase), max(0, increase + 1))
            for bank in banks:
                for direction in (-1, 1):
                    check_funded_case((candidate, bank, direction), a, branches)
                    funded_count += 1
    require((core_count, funded_count) == (172, 4128), "CERTIFICATE")
    require(branches == {"forward_move", "backward_move", "forward_bank",
                         "backward_bank", "backward_domain"}, "BRANCH")

    corruption_entries = [(a, core) for a, core in base if core[5] in (1, 2)]
    require(len(corruption_entries) == 114, "CERTIFICATE")
    image_count = 0
    for a, core in corruption_entries:
        if core[5] == 1:
            require(previous_core(core, a) is None, "IMAGE_GUARD")
            require(funded_step((core, 1000000000, -1), a)
                    == (core, 1000000000, 1), "IMAGE_GUARD")
        image = next_core(core, a)
        p, w, y, v, h, k = image
        for site in range(6):
            corrupt_p = tuple(value + int(site == index)
                              for index, value in enumerate(p))
            corrupt_y = y + int(site == 5)
            corrupted = (corrupt_p, w, corrupt_y, v, h, k)
            require(core_member(corrupted), "INTEGER")
            require(previous_core(corrupted, a) is None, "IMAGE_GUARD")
            require(funded_step((corrupted, 1000000000, -1), a)
                    == (corrupted, 1000000000, 1), "IMAGE_GUARD")
            image_count += 1
    require(image_count == 684, "CERTIFICATE")
    return core_count, funded_count, image_count


def history(word, a, stop=12, metric_coupling=1, feedback_mode="all"):
    first, second = initial_pair(word)
    rows = [(first, 0, scale_at(0), D_H),
            (second, 2 * a, scale_at(1), ready_hermitian(2 * a))]
    core = ready_core(word, a)
    cores = {1: core}
    for n in range(1, stop):
        require(core[5] == n, "RECURRENCE")
        if feedback_mode == "all":
            feedback = 1
        elif feedback_mode == "none":
            feedback = 0
        elif feedback_mode == "first":
            feedback = int(n == 1)
        elif feedback_mode == "reversed":
            feedback = -1
        else:
            raise ValueError("unknown control")
        core = next_core(core, a, metric_coupling=metric_coupling, feedback=feedback)
        require(core_member(core), "INTEGER")
        cores[n + 1] = core
        rows.append((core[0], core[2], scale_at(n + 1), core[4]))
    fields = [tuple(Fraction(value, row[2]) for value in row[0]) for row in rows]
    sources = [Fraction(row[1], row[2]) for row in rows]
    return rows, fields, sources, cores


def free_field_history(word, stop=12):
    first, second = initial_pair(word)
    fields = [tuple(Fraction(value, 2) for value in first),
              tuple(Fraction(value, 2) for value in second)]
    for n in range(1, stop):
        spatial = laplacian(fields[n])
        fields.append(tuple(2 * now - old - spatial_entry
                            for now, old, spatial_entry in
                            zip(fields[n], fields[n - 1], spatial)))
    return fields


def local_action(field, source, previous_field, following_field,
                 previous_source, following_source, n, a):
    """Expanded edge-square potential, independently of laplacian()."""
    kinetic_field = Fraction(sum((value - old) ** 2 + (later - value) ** 2
                                for value, old, later in
                                zip(field, previous_field, following_field)), 2)
    spatial_edges = sum(29 * (field[r] - field[(r + 1) % 5]) ** 2
                        + 65 * (field[r] - field[(r + 2) % 5]) ** 2
                        for r in range(5))
    potential_field = Fraction(spatial_edges, 2 * M)
    kinetic_source = Fraction((source - previous_source) ** 2
                              + (following_source - source) ** 2, 2)
    potential_source = Fraction(source * source, 2) - a * source
    interaction = Fraction(source) * (field[0] - field[1]) / M ** n
    return kinetic_field - potential_field - kinetic_source + potential_source + interaction


def central_gradients(case):
    field, source, previous_field, following_field, previous_source, following_source, n, a = case
    gradients = []
    for site in range(5):
        plus = tuple(value + int(site == index) for index, value in enumerate(field))
        minus = tuple(value - int(site == index) for index, value in enumerate(field))
        gradients.append(Fraction(
            local_action(plus, source, previous_field, following_field,
                         previous_source, following_source, n, a)
            - local_action(minus, source, previous_field, following_field,
                           previous_source, following_source, n, a), 2))
    gradients.append(Fraction(
        local_action(field, source + 1, previous_field, following_field,
                     previous_source, following_source, n, a)
        - local_action(field, source - 1, previous_field, following_field,
                       previous_source, following_source, n, a), 2))
    return tuple(gradients)


def formula_gradients(case):
    field, source, previous_field, following_field, previous_source, following_source, n, a = case
    spatial = laplacian(field)
    field_gradient = tuple(2 * now - old - later - spatial_entry
                           + Fraction(source) * dipole / M ** n
                           for now, old, later, spatial_entry, dipole in
                           zip(field, previous_field, following_field, spatial, DIPOLE))
    source_gradient = (following_source - source + previous_source - a
                       + inner_product(DIPOLE, field) / M ** n)
    return field_gradient + (source_gradient,)


def local_case(data, n, a):
    _, fields, sources, _ = data
    return (fields[n], sources[n], fields[n - 1], fields[n + 1],
            sources[n - 1], sources[n + 1], n, a)


def check_histories():
    digest = sha256()
    records = variations = 0
    histories = {}
    require(Fraction(1630, 209304) < Fraction(1, 125), "RESPONSE_BOUND")
    require(Fraction(648, 323) < 3, "SOURCE_BOUND")
    for word, _, _ in INITIAL_SLICES:
        free = free_field_history(word)
        for a in (-1, 0, 1):
            data = history(word, a)
            histories[word, a] = data
            rows, fields, sources, cores = data
            require(len(rows) == 13, "CERTIFICATE")
            for n, (p, y, denominator, h) in enumerate(rows):
                field = fields[n]
                source = sources[n]
                require(integer_tuple(p, 5) and type(y) is int
                        and integer_tuple(h, 8), "INTEGER")
                require(denominator == scale_at(n), "INTEGER")
                require(sum(p) == denominator and sum(field) == 1, "MEAN")
                require(tuple(value * denominator for value in field) == p
                        and source * denominator == y, "INTEGER")
                require(h == ready_hermitian(y), "SOURCE_READER")
                require(Fraction(h[5], denominator) == source, "SOURCE_READER")
                require(hermitian_determinant(h) == (0, 0), "SOURCE_READER")
                check_h_cost(h)
                require(hermitian_cost(h) == 294 * y ** 4 + 52 * y * y + 4,
                        "COST")
                if n >= 1:
                    require(core_member(cores[n]), "INTEGER")
                    require(5 * core_energy(cores[n]) >= denominator * denominator,
                            "COST")
                require(5 * squared_norm(p) >= denominator * denominator, "COST")
                free_source = 0 if n == 0 else a * SOURCE_FREE_CYCLE[(n - 1) % 6]
                require(abs(source - free_source) < Fraction(2, 323), "SOURCE_BOUND")
                require(abs(source) < Fraction(648, 323), "SOURCE_BOUND")
                for value, free_value in zip(field, free[n]):
                    require(abs(value - free_value) < Fraction(1630, 209304),
                            "RESPONSE_BOUND")
                    require(Fraction(-299, 500) < value < Fraction(499, 500), "LORENTZ")
                    require(1 + value > Fraction(201, 500)
                            and 1 - value > Fraction(1, 500), "LORENTZ")
                    require(value * value - 1 < Fraction(-999, 250000), "LORENTZ")
                record = (word + "|" + str(a) + "|" + str(n) + "|"
                          + comma(p) + "|" + str(y) + "|" + str(denominator)
                          + "|" + comma(h) + "\n")
                digest.update(record.encode("ascii"))
                records += 1
            for n in range(1, 12):
                spatial = laplacian(fields[n])
                field_residual = tuple(future - 2 * now + past + spatial_entry
                                       for future, now, past, spatial_entry in
                                       zip(fields[n + 1], fields[n], fields[n - 1], spatial))
                require(field_residual == tuple(sources[n] * dipole / M ** n
                                                for dipole in DIPOLE), "RECURRENCE")
                require(sources[n + 1] - sources[n] + sources[n - 1]
                        == a - inner_product(DIPOLE, fields[n]) / M ** n,
                        "RECURRENCE")
            for n in (1, 2, 5, 11):
                gradient = central_gradients(local_case(data, n, a))
                require(gradient == (0, 0, 0, 0, 0, 0), "ACTION")
                variations += len(gradient)
    require((records, variations) == (390, 720), "CERTIFICATE")
    return records, digest.hexdigest(), variations, histories


def check_offshell(histories):
    base = local_case(histories["0011", 0], 2, 0)
    field, source, previous_field, following_field, previous_source, following_source, n, a = base
    field_shift = tuple(value + int(index == 0) for index, value in enumerate(field))
    next_shift = tuple(value + int(index == 2) for index, value in enumerate(following_field))
    cases = (
        (field_shift, source, previous_field, following_field,
         previous_source, following_source, n, a),
        (field, source + 1, previous_field, following_field,
         previous_source, following_source, n, a),
        (field, source, previous_field, following_field,
         previous_source, following_source + 1, n, a),
        (field, source, previous_field, next_shift,
         previous_source, following_source, n, a),
        (field, source, previous_field, following_field,
         previous_source - 1, following_source, n, a),
        ((Fraction(1, 3), Fraction(-2, 5), Fraction(0), Fraction(3, 7), Fraction(-1)),
         Fraction(-2, 3), (Fraction(0),) * 5, (Fraction(1),) * 5,
         Fraction(1, 2), Fraction(-3, 4), 2, 1),
    )
    count = 0
    for case in cases:
        observed = central_gradients(case)
        expected = formula_gradients(case)
        require(observed == expected and any(value != 0 for value in observed),
                "OFFSHELL_ACTION")
        count += len(observed)
    require(count == 36, "CERTIFICATE")
    return count


def check_witnesses_and_controls(histories):
    negative = histories["0010", -1]
    positive = histories["0010", 1]
    require(negative[0][2][0] == (487, 167, -230, 130, 94)
            and negative[0][2][1] == -1296, "FIXED_COUNTER")
    require(positive[0][2][0] == (491, 163, -230, 130, 94)
            and positive[0][2][1] == 1296, "FIXED_COUNTER")
    direct_contrast = tuple(upper - lower for upper, lower in
                            zip(positive[1][2], negative[1][2]))
    require(direct_contrast == tuple(Fraction(value, 162) for value in DIPOLE),
            "FIXED_COUNTER")

    zero = histories["0011", 0]
    rows, fields, sources, cores = zero
    require(rows[2][:3] == ((94, 165, 165, 94, 130), 1, 648), "FIXED_COUNTER")
    require(rows[3][:3] == ((22236121, -2269621, -2269620, 22236120, 28091448),
                           105047, 68024448), "FIXED_COUNTER")
    require(sources[2] == Fraction(1, 648), "FIXED_COUNTER")
    free = free_field_history("0011")
    reciprocal_contrast = tuple(value - reference for value, reference in zip(fields[3], free[3]))
    require(reciprocal_contrast == tuple(Fraction(value, 68024448) for value in DIPOLE),
            "FIXED_COUNTER")
    require(core_energy(cores[1]) == 10 and core_energy(cores[2]) == 89378, "COST")
    sharp = core_energy(cores[2]) - core_energy(cores[1])
    require(sharp == 89368, "SHARP_BUDGET")
    require(funded_step((cores[1], sharp, 1), 0) == (cores[2], 0, 1), "SHARP_BUDGET")
    require(funded_step((cores[1], sharp - 1, 1), 0)
            == (cores[1], sharp - 1, -1), "SHARP_BUDGET")

    controls = set()
    disabled = history("0011", 0, stop=3, feedback_mode="none")
    require(disabled[2] == [0, 0, 0, 0] and disabled[1] == free[:4], "CONTROL")
    require(central_gradients(local_case(disabled, 1, 0))[5] == Fraction(-1, 648),
            "CONTROL")
    controls.add("feedback_disabled")

    first_only = history("0011", 0, stop=3, feedback_mode="first")
    require(first_only[2][3] == Fraction(1, 648), "CONTROL")
    continued = sources[3] - first_only[2][3]
    require(continued == Fraction(71, 68024448), "CONTROL")
    controls.add("feedback_first_only")

    field_disabled = history("0011", 0, stop=3, metric_coupling=0)
    require(field_disabled[1] == free[:4], "CONTROL")
    require(central_gradients(local_case(field_disabled, 2, 0))[:5]
            == tuple(Fraction(value, 68024448) for value in DIPOLE), "CONTROL")
    controls.add("metric_coupling_disabled")

    reversed_feedback = history("0011", 0, stop=3, feedback_mode="reversed")
    require(central_gradients(local_case(reversed_feedback, 1, 0))[5]
            == Fraction(-1, 324), "CONTROL")
    controls.add("feedback_sign_reversed")

    omitted_h = next_core(cores[1], 0, move_hermitian=False)
    require(omitted_h[2] == 1 and omitted_h[4][5] == 0, "CONTROL")
    require(omitted_h[4][5] != omitted_h[2], "CONTROL")
    controls.add("hermitian_transport_omitted")

    recovered = older_numerators(cores[2], 0)
    require(recovered is not None and all(value.denominator == 1 for value in recovered),
            "CONTROL")
    # Replacing the true first divisor m by m^2 divides each exact recovery by m.
    wrong_recovered = tuple(value / M for value in recovered)
    require(any(value.denominator != 1 for value in wrong_recovered), "CONTROL")
    require(previous_core(cores[2], 0) == cores[1], "CONTROL")
    controls.add("wrong_first_inverse_divisor")

    degenerate = ((2, 0, 0, 0, 0), (0, 0, 0, 0, 0), 0, 0, D_H, 1)
    require(core_member(degenerate), "CONTROL")
    bad = decode(degenerate)[0][0]
    require((-1, 1 + bad, 1 - bad, 1) == (-1, 2, 0, 1)
            and bad * bad - 1 == 0, "CONTROL")
    controls.add("unrestricted_metric_degeneracy")
    require(len(controls) == 7, "CERTIFICATE")
    return direct_contrast, sources[2], reciprocal_contrast, continued, sharp


def check_cycles(histories):
    periods = []
    for word, a in (("0010", -1), ("0010", 1), ("0011", 0)):
        cores = histories[word, a][3]
        start_core = cores[1]
        for target in (1, 2, 3):
            ceiling = max(core_energy(cores[n]) for n in range(1, target + 1))
            bank = ceiling - core_energy(start_core)
            require(bank >= 0 and core_energy(cores[target + 1]) > ceiling, "SHARP_BUDGET")
            start = (start_core, bank, 1)
            state = start
            seen = {start}
            highest_counter = 1
            first_return = None
            for tick in range(1, 2 * target + 1):
                state = funded_step(state, a)
                require(state_member(state), "PERIOD")
                require(core_energy(state[0]) + state[1] == ceiling, "CONSERVATION")
                highest_counter = max(highest_counter, state[0][5])
                if state == start:
                    first_return = tick
                    break
                require(state not in seen, "PERIOD")
                seen.add(state)
            require(first_return == 2 * target and len(seen) == first_return
                    and highest_counter == target, "PERIOD")
            periods.append(first_return)
    require(tuple(periods) == (2, 4, 6, 2, 4, 6, 2, 4, 6), "CERTIFICATE")
    return tuple(periods)


def comma(values):
    return ",".join(str(value) for value in values)


def certificate_bytes():
    authority_count = check_authority()
    check_initial_data_and_ring()
    fixtures = hermitian_fixtures()
    transports, holonomies = check_transports(fixtures)
    cores, funded, defects = check_core_and_funding(fixtures)
    records, history_hash, joint_variations, histories = check_histories()
    offshell_variations = check_offshell(histories)
    direct, source2, reciprocal, continued, first_bank = check_witnesses_and_controls(histories)
    periods = check_cycles(histories)
    lines = (
        "CERTIFICATE=" + PROBE_ID,
        "AUTHORITY_FILES=" + str(authority_count),
        "TRANSPORT_CHECKS=" + str(transports),
        "HOLONOMY_CHECKS=" + str(holonomies),
        "CORE_FIXTURES=" + str(cores),
        "FUNDED_CASES=" + str(funded),
        "IMAGE_DEFECTS=" + str(defects),
        "HISTORY_RECORDS=" + str(records),
        "HISTORY_SHA256=" + history_hash,
        "JOINT_VARIATIONS=" + str(joint_variations),
        "OFFSHELL_VARIATIONS=" + str(offshell_variations),
        "DIRECT_CONTRAST=" + comma(direct),
        "ZERO_SOURCE_CHI2=" + str(source2),
        "RECIPROCAL_CONTRAST=" + comma(reciprocal),
        "CONTINUED_SOURCE_CONTRAST=" + str(continued),
        "ZERO_SOURCE_FIRST_BANK=" + str(first_bank),
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
