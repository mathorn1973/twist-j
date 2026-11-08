# Spectral energy: an additive-contact obstruction and a compensated interface

**NON-CANONICAL, L1. Analytical candidate; independent acceptance pending.**
Author: A. M. Thorn. License: Apache-2.0. Public reservation: #1767.

## 1. Scope and fixed inputs

This note concerns the actual bounded spectral energy of the object, rather
than an occupation count assigned to a finite simulator. It proves that no
carrier-only energy makes the unchanged contact conserve an additive
object-plus-carrier energy. It then separates three possible responses:
including an interaction term, restricting the input contract, and adding an
explicit compensating battery. The battery construction below has finite
energy capacity but an infinite-dimensional continuous carrier. It is not a
finite local implementation of the apparatus in #1766.

Fixed scientific inputs are:

- Public Canon v105, `mathorn1973/twist-j` main
  `892a0b11089d34e241e1eb76d2c03247022d18e6`, especially the definitions in
  `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md`,
  Sections 1 and 5.3, and `PROOF_CURRENT_RECORD_INTERFACE.md`, Section 2.
- The complete forward filter #1746 at
  `01acc42b78f75095587765e9a5b91ee70dc28f37`,
  `notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md`, Sections 1, 3 and 7.
- The changed apparatus #1766 at
  `d978a455ef01506a9b8eb68c296e6ca89703710a`. Its endpoint and resource
  accounting are not silently identified with the original object's energy.

All claims here are conditional mathematical statements on their declared
carriers. No derivation from the original native update is required or
asserted. No occurrence law, material implementation, new Canon status or
independent review is supplied.

The source uses the dimensionless bounded operator

    H_W = i Log_(3*pi/10) W,             W = exp(-i H_W),
    spec(H_W) subset [-3*pi/10, 17*pi/10].                 (1)

For a chosen positive energy scale E0 one may use E0*H_W as an energy
observable. Its conversion to an empirically calibrated energy is a separate
contract. Additive scalar offsets do not affect any commutator below.

## 2. Exact contact obstruction, including any carrier-only energy

Let the object space have coordinates (R,r) and coin basis e1,...,e4, and let
the complete one-carrier space include both token and pulse arrangements,
positions, banks and labels. Define

    A = (e1-e4)/sqrt(2),             B = (e2-e3)/sqrt(2),
    a_s = |R=s,r=0,iB>,             b_s = |R=s,r=0,A>,
    alpha = a_s tensor |token at s,j>,
    beta  = b_s tensor |pulse at s,bank 1,j>.

The source contact C acts as identity off its contact ports and satisfies

    C alpha = (3/5) alpha + (4/5) beta.                    (2)

The source object step is W=Gamma*S*M2, with M2*A=A and M2*B=B.
The shifts of coin coordinates 1,...,4 are respectively
(-1,0),(0,-1),(0,1),(1,0) in (R,r). Consequently

    W a_s = i (|s,-1,e2> - |s,1,e3>)/sqrt(2),
    W b_s = z_g (|s-1,0,e1> - |s+1,0,e4>)/sqrt(2).        (3)

The first vector has r != 0 throughout; the second has r=0 throughout.
They are normalized and orthogonal. In particular C acts identically on
W*a_s tensor v for every carrier vector v, regardless of its position,
arrangement or label.

**Proposition E1.** For every unitary R_car on the entire carrier space,

    || [W tensor R_car, C] alpha ||^2 = 4/5.              (4)

Indeed, using (2) and the preceding identity,

    [W tensor R_car,C] alpha
      = -(2/5) W*a_s tensor R_car|token at s,j>
        +(4/5) W*b_s tensor R_car|pulse at s,bank 1,j>.

The two terms are orthogonal by their object r supports, even when R_car
mixes arrangements. Their squared norms add to 4/25+16/25=4/5.
No assumption that C fixes W*b_s tensor v is needed or made.

**Corollary E1a.** No self-adjoint carrier-only H_car makes the unchanged C
strongly commute with the additive energy

    Q_add = E0*H_W tensor I + I tensor H_car.             (5)

If it did, it would commute with exp(-i Q_add/E0). Strong commutation of
the tensor factors gives exp(-i Q_add/E0)=W tensor exp(-i H_car/E0), in
contradiction with (4). This argument also covers unbounded H_car when
strong commutation is the conservation contract. For bounded H_car it is
the ordinary operator commutator statement.

Thus an arbitrary reassignment of energy to the carrier alone cannot make
the unchanged instantaneous contact conserve (5). Adding an interaction
energy, or replacing C tensor I by a jointly compensated operation on an
extra system, changes the contract and is not excluded. Merely appending a
spectator does not evade E1. Neither is an interacting scattering energy
that agrees with the
additive energy only asymptotically. The witness is an operator-level failure
of conservation; it does not assert a nonzero change of mean energy for
every individual input state.

## 3. The filter preserves a distribution; the older scattering result has a window

In #1746 every fine-history object coefficient K_eta is a polynomial in the
commuting unitaries W and T_R. They are normal, commute with H_W, and the
complete set obeys sum_eta K_eta^* K_eta=I. For every bounded Borel f,

    sum_eta K_eta^* f(H_W) K_eta = f(H_W).                (6)

Taking f to be a spectral-set indicator proves preservation of the complete
spectral distribution before conditioning. The statement holds with an
arbitrary reference and with fine histories retained. Conditioning on an
accepted subset reweights that distribution. Equation (6) does not preserve
all energy coherences, identify the accepted channel with sqrt(G), or include
the source preparation and capture contact.

There is a separate existing positive energy statement: the canonical
scattering operator commutes with the additive reference energy on the
declared channel sector inside

    J_safe = (5*pi/4, 7*pi/4).

There the spectrum has no 2*pi aliases. This is an asymptotic scattering
statement on that sector. The compact source in #1746 explicitly does not
lie in the old safe spectral window in general. Neither (6) nor the
safe-window theorem extends the latter energy identification to the whole
compact source, its finite capture segment, or the new Hamiltonian compiler.
This is a scope boundary, not a contradiction with the canonical theorem.

## 4. Exact full unitary channels require an explicit escape from additive conservation

The following general statement applies to bounded energy observables, not
just finite-dimensional systems.

**Proposition E2.** Let Q be bounded self-adjoint on a system S, let B_A be
a bounded self-adjoint apparatus energy, and prepare one fixed apparatus state
sigma_A independently of the arbitrary system input. Let V be a joint unitary
commuting with Q tensor I + I tensor B_A. Suppose that for every system state
(equivalently for arbitrary system/reference inputs) its reduced channel is
exactly rho -> U rho U^*. Then [U,Q]=0.

To prove the assertion, purify sigma_A by a passive reference E. An exact
unitary channel has a constant complementary channel: the Stinespring
isometry is U tensor |xi> for one fixed final AE vector. Explicitly, a pure
system input has a pure output U|psi>, so its full output factors; applying
linearity to superpositions of any two input vectors makes the other factor
independent of the input. Therefore the final apparatus marginal sigma'_A
is fixed. Conservation of the additive energy for every rho gives

    U^* Q U - Q = c I,
    c = Tr(B_A sigma_A) - Tr(B_A sigma'_A).               (7)

The spectra of U^*QU and Q are identical and bounded. Equality (7) would
translate their finite spectral supremum by c, forcing c=0. This proves E2.
The same proof extends to an unbounded B_A if the required input and output
means exist and additive conservation justifies the displayed balance.

Applied to U=C and Q=E0*H_W tensor I_car, E1 excludes all exact universal
implementations meeting E2's hypotheses. The result is stronger than a
finite-dimensional apparatus restriction, and does not require apparatus
reset. A final apparatus state independent of the input is already forced
by the exact full-system unitary channel.

This is not a no-go theorem for the restricted logical-input contract in
#1766. That construction fixes the physical preparation, retains other
degrees of freedom and proves an approximate accepted logical channel.
The hypotheses of E2 are not that contract. Useful escapes include a
restricted system input family, approximation with residual apparatus
correlations, or interaction energy at the comparison boundaries. The next
section explicitly constructs the approximation escape while conserving the
actual chosen system energy plus a battery energy.

## 5. A bounded-capacity continuous battery on the actual system carrier

Let Q be any bounded system energy. Subtract its spectral infimum and choose
a finite Delta with

    0 <= Q <= Delta I.

Let U be any specified unitary on that same system Hilbert space, without
compressing the system to a finite position box. Choose L>2*Delta and define

    H_B = L^2([0,L],db),              (B eta)(b)=b eta(b),
    K = Q tensor I + I tensor B.                         (8)

B has finite capacity L and a continuous spectrum. Its Hilbert dimension
is infinite. The following construction counts that resource explicitly.

The spectral decomposition by the total energy lambda in [0,L+Delta]
identifies S tensor B with a direct integral whose system fiber is

    H_lambda = Ran 1_[max(0,lambda-L), min(Delta,lambda)](Q).

This follows by the spectral change of variables lambda=q+b; it can also be
defined by extending battery wavefunctions by zero to the full real line and
then applying the spectral controlled translation of b by q. On the whole
interval Delta <= lambda <= L the fiber equals the full system space. Define
the decomposable unitary

    Gamma_L(U)(lambda) = U                 if Delta <= lambda <= L,
                        identity on H_lambda otherwise.               (9)

The definition is unitary on every raw total-energy fiber, including the
boundary fibers. It strongly commutes with K. It is not a partial isometry
that silently discards a failed battery shift. Also, for any two system
unitaries,

    Gamma_L(U) Gamma_L(V) = Gamma_L(UV)                  (10)

on the entire joint space: inside the interval the fiber is the usual
product, and outside it both factors are identity. The good total-energy
interval is invariant. A finite word therefore has the same compensation
law as its full product; one need not sum one approximation error per gate.

Prepare a normalized battery wavefunction eta supported in [Delta,L-Delta].
Every system input then has total energy in [Delta,L]. On this input (9)
agrees exactly with the full-real-line compensated lift. In a generalized
system energy matrix element q -> q', that lift shifts the battery by q-q'.
Thus the battery pays each system energy change without altering the total
energy.

For an explicit error estimate put w=L-2*Delta and prepare

    eta(b) = sqrt(2/w) sin(pi*(b-Delta)/w)  for Delta <= b <= L-Delta,
             0                            otherwise.                 (11)

Its zero extension belongs to H^1(R), has norm one, and satisfies
||eta'||_2=pi/w. Let Q_c=Q-(Delta/2)I. On the full-line auxiliary space let
T_x eta(b)=eta(b-x), let P=-i d/db, and put

    S_c = exp(i Q_c tensor P).

The full-line lift is S_c (U tensor I) S_c^*: its energy-kernel translation
is q-q', unchanged by centering Q. The bound

    ||(T_x-I)eta||_2 <= |x| ||eta'||_2

follows by integrating the derivative, or from the spectral theorem for P.
Since ||Q_c||<=Delta/2, the spectral theorem for Q_c gives, uniformly in
every normalized system/reference vector psi,

    ||(S_c-I)(psi tensor eta)|| <= (Delta/2)||eta'||_2,
    ||(S_c^*-I)(psi tensor eta)|| <= (Delta/2)||eta'||_2.

Inserting U tensor I between these two comparisons proves

    ||Gamma_L(U)(psi tensor eta) - (U psi) tensor eta||
        <= pi*Delta/(L-2*Delta) =: e_B.                 (12)

The two intermediate full-line vectors are used only to prove the estimate;
the actual unitary (9) acts throughout on the finite interval. The initial
support property makes its action exactly the full-line action being
estimated. No self-adjoint momentum on the bounded interval is assumed.

For D(rho,sigma)=(1/2)||rho-sigma||_1, the same bound, capped at 1, holds
after partial trace and for arbitrary mixed system/reference inputs by
purification. It therefore bounds half the diamond distance of the induced
system channel from U's channel. Equation (12) does not claim exact battery
return. The exact compensated output contains the correlations required by
E2; their joint distance from a returned battery is bounded as displayed.

For the actual contact choose the unchanged system S=object tensor carrier,
U=C and Q=E0*(H_W+(3*pi/10)I) tensor I_car. Equation (1) permits
Delta=2*pi*E0. Equations (8)-(12) then give a concrete energy-conserving
approximate contact interface on the actual object carrier. The construction
does not assign the carrier kinetic energy; one may instead choose any
specified bounded total system energy Q and apply the same theorem.

The battery mean in (11) is L/2 by reflection symmetry. Its entire spectrum
and energy variance are bounded, with Var(B)<=L^2/4. The width, purity and
energy coherence in (11), its preparation, the continuous dimension, and
the controlled coupling in (9) are supplied resources. Choosing
L>=2*Delta+pi*Delta/e makes the bound at most a chosen e>0. This is an
energy-capacity estimate, not a preparation cost or a thermodynamic efficiency.

For a common subsequent acceptance instrument, the unconditional joint
trace-distance bound e_B gives |p_actual-p_ideal|<=e_B. If p_ideal>=p0>e_B,
then p_actual>=p0-e_B and the normalized accepted-state distance is at most
e_B/p0, including the reference and every retained output register. To see
this, complete the instrument by a rejected scalar flag. Contractivity gives
||sigma_actual-sigma_ideal||_1+|p_actual-p_ideal|<=2*e_B for its accepted
subnormalized outputs. Normalizing and using the ideal denominator bounds
the conditional trace distance by e_B/p_ideal<=e_B/p0. This states the
conditioning cost explicitly. It does not replace the predecessor's
independent preparation and spectral errors.

## 6. A static generator with the free phase explicitly included

The commuting unitary (9) alone is a channel construction, not a clock or a
claim that the bare K itself executes U. Here is a separate abstract static
generator on the same continuous carrier that realizes the comparison at a
specified time t_*>0, including its free phase.

Define the bounded system unitary

    U_* = exp(i Q t_*/hbar) U,
    V_* = Gamma_L(U_*),
    A_* = i Log(V_*),                         ||A_*||<=pi,

using a bounded Borel logarithm with exp(-i A_*)=V_*. Functional calculus
gives [A_*,K]=0. Define

    H_full = K + (hbar/t_*) A_* + (pi*hbar/t_*) I.        (13)

It is bounded self-adjoint and satisfies
0<=H_full<=(Delta+L+2*pi*hbar/t_*)I. Its exact evolution at t_* is

    exp(-i H_full t_*/hbar)
       = - exp(-i K t_*/hbar) V_*.                      (14)

Applying (12) to U_* and then the free unitary gives, up to the irrelevant
global sign, a joint-state approximation with the same error e_B to

    U psi tensor exp(-i B t_*/hbar) eta.                 (15)

Thus the free object phase cancels; it is not silently omitted. The bare
energy K and the complete energy H_full both commute with this evolution.
The interaction contribution (hbar/t_*)A_* is an actual term in the latter
energy account, with norm at most pi*hbar/t_*. It is not zero at the endpoints.
For the supplied product input rho tensor |eta><eta|, the full initial
mean is Tr(Q rho)+L/2+(hbar/t_*)Tr(A_*(rho tensor |eta><eta|))
+pi*hbar/t_*. The bounded complete spectrum gives
Var(H_full)<=(Delta+L+2*pi*hbar/t_*)^2/4, with no omitted interaction term.
The construction does not identify H_full with the additive K, switch the
interaction off, supply an internal clock that announces t_*, or prove
spatial locality. Its specification contains the full target operator U.
It is a conditional, bounded-energy existence interface with a continuous
battery, not a replacement for the finite local compiler and its clock proof.

## 7. What a history invariant does and does not establish

Consider a standard open-chain history propagation with nonzero edge weights
and edge operators |t+1><t| tensor U_(t+1), their adjoints, and scalar
clock-diagonal terms. For a fixed data observable Q,

    [H_prop, I_clock tensor Q]=0
      iff [U_(t+1),Q]=0 on every edge.                  (16)

The necessity follows by taking the separate (t+1,t) clock matrix blocks;
distinct edges cannot cancel. The sufficiency is immediate. Thus a final
product commuting with Q does not suffice. The word X,X on a qubit has
product I, but each X fails to commute with Q=|1><1|.

There is always a different, clock-dependent observable. Let
V_0=I, V_t=U_t...U_1 and define

    Q_hist = sum_t |t><t| tensor V_t Q V_t^*.

Then U_(t+1) Q_t=Q_(t+1) U_(t+1), so [H_prop,Q_hist]=0.
This is an exact invariant. To interpret it as a physical energy requires a
separate demonstration of its spatial support, relation to the prescribed
object/carrier energies, and interaction terms. Its existence by conjugation
does not establish those properties. Compensated gates such as (9) preserve
a fixed extended energy K instead, but their continuous resource and coupling
must be retained when comparing them with a finite local compiler.

## 8. An exact finite-carrier obstruction for the compact object input

One cannot preserve the full actual spectral-energy dynamics by quietly
replacing its compact initial state by a finite-dimensional carrier.
Let a_s be the object vector from Section 2. For every n>=1, W^n*a_s has
the component

    <R=s,r=-n,e2 | W^n a_s> = i/(sqrt(2)*5^(n-1)).       (17)

After the first step the r=-1 component is i*e2/sqrt(2). To reach r=-n
in n steps requires the shift -1 at every step, hence the e2 output at
every step. Subsequent e2-to-e2 coin entries are 1/5 and Gamma is identity
at every visited r<0. This proves (17) without enumerating a circuit.
Every W^k*a_s with k<n has r>=-k>-n. Therefore the vectors

    a_s, W a_s, W^2 a_s, ...

are linearly independent, by taking the outermost nonzero r component in
any finite linear combination.

**Proposition E3.** No finite-dimensional invariant exact simulation can
intertwine W on the entire cyclic subspace generated by a_s. In particular
no exact intertwiner of H_W on that cyclic subspace into a finite-dimensional
self-adjoint energy can exist, since functional calculus would also
intertwine W=exp(-iH_W) and all its powers.

This does not exclude the finite spatial margins used for a finite word in
#1746 or #1766. Those realize a specified finite computation on its reachable
support. E3 concerns an exact energy intertwiner for the complete cyclic
object dynamics. Quantitative approximate spectral-energy matching on a
declared finite input family remains possible and requires its own bound.

## 9. Decisive failure conditions and remaining interfaces

This analytical candidate fails at its named scope if any of the following
occurs:

- The source definitions do not give (3), or a carrier-only unitary makes
  the two terms in (4) fail to have the stated orthogonal object supports.
- An implementation satisfying every hypothesis of E2 gives an exact
  universal unitary U with [U,Q]!=0, or the constant-complement argument
  fails under the stated bounded-energy assumptions.
- The direct-integral fibers, raw boundary unitary, initial support or
  controlled translations in (8)-(12) are ill-defined, or a normalized
  system/reference input violates (12).
- The static generator (13) is not self-adjoint/nonnegative, fails to
  conserve K, or leaves an uncancelled object free phase in (15).
- The outermost coefficient (17) vanishes or is reached by a shorter power,
  invalidating the claimed infinite-dimensional cyclic subspace.

The result supplies a concrete obstruction to an unchanged additive contact
and an explicit compensated interface when a coherent continuous battery
and nonlocal coupling are admitted. Closing the finite local apparatus bridge
still requires a quantitatively controlled implementation on the actual
spectral-energy carrier, with its preparation, locality, dimensions,
interaction-energy boundary and accepted-error amplification all included.
No scientific executable, simulation or expanded circuit was run for these
proofs. Same-session derivation and review are not independent acceptance.
