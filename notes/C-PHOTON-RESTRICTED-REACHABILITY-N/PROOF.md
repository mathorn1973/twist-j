# Reachability of the two restricted finite-volume classes

**PUBLIC / NON-CANONICAL. Written proof candidate, candidate-T ceiling.**

- Item: C-PHOTON-RESTRICTED-REACHABILITY-N; claim issue #1267.
- Author: A. M. Thorn.
- Authority: Public Canon v92. This note changes no Canon claim.
- Parent definitions: `notes/C-PHOTON-TWIST-SNAKE-SECTOR-N/PROOF.md`,
  frozen at `fc16df1b06d971ca7ef4e2f35eab92d8b9637bdb` in PR #1266.
  That unmerged candidate is a definition source, not normative authority.
- Scope: connectivity of the exact, ideal mathematical single-link move
  graph at fixed finite L, k, n and class. This is not a statement about
  floating-point implementation, relaxation time or finite-run estimates.

## 1. Statement and conventions

Let L be even with L >= 4, let k be 1 or 2, and put m = L^2. Work on the
periodic four-dimensional lattice with link fields alpha in F_5^E. The
source k is placed on one 01-plaquette of each of the first n slices,
where 0 <= n <= m. Slices are indexed by their fixed (x_2,x_3) coordinates.
Write rep for the representative in {-2,-1,0,1,2}. On a twisted slice j,

\[
f_p=(d\alpha)_p+k1_{p=q_j},\qquad
s_j=\sum_{p\text{ in slice }j}\operatorname{rep}(f_p),\qquad
w_j=\frac{s_j-k}{5},\qquad W_n=\sum_{j<n}w_j.
\tag{1}
\]

The numerator defining w_j is divisible by five because the oriented
plaquette sum of d alpha vanishes in F_5 on each periodic slice. Define

\[
C_-(n)=\{\alpha:2W_n<-n\},\qquad
C_0(n)=\{\alpha:2W_n\ge -n\}.
\tag{2}
\]

A permitted elementary move replaces one link value by any value in F_5,
provided both endpoints of the move belong to the chosen class. The move
graph is undirected.

**Theorem [candidate-T].** For every stated L and k and every
1 <= n <= m, each of C_-(n) and C_0(n) is nonempty and its permitted
single-link move graph is connected. At n=0, C_0(0) is the entire link
space and is connected, while C_-(0) is empty.

Consequently, for every nonempty class the ideal restricted Gibbs sweep
that visits every link in a fixed order is irreducible and aperiodic and
has its class-restricted finite measure as its unique stationary law.
This consequence supplies no useful convergence rate.

## 2. Exact reduction to a bounded-height graph

On one 01-slice let G be its dual square torus. Its m vertices are the
01-plaquettes, and a dual edge joins the two plaquettes incident to each
primal 0-link or 1-link. For L >= 4 this is a connected graph without
self-loops. Choose the orientation of each dual edge so that changing its
corresponding primal link by delta changes the two incident fluxes by
-delta at its tail and +delta at its head. This is possible because a
primal link occurs with opposite signs in those two oriented plaquettes.
The slice curl map is thus the incidence map of G over F_5.

Set

\[
h_p=\operatorname{rep}(f_p)+2\in\{0,1,2,3,4\},\qquad
H=\sum_ph_p=5w+k+2m.
\tag{3}
\]

A single-link update is exactly a modular transfer between adjacent
heights:

\[
(h_u,h_v)\longmapsto
([h_u-\delta]_5,[h_v+\delta]_5),
\tag{4}
\]

where [ ]_5 takes values in {0,1,2,3,4}. Every such transfer lifts to a
single primal-link update. Its effect on plaquettes of other orientations
is immaterial to W_n. It does not change the 01-fluxes of another slice.

The image of the incidence map of a connected graph over F_5 is exactly
the space of vertex vectors whose sum is zero. For completeness, choose
a spanning tree and eliminate leaves: prescribe the flow on a leaf's
unique tree edge to meet the required divergence there, remove that leaf,
and continue. At the final vertex the remaining equation follows from
the zero total divergence. Therefore every height configuration with

\[
H\equiv k+2m\pmod 5
\tag{5}
\]

comes from a link field with the specified source.

The reduction (4) is a projection, not an identification of states:
different link fields may have the same heights. Section 4 explicitly
connects those fibers, including all gauge and noncontractible cycle
degrees of freedom.

## 3. Height transport and monotone reduction

**Lemma 1 [candidate-T, fixed-total transport].** On any finite connected
graph, the configurations h in {0,1,2,3,4}^V with a fixed integer total H
are connected by the moves that transfer one integer unit from a positive
height to an adjacent height smaller than four, without modular wrapping.

**Proof.** Fix a spanning tree and a target configuration b with total H.
Take a leaf v of that tree. If h_v > b_v, the remaining vertices contain
a vacancy: their total is smaller than their target total and hence
smaller than their total capacity. Find a vertex with height below four
at the shortest distance from v in the remaining tree. Every internal
vertex of that path is full. Move one unit from the predecessor of the
vacancy into it, and continue backwards along the path, ending by moving
one unit from v. Every transfer is allowed and h_v decreases by one.
Repeat until h_v=b_v.

If h_v < b_v, the remaining tree contains a positive height because its
total exceeds its target total. A nearest positive vertex has only zero
heights on the internal part of the path to v. Move one unit from that
vertex successively toward v; each recipient has room. Repeat until
h_v=b_v. Once the leaf matches, remove it from the working tree and never
change it again. Induction matches every vertex. These moves are also
the modular moves (4), with no wrap. QED.

**Lemma 2 [candidate-T, monotone sector descent].** Let
r be the representative of k+2m modulo five in {0,1,2,3,4}. Every
height configuration satisfying (5) can reach any prescribed height
configuration with total r along modular transfers whose total H never
increases. Dually it can reach any prescribed configuration with maximal
admissible total along a path whose total never decreases.

**Proof.** If H>r, then H>=5. Choose adjacent vertices u,v. A configuration
of total H with h_u=4 and h_v>=1 exists: reserve four units for u and one
for v, then distribute the remaining H-5 units within the remaining
capacity 4|V|-5. Lemma 1 reaches such a configuration without changing H.
Now transfer one unit from v to u modulo five. The pair (4,b), with
b>=1, becomes (0,b-1), decreasing H by exactly five. Repeat until H=r,
then use Lemma 1 to reach the prescribed configuration at that total.

For ascent apply this descent argument to the complementary heights
g_p=4-h_p. A modular transfer of g is a modular transfer of h with the
opposite orientation. Decreasing the total of g increases H. QED.

In terms of w, the extremal values on a twisted slice are therefore

\[
w_{\min}=\left\lceil\frac{-2m-k}{5}\right\rceil,
\qquad
w_{\max}=\left\lfloor\frac{2m-k}{5}\right\rfloor.
\tag{6}
\]

They are attained because of the incidence-map surjectivity in section 2.
Choose, once for each slice, a canonical minimum-height configuration and
a canonical maximum-height configuration. For example, put the entire
minimum residue r at one chosen vertex and zero at all other vertices;
for the maximum use the complementary construction. Choose any primal
link representative of each canonical configuration.

## 4. Connecting a curl fiber with at most one unit of excursion

**Lemma 3 [candidate-T, fiber connection].** Two slice link fields with
the same flux configuration can be connected by single-link updates such
that every intermediate slice integer w differs from its initial value
by at most one.

**Proof.** Their link-field difference corresponds on G to an F_5-valued
edge flow with zero incidence, since the source is the same. Such flows
are generated by simple cycles. To see this without a topological
assumption, fix a spanning tree. For each edge outside the tree, subtract
the appropriate multiple of its fundamental cycle, eliminating that
edge. The remainder is a divergence-free flow on the tree and vanishes
by leaf elimination. This includes noncontractible cycles of the torus;
no quotient by their circulations is taken.

Realize one simple-cycle circulation of value delta by updating its
edges successively in cyclic order. Before the cycle closes, every
internal vertex of the traversed path has received and lost the same
delta modulo five. Only its two distinct endpoints have altered heights.
The sum of these two new heights is congruent modulo five to the sum of
their two original heights. Each sum lies in [0,8], so their difference
belongs to {-5,0,5}. Thus H has changed by at most five and w by at most
one. On closing the cycle all heights return to their initial values.
Perform each generating cycle in turn. Between cycles the original
heights are restored, so the excursions do not accumulate. The total
edge-field difference is realized exactly. QED.

## 5. Connectivity of both classes

For m=L^2>=16 and k in {1,2}, equation (6) gives

\[
w_{\min}\le -6,\qquad w_{\max}\ge 6.
\tag{7}
\]

Start with any alpha in C_-(n), n>=1. Apply Lemma 2 on each twisted slice,
ending at that slice's canonical minimum-height configuration. Every
step weakly decreases W_n, so no step leaves C_-(n). At the end
W_n=n w_min. Apply Lemma 3 on one slice at a time to bring its primal
0- and 1-links to the chosen canonical representative. During all these
fiber connections,

\[
W_n\le n w_{\min}+1\le -6n+1<-\frac n2.
\tag{8}
\]

Thus the fiber steps also remain in C_-(n). All 2- and 3-links, and all
0- and 1-links of untwisted slices, do not enter W_n and can now be set
individually to fixed reference values. Every alpha in C_-(n) has reached
the same reference link field within the class. Reversing one such path
and concatenating it with another proves connectivity. The constructed
reference also proves nonemptiness.

For C_0(n) use monotone ascent to the maximum-height configurations.
No ascent step leaves C_0(n). During the subsequent fiber connections,

\[
W_n\ge n w_{\max}-1\ge 6n-1\ge -\frac n2.
\tag{9}
\]

Finish by setting the remaining unconstrained links to their reference
values. This gives the same connectivity and nonemptiness conclusion for
C_0(n). At n=0, W_0=0 by definition, so C_0(0) is the full link space and
C_-(0) is empty. This completes the graph-connectivity theorem. QED.

## 6. Consequence for the ideal Gibbs sweep

The exact plaquette weights are strictly positive:

\[
\mathcal W(0)=4,\qquad
\mathcal W(\pm1)=\frac{3+\sqrt5}{2}>0,\qquad
\mathcal W(\pm2)=\frac{3-\sqrt5}{2}>0.
\tag{10}
\]

Hence every permitted elementary replacement has positive probability in
the ideal class-restricted single-link conditional distribution. Keeping
the current link value also always has positive probability. An arbitrary
finite path in the permitted move graph can therefore be embedded in
full fixed-order sweeps: implement one chosen elementary move in a sweep
and keep every other link unchanged. Each prescribed sweep has positive
probability. Connectivity proves irreducibility of the sweep kernel.
Keeping every link unchanged gives a positive diagonal, hence aperiodicity.

Every individual conditional update preserves the class-restricted
finite measure; their composition preserves it as well. Finite-state
irreducibility gives uniqueness of the stationary distribution, and
aperiodicity gives convergence to it from every starting state. No
reversibility of the composed deterministic-order sweep is asserted.

## 7. Scope boundary

This is a written finite-volume candidate-T result about the ideal
mathematical kernel. It removes a connectivity obstruction for the exact
classes (2). It does not bound the time needed to traverse the paths, the
probability of doing so in any usable run length, the spectral gap, the
autocorrelation time, or the bias and interval coverage of a finite run.
It does not prove that a floating-point implementation realizes every
positive ideal transition. It does not show that a forced reset has
equilibrated after any specified number of sweeps.

In particular, the frozen `INCONCLUSIVE_EQUILIBRATION` disposition of the
parent run is unchanged. No sector-sum estimate is rehabilitated by this
proof. No thermodynamic lower bound, cancellation control in the full
measure, P1 closure or PHOTON-MASSLESS-PHASE conclusion follows. Public
Canon v92 is unchanged.
