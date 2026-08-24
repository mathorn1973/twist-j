# C-GRAVITY-PLACE-METRIC-SEAM-N

**Status:** NON-CANONICAL INCUBATION NOTE. No public T/D/C/H/O/F status is created here.

**Date:** 2026-08-09

**Owner lock:** issue #312

**Scope:** preserve two gravity seams for later falsification-first work:

1. the map from the archimedean scale direction to a `1+3` metric block;
2. the normalization that enters the registered active-cell gravity action.

This file changes no Canon, Registry, Frontier, evidence row, gate, probe, verifier, status, or release object.

---

## 0. Public authority and firewall

The authority at creation is Public Canon v39 on `mathorn1973/twist-j main`:

```text
TAG:            canon-v39
CONTENT_COMMIT: ab17b10412d03bf1cd69791fe22c66252502b2d4
CANON_SHA256:   698df2212f0bc782de2fb50ff04fb4026d1e276743d6fae7f10607cca770b556
CANON_BYTES:    187370
BASE_MAIN:      9f144e0ebaf556b5dfd49a9acb6dd5aa81fe5307
```

The following registered scopes remain exactly where they are:

```text
J-PROJECTIONS                 [T]
LOG-AXES-INDEPENDENCE         [T]
CODEC-TR4                     [T]
MEASURE-SPATIAL-ONLY          [T]
GOLDEN-SIX-LINE-SYM2-FRAME   [T]
READING-SPLIT                 [D]
FRW-CANONICAL-FORM            [T]
GRAVITY-BRIDGE-LAW            [D]
CURVATURE-OPERATOR-CANONICAL  [O]
SQRT-PHI-TIME-GRAVITY         [O]
METRO-EDGE-SCALE              [O]
FRW-INHOM                     [O]
```

This Note does not close, weaken, strengthen, duplicate, or bypass any of them.

The public gravity reproduction already states its own boundary: `FRW-CANONICAL-FORM [T]` closes the displayed rank-1 lapse-action algebra, including the exact `864 pi` cell volume and the forced positive fiber multiplier, but does not claim a unique source projector or amplitude ansatz. `GRAVITY-BRIDGE-LAW [D]` does not claim the SI value of Newton's constant.

---

## 1. The arithmetic picture to preserve

Work in

```text
K = Q(zeta_5),
phi = (1 + sqrt(5))/2,
J = 1 + zeta_5^2 = zeta_5 / phi.
```

The archimedean completion is

```text
K tensor_Q R ~= C x C,
```

so `r_1 = 0`, `r_2 = 2`, and the Dirichlet unit rank is

```text
r_1 + r_2 - 1 = 1.
```

At the exact arithmetic level the unit group has one free rank-one direction and finite torsion. In logarithmic coordinates the product formula removes one of the two real modulus coordinates, leaving one noncompact real direction.

That statement is one-dimensional.

The public spatial carrier is instead three-dimensional. `MEASURE-SPATIAL-ONLY [T]` records the declared trace/conformal/spatial split with spatial base `ker(Tr_4)` of dimension `d = 3`, and `READING-SPLIT [D]` says only that the partial decoder reads its registered legs in the stated ways. It does not prove decoder totality, uniqueness, or completeness.

The seam is therefore not

```text
one archimedean direction versus another archimedean direction.
```

It is

```text
one arithmetic scale coordinate
        ->
one normalized scale of a separate three-dimensional spatial block.
```

That arrow requires its own theorem or its own explicit dictionary status. It is not the product formula itself.

---

## 2. First seam: PLACE-TO-METRIC-BLOCKS

`PLACE-TO-METRIC-BLOCKS` is a roadmap label only. It is not a Registry claim and not a formal gate.

The future question is to classify the complete admissible maps from the exact arithmetic scale data into the declared metric carrier.

A useful abstract target is

```text
V_metric = L_tau direct-sum W,

dim L_tau = 1,
dim W = 3,
```

with a Lorentz-signature metric and a scalar static source class.

The classification must answer at least five independent questions.

### G1. Carrier and signature

Which exact registered object supplies

```text
1 time direction + 3 spatial directions?
```

The real dimension four of `K tensor_Q R` does not by itself supply Lorentz signature. A positive Hermitian carrier, a Hermitian `2 x 2` determinant carrier, and a decoder `1+3` split are different objects and must not be silently identified.

A future gate must name the carrier, the metric form, the equality relation, and the map from the arithmetic source into that carrier.

### G2. Spatial centrality, not merely spatial symmetry

Let `W` be the declared three-dimensional spatial representation and let `G_space` be the exact symmetry group used by the candidate.

For a scalar source, the load-bearing statement should be about the response operator itself. A sufficient form would be

```text
C : 1_source -> Sym^2(W*)
```

with `C` equivariant and

```text
dim (Sym^2(W*))^(G_space) = 1.
```

Then the response must lie on the unique invariant metric line:

```text
C(rho) = c(rho) h_0.
```

This kills the traceless shear sector.

The distinction matters because the public theorem `GOLDEN-SIX-LINE-SYM2-FRAME [T]` already carries a negative control showing that lower-order isotropy is insufficient: the cube construction has the expected isotropic first average but its second-order operator is not in the rational `so(3)` commutant. Therefore a future gravity derivation must constrain the coupling/response operator, not merely exhibit an isotropic Gram or isotropic first moment.

### G3. One block scale versus spatial volume

Assume G2 has already forced an isotropic spatial metric

```text
h(N) = f(N)^2 h_0.
```

There are still at least two inequivalent scalar quantities attached to this block:

```text
length/block scale      s(h)   = f,
spatial volume scale    vol(h) = f^d.
```

For `d = 3`, these are `f` and `f^3`.

The arithmetic product formula does not by itself label either one as the physical image of the second place.

A future gate must therefore explain why the place map lands on the normalized block scale

```text
s(h) = (det h / det h_0)^(1/(2d))
```

rather than the volume

```text
vol(h) = (det h / det h_0)^(1/2).
```

This is the point at which the multiplicity `d = 3` either disappears by normalization or survives as an exponent.

### G4. Reciprocity and orientation

The candidate must freeze the orientation and sign conventions before using the product relation.

Schematically, if the time block is read as `N^-1`, the intended scale reading is

```text
place_1 -> -log N,
place_2 -> +log s(h).
```

The future class must forbid an unnamed multiplier, reciprocal swap, or orientation change after the result is known.

### G5. Completeness

Finding one attractive map is not enough.

The complete admissible class must be declared and classified. A possible terminal grammar is

```text
UNIQUE      exactly one equivalence class survives
NONUNIQUE   at least two inequivalent classes survive
EMPTY       the complete frozen class is empty
STOP        typing, admissibility, equivalence, or completeness is unfinished
```

These words are roadmap outcomes only until a separate public claim lock freezes the actual class and decision rules.

---

## 3. Explicit negative witness: gamma 1 versus gamma 1/d

This section is not a new PPN claim. Public Canon v39 has no Registry row promoted here for `gamma = 1`.

Its purpose is narrower: show that the product formula plus isotropy does not by itself choose how a three-dimensional block is scalarized.

Take the static conformal family

```text
ds^2 = N^-2 dn^2 - f(N)^2 h_0.
```

Write

```text
N = exp(Phi),
f(N) = exp(gamma Phi)
```

at weak field. Then

```text
g_00 = 1 - 2 Phi + O(Phi^2),
g_ij = -(1 + 2 gamma Phi) h_0,ij + O(Phi^2).
```

Now compare two scalarizations of the same isotropic spatial block.

### Candidate A: normalized block scale

If reciprocity is imposed on the one block scale,

```text
N^-1 f = 1,
```

then

```text
f = N,
gamma = 1.
```

### Candidate B: full spatial volume

If reciprocity is imposed on the spatial volume,

```text
N^-1 f^d = 1,
```

then

```text
f = N^(1/d),
gamma = 1/d.
```

At `d = 3`:

```text
gamma = 1/3.
```

The `gamma = 1/3` branch is not proposed physics. It is a counterexample to the inference

```text
product formula + isotropy => gamma = 1.
```

Any future proof of the `gamma = 1` route must rule out the volume reading by a typed structural condition, not by observation after the fact.

---

## 4. What the current FRW theorem does and does not do

The current public gravity verifier contains the exact step

```text
sum_(i<j) H_i H_j = 3 H^2
```

on the isotropic `d = 3` background, with

```text
C(3,2) = 3.
```

This is a valid component of `FRW-CANONICAL-FORM [T]` at its registered scope.

It does not prove that an arbitrary source response must satisfy

```text
H_1 = H_2 = H_3.
```

That is not a defect in the registered theorem because the public scope does not claim source-projector uniqueness or a complete metric decoder. It is a warning against using the FRW result later as if isotropy itself had already been selected by the arithmetic place structure.

A future derivation of isotropy should therefore attach to the response operator or source representation, not be imported from the homogeneous ansatz it is meant to justify.

---

## 5. Second seam: ACTIVE-CELL-NORMALIZATION

`ACTIVE-CELL-NORMALIZATION` is also a roadmap label only.

The public reproduction `reproduce/gravity-chain` verifies the exact chain

```text
V_cell^act = 2 (d+1)^2 d^3 pi,
d = 3,
V_cell^act = 864 pi,
G_nat = d^3 = 27.
```

It further verifies the master closure in which the positive fiber multiplier is forced to

```text
k_f = 1.
```

The downstream arithmetic is not the target of this Note. The audit target is upstream:

```text
Why is the active-cell normalization exactly
2 (d+1)^2 d^3 pi?
```

The derivation should expose the origin of each factor:

```text
2,
(d+1)^2,
d^3,
pi,
```

and must make explicit whether any factor counts

```text
orientation,
double cover,
fiber circumference,
source multiplicity,
cell multiplicity,
normalization of the action,
or another exact combinatorial object.
```

A future derivation is incomplete if one of these factors is fixed only because the final value `864 pi` is already known.

The same applies to omitted factors. The proof must rule out hidden multiplicities such as an extra `2`, `1/2`, orientation count, double cover, or fiber count by type or symmetry, not by numerical agreement downstream.

---

## 6. The alternative k-form and the dimension-three compatibility identity

A second parametrization encountered in the audit is

```text
V_alt(d) = (2 pi/3) k^2 (k-3),
k = d(d+1).
```

Substituting `k = d(d+1)` gives

```text
V_alt(d)
 = (2 pi/3) d^2 (d+1)^2 (d(d+1)-3).
```

The registered form is

```text
V_reg(d) = 2 pi (d+1)^2 d^3.
```

For positive `d`, equality requires

```text
(2 pi/3) d^2 (d+1)^2 (d(d+1)-3)
 = 2 pi (d+1)^2 d^3.
```

Cancel the common nonzero factor `2 pi d^2 (d+1)^2`:

```text
(d(d+1)-3)/3 = d.
```

Therefore

```text
d^2 - 2d - 3 = 0,
(d-3)(d+1) = 0.
```

For positive dimension:

```text
d = 3.
```

This observation has two possible meanings and they must not be conflated.

### Case 1. Independent derivations

If `V_alt(d)` and `V_reg(d)` arise independently from two frozen constructions whose assumptions do not already set `d = 3`, then their compatibility selects `d = 3` inside that joint class.

### Case 2. Reparametrization after d = 3

If `V_alt` was written only after `d = 3` or after `864 pi` was already fixed, then the compatibility carries no new selection content. It is an identity engineered around the known point.

A future audit must establish provenance before assigning any scientific weight to the compatibility.

---

## 7. Why k = 12 uniqueness is not a selection theorem

If the target `864 pi` is already known and one solves

```text
(2 pi/3) k^2 (k-3) = 864 pi,
```

then

```text
k^2(k-3) = 1296,
k^3 - 3k^2 - 1296 = 0.
```

Factor exactly:

```text
k^3 - 3k^2 - 1296
 = (k-12)(k^2 + 9k + 108).
```

The quadratic factor has discriminant

```text
9^2 - 4*108 = -351 < 0.
```

Hence

```text
k = 12
```

is the unique real root, not merely the unique integer root in a selected finite window.

But this is inverse uniqueness. It says that the already fixed output `864 pi` determines `k` inside that chosen formula. It does not derive the formula or the target.

Therefore a statement such as

```text
k = 12 is unique in [4,64]
```

is mathematically weaker than the exact factorization above and scientifically irrelevant as selection evidence. If retained at all, it should be a negative control against accidental root multiplicity, not part of the derivation.

---

## 8. Candidate decision surface for the normalization seam

A later formal attack should not start by recomputing `27`. It should start by freezing the source class for the normalization.

At minimum it should decide:

```text
N1. source object
    Which registered action, cell, support, or carrier owns V_cell^act?

N2. factor derivation
    Derive 2, (d+1)^2, d^3, and pi independently of the final target.

N3. multiplicity closure
    Prove that no omitted orientation, cover, fiber, or cell multiplicity
    changes the normalization.

N4. provenance
    Decide whether the alternative k-form is independent or a rewrite.

N5. completeness
    Classify every normalization admitted by the frozen source and
    equivalence relation.
```

A possible future terminal grammar is again

```text
UNIQUE
NONUNIQUE
EMPTY
STOP
```

with the same warning: this Note does not register those outcomes or authorize a computation.

---

## 9. Why the two seams are independent

The first seam asks

```text
one arithmetic logarithmic direction
        ->
one normalized scale of a three-dimensional metric block.
```

It controls the form of the metric response.

The second asks

```text
one registered action/cell construction
        ->
exact normalization V_cell^act = 864 pi.
```

It controls the strength of the equation-layer gravity chain.

A proof of the first does not derive the second. A proof of the second does not derive the first.

This separation is useful because it localizes failure:

```text
place-to-block failure
    does not falsify the exact 864 pi arithmetic already registered;

normalization failure
    does not falsify J-PROJECTIONS, CODEC-TR4, the d=3 spatial carrier,
    or the product formula.
```

The seams should therefore remain separate if they later become public program objects.

---

## 10. Falsification-first summary

The strongest useful negative witnesses currently visible are:

```text
A. BLOCK SCALE VERSUS VOLUME
   isotropy plus reciprocity admits gamma = 1 and gamma = 1/d
   until the scalarization of the spatial block is fixed.

B. RESPONSE VERSUS GRAM ISOTROPY
   the public GOLDEN-SIX-LINE-SYM2-FRAME negative control shows that
   lower-order isotropy does not force a second-order operator into the
   spatial commutant.

C. TARGET INVERSION
   k = 12 is uniquely recovered from 864 pi inside the alternative
   polynomial, but inverse uniqueness is not a derivation of the input
   normalization.

D. PROVENANCE SPLIT
   the two V_cell formulae select d = 3 only if they were independently
   derived without already assuming d = 3 or 864 pi.
```

A later mechanism should be considered stronger only if it eliminates these negative witnesses by exact type, symmetry, or classification, not by choosing the branch that reproduces a desired physical number.

---

## 11. Promotion boundary

This Note preserves a research route. It creates no new public scientific status.

In particular it does **not** claim:

```text
that the unit group derives Lorentz signature;
that the two archimedean places are literally time and space;
that isotropy is currently derived from J;
that gamma = 1 is a Public Canon theorem;
that gamma = 1/3 is a TWIST-J prediction;
that V_alt is a Canon formula;
that d = 3 is newly selected by the compatibility identity;
that G_nat = 27 is weakened or strengthened;
that the SI value of G is derived;
that any current O row is closed.
```

Any formal continuation requires a fresh public claim lock and must freeze, before computation:

```text
layer,
carrier,
source class,
map class,
equality and equivalence,
symmetry group,
normalization,
complete admissible class,
decision conditions,
and every cross-layer lift.
```

No verifier is authorized by this Note.

---

## 12. Repository sources retained by reference

Current public objects relevant to this Note:

```text
STATUS.md
POLICY.md
AGENTS.md
canon/CORE.md
canon/CANON.md
canon/FRONTIER.md
canon/REGISTRY.tsv
reproduce/gravity-chain/README.md
reproduce/gravity-chain/verify.py
```

The Note is intentionally self-contained enough to recover the two questions even if the public frontier later moves:

```text
PLACE-TO-METRIC-BLOCKS:
    why one arithmetic scale coordinate is the normalized scale of one
    three-dimensional spatial block, including isotropy and completeness.

ACTIVE-CELL-NORMALIZATION:
    why the action carries exactly 2 (d+1)^2 d^3 pi before the downstream
    864 pi -> 27 arithmetic is used.
```

That is the preservation target. Nothing is promoted here.
