# C-TM-HANKEL-XOR-DEFECT-1

```text
STATUS:       NON-CANONICAL INCUBATION NOTE
AUTHORITY:    none
PUBLIC BASIS: Public Canon v41, mathorn1973/twist-j main
              tag canon-v41, content commit 096e97b44727830102846746f0c723af1c59a2cf
ISSUE LOCK:   none at claim; the pull request review is the public lock
LAYER:        L1 only; finite integer linear algebra on divisor cubes;
              no L2-L6 lift claimed
COMPUTATION:  exact integer verifiers, two platforms, byte-identical
              transcripts; SHA-256 pins in section 8
PROMOTION:    none; this note creates no Registry row, moves no status,
              and edits no Canon file
```

This note records one finished incubation arc. Every status word below is a
PROPOSAL carried by this note alone; `canon/REGISTRY.tsv` remains the only
authority, and where this note and the registry disagree, the registry wins.

Notation. `t(n) = (-1)^(s_2(n))` with `s_2` the binary digit sum, so
`t(1) = -1`; `c = mu * t` under Dirichlet convolution. The symbol tau is not
used. Public basis rows consumed: `MOBIUS-TM-PRIME2-BRIDGE` [T] (the odd
squarefree subset formula for `c` and even annihilation) and
`TM-MULTIPLICATION-CARRY-DEFECT` [T] (the carry parity law). For an odd
squarefree prime set `P`, `k = |P|`, subsets `S, T`, `n_S` the product,
`K_P(S,T) = c(n_S n_T)`, `Kxor_P(S,T) = c(n_(S XOR T))`, `R_P = K_P - Kxor_P`.
Inertia is written with named fields `NEG ZERO POS`. `P` is EXTREMAL when
`t(n_Z) = (-1)^(|Z|+1)` for every subset `Z`, the equality locus of the bound
`|c(n)| <= 2^k`.

## 1. Bridge (proposed T; proof included)

Let `H(m,n) = c(mn)/(mn)` on `ell2`. With `D_P = diag(n_S)` positive,
`(D_P H_P D_P)(S,T) = c(n_S n_T) = K_P(S,T)`, so by Sylvester
`inertia(H_P) = inertia(K_P)`: the integer matrix `K_P` carries the whole
inertia content of the divisor block. Since
`n_S n_T = n_(S XOR T) n_(S AND T)^2`, the block splits as
`K = Kxor + R` with `Kxor` an XOR circulant (Walsh-diagonalizable) and `R`
supported on pairs with `S AND T` nonempty.

## 2. Parity and the rank no-go (proposed T; proof included)

`c(1) = -1` is odd and `c(N)` is even for every `N >= 2`, because `c(N)` is a
sum of `2^(omega(N))` unit terms. This is table-general: it uses no property
of `t` beyond taking unit values. Hence the nonempty block of `R` is `I`
modulo 2, its determinant is odd, `rank R = 2^k - 1` exactly, and
`ker R = span(e_empty)`. The same parity gives, for every nonempty `U`, an
intersection-layer operator congruent to `I` modulo 2 and of full rank
`2^(k - |U|)`. Consequence: no low-rank compression of the squareful defect
exists, globally or at any single intersection order. The defect is
two-adically unimodular on its carrier.

## 3. Integral Witt form on the extremal locus (proposed T; proof included)

Let `W(S,T) = 2^(|T| - |S|)` if `S` is a subset of `T`, else 0; `W` is
unimodular and `I` modulo 2. On an extremal set,
`W^T Kxor W = diag((-1)^(|S|+1) 3^(|S|))`, an exact integer congruence: the
local identity is `u^T m u = diag(1, -3)` for `m = [[1,-2],[-2,1]]`,
`u = [[1,2],[0,1]]`, and `Kxor = -(m tensor k)` because the extremal cube is
`c(n_T) = -(-2)^(|T|)`. The empty direction splits off at the constant `-1`
for the entire pencil `Kxor + sR`, since the empty row of `W^T R W`
vanishes. The balance `NEG = POS = 2^(k-1)` of the skeleton reads off the
diagonal.

## 4. The k = 2 transfer theorem (proposed T; proof included)

For an extremal pair `{p, q}` put `A = t(p^2)`, `B = t(q^2)`, `D = t(p^2 q)`,
`E = t(p q^2)`, `F = t(p^2 q^2)`, all units. In the `W` basis the pencil
`Kxor + sR` becomes exactly

```text
[ -1   0      0      0                ]
[  0   3+sA   0      s(A+D)           ]
[  0   0      3+sB   s(B+E)           ]
[  0   s(A+D) s(B+E) -9+s(3D+3E+F)    ]
```

For `0 <= s <= 1` the two middle pivots are at least 2, and Schur elimination
leaves `h(s) = -9 + s(3D+3E+F) - s^2 (A+D)^2/(3+sA) - s^2 (B+E)^2/(3+sB)
<= -9 + 7s <= -2 < 0`. Hence the determinant never vanishes on `[0,1]` and
the inertia is constantly `NEG 2 ZERO 0 POS 2`, uniformly over all squareful
sign patterns. Universality of the balanced transfer therefore holds at
`k = 2`.

## 5. Falsification at k = 3 (proposed F content; exact witnesses)

Universality FAILS from `k = 3` on. The extremal triple `P = {5, 101, 293}`,
`n = 147965`, has `K` inertia `NEG 5 ZERO 0 POS 3`, determinant `-3840`, and
the pencil `det(Kxor + sR)` has exactly ONE root in the open interval
`(0, 1)`: an interior crossing, not an endpoint degeneracy. Among ALL 157
extremal triples with `n <= 200000` this is the unique nonbalanced case.
Two further witnesses: `{83, 89, 263}` (`n = 1942781`, determinant `-768`)
and `{149, 269, 293}` (`n = 11743733`, determinant `-9856`), each with one
interior root. All witnesses were verified by two independent exact paths
(characteristic polynomial with Descartes counts, and leading principal
minors) on two architectures.

## 6. Rigidity and the two-scalar law at k = 3 (proposed C; theorem-eligible
parts noted)

Abstract setting: a ternary sign table on `{0,1,2}^3` with the extremal
binary face fixed leaves 19 free squareful signs; the block `K` is linear in
them. Exhaustive facts over all `2^19` tables, reproduced byte-identically
on two architectures:

```text
weight <= 2 block G_6:  det G_6 < 0  iff  inertia (NEG 3, ZERO 0, POS 3)
                        det G_6 = 0  iff  (NEG 2, ZERO 1, POS 3)
                        det G_6 > 0  iff  (NEG 2, ZERO 0, POS 4)
15-bit substrate census 32398 / 110 / 260 (two independent
implementations agree); the four cells of orbit types 122 and 222 do not
enter G_6, so every profile lifts exactly 16 times.
TWO-SCALAR LAW:  FAIL  iff  det G_6 < 0  AND  det K <= 0,
with det K = 0 the singular class (51 of 524288) and det K < 0 the
NEG-heavy class (1775 of 524288); all remaining 522462 tables are
balanced.
```

The rigidity trichotomy rests on: the diagonal pair pivots being negative
(the k = 2 theorem above), a four-value local bound table
`L(-1,-1) = 10, L(-1,+1) = 2, L(+1,-1) = 8, L(+1,+1) = 3` with
`-s(ij,ij) >= L(a_i, b_ij)` (32 local cases) and the coupling bound
`s(ij,ik)^2 <= L(a_i,b_ij) L(a_i,b_ik)` (16 local cases), giving all 2 by 2
principal minors of the pair Schur block nonnegative; the unique
all-minors-zero configuration is `[[-2,2,2],[2,-2,2],[2,2,-2]]` with
inertia `NEG 2 ZERO 0 POS 1`; interlacing then forces at least two negative
directions. These finite case lists are printable, so the trichotomy is
theorem-eligible once written out; this note carries it at computational
grade.

## 7. Invariant layers (proposed C; written lemmas noted)

The 19 cells carry the `S_3` representation `6 triv + sgn + 6 std`. The six
linear orbit sums do NOT decide the transfer: 58 of 3584 sum-buckets are
mixed, with an explicit collision pair. The canonical quadratic layer,
28 invariants (six orbit sums, 21 Gram pairings of the six standard
vectors, circulation squared), IS sufficient: 88352 buckets, zero mixed.
Burnside gives exactly `(2^19 + 3.2^12 + 2.2^7)/6 = 89472` orbits (cycle
counts 19, 12, 7; confirmed by direct enumeration), so the decision factors
through a proper quotient of the orbit space, merging at least 1120 orbit
distinctions and no class pair. Sufficiency means the decision factors
through the quadratic invariant map; no claim is made that the deciding
function is itself a polynomial of degree two.

## 8. Evidence pins

All computations are standard-library exact-integer scripts, no floating
point anywhere, environment `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0 TZ=UTC`, each run twice per platform with byte-identical
output, on Ubuntu 24.04 x86_64 Python 3.11.15 and Debian 13 aarch64 Python
3.13.5. The scripts and transcripts are archived in the incubation records
of the program under these pins (file sha256 / stdout sha256):

```text
c72b5cd7e3da6e67654fb22be22f3f54fc6cf31d6cf080f77f595f48ad979462 / 421a1de10f27b2b006e4749e2d69709fd9323a0b6a5927f02f4c497f1d47bb15
ae97ddb51aecd72580ff339f6512e8a978ecd80af7576b686ed51c7cb07bec79 / 2967fa167a11e8b25a6cceb736cbfa6a179a9aa7acce16d6b04325b9bec86251
0cf742249a3c200342d8915a0c3c9d08740a10c7e8edba563529ebbe98c007c0 / 3ea63d8b88bc8166d319d997a1a179fcd2333497c189590c9537cda69e515b5a
b1178bf5d6a325cbae37a1080c15a8e53b9c47ba4a08fc5777ed42f895afd338 / 50a508399dea10643ddd7dcd1f4b923dc48a54e9889b9ecef9c1df0816bf75d5
c2781d1796ad3168fa3da3b3a03473e5a1821a97f69d132d0c1fef39d08cf3c5 / c65c268958ea71997c56de9c289396b8fe756813eef36ba8a38e563a7bfbaea3
49fb97765f75c067f669866fd2ba00becd19c187c16042b5647d0a213c7339a8 / 570bb07440f44e870860c1d050d0db39076140a8db71b9b755d15544701106b8
417c8f680c93539b94803ff8fff1de08e71dcd095c780a05dc3da2b80591db7e / 996a3320b613a48042d5151d6b6756f7c8e32cf37c7e6f1c3e4b5b9b05e72143
e17e4334596fe9b821d95d27356612b71d64c23750e7c033cba80a243dfd1d01 / 62c7e631bbf73b3b9af2a215c62c59d1a6b413d7dbe9a88bf4b7b32fe4680a06
```

The two runs whose exit status is 1 are the recorded hypothesis
falsifications (section 5 and the failed everywhere-rigidity hypothesis
inside section 6), reproduced bit for bit on both architectures.

## 9. Falsifiers

Sections 1 to 4: one exact counterexample to any identity or inequality at
its stated scope. Section 5: the witness recomputation failing. Sections 6
and 7: any recount mismatch on an independent rerun. Every number in this
note is an exact integer.

## 10. Explicit non-claims

No statement about zeta zeros, the Riemann hypothesis, Weil positivity, or
explicit formulae. No statement about the infinite operator `H` beyond the
finite compressions above. No J-coupling, no physical reading, no L2-L6
lift, no Registry row, no Canon change. Machine-swept results are
computational grade; only the written proofs of sections 1 to 4 are
proposed at theorem grade, and any summary of this note elsewhere must not
exceed these grades.
