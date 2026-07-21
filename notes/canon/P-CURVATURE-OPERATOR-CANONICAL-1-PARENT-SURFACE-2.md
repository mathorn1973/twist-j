# P-CURVATURE-OPERATOR-CANONICAL-1 parent surface proposal 2 (NON-CANONICAL)

Status: `DRAFT / STOP-DEFINITION / SURFACE-PROPOSAL`

This note serves issue #108. It proposes a parent candidate surface in
which the frozen four-way gate is carried honestly, after the merged
rejection of the earlier `EMPTY` routing retype. It is not a public
definition, probe, enumeration result, verifier, selector, Canon change,
or status proposal. The scheduler stays `STOP`.

## Authority pin

```text
Canon:              Public Canon v14, ACTIVE, tag canon-v14
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
public main:        3f6500a
owner row:          CURVATURE-OPERATOR-CANONICAL [O]
gate:               GATE-L1-L2-CURVATURE-CANONICAL
controlling notes:  P-CURVATURE-OPERATOR-CANONICAL-1-PREDEFINITION.md,
                    P-CURVATURE-OPERATOR-CANONICAL-1-DEFINITION-CANDIDATE.md,
                    P-CURVATURE-OPERATOR-CANONICAL-1-AUT-REDUCTION.md
```

## 1. Accepted constraints

Three merged rulings bound this proposal:

```text
1  Zero rows stay in the family AND in the outcome counting. The earlier
   proposal to retype EMPTY as "all surviving classes are zero" is
   rejected as merged: one nonzero plus one zero class must stay
   NONUNIQUE, never UNIQUE.
2  Aut_arch_aff = { identity }, so the affine quotient merges no typed
   exact-equality classes. Uniqueness cannot come from symmetry.
3  No result-dependent admissibility: no rank, trace-square, spectrum,
   nonzero, continuum, or historical-value filter.
```

The consequence is stated plainly: on the 640-row computed inventory,
`EMPTY` cannot be an epistemically open outcome of any pre-result surface,
because well-formed rows exist by construction. The branch-classification
precedent on the D_matter lane sets the accepted standard: the four-way
outcome space is carried as a complete type, a provably unreachable member
is declared as a theorem rather than hidden, and the live scientific
burden sits on `UNIQUE-ALGEBRAIC` versus `NONUNIQUE`.

## 2. The surface, mirroring the accepted C5 pattern

```text
Universe        the frozen 640-row child inventory of the definition
                candidate, with its typed carriers, exact equality, and
                the trivial affine quotient.
Adm_base        the pre-result conditions already frozen there:
                well-formedness, declared carrier routing (dim = 0 rows to
                DEGENERATE-CARRIER, retained), integrity identities as
                checks not filters. Base classification counts ALL typed
                classes, zero classes included.
Outcome space   UNIQUE-ALGEBRAIC | NONUNIQUE | EMPTY | STOP, with the
                declaration: under Adm_base, EMPTY is provably
                unreachable (theorem, not surprise); the expected base
                outcome is NONUNIQUE; neither carries parent force.
Optional
labeled
filters         each one is a candidate dictionary clause; each requires
                its own reviewed owner fold to have any force; the
                classification under each filter again counts ALL
                admissible classes:

  Adm_natural       the row's mode is restriction-natural along the
                    subset tower: for S subseteq S' (same pair, same
                    mode), P_(S') K(S) P_(S') = K(S').
  Adm_recurrent     S subseteq {b, d, e} and pair = {a, c}: the averaging
                    subset lies in the public recurrent mirror algebra
                    and the commutator pair is the public ghost pair
                    (the two generators that never fire on the
                    attractor). Grounded in the public census rows, not
                    in any operator value.
```

## 3. The naturality lemma (proof, not enumeration)

For `S subseteq S'` the `S'`-orbits are unions of `S`-orbits, so
averaging over the coarse partition absorbs averaging over the fine one:

```text
R_(S') R_S = R_(S'),   hence   P_(S') P_S = P_(S').
```

Therefore, for the ambient mode,

```text
P_(S') K_AMB(S,u,v) P_(S')
  = P_(S') P_S C_uv P_S P_(S')
  = P_(S') C_uv P_(S')
  = K_AMB(S',u,v).
```

So `AMB` rows satisfy `Adm_natural` identically (theorem). Whether `INT`
rows satisfy it is OPEN, and that openness is the genuine content of the
filter: under `Adm_natural` the reachable live outcomes are
`UNIQUE-ALGEBRAIC` versus `NONUNIQUE`, with `EMPTY` again declared
provably unreachable (the `AMB` tower exists). No enumeration is run here
and no `INT` witness is computed; the question stays blind for the future
probe.

Under `Adm_recurrent` the subfamily has 8 subsets times 1 pair times 2
modes, 16 rows before routing and equality; the historical row lies
inside it (regression fact, not a filter); its class landscape is open.
The conjunction `Adm_natural and Adm_recurrent` is the strongest candidate
clause and its landscape is also open.

## 4. Acceptance reading

The merged predefinition acceptance item (both positive and negative
scientific outcomes reachable) is carried the same way the accepted
branch classification carries it: positive = `UNIQUE-ALGEBRAIC` under a
declared filter; negative = `NONUNIQUE`; `EMPTY` remains a formal member
of the complete outcome type with its unreachability declared as a
theorem of the frozen surface; `STOP` guards incompleteness. No false
`EMPTY` and no manufactured `UNIQUE` are possible: all classes count,
zeros included, and filters are pre-result predicates whose only proven
member (`AMB` naturality) is proven in this note, before any enumeration.

## 5. Governance and firewall

```text
DEFAULT AFTER READBACK   no filter is adopted; the base surface carries no
                         parent force; CURVATURE-OPERATOR-CANONICAL stays
                         [O]; scheduler stays STOP.
FILTER ADOPTION          a separate reviewed owner fold per filter, stating
                         the clause and its bounded scope, exactly as the
                         D_matter FILTER-ADOPTED state is typed.
FORMAL PROBE             forbidden until a surface with its filters is
                         reviewed, merged, read back, and freshly
                         preregistered; earlier incubation computations are
                         provenance, not evidence.
```

The frontier count is unchanged. This proposal reduces the issue #108
task to two bounded owner choices: whether to adopt this surface as the
parent candidate universe, and which, if any, labeled filter to adopt as
a scoped dictionary clause.
