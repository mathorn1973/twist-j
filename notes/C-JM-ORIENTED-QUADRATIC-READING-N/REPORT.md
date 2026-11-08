# Oriented quadratic records: positivity, normalization, and the index-41 seam

**Status: NON-CANONICAL, L1.** Candidate `C-JM-ORIENTED-QUADRATIC-READING-N`.
Analytical conclusions: candidate-T. Exact local audits: candidate-C.
Owner: A. M. Thorn, session oriented-quadratic-reading-2026-10-20.
No public repository change, scientific promotion or physical layer lift.

## Main answer

There is an explicit positive quadratic pairing between R and its distinct
conjugate lattice bar R. Its diagonal square can be normalized to a positive
trace-one projector without a square-root field extension. The complete
normalized RECORD must retain the normalization mass q together with the
projector rho, or an explicitly declared replacement resource. The record
(q,rho) reconstructs the original integral outer square and therefore the
source up to a simultaneous sign. It retains exact seam membership and the
nonreduced integral direction. The quadratic mod-41 step has order 820 on
the glued carrier, against 20 on the split carrier.

Conversely every reading invariant under nonzero integer scaling has the
same image on nonzero R and nonzero S. Bare trace-one normalization cannot
decide whether an actual integral input belongs to R. This obstruction is
independent of positivity and of the particular quadratic construction.

The construction is an existence result in the specified arithmetic class.
It does not select a physical metric, preparation, instrument, occurrence
law, resource or measurement. It does not derive Born occurrence.

## 1. Source and authority

The predecessor is the merged public note
`notes/C-JM-RESULTANT-SEAM-41-N/REPORT.md`, PR 1671, main commit
`75a7d64f29e37d740ba4895135d7a7b9bcaf162e`.
Its candidate results, not a newly promoted Canon theorem, supply

    f=x^4-3x^3+4x^2-2x+1,
    g=x^4-4x^3+8x^2-4x+1,
    A=Z[x]/f, B=Z[x]/g, S=A x B, R=Z[x]/(fg), [S:R]=41,
    E=Q(zeta5) x Q(zeta8), c(a,b)=(bar a,bar b),
    J=1+j^2, M=1+m+m^2, alpha=(J,M), bar R=c(R).

The two source lattices R and bar R are not identified as subrings of E.
In particular bar alpha and alpha c(alpha) are not in R. Adjoining bar
alpha as an internal ring element yields the full maximal product order;
that operation is NOT performed here.

The remainder inclusion C:R->S has Smith invariants (1^7,41) and satisfies
D C=C H for the split and glued steps D,H. The seam maps u:A->F41 and
v:B->F41 evaluate x at19; R=ker(u-v). Source equality is literal equality
in these fixed lattices. No new quotient by independently chosen branch
units is adopted.

Public Canon remains v103, content
`01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, SHA256
`d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`,
1052518 bytes. Its TWO-PLACE-PHYSICS [D] and QDD-SELECTED-BORN [D]
are comparison boundaries only. The new carrier is not silently identified
with the existing QDD carrier.

## 2. Selected trace pairing, not an internal conjugation of R

Choose explicitly

    b(r,s)=Tr_(E/Q)(r c(s))
          =Tr_(K5/Q)(r5 bar(s5))+Tr_(K8/Q)(r8 bar(s8)).

The two full field traces have coefficient one. This choice introduces no
fitted number, but it is not claimed to be physically forced: positive
relative weights would define other positive forms. It is a Q-bilinear
symmetric form. For integral r,s it is integral, since the products are
algebraic integers in the ambient fields even when they are outside R.

For a nonzero real vector in E tensor_Q R, its diagonal value is twice the
sum of four complex squared moduli, one representative from each conjugate
pair. Consequently b is positive definite. This is a real positive form on
a rational space of dimension eight; it is not the assertion of an
eight-dimensional physical space or a native physical Hilbert space.

Equivalently the genuinely typed scalar pairing is

    R x bar R -> Z,   (r,bar s) -> Tr_(E/Q)(r bar s).

Its codomain is Z. No statement that r bar s belongs to R is required.

In the split power basis let G_S be its integral Gram. In the R power
basis G_R=C^T G_S C. Exact values are

    det G_S=288000,
    det G_R=484128000=41^2 det G_S.

Thus the full marked integral pairing already carries the lattice-index
information through its discriminant. Passing to its rational quadratic
space forgets that integral inclusion unless the lattice is also retained.

## 3. Explicit operator-valued pairing

The full target is the integral tensor MODULE

    K_R=R tensor_Z bar R.

This is not a tensor product over R, which would need an unavailable
internal conjugation, and it is not K5 tensor_Q K8 or a compositum field.
It is the module of pairwise record coefficients. The bilinear pairing is

    B(r,bar s)=r tensor bar s,

and its diagonal quadratic map is

    Q(r)=r tensor bar r.

Equip this module with the explicit kernel composition and involution

    (r tensor bar s)(u tensor bar v)=b(s,u) r tensor bar v,
    (r tensor bar s)^*=s tensor bar r.

All coefficients are integers. Associativity follows directly by multiplying
the two scalar contractions; the involution reverses the order of products.
This is an integral, generally nonunital, finite-rank kernel algebra. It does
not enlarge the source ring R by adjoining bar alpha.

There is a Q-linear representation

    Phi(r tensor bar s)(t)=r b(s,t),   t in E.

Nondegeneracy of b identifies E with its rational dual, so Phi becomes an
isomorphism K_R tensor Q -> End_Q(E). It is injective on K_R. On integral
arguments t in R the value is in R. The involution represents the b-adjoint.
The missing integral identity operator is not silently supplied: it exists
in the declared rational completion.

With r=sum z_i e_i and s=sum w_i e_i in any fixed integral R basis,

    Q(r) has coefficient matrix X=z z^T,
    Phi(B(r,bar s))=z w^T G_R,
    Phi(Q(r))=X G_R.

The star-fixed coefficient lattice is the lattice of symmetric integer
8-by-8 matrices (rank36). The full bilinear module has rank64. Diagonal
squares span the symmetric lattice, since the off-diagonal symmetric basis
vector is (e_i+e_j)^2-e_i^2-e_j^2 in outer-square notation. There is no
factor-of-two change of integral lattice in this convention. A rank-one
output has the original eight coordinates up to sign, not 36 independent
physical degrees of freedom.

For every t,

    b(t,Phi(Q(r))t)=b(r,t)^2>=0.

Thus the operator is positive semidefinite for b, and nonzero when r!=0.
More generally the positive cone is defined by self-adjointness and this
inequality on E tensor R. The finite residue fields below are never ordered.

## 4. Normalization and exact retained information

Let tau(T)=tr(Phi(T)). Then

    q(r)=tau(Q(r))=b(r,r)>0,
    rho(r)=Phi(Q(r))/q(r),  r!=0.

The exact identities are

    rho^sharp=rho, rho^2=rho, tr(rho)=1, G_R rho>=0.

No sqrt(q) is needed. rho is a G_R-self-adjoint endomorphism, not generally
an ordinary symmetric matrix. The covariance X/q is ordinary symmetric
positive semidefinite but obeys tr(G_R X/q)=1, not generally tr(X/q)=1.
These two types are not interchanged.

The output carrier can be stated explicitly as

    Y = Z_(>0) x D_(G_R)(Q),
    D_G(Q)={rho in Mat8(Q):rho^sharp=rho, G rho>=0, tr(rho)=1},
    N(r)=(q(r),rho(r)).

The actual image consists of the rank-one records arising as above. Zero
gets a distinct ZERO record and no normalization. Equality in Y is literal
componentwise equality. The mass is not asserted to be physical energy.

Crucially

    X=q rho G_R^-1.

So N loses no information relative to the integral outer square. Over any
field of characteristic different from two, z z^T=w w^T with nonzero z,w
implies w=+/-z: choose an index with z_i!=0, use equality of the (i,i)
entry for the sign, and then of the entire i-th row. Over Z the reconstruction
can use the exact integer square root of a diagonal perfect square. This is
not an algebraic normalizing-root extension. Therefore N(r)=N(s) exactly
when s=+/-r.

Both simultaneous sign and rational scaling must be distinguished. The raw
square and N retain the scale squared; rho alone discards it.

## 5. The normalized-ray obstruction

From [S:R]=41, one has 41S contained in R. Let F:S minus zero -> Y be any
map satisfying F(ks)=F(s) for nonzero integers k. Then for every s in S,

    F(s)=F(41s),   41s in R.

Thus F(R minus zero)=F(S minus zero). In particular membership of an actual
integral input in R cannot be a function of F: choose s outside R and compare
it to 41s. This proof does not assume continuity, linearity, quadraticity,
positivity or a particular metric. It applies to homogeneous quadratic
records divided by a homogeneous quadratic norm, including rho.

The statement compares the same arithmetic vectors in the same rational
ambient carrier and metric. Giving the R and S outputs different hidden
lattice labels or primitive representative conventions changes the output
contract and is not a counterexample.

A continuous fixed-effect detector with zero probability on all R cannot
be nonzero only on S minus R: the normalized images already coincide.
Alternatively a positive quadratic form zero on all R vanishes on a basis
and hence is identically zero. Modular membership recovery from a full
integral record below is not such a probability effect.

Concrete scale control in S is

    s_-=(1_A,-1_B) not in R, 41s_- in R,
    q(s_-)=8, q(41s_-)=13448, rho(s_-)=rho(41s_-).

Retaining q is therefore a substantive and necessary resource for this
particular full-record contract, not a cosmetic label.

## 6. Recovering the seam from the same quadratic data

In the split power basis write z=[a0,a1,a2,a3,b0,b1,b2,b3]^T. Set

    U=[ [1,19,19^2,19^3,0,0,0,0],
        [0,0,0,0,1,19,19^2,19^3] ],
    ell=U_row1-U_row2, all modulo41.

The conjugate leg uses transported residue maps bar u=u composed with c
and bar v=v composed with c. It does NOT evaluate bar J,bar M at the original
chosen primes and pretend to get19: the original-prime values17,7 remain
unchanged. The transported conjugate primes are part of the declared
R-to-bar R typing.

For X=z z^T in K_S, the induced two-residue record is

    W=U X U^T=[[u(a)^2,u(a)v(b)],[u(a)v(b),v(b)^2]].

It follows identically that

    ell X ell^T=(u(a)-v(b))^2,
    s in R iff ell X ell^T=0 in F41.

A field has no nonzero square equal to zero. On R, W=t^2 [[1,1],[1,1]].
This preserves relative equality, distinguishes opposite nonzero signs and
retains t only up to simultaneous sign. There are21 values of t^2. A diagonal
homogeneous quadratic map cannot distinguish r from -r and cannot be sold
as a faithful readout of all41 oriented residue labels.

For N(s)=(q,rho) use X=q rho G_S^-1 first, then reduce the integral X.
Blind division by q modulo41 is not part of the map.

Multiplication inside E would be insufficient even before normalization:

    s_+=(1,1) in R, s_-=(1,-1) not in R,
    s_+ c(s_+)=s_- c(s_-)=(1,1), q(s_+)=q(s_-)=8.

The full outer squares differ in their cross blocks, while every function
of just the two component norm squares identifies this pair. The missing
cross terms, not just a different denominator, matter.

## 7. Integral kernel lattice distinguishes the seam globally

Let K_S=S tensor_Z bar S with the same kernel convention. Choose Smith
bases of C so R is generated by e1,...,e7,41e8 inside S. Then K_R inside
K_S is generated by d_i d_j e_i tensor bar e_j, d=(1^7,41). Therefore

    K_S/K_R = (Z/41Z)^14 direct-sum Z/41^2Z,
    [K_S:K_R]=41^16.

For the star-fixed symmetric coefficient lattices H_R,H_S,

    H_S/H_R = (Z/41Z)^7 direct-sum Z/41^2Z,
    [H_S:H_R]=41^9.

The elementary divisors are respectively (1^49,41^14,1681) and
(1^28,41^7,1681). These are lattice statements, not newly counted physical
states, event probabilities or coupling constants. The module remains over
Z; no field of degree64 or16 is being adopted.

## 8. The nilpotent direction survives the outer square

The predecessor gives R/41R=F41[epsilon]/epsilon^2 x F41^6. The polynomial
k=(h/(x-19)) mod41 has coefficient vector

    k=[28,32,33,34,27,6,12,1].

It is nonzero in R/41R but Ck=0 mod41, and k^2=0 under ring multiplication.
Its outer square k tensor bar k is NOT zero: its last diagonal coefficient
is1. Tensoring two independent module positions is not multiplying the two
nilpotents in one ring.

This distinction is lost by first mapping to S/41S: C k k^T C^T=0 mod41.
The full integral tensor must be retained before reduction. In fact Ck is
divisible by41 integrally, so q(k) is divisible by41^2. Attempting to use
q(k)^-1 in F41 would be undefined. The pair (q,rho) avoids this problem
because it reconstructs the integral tensor first.

The trace form itself has ranks8 on S/41S and6 on R/41R. The extra drop
is consistent with the trace-pairing discriminant; a contracted trace or
naively reduced operator matrix need not retain every intrinsic tensor
coordinate. The target is the tensor lattice, with the trace used only for
its rational positive representation and normalization.

## 9. Quadratic dynamics still has the factor41

Use the unchanged step alpha on R and bar alpha on bar R. In paired power
bases the raw update is

    X -> H X H^T.

In split coordinates it is X -> D X D^T. This is a deterministic congruence
on the declared tensor module; no physical contact or native U is supplied.

Modulo41, the distinct roots of f and g are respectively
{11,17,19,38} and {6,7,13,19}; every root has twentieth power -1, and19 has
order40. Hence D^20=-I. On the common double factor of H,

    (19+epsilon)^20=-1+27epsilon, epsilon^2=0,
    H^820=-I.

The symmetric-square representation of GL_n over an odd field has kernel
{+I,-I}: if A fixes every z z^T then Az=+/-z, and the vectors e_i+e_j force
the signs on basis vectors to agree. On the split quadratic space the
square of the19 eigenline already has order20, so the order is exactly20.
On the glued space the unipotent term after20 steps acts nontrivially on
the symmetric square (in particular on the square of1 in the double
factor) and has order41. The scalar part still forces order20. Thus

    ord(X -> D X D^T mod41)=20,
    ord(X -> H X H^T mod41)=820.

The same distinction is present on the family of pure outer squares,
since they span the symmetric lattice. It is not merely an effect on
unrealizable non-rank-one test matrices. Neither number is asserted as a
period of the normalized rational state over characteristic zero.

For the full mass-plus-projector record over Q, with H^sharp=G_R^-1 H^T G_R,

    d=tr(H rho H^sharp)>0,
    q'=q d,
    rho'=H rho H^sharp/d.

This agrees exactly with normalizing Hr. The new mass is an integer on
admitted integral inputs even though d is generally rational. H is not
claimed isometric; normalization yields a nonlinear update of rho. This is
not asserted to be a trace-preserving quantum channel.

## 10. Probability-shaped algebra, not occurrence

For nonzero r,s the selected trace pairing gives

    tr(rho(r)rho(s))=b(r,s)^2/[q(r)q(s)] in Q intersect [0,1].

The bounds are the elementary Cauchy inequality in the positive form b.
For any explicitly supplied family of G-self-adjoint positive effects
E_i summing to I, p_i=tr(rho E_i) is nonnegative and sums to1. Positivity
follows directly from p_i=b(r,E_i r)/q(r). No root is needed to evaluate it.

Those effects, their operational equality, physical availability and the
claim that one actual result has law p_i are NOT derived here. Mathematical
information recoverability from (q,rho) is not a one-shot measurement of
rho, a finite-precision experiment, or a proof that q is physically
accessible. Modular membership is an arithmetic decoder of the complete
record, not a positive real-valued Born effect.

The elementary source of this construction is the chosen trace form and
outer-product kernel. It is related to standard density-operator algebra;
standard effect-based representation theorems have their own probability
and effect-consistency premises. For comparison see P. Busch, Quantum
states and generalized observables: a simple proof of Gleason's theorem,
Phys. Rev. Lett.91,120403 (2003), arXiv:quant-ph/9909073. That theorem is not
used as a premise of any new arithmetic statement here.

## 11. A normalized-only alternative pays for a reference

If a single normalized matrix is compulsory, a different, explicit source
contract is available. Adjoin one rational/integer reference coordinate:

    R_hat=Z direct-sum R, G_hat=diag(1,G_R), r_hat=(1,r).

Normalize its outer square by 1+q(r). The resulting nine-by-nine projector
has trace1 and is positive in G_hat. In coordinates

    rho_hat[0,0]=1/(1+q),
    rho_hat[i,0]=z_i/(1+q),
    z_i=rho_hat[i,0]/rho_hat[0,0].

Thus the normalized matrix is injective in r, including its sign, and
q=1/rho_hat[0,0]-1. This does not contradict the scale obstruction: r->(1,r)
is affine and not homogeneous, and the extra reference is not scaled when
r is scaled. It is quadratic on the augmented carrier, not a homogeneous
quadratic pairing on the original R alone. No minimum-reference or physical
reference-availability theorem is claimed.

## 12. Evidence scope

The local PREREG preceded verify.py execution. The first audit uses exact
SymPy integer/rational matrices, including a direct 36-dimensional Smith
check and exact modular powers. It checked38 nonzero integer test vectors
and their pairwise Cauchy/overlap identities, all1681 two-residue pairs,
the trace Grams, nilpotent distinction and the explicit reference formula.
Universal positivity, reconstruction, the scale obstruction, elementary
divisors and dynamics follow from the written arguments, not sample size.

A second, result-exposed program uses only the Python standard library and
no imports of the first implementation. It reconstructs polynomial arithmetic,
cyclotomic conjugation and the trace Gram directly; checks positivity on
all6560 nonzero ternary vectors; and checks quadratic orders through the
separate scalar-kernel criterion. It had its own local pre-execution record.
Both programs passed on one x86_64 environment with empty stderr. This is
a second implementation audit, NOT a blind second-agent confirmation, NOT
an additional architecture, and NOT an earned public T status.

No previously sealed probe, threshold or predecessor statement was changed.
The result may be handed off as a fresh candidate; publication requires a
separate authorized repository task and promotion requires the public fold.
