# C-J-RAMIFIED-CROSSING-N: proof and limits

NON-CANONICAL / NO AUTHORITY. L1 mathematical candidate only. Scope and
predicted numerical witnesses were posted before the first audit in issue
#2102. This is a proof-led, result-exposed audit, not a formal public probe.

## Integral carrier and exact two-cut identity

Let L=Z[j], Phi_5(j)=0, with basis (j,j^2,j^3,j^4), and let
B(x,y)=Tr_{Q(j)/Q}(x conjugate(y)). The matrix is G=5I-11^T. Its
eigenvalues are 1,5,5,5, its determinant is 125, and its reduction modulo 5
has rank one. The gcd of its entries is one. The determinant and modular
rank therefore force Smith invariants (1,5,5,5). In particular,
G^-1=(I+11^T)/5 and the trace-dual lattice L# has quotient
L#/L isomorphic to (Z/5)^3.

Write E_k=Lambda^k L. Creation c_j is wedge by the j-th basis vector.
Contraction a_i on a wedge of k basis vectors is the alternating sum
over deletions, weighted by B(e_i,e_r). The standard wedge Leibniz rule
gives a_i c_j+c_j a_i=G_ij I on each grade. No spin-statistics or
physical fermion interpretation is required.

On E_2 let T+_(i,j,alpha,beta)=(a_i c_j)_(alpha,beta) and
T-_(i,j,alpha,beta)=(c_j a_i)_(alpha,beta). Their sum is
G_ij delta_(alpha,beta). The T+ matrix on the cut
(i,alpha)|(j,beta) factors through E_3, and the T- matrix on
(j,alpha)|(i,beta) factors through E_1. Both intermediate ranks are four.

### Exact Smith invariants of the two cuts

One may independently change the creation labels, the annihilation
labels and the induced wedge bases by unimodular matrices. In detail,
if U G V=diag(1,5,5,5), use the column basis V on L and its induced wedge
bases, and the row basis U for the contraction labels. These changes
induce unimodular changes on both cut matrices and replace G by the
displayed diagonal pairing.

The joint creation map L tensor E_2 -> E_3 has a split integral
surjection: every wedge of three distinct basis elements is a signed
image of one basis column. The stacked creation map E_1 -> (E_2)^4
has a split integral injection: each basis element has a signed
coordinate that occurs in no other column. Hence the nonzero Smith
invariants of T+ are those of stacked contractions E_3 -> (E_2)^4,
and those of T- are those of joint contractions (E_2)^4 -> E_1.

For the diagonal pairing d=(1,5,5,5), each column indexed by a triple S
in the first contraction matrix has nonzero entries +-d_i, i in S, in
rows disjoint from all other columns. Its gcd is one for the three
triples containing the first index, and five for the other triple.
For the second contraction matrix each row indexed by a singleton r
has entries +-d_i, i!=r, in columns disjoint from all other rows.
The gcd is five for r=1 and one for the other three rows.
Independent Bezout operations reduce these disjoint supports. Both cut
Smith lists are therefore (1,1,1,5); rank four over Q and three over F5.
The target matrix on (i,alpha)|(j,beta) has Smith list 1^6,5^18
because it is G tensor I_6 up to a permutation of coordinates.

Using a trace-dual basis for the annihilation labels replaces G by I_4,
so the same calculation gives (1,1,1,1) for both cuts, and I_24 for
the target. This changes the admitted label lattice; it is not an
integral change of basis within the original self-paired lattice.
The index of that change is exactly 125. No native availability or
physical resource cost of dual labels follows.

## Exact commutator and common paired transport

Set sigma(j)=j^2 and D=(sigma-I)/(1-j). Integrality follows on
the basis from D(j^k)=-sum_(t=0)^(k-1) j^(k+t).
For J=1+j^2 and u=j^2+j^3=-phi, direct expansion gives
K=[M_J,D]=M_u sigma. The unit u has inverse -(j+j^4).
Moreover sigma(u)=j+j^4, so u sigma(u)=-1 and
K^2=-sigma^2=-conjugation, K^4=I. In particular K is integral
and invertible. This is a new specified commutator on this carrier,
not the selected public spatial curvature operator.

The same action on both labels does not preserve the trace form:
B(1,1)=4 but B(K1,K1)=Tr(2+j+j^4)=6.
The unique inverse-adjoint action on the other label is
K^vee=M_(1/conjugate(u)) sigma = M_(u^-1) sigma.
Since sigma commutes with conjugation and preserves the trace,
B(Kx,K^vee y)=B(x,y) for every x,y. Both maps are integral
unimodular, and the relation iterates to every integer power.
Equivalently, on the full dual lattice, transport of contraction
labels is contragredient to transport of creation labels.

This supplies a single fixed pairing and its compatible paired
transport, not two post-selected normalizations. It does not show
that a native contact realizes either action on the corresponding
exterior data or that a physical spatial reading selects this K.

## Reader boundary and sharp repair

For x in L, write b=Gx. Modulo 5 every coordinate b_i equals
-sum x_j. On L/5L the map has five fibres of 125 points each.
The nonzero vector e_1-e_2 is invisible to this read, even compared
with zero. It is not zero as an element of L/5L.

Define d_i=(b_i-b_4)/5 modulo 5, i=1,2,3. Division is exact
because b_i-b_4=5(x_i-x_4). Put s=-b_4 modulo 5. Then
x_4=4(s-d_1-d_2-d_3) modulo 5 and x_i=x_4+d_i.
Thus the four residues (s,d_1,d_2,d_3) read the complete 625-point
domain. Any fixed first read with 125-point fibres needs at least
125 supplementary distinguishable values, or at least three F5
digits. The construction attains the bound. Equivalently b mod 25
suffices since 5x=(I+11^T)b. These are mathematical observations,
not a native reader, native time lower bound or result on a particular
prepared carry-state domain.

## What this says about the two comparisons

The OpenAI shifted crossing construction uses an integral exterior
operator identity and two different cuts, with unimodular normalization
of its pairing and asymptotically increasing grades and mode sets.
Our construction is a finite four-mode analogue with the actual
cyclotomic trace pairing. It proves neither the asymptotic rank law
nor Euclidean rigidity for the TWIST-J carrier.

For nonzero s-minors over Z define mu_s(A) as the minimum 5-adic
valuation. Smith invariants give mu_1=mu_2=mu_3=0, mu_4=1 for
each of the two original cuts; after the trace-dual change all
four are zero. With valuation normalized by v_(1-j)(1-j)=1,
the corresponding value one for v_5 becomes four for v_(1-j).
The same ordinary rational rank is compatible with differing
determinantal valuations. This is a finite diagnostic for the
distinction between rank and arithmetic minor control. It does not
supply any estimate for a separate RH/GRH seesaw family, its actual
character fields, common normalization or positional loss.

Source of the finite analogue: OpenAI, Euclidean geometry in the
asymptotic spectrum of tensors, 2026-11-24, crossing-appendix.tex,
blob 652ecbca74d8f0466ea39fcf7dfd00db5444e893 and curvature.tex,
blob 9269654e26f361ff7b130ae3adcc8007db719a04, in
https://github.com/openai/math/tree/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026.
The source is read, not compiled or independently verified. No copied code.

Public arithmetic context: TRACEKERNEL-RESIDUAL-FORM,
TRACEKERNEL-HOME-DIMENSION, A4-RAMIFIED-HODGE-TRACEKERNEL,
COMPLETE-STATE-OBSERVATION-CONTRACT, QDD-COMMUTATOR-READOUT-EQUALITY-FORK.
No identifier or layer is promoted. The full physical curvature-forcing
owner remains O. All conclusions above are candidate-T at this bounded L1
scope only; the execution is candidate-C corroboration.
