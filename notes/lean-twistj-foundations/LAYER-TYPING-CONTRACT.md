# TWIST-J Lean layer-typing contract: cut 3

Status: **NON-CANONICAL DESIGN CONTRACT**.

Authority baseline: **Public Canon v32**. This stacked cut has parent
`notes/lean-twistj-observation-2` at commit
`33d015df40ed646ed46159096d450ec5efc2cf05`. `STATUS.md` remains the
exclusive authority declaration. This contract changes no Canon claim,
status, scope, dependency, evidence, frontier item, or release metadata.

This cut introduces only an explicit typed boundary between a read of one state,
a read of a named forward orbit, and an orbit read that an explicit dictionary
record has chosen to call spatial. It implements no public decoder stage or
leg, no physical space, and no Canon action-layer lift.

## 1. Three typing strata

The generic observation layer names two input carriers:

```lean
abbrev StateReading (S : AutonomousSystem) :=
  PartialReadout S.State

abbrev OrbitReading (S : AutonomousSystem) :=
  PartialReadout (ForwardOrbit S)
```

The input types enforce the difference. `StateReading S` receives one value
of `S.State`; `OrbitReading S` receives a pointed trajectory represented by
`ForwardOrbit S`. Neither alias is a typeclass and neither installs a
coercion.

`StateReading` is a generic negative-control object. The Public Canon decoder
continues to read forward orbits, not individual states. This cut supplies no
public state-reading leg and does not reinterpret a state read as the public
decoder.

The downstream dictionary leaf adds one nominal record:

```lean
structure SpaceReading (S : AutonomousSystem) where
  Output : Type v
  read : ForwardOrbit S → Option Output
```

The neutral field name `Output` is deliberate. A `SpaceReading S` value says
only that a dictionary has selected this orbit-indexed partial read and named
its role spatial. Supplying the record is declaration data, not a theorem that
`Output` is physical space or that any defined output exists.

These three typing strata are not the Canon action layers L1 state, L2
manifold, L3 boundary, L4 support, L5 stream, and L6 measure. In particular,
a generic `S.State` is not automatically the public L1 carrier, and a pointed
forward orbit or its reading is not automatically an L5 stream. No cross-layer
gate is defined or discharged here.

## 2. Named conversions only

The only state-to-orbit adapter supplied by this cut is the explicit function

```lean
def StateReading.atOrbitIndex
    (R : StateReading S) (k : ℕ) : OrbitReading S := ...
```

Its value at `κ` is `R.read (κ.stateAt k)`. The index `k` is a
metatheoretic sampling choice. It is not an external argument to `S.step`, a
physical time variable, a decoder clock, or a registered public convention.

A declared spatial role has the supplied explicit forgetful function

```lean
def SpaceReading.toOrbitReading
    (R : SpaceReading S) : OrbitReading S := ...
```

The conversion preserves the `Option` result definitionally. There is no
reverse helper from an arbitrary `OrbitReading` to `SpaceReading`: constructing
the nominal record must remain the visible dictionary declaration. There is
also no `instance`, `Coe`, `CoeFun`, typeclass, implicit cast, or quotient
connecting the three strata.

The absence of automatic conversion is an API and import-graph property. It
is not stated as the false proposition that no function can exist between two
types; constant functions always make such a proposition too strong.

## 3. Pointed-orbit and partiality boundaries

`ForwardOrbit S` remains the pointed representation introduced in cut 1. It
is not a quotient by shift, tail equality, or eventual equality and is not
proved identical to the Canon set `K` of forward `U`-orbits.

For all three strata, `none` means only that this local read is undefined at
the supplied input. In a `SpaceReading`, `none` does not mean that space does
not exist. Likewise, `some output` proves only that this declared partial map
returned that typed value; it does not confer a physical interpretation.

This cut creates no exact translation between the local `Option` interface
and the Canon's named partial-map domains.

## 4. Dictionary boundary and public non-claims

The existence of a `SpaceReading` term is not derived from `S.step`, the
Public Canon update `U`, `J`, a checkpoint, a commutator, or any registered
claim. The record does not select a canonical readout and carries no law of
totality, uniqueness, completeness, injectivity, separation, reconstruction,
equivariance, continuity, topology, metric, curvature, dimension, or measure.

In particular this cut does not:

- identify `SpaceReading.Output` with an L2 manifold, `GeometryData`, a
  curvature carrier, or a physical observable;
- implement `D_matter`, `D_geom`, `D_clock`, `D_linear`, `D_binary`, or
  `D_quadratic`;
- implement or strengthen `READING-SPLIT [D]`, `TIME-CUT-READING [D]`, or
  any other public dictionary row;
- prove that space arises from fired or silent commutators;
- select a canonical curvature operator or change
  `CURVATURE-OPERATOR-CANONICAL [O]`;
- construct a concrete v32 `SpaceReading` instance or a public-space alias;
- provide an L1-to-L2, L1-to-L5, or any other cross-layer lift; or
- establish existence, totality, uniqueness, or completeness of the decoder.

The empty-output and constant-output regressions are intentional. They show
that the nominal declaration alone supplies neither a defined spatial value
nor separation of orbit inputs.

## 5. No-feedback and import firewall

The new import direction is

```text
Foundation.Orbit ───────────────┐
Observation.PartialReadout ─────┴→ Observation.LayerTyping
                                      │
                                      ↓
                            Dictionary.SpaceReading
                                      │
Observation.OrbitReadout ─────────────┤
                                      ↓
                         Models.LayerTypingRegressions
                                      │
                                      ↓
                                    Audit
```

`Dictionary.SpaceReading` is a downstream leaf over the generic observation
API. Foundation, Architecture, and Observation do not import Dictionary.
Dictionary imports no Architecture, Decoder, Commutator, or AlgebraicSeed
module. The leaf neither implements nor bypasses a future staged Decoder; it
only freezes the nominal record shape needed to keep dictionary declaration
separate from observation mechanics.

No-feedback remains unresolved. `SpaceReading.Output` is arbitrary and could
itself contain a state or state-transforming function. The absence of a
dedicated `write` field therefore does not prove terminality of every future
observer completion. `OBSERVER-WRITE-PORT [H]` remains unchanged and STOP.

## 6. Mandatory regressions

`TwistJ.Models.LayerTypingRegressions` freezes the following controls on the
successor-system demonstration from cut 2:

1. the supplied state-to-orbit adapter is the named `atOrbitIndex` sampler,
   with no implicit conversion;
2. indices zero and one of the same orbit expose different state payloads;
3. a `SpaceReading` can use `Empty` as output and be undefined everywhere;
4. a defined constant `SpaceReading` can equate two distinct orbit inputs;
5. explicit forgetting through `toOrbitReading` preserves both `some` and
   `none`; and
6. none of these constructions introduces a public v32 spatial read.

These controls prevent equal payloads, input typing, dictionary declaration,
definedness, separation, and physical interpretation from being conflated.

## 7. Acceptance conditions

The stacked cut is acceptable only if all of the following hold:

1. it retains the exact Lean, Lake, Mathlib, and manifest pins from cuts 1 and
   2;
2. the complete stacked source builds from the committed lock;
3. `Audit.lean` reports no project axiom or `sorryAx` for the new conversion
   laws and regressions;
4. no `instance`, coercion, reverse adapter from `OrbitReading` to
   `SpaceReading`, or concrete public `SpaceReading` enters the source;
5. Foundation, Architecture, and Observation import no Dictionary module;
6. Dictionary imports no Architecture, Decoder, Commutator, or AlgebraicSeed
   module;
7. all mandatory regressions elaborate; and
8. independent review accepts that these typing strata neither implement the
   Canon action-layer protocol nor create a physical-space theorem.

A successful build remains a manual, status-neutral review aid. This cut is
not a formal probe, a minimal reproduction, a Canon patch, an `A-LEAN-*`
package, or a mechanism for promoting any claim.
