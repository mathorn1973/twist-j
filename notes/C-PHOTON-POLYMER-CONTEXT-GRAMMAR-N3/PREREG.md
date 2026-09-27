# PREREG - C-PHOTON-POLYMER-CONTEXT-GRAMMAR-N3

**Status:** PUBLIC, NON-CANONICAL successor. No Canon authority.
**Owner:** A. M. Thorn / photon-polymer-context3-20260927
**Date:** 2026-09-27
**Issue:** #1206
**Target line:** PUBLIC
**Action layer:** L6 finite-measure neutral-surface combinatorics.
**Authority:** Public Canon v92. Normative files remain unchanged.

## 1. Consumed predecessors

#1172 and #1173 are consumed by incomplete first executions. Each produced no
scientific stdout within its frozen 45-second runtime and therefore earned no
mathematical conclusion.

This successor does not rerun either pin. It creates a new identifier and a
fresh public preregistration plus verifier before any result-bearing execution.

The mathematical object, state definition, transition, grid, caps, candidate
y values and decision grammar below are intentionally identical to #1173.
Only the identifier, custody and execution opportunity are new.

## 2. Face-simple tree activity

A face-simple tree consists of distinct elementary 3-cubes whose
face-intersection graph is exactly a tree and whose shared plaquettes are
distinct tree edges.

With coherent orientation, a tree of \(k\) cubes has exactly

\[
A(k)=4k+2
\]

ternary integer-closed boundary plaquettes.

The exact closed-pattern deletion inequality gives for either global
orientation

\[
\mu_L(+\partial C\ \text{or}\ -\partial C)
\le
2^{1-A(k)}
=
\frac12\,16^{-k}.
\]

The question is whether the exact context grammar below sums every rooted
face-simple cube tree against the activity \(16^{-k}\).

## 3. Exact normalized context state

A state is

\[
(parent,current,uncles).
\]

Requirements:

- parent and current are adjacent elementary 3-cubes sharing one plaquette;
- uncles are exactly the other children selected by parent in the previous
  generation;
- those siblings are pairwise plaquette-disjoint;
- normalize only by translating the base point of current to the origin;
- do **not** quotient rotations, reflections or axis permutations.

A root-generated state may have at most five uncles. Every later state has at
most four because the parent interface is unavailable.

## 4. Transition

For one normalized state:

1. find the unique parent-current interface plaquette;
2. enumerate the three neighboring 3-cubes across each of the other five
   current faces, giving 15 raw child candidates;
3. delete every child sharing a plaquette with any uncle;
4. enumerate every pairwise plaquette-disjoint sibling set \(V\) of the
   survivors, including the empty set;
5. for every \(d\in V\), create the normalized next state
   \((current,d,V\setminus\{d\})\);
6. the transition monomial is the product of the variables of those next
   states.

Grandparent and all older ancestors are deliberately forgotten. Dropping those
collisions enlarges the class, so the grammar is an upper count for actual
face-simple trees.

## 5. Root

Fix root \(c_{012}(0)\). It has exactly 18 candidate children, three across
each face. Enumerate every independent sibling set. The exact root monomial
list is retained, not collapsed to a scalar type count.

## 6. Frozen closure and certificate protocol

State cap:

\[
20000.
\]

Start from every root-generated state and close under the exact transition.
Any attempted state beyond the cap is an audit failure.

Physical cube activity:

\[
x=1/16.
\]

For an exponential tail test use

\[
z=y/16.
\]

Dyadic grid:

\[
Q=2^{18}.
\]

For every state coordinate, start at zero and iterate the exact upper-rounded
map

\[
q^{(n+1)}=\lceil F_z(q^{(n)})\rceil_Q.
\]

Frozen maximum iterations per \(y\): 256.

Frozen maximum represented coordinate: 8.

Frozen \(y\) values, largest first:

\[
17/16,\ 33/32,\ 65/64,\ 129/128,\ 257/256,\ 513/512,\
1025/1024,\ 1.
\]

No grid refinement, quotient, cap increase or threshold change is allowed.

## 7. Decision grammar

**PASS**: an exact fixed supersolution exists for some frozen \(y>1\).

Then, with exact root bound \(H\),

\[
\sum_{k\ge R}N_k16^{-k}
\le
y^{-R}H,
\]

and the corresponding rooted probability is at most one half of this.

**FINITE_ONLY**: no \(y>1\) certificate, but \(y=1\) reaches an exact fixed
supersolution.

**NONE**: no frozen attempt reaches a fixed supersolution under the declared
limits.

NONE rejects only this certificate protocol. It is not a theorem that the
true embedded tree sum diverges.

Any exception, assertion failure, cap overflow, nonzero exit, nonempty stderr
or timeout is an execution failure with no scientific conclusion.

## 8. First scientific execution contract

The complete verifier is committed and publicly read back before execution.

The first scientific execution has a hard wall-clock budget of exactly
45 seconds. The shell runner must terminate the process at that budget.

The intended execution system is an aarch64 connected runner. Its speed is
not part of the scientific statement. No result may use a longer budget.

## 9. Verifier obligations

The verifier must:

- derive cubical incidence from integer coordinates;
- verify four incident 3-cubes per plaquette and the 18-candidate root;
- enumerate every exact root independent sibling set;
- construct and normalize every root-generated state;
- close the state graph under the cap;
- enumerate every exact transition and next state;
- recheck every state and transition invariant after closure;
- report state count, root monomial count, transition monomial count,
  maximum uncles, survivors and children;
- run only the frozen dyadic iteration protocol;
- verify a fixed vector against the exact unrounded map;
- evaluate the exact root bound for a certificate;
- print the explicit scope boundary.

Python standard library only. No float, random number, external data, adaptive
quotient or post-result parameter change.

## 10. Scope boundary

Even PASS covers only the exact face-simple neutral cube-tree grammar.

It does not cover:

- cube complexes with face-intersection cycles;
- arbitrary neutral plaquette surfaces;
- charged endpoint gluing;
- current-component size or R3;
- Xi;
- P1;
- the massless phase or physical photon.

## 11. Repository boundary

Only \`notes/C-PHOTON-POLYMER-CONTEXT-GRAMMAR-N3/\` may be added.

No Canon, Registry, Frontier, formal probe, gate, tool, workflow, release or
existing note may be changed.
