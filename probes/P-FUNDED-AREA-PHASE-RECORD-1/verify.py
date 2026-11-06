#!/usr/bin/env python3
"""Frozen exact L1 audit: funded area, two quadratic records, Weyl path.

A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
Only Python standard library; no floats, files, network or imported verifier.
The alternate transition is a same-author cross-check, not a blind agent.
"""
from hashlib import sha256
from itertools import product
from math import comb, isqrt


class Falsifier(Exception):
    pass


def need(ok, label):
    if not ok:
        raise Falsifier(label)


# State: q,p,u,v,b,sigma,eta,c. Requested letters: (axis, epsilon).
LETTERS = ((0, 1), (1, 1), (0, -1), (1, -1))
IDENTITY = (tuple(range(5)), (0,) * 5)
RAW_BOUND = 12
WORD_DEPTH = 8
WORD_STOCK = 2 * WORD_DEPTH**2 + 2 * WORD_DEPTH**4


def h0(s):
    return sum(x * x for x in s[:4])


def total(s):
    return h0(s) + s[4]


def ready(stock, eta=1, references=(1, -1)):
    return (0, 0, references[0], references[1], stock, 1, eta, 0)


def gate(s, axis, epsilon):
    """Full funded permutation, including the direction-reflecting rejection."""
    t = list(s)
    h = epsilon * s[5]
    if axis == 0:
        t[0] += h
    else:
        t[1] += h
        t[2] += h * s[0]
        t[3] += h * s[0]
    delta = h0(t) - h0(s)
    if s[4] >= delta:
        t[4] -= delta
        return tuple(t)
    t = list(s)
    t[5] = -t[5]
    return tuple(t)


def alternate_gate(s, axis, epsilon):
    """Expanded-work formula, not a call to the primary proposal or h0."""
    q, p, u, v, bank, direction, orient, clock = s
    h = epsilon * direction
    if axis == 0:
        work = 2 * h * q + 1
        candidate = (q + h, p, u, v)
    else:
        work = 2 * h * p + 1 + 2 * h * q * (u + v) + 2 * q * q
        candidate = (q, p + h, u + h * q, v + h * q)
    if work > bank:
        return (q, p, u, v, bank, -direction, orient, clock)
    return candidate + (bank - work, direction, orient, clock)


def letter(clock, eta):
    return ((0, 1), (1, eta), (0, -1), (1, -eta))[clock]


def advance(s):
    t = list(gate(s, *letter(s[7], s[6])))
    t[7] = (s[7] + 1) % 4
    return tuple(t)


def retreat(s):
    t = list(s)
    t[7] = (s[7] - 1) % 4
    axis, eps = letter(t[7], s[6])
    return gate(tuple(t), axis, -eps)


def invariant_pair(s, t, label):
    need(t[4] >= 0 and total(t) == total(s), label + ': energy or stock')
    need(t[2] - t[3] == s[2] - s[3], label + ': reference difference')
    need(t[6] == s[6], label + ': program orientation')
    du, dv = t[2] - s[2], t[3] - s[3]
    need(du == dv, label + ': unequal reference increments')
    difference = t[2]**2 - t[3]**2 - s[2]**2 + s[3]**2
    need(difference == 2 * (s[2] - s[3]) * du,
         label + ': occupied-reference polarization')


def mono_next(op, s, t):
    """Literal action of X^dq or Z^dp on all five current basis images."""
    dq, dp = t[0] - s[0], t[1] - s[1]
    need(dq * dp == 0 and abs(dq) + abs(dp) <= 1, 'non-elementary displacement')
    images, phases = op
    if dq:
        return (tuple((k + dq) % 5 for k in images), phases)
    if dp:
        return (images, tuple((e + dp * k) % 5 for k, e in zip(images, phases)))
    return op


def follow(start, steps):
    history, op, area2 = [start], IDENTITY, 0
    for _ in range(steps):
        s, t = history[-1], advance(history[-1])
        invariant_pair(s, t, 'actual controller')
        op = mono_next(op, s, t)
        area2 += s[0] * t[1] - s[1] * t[0]
        history.append(t)
    return history, op, area2


def check_prepared(history, op, area2):
    """Geometry, actual quadratic read, and independent monomial path."""
    s = history[-1]
    need(s[2] - s[3] == 2, 'prepared reference gap')
    numerator = s[2]**2 - s[3]**2
    need(numerator % 4 == 0, 'nonintegral quadratic record')
    a = numerator // 4
    need(2 * a == area2 + s[0] * s[1], 'shoelace versus quadratic record')
    need(s[2:4] == (1 + a, -1 + a), 'reference reconstruction')
    need(s[2]**2 + s[3]**2 == 2 + 2 * a * a, 'reference work price')
    need(op[0] == tuple((k + s[0]) % 5 for k in range(5)), 'Weyl shift')
    need(op[1] == tuple((k * s[1] + a) % 5 for k in range(5)), 'Weyl phase')
    if s[0] == s[1] == 0:
        need(op == (tuple(range(5)), (a % 5,) * 5), 'closed phase')
    return a


def raw_audit():
    nstates = ngates = rejects = 0
    radius = isqrt(RAW_BOUND)
    for point in product(range(-radius, radius + 1), repeat=4):
        norm = sum(x * x for x in point)
        if norm > RAW_BOUND:
            continue
        for bank in range(RAW_BOUND - norm + 1):
            for direction, orient, clock in product((-1, 1), (-1, 1), range(4)):
                s = point + (bank, direction, orient, clock)
                nstates += 1
                for axis, eps in LETTERS:
                    t = gate(s, axis, eps)
                    need(t == alternate_gate(s, axis, eps), 'expanded gate disagreement')
                    need(gate(t, axis, -eps) == s, 'gate inverse including rejection')
                    invariant_pair(s, t, 'raw gate')
                    if s[:4] == t[:4]:
                        need(t[4] == s[4] and t[5] == -s[5], 'rejection semantics')
                        rejects += 1
                    ngates += 1
                t = advance(s)
                need(retreat(t) == s and advance(retreat(s)) == s, 'full controller inverse')
                expected = list(alternate_gate(s, *letter(clock, orient)))
                expected[7] = (clock + 1) % 4
                need(t == tuple(expected), 'expanded controller disagreement')
                invariant_pair(s, t, 'raw controller')
    print('G1 PASS raw_energy_le_12 states={} gate_checks={} rejected={}'.format(
        nstates, ngates, rejects))


def word_audit():
    nodes = closed = 0
    digest = sha256()

    def visit(s, op, area2, depth):
        nonlocal nodes, closed
        nodes += 1
        a = check_prepared([s], op, area2)
        if s[0] == s[1] == 0:
            closed += 1
        digest.update((str((depth, s, op, area2, a)) + '\n').encode('ascii'))
        if depth == WORD_DEPTH:
            return
        for axis, eps in LETTERS:
            t = gate(s, axis, eps)
            need(t[5] == 1 and t[:4] != s[:4], 'uniform stock bound failed')
            need(t == alternate_gate(s, axis, eps), 'word transition disagreement')
            invariant_pair(s, t, 'word edge')
            op2 = mono_next(op, s, t)
            a2 = area2 + s[0] * t[1] - s[1] * t[0]
            visit(t, op2, a2, depth + 1)

    visit(ready(WORD_STOCK), IDENTITY, 0, 0)
    need(nodes == sum(4**n for n in range(WORD_DEPTH + 1)), 'word coverage')
    need(closed == sum(comb(2*n, n)**2 for n in range(WORD_DEPTH//2 + 1)),
         'closed-word coverage')
    print('G2 PASS words={} integer_closed={} basis_actions={} history_sha256={}'.format(
        nodes, closed, 5 * nodes, digest.hexdigest()))


def witness_audit():
    samples = {}
    for eta in (-1, 1):
        hist, op, area2 = follow(ready(4, eta), 4)
        a = check_prepared(hist, op, area2)
        need(a == eta and hist[-1][:2] == (0, 0), 'oriented square')
        need([h0(s) for s in hist] == [2, 3, 6, 5, 4], 'four-step cost profile')
        need([s[4] for s in hist] == [4, 3, 0, 1, 2], 'four-step bank profile')
        samples[eta] = (hist, op)
        print('G3 WITNESS eta={} record={} phase_exponent={} states={}'.format(
            eta, a, op[1][0], hist))
    plus, minus = samples[1][0], samples[-1][0]
    coarse = lambda hist: [(s[0]**2+s[1]**2, s[2]**2+s[3]**2, s[4], s[5], s[7]) for s in hist]
    need(coarse(plus) == coarse(minus), 'coarse path profiles differ')
    need([(s[2]**2, s[3]**2) for s in plus] !=
         [(s[2]**2, s[3]**2) for s in minus], 'ordered costs fail to distinguish')
    need(samples[1][1] != samples[-1][1], 'opposite phase lost')
    print('G3 PASS entire coarse-energy/work histories agree; labelled reference costs do not')

    count = 0
    for eta, bank, laps in product((-1, 1), range(81), range(1, 7)):
        hist, op, area2 = follow(ready(bank, eta), 4 * laps)
        a = check_prepared(hist, op, area2)
        accepted = all(s[:4] != t[:4] for s, t in zip(hist, hist[1:]))
        need(accepted == (bank >= 2 * laps * laps + 2), 'sharp lap funding threshold')
        if accepted:
            need(a == eta * laps and hist[-1][4] == bank - 2 * laps * laps,
                 'lap record or spent stock')
        count += 1
    hist, op, area2 = follow(ready(52), 20)
    a = check_prepared(hist, op, area2)
    need(a == 5 and op == IDENTITY, 'five laps do not close phase only')
    need(hist[-1] == (0, 0, 6, 4, 2, 1, 1, 0), 'five-lap complete endpoint')
    print('G4 PASS budget_cases={} B_min(K)=2*K^2+2'.format(count))
    print('G4 WITNESS laps=5 area=5 Eplus=36 Eminus=16 bank=2 phase=identity paid_work=50')

    lost = []
    for eta in (-1, 1):
        hist, op, _ = follow(ready(4, eta, (0, 0)), 4)
        s = hist[-1]
        lost.append(((s[2]**2, s[3]**2), op))
    need(lost[0][0] == lost[1][0] == (1, 1) and lost[0][1] != lost[1][1],
         'equal-reference orientation-loss control')
    print('G5 PASS equal zero references give identical squared records and opposite phases')

    hist, op, area2 = follow(ready(3), 4)
    check_prepared(hist, op, area2)
    need(hist[-1][:2] != (0, 0), 'underfunded nominal square unexpectedly closed')
    need(any(s[:4] == t[:4] for s, t in zip(hist, hist[1:])), 'underfunded word did not reject')
    print('G5 WITNESS underfunded_B=3 endpoint={} actual_word_not_nominal'.format(hist[-1]))


def recurrence_audit():
    for eta in (-1, 1):
        start = ready(4, eta)
        s = start
        seen = {start}
        bound = 16 * (2 * isqrt(total(start)) + 1)**4
        period = None
        for k in range(1, bound + 1):
            s = advance(s)
            need(total(s) == total(start), 'recurrence cost')
            if s in seen:
                need(s == start, 'non-permutation transient detected')
                period = k
                break
            seen.add(s)
        need(period is not None, 'finite-energy return bound')
        print('G6 PASS autonomous_B=4 eta={} exact_period={} full_ready_return'.format(eta, period))


def main():
    try:
        raw_audit()
        word_audit()
        witness_audit()
        recurrence_audit()
    except Falsifier as exc:
        print('FALSIFIER: ' + str(exc))
        print('AUDIT FAIL')
        return 0
    print('BOUNDARY selected integer comparison; algebraic path character only; no native U, SI or physical action')
    print('AUDIT PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
