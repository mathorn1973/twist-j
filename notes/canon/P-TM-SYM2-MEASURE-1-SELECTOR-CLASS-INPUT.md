# P-TM-SYM2-MEASURE-1 selector-class definition input (NON-CANONICAL)

```text
C-TM-SELECTOR-CLASS-1
NON-CANONICAL / PARTIAL DEFINITION INPUT
STOP-PREDEFINITION / NO-PROBE / NO PUBLIC STATUS
```

This note is a partial definition input for the selector predefinition of
`TM-SYM2-MEASURE [H]` (issue #119,
`notes/canon/P-TM-SYM2-MEASURE-1-PREDEFINITION.md`). It proposes one exact
selector-class definition for review. It is not `READY-DEFINITION`, not a
preregistration, not a verifier, not a run, not evidence, and not a status
proposal. It contains no computation results. The lane remains `STOP` and
no formal probe is authorized by anything below.

Rev 3. Rev 2 answered the routing and `sigma`/domain review points
(sections 9, 3, 4; marked resolved on the review thread). This revision
answers the remaining merge blocker: section 7 now carries the all-`N`
convergence proof. The dyadic-subsequence argument of Rev 2 was
insufficient (the gaps between dyadic anchors have size of order `N`, so
Lipschitz interpolation gives only an `O(1)` relative bound); the repair
adds the even recurrence and replaces interpolation by a binary induction
over the base-2 expansion of `N`, with the affine forcing and the
peripheral Jordan term bounded exactly at every step. No other content
changes.

## Authority pin

```text
Canon:                 Public Canon v15
state:                 ACTIVE
tag:                   canon-v15
activation commit:     8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:        a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:         53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:           89288
owner row:             TM-SYM2-MEASURE [H]
scheduler:             MEASURE / ROOT / STOP / FORMAL
public lock:           issue #119
```

## 1. Design principle offered for review

The selector should not choose lines. It should transport involution
structure of the declared drive onto involution structure declared on the
registered frame, with everything else delivered by an exact enumeration
and an exact stationary law. Weights are stream-side pushforward weights,
never choices. Whether this principle canonically selects anything is a
question the future evaluation must answer; this note only makes the
question exact.

## 2. Carrier ansatz (declared, not forced)

Let `theta_n = s_2(n) mod 2` be the registered drive cut of the counter
component of the declared autonomous state `Omega = N_0 x F_5^6`, with the
registered doubling `(theta_(2m), theta_(2m+1)) = (theta_m, 1 - theta_m)`.

```text
q(n) := (theta_(n-1), theta_n, theta_(n+1)),   n >= 1,
W3   := the set of length-3 words occurring in the drive.
```

Because `theta` is cube-free at the relevant lengths (the registered
bracket machinery of TIME-CUT-READING excludes `000`; `111` is excluded
symmetrically), `W3` consists of the six words other than `000` and `111`.

DECLARED ANSATZ, with its risk stated: the radius-1 (length-3) window
quotient is NOT a publicly forced complete selector quotient. It is a
proposed carrier. That `|W3|` equals the number of frame lines is a
numerological coincidence risk, not evidence for the ansatz; the
canonicality test below must carry that risk, and any alternative window
radius or quotient is a different candidate definition.

## 3. The complete selector map and its conventions

The selector is a PARTIAL map on the declared autonomous state, total on
its declared domain:

```text
Dom(Sel) := { (n, psi) in Omega = N_0 x F_5^6 : n >= 1 },
Sel : Dom(Sel) -> Lines,
Sel(n, psi) := s(q(n)),
```

where `s : W3 -> Lines` is a class member per section 5. Domain clauses:

```text
n = 0 convention   (0, psi) is NOT in Dom(Sel) for any psi: the tick
                   n = 0 precedes the first complete window and emits no
                   selection. The empirical measure below is indexed by
                   exactly Dom(Sel) truncations, nu_N over n in [1, N],
                   the same index set as the window census; no
                   off-by-one shift between selector and census is
                   permitted. This convention is part of the ansatz, and
                   any padding or one-sided-window alternative is a
                   different candidate definition.
update convention  theta_n is indexed as in the registered selection law
                   (the drive value consumed at tick n); the window adds
                   no new convention beyond centering at n.
seed semantics     the drive is a function of n alone, so Sel(n, psi) is
                   constant in psi: seed-independence is discharged by
                   construction, for every seed and the full ensemble
                   alike. The selector reads the declared autonomous
                   state through its counter component; it is not a
                   function of the checkpoint psi alone.
starts             all n >= 1; no start is discarded.
```

## 4. Line typing and the proposed pairing structure

`Lines` is the registered ordered six-line carrier of
`GOLDEN-SIX-LINE-SYM2-FRAME [T]`, in its registered order and coordinates:
`v1 = (0,1,phi)`, `v2 = (0,1,-phi)`, `v3 = (1,phi,0)`, `v4 = (1,-phi,0)`,
`v5 = (phi,0,1)`, `v6 = (phi,0,-1)`, with `r = phi + 2` and projectors
`P_i = v_i v_i^T / r`.

PROPOSED NEW STRUCTURE, declared as such, in its exact projective
formulation. Every registered line has exactly one zero coordinate in its
registered representative; call that coordinate index the ZERO PATTERN of
the line (a projective invariant of the line with respect to the
registered coordinate frame: whether a line lies in a coordinate plane
does not depend on the chosen representative). Define

```text
sigma(l) := the unique registered line l' with l' != l and
            zero-pattern(l') = zero-pattern(l).
```

CONSISTENCY CLAUSE (checkable, part of the definition): each of the three
zero patterns is carried by exactly two registered lines, so `sigma` is a
well-defined fixed-point-free involution; on the registered list it is
the label permutation

```text
sigma = (v1 v2)(v3 v4)(v5 v6),
```

and each pair is exchanged, projectively, by negating the coordinate at
which its two representatives differ. `sigma` is an ABSTRACT LABEL
INVOLUTION on the registered ordered list: it is NOT a registered
structure of the frame row, and no claim is made that it is induced by a
single projective-linear symmetry of the line set. It is a structure this
definition adds, with the consistency clause above as its only anchor to
the registered vectors. Any competing pairing is a different candidate
definition.

## 5. Selector class, equivalence, and gauge

Window-side structure map: bit negation `N(w) = wbar` (0 and 1 exchanged
in all three slots). Its pedigree as a structure map, not a gauge: the
registered doubling flips the second child bit, and the registered lift
reads the bit as a sign, `Theta_n^2 = (-1)^(theta_n)`; negation is
therefore the drive's own registered flip.

```text
CLASS   Sel_class := { s : W3 -> Lines  total,
                       s(N(w)) = sigma(s(w)) for every w,
                       s surjective }.
```

Surjectivity is the row's own scope (the hypothesis under test says the
stream selects the six lines, not a subframe). No clause of the class
mentions frequencies, moments, densities, or Born values.

```text
GAUGE   G := Aut(Lines, sigma), the full automorphism group of the
        extended structure: all projective-linear transformations over
        Q(phi) that preserve the six-line set AND normalize sigma
        (g sigma g^(-1) = sigma as line permutations).
EQUIV   s ~ g o s for g in G.
```

The gauge is the automorphism group of the declared structure, not any
matrix-class intersection. Its order, its relation to the full projective
stabilizer of the bare line set, and whether Galois conjugation of
`Q(phi)` preserves the structure are outputs of the future evaluation,
not inputs of this definition.

## 6. Canonicality test and checker separation

```text
CANONICAL       exactly one G-orbit of Sel_class;
NONCANONICAL    at least two G-orbits (the checker must then name exact
                orbit invariants);
EMPTY           Sel_class is empty;
STOP            enumeration, gauge computation, or exactness incomplete.
```

Checker requirement (result neutrality): the future public checker must
separate `AUDIT PASS` (exact arithmetic, well-defined structures,
provably complete enumeration of the class and of the gauge) from the
scientific route (the computed orbit count routes the decision). The
checker may not embed an expected orbit count, an expected invariant
list, or an expected weight vector; a legitimate scientific outcome is
never a checker failure.

## 7. Stream-side pushforward weight, limiting measure, and the complete
convergence proof

The registered doubling induces exact child maps on windows,

```text
L(a,b,c) = (1-a, b, 1-b),      R(a,b,c) = (b, 1-b, c),
```

and the transfer `T[x][w] = [x = L(w)] + [x = R(w)]` on `Q^(W3)`. Write
`c(N)` for the census vector, `c_w(N) = #{ n in [1, N] : q(n) = w }`, and
`nu_N := (1/N) sum_(n=1)^(N) delta_(Sel(n, psi))` for the empirical
measure on lines (psi-independent by section 3).

LEMMA 1 (two exact affine recursions; proofs included). For every
`N >= 1`,

```text
(odd)   c(2N + 1) = T c(N) + e_(q(1)),
(even)  c(2N)     = T c(N) + e_(q(1)) - e_(q(2N+1)),
```

and the boundary window is internal to the induction:
`q(2N + 1) = R(q(N))`.

Proof. Odd: the positions `[2, 2N+1]` are exactly the children
`{2m, 2m+1}` of the parents `m in [1, N]`, each parent contributing
exactly its two children; by the registered doubling, the window at an
even child `2m` is `(1 - theta_(m-1), theta_m, 1 - theta_m) = L(q(m))`
and at an odd child `2m+1` is
`(theta_m, 1 - theta_m, theta_(m+1)) = R(q(m))`. Summing over parents
gives the counts over `[2, 2N+1]` as `T c(N)`; position 1 adds
`e_(q(1))`. There is no other boundary term. Even: subtract the single
last position, `c(2N) = c(2N+1) - e_(q(2N+1))`. Boundary identity: the
odd-child formula at parent `N` reads
`q(2N+1) = (theta_N, 1 - theta_N, theta_(N+1)) = R(q(N))`. QED.

LEMMA 2 (all-`N` deviation bound by binary induction; proof included,
spectral input certified; no subsequence and no interpolation step). Let
`f` be a stationary law, `T f = 2 f`, `sum f = 1`, `d(N) := c(N) - N f`.
Because `T(N f) = 2 N f` exactly, Lemma 1 gives the two exact affine
steps on the sum-zero subspace `Z`:

```text
(odd)   d(2N + 1) = T d(N) + u,   u  = e_(q(1)) - f,
(even)  d(2N)     = T d(N) + u',  u' = e_(q(1)) - e_(R(q(N))),
```

where `u, u' in Z` and `max-norm(u), max-norm(u') <= 1` (entries of `f`
lie in `[0, 1]`). Now take any `N >= 1` with binary expansion
`b_K b_(K-1) ... b_0` (`b_K = 1`, `K = floor(log2 N)`), and define the
prefix chain `N^(K) = 1`, `N^(j-1) = 2 N^(j) + b_(j-1)`, so that
`N^(0) = N` and every step is exactly one of the two recursions above.
Unrolling,

```text
d(N) = T^K d(1) + sum_(j=0)^(K-1) T^j u_j,
```

with each `u_j in Z`, `max-norm(u_j) <= 1`, and
`d(1) = e_(q(1)) - f in Z`, `max-norm(d(1)) <= 1`. Let `rho` be the
spectral radius of `T` restricted to `Z`, `rho+ := max(rho, 1)`, and let
`(C_J, m)` be the certified pair with

```text
opnorm(T^j restricted to Z) <= C_J (1 + j)^(m-1) rho+^j    for all j >= 0
```

(`m` = the largest peripheral Jordan degree of the restriction; such a
pair is exactly computable from the minimal polynomial certificate S2
below). Then for EVERY `N >= 1`:

```text
max-norm(d(N)) <= sum_(j=0)^(K) C_J (1 + j)^(m-1) rho+^j
               <= C_J (1 + K)^m rho+^K,
```

hence

```text
max_w | c_w(N) / N - f_w |  <=  C_J (1 + log2 N)^m N^(log2 rho+ - 1).
```

Whenever `rho < 2`, the exponent `log2 rho+ - 1` is negative (it equals
`-1` if `rho <= 1`), so `nu_N` converges to the pushforward `s_* f` for
the FULL sequence of `N`, with that explicit effective modulus. QED
(conditional on the certified spectral data below).

REQUIRED EXACT CERTIFICATES (produced by the future evaluation, not
asserted here):

```text
S1  the transfer T, its exact characteristic polynomial, and its exact
    factorization over Z;
S2  the growth certificate: the exact minimal polynomial of T restricted
    to the sum-zero subspace, its factorization and root moduli, strict
    subdominance rho < 2, and the derived explicit pair (C_J, m) of
    Lemma 2;
S3  uniqueness of the stationary law (rank of T/2 - I equals |W3| - 1 by
    exact elimination), so f in Lemma 2 is unique;
S4  machine verification of BOTH Lemma 1 recursions and of the boundary
    identity q(2N+1) = R(q(N)) on the actual drive, over a contiguous
    range of N up to the audit bound (not only dyadic scales; a
    consistency audit of the derivation, not the source of the theorem).
```

The weight objects are then defined, not chosen:

```text
f       the unique stationary law certified by S3;
nu_s    := s_* f, the STREAM-SIDE PUSHFORWARD WEIGHT of each line (the
        term "physical weight" is not used and no physical reading is
        claimed at this layer);
M_TM(A) := sum_w f_w Tr(P_(s(w)) A) P_(s(w))    as an operator on Sym2.
```

The convergence claim of this definition is exactly Lemma 1 plus Lemma 2
plus the certificates S1 to S4: a complete all-`N` proof with an explicit
effective modulus, whose only computational inputs are exact and
machine-checkable. No value of `f`, `rho`, `m`, `C_J`, `nu_s`, or `M_TM`
is asserted in this note.

## 8. Factor-map slots offered to the Born block (typing only)

Two typed stream maps are offered as CANDIDATE fillers for the row's
factor-meaning slots, with their values left to the evaluation:

```text
third   the leading-pair density map: the stationary density of the
        leading pair (w1, w2) of a window, from the registered pair
        census machinery;
half    the conditional continuation weight: f_(w1 w2 w3) / f_(w1 w2)
        for the admissible continuations of a branching leading pair.
```

TYPE LIMIT, stated up front: by cube-freeness the extreme pairs `00` and
`11` have exactly one admissible continuation, so their continuation
factor is 1 by type; the (third, half) factorization can at most cover
windows with a mixed leading pair. These maps therefore CANNOT by
themselves derive a universal Born halving, and no such derivation is
claimed. Whether `third` and `half` may be read as the row's `1/3` and
`1/2` through a typed Born map remains exactly the reserved dictionary
decision of the predefinition (its false shortcuts 5 and 7).

## 9. Deterministic routing (fixed evaluation order, one route per
condition)

The future evaluation runs two stages in a fixed order. Stage 1 decides
integrity; only if every Stage 1 item passes is Stage 2 (science)
evaluated. Every condition below belongs to exactly one stage and maps to
exactly one route; no condition is routed by judgment.

```text
STAGE 1, INTEGRITY. ANY failure here routes STOP (the evaluation is
invalid; nothing scientific is concluded, positively or negatively):
  I1  exact-arithmetic reproduction of the audit fails (any inexact
      step, any nondeterminism, any platform mismatch at audit time);
  I2  the sigma consistency clause of section 4 fails against the
      registered vectors (some zero pattern is not carried by exactly
      two lines);
  I3  the enumeration of Sel_class or of Aut(Lines, sigma) lacks a
      completeness certificate;
  I4  any of the certificates S1 to S4 of section 7 is missing or
      inexact, or S2 yields rho >= 2 (the modulus formula then proves
      nothing and the weight object is undefined);
  I5  the stationary law is not unique (S3 fails).

STAGE 2, SCIENCE (reached only with Stage 1 all green). Evaluated in
this order; the FIRST matching condition fixes the route:
  N1  Sel_class is EMPTY                          -> NEGATIVE;
  N2  the canonicality test returns NONCANONICAL  -> NEGATIVE
      (the checker names the exact orbit invariants; the fired negative
      is preserved, not repaired by changing the class);
  N3  some line has pushforward weight != some other line's
      (unequal nu_s), or M_TM leaves the registered exact commutant, or
      the 5:2 coefficient ratio is changed        -> NEGATIVE;
  P0  otherwise: the selector clauses of this definition are satisfied
      at evaluation grade. This does NOT route POSITIVE: the row's
      positive closure additionally requires the typed Born derivation,
      which this input deliberately leaves with the reserved dictionary
      decision (section 8). The lane's residual gates own that step.
```

A fired NEGATIVE is archived; no threshold, clause, or class is moved
after evaluation. STOP outcomes carry no scientific weight in either
direction.

## 10. Residual definition debt (what this input does NOT fill)

```text
carrier completeness   whether any window quotient is the right selector
                       carrier at all (section 2 risk);
Born carrier, Born map, factor typing decision (section 8 limit);
density bridge         no relationship between the line weights and
                       GYRON-DENSITY is proposed;
action layers          source and target layers, lifts, and gates from
                       the L1 stream to the terminal L6 measure;
certificate schema     the exact public checker and its completeness
                       proofs (section 6 requirement only names them).
```

This input adds no registry row, no dependency, no gate, no evidence, and
no status. `TM-SYM2-MEASURE [H]` and its lane remain exactly where the
predefinition holds them: `STOP`.
