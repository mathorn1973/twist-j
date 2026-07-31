# RESULT P-READ-REDUNDANCY-1

```text
probe            P-READ-REDUNDANCY-1
claim issue      216
pin_commit       997ba5cba3b44524d33c8d21d919390386aa4931
basis            Public Canon v27, tag canon-v27, CONTENT_COMMIT 116b62ed
verifier         2d28ff4ec95274feb625cf0689289f5b2b398d3c8234947c459b533f7db23565
stdout           5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa
local leg        aarch64, exit 0, empty stderr, 16 of 16 PASS
GitHub leg       x86_64, VERIFY PASS, byte identical
two-arch gate    SATISFIED
falsifiers       none of F1 to F8 fired
verdict          SURVIVED
informs          MINIMAL-READ-DERIVATION [O]
closes           nothing
```

## Outcome against the frozen statements

```text
A  SURVIVED. Absence of feedback alone does not bound finite read redundancy.
   The typed projection funnel carries multiplicity 6 over Z with zero
   arithmetic nodes, on 9 exact values in Q and Q(sqrt5) under 8 port orders
   (A2), on a sixfold cover whose offsets are translation invariant with
   distinct unit-interval types (A3). Over Q every multiplicity in 1..12
   carries (A5). Dropping totality also voids every bound: the diagonal
   common-value map carries every m in 1..8 (A4). Acyclicity, no-feedback,
   integrality and totality together obstruct nothing.

B  SURVIVED. Over Z_S an anonymous total accumulator of multiplicity m exists
   if and only if every prime factor of m lies in S.
   Sufficiency is exhibited by P = e_1/m over the minimal ring (B4).
   Necessity rests on the symbolic argument, whose stratum structure the
   verifier machine-checks: the weight-1 stratum is exactly {(1)} with orbit
   count m and every monomial symmetric basis element has diagonal degree
   equal to its weight (B2), with orbit counts cross-checked against explicit
   enumeration (B1). The diagonal identity therefore forces m c_(1) = 1 in R,
   that is 1/m in R.
   Three independent exhaustion legs corroborate necessity inside their frozen
   boxes and found nothing: 390625 integer symmetric candidates at m = 2 (B5),
   1922375 dyadic power-sum candidates at m = 6 (B6), and 1922375 dyadic
   elementary candidates at m = 6 (B7). One ring cell was cross-checked by a
   route that does not use the prime-support rule at all (B8).

C  HELD. The result only informs MINIMAL-READ-DERIVATION. Nothing here closes
   it and nothing derives beta_1 as the physically canonical coin.
```

The corollary recorded inside `B`: for any `S` with `3 not in S`, in particular
both registered-place instances `{2}` and `{2,5}`, multiplicity 6 is obstructed
while multiplicity 2 carries whenever `2 in S`; on rungs multiplicity 1 is free
over `Z` and multiplicity 5 carries iff `5 in S` (C1). In one sentence:
acyclicity is free, anonymity is priced, and the price is a prime. The sixfold
read costs the prime 3, which the constant ring does not carry; the twofold
read costs only the prime 2, which the read place carries.

## The anti-rhetoric fence held

`C2` confirms the frozen blindness table: over `S = {2,5}` the pair `{2,6}`
forces the 2-cover, `{2,10}` is nonunique because both carry, and `{6,10}`
forces the **larger** cover. The selector is a prime-support selector, not a
smaller-is-better principle. It can fail and it can pick the larger cover.

`C3` records the honest asymmetry in the read semantics: `(6 beta_1)^2 = 36/5`
exceeds 1 so factor absorption is unavailable at `m = 6`, but
`(2 beta_1)^2 = 4/5` is below 1, so at `m = 2` the exclusion of a rescale rests
on the read semantics of `DRIFT-IS-THE-READ [T]`, not on the coherent range.

## Falsifiers

None of `F1` to `F8` fired.

```text
F1  no symmetric integer accumulator satisfies the diagonal identity at m = 2
    within the frozen box; 390625 candidates, zero hits.
F2  the typed projection witness passed every identity and clause check.
F3  no coefficient-system conclusion disagreed with a brute-force conclusion
    on any shared point.
F4  no dyadic ANON TOTAL accumulator was found at m = 6 in either frozen
    family; 1922375 + 1922375 candidates, zero hits.
F5  the orbit-count and basis cross-checks passed at every tested (m, D).
F6  the ring table agreed with the independent cross-check of B8.
F7  no float appears in any assertion or emitted field; the verifier uses only
    int and Fraction, and exact pairs for Q(sqrt5).
F8  the local aarch64 leg and the required GitHub x86_64 leg produced the
    identical stdout hash
    5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa,
    so the transcripts do not differ.
```

The two architectures therefore complete the computation gate of `POLICY.md`
section 4 for this verifier: the local formal leg is `aarch64`, the required
GitHub leg is `x86_64`, and their stdout is byte identical. See `RUN.md` for
both records.

## Status earned

The frozen boxes of `A4` in `PREREG.md` are explicit that the enumerative legs
assert nothing beyond themselves, and that the all-`m`, all-degree content of
`B` rests on the written symbolic proof. `A6` of the same field states that a
public status resting only on the finite boxes is at most `C`.

Accordingly:

```text
A   exhibition. The witnesses are explicit and finite and the statement is a
    pure existence claim, so it is theorem grade on its own terms.
B   the classification is theorem grade by the symbolic argument, which is
    four lines and checkable by hand; the verifier audits it rather than
    establishing it. The three exhaustion legs are corroboration.
C   a scope statement, not a result.
```

No status is claimed in the public registry by this probe. Whether any row is
folded, and at what grade, is a separate reviewed Canon fold under
`POLICY.md` section 5. The promotion proposal
`notes/canon/PROMO-C-READ-REDUNDANCY-1.md` is the input to that decision and
carries no authority of its own.

## Scheduler effect on the parent row

None, and this was frozen before execution. `MINIMAL-READ-DERIVATION [O]`
keeps its own decision text: failure of one favored route is `STOP` unless it
classifies the complete registered decoder class. This probe classifies one
clause pair, `ANON` against `TYPED` and `TOTAL` against `PART`, not the class.
The row stays `O` and `STOP`. `COIN-MINIMAL-READ [H]` is untouched.
`GATE-L5-L1-MINIMAL-READ` is not touched. Declared layer `L5` over the `L1`
coin carrier; no lift is performed and no `L6`, measurement, Born, SI,
decoherence or unique-physics content appears anywhere.

What the probe does supply to the parent row is a reduction: the two decoder
definitions the `O` row already lists as missing, the cover-to-output map and
the accumulator equality rule, are now two named bits with known prices,
anonymity and totality.
