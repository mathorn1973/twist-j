# P-U-PREPARATION-EVENT-RECORD-1: native apparatus observability

**Prospective, proof-first, result-exposed, L1 only.** Issue #866.
The algebra and predicted classifications below precede the joint public
preregistration/code pin and its first formal execution. No new scientific
execution or verifier import is reported here. The proof concerns one exact
native coordinate split with a common independent apparatus preparation; it
is not a completeness claim about every physical apparatus or the decoder.

## 1. Public premises, exposure and the chosen split

The native generators, selector and their involutivity are the public
premises in
[P-QDD-U-NATIVE-READBACK-1/PROOF.md](../P-QDD-U-NATIVE-READBACK-1/PROOF.md).
The adopted `QDD-U-INDUCED-CHANNEL` theorem supplies the generator fibre
formulas and a delay-one factorization, explicitly without a claim about
delays two and above. Its bidirectional channel witnesses are preserved.

Raw sum closure was also exposed in the unmerged, NON-CANONICAL note
`notes/C-QDD-U-INDUCED-NULL-ANATOMY-1-N/C-QDD-U-INDUCED-NULL-ANATOMY-1-N.md`,
section 7, at commit `e43b458337f2ce93dd0700c77e8391910e00d59b`:
17109 bytes, SHA-256
`c442956e3b5a0728b2b1501bbeaaff99ea56f79e6ba98a4c06dccd5bb868d624`.
Its separate piston-sum/fibre-sum generator table is acknowledged prior
algebra, not a new discovery here. Its broader physical language is not
inherited as authority. The new targets are the complete history equivalence,
its exact finite recognition horizons, tail losses, and the source-function
and downstream record/event consequences at the frozen scope. The separate
in-flight `P-QDD-INSTRUMENT-U-INDUCED-2` draft is not resumed or modified.

All checkpoint arithmetic below is in `F5`. Fix

    x=(p1,p4,p1p,p4p,q,r)=(p,A),
    p=(p1,p4,p1p,p4p) in F5^4,        A=(q,r) in F5^2,
    kappa(p)=p1+p4+p1p+p4p,
    z(x)=kappa(p)+q+r.

The natural system block is the four pistons and the apparatus observation
is `A` alone. A fixed ready `a=(q,r)` is the same for every admitted system
preparation. It is not selected as a function of `p` or its desired QDD
output. Every run has the same origin and the same driver word `b_0,b_1,...`.
The general closure argument allows any such binary word. The exact ready
classification later specializes to the public driver
`b_n=theta_n=popcount(n) mod 2`, whose first three bits are `011`.

The native step selects generator `g_(z+2b mod 5)` from `(a,b,c,d,e)`;
generator names in lower case are distinct from the ready `a` and driver
values `b_n`. Explicitly,

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

## 2. Exact closed quotient for every common driver

Let `Q(x)=(z,q,r)`. Summing the generator formulas and reading their last
two coordinates gives the complete quotient table:

| Generator | New `(z,q,r)` |
| --- | --- |
| `a` | `(z,q,r)` |
| `b` | `(-z,-q,-r)` |
| `c` | `(2-z,1-q,-r)` |
| `d` | `(2-z,1-q,1-r)` |
| `e` | `(3-z,2-q,1-r)` |

For example the two `r` contributions in the piston sum of `c` cancel;
its four piston constants sum to `6=1` in `F5`, so its new piston sum is
`1-kappa`, and adding its new `q,r` gives `2-z`. Equivalently the piston
sum transforms under `a,b,c,d,e` as
`kappa,-kappa,1-kappa,-kappa,-kappa`. No individual piston remains in the
quotient formula.

After applying the selector, the two quotient updates are therefore:

| Current `z` | New `(z,q,r)` for driver `0` | New `(z,q,r)` for driver `1` |
| --- | --- | --- |
| `0` | `(0,q,r)` | `(2,1-q,-r)` |
| `1` | `(4,-q,-r)` | `(1,1-q,1-r)` |
| `2` | `(0,1-q,-r)` | `(1,2-q,1-r)` |
| `3` | `(4,1-q,1-r)` | `(3,q,r)` |
| `4` | `(4,2-q,1-r)` | `(1,-q,-r)` |

This proves the commuting identity

    Q(native_step_b(x)) = quotient_step_b(Q(x))

for every checkpoint and both bits. Induction proves it for every finite
common driver word and hence for every infinite common driver. The quotient
has 125 states, since every choice of `z,q,r` has exactly `5^3=125` piston
preimages with the required sum.

In particular, with ready `(q,r)` fixed, the entire history

    H_a(p)=(A_0,A_1,A_2,...)

depends on `p` only through `kappa(p)`. Equality of `kappa` gives equality of
the entire quotient history, not merely the eventual apparatus tail. This
assertion does not require synchronization, any frequency limit, a finite
window, or the special Thue--Morse driver.

## 3. First two observations give the complete TM history equivalence

Now use the fixed-origin TM driver. Parameterize its five possible initial
piston sums by `z=kappa+q+r`. Write `A_t(z)` for the apparatus at tick `t`
from the fixed ready `(q,r)` and that initial `z`. The first bit is zero,
so Section 2 gives

| Initial `z` | `A_1(z)` | Phase `z_1` |
| --- | --- | --- |
| `0` | `(q,r)` | `0` |
| `1` | `(-q,-r)` | `4` |
| `2` | `(1-q,-r)` | `0` |
| `3` | `(1-q,1-r)` | `4` |
| `4` | `(2-q,1-r)` | `4` |

The four apparatus values in the last four rows are always distinct: they
are the common vector `(-q,-r)` plus the distinct offsets
`(0,0),(1,0),(1,1),(2,1)`. Equality of the first row with one of them occurs
if and only if twice the ready equals the corresponding offset. Since the
inverse of two in `F5` is three, the complete collision list is

| Ready `(q,r)` | Initial phases with equal `A_1` |
| --- | --- |
| `(0,0)` | `0,1` |
| `(3,0)` | `0,2` |
| `(3,3)` | `0,3` |
| `(1,3)` | `0,4` |

No other first-observation collision is possible. For ready `(3,0)`, the
colliding initial phases `0,2` also have the same new phase `z_1=0`.
Their whole quotient states at tick one are equal. Section 2 therefore
proves that their apparatus histories are equal at every later tick, for
any common continuation of the driver.

For each of the other three ready states, the colliding `A_1` values have
different phases `0,4`. The next TM bit is one. At phase zero the apparatus
update is `(u,v)->(1-u,-v)`, and at phase four it is
`(u,v)->(-u,-v)`. Their first coordinates differ by one, so `A_2` separates
the two previously colliding histories. Explicitly the complete second-tick
table is

| Initial `z` | `A_2(z)` | Phase `z_2` |
| --- | --- | --- |
| `0` | `(1-q,-r)` | `2` |
| `1` | `(q,r)` | `1` |
| `2` | `(q,r)` | `2` |
| `3` | `(q-1,r-1)` | `1` |
| `4` | `(q-2,r-1)` | `1` |

Every pair already separated at tick one remains separated as histories,
even if its current values coincide at some later tick. Thus

    H_a(p)=H_a(p')
        iff (A_1(p),A_2(p))=(A_1(p'),A_2(p'))

for every fixed ready and every pair of source pistons. This is a theorem
about complete infinite histories obtained from a finite table and an exact
quotient-merger argument; it is not extrapolation from a sampled prefix.

The complete classification and minimum recognition horizons are:

| Ready class | Number of readies | Distinct full-history classes | Least complete history horizon |
| --- | ---: | ---: | ---: |
| Every ready outside the four displayed exceptional readies | 21 | 5 | tick 1 |
| `(0,0)`, `(3,3)`, `(1,3)` | 3 | 5 | tick 2 |
| `(3,0)` | 1 | 4 | tick 1 for its four observable classes |

Here a horizon `h` means observing the chronological prefix
`(A_0,...,A_h)`, with the ready fixed. At horizon zero every source gives
the same observation, so it cannot distinguish four or five classes. For
the three horizon-two readies the explicit tick-one collision proves that
two is least. Ready `(3,0)` never distinguishes all five initial sums at
any horizon; the minimum stated there concerns exactly its four possible
full histories.

In source-sum coordinates the unique permanent full-history identification
at ready `(3,0)` is

    kappa=2  equivalent to  kappa=4,

because `q+r=3` and their initial phases are `0,2`. Each of the other three
sum values is its own class. On all 625 source pistons, a sum fibre has 125
members. Accordingly the source-class sizes are five copies of 125 at the
other 24 readies, and `250,125,125,125` at `(3,0)`.

## 4. Tick-three tails and the transient information that disappears

Applying the third TM bit, again one, gives the exact table

| Initial `z` | `A_3(z)` |
| --- | --- |
| `0` | `(q+1,r+1)` |
| `1` | `(1-q,1-r)` |
| `2` | `(2-q,1-r)` |
| `3` | `(2-q,2-r)` |
| `4` | `(3-q,2-r)` |

All five new phases equal one. Every subsequent common driver bit acts on
the five apparatus trajectories with a common generator, since their phase
recursion is the same. Each generator's apparatus map in Section 2 is a
bijection. Therefore equality of `A_3` is equivalent both to equality of
the entire apparatus tail from tick three and to equality at any one fixed
later tick. A later common update cannot either split equal apparatus
values or merge distinct ones at that synchronized phase.

The last four rows of this table are again always distinct. Equality with
the first row produces exactly the same four exceptional readies and the
same initial phase pairs as in the tick-one table. Consequently:

| Ready | Initial sum pair identified by every tail starting at tick 3 or later |
| --- | --- |
| `(0,0)` | `0,1` |
| `(3,0)` | `2,4` |
| `(3,3)` | `2,4` |
| `(1,3)` | `0,1` |

The other 21 readies retain five tail classes. Each exceptional ready has
four tail classes. At the three ready states `(0,0),(3,3),(1,3)`, the
identified pair is distinguished by the apparatus at tick two, but neither
earlier nor at any tick from three onward. The full history retains that
transient observation; the apparatus tail alone does not. This distinction
does not assert an extra permanent memory inside `A`.

## 5. Necessary and sufficient criterion for any source quantity

Fix the ready and the TM driver. Define the maximal source label `K_a(p)`
as follows:

* if `a!=(3,0)`, let `K_a(p)=kappa(p)`;
* if `a=(3,0)`, let `K_a(p)` be the class of `kappa(p)` under the single
  identification `2~4`.

Sections 2--3 prove the exact equality criterion

    H_a(p)=H_a(p')  iff  K_a(p)=K_a(p').

Let `D` be any admitted subset of source pistons and `h:D->Y` any required
source quantity, with equality in `Y` fixed. Then the following are
equivalent:

1. A function of the entire apparatus history recovers `h(p)` for every
   `p in D`.
2. Equal `K_a` values in `D` imply equal `h` values.
3. There is a function `bar_h` on the attained `K_a` labels with
   `h=bar_h composed with K_a` on `D`.
4. A function of the finite prefix `(A_0,A_1,A_2)` recovers `h` on `D`.

Necessity follows from equal histories. For sufficiency assign to each
attained observable label its common `h` value; the equality criterion makes
this well-defined. The finite prefix identifies that label by Section 3.
This also proves the factorization and the converse implications. For a
particular `h`, a shorter horizon may suffice; Section 3 gives the least
horizon for recovering the complete observable label.

The proposition includes source records, source classes and proposed source
parameters for an event law. It classifies mathematical recoverability and
does not choose `h`, a target-dependent preparation subset, or a physical
context. On the full source carrier, the natural apparatus port supplies at
most five independently distinguishable preparation labels, or four at the
exceptional ready, irrespective of the size of a downstream history store.

## 6. Any causal history processor preserves this equivalence

Allow an arbitrary deterministic downstream processor with a common initial
memory state independent of `p`. Its memory may be finite, unbounded, or an
entire growing history. At each tick its update and outputs may depend on
its current memory, the newly observed `A_n`, the common driver, the common
tick index, and other stipulated common source-independent inputs. Its
functions are fixed across preparations and do not feed back to change `U`.

For two preparations with identical apparatus histories, induction on the
tick gives identical processor states and identical outputs at every tick.
The base case is the common initial memory; the induction step applies the
same function to equal states and equal inputs. Consequently all of the
following remain equal whenever the required objects are defined:

* every selected reader parameter and context obtained by that processor;
* every LOW/HIGH/SILENT output and every internal acceptance decision;
* every record written to its memory and every future update or reset driven
  by those same inputs;
* complete output transcripts, stopping decisions, and finite event counts;
* limiting output densities and positive-acceptance ratios.

The statement does not require a finite horizon. Even a noncausal arbitrary
function of the entire infinite apparatus history takes the same value on
equal histories. Common time and common driver inputs cannot separate them.
Any desired deterministic source-to-record value or selected source law must
therefore obey the factor criterion in Section 5. The existence of a larger
processor memory cannot supply information that never reached its input.

This propagation is a conditional statement about a specified observation
port. A separate source-dependent initial memory, a processor parameter
selected from the source, a different observed port, a system-dependent
external invocation/acceptance schedule, or a feedback intervention changing
the native evolution is outside it. A procedure that also observes current
piston classes has enlarged its input and is not covered merely by calling
that observation a context.

## 7. Exact original-QDD and support obstructions

For a piston `p`, use the inherited balanced lift
`ell=(0,1,2,-2,-1)` and `v=(ell(p1),ell(p4),ell(p1p),ell(p4p))`.
Put `s=sum(v)` and `N=sum(v_i^2)`. On nonzero support the original normalized
QDD LOW value is

    LOW(p) = s^2 / (4*(5N-s^2)).

Consider the two supported pistons

    p_A=(1,0,0,0),       v_A=(1,0,0,0),
    p_B=(2,4,0,0),       v_B=(2,-1,0,0).

Their field-valued sums are both one; their balanced sums are both one,
while their squared norms are one and five. Their exact LOW values are
therefore respectively

    1/16  and  1/96.

For every common ready `(q,r)` and every common driver word, these two
preparations have identical entire apparatus histories by Section 2.
No single apparatus-history-only selector or processor with common ready
memory can assign them their two different required original QDD laws.
This applies to exact finite outputs and to any defined limiting laws;
allowing an unbounded history or internal SILENT events does not separate
identical inputs.

There is a separate support witness:

    p_0=(0,0,0,0),       p_+=(1,4,0,0).

Both have field sum zero, but their balanced vectors are `(0,0,0,0)` and
`(1,-1,0,0)`. Thus the former has `ZERO_SUPPORT` and the latter is supported
with squared norm two. They again have identical entire apparatus histories
for every common ready and driver. Consequently even exact original
ZERO_SUPPORT-versus-SUPPORTED recognition fails in this port class. The
zero case is not normalized or treated as a LOW probability.

These are failures of the source-function factor criterion on the full
registered source domain, not a choice of reader made after observing a
target. Restricting preparations to avoid conflicting fibres changes that
domain and must be separately declared; it does not invalidate the theorem.

## 8. The full native states need not lose the hidden information

For any two distinct full initial checkpoints with the same `Q`, Section 2
gives equal quotient states at every tick of a common driver word. Their
selected generators therefore agree at every tick. Every one of the five
generators is a bijection (indeed an involution), so it sends distinct full
checkpoints to distinct full checkpoints. Induction proves

    x_0!=x'_0 and Q(x_0)=Q(x'_0)
       imply x_n!=x'_n for every n>=0.

Both witness pairs in Section 7 satisfy these premises for any common ready.
They therefore never merge in the full native state even though the entire
apparatus histories agree. This is an observation-port obstruction, distinct
from the earlier original-record loss caused by a full native merger. No
claim is made that preparations with different initial `Q` cannot merge.

## 9. A-only versus an augmented observation, and the exact boundary

The five/four history classification and its recognition horizons concern
`A=(q,r)` alone, starting at tick zero. If the observer is additionally given
`z_0`, then it immediately recovers

    kappa=z_0-q_0-r_0.

For the augmented history `(z_n,A_n)` the maximal source label is therefore
always the full five-valued `kappa`, at horizon zero. In particular its
initial observation distinguishes the two sums lost by A-only observation
at ready `(3,0)`. This is extra access to a sum involving system coordinates,
and must not be silently attributed to the A-only port.

Neither augmented history, the driver nor a common counter resolves the
Section 7 witnesses, which already have equal `Q_0`. From tick three onward
the phase is common across the five source sums, so adding `z` to those late
tails does not undo the tail identifications of Section 4.

The older finite `QDD-U-INDUCED-FINITE-NONSELECTION` census conditions event
counts on the **current piston class**. Such system-side conditioning can
produce class-dependent tables and its `INFO=150` conclusion is untouched.
The present theorem asks a different exact question: what the complete
apparatus observation alone can identify about an independently prepared
original source. Its all-time obstruction extends beyond a fixed list of
linear pointer readings or finite delays, while keeping that source/ready/
observation contract explicit.

There remains native algebraic coupling and backreaction. This proof does
not show that every native split, physical preparation, larger apparatus,
record carrier, coupling, intervention, or reading family fails. It supplies
one complete observability boundary, the recoverable finite source quotient,
and the resulting constraint on the preparation-to-reader-to-event-to-record
chain. A separate conditional processor may write information that reached
its input; it cannot manufacture the missing distinction or thereby close
the physical decoder.
