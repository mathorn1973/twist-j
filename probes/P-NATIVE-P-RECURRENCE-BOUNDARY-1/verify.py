#!/usr/bin/env python3
"""Exact audit of the frozen native recurrence/correction contract.

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.
SPDX-License-Identifier: Apache-2.0
No scientific execution is permitted before the public complete code pin.
"""

import hashlib
import itertools
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
P = 5
ZERO = (0,) * 6
T = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
SHEETS = (
    ((0, 4), (0, 4), (2, 3), (0, 4), (2, 3)),
    ((0, 4), (1, 2), (1, 2), (0, 1), (2, 3)),
)
GATE = "CUSTODY"


def insist(ok, description):
    if not ok:
        raise AssertionError(description)


def gate(name, detail):
    global GATE
    GATE = name
    print("PASS " + name + " " + detail, flush=True)


def mod(x):
    return tuple(a % P for a in x)


def add(x, y):
    return mod(a + b for a, b in zip(x, y))


def sub(x, y):
    return mod(a - b for a, b in zip(x, y))


def letter(i, x):
    p1, p4, p1p, p4p, q, r = x
    if i == 0:
        return p4, p1, p4p, p1p, q, r
    if i == 1:
        return mod((-p1p, -p4p, -p1, -p4, -q, -r))
    if i == 2:
        return mod((2-p1p, 1+r-p4p, 2-p1, 1-r-p4, 1-q, -r))
    if i == 3:
        return mod((2-p1, 1-p4, 3-p1p, 4-p4p, 1-q, 1-r))
    if i == 4:
        return mod((2-p1, 1-p4, 3-p1p, 4-p4p, 2-q, 1-r))
    raise ValueError("unknown letter")


def shift(x, amount):
    return x[:4] + ((x[4] + amount) % 5, x[5])


def sheet(x):
    return sum(x) % 5


def theta(n):
    return n.bit_count() % 2


def free(t, x):
    return letter((sheet(x) + 2*t) % 5, x)


def corrected(t, x):
    insist(sheet(x) in (0, 4), "corrected input outside full code")
    return shift(free(t, x), -2*t)


def legal(n, x):
    phase = n % 5
    return sheet(x) in SHEETS[theta(n-phase)][phase]


def commanded(t, phase):
    insist(phase in (1, 2, 3, 4), "not a command phase")
    return 4 if t == 1 and phase in (1, 3) else 3


def micro(n, x):
    insist(legal(n, x), "illegal forward slice")
    phase = n % 5
    t = theta(n-phase)
    y = free(t, x) if phase == 0 else letter(commanded(t, phase), x)
    insist(legal(n+1, y), "forward code-image failure")
    return n+1, y


def unmicro(n, x):
    insist(n > 0 and legal(n, x), "inverse outside actual image")
    prev = n-1
    phase = prev % 5
    t = theta(prev-phase)
    if phase:
        i = commanded(t, phase)
    elif t == 0:
        i = 0 if sheet(x) == 0 else 4
    else:
        i = 2 if sheet(x) == 2 else 1
    y = letter(i, x)
    insist(legal(prev, y), "inverse code-image failure")
    return prev, y


def block(n, x):
    for _ in range(5):
        n, x = micro(n, x)
    return n, x


def balanced(a):
    return (0, 1, 2, -2, -1)[a]


def read_receiver(x):
    value = balanced(x[1])**2 - balanced(x[3])**2
    return (value > 0) - (value < 0)


def reference_h(y):
    mu, q, p, u, v, alpha, beta, tau, bank, c, direction = y
    h = (0, 1, 0, 0, -1)[mu]
    if (c, direction) not in ((0, 1), (1, -1)):
        return y
    k = h if c == 0 else -h
    price = 2*k*(p+q*(u+v)) + k*k*(1+2*q*q)
    if not 0 <= bank-price <= 3:
        return y
    return (mu, q, p+k, u+k*q, v+k*q, (alpha+k) % 5,
            beta, tau, bank-price, 1-c, -direction)


def reflect(y):
    return y[:-1] + (-y[-1],)


def reference_f(y):
    return reflect(reference_h(y))


def reference_inv(y):
    return reference_h(reflect(y))


def account(y):
    mu, q, p, u, v = y[:5]
    return q*q + p*p + u*u + v*v + 2*balanced(mu)**2 + y[8]


def custody():
    required = {"PREREG.md", "PROOF.md", "verify.py", "break.py",
                "BREAKER.md", "SOURCES.tsv"}
    seen = set()
    for line in (HERE / "CODE_SHA256SUMS").read_text(encoding="ascii").splitlines():
        digest, name = line.split("  ")
        insist(name not in seen and Path(name).name == name,
                "unsafe or duplicated custody name")
        insist(hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest,
                "pinned content hash mismatch")
        seen.add(name)
    insist(required <= seen, "incomplete code custody")
    gate("CUSTODY", "pinned specification author breaker proof and sources")


def main():
    global GATE
    custody()
    states = tuple(itertools.product(range(5), repeat=6))
    by_sheet = {z: tuple(x for x in states if sheet(x) == z) for z in range(5)}
    GATE = "RAW"
    for x in states:
        for i in range(5):
            insist(letter(i, letter(i, x)) == x, "raw involution")
        insist(letter(4, letter(3, x)) == shift(x, 1), "tau translation")
        for t in (0, 1):
            insist(sheet(free(t, x)) == T[t][sheet(x)], "selector sheet table")
    gate("RAW", "15625 states five involutions tau and both selector tables")

    GATE = "CLOCK"
    unit = tuple(tuple(int(i == j) for i in range(6)) for j in range(6))
    offsets = tuple(letter(i, ZERO) for i in range(5))
    matrices = tuple(tuple(sub(letter(i, u), offsets[i]) for u in unit)
                     for i in range(5))

    def linear(columns, v):
        return mod(sum(columns[j][i]*v[j] for j in range(6)) for i in range(6))

    for k in range(1, 257):
        lower = 3 + ((9+k-1)//k)*k
        j = 0
        while not ((1 << j) > k and (j % 2) == ((1+theta(k-1)) % 2)
                   and (1 << j)-k+1 >= lower):
            j += 1
        n = (1 << j)-k+1
        insist(theta(n-1) == theta(n+k-1) == 1, "same-bit all-k certificate")
        columns = unit
        z = (4 + 2*theta(n-1)) % 5
        swaps = 0
        for tick in range(n, n+k):
            i = (z+2*theta(tick)) % 5
            insist(i in (1, 3, 4), "synchronized letter")
            swaps += i == 1
            columns = tuple(linear(matrices[i], u) for u in columns)
            z = T[theta(tick)][z]
        wanted = tuple(mod(((-1)**k)*a for a in u) for u in unit)
        insist(columns == wanted and swaps % 2 == 0, "literal affine block")
        insist(z == (4+2*theta(n+k-1)) % 5, "block final sheet")
    gate("CLOCK", "k=1..256 explicit late same-bit certificates full 6x6 linear parts")

    GATE = "CLASS"
    admitted = []
    for mask in range(1, 32):
        domain = tuple(z for z in range(5) if mask & (1 << z))
        for d0, d1 in itertools.product(range(5), repeat=2):
            if all(sorted((T[t][z]+(d0, d1)[t]) % 5 for z in domain)
                   == list(domain) for t in (0, 1)):
                admitted.append((domain, d0, d1))
    singletons = [((z,), (z-T[0][z]) % 5, (z-T[1][z]) % 5) for z in range(5)]
    wanted = singletons + [((0, 4), 0, 3), ((0, 1), 1, 4)]
    insist(sorted(admitted) == sorted(wanted), "complete correction classification")
    gate("CLASS", "775 triples exactly 5 singleton schemes and 2 maximal pairs")

    GATE = "CORRECTED"
    selected = by_sheet[0] + by_sheet[4]
    for t in (0, 1):
        outputs = set()
        for x in selected:
            y = corrected(t, x)
            insist(sheet(y) == sheet(x), "retained control sheet")
            insist(corrected(t, y) == x, "complete corrected involution")
            outputs.add(y)
        insist(len(outputs) == len(selected) == 6250, "complete corrected bijection")
    gate("CORRECTED", "2 bits x 6250 full occupied states inverse and sheet retention")

    GATE = "MICRO"
    micro_cases = 0
    boundary_pairs = set()
    for m in (0, 20, 25, 50):
        t = theta(m)
        boundary_pairs.add((t, theta(m+5)))
        for phase in range(5):
            n = m+phase
            for z in SHEETS[t][phase]:
                for x in by_sheet[z]:
                    after = micro(n, x)
                    insist(unmicro(*after) == (n, x), "micro inverse after forward")
                    if n:
                        insist(micro(*unmicro(n, x)) == (n, x), "micro forward after inverse")
                    micro_cases += 1
        for x in selected:
            insist(block(m, x) == (m+5, corrected(t, x)), "five-tick equality")
    insist(boundary_pairs == {(0, 0), (0, 1), (1, 0), (1, 1)}, "all boundary bit pairs")
    gate("MICRO", str(micro_cases) + " full-slice cases all four boundary bit pairs 25000 block equalities")

    GATE = "RECEIVER"
    xp = (1, 1, 0, 0, 3, 0)
    xm = (1, 1, 0, 0, 2, 0)
    insist(all(xp[i] == xm[i] for i in range(6) if i != 4), "source-local input")
    insist((xp[1], xp[3]) == (xm[1], xm[3]) == (1, 0), "common occupied receiver")
    full = (
        ((1, 1, 0, 0, 3, 0), (1, 0, 3, 4, 0, 1)),
        ((2, 1, 1, 0, 1, 0), (0, 0, 4, 4, 1, 0)),
    )
    for t in (0, 1):
        yp, ym = corrected(t, xp), corrected(t, xm)
        insist((yp, ym) == full[t], "literal full pair outputs")
        insist((read_receiver(yp), read_receiver(ym)) == (1, -1), "actual receiver acquisition")
    gate("RECEIVER", "only q differs common occupied R fixed present read +1/-1 for both bits")

    GATE = "REFERENCE"
    reference_cases = 0
    for mu, direction in ((1, 1), (4, -1)):
        for alpha, beta, tau in itertools.product(range(5), repeat=3):
            y = (mu, 1, 0, 1, -1, alpha, beta, tau, 3, 0, 1)
            expected = (mu, 1, direction, 1+direction, -1+direction,
                        (alpha+direction) % 5, beta, tau, 0, 1, 1)
            insist(reference_f(y) == expected, "reference full accepted pair")
            insist(reference_inv(expected) == y, "reference inverse")
            insist(account(y) == account(expected) == 8, "reference whole account")
            reference_cases += 1
    for y in ((1, 1, 1, 1, 0, 0, 0, 0, 3, 0, 1),
              (1, 0, -2, 1, 0, 0, 0, 0, 1, 0, 1)):
        insist(account(y) == 8, "reference refusal fixture shell")
        insist(reference_f(y) == reflect(y), "both bank-bound refusals")
        insist(reference_inv(reference_f(y)) == y, "refusal inverse")
    zero = (0, 1, 2, 0, 0, 0, 0, 0, 3, 0, 1)
    insist(account(zero) == 8, "zero-control shell")
    insist(reference_f(zero) == zero[:9] + (1, 1), "zero-control edge advances")
    insist(reference_inv(reference_f(zero)) == zero, "zero-control inverse")
    for c, direction in ((0, -1), (1, 1)):
        y = zero[:9] + (c, direction)
        insist(reference_f(y) == reflect(y), "outward endpoint reflection")
        insist(reference_inv(reference_f(y)) == y, "endpoint inverse")
    gate("REFERENCE", str(reference_cases) + " exposed pair/label cases both bank bounds zero and endpoints; no full-shell realization")

    GATE = "INDEPENDENT"
    replay = subprocess.run([sys.executable, str(HERE / "break.py")],
                            cwd=ROOT, capture_output=True, timeout=120)
    insist(replay.stdout and replay.stdout.isascii(), "independent exact output missing")
    print(replay.stdout.decode("ascii"), end="" if replay.stdout.endswith(b"\n") else "\n", flush=True)
    if replay.stderr:
        sys.stderr.buffer.write(replay.stderr)
        sys.stderr.buffer.flush()
    insist(replay.returncode == 0 and replay.stderr == b"", "independent breaker failed")
    gate("INDEPENDENT", "separately authored pinned breaker executed; same-session result-exposed")
    print("RESULT PASS NO_REALIZATION_IN_FROZEN_CLASS / DECLARED_EXTENSION_ONLY")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print("FALSIFIED " + GATE + " " + str(error), flush=True)
        raise SystemExit(2)
    except Exception as error:
        print("STOP " + GATE + " " + type(error).__name__, flush=True)
        raise SystemExit(1)
