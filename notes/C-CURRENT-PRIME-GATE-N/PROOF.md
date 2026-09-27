# Proof — C-CURRENT-PRIME-GATE-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.
**Basis:** frozen by \`PREREG.md\` at commit
\`a83d6bbace35990875a05544c913e789ac1816cf\`.
**Issue:** #1196.
**Author:** A. M. Thorn.
**Date:** 2026-09-27.

No Canon status is asserted here.

## 1. The local prime gate

Let the lattice dimension be \(D\). Fix one oriented edge \(e\).

For every transverse coordinate direction there are exactly two plaquettes
containing \(e\), one on either side. There are \(D-1\) transverse
directions. Hence the edge star contains exactly

\[
M_D=2(D-1)
\]

plaquettes.

Each occupied plaquette contributes \(+1\) or \(-1\) to
\((\partial n)_e\), and an unoccupied plaquette contributes \(0\). Therefore

\[
|(\partial n)_e|\le M_D=2(D-1).                     \tag{1}
\]

The constraint \(\partial n\equiv0\pmod p\) says that

\[
(\partial n)_e=p\,j_e,\qquad j_e\in\mathbb Z.        \tag{2}
\]

If \(p>D-1\), then \(2p>2(D-1)=M_D\). The only multiples of \(p\)
inside the interval \([-M_D,M_D]\) are therefore

\[
-p,\ 0,\ +p.
\]

Thus

\[
\boxed{p>D-1\quad\Longrightarrow\quad
       j_e\in\{-1,0,1\}.}                             \tag{3}
\]

If \(p>2(D-1)=M_D\), even \(\pm p\) lie outside the interval, so

\[
\boxed{p>2(D-1)\quad\Longrightarrow\quad j\equiv0.} \tag{4}
\]

Combining (3) and (4), the local window in which nonzero current is not
excluded and every allowed nonzero current is unit-capacity is

\[
\boxed{D-1<p\le2(D-1).}                              \tag{5}
\]

This is a local arithmetic theorem. It does not prove that every prime in the
window has a global nonzero configuration.

## 2. Four dimensions select the prime five inside this local window

The photon current representation is four-dimensional, so \(D=4\) and

\[
M_4=2(4-1)=6.
\]

The unit-current window is

\[
3<p\le6.
\]

Among odd primes there is exactly one element:

\[
\boxed{p=5.}                                          \tag{6}
\]

The neighboring cases make the statement sharp:

\[
p=3:\quad j_e\in\{-2,-1,0,1,2\}
\]

is allowed by the local arithmetic bound, while

\[
p\ge7:\quad j_e=0.
\]

So \(p=5\) is neither merely "small" nor an arbitrary odd prime from the
viewpoint of this current carrier. It is the unique odd prime for which the
four-dimensional ternary plaquette star can carry nonzero current while the
local arithmetic itself forbids every charge magnitude larger than one.

This is not a derivation of the TWIST-J axiom. It is a compatibility and
rigidity property of the already selected \(p=5\) current representation.

## 3. The five-of-six charged-edge theorem

The actual \(p=5,D=4\) carrier yields a stronger local statement.

Let \(d_e\) be the number of occupied plaquettes incident on \(e\). Since each
occupied incidence is \(+1\) or \(-1\),

\[
(\partial n)_e\equiv d_e\pmod2.                       \tag{7}
\]

The allowed boundary values are only \(-5,0,+5\).

If \(d_e\) is even, (7) excludes \(\pm5\), so the boundary is zero.

If \(d_e\) is odd, then \(d_e\in\{1,3,5\}\). Degrees \(1\) and \(3\) cannot
reach absolute boundary value \(5\). Hence a charged edge must have
\(d_e=5\), and all five signed incidences must agree.

Therefore

\[
\boxed{
j_e\ne0
\iff
d_e=5\ \text{and all five occupied incidences have one sign}.
}                                                       \tag{8}
\]

Equivalently, a unit current edge is a one-hole defect in the six-plaquette
edge star.

The neutral degrees are exactly

\[
d_e\in\{0,2,4,6\},
\]

with balanced signed incidence. This recovers the local rule used by the
exact augmented current representation in
\`C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md\`.

Equation (8) is the useful dimension-prime relation for the current program:

\[
\boxed{6\ \text{local faces} = 5\ \text{aligned occupied faces}
       +1\ \text{missing face}.}                       \tag{9}
\]

The number five is tied here to the four-dimensional edge incidence
\(2(D-1)=6\), not to a fit of a continuum parameter.

## 4. Nonzero \(p=5\) current is actually realized

The local window would be weaker if the global constraint killed every
nonzero current. It does not.

The already public family in \`CONNECTED-CURRENT.md\` defines, for every
integer separation \(D_s\ge3\),

\[
n_{D_s}=a(0)-a(D_s e_3)-\partial T_{D_s}
\]

on an even torus \(L=2D_s+4\), with ternary face coefficients and exact current

\[
\boxed{
j_{D_s}
=-\partial p_{01}(0)+\partial p_{01}(D_s e_3).
}                                                       \tag{10}
\]

Thus the current is the union of two separated unit four-edge loops with
opposite total homology contribution. The same construction contains a
neutral connecting surface.

An exact in-session finite audit of the frozen formula checked
\(D_s=3,\ldots,12\): every \(n_{D_s}\) remained ternary,
\(|\operatorname{supp}n_{D_s}|=4D_s+40\),
\(\partial n_{D_s}=5j_{D_s}\), the current had eight unit edges, and
\(\partial j_{D_s}=0\). The fact that these eight edges are two four-edge
loops follows already from the exact displayed formula (10), since each term is
the boundary of one \(01\)-plaquette.

The finite audit is candidate-C corroboration only. Equation (10) and the
all-\(D_s\) construction are the written mathematical input.

## 5. Unit conserved currents are cycle systems

Now fix \(p=5,D=4\). Orient every edge with \(j_e=+1\) in its canonical
direction and every edge with \(j_e=-1\) in the reverse direction.

Because

\[
\partial j
=\frac{\partial^2n}{5}
=0,                                                     \tag{11}
\]

the resulting finite directed graph has equal indegree and outdegree at every
vertex.

Use the standard finite Euler-decomposition argument. Start at any vertex
with an unused outgoing edge and follow unused directed edges until the trail
cannot continue. At every vertex other than the start, each arrival consumes
one unused incoming edge. Since the residual graph is balanced before the
trail starts, inability to leave an entered non-start vertex would imply that
strictly more outgoing than incoming edges had already been consumed there,
which is impossible. Hence a maximal trail closes at its starting vertex.

A closed directed trail may revisit vertices. Split it at repeated vertices
into directed simple cycles. Remove all edges of those cycles. At every vertex
the removal deletes equally many incoming and outgoing edges, so the residual
directed graph is again balanced. Iterate until no edge remains.

Therefore

\[
\boxed{
j=\gamma_1+\cdots+\gamma_r
}
                                                               \tag{12}
\]

with \(\gamma_i\) edge-disjoint oriented simple cycles.

The cycles need not be vertex-disjoint, and the decomposition need not be
unique at a vertex with more than one admissible continuation.

This is exactly the structural reduction needed before attacking the whole
current moment. It replaces a general integer flow by a unit-capacity cycle
system without pretending that the probability measure factorizes over those
cycles.

## 6. Every augmented surface component has zero total winding

The exact augmented representation of #1143 is stronger than a decomposition
of the total current. For each consistent paired surface component \(K\), a
reference signing \(\eta_K\) satisfies

\[
J_K=\frac{\partial\eta_K}{5}.                           \tag{13}
\]

Hence, as an integral one-cycle on the four-torus,

\[
5[J_K]=[\partial\eta_K]=0
\qquad\text{in }H_1(T^4,\mathbb Z).                     \tag{14}
\]

But

\[
H_1(T^4,\mathbb Z)\cong\mathbb Z^4
\]

is torsion-free. Therefore

\[
\boxed{[J_K]=0.}                                        \tag{15}
\]

Apply the cycle decomposition (12) to \(J_K\). If \(w(\gamma_i)\in\mathbb Z^4\)
is the winding vector of cycle \(i\), then

\[
\boxed{\sum_i w(\gamma_i)=0.}                           \tag{16}
\]

This point matters. A chosen decomposition may contain individually winding
cycles, but the winding cycles of one augmented component must compensate
collectively.

## 7. What this does and does not buy for the photon proof

The exact covariance remains

\[
\operatorname{Cov}_\mu(j)
=
\mathbb E_{\rm aug}\sum_K J_K\otimes J_K.               \tag{17}
\]

Equations (12) and (16) organize each \(J_K\), but they do not split (17) into
independent cycle probabilities.

The obstruction is concrete:

1. neutral matched faces can connect several disjoint current loops into the
   same surface component \(K\);
2. the sign belongs to \(K\), not independently to every cycle in an arbitrary
   decomposition;
3. at higher-valence current vertices the cycle decomposition can be
   nonunique;
4. the full weight contains the neutral surface and matching factors.

The public \(n_{D_s}\) family already demonstrates the first point: two
separated current loops can be joined by one neutral surface structure.

So the correct next target is not an independent loop gas. It is a bound on a
whole-component functional after decomposing its unit current into cycles and
keeping the neutral component weight intact.

## 8. Relation to ordinary primes

There are two different uses of the word "prime" and they must not be mixed.

The theorem above is directly about the ordinary prime parameter \(p\) in the
modular closure law. The statement \(p=5\) in (6) is exact.

A second, potentially useful language comes from primitive closed cycles.
For a fixed noninteracting finite directed graph, primitive cycles generate a
dynamical or Ihara-type Euler product, and repetition counts are recovered by
ordinary Möbius inversion. That is a legitimate mathematical analogy to prime
factorization.

It is not yet available for the full TWIST-J current measure because the
neutral surfaces make cycle weights nonmultiplicative. An Euler product for
the physical current measure is therefore not claimed.

A future route would have to prove that an appropriately defined connected
current-polymer activity has a multiplicative repetition law or a determinant
representation. Only then would a cycle zeta function become more than
notation.

Issue #1193 is a different arithmetic construction in which the Möbius
function is already an input. It is neither evidence for nor a dependency of
the current prime gate.

## 9. Status

- local prime gate, five-of-six theorem, cycle decomposition and homology
  cancellation: **candidate-T**;
- finite checks of the explicit \(n_{D_s}\) family: **candidate-C**;
- physical selection of \(p=5\): **not claimed**;
- full-current moment, full \(\Xi_L\), \(P1\), massless phase and physical
  photon: **open**.
