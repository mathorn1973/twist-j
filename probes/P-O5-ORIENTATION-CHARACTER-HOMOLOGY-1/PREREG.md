# P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-27.

This probe freezes one exact positive boundary theorem for the oriented split
threshold complex. It follows the completed incidence-triangle no-go by
diagonalizing the full simplicial boundary under the finite orientation-flip
group. It does not prove a summatory estimate, RH, or GRH.

## Public identity

```text
probe:             P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1
public claim lock: issue #599
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1
path:              probes/P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1/
basis main:        3450c6ccc12352ac07d789d2d65fc0430569eea5
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, finite simplicial homology / exact character algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The collision scan covered issues, pull requests, remote branches, the v67
tree, Registry, Frontier, evidence, gates, current O5 probes and current Notes.

Adjacent work is separated as follows.

- `P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1`, merged by PR #598, owns a
  candidate-grade oriented Euler carrier and a no-go only for incidence
  matching followed by an unmatched-cell triangle count. The present probe
  redefines the finite carrier and advances to its signed boundary and homology.
- `P-O5-SQUAREFREE-CORE-1` and
  `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` are separate candidate-grade lanes and
  are not evidence inputs.
- draft Notes PR #595, `C-RAPIDITY-GOLDEN-LADDER-1`, is a separate
  NON-CANONICAL growing-mode lane.
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains untouched.

## Proposed candidate row

At most one row may be offered to a later sealed fold.

```text
O5-ORIENTATION-CHARACTER-HOMOLOGY [candidate-T]

For each N>=1 let Delta_5(N) be the simplicial complex whose vertices are
rational split primes p<=N and whose faces are finite prime sets with product
at most N. Let K_5(N) be its octahedralization, with two formal orientations
(p,+),(p,-) over each split prime and at most one orientation per support
prime. Work with augmented simplicial chains over Q.

For faces J subseteq S of Delta define

  E_(S,J)
    = sum_(epsilon:S->{+-1})
      prod_(j in J) epsilon(j) [S,epsilon].

For each support S the E_(S,J), J subseteq S, form the Walsh Q-basis of its
oriented-face space. The boundary is

  d E_(S,J)
    = 2 sum_(p in S\J) (-1)^pos_S(p) E_(S\{p},J).

Let L_J=link_Delta(J), let
nu_J(T)=#{(j,t) in J x T:j<t}, and define

  Psi_J([T])
    = 2^(-|T|) (-1)^nu_J(T) E_(J union T,J).

Then Psi_J is a chain isomorphism from the augmented chain complex of L_J,
shifted upward by |J|, onto the J-character sector. Consequently

  H~_q(K_5(N);Q)
    ~= direct_sum_(J in Delta_5(N))
       H~_(q-|J|)(link_Delta(J);Q),

and

  chi~(K_5(N))
    = sum_(J in Delta_5(N)) (-1)^|J| chi~(link_Delta(J)).

No summatory estimate, RH, GRH, continuation, zero, physical, or L1-L6 claim
is included.
```

No status is earned by this preregistration. The proof below is the theorem
evidence. The verifier is a bounded exact audit.

## Falsifier first

One exact counterexample falsifies the corresponding frozen statement:

1. a support-level Walsh family is linearly dependent over `Q`;
2. a boundary deletion with `p in J` survives, or a deletion with `p notin J`
   has the wrong sign or coefficient;
3. the sign correction `nu_J(T)` or scale `2^(-|T|)` fails to conjugate the
   sector differential to the link differential;
4. one character sector has the wrong dimension;
5. one rational Betti number disagrees with the shifted direct sum of link
   Betti numbers;
6. the reduced Euler identity fails;
7. the construction selects one orientation, includes an inert or ramified
   prime, imports a target cancellation estimate, or widens beyond finite
   rational homology.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold
or scope widening is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  The support-level Walsh basis, exact character boundary, explicit link
  chain isomorphism, rational homology direct sum and reduced Euler identity.

CODE
  probes/P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1/verify.py.
  Python standard library only; exact integers and Fraction arithmetic;
  deterministic finite chain complexes and exact Gaussian elimination;
  no float, complex approximation, network, random, zeta-zero table,
  special-function evaluation or external package.

CARRIER
  chi_5 split rational primes, the finite support threshold complex Delta_5(N),
  its octahedralization K_5(N), augmented rational simplicial chains,
  the orientation-flip group (C_2)^(P_N), Walsh characters and support links.

SYSTEMATICS
  The two orientations over a split rational prime remain an unordered pair.
  Simplex order is increasing rational prime. No orientation is selected.
  The theorem is over Q; invertibility of two is load-bearing.

THRESHOLD
  G01 through G07 must pass exactly. B1 through B5 must fire at the frozen
  witnesses. One LF EXPECTED.txt, exit zero, empty stderr and byte identity
  are required by the repository architecture gate.

LAYER
  NOT_APPLICABLE. Finite combinatorial topology and exact character algebra.
  No state, manifold, boundary-layer lift, support-layer lift, stream, measure,
  decoder, observable, physical dictionary or SI statement.
```

## 1. Carrier and canonical simplex orientation

Let

```text
P_N = { rational primes p<=N : chi_5(p)=1 }.
```

Define `Delta_5(N)` on the vertex set `P_N`. A finite set `S` is a face when

```text
prod_(p in S) p <= N.
```

The empty face is included. Downward closure is immediate from divisibility.

Define `K_5(N)` by replacing every support vertex `p` with two formal vertices

```text
(p,+), (p,-),
```

and allowing exactly those oriented faces which choose at most one orientation
above each `p` and whose underlying support is a face of `Delta_5(N)`.

For a face with support

```text
S={p_0<...<p_q},
```

the oriented simplex `[S,epsilon]` is ordered by the rational primes
`p_0<...<p_q`, regardless of the signs. This fixes the boundary signs.

The empty face is the unique chain basis element in degree `-1`.

## 2. Walsh basis on each support

Fix a support face `S`. Its oriented-face vector space has the basis

```text
[S,epsilon], epsilon:S->{+1,-1},
```

of cardinality `2^|S|`.

For each `J subseteq S`, define

```text
E_(S,J)
  = sum_epsilon chi_J(epsilon) [S,epsilon],

chi_J(epsilon)
  = prod_(j in J) epsilon(j).
```

The character orthogonality identity is

```text
sum_epsilon chi_J(epsilon) chi_J'(epsilon)
  = 2^|S| if J=J',
    0      otherwise.
```

Thus the square Walsh matrix has nonzero determinant over `Q`, and the
`E_(S,J)` form a basis. Grouping basis vectors with the same `J` across all
supports containing `J` gives a direct-sum decomposition of the augmented
chain groups.

This step uses that `2` is nonzero and invertible in `Q`. No characteristic
two claim is made.

## 3. Exact character boundary

Let `S={p_0<...<p_q}`. The simplicial boundary is

```text
d[S,epsilon]
  = sum_i (-1)^i [S\{p_i}, epsilon restricted].
```

Fix `J subseteq S` and one deleted prime `p_i`.

If `p_i in J`, the two extensions of a fixed lower orientation have opposite
Walsh weights because they differ only in `epsilon(p_i)`. They cancel.

If `p_i notin J`, the two extensions have the same Walsh weight. They add and
produce a factor two.

Therefore

```text
d E_(S,J)
  = 2 sum_(p in S\J) (-1)^pos_S(p) E_(S\{p},J).
```

Every fixed `J` therefore defines a chain subcomplex `C_*^(J)`.

## 4. Link conjugation and the ordering sign

For a face `J` of `Delta_5(N)`, let

```text
L_J = link_Delta(J)
    = { T disjoint from J : J union T is a face of Delta }.
```

For `T in L_J` set

```text
nu_J(T)
  = #{(j,t) in J x T : j<t}.
```

The difference between the position of `t` in the ordered union `J union T`
and its position in `T` is exactly

```text
#{j in J:j<t}.
```

Hence deleting `t` changes `nu_J(T)` by precisely the parity needed to
conjugate the support-order sign to the link-order sign.

Define

```text
Psi_J([T])
  = 2^(-|T|) (-1)^nu_J(T) E_(J union T,J).
```

For `t in T`, the character boundary contributes a factor `2`. The scale
changes from `2^(-|T|)` to `2^(-(|T|-1))`, exactly the scale of the lower link
face. The `nu_J` parity corrects the ordering sign. Therefore

```text
d Psi_J([T]) = Psi_J(d[T]).
```

The map is bijective degree by degree because `T -> J union T` is a bijection
between link faces and supports in the `J` sector. Its degree shift is

```text
dim(J union T) = dim(T)+|J|.
```

Thus `Psi_J` is a chain isomorphism from the augmented link chain complex,
shifted upward by `|J|`, onto `C_*^(J)`.

## 5. Rational homology decomposition

The whole chain complex is the direct sum of the character sectors and every
sector is chain-isomorphic to one shifted link complex. Taking homology gives

```text
H~_q(K_5(N);Q)
  ~= direct_sum_(J in Delta_5(N))
     H~_(q-|J|)(L_J;Q).
```

This is a finite direct sum. No convergence or analytic input appears.

The formula correctly includes the `-1` reduced degree. For example, if `J`
is a maximal face then `L_J` contains only the empty face, whose augmented
homology is one-dimensional in degree `-1`; this contributes in degree
`|J|-1` of the oriented complex.

## 6. Reduced Euler consequence

Reduced Euler characteristic is the alternating sum of rational Betti
numbers. A degree shift by `|J|` multiplies Euler characteristic by
`(-1)^|J|`. Hence

```text
chi~(K_5(N))
  = sum_(J in Delta_5(N))
    (-1)^|J| chi~(L_J).
```

Equivalently, the oriented Euler carrier is exactly decomposed into signed link
sectors. This is a boundary-level identity, not an estimate.

## 7. Why this survives the preceding no-go

The completed incidence-triangle no-go shows that a proof which pairs incident
opposite-parity faces and then bounds only the number of unmatched cells
cannot reach square-root strength because large split primes force many
isolated cells.

The Walsh theorem does not apply that endpoint. It decomposes the complete
boundary operator. Isolated cells become specific link-character homology
sectors rather than an unsigned count. The remaining hard question is whether
the signed family of link sectors admits a uniform reconstruction, operator,
or spectral bound.

No such bound is claimed here.

## 8. Frozen negative controls

```text
B1  erase chi_J(epsilon) from the Walsh vectors.
    At support {11} the two rows coincide and rank drops from 2 to 1.

B2  retain deletion terms for p in J.
    At S=J={11} the true boundary is zero and the mutation is nonzero.

B3  omit the factor 2 in the character boundary.
    At S={11},J=empty the true empty-face coefficient is 2.

B4  omit nu_J(T).
    At N=209, J={11}, T={19}, the support-order and link-order signs differ.

B5  reduce the support Walsh matrix modulo 2 while claiming the Q theorem.
    At support {11} [[1,1],[1,-1]] becomes rank one.
```

Each breaker changes the production constructor, not a parallel toy formula.

## 9. Frozen verifier gates

```text
G01  Walsh orthogonality through support size five.
G02  exact boundary formula on all sectors for N in {11,121,209,500}.
G03  explicit Psi_J chain map on every link sector for the same N.
G04  exact rational Betti decomposition for N in {1,11,121,209,500}.
G05  exact reduced Euler decomposition through N=1000.
G06  B1-B5 all fire at their frozen witnesses.
G07  source firewall: stdlib-only, exact rational, no float/complex/network/
     random/external package/zero table.
```

Finite gates audit the written universal proof. They do not define its scope.

## 10. Formal run discipline

Before the public pin the verifier may only be read and AST-parsed. It may not
be imported or executed.

The first pushed commit contains only fresh `PREREG.md` and `verify.py`.
After exact public readback, run the clean startup preflight

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and require exit zero, exactly one LF stdout line and empty stderr.

Only then may the single accepted scientific command run:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-ORIENTATION-CHARACTER-HOMOLOGY-1/verify.py
```

No threshold, witness, carrier, equation or source firewall may move after the
pin.

## 11. Explicit nonclaims

This probe supplies no RH or GRH result, no summatory cancellation estimate,
no analytic continuation, no zero statement, no Hecke or automorphic object,
no selected split orientation, no physical interpretation, no decoder or
probability statement, and no L1-L6 lift.

It does not assert that link homology is small, concentrated, sign-definite,
uniformly bounded, or sufficient to close any frontier row.
