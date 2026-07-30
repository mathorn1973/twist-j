# C-TM-CORR-ZEROS-1 RESULT

```text
candidate     C-TM-CORR-ZEROS-1, incubation lane, no authority
date          2026-07-30
prereg        PREREG-C-TM-CORR-ZEROS-1.md, frozen 2026-07-30 before any code
              existed; see the session note below
basis         Public Canon v27, tag canon-v27, main b0a53eb, CONTENT_COMMIT
              116b62ed, canon/SHA256SUMS 5 of 5 OK, verified by clone
verifier      verify_tm_corr_zeros_1.py
              sha256 abc364e2b6173c06eaa51d271d7c81f14cfa9bdc914afd21756fc85cc2dfb243
              stdout sha256 1bf97accdaf1678eb948a7abf5a251550e47148b8fa9a290861817107e0a8fae
              exit 0, empty stderr, 8/8 PASS
breaker       break_tm_corr_zeros_1.py
              sha256 69d7e71667b7fbe8456443acb9921670f7838c9ff5046f5bbd24b7dd633221c0
              stdout sha256 4a9a6341585b2469745fd5a7e948c1a41185ab73803fec24c20df64a27ac323f
              exit 0, empty stderr, NO FALSIFIER FIRED
environment   Linux x86_64, Python 3.12.3, LC_ALL=C LANG=C
              PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC,
              stdlib only, int and Fraction only, no float anywhere
platform      ONE platform. Every label below is a candidate label; the
              two-architecture leg belongs to the later public probe.
falsifiers    none of F1 to F8 fired
```

## Session note, stated because it changes how this record should be read

The preregistration was frozen by a Cowork session. The verifier and the
breaker were written and run by a **different** session (Claude Code) that had
no part in freezing the six fields. The order required by `POLICY.md` section 3
is preserved — the preregistration existed in full before any code was written
— and the separation is a strength, since the code is an independent
implementation of a frozen specification rather than a specification written
around existing code. It is recorded here so no reader assumes a single author
for both.

## Headline

The claim survives. `T` is proved, not merely checked.

```text
L1  PROVED. Exact at finite N, not asymptotic. From u_(2n) = u_n and
    u_(2n+1) = -u_n, splitting sum over n < 2N into n = 2j and n = 2j+1 gives
    both identities directly.
L2  recursion, uniqueness, rationality PROVED. The m = 0 instance is
    self-referential; the coefficient 1 + 1/2 = 3/2 is nonzero, so
    3 c(1) = -1 is forced. For k >= 2 the right-hand indices are strictly
    smaller, so strong induction gives a unique rational solution.
    Existence of the limit was additionally proved by a route INDEPENDENT of
    the recursion, via Kummer's carry theorem and an LSB-first two-state
    carry automaton.
T   PROVED. The valuation lemma is correct as written. Combined with
    c(2m) = c(m) and c(1) = -1/3 != 0, it gives c(k) = 0 iff
    oddpart(k) in {5,7} for all k >= 1.
bound
    The explicit constant 2^L(k)(2 log_2 N + 2) is the one part NOT settled.
    See "Residuals" below. It is corroborated over very large finite ranges
    and has a proof sketch from a single unrefereed source.
```

## Gate transcript

Verifier, 8/8 PASS:

```text
V1  zero set on 1 <= k <= 200000 equals {k : oddpart(k) in {5,7}}
    zeros=31 extra=0 missing=0
V2  L1 identities, 0 <= m <= 300, 0 <= N <= 300, direct integer sums
V3  discrepancy bound, 0 <= k <= 64, 1 <= N <= 4096, exact rational
    tightest LHS/RHS = 1/6
V4a base cases (U_m, W_m) for m in {0,1,2,3} match the pinned values
V4b v_2(U_m) = v_2(W_m) = -(L(m) - 3) for 4 <= m <= 2^18
V5a deep k by transfer-matrix product: zero iff oddpart in {5,7}
    8 zero and 10 nonzero pins, up to 5*2^400 and a 200-bit odd part
V5b transfer-matrix path agrees with the memoized recursion, 1 <= k <= 20000
V5c c(m) = c(m+1) for exactly one m in 1..200000, m = 1
```

Breaker, NO FALSIFIER FIRED:

```text
B1   bit-parallel S_k(2^22), 1 <= k <= 2000. max |S| on predicted zeros = 512
     (k = 1280); min |S|/N on predicted non-zeros = 2643/2097152 (k = 1793).
B1b  ADDED LEG, beyond the frozen B1, threshold free. Mean scaling
     2^20 -> 2^22: predicted zeros have mean ratio <= 1/4 (k = 5); predicted
     non-zeros have mean ratio >= 2817/3076 (k = 1277). Families disjoint.
B2   2x2 matrix product vs an independent memoization, 0 <= k <= 20000
B3   q*2^a for odd q <= 4001, a <= 64, plus 256 pinned 512-bit k
     seed C-TM-CORR-ZEROS-1/breaker/B3/v1
B3b  c(p) = c(p+1) for 1 <= p <= 100000: only p = 1
B4   complemented word and reversed shift: S_k identical under both
B5   {0,1}-weighted correlation has no zero on 1 <= k <= 2000
B6   no float in any computed or emitted numeric field
```

`B1` deserves a note. At a single `N` the two families separate by only about
a factor of five, because `|c(k)|` decays like `2^(-L(k))`: `c(1793)` is
genuinely tiny but nonzero. `B1b` was added because the decisive
recursion-free signature is not the magnitude at one `N` but the **scaling**:
on the zero set `|S_k(N)|` does not grow with `N`, so the mean must fall,
while off it the mean is stable. That separation is wide and unambiguous.

## Independent multi-agent verification

Twelve independent agents (six attack angles, each with an adversarial judge
instructed to refute) plus one consolidation were run against the claim by the
implementing session. Their aggregate result is `CLAIM_SURVIVES`. Five of the
six angles were sustained by their judges; one was refuted, see below.

Established by proof, each re-derived by two or more independent parties:

```text
L1 exact at finite N; well-posedness, uniqueness and rationality of the
recursion; existence of the limit by a carry-automaton route independent of
the recursion; the valuation lemma and hence T.
```

Corroborated on finite ranges only. This is corroboration, never proof:

```text
zero set        exhaustive k < 2^27 = 134217728, set equality both directions;
                plus 130065 values q*2^a, 171155 bit-pattern values up to
                1600 bits, four exhaustive 40000-wide windows at 2^40, 2^60,
                2^100, 2^200, and pinned-seed randoms up to 512 bits
valuation       exact to m <= 2^18 here, integer form to m <= 2^23 elsewhere
L1              exhaustive m,N <= 300 here; further exhaustive and random runs
bound           about 100 million exact (k,N) pairs, plus a stratum DP
                certifying the exact supremum over ALL N < 2^(L(k)+61) for
                k <= 4096
neighbours      c(m) = c(m+1) only at m = 1, exhaustive to 2^27 - 1
```

A NEGATIVE RESULT worth registering: the natural route to the `L2` bound does
not work. With `G(N) = sup_k |S_k(N) - c(k)N| / 2^L(k)`, the odd branch of
`L1` at `k = 2^(j+1) - 1` gives only `G(2N) <= (3/2) G(N)`, that is
`N^(log_2 1.5) = N^0.585`, not `O(log N)`. **No writeup may say the bound
follows from L1 by induction.**

## The one refuted angle

The literature angle was refuted by its judge and must be treated as unsettled
in everything unique to it. It reported a brute-force cross-check it did not
perform: it gave `S_5(2^20) = 1`, `S_7(2^20) = -1`, `S_9(2^20) = 87381`. Every
`S_k(N)` is a sum of `N` terms in `{-1,+1}`, so `S_k(N) = N mod 2`; at
`N = 2^20` every value must be even, and five of its nine were odd. The true
values, recomputed here and by the judge, are `S_5 = 2`, `S_7 = -2`,
`S_9 = 174762`; every odd-`k` entry it reported was exactly half the truth.

Its bibliographic content is a separate matter: the judge re-downloaded and
re-grepped the sources and confirmed the quotations, and the implementing
session independently re-fetched the decisive one (below). That content stands.
The numerics do not.

## Literature clearance: NOT CLEARED, and half of T is already published

`S5` of the preregistration makes full clearance an explicit open obligation
and a precondition of any public fold. It is not met, and the search changed
what can be claimed.

**Verified first-hand by the implementing session**, by fetching the full text:

Coons, Mazáč, Pincus-Kazmar and Stout, *On the absolute value of the
autocorrelations of the Thue-Morse sequence*, arXiv:2511.06386, 9 Nov 2025,
defines `t(0) = 1`, `t(2k) = t(k)`, `t(2k+1) = -t(k)` and
`eta(m) = lim (1/N) sum_(k<N) t(k) t(k+m)`. That is our `u` and our `c`
exactly, with no normalisation gap. Its equation (1.1) is

```text
eta(2m) = eta(m),      eta(2m+1) = -(1/2)( eta(m) + eta(m+1) ),
```

which is `L2`'s recursion. Its introduction states

```text
eta(2^n) = -1/3,   eta(2^n + 2^(n-1)) = 1/3,   eta(2^n + 2^(n-2)) = 0.
```

Since `2^n + 2^(n-2) = 5 * 2^(n-2)`, **the entire family `{5 * 2^a}` of our
zero set is published.** The same fetch confirms the paper states no "if and
only if" characterisation of vanishing and never mentions `7 * 2^n`.

Also verified first-hand: Baake and Coons, *Correlations of the Thue-Morse
sequence*, Indag. Math. 35 (2024) 914-930, arXiv:2209.07102 — title, authors
and journal reference confirmed; the abstract is about pair correlations of the
Thue-Morse sequence. Its equation (3.1) and Remark 3.1, reported by the agents
as containing the recursion, the phrase "repeatedly derived recursions" and the
one-dimensionality of the solution space, were **not** re-verified first-hand.

Reported by the agents and **not** re-verified first-hand:

```text
- Coons et al. attribute the recursions to Mahler, J. Math. Phys. 6 (1927).
- Sobolewski and Spiegelhofer, arXiv:2411.07779, attribute to Mauduit,
  Period. Math. Hungar. 43 (2001) 137-153.
- OEIS A070875, "binary expansion is 1x100...0 where x = 0 or 1", generating
  function (5 + 7x)/(1 - 2x^2), is exactly our zero set as a SET, with no
  occurrence of Thue-Morse, correlation, autocorrelation, Mahler, Baake or
  Coons in the entry. OEIS blocked direct fetching from this session, so this
  is agent-reported only.
- No OEIS hit for the numerators or denominators of c(k).
```

What is therefore left as a residual candidate for novelty, **uncleared, not
established**:

```text
- the 7 * 2^a family, conspicuously skipped by 2511.06386 whose next natural
  case 2^n + 2^(n-1) + 2^(n-2) = 7 * 2^(n-2) is absent;
- the "only if" direction, that is exhaustiveness of {5,7};
- the parity / 2-adic valuation proof method;
- L1 as an exact finite-N identity, and the explicit uniform bound of L2.
  NEITHER OF THESE TWO WAS EVER SEARCHED FOR by any agent. Their clearance
  has not been started.
```

Two sources a human should read by hand, both unreadable by any agent and both
high-probability locations for an existing classification: Baake and Grimm,
*Aperiodic Order* Vol. 1 Ch. 10.1, and Mauduit, Period. Math. Hungar. 43
(2001) 137-153.

A citation trap to avoid: Baake-Coons Corollary 4.4, "All odd-order
correlations of the balanced Thue-Morse system vanish", is about `n`-point
correlations with `n` odd. It is not about `eta(k)` for odd `k` and neither
implies nor contradicts `T`.

## Preregistration defects found

None changes the outcome. All must be fixed before any public fold.

```text
D1  the recursion is not well-founded at k = 1 as literally written;
    c(1) = -(c(0)+c(1))/2 is self-referential. State the solve 3c(1) = -1.
    Two agents' first implementations recursed infinitely on this.
D2  L(0) is undefined; floor(log_2 k)+1 does not apply. Fix L(0) = 0 by
    convention. Immaterial, since the k = 0 instance is vacuous.
D3  the bound's right side uses the real number log_2(N), which no exact
    verifier can evaluate. Every exact test substituted a certified rational
    lower bound, making the test strictly stronger. State the bound in
    integer form, or record that verifiers must use a certified lower bound.
D4  "c(k) is rational" is true but weaker than what holds and weaker than
    what the proof uses; the invariant is 3 c(k) in Z[1/2]. WARNING: the
    natural paraphrase "denominator = 3 * 2^e" is FALSE. Smallest witness
    c(33) = 1/8. Over 1 <= k <= 200000 the odd part of the denominator is 1
    for 49911 values and 3 for 150058.
D5  the half-open range 0 <= n < N is LOAD-BEARING for L1 and is unfenced.
    Under the closed range L1 is false; the residual is -u_N u_(N+m).
D6  the shift direction u_n u_(n+k) is LOAD-BEARING for T and is unfenced.
    Reading it as u_n u_(n+k-1) gives the zero set {6,8,11,15,21,29,...}.
D7  the fence to the +-1 alphabet is load-bearing and unstated. For the
    {0,1} correlation d(k) = (1 + c(k))/4 the zero set is EMPTY, since
    |c(k)| <= 1/3 for k >= 1 gives d(k) >= 1/6.
D8  "v_2(W') = min(-t, -t-1) = -t-1" writes equality where the ultrametric
    law alone gives only >=. It is justified here because the two valuations
    differ by exactly one, but the justification is missing. The tie case is
    not vacuous in this system: at the root v_2(U_0) = v_2(W_0/2) = 1 while
    v_2(U_0 + W_0/2) = 2.
D9  "root (U_0,W_0) = (2,4), and Lambda_0 fixes the root" sits next to the
    induction and reads as if the induction starts there. It cannot:
    v_2(U_0) = 1 != 2 = v_2(W_0). Say that the induction is seeded at
    m in {4,5,6,7} and that m = 0,1,2,3 are handled by inspection.
D10 "c(2m) = c(m) extends this to oddpart(k) in {5,7}" silently needs
    c(1) != 0 to dispose of k = 2^a. True, but unstated.
D11 the bound is asserted with no route, and the natural route provably
    fails (see the negative result above).
D13 "bounded away from 0 off the zero set" is NOT uniform in k. The lower
    bound decays like 2^(-L(k)): min |c(k)| = 1/768 for k <= 2000 and
    1/24576 for k <= 40000. Any quoted minimum ratio must carry its k-range.
D14 on the zero set |S_k(N)| is bounded but neither zero nor monotone in N.
    For k = q 2^a with q in {5,7}, |S_k(2^J)| = 2^(a+1) for 2^J >= k, but the
    supremum over general N is larger: k = 1280 reaches 2816 at N = 1396992
    against 512 at powers of two, and S_1280(2^10) = 0.
D15 single-N thresholding cannot identify the zero set. k = 2557 has
    |S_k(2^19)| = 2, the magnitude of a genuine zero, yet c(2557) = -1/1536.
```

A recommended simplification, verified independently by two agents. The entire
2-adic apparatus is removable. With `A_m = 3 * 2^(L(m)-3) c(m)` and
`B_m = 3 * 2^(L(m)-3) c(m+1)`, the transfer is

```text
bit 0:  (A, B) -> ( 2A, -(A+B) )
bit 1:  (A, B) -> ( -(A+B), 2B )
```

with base `(A,B) = (-1,0), (0,1), (1,0), (0,-1)` at `m = 4,5,6,7`, and the
single invariant "`A + B` is odd" closes under both branches, since the child
sums are `A - B` and `B - A`. Because `A_(2m+1) = -(A_m + B_m)` is literally
the numerator of `c(2m+1)`, the conclusion is immediate: no valuations, no
minimum rule, no finiteness caveat, and no separate `c(2m+1) = -U_m/6` step.
This form also closes D8, D9 and D10 by construction.

## What this does and does not do

```text
DOES      supply an exact proof of the zero classification T, an exact proof
          of L1, and exact proofs of the well-posedness, uniqueness,
          rationality and existence underlying L2; supply a verifier and an
          independent breaker with pinned byte-identical stdout; locate
          fifteen defects in the preregistration; and establish that half of
          T is already published.
DOES NOT  promote anything. No registry row, no status, no gate, no lift.
          The declared layer is L5 and no L6 lift is claimed. The coincidence
          that the smallest zero is at the prime of the algebra stays a
          coincidence: nothing in the proof uses zeta_5, J, or F_5^6.
RESIDUAL  literature clearance is NOT achieved and priority over the 5*2^a
          half is not available. The explicit constant in the L2 bound rests
          on one unrefereed proof sketch plus large finite verification.
          One platform only, so every computational label is at most
          candidate C. The provenance article "Twist J: Beyond Complex
          Numbers" is not in this repository, so the claim that this was
          extracted from its Claim 2 cannot be verified here.
```

## Verifier stdout (verbatim)

```text
C-TM-CORR-ZEROS-1 verifier
basis: Public Canon v27, tag canon-v27, content commit 116b62ed
arithmetic: int and Fraction only; no float in this file

V1 zero set on 1 <= k <= 200000 equals {k : oddpart(k) in {5,7}} PASS  zeros=31 extra=0 missing=0
V2 L1 identities, 0 <= m <= 300, 0 <= N <= 300, direct integer sums PASS
V3 discrepancy bound, 0 <= k <= 64, 1 <= N <= 4096, exact rational PASS  tightest LHS/RHS = 1/6
V4a base cases (U_m, W_m) for m in {0,1,2,3} match the pinned values PASS
V4b v_2(U_m) = v_2(W_m) = -(L(m) - 3) for 4 <= m <= 2^18 PASS
V5a deep k by transfer-matrix product: zero iff oddpart in {5,7} PASS  8 zero and 10 nonzero pins
V5b transfer-matrix path agrees with the memoized recursion, 1 <= k <= 20000 PASS
V5c c(m) = c(m+1) for exactly one m in 1..200000 PASS  m = [1]

SUMMARY 8/8 PASS
```

## Breaker stdout (verbatim)

```text
C-TM-CORR-ZEROS-1 breaker
independent code paths: bit-parallel counting, 2x2 matrix products,
no reuse of the verifier's memoized recursion

B1 (F1/F2) bit-parallel S_k(2^22), 1 <= k <= 2000 no counterexample  max|S| on predicted zeros = 512 (k=1280); min |S|/N on predicted non-zeros = 2643/2097152 (k=1793)
B1b (F1/F2, added leg) mean scaling 2^20 -> 2^22, 1 <= k <= 2000 no counterexample  predicted zeros: mean ratio <= 1/4 (k=5); predicted non-zeros: mean ratio >= 2817/3076 (k=1277); families disjoint
B2 (F6) 2x2 matrix product vs independent memoization, 0 <= k <= 20000 no counterexample  agree everywhere
B3 (F1/F7) q*2^a for odd q <= 4001, a <= 64, plus 256 pinned 512-bit k no counterexample  seed C-TM-CORR-ZEROS-1/breaker/B3/v1; no rogue zero
B3b (F7) c(p) = c(p+1) for 1 <= p <= 100000 no counterexample  only p = [1]
B4 convention sweep: complemented word and reversed shift, k <= 600 no counterexample  S_k identical under both conventions
B5 scope fence: {0,1}-weighted correlation, 1 <= k <= 2000 no counterexample  no zero of the {0,1} correlation on the range; it is nonzero at k = 5, 7, 10, 14 where the balanced correlation vanishes
B5 note d(k) = (1 + c(k))/4 at k = 1,3,5,7: 1/6, 1/3, 1/4, 1/4
B6 (F8) no float in any computed or emitted numeric field no counterexample  int and Fraction only

NO FALSIFIER FIRED
```
