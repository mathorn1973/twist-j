#!/usr/bin/env python3
"""Exact retained-program pair source; NON-CANONICAL L1 comparison model.

All execution uses integers/Fraction. This is not native U, a laboratory
implementation, a random sampler, or a physical energy-account model.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from typing import Dict, Tuple, Sequence

DIM = 9
PAIR_DIM = DIM * DIM


def dot(a: Sequence, b: Sequence):
    if len(a) != len(b):
        raise ValueError('dot dimension mismatch')
    return sum(x*y for x, y in zip(a, b))


def kron_vec(a: Sequence, b: Sequence) -> tuple:
    return tuple(x*y for x in a for y in b)


def g0_apply(x: Sequence) -> tuple:
    if len(x) != DIM:
        raise ValueError('one-cell dimension must be nine')
    s = sum(x[1:5])
    return (x[0],) + tuple(5*x[i]-s for i in range(1, 5)) + tuple(4*x[i] for i in range(5, 9))


def pair_metric_apply(x: Sequence) -> tuple:
    if len(x) != PAIR_DIM:
        raise ValueError('pair dimension must be 81')
    rows = [g0_apply(x[9*i:9*i+9]) for i in range(9)]
    cols = [g0_apply([rows[i][j] for i in range(9)]) for j in range(9)]
    return tuple(cols[j][i] for i in range(9) for j in range(9))


def q(z: Sequence[int]) -> int:
    if len(z) != 8 or any(type(a) is not int for a in z):
        raise ValueError('program must be eight integers')
    return 5*sum(a*a for a in z[:4])-sum(z[:4])**2+4*sum(a*a for a in z[4:])


def admitted(z: Sequence[int], bound: int) -> bool:
    if type(bound) is not int or bound < 1:
        return False
    return (z[5]-z[6]-z[7]) % 3 == 0 and 0 < q(z) <= bound


def basis(n: int, i: int) -> tuple:
    return tuple(int(j == i) for j in range(n))


@dataclass(frozen=True)
class PairGate:
    """U=I-v dual^T/den; identity for inadmissible program."""
    program: Tuple[int, ...]
    bound: int
    active: bool
    norm: int
    den: int
    v: tuple
    dual: tuple
    target: tuple

    def apply(self, vector: Sequence) -> tuple:
        if len(vector) != PAIR_DIM:
            raise ValueError('pair vector dimension mismatch')
        if not self.active:
            return tuple(F(x) for x in vector)
        c = F(dot(self.dual, vector), self.den)
        return tuple(F(x)-c*a for x, a in zip(vector, self.v))

    def column(self, j: int) -> Dict[int, F]:
        if not 0 <= j < PAIR_DIM:
            raise ValueError('pair basis index out of range')
        if not self.active:
            return {j: F(1)}
        c = F(self.dual[j], self.den)
        out = {i: -c*a for i, a in enumerate(self.v) if c*a}
        out[j] = out.get(j, F(0))+1
        return {i: x for i, x in out.items() if x}

    def integer_matrix(self) -> list:
        return [[self.den*int(i == j)-self.v[i]*self.dual[j]
                 for j in range(PAIR_DIM)] for i in range(PAIR_DIM)]


def compile_pair(program: Sequence[int], bound: int) -> PairGate:
    z = tuple(program)
    a = 1+q(z)
    e = basis(PAIR_DIM, 0)
    if not admitted(z, bound):
        zero = (0,)*PAIR_DIM
        return PairGate(z, bound, False, a, 1, zero, zero, tuple(F(x) for x in e))
    y = (1,)+z
    w = kron_vec(y, y)
    gy = g0_apply(y)
    dualw = kron_vec(gy, gy)
    v = tuple(a*x-t for x, t in zip(e, w))
    dual = tuple(a*x-t for x, t in zip(e, dualw))
    return PairGate(z, bound, True, a, a*(a-1), v, dual,
                    tuple(F(t, a) for t in w))


@dataclass(frozen=True)
class SourceState:
    """Sparse joint rational vector. Key=(P,B0,...,B(K-1),spectator).

    The last factor is an arbitrary retained spectator label. Old port data
    can be correlated with it. The digital counter is explicitly unbounded.
    """
    program: Tuple[int, ...]
    bound: int
    capacity: int
    counter: int
    amplitudes: dict

    def __post_init__(self):
        q(self.program)
        if type(self.capacity) is not int or self.capacity < 1:
            raise ValueError('capacity must be positive')
        if type(self.counter) is not int:
            raise ValueError('counter must be integer')
        for key in self.amplitudes:
            if len(key) != self.capacity+2:
                raise ValueError('wrong joint basis key length')
            if any(type(j) is not int or not 0 <= j < PAIR_DIM for j in key[:-1]):
                raise ValueError('bad pair-cell basis index')
            if type(key[-1]) is not int or key[-1] < 0:
                raise ValueError('bad spectator label')


def ready_source(program: Sequence[int], bound: int, capacity: int,
                 old_port: dict) -> SourceState:
    """old_port maps (port_basis,spectator_label) to rational amplitude."""
    amps = {(p,)+(0,)*capacity+(s,): F(c) for (p, s), c in old_port.items() if c}
    return SourceState(tuple(program), bound, capacity, 0, amps)


def local_gate(amps: dict, position: int, gate: PairGate) -> dict:
    out = {}
    columns = {}
    for key, value in amps.items():
        j = key[position]
        if j not in columns:
            columns[j] = gate.column(j)
        for i, c in columns[j].items():
            newkey = key[:position]+(i,)+key[position+1:]
            out[newkey] = out.get(newkey, F(0))+value*c
    return {k: c for k, c in out.items() if c}


def swap(amps: dict, a: int, b: int) -> dict:
    out = {}
    for key, c in amps.items():
        k = list(key)
        k[a], k[b] = k[b], k[a]
        out[tuple(k)] = c
    return out


def tick(state: SourceState, inverse: bool = False) -> SourceState:
    """One total reversible addressed step. No outcome sampling."""
    n = state.counter-1 if inverse else state.counter
    gate = compile_pair(state.program, state.bound)
    data = state.amplitudes
    if gate.active and 0 <= n < state.capacity:
        pos = n+1
        if inverse:
            data = local_gate(swap(data, 0, pos), pos, gate)
        else:
            data = swap(local_gate(data, pos, gate), 0, pos)
    return SourceState(state.program, state.bound, state.capacity,
                       state.counter+(-1 if inverse else 1), data)


def lifecycle(state: SourceState) -> str:
    if not admitted(state.program, state.bound):
        return 'INVALID_PROGRAM_NO_ADMITTED_OUTPUT'
    if state.counter < 0:
        return 'BEFORE_SUPPORTED_START'
    if state.counter < state.capacity:
        return 'CAPACITY_AVAILABLE'
    return 'SUPPLY_EXHAUSTED_DATA_RETAINED'


def capture(input_label: Sequence[int], program: Sequence[int], archive: Sequence[int],
            modulus: int, inverse: bool = False) -> tuple:
    """Swap occupied program into a supplied archive, then modular COPY.

    A fresh zero archive gives a faithful new program. A dirty archive is
    still handled reversibly, but does not satisfy the fresh-capture promise.
    """
    if modulus < 2 or not (len(input_label) == len(program) == len(archive)):
        raise ValueError('invalid capture dimensions/modulus')
    x, p, a = tuple(input_label), tuple(program), tuple(archive)
    if inverse:
        return x, a, tuple((u-v) % modulus for u, v in zip(p, x))
    return x, tuple((u+v) % modulus for u, v in zip(a, x)), p


def program_modulus(bound: int) -> int:
    if bound < 1:
        raise ValueError('positive bound required')
    return 2*isqrt(bound)+1
