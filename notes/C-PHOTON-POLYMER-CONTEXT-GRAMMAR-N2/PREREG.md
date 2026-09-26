# PREREG: C-PHOTON-POLYMER-CONTEXT-GRAMMAR-N2

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1173
Branch: `notes/photon-polymer-context2-20260926`

## 1. Basis

Public Canon v92 is the only authority.

- activation/tag target:
  `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit:
  `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256:
  `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`

Non-canonical motivation only:

- #1168 / draft PR #1169: sibling-only scalar majorant is supercritical.
- #1170 / draft PR #1171: uncle-count coefficientwise-max majorant is
  supercritical; its exact census exhibits 1,830 distinct filtered child graphs.

Neither draft is Canon and neither is silently promoted here.

## 1A. Consumed predecessor and implementation-only successor

The predecessor #1172 is consumed by its incomplete first execution at pin
`b7ccd0f945752ce34f35b1873ce19724d1d09af2`: no stdout or stderr was produced
within 45 seconds and the process was explicitly terminated. No scientific
result was earned.

This successor preserves every scientific definition, state, transition,
normalization, grid, y-list and cap below. It may change only exact
implementation strategy: memoization of pure geometric functions, cached
transition monomials, compact immutable keys, and exact bitmask operations.
No rotation/reflection quotient, context merging, coefficientwise maximum or
scientific threshold change is allowed.

The first scientific execution has a fixed 45-second budget. Timeout consumes
this successor audit and yields no mathematical conclusion.

## 2. The face-simple tree activity

For a face-simple tree of `k` elementary 3-cubes, coherent orientation
cancels its `k-1` tree-interface plaquettes and leaves exactly

`
A(k)=4k+2
`

ternary integer-closed boundary faces.

The exact deletion identity already present in the photon notes gives the
absolute union price for each deterministic boundary and its global reversal:

`
mu_L(+partial C or -partial C)
 <= 2^(1-A(k))
 = (1/2)16^(-k).
`

The only question here is whether a more faithful finite geometric grammar
sums all rooted face-simple cube trees against `16^(-k)`.

## 3. Exact context state

A state is the normalized exact tuple

`
(parent, current, uncles).
`

Here:

- `parent` and `current` are elementary 3-cubes sharing exactly one
  plaquette;
- `uncles` are precisely the other children selected by `parent` in the
  previous generation;
- those previous siblings are pairwise plaquette-disjoint;
- normalization translates the base point of `current` to the origin;
- rotations, reflections and axis permutations are **not** quotiented.

A root-generated state may have five uncles because the root has six faces.
Every later state has at most four uncles because one parent-interface face is
unavailable.

No coefficientwise maximum over states is taken.

## 4. State transition

For one exact normalized state:

1. Find the unique plaquette shared by `parent` and `current`.
2. Enumerate the three neighboring 3-cubes across each of the other five
   current faces, giving 15 raw child candidates.
3. Delete each raw candidate whose boundary shares any plaquette with any
   uncle.
4. On the survivors, choose **every** independent sibling set `V`, where
   independence means the chosen child cube boundaries share no plaquette.
5. For each `d in V`, create the normalized next state
   `(current,d,V\{d})`.
6. The transition monomial is the product of the next-state variables for all
   `d in V`; the empty sibling set contributes one.

Grandparent, great-grandparent and every older ancestor are forgotten at the
transition. Collisions with them are therefore dropped, so this grammar remains
an upper count for actual face-simple trees.

## 5. Root transition

Fix `c_012(0)` as root. It has 18 exact child candidates, three across each
of six faces. Enumerate every independent sibling set, including the empty
set. For each selected child create the normalized state whose uncles are the
other selected root children.

The root polynomial is not replaced by a scalar or type count; it is retained
as its exact list of context-state monomials.

## 6. Frozen state closure

Starting from all root-generated states, repeatedly apply the transition above
until no new normalized state appears.

Frozen state cap:

`
20000.
`

If a new state would exceed the cap, the verifier fails the audit. It must not
truncate the state set and call that a scientific result.

The verifier must check every state invariant and every transition target
again after closure.

## 7. Exact upper-rounded certificate

Let the closed state set be `S`. For `s in S`, let

`
F_s(q;z)
`

be the exact sum of all transition monomials, multiplied by cube activity
`z`.

The physical activity is `x=1/16`. To obtain an exponential tail test

`
z=y/16.
`

Use the fixed dyadic grid

`
Q=2^18.
`

For each frozen `y`, start from the zero integer vector and iterate

`
q_int^(0)=0,
q_int^(n+1)=ceil_Q(F(q_int^(n)/Q;z))*Q
`

componentwise, implemented directly as exact integer ceiling in units of
`1/Q`.

Equivalently, each stored coordinate is the integer numerator in units
`1/Q`. No floating point occurs.

If

`
q_int^(n+1)=q_int^(n),
`

then the represented rational vector satisfies `F(q;z)<=q` exactly and is
a rigorous componentwise supersolution.

Frozen candidate `y` values, largest first:

`
17/16,
33/32,
65/64,
129/128,
257/256,
513/512,
1025/1024,
1.
`

Frozen limits for each `y`:

`
maximum iterations: 256,
maximum coordinate: 8.
`

If a coordinate exceeds 8, stop that `y` attempt and continue to the next
declared `y`. Do not enlarge the cap, iteration count or grid.

## 8. Positive consequence

If a fixed point is found at `y>1`, evaluate the exact root transition on
that rational vector. Call the resulting finite bound `H_bound`.

For the actual rooted tree-description counts `N_k`,

`
sum_(k>=R) N_k 16^(-k)
 <= y^(-R) H_bound.
`

Therefore

`
mu_L(exists rooted face-simple cube-tree boundary with k>=R)
 <= (1/2) y^(-R) H_bound.
`

A fixed point only at `y=1` certifies finite total activity for this grammar,
but no exponential margin from this audit.

## 9. Exact verifier obligations

Before the first scientific execution, commit and publicly read back this file
and `verify.py`. Static compilation is allowed; a scientific run is not.

The run must:

1. derive every cubical incidence from integer coordinates;
2. verify four incident 3-cubes per plaquette and the 18-candidate root;
3. enumerate every exact root independent sibling set;
4. construct and normalize every root-generated context state;
5. close the exact context state graph without exceeding 20,000 states;
6. enumerate every exact transition sibling set and every next state;
7. verify all state and transition invariants after closure;
8. record state count, root monomial count, transition monomial count,
   maximum uncles, maximum surviving candidates and maximum children;
9. run only the frozen upper-rounded iteration protocol;
10. verify any fixed vector against the unrounded exact map;
11. evaluate the root bound exactly when a certificate exists;
12. print the explicit scientific boundary.

No float, random number, external library, external data, fitted threshold,
adaptive state quotient or post-result grid change is admitted.

## 10. Decision rules

- `CONTEXT_GRAMMAR_CERTIFICATE PASS`: a fixed exact supersolution exists for
  some frozen `y>1`.
- `CONTEXT_GRAMMAR_CERTIFICATE FINITE_ONLY`: no `y>1` certificate, but
  `y=1` reaches an exact fixed supersolution.
- `CONTEXT_GRAMMAR_CERTIFICATE NONE`: no frozen attempt reaches a fixed
  supersolution under the declared iteration and coordinate limits.

`NONE` is a negative result only for this certificate protocol. It is not a
divergence theorem unless a separate analytic argument proves divergence.

Any assertion failure, state-cap overflow, exception, nonzero exit or nonempty
stderr is an audit failure, not a scientific verdict.

## 11. Scope boundary

Even `PASS` covers only face-simple cube trees under the context grammar.
It does not cover:

- cube complexes with face-intersection cycles;
- arbitrary neutral plaquette surfaces;
- charged endpoint gluing;
- the full two-replica connection kernel;
- uniform `Xi_L` or `Xi_L^(2)`;
- profile existence or limit exchange;
- a massless phase, physical photon, apparatus or P1.

No Canon, Registry, Frontier, formal probe, tool or workflow file changes.
