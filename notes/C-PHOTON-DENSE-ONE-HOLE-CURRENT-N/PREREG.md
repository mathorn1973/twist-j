# PREREG - C-PHOTON-DENSE-ONE-HOLE-CURRENT-N

**Status:** PUBLIC, NON-CANONICAL incubation. No Canon authority.
**Owner:** A. M. Thorn / photon-dense-one-hole-current-20260927
**Date:** 2026-09-27
**Issue:** #1204
**Action layer:** L6 exact finite-volume current/component mathematics.

## Frozen family

Let \(L\ge4\) be even and use the periodic four-torus
\((\mathbb Z/L\mathbb Z)^4\), coordinates
\(x=(x_0,x_1,x_2,x_3)\).

For \(y=(x_1,x_2,x_3)\), define

\[
\sigma(y)=(-1)^{x_1+x_2+x_3}.
\]

In the three-dimensional cross-section graph, define the set \(P\) of
\(e_1\)-edges based at \(y\) satisfying

\[
x_1\equiv x_2\pmod2.
\]

G1 will prove that \(P\) is a perfect matching.

Define the ternary plaquette field \(n_L\), independent of \(x_0\):

\[
n_{02}(x)=n_{03}(x)=\sigma(y),
\]

\[
n_{01}(x)=
\begin{cases}
0,&(y,y+e_1)\in P,\\
\sigma(y),&\text{otherwise},
\end{cases}
\]

and all purely spatial plaquettes vanish.

## G1. Perfect matching and connected complement

Prove:

1. every cross-section vertex is incident to exactly one edge of \(P\);
2. the graph \(G=(\mathbb Z/L\mathbb Z)^3\setminus P\) is connected.

For connectivity it is enough to give an explicit route: all \(e_2,e_3\)
edges remain, and by toggling \(x_2\) parity when necessary one can make the
next desired \(e_1\) edge belong to the complement.

## G2. Exact boundary and current

With the standard cubical orientation, prove

\[
\partial n_L(e_0(x))=5\sigma(y)
\]

for every \(e_0\)-edge, and

\[
\partial n_L(e_i(x))=0,\qquad i=1,2,3.
\]

Hence

\[
j_L:=\partial n_L/5
\]

is unit current on every \(e_0\)-edge:

\[
j_L(e_0(x))=\sigma(y),
\qquad
j_L(e_i(x))=0.
\]

Therefore

\[
M_L=|{\rm supp}\,j_L|=L^4.
\]

## G3. Zero homology

Every cross-section strand winds once in the \(e_0\) direction, with sign
\(\sigma(y)\). Since \(L\) is even,

\[
\sum_{y\in(\mathbb Z/L\mathbb Z)^3}\sigma(y)=0.
\]

Therefore the total winding vector of \(j_L\) is zero.

## G4. Exact face count

All \(02\) and \(03\) plaquettes are occupied, contributing \(2L^4\).

At each fixed \((x_0,x_2,x_3)\), exactly half of the \(L\) possible \(01\)
plaquettes are deleted by the matching rule. Thus

\[
A_L=|{\rm supp}\,n_L|
=
2L^4+\frac12L^4
=
\boxed{\frac52L^4}.
\]

Consequently

\[
\boxed{\frac{A_L}{M_L}=\frac52}.
\]

## G5. Edge degrees and one augmented component

Prove:

- every \(e_0\)-edge has exactly five occupied incident plaquettes, all signed
  incidences aligned, hence is charged degree five;
- a spatial edge corresponding to a missing matching face has degree zero;
- every other occupied spatial edge has exactly two incident faces with
  opposite signed incidence, hence is neutral degree two.

Thus every neutral matching is unique.

The face-link graph is connected because neutral degree-two links join each
cross-section edge-strip through all \(x_0\), while charged \(e_0\)-junctions
join the five nonmatching cross-section edges incident to a vertex. This face
graph has the same connectivity as the incidence graph of the connected
cross-section complement \(G\).

Hence the entire support is one augmented component \(K_L\), with

\[
M_{K_L}=L^4,
\qquad
A_{K_L}=\frac52L^4,
\qquad
z(K_L)=2^{1-(5/2)L^4}.
\]

## G6. Exact signed axial cancellation

For the \(01\) signed slice used in the \(\chi_{00}(te_1)\) channel,

\[
B_{K_L}(r)
=
\sum_{x:x_1=r}j_L(e_0(x)).
\]

Since

\[
j_L(e_0(x))=(-1)^{r+x_2+x_3}
\]

and the sums over \(x_2,x_3\) cancel at even \(L\),

\[
\boxed{B_{K_L}(r)=0\quad\forall r.}
\]

A cyclic primitive is therefore constant and

\[
\boxed{\ell_{K_L}=0.}
\]

## G7. Arbitrary looseness of the R3 size majorant

For this one component,

\[
\frac{M_{K_L}^4}{4L^4}
=
\boxed{\frac{L^{12}}4},
\]

while its exact \(\ell_K^2/L^4\) contribution is zero.

This does not prove that the ensemble expectation \(R_3(L)\) grows. It proves
only that \(M_K\) can be arbitrarily large while the signed infrared slice
cost is exactly zero. Therefore a bound through \(M_K\) can be arbitrarily
loose on individual exact configurations.

## G8. Route boundary

The family is a counterexample to any universal support inequality

\[
A_K\ge c M_K
\]

with \(c>5/2\).

It is not a counterexample to the exact generic floor \(A_K\ge5M_K/4\), and it
does not prove \(5/2\) is optimal.

The result is a route-selection theorem only: future P1 work should preserve
signed current cancellation whenever possible rather than replacing
\(\ell_K\) by component size alone.

## Audit

Only after this preregistration is committed and publicly read back, a
standard-library exact verifier may audit the complete construction at

\[
L\in\{4,6,8,10\}.
\]

It must check the matching, complement connectivity, support size, integer
boundary, current, zero homology, degree census, unique neutral matching,
one-component connectivity, every \(B(r)=0\), and the exact displayed
\(L^{12}/4\) majorant value.

Finite execution is candidate-C only. The all-even-\(L\) result rests on the
written proof.

## Falsifiers

Any exact counterexample to G1-G7 at the stated family fires the corresponding
candidate. A smaller \(A/M\) family elsewhere does not falsify this result.

## Repository boundary

Only \`notes/C-PHOTON-DENSE-ONE-HOLE-CURRENT-N/\` may be added.

No Canon, Registry, Frontier, formal probe, gate, tool, workflow, release or
existing note may be changed.
