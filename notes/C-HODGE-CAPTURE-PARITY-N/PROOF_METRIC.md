# The source parity planes, retained labels, and the unchanged Hodge form

**NON-CANONICAL. L1. Analytical candidate-T; C-HODGE-CAPTURE-PARITY-N.**

This proof was prepared before its first computational audit. It classifies
an explicitly selected current-induced quadratic reading of the bright
arrangement transfer derived in PROOF_TRANSFER.md, with every encoded label
retained. All comparisons use the same regular (E,K) source context at input
and output in the calibrated arrangement chart. It separates a real form
comparison from a comparison over an explicit arithmetic field and from an
operational probability statement.

The source is

<https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md>.

Its full contact and receiver relations are equations (24), (43)--(50).
The target is the unchanged marked beta on the Public v104 E_J carrier.

## 1. Source transfer and a form fixed by its current

Use the exact source quantities

~~~
r = Re(F1)*Re(F2) > 0,
B = 4*sqrt(r),
D = 4 + F1*F2 = u+i*v,
A = 4 - conjugate(F1)*F2,
|D|^2 - |A|^2 = B^2.
~~~

The declared bright parity transfers are

~~~
M_plus  = (1/B)*[[conjugate(D),-conjugate(A)],[A,-D]],
M_minus = diag(-1,1)*M_plus,
M_parity^dagger Sigma M_parity = Sigma,
Sigma = diag(1,-1).
~~~

For any preserved nondegenerate Hermitian current H, its congruence preserves
the real bilinear form

~~~
Q_H(X,Y) = -(1/2)*tr(H*X*H*Y).
~~~

Indeed H*T = T^(-dagger)*H, so the product inside the trace transforms by
similarity. The linear functional ell_H(X)=tr(H*X) is invariant as well.

For two amplitudes the exact identity is

~~~
-det(X) = (1/2)*[(tr(Sigma*X))^2-tr(Sigma*X*Sigma*X)].
~~~

Consequently Q_Sigma(X,X)=-det(X) on ell_Sigma=0. This equality is not valid
on the entire Hermitian carrier without the displayed trace-square term.

This Q_H is an explicitly selected natural form derived from the source
current, not a uniqueness theorem for quadratic readings. Conservation of
current alone does not declare Q_H a positive charge, an occurrence probability,
or a measured spacetime interval. The source law supplies the invariant
current; selecting this invariant trace form as physical observable geometry
is an additional reading prescription whose consequences are analyzed here.

## 2. Moving planes selected by the source action

Let R_M(X)=M*X*M^dagger. Away from the parabolic value |tr(M)|^2=4, define

~~~
U_M = image(R_M-I).
~~~

For a nontrivial elliptic or hyperbolic two-port transfer this is a
two-dimensional invariant plane, and the complementary fixed space has
dimension two. The definition uses the source operator, not the Hodge
target. An explicit source-defined projector onto the moving plane is

~~~
P_move = [2I-R_M-R_M^-1]/[4-|tr(M)|^2].
~~~

It is zero on the fixed space and one on the moving roots, whose sum is
|tr(M)|^2-2. Since ell_Sigma is invariant, it vanishes on U_M. Thus the
restriction of Q_Sigma there is exactly -det.

Write a trace-current-zero Hermitian matrix as

~~~
X(a,z) = [[a,z],[conjugate(z),a]],
q(X) = -a^2+|z|^2.
~~~

The following source-fixed axes lie in this three-dimensional Lorentz space:

~~~
F_plus  = (1/B)*[[u,conjugate(A)],[A,u]],
F_minus = (1/B)*[[-v,-i*conjugate(A)],[i*A,-v]].
~~~

Direct multiplication shows R_Mplus(F_plus)=F_plus and
R_Mminus(F_minus)=F_minus. Their norms are

~~~
q(F_plus)  = v^2/B^2-1,
q(F_minus) = u^2/B^2-1.
~~~

The moving plane is the q-orthogonal complement of the corresponding fixed
axis within ell_Sigma=0. Equivalently,

~~~
U_plus:  Re(A*z)=u*a,
U_minus: Im(A*z)=v*a.
~~~

These equations fix a completely explicit source chart. When A is nonzero,
put y=Im(A*z) on U_plus and x=Re(A*z) on U_minus. The exact restrictions are

~~~
q_plus(a,y)  = [y^2+(B^2-v^2)*a^2]/|A|^2,
q_minus(a,x) = [x^2+(B^2-u^2)*a^2]/|A|^2.
~~~

At either target trace assignment A is necessarily nonzero. No fitted
normalizing constant has been used in these equations.

An elliptic moving plane is positive definite: its fixed axis is timelike
in the three-dimensional space of signature (2,1). A hyperbolic moving plane
has signature (1,1): its fixed axis is spacelike. Therefore one hyperbolic
and one elliptic parity supply signature (3,1) on their direct sum.

This real-signature conclusion does not yet identify the unchanged marked
beta_EJ. In particular it is not a justification for replacing beta_EJ by
(sqrt(5)/2)*beta_EJ.

## 3. Every label and every cross-parity coherence remains accounted for

For the swap J on C^26 tensor C^26,

~~~
d_plus = 26*27/2 = 351,
d_minus = 26*25/2 = 325.
~~~

The full bright amplitude carrier and current are

~~~
V = (C^2 tensor L_plus) direct-sum (C^2 tensor L_minus),
H = (Sigma tensor I_351) direct-sum (Sigma tensor I_325).
~~~

Its Hermitian carrier consists of both diagonal parity blocks and a general
off-diagonal block Z together with its adjoint. The latter evolves as

~~~
Z -> (M_plus tensor I)*Z*(M_minus^dagger tensor I).
~~~

It is a real invariant carrier of dimension 8*351*325. Its contribution to
Q_H is

~~~
-Re tr((Sigma tensor I_351)*Z*(Sigma tensor I_325)*Z^dagger),
~~~

with split signature (4*351*325,4*351*325). In particular it is not a positive
form. This entire coherence sector is retained in the full carrier; it is
not physically deleted by choosing a reading that does not inspect it.

The complete spectral analysis is given in the companion window proof.
Writing spec(M_plus)=i*{rho,rho^-1} and spec(M_minus)={sigma,sigma^-1}, the
cross-parity eigenvalues are contained in plus-or-minus i*rho^epsilon*
sigma^delta. At a Hodge match they contain neither target primary pair.
Thus the target boost and rotation come from the internal parity factors;
cross-parity coherences cannot repair a failed pair of trace conditions.

### 3.1 Canonical label-blind embeddings and their weights

The source-current form on the invariant identity-label embedding is

~~~
iota(X_plus,X_minus)
 = (X_plus tensor I_351) direct-sum (X_minus tensor I_325),

Q_H(iota(X),iota(X))
 = 351*q_plus(X_plus) + 325*q_minus(X_minus).
~~~

If instead the declared coordinates are the two partial traces Y_plus and
Y_minus, their canonical identity-label representatives are

~~~
(Y_plus tensor I_351/351) direct-sum (Y_minus tensor I_325/325),
~~~

and the induced form is

~~~
q_plus(Y_plus)/351 + q_minus(Y_minus)/325.
~~~

These are the same form expressed using two different, explicitly marked
coordinate conventions. Replacing either with an unweighted sum changes
the normalization unless an accompanying coordinate map is displayed.

For a literal quotient form, more is required than an invariant kernel.
If r:W1->E is a surjective reading, restriction of Q_H descends by
Q_E(rX,rY)=Q_H(X,Y) precisely when ker(r) is orthogonal to all of W1.
The descended form is nondegenerate precisely when ker(r) is the radical
of Q_H restricted to W1. Alternatively one can explicitly use an invariant
orthogonal projection and its canonical representatives, as in the partial-
trace construction. These alternatives must not be silently conflated.

The moving-plane projection sends the conserved current H^-1 to zero. This
is a necessary consistency check, not a sufficient form-isometry theorem.

### 3.2 Occupied memory does not select one parity

For the source's label-1 carrier and a memory basis label j,

~~~
j=1:   |1,1> lies entirely in L_plus,
j!=1:  |1,j> = (|1,j>_symmetric+|1,j>_antisymmetric)/sqrt(2).
~~~

The second case includes cross-parity coherences. For a general memory
density matrix rho, including one obtained by tracing an entangled spectator,
the parity probabilities are

~~~
p_plus=(1+rho_11)/2,       p_minus=(1-rho_11)/2.
~~~

Thus arbitrary old memory does not prepare a single parity, nor does it
guarantee equal parity populations. In particular the already-written label
1 memory has no minus-parity population. This does not invalidate the full
operator decomposition; it prevents interpreting a selected eigenlabel as
the original occupied-memory preparation.

Partial traces and moving-plane projections here are linear readings of a
retained state. They are not erasures or new receiver operations. A moving-
plane projection need not preserve positivity of a coherency matrix, so its
four coordinates are not automatically a four-outcome probability law.

## 4. Exact criterion for an arithmetic form comparison

Let L be an explicitly declared real base field containing F=Q(sqrt(5))
over which the selected four-dimensional source action, form, and reading
are defined. This is a condition to prove for on-shell data, not a consequence
of the native law having some cyclotomic coefficients.

At an exact target spectrum the source decomposes orthogonally into the
hyperbolic primary plane and the compact primary plane. The hyperbolic
eigenvalues phi^2,phi^-2 lie in F. Their eigenlines are isotropic and their
pairing is nonzero. Two such marked hyperbolic pairs admit an intertwining
isometry over L by rescaling one eigenvector to match the pairing. No extra
square root is required.

For the compact plane put

~~~
K_L = L[zeta],       zeta^2-phi*zeta+1=0,
zeta^star=phi-zeta.
~~~

It is a quadratic extension because its discriminant phi-3 is negative at
the chosen real embedding. Choose a nonzero source vector v0 by an explicit
source-based convention. The pair (v0,R*v0) is a basis, and invariance gives

~~~
Q_source(R*v0,R*v0)=Q_source(v0,v0)=c_source,
2*Q_source(v0,R*v0)=phi*c_source.
~~~

Thus the source compact form is

~~~
c_source*Norm_KL/L(x+y*zeta).
~~~

Here c_source includes every label-multiplicity weight specified above.
The original public Hodge form, in its fixed compact basis (v,L*v), is

~~~
c_target*Norm_KL/L(x+y*zeta),       c_target=2*sqrt(5)/5.
~~~

Every compact action intertwiner is multiplication by an element of K_L.
Consequently a simultaneous action intertwiner and isometry to the ORIGINAL
beta_EJ exists over L precisely when

~~~
c_source/c_target belongs to Norm_KL/L(K_L^*).
~~~

The inverse ratio gives the equivalent criterion because the multiplicative
relative norm group is closed under inversion. This is a complete
criterion for these two primary planes with nondegenerate invariant forms.
It does not replace c_target by the coefficient belonging to beta/sqrt(5)
or to the repaired (sqrt(5)/2)*beta.

Over R every positive number is such a norm. Hence, after the exact target
spectrum and signature are established, existence of some real isometry is
automatic. That existence alone cannot establish the intended arithmetic
normalization, integral lattice, or a source-selected physical identification.

## 5. What can be decided without numerical values if the reading is K/F

Now impose the stronger, explicit hypothesis that the normalized source
bright matrices and retained-label reading are defined over

~~~
F=Q(sqrt(5)),       K=Q(zeta_5)=F(zeta_10),
~~~

with their ordinary CM involution. This hypothesis is not asserted for the
unevaluated spectral functions. Under it an additional exact classification
is possible.

### 5.1 Only one parity assignment is K-compatible

An M_minus matrix over K with determinant one has a real trace in F. If it
were the target elliptic sector, its trace square would be phi+2. But phi+2
is not a square in F: its rational norm is 5, whereas the rational norm of
an F square is a rational square. Therefore the K-rational assignment must be

~~~
M_minus hyperbolic: kappa_minus=3,
M_plus elliptic:    kappa_plus=phi.
~~~

This assignment is arithmetically consistent: the squared M_plus trace is
-(phi+2), whose square root lies in K. If tau^2=phi-3, then

~~~
[((phi+2)/sqrt(5))*tau]^2 = -(phi+2).
~~~

The opposite assignment would require a larger explicitly declared field;
it cannot be passed off as the same K/F carrier.

### 5.2 The natural compact form has a fixed norm class

In the compatible assignment, the fixed axis F_plus lies in the F-vector
space Herm_2(K/F) with trace-current zero. Its source norm is

~~~
q(F_plus)=(phi+2)/4-1 = -phi^-2/4.
~~~

This is a negative square in F. The ambient trace-current-zero form is

~~~
<-1> orthogonal-sum Norm_K/F.
~~~

The fixed line is isometric to <-1>. Cancelling that common line, or using
reflections to move a norm-minus-one vector to the standard diagonal vector,
shows that its orthogonal moving plane is F-isometric to Norm_K/F itself.
This result is independent of the particular phase of A and of the values
of F1,F2 beyond the exact target equations.

For the identity-label reading, its coefficient is therefore 351 modulo
relative norms; for the partial-trace convention it is 1/351 modulo norms.
These statements concern form classes, not a silently rescaled physical form.

### 5.3 Original beta fails at the other real place

The two real embeddings of F send sqrt(5) to opposite signs. The CM norm
Norm_K/F is positive definite at both places. The coefficient
c_target=2*sqrt(5)/5 is positive at the principal place and negative at the
other place. Thus the original Hodge compact form has opposite signs at the
two places, while the natural source compact form does not.

Therefore there is no F-linear intertwining isometry from this natural
source form to the unchanged beta_EJ, even if the isolated target trace
conditions are met.

The conclusion is not restricted to the identity-label embedding. The
complete target compact eigenspace lies in the elliptic internal parity.
More precisely, its real compact isotypic carrier is the internal moving
plane tensored with Herm(L_plus). On simple tensors the trace formula factors
as Q_Sigma(X,Y)*tr(P*Q), so its current-induced form is the positive compact
norm tensored with the positive Hermitian Hilbert-Schmidt form on the retained
labels, at BOTH real places. Over K/F the latter form is a sum of diagonal
squares and twice the CM norms of off-diagonal entries, which proves this
positivity at each embedding. Every nondegenerate F-rational restriction, or
naturally induced orthogonal quotient, remains positive there.

This positivity statement concerns only that internal compact isotypic
carrier. The full cross-parity trace form remains split as computed in
section 3. At an exact target match the cross-parity carrier has no target
compact eigenvalue, so it cannot contribute to a target compact subquotient
or change the sign obstruction. This uses the complete spectrum, not an
assumption that coherences have been discarded.

A different chosen form, a field with different real-place behavior, or an
explicit scalar that changes sign between the real places is a different
contract. The scalar sqrt(5)/2 used by the predecessor's repaired target is
exactly the kind of normalization change that must remain visible.

### 5.4 Two useful local checks for the fixed identity-label convention

Even after changing to beta/sqrt(5), its compact coefficient would be 2/5.
The ratio against either odd label weight 351 or 325 has odd valuation at 2.
The prime 2 is inert in K/F, so such a ratio is not a relative norm. This
does not establish the same claim for every possible alternative label
reading; it concerns the explicitly fixed identity/partial-trace convention.

At the repaired scale (sqrt(5)/2)*beta the target compact coefficient is one.
Neither 351 nor 325 is a relative norm in K/F: both have valuation one at 13.
For completeness, 13 is inert in F because 5 is not a square modulo 13, and
a primitive fifth root over F_13 first occurs in degree four, since 13 has
order four modulo 5. Thus the relative residue extension K/F has degree two
at 13 and is unramified there. Norm valuations are even, proving the claim.
The inverse weights have the same obstruction.

These local checks apply only to the specified K/F arithmetic carrier.
Enlarging the field can change the splitting of a prime and its norm group.

## 6. Why input phases are not already an arithmetic boundary proof

The source contains the cyclotomic phases g=2*pi/5 and beta=4*pi/5. The fixed
native D2 calibration makes the stated contact coefficients rational and
the pulse coefficients lie in F. Therefore it would be wrong to declare
that the full source has only F(i) coefficients.

There is also a distinction between available phase and relative boundary
phase. On the one-carrier sum in source equation (6), exp(-i*beta) is a
common factor of both arrangements and of the full step. It cancels from
coherency congruence. The object contact phase g is local and can affect the
actual resolvents; its effect is already contained in F1 and F2.

The on-shell functions and the normalization sqrt(Re(F1)*Re(F2)) are spectral
objects, not automatically elements of K. A field of native coefficients
does not by itself provide a K-rational normalized channel basis, its
integral lattice, or an involution-compatible reduction. Accordingly:

1. The real signature result in sections 1--3 is unconditional for the
   stated regular parity transfers.
2. The norm criterion in section 4 applies once a comparison field and
   source-fixed reading have actually been supplied.
3. The sharp F-arithmetic obstruction in section 5 is conditional on that
   K/F typing. It must not be claimed as an unproved property of the actual
   unevaluated boundary values.

The companion window theorem already excludes exact fixed Hodge matching
on the source packet's absolutely continuous energy-momentum support, before
any form equation is imposed. These metric results classify the remaining
isolated conditional comparison without changing the original beta.
