# Native common-ready source retention

**Prospective proof; result exposed; L1 only.** Public issue
[#871](https://github.com/mathorn1973/twist-j/issues/871). This proof is frozen
with the joint preregistration and accepted verifier before formal execution.
It supplies no physical instrument, probability or Canon promotion.

## 1. Domain, input and inherited facts

Use unchanged U on `Omega=N_0 x F_5^6`, with the origin-zero Thue--Morse
driver. Write `x=(p1,p4,p1p,p4p,q,r)=(p,a)` and
`D_a={(p,a):p in F_5^4}` for a common ready `a=(q,r)`, independent of p.
F_n denotes the checkpoint after n ticks from `(0,x)`.

The readback input is the **complete current checkpoint and actual counter**
`(n,F_n(x))`, with the common ready known. It contains neither a separately
retained source nor an external early-history buffer. This is more access
than the native apparatus port `(q,r)` alone, whose inability to recover
quadratic source shape remains unchanged.

The registered U-NATIVE-CHART-AND-QDD-READBACK theorem and its
[proof, sections 1--5](../P-QDD-U-NATIVE-READBACK-1/PROOF.md) supply the
five involutive generators, origin-zero synchronization at tick three,
bijectivity of every later reachable-sheet transition, the conserved
five-label chart, and the first-three-tick maps H_z below. The registered
U-NATIVE-APPARATUS-HISTORY-FACTOR theorem and its
[proof, section 4](../P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md) already
supply the apparatus table below. The new deduction is its combination
with the full-sheet bijections, giving complete common-ready source
retention and an explicit source reader.

## 2. Complete classification of all 25 common readies

For every common ready a, the following are equivalent:

1. Every initial p can be recovered from `(n,F_n(p,a))` for every n.
2. F3 is injective on D_a.
3. `a` is outside `{(0,0),(3,0),(3,3),(1,3)}`.

For each of the 21 good readies, `|F_n(D_a)|=625` at every n. For each
exceptional ready, at every `n>=3`, the image has 500 states, comprising
125 fibres of size two and 375 singleton fibres.

**Proof.** All checkpoint arithmetic is in F5. The initial bits are 011.
Composition read right to left gives

```text
H0=eca, H1=d, H2=e, H3=dbd, H4=dbe.
```

Reading the last two coordinates gives the inherited complete table:

| Initial phase z | `(q3,r3)` |
| --- | --- |
| 0 | `(q+1,r+1)` |
| 1 | `(1-q,1-r)` |
| 2 | `(2-q,1-r)` |
| 3 | `(2-q,2-r)` |
| 4 | `(3-q,2-r)` |

The last four rows are pairwise distinct. The first equals rows 1,2,3,4
respectively only at `(0,0),(3,0),(3,3),(1,3)`: solve the two affine
equalities, using `2^{-1}=3` in F5. Thus each exceptional ready has one
coincident phase pair and three other distinct rows; every good ready has
five distinct rows.

For fixed z, `D_a intersect {sum(x)=z}` has 125 points. H_z is bijective
on the full initial phase sheet and hence injective on this subset. Its
image is contained in the set with total phase one and the fixed displayed
`(q3,r3)`. This latter set also has 125 points, because its four pistons
have one specified sum. The image therefore equals that whole set.
Distinct table rows give disjoint output sets; the coincident pair gives
the same set with exactly two preimages per point. This proves the counts
and equivalence of (2) and (3).

Later reachable-sheet bijections preserve this partition. Earlier
injectivity for a good ready follows as well: an earlier merger would
persist to tick three. Thus (2) implies recoverability at every n, while
(1) immediately implies (2). Section 3 makes the recovery explicit.

For completeness, each exceptional double fibre has distinct full QDD
records. Its initial-phase pair is 0 with one of 1,2,3,4. The inverse
piston classes are respectively A with B or C from the inherited
[full-record proof, section 6](../P-QDD-U-NATIVE-READBACK-1/PROOF.md), which
proves `A != +/-B` and `A != +/-C`. Complete QDD equality is exactly
common-sign equality there. There is only one zero source in D_a, so at
least 124 of its 125 conflicting pairs consist of supported sources.
Consequently full original QDD recovery on all supported sources also
fails at each exceptional ready.

## 3. Constructive source reader at common ready `(0,1)`

Choose `(q,r)=(0,1)` once, independently of p and its QDD value. The five
table rows are `(1,2),(1,0),(2,0),(2,1),(3,1)`, all distinct. This admits
every one of the 625 piston sources and all 624 supported sources.

For `n>=3`, use the inherited chart to recover the tick-three state y
from `(n,x_n)`. To specify the construction completely, put

```text
theta(j)=popcount(j) mod 2,
S(M)=M-floor(M/2)+floor(M/4)-...,
t_n=(-1)^(n-3), h_n=(-1)^(n+theta(n-1)),
N_n=S(floor((n-1)/2))-1,
alpha=t_n(p1+p1p), beta=t_n(p4+p4p),
gamma=h_n(p1-p1p-2), delta=h_n(p4-p4p-1),
epsilon=t_n*r-N_n.
```

Reduce these five labels modulo five. Their tick-three inverse is

```text
y1=3(alpha+2+gamma), y1p=3(alpha-2-gamma),
y4=3(beta+1+delta), y4p=3(beta-1-delta),
yr=epsilon, yq=1-alpha-beta-epsilon.
```

The chart theorem proves y=F3(x0) for every n, not just the tested times.
Read `(yq,yr)` in the distinct-row table to identify z, then apply
`H_z^{-1}`. Explicitly the inverse compositions are
`ace,d,e,dbd,ebd`, respectively. Every factor is an involution, so this
returns the exact original six-coordinate head and therefore p.

For `n=0,1,2`, either finish the at most three known native transitions
and apply the same inverse, or try the five initial phases, reverse their
known n-step generator words and retain the candidate with the declared
ready and matching initial phase. The proven injectivity makes the latter
candidate unique. This uses no future measured record: future transitions
in the former option are calculations from the present mathematical state.

The zero source is treated by the same inverse, without division. Applying
the registered QDD map afterwards returns ZERO_SUPPORT at p=0 and the
existing supported record otherwise. No probability or event is assigned
to the zero source by this retention statement.

This selected ready is an allowed common mathematical initial condition.
Its existence does not derive a physical preparation operation, a physical
full-state observation port or an apparatus interaction. No selected ready
is inserted into the unchanged U update, and the reader never feeds back.

## 4. Regenerable-archive corollary and its precise boundary

For any preparation subset D at common origin zero, let
`H:D->Y^N_0` be a stipulated complete history with literal ordered equality,
and let H_n denote its prefix through n. Then an exact reader of only
`(n,F_n(x))` returns H_n for every `n>=3` iff H is constant on F3 fibres
intersected with D. This permits arbitrary clock-dependent readers.

**Proof.** Equal F3 values give equal current native states at every later
time. Exact prefix readback therefore gives equal finite prefixes of H at
every length, hence equal complete histories. Conversely assign the common
history to each attained F3 value, recover that value with the chart and
truncate. This converse is set-theoretic; executable finite-prefix
readback also requires a finite-prefix algorithm for the stipulated H.

There are at most `|F3(D)|<=3125` distinct complete histories in this
current-state archive class. The bound counts alternatives at common
origin, not archive length or complexity as a function of the counter.
On a good common-ready slice, every computable source-dependent history
can accordingly be regenerated from current state and counter. In
particular the selected source-incidence slot construction may be
recomputed with a fixed start and calendar without a saved copy of p.
No runtime or physical locality bound is asserted for this recomputation.

This corollary does not assert a physical blank-cell write, a material
archive, independently writable new inputs or a physical occurrence law.
A physically retained early history or an ancillary memory is another
input class. The original full-domain v79 readback obstruction and the
apparatus-only history factor remain intact. No global physical
apparatus-completeness or physical decoder obligation is closed here.

## 5. Exact audit scope

The unexecuted accepted `native_audit.py` uses its own direct transcription
of the five generators for forward U, and the chart/table inverse above
for readback. It checks all 625 sources at common ready `(0,1)` at every
`n=0,...,64`; all 25 readies and 625 sources at tick three; the exact
625/500 image cardinalities and fibre multiplicities; distinct QDD
common-sign classes on every exceptional double fibre; and zero-source
retention. No module is imported or run before the joint public pin.
The all-n statements rest on this proof and the inherited chart theorem;
the finite audit is not their proof or a physical experiment.
