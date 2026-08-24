# PREREG P-A3-FCC-POINT-GROUP-1

```text
CLAIM:           A3-FCC-POINT-GROUP
PROBE:           P-A3-FCC-POINT-GROUP-1
BRANCH:          probe/P-A3-FCC-POINT-GROUP-1
PATH:            probes/P-A3-FCC-POINT-GROUP-1/
PUBLIC LOCK:     issue #275
STATUS:          RESULT-EXPOSED / PROSPECTIVE / NO FORMAL RUN BEFORE PIN
ACTION LAYER:    L1 exact integral, rational, and finite algebra only
INTERLAYER GATE: none
```

This file and the adjacent accepted `verify.py` become immutable only when
they are committed and pushed together on the branch above.  Static source
review and syntax parsing are permitted before that pin.  No scientific gate
in `verify.py` may be executed before exact public readback of the pin.

## Authority and collision readback

The prospective base is Public Canon v36:

```text
STATE:          ACTIVE
authority:      mathorn1973/twist-j main
base main:      470d95826037d75e29530177171763f1376b4614
tag:            canon-v36
activation:     a2c96226fc0ec994865d323dfc2b5c72fdd9dc41
content commit: df64035f6f0cadbeb17f539eaeec5d8d0f444515
Canon SHA-256:  c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
Canon bytes:    175814
main check:     workflow run 30913500864, success
```

The tag activation and content commits are ancestors of the base, and all
five entries of `canon/SHA256SUMS` agree.  At claim time and again before
branch creation there was no issue, pull request, remote branch, probe,
Registry or Frontier row, Gate, note, object lock, or claim lock named
`A3-FCC-POINT-GROUP` or `P-A3-FCC-POINT-GROUP-1`.  Issue #275 owns this one
probe.  Issue #274 released and closed the former photon-labelled reservation
before issue #275 opened.

## Frozen field 1: equations and atomic theorem gates

### Integral lattice and transport types

Let

```text
L = {x in Z^4 : x1+x2+x3+x4=0},
b1 = e1-e2, b2=e2-e3, b3=e3-e4,
A = [[ 2,-1, 0],
     [-1, 2,-1],
     [ 0,-1, 2]],
q(u,v) = u^T A v,
R = {u in Z^3 : q(u,u)=2},
Aut = {g in GL_3(Z) : g^T A g=A}.
```

For `P_sigma e_i=e_(sigma(i))`, let `g_(eps,sigma)` be the matrix in the
displayed `b` basis induced by `eps P_sigma` on `L`, for
`eps in {+1,-1}` and `sigma in S_4`.  Put

```text
W = {g_(eps,sigma) : eps in {+1,-1}, sigma in S_4}.
```

The fixed transport matrix is

```text
F = [[ 1, 0,-1],
     [-1, 1,-1],
     [ 0,-1, 0]],
D3 = {y in Z^3 : y1+y2+y3 is even},
Shell(N) = {y in D3 : y.y=N}.
```

`FCC` in the claim identifier means only the conventional mathematical name
for this presentation of `D3`.  It is not a physical, photon, spatial,
checkpoint, or decoder carrier.

### Finite reduction type

Over `F_5`, define

```text
V5 = F_5^3,
b_A(u,v) = u^T (A mod 5) v,
O5 = {M in Mat_3(F_5) : M^T A M=A},
red_5(g) = g mod 5.
```

An integral subgroup lift of an inclusion `i_H:H -> O5` means a homomorphism

```text
s:H -> Aut  with  red_5 o s = i_H.
```

Such an `s` is automatically injective.  The icosahedral cases in this
probe mean only `H ~= A5` or `H ~= A5 x C2` inside this exact diagram.

### Homogeneous quartic and shell-weight types

Let

```text
V4 = Q[x,y,z]_4
```

mean the 15-dimensional space of homogeneous polynomials of exact degree
four.  The transported signed-permutation group `B3` acts by

```text
(g.p)(X) = p(g^-1 X).
```

Put

```text
r2 = x^2+y^2+z^2,
R4 = r2^2,
M4 = x^4+y^4+z^4.
```

For distinct coordinate indices `i,j`, define the frozen cubic-axis
anisotropy

```text
a_ij(S) = sum_(v in S) v_i^4
          - 3 sum_(v in S) v_i^2 v_j^2.
```

Coordinate independence below means equality for the six ordered distinct
coordinate pairs, equivalently independence under signed permutations of the
frozen cubic axes.  It does not mean invariance under arbitrary real
orthogonal coordinate changes.

For `S1=Shell(2)`, `S2=Shell(4)`, and `S3=Shell(6)`, weights are explicitly

```text
w=(w1,w2,w3) in Q_(>=0)^3,
```

where `wi` is the common per-vector coefficient assigned to every vector of
`Si`.  These are not total shell masses.

For ordered indices `i,j,k,l in {1,2,3}`, freeze the full fourth-moment
tensor

```text
M_ijkl(w) = sum_(s=1)^3 ws sum_(v in Ss) v_i v_j v_k v_l.
```

Fourth-order isotropy means exactly that there exists `lambda in Q` such
that all 81 ordered components obey

```text
M_ijkl(w) = lambda(δ_ij δ_kl + δ_ik δ_jl + δ_il δ_jk).
```

This is a rank-four tensor condition, not a name for the single scalar
`a_ij`.  Because every shell has signed-permutation symmetry, every component
with an odd coordinate multiplicity vanishes, all `M_iiii` agree, and all
`M_iijj` for `i != j` agree.  Taking `lambda=M_1122`, the 81 residual rows
in the three weights are exactly 78 zero rows and three copies of
`(-4,32,-72)`.  Hence the full tensor condition is equivalent, in both
directions, to `-4w1+32w2-72w3=0`.

### Atomic target predicates

The accepted verifier prints one boolean and one name for every predicate
below.  A failure cannot be hidden inside a grouped boolean.

```text
A01a BASIS-GRAM                       Gram(b1,b2,b3)=A.
A01b POSITIVE-DEFINITE                leading principal minors=(2,3,4).
A01c ROOT-COUNT                       |R|=12.
A01d ROOT-CLASSIFICATION              R is exactly all e_i-e_j, i!=j.
A02a GRAM-TRIPLE-COUNT                the complete 12^3 filter accepts 48.
A02b UNIMODULAR                       every accepted matrix has det +-1.
A02c AUT-PREDICATE                    every accepted matrix preserves A.
A03a S4-FAITHFUL                      the S4 restriction set has size 24.
A03b SIGNED-S4-SIZE                   W has size 48.
A03c AUT-EQUALS-SIGNED-S4             the two explicit sets are equal.
A03d MINUS-I-OUTSIDE-S4               -I is outside the S4 factor.
A03e MINUS-I-CENTRAL                  -I centralises every Aut element.
A03f AUT-DIRECT-PRODUCT               the preceding marked model is S4 x C2.
A04a AUT-ORDER-HISTOGRAM              {1:1,2:19,3:8,4:12,6:8}.
A04b AUT-NO-ORDER-FIVE                no Aut element has order five.

D01a TRANSPORT-ISOMETRY               F^T F=A.
D01b TRANSPORT-INDEX                  det(F)=-2.
D01c IMAGE-IN-D3                      the three image columns lie in D3.
D01d INVERSE-FORMULA                  the displayed rational inverse is exact.
D01e D3-IN-IMAGE                      D3 basis generators have integral preimages.
D02a MINIMAL-SHELL-SIZE               |Shell(2)|=12.
D02b ROOT-TRANSPORT                   F(R)=Shell(2).
D03a CONJUGATES-INTEGRAL              every F g F^-1 is integral.
D03b SIGNED-GROUP-SIZE                signed permutations have size 48.
D03c TRANSPORTED-GROUP                F Aut F^-1 equals that signed group.
D04a SHELL4-AXES                      Shell(4)={+-2e1,+-2e2,+-2e3}.
D04b AXES-SPAN                        those axes span rank three.
D04c SIGNED-PRESERVE-D3               every signed permutation preserves D3.
D04d FULL-POINT-GROUP                 the shell ceiling and converse both hold.

F01a FINITE-FORM-NONDEGENERATE        det(A) mod 5 is nonzero.
F01b FINITE-ORTHOGONAL-SIZE           |O5|=240.
F01c FINITE-ORDER-HISTOGRAM           {1:1,2:51,3:20,4:60,5:24,6:60,10:24}.
F02a REDUCTION-HOMOMORPHISM           red_5 respects every ordered product.
F02b REDUCTION-ORTHOGONAL             im(red_5) is contained in O5.
F02c REDUCTION-INJECTIVE              ker(red_5)={I}.
F02d REDUCTION-IMAGE-SIZE             |im(red_5)|=48.
F02e REDUCTION-INDEX-FIVE             |O5|=5|im(red_5)|, with nonempty image.
F02f REDUCTION-HISTOGRAM              {1:1,2:19,3:8,4:12,6:8}.
F02g REDUCTION-NO-ORDER-FIVE          im(red_5) has no order-five element.
F03a A5-ORDER-DIVISIBLE-BY-FIVE       5 divides |A5|=60.
F03b A5XC2-ORDER-DIVISIBLE-BY-FIVE    5 divides |A5 x C2|=120.
F03c A5-NO-LIFT                       Cauchy plus Aut order census obstructs it.
F03d A5XC2-NO-LIFT                    the same typed obstruction applies.

Q01a EXACT-DEGREE-FOUR-DIMENSION      dim Q[x,y,z]_4=15.
Q01b FIXED-SPACE-DIMENSION            dim V4^B3=2.
Q01c RADIAL-QUARTIC-INVARIANT         R4 is invariant.
Q01d CUBIC-QUARTIC-INVARIANT          M4 is invariant.
Q01e INVARIANT-BASIS-RANK             R4,M4 are independent.
Q01f INVARIANT-BASIS-SPANS            they span the two-dimensional fixed space.
Q02a QUOTIENT-DIMENSION               dim(V4^B3/Q R4)=1.
Q02b M4-CLASS-NONZERO                 M4 is not radial.
Q02c QUARTER-TURN-GROUP-SIZE          the frozen generator has order four.
Q02d QUARTER-TURN-FIXED-DIMENSION     its fixed-space dimension is five.

S01a SHELL-SIZES                      (12,6,24,12).
S01b SHELL-ANISOTROPIES               (-4,32,-72,-64).
S01c SECOND-DIAGONAL-SYMMETRY         all M20 axis values agree.
S01d FOURTH-DIAGONAL-SYMMETRY         all M40 axis values agree.
S01e PAIRED-FOURTH-SYMMETRY           all M22 coordinate-pair values agree.
S01f ORDERED-ANISOTROPY-SYMMETRY      all six ordered a_ij agree.
S01g MIXED-SECOND-ZERO                all mixed second moments vanish.
S01h ODD-FOURTH-ZERO                  every odd-multiplicity quartic vanishes.
S01i RADIAL-MOMENT-IDENTITY           3M40+6M22=|S|N^2 on every shell.
S01j SHELL-NONISOTROPY                all four single-shell anisotropies are nonzero.

T01 FOURTH-TENSOR-INDEX-CARDINALITY   all 81 ordered index tuples occur once.
T02 B3-TENSOR-REDUCTION               each full shell tensor has the B3 shape.
T03 ISOTROPY-ANCHOR-COEFFICIENTS      shell M1122 values are (4,0,72).
T04 TENSOR-RESIDUAL-CENSUS            78 zero rows and 3 anisotropy rows.
T05 FULL-TENSOR-ISOTROPY-IFF          all 81 equations iff a.w=0.

C01a PER-VECTOR-COEFFICIENTS          a=(-4,32,-72).
C01b COEFFICIENTS-DIVISIBLE-BY-FOUR   exact division by four is integral.
C01c REDUCED-CONE-EQUATION            (-1,8,-18), so w1=8w2-18w3.
C02a FIRST-RAY-ON-CONE                (8,1,0) satisfies the equation.
C02b SECOND-RAY-ON-CONE               (0,9,4) satisfies the equation.
C02c RAYS-NONNEGATIVE                 all six displayed coordinates are >=0.
C02d FIRST-RAY-PRIMITIVE              gcd(8,1,0)=1.
C02e SECOND-RAY-PRIMITIVE             gcd(0,9,4)=1.
C02f SYMBOLIC-DECOMPOSITION           the displayed identity holds coefficientwise.
C02g DECOMPOSITION-UNIQUE             the two rays have rank two.
C02h DECOMPOSITION-COEFFICIENT-SIGNS  w1/8,w3/4 are nonnegative on the cone.
C02i CONE-COMPLETE                    the bidirectional symbolic proof is satisfied.
C02j TENSOR-WITNESSES                 both rays and (6,3,1) pass all 81 equations.
C03a FIRST-RAY-BOUNDARY               it has exactly two positive coordinates.
C03b SECOND-RAY-BOUNDARY              it has exactly two positive coordinates.
C03c INTERIOR-POSITIVE                (6,3,1) has three positive coordinates.
C03d INTERIOR-ON-CONE                 (6,3,1) satisfies the equation.
C03e FACE-W2-ZERO                     signs force w1=w3=0 when w2=0.
C04a TOTAL-MASS-INTEGRAL-SCALING      clearing denominator three is exact.
C04b TOTAL-MASS-EQUATION              (-1,16,-9).
C04c WEIGHT-TYPES-DISTINCT            it differs from the per-vector equation.
```

`I01 AUT-ORDERS-RESOLVED` and `I02 FINITE-ORDERS-RESOLVED` are integrity
checks, not scientific atoms: a zero order at the frozen group bound causes
`STOP`, never `NEGATIVE`.

The completeness proof for `A02` is the root-image lemma: an integral
isometry sends each displayed basis root to a root, so every element occurs
among the `12^3` triples; every accepted unimodular triple conversely
preserves `A`.  For `D04`, a real lattice isometry permutes `Shell(4)`;
because that shell is exactly the six spanning axes, the isometry is signed
permutation, while `D04c` proves the converse.  For `C02`, substituting
`w1=8w2-18w3` gives

```text
w=(w1/8)(8,1,0)+(w3/4)(0,9,4),
```

with nonnegative coefficients, and rank two gives uniqueness.  These are
unbounded algebraic proofs; no bounded scan is evidence for them.

The full-point-group, lift, invariant-space, cone, and face statements carry
explicit proofs above.  Finite enumeration audits only the declared finite
sets and never substitutes a bounded scan for an unbounded assertion.

## Frozen field 2: accepted code

The adjacent `verify.py` is the only accepted verifier for this probe.  It is
a newly reviewed implementation of this corrected contract.  The builder has
seen the earlier incubation programs, so no code-independence or blindness
claim is made for `verify.py`.

Requirements:

```text
Python 3.12, standard library only
integer, Fraction, and explicit F_5 arithmetic only
no float, random input, argv input, external file, network, timestamp,
locale-dependent value, environment echo, or unordered rendering
empty stderr and deterministic sorted stdout
all scientific gates, integrity checks, and controls execute before summary
PROBE-PASS and NEGATIVE exit zero; STOP exits nonzero
```

Exact completeness procedures:

1. construct roots directly from the typed `Z^4` definition;
2. filter all `12^3=1728` ordered root triples;
3. independently construct all 48 restrictions of `eps P_sigma`;
4. compute integral orders with the finite bound 48;
5. verify `F`, its exact rational inverse, D3 shells, and conjugates;
6. enumerate every one of the `125^3` ordered column triples over `F_5`,
   pruned only by the six Gram equations defining `O5`;
7. compute finite orders with bound 240 and check the red_5 homomorphism;
8. build all 15 exact-degree-four monomials and compute fixed-space ranks
   by exact rational row reduction;
9. enumerate `Shell(N)` with the complete bound `|yi|<=isqrt(N)`;
10. evaluate every one of the 81 ordered fourth-tensor components, check the
    exact residual-row census, and reduce full isotropy symbolically;
11. certify cone completeness, rays, and faces by symbolic rational
    identities, never by a weight search.

The sole formal command is

```text
python3 probes/P-A3-FCC-POINT-GROUP-1/verify.py
```

## Frozen field 3: carriers, data, and finite bounds

There are no external data.

```text
integral carrier:    L in the displayed b basis
transport:           F Z^3 = D3 in standard coordinates
finite carrier:      (F_5^3,A mod 5)
polynomial carrier:  homogeneous V4, dimension 15
moment coefficients: Q_(>=0)^3, common per-vector weights
```

Completeness is fixed independently of adjustable cutoffs:

```text
roots:       exact norm-two classification in sum-zero Z^4
Aut:         all 12^3 ordered root-image triples
O5:          all 125^3 ordered column triples
orders:      finite group bounds 48 and 240
V4:          all 15 exact-degree-four monomials
shells:      coordinate bound isqrt(N), derived from yi^2<=N
weight cone: symbolic parametrization and sign proof, no search
```

No bound, carrier, weight type, threshold, or outcome may move after pinning.

## Frozen field 4: systematics, exposure, and scope

1. This probe concerns only the explicitly declared standard `A3/D3`
   lattice.  `FCC` is a conventional lattice alias.
2. Issue #193 remains `UNTYPED`.  This probe neither invokes nor repairs
   `GATE-LIFT-KERNEL-Z`.
3. `L`, `D3`, `R`, and all shell coefficients are probe-local and are not
   identified with the checkpoint trace kernel, `J-STEP`, `CODEC-TR4`, a
   decoder carrier, photon carrier, or internal step set.
4. Issue #195 and `CARRY-PENTAD` concern differently typed carriers.  Their
   overlapping counts are collision controls, not premises or independent
   confirmation.
5. F03 concerns only subgroup lifts through this exact `red_5` diagram.  It
   says nothing about icosahedral actions on another lattice.
6. Q01-Q02 concern homogeneous exact degree four only.
7. S01 covers only norms 2,4,6,8.  C01-C04 cover only the first three shells.
8. The weights are unnormalised algebraic coefficients.  No probability,
   Born weight, shell selection, L6 measure, or physical isotropy is claimed.
9. There is no operator, dispersion, polarization, holonomy, time,
   continuum, SI, or observed-photon statement.
10. Scientific dependencies: none.  Issues #193, #195, #274, and #275 are
    governance, boundary, collision, or exposure records, not theorem
    premises.

### Mandatory exposed-result disclosure

The positive numerical outcome was known before issue #275 and before this
prospective pin:

```text
incubation branch: notes/c-photon-point-group-1
incubation commit: 56674bb294cf76344aa6bde4b8175fd85c59eb52
incubation parent: 470d95826037d75e29530177171763f1376b4614
old PREREG SHA-256:
  019887766014890fc6f1a4b79f0b541740921a0dd772846535b2d5cb2aa9014b
old PREREG bytes: 10374
old verifier stdout SHA-256:
  dcad65a5cb750dffcf12c958c4c82b6b8006ed90cc65056efeec43568578087e
old self-break stdout SHA-256:
  a449e9a8bc99c222cf9fe8d458b4d4b146ab07dc30cfbd98e5d423559290ce42
cross-model record: issue #274, BREAK FOUND — SPECIFICATION/TYPE
```

Those runs are non-formal incubation records and cannot become
`EXPECTED.txt`, `RUN.md`, evidence, or architecture records.  The current
builder read the old PREREG, verifier, breaker, README, RESULT, and stdouts
after freezing the issue #274 blind verdict.  No information-firewall claim
is made for this builder or the new verifier.  The new verifier is a
prospective conformance audit of an exposed result.

A fresh post-pin breaker must receive only this exact `PREREG.md`, issue #275,
and Public Canon v36.  It must not receive or open the accepted `verify.py`,
old implementation, any stdout, or expected result.  Its information
firewall and separately derived artifact, not its model label alone, are the
independence claim.

## Frozen field 5: type-correct controls and outcomes

Every control stays inside an explicitly declared ambient type, or explicitly
mutates a stated subtype, predicate, or expected constant.  A control may
therefore be rejected by the frozen nonnegative-cone subtype while remaining
in the ambient rational weight space.  There is no impossible rank-three
integral order-five fixture.

Exact control output names are frozen as follows:

```text
K01 WRONG-GRAM-ROOT-TRIPLE
K02 PROPER-INTEGRAL-SUBGROUP
K03 SUBGROUP-HISTOGRAM
K04 BAD-ISOMETRY-TRANSPORT
K05 WRONG-SHELL-AXES
K06 PROPER-POINT-SUBGROUP
K07 SPECIAL-ORTHOGONAL-SUBGROUP
K08 PROPER-REDUCTION-IMAGE
K09a SECTION-RIGHT-INVERSE
K09b SECTION-HOMOMORPHISM
K10 QUARTER-TURN-INVARIANTS
K11a WRONG-SHELL-SIZE-TABLE
K11b WRONG-SHELL-ANISOTROPY-TABLE
K12 ASYMMETRIC-D3-SUBSET
K13 OFF-CONE-WEIGHT
K14a FIRST-BOUNDARY-NOT-STRICT
K14b SECOND-BOUNDARY-NOT-STRICT
K15 NONZERO-OTHER-FACE
K16a PER-VECTOR-RAY-ACCEPTED
K16b TOTAL-MASS-ALIAS-REJECTED
K17 DEGREE-AT-MOST-FOUR-ALIAS
K18 NONINJECTIVE-REDUCTION-MUTATION
K19 ORDER-FIVE-FINITE-SUPERGROUP
K20 RADIAL-QUOTIENT-ZERO
K21 WRONG-RADIAL-MOMENT-RHS
K22 EQUATION-WITHOUT-NONNEGATIVITY
```

```text
K01 A root triple made of (b1,b2,b1+b2) is rejected by the Cartan-Gram
    predicate.
K02 The determinant-one subgroup of Aut has order 24 and is rejected as
    the full 48-element Aut group.
K03 Its histogram {1:1,2:9,3:8,4:6} is rejected as the full histogram.
K04 F with its first column negated fails F^T F=A.
K05 Shell(2) is rejected by the Shell(4)-axes predicate.
K06 The determinant-one signed permutations are rejected as the full point
    group.
K07 The determinant-one finite orthogonal subgroup is rejected as O5.
K08 The reduction of the determinant-one Aut subgroup is rejected as the
    full 48-element reduction image.
K09a-K09b That smaller image has an explicit integral section, preventing
    F03 from widening to a claim that no subgroup lifts.  The inverse table
    for red_5 on the determinant-one subgroup is checked separately as a
    right inverse and as a homomorphism on every ordered pair.
K10 The concrete quarter-turn subgroup has invariant dimension 5 and is
    rejected by the full-group dimension-two predicate.
K11a A wrong shell-size table is rejected.
K11b Replacing a(Shell(2))=-4 by zero is rejected.
K12 The in-type subset {(1,1,0),(-1,-1,0)} of D3 fails cubic-coordinate
    independence and the full B3 tensor-shape predicate.
K13 The in-type weight (1,1,1) is off the per-vector cone, residual -44,
    and fails the full 81-component isotropy predicate.
K14a-K14b Each boundary ray is separately rejected as a positive triple.
K15 A nonzero point on the face w3=0 prevents the face exclusion from
    being applied indiscriminately to every face.
K16a-K16b The ray (8,1,0) is separately accepted by the per-vector equation
    and rejected by the total-mass equation.
K17 The 35-dimensional degree-at-most-four space is rejected as the
    15-dimensional exact-degree-four carrier.
K18 A constant-identity map Aut->O5 has a nontrivial kernel and is rejected
    by the reduction-injectivity predicate.
K19 The full finite orthogonal supergroup carries 24 order-five elements and
    is rejected by the no-order-five image predicate.
K20 The radial quartic has zero quotient class and is rejected as the M4
    nonzero-class witness.
K21 The correct first-shell moment identity rejects a right-hand side
    mutated by one.
K22 The negative of the first ray satisfies the linear equation but is
    rejected by nonnegativity.
```

Outcomes:

```text
PROBE-PASS
    Every scientific atom is true, both integrity checks pass, and every
    control behaves as frozen.  This is only the local verifier verdict.  It
    is never by itself `THEOREM-CERTIFIED` and makes no status move.

NEGATIVE
    Exhaustive computation terminates, both integrity checks and every
    control behave correctly, and at least one scientific atom is false.
    Every failed atom is printed.  This is an exit-zero scientific result.

STOP
    authority, collision, pin, hash, security, type, completeness,
    determinism, stderr, transcript, or architecture validation fails; a
    control does not fire; an exception prevents exhaustive completion; or
    a bounded search replaces a symbolic proof.  STOP exits nonzero.
```

Only a later `RESULT.md` may map `PROBE-PASS` to `THEOREM-CERTIFIED`, and
only after exact public pin readback, the fresh blind breaker, one compliant
formal Linux run, and byte-identical success in both required architecture
jobs.  The verifier cannot certify those governance facts itself.

A fired falsifier is preserved.  It cannot be hidden by changing a bound,
weight type, statement, control, or outcome.  A defect in either pinned file
invalidates this probe name; do not amend, resume, or reinterpret it.

## Frozen field 6: action layer

```text
L1 exact algebra only:
  integral lattice -> isometric integral presentation
  integral automorphism group -> finite mod-five orthogonal image
  exact rational invariant space
  exact finite-shell moment tensors and symbolic rational cone
```

There is no L1-to-L2 lift and no named interlayer gate.  In particular, this
probe does not adopt an A3 photon carrier, decoder step set, spatial manifold,
L5 stream, or L6 measure.

After the public pin, a fresh blind breaker must freeze before execution.
The first formal run must occur on an authorized Linux or Linux-compatible
runner.  Only afterward may `EXPECTED.txt`, `RUN.md`, and `RESULT.md` be added.
