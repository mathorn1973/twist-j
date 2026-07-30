# P-CURVATURE-OPERATOR-CANONICAL-1 predefinition ruling (NON-CANONICAL)

Status: `DRAFT / STOP-PREDEFINITION`

This note proposes the finite definition surface required before canonical
curvature can be classified. It is not a public probe, authorizes no
enumeration or verifier, changes no Canon status, and creates no selector
obligation. The public lock is issue #108.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          CURVATURE-OPERATOR-CANONICAL [O]
scheduler:          DECODER_CORE / ROOT / STOP / FORMAL
normative layer:    L2
gate:               GATE-L1-L2-CURVATURE-CANONICAL
future probe:       P-CURVATURE-OPERATOR-CANONICAL-1
```

The closed historical results provide one exact witness on the full
`F_5^6` carrier:

```text
K_hist = P[A,C]P |_V,
Tr(K_hist^2) = -881/8,
K_amb = K_int,
K_ext = 0,
rank(K_hist) = 292,
nullity(K_hist) = 526.
```

They constrain one declared full-carrier candidate but do not define a
future candidate class and do not select `K_hist` as canonical.

The registered dependency floor is:

```text
CURVATURE-OPERATOR-CANONICAL -> DEF-ARCHITECTURE
  [REQUIRES]
CURVATURE-OPERATOR-CANONICAL -> CURVATURE-HISTORICAL-GAUSS-SPLIT
  [BOUNDED_BY]
```

## Classification object to be frozen

A valid definition package must publish one finite exact tuple

```text
S = (X, k, F, mu, G, star, Tr,
     G_proj, rho, R, P0, P, V,
     W, K_rule, normalization,
     Adm, Equiv, order,
     classification_algorithm,
     completeness_method,
     certificate_schema,
     certificate_checker).
```

The symbols are placeholders until the corresponding rows below resolve.
No default is inherited merely because the historical witness used it. The
filled class-count certificate is an output of the future pinned probe, not a
predefinition input.

| Block | Required decision | Current ruling |
| --- | --- | --- |
| carrier | finite `X`, coefficient field `k`, function/module space `F`, total domain and codomain | `UNRESOLVED` |
| measure | exact weights `mu`, Gram/inner product `G`, adjoint `star`, ordinary or normalized trace `Tr` | `UNRESOLVED` |
| projection | complete allowed projection-group class `G_proj`, action `rho`, Reynolds convention `R`, constant removal `P0`, resulting `P` and `V`, conjugacy treatment | `UNRESOLVED` |
| operator | complete finite word/generator class `W`, ambient/intrinsic/exterior choice, orientation and exact construction rule `K_rule` | `UNRESOLVED` |
| scale | fixed normalization or an explicit quotient by scale, chosen before classification | `UNRESOLVED` |
| admissibility | decidable exact predicate `Adm` on every candidate | `UNRESOLVED` |
| equivalence | exact intertwiner group and preserved structures; treatment of carrier, generator and orientation relabeling, sign, rescaling, similarity, isometry and spectral equality | `UNRESOLVED` |
| completeness | deterministic ordering and classification algorithm, exhaustive finite bound or proof of reduction, certificate schema and exact certificate checker | `UNRESOLVED` |

## Scale obstruction that must be decided, not computed around

If the future admissible class contains both `K_hist` and `2 K_hist`, and
equivalence preserves `Tr(K^2)`, then the two candidates are inequivalent:

```text
Tr((2 K_hist)^2) = 4 Tr(K_hist^2) = -881/2 != -881/8.
```

Thus uniqueness is impossible on that surface unless scale is fixed or
explicitly quotiented. This is a conditional obstruction, not a present
`NONUNIQUE` result.

## Acceptance test before enumeration exists

The lane may move from `STOP` to `READY` only when all of the following are
publicly reviewable before any classification output:

1. `S` contains no unresolved carrier, normalization, operator, equivalence,
   algorithm, or completeness-method choice;
2. `Adm` is an exact decidable predicate on every candidate;
3. `Equiv` is an exact equivalence relation and its certificate schema and
   checker are frozen without supplying a result-dependent class count;
4. the deterministic ordering, exhaustive finite bound or reduction proof,
   and class-enumeration algorithm are frozen;
5. the historical witness either appears by the frozen predicate or is
   excluded by a stated pre-output rule;
6. no expected trace, rank, spectrum, class count or certificate instance is
   used to choose the surface;
7. the L1-to-L2 interpretation remains owned by the existing registered gate
   `GATE-L1-L2-CURVATURE-CANONICAL`;
8. all four probe outcomes remain reachable under the frozen definitions.

Any missing definition leaves the lane at `STOP`. A convenient operator found
after enumeration may not be inserted into the class retroactively.

## Future formal routing, still forbidden

Only after a reviewed definition freeze may a separate commit create:

```text
branch: probe/P-CURVATURE-OPERATOR-CANONICAL-1
path:   probes/P-CURVATURE-OPERATOR-CANONICAL-1/
```

The immutable preregistration must preserve these probe outcomes:

```text
EMPTY       zero admissible equivalence classes
UNIQUE      exactly one admissible equivalence class
NONUNIQUE   at least two admissible equivalence classes
STOP        incomplete, inexact, or non-reproducing classification
```

These are probe outcomes, not public status labels. Any later registry move
belongs to a separate reviewed Canon fold. `NONUNIQUE` is a valid negative
closure and must be preserved. It does not authorize an output-selected
selector. A later selector, if genuinely needed, would require its own prior
public definition and cannot be smuggled into this lane.

## Debt firewall

This note does not promote the historical operator, infer continuum or
physical curvature, choose a spectrum, fit a normalization, change the
frontier count, or edit the Canon. It turns the existing `STOP` row into one
finite definition package and one future classification under the existing
registered gate.
