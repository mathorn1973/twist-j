#!/usr/bin/env python3
"""Frozen operation-only sampler exercise, PREREG test 7.

PUBLIC / NON-CANONICAL. Original code: A. M. Thorn, Apache-2.0.
Exactly two sweeps per start. No equilibrium, phase or mixing conclusion.
For hot starts the seeded sampler stream first supplies uniform link values
using randrange(7), then continues with exact conditional updates.
"""

from hashlib import sha256
import json

from z7_exact import CubicLattice, ExactHeatBath, K7, stack_helicity, uniform_helicity


def digest(values):
    return sha256(bytes(values)).hexdigest()


def main():
    rows = []
    seeds = {(2, "cold"): 230701, (2, "hot"): 230702,
             (3, "cold"): 230703, (3, "hot"): 230704}
    for length in (2, 3):
        lattice = CubicLattice((length,) * 4)
        for start in ("cold", "hot"):
            seed = seeds[(length, start)]
            sampler = ExactHeatBath(lattice, seed)
            if start == "hot":
                sampler.links = [sampler.rng.randrange(7) for _ in range(lattice.n_edges)]
                sampler.flux = lattice.curl(sampler.links)
            sampler.assert_consistent()
            initial_links = digest(sampler.links)
            sweeps = []
            for sweep in (1, 2):
                sampler.sweep()
                sampler.assert_consistent()
                uniform = uniform_helicity(lattice, sampler.flux)
                stack = stack_helicity(lattice, sampler.flux)
                if K7.from_json(uniform.to_json()) != uniform or K7.from_json(stack.to_json()) != stack:
                    raise AssertionError("Reader serialization round trip")
                if sampler.counters["edge_updates"] != sweep * lattice.n_edges:
                    raise AssertionError("Wrong sweep update count")
                sweeps.append({"sweep": sweep, "links_sha256": digest(sampler.links),
                               "flux_sha256": digest(sampler.flux),
                               "uniform_all_orientations": uniform.to_json(),
                               "stack_01": stack.to_json(),
                               "principal_plane_diagnostics": lattice.principal_plane_fluxes(sampler.flux),
                               "counters": dict(sampler.counters)})
            rows.append({"L": length, "start": start, "seed": seed,
                         "initial_links_sha256": initial_links, "sweeps": sweeps})
    print(json.dumps({"candidate": "C-PHOTON-U1-FINITE-CENTER-N",
                      "status": "PASS_OPERATIONS_ONLY", "phase_decision_weight": 0,
                      "runs": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
