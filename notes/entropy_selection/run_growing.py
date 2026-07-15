#!/usr/bin/env python3
"""Run the bounded NON-CANONICAL growing-context entropy recon."""

from __future__ import annotations

try:
    from .collars import CollarSpec
    from .growing import (
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        format_horizon_report,
    )
    from .measure import audit
except ImportError:  # Direct execution from this directory.
    from collars import CollarSpec  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        format_horizon_report,
    )
    from measure import audit  # type: ignore[no-redef]


def main() -> int:
    print("ENTROPY-SELECTION growing-context recon")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print("Exact cylinder weights; joint two-child incidence; no periodic closure.")
    print()

    measure = audit(20)
    print("EXACT THUE--MORSE CONTEXT DATA")
    print("  closure/frequency audit through length 20: %s" % measure.passed)
    print("  complexities=%s" % (measure.complexities,))
    print("  maximum denominators=%s" % (measure.maximum_denominators,))
    print()

    solver = GrowingContextSolver()
    pair = CollarSpec(1, 0)
    print("WEIGHTED LEXICOGRAPHIC REGRESSION")
    for level in range(2, 7):
        lower = solver.lexicographic_family(level, pair)
        upper = solver.lexicographic_family(level + 1, pair)
        report = solver.refinement_report(upper, lower)
        print("  D_%d=%s" % (level, report.distance))
    print()

    print("ANCHORED HORIZON 2..5 / FOUR DETERMINISTIC INITIALIZATIONS")
    print("  level 2 remains fixed in every run")
    candidates = []
    for seed in ("lexicographic", "tree"):
        for phase in (0, 1):
            optimizer = FiniteHorizonOptimizer(
                2,
                5,
                solver=solver,
                seed=seed,
                lift_phase=phase,
            )
            report = optimizer.optimize(10)
            candidates.append((report.final_objective, seed, phase, report))
            print(
                "  seed=%s child=%d initial=%s final=%s"
                % (
                    seed,
                    phase,
                    report.initial_objective,
                    report.final_objective,
                )
            )
    candidates.sort(key=lambda item: (item[0], item[1], item[2]))
    _, best_seed, best_phase, best = candidates[0]
    print("  best bounded initialization: seed=%s child=%d" % (best_seed, best_phase))
    print(format_horizon_report(best))
    free_best = FiniteHorizonOptimizer(
        2,
        5,
        solver=solver,
        seed=best_seed,
        lift_phase=best_phase,
        freeze_minimum=False,
    ).optimize(10)
    print(
        "  all-levels-free sensitivity from the same seed: %s"
        % free_best.final_objective
    )
    print()

    print("EXTENDED ANCHORED COORDINATE-OPTIMUM READOUT 2..8")
    extended = FiniteHorizonOptimizer(
        2,
        8,
        solver=solver,
        seed="tree",
        lift_phase=1,
    ).optimize(20)
    print(format_horizon_report(extended))
    free_extended = FiniteHorizonOptimizer(
        2,
        8,
        solver=solver,
        seed="tree",
        lift_phase=1,
        freeze_minimum=False,
    ).optimize(20)
    print(
        "  all-levels-free sensitivity from the same seed: %s"
        % free_extended.final_objective
    )
    print()
    print("INTERPRETATION")
    print("  Coordinate sweeps are exact for each fixed-neighbor update, but the")
    print("  objective is nonconvex. Anchored points are conditional on level 2;")
    print("  the all-levels-free readouts are coordinate-local diagnostics only.")
    print("  Some individual child-branch terms vanish, but every printed total")
    print("  adjacent distance remains positive and no tail decay is visible;")
    print("  no summable Cauchy tail or measurable selector is established.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
