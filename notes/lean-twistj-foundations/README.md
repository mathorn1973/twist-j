# Lean laboratory: TWIST-J foundations, cuts 1 and 2

Status: **NON-CANONICAL NOTE**.

This directory is the stacked Lean laboratory for the first two narrow Public
Canon v32 ontology cuts. It separates things that the prose must not conflate:

- an autonomous one-step map;
- a natural-valued internal counter carried by the complete state;
- a checkpoint projection that may recur; and
- the metatheoretic iteration used to state and prove a theorem;
- a named forward orbit rather than one state;
- an undefined partial read rather than a default value; and
- equality of every reading under one family rather than equality of the
  orbit inputs.

The central manual theorems are

```text
tick (evolve k ω) = tick ω + k
0 < k -> evolve k ω != ω.
```

`TwistJ.Architecture.publicCanonV32_fullState_nonreturn` specializes the
second theorem to a checkpoint carrier represented by `Fin 6 → ZMod 5`, with
an arbitrary checkpoint map in the same counter-checkpoint skew-product shape.
The declared v32 selector update is the intended Canon-level instance; its
exact translation remains a separate review obligation because this cut does
not formalize or assume the internal formulas for `a,...,e`.

The second cut adds ordinary explicit `PartialReadout` and heterogeneous
`ReadoutFamily` structures. For one fixed family it defines

```text
ObservationallyEquivalent R x y
  iff for every i, R.read i x = R.read i y.
```

The output carrier may depend on `i`; outputs are compared only at the same
index. Orbit readout aliases accept `ForwardOrbit S`, not a single state.

Nothing here changes `canon/`, the registry, frontier, evidence ledger,
history, release metadata, or any claim status. In particular,
`FULL-STATE-NONRETURN` is only a proposed future `T-target` label. This tree is
not a formal probe, a minimal reproduction, or an `A-LEAN-*` audit package.

## Contents

```text
TwistJ/Foundation/
  AutonomousSystem.lean
  InternalCounter.lean
  Orbit.lean
TwistJ/Architecture/
  N0.lean
  CounterCheckpoint.lean
  UpdateShape.lean
TwistJ/Observation/
  PartialReadout.lean
  ReadoutFamily.lean
  ObservationalEquivalence.lean
  OrbitReadout.lean
TwistJ/Models/
  CounterRegressions.lean
  ReadoutRegressions.lean
Audit.lean
FOUNDATION-CONTRACT.md
OBSERVATION-CONTRACT.md
```

The enforced import graph in the stacked cuts is

```text
Foundation.Orbit ---------------------> Observation.OrbitReadout
Architecture.UpdateShape ------------> Observation.OrbitReadout
PartialReadout -> ReadoutFamily -> ObservationalEquivalence
Observation --------------------------> Models/Audit
```

There is no algebraic-seed, decoder, dictionary, commutator, or layer module in
this project. Observation may import the update layer; the update layer does
not import Observation and must never import Decoder or Dictionary. The
parallel algebraic-seed laboratory is not a dependency.

## Pinned manual environment

This laboratory deliberately reuses the already reviewed environment of
`notes/lean-j-cyclotomic/`:

```text
toolchain:    leanprover/lean4:v4.30.0
Lean commit:  d024af099ca4bf2c86f649261ebf59565dc8c622
Lake:         5.0.0-src+d024af0
Mathlib:      c5ea00351c28e24afc9f0f84379aa41082b1188f
manifest:     format 1.2.0
```

The complete nine-package closure is pinned in `lake-manifest.json`.
Generated `.lake/` state is ignored.

From this directory, the manual checks are:

```bash
lake env lean --version
lake build
lake env lean Audit.lean
```

Routine builds consume the committed lock. `lake update` is only a lock
regeneration check here and must leave `lake-manifest.json` byte-identical.

`Audit.lean` prints the axiom footprint of the counter theorems, the exact
v32-shaped specialization, the observation-equivalence laws, and the
regressions. A successful local build is a review aid only and creates no
public evidence or scientific status.

## Manual verification

On 2026-08-02, Ubuntu 24.04.3 LTS x86_64 with the pins above reported:

```text
Build completed successfully (1121 jobs).
```

`lake env lean Audit.lean` exited zero. The general counter theorem, general
no-return theorem, both architecture theorems, and both exact v32-shaped
specializations each reported `does not depend on any axioms`. No project
axiom or `sorryAx` occurs. The modular `ZMod 5` periodicity regression alone
reported `[propext, Quot.sound]`, as expected for its quotient carrier; those
axioms do not enter the general or v32-shaped results.

Lake's regenerated lock was byte-identical to the committed manifest:

```text
lake-manifest.json  3173 bytes
SHA-256             85af4a94effdd6d702b41d39901181bc76f76e3a796113406d93acec0c95394c
```

These are manual, status-neutral checks. No build output or run record is
tracked.

On 2026-08-03, the stacked cut 2 source on Ubuntu 24.04.3 LTS WSL2 x86_64
with the same committed pins reported:

```text
Build completed successfully (1126 jobs).
```

`lake env lean Audit.lean` exited zero. The pointwise observational-equivalence
laws, its explicit `Setoid`, the unequal-leg theorem, the `leg` and `toFamily`
bridges, the everywhere-undefined and everywhere-constant examples, and the
empty-family regression reported `does not depend on any axioms`. The local
undefinedness lemma and concrete conditional Option regressions reported only
`[propext]`. No project axiom or `sorryAx` occurs. The earlier
`ForwardOrbit.stateAt_succ` proof reports `[propext, Quot.sound]` through the
Mathlib iteration machinery; neither axiom enters the counter/no-return or
observation-equivalence laws.

The cut 1 lock remained byte-identical:

```text
lake-manifest.json  3173 bytes
SHA-256             85af4a94effdd6d702b41d39901181bc76f76e3a796113406d93acec0c95394c
```

The binding design scopes and their non-claims are in
`FOUNDATION-CONTRACT.md` and `OBSERVATION-CONTRACT.md`.
