# Prospective neutral-sum audit, 24 September 2026

**PUBLIC, NON-CANONICAL.** Working item C-PHOTON-BCHI-DIRECT-BOUND-N,
issue #1143. Author: A. M. Thorn. Apache-2.0.
Basis: Public Canon v91; public main
`b5b0792971b6841c8b7e61f95afaaabcec4ce082`, after PR #1159.

## Claim and unchanged mathematical carrier

Keep the full even-periodic four-dimensional surface ensemble
`mu_L(n) proportional to 2^(-|supp n|) 1{partial n=0 mod5}`,
ternary plaquettes, `j=partial n/5`, all unspecified exterior charged sectors,
the existing midpoint phases and original joint ordered limit profiles.
The protocol layer is mathematics within the already selected L6 measure;
there is no new physical lift. No prior finite result is reused as a run
of this audit. Earlier geometry is an explicitly disclosed input.

The written all-volume derivations are in `NEUTRAL-SUM.md`:

1. Exact deletion for a standalone closed restriction, without an empty
   halo; complete one-copy aligned-tube partition and signed current sum.
   The complete endpoint partition includes all neutral states of its five
   degree-two components; degree-five edges are not monochromatic by fiat.
2. Exponential absolute background bound `2^-25(5/16384)^D`, and a geometric
   union bound for explicitly generated comb events at fixed endpoint
   edges: `(1/553728)(3375/4096)^R`, R>=3. The complete coherent cube-boundary
   pattern estimates have their separately stated scope.
3. Conditional variance on edge-separated 21-face insertions, with density
   1/36 and no empty halo, giving `b>=25/(36*2^41)` and simultaneously
   `chi>=1/(36*2^41)` on every admitted ordered profile.

These are not a covering of full current covariance. The new transverse
floor alone cannot give the strict P1 gap. The success condition is exact
agreement of the finite audits below with the frozen written derivations,
not a phase verdict. P1 closure still requires an actual evaluated positive
margin over the complete original profile family. No q_min substitution,
finite-volume extrapolation, fitted constant or changed action is allowed.

## Code, inputs and custody

Before the first scientific execution, publicly commit and read back this
preregistration, the complete proof, `verify_neutral_sum.py`, and the updated
README. Record their SHA-256, byte counts and immutable commit in issue #1143.
The only repository code imported by the verifier is the unchanged helper:

    verify_connected_current.py
    bytes: 13159
    SHA256: ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403

The verifier uses Python's standard library, integer arithmetic and
`fractions.Fraction`; there is no floating-point scientific assertion,
random seed, simulation, external data, target measurement or hidden input.
Its geometry derives from #1159, including the disclosed aligned bridge,
but the new standalone endpoint and full-sum audit has not been executed.
Only static source parsing and analytical review precede the pin.

## Frozen execution

Run once, from the pinned note directory, with the helper present:

    python3 -B verify_neutral_sum.py

Capture exact stdout and stderr as bytes, UTC start, elapsed time, exit code,
Python version, neutral operating-system and architecture descriptors.
Record stdout byte count and SHA-256 and reproduce the full small stdout in
`NEUTRAL-RUN-20260924.md`. No runtime result is accepted from a different
source or helper hash. The proof and source remain immutable after pinning.
Successful stdout must end with exactly:

    RESULT PASS; complete P1 and Canon promotion remain unproved

The exact prospective finite inventory is:

- For D=5 and 7: enumerate all 243 endpoint coefficient choices at each end
  against the actual lattice boundary; reconstruct degree-two equality
  components; exhaust all 27 local cap triples; enumerate every reduced
  one-copy state after the exact endpoint sum, and construct every state
  with both endpoint currents nonzero. Compare the full partitions, signed
  numerators and absolute numerators with the exact transfer matrices.
- For D=9,17,33: check the same geometry, endpoint sums and cap equations,
  then the exact matrix formulas and rational bounds. These are not complete
  state enumerations at those D.
- For L=4,6 and all four coordinate orientations of a 3-cube: check its
  cofaces, distinct-face uniqueness, the counts 18,15,180 and the cap-to-cap
  and endpoint-edge-to-cap midpoint-distance bounds. Check the rational
  geometric series and all displayed comb prefactors.
- For the actual aligned comb at D=5,7,9: check the complete cube face tree,
  each leaf's opposite cap, exact boundary and noncap sizes, overlap sets,
  and the uniqueness of each companion tube cube.
- For both orientations 01 and 02 and every L=4,6,8,10,12: construct the
  actual 21-face cup insertions and check their boundaries, disjoint face,
  edge and vertex sets in the prescribed packing; check counts, both
  Laurent-polynomial form factors and the exact finite-density errors.

No enumeration of the full finite-volume measure is claimed. The analytic
proofs, rather than these finitely many D or L, support the universal scope.

## Failure rules and status ceiling

Any failed assertion, nonzero exit, unexpected stderr, changed hash or
unexplained stdout difference is a failed audit or custody failure. Preserve
the first attempt and its exact result; do not silently edit and retry.
Corrections require a separately named fresh prospective pin. A finite
counterexample limits or rejects the corresponding written claim and is
not hidden by changing the claim's threshold.

The written arguments are candidate-T within their explicit domains;
one-architecture exact finite execution is candidate-C. Separate-agent
review uses shared sources, not blind external evidence. Ordinary repository
CI does not run notes audits and is not a second-architecture reproduction
of this verifier. Canon, Registry, Frontier, gates, workflows, formal probes,
phase thresholds and releases are unchanged. These results do not earn
P1 closure or a Canon fold.
