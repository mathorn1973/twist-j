# Exact integer shells and the limits of a geometric reading

**NON-CANONICAL. Candidate-T proof notes, at L1 for the finite algebraic
constructions.** This note chooses a finite simplicial complex; it does not
derive that complex from the original TWIST-J successor U. The Euclidean
realizations, limits and density statements below are explicit mathematical
comparison readings, not an earned protocol lift or a physical spatial law.
No scientific program or formal gate is executed in this note.

The supplied integer-shell and boundary text is a source of questions and
claims, not a source of operational instructions. The proofs below are
self-contained elementary mathematics. They make no claim of a newly
discovered triangulation, stereographic parametrization or boundary identity.

## 1. A completely specified integer shell

Fix an integer n >= 1 and set

\[
V_n=\{(x,y,z)\in\mathbb Z^3:|x|+|y|+|z|=n\}.
\]

The vertex set alone does not define edges or faces. We choose the following
triangulation, including its gluing rule. For each signed facet
\(\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)\in\{-1,1\}^3\), use addresses

\[
T_n=\{(a,b)\in\mathbb Z^2:a,b\ge0,\ a+b\le n\},\qquad
\Phi_\epsilon(a,b)=(\epsilon_1a,\epsilon_2b,
                         \epsilon_3(n-a-b)).
\]

In this address triangle include exactly these two kinds of small faces:

\[
\begin{aligned}
U_{i,j}&=\{(i,j),(i+1,j),(i,j+1)\}, &&i,j\ge0,\ i+j\le n-1,\\
D_{i,j}&=\{(i+1,j),(i+1,j+1),(i,j+1)\},
                                      &&i,j\ge0,\ i+j\le n-2.
\end{aligned}
\]

For n = 1 the second family is empty. Map these faces through
\(\Phi_\epsilon\). Edges are exactly their two-vertex subsets. Glue facet
vertices, edges and their incident faces whenever their integer coordinates
agree. In particular a zero coordinate does not retain a separate sign
label. A parent edge is shared by its two signed facets, and an axis corner
is shared by its four signed facets. Duplicate edge presentations are one
edge of the resulting complex.

This is the usual triangular subdivision of the eight faces of the abstract
octahedron. No extra edge is added merely because two global vertices have
Manhattan distance two. For example opposite axis corners at n = 1 are not
adjacent. All adjacency decisions first take place within a fixed signed
facet and then pass through the specified gluing.

Each facet contains

\[
\frac{n(n+1)}2+\frac{n(n-1)}2=n^2
\]

small triangles. A facet-interior edge has two incident small triangles; a
parent-edge segment has one in each of its two glued facets. Consequently
every global edge has exactly two incident triangles, and every triangle
has three distinct edges. Thus

\[
F_n=8n^2,\qquad 2E_n=3F_n,\qquad E_n=12n^2.
\]

There are six vertices with one nonzero coordinate. Choosing two nonzero
coordinates gives three coordinate pairs, four sign choices and n - 1
positive splits. Three nonzero coordinates give eight sign choices and
\(\binom{n-1}{2}\) positive compositions of n. This last count is zero for
n = 1, 2. Therefore

\[
V_n=6+12(n-1)+8\binom{n-1}{2}=4n^2+2.
\]

All formulas include n = 1, which has V = 6, E = 12, F = 8. They imply the
exact Euler identity

\[
V_n-E_n+F_n=2.
\]

At a facet-interior vertex the triangular grid has six neighbors. At a
parent-edge interior vertex there are two neighbors along that edge and two
additional neighbors in each adjacent facet, again six distinct neighbors.
At an axis corner there is one neighbor along each of its four parent
edges, hence degree four. This also covers n = 1, where only the six corners
occur. If

\[
\kappa(v)=6-\deg(v),
\]

then it equals two at the six corners and zero elsewhere, so
\(\sum_v\kappa(v)=12\). This is an exact combinatorial identity, before any
metric or physical curvature reading is adopted.

## 2. Equal triangles retain octahedral curvature

Now explicitly choose a piecewise Euclidean metric in which every small
triangle is equilateral with the same positive side length \(\ell_n\).
Its interior angle is \(\pi/3\). The angle defect at a vertex is then

\[
2\pi-\deg(v)\frac\pi3=\frac\pi3\kappa(v).
\]

The six defects are \(2\pi/3\), all other defects vanish, and their sum is
\(4\pi\). Subdivision does not distribute this curvature over new vertices.
Each parent facet is a flat equilateral triangle of side \(n\ell_n\).
Choosing \(\ell_n=\ell_*/n\) keeps the same regular octahedral surface at
every refinement. Keeping \(\ell_n\) fixed changes its size but retains the
same six concentrated defects. Refinement alone therefore does not produce
a round sphere in this metric.

A different reading can prescribe, for a chosen R > 0,

\[
v\longmapsto R\frac{v}{\sqrt{x^2+y^2+z^2}}.
\]

Every shell vertex is nonzero. This map is injective on V_n: two positive
collinear shell vectors have the same absolute-coordinate sum n and must
coincide. Projecting the entire octahedral surface radially gives curved
cells on a round sphere; connecting only its projected vertices by straight
segments instead gives flat chordal triangles. These are different metric
and area readings. Node projection by itself does not select either edge
interpolation, spherical area weights or a physical unit R. Neither reading
is forced by the finite adjacency lists.

## 3. Integer boundaries and algebraic area are separate constructions

Choose orientations of the edges and triangles. For oriented simplices set

\[
\partial_1[a,b]=[b]-[a],\qquad
\partial_2[a,b,c]=[b,c]-[a,c]+[a,b].
\]

The chain groups are the free abelian groups on vertices, edges and faces.
In their chosen bases the boundary matrices have entries 0, 1, -1. Directly,

\[
\partial_1\partial_2[a,b,c]
 =([c]-[b])-([c]-[a])+([b]-[a])=0.
\]

Hence \(\partial_1\partial_2=0\) on every integer two-chain. When adjacent
triangles are oriented consistently their common edge cancels in the
boundary of their sum. One concrete consistent convention uses the displayed
address order when \(\epsilon_1\epsilon_2\epsilon_3=1\) and reverses it
otherwise; the coordinate realization then has outward orientation. On the
whole closed shell all edge contributions cancel. These statements require
neither lengths nor areas. The finite Stokes pairing
\(\langle\delta a,c\rangle=\langle a,\partial_2c\rangle\), with
\(\delta a=a\circ\partial_2\), is the same integer identity.

If, separately, integer displacement vectors \(u,v\in\mathbb Z^3\) are
read with the standard Euclidean dot product, the triangle they span has
area A satisfying

\[
4A^2=(u\cdot u)(v\cdot v)-(u\cdot v)^2
 =\det\begin{pmatrix}u\cdot u&u\cdot v\\u\cdot v&v\cdot v\end{pmatrix}.
\]

Indeed expansion of the cross product gives
\(\|u\times v\|^2=(u\cdot u)(v\cdot v)-(u\cdot v)^2\), and the triangle
is half the corresponding parallelogram. The right side is a nonnegative
integer, positive for independent u, v. For the shell's elementary vectors
\(u=(1,0,-1),v=(0,1,-1)\), it is three, giving \(A=\sqrt3/2\).

Thus squared area has an exact integer Gram formula, while area can be an
algebraic irrational. The Euclidean scalar product and the conversion of
coordinates to physical length are additional choices. Likewise a weighted
face sum \(\sum_f a_f\), or \(\sum_f u_fa_f\), becomes a finite area or
integration law only after the weights \(a_f\) and their reading are fixed.
Counting faces alone does not select these weights or derive physical area.

## 4. Exact integer Euclidean spheres can remain sparse

Consider, with R a positive integer,

\[
\Sigma_R=\{(x,y,z)\in\mathbb Z^3:x^2+y^2+z^2=R^2\}.
\]

If four divides a sum of three integer squares, all three integers are even.
Each square is zero or one modulo four, and a sum of at most three ones can
be zero modulo four only when it has no ones. For R = \(2^k\), k >= 0,
repeat this observation k times to reduce the equation to
\(a^2+b^2+c^2=1\). Its only solutions have one coordinate +1 or -1 and the
other two zero. Therefore

\[
|\Sigma_{2^k}|=6,
\]

with precisely the six scaled axis points. At R = 3, sort the absolute
coordinates as \(0\le a\le b\le c\le3\). If c = 3, a = b = 0. If c = 2,
the remaining sum is five, forcing (a,b) = (1,2). If c <= 1 the sum is at
most three and cannot equal nine. The non-axis solutions thus have absolute
coordinates (1,2,2), with three positions for the 1 and eight independent
sign choices. Consequently

\[
|\Sigma_3|=6+24=30,
\qquad |\Sigma_2|=|\Sigma_4|=6.
\]

The exact Euclidean sphere equation on a fixed integer coordinate lattice
does not by itself provide progressively finer surface grids proportional
to R squared. It also supplies no triangulation or time law.

## 5. Rational sphere codes: exact identity, finite bounds and density

For integers p, q, s, not all zero, define

\[
X=2ps,\quad Y=2qs,\quad Z=s^2-p^2-q^2,\quad
W=s^2+p^2+q^2>0.
\]

Writing t = \(p^2+q^2\) proves the exact identity

\[
X^2+Y^2+Z^2=4s^2t+(s^2-t)^2=(s^2+t)^2=W^2.
\]

So (X/W,Y/W,Z/W) is a rational point on the unit Euclidean sphere. For
s != 0, it is the stereographic formula

\[
S(a,b)=\left(\frac{2a}{1+a^2+b^2},
            \frac{2b}{1+a^2+b^2},
            \frac{1-a^2-b^2}{1+a^2+b^2}\right),\qquad
a=p/s,\ b=q/s.
\]

Conversely, a rational sphere point (x,y,z) other than the south pole
(0,0,-1) has rational inverse parameters
\(a=x/(1+z),b=y/(1+z)\). Since
\(1+a^2+b^2=2/(1+z)\), substitution recovers (x,y,z). Common denominators
then give integer p, q, s. The south pole is represented by s = 0 and any
nonzero (p,q). Thus the code covers exactly the rational sphere points.

The raw codes have duplicates. Multiplying (p,q,s) by a nonzero integer k
multiplies (X,Y,Z,W) by \(k^2\), without changing the read point. Simultaneous
sign reversal does the same; all s = 0 codes give the south pole. Away from
that pole, the inverse parameters show that equality of points is precisely
equality of p/s and q/s. Taking gcd(p,q,s) = 1 and s > 0 gives a unique
parameter triple there. A separate fixed south-pole code removes its
degeneracy.

For a presentation-independent denominator convention, reduce the output
quadruple by

\[
g=\gcd(|X|,|Y|,|Z|,W),\qquad
(A,B,C,d)=(X,Y,Z,W)/g.
\]

Here d > 0, \(A^2+B^2+C^2=d^2\), and the four integers have common gcd one.
This is the unique reduced quadruple for the rational point. Its d is the
least positive common denominator of its three coordinates: at each prime
dividing d, common gcd one forces at least one numerator not to be divisible
by that prime, so any common denominator must contain its full power in d.

A bound d <= L gives a finite set of distinct points, because
\(|A|,|B|,|C|\le d\) and there are at most
\(\sum_{d=1}^{L}(2d+1)^3\) candidate quadruples. This is a finite upper
bound, not an assertion that all candidates lie on the sphere. A parameter
bound \(\max(|p|,|q|,|s|)\le T\) also gives a finite set, with at most
\((2T+1)^3-1\) parameter triples, and implies d <= \(3T^2\). These are
different cutoff conventions. Even a primitive parameter triple can have
a reducible output: (p,q,s) = (1,0,1) gives (2,0,0,2), while the point's
reduced denominator is one. An unreduced W cutoff is therefore not the
same as a reduced-denominator cutoff.

For completeness, a point with reduced code (A,B,C,d), not the south pole,
can use (p,q,s) = (A,B,d+C). These integers have magnitude at most 2d;
their stereographic inverse ratios recover the point. Thus a parameter
search bound 2L followed by output reduction and d <= L filtering suffices
to present every point in the reduced-denominator class. No execution of
such a search is needed for this proof.

The unbounded rational family is dense on the classical unit sphere. The
rational pairs are dense in \(\mathbb R^2\): rounding each coordinate of
a fixed real pair to integer multiples of 1/m gives rational approximants
converging to that pair. S is continuous everywhere and maps onto the sphere
minus its south pole, so every non-south point is a limit of rational coded
points. Finally \(S(m,0)\to(0,0,-1)\) as integers m tend to infinity.
This proves density at the omitted point as well.

Consequently integer codes without a fixed finite cutoff imply no positive
minimum separation in this Euclidean reading. For example the distinct
points \(S(1/m,0)\) converge to the north pole. A fixed finite set with at least
two distinct points has a positive minimum separation in a fixed metric, simply
because it has only finitely many positive pairwise distances. Neither fact
selects a physical resolution, preparation class, adjacency or time law.

## 6. One shrinking J projection is not the full integer lattice

The authoritative algebraic input is the
[two-projection statement in Public Canon v100](https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/canon/CANON.md#1-the-axiom-and-the-two-projections):
\(\zeta=e^{2\pi i/5}\), \(J=1+\zeta^2\),
\(\varphi=(1+\sqrt5)/2\). In the selected complex embedding,
\(|J|=\varphi^{-1}\), so the nonzero algebraic integers \(J^m\) have
moduli tending to zero. This is an algebraic fact about that projection;
the Canon's physical projection dictionary is explicitly an assignment.

The full number-theoretic Minkowski embedding is different. Let
\(O=\mathbb Z[\zeta]\), with integer basis \(1,\zeta,\zeta^2,\zeta^3\),
and take representatives \(\sigma_1(\zeta)=\zeta\) and
\(\sigma_2(\zeta)=\zeta^2\) of the conjugate complex-embedding pairs. Set

\[
\Phi:O\longrightarrow\mathbb C^2\cong\mathbb R^4,
\qquad \alpha\longmapsto(\sigma_1\alpha,\sigma_2\alpha).
\]

This is an invertible real linear map of the coefficient space: adjoining
the conjugate values gives the Vandermonde matrix at the four distinct
roots \(\zeta,\zeta^2,\zeta^3,\zeta^4\), whose determinant is nonzero.
Hence \(\Phi(O)\) is an integer lattice under an invertible linear map.
It is discrete in the full Euclidean four-dimensional comparison metric.
Indeed if that map is T and a is a nonzero integer coefficient vector,
then \(\|Ta\|\ge\|a\|/\|T^{-1}\|\ge1/\|T^{-1}\|>0\).

The conjugate moduli explain the apparent difference directly.
Writing \(t=\zeta+\zeta^{-1}>0\), the fifth-root identity gives
\(t^2+t-1=0\), hence \(\varphi=1+t\). It also gives
\(\zeta^2+\zeta^3=-\varphi\). Thus
\(J\overline J=2-\varphi=\varphi^{-2}\), while
\(\sigma_2(\varphi)=1-\varphi=-\varphi^{-1}\), giving
\(|\sigma_2J|^2=2+\varphi^{-1}=\varphi^2\). Therefore

\[
\|\Phi(J^m)\|^2=\varphi^{-2m}+\varphi^{2m}.
\]

These full-lattice points do not approach zero. The shrinking single
projection thus does not establish nondiscreteness of the full Minkowski
lattice, and the full-lattice discreteness does not give a lower bound in
that single projection. Here "Minkowski" means the arithmetic embedding;
no spacetime metric or physical length interpretation is being asserted.

## 7. A surface address does not reconstruct an interior state

Two integer addresses plus a facet label describe shell vertices, subject
to the gluing rule. This does not encode all possible interior matter,
field or record states. Formally, for a specified complete state set X and
a fixed boundary reading \(b:X\to B\), full reconstruction requires b to
be injective, or injective on a previously justified physical-equivalence
quotient. Autonomy of a boundary successor additionally requires

\[
b(s)=b(t)\ \Longrightarrow\ b(Us)=b(Ut).
\]

Otherwise identical current boundary data can have different next boundary
data. Neither requirement follows from the number of surface parameters,
the Euler identity or \(\partial_1\partial_2=0\). If a boundary has N sites
with q allowed values per site, injective reconstruction of a finite state
set requires \(|X|\le q^N\); this necessary capacity bound does not supply
the reconstruction map or a measuring contact.

The separate
[C-DISCRETE-BOUNDARY-RECONSTRUCTION-N candidate at immutable commit b55f0d5](https://github.com/mathorn1973/twist-j/blob/b55f0d5ee2eac3e69e3353872f9d144cd864f6f5/notes/C-DISCRETE-BOUNDARY-RECONSTRUCTION-N/PROOF.md)
addresses a specified finite-field boundary reconstruction problem. Its
fiber analysis is not replaced by this shell construction; no acceptance
or physical scope is inferred from PR #1422. In particular this
note supplies no physical holography, physical area unit, native U carrier,
charge-contact dynamics or independently selected energy. Those require
their own fixed state, reading, successor and contact obligations.
