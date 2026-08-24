# Audit of the T1 Hausdorff attack, weight theorem, truncation emptiness (2026-08-20)

```text
STATUS:      NON-CANONICAL INCUBATION NOTE, addendum to the T1 attack.
             REVISION 2. Revision 1 carried four errors, corrected at
             handoff commit addc4572 and re-verified independently; the
             withdrawn claims are named in the correction record below.
AUTHORITY:   none. The authoritative copy with all pins is
             mathorn1973/twistj-handoff PR #3, branch
             agent/rh-t1-weight-theorem, into PR #2's branch
             agent/rh-hausdorff-t1-attack, head addc4572.
PARENT LOCK: mathorn1973/twist-j issue #374, C-RH-WEIL-NORM-JUNCTION-1-N
FIREWALL:    no RH proof, no evidence for RH, no Canon, Registry, Frontier
             or status movement, no L1-L6 lift. Model statements are about
             model functions, never about zeta.
```

## Currency gate

The parent report `RH-HAUSDORFF-T1-ATTACK-2026-08-20.md` reads back Public
Canon v54. That basis has moved twice during this work.

```text
main            362e9c3a9afa9f63005eaf0a1c03baac66617012
STATE           ACTIVE, Public Canon v55, cutover 2026-08-19
TAG             canon-v55, ancestor of main
CONTENT_COMMIT  6236c10cd89e0a3a53fca730f50c50c237d4add0, ancestor of main
CANON_SHA256    e22ebb5648611780743122da67ec965394c3f97ed18b99079be028ca6ebb47a9
CANON_BYTES     282461
SHA256SUMS      5 of 5 OK
v55 content     one row DE-W-CONSTANT [H] from P-DE-W-ARMING-1, nothing in
                the RH, zero, Weil or Hausdorff lane
head delta      since 70e1c480 four probe bundles were added and no file
                under canon/ changed
v54 basis       483591d3 is still an ancestor of main, no history rewritten
```

Side observation for open owner decision 3: three of the five stalled
candidate lanes have moved into public probes on this head.

```text
P-ENTROPY-RESIDUE-MATH-1     PROVED AND AUDITED / CANON UNCHANGED
P-J-LI-CARRIER-NOGO-1        PROVED AND AUDITED / CANON UNCHANGED
P-KERNEL-SUBSET-LANDSCAPE-1  DECIDED AND AUDITED / CANON UNCHANGED
P-PENTAGON-ONLY-DILATIONS-1  PROVED AND AUDITED / ROUTE DEAD / CANON UNCHANGED
```

Still unmoved: `C-C8-BILINEAR-SHADOW-1` and `C-COLOR-MEASURE-DIM-1`.

## Audit verdict on the parent report

Exact-arithmetic confirmation, independent code path: the `C_{n,j}` rows
derived from scratch by symbolic differentiation of `M(sqrt x)/(2 sqrt x)`
and only then compared to the closed form; `Q_{n,r}(0)` and the leading
coefficient; the `C_p` closed form of 5.2 including the enclosure that
yields exactly `641/4800`; `b_6` for `alpha = 1/4 + i`;
`Re(q(1-q)) = -7/100` for `alpha = 2/5 + i/5`.

Numerical cross-check, `mpmath`, NOT exact arithmetic: `M(1)`, `A_1`, `A_2`
reproduce every printed digit, and the section 4 Euler formula matches the
zero side and direct differentiation of `xi'/xi` on the sampled rows. This
is `[R]` grade, not confirmation.

No finding of substance against the parent report. The order-200 run is
neither confirmed nor contradicted here.

## The three new rows, candidate-T

Notation of the parent report: `q_P = 1/(1 - alpha_P^2)`,
`H_{n,r} = sum_P m_P q_P^{n+1} (1 - q_P)^r`.

**W1, the family is one Weil explicit-formula row.** With
`gamma_rho = (rho - 1/2)/i`, real exactly on the critical line and complex
off it,

```text
H_{n,r} = (1/2) sum_rho h_{n,r}(gamma_rho),
h_{n,r}(t) = t^{2r} / (1 + t^2)^{n+r+1},
integral over R of h_{n,r}(t) exp(-i u t) dt = pi exp(-|u|) Q_{n,r}(|u|).
```

So `Q_{n,r}` is the polynomial factor of the Fourier transform of its own
test function, the boxed Euler formula is Weil's explicit formula for it,
and the `1/2` is the functional-pair halving. For `r >= 1`, `h_{n,r}` peaks
at `t^2 = r/(n+1)`: a band-pass weight on real zero height. The filter
language is literal only for real `gamma_rho`, hence on the critical line.
For `r = 0` it is a low-pass, not a band-pass.

**W2, exact moments.** `h_{n,r}` vanishes to order exactly `2r` at the
origin, so

```text
integral over (0,inf) of t^{2k} exp(-t) Q_{n,r}(t) dt
    = 0                for 0 <= k < r,
    = (-1)^r (2r)!     for k = r.
Finite integer form: sum_j q_{n,r,j} (j + 2k)! = 0, resp. (-1)^r (2r)!.
```

Elementary proof of `k = 0` with no Fourier step: `sum_j C_{m,j} j! = 1`
for every `m`, so `int exp(-t) Q_{n,r} = sum_l (-1)^l binom(r,l) = 0`.

**W3, exact sign-change count.** `Q_{n,r}` has exactly `r` sign changes on
`(0, infinity)`, for every `n`. Lower bound: if it had `s < r`, then
`prod_i (t^2 - t_i^2)` lies in the span of `1, t^2, ..., t^{2r-2}`, so W2
forces a vanishing integral of a one-signed integrand. Upper bound: write
`exp(-t) Q_{n,r}` as a positive-weight integral of `L_r^{(n)}(y)` against
`exp(-t^2/(4y))`; in `u = t^2` and `w = -1/y`, both increasing on
`(0,infinity)`, the kernel is `exp(u w/4)`, strictly totally positive,
hence variation diminishing.

**What W2 and W3 unify, and what they do not.** They strengthen parent 5.1
from odd `r` to every `r >= 1` with an exact count, and they explain parent
5.3: the Laguerre route has a positive kernel but a source with exactly `r`
sign changes, so it preserves the oscillation rather than removing it.
They do NOT imply parent 5.2 and they do NOT imply parent 5.4. For
`Q_{0,1}` the complete prime-`p` contribution is
`C_p = L x (L - (1-x))/(4(1-x)^2) > 0` for every prime, so grouping does
rescue that row; 5.2 needs its own `Q_{1,1}` computation, which gives
`C_2 < 0 < C_11`. And a positive measure can integrate a sign-changing
function to zero, so 5.4 needs its own signed-density argument.

## Two truncation-emptiness lemmas, candidate-T

The admissible class `A` is the model class: even real entire `X` of order
at most `1/2`, `X(0) != 0`, centred zeros closed under `alpha -> -alpha`
and conjugation, `|Re alpha| < 1/2`, `sum m_alpha/(1+|alpha|^2) < infinity`,
`alpha != +-1`. "Model RH" means every `alpha` purely imaginary. RH-empty
means positivity of the subfamily does not imply model RH on `A`; it is not
a counterexample to anything zeta-specific.

```text
LEMMA A  For every r0 there is an admissible X with an off-critical zero
and H_{n,r} > 0 for every n >= 0 and every r <= r0.
alpha_0 = i, alpha_1 = 1/10 + i T, T = 2^(r0+2). Then |z_1| < T^-2 and
|1 - z_1| < 2, so the perturbation is below 2^{1+r} T^{-2(n+1)} <
2^{-(n+1)-r}, because (n+1)(2 r0 + 3) > 1 + 2 r for all n >= 0, r <= r0.

LEMMA B  For every n0 there is an admissible X with an off-critical zero
and H_{n,r} > 0 for every r >= 0 and every n <= n0.
alpha_0 = i, alpha_1 = 1/N + i/2. The choices must be made R first, then N.
Pick an integer R depending only on n0 with 2 (5/3)^(n0+1) 2^(-R) < 1.
Then pick one N large enough that simultaneously 2|z_1| <= 5/3,
2|y_1| <= 1/2, and (n0+1)|arg z_1| + (R-1)|arg y_1| < pi/2. Such N exists
because z_1 -> 4/5, y_1 -> 1/5 and both arguments tend to zero. For r < R
the off-critical term is itself positive; for r >= R the critical-pair term
dominates by the displayed envelope.
```

Consequence: T1' needs both parameters unbounded. The unconditional
`A_1(1), A_2(1), A_3(1) > 0` of parent section 7 does not reduce the
model-RH equivalence and gives no quantitative control of the unbounded-`r`
tail. Strictly stronger than parent section 8, which excluded only finite
subsets.

## Phase, candidate-T

For off-critical `alpha = delta + i T`, `0 < delta < 1/2`, `T > delta`, and
`z_1 = 1/(1 - alpha^2)`:

```text
arg z_1 > 0 > arg(1 - z_1),
arg z_1 = 2T/(1+T^2) delta + O_T(delta^3),
|arg(1-z_1)| = 2/(T(1+T^2)) delta + O_T(delta^3),
ratio of the linear coefficients exactly T^-2.
```

Along the continuous ray `r = T^2 (n+1)` the first-order terms cancel and

```text
Theta/(n+1) = 2(1+5T^2)/(3T(1+T^2)^2) delta^3 + O_T(delta^5),
             = 10/(3T^3) delta^3 + O(T^-5) for large T.
```

The cubic coefficient is **positive**. Sign opposition and first-order
cancellation are established; no universal phase obstruction follows, and
no general statement is made about where an off-critical quartet must turn
negative.

## Sparse detection reconnaissance, model reading only

```text
[R, NON-FORMAL] background: first 300 true ordinates; injected quartet
alpha = delta + iT; sparse sign grid, n to 600, r in powers of two to 262144.
  T = 16, delta = 45/100   sampled negative cell (n,r) = (200, 65536)
  T = 20, delta = 45/100   (200, 65536) and (400, 131072)
  T = 30, delta = 45/100   none on the sampled grid
A naive small-n scan over r to 60000 found nothing at T in {14,20,30,60,100}.
```

These are finite-grid observations, not consequences of W1 to W3 or of the
phase row. No first-detection claim and no asymptotic bound.

## J7 SOURCE

Still `[O]`. The obligation is that for every `n, r >= 0`

```text
sum_{m>=2} Lambda(m) m^{-3/2} Q_{n,r}(log m) <= sum_j q_{n,r,j} E_j,
```

which by W1 is the prime side against the archimedean side of Weil's
explicit formula for `h_{n,r}`. By W2 and W3 direct pointwise positivity of
`Q_{n,r}` is unavailable for `r >= 1` and the natural Laguerre
subordination retains a signed source; this does not rule out every
possible positive grouping, kernel or representing measure. The other two
local routes fail for their own exact reasons (5.2 by `Q_{1,1}`, 5.4 by the
explicit signed density). Lemmas A and B remove every bounded band in `n`
and in `r`. Any candidate transform must account for the zero of order `2r`
at the origin and the resulting exact moment and sign-change structure;
W2 and W3 do not prove that no such transform exists.

## Correction record

Revision 1 of this note and of the handoff report carried four errors,
found and corrected at handoff commit `addc4572`, then re-verified on an
independent exact code path in this session (`breaker_t1_corrections.py`,
C1 to C6 all SURVIVE).

```text
1  Band-pass ray cubic remainder. Revision 1 claimed
   arg z_1 - T^2 |arg(1-z_1)| = -2 delta^3 T/((1+s)s) + O(delta^5) and
   concluded a universal phase obstruction. WRONG: the arctan cubic terms
   are the same order in delta and were dropped. The correct coefficient is
   2(1+5T^2)/(3T(1+T^2)^2) > 0. Ratio of the true to the withdrawn leading
   term tends to -5/3. The universal phase obstruction is withdrawn.
2  Unification. Revision 1 claimed parent 5.1 to 5.4 are one corollary of
   W2 and W3. WRONG for 5.2 and 5.4; narrowed to 5.1 and 5.3.
3  W3 upper bound orientation. Revision 1 used v = 1/y, making the kernel
   exp(-uv/4) in two increasing variables. WRONG: that kernel has strictly
   negative 2x2 minors, it is sign regular, not totally positive. The
   correct orientation is w = -1/y, kernel exp(uw/4).
4  Lemma B quantifiers. Revision 1 chose R after N. Corrected to R first
   from n0 alone, then one N satisfying three explicit uniform bounds.
Also sharpened: W2 now states the k = r moment exactly, (-1)^r (2r)!.
Also downgraded: the verdict table now separates exact confirmation from
the mpmath cross-check, and the frontier cells are labelled sampled.
```

## Pins

```text
verify_t1_weight_theorem.py
  1762bfca2d9f07046f633cbcb3b30727ac6bbabd4235511cf6c3086f29620988
  25760 bytes, stdlib only, exact arithmetic, no float in any assertion,
  exit 0, 19 of 19 PASS
verify_t1_weight_theorem.stdout.txt
  8c827b62a240c79c078c27936f286728b203abc71bf41cd886b6a9b307f9eee6
  1696 bytes, BYTE-IDENTICAL on three machines:
    macOS arm64 CPython 3.9.6
    Linux x86_64 Ubuntu 24.04.4 CPython 3.11.15  (two independent runs)
  environment
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
RH-T1-WEIGHT-THEOREM-2026-08-20.md
  2acfb2a0be30470e8cccecb1d8cbe0e47f34c4850824f1e936d73b762edfccc8
breaker_t1_weight_theorem.py
  575b3d727fa3b3718517721d72fa3ce2fd75e9313d2bf2a2c373ce9c90b8dc0c
  stdout b92bdc862fda12a8beff2aa2dd236609fb04d995220d98502cee3db19831a1d4
recon_t1_euler_crosscheck.py   [R, NON-FORMAL]
  059de9120d04f65ed39ba557c4cf738e08cc7e3e335a4cd8084edf7d580e73b4
  stdout b481073644060b0f06aaa477cc83be3ca43bda2af545a3322be2274457e3cbc1
recon_frontier_scan.py   [R, NON-FORMAL]
  17737ce7ec8ff7869da22b0c1e1f3e92879b5071d3c7a25f271f252a12ed49f4
  stdout f9745299b4434ab05cc25ab93587e9586fc1b6e0c7edf0f2be642b52ffec9ed9
handoff record
  PR https://github.com/mathorn1973/twistj-handoff/pull/3, draft, CLEAN,
  MERGEABLE, not merged. base agent/rh-hausdorff-t1-attack,
  head agent/rh-t1-weight-theorem, commits 0238211, 11d8520, addc4572,
  author A. M. Thorn <thorn@twistj.com>
parent PR #2
  commit 30e746f588fae339e4fb596298747806c9093d1a, base a06e629d
  RH-RAY-PICK-CONSOLIDATION-2026-08-20.md readback confirmed:
  bfe235ff950795253e9eac25926a104bfd8ec649e25771a26172c8220e621b3b,
  14957 bytes
```

## Falsifiers

```text
FC1  a triple (n,r,k) where sum_j q_{n,r,j} (j+2k)! is nonzero for k < r,
     or differs from (-1)^r (2r)! at k = r.
FC2  a triple (n,r,u), u > 0, where the Fourier transform of h_{n,r}
     differs from pi exp(-u) Q_{n,r}(u), or an admissible configuration
     where gamma_rho = (rho-1/2)/i does not give the W1 identity.
FC3  a pair (n,r) where the sign-change count of Q_{n,r} on (0,inf)
     differs from r.
FC4  an r0 for which the displayed X is not admissible or not
     off-critical, or a pair n >= 0, r <= r0 with H_{n,r} <= 0.
FC5  an n0 for which no R then N satisfy the displayed uniform bounds, or
     a pair n <= n0, r >= 0 with H_{n,r} <= 0.
FC6  an off-critical alpha with arg z_1 <= 0 or arg(1-z_1) >= 0, or a ray
     cubic coefficient differing from 2(1+5T^2)/(3T(1+T^2)^2).
FC7  irreproducibility of the pinned verifier.
```

## What this does not do

No probe, no preregistration, no public write, no branch in
`mathorn1973/twist-j`, no status change for RH or for lock #374. W1, W2, W3
and the two lemmas are candidate grade. The Weil explicit formula and
Bessel-kernel Fourier pairs are classical; new here are the identification
of `Q_{n,r}` with that transform, the exact moment and sign-change theorem
for this family, and the two truncation-emptiness lemmas.
