# Mobile charge: the bound-charge obstruction and a resonant defect continuation

NON-CANONICAL. Conditional candidate-T, pending independent review.
Analytical proof. No public acceptance or independent review is claimed.
Finite audit status, if any, is recorded separately in RESULT.md.
Source and selection boundaries are fixed in CONTRACT.md.

## 1. The old homogeneous charge does not propagate

Let R=Z[phi], s=2-phi. Then s^2=3s-1 and 0<s<1/2 in the marked
embedding. Let G be the vertex-to-edge incidence, C the triangle
circulation, P=C^T C. In particular G^T P=0.

First keep the PREDECESSOR rule exactly, with L=I and Gamma=sI:

    x'=x+v,
    E'=E-sPA-sv,
    A'=A+E',
    v'=v-sx'+sE'.                                           (1)

Define vertex arrays

    rho=-s G^T x,       Q=G^T(E+s x),       w=G^T v,
    b=s+s^2=4s-1.

Taking divergences in (1), without projecting or approximating, gives

    Q'=Q,
    rho'=rho-s w,
    w'=(1-b)w+(1+s)rho+sQ.                                  (2)

Indeed G^T E=Q+rho, and G^T E'=G^T E-s w. Eliminating w yields

    rho[n+2]=(2-b)rho[n+1]-rho[n]-s^2 Q
            =(3-4s)rho[n+1]-rho[n]-s^2 Q.                    (3)

This is a POINTWISE equation at each vertex. There is no spatial operator
on its right side. On a finite quotient it holds at every vertex, for all
states, including nonzero Q. On the infinite graph it holds pointwise as
well; no convergence assumption is needed for this local identity.

Consequently the charge support at every n>=0 is contained in

    supp rho[0] union supp rho[1] union supp Q.               (4)

In the Q=0 sector the whole charge history lies in the at-most-two-
dimensional linear span of its first two spatial profiles. A point with
rho[0]=rho[1]=Q=0 cannot acquire this charge later. This excludes sustained
transport of a nonzero compact charge profile to arbitrarily distant sites
by (1). It does NOT exclude oscillating charge exchange within that fixed
support, transport of neutral energy, or other charge readings.

For a temporal mode with Q=0 and nonzero rho, its multiplier z must satisfy

    z^2-(3-4s)z+1=0,
    4 sin^2(omega/2)=b.                                     (5)

This frequency is independent of momentum. Equivalently, in the homogeneous
spatial decomposition every positive-stiffness P eigenvector is annihilated
by G^T, so its associated (A,E,x,v) modes have rho=0. Propagating polariton
branches are not transported free charge in this reading. Inhomogeneous
L is not covered by (3); its bound supports are a different specified model.

This supplies the precise reason not to identify the previously established
material current with freely transported particle charge. Continuity alone
was insufficient.

## 2. A separate field-defect carrier, with its new premise visible

Return to the predecessor EMPTY-material field carrier (A,E) in R^N x R^N.
Its free wave and doubled field energy are

    W(A,E)=(A+E-sPA, E-sPA),
    F(A,E)=E^T E+s A^T P(A-E).                               (6)

The inverse is A=A'-E', E=E'+sP(A'-E'). Direct expansion proves F W=F.
W preserves G^T E pointwise. Now make a NEW, unadopted interpretation:

    rho_f=G^T E                                               (7)

is candidate free charge, including its nonzero sector. This is not the
old rho=-sG^T x. A nonzero Gauss defect of an old source-free interpretation
has not secretly become an accepted physical particle. The source sector
and interpretation in (7) must be admitted independently for a physical use.
No extra charge label or assigned particle position is stored here.

At an oriented edge e:u->v, hold A and every other E component fixed.
Writing E_e'=E_e+delta changes only

    rho_f(u)'=rho_f(u)-delta,
    rho_f(v)'=rho_f(v)+delta.                                (8)

To exchange those two charge values, the unique possible increment is

    delta=rho_f(u)-rho_f(v).                                 (9)

The exact field-energy cost is

    F(A,E+delta e)-F(A,E)
      =delta [2E_e-s(PA)_e+delta].                            (10)

Equation (10) is polynomial arithmetic in R and uses P=P^T. The ring has
no zero divisors. Thus a nontrivial charge exchange with no other state
change is energy conserving if and only if the bracket in (10) is zero.
This is a classification in a specified local class, not a selection of
that class from J.

## 3. A complete conservative hop, not a prescribed current

Define H_e by the following exact rule:

    delta=rho_f(u)-rho_f(v),
    g=2E_e-s(PA)_e+delta;
    if g=0: E_e'=E_e+delta; otherwise: E_e'=E_e.
    All other entries, including A, are unchanged.           (11)

Testing g=0 means equality of both integer coefficients, not a tolerance.
For an executed hop delta'=-delta and g'=g. Thus applying H_e twice returns
every state, including rejected cases. H_e is a total local involution,
with no division, rounding, erasure or auxiliary energy account.
It conserves F and exchanges exact endpoint charge values. In particular,
when one endpoint is charged and the other neutral, the same nonzero charge
moves to a formerly neutral vertex, with the requisite field change.
The actual current of this contact is j_e=-delta e; (8) is precisely
rho_f'-rho_f=-G^T j_e. No future path is an input.

Gates on edges with disjoint endpoints commute. Their predicates share A,
which is fixed, and only use their respective endpoint divergences and their
own E entries. Changing another disjoint edge affects none of these data.
Their product is therefore the same whether evaluated simultaneously from
the pre-layer state or sequentially in any order.

For an explicit autonomous finite-range schedule, use primitive D3
coordinates, b0=0,b1=e1,b2=e2,b3=e3, with the fixed physical embedding
b1=(1,1,0), b2=(1,0,1), b3=(0,1,1). Edge types ij in order
01,02,03,12,13,23 have displacement d=bj-bi. Let i(d) be the index of its first nonzero
primitive coordinate, whose value is +1 or -1. Split all tails by the parity
of their i(d)-th coordinate. Each of the resulting twelve edge classes is a
matching. This works on the infinite graph and on tori with all side
lengths even, retaining the predecessor's labelled parallel edges.

Include c in Z/12 in the COMPLETE state, and set

    T(A,E,c)=(W H_c(A,E), c+1).                              (12)

Here H_c is the corresponding matching product. The inverse decrements c,
applies W^-1, then H_c. This is an all-state integer-coefficient bijection.
The twelve-state schedule is an explicit extra resource, not native U.
It chooses a staggered ordering, not a derived rotational symmetry.

Every step conserves F and the entire multiset of charge values on a finite
quotient. W does not move charge; H_c permutes the values. On an infinite
lattice with finitely many charged sites the same finite multiset is
preserved. A hop can annihilate neither a charge value nor its sign.
The complete current is assembled from actual executed contacts; the free
wave adds only the divergence-free increment -sPA. Charge continuity holds
at every step. The source-free sector rho_f=0 is invariant and each H_c
is the identity there, so its field history is EXACTLY the old free wave.

The marked energy is nonnegative because

    F=s|C(A-E/2)|^2+E^T(I-sP/4)E
      >=s|C(A-E/2)|^2+(1-2s)|E|^2.                         (13)

We use the unchanged predecessor bound P<=8I. Thus fixed finite F controls
E and CA in the marked reading along (12). It does not bound all integer
coefficients. The old growing conjugate neutral mode is still present.
H_e and T are not asserted symplectic or variational.

## 4. An exact first-hop witness on the full graph

On the infinite graph, or either even torus containing the distinct square
vertices 0,a=b1,b=b2,a+b, take A=0 and E=-1 on exactly the four edges

    0->a,  a->a+b,  0->b,  b->a+b.                          (14)

All other E entries vanish. The initial charges are +2 at 0 and -2 at a+b,
and zero elsewhere. F=4. No material support matrix L was introduced.

At phase c=0 (type 01, even first-coordinate tail), the two occupied
01 edges each have delta=2, E_e=-1, PA=0, so g=0. Both flip to +1.
Other edges of this matching have delta=0 and do nothing. The positive
charge moves from 0 to a, and the negative one from a+b to b. Both arrival
vertices were initially neutral. The subsequent free wave gives

    A'=E_hop,       E'=E_hop,       F'=4.                    (15)

The new charge support is exactly {a,b}. This is a genuine one-step change
of charge position read from the field, not movement of a supplied label.
It is NOT a proof of indefinite travel, inertial motion, an asymptotic
particle state, or a physical electron. The schedule and resonant initial
flux are chosen. Any longer trajectory must be computed or proved under
that same rule, never imposed as a current sequence.

## 5. The price: this hop fails robust marked reading

There is a sharp obstruction in exactly the local class used above.
Assume a total map fixes A and all E except E_e; its endpoint charges must
be either unchanged or exchanged, and it conserves F on the entire carrier.
If it is continuous in the marked-field subspace topology, it is identity.

Proof. A nontrivial value at X necessarily has delta!=0 and g=0 by (8)-(10).
P_ee>0, since e belongs to a triangle. Keep E fixed and perturb only

    A_m=A+s^m e,       m=1,2,... .                           (16)

These are exact R-valued states, converging to X in the marked reading,
with the SAME charge distribution. Their swap bracket is

    g_m=-s^(m+1) P_ee != 0.                                 (17)

Energy conservation forbids the exchange there, so the map is identity
on X_m. Its outputs converge to X, not its nontrivial output at X.
This contradicts continuity. Conversely identity is continuous.
No theorem about all nonlinear or extended-state interactions follows.

For the square witness, take e=0->a in (16). That edge is the only phase-0
matching edge meeting 0. At the unperturbed input the final charge at 0 is
zero. At EVERY perturbed input it remains +2. The free wave does not change
that conclusion. Thus the full scheduled rule has an explicit observable
continuity failure, not merely an unobserved coefficient discontinuity.
Choosing a numerical tolerance would change (11) and generally violate
exact energy conservation; it is not an allowed repair.

Accordingly (12) earns only a resonant mobile-defect construction. It FAILS
the explicitly tested robustness requirement and is not a derived robust
free-charge law. Within this class no continuous alternative can rescue it.
A different construction may change A, change a larger field neighbourhood,
add actual recoil degrees, or adopt a different complete interaction law.

For a charge q moving from a charged vertex to a neutral neighbour while
only E_e changes, the precise outstanding mechanical/interaction exchange
would have to be

    Delta E_other=-q[2E_e-s(PA)_e+q]                        (18)

in doubled-energy units. Adding an account coordinate with (18) as its
update would not derive a mechanical carrier. Nor does conservation alone
select a mass, momentum variable or law for one.

## 6. A fixed unit charge has a positive infimum, but no minimum here

The earlier unit-rescaling argument scales charge as well as field. It must
NOT be used as if it preserved a specified nonzero charge. A separate
fixed-charge test is possible on the actual labelled (2,2,2) D3 quotient.
Set rho_f=delta_0-delta_a for a=b1. These charges and all R-valued arrays
have literal equality; the charge is fixed, not rescaled.

Let Delta=G^T G. Over the reals, any E with G^T E=rho_f decomposes uniquely
as E=E_L+E_T, where E_L=G Delta^+ rho_f and G^T E_T=0. Since P G=0,
(13) gives

    F(A,E)>=|E_L|^2=rho_f^T Delta^+ rho_f.                   (19)

The positive matrix I-sP/4 implies equality requires E_T=0 and CA=0.
It is attained on the REAL completion by E=E_L,A=0. Delta^+ here is only
the inverse on the mean-zero vertex subspace, with zero on constants.

The eight vertex characters are chi_t(x)=(-1)^(t.x), t in F2^3. The six
edge directions are all nonzero elements except (1,1,1). Because labelled
opposite edges remain separate at size two, the Laplacian eigenvalue is

    lambda_t=2 sum_d(1-chi_t(d)).                            (20)

It is 12 on the four odd-weight t, 16 on the three weight-two t, and zero
at t=0. The Fourier coefficient of rho_f is 1-chi_t(a). It is two on four
t, exactly two with eigenvalue 12 and two with eigenvalue 16. Parseval gives

    rho_f^T Delta^+ rho_f
      =(1/8) [2*4/12+2*4/16]=7/48.                         (21)

These counts are an exact analytical calculation, not a numerical fit.

The SAME number is the infimum over R-valued fields with EXACT unit charge.
An integer solution exists: E0=-e_(0->a). The real kernel of G^T is spanned
by integer cycle vectors of this connected finite multigraph. R is dense
in the marked real line: s^m->0 and nearest integer multiples of s^m
approximate any real number. Approximate the real coefficients of
E_L-E0 in an integer cycle basis by coefficients in R. This produces
E_j in R^48 with G^T E_j=rho_f EXACTLY and E_j->E_L. With A=0,
F(0,E_j)=|E_j|^2->7/48.

But F(A,E) belongs to R on every exact state. R intersect Q=Z, while
7/48 is not an integer. Therefore the infimum is not attained:

    inf_{R states, fixed rho_f} F=7/48,
    no exact state has F=7/48.                              (22)

In ordinary energy H=F/2 the infimum is 7/96. All states in this unit-charge
sector already have primitive complete integer coordinates: a common
integer divisor greater than one would divide the unit coefficient in
G^T E, which is impossible. Primitivity does not repair nonattainment.
The same approximation supplies infinitely many fixed-charge states in a
bounded energy interval. Coordinate discreteness does not make this marked
fixed-charge energy surface finite.

This result does NOT deny a positive energy cost at fixed charge, and does
NOT prove that every dynamically selected charged state is impossible.
It excludes selecting an exact ground-state carrier here by bare minimization
of this specific energy. Metastability, additional constraints, another
energy and genuine microscopic state selection remain separate questions.

## 7. Physical accounting and the exact outstanding task

For finite-support E on the infinite graph, summing G^T E gives zero.
The same identity holds for any finite closed quotient. Therefore a
nonzero charged core needs compensating charge or an appropriate noncompact
field/boundary sector. A fully compact isolated one-sign charged field
cannot be manufactured by changing its name. The square witness retains
its compensating charge explicitly. A finite-support two-charge field need
not be a static minimizer or a freely translating dressed particle.

All new equations are R-homogeneous except their equality predicates, which
are homogeneous too. Multiplying all fields by s^m commutes with W and H,
scales charge by s^m and F by s^(2m), and preserves primitive integer gcd.
Thus the construction supplies neither a selected charge unit nor mass.
It does not recover an electron, proton, neutron or photon quantum.

The proven useful distinctions are now concrete:
- the old bound-charge reading has an exact homogeneous no-transport law;
- the new field-defect rule can move an actual charge value while conserving
  the unchanged free-field energy and leaving neutral waves untouched;
- that local move is resonance-only and discontinuous in the marked reading;
- even at fixed unit charge, bare marked-energy minimization has no exact
  minimizer on the stated finite integral carrier.

A physical successor must therefore supply more than a moving maximum or
an imposed trajectory. It needs independently admitted charge/source
semantics, accompanying field, a robust complete evolution and actual
mechanical degrees or an alternative energy mechanism. The new comparison
is not the old variational bound-material action, not an accepted source-free
Gauss constraint, and not a derivation from native U or J. No physical O
closes. No independent review is claimed. A finite audit cannot by itself
establish these all-state and infinite-sequence arguments.

Primary methodological context only: Squire, Qin, Tang,
arXiv:1401.6723; Moon, Teixeira, Omelchenko, arXiv:1409.0854.
They distinguish charged-particle transport and exact current deposition
from a prescribed polarization law; no theorem from them is needed above,
and no original-paper files are redistributed. The local charge-swap
classification and the fixed-charge calculation are self-contained.

Original prose: Apache-2.0.
