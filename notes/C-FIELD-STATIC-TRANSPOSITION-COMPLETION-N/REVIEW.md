# Separate static proof review

**NON-CANONICAL / NO AUTHORITY. Exposed assistant text review of conditional
candidate-T claims at L1.** This review assigns no computational status,
public gate result, physical interpretation, or promotion.

## 1. Verdict and exact reviewed texts

No substantive mathematical defect was found in T1--T7 at the exact text
versions below. The complete static-contact construction, its relative
maximality, its scoped energy-profile classification, and the new readout
counterexample are supported by the stated arguments. No proof correction
is required by this review.

| Reviewed file | SHA-256 |
|---|---|
| PREREG.md | `58b8e76488c0eda439407b8e52ee667dfb33ba7ffab6c88dada2a7f30c6470d1` |
| ADDENDUM-READOUT.md | `d9ada337b321f16659ead0ee0dcc76ae25efdc229f18ad4d24ef23e4cdc23320` |
| PROOF.md | `b6f389ed5b476fee7dc07aed939e599968b25e166fe3e350a854539cd86f6e34` |

The hashes were read from these actual local files during this review.
The verdict covers these three versions, not a later unreviewed revision.
PREREG.md is unchanged from the author's original specification pin. T7
is explicitly an additive claim in ADDENDUM-READOUT.md, rather than a
retroactive change to T1--T6.

## 2. Method and independence limits

The reviewer is the separate assistant context
`/root/readout_geometry_review`. This was a static mathematical review:
algebraic identities, complete branch logic, full-state equality, and the
two exact histories were checked by hand. Only text-reading, hash, and
review-file-writing operations were used for this review. No scientific
program, trial import, finite enumeration, or numerical audit was executed.

Neither the new verification programs nor any program stdout/stderr was
read. The user-supplied bundle's RESULT, PROMO and PREREG prose was read for
scope and provenance; its reported run results were not reproduced or
independently certified. Earlier PR #1424 mathematical prose was available
as context. The public authority bootstrap was performed by the parent
session; this review is not a separate repetition of that bootstrap.

This review is exposed, not blind. The reviewer discussed the construction
and its boundaries with the author before the proof was completed, supplied
the elementary +5 witness and guard-boundary observations, and suggested
the matter-projection argument used in T4. The author supplied the frozen
T7 histories; the reviewer separately checked every stated intermediate
state and account by hand. None of this constitutes external peer review,
independent discovery, implementation review, or two-architecture evidence.

## 3. Universal algebra and the complete carrier

The specification retains arbitrary integer cells with nonnegative stocks.
It does not silently restrict the construction to Gauss states, integral
splits, neutral matter, accepted reactions, or empty helper registers.

For T1, the simultaneous requirements `C^t d=0` and
`D d=rho'-rho` have a unique rational solution: the static space has
dimension two, and `D S_E` has rank two onto the zero-sum charge plane.
The three displayed vectors have the required divergences, are orthogonal
to C, and have squared norms 10, 15 and 15. Their unit-magnitude components
give the exact integrality condition `5 divides t`.

The static displacement leaves the rational active coordinate y unchanged,
even off the integral-split lattice. The energy calculation correctly drops
the mixed term because `k^t C M=0`, not because M is assumed zero. Thus the
price equals the difference of `EC(D E)` on all eligible raw states. On a
non-Gauss state the argument remains `D E`; it is not replaced by rho.
The full spectator energy is preserved by swapping complete registers.

The general proof of `F G=G F` in PROOF section 2 is sufficient. The raw F
inverse is integral, and A_f is the stated product of integer shears.
The displayed `A_f L=L A_f` product is correct. The energy identities give
both `H(A_f y)=H(y)` and `H(Lx)=5H(x)`. Hence F preserves integral splitting,
L-image admission in both directions, and reaction funding. Both accepted
reaction formulas commute with F, and all structural and funding rejections
remain rejected. The argument does not rely on the source bundle's fired
global uniqueness sentence.

## 4. Rejected branches and the acceptance filter

For T2 and T3, proposal reversal changes t to -t and the price to its
negative, returning the whole original cell. Legal proposal edges and
equality of their endpoint acceptance bits are symmetric. Thus the
performed edges are complete transpositions, while every refused input
is a literal full-state fixed point.

The G-commutation proof covers refusals rather than considering only
performed events. On a G-accepted input the four reserve values are

```text
r                 r-kappa
r+deltaG          r+deltaG-kappa.
```

Both rows are legal exactly when
`kappa <= min(r,r+deltaG)`, in addition to field integrality. At the G
partner the inverse reaction increment is `-deltaG`, so the same condition
is obtained. A negative proposed stock and a funded proposal with an
unfunded reaction corner are therefore rejected at both ends of the G
edge. The raw algebraic square commutes whenever it is performed.

On a G-rejected input, G is the identity. A performed contact is required
to have a G-rejected output; otherwise the whole contact is refused.
This covers nonliteral matter, nonintegral splits, failed R image admission,
failed funding, and both directions of acceptance mismatch. Actual G
acceptance is used throughout, including on non-Gauss inputs.

F fixes the static price and the relevant stock, commutes with the raw
proposal, and preserves both acceptance bits. Consequently its commutation
extends to the complete refusal rule. Since the contact fixes m and
preserves actual G acceptance, it also preserves e and commutes with
Ghat for every pointer value, without a reset assumption.

Acceptance equality is used together with the commuting raw formulas.
The proof correctly does not present this filter as a universal method
for making arbitrary operations commute.

## 5. Maximality and the energy family

T4 is proved for the actual frozen competitor class, including complete
competitors that are not assumed bijective. Every allowed competitor V
fixes m. Therefore `V G=G V` implies

```text
pi_m(G V s)=pi_m(V G s)=pi_m(G s),  pi_m(V s)=pi_m(s).
```

Since accepted G branches change between distinct literal matter endpoints,
this forces `aG(Vs)=aG(s)`. Each nonidentity proposal use must pass the
same filter as S_ij. S_ij uses every such proposal, so every competitor's
nonidentity support is contained in its support. Equality of greatest
supports fixes the same choice at every state where the proposal is not
already identity. The asserted maximum is therefore unique in this class.

This is neither a uniqueness theorem for all contacts nor a physical
principle requiring greatest support. The identity and smaller allowed
contacts are not excluded as physical possibilities by the mathematics.

For T5, parity is asserted only for integral proposals. The price of S01
is even; the S02 and S12 prices have the parity of `t/5`. Refusals have
zero actual price. The +5 witness has total cell energy 335, changes
stock from 7 to 2, and gives `Delta Hc=1-c`. Both completed laws therefore
require c=1, and universal H1 preservation gives sufficiency on the whole
carrier. This establishes exactly the declared profile-family result.
It is not an inference from a finite audit and does not independently
justify the H1-based reserve compensation.

The r=5 and r=6 examples correctly distinguish individually funded raw
proposals from G-compatible contacts. Their proposed R outputs have
stocks 0 and 1 and reject G, so the completed contact refuses. At their
G partners the proposal is unfunded. The stated nontrivial-F example
with AM, `y=(0,0,1,0)` and `M=(1,0)` is also consistent: it has H(y)=1,
and both +5 proposals remain accepted at their endpoints.

## 6. Separate manual check of both T7 histories

All quantities in ADDENDUM-READOUT.md were checked in the two actual
complete forward histories, not merely by assuming existence of inverse
images. The initial receiver fields have the following accounts:

| Quantity | X01 receiver | X12 receiver |
|---|---:|---:|
| Electric field | (-2,0,2,-3) | (1,3,1,1) |
| M | (0,0) | (0,0) |
| Rational active y | (-1,0,0,0) | (-1,0,0,0) |
| Static sigma | (-1,2) | (2,1) |
| H(y) | 2 | 2 |
| Static energy | 15 | 10 |
| Hraw | 17 | 12 |
| Spectator energy | 300 | 300 |
| AM energy | 20 | 20 |
| Initial receiver stock | 6 | 6 |
| Initial receiver H1 | 343 | 338 |

Both inputs are Gauss states. Their AM guards are exactly
`6+2-4*2=0`, so both reactions are genuinely accepted. Since
`L(-1,0,0,0)=(-1,3,0,-5)`, after G their receiver fields are
`(-5,0,5,0)` and `(-2,3,4,4)`, respectively, with `M=(0,-5)`, matter R,
and stock zero. The event bit is zero for this AM-to-R reaction.

The source stocks 81 and 86 pass through A and B to the receiver. Both
source stocks and the link become zero. Here `C(0,-5)=(5,0,-5,-5)`, so F
gives the two pre-contact electric fields `(0,0,0,-5)` and `(3,3,-1,-1)`.
For each field the magnetic update gives M=0, exactly as stated.

The first final contact is S01, with price zero and unchanged stock 81.
The second is S12, with price +5 and stock 86 becoming 81. Their rational
active coordinate is `(-1,-2,0,0)`, in L's image with
`x=(-1,0,2,-1)` and H(x)=2. The relevant R funding expressions are 87
and 92 before the two respective contacts and 87 at the common output;
all are nonnegative. Thus both final contacts pass their complete guards.
Each produces precisely the specified Y receiver, including its full
spectator registers, not just its energy or charges.

The final receiver has H1=424. Source, link and pointer agree throughout
the claimed final comparison, and both pointers remain zero. The complete
accounts are

```text
81 + 343 + 1 = 425,
86 + 338 + 1 = 425,
0 + 424 + 0 + 1 = 425.
```

The last receiver changes are consequently 81 and 86. No function of
the identical old final state Y can return both. The minimax absolute
error bound 5/2 follows directly from their separation of 5. Two extra
distinguishable values are necessary for this pair, and a retained,
available contact label suffices for the controlled two-law family by
its known inverse. This is an abstract code statement: the expanded
complete states differ in that label. Physical preparation, control,
energy accounting and readable access to the label are not obtained
from the counterexample or the abstract controlled bijection.

## 7. Boundaries retained by the proof

The incident-stock-swap counterexample is correct. With cell stock 7 and
link stock zero, contact then B gives changed field, cell stock zero and
link stock 2. B then contact leaves the original field, cell stock zero
and link stock 7 because the +5 proposal is unfunded. Commutation with G
and F is therefore not transferred to incident B or to the entire old
chain. Disjoint operations are a different case.

The source-alphabet statement is scoped to the same identified carrier
and to primitives and controller updates preserving the same actual node
charges. Finite adaptive composition cannot change those charges, whereas
the new witnesses do. This excludes an implementation by that old alphabet;
it does not exclude a broader source dynamics or derive one.

The comparison with the old prices 5 and 80 does not place the old
active-kick contacts inside this new static-proposal class. It supplies
additional admissible mathematical contact outcomes. The field work here
is a difference in the selected Hraw account, not an independently earned
physical unit or measured work law.

The supplied bundle's fired S3 and S4b remain fired. The separate correction
to the conjunction concerning Zdom correctly requires nonzero nu when
nonzero charge movement is asserted. No unrestricted uniqueness, physical
energy selection, native-U occurrence rule, operational instrument,
geometric metric, Hilbert coherence or full-model photon phase is established.

## 8. Disposition

The exact reviewed text is suitable to retain as a complete conditional
candidate-T argument with the stated boundaries. This is a scoped proof
review verdict, not a promotion or computation-grade certification.
Execution records, implementation correctness, finite audit results and
architecture requirements remain outside this review. Any later substantive
change to the three pinned texts requires a correspondingly identified
review update; this file must not silently certify such a change.
