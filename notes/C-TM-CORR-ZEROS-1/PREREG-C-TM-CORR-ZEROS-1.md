# PREREG C-TM-CORR-ZEROS-1

CANDIDATE. NON-CANONICAL. Carries no authority, promotes nothing, edits no
normative file. Incubation lane of the TWIST J project.

```text
candidate id      C-TM-CORR-ZEROS-1
target line       public, mathorn1973/twist-j
proposed claim    TM-CORR-ZEROS
proposed status   T for the zero-set statement, C for the finite range checks
session           Cowork, claude-opus-5, one named session for this candidate
frozen (UTC)      2026-07-30
basis             Public Canon v27, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
                  main HEAD        b0a53eb65e3a3511af28f5876b9d1bb882bda160
                  tag              canon-v27 -> b0a53eb65e3a3511af28f5876b9d1bb882bda160
                  CONTENT_COMMIT   116b62edf505914d96fcd65318d97f3675c53f85 (ancestor of HEAD)
                  CANON_SHA256     c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
                  CANON_BYTES      150959
                  canon/SHA256SUMS 5 of 5 OK
                  tools/check_canon.py  CANON PASS v27 claims=214
provenance        extracted from the pre-axiom article "Twist J: Beyond Complex
                  Numbers", Claim 2, which asserted the zero classification as a
                  finite check to k <= 10000 with no proof and no registry row.
collision check   no AUTOCORR, CORR-ZERO or TM-CORR row in canon/REGISTRY.tsv at
                  v27; grep of canon/ for "autocorrelation" returns no claim row.
```

## 1. Equation

Let `s_2(n)` be the binary digit sum, `t_n = s_2(n) mod 2` the Thue-Morse bit,
and

```text
u_n = (-1)^t_n in {-1, +1},        S_k(N) = sum_(0 <= n < N) u_n u_(n+k).
```

Define the balanced two-point correlation

```text
c(k) = lim_(N -> infinity) S_k(N)/N.
```

The claim has three parts.

**L1 (exact dyadic self-similarity).** For all integers `m >= 0`, `N >= 0`

```text
S_(2m)(2N)     = 2 S_m(N),
S_(2m+1)(2N)   = -( S_m(N) + S_(m+1)(N) ).
```

**L2 (existence and recursion).** For each fixed `k` the limit `c(k)` exists,
`c` is the unique solution of

```text
c(0) = 1,      c(2m) = c(m),      c(2m+1) = -( c(m) + c(m+1) )/2,
```

so `c(k) in Q` for every `k`, and the discrepancy obeys a logarithmic bound:
with `L(k)` the binary length of `k`,

```text
| S_k(N) - c(k) N |  <=  2^L(k) ( 2 log_2 N + 2 )        for all N >= 1.
```

**T (the zero set).** For every integer `k >= 1`,

```text
c(k) = 0   <=>   oddpart(k) in {5, 7},
```

that is, the zero set is exactly
`{ 5 * 2^a : a >= 0 } union { 7 * 2^a : a >= 0 }`. Equivalently `c(k) = 0` iff
`k in {5, 7, 10, 14, 20, 28, 40, 56, ...}`. `c(0) = 1` is not zero and `k = 0`
is excluded.

**Proof to be checked, stated before execution.** Put `u_m = c(m) + c(m+1)`,
`w_m = c(m) - c(m+1)`, `U_m = 3 u_m`, `W_m = 3 w_m`. The recursion gives the
two transfer maps on the binary tree `m -> (2m, 2m+1)`

```text
Lambda_0 (U, W) = (  W/2,  U + W/2 ),
Lambda_1 (U, W) = ( -W/2, -U + W/2 ),
```

with root `(U_0, W_0) = (2, 4)` and `Lambda_0` fixing the root. Then
`c(2m+1) = -U_m/6`, so odd-index zeros are exactly the `m` with `U_m = 0`.
Direct evaluation gives `(U_1, W_1) = (-2, 0)`, `(U_2, W_2) = (0, -2)`,
`(U_3, W_3) = (0, 2)`, and `(U_m, W_m) = (+-1, +-1)` for `m in {4, 5, 6, 7}`.
2-adic valuation induction: if `v_2(U) = v_2(W) = -t` is finite then in both
branches `v_2(U') = -t-1` and `v_2(W') = min(-t, -t-1) = -t-1`, both finite.
Hence `v_2(U_m) = v_2(W_m) = -(L(m) - 3)` for all `m >= 4` and neither
coordinate ever vanishes again. Therefore `U_m = 0` iff `m in {2, 3}`, i.e.
`c(k) = 0` for odd `k` iff `k in {5, 7}`; `c(2m) = c(m)` extends this to
`oddpart(k) in {5, 7}`. The statement `W_m = 0` iff `m = 1` is the same lemma
and records that `c(1) = c(2)` is the unique coincidence of neighbours.

## 2. Code

```text
verifier   verify_tm_corr_zeros_1.py
breaker    break_tm_corr_zeros_1.py
rules      Python standard library only; Fraction and integer arithmetic only;
           no float anywhere in any assertion or any printed field; under 120 s;
           run from the working directory with
           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
           deterministic output, no wall-clock, no hostname, no nickname
```

Verifier gates, all exact:

```text
V1  zero set on 1 <= k <= 200000 by memoized rational recursion
V2  L1 identities for all 0 <= m <= 300, 0 <= N <= 300 by direct integer sums
V3  L2 discrepancy bound for 0 <= k <= 64, N in 1..4096, exact rational compare
V4  valuation lemma: base cases m in {0,1,2,3} and
    v_2(U_m) = v_2(W_m) = -(L(m) - 3) for all 4 <= m <= 2^18
V5  deep k by transfer-matrix product on the binary expansion, pinned list
    including 5*2^100, 7*2^100, 5*2^400, 7*2^400 and fixed large non-{5,7}
    odd parts; zero iff oddpart in {5, 7}
```

Breaker gates, independent code path:

```text
B1  brute-force integer counting of S_k(N) at N = 2^22 for 1 <= k <= 2000,
    no Fraction, no recursion: separation test between the predicted zeros and
    the predicted non-zeros
B2  matrix-product implementation of c disagreeing nowhere with the memoized
    recursion on 0 <= k <= 20000
B3  adversarial deep search: 256 pseudorandom k of 512 bits from a pinned seed
    list, plus every k = q * 2^a with q odd, q <= 4001, a <= 64
B4  convention sweep: complemented Thue-Morse (t_0 = 1) and the reversed
    correlation S_k with negative shift
B5  the {0,1}-weighted correlation, recorded as a different function with a
    different zero set, to fence the scope of the claim
```

## 3. Carrier and data

No experimental data, no external file, no network. The carrier is the drive
word of the public kernel: the Thue-Morse cut `theta_n = s_2(n) mod 2` of the
counter, as declared in `canon/CORE.md` and used by `TIME-CUT-READING [D]` and
`RAMIFIED-TM-LIFT [T]`. The claim is a statement about that word alone. It is
independent of `F_5^6`, of the five generators, of the selector and of the
decoder, and it does not depend on any architecture choice.

## 4. Systematics

```text
S1  convention. u_n = (-1)^t_n with t_0 = 0. Complementing the word maps
    u -> -u and leaves every product u_n u_(n+k) fixed, so the claim is
    invariant under the choice of fixed point. B4 checks this.
S2  weighting. The claim is about the balanced (+-1) correlation. The
    {0,1}-weighted correlation sum(t_n t_(n+k))/N is a different function with a
    different zero set. B5 records it so no reader can transfer the claim.
S3  normalization. c(k) is a Cesaro mean over n, not a mean over k, and not a
    Fourier coefficient of the Thue-Morse measure.
S4  the limit. Existence is part of the claim (L2), not an assumption. The
    discrepancy bound is checked on a finite range only; the bound itself is
    proved, and the constant 2^L(k) is not optimal and is not claimed to be.
S5  prior art. The recursion for c is classical in the literature on Thue-Morse
    correlations. Two current sources were read at abstract level only
    (arXiv 2209.07102; Ramanujan J. s11139-021-00434-7) and neither abstract
    states the zero classification. NO PRIORITY IS CLAIMED. A full literature
    clearance is an explicit open obligation of this candidate and a precondition
    of any public fold; the mathematical content stands on the proof either way.
S6  no float. Any float in the code path is itself a failure of the gate.
```

## 5. Failure threshold

Binary, exact, no tolerance. The candidate fails if any of the following holds.

```text
F1  some k with 1 <= k <= 200000 and oddpart(k) not in {5,7} has c(k) = 0
F2  some k with 1 <= k <= 200000 and oddpart(k) in {5,7} has c(k) != 0
F3  some (m, N) with m <= 300, N <= 300 violates an L1 identity
F4  some (k, N) in the V3 range violates the discrepancy bound
F5  some m with 4 <= m <= 2^18 has v_2(U_m) != -(L(m) - 3) or
    v_2(W_m) != -(L(m) - 3), or a base case m in {0,1,2,3} differs from the
    pinned value
F6  the deep-k transfer-matrix path disagrees with the zero classification on
    any pinned k, or disagrees with the memoized recursion where both apply
F7  the breaker exhibits any k with oddpart(k) not in {5,7} and c(k) = 0, or any
    p != 1 with c(p) = c(p+1)
F8  any float appears in an assertion or an emitted field
```

A fired falsifier is archived, not deleted, and the threshold is not moved after
the fact. If F1, F2, F6 or F7 fires, the extracted claim is dead and the article
row that carried it stays dead with it.

Registry falsifier text proposed for the public row:

```text
fires if any k >= 1 with oddpart(k) not in {5, 7} has c(k) = 0, if any k with
oddpart(k) in {5, 7} has c(k) != 0, if the 2-adic valuation lemma fails at any
m >= 4, or if the aarch64 and x86_64 transcripts differ
```

## 6. Action layer

```text
declared layer   L5, the drive stream. The claim is a statement about the mean of
                 a product of two positions of the drive word.
not claimed      no L6 lift. c(k) is not asserted to be a physical measure, a
                 spectral density, a decoder output or an observable. The word
                 "anti-resonance" is descriptive and carries no physical status.
                 Any lift to L6, and any use of the value 5 in the zero set as
                 evidence about p = 5, needs its own named gate and is refused
                 here.
fence            the coincidence that the smallest zero is at the prime of the
                 algebra is recorded as a coincidence at this layer. The zero set
                 {5, 7} is a fact about base 2 and the digit sum; nothing in the
                 proof uses zeta_5, J, or F_5^6.
```

## 7. Action on outcome

```text
pass   package PROMO-C-TM-CORR-ZEROS-1 with the exact statement, the proof, the
       verifier and breaker pins, and the registry, frontier and canon edits a
       public fold would make. Promotion still requires the public two-platform
       pinned run and an independent proof reading. No promotion by living here.
fail   archive the fired falsifier in the candidate record, mark the extracted
       article claim F, and record which of F1..F8 fired.
```
