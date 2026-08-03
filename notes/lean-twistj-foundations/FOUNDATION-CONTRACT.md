# TWIST-J Lean foundation contract: cut 1

Status: **NON-CANONICAL DESIGN CONTRACT**.

Authority baseline: **Public Canon v32**. `STATUS.md` remains the exclusive
authority declaration. This contract changes no Canon claim, status, scope,
dependency, evidence, frontier item, or release metadata.

Labels ending in `-target` describe possible future roles only. They are not
earned or registered public statuses.

## 1. Frozen scope

This cut formalizes only the counter consequence of the declared autonomous
skew-product architecture. The primitive dynamical object is

```lean
structure AutonomousSystem where
  State : Type u
  step : State → State
```

and metatheoretic iteration is

```lean
def AutonomousSystem.evolve
    (S : AutonomousSystem) (k : ℕ) : S.State → S.State :=
  S.step^[k]
```

The index `k` is not an external time input to the system. The primitive map
`step : State → State` accepts only the current complete state. `evolve k` is
the metalanguage operation used to discuss repeated application of that same
map.

An internal counter is additional structure, not a consequence of
determinism:

```lean
structure InternalCounter (S : AutonomousSystem) where
  tick : S.State → ℕ
  tick_step : ∀ x, tick (S.step x) = tick x + 1
```

The theorem target is

```text
tick (evolve k x) = tick x + k
0 < k -> evolve k x != x.
```

The first statement is induction on `k`; the second follows by applying
`tick` to a hypothetical return. Neither proof uses a project axiom.

## 2. `N0` and the public state shape

`N0` is a named copy of `ℕ` with fields

```lean
structure N0 where
  index : ℕ

def N0.succ (n : N0) : N0 :=
  ⟨n.index + 1⟩
```

This represents the named forward orbit of zero under the 2-adic odometer by
its index. It is not an identification with all of `ℤ_2`, and this cut defines
no Thue-Morse parity outside that forward orbit. A later map from `N0` into a
2-adic carrier is a separate theorem obligation.

The complete state is

```lean
structure CounterCheckpointSystem where
  Checkpoint : Type u
  updateCheckpoint : N0 → Checkpoint → Checkpoint

structure Omega (A : CounterCheckpointSystem) where
  counter : N0
  checkpoint : A.Checkpoint
```

and its one-step update is

```lean
def CounterCheckpointSystem.U (A : CounterCheckpointSystem) :
    Omega A → Omega A
  | ⟨n, ψ⟩ => ⟨n.succ, A.updateCheckpoint n ψ⟩
```

For the exact v32-shaped specialization, the checkpoint carrier is

```lean
Fin 6 → ZMod 5
```

which represents `F_5^6`. The checkpoint-update function remains an explicit
parameter. Thus the theorem covers every update of the displayed autonomous
skew-product form without pretending that the five internal maps or selector
have already been formalized.

## 3. Proposed public theorem

Proposed label: `FULL-STATE-NONRETURN [T-target]`.

Proposed scope:

> On the Public Canon v32 carrier `Omega = N0 × F_5^6`, every checkpoint map
> in the same autonomous counter-checkpoint skew-product shape advances the
> internal counter by exactly one per application of `U`; hence `U` has no
> positive-period point on the complete state. The declared v32 selector
> update is the intended Canon-level instance.

More explicitly, let `A : N0 × F_5^6 → F_5^6` and define

```text
U_A(n, ψ) = (n + 1, A(n, ψ)).
```

Then, for every complete state `ω` and `k : ℕ`,

```text
tick (U_A^[k] ω) = tick ω + k,
0 < k -> U_A^[k] ω != ω.
```

Here `tick (n, ψ) = n.index`; the statement does not install an implicit
coercion or addition operation on `N0`.

The declared v32 selector update is the intended instance of this universal
L1-only skew-product theorem. Its exact formula is not a Lean declaration in
this cut and remains part of the independent Canon-to-Lean translation review.

The Lean declarations intended to support independent translation review are

```text
CounterCheckpointSystem.counter_index_evolve
CounterCheckpointSystem.fullState_nonreturn
publicCanonV32_counter_index_evolve
publicCanonV32_fullState_nonreturn
```

The generic theorem is deliberately stronger in carrier generality. The
`publicCanonV32_*` theorem fixes the checkpoint carrier needed by the proposed
public wording.

This contract does not claim:

- that the checkpoint projection is nonperiodic;
- that every deterministic system carries a natural-valued internal counter;
- that the counter is physical time;
- that the theorem supplies a physical time arrow or physical irreversibility;
- that the update architecture is derived from `J`;
- that the displayed update is the unique admissible architecture;
- that a decoder is total, unique, or complete; or
- that every future observer completion has no write-back channel.

It also supplies no lift from L1 to any of L2--L6.

In particular, `OBSERVER-WRITE-PORT [H]` remains a live STOP obligation. A
module-import firewall for the current declared architecture is not a
classification of all future admissible completions.

The novelty boundary is equally explicit. `KERNEL-Z6-SYNCHRONIZATION [T]`
already proves checkpoint non-eventual-periodicity for the exact v32 update
from counter zero, while `CARRY-J-CHECKPOINT [T]` includes the checkpoint
recurrence `ψ_4 = ψ_6`. The proposed theorem instead quantifies over every
checkpoint update of the displayed shape and every initial counter, and it
speaks only about return of the complete state. It neither replaces nor
weakens those existing checkpoint results.

## 4. Orbit and future readout boundary

`ForwardOrbit S` names a forward orbit by its initial complete state, and
`ForwardOrbit.stateAt` derives its sequence by `evolve`. A future readout
layer can therefore use an orbit as its input rather than silently reading one
state.

This cut introduces no `PartialReadout` or `ReadoutFamily`; those belong to the
next cut. When added, their required shapes are

```lean
structure PartialReadout (Input : Type u) where
  Output : Type v
  read : Input → Option Output

structure ReadoutFamily (Input : Type u) where
  Index : Type v
  Output : Index → Type w
  read : (i : Index) → Input → Option (Output i)
```

For the public decoder, `Input` must be a forward-orbit type. `Option`
preserves the distinction between undefined and defined output.

The stacked implementation of that next cut is governed separately by
`OBSERVATION-CONTRACT.md`; it does not retroactively widen this cut 1 contract.

## 5. Import firewall

The present modules obey

```text
Foundation
    ↓
Architecture.CounterCheckpoint / Architecture.UpdateShape
    ↓
Models.CounterRegressions / Audit
```

The planned extension must preserve

```text
Foundation
    ↓
Architecture.Update
    ↓
Observation
    ↓
Decoder
    ↓
Dictionary.
```

Forbidden edges include

```text
Architecture.Update -> Decoder
Architecture.Update -> Dictionary.
```

No `AlgebraicSeed` module is an ancestor of the counter theorem. The
no-return result depends on the declared architecture, not on `J`. Any later
algebraic-seed development is a parallel branch of the dependency graph.

That later branch must itself keep two layers distinct. `FifthRootData` may
carry a primitive fifth root in a general commutative ring and define
`FifthRootData.J` as `1 + ζ^2`; `J` is a Lean `def`, not a Lean `axiom`.
Arithmetic statements such as the public norm and trace belong to a separate
`CyclotomicFiveData` layer for `Q(ζ_5)` or `Z[ζ_5]`, not to arbitrary
commutative rings. The public word "axiom" records the choice of this defined
object as the generator of the theory; it does not authorize an unproved Lean
constant.

## 6. Mandatory regressions

`TwistJ.Models.CounterRegressions` freezes four negative controls.

1. A counter on `ZMod 5` returns after five steps.
2. That modular system cannot carry the exact `ℕ`-valued `tick_step` law.
3. A one-state deterministic system also admits no such internal counter.
4. Two complete states may have equal checkpoint projections but different
   counters; a constant checkpoint can recur at every step while the complete
   state still has no positive-period point.

These examples ensure that non-return follows from the exact natural-counter
law on the complete state, not from the words "counter", "deterministic", or
"checkpoint".

## 7. Acceptance conditions for this laboratory

The first cut is acceptable only if all of the following hold:

1. the committed Lean and Mathlib pins match the existing reviewed laboratory;
2. the complete source builds from the committed Lake lock;
3. `Audit.lean` reports no project axiom and no `sorryAx` for the general and
   v32-shaped counter/non-return theorems;
4. the import graph contains no decoder, dictionary, or algebraic-seed edge;
5. the regression theorems elaborate; and
6. an independent reviewer accepts the translation between the proposed
   Canon wording and the Lean statement.

This remains status-neutral even after a successful build. The ordinary Canon
process must first establish and release an exact `T` or `T-LOCK` statement.
Only afterward may a separate `A-LEAN-*` package audit that already released
scope under whatever supplemental-audit policy is then active. Draft PR #249
does not promote this laboratory and is not imported here.

The later work order remains:

```text
1  counter and complete-state non-return
2  orbit readout and layer typing
3  commutator boundary and fired no-go
4  algebraic seed and axiom boundary
5  Canon foundation wording.
```
