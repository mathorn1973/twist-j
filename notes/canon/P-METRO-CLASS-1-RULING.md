# P-METRO-CLASS-1 owner ruling (NON-CANONICAL)

Status: `DRAFT / LANE-READY / DEFINITION-UNRESOLVED / NOT PINNED`

This note starts the owner ruling for one formal metrology probe. It is not
`PREREG.md`, contains no accepted verifier, authorizes no formal execution,
and changes no Canon status. The public lock is issue #109.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          METRO-ADMISSIBILITY [O]
scheduler:          DECODER_CORE / ROOT / READY / FORMAL
gate:               GATE-L5-L6-METRO-NORMALIZATION
future branch:      probe/P-METRO-CLASS-1
future path:        probes/P-METRO-CLASS-1/
```

`READY` means that this root lane may choose and define one residual class.
It does not mean that a residual class, reduction relation, or admissibility
criterion has already been supplied by the Canon.

## Rejected minimal target and class-selection gate

The apparently smallest target is:

```text
METRO-RATIONAL-PRODUCT-FS
```

meaning finite products of normalized one-dimensional rational finite-state
protocols, with a vector readout and no stochastic, irrational,
unbounded-memory, non-finite-state, or SI-unit extension.

This candidate is **not accepted as the formal target**. Any finite Cartesian
product can be relabeled as one finite-state carrier. Without an invariant
typed meaning of dimension and vector support it is not beyond the current
one-dimensional boundary. Defining its admissibility to mean that every
factor is admissible would then be tautological, not a metrological theorem.

The product candidate may be reconsidered only if all of these are frozen
before output:

1. `d >= 2`, the structured product decomposition, and the codomain `Q^d`
   are parts of the type and cannot be erased by an allowed relabeling;
2. a direct product-level L5-to-L6 measure and normalization map is defined
   independently of factorwise admissibility;
3. the coefficient ring, source carrier, measure codomain, equality, and
   product/tensor normalization are exact and contain no hidden factor
   weights or new free parameter;
4. either the factorization is declared input structure with no canonicity
   claim, or all valid factorizations and regroupings yield the same decision;
5. finite bounds on `d`, state counts, and rational data are public, or an
   all-`d` theorem supplies completeness.

Even after those repairs, a product theorem would cover only a narrow
subclass. It must not automatically close the broad parent row or discharge
downstream quantification over every admissible output.

## Definition surface required for acceptance

Before `PREREG.md` or `verify.py` is created, the ruling must resolve this
finite tuple:

```text
P = (coefficient_ring,
     S, T, initial_scope, reachable_scope,
     readout, L5_source, L6_measure_codomain, equality,
     measure_transport, normalization, admissibility,
     reductions, reduction_equivalence,
     from_layer, to_layer, gate_id).
```

For any product candidate, it must additionally resolve:

1. whether a product protocol has synchronous or independently clocked
   factors;
2. whether the product state carrier is the full Cartesian product or only
   its reachable subset;
3. whether the vector readout is ordered, quotiented by coordinate
   permutations, or paired with a named basis;
4. the exact L5 source object, L6 measure object, and how factor measures and
   normalizations combine without hidden weights;
5. the complete allowed reductions, including explicit decisions on state
   relabeling, unreachable-state deletion, time refinement, factor
   permutation, factor regrouping, and any state minimization;
6. an exact equivalence on reduced protocols;
7. exact bounds on dimension, state counts, denominators and other rational
   data, or a theorem-grade all-parameter reduction;
8. whether two decompositions of the same underlying typed protocol must
   agree and how associativity and regrouping are certified.

No option in this list may be chosen after seeing a class count or
counterexample.

## Non-circular criterion requirement

A product candidate must supply two independently defined exact maps:

```text
Adm_direct(P)        from the direct product-level L5 -> L6 measure map,
Adm_compositional(P) from the separately defined factor maps and the frozen
                     product-normalization rule.
```

The target may be the theorem

```text
Adm_direct(P) = Adm_compositional(P)
```

on the complete frozen carrier. The equality may not be used as the
definition of either side. The verifier must also test both maps on every
allowed reduction-equivalence class and on every valid factorization required
by the ruling.

If the public one-dimensional boundary cannot supply its typed protocol and
criterion, or no independent direct product-level measure map is available,
the owner ruling remains incomplete. The correct result is then `STOP` before
a formal branch, not a convenient new definition hidden inside code.

## Parent-closure gate

Before a formal probe is authorized, review must state why the chosen class
can change the registered parent row without hiding residual work. One of the
following must be true:

1. the chosen class covers the complete protocol universe quantified by the
   registered scope and every downstream dependency; or
2. a separate governance fold first narrows or splits the scope explicitly
   and assigns every remaining residual class to a public owner.

Neither condition is currently established. Therefore issue #109 starts the
lane, but this draft does not yet authorize creation of
`probe/P-METRO-CLASS-1`.

## Frozen scientific routing for the future probe

Once the definition surface and parent-closure gate are accepted, the formal
preregistration must use:

```text
POSITIVE
  the exact public criterion classifies every protocol in the frozen class
  and is invariant under every allowed reduction.

NEGATIVE
  the direct and compositional predicates disagree, normalization is not
  total, two reduction-equivalent protocols receive different decisions, or
  two factorizations that are required to agree produce different decisions.

STOP
  the carrier, equality, criterion, reduction relation, normalization,
  completeness method, layer endpoints, or gate typing is incomplete or
  fails an integrity check.
```

Classifying an individual protocol as inadmissible is an ordinary output, not
a falsifier. A `NEGATIVE` result is first-class and must be preserved. `STOP`
is not a scientific result.

## Required controls

The future preregistration must include at least:

- one positive identity/relabeling control;
- one unreachable-state reduction control;
- one deliberately non-equivalent protocol pair;
- one normalization mismatch control;
- two valid decompositions or regroupings of one typed protocol when the
  ruling requires decomposition independence;
- complete orbit/class accounting for the frozen finite surface;
- exact L5-to-L6 typing through
  `GATE-L5-L6-METRO-NORMALIZATION`.

The six policy fields, accepted verifier, hashes, and immutable public pin
must exist before the first formal execution. `EXPECTED.txt`, `RUN.md`, and
`RESULT.md` remain forbidden before that pin.

## Scope firewall

The product control excludes non-finite streams, unbounded memory, stochastic
protocols, irrational carriers, physical units, the SI bridge, and scheme
selection. No narrow product result may by itself close
`METRO-ADMISSIBILITY`, `METRO-EDGE-SCALE`, `SCHEME-DICTIONARY`,
`OBSERVER-WRITE-PORT`, or decoder completeness. Other residual metrology
classes are neither solved nor opened as new registry rows by this ruling.
