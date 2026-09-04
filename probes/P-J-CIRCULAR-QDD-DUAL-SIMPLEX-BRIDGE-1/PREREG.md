# P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1 preregistration

Status: **FROZEN TARGET / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY / PUBLIC
STATUS NONE.**

This preregistration owns one exact algebraic bridge.  It compares the actual
integral circular quotient of the alternating-form carrier with the public
characteristic-zero QDD `J` simplex.  The comparison is neither equality of
the two lattices nor an abstract rational similarity: the target is a signed
integral intertwiner from the QDD lattice onto the metric dual of the circular
lattice.

The target values are exposed before execution.  A match confirms the two
claims below at candidate-T/L1 because the universal conclusions are carried
by the proofs in this file; the program audits their finite exact premises.
A mismatch fires the affected claim and is never tuned away.

```text
probe:           P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1
branch:          probe/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1
path:            probes/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1/
claim lock:      https://github.com/mathorn1973/twist-j/issues/799
owner:           A. M. Thorn / delegated session 2026-09-04
mode:            RESULT-EXPOSED / PROOF-FIRST
action layer:    L1 exact algebra
public basis:    Public Canon v75
base main:       6a312ea988e885ff63f3bfeebf4c6c58f70bbef4
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
canon sha256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
canon bytes:     399513
formal runs:     0 before the atomic pin
public status:   NONE
```

## 1. Collision, authority, and novelty lock

Before the claim lock is opened, the public issue and pull-request index,
repository tree, Registry, object-lock surface, and all remote heads must be
searched for the exact probe and claim names and for the combined circular,
QDD, dual-simplex, and signed-intertwiner target.  The declared v75 content
commit and tag must be ancestors of `base main`; the Canon hash and byte count
must match `STATUS.md`.

The following ingredients are already public and are not new claims here:

* `J-STEP [T]` fixes multiplication by `J` on `Z^4`;
* `CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]` fixes the hyperbolic and circular
  primary lattices in the alternating-form carrier;
* `AFFINE-READING-DEGREE-CENSUS [T]` and
  `AFFINE-QUADRATIC-FORM-UNIQUENESS [T]` fix the characteristic-zero affine
  action and its invariant quadratic line;
* `CARRY-PENTAD [T]` already contains the augmentation root lattice `A4`, a
  five-cycle, and an integral cyclotomic bridge;
* public predecessor `P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1`, merged as
  `6a312ea988e885ff63f3bfeebf4c6c58f70bbef4`, exposed the quotient matrices,
  their forty-element group, and one common positive form at candidate-T/L1.

The L4 theorem `QDD-J-AFFINE-APPARATUS-NONSELECTION [T]` is an adjacent
novelty boundary, not a dependency.  No pointer, memory, apparatus, target
effect, or L4-to-L1 edge enters this probe.  The pure L1 simplex and affine
maps are reconstructed below from `M_J`.

The new content is only their simultaneous integral identification:

```text
QDD Z^4  --T-->  circular metric dual L#,
QDD AGL_1(F_5)  --T-->  one signed complement in the circular 40-group.
```

Neither the abstract `A4` isometry nor either group order alone earns either
claim.

## 2. Frozen claims and decision rule

```text
claim A: J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE
claim B: J-CIRCULAR-QDD-SIGNED-AFFINE-PROJECTOR-INTERTWINER
```

Claim A is confirmed exactly when gates G01--G11 and G15 pass.  Claim B is
confirmed exactly when gates G01, G02, G05--G10, and G12--G15 pass.  Otherwise the
affected claim is `FIRED`.  `OVERALL PASS` requires both claims.  All
equalities are exact; there is no numerical tolerance or search-dependent
threshold.

### Six required preregistration fields

1. **Equation.**  Sections 3--8 freeze every source matrix, quotient,
   intertwining equation, lattice equality, metric identity, projector formula,
   finite-group target, and exposed witness tested by the probe.
2. **Code.**  The sole accepted verifier is the exact path named in section 12;
   its pinned bytes are the only executable scientific specification.
3. **Carrier or data.**  The typed carriers are `O_K`, `E_Z`, `H_Z`, `L`, `L#`,
   `C_Z`, and the separate QDD carrier `V_Q=Q^4`.  There is no external dataset.
4. **Systematics.**  Sections 9 and 11 freeze basis, pullback, sign, orientation,
   seam, bounded-enumeration, integrality, and projectivization controls; all
   arithmetic is exact integer or rational arithmetic.
5. **Failure threshold.**  Tolerance is zero.  Failure of any frozen condition
   fires each owning claim; pin, parse, environment, or execution-integrity
   failure is `STOP` rather than scientific evidence.
6. **Action layer.**  The probe is L1 only.  Born, probability, measurement,
   apparatus, physical qudit, decoder completion, and every L2--L6 lift are
   explicitly outside its output scope.

## 3. Common public source and circular quotient

Let

```text
K   = Q(zeta),               Phi_5(zeta)=0,
O_K = Z[zeta],               basis (1,zeta,zeta^2,zeta^3),
J   = 1+zeta^2.
```

The verifier must reconstruct multiplication by `J` from the cyclotomic
relation, not accept the following comparison matrix as its source:

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0, 0,0],
       [0,1,-1,1]].
```

It must likewise derive the matrix `U_2` of the Galois automorphism
`zeta -> zeta^2`.  On

```text
E_Z = Alt^2(O_K^*)
```

use upper-triangular coordinate order `(01,02,03,12,13,23)` and covariant
pullbacks

```text
P(W)   = M_J^T W M_J,
S_E(W) = U_2^T W U_2.
```

The pullback convention is load-bearing.  The hyperbolic lattice and quotient
are

```text
Omega_1 = (1,0,0,1,0,1),
Omega_2 = (0,1,-1,0,1,0),
H_Z     = Z Omega_1 + Z Omega_2,
L       = E_Z/H_Z.
```

The inclusion matrix of `H_Z` in `E_Z` must have Smith invariants `(1,1)`.
Thus `H_Z` is saturated; together with the displayed integral quotient basis
and section below, this makes `L` the integral quotient rather than only the
rational cokernel.

Freeze the quotient basis

```text
b_L = (bar e_03, bar e_12, bar e_13, bar e_23)
```

and relations

```text
bar e_01 = -bar e_12-bar e_23,
bar e_02 =  bar e_03-bar e_13.
```

The verifier must derive the quotient matrices rather than merely enter them:

```text
P_L = [[ 0, 1, 0, 0],
       [ 0, 1, 0,-1],
       [ 0,-1, 1, 1],
       [-1, 1,-1,-1]],

S_L = [[-1, 0, 0, 0],
       [ 0, 1, 0,-1],
       [ 1,-1, 0, 0],
       [ 0, 1, 1, 0]].
```

As an input guard, solve the rational symmetric invariance equations.  Their
frozen dimensions and primitive positive generator are

```text
dim {G in Sym_4(Q): P_L^T G P_L=G}                 = 2,
dim {G in Sym_4(Q): P_L^T G P_L=S_L^T G S_L=G}     = 1,

G_L = [[2, 0,1, 0],
       [0, 2,0,-1],
       [1, 0,2, 1],
       [0,-1,1, 2]].
```

Its leading principal minors are `(2,4,6,5)`.  This rederives the predecessor
form but does not reclaim its existence or uniqueness as new content and does
not choose a Born normalization.

For the separate predecessor seam retain the circular primary basis

```text
c_1=(-1, 0,1,0,0,0),  c_2=(0,-1,0,1,0,0),
c_3=( 0,-1,0,0,1,0),  c_4=(-1,0,0,0,0,1).
```

Its injection into `L` has index five, and on `L/C_Z` the already exposed
actions are `P_L=-1` and `S_L=2` modulo five.  This seam will be checked again
only to prevent its conflation with the different discriminant quotient in
Section 7.

The stronger frozen lattice identity is

```text
C_Z=(I+P_L)L.
```

It identifies the displayed primary lattice with the image of the public
operator, not just with an arbitrary index-five sublattice.

## 4. The circular root lattice and its dual

In the frozen quotient basis put `L=Z^4` with Gram `G_L`.  Freeze the
unimodular change of basis

```text
B = [[1, 0,0,0],
     [0, 0,0,1],
     [0,-1,0,0],
     [0, 0,1,0]],       det B=-1.
```

The target is

```text
B^T G_L B = Cartan(A4)
            = [[ 2,-1, 0, 0],
               [-1, 2,-1, 0],
               [ 0,-1, 2,-1],
               [ 0, 0,-1, 2]].
```

Thus `(L,G_L)` is integrally the root lattice `A4`, is even, and has
determinant five.  Its metric dual is

```text
L# = {x in Q^4 : G_L x in Z^4} = G_L^(-1) Z^4,
[L#:L]=5,
L#/L ~= Z/5.
```

There is no integral orthogonal basis of `L`.  Indeed, every norm in an even
integral lattice is even.  A diagonal Gram in a `Z`-basis of this rank-four
lattice would therefore have four positive even diagonal entries and
determinant divisible by `2^4=16`, contradicting determinant five.  The
verifier audits evenness, determinant, and the `A4` basis; this displayed
argument carries the universal conclusion.

## 5. Pure L1 QDD simplex

On a separate rational carrier `V_Q=Q^4`, define

```text
1   = (1,1,1,1)^T,
G_Q = I_4-(1/5) 1 1^T,
D   = M_J-I_4,
u_x = D^x e_0,              x in F_5.
```

The first four vertices form a unimodular basis, all five span `Z^4`, and

```text
D^5=I,
sum_x u_x=0,
<u_x,u_y>_(G_Q) = 4/5 if x=y, and -1/5 otherwise.
```

For `c in F_5^*`, `b in F_5`, derive the unique rational map

```text
rho(c,b) u_x = u_(b+cx).
```

The verifier must exhaust all twenty maps, their affine multiplication law,
faithfulness, integrality, and `G_Q`-orthogonality.  In particular,

```text
D = rho(1,1),
R = rho(3,0)
  = [[1,0,0,-1],
     [0,0,1,-1],
     [0,0,0,-1],
     [0,1,0,-1]].
```

The multiplier `3` is frozen because it matches `S_L`; `rho(2,0)` is its
inverse and equals the independently reconstructed Galois matrix `U_2` from
section 3.  It is not silently substituted for `R`.

## 6. Reconstructed signed dual isometry

Do not start from a fitted map.  Solve the sixteen-variable rational system

```text
X D = (-P_L) X,
X R = (-S_L) X.
```

Its solution space must have dimension one.  Clear denominators in a nonzero
generator, divide by the gcd of all entries, and fix the sign by requiring its
first nonzero row-major entry to be positive.  The exposed primitive generator
and isometry are

```text
A = 5T
  = [[ 4,-1,-1,-1],
     [ 1, 1, 1,-4],
     [-3, 2, 2, 2],
     [ 2,-3, 2,-3]],

T = A/5,                    det T=-1/5.
```

The two independent lattice and metric targets are

```text
G_L T = U = [[1, 0,0, 0],
             [0, 1,0,-1],
             [0, 0,1, 0],
             [0,-1,1, 0]],       det U=-1,

T^T G_L T = G_Q.
```

Since the simultaneous intertwiner space is one-dimensional, imposing the
metric equation leaves exactly the two witnesses `+T` and `-T`.  This is
relative uniqueness for the frozen marked actions, not an unmarked canonical
choice.

Because `U` is unimodular,

```text
T Z^4 = G_L^(-1) U Z^4 = G_L^(-1) Z^4 = L#.
```

This proves exact equality of lattices, not merely rational equality or an
index comparison.  It also makes `T` a metric isometry from the QDD lattice
onto the circular **dual** lattice.  It is not an integral automorphism of
`L`, and `L#` is not renamed `L`.

There is a stronger three-lattice target.  In the same public cyclotomic power
basis let

```text
lambda=zeta-1,          O_K=Z^4.
```

The verifier must derive multiplication by `lambda` from `Phi_5` and compare
full lattices in both directions.  The frozen chain is

```text
lambda^2 O_K  subset  lambda O_K  subset  O_K
     | T                  | T             | T
     v                    v               v
    C_Z       subset      L      subset   L#.
```

All three vertical arrows are exact lattice equalities.  Each horizontal step
has index five, and the total quotient `L#/C_Z` has Smith invariants
`(1,1,5,5)`.  In particular, this chain also proves `C_Z=(I+P_L)L`: under the
signed intertwiner, `I+P_L` corresponds to `I-D`, and
`1-zeta^2=-(zeta-1)(zeta+1)` with `zeta+1` a cyclotomic unit.

The minus signs are part of the theorem:

```text
T D = (-P_L) T,
T R = (-S_L) T.
```

The unsigned equations with `P_L,S_L` fail for this isometry.  The bridge is
between the QDD phase motor `D=M_J-I`, multiplication by `zeta^2`, and
`-P_L`; it does not identify the full raw `M_J` with `-P_L`.

## 7. Weight simplex, minimum shell, and two order-five seams

Put `w_x=T u_x`.  The exposed oriented pentad is

```text
w_0=( 4, 1,-3, 2)/5,
w_1=(-1, 1, 2, 2)/5,
w_2=(-1, 1,-3, 2)/5,
w_3=(-1, 1, 2,-3)/5,
w_4=(-1,-4, 2,-3)/5.
```

It satisfies

```text
sum_x w_x=0,
<w_x,w_y>_(G_L) = 4/5 if x=y, and -1/5 otherwise,
w_(x+1) = -P_L w_x,
w_(3x)  = -S_L w_x.
```

The complete nonzero minimum shell of `L#` is

```text
Min(L#)={+w_x,-w_x : x in F_5},    minimum squared norm=4/5.
```

Hence it has ten vectors and five antipodal classes.  The displayed `T`
chooses and labels one oriented pentad; neither the sign choice nor the
labeling is claimed canonical without the frozen bases and generators.

Completeness is finite and exact.  Under `T`, a vector is represented by
`n in Z^4` and has squared norm

```text
n^T G_Q n = sum_i n_i^2-(sum_i n_i)^2/5.
```

The least eigenvalue of `G_Q` is `1/5`.  Therefore norm at most `4/5`
implies `sum_i n_i^2<=4`, so every coordinate lies in `[-2,2]`.  Exhausting
that box proves there is no shorter nonzero vector and gives exactly the ten
listed vectors.  This is a completeness bound, not an unbounded search.

The preimage of the root lattice is

```text
T^(-1)(L)={n in Z^4 : sum_i n_i=0 mod 5}.
```

All `w_x` occupy one generating class of `L#/L`, while their pairwise
differences generate `L`.  Thus the full lattice chain is

```text
C_Z subset L subset L#,       [L:C_Z]=[L#:L]=5.
```

The QDD maps `D` and `R` act trivially on this
discriminant group; consequently

```text
P_L on L#/L = -1,
S_L on L#/L = -1.
```

This is not the primary seam `L/C_Z`, where the actions are respectively
`-1` and `2`.  The two cyclic quotients of order five are not identified
equivariantly.

## 8. Projector and affine-group bridge

For each `k in F_5`, average the four affine maps fixing `k`:

```text
Q_k = (1/4) sum_(c in F_5^*) rho(c,(1-c)k).
```

The verifier must derive, not assume,

```text
Q_k = (5/4) u_k u_k^T G_Q,
Q_k^2=Q_k,
rank Q_k=1,
sum_k Q_k=(5/4)I.
```

Transport them across the bridge:

```text
Pi_k = T Q_k T^(-1)
     = (5/4) w_k w_k^T G_L.
```

Each `Pi_k` is rank one, idempotent and self-adjoint for `G_L`, with image
`Q w_k`.  The unordered family is exactly the family attached to the five
antipodal classes of minimum vectors and obeys

```text
sum_k Pi_k=(5/4)I,
tr(Pi_i Pi_j)=1/16 for i!=j.
```

Thus these five projectors are not mutually orthogonal and are not a PVM.
Their matrices have fractional entries and do not lie in `End_Z(L)`.
Although the rescaled operators `(4/5)Pi_k` sum algebraically to the identity,
this probe does not call them effects or a POVM and supplies no occurrence
law.

The twenty QDD affine matrices satisfy

```text
T rho(c,b) T^(-1) in <-P_L,-S_L>.
```

More explicitly, if `c=3^r mod 5`, then

```text
T rho(c,b) = (-P_L)^b (-S_L)^r T.
```

They transport the five `Q_k`, and their conjugates transport the five
`Pi_k`, by the same affine permutation.

Put

```text
H_Q = <-P_L,-S_L>,
G_C = < P_L, S_L>.
```

The target is

```text
|H_Q|=20,       H_Q ~= AGL_1(F_5),       -I not in H_Q,
|G_C|=40,       G_C=H_Q disjoint-union (-H_Q),
G_C ~= C_2 x H_Q,
projective image of G_C = projective image of H_Q, of order 20.
```

This is a split central sign extension.  `H_Q` is one concrete linear
complement selected by the signed isometry; another projectively identical
choice is not silently substituted.  In particular, the predecessor used the
different complement `<-P_L,S_L>`; the two complements have the same
projective image but are not equal as linear subgroups; their intersection has
order ten.  The kernel of the action of `G_C` on the five projectors is exactly
`{+I,-I}`.  The full group preserves the five projectors and antipodal classes,
while the complement `H_Q` preserves the chosen oriented pentad.  Neither
subgroup is the complete marked-simplex automorphism group `S_5`, and `G_C` is
not the complete lattice automorphism group `C_2 x S_5`.

## 9. Frozen exact gates

```text
G01 FIELD_SOURCE
    Reconstruct Phi_5 arithmetic, M_J, D, and the Galois matrix U_2.

G02 ALT2_QUOTIENT
    Reconstruct both ambient pullbacks, H_Z with Smith invariants (1,1), the
    integral quotient map and section, P_L, S_L, C_Z -> L, the equality
    C_Z=(I+P_L)L, and the predecessor primary seam.

G03 COMMON_FORM_GUARD
    Solve the symmetric invariance systems, recover dimensions 2 and 1 and
    primitive G_L, and verify its four positive leading minors.

G04 A4_ROOT_AND_NONORTHOGONALITY
    Verify B is unimodular, B^T G_L B=Cartan(A4), evenness, determinant five,
    Smith invariants (1,1,1,5), and the parity-determinant proof premise.

G05 QDD_SIMPLEX
    Reconstruct D, all u_x, G_Q, the complete simplex Gram, and rho(3,0).

G06 BRIDGE_RECONSTRUCTION
    Solve the simultaneous sixteen-variable intertwiner equations, obtain
    nullity one, and recover the normalized primitive A=5T exactly.

G07 DUAL_LATTICE
    Verify det T=-1/5 and G_L T=U in GL_4(Z), hence T Z^4=L#; derive
    multiplication by lambda and prove the exact chain
    T(lambda^2 O_K)=C_Z, T(lambda O_K)=L, T(O_K)=L#, both indices five,
    total Smith invariants (1,1,5,5), and C_Z=(I+P_L)L.

G08 METRIC_ISOMETRY
    Verify T^T G_L T=G_Q exactly.

G09 SIGNED_INTERTWINING
    Verify T D=(-P_L)T and T R=(-S_L)T and the two oriented-pentad actions;
    verify that removing either load-bearing sign fails for frozen T.

G10 DISCRIMINANT_SEAMS
    Verify [L#:L]=5, the congruence description of T^(-1)(L), actions
    (P_L,S_L)=(-1,-1), and their difference from the primary seam (-1,2).

G11 MINIMUM_SHELL
    Apply the proved coordinate bound and exhaust [-2,2]^4; obtain minimum
    4/5 and exactly {+w_x,-w_x}, ten vectors in five antipodal classes; verify
    that the pairwise differences generate L.

G12 PROJECTOR_FORMULAS
    Derive stabilizer averages Q_k and transported Pi_k; verify formula,
    rank, idempotence, metric adjoint, images, frame sum, and overlap 1/16.

G13 AFFINE_TRANSPORT
    Exhaust all twenty rho(c,b), the affine law and faithful orthogonal
    action, the signed element formula, and transport of both families.

G14 SPLIT_SIGN_GROUP
    Exhaust H_Q and G_C; verify orders 20 and 40, -I exclusion, disjoint
    sign decomposition, direct-product law, projective order 20 with kernel
    {+I,-I}, and order-ten intersection with the predecessor complement.

G15 NEGATIVE_CONTROLS_AND_FIREWALL
    Verify T is not an integral L-automorphism, L!=L#, bare P_L/S_L do not
    preserve the oriented pentad, there are ten vectors rather than five,
    the bare unsigned intertwining equations fail for frozen T, the primary
    and discriminant seams differ, and the output explicitly labels Born,
    probability, measurement, apparatus, physical qudit, decoder completion,
    and every L2--L6 lift as NONE.  Projector and finite-group negative
    controls belong only to G12 and G14, respectively.
```

The verifier must print one deterministic line for each gate, both claim
decisions, and the overall decision.  A failed frozen mathematical condition
prints `FAIL` and selects `FIRED` for every owning claim.  Exceptions and a
nonzero exit are reserved for integrity `STOP`; a scientific mismatch must
not be converted into `STOP`.

## 10. Exact proof implications

The following implications are fixed before execution.

1. `G_L T in GL_4(Z)` proves equality `T Z^4=L#`; metric equality then proves
   an integral lattice isometry from the QDD lattice to the circular dual.
2. The unimodular `A4` basis and the finite norm census prove the root/weight
   identification and the complete minimum shell.  The even determinant-five
   argument proves that no integral orthogonal basis of `L` exists.
3. The two signed generator identities imply the formula for all twenty
   affine elements.  Exact finite closure then proves that this image is a
   complement and that the forty-element group splits as its central sign
   extension.
4. Conjugating the independently derived stabilizer averages proves every
   projector and covariance identity.  Their nonzero pair overlaps and frame
   constant prevent a PVM reading.

If all owning gates pass, claim A and claim B are candidate-T/L1.  If any
owning gate fails, the respective claim is `FIRED`.  A proof defect, hidden
input, incomplete enumeration, post-pin edit, floating tolerance, ambiguous
carrier, or verifier integrity failure is `STOP`, not evidence for either
claim.

## 11. Scope firewalls

This probe is exact L1 algebra only.

* `L`, `L#`, `C_Z`, and the QDD `Z^4` are four typed objects.  Isomorphism is
  written through `T`; none is replaced by literal equality.
* The discriminant seam `L#/L` and primary seam `L/C_Z` are different.
* The bridge carries the motor `D=M_J-I`, not the raw `J` step `M_J`.
* The minus signs select an oriented lift and may not be erased by saying
  “projectively”.  Projectivization is a separate conclusion.
* `T` is the normalized witness relative to all frozen markings.  It is not a
  basis-free assertion that an unmarked bridge is canonical; metric
  intertwining leaves the two witnesses `+T` and `-T` before the displayed
  sign normalization.
* Five antipodal classes are not five chosen physical rays.  `T` supplies one
  algebraic orientation and labeling, not a physical selector.
* `G_L` supplies a positive invariant form only up to scale.  Neither it nor
  the tight projector frame derives a Born normalization.
* The projectors are nonorthogonal; no lattice basis is an integral
  orthogonal basis.  This is not a theorem that physical measurement is
  impossible.
* No Born rule, probability, state/effect semantics, preparation, PVM/POVM,
  measurement, apparatus, event stream, physical qudit, Clifford class,
  universality, amplitude recombination, physical interference, space, time,
  action quantum, numerical value of `h`, anyon model, or L2--L6 bridge is
  established.

Public Canon, Registry, Frontier, gates, dictionaries, dependencies, and
`STATUS.md` remain unchanged.  The two claims remain publicly unregistered
candidate-T even if every gate passes; later registration requires a separate
fold.

## 12. Accepted code and execution protocol

Accepted exact file:

```text
probes/P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-1/verify.py
```

It uses only the Python standard library and exact integer/Fraction
arithmetic.  It has no file input, network, subprocess, shell, randomness,
clock, dynamic import, `eval`, `exec`, float, complex approximation, external
dataset, or imported scratch transcript.  Every loop is explicitly bounded.

Before the first formal execution, this `PREREG.md` and the accepted
`verify.py` must be committed and pushed together, their Git blobs and SHA-256
hashes recorded, and both files read back byte for byte from the public
remote.  Static source inspection and syntax compilation are permitted before
that pin; importing or executing the verifier is forbidden.

After the pin, run the immutable verifier exactly once locally from repository
root in a clean deterministic environment.  Preserve its exact stdout as
`EXPECTED.txt`, record neutral execution metadata in `RUN.md`, add the decision
in `RESULT.md`, and do not alter either pinned file.  The pull request must
change only this probe directory, pass the public x86_64 and aarch64 replay
with byte-identical stdout, pass the aggregate `check`, and receive a named
manual security review.
