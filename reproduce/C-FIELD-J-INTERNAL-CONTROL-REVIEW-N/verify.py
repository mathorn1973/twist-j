#!/usr/bin/env python3
"""Independent exact port-machine audit. No runtime files or sampled inputs.

Original review implementation, Apache-2.0. Scientific execution is permitted
only after publication/readback of the complete review source freeze.
"""
from fractions import Fraction as Q
from itertools import product


ZERO = (0, 0, 0, 0)
COEFF = ((-1, -1, -1, -1), (1, 0, 0, 0),
         (0, 1, 0, 0), (0, 0, 1, 0))


def chart(a):
    x, y, z, w = a
    return (y, z-w, x-y-w, y-2*z+w)


LABELS = tuple(chart(a) for a in COEFF)
EMPTY = (0, ZERO, 0)
HAD = ((1, 1, 1, 1), (1, -1, 1, -1),
       (1, 1, -1, -1), (1, -1, -1, 1))


def height(y):
    a, b, c, d = y
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d


def code(y):
    x, y1, z, w = y
    a = (2*x-2*y1+z-w, x, x-y1-w, x-2*y1-w)
    return 1+(((a[0]+3)*5+a[1]+2)*5+a[2]+2)*7+a[3]+3


def width(n):
    return max(1, (n-1).bit_length())


def replace(s, pairs):
    t = list(s)
    for i, v in pairs:
        t[i] = v
    return tuple(t)


def swap(s, i, j):
    return replace(s, ((i, s[j]), (j, s[i])))


def add(out, state, value):
    out[state] = out.get(state, Q(0)) + value
    if not out[state]:
        del out[state]


def lift(v, law):
    out = {}
    for s, value in v.items():
        for t, factor in law(s):
            add(out, t, value*factor)
    return out


def norm(v):
    return sum((x*x for x in v.values()), Q(0))


def outer(v, w):
    return {(s, t): a*b for s, a in v.items() for t, b in w.items()}


class Device:
    # Every item is an actual tensor coordinate, including program and descriptor.
    head_names = ('pos', 'pc', 'q', 'a', 'e', 'b', 'fa', 'fb',
                  'I', 'C', 'run', 'X', 'Y', 'P0', 'P1', 'l0',
                  'z0', 'beta', 'mu0')

    def __init__(self, N, K, L, B, S):
        self.N, self.K, self.L, self.B, self.S = N, K, L, B, S
        self.toy = False
        self.T, self.M = 2*N-1, 2*L
        self.ew, self.cw = width(K+1), 1
        self.fields = (4, 1, width(K+1), width(L),
                       width(self.T), width(self.T), 1)
        self.v = sum(self.fields)
        names = list(self.head_names)
        for family, count in (('packet', self.T), ('latch', 1),
                              ('pointer', K+1), ('flag', K), ('bath', B),
                              ('meta', K), ('program', S), ('theta', 1),
                              ('reference', 1)):
            indices = list(range(len(names), len(names)+count))
            setattr(self, family, indices)
            names.extend(f'{family}{i}' for i in range(count))
        self.size = len(names)
        self.names = tuple(names)
        for i, name in enumerate(self.head_names):
            setattr(self, name, i)
        self.ports = []
        for bus, family in ((self.X, self.packet), (self.Y, self.packet),
                            (self.P0, self.pointer), (self.P1, self.pointer),
                            (self.l0, self.latch), (self.z0, self.flag),
                            (self.mu0, self.meta), (self.beta, self.bath)):
            self.ports.extend((bus, address, memory)
                              for address, memory in enumerate(family))
        self.g = len(self.ports)
        self.stations = ([('fetch', i) for i in range(S)] + [('pre',)] +
                         [('port', *p) for p in self.ports] + [('exec',)] +
                         [('port', *p) for p in reversed(self.ports)] +
                         [('post',)] + [('fetch', i) for i in reversed(range(S))] +
                         [('pc',)])
        self.d = len(self.stations)

    def word(self, op, inv=0, i=0, j=0, x=0, y=0, k=0):
        value = 0
        shift = 0
        for field, bits in zip((op, inv, i, j, x, y, k), self.fields):
            assert 0 <= field < (1 << bits)
            value |= field << shift
            shift += bits
        return value

    def decode(self, value):
        fields = []
        for bits in self.fields:
            fields.append(value & ((1 << bits)-1))
            value >>= bits
        op, inv, i, j, x, y, k = fields
        if (op > 8 or (op == 1 and (i > self.K or j >= self.L)) or
                (op == 5 and (x >= self.T or y >= self.T or x == y)) or
                (op in (6, 7) and k >= 2)):
            op = 0
        return op, inv, i, j, x, y, k

    def fixture(self, f, words=None, clean=False, label=0):
        s = [0]*self.size
        ys = (ZERO,) + LABELS + ((0, 0, 4, 0),)
        for j, index in enumerate(self.packet):
            s[index] = ((j+f) % 2, ys[(2*j+f) % 6], (j+f) % 4)
        for j, index in enumerate(self.pointer):
            s[index] = (3*j+f) % self.M
        for family in (self.flag, self.bath):
            for j, index in enumerate(family):
                s[index] = (j+f) % 2
        s[self.latch[0]] = f % 2
        for j, index in enumerate(self.meta):
            s[index] = (j+f) % (1 << (self.ew+self.cw+1))
        s[self.X] = (f % 2, ys[(f+1) % 6], f % 4)
        s[self.Y] = ((f+1) % 2, ys[(f+3) % 6], (f+2) % 4)
        for index, value in ((self.P0, f % self.M),
                             (self.P1, (self.M-f-1) % self.M),
                             (self.l0, (f+1) % 2), (self.z0, f % 2),
                             (self.beta, (f+1) % 2),
                             (self.mu0, (1 << (self.ew+2))-1),
                             (self.a, f % (self.K+1)),
                             (self.b, f % (self.B+1)),
                             (self.e, (f+1) % (self.K+1)),
                             (self.fa, f % (self.S+1)),
                             (self.fb, (f+1) % (self.S+1)),
                             (self.I, f % (1 << self.ew)),
                             (self.C, f % 2), (self.run, f % 2)):
            s[index] = value
        if clean:
            for index in self.packet:
                s[index] = EMPTY
            s[self.packet[0]] = (1, LABELS[label], 2)
            for index in (self.pos, self.pc, self.q, self.a, self.b, self.e,
                          self.fa, self.fb, self.I, self.C, self.run,
                          self.latch[0], *self.pointer, *self.flag,
                          *self.meta, *self.bath):
                s[index] = 0
        if words is None:
            words = [self.word(15, t % 2) for t in range(self.S)]
        assert len(words) == self.S
        for index, value in zip(self.program, words):
            s[index] = value
        return tuple(s)

    def addresses(self, s):
        op, _, i, _, x, y, _ = self.decode(s[self.q])
        if op == 1:
            return {self.P0: self.pointer[i], **(
                {self.beta: self.bath[s[self.b]]} if s[self.b] < self.B else {})}
        if op in (2, 3):
            return {self.X: self.packet[0]}
        if op == 4:
            return {self.X: self.packet[self.N-1], self.l0: self.latch[0],
                    self.P0: self.pointer[0]}
        if op == 5:
            return {self.X: self.packet[x], self.Y: self.packet[y]}
        if op == 8:
            a = s[self.a]
            ans = {self.P0: self.pointer[0]}
            if a < self.K:
                ans.update({self.P1: self.pointer[a+1], self.z0: self.flag[a],
                            self.mu0: self.meta[a]})
            return ans
        return {}

    def advance(self, s, undo=False):
        op = self.decode(s[self.q])[0]
        if op == 7:
            return replace(s, ((self.e, (s[self.e]+(-1 if undo else 1)) % (self.K+1)),))
        if op not in (1, 8):
            return s
        cursor, failure, capacity = ((self.b, self.fb, self.B) if op == 1
                                     else (self.a, self.fa, self.K))
        old = (s[cursor]-1) % (capacity+1) if undo else s[cursor]
        delta = int(old == capacity)*(-1 if undo else 1)
        return replace(s, ((cursor, old if undo else (old+1) % (capacity+1)),
                           (failure, (s[failure]+delta) % (self.S+1))))

    def primitive(self, s, targets, adjoint=False):
        op, _, _, j, _, _, k = self.decode(s[self.q])
        if op == 1 and s[self.b] < self.B:
            p, bit = targets[self.P0], targets[self.beta]
            support = ((2*j, 0), (2*((j+1) % self.L), 0),
                       (2*j, 1), (2*((j+1) % self.L), 1))
            signs = (1, -1, -1, -1)
            key = (s[p], s[bit])
            if key not in support:
                return [(s, Q(1))]
            col = support.index(key)
            ans = []
            for row, (pv, bv) in enumerate(support):
                factor = Q(int(row == col))-Q(signs[row]*signs[col], 2)
                if factor:
                    ans.append((replace(s, ((p, pv), (bit, bv))), factor))
            return ans
        if op in (2, 3) and s[self.C] < 2:
            index = targets[self.X]
            b, y, r = s[index]
            if s[self.C] == 1 and b == 1 and y in LABELS:
                col = LABELS.index(y)
                return [(replace(s, ((index, (b, field, r)),)), Q(HAD[row][col], 2))
                        for row, field in enumerate(LABELS)]
        if op == 4:
            p, l, q = targets[self.X], targets[self.l0], targets[self.P0]
            b, y, r = s[p]
            supported = y in LABELS if self.toy else height(y) <= 5
            translation = ((1, 0, 2, 4)[LABELS.index(y)]
                           if self.toy and y in LABELS else code(y))
            if b == 1 and supported:
                if not adjoint:
                    if s[l] == 1:
                        return [(replace(s, ((p, (b, y, r+2)), (l, 0))), Q(1))]
                    if r >= 2:
                        return [(replace(s, ((p, (b, y, r-2)), (l, 1),
                                             (q, (s[q]+translation) % self.M))), Q(1))]
                else:
                    if s[l] == 1:
                        return [(replace(s, ((p, (b, y, r+2)), (l, 0),
                                             (q, (s[q]-translation) % self.M))), Q(1))]
                    if r >= 2:
                        return [(replace(s, ((p, (b, y, r-2)), (l, 1))), Q(1))]
        if op == 5:
            return [(swap(s, targets[self.X], targets[self.Y]), Q(1))]
        if op in (6, 7):
            return [(replace(s, ((self.I, s[self.I] ^ s[self.e]),
                                 (self.C, s[self.C] ^ k),
                                 (self.run, s[self.run] ^ 1))), Q(1))]
        if op == 8 and s[self.a] < self.K:
            p, q, flag, meta = (targets[x] for x in (self.P0, self.P1, self.z0, self.mu0))
            payload = s[self.I] | (s[self.C] << self.ew) | (1 << (self.ew+self.cw))
            return [(replace(s, ((p, s[q]), (q, s[p]), (flag, s[flag] ^ 1),
                                 (meta, s[meta] ^ payload))), Q(1))]
        return [(s, Q(1))]

    def station(self, s, at, undo=False):
        entry = self.stations[at]
        kind = entry[0]
        inv = self.decode(s[self.q])[1]
        if kind == 'fetch':
            t = entry[1]
            if s[self.pc] == t:
                s = replace(s, ((self.q, s[self.q] ^ s[self.program[t]]),))
        elif kind == 'port':
            bus, _, memory = entry[1:]
            if self.addresses(s).get(bus) == memory:
                s = swap(s, bus, memory)
        elif kind == 'pre' and inv:
            s = self.advance(s, not undo)
        elif kind == 'post' and not inv:
            s = self.advance(s, undo)
        elif kind == 'exec':
            return self.primitive(s, {x: x for x in range(self.size)}, bool(inv) ^ undo)
        elif kind == 'pc':
            s = replace(s, ((self.pc, (s[self.pc]+(-1 if undo else 1)) % self.S),))
        return [(s, Q(1))]

    def step(self, s, undo=False):
        at = (s[self.pos]-1) % self.d if undo else s[self.pos]
        before = replace(s, ((self.pos, at),)) if undo else s
        return [(replace(t, ((self.pos, at if undo else (at+1) % self.d),)), f)
                for t, f in self.station(before, at, undo)]

    def identity_station(self, s, at):
        entry = self.stations[at]
        op, inv, _, _, _, _, _ = self.decode(s[self.q])
        if entry[0] == 'fetch':
            return s[self.pc] != entry[1]
        if entry[0] == 'port':
            return self.addresses(s).get(entry[1]) != entry[3]
        if entry[0] == 'pre':
            return not inv or op not in (1, 7, 8)
        if entry[0] == 'post':
            return bool(inv) or op not in (1, 7, 8)
        if entry[0] == 'exec':
            return op == 0
        return False

    def tour(self, v, bath_isolated=False):
        # Coalesce only ports proved unselected by unchanged classical controls.
        # The position is advanced through every omitted identity station.
        sig_indices = tuple(range(self.pc, self.run+1)) + tuple(self.program)
        signatures = {tuple(s[i] for i in sig_indices) for s in v}
        assert len(signatures) == 1
        assert all(s[self.pos] == 0 for s in v)
        ticks = 0
        for at, entry in enumerate(self.stations):
            representative = next(iter(v))
            idle = self.identity_station(representative, at)
            if bath_isolated:
                assert self.decode(representative[self.q])[0] != 1
                if entry[0] == 'port' and entry[1] == self.beta:
                    assert idle
            if not idle:
                v = lift(v, lambda s: self.station(replace(s, ((self.pos, at),)), at))
            ticks += 1
        v = lift(v, lambda s: [(replace(s, ((self.pos, 0),)), Q(1))])
        assert ticks == self.d
        return v, ticks

    def external(self, s):
        # Literal memory-target primitive, with independently placed cursor undo.
        original_q = s[self.q]
        word = s[self.program[s[self.pc]]]
        t = replace(s, ((self.q, word),))
        op, inv, i, _, x, y, _ = self.decode(word)
        if inv:
            t = self.advance(t, True)
        a, b = t[self.a], t[self.b]
        target = {}
        if op == 1:
            target[self.P0] = self.pointer[i]
            if b < self.B:
                target[self.beta] = self.bath[b]
        elif op in (2, 3):
            target[self.X] = self.packet[0]
        elif op == 4:
            target = {self.X: self.packet[self.N-1], self.l0: self.latch[0],
                      self.P0: self.pointer[0]}
        elif op == 5:
            target = {self.X: self.packet[x], self.Y: self.packet[y]}
        elif op == 8 and a < self.K:
            target = {self.P0: self.pointer[0], self.P1: self.pointer[a+1],
                      self.z0: self.flag[a], self.mu0: self.meta[a]}
        ans = []
        for u, factor in self.primitive(t, target, bool(inv)):
            if not inv:
                u = self.advance(u)
            u = replace(u, ((self.q, original_q), (self.pc, (s[self.pc]+1) % self.S)))
            ans.append((u, factor))
        return ans

    def energy(self, s):
        packets = sum(b+height(y)+r for b, y, r in
                      (s[i] for i in self.packet+[self.X, self.Y]))
        return packets+2*(s[self.latch[0]]+s[self.l0])+1+2*self.K+self.B+self.K+self.S+17


def compile_program(N, K, L, counts, contexts, W):
    T = 2*N-1
    raw = []
    for i, sweeps in enumerate(counts):
        for _ in range(sweeps):
            for j in range(L):
                raw.append((1, 0, i, j, 0, 0, 0))
    for context in contexts:
        raw.extend(((6, 0, 0, 0, 0, 0, context), (2, 0, 0, 0, 0, 0, 0)))
        for _ in range(2*T):
            raw.append((4, 0, 0, 0, 0, 0, 0))
            for j in range(N-1):
                raw.append((5, 0, 0, 0, j, 2*N-2-j, 0))
            for j in range(N-1):
                raw.append((5, 0, 0, 0, 2*N-2-j, j+1, 0))
        raw.extend(((3, 0, 0, 0, 0, 0, 0), (8, 0, 0, 0, 0, 0, 0),
                    (7, 0, 0, 0, 0, 0, context)))
    H = len(raw)
    inverse = [(o, 1-i, p, j, x, y, k) for o, i, p, j, x, y, k in reversed(raw)]
    return raw+[(0, 0, 0, 0, 0, 0, 0)]*W+inverse, H


def audit_compiler():
    count = 0
    for N, K, W in product((2, 4), (0, 1, 3), (1, 3)):
        for h in range(K+1):
            for counts in ((0,)*(K+1), tuple(i % 2 for i in range(K+1))):
                contexts = tuple((i+1) % 2 for i in range(h))
                words, H = compile_program(N, K, 613, counts, contexts, W)
                B, T = 613*sum(counts), 2*N-1
                assert H == B+h*(2*T*T+5)
                assert len(words) == 2*H+W
                assert [(o, 1-i, p, j, x, y, k) for o, i, p, j, x, y, k
                        in reversed(words[:H])] == words[H+W:]
                assert words[:B] == [(1, 0, i, j, 0, 0, 0)
                                     for i, n in enumerate(counts)
                                     for _ in range(n) for j in range(613)]
                for t in range(h):
                    start = B+t*(2*T*T+5)
                    for step in range(1, 2*T+1):
                        receiver = start+2+(step-1)*T
                        assert words[receiver][0] == 4
                        assert receiver+T == start+2+step*T
                    assert words[start+2*T*T+3][0] == 8
                count += 1
    return count


def inventory(d):
    return [d.word(0), d.word(6, k=1), d.word(7, k=0), d.word(2),
            d.word(3), d.word(4), d.word(5, x=0, y=d.T-1),
            d.word(1, i=0, j=0), d.word(1, i=d.K, j=d.L-1),
            d.word(8), d.word(15), d.word(5, x=0, y=0),
            d.word(1, j=(1 << width(d.L))-1)]


def audit_stations():
    cases = 0
    for args in ((2, 0, 613, 0, 1), (2, 1, 3, 1, 2), (3, 2, 613, 2, 3)):
        d = Device(*args)
        assert d.g == 4*d.N+4*d.K+d.B+1
        assert d.d == 2*d.S+2*d.g+4
        incidence = {}
        for station in d.stations:
            if station[0] == 'port':
                memory = station[3]
            elif station[0] == 'fetch':
                memory = d.program[station[1]]
            else:
                continue
            incidence[memory] = incidence.get(memory, 0)+1
        assert max(incidence.values()) <= 4
        for f, word, polarity, pc in product(range(3), inventory(d), (0, 1), range(d.S)):
            s = d.fixture(f)
            s = replace(s, ((d.q, word ^ (polarity << 4)), (d.pc, pc)))
            for at in range(d.d):
                a = replace(s, ((d.pos, at),))
                for backwards in (False, True):
                    out = dict(d.step(a, backwards))
                    assert norm(out) == 1
                    assert all(d.energy(t) == d.energy(a) for t in out)
                    recovered = lift(out, lambda t: d.step(t, not backwards))
                    assert recovered == {a: Q(1)}
                    cases += 1
    return cases


def audit_commands():
    d = Device(3, 2, 613, 3, 1)
    cases = 0
    for f, word, polarity in product(range(3), inventory(d), (0, 1)):
        s = d.fixture(f, [word ^ (polarity << 4)])
        s = replace(s, ((d.q, 0), (d.pc, 0), (d.pos, 0)))
        # Force an endpoint cursor, including exhaustion, independently of f.
        s = replace(s, ((d.a, (2*f) % 3), (d.b, (2*f) % 4)))
        a = replace(s, ((d.packet[0], (1, LABELS[1], 2)),
                        (d.packet[d.N-1], (1, LABELS[1], 2)), (d.reference[0], 0)))
        b = replace(s, ((d.packet[0], (1, LABELS[2], 2)),
                        (d.packet[d.N-1], (1, LABELS[2], 2)),
                        (d.X, (1, LABELS[3], 3)), (d.reference[0], 1)))
        for v in ({a: Q(1)}, {b: Q(1)}, {a: Q(1), b: Q(2, 3)}):
            out, ticks = d.tour(v)
            expected = lift(v, d.external)
            assert out == expected and ticks == d.d
            assert norm(out) == norm(v)
            assert outer(out, out) == outer(expected, expected)
            cases += 1
    # Explicit exhaustion followed by inverse recovers pre-wrap addresses.
    for op, cursor, failure, cap in ((1, d.b, d.fb, d.B), (8, d.a, d.fa, d.K)):
        s = d.fixture(0, [d.word(op)])
        s = replace(s, ((cursor, cap), (failure, 0), (d.q, 0)))
        out, _ = d.tour({s: Q(1)})
        t = next(iter(out))
        assert t[cursor] == 0 and t[failure] == 1
        t = replace(t, ((d.program[0], d.word(op, 1)),))
        restored, _ = d.tour({t: Q(1)})
        expected = replace(s, ((d.program[0], d.word(op, 1)),))
        assert restored == {expected: Q(1)}
    return cases


def history_weights(v, d, h):
    out = {w: Q(0) for w in product((0, 1), repeat=h)}
    for s, a in v.items():
        word = tuple(s[d.pointer[i+1]] % 2 for i in range(h))
        out[word] += a*a
    return out


def bath_marginal(v, d):
    # Exact partial trace over all coordinates except the retained baths.
    chosen = set(d.bath)
    groups = {}
    for s, a in v.items():
        rest = tuple(x for i, x in enumerate(s) if i not in chosen)
        bath = tuple(s[i] for i in d.bath)
        groups.setdefault(rest, {})[bath] = a
    out = {}
    for group in groups.values():
        for b, a in group.items():
            for c, z in group.items():
                add(out, (b, c), a*z)
    return out


def audit_programs():
    cases, mixed, outside_mixed = 0, Q(0), Q(0)
    domains = [(613, 2, (0, 0, 0), w) for w in
               ((), (0,), (1,), (0, 0), (1, 1), (0, 1), (1, 0))]
    domains += [(3, 1, (1, 0), (0,)), (3, 1, (1, 0), (1,)),
                (3, 2, (1, 0, 0), (0, 0)), (3, 2, (1, 0, 0), (0, 1))]
    for L, K, counts, contexts in domains:
        words, H = compile_program(2, K, L, counts, contexts, 1)
        B = L*sum(counts)
        d = Device(2, K, L, B, len(words))
        d.toy = L == 3
        tape = [d.word(*w) for w in words]
        columns, expected_columns = [], []
        for label in range(4):
            s = d.fixture(1, tape, clean=True, label=label)
            v = {s: Q(1)}
            expected = dict(v)
            if H == 0:
                columns.append(v)
                expected_columns.append(expected)
            bath_before = None
            for command in range(d.S):
                if command == B:
                    bath_before = bath_marginal(v, d)
                isolated = B <= command < H+1
                v, ticks = d.tour(v, isolated)
                expected = lift(expected, d.external)
                assert v == expected and ticks == d.d
                assert norm(v) == 1
                if isolated:
                    assert bath_marginal(v, d) == bath_before
                if command+1 == H:
                    columns.append(v)
                    expected_columns.append(expected)
                    for state in v:
                        assert state[d.pos] == state[d.q] == state[d.fa] == state[d.fb] == 0
                        assert state[d.pc] == H and state[d.b] == B
                        assert state[d.a] == len(contexts) and state[d.e] == len(contexts)
                        assert state[d.I] == state[d.C] == state[d.run] == 0
                        assert tuple(state[i] for i in range(d.X, d.mu0+1)) == tuple(
                            s[i] for i in range(d.X, d.mu0+1))
                        for j, k in enumerate(contexts):
                            assert state[d.flag[j]] == 1
                            assert state[d.meta[j]] == j | (k << d.ew) | (1 << (d.ew+1))
                    if contexts == (1, 1) and L == 613:
                        weights = history_weights(v, d, 2)
                        mixed += weights[(0, 1)]+weights[(1, 0)]
                if command == H:
                    # NOP read window preserves all data and bus coordinates.
                    before = lift(expected, lambda x: [(replace(x, ((d.pc, H),)), Q(1))])
                    if H:
                        assert before == columns[-1]
            assert v == {s: Q(1)}
            cases += 1
        for a, b in product(range(4), repeat=2):
            assert outer(columns[a], columns[b]) == outer(expected_columns[a], expected_columns[b])
        if B:
            for variant in ('correlated', 'odd', 'dirty_bath', 'dirty_flag'):
                a = d.fixture(1, tape, clean=True, label=1)
                b = d.fixture(2, tape, clean=True, label=2)
                b = replace(b, ((d.reference[0], 1),))
                if variant != 'correlated':
                    index = {'odd': d.pointer[0], 'dirty_bath': d.bath[0],
                             'dirty_flag': d.flag[0]}[variant]
                    a, b = replace(a, ((index, 1),)), replace(b, ((index, 1),))
                original = {a: Q(1), b: Q(2, 3)}
                v = dict(original)
                for command in range(d.S):
                    expected = lift(v, d.external)
                    v, _ = d.tour(v, B <= command < H+1)
                    assert v == expected
                    if command+1 == H and contexts == (0, 0) and variant == 'odd':
                        weights = history_weights(v, d, 2)
                        outside_mixed += weights[(0, 1)]+weights[(1, 0)]
                assert v == original
                cases += 1
    # Positive even-sector preparation preserves exact repeated parity, even
    # while its within-HIGH post-state differs from ideal readiness.
    assert mixed == 0
    assert outside_mixed > 0  # Retained off-domain ideal-zero histories.
    return cases, mixed, outside_mixed


def matmul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(4)), Q(0))
                       for j in range(4)) for i in range(4))


def audit_ideal():
    ident = tuple(tuple(Q(i == j) for j in range(4)) for i in range(4))
    U = (ident, tuple(tuple(Q(x, 2) for x in row) for row in HAD))
    projectors = [tuple(tuple(Q(i == j and int(i == 0) == o)
                              for j in range(4)) for i in range(4)) for o in (0, 1)]
    cases = 0
    for contexts in ((), (0,), (1,), (0, 0), (1, 1), (0, 1), (1, 0)):
        columns = []
        for source in range(4):
            v = {(source, ()): Q(1)}
            for k in contexts:
                pre, measured, post = {}, {}, {}
                for (j, history), value in v.items():
                    for i in range(4):
                        add(pre, (i, history), U[k][i][j]*value)
                for (i, history), value in pre.items():
                    add(measured, (i, history+(int(i == 0),)), value)
                for (j, history), value in measured.items():
                    for i in range(4):
                        add(post, (i, history), U[k][j][i]*value)
                v = post
            columns.append(v)
        for word in product((0, 1), repeat=len(contexts)):
            operator = ident
            for k, outcome in zip(contexts, word):
                operator = matmul(matmul(matmul(U[k], projectors[outcome]), U[k]), operator)
            for a, b in product(range(4), repeat=2):
                actual = {(i, j): columns[a].get((i, word), Q(0))*columns[b].get((j, word), Q(0))
                          for i, j in product(range(4), repeat=2)}
                expected = {(i, j): operator[i][a]*operator[j][b]
                            for i, j in product(range(4), repeat=2)}
                assert actual == expected
                if len(contexts) == 2 and contexts[0] == contexts[1] and word[0] != word[1]:
                    assert not any(actual.values())
                cases += 1
        # Explicit retained within-HIGH off-diagonal in the identity context.
        if contexts == (0,):
            assert columns[1][(1, (0,))]*columns[2][(2, (0,))] == 1
    return cases


def audit_loader():
    cases = 0
    for L in (3, 5):
        for p in range(0, 2*L, 2):
            d = Device(2, 0, L, L, 1)
            s = d.fixture(0, [d.word(1)])
            s = replace(s, ((d.b, 0), (d.q, 0), (d.pointer[0], p),
                            *((index, 0) for index in d.bath)))
            v = {s: Q(1)}
            for j in range(L):
                v = lift(v, lambda t: [(replace(t, ((d.program[0], d.word(1, j=j)),)), Q(1))])
                expected = lift(v, d.external)
                v, _ = d.tour(v)
                assert v == expected
            groups = {}
            for t, value in v.items():
                rest = tuple(x for i, x in enumerate(t) if i != d.pointer[0])
                groups[rest] = groups.get(rest, Q(0))+value
            fidelity = sum((a*a for a in groups.values()), Q(0))/L
            assert 1-fidelity <= (1-Q(4, L**3))*(1-Q(1, L))
            assert fidelity < 1
            assert norm(v) == 1
            cases += 1
    return cases


def report(admission, chronology, retained, completed, request, cursor, capacity):
    if not chronology:
        resource = 'NO_CLASSICAL_CHRONOLOGY'
    elif request is None:
        resource = 'NO_REQUEST'
    elif cursor < capacity:
        resource = 'WITHIN_CAPACITY'
    else:
        resource = 'CAPACITY_EXHAUSTED'
    if not admission or not chronology or not retained:
        status = 'INVALID_PROMISE'
    elif completed == 0:
        status = 'NO_COMPLETED_ROUND'
    else:
        status = 'FORMAL_RECORD_AVAILABLE'
    return status, resource, 'NOT_DERIVED'


def audit_boundary():
    count = 0
    for admitted, chronology, retained, completed, request, cursor in product(
            (False, True), (False, True), (False, True), (0, 1, 2), (None, 'APPEND'), (0, 2)):
        result = report(admitted, chronology, retained, completed, request, cursor, 2)
        assert result[2] == 'NOT_DERIVED'
        if not (admitted and chronology and retained):
            assert result[0] == 'INVALID_PROMISE'
        if request is None and chronology:
            assert result[1] == 'NO_REQUEST'
        count += 1
    assert report(True, True, True, 2, None, 2, 2)[:2] == (
        'FORMAL_RECORD_AVAILABLE', 'NO_REQUEST')
    assert report(False, True, True, 2, 'APPEND', 2, 2)[:2] == (
        'INVALID_PROMISE', 'CAPACITY_EXHAUSTED')
    epsilon_control, epsilon_occurrence = Q(0), None
    assert epsilon_control == 0 and epsilon_occurrence is None
    return count


def main():
    print('C-FIELD-J-INTERNAL-CONTROL independent exact review audit')
    print('compiler_descriptors', audit_compiler())
    print('station_inverse_cases', audit_stations())
    print('complete_command_cases', audit_commands())
    programs, mixed, outside_mixed = audit_programs()
    print('complete_program_cases', programs)
    print('retained_repeated_context_nonconstant_weight', mixed)
    print('off_domain_retained_nonconstant_weight', outside_mixed)
    print('ideal_history_matrix_units', audit_ideal())
    print('finite_loader_columns', audit_loader())
    print('typed_boundary_cases', audit_boundary())
    print('PASS exact conditional control; occurrence law NOT_DERIVED')


if __name__ == '__main__':
    main()
