"""Exact coupled optimum for the fixed-``r=2`` horizon ``2..6``.

NON-CANONICAL LOCAL ANALYSIS.  Exact ordinary- and special-block lower
bounds are matched by one structured family on all 625 source blocks.  The
zero-price block dual therefore closes the root at
``118780 / (48*3125) = 5939/7500`` without branching.

The lower calculation is a point-coordinate relaxation.  Its matching upper
witness is independently reassembled, checked to be bijective at every
boundary node, and replayed against every weighted edge and anchor.  This is
only the named frozen level-2 boundary and finite horizon.  It gives no
inverse-limit, entropy, measure, selection, or Canon authority.

Optimized Python (``-O``) is refused because the exact component audits retain
explicit assertion gates.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256

try:
    from . import horizon6_ordinary as ordinary
    from . import horizon6_prep as prep
    from .basins import family_signature
    from .bounds import (
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from .collars import collar_graph
    from .growing import (
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
    )
    from .path_bounds import (
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )
except ImportError:  # Direct execution from this directory.
    import horizon6_ordinary as ordinary  # type: ignore[no-redef]
    import horizon6_prep as prep  # type: ignore[no-redef]
    from basins import family_signature  # type: ignore[no-redef]
    from bounds import (  # type: ignore[no-redef]
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from collars import collar_graph  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
    )
    from path_bounds import (  # type: ignore[no-redef]
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )


DOMAIN = 3125
SCALE = 48
FIBER_SIZE = DOMAIN
BLOCK_COUNT = 625
ORDINARY_BLOCK_COUNT = 624
NODE_COUNT = 44
PAIR_COUNT = 76
PIN_COUNT = 12
EDGE_COUNT = PAIR_COUNT + PIN_COUNT
OBJECTIVE_SCALE = SCALE * FIBER_SIZE

EXPECTED_ORDINARY_MINIMUM = 190
EXPECTED_SPECIAL_MINIMUM = 220
EXPECTED_SCALED_OPTIMUM = 118_780
EXPECTED_OPTIMUM = Fraction(5939, 7500)
EXPECTED_TRANSITIONS = (
    Fraction(313, 1875),
    Fraction(573, 1250),
    Fraction(1249, 7500),
    Fraction(0),
)
EXPECTED_ORDINARY_BAD = (
    0, 2, 5, 6, 7, 9, 13, 14, 17, 19, 24, 26, 40, 42, 76, 77,
)
EXPECTED_SPECIAL_BAD = (
    1, 3, 6, 8, 10, 12, 13, 15, 18, 19, 21, 36, 76, 79, 80, 81,
)
COUPLED_FAMILY_SIGNATURES = (
    "c06fda5221cdcdd7859e9e3fc3ae648790b7c44d4adf18af5eaabd919b4eda02",
    "f94068a56f8d223865dddffa6e86bfaada03655aac39ccfed20b4a2f3e65cfe4",
    "6fa49220a130cb3ad251758a811a42f2c23ab5b8951f5db43b70468473f00450",
    "04f284f7ca96d4e4593cb88d55103cc368366f3995d550a2e5364b7e47530462",
    "54928d1ca558073ee99a45c6e619062637f22332964949351078400e6e14f7c5",
)
EXPECTED_COMBINED_SIGNATURE_SHA256 = (
    "6780cea7ed7cbddd332ab6ef5370df4806086abc3d5bac2a47da52b934ffce58"
)


@dataclass(frozen=True, slots=True)
class CoupledHorizon6Witness:
    families: tuple[BoundaryFamily, ...]
    family_signatures: tuple[str, ...]
    combined_signature_sha256: str
    per_block_scaled_costs: tuple[int, ...]
    transition_distances: tuple[Fraction, ...]
    objective: Fraction


@dataclass(frozen=True, slots=True)
class ExactCoupledHorizon6Certificate:
    minimum_level: int
    maximum_level: int
    seed: str
    lift_phase: int
    ordinary: ordinary.OrdinaryHorizon6Report
    special: prep.SpecialHorizon6Report
    block_minima: tuple[int, ...]
    assignment_price: Fraction
    assignment_minima: tuple[int, ...]
    scaled_lower_bound: int
    witness: CoupledHorizon6Witness
    scaled_upper_bound: int
    optimum: Fraction
    root_nodes: int
    branched_nodes: int
    fathomed_by_bound: int


def _require_assertion_gates() -> None:
    if not __debug__:
        raise RuntimeError("optimized Python disables required assertion gates")


@lru_cache(maxsize=1)
def _special_labels() -> tuple[BlockLabel, ...]:
    graph = constraint_graph(3, 6)
    solver = _solver()
    offsets = prep.EXPECTED_COORD0_ASSIGNMENT
    if len(offsets) != len(graph.nodes) or len(graph.nodes) != NODE_COUNT:
        raise AssertionError("special horizon-6 node census changed")
    labels = tuple(
        BlockLabel(
            solver.model.cells_by_half[_expected_half(node)][0],
            tuple((offsets[index] + coordinate) % 5 for coordinate in range(5)),
        )
        for index, node in enumerate(graph.nodes)
    )
    cost, bad = prep._reassembled_witness(offsets)
    if cost != EXPECTED_SPECIAL_MINIMUM or bad != EXPECTED_SPECIAL_BAD:
        raise AssertionError("special horizon-6 witness changed")
    return labels


@lru_cache(maxsize=1)
def _structured_families() -> tuple[BoundaryFamily, ...]:
    graph, ordinary_labels, node_cells = ordinary.lifted_ordinary_labels()
    reference = constraint_graph(3, 6)
    if graph != reference or len(ordinary_labels) != ORDINARY_BLOCK_COUNT:
        raise AssertionError("ordinary lifted-label graph changed")
    if len(node_cells) != NODE_COUNT or any(
        len(cells) != ORDINARY_BLOCK_COUNT for cells in node_cells
    ):
        raise AssertionError("ordinary lifted cells are not all-different")
    special_labels = _special_labels()
    maps: dict[tuple[int, tuple[int, ...]], StructuredMap] = {}
    for node_index, node in enumerate(graph.nodes):
        labels = tuple(
            ordinary_labels[block_id][node_index]
            for block_id in range(ORDINARY_BLOCK_COUNT)
        ) + (special_labels[node_index],)
        maps[node] = StructuredMap(
            half=_expected_half(node),
            cells=tuple(label.cell for label in labels),
            permutations=tuple(label.permutation for label in labels),
        )

    optimizer = FiniteHorizonOptimizer(
        2,
        6,
        solver=_solver(),
        seed="tree",
        lift_phase=1,
        freeze_minimum=True,
    )
    families = [optimizer.family(2)]
    for level in range(3, 7):
        spec = optimizer.specs[level]
        families.append(
            BoundaryFamily(
                level=level,
                spec=spec,
                maps=tuple(
                    maps[(level, word)] for word in collar_graph(spec).vertices
                ),
                origin="exact-coupled-horizon6",
            )
        )
    result = tuple(families)
    signatures = tuple(family_signature(family) for family in result)
    if signatures != COUPLED_FAMILY_SIGNATURES:
        raise AssertionError("coupled horizon-6 signatures changed")
    return result


def _maps_by_node(
    families: tuple[BoundaryFamily, ...],
) -> dict[tuple[int, tuple[int, ...]], StructuredMap]:
    return {
        (family.level, word): mapping
        for family in families[1:]
        for word, mapping in zip(
            collar_graph(family.spec).vertices, family.maps, strict=True
        )
    }


def _scaled_edge_weights() -> tuple[int, ...]:
    graph = constraint_graph(3, 6)
    result = tuple(int(edge.weight * SCALE) for edge in graph.edges) + tuple(
        prep.EXPECTED_ANCHOR_SCALED6 for _ in anchor_terminals()
    )
    if Counter(result) != Counter({1: 16, 2: 56, 4: 16}):
        raise AssertionError("horizon-6 scaled edge census changed")
    return result


def _edge_mismatch_from_maps(
    maps: dict[tuple[int, tuple[int, ...]], StructuredMap],
    block_id: int,
    edge_id: int,
) -> int:
    graph = constraint_graph(3, 6)
    if edge_id < PAIR_COUNT:
        edge = graph.edges[edge_id]
        upper = maps[edge.upper]
        lower = maps[edge.lower]
        label = BlockLabel(upper.cells[block_id], upper.permutations[block_id])
        if edge.phase:
            label = _advance_label(block_id, label, edge.lower_level, edge.letter)
        return _label_mismatches(
            label,
            BlockLabel(lower.cells[block_id], lower.permutations[block_id]),
        )
    terminal = anchor_terminals()[edge_id - PAIR_COUNT]
    parent = maps[terminal.parent]
    target = _reverse_anchor(
        terminal,
        block_id,
        _terminal_label(terminal.id, block_id),
    )
    return _label_mismatches(
        BlockLabel(parent.cells[block_id], parent.permutations[block_id]),
        target,
    )


def per_block_scaled_costs(
    families: tuple[BoundaryFamily, ...],
) -> tuple[int, ...]:
    maps = _maps_by_node(families)
    weights = _scaled_edge_weights()
    return tuple(
        sum(
            weights[edge_id]
            * _edge_mismatch_from_maps(maps, block_id, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
        for block_id in range(BLOCK_COUNT)
    )


@lru_cache(maxsize=1)
def build_coupled_witness() -> CoupledHorizon6Witness:
    _require_assertion_gates()
    solver = _solver()
    families = _structured_families()
    if any(not solver.validate_family(family) for family in families):
        raise AssertionError("coupled horizon-6 family is not bijective")
    reports = tuple(
        solver.refinement_report(families[index], families[index - 1])
        for index in range(1, 5)
    )
    costs = per_block_scaled_costs(families)
    signatures = tuple(family_signature(family) for family in families)
    witness = CoupledHorizon6Witness(
        families=families,
        family_signatures=signatures,
        combined_signature_sha256=sha256(
            "".join(signatures).encode("ascii")
        ).hexdigest(),
        per_block_scaled_costs=costs,
        transition_distances=tuple(report.distance for report in reports),
        objective=sum((report.distance for report in reports), Fraction(0)),
    )
    if not verify_coupled_witness(witness):
        raise AssertionError("new coupled horizon-6 witness failed replay")
    return witness


def verify_coupled_witness(witness: CoupledHorizon6Witness) -> bool:
    if (
        not __debug__
        or type(witness) is not CoupledHorizon6Witness
        or type(witness.families) is not tuple
        or type(witness.family_signatures) is not tuple
        or any(type(value) is not str for value in witness.family_signatures)
        or type(witness.combined_signature_sha256) is not str
        or type(witness.per_block_scaled_costs) is not tuple
        or any(type(value) is not int for value in witness.per_block_scaled_costs)
        or type(witness.transition_distances) is not tuple
        or any(type(value) is not Fraction for value in witness.transition_distances)
        or type(witness.objective) is not Fraction
        or len(witness.families) != 5
    ):
        return False
    try:
        solver = _solver()
        families_valid = all(
            type(family) is BoundaryFamily and solver.validate_family(family)
            for family in witness.families
        )
        signatures = tuple(
            family_signature(family) for family in witness.families
        )
        reports = tuple(
            solver.refinement_report(
                witness.families[index], witness.families[index - 1]
            )
            for index in range(1, 5)
        )
        costs = per_block_scaled_costs(witness.families)
        maps = _maps_by_node(witness.families)
        weights = _scaled_edge_weights()
        ordinary_mismatches = tuple(
            _edge_mismatch_from_maps(maps, 0, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
        special_mismatches = tuple(
            _edge_mismatch_from_maps(maps, SPECIAL_BLOCK, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
    except (
        AssertionError,
        AttributeError,
        IndexError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return False
    ordinary_bad = tuple(
        edge_id for edge_id, value in enumerate(ordinary_mismatches) if value
    )
    special_bad = tuple(
        edge_id for edge_id, value in enumerate(special_mismatches) if value
    )
    transition_distances = tuple(report.distance for report in reports)
    return (
        families_valid
        and signatures == witness.family_signatures == COUPLED_FAMILY_SIGNATURES
        and sha256("".join(signatures).encode("ascii")).hexdigest()
        == witness.combined_signature_sha256
        == EXPECTED_COMBINED_SIGNATURE_SHA256
        and costs == witness.per_block_scaled_costs
        == (EXPECTED_ORDINARY_MINIMUM,) * ORDINARY_BLOCK_COUNT
        + (EXPECTED_SPECIAL_MINIMUM,)
        and transition_distances
        == witness.transition_distances
        == EXPECTED_TRANSITIONS
        and witness.objective
        == sum(transition_distances, Fraction(0))
        == EXPECTED_OPTIMUM
        and sum(costs) == OBJECTIVE_SCALE * witness.objective
        == EXPECTED_SCALED_OPTIMUM
        and ordinary_bad == EXPECTED_ORDINARY_BAD
        and special_bad == EXPECTED_SPECIAL_BAD
        and all(ordinary_mismatches[index] == 5 for index in ordinary_bad)
        and all(special_mismatches[index] == 5 for index in special_bad)
        and sum(weights[index] * 5 for index in ordinary_bad)
        == EXPECTED_ORDINARY_MINIMUM
        and sum(weights[index] * 5 for index in special_bad)
        == EXPECTED_SPECIAL_MINIMUM
    )


@lru_cache(maxsize=1)
def build_exact_coupled_horizon6() -> ExactCoupledHorizon6Certificate:
    _require_assertion_gates()
    ordinary_report = ordinary.build_ordinary_horizon6()
    special_report = prep.build_special_horizon6()
    block_minima = (ordinary_report.optimum,) * ORDINARY_BLOCK_COUNT + (
        special_report.reassembled_cost,
    )
    witness = build_coupled_witness()
    scaled = sum(block_minima)
    certificate = ExactCoupledHorizon6Certificate(
        minimum_level=2,
        maximum_level=6,
        seed="tree",
        lift_phase=1,
        ordinary=ordinary_report,
        special=special_report,
        block_minima=block_minima,
        assignment_price=Fraction(0),
        assignment_minima=(0,) * NODE_COUNT,
        scaled_lower_bound=scaled,
        witness=witness,
        scaled_upper_bound=sum(witness.per_block_scaled_costs),
        optimum=Fraction(scaled, OBJECTIVE_SCALE),
        root_nodes=1,
        branched_nodes=0,
        fathomed_by_bound=1,
    )
    if not verify_exact_coupled_horizon6(certificate):
        raise AssertionError("new coupled horizon-6 certificate failed replay")
    return certificate


def verify_exact_coupled_horizon6(
    certificate: ExactCoupledHorizon6Certificate,
) -> bool:
    if (
        not __debug__
        or type(certificate) is not ExactCoupledHorizon6Certificate
        or type(certificate.minimum_level) is not int
        or type(certificate.maximum_level) is not int
        or type(certificate.seed) is not str
        or type(certificate.lift_phase) is not int
        or type(certificate.block_minima) is not tuple
        or any(type(value) is not int for value in certificate.block_minima)
        or type(certificate.assignment_price) is not Fraction
        or type(certificate.assignment_minima) is not tuple
        or any(type(value) is not int for value in certificate.assignment_minima)
        or type(certificate.scaled_lower_bound) is not int
        or type(certificate.scaled_upper_bound) is not int
        or type(certificate.optimum) is not Fraction
        or any(
            type(value) is not int
            for value in (
                certificate.root_nodes,
                certificate.branched_nodes,
                certificate.fathomed_by_bound,
            )
        )
    ):
        return False
    try:
        ordinary_valid = ordinary.verify_ordinary_horizon6(certificate.ordinary)
        special_valid = prep.verify_special_horizon6(certificate.special)
        witness_valid = verify_coupled_witness(certificate.witness)
    except (
        AssertionError,
        AttributeError,
        IndexError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return False
    expected_blocks = (
        (EXPECTED_ORDINARY_MINIMUM,) * ORDINARY_BLOCK_COUNT
        + (EXPECTED_SPECIAL_MINIMUM,)
    )
    return (
        (certificate.minimum_level, certificate.maximum_level) == (2, 6)
        and certificate.seed == "tree"
        and certificate.lift_phase == 1
        and ordinary_valid
        and special_valid
        and certificate.ordinary.optimum == EXPECTED_ORDINARY_MINIMUM
        and certificate.special.reassembled_cost == EXPECTED_SPECIAL_MINIMUM
        and certificate.block_minima == expected_blocks
        and certificate.assignment_price == 0
        and certificate.assignment_minima == (0,) * NODE_COUNT
        and certificate.scaled_lower_bound
        == sum(certificate.assignment_minima) + sum(certificate.block_minima)
        == EXPECTED_SCALED_OPTIMUM
        and witness_valid
        and certificate.witness.per_block_scaled_costs
        == certificate.block_minima
        and certificate.scaled_upper_bound
        == sum(certificate.witness.per_block_scaled_costs)
        == certificate.scaled_lower_bound
        and certificate.optimum
        == Fraction(certificate.scaled_lower_bound, OBJECTIVE_SCALE)
        == certificate.witness.objective
        == EXPECTED_OPTIMUM
        and (
            certificate.root_nodes,
            certificate.branched_nodes,
            certificate.fathomed_by_bound,
        )
        == (1, 0, 1)
    )


def format_exact_report(certificate: ExactCoupledHorizon6Certificate) -> str:
    if not verify_exact_coupled_horizon6(certificate):
        raise ValueError("cannot format an invalid coupled horizon-6 certificate")
    return "\n".join(
        (
            "EXACT COUPLED HORIZON 2..6",
            "  scope=fixed-r2 structured finite boundary; seed=tree; phase=1",
            "  ordinary exact block: full-domain retraction and dual replay "
            "optimum=190",
            "  special exact block: full-domain retraction and coordinate DP "
            "optimum=220",
            "  zero-price block dual: histogram={190:624,220:1} "
            "scaled=118780",
            "  coupled witness: transitions=(313/1875,573/1250,"
            "1249/7500,0)",
            "  structured replay: 625/625 block minima attained; all families "
            "bijective",
            "  lower=118780 upper=118780 root=(1,0,1)",
            "  RESULT optimum=5939/7500 "
            "[NON-CANONICAL finite-horizon only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION COUPLED EXACT CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_exact_report(build_exact_coupled_horizon6()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
