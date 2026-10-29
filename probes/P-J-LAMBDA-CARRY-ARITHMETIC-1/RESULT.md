# Result: reversible coefficient compilation passes the frozen exact audit

2026-10-29. **NON-CANONICAL. L1 conditional construction.**
Status: candidate-C for the first exact finite run; the all-N claim rests
on the accompanying analytical proof. No canonical status is assigned.

## First result

Public source pin: `58ae23f4f6fbf4ef3b9338cbd63faaf01df87b36`.
The first run completed with exit zero, empty stderr and 8354 bytes of
deterministic scientific stdout, committed as `EXPECTED.txt`.
SHA-256: `7d02438c04094fc09b0b77965d572b9655776438c3d033ae55242372a6e06bc4`.

All nine frozen falsifier groups passed. No failure condition fired and no
accepted source, threshold, test family or code changed after the pin.
The exact local environment and hashes are in `RUN.md`.

## What passed

- Both freshly rerun preceding arithmetic representations agreed exactly.
- All 250 signed H input/target cases, returned helpers and physical
  primitive inventories passed.
- All 406900 pairs for adders of widths one through four passed in both
  directions, using the generated ripple schedules. The additional 668
  fully primitive-expanded small-adder cases passed.
- Both complete carry closures, all 16490 edges, and 30 predeclared full
  coefficient steps expanded through ADD/H to elementary permutations
  agreed, including literal reverse cleanup.
- All 97655 words of lengths one through seven and all 175 fixed longer
  inputs retained the prior exact ring identities and map hashes.
- The whole generated multipliers, signed dirty-target evaluations and
  repeated archive programs returned every admitted workspace to zero.
- All 3125 length-five archives remained distinct, with exactly 120 zero
  root sums. All shorter archive hashes also remained identical.
- The emitted instruction inventories and allocated cells agreed with
  the stated formulas for every preregistered length.

## Constructive improvement

For each positive finite N, the coefficient compiler replaces the generic
row-table bound `6249713 N` by `136917 N` paired pulses per multiplication.
This is more than a 45-fold reduction of these two construction bounds,
not a measured laboratory speedup or an optimum theorem.
Local operations have bound `255187 N+32`.

Data and work occupy `14N+22` five-level cells, or `15N+22` with an N-cell
archive. The preceding construction used `7N+16`, or `8N+16` with archive.
For the complete N-letter reading the new pair bound is `136917 N^2+N`;
the full instruction bound, including initial Fourier preparation, is
`392104 N^2+36N`.

The new compiler never consults the 1649-state table. It uses four bounded
integer coefficients and fixed-width reversible adders. The audit constructs
a transition table only as a finite verification cache. The all-N result
uses the proved coefficient bound and symbolic circuit construction.

## Interpretation and verification limits

The primitive matrices are checked exactly; the large circuit is verified
compositionally through exhaustive block laws and complete reachable-edge
coverage. Not every physical pulse of every large circuit is simulated.
The 1649 reachable exact carries are representation-specific, not a proved
minimum over all possible realizations.

This is still a supplied-control construction. Enlarged addressed cells,
clean preparation, program clock, routing, energy/work and protection from
physical errors remain separate assumptions or accounts. Formal archive
weights do not derive a single occurred outcome, select J among units,
realize this apparatus under native U, or provide an L1-to-L6 lift.

The original one-architecture run and any subsequent required CI replay
must be distinguished. Repository CI checks exact reproduction and integrity;
mathematical acceptance remains separately scoped. No Canon, registry,
frontier, policy, workflow, tag or release change is made.
