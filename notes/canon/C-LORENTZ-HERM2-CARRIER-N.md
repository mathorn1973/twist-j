# C-LORENTZ-HERM2-CARRIER-N common causal carrier predefinition (NON-CANONICAL)

```text
STATUS:                    NON-CANONICAL INCUBATION PREDEFINITION
AUTHORITY:                 NO NORMATIVE AUTHORITY
PUBLIC BASE:               470d95826037d75e29530177171763f1376b4614
PUBLIC CANON:              Public Canon v36 / canon-v36
PUBLIC ACTIVATION COMMIT:  a2c96226fc0ec994865d323dfc2b5c72fdd9dc41
PUBLIC CONTENT COMMIT:     df64035f6f0cadbeb17f539eaeec5d8d0f444515
PUBLIC CANON SHA-256:      c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5
PUBLIC CANON BYTES:        175814
CLAIM ISSUE:               276
INCUBATION ITEM:           C-LORENTZ-HERM2-CARRIER-N
ACTION LAYER:              L4 QUADRATIC SUPPORT ONLY
FORMAL PROBE:              NONE
PREREGISTRATION:           NONE
VERIFIER / RUN:            NONE
CANON / TABLE CHANGE:      NONE
SCIENTIFIC PROMOTION:      NONE
```

This note freezes one narrow construction surface for the next Lorentz work.
It does not claim that the construction has been proved, that the Lorentz
density statement is publicly registered, or that any physical decoder is
Lorentz invariant.

The target is smaller than an end-to-end Lorentz program. It asks only whether
the already public exact ingredients can be assembled on one typed
four-dimensional Hermitian carrier with one determinant form and one future
cone.

No computation is performed by this note. Any future computation must receive
its own prospective pin before execution.

## 1. Exact public position

The controlling public inputs are:

```text
BOOST-READING-SPLIT              [T]
BOOST-COUNT-LADDER               [D]
CENTRAL-LIFT-PHASE               [T]
COLOR-INTEGRAL-LIFT              [T]
COLOR-CM-2I-SEMILINEAR-PAIR      [T]
```

Their scopes remain unchanged.

`BOOST-READING-SPLIT [T]` supplies the exact rapidity arithmetic. It does not
force the velocity dictionary.

`BOOST-COUNT-LADDER [D]` reads the count as rapidity and the resulting ratio as
velocity. It is a dictionary, not a carrier theorem.

`CENTRAL-LIFT-PHASE [T]` supplies the exact normalized Hermitian action of the
J lift and the fifth-power pure-boost statement. Its registered scope
explicitly excludes a positive or causal cone, a common carrier, a decoder,
and every L5 or L6 lift.

`COLOR-INTEGRAL-LIFT [T]` supplies a marked integral two-generator model of
`2I` over `Z[zeta_5]`.

`COLOR-CM-2I-SEMILINEAR-PAIR [T]` supplies, on the single marked `rho` branch,
the invariant totally positive definite Hermitian form `H0` and its exact
one-dimensional invariant-form line.

Public Canon v36 also contains the narrative sentence that the group generated
by icosahedral rotations and the J boost is dense in `SO+(3,1)`. The public
Registry contains no density row. Under the public authority rule, that
sentence is not by itself a registered public claim.

Public Canon v36 further states that no end-to-end Lorentz closure is asserted.
This note does not alter either fact.

## 2. Incubation objective

Freeze one candidate datum

```text
D_LOR = (K, F, conjugation, sigma_1, V_H, q, C_plus,
         rho, H0, A_J, R_2I, B_J, equivalence)
```

with the following meaning:

```text
K          = Q(zeta_5),
F          = K^+ = Q(sqrt(5)),
conjugation = complex conjugation on K/F,
sigma_1    = the principal archimedean embedding,
V_H        = Herm_2(K/F),
q          = determinant,
C_plus     = the closed future cone under sigma_1,
rho        = the marked integral 2I representation,
H0         = the invariant totally positive Hermitian form,
A_J        = diag(J,1),
R_2I       = the congruence action induced by rho,
B_J        = the normalized congruence action induced by A_J.
```

The candidate must establish only a common L4 carrier. Density, continuity
transfer, field invariance, decoder action, metrology, and experiment remain
separate stages.

## 3. Native Hermitian carrier

Let

```text
j = zeta_5,
K = Q(j),
F = Q(j + j^-1) = Q(sqrt(5)),
bar(x) = complex conjugation.
```

Define the four-dimensional `F`-vector space

```text
V_H = Herm_2(K/F)
    = { X(u,v,w) = [[u,w],[bar(w),v]] : u,v in F, w in K }.
```

Because `[K:F] = 2`,

```text
dim_F(V_H) = 1 + 1 + 2 = 4.
```

Define the quadratic form

```text
q(X) = det(X) = u v - w bar(w) in F.
```

Its polarized bilinear form is

```text
B_q(X,Y) = (q(X+Y) - q(X) - q(Y))/2.
```

All equality in this note is exact equality in `K`, `F`, or the displayed
matrix carrier. No decimal witness is admissible for a scientific gate.

### 3.1 Exact native diagonalization

Put

```text
delta = j - j^-1.
```

Then

```text
bar(delta) = -delta,
delta^2 = -(phi + 2).
```

Every `w in K` is uniquely

```text
w = x + y delta,    x,y in F.
```

Therefore

```text
w bar(w) = x^2 + (phi + 2) y^2.
```

With

```text
t = (u+v)/2,
z = (u-v)/2,
```

we obtain

```text
q = t^2 - z^2 - x^2 - (phi + 2) y^2.
```

Under the principal embedding, `phi + 2 > 0`, so `q` has real signature
`(1,3)`.

This native form is preferred to an unnamed rescaling of `y`. A standard
Minkowski coordinate may be introduced later only by a named exact extension
and a named equivalence gate.

## 4. Future cone and boundary

Under the principal embedding, define

```text
C_plus = { X in V_H : sigma_1(X) is positive semidefinite }.
```

For a `2 x 2` Hermitian matrix this is equivalent to

```text
sigma_1(u) >= 0,
sigma_1(v) >= 0,
sigma_1(q(X)) >= 0.
```

The interior is

```text
C_plus_open = { X : sigma_1(X) is positive definite }.
```

The causal boundary is

```text
partial C_plus = { X in C_plus : q(X) = 0 }.
```

The zero matrix belongs to the closed cone and to its boundary. No division by
`q(X)` is permitted at the boundary.

This note uses the cone only as an exact L4 order structure. It does not call a
cone point an event, state, observation, particle, or measured spacetime
coordinate.

## 5. The J action on the native carrier

Use the exact public element

```text
A_J = diag(J,1) in GL_2(K).
```

Since

```text
J = phi^-1 j,
J bar(J) = phi^-2,
|det A_J| = phi^-1
```

under the principal embedding, define the normalized Hermitian action

```text
B_J(X) = A_J X A_J^dagger / phi^-1
       = phi A_J X A_J^dagger.
```

For `X = X(u,v,w)` this gives the exact formula

```text
B_J : (u,v,w) -> (phi^-1 u, phi v, j w).
```

Therefore

```text
q(B_J X) = q(X).
```

The proof is direct:

```text
(phi^-1 u)(phi v) - (j w)(bar(j) bar(w))
= u v - w bar(w).
```

Because `B_J` is a positive scalar times Hermitian congruence,

```text
B_J(C_plus) = C_plus,
B_J(C_plus_open) = C_plus_open.
```

The fifth power is

```text
B_J^5 : (u,v,w) -> (phi^-5 u, phi^5 v, w).
```

Thus the transverse phase closes after five actions and the fifth power is a
pure boost on the two null coordinates.

In the native null-coordinate convention

```text
u = t+z,
v = t-z,
```

one application has rapidity `ln phi` together with the transverse phase `j`.
The pure fifth power has rapidity `5 ln phi`.

The exact algebra above is a candidate inline proof, not a status promotion by
this note.

## 6. The marked 2I action

Let

```text
rho : 2I -> SL_2(O_K)
```

be the exact marked representation supplied by `COLOR-INTEGRAL-LIFT [T]`.
A future promotion package must import the literal public matrices for the
marked generators. A theorem-family name is not enough.

Define

```text
R_g(X) = rho(g) X rho(g)^dagger.
```

Since `det rho(g) = 1`,

```text
q(R_g X) = q(X).
```

Hermitian congruence also gives

```text
R_g(C_plus) = C_plus,
R_g(C_plus_open) = C_plus_open.
```

The center acts trivially:

```text
R_(-I)(X) = X.
```

Therefore the induced action factors through

```text
2I/{+I,-I} ~= A5.
```

This factorization is the candidate spatial rotation action. It is not yet a
proof that the exact marked matrices used here are typed on the same basis as
`A_J`.

## 7. Invariant time axis from H0

Use the exact public single-branch invariant form

```text
H0 = sum_(g in 2I) rho(g)^dagger rho(g).
```

The public theorem states that `H0` is totally positive definite and that the
invariant Hermitian forms on the marked single branch are exactly the line
`F H0`.

The invariance law is

```text
rho(g)^dagger H0 rho(g) = H0.
```

Define the future timelike carrier point

```text
T0 = H0^-1.
```

Inverting the invariance law gives

```text
rho(g) T0 rho(g)^dagger = T0.
```

Thus every `R_g` fixes `T0`.

Since `H0` is positive definite, so is `T0`, and

```text
q(T0) > 0
```

under the principal embedding.

Define the exact spatial hyperplane

```text
S_H0 = { X in V_H : B_q(X,T0) = 0 }.
```

At the principal embedding, the restriction of `q` to `S_H0` is negative
definite. The projective `A5` action preserves this hyperplane and its negative
definite form.

This supplies the exact meaning of `icosahedral rotations` for the candidate:
the projective marked `2I` action fixes one future timelike ray and acts
orthogonally on its three-dimensional complement.

## 8. Common-carrier datum

The smallest candidate datum is

```text
D_LOR = (V_H, q, C_plus, rho, H0, A_J, {R_g}, B_J).
```

Both sectors act on the same `F`-vector space:

```text
R_g in SO^+(q) under sigma_1,
B_J in SO^+(q) under sigma_1.
```

Here `SO^+(q)` means the determinant-one real isometries of `q` preserving the
chosen future cone component. It does not mean that the complete physical
model has been lifted to a Lorentz-equivariant field theory.

The generated candidate group is

```text
Gamma_LOR = < R_g for g in 2I, B_J > <= SO^+(q).
```

No density statement is made at this point.

### 8.1 Marking and simultaneous-conjugacy equivalence

The public `rho` matrices and `A_J` must be compared in one explicit `K^2`
basis. An unnamed basis change is forbidden.

Admit only the following named equivalence. For one exact
`C in GL_2(K)` and one totally positive `c in F^x`, transform

```text
rho_C(g) = C rho(g) C^-1,
A_J,C    = C A_J C^-1,
H0_C     = c (C^-1)^dagger H0 C^-1.
```

The same `C` must act on both sectors. Conjugating only the rotations or only
the boost changes the relative placement and is not an equivalence.

The factor `c` changes only the scale of the fixed time ray. It may not depend
on a group element or a later density result.

The exact relative conjugacy invariants needed by an external density theorem
must be computed before that theorem is imported. Candidate examples include
traces of words and commutators in the marked generators, but the complete
required list is source-dependent and is not frozen by this note.

## 9. Frozen construction gates

A future exact proof package must decide these gates in order.

### C0. Authority and collision

```text
PASS iff the public authority is current, the incubation item is not
colliding, and every imported public claim retains its exact status and scope.
```

Any authority mismatch is `STOP`.

### C1. Carrier typing

Prove exactly:

```text
[K:F] = 2,
dim_F(V_H) = 4,
q(X) in F,
delta^2 = -(phi+2),
q = t^2-z^2-x^2-(phi+2)y^2,
signature_sigma1(q) = (1,3).
```

### C2. Cone typing

Prove the equivalence between positive semidefiniteness and the three exact
principal-embedding inequalities. Prove the interior and boundary statements.

### C3. J action

Prove exactly:

```text
B_J(u,v,w) = (phi^-1 u, phi v, j w),
q o B_J = q,
B_J(C_plus) = C_plus,
B_J^5(u,v,w) = (phi^-5 u, phi^5 v, w).
```

### C4. Marked 2I action

Import the literal public marked generators and prove exactly:

```text
|rho(2I)| = 120,
det rho(g) = 1,
center = {+I,-I},
projective image ~= A5,
q o R_g = q,
R_g(C_plus) = C_plus.
```

This gate may rely on the already public theorem only through exact source
readback. It may not silently replace the marking.

### C5. Invariant time ray

Prove exactly:

```text
rho(g)^dagger H0 rho(g) = H0,
H0 is totally positive definite,
T0 = H0^-1,
R_g(T0) = T0,
q|S_H0 is negative definite.
```

### C6. Common marking

Prove that the public `rho`, `H0`, and `A_J` inhabit the same named `K^2`
basis, or publish one exact simultaneous conjugation satisfying section 8.1.

This is the load-bearing seam of the incubation item. A separate conjugation
for each sector is a failure of the gate.

### C7. Density source gate

No density theorem may be consumed until the source package freezes:

```text
exact bibliographic record,
exact version,
exact theorem or theorem chain,
all hypotheses,
the source rotation generators,
the source boost or loxodromic element,
the topology and connected component,
the exact target group,
the exact conjugacy or equality map from D_LOR,
the exact conclusion used by TWIST-J.
```

A title, DOI, abstract, numerical orbit, or generic statement about
noncommuting rotations and boosts is insufficient.

### C8. Continuity transfer gate

Even after density, a Lorentz-invariance conclusion requires a separate typed
statement containing:

```text
field or configuration space,
topology,
continuous Lorentz action,
functional or observable,
continuity class,
invariance under Gamma_LOR,
complete dependency graph.
```

The standard closure argument may then show that a continuous
`Gamma_LOR`-invariant functional is invariant under the closure of
`Gamma_LOR`. It does not supply the functional, its continuity, its physical
meaning, or a decoder lift.

C8 is not part of the first promotion package.

## 10. External density pin, not consumed

The owner supplied the following bibliographic locator:

```text
DOI:    10.5281/zenodo.20029795
TITLE:  Dense cyclotomic subgroups of the Lorentz group
```

Status in this note:

```text
UNCONSUMED EXTERNAL PIN
```

This note does not independently resolve the record, identify a theorem
number, import its hypotheses, or claim that its generators equal the datum
`D_LOR`.

The pin may be used only to start C7. It is not evidence for C1 through C6 and
is not a substitute for a Registry row.

## 11. Result vocabulary for incubation

Only the following incubation records are allowed:

```text
candidate-T positive:
    C1 through C6 have complete exact proofs on the frozen datum.

candidate-T negative:
    one exact theorem proves that the frozen datum fails a named C1 through
    C6 gate. The negative result is scoped to this datum or equivalence class.

candidate-C:
    finite exact checks pass on a declared finite surface, but no completeness
    proof establishes C1 through C6.

STOP:
    authority, source readback, marking, equality, positivity, completeness,
    license, security, or typing is incomplete.
```

A failed candidate marking does not prove that no common Hermitian carrier
exists. It proves only that the frozen datum fails.

No result from this incubation note may enter the public Registry without a
separate reviewed promotion package.

## 12. Scope firewall

This note does not claim or define:

```text
Lorentz density as a public TWIST-J theorem,
uniqueness of the Hermitian carrier,
uniqueness of the invariant time ray beyond the marked rho branch,
a physical spacetime manifold,
a continuum limit,
a field action,
a Lorentz-invariant decoder,
a Lorentz-invariant measure,
a particle state,
a Born cone or probability cone,
a split-unit projector,
a QCarrier or MatterData schema,
an observer,
a clock,
an L5 stream,
an L6 measure,
an SI scale,
a measured prediction,
an end-to-end Lorentz closure.
```

It also does not merge the color and Lorentz physical dictionaries. It uses the
marked `2I` representation only as exact algebraic input for a candidate
rotation subgroup.

## 13. Proposed next work

The first ordered work is proof assembly, not density.

```text
1. Read back the literal rho(S), rho(T), and H0 from the public evidence.
2. Express A_J in the same named K^2 basis.
3. Prove C1 through C5 symbolically.
4. Decide C6 with literal equality or one frozen simultaneous conjugation.
5. Package the proof as PROMO-C-LORENTZ-HERM2-CARRIER-N.
6. Only after C1 through C6 close, start the separate C7 source import.
7. Keep C8 outside the first promotion.
```

The preferred proof uses exact symbolic arithmetic over `Q(zeta_5)` and
`Q(sqrt(5))`. A verifier may audit the proof, but a one-lane local run alone
cannot earn a public computation-grade theorem.

## 14. Promotion boundary

A future package named

```text
PROMO-C-LORENTZ-HERM2-CARRIER-N
```

may propose exactly one public claim:

```text
The marked 2I rotations and the normalized J action act by
future-cone-preserving determinant isometries on one exact four-dimensional
Hermitian carrier.
```

The proposal must state the exact carrier, marking, equivalence, action layer,
proof, evidence, and falsifier. It must not include density or continuity
transfer unless those have separately completed C7 and C8 under their own
public authority.

Until then:

```text
CANON CHANGE                 NONE
REGISTRY CHANGE              NONE
FRONTIER CHANGE              NONE
DEPENDENCY CHANGE            NONE
GATE CHANGE                  NONE
FORMAL PROBE                 NONE
FORMAL RUN                   NONE
INCUBATION STATUS            PREDEFINITION / STOP BEFORE PROOF ASSEMBLY
```
