#!/usr/bin/env python3
"""Exact hard-target sector-umbrella ladder for L<=4 development."""

from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
from typing import Sequence

from mobility_kernel import (
    ALLOWED,
    LEGACY,
    PAIRS,
    BitStream,
    Torus4,
    current_hash,
    homology_vector,
    integer_current,
    principal,
    state_sha256,
    support_size,
    tristar_generator,
    tristar_witness,
)
SECTOR_DOMAIN = b"photon-z5-dual-mobility-qualification-1"


def translated_harmonic_plane(
    lattice: Torus4,
    pair_index: int,
    translation: int,
) -> dict[int, int]:
    """One translated coordinate two-torus, independent of rejected ladders."""

    a, b = PAIRS[pair_index]
    complement = tuple(axis for axis in range(4) if axis not in (a, b))
    if not 0 <= translation < lattice.L * lattice.L:
        raise ValueError("bad harmonic-plane translation")
    fixed = (translation // lattice.L, translation % lattice.L)
    result: dict[int, int] = {}
    for ia in range(lattice.L):
        for ib in range(lattice.L):
            x = [0] * 4
            x[a] = ia
            x[b] = ib
            x[complement[0]] = fixed[0]
            x[complement[1]] = fixed[1]
            result[lattice.plaq_index(tuple(x), a, b)] = 1
    return result


def sector_score(current: Sequence[int], homology: Sequence[int]) -> int:
    return int(any(current)) + int(any(homology))


@dataclass
class HardReplica:
    values: list[int]
    support: int
    current: list[int]
    current_nonzero_count: int
    homology: tuple[int, ...]

    @classmethod
    def from_values(cls, lattice: Torus4, values: Sequence[int]) -> "HardReplica":
        normalized = [value % 5 for value in values]
        if any(value not in ALLOWED for value in normalized):
            raise ValueError("hard replica contains +/-2")
        if any(lattice.boundary1(normalized)):
            raise ValueError("hard replica is not closed mod 5")
        current = integer_current(lattice, normalized)
        return cls(
            normalized,
            support_size(normalized),
            current,
            sum(value != 0 for value in current),
            homology_vector(lattice, normalized),
        )

    @property
    def score(self) -> int:
        return int(self.current_nonzero_count != 0) + int(any(self.homology))


@dataclass(frozen=True)
class HardCandidate:
    k: int
    support: int
    current_changes: tuple[tuple[int, int], ...]
    current_nonzero_count: int
    homology: tuple[int, ...]
    changes: tuple[tuple[int, int], ...]
    exponent: int
    integer_weight: int = 0


def candidate_current_changes(
    lattice: Torus4,
    replica: HardReplica,
    changes: Sequence[tuple[int, int]],
) -> tuple[tuple[tuple[int, int], ...], int]:
    boundary_delta: dict[int, int] = {}
    for plaquette, new in changes:
        old = replica.values[plaquette]
        delta = principal(new) - principal(old)
        if not delta:
            continue
        site = plaquette // len(PAIRS)
        pair = PAIRS[plaquette % len(PAIRS)]
        x = lattice.site_coord(site)
        for link, coefficient in lattice.plaquette_boundary(x, *pair).items():
            boundary_delta[link] = boundary_delta.get(link, 0) + delta * coefficient
    changes_out: list[tuple[int, int]] = []
    nonzero_count = replica.current_nonzero_count
    for link, value in boundary_delta.items():
        if value % 5:
            raise AssertionError("hard candidate current delta is not integral")
        old = replica.current[link]
        new = old + value // 5
        nonzero_count += int(new != 0) - int(old != 0)
        if new != old:
            changes_out.append((link, new))
    return tuple(changes_out), nonzero_count


def candidate_homology(
    lattice: Torus4,
    replica: HardReplica,
    changes: Sequence[tuple[int, int]],
) -> tuple[int, ...]:
    totals = [0] * len(PAIRS)
    for plaquette, new in changes:
        totals[plaquette % len(PAIRS)] += new - replica.values[plaquette]
    inverse = pow((lattice.L * lattice.L) % 5, -1, 5)
    return tuple(
        (replica.homology[index] + inverse * totals[index]) % 5
        for index in range(len(PAIRS))
    )


def hard_orbit_candidates(
    lattice: Torus4,
    replica: HardReplica,
    generator: dict[int, int],
    level: int,
) -> tuple[HardCandidate, ...]:
    raw: list[HardCandidate] = []
    for k in range(5):
        support = replica.support
        changes: list[tuple[int, int]] = []
        valid = True
        for plaquette, coefficient in generator.items():
            old = replica.values[plaquette]
            new = (old + k * coefficient) % 5
            if new not in ALLOWED:
                valid = False
                break
            support += int(new != 0) - int(old != 0)
            if new != old:
                changes.append((plaquette, new))
        if not valid:
            continue
        frozen_changes = tuple(changes)
        current_changes, current_nonzero_count = candidate_current_changes(
            lattice, replica, frozen_changes
        )
        homology = candidate_homology(lattice, replica, frozen_changes)
        score = int(current_nonzero_count != 0) + int(any(homology))
        exponent = level * score - support
        raw.append(
            HardCandidate(
                k,
                support,
                current_changes,
                current_nonzero_count,
                homology,
                frozen_changes,
                exponent,
            )
        )
    if not raw:
        raise AssertionError("hard orbit lost k=0")
    minimum = min(candidate.exponent for candidate in raw)
    return tuple(
        HardCandidate(
            candidate.k,
            candidate.support,
            candidate.current_changes,
            candidate.current_nonzero_count,
            candidate.homology,
            candidate.changes,
            candidate.exponent,
            1 << (candidate.exponent - minimum),
        )
        for candidate in raw
    )


def hard_orbit_heatbath(
    lattice: Torus4,
    replica: HardReplica,
    generator: dict[int, int],
    level: int,
    rng: BitStream,
) -> HardCandidate:
    candidates = hard_orbit_candidates(lattice, replica, generator, level)
    total = sum(candidate.integer_weight for candidate in candidates)
    draw = rng.bounded(total)
    cumulative = 0
    chosen = candidates[-1]
    for candidate in candidates:
        cumulative += candidate.integer_weight
        if draw < cumulative:
            chosen = candidate
            break
    for plaquette, new in chosen.changes:
        replica.values[plaquette] = new
    for link, new in chosen.current_changes:
        replica.current[link] = new
    replica.support = chosen.support
    replica.current_nonzero_count = chosen.current_nonzero_count
    replica.homology = chosen.homology
    return chosen


def sector_swap_accept(
    lower: HardReplica,
    upper: HardReplica,
    rng: BitStream,
) -> bool:
    exponent = lower.score - upper.score
    if exponent >= 0:
        return True
    return rng.bits(-exponent) == 0


@dataclass
class SectorDiagnostics:
    transitions: int = 0
    family_attempts: dict[str, int] = field(
        default_factory=lambda: {
            "hold": 0,
            "legacy": 0,
            "conjugation": 0,
            "cube": 0,
            "tristar": 0,
            "homology": 0,
            "swap": 0,
        }
    )
    swap_attempts: list[int] = field(default_factory=list)
    swap_accepts: list[int] = field(default_factory=list)
    label_roundtrips: list[int] = field(default_factory=list)
    target_current_entries: int = 0
    target_current_exits: int = 0
    target_current_hashes: set[str] = field(default_factory=set)
    target_current_event_hashes: set[str] = field(default_factory=set)
    target_current_entry_labels: set[int] = field(default_factory=set)
    target_homology_changes: int = 0
    target_homology_vectors: set[tuple[int, ...]] = field(default_factory=set)
    target_homology_component_changes: list[int] = field(
        default_factory=lambda: [0] * len(PAIRS)
    )
    target_homology_values: list[set[int]] = field(
        default_factory=lambda: [set() for _ in PAIRS]
    )
    local_current_births: list[int] = field(default_factory=list)
    local_current_deaths: list[int] = field(default_factory=list)
    local_homology_changes: list[int] = field(default_factory=list)
    top_current_entries: int = 0
    top_homology_entries: int = 0


class SectorLadder:
    """All levels use hard states; only exact sector indicators are biased."""

    def __init__(self, L: int, seed: int, start: str = "cold", S: int | None = None):
        if not 2 <= L <= 4:
            raise ValueError("sector development is hard-limited to 2<=L<=4")
        self.lattice = Torus4(L)
        self.S = max(15, L * L) if S is None else S
        if self.S < max(15, L * L):
            raise ValueError("S must cover both exact support barriers")
        self.rng = BitStream(seed, domain=SECTOR_DOMAIN)
        self.replicas = self._initial_replicas(start)
        self.labels = list(range(self.S + 1))
        self.label_phase = [0] * (self.S + 1)
        self.label_phase[0] = 1
        self.diagnostics = SectorDiagnostics(
            swap_attempts=[0] * self.S,
            swap_accepts=[0] * self.S,
            label_roundtrips=[0] * (self.S + 1),
            local_current_births=[0] * (self.S + 1),
            local_current_deaths=[0] * (self.S + 1),
            local_homology_changes=[0] * (self.S + 1),
        )
        self._record_target()

    def _initial_replicas(self, start: str) -> list[HardReplica]:
        zero = [0] * self.lattice.n_plaq
        if start == "cold":
            return [HardReplica.from_values(self.lattice, zero) for _ in range(self.S + 1)]
        if start != "stratified":
            raise ValueError("sector ladder start must be cold or stratified")
        _, witness, _, _ = tristar_witness(self.lattice)
        minus_witness = [(-value) % 5 for value in witness]
        h_state = [0] * self.lattice.n_plaq
        for plaquette, value in self.lattice.harmonic_plane(*PAIRS[0]).items():
            h_state[plaquette] = value
        minus_h = [(-value) % 5 for value in h_state]
        starts = (witness, minus_witness, h_state, minus_h)
        replicas = [HardReplica.from_values(self.lattice, zero)]
        for level in range(1, self.S + 1):
            replicas.append(
                HardReplica.from_values(self.lattice, starts[(level - 1) % len(starts)])
            )
        return replicas

    def _record_target(self) -> None:
        target = self.replicas[0]
        self.diagnostics.target_current_hashes.add(current_hash(target.current))
        self.diagnostics.target_homology_vectors.add(target.homology)
        for index, value in enumerate(target.homology):
            self.diagnostics.target_homology_values[index].add(value)

    def _target_before(self) -> tuple[bool, tuple[int, ...]]:
        target = self.replicas[0]
        return target.current_nonzero_count != 0, target.homology

    def _target_after(self, before: tuple[bool, tuple[int, ...]]) -> None:
        old_current, old_homology = before
        target = self.replicas[0]
        new_current = target.current_nonzero_count != 0
        if not old_current and new_current:
            self.diagnostics.target_current_entries += 1
            self.diagnostics.target_current_event_hashes.add(
                current_hash(target.current)
            )
            self.diagnostics.target_current_entry_labels.add(self.labels[0])
        elif old_current and not new_current:
            self.diagnostics.target_current_exits += 1
        if target.homology != old_homology:
            self.diagnostics.target_homology_changes += 1
            for index, (old, new) in enumerate(
                zip(old_homology, target.homology)
            ):
                self.diagnostics.target_homology_component_changes[index] += int(
                    old != new
                )
        self._record_target()

    def _record_local_change(
        self,
        level: int,
        old_current: bool,
        old_homology: tuple[int, ...],
    ) -> None:
        replica = self.replicas[level]
        new_current = replica.current_nonzero_count != 0
        if not old_current and new_current:
            self.diagnostics.local_current_births[level] += 1
        elif old_current and not new_current:
            self.diagnostics.local_current_deaths[level] += 1
        if replica.homology != old_homology:
            self.diagnostics.local_homology_changes[level] += 1

    def _update_label_endpoint(self, level: int) -> None:
        label = self.labels[level]
        if level == 0:
            if self.label_phase[label] == 2:
                self.diagnostics.label_roundtrips[label] += 1
            self.label_phase[label] = 1
        elif level == self.S and self.label_phase[label] == 1:
            self.label_phase[label] = 2

    def step(self) -> str:
        selector = self.rng.bits(4)
        target_before = self._target_before()
        target_touched = False
        old_top_current = self.replicas[self.S].current_nonzero_count != 0
        old_top_homology = any(self.replicas[self.S].homology)

        if selector == 0:
            family = "hold"
        elif selector == 1:
            family = "legacy"
            target = self.replicas[0]
            candidate, _ = LEGACY.metropolis_step(
                self.lattice, target.values, self.rng
            )
            if candidate != target.values:
                self.replicas[0] = HardReplica.from_values(self.lattice, candidate)
                target_touched = True
        elif selector == 2:
            family = "conjugation"
            level = self.rng.bounded(self.S + 1)
            replica = self.replicas[level]
            local_before = (replica.current_nonzero_count != 0, replica.homology)
            if replica.support:
                replica.values = [(-value) % 5 for value in replica.values]
                replica.current = [-value for value in replica.current]
                replica.homology = tuple((-value) % 5 for value in replica.homology)
                target_touched = level == 0
                self._record_local_change(level, *local_before)
        elif selector in (3, 4, 5):
            family = "cube"
            level = self.rng.bounded(self.S + 1)
            replica = self.replicas[level]
            local_before = (replica.current_nonzero_count != 0, replica.homology)
            chosen = hard_orbit_heatbath(
                self.lattice,
                replica,
                self.lattice.generator(0, self.rng.bounded(self.lattice.n_cubes)),
                level,
                self.rng,
            )
            self._record_local_change(level, *local_before)
            target_touched = level == 0 and bool(chosen.changes)
        elif selector in (6, 7, 8, 9):
            family = "tristar"
            level = self.rng.bounded(self.S + 1)
            replica = self.replicas[level]
            local_before = (replica.current_nonzero_count != 0, replica.homology)
            chosen = hard_orbit_heatbath(
                self.lattice,
                replica,
                tristar_generator(
                    self.lattice,
                    self.rng.bounded(self.lattice.n_plaq),
                    self.rng.bounded(4),
                ),
                level,
                self.rng,
            )
            self._record_local_change(level, *local_before)
            target_touched = level == 0 and bool(chosen.changes)
        elif selector in (10, 11):
            family = "homology"
            level = self.rng.bounded(self.S + 1)
            replica = self.replicas[level]
            local_before = (replica.current_nonzero_count != 0, replica.homology)
            chosen = hard_orbit_heatbath(
                self.lattice,
                replica,
                translated_harmonic_plane(
                    self.lattice,
                    self.rng.bounded(len(PAIRS)),
                    self.rng.bounded(self.lattice.L * self.lattice.L),
                ),
                level,
                self.rng,
            )
            self._record_local_change(level, *local_before)
            target_touched = level == 0 and bool(chosen.changes)
        else:
            family = "swap"
            level = self.rng.bounded(self.S)
            self.diagnostics.swap_attempts[level] += 1
            if sector_swap_accept(
                self.replicas[level], self.replicas[level + 1], self.rng
            ):
                self.replicas[level], self.replicas[level + 1] = (
                    self.replicas[level + 1],
                    self.replicas[level],
                )
                self.labels[level], self.labels[level + 1] = (
                    self.labels[level + 1],
                    self.labels[level],
                )
                self.diagnostics.swap_accepts[level] += 1
                self._update_label_endpoint(level)
                self._update_label_endpoint(level + 1)
                target_touched = level == 0

        self.diagnostics.transitions += 1
        self.diagnostics.family_attempts[family] += 1
        if target_touched:
            self._target_after(target_before)
        top = self.replicas[self.S]
        if not old_top_current and top.current_nonzero_count != 0:
            self.diagnostics.top_current_entries += 1
        if not old_top_homology and any(top.homology):
            self.diagnostics.top_homology_entries += 1
        return family

    def steps(self, count: int) -> None:
        for _ in range(count):
            self.step()


def sector_record(ladder: SectorLadder) -> dict[str, object]:
    rates = [
        accepts / attempts if attempts else 0.0
        for accepts, attempts in zip(
            ladder.diagnostics.swap_accepts, ladder.diagnostics.swap_attempts
        )
    ]
    target = ladder.replicas[0]
    return {
        "S": ladder.S,
        "family_attempts": ladder.diagnostics.family_attempts,
        "label_levels": [ladder.labels.index(label) for label in range(ladder.S + 1)],
        "label_phase": ladder.label_phase,
        "label_roundtrips": ladder.diagnostics.label_roundtrips,
        "max_swap_rate": max(rates, default=0.0),
        "min_swap_rate": min(rates, default=0.0),
        "replicas_with_roundtrip": sum(
            count > 0 for count in ladder.diagnostics.label_roundtrips
        ),
        "swap_accepts": ladder.diagnostics.swap_accepts,
        "swap_attempts": ladder.diagnostics.swap_attempts,
        "target_current_entries": ladder.diagnostics.target_current_entries,
        "target_current_exits": ladder.diagnostics.target_current_exits,
        "target_current_hashes": len(ladder.diagnostics.target_current_hashes),
        "target_current_event_hashes": len(
            ladder.diagnostics.target_current_event_hashes
        ),
        "target_current_entry_labels": sorted(
            ladder.diagnostics.target_current_entry_labels
        ),
        "target_homology_component_changes": (
            ladder.diagnostics.target_homology_component_changes
        ),
        "target_homology_changes": ladder.diagnostics.target_homology_changes,
        "target_homology_vectors": len(ladder.diagnostics.target_homology_vectors),
        "target_homology_values": [
            sorted(values) for values in ladder.diagnostics.target_homology_values
        ],
        "target_state_sha256": state_sha256(target.values),
        "target_support": target.support,
        "top_current_entries": ladder.diagnostics.top_current_entries,
        "top_homology_entries": ladder.diagnostics.top_homology_entries,
        "local_current_births": ladder.diagnostics.local_current_births,
        "local_current_deaths": ladder.diagnostics.local_current_deaths,
        "local_homology_changes": ladder.diagnostics.local_homology_changes,
        "transitions": ladder.diagnostics.transitions,
        "walkers_at_halftrip": sum(phase == 2 for phase in ladder.label_phase),
    }
