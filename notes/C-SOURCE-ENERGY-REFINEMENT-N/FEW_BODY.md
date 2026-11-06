# An exact positive lift with bounded interaction order

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`d69ff34274ffce191055df7fd44e092366e20819`.
Independent scientific acceptance is not asserted.

The positive finite energy from the predecessor need not remain one
interaction involving every occupation coordinate in its region. Its
complete action on the original active charge-ten code has an exact
positive extension whose Hermitian terms use at most ten occupation
coordinates, or twenty qubits in the stated finite representation.
No ancilla, clock, changed encoding or approximate effective dynamics
is used. The resulting terms can still connect widely separated sites.
Interaction order, geometric range and the number of terms are distinct.

## 1. Fixed original code and the finite target matrix

Take the original finite coordinate code and occupation isometry of
[PR1781 PHYSICAL_BLOCK.md](https://github.com/mathorn1973/twist-j/blob/5f7301e4d891596628cb25c6e735a7e4cd9004a8/notes/C-FINITE-OCCUPATION-ENERGY-N/PHYSICAL_BLOCK.md).
For L>=7 let

    d_code=8112(2L+1)^3,
    Lambda_L={97-2L,...,97+2L}.                       (F1)

The finite coordinate basis retains R,r,c, four object coins, three
carrier arrangements and all 26 carrier and receiver labels. The
receiver is fixed at physical site 100. Let h be any positive matrix on
this finite space, with

    0<=h<=b I,       b<=2pi E0.                      (F2)

The particular source-energy construction uses h=E0 q(U_L), with one
fixed positive Laurent polynomial q for both phase settings. The
theorem below is not restricted to that polynomial or its source pair.
It intertwines h on the entire finite code.

Index the coordinate basis by alpha=1,...,d_code. The original
phase-weighted occupation isometry has the form

    J|alpha>=exp(i theta_alpha)|occ_alpha>.          (F3)

The phase includes the original Gamma^(-1) D_2^* gauge. It is not
dropped or reinterpreted as a physical preparation resource.

Every occ_alpha has exactly five nonzero active occupation coordinates,
all equal to +1 or -1: two for the object, two for its token/pulse
carrier, and one for the receiver memory. Their physical positions lie
in Lambda_L. The two object constituents can occupy two sites, the
carrier one site, and the receiver site 100. Thus each basis ket uses
at most four spatial sites, one of which is always 100.

Write u=(x,a) for a physical site and active coordinate index. The
active indices are a in {1,...,16,25,...,37}; the other nine coordinates
at each site are identity spectators. Let S_alpha be the set of the
five nonzero active coordinates of occ_alpha, and let
s_alpha,u in {-1,+1} be their values. The active occupation charge is

    N_act=2 sum_active u h_u^2.                      (F4)

Every code ket has active charge ten. This charge counts the occupied
coordinates and is distinct from the target Hamiltonian energy h.

## 2. Five-coordinate annihilation maps

On the original raw occupation factors define the bounded operators

    A_alpha=exp(-i theta_alpha)
            product_(u in S_alpha) |0><s_alpha,u|_u, (F5)

with identity on every other coordinate. In particular there is no
vacuum projector on the unmentioned coordinates, the rest of a site,
onsite spectators or the outside region. Each A_alpha has norm one.
Its adjoint creates the complete gauged code ket from the active vacuum:

    A_alpha^*|vac>=J|alpha>.                         (F6)

Let P_10 be the projection onto total active charge ten, first with
identity spectators suppressed from the notation. Then

    A_alpha P_10=|vac><J alpha|.                     (F7)

To prove (F7), work in the raw occupation basis. A_alpha can be nonzero
only when all five coordinates in S_alpha have their specified signed
unit values. Those five coordinates already contribute charge ten.
Within P_10 every other active coordinate must therefore vanish. The
input is exactly occ_alpha, including its positions and labels. The
phase in (F5) gives the bra in (F7). This proves the identity on a basis
and hence on the entire charge-ten subspace. Invalid charge-ten states,
including states containing an occupation of absolute value two, cannot
evade this argument.

Tensoring (F7) with arbitrary onsite spectator and passive-reference
identities retains its total active-charge-ten qualification. There is
also a separate LOCAL identity: if J_Lambda is the finite-region code
map and xi_out is an arbitrary outside vector, then

    A_alpha (J_Lambda|beta> tensor xi_out)
       =delta_alpha,beta |vac_Lambda> tensor xi_out. (F7a)

Here the outside state can carry active charge; the global charge need
not be ten, and the vacuum in (F7a) is only the local active vacuum.
This identity follows from the local charge-ten code and the outside
identity factors in (F5), not from applying global P_10 to a charged
outside state. No occupied spectator or outside factor is projected
onto vacuum.

## 3. Positive full-space extension and exact intertwining

Define the finite row map into d_code copies of the raw space,

    R Psi=sum_alpha |alpha> tensor A_alpha Psi.

This row map is an algebraic proof factorization. Its copy index is not
a physical ancillary register and is not added to the Hamiltonian's
state space; the actual operator is the sum on the original factors in
(F9).

Its norm obeys

    R^*R=sum_alpha A_alpha^*A_alpha<=d_code I.        (F8)

The proposed physical Hamiltonian is

    H_few=R^*(h tensor I)R
         =sum_(alpha,beta) h_alpha,beta
                           A_alpha^*A_beta.         (F9)

This is a bounded self-adjoint operator on the complete raw occupation
space. Equations (F2) and (F8) prove

    0<=H_few<=d_code b I.                           (F10)

The positivity is a property of the whole sum. It does not require each
Hermitian summand below to be positive.

Using (F6)-(F7) gives the exact operator identity

    H_few P_10=J h J^*,
    H_few J=J h.                                   (F11)

Thus the finite original code is invariant, every invalid charge-ten
state outside it is annihilated, and the norm on that code is exactly
||h||. The entire original charge-ten sector has the same action as the
predecessor's one-block Hamiltonian, including zero action outside the
finite coordinate box. The extension on higher active-charge sectors
is different: several annihilation patterns can act on one raw input.
That action is explicitly (F9), remains positive, and is not claimed to
vanish. The active vacuum is annihilated by every A_alpha and has zero
Hamiltonian energy.

Separately, (F7a) gives

    H_few (J_Lambda tensor I_out)
       =(J_Lambda tensor I_out)(h tensor I_out).     (F11a)

This is the appropriate intertwining statement with arbitrary charged
outside factors. Equation (F11) itself uses the global original code
with active vacuum outside and the global charge projection P_10.

Every A_alpha lowers active charge by ten wherever it is nonzero.
Equivalently,

    exp(it N_act) A_alpha exp(-it N_act)
        =exp(-10it) A_alpha.

Each product A_alpha^*A_beta therefore commutes with all charge
unitaries and spectral projections. This proves strong charge
commutation of H_few, including on the unbounded integer occupation
space. Spectator and outside charges commute separately, since the
operator carries identities there.

Self-adjointness and (F11) make Ran J a reducing subspace. Consequently,
for every bounded Borel function F,

    F(H_few)J=J F(h).                               (F12)

This includes the complete continuous-time propagator and every energy
spectral indicator. All reference correlations are retained by the
identity extension. In particular, whenever the original phase pair has
identical complete h energy laws, it has exactly identical complete
H_few energy laws too. This is not only a mean-energy equality.

## 4. Explicit Hermitian summands and their support

Put T_alpha,beta=A_alpha^*A_beta. On the coordinate set
S_alpha union S_beta this is the single matrix unit

    T_alpha,beta=exp(i(theta_alpha-theta_beta))
       |occ_alpha restricted to the union>
       <occ_beta restricted to the union|,          (F13)

where a coordinate missing from one occupation pattern has value zero
in that pattern. Every other coordinate carries identity. Formula (F13)
follows by multiplying the local creation and annihilation factors in
(F5); it introduces no extra controls.

Write the Hamiltonian as

    H_few=sum_alpha h_alpha,alpha T_alpha,alpha
       +sum_(alpha<beta)
          [h_alpha,beta T_alpha,beta
            +conj(h_alpha,beta) T_beta,alpha].       (F14)

The diagonal term uses five occupation-coordinate factors and has norm
h_alpha,alpha. For alpha!=beta, the two occupation kets in (F13) are
orthogonal: their full patterns are distinct and all of their nonzero
coordinates occur in the union. The paired Hermitian summand therefore
has eigenvalues +|h_alpha,beta| and -|h_alpha,beta| on that two-state
subspace, zero on its local complement, and identity multiplicity on
the untouched factors. Its norm is exactly |h_alpha,beta|. Thus every
Hermitian term in (F14) has norm at most

    ||h||<=2pi E0.                                 (F15)

Each coordinate union has at most ten elements. Each spatial union has
at most seven sites: both original configurations use at most four
sites and share receiver site 100. The bounds per Hermitian term are
therefore

    at most 10 active occupation coordinates,
    at most 7 physical lattice sites.               (F16)

In the predecessor's four-level representation 0,+1,-1,2 of each
occupation coordinate, these are at most twenty encoded qubits. This
is the support of a complete matrix term, not a two-qubit gate circuit.
On the full integer occupation space, (F5) defines its bounded extension
directly. Values outside the four-level representation are handled by
the displayed rank-one factors when selected, and by identity when not
selected; there is no global truncation projector.

There are at most

    N_terms<=d_code(d_code+1)/2                       (F17)

Hermitian terms. Zero terms may be omitted. Every nonzero term in this
displayed decomposition touches receiver site 100, so that site's
incidence equals N_terms. In particular (F17) is a finite bound, not a
bounded-incidence claim. Other sites and coordinates have incidence at
most N_terms. No efficient storage, generation or calibration of these
matrix elements follows from their finite formula.

The spatial diameter of a term is at most 4L, since all its sites lie
in Lambda_L. It need not be close to zero or bounded independently of
L. The construction removes growing interaction ORDER, but does not
remove large geometric RANGE, large incidence, or the large total norm
bound (F10) on higher-charge raw sectors. The on-code norm remains b.

## 5. Application to the source-energy refinement

The companion [FEJER_RADIUS.md](FEJER_RADIUS.md) supplies the positive
finite energy matrix with

    L=47(2^35-1)+3.

Insert that matrix h and its exact original occupation isometry into
(F5)-(F9). Equation (F11) shows that this replacement adds ZERO error
to its energy-action and continuous-time comparisons with the original
Q, or to its receiver contrast. The prepared source vectors, all 26
old-memory labels and arbitrary passive references are unchanged. The
fresh-write conclusion keeps the original 25-label restriction on old
memory. No source is reselected after the interaction is decomposed.

The complete occupation inventory remains the companion's finite
region. No auxiliary register, pure ancilla, clock, spectral encoding,
boundary decoder or changed physical port is added. Exact energy-law
equality holds for the declared ideal Hamiltonian. Generic calibration
errors need not preserve that equality; the predecessor's comparison
budget is a bound on the COMPLETE generator perturbation. It must not
be assigned independently to every one of the potentially many terms
in (F14).

This is a different allowed raw completion of the same finite-code
law. The previous zero complement on all local higher-charge inputs is
not retained or needed by this contract. Positivity, charge, vacuum,
spectator identity and the entire admitted code law are retained exactly.
No thermal preparation, funded terminal detector, renewal, empirical
energy calibration or native six-pentit derivation is supplied.

## 6. Separate review obligations

1. Check the original occupation inventory: precisely five signed unit
   coordinates, active charge ten, at most four sites per basis ket,
   and the fixed receiver shared by every configuration.
2. Check the phases in (F3), (F5) and (F6), with the complete original
   Gamma^(-1) D_2^* gauge retained.
3. Check (F7) on the entire raw charge-ten subspace, including invalid
   occupations and original code states outside the finite box.
4. Check the Gram form, full-space positivity, norm bound, vacuum and
   explicitly different higher-charge completion in (F8)-(F11).
5. Check strong charge commutation and all spectator, outside and
   reference identity factors without a hidden vacuum projector.
6. Check exact code intertwining and Borel functional calculus, including
   the whole energy measures and complete time evolution in (F12).
7. Check the local matrix-unit formula, Hermitian pairing and exact
   per-term norm, without assuming positive individual summands.
8. Check the ten-coordinate, twenty-qubit and seven-site support bounds,
   term count, receiver incidence and potentially large spatial diameter.
9. Check the unchanged source comparison, zero added error and the
   distinction between a complete perturbation budget and a per-term
   allowance; preserve the remaining physical preparation/readout limits.

No scientific executable, matrix enumeration, numerical search or
simulation was run for this analytical construction. Same-session
authoring and adversarial checks are not independent acceptance.
