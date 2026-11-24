# C-RH-JACOBI-GROWTH-LADDER-N — review record 2026-09-16

```text
STATUS      NON-CANONICAL review record; no verifier; no evidence
DATE        2026-09-16
OBJECT      notes/C-RH-JACOBI-GROWTH-LADDER-N.md, blob 2b556852eac7fcae009f2dec0fcb5995fb358544,
            SHA-256 1eaa6f995b4331468fce8cfd456247191e279083e5aaa61cd29d6a8dc80c396c, 16578 bytes,
            commit 22c967b3a7458e88634578e06a066cca84949342 on the branch of PR #1031
LOCK        #1030
BASIS       Public Canon v87, main 5c9a494de3f4b9856c292a77d35280fb086a0404
AUTHORITY   none; no Canon, Registry, Frontier, gate, evidence or claim-status motion
```

The reviewed note is left byte-identical so that the hashes recorded in #1030
stay true. Where this record narrows or corrects a sentence of the note, the
reading given here is the intended one.

## 1. Method

This is the third static mathematical review of the note and the first with a
recorded method. It is independent of the two reviews named in the note's
section 9, which are reported in #1030 without a separate record.

Eight referee runs, each with a disjoint brief matching one of the note's own
failure tests (normalization (3)-(8); power coefficient (9)-(11); dyadic
Cauchy-Schwarz (12)-(14); identification (15)-(16); shadow threshold (17)-(18);
accumulating family (19)-(21); sharpness model and section 8; scope and
consistency), were instructed to refute, to rederive independently, and to
ignore the note's own review sentence. Any finding graded fatal or gap was to
be sent to three further independent verifiers with the opposite brief; no
such finding arose, so that stage did not run. Exact rational arithmetic on
small-`n` identities (formula (9) for `n <= 8`, orthogonality of `e_n`,
`R_n(0)`, `d_n(1)`, `d_n(2)`, `d_n(3)`) was used only as a reading aid.

No numerical work on zeta values or zeros was done. Nothing here is evidence
for (12), (19) or (21), which remain open exactly as the note states.

## 2. Verdict

**HOLDS.** The conditional implication (1), the exact coefficient (9), the
shadow threshold (17), the growth obstruction (18) and the accumulating-family
consequence (20) stand as stated, at candidate-T. No fatal defect and no
repairable gap was found. The items below are wording corrections; none
changes a conclusion.

## 3. Corrections and intended readings

1. **Section 4, sentence after (11).** "Positive integral alpha values cause no
   problem: the relevant coefficients eventually vanish" is false at
   `alpha = 1`: from (9),

   \[
   d_n(1)=(-1)^n\frac{\sqrt{2n+3}}{(n+1)(n+2)}\ne0\qquad(n\ge0),
   \]

   checked exactly for `n <= 6`. The sentence is true for integer
   `alpha >= 2`, where `d_n(alpha) = 0` for `n >= alpha - 1` (checked exactly
   for `alpha = 2, 3`). Since `alpha = 1` is not an apparent singularity of
   (10) and is covered by (11), nothing else is affected. Intended reading:
   "Integer `alpha >= 2`, the only apparent singularities of (10) in
   `Re alpha > 1/2`, cause no problem: `d_n(alpha) = 0` for `n >= alpha - 1`.
   At `alpha = 1` the coefficients are `(-1)^n sqrt(2n+3)/((n+1)(n+2))` and
   satisfy (11)."

2. **Section 3, sentence after (8).** "Both displayed terms have residue
   `c_epsilon`" is to be read as: `c_eps/(s-1)` and `zeta(s)/(s zeta(s+eps))`
   each have residue `c_eps` at `s = 1` (because `zeta(1+eps) != 0` for real
   `eps > 0`), so their difference is removable there.

3. **Section 4, qualifier before (10).** (10) is an identity for every
   `n >= 0` and every `alpha` outside the poles `-1, ..., -(n+1)`, with
   `Gamma(n+2-alpha)/Gamma(2-alpha)` read as `(-1)^n prod_{j=2}^{n+1}(j-alpha)`
   at integer `alpha >= 2`. "Sufficiently large `n`" is only what keeps
   `Gamma(n+2-alpha)` pole-free on a fixed compact set; it is not a
   restriction on the identity.

4. **Section 5, (14).** The blocks `B <= n < 2B` with `B = 2^b >= 1` do not
   contain `n = 0`. The omitted term `u_0 d_0(alpha) = sqrt(3) u_0/(alpha+1)`
   is one holomorphic term on `Re alpha > -1`. Intended reading: "the `n = 0`
   term is treated separately."

5. **Section 6, hypothesis.** The growth hypothesis (12), for the same fixed
   `eps` and `kappa`, is in force throughout section 6; the first paragraph
   uses it through domain (1) without restating it. The boxes carry no
   hypothesis inside them. Intended readings:

   - (17): "Under (12) for fixed `eps` and `kappa >= 0`, every nontrivial zero
     `rho` satisfying (2) has `ord_{rho-eps} zeta >= ord_rho zeta`."
   - (18): "If `rho = beta + i gamma` has no shadow `rho - eps` of
     multiplicity at least `ord_rho zeta`, then
     `limsup_N log(1+A_N(eps))/log(N+2) >= 4 beta - 2 - 2 eps`."

6. **Section 7, (21).** The open target is displayed in a box like the proved
   statements (9), (17), (18). The prose says it is open and not claimed; the
   box marks the target, not a result.

7. **Section 6, "nonreal".** The fact used, that no nontrivial zero is real,
   is the classical `zeta(sigma) != 0` for real `0 < sigma < 1`: with
   `eta(sigma) = sum (-1)^{n-1} n^{-sigma} > 0` (alternating series with
   decreasing terms) and `1 - 2^{1-sigma} < 0`, one has
   `zeta(sigma) = eta(sigma)/(1 - 2^{1-sigma}) < 0`. It belongs with the
   imports of section 9.

8. **Section 9, third bullet.** "Isolation of analytic zeros" is the identity
   theorem for analytic functions (for instance Ahlfors, *Complex Analysis*,
   third edition, chapter 4, section 3.2), not a statement of DLMF 25.2, 25.4
   or 25.10; those cover the zeta facts in the same bullet.

9. **Header and section 9, status vocabulary.** `candidate-T` is used as in
   the source note's section 0: an analytic derivation exists without
   independent public analytic review. This record is a review of that kind;
   it confers no status.

## 4. Observations, not defects

- **(16) is unconditional for `Re alpha > 2`.** From (4) and (15),
  `|u_n| <= (2/(1-delta)) sqrt(2n+3) (n+1)(n+2)/2 = O(n^{5/2})`, so with (11)
  the terms of (13) are `O(n^{3 - 2 Re alpha})` and (13) converges and equals
  `M_eps(alpha - delta)` on `Re alpha > 2` without (12). The hypothesis (12)
  is used only to extend holomorphy leftward to the half-plane in (1).
- **(11) holds on all of `Re alpha > -1`,** locally uniformly; the restriction
  to `Re alpha > 1/2` is needed only for summability in (14).
- **Sharpness for every exponent.** The family `g_a(t) = t^{-a}`, `1/2 < a < 2`,
  satisfies (4), has `u_n = d_n(1-a)`, hence `|u_n|^2 asymp n^{4a-3}` and
  `A_N asymp N^{4a-2}`, and its Mellin pairing `1/(s + delta - a)` has its
  pole at `s = 1/2 - eps/2 + (4a-2)/4`. So the factor `1/4` in (1) is attained
  for every `kappa = 4a - 2` in `(0, 6)`, not only for `kappa = 1`. In the
  note's model the error term in `u_n^*` is in fact `O(n^{-2})`.
- **Section 8, consistency with the unconditional domain.** `M_eps` is
  holomorphic on `Re s > 1 - eps` unconditionally: its only possible poles are
  `s = 0`, the shifted trivial zeros `-2k - eps`, and the shadows `rho - eps`
  with `Re(rho - eps) < 1 - eps`; `s = 1` is removable. For `kappa = 2 - 2 eps` the half-plane in (1) is
  exactly `Re s > 1 - eps`, which restates (22): the current exponent yields
  nothing beyond the known boundary. A power saving `eta` must stay bounded
  away from zero along an accumulating family for the line `Re s = 1 - eta/4`
  to be reached.
- **Section 3 dictionary.** `b_{n,k}` in the source are the coefficients of
  `R_n` in (5), so `a_n = int_0^1 g_eps(t) t R_n(t) dt` and
  `u_n = sqrt(2n+3) a_n`; the source's scalar `A = N + 2` is unrelated to
  `A_N`.
- **Section 5, (15).** The maximum is attained at `t = 0` (Jacobi argument
  `x = -1`) because the parameter `2` exceeds the parameter `0`
  (Szego, Theorem 7.32.1).
- **Section 7.** The limit `eps_* = 0` lies outside the range
  `0 < eps <= 1/4` of section 3 but is never used as a parameter. The
  multiplicity clause of (17) is not needed for (20); one shadow zero per `j`
  suffices.

## 5. Steps independently rederived and confirmed

- (3)-(4): `0 <= h_eps <= 1`, `0 < c_eps < 1`, `|F_eps(x)| <= 2x`,
  `t |g_eps(t)| <= 2 t^{-delta}`; on `t > 1`, `g_eps = c_eps t^{-1-delta}` with
  squared norm `c_eps^2/(1+eps)`.
- (5): the displayed coefficients of `R_n` agree with `P_n^{(0,2)}(2t-1)` and
  with the Rodrigues form (exact, `n <= 8`); orthogonality
  `int_0^1 t^2 R_n R_m = 1_{n=m}/(2n+3)`; completeness by the isometry
  `f -> t f` of `L^2((0,1), t^2 dt)` onto `L^2(0,1)`.
- (6)-(7): `u_n = sqrt(2n+3) a_n`, `A_N = L_N - c_eps^2/(1+eps)`; (7) is (8)
  at `s = k + 2 - delta` and agrees with the source's (35).
- (8): substitution `x = 1/t`, `sum h_eps(n) n^{-s} = zeta(s)/zeta(s+eps)`,
  Fubini for `Re s > 1`, both residues `c_eps` at `s = 1`.
- (9): `n`-fold integration by parts of the Rodrigues form with boundary
  terms `O(t^{alpha+1})` at `0` and vanishing at `1`, beta integral
  `B(alpha+1, n+1)`; poles only at `alpha = -1, ..., -(n+1)`, zeros at
  `alpha = 2, ..., n+1`; exact termwise checks for `n <= 8`.
- (10): `prod_{j=2}^{n+1}(alpha-j) = (-1)^n Gamma(n+2-alpha)/Gamma(2-alpha)` and
  `prod_{j=1}^{n+1}(alpha+j) = Gamma(alpha+n+2)/Gamma(alpha+1)`.
- (11): DLMF 5.11(iii) gives
  `Gamma(n+2-alpha)/Gamma(n+2+alpha) = n^{-2 alpha}(1 + O_K(1/n))`, hence the
  exponent `1/2 - 2 Re alpha`.
- (12)-(14): block bound `C^{1/2} 3^{kappa/2} C_K B^{kappa/2 + 1 - 2a}`;
  negative exponent iff `a > 1/2 + kappa/4`, i.e. `Re s > 1/2 - eps/2 + kappa/4`
  with `alpha = s + delta`; Weierstrass gives holomorphy of (13). For
  `kappa = 0` this recovers the addendum's `H^2` statement.
- (15): Szego Theorem 7.32.1 with the larger parameter `2`,
  `max_{[0,1]} |R_n| = (n+1)(n+2)/2 = |R_n(0)|`; `R_n(0) = (-1)^n (n+1)(n+2)/2`
  exactly.
- (16): terms `O((n+1)^{3 - 2 Re alpha})`, summable for `Re alpha > 2`; `L^2`
  and pointwise identification of `sum d_n e_n` with `t^{alpha-1}` on `(0,1]`;
  interchange by `|int g_eps t^{alpha-1} - sum_{n<=N} u_n d_n| <=
  sup_{[0,1]} |phi - phi_N| int_0^1 t |g_eps|` with `phi_N = sum_{n<=N} d_n e_n/t`,
  using only (4).
- (1): identity theorem on the connected half-plane with the open overlap
  `Re s > max(2 - delta, 1/2 - delta + kappa/4)`; `s = 0` lies outside the
  half-plane, `s = 1` is removable, shadowed zeros of `zeta(s+eps)` are
  removable; the pairing is bilinear and holomorphic (`u_n` real, no
  conjugation).
- Sharpness model: `u_n^* = d_n(1/4) -> (-1)^n sqrt(2) Gamma(5/4)/Gamma(7/4)`,
  `A_N^* ~ 2 Gamma(5/4)^2 Gamma(7/4)^{-2} N`, `kappa = 1`, pole at
  `s = 3/4 - delta` exactly on the boundary of (1); `g_*` is not in `L^2`.
- (17): `s_0 = rho - eps` is strictly interior to (1) iff (2); `Im s_0 != 0`;
  the order of `zeta(s)/(s zeta(s+eps))` at `s_0` is `ord_{s_0} zeta - m`;
  holomorphy forces `ord_{s_0} zeta >= m` for every `m`.
- (18): `A_N >= 0` gives a nonnegative limsup; a `kappa` strictly between the
  limsup and `4 beta - 2 - 2 eps` yields (12) after enlarging `C`; (18) never
  contradicts the source's (38) for `beta <= 1`.
- (19)-(20): (2) holds for all large `j`; the shadows `rho - eps_j` are
  distinct zeros converging to the nonreal point `rho - eps_*`, contradicting
  isolation; no uniform bound on `C_j` is needed; `eps_* = kappa_* = 0` and
  `xi(s) = xi(1-s)` give RH.
- (21): `eps_j = 2^{-j} <= 1/4` iff `j >= 2`; `kappa_j = 2 eps_j -> 0`;
  individual threshold `beta > 1/2 + eps_j`; stated as open and not claimed
  equivalent to RH.
- (22): `kappa_current = 2 - 2 eps` read from the source's (38) through
  `A_N = L_N - c_eps^2/(1+eps)` and `A = N + 2`;
  `1/2 + eps/2 + (2 - 2 eps)/4 = 1`; the factor `exp(-sqrt(2 log A)/20)` lowers
  neither the polynomial exponent nor gives a power saving.

## 6. Not examined

- The source's finite-degree bound (38) itself; only its consistency with the
  dictionary of section 3 was checked.
- The truth of (12) for the arithmetic `g_eps` at any `kappa < 2 - 2 eps`, of
  (19), or of (21). The note claims none of them; this is the whole remaining
  analytic debt.
- The promotion package `PROMO-C-RH-JACOBI-GROWTH-LADDER-N` named in section
  9; no such file exists in this branch, and none is required by the lock.

## 7. Handoff: proposed next lock, not claimed here

The natural continuation is a converse to (1): does the growth exponent of
the arithmetic energy equal, rather than merely bound, the quantity
`4 (sigma_hol - 1/2 + eps/2)`, where `sigma_hol` is the abscissa of
holomorphy of `M_eps`? A converse of this kind would show that target (21)
is not weaker in disguise but sits at exactly the strength of the
shadow-free statement "`M_{eps_j}` holomorphic on `Re s > 1/2` with a vertical
growth condition, for a sequence `eps_j -> 0`".

Two ingredients would be needed, and both are open here:

1. a justified Mellin-Parseval representation
   `u_n = (2 pi i)^{-1} int_{(c)} M_eps(w - delta) d_n(1-w) dw` on a vertical
   line inside the holomorphy domain, with `Re w < 2` so that `d_n(1-w)` is
   defined; the pairing conditions are not automatic, because only (4) is
   known for `g_eps`, and the line must be chosen so that both sides are
   square integrable or the integrand is absolutely integrable;
2. a bound for `d_n(1-c-it)` uniform in `n` and `t`, from Stirling's formula
   applied to (10); the expected shape is
   `sqrt(n) |t|^{1-2c} (n+|t|)^{2c-2}` up to constants, and the absolute-value
   step is where the loss against the true energy is to be expected. The
   factor `1/s` in (8) is what makes a vertical growth hypothesis on `M_eps`
   plausible at all.

The exact growth hypothesis, and whether it is implied by RH on the relevant
lines, are to be fixed under the new lock; nothing about them is asserted
here. Neither the converse nor any energy bound is proved in this record.
