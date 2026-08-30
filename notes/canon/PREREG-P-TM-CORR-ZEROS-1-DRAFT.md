# PREREG P-TM-CORR-ZEROS-1 (public wording) — DRAFT

```text
DRAFT / NOT PINNED / NO PROBE / NO AUTHORITY / NO FORMAL RUN
Awaiting the owner disposition (a) of issue #690. On that disposition the
sequence is: a fresh object-lock issue claiming P-TM-CORR-ZEROS-1, then
this text pinned as probes/P-TM-CORR-ZEROS-1/PREREG.md with the pin
commit and file hashes recorded in the lock, then the accepted verifier,
and only then any formal gate execution. Drafting before the pin is
static preparation permitted by POLICY.md section 3; formal gates are not.
```

Source lane: `notes/C-TM-CORR-ZEROS-1` (candidate bundle, re-verified
byte-identically on `main` at `7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2`;
see issue #690) and the fold proposal
`notes/canon/PROMO-C-TM-CORR-ZEROS-1.md`. This draft is the candidate
preregistration rewritten in public wording with the defect ledger
D1–D15 of `C-TM-CORR-ZEROS-1_RESULT_2026-07-30.md` fixed in place. The
working map orders this lane as step 9.4 and forbids any parallel
contract.

## Priority posture (travels with the row)

**No priority is claimed for any part of this statement.** The `{5*2^a}`
zero family is published (Coons, Mazáč, Pincus-Kazmar, Stout,
arXiv:2511.06386, which also states the recursion as its equation (1.1));
the recursion is classical (Mahler 1927; surveyed in Baake–Coons, Indag.
Math. 35 (2024) 914–930). The row is registered on its written proof with
the prior art cited. Baake–Grimm, *Aperiodic Order* Vol. 1 Ch. 10.1, and
Mauduit, Period. Math. Hungar. 43 (2001) 137–153, must be read by a human
before any novelty language may ever be added anywhere; this row needs no
such language.

## 1. Equation (the claim, with its three load-bearing fences inside)

Let `s_2(n)` be the binary digit sum, `t_n = s_2(n) mod 2`,
`u_n = (-1)^(t_n)`, and, over the **half-open** range,

```text
S_k(N) = sum_(0 <= n < N) u_n u_(n+k),        c(k) = lim_(N->inf) S_k(N)/N.
```

Fences, each load-bearing (D5, D6, D7): the half-open range (under the
closed range part (i) is false; the residual is `-u_N u_(N+m)`); the shift
direction `u_n u_(n+k)` (the reading `u_n u_(n+k-1)` has zero set
`{6,8,11,15,21,29,...}`); the balanced `+-1` alphabet (the `{0,1}`-weighted
correlation `d(k) = (1 + c(k))/4` has empty zero set, since
`|c(k)| <= 1/3` for `k >= 1`).

Proposed row `TM-CORR-ZEROS [T]`, four parts:

```text
(i)   S_(2m)(2N) = 2 S_m(N) and S_(2m+1)(2N) = -(S_m(N) + S_(m+1)(N)),
      exactly, for all integers m, N >= 0.
(ii)  c(k) exists for every k and is the unique solution of c(0) = 1,
      c(2m) = c(m), c(2m+1) = -(c(m) + c(m+1))/2, where the k = 1
      instance is self-referential and is solved explicitly:
      c(1) = -(c(0) + c(1))/2 has the nonzero coefficient 3/2, giving
      3 c(1) = -1 (D1). The invariant is 3 c(k) in Z[1/2] (D4); the
      paraphrase "denominator = 3 * 2^e" is false and is not claimed.
(iii) for every k >= 1: c(k) = 0 iff oddpart(k) in {5, 7}; the zero set
      is exactly {5*2^a} union {7*2^a}; k = 0 is excluded, c(0) = 1.
(iv)  c(m) = c(m+1) holds for exactly one m >= 1, namely m = 1.
```

Convention: `L(k)` is the binary length of `k`, with `L(0) = 0` (D2);
the `k = 0` instance of every recursion clause is vacuous.

**Explicitly excluded from the row (D11, D13, D14, D15):** the explicit
discrepancy bound `|S_k(N) - c(k)N| <= 2^L(k)(2 log_2 N + 2)` is not part
of this claim (single unrefereed proof-sketch source; the natural sup-norm
induction provably gives only `N^0.585`); no uniform lower bound off the
zero set is claimed (the true lower bound decays like `2^(-L(k))`); no
finite-`N` magnitude statement on the zero set is claimed (`|S_k(N)|` is
bounded but neither zero nor monotone there); no single-`N` threshold
identifies the zero set (witness `k = 2557`), and the verifier uses exact
`c(k)` values only.

## 2. Proof to be audited (stated before execution)

The zero classification is proved, not sampled. Rescale by
`A_m = 3 * 2^(L(m)-3) c(m)`, `B_m = 3 * 2^(L(m)-3) c(m+1)`; the recursion
becomes the integer transfer

```text
bit 0:   (A, B) -> (  2A, -(A+B) )
bit 1:   (A, B) -> ( -(A+B),  2B )
```

seeded at the base layer `m in {4, 5, 6, 7}` with
`(A,B) = (-1,0), (0,1), (1,0), (0,-1)`; the cases `m in {0,1,2,3}` are
handled by direct inspection, not by the induction (D9). The single
invariant "`A + B` is odd" closes under both branches, so
`A_(2m+1) = -(A_m + B_m)`, the numerator of `c(2m+1)`, never vanishes for
`m >= 4`; direct evaluation gives `c(2m+1) = 0` exactly at `m in {2, 3}`,
that is odd zeros exactly at `k in {5, 7}`. Then `c(2m) = c(m)` extends
the classification to all `k`, using `c(1) = -1/3 != 0` to dispose of
`k = 2^a` (D10). No 2-adic valuation equality is used anywhere (the D8
route of the candidate record is retired in favor of the parity
invariant). Part (i) follows from `u_(2n) = u_n`, `u_(2n+1) = -u_n` by
splitting the sum; existence of the limit is established independently
through Kummer's carry theorem and an LSB-first two-state carry automaton.

## 3. Code (the accepted verifier, to be pinned with this preregistration)

One file `verify.py`, merging the candidate verifier legs (V1–V5) and the
breaker legs (B1–B6) of the source lane into one deterministic program:
Python standard library only; `int` and `Fraction` only, no float in any
assertion; any comparison involving `log_2 N` replaced by a certified
rational bound making the test strictly stronger (D3); environment
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`;
exit 0, empty stderr, stdout byte-identical to the committed
`EXPECTED.txt`. Gates: the exact finite-`N` identities of (i) on
exhaustive ranges under the registered fences; the recursion solve and
the `3 c(k) in Z[1/2]` invariant; the parity-invariant induction audit
with its base layer and the `m <= 3` inspection; the zero-set audit by
exact `c(k)` values on an exhaustive range; the (iv) uniqueness audit;
and the three fence breakers (closed range, shifted direction, `{0,1}`
alphabet) as negative controls.

## 4. Carrier or data

None external. The object is the Thue-Morse word alone; every quantity is
integer or rational and computed exactly in the verifier. No dataset, no
manifest.

## 5. Systematics and failure threshold

Falsifier (inline, for the row):

```text
fires if any k >= 1 with oddpart(k) not in {5, 7} has c(k) = 0; if any k
with oddpart(k) in {5, 7} has c(k) != 0; if the parity invariant "A + B
odd" fails at any m >= 4; if any exact finite-N identity of (i) fails at
any (m, N) under the registered half-open convention; or if the aarch64
and x86_64 transcripts differ
```

No threshold moves after the pin. A fired falsifier is merged, not
hidden. An integrity mismatch (pin, transcript, architecture) without an
exact mathematical negation is STOP, not a scientific falsifier.

## 6. Action layer

`L5`, the drive word; no lift. `c(k)` is not asserted to be a physical
measure, spectral density, decoder output, or observable. The proof uses
no `zeta_5`, no `J`, and no `F_5^6`; the appearance of `5` in the zero
set is a fact about base 2 and the binary digit sum and is recorded as a
coincidence. Any lift, and any use of the zero set as evidence about
`p = 5`, requires its own named gate and is refused here.

## Status ceiling and evidence path

The `T` status of the row rests on the written proof of section 2; the
two-architecture byte-identical run of the pinned verifier is the audit
(POLICY.md: an independent proof may earn `T`; the verifier is then an
audit). Computation-only parts remain at most `C` if the proof audit
fails. Evidence path after the formal run:
`probes/P-TM-CORR-ZEROS-1/` with `PREREG.md` (this text, pinned),
`verify.py`, `EXPECTED.txt`, `RUN.md` (neutral platform fields), and
`RESULT.md`; the pull request changes exactly that one probe directory.

## Collision block

At drafting (`main` = `7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2`): no
`TM-CORR`, `AUTOCORR`, or `CORR-ZERO` row in `canon/REGISTRY.tsv`; no
remote branch, probe directory, or open issue naming the correlation
question; the source lane and its promo are the only prior objects and
this draft continues them. The object-lock issue must re-scan at claim
time.
