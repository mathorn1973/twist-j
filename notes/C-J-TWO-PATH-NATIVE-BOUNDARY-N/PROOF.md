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

The proven output is the complete declared two-path instrument, its field
representation, history law and boundaries. NATIVE.md also gives an
actual-U controlled-shift witness conditional on a specified coherent
orbit code. It does not derive that code's preparation or its coherent
output reading. No physical event selection, general phase controller,
free record reset, or identification with photons, neutrinos or another
particle is supplied. The scientific status remains conditional analytical
candidate-T pending independent review.
