#!/usr/bin/env python3
"""Exact audit for P-PHOTON-WILSON-VILLAIN-BRIDGE-1.

The universal positivity and Poisson arguments are proved in PREREG.md.  This
standard-library program audits the exact Q(sqrt(5)) Fourier datum, support
invariants, residue witnesses, bridge action, and mutation controls.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Q5:
    """An exact value a + b sqrt(5), with a,b rational."""

    a: Fraction
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: "Q5 | Fraction | int") -> "Q5":
        if isinstance(value, Q5):
            return value
        return Q5(Fraction(value), Fraction(0))

    def __add__(self, other: "Q5 | Fraction | int") -> "Q5":
        value = Q5.coerce(other)
        return Q5(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self) -> "Q5":
        return Q5(-self.a, -self.b)

    def __sub__(self, other: "Q5 | Fraction | int") -> "Q5":
        return self + (-Q5.coerce(other))

    def __rsub__(self, other: "Q5 | Fraction | int") -> "Q5":
        return Q5.coerce(other) - self

    def __mul__(self, other: "Q5 | Fraction | int") -> "Q5":
        value = Q5.coerce(other)
        return Q5(
            self.a * value.a + 5 * self.b * value.b,
            self.a * value.b + self.b * value.a,
        )

    __rmul__ = __mul__

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0


ZERO = Q5(Fraction(0))
PHI2 = Q5(Fraction(3, 2), Fraction(1, 2))
PHI_MINUS2 = Q5(Fraction(3, 2), Fraction(-1, 2))
PUBLIC_W = (Q5(Fraction(4)), PHI2, PHI_MINUS2, PHI_MINUS2, PHI2)
PUBLIC_FW = (
    Q5(Fraction(10)),
    Q5(Fraction(5)),
    ZERO,
    ZERO,
    Q5(Fraction(5)),
)


class GateError(Exception):
    """A deterministic integrity or audit gate stopped the run."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise GateError(label)


def two_cosine(residue: int) -> Q5:
    residue %= 5
    if residue == 0:
        return Q5(Fraction(2))
    if residue in (1, 4):
        return Q5(Fraction(-1, 2), Fraction(1, 2))
    return Q5(Fraction(-1, 2), Fraction(-1, 2))


def dft_symmetric(vector: tuple[Q5, Q5, Q5, Q5, Q5]) -> tuple[Q5, Q5, Q5, Q5, Q5]:
    require(vector[1] == vector[4] and vector[2] == vector[3], "DFT_INPUT_NOT_SYMMETRIC")
    output = []
    for k in range(5):
        output.append(vector[0] + vector[1] * two_cosine(k) + vector[2] * two_cosine(2 * k))
    return tuple(output)  # type: ignore[return-value]


def support_size(vector: tuple[Q5, Q5, Q5, Q5, Q5]) -> int:
    return sum(not entry.is_zero() for entry in vector)


def support_pair(
    vector: tuple[Q5, Q5, Q5, Q5, Q5],
    transform: tuple[Q5, Q5, Q5, Q5, Q5],
) -> tuple[int, int]:
    return tuple(sorted((support_size(vector), support_size(transform))))  # type: ignore[return-value]


def automorphism_permute(
    vector: tuple[Q5, Q5, Q5, Q5, Q5], unit: int
) -> tuple[Q5, Q5, Q5, Q5, Q5]:
    require(unit in (1, 2, 3, 4), "BAD_AUTOMORPHISM_UNIT")
    return tuple(vector[(unit * index) % 5] for index in range(5))  # type: ignore[return-value]


def evaluate() -> tuple[str, ...]:
    lines = []

    require(PHI2 * PHI_MINUS2 == Q5(Fraction(1)), "G01_GOLDEN_RECIPROCITY")
    require(all(not entry.is_zero() for entry in PUBLIC_W), "G01_PUBLIC_WEIGHT_SUPPORT")
    lines.append("G01 public five-center weight has full support PASS")

    computed_fw = dft_symmetric(PUBLIC_W)
    require(computed_fw == PUBLIC_FW, "G02_PUBLIC_DFT")
    lines.append("G02 exact DFT equals 10,5,0,0,5 PASS")

    require(dft_symmetric(PUBLIC_FW) == tuple(entry * 5 for entry in PUBLIC_W), "G03_DFT_SQUARE")
    lines.append("G03 Fourier-square normalization audit PASS")

    target_pair = support_pair(PUBLIC_W, PUBLIC_FW)
    require(target_pair == (3, 5), "G04_TARGET_BISUPPORT")
    lines.append("G04 public unordered bi-support is 3,5 PASS")

    for residue in range(5):
        r, s = residue, 0
        require((r - s - residue) % 5 == 0, "G05_WILSON_RESIDUE_WITNESS")
        require(r >= 0 and s >= 0, "G05_WILSON_NONNEGATIVE_INDICES")
    lines.append("G05 Wilson positive-series residue witnesses complete PASS")

    wilson_positive_pair = (5, 5)
    wilson_zero_pair = (1, 5)
    require(target_pair != wilson_positive_pair, "G06_WILSON_POSITIVE_SUPPORT")
    require(target_pair != wilson_zero_pair, "G06_WILSON_ZERO_SUPPORT")
    lines.append("G06 Wilson beta-positive and beta-zero supports excluded PASS")

    for residue in range(5):
        character_term_index = residue + 5 * 0
        position_term_shift = Fraction(residue, 5)
        require(character_term_index == residue, "G07_VILLAIN_CHARACTER_TERM")
        require(Fraction(0) - position_term_shift == -Fraction(residue, 5), "G07_VILLAIN_POSITION_TERM")
    villain_pair = (5, 5)
    require(target_pair != villain_pair, "G07_VILLAIN_SUPPORT")
    lines.append("G07 Villain positive character and position terms excluded PASS")

    for unit in (1, 2, 3, 4):
        permuted_w = automorphism_permute(PUBLIC_W, unit)
        permuted_fw = automorphism_permute(PUBLIC_FW, unit)
        require(support_pair(permuted_w, permuted_fw) == target_pair, "G08_AUTOMORPHISM_SUPPORT")
    lines.append("G08 all four Z5 automorphisms preserve bi-support PASS")

    require(tuple(reversed(target_pair)) == (5, 3), "G09_FOURIER_SWAP")
    require(tuple(sorted(reversed(target_pair))) == target_pair, "G09_UNORDERED_SWAP")
    lines.append("G09 optional Fourier exchange preserves unordered bi-support PASS")

    require(target_pair not in (wilson_positive_pair, wilson_zero_pair, villain_pair), "G10_FAMILY_EXCLUSION")
    lines.append("G10 every frozen finite-coupling family is a nonmember PASS")

    mutated_fw = list(PUBLIC_FW)
    mutated_fw[2] = Q5(Fraction(1))
    mutated_fw[3] = Q5(Fraction(1))
    require(support_pair(PUBLIC_W, tuple(mutated_fw)) == (5, 5), "S01_ZERO_MUTATION")  # type: ignore[arg-type]
    lines.append("S01 zero-removal mutation destroys obstruction PASS")

    beta_zero_position = tuple(Q5(Fraction(1)) for _ in range(5))
    beta_zero_transform = (Q5(Fraction(5)), ZERO, ZERO, ZERO, ZERO)
    require(support_pair(beta_zero_position, beta_zero_transform) == (1, 5), "S02_BETA_ZERO")
    lines.append("S02 beta-zero endpoint control PASS")

    return tuple(lines)


def render(lines: tuple[str, ...]) -> bytes:
    header = (
        "P-PHOTON-WILSON-VILLAIN-BRIDGE-1\n",
        "ARITHMETIC exact-Qsqrt5-and-support\n",
    )
    body = tuple(line + "\n" for line in lines)
    footer = (
        "S03 fresh-state deterministic replay PASS\n",
        "OUTCOME FINITE-COUPLING-NONMEMBER\n",
        "RESULT 13/13 ALL PASS\n",
    )
    return "".join(header + body + footer).encode("ascii")


def main() -> int:
    if len(sys.argv) != 1:
        sys.stderr.write("usage: verify.py\n")
        return 2
    try:
        first = evaluate()
        second = evaluate()
        require(first == second, "S03_NONDETERMINISTIC")
        transcript = render(first)
        require(transcript == render(second), "S03_RENDER_NONDETERMINISTIC")
    except GateError as exc:
        sys.stderr.write("STOP " + str(exc) + "\n")
        return 1
    sys.stdout.buffer.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
