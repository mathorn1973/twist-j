# RESULT. P-CARRY-ARITY-CIRCUIT-1

## Current verdict

```text
SCIENTIFIC TARGET:   CARRY-ARITY-CIRCUIT
PROOF STATUS:        proof supplied in frozen PREREG, review pending
LOCAL AUDIT:         PASS, 6/6, x86_64
TWO-ARCH GATE:       PENDING
PUBLIC REGISTRATION: NONE
CANON CHANGE:        NONE
```

No scientific falsifier fired in the valid local run.

The frozen all-n statement is:

```text
For q_n(x)=binom(popcount(x),2) mod 2 on F_2^n and
P_n={x!=0:q_n(x)=0}, the complete set P_n is a spanning circuit
if and only if n=4.
```

Equivalently `|P_n|=n+1` iff `n=4`. At `n=4`, the complete singular locus is
`{1,2,4,8,15}`, so its cardinality five is an output of the carry-arity
criterion, not an input prime/order condition.

The proof is universal and does not depend on the finite verifier sweep:
for `n<4` only weight-one singular words exist; for `n=4` there is exactly
one additional weight-four word; for `n>=5` the weight-four layer alone has
`binom(n,4)>=5` members, too many for one spanning circuit.

The existing `CARRY-PENTAD [T]` remains a separate dependency only for the
bounded consequence after `n=4` is selected. This result does not choose a
five-cycle, orientation, exponent, `J`, a zeta carrier, an adelic completion,
a Weil form, positivity, RH, a decoder, or any L2-L6 lift.

## Next gate

Open a draft probe PR changing only `probes/P-CARRY-ARITY-CIRCUIT-1/` and
require both public architecture jobs plus aggregate `check`. Only after
byte-identical `EXPECTED.txt` reproduction and proof review may a separate
fold consider registration. Any change to `PREREG.md` or `verify.py` requires
a new named probe; the current pin is immutable.
