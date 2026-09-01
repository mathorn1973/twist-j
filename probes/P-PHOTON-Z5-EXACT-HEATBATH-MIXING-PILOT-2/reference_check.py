#!/usr/bin/env python3
"""Independent exact small-lattice fixture for the Pilot-2 C++ kernel."""

from __future__ import annotations

import argparse
import copy
import subprocess
import sys


D = 4
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
FACE_WEIGHTS = ((4, 0), (1, 1), (2, -1), (2, -1), (1, 1))
CAP = 256
MASK32 = (1 << 32) - 1
MASK64 = (1 << 64) - 1
DOMAINS = (0x484F5401, 0x4C4F4302, 0x4C494E03, 0x464C5404, 0x43484705)
HOT, LOCAL, LINE, FLAT, CHARGE = range(5)


class StopIntegrity(RuntimeError):
    pass


def mod5(value: int) -> int:
    return value % 5


def qadd(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def qsub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def qmul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    c, d = y
    return a * c + b * d, a * d + b * c + b * d


def qscale(x: tuple[int, int], n: int) -> tuple[int, int]:
    return x[0] * n, x[1] * n


def qsign(x: tuple[int, int]) -> int:
    p = 2 * x[0] + x[1]
    q = x[1]
    if p == 0 and q == 0:
        return 0
    if p >= 0 and q >= 0:
        return 1
    if p <= 0 and q <= 0:
        return -1
    if p >= 0:
        return 1 if p * p > 5 * q * q else -1
    return 1 if 5 * q * q > p * p else -1


def philox4x32_10(
    counter: tuple[int, int, int, int], key: tuple[int, int]
) -> tuple[int, int, int, int]:
    words = list(counter)
    keys = list(key)
    for round_index in range(10):
        product0 = 0xD2511F53 * words[0]
        product1 = 0xCD9E8D57 * words[2]
        lo0, hi0 = product0 & MASK32, (product0 >> 32) & MASK32
        lo1, hi1 = product1 & MASK32, (product1 >> 32) & MASK32
        words = [
            (hi1 ^ words[1] ^ keys[0]) & MASK32,
            lo1,
            (hi0 ^ words[3] ^ keys[1]) & MASK32,
            lo0,
        ]
        if round_index != 9:
            keys[0] = (keys[0] + 0x9E3779B9) & MASK32
            keys[1] = (keys[1] + 0xBB67AE85) & MASK32
    return tuple(words)  # type: ignore[return-value]


class CounterRng:
    def __init__(self, seed: int) -> None:
        self.key = seed & MASK32, (seed >> 32) & MASK32

    def block(self, kind: int, cycle: int, ordinal: int, block: int) -> tuple[int, ...]:
        return philox4x32_10((cycle, ordinal, DOMAINS[kind], block), self.key)

    def u64(self, kind: int, cycle: int, ordinal: int, block: int) -> int:
        words = self.block(kind, cycle, ordinal, block)
        return (words[0] << 32) | words[1]


class CounterBits:
    def __init__(self, rng: CounterRng, kind: int, cycle: int, ordinal: int) -> None:
        self.rng = rng
        self.kind = kind
        self.cycle = cycle
        self.ordinal = ordinal
        self.used = 0

    def next(self) -> int:
        block = self.used // 64
        offset = self.used % 64
        word = self.rng.u64(self.kind, self.cycle, self.ordinal, block)
        self.used += 1
        return (word >> (63 - offset)) & 1

    def label(self) -> str:
        return f"kind={self.kind} cycle={self.cycle} ordinal={self.ordinal}"


def exact_uniform5(rng: CounterRng, kind: int, cycle: int, ordinal: int) -> int:
    block = 0
    while True:
        word = rng.u64(kind, cycle, ordinal, block)
        if word < MASK64:
            return word % 5
        block += 1
        if block > MASK32:
            raise StopIntegrity("uniform5 counter exhausted")


def exact_category(weights: tuple[tuple[int, int], ...], bits: object) -> int:
    cumulative = [(0, 0)]
    for weight in weights:
        if qsign(weight) <= 0:
            raise AssertionError("nonpositive categorical mass")
        cumulative.append(qadd(cumulative[-1], weight))
    total = cumulative[-1]
    prefix = 0
    for n in range(64, CAP + 1, 64):
        for _ in range(64):
            prefix = (prefix << 1) | bits.next()  # type: ignore[attr-defined]
        scale = 1 << n
        for category in range(len(weights)):
            lower = qsub(qscale(total, prefix), qscale(cumulative[category], scale))
            upper = qsub(
                qscale(cumulative[category + 1], scale),
                qscale(total, prefix + 1),
            )
            if qsign(lower) >= 0 and qsign(upper) >= 0:
                return category
    raise StopIntegrity(f"categorical cap exhausted {bits.label()}")  # type: ignore[attr-defined]


class VectorBits:
    def __init__(self, values: list[int]) -> None:
        self.values = values
        self.cursor = 0

    def next(self) -> int:
        value = self.values[self.cursor]
        self.cursor += 1
        return value

    @staticmethod
    def label() -> str:
        return "vector"


class FifthBoundaryBits:
    def __init__(self) -> None:
        self.remainder = 1

    def next(self) -> int:
        self.remainder *= 2
        if self.remainder >= 5:
            self.remainder -= 5
            return 1
        return 0

    @staticmethod
    def label() -> str:
        return "fifth-boundary"


class RejectOnceRng:
    @staticmethod
    def u64(kind: int, cycle: int, ordinal: int, block: int) -> int:
        del kind, cycle, ordinal
        return MASK64 if block == 0 else 7


class Lattice:
    def __init__(self, linear_size: int, seed: int, start: str) -> None:
        self.L = linear_size
        self.V = linear_size**D
        self.rng = CounterRng(seed)
        self.coords = [self.decode(site) for site in range(self.V)]
        self.plus = [[0] * D for _ in range(self.V)]
        self.minus = [[0] * D for _ in range(self.V)]
        for site, coordinate in enumerate(self.coords):
            for mu in range(D):
                xp = list(coordinate)
                xm = list(coordinate)
                xp[mu] = (xp[mu] + 1) % self.L
                xm[mu] = (xm[mu] - 1) % self.L
                self.plus[site][mu] = self.encode(tuple(xp))
                self.minus[site][mu] = self.encode(tuple(xm))
        if start == "cold":
            self.links = [0] * (self.V * D)
        elif start == "hot":
            self.links = [
                exact_uniform5(self.rng, HOT, 0, ordinal)
                for ordinal in range(self.V * D)
            ]
        else:
            raise AssertionError("invalid start")
        self.flux = self.computed_flux()
        self.validate_line_geometry()

    def decode(self, site: int) -> tuple[int, int, int, int]:
        result = [0] * D
        for mu in reversed(range(D)):
            result[mu] = site % self.L
            site //= self.L
        return tuple(result)  # type: ignore[return-value]

    def encode(self, coordinate: tuple[int, ...]) -> int:
        site = 0
        for value in coordinate:
            site = site * self.L + value
        return site

    @staticmethod
    def pair_index(a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        return PAIRS.index((a, b))

    def computed_flux(self) -> list[int]:
        result = [0] * (self.V * len(PAIRS))
        for site in range(self.V):
            for pair, (a, b) in enumerate(PAIRS):
                result[site * 6 + pair] = mod5(
                    self.links[site * D + a]
                    + self.links[self.plus[site][a] * D + b]
                    - self.links[self.plus[site][b] * D + a]
                    - self.links[site * D + b]
                )
        return result

    def assert_flux(self) -> None:
        if self.computed_flux() != self.flux:
            raise AssertionError("Python flux cache mismatch")

    def incident(self, site: int, mu: int) -> list[tuple[int, int, int]]:
        result = []
        for nu in range(D):
            if nu == mu:
                continue
            pair = self.pair_index(mu, nu)
            sign = 1 if mu < nu else -1
            result.append((site, pair, sign))
            result.append((self.minus[site][nu], pair, -sign))
        return result

    def local_masses(self, site: int, mu: int) -> tuple[tuple[int, int], ...]:
        link_id = site * D + mu
        old = self.links[link_id]
        affected = self.incident(site, mu)
        masses = []
        for candidate in range(5):
            delta = candidate - old
            mass = (1, 0)
            for base, pair, sign in affected:
                value = mod5(self.flux[base * 6 + pair] + sign * delta)
                mass = qmul(mass, FACE_WEIGHTS[value])
            masses.append(mass)
        return tuple(masses)

    def apply_link_value(self, site: int, mu: int, selected: int) -> None:
        link_id = site * D + mu
        delta = selected - self.links[link_id]
        self.links[link_id] = mod5(selected)
        for base, pair, sign in self.incident(site, mu):
            face = base * 6 + pair
            self.flux[face] = mod5(self.flux[face] + sign * delta)

    def update_link(self, link_id: int, cycle: int) -> None:
        site, mu = divmod(link_id, D)
        masses = self.local_masses(site, mu)
        bits = CounterBits(self.rng, LOCAL, cycle, link_id)
        self.apply_link_value(site, mu, exact_category(masses, bits))

    def local_sweep(self, cycle: int, reverse: bool) -> None:
        order = range(self.V * D - 1, -1, -1) if reverse else range(self.V * D)
        for link_id in order:
            self.update_link(link_id, cycle)

    def line_faces(self, base: int, mu: int) -> list[tuple[int, int]]:
        if self.coords[base][mu] != 0:
            raise AssertionError("invalid line base")
        result = []
        site = base
        for _ in range(self.L):
            for face_base, pair, sign in self.incident(site, mu):
                result.append((face_base * 6 + pair, sign))
            site = self.plus[site][mu]
        if len(result) != 6 * self.L or len({face for face, _ in result}) != len(result):
            raise AssertionError("line face census")
        return result

    def validate_line_geometry(self) -> None:
        count = 0
        for mu in range(D):
            for base in range(self.V):
                if self.coords[base][mu] == 0:
                    self.line_faces(base, mu)
                    count += 1
        if count != D * self.L**3:
            raise AssertionError("line census")

    def line_masses(self, affected: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
        masses = []
        for delta in range(5):
            mass = (1, 0)
            for face, sign in affected:
                mass = qmul(mass, FACE_WEIGHTS[mod5(self.flux[face] + sign * delta)])
            masses.append(mass)
        return tuple(masses)

    def apply_line(self, base: int, mu: int, delta: int, affected: list[tuple[int, int]]) -> None:
        delta = mod5(delta)
        if delta == 0:
            return
        site = base
        for _ in range(self.L):
            link = site * D + mu
            self.links[link] = mod5(self.links[link] + delta)
            site = self.plus[site][mu]
        for face, sign in affected:
            self.flux[face] = mod5(self.flux[face] + sign * delta)

    def line_sweep(self, cycle: int, reverse: bool) -> None:
        lines = []
        ordinal = 0
        for mu in range(D):
            for base in range(self.V):
                if self.coords[base][mu] == 0:
                    lines.append((base, mu, ordinal))
                    ordinal += 1
        if len(lines) != D * self.L**3:
            raise AssertionError("complete line sweep")
        if reverse:
            lines.reverse()
        for base, mu, physical_ordinal in lines:
            affected = self.line_faces(base, mu)
            masses = self.line_masses(affected)
            bits = CounterBits(self.rng, LINE, cycle, physical_ordinal)
            delta = exact_category(masses, bits)
            self.apply_line(base, mu, delta, affected)

    def flat_sheet(self, cycle: int, mu: int) -> None:
        before = list(self.flux)
        shift = exact_uniform5(self.rng, FLAT, cycle, mu)
        for site in range(self.V):
            if self.coords[site][mu] == 0:
                link = site * D + mu
                self.links[link] = mod5(self.links[link] + shift)
        if self.flux != before:
            raise AssertionError("flat sheet changed cache bytes")

    def charge(self, cycle: int) -> None:
        apply = (self.rng.block(CHARGE, cycle, 0, 0)[0] >> 31) & 1
        if apply:
            self.links = [mod5(-value) for value in self.links]
            self.flux = [mod5(-value) for value in self.flux]

    def macro_cycle(self, cycle: int) -> None:
        reverse = bool(cycle & 1)
        self.local_sweep(cycle, reverse)
        self.line_sweep(cycle, reverse)
        for mu in range(D):
            self.flat_sheet(cycle, mu)
        self.charge(cycle)
        self.assert_flux()

    def global_weight(self) -> tuple[int, int]:
        result = (1, 0)
        for value in self.flux:
            result = qmul(result, FACE_WEIGHTS[value])
        return result

    def state_hash(self) -> int:
        result = 1469598103934665603
        for value in self.links + self.flux:
            result ^= value
            result = (result * 1099511628211) & MASK64
        return result


def masses_text(masses: tuple[tuple[int, int], ...]) -> str:
    return ";".join(f"{a},{b}" for a, b in masses)


def local_environment_digest() -> int:
    result = 1469598103934665603
    for key in range(5**6):
        cursor = key
        residual = [0] * 6
        for digit in reversed(range(6)):
            residual[digit] = cursor % 5
            cursor //= 5
        for candidate in range(5):
            mass = (1, 0)
            for digit in range(3):
                mass = qmul(mass, FACE_WEIGHTS[mod5(residual[digit] + candidate)])
            for digit in range(3, 6):
                mass = qmul(mass, FACE_WEIGHTS[mod5(residual[digit] - candidate)])
            for byte in f"{mass[0]},{mass[1]};".encode("ascii"):
                result ^= byte
                result = (result * 1099511628211) & MASK64
    return result


def fixture_text() -> str:
    zero = philox4x32_10((0, 0, 0, 0), (0, 0))
    assert zero == (0x6627E8D5, 0xE169C58D, 0xBC57AC4C, 0x9B00DBD8)
    assert len(set(DOMAINS)) == len(DOMAINS)

    rng = CounterRng(0x123456789ABCDEF0)
    namespace_words = tuple(rng.u64(kind, 7, 11, 0) for kind in range(5))
    assert namespace_words == (
        0x97CE33141A291992,
        0xD585CCC9ABE0F907,
        0xE5D6E154AE60448E,
        0xB486EF61E40D0516,
        0x080D764BF04C4E9A,
    )
    assert exact_uniform5(RejectOnceRng(), HOT, 0, 0) == 2  # type: ignore[arg-type]
    assert ((rng.block(CHARGE, 7, 11, 0)[0] >> 31) & 1) == 0

    lower_bits = [1] + [0] * 63
    upper_bits = [0] + [1] * 63
    assert exact_category(((1, 0), (1, 0)), VectorBits(upper_bits)) == 0
    assert exact_category(((1, 0), (1, 0)), VectorBits(lower_bits)) == 1
    try:
        exact_category(((1, 0),) * 5, FifthBoundaryBits())
    except StopIntegrity:
        pass
    else:
        raise AssertionError("forced 1/5 boundary did not exhaust cap")

    local = Lattice(3, 0x123456789ABCDEF0, "hot")
    local_digest = local_environment_digest()
    local_masses = local.local_masses(0, 0)
    assert local.links[0] == 2
    raw_residuals = tuple(
        (mod5(local.flux[base * 6 + pair] - sign * local.links[0]), sign)
        for base, pair, sign in local.incident(0, 0)
    )
    assert raw_residuals == ((0, 1), (2, -1), (2, 1), (0, -1), (4, 1), (0, -1))
    residual_plus = tuple(residual for residual, sign in raw_residuals if sign > 0)
    residual_minus = tuple(residual for residual, sign in raw_residuals if sign < 0)
    local_key = 0
    for residual in residual_plus + residual_minus:
        local_key = 5 * local_key + residual
    assert residual_plus == (0, 2, 4) and residual_minus == (2, 0, 0)
    assert local_key == 1800
    assert local_masses == ((128, -64), (20, 32), (8, -4), (52, -32), (2, 3))
    complete_local = []
    for candidate in range(5):
        shifted = copy.deepcopy(local)
        shifted.apply_link_value(0, 0, candidate)
        shifted.assert_flux()
        complete_local.append(shifted.global_weight())
    for i in range(5):
        for j in range(5):
            assert qmul(complete_local[i], local_masses[j]) == qmul(
                complete_local[j], local_masses[i]
            )

    line_masses_by_l = {}
    expected_lines = {
        3: ((5120, 8192), (64, 64), (5696, -3520), (16, 0), (1024, 1024)),
        4: ((64, 64), (16384, 16384), (53248, 86016), (256, 0), (59648, -36864)),
    }
    for linear_size in (3, 4):
        line = Lattice(linear_size, 0x0F1E2D3C4B5A6978, "hot")
        affected = line.line_faces(0, 0)
        masses = line.line_masses(affected)
        assert masses == expected_lines[linear_size]
        line_masses_by_l[linear_size] = masses
        complete_line = []
        for delta in range(5):
            shifted = copy.deepcopy(line)
            shifted.apply_line(0, 0, delta, shifted.line_faces(0, 0))
            shifted.assert_flux()
            complete_line.append(shifted.global_weight())
            rotated = shifted.line_masses(shifted.line_faces(0, 0))
            assert all(rotated[next_delta] == masses[(delta + next_delta) % 5]
                       for next_delta in range(5))
        for i in range(5):
            for j in range(5):
                assert qmul(complete_line[i], masses[j]) == qmul(
                    complete_line[j], masses[i]
                )

    identity = Lattice(3, 0x8877665544332211, "hot")
    original_weight = identity.global_weight()
    for mu in range(D):
        before = list(identity.flux)
        shift = mu + 1
        for site in range(identity.V):
            if identity.coords[site][mu] == 0:
                link = site * D + mu
                identity.links[link] = mod5(identity.links[link] + shift)
        assert identity.flux == before
        identity.assert_flux()
    identity.links = [mod5(-value) for value in identity.links]
    identity.flux = [mod5(-value) for value in identity.flux]
    identity.assert_flux()
    assert identity.global_weight() == original_weight

    hashes = {}
    for linear_size in (3, 4):
        state = Lattice(linear_size, 0x123456789ABCDEF0, "hot")
        state.macro_cycle(0)
        state.macro_cycle(1)
        hashes[linear_size] = state.state_hash()
    assert hashes == {3: 0xF2DDB5B90DEBF718, 4: 0x6119D2E215A1020B}

    lines = [
        "FIXTURE PHILOX_ZERO 6627e8d5e169c58dbc57ac4c9b00dbd8",
        "FIXTURE NAMESPACE HOT=97ce33141a291992 LOCAL=d585ccc9abe0f907 "
        "LINE=e5d6e154ae60448e FLAT=b486ef61e40d0516 CHARGE=080d764bf04c4e9a",
        "FIXTURE PREFIX_ENDPOINTS PASS",
        "FIXTURE CAP256_STOP_INTEGRITY PASS",
        "FIXTURE UNIFORM5_REJECTION PASS",
        "FIXTURE HASH_SCHEME TWISTJ_FNVLIKE64_V1",
        f"FIXTURE LOCAL_ENVIRONMENTS count=15625 digest={local_digest:016x}",
        f"FIXTURE LOCAL_WITNESS old={local.links[0]} "
        f"residual_plus={','.join(map(str, residual_plus))} "
        f"residual_minus={','.join(map(str, residual_minus))} "
        f"key={local_key} masses={masses_text(local_masses)}",
        f"FIXTURE LINE_L3 masses={masses_text(line_masses_by_l[3])}",
        f"FIXTURE LINE_L4 masses={masses_text(line_masses_by_l[4])}",
        f"FIXTURE L3_TWO_CYCLE_STATE_HASH {hashes[3]:016x}",
        f"FIXTURE L4_TWO_CYCLE_STATE_HASH {hashes[4]:016x}",
        "FIXTURE RESULT PASS",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    if sys.flags.optimize != 0:
        raise RuntimeError("reference fixture forbids Python optimization")
    parser = argparse.ArgumentParser()
    parser.add_argument("--cpp", help="optional compiled C++ fixture executable")
    args = parser.parse_args()
    expected = fixture_text()
    if args.cpp:
        completed = subprocess.run(
            [args.cpp, "--fixture"], capture_output=True, check=False
        )
        if (completed.returncode != 0 or completed.stderr
                or completed.stdout != expected.encode("ascii")):
            raise AssertionError(
                "C++/Python fixture mismatch: "
                f"returncode={completed.returncode} stderr={completed.stderr!r}"
            )
    sys.stdout.buffer.write(expected.encode("ascii"))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"REFERENCE ERROR: {error}", file=sys.stderr)
        raise SystemExit(2)
