#!/usr/bin/env python3
"""NON-CANONICAL reconstruction of the finite living kernel.

This module is local entropy-selection infrastructure.  It imports definitions
from the merged public P-ENTROPY-MIRROR-1 verifier, but it does not invoke that
verifier's ``main`` function and is not a formal probe execution.  The data
below therefore carry no claim status and must not be used as run evidence.

The useful output is an exact address for every recurrent state::

    (component, half, cell, q)  with q in F_5.

Here ``cell`` is the canonical, minimum-state-ordered level-2 pentagon within
one component-half.  The coherent public level-2 return gives the ``q``
coordinate.  Every one-tick map is then exposed as a component-preserving cell
map together with an affine rule ``q -> a*q + b (mod 5)``.

Python standard library only; it creates no scientific output files.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import MappingProxyType, ModuleType
from typing import Iterable, Mapping


MODULUS = 5
STATE_COUNT = MODULUS**6
REPO_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_MIRROR = (
    REPO_ROOT / "probes" / "P-ENTROPY-MIRROR-1" / "verify.py"
)


@dataclass(frozen=True, order=True)
class LivingAddress:
    """Canonical coordinates of one state in the recurrent living carrier."""

    component: int
    half: int
    cell: int
    q: int


@dataclass(frozen=True)
class Pentagon:
    """One canonical level-2 five-cell in its coherent F_5 gauge."""

    id: int
    component: int
    half: int
    local: int
    states: tuple[int, ...]
    state_by_q: tuple[int, ...]

    @property
    def origin(self) -> int:
        return self.state_by_q[0]


@dataclass(frozen=True)
class CellAction:
    """The quotient and affine parts of one letter on one source cell."""

    epsilon: int
    source_cell: int
    target_cell: int
    component: int
    source_half: int
    target_half: int
    source_local: int
    target_local: int
    multiplier: int
    offset: int

    def apply_q(self, q: int) -> int:
        if not 0 <= q < MODULUS:
            raise ValueError("q must lie in F_5")
        return (self.multiplier * q + self.offset) % MODULUS


@dataclass(frozen=True)
class CheckResult:
    """One exact local reconstruction check."""

    name: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class LivingKernel:
    """Reusable exact decomposition of the merged public finite kernel."""

    letters: tuple[tuple[int, ...], tuple[int, ...]]
    support: frozenset[int]
    components: tuple[frozenset[int], ...]
    halves: tuple[frozenset[int], frozenset[int]]
    pentagons: tuple[Pentagon, ...]
    cells_by_half: tuple[tuple[int, ...], tuple[int, ...]]
    singlet_component: int
    component_of_state: tuple[int, ...]
    half_of_state: tuple[int, ...]
    cell_of_state: tuple[int, ...]
    q_of_state: tuple[int, ...]
    cell_lookup: Mapping[tuple[int, int, int], int]
    actions: tuple[tuple[CellAction, ...], tuple[CellAction, ...]]

    def encode_state(self, state: int) -> LivingAddress:
        """Return the canonical living address of ``state``."""

        if not 0 <= state < STATE_COUNT or self.cell_of_state[state] < 0:
            raise ValueError("state is not in the recurrent living carrier")
        cell = self.pentagons[self.cell_of_state[state]]
        return LivingAddress(
            component=cell.component,
            half=cell.half,
            cell=cell.local,
            q=self.q_of_state[state],
        )

    def decode_address(self, address: LivingAddress) -> int:
        """Return the encoded kernel state at ``address``."""

        if not 0 <= address.q < MODULUS:
            raise ValueError("q must lie in F_5")
        try:
            cell_id = self.cell_lookup[
                (address.component, address.half, address.cell)
            ]
        except KeyError as exc:
            raise ValueError("unknown component-half-cell address") from exc
        return self.pentagons[cell_id].state_by_q[address.q]

    def cell_id(self, component: int, half: int, cell: int) -> int:
        """Resolve a local component-half cell label to its global cell id."""

        try:
            return self.cell_lookup[(component, half, cell)]
        except KeyError as exc:
            raise ValueError("unknown component-half-cell address") from exc

    def cell_action(
        self, epsilon: int, component: int, half: int, cell: int
    ) -> CellAction:
        """Return the exact cell/affine action of ``F_epsilon``."""

        if epsilon not in (0, 1):
            raise ValueError("epsilon must be 0 or 1")
        return self.actions[epsilon][self.cell_id(component, half, cell)]

    def tick_address(self, epsilon: int, address: LivingAddress) -> LivingAddress:
        """Apply one public branch letter entirely in decomposed coordinates."""

        action = self.cell_action(
            epsilon, address.component, address.half, address.cell
        )
        return LivingAddress(
            component=action.component,
            half=action.target_half,
            cell=action.target_local,
            q=action.apply_q(address.q),
        )

    def tick_state(self, epsilon: int, state: int) -> int:
        """Apply one letter via the decomposed address model."""

        return self.decode_address(self.tick_address(epsilon, self.encode_state(state)))

    def apply_word(
        self, word: Iterable[int], address: LivingAddress
    ) -> LivingAddress:
        """Apply a finite driver word from left to right in address form."""

        result = address
        for epsilon in word:
            result = self.tick_address(epsilon, result)
        return result

    def component_cells(self, component: int, half: int) -> tuple[int, ...]:
        """Return global cell ids in canonical local order."""

        result = []
        local = 0
        while (component, half, local) in self.cell_lookup:
            result.append(self.cell_lookup[(component, half, local)])
            local += 1
        if not result:
            raise ValueError("unknown component-half")
        return tuple(result)


def _load_public_mirror() -> ModuleType:
    """Load definitions only; never invoke the public verifier entry point."""

    spec = spec_from_file_location("public_entropy_mirror_1", PUBLIC_MIRROR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load merged P-ENTROPY-MIRROR-1 definitions")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _cycle_type(mapping: tuple[int, ...], points: Iterable[int]) -> Counter[int]:
    remaining = set(points)
    cycles: Counter[int] = Counter()
    while remaining:
        start = min(remaining)
        state = start
        length = 0
        while state in remaining:
            remaining.remove(state)
            state = mapping[state]
            length += 1
        if state != start:
            raise ValueError("map is not a permutation of the requested carrier")
        cycles[length] += 1
    return cycles


def _affine_rule(
    letter: tuple[int, ...], source: Pentagon, target: Pentagon
) -> tuple[int, int]:
    source_q = {state: q for q, state in enumerate(source.state_by_q)}
    target_q = {state: q for q, state in enumerate(target.state_by_q)}
    values = [0] * MODULUS
    for state, q in source_q.items():
        values[q] = target_q[letter[state]]
    offset = values[0]
    multiplier = (values[1] - offset) % MODULUS
    if multiplier == 0 or any(
        values[q] != (multiplier * q + offset) % MODULUS
        for q in range(MODULUS)
    ):
        raise ValueError("one-tick cell map is not affine over F_5")
    return multiplier, offset


@lru_cache(maxsize=1)
def reconstruct() -> LivingKernel:
    """Reconstruct and cache the complete local living-kernel data model."""

    public = _load_public_mirror()
    letters = public.build_letters()
    tm = public.thue_morse(1 << 16)
    support_raw, components_raw = public.census(letters, tm)
    support = frozenset(support_raw)
    components = tuple(frozenset(component) for component in components_raw)
    halves = (
        frozenset(letters[0][state] for state in support),
        frozenset(letters[1][state] for state in support),
    )

    component_of_state = [-1] * STATE_COUNT
    for component_id, component in enumerate(components):
        for state in component:
            if component_of_state[state] != -1:
                raise ValueError("recurrent components overlap")
            component_of_state[state] = component_id

    half_of_state = [-1] * STATE_COUNT
    for half, points in enumerate(halves):
        for state in points:
            if half_of_state[state] != -1:
                raise ValueError("living halves overlap")
            half_of_state[state] = half

    phi_1 = (
        public.compose(letters[1], letters[0]),
        public.compose(letters[0], letters[1]),
    )
    phi_2 = (
        public.compose(phi_1[1], phi_1[0]),
        public.compose(phi_1[0], phi_1[1]),
    )
    gauge_generators = (
        public.compose(phi_2[0], phi_2[1]),
        public.compose(phi_2[1], phi_2[0]),
    )

    pentagons_mutable: list[Pentagon] = []
    cell_lookup: dict[tuple[int, int, int], int] = {}
    cell_of_state = [-1] * STATE_COUNT
    q_of_state = [-1] * STATE_COUNT
    cells_by_half_mutable: list[list[int]] = [[], []]

    for component_id, component in enumerate(components):
        for half in (0, 1):
            points = component & halves[half]
            outer = (half - 2) % 2
            returns = (
                public.compose(phi_2[outer], phi_2[0]),
                public.compose(phi_2[outer], phi_2[1]),
            )
            raw_cells = public.orbit_partition(points, returns)
            cells = tuple(
                sorted((frozenset(cell) for cell in raw_cells), key=min)
            )
            for local, cell in enumerate(cells):
                origin = min(cell)
                state = origin
                state_by_q = []
                for _q in range(MODULUS):
                    state_by_q.append(state)
                    state = gauge_generators[half][state]
                if state != origin or frozenset(state_by_q) != cell:
                    raise ValueError("coherent level-2 gauge does not orient a cell")

                cell_id = len(pentagons_mutable)
                pentagon = Pentagon(
                    id=cell_id,
                    component=component_id,
                    half=half,
                    local=local,
                    states=tuple(sorted(cell)),
                    state_by_q=tuple(state_by_q),
                )
                pentagons_mutable.append(pentagon)
                cell_lookup[(component_id, half, local)] = cell_id
                cells_by_half_mutable[half].append(cell_id)
                for q, cell_state in enumerate(pentagon.state_by_q):
                    if cell_of_state[cell_state] != -1:
                        raise ValueError("canonical pentagons overlap")
                    cell_of_state[cell_state] = cell_id
                    q_of_state[cell_state] = q

    pentagons = tuple(pentagons_mutable)
    actions_mutable: list[list[CellAction]] = [[], []]
    for epsilon in (0, 1):
        for source in pentagons:
            target_ids = {
                cell_of_state[letters[epsilon][state]] for state in source.states
            }
            if len(target_ids) != 1 or -1 in target_ids:
                raise ValueError("one-tick image is not one canonical pentagon")
            target = pentagons[next(iter(target_ids))]
            multiplier, offset = _affine_rule(letters[epsilon], source, target)
            actions_mutable[epsilon].append(
                CellAction(
                    epsilon=epsilon,
                    source_cell=source.id,
                    target_cell=target.id,
                    component=source.component,
                    source_half=source.half,
                    target_half=target.half,
                    source_local=source.local,
                    target_local=target.local,
                    multiplier=multiplier,
                    offset=offset,
                )
            )

    singlets = [
        component_id
        for component_id, component in enumerate(components)
        if len(component) == 10
    ]
    if len(singlets) != 1:
        raise ValueError("the recurrent census has no unique singlet")

    return LivingKernel(
        letters=letters,
        support=support,
        components=components,
        halves=halves,
        pentagons=pentagons,
        cells_by_half=(
            tuple(cells_by_half_mutable[0]),
            tuple(cells_by_half_mutable[1]),
        ),
        singlet_component=singlets[0],
        component_of_state=tuple(component_of_state),
        half_of_state=tuple(half_of_state),
        cell_of_state=tuple(cell_of_state),
        q_of_state=tuple(q_of_state),
        cell_lookup=MappingProxyType(cell_lookup),
        actions=(tuple(actions_mutable[0]), tuple(actions_mutable[1])),
    )


def self_checks(model: LivingKernel | None = None) -> tuple[CheckResult, ...]:
    """Check the decomposition against every merged finite mirror fact."""

    if model is None:
        model = reconstruct()
    checks: list[CheckResult] = []

    def record(name: str, passed: bool, detail: str) -> None:
        checks.append(CheckResult(name=name, passed=bool(passed), detail=detail))

    component_sizes = Counter(map(len, model.components))
    core_ok = (
        len(model.support) == 6250
        and len(model.components) == 313
        and component_sizes == Counter({20: 312, 10: 1})
        and tuple(map(len, model.halves)) == (3125, 3125)
        and model.halves[0].isdisjoint(model.halves[1])
        and all(
            model.component_of_state[model.letters[epsilon][state]]
            == component_id
            for component_id, component in enumerate(model.components)
            for epsilon in (0, 1)
            for state in component
        )
    )
    record(
        "M01 CORE",
        core_ok,
        "6250 states; 312x20 + 1x10 components; halves 3125 + 3125",
    )

    fixed_states = tuple(
        tuple(
            state
            for state in sorted(model.halves[epsilon])
            if model.letters[epsilon][state] == state
        )
        for epsilon in (0, 1)
    )
    mirror_ok = (
        _cycle_type(model.letters[0], model.halves[0])
        == Counter({2: 1562, 1: 1})
        and _cycle_type(model.letters[1], model.halves[1])
        == Counter({2: 1562, 1: 1})
        and fixed_states == ((10366,), (11616,))
        and all(
            model.component_of_state[fixed[0]] == model.singlet_component
            for fixed in fixed_states
        )
    )
    record(
        "M02 MIRROR",
        mirror_ok,
        "own-half type {1:1,2:1562}; fixed witnesses 10366 and 11616",
    )

    alternation_ok = all(
        model.letters[1][model.letters[0][state]] == state
        for state in model.halves[1]
    ) and all(
        model.letters[0][model.letters[1][state]] == state
        for state in model.halves[0]
    )
    record(
        "M03 ALTERNATION",
        alternation_ok,
        "F1 o F0 = id on H1; F0 o F1 = id on H0",
    )

    expected_component_cells = all(
        len(model.component_cells(component_id, half))
        == (1 if len(component) == 10 else 2)
        for component_id, component in enumerate(model.components)
        for half in (0, 1)
    )
    pentagon_ok = (
        len(model.pentagons) == 1250
        and tuple(map(len, model.cells_by_half)) == (625, 625)
        and all(len(cell.states) == 5 for cell in model.pentagons)
        and all(cell.origin == min(cell.states) for cell in model.pentagons)
        and frozenset(
            state for cell in model.pentagons for state in cell.states
        )
        == model.support
        and expected_component_cells
    )
    record(
        "B04 PENTAGONS",
        pentagon_ok,
        "canonical level-2 partition: 625 five-cells in each half",
    )

    quotient_maps = tuple(
        tuple(action.target_cell for action in model.actions[epsilon])
        for epsilon in (0, 1)
    )
    swap_ok = True
    for epsilon in (0, 1):
        swap_ok = swap_ok and (
            _cycle_type(quotient_maps[epsilon], model.cells_by_half[epsilon])
            == Counter({2: 312, 1: 1})
        )
        for cell_id in model.cells_by_half[epsilon]:
            source = model.pentagons[cell_id]
            target = model.pentagons[quotient_maps[epsilon][cell_id]]
            swap_ok = swap_ok and source.component == target.component
            swap_ok = swap_ok and (
                target.id == source.id
                if source.component == model.singlet_component
                else target.id != source.id
            )
    record(
        "M04 SWAP",
        swap_ok,
        "own-half cell type {1:1,2:312}; singlet fixed, other pairs swapped",
    )

    address_ok = (
        all(model.cell_of_state[state] >= 0 for state in model.support)
        and all(model.q_of_state[state] in range(MODULUS) for state in model.support)
        and all(
            model.decode_address(model.encode_state(state)) == state
            for state in model.support
        )
        and all(
            model.tick_state(epsilon, state) == model.letters[epsilon][state]
            for epsilon in (0, 1)
            for state in model.support
        )
    )
    record(
        "R01 ADDRESS",
        address_ok,
        "address roundtrip and decomposed one-tick action agree on 2x6250 states",
    )

    affine_orders: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    reflection_ok = True
    for source in model.pentagons:
        pair = tuple(
            (
                model.actions[epsilon][source.id].multiplier,
                model.actions[epsilon][source.id].offset,
            )
            for epsilon in (0, 1)
        )
        affine_orders[pair] += 1
        for epsilon in (0, 1):
            action = model.actions[epsilon][source.id]
            reflection_ok = reflection_ok and (
                action.component == source.component
                and action.target_half == epsilon
                and action.multiplier == 4
            )
    expected_orders = Counter(
        {
            ((4, 0), (4, 2)): 625,
            ((4, 2), (4, 0)): 625,
        }
    )
    reflection_ok = reflection_ok and affine_orders == expected_orders
    record(
        "M05 REFLECTION",
        reflection_ok,
        "q -> -q+b; ordered offsets (0,2) and (2,0), 625 cells each",
    )

    consistency_ok = True
    for half in (0, 1):
        for cell in model.cells_by_half[half]:
            consistency_ok = consistency_ok and (
                quotient_maps[0][quotient_maps[1][cell]]
                == quotient_maps[0][quotient_maps[0][cell]]
                and quotient_maps[1][quotient_maps[0][cell]]
                == quotient_maps[1][quotient_maps[1][cell]]
            )
    record(
        "M06 CONSISTENCY",
        consistency_ok,
        "both mixed cell compositions equal their same-letter counterparts",
    )

    return tuple(checks)


def main() -> int:
    model = reconstruct()
    checks = self_checks(model)
    print("ENTROPY-SELECTION living-kernel reconstruction")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print("definitions: merged public P-ENTROPY-MIRROR-1 (entry point not run)")
    print()
    print(
        "carrier states=%d components=%d cells=%d"
        % (len(model.support), len(model.components), len(model.pentagons))
    )
    print(
        "singlet component=%d minimum-state=%d"
        % (
            model.singlet_component,
            min(model.components[model.singlet_component]),
        )
    )
    print()
    for check in checks:
        print(("PASS" if check.passed else "FAIL") + " " + check.name)
        print("  " + check.detail)
    passed = sum(check.passed for check in checks)
    print()
    print(
        "RECON CHECKS %d/%d %s"
        % (passed, len(checks), "ALL PASS" if passed == len(checks) else "FAIL")
    )
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
