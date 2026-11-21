#!/usr/bin/env python3
"""Independent direct-coordinate breaker for P-INTEGER-RECIPROCAL-SOURCE-ACTION-1.

Do not execute or import before the public pin is remotely read back.
Written from PREREG.md and the canonical v103 sources without importing
this probe's primary verify.py or PROOF.md. Both implementations were
authored in the same assisted session from PREREG.md; this is independence
of implementation representation (direct 8-coordinate Hermitian gates and
explicit 5x5 matrices vs polynomial ring and circulant indexing), not a
separate human laboratory.
"""

from fractions import Fraction
import hashlib
import math
from pathlib import Path
import sys


PROBE_ID = "P-INTEGER-RECIPROCAL-SOURCE-ACTION-1"
M = 324
M2 = 104976
DIPOLE = (1, -1, 0, 0, 0)
SOURCE_CYCLE_0 = (1, 2, 2, 1, 0, 0)
SOURCE_CYCLE_1 = (0, 1, 2, 2, 1, 0)
ZERO_H = (0, 0, 0, 0, 0, 0, 0, 0)
D_H = (0, 0, 1, 0, 0, 0, 0, 0)
Z_H = (1, 0, 1, 0, 0, 1, 0, 0)

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

INITIAL_SLICES = (
    ("0010", (0, 1, 1, 0, 0), (1, 1, 0, 0, 0), 1),
    ("0011", (0, 1, 1, 0, 0), (0, 1, 1, 0, 0), 0),
    ("0100", (1, 1, 0, 0, 0), (1, 0, 0, 0, 1), 0),
    ("0101", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), 0),
    ("0110", (0, 1, 1, 0, 0), (1, 0, 0, 0, 1), 2),
    ("1001", (1, 0, 0, 0, 1), (0, 1, 1, 0, 0), -2),
    ("1010", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), 0),
    ("1011", (1, 1, 0, 0, 0), (0, 1, 1, 0, 0), -1),
    ("1100", (1, 0, 0, 0, 1), (1, 0, 0, 0, 1), 0),
    ("1101", (1, 0, 0, 0, 1), (1, 1, 0, 0, 0), 0),
)
EXPECTED_WORD_ORDER = (
    "0010", "0011", "0100", "0101", "0110",
    "1001", "1010", "1011", "1100", "1101",
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
    "AUTHORITY", "RING", "TRANSPORT", "COST", "BARE_INVERSE",
    "FUNDED_INVERSE", "CONSERVATION", "BRANCH", "IMAGE_GUARD",
    "COUPLING_SELECTION", "INITIAL_DATA", "SOURCE_PATTERN",
    "DENOMINATOR", "MEAN", "RECURRENCE", "LORENTZ", "RESPONSE_BOUND",
    "ACTION", "PREFIX", "SHARP_BUDGET", "DETECTOR", "FIXED_COUNTER",
    "BACKREACTION", "CONTROL", "PERIOD", "CERTIFICATE", "BREAKER_BYTES",
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


def inner_product(left, right):
    return sum(a * b for a, b in zip(left, right))


def real_product(x, y):
    """Product of real pairs using phi^2 = phi + 1."""
    x0, x1 = x
    y0, y1 = y
    return (x0 * y0 + x1 * y1,
            x0 * y1 + x1 * y0 + x1 * y1)


def off_diagonal_norm(c):
    """c*conjugate(c) as an independent real pair."""
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


def parity_functional(numerator, previous):
    return sum(dipole * ((now % 2) - (old % 2))
               for dipole, now, old in zip(DIPOLE, numerator, previous))


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


def next_core(core, coupling=1, reciprocal=True):
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
        if reciprocal:
            s = s + coupling * parity_functional(numerator, previous)
        numerator, previous = following, numerator
        counter += 1
    else:
        raise ValueError("phase outside carrier")
    return (s, q, h, reference, detector, numerator, previous, counter, (phase + 1) % 7)


def previous_core(core, coupling=1, reciprocal=True):
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
        recovered_p = previous
        recovered_q = tuple(entry // divisor for entry in residual)
        if reciprocal:
            s = s - coupling * parity_functional(recovered_p, recovered_q)
        numerator, previous = recovered_p, recovered_q
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


def funded_step(state, coupling=1, reciprocal=True):
    core, bank, direction = state
    if direction == 1:
        target = next_core(core, coupling, reciprocal)
    elif direction == -1:
        target = previous_core(core, coupling, reciprocal)
    else:
        raise ValueError("direction outside carrier")
    ceiling = core_cost(core) + bank
    if target is None or core_cost(target) > ceiling:
        return (core, bank, -direction)
    return (target, ceiling - core_cost(target), direction)


def conjugate_inverse(state, coupling=1, reciprocal=True):
    return reverse_direction(funded_step(reverse_direction(state), coupling, reciprocal))


def initial_row(word):
    for label, first, second, beta in INITIAL_SLICES:
        if label == word:
            return first, second, beta
    raise ValueError("word outside frozen table")


def ready_core(word, source):
    first, second, _ = initial_row(word)
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
    for word, first, second, beta in INITIAL_SLICES:
        bits = tuple(int(bit) for bit in word)
        require(len(bits) == 4 and all(bit in (0, 1) for bit in bits), "INITIAL_DATA")
        for t, recorded in enumerate((first, second)):
            location = bits[t + 2] - bits[t]
            from_bits = tuple(int((site - location) % 5 in (0, 1)) for site in range(5))
            require(recorded == from_bits and sum(recorded) == 2, "INITIAL_DATA")
        require(parity_functional(second, first) == beta, "INITIAL_DATA")
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


def check_coupling_selection():
    count = 0
    for sigma in (-2, -1, 1, 2):
        step1 = hermitian_B(D_H, -sigma)
        step2 = hermitian_A_inverse(step1)
        step3 = hermitian_B(step2, sigma)
        step4 = hermitian_A(step3)
        diff = tuple(a - b for a, b in zip(step4, D_H))
        require(diff == (9 * sigma * sigma, -5 * sigma * sigma, 0, 0,
                         -2 * sigma, sigma, -sigma, 0), "COUPLING_SELECTION")
        matching = tuple(i for i in range(8) if diff[i] == sigma)
        require(matching == (5,), "COUPLING_SELECTION")
        count += 1

    dipoles = []
    other_zero_sum = []
    for a0 in (-1, 0, 1):
        for a1 in (-1, 0, 1):
            for a2 in (-1, 0, 1):
                for a3 in (-1, 0, 1):
                    for a4 in (-1, 0, 1):
                        vec = (a0, a1, a2, a3, a4)
                        if sum(vec) == 0 and vec != (0, 0, 0, 0, 0):
                            if square_sum(vec) == 2:
                                dipoles.append(vec)
                            else:
                                other_zero_sum.append(vec)
    require(len(dipoles) == 20 and len(other_zero_sum) == 30, "COUPLING_SELECTION")
    selected = [vec for vec in dipoles
                if vec[2:] == (0, 0, 0) and vec[0] > 0]
    require(selected == [DIPOLE], "COUPLING_SELECTION")
    for vec in dipoles:
        require(vec.count(1) == 1 and vec.count(-1) == 1 and vec.count(0) == 3,
                "COUPLING_SELECTION")
        count += 1

    odd_failed_words = []
    for word, first, second, _ in INITIAL_SLICES:
        require(any(second[site] == 0 and DIPOLE[site] == 0 for site in (2, 3, 4)),
                "COUPLING_SELECTION")
        applied = matrix_vector(C_MATRIX, second)
        odd_p2 = tuple(val - M * old + dip
                       for val, old, dip in zip(applied, first, DIPOLE))
        even_p2 = tuple(val - M * old + 2 * dip
                        for val, old, dip in zip(applied, first, DIPOLE))
        require(math.gcd(2 * M, *even_p2) == 1, "COUPLING_SELECTION")
        if math.gcd(2 * M, *odd_p2) != 1:
            require(math.gcd(2 * M, *odd_p2) == 2, "COUPLING_SELECTION")
            odd_failed_words.append(word)
        count += 1
    require(tuple(odd_failed_words) == ("0010", "0101", "1010", "1101"),
            "COUPLING_SELECTION")
    require(count == 34, "CERTIFICATE")
    return count


def reader_denominator(counter):
    return 2 if counter == 0 else 2 * (M ** (counter - 1))


def laplacian_vector(field):
    return tuple(Fraction(sum(coeff * val for coeff, val in zip(row, field)), M)
                 for row in L_NUMERATOR)


def metric_diagonal(value):
    return (Fraction(-1), 1 + value, 1 - value, Fraction(1))


def check_lorentz(field):
    for value in field:
        require(Fraction(-299, 500) < value < Fraction(499, 500), "LORENTZ")
        diag = metric_diagonal(value)
        require(diag[0] < 0 and diag[1] > Fraction(201, 500)
                and diag[2] > Fraction(1, 500) and diag[3] > 0, "LORENTZ")
        det = diag[0] * diag[1] * diag[2] * diag[3]
        require(det < Fraction(-999, 250000), "LORENTZ")


def rational_reference(word, source, beta, reciprocal=True):
    first, second, _ = initial_row(word)
    fields = [
        tuple(Fraction(entry, 2) for entry in first),
        tuple(Fraction(entry, 2) for entry in second),
    ]
    for n in range(1, 24):
        idx = (n - 1) % 6
        chi_val = source * SOURCE_CYCLE_0[idx] + (beta * SOURCE_CYCLE_1[idx] if reciprocal else 0)
        forcing = tuple(Fraction(chi_val * entry, M ** n) for entry in DIPOLE)
        lap = laplacian_vector(fields[n])
        following = tuple(2 * now - old - lap_entry + force_entry
                          for now, old, lap_entry, force_entry
                          in zip(fields[n], fields[n - 1], lap, forcing))
        fields.append(following)
    return tuple(fields)


def local_joint_slice(candidate, xi, previous, following, prev_chi, next_chi, n, eff_a):
    backward = sum((now - old) ** 2 for now, old in zip(candidate, previous))
    forward = sum((later - now) ** 2 for now, later in zip(candidate, following))
    potential = inner_product(candidate, laplacian_vector(candidate))
    coupling_term = Fraction(xi, M ** n) * inner_product(DIPOLE, candidate)
    chi_kinetic = Fraction((xi - prev_chi) ** 2 + (next_chi - xi) ** 2, 2)
    chi_potential = Fraction(xi * xi, 2) - eff_a * xi
    return (Fraction(backward + forward, 2) - Fraction(potential, 2)
            + coupling_term - (chi_kinetic - chi_potential))


def check_histories():
    digest = hashlib.sha256()
    record_count = 0
    variation_count = 0

    for word, first, second, beta in INITIAL_SLICES:
        free_reference = rational_reference(word, 0, 0, reciprocal=False)
        for source in (-1, 0, 1):
            reference = rational_reference(word, source, beta, reciprocal=True)
            core = ready_core(word, source)
            numerators = [first, second]
            chis = [0]
            for n in range(1, 24):
                require(core[7] == n and core[8] == 0, "RECURRENCE")
                for _ in range(6):
                    core = next_core(core)
                require(core[7] == n and core[8] == 6, "RECURRENCE")
                chi_value = core[2][5] - core[3][5]
                expected_chi = (source * SOURCE_CYCLE_0[(n - 1) % 6]
                                + beta * SOURCE_CYCLE_1[(n - 1) % 6])
                require(chi_value == expected_chi, "SOURCE_PATTERN")
                chis.append(chi_value)
                s_before = core[0]
                core = next_core(core)
                require(core[0] - s_before == (beta if n == 1 else 0),
                        "BACKREACTION")
                require(core[7] == n + 1 and core[8] == 0, "RECURRENCE")
                numerators.append(core[5])
            extra_core = core
            for _ in range(6):
                extra_core = next_core(extra_core)
            chi_24 = extra_core[2][5] - extra_core[3][5]
            require(chi_24 == (source * SOURCE_CYCLE_0[23 % 6]
                               + beta * SOURCE_CYCLE_1[23 % 6]),
                    "SOURCE_PATTERN")
            chis.append(chi_24)

            fields = []
            for n, numerator in enumerate(numerators):
                denom = reader_denominator(n)
                require(sum(numerator) == denom, "MEAN")
                require(math.gcd(*numerator, denom) == 1, "DENOMINATOR")
                require(math.gcd(*numerator) == 1, "DENOMINATOR")
                if n >= 1:
                    require(tuple(entry % 2 for entry in numerator)
                            == tuple(entry % 2 for entry in second),
                            "DENOMINATOR")
                field = tuple(Fraction(entry, denom) for entry in numerator)
                require(sum(field) == 1, "MEAN")
                least_common = math.lcm(*(entry.denominator for entry in field))
                require(least_common == denom, "DENOMINATOR")
                require(field == reference[n], "RECURRENCE")
                check_lorentz(field)
                for value, free_value in zip(field, free_reference[n]):
                    require(abs(value - free_value)
                            < Fraction(1645, 209304) < Fraction(1, 125),
                            "RESPONSE_BOUND")
                fields.append(field)
                line = (f"{word}|{source}|{n}|"
                        + ",".join(str(entry) for entry in numerator)
                        + f"|{denom}\n")
                digest.update(line.encode("ascii"))
                record_count += 1

            eff_a = source + beta
            for n in range(1, 24):
                require(chis[n + 1] - chis[n] + chis[n - 1] == eff_a,
                        "SOURCE_PATTERN")
                lap = laplacian_vector(fields[n])
                left = tuple(fields[n + 1][site] - 2 * fields[n][site]
                             + fields[n - 1][site] + lap[site]
                             for site in range(5))
                right = tuple(Fraction(chis[n] * entry, M ** n)
                              for entry in DIPOLE)
                require(left == right, "RECURRENCE")
                if source == 0 and beta == 0:
                    require(left == (0, 0, 0, 0, 0), "CONTROL")

            for n in (1, 2, 7, 23):
                for site in range(5):
                    plus = tuple(fields[n][idx] + int(idx == site)
                                 for idx in range(5))
                    minus = tuple(fields[n][idx] - int(idx == site)
                                  for idx in range(5))
                    slope_m = Fraction(
                        local_joint_slice(plus, chis[n], fields[n - 1],
                                          fields[n + 1], chis[n - 1],
                                          chis[n + 1], n, eff_a)
                        - local_joint_slice(minus, chis[n], fields[n - 1],
                                            fields[n + 1], chis[n - 1],
                                            chis[n + 1], n, eff_a),
                        2,
                    )
                    require(slope_m == 0, "ACTION")
                    variation_count += 1
                slope_s = Fraction(
                    local_joint_slice(fields[n], chis[n] + 1, fields[n - 1],
                                      fields[n + 1], chis[n - 1],
                                      chis[n + 1], n, eff_a)
                    - local_joint_slice(fields[n], chis[n] - 1, fields[n - 1],
                                        fields[n + 1], chis[n - 1],
                                        chis[n + 1], n, eff_a),
                    2,
                )
                expected_tail = Fraction(inner_product(DIPOLE, numerators[n]),
                                         2 * (M ** (2 * n - 1)))
                require(slope_s == expected_tail
                        and abs(slope_s) < Fraction(1, 162), "ACTION")
                at_center = local_joint_slice(
                    fields[n], chis[n], fields[n - 1], fields[n + 1],
                    chis[n - 1], chis[n + 1], n, eff_a)
                at_plus = local_joint_slice(
                    fields[n], chis[n] + 1, fields[n - 1], fields[n + 1],
                    chis[n - 1], chis[n + 1], n, eff_a)
                at_minus = local_joint_slice(
                    fields[n], chis[n] - 1, fields[n - 1], fields[n + 1],
                    chis[n - 1], chis[n + 1], n, eff_a)
                require(at_center - at_plus > Fraction(40, 81)
                        and at_center - at_minus > Fraction(40, 81), "ACTION")
                variation_count += 1

    require(record_count == 750 and variation_count == 720, "CERTIFICATE")
    return record_count, digest.hexdigest(), variation_count


def first_funded_block(source, bank, coupling=1, reciprocal=True):
    state = (ready_core("0010", source), bank, 1)
    states = [state]
    for _ in range(7):
        state = funded_step(state, coupling=coupling, reciprocal=reciprocal)
        states.append(state)
    return tuple(states)


def check_detector(core, expected_j_coefficient):
    detector = core[4]
    require(detector[5] == expected_j_coefficient, "DETECTOR")
    recovered = tuple(z - h + r for z, h, r in zip(detector, core[2], core[3]))
    require(recovered == Z_H, "DETECTOR")


def check_fixed_counter_and_controls():
    prescribed_prefix = {
        -1: (31, 31, 43, 63, 147, 377, 747, 344440),
        0: (30, 30, 30, 40, 40, 30, 30, 345012),
        1: (31, 31, 43, 63, 147, 377, 803, 347090),
    }
    prescribed_second = {
        -1: (487, 167, -230, 130, 94),
        1: (491, 163, -230, 130, 94),
    }
    prescribed_third = {
        -1: (120111, -6141, -59422, 98366, 57038),
        0: (120977, -7007, -59350, 98366, 56966),
        1: (121843, -7873, -59278, 98366, 56894),
    }
    prefixes = {}
    sharp_banks = {}
    two_block_cores = {}
    for source in (-1, 0, 1):
        core = ready_core("0010", source)
        cores = [core]
        for _ in range(14):
            core = next_core(core)
            cores.append(core)
        two_block_cores[source] = tuple(cores)
        energy_list = tuple(core_cost(c) for c in cores[:8])
        prefixes[source] = energy_list
        require(prefixes[source] == prescribed_prefix[source], "PREFIX")
        if source in (-1, 1):
            require(cores[7][5] == prescribed_second[source], "FIXED_COUNTER")
            sharp_banks[source] = max(energy_list) - energy_list[0]
        require(cores[14][5] == prescribed_third[source], "BACKREACTION")

    sharp_pair = (sharp_banks[-1], sharp_banks[1])
    require(sharp_pair == (344409, 347059), "SHARP_BUDGET")
    common_bank = max(sharp_pair)
    require(common_bank == 347059, "SHARP_BUDGET")

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
    require(final_banks == (2650, 0), "SHARP_BUDGET")
    denom2 = reader_denominator(negative[0][7])
    require(negative[0][7] == positive[0][7] == 2, "FIXED_COUNTER")
    negative_field = tuple(Fraction(value, denom2) for value in negative[0][5])
    positive_field = tuple(Fraction(value, denom2) for value in positive[0][5])
    contrast = tuple(upper - lower for upper, lower in zip(positive_field, negative_field))
    require(contrast == tuple(Fraction(value, 162) for value in DIPOLE), "FIXED_COUNTER")
    for lower, upper, difference in zip(negative_field, positive_field, contrast):
        matrix_difference = tuple(x - y for x, y
                                  in zip(metric_diagonal(upper), metric_diagonal(lower)))
        require(matrix_difference == (0, difference, -difference, 0), "FIXED_COUNTER")

    controls = set()
    unforced_reference = rational_reference("0010", 0, 0, reciprocal=False)
    scaled_free2 = tuple(value * reader_denominator(2) for value in unforced_reference[2])
    scaled_free3 = tuple(value * reader_denominator(3) for value in unforced_reference[3])
    require(all(value.denominator == 1 for value in scaled_free2), "CONTROL")
    require(all(value.denominator == 1 for value in scaled_free3), "CONTROL")
    unforced_p2 = tuple(value.numerator for value in scaled_free2)
    unforced_p3 = tuple(value.numerator for value in scaled_free3)
    require(unforced_p3 == (120975, -7005, -59350, 98366, 56966), "CONTROL")

    denom3 = reader_denominator(3)
    zero_seed_field3 = tuple(Fraction(value, denom3) for value in prescribed_third[0])
    zero_contrast = tuple(rec - free for rec, free
                          in zip(zero_seed_field3, unforced_reference[3]))
    require(zero_contrast == tuple(Fraction(value, 104976) for value in DIPOLE),
            "BACKREACTION")

    for source, expected_chi2 in ((-1, -1), (0, 1), (1, 3)):
        rec_c13 = two_block_cores[source][13]
        require(rec_c13[2][5] - rec_c13[3][5] == expected_chi2, "BACKREACTION")
        ow_core = ready_core("0010", source)
        ow_cores = [ow_core]
        for _ in range(14):
            ow_core = next_core(ow_core, coupling=1, reciprocal=False)
            ow_cores.append(ow_core)
        require(ow_cores[13][2][5] - ow_cores[13][3][5] == 2 * source, "CONTROL")
        require(ow_cores[7][5] == two_block_cores[source][7][5], "CONTROL")
        diff_p3 = tuple(a - b for a, b in zip(two_block_cores[source][14][5],
                                              ow_cores[14][5]))
        require(diff_p3 == (2, -2, 0, 0, 0), "BACKREACTION")
    controls.add("one_way_comparison")

    control_outputs = []
    for source in (-1, 1):
        history = first_funded_block(source, common_bank, coupling=0)
        require(history[-1][0][7:] == (2, 0) and history[-1][2] == 1, "CONTROL")
        require(history[-1][0][5] == unforced_p2, "CONTROL")
        require(history[-1][0][0] == source, "CONTROL")
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
        absent_backreaction = previous_core(image, reciprocal=False)
        require(absent_backreaction is not None
                and absent_backreaction != common_histories[source][-2][0]
                and absent_backreaction[0] != common_histories[source][-2][0][0],
                "CONTROL")
    controls.add("omitted_inverse_source")
    controls.add("omitted_inverse_backreaction")

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
    require(controls == {
        "one_way_comparison", "coupling_zero", "omitted_inverse_source",
        "omitted_inverse_backreaction", "wrong_first_multiplier",
        "unrestricted_degeneracy"}, "CERTIFICATE")

    return (
        prefixes[-1], prefixes[0], prefixes[1],
        negative[0][5], positive[0][5],
        prescribed_third[-1], prescribed_third[0], prescribed_third[1],
        sharp_pair, final_banks, contrast, zero_contrast, len(controls),
    )


def check_cycles():
    fixtures = (
        (-1, 772, 14), (-1, 344409, 26), (-1, 347059, 28), (-1, 344408, 14),
        (1, 772, 14), (1, 344409, 14), (1, 347059, 18), (1, 347058, 14),
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
    selection_count = check_coupling_selection()
    history_count, history_hash, action_count = check_histories()
    (prefix_negative, prefix_zero, prefix_positive,
     second_negative, second_positive,
     third_negative, third_zero, third_positive,
     sharp, final_banks, contrast, zero_contrast,
     control_count) = check_fixed_counter_and_controls()
    periods = check_cycles()
    require(control_count == 6, "CERTIFICATE")
    lines = (
        "CERTIFICATE=" + PROBE_ID,
        "AUTHORITY_FILES=" + str(authority_count),
        "TRANSPORT_CHECKS=" + str(transport_count),
        "CORE_FIXTURES=" + str(core_count),
        "FUNDED_CASES=" + str(funded_count),
        "IMAGE_DEFECTS=" + str(image_count),
        "COUPLING_SELECTION_CHECKS=" + str(selection_count),
        "HISTORY_RECORDS=" + str(history_count),
        "HISTORY_SHA256=" + history_hash,
        "ACTION_VARIATIONS=" + str(action_count),
        "PREFIX_NEG=" + comma(prefix_negative),
        "PREFIX_ZERO=" + comma(prefix_zero),
        "PREFIX_POS=" + comma(prefix_positive),
        "P2_NEG=" + comma(second_negative),
        "P2_POS=" + comma(second_positive),
        "P3_NEG=" + comma(third_negative),
        "P3_ZERO=" + comma(third_zero),
        "P3_POS=" + comma(third_positive),
        "SHARP_BANKS=" + comma(sharp),
        "COMMON_FINAL_BANKS=" + comma(final_banks),
        "METRIC_CONTRAST=" + comma(contrast),
        "ZERO_SEED_CONTRAST=" + comma(zero_contrast),
        "CYCLE_PERIODS=" + comma(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 25, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate_bytes()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
