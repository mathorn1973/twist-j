#!/usr/bin/env python3
"""Exact audit of the frozen fetched-program controller; Apache-2.0.

Specification e5ff31fd7296df4bf740fd27c1ac3de14b5c8148.
No predecessor or independent implementation is imported. Sparse vectors
retain every factor. The expected side applies a separately coded direct
logical command; only the implemented side visits actual memory ports.
"""

from fractions import Fraction as Q
from itertools import product


# Full state: packet bank, latch, pointers, flags, metadata, baths,
# immutable program, immutable descriptor, head controls, buses, reference.
PK, LA, PT, FL, ME, BA, PROGRAM, THETA, CONTROL, BUS, REF = range(11)
POS, PC, INS, AC, EP, BC, FA, FB, IV, CX, RUN = range(11)
BX, BY, BP, BQ, BL, BF, BB, BM = range(8)
FIELDS = ((-1, 0, 1, 0), (0, 0, 1, 0),
          (1, 0, -1, 1), (0, 1, 0, -2))
ZERO_FIELD = (0, 0, 0, 0)
FIELD_LIST = (ZERO_FIELD,) + FIELDS + ((0, 0, 4, 0),)
EMPTY = (0, ZERO_FIELD, 0)
HALF = Q(1, 2)
HAD = ((1, 1, 1, 1), (1, -1, 1, -1),
       (1, 1, -1, -1), (1, -1, -1, 1))
NOP, COLLIDE, PLUS, MINUS, RECEIVER, SWAP, OPEN, CLOSE, APPEND = range(9)


def put(t, i, value):
    return t[:i] + (value,) + t[i + 1:]


def head(s, i, value):
    return put(s, CONTROL, put(s[CONTROL], i, value))


def bus(s, i, value):
    return put(s, BUS, put(s[BUS], i, value))


def memory(s, bank, address, value):
    if bank == LA:
        return put(s, LA, value)
    return put(s, bank, put(s[bank], address, value))


def memory_value(s, bank, address):
    return s[LA] if bank == LA else s[bank][address]


def width(d):
    return max(1, (d - 1).bit_length())


def hfield(y):
    a, b, c, d = y
    return 2*a*a-2*a*b+3*b*b+c*c+d*d+2*a*c-a*d-b*c+3*b*d


def source_code(y):
    x, y1, z, t = y
    a = 2*x-2*y1+z-t
    b = x
    c = x-y1-t
    d = x-2*y1-t
    return 1 + (((a+3)*5+(b+2))*5+(c+2))*7+(d+3)


class Device:
    def __init__(self, n, k, baths, size, length, toy=False):
        self.n, self.k, self.baths, self.size, self.length = n, k, baths, size, length
        self.t, self.mod, self.toy = 2*n-1, 2*length, toy
        self.ew, self.cw = width(k+1), 1
        self.widths = (4, 1, width(k+1), width(length), width(self.t), width(self.t), 1)
        self.v = sum(self.widths)
        self.mw = self.ew + self.cw + 1
        self.decoded = {}
        self.ports = tuple(
            [(PK, i, BX) for i in range(self.t)]
            + [(PK, i, BY) for i in range(self.t)]
            + [(PT, i, BP) for i in range(k+1)]
            + [(PT, i, BQ) for i in range(k+1)]
            + [(LA, 0, BL)]
            + [(FL, i, BF) for i in range(k)]
            + [(ME, i, BM) for i in range(k)]
            + [(BA, i, BB) for i in range(baths)])
        self.g = len(self.ports)
        self.stations = tuple(
            [('fetch', t) for t in range(size)] + [('pre',)]
            + [('port',) + p for p in self.ports] + [('exec',)]
            + [('port',) + p for p in reversed(self.ports)] + [('post',)]
            + [('fetch', t) for t in reversed(range(size))] + [('pc',)])
        self.d = len(self.stations)
        assert self.g == 4*n+4*k+baths+1
        assert self.d == 2*size+2*self.g+4

    def word(self, op, inverse=0, i=0, j=0, x=0, y=0, k=0):
        result, shift = 0, 0
        for value, bits in zip((op, inverse, i, j, x, y, k), self.widths):
            assert 0 <= value < 2**bits
            result |= value << shift
            shift += bits
        return result

    def decode(self, word):
        if word not in self.decoded:
            rest, fields = word, []
            for bits in self.widths:
                fields.append(rest & (2**bits-1))
                rest >>= bits
            assert rest == 0
            op, inv, i, j, x, y, k = fields
            invalid = (op > APPEND
                       or (op == COLLIDE and (i > self.k or j >= self.length))
                       or (op == SWAP and (x >= self.t or y >= self.t or x == y))
                       or (op in (OPEN, CLOSE) and k >= 2))
            if invalid:
                fields[0] = NOP
            self.decoded[word] = tuple(fields)
        return self.decoded[word]

    def meta(self, invocation, context, done):
        return invocation | (context << self.ew) | (done << (self.ew+self.cw))

    def inventory(self):
        return (self.word(NOP), self.word(OPEN, k=0), self.word(CLOSE, k=1),
                self.word(PLUS), self.word(MINUS), self.word(RECEIVER),
                self.word(SWAP, x=0, y=self.t-1), self.word(COLLIDE, i=0, j=0),
                self.word(COLLIDE, i=self.k, j=self.length-1), self.word(APPEND),
                self.word(15), self.word(SWAP, x=0, y=0))


def dirty_fixture(d, f):
    packets = tuple(((v+f) % 2, FIELD_LIST[(v+f) % 6], (v+2*f) % 4)
                    for v in range(d.t))
    pointers = tuple((2*i+f) % d.mod for i in range(d.k+1))
    flags = tuple((t+f) % 2 for t in range(d.k))
    metadata = tuple(d.meta((t+f) % 2**d.ew, (t+2*f) % 2**d.cw, (t+f) % 2)
                     for t in range(d.k))
    baths = tuple((u+f) % 2 for u in range(d.baths))
    inv = d.inventory()
    program = tuple(inv[(t+f) % 12] ^ (((t+f) % 2) << 4) for t in range(d.size))
    ctl = (0, 0, 0, f % (d.k+1), (f+1) % (d.k+1), f % (d.baths+1),
           f % (d.size+1), (f+2) % (d.size+1), f % 2**d.ew,
           f % 2**d.cw, f % 2)
    buses = ((f % 2, FIELD_LIST[f % 6], f % 4),
             ((f+1) % 2, FIELD_LIST[(f+3) % 6], (f+2) % 4),
             f % d.mod, (d.mod-1-f) % d.mod,
             (f+1) % 2, f % 2, (f+1) % 2, (2**d.mw-1) if f % 2 else 0)
    return (packets, f % 2, pointers, flags, metadata, baths,
            program, 0, ctl, buses, 0)


def selected(d, ctl, ins, port):
    op, _, i, _, x, y, _ = ins
    bank, address, lane = port
    if op == COLLIDE:
        return ((lane == BP and bank == PT and address == i)
                or (lane == BB and bank == BA and address == ctl[BC] < d.baths))
    if op in (PLUS, MINUS):
        return lane == BX and bank == PK and address == 0
    if op == RECEIVER:
        return ((lane == BX and bank == PK and address == d.n-1)
                or (lane == BL and bank == LA)
                or (lane == BP and bank == PT and address == 0))
    if op == SWAP:
        return bank == PK and ((lane == BX and address == x) or (lane == BY and address == y))
    if op == APPEND:
        return ((lane == BP and bank == PT and address == 0)
                or (ctl[AC] < d.k and (
                    (lane == BQ and bank == PT and address == ctl[AC]+1)
                    or (lane == BF and bank == FL and address == ctl[AC])
                    or (lane == BM and bank == ME and address == ctl[AC]))))
    return False


def counter(d, s, op, inverse):
    ctl = list(s[CONTROL])
    if op in (COLLIDE, APPEND):
        at, fail, capacity = (BC, FB, d.baths) if op == COLLIDE else (AC, FA, d.k)
        if inverse:
            ctl[at] = (ctl[at]-1) % (capacity+1)
            ctl[fail] = (ctl[fail]-int(ctl[at] == capacity)) % (d.size+1)
        else:
            ctl[fail] = (ctl[fail]+int(ctl[at] == capacity)) % (d.size+1)
            ctl[at] = (ctl[at]+1) % (capacity+1)
    elif op == CLOSE:
        ctl[EP] = (ctl[EP]+(-1 if inverse else 1)) % (d.k+1)
    return put(s, CONTROL, tuple(ctl))


def receiver(d, packet, latch, pointer, inverse):
    present, field, reserve = packet
    if d.toy:
        supported = present == 1 and field in FIELDS
        code = (1, 0, 2, 4)[FIELDS.index(field)] if supported else 0
    else:
        supported = present == 1 and hfield(field) <= 5
        code = source_code(field) if supported else 0
    if not supported:
        return packet, latch, pointer
    if inverse:
        if latch:
            reserve, latch, pointer = reserve+2, 0, (pointer-code) % d.mod
        elif reserve >= 2:
            reserve, latch = reserve-2, 1
    else:
        if latch:
            reserve, latch = reserve+2, 0
        elif reserve >= 2:
            reserve, latch, pointer = reserve-2, 1, (pointer+code) % d.mod
    return (present, field, reserve), latch, pointer


def execute(d, s, ins, adjoint=False):
    op, inverse, _, edge, _, _, context = ins
    inverse ^= adjoint
    ctl, buses = s[CONTROL], s[BUS]
    if op == COLLIDE and ctl[BC] < d.baths:
        p, b = buses[BP], buses[BB]
        left, right = 2*edge, 2*((edge+1) % d.length)
        signs = {(left, 0): 1, (right, 0): -1, (left, 1): -1, (right, 1): -1}
        if (p, b) in signs:
            answer = {}
            for (q, u), sign in signs.items():
                coefficient = int((q, u) == (p, b))-HALF*signs[p, b]*sign
                target = bus(bus(s, BP, q), BB, u)
                if coefficient:
                    answer[target] = coefficient
            return answer
    elif op in (PLUS, MINUS) and ctl[CX] == 1:
        present, field, reserve = buses[BX]
        if present == 1 and field in FIELDS:
            col = FIELDS.index(field)
            return {bus(s, BX, (present, FIELDS[row], reserve)):
                    HALF * (-1 if (row & col).bit_count() % 2 else 1)
                    for row in range(4)}
    elif op == RECEIVER:
        packet, latch, pointer = receiver(d, buses[BX], buses[BL], buses[BP], inverse)
        s = bus(bus(bus(s, BX, packet), BL, latch), BP, pointer)
    elif op == SWAP:
        s = bus(bus(s, BX, buses[BY]), BY, buses[BX])
    elif op in (OPEN, CLOSE):
        s = head(head(head(s, IV, ctl[IV] ^ ctl[EP]), CX, ctl[CX] ^ context), RUN, ctl[RUN] ^ 1)
    elif op == APPEND and ctl[AC] < d.k:
        s = bus(bus(s, BP, buses[BQ]), BQ, buses[BP])
        s = bus(bus(s, BF, buses[BF] ^ 1), BM, buses[BM] ^ d.meta(ctl[IV], ctl[CX], 1))
    return {s: 1}


def station(d, s, index, inverse=False):
    kind, *args = d.stations[index]
    ctl = s[CONTROL]
    ins = d.decode(ctl[INS])
    op, polarity = ins[:2]
    if kind == 'fetch':
        if ctl[PC] == args[0]:
            s = head(s, INS, ctl[INS] ^ s[PROGRAM][args[0]])
    elif kind == 'port':
        bank, address, lane = args
        if selected(d, ctl, ins, args):
            old = memory_value(s, bank, address)
            s = bus(memory(s, bank, address, s[BUS][lane]), lane, old)
    elif kind == 'pre' and polarity:
        s = counter(d, s, op, not inverse)
    elif kind == 'post' and not polarity:
        s = counter(d, s, op, inverse)
    elif kind == 'exec':
        return execute(d, s, ins, inverse)
    elif kind == 'pc':
        s = head(s, PC, (ctl[PC]+(-1 if inverse else 1)) % d.size)
    return {s: 1}


def step(d, s, inverse=False):
    position = s[CONTROL][POS]
    if inverse:
        position = (position-1) % d.d
        s = head(s, POS, position)
        return station(d, s, position, True)
    return {head(t, POS, (position+1) % d.d): coefficient
            for t, coefficient in station(d, s, position).items()}


def linear(vector, operation):
    result = {}
    for state, coefficient in vector.items():
        for target, value in operation(state).items():
            result[target] = result.get(target, 0) + coefficient*value
    return {s: c for s, c in result.items() if c}


def norm(vector):
    return sum(c*c for c in vector.values())


def energy(d, s):
    def packet(p):
        return p[0]+hfield(p[1])+p[2]
    return (sum(packet(p) for p in s[PK])+2*s[LA]+1+2*d.k
            +packet(s[BUS][BX])+packet(s[BUS][BY])+2*s[BUS][BL]
            +d.baths+d.k+d.size+17)


def identity_station(d, s, index):
    """Only state-independent-on-payload identity predicates may coalesce."""
    item, ctl = d.stations[index], s[CONTROL]
    op, polarity, *unused = d.decode(ctl[INS])
    if item[0] == 'fetch':
        return ctl[PC] != item[1]
    if item[0] == 'port':
        return not selected(d, ctl, d.decode(ctl[INS]), item[1:])
    if item[0] == 'pre':
        return not polarity or op not in (COLLIDE, APPEND, CLOSE)
    if item[0] == 'post':
        return polarity or op not in (COLLIDE, APPEND, CLOSE)
    if item[0] == 'exec':
        return op == NOP
    return False


def tour(d, vector, statistics, isolate_baths=False):
    initial_controls = {s[CONTROL] for s in vector}
    assert len(initial_controls) == 1 and next(iter(initial_controls))[POS] == 0
    assert next(iter(initial_controls))[INS] == 0
    seen, skipped, active = 0, 0, 0
    for index, item in enumerate(d.stations):
        representative = next(iter(vector))
        ctl = representative[CONTROL]
        if isolate_baths and item[0] == 'port' and item[1] == BA:
            assert not selected(d, ctl, d.decode(ctl[INS]), item[1:])
        seen += 1
        if identity_station(d, representative, index):
            skipped += 1
            continue
        # Common controls hold at entry and after every active station;
        # skipped identities cannot change them on any amplitude.
        assert all(s[CONTROL] == ctl for s in vector)
        # Exact head translations through individually checked identity stations.
        vector = {head(s, POS, index): c for s, c in vector.items()}
        def actual_step(s):
            result = step(d, s)
            if isolate_baths:
                assert all(t[BA] == s[BA] for t in result)
            return result
        vector = linear(vector, actual_step)
        next_controls = next(iter(vector))[CONTROL]
        assert all(s[CONTROL] == next_controls for s in vector)
        active += 1
    assert seen == active+skipped == d.d
    assert all(s[CONTROL][POS] == 0 and s[CONTROL][INS] == 0 for s in vector)
    statistics['tours'] += 1
    statistics['ticks'] += d.d
    statistics['active'] += active
    statistics['identity'] += skipped
    return vector


# Independent direct logical reference: no port selection or routing helpers.
def reference_counter(d, state, opcode, backwards):
    values = list(state[CONTROL])
    if opcode == CLOSE:
        values[EP] = (values[EP]+1-2*backwards) % (d.k+1)
    if opcode == APPEND:
        old = (values[AC]-backwards) % (d.k+1)
        values[FA] = (values[FA]+(1-2*backwards)*(old == d.k)) % (d.size+1)
        values[AC] = old if backwards else (old+1) % (d.k+1)
    if opcode == COLLIDE:
        old = (values[BC]-backwards) % (d.baths+1)
        values[FB] = (values[FB]+(1-2*backwards)*(old == d.baths)) % (d.size+1)
        values[BC] = old if backwards else (old+1) % (d.baths+1)
    return put(state, CONTROL, tuple(values))


def reference_receiver(d, packet, latch, pointer, undo):
    presence, field, reserve = packet
    supported = presence == 1 and (field in FIELDS if d.toy else hfield(field) <= 5)
    if not supported:
        return packet, latch, pointer
    translation = (1, 0, 2, 4)[FIELDS.index(field)] if d.toy else source_code(field)
    if (not undo and latch == 0 and reserve >= 2):
        return (presence, field, reserve-2), 1, (pointer+translation) % d.mod
    if not undo and latch == 1:
        return (presence, field, reserve+2), 0, pointer
    if undo and latch == 1:
        return (presence, field, reserve+2), 0, (pointer-translation) % d.mod
    if undo and latch == 0 and reserve >= 2:
        return (presence, field, reserve-2), 1, pointer
    return packet, latch, pointer


def reference_gate(d, state, instruction):
    op, undo, i, j, x, y, k = instruction
    ctl = state[CONTROL]
    if op == COLLIDE and ctl[BC] < d.baths:
        p, b = state[PT][i], state[BA][ctl[BC]]
        pair = (2*j, 2*((j+1) % d.length))
        if p not in pair:
            return {state: 1}
        column = pair.index(p)
        # Q/J and J*/(I-|s><s|) bath blocks, independent of reflection code.
        if b == 0:
            coefficients = ((1, 1), (1, 1)) if column == 0 else ((1, 1), (-1, -1))
        else:
            coefficients = ((1, -1), (1, -1)) if column == 0 else ((1, -1), (-1, 1))
        result = {}
        for bath in (0, 1):
            for pointer in (0, 1):
                target = memory(memory(state, PT, i, pair[pointer]), BA, ctl[BC], bath)
                result[target] = HALF*coefficients[bath][pointer]
        return result
    if op in (PLUS, MINUS):
        packet = state[PK][0]
        if ctl[CX] == 1 and packet[0] == 1 and packet[1] in FIELDS:
            column = FIELDS.index(packet[1])
            return {memory(state, PK, 0, (1, FIELDS[row], packet[2])): HALF*HAD[row][column]
                    for row in range(4)}
    elif op == RECEIVER:
        p, l, q = reference_receiver(d, state[PK][d.n-1], state[LA], state[PT][0], undo)
        state = memory(memory(memory(state, PK, d.n-1, p), LA, 0, l), PT, 0, q)
    elif op == SWAP:
        px, py = state[PK][x], state[PK][y]
        state = memory(memory(state, PK, x, py), PK, y, px)
    elif op in (OPEN, CLOSE):
        values = list(ctl)
        values[IV] ^= values[EP]
        values[CX] ^= k
        values[RUN] ^= 1
        state = put(state, CONTROL, tuple(values))
    elif op == APPEND and ctl[AC] < d.k:
        a = ctl[AC]
        active, archived = state[PT][0], state[PT][a+1]
        state = memory(memory(state, PT, 0, archived), PT, a+1, active)
        state = memory(state, FL, a, state[FL][a] ^ 1)
        encoding = ctl[IV] + 2**d.ew*ctl[CX] + 2**(d.ew+d.cw)
        state = memory(state, ME, a, state[ME][a] ^ encoding)
    return {state: 1}


def reference_command(d, state):
    assert state[CONTROL][POS] == state[CONTROL][INS] == 0
    instruction = d.decode(state[PROGRAM][state[CONTROL][PC]])
    op, undo = instruction[:2]
    if undo:
        state = reference_counter(d, state, op, True)
    result = reference_gate(d, state, instruction)
    answer = {}
    for target, coefficient in result.items():
        if not undo:
            target = reference_counter(d, target, op, False)
        target = head(target, PC, (target[CONTROL][PC]+1) % d.size)
        answer[target] = answer.get(target, 0)+coefficient
    return answer


def gamma(n):
    bits = bin(n+1)[2:]
    return '1'*len(bits)+'0'+bits


def descriptor(d, sweeps, contexts, wait):
    identifier = b'AUDIT-I-H4'
    values = (d.n, d.k, d.length, d.baths, 2, len(contexts), wait) + tuple(sweeps) + tuple(contexts) + (d.size, d.g, d.d)
    bits = ''.join(gamma(v) for v in values)
    bits += gamma(len(identifier))+''.join(format(v, '08b') for v in identifier)+'0'
    padded = bits+'0'*7
    cursor = 0
    def read():
        nonlocal cursor
        length = 0
        while padded[cursor] == '1':
            cursor += 1
            length += 1
        cursor += 1
        value = int(padded[cursor:cursor+length], 2)-1
        cursor += length
        return value
    assert tuple(read() for _ in values) == values
    size = read()
    assert bytes(int(padded[cursor+8*t:cursor+8*(t+1)], 2) for t in range(size)) == identifier
    cursor += 8*size
    assert padded[cursor:] == '0'*8
    return int(padded, 2), len(padded)


def compile_program(n, k, length, sweeps, contexts, wait=1, toy=False):
    baths = length*sum(sweeps)
    t, horizon = 2*n-1, len(contexts)
    useful = baths+horizon*(2*t*t+5)
    size = 2*useful+wait
    d = Device(n, k, baths, size, length, toy)
    forward = []
    for i, count in enumerate(sweeps):
        for repeat in range(count):
            for j in range(length):
                forward.append(d.word(COLLIDE, i=i, j=j))
    # Packet cycle indices: C_j=j, Q_j=T-1-j.
    transport = ([d.word(RECEIVER)]
                 + [d.word(SWAP, x=j, y=d.t-1-j) for j in range(n-1)]
                 + [d.word(SWAP, x=d.t-1-j, y=j+1) for j in range(n-1)])
    assert len(transport) == d.t
    for context in contexts:
        forward.extend((d.word(OPEN, k=context), d.word(PLUS)))
        for tick in range(2*d.t):
            forward.extend(transport)
        forward.extend((d.word(MINUS), d.word(APPEND), d.word(CLOSE, k=context)))
    assert len(forward) == useful
    program = tuple(forward + [d.word(NOP)]*wait + [word ^ 16 for word in reversed(forward)])
    assert len(program) == d.size
    description, theta_width = descriptor(d, sweeps, contexts, wait)
    return d, program, useful, description, theta_width


def initialized(d, program, description, source=0, second=False):
    packets = ( (1, FIELDS[source], 2), ) + (EMPTY,)*(d.t-1)
    pointers = tuple((2*i if second else 0) % d.mod for i in range(d.k+1))
    buses = dirty_fixture(d, 1)[BUS] if second else (EMPTY, EMPTY, 0, 0, 0, 0, 0, 0)
    return (packets, 0, pointers, (0,)*d.k, (0,)*d.k, (0,)*d.baths,
            program, description, (0,)*11, buses, 0)


def compiler_audit():
    count = collisions = round_count = 0
    for n, k in product((2, 3, 4), range(4)):
        choices = ((0,)*(k+1), (1,)*(k+1), tuple(i % 2 for i in range(k+1)))
        for h, sweeps, wait in product(range(k+1), choices, (1, 2)):
            contexts = tuple(t % 2 for t in range(h))
            d, tape, useful, encoded, tw = compile_program(n, k, 613, sweeps, contexts, wait)
            assert encoded < 2**tw
            expected_collisions = [(i, j) for i in range(k+1) for _ in range(sweeps[i]) for j in range(613)]
            got_collisions = [(d.decode(w)[2], d.decode(w)[3]) for w in tape[:d.baths]]
            assert got_collisions == expected_collisions
            assert len(got_collisions) == 613*sum(sweeps)
            assert tape[useful:useful+wait] == (0,)*wait
            assert tape[useful+wait:] == tuple(w ^ 16 for w in reversed(tape[:useful]))
            b = a = epoch = 0
            invocation = context = running = 0
            visited, allocated = [], []
            for command_number, word in enumerate(tape[:useful]):
                op, inv, i, j, x, y, setting = d.decode(word)
                assert inv == 0
                if op == COLLIDE:
                    assert b < d.baths
                    visited.append(b)
                    b += 1
                elif op == OPEN:
                    invocation ^= epoch
                    context ^= setting
                    running ^= 1
                    assert (invocation, context, running) == (epoch, contexts[epoch], 1)
                elif op == APPEND:
                    assert a < k and (invocation, context, running) == (a, contexts[a], 1)
                    allocated.append((a, invocation, context))
                    a += 1
                elif op == CLOSE:
                    invocation ^= epoch
                    context ^= setting
                    running ^= 1
                    epoch += 1
                    assert (invocation, context, running) == (0, 0, 0)
                if op == RECEIVER:
                    rel = command_number-d.baths
                    rt, within = divmod(rel, 2*d.t*d.t+5)
                    step = (within-2)//d.t+1
                    assert within == 2+(step-1)*d.t
                    assert 1 <= step <= 2*d.t and rt < h
                    # EXEC's completed microtick and full B-step boundary.
                    receiver_tick = command_number*d.d+d.size+1+d.g+1
                    full_step_tick = (d.baths+rt*(2*d.t*d.t+5)+2+step*d.t)*d.d
                    assert 0 < full_step_tick-receiver_tick < d.t*d.d
            assert visited == list(range(d.baths)) and a == epoch == h
            assert allocated == [(t, t, contexts[t]) for t in range(h)]
            assert b == d.baths and useful*d.d < (useful+wait)*d.d <= d.size*d.d
            count += 1
            collisions += len(visited)
            round_count += h
    assert count == 180
    return count, collisions, round_count


def local_audit():
    cases = energy_checks = 0
    for parameters in ((2, 0, 0, 1, 3), (2, 1, 2, 2, 3),
                       (3, 2, 3, 3, 5), (2, 2, 3, 3, 613)):
        d = Device(*parameters)
        for f, word, polarity, pc, position in product(range(5), d.inventory(), (0, 1), range(d.size), range(d.d)):
            state = dirty_fixture(d, f)
            state = head(head(head(state, INS, word ^ (polarity << 4)), PC, pc), POS, position)
            forward, backward = step(d, state), step(d, state, True)
            assert linear(forward, lambda s: step(d, s, True)) == {state: 1}
            assert linear(backward, lambda s: step(d, s)) == {state: 1}
            assert norm(forward) == norm(backward) == 1
            for target in tuple(forward)+tuple(backward):
                assert energy(d, target) == energy(d, state)
                energy_checks += 1
            cases += 1
    return cases, energy_checks


def command_instances(d):
    cases = [(d.word(NOP), None, None)]
    cases += [(d.word(op, k=k), None, None) for op in (OPEN, CLOSE) for k in range(2)]
    cases += [(d.word(op), None, None) for op in (PLUS, MINUS, RECEIVER)]
    cases += [(d.word(SWAP, x=x, y=y), None, None) for x in range(d.t) for y in range(x+1, d.t)]
    cases += [(d.word(COLLIDE, i=i, j=j), None, b) for i in range(3) for j in (0, 612) for b in range(3)]
    cases += [(d.word(APPEND), a, None) for a in range(2)]
    cases += [(d.word(COLLIDE), None, 3), (d.word(APPEND), 2, None)]
    assert len(cases) == 40
    return cases


def command_fixture(d, instance, polarity, source, pointer, bath_bit, f):
    word, archive, bath_address = instance
    word ^= polarity << 4
    s = dirty_fixture(d, f)
    s = put(s, PROGRAM, (word,))
    s = head(head(head(s, POS, 0), PC, 0), INS, 0)
    if archive is not None:
        s = head(s, AC, archive)
    if bath_address is not None:
        s = head(s, BC, bath_address)
    op, _, i, _, x, _, _ = d.decode(word)
    target = d.n-1 if op == RECEIVER else x if op == SWAP else 0
    s = memory(s, PK, target, (1, FIELDS[source], 2))
    s = memory(s, PT, i if op == COLLIDE else 0, pointer)
    s = memory(s, BA, s[CONTROL][BC] if s[CONTROL][BC] < d.baths else 0, bath_bit)
    return s


def command_audit(statistics):
    d = Device(3, 2, 3, 1, 613)
    instances = command_instances(d)
    count = correlated = 0
    for instance, polarity, source, p, u, f in product(instances, (0, 1), range(4), (0, 1, 2, 1224, 1225), (0, 1), (0, 1)):
        state = command_fixture(d, instance, polarity, source, p, u, f)
        actual = tour(d, {state: 1}, statistics)
        expected = reference_command(d, state)
        assert actual == expected
        assert all(t[BUS] == state[BUS] for t in actual)
        assert norm(actual) == 1
        count += 1
    for instance in instances:
        left = command_fixture(d, instance, 0, 1, 0, 0, 0)
        right = command_fixture(d, instance, 0, 2, 0, 0, 0)
        left = put(bus(left, BX, EMPTY), REF, 0)
        right = put(bus(right, BX, (1, FIELDS[3], 3)), REF, 1)
        vector = {left: 1, right: Q(2, 3)}
        actual = tour(d, vector, statistics)
        expected = linear(vector, lambda s: reference_command(d, s))
        assert actual == expected and norm(actual) == Q(13, 9)
        # Factorized exact dyads retain both off-diagonal reference blocks.
        for ket, bra in product((left, right), repeat=2):
            assert (reference_command(d, ket), reference_command(d, bra)) == (
                tour(d, {ket: 1}, statistics), tour(d, {bra: 1}, statistics))
        correlated += 1
    assert count == 6400 and correlated == 40
    return count, correlated


def check_program(d, tape, useful, vector, statistics, positive=True):
    initial = dict(vector)
    expected = dict(vector)
    boundary_columns = None
    for command in range(d.size):
        isolate = d.baths <= command < useful + (d.size-2*useful)
        vector = tour(d, vector, statistics, isolate)
        expected = linear(expected, lambda s: reference_command(d, s))
        assert vector == expected and norm(vector) == norm(initial)
        if command+1 == useful:
            boundary_columns = dict(vector)
            for state in vector:
                ctl = state[CONTROL]
                h = (useful-d.baths)//(2*d.t*d.t+5)
                assert ctl[BC] == d.baths and ctl[AC] == ctl[EP] == h
                assert ctl[IV] == ctl[CX] == ctl[RUN] == ctl[FA] == ctl[FB] == 0
                if positive:
                    assert state[FL] == (1,)*h+(0,)*(d.k-h)
                assert state[LA] == 0 and state[PK][0][0] == 1 and state[PK][0][2] == 2
                assert all(packet == EMPTY for packet in state[PK][1:])
        if useful <= command < d.size-useful:
            # NOP moves only position/PC/fetch scratch; logical memory unchanged.
            for state in vector:
                assert d.decode(tape[command])[0] == NOP
    assert vector == initial
    if useful == 0:
        boundary_columns = initial
    assert boundary_columns is not None
    return boundary_columns


def measurement_program_audit(statistics):
    words = ((), (0,), (1,), (0, 0), (1, 1), (0, 1), (1, 0))
    programs = dyads = 0
    for contexts, second in product(words, (False, True)):
        d, tape, useful, description, _ = compile_program(2, 2, 613, (0, 0, 0), contexts)
        actual_columns, expected_columns = [], []
        for source in range(4):
            s = initialized(d, tape, description, source, second)
            final = check_program(d, tape, useful, {s: 1}, statistics)
            expected = {s: 1}
            for _ in range(useful):
                expected = linear(expected, lambda state: reference_command(d, state))
            assert final == expected
            for state in final:
                assert state[ME] == tuple(d.meta(t, k, 1) for t, k in enumerate(contexts))+(0,)*(2-len(contexts))
            actual_columns.append(final)
            expected_columns.append(expected)
        for i, j in product(range(4), repeat=2):
            # Exact factored representation of the complete |i><j| image.
            assert (actual_columns[i], actual_columns[j]) == (expected_columns[i], expected_columns[j])
            dyads += 1
        programs += 1
    return programs, dyads


def mm(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))


IDENTITY = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))


def ideal_histories():
    contexts_all = ((), (0,), (1,), (0, 0), (1, 1), (0, 1), (1, 0))
    histories = units = 0
    for contexts in contexts_all:
        columns = []
        for source in range(4):
            current = {(source, ()): 1}
            for context in contexts:
                for when in (0, 1):
                    if context:
                        result = {}
                        for (field, history), coefficient in current.items():
                            for row in range(4):
                                key = row, history
                                result[key] = result.get(key, 0)+coefficient*HALF*HAD[row][field]
                        current = {key: value for key, value in result.items() if value}
                    if when == 0:
                        current = {(field, history+(int(field != 0),)): value
                                   for (field, history), value in current.items()}
            columns.append(current)
        assert all(norm(column) == 1 for column in columns)
        for history in product((0, 1), repeat=len(contexts)):
            operator = IDENTITY
            for context, outcome in zip(contexts, history):
                low = tuple(tuple(Q(1, 4) if context else int(i == j == 0) for j in range(4)) for i in range(4))
                projection = low if outcome == 0 else tuple(tuple(IDENTITY[i][j]-low[i][j] for j in range(4)) for i in range(4))
                operator = mm(projection, operator)
            for i, j, x, y in product(range(4), repeat=4):
                assert columns[i].get((x, history), 0)*columns[j].get((y, history), 0) == operator[x][i]*operator[y][j]
            if len(contexts) == 2 and contexts[0] == contexts[1] and history[0] != history[1]:
                assert operator == ((0, 0, 0, 0),)*4
            if len(contexts) == 2 and contexts[0] != contexts[1]:
                assert any(value for row in operator for value in row)
            histories += 1
            units += 16
    return histories, units


def loader_program_audit(statistics):
    programs = negative = units = 0
    cases = ((1, (1, 0), (0,)), (1, (1, 0), (1,)),
             (2, (1, 0, 0), (0, 0)), (2, (1, 0, 0), (0, 1)))
    for k, sweeps, contexts in cases:
        d, tape, useful, description, _ = compile_program(2, k, 3, sweeps, contexts, toy=True)
        columns, reference_columns = [], []
        for source in range(4):
            s = initialized(d, tape, description, source)
            columns.append(check_program(d, tape, useful, {s: 1}, statistics))
            expected = {s: 1}
            for _ in range(useful):
                expected = linear(expected, lambda state: reference_command(d, state))
            reference_columns.append(expected)
        for i, j in product(range(4), repeat=2):
            assert (columns[i], columns[j]) == (reference_columns[i], reference_columns[j])
            units += 1
        for variant in range(4):
            left = put(initialized(d, tape, description, 1), REF, 0)
            right = put(initialized(d, tape, description, 2), REF, 1)
            if variant == 1:
                left, right = memory(left, PT, 0, 1), memory(right, PT, 0, 1)
            elif variant == 2:
                left, right = memory(left, BA, 0, 1), memory(right, BA, 0, 1)
            elif variant == 3:
                left, right = memory(left, FL, 0, 1), memory(right, FL, 0, 1)
            result = check_program(d, tape, useful, {left: 1, right: Q(2, 3)}, statistics, variant != 3)
            assert norm(result) == Q(13, 9)
            negative += int(variant != 0)
        programs += 1
    return programs, negative, units


def main():
    statistics = {'tours': 0, 'ticks': 0, 'active': 0, 'identity': 0}
    descriptors, baths, rounds = compiler_audit()
    print(f'PASS compiler: descriptors={descriptors} fresh_addresses={baths} rounds={rounds}')
    local, energies = local_audit()
    print(f'PASS microstep: inverse_cases={local} energy_terms={energies}')
    commands, correlations = command_audit(statistics)
    print(f'PASS routing: full_commands={commands} correlated_vectors={correlations}')
    programs, units = measurement_program_audit(statistics)
    histories, branch_units = ideal_histories()
    print(f'PASS measurement: programs={programs} full_source_units={units} ideal_histories={histories} branch_units={branch_units}')
    loaders, negatives, loader_units = loader_program_audit(statistics)
    print(f'PASS retained_loader: programs={loaders} negative_inputs={negatives} full_source_units={loader_units}')
    assert statistics['ticks'] == statistics['active']+statistics['identity']
    print('PASS timing: tours={tours} microticks={ticks} active_stations={active} proved_identity_stations={identity}'.format(**statistics))
    print('SCOPE conditional local fetched-program control; epsilon_control=0 by proof; occurrence NOT DERIVED')


if __name__ == '__main__':
    main()
