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
    from .coupled_exact import (
        build_exact_coupled_certificate,
        format_exact_report,
    )
    from .growing import FiniteHorizonOptimizer, GrowingContextSolver
    from .path_bounds import (
        build_catalog_dual,
        build_path_certificate,
        format_path_report,
    )
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
    from coupled_exact import (  # type: ignore[no-redef]
        build_exact_coupled_certificate,
        format_exact_report,
    )
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
    )
    from path_bounds import (  # type: ignore[no-redef]
        build_catalog_dual,
        build_path_certificate,
        format_path_report,
    )


def main() -> int:
    print("ENTROPY-SELECTION certified bounds and basin landscape")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print()

    expected_bounds = {
        4: Fraction(157, 1875),
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

    path_certificate = build_path_certificate()
    path_dual = build_catalog_dual()
    if path_certificate.lower_bound != Fraction(417, 1250):
        raise AssertionError("anchor-to-anchor lower-bound regression changed")
    if path_dual.bound != path_certificate.lower_bound:
        raise AssertionError("anchor-to-anchor catalog primal/dual gap changed")
    print("STRONGER HORIZON 2..4 ANCHOR-TO-ANCHOR BOUND")
    print(format_path_report(path_certificate, path_dual))
    print(
        "  old coordinate-local reference=%s difference=%s"
        % (
            reports[4].incumbent,
            reports[4].incumbent - path_certificate.lower_bound,
        )
    )
    print()

    exact_coupled = build_exact_coupled_certificate()
    if exact_coupled.optimum != Fraction(417, 1250):
        raise AssertionError("exact coupled 2..4 optimum regression changed")
    print("EXACT COUPLED HORIZON 2..4 CLOSURE")
    print(format_exact_report(exact_coupled))
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
    reference = reports[5].incumbent
    print("  coordinate-sweep reference=%s" % reference)
    print(
        "  distant grid improves reference=%s"
        % (basins.best_objective < reference)
    )
    print()
    print("INTERPRETATION")
    print("  The lower bounds are global only inside the fixed-r2 structured")
    print("  finite-horizon scope. At 2..4, its block relaxation lower bound and")
    print("  a coupled feasible witness coincide at 417/1250, closing that named")
    print("  problem exactly. The 2..5 bound remains below its feasible reference.")
    print("  Eight separated initializations give eight terminal diagnostics; none")
    print("  improves that reference and every 2..5 adjacent distance stays positive.")
    print("  Levels beyond 5 remain tested only in the reference 2..8 run, so this")
    print("  grid carries no asymptotic or Cauchy conclusion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
