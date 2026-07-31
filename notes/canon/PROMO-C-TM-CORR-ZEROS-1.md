# PROMO-C-TM-CORR-ZEROS-1

Promotion proposal. One doc a fold can consume without reading anything else.
Candidate carries no authority; validation is public, not here.

```text
CANDIDATE    C-TM-CORR-ZEROS-1
             prereg PREREG-C-TM-CORR-ZEROS-1.md, frozen 2026-07-30
TARGET       public line, mathorn1973/twist-j, as a new probe
             P-TM-CORR-ZEROS-1 plus one T row. Additive; no existing row
             changes status or scope.
PROPOSED BY  incubation lane, preregistration frozen by a Cowork session,
             code written and run by a separate Claude Code session
CONTEXT      the Thue-Morse cut theta_n = s_2(n) mod 2 declared in
             canon/CORE.md and used by TIME-CUT-READING [D] and
             RAMIFIED-TM-LIFT [T]
BLOCKER      literature clearance is NOT achieved and half of the statement
             is already published. Read section "Priority" before folding.
```

## Exact statement (proposed status T after the public probe)

Let `s_2(n)` be the binary digit sum, `t_n = s_2(n) mod 2`, `u_n = (-1)^t_n`,
and `S_k(N) = sum_(0 <= n < N) u_n u_(n+k)` over the **half-open** range.
Let `c(k) = lim_(N -> inf) S_k(N)/N`.

```text
T (proposed)  TM-CORR-ZEROS, layer L5 over the drive word, no lift.
  (i)   S_(2m)(2N) = 2 S_m(N) and S_(2m+1)(2N) = -(S_m(N) + S_(m+1)(N))
        exactly, for all integers m, N >= 0. Exact at finite N.
  (ii)  c(k) exists for every k, is the unique solution of c(0) = 1,
        c(2m) = c(m), c(2m+1) = -(c(m)+c(m+1))/2, and satisfies
        3 c(k) in Z[1/2].
  (iii) For every k >= 1, c(k) = 0 if and only if oddpart(k) in {5, 7};
        that is, the zero set is exactly {5*2^a} union {7*2^a}. k = 0 is
        excluded and c(0) = 1.
  (iv)  c(m) = c(m+1) holds for exactly one m >= 1, namely m = 1.
```

The scope must fence three load-bearing conventions, each of which changes the
statement if altered: the **half-open** summation range (under the closed range
(i) is false, residual `-u_N u_(N+m)`); the **shift direction** `u_n u_(n+k)`
(reading `u_n u_(n+k-1)` gives the zero set `{6,8,11,15,21,29,...}`); and the
**balanced +-1 alphabet** (the `{0,1}`-weighted correlation is
`d(k) = (1 + c(k))/4`, whose zero set is empty since `|c(k)| <= 1/3` for
`k >= 1`).

## Proof

Recommended form, which avoids 2-adic valuations entirely. Put

```text
A_m = 3 * 2^(L(m)-3) * c(m),      B_m = 3 * 2^(L(m)-3) * c(m+1),
```

with `L(m)` the binary length. The recursion gives the transfer

```text
bit 0:   (A, B) -> (  2A, -(A+B) )
bit 1:   (A, B) -> ( -(A+B),  2B )
```

with base `(A,B) = (-1,0), (0,1), (1,0), (0,-1)` at `m = 4, 5, 6, 7`. The
single invariant "`A + B` is odd" closes under both branches, since the child
sums are `A - B` and `B - A`, congruent to `A + B` mod 2. Because
`A_(2m+1) = -(A_m + B_m)` is literally the numerator of `c(2m+1)`, the odd
part of the numerator is never zero for `m >= 4`. Direct inspection gives the
remaining cases: `c(2m+1) = 0` exactly at `m = 2, 3`, so `c(k) = 0` for odd `k`
exactly at `k = 5, 7`. Every `m >= 8` has parent `floor(m/2) >= 4`, so descent
from any `m >= 4` terminates inside the base layer. Finally `c(2m) = c(m)`
extends the classification to all `k`, using `c(1) = -1/3 != 0` to dispose of
`k = 2^a`.

`(i)` follows from `u_(2n) = u_n` and `u_(2n+1) = -u_n` by splitting the sum
over `n < 2N` into `n = 2j` and `n = 2j+1`. `(ii)`'s well-posedness needs the
explicit solve of the self-referential instance `c(1) = -(c(0)+c(1))/2`, whose
coefficient `3/2` is nonzero, giving `3 c(1) = -1`; for `k >= 2` the
right-hand indices are strictly smaller. Existence of the limit was separately
established through Kummer's carry theorem and an LSB-first two-state carry
automaton, a route independent of the recursion.

## Priority. Read this before folding.

**Half of (iii) is already published.** Coons, Mazáč, Pincus-Kazmar and Stout,
*On the absolute value of the autocorrelations of the Thue-Morse sequence*,
arXiv:2511.06386 (9 Nov 2025), defines exactly this object and states in its
introduction

```text
eta(2^n) = -1/3,   eta(2^n + 2^(n-1)) = 1/3,   eta(2^n + 2^(n-2)) = 0,
```

and `2^n + 2^(n-2) = 5 * 2^(n-2)`, so the whole family `{5 * 2^a}` is
published. Its equation (1.1) is the recursion of `(ii)`. The recursion itself
is classical, traced in the literature to Mahler (1927) and surveyed in Baake
and Coons, *Correlations of the Thue-Morse sequence*, Indag. Math. 35 (2024)
914-930.

The residual candidates for novelty, **uncleared**, are: the `7 * 2^a` family,
which arXiv:2511.06386 conspicuously skips; the "only if" direction, that is
exhaustiveness of `{5,7}`; the parity proof method; and `(i)` as an exact
finite-`N` identity together with the explicit discrepancy bound — neither of
which has been prior-art searched at all.

Two sources a human must read by hand before any priority language is used:
Baake and Grimm, *Aperiodic Order* Vol. 1 Ch. 10.1, and Mauduit,
Period. Math. Hungar. 43 (2001) 137-153.

A trap: Baake-Coons Corollary 4.4, "All odd-order correlations of the balanced
Thue-Morse system vanish", is about `n`-point correlations with odd `n`. It is
not about `c(k)` for odd `k`.

The safe posture is to register the row on its proof and cite the prior art,
claiming no priority.

## Deliberately NOT proposed for the row

The explicit discrepancy bound `|S_k(N) - c(k) N| <= 2^L(k)(2 log_2 N + 2)` is
**not** proposed as part of the `T` row. It is corroborated over roughly 100
million exact `(k,N)` pairs and by a stratum argument certifying the exact
supremum over all `N < 2^(L(k)+61)` for `k <= 4096`, and it has a
carry-decomposition proof sketch, but that sketch comes from a single
unrefereed source. Register it, if at all, as a separate row at `C`, or leave
it on the frontier.

One negative result must travel with any writeup: the bound does **not** follow
from `(i)` by the natural sup-norm induction. With
`G(N) = sup_k |S_k(N) - c(k)N| / 2^L(k)`, the odd branch at `k = 2^(j+1) - 1`
gives only `G(2N) <= (3/2) G(N)`, that is `N^0.585`, not `O(log N)`.

## Falsifier (for the T row, inline)

```text
fires if any k >= 1 with oddpart(k) not in {5, 7} has c(k) = 0, if any k with
oddpart(k) in {5, 7} has c(k) != 0, if the parity invariant "A + B odd" fails
at any m >= 4, if the exact finite-N identities of (i) fail at any (m, N)
under the registered half-open convention, or if the aarch64 and x86_64
transcripts differ
```

## Layer and fence

Declared layer `L5`, the drive word. No `L6` lift. `c(k)` is not asserted to
be a physical measure, a spectral density, a decoder output or an observable.
Any lift, and any use of the value `5` in the zero set as evidence about
`p = 5`, needs its own named gate and is refused here. The coincidence that the
smallest zero sits at the prime of the algebra is recorded as a coincidence:
the zero set `{5,7}` is a fact about base 2 and the binary digit sum, and
nothing in the proof uses `zeta_5`, `J`, or `F_5^6`.

## Verifier and pins

```text
verify_tm_corr_zeros_1.py  sha256 abc364e2b6173c06eaa51d271d7c81f14cfa9bdc914afd21756fc85cc2dfb243
                           stdout 1bf97accdaf1678eb948a7abf5a251550e47148b8fa9a290861817107e0a8fae
                           exit 0, empty stderr, 8/8 PASS
break_tm_corr_zeros_1.py   sha256 69d7e71667b7fbe8456443acb9921670f7838c9ff5046f5bbd24b7dd633221c0
                           stdout 4a9a6341585b2469745fd5a7e948c1a41185ab73803fec24c20df64a27ac323f
                           exit 0, empty stderr, NO FALSIFIER FIRED
```

ONE platform so far, Linux x86_64, Python 3.12.3. The public probe must rerun
the merged verifier on two architectures with byte-identical stdout; until
then every computational label is a candidate label and a computation-only row
is at most `C`. The proof of `(iii)` is independent of that and is short
enough to check by hand.

## Dependency edges

```text
Uses      nothing. The statement is about the Thue-Morse word alone and is
          independent of F_5^6, the five generators, the selector and the
          decoder. It touches the same word that TIME-CUT-READING [D] and
          RAMIFIED-TM-LIFT [T] read, but derives nothing from either.
No edits  to any existing row's status or scope. Additive only.
```

## Exact edits the fold would make

```text
1  probes/P-TM-CORR-ZEROS-1/: PREREG.md (six fields, public wording, with the
   defects D1 to D15 of the candidate record fixed), verify.py (merge of the
   candidate verifier and breaker legs into one file), EXPECTED.txt, RUN.md,
   RESULT.md after the two-platform run.
2  canon/REGISTRY.tsv: add the T row above with its inline falsifier
   (schema: claim_id status scope canon_section evidence falsifier;
   evidence probes/P-TM-CORR-ZEROS-1).
3  canon/CANON.md: fold owner's call. If the row is added, the prior-art
   sentence must travel with it.
4  canon/EVIDENCE.tsv, DEPENDENCIES.tsv, HISTORY.tsv, and the generated views
   per the usual fold procedure. Integer-versioned sealed fold, new hashes,
   no squash.
```

## Claim check before folding

Check issues, branches, `probes/` and the registry for collisions first. As of
2026-07-30 against `main` at `b0a53eb`: no `TM-CORR`, `AUTOCORR` or
`CORR-ZERO` row in `canon/REGISTRY.tsv`; no occurrence of "autocorrelation"
anywhere in `canon/`; no remote branch, probe directory or open issue naming
the correlation question.
