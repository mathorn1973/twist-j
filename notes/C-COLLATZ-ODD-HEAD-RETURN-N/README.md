# C-COLLATZ-ODD-HEAD-RETURN-N

**NON-CANONICAL mathematical note. Author: A. M. Thorn.**

The exact arithmetic component is L1 candidate-T material. The Haar appendix
is a separately defined classical probability calculation, with no claim of
an earned lift to the canonical TWIST-J stream or measure layers.

Reservation: [issue #1861](https://github.com/mathorn1973/twist-j/issues/1861).
Base: `0c33e2b281e39127c269ef5dd7f5b529a62e9e65` (Public Canon v107).

This proposal follows the exact block identities in
[PR #1859](https://github.com/mathorn1973/twist-j/pull/1859), at its immutable
evidence head `b9a163e0dc1066429ed3fe367ac0756ef433c021`. It studies the odd
head in $n+1=2^k u$, the transition to the next block, and the effect of this
coordinate change on the real linear coefficients. Its proofs are
self-contained and make no priority claim.

## The block and the head

Write $T(n)=(3n+1)/2^{v_2(3n+1)}$ for positive odd $n$. A block consists of
all initial valuation-one steps followed by the first step whose valuation
is at least two. Thus its length is $k=v_2(n+1)$, and

$$
n=2^k u-1,\qquad t=v_2(3^k u-1),\qquad
B(n)=T^k(n)=\frac{3^k u-1}{2^t}.
$$

Writing $B(n)+1=2^{k'}u'$ gives the exact head transition

$$
\boxed{2^{t+k'}u'=3^k u+2^t-1.}
$$

The proofs establish four useful constraints on this description.

1. The state requires both $k$ and $u$. Even a fixed head can have
   unbounded output heads as the block length varies.
2. The inverse head map has a precise integral condition modulo $3^k$.
   This condition is automatic over $\mathbb Z_2$, where three is a unit,
   but is required for positive integer inputs.
3. For every prescribed finite length there is an explicit positive orbit
   whose number and odd head both increase throughout that many complete
   blocks. The next boundary of this family is also determined exactly.
4. In the Haar model, the block coefficient has first moment one, whereas
   the head coefficient has infinite first moment. Their logarithmic
   coefficients differ by an explicitly telescoping boundary term.

The block used here is a run ending at one contracting step. It need not be
the whole maximal contracting phase of an orbit.

## Files and replay

| File | Role |
| --- | --- |
| [PROOF.md](PROOF.md) | Integer block transition, inverse fibers, and exact growth family |
| [MEASURE.md](MEASURE.md) | Haar branch laws, coefficient moments, and logarithmic boundary term |
| [REPLAY-SPEC.md](REPLAY-SPEC.md) | Fixed finite inventory and execution contract |
| [verify.py](verify.py) | Exact standard-library verifier |

The identities and explicit witnesses were derived before the integrated
verifier was written. This is a result-exposed publication replay. The complete
source and specification will be publicly pinned and read back before its
first execution; the actual stdout and neutral execution record will then be
appended without rewriting that pin.

From the repository root, with Python 3.12 or later and assertions enabled:

```sh
python3 -I notes/C-COLLATZ-ODD-HEAD-RETURN-N/verify.py
```

The finite audit uses integers and exact rational arithmetic. Infinite
quantifiers, Haar measure, and the moment limits come from the proofs, not
from extrapolating finite counts. Real coefficients are defined from finite
valuation data; no Archimedean magnitude is assigned to a general 2-adic
state.

## Scope

This is candidate-T proof material and candidate-C finite evidence awaiting
review. The arbitrary-length growth family uses a different positive initial
value for each requested length. It does not exhibit an infinite positive
escaping orbit. The Haar conclusions do not transfer an almost-sure statement
to every positive integer. No Collatz convergence, new cycle exclusion,
physical realization, or canonical promotion is asserted.

The repository's `probes/` and `reproduce/` selectors do not execute this
notes verifier. Required architecture jobs check repository integrity;
their success cannot be counted as scientific executions of this note.
Scientific replay records must state their actual environments and pins.
