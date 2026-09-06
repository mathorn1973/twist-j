# Mixed branch completeness and the three-pass attenuation selector

This is the written proof component of P-QDD-V80-CLOSURE-BOUNDARIES-1.
Its scope is mathematical L4 support and channels, with no physical
apparatus, occurrence, sampling, or L6 conclusion. Status and formal
execution order are controlled by the probe's PREREG.md and RESULT.md.

## 1. Frozen source, channel class and equality

Use the target-independent rational J simplex and a marked token. P is its
rank-one orthogonal projector and Q is the complementary rank-three
projector. In the displayed moving-support basis at token 2,

```text
w1=(1,0,0,-1), w2=(0,1,0,-1), w3=(0,0,1,-1),
H=[[2,1,1],[1,2,1],[1,1,2]],
A=QD_JQ|W=[[-1,-1,-3/4],[0,0,1/4],[1,0,1/4]].
```

The five token cases are conjugate: D_J sends u_k to u_(k+1), Q_k to
Q_(k+1), and the basis at one token to a basis with the same H and A at
the next token. Selecting token 2 for this display does not identify the
projectors as physical effects. Comparison with the registered algebraic
targets is only the final comparison.

W is either the real Hilbert space with Gram H or its complexification.
The adjoint is `X^sharp=H^-1 X* H`, with transpose or conjugate transpose
according to the field. Define `Ad_A(X)=AXA^sharp`.

The admitted class is every completely positive trace-preserving linear
channel E on the full operator algebra of W, with exact channel equality:

```text
E(X)=sum_j K_j X K_j^sharp,
sum_j K_j^sharp K_j=I,
E*(Y)=sum_j K_j^sharp Y K_j.
```

The finite Kraus list has arbitrary real or complex entries: no rationality,
purity, invertibility, symmetry, idempotence or unitality of E is required.
Only E*, its trace adjoint, is unital. This covers the full finite-dimensional
CP class: in an orthonormal basis complete positivity makes the Choi matrix
`sum_ab |a><b| tensor E(|a><b|)` positive; a positive matrix is a finite sum
of positive rank-one matrices; reshaping each vector in that sum into a
matrix gives the displayed Kraus formula. Trace preservation gives the
Kraus-square identity. This argument applies over both R and C.

This equality identifies reduced channel maps only. It does not identify
microscopic couplings, environments, classical or quantum memory, phase
transitions, or complete apparatus laws. A phase-indexed family may use this
class at every phase, but the theorem does not impose or select its phase
law or erase its future-output dependence.

## 2. Complete mixed branch fibres for projective effects

Suppose one outcome has Kraus maps L_j on the ambient support, exact effect
`sum_j L_j^sharp L_j=Q`, and ordinary repeatability: after that outcome the
opposite P outcome has zero total weight on every input. Then exactly

```text
L_j=Q L_j Q for every j,
Phi_Q(X)=E_Q(QXQ),
```

where E_Q is an arbitrary channel of section 1 on QV. Conversely every such
E_Q gives a repeatable Q branch with effect Q.

For v in PV, the effect identity says `sum_j ||L_j v||^2=0`; positivity
kills every L_j P. Repeatability says `sum_j ||P L_j v||^2=0`; positivity
kills every P L_j. Restriction to QV therefore has Kraus squares summing to
its identity. Conversely that identity and support prove the effect and
repeatability conditions immediately.

The same proof at each phase requires the next phase to have the same P,Q
on the same support carrier. With changing projectors the corresponding
formula would instead be L_j=Q_next L_j Q_current; that is not the fixed
support class above. No finite phase set or injective phase update is required.
This is pointwise completeness in the explicitly CP typed class, not full
apparatus-family completeness. Correlations with quantum memory can prevent
even a state-independent reduced CP map from existing.

On the rank-one P support every trace-preserving channel is the identity,
because its operator algebra is one-dimensional. Thus the LOW reduced
channel is fixed in this class. This does not fix an outcome or LOW
microscopic apparatus.

## 3. Exact mixed nonselection under terminality and record symmetry

On W the identity channel and the depolarizing channel

```text
E_id(X)=X,
E_dep(X)=tr(X) I/3
```

are both CP, trace-preserving, strictly idempotent, and covariant under
every orthogonal or unitary change of basis. In the ambient space they give
the two branches `QXQ` and `tr(QX)Q/3`, with the same Q effect and ordinary
repeatability. They differ on every pure input: the output purities are
respectively 1 and 1/3.

The nonidentity example has rational Kraus operators in the rational H
basis. Let rho range over the 24 coordinate permutations of the four
ambient coordinates restricted to the sum-zero support. For each rho take

```text
rho/6, rho/12, rho/12.
```

Their squares sum to identity, since `1/36+1/144+1/144=1/24`.
Their channel is the S4 twirl. Its output commutes with all permutations;
the standard sum-zero representation has scalar centralizer, so trace
preservation makes the output `tr(X)I/3`. The audit verifies this equality
on all nine matrix units, so the explicit rational witness requires no
representation-theory assumption. There are 72 rational Kraus maps.

Therefore strict channel idempotence plus complete S4 record-partition
covariance does not select the identity in the mixed class. This does not
contradict the public pure-map theorems, whose class and equality differ.

## 4. The three-pass theorem

Define the attenuation observables independently of E:

```text
B_n=(A^sharp)^n A^n, n=0,1,2,3; B_0=I.
```

For every E in the full class of section 1, the following are equivalent:

```text
(i)   E*(B_n)=B_n for n=1,2,3;
(ii)  E=id;
(iii) E o Ad_A = Ad_A o E.
```

The exact certificate for the nontrivial implication is

```text
H-A^T H A=diag(0,0,5/4),
I-A^sharp A=(15/16) Proj_H(d0),
d0=(-1,-1,3)^T, d1=(11,-5,-1)^T, d2=(-9,-25,-5)^T,
A^sharp d0=d1/4, A^sharp d1=d2/4,
det[d0 d1 d2]=-1024,
<d0,d1>_H=-4, <d0,d2>_H=-20.
```

For n=0,1,2 the difference

```text
B_n-B_(n+1)=(A^sharp)^n (I-A^sharp A) A^n
```

is a nonzero positive scalar times `R_n=Proj_H(dn)`. Its trace, which is
that scalar, is respectively `15/16`, `215/256`, `2815/4096`.
E* fixes B0 by trace preservation and B1 through B3 by (i), hence fixes the
three rank-one projectors.

Here is the elementary fixed-projector argument. If `E*(R)=R`, then for
v in ker R,

```text
sum_j ||R K_j v||^2=<v,E*(R)v>=0.
```

Each K_j preserves ker R. For v in im R, the Kraus-square identity gives

```text
sum_j ||(I-R)K_j v||^2
 =sum_j ||K_j v||^2-sum_j ||R K_j v||^2=0.
```

Each K_j also preserves im R and therefore commutes with R. No property
of a selected Kraus representation beyond positivity and trace preservation
is used.

Apply this to R0,R1,R2. Each K_j has the three eigenvectors dn. Commuting
with R0 and the two nonzero inner products force the eigenvalues on d1
and d2 to equal the one on d0. The nonzero determinant makes these a
basis, so `K_j=c_j I`. The Kraus-square identity gives
`sum_j |c_j|^2=1`; hence E=id. This proves (i) implies (ii) over R and C.
The audit independently checks that the rational linear commutator system
`[X,R_n]=0` has rank eight on the nine matrix entries, with identity in its
kernel. This rank certificate also holds after extending scalars to C.

(ii) implies (iii) immediately. For (iii) implies (i), iterate covariance
and use trace preservation:

```text
tr(B_n E(X))=tr(Ad_A^n(E(X)))
 =tr(E(Ad_A^n(X)))=tr(Ad_A^n(X))=tr(B_n X).
```

The nondegenerate trace pairing gives `E*(B_n)=B_n`, for every n.

Thus the public exact commutator-saturation selector has a valid mixed and
irrational channel extension on this fixed finite support when saturation
means equality of full unnormalized channel outputs. A condition involving
only normalized rays or an outcome label is not being substituted for it.

## 5. The first two passes are insufficient

Let S=span(d0,d1), R_S its H-orthogonal projector, and

```text
E_S(X)=R_S X R_S+(I-R_S)X(I-R_S).
```

This is a rational CP trace-preserving channel. It fixes R0 and R1, hence
B1 and B2, since those are linear combinations of I,R0,R1. But d2 has a
nonzero S component by `<d0,d2>_H=-20`, and a nonzero perpendicular
component by the determinant. E_S therefore removes a nonzero off-block
part of R2 and does not fix B3. It is not the identity channel. This is a
sharp necessity witness for using all three of this nested pass family;
no minimality over every possible alternative observable family is claimed.

## 6. Physical and class boundary

Condition (i) has the independent sequential interpretation

```text
tr(A^n E(rho) (A^sharp)^n)=tr(A^n rho (A^sharp)^n), n=1,2,3,
```

on every supported density rho: the proposed post-state channel preserves
three fixed attenuation profiles. The tests are defined without taking
Lueder, COMM-SAT, projective idempotence or the target effects as inputs.
They can be falsified by independently prepared inputs and attenuation
tests. The native architecture has not realized such tests or established
their preservation. This conditional test principle is not adopted as a
physical law by the proof or verifier.

Complete positivity is essential to this conclusion. On the complexification,
transpose in a real orthonormal basis is positive and trace-preserving,
commutes with Ad_A because A is real, and fixes all Bn, but it changes
complex states. It is not completely positive: applying its extension to
one factor of a maximally entangled projector gives the swap operator up
to scale, negative on an antisymmetric vector. Thus extending the claim to
all positive maps would be false. J and U do not themselves derive the CP
apparatus type.

Neither pointwise mixed class completeness nor the selector classifies all
finite or unbounded apparatus memory, nonlinear or differently typed
architectures, or physical realizations. Equality of reduced channels is
not full apparatus equality. No physical effects, source capture, ready
phase, context, persistence, reset, outcome law or L1-to-L5 gate is supplied.
The three QDD physical owners remain open at their registered scopes.
SAMPLING NOT PROVIDED. No L6 statement follows.
