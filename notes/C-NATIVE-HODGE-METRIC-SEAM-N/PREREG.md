# C-NATIVE-HODGE-METRIC-SEAM-N: prospective contract

Status: PUBLIC NON-CANONICAL incubation. No Canon authority.
Owner: A. M. Thorn / native-hodge-metric-seam-20260928; issue #1251.
Date: 2026-09-28.
Basis: Public Canon v92, main 1c21ef3651aded084a8dd6e5ba9c9260e8549408.

## Inherited inputs

1. RELATIONAL-GROWTH-SATURATION-BOUNDARY [T], at its exact L1 scope:
   the selected torsion-free fired-commutator cover L~=Z^2 has six declared
   unit steps +/-e1,+/-e2,+/-(e1+e2) and word norm
   max(|x|,|y|,|x-y|). The signed integer lift is a conditional cover of the
   finite native fired translations, not a physical metric theorem.

2. C-OMEGA-GENERATIVE-GEOMETRY-N2, PUBLIC NON-CANONICAL:
   tagged hexagonal data map to cube-shell coordinates z=(a,b,c) with
   x=a-c, y=b-c, and increasing the tag r at fixed x,y increments
   z by d=(1,1,1). Its signed completion exhausts Z^3.

3. J-HODGE-HERM2-LOXODROME [T]:
   the fixed-J E+ carrier has signature (3,1). In its inherited marked
   spatial coordinates the exact block is
       q_H=(sqrt5/10)(2 I_3 + 11^T),
   while the fourth marked basis vector has squared norm
       -(2+sqrt5)/8.

Pinned source bytes:

- notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/PROOF.md
  SHA256 a6be9bd44df63655e2a42ec88c9f4cbb853b9ba15f5f5a869ec89e1ca5775c60
- notes/C-OMEGA-GENERATIVE-GEOMETRY-N2/generate.py
  SHA256 8a93ea5bfe5ba8cae0d2e20e1735d2c9b5731ec3d0f6fad6ce58bb2def1c0ada
- probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md
  SHA256 19435a7bd5b33f2b7995262c2dbfc8eb8fa36b6112723fe15dc957aed60ef5c4
- probes/P-RELATIONAL-GROWTH-SATURATION-1/verify.py
  SHA256 b38b6981af4d275fd7b2a810707e20b3cd61b8dbc365171f2ab36cb550235328
- probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py
  SHA256 02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9
- notes/C-HODGE-SPACETIME-WINDOW-N/PROOF.md
  SHA256 aefac8315a9858e9bfdf26a51f95b6790830a31e9c185a4c883ad66129f70442

No source status is strengthened by composition.

## G1: linear seam between the cover and cube completion

Use the difference projection

    pi(a,b,c)=(a-c,b-c)

and diagonal d=(1,1,1). The zero-sum section of (x,y) is

    p(x,y)=((2x-y)/3,(-x+2y)/3,(-x-y)/3).

Prove

    ||p(x,y)||^2=(2/3)(x^2+y^2-xy),

and that the six selected cover unit steps form one hexagonal orbit in the
zero-sum plane. Increasing the N2 tag at fixed (x,y) translates by d.

## G2: complete symmetric metric class

Grant the full abstract automorphism symmetry of the selected six-step
hexagonal cover on the zero-sum plane, and let it fix the diagonal line.
This is deliberately stronger than claiming those automorphisms are all
symmetries of native U.

Classify every positive-definite real quadratic form Q on R^3 invariant under
that action. Prove the zero-sum plane and diagonal line are orthogonal and
that, after normalizing each cover unit step to squared length one, the
COMPLETE family is

    Q_rho=(3/2) I_3 + (rho/9 - 1/2) 11^T,     rho>0,

with rho=Q_rho(d). Positivity is equivalent exactly to rho>0.

Thus symmetry, the chosen unit-step convention and the tagged completion leave
one positive dimensionless ratio unfixed.

## G3: exact Hodge member and explicit nonuniqueness

Pull back the accepted Hodge spatial block to this coordinate seam. Let u be
any one cover unit step after the zero-sum section. Prove exactly

    q_H(u)=2sqrt5/15,
    q_H(d)=3sqrt5/2,
    q_H(d)/q_H(u)=45/4.

After normalizing q_H(u)=1,

    Q_H,norm=(3/2)I_3+(3/4)11^T=Q_(45/4).

Verify at least one distinct positive symmetric control at the same unit-step
normalization, for example

    Q_E=(3/2)I_3=Q_(9/2).

Therefore cover symmetry, positivity, cubic metric growth, immutable prefixes
and the native-generation rules do NOT select the Hodge metric.

## G4: selected Hodge seam

As a candidate-D dictionary only: if the owner independently adopts the
already accepted fixed-J Hodge target and identifies the selected cover
difference plane with its zero-sum spatial plane, then fixing one cover unit
step to squared length one determines the entire scale-free spatial metric
uniquely as Q_(45/4).

This is a selection of one member after an independent target choice, not a
derivation of rho=45/4 from U. Calling rho_H a native prediction is forbidden.

## G5: full normalized flat Lorentz metric

Normalize the full inherited E+ form by the same positive factor that makes a
cover unit step have squared length one. Prove

    g_norm = Q_(45/4) direct-sum [-(15+6sqrt5)/16].

Prove signature (3,1). Overall positive rescaling leaves the null cone
unchanged. This supplies an exact scale-free selected flat-spacetime metric
conditional on G4.

No event-resolution selection, generation-time/event-time identification,
METRO-TICK calibration, SI scale, curved geometry, occurrence or L6 measure.

## G6: selection debt

State explicitly: any future claim that the current native
commutator/generative architecture DERIVES the Hodge metric must provide an
independent metric-sensitive law fixing rho=45/4, or an exactly equivalent
invariant condition. Reusing the Hodge target itself to set rho is circular
for a derivation claim.

The existing microscopic spacelike one-hop support counterexample remains
unchanged. No photon cone, physical Galois equivalence, massless phase,
polarization or curvature conclusion.

## Prospective execution

Commit and publicly read back PREREG.md, metric.py and verify.py before any
scientific execution. Exact standard-library arithmetic only; the inherited
Q(sqrt5) implementation is hash-pinned.

The audit will:
- hash-check every inherited source above;
- verify the tagged cube/difference identities and six unit directions;
- solve the exact linear invariant-form constraints under coordinate
  permutations and confirm their two-dimensional span;
- verify the complete normalized Q_rho formula on rational controls;
- reproduce the exact Hodge ratio 45/4 and normalized spatial matrix;
- reproduce the normalized time coefficient and signature certificate.

Universal statements rest on PROOF.md. Finite/symbolic execution corroborates
them and is not independent-agent confirmation.

Only this directory may be added. No Canon, Registry, Frontier, public gate,
workflow, tool or predecessor changes. Runtime/integrity failure is STOP.
