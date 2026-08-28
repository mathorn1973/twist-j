#!/usr/bin/env python3
"""Exact audit for P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1.

The written proofs in PREREG.md carry the universal statements. This verifier
uses exact integer arithmetic only and audits frozen finite ranges plus the
checkpoint-obstruction witness inherited from CARRY-J-CHECKPOINT [T].
"""

from __future__ import annotations


OMEGA_1 = (1, 0, 0, 1, 0, 1)
OMEGA_2 = (0, 1, -1, 0, 1, 0)
QUADRATIC_RESIDUES_MOD_5 = {1, 4}


def pfaffian(w: tuple[int, int, int, int, int, int]) -> int:
    """Pfaffian in coordinate order (w01,w02,w03,w12,w13,w23)."""
    w01, w02, w03, w12, w13, w23 = w
    return w01 * w23 - w02 * w13 + w03 * w12


def add_scaled(
    a: int,
    u: tuple[int, int, int, int, int, int],
    b: int,
    v: tuple[int, int, int, int, int, int],
) -> tuple[int, int, int, int, int, int]:
    return tuple(a * x + b * y for x, y in zip(u, v, strict=True))  # type: ignore[return-value]


def fibonacci_pair(k: int) -> tuple[int, int]:
    """Return (F_k,F_(k+1)) for k >= 0."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    f_k, f_next = 0, 1
    for _ in range(k):
        f_k, f_next = f_next, f_k + f_next
    return f_k, f_next


def omega(k: int) -> tuple[int, int, int, int, int, int]:
    f_k, f_next = fibonacci_pair(k)
    return add_scaled(f_next, OMEGA_1, f_k, OMEGA_2)


def theta(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return n.bit_count() & 1


def ramified_phase(n: int) -> int:
    """Theta_n = 2^s_2(n) in F_5^*."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return pow(2, n.bit_count(), 5)


def chi5(x: int) -> int:
    """Quadratic character on F_5^*."""
    residue = x % 5
    if residue == 0:
        raise ValueError("chi5 is used only on F_5^*")
    return 1 if residue in QUADRATIC_RESIDUES_MOD_5 else -1


def orientation_character(k: int) -> int:
    value = pfaffian(omega(k))
    if value not in (-1, 1):
        raise AssertionError("frozen Pell form is not unimodular")
    return value


def gate_1_pencil_formula() -> None:
    for a in range(-32, 33):
        for b in range(-32, 33):
            w = add_scaled(a, OMEGA_1, b, OMEGA_2)
            assert pfaffian(w) == a * a - a * b - b * b
    print("PASS 1: frozen Pfaffian pencil formula")


def gate_2_fibonacci_orientation() -> None:
    for k in range(2049):
        assert orientation_character(k) == (1 if k % 2 == 0 else -1)
    print("PASS 2: Fibonacci Pell orientation sign")


def gate_3_ramified_character() -> None:
    for k in range(4097):
        expected = 1 if k % 2 == 0 else -1
        assert chi5(pow(2, k, 5)) == expected
    print("PASS 3: ramified quadratic character")


def gate_4_composed_character() -> None:
    for n in range(1 << 18):
        expected = 1 if theta(n) == 0 else -1
        assert orientation_character(n.bit_count()) == expected
        assert chi5(ramified_phase(n)) == expected
    print("PASS 4: Thue-Morse symplectic character composition")


def gate_5_checkpoint_obstruction_witness() -> None:
    # CARRY-J-CHECKPOINT [T] owns psi_4 = psi_6 for every seed.
    # This audit checks that the inherited two times carry opposite quotient
    # characters, which strengthens the full-phase no-go to this binary
    # orientation character.
    assert ramified_phase(4) == 2
    assert ramified_phase(6) == 4
    assert orientation_character((4).bit_count()) == -1
    assert orientation_character((6).bit_count()) == 1
    assert chi5(ramified_phase(4)) == -1
    assert chi5(ramified_phase(6)) == 1
    print("PASS 5: checkpoint obstruction carries opposite characters")


def gate_6_direct_reduction_guard() -> None:
    for k in range(2049):
        reduced = orientation_character(k) % 5
        assert reduced in QUADRATIC_RESIDUES_MOD_5
    print("PASS 6: direct Pfaffian reduction is QR-only")


def gate_7_negation_orientation_guard() -> None:
    for k in range(257):
        w = omega(k)
        minus_w = tuple(-x for x in w)
        assert pfaffian(minus_w) == pfaffian(w)
    print("PASS 7: omega and minus omega share 4D orientation")


def gate_8_first_twenty_balance() -> None:
    values = [1 if theta(n) == 0 else -1 for n in range(20)]
    assert values.count(1) == 10
    assert values.count(-1) == 10
    print("PASS 8: first twenty counter values split 10/10")


def main() -> int:
    gate_1_pencil_formula()
    gate_2_fibonacci_orientation()
    gate_3_ramified_character()
    gate_4_composed_character()
    gate_5_checkpoint_obstruction_witness()
    gate_6_direct_reduction_guard()
    gate_7_negation_orientation_guard()
    gate_8_first_twenty_balance()
    print("RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
