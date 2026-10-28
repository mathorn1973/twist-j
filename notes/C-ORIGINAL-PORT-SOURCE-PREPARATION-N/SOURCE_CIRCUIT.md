# Exact preparation by three finite selection blocks

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance of this construction is pending.** Author: A. M. Thorn.
License: Apache-2.0.

This note gives a complete unitary circuit for the contact-active source
pair specified in the auxiliary ACTIVE_EQUAL_SPECTRUM.md record of
[#1775](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399077081).
It assumes that record's exact source identities and normalization. It
does not extend the primary experiment's registration to this source
construction or claim independent acceptance of either result.

The circuit replaces a single target-dependent rotation on a large source
span by explicitly specified selection, attenuation and reflection gates.
It uses the full U_rec, including its interaction with the receiver.
All inverse calls, supplied rotations and preparation resources are
listed. Their original-native derivation and physical control admission
are separate obligations. No scientific executable was run.

## 1. Fixed source and an entire unknown-memory input subspace

Use the unchanged one-pair, one-carrier Canon v105 model at
[892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L27411-L27565).
Write U=U_rec on H_S tensor M, where H_S contains the object and
token/pulse coordinates, coins, banks and carrier label, and M=C^26 is
the actual receiver memory. An arbitrary passive reference is retained.
The receiver position is 100. Let

```text
u2=|R=97,r=0,e2; y=97,t0>,
u3=|R=97,r=0,e3; y=97,t0>,
chi_s=i(u2-u3)/sqrt(2),
J_chi xi=chi_s tensor xi,              xi in M.
```

The complete supplied seed loader on H_S is

```text
L|span(u2,u3) = (i/sqrt(2)) [[1,1],[-1,1]],
L|span(u2,u3)^perp = I.
```

It is unitary and L u2=chi_s. It acts as identity on M and the reference.
Define D=U^2-U^(-2). The #1775 identities give

```text
D J_chi = d_s tensor I_M,
<chi_s,d_s>=0,
Z=1+||d_s||^2=(39521+154 sqrt(5))/15625,
psi_s,+ =(chi_s+d_s)/sqrt(Z),
psi_s,- =(chi_s-d_s)/sqrt(Z).                         (S1)
```

Here d_s is a fixed source vector; the tensor formula means
D(chi_s tensor xi)=d_s tensor xi for every xi. This factorization follows
because both U^(+2) and U^(-2) move the carrier at most two sites from 97.
Their support has carrier coordinate at most 99, so receiver calibration
is identity at both ends. No unknown memory vector enters a gate definition.

The circuit prepares psi_s,+ tensor xi for every state on the entire M,
including reference correlations. The #1775 receiver-flag contrast later
uses the narrower old-memory space span(d1,...,d25), which excludes an
initial d0 flag. Preparation of all M does not broaden that readout theorem.

The exact value of Z is a mathematical calibration input. Positivity gives

```text
Z>39521/15625>9/4,                 1<=Z<=5.            (S2)
```

The upper bound follows also from ||D||<=2. The strict lower bound follows
from 4*39521=158084>140625=9*15625.

## 2. Complete selection and attenuation gates

Add a qutrit a with basis 0,1,2 and a qubit b, both initially zero.
These are supplied pure auxiliaries, not free thermal readies. Define

```text
omega=(|0>+|1>+|2>)/sqrt(3),
v=(|0>-omega)/sqrt(2-2/sqrt(3)),
R=I-2|v><v|.
```

R is a complete qutrit unitary, R=R*=R^(-1), and R|0>=omega.
On the qutrit and the entire source/memory space set

```text
SELECT=|0><0| tensor I
       +|1><1| tensor U^2
       -|2><2| tensor U^(-2),
B=(R* tensor I) SELECT (R tensor I).                 (S3)
```

SELECT is a direct sum of complete unitaries. In particular,

```text
(<0| tensor I) B (|0> tensor I)=(I+U^2-U^(-2))/3.     (S4)
```

For an explicit gate sequence, let C_j(V) apply V when a=j and identity
otherwise, and let J_minus=diag(1,1,-1). Then

```text
SELECT=(J_minus tensor I) C_2(U*) C_2(U*) C_1(U) C_1(U).
```

The two controlled sectors commute. This expression uses two forward and
two inverse conditional source calls, plus one qutrit sign gate. Its
inverse reverses these gates and adjoints each source call. U* is a
supplied inverse operation, not a negative physical waiting time.

The global phase of U is part of each controlled call. In Canon notation,

```text
U_rec=Tcal [exp(-i beta) Rcal Wcal C] Tcal,
beta=4pi/5.
```

Dropping exp(-i beta) inside C_j(U_rec) changes the relative phase of the
qutrit branches, the polynomial in (S4), and generally the target. An
implementation known only up to an uncontrolled global phase is therefore
insufficient. Receiver calibration Tcal is also retained in every call;
no receiver-isolation operation is assumed.

Set

```text
t=3/(2sqrt(Z)),       s=sqrt(1-t^2),
T=|0><0|_a tensor [[t,-s],[s,t]]_b
  +(I-|0><0|_a) tensor I_b,                         (S5)
```

with identity on source and memory. By (S2), 0<t<1 and s>0. T is a
complete two-register controlled rotation, including its action on b=1.
It is an additional exact irrational calibration, explicitly supplied
rather than derived from the original six-pentit law or from U_rec.

With the evident tensor order, define the full unitary

```text
Aop = T (B tensor I_b) (I_(a,b) tensor L tensor I_M).
```

It acts on every raw input, including every flag value and source state.

## 3. Exact amplification on the whole memory subspace

Let

```text
P=|0,0,u2><0,0,u2|_(a,b,S) tensor I_M,
Pi=|0,0><0,0|_(a,b) tensor I_(S,M),
R_in=I-2P,                S_good=I-2Pi.
```

Both reflections are complete unitaries. R_in selects a fixed basis
source port and the two fixed auxiliary values, while acting identically
on every memory and reference vector. It is not a reflection about an
unknown joint memory state.

Define the isometry V_seed on Ran(P) by

```text
V_seed(|0,0,u2> tensor xi)=|0,0> tensor psi_s,+ tensor xi.
```

Equations (S1), (S4) and (S5) give

```text
Pi Aop P=(sqrt(Z)/3)t V_seed P=(1/2)V_seed P,
P Aop* Pi Aop P=(1/4)P.                             (S6)
```

Thus the unattenuated success probability Z/9 is set to precisely 1/4.
No success branch is measured or discarded. The complementary amplitude
remains in the complete flag/source state until the next operations.

The preparation unitary is

```text
W_prep=-Aop R_in Aop* S_good Aop.                    (S7)
```

For a direct proof, take any eta in Ran(P), put Psi=Aop eta and
g=Pi Psi. Let P_A=Aop P Aop*. Equation (S6) implies
P_A g=Psi/4. Consequently

```text
(I-2P_A)(I-2Pi)Psi
 =Psi-2g-2(Psi-2P_A g)
 =-2g.
```

After the overall minus in (S7), the result is 2g=V_seed eta. Therefore

```text
W_prep P=V_seed P.                                  (S8)
```

This is an operator identity on a 26-dimensional seed subspace, not only
a calculation for one memory basis value. Tensoring with identity on any
passive reference and taking mixtures yields

```text
W_prep [|0,0,u2><0,0,u2| tensor rho_(M,R)] W_prep*
 =|0,0><0,0| tensor |psi_s,+><psi_s,+| tensor rho_(M,R).
                                                               (S9)
```

The two auxiliaries return exactly to zero. The old memory, including all
reference correlations, is exactly restored at this endpoint. During the
middle and last selection blocks, receiver crossings and memory exchange
may occur. Memory independence throughout the preparation is not claimed.

Every operation in (S7) is a full-space unitary. Their action outside
Ran(P) is retained; no behavior on dirty flags or different source inputs
is erased to obtain (S8). The overall minus can be omitted for an entire
unconditionally executed preparation without changing any density matrix.
If this preparation is coherently controlled as part of another circuit,
its phase convention must be retained or compensated explicitly.

## 4. The second phase, including a coherent selector

The #1775 source identities also give that d_s has zero coefficient at
both u2 and u3. Define

```text
P_src=|u2><u2|+|u3><u3|,       F=I-2P_src
```

on H_S, with identities on M and all references. Then
F psi_s,+=-psi_s,-. For a classical choice of setting this global sign
does not affect the prepared density matrix.

If a qubit q selects the phase coherently, use the complete controlled
unitary

```text
V_choice=|0><0|_q tensor I + |1><1|_q tensor (-F).     (S10)
```

It can be written as controlled-F followed by Z on q. The latter is a
counted phase correction; omitting it would change off-diagonal selector
coherences. On the admitted prepared source, (S10) gives the exact map
|0>psi_s,+ and |1>psi_s,- with the stated relative phase, even when q,
M and the passive reference are initially correlated.

## 5. Exact operation counts and timing contract

Expand each SELECT as in Section 2. The circuit (S7) contains:

| Operation | Count |
| --- | ---: |
| Conditional U_rec | 6 |
| Conditional U_rec* | 6 |
| Seed loader L or L* | 3 |
| Qutrit R or R* | 6 |
| Qutrit J_minus | 3 |
| Attenuation T or T* | 3 |
| Fixed-seed reflection R_in | 1 |
| Good-flag reflection S_good | 1 |

This is 29 named operations, or 17 if the three SELECT blocks are each
counted as one composite operation. The table uses the expanded count;
the inverse source calls are not omitted. The unobservable overall phase
is separate. The optional coherent setting adds one controlled-F and
one Z_q, for 31 named operations and one additional selector qubit.

These are conditional source calls and specified register gates, not a
claim of 29 elementary two-qubit interactions. In a direct factorization
of all twelve U_rec/U_rec* calls there are, without cancellations,
24 conditional receiver calibrations and twelve instances of each source
factor C, M2, streaming, Gamma, pulse Q, pulse E and the scalar phase.
M2 itself is the product of two specified single-copy coins. A physical
implementation must also count the realization, routing and control of
each factor; a conditional whole-lattice unitary is not a free local gate.

For supplied upper durations tau_U, tau_Uinv, tau_L, tau_R, tau_J,
tau_T, tau_in and tau_good, a serial schedule has upper duration

```text
T_prep <=6tau_U+6tau_Uinv+3tau_L+6tau_R+3tau_J
         +3tau_T+tau_in+tau_good.                   (S11)
```

The optional coherent setting adds its two durations. These symbols must
be filled by an admitted control model before claiming a physical time.
The three subsequent original macrosteps are separate from preparation;
the inverse calls do not run a clock backward or get identified with that
later three-step readout time.

The explicitly supplied resources are the localized source basis state
u2, the arbitrary occupied memory/reference input, one ready qutrit, one
ready qubit, the exact loader and qutrit/attenuation calibration, both
reflections, and coherent controlled access to U_rec and its inverse with
their phases fixed. The optional setting needs one selector qubit. These
counts do not manufacture the readies from a Gibbs state, assign their
physical spectra, fund switching, or regenerate a consumed controller.

## 6. A complete-state perturbation budget

Suppose every implemented operation is a full-space unitary approximating
its named ideal operation in operator norm. Let the respective uniform
bounds be eps_U, eps_Uinv, eps_L, eps_R, eps_J, eps_T, eps_in, eps_good.
Unitary telescoping gives

```text
||W_tilde-W_prep||<=epsilon_gate,
epsilon_gate=6eps_U+6eps_Uinv+3eps_L+6eps_R+3eps_J
             +3eps_T+eps_in+eps_good.               (S12)
```

If the actual joint seed differs from the admitted seed/reference state
by trace distance zeta, the complete final state, with both auxiliaries
and every reference retained, differs from (S9) by at most
zeta+epsilon_gate. This follows from purification, the operator-norm
bound and trace-distance contraction. It is not only a marginal fidelity.
The coherent setting contributes the errors of its two additional gates.
For example, for G=29 named operations, seed error at most epsilon/2
and each gate error at most epsilon/(2G) suffice for total error epsilon.
Use G=31 when those setting gates are included.

The attenuation error can be stated without hiding its calibration:
if t=cos(theta), s=sin(theta), then changing theta to theta_tilde gives

```text
||T_tilde-T||=2|sin((theta_tilde-theta)/2)|
             <=|theta_tilde-theta|.
```

No numerical tolerance or manufacturing process is asserted here. The
formula provides a comparison once such errors have actually been bounded.
Conditional U_rec errors must include their controlled phase error.

No flag postselection is needed in the ideal circuit. If the actual
auxiliary-zero event is nevertheless read, its probability is at least
1-epsilon and the normalized complete accepted state is within epsilon
of the ideal target when the preceding joint error is epsilon. This uses
the accepted-plus-rejected instrument bound with ideal success probability
one, not a discarded failure branch in the construction.

After three exact common forward U_rec steps, the same state bound holds.
Any additional evolution error must be added. For the two phase settings,
receiver-probability contrast differs from its ideal value by at most
epsilon_++epsilon_-. The source result supplies ideal contrast greater
than 1/50, but a robust numerical margin requires retaining its exact
value or a stated rational margin; strict positivity alone does not
supply an arbitrary tolerance budget.

## 7. Optional finite-coordinate closure

This paragraph gives a finite register realization of the circuit's
mathematical domain. It is a computational closure, not a physical spatial
locality theorem and not a periodic-box spectral logarithm.

Each SELECT block moves any source coordinate by at most two. Although
its expanded schedule has four conditional calls, each qutrit sector
executes only its own two forward or inverse calls. The inverse SELECT
has the same bound. L, all reflections and the other small gates do not
move a coordinate. Across the three blocks, every actually reachable
component therefore satisfies

```text
|R-97|<=6,       |r|<=6,       |c-97|<=6,             (S13)
```

where c is the token or pulse coordinate. Inverses satisfy the same
finite-propagation bound. Intermediate receiver interactions are included.
The final target has coordinate displacement at most two; three further
forward steps have displacement at most five from the original seed.

Use fifteen coordinate values for each register: R,c in {90,...,104}
and r in {-7,...,7}. Replace streaming by cyclic shifts on these registers
and use the corresponding complete finite pulse-edge unitary. Keep the
same contact predicate r=0,R=c, the same phases and the receiver predicate
c>=100. This defines a complete finite unitary. Every visited coordinate
in (S13), including the needed forward/inverse one-step operations, stays
off the cyclic boundary, so the entire admitted circuit and the following
three-step readout agree exactly with the original infinite-space law.
The finite unitary is not equal to that law on arbitrary boundary inputs.

The valid coordinate/internal/auxiliary space has dimension

```text
15^3 *4 *3 *26^2 *3 *2 =164268000.                   (S14)
```

The internal factor 3 is token, pulse bank 1 or pulse bank 2. Three
four-qubit coordinate registers, two coin qubits, two arrangement qubits,
two five-qubit label registers, two qutrit-encoding qubits and b use
29 binary qubits, before any control workspace. Extend the valid-space
unitaries by identity on the unused binary codes; the resulting operators
remain complete unitaries. A controlled exact phase setting adds one bit.
This padding prescription is a raw-space extension, not a locality proof
for recognizing the valid sector.

Cyclic wrap edges are not local edges of the original integer lattice.
They can be replaced by an explicitly routed finite implementation or a
suitable unitary boundary rule, but their gate count and geometry must
then be supplied. Likewise, a source-basis reflection and a controlled
source call require actual control routing. The finite count (S14) does
not settle those physical interfaces.

## 8. Limits and falsifiers

The preparation is exact under its supplied-gate contract and the #1775
source identities. It does not obtain those gates from the original
six-pentit law, prove energy conservation during preparation, provide
thermal readiness, or select a physical spectral energy. The exact
attenuation and source-call phases are substantive assumptions. Memory
restoration at the endpoint does not imply that its intermediate
interaction, or the new controller, has no resource cost.

Decisive failures would include a wrong controlled scalar phase, omitting
the actual receiver from a source call, replacing the seed-subspace
reflection by an unknown-state reflection, failure of (S6), a hidden
postselection, uncounted inverse access, or a boundary interaction on an
admitted circuit prefix. Exact source preparation also does not prove
finite receiver retention, outcome selection or regeneration for a
further experiment. All review within this authoring session is distinct
from independent scientific acceptance.
