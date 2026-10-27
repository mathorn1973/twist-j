# A finite exact-energy source and a one-shot autonomous controller

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T;
independent mathematical acceptance pending.**
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1803](https://github.com/mathorn1973/twist-j/issues/1803).

This is an analytical construction. No scientific executable, numerical
experiment or finite enumeration is used. Its system is the complete
16-dimensional sector specified below, not the infinite spatial walk.
The energy reading, source preparation, coupling and endpoint time are
supplied definitions. The proof does not derive them from the native update.

## 1. Fixed system and target

Use the comparison model of
[#1793](https://github.com/mathorn1973/twist-j/blob/6f8e8e93a3b459695262c50c2ccbd120cdeb7e99/notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/PROOF.md)
at the displayed immutable revision. Let X,Y,Z be the Pauli matrices and
let the one-walk momenta be k in {0,pi/2,pi,3pi/2}. Define

```text
U2(k) = exp(ikZ)(I+2iX)/sqrt5,
H(k)  = sqrt5 (U2(k)^* - U2(k))/(2i)
      = -2 cos(k) X + sin(k) A0,
A0    = 2Y-Z,                         A0^2=5I.             (FCS-1)
```

There are two distinguishable walks, each already carrying its own
two-dimensional coin. On their total-momentum-pi sector S,

```text
S = direct-sum_k (|k,pi-k> tensor C^2 tensor C^2),
dim S = 16,
H0 = H tensor I + I tensor H,
P = |u><u| tensor I_4,
u = (1/2) sum_k |k,pi-k>,
V_g = exp(-igP) (U2 tensor U2),                    g real. (FCS-2)
```

The restriction of the position-coincidence projector to S is exactly P:
its momentum-pair matrix elements are all 1/4. The free walk and the
coincidence projector preserve total momentum, so V_g is a unitary on
this entire sector. No outgoing band or measurement outcome is selected.

At pairs (0,pi) and (pi,0), the one-spin energies are plus/minus2.
Each pair therefore contributes {4,0,0,-4}. At the other two pairs the
one-spin energies are plus/minussqrt5, giving {2sqrt5,0,0,-2sqrt5}.
Consequently

```text
E in {4,-4,2sqrt5,-2sqrt5,0},
rank Pi_E = {2,2,2,2,8},
H0 = sum_E E Pi_E,
H_S = H0 + 2sqrt5 I,                  0 <= H_S <= 4sqrt5 I. (FCS-3)
```

Here Pi_E denotes the complete spectral projector, including its full
degeneracy. The common positive offset changes no energy difference.
All following statements hold for any unitary V on S; the nominated
application takes V=V_g. General source compensation is inherited
background, not a claim of a new general principle.

## 2. Finite source and complete energy shells

Fix an integer M>=1 and put N=M+3. The source Hilbert space and energy are

```text
B_M = span{|m,n>: 0<=m,n<=N},
dim B_M = (M+4)^2,
H_B |m,n> = (4m+2sqrt5 n)|m,n>,
A = H_S tensor I + I tensor H_B.                          (FCS-4)
```

All source energies are nonnegative. Assign the integer vectors

```text
v_4=(1,0),    v_-4=(-1,0),
v_2sqrt5=(0,1),    v_-2sqrt5=(0,-1),    v_0=(0,0).          (FCS-5)
```

Thus E=4(v_E)_1+2sqrt5(v_E)_2. A vector with system energy E and
source coordinate z=(m,n) has total energy

```text
a_t = 2sqrt5 + 4t_1 + 2sqrt5 t_2,       t=z+v_E.           (FCS-6)
```

Distinct integer pairs t give distinct a_t, since sqrt5 is irrational.
For every t in the square

```text
G_M = {1,...,M+2}^2,
J_t psi = sum_E Pi_E psi tensor |t-v_E>,                  (FCS-7)
```

all coordinates on the right lie in the finite source box. Orthogonality
of the Pi_E gives J_t^* J_t=I_S. The range of J_t is the full eigenspace
of A at a_t: every admissible system energy has exactly the complementary
source coordinate t-v_E. Distinct ranges are orthogonal. Conversely, a
shell containing every system energy requires 1<=t_i<=N-1 for i=1,2,
by testing the positive and negative unit vectors in (FCS-5).

Let Q_M=sum_{t in G_M} J_t J_t^*. Define on the entire finite carrier

```text
Gamma_M(V) = sum_{t in G_M} J_t V J_t^* + (I-Q_M).         (FCS-8)
```

It acts as V on each complete shell and as the identity on all remaining
shells. The identity term includes every unprepared and boundary state.
There is no attempted out-of-range shift, projection or renormalization.
Block multiplication proves

```text
Gamma_M(V)^* = Gamma_M(V^*),
Gamma_M(V)^* Gamma_M(V) = Gamma_M(V) Gamma_M(V)^* = I,
[Gamma_M(V),A] = 0,
Gamma_M(V1) Gamma_M(V2) = Gamma_M(V1 V2).                  (FCS-9)
```

These are exact full-space identities. In particular the conserved
quantity is the original specified sine-energy account, with its fixed
offset, not a rounded energy. Write W_M=Gamma_M(V_g).

## 3. One coherent preparation for every input

Let theta=pi/(M+1). On one source coordinate define the real vector

```text
eta_M = sqrt(2/(M+1)) sum_{r=1}^M sin(r theta)|r+1>,
beta_M = eta_M tensor eta_M.                              (FCS-10)
```

The finite sine identity sum_{r=1}^M sin^2(r theta)=(M+1)/2 proves
normalization. Both occupied coordinates lie in {2,...,M+1}. For every
system energy and occupied source coordinate z, t=z+v_E belongs to G_M.
Therefore psi tensor beta_M lies entirely in Q_M for every psi in S,
without imposing any restriction on its energy components.

For the estimate only, extend eta_M by zero to ell^2(Z). Let T_a denote
translation by integer a. Its adjacent overlap is

```text
<eta_M,T_1 eta_M> = cos(theta),
delta_M = ||(T_1-I)eta_M||
        = ||(T_-1-I)eta_M||
        = 2 sin(pi/(2(M+1))) <= pi/(M+1).                (FCS-11)
```

Indeed, the sine recurrence eta_{j-1}+eta_{j+1}=2cos(theta)eta_j
holds on the occupied indices with zero Dirichlet endpoints. Multiplying
by eta_j and summing gives twice the adjacent overlap. Normalization
then gives the norm identity. No periodic boundary is used.

On the auxiliary bilateral space ell^2(Z^2), set T_v|z>=|z+v> and

```text
D = sum_E Pi_E tensor T_-v_E.                            (FCS-12)
```

This D is unitary. For each v_E in (FCS-5), a shift by v_E or -v_E
changes beta_M in norm by at most delta_M. Orthogonality of the system
spectral components therefore gives, for every unit vector psi,

```text
||(D-I)(psi tensor beta_M)|| <= delta_M,
||(D^*-I)(psi tensor beta_M)|| <= delta_M.                (FCS-13)
```

On these prepared vectors the actual finite operator Gamma_M(V)
agrees exactly with D(V tensor I)D^*. A matrix element taking system
energy E to E' shifts the source by v_E-v_E'. Its total label t is
unchanged and remains in G_M; the final source coordinate lies in
{0,...,M+3}^2. This proves the equality to the finite-shell definition
before any auxiliary-space norm estimate is applied.

Insert and subtract D(V psi tensor beta_M). The two differences are
controlled by (FCS-13), since D and V are unitary. Hence

```text
||Gamma_M(V)(psi tensor beta_M) - V psi tensor beta_M||
  <= e_M := 2 delta_M
   = 4 sin(pi/(2(M+1))) <= 2pi/(M+1).                   (FCS-14)
```

Every step holds with Pi_E and V tensored by the identity on an arbitrary
passive reference. The norm bound is thus uniform over all system/reference
vectors, not only uncorrelated inputs or energy eigenvectors.

Define the actual and ideal joint channels from S into S tensor B_M by

```text
E_M(rho) = W_M (rho tensor |beta_M><beta_M|) W_M^*,
F_M(rho) = V_g rho V_g^* tensor |beta_M><beta_M|.           (FCS-15)
```

The trace distance convention is D_tr(rho,sigma)=||rho-sigma||_1/2.
For pure states it is at most their vector distance. Purification and
partial trace extend (FCS-14) to every mixed system/reference input, so

```text
(1/2)||E_M-F_M||_diamond <= min{1,2 delta_M}.              (FCS-16)
```

Tracing out the source gives the same bound for the reduced contact.
This does not assert exact source return or absence of correlations:
the comparison retains both in the joint output.

For any finite word V_q...V_1 on this same S, first use the homomorphism
in (FCS-9), then apply (FCS-14) to its unitary product once. The same
bound applies without resetting or replacing beta_M between factors.
This algebraic composition result does not make the controller in
Section 5 execute that word or repeat one target automatically.

## 4. Explicit resources and their scope

Reflection of the sine probabilities about (M+3)/2 gives the exact
mean of each source coordinate. Thus

```text
dim B_M = (M+4)^2,
C_M := ||H_B|| = (4+2sqrt5)(M+3),
<H_B>_beta = C_M/2 = (2+sqrt5)(M+3),
Var_beta(H_B) <= C_M^2/4.                                (FCS-17)
```

The variance bound follows from the spectral interval [0,C_M]. All
quantities are finite for every M. For any chosen 0<epsilon<1, selecting

```text
M = max{1, ceil(2pi/epsilon)}                            (FCS-18)
```

is a conservative prescription implying e_M<epsilon. The full finite
source unitary exists exactly; only its comparison to the unassisted
target channel is approximate. These are sufficient resource bounds,
not optimal dimension, energy or preparation-work claims.

The pure packet (FCS-10), including its energy coherence, is a supplied
resource. Its preparation cannot be replaced by an energy-distribution
table. The source Hamiltonian is nondegenerate because 4m+2sqrt5 n
has distinct values at distinct integer pairs. The separate preparation
boundary is treated in the accompanying note; increasing stationary
capacity alone does not supply this packet.

The spectral projectors in (FCS-7) and their controlled couplings remain
declared operators. Finiteness of the box proves neither locality in the
original walk positions nor a preparation protocol for these operators.

## 5. A positive static one-shot controller

Fix tau>0, use units hbar=1, and add C=span{|0>,|1>}. Let

```text
R_tau = exp(i tau A) W_M,
X_R = R_tau tensor |1><0| + R_tau^* tensor |0><1|,
kappa = pi/(2tau),
H_tot = A tensor I_C + kappa(I-X_R).                     (FCS-19)
```

Equation (FCS-9) implies [R_tau,A]=0. Direct block multiplication gives
X_R=X_R^*, X_R^2=I, and [X_R,A tensor I_C]=0. Therefore

```text
0 <= H_tot <= B_bound I,
B_bound := 4sqrt5 + C_M + pi/tau,
[H_tot,A tensor I_C] = 0,
dim(S tensor B_M tensor C) = 32(M+4)^2.                  (FCS-20)
```

Here B_M denotes the source Hilbert space from (FCS-4), whereas B_bound
is a scalar norm bound. Positivity follows because A>=0 and I-X_R>=0.
All matrices are finite; no logarithm of W_M is needed.

Commutativity yields the full time-dependent identity

```text
exp(-itH_tot)
 = exp(-itA) exp(-ikappa t)
   [cos(kappa t) I + i sin(kappa t) X_R].                (FCS-21)
```

Tensor identities on C are suppressed only on exp(-itA). At t=tau,
exp(-ikappa tau)i sin(kappa tau)=1 and the cosine is zero. Thus, for
every joint system/source vector chi,

```text
exp(-i tau H_tot)(chi tensor |0>)
 = exp(-i tau A) R_tau chi tensor |1>
 = W_M chi tensor |1>.                                 (FCS-22)
```

The free phase is explicitly cancelled by the factor in R_tau. The
endpoint action is exact on the whole joint space, not only on beta_M.
For chi=psi tensor beta_M, (FCS-14) and (FCS-16) give the same uniform
joint-vector and channel error relative to V_g psi tensor beta_M tensor
|1>, including arbitrary references. The controller adds no endpoint
approximation error.

## 6. Complete energy, timing and recurrence

One possible decomposition is zero bare controller Hamiltonian and
interaction kappa I-kappa X_R. The constant is retained in the displayed
energy convention. In any initial density rho_SB tensor |0><0|,
the expectations of X_R and A X_R vanish because they are off-diagonal
in C. Using X_R^2=I gives exactly

```text
<H_tot>_in = <A>_rho + kappa,
Var_in(H_tot) = Var_rho(A) + kappa^2.                    (FCS-23)
```

For the supplied independent source input,
<A>=Tr(H_S rho_S)+C_M/2 and
Var(A)=Var_rho_S(H_S)+Var_beta(H_B). The same equations hold for the
system marginal of an input entangled with a passive reference.
Both full-energy moments are conserved during the autonomous evolution.
At the endpoint the controller is |1>, so the expectation of the
off-diagonal interaction -kappa X_R is again zero; (FCS-9) preserves the
distribution of A as well. Endpoint additive balance already follows
from (FCS-9), independently of this mean-interaction observation. The
interaction is not the zero operator at either endpoint. The constant
kappa is an energy offset in this convention, not a claimed thermodynamic
cost of manufacturing or preparing the apparatus.

Let B_bound=4sqrt5+C_M+pi/tau. The spectral theorem gives
||exp(-idH_tot)-I||<=B_bound |d|. Consequently a timing error d changes
the complete ideal-output comparison by at most

```text
joint vector error <= 2 delta_M + B_bound |d|,
joint trace distance <= min{1,2 delta_M+B_bound |d|}.     (FCS-24)
```

These bounds remain reference-uniform. The controller flag itself has,
for every normalized chi and all real t, the exact probability

```text
Pr(C=1 at t) = sin^2(kappa t).                          (FCS-25)
```

This follows from (FCS-21), since both chi and R_tau chi have norm one.
Thus the flag reaches one at tau but does not stay there. In particular

```text
exp(-i 2tau H_tot) = exp(-i 2tau A) tensor I_C.           (FCS-26)
```

It does not execute W_M twice. The interaction is always present; an
external read at tau or an additional retention mechanism is required
to use the endpoint as a lasting record. There is no exact self-stop,
tick train that repeatedly executes V_g, or free reset in this construction.

## 7. Attribution and physical boundary

The Public Canon v105 claim SELECTED-SPECTRAL-ENERGY-SOURCE already
supplies a continuous source with finite capacity and a uniform
reference-sensitive error. The general exact-channel obstruction and
the rounded finite-source lift are already in
[#1768](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/ENERGY.md)
and its FINITE_BATTERY.md. The present specialization uses the two exact
integer energy coordinates of this finite sector, so no rounding drift
is required. Its one-shot controller is a supplied implementation, not
a novelty claim for autonomous unitary dilation in general.

The finite rotor in
[#1795](https://github.com/mathorn1973/twist-j/blob/e4d165c5c5471ea5746013f7f8f5c394512f9884/notes/C-DIRAC-FINITE-ROTOR-CLOCK-N/PROOF.md)
concerns a different spatial target. Its repeated-step and spatial-range
claims are not imported into (FCS-19).

The present positive result is exact conservation of the specified
additive sine-energy account, a finite coherent source with controlled
joint error, and one positive static generator realizing the compensated
operation at a nominated time. The coupling is specified through the
target and its spectral projectors. Spatial locality, coherent source
preparation from a primitive law, self-stopping clocks and native-U
admission remain separate obligations. The coincidence-support boundary
in the accompanying note tests one precise local class, not all such
obligations.

A is a conserved account; H_tot is the generator of time evolution.
They are distinct operators. This construction does not identify their
physical roles, fix tau from A, choose omega over sin(omega), identify
an electron or any other species, calibrate an SI scale, or establish an
occurrence law. Its scope remains the declared finite L1 model.
