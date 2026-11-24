#!/usr/bin/env python3
"""Exact publication replay: funded two-pass source renewal on 64h+3.

NON-CANONICAL / L1. No runtime input, file, network or random source.
The contact word does not call the observational arithmetic oracle.
"""

from hashlib import sha256
from json import dumps
from math import gcd


if not __debug__:
    raise RuntimeError("This replay requires assertions; do not use -O.")

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
POWERS = (ONE, (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1))
OLD = (POWERS[1], (1, 0, 0, 1))

# The loader consists only of these four declared integral affine maps.
# Rows are (coefficient of h, constant term), in the rho basis.
DONORS = (
    ((1600, 832, 448, 320), (84, 46, 26, 18)),
    ((-192, 0, 192, 0), (-6, 0, 6, -4)),
    ((648, 516, 204, -108), (34, 26, 10, -6)),
    ((-288, 0, 0, 288), (-12, 0, 0, 16)),
)

# Independently expanded closed final residues, not obtained by executing C.
SPENT = (
    ((832, 992, 352, 224), (42, 53, 21, 13)),
    ((0, -384, 384, 0), (4, -14, 18, -2)),
    ((642, 132, -180, -474), (33, 6, -10, -25)),
    ((576, 576, 576, 1152), (30, 28, 28, 58)),
)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k * x for x in a)


def mul(a, b):
    # Independent cyclic convolution, followed by 1+rho+...+rho^4=0.
    t = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            t[(i + j) % 5] += x * y
    return tuple(t[i] - t[4] for i in range(4))


def sigma(a, d):
    t = [0] * 5
    for i, x in enumerate(a):
        t[i * d % 5] += x
    return tuple(t[i] - t[4] for i in range(4))


def u(d):
    return sub(ONE, POWERS[d % 5])


def j(d):
    return add(ONE, POWERS[d % 5])


def q(a):
    s = sum(a)
    t = 5 * sum(x * x for x in a) - s * s
    assert t % 2 == 0
    return t // 2


def norm(a):
    return mul(a, sigma(a, 4))


def eps(a):
    return sum(a) % 5


def total(state):
    s = ZERO
    h = ZERO
    for a in state:
        s = add(s, a)
        h = add(h, norm(a))
    return s, h, sum(map(q, state)), tuple(map(eps, state))


def affine(row, h):
    return add(scale(h, row[0]), row[1])


def ready(n, d):
    return [scale(n, u(d)), scale(n, sub(scale(12, ONE), j(d))), scale(2, j(d))]


def load(h, d):
    assert h >= 0 and d in (1, 2, 3, 4)
    state = ready(64 * h + 3, d) + [ZERO] * 26
    state.extend(sigma(affine(row, h), d) for row in DONORS)
    state.extend(OLD)
    assert len(state) == 35
    return state


def word(d):
    # Edges and powers depend on the supplied initial chart only, not h or state.
    result = []
    for current, start, donor in ((d, 3, 29), (4 * d % 5, 16, 31)):
        result.extend(((0, 1, current), (0, 2, current)))
        e = current
        for offset in range(13):
            e = 2 * e % 5
            result.append((0, start + offset, e))
        result.extend(((1, donor, current), (2, donor + 1, current)))
    assert len(result) == 34
    assert sum(e for _, _, e in result) == 85
    return tuple(result)


class Native:
    def __init__(self):
        self.calls = self.enabled = self.refused = 0

    def c(self, state, left, right):
        self.calls += 1
        a, b = state[left], state[right]
        if any((x - y) % 2 for x, y in zip(a, b)):
            self.refused += 1
            return
        self.enabled += 1
        s = tuple((x + y) // 2 for x, y in zip(a, b))
        t = tuple((x - y) // 2 for x, y in zip(a, b))
        # Literal native multiplication by rho, independent of mul().
        rt = (-t[3], t[0] - t[3], t[1] - t[3], t[2] - t[3])
        aa, bb = add(s, rt), sub(s, rt)
        assert add(a, b) == add(aa, bb)
        assert add(norm(a), norm(b)) == add(norm(aa), norm(bb))
        assert q(a) + q(b) == q(aa) + q(bb)
        assert (eps(a), eps(b)) == (eps(aa), eps(bb))
        state[left], state[right] = aa, bb

    def power(self, state, entry):
        left, right, exponent = entry
        assert left != right and 1 <= exponent <= 4
        enabled_before = self.enabled
        for _ in range(exponent):
            self.c(state, left, right)
        count = self.enabled - enabled_before
        assert count in (0, exponent)
        return count == exponent


def v2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def read_current(state, start):
    active = state[0]
    m = gcd(*active)
    assert m > 0 and m % 2 == 1
    shape = tuple(x // m for x in active)
    matches = [d for d in range(1, 5) if shape == u(d)]
    assert len(matches) == 1
    records = state[start:start + 13]
    depth = 0
    while depth < 13 and records[depth] != ZERO:
        depth += 1
    assert depth < 13 and all(a == ZERO for a in records[depth:])
    return m, matches[0], depth


def records(n, d, depth):
    x = 3 * n + 1
    m = x // (2 ** depth)
    assert v2(x) == depth and x == 2 ** depth * m
    out = []
    for s in range(1, depth + 1):
        e = 2 ** s * d % 5
        out.append(scale(2 ** (depth - s) * m, mul(u(e), u(e))))
    return out + [ZERO] * (13 - depth)


def occupied(n, d, m, target_chart):
    return [
        scale(m, u(target_chart)),
        scale(2 * n, sub(scale(3, j(d)), POWERS[d])),
        add(scale(3 * n, mul(u(d), u(d))), mul(j(d), j(d))),
    ]


def boundary(h, d, stage, renewed):
    # Whole-state closed oracle, evaluated only by audits, never by the word.
    n0, n1, n2 = 64 * h + 3, 96 * h + 5, 18 * h + 1
    d1, d2 = 4 * d % 5, 3 * d % 5
    assert (3 * n0 + 1) // 2 == n1
    assert (3 * n1 + 1) // 16 == n2
    if stage == 1:
        source = ready(n1, d1) if renewed else occupied(n0, d, n1, d1)
        raw = source + records(n0, d, 1) + [ZERO] * 13
        bank = SPENT[:2] + DONORS[2:] if renewed else DONORS
    else:
        source = ready(n2, d2) if renewed else occupied(n1, d1, n2, d2)
        raw = source + records(n0, d, 1) + records(n1, d1, 4)
        bank = SPENT if renewed else SPENT[:2] + DONORS[2:]
    raw.extend(sigma(affine(row, h), d) for row in bank)
    raw.extend(OLD)
    assert len(raw) == 35
    return raw


def prefix_boundary(h, d, stage, second):
    # A separate closed description of each of the two prefix outputs.
    state = load(h, d) if stage == 1 else boundary(h, d, 1, True)
    n = 64 * h + 3 if stage == 1 else 96 * h + 5
    e = d if stage == 1 else 4 * d % 5
    state[0] = scale(6 * n, u(e))
    state[1] = scale(2 * n, sub(scale(3, j(e)), POWERS[e]))
    if second:
        state[0] = scale(3 * n + 1, u(2 * e))
        state[2] = add(scale(3 * n, mul(u(e), u(e))), mul(j(e), j(e)))
    return state


def audit_donor(h, d, index, entry, state):
    stage = 1 if index < 17 else 2
    n = 96 * h + 5 if stage == 1 else 18 * h + 1
    target_chart = (4 if stage == 1 else 3) * d % 5
    left, right, exponent = entry
    target = ready(n, target_chart)[left]
    a, donor = state[left], state[right]
    delta = sub(donor, a)
    assert all(x % 2 == 0 for x in delta)
    quotient = tuple(x // 2 for x in delta)
    assert mul(u(exponent), quotient) == sub(target, a)
    return target, sub(add(a, donor), target)


def audit_accounts(h, state, final):
    bank = sum(q(a) for a in state[29:33])
    if final:
        assert bank == 5851540 * h * h + 585660 * h + 14798
        assert sum(q(a) for a in state[3:29]) == 551340 * h * h + 60300 * h + 1650
        assert sum(q(a) for a in state[:3]) == 260 * (18 * h + 1) ** 2 + 12
    else:
        assert bank == 5422160 * h * h + 555480 * h + 14368
        assert tuple(eps(a) for a in state[29:33]) == (4, 1, 4, 4)
        assert all(all(x % 2 == 0 for x in a) for a in state[29:33])
    assert sum(q(a) for a in state[:33]) == 6487120 * h * h + 655320 * h + 16720


def main():
    native = Native()
    digest = sha256()
    cases = 0
    corpus = [("dense", h) for h in range(1024)]
    corpus.extend(("large", 2 ** k + c) for k in (32, 64, 128, 256) for c in (-1, 0, 1, 7))
    for tag, h in corpus:
        reference = None
        for d in range(1, 5):
            state = load(h, d)
            initial = state.copy()
            invariants = total(initial)
            audit_accounts(h, state, False)
            program = word(d)
            trace = []
            before = (native.calls, native.enabled, native.refused)
            first_archive = None
            for index, entry in enumerate(program):
                reset_expected = None
                if index in (15, 16, 32, 33):
                    reset_expected = audit_donor(h, d, index, entry, state)
                enabled = native.power(state, entry)
                if reset_expected is not None:
                    assert enabled
                    assert (state[entry[0]], state[entry[1]]) == reset_expected
                if index in (0, 1, 17, 18):
                    assert enabled
                    assert state == prefix_boundary(h, d, 1 if index < 17 else 2, index in (1, 18))
                if 2 <= index <= 14:
                    assert enabled == (index == 2)
                if 19 <= index <= 31:
                    assert enabled == (index <= 22)
                assert tuple(state[33:]) == OLD
                if first_archive is not None:
                    assert state[3:16] == first_archive
                trace.append(tuple(state[:33]))
                if index in (14, 16, 31, 33):
                    stage = 1 if index < 17 else 2
                    renewed = index in (16, 33)
                    assert state == boundary(h, d, stage, renewed)
                    assert total(state) == invariants
                    if stage == 1:
                        assert read_current(state, 3) == (96 * h + 5, 4 * d % 5, 1)
                        first_archive = state[3:16].copy()
                    else:
                        assert read_current(state, 16) == (18 * h + 1, 3 * d % 5, 4)
            audit_accounts(h, state, True)
            if reference is None:
                reference = trace
            else:
                for base, actual in zip(reference, trace):
                    assert actual == tuple(sigma(a, d) for a in base)
            if h == 0:
                assert [read_current(boundary(h, d, s, True), 3 if s == 1 else 16)[0] for s in (1, 2)] == [5, 1]
                assert sum(q(a) for a in initial[29:31]) == 10504
                assert sum(q(a) for a in boundary(h, d, 1, True)[29:31]) == 5969
                assert sum(q(a) for a in state[29:33]) == 14798
            digest.update((dumps([tag, h, d, state], separators=(",", ":")) + "\n").encode("ascii"))
            for left, right, exponent in reversed(program):
                native.power(state, (left, right, 5 - exponent))
            assert state == initial
            assert total(state) == invariants
            assert (native.calls - before[0], native.enabled - before[1], native.refused - before[2]) == (170, 65, 105)
            cases += 1
    assert cases == 4160
    assert (native.calls, native.enabled, native.refused) == (707200, 270400, 436800)
    print("CONTACT-FUNDED-TWO-PASS-REPLAY v1")
    print("scope: n=64h+3,h>=0; supplied initial chart; depths (1,4)")
    print("loader: four fixed integral affine donors; no T,v,m call; PASS")
    print("dense h=0..1023: 4096 complete two-pass cases; PASS")
    print("large h near 2^32,2^64,2^128,2^256: 64 complete cases; PASS")
    print("native word: 34 powered contacts, 85 primitives, 33 core slots; PASS")
    print("two ready boundaries: actual occupied-source renewal; PASS")
    print("literal archives: both new batches and two occupied old slots; PASS")
    print("Galois covariance: all 34 corresponding macro boundaries; PASS")
    print("conservation: sum, real-quadratic account, Q, labelled residues; PASS")
    print("complete native inverses: 4160; PASS")
    print("primitive calls: 707200 enabled: 270400 refused: 436800")
    print("h=0: 3->5->1; initial bank 14368; final bank 14798; records 1650")
    print("complete-output fingerprint SHA-256: " + digest.hexdigest())
    print("scope: fixed itinerary compiled into loading and schedule; no autonomous selector")
    print("scope: no indefinite renewal, minimum-funding or Collatz-convergence claim")


if __name__ == "__main__":
    main()
