# TWIST-J Lean observation contract: cut 2

Status: **NON-CANONICAL DESIGN CONTRACT**.

Authority baseline: **Public Canon v32**. This stacked cut has parent
`notes/lean-twistj-foundations-1` at commit
`51e12bd4fe0f2b6998c1b91e8b6113302079efcb`. `STATUS.md` remains the
exclusive authority declaration. This contract changes no Canon claim,
status, scope, dependency, evidence, frontier item, or release metadata.

This cut formalizes a pointed forward trajectory, partial readouts on a common
input, indexed readout families with index-dependent output carriers, and the
kernel equivalence induced by equality of their `Option` outputs. It supplies
no concrete public decoder leg, stage, output schema, physical dictionary,
completion, or public claim status.

## 1. Frozen objects

The first cut already defines a named forward orbit by its initial complete
state:

```lean
structure ForwardOrbit (S : AutonomousSystem) where
  initial : S.State

def ForwardOrbit.stateAt (κ : ForwardOrbit S) (k : ℕ) : S.State :=
  S.evolve k κ.initial
```

The second cut adds two ordinary explicit structures:

```lean
structure PartialReadout (Input : Type u) where
  Output : Type v
  read : Input → Option Output

structure ReadoutFamily (Input : Type u) where
  Index : Type v
  Output : Index → Type w
  read : (i : Index) → Input → Option (Output i)
```

Neither structure is a typeclass and neither installs a coercion. A selected
family leg can be converted explicitly to `PartialReadout`; a single readout
can be converted explicitly to a unit-indexed family.

For orbit observation the input aliases are

```lean
OrbitPartialReadout S := PartialReadout (ForwardOrbit S)
OrbitReadoutFamily S  := ReadoutFamily (ForwardOrbit S).
```

The exact v32-shaped alias takes the forward orbit of
`(publicCanonV32System updateCheckpoint).autonomousSystem`. As in cut 1, the
checkpoint update remains a parameter with the declared v32 selector update
as its intended Canon-level instance. No internal formula for `a,...,e` is
introduced here.

## 2. Pointed-orbit boundary

`ForwardOrbit S` is a pointed trajectory represented by an initial complete
state and its derived iterates. It is not yet a quotient or a proof of exact
identification with the Canon set `K` of forward `U`-orbits.

In particular, this cut does not:

- identify two initial states with equal tails;
- quotient by shifts or eventual equality;
- prove an extensional sequence characterization of orbit equality;
- implement the public `history_equivalence_id`; or
- prove that the pointed representation is canonical, complete, or unique.

The input type nevertheless enforces the required ontological distinction: an
orbit readout receives a named forward trajectory, not a single state. A
particular readout may inspect any derived `stateAt k`, but this cut declares
no public readout formula.

## 3. Partiality and `Option`

`none` means that a readout is undefined at that input. `some output` means
that it is defined with that exact typed value. There is no implicit default
output and no erasure of the distinction:

```text
none != some output.
```

At the same time, two undefined reads at the same family leg compare equal:

```text
none = none.
```

This is the intended extensional semantics of this small interface. `Option`
does not record a reason for undefinedness, a public `domain_id`, a staged
domain proof, or a completion manifest. `PartialReadout.IsDefinedAt` and
`IsUndefinedAt` are local predicates only.

## 4. Heterogeneous observational equivalence

For one fixed family, define

```lean
def ReadoutFamily.ObservationallyEquivalent
    (R : ReadoutFamily Input) (x y : Input) : Prop :=
  ∀ i, R.read i x = R.read i y
```

The family is heterogeneous because `Output i` depends on `i`. Values are
compared only at the same index, where both sides have type
`Option (Output i)`. No `HEq`, cross-index coercion, or equality between
different output carriers is asserted.

The relation is reflexive, symmetric, and transitive and is packaged as a
`Setoid` for the fixed family. Equality of inputs implies observational
equivalence. One unequal leg refutes it. No quotient is constructed.

These elementary facts do not make the relation any of the following:

- equality of forward orbits;
- an injectivity, separation, reconstruction, or completeness theorem;
- a maximal invariant or universal quotient;
- a congruence for `U` or for orbit shift;
- a candidate equivalence up to output isomorphism;
- the Canon reduction equivalence or `history_equivalence_id`; or
- a factor-canonicity, terminality, or decoder-completion result.

The family index may be empty. In that case every two inputs are vacuously
equivalent. A constant defined family or an everywhere-undefined family can
also equate distinct inputs. The structure therefore assumes neither
nonemptiness nor separation.

## 5. Relationship to the public decoder

Public Canon v32 declares the staged partial interface

```text
D_matter : dom(D_matter) subset K -> MatterData
D_geom   : dom(D_geom) subset K x MatterData -> GeometryData
D_clock  : dom(D_clock) subset K x MatterData x GeometryData
          -> ObservableHistory,
```

where the Canon names partial-map domains rather than using `Option`
signatures. `Option` is only this cut's local totalized representation of
undefinedness; no exact translation theorem is asserted. This cut does not
implement those three stages. `ReadoutFamily` has one common input type and
therefore does not by itself model their staged dependent inputs.

The functional stages `D_matter`, `D_geom`, and `D_clock` are also distinct
from the registered reading legs `D_linear`, `D_binary`, and `D_quadratic`.
No assignment between those two axes is introduced here.

Relative to `READING-SPLIT [D]`, this cut supplies only a possible future
typed carrier for a family of readings. It implements none of the three
registered maps, proves no relation between them, and changes neither the
claim's status nor its evidence.

## 6. No-feedback and import firewall

The stacked module graph has two upstream branches that meet at orbit
observation:

```text
Observation.PartialReadout → ReadoutFamily → ObservationalEquivalence ─┐
Foundation.AutonomousSystem → Foundation.Orbit ────────────────────────┤
Foundation.AutonomousSystem → Architecture.UpdateShape ────────────────┤
                                                                       ↓
                                                       Observation.OrbitReadout
                                                                       │
                                                                       ↓
                                            Models.ReadoutRegressions / Audit
```

Arrows point from an imported upstream module toward a downstream consumer.
`OrbitReadout` imports both `Foundation.Orbit` and
`Architecture.UpdateShape`, while the generic observation chain is independent
of both. No existing Foundation or Architecture source imports Observation.
Observation imports no future Decoder or Dictionary module. The algebraic-seed
laboratory remains a parallel project and is not an import ancestor.

This acyclic graph formalizes only the currently declared dependency
direction. The absence of a `write` field does not resolve
`OBSERVER-WRITE-PORT [H]`. In particular, `Output` is an arbitrary type and
could itself contain a state or a state-transforming function. This cut
publishes no complete output schema, write-channel type, L1 codomain,
protocol class, closure manifest, or complete dependency graph.

Therefore `OBSERVER-WRITE-PORT [H]` remains unchanged and STOP. A future
Decoder may import Observation; Observation must not import that future
Decoder, and Architecture.Update must not import either Decoder or Dictionary.

## 7. Mandatory regressions

`TwistJ.Models.ReadoutRegressions` freezes the following controls on named
forward orbits of a simple successor system:

1. `none` differs from a defined `some` value;
2. two distinct inputs can both produce `none`;
3. a heterogeneous family has both `ℕ` and `Bool` output legs;
4. equal `none` results at one leg do not imply family equivalence;
5. a defined/undefined difference at one leg refutes family equivalence;
6. an everywhere-undefined family equates distinct inputs;
7. an everywhere-defined constant family also equates distinct inputs; and
8. an empty-index family equates every two inputs vacuously.

These regressions prevent partiality, heterogeneity, observational equality,
input equality, totality, and separation from being silently conflated.

## 8. Acceptance conditions

The stacked cut is acceptable only if all of the following hold:

1. it retains the exact Lean, Lake, Mathlib, and manifest pins from cut 1;
2. the complete stacked source builds from the committed lock;
3. `Audit.lean` reports no project axiom or `sorryAx` for the observation
   structures, equivalence laws, and regressions;
4. no source under Foundation or Architecture imports Observation, Decoder,
   Dictionary, or AlgebraicSeed;
5. no observation source imports Decoder, Dictionary, or AlgebraicSeed;
6. all mandatory regressions elaborate; and
7. an independent reviewer accepts the distinction between this kernel
   relation and every stronger public decoder or orbit-equivalence notion.

A successful build remains a manual, status-neutral review aid. This cut is
not a formal probe, a minimal reproduction, a Canon patch, an `A-LEAN-*`
package, or a mechanism for promoting any claim.

The downstream layer-typing extension is governed separately by
`LAYER-TYPING-CONTRACT.md`. It does not retroactively widen this cut 2
contract or turn a generic observation into a physical dictionary statement.
