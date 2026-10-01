"""NON-CANONICAL development runtime; no physical qualification.

Independent matrix implementation of the fixed #1316 law. The 32*N-1
signed registers exclude the authoritative, sampled physical C5 pointer.
No experiment label, trajectory table or event log is an input.
"""
from dataclasses import dataclass

C = ((1, -1), (-1, 0), (0, 1), (0, 1))
K = ((6, 2, -1, 2), (2, 6, 2, -1), (-1, 2, 6, 2), (2, -1, 2, 6))
H = ((4, -2, 2, -1), (-2, 6, -1, 3), (2, -1, 2, 0), (-1, 3, 0, 2))
L = ((1, -3, -1, -2), (-3, 4, -2, 1), (0, 5, 1, 2), (5, -5, 2, -1))
LINV5 = ((1, 2, 1, 2), (2, -1, 2, -1), (0, -5, 1, -3), (-5, 5, -3, 4))
P = ((1, -1, 0, 0), (-1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
S = ((1, 0), (1, 0), (0, 1), (1, -1), (0, 0), (0, 0))
SPLIT5 = ((2, -3, 1, 1), (-1, -1, 2, 2), (2, 2, 1, 1), (1, 1, 3, -2))
R = (1, -2, 1, 0) + (0,) * 8
AM = (1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0)
LIMITS = (6,) * 24 + (15, 9, 11, 11, 12, 18, 41)


def mv(matrix, values):
    return tuple(sum(a * b for a, b in zip(row, values)) for row in matrix)


def quadratic(matrix, values):
    return sum(a * b for a, b in zip(values, mv(matrix, values)))


def bank_counts(registers, n=3):
    result = []
    for i in range(n):
        cell = registers[31*i:31*i+31]
        e, m = cell[24:28], cell[28:30]
        result.extend((sum(quadratic(K, cell[j:j+4]) for j in range(0, 24, 4)),
                       sum(x*x for x in e+m) + sum(a*b for a, b in zip(e, mv(C, m))), cell[30]))
    return tuple(result) + tuple(registers[31*n:])


def validate(registers, pointer, n=3):
    if type(n) is not int or not 2 <= n <= 16:
        raise ValueError('supported parameter N is 2..16')
    if type(pointer) is not int or not 0 <= pointer < 5:
        raise ValueError('invalid physical p')
    if len(registers) != 32*n-1 or any(type(x) is not int for x in registers):
        raise ValueError('wrong register carrier')
    # Bounds precede every multiply and any narrowing to the 16-bit bank.
    for i in range(n):
        if any(abs(x) > bound for x, bound in zip(registers[31*i:31*i+31], LIMITS)):
            raise ValueError('coordinate bound')
        if registers[31*i+30] < 0:
            raise ValueError('negative resource')
    if any(not 0 <= x <= 41 for x in registers[31*n:]):
        raise ValueError('channel bound')
    counts = bank_counts(tuple(registers), n)
    if any(x < 0 for x in counts) or sum(counts) != 41:
        raise ValueError('outside H=41 shell')


def reaction(cell):
    matter = cell[:12]
    if matter not in (R, AM):
        return cell
    split = mv(SPLIT5, cell[24:28])
    if any(x % 5 for x in split):
        return cell
    a, b, u, v = (x//5 for x in split)
    y = (a, b) + cell[28:30]
    if matter == R:
        numerator = mv(LINV5, y)
        if any(x % 5 for x in numerator):
            return cell
        low = tuple(x//5 for x in numerator)
        balance = cell[30] + 2*quadratic(H, low)-2
        output, target = low, AM
    else:
        balance = cell[30] + 2-2*quadratic(H, y)
        output, target = mv(L, y), R
    if balance < 0:
        return cell
    raw = tuple(a+b for a, b in zip(mv(P, output), mv(S, (u, v))))
    return target + cell[12:24] + raw + (balance,)


def layer(registers, pointer, kind, *, inverse=False, cuts=0, n=3):
    validate(registers, pointer, n)
    if kind not in 'GABF' or len(kind) != 1 or type(inverse) is not bool:
        raise ValueError('layer/direction')
    if type(cuts) is not int or not 0 <= cuts < 1 << (n-1):
        raise ValueError('cut mask')
    old = tuple(registers)
    result = list(old)
    proposed_p = pointer
    if kind == 'G':
        for i in range(n):
            cell = old[31*i:31*i+31]
            new = reaction(cell)
            result[31*i:31*i+31] = new
            if i == n-1:
                before, after = (new, cell) if inverse else (cell, new)
                event = before[:12] == R and after[:12] == AM
                proposed_p = (pointer + (-1 if inverse else 1)*event) % 5
    elif kind in ('A', 'B'):
        for i in range(n-1):
            if not cuts & (1 << i):
                r, q = 31*(i + (kind == 'B'))+30, 31*n+i
                result[r], result[q] = old[q], old[r]
    else:
        ct = tuple(zip(*C))
        for i in range(n):
            base = 31*i+24
            e, m = old[base:base+4], old[base+4:base+6]
            if inverse:
                m = tuple(a+b for a, b in zip(m, mv(ct, e)))
                e = tuple(a-b for a, b in zip(e, mv(C, m)))
            else:
                e = tuple(a+b for a, b in zip(e, mv(C, m)))
                m = tuple(a-b for a, b in zip(m, mv(ct, e)))
            result[base:base+6] = e+m
    validate(result, proposed_p, n)
    return tuple(result), proposed_p


def read_pointer(pointer):
    if type(pointer) is not int or not 0 <= pointer < 5:
        raise ValueError('invalid physical p')
    return pointer != 0


@dataclass(frozen=True)
class Confirmation:
    """Inputs from independent, qualified physical interfaces; not promises.

    No default is healthy. Until those interfaces are qualified this record
    can only be a SOFTWARE fixture. No lab-ready driver is provided here.
    """
    measured: bool
    adc_ok: bool
    samples_complete: bool
    dock_identity_ok: bool
    reserve_ok: bool
    energy_bounds_ok: bool
    p_valid: bool
    pointer: int
    cut_a: int
    cut_b: int
    disconnected: bool
    elapsed_us: int
    operation_done: bool = False
    voltage_ok: bool = False


class Controller:
    def __init__(self, registers, pointer, *, n=3, inverse=False, cuts=0):
        validate(registers, pointer, n)
        self.registers = tuple(registers)
        self.n, self.inverse, self.cuts = n, inverse, cuts
        self.phase, self.slot = 'READY', 0
        self.pending = None

    def fail(self, reason):
        self.phase = 'ERROR'
        self.pending = None
        # Registers are stale after physical failure; they are NOT rollback.
        raise RuntimeError(reason)

    def plan(self, physical_p):
        if self.phase != 'READY':
            self.fail('not READY')
        kind = ('FBAG' if self.inverse else 'GABF')[self.slot]
        try:
            candidate = layer(self.registers, physical_p, kind, inverse=self.inverse,
                              cuts=self.cuts, n=self.n)
        except (ValueError, TypeError):
            self.fail('invalid current state, pointer or configuration')
        self.pending = (kind, candidate, physical_p)
        self.last_elapsed = -1
        self.phase = 'BREAK'
        return kind, candidate

    def confirm(self, observation):
        if self.phase not in ('BREAK', 'EXECUTING', 'SETTLE') or self.pending is None:
            self.fail('no pending physical operation')
        if type(observation) is not Confirmation:
            self.fail('malformed acquisition confirmation')
        flags = (observation.measured, observation.adc_ok, observation.samples_complete,
                 observation.dock_identity_ok, observation.reserve_ok,
                 observation.energy_bounds_ok, observation.p_valid, observation.voltage_ok)
        if not all(x is True for x in flags):
            self.fail('invalid measurement, identity or reserve')
        if type(observation.pointer) is not int or not 0 <= observation.pointer < 5:
            self.fail('invalid pointer word')
        if any(type(mask) is not int or not 0 <= mask < 1 << (self.n-1)
               for mask in (observation.cut_a, observation.cut_b)):
            self.fail('invalid physical cut word')
        if type(observation.operation_done) is not bool:
            self.fail('invalid completion word')
        if observation.cut_a != self.cuts or observation.cut_b != self.cuts:
            self.fail('physical cut mismatch')
        kind, (candidate, pointer), old_p = self.pending
        deadline = {'G': 1700000, 'A': 2200000, 'B': 2200000, 'F': 100000}[kind]
        slot_end = {'G': 2000000, 'A': 2500000, 'B': 2500000, 'F': 3000000}[kind]
        if type(observation.elapsed_us) is not int or not max(0, self.last_elapsed) <= observation.elapsed_us <= slot_end:
            self.fail('invalid or nonmonotone slot timestamp')
        self.last_elapsed = observation.elapsed_us
        if self.phase in ('BREAK', 'EXECUTING') and observation.elapsed_us > deadline:
            self.fail('operation deadline')
        if self.phase == 'BREAK':
            if observation.disconnected is not True or observation.pointer != old_p or observation.operation_done:
                self.fail('break-before-make')
            self.phase = 'EXECUTING'
            return False
        if self.phase == 'EXECUTING':
            if observation.operation_done:
                self.phase = 'SETTLE'
            return False
        # Complete calibrated readings over the fixed final 100 ms are required;
        # samples_complete is supplied by acquisition, not a model trajectory.
        if observation.elapsed_us != slot_end or observation.disconnected is not True:
            self.fail('fixed settled window incomplete')
        if observation.pointer != pointer:
            self.fail('physical pointer did not complete')
        self.registers = candidate
        self.pending = None
        self.slot = (self.slot+1) % 4
        self.phase = 'READY'
        return True
