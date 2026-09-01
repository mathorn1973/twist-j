#!/usr/bin/env python3
"""Independent reference for the exact t=1 Z5 heat-bath transition."""

from __future__ import annotations

from dataclasses import dataclass

MASK32 = (1 << 32) - 1
MASK64 = (1 << 64) - 1
M0 = 0xD2511F53
M1 = 0xCD9E8D57
W0 = 0x9E3779B9
W1 = 0xBB67AE85
D = 4
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}


@dataclass(frozen=True)
class PhiInt:
    a: int
    b: int

    def __add__(self, other: "PhiInt") -> "PhiInt":
        return PhiInt(self.a + other.a, self.b + other.b)

    def __sub__(self, other: "PhiInt") -> "PhiInt":
        return PhiInt(self.a - other.a, self.b - other.b)

    def __mul__(self, other: object) -> "PhiInt":
        if isinstance(other, int):
            return PhiInt(self.a * other, self.b * other)
        if not isinstance(other, PhiInt):
            return NotImplemented
        return PhiInt(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )


def sign_phi(value: PhiInt) -> int:
    p = 2 * value.a + value.b
    q = value.b
    if p == 0 and q == 0:
        return 0
    if p >= 0 and q >= 0:
        return 1
    if p <= 0 and q <= 0:
        return -1
    if p >= 0:
        return 1 if p * p > 5 * q * q else -1
    return 1 if 5 * q * q > p * p else -1


def philox4x32_10(counter: tuple[int, int, int, int], key: tuple[int, int]) -> tuple[int, int, int, int]:
    c = list(counter)
    k0, k1 = key
    for round_index in range(10):
        product0 = M0 * c[0]
        product1 = M1 * c[2]
        low0, high0 = product0 & MASK32, (product0 >> 32) & MASK32
        low1, high1 = product1 & MASK32, (product1 >> 32) & MASK32
        c = [
            (high1 ^ c[1] ^ k0) & MASK32,
            low1,
            (high0 ^ c[3] ^ k1) & MASK32,
            low0,
        ]
        if round_index != 9:
            k0 = (k0 + W0) & MASK32
            k1 = (k1 + W1) & MASK32
    return tuple(c)


def random_u64(seed: int, stream: int, counter: int, lane: int = 0) -> int:
    output = philox4x32_10(
        (counter & MASK32, (counter >> 32) & MASK32, stream & MASK32, lane & MASK32),
        (seed & MASK32, (seed >> 32) & MASK32),
    )
    return ((output[0] << 32) | output[1]) & MASK64


def bounded5(seed: int, stream: int, counter: int) -> int:
    limit = (MASK64 // 5) * 5
    lane = 0
    while True:
        value = random_u64(seed, stream, counter, lane)
        if value < limit:
            return value % 5
        lane += 1


class Lattice:
    def __init__(self, linear_size: int, seed: int) -> None:
        self.L = linear_size
        self.V = linear_size**D
        self.seed = seed
        self.coords = [self.decode(site) for site in range(self.V)]
        self.plus = [[0] * D for _ in range(self.V)]
        self.minus = [[0] * D for _ in range(self.V)]
        for site, coordinate in enumerate(self.coords):
            for mu in range(D):
                plus_coordinate = list(coordinate)
                minus_coordinate = list(coordinate)
                plus_coordinate[mu] = (plus_coordinate[mu] + 1) % self.L
                minus_coordinate[mu] = (minus_coordinate[mu] - 1) % self.L
                self.plus[site][mu] = self.encode(tuple(plus_coordinate))
                self.minus[site][mu] = self.encode(tuple(minus_coordinate))
        self.links = [bounded5(seed, 0, index) for index in range(self.V * D)]
        self.flux = [0] * (self.V * len(PAIRS))
        self.weights = (
            PhiInt(4, 0),
            PhiInt(1, 1),
            PhiInt(2, -1),
            PhiInt(2, -1),
            PhiInt(1, 1),
        )
        self.recompute_flux()

    def decode(self, site: int) -> tuple[int, int, int, int]:
        coordinate = [0] * D
        for mu in range(D - 1, -1, -1):
            coordinate[mu] = site % self.L
            site //= self.L
        return tuple(coordinate)

    def encode(self, coordinate: tuple[int, int, int, int]) -> int:
        site = 0
        for value in coordinate:
            site = site * self.L + value
        return site

    def recompute_flux(self) -> None:
        for site in range(self.V):
            for pair_index, (mu, nu) in enumerate(PAIRS):
                self.flux[site * 6 + pair_index] = (
                    self.links[site * D + mu]
                    + self.links[self.plus[site][mu] * D + nu]
                    - self.links[self.plus[site][nu] * D + mu]
                    - self.links[site * D + nu]
                ) % 5

    def gauge_transform_for_test(self) -> None:
        gauge = [
            sum((mu + 1) * coordinate[mu] for mu in range(D)) % 5
            for coordinate in self.coords
        ]
        for site in range(self.V):
            for mu in range(D):
                index = site * D + mu
                self.links[index] = (
                    self.links[index] + gauge[self.plus[site][mu]] - gauge[site]
                ) % 5
        self.recompute_flux()

    def incident(self, site: int, mu: int) -> list[tuple[int, int, int]]:
        result: list[tuple[int, int, int]] = []
        for nu in range(D):
            if nu == mu:
                continue
            pair = (mu, nu) if mu < nu else (nu, mu)
            pair_index = PAIR_INDEX[pair]
            sign_at_site = 1 if mu < nu else -1
            result.append((site, pair_index, sign_at_site))
            result.append((self.minus[site][nu], pair_index, -sign_at_site))
        return result

    def update_link(self, site: int, mu: int, sweep_index: int, ordinal: int) -> None:
        link_index = site * D + mu
        old_value = self.links[link_index]
        affected = self.incident(site, mu)
        local_weights: list[PhiInt] = []
        total = PhiInt(0, 0)
        for candidate in range(5):
            delta = candidate - old_value
            value = PhiInt(1, 0)
            for base, pair_index, sign in affected:
                flux = (self.flux[base * 6 + pair_index] + sign * delta) % 5
                value = value * self.weights[flux]
            assert sign_phi(value) > 0
            local_weights.append(value)
            total = total + value

        draw = random_u64(
            self.seed,
            1,
            sweep_index * self.V * D + ordinal,
        )
        cumulative = PhiInt(0, 0)
        selected = 4
        for candidate, weight in enumerate(local_weights):
            cumulative = cumulative + weight
            difference = cumulative * (1 << 64) - total * draw
            if sign_phi(difference) > 0:
                selected = candidate
                break

        delta = selected - old_value
        if delta == 0:
            return
        self.links[link_index] = selected
        for base, pair_index, sign in affected:
            index = base * 6 + pair_index
            self.flux[index] = (self.flux[index] + sign * delta) % 5

    def sweep(self, sweep_index: int) -> None:
        for ordinal in range(self.V * D):
            self.update_link(ordinal // D, ordinal % D, sweep_index, ordinal)

    def state_hash(self) -> int:
        value = 1469598103934665603
        for byte in self.links + self.flux:
            value ^= byte
            value = (value * 1099511628211) & MASK64
        return value


def main() -> None:
    assert philox4x32_10((0, 0, 0, 0), (0, 0)) == (
        0x6627E8D5,
        0xE169C58D,
        0xBC57AC4C,
        0x9B00DBD8,
    )
    weights = (
        PhiInt(4, 0),
        PhiInt(1, 1),
        PhiInt(2, -1),
        PhiInt(2, -1),
        PhiInt(1, 1),
    )
    assert weights[1] * weights[2] == PhiInt(1, 0)
    assert weights[1] + weights[2] == PhiInt(3, 0)

    lattice = Lattice(3, 0x123456789ABCDEF0)
    flux_before = list(lattice.flux)
    lattice.gauge_transform_for_test()
    assert lattice.flux == flux_before
    for sweep_index in range(3):
        lattice.sweep(sweep_index)
    assert lattice.state_hash() == 0xEAA7BCBE93566B43

    print("REFERENCE PHILOX PASS")
    print("REFERENCE EXACT_PHI_HEATBATH PASS")
    print("REFERENCE GAUGE_INVARIANCE PASS")
    print("REFERENCE STATE_HASH eaa7bcbe93566b43")
    print("REFERENCE RESULT PASS")


if __name__ == "__main__":
    main()
