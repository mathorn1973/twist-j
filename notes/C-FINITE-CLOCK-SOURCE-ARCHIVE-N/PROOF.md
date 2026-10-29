# A common finite-horizon source, clock and record construction

2026-10-29. NON-CANONICAL, conditional analytical L1 proposal.
All statements below are mathematical constructions and estimates. No
scientific executable, numerical experiment or finite scan is used.
Set hbar=1. Operators are defined on their complete stated carriers.

## 1. Fixed finite system and active record process

Use the exact system of
[#1804, PROOF](https://github.com/mathorn1973/twist-j/blob/181b8b0dd98e0a697311fb83ab61493c94fd9e20/notes/C-DIRAC-FINITE-COHERENT-SOURCE-N/PROOF.md).
For k in {0,pi/2,pi,3pi/2}, with Pauli matrices X,Y,Z, define

```text
U2(k)=exp(ikZ)(I+2iX)/sqrt5,
H_sin(k)=sqrt5 (U2(k)^* - U2(k))/(2i)
        =-2cos(k)X+sin(k)(2Y-Z).
```

There are two distinguishable walks on the four-site ring. Their complete
total-momentum-pi sector is

```text
S=direct-sum_k |k,pi-k> tensor C^2 tensor C^2,   dim S=16.
```

On this space set H0=H_sin tensor I+I tensor H_sin,
u=(1/2)sum_k |k,pi-k>, P=|u><u| tensor I_4, and, for supplied real g,

```text
V_g=exp(-igP)(U2 tensor U2),
H_S=H0+2sqrt5 I,           0<=H_S<=4sqrt5 I.
```

The distinct unshifted energies E, and their complete spectral ranks, are
{4,-4,2sqrt5,-2sqrt5,0} and {2,2,2,2,8}. Write their projectors Pi_E.
The shift in H_S is retained in every total-energy formula.

For N>=1 add R_N=(C^5)^(tensor N), a bank of N active archive cells.
Assign this bank exactly zero energy in the account defined below. This
is a declared resource, not identification with any different original
record Hamiltonian. Let X_j add one modulo five in cell j.

Fix a complete five-projector partition {P_s:s=0,...,4} of S. One
fully specified choice is the following: order the momenta as above,
use the Z coin bases, index the resulting 16 basis vectors by
i=4k_index+2coin_1+coin_2, and group indices by i mod5. The ranks are
4,3,3,3,3. The partition is supplied; it is not selected by an occurrence
law or derived as a physical detector observable.

Define complete logical stages and prefixes on S tensor R_N:

```text
C_j=sum_(s=0)^4 P_s tensor X_j^s,
W_j=C_j (V_g tensor I_R),
G_0=I,              G_j=W_j ... W_1,       1<=j<=N.
```

Orthogonality and completeness of the P_s make every C_j unitary on
all archive states, including occupied cells. No state is erased or
discarded. W_j acts trivially on archive cells other than j.

For fresh cells initially |0>^N, the exact joint prefix is

```text
G_j(|psi> tensor |0>^N)
 =sum_(s_1,...,s_j)
   P_(s_j)V_g ... P_(s_1)V_g |psi>
   tensor |s_1,...,s_j,0,...,0>.
```

Thus the target is a coherent sequential record dilation. It is not
V_g^j on the unrecorded system alone: correlation with earlier cells
is retained and can affect later reduced system behavior. No selection
of one occurred history or uniform independent word law is inferred.

An already occupied older archive O may be included, jointly arbitrary
with S and a passive reference F. Every operator below carries I_O and
I_F. Its state and correlations are retained. New information goes into
the explicitly counted fresh bank; the old archive is not reset. The
analytic norm estimates actually hold for arbitrary initial R_N too;
fresh zeros are needed only for the displayed history interpretation.

## 2. One finite coherent source for the whole active archive

Fix M>=1 and B_M=span{|m,n>:0<=m,n<=M+3}. Define

```text
dim B_M=(M+4)^2,
H_B|m,n>=(4m+2sqrt5 n)|m,n>,
E_M=(H_S tensor I_R) tensor I_B + I_(S,R) tensor H_B.
```

The archive and the clock added later have zero terms in this particular
account. Its capacity is

```text
0<=E_M<=[4sqrt5+(4+2sqrt5)(M+3)]I.
```

Put v_4=(1,0), v_-4=(-1,0), v_2sqrt5=(0,1),
v_-2sqrt5=(0,-1), v_0=(0,0). For t in {1,...,M+2}^2 let

```text
J_t psi=sum_E (Pi_E tensor I_R)psi tensor |t-v_E>,
Q_comp=sum_t J_t J_t^*,
Gamma_M(Y)=sum_t J_t Y J_t^* + (I-Q_comp),
Kappa_M(K)=sum_t J_t K J_t^*.
```

Here Y is any unitary and K any Hermitian operator on S tensor R_N.
The J_t include the **entire active archive degeneracy**. The extension
is not an appeal to a theorem about a passive reference. Each J_t is an
isometry onto the complete E_M eigenspace with energy
2sqrt5+4t_1+2sqrt5 t_2. Distinct t have distinct energies. Every incomplete
shell is retained in I-Q_comp; boundary-coordinate states belonging to
complete shells are included in their J_t ranges.

Multiplication of these orthogonal blocks proves on the full finite space:

```text
Gamma_M(Y2)Gamma_M(Y1)=Gamma_M(Y2Y1),
Gamma_M(Y)^*=Gamma_M(Y^*),
[Gamma_M(Y),E_M]=0,
[Kappa_M(K),E_M]=0,
exp(-is Kappa_M(K))=Gamma_M(exp(-isK)),
||Kappa_M(K)||<=||K||.
```

The Hermitian lift is zero on the incomplete-shell complement, whose
exponential is identity. This is why the last exponential formula holds.

Prepare just once the normalized source

```text
eta_M=sqrt(2/(M+1)) sum_(r=1)^M sin(pi r/(M+1)) |r+1>,
beta_M=eta_M tensor eta_M.
```

This initial source is a product with S,R_N,O,F. Arbitrary initial
source correlations are not admitted to the comparison theorem.
The source can become correlated during the subsequent actual evolution.

For completeness, the error proof survives the active-archive extension.
Extend eta_M by zero to the bilateral integer lattice. Its unit shift
has overlap cos(pi/(M+1)), so

```text
delta_M=||(T_1-I)eta_M||=2sin(pi/(2(M+1))).
```

On the auxiliary bilateral source let
D=sum_E (Pi_E tensor I_R) tensor T_-v_E. Orthogonality of the full
extended projectors gives
||(D-I)(psi tensor beta_M)||<=delta_M and the same for D^*.
Every occupied source position has a complete shell. On the prepared
subspace the finite Gamma_M(Y) agrees exactly with D(Y tensor I)D^*;
all final coordinates lie inside the actual finite box. Inserting and
subtracting D(Y psi tensor beta_M) therefore proves

```text
||Gamma_M(Y)(psi tensor beta_M)-Y psi tensor beta_M||
 <= e_M :=2delta_M=4sin(pi/(2(M+1)))<=2pi/(M+1).
```

The estimate holds for every unit vector of S tensor R_N, for every
unitary Y on that whole space, and after tensoring an arbitrary reference.
Thus it is uniform in the archive dimension and input entanglement.

In particular, for each complete prefix,

```text
Gamma_M(W_j)...Gamma_M(W_1)=Gamma_M(G_j).
```

Apply the error bound once to Y=G_j and the original prepared source.
The bound remains e_M, with **no factor j or N and no intermediate
source reset**. Applying a product-input estimate separately after each
factor would be unnecessary and would ignore its actual correlations.

## 3. One finite-stage program and its complete pulse generators

Choose a tick interval tau>0. For each finite unitary W_j fix the spectral
phase convention W_j=sum_theta exp(-i theta) P_(j,theta), with
-pi<theta<=pi. In particular eigenvalue -1 is assigned theta=pi. Set

```text
K_j=sum_theta theta P_(j,theta),
Ktilde_j=Kappa_M(K_j),
K_j=K_j^*, ||K_j||<=pi,
exp(-iKtilde_j)=Gamma_M(W_j),   [Ktilde_j,E_M]=0.
```

This uses a finite spectral definition, not an analytic logarithm across
a branch cut. Since W_j acts identically on old/future archive cells,
its spectral function and its shell lift do likewise. These couplings
are supplied exact matrices. Their original-position locality or cost
of synthesis is not asserted.

Set the program period T=(N+2)tau and d=tau/3. For j=1,...,N put
b_j=(j-1)tau+tau/3. On the circle of length T define

```text
a_j(phi)=(2/d) sin^2(pi(phi-b_j)/d),  b_j<=phi<=b_j+d;
         0,                         otherwise.
A(phi)=sum_(j=1)^N a_j(phi) Ktilde_j.
```

The envelopes have area one, disjoint interiors and vanishing value
and first derivative at every endpoint. Thus A is periodic C^1 and

```text
||A(phi)||<=h=6pi/tau,
||A'(phi)||<=h1=18pi^2/tau^2,
[A(phi),E_M]=0.
```

It is zero before the first pulse, between stages, and throughout the
final extended idle region. The argument phi will be an internal clock
coordinate. No external switching is used in the actual construction.

## 4. Exact auxiliary suspension and read times

On the auxiliary circle clock let P_C=-i derivative_phi and
D_C=P_C+A(phi), with periodic Sobolev domain H^1. Since A is bounded
Hermitian and C^1, D_C is self-adjoint and Dom(D_C^2)=H^2.

Choose w=tau/12, phi_*=tau/12 and the normalized real packet

```text
f(phi)=sqrt(8/(3w)) sin^2(pi(phi-phi_*)/w)
       on [phi_*,phi_*+w], and zero elsewhere.
```

It belongs to H^2; f and its first derivative vanish at the support
endpoints. Its complete support lies in the initial idle region, and

```text
||f'||=8sqrt3 pi/tau,
||f''||=192sqrt3 pi^2/tau^2,
alpha=||f'||^2=192pi^2/tau^2.
```

The characteristic solution of (partial_t+partial_phi)Psi=-iA(phi)Psi
translates f and applies the chronological pulse product encountered by
each point of its support. Write T_t f(phi)=f(phi-t). At t=j tau,
0<=j<=N, every support point has passed exactly the first j pulses and
lies in the next idle region. No point wraps around the circle. Therefore

```text
exp(-ij tau D_C)(f tensor xi)
 =T_(j tau)f tensor Gamma_M(G_j)xi.
```

For **every** t in [N tau,(N+1)tau], no further pulse is encountered,
and the same identity holds with T_t f and Gamma_M(G_N). Here xi is
any joint system/archive/source vector, not only a prepared source input.
The target is constant throughout this final interval except for the
explicit translated clock. This is an uninterrupted evolution statement,
not a claim about measurements made at all prefixes in the same run.

The auxiliary first-order generator is not the actual positive finite
Hamiltonian. It is used to prove the comparison below.

## 5. Positive rotor and uniform orbit estimate

Put Omega=2pi/T. Choose an integer ell>=1, Lambda=ell Omega, and the
periodic boost G_ell f(phi)=exp(iLambda phi)f(phi). Define

```text
H_Lambda=P_C^2/(2Lambda)+A(phi)+hI,
c_Lambda=Lambda/2+h,
C_f=||f''||+2h||f'||+h1+h^2
   =(288sqrt3+54)pi^2/tau^2.
```

H_Lambda is self-adjoint on H^2 and H_Lambda>=P_C^2/(2Lambda)>=0.
Its gauge transform is

```text
G_ell^* H_Lambda G_ell=c_Lambda I+D_C+P_C^2/(2Lambda).
```

For Phi_0=f tensor xi with ||xi||=1, A vanishes near its support,
so D_C Phi_0=-if' tensor xi and D_C^2 Phi_0=-f'' tensor xi.
The exact identity

```text
P_C^2=D_C^2-2A D_C+i A'+A^2
```

on H^2, together with conservation of the two D_C graph norms, gives

```text
||P_C^2 exp(-itD_C)Phi_0||<=C_f
```

for all real t, uniformly in xi and any reference. Duhamel on H^2 then
proves the positive-rotor comparison error at elapsed time t>=0 is at
most t C_f/(2Lambda). The perturbation is not assumed bounded on the
entire auxiliary circle space; it is bounded on this exact graph-norm
orbit as displayed.

Let Phi=G_ell f tensor xi. Its uncompressed rotor energy is

```text
E_rot=Lambda/2+h+alpha/(2Lambda),
C_E=sqrt(2Lambda E_rot)=sqrt(Lambda^2+2hLambda+alpha).
```

These quantities are independent of xi. Positivity and conservation of
H_Lambda give ||P_C exp(-itH_Lambda)Phi||<=C_E at every real time.
These are auxiliary uncompressed moments; they are not silently assigned
to the actual finite clock packet below.

## 6. The actual finite clock, phase and compression estimate

For an integer L>=0 let Q_L retain the Fourier modes e_m with |m|<=L,
where e_m(phi)=T^(-1/2)exp(imOmega phi). Set

```text
p_cut=Omega(L+1),
p0=||Q_L G_ell f||,
f_L=Q_L G_ell f/p0,
H=Q_L H_Lambda Q_L
```

on C_L tensor S tensor R_N tensor B_M, dim C_L=2L+1. The choices in
Section 8 ensure p0>0. The complete finite matrix is

```text
H=diag_(-L<=m<=L)((Omega m)^2/(2Lambda)) tensor I
  +sum_(j=1)^N A_j^(L) tensor Ktilde_j +hI,
(A_j^(L))_(mn)=(1/T)integral_0^T a_j(phi)exp(i(n-m)Omega phi)dphi.
```

It is bounded, self-adjoint and positive on the whole finite carrier:

```text
0<=H<=B_H I,       B_H=(Omega L)^2/(2Lambda)+2h.
```

All its coefficients are fixed before evolution. The initial clock is
the single packet f_L. Its translated comparison packet is

```text
chi_t=Q_L G_ell T_t f/p0.
```

It is normalized for every t because
Q_L G_ell T_t f=exp(iLambda t)T_t Q_L G_ell f. This identity fixes the
phase convention: the ideal joint vector below contains
exp(-it c_Lambda)chi_t. Replacing chi_t by T_t f_L requires the
additional phase exp(iLambda t); it cannot be dropped when times are
coherently controlled. No such controlled-time experiment is claimed here.

For u(t)=exp(-itH_Lambda)Phi, the discarded Fourier tail obeys
||(I-Q_L)u(t)||<=C_E/p_cut. The kinetic part and scalar shift commute
with Q_L. Consequently, if v(t)=exp(-itH)Q_L Phi, Duhamel for the
retained component gives

```text
||v(t)-Q_L u(t)||<=t h C_E/p_cut.
```

At a nominated tick or final-window time, the projected auxiliary
target is exactly p0 chi_t tensor Gamma_M(G_j)xi, with j=N throughout
the final window. Combining the rotor and compression estimates and
dividing by p0 yields

```text
||exp(-itH)(f_L tensor xi)
  -exp(-it c_Lambda)chi_t tensor Gamma_M(G_j)xi||
 <= eta(t):=[t C_f/(2Lambda)+t h C_E/p_cut]/p0.
```

Both compared states lie in the retained space. No separate final-tail
term is needed; projection and normalization have already been included.
The bound is uniform in the entire joint xi and arbitrary references.
Moreover p0>=sqrt(1-C_E^2/p_cut^2) when p_cut>C_E.

## 7. One joint theorem, including the source and archive

Take xi=psi tensor beta_M, with arbitrary normalized psi on S tensor R_N
and any retained old archive/reference. First compare the exact H
evolution with Gamma_M(G_j) using Section 6, then compare that whole
prefix once with G_j using Section 2. The triangle inequality gives

```text
||exp(-itH)(f_L tensor psi tensor beta_M)
 -exp(-it c_Lambda)chi_t tensor (G_j psi) tensor beta_M||
 <= eta(t)+e_M.
```

This holds at every t=j tau, 0<=j<=N, and at every
t in [N tau,(N+1)tau] with j=N, for the **same apparatus and initial
state**. All clock/source correlations remain in the actual vector
being compared. There is no source replacement, clock reset, intermediate
measurement, or postselected success condition.

Purification and partial trace give, for the complete joint output channel,

```text
half-diamond-distance <= min(1,eta(t)+e_M).
```

The same upper bound applies to trace distance, with convention one half
of the trace norm, on every retained subsystem and reference. In
particular the complete history target of Section 1, its old-record
correlations and its final-window channel all satisfy this bound.

In the ideal programmed prefix, later stages act identically on already
written cells. Their joint reduced record is unchanged, including a
passive reference, by unitary evolution on its complement. The actual
finite-clock process is compared to that complete ideal prefix/window
by the displayed error; exact continuous preservation between all ticks
is not asserted. The old archive O is untouched exactly because the
entire physical generator carries I_O. Correlations with the evolving
system are retained, not declared to be a product.

## 8. Explicit finite choices and resources

Given N>=1, tau>0 and 0<epsilon<1, choose positive epsilon_s,epsilon_c
with epsilon_s+epsilon_c<=epsilon. Set

```text
M=max(1,ceil(2pi/epsilon_s)),
T_h=(N+1)tau,
ell=max(1,ceil(2T_h C_f/(Omega epsilon_c))),
Lambda=ell Omega,
p_req=max(2C_E,4T_h h C_E/epsilon_c),
L=max(0,ceil(p_req/Omega)).
```

These choices are finite and noncircular: C_f and Omega precede ell;
C_E follows Lambda; then L is chosen. They imply e_M<epsilon_s,
p_cut>=2C_E, p0>=sqrt3/2>1/2, and for every 0<=t<=T_h,

```text
eta(t)<=2[T_h C_f/(2Lambda)+T_h h C_E/p_cut]
       <=epsilon_c.
```

Thus the stated joint error is at most epsilon at all declared ticks
and throughout the final window. The complete active carrier dimension is

```text
dim H_active =16 * 5^N * (M+4)^2 * (2L+1).
```

A supplied old archive of dimension d_O multiplies this by d_O. A
passive mathematical reference is not counted as manufactured apparatus.
The raw archive has all 5^N states; no padding or unprepared sector is
discarded. Full source boundary shells and all finite clock modes are
part of H. The formula is a sufficient construction, not an optimum.

## 9. Two conserved operators and the preparation account

Every Ktilde_j commutes with E_M. The clock kinetic term, cutoff and
scalar shift do also. Therefore on the complete finite space

```text
[H,I_C tensor E_M]=0.
```

This is exact at every real time, not just at readout. The full
distribution of the declared additive sine-energy account is conserved.
The total positive generator H is also conserved by its own evolution.
They are distinct operators. In particular E_M has not been silently
added as another term of H: doing so would introduce an additional
exp(-itE_M) in the target and require a new phase account.

Put C_B=(4+2sqrt5)(M+3). In the prepared product source,

```text
<H_B>_beta=C_B/2,              Var_beta(H_B)<=C_B^2/4,
<E_M>=Tr(H_S rho_S)+C_B/2,
Var(E_M)=Var_(rho_S)(H_S)+Var_beta(H_B).
```

These equalities allow arbitrary system/archive/reference correlations;
only the initial source is independent. For the actual finite generator
one has 0<=<H><=B_H and Var(H)<=B_H^2/4. Its initial packet has Fourier
tails in the programmed region, so the uncompressed idle-packet moments
from Section 5 are not substituted as exact finite-clock moments.

The coherent beta_M, coherent f_L, clean new archive cells and exact
couplings are supplied. Their manufacture or replenishment is not funded
by this theorem. In particular the stationary thermal preparation of
another model cannot be relabeled as a source of beta_M coherence.
There is no claim of thermodynamic work cost, dissipation, a thermal
success probability, or reset of all used resources.

## 10. Locality, return and physical boundary

All factors here are finite, but the shell projectors and K_j are
spectrally defined. No original-position finite-range bound is inherited
from the different single-walk system of #1795. No claim of support only
at a coincidence point is made; the strict coincidence-support
obstruction of #1804 is not contradicted.

The stage clock continues to evolve during the final hold window.
The reading statement compares the full joint state throughout that
window, not a permanently stopped flag. After the window, periodic
program repetition and finite-dimensional recurrence are outside the
contract and can act on the existing archive. A larger N or smaller
error changes the apparatus. No single finite apparatus for an arbitrary
fresh infinite record stream has been constructed.

The logical archive partition and initial readiness are supplied. The
construction does not identify its recorded symbols with the 26-state
original capture instrument in #1774, derive a probability of one
occurred event, establish the original lattice preparation, identify
H with a nominated physical sine-energy operator, fix tau from that
account, or realize the apparatus under the original six-pentit U.

Its achieved conjunction is specific: one finite static positive
generator, a counted finite source with exact additive conservation,
a genuine active record process, reference-uniform finite-prefix
accuracy, and a nonzero final reading window under one preparation.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
