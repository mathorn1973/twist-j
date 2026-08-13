# C-GOLDEN-AME-A5-LU-COVARIANTS-1-N — result

Status: **NON-CANONICAL, INCONCLUSIVE**

Decision: **the frozen `n<=3` breaker is structurally blind on every
four-party perfect tensor**

Canon change: **none**

`PROMO.md`: **not created**

## Verdict

The preregistered arbitrary-local-unitary `A5` test does not decide the
hypothesis.  All 32 degree-four (`n=2`) and all 1728 degree-six (`n=3`)
one-leg covariants are scalar.  Consequently there is no nonzero commutator,
third independent matrix, or spectral `1+5` violation in the frozen family.

This is not evidence for an `A5` action.  Exact 2-unitarity forces the same
scalarity for every four-party perfect tensor at `n<=3`; it is therefore a
structural limitation of this contraction family.  The first degree not
covered by the obstruction is `n=4`.

## Gate ledger

| Gate | Result | Scope |
|---|---|---|
| G0 source and AME replay | **PASS by exact replay** | pinned 8515-byte source, 112 nonzero entries, exact unitarity of all three flattenings, entry field `Q(zeta_40)` |
| G1 covariance and census | **PASS** | exact index proof; 8 plus 432 diagrams per leg; no connectedness filter |
| G2 finite-field locator | **NO FIRE** | all 1760 matrices scalar modulo 41; two independent implementations |
| G3 exact witness | **NOT TRIGGERED** | no modular nonvanishing witness exists in the frozen family |
| G4 verdict | **INCONCLUSIVE** | neither an `A5` action nor its absence follows |

The exact G0 transcript is the immutable source/field replay published in
[`C-GOLDEN-AME-GALOIS-DESCENT-1-N`](https://github.com/mathorn1973/twist-j/tree/5d93967cd49ca48357f0ed61fe86d4434ea0d520/notes/C-GOLDEN-AME-GALOIS-DESCENT-1-N).
Its transcript SHA-256 is
`3ed4587d8526cc3625cfbceefa4a8ab66983795c0bd90111e7486dd296d964cb`.

## G1 — covariance

Under `A'=(V_0 tensor ... tensor V_3)A`, every closed wire contains one
matrix entry of `V_ell` and one conjugate entry.  Unitarity cancels them:

```text
sum_x V_ell[x,a] conjugate(V_ell[x,b]) = delta(a,b).
```

All closed local actions therefore disappear.  The two open indices on leg
`q` retain `V_q` and `V_q^dagger`, giving exactly

```text
C_q(A') = V_q C_q(A) V_q^dagger.
```

The verifier also checks this identity on all 1760 orientations for a
generic finite-field tensor and a deterministic tuple of nonmonomial
orthogonal matrices.

## Why every frozen diagram is exactly scalar

Make the balanced contraction into a bipartite multigraph: `n` vertices are
the copies of `A`, `n` vertices are the copies of `bar(A)`, and every closed
wire is an edge.  There are `4n-1` edges across only `n^2` opposite-vertex
pairs.

For `n=2` and `n=3`, respectively,

```text
7 > 4,
11 > 9.
```

Thus some `A`/`bar(A)` pair shares at least two wires.  Exact 2-unitarity
contracts that pair to two Kronecker deltas.  The deltas splice the remaining
wires, possibly contributing a closed dimension factor or transporting an
open endpoint.  The result is the same kind of balanced diagram with one
fewer tensor pair.  Induction ends at a scalar multiple of `I_6`.

At `n=4`, however, `4n-1=15<=16=n^2`; a double edge is no longer forced.
That is the first potentially informative degree.

## Machine census

At the frozen good-prime map `zeta_40 -> 6 in F_41`, the residues are

```text
z=6, conjugate(z)=7, w=36, a=4, b=28, c=12.
```

The primary descriptor-list SHA-256 is
`eb08b19c49afaaeaec0c8720be2d25e71e0c527defa0363a9ab86b88bd7433f1`.
The scalar distributions, identical on every leg, are shown both exactly and
after reduction:

| `n` | exact scalar and multiplicity per leg | residues mod 41 |
|---:|---|---|
| 2 | `6 x 3`, `36 x 4`, `216 x 1` | `6,36,11` |
| 3 | `6 x 108`, `36 x 192`, `216 x 106`, `1296 x 24`, `7776 x 2` | `6,36,11,25,27` |

The ordered scalar transcript has SHA-256
`2fa27b3a510c696179c9a6b391811e70d2220fe5868f0928f220eb1ad6a78628`.
Exact 2-unitary reduction proves the class values, and one representative of
every residue class on every leg was also contracted directly in
`Q(zeta_40)`.  The independent implementation repeats the full census, verifies seven
dispersed `n=3` diagrams by direct sparse summation over support triples, and
produces byte-identical JSON on rerun.

## Boundary

This result diagnoses only the frozen `n<=3` one-open-leg covariant family.
It does not prove or refute arbitrary local-unitary `1+5` actions, general
perfect-tensor equivalence, the Gross--Goedicke artisanal constructions, a
six-line frame, a decoder, Born probabilities, or any physical claim.
