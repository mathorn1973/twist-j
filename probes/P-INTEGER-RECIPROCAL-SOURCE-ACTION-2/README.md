# Integer source-metric impulse and mixed-variation model

NON-CANONICAL, L1. Ownership issue:
https://github.com/mathorn1973/twist-j/issues/1642.

This probe extends `P-INTEGER-PRIMITIVE-SOURCE-METRIC-1` (Draft PR #1641) with:

1. **Finite coupling-selection classification (`Theorem B2`):** Checks that
   `c_1 = coeff_j((H-R)_01)` is the unique coordinate among the eight fixed
   canonical coordinate projections of `Herm_2(Z[j])` extracting `+sigma` on the
   prepared loop, that the 20 signed pair dipoles `e_r - e_s` are the minimal
   zero-sum integer vectors in `Z^5 \ {0}` (fixing `ell = (1,-1,0,0,0)` on the
   marked support `{0,1}`), and that `kappa = 2` is the minimal positive even
   integer factor preserving the 2-adic primitive denominator
   `d_n = 2 * 324^(n-1)`.
2. **Full-carrier reversible parity impulse and mixed variational audit
   (`Theorems B1, B3-B5`):** Adds the phase-6 parity-difference feedback
   `Phi(P,Q) = (P_0 mod 2 - P_1 mod 2) - (Q_0 mod 2 - Q_1 mod 2)` into the
   source register `s' = s + Phi(P,Q)`, preserving the 38-coordinate core
   injection, the 40-coordinate reversible funded bijection `F^-1 = Rev F Rev`
   with conserved `E + b`, the exact primitive denominator `d_n = 2 * 324^(n-1)`,
   and the all-counter Lorentzian signature bound `-299/500 < h_n(r) < 499/500`
   (`||h_n - h_n^free||_inf < 1645/209304 < 1/125`) across all ten canonical
   words and `a in {-1,0,+1}`. On ready trajectories, `Phi(P,Q)` acts as a
   one-time initial impulse `beta(w) = Phi(P_1, P_0)` at the first field gate
   (`k=1 -> 2`), followed by the six-periodic source oscillator
   `chi_n = a*(1,2,2,1,0,0)_n + beta(w)*(0,1,2,2,1,0)_n`. The variational audit
   verifies 600 vanishing reduced TT metric variations and 120 source variations
   equal to `tau_n = <ell, h_n>/324^n` with single-integer coordinate optimality
   `A_rec(chi) - A_rec(chi + k e_n) = k^2/2 - k tau_n > 0` for `k in Z \ {0}`.

## Read and reproduce

- `PREREG.md` freezes the carrier, fixtures, falsifiers, and certificate grammar.
- `PROOF.md` gives the frozen derivations (see `RESULT.md` and `REVIEW.md` for
  explicit post-pin errata and scope corrections).
- `SOURCE.md` identifies the actual Public Canon v103 bytes, non-canonical
  companions, consumed predecessor pin, and declared modeling choices.
- `verify.py` uses the polynomial quotient ring `Z[j] = Z[x]/(1+x+x^2+x^3+x^4)`
  and `2x2` Hermitian matrices.
- `breaker.py` independently uses direct 8-coordinate integer formulas and
  explicit `C/L` matrices.
- `FROZEN.sha256` commits the five prospective source files.
- `EXPECTED.txt` is the exact first formal stdout (`844` bytes, `27` lines).
- `RUN.md`, `RESULT.md`, and `REVIEW.md` record execution custody, validated
  scope, and explicit frozen-proof errata.

From the repository root, using Python 3.12 and the standard library:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 probes/P-INTEGER-RECIPROCAL-SOURCE-ACTION-2/verify.py

Expected successful output ends with:

    CERTIFICATE_RESULT=PASS
    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The complete output must match `EXPECTED.txt` byte for byte. The unchanged
repository PR workflow performs this replay on both `x86_64` and `aarch64`.

## Limits and errata summary

On ready histories, `Phi(P,Q)` is a one-time initial impulse rather than
sustained feedback at every counter, and the continuous source derivative of
`A_rec` equals `tau_n = <ell, h_n>/324^n` on-shell, which is generally nonzero
(satisfying single-integer coordinate optimality rather than continuous source
stationarity). Explicit errata in the frozen `PROOF.md` text (including the
withdrawal of section 3.2) are documented in `RESULT.md` and `REVIEW.md`.
Sustained every-step feedback and continuous joint stationarity (`dA/dh = 0` and
`dA/dchi = 0`) are established in the separate successor probe
`P-INTEGER-JOINT-VARIATION-1` (Draft PR #1646, issue #1645).
