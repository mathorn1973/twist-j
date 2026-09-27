# Native counter to Hodge-event addresses

Status: PUBLIC NON-CANONICAL.
Ceiling: candidate-T written consequences of registered T inputs and one selected
NON-CANONICAL Hodge-event target; candidate-C finite audit.
Owner: issue #1243. Author: A. M. Thorn <thorn@twistj.com>.
Prospective pin: 6ad742a24fa821c16a27a929e38927007a44cf31.

No Canon status is asserted here.

## 1. Source and target types

Let

    Omega=N_0 x F5^6,
    U(n,x)=(n+1,d_n x)

be the declared native carrier and update. On the origin-zero reachable domain

    D={(n,x):x in X_n}

use the registered conserved labels

    ell_n:X_n -> F5^5,
    ell_(n+1)(d_n x)=ell_n(x).

Every ell_n is onto. At n=0 its 3125 fibres each contain exactly five native
heads, one from each initial trace phase. For n>=3 the reachable current slice
X_n itself has exactly 3125 checkpoints, one per label.

Fix independently one integer event resolution h>=3 from
C-HODGE-EVENT-CAUCHY-N. Its selected event mesh is

    Gamma_h={e_h(m,z):m in Z, z in Z^3}.

The inherited proof says e_h is injective, equal-m distinct z are spacelike,
and e_h(m,z),e_h(m+1,z) are future timelike. Hence

    slice(e_h(m,z))=m,
    spatial(e_h(m,z))=z,
    T_h(e_h(m,z))=e_h(m+1,z)

are well defined and T_h is a bijection.

Nothing here identifies Gamma_h as the uniquely physical event carrier. It is
a stipulated target for the classification.

## 2. Complete reachable clock-aligned bridge class

A reachable clock-aligned point bridge is a total map B:D->Gamma_h satisfying

    B(n+1,d_n x)=T_h B(n,x),                         (1)
    slice(B(n,x))=n.                                  (2)

The registered arbitrary-target theorem applies with Y=Gamma_h and L=T_h.
Thus every solution of (1), before imposing (2), is uniquely

    B(n,x)=T_h^n A(ell_n(x))                          (3)

for arbitrary A:F5^5->Gamma_h.

Write uniquely A(lambda)=e_h(m_lambda,z_lambda). Equation (2) at n=0 gives
m_lambda=0 for every label lambda. Conversely this condition makes (2) hold
for every n. Therefore A is precisely an arbitrary spatial assignment
G:F5^5->Z^3 and

    B_G(n,x)=e_h(n,G(ell_n(x))).                      (4)

This proves the complete class, not one favored construction.

The counter in (4) is the first coordinate of the declared native state Omega.
No external clock or future input has been added.

## 3. A faithful finite worldline bundle exists

Represent F5 coordinates by 0,1,2,3,4 and define

    G0(a,b,c,d,e)=(a+5b,c+5d,e).                      (5)

Its inverse is quotient and remainder modulo five. Hence G0 is a bijection

    F5^5 -> {0,...,24} x {0,...,24} x {0,...,4},

whose target contains exactly 3125 sites.

Call a bridge faithful when G is injective. For every faithful bridge and every
native counter n, distinct retained labels have distinct z and hence lie at
distinct points of one inherited spacelike slice; each retained label has a
future-timelike successor; and exactly 3125 retained labels/worldlines occur.

The five initial native heads in one ell_0 fibre necessarily share the same
event worldline because (4) depends on them only through ell_0. Faithfulness
is to the retained 3125-label quotient, not to all 15625 initial heads.

## 4. The native counter is necessary

Suppose an address reader ignored the native counter and were a fixed map
F:F5^6->Gamma_h. Its range is finite, so the set of slice values of F is finite.
Exact alignment slice(F(x))=n on a nonempty reachable state at every
n in N_0 would require that finite set to contain every natural number, a
contradiction.

Thus the unbounded native counter cannot be eliminated from an exact
clock-aligned point bridge. This does not make its metric interpretation
automatic.

## 5. Exact intertwining does not select the target

The theorem used above quantifies over every stipulated set Y and every
bijection L:Y->Y. Its proof uses only the native retained label and invertible
target update. It never uses a metric, Hodge operator, dimension, cone or event
spacing.

Consequently existence of an exact reader satisfying R U=L R is target-blind
at this contract. Choosing Y=Gamma_h does not derive Hodge spacetime from U.
Choosing h is also external: every h>=3 supplies another admissible stipulated
target.

At fixed h, equation (4) leaves G completely arbitrary. Native intertwining
therefore selects neither the spatial placement of the 3125 retained labels
nor their pairwise distances.

This is a nonselection theorem for the declared reader class. It is not a claim
that arbitrary targets are physically equivalent. Additional metric-sensitive
source structure may narrow the class, but it is not present in this contract.

For the same reason this criterion cannot by itself choose E+ over a future
separately stipulated Galois-conjugate event system. No physical Galois
equivalence is inferred.

## 6. Additive spatial naturality gives only the zero map

Suppose the spatial assignment is an additive homomorphism

    G:F5^5 -> Z^3.

For every v,

    5G(v)=G(5v)=G(0)=0.

Z^3 is torsion-free, so G(v)=0 for every v. The same proof works for any
additive target without 5-torsion.

Thus no faithful point bridge can preserve the native chart addition as a
linear/additive characteristic-zero spatial coordinate map. Any faithful
address must use a nonlinear/integer-lift rule such as (5), or additional
structure with a different algebraic contract.

This is not an objection to nonlinear decoding.

## 7. Point readers cannot generate a complete spatial slice

For every n>=3, the reachable current slice X_n contains exactly 3125 states.
A single-valued point bridge therefore emits at most 3125 event addresses at
that native time.

But one marked Hodge-event slice is

    Gamma_h(m)={e_h(m,z):z in Z^3},

which is infinite because e_h is injective. Hence no point reader on the
reachable current state can cover a complete spatial slice.

If each current checkpoint emits at most c addresses, the union at one time
contains at most 3125c events. The marked cube

    C_R={e_h(m,z): |z_1|,|z_2|,|z_3|<=R}

has exactly

    |C_R|=(2R+1)^3

points. Covering it requires

    c >= ceil((2R+1)^3/3125).                          (6)

The right side is unbounded with R. No fixed finite output budget per current
state generates all spatial scales.

Therefore a decoder that emits complete unbounded spatial geometry must change
type. It needs, for example, an unbounded/generative geometric output, an
accumulated history/log, or another carrier. The theorem does not decide which
mechanism is physical.

This is the main architectural distinction:

    state -> one event

can provide event identity/worldline addresses, but cannot by itself be the
full geometry decoder.

## 8. Whole-Omega separable control

The registered whole-Omega theorem classifies readers only in the separable
form

    R(n,x)=L^n F(x).

For L=T_h, exact intertwining is equivalent to F=g(Q(x)) for arbitrary g on
the thirteen sign-quotient classes Q.

Clock alignment forces every g(Q) to lie on event slice zero. Thus every
whole-Omega separable clock-aligned event bridge has one arbitrary initial
event assignment per Q class and at most thirteen independently placed
worldlines.

This is complete only for that registered separable class. Arbitrary
nonseparable readers on whole Omega remain outside scope.

## 9. Clock alignment is not metric calibration

Equation (4) identifies native counter n with integer event-slice label m. It
does not identify one event-mesh segment with METRO-TICK=2pi/5.

In the inherited selected geometry, same-site mesh segments have ideal proper
length sqrt(ct)/h plus a bounded rounding correction. Resolution h remains an
input. No SI scale or exact equality with METRO-TICK is supplied.

The positive result is an address/causal-order bridge, not a completed
clock-metric bridge.

## 10. Status

- complete reachable clock-aligned bridge classification: candidate-T;
- faithful 3125-worldline construction and causal-slice corollary: candidate-T
  conditional on the selected Hodge event target;
- counter necessity: candidate-T;
- target/resolution nonselection: candidate-T at the exact reader contract;
- additive zero theorem: inherited T specialized here, candidate-T corollary;
- point/bounded-batch spatial-capacity obstruction: candidate-T;
- whole-Omega separable thirteen-worldline control: candidate-T corollary;
- finite exact executable checks: candidate-C corroboration;
- native derivation of full spatial geometry, physical E+ selection, metric
  calibration, occurrence law, photon and curved spacetime: OPEN / unchanged.
