#!/usr/bin/env python3
"""Independent exact falsifier certificate for the physical spatial cut.

NON-CANONICAL, finite audit candidate-C, L1. The separate analytical proofs
carry their own candidate-T scope. Standard library only. This file neither
imports nor reads the main verifier or its helpers. All scientific arithmetic
is exact in Q(i, sqrt(5)), using an implementation local to this file.

The nine groups audit specific wrong replacements of the declared law:
wrong native weights; missing edge interference or discarded old memory;
omitted label sectors; pulse-only instead of additive current; independent
marked copies; encoded-particle counting on arbitrary native contents;
confusion between edge eigenvalues and polar factors; whole period replaced
by its edge; and omitted contact/coin pullbacks or reversed streaming signs.

The sparse macrostep checks use finite-support states on the actual infinite
lattice. No periodic boundary or lattice truncation is introduced. The final
Gamma and common phase commute with the charge observable and therefore
cancel exactly from this charge-current audit; no approximate phase is used.

The source is handoff33 at 0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8:
homogeneous-capture-2026-10-22/proofs/homogeneous_source.md and the inherited
original-rearrangement/original_note.tex native object streaming definition.
The native SWAP input is explicitly the post-onsite-permutation pair
((h_99,1,h_99,3),(h_100,2,h_100,4)); all 5**4 patterns are retained.

Execution is permitted only after the accepted complete file and the proof
contract have been publicly pinned and read back. Static parsing is not a run.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product


@dataclass(frozen=True)
class Exact:
    """a + b sqrt(5) + i(c + d sqrt(5)), with rational coefficients."""

    a: F = F(0)
    b: F = F(0)
    c: F = F(0)
    d: F = F(0)

    def __post_init__(self):
        for name in ("a", "b", "c", "d"):
            object.__setattr__(self, name, F(getattr(self, name)))

    @staticmethod
    def coerce(value):
        if isinstance(value, Exact):
            return value
        if isinstance(value, (int, F)):
            return Exact(value)
        raise TypeError("exact scalars require int, Fraction, or Exact")

    def __add__(self, other):
        other = self.coerce(other)
        return Exact(self.a + other.a, self.b + other.b,
                     self.c + other.c, self.d + other.d)

    __radd__ = __add__

    def __neg__(self):
        return Exact(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return Exact(a*e + 5*b*f - c*g - 5*d*h,
                     a*f + b*e - c*h - d*g,
                     a*g + 5*b*h + c*e + 5*d*f,
                     a*h + b*g + c*f + d*e)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, (int, F)):
            raise TypeError("only rational denominators are used")
        other = F(other)
        if not other:
            raise ZeroDivisionError
        return Exact(self.a/other, self.b/other,
                     self.c/other, self.d/other)

    def conjugate(self):
        return Exact(self.a, self.b, -self.c, -self.d)

    def real(self):
        return Exact(self.a, self.b)

    def norm2(self):
        return self.conjugate() * self


ZERO = Exact()
ONE = Exact(1)
I = Exact(0, 0, 1)
ROOT5 = Exact(0, 1)
C = ROOT5 / 5
S = 2 * ROOT5 / 5
SIGMA = ((ONE, ZERO), (ZERO, -ONE))


def matrix(rows):
    return tuple(tuple(Exact.coerce(x) for x in row) for row in rows)


def identity(size):
    return matrix([[int(i == j) for j in range(size)] for i in range(size)])


def mm(left, right):
    assert len(left[0]) == len(right)
    return tuple(tuple(sum((left[i][k] * right[k][j]
                            for k in range(len(right))), ZERO)
                       for j in range(len(right[0])))
                 for i in range(len(left)))


def adjoint(value):
    return tuple(tuple(value[j][i].conjugate() for j in range(len(value)))
                 for i in range(len(value[0])))


def matrix_add(left, right):
    return tuple(tuple(x + y for x, y in zip(a, b))
                 for a, b in zip(left, right))


def matrix_scale(scalar, value):
    return tuple(tuple(scalar * x for x in row) for row in value)


def determinant2(value):
    return value[0][0]*value[1][1] - value[0][1]*value[1][0]


def trace2(value):
    return value[0][0] + value[1][1]


def put(state, key, amplitude):
    amplitude = Exact.coerce(amplitude)
    value = state.get(key, ZERO) + amplitude
    if value == ZERO:
        state.pop(key, None)
    else:
        state[key] = value


def inner(left, right):
    return sum((value.conjugate() * right.get(key, ZERO)
                for key, value in left.items()), ZERO)


def norm2(state):
    return inner(state, state)


def sum_states(*states):
    result = {}
    for state in states:
        for key, value in state.items():
            put(result, key, value)
    return result


# Isolated edge keys are (bank, carrier_label, old_memory_label).
def swap_labels(state):
    return {(j, i): value for (i, j), value in state.items()}


def edge_gate(state, use_swap=True):
    result = {}
    for (bank, label, memory), amplitude in state.items():
        crossed = (memory, label) if use_swap else (label, memory)
        if bank == 0:
            put(result, (0, label, memory), C * amplitude)
            put(result, (1, *crossed), S * amplitude)
        else:
            assert bank == 1
            put(result, (0, *crossed), -S * amplitude)
            put(result, (1, label, memory), C * amplitude)
    return result


def edge_current_from_right_charge(state, use_swap=True):
    def right_charge(values):
        return 4 * sum((value.norm2() for key, value in values.items()
                        if key[0] == 1), ZERO)
    return right_charge(edge_gate(state, use_swap)) - right_charge(state)


def edge_current_formula(state, use_swap=True, coherent=True):
    left = sum((value.norm2() for key, value in state.items()
                if key[0] == 0), ZERO)
    right = sum((value.norm2() for key, value in state.items()
                 if key[0] == 1), ZERO)
    cross = ZERO
    for (bank, label, memory), amplitude in state.items():
        if bank == 0:
            target = (1, memory, label) if use_swap else (1, label, memory)
            cross += state.get(target, ZERO).conjugate() * amplitude
    interference = 2*C*S*cross.real() if coherent else ZERO
    return 4 * (S*S*(left-right) + interference)


def trace_old_memory(state):
    reduced = {}
    for (bank, label, memory), value in state.items():
        for (bank2, label2, memory2), value2 in state.items():
            if memory == memory2:
                key = ((bank, label), (bank2, label2))
                put(reduced, key, value * value2.conjugate())
    return reduced


VELOCITY = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ELL = 2
RECEIVER = 3
WEIGHTS = (2, 2, 4, 2)


def physical_charge(coordinates, ell, weights=WEIGHTS):
    return sum(weight * int(position > ell)
               for weight, position in zip(weights, coordinates))


def object_current(xa, xb, coin, ell):
    va, vb = VELOCITY[coin]
    return (2*(int(xa+va > ell)-int(xa > ell))
            + 2*(int(xb+vb > ell)-int(xb > ell)))


# Full finite-support lattice keys:
# (arrangement, x_A, x_B, carrier_position, object_coin, bank, label, memory).
# The token has bank -1. The single encoded receiver is at RECEIVER.
def basis(arrangement, xa, xb, carrier, coin, bank=-1, label=0, memory=1):
    assert xa % 2 == xb % 2
    assert arrangement in ("T", "P")
    assert bank == -1 if arrangement == "T" else bank in (0, 1)
    return (arrangement, xa, xb, carrier, coin, bank, label, memory)


M2 = matrix(((1, 2*I, 2*I, -4),
             (2*I, 1, -4, 2*I),
             (2*I, -4, 1, 2*I),
             (-4, 2*I, 2*I, 1)))
M2 = matrix_scale(F(1, 5), M2)
ALPHA0 = (ZERO, I, -I, ZERO)
BETA0 = (ONE, ZERO, ZERO, -ONE)


def capture(state):
    """Use unnormalized contact vectors; their squared norms are both 2."""
    result = dict(state)
    contexts = {(xa, label, memory)
                for (arrangement, xa, xb, carrier, coin, bank, label, memory)
                in state if xa == xb == carrier}
    for site, label, memory in contexts:
        token = [state.get(basis("T", site, site, site, coin, -1,
                                 label, memory), ZERO) for coin in range(4)]
        pulse = [state.get(basis("P", site, site, site, coin, 0,
                                 label, memory), ZERO) for coin in range(4)]
        da = sum((a.conjugate()*v for a, v in zip(ALPHA0, token)), ZERO)
        db = sum((b.conjugate()*v for b, v in zip(BETA0, pulse)), ZERO)
        for coin in range(4):
            put(result, basis("T", site, site, site, coin, -1, label, memory),
                ALPHA0[coin] * (-da/5 - 2*db/5))
            put(result, basis("P", site, site, site, coin, 0, label, memory),
                BETA0[coin] * (2*da/5 - db/5))
    return result


def pulse_onsite_coin(state):
    result = {}
    for key, amplitude in state.items():
        arrangement, xa, xb, carrier, coin, bank, label, memory = key
        if arrangement == "T":
            put(result, key, amplitude)
        elif bank == 0:
            put(result, key, C*amplitude)
            put(result, basis("P", xa, xb, carrier, coin, 1, label, memory),
                S*amplitude)
        else:
            put(result, basis("P", xa, xb, carrier, coin, 0, label, memory),
                -S*amplitude)
            put(result, key, C*amplitude)
    return result


def object_coin(state):
    result = {}
    for key, amplitude in state.items():
        arrangement, xa, xb, carrier, coin, bank, label, memory = key
        for output_coin in range(4):
            put(result, basis(arrangement, xa, xb, carrier, output_coin,
                              bank, label, memory),
                M2[output_coin][coin]*amplitude)
    return result


def d0(state):
    return object_coin(pulse_onsite_coin(state))


def streaming(state, wrong_sign=False):
    result = {}
    for key, amplitude in state.items():
        arrangement, xa, xb, carrier, coin, bank, label, memory = key
        va, vb = VELOCITY[coin]
        if wrong_sign:
            va, vb = -va, -vb
        put(result, basis(arrangement, xa+va, xb+vb, carrier, coin,
                          bank, label, memory), amplitude)
    return result


def pulse_edges(state, use_swap=True):
    result = {}
    for key, amplitude in state.items():
        arrangement, xa, xb, carrier, coin, bank, label, memory = key
        if arrangement == "T":
            put(result, key, amplitude)
            continue
        put(result, key, C*amplitude)
        output_site = carrier+1 if bank == 0 else carrier-1
        right_endpoint = carrier+1 if bank == 0 else carrier
        swap = use_swap and right_endpoint == RECEIVER
        new_label, new_memory = ((memory, label) if swap else (label, memory))
        coefficient = S if bank == 0 else -S
        put(result, basis("P", xa, xb, output_site, coin, 1-bank,
                          new_label, new_memory), coefficient*amplitude)
    return result


def charge_expectation(state):
    return sum((amplitude.norm2() * physical_charge(
                (key[1], key[2], key[3], RECEIVER), ELL)
                for key, amplitude in state.items()), ZERO)


def raw_current(state, coherent=True, pulse_only=False):
    object_part = ZERO if pulse_only else sum((
        amplitude.norm2()*object_current(key[1], key[2], key[4], ELL)
        for key, amplitude in state.items()), ZERO)
    left = ZERO
    right = ZERO
    cross = ZERO
    for key, amplitude in state.items():
        arrangement, xa, xb, carrier, coin, bank, label, memory = key
        if arrangement != "P":
            continue
        if bank == 0 and carrier == ELL:
            left += amplitude.norm2()
            crossed = (memory, label) if RECEIVER == ELL+1 else (label, memory)
            target = basis("P", xa, xb, ELL+1, coin, 1, *crossed)
            cross += state.get(target, ZERO).conjugate()*amplitude
        if bank == 1 and carrier == ELL+1:
            right += amplitude.norm2()
    interference = 2*C*S*cross.real() if coherent else ZERO
    return object_part + 4*(S*S*(left-right)+interference)


def group_weights():
    cases = [((2, 0, 0, 0), 2), ((0, 2, 0, 0), 2),
             ((0, 0, 2, 0), 4), ((0, 0, 0, 2), 2),
             ((2, 2, 2, 2), 10), ((0, 0, 0, 0), 0)]
    assert all(physical_charge(coords, 0) == target for coords, target in cases)
    wrong_weights = ((1, 1, 1, 0), (4, 4, 4, 2), (2, 2, 4, 0),
                     (0, 0, 4, 0), (2, 2, 2, 2))
    for wrong in wrong_weights:
        assert any(physical_charge(coords, 0, wrong) != target
                   for coords, target in cases)
    assert sum(WEIGHTS) == 10
    token = {basis("T", 0, 0, ELL, 0): ONE}
    assert pulse_edges(token) == token
    # Receiver charge is a constant 2 on the encoded edge, not zero.
    assert (2, 6) == (2+0, 2+4)
    assert 6-2 == WEIGHTS[2]


def group_coherence():
    plus = {(0, 0, 1): ONE, (1, 1, 0): ONE}
    minus = {(0, 0, 1): ONE, (1, 1, 0): -ONE}
    for state in (plus, minus):
        assert edge_current_from_right_charge(state) == edge_current_formula(state)
        assert norm2(edge_gate(state)) == norm2(state)
    assert edge_current_formula(plus) == Exact(F(16, 5))
    assert edge_current_formula(minus) == Exact(F(-16, 5))
    assert edge_current_formula(plus, coherent=False) == ZERO
    assert edge_current_formula(plus, use_swap=False) == ZERO
    assert edge_current_from_right_charge(plus, use_swap=False) == ZERO
    assert trace_old_memory(plus) == trace_old_memory(minus)
    assert edge_current_formula(plus) != edge_current_formula(minus)
    quadrature = {(0, 0, 1): ONE, (1, 1, 0): I}
    assert edge_current_formula(quadrature) == ZERO


def group_labels():
    seen = set()
    symmetric = 0
    antisymmetric = 0
    for label, memory in product(range(26), repeat=2):
        left = {(0, label, memory): ONE}
        right = {(1, memory, label): ONE}
        assert not (set(left) | set(right)) & seen
        seen.update(left)
        seen.update(right)
        out_left, out_right = edge_gate(left), edge_gate(right)
        assert norm2(out_left) == ONE and norm2(out_right) == ONE
        assert inner(out_left, out_right) == ZERO
        assert 6*norm2(out_left) == Exact(6)
        for state in (left, right):
            assert edge_current_from_right_charge(state) == edge_current_formula(state)
        singleton = {(label, memory): ONE}
        assert swap_labels(swap_labels(singleton)) == singleton
        if label == memory:
            assert swap_labels(singleton) == singleton
            symmetric += 1
        elif label < memory:
            plus = {(label, memory): ONE, (memory, label): ONE}
            minus = {(label, memory): ONE, (memory, label): -ONE}
            assert swap_labels(plus) == plus
            assert swap_labels(minus) == {key: -value for key, value in minus.items()}
            symmetric += 1
            antisymmetric += 1
    assert len(seen) == 2*676
    assert (symmetric, antisymmetric) == (351, 325)
    assert 4*676 == 2704 and 4*2*676 == 5408


def group_additivity():
    source_exponents = ((1, 0), (0, 1), (0, -1), (-1, 0))
    checked = 0
    for xa, xb in product(range(-2, 4), repeat=2):
        if xa % 2 != xb % 2:
            continue
        center, relative = (xa+xb)//2, (xa-xb)//2
        for coin, (exponent_p, exponent_q) in enumerate(source_exponents):
            # e^(+iP) times e^(-iPn) is e^(-iP(n-1)).
            new_center, new_relative = center-exponent_p, relative-exponent_q
            new_a, new_b = new_center+new_relative, new_center-new_relative
            assert (new_a-xa, new_b-xb) == VELOCITY[coin]
            assert new_a % 2 == new_b % 2
            ua, ub = int(xa == 0), int(xb == 0)
            wa, wb = int(xa == 1), int(xb == 1)
            entries = (-2*(wa+wb), -2*wa+2*ub, 2*ua-2*wb, 2*(ua+ub))
            assert object_current(xa, xb, coin, 0) == entries[coin]
            da = int(new_a > 0)-int(xa > 0)
            db = int(new_b > 0)-int(xb > 0)
            assert da*db != -1
            checked += 1
    assert checked == 72
    assert object_current(0, 0, 3, 0) == 4
    assert object_current(1, 1, 0, 0) == -4
    both = {basis("P", ELL, ELL, ELL, 3, 0): ONE}
    actual = charge_expectation(pulse_edges(streaming(both))) - charge_expectation(both)
    assert actual == Exact(F(36, 5)) == raw_current(both)
    assert raw_current(both, pulse_only=True) == Exact(F(16, 5)) != actual
    opposite = {basis("P", ELL+1, ELL+1, ELL, 0, 0): ONE}
    assert raw_current(opposite) == Exact(F(-4, 5))
    token = {basis("T", ELL, ELL, ELL, 3): ONE}
    assert raw_current(token) == Exact(4)
    assert raw_current(token, pulse_only=True) == ZERO
    # The local post-coin compression has k=(0,2,2,4), not four equal weights.
    # Its pulse contribution has eigenvalues +/-t, t=8/sqrt(5); 2<t<4.
    assert F(4) < F(64, 5) < F(16)
    assert (1+1+1+2, 1+1+1+0) == (5, 3)


def group_marking():
    first = {basis("T", 0, 0, 0, 0): ONE}
    second = {basis("T", 4, 4, 0, 0): ONE}
    state = sum_states(first, {key: I*value for key, value in second.items()})
    marked = ZERO
    for mark, weight in enumerate(WEIGHTS):
        marked += weight*sum((value.norm2()*int(
            (key[1], key[2], key[3], RECEIVER)[mark] > ELL)
            for key, value in state.items()), ZERO)
    assert marked == charge_expectation(state)
    assert sum((weight*norm2(state) for weight in WEIGHTS), ZERO) == 10*norm2(state)
    physical_copies = (state, state, state, state)
    assert all(copy == physical_copies[0] for copy in physical_copies)
    # Remove the fixed square-root charge weights before this compatibility
    # comparison. Equal total weighted norm does not enforce a common psi.
    fake_copies = (first, second, first, first)
    assert sum((weight*norm2(copy) for weight, copy in zip(WEIGHTS, fake_copies)), ZERO) == Exact(10)
    assert not all(copy == fake_copies[0] for copy in fake_copies)
    assert first != second


def group_native_swap():
    lift = (0, 1, 2, -2, -1)

    def charge(pair):
        return 2*sum(lift[value]**2 for value in pair)

    outputs = set()
    count = 0
    for left1, left2, right1, right2 in product(range(5), repeat=4):
        left, right = (left1, left2), (right1, right2)
        output = (right1, right2, left1, left2)
        assert output not in outputs
        outputs.add(output)
        assert charge(left)+charge(right) == charge(output[:2])+charge(output[2:])
        current = charge(output[2:])-charge(right)
        assert current == charge(left)-charge(right)
        assert (output[2], output[3], output[0], output[1]) == (left1, left2, right1, right2)
        count += 1
    assert count == len(outputs) == 625
    assert charge((2, 0))-charge((0, 0)) == 8
    assert charge((2, 2))-charge((0, 0)) == 16
    wrong_encoded_count = 2*sum(int(value != 0) for value in (2, 0))
    assert wrong_encoded_count == 2 and wrong_encoded_count != 8
    assert 8 > 4  # A full-native crossing need not be bounded by pair charge 4.


def physical_edge_transfer():
    return matrix(((ROOT5/2, F(-1, 2)), (F(1, 2), -ROOT5/2)))


def group_edge_transfer():
    eye = identity(2)
    transfer = physical_edge_transfer()
    assert ROOT5*ROOT5 == Exact(5)
    assert I*I == -ONE
    assert C*C+S*S == ONE
    assert mm(transfer, transfer) == eye
    assert mm(adjoint(transfer), mm(SIGMA, transfer)) == SIGMA
    assert mm(adjoint(transfer), mm(matrix_scale(4, SIGMA), transfer)) == matrix_scale(4, SIGMA)
    assert determinant2(transfer) == -ONE and trace2(transfer) == ZERO
    a, b = ONE+I, ROOT5-I
    out_a, out_b = C*a-S*b, S*a+C*b
    transferred = mm(transfer, ((a,), (out_a,)))
    assert transferred == ((out_b,), (b,))
    polar_square = mm(adjoint(transfer), transfer)
    assert trace2(polar_square) == Exact(3)
    assert determinant2(polar_square) == ONE
    polynomial = matrix_add(matrix_add(mm(polar_square, polar_square),
                                       matrix_scale(-3, polar_square)), eye)
    assert polynomial == matrix_scale(0, eye)
    phi, inverse_phi = (ONE+ROOT5)/2, (ROOT5-ONE)/2
    assert phi*inverse_phi == ONE
    assert mm(polar_square, ((ONE,), (-ONE,))) == ((phi*phi,), (-phi*phi,))
    assert mm(polar_square, ((ONE,), (ONE,))) == ((inverse_phi*inverse_phi,),
                                               (inverse_phi*inverse_phi,))
    # sqrt(5)>1 establishes positivity of both explicitly identified factors.
    assert 5 > 1
    assert trace2(transfer) != phi+inverse_phi


def group_full_free_period():
    zeta, inverse_zeta = I, -I
    onsite = matrix_scale(ROOT5/2,
                          matrix(((-inverse_zeta, C), (-C, zeta))))
    period = mm(onsite, physical_edge_transfer())
    explicit = matrix(((ONE/4+5*I/4, -ROOT5*(ONE+I)/4),
                       (ROOT5*(I-ONE)/4, ONE/4-5*I/4)))
    assert period == explicit
    assert mm(adjoint(onsite), mm(SIGMA, onsite)) == SIGMA
    assert mm(adjoint(period), mm(SIGMA, period)) == SIGMA
    assert determinant2(period) == ONE
    assert trace2(period) == Exact(F(1, 2))
    assert mm(period, period) != identity(2)
    assert period != physical_edge_transfer()
    # zeta=i has cos(epsilon)=0, hence source dispersion gives cos(k)=1/4.
    assert F(1-5*0, 2) == 2*F(1, 4)


def group_macrostep():
    assert mm(adjoint(M2), M2) == identity(4)
    bright = {basis("T", ELL, ELL, ELL, 1): I,
              basis("T", ELL, ELL, ELL, 2): -I}
    dark = {basis("T", ELL, ELL, ELL, 0): ONE}
    bright_pulse = {basis("P", ELL, ELL, ELL, 0, 0): ONE,
                    basis("P", ELL, ELL, ELL, 3, 0): -ONE}
    correlated = {
        basis("P", 0, 0, ELL, 0, 0, 0, 1): C,
        basis("P", 0, 0, ELL, 0, 1, 0, 1): -S,
        basis("P", 0, 0, ELL+1, 0, 0, 1, 0): S,
        basis("P", 0, 0, ELL+1, 0, 1, 1, 0): C,
    }
    fixtures = (bright, dark, correlated, sum_states(bright, bright_pulse))
    for state in fixtures:
        contact = capture(state)
        pulse_coin = pulse_onsite_coin(contact)
        pre_stream = object_coin(pulse_coin)
        streamed = streaming(pre_stream)
        evolved = pulse_edges(streamed)
        for stage in (contact, pulse_coin, pre_stream, streamed, evolved):
            assert norm2(stage) == norm2(state)
        actual = charge_expectation(evolved)-charge_expectation(state)
        assert actual == raw_current(pre_stream)
    bright_current = raw_current(d0(capture(bright)))
    assert bright_current == Exact(F(3012, 625))
    assert bright_current != raw_current(d0(bright))
    assert bright_current != raw_current(capture(bright))
    dark_current = raw_current(d0(capture(dark)))
    assert dark_current == Exact(F(16, 5))
    assert dark_current != raw_current(pulse_onsite_coin(capture(dark)))
    wrong_stream = pulse_edges(streaming(d0(capture(dark)), wrong_sign=True))
    assert charge_expectation(wrong_stream)-charge_expectation(dark) != dark_current
    assert raw_current(d0(capture(dark)), pulse_only=True) != dark_current
    pre_correlated = d0(capture(correlated))
    correct = raw_current(pre_correlated)
    assert correct == Exact(F(16, 5))
    assert raw_current(pre_correlated, coherent=False) == ZERO
    wrong_memory = pulse_edges(streaming(pre_correlated), use_swap=False)
    assert charge_expectation(wrong_memory)-charge_expectation(correlated) == ZERO
    assert correct != ZERO


GROUPS = (
    ("charge weights 2,2,4,2 and standing sectors", group_weights),
    ("coherent edge current and old-memory counterexamples", group_coherence),
    ("all 676 label pairs and swap multiplicities 351,325", group_labels),
    ("additive object-plus-pulse current and common parity", group_additivity),
    ("common-state constraint for four marked copies", group_marking),
    ("all 625 native object-SWAP inputs and charge-8 witness", group_native_swap),
    ("physical edge transfer, indefinite form and golden polar factors", group_edge_transfer),
    ("free period at zeta=i has trace 1/2 and determinant 1", group_full_free_period),
    ("exact macrostep pullback and omitted-layer/sign counterexamples", group_macrostep),
)


def main():
    for index, (label, check) in enumerate(GROUPS, 1):
        check()
        print("PASS {}/9 {}".format(index, label))
    print("PASS 9 independent exact falsifier groups")


if __name__ == "__main__":
    main()
