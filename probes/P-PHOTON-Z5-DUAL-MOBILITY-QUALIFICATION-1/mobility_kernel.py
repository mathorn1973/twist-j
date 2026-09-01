#!/usr/bin/env python3
"""Development-only exact mobility wrapper for the frozen #767 dual kernel.

The module deliberately accepts only L<=4.  It contains no primal reader and
no Ward observable.  Its purpose is to qualify current and homology mobility
before a fresh formal cross-check can even be proposed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import importlib.util
from pathlib import Path
import sys
from typing import Iterable, Sequence


PROBE = "P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1"
DOMAIN = b"dual756mobility1-development"
LEGACY_SHA256 = "13a48372cac01c7990a489f04b96e7329af900c0e7917d3085eeaf4462ef77d0"
ALLOWED = (0, 1, 4)
PAIRS = tuple((a, b) for a in range(4) for b in range(a + 1, 4))
TRIPLES = tuple(
    (a, b, c)
    for a in range(4)
    for b in range(a + 1, 4)
    for c in range(b + 1, 4)
)
FAMILIES = (
    "hold",
    "conjugation",
    "legacy_word",
    "cube_heatbath",
    "tristar_heatbath",
    "homology_heatbath",
)


def _load_legacy():
    root = Path(__file__).resolve().parents[2]
    path = (
        root
        / "probes"
        / "P-PHOTON-Z5-DUAL-WORM-CROSSCHECK-1"
        / "dual_cycle_kernel.py"
    )
    if hashlib.sha256(path.read_bytes()).hexdigest() != LEGACY_SHA256:
        raise RuntimeError("immutable #767 kernel failed SHA-256 custody")
    spec = importlib.util.spec_from_file_location("photon_dual_767", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load immutable #767 kernel")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


LEGACY = _load_legacy()
BitStream = LEGACY.BitStream
Torus4 = LEGACY.Torus4


def principal(residue: int) -> int:
    value = residue % 5
    if value == 4:
        return -1
    if value in (0, 1):
        return value
    raise ValueError(f"forbidden hard-target residue {value}")


def support_size(state: Sequence[int]) -> int:
    return sum(value % 5 != 0 for value in state)


def add_cycles(*cycles: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for cycle in cycles:
        for plaquette, coefficient in cycle.items():
            value = (result.get(plaquette, 0) + coefficient) % 5
            if value:
                result[plaquette] = value
            else:
                result.pop(plaquette, None)
    return result


def scale_cycle(cycle: dict[int, int], scalar: int) -> dict[int, int]:
    return {
        plaquette: (scalar * coefficient) % 5
        for plaquette, coefficient in cycle.items()
        if (scalar * coefficient) % 5
    }


def cycle_state(lattice: Torus4, cycle: dict[int, int]) -> list[int]:
    state = [0] * lattice.n_plaq
    for plaquette, coefficient in cycle.items():
        state[plaquette] = coefficient % 5
    return state


def aligned_incident_cubes(
    lattice: Torus4,
    plaquette: int,
) -> tuple[dict[int, int], ...]:
    """Return the four incident cube boundaries aligned +1 at plaquette."""

    pair_index = plaquette % len(PAIRS)
    site = plaquette // len(PAIRS)
    a, b = PAIRS[pair_index]
    x = lattice.site_coord(site)
    complement = tuple(axis for axis in range(4) if axis not in (a, b))
    incidents: list[dict[int, int]] = []
    for axis in complement:
        axes = tuple(sorted((a, b, axis)))
        for base in (x, lattice.shift(x, axis, -1)):
            cube = lattice.cube_boundary(base, *axes)
            central = cube.get(plaquette, 0) % 5
            if central not in (1, 4):
                raise AssertionError("incident cube lacks central face")
            incidents.append(scale_cycle(cube, 1 if central == 1 else 4))
    if len(incidents) != 4:
        raise AssertionError("a 4D plaquette must have four incident cubes")
    if any(cycle.get(plaquette) != 1 for cycle in incidents):
        raise AssertionError("incident alignment failed")
    return tuple(incidents)


def tristar_generator(
    lattice: Torus4,
    plaquette: int,
    omitted: int,
) -> dict[int, int]:
    if not 0 <= omitted < 4:
        raise ValueError("omitted incident cube must be 0..3")
    incidents = aligned_incident_cubes(lattice, plaquette)
    generator = add_cycles(
        *(cycle for index, cycle in enumerate(incidents) if index != omitted)
    )
    if generator.get(plaquette) != 3:
        raise AssertionError("tri-star central coefficient must be +3 mod 5")
    return generator


def tristar_witness(
    lattice: Torus4,
    pair_index: int = 0,
    omitted: int = 0,
) -> tuple[list[int], list[int], int, dict[int, int]]:
    """Return the canonical 6-face -> 21-face current witness pair."""

    if lattice.L < 3:
        raise ValueError("nonwrapping tri-star witness requires L>=3")
    x = (1, 1, 1, 1)
    plaquette = lattice.plaq_index(x, *PAIRS[pair_index])
    incidents = aligned_incident_cubes(lattice, plaquette)
    before = cycle_state(lattice, incidents[omitted])
    generator = tristar_generator(lattice, plaquette, omitted)
    after = LEGACY.add_increment(before, generator)
    if not lattice.valid_state(before) or not lattice.valid_state(after):
        raise AssertionError("canonical tri-star witness left hard target")
    return before, after, plaquette, generator


def integer_boundary(lattice: Torus4, state: Sequence[int]) -> list[int]:
    boundary = [0] * lattice.n_links
    for site in range(lattice.volume):
        x = lattice.site_coord(site)
        for a, b in PAIRS:
            value = principal(state[lattice.plaq_index(x, a, b)])
            if not value:
                continue
            for link, coefficient in lattice.plaquette_boundary(x, a, b).items():
                boundary[link] += coefficient * value
    return boundary


def integer_current(lattice: Torus4, state: Sequence[int]) -> list[int]:
    boundary = integer_boundary(lattice, state)
    if any(value % 5 for value in boundary):
        raise AssertionError("integer lift violates modular closure")
    current = [value // 5 for value in boundary]
    divergence = [0] * lattice.volume
    for site in range(lattice.volume):
        x = lattice.site_coord(site)
        for axis in range(4):
            value = current[lattice.link_index(x, axis)]
            divergence[site] -= value
            divergence[lattice.site_index(lattice.shift(x, axis))] += value
    if any(divergence):
        raise AssertionError("integer current is not conserved")
    return current


def homology_vector(lattice: Torus4, state: Sequence[int]) -> tuple[int, ...]:
    """H_2(T^4;Z_5) coordinates for L coprime to five."""

    scale = (lattice.L * lattice.L) % 5
    inverse = pow(scale, -1, 5)
    totals = [0] * len(PAIRS)
    for site in range(lattice.volume):
        base = site * len(PAIRS)
        for pair_index in range(len(PAIRS)):
            totals[pair_index] += state[base + pair_index]
    return tuple((inverse * total) % 5 for total in totals)


def validate_state(lattice: Torus4, state: Sequence[int]) -> None:
    if not lattice.valid_state(list(state)):
        raise AssertionError("state left the closed hard target")
    integer_current(lattice, state)
    homology_vector(lattice, state)


@dataclass(frozen=True)
class OrbitCandidate:
    k: int
    support: int
    changes: tuple[tuple[int, int], ...]
    integer_weight: int = 0


def orbit_candidates(
    state: Sequence[int],
    generator: dict[int, int],
    old_support: int | None = None,
) -> tuple[OrbitCandidate, ...]:
    if old_support is None:
        old_support = support_size(state)
    raw: list[tuple[int, int, tuple[tuple[int, int], ...]]] = []
    for k in range(5):
        support = old_support
        changes: list[tuple[int, int]] = []
        valid = True
        for plaquette, coefficient in generator.items():
            old = state[plaquette] % 5
            new = (old + k * coefficient) % 5
            if new not in ALLOWED:
                valid = False
                break
            support += int(new != 0) - int(old != 0)
            if new != old:
                changes.append((plaquette, new))
        if valid:
            raw.append((k, support, tuple(changes)))
    if not raw:
        raise AssertionError("orbit heat-bath lost its k=0 state")
    max_support = max(support for _, support, _ in raw)
    return tuple(
        OrbitCandidate(k, support, changes, 1 << (max_support - support))
        for k, support, changes in raw
    )


def exact_orbit_heatbath(
    state: Sequence[int],
    generator: dict[int, int],
    rng: BitStream,
    old_support: int | None = None,
) -> tuple[list[int], OrbitCandidate, tuple[OrbitCandidate, ...]]:
    candidates = orbit_candidates(state, generator, old_support)
    total = sum(candidate.integer_weight for candidate in candidates)
    draw = rng.bounded(total)
    chosen = candidates[-1]
    cumulative = 0
    for candidate in candidates:
        cumulative += candidate.integer_weight
        if draw < cumulative:
            chosen = candidate
            break
    result = list(state)
    for plaquette, value in chosen.changes:
        result[plaquette] = value
    return result, chosen, candidates


def changed_indices(before: Sequence[int], after: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        index for index, (left, right) in enumerate(zip(before, after)) if left != right
    )


@dataclass
class FamilyDiagnostics:
    attempts: int = 0
    changed: int = 0
    current_changed: int = 0
    homology_changed: int = 0


@dataclass
class MobilityDiagnostics:
    transitions: int = 0
    families: dict[str, FamilyDiagnostics] = field(
        default_factory=lambda: {name: FamilyDiagnostics() for name in FAMILIES}
    )
    current_hashes: set[str] = field(default_factory=set)
    homology_vectors: set[tuple[int, ...]] = field(default_factory=set)
    first_nonzero_current: int | None = None
    current_zero_to_nonzero: int = 0
    current_nonzero_to_zero: int = 0
    homology_sector_changes: int = 0


def current_hash(current: Sequence[int]) -> str:
    payload = ",".join(str(value) for value in current).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


class MobilityChain:
    """Exact random-scan wrapper; every component is separately reversible."""

    def __init__(self, L: int, seed: int, start: str):
        if not 2 <= L <= 4:
            raise ValueError("mobility development is hard-limited to 2<=L<=4")
        self.lattice = Torus4(L)
        self.rng = BitStream(seed, domain=DOMAIN)
        self.state = self._initial_state(start)
        self.support = support_size(self.state)
        self.current = integer_current(self.lattice, self.state)
        self.homology = homology_vector(self.lattice, self.state)
        self.diagnostics = MobilityDiagnostics()
        self._record_state()
        validate_state(self.lattice, self.state)

    def _initial_state(self, start: str) -> list[int]:
        if start == "cold":
            return [0] * self.lattice.n_plaq
        if start == "homology":
            return cycle_state(self.lattice, self.lattice.harmonic_plane(*PAIRS[0]))
        before, after, _, _ = tristar_witness(self.lattice)
        if start == "surface":
            return before
        if start == "witness":
            return after
        if start == "minus_witness":
            return [(-value) % 5 for value in after]
        raise ValueError("start must be cold, surface, homology, witness, or minus_witness")

    def _record_state(self) -> None:
        self.diagnostics.current_hashes.add(current_hash(self.current))
        self.diagnostics.homology_vectors.add(self.homology)

    def step(self) -> str:
        selector = self.rng.bits(4)
        if selector == 0:
            family = "hold"
            candidate = self.state.copy()
        elif selector == 1:
            family = "conjugation"
            candidate = [(-value) % 5 for value in self.state]
        elif selector in (2, 3):
            family = "legacy_word"
            candidate, _ = LEGACY.metropolis_step(
                self.lattice, self.state, self.rng
            )
        elif selector in (4, 5, 6, 7):
            family = "cube_heatbath"
            generator = self.lattice.generator(
                0, self.rng.bounded(self.lattice.n_cubes)
            )
            candidate, _, _ = exact_orbit_heatbath(
                self.state, generator, self.rng, self.support
            )
        elif selector in (8, 9, 10, 11, 12, 13):
            family = "tristar_heatbath"
            plaquette = self.rng.bounded(self.lattice.n_plaq)
            omitted = self.rng.bounded(4)
            generator = tristar_generator(self.lattice, plaquette, omitted)
            candidate, _, _ = exact_orbit_heatbath(
                self.state, generator, self.rng, self.support
            )
        else:
            family = "homology_heatbath"
            generator = self.lattice.generator(1, self.rng.bounded(len(PAIRS)))
            candidate, _, _ = exact_orbit_heatbath(
                self.state, generator, self.rng, self.support
            )

        family_stats = self.diagnostics.families[family]
        family_stats.attempts += 1
        self.diagnostics.transitions += 1
        old_current_nonzero = any(self.current)
        old_homology = self.homology
        indices = changed_indices(self.state, candidate)
        if indices:
            family_stats.changed += 1
            new_current = integer_current(self.lattice, candidate)
            new_homology = homology_vector(self.lattice, candidate)
            if new_current != self.current:
                family_stats.current_changed += 1
            if new_homology != self.homology:
                family_stats.homology_changed += 1
                self.diagnostics.homology_sector_changes += 1
            self.state = candidate
            self.support = support_size(candidate)
            self.current = new_current
            self.homology = new_homology

        new_current_nonzero = any(self.current)
        if not old_current_nonzero and new_current_nonzero:
            self.diagnostics.current_zero_to_nonzero += 1
            if self.diagnostics.first_nonzero_current is None:
                self.diagnostics.first_nonzero_current = self.diagnostics.transitions
        elif old_current_nonzero and not new_current_nonzero:
            self.diagnostics.current_nonzero_to_zero += 1
        if old_homology != self.homology:
            self.diagnostics.homology_vectors.add(self.homology)
        self._record_state()
        return family

    def steps(self, count: int, validate_every: int = 0) -> None:
        for index in range(count):
            self.step()
            if validate_every and (index + 1) % validate_every == 0:
                validate_state(self.lattice, self.state)


def state_sha256(state: Sequence[int]) -> str:
    return hashlib.sha256(bytes(value % 5 for value in state)).hexdigest()


def diagnostics_record(chain: MobilityChain) -> dict[str, object]:
    return {
        "current_hashes": len(chain.diagnostics.current_hashes),
        "current_nonzero_to_zero": chain.diagnostics.current_nonzero_to_zero,
        "current_zero_to_nonzero": chain.diagnostics.current_zero_to_nonzero,
        "families": {
            name: {
                "attempts": stats.attempts,
                "changed": stats.changed,
                "current_changed": stats.current_changed,
                "homology_changed": stats.homology_changed,
            }
            for name, stats in chain.diagnostics.families.items()
        },
        "final_current_nonzero": sum(value != 0 for value in chain.current),
        "final_homology": list(chain.homology),
        "final_state_sha256": state_sha256(chain.state),
        "final_support": chain.support,
        "first_nonzero_current": chain.diagnostics.first_nonzero_current,
        "homology_sector_changes": chain.diagnostics.homology_sector_changes,
        "homology_vectors": len(chain.diagnostics.homology_vectors),
        "transitions": chain.diagnostics.transitions,
    }
