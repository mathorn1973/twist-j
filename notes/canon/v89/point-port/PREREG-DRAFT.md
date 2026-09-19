# Native point-port capacity: preregistration draft

**NON-CANONICAL. UNPINNED PREPARATION. No formal execution or earned status.**

Proposed identifier: `P-QDD-NATIVE-POINT-PORT-CAPACITY-1` (unreserved).
Proposed claim: `QDD-NATIVE-POINT-PORT-CAPACITY`. Action layer: **L1**.
Formal owner, public issue and pin: **not assigned**. This file is a review
input; it does not start a probe. The operational procedure is the current
`POLICY.md` and `AGENTS.md`, not the incubation issue's run procedure.

## Basis and exposure

Public Canon v88 at main `e57d4506d5b28bf8cb4979c4e29db6b10b2441f2`,
content `168e95561aa7bdd6ddeec72d40560fa5b8ac5e81`. Accepted source:
[issue #1036](https://github.com/mathorn1973/twist-j/issues/1036), tree
`462e9721ad4b9f60f2df6c98715b0bfcc1976425`; proof blob
`ab03fc5ab37ec787ea3794862a1a9b69048f0749`.

The source proof and its published finite results have already been read.
All numerical targets below are exposed intake targets, not blind
predictions. Source run records do not count as this proposed public probe's
execution. The inherited quotient and history-indistinguishability theorem
are the existing `P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md`, blob
`f848b6fa08163bcef2c51a0a7fdfad4b299163a6`; they are dependencies, not new
claims. The isolated source audit is adapted with explicit assertions in
the adjacent `verify.py` draft, with attribution retained.

## Equation, carrier and comparison class

Let `P=F5^4`, `P*=P\{0}`, `ell=(0,1,2,-2,-1)`, `v=ell(p)`,
`s=sum(v)`, `N=sum(v_i^2)`. The original target is

```text
beta(p) = s^2/[4(5N-s^2)]  (p in P*).
beta(0) is undefined; its tag is ZERO_SUPPORT.
```

Freeze one experimental context and one deterministic encoder
`f:P -> F5^4`, arbitrary nonlinear and possibly noninjective. Each source
launches exactly one point `(f(p),q0,r0)` at native counter zero. The target
continues to be `beta(p)`, never `beta(f(p))`. The subsequent evolution is
the unchanged native `U` with `theta_n=popcount(n) mod 2`.

Observe only the full chronological `A_n=(q_n,r_n)` history, common clock,
and common source-independent inputs. Granting full
`Q_n=(z_n,q_n,r_n)` history is an explicitly larger comparison class:
`x_n` is the full six-coordinate checkpoint (four current pistons, q_n,
r_n), and `z_n=sum x_n mod 5` sums all six coordinates, distinct from the
initial encoded four-piston sum k(p). Arbitrary downstream nonlinear
processing, unbounded memory,
stopping, silence, postselection and processor-memory reset are admitted.
They neither intervene in `U` nor observe another source coordinate.

An optional random variable `xi` has a fixed source-independent probability
law and supplies the ready and all processor randomness. All maps and
events used to define laws must be measurable. Conditional on `xi` the
processor is deterministic; its initial state and transition/output rules
are the same for every source. Crucially **f is independent of xi**. This
external probability model is a mathematical relaxation, not native
sampling or an L6 physical measure. Conditional response is evaluated only
on one fixed processor-defined completion event with strictly positive
probability at every supported source; source-dependent acceptance supplied
from outside the observed history is not admitted.

The faithful subclass consists of permutations `f` of all 625 labels,
including the null. It is not merely injection on the 624 supported labels.

## Frozen claims and exact failure thresholds

1. Complete transcript laws factor through `k(p)=sum f(p) mod 5`.
   Every completed binary response therefore has at most five distinct
   supported-source LOW values, including after admitted postselection.
   A pathwise proof is required; finite history regressions alone do not
   establish the universal statement.
2. The six balanced inputs `(1,-1,0,0)`, `(1,0,0,0)`, `(1,1,0,0)`,
   `(1,1,1,0)`, `(2,1,1,2)`, `(1,1,1,1)` have respectively
   `0,1/16,1/6,3/8,9/14,1`. Thus no member of the class realizes the
   complete original target law. This necessary event failure excludes a
   full cycle requiring that event in this class only.
3. The supported target census is exactly the 22 values and multiplicities
   frozen below, totaling 624. Require agreement of direct source
   enumeration, an independent multinomial enumeration and the frozen
   table. The null must remain separately tagged.
4. In the supported-only metric
   `min_(k,c) max_(p in P*) |beta(p)-c_(k(p))|`, with at most five responses
   in `[0,1]` and arbitrary deterministic k, the exact optimum is `9/128`.
   Require the displayed six-source packing and complete five-block cover,
   plus exact interval enumeration/dynamic-programming agreement. A
   target-aware encoder and externally supplied finite uniform random
   response realize the upper certificate at ready `(0,1)`.
5. For permutations of all 625 labels the corresponding supported-only
   optimum is `27/64`. Require the analytic 120-source strict high-weight
   count, the capacity argument, all five possible positions of the
   124-member supported block, and the full 625-image bijection attaining
   the displayed sorted-block certificate.
6. Every faithful encoder leaves the null in a message fibre with 124
   supported labels. Exact ZERO_SUPPORT/SUPPORTED classification on all
   original labels is impossible. No numeric value is assigned to beta(0).

### Frozen finite statement for review without verifier or proof access

| beta | Multiplicity | beta | Multiplicity |
| ---: | ---: | ---: | ---: |
| 0 | 84 | 2/17 | 24 |
| 1/256 | 24 | 9/64 | 24 |
| 1/176 | 48 | 5/32 | 8 |
| 1/136 | 32 | 1/6 | 24 |
| 1/96 | 24 | 2/7 | 24 |
| 1/56 | 48 | 5/16 | 24 |
| 1/46 | 36 | 3/8 | 16 |
| 1/26 | 48 | 5/8 | 8 |
| 9/224 | 24 | 9/14 | 12 |
| 1/16 | 56 | 49/64 | 8 |
| 9/104 | 24 | 1 | 4 |

The six field-label packing sources `0014,0012,0112,1112,1222,1111`
have weights `0,9/64,2/7,5/8,49/64,1` in that order; their least
adjacent separation is `9/64`.

| Free upper block extremes | Center |
| --- | ---: |
| `[0,1/46]` | 1/92 |
| `[1/26,1/6]` | 4/39 |
| `[2/7,3/8]` | 37/112 |
| `[5/8,49/64]` | 89/128 |
| `[1,1]` | 1 |

The blocks cover exactly the attained target values without overlap. Send
the labels in each block to any native point of its selected piston sum,
such as `(k,0,0,0)`. This free construction may destroy other source data.

Exactly 120 supported labels have beta strictly above `5/32`. For faithful
attainment, sort supported labels by `(beta(p),p)` with p in lexicographic
order and use:

| Supported block size | Extremes | Center |
| ---: | --- | ---: |
| 124 | `[0,1/176]` | 1/352 |
| 125 | `[1/176,1/56]` | 29/2464 |
| 125 | `[1/56,1/16]` | 9/224 |
| 125 | `[1/16,5/32]` | 7/64 |
| 125 | `[5/32,1]` | 37/64 |

Assign these blocks bijectively, in order, to the first available
lexicographic native points of sum `0,1,2,3,4`, and place the null in the
last remaining point of fibre zero. The result is a 625-image permutation.
The other four placements of the 124-member block are also frozen audit
targets with the same optimum `27/64`.

Both upper constructions use comparison ready `(0,1)`, for which sums
`0,1,2,3,4` produce first A observations
`(0,4),(1,4),(1,0),(2,0),(0,1)`. Decode the sum and realize its rational
center by thresholding an externally supplied common finite uniform integer
with a denominator divisible by all five response denominators. This
declares the comparison randomness and does not derive it from U.

Every exact equation, membership, count, sharp value and bijection above
has zero tolerance. A counterexample within the declared class, a missing
proof step, or any assertion failure prevents acceptance of the affected
claim. Preserve failures and do not repair thresholds after the public
pin. Physical outside-class examples are not falsifiers of this statement;
an example meeting every frozen hypothesis is.

## Code, systematics and execution boundary

The proposed accepted verifier is the adjacent `verify.py` **draft**:
standard-library Python, integer/Fraction decisions, no downloaded data,
predecessor imports, stochastic search, external process or runtime file
writes. It audits the original generators against the quotient, selected
updates for both bits, inherited ready-history regressions, all quadratic
targets and all finite certificates. Its eight-step histories remain
explicit regressions, not evidence for arbitrary-time extrapolation.

Finite branch response centers are ideal mathematical probabilities. They
have no measured error bar and do not come from an adopted occurrence law.
Both attaining encoders are target-aware comparison constructions.
Faithful and noninjective optimization must remain distinct; the latter
upper certificate does not promise correct null classification. Common
launch time, seed independence, unchanged source labels and no native
intervention are load-bearing hypotheses.

Before execution, complete current authority/collision checks, assign the
public owner and issue, freeze the final statement and code on its own
`probe/P-NAME` branch, and commit/push the accepted `PREREG.md` and
`verify.py`. Record that pin and hashes. Only then follow current public
execution, exact-output and two-architecture requirements. Independent
proof review is separate from reproduction. No `RUN.md`, `EXPECTED.txt`,
formal result, probe reservation or Canon promotion is supplied here.

The complete physical QDD owners remain O. No physical preparation,
coherent-code rejection, occurrence law, persistent record, native reset,
complete apparatus class, or L1-to-L5/L6 gate is claimed.
