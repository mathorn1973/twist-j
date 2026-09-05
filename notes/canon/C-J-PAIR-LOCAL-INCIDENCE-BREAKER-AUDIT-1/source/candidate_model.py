"""Unexecuted candidate specification of the A-channel one-cut census model.

This is a finite mathematical apparatus witness, not a physical simulator,
accepted verifier, preregistration, formal run, or evidence of Born sampling.
Resource limits bound this implementation only. The written proofs carry
the general statements. No work is performed when this module is imported.
The specified state domain consists of prepare_blank outputs and declared
transitions, not arbitrary directly forged Bank instances.
"""

from dataclasses import dataclass, replace
from fractions import Fraction


Vector = tuple[int, int, int, int, int]
Token = tuple[str, int, int, int]  # role, cell, sign, fresh ordinal
Address = tuple[Token, Token]


def a_step(vector: Vector) -> Vector:
    """A=1+g^2-g^3-g^4, with g e_k=e_(k+1)."""
    return tuple(
        vector[k] + vector[(k - 2) % 5]
        - vector[(k - 3) % 5] - vector[(k - 4) % 5]
        for k in range(5)
    )


def residual_fibre(vector: Vector, role: str) -> tuple[Token, ...]:
    """Fresh units at one cut; no historical survivor or inter-cut identity."""
    return tuple(
        (role, cell, 1 if coefficient > 0 else -1, ordinal)
        for cell, coefficient in enumerate(vector)
        for ordinal in range(1, abs(coefficient) + 1)
    )


@dataclass(frozen=True)
class Bank:
    cut_id: str
    preparation: Vector
    steps: int
    coefficients: Vector
    addresses: tuple[Address, ...]
    bits: tuple[bool, ...]


def prepare_blank(
    preparation: Vector,
    steps: int,
    cut_id: str,
    *,
    max_steps: int = 20,
    max_units: int = 128,
) -> Bank:
    """Prepare a bounded bank at a supported integral A read cut.

    The physical source-to-preparation map is an input obligation. This
    routine cannot certify physical provenance or meaning of the source.
    """
    if len(preparation) != 5 or any(type(x) is not int for x in preparation):
        raise ValueError("Preparation must contain exactly five integers")
    if sum(preparation) != 0 or not any(preparation):
        raise ValueError("Preparation must be nonzero and augmentation-zero")
    if any((x - preparation[0]) % 5 for x in preparation):
        raise ValueError("Preparation is outside the centered plenum lattice")
    if type(steps) is not int or not 0 <= steps <= max_steps:
        raise ValueError("Read cut exceeds the declared implementation bound")
    if not isinstance(cut_id, str) or not cut_id:
        raise ValueError("A nonempty cut identifier is required")
    if type(max_units) is not int or max_units < 1:
        raise ValueError("Unit capacity must be a positive integer")

    vector = tuple(preparation)
    for _ in range(steps):
        vector = a_step(vector)
    units = sum(abs(x) for x in vector)
    if units > max_units:
        raise ValueError("Insufficient bank capacity: no truncated census")

    system = residual_fibre(vector, "S")
    record = residual_fibre(vector, "R")
    addresses = tuple((x, y) for x in system for y in record)
    return Bank(
        cut_id, tuple(preparation), steps, vector,
        addresses, (False,) * len(addresses),
    )


def toggle_same_cell(bank: Bank) -> Bank:
    """One reversible activation, using only cell equality at each address.

    No coefficient magnitude, exponent, Gram matrix, normalized target,
    ordinal matching, or random input is read by the gate. Complete pair
    address availability is an explicit resource premise of preparation.
    A second activation erases a blank-start record bank.
    """
    if len(bank.addresses) != len(bank.bits):
        raise ValueError("Malformed bank")
    return replace(
        bank,
        bits=tuple(
            bit ^ (system[1] == record[1])
            for (system, record), bit in zip(bank.addresses, bank.bits)
        ),
    )


def active_records(bank: Bank) -> tuple[tuple[str, Token, Token], ...]:
    """Names of active sites in an immutable snapshot, one name per site."""
    if len(bank.addresses) != len(bank.bits):
        raise ValueError("Malformed bank")
    return tuple(
        (bank.cut_id, system, record)
        for (system, record), bit in zip(bank.addresses, bank.bits)
        if bit
    )


def census(bank: Bank) -> tuple[tuple[int, ...], tuple[Fraction, ...]]:
    """Complete population census, not a one-observer sampling law."""
    counts = [0] * 5
    for _, system, record in active_records(bank):
        if system[1] != record[1]:
            raise ValueError("Off-cell active record violates the candidate model")
        counts[system[1]] += 1
    total = sum(counts)
    if total == 0:
        raise ValueError("Empty record population has no normalized census")
    return tuple(counts), tuple(Fraction(count, total) for count in counts)


def retain(bank: Bank) -> Bank:
    """Specified storage identity; its physical implementation is not proved."""
    return bank
