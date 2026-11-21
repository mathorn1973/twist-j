# Exact boundaries between J, U and D

**NON-CANONICAL / candidate-T / L1 only.**
Author: A. M. Thorn <thorn@twistj.com>. Owner #1288.
Public premises refer to the v94 base in PREREG.md. Labels "inherited T"
refer to that registry; all new conclusions below remain candidate-T.

## 1. The unmarked unit axis and the marked J step

Put K=Q(j), j a primitive fifth root, O=Z[j],
phi=-j^2-j^3 and J=1+j^2=j/phi. The inherited J-HARMONIC-SEAM [T]
gives E=O^*=mu_10 x <phi>. Thus

    C=E/mu_10 ~= Z,      [phi^m] <-> m,
    L_[J](m)=m-1.                                      (1)

This uses the full unit theorem, not merely the Dirichlet rank count.
K has no real embedding: its four embeddings form two complex-conjugate
pairs. Its real quadratic subfield has two real embeddings.

Let sigma_2(j)=j^2. Since sigma_2(phi)=-phi^-1,

    sigma_2(J)=-j^2 phi=(-j^3)J^-1.                     (2)

Consequently sigma_2 induces tau(m)=-m on C and

    tau L_[J] tau = L_[J]^-1.                          (3)

In particular (2) is not equality sigma_2(J)=J^-1 in K. The torsion
factor is essential before taking the quotient.

**Proposition U1 (unmarked nonselection).** There is no Galois-invariant
choice of a generator, or positive cone defining an order, on the unmarked C.

Proof. Its two generators are interchanged by tau. If a positive cone P
were invariant, then P=-P. But for every nonzero m a positive cone contains
exactly one of m,-m. This is a contradiction. The other Galois elements
act by either identity or tau, so the full Galois claim follows. QED.

The word unmarked is load-bearing. On (C,[J]), the semigroup
{[J]^n:n>0} is already distinguished algebraically; no complex embedding
is necessary to make that choice. Sigma_2 does not preserve this marking.
U1 proves no physical time-arrow statement for the marked theory.

**Proposition U2 (three different reversal questions).**

1. Multiplication M_J:O->O is bijective: J^-1=-j-j^2 lies in O and
   J(-j-j^2)=1 by 1+j+j^2+j^3+j^4=0.
2. On the unit carrier E, I(u)=u^-1 is an involution with
   I L_J I=L_(J^-1).
3. There is no additive lattice automorphism A:O->O satisfying
   A M_J A^-1=M_J^-1.

For the third statement, an additive lattice automorphism extends to an
invertible Q-linear map on K, and similar Q-linear maps have equal traces.
Each j^a with 5 not dividing a has field trace -1. Hence

    Tr(M_J)=Tr(1+j^2)=4-1=3,
    Tr(M_J^-1)=Tr(-j-j^2)=2.                           (4)

They are unequal. This also excludes an additive involutive reversor. QED.

The inversion I in clause 2 is not additive, and inversion of a nonunit
integral element need not be integral. It cannot be used as an additive
symmetry of the entire lattice. Conversely, the absence of the particular
linear symmetry in clause 3 does not turn bijective multiplication into
information erasure or identify its orientation with physical time.

Thus the stronger proposed assertion "no algebraic invariant distinguishes
J and J^-1" is false: trace (4) distinguishes them. The valid nonselection
theorem is U1 in its stated symmetry class.

## 2. Native synchronization is finite loss on a specified start family

Write x=(p1,p4,p1p,p4p,q,r) in X=F_5^6 and z(x)=sum x_i. Let

    theta_n=s_2(n) mod 2,
    F_t(x)=g_(z(x)+2t mod 5)(x),
    U(n,x)=(n+1,F_(theta_n)(x)),
    E_n(x0)=pr_X U^n(0,x0).

KERNEL-Z6-SYNCHRONIZATION [T] states that for n>=3

    X_n={x:z(x)=4+2theta_(n-1)},
    E_n|{z=z0}: {z=z0} -> X_n is bijective
    for every z0 in F_5.                               (5)

Therefore |X_n|=5^5, E_n is exactly five-to-one, and the selected tail
generators for adjacent bits 00,01,10,11 are respectively e,b,b,d.
Each is an involution mapping X_n bijectively onto X_(n+1).

It follows immediately that for any heads x0,y0 and n>=3,

    E_n(x0)=E_n(y0) iff E_3(x0)=E_3(y0).                (6)

There are no later mergers on the family (5). This is a fixed-time exact
information statement, not an entropy or energy-dissipation statement.

The quantifier cannot be extended to all of Omega=N_0 x X. The inherited
generator trace laws are z(bx)=-z(x), z(dx)=2-z(x), z(ex)=3-z(x).
For t=0 and y in {z=4}, the distinct states b(y) in {z=1} and e(y) in
{z=4} both map to y under F_0. For t=1 and y in {z=1}, the distinct
states d(y) in {z=1} and b(y) in {z=4} both map to y under F_1.
Thus at every counter n the full slice contains a collision. On each
synchronized reachable sheet X_n, n>=3, only one member of each such pair
is admitted.

## 3. Exact native coordinates, partial inverse and direct jumps

This section records the already registered U-NATIVE-CHART-AND-QDD-READBACK
[T], with its proof in
[P-QDD-U-NATIVE-READBACK-1/PROOF.md](../../probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md),
sections 1-3. It is not a new decoder result.

For integers M>=0 define the finite alternating sum

    S(M)=M-floor(M/2)+floor(M/4)-floor(M/8)+... .

For n>=3 put

    t_n=(-1)^(n-3), h_n=(-1)^(n+theta_(n-1)),
    N_n=S(floor((n-1)/2))-1.

On X_n the conserved chart Lambda_n(x)=(alpha,beta,gamma,delta,epsilon) is

    alpha=t_n(p1+p1p),       beta=t_n(p4+p4p),
    gamma=h_n(p1-p1p-2),     delta=h_n(p4-p4p-1),
    epsilon=t_n*r-N_n.                                 (7)

All labels are in F_5. For l=(alpha,beta,gamma,delta,epsilon), the inverse is

    A=t_n*alpha, B=t_n*beta, C=2+h_n*gamma, D=1+h_n*delta,
    p1=3(A+C), p1p=3(A-C), p4=3(B+D), p4p=3(B-D),
    r=t_n*(epsilon+N_n), q=4+2theta_(n-1)-A-B-r.         (8)

Three is the inverse of two in F_5. The inherited proof gives both inverse
identities and Lambda_(n+1)(F_(theta_n)x)=Lambda_n(x).

**Proposition R1 (precise tail conjugacy).** For

    R_3={(n,x):n>=3, x in X_n},
    C(n,x)=(n-3,Lambda_n(x)),

C is a bijection R_3 -> N_0 x F_5^5 and conjugates U|R_3 to

    S_+(k,l)=(k+1,l).                                  (9)

This follows by substituting the inherited chart invariance. In particular
U|R_3 is injective but not onto R_3: its image excludes n=3. It is a
bijection between each pair of consecutive slices, not a homeomorphism of
the entire one-sided tail onto itself.

For n>=4 its inverse on the image is exactly

    (n,x) -> (n-1,g_(4+2(theta_(n-2)+theta_(n-1)) mod5)(x)).  (10)

The same involution generated the preceding step, which proves (10).

Also, for every origin-zero head and n>=3,

    E_n(x0)=Lambda_n^-1(Lambda_3(E_3(x0))).              (11)

Only three initial transitions and logarithmically many integer arithmetic
operations in n are required. Bit complexity is not identified with the
number of such operations. Outputting an entire list of n checkpoints is
a different task from computing its specified nth entry.

The existing no-finite-autonomous-realization result follows from exact
aperiodicity, whereas (11) allows random-access evaluation. There is no
contradiction: a finite autonomous system must eventually repeat, but an
algorithm supplied with an unbounded integer n is not such a system.

For full initial-head readback, retaining z(x0) as a correctly initialized
five-valued auxiliary label suffices by (5); fewer than five values cannot
separate a five-element fibre. This is also inherited from the native
readback theorem. It applies to initialized reachable slices, not the
unconstrained product of Omega with an arbitrary extra register. A complete
head-retaining orbit, the source type of some decoders, is different again
from a current checkpoint and already contains x0.

## 4. Natural extension, reversible dilation and the auxiliary hull

For a map f:Y->Y define its ordinary natural extension here by

    Nat(f)={(y_k)_(k in Z): f(y_k)=y_(k+1) for every k}.

**Proposition R2.** Nat(U) is empty; so is Nat(U|R_3).

Proof. The counter in a compatible bi-infinite sequence would satisfy
n_k=n_0+k. It becomes negative for sufficiently negative k, contrary to
n_k in N_0. Equivalently, U^m(Omega) lies entirely in counter slices n>=m,
so their intersection is empty. The same argument applies to R_3. QED.

A different construction embeds (9) in the bilateral shift

    S_Z(k,l)=(k+1,l) on Z x F_5^5,
    R(k,l)=(-k,l),  R S_Z R=S_Z^-1.                    (12)

This is a reversible dilation obtained by adjoining negative counter
coordinates in the chart. It is not Nat(U), and it defines neither native
theta_n at negative n nor a physical history for those added states.

There is already a separate, more structured two-sided system. The public
TM-CHECKPOINT-HULL-STABLE-IMAGE [T] freezes the two-sided Thue-Morse hull
K_TM, (S_K kappa)_m=kappa_(m+1), and

    X_hull=K_TM x X,
    V(kappa,x)=(S_K kappa,F_(kappa_0)(x)),
    X_stab={(kappa,x):z(x)=4+2kappa_(-1)}.

Its registered theorem states

    V^9(X_hull)=X_stab=intersection_(m>=0) V^m(X_hull),  (13)

with nine least. V_stab is a homeomorphism and has the involutive reversor

    (rho kappa)_m=kappa_(-m-1),
    i(kappa)=4+2(kappa_(-1)+kappa_0) mod5,
    R_cp(kappa,x)=(rho kappa,g_(i(kappa))(x)),
    R_cp V_stab R_cp=V_stab^-1.                        (14)

Evaluation at zero conjugates Nat(V) with X_stab. Unlike R2 this inverse
limit is nonempty. The difference is the original carrier, not conflicting
answers about one object. See the complete registered proof in
[the hull preregistration](../../probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1/PREREG.md),
sections 3.1-3.6.

The Canon explicitly does not select X_stab as physical state space or
identify V with U. Accordingly (13)-(14) do not prove absence of a physical
arrow, any thermodynamic property, or physical time-reversal symmetry.

## 5. Exact fired group and the spatial commutator obstruction

Let G=<b,d,e> on X. Let N be the 25 translations T_(u,v) in the final
two coordinates. FIRED-COMMUTATOR-NOGO [T] gives

    [G,G]=N ~= C_5 x C_5,
    [d,e]=T_(3,0), [b,d]=T_(3,3), [b,e]=T_(1,3).       (15)

The full G is nonabelian. Its action on the first four piston coordinates
is abelian. The linear parts are B,-I,-I for b,d,e, and generate the four
distinct matrices I,B,-I,-B.

**Proposition L1 (abelianization and exact factor obstruction).**

    G/N ~= C_2 x C_2,             |G|=100.              (16)

Moreover any homomorphism Pi:G->Aut(V) with N contained in ker Pi has
Pi([g,h])=id for every g,h. It cannot realize a target requiring a
nonidentity spatial commutator.

Proof. The generator formulas give ed=T_(1,0), so eN=dN. The quotient
is generated by commuting involutions bN,dN, hence has at most four
elements. Its linear image has four elements, and N has identity linear
part, so it has at least four. This proves (16). Any homomorphism killing
N factors through that abelian quotient, proving the final assertion. QED.

This does not rule out every geometry. For example, the commuting coordinate
translations of Z^3 preserve the exact graph distance
d(x,y)=sum_i |x_i-y_i| and support nearest-neighbor dependencies. A metric
space does not require noncommuting translations. The hypothesis about
spatial commutators is a particular target contract. Nonhomomorphic or
fibre-sensitive readings lie outside Proposition L1.

## 6. Fixed-source capacity for independent local configurations

Freeze origin n=0, one known observation counter n, one deterministic
decoder, and all its contexts and parameters. The only variable source
input is x0 in X. No external configuration, independent ensemble,
newly writable input, variable start counter or changing decoder is supplied.

**Proposition L2 (faithful-configuration capacity).** A decoder of the
head-retaining prefix (x0,...,E_n(x0)), or entire origin-zero forward orbit,
has at most 5^6 possible outputs. A decoder of the synchronized current
checkpoint at fixed n>=3, or its entire subsequent tail, has at most 5^5.

Proof. The first inputs are deterministic functions of 5^6 possible heads.
The second inputs are deterministic functions of |X_n|=5^5 possible current
states. A function cannot increase the cardinality of its image. QED.

In particular, suppose an encoding of every configuration in A^V has a
decoder left inverse, with finite |A|>=2 and finite V. Then

    |A|^|V| <= 5^6  (head-retaining source),
    |A|^|V| <= 5^5  (synchronized current/tail source). (17)

Indeed a left inverse forces the encoding to be injective. Thus the fixed
native source cannot faithfully encode full independently variable field
spaces for unbounded |V|. For binary A the upper bounds on independent
sites are 13 and 11: 2^13<=15625<2^14 and 2^11<=3125<2^12.

These are configuration-capacity bounds, not spatial-dimension bounds.
A fixed large or infinite geometric pattern can have a short description;
(17) does not forbid it. Nor does it exclude constrained field families,
an enlarged source, chosen field initial data or a decoder carrying extra
input. Making all those choices fixed is essential.

The generic capacity principle already occurs in the NON-CANONICAL
[C-OMEGA-U-TURING-1](../C-OMEGA-U-TURING-1.md), sections 2-3, which also
treats arbitrary starting counters for tail-disjoint orbits. L2 is the
fixed-source field specialization, with the sharper inherited synchronized
count. No Turing-impossibility theorem is imported as a Canon premise.

## 7. Conditional finite dependency cone

Freeze undirected graphs V_m with shortest-path graph distance,
configurations A^(V_m), and deterministic maps F_m. Write
B_R(A)=union_(a in A) B_R(a). Suppose the value (F_m x)(v) depends only on
x restricted to B_R(v), with one integer R>=0 independent of m.

**Proposition L3.** If two initial configurations differ only on A_0, their
disagreement sets satisfy

    A_(k+1) subset B_R(A_k),
    A_k subset B_(Rk)(A_0).                            (18)

Proof. For v outside B_R(A_k), the two configurations agree at every input
in B_R(v); hence their next values at v agree. This proves the first
inclusion. Iterate it and apply the graph triangle inequality for the
second. QED.

Identical prescribed time-dependent coefficients do not change this proof.
If external controls vary between the compared evolutions, their local
inputs must also be included in the disagreement bookkeeping. A spatially
global state-dependent selector cannot simply be omitted from that test.

(18) is exact finite dependency support. It is neither a general quantum
Lieb-Robinson estimate nor an identification with a physical light cone.
The graph, physical distance, clock and realization still require a bridge.
This note proves the conditional lemma; it does not construct a scalable
native realization of U satisfying its premises.

## 8. Existing chosen geometric carriers and remaining construction

RELATIONAL-GROWTH-SATURATION-BOUNDARY [T], evidenced by
[P-RELATIONAL-GROWTH-SATURATION-1](../../probes/P-RELATIONAL-GROWTH-SATURATION-1/PROOF.md),
already distinguishes native finite semantic balls from an added cover.
The native fired-translation balls have sizes 1,7,19,25,25,... . The chosen
torsion-free Z^2 cover has

    rho(x,y)=max(|x|,|y|,|x-y|),
    |B_r|=3r(r+1)+1.

It also classifies the rank-two derived lattice of the signed-integer
affine interpretation. Neither construction alone supplies a physical
three-dimensional space or the silent-spatial curvature reading.

The NON-CANONICAL
[C-OMEGA-GENERATIVE-GEOMETRY-N2](../C-OMEGA-GENERATIVE-GEOMETRY-N2/PROOF.md)
already supplies a chosen Z^3 archive, fixed metric, local scalar stencil
and dependency-closed finite patches. It explicitly adds the cover, layer
coordinate, signs, event chart, metric, scale, field initial data and source.
Its native selector bits change serialization order; completed cubes,
metric and the full field solution are independent of those order bits.
The represented scalar-field time and native archive-emission counter are
different. These limitations are part of that note, not new falsifications.
The companion
[C-NATIVE-HODGE-METRIC-SEAM-N3](../C-NATIVE-HODGE-METRIC-SEAM-N3/PROOF.md)
further delimits the metric-sensitive bridge. Neither is promoted here.

A new native locality construction must freeze at least: its scalable
source and configuration class, equality, graph and radius, permissible
encodings, correspondence of clocks, and the relationship of its active
commutators to the required geometric reading. If it claims full independent
configuration spaces, it must explicitly meet or change the source premise
in (17). A chosen output graph and equation are not that proof.

## 9. What cannot be inferred physically

The foregoing theorems are L1. The following implications were proposed in
the motivating text but are not consequences of the frozen mathematics:

- n=0 is a boundary, not a low-entropy condition without a measure and
  specified coarse observation.
- A many-to-one checkpoint map is not by itself energy dissipation.
- Noninjectivity of a subsystem read does not establish nonunitarity of a
  complete system. As an exact countermodel, the unitary SWAP sends
  |b>_S|0>_E to |0>_S|b>_E: the system output alone forgets b while the
  full state retains it. This is a logical countermodel, not a TWIST-J lift.
- Invertibility is not the same as existence of a reversor in a declared
  symmetry class, as U2 itself demonstrates. A reversor also does not decide
  all thermodynamic or observational asymmetries of a selected state.
- Spatially abelian piston action does not imply that every possible
  spatial geometry is absent; (15) also shows that the whole fired group
  is not abelian.

The remaining physical arrow and locality questions require typed decoder
contracts. No physical ARROW verdict, dimension, apparatus, occurrence,
entropy law or L2-L6 lift is earned by this candidate.
