# MINIMAL-READ: conditional selection depends on the coefficient ring

- **Working item:** C-MINIMAL-READ-CONDITIONAL-TABLE-N
- **Owner item:** MINIMAL-READ-DERIVATION [O]
- **Author:** A. M. Thorn, drafted with an AI agent session
- **Date:** 22 September 2026; publication review incorporated 23 September 2026
- **Scope:** PUBLIC, NON-CANONICAL; no authority; no probe. Proposal for an
  owner decision. The registered row remains O and STOP.
- **Scientific ceiling:** candidate-T for the conditional algebra below;
  candidate-D for the proposed physical dictionary. Neither is a closure
  of the complete registered decoder obligation.

Basis: Public Canon v91. The inputs are two T rows of `canon/REGISTRY.tsv`:

- **COIN-SELECTION-CONDITIONAL [T].** The positive-orientation
  integer-admissible alternator coins are exactly `{beta_1, beta_3}`.
  `beta_1` has generic/rung multiplicities 2/1, and `beta_3` has 6/5.
- **READ-REDUNDANCY-PRIME-SUPPORT [T].** For anonymous total polynomial
  accumulators with coefficients in the localization `Z_S`, multiplicity
  `m` carries iff every prime divisor of `m` lies in `S`. Over `Q` every
  multiplicity carries, and dropping totality removes every bound. The
  row informs MINIMAL-READ-DERIVATION and closes it in neither direction.

## Clauses the proposed accumulator class would have to fix

For each positive multiplicity `m`, declare a characteristic-zero integral
domain `R` and the following complete accumulator class:

```text
R1  F is symmetric in its m inputs (anonymous reads).
R2  F is total from R^m to R and satisfies F(t,...,t)=t for every t in R.
R3  F belongs to R[x_1,...,x_m]: its coefficients, not only its values,
    must lie in the declared ring R.
R4  Choose R=Z[S^(-1)], explicitly the localization that inverts the
    primes in S, and separately choose S={2} (or S={2,5} if the write
    place is additionally admitted in this proposed read dictionary).
```

The association in R4 with TWO-PLACE-PHYSICS [D] is an additional dictionary
choice. The label `v_2` does not itself select this localization, the
polynomial family, or the accumulator domain and codomain.

## Exact unit criterion (candidate-T)

Write the common coefficient of the linear monomials `x_i` as `c`.
Symmetry makes it the same for every `i`. Substituting `x_i=t` gives a
univariate polynomial whose coefficient of `t` is `m c`. The identity
`F(t,...,t)=t` holds over the infinite integral domain `R`, hence it is a
polynomial identity. Its degree-one coefficient gives

```text
m c = 1 in R.
```

Thus the positive integer `m`, embedded in `R`, must be a unit.
Conversely, if `m` is a unit, the polynomial

```text
F(x_1,...,x_m) = (x_1+...+x_m)/m
```

belongs to `R[x_1,...,x_m]`, is symmetric and total on `R^m`, and has the
required diagonal identity. This proves necessity and sufficiency for the
stated polynomial class. It selects no physical coefficient ring.

## Conditional localization table

A coin passes this accumulator test iff all of its generic/rung
multiplicities carry. For `R=Z[S^(-1)]`:

| S | beta_1 (2, 1) | beta_3 (6, 5) | Conditional accumulator selection |
|---|---|---|---|
| 2 not in S | no | no | Neither coin passes this class |
| 2 in S, {3, 5} not both in S | yes | no | Only beta_1 passes |
| {2, 3, 5} subset of S | yes | yes | Both coins pass; this test is nonunique |

This is the original prime-support table with its coefficient ring made
explicit. For `S={2}` or `S={2,5}`, only `beta_1` passes. If only the
generic multiplicity were included in a different contract, `beta_3`
would need `{2,3}` instead; the conclusions at those two choices of `S`
would be unchanged. Such a change must be declared, not inferred.

Arithmetic: `2=2`, `1` has no prime divisor, `6=2*3`, and `5=5`.

## Localization is not a 2-adic coefficient ring

For `S={2}`, `Z[S^(-1)]=Z[1/2]`. It is neither the 2-adic integers `Z_2`
nor the 2-adic field `Q_2`. Applying the same unit criterion gives:

| Coefficient ring R | Admitted positive integer multiplicities | beta_1 (2, 1) | beta_3 (6, 5) |
|---|---|---|---|
| Z[1/2] | Powers of 2, including 1 | yes | no |
| Z_2 | Odd integers | no | no |
| Q_2 | Every positive integer | yes | yes |

Indeed, `1/2` belongs to `Z[1/2]` but not `Z_2`, whereas `1/3` belongs to
`Z_2` but not `Z[1/2]`; both belong to `Q_2`. The conditional table over
the localization survives. Its interpretation as a consequence of the
phrase "2-adic read place" alone does not.

## Why domain and codomain alone are insufficient

The coefficient condition `F in R[x_1,...,x_m]` is essential. Consider

```text
F(x,y) = (x+y+(x-y)^2)/2 in Q_2[x,y].
```

This polynomial is symmetric and `F(t,t)=t`. For all `x,y in Z_2`, reduction
modulo 2 gives `(x-y)^2 = x+y`, so its numerator is divisible by 2 and
`F(x,y)` belongs to `Z_2`. Thus `F:Z_2^2 -> Z_2` is total even though
the expanded coefficients of `x`, `y`, `x^2`, and `y^2` equal `1/2`,
which is not in `Z_2`. This integer-valued polynomial lies outside
`Z_2[x,y]` and does not contradict the unit criterion. A contract that
states only the map's domain and codomain would admit it and would not
support the displayed `Z_2` exclusion.

Dropping polynomiality changes the family as well. On the ordered
localization `Z[S^(-1)]` inside `Q`, the minimum or maximum of the inputs
is a total symmetric diagonal-preserving map for every multiplicity.
This example does not assume a compatible order on `Z_2` or `Q_2`.

## Owner decision and remaining obligation

The proposed shortest route is to adopt the complete accumulator contract
R1 to R4 explicitly, justify its cover-to-output use, and supply the full
typed L5-read to L1-coin selection route with its dependency graph. The
conditional unique survivor is then `beta_1`; the selection depends on
the declared coefficient-ring and polynomial-family choices. No theorem
selecting those choices from `v_2` has been supplied.

Such a physical dictionary route has ceiling D. It does not adopt a
minimal-cost principle, and the prime-support selector can select larger
multiplicities in other families. Nevertheless, the registered parent
requires completeness of the whole admissible decoder class, its carrier,
maps, accumulator/equality rule, graph and layer typing. This note alone
does not supply those requirements or close that parent positively.

Likewise, admitting two accumulator realizations or removing R3 does not
close the parent negatively until fully compliant realizations are proved
inside the complete registered decoder class. The localization table,
the p-adic alternatives and the integer-valued boundary example delimit
the proposal; they do not silently replace the existing public contract.
