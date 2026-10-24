"""NON-CANONICAL independent exact challenger for the frozen delay candidate.

Authored from PREREG.md, independently of the primary and predecessor code.
The running state is a flat list of 95 integers. Scalar formulas implement
the dynamics; separate matrix certificates and energy-difference recognition
audit them. No third-party modules, filesystem inputs, floats or searches.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product


R = [1, -2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
AM = [1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0]
ZM = [0] * 12
ZERO = [0] * 6
RESOURCES = (30, 61, 92, 93, 94)
C = [[1, -1], [-1, 0], [0, 1], [0, 1]]
D = [[1, 1, 1, 0], [-1, -1, 0, -1], [0, 0, -1, 1]]
K = [[6, 2, -1, 2], [2, 6, 2, -1], [-1, 2, 6, 2], [2, -1, 2, 6]]
A = [[1, 0, 1, 0], [0, 1, 0, 1], [-2, 1, -1, 1], [1, -3, 1, -2]]
B = [[4, -2, 2, -1], [-2, 6, -1, 3], [2, -1, 2, 0], [-1, 3, 0, 2]]
L = [[1, -3, -1, -2], [-3, 4, -2, 1], [0, 5, 1, 2], [5, -5, 2, -1]]
N = [[1, 2, 1, 2], [2, -1, 2, -1], [0, -5, 1, -3], [-5, 5, -3, 4]]


def qform(v):
    a, b, c, d = v
    return (6 * (a*a + b*b + c*c + d*d)
            + 4 * (a*b + a*d + b*c + c*d) - 2 * (a*c + b*d))


def hform(v):
    a, b, c, d = v
    return 2*a*a + 3*b*b + c*c + d*d - 2*a*b + 2*a*c - a*d - b*c + 3*b*d


def raw_energy(z):
    e0, e1, e2, e3, m0, m1 = z
    return (e0*e0 + e1*e1 + e2*e2 + e3*e3 + m0*m0 + m1*m1
            + e0*(m0-m1) - e1*m0 + (e2+e3)*m1)


def pfield(v):
    a, b, c, d = v
    return [a-b, -a, b, b, c, d]


def sfield(u, v):
    return [u, u, v, u-v, 0, 0]


def stretch(v):
    a, b, c, d = v
    return [a-3*b-c-2*d, -3*a+4*b-2*c+d, 5*b+c+2*d, 5*a-5*b+2*c-d]


def five_preimage(v):
    a, b, c, d = v
    return [a+2*b+c+2*d, 2*a-b+2*c-d, -5*b+c-3*d, -5*a+5*b-3*c+4*d]


def field_forward(z):
    e0, e1, e2, e3, m0, m1 = z
    e0, e1, e2, e3 = e0+m0-m1, e1-m0, e2+m1, e3+m1
    return [e0, e1, e2, e3, m0-e0+e1, m1+e0-e2-e3]


def field_backward(z):
    e0, e1, e2, e3, m0, m1 = z
    m0, m1 = m0+e0-e1, m1-e0+e2+e3
    return [e0-m0+m1, e1+m0, e2-m1, e3-m1, m0, m1]


def boundary(z):
    e0, e1, e2, e3 = z[:4]
    return (e0+e1+e2, -e0-e1-e3, -e2+e3)


def add(x, y):
    return [a+b for a, b in zip(x, y)]


def reaction(cell):
    """Whole-input rejection, with recognition preceding any write."""
    matter = cell[:12]
    if matter != R and matter != AM:
        return cell[:]
    e0, e1, e2, e3, c, d = cell[24:30]
    g = 2*e0 - 3*e1 + e2 + e3
    if g % 5:
        return cell[:]
    a = g // 5
    b = (-e0-e1+2*e2+2*e3) // 5
    u = (2*e0+2*e1+e2+e3) // 5
    v = (e0+e1+3*e2-2*e3) // 5
    y = [a, b, c, d]
    if matter == R:
        if (a+2*b) % 5 or (c+2*d) % 5:
            return cell[:]
        numerator = five_preimage(y)
        assert all(n % 5 == 0 for n in numerator)
        low = [n // 5 for n in numerator]
        balance = cell[30] + 4*hform(low) - 2
        target, new_field = AM, pfield(low)
    else:
        balance = cell[30] + 2 - 4*hform(y)
        target, new_field = R, pfield(stretch(y))
    if balance < 0:
        return cell[:]
    out = cell[:]
    out[:12] = target
    out[24:30] = add(new_field, sfield(u, v))
    out[30] = balance
    return out


def resource_values(state):
    return tuple(state[j] for j in RESOURCES)


def legal(state):
    assert len(state) == 95
    assert all(type(value) is int for value in state)
    assert all(state[j] >= 0 for j in RESOURCES)


@lru_cache(maxsize=8192)
def cell_accounts(cell):
    """Cache exact immutable local accounts, never outcomes or assertions."""
    matter_sum = tuple(sum(cell[4*j+k] for j in range(3)) for k in range(4))
    charges = (sum(cell[:12])+sum(cell[12:16]), sum(cell[16:20]), sum(cell[20:24]))
    divergence = boundary(cell[24:30])
    defects = tuple(divergence[j]-charges[j] for j in range(3))
    energy = sum(qform(cell[j:j+4]) for j in range(0, 24, 4))
    energy += raw_energy(cell[24:30]) + cell[30]
    return energy, charges, defects, cell[12:24], matter_sum


def accounts(state):
    cells = [cell_accounts(tuple(state[31*i:31*i+31])) for i in range(3)]
    energies = tuple(cell[0] for cell in cells) + (state[93], state[94])
    conserved = (sum(energies), tuple(v for c in cells for v in c[1]),
                 tuple(v for c in cells for v in c[2]),
                 tuple(v for c in cells for v in c[3]),
                 tuple(v for c in cells for v in c[4]))
    return energies, conserved


def contact_indices(kind, i):
    return 31*(i if kind == "A" else i+1)+30, 93+i


def frames(op, cut):
    kind, i = op
    base = 31*i
    if kind == "G":
        return set(range(base, base+31)), set(range(base, base+12)) | set(range(base+24, base+31))
    if kind in ("F", "f"):
        support = set(range(base+24, base+30))
        return support, support
    if i == cut:
        return set(), set()
    support = set(contact_indices(kind, i))
    return support, support


def primitive(state, op, cut=None):
    kind, i = op
    out = state[:]
    base = 31*i
    if kind == "G":
        out[base:base+31] = reaction(state[base:base+31])
    elif kind in ("F", "f"):
        transform = field_forward if kind == "F" else field_backward
        out[base+24:base+30] = transform(state[base+24:base+30])
    elif i != cut:
        r, q = contact_indices(kind, i)
        out[r], out[q] = state[q], state[r]
    return out


G_LAYER = [("G", i) for i in range(3)]
F_LAYER = [("F", i) for i in range(3)]
f_LAYER = [("f", i) for i in range(3)]
A_LAYER = [("A", i) for i in range(2)]
B_LAYER = [("B", i) for i in range(2)]
SCHEDULE = [G_LAYER, A_LAYER, B_LAYER, F_LAYER]
BA_SCHEDULE = [G_LAYER, B_LAYER, A_LAYER, F_LAYER]
SWEEP_SCHEDULE = [G_LAYER, [("A", 0)], [("B", 0)], [("A", 1)], [("B", 1)], F_LAYER]


def inverse_schedule(schedule):
    return [[("f" if kind == "F" else "F" if kind == "f" else kind, i)
             for kind, i in reversed(layer)] for layer in reversed(schedule)]


REASONS = set()


def recognize_by_energy(before, after):
    """Audit G through raw-energy differences and all split divisibilities."""
    matter = before[:12]
    reason = "off endpoint"
    expected = before[:]
    if matter == R or matter == AM:
        e0, e1, e2, e3, c, d = before[24:30]
        numerators = [2*e0-3*e1+e2+e3, -e0-e1+2*e2+2*e3,
                      2*e0+2*e1+e2+e3, e0+e1+3*e2-2*e3]
        reason = "outside split"
        if all(value % 5 == 0 for value in numerators):
            a, b, u, v = [value // 5 for value in numerators]
            y = [a, b, c, d]
            reason = "outside image"
            n = mv(N, y)
            if matter == AM or all(value % 5 == 0 for value in n):
                new_matter = AM if matter == R else R
                new_y = [value // 5 for value in n] if matter == R else mv(L, y)
                new_z = add(pfield(new_y), sfield(u, v))
                delta = (sum(qform(matter[j:j+4]) for j in (0, 4, 8))
                         - sum(qform(new_matter[j:j+4]) for j in (0, 4, 8))
                         + raw_energy(before[24:30]) - raw_energy(new_z))
                reason = "funding R" if matter == R else "funding AM"
                if before[30] + delta >= 0:
                    expected[:12] = new_matter
                    expected[24:30] = new_z
                    expected[30] += delta
                    reason = "applied R" if matter == R else "applied AM"
    assert after == expected, reason
    REASONS.add(reason)


def audit_primitive(before, after, op, cut, before_accounts, thorough):
    legal(after)
    after_accounts = accounts(after)
    assert after_accounts[1] == before_accounts[1], ("primitive invariants", op, cut)
    reads, writes = frames(op, cut)
    assert all(after[j] == before[j] for j in range(95) if j not in writes)
    kind, i = op
    if kind == "G":
        base = 31*i
        recognize_by_energy(before[base:base+31], after[base:base+31])
        assert primitive(after, op, cut) == before
        assert primitive(after, ("F", i), cut) == primitive(primitive(before, ("F", i), cut), op, cut)
        assert after_accounts[0] == before_accounts[0]
    elif kind in ("F", "f"):
        assert primitive(after, ("f" if kind == "F" else "F", i), cut) == before
        assert after_accounts[0] == before_accounts[0]
    else:
        assert primitive(after, op, cut) == before
        energy_delta = [0]*5
        if i != cut:
            r, q = contact_indices(kind, i)
            owner = i if kind == "A" else i+1
            energy_delta[owner] = before[q]-before[r]
            energy_delta[3+i] = before[r]-before[q]
            assert after[r] == before[q] and after[q] == before[r]
        assert tuple(b-a for a, b in zip(before_accounts[0], after_accounts[0])) == tuple(energy_delta)
    if thorough:
        # Simultaneously vary every coordinate outside the declared read frame.
        perturbed = [value if j in reads else value+1 for j, value in enumerate(before)]
        other = primitive(perturbed, op, cut)
        assert all(other[j] == after[j] for j in writes), ("read frame", op)
        assert all(other[j] == perturbed[j] for j in range(95) if j not in writes)
    return after_accounts


def advance(state, schedule=SCHEDULE, cut=None, audit=False, thorough=False):
    current = state[:]
    initial = accounts(current) if audit else None
    observed = initial
    layer_states = []
    for layer in schedule:
        layer_input = current[:]
        layer_writes = set()
        for op in layer:
            reads, writes = frames(op, cut)
            assert not layer_writes.intersection(reads | writes)
            layer_writes.update(writes)
            new = primitive(current, op, cut)
            if audit:
                observed = audit_primitive(current, new, op, cut, observed, thorough)
            current = new
        if audit:
            legal(current)
            assert observed[1] == initial[1], "layer invariants"
            assert all(current[j] == layer_input[j] for j in range(95) if j not in layer_writes)
            reverse = layer_input[:]
            for op in reversed(layer):
                reverse = primitive(reverse, op, cut)
            assert reverse == current, "within-layer order"
        layer_states.append(current[:])
    if schedule == SCHEDULE and cut is None:
        a, b, c, p, q = resource_values(layer_states[0])
        assert resource_values(layer_states[1]) == (p, q, c, a, b)
        assert resource_values(layer_states[2]) == (p, a, b, q, c)
    return current


def audit_case(state, schedule=SCHEDULE, cut=None):
    legal(state)
    forward = advance(state, schedule, cut, True, True)
    inverse = inverse_schedule(schedule)
    assert advance(forward, inverse, cut, True) == state, "inverse after forward"
    backward = advance(state, inverse, cut, True)
    assert advance(backward, schedule, cut, True) == state, "forward after inverse"
    reversed_layers = [list(reversed(layer)) for layer in schedule]
    assert advance(state, reversed_layers, cut) == forward
    return forward


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def mv(matrix, vector):
    return [sum(a*b for a, b in zip(row, vector)) for row in matrix]


def mm(left, right):
    columns = transpose(right)
    return [[sum(a*b for a, b in zip(row, column)) for column in columns] for row in left]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def power(matrix, exponent):
    answer = identity(len(matrix))
    for _ in range(exponent):
        answer = mm(answer, matrix)
    return answer


def scale(matrix, factor):
    return [[factor*x for x in row] for row in matrix]


def determinant(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    result = Fraction(1)
    for j in range(len(work)):
        pivot = next((i for i in range(j, len(work)) if work[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            work[pivot], work[j] = work[j], work[pivot]
            result = -result
        diagonal = work[j][j]
        result *= diagonal
        for i in range(j+1, len(work)):
            multiplier = work[i][j] / diagonal
            for k in range(j+1, len(work)):
                work[i][k] -= multiplier * work[j][k]
    return result


def matrix_of(transform, size):
    return transpose([transform(row) for row in identity(size)])


def certificates():
    p = matrix_of(pfield, 4)
    s = transpose([sfield(1, 0), sfield(0, 1)])
    t = matrix_of(field_forward, 6)
    ti = matrix_of(field_backward, 6)
    raw_form = [[2*int(i == j) for j in range(6)] for i in range(6)]
    for i in range(4):
        for j in range(2):
            raw_form[i][4+j] = raw_form[4+j][i] = C[i][j]
    assert mm(D, C) == [[0, 0] for _ in range(3)]
    assert mm(D, p[:4]) == [[0]*4 for _ in range(3)]
    assert mm(D, s[:4]) == [[2, 1], [-3, 1], [1, -2]]
    assert mm(t, p) == mm(p, A)
    assert mm(t, s) == s
    assert power(t, 5) == identity(6)
    assert mm(t, ti) == mm(ti, t) == identity(6)
    assert mm(mm(transpose(t), raw_form), t) == raw_form
    assert mm(mm(transpose(ti), raw_form), ti) == raw_form
    assert mm(A, L) == mm(L, A)
    assert power(A, 5) == identity(4)
    assert mm(L, N) == mm(N, L) == scale(identity(4), 5)
    assert mm(mm(transpose(A), B), A) == B
    assert mm(mm(transpose(L), B), L) == scale(B, 5)
    assert matrix_of(stretch, 4) == L and matrix_of(five_preimage, 4) == N
    w = [p[i]+s[i] for i in range(6)]
    numerator = [[2, -3, 1, 1, 0, 0], [-1, -1, 2, 2, 0, 0],
                 [0, 0, 0, 0, 5, 0], [0, 0, 0, 0, 0, 5],
                 [2, 2, 1, 1, 0, 0], [1, 1, 3, -2, 0, 0]]
    assert mm(numerator, w) == mm(w, numerator) == scale(identity(6), 5)
    assert abs(determinant(w)) == 5
    for row, factor in ((1, 2), (4, 1), (5, 3)):
        assert all((numerator[row][j]-factor*numerator[0][j]) % 5 == 0 for j in range(6))
    separated = [[0]*6 for _ in range(6)]
    for i in range(4):
        separated[i][:4] = B[i]
    separated[4][4:] = [6, -2]
    separated[5][4:] = [-2, 4]
    assert mm(mm(transpose(w), raw_form), w) == separated
    v = [[1, 1, 1, 1], [2, 1, 2, 1], [0, -1, 1, 0], [-5, -2, -3, -1]]
    assert determinant(L) == 25 and determinant(v) == 1
    assert mm(L, v) == [[5, 3, 0, 0], [0, 1, 0, 0], [0, 0, 5, 3], [0, 0, 0, 1]]
    admitted = 0
    for y in product(range(5), repeat=4):
        congruence = (y[0]+2*y[1]) % 5 == 0 and (y[2]+2*y[3]) % 5 == 0
        ny = mv(N, y)
        assert congruence == all(value % 5 == 0 for value in ny)
        ay = mv(A, y)
        assert congruence == ((ay[0]+2*ay[1]) % 5 == 0 and (ay[2]+2*ay[3]) % 5 == 0)
        if congruence:
            admitted += 1
            assert mv(L, [value // 5 for value in ny]) == list(y)
    assert admitted == 25
    # Leading principal minors certify the positive forms; computed once.
    for form in (K, B, raw_form):
        assert form == transpose(form)
        for size in range(1, len(form)+1):
            assert determinant([row[:size] for row in form[:size]]) > 0
    assert sum(qform(R[j:j+4]) for j in (0, 4, 8)) == 18
    assert sum(qform(AM[j:j+4]) for j in (0, 4, 8)) == 20
    assert [sum(R[4*j+k] for j in range(3)) for k in range(4)] == [1, -2, 1, 0]
    assert [sum(AM[4*j+k] for j in range(3)) for k in range(4)] == [1, -2, 1, 0]
    assert sum(R) == sum(AM) == 0
    assert hform([0, 0, 1, 0]) == 1 and hform([0, 0, 1, 1]) == 2
    assert stretch([0, 0, 1, 0]) == [-1, -2, 1, 2]
    assert pfield(stretch([0, 0, 1, 0])) == [1, 1, -2, -2, 1, 2]
    assert pfield([0, 0, 1, 0]) == [0, 0, 0, 0, 1, 0]
    # Polarization audits each independently expanded scalar energy formula.
    for form, scalar, multiplier in ((K, qform, 1), (B, hform, 2), (raw_form, raw_energy, 2)):
        basis = identity(len(form))
        for i, x in enumerate(basis):
            assert multiplier*scalar(x) == form[i][i]
            for j, y in enumerate(basis):
                assert multiplier*(scalar(add(x, y))-scalar(x)-scalar(y)) == 2*form[i][j]
    # Structural support on C0--Q0--C1--Q1--C2, in either direction.
    for schedule in (SCHEDULE, inverse_schedule(SCHEDULE)):
        dependencies = [{i} for i in range(5)]
        for layer in schedule:
            old = [entry.copy() for entry in dependencies]
            touched = set()
            for kind, i in layer:
                blocks = [2*i] if kind in ("G", "F", "f") else ([2*i, 2*i+1] if kind == "A" else [2*i+1, 2*i+2])
                assert not touched.intersection(blocks)
                touched.update(blocks)
                union = set().union(*(old[j] for j in blocks))
                for j in blocks:
                    dependencies[j] = union
        assert all(abs(i-j) <= 2 for i, causes in enumerate(dependencies) for j in causes)


def make_state(templates, resources=(0, 0, 0), channels=(0, 0), background=0):
    state = []
    static = ((0, 0),)*3 if background == 0 else ((1, 0), (1, 0), (0, 1))
    for i, (matter, raw) in enumerate(templates):
        field = add(raw, sfield(*static[i]))
        spectator = []
        for charge in boundary(field):
            spectator.extend([charge, 0, 0, 0])
        if background == 2:
            spectator[0] += (1, -1, 2)[i]
        state.extend(list(matter)+spectator+field+[resources[i]])
    state.extend(channels)
    legal(state)
    return state


HIGH = [1, 1, -2, -2, 1, 2]
LOW = [0, 0, 0, 0, 1, 0]
LOW_PHASES = [HIGH, [1, -1, 0, 0, -1, 1], [-1, 0, 1, 1, 0, -2], [1, 0, -1, -1, -1, 1]]
BASE = [(R, HIGH), (ZM, ZERO), (R, ZERO)]


def finite_inventory():
    core = [(R, ZERO), (R, HIGH), (AM, LOW), (ZM, ZERO)]
    triples = [list(triple) for triple in product(core, repeat=3)]
    exceptions = [(AM, ZERO), (R, pfield(stretch([0, 0, 1, 1]))),
                  (AM, pfield([0, 0, 1, 1])), (R, pfield([0, 0, 1, -2])),
                  (R, [1, 0, 0, 0, 0, 0]), (AM[4:8]+AM[:4]+AM[8:], LOW),
                  ([0, 1, -2, 1]+[0]*8, HIGH)]
    for exceptional in exceptions:
        for i in range(3):
            triple = BASE[:]
            triple[i] = exceptional
            triples.append(triple)
    assert len(triples) == 85
    resource_triples = [(0, 0, 0), (1, 2, 5), (2, 5, 6), (5, 6, 7), (6, 7, 1), (7, 1, 2)]
    channel_pairs = [(0, 0), (1, 2), (2, 1), (3, 4)]
    count = 0
    for triple in triples:
        assert all(sum(matter) == 0 for matter, _ in triple)
        for resources, channels, background in product(resource_triples, channel_pairs, range(3)):
            state = make_state(triple, resources, channels, background)
            expected_defect = (-1, 0, 0, 1, 0, 0, -2, 0, 0) if background == 2 else (0,)*9
            assert accounts(state)[1][2] == expected_defect
            audit_case(state)
            count += 1
    assert count == 6120
    assert REASONS == {"off endpoint", "outside split", "outside image", "funding R", "funding AM", "applied R", "applied AM"}


def expected_boundary(k, resource_row, matter_row, background=0, field=None):
    templates = [(matter_row[0], LOW_PHASES[k] if field is None else field),
                 (matter_row[1], ZERO), (matter_row[2], ZERO)]
    return make_state(templates, resource_row[:3], resource_row[3:], background)


def check_path(states, schedule=SCHEDULE, cut=None, energies=None):
    for k, state in enumerate(states):
        legal(state)
        if energies is not None:
            assert accounts(state)[0] == energies[k]
        if k+1 < len(states):
            assert audit_case(state, schedule, cut) == states[k+1], ("full boundary", k+1, cut)


def boundary_witnesses():
    standard_resources = [(0, 0, 0, 0, 0), (0, 2, 0, 0, 0), (0, 0, 2, 0, 0), (0, 0, 0, 0, 0)]
    standard_matter = [(R, ZM, R), (AM, ZM, R), (AM, ZM, R), (AM, ZM, AM)]
    neutral_energy = [(23, 0, 18, 0, 0), (21, 2, 18, 0, 0), (21, 0, 20, 0, 0), (21, 0, 20, 0, 0)]
    charged_energy = [(110, 87, 56, 0, 0), (108, 89, 56, 0, 0), (108, 87, 58, 0, 0), (108, 87, 58, 0, 0)]
    for background, energies in ((0, neutral_energy), (1, charged_energy)):
        states = [expected_boundary(k, standard_resources[k], standard_matter[k], background) for k in range(4)]
        check_path(states, energies=energies)
        assert all(accounts(state)[1][0] == (41 if background == 0 else 253) for state in states)
        assert all(accounts(state)[1][2] == (0,)*9 for state in states)
        if background == 1:
            assert accounts(states[0])[1][1] == (2, -3, 1, 2, -3, 1, 1, 1, -2)
            assert energies[0][1] == 84+3
        # Cut 0 leaves the source isolated; its own funded inverse still acts.
        cut0_resources = [(0, 0, 0, 0, 0), (2, 0, 0, 0, 0), (0, 0, 0, 0, 0), (2, 0, 0, 0, 0)]
        cut0_matter = [(R, ZM, R), (AM, ZM, R), (R, ZM, R), (AM, ZM, R)]
        cut0_fields = [HIGH, LOW_PHASES[1], [-1, -1, 2, 2, 1, -3], LOW_PHASES[3]]
        cut0 = [expected_boundary(k, cut0_resources[k], cut0_matter[k], background, cut0_fields[k]) for k in range(4)]
        check_path(cut0, cut=0)
        cut1_resources = [(0, 0, 0, 0, 0), (0, 2, 0, 0, 0), (0, 0, 0, 2, 0), (2, 0, 0, 0, 0)]
        cut1 = [expected_boundary(k, cut1_resources[k], (R if k == 0 else AM, ZM, R), background) for k in range(4)]
        check_path(cut1, cut=1)
        for cut, path in enumerate((cut0, cut1)):
            assert path[0] == states[0]
            assert all(state[62:93] == states[0][62:93] for state in path)
            assert all(state[93+cut] == states[0][93+cut] for state in path)
        # Ready target has no funded local move and its static field is fixed.
        target = states[0][62:93]
        assert reaction(target) == target and field_forward(target[24:30]) == target[24:30]
    paid_resources = [(0, 0, 0, 0, 0), (0, 2, 0, 0, 0), (0, 0, 0, 0, 0)]
    paid_matter = [(R, R, R), (AM, R, R), (AM, AM, R)]
    paid = [expected_boundary(k, paid_resources[k], paid_matter[k]) for k in range(3)]
    check_path(paid, energies=[(23, 18, 18, 0, 0), (21, 20, 18, 0, 0), (21, 20, 18, 0, 0)])
    assert all(accounts(state)[1][0] == 59 for state in paid)
    # Nonimage control: P A^k y supplies independent expected raw coordinates.
    y = [0, 0, 1, -2]
    nonimage = []
    for k in range(4):
        phase = mv(power(A, k), y)
        assert not ((phase[0]+2*phase[1]) % 5 == 0 and (phase[2]+2*phase[3]) % 5 == 0)
        raw = pfield(phase)
        assert raw_energy(raw) == 5
        state = make_state([(R, raw), (ZM, ZERO), (R, ZERO)])
        assert primitive(state, ("G", 0)) == state
        nonimage.append(state)
    assert primitive(nonimage[0], ("F", 0)) != nonimage[0]
    check_path(nonimage)
    assert all(state[62:93] == nonimage[0][62:93] for state in nonimage)
    # Three exposed alternatives have different complete states and delays.
    ba_resources = [(0, 0, 0, 0, 0), (0, 0, 0, 2, 0), (0, 0, 0, 0, 2), (0, 0, 2, 0, 0)]
    ba = [expected_boundary(k, ba_resources[k], (R if k == 0 else AM, ZM, R)) for k in range(4)]
    check_path(ba, BA_SCHEDULE)
    sweep_resources = [(0, 0, 0, 0, 0), (0, 0, 2, 0, 0), (0, 0, 0, 0, 0)]
    sweep_matter = [(R, ZM, R), (AM, ZM, R), (AM, ZM, AM)]
    sweep = [expected_boundary(k, sweep_resources[k], sweep_matter[k]) for k in range(3)]
    check_path(sweep, SWEEP_SCHEDULE)
    neutral = [expected_boundary(k, standard_resources[k], standard_matter[k]) for k in range(4)]
    assert neutral[1] != ba[1] and neutral[1] != sweep[1] and ba[1] != sweep[1]


def occupied_and_wrong_controls():
    empty = [(ZM, ZERO)]*3
    occupied = make_state(empty, (0, 1, 2), (3, 4))
    expected = make_state(empty, (3, 0, 1), (4, 2))
    reverse_order = make_state(empty, (1, 2, 4), (0, 3))
    assert audit_case(occupied) == expected
    assert audit_case(occupied, BA_SCHEDULE) == reverse_order
    assert accounts(occupied)[1][0] == accounts(expected)[1][0] == accounts(reverse_order)[1][0] == 10
    for cut, resource_row in ((0, (0, 4, 1, 3, 2)), (1, (3, 0, 2, 1, 4))):
        expected_cut = make_state(empty, resource_row[:3], resource_row[3:])
        assert audit_case(occupied, cut=cut) == expected_cut
        assert expected_cut[93+cut] == occupied[93+cut]
        assert accounts(expected_cut)[1][0] == 10
    source = primitive(make_state(BASE), ("G", 0))
    assert (source[30], source[93]) == (2, 0)
    copied = source[:]
    copied[93] = copied[30]
    assert accounts(copied)[1][0] == accounts(source)[1][0]+2
    for kind in ("A", "B"):
        for i in range(2):
            r, q = contact_indices(kind, i)
            full = make_state(empty)
            full[r], full[q] = ((2, 1) if kind == "A" else (1, 2))
            vacant = full[:]
            vacant[q if kind == "A" else r] = 0
            bad_full, bad_vacant = full[:], vacant[:]
            if kind == "A":
                bad_full[r], bad_full[q] = 0, full[r]
                bad_vacant[r], bad_vacant[q] = 0, vacant[r]
            else:
                bad_full[q], bad_full[r] = 0, full[q]
                bad_vacant[q], bad_vacant[r] = 0, vacant[q]
            assert full != vacant and bad_full == bad_vacant
            assert accounts(bad_full)[1][0] == accounts(full)[1][0]-1
            assert primitive(full, (kind, i)) != primitive(vacant, (kind, i))


def main():
    certificates()
    finite_inventory()
    boundary_witnesses()
    occupied_and_wrong_controls()
    print("CHALLENGER PASS: independent delay audit; both cuts, occupied contents and order controls")


if __name__ == "__main__":
    main()
