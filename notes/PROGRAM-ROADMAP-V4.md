# TWIST-J program roadmap after Public Canon v4

Status: **NON-CANONICAL LOCAL ANALYSIS**

Snapshot: 2026-07-15, based on public `main` at
`0b5c7c459d4c4677b7bc834b92d5e485f410f7cb`. Public Canon v4 remains pinned
by `canon-v4` at `ebc5c06f4d0bc5c0d01b931e4f26cccd72b60325`; the later main
commit merges `P-ENTROPY-MIRROR-1` but does not fold it into the registry or
Canon. This note is a planning surface. It changes no public claim, status,
dependency, gate, or Canon byte.

## Current program shape

Public Canon v4 contains 174 registered claims:

```text
T 83    D 38    C 20    H 6    O 21    F 6
live H/O: 27
```

The closed core is strongest in exact finite algebra and reproducible finite
computation. The main unresolved work is not another census. It is the
selection of canonical objects and the proof of cross-layer lifts:

- a living entropy selector and its regularity and measure law;
- a canonical curvature-operator class;
- a non-abelian color measure;
- typed decoder and metrology interfaces;
- only then the downstream phenomenological readings.

One public probe is operationally unfinished:

1. `P-CURVATURE-GAUSS-SPLIT-1` has a frozen pin and formal aarch64 evidence,
   but still needs a scoped result, current-main reconciliation, PR, and
   x86_64 closure. Its result cannot by itself close canonical-operator
   selection.

`P-ENTROPY-MIRROR-1` is publicly merged by PR #37 with a byte-identical
aarch64/x86_64 result. Its later registry/Canon promotion remains a separate
fold. Local recon may use the merged finite result, but must preserve its
scope ceiling.

## Prioritization rule

Order work by four questions:

1. Is the input object already public and typed?
2. Is there an exact falsifier or a finite classification target?
3. Does the result remove a dependency for several later claims?
4. Can the work begin as local recon without changing a public threshold?

This favors selection and classification problems over premature numerical
readings.

## Roadmap

### Lane 0: close work already in flight

- Finish or explicitly park `P-CURVATURE-GAUSS-SPLIT-1`.
- Keep the merged mirror result out of the Canon until a separate reviewed
  fold states only its earned finite L5 scope.
- Clean merged worktrees and superseded branches only as a separate repository
  maintenance task, after unique-commit review.

This lane must not be mixed with new scientific commits.

### Lane 1: entropy selection recon

This is the highest-leverage next scientific lane. Four public probes have
already reduced `ENTROPY-LAYER-BRIDGE [O]` to an equivariant fiber selection

```text
Psi_kappa : O/lambda^5 -> L_kappa

Psi_(S kappa)(J y) = F_(theta(kappa))(Psi_kappa(y)).
```

The local analysis should proceed in this order:

1. Build an explicit `O/lambda^5` model, including lambda digits, the action
   of `J`, valuations, carries, and centralizer.
2. Decompose the living fiber as 625 canonical pentagons times one `F_5`
   coordinate, with the 313 recurrent components retained as invariants.
3. Rewrite the problem as finite-permutation cocycle cohomology over the
   Thue--Morse 2-adic factor. Search for a transfer family, not a finite
   cylinder rule.
4. Solve compatible truncated transfer equations and count solutions modulo
   the public symmetry/centralizer group.
5. Treat existence, canonicity, regularity, and measure as four separate
   decisions. A family can exist and still fail canonicity or regularity.
6. Attempt falsification first: incompatible truncations, two inequivalent
   inverse-limit families, or a pushforward mismatch are valid outcomes.

The first diagnostic is recorded in `notes/ENTROPY-SELECTION-RECON.md`.

### Lane 2: curvature classification

After Gauss split closes, keep three objects separate:

- the historical full-carrier operator `K_X`;
- the reduced spatial operator `C_S` from the quotient construction;
- the still-open canonical equivalence class.

Recommended order:

1. reproduce and type `C_S`, its trace, rank/nullity, and exact spectrum;
2. freeze the carrier, measure, projection group, equivalence relation, and
   ambient/intrinsic commutator choices;
3. enumerate or classify the admissible operator classes;
4. return exactly `UNIQUE`, `NONUNIQUE`, `EMPTY`, or `STOP`.

Do not optimize toward `-21/8`, a preferred spectrum, or a physical curvature
reading. Those are downstream questions.

### Lane 3: color-measure selection

Turn `COLOR-MEASURE-SELECTION [O]` into an exact constraint problem:

- rows: the 24 public carrier orbits;
- constraints: the 16 public observable types plus declared symmetries;
- outputs: feasibility, rank, solution-space dimension, positivity, and
  equivalence classes of weight vectors.

A unique admissible vector is a positive route. No vector or at least two
inequivalent survivors is an equally legitimate closure. Before a later fold,
audit whether the ledger should name an explicit dependency on the completed
color-measure transport claim.

### Lane 4: interfaces before phenomenology

Work upstream first:

1. `METRO-ADMISSIBILITY`;
2. `QUADRATIC-ENVELOPE-DECODER` and `QUADRATIC-DECODER-DATA`;
3. `OBSERVER-WRITE-PORT` after the decoder graph is typed;
4. `METRO-EDGE-SCALE` and the SI clause;
5. `TT-SOURCE` and `TT-VECTOR-STATE-NORMALIZATION` before polarization or
   quasinormal inference.

These items define what later numerical comparisons are even allowed to
mean.

### Lane 5: deferred empirical and imported-analysis work

Defer the following until their upstream scheme, inference, source, or
admissibility maps exist:

- `NS-TILT` and external CMB comparison;
- `ALPHA-S-RUNNING` before `SCHEME-DICTIONARY`;
- `QNM-LEAVER-MU` before a public shadow-to-mu inference rule;
- proton/QCD and neutron electromagnetic residuals;
- the photon roughening/import route;
- numerical gravitational-wave readings before source and normalization.

This avoids spending effort on comparisons whose public typing is still
open.

## Promotion boundary

A local analysis may become a public probe only after it has all of:

1. one named claim and action layer;
2. public inputs with exact identities;
3. a falsifier-first decision surface;
4. a declared scope ceiling;
5. a bounded exact computation or a proof plan;
6. collision review against issues, branches, probes, and registry;
7. an owner decision to create the public issue lock.

Only then should `PREREG.md` and an accepted verifier be frozen and pushed.
Canon edits come later, in a separate fold, after public probe merge and
readback. Several related finite results may be folded together, but no
speculative analysis belongs in the Canon bundle.

## Immediate next local milestone

The explicit lambda-digit carrier, living cell decomposition, finite-context
solver, first Rokhlin-tower baseline, exact cylinder measures, two-sided
collars, and a growing-context finite-horizon optimizer now live in
`notes/entropy_selection/`; exact local results are summarized in
`notes/ENTROPY-SELECTION-RECON.md`. The first level-2-anchored coordinate
optima through level 8 do not show a summable Cauchy tail. The next milestone
is a rigorous lower bound or global certificate for the small structured
horizons. It must return one of:

- an explicit compatible transfer system;
- a precise obstruction for a named regularity class;
- a proof that multiple inequivalent transfers survive, defeating canonicity;
- a smaller exact subproblem suitable for a later public preregistration.

The present empty finite-context cell-sector solver is not yet such a no-go:
it closes only its declared exact-cylinder ansatz. Likewise, a transfer that
is exact away from shrinking tower roofs is not yet a measurable construction;
cross-level Cauchy compatibility is the next gate.
