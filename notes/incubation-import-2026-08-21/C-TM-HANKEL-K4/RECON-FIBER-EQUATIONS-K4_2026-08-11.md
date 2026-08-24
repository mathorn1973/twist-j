# RECON fiber equations and the discrete obstruction, k4, 2026-08-11

NON-CANONICAL. Two runs on the structural route, before any successor
freeze. No mask seen in earlier work was used to build anything here; the
known mask appears only as a named regression witness. Scripts
recon_fiber_equations_k4.py and recon_fiber_parity_k4.py, logs recon4.log
and recon5.log.

## The exact fiber equations, derived

Every parent-map vector is L_a(v) for a linear map L_a of the 65 signs,
and every parent-map coordinate is B(L_a(v), L_b(v)) for a symmetric
bilinear form B per sector: the plain inner product on the standard part,
and the character-projected forms on [22] and [211]. Writing m_j = v_j on
the flipped set and 0 elsewhere, the flip is v -> v - 2m, so

```text
B(L_a(v-2m), L_b(v-2m)) - B(L_a(v), L_b(v))
   = -2 [ B(L_a(v), L_b(m)) + B(L_a(m), L_b(v)) ] + 4 B(L_a(m), L_b(m))
```

and F_109 is preserved if and only if

```text
sum_{j in orbit} m_j = 0                        for each of the 10 orbits
B(L_a(v), L_b(m)) + B(L_a(m), L_b(v))
     = 2 B(L_a(m), L_b(m))                      for each sector, a <= b
```

10 linear conditions on m alone, and 99 conditions that are LINEAR IN THE
TABLE v for a fixed flip pattern m. Necessary and sufficient, not merely
necessary.

Audit: the predicate computed from these equations agreed with direct
F_109 comparison on 1413 of 1413 instances, weight 2 and weight 4, across
twelve bases. Exact agreement.

## Why this changes the method

For fixed m the fiber condition is an inhomogeneous linear system in the
table. Fiber pairs stop being something one finds by luck in a sampled
domain and become something one SOLVES FOR. That is the targeted attack
the owner asked for, and it also opens the only route that could ever
prove T-A rather than fail to kill it.

## Two cheap obstructions, both vacuous

```text
rational relaxation   all 252 weight-2 flip patterns leave a nonempty
                      rational solution space; free dimensions 33, 38,
                      44, 47, 49, 52. Zero patterns are killed.
parity certificate    substituting v = 1 - 2z turns each equation into
                      2 sum_j A_ij z_j = sum_j A_ij - rhs, so an odd row
                      would be unsatisfiable over the sign cube for EVERY
                      table of the whole stratum. Zero of 252 weight-2
                      patterns and zero of 29478 structurally enumerated
                      weight-4 patterns carry an odd row.
```

This confirms the owner's mechanistic hypothesis in its first half and
sharpens it. The continuous Gram freedom is enormous, the two cheapest
discrete obstructions are empty, and yet 47934 weight-2 moves in the last
candidate produced not one fiber pair. The obstruction is therefore
neither dimensional nor modulo 2; it lives in the integer sign cube
itself, deeper than either filter reaches. That is now a sharp, concrete
target rather than a feeling about thin fibers.

## What the successor must carry

The remaining question per flip pattern is exact 0/1 feasibility:

```text
2 sum_j A_ij z_j = sum_j A_ij - rhs_i,   z in {0,1}^65, z pinned on M
```

about 30 equations in 63 unknowns per weight-2 pattern. This needs a real
propagation and backtracking engine with a declared node budget, and it
admits three per-pattern outcomes that must all be reportable: FEASIBLE
with an explicit table, INFEASIBLE with an exhausted search tree (a
complete impossibility certificate over the whole stratum), and UNDECIDED
at the declared budget. UNDECIDED is a scope statement, not a STOP, and
must never be counted as either outcome.

A feasible solution is then tested for the two-profile condition and for
flow: a feasible pattern whose two endpoints lie in S_pm with opposite
flow kills T-A outright, and one whose endpoints are not two-profile is
still a structural discovery about the fiber relation.
