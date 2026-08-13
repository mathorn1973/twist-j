# C-GOLDEN-AME-A5-LU-COVARIANTS-2-N — result

Status: **NON-CANONICAL, exact scoped negative**

Decision: **the frozen `n=4` Schur hard breaker fires**

Canon change: **none**

`PROMO.md`: **not created**

## Verdict

The pinned golden AME(4,6) tensor admits no local-unitary action

```text
rho_q : A5 -> U(6),  rho_q unitarily equivalent to 1+5,
(rho_0(g) tensor rho_1(g) tensor rho_2(g) tensor rho_3(g)) A = A
```

within the exact scope frozen in the preregistration.  This includes arbitrary
complex local changes of basis and is strictly wider than the earlier
monomial no-go.

The first hard witness in the frozen order occurs on leg `q=0`, irreducible
graph

```text
R1 = (1032,2310,3201).
```

Let its exact one-leg covariant be `M`.  Reduction at `zeta_40 -> 6 in F_41`
gives

```text
M = diag(4,19,19,1,1,4).
```

The unital star-algebra already contains `I,M,M^2`.  Flatten them as three
rows and select positions `(0,0),(1,1),(3,3)`.  The resulting determinant is

```text
31 mod 41 != 0.
```

Hence the generated algebra has dimension at least three.  Under any scoped
`1+5` action, Schur's lemma would require it to lie in
`End_A5(1+5)=C direct-sum C`, which has dimension two.  Contradiction.

Independently, the exact matrix is diagonal with three distinct eigenvalues,
each of multiplicity two.  The forbidden multiplicity split `2+2+2` is a
second Schur contradiction: every nonscalar Hermitian element of
`C direct-sum C` has split `1+5`.

## Gate ledger

| Gate | Result | Exact scope |
|---|---|---|
| G0 public pin and replay | **PASS** | pin commit/tree/prereg hash, 8515-byte source, 112 support entries, prior exact source/2-unitarity/field replay |
| G1 graph quotient | **PASS** | 82944 raw diagrams per leg, 2345 dummy-copy orbits, 2341 exact double-edge reductions, four irreducible cores |
| G2 `F_41` locator | **PASS, HARD WITNESS FOUND** | all 16 primary matrices and all 16 independently contracted stars; first frozen witness `q=0,R1` |
| G3 exact certificate | **PASS** | exact `Q(zeta_40)` lift, nonzero 16-coefficient minor, denominators prime to 41, two contraction orderings, exact star audit |
| G4 verdict | **EXACT NO** | all arbitrary-local-unitary `1+5` actions in the frozen scope |

## Frozen graph reduction

For `n=4` there are

```text
3! * (4!)^3 = 82944
```

raw diagrams per leg.  Normalizing the open-leg matching leaves `24^3=13824`
ordered triples, with simultaneous conjugation by `S3` fixing copy zero.
Burnside's count is

```text
(24^3 + 3*4^3 + 2*3^3)/6 = 2345.
```

Exactly 2341 orbits have a double edge and reduce by one exact 2-unitarity
identity to the previously classified `n<=3` family.  The four new connected
orbits are

```text
R0=(1032,2301,3210), R1=(1032,2310,3201),
R2=(1230,2301,3012), R3=(1230,3012,2301).
```

No tensor leg or color was quotiented.  The reduction uses only dummy-copy
relabeling and exact 2-unitarity.

## Complete modular census

All 16 matrices, not only the early witness, were computed.  Every star was
contracted independently as `C(bar(A),A)^T` and equals its predicted
self-adjoint primary matrix.

| leg | core | scalar or diagonal summary mod 41 | matrix SHA-256 |
|---:|---:|---|---|
| 0 | R0 | `19 I` | `5b1bc285a24fe0eec8f6eea3efb38425bd1c944aa5db6ef8a2a3c0cc3697dec4` |
| 0 | R1 | `diag(4,19,19,1,1,4)` | `08d667a0f9443f5c7498d9fea23c2500d9a50ff6c4c260b6f82944d621aed3cd` |
| 0 | R2 | `9 I` | `cca64882dc13ee88752689ed5990f53aa42f95ff0b01ba9c6c188dee51d74177` |
| 0 | R3 | `33 I` | `bde5b5946da285399cf6fde588d993b8be17dfc4f70f4f0b6d164d9d76186358` |
| 1 | R0 | `19 I` | `5b1bc285a24fe0eec8f6eea3efb38425bd1c944aa5db6ef8a2a3c0cc3697dec4` |
| 1 | R1 | `diag(19,1,1,4,4,19)` | `b868eab7f4d5417b3382a340ed75857eed33b26f77fb738c8a5619928df745df` |
| 1 | R2 | `33 I` | `bde5b5946da285399cf6fde588d993b8be17dfc4f70f4f0b6d164d9d76186358` |
| 1 | R3 | `9 I` | `cca64882dc13ee88752689ed5990f53aa42f95ff0b01ba9c6c188dee51d74177` |
| 2 | R0 | nonscalar; 6 off-diagonal nonzeros | `5b30c3c23847f9dec5abef9ec816a394d76bb74e6b129677d1489429d34ffcea` |
| 2 | R1 | nonscalar; 6 off-diagonal nonzeros | `ee725d04e21559f3a6a99be6cdf61ff4031e03c17e14aa3fee31ecdbb5d48bc4` |
| 2 | R2 | nonscalar; 6 off-diagonal nonzeros | `81f61b459b35058be6cd7cce5fd96c83b1bbe239e0e9e5ba8f2c1808bcb0f4b3` |
| 2 | R3 | nonscalar; 6 off-diagonal nonzeros | `0d07752c6071cf43c2058c4643b4f84e01359bacf45b820350d260288c789427` |
| 3 | R0 | nonscalar; 6 off-diagonal nonzeros | `f38f93d73a09abe6a44585acc030b844a8242fc6a142b8990acf9065a29ddd89` |
| 3 | R1 | nonscalar; 6 off-diagonal nonzeros | `2aa831ffd519c171de66e4efa7e9413c28d9e9d3bd52555f74ae62a53f53cdd6` |
| 3 | R2 | nonscalar; 6 off-diagonal nonzeros | `1d0899a3e3f110ac6bf2da6164958c26d6c13ba1c636d9df3ec10db45818a2f0` |
| 3 | R3 | nonscalar; 6 off-diagonal nonzeros | `9dd3297e8f9fbc7a710c642c3ddc42dbb32a290169585e1b5eda30c1c1d5658a` |

`MODULAR_RESULT.json` contains all 32 complete matrices, including the 16
independently evaluated stars.

## Exact witness

Write `z=zeta_40`.  The exact `R1` matrix is diagonal.  Its three distinct
diagonal values occupy index pairs `{0,5}`, `{1,2}`, and `{3,4}`.  Their
power-basis coefficients are printed in `EXACT_WITNESS.json`; therefore the
exact eigenvalue multiplicities are `2+2+2`.

The exact minor for `I,M,M^2` is

```text
(1/256) + (3/256)z^2 - (3/512)z^6 - (1/512)z^8
+ (3/512)z^10 + (1/512)z^12 - (3/512)z^14.
```

It reduces to `31 mod 41`, so it is nonzero exactly.  The common denominator
LCM of the witness matrix and minor is `512`, which is prime to 41.  The
reduction homomorphism is therefore defined.

The exact sparse verifier contracts the same graph through two different
binary trees.  The complete 36-entry matrices agree.  It separately computes
`C(bar(A),A)^T` and obtains the same exact matrix.

## Boundary

This result refutes only the stated diagonal `A5` action with each local
representation unitarily equivalent to `1+5`.  It does not refute the AME
construction, arbitrary perfect-tensor equivalence, other local
representations, non-diagonal group actions, the Gross--Goedicke artisanal
solutions, or any physical interpretation.  It changes no Canon or Registry
claim and supplies no decoder, Born rule, error-correction theorem, or
hardware statement.
