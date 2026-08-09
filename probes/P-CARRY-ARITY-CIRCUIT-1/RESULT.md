# P-CARRY-ARITY-CIRCUIT-1 result

Status: TRUE PROOF-FIRST LEMMA; TWO-ARCHITECTURE AUDIT PASS; PROMOTION STOP AFTER POST-PIN SCOPE REVIEW

## Recorded decision

```text
mathematical statement: TRUE by the all-n proof in the frozen PREREG
finite audit:           RESULT 6/6 ALL PASS
x86_64 replay:          PASS
aarch64 replay:         PASS
aggregate check:        PASS
public registration:    NONE
promotion from #314:    STOP
Canon change:           NONE
```

The verifier is an audit only. The theorem-grade content, to the extent retained
as a lemma, is carried by the exact all-n proof, following the public precedent
that an independent proof may earn T while its verifier remains an audit.

## One-line reduction

For

```text
q_n(x) = binom(popcount(x),2) mod 2,
P_n    = {x != 0 : q_n(x)=0},
```

the carry bit has the exact weight pattern

```text
q_n(x)=0  iff  popcount(x) mod 4 is in {0,1}.
```

Thus its weight period is exactly `4 = 2^2`. The first non-atomic singular
weight is four. At the first arity where that layer can occur,

```text
n = 4,
P_4 = {e_1,e_2,e_3,e_4,1_4},
|P_4| = 5 = 2^2 + 1,
e_1+e_2+e_3+e_4+1_4 = 0.
```

The earlier circuit formulation is a correct corollary: `P_n` is a spanning
circuit iff `n=4`. It is not retained as an independently motivated selector.

## Why promotion stops

Post-pin adversarial review found two defects in the frozen **promotion scope**,
not in the theorem proof.

1. The predicate “the complete nonzero singular locus is one spanning circuit”
   was not independently distinguished before the result. Treating that
   predicate itself as the selector would be result-shaped.
2. The frozen preregistration did not declare the adjacent arithmetic collision.
   The already-public `CARRY-PENTAD [T]` contains the fixed-five width gate
   `ord_5(2)=4`; the older project `verify_and_xor_p5.py` also recorded the
   equivalent quarter-turn arithmetic `2^2=-1 mod p => p=5`. The latter is
   provenance only here, not public evidence. The new lemma supplies a reverse
   route `second carry bit -> period 4 -> first non-atomic arity 4 -> 5 points`,
   not a new numerical fact `2^2+1=5`.

The frozen preregistration itself states that a post-pin defect invalidates the
probe id rather than authorizing a threshold/scope repair. Therefore its bytes
are not edited or reinterpreted. Issue #314 is closed and PR #315 is superseded.

## Procedure disclosure

No accepted-verifier execution occurred before the immutable pin. One excluded
notebook-wrapper preflight occurred **after** pin and remote readback; it is
recorded explicitly in `RUN.md`. It wrote unrelated startup instrumentation to
stderr and is not evidence. The subsequent neutral shell execution is the
formal local record. The first PR workflow attempt failed before verifier
execution on a RUN-schema test; only `RUN.md` was changed. No amend, rebase,
force-push, or change to frozen `PREREG.md` or `verify.py` occurred.

## Surviving scope

What survives from #314 is the exact arithmetic lemma:

```text
second carry bit
  -> exact weight period 2^2
  -> first non-atomic singular arity 4
  -> five-point singular locus 2^2+1.
```

No prime, five-cycle, cyclotomic field, `J`, zeta carrier, adelic completion,
Weil form, positivity, RH, decoder, physics, or L2-L6 lift follows from this
probe. A successor G0 must use a fresh name and an independently distinguished
symmetry criterion, with the arithmetic collision declared before its pin.
