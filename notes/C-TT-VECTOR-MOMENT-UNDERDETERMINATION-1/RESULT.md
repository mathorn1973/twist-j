# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 result

Incubation candidate. No authority. Nothing here promotes anything.
Parent `TT-VECTOR-STATE-NORMALIZATION` stays `[O]` / STOP and is untouched.

Date 2026-08-17. Prereg frozen and hashed before first execution.

## Verdict

```text
S1  fourth-moment separation           candidate-T   no falsifier fired
S2  fixed-modulus Wick no-go           candidate-T   no falsifier fired
S3  four-fold trichotomy, control      candidate-T   no falsifier fired
A1  amplification, six-member family   candidate-T   post-freeze, disclosed
parent TT-VECTOR-STATE-NORMALIZATION   [O] / STOP    unchanged
```

Verifier: 63 of 63 gates PASS, exit 0, empty stderr.
Breaker: 13 of 13 gates PASS, exit 0, empty stderr, zero breaks found.

## Pins

```text
PREREG.md   sha256 091ef70b0b0f65247afab229c1d4a8a9ade7ccdaa9a0009de6f26a052a7d519d  11477 B
verify.py   sha256 68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c  13398 B
breaker.py  sha256 6fc905cec73a5bc3607b384723ea0d25eaf6c91a17828b64b64075c891bcff43   9112 B
EXPECTED.txt sha256 d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6  4313 B
BREAK.txt   sha256 0ac5a53d4046a123d666410004e6bc9545c942ec38e98ed88c950d866301064d   1064 B
```

The PREREG and verifier hashes above were recorded before the verifier was
executed for the first time. An earlier shell invocation returned 127 from
`/bin/sh` because the `time` builtin was absent; Python was never entered and
no output was produced, so the first execution of the verifier is the one
reported here.

## Environment

```text
platform      Ubuntu 24.04 container, Linux 6.18.5
architecture  x86_64
python        3.12.3
env           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
verify        5 seconds, executed 3 times, byte-identical stdout each time
breaker       4 seconds
```

ONE LEG ONLY. This is a single architecture. The contract requires two
architectures with byte-identical stdout, and a computation-only claim on two
legs of the same architecture stays at most C. The candidate labels above are
therefore carried by the written proofs below, not by the run; the verifier
audits those proofs at complete finite scope. The public child probe must
still run the local aarch64 leg and the GitHub x86_64 check.

## Currency gate, run in this session

```text
clone         github.com/mathorn1973/twist-j, main
HEAD          4020c5373453ef4b8466a8738337be187fc238b6
STATE         ACTIVE, CANON Public Canon v50
TAG           canon-v50 -> 6b40d54831d9204a5bee9277177b4de1dae8b529, ancestor of HEAD
CONTENT       b68c60c57cfd0b1e655b6fc4d5496a333a249fdf, ancestor of HEAD
SHA256SUMS    5 of 5 OK
CANON.md      240724 B, sha256 f99f5eeb42db3e9d40bc6a46f716aa98d7af1925b66989406e0b3671ab43a9fe
              agrees with STATUS.md
probes/       no directory matching this candidate; no collision
GATES.tsv     10 rows, none owning this normalization
NORMATIVE.tsv TT-SQUARING-DECODER D NOT_APPLICABLE, POL-READ D NOT_APPLICABLE,
              TT-VECTOR-STATE-NORMALIZATION O NOT_APPLICABLE, all gate_ids empty
```

The gate was run independently in this session and is not taken on report.

## Proofs

The status is carried by these, in `Q(zeta_5)`, `z = zeta_5`, `X = Z/5`,
`a = 1`. Write a monomial as `M = prod_x v_x^{p_x} conj(v_x)^{q_x}`, total
degree `d = sum_x (p_x + q_x)`, net exponents `n_x = p_x - q_x`.

### Lemma 0, closed forms

Under `A`, independence over sites and orthogonality of characters of `Z/5`
give `E_A[M] = prod_x [n_x = 0 mod 5]`.

Under `B_m`, `M = z^{t_0 S} z^{m W} prod_x eps_x^{p_x + q_x}` with
`S = sum_x n_x` and `W = sum_x x n_x`. Averaging over `t_0` gives
`[S = 0 mod 5]`, averaging over `eps` gives `prod_x [p_x + q_x even]`, and the
survivor is `z^{m W mod 5}`.

### S1(i)

Take `(p, q)` with a single `v_x`: `n_x = 1`, so `E_A = 0` and `S = 1`, so
`E_{B_0} = 0`. Take `v_x conj(v_y)`: for `x = y`, `n = 0` everywhere, both
give 1; for `x != y`, `n_x = 1` so `E_A = 0`, and the parity at `x` is odd so
`E_{B_0} = 0`. Take `v_x v_y`: `x = y` gives `n_x = 2`, so `E_A = 0`, and
`S = 2`, so `E_{B_0} = 0`; `x != y` gives `E_A = 0` and `S = 2`, so
`E_{B_0} = 0`. Hence mean 0, `C = delta`, `P = 0` under both, and the spectra
follow.

### S1(ii), no separation below degree 4

Case (a), some `p_x + q_x` odd. Then `E_{B_0} = 0`. If `E_A = 1` then
`n_x = 0 mod 5` for every `x`; since `|n_x| <= d <= 3 < 5` this forces
`n_x = 0`, hence `p_x = q_x` and `p_x + q_x` even for every `x`, a
contradiction. So `E_A = 0` as well.

Case (b), every `p_x + q_x` even. Then `d` is even, so `d` is 0 or 2. For
`d = 0` both are 1. For `d = 2` exactly one site carries weight 2, with
`(p_x, q_x)` one of `(2,0)`, `(1,1)`, `(0,2)`. For `(1,1)`: `n = 0`
everywhere, so `E_A = 1`, and `S = 0` with even parity, so `E_{B_0} = 1`. For
`(2,0)` and `(0,2)`: `n_x = +2` or `-2`, so `E_A = 0`, and `S = +2` or `-2`,
not `0 mod 5`, so `E_{B_0} = 0`. Equal in every case. Linearity of
expectation extends this from monomials to all polynomials of degree at most
3, in particular to every quadratic `Q(v, conj(v))`. QED

### S1(iii), the squared image

Under `A`, `w_x = z^{2 t_x}` and `t -> 2t` is a bijection of `Z/5`, so
`(w_x)` is again iid uniform on the fifth roots of unity and
`C^w_{xy} = delta_{xy}`, whence `S_w(k) = 1` for every `k`. Under `B_0`,
`eps_x^2 = 1`, so `w_x = z^{2 t_0}` is constant in `x` and
`C^w_{xy} = E[z^{2 t_0} z^{-2 t_0}] = 1` for all `x, y`, whence
`S_w(k) = sum_r z^{-k r} = 5 delta_{k,0}`. In both cases
`E[w_x w_y] = E[z^{4 t}]` type terms vanish, so `Pi_w = 0`. QED

### S1(iv), the separator set at degree 4 is exactly 20 monomials

At `d = 4`, if `E_A = 1` then `|n_x| <= 4 < 5` forces `n_x = 0` for every `x`,
hence `p_x = q_x`, hence every parity even and `S = 0`, hence `E_{B_0} = 1`.
So `E_A = 1` implies `E_{B_0} = 1`, and every separator has `E_A = 0` and
`E_{B_0} = 1`. Such a separator has every `p_x + q_x` even, `S = 0 mod 5`, and
not every `n_x` zero. With `d = 4` and all parities even, either one site
carries 4 or two distinct sites carry 2 each.

One site carries 4: `(4,0)`, `(3,1)`, `(2,2)`, `(1,3)`, `(0,4)` give
`S = 4, 2, 0, -2, -4`. Only `(2,2)` has `S = 0 mod 5`, and it has `n = 0`
everywhere, so it is not a separator.

Two sites `x != y` carry 2 each: at each the net is in `{+2, 0, -2}`, and
`|S| <= 4`, so `S = 0 mod 5` forces `S = 0`. The pairs summing to zero are
`(0,0)`, excluded because all nets vanish, and `(+2,-2)` and `(-2,+2)`. Those
are exactly `v_x^2 conj(v_y)^2` over ordered pairs `x != y`, which is
`5 * 4 = 20` monomials, and the two orientations coincide as a set.

Together with S1(ii) the minimal separating degree is exactly 4. QED

### S2, fixed modulus excludes the Wick closure

Let `|v_x|^2 = a^2` almost surely with `a > 0`, `E[v_x] = 0`,
`P_{xx} = E[v_x^2] = 0`. Then `E[|v_x|^4] = E[(a^2)^2] = a^4` exactly, since
the random variable `|v_x|^2` is the constant `a^2`. The Isserlis closure for
a mean-zero Gaussian field gives
`E[v_x^2 conj(v_x)^2] = P_{xx} conj(P_{xx}) + 2 C_{xx}^2 = 0 + 2 a^4`.
Equality would need `a^4 = 2 a^4`, that is `a = 0`, contrary to `a > 0`. The
fourth cumulant is therefore `K_{xx} = a^4 - 2 a^4 = -a^4`, never zero for
positive scale. No deterministic-modulus law is Gaussian, and no Wick or
Gaussian boundary condition can be imposed on the vector doublet while the
pointwise modulus is held fixed. QED

### S3, the trichotomy

`(rho_u v)_x = v_{u^{-1} x} = z^{t_0} eps_{u^{-1} x} z^{m u^{-1} x}`. The
field `(eps_{u^{-1} x})_x` has the same law as `(eps_x)_x`, so
`rho_u B_m = B_{m u^{-1}}`. The exponent vector of a `B_m` configuration
determines `m` as `e_1 - e_0`, so `B_m != B_{m'}` for `m != m'`. Hence
`rho_u B_m = B_m` for all `u` if and only if `m = 0`. `B_m` with `m != 0` has
`C^w_{r,0} = z^{2 m r}` and therefore `S_w(k) = 5 delta_{k, 2m}`, an
arbitrary peak, but is not `rho`-invariant. The uniform mixture over
`m` in `{1,2,3,4}` is `rho`-invariant because `rho_u` permutes those four
laws, and its spectrum is `(5/4)(1 - delta_{k,0})`. QED

## A1, amplification found by the breaker, disclosed as post-freeze

BRK-5 established, and the same proof of S1(ii) gives directly, that every
`B_m` for `m` in `Z/5`, not only `B_0`, shares every expectation of every
monomial of total degree at most 3 with `A`. Proof: in case (a) both sides are
0 as before; in case (b) with `d = 2`, `(1,1)` at site `x` has `W = 0` so the
survivor is `z^0 = 1` for every `m`, and `(2,0)` and `(0,2)` have
`S = +2, -2`, so both vanish for every `m`.

So the underdetermination family is not a pair. It contains at least the six
laws `A`, `B_0`, `B_1`, `B_2`, `B_3`, `B_4` and every mixture of them, all
sharing identical mean, `C`, `P`, `S_v`, `Pi_v` and every polynomial
expectation up to degree 3, while `S_w` ranges over `1`, `5 delta_{k,0}`,
`5 delta_{k,2}`, `5 delta_{k,4}`, `5 delta_{k,1}`, `5 delta_{k,3}` and their
convex hull.

This was not in the frozen statement. It is labelled candidate-T on its proof
and disclosed here rather than folded back into S1 to S3. If the child probe
wants it, it must be preregistered explicitly in the public PREREG, not
imported from this record.

## What did not fire, and one honest weakness

None of `F1` to `F8` fired. Every gate is an exact equality over `Q(zeta_5)`
or an exact set equality; no threshold exists that could have been moved.

Weakness to disclose in the child probe: the BRK-5 peak sub-check counts
contributions on the rational line rather than computing the full field
element, so on its own it identifies the peak by a maximum and not by an
exact spectrum. The exact spectra of every `B_m` and of the mixture are
computed in full over `Q(zeta_5)` in the verifier, gates
`B1..B4.S_w.equals.5.delta.k.*` and `Bmix.S_w.equals.5over4.off.zero`, so the
claim does not rest on the breaker sub-check. The sub-check is corroboration,
not evidence.

## Consequence for the parent, stated without inflation

The parent asks for a public vector-doublet normalization yielding a numerical
`r_T(k)`. This candidate does not supply one and does not close the parent in
either direction. What it does supply is a sharp obstruction, exhibited rather
than argued: fixing the mean, the two-point covariance, the pseudo-covariance
and every polynomial functional through degree 3 leaves `S_w` completely free
across the whole family above. Whatever the parent eventually freezes, it must
freeze fourth-moment data, or the complete state, or an explicit non-Gaussian
closure rule; and by S2 it cannot reach for a Wick or Gaussian boundary while
holding the pointwise modulus fixed. That narrows the repair space. It does
not close the point.

The parent remains `[O]` / STOP. No gate is created. `canon/GATES.tsv` is not
touched. `w = v^2` is an `L1` algebraic map here and `S_w` is the power
spectrum of the squared image, not a tensor spectrum and not `r_T(k)`.
