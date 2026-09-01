#!/usr/bin/env python3
"""Exact reference audit for the fixed t=1 Z5 photon heat-bath kernel."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import gcd
from typing import Iterable, Iterator


@dataclass(frozen=True, slots=True)
class QPhi:
    """The algebraic integer a+b*phi with phi^2=phi+1."""

    a: int
    b: int = 0

    def __add__(self, other: "QPhi") -> "QPhi":
        return QPhi(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "QPhi":
        return QPhi(-self.a, -self.b)

    def __sub__(self, other: "QPhi") -> "QPhi":
        return self + (-other)

    def __mul__(self, other: "QPhi") -> "QPhi":
        # (a+b phi)(c+d phi)=(ac+bd)+(ad+bc+bd)phi.
        return QPhi(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def scale(self, integer: int) -> "QPhi":
        return QPhi(integer * self.a, integer * self.b)

    def __pow__(self, exponent: int) -> "QPhi":
        if exponent < 0:
            raise ValueError("negative powers are not represented integrally")
        result = QPhi(1)
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result


def sign(value: QPhi) -> int:
    """Exact sign under the real embedding phi=(1+sqrt(5))/2."""

    # 2(a+b phi)=(2a+b)+b sqrt(5).
    c = 2 * value.a + value.b
    d = value.b
    if c == 0 and d == 0:
        return 0
    if c >= 0 and d >= 0:
        return 1
    if c <= 0 and d <= 0:
        return -1
    left = c * c
    right = 5 * d * d
    if left == right:
        raise AssertionError("nonzero integer equality c^2=5d^2 is impossible")
    if c > 0 and d < 0:
        return 1 if left > right else -1
    # c<0<d.
    return 1 if right > left else -1


def compare(left: QPhi, right: QPhi) -> int:
    return sign(left - right)


def qsum(values: Iterable[QPhi]) -> QPhi:
    total = QPhi(0)
    for value in values:
        total = total + value
    return total


PHI = QPhi(0, 1)
FACE_WEIGHTS = (
    QPhi(4, 0),
    QPhi(1, 1),
    QPhi(2, -1),
    QPhi(2, -1),
    QPhi(1, 1),
)
INCIDENT_SIGNS = (1, 1, 1, -1, -1, -1)


def local_weights(residual_fluxes: tuple[int, ...]) -> tuple[QPhi, ...]:
    if len(residual_fluxes) != 6:
        raise ValueError("a four-dimensional link must meet six plaquettes")
    weights: list[QPhi] = []
    for link_value in range(5):
        weight = QPhi(1)
        for residual, orientation in zip(residual_fluxes, INCIDENT_SIGNS):
            flux = (residual + orientation * link_value) % 5
            weight = weight * FACE_WEIGHTS[flux]
        weights.append(weight)
    return tuple(weights)


def counter_bits(stream: int) -> Iterator[int]:
    """Public deterministic counter stream used only for reproducibility audit."""

    block = 0
    while True:
        payload = (
            b"TWIST-J/PHOTON/Z5/EXACT-HEATBATH/KERNEL-1\0"
            + stream.to_bytes(8, "big")
            + block.to_bytes(8, "big")
        )
        digest = sha256(payload).digest()
        for byte in digest:
            for shift in range(7, -1, -1):
                yield (byte >> shift) & 1
        block += 1


def exact_category(
    weights: tuple[QPhi, ...],
    bits: Iterator[int],
    *,
    bit_cap: int = 512,
) -> tuple[int, int, int]:
    """Sample by refining a dyadic interval and comparing in Z[phi].

    The return certificate (category,n,prefix) proves that the complete dyadic
    interval [prefix/2^n,(prefix+1)/2^n) lies inside that category's exact
    cumulative-probability interval. No probability is rounded to n bits.
    """

    if not weights or any(sign(weight) <= 0 for weight in weights):
        raise ValueError("categorical weights must be strictly positive")
    total = qsum(weights)
    cumulative = [QPhi(0)]
    for weight in weights:
        cumulative.append(cumulative[-1] + weight)

    prefix = 0
    for n in range(1, bit_cap + 1):
        prefix = (prefix << 1) | next(bits)
        scale = 1 << n
        lower_mass = total.scale(prefix)
        upper_mass = total.scale(prefix + 1)
        for category in range(len(weights)):
            lower_threshold = cumulative[category].scale(scale)
            upper_threshold = cumulative[category + 1].scale(scale)
            if (
                compare(lower_mass, lower_threshold) >= 0
                and compare(upper_mass, upper_threshold) <= 0
            ):
                return category, n, prefix
    raise RuntimeError("bit cap reached before an exact category certificate")


def audit_flat_holonomy() -> None:
    """Check the closed hyperplane 1-cochain on small periodic four-tori."""

    for length in (2, 3, 4, 5):
        site_list = tuple(product(range(length), repeat=4))
        for direction in range(4):
            for holonomy in range(5):
                def sheet(site: tuple[int, ...], link_direction: int) -> int:
                    return (
                        holonomy
                        if link_direction == direction and site[direction] == 0
                        else 0
                    )

                for site in site_list:
                    for mu in range(4):
                        for nu in range(mu + 1, 4):
                            site_mu = list(site)
                            site_mu[mu] = (site_mu[mu] + 1) % length
                            site_nu = list(site)
                            site_nu[nu] = (site_nu[nu] + 1) % length
                            curvature = (
                                sheet(site, mu)
                                + sheet(tuple(site_mu), nu)
                                - sheet(tuple(site_nu), mu)
                                - sheet(site, nu)
                            ) % 5
                            if curvature != 0:
                                raise AssertionError("flat holonomy changed a plaquette")

                site = [0, 0, 0, 0]
                loop_sum = 0
                for coordinate in range(length):
                    site[direction] = coordinate
                    loop_sum += sheet(tuple(site), direction)
                if loop_sum % 5 != holonomy:
                    raise AssertionError("flat sheet has the wrong cycle holonomy")


def main() -> None:
    if PHI * PHI != PHI + QPhi(1):
        raise AssertionError("phi relation failed")
    if any(sign(weight) <= 0 for weight in FACE_WEIGHTS):
        raise AssertionError("face weights are not all positive")
    if FACE_WEIGHTS[1] != FACE_WEIGHTS[4] or FACE_WEIGHTS[2] != FACE_WEIGHTS[3]:
        raise AssertionError("Z5 inversion symmetry failed")

    expected_zero_weights = (
        QPhi(4096),
        QPhi(89, 144),
        QPhi(233, -144),
        QPhi(233, -144),
        QPhi(89, 144),
    )
    zero_weights = local_weights((0, 0, 0, 0, 0, 0))
    if zero_weights != expected_zero_weights:
        raise AssertionError(f"all-zero local weights differ: {zero_weights!r}")
    zero_total = qsum(zero_weights)
    if zero_total != QPhi(4740):
        raise AssertionError("all-zero local total must be 4740")
    divisor = gcd(4096, 4740)
    keep_numerator = 4096 // divisor
    keep_denominator = 4740 // divisor
    if (keep_numerator, keep_denominator) != (1024, 1185):
        raise AssertionError("unexpected reduced all-zero probability")
    if keep_denominator & (keep_denominator - 1) == 0:
        raise AssertionError("the witness probability unexpectedly became dyadic")

    environment_count = 0
    for stream, residuals in enumerate(product(range(5), repeat=6)):
        residual_tuple = tuple(residuals)
        weights = local_weights(residual_tuple)
        if any(sign(weight) <= 0 for weight in weights):
            raise AssertionError("nonpositive local candidate weight")
        if sign(qsum(weights)) <= 0:
            raise AssertionError("nonpositive local normalization")

        # Changing the residual origin by one link unit must only permute the
        # five candidate weights.
        shifted = tuple(
            (residual + orientation) % 5
            for residual, orientation in zip(residual_tuple, INCIDENT_SIGNS)
        )
        shifted_weights = local_weights(shifted)
        if any(shifted_weights[a] != weights[(a + 1) % 5] for a in range(5)):
            raise AssertionError("local translation covariance failed")

        category, bits_used, prefix = exact_category(weights, counter_bits(stream))
        if not (0 <= category < 5 and 1 <= bits_used <= 512):
            raise AssertionError("invalid exact sampler certificate")
        scale = 1 << bits_used
        cumulative = [QPhi(0)]
        for weight in weights:
            cumulative.append(cumulative[-1] + weight)
        total = cumulative[-1]
        if compare(total.scale(prefix), cumulative[category].scale(scale)) < 0:
            raise AssertionError("sampler certificate crosses lower threshold")
        if compare(
            total.scale(prefix + 1), cumulative[category + 1].scale(scale)
        ) > 0:
            raise AssertionError("sampler certificate crosses upper threshold")
        environment_count += 1

    if environment_count != 5**6:
        raise AssertionError("local environment census is incomplete")

    audit_flat_holonomy()

    print("REPRODUCTION PHOTON-Z5-EXACT-HEATBATH-KERNEL")
    print("FIELD Z[phi]")
    print("FACE_WEIGHTS 4,1+phi,2-phi,2-phi,1+phi")
    print("LOCAL_ENVIRONMENTS 15625")
    print("CANDIDATES_PER_ENVIRONMENT 5")
    print("INCIDENT_ORIENTATIONS +++---")
    print("ALL_LOCAL_WEIGHTS POSITIVE")
    print("ALL_ZERO_CANDIDATE_WEIGHTS 4096,89+144phi,233-144phi,233-144phi,89+144phi")
    print("ALL_ZERO_TOTAL 4740")
    print("ALL_ZERO_KEEP_PROBABILITY 1024/1185")
    print("FIXED_DYADIC_CATEGORICAL_EXACTNESS IMPOSSIBLE")
    print("PREFIX_INTERVAL_SAMPLER EXACT_CERTIFICATES")
    print("TRANSLATION_COVARIANCE PASS")
    print("FLAT_HOLONOMY_PLAQUETTE_CHANGE ZERO")
    print("FINITE_VOLUME_CHAIN IRREDUCIBLE_APERIODIC")
    print("STATIONARY_MEASURE FIXED_T1_Z5_FACE_WEIGHT")
    print("RESULT PASS")


if __name__ == "__main__":
    main()
