#!/usr/bin/env python3
"""Exact audit of a declared funded network; NON-CANONICAL / L1.

Two arithmetic implementations by one author, not independent authorship.
The complete source is frozen before execution. Standard library only.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
J = (1, 0, 1, 0)
JI = (0, -1, -1, 0)
G = (2, 0, 1, 1)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def sub(x, y):
    return add(x, neg(y))


def scale(k, x):
    return tuple(k * a for a in x)


def half(x):
    assert all(a % 2 == 0 for a in x)
    return tuple(a // 2 for a in x)


def trace(x):
    return 4 * x[0] - sum(x[1:])


class Ring:
    def __init__(self, cyclic):
        self.cyclic = cyclic

    @lru_cache(maxsize=None)
    def mul(self, x, y):
        if self.cyclic:
            p = [0] * 5
            for i, a in enumerate(x):
                for j, b in enumerate(y):
                    p[(i + j) % 5] += a * b
            return tuple(p[i] - p[4] for i in range(4))
        p = [0] * 7
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                p[i + j] += a * b
        for k in range(6, 3, -1):
            a = p[k]
            for j in range(1, 5):
                p[k - j] -= a
            p[k] = 0
        return tuple(p[:4])

    def conjugate(self, x):
        if self.cyclic:
            p = [0] * 5
            for k, a in enumerate(x):
                p[(-k) % 5] += a
            return tuple(p[i] - p[4] for i in range(4))
        a, b, c, d = x
        return a - b, -b, d - b, c - b

    @lru_cache(maxsize=None)
    def h(self, x):
        return self.mul(x, self.conjugate(x))

    @lru_cache(maxsize=None)
    def q(self, x):
        numerator = 5 * sum(a*a for a in x) - sum(x)**2
        assert numerator % 2 == 0
        assert trace(self.h(x)) == numerator
        assert numerator >= sum(a*a for a in x)
        return numerator // 2

    def account(self, z):
        s, h, q = ZERO, ZERO, 0
        for x in z:
            s, h, q = add(s, x), add(h, self.h(x)), q + self.q(x)
        assert trace(h) == 2*q
        return s, h, q

    def gate(self, z):
        x, y, p, r = z
        dx, dp = sub(x, y), sub(p, r)
        if any(a % 2 for a in dx + dp):
            return z
        c, d, u, v = half(add(x, y)), half(add(p, r)), half(dx), half(dp)
        hu, hv = self.h(u), self.h(v)
        if u != ZERO and hv == self.mul(G, hu):
            u, v = self.mul(J, u), self.mul(JI, v)
        elif v != ZERO and hu == self.mul(G, hv):
            u, v = self.mul(JI, u), self.mul(J, v)
        else:
            return z
        return add(c, u), sub(c, u), add(d, v), sub(d, v)


P = Ring(False)
R = Ring(True)


def apply(z, addresses, ring):
    out = list(z)
    values = ring.gate(tuple(z[i] for i in addresses))
    for i, x in zip(addresses, values):
        out[i] = x
    return tuple(out)


def layer(z, parity, ring):
    m = len(z) // 2
    assert len(z) == 2*m and m >= 4 and m % 2 == 0
    out = list(z)
    used = set()
    for i in range(parity, m, 2):
        j = (i+1) % m
        ids = (2*i, 2*i+1, 2*j, 2*j+1)
        assert not used.intersection(ids)
        used.update(ids)
        vals = ring.gate(tuple(z[k] for k in ids))
        for k, x in zip(ids, vals):
            out[k] = x
    assert len(used) == len(z)
    return tuple(out)


def step(z, ring=P, inverse=False):
    first, second = (1, 0) if inverse else (0, 1)
    return layer(layer(z, first, ring), second, ring)


def step4(z, ring=P, inverse=False):
    a, b = (0,1,2,3), (1,2,3,0)
    if inverse:
        a, b = b, a
    return apply(apply(z, a, ring), b, ring)


def flip(z, site):
    out = list(z)
    out[2*site] = neg(out[2*site])
    out[2*site+1] = neg(out[2*site+1])
    return tuple(out)


def sums(z):
    return tuple(add(z[i], z[i+1]) for i in range(0, len(z), 2))


def encode(bits, amplitude=1, tagged=False):
    out = []
    for i, bit in enumerate(bits):
        phase = ONE
        if tagged:
            for _ in range(i % 5):
                phase = P.mul(phase, RHO)
            phase = scale((-1)**i, phase)
        u = scale(amplitude, P.mul(phase, J if bit else ONE))
        c = scale(i % 3 - 1, ONE) if tagged else ZERO
        out.extend((add(c,u), sub(c,u)))
    return tuple(out)


def shifted(bits, time):
    m = len(bits)
    return tuple(bits[(i-2*time) % m] if i % 2 == 0
                 else bits[(i+2*time) % m] for i in range(m))


def sign_reader(x):
    if x == ZERO:
        return ["BLANK"]
    t = trace(x)
    return ["VALUE", int(t > 0) - int(t < 0)]


def read_remote(z, d):
    left, right = 2*d, 2*d+1
    ql = P.q(z[2*left]) + P.q(z[2*left+1])
    qr = P.q(z[2*right]) + P.q(z[2*right+1])
    value = Fraction(ql-qr, 2)
    return ["NO_EXCESS"] if not value else ["VALUE", value.numerator, value.denominator]


def audit():
    assert __debug__, "Assertions must be enabled"
    for ring in (P, R):
        assert ring.mul(J, JI) == ONE
        assert ring.h(J) == G
    digest = sha256()
    counts = {}

    def row(kind, *values):
        data = json.dumps([kind, *values], separators=(",",":"), sort_keys=True)
        digest.update((data+"\n").encode("ascii"))

    alphabet = (ZERO, ONE, neg(ONE), ROOT, neg(ROOT), J, neg(J), JI, neg(JI))
    count = 0
    for z in product(alphabet, repeat=4):
        out = P.gate(z)
        assert out == R.gate(z)
        assert P.gate(out) == R.gate(out) == z
        assert P.account(z) == P.account(out) == R.account(out)
        assert sums(z) == sums(out)
        for i in (0,1):
            assert P.gate(flip(z,i)) == flip(out,i)
        row("gate", z, out)
        count += 1
    assert count == 6561
    counts["raw_gate_cases"] = count

    sites = tuple((add(c,u), sub(c,u)) for c in (ZERO,ONE) for u in (ZERO,ONE,J))
    sites += ((ZERO, ONE),)
    count = 0
    for ps in product(sites, repeat=4):
        z = tuple(x for p in ps for x in p)
        out = step(z)
        assert out == step(z,R)
        assert step(out,inverse=True) == step(out,R,inverse=True) == z
        assert P.account(z) == P.account(out) == R.account(out)
        assert sums(z) == sums(out)
        for i in range(4):
            assert step(flip(z,i)) == flip(out,i)
            if z[2*i] == z[2*i+1]:
                assert out[2*i:2*i+2] == z[2*i:2*i+2]
        row("network", z, out)
        count += 1
    assert count == 2401
    counts["general_network_cases"] = count

    starts, steps = 0, 0
    for m in (4,6,8,10):
        for bits in product((0,1),repeat=m):
            initial = encode(bits)
            z = initial
            old_account = P.account(z)
            assert old_account[2] == 4*m+2*sum(bits)
            for t in range(m//2):
                assert z == encode(shifted(bits,t))
                out = step(z)
                assert out == step(z,R) == encode(shifted(bits,t+1))
                assert step(out,inverse=True) == z
                assert P.account(out) == old_account
                row("binary", m, bits, t, z, out)
                z = out
                steps += 1
            assert z == initial
            starts += 1
    assert (starts,steps) == (1360,6368)
    counts.update(binary_starts=starts,binary_steps=steps)

    starts, steps = 0, 0
    for amplitude in (-3,-1,1,3):
        for bits in product((0,1),repeat=8):
            initial = encode(bits,amplitude,True)
            z = initial
            acc = P.account(z)
            for t in range(4):
                out = step(z)
                assert out == step(z,R) == encode(shifted(bits,t+1),amplitude,True)
                assert step(out,inverse=True) == z
                assert P.account(out) == acc
                row("tagged",amplitude,bits,t,z,out)
                z = out
                steps += 1
            assert z == initial
            starts += 1
    assert (starts,steps) == (1024,4096)
    counts.update(tagged_starts=starts,tagged_steps=steps)

    boundaries, backward_steps = 0, 0
    example = []
    for d in range(1,9):
        for message in (-1,1):
            bits = [0]*(4*d)
            bits[0 if message == 1 else 1] = 1
            initial = encode(bits)
            z = initial
            history = []
            readings = []
            acc = P.account(z)
            assert acc[0] == ZERO and acc[2] == 16*d+2
            for t in range(4*d+1):
                expected = ["VALUE",message,1] if t % (2*d) == d else ["NO_EXCESS"]
                reading = read_remote(z,d)
                assert reading == expected
                assert z == encode(shifted(bits,t))
                assert P.account(z) == acc
                if t in (2*d,4*d):
                    assert z == initial
                history.append(z)
                readings.append(reading)
                row("message",d,message,t,z,reading)
                boundaries += 1
                if t < 4*d:
                    out = step(z)
                    assert out == step(z,R)
                    z = out
            for old in reversed(history[:-1]):
                z = step(z,inverse=True)
                assert z == old
                backward_steps += 1
            if d == 2:
                example.append([message,readings[:5]])
    assert (boundaries,backward_steps) == (304,288)
    counts.update(message_boundaries=boundaries,message_backward_steps=backward_steps)

    w = P.mul(J,RHO)
    zplus = (scale(2,ONE),ZERO,w,neg(w))+(ZERO,)*12
    zminus = flip(zplus,0)
    count = 0
    for t in range(33):
        assert zminus == flip(zplus,0)
        assert zminus[2:] == zplus[2:]
        assert all(x == ZERO for x in zplus[4:])
        row("original_sign",t,zminus,zplus)
        count += 2
        if t < 32:
            zplus,zminus = step(zplus),step(zminus)
    assert count == 66
    counts["original_sign_boundaries"] = count

    cycles = {
        1: ((scale(2,ONE),ZERO,w,neg(w)),
            (scale(2,ONE),neg(w),w,ZERO),
            (add(ONE,J),sub(ONE,J),RHO,neg(RHO))),
        -1: ((scale(-2,ONE),ZERO,w,neg(w)),
             (neg(add(ONE,J)),sub(J,ONE),RHO,neg(RHO)))
    }
    four_examples = []
    count = 0
    for message in (-1,1):
        cycle = cycles[message]
        assert len(set(cycle)) == len(cycle)
        z = cycle[0]
        history = []
        tr = []
        for t in range(13):
            assert z == cycle[t % len(cycle)]
            assert P.account(z) == (scale(2*message,ONE),(8,0,2,2),14)
            reading = sign_reader(z[1])
            assert reading == (["BLANK"] if t % len(cycle) == 0 else ["VALUE",message])
            row("repair",message,t,z,reading)
            history.append(z)
            tr.append(trace(z[1]))
            count += 1
            if t < 12:
                mid = P.gate(z)
                assert sign_reader(mid[1]) in (["BLANK"],["VALUE",message])
                out = step4(z)
                assert out == step4(z,R)
                assert step4(out,inverse=True) == z
                z = out
        for old in reversed(history[:-1]):
            z = step4(z,inverse=True)
            assert z == old
        four_examples.append([message,tr[:len(cycle)+1]])
    assert count == 26
    counts["four_cell_boundaries"] = count
    assert step4(cycles[1][0])[2:] != step4(cycles[-1][0])[2:]
    return {"probe":"P-J-FUNDED-PAIR-NETWORK-1","status":"PASS",
            "arithmetic_encodings_agree":True,"independent_authorship":False,
            "counts":counts,"four_cell_account":14,
            "four_cell_periods":[[-1,2],[1,3]],"four_cell_receiver_traces":four_examples,
            "remote_example_account":34,"remote_example_readings":example,
            "state_sha256":digest.hexdigest()}


if __name__ == "__main__":
    print(json.dumps(audit(),sort_keys=True,separators=(",",":")))
