#!/usr/bin/env python3
"""TWIST-J: explicit source / carrier / pointer / archive model.

Python 3.10+, standard library only. Integer arithmetic in Z[zeta_5].
This is a chosen mathematical apparatus, NOT a realization of native U.
The finite readout measures O/5O (a ring, not the field F_625).
No random sampler or Born rule is hidden in this program.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Iterable, Sequence

Address = tuple[int, int, int, int]
Symbol = tuple[int, int]
ZERO: Address = (0, 0, 0, 0)
ONE: Address = (1, 0, 0, 0)
ZETA: Address = (0, 1, 0, 0)
J: Address = (1, 0, 1, 0)
J_INV: Address = (0, -1, -1, 0)
MODULUS = 5
SOURCE_ALPHABET: tuple[Symbol, ...] = tuple(
    (u, v) for u in range(-2, 3) for v in range(-2, 3)
)


def address(values: Sequence[int]) -> Address:
    if len(values) != 4 or any(type(x) is not int for x in values):
        raise ValueError('An address must have exactly four integer coordinates.')
    return tuple(values)  # type: ignore[return-value]


def symbol(values: Sequence[int]) -> Symbol:
    if len(values) != 2 or any(type(x) is not int or not -2 <= x <= 2 for x in values):
        raise ValueError('A source symbol must have two integer coordinates in [-2, 2].')
    return (values[0], values[1])


def add(a: Address, b: Address) -> Address:
    return tuple(x+y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Address, b: Address) -> Address:
    return tuple(x-y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(k: int, a: Address) -> Address:
    return tuple(k*x for x in a)  # type: ignore[return-value]


def mul(a: Address, b: Address) -> Address:
    c = [0]*7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i+k] += x*y
    for degree in range(6, 3, -1):
        for k in range(4):
            c[degree-4+k] -= c[degree]
        c[degree] = 0
    return tuple(c[:4])  # type: ignore[return-value]


def power(a: Address, n: int) -> Address:
    if type(n) is not int or n < 0:
        raise ValueError('The exponent must be a nonnegative integer.')
    result = ONE
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def multiply_j(a: Address) -> Address:
    x, y, z, t = a
    return (x-z+t, y-z, x, y-z+t)


def multiply_j_inverse(a: Address) -> Address:
    x, y, z, t = a
    return (z, -x+z+t, -x-y+z+t, -y+t)


def residue(a: Address, q: int = MODULUS) -> Address:
    if type(q) is not int or q < 2:
        raise ValueError('The modulus must be an integer >= 2.')
    return tuple(x % q for x in a)  # type: ignore[return-value]


def centered(x: int) -> int:
    if type(x) is not int:
        raise ValueError('The residue must be an integer.')
    return (x+2) % 5 - 2


def input_address(s: Sequence[int]) -> Address:
    u, v = symbol(s)
    return (u, v, 0, 0)


def step(a: Address, s: Sequence[int]) -> Address:
    """Exact infinite-lattice carrier step; the source symbol is NOT erased."""
    return add(multiply_j(a), input_address(s))


def step_inverse(b: Address, s: Sequence[int]) -> Address:
    return multiply_j_inverse(sub(b, input_address(s)))


def block_encode(digits: Address) -> Address:
    """L(u0,v0,u1,v1) = J*b0 + b1; unimodular over Z."""
    u0, v0, u1, v1 = digits
    return (u0+u1, v0+v1, u0, v0)


def block_decode(delta: Address) -> Address:
    x, y, z, t = delta
    return (z, t, x-z, y-t)


def read_residue_to_pointer(a: Address, pointer: Address = ZERO) -> Address:
    """Induced basis permutation of the four coherent phase readers.

    The verifier independently reconstructs the phase-reader kernel using exact
    cyclotomic sums. This function alone is not the proof of that construction.
    """
    return residue(add(pointer, residue(a)))


def record_gates(
    carrier_after: Address, reference: Address, pointer: Address, archive_cell: Address
) -> tuple[Address, Address, Address]:
    """Six invertible finite-register gates after the two carrier steps.

    Works on arbitrary register values. Correct block extraction requires a
    synchronized reference, an initially zero pointer, and a fresh zero archive.
    Output is (new_reference, new_pointer, new_archive_cell).
    """
    m, p, e = residue(reference), residue(pointer), residue(archive_cell)
    p = read_residue_to_pointer(carrier_after, p)
    p = residue(sub(p, multiply_j(multiply_j(m))))
    p = residue(block_decode(p))
    e = residue(add(e, p))
    p = residue(sub(p, e))
    m = residue(add(multiply_j(multiply_j(m)), block_encode(e)))
    return m, p, e


def record_gates_inverse(
    carrier_after: Address, reference: Address, pointer: Address, archive_cell: Address
) -> tuple[Address, Address, Address]:
    m, p, e = residue(reference), residue(pointer), residue(archive_cell)
    m = residue(multiply_j_inverse(multiply_j_inverse(sub(m, block_encode(e)))))
    p = residue(add(p, e))
    e = residue(sub(e, p))
    p = residue(block_encode(p))
    p = residue(add(p, multiply_j(multiply_j(m))))
    p = residue(sub(p, residue(carrier_after)))
    return m, p, e


@dataclass
class Apparatus:
    """Basis-state simulation. A coherent model uses linear extension of its gates.

    One archive cell has four F_5 coordinates and stores two source symbols.
    The finite pointer is reset; the archive grows. No physical device is claimed.
    """
    initial: Address = ZERO
    carrier: Address = field(init=False)
    reference: Address = field(init=False)
    pointer: Address = field(default=ZERO, init=False)
    archive: list[Address] = field(default_factory=list, init=False)
    steps: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        self.carrier = address(self.initial)
        self.reference = residue(self.carrier)

    def run_block(self, first: Sequence[int], second: Sequence[int]) -> Address:
        s0, s1 = symbol(first), symbol(second)
        if self.pointer != ZERO or self.reference != residue(self.carrier):
            raise RuntimeError('The pointer or reference is not ready.')
        before = self.carrier
        after = step(step(before, s0), s1)
        m, p, recorded = record_gates(after, self.reference, ZERO, ZERO)
        if p != ZERO or m != residue(after):
            raise AssertionError('The apparatus failed to reset or synchronize.')
        expected = residue(s0+s1)
        if recorded != expected:
            raise AssertionError('The recorded source differs from the input.')
        self.carrier, self.reference, self.pointer = after, m, p
        self.archive.append(recorded)
        self.steps += 2
        return recorded

    def recovered_symbols(self) -> list[Symbol]:
        result: list[Symbol] = []
        for u0, v0, u1, v1 in self.archive:
            result.extend(((centered(u0), centered(v0)), (centered(u1), centered(v1))))
        return result

    def reconstruct_carrier(self) -> Address:
        a = self.initial
        for s in self.recovered_symbols():
            a = step(a, s)
        return a


def chosen_checkpoint_port(psi: Sequence[int]) -> Symbol:
    """Explicit NEW choice: read the first two coordinates of an F_5^6 checkpoint.

    This function does not claim those coordinates are selected by native physics.
    """
    if len(psi) != 6 or any(type(x) is not int or not 0 <= x < 5 for x in psi):
        raise ValueError('A checkpoint must have six canonical F_5 residues.')
    return (centered(psi[0]), centered(psi[1]))


def extend_native_step(
    n: int, psi: tuple[int, ...], carrier: Address,
    native_step: Callable[[int, tuple[int, ...]], tuple[int, tuple[int, ...]]]
) -> tuple[int, tuple[int, ...], Address]:
    """Read-only extension of a supplied, separately validated native kernel.

    No native kernel is included or inferred here. Projection of the returned
    tuple onto (n,psi) equals native_step(n,psi) by construction. This does NOT
    imply that the added carrier or reader already exists inside native U.
    No global unitarity is asserted for an arbitrary noninjective native_step.
    """
    if type(n) is not int or n < 0:
        raise ValueError('The step counter must be a nonnegative integer.')
    s = chosen_checkpoint_port(psi)
    n1, psi1 = native_step(n, psi)
    if n1 != n+1:
        raise ValueError('The supplied kernel did not advance the counter by one.')
    chosen_checkpoint_port(psi1)  # Validate the returned checkpoint only.
    return n1, psi1, step(carrier, s)
