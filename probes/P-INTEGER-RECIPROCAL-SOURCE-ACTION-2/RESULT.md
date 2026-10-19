# Result

Status: PASS  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Ownership: https://github.com/mathorn1973/twist-j/issues/1642  
Pin: 3ae3ea66e1e3c633c048ece10e3baf43f144d8c7

## Observed completed result

The first formal primary run (`verify.py`, polynomial quotient ring `Z[j]` and
`2x2` Hermitian matrix multiplication) completed with exit zero and empty
stderr. Its independent direct 8-coordinate integer and explicit `C/L` matrix
implementation (`breaker.py`) also completed with exit zero and empty stderr and
emitted the exact same 25-line certificate bytes, after which `verify.py`
appended its two terminal success lines. The 844-byte, 27-line final stdout has
SHA-256 `857a26b1a8caf10e90b56f0f2df222ea1d8557eb2f60a24ff6b32a8093d1bdd8`.
`EXPECTED.txt` contains those exact bytes. `RUN.md` records custody and the
local environment.

No preregistered falsifier fired. No fixture or threshold was changed after the
public pin. This is a completed gate, not an abandoned pin. The frozen six-file
bundle remains byte-for-byte unchanged from `3ae3ea66e1e3c633c048ece10e3baf43f144d8c7`.

| Finite audit | Observed result |
| --- | --- |
| Actual normative authority files | All 5 hashes and sizes match Public Canon v103 |
| Hermitian transports | 133 entries pass closure, inverse, determinant and cost checks |
| Full-carrier fixtures | 399 cores, 9576 funded entries, all declared inverse/account branches |
| Corrupt field images | 38 rejected by exact congruence; lower boundary also reflects |
| Coupling-selection audit | 34 coordinate-projection, 20-minimal-dipole and even-factor parity checks pass |
| Field history | 750 records through counter 24 across a in {-1, 0, +1}, all exact primitive denominators and metric bounds |
| History payload SHA-256 | e3831741acc15d0ec25bf84565e25e46cf23723191d80dd36a91a25594d3e3b2 |
| Mixed variational audit | 720 checks: 600 vanishing reduced TT metric central differences + 120 source central differences equal to tau_n with single-integer coordinate optimality |
| Complete funded cycles | Least periods 14,26,28,14,14,14,18,14 |
| Negative controls | Zero-amplitude source impulse, disabled backreaction, disabled metric coupling, omitted inverse backreaction, omitted inverse source, wrong first multiplier and unrestricted metric degeneracy behave as preregistered |
| Primary/breaker certificate | Unmodified 25-line certificate stdout bytes identical |

## Actual frozen construction and concrete witnesses

In the pinned construction (`PREREG.md` section 3, `verify.py` lines 245-277),
the phase-6 update reads

    Phi(P,Q) = (P_0 mod 2 - P_1 mod 2) - (Q_0 mod 2 - Q_1 mod 2),
    s' = s + Phi(P,Q),
    P' = C P - a(k) Q + 2 chi(H,R) ell,
    Q' = P, k' = k + 1, p' = 0,

leaving `H` unchanged during phase 6. The partial inverse at `p=0` first
recovers `(P_prev, Q_prev)` via the exact congruence divisor `a(k-1)` and then
subtracts `Phi(P_prev, Q_prev)` from `s`.

On every ready history, because `P_n == P_1 (mod 2)` for all `n >= 1`, the
feedback `Phi(P,Q)` equals

    beta(w) = Phi(P_1, P_0)
            = [(P_{1,0} mod 2) - (P_{1,1} mod 2)]
              - [(P_{0,0} mod 2) - (P_{0,1} mod 2)]

at the first field gate (`k=1 -> 2`; for example, at word `0010`,
`P_1 = (1,1,0,0,0)` and `P_0 = (0,1,1,0,0)` give `beta(0010) = 0 - (-1) = +1`)
and vanishes at every later gate (`k >= 2`). Thus on ready histories the
field-to-source coupling is a **one-time initial field-dependent impulse** into
the source register `s`, followed by the six-periodic source readout

    chi_n(a;w) = a * (1,2,2,1,0,0)_n + beta(w) * (0,1,2,2,1,0)_n,

satisfying `|chi_1| <= 1` and `|chi_n| <= 6` for `n >= 2` (attained at word
`0110`, `a=1`, `n=3`).

1. **Same-counter source-to-metric witness (`k=2`) and second-block witness (`k=3`):**
   At word `0010` (`beta(0010) = +1`), the same initial field data and common
   bank `347059` allow both `a=-1` and `a=+1` to reach `k=2` with primitive
   numerators

       P2(-)=(487,167,-230,130,94),
       P2(+)=(491,163,-230,130,94),
       h2(+)-h2(-)=(1,-1,0,0,0)/162,

   sharp first-block banks `344409` and `347059` (common final banks `2650` and
   `0`), and energy prefixes

       PREFIX_NEG  = 31,31,43,63,147,377,747,344440,
       PREFIX_ZERO = 30,30,30,40,40,30,30,345012,
       PREFIX_POS  = 31,31,43,63,147,377,803,347090.

   Advancing through block 2 to `k=3` yields primitive numerators

       P3(-)=(120111,-6141,-59422,98366,57038),
       P3(0)=(120977,-7007,-59350,98366,56966),
       P3(+)=(121843,-7873,-59278,98366,56894).

2. **Ready zero-amplitude source witness (`a=0`) at `k=3`:**
   For `a=0` at word `0010`, the ready state has `H = R = diag(0,1)` and
   occupied detector `Z = Z_0` (nonzero matrices with `H - R = 0` initially).
   At `k=2` the field equals the canonical free slice `P2(0) = P2(free) =
   (489,165,-230,130,94)`. The first-block impulse sets `s = +1`, producing
   `chi_2(0) = +1` in block 2 and a field response at `k=3`:

       h3(0) - h3(free) = (1,-1,0,0,0) / 104976.

## Validated mathematical scope and explicit frozen-proof errata

Following the public review (`https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6267871040`),
the valid mathematical claims certified by this probe and the explicit errata in
the frozen `PROOF.md` / `PREREG.md` text are recorded below without altering the
frozen files:

### Validated claims

- **Full-carrier reversible integer map (`B1`):** The 38-coordinate core step
  with `s' = s + Phi(P,Q)` is injective with exact partial inverse `Core^-1`,
  and the 40-coordinate reversible funded bijection satisfies `F^-1 = Rev F Rev`
  conserving `E + b`.
- **Finite coupling classification (`B2`):**
  1. Among the **eight fixed canonical coordinate projections** of
     `Herm_2(Z[j])`, `c_1 = coeff_j((H-R)_01)` is the unique coordinate that
     extracts `+sigma` on the prepared loop (this is a coordinate-choice
     statement, not uniqueness over all integer linear functionals, since
     `-c_2`, `c_0 + 3 c_1`, and `c_1 + t(5 a_0 + 9 a_1)` also evaluate to
     `sigma` on the loop).
  2. Among zero-sum integer vectors `ell in Z^5 \ {0}`, minimal Euclidean norm
     `||ell||_2^2 = 2` selects the 20 signed pair dipoles `e_r - e_s`;
     selecting the marked support `{0,1}` and orientation fixes
     `ell = (1,-1,0,0,0)`.
  3. Preserving the exact 2-adic numerator parity `P_n == P_n^free (mod 2)` on
     canonical words where `P_1 == ell (mod 2)` requires an even integer
     forcing factor `kappa in 2 Z_>0`, with minimal positive choice `kappa = 2`.
- **All-counter primitive denominator and Lorentzian signature (`B3-B4`):**
  For all ten canonical words and `a in {-1,0,+1}`, the least common denominator
  of `h_n = P_n / (2 * 324^(n-1))` is `d_n = 2 * 324^(n-1)`. Using the true
  uniform source bound `|chi_1| <= 1`, `|chi_n| <= 6` (`n >= 2`), the zero-sum
  response bound is

      ||h_n - h_n^free||_inf < 1645 / 209304 < 1 / 125,

  which combines with the canonical free K1 bound to prove
  `-299/500 < h_n(r) < 499/500`, Lorentz signature `(-,+,+,+)`, and
  `det g_n(r) < -999/250000 < 0` for all `n >= 1`.
- **Mixed variational property (`B5`):** The frozen action `A_rec` in `PROOF.md`
  section 5 has a single scalar source variable `chi_n` (with negative source
  kinetic term) and constant `f = a + beta(w)`. Its exact source partial
  derivative is

      dA_rec / d(chi_n) = (chi_{n+1} - chi_n + chi_{n-1} - f) + <ell, h_n> / 324^n
                        = r_n + tau_n.

  On the selected trajectories `r_n = 0`, leaving a **generally nonzero
  continuous source gradient** `dA_rec / d(chi_n) = tau_n` (for example, at
  word `0010`, `a=0`, `n=2`, `tau_2 = 1/209952 != 0`). What holds and is checked
  by the 720 executable tests is:
  1. Exact continuous stationarity with respect to all metric, lapse, and shift
     components evaluated on the TT representative (`600` reduced TT central
     differences vanish); and
  2. For each single-step integer shift `chi_n -> chi_n + k` (`k in Z \ {0}`)
     with neighboring `chi` values held fixed,

         A_rec(chi) - A_rec(chi + k e_n) = k^2 / 2 - k * tau_n > 0

     because `|tau_n| < 1/162 < 1/2` (`120` checks). This is coordinatewise
     single-integer optimality with fixed neighbors, not continuous source
     stationarity and not optimality over multi-step compact integer
     perturbations (e.g., adding `+1` at three consecutive steps changes `A_rec`
     by `+1/2 + tau_{n-1} + tau_n + tau_{n+1} > 13/27 > 0`). Furthermore,
     because both initial slices `n=0,1` are fixed by initial data, genuine
     interior variations start at `n=2`, while the `n=1` equation holds as the
     declared initial recurrence identity.

### Explicit errata in the frozen `PROOF.md` and `PREREG.md`

1. **Off-shell source derivative sign (`PROOF.md` lines 627-629, `PREREG.md` lines 306-308):**
   The printed off-shell formula has the wrong sign on `r_n = chi_{n+1} - chi_n + chi_{n-1} - f`.
   The correct derivative is `r_n + tau_n` (on-shell `r_n = 0`, where both match `tau_n`).
2. **Spectrum of `L` (`PROOF.md` section 3.3):**
   `PROOF.md` prints `(235 +/- 36*sqrt(5))/324`; the true nonzero eigenvalues of
   `L = (648 I - C)/324` on `1^perp` are `(235 +/- 18*sqrt(5))/324`. Both lie in
   `(2/5, 1)`, so the conservative Green norm bound `5/2` and the response bound
   `1645/209304 < 1/125` remain intact.
3. **Oscillator summation (`PROOF.md` lines 321-326):**
   The printed telescoping identity is algebraically false; the six-periodic
   formula `chi_n = a*(1,2,2,1,0,0)_n + beta(w)*(0,1,2,2,1,0)_n` follows by
   adding the autonomous source component `chi_n^auto = a*(1,2,2,1,0,0)_n`
   (`chi_1^auto = a`, `chi_2^auto = 2a`) to the `beta`-driven impulse response
   `q_n = beta(w)*(0,1,2,2,1,0)_n` satisfying the second-order initial-value
   recurrence `q_{t+1} - q_t + q_{t-1} = beta(w) * delta_{t,1}` with `q_0 = q_1 = 0`.
4. **Detector norm and `P_2` norm arithmetic (`PROOF.md` section 4.1):**
   `N(D_0) = 4` (not `6`), `N(A^-1 D_0) = 14` (not `16`), and the Euclidean
   squared norms of `P_2` for word `0010` (free / minus / plus) are `344982`,
   `343694`, and `346286` (rather than two offsetting `+2` typos in `PROOF.md`).
   The executable energy prefixes and sharp banks `344409, 347059` are exact.
5. **Vector parity wording (`PREREG.md` B2.3):**
   Because `sum_r ell_r = 0`, odd forcing changes the vector residue
   `P_n (mod 2)` rather than the parity of the scalar coordinate sum.
6. **Withdrawal of `PROOF.md` section 3.2 (unproved secular-resonance no-go):**
   Section 3.2 of `PROOF.md` is withdrawn as a theorem. Replacing `Phi(P,Q)` by
   `<ell, P_n>` accumulates `a + sum_{t=1}^n <ell, P_t>`, an upper Green bound
   exceeding a threshold does not prove a lower bound, reduction modulo 2 does
   not extend as a ring homomorphism to `Z[1/324]`, and the exact ready-source
   norm is `294 chi^4 + 52 chi^2 + 4`.

True continuous joint stationarity (`dA/dh = 0` and `dA/dchi = 0` with sustained
every-step feedback) is achieved in the separate successor probe
`P-INTEGER-JOINT-VARIATION-1` (Draft PR #1646, issue #1645).
