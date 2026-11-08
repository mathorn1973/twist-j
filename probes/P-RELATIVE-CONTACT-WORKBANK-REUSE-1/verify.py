#!/usr/bin/env python3
"""Exact three-use write/copy/uncompute audit. NON-CANONICAL / L1.

The ring arithmetic and S builder are adapted from the public
P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1 verifier at
26731e2bd7f1394b4d274528525e6d78cbe6bbf9. The six-place copier is the
disclosed C-BANK-COPY-WORD-1 witness, not a newly discovered word.
The four/five-coefficient comparison is an internal representation crosscheck,
not independent authorship or independent mathematical acceptance.

Every literal primitive of the forward program and its expanded inverse is
visited. Only exact ordered two-value contact maps are cached; complete states,
word endpoints, input cases and oracle answers are never cached as transitions.
Expected formulas are used only by assertions. No search, randomness, network,
subprocess, file writes, floating-point arithmetic or timing output is used.
"""

from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import re
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
WORD_SHA256 = "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b"


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    coefficients = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            coefficients[(i + j) % 5] += x * y
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def conjugate(a):
    coefficients = [0] * 5
    for i, x in enumerate(a):
        coefficients[(-i) % 5] += x
    return tuple(coefficients[i] - coefficients[4] for i in range(4))


def hermitian(a):
    return mul(a, conjugate(a))


def mul_j(a):
    x, y, z, t = a
    return (-t, x - t, y - t, z - t)


def rotate(a, k=1):
    for _ in range(2 * (k % 5)):
        a = mul_j(a)
    return a


def account(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def residue(a):
    return sum(a) % 5


def contact4(a, b):
    admitted = all((x - y) % 2 == 0 for x, y in zip(a, b))
    if not admitted:
        return a, b, False
    center = tuple((x + y) // 2 for x, y in zip(a, b))
    half = tuple((x - y) // 2 for x, y in zip(a, b))
    turned = rotate(half)
    return add(center, turned), sub(center, turned), True


# Independent five-cyclic-coefficient arithmetic modulo a constant vector.
# Its contact implementation calls neither contact4 nor rotate.
def normalize5(a):
    minimum = min(a)
    return tuple(x - minimum for x in a)


def lift5(a):
    return normalize5(a + (0,))


def add5(a, b):
    return normalize5(tuple(x + y for x, y in zip(a, b)))


def sub5(a, b):
    return normalize5(tuple(x - y for x, y in zip(a, b)))


def hermitian5(a):
    coefficients = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            coefficients[(i - j) % 5] += x * y
    return normalize5(coefficients)


def account5(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def contact5(a, b):
    difference = sub5(a, b)
    admitted = all(x % 2 == 0 for x in difference)
    if not admitted:
        return a, b, False
    half = tuple(x // 2 for x in difference)
    turned = tuple(half[(i - 2) % 5] for i in range(5))
    delta = sub5(turned, half)
    return add5(a, delta), sub5(b, delta), True


class ExactContacts:
    """Intern exact values and certify each distinct ordered pair's orbit.

    A cached transition consists of two value IDs only. Certification checks
    both arithmetic representations, the guard, complete Hermitian account,
    its trace Q, sum, labelled residues and C^5=id. Refused and admitted
    diagonal pairs are fixed; an admitted nonzero difference has period five.
    Every use still reads and writes the two actual addressed state entries.
    """

    def __init__(self):
        self.values = []
        self.value_ids = {}
        self.values5 = []
        self.norms = []
        self.accounts = []
        self.residues = []
        self.transitions = []
        self.admitted = []
        self.contacts = 0
        self.swaps = 0
        self.certified_orbits = 0

    def intern(self, value):
        assert len(value) == 4 and all(type(x) is int for x in value)
        if value in self.value_ids:
            return self.value_ids[value]
        identity = len(self.values)
        lifted = lift5(value)
        norm = hermitian(value)
        assert lift5(norm) == hermitian5(lifted)
        assert account(value) == account5(lifted)
        assert residue(value) == sum(lifted) % 5
        self.value_ids[value] = identity
        self.values.append(value)
        self.values5.append(lifted)
        self.norms.append(norm)
        self.accounts.append(account(value))
        self.residues.append(residue(value))
        self.transitions.append({})
        self.admitted.append({})
        return identity

    def encode(self, state):
        return [self.intern(value) for value in state]

    def decode(self, state):
        return tuple(self.values[identity] for identity in state)

    def certify(self, ia, ib):
        start = (ia, ib)
        records = []
        orbit = []
        guard = None
        for _ in range(5):
            a, b = self.values[ia], self.values[ib]
            a5, b5 = self.values5[ia], self.values5[ib]
            c, d, accepted = contact4(a, b)
            c5, d5, accepted5 = contact5(a5, b5)
            assert accepted == accepted5
            assert (c5, d5) == (lift5(c), lift5(d))
            if guard is None:
                guard = accepted
            assert accepted == guard
            ic, id_ = self.intern(c), self.intern(d)
            assert add(c, d) == add(a, b)
            assert add5(c5, d5) == add5(a5, b5)
            assert add(self.norms[ic], self.norms[id_]) == add(self.norms[ia], self.norms[ib])
            assert self.accounts[ic] + self.accounts[id_] == self.accounts[ia] + self.accounts[ib]
            assert (self.residues[ic], self.residues[id_]) == (self.residues[ia], self.residues[ib])
            assert account5(c5) + account5(d5) == account5(a5) + account5(b5)
            assert add5(hermitian5(c5), hermitian5(d5)) == add5(hermitian5(a5), hermitian5(b5))
            records.append((ia, ib, ic, id_, accepted))
            ia, ib = ic, id_
            orbit.append((ia, ib))
        assert (ia, ib) == start  # Also four further contacts undo the first.
        if not guard or start[0] == start[1]:
            assert all(pair == start for pair in orbit)
        else:
            assert start not in orbit[:4] and len(set(orbit)) == 5
        for ia, ib, ic, id_, accepted in records:
            output = (ic, id_)
            assert self.transitions[ia].get(ib, output) == output
            assert self.admitted[ia].get(ib, accepted) == accepted
            self.transitions[ia][ib] = output
            self.admitted[ia][ib] = accepted
        self.certified_orbits += 1
        return self.transitions[start[0]][start[1]]

    def apply(self, state, word):
        # Hot loop deliberately visits EVERY literal contact, including refused
        # and diagonal contacts and the four copies in every literal inverse.
        transitions = self.transitions
        certify = self.certify
        for i, j in word:
            a, b = state[i], state[j]
            result = transitions[a].get(b)
            if result is None:
                result = certify(a, b)
            state[i], state[j] = result
        self.contacts += len(word)

    def apply_counted(self, state, word):
        accepted = 0
        for i, j in word:
            a, b = state[i], state[j]
            result = self.transitions[a].get(b)
            if result is None:
                result = self.certify(a, b)
            state[i], state[j] = result
            accepted += self.admitted[a][b]
        self.contacts += len(word)
        return accepted

    def swap(self, state, i, j):
        a, b = state[i], state[j]
        # A generic supplied SWAP transports residues. These frozen reloads
        # exchange equal residues and therefore also preserve labelled residues.
        assert self.residues[a] == self.residues[b]
        state[i], state[j] = b, a
        self.swaps += 1

    def invariants(self, state):
        total, norm = ZERO, ZERO
        for identity in state:
            total = add(total, self.values[identity])
            norm = add(norm, self.norms[identity])
        return (sum(self.accounts[i] for i in state), total, norm,
                tuple(self.residues[i] for i in state))


def inverse(word):
    return tuple(edge for edge in reversed(word) for _ in range(4))


U = sub(ONE, rotate(ONE))
J = add(ONE, rotate(ONE))
B = add(ONE, rotate(ONE, 2))
F = ((0, 1), (1, 2))
F_INVERSE = inverse(F)
T = ((3, 4),)
G, H, GATE, CLOCK = 5, 9, 10, 3
OPEN = ((1, G),)
A0 = ((G, H),)
OPEN2 = ((H, GATE),)


def enable(selector):
    contact = ((selector, H),)
    return A0 + contact + A0 * 4 + contact * 4


def disable(selector):
    contact = ((selector, H),)
    return contact + A0 + contact * 4 + A0 * 4


def scan(base):
    word = ()
    for p in range(5):
        a, b = base + 2 * p, base + 2 * p + 1
        opening = ((CLOCK, GATE),)
        writer = ((CLOCK, a),) * 4 + ((a, b),) * 4
        writer += ((CLOCK, a), (a, b))
        word += opening + writer + opening * 4 + T
    return word


def wrapper(selector, base):
    return enable(selector) + OPEN2 + scan(base) + OPEN2 * 4 + disable(selector)


def d_word(c, d):
    a, b = ((H, c),), ((H, d),)
    return a * 3 + b * 3 + a + b + a


def selector_word(c, d):
    word = d_word(c, d)
    return A0 + word + A0 * 4 + word


READ = OPEN + wrapper(6, 11) + wrapper(7, 21)
READ += selector_word(7, 8) + selector_word(6, 7) + OPEN * 4
S = READ + F_INVERSE + READ + F + F + T
WRITE = S * 10
S_INVERSE = inverse(S)
UNCOMPUTE = inverse(WRITE)

# Six-place chronological word C14^2 C45 C14^3 C16^4 C14 C16.
MODULE = ((0, 3),) * 2 + ((3, 4),) + ((0, 3),) * 3
MODULE += ((0, 5),) * 4 + ((0, 3), (0, 5))


def copy_modules(source, target):
    modules = []
    for p in range(5):
        q = (p + 1) % 5
        places = (source + 2 * p, source + 2 * p + 1,
                  source + 2 * q, source + 2 * q + 1,
                  target + 2 * p, target + 2 * p + 1)
        modules.append(tuple((places[i], places[j]) for i, j in MODULE))
    return tuple(modules)


COPY_MODULES = tuple((copy_modules(11, 31 + 20 * stage),
                      copy_modules(21, 41 + 20 * stage)) for stage in range(3))
COPIES = tuple(tuple(edge for modules in stage for module in modules for edge in module)
               for stage in COPY_MODULES)
CYCLES = tuple(WRITE + copier + UNCOMPUTE for copier in COPIES)
RELOADS = (tuple((i, 91 + i) for i in range(5)),
           tuple((i, 96 + i) for i in range(5)))
INVERSE_CYCLES = tuple(inverse(cycle) for cycle in CYCLES)
PROGRAM = ()
for _stage in range(3):
    if _stage:
        PROGRAM += tuple(("SWAP", i, j) for i, j in RELOADS[_stage - 1])
    PROGRAM += tuple(("C", i, j) for i, j in CYCLES[_stage])
INVERSE_PROGRAM = tuple(operation for kind, i, j in reversed(PROGRAM)
                        for operation in [(kind, i, j)] * (4 if kind == "C" else 1))


def source_phase(index):
    index %= 9
    if index == 0:
        return ZERO, (2, 0, 0, 0), ZERO
    power = index if index <= 4 else index - 4
    r = rotate(ONE, power)
    u, w = sub(ONE, r), add(ONE, r)
    return (u, w, ZERO) if index <= 4 else (ZERO, w, u)


def input_state(source, clock):
    q = rotate(J, clock)
    return source_phase(source) + (q, neg(q))


def bank_state(label):
    assert label is None or 0 <= label < 5
    bank = ()
    for p in range(5):
        value = rotate(B, int(p == label))
        bank += (neg(value), value)
    return bank


def final_labels(source, clock):
    assert source in (0, 1)
    return (-clock) % 5, (-(clock + (1, 8)[source])) % 5


def event_schedule(source):
    assert source in (0, 1)
    return ((0, 0), (1, 1), (9, 0)) if source == 0 else ((0, 1), (8, 0), (9, 1))


def state_formula(parameters, stage, source, clock, selector, work_labels, archive_labels):
    assert len(parameters) == 3 and stage in range(3)
    assert selector in range(3) and len(work_labels) == 2 and len(archive_labels) == 6
    tokens = tuple(U if i == selector else ZERO for i in range(3))
    state = input_state(source, clock) + (ZERO,) + tokens + (J, ZERO)
    for label in work_labels + archive_labels:
        state += bank_state(label)
    # Previous prepared inputs are parked, intact, by the two fixed reloads.
    queued = ((1, 2), (0, 2), (0, 1))[stage]
    for index in queued:
        state += input_state(*parameters[index])
    assert len(state) == 101
    return state


def archives(parameters, completed):
    labels = ()
    for stage, (source, clock) in enumerate(parameters):
        labels += final_labels(source, clock) if stage < completed else (None, None)
    return labels


def ready_formula(parameters, stage, completed):
    source, clock = parameters[stage]
    return state_formula(parameters, stage, source, clock, 0, (None, None),
                         archives(parameters, completed))


def write_formula(parameters, stage, tick, read=None, copied=None):
    source, clock = parameters[stage]
    cutoff = (tick, 1 if read is None else read)
    marks = sum(event <= cutoff for event in event_schedule(source))
    pair = final_labels(source, clock)
    labels = tuple(pair[i] if marks > i else None for i in range(2))
    archive_labels = archives(parameters, stage) if copied is None else copied
    return state_formula(parameters, stage, source + tick + (1 if read is None else -read),
                         clock + tick + int(read is None), marks % 3, labels, archive_labels)


def read_bank(state, base):
    absent = (neg(B), B)
    present = (neg(rotate(B)), rotate(B))
    marks = []
    for p in range(5):
        pair = tuple(state[base + 2 * p:base + 2 * p + 2])
        assert pair in (absent, present), (base, p, "invalid archive pair")
        if pair == present:
            marks.append(p)
    assert len(marks) <= 1
    return marks[0] if marks else None


def read_archives(state):
    """Only the six current archive banks enter this decoder."""
    labels = tuple(read_bank(state, 31 + 10 * i) for i in range(6))
    decoded = []
    for pa, pb in zip(labels[::2], labels[1::2]):
        assert pa is not None and pb is not None
        difference = (pa - pb) % 5
        assert difference in (1, 3)
        decoded.append((0 if difference == 1 else 1, (-pa) % 5))
    return labels, tuple(decoded)


def check_complete(engine, state, expected, invariant, context):
    assert len(state) == len(expected) == 101
    assert engine.decode(state) == expected, context
    assert engine.invariants(state) == invariant, context


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("ascii")


def local_copier_audit(engine):
    """40 cases: three six-place cases and five marks, each at five rotations."""
    start = engine.contacts
    local_cases = bank_cases = module_boundaries = 0
    for rotation in range(5):
        pair = lambda phase: (neg(rotate(B, rotation + phase)), rotate(B, rotation + phase))
        for source_phase_, neighbour_phase, accepted_expected in ((0, 0, 10), (1, 0, 6), (0, 1, 5)):
            initial = pair(source_phase_) + pair(neighbour_phase) + pair(0)
            expected = pair(source_phase_) + pair(neighbour_phase) + pair(source_phase_)
            state = engine.encode(initial)
            invariant = engine.invariants(state)
            assert engine.apply_counted(state, MODULE) == accepted_expected
            assert engine.decode(state) == expected and engine.invariants(state) == invariant
            engine.apply(state, inverse(MODULE))
            assert engine.decode(state) == initial and engine.invariants(state) == invariant
            local_cases += 1
        for label in range(5):
            rotated = lambda bank: tuple(rotate(value, rotation) for value in bank)
            source = rotated(bank_state(label))
            initial = source + rotated(bank_state(None))
            state = engine.encode(initial)
            invariant = engine.invariants(state)
            accepted = 0
            modules = copy_modules(0, 10)
            for p, module in enumerate(modules):
                accepted += engine.apply_counted(state, module)
                target = rotated(bank_state(label if p >= label else None))
                assert engine.decode(state) == source + target
                assert engine.invariants(state) == invariant
                module_boundaries += 1
            assert accepted == 41
            word = tuple(edge for module in modules for edge in module)
            engine.apply(state, inverse(word))
            assert engine.decode(state) == initial and engine.invariants(state) == invariant
            bank_cases += 1
    assert (local_cases, bank_cases, module_boundaries) == (15, 25, 125)
    assert engine.contacts - start == 8400
    return local_cases + bank_cases


def boundary_audit(engine):
    """Three declared boundary controls, separate from the 40 positive cases."""
    start = engine.contacts
    pair = lambda phase: (neg(rotate(B, phase)), rotate(B, phase))
    # The four addressed phases0011 end2112. The other two entries stay fixed.
    initial = pair(0) + pair(0) + pair(1)
    expected = (neg(rotate(B, 2)), B, neg(B), rotate(B),
                neg(rotate(B)), rotate(B, 2))
    state = engine.encode(initial)
    invariant = engine.invariants(state)
    engine.apply(state, MODULE)
    assert engine.decode(state) == expected and engine.invariants(state) == invariant
    assert engine.decode(state) != initial  # Not an arbitrary occupied-target writer.
    engine.apply(state, inverse(MODULE))
    assert engine.decode(state) == initial and engine.invariants(state) == invariant

    modules = copy_modules(0, 10)
    word = tuple(edge for module in modules for edge in module)
    initial = bank_state(None) * 2
    state = engine.encode(initial)
    invariant = engine.invariants(state)
    assert engine.apply_counted(state, word) == 50
    assert engine.decode(state) == initial and engine.invariants(state) == invariant
    engine.apply(state, inverse(word))
    assert engine.decode(state) == initial and engine.invariants(state) == invariant

    initial = bank_state(0) + bank_state(None)
    state = engine.encode(initial)
    invariant = engine.invariants(state)
    engine.apply(state, word)
    copied = bank_state(0) * 2
    assert engine.decode(state) == copied
    engine.apply(state, word)
    assert engine.decode(state) != initial  # This K is not an involution.
    assert engine.decode(state) != copied
    assert engine.invariants(state) == invariant
    engine.apply(state, inverse(word) * 2)
    assert engine.decode(state) == initial and engine.invariants(state) == invariant
    assert engine.contacts - start == 960
    return 3


def main():
    if sys.flags.optimize or not __debug__:
        raise SystemExit("Integrity failure: assertions must remain enabled")
    assert len(READ) == 261 and len(S) == 535 and len(WRITE) == 5350
    assert len(UNCOMPUTE) == 21400 and UNCOMPUTE == S_INVERSE * 10
    assert len(MODULE) == 12 and all(len(word) == 120 for word in COPIES)
    assert all(len(word) == 26870 for word in CYCLES)
    assert all(len(word) == 107480 for word in INVERSE_CYCLES)
    split_step = S[:1] + S[1:261] + S[261:269] + S[269:270] + S[270:530] + S[530:535]
    assert split_step == S and split_step * 10 == WRITE
    assert len(PROGRAM) == 80620 and len(INVERSE_PROGRAM) == 322450
    assert sum(kind == "C" for kind, _, _ in PROGRAM) == 80610
    assert sum(kind == "C" for kind, _, _ in INVERSE_PROGRAM) == 322440
    inverse_blocks = ()
    for stage in range(2, -1, -1):
        inverse_blocks += tuple(("C", i, j) for i, j in INVERSE_CYCLES[stage])
        if stage:
            inverse_blocks += tuple(("SWAP", i, j) for i, j in reversed(RELOADS[stage - 1]))
    assert INVERSE_PROGRAM == inverse_blocks
    word_bytes = Path(__file__).with_name("WORD535.txt").read_bytes()
    assert sha256(word_bytes).hexdigest() == WORD_SHA256
    literal = tuple((int(i) - 1, int(j) - 1)
                    for i, j in re.findall(r"C\((\d+),(\d+)\)", word_bytes.decode("ascii")))
    assert literal == S
    assert all(0 <= i < 31 and 0 <= j < 31 and i != j for i, j in S)
    for stage, word in enumerate(COPIES):
        allowed = set(range(11, 31)) | set(range(31 + 20 * stage, 51 + 20 * stage))
        assert all(i in allowed and j in allowed and i != j for i, j in word)
        # These supports imply literal, every-primitive retention of every
        # previously completed permanent archive, not just boundary equality.
        assert all(i < 31 or i >= 31 + 20 * stage for edge in word for i in edge)
    assert RELOADS == (tuple((i, 91 + i) for i in range(5)),
                       tuple((i, 96 + i) for i in range(5)))

    engine = ExactContacts()
    # Explicit diagonal and refused edge cases are not mistaken for period 5.
    for a, b in ((ZERO, ZERO), (B, B), (ZERO, ONE), (neg(B), B)):
        ia, ib = engine.intern(a), engine.intern(b)
        engine.certify(ia, ib)
    local_cases = local_copier_audit(engine)
    boundary_cases = boundary_audit(engine)
    source = engine.encode(source_phase(0))
    assert len({source_phase(i) for i in range(9)}) == 9
    for phase in range(9):
        assert engine.decode(source) == source_phase(phase)
        engine.apply(source, F)
        assert engine.decode(source) == source_phase(phase + 1)
    assert engine.contacts == 9378 and engine.swaps == 0

    alphabet = tuple(product(range(2), range(5)))
    inputs = tuple(product(alphabet, repeat=3))
    preparations = tuple(ready_formula(parameters, 0, 0) for parameters in inputs)
    assert len(inputs) == len(set(preparations)) == 1000
    auxiliary = {state[5:91] for state in preparations}
    assert len(auxiliary) == 1 and len(next(iter(auxiliary))) == 86
    assert sum(map(account, next(iter(auxiliary)))) == 248
    assert all(sum(map(account, input_state(*item))) == 14 for item in alphabet)
    varying = tuple(i for i in range(101) if len({state[i] for state in preparations}) > 1)
    assert varying == (0, 1, 3, 4, 91, 92, 94, 95, 96, 97, 99, 100)
    invariant = engine.invariants(engine.encode(preparations[0]))
    assert invariant[:2] == (290, (8, 0, 0, 0))
    assert invariant[2] == (108, 0, -74, -74)
    assert all(engine.invariants(engine.encode(state)) == invariant for state in preparations)

    start_contacts, start_swaps = engine.contacts, engine.swaps
    read_count = write_steps = uncompute_steps = copy_boundaries = 0
    copies = cycles = reloads = events = inverses = 0
    histories, decoded_inputs = set(), set()
    endpoint_digest, decoded_digest = sha256(), sha256()
    for parameters, initial in zip(inputs, preparations):
        state = engine.encode(initial)
        case_contacts, case_swaps = engine.contacts, engine.swaps
        for stage in range(3):
            if stage:
                for i, j in RELOADS[stage - 1]:
                    engine.swap(state, i, j)
                check_complete(engine, state, ready_formula(parameters, stage, stage),
                               invariant, (parameters, stage, "reload"))
                reloads += 1
            source_label, clock_label = parameters[stage]
            schedule = event_schedule(source_label)
            event_selectors = []
            for tick in range(10):
                # Split at actual read openings and completions. Concatenation
                # is exactly S; no endpoint replaces any trajectory segment.
                for read, onset, completion in ((0, 0, 261), (1, 269, 530)):
                    assert engine.values[state[G]] == ZERO
                    engine.apply(state, S[onset:onset + 1])
                    active = (tick, read) in schedule
                    assert engine.values[state[G]] == (U if active else ZERO)
                    if active:
                        selector = tuple(engine.values[i] for i in state[6:9])
                        assert selector in ((U, ZERO, ZERO), (ZERO, U, ZERO), (ZERO, ZERO, U))
                        event_selectors.append(selector.index(U))
                        events += 1
                    engine.apply(state, S[onset + 1:completion])
                    check_complete(engine, state, write_formula(parameters, stage, tick, read),
                                   invariant, (parameters, stage, tick, read, "read"))
                    read_count += 1
                    if read == 0:
                        engine.apply(state, S[261:269])
                engine.apply(state, S[530:535])
                check_complete(engine, state, write_formula(parameters, stage, tick),
                               invariant, (parameters, stage, tick, "write step"))
                write_steps += 1
            assert event_selectors == [0, 1, 2]
            pair = final_labels(source_label, clock_label)
            copied = list(archives(parameters, stage))
            for bank, modules in enumerate(COPY_MODULES[stage]):
                accepted = 0
                for p, module in enumerate(modules):
                    accepted += engine.apply_counted(state, module)
                    copied[2 * stage + bank] = pair[bank] if p >= pair[bank] else None
                    check_complete(engine, state,
                                   write_formula(parameters, stage, 9, copied=tuple(copied)),
                                   invariant, (parameters, stage, bank, p, "copy module"))
                    copy_boundaries += 1
                assert accepted == 41
                assert copied[2 * stage + bank] == pair[bank]
                copies += 1
            assert tuple(copied) == archives(parameters, stage + 1)
            for remaining in range(9, -1, -1):
                engine.apply(state, S_INVERSE)
                expected = (write_formula(parameters, stage, remaining - 1, copied=tuple(copied))
                            if remaining else ready_formula(parameters, stage, stage + 1))
                check_complete(engine, state, expected, invariant,
                               (parameters, stage, remaining, "uncompute step"))
                uncompute_steps += 1
            assert engine.decode(state)[:31] == input_state(*parameters[stage]) + initial[5:31]
            assert engine.contacts - case_contacts == 26870 * (stage + 1)
            cycles += 1
        assert engine.contacts - case_contacts == 80610 and engine.swaps - case_swaps == 10
        endpoint = engine.decode(state)
        labels, decoded = read_archives(endpoint)
        assert decoded == parameters
        histories.add(labels)
        decoded_inputs.add(decoded)
        endpoint_digest.update(compact([parameters, endpoint]))
        decoded_digest.update(compact([parameters, labels, decoded]))
        # Reverse the ENTIRE literal mixed program: inverse(C) is four C's,
        # including when that C belonged to the forward uncompute expansion.
        # No algebraic shortening of the 322440 inverse contacts occurs.
        for stage in range(2, -1, -1):
            engine.apply(state, INVERSE_CYCLES[stage])
            check_complete(engine, state, ready_formula(parameters, stage, stage),
                           invariant, (parameters, stage, "inverse cycle"))
            if stage:
                for i, j in reversed(RELOADS[stage - 1]):
                    engine.swap(state, i, j)
                check_complete(engine, state, ready_formula(parameters, stage - 1, stage),
                               invariant, (parameters, stage, "inverse reload"))
        check_complete(engine, state, initial, invariant, (parameters, "complete inverse"))
        assert engine.contacts - case_contacts == 403050 and engine.swaps - case_swaps == 20
        inverses += 1
    assert (read_count, write_steps, uncompute_steps, copy_boundaries) == (60000, 30000, 30000, 30000)
    assert (copies, cycles, reloads, events, inverses) == (6000, 3000, 2000, 9000, 1000)
    assert engine.contacts - start_contacts == 403050000
    assert engine.swaps - start_swaps == 20000
    assert len(histories) == len(decoded_inputs) == 1000 and decoded_inputs == set(inputs)
    result = {
        "status": "PASS", "scope": "NON-CANONICAL / L1 / candidate-C",
        "study": "three successive write-copy-uncompute cycles on one working core",
        "slots": 101, "complete_account": 290, "complete_sum": [8, 0, 0, 0],
        "complete_hermitian_j_basis": list(invariant[2]),
        "common_auxiliary_slots": 86, "common_auxiliary_account": 248,
        "prepared_input_addresses": 15, "varying_initial_addresses": 12,
        "prepared_input_account": 42, "ordered_triples": 1000,
        "working_banks": 2, "permanent_archive_banks": 6,
        "working_bank_account": 60, "permanent_archive_account": 180,
        "write_contacts": 5350, "two_copy_contacts": 120, "uncompute_contacts": 21400,
        "cycle_contacts": 26870, "forward_contacts_each": 80610, "forward_swaps_each": 10,
        "inverse_contacts_each": 322440, "inverse_swaps_each": 10,
        "full_read_checkpoints": read_count, "full_write_step_checkpoints": write_steps,
        "full_uncompute_step_checkpoints": uncompute_steps,
        "full_copy_module_checkpoints": copy_boundaries, "whole_bank_copies": copies,
        "complete_working_core_restorations": cycles, "full_reload_checkpoints": reloads,
        "write_events": events, "complete_inverses": inverses,
        "archive_histories": len(histories), "decoded_triples": len(decoded_inputs),
        "trajectory_contact_applications": engine.contacts - start_contacts,
        "trajectory_swap_applications": engine.swaps - start_swaps,
        "local_copier_cases": local_cases, "local_copier_contacts_excluded": 8400,
        "boundary_control_cases": boundary_cases, "boundary_control_contacts_excluded": 960,
        "source_orbit_contacts_excluded": 18,
        "certified_ordered_pair_maps": sum(map(len, engine.transitions)),
        "certified_pair_orbits": engine.certified_orbits,
        "interned_exact_values": len(engine.values),
        "labelled_residue_vector": list(invariant[3]),
        "word535_sha256": WORD_SHA256,
        "complete_program_sha256": sha256(compact(PROGRAM)).hexdigest(),
        "complete_inverse_program_sha256": sha256(compact(INVERSE_PROGRAM)).hexdigest(),
        "complete_endpoint_sha256": endpoint_digest.hexdigest(),
        "decoded_history_sha256": decoded_digest.hexdigest(),
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
