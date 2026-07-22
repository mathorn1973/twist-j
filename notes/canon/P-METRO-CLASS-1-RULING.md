# P-METRO-CLASS-1 owner ruling (NON-CANONICAL)

Status: `DRAFT / LANE-READY / DEFINITION-UNRESOLVED / NOT PINNED`

This note starts the owner ruling for one formal metrology probe. It is not
`PREREG.md`, contains no accepted verifier, authorizes no formal execution,
and changes no Canon status. The public lock is issue #109.

The owner consolidation `V15-OWNER-FOLD-107-109.md` selects a joint exact
certificate architecture for this lane. It does not supply the certificate
schema or its soundness/completeness proof, so the definition remains
unresolved and the future probe remains unauthorized.

## Authority pin

```text
Canon:              Public Canon v15
state:              ACTIVE
tag:                canon-v15
activation commit:  8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:     a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:      53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:        89288
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
   without defining admissibility by factorwise limits;
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
     joint_certificate_relation,
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

## Direct criterion and joint-certificate requirement

The scientific predicate is the direct translated-box property:

```text
Adm_direct(P) in Decision(Y_r),

Decision(Y_r) = {INADMISSIBLE} union {ADMISSIBLE(L) : L in Y_r}.

Adm_direct(P) is the exact decision obtained from the direct L5 -> L6
transport, including total tagged normalization, uniformity over allowed
starts and translations, the unique terminal value L in the admissible
case, and an effective modulus.
```

Factorwise power convergence is not a second admissibility law. The future
definition must instead publish an exact certificate relation

```text
Cert_joint(P, c, d),

d in Decision(Y_r).
```

The decision `d` carries only the semantic output: `INADMISSIBLE`, or
`ADMISSIBLE(L)` with its exact terminal value. The certificate `c` carries
the proof payload: an effective modulus in the admissible case, or an exact
failure witness in the inadmissible case, together with the required exact
algebraic data. Multiple valid certificates may carry the same decision.

The certificate data must cover both the anchored joint action and uniform
translated boxes. It therefore includes simultaneous primary/peripheral data
on the relevant invariant submodule of `Q^(S_reach)`, the individual digit
transition maps, a q-adic boundary/residue decomposition, and an effective
modulus. Averaged actions alone do not certify translated-box uniformity. The
relevant submodule is generated by the readout components under the allowed
actions. The frozen certificate type must also include the observable quotient
induced by evaluation at every allowed reachable start; a Krylov submodule
alone is insufficient when the allowed starts do not exhaust `S_reach`.
Algebraic modes outside the typed observable quotient cannot manufacture
failure.

`Cert_joint` must be defined from its own exact algebra and certificate
schema, without consulting the output of `Adm_direct`. Before a formal
branch, the definition package must freeze a terminating checker and the
soundness/completeness target

```text
Adm_direct(P) = d
  iff there exists c with Cert_joint(P,c,d),

no two valid certificates for P carry different decisions, and every
valid certificate carrying `ADMISSIBLE(L)` carries the same exact `L`.
```

The target covers both the anchored all-parameter reduction and the full
translated-box property with an effective modulus. The equivalence is a
theorem to be decided, never the definition of either side.

If the direct property, certificate schema, relevant submodule, exact
peripheral/Jordan tests, translated-box boundary reduction, or completeness
method remains unresolved, the correct state is `STOP` before a formal
branch. No factorwise shortcut or convenient new definition may be hidden
inside code.

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
  the exact direct criterion classifies every protocol in the frozen class;
  the joint certificate system is sound and complete for it; and the
  decision is invariant under every allowed reduction.

NEGATIVE
  an exact admitted counterexample refutes certificate soundness or
  completeness, normalization is not total, two reduction-equivalent
  protocols receive different direct decisions, or two presentations or
  factorizations required to agree receive different direct decisions.

STOP
  the carrier, equality, direct criterion, certificate schema, relevant
  submodule, reduction relation, normalization, completeness method, layer
  endpoints, or gate typing is incomplete; or the checker/artifact fails an
  integrity or reproduction check without an exact mathematical
  counterexample.
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
- the exact two-state fixed-length control from
  `P-METRO-CLASS-1-FORK-WITNESS.md`, used only to reject factorwise power
  convergence as a necessary law for joint anchored convergence;
- two valid decompositions or regroupings of one typed protocol when the
  ruling requires decomposition independence;
- for a `FINITE SURFACE`, complete orbit/class accounting; for an
  `ALL-PARAMETER THEOREM`, termination and completeness certificates plus
  finite regression controls;
- exact L5-to-L6 typing through
  `GATE-L5-L6-METRO-NORMALIZATION`.

The six policy fields, accepted verifier, hashes, and immutable public pin
must exist before the first formal execution. `EXPECTED.txt`, `RUN.md`, and
`RESULT.md` remain forbidden before that pin.

The fixed-length factorwise control is proposal-local. It creates no Canon
row, evidence owner, dependency, or independent metrology obligation, and it
does not by itself decide the complete direct property on an admitted
protocol.

## Scope firewall

The product control excludes non-finite streams, unbounded memory, stochastic
protocols, irrational carriers, physical units, the SI bridge, and scheme
selection. No narrow product result may by itself close
`METRO-ADMISSIBILITY`, `METRO-EDGE-SCALE`, `SCHEME-DICTIONARY`,
`OBSERVER-WRITE-PORT`, or decoder completeness. Other residual metrology
classes are neither solved nor opened as new registry rows by this ruling.
