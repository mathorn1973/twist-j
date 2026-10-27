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

The proven output is the complete declared two-path instrument, its field
representation, history law and boundaries. No native coupling, physical
event selection, phase control, free record reset, or identification with
photons, neutrinos or another particle is derived here. The scientific
status remains conditional analytical candidate-T pending independent review.
