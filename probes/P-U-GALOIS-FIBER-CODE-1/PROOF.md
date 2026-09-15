# Native Galois-fiber code and conditional QDD split

L1 mathematical proof for P-U-GALOIS-FIBER-CODE-1. This public probe creates
no Canon status. A. M. Thorn; original text Apache-2.0.

## Native fibers

All native coordinates below are in F5. Write x=(a,b,c,d,q,r), z=sum(x).
The declared generators are

    a(x)=(b,a,d,c,q,r),
    b(x)=(-c,-d,-a,-b,-q,-r),
    c(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r),
    d(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
    e(x)=(2-a,1-b,3-c,4-d,2-q,1-r).

Direct substitution shows each squares to identity. Their trace maps are
z,-z,2-z,2-z,3-z. Therefore T_t(x)=g_(z+2t)(x) has sheet maps
tau_0=(0,4,0,4,4), tau_1=(2,1,1,3,1). On any fixed sheet X_s it is
one bijective affine generator onto X_(tau_t(s)). Actual origin-zero U
uses 011. The chronological words are ace,bbd,cce,dbd,ebd; cancelling
involutions yields F_s=eca,d,e,dbd,dbe. All end on X_1, so each restriction
F_s:X_s->X_1 is a bijection. Each sheet has 5^5 points.

Order nonzero marks as (1,2,4,3). Choose Y_h=(h,0,0,0,1-h,0). Its four
antecedents on nonzero sheets are

    X_(1,h)=(2-h,1,3,4,h,1),
    X_(2,h)=(2-h,1,3,4,h+1,1),
    X_(3,h)=(0,0,-h,0,h+1,2),
    X_(4,h)=(0,0,-h,0,h+2,2).

Their traces are 1,2,3,4. The first step joins s=1,3,4 at
R_h=(2,1,h+3,4,-h,4), while s=2 gives S_h=(4,3,h,4,-h,4). The second
step returns these to X_(1,h), X_(2,h); the third maps both to Y_h. This
proves common partitions discrete, {1,3,4}|{2}, {1,3,4}|{2}, indiscrete.
Different h cannot meet earlier, since their deterministic final outputs
differ. Thus the support counts are 16,8,8,4. After synchronization every
common-clock step is a bijection on the known current sheet. Induction
preserves distinct endpoints for any subsequent actual time. Inverse words
define addresses only; none is executed.

## Source, code and Gram theorem

Let K=Q(j), Phi5(j)=0, with principal embedding and conjugation j->j^4.
Put g=1+2j+2j^4, so g is real, g^2=5, and c=g/10. Mark the rational
source by A(v)=sum_(i=1)^4 v_i j^i, with positive form Tr(A bar(B))/5.
Since Tr(1)=4 and Tr(j^m)=-1 for m not divisible by five, its Gram is
G=I4-ones4/5. This has eigenvalues 1,1,1,1/5, and is positive definite.

In Galois order (1,2,4,3), set

    H=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)).

Its columns are orthogonal of squared norm four. Its invariant normalized
row under the cyclic Galois action is (1,1,1,1)/2, unique up to sign:
invariance forces four equal entries and normalization fixes their magnitude.
The complement has dimension three; choosing a basis there is a convention.
No symmetry of full U or physical Galois-selection law is asserted.

Define the Q-linear code into K-valued coordinates on the sixteen points by

    V(A)=c sum_(k,a) H_(k,a) sigma_a(A) e_(X_(a,h_k)).

The rational four-dimensional source K and output coefficient field K are
distinct uses of K. The four source-basis columns define, separately, a
complex-linear extension; all Hermitian matrix identities below hold on it.
The code is not K-linear in field multiplication and is not a single native
checkpoint. The free linear pushforward N_n sends e_x to e_(U^n x).

For a prefix partition P_n, the coefficient for fiber k and merger block B
is c sum_(a in B) H_(k,a) sigma_a(A). The cross-inner product of encoded
A,A' at that prefix is therefore

    |c|^2 sum_(B in P_n) sum_(a,b in B)
      conjugate(sigma_a(A)) sigma_b(A') sum_k H_(k,a)H_(k,b).

The innermost sum is 4 delta_ab. Each a occurs once and 4|c|^2=1/5, so
the result is Tr(bar(A) A')/5. Hence (N_n V)^*(N_n V)=G for n=0,1,2,3.
Known-sheet injectivity proves the same at all later times. This includes
all cross terms; it is not an inference from individual norms or endpoint
agreement. No normalization or extra operation is inserted during U.

At n=3 the square output matrix is

    W(A)=sum_k y_k(A)e_(Y_(h_k)),
    y_k(A)=c sum_a H_(k,a) sigma_a(A).

Since W^*W=G, W is invertible and W^-1=G^-1 W^*, G^-1=I4+ones4.
This inverse is a comparison map, not an executed native operation.

## LOW/HIGH and conditional post-state theorem

The first row gives y_0(A)=Tr(A)/(2g). Let ell(A)=Tr(A)/4 and
A_perp=A-ell(A). The last three rows sum to zero, whence

    D_0 W(A)=W(ell(A)), (I-D_0)W(A)=W(A_perp),

where D_0 selects Y_1, or p1=1 on the four displayed outputs at time three.
In the shifted basis Tr(A(v))=-sum_i v_i and sum_(i=1)^4 j^i=-1. Thus
ell has matrix P_LOW=ones4/4; its complement has P_HIGH=I-P_LOW.
These commute with G and are G-self-adjoint orthogonal projectors.

The Canon's unshifted chart is iota_B0(v)=v_1+v_2 j+v_3 j^2+v_4 j^3.
Multiplication by j is a trace-form isometry and carries its LOW line
Q*(-j^4) onto Q*1. Hence the unchanged coordinate projectors above agree
with DEF-QDD-PROJECTOR-LOW/HIGH under this explicitly declared chart.
This is an algebraic comparison, not a physical context choice.

The exact effect forms are W^*D_oW=G P_o. With the source G-adjoint their
pullbacks are P_o. Weights sum to v^*Gv, and LOW weight is
|sum_i v_i|^2/20. Zero input has zero total and no normalized state; any
zero-weight branch is left unnormalized and is not divided by zero.

Transport a source operator rho by W rho W^-1, appropriate for the source
metric G. Only conditional on the ideal COARSE map sigma->D_o sigma D_o,
intertwining on both sides gives

    D_o W rho W^-1 D_o = W P_o rho P_o W^-1.

This holds for every operator, including every source density operator, and
preserves all three-dimensional HIGH coherences. Fine discrimination of the
three HIGH coordinates followed by forgetting is a different map, since it
deletes their off-diagonal entries. Neither coarse projection nor a selected
outcome, physical pointer factor, occurrence, record or reset is derived.

## Preparation boundary

For any real orthogonal 4-by-4 T replace cH by T/g. The identical prefix
proof uses sum_k T_(k,a)T_(k,b)=delta_ab, and the endpoint is
T(sigma_1(A),sigma_2(A),sigma_4(A),sigma_3(A))^T/g. Thus native merger and
prefix isometry alone do not uniquely select H/2. T=I is an explicit
different rational template with the same Gram preservation. Arithmetic
invariance selects the trivial row only within the declared row criterion.

In abstract antecedent coordinates (k,a), the chosen address vectors
b_a=(H_(k,a)/2)_k are orthonormal, and therefore are not one common ready
vector independent of a. The Galois embedding matrix is nonsingular (its
columns have positive trace Gram), so the four channels span the full source
after scalar extension. The code requires those specified correlations;
no universal necessity claim about other codes follows.

For A=1 the sixteen coefficients have squared magnitude 1/20. Coherent
addition gives W(1)=(2/g,0,0,0), squared norm 4/5. Removing initial phase
coherences first gives four equal unnormalized endpoint weights 1/5, which
differs. This explains the resource in the chosen representation; it is not
a physical probability prediction or preparation procedure.

Physical preparation/adoption of V, an actual coarse event, occurrence,
persistent material records, reset/repetition, a complete physical apparatus
family and L1-to-L5/L6 gates remain open. The selected free representation
is not a globally normalized quantum channel. Its exact isometric
restriction supplies no physical adoption by itself.
