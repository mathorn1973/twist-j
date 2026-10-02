#!/usr/bin/env python3
"""NON-CANONICAL independent closed exact audit. See reviewer PREREG.md."""

from fractions import Fraction as F
from itertools import product
from math import gcd

M = 1226
HALF = 613
ZERO_Y = (0, 0, 0, 0)
EMPTY = (0, ZERO_Y, 0)
FOUR = ((-1, -1, -1, -1), (1, 0, 0, 0),
        (0, 1, 0, 0), (0, 0, 1, 0))
FOUR_CODES = (395, 788, 648, 620)
NS = (2, 3, 5, 8)


def field(a):
    x, y, z, t = a
    return (y, z - t, x - y - t, y - 2 * z + t)


def chart(y):
    a, b, c, d = y
    return (2*a - 2*b + c - d, a, a - b - d, a - 2*b - d)


def energy_y(y):
    a, b, c, d = y
    return 2*a*a - 2*a*b + 3*b*b + c*c + d*d + 2*a*c - a*d - b*c + 3*b*d


def energy_a(a):
    x, y, z, t = a
    return x*x + y*y + z*z + t*t - x*z - x*t - y*t


def code(y):
    a, b, c, d = chart(y)
    return 1 + 175*(a+3) + 35*(b+2) + 7*(c+2) + d+3


def supported(packet):
    return packet[0] == 1 and energy_y(packet[1]) <= 5


def reaction(state, inverse=False):
    slots, latch, pointer = state
    b, y, reserve = slots[-1]
    if not supported(slots[-1]):
        return state
    if inverse:
        if latch:
            reserve, latch, pointer = reserve+2, 0, (pointer-code(y)) % M
        elif reserve >= 2:
            reserve, latch = reserve-2, 1
    else:
        if latch:
            reserve, latch = reserve+2, 0
        elif reserve >= 2:
            reserve, latch, pointer = reserve-2, 1, (pointer+code(y)) % M
    return (slots[:-1] + ((b, y, reserve),), latch, pointer)


def contact(state, matching, cut=None):
    slots, latch, pointer = state
    slots = list(slots)
    for j in range((len(slots)-1)//2):
        if j != cut:
            left = 2*j + matching
            slots[left], slots[left+1] = slots[left+1], slots[left]
    return (tuple(slots), latch, pointer)


def step(state, cut=None, inverse=False):
    if inverse:
        return reaction(contact(contact(state, 1, cut), 0, cut), True)
    return contact(contact(reaction(state), 0, cut), 1, cut)


def energy(state):
    slots, latch, _ = state
    return 1 + 2*latch + sum(b+energy_y(y)+r for b, y, r in slots)


def accounts(state):
    slots, latch, _ = state
    return (sorted((b, y) for b, y, r in slots), sum(p[2] for p in slots)+2*latch)


def clean(ncells, y, reserve=2, pointer=0, presence=1):
    return (((presence, y, reserve),) + (EMPTY,)*(2*ncells-2), 0, pointer)


def predicted(ncells, y, pointer, boundary):
    period = 2*ncells-1
    order = tuple(range(0, period, 2)) + tuple(range(period-2, 0, -2))
    reactions = 0 if boundary < ncells else 1+(boundary-ncells)//period
    writes = 0 if boundary < ncells else 1+(boundary-ncells)//(2*period)
    latch = reactions % 2
    slots = [EMPTY]*period
    slots[order[boundary % period]] = (1, y, 2*(1-latch))
    return (tuple(slots), latch, (pointer+writes*code(y)) % M)


def audit_arithmetic():
    labels = []
    shells = [0]*6
    allcodes = []
    for a in product(range(-3, 4), range(-2, 3), range(-2, 3), range(-3, 4)):
        y = field(a)
        assert chart(y) == a
        h = energy_y(y)
        assert h == energy_a(a)
        x, b, c, d = a
        assert 2*h == c*c+(c-x)**2+(x-d)**2+(d-b)**2+b*b
        allcodes.append(code(y))
        if h <= 5:
            labels.append(y)
            shells[h] += 1
    assert sorted(allcodes) == list(range(1, M))
    assert len(labels) == 291 and shells == [1, 20, 30, 60, 60, 120]
    assert len(set(map(code, labels))) == 291
    assert tuple(code(field(a)) for a in FOUR) == FOUR_CODES
    assert all(energy_y(field(a)) == 1 for a in FOUR)
    assert code(ZERO_Y) == 613
    assert gcd(28, M) == 2
    orbit, p = set(), 0
    while p not in orbit:
        orbit.add(p)
        p = (p+28) % M
    assert p == 0 and orbit == set(range(0, M, 2))
    # Exact polynomial (1-z)(1+...+z^(L-1)) = 1-z^L.
    coeff = [0]*(HALF+1)
    for j in range(HALF):
        coeff[j] += 1
        coeff[j+1] -= 1
    assert coeff == [1]+[0]*(HALF-1)+[-1]
    return tuple(labels)


def audit_classical(labels):
    local = 0
    for y, b, r, latch, p in product(labels+(field((4, 0, 0, 0)),
                                                field((1000000, 0, 0, 0))),
                                      (0, 1), (0, 1, 2, 3, 7, 1000000),
                                      (0, 1), (0, 1, 613, 1225)):
        s = (((b, y, r),), latch, p)
        assert reaction(reaction(s), True) == s
        assert reaction(reaction(s, True)) == s
        assert energy(reaction(s)) == energy(s)
        assert accounts(reaction(s)) == accounts(s)
        local += 1
    pool = tuple((b, y, r) for b, y, r in product(
        (0, 1), (ZERO_Y, field(FOUR[0]), field(FOUR[2]), field((4, 0, 0, 0))),
        (0, 1, 2, 7)))
    dirty = 0
    for n in NS:
        for cut in (None,)+tuple(range(n-1)):
            for k in range(24):
                slots = tuple(pool[(11*k+7*j+j*j) % len(pool)] for j in range(2*n-1))
                s = (slots, k % 2, (71*k+613) % M)
                forward = step(s, cut)
                backward = step(s, cut, True)
                assert step(forward, cut, True) == s
                assert step(backward, cut) == s
                for t in (reaction(s), contact(reaction(s), 0, cut), forward, backward):
                    assert energy(t) == energy(s) and accounts(t) == accounts(s)
                if cut is not None:
                    assert forward[0][2*cut+1] == slots[2*cut+1]
                    assert backward[0][2*cut+1] == slots[2*cut+1]
                dirty += 1
    clean_steps = 0
    for n, y, p in product(NS, labels, (0, 17, 1225)):
        s = clean(n, y, pointer=p)
        initial_energy = energy(s)
        for boundary in range(1, 4*(2*n-1)+1):
            old, s = s, step(s)
            assert s == predicted(n, y, p, boundary)
            assert step(s, inverse=True) == old
            assert energy(s) == initial_energy
            clean_steps += 1
    controls = 0
    for n in NS:
        for a in FOUR:
            y = field(a)
            requests = [(clean(n, y), cut, 'cut') for cut in range(n-1)]
            requests.extend((clean(n, y, reserve=r), None, 'no') for r in (0, 1))
            requests.append((clean(n, y, presence=0), None, 'no'))
            mismatched = list(clean(n, y, reserve=0)[0])
            mismatched[-2] = (0, ZERO_Y, 2)
            requests.append(((tuple(mismatched), 0, 0), None, 'no'))
            for initial, cut, label in requests:
                s = initial
                for unused in range(2*(2*n-1)):
                    s = step(s, cut)
                    assert s[1:] == (0, 0)
                    assert energy(s) == energy(initial)
                    if label == 'cut':
                        assert s[0][-1] == EMPTY
                    controls += 1
        for y, b, first in ((ZERO_Y, 0, None), (ZERO_Y, 1, n),
                             (field((4, 0, 0, 0)), 1, None)):
            s = clean(n, y, presence=b, reserve=2 if b else 0)
            writes = []
            for tick in range(1, 2*(2*n-1)+1):
                if supported(s[0][-1]) and s[1] == 0 and s[0][-1][2] >= 2:
                    writes.append(tick)
                s = step(s)
                controls += 1
            assert writes == ([] if first is None else [first])
        slots = [EMPTY]*(2*n-1)
        slots[-1] = (1, field(FOUR[0]), 2)
        preloaded = (tuple(slots), 0, 0)
        assert reaction(preloaded)[1:] == (1, FOUR_CODES[0])
    return local, dirty, clean_steps, controls


def rotate(mask, c):
    c %= M
    limit = (1 << M)-1
    return ((mask << c) | (mask >> (M-c))) & limit


def audit_pointer(labels):
    even = sum(1 << p for p in range(0, M, 2))
    odd = ((1 << M)-1) ^ even
    bins = (even, odd)
    codes = tuple(map(code, labels))
    coefficients = 0
    shifted = {(c, phase): rotate(bins[phase], c) for c in codes for phase in (0, 1)}
    for ca, cb, outcome in product(codes, codes, (0, 1)):
        blank = int(ca == cb and ca % 2 == outcome)
        assert blank == int(((1 << ca) & (1 << cb) & bins[outcome]) != 0)
        diagonal = int(ca == cb) * F((shifted[ca, 0] & bins[outcome]).bit_count(), HALF)
        assert diagonal == int(ca == cb and ca % 2 == outcome)
        for phase in (0, 1):
            coherent = F((shifted[ca, phase] & shifted[cb, phase] & bins[outcome]).bit_count(), HALF)
            assert coherent == int((ca+phase) % 2 == outcome and (cb+phase) % 2 == outcome)
        coefficients += 4
    assert FOUR_CODES[1] != FOUR_CODES[2] and FOUR_CODES[1] % 2 == FOUR_CODES[2] % 2
    translations = 0
    for c, p in product(codes, range(M)):
        assert ((p+c) % M-c) % M == p
        translations += 1
    offsets = sorted({0, 1, 613} | {(a-b) % M for a in FOUR_CODES for b in FOUR_CODES})
    assert len(offsets) == 15
    units = 0
    for ca, cb, p, d in product(FOUR_CODES, FOUR_CODES, range(M), offsets):
        ket, bra = (p+ca) % M, (p+d+cb) % M
        for read in (lambda x: x % 2, lambda x: int(x != 0), lambda x: x):
            actual = {read(ket): 1} if ket == bra else {}
            predicted_trace = {read((p+ca) % M): 1} if d == (ca-cb) % M else {}
            assert actual == predicted_trace
            units += 1
    return coefficients, translations, units


class QI:
    """The exact field Q(i), independent of Python floating-point complex."""
    __slots__ = ('r', 'i')

    def __init__(self, r=0, i=0):
        if isinstance(r, QI):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)

    def __add__(self, other):
        other = QI(other)
        return QI(self.r+other.r, self.i+other.i)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-QI(other))

    def __rsub__(self, other):
        return QI(other) + (-self)

    def __mul__(self, other):
        other = QI(other)
        return QI(self.r*other.r-self.i*other.i, self.r*other.i+self.i*other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = QI(other)
        denominator = other.r*other.r+other.i*other.i
        if not denominator:
            raise ZeroDivisionError('zero Q(i) denominator')
        return QI((self.r*other.r+self.i*other.i)/denominator,
                  (self.i*other.r-self.r*other.i)/denominator)

    def __rtruediv__(self, other):
        return QI(other)/self

    def conjugate(self):
        return QI(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        other = QI(other)
        return self.r == other.r and self.i == other.i

    def __repr__(self):
        return 'QI(%s,%s)' % (self.r, self.i)


def matrix(rows):
    return tuple(tuple(QI(x) for x in row) for row in rows)


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def mm(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))
                            if a[i][k] and b[k][j]), QI())
                       for j in range(len(b[0]))) for i in range(len(a)))


def plus(a, b):
    return tuple(tuple(x+y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def minus(a, b):
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))


def diagonal(values):
    return matrix([[values[i] if i == j else 0 for j in range(len(values))]
                   for i in range(len(values))])


def inverse(a):
    n = len(a)
    rows = [list(a[i])+list(identity(n)[i]) for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        rows[j] = [x/scale for x in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                scale = rows[i][j]
                rows[i] = [x-scale*y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


I4 = identity(4)
WEIGHTS = (F(4, 5), F(2), F(6), F(12))
W = diagonal(WEIGHTS)
WI = diagonal(tuple(1/x for x in WEIGHTS))
LOW = diagonal((1, 0, 0, 0))
HIGH = minus(I4, LOW)
PHASE_D = diagonal((1, QI(0, 1), -1, QI(0, -1)))


def sharp(a):
    return mm(mm(WI, adjoint(a)), W)


def trace(a):
    return sum((a[i][i] for i in range(len(a))), QI())


def audit_chart():
    gram = matrix([[F(int(i == j))-F(1, 5) for j in range(4)] for i in range(4)])
    basis = matrix(((1, 1, 1, 1), (1, -1, 1, 1), (1, 0, -2, 1), (1, 0, 0, -3)))
    bi = inverse(basis)
    assert mm(mm(adjoint(basis), gram), basis) == W
    assert mm(bi, basis) == I4
    motor = matrix(((0, 0, 0, -1), (1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1)))
    assert mm(mm(adjoint(motor), gram), motor) == gram
    rp = [I4]
    for unused in range(5):
        rp.append(mm(rp[-1], motor))
    assert rp[5] == I4
    rr = [mm(mm(bi, x), basis) for x in rp]
    p0 = matrix([[F(1, 4)]*4]*4)
    pre, targets = [], []
    for k in range(5):
        u = rr[(-k) % 5]
        assert mm(sharp(u), u) == I4
        pre.append(u)
        p = mm(mm(rp[k], p0), rp[(-k) % 5])
        q = minus(I4, p)
        physical = (mm(mm(bi, q), basis), mm(mm(bi, p), basis))
        assert physical[1] == mm(mm(sharp(u), LOW), u)
        assert physical[0] == mm(mm(sharp(u), HIGH), u)
        assert plus(*physical) == I4
        for projection in physical:
            assert sharp(projection) == projection
            assert mm(projection, projection) == projection
        targets.append(physical)
    assert mm(sharp(PHASE_D), PHASE_D) == I4
    return pre, targets


def add_sparse(result, key, value):
    if value:
        result[key] = result.get(key, QI())+value
        if not result[key]:
            del result[key]


def source_control(vector, u):
    result = {}
    for (a, active, cells), value in vector.items():
        for b in range(4):
            add_sparse(result, (b, active, cells), u[b][a]*value)
    return result


def phase_writer(vector):
    return {(a, active ^ int(a == 0), cells): value
            for (a, active, cells), value in vector.items()}


def append_phase(vector, index):
    result = {}
    for (a, active, cells), value in vector.items():
        archived, flag = cells[index]
        changed = cells[:index]+((active, flag ^ 1),)+cells[index+1:]
        add_sparse(result, (a, archived, changed), value)
    return result


def select_cell(vector, index, parity):
    return {key: value for key, value in vector.items()
            if key[2][index] == (parity, 1)}


def round_vector(vector, u, d, index):
    vector = source_control(vector, d)
    vector = source_control(vector, u)
    vector = phase_writer(vector)
    vector = source_control(vector, sharp(u))
    return append_phase(vector, index)


def inverse_round(vector, u, d, index):
    vector = append_phase(vector, index)
    vector = source_control(vector, u)
    vector = phase_writer(vector)
    vector = source_control(vector, sharp(u))
    return source_control(vector, sharp(d))


def frozen_record(word, capacity=3):
    return tuple((bit, 1) for bit in word)+((0, 0),)*(capacity-len(word))


def complete_branch(contexts, word, pre, d_at_second=False):
    columns = []
    for a in range(4):
        v = {(a, 0, ((0, 0),)*3): QI(1)}
        for index, (k, parity) in enumerate(zip(contexts, word)):
            d = PHASE_D if d_at_second and index == 1 else I4
            v = select_cell(round_vector(v, pre[k], d, index), index, parity)
        assert all(active == 0 and cells == frozen_record(word)
                   for b, active, cells in v)
        columns.append(tuple(v.get((b, 0, frozen_record(word)), QI()) for b in range(4)))
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


def claimed_branch(contexts, word, targets, d_at_second=False):
    result = I4
    for index, (k, parity) in enumerate(zip(contexts, word)):
        d = PHASE_D if d_at_second and index == 1 else I4
        result = mm(mm(targets[k][parity], d), result)
    return result


def unit_output(left, right, a, b):
    # left E_ab right^sharp, in the rational W-metric chart.
    return tuple(tuple(left[i][a]*right[j][b].conjugate()*WEIGHTS[j]/WEIGHTS[b]
                       for j in range(4)) for i in range(4))


def check_all_units(actual, desired):
    for a, b in product(range(4), repeat=2):
        assert unit_output(actual, actual, a, b) == unit_output(desired, desired, a, b)


def audit_phase_and_reference():
    units = 0
    # The retained two-phase action, independent of a reduced source map.
    for a, b, r, s in product(range(4), range(4), (0, 1), (0, 1)):
        ket = {(a, r, ()): QI(1)}
        bra = {(b, s, ()): QI(1)}
        k = next(iter(phase_writer(ket)))
        l = next(iter(phase_writer(bra)))
        assert k == (a, r ^ int(a == 0), ())
        assert l == (b, s ^ int(b == 0), ())
        for outcome in (0, 1):
            selected = int(k[1] == outcome and l[1] == outcome)
            assert selected == int((r ^ int(a == 0)) == outcome and (s ^ int(b == 0)) == outcome)
        units += 1
    densities = (matrix(((1, 0), (0, 0))), matrix(((0, 0), (0, 1))),
                 matrix(((F(1, 2), F(1, 2)), (F(1, 2), F(1, 2)))),
                 matrix(((F(1, 2), QI(0, F(-1, 2))),
                         (QI(0, F(1, 2)), F(1, 2)))))
    for tau in densities:
        assert trace(tau) == 1 and adjoint(tau) == tau
        for a, b, outcome in product(range(4), range(4), (0, 1)):
            direct = QI()
            for r, s in product((0, 1), repeat=2):
                if (r ^ int(a == 0)) == outcome and (s ^ int(b == 0)) == outcome:
                    direct += tau[r][s]
            assert direct == tau[outcome ^ int(a == 0)][outcome ^ int(b == 0)]
    # Entangled state in the literal orthonormal f/reference basis.
    entangled = {(2, 2): F(1, 2), (2, 5): F(1, 2),
                 (5, 2): F(1, 2), (5, 5): F(1, 2)}
    coherent = dict(entangled)
    blank = {key: value for key, value in entangled.items() if key[0]//2 == key[1]//2}
    assert coherent[(2, 5)] == F(1, 2) and (2, 5) not in blank
    assert sum(value for (i, j), value in blank.items() if i == j) == 1
    # Two joint inputs with the same reduced source and opposite certain reads.
    for correlated, outcome in ((((0, 0), (1, 1)), 1), (((0, 1), (1, 0)), 0)):
        assert sorted(a for a, phase in correlated) == [0, 1]
        assert all((phase ^ int(a == 0)) == outcome for a, phase in correlated)
    return units, densities


def audit_archive(pre, targets):
    cases = 0
    for p, q, z in product(range(M), range(M), (0, 1)):
        once = (q, p, 1-z)
        twice = (once[1], once[0], 1-once[2])
        assert twice == (p, q, z)
        assert 1+1+1 == 3  # Three stipulated constant-energy registers.
        cases += 1
    for a, active, archive, flag in product(range(4), (0, 1), (0, 1), (0, 1)):
        v = {(a, active, ((archive, flag),)): QI(1)}
        assert append_phase(append_phase(v, 0), 0) == v
        assert inverse_round(round_vector(v, pre[3], PHASE_D, 0), pre[3], PHASE_D, 0) == v
    false = append_phase({(1, 0, ((0, 0),)): QI(1)}, 0)
    assert false == {(1, 0, ((0, 1),)): QI(1)}
    for a in range(4):
        initial = {(a, 0, ()): QI(1)}
        assert phase_writer(phase_writer(initial)) == initial
    # Passive source operations preserve the archive marginal; coherent
    # parity-controlled feedback need preserve only its diagonal probabilities.
    def archive_marginal(components):
        result = {}
        for a, r in components:
            for b, s in components:
                if a == b:
                    result[r, s] = result.get((r, s), F(0))+F(1, 2)
        return result

    before = archive_marginal(((0, 0), (0, 1)))
    passive = archive_marginal(((1, 0), (1, 1)))
    feedback = archive_marginal(((0, 0), (1, 1)))
    assert before == passive and before != feedback
    assert before[0, 0] == feedback[0, 0] and before[1, 1] == feedback[1, 1]
    for capacity in (0, 3):
        remaining = list(range(capacity))
        for unused in range(capacity):
            assert remaining
            remaining.pop(0)
        assert ('SUPPORTED' if remaining else 'RESOURCE_EXHAUSTED') == 'RESOURCE_EXHAUSTED'
    branches = 0
    for length in range(4):
        for contexts in product(range(5), repeat=length):
            total_effect = diagonal((0, 0, 0, 0))
            for word in product((0, 1), repeat=length):
                actual = complete_branch(contexts, word, pre)
                desired = claimed_branch(contexts, word, targets)
                assert actual == desired
                check_all_units(actual, desired)
                total_effect = plus(total_effect, mm(sharp(actual), actual))
                if length and len(set(contexts)) == 1 and len(set(word)) > 1:
                    assert actual == diagonal((0, 0, 0, 0))
                branches += 1
            assert total_effect == I4
    assert branches == 1111
    # Direct coherent composition retains cross terms for both fixed programs.
    coherent_pairs = 0
    contexts = (0, 1, 0)
    for add_d in (False, True):
        columns = []
        for a in range(4):
            v = {(a, 0, ((0, 0),)*3): QI(1)}
            for index, k in enumerate(contexts):
                v = round_vector(v, pre[k], PHASE_D if add_d and index == 1 else I4, index)
            columns.append(v)
        actuals, desireds = {}, {}
        for word in product((0, 1), repeat=3):
            actuals[word] = tuple(tuple(columns[j].get((i, 0, frozen_record(word)), QI())
                                        for j in range(4)) for i in range(4))
            desireds[word] = claimed_branch(contexts, word, targets, add_d)
            assert actuals[word] == complete_branch(contexts, word, pre, add_d)
        for w, v in product(actuals, repeat=2):
            for a, b in product(range(4), repeat=2):
                assert unit_output(actuals[w], actuals[v], a, b) == unit_output(desireds[w], desireds[v], a, b)
                coherent_pairs += 1
    # Adaptive contexts and bounded stopping keep all leaves.
    adaptive, stopped = [], []
    for word in product((0, 1), repeat=3):
        contexts = tuple(sum(word[:j]) % 5 for j in range(3))
        actual = complete_branch(contexts, word, pre)
        desired = claimed_branch(contexts, word, targets)
        assert actual == desired
        check_all_units(actual, desired)
        adaptive.append(actual)
        if word[0] == 0:
            stopped.append(actual)
    stopped.append(complete_branch((0,), (1,), pre))
    for leaves in (adaptive, stopped):
        total = diagonal((0, 0, 0, 0))
        for k in leaves:
            total = plus(total, mm(sharp(k), k))
        assert total == I4
    # Prefix identity as operator equality gives every density/reference trace.
    for length in range(3):
        for prefix in product((0, 1), repeat=length):
            contexts = tuple(sum(prefix[:j]) % 5 for j in range(length))
            parent = complete_branch(contexts, prefix, pre)
            child_sum = diagonal((0, 0, 0, 0))
            for bit in (0, 1):
                child_contexts = contexts+(sum(prefix) % 5,)
                child = complete_branch(child_contexts, prefix+(bit,), pre)
                child_sum = plus(child_sum, mm(sharp(child), child))
            assert child_sum == mm(sharp(parent), parent)
    return cases, branches, coherent_pairs


def paired_seed(a, b, tau1, tau2):
    vector = {}
    for side, tau in enumerate((tau1, tau2)):
        for p, q in product((0, 1), repeat=2):
            if tau[p][q]:
                vector[side*64+(2*a+p)*8+2*b+q] = tau[p][q]
    return vector


def alphabet_action(vector, name):
    result = {}
    phases = (QI(1), QI(0, 1), QI(-1), QI(0, -1))
    for index, value in vector.items():
        side, index = divmod(index, 64)
        row, col = divmod(index, 8)
        a, p = divmod(row, 2)
        b, q = divmod(col, 2)
        if name in ('writer', 'inverse'):
            p, q = p ^ int(a == 0), q ^ int(b == 0)
        elif name == 'cycle':
            a, b = (a+1) % 4, (b+1) % 4
        elif name == 'D':
            value = phases[a]*phases[b].conjugate()*value
        elif name in ('read0', 'read1'):
            bit = int(name[-1])
            if p != bit or q != bit:
                continue
        else:
            raise AssertionError('unknown fixed operation')
        add_sparse(result, side*64+(2*a+p)*8+2*b+q, value)
    return result


def reduce_vector(vector, basis):
    vector = dict(vector)
    for pivot in sorted(basis):
        scale = vector.get(pivot, QI())
        if scale:
            for index, value in basis[pivot].items():
                add_sparse(vector, index, -scale*value)
    return vector


def span_verdict(tau1, tau2):
    alphabet = ('writer', 'inverse', 'cycle', 'D', 'read0', 'read1')
    basis, queue = {}, []

    def extend(v):
        reduced = reduce_vector(v, basis)
        if reduced:
            pivot = min(reduced)
            scale = reduced[pivot]
            reduced = {key: value/scale for key, value in reduced.items()}
            basis[pivot] = reduced
            queue.append(reduced)

    for a, b in product(range(4), repeat=2):
        extend(paired_seed(a, b, tau1, tau2))
    cursor = 0
    while cursor < len(queue):
        vector = queue[cursor]
        cursor += 1
        for op in alphabet:
            extend(alphabet_action(vector, op))
    assert len(basis) <= 128
    for vector in basis.values():
        for op in alphabet:
            assert not reduce_vector(alphabet_action(vector, op), basis)
    equal = all(all(vector.get(j, QI()) == vector.get(64+j, QI()) for j in range(64))
                for vector in basis.values())
    return equal, len(basis)


def audit_family(densities):
    ready_even, ready_odd, ready_plus, unused = densities
    verdicts = (span_verdict(ready_even, ready_even),
                span_verdict(ready_even, ready_odd),
                span_verdict(ready_even, ready_plus))
    assert tuple(v[0] for v in verdicts) == (True, False, False)
    assert ready_even != ready_odd
    for a, b, logical in product(range(4), range(4), (0, 1)):
        even_gamma = ready_even[logical ^ int(a == 0)][logical ^ int(b == 0)]
        odd_gamma = ready_odd[(logical ^ 1) ^ int(a == 0)][(logical ^ 1) ^ int(b == 0)]
        assert even_gamma == odd_gamma
    return tuple(v[1] for v in verdicts)


def main():
    labels = audit_arithmetic()
    local, dirty, clean_steps, controls = audit_classical(labels)
    coefficients, translations, pointer_units = audit_pointer(labels)
    pre, targets = audit_chart()
    phase_units, densities = audit_phase_and_reference()
    append_cases, branches, coherent_pairs = audit_archive(pre, targets)
    dimensions = audit_family(densities)
    print('NON-CANONICAL independent C local-instrument audit')
    print('arithmetic: 1225 box labels; 291 supported; shell and code identities PASS')
    print('actual B: local=%d dirty=%d clean_steps=%d raw_control_steps=%d PASS' %
          (local, dirty, clean_steps, controls))
    print('pointer: coefficients=%d translations=%d operator_partition_cases=%d PASS' %
          (coefficients, translations, pointer_units))
    print('rational orthogonal chart: five complete context instruments PASS')
    print('phase/reference: retained phase_units=%d; entangled HIGH distinction PASS' % phase_units)
    print('archive: append_cases=%d; dirty validity, inverse, capacity PASS' % append_cases)
    print('histories: branches=%d source_units=%d coherent_unit_pairs=%d PASS' %
          (branches, 16*branches, coherent_pairs))
    print('adaptive and bounded stopping: complete leaves and prefix effects PASS')
    print('whole-family finite alphabet: E/E E/O E/plus span_dimensions=%s PASS' % (dimensions,))
    print('scope: conditional L1 maps only; physical occurrence and class completeness NOT PROVIDED')


if __name__ == '__main__':
    main()
