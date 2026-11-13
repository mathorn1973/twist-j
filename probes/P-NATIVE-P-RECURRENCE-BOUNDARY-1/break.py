#!/usr/bin/env python3
"""Frozen, result-exposed, method-separate audit of assertions A--E.

PUBLIC / NON-CANONICAL / L1. SPDX-License-Identifier: Apache-2.0.
Written from PREREG.md and the pinned #1629 comparison contract.
Neither the author's proof nor executable nor scientific output was read.
"""

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import sys


PREREG_SHA256 = "f6d16a47d191866e2299a3802b6fc6590f5fb23042e37895f5d03fd165b6c9f7"
SHEETS = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
SLICE_SHEETS = (
    ((0, 4), (0, 4), (2, 3), (0, 4), (2, 3)),
    ((0, 4), (1, 2), (1, 2), (0, 1), (2, 3)),
)
BASE_SHEETS = (0, 4)
LIFT = (0, 1, 2, -2, -1)
EPSILON = (0, 1, 0, 0, -1)
SWAP = (2, 3, 0, 1, 4, 5)


def require(condition, claim, message):
    if not condition:
        print("BREAKER FAIL " + claim + ": " + message)
        raise SystemExit(1)


def bit(n):
    return n.bit_count() & 1


def sign(n):
    return (n > 0) - (n < 0)


def identity(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def multiply(left, right):
    """Exact homogeneous affine composition, left after right."""
    size = len(left)
    return tuple(
        tuple(
            sum(c * right[h][j] for h, c in enumerate(left[i]) if c) % 5
            for j in range(size)
        )
        for i in range(size)
    )


def power(matrix, exponent):
    answer = identity(len(matrix))
    for _ in range(exponent):
        answer = multiply(matrix, answer)
    return answer


class Affine:
    """Homogeneous matrices, evaluated as sparse rows."""

    def __init__(self, rows):
        self.matrix = tuple(tuple(c % 5 for c in row) for row in rows)
        self.rows = tuple(
            tuple((j, c) for j, c in enumerate(row) if c)
            for row in self.matrix[:-1]
        )

    def __call__(self, point):
        homogeneous = point + (1,)
        return tuple(
            sum(c * homogeneous[j] for j, c in row) % 5 for row in self.rows
        )


def native_matrices():
    final = (0, 0, 0, 0, 0, 0, 1)
    a = (
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0), final,
    )
    b = (
        (0, 0, -1, 0, 0, 0, 0),
        (0, 0, 0, -1, 0, 0, 0),
        (-1, 0, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0, -1, 0), final,
    )
    c = (
        (0, 0, -1, 0, 0, 0, 2),
        (0, 0, 0, -1, 0, 1, 1),
        (-1, 0, 0, 0, 0, 0, 2),
        (0, -1, 0, 0, 0, -1, 1),
        (0, 0, 0, 0, -1, 0, 1),
        (0, 0, 0, 0, 0, -1, 0), final,
    )

    def reflection(offset):
        return tuple(
            tuple(-int(i == j) for j in range(6)) + (offset[i],)
            for i in range(6)
        ) + (final,)

    return tuple(Affine(rows) for rows in (
        a, b, c, reflection((2, 1, 3, 4, 1, 1)),
        reflection((2, 1, 3, 4, 2, 1)),
    ))


def sheet(point):
    return sum(point) % 5


class NativeAudit:
    def __init__(self):
        self.letters = native_matrices()
        self.tau = Affine(multiply(self.letters[4].matrix, self.letters[3].matrix))
        self.translations = tuple(Affine(power(self.tau.matrix, j)) for j in range(5))
        self.corrected = {
            (t, z): Affine(multiply(
                self.translations[(-2 * t) % 5].matrix,
                self.letters[(z + 2 * t) % 5].matrix,
            ))
            for t in (0, 1) for z in BASE_SHEETS
        }
        self.points = tuple(product(range(5), repeat=6))
        self.fibres = tuple(tuple(x for x in self.points if sheet(x) == z)
                            for z in range(5))
        self.selected = self.fibres[0] + self.fibres[4]

    def literal(self, t, x):
        return self.letters[(sheet(x) + 2 * t) % 5](x)

    def compound(self, t, x):
        return self.corrected[t, sheet(x)](x)

    def allowed(self, n, x):
        phase = n % 5
        start = n - phase
        return sheet(x) in SLICE_SHEETS[bit(start)][phase]

    def command(self, n):
        phase = n % 5
        require(phase != 0, "D", "command requested at selector phase")
        return ((3, 3, 3, 3), (4, 3, 4, 3))[bit(n - phase)][phase - 1]

    def micro_forward(self, n, x):
        if n % 5 == 0:
            return n + 1, self.literal(bit(n), x)
        return n + 1, self.letters[self.command(n)](x)

    def micro_backward(self, n, y):
        require(n > 0, "D", "inverse requested outside forward image")
        previous = n - 1
        if previous % 5:
            return previous, self.letters[self.command(previous)](y)
        t = bit(previous)
        source_sheets = tuple(z for z in BASE_SHEETS if SHEETS[t][z] == sheet(y))
        require(len(source_sheets) == 1, "D", "selector inverse sheet ambiguous")
        command = (source_sheets[0] + 2 * t) % 5
        return previous, self.letters[command](y)

    def raw_and_classification(self):
        involutions = selector_checks = translation_checks = 0
        for x in self.points:
            for letter in self.letters:
                require(letter(letter(x)) == x, "B", "raw involution failed")
                involutions += 1
            shifted = x[:4] + ((x[4] + 1) % 5,) + x[5:]
            require(self.tau(x) == shifted, "B", "e after d is not q translation")
            translation_checks += 1
            for t in (0, 1):
                require(sheet(self.literal(t, x)) == SHEETS[t][sheet(x)],
                        "B", "literal selector sheet law failed")
                selector_checks += 1

        found = []
        examined = 0
        for mask in range(1, 32):
            domain = tuple(z for z in range(5) if mask & (1 << z))
            for corrections in product(range(5), repeat=2):
                examined += 1
                works = True
                for t in (0, 1):
                    image = tuple((SHEETS[t][z] + corrections[t]) % 5 for z in domain)
                    works = works and len(set(image)) == len(domain) and set(image) == set(domain)
                if works:
                    found.append((domain, corrections))
        nominated = [((z,), tuple((z - SHEETS[t][z]) % 5 for t in (0, 1)))
                     for z in range(5)]
        nominated += [((0, 4), (0, 3)), ((0, 1), (1, 4))]
        require(set(found) == set(nominated), "B", "correction classification differs")
        require(len(found) == 7 and max(len(d) for d, _ in found) == 2,
                "B", "number or maximal size differs")
        maximal_unchanged = tuple(d for d, correction in found
                                 if len(d) == 2 and correction[0] == 0)
        require(maximal_unchanged == ((0, 4),), "B", "unchanged t=0 pair is not unique")
        print("BREAKER raw involutions=" + str(involutions)
              + " selector=" + str(selector_checks) + " tau=" + str(translation_checks))
        print("BREAKER correction triples examined=" + str(examined)
              + " accepted=" + str(len(found)))

    def synchronized_matrix(self, n, length):
        z = (4 + 2 * bit(n - 1)) % 5
        matrix = identity(7)
        for clock in range(n, n + length):
            t = bit(clock)
            matrix = multiply(self.letters[(z + 2 * t) % 5].matrix, matrix)
            z = SHEETS[t][z]
        return matrix, z

    def check_linear_block(self, n, length, identity_expected=False):
        matrix, z = self.synchronized_matrix(n, length)
        exchange = bit(n - 1) ^ bit(n + length - 1)
        permutation = SWAP if exchange else tuple(range(6))
        scalar = 4 if length % 2 else 1
        target = tuple(tuple(scalar * int(j == permutation[i]) for j in range(6))
                       for i in range(6))
        require(tuple(row[:6] for row in matrix[:6]) == target,
                "A", "composed affine linear part differs from endpoint formula")
        require(z == (4 + 2 * bit(n + length - 1)) % 5,
                "A", "synchronized sheet failed to persist")
        if identity_expected:
            require(exchange == 0, "A", "recurrence certificate did not remove exchange")

    def recurrence(self):
        sync_cases = 0
        for start in range(1024):
            for initial in range(5):
                z = initial
                for clock in range(start, start + 9):
                    z = SHEETS[bit(clock)][z]
                require(z == (4 + 2 * bit(start + 8)) % 5,
                        "A", "finite inherited nine-tick synchronization audit failed")
                sync_cases += 1
        stencils = 0
        for n in range(3, 97):
            for length in range(1, 17):
                self.check_linear_block(n, length)
                stencils += 1
        lengths = set(range(1, 129))
        lengths.update((1 << j) + d for j in range(1, 11) for d in (-1, 0, 1))
        certificates = 0
        for length in sorted(lengths):
            threshold = 3 + ((9 + length - 1) // length) * length
            for lower in (threshold, threshold + 1000000):
                j = 1
                parity = (1 + bit(length - 1)) % 2
                while (1 << j) <= length or (1 << j) - length + 1 < lower or j % 2 != parity:
                    j += 1
                n = (1 << j) - length + 1
                require(n >= lower and bit(n - 1) == 1 and bit(n + length - 1) == 1,
                        "A", "binary complement certificate failed")
                self.check_linear_block(n, length, identity_expected=True)
                certificates += 1
        print("BREAKER recurrence sync_cases=" + str(sync_cases)
              + " affine_stencils=" + str(stencils) + " certificates=" + str(certificates))

    def all_compound_states(self):
        cases = 0
        for t in (0, 1):
            image = set()
            for x in self.selected:
                y = self.compound(t, x)
                require(sheet(y) == sheet(x), "C", "compound changed selected sheet")
                require(self.compound(t, y) == x, "C", "compound full inverse failed")
                require(y == self.translations[(-2 * t) % 5](self.literal(t, x)),
                        "C", "compound matrix is not the declared correction")
                image.add(y)
                cases += 1
            require(image == set(self.selected), "C", "compound not onto full occupied carrier")
        for n in range(65):
            for x in (self.selected[0], self.selected[-1], (1, 1, 0, 0, 3, 0)):
                y = self.compound(bit(n), x)
                require(self.compound(bit((n + 1) - 1), y) == x,
                        "C", "compound previous-bit clock inverse failed")
        print("BREAKER compound full_states=" + str(cases))

    def microphases(self):
        boundary_representatives = {}
        for start in range(0, 10240, 5):
            boundary_representatives.setdefault((bit(start), bit(start + 5)), start)
        require(set(boundary_representatives) == set(product((0, 1), repeat=2)),
                "D", "finite actual block starts did not cover all boundary bit pairs")
        forward_cases = reverse_cases = blocks = 0
        for bits, start in sorted(boundary_representatives.items()):
            t = bits[0]
            for phase in range(5):
                n = start + phase
                current_sheets = SLICE_SHEETS[t][phase]
                domain = tuple(x for z in current_sheets for x in self.fibres[z])
                destination_sheets = BASE_SHEETS if phase == 4 else SLICE_SHEETS[t][phase + 1]
                destination = tuple(x for z in destination_sheets for x in self.fibres[z])
                image = set()
                for x in domain:
                    require(self.allowed(n, x), "D", "wrong source microphase slice")
                    next_n, y = self.micro_forward(n, x)
                    require(next_n == n + 1 and self.allowed(next_n, y),
                            "D", "microtick clock or destination slice failed")
                    require(self.micro_backward(next_n, y) == (n, x),
                            "D", "backward after forward failed on full slice")
                    image.add(y)
                    forward_cases += 1
                require(image == set(destination), "D", "microphase image incomplete")
                for y in destination:
                    previous_n, x = self.micro_backward(n + 1, y)
                    require(self.micro_forward(previous_n, x) == (n + 1, y),
                            "D", "forward after backward failed on full slice")
                    reverse_cases += 1
            for x in self.selected:
                state = (start, x)
                for _ in range(5):
                    state = self.micro_forward(*state)
                require(state == (start + 5, self.compound(t, x)),
                        "D", "five actual ticks differ from corrected block")
                for _ in range(5):
                    state = self.micro_backward(*state)
                require(state == (start, x), "D", "five-tick full inverse failed")
                blocks += 1
        print("BREAKER microphases forward=" + str(forward_cases)
              + " reverse=" + str(reverse_cases) + " blocks=" + str(blocks)
              + " boundary_types=" + str(len(boundary_representatives)))
        return boundary_representatives

    def source_pair(self, boundary_representatives):
        pair = ((1, 1, 0, 0, 3, 0), (1, 1, 0, 0, 2, 0))
        require(all(pair[0][i] == pair[1][i] for i in (0, 1, 2, 3, 5)),
                "E", "paired preparation changes a nonsource coordinate")
        require(tuple(sheet(x) for x in pair) == (0, 4), "E", "paired sheets differ")
        for t in (0, 1):
            outputs = tuple(self.compound(t, x) for x in pair)
            receiver = tuple((y[1], y[3]) for y in outputs)
            readings = tuple(sign(LIFT[a] ** 2 - LIFT[b] ** 2) for a, b in receiver)
            require(receiver == ((1, 0), (0, 4)) and readings == (1, -1),
                    "E", "one present receiver read does not separate corrected outputs")
            require(tuple(sheet(y) for y in outputs) == (0, 4),
                    "E", "full state lost the source sheet distinction")
        for start in boundary_representatives.values():
            for x, expected in zip(pair, (1, -1)):
                state = (start, x)
                for _ in range(5):
                    state = self.micro_forward(*state)
                y = state[1]
                require(sign(LIFT[y[1]] ** 2 - LIFT[y[3]] ** 2) == expected,
                        "E", "actual blocked acquisition does not realize paired read")
        print("BREAKER paired acquisition=PASS source=q receiver=p4,p4p")


@dataclass(frozen=True)
class Reference:
    mu: int
    q: int
    p: int
    u: int
    v: int
    alpha: int
    beta: int
    central: int
    bank: int
    vertex: int
    direction: int


def reference_energy(y):
    return sum(a * a for a in (y.q, y.p, y.u, y.v)) + 2 * LIFT[y.mu] ** 2


def integer_shear(k, y):
    coordinates = (y.q, y.p, y.u, y.v, 1)
    rows = (
        (1, 0, 0, 0, 0), (0, 1, 0, 0, k),
        (k, 0, 1, 0, 0), (k, 0, 0, 1, 0),
    )
    q, p, u, v = tuple(sum(a * b for a, b in zip(row, coordinates)) for row in rows)
    return replace(y, q=q, p=p, u=u, v=v, alpha=(y.alpha + k) % 5)


def reference_partner(y):
    if (y.vertex, y.direction) not in ((0, 1), (1, -1)):
        return y
    k = EPSILON[y.mu] if y.vertex == 0 else -EPSILON[y.mu]
    proposal = integer_shear(k, y)
    change = reference_energy(proposal) - reference_energy(y)
    formula = 2 * k * (y.p + y.q * (y.u + y.v)) + k * k * (1 + 2 * y.q * y.q)
    require(change == formula, "reference", "energy difference does not equal Delta")
    bank = y.bank - change
    if not 0 <= bank <= 3:
        return y
    return replace(proposal, bank=bank, vertex=1 - y.vertex, direction=-y.direction)


def reference_flip(y):
    return replace(y, direction=-y.direction)


def reference_forward(y):
    return reference_flip(reference_partner(y))


def reference_backward(y):
    return reference_partner(reference_flip(y))


def weyl_action(y, basis):
    shifted = (basis + y.beta) % 5
    return shifted, (y.central + y.alpha * shifted) % 5


def reference_audit():
    accepted_edges = refused_points = zero_points = 0
    for mu in (1, 4):
        h = EPSILON[mu]
        for alpha, beta, central in product(range(5), repeat=3):
            start = Reference(mu, 1, 0, 1, -1, alpha, beta, central, 3, 0, 1)
            require(reference_energy(start) + start.bank == 8,
                    "reference", "exposed pair not in Y_(8,3)")
            expected = replace(start, p=h, u=1 + h, v=-1 + h, alpha=(alpha + h) % 5,
                               bank=0, vertex=1)
            require(reference_forward(start) == expected,
                    "reference", "full exposed forward output differs")
            require(sign(expected.u ** 2 - expected.v ** 2) == h,
                    "reference", "exposed reference record differs")
            current = start
            for _ in range(4):
                edge = reference_partner(current)
                following = reference_forward(current)
                require(reference_partner(edge) == current,
                        "reference", "complete pairing inverse failed")
                require(reference_backward(following) == current
                        and reference_forward(reference_backward(current)) == current,
                        "reference", "full local tick inverse failed")
                require(reference_energy(following) + following.bank == 8,
                        "reference", "complete reference energy account changed")
                k = (h if current.vertex == 0 else -h) if edge.vertex != current.vertex else 0
                for basis in range(5):
                    output, phase = weyl_action(current, basis)
                    require(weyl_action(following, basis) == (output, (phase + k * output) % 5),
                            "reference", "Weyl equality lost a central phase or shift")
                current = following
                accepted_edges += 1
            require(current == start, "reference", "four-step accepted cycle not closed")

            for vertex, direction in product((0, 1), (1, -1)):
                refused = Reference(mu, 1, 1, 1, 0, alpha, beta, central, 3, vertex, direction)
                require(reference_energy(refused) + refused.bank == 8,
                        "reference", "refusal witness not on full shell")
                require(reference_partner(refused) == refused
                        and reference_forward(refused) == reference_flip(refused)
                        and reference_backward(reference_forward(refused)) == refused,
                        "reference", "refusal changed a retained coordinate")
                refused_points += 1

    for mu, geometry, bank in ((0, (2, 1, 1, 1), 1), (2, (0, 0, 0, 0), 0),
                              (3, (0, 0, 0, 0), 0)):
        for alpha, beta, central in product(range(5), repeat=3):
            for vertex, direction in product((0, 1), (1, -1)):
                y = Reference(mu, *geometry, alpha, beta, central, bank, vertex, direction)
                require(reference_energy(y) + y.bank == 8,
                        "reference", "zero-source witness not on full shell")
                inward = (vertex, direction) in ((0, 1), (1, -1))
                expected = replace(y, vertex=1 - vertex) if inward else reference_flip(y)
                require(reference_forward(y) == expected and reference_backward(expected) == y,
                        "reference", "accepted zero-source edge or its inverse failed")
                zero_points += 1
    print("BREAKER reference cycle_edges=" + str(accepted_edges)
          + " refusal_points=" + str(refused_points) + " zero_points=" + str(zero_points))


def main():
    prereg = Path(__file__).with_name("PREREG.md").read_bytes()
    if sha256(prereg).hexdigest() != PREREG_SHA256:
        print("BREAKER INTEGRITY_STOP preregistration hash differs")
        return 2
    print("BREAKER exposure=result-exposed method-separate same-session")
    audit = NativeAudit()
    audit.raw_and_classification()
    audit.recurrence()
    audit.all_compound_states()
    representatives = audit.microphases()
    audit.source_pair(representatives)
    reference_audit()
    print("BREAKER verdict=A-E_FINITE_AUDIT_SURVIVES extension=NEW_DECLARED P_admission=OPEN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
