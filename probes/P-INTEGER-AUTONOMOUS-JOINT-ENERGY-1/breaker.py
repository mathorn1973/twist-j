#!/usr/bin/env python3
"""Independent rational/direct-coordinate audit of the autonomous joint law.

Written from this probe's PREREG.md without reading its primary or PROOF.md.
Direct Hermitian formulas are adapted from the completed independent breaker
of P-INTEGER-JOINT-VARIATION-1; the new dynamics and checks follow this contract.
The primary and breaker share the specification and assisted-session context.
This is implementation independence, not a claim of an independent laboratory.

Do not execute or import before the complete public prospective pin is read
back. The program uses only exact integers and Fraction arithmetic. It neither
imports the primary nor reads expected output, proof, or source-manifest files.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import lcm
from pathlib import Path
import sys


PROBE = "P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1"
M = 324
G = F(1, 324)
ELL = (1, -1, 0, 0, 0)
H_ZERO = (0, 0, 0, 0, 0, 0, 0, 0)
H_REFERENCE = (0, 0, 1, 0, 0, 0, 0, 0)
DELTA = F(253, 8684010)

# Each row is (word, canonical numerator at 0, canonical numerator at 1,
# canonical first bond energy, initial canonical dipole).
INITIAL = (
    ("0010", (0, 1, 1, 0, 0), (1, 1, 0, 0, 0), F(713, 2592), F(-1, 2)),
    ("0011", (0, 1, 1, 0, 0), (0, 1, 1, 0, 0), F(53, 432), F(-1, 2)),
    ("0100", (1, 1, 0, 0, 0), (1, 0, 0, 0, 1), F(713, 2592), F(0)),
    ("0101", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), F(53, 432), F(0)),
    ("0110", (0, 1, 1, 0, 0), (1, 0, 0, 0, 1), F(67, 162), F(-1, 2)),
    ("1001", (1, 0, 0, 0, 1), (0, 1, 1, 0, 0), F(67, 162), F(1, 2)),
    ("1010", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), F(53, 432), F(0)),
    ("1011", (1, 1, 0, 0, 0), (0, 1, 1, 0, 0), F(713, 2592), F(0)),
    ("1100", (1, 0, 0, 0, 1), (1, 0, 0, 0, 1), F(53, 432), F(1, 2)),
    ("1101", (1, 0, 0, 0, 1), (1, 1, 0, 0, 0), F(713, 2592), F(1, 2)),
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

FALSIFIERS = frozenset((
    "AUTHORITY", "RING", "TRANSPORT", "HOLONOMY", "COST", "INITIAL_DATA",
    "INTEGER", "BARE_INVERSE", "FUNDED_INVERSE", "CONSERVATION", "BRANCH",
    "IMAGE_GUARD", "RECURRENCE", "MEAN", "SOURCE_READER", "LORENTZ",
    "SOURCE_BOUND", "EQUILIBRIUM", "ENERGY", "PRECISION", "GRAM", "ACTION",
    "OFFSHELL_ACTION", "CANONICAL", "SYMPLECTIC", "FIXED_COUNTER", "CONTROL",
    "SHARP_BUDGET", "PERIOD", "CERTIFICATE", "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    def __init__(self, key):
        if key not in FALSIFIERS:
            raise ValueError("unregistered falsifier key")
        self.key = key
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def square_norm(vector):
    return sum(value * value for value in vector)


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def times(factor, vector):
    return tuple(factor * value for value in vector)


def unit(size, site):
    return tuple(F(int(index == site)) for index in range(size))


def integer_tuple(value, size):
    return (isinstance(value, tuple) and len(value) == size
            and all(type(entry) is int for entry in value))


def laplacian(field):
    return tuple(F(188 * field[r]
                   - 29 * (field[(r - 1) % 5] + field[(r + 1) % 5])
                   - 65 * (field[(r - 2) % 5] + field[(r + 2) % 5]), M)
                 for r in range(5))


def edge_form(left, right):
    """The spatial quadratic form from weighted edge differences."""
    total = F(0)
    for site in range(5):
        for offset, weight in ((1, 29), (2, 65)):
            neighbor = (site + offset) % 5
            total += weight * (left[site] - left[neighbor]) * (right[site] - right[neighbor])
    return total / M


def stiffness(vector):
    field, source = vector[:5], vector[5]
    return tuple(value - G * source * dipole
                 for value, dipole in zip(laplacian(field), ELL)) + (
                     source - G * dot(ELL, field),)


def stiffness_form(left, right):
    return (edge_form(left[:5], right[:5]) + left[5] * right[5]
            - G * (left[5] * dot(ELL, right[:5]) + right[5] * dot(ELL, left[:5])))


def equilibrium(a):
    force = F(a, 4)
    field = tuple(F(1, 5) + force * entry / 8683757
                  for entry in (40986, -40986, 5832, 0, -5832))
    source = force * F(8684010, 8683757)
    return field + (source,)


def centered(physical, a):
    return subtract(physical, equilibrium(a))


def total_bond(previous, current, a):
    older = centered(previous, a)
    now = centered(current, a)
    return (F(square_norm(subtract(now, older)), 2)
            + stiffness_form(older, now) / 2)


def component_bonds(previous, current):
    """Uncentered three-term decomposition, used only in context a=0."""
    h_old, c_old = previous[:5], previous[5]
    h_now, c_now = current[:5], current[5]
    field = F(square_norm(subtract(h_now, h_old)), 2) + edge_form(h_old, h_now) / 2
    source = F((c_now - c_old) ** 2, 2) + c_old * c_now / 2
    interaction = -G * (c_old * dot(ELL, h_now) + c_now * dot(ELL, h_old)) / 2
    return field, source, interaction


def real_product(left, right):
    a, b = left
    c, d = right
    return a * c + b * d, a * d + b * c + b * d


def off_diagonal_norm(c):
    c0, c1, c2, c3 = c
    adjacent = c0 * c1 + c1 * c2 + c2 * c3
    other = c0 * c2 + c0 * c3 + c1 * c3
    return square_norm(c) - adjacent, adjacent - other


def times_j(c):
    c0, c1, c2, c3 = c
    return -c3, c0 - c3, c1 - c3, c2 - c3


def times_j_inverse(c):
    c0, c1, c2, c3 = c
    return c1 - c0, c2 - c0, c3 - c0, -c0


def hermitian_a(h):
    a0, a1, d0, d1 = h[:4]
    return (2 * a0 - a1, -a0 + a1, d0 + d1, d0 + 2 * d1,
            *times_j(h[4:]))


def hermitian_a_inverse(h):
    a0, a1, d0, d1 = h[:4]
    return (a0 + a1, a0 + 2 * a1, 2 * d0 - d1, -d0 + d1,
            *times_j_inverse(h[4:]))


def hermitian_b(h, t):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    return (a0 + t * (2 * c0 - c1) + t * t * d0,
            a1 + t * (c1 - c2 - c3) + t * t * d1,
            d0, d1, c0 + t * d0, c1, c2 - t * d1, c3 - t * d1)


def hermitian_loop(h, t):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    cross0 = -5 * c0 + 5 * c1 - 3 * c2 + c3
    cross1 = 2 * c0 - 3 * c1 + 3 * c2
    return (a0 + t * cross0 + t * t * (9 * d0 - 5 * d1),
            a1 + t * cross1 + t * t * (-5 * d0 + 4 * d1),
            d0, d1,
            c0 + t * (-2 * d0 + d1), c1 + t * d0,
            c2 + t * (-d0 + 2 * d1), c3 + t * d1)


def monitor(y):
    return 9 * y * y, -5 * y * y, 1, 0, -2 * y, y, -y, 0


def hermitian_cost(h):
    a0, a1, d0, d1 = h[:4]
    return (4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
            + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
            + 10 * square_norm(h[4:]) - 2 * sum(h[4:]) ** 2)


def trace_cost(h):
    aa = real_product(h[:2], h[:2])
    dd = real_product(h[2:4], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return 4 * (aa[0] + dd[0] + 2 * cc[0]) + 2 * (aa[1] + dd[1] + 2 * cc[1])


def hermitian_determinant(h):
    ad = real_product(h[:2], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return ad[0] - cc[0], ad[1] - cc[1]


def core_member(core):
    if not isinstance(core, tuple) or len(core) != 4:
        return False
    z, r, d, h = core
    return (integer_tuple(z, 6) and integer_tuple(r, 6)
            and type(d) is int and d >= 1 and integer_tuple(h, 8))


def state_member(state):
    return (isinstance(state, tuple) and len(state) == 3 and core_member(state[0])
            and type(state[1]) is int and state[1] >= 0
            and type(state[2]) is int and state[2] in (-1, 1))


def decode(core):
    z, r, d, _ = core
    return (tuple(F(value, d) for value in z),
            tuple(F(value, d) for value in r))


def encode(values, denominator):
    scaled = tuple(value * denominator for value in values)
    require(all(isinstance(value, F) and value.denominator == 1 for value in scaled), "INTEGER")
    return tuple(value.numerator for value in scaled)


def forward(core, a, field_coupling=1, feedback=1, move_monitor=True):
    """Autonomous rational update, with separately labelled control switches."""
    old_z, _, d, h = core
    current, previous = decode(core)
    spatial = laplacian(current[:5])
    field = tuple(2 * current[r] - previous[r] - spatial[r]
                  + field_coupling * G * current[5] * ELL[r] for r in range(5))
    source = current[5] - previous[5] + F(a, 4) + feedback * G * dot(ELL, current[:5])
    next_d = M * d
    next_z = encode(field + (source,), next_d)
    next_r = encode(current, next_d)
    next_h = hermitian_loop(h, next_z[5] - old_z[5]) if move_monitor else h
    return next_z, next_r, next_d, next_h


def backward(core, a):
    """Outer image guards plus rational reconstruction of the older slice."""
    z, r, d, h = core
    if d % M or any(value % M for value in r):
        return None
    previous_d = d // M
    current, previous = decode(core)
    spatial = laplacian(previous[:5])
    older_field = tuple(2 * previous[site] - current[site] - spatial[site]
                        + G * previous[5] * ELL[site] for site in range(5))
    older_source = previous[5] - current[5] + F(a, 4) + G * dot(ELL, previous[:5])
    older_scaled = tuple(value * previous_d for value in older_field + (older_source,))
    if any(value.denominator != 1 for value in older_scaled):
        return None
    previous_z = tuple(value // M for value in r)
    previous_r = tuple(value.numerator for value in older_scaled)
    previous_h = hermitian_loop(h, previous_z[5] - z[5])
    return previous_z, previous_r, previous_d, previous_h


def account(core):
    z, r, d, h = core
    return 1 + d + square_norm(z) + square_norm(r) + hermitian_cost(h)


def core_bond(core, a):
    current, previous = decode(core)
    return total_bond(previous, current, a)


def reverse(state):
    return state[0], state[1], -state[2]


def funded(state, a):
    core, bank, direction = state
    if direction == 1:
        destination = forward(core, a)
    elif direction == -1:
        destination = backward(core, a)
    else:
        raise ValueError("direction outside carrier")
    ceiling = account(core) + bank
    if destination is None or account(destination) > ceiling:
        return reverse(state)
    return destination, ceiling - account(destination), direction


def inverse_funded(state, a):
    return reverse(funded(reverse(state), a))


def initial_row(word):
    for row in INITIAL:
        if row[0] == word:
            return row
    raise ValueError("word outside declared prepared family")


def prepared_core(word, a):
    _, first, second, _, _ = initial_row(word)
    z = tuple(6 + 5 * entry for entry in second) + (10 * a,)
    r = tuple(6 + 5 * entry for entry in first) + (0,)
    return z, r, 40, monitor(10 * a)


def check_authority():
    repository = Path(__file__).resolve().parents[2]
    for name, size, digest in AUTHORITY:
        data = (repository / "canon" / name).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest, "AUTHORITY")
    require(len(AUTHORITY) == 5, "CERTIFICATE")
    return len(AUTHORITY)


def check_initial_and_ring():
    labels = ("0010", "0011", "0100", "0101", "0110",
              "1001", "1010", "1011", "1100", "1101")
    require(tuple(row[0] for row in INITIAL) == labels, "INITIAL_DATA")
    for word, first, second, expected_energy, expected_dipole in INITIAL:
        bits = tuple(int(bit) for bit in word)
        for n, literal in enumerate((first, second)):
            site = bits[n + 2] - bits[n]
            expected = tuple(int((r - site) % 5 in (0, 1)) for r in range(5))
            require(literal == expected, "INITIAL_DATA")
        h0 = tuple(F(value, 2) for value in first)
        h1 = tuple(F(value, 2) for value in second)
        energy = F(square_norm(subtract(h1, h0)), 2) + edge_form(h0, h1) / 2
        require(energy == expected_energy and dot(ELL, h0) == expected_dipole, "INITIAL_DATA")
        for a in (-1, 0, 1):
            core = prepared_core(word, a)
            current, previous = decode(core)
            require(core_member(core) and sum(current[:5]) == sum(previous[:5]) == 1,
                    "INITIAL_DATA")
            require(current[:5] == tuple(F(1, 5) + (value - F(1, 5)) / 4 for value in h1)
                    and previous[:5] == tuple(F(1, 5) + (value - F(1, 5)) / 4 for value in h0)
                    and current[5] == F(a, 4) and previous[5] == 0, "INITIAL_DATA")
    require(real_product((0, 1), (0, 1)) == (1, 1), "RING")
    require(real_product((0, 1), (-1, 1)) == (1, 0), "RING")
    for index in range(4):
        basis = tuple(int(site == index) for site in range(4))
        image = basis
        orbit = []
        for _ in range(5):
            orbit.append(image)
            require(times_j_inverse(times_j(image)) == image, "RING")
            image = times_j(image)
        require(image == basis and tuple(sum(row[r] for row in orbit) for r in range(4))
                == (0, 0, 0, 0), "RING")


def hermitian_fixtures():
    fixtures = [H_ZERO]
    for index in range(8):
        basis = tuple(int(site == index) for site in range(8))
        fixtures.extend((basis, tuple(-value for value in basis)))
    fixtures.extend(((1, -1, 2, 0, -2, 1, 0, 1),
                     (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(fixtures) == 19, "CERTIFICATE")
    return tuple(fixtures)


def check_h_cost(h):
    require(integer_tuple(h, 8), "TRANSPORT")
    value = hermitian_cost(h)
    require(value == trace_cost(h) and value >= 2 * square_norm(h)
            and (value == 0) == (h == H_ZERO), "COST")


def check_transports(fixtures):
    transports = holonomies = 0
    for h in fixtures:
        check_h_cost(h)
        for image, inverse in ((hermitian_a(h), hermitian_a_inverse),
                               (hermitian_a_inverse(h), hermitian_a)):
            check_h_cost(image)
            require(inverse(image) == h and hermitian_determinant(image) == hermitian_determinant(h),
                    "TRANSPORT")
            transports += 1
        for t in (-2, -1, 0, 1, 2):
            image = hermitian_b(h, t)
            check_h_cost(image)
            require(hermitian_b(image, -t) == h
                    and hermitian_determinant(image) == hermitian_determinant(h), "TRANSPORT")
            transports += 1
            direct = hermitian_loop(h, t)
            factored = hermitian_a(hermitian_b(hermitian_a_inverse(hermitian_b(h, -t)), t))
            require(direct == factored and hermitian_loop(direct, -t) == h
                    and hermitian_determinant(direct) == hermitian_determinant(h), "HOLONOMY")
            check_h_cost(direct)
            holonomies += 1
    require((transports, holonomies) == (133, 95), "CERTIFICATE")
    return transports, holonomies


def check_funded_case(state, a, branches):
    require(state_member(state), "INTEGER")
    core, bank, direction = state
    out = funded(state, a)
    require(state_member(out), "INTEGER")
    require(inverse_funded(out, a) == state and funded(inverse_funded(state, a), a) == state,
            "FUNDED_INVERSE")
    require(account(out[0]) + out[1] == account(core) + bank, "CONSERVATION")
    require(core_bond(out[0], a) == core_bond(core, a), "ENERGY")
    target = forward(core, a) if direction == 1 else backward(core, a)
    label = "forward" if direction == 1 else "backward"
    if target is None:
        branches.add(label + "_domain")
        expected = reverse(state)
    elif account(target) > account(core) + bank:
        branches.add(label + "_bank")
        expected = reverse(state)
    else:
        branches.add(label + "_move")
        expected = target, account(core) + bank - account(target), direction
    require(out == expected, "BRANCH")


def check_core_and_funding(fixtures):
    base = []
    for a in (-1, 0, 1):
        for i in range(19):
            for d in (1, 2, 40):
                z = (i - 9, 1, -2, 0, 3, i % 5 - 2)
                r = (2, -1, 0, 1, 9 - i, (i // 5) % 5 - 2)
                base.append((a, (z, r, d, fixtures[i])))
    require(len(base) == 171, "CERTIFICATE")
    decrease = ((0, 0, 0, 0, 0, 100), (0, 0, 0, 0, 0, 100), 1, monitor(100))
    require(account(forward(decrease, 0)) < account(decrease), "BRANCH")
    entries = base + [(0, decrease)]
    core_count = funded_count = 0
    branches = set()
    for a, core in entries:
        image = forward(core, a)
        require(core_member(core) and core_member(image), "INTEGER")
        require(image[2] == M * core[2] and backward(image, a) == core, "BARE_INVERSE")
        predecessor = backward(core, a)
        if predecessor is not None:
            require(forward(predecessor, a) == core, "BARE_INVERSE")
        require(core_bond(image, a) == core_bond(core, a), "ENERGY")
        core_count += 1
        for candidate in (core, image):
            increase = account(forward(candidate, a)) - account(candidate)
            banks = (0, 1, 772, max(0, increase - 1), max(0, increase), max(0, increase + 1))
            for bank in banks:
                for direction in (-1, 1):
                    check_funded_case((candidate, bank, direction), a, branches)
                    funded_count += 1
    require((core_count, funded_count) == (172, 4128), "CERTIFICATE")
    require(branches == {"forward_move", "backward_move", "forward_bank", "backward_bank",
                         "backward_domain"}, "BRANCH")
    image_defects = 0
    for a, core in base:
        require(backward(core, a) is None, "IMAGE_GUARD")
        require(funded((core, 1000000000, -1), a) == (core, 1000000000, 1), "IMAGE_GUARD")
        z, r, d, h = forward(core, a)
        for entry in range(13):
            corrupt_d = d + int(entry == 0)
            corrupt_r = tuple(value + int(entry == site + 1) for site, value in enumerate(r))
            corrupt_z = tuple(value + int(entry == site + 7) for site, value in enumerate(z))
            corrupt = corrupt_z, corrupt_r, corrupt_d, h
            require(core_member(corrupt) and backward(corrupt, a) is None, "IMAGE_GUARD")
            require(funded((corrupt, 1000000000, -1), a) == (corrupt, 1000000000, 1), "IMAGE_GUARD")
            image_defects += 1
    require(image_defects == 2223, "CERTIFICATE")
    return core_count, funded_count, image_defects


def transpose(matrix):
    return tuple(tuple(row[column] for row in matrix) for column in range(len(matrix[0])))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(dot(row, column) for column in columns) for row in left)


def matrix_vector(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def identity(size):
    return tuple(unit(size, index) for index in range(size))


def determinant(matrix):
    rows = [list(map(F, row)) for row in matrix]
    answer = F(1)
    for column in range(len(rows)):
        pivot = next((r for r in range(column, len(rows)) if rows[r][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            answer = -answer
        value = rows[column][column]
        answer *= value
        for r in range(column + 1, len(rows)):
            factor = rows[r][column] / value
            for c in range(column, len(rows)):
                rows[r][c] -= factor * rows[column][c]
    return answer


def solve(matrix, rhs):
    rows = [list(map(F, row)) + [F(value)] for row, value in zip(matrix, rhs)]
    size = len(rows)
    for column in range(size):
        pivot = next((r for r in range(column, size) if rows[r][column]), None)
        require(pivot is not None, "EQUILIBRIUM")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        value = rows[column][column]
        rows[column] = [entry / value for entry in rows[column]]
        for r in range(size):
            if r == column:
                continue
            factor = rows[r][column]
            rows[r] = [entry - factor * basis for entry, basis in zip(rows[r], rows[column])]
    return tuple(row[-1] for row in rows)


def matrices_and_equilibrium():
    kmat = transpose(tuple(stiffness(unit(6, site)) for site in range(6)))
    eye = identity(6)
    require(kmat == transpose(kmat), "GRAM")
    columns = tuple(subtract(unit(6, site), unit(6, 4)) for site in range(4)) + (unit(6, 5),)
    umat = transpose(columns)
    gram_k = multiply(multiply(transpose(umat), kmat), umat)
    inverse_dipole = times(F(324, 53605), (253, -253, 36, 0, -36))
    require(sum(inverse_dipole) == 0 and laplacian(inverse_dipole) == ELL, "EQUILIBRIUM")
    require(dot(ELL, inverse_dipole) == F(163944, 53605)
            and G * G * dot(ELL, inverse_dipole) == DELTA, "EQUILIBRIUM")
    for a in (-1, 0, 1):
        force = (F(0),) * 5 + (F(a, 4),)
        coordinates = solve(gram_k, matrix_vector(transpose(umat), force))
        derived = matrix_vector(umat, coordinates)
        expected = subtract(equilibrium(a), (F(1, 5),) * 5 + (F(0),))
        require(derived == expected and matrix_vector(kmat, derived) == force,
                "EQUILIBRIUM")
        eq = equilibrium(a)
        require(sum(eq[:5]) == 1 and laplacian(eq[:5]) == times(G * eq[5], ELL)
                and eq[5] == F(a, 4) + G * dot(ELL, eq[:5]), "EQUILIBRIUM")
    ksquare = multiply(kmat, kmat)
    forms = (
        tuple(tuple(kmat[i][j] - F(59, 100) * eye[i][j] for j in range(6)) for i in range(6)),
        tuple(tuple(F(201, 200) * eye[i][j] - kmat[i][j] for j in range(6)) for i in range(6)),
        tuple(tuple(kmat[i][j] - ksquare[i][j] / 4 - eye[i][j] / 2
                    for j in range(6)) for i in range(6)),
    )
    count = 0
    for form in forms:
        gram = multiply(multiply(transpose(umat), form), umat)
        require(gram == transpose(gram), "GRAM")
        for size in range(1, 6):
            leading = tuple(row[:size] for row in gram[:size])
            require(determinant(leading) > 0, "GRAM")
            count += 1
    require(count == 15, "CERTIFICATE")
    return kmat, count


def history(word, a, stop=12, field_coupling=1, feedback_mode="all"):
    core = prepared_core(word, a)
    current, previous = decode(core)
    cores = {1: core}
    values = [previous, current]
    rows = [(core[1][:5], 0, 40, H_REFERENCE),
            (core[0][:5], core[0][5], 40, core[3])]
    for n in range(1, stop):
        if feedback_mode == "all":
            feedback = 1
        elif feedback_mode == "none":
            feedback = 0
        elif feedback_mode == "first":
            feedback = int(n == 1)
        elif feedback_mode == "reversed":
            feedback = -1
        else:
            raise ValueError("unknown feedback comparison")
        core = forward(core, a, field_coupling=field_coupling, feedback=feedback)
        require(core_member(core), "INTEGER")
        cores[n + 1] = core
        current, _ = decode(core)
        values.append(current)
        rows.append((core[0][:5], core[0][5], core[2], core[3]))
    return rows, values, cores


def free_history(word, a, stop=12):
    current, previous = decode(prepared_core(word, a))
    values = [previous, current]
    for n in range(1, stop):
        old, now = values[n - 1], values[n]
        spatial = laplacian(now[:5])
        field = tuple(2 * now[site] - old[site] - spatial[site] for site in range(5))
        source = now[5] - old[5] + F(a, 4)
        values.append(field + (source,))
    return values


def local_action(v, xi, hp, hn, cp, cn, a):
    kinetic_h = F(square_norm(subtract(v, hp)) + square_norm(subtract(hn, v)), 2)
    kinetic_c = F((xi - cp) ** 2 + (cn - xi) ** 2, 2)
    return (kinetic_h - edge_form(v, v) / 2 + kinetic_c - xi * xi / 2
            + F(a, 4) * xi + G * xi * dot(ELL, v))


def central_gradients(case):
    v, xi, hp, hn, cp, cn, a = case
    answer = []
    for site in range(5):
        e = unit(5, site)
        answer.append((local_action(add(v, e), xi, hp, hn, cp, cn, a)
                       - local_action(subtract(v, e), xi, hp, hn, cp, cn, a)) / 2)
    answer.append((local_action(v, xi + 1, hp, hn, cp, cn, a)
                   - local_action(v, xi - 1, hp, hn, cp, cn, a)) / 2)
    return tuple(answer)


def formula_gradients(case):
    v, xi, hp, hn, cp, cn, a = case
    metric = tuple(2 * now - past - future - spatial + G * xi * dipole
                   for now, past, future, spatial, dipole in zip(v, hp, hn, laplacian(v), ELL))
    source = xi - cp - cn + F(a, 4) + G * dot(ELL, v)
    return metric + (source,)


def local_case(values, n, a):
    return (values[n][:5], values[n][5], values[n - 1][:5], values[n + 1][:5],
            values[n - 1][5], values[n + 1][5], a)


def valuation3(value):
    require(type(value) is int and value > 0, "PRECISION")
    exponent = 0
    while value % 3 == 0:
        value //= 3
        exponent += 1
    return exponent


def check_histories():
    digest = sha256()
    records = variations = bonds = precision = 0
    histories = {}
    for word, _, _, canonical_energy, initial_dipole in INITIAL:
        for a in (-1, 0, 1):
            data = history(word, a)
            histories[word, a] = data
            rows, values, cores = data
            require(len(rows) == len(values) == 13, "CERTIFICATE")
            first_bond = total_bond(values[0], values[1], a)
            initial_formula = (canonical_energy / 16 - G * F(a, 32) * initial_dipole
                               + F(a * a, 32) / (1 - DELTA))
            require(first_bond == initial_formula, "ENERGY")
            for n, (p, y, denominator, h) in enumerate(rows):
                now = values[n]
                require(integer_tuple(p, 5) and type(y) is int and integer_tuple(h, 8), "INTEGER")
                require(denominator == (40 if n == 0 else 40 * M ** (n - 1)), "INTEGER")
                require(tuple(F(entry, denominator) for entry in p) + (F(y, denominator),) == now,
                        "INTEGER")
                require(sum(p) == denominator and sum(now[:5]) == 1, "MEAN")
                require(h == monitor(y) and F(h[5], denominator) == now[5]
                        and hermitian_determinant(h) == (0, 0), "SOURCE_READER")
                check_h_cost(h)
                require(hermitian_cost(h) == 294 * y ** 4 + 52 * y * y + 4, "COST")
                require(abs(now[5]) < F(3, 4), "SOURCE_BOUND")
                for field_value in now[:5]:
                    require(abs(field_value - F(1, 5)) < F(9, 20)
                            and F(-1, 4) < field_value < F(13, 20)
                            and field_value * field_value - 1 < F(-231, 400), "LORENTZ")
                if n >= 1:
                    require(core_member(cores[n]) and decode(cores[n])[1] == values[n - 1], "INTEGER")
                    require(5 * account(cores[n]) >= denominator * denominator, "COST")
                    joint_denominator = lcm(*(entry.denominator for entry in now))
                    require(valuation3(joint_denominator) == 4 * (n - 1), "PRECISION")
                    precision += 1
                    observed_bond = total_bond(values[n - 1], now, a)
                    require(observed_bond == first_bond and 0 < observed_bond < F(3, 50), "ENERGY")
                    z_old, z_now = centered(values[n - 1], a), centered(now, a)
                    u = subtract(z_now, z_old)
                    v = times(F(1, 2), add(z_now, z_old))
                    square_form = (F(square_norm(u), 2) - stiffness_form(u, u) / 8
                                   + stiffness_form(v, v) / 2)
                    completed = subtract(z_old, subtract(z_now, times(F(1, 2), stiffness(z_now))))
                    completed_form = (F(square_norm(completed), 2)
                                      + stiffness_form(z_now, z_now) / 2
                                      - square_norm(stiffness(z_now)) / 8)
                    require(observed_bond == square_form == completed_form, "ENERGY")
                    bonds += 1
                line = (word + "|" + str(a) + "|" + str(n) + "|" + comma(p) + "|" + str(y)
                        + "|" + str(denominator) + "|" + comma(h) + "\n")
                digest.update(line.encode("ascii"))
                records += 1
            for n in range(1, 12):
                old, now, future = values[n - 1], values[n], values[n + 1]
                spatial = laplacian(now[:5])
                field_residual = tuple(future[r] - 2 * now[r] + old[r] + spatial[r]
                                       - G * now[5] * ELL[r] for r in range(5))
                source_residual = future[5] - now[5] + old[5] - F(a, 4) - G * dot(ELL, now[:5])
                require(field_residual == (0,) * 5 and source_residual == 0, "RECURRENCE")
            for n in (1, 2, 5, 11):
                require(central_gradients(local_case(values, n, a)) == (0,) * 6, "ACTION")
                variations += 6
    require((records, variations, bonds, precision) == (390, 720, 360, 360), "CERTIFICATE")
    return records, digest.hexdigest(), variations, bonds, precision, histories


def check_offshell(histories):
    values = histories["0011", 0][1]
    v, xi, hp, hn, cp, cn, a = local_case(values, 2, 0)
    cases = (
        (add(v, unit(5, 0)), xi, hp, hn, cp, cn, a),
        (v, xi + 1, hp, hn, cp, cn, a),
        (v, xi, hp, hn, cp, cn + 1, a),
        (v, xi, hp, add(hn, unit(5, 2)), cp, cn, a),
        (v, xi, hp, hn, cp - 1, cn, a),
        ((F(1, 3), F(-2, 5), F(0), F(3, 7), F(-1)), F(-2, 3),
         (F(0),) * 5, (F(1),) * 5, F(1, 2), F(-3, 4), 1),
    )
    count = 0
    for case in cases:
        observed = central_gradients(case)
        expected = formula_gradients(case)
        require(observed == expected and any(entry != 0 for entry in observed), "OFFSHELL_ACTION")
        count += len(observed)
    require(count == 36, "CERTIFICATE")
    return count


def generating_function(position, momentum_new):
    return dot(position, momentum_new) + F(square_norm(momentum_new), 2) + stiffness_form(position, position) / 2


def generating_gradients(position, momentum_new):
    position_gradient = []
    momentum_gradient = []
    for site in range(6):
        basis = unit(6, site)
        position_gradient.append((generating_function(add(position, basis), momentum_new)
                                  - generating_function(subtract(position, basis), momentum_new)) / 2)
        momentum_gradient.append((generating_function(position, add(momentum_new, basis))
                                  - generating_function(position, subtract(momentum_new, basis))) / 2)
    return tuple(position_gradient), tuple(momentum_gradient)


def wronskian(older1, current1, older2, current2):
    return dot(older1, current2) - dot(current1, older2)


def check_canonical_and_symplectic(histories, kmat):
    eye = identity(6)
    transition = tuple(tuple(2 * eye[i][j] - kmat[i][j] for j in range(6))
                       + tuple(-entry for entry in eye[i]) for i in range(6))
    transition += tuple(eye[i] + (F(0),) * 6 for i in range(6))
    alternating = tuple((F(0),) * 6 + tuple(-entry for entry in eye[i]) for i in range(6))
    alternating += tuple(eye[i] + (F(0),) * 6 for i in range(6))
    require(multiply(multiply(transpose(transition), alternating), transition) == alternating, "SYMPLECTIC")
    step_count = 0
    for word, _, _, _, _ in INITIAL:
        for a in (-1, 0, 1):
            values = histories[word, a][1]
            for n in range(1, 12):
                old, now, future = (centered(values[t], a) for t in (n - 1, n, n + 1))
                p_old = subtract(now, old)
                p_new = subtract(future, now)
                require(p_new == subtract(p_old, stiffness(now)) and future == add(now, p_new), "CANONICAL")
                dz, dp = generating_gradients(now, p_new)
                require(dz == p_old and dp == future, "CANONICAL")
                require(matrix_vector(transition, now + old) == future + now, "CANONICAL")
                step_count += 1
    require(step_count == 330, "CERTIFICATE")
    symplectic_count = 0
    for a in (-1, 0, 1):
        for i in range(len(INITIAL)):
            first = tuple(centered(value, a) for value in histories[INITIAL[i][0], a][1])
            for j in range(i + 1, len(INITIAL)):
                second = tuple(centered(value, a) for value in histories[INITIAL[j][0], a][1])
                reference = wronskian(first[0], first[1], second[0], second[1])
                for n in range(1, 13):
                    require(wronskian(first[n - 1], first[n], second[n - 1], second[n]) == reference,
                            "SYMPLECTIC")
                    symplectic_count += 1
    require(symplectic_count == 1620, "CERTIFICATE")
    first = histories["0010", 1][1]
    second = histories["0011", 1][1]
    raw2 = wronskian(first[1], first[2], second[1], second[2])
    raw3 = wronskian(first[2], first[3], second[2], second[3])
    drift = raw3 - raw2
    require(drift == F(1, 4) * (first[2][5] - second[2][5]) == F(1, 10368), "CONTROL")
    return step_count, symplectic_count, drift


def check_witnesses_and_controls(histories):
    negative = histories["0010", -1]
    positive = histories["0010", 1]
    require(negative[0][2][:3] == ((4379, 2779, 794, 2594, 2414), -6480, 12960)
            and positive[0][2][:3] == ((4399, 2759, 794, 2594, 2414), 6480, 12960), "FIXED_COUNTER")
    direct = subtract(positive[1][2][:5], negative[1][2][:5])
    require(direct == times(F(1, 648), ELL), "FIXED_COUNTER")
    rows, values, cores = histories["0011", 0]
    require(rows[1][:3] == ((6, 11, 11, 6, 6), 0, 40), "FIXED_COUNTER")
    require(rows[2][:3] == ((2414, 2769, 2769, 2414, 2594), -5, 12960), "FIXED_COUNTER")
    require(rows[3][:3] == ((973001, 594836, 594831, 973006, 1063366), -1975, 4199040), "FIXED_COUNTER")
    free = free_history("0011", 0)
    reciprocal = subtract(values[3][:5], free[3][:5])
    require(values[2][5] == F(-1, 2592) and values[2][:5] == free[2][:5]
            and reciprocal == times(F(-1, 839808), ELL), "FIXED_COUNTER")
    first_components = component_bonds(values[0], values[1])
    second_components = component_bonds(values[1], values[2])
    third_components = component_bonds(values[2], values[3])
    total = total_bond(values[0], values[1], 0)
    exchange = subtract(second_components, first_components)
    require(total == F(53, 6912) and sum(first_components) == sum(second_components)
            == sum(third_components) == total, "ENERGY")
    require(exchange == (0, F(1, 13436928), F(-1, 13436928)), "ENERGY")
    second_exchange = subtract(third_components, second_components)
    b0 = 839808
    require(second_exchange == (F(-180609, 2 * b0 * b0), F(28045, 2 * b0 * b0),
                                F(152564, 2 * b0 * b0)), "ENERGY")
    require(account(cores[1]) == 745 and account(cores[2]) == 70657990
            and hermitian_cost(cores[2][3]) == 185054
            and square_norm(cores[2][0][:5]) == 33718350
            and square_norm(cores[2][1]) == 36741600, "SHARP_BUDGET")
    bank = account(cores[2]) - account(cores[1])
    require(bank == 70657245 and funded((cores[1], bank, 1), 0) == (cores[2], 0, 1)
            and funded((cores[1], bank - 1, 1), 0) == (cores[1], bank - 1, -1), "SHARP_BUDGET")
    controls = set()
    no_feedback = history("0011", 0, stop=3, feedback_mode="none")
    require(no_feedback[1] == free[:4] and all(value[5] == 0 for value in no_feedback[1]), "CONTROL")
    require(central_gradients(local_case(no_feedback[1], 1, 0))[5] == F(-1, 2592), "CONTROL")
    controls.add("no_feedback")
    first_only = history("0011", 0, stop=3, feedback_mode="first")
    continued = values[3][5] - first_only[1][3][5]
    require(first_only[1][3][5] == values[2][5] and continued == F(-71, 839808), "CONTROL")
    controls.add("first_feedback_only")
    no_field = history("0011", 0, stop=3, field_coupling=0)
    require([value[:5] for value in no_field[1]] == [value[:5] for value in free[:4]], "CONTROL")
    require(central_gradients(local_case(no_field[1], 2, 0))[:5] == times(F(-1, 839808), ELL), "CONTROL")
    controls.add("no_field_coupling")
    wrong_sign = history("0011", 0, stop=3, feedback_mode="reversed")
    require(central_gradients(local_case(wrong_sign[1], 1, 0))[5] == F(-1, 1296), "CONTROL")
    controls.add("wrong_feedback_sign")
    no_monitor = forward(cores[1], 0, move_monitor=False)
    require(no_monitor[3][5] == 0 and no_monitor[0][5] == -5, "CONTROL")
    controls.add("no_monitor_transport")
    uncoupled_account_increase = sum(second_components[:2]) - sum(first_components[:2])
    require(uncoupled_account_increase == F(1, 13436928) != 0
            and uncoupled_account_increase + exchange[2] == 0, "CONTROL")
    controls.add("omitted_interaction_energy")
    degenerate = ((1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), 1, H_REFERENCE)
    require(core_member(degenerate), "CONTROL")
    bad = decode(degenerate)[0][0]
    require((-1, 1 + bad, 1 - bad, 1) == (-1, 2, 0, 1) and bad * bad - 1 == 0, "CONTROL")
    controls.add("unrestricted_metric_degeneracy")
    require(len(controls) == 7, "CERTIFICATE")
    return direct, values[2][5], reciprocal, continued, total, exchange, bank


def check_cycles(histories):
    periods = []
    for a in (-1, 0, 1):
        cores = histories["0011", a][2]
        require(account(cores[1]) < account(cores[2]) < account(cores[3]), "SHARP_BUDGET")
        for target in (1, 2):
            ceiling = max(account(cores[n]) for n in range(1, target + 1))
            start = cores[1], ceiling - account(cores[1]), 1
            state = start
            seen = {state}
            first_return = None
            reached = 1
            for tick in range(1, 2 * target + 1):
                state = funded(state, a)
                require(state_member(state), "PERIOD")
                require(account(state[0]) + state[1] == ceiling
                        and core_bond(state[0], a) == core_bond(start[0], a), "CONSERVATION")
                if state[0] == cores[target]:
                    reached = target
                if state == start:
                    first_return = tick
                    break
                require(state not in seen, "PERIOD")
                seen.add(state)
            require(first_return == 2 * target and len(seen) == first_return and reached == target, "PERIOD")
            periods.append(first_return)
    require(tuple(periods) == (2, 4, 2, 4, 2, 4), "CERTIFICATE")
    return tuple(periods)


def comma(values):
    return ",".join(str(value) for value in values)


def certificate():
    authority = check_authority()
    check_initial_and_ring()
    fixtures = hermitian_fixtures()
    transports, holonomies = check_transports(fixtures)
    cores, funded_cases, defects = check_core_and_funding(fixtures)
    kmat, minors = matrices_and_equilibrium()
    records, digest, variations, bonds, precision, histories = check_histories()
    offshell = check_offshell(histories)
    canonical, symplectic, drift = check_canonical_and_symplectic(histories, kmat)
    direct, chi2, reciprocal, continued, total, exchange, bank = check_witnesses_and_controls(histories)
    periods = check_cycles(histories)
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority),
        "TRANSPORT_CHECKS=" + str(transports),
        "HOLONOMY_CHECKS=" + str(holonomies),
        "CORE_FIXTURES=" + str(cores),
        "FUNDED_CASES=" + str(funded_cases),
        "IMAGE_DEFECTS=" + str(defects),
        "HISTORY_RECORDS=" + str(records),
        "HISTORY_SHA256=" + digest,
        "JOINT_VARIATIONS=" + str(variations),
        "OFFSHELL_VARIATIONS=" + str(offshell),
        "K_MINOR_CHECKS=" + str(minors),
        "ENERGY_BONDS=" + str(bonds),
        "PRECISION_CHECKS=" + str(precision),
        "CANONICAL_STEPS=" + str(canonical),
        "SYMPLECTIC_CHECKS=" + str(symplectic),
        "DIRECT_CONTRAST=" + comma(direct),
        "ZERO_SOURCE_CHI2=" + str(chi2),
        "RECIPROCAL_CONTRAST=" + comma(reciprocal),
        "CONTINUED_SOURCE_CONTRAST=" + str(continued),
        "ZERO_SOURCE_TOTAL_ENERGY=" + str(total),
        "ZERO_SOURCE_ENERGY_EXCHANGE=" + comma(exchange),
        "AFFINE_WRONSKIAN_DRIFT=" + str(drift),
        "ZERO_SOURCE_FIRST_BANK=" + str(bank),
        "CYCLE_PERIODS=" + comma(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 27, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
