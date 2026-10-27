# Autonomous readings without the counter

**PUBLIC / NON-CANONICAL / candidate-T / L1 only / no authority.**
Author: A. M. Thorn <thorn@twistj.com>.
Owner: [#1290](https://github.com/mathorn1973/twist-j/issues/1290).
Basis: Public Canon v94, main/tag target
`af8dc5956e26917b265fd0070f500c841c326512`.

This note restricts a reading by its input and update contract before
specifying a physical target: one fixed function of the present native
checkpoint, with no counter, driver bit, history, auxiliary memory or other
input, must turn every admitted native step into the same deterministic
target step. The target map is not assumed invertible. This is a chosen
mathematical comparison class, not a physically forced decoder architecture.

| Domain or question | Exact candidate result |
| --- | --- |
| Every origin-zero reachable state at every n>=3 | Every admitted read is f=h V, where V takes 625 values in F5^4 and h(-v)=L h(v). The maximal covariant factor has step v -> -v. |
| Possible realized target dynamics | Only fixed points and two-cycles. If their counts are a and b, exactly a>=1 and a+b<=313 are possible. The maximal factor has one fixed point and 312 two-cycles. |
| A read total on every checkpoint at every counter | Exactly f=g Q, with Q the inherited thirteen-class quotient and all values of g fixed by L. |
| Marked scalar J or exterior J as target | Only the zero read exists in the declared current-checkpoint class. In particular the exterior target's period-ten sector is excluded as well as its hyperbolic sector. |
| Metric on the maximal factor | Even invariance under every automorphism of the bare factor leaves three positive lengths with three triangle inequalities. Fixing the step-pair length to one does not select a metric. |

The new part is the complete **covariant** factor for arbitrary target
self-maps, its sharper target exclusion, and the stated metric class.
The vector V, its sign law, the 313 invariant components, the thirteen
whole-space components and the exterior target's spectrum are inherited
public results. They are not presented as new discoveries.

The distinction from the registered counter-reading theorem is exact:
allowing the unbounded n restores the family L^n G(ell_n(x)) for arbitrary
stipulated bijections L and arbitrary G. Removing n from the reader's input
changes that class. A fixed finite window, a memory register, a different
sampling clock or a decoder retaining the original head changes it again.

This does not say that native checkpoints are periodic. They are not.
It classifies only those fixed checkpoint functions whose outputs have an
autonomous deterministic update valid for all heads and all admitted times.
An arbitrary fixed observation need not have such an output update.

The finite metric result neither constructs scalable space nor identifies
any distance, sign, cycle or source coordinate with a physical observable.
All 25 live H/O items remain open. No Canon, registry or physical gate changes.

Read [PREREG.md](PREREG.md) for the input/equality contract,
[PROOF.md](PROOF.md) for the exact classifications,
[REVIEW.md](REVIEW.md) for the exposed mathematical reviews, and
[PROMO-C-U-CLOCK-BLIND-AUTONOMOUS-FACTOR-N.md](PROMO-C-U-CLOCK-BLIND-AUTONOMOUS-FACTOR-N.md)
for the promotion boundary. No new scientific program was executed.
