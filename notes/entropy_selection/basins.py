"""Context-dependent seeds for one fixed growing-context boundary problem.

NON-CANONICAL LOCAL ANALYSIS.  Primary grid runs keep one exact frozen tree
family at the minimum level and diversify only free levels.  Relative orbit
signatures below concern explicit block assignments, not the full cocycle
centralizer.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from typing import Iterable

try:
    from .collars import CollarSpec, collar_graph
    from .growing import (
        BLOCK_COUNT,
        BoundaryFamily,
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        HorizonReport,
        StructuredMap,
        default_collar,
    )
    from .measure import cylinder_frequency
except ImportError:  # Direct execution from this directory.
    from collars import CollarSpec, collar_graph  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        BLOCK_COUNT,
        BoundaryFamily,
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        HorizonReport,
        StructuredMap,
        default_collar,
    )
    from measure import cylinder_frequency  # type: ignore[no-redef]


MODULUS = 5
CELL_SHIFT_UNIT = BLOCK_COUNT // MODULUS
MAXIMUM_CASES = 16
MAXIMUM_SWEEPS = 50
MAXIMUM_HORIZON_SPAN = 8
CycleSignature = tuple[tuple[int, int], ...]


@dataclass(frozen=True, order=True, slots=True)
class SeedSpec:
    """One row of a four-row context/level Latin seed pattern."""

    name: str
    phase_index: int

    def __post_init__(self) -> None:
        if not self.name or any(character.isspace() for character in self.name):
            raise ValueError("a seed name must be non-empty and whitespace-free")
        if not 0 <= self.phase_index < MODULUS - 1:
            raise ValueError("a seed phase index must lie in {0,1,2,3}")


DEFAULT_SEEDS: tuple[SeedSpec, ...] = tuple(
    SeedSpec("context%d" % index, index) for index in range(MODULUS - 1)
)


@dataclass(frozen=True, slots=True)
class RelativeContextOrbit:
    level: int
    spec: CollarSpec
    contexts: int
    distinct_block_permutations: int
    global_block_relabeling: bool
    cycle_signatures: tuple[CycleSignature, ...]
    signature: str


@dataclass(frozen=True, slots=True)
class SeedAudit:
    names: tuple[str, ...]
    valid_families: bool
    reproducible: bool
    signatures_unique: bool
    context_orbits_unique: bool
    no_global_block_relabeling: bool
    minimum_pairwise_distance: Fraction
    minimum_reference_distance: Fraction
    pairwise_distances: tuple[tuple[str, str, Fraction], ...]

    @property
    def passed(self) -> bool:
        return (
            self.valid_families
            and self.reproducible
            and self.signatures_unique
            and self.context_orbits_unique
            and self.no_global_block_relabeling
            and self.minimum_pairwise_distance == 1
            and self.minimum_reference_distance == 1
        )


@dataclass(frozen=True, slots=True)
class SeedInitialization:
    seed: str
    lift_phase: int
    anchor_signature: str
    free_signature: str
    baseline_distance: Fraction
    relative_orbits: tuple[RelativeContextOrbit, ...]


@dataclass(frozen=True, slots=True)
class BasinRun:
    seed: str
    lift_phase: int
    anchor_signature: str
    initial_free_signature: str
    context_orbit_signature: str
    initial_objective: Fraction
    final_objective: Fraction
    sweeps: int
    total_updates: int
    final_signature: str
    final_free_signature: str
    diagnostic_signature: str
    report: HorizonReport


@dataclass(frozen=True, slots=True)
class BasinReport:
    minimum_level: int
    maximum_level: int
    maximum_sweeps: int
    boundary_problem_signature: str
    runs: tuple[BasinRun, ...]
    distinct_initial_free_signatures: int
    distinct_context_orbit_signatures: int
    distinct_final_signatures: int
    distinct_final_free_signatures: int
    distinct_diagnostic_signatures: int
    distinct_objectives: int
    best_objective: Fraction


def permutation_cycle_signature(permutation: Iterable[int]) -> CycleSignature:
    """Return the exact cycle census of a finite permutation."""

    values = tuple(permutation)
    if set(values) != set(range(len(values))):
        raise ValueError("cycle signatures require a permutation of range(n)")
    seen: set[int] = set()
    lengths: Counter[int] = Counter()
    for start in range(len(values)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = values[current]
        lengths[length] += 1
    return tuple(sorted(lengths.items()))


def _seed_phase(
    seed: SeedSpec,
    level: int,
    context_rank: int,
    word: tuple[int, ...],
) -> int:
    """Return a nonzero F_5 phase, Latin across the four default seeds."""

    parity = (level + context_rank + sum(word)) & 1
    orientation = 1 if parity == 0 else 3
    context_term = (
        context_rank
        + 2 * level
        + sum((index + 1) * bit for index, bit in enumerate(word))
    ) % (MODULUS - 1)
    return 1 + (orientation * seed.phase_index + context_term) % (MODULUS - 1)


def _diversify_map(mapping: StructuredMap, phase: int) -> StructuredMap:
    if not 1 <= phase < MODULUS:
        raise ValueError("a diversification phase must be nonzero in F_5")
    shift = CELL_SHIFT_UNIT * phase
    cells = tuple(
        mapping.cells[(block + shift) % BLOCK_COUNT]
        for block in range(BLOCK_COUNT)
    )
    permutations = tuple(
        tuple((target + phase) % MODULUS for target in source_permutation)
        for source_permutation in (
            mapping.permutations[(block + shift) % BLOCK_COUNT]
            for block in range(BLOCK_COUNT)
        )
    )
    return StructuredMap(mapping.half, cells, permutations)


def diversify_family(reference: BoundaryFamily, seed: SeedSpec) -> BoundaryFamily:
    """Apply different 125-step rotations at different free contexts."""

    graph = collar_graph(reference.spec)
    if len(reference.maps) != len(graph.vertices):
        raise ValueError("the reference family has the wrong context census")
    maps = tuple(
        _diversify_map(
            mapping,
            _seed_phase(seed, reference.level, rank, word),
        )
        for rank, (word, mapping) in enumerate(
            zip(graph.vertices, reference.maps, strict=True)
        )
    )
    return BoundaryFamily(
        level=reference.level,
        spec=reference.spec,
        maps=maps,
        origin="context-basin:%s" % seed.name,
    )


def family_signature(family: BoundaryFamily) -> str:
    """Stable exact digest of every map in one boundary family."""

    payload = (
        family.level,
        family.spec.left,
        family.spec.right,
        tuple(
            (mapping.half, mapping.cells, mapping.permutations)
            for mapping in family.maps
        ),
    )
    return sha256(repr(payload).encode("ascii")).hexdigest()


def family_distance(left: BoundaryFamily, right: BoundaryFamily) -> Fraction:
    """Invariant-measure Hamming distance between two context families."""

    if left.level != right.level or left.spec != right.spec:
        raise ValueError("family distances require one level and collar spec")
    graph = collar_graph(left.spec)
    if len(left.maps) != len(graph.vertices) or len(right.maps) != len(graph.vertices):
        raise ValueError("a boundary family has the wrong context census")
    return sum(
        (
            cylinder_frequency(word) * left_map.distance(right_map)
            for word, left_map, right_map in zip(
                graph.vertices, left.maps, right.maps, strict=True
            )
        ),
        Fraction(0),
    )


def relative_block_permutations(
    reference: BoundaryFamily,
    candidate: BoundaryFamily,
) -> tuple[tuple[int, ...], ...]:
    """Resolve candidate assignments as source-block relabelings of reference."""

    if reference.level != candidate.level or reference.spec != candidate.spec:
        raise ValueError("relative permutations require matching families")
    if len(reference.maps) != len(candidate.maps):
        raise ValueError("relative families have different context censuses")
    result = []
    for reference_map, candidate_map in zip(
        reference.maps, candidate.maps, strict=True
    ):
        if reference_map.half != candidate_map.half:
            raise ValueError("relative families target different living halves")
        inverse = {
            cell: block for block, cell in enumerate(reference_map.cells)
        }
        try:
            permutation = tuple(inverse[cell] for cell in candidate_map.cells)
        except KeyError as exc:
            raise ValueError("relative families use different target cells") from exc
        if set(permutation) != set(range(BLOCK_COUNT)):
            raise AssertionError("relative cell assignments are not a permutation")
        result.append(permutation)
    return tuple(result)


def global_block_relabeling(
    reference: BoundaryFamily,
    candidate: BoundaryFamily,
) -> tuple[int, ...] | None:
    """Return one common block permutation, or None if context dependence is real."""

    permutations = relative_block_permutations(reference, candidate)
    if not permutations:
        return None
    common = permutations[0]
    return common if all(item == common for item in permutations) else None


def relative_context_orbit(
    reference: BoundaryFamily,
    candidate: BoundaryFamily,
) -> RelativeContextOrbit:
    """Exact context-indexed orbit signature relative to one reference family."""

    permutations = relative_block_permutations(reference, candidate)
    cycles = tuple(permutation_cycle_signature(item) for item in permutations)
    return RelativeContextOrbit(
        level=reference.level,
        spec=reference.spec,
        contexts=len(permutations),
        distinct_block_permutations=len(set(permutations)),
        global_block_relabeling=global_block_relabeling(reference, candidate)
        is not None,
        cycle_signatures=cycles,
        signature=sha256(repr(permutations).encode("ascii")).hexdigest(),
    )


def audit_seeds(
    solver: GrowingContextSolver,
    level: int,
    spec: CollarSpec,
    seeds: Iterable[SeedSpec] = DEFAULT_SEEDS,
    reference: BoundaryFamily | None = None,
) -> SeedAudit:
    """Audit free-family separation relative to one common reference."""

    catalog = tuple(seeds)
    if len(catalog) < 2 or len({seed.name for seed in catalog}) != len(catalog):
        raise ValueError("a basin audit needs at least two uniquely named seeds")
    common = reference if reference is not None else solver.tree_family(level, spec)
    if common.level != level or common.spec != spec:
        raise ValueError("the common reference has the wrong level or collar")
    families = tuple(diversify_family(common, seed) for seed in catalog)
    repeated = tuple(diversify_family(common, seed) for seed in catalog)
    signatures = tuple(family_signature(family) for family in families)
    orbits = tuple(relative_context_orbit(common, family) for family in families)
    pairs = tuple(
        (
            catalog[left].name,
            catalog[right].name,
            family_distance(families[left], families[right]),
        )
        for left in range(len(catalog))
        for right in range(left + 1, len(catalog))
    )
    return SeedAudit(
        names=tuple(seed.name for seed in catalog),
        valid_families=all(solver.validate_family(family) for family in families),
        reproducible=families == repeated,
        signatures_unique=len(set(signatures)) == len(signatures),
        context_orbits_unique=len({item.signature for item in orbits})
        == len(orbits),
        no_global_block_relabeling=all(
            not item.global_block_relabeling for item in orbits
        ),
        minimum_pairwise_distance=min(distance for _, _, distance in pairs),
        minimum_reference_distance=min(
            family_distance(common, family) for family in families
        ),
        pairwise_distances=pairs,
    )


def _horizon_digest(families: Iterable[BoundaryFamily]) -> str:
    payload = tuple(family_signature(family) for family in families)
    return sha256(repr(payload).encode("ascii")).hexdigest()


def initialize_optimizer(
    optimizer: FiniteHorizonOptimizer,
    seed: SeedSpec,
    *,
    lift_phase: int | None = None,
    anchor: BoundaryFamily | None = None,
) -> SeedInitialization:
    """Keep one frozen tree anchor and diversify only common free-level lifts."""

    phase = optimizer.lift_phase if lift_phase is None else lift_phase
    if phase not in (0, 1):
        raise ValueError("lift phase must be 0 or 1")
    minimum = optimizer.minimum_level
    common_anchor = (
        anchor
        if anchor is not None
        else optimizer.solver.tree_family(minimum, optimizer.specs[minimum])
    )
    if common_anchor.level != minimum or common_anchor.spec != optimizer.specs[minimum]:
        raise ValueError("the anchor does not match the optimizer boundary")
    if not optimizer.solver.validate_family(common_anchor):
        raise ValueError("the declared anchor is not a valid boundary family")

    optimizer.seed = "tree+context-%s" % seed.name
    optimizer.lift_phase = phase
    optimizer.freeze_minimum = True
    optimizer.maximum_matching_component = 0
    optimizer.maps = {minimum: list(common_anchor.maps)}

    baseline = []
    for level in range(minimum + 1, optimizer.maximum_level + 1):
        maps = tuple(optimizer._child_lift(level, phase))
        family = BoundaryFamily(
            level=level,
            spec=optimizer.specs[level],
            maps=maps,
            origin="common-tree-lift",
        )
        baseline.append(family)
        optimizer.maps[level] = list(maps)

    diversified = tuple(diversify_family(family, seed) for family in baseline)
    for family in diversified:
        optimizer.maps[family.level] = list(family.maps)
    if any(
        not optimizer.solver.validate_family(optimizer.family(level))
        for level in range(minimum, optimizer.maximum_level + 1)
    ):
        raise AssertionError("the seeded optimizer contains an invalid family")
    orbits = tuple(
        relative_context_orbit(reference, candidate)
        for reference, candidate in zip(baseline, diversified, strict=True)
    )
    return SeedInitialization(
        seed=seed.name,
        lift_phase=phase,
        anchor_signature=family_signature(common_anchor),
        free_signature=_horizon_digest(diversified),
        baseline_distance=min(
            (family_distance(reference, candidate) for reference, candidate in zip(
                baseline, diversified, strict=True
            )),
            default=Fraction(0),
        ),
        relative_orbits=orbits,
    )


def optimizer_signature(optimizer: FiniteHorizonOptimizer) -> str:
    """Stable digest of every current map, including the fixed anchor."""

    return _horizon_digest(
        optimizer.family(level)
        for level in range(optimizer.minimum_level, optimizer.maximum_level + 1)
    )


def free_optimizer_signature(optimizer: FiniteHorizonOptimizer) -> str:
    """Stable digest of only the free maps above the minimum level."""

    return _horizon_digest(
        optimizer.family(level)
        for level in range(
            optimizer.minimum_level + 1, optimizer.maximum_level + 1
        )
    )


def _diagnostic_signature(report: HorizonReport) -> str:
    """Hash exact numerical readouts; this is not a physical observable."""

    payload = (
        report.final_objective,
        tuple(
            (
                item.distance,
                item.first_child_distance,
                item.second_child_distance,
                item.maximum_branch_distance,
            )
            for item in report.refinements
        ),
        tuple(
            (
                item.conditional_roof_defect,
                item.full_equation_error,
                item.zero_defect_weight,
                item.maximum_edge_defect,
            )
            for item in report.family_reports
        ),
    )
    return sha256(repr(payload).encode("ascii")).hexdigest()


def _orbit_horizon_signature(orbits: Iterable[RelativeContextOrbit]) -> str:
    payload = tuple(item.signature for item in orbits)
    return sha256(repr(payload).encode("ascii")).hexdigest()


def explore_basins(
    *,
    minimum_level: int = 2,
    maximum_level: int = 5,
    maximum_sweeps: int = 5,
    seeds: Iterable[SeedSpec] = DEFAULT_SEEDS,
    lift_phases: Iterable[int] = (0, 1),
    solver: GrowingContextSolver | None = None,
    anchor: BoundaryFamily | None = None,
) -> BasinReport:
    """Run a bounded grid for one frozen minimum-level boundary family."""

    catalog = tuple(seeds)
    phases = tuple(lift_phases)
    if not catalog or not phases:
        raise ValueError("a basin exploration needs seeds and lift phases")
    if len({seed.name for seed in catalog}) != len(catalog):
        raise ValueError("seed names must be unique")
    if any(phase not in (0, 1) for phase in phases) or len(set(phases)) != len(phases):
        raise ValueError("lift phases must be a unique subset of {0,1}")
    if len(catalog) * len(phases) > MAXIMUM_CASES:
        raise ValueError("basin exploration exceeds the declared case bound")
    if not 1 <= maximum_sweeps <= MAXIMUM_SWEEPS:
        raise ValueError("basin exploration exceeds the declared sweep bound")
    if maximum_level - minimum_level > MAXIMUM_HORIZON_SPAN:
        raise ValueError("basin exploration exceeds the declared horizon bound")

    shared_solver = solver if solver is not None else GrowingContextSolver()
    common_anchor = (
        anchor
        if anchor is not None
        else shared_solver.tree_family(minimum_level, default_collar(minimum_level))
    )
    boundary_signature = family_signature(common_anchor)
    runs = []
    for seed in catalog:
        for phase in phases:
            optimizer = FiniteHorizonOptimizer(
                minimum_level,
                maximum_level,
                solver=shared_solver,
                seed="tree",
                lift_phase=phase,
                freeze_minimum=True,
            )
            initialized = initialize_optimizer(
                optimizer,
                seed,
                lift_phase=phase,
                anchor=common_anchor,
            )
            if initialized.anchor_signature != boundary_signature:
                raise AssertionError("a basin run changed the frozen boundary")
            initial = optimizer.objective()
            report = optimizer.optimize(maximum_sweeps)
            if (
                report.initial_objective != initial
                or report.final_objective > initial
                or not report.minimum_level_frozen
            ):
                raise AssertionError("a basin run violated its boundary problem")
            runs.append(
                BasinRun(
                    seed=seed.name,
                    lift_phase=phase,
                    anchor_signature=initialized.anchor_signature,
                    initial_free_signature=initialized.free_signature,
                    context_orbit_signature=_orbit_horizon_signature(
                        initialized.relative_orbits
                    ),
                    initial_objective=initial,
                    final_objective=report.final_objective,
                    sweeps=len(report.sweeps),
                    total_updates=sum(
                        sweep.changed_nodes for sweep in report.sweeps
                    ),
                    final_signature=optimizer_signature(optimizer),
                    final_free_signature=free_optimizer_signature(optimizer),
                    diagnostic_signature=_diagnostic_signature(report),
                    report=report,
                )
            )
    if {run.anchor_signature for run in runs} != {boundary_signature}:
        raise AssertionError("basin report mixed different boundary problems")
    return BasinReport(
        minimum_level=minimum_level,
        maximum_level=maximum_level,
        maximum_sweeps=maximum_sweeps,
        boundary_problem_signature=boundary_signature,
        runs=tuple(runs),
        distinct_initial_free_signatures=len(
            {run.initial_free_signature for run in runs}
        ),
        distinct_context_orbit_signatures=len(
            {run.context_orbit_signature for run in runs}
        ),
        distinct_final_signatures=len({run.final_signature for run in runs}),
        distinct_final_free_signatures=len(
            {run.final_free_signature for run in runs}
        ),
        distinct_diagnostic_signatures=len(
            {run.diagnostic_signature for run in runs}
        ),
        distinct_objectives=len({run.final_objective for run in runs}),
        best_objective=min(run.final_objective for run in runs),
    )


def format_basin_report(report: BasinReport) -> str:
    """Render one compact deterministic basin summary."""

    lines = [
        "initialization-grid levels=%d..%d sweeps<=%d runs=%d boundary=%s best=%s"
        % (
            report.minimum_level,
            report.maximum_level,
            report.maximum_sweeps,
            len(report.runs),
            report.boundary_problem_signature[:12],
            report.best_objective,
        ),
        "  distinct initial=%d context-orbits=%d finals=%d free-finals=%d "
        "diagnostics=%d objectives=%d"
        % (
            report.distinct_initial_free_signatures,
            report.distinct_context_orbit_signatures,
            report.distinct_final_signatures,
            report.distinct_final_free_signatures,
            report.distinct_diagnostic_signatures,
            report.distinct_objectives,
        ),
    ]
    for run in report.runs:
        lines.append(
            "  seed=%s phase=%d objective=%s -> %s sweeps=%d "
            "total-updates=%d final=%s"
            % (
                run.seed,
                run.lift_phase,
                run.initial_objective,
                run.final_objective,
                run.sweeps,
                run.total_updates,
                run.final_free_signature[:12],
            )
        )
    return "\n".join(lines)


__all__ = [
    "BasinReport",
    "BasinRun",
    "CELL_SHIFT_UNIT",
    "CycleSignature",
    "DEFAULT_SEEDS",
    "MAXIMUM_CASES",
    "MAXIMUM_HORIZON_SPAN",
    "MAXIMUM_SWEEPS",
    "RelativeContextOrbit",
    "SeedAudit",
    "SeedInitialization",
    "SeedSpec",
    "audit_seeds",
    "diversify_family",
    "explore_basins",
    "family_distance",
    "family_signature",
    "format_basin_report",
    "free_optimizer_signature",
    "global_block_relabeling",
    "initialize_optimizer",
    "optimizer_signature",
    "permutation_cycle_signature",
    "relative_block_permutations",
    "relative_context_orbit",
]
