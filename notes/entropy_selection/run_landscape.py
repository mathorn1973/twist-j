#!/usr/bin/env python3
"""Replay certified bounds and separated fixed-anchor initializations."""

from __future__ import annotations

from fractions import Fraction

try:
    from .basins import (
        DEFAULT_SEEDS,
        audit_seeds,
        explore_basins,
        format_basin_report,
    )
    from .bounds import bound_report, format_report as format_bound_report
    from .growing import FiniteHorizonOptimizer, GrowingContextSolver
except ImportError:  # Direct execution from this directory.
    from basins import (  # type: ignore[no-redef]
        DEFAULT_SEEDS,
        audit_seeds,
        explore_basins,
        format_basin_report,
    )
    from bounds import (  # type: ignore[no-redef]
        bound_report,
        format_report as format_bound_report,
    )
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
    )


def main() -> int:
    print("ENTROPY-SELECTION certified bounds and basin landscape")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print()

    expected_bounds = {
        4: Fraction(251, 3000),
        5: Fraction(313, 2500),
    }
    print("CERTIFIED FIXED-ANCHOR LOWER BOUNDS")
    reports = {}
    for maximum_level in (4, 5):
        report = bound_report(maximum_level, "tree", 1)
        if report.certificate.lower_bound != expected_bounds[maximum_level]:
            raise AssertionError("small-horizon lower-bound regression changed")
        reports[maximum_level] = report
        print(format_bound_report(report))
    print()

    solver = GrowingContextSolver()
    reference_optimizer = FiniteHorizonOptimizer(
        2,
        3,
        solver=solver,
        seed="tree",
        lift_phase=0,
        freeze_minimum=True,
    )
    reference = reference_optimizer.family(3)
    audit = audit_seeds(
        solver,
        reference.level,
        reference.spec,
        reference=reference,
    )
    if not audit.passed:
        raise AssertionError("context-dependent basin seeds failed separation gates")
    print("CONTEXT-DEPENDENT SEED AUDIT")
    print("  seeds=%s" % (tuple(seed.name for seed in DEFAULT_SEEDS),))
    print("  pairwise distance=%s" % audit.minimum_pairwise_distance)
    print("  reference distance=%s" % audit.minimum_reference_distance)
    print("  no single global block relabeling=%s" % audit.no_global_block_relabeling)
    print()

    print("FIXED-TREE-ANCHOR INITIALIZATION GRID")
    basins = explore_basins(
        minimum_level=2,
        maximum_level=5,
        maximum_sweeps=10,
        solver=solver,
    )
    if (
        basins.best_objective != Fraction(3443, 3750)
        or basins.distinct_diagnostic_signatures != 8
        or basins.distinct_objectives != 8
        or any(
            refinement.distance <= 0
            for run in basins.runs
            for refinement in run.report.refinements
        )
    ):
        raise AssertionError("bounded basin landscape regression changed")
    print(format_basin_report(basins))
    incumbent = reports[5].incumbent
    print("  reference incumbent=%s" % incumbent)
    print("  distant grid improves incumbent=%s" % (basins.best_objective < incumbent))
    print()
    print("INTERPRETATION")
    print("  The lower bounds are global only inside the fixed-r2 structured")
    print("  finite-horizon scope; neither bound meets its feasible incumbent.")
    print("  Eight separated initializations give eight terminal diagnostics; none")
    print("  improves the incumbent and every 2..5 adjacent distance stays positive.")
    print("  Levels beyond 5 remain tested only in the reference 2..8 run, so this")
    print("  grid carries no asymptotic or Cauchy conclusion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
