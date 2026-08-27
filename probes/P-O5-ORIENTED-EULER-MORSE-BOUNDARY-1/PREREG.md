# P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / NO FORMAL RUN YET / CANON UNCHANGED**

Date: 2026-08-27.

This probe freezes one exact combinatorial-topology carrier for the squarefree
split-orientation sum and one narrow attack-route boundary. It tests whether a
face-incidence sign-reversing matching followed only by a critical-cell
triangle bound can reach the square-root scale.

It does not prove or disprove RH or GRH and it does not estimate the actual
summatory function.

## Public identity, authority, and action layer

```text
probe:             P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1
public claim lock: issue #594
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1
path:              probes/P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1/
basis main:        e051ad2472e77cf2ffbc2bad965e2a99e7dfea10
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, finite combinatorial topology / analytic-number-theory boundary
layer lift:        none
authority:         none until a later sealed Canon fold
```

The authority tag targets activation commit
`7dd25c7c21202c560d8a31774971c7c6200fca76`. That commit and the declared
content commit are ancestors of the displayed basis main. The immutable v67
release records the same content identity.

The collision scan covered issues, pull requests, every remote branch, the
Public Canon v67 tree, Registry, Frontier, Evidence, Gates, current probes and
current Notes. No existing object owns this probe or proposed row.

## Adjacent work and ownership boundary

Public `J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]` owns the safe-half-plane
factor

\[
O_5(s)=\prod_{\chi_5(p)=1}\frac{(1-p^{-s})^2}{1+p^{-2s}}
\qquad(\Re s>1)
\]

and owns no continuation or cancellation.

Merged `P-O5-SQUAREFREE-CORE-1` independently carries, at candidate grade
pending a later fold, the squarefree factor

\[
S_5(s)=\prod_{\chi_5(p)=1}(1-2p^{-s})
\]

and the analytic-unit transfer from `O_5`. The finite coefficient formula used
here is re-derived below. This probe creates no additional evidence credit for
that result.

Merged `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` independently carries, at candidate
grade pending a later fold, a divisor-coordinate read of field GRH. It is not
an input here.

`J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO [T]` concerns the coefficient-l1 norm of
the full integral rapidity lift. The present route concerns a different finite
face-incidence carrier. `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains the
separate ordinary-Mobius augmentation problem and is untouched.

## Proposed candidate row

At most the following package may be offered to a later sealed fold:

```text
O5-ORIENTED-EULER-MORSE-BOUNDARY [candidate-T]

For every integer N>=1, let K_5(N) be the finite simplicial complex whose
vertices are the two formal orientations (p,+),(p,-) of each rational split
prime p<=N, and whose faces select at most one orientation over each p and
have underlying prime product at most N. Let

    s_5(n)=(-2)^omega(n)

on squarefree integers supported entirely on split primes and zero otherwise,
and let S_5^sum(N)=sum_(n<=N)s_5(n).

Then

    S_5^sum(N) = - reduced_Euler_characteristic(K_5(N)).

Every split prime p with 11p>N contributes two isolated vertices. If

    I_5(N)=#{split p : 11p>N and p<=N},

then every matching of faces along one-vertex incidence leaves at least
max(0,2I_5(N)-1) unmatched faces even when the empty face may be used, and at
least 2I_5(N) when it may not. Consequently a route which cancels matched
opposite-parity faces and then bounds only by the number of unmatched faces
cannot reach the all-epsilon square-root scale: by the classical prime number
theorem in the split residue classes 1 and 4 modulo 5, I_5(N) has order
N/log N. This no-go is only for the critical-cell triangle route. Signed
critical-cell, Morse-boundary, homological, weighted, nonlocal and spectral
cancellation remain open.
```

The exact finite carrier and matching floor are theorem-grade by the proof
below. The final asymptotic route statement imports only PNT in arithmetic
progressions modulo 5 and is `candidate-T on [T-lit]`.

## Falsifier first

One exact counterexample falsifies the corresponding frozen statement:

1. `K_5(N)` is not downward closed for one `N`;
2. its face count or augmented Euler identity differs from `S_5^sum(N)`;
3. a split prime `p` with `11p>N` belongs to an edge;
4. a valid one-vertex-incidence matching matches two isolated vertices
   through the single empty face, or matches an isolated vertex to a nonface;
5. the unmatched-face lower bound fails;
6. the PNT-in-progressions consequence is misstated;
7. the construction selects one orientation, admits an inert or ramified
   prime, imports target cancellation, or widens the no-go beyond the frozen
   triangle-count route.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold,
or scope widening is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  The definition of K_5(N), its exact face-count and augmented Euler identity,
  the isolated-vertex theorem, the universal incidence-matching floor, and the
  PNT-AP consequence for the critical-cell triangle route.

CODE
  probes/P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1/verify.py.
  Python standard library only; exact integers; deterministic face generation,
  exact maximum bipartite matching on frozen finite audits; no float, complex
  approximation, random input, network, external package or zero table.

CARRIER
  Rational split primes for chi_5, two formal orientations per split prime,
  finite simplicial faces, integer prime-product norms, augmented face parity,
  and one-vertex-incidence matchings.

SYSTEMATICS
  The two orientations over one split rational prime remain an unordered pair.
  At most one may occur in a face. The empty face is included in the augmented
  Euler sum. The universal matching floor permits the empty face to be used at
  most once, which is the strongest convention for the route.

THRESHOLD
  G01 through G08 must pass exactly. B1 through B5 must fire at the frozen
  first witnesses 11,121,2,(209,19),1. Stdout must equal one committed LF
  EXPECTED.txt byte for byte; exit zero and empty stderr are required on the
  required architecture jobs.

LAYER
  NOT_APPLICABLE. Finite combinatorial topology and analytic-number-theory
  boundary only. No L1-L6 lift, state, decoder, probability, physical or SI
  statement.
```

## 1. The oriented split threshold complex

Let `chi_5` be the quadratic character modulo five. A rational prime is called
split when `chi_5(p)=1`, equivalently `p mod 5` is `1` or `4`. The smallest
split rational prime is `11`, since `2,3,7` are inert and `5` is ramified.

Fix `N>=1`. The vertex set of `K_5(N)` is

\[
V_N=\{(p,+),(p,-):p\le N,\ p\text{ split}\}.
\]

For a finite set `F` of vertices, write `supp(F)` for the underlying rational
primes and

\[
\nu(F)=\prod_{p\in\operatorname{supp}(F)}p,
\qquad \nu(\varnothing)=1.
\]

Declare `F` to be a face exactly when it contains at most one of `(p,+)` and
`(p,-)` for each `p`, and `nu(F)<=N`.

If `G subset F`, then `G` still contains at most one orientation over each
prime and `nu(G)` divides `nu(F)`, hence `nu(G)<=nu(F)<=N`. Thus `K_5(N)` is a
finite simplicial complex.

If `Delta_5(N)` is the underlying complex of split-prime supports with product
at most `N`, then `K_5(N)` is its octahedralization: every vertex `p` is
replaced by the zero-sphere `{(p,+),(p,-)}`, and a face selects at most one
member of each zero-sphere.

## 2. Exact Euler carrier

For a squarefree split integer

\[
n=\prod_{j=1}^k p_j,
\]

a face with support `{p_1,...,p_k}` has one of two orientations over every
prime. It therefore has exactly `2^k` oriented lifts, all with cardinality
`k`. Conversely every `k`-vertex face has one squarefree split support of this
form.

If `f_(k-1)(N)` is the number of `k`-vertex faces and `f_(-1)(N)=1` counts the
empty face, then

\[
f_{k-1}(N)
=\sum_{\substack{n\le N\\n\text{ squarefree split}\\\omega(n)=k}}2^k.
\]

Define

\[
s_5(n)=
\begin{cases}
(-2)^{\omega(n)},&n\text{ squarefree split},\\
0,&\text{otherwise}.
\end{cases}
\]

Then

\[
\begin{aligned}
S_5^{\rm sum}(N)
&=\sum_{n\le N}s_5(n)\\
&=\sum_{k\ge0}(-1)^k f_{k-1}(N).
\end{aligned}
\]

Using the standard augmented convention

\[
\widetilde\chi(K)=\sum_{i=-1}^{\dim K}(-1)^i f_i(K)
=-1+f_0-f_1+f_2-\cdots,
\]

we obtain

\[
\boxed{S_5^{\rm sum}(N)=-\widetilde\chi(K_5(N)).}
\]

This identity is finite and exact for every `N`.

## 3. Isolated large-prime vertices

Let `p` be split and suppose `11p>N`. Any second vertex in a face containing
`(p,+)` or `(p,-)` lies over a distinct split rational prime `q`. Since `11`
is the smallest split prime, `q>=11`, so

\[
pq\ge 11p>N.
\]

Therefore no such two-vertex set is a face. Both `(p,+)` and `(p,-)` are
isolated vertices.

Put

\[
I_5(N)=\#\{p\le N:p\text{ split and }11p>N\}.
\]

The complex has at least `2 I_5(N)` isolated vertices.

The strict inequality is load-bearing. At `N=209=11*19`, the split prime
`p=19` satisfies `11p=N`, and the four oriented edges with support `{11,19}`
are valid. Thus replacing `11p>N` by `11p>=N` is false.

## 4. Universal incidence-matching floor

Consider any matching on the augmented face poset in which a matched pair
consists of two faces differing by exactly one vertex. Such a pair has opposite
face-cardinality parity, so its contributions to the augmented Euler sum
cancel exactly.

An isolated vertex has no coface of cardinality two. Its only possible
one-vertex-incidence partner in the augmented poset is the empty face. Because
a matching uses each face at most once, the single empty face can absorb at
most one isolated vertex. Hence every such matching leaves at least

\[
\boxed{\max(0,2I_5(N)-1)}
\]

unmatched faces. If the empty face is not admitted to the matching, all
`2I_5(N)` isolated vertices remain unmatched.

This statement does not require acyclicity. It therefore applies a fortiori to
every discrete Morse matching of this incidence type.

After cancelling all matched pairs, the triangle inequality gives only

\[
|S_5^{\rm sum}(N)|
\le \#\{\text{unmatched faces}\}.
\]

The theorem above says that this particular upper-bound mechanism cannot make
the right side smaller than the isolated-vertex floor.

## 5. Asymptotic route verdict

The only analytic import is the classical prime number theorem in arithmetic
progressions modulo five:

\[
\pi(x;5,1)\sim\frac14\operatorname{Li}(x),
\qquad
\pi(x;5,4)\sim\frac14\operatorname{Li}(x).
\]

Therefore the number of split primes in `(N/11,N]` has order `N/log N`, so

\[
I_5(N)\asymp \frac{N}{\log N}.
\]

For every fixed `epsilon<1/2`, `N/log N` is not
`O(N^(1/2+epsilon))`. Consequently no sequence of incidence matchings whose
final estimate is only the unmatched-face triangle count can prove the
all-epsilon square-root bound.

This is a route no-go, not a lower bound for `|S_5^sum(N)|`. Large cancellation
among unmatched contributions is not excluded.

## 6. Frozen negative controls

The accepted verifier must route all mutations through the same face and
coefficient constructors.

```text
B1 ONE_ORIENTATION
   Keep only one orientation over each split prime. The Euler coefficient
   first differs from `s_5` at N=11.

B2 ALLOW_CONJUGATE_PAIR
   Permit both `(p,+)` and `(p,-)` in one face. The first extra face has
   norm 11^2=121, so the identity first fails at N=121.

B3 INERT_TWO_AS_SPLIT
   Admit p=2 as split. Support first differs at N=2.

B4 CLOSED_ISOLATION_THRESHOLD
   Replace `11p>N` by `11p>=N`. At N=209,p=19 this falsely declares an
   isolated vertex although the support edge `{11,19}` exists.

B5 DROP_EMPTY_FACE
   Omit the empty face from the augmented Euler sum. The constant term first
   fails at N=1.
```

## 7. Frozen verifier gates

```text
G01  exact chi_5 prime classification and first split prime 11
G02  finite face generation is duplicate-free and downward closed
G03  coefficient sum equals augmented face-parity sum on frozen N values
G04  exact dimension counts equal 2^omega support multiplicities
G05  strict isolated-vertex theorem and N=209 boundary witness
G06  maximum one-incidence matching audits obey both isolated-cell floors
G07  B1 through B5 fire at their frozen first witnesses
G08  exact-integer stdlib source firewall
```

The finite audits do not define the universal theorem scope. The proof above
does.

## 8. Clean interpreter-startup control

Before the single accepted local verifier execution, run

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and require exit zero, exactly `PYTHON_STARTUP_CLEAN` plus LF, and empty
stderr. Failure is STOP and no scientific output is accepted.

The scientific command is

```text
env -i PATH=/usr/bin*/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1/verify.py
```

## 9. Explicit nonclaims

This probe supplies no RH or GRH result and no cancellation estimate for the
squarefree split sum. It does not register or fold the candidate results of
`P-O5-SQUAREFREE-CORE-1` or `P-O5-DEDEKIND-GRH-DIVISOR-READ-1`.

It does not select one split orientation, introduce a Hecke or automorphic
character, or claim probability, physics, SI, decoder, measure, or an L1-L6
lift.

It does not rule out cancellation among unmatched cells, the Morse boundary,
alternating homology, weighted or nonlocal matchings, nondiagonal kernels,
growing modes, spectral methods, or any complete transfer class. Failure of
this one route is STOP for broader attacks, not negative closure of a frontier
row.
