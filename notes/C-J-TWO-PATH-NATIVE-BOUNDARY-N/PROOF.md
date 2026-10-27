# A complete two-path instrument for the cyclotomic J operator

**NON-CANONICAL / L1 / conditional analytical candidate-T.**

Author: A. M. Thorn <thorn@twistj.com>. License: Apache-2.0.

Owner reservation: [issue #1806](https://github.com/mathorn1973/twist-j/issues/1806).
Public context: [Canon v105 at main 892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/STATUS.md).
Every operator and equality used in this note is defined below. The result
is a supplied mathematical instrument, not its native physical admission.

## 1. The five-cycle and the field carrier

Let C act on Q^5 by C|r>=|r+1 mod 5>, with r=0,...,4, and put R=C^2.
Both are integer permutation matrices, R^5=I and R^T R=I. Define

    B_Q={a in Q^5: sum_r a_r=0},
    B_Z=B_Q intersect Z^5,
    zeta=exp(2 pi i/5),   K_field=Q(zeta),
    Theta(a)=sum_(r=0)^4 a_r zeta^r.                         (JI-01)

The only rational relation between 1,zeta,...,zeta^4 is their sum zero.
Thus the kernel of Theta on Q^5 is span{(1,1,1,1,1)}, which intersects
B_Q trivially. Dimension four then makes Theta:B_Q->K_field an isomorphism.
It intertwines the operators exactly:

    Theta(Ca)=zeta Theta(a),
    Theta(Ra)=zeta^2 Theta(a),
    Theta((I+R)a)=(1+zeta^2)Theta(a)=J Theta(a).             (JI-02)

The consecutive differences |r>-|r+1>, r=0,...,3, are a Z-basis of B_Z.
Their images are zeta^r(1-zeta), so

    Theta(B_Z)=(1-zeta) Z[zeta].                            (JI-03)

This is the cyclotomic augmentation ideal, not the entire ring of integers.
Using Tr(zeta^m)=4 for m=0 mod 5 and -1 otherwise gives

    Tr(Theta(a) conjugate(Theta(b)))
      =5 sum_r a_r b_r-(sum_r a_r)(sum_r b_r)
      =5 a dot b,                       a,b in B_Q.          (JI-04)

The quantum carrier below is H=C^5 with its ordinary positive inner
product, or its invariant balanced subspace B=B_Q tensor_Q C. Formula
(JI-02) is a rational representation identity. Complexifying it uses
K_field tensor_Q C and its four embeddings; it does not collapse B to
one chosen scalar embedding in C.

## 2. One full two-port law and both outputs

On C^2_port tensor H define

    K_0=(I+R)/2,             K_1=(I-R)/2,
    V=[[K_0,K_1],[K_1,K_0]].                               (JI-05)

The symbol K_0 is an operator, distinct from the field K_field. By (JI-02)
its restriction to the rational balanced carrier represents multiplication
by J/2. The complementary output is equally part of the law.

With H_2=(1/sqrt(2))[[1,1],[1,-1]],

    V=(H_2 tensor I) diag(I,R) (H_2 tensor I).               (JI-06)

Hence V is unitary. Its displayed final matrix has rational entries even
though this factorization uses H_2. Equivalently, direct multiplication gives

    K_0^*K_0+K_1^*K_1=I,
    K_0^*K_1+K_1^*K_0=0.                                  (JI-07)

Preparing port |0> gives |0> K_0 psi+|1> K_1 psi. Measuring that output
port defines the two-outcome instrument with unnormalized output
K_j rho K_j^*. The probability statement here is the declared Hilbert-space
instrument rule, not a derivation of physical occurrence from native U.

All operators in (JI-05) are polynomials in R and commute. The exact power
of the full law is

    V^n=(1/2)[[I+R^n,I-R^n],[I-R^n,I+R^n]],  V^5=I.        (JI-08)

Reusing the same port therefore does not implement K_0^n. Repeated selected
outputs, fresh records and a reused coherent port are different processes.

## 3. Golden effects and the trivial dark mode

For k=0,...,4 let

    f_k=(1/sqrt(5)) sum_r zeta^(-kr)|r>,
    Pi_k=|f_k><f_k|,        R f_k=zeta^(2k)f_k.

Write phi=(1+sqrt(5))/2, P_0=Pi_0, P_-=Pi_1+Pi_4 and P_+=Pi_2+Pi_3.
These are orthogonal projectors summing to I; B=range(P_-+P_+).
The effect of output zero is

    E=K_0^*K_0=(2I+R+R^*)/4
      =P_0+p_- P_-+p_+ P_+,
    p_-=(3-sqrt(5))/8=phi^(-2)/4,
    p_+=(3+sqrt(5))/8=phi^2/4.                             (JI-09)

Indeed its kth eigenvalue is |1+zeta^(2k)|^2/4; evaluating the two conjugate
pairs gives (JI-09). The other effect is I-E, with eigenvalues

    0,  q_-=(5+sqrt(5))/8,  q_+=(5-sqrt(5))/8.              (JI-10)

On the trivial mode f_0, K_0=I and K_1=0. This mode is dark for outcome
one. It must be excluded by the stated balanced preparation if a strictly
decaying no-click bound is wanted. It cannot be silently discarded later.

The bit j labels the observed output port. The projectors P_-,P_+ label
different spectral sectors of that same input operator. A bit is not a
choice of Galois embedding. In particular the two conjugate modes within
each sector have identical bit probabilities but different branch phases.

## 4. Every finite history, including arbitrary references

Use N initially prepared fresh port bits, applying V once to each bit and
the same system. For a history h=(h_1,...,h_N), let n_j be its number of
bits equal to j. The complete isometry is exactly

    W_N psi=sum_(h in {0,1}^N) |h> tensor L_h psi,
    L_h=K_(h_N)...K_(h_1)=K_1^(n_1) K_0^(n_0).             (JI-11)

This follows by induction from (JI-05). Equation (JI-07), or the product
of the N unitaries, proves sum_h L_h^*L_h=I. Before reading the records,
the exact output density is

    sum_(h,h') |h><h'| tensor L_h rho L_(h')^*.              (JI-12)

Every equality remains exact after tensoring all system operators with
the identity on an arbitrary reference. In particular (JI-12) includes
coherences with the reference and between unmeasured histories.

For an arbitrary normalized system-reference state rho, define
w_j=Tr[(P_j tensor I_ref)rho], j=0,-,+. Reading a specified history gives

    Pr(h)=w_0 1_(n_1=0)
           +w_- p_-^(n_0)q_-^(n_1)
           +w_+ p_+^(n_0)q_+^(n_1).                       (JI-13)

Its unnormalized conditional state is (L_h tensor I)rho(L_h^* tensor I).
The count distribution has the additional factor binomial(N,n_0), because
all histories with those counts have the same probability.

These are mixtures of Bernoulli histories conditional on a fixed spectral
sector, not generally independent bits without that conditioning. For
example the covariance of the first two zero indicators is Var_w(p_j).
The weights update by the factors in (JI-13). When w_-,w_+ are nonzero,
the exact posterior odds are

    w_+^(h)/w_-^(h)
      =(w_+/w_-) (p_+/p_-)^(n_0)(q_+/q_-)^(n_1)
      =(w_+/w_-) phi^(4n_0-2n_1).                          (JI-14)

Here p_+/p_-=phi^4 and q_+/q_-=phi^(-2), by phi^2=phi+1.
Zero prior weights stay zero. A history containing a one eliminates the
trivial dark sector; an all-zero finite history does not.

## 5. No-click bounds and an honest stopping instrument

The all-zero history has L_(0...0)=K_0^N. On B,

    ||K_0^N||^2=p_+^N,
    Pr(0...0)=w_-p_-^N+w_+p_+^N <=p_+^N.                  (JI-15)

The operator norm equality remains valid with any reference identity, so
the probability bound is uniform over arbitrary entangled preparations
supported in B. With trivial weight admitted the exact probability is
w_0+w_-p_-^N+w_+p_+^N, which tends to w_0 rather than zero.

If one stops at the first outcome one, the histories are represented by

    M_n=K_1 K_0^n,  n=0,1,... .

At any finite cutoff N the complete effects obey the telescoping identity

    sum_(n=0)^(N-1) M_n^*M_n+(K_0^N)^*K_0^N=I.            (JI-16)

Thus the residual no-click branch is part of the instrument. Removing it
without recording or accounting for it is not a trace-preserving operation.
On B its norm tends to zero, so the infinite first-click instrument has
total probability one. This does not supply a finite guaranteed stopping
time. On H the never-click effect is P_0.

If each attempt has a separately supplied period tau, then on B

    Pr(T>N tau)=w_-p_-^N+w_+p_+^N,
    E[T]=tau[w_-/(1-p_-)+w_+/(1-p_+)].                      (JI-17)

These are instrument waiting-time formulas, not an intrinsic particle
lifetime. The prepared record resources and any clock, feedback or removal
mechanism require their own implementation contract.

## 6. Discarding outputs and the dephasing limit

For one unselected output the exact channel is

    Ecal(rho)=K_0 rho K_0^*+K_1 rho K_1^*
             =(rho+R rho R^*)/2.                           (JI-18)

For every matrix block Pi_k rho Pi_l its Nth iterate multiplies by

    [(1+zeta^(2(k-l)))/2]^N.                               (JI-19)

The multiplier is one for k=l and has modulus strictly less than one
otherwise. Hence the limit is

    Dcal(rho)=sum_k Pi_k rho Pi_k
              =(1/5)sum_(r=0)^4 R^r rho R^(-r).            (JI-20)

There is no residual period in this unselected limit. This differs from
conjugation by R alone, which is periodic. It also dephases the conjugate
modes within a fixed p sector: their bit probabilities agree, but the
discarded branch phases need not. The exact formulas again include arbitrary
references by tensoring identities. Equivalently Ecal^N is a finite mixture
of five conjugations, with binomial weights modulo five converging to 1/5.

## 7. Resultant amplitude is not fringe visibility

To define ordinary interferometric visibility, suppose an adjustable arm
phase chi is additionally supplied. Its zero-output block is
K_0(chi)=(I+exp(i chi)R)/2. For a normalized state rho,

    P_0(chi)=(1/2)[1+Re(exp(i chi)Tr(rho R))],
    visibility=(P_max-P_min)/(P_max+P_min)=|Tr(rho R)|.      (JI-21)

A pure R eigenstate has visibility one, even though its fixed-chi=0
probability can be p_- or p_+. On the maximally mixed balanced state
rho=I_B/4, Tr(rho R)=-1/4, so visibility is 1/4 and P_0(0)=3/8.
The latter trace follows because Tr_H(R)=0 and R acts as one on f_0.

Thus |1+zeta^2|=1/phi describes an unnormalized resultant amplitude in
the nominated embedding. The corresponding selected amplitude in this
balanced two-port device is 1/(2phi), and its probability is p_-.
Neither value is a universal fringe visibility. Formula (JI-21) assumes
the extra adjustable phase; it does not construct its native controller.

## 8. No deterministic normalized J map on arbitrary superpositions

On B the map K_0 is invertible but K_0^*K_0 is not scalar, because
p_- differs from p_+. There is no deterministic quantum channel whose
output for every normalized pure input psi is the pure state along

    K_0 psi/||K_0 psi||.                                   (JI-22)

To prove this, suppose such a channel has Kraus operators A_r. Purity of
the requested output implies that A_r psi is collinear with K_0 psi for
every r and every psi: a sum of positive rank-one operators cannot have
one-dimensional support otherwise. Thus K_0^(-1)A_r sends every vector
to a scalar multiple of itself. Linearity, applied to pairs of independent
vectors and their sum, makes it c_r I. Hence A_r=c_r K_0. Trace preservation
would require

    I=sum_r A_r^*A_r=(sum_r |c_r|^2)K_0^*K_0,

contradicting (JI-09). The argument includes arbitrary ancillas, measurements
and outcome-dependent unitary feedback whenever their final operation is a
deterministic channel. It is not a prohibition on the reversible arithmetic
map x->Jx in its own separately specified integer carrier.

On one fixed p sector the obstruction disappears: K_0/sqrt(p) is unitary
there, and K_1/sqrt(1-p) is also unitary. Suitable supplied feedback can
make both outcomes implement the same chosen unitary on that sector.
This does not extend to unknown coherent superpositions of P_- and P_+;
their different likelihood factors remain part of the instrument. On P_0
the zero outcome is already deterministic and K_0=I.

## 9. Reduced Hermitian determinant and record entanglement

This section develops the author's determinant supplement to the first
revision. It fixes the two individual Fourier modes, rather than treating
each rank-two golden sector as a single complex coordinate. Let k!=l,
let r_k=zeta^(2k), r_l=zeta^(2l), and take

    psi=alpha f_k+beta f_l,    s=|alpha|^2+|beta|^2>0.

Both K_j preserve this two-dimensional plane. In its ordered orthonormal
basis put a=K_0 psi, b=K_1 psi and H(v)=v v^*. The reduced output is

    Q=H(a)+H(b),     Tr Q=s.

It is the carrier marginal of the coherent joint vector
|0> a+|1> b, obtained by tracing the port. It is also the carrier marginal
after dephasing that port record. The coherent joint state itself is pure;
selecting either nonzero outcome gives a pure conditional carrier state.
Thus these are three different states, not a pure global state acquiring
a nonzero determinant merely because its record is retained.

The two column vectors obey

    det[a,b]=alpha beta (r_k-r_l)/2,
    det Q=|alpha beta|^2 gamma_(k,l),
    gamma_(k,l)=|r_k-r_l|^2/4.                              (JI-23)

The first identity follows by subtracting
(1+r_k)(1-r_l) and (1+r_l)(1-r_k) and dividing by four.
The second is det([a,b][a,b]^*)=|det[a,b]|^2. Explicitly,

    gamma_(k,l)=(5+sqrt5)/8  if k-l=+/-1 mod5,
    gamma_(k,l)=(5-sqrt5)/8  if k-l=+/-2 mod5.              (JI-24)

Indeed gamma=sin^2(2*pi*(k-l)/5); the two values follow from the exact
cosines of 2*pi/5 and 4*pi/5. In particular the author's value
(5+sqrt5)/8 is exact on span{f_1,f_2}, and on its conjugate span{f_4,f_3}.
The other cross-sector choices span{f_1,f_3} and span{f_4,f_2} instead
give (5-sqrt5)/8. Merely naming the two golden sectors does not fix it.

The orientation-free pair is one Galois orbit in Q(sqrt5). With
gamma_+=(5+sqrt5)/8 and gamma_-=(5-sqrt5)/8,

    gamma_++gamma_-=5/4,       gamma_+ gamma_-=5/16,
    16 gamma_+^2-20 gamma_++5=0,
    16 gamma_-^2-20 gamma_-+5=0.                           (JI-24a)

The involution sqrt5->-sqrt5 exchanges the roots. Their symmetric
invariants are rational; the unordered pair itself still consists of
irrational algebraic numbers. Fixing the physical mode pair assigns one
root to its determinant coefficient. No unspecified choice of orientation
is allowed to select the desired coefficient after observing a result.
The pair still determines {phi^2,phi^(-2)} as its two directed ratios.
Global complex conjugation reverses the cycle but fixes both real roots;
choosing one mode from each conjugate pair is not by itself a derived
spatial handedness.

The product has a precise click-branch meaning on the four-dimensional
balanced carrier, with the determinant taken over C (equivalently the
rational determinant before complexification):

    det_B K_1=product_(k=1)^4 (1-zeta^(2k))/2
             =N_(K_field/Q)(1-zeta^2)/16
             =Phi_5(1)/16=5/16=gamma_+ gamma_-.            (JI-24b)

Here multiplication by two permutes the four nonzero residues modulo five
and Phi_5(t)=t^4+t^3+t^2+t+1. This norm formula uses the primitive cycle
element zeta, not J=1+zeta^2. The click effect E_1=K_1^*K_1 has eigenvalues
gamma_+,gamma_-, each twice on B. Consequently

    det_B E_1=25/256,
    det_H K_1=0,
    det_(one mode from each P sector) E_1=5/16.            (JI-24c)

The full H determinant vanishes because the constant mode is dark. On
the indicated two-mode plane the branch determinant generally has a phase
and has modulus sqrt5/4, rather than 5/16. The coefficient gamma_(k,l)
in the reduced-state determinant and the effect eigenvalues are different
objects even though they share this pair of algebraic values.

Once the carrier, instrument and mode/readout identification are fixed,
the polynomial in (JI-24a), with both distinct roots present, is an
orientation-free necessary spectral test. For E_1 on B each root must
also have multiplicity two. Failure falsifies that declared model; success
alone does not establish its branch phases, eigenvectors, native control,
or physical mass interpretation.

The operator form makes the scope of this test explicit:

    16 E_1^2-20 E_1+5I=I+R+R^2+R^3+R^4=5P_0.            (JI-24d)

Indeed, with S=R+R^(-1), its left side is S^2+S-I. It vanishes on B
but not on the constant mode. The polynomial tests effect eigenvalues,
not every measured click probability. For a normalized state on B with
sector weights w_-,w_+, the probability q=w_- gamma_++w_+ gamma_- instead
satisfies 16q^2-20q+5=-5w_-w_+, which is nonzero when both weights are
positive. A convex mixture is not a failed spectral prediction.

In Hermitian coordinates Q=t I+x sigma_x+y sigma_y+z sigma_z,
t=s/2 and det Q=t^2-x^2-y^2-z^2. Equations (JI-23)-(JI-24) imply

    0 <= det Q/(Tr Q/2)^2
       =4|alpha beta|^2 gamma_(k,l)/s^2
       <=gamma_(k,l)<1.                                   (JI-25)

The first inequality is strict exactly when alpha beta!=0. The output
then lies in the interior of the positive Hermitian cone; a one-mode
input stays on its boundary. The upper bound alone does not prove strict
interiority. It additionally excludes the central matrix (s/2)I on this
particular two-mode plane. Equality at the upper bound holds exactly when
|alpha|=|beta|. Trace preservation does not identify that trace with a
physical energy or supply a rest frame.

For the normalized pure joint state on port C^2 tensor this mode plane,
define its pure-state concurrence by C_ent=2|det[a,b]|/s. Thus

    C_ent^2=4 det Q/s^2,
    max C_ent=sqrt(gamma_(k,l))<1.                         (JI-26)

This relation concerns the coherent premeasurement joint state. If the
record is fully dephased, the joint state becomes the separable sum
sum_j |j><j| tensor H(K_j psi)/s. Its carrier marginal Q/s is unchanged,
but its entanglement is not the premeasurement concurrence. Therefore
the reduced determinant alone does not certify entanglement of an
arbitrary state that has the same classical record.

### 9a. The full four-mode carrier has a different bound

For any normalized psi in H, set c=<psi,R psi>. The general reduced
carrier state has the form

    Q=(|psi><psi|+|R psi><R psi|)/2.

It has rank at most two. Its possibly nonzero eigenvalues, including a
zero in the rank-one case, are (1+|c|)/2 and (1-|c|)/2. One way to see
this is to form the two-column matrix [psi,R psi]/sqrt(2); its Gram
matrix is (1/2)[[1,c],[conjugate(c),1]]. Hence the product of these two
eigenvalues equals the determinant of the normalized port marginal:

    det rho_port=(1-|c|^2)/4.                              (JI-27)

When the carrier is B of dimension four, its ordinary 4-by-4 determinant
is always zero. It must not be substituted for this two-eigenvalue
product, nor identified with a fixed two-dimensional Hermitian reading.
The rank-independent notation is e_2(Q)=((Tr Q)^2-Tr(Q^2))/2; here it
equals det rho_port, including zero at rank one. It is not the product
of only the nonzero eigenvalues when the rank drops.

For the pure input of this section the visibility from (JI-21) therefore
obeys the exact relation 4 det rho_port+visibility^2=1. This is general
two-path algebra, not a special selection law of J. For a mixed input rho,
the record determinant remains (1-|Tr(rho R)|^2)/4 but no longer certifies
record-carrier entanglement by itself. For example rho=I_B/4 gives
det rho_port=15/64, while the joint output is the separable mixture
(1/4) sum_(k=1)^4 |chi_k><chi_k| tensor Pi_k, where
|chi_k>=((1+r_k)|0>+(1-r_k)|1>)/2. A purification changes the relevant
bipartition to record versus carrier plus reference.

There is a simple exact balanced input achieving maximal record
entanglement:

    psi=(|0>-|1>)/sqrt(2),
    R psi=(|2>-|3>)/sqrt(2),
    <psi,R psi>=0.                                        (JI-28)

Both vectors lie in B and are orthonormal. The two output vectors
a=(psi+R psi)/2 and b=(psi-R psi)/2 are orthogonal, each with squared
norm 1/2. Therefore rho_port=I_2/2, and the carrier marginal on B has
spectrum (1/2,1/2,0,0). This refutes a carrier-wide claim that this contact
never maximally entangles its record. The fixed two-mode bound (JI-26)
remains correct and is not a bound on every state of B.

Furthermore the pair f_1,f_4 lies entirely inside P_- and can already
entangle the record: for nonzero alpha,beta, (JI-23) gives a positive
determinant with gamma=(5-sqrt5)/8. Thus record entanglement detects
different phases of R, not only occupation of both golden-modulus
sectors. For a fixed two-mode Hermitian reading, the reduced output is
strictly inside the cone when both modes with different shift phases are
occupied. The identification of its determinant with pure-state record
entanglement applies only while the joint state remains pure. Dephasing
the retained record preserves the marginal determinant and removes that
entanglement, as shown above.

This gives a precise conditional reduced-state determinant theorem. A
physical identification with rest mass remains a proposed interpretation,
not a newly registered H claim or a derived mass law. It supplies no
native source, occurrence rule, dynamics, conservation law or SI units.

## 10. The local meaning of agreement and one ramified factor

Put j=zeta, O=Z[j], lambda=1-j, and work in the localization O_(lambda).
Its denominators outside the prime ideal (lambda), including 2, are units.
The residue field is O/(lambda)=F_5: setting j=1 in Phi_5(j)=0 gives 5=0.
Under the field identification in section 1, the two branch multipliers are

    a=J/2=1-lambda+lambda^2/2,
    b=(1-j^2)/2=lambda(1-lambda/2)=lambda(1+j)/2,
    a+b=1,     a=1 mod lambda.                            (JI-29)

Thus a and (1+j)/2 are local units. Normalize the prime-ideal valuation
by v_lambda(lambda)=1. Then v_lambda(a)=0 and v_lambda(b)=1: the second
branch contributes one ramified factor times a unit, not literally just
lambda. The first branch is the identity on the residue field, not on
the full local carrier. In fact a-1=-b has valuation exactly one.

The rational prime and the residue field must also be distinguished:

    5=lambda^4 j^2(1+j)^2,       (5)=(lambda)^4,
    O/(5) = F_5[t]/(t^4),       t=lambda mod 5.            (JI-30)

The first equality follows by expanding with 1+j+j^2+j^3+j^4=0.
Its remaining factor is a unit: j is a unit and N(1+j)=Phi_5(-1)=1.
For the quotient identity substitute j=1-t into Phi_5; the polynomial
is t^4-5t^3+10t^2-10t+5, which reduces to t^4 modulo five.
Here a=1-t+3t^2 and b=t-3t^2. Consequently a is not the identity
modulo five, while b is a nonzero nilpotent of order four. This is a
quotient statement; it does not make the exact multiplier b nilpotent.

For a fixed nonzero algebraic input x in K_field and a finite history,

    L_h x=a^(n_0)b^(n_1)x
         =lambda^(n_1) a^(n_0)((1+j)/2)^(n_1)x,
    v_lambda(L_h x)=v_lambda(x)+n_1.                      (JI-31)

This is the unnormalized arithmetic branch. The initial valuation is
part of the formula; in particular Theta(B_Z)=lambda O by (JI-03).
It is not a valuation assigned to every normalized complex quantum
state. On the complex balanced carrier both K_0 and K_1 are invertible,
because all their effect eigenvalues in (JI-09)-(JI-10) are positive.
Every finite history therefore sends a nonzero complex input to a
nonzero vector. For algebraic inputs admitting reduction, vanishing
modulo five is not an exact zero of the complex branch.

## 11. Agreement, signed phase pairing and two quadratures

For a normalized state rho put c=Tr(rho R)=x+i y. For a pure input,
c=<psi,R psi>. Its real part is the real inner-product overlap; its
imaginary part is a signed phase pairing. With the additionally supplied
arm phase of section 7, the complete probability formula is

    2P_0(chi)-1=x cos(chi)-y sin(chi),
    x=2P_0(0)-1,
    y=1-2P_0(pi/2).                                      (JI-32)

Thus a quarter-turn is a clean orthogonal quadrature. It is not a
scalar already in K_field: Gal(Q(zeta_5)/Q) is cyclic of order four,
so it has exactly one subgroup of index two. Its unique quadratic
subfield is the real fixed field of conjugation, Q(sqrt5). If i belonged
to K_field, Q(i) would be a different quadratic subfield, a contradiction.
This excludes scalar multiplication by i inside that number field;
it does not exclude a real matrix implementing a quarter-turn on a
separately specified plane, or the i already used in the ambient C-space.

A quarter-turn is not necessary to reconstruct y. Any supplied chi with
sin(chi)!=0, including chi=2pi/5, gives

    y=[(2P_0(0)-1)cos(chi)-(2P_0(chi)-1)]/sin(chi).        (JI-33)

For the latter phase exp(i chi)=j in the nominated embedding. Membership
of that scalar in the field does not implement its controlled arm phase
on the full carrier. Both readings presuppose the indicated preparations
and controls; no native phase controller is derived by these identities.

The geometric terminology also has a precise limit. On the realification
of the Hilbert space define g(v,w)=Re<v,w> and omega(v,w)=Im<v,w>, with
the first argument conjugate-linear. Then omega(v,w)=g(i v,w). This is
the signed symplectic pairing, not in general the whole Euclidean area.
Indeed the squared real wedge area and the complex Gram determinant obey

    A_real^2=||v||^2||w||^2-g(v,w)^2,
    det Gram_C(v,w)=A_real^2-omega(v,w)^2.                (JI-34)

These follow by expanding |<v,w>|^2=g(v,w)^2+omega(v,w)^2. For example
v=e_1,w=e_2 have unit real area and zero omega, whereas v=e_1,w=i e_1
have unit real area, omega=1 and zero complex Gram determinant.

Finally discarding the port does not consume a universal visibility
budget. For the channel Ecal from (JI-18), cyclicity of the trace gives

    Tr(Ecal(rho) R)
      = [Tr(rho R)+Tr(R rho R^* R)]/2
      = Tr(rho R).                                       (JI-35)

Consequently x, y and the fringe visibility |c| measured with R are unchanged
under every iterate of Ecal. This is compatible with (JI-19)-(JI-20):
the channel removes off-diagonal R-mode coherences, whereas Tr(rho R)
depends only on diagonal mode weights. The pure-state relation between
record entanglement and visibility in section 9 is a relation for that
joint preparation, not a universal loss law for repeated contacts.

## 12. A Gauss-balanced source and its phase convention

Put j=zeta and define the quadratic Gauss sum and character by

    G=j-j^2-j^3+j^4,      G^2=5,
    chi_5(1)=chi_5(4)=1,  chi_5(2)=chi_5(3)=-1,
    sigma_a(j)=j^a,       sigma_a(G)=chi_5(a)G.            (JI-36)

Indeed x=j+j^(-1) satisfies x^2+x=1 and G=2x+1, proving G^2=5.
In the nominated embedding G is positive, hence G=sqrt5. Multiplication
of the four nonzero exponents by a proves the character formula.
G belongs to the ring of algebraic integers O=Z[j], but not to Z.
Using it as an amplitude is not the same as an ordinary integer point
coefficient or a proof of its native preparation.

Use the checkpoint addresses of NATIVE.md section 2d, with entries in F5:

    u_tilde,k=sum_(t in F5)|k,0,0,0,t,1-k-t>,
    v_k=|0,1,0,0,k,-k>,
    S_raw f=sum_k f(k)u_tilde,k,   P_raw f=sum_k f(k)v_k.

Here f(k) denotes the coordinates of a source vector f in C^5. The five
orbit sums have disjoint supports of size five; the five additional point
states have mutually disjoint supports, also disjoint from all orbit sums.
Consequently the exact Gram identities and the balanced source map are

    S_raw^*S_raw=5I,   P_raw^*P_raw=I,   S_raw^*P_raw=0,
    W_G=S_raw+G P_raw,          W_G^*W_G=10I.              (JI-37)

Define the counting isometry E by E(|0> tensor f)=S_raw f/sqrt5 and
E(|1> tensor f)=P_raw f, using the positive orbit norm sqrt5. With
E_B=E(H_2 tensor I), as in the fixed native code, one obtains

    ||W_G f||^2=10||f||^2,
    W_G f/sqrt10=E_B(|0> tensor f).                       (JI-38)

Thus for unit f this supplies exactly the desired ready-code vector.
It is an equality of preparations, not a preparation procedure.

For example f=e_0-e_1 has norm squared two and zero coordinate sum.
Its logical data lie in B and are nonconstant. For the native checkpoint
translation F from NATIVE.md section 2d the normalized source obeys

    Psi=(u_tilde,0-u_tilde,1+G(v_0-v_1))/sqrt20,
    F Psi=(u_tilde,0-u_tilde,1+G(v_2-v_3))/sqrt20.         (JI-38a)

This is an explicit active candidate source, not a derived preparation.

Equal raw coefficients instead give (S_raw+P_raw)f/sqrt6. Under E its
path factor is (sqrt5|0>+|1>)/sqrt6. After the controlled shift
D=diag(I,R) and balanced recombination, its two branches are

    A_0=(sqrt5 I+R)/sqrt12,
    A_1=(sqrt5 I-R)/sqrt12,
    A_0^*A_0+A_1^*A_1=I.                                 (JI-39)

The completeness identity follows by cancelling the two cross terms.
This is a complete instrument, but not the branches (I+/-R)/2.

For source coordinates in K_field write f^(a)(k)=sigma_a(f(k)). The raw
addresses are fixed integer basis vectors, so coefficient conjugation gives

    sigma_a(W_G f)=S_raw f^(a)+chi_5(a)G P_raw f^(a).       (JI-40)

In a fixed positive counting normalization the two path coefficients
are therefore 1 and chi_5(a), divided by sqrt2; the input f^(a) must
also be normalized if it is not unit. For rational f, sigma_2 changes
the relative point-arm sign, not the sign of the whole vector: its orbit
part is unchanged and nonzero. For general f in K_field^5 the source itself
is also conjugated. Calling the entire prepared family Galois-odd is
therefore not the statement in (JI-40).

In the fixed position basis R is an integer permutation and is unchanged
by entrywise coefficient conjugation. With that same law and recombiner,
the branches are (I+/-chi_5(a)R)/2, so chi_5(a)=-1 exchanges the ports.
Transporting the field representation is a different convention:
sigma_a M_(j^2) sigma_a^(-1)=M_(j^(2a)), represented by R^a. The transported
family is then (I+/-chi_5(a)R^a)/2; its reference shift must be stated.

If the encoder's sqrt5 is instead written algebraically as G and also
conjugated, its orbit column changes sign for chi_5(a)=-1. For these a,
extending the automorphism to fix sqrt2 gives sigma_a(E_B)=-E_B X, where X exchanges
the two logical ports. Conjugating both the source and encoder/readout
preserves its logical ready label. No unavoidable physical sector or port
selection follows: the conclusion depends on which source, encoder and
readout are held fixed.

Finally modulus balance alone does not determine relative phase. For
every m in Z, G j^m is also an algebraic integer with modulus sqrt5 and

    W_(G j^m)^*W_(G j^m)=10I,
    output branches=(I+/-j^m R)/2.                       (JI-41)

Thus the balance condition permits different phase-sensitive instruments.
Even the scalar -(sigma_a(G)/sqrt5)^2=-1 forgets the character sign.
The Gauss choice gives an exact constructive source formula, while its
orbit coherence, coefficients, relative phase and preparation remain
supplied resources. The native fixed-code transport in NATIVE.md does
not derive that source or its physical readout.

## 13. A complete two-sheet merger and what its difference port adds

At a fixed clock phase suppose the two disjoint sheets X_1,X_4 map
bijectively onto the same set Y. Let H_s=ell^2(X_s), H_Y=ell^2(Y), and
write F_s:H_s->H_Y for the unitary counting extensions of those bijections.
The deterministic counting pushforward of the merged map is

    N=[F_1,F_4]:H_1 direct-sum H_4 -> H_Y,
    NN^*=2I,      ||N||=sqrt2,
    ker N={(F_1^*y,-F_4^*y): y in H_Y}.                   (JI-42)

These identities follow from F_s F_s^*=F_s^*F_s=I. In particular the
normalized antisymmetric parent pair is annihilated, whereas the symmetric
pair has its squared norm doubled. Thus N is neither an isometry nor a
quantum Kraus branch on this entire counting space. Dividing it by sqrt2
makes a contraction; it does not restore the missing antisymmetric space.

A complete norm-preserving extension retains both outputs:

    K_+=[F_1,F_4]/sqrt2,      K_-=[F_1,-F_4]/sqrt2,
    W=[[F_1,F_4],[F_1,-F_4]]/sqrt2 : H_1+H_4 -> H_Y+H_Y,
    W^*W=WW^*=I,             K_+^*K_++K_-^*K_-=I.         (JI-43)

Direct multiplication proves the identities. Equivalently W is a
Hadamard on the output label after diag(F_1,F_4). Its inverse recovers
the two input components from outputs y_+,y_- as
F_1^*(y_++y_-)/sqrt2 and F_4^*(y_+-y_-)/sqrt2.
The output dimension equals the input dimension; for the synchronized
sheets both are 6250. An unused native coordinate might be proposed as
the label, but assigning that role would still require a new proved law.
W has full rank while N has half that rank. It is a supplied completion
of N/sqrt2, not the unchanged native counting pushforward N.

There is no operation on the merged current state alone that recovers
the lost difference on all inputs. On vectors, K_- does not factor
through N because it is nonzero on ker N. On literal checkpoints, two
parents with the same full checkpoint and counter after merger have the
same deterministic future. Distinguishing them requires information that
was retained outside that merged state before the collision.

The full output W rho W^* is coherent and trace preserving. Selecting
one output gives the unnormalized operation K_+ rho K_+^* or
K_- rho K_-^*. If the output label is discarded, a block input rho gives

    Phi(rho)=K_+rho K_+^*+K_-rho K_-^*
            =F_1 rho_11 F_1^*+F_4 rho_44 F_4^*.           (JI-44)

The cross-sheet coherences cancel in this reduced channel. The which-sheet
Kraus pair [F_1,0],[0,F_4] gives exactly the same channel; K_+,K_- are
its Hadamard-rotated pair. Thus the discarded merger channel does not
specify a coherent sum/difference measurement or choose its readout basis.

To obtain the two-path J branches one must also specify the input matching.
Let I_14:H_1->H_4 be a supplied unitary identification and put

    E_I f=(f,I_14 f)/sqrt2,      R_I=F_1^(-1)F_4 I_14,
    K_+ E_I=F_1(I+R_I)/2,       K_- E_I=F_1(I-R_I)/2,
    N E_I=F_1(I+R_I)/sqrt2.                            (JI-45)

These follow by substitution, and E_I is an isometry. Only when the
independently specified matching realizes the required R_I=C^2 on the
declared source carrier do they reproduce K_0,K_1 of section 2, up to
the common output unitary F_1. The merger alone does not select that
matching: changing I_14 can change R_I to any unitary on H_1.

The arithmetic statement M_J=2K_0 likewise needs its representation.
On the rational balanced carrier, (JI-02) says exactly

    Theta ((I+C^2)|_(B_Q))=multiplication_by_J Theta,
    Theta (2K_0|_(B_Q))=multiplication_by_J Theta.          (JI-46)

An integer matrix M_J in a field basis represents the right-hand operator;
it is not literally the rectangular merger N or a five-by-five matrix.
A nonorthonormal integer basis must carry its Gram matrix G_metric:
the physical adjoint is M_J^sharp=G_metric^(-1)M_J^*G_metric, and the
zero-output effect is M_J^sharp M_J/4 in those coordinates. The trace
form (JI-04) supplies the relevant metric. A Euclidean transpose in an
arbitrary integer basis does not by itself compute this effect.

Retaining the minus port retains amplitude information in the completed
law. Its sign label is not the original sheet label: two literal parents
of one output y become (|y>,|y>)/sqrt2 and (|y>,-|y>)/sqrt2. Measuring
only the port gives probabilities 1/2,1/2 for both. No permanent
classical record follows from the port's existence. A durable record needs a
specified coupling, reader and subsequent dynamics. The separate Canon
NOWRITE result, invoked in NATIVE.md section 3b, concerns unchanged U
on synchronized checkpoints and fixed checkpoint readers: eventual
constancy forces constancy on the recurrent invariant fiber, excluding
a distinct BLANK-to-permanent-WRITTEN transition in that class. It allows
finite retention and does not exclude added memory or changed dynamics.
That recurrence theorem is not equivalent to two-to-oneness, nor does
this supplied unitary completion evade it within its original scope.

## 14. Exact window frequencies and dyadic counts

Count starting counters 0<=n<N, allowing a window to continue beyond N.
First use the supplied-sheet convention of NATIVE.md section 3g: at each
start the source is X_1, whether or not the preceding actual trajectory
occupies that sheet. A qualifying window returns all pistons and is a
pure fibre translation on the whole sheet; a nonzero translation is not
itself a prepared or read two-path contact.

The bit recursion theta_(2m)=theta_m, theta_(2m+1)=1-theta_m supplies
exact limiting factor frequencies. These are already proved in
[TT-NATIVE-FOUR-WORD-LAW](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L25342),
not merely postulated as the optional K1 weights. For completeness,
the first M bits have one-letter imbalance at most one. An even child
pair is 01 or 10 according to its parent bit; odd child pairs arise as

    00 -> 10,   01 -> 11,   10 -> 00,   11 -> 01.

If p_N is the normalized pair-count vector in order 00,01,10,11 and P
is this permutation matrix, parity splitting gives

    p_(2M)=(0,1/4,1/4,0)+(1/2)P p_M+O(1/M).

An odd terminal start adds O(1/N). The affine map contracts by 1/2;
iterating the error over dyadic scales proves convergence, with error
O(log N/N), to (1,2,2,1)/6. The even/odd triples from a parent pair ab
are a,(1-a),b and (1-a),b,(1-b), giving frequency 1/6 to each of
001,010,011,100,101,110. Four-letter windows have the parity forms

    even: a,(1-a),b,(1-b),
    odd:  (1-a),b,(1-b),c.

Their ten-word language has frequency 1/6 for 0110 and 1001 and 1/12
for each other word. These limits count overlapping native windows;
they are not independent outcome probabilities.

The classification in NATIVE.md section 3g now gives the following exact
limits for a separately supplied X_1 source at every start:

| Length | Nonzero translation density | Identity density |
| ---: | ---: | ---: |
| 2 | 0 | 1/2 |
| 4 | 1/4 | 1/4 |
| 6 | 11/24 | 1/24 |
| 8 | 1/2 | 0 |

For length four the nonzero words are 0011 and 1001, with r shifts +2
and -2 and densities 1/12 and 1/6. For length six all qualifying even
starts are nonzero; the only odd-start exception has parent word 0011,
of density (1/2)(1/12)=1/24 among all starts. For length eight every
qualifying window is nonzero. The qualification condition at each even
length is that its last bit is one, of limiting density 1/2. The
inherited factor estimates also give O(log N/N) errors for these limits.

The finite dyadic counts can be proved without a census. Let
p_h count 00 pairs at starts below 2^h, including the endpoint pair.
For h>=1 the first 2^h bits are balanced, theta_0=0 and theta_(2^h)=1.
Consequently the 11 count is p_h+1. The odd-child pair rule gives

    p_1=0,   p_h=2^(h-2)-p_(h-1)-1 for h>=2,
    p_h=(2^h-3-(-1)^h)/6.                               (JI-47)

The last formula follows by induction. If C_w(M) counts starts below M
of word w, parity splitting gives
C_1001(2M)=C_10(M) and C_0011(2M)=C_101(M), while
C_101(2K)=C_00(K)+C_11(K). Substitution of (JI-47), with the directly
checked first dyadic case, yields for N=2^k, k>=2 and epsilon=(-1)^k

    C_0011(N)=(N/4-epsilon)/3,
    C_1001(N)=(N-3-epsilon)/6.                           (JI-48)

For the unified table below take k>=3. The total qualifying count at
length L is sum_(0<=n<N) theta_(n+L-1). Since
theta_(N+j)=1-theta_j for 0<=j<N, the finite boundary correction gives
N/2+1 for L=2,8 and N/2-1 for L=4,6. The length-six identity count is
C_0011(N/2)=N/24+epsilon/3. Thus the exact counts are

| Length | Nonzero translations | Identities |
| ---: | --- | --- |
| 2 | 0 | N/2+1 |
| 4 | N/4-(1+epsilon)/2 | N/4+(epsilon-1)/2 |
| 6 | 11N/24-1-epsilon/3 | N/24+epsilon/3 |
| 8 | N/2+1 | 0 |

At N=4096 these formulas, not a new execution, give

| Length | Nonzero translations | Identities |
| ---: | ---: | ---: |
| 2 | 0 | 2049 |
| 4 | 1023 | 1024 |
| 6 | 1876 | 171 |
| 8 | 2049 | 0 |

The length-four signed counts are 341 for r+2 and 682 for r-2 by
(JI-48). These reproduce the stated finite counts analytically; an
external run still needs its own verifier and execution evidence.

The actually occupied sheet is a different convention. For n>=1 every
origin-zero X14 trajectory has z_n=4+2 theta_(n-1). A four-tick return of its pistons
is nonzero exactly for the five-letter factors, starting at n-1,

    00110, 01100, 10011, 11001.

For even n-1 these are 01100 or 10011 and arise from parent triples
010 or 101; for odd n-1 they are 11001 or 00110 from the same triples.
Each factor has density 1/12. The total return-window density is 1/3,
with r+2 at odd n and r-2 at even n, each of density 1/6. The qualifying starts
occupying X_1 and those occupying X_4 each contribute density 1/6 among
all counters; conditioned on either occupied sheet, the density is 1/3.
There are no identity four-tick returns under this occupied-sheet
convention. These arithmetic window densities do not supply fresh ready
states, nonoverlapping uses, resets, stored outputs or a contact rate.

For the separately declared contact, the r shifts +2 and -2 give the
same effects (2I+/-[C_r^2+C_r^(-2)])/4. Their phase amplitudes can differ;
this equality does not turn window densities into outcome probabilities.

The proven output is the complete declared two-path instrument, its field
representation, history law and boundaries. NATIVE.md also gives an
actual-U controlled-shift witness conditional on a specified coherent
orbit code. It does not derive that code's preparation or its coherent
output reading. No physical event selection, general phase controller,
free record reset, or identification with photons, neutrinos or another
particle is supplied. The scientific status remains conditional analytical
candidate-T pending independent review.
