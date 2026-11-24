# Moving integer string endpoints: an exact construction and a bridge boundary

NON-CANONICAL. Conditional candidate-T, pending independent review.
Reservation #1410. Author: A. M. Thorn. Date: 2026-10-07.
This is a new comparison model, not native U, an electron, a magnetic
monopole identification, or a continuation of the old photon energy.

## 1. Question and all changed premises

The question is whether a fixed lattice of integer variables can support
an exactly translating localized charge value without an independent
particle-position register. The previous wave/polarization model does not
supply that: its homogeneous bound charge has a pointwise oscillator law
and its Gauss defect is pointwise conserved. Its subsequently proposed
same-energy one-edge exchange is resonant and fails the dense marked-field
continuity test. Those results are not revised here.

Public basis: mathorn1973/twist-j main
7d7f588c42422c2cf37b04d76ebc13ca55eb96dc, Public Canon v100.
The predecessor wave has PR #1405 head
393354eaa6ff8afc84d624c06995c3c087f679cd; the bound matter comparison has
PR #1407 head 1144fa12012856c61e93ea95b61bb0e28dd97ee2.
The separate mobility candidate, reservation #1408, already exists at
52bdadc8987c7caa0cd52c22bb28f5baa4b96fad and is not duplicated or edited.

Here change BOTH the carrier and the energy. Let the graph be D3 with
primitive basis b1=(1,1,0), b2=(1,0,1), b3=(0,1,1), b0=0, and all six
translated directed edge types b_j-b_i for i<j. G is head-minus-tail
incidence. Work on the infinite graph or on primitive periodic quotients
with first period even and all periods at least two. Keep edge labels,
including distinct labels that acquire the same endpoints on a quotient.
No edge is a self-loop in the quoted finite domains.

The complete state is a link field

    f in B^Edges,                 B={-2,-1,0,1,2} subset Z.

Arithmetic is ordinary integer arithmetic, NOT mod 5. Selecting the
balanced five-state alphabet is an additional premise; its size does not
prove that J selects it. Define the mathematical endpoint charge and energy

    n=G^T f,                     H_def(f)=sum_z n_z^2.       (1)

The sum is finite on a finite quotient or a state with finite charge support.
The charge is computed from links; it is not a separately updated label.
On a finite quotient, sum_z n_z=0. At each vertex |n_z|<=24.
The neutral zero field is a comparison background, not a physical plenum
or a claimed state of the electromagnetic field.

H_def is a NEW selected nonnegative energy. Its unit is not an electron
mass or a photon quantum. Closed flux cycles have zero energy. No action,
Coulomb potential, physical gauge symmetry, or electromagnetic field
identification is inferred from (1).

Action-layer boundary: the selected graph is L2 input; the finite-alphabet
map below is L1 comparison mathematics. NOTE-D3-STRING-ENDPOINT-READING
names only an unadopted comparison to L5 charge/current histories. It is
not a registered or passed layer gate.

## 2. The energy fixes the only possible nonidentity one-edge change

Fix a directed edge e:a->b. Change only f_e by delta in Z. Then

    n_a'=n_a-delta,               n_b'=n_b+delta,
    H_def'-H_def=2delta(delta-d), d=n_a-n_b.                (2)

There are no zero divisors in Z, so an energy-preserving change has
exactly the alternatives delta=0 or delta=d. The nonidentity change,
when allowed by the alphabet, exchanges the entire endpoint charge values.

Select the maximal such contact: perform delta=d whenever f_e+d is in B;
otherwise perform delta=0. All other links remain fixed. Denote it R_e.
The choice to execute an admitted nonidentity branch is itself part of the
model; energy conservation alone also allows refusing it.

For an active contact, d'=-d and f_e'+d'=f_e belongs to B. It is therefore
active in reverse. For a rejected contact the state is unchanged. Thus

    R_e^2=identity,    H_def(R_e f)=H_def(f)                (3)

on EVERY state. The full multiset of n values is conserved. The integrated
oriented current is j=-delta e, with

    n'-n=-G^T j.                                         (4)

The local charge-energy values n_a^2 and n_b^2 are exchanged. Their changes
are n_b^2-n_a^2 and its negative. This is exact local energy transport, not
an additional work-account variable. It supplies no kinetic energy or
work against a separate electromagnetic force.

R_e depends only on the links incident to a or b. Contacts on an edge
matching commute: changing one matching edge alters n only at its two
endpoints, disjoint from all other matching endpoints. Distinct incident
but unmodified links do not invalidate this argument.

## 3. One fixed autonomous schedule, with its anisotropy disclosed

In primitive coordinates x=(x1,x2,x3), let M_0 apply R_e on all edges
x->x+b1 with x1 even, and let M_1 apply it on those with x1 odd.
Each layer is an edge matching. Set, with rightmost map acting first,

    T=M_1 M_0,                  T^-1=M_0 M_1.             (5)

This is one fixed local reversible map on the entire link-state space.
On infinite configurations the two layers are defined pointwise by their
finite dependency neighbourhoods. No future path or sequence of selected
particle locations is supplied. One full update includes both layers.
Using individual half-steps as ticks instead would require retaining the
matching-phase bit; that is not hidden in the physical time interpretation.

This schedule is one-axis and period-two. It commutes with translations by
2b1, b2, and b3. Translation by b1 exchanges the layers and gives

    tau_b1 T tau_b1^-1=T^-1,                              (6)

not full one-site spatial covariance of T. The selected direction, sublattice
origin, and update order are architecture. No isotropic 3D motion or
Lorentz/physical-speed claim follows.

## 4. Exact all-time translation of a finite string

Fix one row x=r+kb1, with primitive r1=0. Let f^(a,b) put value +1 on
its b1 edges k=a,...,b-1, and zero on every other edge of the 3D graph.
For a<b its only charges are

    n_(r+ab1)=-1,  n_(r+bb1)=+1,   H_def=2.               (7)

If a,b are both even and b-a>=2, layer M_0 removes the leftmost occupied
edge and fills the first empty edge after the right endpoint. These two
edges are disjoint and both changes lie in B. All other candidate edges
have equal endpoint charges and delta=0. The result is f^(a+1,b+1).
M_1 repeats the operation, giving f^(a+2,b+2).

If a,b are both odd, M_0 instead fills the edge immediately before the
left endpoint and removes the rightmost occupied edge. The endpoints
move to a-1,b-1; M_1 repeats. Therefore

    T^m f^(a,b)=tau_(2m b1) f^(a,b)    if a,b even,
    T^m f^(a,b)=tau_(-2m b1) f^(a,b)   if a,b odd           (8)

for every integer m, including negative m by (5). This is equality of
ALL link values, not just a moving maximum of a selected readout.
The charge support, string shape, and its energy are transported exactly.
On an even periodic row the same proof applies to cyclic intervals of
even length strictly between zero and the period, including across wrap.

Example: the two-link string from primitive 0 to (2,0,0) has charges
-1 at 0 and +1 at (2,0,0). One full update moves them to (2,0,0) and
(4,0,0). At every intermediate contact and every later update H_def=2.
Initial data, not the sign of charge, determine the selected chirality
through the sublattice. The speed is fixed by the schedule; this is not
an inertial mass/velocity relation.

The endpoints have no confining energy in (1): any simple signed unit
path, with no repeated edge, has charges -1,+1 only at its endpoints
and H_def=2 independently of its length. It need not be one of the
ballistic states in (8). Absence of a length cost alone does not establish
dynamical mobility in every background, a Coulomb force, or a binding law.
An even finite straight string is a translating neutral pair, not one
isolated charged particle or a dynamically bound proton/neutron model.

## 5. A single moving endpoint needs its field tail

On one infinite row, put f=+1 on b1 edges k<a and zero elsewhere. Each
vertex sees finite incident data. There is exactly one charge +1 at a,
and H_def=1. The string is half-infinite; no global finite-flux sum is used.
The same boundary-edge proof gives

    T^m f=tau_(2m b1)f  for a even,
    T^m f=tau_(-2m b1)f for a odd.                        (9)

The semi-infinite configuration with f=+1 on k>=a similarly has charge
-1 and the same parity-dependent translation. Charge is localized, while
the complete field has a tail to infinity. Thus this does not violate the
zero-total-charge identity on finite-support states or a closed torus.
It does not establish finite energy for the PREDECESSOR electromagnetic
reading; it has finite energy only for the new H_def.

For nonzero finite-support charges on a closed graph, H_def is an even
positive integer and at least two: n^2=n mod 2 and sum n=0. Equation (7)
attains two. On the one-tail domain H_def=1 is attained. These are selected
energy gaps, not derived charge units, rest masses, or Planck's relation.

## 6. The string environment matters: equal charges can move differently

Let a=0, b=b1, c=b2, p=-b1. Prepare f=+1 on p->a only. Then n_p=-1,
n_a=+1, n_b=0. The contact e:a->b has f_e=0,d=1 and transports +1 to b.

Now add twice the oriented triangle circulation a->b->c->a. In stored
orientations this adds +2 on a->b, +2 on b->c (type b2-b1), and -2 on
a->c. All new links still lie in B. The circulation has zero divergence,
so the COMPLETE charge profile and H_def are identical to the first state.
But now f_e=2 and f_e+d=3 is forbidden. R_e is the identity.

Consequently n by itself is not an autonomous complete state description.
The actual link configuration can allow or obstruct the same endpoint hop.
This witness is local and works in the infinite graph and on the audited
quotients, with the labelled edges retained. It is not a force law.

## 7. Why this does not evade the earlier obstruction or finish the photon

The old continuity theorem concerned dense Z[phi] amplitudes, their old
quadratic energy, and changes of just one old electric coordinate. This
item changes the state space and energy. B is discrete in the marked real
metric, and a finite-neighbourhood map on B^Edges is continuous in its
product topology. The arbitrarily small s^m perturbations of the old proof
are not admitted here. This is a change of premises, not a refutation.

The multiset of n is conserved by every R_e and hence by T. From n=0 no
charged pair can be created. In fact all zero-charge configurations are
pointwise fixed, since every d=0. The neutral sector has no dynamics at all
under (5); zero-energy closed loops are not propagating photons.

For the simplest proposed identification with the old wave, set A=x=v=0
and E=f. Its old doubled energy is F_wave=sum_e f_e^2. A unit string with
L edges has F_wave=L, whereas H_def=2. Thus the naive combined expression

    H_def+kappa F_wave = 2+kappa L,     kappa>0            (10)

has a positive string-length cost. Extending an endpoint by one previously
empty edge, holding the other endpoint fixed, changes F_wave by +1 and
H_def by zero. Such an R_e is NOT a conservative operation of (10).
This is one explicit failed gluing, not a theorem about every possible
joint energy, Coulomb dressing, or quantum string-net phase. The rigid pair
translation (8) keeps L fixed and happens to keep this particular F_wave,
but that does not repair the all-state failure or yield separated charges.

Using the whole old wave rule after T is also unproved and generally does
not preserve the bounded alphabet. No claim of common photon/matter
intertwining, radiation, work on a moving carrier, or energy exchange with
the prior field is made. Nothing is inferred for electron/proton/neutron
spin, statistics, rest energy, stability, or nuclear structure.

## 8. What has and has not been selected

Energy conservation derives the two possible one-link moves in (2), not
the alphabet, H_def, permission to execute a nonidentity move, schedule,
background, or physical interpretation. The full state contains no separate
position/velocity marker, but the chosen schedule visibly programs a
chirality into the spatial sublattice. We do not call that inertial motion.

The construction supplies a literal all-time mobile charged endpoint in an
integer link system, with exact inverse/current/energy and a boundary tail
when necessary. It supplies a mechanism and a sharply stated failed bridge,
not a physical elementary particle. The next joint-law question must preserve
neutral positive-energy transverse field motion while allowing such charged
endpoint motion and accounting for its work. Simply adding the old electric
energy term is insufficient by (10).

Methodological primary context, not black-box premises of this proof:
- M. Levin and X.-G. Wen, Phys. Rev. B 73, 035122 (2006),
  DOI 10.1103/PhysRevB.73.035122; arXiv:hep-th/0507118.
- C. Castelnovo, R. Moessner and S. L. Sondhi, Nature 451, 42-45 (2008),
  DOI 10.1038/nature06433; arXiv:0710.5515.
Their quantum/condensed-matter mechanisms are not proved equivalent to (5).
Original text and code: Apache-2.0. No independent review is claimed.
