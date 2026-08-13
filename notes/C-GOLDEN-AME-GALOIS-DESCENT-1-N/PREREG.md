# C-GOLDEN-AME-GALOIS-DESCENT-1-N — preregistration

Status: **NON-CANONICAL INCUBATION**  
Target line: **PUBLIC**  
Layer: **L1 exact algebra and finite gauge classification only**  
Created: 2026-08-13  
Lock: [issue #365](https://github.com/mathorn1973/twist-j/issues/365)  
Canon writes: **forbidden**  
Formal hypothesis computation before this pin: **none**

## 1. Question

The earlier incubation `C-GOLDEN-AME-TWOPLACE-1-N` proved that the pinned
golden AME(4,6) representative has minimal entry field

```text
K = Q(zeta_40) = Q(zeta_5,zeta_8),  [K:Q] = 16,
```

but refuted its proposed six-line `A5` bridge inside a local monomial class.
That negative result is final in its scope and is not reopened here.

This incubation asks a different question.  Although the printed entries
need all of `K`, can the **local-monomial equivalence class** of the four-party
tensor descend to a proper fixed field?  Equivalently, which Galois conjugates
of the tensor are locally monomially equivalent to it, and do the resulting
equivalences satisfy a coherent descent cocycle?

This is not an `A5` test.  `Gal(K/Q)` has order 16 and no element of order five;
Galois automorphisms may also exchange the amplitude labels `a` and `b`.
Therefore the order-five support-degree obstruction from the earlier
incubation does not answer this question.

## 2. Frozen authority and source

| Item | Frozen value |
|---|---|
| Canon | Public Canon v46 |
| Authority | `mathorn1973/twist-j` `main` |
| Tag | `canon-v46` |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| `canon/CANON.md` SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |
| `canon/CANON.md` bytes | `222760` |

The sole matrix input is `matrix-toolbox/AME_4_6` at commit
`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`, file
`AME46_ORIGINAL.m`, Git blob
`e0d0e171d58b3360c39595d677ffc401a466112d`, 8515 bytes, SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.
The source is parsed directly; numerical MATLAB output is not evidence.

Use zero-based indices and

```text
A[i,j,k,l] = U[6i+j,6k+l].
```

The exact coefficient model is

```text
z = zeta_40,
w = z^2 = zeta_20,
c = (z^5+z^-5)/2,
a = c/(w+w^-1),
b = (w^2+w^-2)a.
```

The Galois group is indexed by

```text
G = (Z/40Z)^x,
sigma_k(z) = z^k,
k in {1,3,7,9,11,13,17,19,21,23,27,29,31,33,37,39}.
```

Its frozen CRT generators are `3` (order four), `17` (order two), and `21`
(order two).  Their subgroup closure must be verified rather than assumed.

Relevant Canon facts are only `PLENUM-POINT [T]`, `Z2-PLACES-SPLIT [T]`, and
the exact arithmetic defining the two cyclotomic places.  `TWO-PLACE-PHYSICS
[D]` is not promoted or used as an operator or selection principle.

## 3. Frozen gauge and equivalence relation

The four tensor parties remain labeled.  The primary gauge group is the
projective local monomial group

```text
H_40 = ((mu_40^6 semidirect S_6)^4) / mu_40_global.
```

Thus a witness from `A` to `sigma_k(A)` consists of four permutations
`p_q in S_6`, 24 diagonal exponents `d_q(r) in Z/40Z`, and one global exponent
`h in Z/40Z`, satisfying for every tensor index `x=(x_0,...,x_3)`

```text
sigma_k(A[x]) = z^h z^(sum_q d_q(p_q(x_q)))
                A[p_0(x_0),...,p_3(x_3)].
```

Changing all exponents by a projectively trivial scalar is quotient gauge.
No arbitrary local unitary, arbitrary `GL_6`, phase outside `mu_40`, change of
tensor representative, or relabeling chosen after a failure is permitted.

A secondary **unlabeled-party audit** may additionally enumerate `S_4` leg
permutations, reported separately.  It cannot repair failure of the primary
labeled-party descent question.

## 4. Definitions to classify

Define the transporter set

```text
T_k = { M in H_40 : M.A = sigma_k(A) }.
```

The Galois stabilizer of the gauge orbit is

```text
G_mod = { k in G : T_k is nonempty }.
```

Its fixed field `K_mod = K^G_mod` is the **field of moduli in the frozen
gauge class**.  This is distinct from the already proved field of entries.

A coherent descent datum to `K^H`, for a subgroup `H <= G_mod`, is a choice
`M_k in T_k` for every `k in H`, with `M_1=1`, satisfying the semilinear
cocycle law

```text
M_(kl) = sigma_k(M_l) M_k
```

in the projective gauge quotient.  The automorphism `sigma_k` acts on every
phase exponent by multiplication by `k` and fixes permutations.  Existence of
individual transporters is field-of-moduli evidence only; it is not descent.

## 5. Complete finite algorithm

### 5.1 Support and amplitude transporters

For each `k`, apply `sigma_k` exactly in `Q[z]/Phi_40(z)` to every nonzero
entry.  Classify its amplitude orbit and residual `z` exponent without
floating point.  Enumerate all independent local permutations that preserve
the four one-coordinate degree vectors and then retain exactly those that map
the full support and Galois-transformed amplitude labels.  Degree partitions
are a pruning device only; completeness is certified by reporting every
candidate count and independently brute-forcing every resulting finite
Cartesian product.

### 5.2 Phase lift

For each surviving permutation tuple, form the 112 exact congruences in 25
variables over `Z/40Z` (24 local phases plus global phase).  Decide solvability
separately over `Z/8Z` and `Z/5Z`, then combine by CRT.  Record ranks and an
explicit left-null inconsistency certificate modulo 2 or 5 for every rejected
class, or one normalized phase solution plus a kernel basis for every lift.
Substitution into all 112 exact entries is mandatory.

### 5.3 Group and fixed field

Compute all 16 transporter sets, not just the three generators.  Verify by
composition that `G_mod` is a subgroup.  Identify it as a subgroup of
`(Z/40Z)^x`, list its elements, and determine the fixed field by exact traces
or orbit sums.  State separately:

1. field of printed entries `K`;
2. field of moduli `K_mod` in this gauge;
3. any field of definition established by coherent descent.

### 5.4 Coherence obstruction

Let `Aut_H(A)=T_1`.  From the complete transporter cosets, solve the cocycle
equations for the frozen generators of every subgroup of `G_mod`, including
their order and commutation relations.  Quotient choices by coboundaries from
`Aut_H(A)`.  A nontrivial defect must be printed as an explicit element of
`Aut_H(A)` and checked on all entries.  No coherent descent may be inferred
from pairwise equivalence alone.

## 6. Frozen gates

**G0 — source and field replay.** Reproduce the pin, 112-entry support, exact
2-unitarity, and `Q(entries)=Q(zeta_40)` using the previously published exact
identities.  A mismatch is integrity STOP.

**G1 — Galois action.** Enumerate the 16 units modulo 40, verify the group
structure and the exact action on `a,b,c,w`, and hash the 16 conjugate tensors.

**G2 — complete transporters.** Execute sections 5.1 and 5.2 for every `k`.
Publish exact candidate counts, transporter counts, witnesses, and
inconsistency certificates.

**G3 — field of moduli.** Determine `G_mod` and `K_mod` exactly.  Failure of
even one `k` is a negative for descent through that automorphism, not a global
failure for smaller subfields.

**G4 — coherent descent.** Classify projective cocycles and coboundaries for
every subgroup of `G_mod`; determine the maximal subgroups for which coherent
data exist and the corresponding fields of definition inside this frozen
gauge.

**G5 — party audit.** Repeat G2 with `S_4` leg permutations as a secondary
classification.  Keep labeled and unlabeled conclusions distinct.

**G6 — output.** Publish exact scripts, stdout, hashes, certificates, and a
scoped result.  Create no `PROMO.md` unless a nontrivial coherent descent
survives and is independently reproduced.  No Canon edit is authorized.

## 7. Hard falsifiers and stop rules

1. Any pin, parser, field, or 2-unitarity mismatch is integrity STOP.
2. If `T_k` is empty, descent through `sigma_k` fails in the frozen gauge;
   phases cannot repair a support/amplitude failure.
3. If transporters exist but no generator choices satisfy the cocycle laws,
   field of moduli does not imply field of definition; record the exact
   obstruction and stop the proposed descent at G4.
4. A result depending on arbitrary local unitaries, phases outside `mu_40`,
   an unregistered representative, numerical tolerance, or a post-hoc widened
   permutation class fails scope.
5. Coincidence of fields, equality of conjugate spectra, or pairwise local
   equivalence alone is not coherent descent.

## 8. Interpretation firewall

Positive outcomes are exact L1 statements about one tensor's arithmetic gauge
orbit.  They do not connect it to the six golden lines, `A5`, color, a decoder,
Born probability, fault-tolerant hardware, or physical write/read operations.
Negative outcomes are confined to `H_40`; they do not exclude arbitrary local
unitary equivalence or the separate artisanal `9+27` Clifford construction.
