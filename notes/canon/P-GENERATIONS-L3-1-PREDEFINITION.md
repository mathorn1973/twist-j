# P-GENERATIONS-L3-1 predefinition ruling (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION`

This note proposes the finite typed definition surface required before the
generation count can be derived at the L3 boundary layer. It is not a public
probe, authorizes no enumeration or verifier, changes no Canon status, and
creates no selector obligation. The public lock is issue #687; the lane is
ordered as step 2 by the v71 working map
(`notes/PRACOVNI-MAPA-V71-2026-08-30`, section 9.2).

## Authority pin

```text
Canon:              Public Canon v71
state:              ACTIVE
tag:                canon-v71
content commit:     a77d720433c19976f9ab663d023ec9364eac34eb
Canon SHA-256:      0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
Canon bytes:        369836
main at drafting:   7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
owner row:          GENERATIONS-L3 [O], "the generation structure at the
                    standard model L3 frontier"
scheduler:          ROOT / READY / FORMAL
gate:               GATE-L2-L3-GENERATIONS (OPEN_LIFT, L2 -> L3), decision:
                    "closes positively by deriving the generation count at
                    the L3 boundary layer; closes negatively if the derived
                    count differs from three"
future probe:       P-GENERATIONS-L3-1 (claimed by issue #687)
```

## The definition tuple to be frozen

A valid predefinition package must publish one finite exact tuple

```text
S = (X_2, act_2, Eq_2,        the L2 source object, its action, its equality
     Y_3, act_3, Eq_3,        the L3 boundary carrier, its action, equality
     A, Adm,                  the complete admissible lift class A : X_2 -> Y_3
                              and its exact admissibility predicate
     totality, dep_graph,     totality status of every map and the finite
                              acyclic dependency graph
     N_gen,                   the integer functional N_gen : A -> Z_(>=0)
     no_three_certificate,    the exclusion audit of section 3
     decision_procedure,      the frozen routing of section 4
     certificate_schema,
     certificate_checker).
```

The symbols are placeholders until the corresponding slot rows below resolve.
No default is inherited from any historical text, and no slot may be filled
after inspection of the resulting count.

## 1. Slot audit against Public Canon v71

**Y_3 — UNRESOLVED, no public default exists.** v71 registers no L3-typed
carrier at all: `GENERATIONS-L3` is the only row naming the L3 layer, and it
carries no carrier, action, or equality. The L3 boundary slot must be
supplied by an owner ruling or by a prior public lane; until then it is
empty, not defaulted.

**X_2 — UNRESOLVED, every v71 candidate is itself open.** The L2-anchored
lanes of v71 are:

- `CURVATURE-OPERATOR-CANONICAL [O]` — the canonical L2 operator class is
  itself an open obligation (gate `GATE-L1-L2-CURVATURE-CANONICAL`,
  predefinition lane issue #108); it cannot serve as a frozen source while
  its own classification is open;
- `TRACEKERNEL-CURVATURE-FORCING` — L2 -> L1, scheduler BLOCKED;
- `ENTROPY-LAYER-BRIDGE` — L2 -> L5, scheduler STOP.

No settled registered L2 object exists today that can serve as `X_2`. The
admissible resolution routes are exactly:

```text
R1  wait for the canonical curvature class: X_2 := the closed output of the
    CURVATURE-OPERATOR-CANONICAL lane; couples this lane to issue #108 and
    is BLOCKED until that lane closes;
R2  an owner-ruled explicit finite L2 manifold object, frozen with its own
    justification that is independent of the number three and prior to any
    evaluation of N_gen;
R3  neither: the lane stops before any probe opens, and that stop is itself
    the recorded outcome (the map's section 9.2 declares this valuable).
```

**N_gen — SHAPE ONLY.** The functional must be total on `A`, valued in
`Z_(>=0)`, and defined by the types of `X_2` and `Y_3` alone (an orbit,
multiplicity, or component count of the lifted structure), never by its
value. Its exact definition necessarily rides the same freeze as `X_2` and
`Y_3` and is therefore unresolved with them.

**Frozen now by this draft (proposal, owner ANO at the lock):**

- the no-three prohibition of section 3;
- the decision procedure of section 4, verbatim from issue #687;
- the certificate schema of section 5.

## 2. The completeness demand

`A` must be the complete class of admissible lifts under `Adm`, or an
explicitly declared restricted subclass with the restriction stated in the
claim itself. A single constructed lift is not a derivation of generations;
`V = {N_gen(f) : f in A}` is computed only after `A` is closed.

## 3. The no-three prohibition

The integer three must not appear in the definitions of `X_2`, `Y_3`,
`act_2`, `act_3`, `Eq_2`, `Eq_3`, `Adm`, any normalization, or any selection
rule, except where it is forced verbatim by an already registered public row
cited by name. The `no_three_certificate` audits both the definition texts
and the constructed objects for cardinality-three choices that are not so
forced. A violation routes STOP at node 1 of the decision procedure.

## 4. Decision procedure (frozen)

With `V = { N_gen(f) : f in A }`:

```text
node 1  any slot of S unresolved, any map non-total without a declared
        residual domain, the dependency graph cyclic or incomplete, or the
        no-three certificate violated?      YES -> STOP     NO -> node 2
node 2  A empty?                            YES -> STOP (empty class)
                                            NO  -> node 3
node 3  |V| >= 2?                           YES -> STOP (multiple counts)
                                            NO  -> node 4
node 4  V = {3}?                            YES -> PASS
                                            NO  -> FAIL (V = {n}, n != 3)
```

All four outcomes are first class; `PASS`, `FAIL`, and `STOP` all remain
reachable at this predefinition, and nothing here anticipates which fires.

## 5. Certificate schema

The later pinned probe must produce: the complete enumeration or reduction
proof closing `A`; the per-lift evaluation transcript of `N_gen`; the
no-three audit; the totality and acyclicity checks; and the deterministic
route through section 4. The filled certificate is an output of the pinned
probe, never a predefinition input.

## Ruling

`STOP-PREDEFINITION`. The exact reasons: `Y_3` has no public carrier;
`X_2` has no settled public source (routes R1–R3 above); `N_gen` is
shape-only until both resolve. `READY` requires owner resolutions of the
`X_2` and `Y_3` slots frozen without knowledge of the resulting count; the
`READY` scheduler label does not substitute for this typed contract. No
`probes/` directory, preregistration, or verifier may be created while this
ruling stands.

## Debt firewall

This draft creates no Canon claim, moves no frontier row, changes no gate,
derives no count, and inserts the number three nowhere except inside the
target condition `V = {3}` of the registered decision, quoted from the
public gate row.
