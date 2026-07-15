#!/usr/bin/env python3
"""Run the explicit NON-CANONICAL entropy-selection recon suite."""

from __future__ import annotations

try:
    from .block_solver import ReducedBlockSolver, format_report
    from .lambda5 import (
        arithmetic_centralizer_description,
        centralizer_description,
        j_orbit_spectrum,
    )
    from .living import reconstruct, self_checks
    from .tower import LexicographicTowerBaseline, format_tower_report
except ImportError:  # Direct execution from this directory.
    from block_solver import ReducedBlockSolver, format_report  # type: ignore[no-redef]
    from lambda5 import (  # type: ignore[no-redef]
        arithmetic_centralizer_description,
        centralizer_description,
        j_orbit_spectrum,
    )
    from living import reconstruct, self_checks  # type: ignore[no-redef]
    from tower import (  # type: ignore[no-redef]
        LexicographicTowerBaseline,
        format_tower_report,
    )


def main() -> int:
    print("ENTROPY-SELECTION explicit construction and solver recon")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print("No periodic closure of a Thue--Morse supertile is used.")
    print()

    arithmetic = arithmetic_centralizer_description()
    full = centralizer_description()
    print("SOURCE-L5")
    print("  carrier=3125 additive-type=Z/25 + (Z/5)^3")
    print("  J orbit spectrum=%s" % (j_orbit_spectrum(),))
    print("  arithmetic unit centralizer order=%d" % arithmetic.order)
    print("  full permutation centralizer=%s" % (" x ".join(full.abstract_factors),))
    print()

    model = reconstruct()
    checks = self_checks(model)
    print("TARGET-LIVING")
    print("  components=%d pentagons=%d" % (len(model.components), len(model.pentagons)))
    print("  reconstruction checks=%d/%d" % (sum(check.passed for check in checks), len(checks)))
    print()

    solver = ReducedBlockSolver(model)
    print("REDUCED EXACT-CONTEXT SOLVER")
    for level in range(2, 7):
        for width in range(2, 9):
            print(format_report(solver.report(level, width)))
    print()

    approximant = LexicographicTowerBaseline(model)
    print("EXPLICIT ROKHLIN-TOWER BASELINE")
    for level in range(2, 7):
        print(format_tower_report(approximant.report(level)))
    print()
    print("INTERPRETATION")
    print("  EMPTY closes only the finite-context cell-sector ansatz tested above.")
    print("  The tower baseline is exact off roofs; its tested lexicographic")
    print("  adjacent disagreements stay macroscopic. Shrinking roofs alone do not")
    print("  prove a selector.")
    print("  Growing optimization is reported by run_growing; fixed-anchor bounds")
    print("  and separated basins by run_landscape. No summable tail is established.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
