# Charge-faithful replica wiring and the failure of uniform conditional thinning

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-T written derivation plus candidate-C one-architecture exact audit.
Owner: #1165.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.
Basis: Public Canon v92.

This note is the successor to the consumed failed audit #1164. The predecessor
failed only because one auxiliary gluing fixture had no admissible sign
assignment. Its pin and failed output remain preserved. The successor freezes a
single corrected fixture before execution and leaves the scientific question
unchanged.

The result is deliberately narrow:

1. the full two-replica measure admits a positive **charge-faithful** local
   wiring in which every nonzero replica-current difference is represented by
   exactly one equal-sign block of size five or ten;
2. after forgetting signs, the exact target-edge completion law contains the
   component-count factor `2^k`;
3. no universal conditional transmission constant `q_*<1` can hold over all
   admitted support/exterior conditionings of this representation;
4. this does **not** bound the unconditional current moment uniformly and does
   not close P1.

## 1. Local charge-faithful projector

Retain the two independent original replicas and put

`
s=n1+n2, d=n1-n2, a=|d|.
`

At one edge, each incident active face contributes `a_p` distinguishable
tokens, all tied to one face sign. Let

`
m=sum_p a_p <= 12
`

and let `z_t in {+1,-1}` be the incidence sign of each token.

Allowed blocks are:

- opposite-sign pairs;
- at most one equal-sign block of size `h=5` or `h=10`.

Include `h=0` for an all-pair partition. Put

`
r=(m-h)/2.
`

Each individual labelled partition has weight

`
lambda(m,h)=1/(binom(r+h,h) r!).
`

### Candidate-T local identity

For every token-sign assignment,

`
sum_(pi compatible) lambda(m,h(pi))
 = 1{sum_t z_t = 0 mod 5}.                         (1)
`

**Proof.** Suppose the assignment has `p` positive and `q` negative
tokens. Any compatible pair contributes zero to the signed sum and the one
large block contributes `+h` or `-h`. Hence compatibility implies
divisibility by five.

Conversely, because `m<=12`, an admissible assignment has

`
h=|p-q| in {0,5,10},
r=min(p,q).
`

Assume `p=r+h`, `q=r`; the reversed case is identical. Choose the `h`
majority tokens in the large block and pair the remaining `r` majority
tokens with the `r` minority tokens. The number of compatible labelled
partitions is exactly

`
binom(r+h,h) r!.
`

Multiplying by `lambda(m,h)` gives one. This proves (1).

The same proof gives the charge-faithful statement. If

`
q_e=(sum_t z_t)/5,
`

then

`
h=5|q_e|.
`

Thus a large block exists iff the actual replica-current difference at the
edge is nonzero. Magnitude-one difference uses one five-block; magnitude-two
difference uses one ten-block.

## 2. Full unsigned representation

For fixed face data `(s,a)`, choose one local partition at every edge and
then forget the face signs. The partition relations induce a signed graph on
the active faces. Inconsistent structures have zero mass. For a consistent
structure `T`, let `k(T)` be the number of sign components.

Exactly as in the full-replica construction of #1163, summing the independent
component signs gives

`
w2(T)=2^k(T) product_p omega(s_p,a_p)
              product_e lambda(m_e,h_e).                   (2)
`

Equation (1) reconstructs each admissible replica pair with total local wiring
mass one at every edge. Therefore the total partition sum of (2) is exactly

`
Z_L^2.
`

Conditional on a consistent unsigned structure, its component signs are
independent and uniform.

This is a replacement of the local wiring, not a change of the original
replica measure.

## 3. Exact exterior completion law

Fix the face data and all unsigned wiring away from a target edge `e`. Let
`G_ext` be the resulting signed-relation graph. For each candidate local
partition `pi`, define

`
k_pi = k(G_ext union pi).
`

All factors in (2) not involving the target edge cancel. Hence

`
P(pi | exterior, s, a)
 =
  1{consistent(G_ext,pi)} 2^k_pi lambda(m,h(pi))
  -------------------------------------------------.       (3)
  sum_pi' 1{consistent(G_ext,pi')} 2^k_pi' lambda(m,h(pi'))
`

The factor `2^k` is compulsory. Treating `lambda` alone as an independent
transmission probability is wrong.

The exact finite audit enumerates every signed set-partition relation on up to
six incident face signs, every amplitude pattern with entries one or two, and
12,616 exterior-completion cases. In that frozen class, direct sign counting
and the partition law agree exactly. The maximal conditional charged fraction
is

`
1.
`

That finite fact already blocks a naive uniform conditional estimate, but the
following all-distance construction supplies the geometric reason.

## 4. All-distance deterministic connection

Use the explicit neutral-tube family already proved in
`CONNECTED-CURRENT.md`. For every integer `D>=3` it gives a ternary
two-chain `n_D` on an even torus with

`
|supp n_D| = 4D+40,
degree-five occupied edges = 8,
degree-two occupied edges = 8D+60,
`

two separated four-edge current loops, and a connected occupied-face graph.
All remaining edges are neutral degree-two seams.

Now take the replica pair

`
n1=n_D, n2=-n_D.
`

Then `s=0` and `a=2` on every occupied face.

### Neutral degree-two edge

There are two incident faces and four tokens, two from each face. Closure
forces the two face incidence signs to be opposite. Therefore `h=0`,
`r=2`. There are exactly two compatible labelled pairings, each of weight
`1/2`. Both pairings join the same two face vertices.

So the pair-label choice is random but the face connection is deterministic.

### Charged degree-five edge

There are five incident faces and ten tokens. Since the one-copy current has
magnitude one, all five incidence signs of `n_D` agree. For the replica
difference all ten token signs therefore agree. Hence

`
h=10, r=0.
`

There is exactly one compatible ten-block, of weight one, joining all five
face vertices.

### Consequence

Every compatible charge-faithful wiring has the same face-component
connectivity as the occupied support of `n_D`. That support is connected for
every `D>=3`. Thus the two separated marked charged blocks lie in the same
auxiliary component with exact conditional probability

`
P(connection | s=0, a=2 on supp n_D, empty exterior)=1       (4)
`

for arbitrarily large separation.

The event conditioned on in (4) is admitted and has positive finite-volume
weight. The two possible replica signings are the global reversals
`(n_D,-n_D)` and `(-n_D,n_D)`; both have the same unsigned connection.

Therefore the frozen route

`
exists q_*<1 bounding every admitted conditional continuation
`

is false.

## 5. What the no-go does not say

Equation (4) is a **conditional** statement. The conditioned support becomes
rare as `D` grows. Nothing here prevents its full-measure weight from
suppressing the unconditional covariance.

Accordingly, this result does not prove or disprove any uniform bound for

`
Xi_L
`

or

`
Xi_L^(2).
`

It also does not establish or refute exponential clustering, the massless
phase, a physical photon, rotational restoration or P1.

What it removes is one proof strategy: an exploration dominated solely by a
universal per-step conditional factor strictly below one after arbitrary
admitted support/exterior conditioning.

Any successful next estimate must retain the unconditional weight of the
explored support, exploit signed cancellation, or use another exact mechanism
that is not destroyed by the deterministic neutral-tube family.

## 6. Exact audit status

The successor verifier was frozen at

`
fdd1662ec3f828db20c9982a6821e12628863e55
`

before its first scientific execution.

One Linux x86_64 / Python 3.13.5 run passed with exact integer and
`Fraction` arithmetic, exit code zero and empty stderr. It checked:

- nine ordered replica-face pairs;
- all 153 allowed one-copy edge stars and 23,409 ordered replica-star pairs;
- 18,862 labelled local partitions;
- all 8,191 token sign assignments, 1,719 admissible;
- 12,616 exterior signed-relation completions;
- three multi-edge gluing fixtures and 101 covariance entries;
- the 53-state four-cup complex, all 2,809 replica pairs and 441 covariance
  entries;
- the deterministic tube witness at `D=3,4,5,8,13`;
- the exact existing one-edge current budget.

This is **candidate-C**, not a two-architecture gate. The all-`D` statement
above is a written **candidate-T** argument resting on the already published
all-`D` geometry in `CONNECTED-CURRENT.md`; it still requires separate
review before any public promotion.

Public Canon v92 is unchanged. P1 remains open.
