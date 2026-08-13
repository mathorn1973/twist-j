# C-GOLDEN-AME-A5-LU-COVARIANTS-2-N — preregistration

Status: **NON-CANONICAL INCUBATION**  
Layer: **L1 exact invariant theory**  
Lock: [issue #367](https://github.com/mathorn1973/twist-j/issues/367)  
Created: 2026-08-14  
Canon writes: **forbidden**

Formal golden-tensor computation before this pin: **none**

## 1. Question and continuation boundary

The first incubation scanned every frozen balanced one-leg diagram with
`n<=3` at `z -> 6 in F_41`.  Its locator did not fire: all reductions were
scalar modulo 41.  That result is `INCONCLUSIVE`, not evidence for an `A5`
action.  The frozen prior result commit is
`496360925534050f782d65cfda0c2b61b79ad62b`.

This continuation tests the first genuinely new contraction topology at
`n=4`.  Its target class is unchanged:

```text
rho_q : A5 -> U(6), rho_q ~= 1+5,
(rho_0(g) tensor ... tensor rho_3(g)) A = A.
```

The four local conjugating unitaries remain arbitrary.  No monomial basis,
six-line incidence map, or field of definition for `rho_q` is assumed.

Before the public pin, only the tensor-independent colored-graph quotient and
a generic-array contraction engine were computed.  The golden tensor and its
support were not loaded by this design computation.

### Authority and tensor source

| Item | Frozen value |
|---|---|
| Canon | Public Canon v46 |
| Authority | `mathorn1973/twist-j` `main` |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| Canon SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |

The sole post-pin tensor input is `matrix-toolbox/AME_4_6` commit
`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`, file `AME46_ORIGINAL.m`,
8515 bytes, Git blob `e0d0e171d58b3360c39595d677ffc401a466112d`, SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.
Use `A[i,j,k,l]=U[6i+j,6k+l]` without a preliminary gauge change.

## 2. Frozen `n=4` graph model

Fix the open leg `q`.  There are four labeled `A` vertices and four labeled
`bar(A)` vertices.  The open-leg color gives a matching on copies `1,2,3`;
the other three colors give perfect matchings on `0,1,2,3`.  Hence the raw
count is

```text
3! * (4!)^3 = 82944 per leg.
```

Independent relabelings of the closed `A` and `bar(A)` copies act by

```text
p_c -> beta p_c alpha^-1,  alpha,beta in S3 fixing 0.
```

Normalize the open-leg matching `p_q` to the identity and set
`tau_c=p_q^-1 p_c` for the other colors.  The residual action is simultaneous
conjugation of the ordered triple `(tau_1,tau_2,tau_3) in S4^3` by `S3`
fixing 0.  Burnside's lemma gives

```text
(24^3 + 3*4^3 + 2*3^3)/6 = 2345 orbits per leg.
```

The four tensor legs and the three remaining colors stay labeled.  No party
or color permutation is quotiented.

## 3. Exact double-edge reduction

A double edge is a pair `(A_r,bar(A)_s)` joined by at least two distinct
colors.  Contracting either two shared colors invokes exactly one of the six
2-unitarity identities.  It deletes those two tensor vertices and splices
the two remaining colors.  Every additional shared color becomes a closed
dimension-six loop.

- If the deleted pair does not contain both open endpoints, the result is a
  balanced one-leg `n=3` diagram, after dummy-copy relabeling.
- If it contains both open endpoints, the result is `I_6` times a closed
  scalar `n=3` network.

This is an exact tensor identity, not a heuristic connectedness filter.  The
prior result proves, by exact 2-unitary induction rather than modular
vanishing, that every resulting `n<=3` one-leg diagram is scalar.  Thus a
double-edge `n=4` diagram contains no new Schur-algebra information.

Complete graph enumeration gives, after normalizing `p_q`,

```text
13824 labeled triples
13800 with a double edge
   24 double-edge-free
```

and after the residual `S3` quotient,

```text
2341 reducible orbit representatives
   4 irreducible orbit representatives per leg.
```

All four irreducible graphs are connected and have trivial residual
automorphism.  In one-line permutation notation, their ordered triples are

```text
R0 = (1032, 2301, 3210)
R1 = (1032, 2310, 3201)
R2 = (1230, 2301, 3012)
R3 = (1230, 3012, 2301).
```

Their frozen ordered-list SHA-256 is

```text
df5a7d9f6d3454119cc7eaf066a42e1382232c442f3ab69e6906319bde0f6134.
```

The complete 2345-representative list has SHA-256

```text
06b887026919ba24f95592fd125e0608033337634def90fdbd8c08e18bc99020.
```

The star involution sends an ordered triple to the canonical orbit of its
componentwise inverse.  Each `R0,...,R3` returns to its own orbit.  Its
covariant is therefore formally self-adjoint by dummy-copy relabeling.  The
post-pin scan nevertheless evaluates `C(bar(A),A)^T` independently as an
orientation audit and asserts equality before reuse.

## 4. Frozen modular scan

After the public pin only, parse the same pinned AME source and replay the
first incubation.  Reduce at

```text
z -> 6 in F_41, bar(z) -> 6^-1.
```

For each `q=0,1,2,3`, compute `R0,R1,R2,R3` in that order.  Audit the star
correctly as

```text
C(A,bar(A))^star = C(bar(A),A)^T;
```

ordinary transpose at the same residue is not a substitute for cyclotomic
conjugation.

Maintain the unital star-algebra generated by the matrices on each leg,
starting with `I_6`.  After every new matrix, use this frozen priority:

1. first row-major nonzero entry of a commutator;
2. first three-dimensional span, certified by the lexicographically first
   nonzero `3 x 3` minor of flattened matrices;
3. closure under multiplication and star, stopping at dimension three;
4. record the first nonscalar matrix even if none of 1--3 fires.

A nonscalar matrix alone is not a Schur violation: `C direct-sum C` contains
nonscalar matrices.  It becomes a hard witness only through a nonzero
commutator, star-algebra dimension greater than two, or an exact spectral
multiplicity violation.

For an optional spectral locator, an allowed exact matrix has characteristic
polynomial `(t-lambda)(t-mu)^5`.  At the split prime its reduction may have
multiplicities `(1,5)` or may coalesce to `(6)`.  No other modular
multiplicity pattern is compatible.  Any spectral locator must still be
lifted as required below.

## 5. Frozen contraction path and complexity

For every core use the same pairwise tree

```text
X03 = contract(A0,B3)             # one shared wire, rank 6
X32 = contract(A3,B2)             # one shared wire, rank 6
X   = contract(X03,X32)           # two shared wires, rank 8
X21 = contract(A2,B1)             # one shared wire, rank 6
X   = contract(X,X21)             # four shared wires, rank 6
X   = contract(X,A1)              # three shared wires, rank 4
C   = contract(X,B0)              # three shared wires, rank 2
```

Subset dynamic programming certifies that this is optimal among binary
paths without outer products both in total dense arithmetic and maximal
rank.  Per representative it uses

```text
122059872 modular multiply-adds,
maximum rank 8 = 6^8 = 1679616 residues,
about 12.8 MiB per largest int64 array before temporaries.
```

There are only `4*4=16` primary matrices; the independently evaluated stars
must agree with them by the frozen graph involution.  A generic-array
benchmark reaches a hard witness after two contractions in under one second
on the design host; this timing is advisory and not a gate.

## 6. Gates

**G0 — public pin and replay.** Freeze the previous result commit, source,
this preregistration, the four representatives, scripts, and hashes.  Replay
the source pin, exact 2-unitarity, and all `n<=3` modular outputs.

**G1 — graph quotient.** Independently reproduce the raw count, Burnside
count 2345, all 13824 normalized triples, the double-edge rewrite on every
one of the 13800 reducible triples, and the four irreducible representatives.

**G2 — `F_41` locator.** Compute the 16 primary irreducible matrices and
independently contracted stars in frozen order; assert the graph-predicted
self-adjoint equality.  Publish matrices, hashes, scalar tests,
commutators, span dimensions, closure steps, and any modular minor.

**G3 — exact certificate.** For the first hard modular locator, publish the
complete descriptors and show that the reduction homomorphism from the
41-integral coefficient model to `F_41` is defined at every denominator.  A
nonzero residue is already an exact
nonvanishing certificate.  In addition, recompute the cited entry or minor
in `Q(zeta_40)` and publish its 16 power-basis coefficients.  Verify the same
diagram through an independent contraction ordering.  A resource failure at
this gate gives `NO VERDICT`, not a negative result.

**G4 — verdict.** A G3-certified nonzero commutator, dimension-three minor,
or exact forbidden spectrum gives `EXACT NO` for every scoped arbitrary-local-
unitary `1+5` action.  If all four cores on all legs fail to locate a hard
witness, the result is `INCONCLUSIVE`.

## 7. Firewalls

- No golden-tensor value may be computed before the public pin.
- The four-core quotient uses only dummy-copy relabeling; it does not quotient
  tensor legs or colors.
- Double-edge removal uses the separately proved exact `n<=3` scalar theorem;
  it does not infer exact vanishing from a modular zero.
- A first nonscalar covariant is not by itself a negative result.
- A modular zero is not evidence of exact zero.
- No result promotes the six-line frame, color, a decoder, Born probability,
  error correction, hardware, or any L2--L6 statement.
