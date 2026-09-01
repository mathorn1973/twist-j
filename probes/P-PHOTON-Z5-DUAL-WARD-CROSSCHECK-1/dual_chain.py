#!/usr/bin/env python3
"""Independent closed-surface chain for the zero-evidence #756 execution.

The transition law is the frozen kernel from
``P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1/dual_cycle_kernel.py``.  This version is
arranged for the larger L=6,8 decision fixtures: proposals touch only their
sparse increment, while a complete state/closure check is performed before
the first transition and at every emitted sample.

Only the Python standard library is used.  Output is deterministic JSONL on
stdout; diagnostics and errors go to stderr.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
import sys
from typing import Iterable, Sequence


DIM = 4
PAIRS = tuple((a, b) for a in range(DIM) for b in range(a + 1, DIM))
TRIPLES = tuple(
    (a, b, c)
    for a in range(DIM)
    for b in range(a + 1, DIM)
    for c in range(b + 1, DIM)
)
PAIR_LABELS = tuple(f"{a}{b}" for a, b in PAIRS)
FAMILY_NAMES = ("inline1", "transverse1", "inline2", "transverse2")
ALLOWED_RESIDUES = (0, 1, 4)
BITSTREAM_DOMAIN = b"dual756"


def mod5(value: int) -> int:
    return value % 5


def principal_allowed(residue: int) -> bool:
    return residue % 5 in ALLOWED_RESIDUES


def support_size(state: Sequence[int]) -> int:
    return sum(1 for value in state if value % 5)


def principal(residue: int) -> int:
    """Return the frozen principal representative in {-1,0,+1}."""

    value = residue % 5
    if value == 4:
        return -1
    if value in (0, 1):
        return value
    raise ValueError(f"forbidden residue {value}")


def json_line(record: dict[str, object]) -> str:
    return json.dumps(
        record,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )


def emit_json(record: dict[str, object]) -> None:
    """Write canonical ASCII JSONL with LF even on Windows."""

    sys.stdout.buffer.write(json_line(record).encode("ascii") + b"\n")
    sys.stdout.buffer.flush()


def parse_seed(text: str) -> int:
    try:
        value = int(text, 0)
    except ValueError as error:
        raise argparse.ArgumentTypeError("seed must be an integer") from error
    if not 0 <= value < (1 << 128):
        raise argparse.ArgumentTypeError("seed must satisfy 0 <= seed < 2^128")
    return value


@dataclass
class BitStream:
    """The frozen SHA-256 counter bitstream, byte for byte."""

    seed: int
    domain: bytes = BITSTREAM_DOMAIN
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
    """Frozen four-torus indexing plus precomputed periodic neighbours."""

    def __init__(self, L: int):
        if L < 2:
            raise ValueError("L must be at least 2")
        self.L = L
        self.volume = L**DIM
        self.pair_index = {pair: index for index, pair in enumerate(PAIRS)}
        self.triple_index = {
            triple: index for index, triple in enumerate(TRIPLES)
        }
        self.coords = tuple(self.site_coord(site) for site in range(self.volume))
        self.forward = tuple(
            tuple(self.site_index(self.shift(x, mu)) for x in self.coords)
            for mu in range(DIM)
        )
        self.harmonic_generators = tuple(
            tuple(self._harmonic_plane_indices(a, b)) for a, b in PAIRS
        )
        self.pair_shifts = self._make_pair_shifts()
        angle = 2.0 * math.pi / L
        self.low_cos = tuple(math.cos(angle * coordinate) for coordinate in range(L))
        self.low_sin = tuple(math.sin(angle * coordinate) for coordinate in range(L))

    def site_index(self, x: Sequence[int]) -> int:
        value = 0
        for coordinate in x:
            value = value * self.L + (coordinate % self.L)
        return value

    def site_coord(self, index: int) -> tuple[int, int, int, int]:
        if not 0 <= index < self.volume:
            raise ValueError("site index out of range")
        result = [0] * DIM
        for mu in range(DIM - 1, -1, -1):
            result[mu] = index % self.L
            index //= self.L
        return tuple(result)  # type: ignore[return-value]

    def shift(
        self,
        x: Sequence[int],
        mu: int,
        delta: int = 1,
    ) -> tuple[int, int, int, int]:
        result = list(x)
        result[mu] = (result[mu] + delta) % self.L
        return tuple(result)  # type: ignore[return-value]

    def shifted_site(self, site: int, displacement: Sequence[int]) -> int:
        x = self.coords[site]
        return self.site_index(
            tuple(x[mu] + displacement[mu] for mu in range(DIM))
        )

    def _link_index_site(self, site: int, mu: int) -> int:
        return site * DIM + mu

    def _plaq_index_site(self, site: int, pair_index: int) -> int:
        return site * len(PAIRS) + pair_index

    def link_index(self, x: Sequence[int], mu: int) -> int:
        """Compatibility form of the frozen oriented-link index."""

        return self._link_index_site(self.site_index(x), mu)

    def plaq_index(self, x: Sequence[int], a: int, b: int) -> int:
        """Compatibility form of the frozen oriented-plaquette index."""

        if a > b:
            a, b = b, a
        return self._plaq_index_site(self.site_index(x), self.pair_index[(a, b)])

    @property
    def n_links(self) -> int:
        return self.volume * DIM

    @property
    def n_plaq(self) -> int:
        return self.volume * len(PAIRS)

    @property
    def n_cubes(self) -> int:
        return self.volume * len(TRIPLES)

    def _harmonic_plane_indices(self, a: int, b: int) -> Iterable[int]:
        pair_index = self.pair_index[(a, b)]
        for ia in range(self.L):
            for ib in range(self.L):
                x = [0] * DIM
                x[a] = ia
                x[b] = ib
                yield self._plaq_index_site(self.site_index(x), pair_index)

    def plaquette_boundary(
        self,
        x: Sequence[int],
        a: int,
        b: int,
    ) -> dict[int, int]:
        """The exact frozen boundary convention for one oriented face."""

        if a > b:
            a, b = b, a
        x_tuple = tuple(x)
        return {
            self.link_index(x_tuple, a): 1,
            self.link_index(self.shift(x_tuple, a), b): 1,
            self.link_index(self.shift(x_tuple, b), a): -1,
            self.link_index(x_tuple, b): -1,
        }

    def cube_boundary(
        self,
        x: Sequence[int],
        a: int,
        b: int,
        c: int,
    ) -> dict[int, int]:
        axes = tuple(sorted((a, b, c)))
        result: dict[int, int] = {}
        x_tuple = tuple(x)
        for position, axis in enumerate(axes):
            face = tuple(value for value in axes if value != axis)
            sign = 1 if position % 2 == 0 else -1
            upper = self.shift(x_tuple, axis)
            for base, coefficient in ((upper, sign), (x_tuple, -sign)):
                plaquette = self.plaq_index(base, *face)
                result[plaquette] = result.get(plaquette, 0) + coefficient
        return {
            plaquette: value % 5
            for plaquette, value in result.items()
            if value % 5
        }

    def harmonic_plane(self, a: int, b: int) -> dict[int, int]:
        if a > b:
            a, b = b, a
        pair_index = self.pair_index[(a, b)]
        return {
            plaquette: 1
            for plaquette in self.harmonic_generators[pair_index]
        }

    def boundary1(self, state: Sequence[int]) -> list[int]:
        if len(state) != self.n_plaq:
            raise ValueError("bad state length")
        boundary = [0] * self.n_links
        pair_count = len(PAIRS)
        for site in range(self.volume):
            base = site * pair_count
            x = self.coords[site]
            for pair_index, (a, b) in enumerate(PAIRS):
                value = state[base + pair_index] % 5
                if value == 0:
                    continue
                for link, coefficient in self.plaquette_boundary(x, a, b).items():
                    boundary[link] = (boundary[link] + coefficient * value) % 5
        return boundary

    def valid_state(self, state: Sequence[int]) -> bool:
        return (
            len(state) == self.n_plaq
            and all(principal_allowed(value) for value in state)
            and not any(self.boundary1(state))
        )

    def generator(self, kind: int, index: int) -> dict[int, int]:
        result: dict[int, int] = {}
        for plaquette, coefficient in self.generator_items(kind, index):
            value = (result.get(plaquette, 0) + coefficient) % 5
            if value:
                result[plaquette] = value
            else:
                result.pop(plaquette, None)
        return result

    def generator_items(self, kind: int, index: int) -> Iterable[tuple[int, int]]:
        """Yield the frozen generator's nonzero (plaquette,residue) entries."""

        if kind == 0:
            if not 0 <= index < self.n_cubes:
                raise ValueError("cube generator index out of range")
            site = index // len(TRIPLES)
            axes = TRIPLES[index % len(TRIPLES)]
            for position, axis in enumerate(axes):
                face = tuple(value for value in axes if value != axis)
                pair_index = self.pair_index[face]
                sign = 1 if position % 2 == 0 else 4
                yield self._plaq_index_site(self.forward[axis][site], pair_index), sign
                yield self._plaq_index_site(site, pair_index), (-sign) % 5
            return
        if kind == 1:
            if not 0 <= index < len(PAIRS):
                raise ValueError("homology generator index out of range")
            for plaquette in self.harmonic_generators[index]:
                yield plaquette, 1
            return
        raise ValueError("generator kind must be 0 or 1")

    def _make_pair_shifts(self) -> dict[str, tuple[tuple[int, ...], ...]]:
        result: dict[str, list[tuple[int, ...]]] = {
            name: [] for name in FAMILY_NAMES
        }
        for a, b in PAIRS:
            transverse = min(axis for axis in range(DIM) if axis not in (a, b))
            vectors = {
                "inline1": tuple(1 if axis == a else 0 for axis in range(DIM)),
                "transverse1": tuple(
                    1 if axis == transverse else 0 for axis in range(DIM)
                ),
                "inline2": tuple(2 if axis == a else 0 for axis in range(DIM)),
                "transverse2": tuple(
                    2 if axis == transverse else 0 for axis in range(DIM)
                ),
            }
            for name in FAMILY_NAMES:
                result[name].append(
                    tuple(
                        self.shifted_site(site, vectors[name])
                        for site in range(self.volume)
                    )
                )
        return {name: tuple(shifts) for name, shifts in result.items()}


def proposal_increment(lattice: Torus4, rng: BitStream) -> tuple[dict[int, int], int]:
    """Generate the exact frozen random-word cycle increment."""

    length = rng.geometric_half()
    increment: dict[int, int] = {}
    for _ in range(length):
        kind = rng.bit()
        index = rng.bounded(lattice.n_cubes if kind == 0 else len(PAIRS))
        sign = 1 if rng.bit() == 0 else 4
        for plaquette, coefficient in lattice.generator_items(kind, index):
            value = (increment.get(plaquette, 0) + sign * coefficient) % 5
            if value:
                increment[plaquette] = value
            else:
                increment.pop(plaquette, None)
    return increment, length


@dataclass
class ChainDiagnostics:
    transitions: int = 0
    proposal_letters: int = 0
    zero_words: int = 0
    accepted: int = 0
    rejected_firewall: int = 0
    rejected_metropolis: int = 0
    max_word_length: int = 0

    def record(self, word_length: int, terminal: str) -> None:
        self.transitions += 1
        self.proposal_letters += word_length
        self.max_word_length = max(self.max_word_length, word_length)
        if word_length == 0:
            self.zero_words += 1
        if terminal == "accepted":
            self.accepted += 1
        elif terminal == "firewall":
            self.rejected_firewall += 1
        elif terminal == "metropolis":
            self.rejected_metropolis += 1
        else:
            raise AssertionError(f"unknown transition terminal {terminal}")

    def as_record(self) -> dict[str, int]:
        return {
            "accepted": self.accepted,
            "max_word_length": self.max_word_length,
            "proposal_letters": self.proposal_letters,
            "rejected_firewall": self.rejected_firewall,
            "rejected_metropolis": self.rejected_metropolis,
            "transitions": self.transitions,
            "zero_words": self.zero_words,
        }


class DualChain:
    """Sparse exact Metropolis chain with an incrementally maintained support."""

    def __init__(self, lattice: Torus4, seed: int, start: str):
        self.lattice = lattice
        self.rng = BitStream(seed)
        self.state = self._initial_state(start)
        self.support = sum(1 for value in self.state if value)
        self.diagnostics = ChainDiagnostics()
        validate_state(self.lattice, self.state, self.support)

    def _initial_state(self, start: str) -> bytearray:
        if start == "cold":
            return bytearray(self.lattice.n_plaq)
        if start != "surface":
            raise ValueError("start must be cold or surface")
        if self.lattice.L % 2:
            raise ValueError("surface start requires even L")

        state = bytearray(self.lattice.n_plaq)
        triple_index = self.lattice.triple_index[(0, 1, 2)]
        even_coordinates = range(0, self.lattice.L, 2)
        for x0 in even_coordinates:
            for x1 in even_coordinates:
                for x2 in even_coordinates:
                    for x3 in even_coordinates:
                        site = self.lattice.site_index((x0, x1, x2, x3))
                        cube_index = site * len(TRIPLES) + triple_index
                        for plaquette, coefficient in self.lattice.generator_items(
                            0, cube_index
                        ):
                            state[plaquette] = (state[plaquette] + coefficient) % 5
        return state

    def step(self) -> None:
        increment, word_length = proposal_increment(self.lattice, self.rng)

        changes: list[tuple[int, int]] = []
        support_delta = 0
        for plaquette, coefficient in increment.items():
            old = self.state[plaquette]
            new = (old + coefficient) % 5
            if new not in ALLOWED_RESIDUES:
                self.diagnostics.record(word_length, "firewall")
                return
            support_delta += int(new != 0) - int(old != 0)
            changes.append((plaquette, new))

        if support_delta > 0:
            for _ in range(support_delta):
                if self.rng.bit() != 0:
                    self.diagnostics.record(word_length, "metropolis")
                    return

        for plaquette, value in changes:
            self.state[plaquette] = value
        self.support += support_delta
        if not 0 <= self.support <= self.lattice.n_plaq:
            raise AssertionError("incremental support left its exact range")
        self.diagnostics.record(word_length, "accepted")

    def steps(self, count: int) -> None:
        for _ in range(count):
            self.step()


def integer_boundary(lattice: Torus4, state: Sequence[int]) -> list[int]:
    """Compute partial n with principal integer representatives."""

    boundary = [0] * lattice.n_links
    forward = lattice.forward
    pair_count = len(PAIRS)
    for site in range(lattice.volume):
        base = site * pair_count
        link_base = site * DIM
        for pair_index, (a, b) in enumerate(PAIRS):
            value = principal(state[base + pair_index])
            if value == 0:
                continue
            boundary[link_base + a] += value
            boundary[forward[a][site] * DIM + b] += value
            boundary[forward[b][site] * DIM + a] -= value
            boundary[link_base + b] -= value
    return boundary


def current_from_boundary(boundary: Sequence[int]) -> list[int]:
    current: list[int] = []
    for value in boundary:
        if value % 5:
            raise AssertionError("state violates partial n = 0 mod 5")
        current.append(value // 5)
    return current


def validate_current_conservation(lattice: Torus4, current: Sequence[int]) -> None:
    divergence = [0] * lattice.volume
    for site in range(lattice.volume):
        base = site * DIM
        for mu in range(DIM):
            value = current[base + mu]
            divergence[site] -= value
            divergence[lattice.forward[mu][site]] += value
    if any(divergence):
        raise AssertionError("integer current violates partial j = 0")


def validate_state(
    lattice: Torus4,
    state: Sequence[int],
    expected_support: int | None = None,
) -> list[int]:
    """Run the full support, modular-closure and integer-current firewall."""

    if len(state) != lattice.n_plaq:
        raise AssertionError("bad state length")
    if any(value not in ALLOWED_RESIDUES for value in state):
        raise AssertionError("state contains a zero-weight residue")
    support = sum(1 for value in state if value)
    if expected_support is not None and support != expected_support:
        raise AssertionError("incremental support disagrees with full census")
    current = current_from_boundary(integer_boundary(lattice, state))
    validate_current_conservation(lattice, current)
    return current


def current_statistics(lattice: Torus4, current: Sequence[int]) -> dict[str, object]:
    sums = [0] * DIM
    square_sums = [0] * DIM
    nonzero = [0] * DIM
    for site in range(lattice.volume):
        base = site * DIM
        for mu in range(DIM):
            value = current[base + mu]
            sums[mu] += value
            square_sums[mu] += value * value
            nonzero[mu] += int(value != 0)

    total_links = lattice.n_links
    return {
        "j_mean": sum(sums) / total_links,
        "j_mean_by_direction": [value / lattice.volume for value in sums],
        "j_nonzero_count": sum(nonzero),
        "j_nonzero_count_by_direction": nonzero,
        "j_nonzero_density": sum(nonzero) / total_links,
        "j_nonzero_density_by_direction": [
            value / lattice.volume for value in nonzero
        ],
        "j_sum": sum(sums),
        "j_sum_by_direction": sums,
        "j2_mean": sum(square_sums) / total_links,
        "j2_mean_by_direction": [
            value / lattice.volume for value in square_sums
        ],
        "j2_sum": sum(square_sums),
        "j2_sum_by_direction": square_sums,
        "partial_j_zero": True,
    }


def low_momentum_statistics(
    lattice: Torus4,
    current: Sequence[int],
) -> dict[str, object]:
    momenta: list[dict[str, object]] = []
    trace_powers: list[float] = []
    volume = lattice.volume

    for momentum_axis in range(DIM):
        real = [0.0] * DIM
        imag = [0.0] * DIM
        for site, coordinates in enumerate(lattice.coords):
            cosine = lattice.low_cos[coordinates[momentum_axis]]
            minus_sine = -lattice.low_sin[coordinates[momentum_axis]]
            base = site * DIM
            for component in range(DIM):
                value = current[base + component]
                real[component] += value * cosine
                imag[component] += value * minus_sine
        component_power = [
            (real[mu] * real[mu] + imag[mu] * imag[mu]) / volume
            for mu in range(DIM)
        ]
        trace = sum(component_power)
        trace_powers.append(trace)
        momenta.append(
            {
                "component_imag": imag,
                "component_power": component_power,
                "component_real": real,
                "longitudinal_power": component_power[momentum_axis],
                "momentum_axis": momentum_axis,
                "sj_trace": trace,
                "transverse_power": trace - component_power[momentum_axis],
            }
        )

    return {
        "axis_average_sj_trace": sum(trace_powers) / DIM,
        "lowest_momenta": momenta,
    }


def plaquette_statistics(lattice: Torus4, state: Sequence[int]) -> dict[str, object]:
    sums = [0] * len(PAIRS)
    square_sums = [0] * len(PAIRS)
    pair_count = len(PAIRS)
    for site in range(lattice.volume):
        base = site * pair_count
        for pair_index in range(pair_count):
            value = principal(state[base + pair_index])
            sums[pair_index] += value
            square_sums[pair_index] += value * value

    total_plaquettes = lattice.n_plaq
    families: list[dict[str, object]] = []
    for family in FAMILY_NAMES:
        product_sums = [0] * pair_count
        shifts = lattice.pair_shifts[family]
        for pair_index in range(pair_count):
            shifted_sites = shifts[pair_index]
            product_sum = 0
            for site in range(lattice.volume):
                left = principal(state[site * pair_count + pair_index])
                right = principal(
                    state[shifted_sites[site] * pair_count + pair_index]
                )
                product_sum += left * right
            product_sums[pair_index] = product_sum
        families.append(
            {
                "family": family,
                "mean": sum(product_sums) / total_plaquettes,
                "mean_by_orientation": [
                    value / lattice.volume for value in product_sums
                ],
                "sum": sum(product_sums),
                "sum_by_orientation": product_sums,
            }
        )

    return {
        "n_mean": sum(sums) / total_plaquettes,
        "n_mean_by_orientation": [value / lattice.volume for value in sums],
        "n_sum": sum(sums),
        "n_sum_by_orientation": sums,
        "n2_mean": sum(square_sums) / total_plaquettes,
        "n2_mean_by_orientation": [
            value / lattice.volume for value in square_sums
        ],
        "n2_sum": sum(square_sums),
        "n2_sum_by_orientation": square_sums,
        "pair_products": families,
    }


def sample_record(chain: DualChain, index: int) -> dict[str, object]:
    current = validate_state(chain.lattice, chain.state, chain.support)
    record: dict[str, object] = {
        "diagnostics": chain.diagnostics.as_record(),
        "index": index,
        "state_sha256": hashlib.sha256(bytes(chain.state)).hexdigest(),
        "support": chain.support,
        "type": "sample",
    }
    record.update(plaquette_statistics(chain.lattice, chain.state))
    record.update(current_statistics(chain.lattice, current))
    record.update(low_momentum_statistics(chain.lattice, current))
    return record


def run(args: argparse.Namespace) -> int:
    if args.mode == "dev":
        if not 2 <= args.L <= 4:
            raise ValueError("development mode requires 2 <= L <= 4")
    elif args.mode == "decision":
        if args.L not in (6, 8):
            raise ValueError("decision mode requires L=6 or L=8")
    else:
        raise AssertionError("unrecognized execution mode")

    lattice = Torus4(args.L)
    chain = DualChain(lattice, args.seed, args.start)
    emit_json(
        {
            "L": args.L,
            "between_steps": args.between,
            "bitstream": "sha256-counter-msb-first",
            "domain": BITSTREAM_DOMAIN.decode("ascii"),
            "mode": args.mode,
            "orientation_order": list(PAIR_LABELS),
            "pair_product_families": list(FAMILY_NAMES),
            "samples": args.samples,
            "seed": f"0x{args.seed:032x}",
            "start": args.start,
            "thermal_steps": args.thermal,
            "type": "run",
        }
    )

    chain.steps(args.thermal)
    for sample_index in range(args.samples):
        chain.steps(args.between)
        emit_json(sample_record(chain, sample_index))

    emit_json(
        {
            "diagnostics": chain.diagnostics.as_record(),
            "final_state_sha256": hashlib.sha256(bytes(chain.state)).hexdigest(),
            "final_support": chain.support,
            "samples_emitted": args.samples,
            "type": "summary",
        }
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Frozen independent Z5 dual closed-surface chain"
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)
    for mode, help_text in (
        ("dev", "development fixture, restricted to 2 <= L <= 4"),
        ("decision", "zero-evidence decision chain, restricted to L=6,8"),
    ):
        subparser = subparsers.add_parser(mode, help=help_text)
        subparser.add_argument("--L", type=int, required=True)
        subparser.add_argument("--seed", type=parse_seed, required=True)
        subparser.add_argument("--thermal", type=int, required=True)
        subparser.add_argument("--samples", type=int, required=True)
        subparser.add_argument("--between", type=int, required=True)
        subparser.add_argument(
            "--start", choices=("cold", "surface"), required=True
        )
    return parser


def validate_cli_counts(args: argparse.Namespace) -> None:
    if args.thermal < 0:
        raise ValueError("thermal must be nonnegative")
    if args.samples <= 0:
        raise ValueError("samples must be positive")
    if args.between <= 0:
        raise ValueError("between must be positive")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        validate_cli_counts(args)
        return run(args)
    except (AssertionError, OSError, ValueError) as error:
        print(f"DUAL_CHAIN_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
