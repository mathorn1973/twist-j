# A strict coincidence-support obstruction

**NON-CANONICAL / L1 / conditional analytical candidate-T.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: #1803. No scientific executable or numerical experiment is used.

This statement concerns the complete sixteen-dimensional total-momentum-pi
sector of the L=4, mu=2 comparison model in #1793 at
`6f8e8e93a3b459695262c50c2ccbd120cdeb7e99`. It does not classify all spatially
local interactions, nor transfer its conclusion to the different point
contact in #1795. We use hbar=1.

Write S=C^4_momentum tensor C^2 tensor C^2 and

    u=(1/2) sum_(k in {0,pi/2,pi,3pi/2}) |k,pi-k>,
    P=|u><u| tensor I_4,
    A_c=2Y-Z,                 A_c^2=5I.

The free sine-energy operator on the momentum block k is

    H0(k)=2 cos(k)(-X_1+X_2)+sin(k)(A_(c,1)+A_(c,2)).       (L1)

In particular P H0 P=0, by averaging the sine and cosine over the four
momenta. Let B be any finite-dimensional complete source, including all
controllers and clocks, with self-adjoint energy H_B. Consider precisely
the self-adjoint interactions J satisfying

    J=(P tensor I_B) J (P tensor I_B),
    [J,H0 tensor I_B+I_S tensor H_B]=0.                    (L2)

The first condition is strict coincidence support. The second demands
conservation of the fixed bare additive account under the full generator
H0+H_B+J at every time. Shifting H0 by 2sqrt5 I, as in H_S, changes neither
condition. All operators here are finite and bounded; no domain extension
to an unbounded source is claimed.

## 1. The map from coincidence to its exterior

Set T=(I-P)H0P, as a map from Ran(P). Since P H0 P=0,
T^*T=P H0^2 P. Identify Ran(P) with the four-dimensional coin through
v -> u tensor v. The four-point average of (L1) gives

    T^*T=(1/2)[4(-X_1+X_2)^2+(A_(c,1)+A_(c,2))^2]
        =9I-4F+5G,                                        (L3)
    F=X tensor X,             G=(A_c tensor A_c)/5.

F and G are self-adjoint involutions. They commute because X A_c=-A_c X.
Also Tr(F)=Tr(G)=Tr(FG)=0; the last identity follows from Tr(X A_c)=0.
Thus each joint projector

    (I+fF)(I+gG)/4,                 f,g in {-1,1},

has trace and rank one. The corresponding eigenvalues in (L3) are
9-4f+5g, giving the complete spectrum

    0, 8, 10, 18.                                         (L4)

The kernel is exactly one-dimensional, with coin projector

    D_c=(I+F)(I-G)/4,
    D=|u><u| tensor D_c.                                   (L5)

D is a rank-one subprojection of P, and H0 D=0: its exterior component
vanishes by (L3), and its coincidence component by P H0 P=0. By adjointness
also D H0=0. The name dark state below means only this precise kernel.

## 2. The entire admitted interaction class

Compress the commutator in (L2) from P to I-P. The source-energy term has
no off-diagonal system block, and the support of J removes the other term.
Consequently

    (T tensor I_B) J=0.                                   (L6)

The range of J is contained in Ran(D tensor I_B). Self-adjointness gives
the same support on its input side. Since D has rank one, every such
operator is D tensor C for one self-adjoint source operator C. Using
H0 D=D H0=0, its remaining commutation condition is [C,H_B]=0. Conversely
every such C satisfies both conditions (L2). Hence the exact classification
is

    J=D tensor C,       C=C^*,       [C,H_B]=0.             (L7)

Only the single zero-energy contact state can participate. In the
scalar-contact subclass J=P tensor B_0, this implies B_0=0, because
P-D is a nonzero subprojection whereas every operator in (L7) vanishes
on its range. Extra source capacity or coherence does not alter (L7).

## 3. A nonzero implementation-error floor

The predecessor's normalized input is

    a=|0,pi> tensor |-x,+x>.

Its coin has F=-1, whereas D_c requires F=+1. Therefore

    D a=0,                       H0 a=4a.

For every interaction (L7), every source density, and every time,
evolution under H_full=H_S+H_B+J leaves the system marginal exactly
|a><a|. This follows directly: the subspace a tensor B is invariant,
J vanishes there, and H_S acts by the scalar 4+2sqrt5.

For the desired contact put

    K_g=I+bP,       b=exp(-ig)-1,       s=sin^2(g/2),
    V_g=K_g(U_2 tensor U_2).

The free pair step maps a to -a, so V_g a=-K_g a. Since <a,P a>=1/4,

    |<a,V_g a>|^2=|1+b/4|^2=1-3s/4.

The pure-state trace-distance identity then gives exactly

    (1/2)|| |a><a|-|V_g a><V_g a| ||_1=sqrt(3s/4).        (L8)

This is a lower bound for the worst-case implementation error over all
inputs, not a claim to have optimized the entire channel distance. At
g=2pi/5 the displayed value is

    sqrt[3(5-sqrt5)/32] > 0.                              (L9)

Thus even arbitrarily large finite coherent sources cannot approximate
the target arbitrarily accurately within (L2). For g in 2pi Z this
particular lower bound is zero and supplies no obstruction.

## 4. Boundary and the next spatial contract

The obstruction needs all three hypotheses: this fixed sine-energy
account, strict coincidence support, and preservation of that bare account
throughout time. It does not exclude interactions that extend beyond
coincidence (including finite-range interactions), preservation only at
specified endpoints, a full conserved energy with interaction terms while
the bare account changes, or a different free-energy/dynamics contract.

The source lift in PROOF.md lies outside this class: no coincidence-only
support is asserted for its spectral couplings. Its positive controller
Hamiltonian therefore does not contradict (L7). Conversely a successful
abstract source lift does not establish its spatial implementation.

A next spatial construction must state which hypothesis changes. If the
bare account must remain conserved at every time, the coupling must act
outside P on the relevant bright components. If a strictly supported
contact is retained instead, its interaction energy can be part of the
conserved full Hamiltonian while the bare account changes during contact;
the endpoint law and source budget must then be proved anew. Neither
option is selected or implemented by this negative result.
