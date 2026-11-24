# PREREG: C-PHOTON-REPLICA-COMPLETION-BOUND-N

**PUBLIC, NON-CANONICAL. No Canon authority.**
Author: A. M. Thorn <thorn@twistj.com>
Date: 26 September 2026
License: Apache-2.0
Owner issue: #1164
Branch: `notes/photon-replica-completion-20260926`

## 1. Frozen public basis

Public Canon v92 is the only authority.

- activation commit and tag target: `8b1132d828d94f83e653dab34d686a7e68394939`
- content commit: `d7eb6de16c11f6a105996de02ffd7afa32683a93`
- Canon SHA-256: `31783fcd8e5ad2a697efd92a6d9fb92c2a21c101b95b9c282ea50fa7cb245f68`
- Canon bytes: `797365`
- starting candidate proof: PR #1163, commit `0c534baaf1db715961fde93e125f00c9d7436ca8`,
  `notes/C-PHOTON-BCHI-DIRECT-BOUND-N/REPLICA-WIRING.md`

No file under `canon/`, `probes/`, `tools/` or `.github/` is changed by this item.

## 2. One scoped question

The two-replica representation of #1163 permits opposite pairs and multiple
five-blocks at one edge. This item asks whether the representation can be
replaced by a **charge-faithful local projector** in which the only non-pair
block is one equal-sign block of size five or ten, so that the auxiliary
charged block at an edge is present exactly when the actual replica-current
difference at that edge is nonzero.

The second question is then forced: after the exterior unsigned wiring is
fixed, does the exact completion law retain any universal one-step contraction
strictly below one, or can an admitted exterior/support completion force
connection with conditional probability one?

This is an L6 finite-measure question only. There is no L4-to-L6 lift, no
thermodynamic-limit interchange, no physical photon claim and no P1 closure.

## 3. Frozen measure and variables

For even finite torus size `L >= 4`, use exactly the measure already frozen in
#1163:

`
mu_L(n) = Z_L^-1 product_p w(n_p) 1{partial n = 0 mod 5},
n_p in {-1,0,1}, w(0)=1, w(+1)=w(-1)=1/2,
j = partial n/5.
`

For two independent copies put

`
s = n1+n2, d=n1-n2, a=|d|.
`

The face table and inverse are those of #1163. Every active face carries one
sign variable `x_p` with `d_p=a_p x_p`; if `a_p=2`, both distinguishable
tokens of the face carry that same sign.

## 4. Frozen charge-faithful local rule

At one edge let `m=sum a_p <= 12` be the number of labelled tokens and let
`z_t in {+1,-1}` be their incidence signs.

A local partition contains opposite-sign pairs and **at most one** equal-sign
block of size

`
h in {0,5,10}.
`

If `h>0`, every token in that block must have the same incidence sign.
Write

`
r=(m-h)/2.
`

Every individual labelled-token partition of this type receives weight

`
lambda(m,h) = 1 / ( C(r+h,h) r! ).
`

The intended exact projector is

`
sum_{compatible partitions pi} lambda(m,h(pi))
 = 1{ sum_t z_t = 0 mod 5 }.
`

For an admissible sign assignment,

`
h = |sum_t z_t| in {0,5,10}
`

and therefore the non-pair block has charge

`
q = (sum_t z_t)/5 in {0,+-1,+-2}.
`

The proposed representation is charge-faithful iff an edge has a size-five or
size-ten block exactly when the actual difference current at that edge is
nonzero, with block size `5|q|`.

## 5. Frozen exterior completion law

Fix the face data `(s,a)` and all unsigned wiring except at one target edge.
Let `G_ext` be the resulting signed-relation graph on active face signs.

For a candidate local partition `pi`, let

- `consistent(G_ext,pi)` mean the combined signed relations admit a face-sign
  assignment;
- `k(G_ext union pi)` be the number of sign components after adding `pi`.

The exact conditional mass to be tested is proportional to

`
1{consistent} * 2^(k(G_ext union pi)) * lambda(m,h(pi)).
`

No local `lambda` is interpreted as an independent transmission
probability. The component-count factor is part of the frozen test.

## 6. Frozen route condition

The proposed uniform conditional-thinning route is:

`
there exists q_* < 1 such that every admitted target-edge conditioning
has conditional probability of the charged/continuing completion <= q_*.
`

It is **refuted at this declared scope** if one admitted finite completion
family has exact conditional probability one for the relevant charged
connection at arbitrarily large declared separation.

Such a refutation does **not** imply failure of unconditional decay,
`Xi_L`, `Xi_L^(2)`, the photon phase or P1.

## 7. Prospective exact audit

The verifier committed with this file is frozen before its first scientific
execution. Static parsing or byte inspection is not a scientific run.

The first scientific run must use Python standard library only and exact
integer/Fraction arithmetic. No random numbers, fitting, floats or external
data are admitted.

It must check:

1. **Face bijection.** All nine ordered ternary replica-face pairs, exact
   weights and inverse map.
2. **Actual star census.** Enumerate all 153 one-copy six-face edge stars with
   sum divisible by five and all 23,409 ordered replica-star pairs. Verify the
   possible difference-current magnitudes and token counts.
3. **Charge-faithful projector.** Independently enumerate all labelled
   pair/one-block partitions for `m=0,...,12`; enumerate all `2^m` sign
   assignments. Every compatible weighted sum must equal the modulo-five
   indicator. Expected totals are 18,862 partitions, 8,191 sign assignments
   and 1,719 admissible assignments.
4. **Exterior completion law.** Enumerate signed set-partition relations for
   up to six tied face signs and every amplitude pattern with entries one or
   two. Compare the partition-derived conditional masses with direct sign
   enumeration. The maximum conditional charged fraction is recorded exactly.
5. **Gluing fixtures.** Check at least three multi-edge relation fixtures and
   all face covariance entries against direct sign enumeration.
6. **Four-cup finite complex.** Reproduce the 53-state exact finite complex,
   all 2,809 ordered replica pairs and 441 covariance entries.
7. **Arbitrarily long torus witness family.** For `D in {3,4,5,8,13}`,
   construct two separated current loops joined by the neutral tube already
   used in the photon notes. Verify exact closure, connected support,
   five-face current junctions with doubled replica tokens, deterministic
   auxiliary connection, constant axial quotient and separation-dependent
   support size.
8. **One-edge budget cross-check.** Recompute the already-derived exact
   single-edge current upper bound `31250/208397` and the independent
   two-replica disagreement polynomial as a consistency check only.

## 8. Frozen pass and failure conditions

PASS requires every exact assertion in `verify.py` to succeed, exit code
zero and empty stderr.

Any assertion failure, exception, timeout, nonzero exit or nonempty stderr is
a failed first audit. It is preserved. The source is not silently edited and
rerun as the same first audit.

The finite audit can earn at most **candidate-C**. Written algebra derived from
the frozen definitions can be labelled **candidate-T** only as a
NON-CANONICAL proof pending separate review.

## 9. Interpretation boundaries

Even a PASS establishes only the finite algebra and the declared route
decision. It does not establish a uniform bound on either current moment, an
infinite-volume connection estimate, profile existence, rotational
restoration, spectral transfer, a massless phase, a physical photon or P1.

A fired conditional-thinning route is retained as negative progress. The next
valid route would have to use an unconditional weighted estimate, a signed
quotient estimate, or another preregistered mechanism that does not assume
uniform contraction after arbitrary admitted conditioning.
