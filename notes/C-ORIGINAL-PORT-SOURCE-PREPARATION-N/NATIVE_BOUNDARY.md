# Original native update: source-preparation boundary and a usable exchange

**NON-CANONICAL. L1. Conditional analytical candidate.**

Author: A. M. Thorn. Date: 2026-10-25. Apache-2.0.
This is a same-session analytical derivation, without independent acceptance.
No scientific executable, enumeration or simulation supplies its conclusions.
The statements below neither change the Canon nor establish a material
realization of the original spatial source.

## 1. Authority, carriers and the actual native rule

The authority used here is Public Canon v105, pinned at
[`892a0b11089d34e241e1eb76d2c03247022d18e6`](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
Its declared content commit is
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`; its Canon SHA-256 is
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`
and its byte count is 1295029. The native definitions are in
[section 2](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L460-L487)
and the [displayed generator formulas](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L596-L611).

Write the original autonomous state and update as

\[
 \Omega=\mathbb N_0\times\mathbb F_5^6,\qquad
 x=(p_1,p_4,p'_1,p'_4,q,r),\qquad z(x)=\sum_{i=1}^6x_i,
\]
\[
 \theta_n=s_2(n)\bmod2,\qquad
 U_{\rm nat}(n,x)=(n+1,g_{z(x)+2\theta_n}(x)),
 \quad(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e).
 \tag{N1}
\]

The subscript in (N1) and every checkpoint coordinate are reduced modulo
five. The counter is part of the state. It is not an externally chosen
sequence of generator calls. The five affine involutions are

\[
\begin{aligned}
a(x)&=(p_4,p_1,p'_4,p'_1,q,r),\\
b(x)&=(-p'_1,-p'_4,-p_1,-p_4,-q,-r),\\
c(x)&=(2-p'_1,1-p'_4+r,2-p_1,1-p_4-r,1-q,-r),\\
d(x)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,1-q,1-r),\\
e(x)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,2-q,1-r).
\end{aligned}
\tag{N2}
\]

The specified occupation-space walk in the source experiment has a
different carrier and operator, here denoted \(U_{\rm rec}\). Its complex
amplitudes, token/pulse arrangements, contact and receiver calibration
are additional construction data. The Canon explicitly says that its
occupation intertwiner is not an intertwiner from (N1), and does not
derive those preparation operations from (N1):
[HOMOGENEOUS-CAPTURE-CURRENT-RECORD, scope](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27430-L27438).
No use of the same letter \(U\) identifies these two laws.

## 2. The full native map has no direct unitary basis lift

At counter zero consider the distinct heads

\[
 x=(4,1,0,0,0,0),\qquad y=(2,1,1,2,1,0).
\]

Their traces are zero and two. Thus the actual selectors choose \(a\)
and \(c\), respectively, and substitution into (N2) gives

\[
 U_{\rm nat}(0,x)=U_{\rm nat}(0,y)
   =(1,(1,4,0,0,0,0)).
 \tag{N3}
\]

Consequently the prescription
\(|n,x\rangle\mapsto|U_{\rm nat}(n,x)\rangle\), with distinct native
states represented by orthonormal basis vectors, is not an isometry on
the full origin-zero input family. It sends two orthogonal vectors to
the same vector. This exact collision is also recorded in
[U-NATIVE-CHART-AND-QDD-READBACK](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L1075-L1092).

This obstruction concerns that full carrier and that literal basis lift.
It permits a declared injective input family, a retained distinguishing
register, or another explicit reversible extension. Section 4 supplies
an injective family. A unitary extension that stores the distinction of
(N3) in garbage is a changed carrier whose garbage cannot be omitted
from a preparation or reset account.

## 3. What the chart and the coefficient factor do establish

For \(n\ge3\), the registered native chart is a bijection

\[
 J_n:\mathbb F_5^5\longrightarrow
 X_n=\{x:z(x)=4-3\theta_{n-1}\},\qquad
 U_nJ_n=J_{n+1},
 \tag{N4}
\]

where \(U_n(x)=g_{z(x)+2\theta_n}(x)\). See the
[chart formulas and transport identity](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L1041-L1079).
On the linear spans of these basis sets, write \(\mathcal J_n\) for
the unitary basis identification induced by \(J_n\), and \(\mathsf P_n\)
for the bijective native basis map from \(X_n\) to \(X_{n+1}\). Then

\[
 \mathcal J_{n+k}^{*}\mathsf P_{n+k-1}\cdots
       \mathsf P_n\mathcal J_n=I\qquad(n\ge3,\ k\ge0).
 \tag{N5}
\]

This follows by iterating (N4). In the same transported chart coordinates,
unchanged native evolution preserves all five labels. A fixed reader of
those labels therefore reads the same state. Assigning a new gate to a
time-dependent reader does not derive that gate as a physical operation.
Equation (N5) is not a prohibition on other readers: fixed checkpoint
coordinates do change, and the early exchange below is real.

The separate SOURCE-PHASE-NATIVE proposal is inspected at the immutable
pin `5ce14091995dfdc0e57fe7b256b72aed6f16ac3e`. Its
[local factor](https://github.com/mathorn1973/twist-j/blob/5ce14091995dfdc0e57fe7b256b72aed6f16ac3e/notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md#L245-L340)
starts with a finite-support coefficient field over
\(\mathcal O=\mathbb Z[\zeta_{20}]\), retained scale and static labels.
It defines a coupled network by applying \(U_n\) at every cell and then,
every third tick, replacing its fifth chart label by
\(\epsilon\mapsto B\epsilon\), where \(B=4\operatorname{Adj}\) over
\(\mathbb F_5\). The resulting statement is

\[
 \Pi_{\rm loc}\widetilde U=U_{\rm net}\Pi_{\rm loc}.
 \tag{N6}
\]

The extra label replacement is explicitly part of \(U_{\rm net}\).
It is not supplied by (N4). Equation (N6) is a surjective semiconjugacy
from the enlarged coefficient carrier, rather than an inverse
construction of that carrier from the six checkpoint coordinates.

There is an elementary obstruction to such an inverse on its full
declared coefficient family. Choose distinct unit coefficient-port basis
vectors \(v_0,v_1\) and the two raw tables

\[
 a_+=v_0+5v_1,\qquad a_-=v_0-5v_1.
 \tag{N7}
\]

They have the same residues at every port under the stated maps to
\(\mathbb F_5\), the same norm \(\sqrt{26}\), and can use the same
static labels and normalization scalar \(1/\sqrt{26}\). Their complex
Hilbert readings
\((v_0+5v_1)/\sqrt{26}\) and \((v_0-5v_1)/\sqrt{26}\) are distinct
even as rays. Their projected native initial data coincide, so their
entire deterministic projected histories coincide. No common reader
receiving only those projected heads, the counter, their histories and
the common normalization scalar can recover both Hilbert readings.
This remains true for the coupled network in (N6); the added raw field
is exactly the information omitted by the projection.

The obstruction assumes that no further input label retains the omitted
coefficient information. It does not exclude a separately declared
encoding of a restricted finite source family. Likewise the proposal's
[localized-ring boundary](https://github.com/mathorn1973/twist-j/blob/5ce14091995dfdc0e57fe7b256b72aed6f16ac3e/notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md#L204-L242),
\(\mathcal O[1/5]\not\to\mathbb F_5\) as a unital ring map, concerns
that coefficient reduction. It is not a theorem excluding every
finite-register encoding or every physical realization.

## 4. An exact native SWAP, including an occupied second register

At counter zero define the 25-head code

\[
 E(\lambda,\mu)=(\lambda,\mu,-\lambda,-\mu,0,0),
 \qquad\lambda,\mu\in\mathbb F_5.
 \tag{N8}
\]

Every head has trace zero, and \(\theta_0=0\). Thus every term uses
the same actual selector \(a\), with

\[
 U_{\rm nat}(0,E(\lambda,\mu))=(1,E(\mu,\lambda)).
 \tag{N9}
\]

The two fixed coordinate blocks are \((p_1,p'_1)\) and
\((p_4,p'_4)\), each restricted to its zero-sum code. Equation (N9)
exchanges their values without assuming that the second is blank.
It generalizes the first step of the Canon's
[native one-shot source family](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L7232-L7264),
which takes \(\mu=0\).

Let \(\mathcal E_n|\lambda,\mu\rangle=|n,E(\lambda,\mu)\rangle\).
On this declared code the linear extension \(\mathsf A\) of (N9)
is an isometry and satisfies

\[
 \mathsf A\mathcal E_0=\mathcal E_1\operatorname{SWAP}.
 \tag{N10}
\]

Tensoring (N10) with \(I_R\) proves the same identity on arbitrary
code states correlated with a passive reference \(R\), including mixed
states by linearity. The old second-register information moves to the
first register and is retained. This is an exact mathematical statement
about a chosen linear extension of an injective native branch. It does
not derive coherent amplitudes, the reference carrier, a material
Hilbert-space implementation or the input preparation from the classical
checkpoint law.

This is a one-tick primitive at the declared counter. After (N9), the
checkpoint trace is still zero but \(\theta_1=1\), so the next actual
native selector is \(c\). Repeated freely scheduled calls to \(a\) do
not follow from (N9); counter preparation and any intervention must be
included before such a schedule is claimed.

## 5. Relative eigenphase and its readiness requirement

For \(\lambda\ne\mu\), define already prepared checkpoint states

\[
 |\chi_\pm\rangle=
 \frac{|E(\lambda,\mu)\rangle\pm|E(\mu,\lambda)\rangle}{\sqrt2}.
 \tag{N11}
\]

Both configurations have trace zero, so the actual counter-zero step
acts on their linear span as

\[
 \mathsf A(|0\rangle\otimes|\chi_\pm\rangle)
   =\pm|1\rangle\otimes|\chi_\pm\rangle.
 \tag{N12}
\]

On a superposition of the two eigenspaces this is a relative phase
change. On one eigenstate alone the sign is global. Equation (N12)
does not provide a controlled-SWAP or a phase control conditional on an
independent source bit. Such a controller and its common input state
would require another explicit native admission.

The larger checkpoint sheet \(X_0=\{x:z(x)=0\}\) is invariant under
\(a\) and has \(5^5=3125\) heads. A fixed head obeys
\(p_1=p_4\), \(p'_1=p'_4\), and
\(2p_1+2p'_1+q+r=0\), leaving \(5^3=125\) choices.
The other 3000 heads form 1500 transpositions. Hence its permutation
lift \(A_0\) has

\[
 \dim\ker(A_0-I)=1625,\qquad
 \dim\ker(A_0+I)=1500.
 \tag{N13}
\]

Put \(P_-=(I-A_0)/2\). Its diagonal matrix element in a checkpoint
basis state is zero on fixed heads and \(1/2\) on every other head.
For any checkpoint-diagonal density matrix \(\rho\) and any density
matrix \(\sigma=P_-\sigma P_-\), therefore,

\[
 \operatorname{Tr}(P_-\rho)\le\tfrac12,\qquad
 D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1\ge\tfrac12.
 \tag{N14}
\]

The second inequality follows by testing the two states with the effect
\(P_-\). Classical randomized preparations, deterministic checkpoint
updates and permutation lifts with checkpoint-diagonal ancillas remain
diagonal after discarding classical auxiliary registers. They cannot
prepare the required antisymmetric state within trace distance below
\(1/2\) in this carrier. Equation (N14) is a preparation-class bound,
not a claim about every Gibbs state: a separately supplied Hamiltonian
may already have coherent eigenvectors in the checkpoint basis. Its
couplings, preparation and thermodynamic resources would then be part
of the proposed apparatus.

This clarifies a tempting finite dictionary for the source phase
selector \(F=I-2P_{\rm src}\), where \(P_{\rm src}\) projects onto
two source occupation ports. Choose two orthonormal vectors in the
minus eigenspace of \(A_0\) and, for an admitted F-invariant finite source
space containing \(\operatorname{span}\{u_2,u_3\}\) and having dimension
between 2 and 1627, enough orthonormal vectors in its plus
eigenspace. A target-chosen isometry \(J\) then satisfies

\[
 A_0J=JF.
 \tag{N15}
\]

This is a valid conditional dictionary, not an implementation in the
original occupation reading. In particular, \(Fu_2=-u_2\) forces
\(Ju_2\in\operatorname{ran}P_-\). The known occupation input \(u_2\)
cannot simultaneously be represented by a single native checkpoint
basis state. Preparing its chosen code already faces (N14). Using
\(J\) as a supplied decoder also requires its own physical admission;
the dimensions in (N13) do not provide one.

## 6. Bounded admission contract for the source gates

The active source pair motivating this question is pinned by
[#1775, comment 6399173427](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399173427):
`ACTIVE_EQUAL_SPECTRUM.md`, 23985 bytes, SHA-256
`c6c5e76e48014ba8f670ff9ae8ea44557867b9dc92de38cef94a5e527bad7e5f`.
Its supplied loader and phase selector act on the source factor,
independently of the occupied memory and reference. In its notation,
one requires \(G_+Lu_2=\psi_+\) and
\(F\psi_+=-\psi_-\), with \(F=I-2P_{\rm src}\).
The source contains coherent token and pulse components. The present
note proves neither of these preparations from (N1).

A next native admission must fix the following data before claiming
that connection:

1. **Carrier and input.** Specify the finite native registers, counter
   interval, every auxiliary input, and a common embedding of the known
   input port and the admitted source space. Keep arbitrary occupied
   memory/reference inputs separate. State whether the ready source is
   a checkpoint basis state, a diagonal mixture or supplied coherence.
2. **Actual rule and phase control.** Exhibit the actual selectors of
   (N1), or declare every added coupling. Give the complete action on
   failures and invalid codes. For a coherent phase selector, include
   its control register and relative control phase; independently
   selected classical settings do not establish controlled kickback.
3. **Fixed reader and target.** Freeze a common source-to-occupation
   reader and its physical implementation before assessing the target
   response. Prove the preparation and phase identities jointly with
   \(I_{\rm mem,ref}\), on the stated inputs. A different reader chosen
   for each setting is not this contract. If a preparation channel or
   decoder leaves garbage, retain it and prove the required reduced
   channel without assuming it is independent.
4. **Resources and reuse.** Count the coherent donor, phase reference,
   clocks, controls, work storage, entropy sinks and any retained
   distinguishing labels. State the output time and support, error norm
   uniform over the admitted references, and the reset or consumption
   rule for every branch. A finite approximation requires an explicit
   error budget; an exact algebraic gate does not imply exact material
   couplings.

The decisive positive test is one complete source preparation and one
phase selection in this fixed interface, with the original receiver's
joint output law preserved. A faithful finite encoding is allowed, but
its admission must state what it realizes and whether the original
occupation state itself is produced. No blanket impossibility follows
for extensions that meet this contract.

## 7. Falsifiers and remaining scope

An exact failure of (N3), (N4), (N9), the fixed-head count in (N13), or
the diagonal estimate in (N14) falsifies the corresponding bounded
claim. A reader recovering both states in (N7) from identical declared
projected inputs falsifies the no-inverse statement. A proposed escape
using an extra label, another reader, pre-existing coherence or a new
coupling changes a stated hypothesis and must be assessed in its own
admitted carrier.

The native SWAP and eigenphase are useful algebraic components. The
physical coherent source preparation, its fixed occupation reader,
its complete energy account and its regeneration remain open here.
All new deductions in this note remain NON-CANONICAL L1 candidates
pending independent review.
