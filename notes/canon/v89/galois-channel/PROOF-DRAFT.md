# Proof draft: complete Galois-channel optimum and minimal auxiliary

**NON-CANONICAL / DRAFT / NO EARNED PUBLIC STATUS.**
A. M. Thorn; adapted synthesis of original Apache-2.0 issue proofs #1037
and #1038. Source identities and review limits are in SOURCE-REVIEW.md.
This proof is mathematical review material, not a formal run record.

## 1. Unchanged code and declared complex comparison

Use k,a=0,1,2,3 in the public mark order (1,2,4,3), with input
H_in=C^16 having orthonormal basis e_(k,a) and output H_out=C^4
having basis e_k. Set

    H=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)),
    F=H/2,       C e_a=(1/2) sum_k H_ka e_(k,a),
    Pi=CC*,      Q=I16-Pi,       D=FC*,       q_ka=Qe_(k,a).

Since H*H=4I, C*C=F*F=I. Thus Pi and Q are orthogonal projections
of ranks four and twelve, D*D=Pi, DD*=I, and DC=F.

The inherited native fiber code uses the same sixteen antecedents
X_(a,h_k) and endpoints Y_(h_k). Its free amplitude pushforward is
N e_(k,a)=e_k, hence NC=F and NN*=4I. These native identities and the
support counts 16,8,8,4 belong to the already public
P-U-GALOIS-FIBER-CODE-1 proof and are not new claims here.

For clarity, the original source coordinate change is also explicit.
Let j be a primitive fifth root of unity, take the positive real sqrt5,
and extend the four rational source-basis columns of
A(v)=sum_(i=1)^4 v_i j^i complex linearly. Put
alpha_a=sigma_a(A)/sqrt5 in Galois order (1,2,4,3). Its matrix E has

    (E*E)_ij=(1/5)sum_(a=1)^4 j^(a(j-i))
             =4/5 if i=j, -1/5 otherwise.

Thus E*E=I4-ones4/5, with eigenvalues 1,1,1,1/5, so E is invertible.
The public coefficient sqrt5 H_ka sigma_a(A)/10 equals H_ka alpha_a/2.
The comparison below therefore uses the full unchanged complex code,
not a newly chosen preparation or a new primitive J.

The class A comprises all complex CPTP maps Phi:M16(C)->M4(C) with

    Phi(C rho C*)=F rho F*

for every complex four-by-four source operator rho. Density operators span
the operator space, so it is equivalent to require this for all density
operators. CPTP is an external mathematical premise, not a derived
physical TWIST-J law.

For raw input e_(k,a), set

    f_ka(Phi)=<k|Phi(|k,a><k,a|)|k>,
    delta(Phi)=max_(k,a)(1-f_ka(Phi)).

The output coordinate distribution is normalized and nonnegative; its
total variation against the deterministic endpoint k is 1-f_ka. This
metric is not quantum trace distance, a QDD weight error or a measurement.

## 2. Finite channel representation and full-output decomposition

For completeness, the finite Kraus/isometry characterization needed here
follows from complete positivity. With Omega=sum_i e_i tensor e_i, the
Choi matrix J=(id tensor Phi)(|Omega><Omega|) is positive semidefinite.
Its spectral factorization J=sum_mu|w_mu><w_mu| and the unique reshaping
w_mu=sum_i e_i tensor K_mu e_i give

    Phi(|i><j|)=sum_mu K_mu|i><j|K_mu*.

Linearity gives Phi(X)=sum_mu K_mu X K_mu*. Trace preservation is
equivalent to sum_mu K_mu*K_mu=I. Consequently
Tx=sum_mu K_mu x tensor e_mu is an isometry and
Phi(X)=Tr_env(TXT*). Conversely those equations give a CPTP map, because
each amplified Kraus term preserves positivity. This uses only the
finite spectral theorem and tensor-product matrix identities.

For Phi in A, each pure code-basis input has pure output F e_a.
A bipartite vector with a rank-one output marginal is a product vector:
its coefficients along every output vector perpendicular to F e_a have
squared norm zero. Hence

    TC e_a=F e_a tensor eta_a

for a unit vector eta_a. The off-diagonal source matrix units require
<eta_b,eta_a>=1 for every a,b. Therefore all eta_a equal a single eta,
including their phases, and TC alpha=F alpha tensor eta for every alpha.

F is onto the whole four-dimensional output. The code image is thus
H_out tensor eta. Since T is an isometry, T(im Q) is orthogonal to it,
and hence lies in H_out tensor eta-perp. Partial trace annihilates all
cross terms between these two environmental sectors. Restricting T to
im Q supplies a trace-preserving complement channel Psi, and

    Phi(X)=D X D* + Psi(Q X Q).                         (1)

The surjectivity of F is essential: a code filling only part of a larger
output does not imply this same cross-term conclusion.

## 3. A sharp bound over the entire complex channel class

Let E_a denote the coordinate subspace with fixed a, and Q_a the
rank-three part of Q on E_a. These blocks are orthogonal and sum to Q.
For every k,a, ||q_ka||^2=3/4 and

    L_ka=(3/4)Q_a-|q_ka><q_ka| >=0.                    (2)

On im Q_a this slack has eigenvalue zero along q_ka and eigenvalue 3/4
on its two-dimensional orthogonal complement; it is zero outside E_a.
Equivalently it is Hermitian and L_ka^2=(3/4)L_ka.

Let A_k=Psi*(|k><k|), regarded as an operator supported on im Q.
Then A_k>=0 and sum_k A_k=Q. The D part of a raw e_(k,a) has
amplitude H_ka^2/4=1/4 at coordinate k. Equation (1) yields

    sum_(k,a) f_ka
      =1+sum_(k,a)<q_ka,A_k q_ka>
      <=1+(3/4)sum_a Tr[(sum_k A_k)Q_a]
      =1+(3/4)Tr Q=10.                               (3)

Therefore mean(f)<=5/8 and min(f)<=5/8 for every admitted complex
channel and every auxiliary dimension. This is a complete-class proof,
not an enumeration of rational channels.

## 4. Two attaining global channels

A seventeen-Kraus construction is

    K0=D,        K_(k,a)=|k><q_ka|.

Because sum_(k,a)|q_ka><q_ka|=Q, their adjoint products sum to Pi+Q=I.
Moreover K0 C=F and every other K C=0. Thus Phi17 is CPTP and
transfers every coded source operator exactly.

A distinct five-Kraus construction is

    J0=D,        J_(a+1)=sum_k|k><q_ka|.

Orthogonality of the output coordinates gives
sum_(a=0)^3 J_(a+1)*J_(a+1)=Q. It too is CPTP and exact on the full
code. On raw input e_(j,b), its nonzero output vectors are

    J0 e_(j,b) : component k = H_jb H_kb/4,
    J_(b+1)e_(j,b) : component k = delta_kj-H_kb H_jb/4.

For Phi17 the latter components go into separate Kraus sectors; for
Phi5 they share one sector. In either case, coordinate probabilities are

    1/16+9/16=5/8 at k=j,
    1/16+1/16=1/8 at k!=j.

Thus both attain (3) with the same agreement at every raw point, proving

    max_Phi min_(k,a) f_ka = max_Phi mean_(k,a) f_ka =5/8,
    min_Phi delta(Phi)=3/8.

They are different global channels. On raw e_(0,0), entry(0,1) of the
output density is +1/16 for Phi17 and -1/8 for Phi5. Phi5 has density

    (( 5/8,-1/8,-1/8,-1/8),
     (-1/8, 1/8, 1/8, 1/8),
     (-1/8, 1/8, 1/8, 1/8),
     (-1/8, 1/8, 1/8, 1/8)).

Kraus grouping is not a mere change of representation of Phi17.

## 5. Equality fixes the coordinate effects

At mean optimum, every nonnegative slack Tr(A_k L_ka) in (3) vanishes.
For positive A,L, Tr(AL)=||L^(1/2)A^(1/2)||_HS^2=0, so
range A is contained in ker L. Intersecting the kernels for a=0,...,3
inside im Q gives

    range A_k subset S_k=span{q_k0,q_k1,q_k2,q_k3}.

The four q vectors are nonzero and lie in orthogonal E_a blocks.
Consequently a positive Hermitian coefficient matrix lambda_k satisfies

    A_k=sum_(a,b)lambda_(k,ab)|q_ka><q_kb|.            (4)

To impose all blocks of completeness, put P=I4-ones4/4,
r_k=P e_k, and Z_a=diag(H_0a,...,H_3a). Identifying E_a with C^4 gives

    q_ka=H_ka Z_a r_k,             Q_a=Z_a P Z_a.

The outer products |r_k><r_k| are linearly independent even over C.
Their diagonal vectors form M=(8I4+ones4)/16: its diagonal entries
are 9/16 and off-diagonal entries 1/16. Its eigenvalues are
3/4,1/2,1/2,1/2 and determinant 3/32. Vanishing of any complex linear
combination of the outer products forces its diagonal combination to
vanish, and invertibility of M forces every coefficient to be zero.

In the a=a block of sum_k A_k=Q, conjugating by Z_a gives
sum_k lambda_(k,aa)|r_k><r_k|=P=sum_k|r_k><r_k|.
Therefore lambda_(k,aa)=1. In an a!=b block, conjugating by Z_a
and Z_b gives

    sum_k lambda_(k,ab)H_ka H_kb |r_k><r_k|=0.

Independence forces every lambda_(k,ab)=0. Equation (4) reduces to

    A_k=sum_a|q_ka><q_ka|,           rank A_k=4.        (5)

The four nonzero eigenvalues are 3/4. This argument includes complex
off-block coefficients; a diagonal-block calculation alone would not
prove uniqueness. If min(f)=5/8, then mean(f)>=5/8 and (3) forces
equality, so (5) also applies to every worst-coordinate optimizer.
It fixes effects, not global channels, as section 4 demonstrates.

## 6. The exact purified auxiliary minimum

In every pure-environment dilation, section 2 places T(im Q) in
H_out tensor eta-perp. Projecting the output onto coordinate k gives
B_k=(<k| tensor I)TQ:im Q->eta-perp. Its Gram is A_k, so

    rank A_k=rank B_k<=dim(env)-1.

Equation (5) forces dim(env)>=5. The five Kraus operators J_mu give an
isometry with environment C^5, so five is attained. Their Hilbert-Schmidt
Gram diag(4,3,3,3,3), determinant 324, also shows this particular channel
has Kraus rank five.

An initially mixed environment is counted after purification. The result
is not a bound on only the unpurified subsystem, five bits, an intrinsic
native prime, or the number of optical components.

Optimal raw agreement is essential. A four-dimensional-auxiliary control is

    V4[(l,mu),(k,a)]=F_la F_mu,k H_ka.

It first applies the inverse of L=ZB defined below, swaps the two
four-valued registers, then applies F on the output; all three operations
are unitary. Directly, V4 C alpha=F alpha tensor e0. Each raw column
has sixteen entries of magnitude 1/4, so every output coordinate has
probability 4/16=1/4. It transfers the full code but fails the optimum.
Dimension counting 4 dim(env)>=16 shows four is already the smallest
possible full-input pure dilation if optimal agreement is omitted.

## 7. Exact native point compatibility is a separate control

If a CPTP map Lambda sends every raw |k,a><k,a| to |k><k|,
its coordinate effects B_l=Lambda*(|l><l|) are positive contractions
with diagonal entries delta_lk. For a positive matrix, a zero diagonal
entry forces its whole row and column to vanish, because
|B_ij|^2<=B_ii B_jj. Apply this both to B_l and I-B_l. It follows that

    B_l=sum_a|l,a><l,a|.

Hence C*B_l C=I4/4 and every coded operator has output coordinate weight
Tr(rho)/4. For alpha=(1,1,1,1)/2, exact transfer would require e0,
whereas a point-exact channel gives the uniform coordinate distribution.
Their total variation is 3/4, distinct from the optimized raw error 3/8.

The explicit point-exact control L_a e_(k,b)=delta_ab e_k has
sum_a L_a*L_a=I and gives I4/4 on that source. This demonstrates
incompatibility of simultaneous exact raw transitions and exact code
transfer under the CPTP comparison hypothesis; it does not refute NC=F.

## 8. Full reversible certificate and factorization

In input order (sixteen signal, four additional coordinates) and output
order (sixteen residual, four central coordinates), set

    U20=((Q,C),(D,0)).

Using Q^2=Q, QC=0, C*C=I, D*D=Pi, DD*=I, direct block multiplication
gives U20*U20=U20 U20*=I20. In particular,

    U20(x,0)=(Qx,Dx),
    U20(C alpha,0)=(0,F alpha),
    U20(0,z)=(Cz,0).

Relabel central k as(k,mu=0) and residual(k,a) as(k,mu=a+1).
The first sixteen columns then become the five-Kraus dilation
T5 x=sum_mu J_mu x tensor e_mu. Tracing mu gives Phi5; retaining all
twenty outputs gives the reversible matrix. On code inputs the auxiliary
label is fixed and contains no LOW/HIGH outcome record.

Let B apply F on k separately for each a, Z=diag(H_ka), L=ZB, and
E0 e_a=e_(0,a). Since the first column of F has entries 1/2, LE0=C.
Let S swap each e_(0,a) with additional coordinate a and fix the other
twelve signal coordinates. The swap has block form
((I-E0E0*,E0),(E0*,0)); conjugation gives

    (L direct-sum I4)S(L* direct-sum I4)=((Q,C),(C*,0)).
    U20=(I16 direct-sum F)(L direct-sum I4)S(L* direct-sum I4).

Thus chronological factors are Z, B, the four swaps, B, Z, and F on
the last four coordinates. Each F is the product of two layers of
balanced two-coordinate Hadamard matrices: pairs(0,1),(2,3), then
(0,2),(1,3). Multiplying their integer numerators and dividing by two
gives precisely H/2. This certifies the full matrix, not just code inputs.

The matched loader and inverse loader cancel. Therefore on the four
designated initial coordinates, the composite loaded response is simply
F routed to the central outputs. A matched-code experiment by itself
would validate a constructed network, not independently predict native
physics. Every raw, complementary and reverse-input output remains part
of the mathematical certificate; residual outputs cannot be removed and
the survivors renormalized.

## 9. Audit boundary and proposed disposition

The accompanying verifier draft is intended to audit finite rational
identities in this proof after a proper public pin. It has not been run
in this preparation. Equality on all sixteen source matrix units extends
over C by complex linearity. Universal optimization and minimality follow
from sections 2--6, not from a finite channel scan or source stdout.

The candidate statements are two L1 mathematical results:
U-GALOIS-CPTP-POINT-COMPATIBILITY and
U-GALOIS-OPTIMAL-AUXILIARY-DIMENSION. No status has been earned by these
drafts. Original issue proofs and reported executions remain incubation
material; public acceptance and any Canon fold are separate.

The formal basis states are not established physical preparations. U,
N, Phi17, Phi5 and U20 must remain distinct. No physical Galois loading,
native coupling, exclusive event, occurrence law, terminal post-state,
persistent material archive, reset, apparatus completeness or layer lift
is provided. Existing physical QDD obligations therefore remain open.
