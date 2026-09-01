#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import hashlib

DIM = 4
PAIRS = tuple((a, b) for a in range(DIM) for b in range(a + 1, DIM))
TRIPLES = tuple(
    (a, b, c)
    for a in range(DIM)
    for b in range(a + 1, DIM)
    for c in range(b + 1, DIM)
)


def mod5(x: int) -> int:
    return x % 5


def principal_allowed(x: int) -> bool:
    return x % 5 in (0, 1, 4)


def support_size(state: list[int]) -> int:
    return sum(1 for value in state if value % 5)


@dataclass
class BitStream:
    seed: int
    domain: bytes = b"dual756"
    block_counter: int = 0
    buffer: int = 0
    bits_left: int = 0

    def _refill(self) -> None:
        payload = (
            self.domain
            + self.seed.to_bytes(16, "big")
            + self.block_counter.to_bytes(16, "big")
        )
        self.block_counter += 1
        self.buffer = int.from_bytes(hashlib.sha256(payload).digest(), "big")
        self.bits_left = 256

    def bit(self) -> int:
        if self.bits_left == 0:
            self._refill()
        self.bits_left -= 1
        return (self.buffer >> self.bits_left) & 1

    def bits(self, n: int) -> int:
        value = 0
        for _ in range(n):
            value = (value << 1) | self.bit()
        return value

    def bounded(self, n: int) -> int:
        if n <= 0:
            raise ValueError("n must be positive")
        width = (n - 1).bit_length()
        while True:
            value = self.bits(width)
            if value < n:
                return value

    def geometric_half(self) -> int:
        length = 0
        while self.bit() == 0:
            length += 1
        return length


class Torus4:
    def __init__(self, L: int):
        if L < 1:
            raise ValueError("L>=1")
        self.L = L
        self.volume = L**DIM
        self.pair_index = {pair: index for index, pair in enumerate(PAIRS)}
        self.triple_index = {
            triple: index for index, triple in enumerate(TRIPLES)
        }

    def site_index(self, x: tuple[int, int, int, int]) -> int:
        value = 0
        for coordinate in x:
            value = value * self.L + (coordinate % self.L)
        return value

    def site_coord(self, index: int) -> tuple[int, int, int, int]:
        result = [0] * DIM
        for mu in range(DIM - 1, -1, -1):
            result[mu] = index % self.L
            index //= self.L
        return tuple(result)

    def shift(
        self,
        x: tuple[int, int, int, int],
        mu: int,
        delta: int = 1,
    ) -> tuple[int, int, int, int]:
        result = list(x)
        result[mu] = (result[mu] + delta) % self.L
        return tuple(result)

    def link_index(self, x: tuple[int, int, int, int], mu: int) -> int:
        return self.site_index(x) * DIM + mu

    def plaq_index(
        self,
        x: tuple[int, int, int, int],
        a: int,
        b: int,
    ) -> int:
        if a > b:
            a, b = b, a
        return self.site_index(x) * len(PAIRS) + self.pair_index[(a, b)]

    @property
    def n_links(self) -> int:
        return self.volume * DIM

    @property
    def n_plaq(self) -> int:
        return self.volume * len(PAIRS)

    @property
    def n_cubes(self) -> int:
        return self.volume * len(TRIPLES)

    def plaquette_boundary(
        self,
        x: tuple[int, int, int, int],
        a: int,
        b: int,
    ) -> dict[int, int]:
        if a > b:
            a, b = b, a
        return {
            self.link_index(x, a): 1,
            self.link_index(self.shift(x, a), b): 1,
            self.link_index(self.shift(x, b), a): -1,
            self.link_index(x, b): -1,
        }

    def cube_boundary(
        self,
        x: tuple[int, int, int, int],
        a: int,
        b: int,
        c: int,
    ) -> dict[int, int]:
        axes = tuple(sorted((a, b, c)))
        result: dict[int, int] = {}
        for position, axis in enumerate(axes):
            face = tuple(value for value in axes if value != axis)
            sign = 1 if position % 2 == 0 else -1
            upper = self.shift(x, axis)
            for base, coefficient in ((upper, sign), (x, -sign)):
                plaquette = self.plaq_index(base, *face)
                result[plaquette] = result.get(plaquette, 0) + coefficient
        return {
            plaquette: mod5(value)
            for plaquette, value in result.items()
            if mod5(value)
        }

    def harmonic_plane(self, a: int, b: int) -> dict[int, int]:
        if a > b:
            a, b = b, a
        result: dict[int, int] = {}
        for ia in range(self.L):
            for ib in range(self.L):
                x = [0] * DIM
                x[a] = ia
                x[b] = ib
                result[self.plaq_index(tuple(x), a, b)] = 1
        return result

    def boundary1(self, state: list[int]) -> list[int]:
        if len(state) != self.n_plaq:
            raise ValueError("bad state length")
        result = [0] * self.n_links
        for site in range(self.volume):
            x = self.site_coord(site)
            for a, b in PAIRS:
                value = state[self.plaq_index(x, a, b)] % 5
                if not value:
                    continue
                for link, coefficient in self.plaquette_boundary(x, a, b).items():
                    result[link] = (result[link] + coefficient * value) % 5
        return result

    def valid_state(self, state: list[int]) -> bool:
        return (
            len(state) == self.n_plaq
            and all(principal_allowed(value) for value in state)
            and all(value == 0 for value in self.boundary1(state))
        )

    def generator(self, kind: int, index: int) -> dict[int, int]:
        if kind == 0:
            site = index // len(TRIPLES)
            triple = TRIPLES[index % len(TRIPLES)]
            return self.cube_boundary(self.site_coord(site), *triple)
        if kind == 1:
            return self.harmonic_plane(*PAIRS[index])
        raise ValueError("kind")


def add_increment(
    state: list[int],
    increment: dict[int, int],
    sign: int = 1,
) -> list[int]:
    result = state.copy()
    for plaquette, coefficient in increment.items():
        result[plaquette] = (result[plaquette] + sign * coefficient) % 5
    return result


def proposal_increment(
    lattice: Torus4,
    rng: BitStream,
) -> tuple[dict[int, int], int]:
    length = rng.geometric_half()
    increment: dict[int, int] = {}
    for _ in range(length):
        kind = rng.bit()
        index = rng.bounded(lattice.n_cubes if kind == 0 else len(PAIRS))
        sign = 1 if rng.bit() == 0 else -1
        for plaquette, coefficient in lattice.generator(kind, index).items():
            increment[plaquette] = (
                increment.get(plaquette, 0) + sign * coefficient
            ) % 5
            if increment[plaquette] == 0:
                del increment[plaquette]
    return increment, length


def metropolis_step(
    lattice: Torus4,
    state: list[int],
    rng: BitStream,
) -> tuple[list[int], dict[str, int]]:
    if not lattice.valid_state(state):
        raise ValueError("invalid input state")
    increment, length = proposal_increment(lattice, rng)
    candidate = add_increment(state, increment)
    diagnostics = {
        "word_length": length,
        "invalid_support": 0,
        "support_delta": 0,
        "accepted": 0,
    }
    if not all(principal_allowed(value) for value in candidate):
        diagnostics["invalid_support"] = 1
        return state, diagnostics
    if any(lattice.boundary1(candidate)):
        raise AssertionError("cycle proposal violated closure")
    delta = support_size(candidate) - support_size(state)
    diagnostics["support_delta"] = delta
    accept = True
    if delta > 0:
        for _ in range(delta):
            if rng.bit() != 0:
                accept = False
                break
    if accept:
        diagnostics["accepted"] = 1
        return candidate, diagnostics
    return state, diagnostics


def state_sha256(state: list[int]) -> str:
    return hashlib.sha256(bytes(value % 5 for value in state)).hexdigest()
